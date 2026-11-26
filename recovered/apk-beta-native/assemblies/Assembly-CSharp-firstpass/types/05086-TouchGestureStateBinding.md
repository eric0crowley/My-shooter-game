# `TouchGestureStateBinding` — TypeDefIndex 5086

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x20` | `DigitalBinding` | `rawPressBinding` |
| `0x28` | `DigitalBinding` | `normalPressBinding` |
| `0x30` | `DigitalBinding` | `longPressBinding` |
| `0x38` | `DigitalBinding` | `tapBinding` |
| `0x40` | `DigitalBinding` | `doubleTapBinding` |
| `0x48` | `DigitalBinding` | `longTapBinding` |
| `0x50` | `DirectionBinding` | `normalPressSwipeDirBinding` |
| `0x58` | `DirectionBinding` | `longPressSwipeDirBinding` |
| `0x60` | `AxisBinding` | `normalPressSwipeHorzAxisBinding` |
| `0x68` | `AxisBinding` | `normalPressSwipeVertAxisBinding` |
| `0x70` | `AxisBinding` | `longPressSwipeHorzAxisBinding` |
| `0x78` | `AxisBinding` | `longPressSwipeVertAxisBinding` |
| `0x80` | `ScrollDeltaBinding` | `normalPressScrollHorzBinding` |
| `0x88` | `ScrollDeltaBinding` | `normalPressScrollVertBinding` |
| `0x90` | `ScrollDeltaBinding` | `longPressScrollHorzBinding` |
| `0x98` | `ScrollDeltaBinding` | `longPressScrollVertBinding` |
| `0xA0` | `MousePositionBinding` | `rawPressMousePosBinding` |
| `0xA8` | `MousePositionBinding` | `normalPressMousePosBinding` |
| `0xB0` | `MousePositionBinding` | `longPressMousePosBinding` |
| `0xB8` | `MousePositionBinding` | `tapMousePosBinding` |
| `0xC0` | `MousePositionBinding` | `doubleTapMousePosBinding` |
| `0xC8` | `MousePositionBinding` | `longTapMousePosBinding` |
| `0xD0` | `MousePositionBinding` | `normalPressSwipeMousePosBinding` |
| `0xD8` | `MousePositionBinding` | `longPressSwipeMousePosBinding` |
| `0xE0` | `EmuTouchBinding` | `rawPressEmuTouchBinding` |
| `0xE8` | `EmuTouchBinding` | `normalPressEmuTouchBinding` |
| `0xF0` | `EmuTouchBinding` | `longPressEmuTouchBinding` |
| `0xF8` | `JoystickStateBinding` | `normalPressSwipeJoyBinding` |
| `0x100` | `JoystickStateBinding` | `longPressSwipeJoyBinding` |

## `TouchGestureStateBinding.ctor` — RVA `0xc5e9e4`

- Lift status: **exact**; input span: 1668 bytes; span to next metadata RVA: 1668 bytes.
- Metadata signature: `public void .ctor(InputBindingBase parent) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=226 (informational only).

```csharp
public static ulong TouchGestureStateBinding_ctor_RVAc5e9e4(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x22 = default(ulong);
        ulong x23 = default(ulong);
        ulong x24 = default(ulong);
        ulong x25 = default(ulong);
        ulong x26 = default(ulong);
        ulong x27 = default(ulong);
        ulong x28 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFA0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x28);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x27);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x26);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x25);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x0UL))), x24);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x8UL))), x19);
        x28 = 0x1BAB000UL;
        x27 = 0x1A8C000UL;
        x26 = 0x1A8C000UL;
        x25 = 0x1A8C000UL;
        x24 = 0x1A8C000UL;
        x23 = 0x1A8D000UL;
        x22 = 0x1A8D000UL;
        x21 = 0x1A8C000UL;
        x27 = RuntimeMemory.ReadU64(unchecked((ulong)((x27) + (0x988UL))));
        x26 = RuntimeMemory.ReadU64(unchecked((ulong)((x26) + (0x990UL))));
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x28) + (0x2DCUL))))))));
        x25 = RuntimeMemory.ReadU64(unchecked((ulong)((x25) + (0xB18UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((x24) + (0xBE8UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0x30UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x38UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x998UL))));
        x20 = x1;
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC5EAA4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x990UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x988UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x38UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xBE8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x998UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x30UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB18UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x28) + (0x2DCUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC5EAA4;
        label_0xC5EAA4:
        ;
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1589338UL /* metadata target: Object.ctor */, x0, x1, x2, x3);
        x0 = x19;
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x10UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x18UL))), x20);
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x10UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        x0 = RuntimeMemory.ReadU64(x27);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = x19;
        x2 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC4EAA8UL /* metadata target: DigitalBinding.ctor */, x0, x1, x2, x3);
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x20UL))), x20);
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x27);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = x19;
        x2 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC4EAA8UL /* metadata target: DigitalBinding.ctor */, x0, x1, x2, x3);
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x30UL))), x20);
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x27);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = x19;
        x2 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC4EAA8UL /* metadata target: DigitalBinding.ctor */, x0, x1, x2, x3);
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x28UL))), x20);
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x27);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = x19;
        x2 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC4EAA8UL /* metadata target: DigitalBinding.ctor */, x0, x1, x2, x3);
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x38UL))), x20);
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x27);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = x19;
        x2 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC4EAA8UL /* metadata target: DigitalBinding.ctor */, x0, x1, x2, x3);
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x40UL))), x20);
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x27);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = x19;
        x2 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC4EAA8UL /* metadata target: DigitalBinding.ctor */, x0, x1, x2, x3);
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x48UL))), x20);
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x26);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = x19;
        x2 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC4EAC4UL /* metadata target: AxisBinding.ctor */, x0, x1, x2, x3);
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x60UL))), x20);
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x26);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = x19;
        x2 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC4EAC4UL /* metadata target: AxisBinding.ctor */, x0, x1, x2, x3);
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x68UL))), x20);
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x26);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = x19;
        x2 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC4EAC4UL /* metadata target: AxisBinding.ctor */, x0, x1, x2, x3);
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x70UL))), x20);
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x26);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = x19;
        x2 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC4EAC4UL /* metadata target: AxisBinding.ctor */, x0, x1, x2, x3);
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x78UL))), x20);
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x25);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = x19;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC5E460UL /* metadata target: ScrollDeltaBinding.ctor */, x0, x1, x2, x3);
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x80UL))), x20);
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x25);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = x19;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC5E460UL /* metadata target: ScrollDeltaBinding.ctor */, x0, x1, x2, x3);
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x88UL))), x20);
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x25);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = x19;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC5E460UL /* metadata target: ScrollDeltaBinding.ctor */, x0, x1, x2, x3);
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x90UL))), x20);
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x25);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = x19;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC5E460UL /* metadata target: ScrollDeltaBinding.ctor */, x0, x1, x2, x3);
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x98UL))), x20);
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x24);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x1589338UL /* metadata target: Object.ctor */, x0, x1, x2, x3);
        x0 = x20;
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x10UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x18UL))), x19);
        x1 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x25 = unchecked((ulong)(unchecked((uint)(0xFFFFFFFFFFFFFFFFUL))));
        x0 = x19;
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x10UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x20) + (0x20UL))), unchecked((uint)(x25)));
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0xE0UL))), x20);
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x24);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x1589338UL /* metadata target: Object.ctor */, x0, x1, x2, x3);
        x0 = x20;
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x10UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x18UL))), x19);
        x1 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = x19;
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x10UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x20) + (0x20UL))), unchecked((uint)(x25)));
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0xE8UL))), x20);
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x24);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x1589338UL /* metadata target: Object.ctor */, x0, x1, x2, x3);
        x0 = x20;
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x10UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x18UL))), x19);
        x1 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = x19;
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x10UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x20) + (0x20UL))), unchecked((uint)(x25)));
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0xF0UL))), x20);
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x23);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x1589338UL /* metadata target: Object.ctor */, x0, x1, x2, x3);
        x0 = x20;
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x10UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x18UL))), x19);
        x1 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0xAUL))));
        x0 = x19;
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x10UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x20) + (0x20UL))), unchecked((uint)(x8)));
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0xA0UL))), x20);
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x23);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x1589338UL /* metadata target: Object.ctor */, x0, x1, x2, x3);
        x0 = x20;
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x10UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x18UL))), x19);
        x1 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x24 = unchecked((ulong)(unchecked((uint)(0x14UL))));
        x0 = x19;
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x10UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x20) + (0x20UL))), unchecked((uint)(x24)));
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0xA8UL))), x20);
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x23);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x1589338UL /* metadata target: Object.ctor */, x0, x1, x2, x3);
        x0 = x20;
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x10UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x18UL))), x19);
        x1 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = x19;
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x10UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x20) + (0x20UL))), unchecked((uint)(x24)));
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0xB0UL))), x20);
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x23);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x1589338UL /* metadata target: Object.ctor */, x0, x1, x2, x3);
        x0 = x20;
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x10UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x18UL))), x19);
        x1 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x25 = unchecked((ulong)(unchecked((uint)(0x1EUL))));
        x0 = x19;
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x10UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x20) + (0x20UL))), unchecked((uint)(x25)));
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0xB8UL))), x20);
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x23);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x1589338UL /* metadata target: Object.ctor */, x0, x1, x2, x3);
        x0 = x20;
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x10UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x18UL))), x19);
        x1 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = x19;
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x10UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x20) + (0x20UL))), unchecked((uint)(x25)));
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0xC0UL))), x20);
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x23);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x1589338UL /* metadata target: Object.ctor */, x0, x1, x2, x3);
        x0 = x20;
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x10UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x18UL))), x19);
        x1 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = x19;
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x10UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x20) + (0x20UL))), unchecked((uint)(x25)));
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0xC8UL))), x20);
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x23);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x1589338UL /* metadata target: Object.ctor */, x0, x1, x2, x3);
        x0 = x20;
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x10UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x18UL))), x19);
        x1 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = x19;
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x10UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x20) + (0x20UL))), unchecked((uint)(x24)));
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0xD0UL))), x20);
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x23);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x1589338UL /* metadata target: Object.ctor */, x0, x1, x2, x3);
        x0 = x20;
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x10UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x18UL))), x19);
        x1 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = x19;
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x10UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x20) + (0x20UL))), unchecked((uint)(x24)));
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0xD8UL))), x20);
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x22);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = x19;
        x2 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC5C9ECUL /* metadata target: DirectionBinding.ctor */, x0, x1, x2, x3);
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x50UL))), x20);
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x22);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = x19;
        x2 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC5C9ECUL /* metadata target: DirectionBinding.ctor */, x0, x1, x2, x3);
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x58UL))), x20);
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x21);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = x19;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC5DE7CUL /* metadata target: JoystickStateBinding.ctor */, x0, x1, x2, x3);
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0xF8UL))), x20);
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x21);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = x19;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC5DE7CUL /* metadata target: JoystickStateBinding.ctor */, x0, x1, x2, x3);
        x0 = unchecked((ulong)((x19) + (0x100UL)));
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x100UL))), x20);
        x1 = x20;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x50UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x40UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))));
        x26 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x25 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x28 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x27 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0xB7D8D0UL);
        return default(ulong);
    }
```

## `TouchGestureStateBinding.CopyFrom` — RVA `0xc5f068`

- Lift status: **exact**; input span: 992 bytes; span to next metadata RVA: 992 bytes.
- Metadata signature: `public void CopyFrom(TouchGestureStateBinding b) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=129 (informational only).

```csharp
public static ulong TouchGestureStateBinding_CopyFrom_RVAc5f068(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x10 = default(ulong);
        ulong x11 = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        if ((x1 == 0x0UL))
        {
            goto label_0xC5F444;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x1) + (0x10UL))))))));
        x19 = x1;
        x20 = x0;
        RuntimeMemory.WriteU8(unchecked((ulong)((x0) + (0x10UL))), unchecked((byte)(unchecked((uint)(x8)))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC5F438;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x9 = x20;
        goto label_0xC5F090;
        label_0xC5F090:
        ;
        RuntimeMemory.WriteU8(unchecked((ulong)((x9) + (0x10UL))), unchecked((byte)(unchecked((uint)(x8)))));
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0x18UL))));
        if ((x9 != 0x0UL))
        {
            goto label_0xC5F090;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x20UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC5F444;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x20UL))));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC5C1E0UL /* metadata target: DigitalBinding.CopyFrom */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x28UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC5F444;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x28UL))));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC5C1E0UL /* metadata target: DigitalBinding.CopyFrom */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x30UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC5F444;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x30UL))));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC5C1E0UL /* metadata target: DigitalBinding.CopyFrom */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x38UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC5F444;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x38UL))));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC5C1E0UL /* metadata target: DigitalBinding.CopyFrom */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x40UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC5F444;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x40UL))));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC5C1E0UL /* metadata target: DigitalBinding.CopyFrom */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x48UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC5F444;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x48UL))));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC5C1E0UL /* metadata target: DigitalBinding.CopyFrom */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x50UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC5F444;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x50UL))));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC5CC2CUL /* metadata target: DirectionBinding.CopyFrom */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x58UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC5F444;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x58UL))));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC5CC2CUL /* metadata target: DirectionBinding.CopyFrom */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x60UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC5F444;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x60UL))));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC5B53CUL /* metadata target: AxisBinding.CopyFrom */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x68UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC5F444;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x68UL))));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC5B53CUL /* metadata target: AxisBinding.CopyFrom */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x70UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC5F444;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x70UL))));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC5B53CUL /* metadata target: AxisBinding.CopyFrom */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x78UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC5F444;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x78UL))));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC5B53CUL /* metadata target: AxisBinding.CopyFrom */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x80UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC5F444;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x80UL))));
        x0 = RuntimeCalls.InvokeDirect(0xC5E68CUL /* metadata target: ScrollDeltaBinding.CopyFrom */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x88UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC5F444;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x88UL))));
        x0 = RuntimeCalls.InvokeDirect(0xC5E68CUL /* metadata target: ScrollDeltaBinding.CopyFrom */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x90UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC5F444;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x90UL))));
        x0 = RuntimeCalls.InvokeDirect(0xC5E68CUL /* metadata target: ScrollDeltaBinding.CopyFrom */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x98UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC5F444;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x98UL))));
        x0 = RuntimeCalls.InvokeDirect(0xC5E68CUL /* metadata target: ScrollDeltaBinding.CopyFrom */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xA0UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC5F444;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xA0UL))));
        if ((x9 == 0x0UL))
        {
            goto label_0xC5F204;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x9) + (0x10UL))))))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x8) + (0x10UL))), unchecked((byte)(unchecked((uint)(x10)))));
        if ((unchecked((uint)(x10)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC5F204;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x11 = x8;
        goto label_0xC5F1F0;
        label_0xC5F1F0:
        ;
        RuntimeMemory.WriteU8(unchecked((ulong)((x11) + (0x10UL))), unchecked((byte)(unchecked((uint)(x10)))));
        x11 = RuntimeMemory.ReadU64(unchecked((ulong)((x11) + (0x18UL))));
        if ((x11 != 0x0UL))
        {
            goto label_0xC5F1F0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x9) + (0x20UL))))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x8) + (0x20UL))), unchecked((uint)(x9)));
        goto label_0xC5F204;
        label_0xC5F204:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xA8UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC5F444;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xA8UL))));
        if ((x9 == 0x0UL))
        {
            goto label_0xC5F23C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x9) + (0x10UL))))))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x8) + (0x10UL))), unchecked((byte)(unchecked((uint)(x10)))));
        if ((unchecked((uint)(x10)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC5F23C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x11 = x8;
        goto label_0xC5F228;
        label_0xC5F228:
        ;
        RuntimeMemory.WriteU8(unchecked((ulong)((x11) + (0x10UL))), unchecked((byte)(unchecked((uint)(x10)))));
        x11 = RuntimeMemory.ReadU64(unchecked((ulong)((x11) + (0x18UL))));
        if ((x11 != 0x0UL))
        {
            goto label_0xC5F228;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x9) + (0x20UL))))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x8) + (0x20UL))), unchecked((uint)(x9)));
        goto label_0xC5F23C;
        label_0xC5F23C:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xB0UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC5F444;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xB0UL))));
        if ((x9 == 0x0UL))
        {
            goto label_0xC5F274;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x9) + (0x10UL))))))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x8) + (0x10UL))), unchecked((byte)(unchecked((uint)(x10)))));
        if ((unchecked((uint)(x10)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC5F274;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x11 = x8;
        goto label_0xC5F260;
        label_0xC5F260:
        ;
        RuntimeMemory.WriteU8(unchecked((ulong)((x11) + (0x10UL))), unchecked((byte)(unchecked((uint)(x10)))));
        x11 = RuntimeMemory.ReadU64(unchecked((ulong)((x11) + (0x18UL))));
        if ((x11 != 0x0UL))
        {
            goto label_0xC5F260;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x9) + (0x20UL))))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x8) + (0x20UL))), unchecked((uint)(x9)));
        goto label_0xC5F274;
        label_0xC5F274:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xB8UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC5F444;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xB8UL))));
        if ((x9 == 0x0UL))
        {
            goto label_0xC5F2AC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x9) + (0x10UL))))))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x8) + (0x10UL))), unchecked((byte)(unchecked((uint)(x10)))));
        if ((unchecked((uint)(x10)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC5F2AC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x11 = x8;
        goto label_0xC5F298;
        label_0xC5F298:
        ;
        RuntimeMemory.WriteU8(unchecked((ulong)((x11) + (0x10UL))), unchecked((byte)(unchecked((uint)(x10)))));
        x11 = RuntimeMemory.ReadU64(unchecked((ulong)((x11) + (0x18UL))));
        if ((x11 != 0x0UL))
        {
            goto label_0xC5F298;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x9) + (0x20UL))))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x8) + (0x20UL))), unchecked((uint)(x9)));
        goto label_0xC5F2AC;
        label_0xC5F2AC:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xC0UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC5F444;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xC0UL))));
        if ((x9 == 0x0UL))
        {
            goto label_0xC5F2E4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x9) + (0x10UL))))))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x8) + (0x10UL))), unchecked((byte)(unchecked((uint)(x10)))));
        if ((unchecked((uint)(x10)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC5F2E4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x11 = x8;
        goto label_0xC5F2D0;
        label_0xC5F2D0:
        ;
        RuntimeMemory.WriteU8(unchecked((ulong)((x11) + (0x10UL))), unchecked((byte)(unchecked((uint)(x10)))));
        x11 = RuntimeMemory.ReadU64(unchecked((ulong)((x11) + (0x18UL))));
        if ((x11 != 0x0UL))
        {
            goto label_0xC5F2D0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x9) + (0x20UL))))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x8) + (0x20UL))), unchecked((uint)(x9)));
        goto label_0xC5F2E4;
        label_0xC5F2E4:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xC8UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC5F444;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xC8UL))));
        if ((x9 == 0x0UL))
        {
            goto label_0xC5F31C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x9) + (0x10UL))))))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x8) + (0x10UL))), unchecked((byte)(unchecked((uint)(x10)))));
        if ((unchecked((uint)(x10)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC5F31C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x11 = x8;
        goto label_0xC5F308;
        label_0xC5F308:
        ;
        RuntimeMemory.WriteU8(unchecked((ulong)((x11) + (0x10UL))), unchecked((byte)(unchecked((uint)(x10)))));
        x11 = RuntimeMemory.ReadU64(unchecked((ulong)((x11) + (0x18UL))));
        if ((x11 != 0x0UL))
        {
            goto label_0xC5F308;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x9) + (0x20UL))))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x8) + (0x20UL))), unchecked((uint)(x9)));
        goto label_0xC5F31C;
        label_0xC5F31C:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xD0UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC5F444;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xD0UL))));
        if ((x9 == 0x0UL))
        {
            goto label_0xC5F354;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x9) + (0x10UL))))))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x8) + (0x10UL))), unchecked((byte)(unchecked((uint)(x10)))));
        if ((unchecked((uint)(x10)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC5F354;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x11 = x8;
        goto label_0xC5F340;
        label_0xC5F340:
        ;
        RuntimeMemory.WriteU8(unchecked((ulong)((x11) + (0x10UL))), unchecked((byte)(unchecked((uint)(x10)))));
        x11 = RuntimeMemory.ReadU64(unchecked((ulong)((x11) + (0x18UL))));
        if ((x11 != 0x0UL))
        {
            goto label_0xC5F340;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x9) + (0x20UL))))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x8) + (0x20UL))), unchecked((uint)(x9)));
        goto label_0xC5F354;
        label_0xC5F354:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xD8UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC5F444;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xD8UL))));
        if ((x9 == 0x0UL))
        {
            goto label_0xC5F38C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x9) + (0x10UL))))))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x8) + (0x10UL))), unchecked((byte)(unchecked((uint)(x10)))));
        if ((unchecked((uint)(x10)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC5F38C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x11 = x8;
        goto label_0xC5F378;
        label_0xC5F378:
        ;
        RuntimeMemory.WriteU8(unchecked((ulong)((x11) + (0x10UL))), unchecked((byte)(unchecked((uint)(x10)))));
        x11 = RuntimeMemory.ReadU64(unchecked((ulong)((x11) + (0x18UL))));
        if ((x11 != 0x0UL))
        {
            goto label_0xC5F378;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x9) + (0x20UL))))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x8) + (0x20UL))), unchecked((uint)(x9)));
        goto label_0xC5F38C;
        label_0xC5F38C:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xE0UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC5F444;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xE0UL))));
        if ((x9 == 0x0UL))
        {
            goto label_0xC5F3B8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x9) + (0x10UL))))))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x8) + (0x10UL))), unchecked((byte)(unchecked((uint)(x9)))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC5F3B8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        goto label_0xC5F3AC;
        label_0xC5F3AC:
        ;
        RuntimeMemory.WriteU8(unchecked((ulong)((x8) + (0x10UL))), unchecked((byte)(unchecked((uint)(x9)))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x18UL))));
        if ((x8 != 0x0UL))
        {
            goto label_0xC5F3AC;
        }
        else
        {
            goto label_0xC5F3B8;
        }
        label_0xC5F3B8:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xE8UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC5F444;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xE8UL))));
        if ((x9 == 0x0UL))
        {
            goto label_0xC5F3E4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x9) + (0x10UL))))))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x8) + (0x10UL))), unchecked((byte)(unchecked((uint)(x9)))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC5F3E4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        goto label_0xC5F3D8;
        label_0xC5F3D8:
        ;
        RuntimeMemory.WriteU8(unchecked((ulong)((x8) + (0x10UL))), unchecked((byte)(unchecked((uint)(x9)))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x18UL))));
        if ((x8 != 0x0UL))
        {
            goto label_0xC5F3D8;
        }
        else
        {
            goto label_0xC5F3E4;
        }
        label_0xC5F3E4:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xF0UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC5F444;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xF0UL))));
        if ((x9 == 0x0UL))
        {
            goto label_0xC5F410;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x9) + (0x10UL))))))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x8) + (0x10UL))), unchecked((byte)(unchecked((uint)(x9)))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC5F410;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        goto label_0xC5F404;
        label_0xC5F404:
        ;
        RuntimeMemory.WriteU8(unchecked((ulong)((x8) + (0x10UL))), unchecked((byte)(unchecked((uint)(x9)))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x18UL))));
        if ((x8 != 0x0UL))
        {
            goto label_0xC5F404;
        }
        else
        {
            goto label_0xC5F410;
        }
        label_0xC5F410:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xF8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC5F444;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xF8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xC5DF74UL /* metadata target: JoystickStateBinding.CopyFrom */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x100UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC5F444;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x100UL))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0xC5DF74UL /* metadata target: JoystickStateBinding.CopyFrom */);
        label_0xC5F438:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        label_0xC5F444:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `TouchGestureStateBinding.SyncTouchState` — RVA `0xc5f448`

- Lift status: **partial**; input span: 1784 bytes; span to next metadata RVA: 1784 bytes.
- Metadata signature: `public void SyncTouchState(TouchGestureState screenState, TouchGestureState orientedState, JoystickState swipeJoyState, InputRig rig) { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=187 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'frintp' at 0xc5f7e4; reason: Unsupported instruction 'frintm' at 0xc5f818; reason: Unsupported instruction 'csel' at 0xc5f834; reason: Unknown IR expression at 0xc5f834; reason: Unsupported instruction 'frintp' at 0xc5f8d0; reason: Unsupported instruction 'frintm' at 0xc5f8dc; reason: Unsupported instruction 'csel' at 0xc5f8f8; reason: Unknown IR expression at 0xc5f8f8

```csharp
public static ulong TouchGestureStateBinding_SyncTouchState_RVAc5f448(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        double __arm64_fcvtz_source_12974028 = default(double);
        double __arm64_fcvtz_source_12974080 = default(double);
        double __arm64_fcvtz_source_12974120 = default(double);
        double __arm64_fcvtz_source_12974264 = default(double);
        double __arm64_fcvtz_source_12974316 = default(double);
        double __arm64_fcvtz_source_12974476 = default(double);
        double __arm64_fcvtz_source_12974620 = default(double);
        double __arm64_fcvtz_source_12974672 = default(double);
        ulong __arm64_flags_left_12973316 = default(ulong);
        uint __arm64_flags_left_12973332 = default(uint);
        uint __arm64_flags_left_12973404 = default(uint);
        ulong __arm64_flags_left_12974036 = default(ulong);
        ulong __arm64_flags_left_12974088 = default(ulong);
        ulong __arm64_flags_left_12974272 = default(ulong);
        ulong __arm64_flags_left_12974628 = default(ulong);
        ulong __arm64_flags_result_12974036 = default(ulong);
        ulong __arm64_flags_result_12974088 = default(ulong);
        ulong __arm64_flags_result_12974272 = default(ulong);
        ulong __arm64_flags_result_12974628 = default(ulong);
        ulong __arm64_flags_right_12973316 = default(ulong);
        uint __arm64_flags_right_12973332 = default(uint);
        uint __arm64_flags_right_12973404 = default(uint);
        ulong __arm64_flags_right_12974036 = default(ulong);
        ulong __arm64_flags_right_12974088 = default(ulong);
        ulong __arm64_flags_right_12974272 = default(ulong);
        ulong __arm64_flags_right_12974628 = default(ulong);
        float __arm64_float_flags_left_12973860 = default(float);
        double __arm64_float_flags_left_12973872 = default(double);
        float __arm64_float_flags_left_12973976 = default(float);
        double __arm64_float_flags_left_12973988 = default(double);
        double __arm64_float_flags_left_12974012 = default(double);
        double __arm64_float_flags_left_12974064 = default(double);
        double __arm64_float_flags_left_12974124 = default(double);
        float __arm64_float_flags_left_12974212 = default(float);
        double __arm64_float_flags_left_12974224 = default(double);
        double __arm64_float_flags_left_12974248 = default(double);
        double __arm64_float_flags_left_12974320 = default(double);
        double __arm64_float_flags_left_12974480 = default(double);
        float __arm64_float_flags_left_12974568 = default(float);
        double __arm64_float_flags_left_12974580 = default(double);
        double __arm64_float_flags_left_12974604 = default(double);
        double __arm64_float_flags_left_12974676 = default(double);
        float __arm64_float_flags_right_12973860 = default(float);
        double __arm64_float_flags_right_12973872 = default(double);
        float __arm64_float_flags_right_12973976 = default(float);
        double __arm64_float_flags_right_12973988 = default(double);
        double __arm64_float_flags_right_12974012 = default(double);
        double __arm64_float_flags_right_12974064 = default(double);
        double __arm64_float_flags_right_12974124 = default(double);
        float __arm64_float_flags_right_12974212 = default(float);
        double __arm64_float_flags_right_12974224 = default(double);
        double __arm64_float_flags_right_12974248 = default(double);
        double __arm64_float_flags_right_12974320 = default(double);
        double __arm64_float_flags_right_12974480 = default(double);
        float __arm64_float_flags_right_12974568 = default(float);
        double __arm64_float_flags_right_12974580 = default(double);
        double __arm64_float_flags_right_12974604 = default(double);
        double __arm64_float_flags_right_12974676 = default(double);
        ulong __arm64_pair_address_12973136 = default(ulong);
        ulong __arm64_pair_address_12973140 = default(ulong);
        ulong __arm64_pair_address_12973292 = default(ulong);
        ulong __arm64_pair_address_12973296 = default(ulong);
        ulong __arm64_pair_address_12973620 = default(ulong);
        ulong __arm64_pair_address_12973676 = default(ulong);
        ulong __arm64_pair_address_12973732 = default(ulong);
        ulong __arm64_pair_address_12973744 = default(ulong);
        ulong __arm64_pair_address_12973748 = default(ulong);
        ulong __arm64_pair_address_12973752 = default(ulong);
        ulong __arm64_pair_address_12973756 = default(ulong);
        ulong __arm64_pair_address_12974360 = default(ulong);
        ulong __arm64_pair_address_12974716 = default(ulong);
        ulong __arm64_pair_address_12974872 = default(ulong);
        ulong __arm64_pair_address_12974876 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v10 = default(RuntimeVector128);
        RuntimeVector128 v11 = default(RuntimeVector128);
        RuntimeVector128 v12 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
        RuntimeVector128 v4 = default(RuntimeVector128);
        RuntimeVector128 v5 = default(RuntimeVector128);
        RuntimeVector128 v6 = default(RuntimeVector128);
        RuntimeVector128 v7 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        RuntimeVector128 v9 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x22 = default(ulong);
        ulong x23 = default(ulong);
        ulong x24 = default(ulong);
        ulong x25 = default(ulong);
        ulong x26 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        sp = unchecked((ulong)((sp) - (0x80UL)));
        RuntimeMemory.WriteF64(unchecked((ulong)((sp) + (0x10UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v12.GetUInt64(0)))));
        __arm64_pair_address_12973136 = unchecked((ulong)((sp) + (0x18UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12973136, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v11.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12973136) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v10.GetUInt64(0)))));
        __arm64_pair_address_12973140 = unchecked((ulong)((sp) + (0x28UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12973140, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12973140) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x38UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x0UL))), x26);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))), x25);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x0UL))), x24);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x8UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x70UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x70UL)))) + (0x8UL))), x19);
        x24 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x24) + (0x2DDUL))))))));
        x19 = x4;
        x22 = x3;
        x23 = x2;
        x20 = x1;
        x21 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC5F4A0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD8UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x24) + (0x2DDUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC5F4A0;
        label_0xC5F4A0:
        ;
        if ((x20 == 0x0UL))
        {
            goto label_0xC5F4D8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x10UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC5F4D8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xD8UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC5F4C4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC5F4C0UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC5F4C4;
        label_0xC5F4C4:
        ;
        x0 = x19;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179568CUL /* metadata target: Object.op_Equality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC5F500;
        }
        else
        {
            goto label_0xC5F4D8;
        }
        label_0xC5F4D8:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x70UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x70UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x60UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x8UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x50UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x8UL))));
        x26 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x40UL))));
        x25 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x38UL))));
        __arm64_pair_address_12973292 = unchecked((ulong)((sp) + (0x28UL)));
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12973292)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12973292) + (0x8UL))))), 0));
        __arm64_pair_address_12973296 = unchecked((ulong)((sp) + (0x18UL)));
        v11 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12973296)), 0));
        v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12973296) + (0x8UL))))), 0));
        v12 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((sp) + (0x10UL))))), 0));
        sp = unchecked((ulong)((sp) + (0x80UL)));
        return x0;
        label_0xC5F500:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x127UL))))))));
        __arm64_flags_left_12973316 = x23;
        __arm64_flags_right_12973316 = 0x0UL;
        x24 = ((unchecked((ulong)((__arm64_flags_left_12973316) - (__arm64_flags_right_12973316))) == 0x0UL) ? x20 : x23);
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC5F598;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x20) + (0x134UL))))));
        __arm64_flags_left_12973332 = unchecked((uint)(x8));
        __arm64_flags_right_12973332 = unchecked((uint)0x1UL);
        if ((!((unchecked((uint)((__arm64_flags_left_12973332) - (__arm64_flags_right_12973332))) == unchecked((uint)0x0UL)))))
        {
            goto label_0xC5F55C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x38UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC5FB3C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x2 = x19;
        x3 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x4 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC4F00CUL /* metadata target: DigitalBinding.Sync */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xB8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC5FB3C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC5F540UL);
        }
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x20) + (0x130UL))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x20) + (0x12CUL))))), 0));
        x1 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xC5E3A8UL /* metadata target: MousePositionBinding.SyncPos */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x127UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC5F598;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x20) + (0x134UL))))));
        goto label_0xC5F55C;
        label_0xC5F55C:
        ;
        __arm64_flags_left_12973404 = unchecked((uint)(x8));
        __arm64_flags_right_12973404 = unchecked((uint)0x2UL);
        if ((!((unchecked((uint)((__arm64_flags_left_12973404) - (__arm64_flags_right_12973404))) == unchecked((uint)0x0UL)))))
        {
            goto label_0xC5F598;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x40UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC5FB3C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x2 = x19;
        x3 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x4 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC4F00CUL /* metadata target: DigitalBinding.Sync */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xC0UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC5FB3C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC5F588UL);
        }
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x20) + (0x130UL))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x20) + (0x12CUL))))), 0));
        x1 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xC5E3A8UL /* metadata target: MousePositionBinding.SyncPos */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        goto label_0xC5F598;
        label_0xC5F598:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x128UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC5F5D4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x48UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC5FB3C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x2 = x19;
        x3 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x4 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC4F00CUL /* metadata target: DigitalBinding.Sync */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xC8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC5FB3C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC5F5C4UL);
        }
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x20) + (0x130UL))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x20) + (0x12CUL))))), 0));
        x1 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xC5E3A8UL /* metadata target: MousePositionBinding.SyncPos */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        goto label_0xC5F5D4;
        label_0xC5F5D4:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x24) + (0x106UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC5F5E8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x58UL))));
        if ((x0 != 0x0UL))
        {
            goto label_0xC5F5F8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC5F5E4UL);
        }
        goto label_0xC5FB3C;
        label_0xC5F5E8:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x24) + (0x104UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC5F608;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x50UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC5FB3C;
        }
        else
        {
            goto label_0xC5F5F8;
        }
        label_0xC5F5F8:
        ;
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x24) + (0x138UL))));
        x2 = x19;
        x3 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC5CFA0UL /* metadata target: DirectionBinding.SyncDirectionState */, x0, x1, x2, x3);
        goto label_0xC5F608;
        label_0xC5F608:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x24) + (0x1CUL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC5FAD8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x20UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC5FB3C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x2 = x19;
        x3 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x4 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC4F00CUL /* metadata target: DigitalBinding.Sync */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xA0UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC5FB3C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC5F634UL);
        }
        __arm64_pair_address_12973620 = unchecked((ulong)((x20) + (0x44UL)));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12973620)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12973620) + (0x4UL))))), 0));
        x1 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xC5E3A8UL /* metadata target: MousePositionBinding.SyncPos */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x104UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC5F678;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x28UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC5FB3C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x2 = x19;
        x3 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x4 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC4F00CUL /* metadata target: DigitalBinding.Sync */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xA8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC5FB3C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC5F66CUL);
        }
        __arm64_pair_address_12973676 = unchecked((ulong)((x20) + (0x44UL)));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12973676)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12973676) + (0x4UL))))), 0));
        x1 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xC5E3A8UL /* metadata target: MousePositionBinding.SyncPos */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        goto label_0xC5F678;
        label_0xC5F678:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x106UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC5F6B0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x30UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC5FB3C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x2 = x19;
        x3 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x4 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC4F00CUL /* metadata target: DigitalBinding.Sync */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xB0UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC5FB3C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC5F6A4UL);
        }
        __arm64_pair_address_12973732 = unchecked((ulong)((x20) + (0x44UL)));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12973732)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12973732) + (0x4UL))))), 0));
        x1 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xC5E3A8UL /* metadata target: MousePositionBinding.SyncPos */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        goto label_0xC5F6B0;
        label_0xC5F6B0:
        ;
        __arm64_pair_address_12973744 = unchecked((ulong)((x24) + (0xD8UL)));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12973744)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12973744) + (0x4UL))))), 0));
        __arm64_pair_address_12973748 = unchecked((ulong)((x24) + (0xE0UL)));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12973748)), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12973748) + (0x4UL))))), 0));
        __arm64_pair_address_12973752 = unchecked((ulong)((x24) + (0xE8UL)));
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12973752)), 0));
        v5 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12973752) + (0x4UL))))), 0));
        __arm64_pair_address_12973756 = unchecked((ulong)((x24) + (0xF0UL)));
        v6 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12973756)), 0));
        v7 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12973756) + (0x4UL))))), 0));
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x24) + (0x106UL))))))));
        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0))))), 0));
        v12 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v6.GetUInt64(0)))), 0))))), 0));
        v11 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v5.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v7.GetUInt64(0)))), 0))))), 0));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC5F744;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x25 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x25) + (0x242UL))))))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x90UL))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC5F6FC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xA60UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x25) + (0x242UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC5F6FC;
        label_0xC5F6FC:
        ;
        x26 = 0x1A8C000UL;
        x26 = RuntimeMemory.ReadU64(unchecked((ulong)((x26) + (0xA60UL))));
        x0 = RuntimeMemory.ReadU64(x26);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC5F714;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC5F710UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        goto label_0xC5F714;
        label_0xC5F714:
        ;
        v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(unchecked((double)(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v12.GetUInt64(0)))), 0)))), 0));
        x0 = unchecked((ulong)((sp) + (0x8UL)));
        v0 = v10;
        x0 = RuntimeCalls.InvokeDirect(0x19B0C60UL, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        __arm64_float_flags_left_12973860 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v12.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12973860 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        if ((__arm64_float_flags_left_12973860 >= __arm64_float_flags_right_12973860))
        {
            goto label_0xC5F7B8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC5F72CUL);
        }
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(global::System.BitConverter.Int64BitsToDouble(unchecked((long)0xBFE0000000000000UL))), 0));
        __arm64_float_flags_left_12973872 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0))));
        __arm64_float_flags_right_12973872 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0))));
        if (((__arm64_float_flags_left_12973872 != __arm64_float_flags_right_12973872) || ((__arm64_float_flags_left_12973872 != __arm64_float_flags_left_12973872) || (__arm64_float_flags_right_12973872 != __arm64_float_flags_right_12973872))))
        {
            goto label_0xC5F7E0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC5F738UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((sp) + (0x8UL))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(global::System.BitConverter.Int64BitsToDouble(unchecked((long)0xBFF0000000000000UL))), 0));
        goto label_0xC5F7CC;
        label_0xC5F744:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x24) + (0x104UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC5FAD8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x25 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x25) + (0x242UL))))))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x80UL))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC5F770;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xA60UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x25) + (0x242UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC5F770;
        label_0xC5F770:
        ;
        x26 = 0x1A8C000UL;
        x26 = RuntimeMemory.ReadU64(unchecked((ulong)((x26) + (0xA60UL))));
        x0 = RuntimeMemory.ReadU64(x26);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC5F788;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC5F784UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        goto label_0xC5F788;
        label_0xC5F788:
        ;
        v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(unchecked((double)(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v12.GetUInt64(0)))), 0)))), 0));
        x0 = unchecked((ulong)((sp) + (0x8UL)));
        v0 = v10;
        x0 = RuntimeCalls.InvokeDirect(0x19B0C60UL, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        __arm64_float_flags_left_12973976 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v12.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12973976 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        if ((__arm64_float_flags_left_12973976 >= __arm64_float_flags_right_12973976))
        {
            goto label_0xC5F7EC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC5F7A0UL);
        }
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(global::System.BitConverter.Int64BitsToDouble(unchecked((long)0xBFE0000000000000UL))), 0));
        __arm64_float_flags_left_12973988 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0))));
        __arm64_float_flags_right_12973988 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0))));
        if (((__arm64_float_flags_left_12973988 != __arm64_float_flags_right_12973988) || ((__arm64_float_flags_left_12973988 != __arm64_float_flags_left_12973988) || (__arm64_float_flags_right_12973988 != __arm64_float_flags_right_12973988))))
        {
            goto label_0xC5F96C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC5F7ACUL);
        }
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((sp) + (0x8UL))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(global::System.BitConverter.Int64BitsToDouble(unchecked((long)0xBFF0000000000000UL))), 0));
        goto label_0xC5F800;
        label_0xC5F7B8:
        ;
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(global::System.BitConverter.Int64BitsToDouble(unchecked((long)0x3FE0000000000000UL))), 0));
        __arm64_float_flags_left_12974012 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0))));
        __arm64_float_flags_right_12974012 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0))));
        if (((__arm64_float_flags_left_12974012 != __arm64_float_flags_right_12974012) || ((__arm64_float_flags_left_12974012 != __arm64_float_flags_left_12974012) || (__arm64_float_flags_right_12974012 != __arm64_float_flags_right_12974012))))
        {
            goto label_0xC5F814;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC5F7C4UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((sp) + (0x8UL))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(global::System.BitConverter.Int64BitsToDouble(unchecked((long)0x3FF0000000000000UL))), 0));
        goto label_0xC5F7CC;
        label_0xC5F7CC:
        ;
        __arm64_fcvtz_source_12974028 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0))));
        x8 = unchecked((ulong)(((__arm64_fcvtz_source_12974028 != __arm64_fcvtz_source_12974028) ? unchecked((long)0x0UL) : ((__arm64_fcvtz_source_12974028 >= global::System.BitConverter.Int64BitsToDouble(unchecked((long)0x43E0000000000000UL))) ? unchecked((long)0x7FFFFFFFFFFFFFFFUL) : ((__arm64_fcvtz_source_12974028 < global::System.BitConverter.Int64BitsToDouble(unchecked((long)0xC3E0000000000000UL))) ? unchecked((long)0x8000000000000000UL) : unchecked((long)(__arm64_fcvtz_source_12974028)))))));
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(unchecked((double)((global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0))))) + (global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0)))))))), 0));
        __arm64_flags_left_12974036 = x8;
        __arm64_flags_right_12974036 = 0x1UL;
        __arm64_flags_result_12974036 = unchecked((ulong)((__arm64_flags_left_12974036) & (__arm64_flags_right_12974036)));
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(((__arm64_flags_result_12974036 == 0x0UL) ? global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))) : global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0)))))), 0));
        goto label_0xC5F81C;
        label_0xC5F7E0:
        ;
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(unchecked((double)((global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v10.GetUInt64(0))))) + (global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0)))))))), 0));
        RuntimeCalls.Unsupported("frintp", 0xC5F7E4UL);
        goto label_0xC5F81C;
        label_0xC5F7EC:
        ;
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(global::System.BitConverter.Int64BitsToDouble(unchecked((long)0x3FE0000000000000UL))), 0));
        __arm64_float_flags_left_12974064 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0))));
        __arm64_float_flags_right_12974064 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0))));
        if (((__arm64_float_flags_left_12974064 != __arm64_float_flags_right_12974064) || ((__arm64_float_flags_left_12974064 != __arm64_float_flags_left_12974064) || (__arm64_float_flags_right_12974064 != __arm64_float_flags_right_12974064))))
        {
            goto label_0xC5F978;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC5F7F8UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((sp) + (0x8UL))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(global::System.BitConverter.Int64BitsToDouble(unchecked((long)0x3FF0000000000000UL))), 0));
        goto label_0xC5F800;
        label_0xC5F800:
        ;
        __arm64_fcvtz_source_12974080 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0))));
        x8 = unchecked((ulong)(((__arm64_fcvtz_source_12974080 != __arm64_fcvtz_source_12974080) ? unchecked((long)0x0UL) : ((__arm64_fcvtz_source_12974080 >= global::System.BitConverter.Int64BitsToDouble(unchecked((long)0x43E0000000000000UL))) ? unchecked((long)0x7FFFFFFFFFFFFFFFUL) : ((__arm64_fcvtz_source_12974080 < global::System.BitConverter.Int64BitsToDouble(unchecked((long)0xC3E0000000000000UL))) ? unchecked((long)0x8000000000000000UL) : unchecked((long)(__arm64_fcvtz_source_12974080)))))));
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(unchecked((double)((global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0))))) + (global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0)))))))), 0));
        __arm64_flags_left_12974088 = x8;
        __arm64_flags_right_12974088 = 0x1UL;
        __arm64_flags_result_12974088 = unchecked((ulong)((__arm64_flags_left_12974088) & (__arm64_flags_right_12974088)));
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(((__arm64_flags_result_12974088 == 0x0UL) ? global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))) : global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0)))))), 0));
        goto label_0xC5F980;
        label_0xC5F814:
        ;
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(unchecked((double)((global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v10.GetUInt64(0))))) + (global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0)))))))), 0));
        RuntimeCalls.Unsupported("frintm", 0xC5F818UL);
        goto label_0xC5F81C;
        label_0xC5F81C:
        ;
        if ((x23 == 0x0UL))
        {
            goto label_0xC5FB3C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x7FF0000000000000UL;
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(global::System.BitConverter.Int64BitsToDouble(unchecked((long)(x8)))), 0));
        __arm64_fcvtz_source_12974120 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0))));
        x9 = unchecked((ulong)(unchecked((uint)(((__arm64_fcvtz_source_12974120 != __arm64_fcvtz_source_12974120) ? unchecked((int)0x0UL) : ((__arm64_fcvtz_source_12974120 >= global::System.BitConverter.Int64BitsToDouble(unchecked((long)0x41E0000000000000UL))) ? unchecked((int)0x7FFFFFFFUL) : ((__arm64_fcvtz_source_12974120 < global::System.BitConverter.Int64BitsToDouble(unchecked((long)0xC1E0000000000000UL))) ? unchecked((int)0x80000000UL) : unchecked((int)(__arm64_fcvtz_source_12974120)))))))));
        __arm64_float_flags_left_12974124 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0))));
        __arm64_float_flags_right_12974124 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0))));
        x8 = unchecked((ulong)(unchecked((uint)(0xFFFFFFFF80000000UL))));
        RuntimeCalls.Unsupported("csel", 0xC5F834UL);
        x1 = unchecked((ulong)((__Unsupported<bool>("Unknown IR expression") ? unchecked((uint)(x8)) : unchecked((uint)(x9)))));
        x0 = x23;
        x2 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xC5E7E8UL /* metadata target: ScrollDeltaBinding.SyncScrollDelta */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x25) + (0x242UL))))))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x98UL))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC5F864;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xA60UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x25) + (0x242UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC5F864;
        label_0xC5F864:
        ;
        x0 = RuntimeMemory.ReadU64(x26);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC5F874;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC5F870UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, unchecked((ulong)(unchecked((uint)(x3)))));
        goto label_0xC5F874;
        label_0xC5F874:
        ;
        v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(unchecked((double)(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0)))), 0));
        x0 = unchecked((ulong)((sp) + (0x8UL)));
        v0 = v10;
        x0 = RuntimeCalls.InvokeDirect(0x19B0C60UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, unchecked((ulong)(unchecked((uint)(x3)))));
        __arm64_float_flags_left_12974212 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12974212 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        if ((__arm64_float_flags_left_12974212 >= __arm64_float_flags_right_12974212))
        {
            goto label_0xC5F8A4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC5F88CUL);
        }
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(global::System.BitConverter.Int64BitsToDouble(unchecked((long)0xBFE0000000000000UL))), 0));
        __arm64_float_flags_left_12974224 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0))));
        __arm64_float_flags_right_12974224 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0))));
        if (((__arm64_float_flags_left_12974224 != __arm64_float_flags_right_12974224) || ((__arm64_float_flags_left_12974224 != __arm64_float_flags_left_12974224) || (__arm64_float_flags_right_12974224 != __arm64_float_flags_right_12974224))))
        {
            goto label_0xC5F8CC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC5F898UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((sp) + (0x8UL))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(global::System.BitConverter.Int64BitsToDouble(unchecked((long)0xBFF0000000000000UL))), 0));
        goto label_0xC5F8B8;
        label_0xC5F8A4:
        ;
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(global::System.BitConverter.Int64BitsToDouble(unchecked((long)0x3FE0000000000000UL))), 0));
        __arm64_float_flags_left_12974248 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0))));
        __arm64_float_flags_right_12974248 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0))));
        if (((__arm64_float_flags_left_12974248 != __arm64_float_flags_right_12974248) || ((__arm64_float_flags_left_12974248 != __arm64_float_flags_left_12974248) || (__arm64_float_flags_right_12974248 != __arm64_float_flags_right_12974248))))
        {
            goto label_0xC5F8D8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC5F8B0UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((sp) + (0x8UL))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(global::System.BitConverter.Int64BitsToDouble(unchecked((long)0x3FF0000000000000UL))), 0));
        goto label_0xC5F8B8;
        label_0xC5F8B8:
        ;
        __arm64_fcvtz_source_12974264 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0))));
        x8 = unchecked((ulong)(((__arm64_fcvtz_source_12974264 != __arm64_fcvtz_source_12974264) ? unchecked((long)0x0UL) : ((__arm64_fcvtz_source_12974264 >= global::System.BitConverter.Int64BitsToDouble(unchecked((long)0x43E0000000000000UL))) ? unchecked((long)0x7FFFFFFFFFFFFFFFUL) : ((__arm64_fcvtz_source_12974264 < global::System.BitConverter.Int64BitsToDouble(unchecked((long)0xC3E0000000000000UL))) ? unchecked((long)0x8000000000000000UL) : unchecked((long)(__arm64_fcvtz_source_12974264)))))));
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(unchecked((double)((global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0))))) + (global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0)))))))), 0));
        __arm64_flags_left_12974272 = x8;
        __arm64_flags_right_12974272 = 0x1UL;
        __arm64_flags_result_12974272 = unchecked((ulong)((__arm64_flags_left_12974272) & (__arm64_flags_right_12974272)));
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(((__arm64_flags_result_12974272 == 0x0UL) ? global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))) : global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0)))))), 0));
        goto label_0xC5F8E0;
        label_0xC5F8CC:
        ;
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(unchecked((double)((global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v10.GetUInt64(0))))) + (global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0)))))))), 0));
        RuntimeCalls.Unsupported("frintp", 0xC5F8D0UL);
        goto label_0xC5F8E0;
        label_0xC5F8D8:
        ;
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(unchecked((double)((global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v10.GetUInt64(0))))) + (global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0)))))))), 0));
        RuntimeCalls.Unsupported("frintm", 0xC5F8DCUL);
        goto label_0xC5F8E0;
        label_0xC5F8E0:
        ;
        if ((x23 == 0x0UL))
        {
            goto label_0xC5FB3C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x7FF0000000000000UL;
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(global::System.BitConverter.Int64BitsToDouble(unchecked((long)(x8)))), 0));
        __arm64_fcvtz_source_12974316 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0))));
        x9 = unchecked((ulong)(unchecked((uint)(((__arm64_fcvtz_source_12974316 != __arm64_fcvtz_source_12974316) ? unchecked((int)0x0UL) : ((__arm64_fcvtz_source_12974316 >= global::System.BitConverter.Int64BitsToDouble(unchecked((long)0x41E0000000000000UL))) ? unchecked((int)0x7FFFFFFFUL) : ((__arm64_fcvtz_source_12974316 < global::System.BitConverter.Int64BitsToDouble(unchecked((long)0xC1E0000000000000UL))) ? unchecked((int)0x80000000UL) : unchecked((int)(__arm64_fcvtz_source_12974316)))))))));
        __arm64_float_flags_left_12974320 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0))));
        __arm64_float_flags_right_12974320 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0))));
        x8 = unchecked((ulong)(unchecked((uint)(0xFFFFFFFF80000000UL))));
        RuntimeCalls.Unsupported("csel", 0xC5F8F8UL);
        x1 = unchecked((ulong)((__Unsupported<bool>("Unknown IR expression") ? unchecked((uint)(x8)) : unchecked((uint)(x9)))));
        x0 = x23;
        x2 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xC5E7E8UL /* metadata target: ScrollDeltaBinding.SyncScrollDelta */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x120UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC5F95C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xD8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC5FB3C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC5F918UL);
        }
        __arm64_pair_address_12974360 = unchecked((ulong)((x20) + (0x44UL)));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12974360)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12974360) + (0x4UL))))), 0));
        x1 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xC5E3A8UL /* metadata target: MousePositionBinding.SyncPos */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x70UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC5FB3C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)(0x3UL))));
        v0 = v9;
        x2 = x19;
        x3 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC4F160UL /* metadata target: AxisBinding.SyncFloat */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x78UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC5FB3C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)(0x3UL))));
        v0 = v8;
        x2 = x19;
        x3 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC4F160UL /* metadata target: AxisBinding.SyncFloat */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xC5F95C;
        label_0xC5F95C:
        ;
        if ((x22 == 0x0UL))
        {
            goto label_0xC5FAD8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x100UL))));
        if ((x0 != 0x0UL))
        {
            goto label_0xC5FACC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC5F968UL);
        }
        goto label_0xC5FB3C;
        label_0xC5F96C:
        ;
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(unchecked((double)((global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v10.GetUInt64(0))))) + (global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0)))))))), 0));
        RuntimeCalls.Unsupported("frintp", 0xC5F970UL);
        goto label_0xC5F980;
        label_0xC5F978:
        ;
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(unchecked((double)((global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v10.GetUInt64(0))))) + (global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0)))))))), 0));
        RuntimeCalls.Unsupported("frintm", 0xC5F97CUL);
        goto label_0xC5F980;
        label_0xC5F980:
        ;
        if ((x23 == 0x0UL))
        {
            goto label_0xC5FB3C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x7FF0000000000000UL;
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(global::System.BitConverter.Int64BitsToDouble(unchecked((long)(x8)))), 0));
        __arm64_fcvtz_source_12974476 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0))));
        x9 = unchecked((ulong)(unchecked((uint)(((__arm64_fcvtz_source_12974476 != __arm64_fcvtz_source_12974476) ? unchecked((int)0x0UL) : ((__arm64_fcvtz_source_12974476 >= global::System.BitConverter.Int64BitsToDouble(unchecked((long)0x41E0000000000000UL))) ? unchecked((int)0x7FFFFFFFUL) : ((__arm64_fcvtz_source_12974476 < global::System.BitConverter.Int64BitsToDouble(unchecked((long)0xC1E0000000000000UL))) ? unchecked((int)0x80000000UL) : unchecked((int)(__arm64_fcvtz_source_12974476)))))))));
        __arm64_float_flags_left_12974480 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0))));
        __arm64_float_flags_right_12974480 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0))));
        x8 = unchecked((ulong)(unchecked((uint)(0xFFFFFFFF80000000UL))));
        RuntimeCalls.Unsupported("csel", 0xC5F998UL);
        x1 = unchecked((ulong)((__Unsupported<bool>("Unknown IR expression") ? unchecked((uint)(x8)) : unchecked((uint)(x9)))));
        x0 = x23;
        x2 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xC5E7E8UL /* metadata target: ScrollDeltaBinding.SyncScrollDelta */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x25) + (0x242UL))))))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x88UL))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC5F9C8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xA60UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x25) + (0x242UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC5F9C8;
        label_0xC5F9C8:
        ;
        x0 = RuntimeMemory.ReadU64(x26);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC5F9D8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC5F9D4UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xC5F9D8;
        label_0xC5F9D8:
        ;
        v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(unchecked((double)(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0)))), 0));
        x0 = unchecked((ulong)((sp) + (0x8UL)));
        v0 = v10;
        x0 = RuntimeCalls.InvokeDirect(0x19B0C60UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        __arm64_float_flags_left_12974568 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12974568 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        if ((__arm64_float_flags_left_12974568 >= __arm64_float_flags_right_12974568))
        {
            goto label_0xC5FA08;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC5F9F0UL);
        }
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(global::System.BitConverter.Int64BitsToDouble(unchecked((long)0xBFE0000000000000UL))), 0));
        __arm64_float_flags_left_12974580 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0))));
        __arm64_float_flags_right_12974580 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0))));
        if (((__arm64_float_flags_left_12974580 != __arm64_float_flags_right_12974580) || ((__arm64_float_flags_left_12974580 != __arm64_float_flags_left_12974580) || (__arm64_float_flags_right_12974580 != __arm64_float_flags_right_12974580))))
        {
            goto label_0xC5FA30;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC5F9FCUL);
        }
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((sp) + (0x8UL))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(global::System.BitConverter.Int64BitsToDouble(unchecked((long)0xBFF0000000000000UL))), 0));
        goto label_0xC5FA1C;
        label_0xC5FA08:
        ;
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(global::System.BitConverter.Int64BitsToDouble(unchecked((long)0x3FE0000000000000UL))), 0));
        __arm64_float_flags_left_12974604 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0))));
        __arm64_float_flags_right_12974604 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0))));
        if (((__arm64_float_flags_left_12974604 != __arm64_float_flags_right_12974604) || ((__arm64_float_flags_left_12974604 != __arm64_float_flags_left_12974604) || (__arm64_float_flags_right_12974604 != __arm64_float_flags_right_12974604))))
        {
            goto label_0xC5FA3C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC5FA14UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((sp) + (0x8UL))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(global::System.BitConverter.Int64BitsToDouble(unchecked((long)0x3FF0000000000000UL))), 0));
        goto label_0xC5FA1C;
        label_0xC5FA1C:
        ;
        __arm64_fcvtz_source_12974620 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0))));
        x8 = unchecked((ulong)(((__arm64_fcvtz_source_12974620 != __arm64_fcvtz_source_12974620) ? unchecked((long)0x0UL) : ((__arm64_fcvtz_source_12974620 >= global::System.BitConverter.Int64BitsToDouble(unchecked((long)0x43E0000000000000UL))) ? unchecked((long)0x7FFFFFFFFFFFFFFFUL) : ((__arm64_fcvtz_source_12974620 < global::System.BitConverter.Int64BitsToDouble(unchecked((long)0xC3E0000000000000UL))) ? unchecked((long)0x8000000000000000UL) : unchecked((long)(__arm64_fcvtz_source_12974620)))))));
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(unchecked((double)((global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0))))) + (global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0)))))))), 0));
        __arm64_flags_left_12974628 = x8;
        __arm64_flags_right_12974628 = 0x1UL;
        __arm64_flags_result_12974628 = unchecked((ulong)((__arm64_flags_left_12974628) & (__arm64_flags_right_12974628)));
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(((__arm64_flags_result_12974628 == 0x0UL) ? global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))) : global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0)))))), 0));
        goto label_0xC5FA44;
        label_0xC5FA30:
        ;
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(unchecked((double)((global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v10.GetUInt64(0))))) + (global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0)))))))), 0));
        RuntimeCalls.Unsupported("frintp", 0xC5FA34UL);
        goto label_0xC5FA44;
        label_0xC5FA3C:
        ;
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(unchecked((double)((global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v10.GetUInt64(0))))) + (global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0)))))))), 0));
        RuntimeCalls.Unsupported("frintm", 0xC5FA40UL);
        goto label_0xC5FA44;
        label_0xC5FA44:
        ;
        if ((x23 == 0x0UL))
        {
            goto label_0xC5FB3C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x7FF0000000000000UL;
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(global::System.BitConverter.Int64BitsToDouble(unchecked((long)(x8)))), 0));
        __arm64_fcvtz_source_12974672 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0))));
        x9 = unchecked((ulong)(unchecked((uint)(((__arm64_fcvtz_source_12974672 != __arm64_fcvtz_source_12974672) ? unchecked((int)0x0UL) : ((__arm64_fcvtz_source_12974672 >= global::System.BitConverter.Int64BitsToDouble(unchecked((long)0x41E0000000000000UL))) ? unchecked((int)0x7FFFFFFFUL) : ((__arm64_fcvtz_source_12974672 < global::System.BitConverter.Int64BitsToDouble(unchecked((long)0xC1E0000000000000UL))) ? unchecked((int)0x80000000UL) : unchecked((int)(__arm64_fcvtz_source_12974672)))))))));
        __arm64_float_flags_left_12974676 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0))));
        __arm64_float_flags_right_12974676 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0))));
        x8 = unchecked((ulong)(unchecked((uint)(0xFFFFFFFF80000000UL))));
        RuntimeCalls.Unsupported("csel", 0xC5FA5CUL);
        x1 = unchecked((ulong)((__Unsupported<bool>("Unknown IR expression") ? unchecked((uint)(x8)) : unchecked((uint)(x9)))));
        x0 = x23;
        x2 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xC5E7E8UL /* metadata target: ScrollDeltaBinding.SyncScrollDelta */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x120UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC5FAC0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xD0UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC5FB3C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC5FA7CUL);
        }
        __arm64_pair_address_12974716 = unchecked((ulong)((x20) + (0x44UL)));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12974716)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12974716) + (0x4UL))))), 0));
        x1 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xC5E3A8UL /* metadata target: MousePositionBinding.SyncPos */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x60UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC5FB3C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)(0x3UL))));
        v0 = v9;
        x2 = x19;
        x3 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC4F160UL /* metadata target: AxisBinding.SyncFloat */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x68UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC5FB3C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)(0x3UL))));
        v0 = v8;
        x2 = x19;
        x3 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC4F160UL /* metadata target: AxisBinding.SyncFloat */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xC5FAC0;
        label_0xC5FAC0:
        ;
        if ((x22 == 0x0UL))
        {
            goto label_0xC5FAD8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xF8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC5FB3C;
        }
        else
        {
            goto label_0xC5FACC;
        }
        label_0xC5FACC:
        ;
        x1 = x22;
        x2 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xC5DFFCUL /* metadata target: JoystickStateBinding.SyncJoyState */, x0, x1, x2, x3);
        goto label_0xC5FAD8;
        label_0xC5FAD8:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xE0UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC5FB3C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = x20;
        x2 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xC5D5B4UL /* metadata target: EmuTouchBinding.SyncState */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x24) + (0x106UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC5FB2C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xF0UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC5FB3C;
        }
        else
        {
            goto label_0xC5FAFC;
        }
        label_0xC5FAFC:
        ;
        x1 = x20;
        x2 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x70UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x70UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x60UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x8UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x50UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x8UL))));
        x26 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x40UL))));
        x25 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x38UL))));
        __arm64_pair_address_12974872 = unchecked((ulong)((sp) + (0x28UL)));
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12974872)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12974872) + (0x8UL))))), 0));
        __arm64_pair_address_12974876 = unchecked((ulong)((sp) + (0x18UL)));
        v11 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12974876)), 0));
        v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12974876) + (0x8UL))))), 0));
        v12 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((sp) + (0x10UL))))), 0));
        sp = unchecked((ulong)((sp) + (0x80UL)));
        return RuntimeCalls.InvokeDirect(0xC5D5B4UL /* metadata target: EmuTouchBinding.SyncState */);
        label_0xC5FB2C:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x24) + (0x104UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC5F4D8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xE8UL))));
        if ((x0 != 0x0UL))
        {
            goto label_0xC5FAFC;
        }
        else
        {
            goto label_0xC5FB3C;
        }
        label_0xC5FB3C:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `TouchGestureStateBinding.OnIsBoundToAxis` — RVA `0xc5fb80`

- Lift status: **exact**; input span: 980 bytes; span to next metadata RVA: 980 bytes.
- Metadata signature: `protected override bool OnIsBoundToAxis(string axisName, InputRig rig) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=153 (informational only).

```csharp
public static uint TouchGestureStateBinding_OnIsBoundToAxis_RVAc5fb80(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x10UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC5FF1C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x21 = x0;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x20UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC5FF50;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x19 = x2;
        x20 = x1;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x1E8UL))));
        x3 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x1E8UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC5FF14;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x28UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC5FF50;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x1 = x20;
        x2 = x19;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x1E8UL))));
        x3 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x1E8UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC5FF14;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x30UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC5FF50;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x1 = x20;
        x2 = x19;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x1E8UL))));
        x3 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x1E8UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC5FF14;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x38UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC5FF50;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x1 = x20;
        x2 = x19;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x1E8UL))));
        x3 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x1E8UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC5FF14;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x40UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC5FF50;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x1 = x20;
        x2 = x19;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x1E8UL))));
        x3 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x1E8UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC5FF14;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x48UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC5FF50;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x1 = x20;
        x2 = x19;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x1E8UL))));
        x3 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x1E8UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC5FF14;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x50UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC5FF50;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x1 = x20;
        x2 = x19;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x1E8UL))));
        x3 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x1E8UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC5FF14;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x58UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC5FF50;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x1 = x20;
        x2 = x19;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x1E8UL))));
        x3 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x1E8UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC5FF14;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x60UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC5FF50;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x1 = x20;
        x2 = x19;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x1E8UL))));
        x3 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x1E8UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC5FF14;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x68UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC5FF50;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x1 = x20;
        x2 = x19;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x1E8UL))));
        x3 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x1E8UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC5FF14;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x70UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC5FF50;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x1 = x20;
        x2 = x19;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x1E8UL))));
        x3 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x1E8UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC5FF14;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x78UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC5FF50;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x1 = x20;
        x2 = x19;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x1E8UL))));
        x3 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x1E8UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC5FF14;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x80UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC5FF50;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x1 = x20;
        x2 = x19;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x1E8UL))));
        x3 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x1E8UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC5FF14;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x88UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC5FF50;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x1 = x20;
        x2 = x19;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x1E8UL))));
        x3 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x1E8UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC5FF14;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x90UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC5FF50;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x1 = x20;
        x2 = x19;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x1E8UL))));
        x3 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x1E8UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC5FF14;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x98UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC5FF50;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x1 = x20;
        x2 = x19;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x1E8UL))));
        x3 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x1E8UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC5FF14;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xA0UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC5FF50;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x1 = x20;
        x2 = x19;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x1E8UL))));
        x3 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x1E8UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC5FF14;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xA8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC5FF50;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x1 = x20;
        x2 = x19;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x1E8UL))));
        x3 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x1E8UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC5FF14;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xB0UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC5FF50;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x1 = x20;
        x2 = x19;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x1E8UL))));
        x3 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x1E8UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC5FF14;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xB8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC5FF50;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x1 = x20;
        x2 = x19;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x1E8UL))));
        x3 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x1E8UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC5FF14;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xC0UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC5FF50;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x1 = x20;
        x2 = x19;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x1E8UL))));
        x3 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x1E8UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC5FF14;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xC8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC5FF50;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x1 = x20;
        x2 = x19;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x1E8UL))));
        x3 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x1E8UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC5FF14;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xD0UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC5FF50;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x1 = x20;
        x2 = x19;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x1E8UL))));
        x3 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x1E8UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC5FF14;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xD8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC5FF50;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x1 = x20;
        x2 = x19;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x1E8UL))));
        x3 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x1E8UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC5FF14;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x100UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC5FF50;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x1 = x20;
        x2 = x19;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x1E8UL))));
        x3 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x1E8UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC5FF14;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xF8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC5FF50;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x1 = x20;
        x2 = x19;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x1E8UL))));
        x3 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x1E8UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC5FF14;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xE0UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC5FF50;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x1 = x20;
        x2 = x19;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x1E8UL))));
        x3 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x1E8UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC5FF14;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xE8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC5FF50;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x1 = x20;
        x2 = x19;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x1E8UL))));
        x3 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x1E8UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC5FF2C;
        }
        else
        {
            goto label_0xC5FF14;
        }
        label_0xC5FF14:
        ;
        x0 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        goto label_0xC5FF20;
        label_0xC5FF1C:
        ;
        x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xC5FF20;
        label_0xC5FF20:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return unchecked((uint)(x0));
        label_0xC5FF2C:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xF0UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC5FF50;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x1 = x20;
        x2 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x4 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x1E8UL))));
        x3 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x1E8UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return unchecked((uint)(RuntimeCalls.InvokeIndirect(x4)));
        label_0xC5FF50:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(uint);
    }
```

## `TouchGestureStateBinding.OnIsBoundToKey` — RVA `0xc5ff54`

- Lift status: **exact**; input span: 628 bytes; span to next metadata RVA: 628 bytes.
- Metadata signature: `protected override bool OnIsBoundToKey(KeyCode keyCode, InputRig rig) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=98 (informational only).

```csharp
public static uint TouchGestureStateBinding_OnIsBoundToKey_RVAc5ff54(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x10UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC60190;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x21 = x0;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x20UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC601C4;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x19 = x2;
        x20 = unchecked((ulong)(unchecked((uint)(x1))));
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x1D8UL))));
        x3 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x1D8UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC60188;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x28UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC601C4;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x1 = unchecked((ulong)(unchecked((uint)(x20))));
        x2 = x19;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x1D8UL))));
        x3 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x1D8UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC60188;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x30UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC601C4;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x1 = unchecked((ulong)(unchecked((uint)(x20))));
        x2 = x19;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x1D8UL))));
        x3 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x1D8UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC60188;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x38UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC601C4;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x1 = unchecked((ulong)(unchecked((uint)(x20))));
        x2 = x19;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x1D8UL))));
        x3 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x1D8UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC60188;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x40UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC601C4;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x1 = unchecked((ulong)(unchecked((uint)(x20))));
        x2 = x19;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x1D8UL))));
        x3 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x1D8UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC60188;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x48UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC601C4;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x1 = unchecked((ulong)(unchecked((uint)(x20))));
        x2 = x19;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x1D8UL))));
        x3 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x1D8UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC60188;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x50UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC601C4;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x1 = unchecked((ulong)(unchecked((uint)(x20))));
        x2 = x19;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x1D8UL))));
        x3 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x1D8UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC60188;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x58UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC601C4;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x1 = unchecked((ulong)(unchecked((uint)(x20))));
        x2 = x19;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x1D8UL))));
        x3 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x1D8UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC60188;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x60UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC601C4;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x1 = unchecked((ulong)(unchecked((uint)(x20))));
        x2 = x19;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x1D8UL))));
        x3 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x1D8UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC60188;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x68UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC601C4;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x1 = unchecked((ulong)(unchecked((uint)(x20))));
        x2 = x19;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x1D8UL))));
        x3 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x1D8UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC60188;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x70UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC601C4;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x1 = unchecked((ulong)(unchecked((uint)(x20))));
        x2 = x19;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x1D8UL))));
        x3 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x1D8UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC60188;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x78UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC601C4;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x1 = unchecked((ulong)(unchecked((uint)(x20))));
        x2 = x19;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x1D8UL))));
        x3 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x1D8UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC60188;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x100UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC601C4;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x1 = unchecked((ulong)(unchecked((uint)(x20))));
        x2 = x19;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x1D8UL))));
        x3 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x1D8UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC60188;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xF8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC601C4;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x1 = unchecked((ulong)(unchecked((uint)(x20))));
        x2 = x19;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x1D8UL))));
        x3 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x1D8UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC60188;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x80UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC601C4;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x1 = unchecked((ulong)(unchecked((uint)(x20))));
        x2 = x19;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x1D8UL))));
        x3 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x1D8UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC60188;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x88UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC601C4;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x1 = unchecked((ulong)(unchecked((uint)(x20))));
        x2 = x19;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x1D8UL))));
        x3 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x1D8UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC60188;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x90UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC601C4;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x1 = unchecked((ulong)(unchecked((uint)(x20))));
        x2 = x19;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x1D8UL))));
        x3 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x1D8UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC601A0;
        }
        else
        {
            goto label_0xC60188;
        }
        label_0xC60188:
        ;
        x0 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        goto label_0xC60194;
        label_0xC60190:
        ;
        x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xC60194;
        label_0xC60194:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return unchecked((uint)(x0));
        label_0xC601A0:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x98UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC601C4;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x1 = unchecked((ulong)(unchecked((uint)(x20))));
        x2 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x4 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x1D8UL))));
        x3 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x1D8UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return unchecked((uint)(RuntimeCalls.InvokeIndirect(x4)));
        label_0xC601C4:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        return default(uint);
    }
```

## `TouchGestureStateBinding.OnIsEmulatingMousePosition` — RVA `0xc601c8`

- Lift status: **exact**; input span: 388 bytes; span to next metadata RVA: 388 bytes.
- Metadata signature: `protected override bool OnIsEmulatingMousePosition() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=56 (informational only).

```csharp
public static uint TouchGestureStateBinding_OnIsEmulatingMousePosition_RVAc601c8(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x8UL))), x19);
        x19 = x0;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xA0UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC60348;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x208UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x210UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC60320;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xA8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC60348;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x208UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x210UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC60320;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xB0UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC60348;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x208UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x210UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC60320;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xB8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC60348;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x208UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x210UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC60320;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xC0UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC60348;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x208UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x210UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC60320;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xC8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC60348;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x208UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x210UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC60320;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xD0UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC60348;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x208UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x210UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC60320;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xD8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC60348;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x208UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x210UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC60320;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x100UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC60348;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x208UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x210UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC60320;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xF8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC60348;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x208UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x210UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC60320;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xE0UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC60348;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x208UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x210UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC60320;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xE8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC60348;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x208UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x210UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC6032C;
        }
        else
        {
            goto label_0xC60320;
        }
        label_0xC60320:
        ;
        x0 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return unchecked((uint)(x0));
        label_0xC6032C:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xF0UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC60348;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x208UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x210UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return unchecked((uint)(RuntimeCalls.InvokeIndirect(x2)));
        label_0xC60348:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(uint);
    }
```

## `TouchGestureStateBinding.OnIsEmulatingTouches` — RVA `0xc6034c`

- Lift status: **exact**; input span: 336 bytes; span to next metadata RVA: 336 bytes.
- Metadata signature: `protected override bool OnIsEmulatingTouches() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=43 (informational only).

```csharp
public static uint TouchGestureStateBinding_OnIsEmulatingTouches_RVAc6034c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x8UL))), x19);
        x19 = x0;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xA0UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC60498;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x1F8UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x1F8UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC60474;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xA8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC60498;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x1F8UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x1F8UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC60474;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xB0UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC60498;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x1F8UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x1F8UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC60474;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xB8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC60498;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x1F8UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x1F8UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC60474;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xC0UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC60498;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x1F8UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x1F8UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC60474;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xC8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC60498;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x1F8UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x1F8UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC60474;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xD0UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC60498;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x1F8UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x1F8UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC60474;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xD8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC60498;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x1F8UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x1F8UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC60474;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x100UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC60498;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x1F8UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x1F8UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC60474;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xF8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC60498;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x1F8UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x1F8UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC60474;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xE0UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC60498;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x1F8UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x1F8UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC60474;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xE8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC60498;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x1F8UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x1F8UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC60480;
        }
        else
        {
            goto label_0xC60474;
        }
        label_0xC60474:
        ;
        x0 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return unchecked((uint)(x0));
        label_0xC60480:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xF0UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC60498;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x1F8UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x1F8UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return unchecked((uint)(RuntimeCalls.InvokeIndirect(x2)));
        label_0xC60498:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(uint);
    }
```

## `TouchGestureStateBinding.OnGetSubBindingDescriptions` — RVA `0xc6049c`

- Lift status: **exact**; input span: 1340 bytes; span to next metadata RVA: 1340 bytes.
- Metadata signature: `protected override void OnGetSubBindingDescriptions(BindingDescriptionList descList, Object undoObject, string parentMenuPath) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=269 (informational only).

```csharp
public static ulong TouchGestureStateBinding_OnGetSubBindingDescriptions_RVAc6049c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x22 = default(ulong);
        ulong x23 = default(ulong);
        ulong x24 = default(ulong);
        ulong x25 = default(ulong);
        ulong x26 = default(ulong);
        ulong x27 = default(ulong);
        ulong x28 = default(ulong);
        ulong x29 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFA0UL)))) + (0x0UL))), x29);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFA0UL)))) + (0x8UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x28);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x27);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x26);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x25);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x0UL))), x24);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x8UL))), x19);
        x23 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x23) + (0x2DEUL))))))));
        x20 = x3;
        x19 = x2;
        x21 = x1;
        x22 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC60628;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x60UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x68UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x70UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x78UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x80UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x88UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x90UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x98UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xA0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xA8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xC0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xC8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xE0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xE8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xF0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xF8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x100UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x108UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x110UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x118UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x120UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x128UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x130UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x138UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x23) + (0x2DEUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC60628;
        label_0xC60628:
        ;
        if ((x21 == 0x0UL))
        {
            goto label_0xC609D4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xD0UL))));
        x26 = 0x1A8D000UL;
        x27 = 0x1A8D000UL;
        x28 = 0x1A8D000UL;
        x25 = 0x1A8D000UL;
        x24 = 0x1A8D000UL;
        x23 = 0x1A8D000UL;
        x29 = 0x1A8D000UL;
        x26 = RuntimeMemory.ReadU64(unchecked((ulong)((x26) + (0xB0UL))));
        x27 = RuntimeMemory.ReadU64(unchecked((ulong)((x27) + (0x98UL))));
        x28 = RuntimeMemory.ReadU64(unchecked((ulong)((x28) + (0xE8UL))));
        x25 = RuntimeMemory.ReadU64(unchecked((ulong)((x25) + (0x120UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((x24) + (0x88UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0x130UL))));
        x29 = RuntimeMemory.ReadU64(unchecked((ulong)((x29) + (0xF8UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x20UL))));
        x2 = RuntimeMemory.ReadU64(x8);
        x0 = x21;
        x3 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xC5D750UL /* metadata target: BindingDescriptionList.Add */, x0, x1, x2, x3);
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x28UL))));
        x2 = RuntimeMemory.ReadU64(x26);
        x0 = x21;
        x3 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xC5D750UL /* metadata target: BindingDescriptionList.Add */, x0, x1, x2, x3);
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x30UL))));
        x2 = RuntimeMemory.ReadU64(x27);
        x0 = x21;
        x3 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xC5D750UL /* metadata target: BindingDescriptionList.Add */, x0, x1, x2, x3);
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x38UL))));
        x2 = RuntimeMemory.ReadU64(x28);
        x0 = x21;
        x3 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xC5D750UL /* metadata target: BindingDescriptionList.Add */, x0, x1, x2, x3);
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x40UL))));
        x2 = RuntimeMemory.ReadU64(x25);
        x0 = x21;
        x3 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xC5D750UL /* metadata target: BindingDescriptionList.Add */, x0, x1, x2, x3);
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x48UL))));
        x2 = RuntimeMemory.ReadU64(x24);
        x0 = x21;
        x3 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xC5D750UL /* metadata target: BindingDescriptionList.Add */, x0, x1, x2, x3);
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x80UL))));
        x2 = RuntimeMemory.ReadU64(x23);
        x0 = x21;
        x3 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xC5D750UL /* metadata target: BindingDescriptionList.Add */, x0, x1, x2, x3);
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x88UL))));
        x2 = RuntimeMemory.ReadU64(x29);
        x0 = x21;
        x3 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xC5D750UL /* metadata target: BindingDescriptionList.Add */, x0, x1, x2, x3);
        x8 = 0x1A8D000UL;
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x90UL))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x68UL))));
        x0 = x21;
        x3 = x20;
        x2 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xC5D750UL /* metadata target: BindingDescriptionList.Add */, x0, x1, x2, x3);
        x8 = 0x1A8D000UL;
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x98UL))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xC0UL))));
        x0 = x21;
        x3 = x20;
        x2 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xC5D750UL /* metadata target: BindingDescriptionList.Add */, x0, x1, x2, x3);
        x8 = 0x1A8D000UL;
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x60UL))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x100UL))));
        x2 = unchecked((ulong)(unchecked((uint)(0x3UL))));
        x0 = x21;
        x3 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xC5DAACUL /* metadata target: BindingDescriptionList.Add */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x8 = 0x1A8D000UL;
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x68UL))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x78UL))));
        x2 = unchecked((ulong)(unchecked((uint)(0x3UL))));
        x0 = x21;
        x3 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xC5DAACUL /* metadata target: BindingDescriptionList.Add */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x8 = 0x1A8D000UL;
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x70UL))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x70UL))));
        x2 = unchecked((ulong)(unchecked((uint)(0x3UL))));
        x0 = x21;
        x3 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xC5DAACUL /* metadata target: BindingDescriptionList.Add */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x8 = 0x1A8D000UL;
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x78UL))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xE0UL))));
        x2 = unchecked((ulong)(unchecked((uint)(0x3UL))));
        x0 = x21;
        x3 = RuntimeMemory.ReadU64(x8);
        x5 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xC5DAACUL /* metadata target: BindingDescriptionList.Add */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x8 = 0x1A8D000UL;
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x50UL))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x0 = x21;
        x3 = x20;
        x2 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xC5D750UL /* metadata target: BindingDescriptionList.Add */, x0, x1, x2, x3);
        x8 = 0x1A8D000UL;
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x58UL))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x80UL))));
        x0 = x21;
        x3 = x20;
        x2 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xC5D750UL /* metadata target: BindingDescriptionList.Add */, x0, x1, x2, x3);
        x8 = 0x1A8D000UL;
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0xF8UL))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x118UL))));
        x0 = x21;
        x3 = x20;
        x2 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xC5D750UL /* metadata target: BindingDescriptionList.Add */, x0, x1, x2, x3);
        x8 = 0x1A8D000UL;
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x100UL))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xC8UL))));
        x0 = x21;
        x3 = x20;
        x2 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xC5D750UL /* metadata target: BindingDescriptionList.Add */, x0, x1, x2, x3);
        x8 = 0x1A8D000UL;
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0xA0UL))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x90UL))));
        x0 = x21;
        x3 = x20;
        x2 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xC5D750UL /* metadata target: BindingDescriptionList.Add */, x0, x1, x2, x3);
        x8 = 0x1A8D000UL;
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0xA8UL))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xA0UL))));
        x0 = x21;
        x3 = x20;
        x2 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xC5D750UL /* metadata target: BindingDescriptionList.Add */, x0, x1, x2, x3);
        x8 = 0x1A8D000UL;
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0xB0UL))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x110UL))));
        x0 = x21;
        x3 = x20;
        x2 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xC5D750UL /* metadata target: BindingDescriptionList.Add */, x0, x1, x2, x3);
        x8 = 0x1A8D000UL;
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0xB8UL))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xD8UL))));
        x0 = x21;
        x3 = x20;
        x2 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xC5D750UL /* metadata target: BindingDescriptionList.Add */, x0, x1, x2, x3);
        x8 = 0x1A8D000UL;
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0xC0UL))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x128UL))));
        x0 = x21;
        x3 = x20;
        x2 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xC5D750UL /* metadata target: BindingDescriptionList.Add */, x0, x1, x2, x3);
        x8 = 0x1A8D000UL;
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0xC8UL))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xA8UL))));
        x0 = x21;
        x3 = x20;
        x2 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xC5D750UL /* metadata target: BindingDescriptionList.Add */, x0, x1, x2, x3);
        x8 = 0x1A8D000UL;
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0xD0UL))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x138UL))));
        x0 = x21;
        x3 = x20;
        x2 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xC5D750UL /* metadata target: BindingDescriptionList.Add */, x0, x1, x2, x3);
        x8 = 0x1A8D000UL;
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0xD8UL))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x108UL))));
        x0 = x21;
        x3 = x20;
        x2 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xC5D750UL /* metadata target: BindingDescriptionList.Add */, x0, x1, x2, x3);
        x8 = 0x1A8D000UL;
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0xE8UL))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xF0UL))));
        x0 = x21;
        x3 = x20;
        x2 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xC5D750UL /* metadata target: BindingDescriptionList.Add */, x0, x1, x2, x3);
        x8 = 0x1A8D000UL;
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0xF0UL))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x60UL))));
        x0 = x21;
        x3 = x20;
        x4 = x19;
        x2 = RuntimeMemory.ReadU64(x8);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x50UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x40UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))));
        x26 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x25 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x28 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x27 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x29 = RuntimeMemory.ReadU64(sp);
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeDirect(0xC5D750UL /* metadata target: BindingDescriptionList.Add */);
        label_0xC609D4:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```
