# `InputRig.NamedConfigElement` — TypeDefIndex 5002

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x10` | `string` | `name` |

## `InputRig.NamedConfigElement.ctor` — RVA `0xc3f634`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public void .ctor() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static ulong InputRig_NamedConfigElement_ctor_RVAc3f634(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x1 = 0x0UL;
        return RuntimeCalls.InvokeDirect(0x1589338UL /* metadata target: Object.ctor */);
        return default(ulong);
    }
```

## `InputRig.NamedConfigElement.Reset` — RVA `0xc427d8`

- Lift status: **exact**; input span: 4 bytes; span to next metadata RVA: 4 bytes.
- Metadata signature: `public virtual void Reset() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=0 (informational only).

```csharp
public static ulong InputRig_NamedConfigElement_Reset_RVAc427d8(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        return x0;
        return default(ulong);
    }
```

## `InputRig.NamedConfigElement.Update` — RVA `0xc427dc`

- Lift status: **exact**; input span: 4 bytes; span to next metadata RVA: 4 bytes.
- Metadata signature: `public virtual void Update(InputRig rig) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=0 (informational only).

```csharp
public static ulong InputRig_NamedConfigElement_Update_RVAc427dc(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        return x0;
        return default(ulong);
    }
```
