# `SuperTouchZone.EmulatedFingerObject` — TypeDefIndex 5029

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x48` | `Vector2` | `emuPos` |
| `0x50` | `SuperTouchZone` | `parentZone` |

## `SuperTouchZone.EmulatedFingerObject.ctor` — RVA `0xc4d010`

- Lift status: **exact**; input span: 44 bytes; span to next metadata RVA: 44 bytes.
- Metadata signature: `public void .ctor(SuperTouchZone parentZone) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=6 (informational only).

```csharp
public static ulong SuperTouchZone_EmulatedFingerObject_ctor_RVAc4d010(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x30 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        x19 = x1;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC4D03CUL /* metadata target: TouchObject.ctor */, x0, x1, x2, x3);
        RuntimeMemory.WriteU64(unchecked((ulong)((x20) + (0x50UL))), x19);
        x0 = x20;
        x1 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0xB7D8D0UL);
        return default(ulong);
    }
```
