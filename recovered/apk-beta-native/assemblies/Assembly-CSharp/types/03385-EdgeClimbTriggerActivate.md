# `EdgeClimbTriggerActivate` — TypeDefIndex 3385

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x20` | `BoxCollider` | `triggerToActivate` |

## `EdgeClimbTriggerActivate.OnTriggerEnter` — RVA `0xc95404`

- Lift status: **exact**; input span: 32 bytes; span to next metadata RVA: 32 bytes.
- Metadata signature: `private void OnTriggerEnter(Collider other) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=4 (informational only).

```csharp
public static ulong EdgeClimbTriggerActivate_OnTriggerEnter_RVAc95404(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x30 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL))), x30);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x20UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC95420;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x2 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0x17CF938UL /* metadata target: Collider.set_enabled */);
        label_0xC95420:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        return default(ulong);
    }
```

## `EdgeClimbTriggerActivate.ctor` — RVA `0xc95424`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public void .ctor() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static ulong EdgeClimbTriggerActivate_ctor_RVAc95424(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x1 = 0x0UL;
        return RuntimeCalls.InvokeDirect(0x1796274UL /* metadata target: MonoBehaviour.ctor */);
        return default(ulong);
    }
```
