# `TouchGestureConfig` — TypeDefIndex 5095

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x10` | `int` | `maxTapCount` |
| `0x14` | `bool` | `cleanTapsOnly` |
| `0x15` | `bool` | `detectLongPress` |
| `0x16` | `bool` | `detectLongTap` |
| `0x17` | `bool` | `endLongPressWhenMoved` |
| `0x18` | `bool` | `endLongPressWhenSwiped` |
| `0x1C` | `TouchGestureConfig.DirMode` | `dirMode` |
| `0x20` | `DirectionState.OriginalDirResetMode` | `swipeOriginalDirResetMode` |
| `0x24` | `TouchGestureConfig.DirConstraint` | `swipeConstraint` |
| `0x28` | `TouchGestureConfig.DirConstraint` | `swipeDirConstraint` |
| `0x2C` | `TouchGestureConfig.DirConstraint` | `scrollConstraint` |

## `TouchGestureConfig.ctor` — RVA `0xc61ab8`

- Lift status: **exact**; input span: 40 bytes; span to next metadata RVA: 40 bytes.
- Metadata signature: `public void .ctor() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=4 (informational only).

```csharp
public static ulong TouchGestureConfig_ctor_RVAc61ab8(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x8UL))), x19);
        x1 = 0x0UL;
        x19 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x1589338UL /* metadata target: Object.ctor */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x19) + (0x10UL))), unchecked((uint)(x8)));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x14UL))), unchecked((byte)(unchecked((uint)(x8)))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x19) + (0x20UL))), unchecked((uint)(x8)));
        x30 = RuntimeMemory.ReadU64(sp);
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return x0;
        return default(ulong);
    }
```
