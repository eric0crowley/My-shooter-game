# `TouchControl.HitPool.TouchControlFilterFunc` — TypeDefIndex 5041

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## `TouchControl.HitPool.TouchControlFilterFunc.ctor` — RVA `0xc53a78`

- Lift status: **exact**; input span: 264 bytes; span to next metadata RVA: 264 bytes.
- Metadata signature: `public void .ctor(object object, IntPtr method) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=33 (informational only).

```csharp
public static ulong TouchControl_HitPool_TouchControlFilterFunc_ctor_RVAc53a78(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12925624 = default(uint);
        uint __arm64_flags_right_12925624 = default(uint);
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
            goto label_0xC53ACC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC53AB8UL);
        }
        __arm64_flags_left_12925624 = unchecked((uint)(x22));
        __arm64_flags_right_12925624 = unchecked((uint)0x1UL);
        if ((!((unchecked((uint)((__arm64_flags_left_12925624) - (__arm64_flags_right_12925624))) == unchecked((uint)0x0UL)))))
        {
            goto label_0xC53AD4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0xA29000UL;
        x8 = unchecked((ulong)((x8) + (0xA68UL)));
        goto label_0xC53B48;
        label_0xC53ACC:
        ;
        if ((unchecked((uint)(x22)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC53AE8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC53AD0UL);
        }
        if ((x21 == 0x0UL))
        {
            goto label_0xC53B68;
        }
        else
        {
            goto label_0xC53AD4;
        }
        label_0xC53AD4:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x10UL))));
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x20UL))));
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x18UL))), x8);
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x40UL))), x9);
        goto label_0xC53B4C;
        label_0xC53AE8:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x70UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC53B18;
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
            goto label_0xC53B24;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC53B08UL);
        }
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC53B34;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0xA29000UL;
        x8 = unchecked((ulong)((x8) + (0xB64UL)));
        goto label_0xC53B48;
        label_0xC53B18:
        ;
        x8 = 0xA29000UL;
        x8 = unchecked((ulong)((x8) + (0xA48UL)));
        goto label_0xC53B48;
        label_0xC53B24:
        ;
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC53B40;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0xA29000UL;
        x8 = unchecked((ulong)((x8) + (0xAA4UL)));
        goto label_0xC53B48;
        label_0xC53B34:
        ;
        x8 = 0xA29000UL;
        x8 = unchecked((ulong)((x8) + (0xB28UL)));
        goto label_0xC53B48;
        label_0xC53B40:
        ;
        x8 = 0xA29000UL;
        x8 = unchecked((ulong)((x8) + (0xA78UL)));
        goto label_0xC53B48;
        label_0xC53B48:
        ;
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x18UL))), x8);
        goto label_0xC53B4C;
        label_0xC53B4C:
        ;
        x8 = 0xA29000UL;
        x8 = unchecked((ulong)((x8) + (0x9F4UL)));
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x38UL))), x8);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        label_0xC53B68:
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

## `TouchControl.HitPool.TouchControlFilterFunc.Invoke` — RVA `0xc53b80`

- Lift status: **exact**; input span: 20 bytes; span to next metadata RVA: 20 bytes.
- Metadata signature: `public virtual bool Invoke(TouchControl c) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=4 (informational only).

```csharp
public static ulong TouchControl_HitPool_TouchControlFilterFunc_Invoke_RVAc53b80(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong x8 = default(ulong);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x40UL))));
        x3 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x18UL))));
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x28UL))));
        x0 = x8;
        return RuntimeCalls.InvokeIndirect(x3);
        return default(ulong);
    }
```

## `TouchControl.HitPool.TouchControlFilterFunc.BeginInvoke` — RVA `0xc53b94`

- Lift status: **exact**; input span: 32 bytes; span to next metadata RVA: 32 bytes.
- Metadata signature: `public virtual IAsyncResult BeginInvoke(TouchControl c, AsyncCallback callback, object object) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=4 (informational only).

```csharp
public static ulong TouchControl_HitPool_TouchControlFilterFunc_BeginInvoke_RVAc53b94(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x30 = default(ulong);
        sp = unchecked((ulong)((sp) - (0x20UL)));
        RuntimeMemory.WritePtr(unchecked((ulong)((unchecked((ulong)((sp) + (0x8UL)))) + (0x0UL))), 0x0UL);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x8UL)))) + (0x8UL))), x30);
        RuntimeMemory.WriteU64(sp, x1);
        x1 = sp;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8E0UL, x0, x1, x2, x3);
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        return x0;
        return default(ulong);
    }
```

## `TouchControl.HitPool.TouchControlFilterFunc.EndInvoke` — RVA `0xc53bb4`

- Lift status: **exact**; input span: 40 bytes; span to next metadata RVA: 40 bytes.
- Metadata signature: `public virtual bool EndInvoke(IAsyncResult result) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=4 (informational only).

```csharp
public static uint TouchControl_HitPool_TouchControlFilterFunc_EndInvoke_RVAc53bb4(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x30 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL))), x30);
        x0 = x1;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8E4UL, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            label_0xC53BD8:
            ;
            x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        }
        else
        {
            x0 = RuntimeCalls.InvokeDirect(0xB7DA68UL, x0, x1, x2, x3);
            x0 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(x0)))));
            x30 = RuntimeMemory.ReadU64(sp);
            return unchecked((uint)(x0));
        }
        return default(uint);
    }
```
