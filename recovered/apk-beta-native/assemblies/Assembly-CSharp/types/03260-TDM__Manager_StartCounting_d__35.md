# `__TDM__Manager.<StartCounting>d__35` — TypeDefIndex 3260

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x10` | `int` | `<>1__state` |
| `0x18` | `object` | `<>2__current` |
| `0x20` | `__TDM__Manager` | `<>4__this` |

## `__TDM__Manager.<StartCounting>d__35.ctor` — RVA `0xc6c22c`

- Lift status: **exact**; input span: 40 bytes; span to next metadata RVA: 40 bytes.
- Metadata signature: `public void .ctor(int <>1__state) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=5 (informational only).

```csharp
public static ulong TDM__Manager_StartCounting_d__35_ctor_RVAc6c22c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
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

## `__TDM__Manager.<StartCounting>d__35.Dispose` — RVA `0xc6cebc`

- Lift status: **exact**; input span: 4 bytes; span to next metadata RVA: 4 bytes.
- Metadata signature: `private void System.IDisposable.Dispose() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=0 (informational only).

```csharp
public static ulong TDM__Manager_StartCounting_d__35_Dispose_RVAc6cebc(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        return x0;
        return default(ulong);
    }
```

## `__TDM__Manager.<StartCounting>d__35.MoveNext` — RVA `0xc6cec0`

- Lift status: **exact**; input span: 756 bytes; span to next metadata RVA: 756 bytes.
- Metadata signature: `private bool MoveNext() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=118 (informational only).

```csharp
public static uint TDM__Manager_StartCounting_d__35_MoveNext_RVAc6cec0(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13029136 = default(uint);
        uint __arm64_flags_left_13029144 = default(uint);
        uint __arm64_flags_left_13029440 = default(uint);
        uint __arm64_flags_right_13029136 = default(uint);
        uint __arm64_flags_right_13029144 = default(uint);
        uint __arm64_flags_right_13029440 = default(uint);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
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
        x20 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x346UL))))))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC6CF08;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x3E8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x490UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x498UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x346UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC6CF08;
        label_0xC6CF08:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x10UL))))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x20UL))));
        __arm64_flags_left_13029136 = unchecked((uint)(x8));
        __arm64_flags_right_13029136 = unchecked((uint)0x2UL);
        if ((unchecked((uint)((__arm64_flags_left_13029136) - (__arm64_flags_right_13029136))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC6D010;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC6CF18UL)));
        }
        __arm64_flags_left_13029144 = unchecked((uint)(x8));
        __arm64_flags_right_13029144 = unchecked((uint)0x1UL);
        if ((unchecked((uint)((__arm64_flags_left_13029144) - (__arm64_flags_right_13029144))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC6D02C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC6CF20UL)));
        }
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC6D19C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)(unchecked((uint)(0xFFFFFFFFFFFFFFFFUL))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x19) + (0x10UL))), unchecked((uint)(x8)));
        if ((x22 == 0x0UL))
        {
            goto label_0xC6D1B0;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0xC8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC6D1B0;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794CD0UL /* metadata target: GameObject.SetActive */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0xD0UL))));
        x20 = unchecked((ulong)((x22) + (0xB8UL)));
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1545824UL /* metadata target: Int32.ToString */, x0, x1, x2, x3);
        x23 = 0x1A8D000UL;
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0x498UL))));
        x1 = x0;
        x2 = 0x0UL;
        x8 = RuntimeMemory.ReadU64(x23);
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0x13ED2C8UL /* metadata target: String.Concat */, x0, x1, x2, x3);
        if ((x21 == 0x0UL))
        {
            goto label_0xC6D1B0;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(x21);
        x1 = x0;
        x0 = x21;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x5E8UL))));
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x5F0UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0xD8UL))));
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1545824UL /* metadata target: Int32.ToString */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x23);
        x1 = x0;
        x2 = 0x0UL;
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0x13ED2C8UL /* metadata target: String.Concat */, x0, x1, x2, x3);
        if ((x21 == 0x0UL))
        {
            goto label_0xC6D1B0;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(x21);
        x1 = x0;
        x0 = x21;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x5E8UL))));
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x5F0UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x3E8UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x8 = 0x432000UL;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x378UL))))), 0));
        x1 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x1799B00UL /* metadata target: WaitForSeconds.ctor */, x0, x1, x2, x3);
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x18UL))), x20);
        x0 = x19;
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x19) + (0xFFFFFFFFFFFFFFF8UL))), unchecked((uint)(x0)));
        goto label_0xC6D1A0;
        label_0xC6D010:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(0xFFFFFFFFFFFFFFFFUL))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x19) + (0x10UL))), unchecked((uint)(x8)));
        if ((x22 == 0x0UL))
        {
            goto label_0xC6D1B0;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x22) + (0xB8UL))))));
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) - (unchecked((uint)(0x1UL)))))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x22) + (0xB8UL))), unchecked((uint)(x8)));
        goto label_0xC6D038;
        label_0xC6D02C:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(0xFFFFFFFFFFFFFFFFUL))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x19) + (0x10UL))), unchecked((uint)(x8)));
        if ((x22 == 0x0UL))
        {
            goto label_0xC6D1B0;
        }
        else
        {
            goto label_0xC6D038;
        }
        label_0xC6D038:
        ;
        x20 = x22;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x20) + (0xB8UL))))));
        __arm64_flags_left_13029440 = unchecked((uint)(x8));
        __arm64_flags_right_13029440 = unchecked((uint)0x0UL);
        if (((unchecked((uint)((__arm64_flags_left_13029440) - (__arm64_flags_right_13029440))) == unchecked((uint)0x0UL)) || ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13029440) - (__arm64_flags_right_13029440))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_13029440)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13029440)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13029440) - (__arm64_flags_right_13029440))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13029440)) < unchecked((int)0x0UL)))))))
        {
            goto label_0xC6D140;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0xD0UL))));
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1545824UL /* metadata target: Int32.ToString */, x0, x1, x2, x3);
        x23 = 0x1A8D000UL;
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0x498UL))));
        x1 = x0;
        x2 = 0x0UL;
        x8 = RuntimeMemory.ReadU64(x23);
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0x13ED2C8UL /* metadata target: String.Concat */, x0, x1, x2, x3);
        if ((x21 == 0x0UL))
        {
            goto label_0xC6D1B0;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(x21);
        x1 = x0;
        x0 = x21;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x5E8UL))));
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x5F0UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0xD8UL))));
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1545824UL /* metadata target: Int32.ToString */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x23);
        x1 = x0;
        x2 = 0x0UL;
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0x13ED2C8UL /* metadata target: String.Concat */, x0, x1, x2, x3);
        if ((x21 == 0x0UL))
        {
            goto label_0xC6D1B0;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(x21);
        x1 = x0;
        x0 = x21;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x5E8UL))));
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x5F0UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0xE8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC6D1B0;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x490UL))));
        x2 = 0x0UL;
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x1767884UL /* metadata target: Animator.SetTrigger */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0xE0UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC6D1B0;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x176A5CCUL /* metadata target: AudioSource.Play */, x0, x1, x2, x3);
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x3E8UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x8 = 0x432000UL;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x378UL))))), 0));
        x1 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x1799B00UL /* metadata target: WaitForSeconds.ctor */, x0, x1, x2, x3);
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x18UL))), x20);
        x0 = x19;
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x2UL))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x19) + (0xFFFFFFFFFFFFFFF8UL))), unchecked((uint)(x8)));
        x0 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        goto label_0xC6D1A0;
        label_0xC6D140:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0xC0UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC6D1B0;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794CD0UL /* metadata target: GameObject.SetActive */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0xC8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC6D1B0;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794CD0UL /* metadata target: GameObject.SetActive */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0xC0UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC6D1B0;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794CD0UL /* metadata target: GameObject.SetActive */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0xD0UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC6D1B0;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792190UL /* metadata target: Component.get_gameObject */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC6D1B0;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794CD0UL /* metadata target: GameObject.SetActive */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xC6D19C;
        label_0xC6D19C:
        ;
        x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xC6D1A0;
        label_0xC6D1A0:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return unchecked((uint)(x0));
        label_0xC6D1B0:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, unchecked((ulong)(unchecked((uint)(x0)))), unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        return default(uint);
    }
```

## `__TDM__Manager.<StartCounting>d__35.get_Current` — RVA `0xc6d1b4`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `private object System.Collections.Generic.IEnumerator<System.Object>.get_Current() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static ulong TDM__Manager_StartCounting_d__35_get_Current_RVAc6d1b4(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x18UL))));
        return x0;
        return default(ulong);
    }
```

## `__TDM__Manager.<StartCounting>d__35.Reset` — RVA `0xc6d1bc`

- Lift status: **exact**; input span: 56 bytes; span to next metadata RVA: 56 bytes.
- Metadata signature: `private void System.Collections.IEnumerator.Reset() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=8 (informational only).

```csharp
public static ulong TDM__Manager_StartCounting_d__35_Reset_RVAc6d1bc(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
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
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x4A0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D940UL, x0, x1, x2, x3);
        x1 = x0;
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xB7DA4CUL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `__TDM__Manager.<StartCounting>d__35.get_Current` — RVA `0xc6d1f4`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `private object System.Collections.IEnumerator.get_Current() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static ulong TDM__Manager_StartCounting_d__35_get_Current_RVAc6d1f4(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x18UL))));
        return x0;
        return default(ulong);
    }
```
