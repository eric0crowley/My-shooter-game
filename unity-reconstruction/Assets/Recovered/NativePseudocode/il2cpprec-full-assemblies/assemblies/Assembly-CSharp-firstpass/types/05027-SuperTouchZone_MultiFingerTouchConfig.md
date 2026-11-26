# `SuperTouchZone.MultiFingerTouchConfig` — TypeDefIndex 5027

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x10` | `TouchGestureStateBinding` | `binding` |
| `0x18` | `bool` | `driveOtherControl` |
| `0x20` | `TouchControl` | `controlToDriveOnRawPress` |
| `0x28` | `TouchControl` | `controlToDriveOnNormalPress` |
| `0x30` | `TouchControl` | `controlToDriveOnLongPress` |
| `0x38` | `TouchControl` | `controlToDriveOnNormalPressSwipe` |
| `0x40` | `TouchControl` | `controlToDriveOnNormalPressSwipeU` |
| `0x48` | `TouchControl` | `controlToDriveOnNormalPressSwipeR` |
| `0x50` | `TouchControl` | `controlToDriveOnNormalPressSwipeD` |
| `0x58` | `TouchControl` | `controlToDriveOnNormalPressSwipeL` |
| `0x60` | `TouchControl` | `controlToDriveOnLongPressSwipe` |
| `0x68` | `TouchControl` | `controlToDriveOnLongPressSwipeU` |
| `0x70` | `TouchControl` | `controlToDriveOnLongPressSwipeR` |
| `0x78` | `TouchControl` | `controlToDriveOnLongPressSwipeD` |
| `0x80` | `TouchControl` | `controlToDriveOnLongPressSwipeL` |
| `0x88` | `TouchGestureConfig` | `touchConfig` |
| `0x90` | `JoystickConfig` | `swipeJoyConfig` |

## `SuperTouchZone.MultiFingerTouchConfig.ctor` — RVA `0xc49670`

- Lift status: **exact**; input span: 236 bytes; span to next metadata RVA: 236 bytes.
- Metadata signature: `public void .ctor() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=37 (informational only).

```csharp
public static ulong SuperTouchZone_MultiFingerTouchConfig_ctor_RVAc49670(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x22 = default(ulong);
        ulong x23 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFD0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFD0UL)))) + (0x8UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x19);
        x23 = 0x1BAB000UL;
        x20 = 0x1A8C000UL;
        x22 = 0x1A8C000UL;
        x21 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x23) + (0x23EUL))))))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xC28UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0xC30UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x60UL))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC496D0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x60UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xC30UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xC28UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x23) + (0x23EUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC496D0;
        label_0xC496D0:
        ;
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1589338UL /* metadata target: Object.ctor */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x20);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = 0x0UL;
        x2 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC5E9E4UL /* metadata target: TouchGestureStateBinding.ctor */, x0, x1, x2, x3);
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x10UL))), x20);
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x18UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        x0 = RuntimeMemory.ReadU64(x22);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC61AB8UL /* metadata target: TouchGestureConfig.ctor */, x0, x1, x2, x3);
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x88UL))), x20);
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x21);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC609D8UL /* metadata target: JoystickConfig.ctor */, x0, x1, x2, x3);
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x90UL))), x20);
        x0 = x19;
        x1 = x20;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeDirect(0xB7D8D0UL);
        return default(ulong);
    }
```
