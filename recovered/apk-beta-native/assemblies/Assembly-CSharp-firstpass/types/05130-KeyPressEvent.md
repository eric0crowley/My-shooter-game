# `KeyPressEvent` — TypeDefIndex 5130

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x20` | `KeyCode` | `keyCode` |
| `0x24` | `KeyPressEvent.EventType` | `eventType` |
| `0x28` | `UnityEvent` | `keyEvent` |

## `KeyPressEvent.ctor` — RVA `0xc68584`

- Lift status: **exact**; input span: 108 bytes; span to next metadata RVA: 108 bytes.
- Metadata signature: `public void .ctor() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=17 (informational only).

```csharp
public static ulong KeyPressEvent_ctor_RVAc68584(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
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
        x20 = 0x1A8D000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x31AUL))))))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x258UL))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC685B8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x258UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x31AUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC685B8;
        label_0xC685B8:
        ;
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1796274UL /* metadata target: MonoBehaviour.ctor */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x20);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x17A2850UL /* metadata target: UnityEvent.ctor */, x0, x1, x2, x3);
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x28UL))), x20);
        x0 = x19;
        x1 = x20;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeDirect(0xB7D8D0UL);
        return default(ulong);
    }
```

## `KeyPressEvent.Update` — RVA `0xc685f0`

- Lift status: **exact**; input span: 244 bytes; span to next metadata RVA: 244 bytes.
- Metadata signature: `private void Update() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=34 (informational only).

```csharp
public static uint KeyPressEvent_Update_RVAc685f0(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13010464 = default(uint);
        uint __arm64_flags_left_13010472 = default(uint);
        uint __arm64_flags_right_13010464 = default(uint);
        uint __arm64_flags_right_13010472 = default(uint);
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        x20 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x31BUL))))))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC6861C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xE0UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x31BUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC6861C;
        label_0xC6861C:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x24UL))))));
        __arm64_flags_left_13010464 = unchecked((uint)(x8));
        __arm64_flags_right_13010464 = unchecked((uint)0x2UL);
        if ((unchecked((uint)((__arm64_flags_left_13010464) - (__arm64_flags_right_13010464))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC68664;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC68628UL)));
        }
        __arm64_flags_left_13010472 = unchecked((uint)(x8));
        __arm64_flags_right_13010472 = unchecked((uint)0x1UL);
        if ((unchecked((uint)((__arm64_flags_left_13010472) - (__arm64_flags_right_13010472))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC686A8;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC68630UL)));
        }
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC686D4;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xE0UL))));
        x20 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x20UL))))));
        x0 = RuntimeMemory.ReadU64(x8);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC68650;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC6864CUL)));
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC68650;
        label_0xC68650:
        ;
        x0 = unchecked((ulong)(unchecked((uint)(x20))));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC36D34UL /* metadata target: CF2Input.GetKeyDown */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC68690;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC68660UL)));
        }
        goto label_0xC686D4;
        label_0xC68664:
        ;
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xE0UL))));
        x20 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x20UL))))));
        x0 = RuntimeMemory.ReadU64(x8);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC68680;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC6867CUL)));
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC68680;
        label_0xC68680:
        ;
        x0 = unchecked((ulong)(unchecked((uint)(x20))));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC36B94UL /* metadata target: CF2Input.GetKey */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC686D4;
        }
        else
        {
            goto label_0xC68690;
        }
        label_0xC68690:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x28UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC686E0;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x1 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        return unchecked((uint)(RuntimeCalls.InvokeDirect(0x17A29C8UL /* metadata target: UnityEvent.Invoke */)));
        label_0xC686A8:
        ;
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xE0UL))));
        x20 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x20UL))))));
        x0 = RuntimeMemory.ReadU64(x8);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC686C4;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC686C0UL)));
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC686C4;
        label_0xC686C4:
        ;
        x0 = unchecked((ulong)(unchecked((uint)(x20))));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC36EF4UL /* metadata target: CF2Input.GetKeyUp */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC68690;
        }
        else
        {
            goto label_0xC686D4;
        }
        label_0xC686D4:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return unchecked((uint)(x0));
        label_0xC686E0:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        return default(uint);
    }
```
