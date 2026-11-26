# `GamepadManager.OnDisconnectionCallback` — TypeDefIndex 4951

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## `GamepadManager.OnDisconnectionCallback.ctor` — RVA `0xc2d728`

- Lift status: **exact**; input span: 268 bytes; span to next metadata RVA: 268 bytes.
- Metadata signature: `public void .ctor(object object, IntPtr method) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=33 (informational only).

```csharp
public static ulong GamepadManager_OnDisconnectionCallback_ctor_RVAc2d728(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12769128 = default(uint);
        uint __arm64_flags_left_12769148 = default(uint);
        uint __arm64_flags_right_12769128 = default(uint);
        uint __arm64_flags_right_12769148 = default(uint);
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
            goto label_0xC2D77C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC2D768UL);
        }
        __arm64_flags_left_12769128 = unchecked((uint)(x22));
        __arm64_flags_right_12769128 = unchecked((uint)0x2UL);
        if ((!((unchecked((uint)((__arm64_flags_left_12769128) - (__arm64_flags_right_12769128))) == unchecked((uint)0x0UL)))))
        {
            goto label_0xC2D7B8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0xA29000UL;
        x8 = unchecked((ulong)((x8) + (0x7E0UL)));
        goto label_0xC2D7FC;
        label_0xC2D77C:
        ;
        __arm64_flags_left_12769148 = unchecked((uint)(x22));
        __arm64_flags_right_12769148 = unchecked((uint)0x1UL);
        if ((!((unchecked((uint)((__arm64_flags_left_12769148) - (__arm64_flags_right_12769148))) == unchecked((uint)0x0UL)))))
        {
            goto label_0xC2D7B4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x70UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC2D7CC;
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
            goto label_0xC2D7D8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC2D7A4UL);
        }
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC2D7E8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0xA29000UL;
        x8 = unchecked((ulong)((x8) + (0x8FCUL)));
        goto label_0xC2D7FC;
        label_0xC2D7B4:
        ;
        if ((unchecked((uint)(x21)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC2D81C;
        }
        else
        {
            goto label_0xC2D7B8;
        }
        label_0xC2D7B8:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x10UL))));
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x20UL))));
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x18UL))), x8);
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x40UL))), x9);
        goto label_0xC2D800;
        label_0xC2D7CC:
        ;
        x8 = 0xA29000UL;
        x8 = unchecked((ulong)((x8) + (0x7BCUL)));
        goto label_0xC2D7FC;
        label_0xC2D7D8:
        ;
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC2D7F4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0xA29000UL;
        x8 = unchecked((ulong)((x8) + (0x824UL)));
        goto label_0xC2D7FC;
        label_0xC2D7E8:
        ;
        x8 = 0xA29000UL;
        x8 = unchecked((ulong)((x8) + (0x8B0UL)));
        goto label_0xC2D7FC;
        label_0xC2D7F4:
        ;
        x8 = 0xA29000UL;
        x8 = unchecked((ulong)((x8) + (0x7F4UL)));
        goto label_0xC2D7FC;
        label_0xC2D7FC:
        ;
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x18UL))), x8);
        goto label_0xC2D800;
        label_0xC2D800:
        ;
        x8 = 0xA29000UL;
        x8 = unchecked((ulong)((x8) + (0x764UL)));
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x38UL))), x8);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        label_0xC2D81C:
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

## `GamepadManager.OnDisconnectionCallback.Invoke` — RVA `0xc2d834`

- Lift status: **exact**; input span: 20 bytes; span to next metadata RVA: 20 bytes.
- Metadata signature: `public virtual void Invoke(GamepadManager.Gamepad gamepad, GamepadManager.DisconnectionReason reason) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=4 (informational only).

```csharp
public static ulong GamepadManager_OnDisconnectionCallback_Invoke_RVAc2d834(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
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

## `GamepadManager.OnDisconnectionCallback.BeginInvoke` — RVA `0xc2d848`

- Lift status: **exact**; input span: 148 bytes; span to next metadata RVA: 148 bytes.
- Metadata signature: `public virtual IAsyncResult BeginInvoke(GamepadManager.Gamepad gamepad, GamepadManager.DisconnectionReason reason, AsyncCallback callback, object object) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=23 (informational only).

```csharp
public static ulong GamepadManager_OnDisconnectionCallback_BeginInvoke_RVAc2d848(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
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
        sp = unchecked((ulong)((sp) - (0x60UL)));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x20UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x0UL))), x24);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x8UL))), x19);
        x24 = 0x1BAB000UL;
        RuntimeMemory.WriteU32(unchecked((ulong)((sp) + (0x2CUL))), unchecked((uint)(x2)));
        x23 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x24) + (0x116UL))))))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0x128UL))));
        x19 = x4;
        x20 = x3;
        x22 = x1;
        x21 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
        }
        else
        {
            x0 = 0x1A8C000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x128UL))));
            // Likely IL2CPP class initialization helper (guarded call).
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
            RuntimeMemory.WriteU8(unchecked((ulong)((x24) + (0x116UL))), unchecked((byte)(unchecked((uint)(x8)))));
        }
        label_0xC2D898:
        ;
        x0 = RuntimeMemory.ReadU64(x23);
        x1 = unchecked((ulong)((sp) + (0x2CUL)));
        RuntimeMemory.WritePtr(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), 0x0UL);
        RuntimeMemory.WritePtr(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), 0x0UL);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x8UL))), x22);
        x0 = RuntimeCalls.InvokeDirect(0xB7DA64UL, x0, x1, x2, x3);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x10UL))), x0);
        x1 = unchecked((ulong)((sp) + (0x8UL)));
        x0 = x21;
        x2 = x20;
        x3 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8E0UL, x0, x1, x2, x3);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x50UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x40UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        return x0;
        return default(ulong);
    }
```

## `GamepadManager.OnDisconnectionCallback.EndInvoke` — RVA `0xc2d8dc`

- Lift status: **exact**; input span: 12 bytes; span to next metadata RVA: 12 bytes.
- Metadata signature: `public virtual void EndInvoke(IAsyncResult result) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=2 (informational only).

```csharp
public static ulong GamepadManager_OnDisconnectionCallback_EndInvoke_RVAc2d8dc(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x0 = x1;
        x1 = 0x0UL;
        return RuntimeCalls.InvokeDirect(0xB7D8E4UL);
        return default(ulong);
    }
```
