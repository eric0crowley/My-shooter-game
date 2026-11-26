# `TouchControlPanel.SystemTouchEventData` — TypeDefIndex 5044

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x10` | `Vector2` | `pos` |
| `0x18` | `Camera` | `cam` |
| `0x20` | `int` | `id` |
| `0x24` | `bool` | `isMouseEvent` |
| `0x28` | `int` | `touchId` |

## `TouchControlPanel.SystemTouchEventData.ctor` — RVA `0xc551c0`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public void .ctor() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static ulong TouchControlPanel_SystemTouchEventData_ctor_RVAc551c0(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x1 = 0x0UL;
        return RuntimeCalls.InvokeDirect(0x1589338UL /* metadata target: Object.ctor */);
        return default(ulong);
    }
```
