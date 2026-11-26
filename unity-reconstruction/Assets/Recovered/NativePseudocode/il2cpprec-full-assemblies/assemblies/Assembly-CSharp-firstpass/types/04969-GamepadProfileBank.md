# `GamepadProfileBank` — TypeDefIndex 4969

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x18` | `GamepadProfile[]` | `profiles` |

## `GamepadProfileBank.GetProfile` — RVA `0xc30b70`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public GamepadProfile GetProfile(string deviceIdentifier) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static ulong GamepadProfileBank_GetProfile_RVAc30b70(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x0 = 0x0UL;
        return x0;
        return default(ulong);
    }
```

## `GamepadProfileBank.ctor` — RVA `0xc30b78`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public void .ctor() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static ulong GamepadProfileBank_ctor_RVAc30b78(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x1 = 0x0UL;
        return RuntimeCalls.InvokeDirect(0x179634CUL /* metadata target: ScriptableObject.ctor */);
        return default(ulong);
    }
```
