# `BindingDescriptionList.NameFormatter` — TypeDefIndex 5080

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## `BindingDescriptionList.NameFormatter.ctor` — RVA `0xc5dc9c`

- Lift status: **exact**; input span: 268 bytes; span to next metadata RVA: 268 bytes.
- Metadata signature: `public void .ctor(object object, IntPtr method) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=33 (informational only).

```csharp
public static ulong BindingDescriptionList_NameFormatter_ctor_RVAc5dc9c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12967132 = default(uint);
        uint __arm64_flags_left_12967152 = default(uint);
        uint __arm64_flags_right_12967132 = default(uint);
        uint __arm64_flags_right_12967152 = default(uint);
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x22 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFD0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x19);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x2) + (0x8UL))));
        x19 = x0;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x28UL))), x2);
        x20 = x2;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x10UL))), x8);
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x20UL))), x1);
        x21 = x1;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x22 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x52UL))))))));
        x0 = x20;
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x40UL))), x19);
        x0 = RuntimeCalls.InvokeDirect(0xB7D9E4UL, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC5DCF0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC5DCDCUL);
        }
        __arm64_flags_left_12967132 = unchecked((uint)(x22));
        __arm64_flags_right_12967132 = unchecked((uint)0x2UL);
        if ((!((unchecked((uint)((__arm64_flags_left_12967132) - (__arm64_flags_right_12967132))) == unchecked((uint)0x0UL)))))
        {
            goto label_0xC5DD2C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0xA29000UL;
        x8 = unchecked((ulong)((x8) + (0xD9CUL)));
        goto label_0xC5DD70;
        label_0xC5DCF0:
        ;
        __arm64_flags_left_12967152 = unchecked((uint)(x22));
        __arm64_flags_right_12967152 = unchecked((uint)0x1UL);
        if ((!((unchecked((uint)((__arm64_flags_left_12967152) - (__arm64_flags_right_12967152))) == unchecked((uint)0x0UL)))))
        {
            goto label_0xC5DD28;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x70UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC5DD40;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D9DCUL, x0, x1, x2, x3);
        x21 = unchecked((ulong)(unchecked((uint)(x0))));
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7DF68UL, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x21))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC5DD4C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC5DD18UL);
        }
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC5DD5C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0xA29000UL;
        x8 = unchecked((ulong)((x8) + (0xEB8UL)));
        goto label_0xC5DD70;
        label_0xC5DD28:
        ;
        if ((unchecked((uint)(x21)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC5DD90;
        }
        else
        {
            goto label_0xC5DD2C;
        }
        label_0xC5DD2C:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x10UL))));
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x20UL))));
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x18UL))), x8);
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x40UL))), x9);
        goto label_0xC5DD74;
        label_0xC5DD40:
        ;
        x8 = 0xA29000UL;
        x8 = unchecked((ulong)((x8) + (0xD78UL)));
        goto label_0xC5DD70;
        label_0xC5DD4C:
        ;
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC5DD68;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0xA29000UL;
        x8 = unchecked((ulong)((x8) + (0xDE0UL)));
        goto label_0xC5DD70;
        label_0xC5DD5C:
        ;
        x8 = 0xA29000UL;
        x8 = unchecked((ulong)((x8) + (0xE6CUL)));
        goto label_0xC5DD70;
        label_0xC5DD68:
        ;
        x8 = 0xA29000UL;
        x8 = unchecked((ulong)((x8) + (0xDB0UL)));
        goto label_0xC5DD70;
        label_0xC5DD70:
        ;
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x18UL))), x8);
        goto label_0xC5DD74;
        label_0xC5DD74:
        ;
        x8 = 0xA29000UL;
        x8 = unchecked((ulong)((x8) + (0xD18UL)));
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x38UL))), x8);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        label_0xC5DD90:
        ;
        x1 = 0x449000UL;
        x1 = unchecked((ulong)((x1) + (0x23CUL)));
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB90UL, x0, x1, x2, x3);
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xB7DA4CUL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `BindingDescriptionList.NameFormatter.Invoke` — RVA `0xc5dda8`

- Lift status: **exact**; input span: 20 bytes; span to next metadata RVA: 20 bytes.
- Metadata signature: `public virtual string Invoke(InputBindingBase bind, string name) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=4 (informational only).

```csharp
public static ulong BindingDescriptionList_NameFormatter_Invoke_RVAc5dda8(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong x8 = default(ulong);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x40UL))));
        x4 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x18UL))));
        x3 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x28UL))));
        x0 = x8;
        return RuntimeCalls.InvokeIndirect(x4);
        return default(ulong);
    }
```

## `BindingDescriptionList.NameFormatter.BeginInvoke` — RVA `0xc5ddbc`

- Lift status: **exact**; input span: 40 bytes; span to next metadata RVA: 40 bytes.
- Metadata signature: `public virtual IAsyncResult BeginInvoke(InputBindingBase bind, string name, AsyncCallback callback, object object) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=6 (informational only).

```csharp
public static ulong BindingDescriptionList_NameFormatter_BeginInvoke_RVAc5ddbc(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x30 = default(ulong);
        sp = unchecked((ulong)((sp) - (0x30UL)));
        RuntimeMemory.WritePtr(unchecked((ulong)((unchecked((ulong)((sp) + (0x18UL)))) + (0x0UL))), 0x0UL);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x18UL)))) + (0x8UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x8UL)))) + (0x0UL))), x1);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x8UL)))) + (0x8UL))), x2);
        x1 = unchecked((ulong)((sp) + (0x8UL)));
        x2 = x3;
        x3 = x4;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8E0UL, x0, x1, x2, x3);
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        return x0;
        return default(ulong);
    }
```

## `BindingDescriptionList.NameFormatter.EndInvoke` — RVA `0xc5dde4`

- Lift status: **exact**; input span: 12 bytes; span to next metadata RVA: 12 bytes.
- Metadata signature: `public virtual string EndInvoke(IAsyncResult result) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=2 (informational only).

```csharp
public static ulong BindingDescriptionList_NameFormatter_EndInvoke_RVAc5dde4(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x0 = x1;
        x1 = 0x0UL;
        return RuntimeCalls.InvokeDirect(0xB7D8E4UL);
        return default(ulong);
    }
```
