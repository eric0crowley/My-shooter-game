# `TouchJoystickSpriteAnimator` — TypeDefIndex 5016

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0xF0` | `TouchJoystickSpriteAnimator.SpriteMode` | `spriteMode` |
| `0xF8` | `SpriteConfig` | `spriteNeutralPressed` |
| `0x100` | `SpriteConfig` | `spriteUp` |
| `0x108` | `SpriteConfig` | `spriteUpRight` |
| `0x110` | `SpriteConfig` | `spriteRight` |
| `0x118` | `SpriteConfig` | `spriteDownRight` |
| `0x120` | `SpriteConfig` | `spriteDown` |
| `0x128` | `SpriteConfig` | `spriteDownLeft` |
| `0x130` | `SpriteConfig` | `spriteLeft` |
| `0x138` | `SpriteConfig` | `spriteUpLeft` |
| `0x140` | `bool` | `animateTransl` |
| `0x144` | `Vector2` | `moveScale` |
| `0x14C` | `float` | `translationSmoothingTime` |
| `0x150` | `TouchJoystickSpriteAnimator.RotationMode` | `rotationMode` |
| `0x154` | `float` | `simpleRotationRange` |
| `0x158` | `float` | `rotationSmoothingTime` |
| `0x15C` | `float` | `lastSafeCompassAngle` |

## `TouchJoystickSpriteAnimator.ctor` — RVA `0xc44f64`

- Lift status: **exact**; input span: 656 bytes; span to next metadata RVA: 656 bytes.
- Metadata signature: `public void .ctor() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=104 (informational only).

```csharp
public static ulong TouchJoystickSpriteAnimator_ctor_RVAc44f64(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_load_address_12866028 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x22 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteF64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFD0UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        sp = unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFD0UL)));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x8UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x19);
        x22 = 0x1BAB000UL;
        x20 = 0x1A8C000UL;
        x21 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x22) + (0x21CUL))))))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xB80UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x3D0UL))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC44FC0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB58UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB80UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x3D0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x22) + (0x21CUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC44FC0;
        label_0xC44FC0:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(0xCCCDUL))));
        x8 = unchecked((ulong)(unchecked((uint)(unchecked((ulong)((unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((~(0xFFFFUL)))))))))) | (unchecked((ulong)((unchecked((ulong)((0x3DCCUL) << (int)(unchecked((int)(0x10UL)))))) << (int)(unchecked((int)(0x0UL))))))))))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x19) + (0x14CUL))), unchecked((uint)(x8)));
        RuntimeMemory.WriteU32(unchecked((ulong)((x19) + (0x158UL))), unchecked((uint)(x8)));
        x0 = RuntimeMemory.ReadU64(x21);
        x21 = 0x1A8C000UL;
        x20 = RuntimeMemory.ReadU64(x20);
        x22 = unchecked((ulong)((x19) + (0x144UL)));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xB58UL))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC44FF0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC44FECUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC44FF0;
        label_0xC44FF0:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1556240UL /* metadata target: Type.GetTypeFromHandle */, x0, x1, x2, x3);
        x1 = x0;
        x0 = x19;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC63A74UL /* metadata target: TouchControlSpriteAnimatorBase.ctor */, x0, x1, x2, x3);
        x8 = 0x431000UL;
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((x8) + (0xC38UL))))), 0));
        v1 = (RuntimeVector128.Zero.WithUInt32(0, unchecked((uint)((unchecked((uint)0x3FUL)) << (int)(unchecked((int)(unchecked((uint)0x18UL))))))) | RuntimeVector128.Zero.WithUInt32(0, unchecked((uint)((unchecked((uint)0x3FUL)) << (int)(unchecked((int)(unchecked((uint)0x18UL))))))).ShiftLeftLogical(unchecked((int)0x20UL)));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x140UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        RuntimeMemory.WriteF64(x22, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0)))));
        RuntimeMemory.WritePtr(unchecked((ulong)((x19) + (0x150UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        RuntimeMemory.WriteF64(unchecked((ulong)((x22) + (0x10UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))));
        RuntimeMemory.WritePtr(unchecked((ulong)((x19) + (0x15CUL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        x0 = RuntimeMemory.ReadU64(x21);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x8 = 0x432000UL;
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x3E0UL))))), 0));
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x2 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x3 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC63528UL /* metadata target: SpriteConfig.ctor */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), x3);
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0xF8UL))), x20);
        x0 = x19;
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = RuntimeMemory.ReadU64(x21);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x2 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x3 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC63528UL /* metadata target: SpriteConfig.ctor */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = unchecked((ulong)((x19) + (0x8UL)));
        x1 = x20;
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x8UL))), x20);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = RuntimeMemory.ReadU64(x21);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x2 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x3 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC63528UL /* metadata target: SpriteConfig.ctor */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = unchecked((ulong)((x19) + (0x10UL)));
        x1 = x20;
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x10UL))), x20);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = RuntimeMemory.ReadU64(x21);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x2 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x3 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC63528UL /* metadata target: SpriteConfig.ctor */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = unchecked((ulong)((x19) + (0x18UL)));
        x1 = x20;
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x18UL))), x20);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = RuntimeMemory.ReadU64(x21);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x2 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x3 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC63528UL /* metadata target: SpriteConfig.ctor */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = unchecked((ulong)((x19) + (0x20UL)));
        x1 = x20;
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x20UL))), x20);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = RuntimeMemory.ReadU64(x21);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x2 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x3 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC63528UL /* metadata target: SpriteConfig.ctor */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = unchecked((ulong)((x19) + (0x28UL)));
        x1 = x20;
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x28UL))), x20);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = RuntimeMemory.ReadU64(x21);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x2 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x3 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC63528UL /* metadata target: SpriteConfig.ctor */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = unchecked((ulong)((x19) + (0x30UL)));
        x1 = x20;
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x30UL))), x20);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = RuntimeMemory.ReadU64(x21);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x2 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x3 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC63528UL /* metadata target: SpriteConfig.ctor */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = unchecked((ulong)((x19) + (0x38UL)));
        x1 = x20;
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x38UL))), x20);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = RuntimeMemory.ReadU64(x21);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x2 = unchecked((ulong)(unchecked((uint)0x0UL)));
        v0 = v8;
        x3 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC63528UL /* metadata target: SpriteConfig.ctor */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = unchecked((ulong)((x19) + (0x40UL)));
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x40UL))), x20);
        x1 = x20;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        __arm64_load_address_12866028 = sp;
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_load_address_12866028)), 0));
        sp = unchecked((ulong)((__arm64_load_address_12866028) + (0x30UL)));
        return RuntimeCalls.InvokeDirect(0xB7D8D0UL);
        return default(ulong);
    }
```

## `TouchJoystickSpriteAnimator.SetSprite` — RVA `0xc451f4`

- Lift status: **exact**; input span: 224 bytes; span to next metadata RVA: 224 bytes.
- Metadata signature: `public void SetSprite(Sprite sprite) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=23 (informational only).

```csharp
public static ulong TouchJoystickSpriteAnimator_SetSprite_RVAc451f4(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x30 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        x20 = x0;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x78UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC452D0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC45208UL);
        }
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x18UL))), x1);
        x19 = x1;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xF8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC452D0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC4521CUL);
        }
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x18UL))), x19);
        x1 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x100UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC452D0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC45230UL);
        }
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x18UL))), x19);
        x1 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x108UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC452D0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC45244UL);
        }
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x18UL))), x19);
        x1 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x110UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC452D0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC45258UL);
        }
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x18UL))), x19);
        x1 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x118UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC452D0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC4526CUL);
        }
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x18UL))), x19);
        x1 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x120UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC452D0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC45280UL);
        }
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x18UL))), x19);
        x1 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x128UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC452D0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC45294UL);
        }
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x18UL))), x19);
        x1 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x130UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC452D0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC452A8UL);
        }
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x18UL))), x19);
        x1 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x138UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC452D0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC452BCUL);
        }
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x18UL))), x19);
        x1 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0xB7D8D0UL);
        label_0xC452D0:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `TouchJoystickSpriteAnimator.SetColor` — RVA `0xc452d4`

- Lift status: **exact**; input span: 176 bytes; span to next metadata RVA: 176 bytes.
- Metadata signature: `public void SetColor(Color color) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=11 (informational only).

```csharp
public static ulong TouchJoystickSpriteAnimator_SetColor_RVAc452d4(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_pair_address_12866272 = default(ulong);
        ulong __arm64_pair_address_12866276 = default(ulong);
        ulong __arm64_pair_address_12866288 = default(ulong);
        ulong __arm64_pair_address_12866292 = default(ulong);
        ulong __arm64_pair_address_12866304 = default(ulong);
        ulong __arm64_pair_address_12866308 = default(ulong);
        ulong __arm64_pair_address_12866320 = default(ulong);
        ulong __arm64_pair_address_12866324 = default(ulong);
        ulong __arm64_pair_address_12866336 = default(ulong);
        ulong __arm64_pair_address_12866340 = default(ulong);
        ulong __arm64_pair_address_12866352 = default(ulong);
        ulong __arm64_pair_address_12866356 = default(ulong);
        ulong __arm64_pair_address_12866368 = default(ulong);
        ulong __arm64_pair_address_12866372 = default(ulong);
        ulong __arm64_pair_address_12866384 = default(ulong);
        ulong __arm64_pair_address_12866388 = default(ulong);
        ulong __arm64_pair_address_12866400 = default(ulong);
        ulong __arm64_pair_address_12866404 = default(ulong);
        ulong __arm64_pair_address_12866416 = default(ulong);
        ulong __arm64_pair_address_12866420 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL))), x30);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x78UL))));
        if ((x8 == 0x0UL))
        {
        }
        else
        {
            __arm64_pair_address_12866272 = unchecked((ulong)((x8) + (0x20UL)));
            RuntimeMemory.WriteF32(__arm64_pair_address_12866272, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
            RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_12866272) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0));
            __arm64_pair_address_12866276 = unchecked((ulong)((x8) + (0x28UL)));
            RuntimeMemory.WriteF32(__arm64_pair_address_12866276, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0));
            RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_12866276) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0));
            x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xF8UL))));
            if ((x8 == 0x0UL))
            {
            }
            else
            {
                __arm64_pair_address_12866288 = unchecked((ulong)((x8) + (0x20UL)));
                RuntimeMemory.WriteF32(__arm64_pair_address_12866288, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
                RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_12866288) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0));
                __arm64_pair_address_12866292 = unchecked((ulong)((x8) + (0x28UL)));
                RuntimeMemory.WriteF32(__arm64_pair_address_12866292, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0));
                RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_12866292) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0));
                x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x100UL))));
                if ((x8 == 0x0UL))
                {
                }
                else
                {
                    __arm64_pair_address_12866304 = unchecked((ulong)((x8) + (0x20UL)));
                    RuntimeMemory.WriteF32(__arm64_pair_address_12866304, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
                    RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_12866304) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0));
                    __arm64_pair_address_12866308 = unchecked((ulong)((x8) + (0x28UL)));
                    RuntimeMemory.WriteF32(__arm64_pair_address_12866308, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0));
                    RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_12866308) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0));
                    x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x108UL))));
                    if ((x8 == 0x0UL))
                    {
                    }
                    else
                    {
                        __arm64_pair_address_12866320 = unchecked((ulong)((x8) + (0x20UL)));
                        RuntimeMemory.WriteF32(__arm64_pair_address_12866320, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
                        RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_12866320) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0));
                        __arm64_pair_address_12866324 = unchecked((ulong)((x8) + (0x28UL)));
                        RuntimeMemory.WriteF32(__arm64_pair_address_12866324, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0));
                        RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_12866324) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0));
                        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x110UL))));
                        if ((x8 == 0x0UL))
                        {
                        }
                        else
                        {
                            __arm64_pair_address_12866336 = unchecked((ulong)((x8) + (0x20UL)));
                            RuntimeMemory.WriteF32(__arm64_pair_address_12866336, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
                            RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_12866336) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0));
                            __arm64_pair_address_12866340 = unchecked((ulong)((x8) + (0x28UL)));
                            RuntimeMemory.WriteF32(__arm64_pair_address_12866340, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0));
                            RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_12866340) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0));
                            x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x118UL))));
                            if ((x8 == 0x0UL))
                            {
                            }
                            else
                            {
                                __arm64_pair_address_12866352 = unchecked((ulong)((x8) + (0x20UL)));
                                RuntimeMemory.WriteF32(__arm64_pair_address_12866352, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
                                RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_12866352) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0));
                                __arm64_pair_address_12866356 = unchecked((ulong)((x8) + (0x28UL)));
                                RuntimeMemory.WriteF32(__arm64_pair_address_12866356, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0));
                                RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_12866356) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0));
                                x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x120UL))));
                                if ((x8 == 0x0UL))
                                {
                                }
                                else
                                {
                                    __arm64_pair_address_12866368 = unchecked((ulong)((x8) + (0x20UL)));
                                    RuntimeMemory.WriteF32(__arm64_pair_address_12866368, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
                                    RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_12866368) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0));
                                    __arm64_pair_address_12866372 = unchecked((ulong)((x8) + (0x28UL)));
                                    RuntimeMemory.WriteF32(__arm64_pair_address_12866372, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0));
                                    RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_12866372) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0));
                                    x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x128UL))));
                                    if ((x8 == 0x0UL))
                                    {
                                    }
                                    else
                                    {
                                        __arm64_pair_address_12866384 = unchecked((ulong)((x8) + (0x20UL)));
                                        RuntimeMemory.WriteF32(__arm64_pair_address_12866384, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
                                        RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_12866384) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0));
                                        __arm64_pair_address_12866388 = unchecked((ulong)((x8) + (0x28UL)));
                                        RuntimeMemory.WriteF32(__arm64_pair_address_12866388, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0));
                                        RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_12866388) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0));
                                        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x130UL))));
                                        if ((x8 == 0x0UL))
                                        {
                                        }
                                        else
                                        {
                                            __arm64_pair_address_12866400 = unchecked((ulong)((x8) + (0x20UL)));
                                            RuntimeMemory.WriteF32(__arm64_pair_address_12866400, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
                                            RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_12866400) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0));
                                            __arm64_pair_address_12866404 = unchecked((ulong)((x8) + (0x28UL)));
                                            RuntimeMemory.WriteF32(__arm64_pair_address_12866404, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0));
                                            RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_12866404) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0));
                                            x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x138UL))));
                                            if ((x8 == 0x0UL))
                                            {
                                            }
                                            else
                                            {
                                                __arm64_pair_address_12866416 = unchecked((ulong)((x8) + (0x20UL)));
                                                RuntimeMemory.WriteF32(__arm64_pair_address_12866416, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
                                                RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_12866416) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0));
                                                __arm64_pair_address_12866420 = unchecked((ulong)((x8) + (0x28UL)));
                                                RuntimeMemory.WriteF32(__arm64_pair_address_12866420, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0));
                                                RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_12866420) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0));
                                                x30 = RuntimeMemory.ReadU64(sp);
                                                return x0;
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
        label_0xC45380:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `TouchJoystickSpriteAnimator.SetStateSprite` — RVA `0xc45384`

- Lift status: **exact**; input span: 64 bytes; span to next metadata RVA: 64 bytes.
- Metadata signature: `public void SetStateSprite(TouchJoystickSpriteAnimator.ControlState state, Sprite sprite) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=9 (informational only).

```csharp
public static ulong TouchJoystickSpriteAnimator_SetStateSprite_RVAc45384(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x30 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        x19 = x2;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC453C4UL /* metadata target: TouchJoystickSpriteAnimator.GetStateSpriteConfig */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC453B0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC4539CUL);
        }
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x18UL))), x19);
        x1 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0xB7D8D0UL);
        label_0xC453B0:
        ;
        x0 = x20;
        x1 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0xC451F4UL /* metadata target: TouchJoystickSpriteAnimator.SetSprite */);
        return default(ulong);
    }
```

## `TouchJoystickSpriteAnimator.GetStateSpriteConfig` — RVA `0xc453c4`

- Lift status: **exact**; input span: 128 bytes; span to next metadata RVA: 128 bytes.
- Metadata signature: `public SpriteConfig GetStateSpriteConfig(TouchJoystickSpriteAnimator.ControlState state) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=28 (informational only).

```csharp
public static ulong TouchJoystickSpriteAnimator_GetStateSpriteConfig_RVAc453c4(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12866500 = default(uint);
        uint __arm64_flags_right_12866500 = default(uint);
        ulong x10 = default(ulong);
        ulong x11 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        __arm64_flags_left_12866500 = unchecked((uint)(x1));
        __arm64_flags_right_12866500 = unchecked((uint)0x9UL);
        if (((__arm64_flags_left_12866500 >= __arm64_flags_right_12866500) && (!((unchecked((uint)((__arm64_flags_left_12866500) - (__arm64_flags_right_12866500))) == unchecked((uint)0x0UL))))))
        {
            goto label_0xC453F0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = 0x452000UL;
        x8 = unchecked((ulong)(unchecked((uint)(x1))));
        x9 = unchecked((ulong)((x9) + (0xD4UL)));
        x10 = 0xC453E8UL;
        x11 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x9) + (unchecked((ulong)(unchecked((uint)(x8))))))))))));
        x10 = unchecked((ulong)((x10) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x11))) << (int)(unchecked((int)(unchecked((uint)(0x2UL))))))))))));
        return RuntimeCalls.InvokeIndirect(x10);
        label_0xC453F0:
        ;
        x0 = 0x0UL;
        return x0;
        return default(ulong);
    }
```

## `TouchJoystickSpriteAnimator.SetStateColor` — RVA `0xc45444`

- Lift status: **exact**; input span: 100 bytes; span to next metadata RVA: 100 bytes.
- Metadata signature: `public void SetStateColor(TouchJoystickSpriteAnimator.ControlState state, Color color) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=12 (informational only).

```csharp
public static ulong TouchJoystickSpriteAnimator_SetStateColor_RVAc45444(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_pair_address_12866628 = default(ulong);
        ulong __arm64_pair_address_12866632 = default(ulong);
        ulong __arm64_pair_address_12866668 = default(ulong);
        ulong __arm64_pair_address_12866676 = default(ulong);
        ulong __arm64_pair_address_12866680 = default(ulong);
        ulong __arm64_pair_address_12866684 = default(ulong);
        ulong __arm64_pair_address_12866708 = default(ulong);
        ulong __arm64_pair_address_12866720 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v10 = default(RuntimeVector128);
        RuntimeVector128 v11 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        RuntimeVector128 v9 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        __arm64_pair_address_12866628 = unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFD0UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12866628, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v11.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12866628) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v10.GetUInt64(0)))));
        sp = __arm64_pair_address_12866628;
        __arm64_pair_address_12866632 = unchecked((ulong)((sp) + (0x10UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12866632, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12866632) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x19);
        v8 = v3;
        v9 = v2;
        v10 = v1;
        v11 = v0;
        x19 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC453C4UL /* metadata target: TouchJoystickSpriteAnimator.GetStateSpriteConfig */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC45484;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC4546CUL);
        }
        __arm64_pair_address_12866668 = unchecked((ulong)((x0) + (0x28UL)));
        RuntimeMemory.WriteF32(__arm64_pair_address_12866668, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_12866668) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        __arm64_pair_address_12866676 = unchecked((ulong)((sp) + (0x10UL)));
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12866676)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12866676) + (0x8UL))))), 0));
        __arm64_pair_address_12866680 = unchecked((ulong)((x0) + (0x20UL)));
        RuntimeMemory.WriteF32(__arm64_pair_address_12866680, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_12866680) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0));
        __arm64_pair_address_12866684 = sp;
        v11 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12866684)), 0));
        v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12866684) + (0x8UL))))), 0));
        return x0;
        label_0xC45484:
        ;
        x0 = x19;
        v2 = v9;
        v3 = v8;
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        __arm64_pair_address_12866708 = unchecked((ulong)((sp) + (0x10UL)));
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12866708)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12866708) + (0x8UL))))), 0));
        v0 = v11;
        v1 = v10;
        __arm64_pair_address_12866720 = sp;
        v11 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12866720)), 0));
        v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12866720) + (0x8UL))))), 0));
        sp = unchecked((ulong)((__arm64_pair_address_12866720) + (0x30UL)));
        return RuntimeCalls.InvokeDirect(0xC452D4UL /* metadata target: TouchJoystickSpriteAnimator.SetColor */);
        return default(ulong);
    }
```

## `TouchJoystickSpriteAnimator.OnInitComponent` — RVA `0xc454a8`

- Lift status: **exact**; input span: 504 bytes; span to next metadata RVA: 504 bytes.
- Metadata signature: `protected override void OnInitComponent() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=64 (informational only).

```csharp
public static ulong TouchJoystickSpriteAnimator_OnInitComponent_RVAc454a8(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
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
        x20 = 0x1BAB000UL;
        x21 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x21DUL))))))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xD8UL))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC454DC;
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
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x21DUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC454DC;
        label_0xC454DC:
        ;
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC63B4CUL /* metadata target: TouchControlSpriteAnimatorBase.OnInitComponent */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x21);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x40UL))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC454FC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC454F8UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC454FC;
        label_0xC454FC:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794AC8UL /* metadata target: Object.op_Inequality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC45690;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x40UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC4569C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(x21);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xD8UL))));
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC4552C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC45528UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC4552C;
        label_0xC4552C:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794AC8UL /* metadata target: Object.op_Inequality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC45690;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x78UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC4569C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(x21);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x18UL))));
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC4555C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC45558UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC4555C;
        label_0xC4555C:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179568CUL /* metadata target: Object.op_Equality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC45690;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x40UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC4569C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x78UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC4569C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xD8UL))));
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x18UL))), x1);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x40UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC4569C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xF8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC4569C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xD8UL))));
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x18UL))), x1);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x40UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC4569C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x100UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC4569C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xD8UL))));
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x18UL))), x1);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x40UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC4569C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x108UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC4569C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xD8UL))));
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x18UL))), x1);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x40UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC4569C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x110UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC4569C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xD8UL))));
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x18UL))), x1);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x40UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC4569C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x118UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC4569C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xD8UL))));
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x18UL))), x1);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x40UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC4569C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x120UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC4569C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xD8UL))));
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x18UL))), x1);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x40UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC4569C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x128UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC4569C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xD8UL))));
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x18UL))), x1);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x40UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC4569C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x130UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC4569C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xD8UL))));
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x18UL))), x1);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x40UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC4569C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x138UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC4569C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xD8UL))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x18UL))), x1);
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeDirect(0xB7D8D0UL);
        label_0xC45690:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return x0;
        label_0xC4569C:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `TouchJoystickSpriteAnimator.OnUpdateAnimator` — RVA `0xc456a0`

- Lift status: **exact**; input span: 928 bytes; span to next metadata RVA: 928 bytes.
- Metadata signature: `protected override void OnUpdateAnimator(bool skipAnim) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=119 (informational only).

```csharp
public static ulong TouchJoystickSpriteAnimator_OnUpdateAnimator_RVAc456a0(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12867344 = default(uint);
        ulong __arm64_flags_left_12867364 = default(ulong);
        uint __arm64_flags_left_12867500 = default(uint);
        uint __arm64_flags_left_12867508 = default(uint);
        uint __arm64_flags_left_12867556 = default(uint);
        uint __arm64_flags_left_12867692 = default(uint);
        uint __arm64_flags_left_12867880 = default(uint);
        uint __arm64_flags_left_12867996 = default(uint);
        uint __arm64_flags_right_12867344 = default(uint);
        ulong __arm64_flags_right_12867364 = default(ulong);
        uint __arm64_flags_right_12867500 = default(uint);
        uint __arm64_flags_right_12867508 = default(uint);
        uint __arm64_flags_right_12867556 = default(uint);
        uint __arm64_flags_right_12867692 = default(uint);
        uint __arm64_flags_right_12867880 = default(uint);
        uint __arm64_flags_right_12867996 = default(uint);
        float __arm64_float_flags_left_12867904 = default(float);
        float __arm64_float_flags_right_12867904 = default(float);
        ulong __arm64_load_address_12867480 = default(ulong);
        ulong __arm64_load_address_12868140 = default(ulong);
        ulong __arm64_pair_address_12867236 = default(ulong);
        ulong __arm64_pair_address_12867240 = default(ulong);
        ulong __arm64_pair_address_12867472 = default(ulong);
        ulong __arm64_pair_address_12867476 = default(ulong);
        ulong __arm64_pair_address_12867724 = default(ulong);
        ulong __arm64_pair_address_12867788 = default(ulong);
        ulong __arm64_pair_address_12867876 = default(ulong);
        ulong __arm64_pair_address_12868128 = default(ulong);
        ulong __arm64_pair_address_12868132 = default(ulong);
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
        ulong x10 = default(ulong);
        ulong x11 = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x22 = default(ulong);
        ulong x23 = default(ulong);
        ulong x24 = default(ulong);
        ulong x25 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteF64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFF90UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v12.GetUInt64(0)))));
        sp = unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFF90UL)));
        __arm64_pair_address_12867236 = unchecked((ulong)((sp) + (0x10UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12867236, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v11.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12867236) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v10.GetUInt64(0)))));
        __arm64_pair_address_12867240 = unchecked((ulong)((sp) + (0x20UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12867240, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12867240) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))), x25);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x0UL))), x24);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x8UL))), x19);
        x21 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x21EUL))))))));
        x20 = unchecked((ulong)(unchecked((uint)(x1))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC456F0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB88UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x21EUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC456F0;
        label_0xC456F0:
        ;
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x28UL))));
        if ((x21 == 0x0UL))
        {
            goto label_0xC4572C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = 0x1A8C000UL;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0xB88UL))));
        x8 = RuntimeMemory.ReadU64(x21);
        x1 = RuntimeMemory.ReadU64(x9);
        x10 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x130UL))))))));
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x1) + (0x130UL))))))));
        __arm64_flags_left_12867344 = unchecked((uint)(x10));
        __arm64_flags_right_12867344 = unchecked((uint)(x9));
        if ((!((__arm64_flags_left_12867344 >= __arm64_flags_right_12867344))))
        {
            goto label_0xC45A34;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xC8UL))));
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) << (int)(unchecked((int)(unchecked((uint)(0x3UL))))))))))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xFFFFFFFFFFFFFFF8UL))));
        __arm64_flags_left_12867364 = x8;
        __arm64_flags_right_12867364 = x1;
        if ((!((unchecked((ulong)((__arm64_flags_left_12867364) - (__arm64_flags_right_12867364))) == 0x0UL))))
        {
            goto label_0xC45A34;
        }
        else
        {
            goto label_0xC4572C;
        }
        label_0xC4572C:
        ;
        x22 = 0x1A8C000UL;
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0xD8UL))));
        x0 = RuntimeMemory.ReadU64(x22);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC45744;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC45740UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC45744;
        label_0xC45744:
        ;
        x0 = x21;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179568CUL /* metadata target: Object.op_Equality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC45780;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(x22);
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x40UL))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC4576C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC45768UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC4576C;
        label_0xC4576C:
        ;
        x0 = x22;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179568CUL /* metadata target: Object.op_Equality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC457A0;
        }
        else
        {
            goto label_0xC45780;
        }
        label_0xC45780:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x60UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x50UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x8UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x40UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
        x25 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))));
        __arm64_pair_address_12867472 = unchecked((ulong)((sp) + (0x20UL)));
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12867472)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12867472) + (0x8UL))))), 0));
        __arm64_pair_address_12867476 = unchecked((ulong)((sp) + (0x10UL)));
        v11 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12867476)), 0));
        v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12867476) + (0x8UL))))), 0));
        __arm64_load_address_12867480 = sp;
        v12 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_load_address_12867480)), 0));
        return x0;
        label_0xC457A0:
        ;
        if ((x21 == 0x0UL))
        {
            goto label_0xC45A3C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0xF0UL))))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x180UL))));
        __arm64_flags_left_12867500 = unchecked((uint)(x8));
        __arm64_flags_right_12867500 = unchecked((uint)0x2UL);
        if ((unchecked((uint)((__arm64_flags_left_12867500) - (__arm64_flags_right_12867500))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC457D0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC457B4UL);
        }
        __arm64_flags_left_12867508 = unchecked((uint)(x8));
        __arm64_flags_right_12867508 = unchecked((uint)0x1UL);
        if ((!((unchecked((uint)((__arm64_flags_left_12867508) - (__arm64_flags_right_12867508))) == unchecked((uint)0x0UL)))))
        {
            goto label_0xC4580C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC457BCUL);
        }
        if ((x22 == 0x0UL))
        {
            goto label_0xC45A3C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x22;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC60D68UL /* metadata target: JoystickState.GetDir4 */, x0, x1, x2, x3);
        goto label_0xC457E0;
        label_0xC457D0:
        ;
        if ((x22 == 0x0UL))
        {
            goto label_0xC45A3C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x22;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC60D84UL /* metadata target: JoystickState.GetDir8 */, x0, x1, x2, x3);
        goto label_0xC457E0;
        label_0xC457E0:
        ;
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) - (unchecked((uint)(0x1UL)))))));
        __arm64_flags_left_12867556 = unchecked((uint)(x8));
        __arm64_flags_right_12867556 = unchecked((uint)0x7UL);
        if (((__arm64_flags_left_12867556 >= __arm64_flags_right_12867556) && (!((unchecked((uint)((__arm64_flags_left_12867556) - (__arm64_flags_right_12867556))) == unchecked((uint)0x0UL))))))
        {
            goto label_0xC4580C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = 0x452000UL;
        x9 = unchecked((ulong)((x9) + (0xDEUL)));
        x10 = 0xC45804UL;
        x11 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x9) + (unchecked((ulong)(unchecked((uint)(x8))))))))))));
        x10 = unchecked((ulong)((x10) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x11))) << (int)(unchecked((int)(unchecked((uint)(0x2UL))))))))))));
        return RuntimeCalls.InvokeIndirect(x10);
        label_0xC4580C:
        ;
        x23 = 0x0UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xE0UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC45A3C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x1CUL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC45830;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC45820UL);
        }
        if ((x23 == 0x0UL))
        {
            goto label_0xC4582C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x23) + (0x10UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC45840;
        }
        else
        {
            goto label_0xC4582C;
        }
        label_0xC4582C:
        ;
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xF8UL))));
        goto label_0xC45830;
        label_0xC45830:
        ;
        if ((x23 == 0x0UL))
        {
            goto label_0xC4583C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x23) + (0x10UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC45840;
        }
        else
        {
            goto label_0xC4583C;
        }
        label_0xC4583C:
        ;
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x78UL))));
        goto label_0xC45840;
        label_0xC45840:
        ;
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC58364UL /* metadata target: CFUtils.get_editorStopped */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC459EC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC63890UL /* metadata target: TouchControlAnimatorBase.IsIllegallyAttachedToSource */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC459EC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC4585CUL);
        }
        if ((x22 == 0x0UL))
        {
            goto label_0xC45A3C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x21) + (0x38UL))))));
        x0 = x22;
        x2 = 0x0UL;
        __arm64_flags_left_12867692 = unchecked((uint)(x8));
        __arm64_flags_right_12867692 = unchecked((uint)0x2UL);
        x1 = unchecked((ulong)(((!((__arm64_flags_left_12867692 >= __arm64_flags_right_12867692))) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xC60C94UL /* metadata target: JoystickState.GetVectorEx */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x140UL))))))));
        x24 = 0x432000UL;
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC458D4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC45884UL);
        }
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x144UL))))), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x148UL))))), 0));
        __arm64_pair_address_12867724 = unchecked((ulong)((x19) + (0xDCUL)));
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12867724)), 0));
        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12867724) + (0x4UL))))), 0));
        v10 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x14CUL))))), 0));
        x0 = 0x0UL;
        v11 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
        v12 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0))))), 0));
        x0 = RuntimeCalls.InvokeDirect(0xC5834CUL /* metadata target: CFUtils.get_realDeltaTimeClamped */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        v6 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x24) + (0x2E8UL))))), 0));
        v5 = v0;
        v7 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F400000UL)), 0)), 0));
        v0 = v8;
        v1 = v9;
        v2 = v11;
        v3 = v12;
        v4 = v10;
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC5877CUL /* metadata target: CFUtils.SmoothTowardsVec2 */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        __arm64_pair_address_12867788 = unchecked((ulong)((x19) + (0xDCUL)));
        RuntimeMemory.WriteF32(__arm64_pair_address_12867788, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_12867788) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0));
        goto label_0xC4590C;
        label_0xC458D4:
        ;
        x25 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x25) + (0x1E0UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC458F4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x138UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x25) + (0x1E0UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC458F4;
        label_0xC458F4:
        ;
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x138UL))));
        x8 = RuntimeMemory.ReadU64(x8);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(x8)), 0));
        RuntimeMemory.WriteF64(unchecked((ulong)((x19) + (0xDCUL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))));
        goto label_0xC4590C;
        label_0xC4590C:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x150UL))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC459EC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xE0UL))));
        if ((x9 == 0x0UL))
        {
            goto label_0xC45A3C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x9) + (0x1CUL))))))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC4598C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC45924UL);
        }
        __arm64_pair_address_12867876 = unchecked((ulong)((x22) + (0x24UL)));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12867876)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12867876) + (0x4UL))))), 0));
        __arm64_flags_left_12867880 = unchecked((uint)(x8));
        __arm64_flags_right_12867880 = unchecked((uint)0x3UL);
        if ((!((unchecked((uint)((__arm64_flags_left_12867880) - (__arm64_flags_right_12867880))) == unchecked((uint)0x0UL)))))
        {
            goto label_0xC45998;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC45930UL);
        }
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x24) + (0x2E8UL))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        __arm64_float_flags_left_12867904 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12867904 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_12867904 <= __arm64_float_flags_right_12867904) || ((__arm64_float_flags_left_12867904 != __arm64_float_flags_left_12867904) || (__arm64_float_flags_right_12867904 != __arm64_float_flags_right_12867904))))
        {
            goto label_0xC459B0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC45948UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x22) + (0x1CUL))))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((x19) + (0x15CUL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        goto label_0xC459B4;
        label_0xC4598C:
        ;
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        RuntimeMemory.WritePtr(unchecked((ulong)((x19) + (0x15CUL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        goto label_0xC459B8;
        label_0xC45998:
        ;
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x154UL))))), 0));
        __arm64_flags_left_12867996 = unchecked((uint)(x8));
        __arm64_flags_right_12867996 = unchecked((uint)0x1UL);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((unchecked((uint)((__arm64_flags_left_12867996) - (__arm64_flags_right_12867996))) == unchecked((uint)0x0UL)) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes((-(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0)))), 0));
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        goto label_0xC459B8;
        label_0xC459B0:
        ;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x15CUL))))), 0));
        goto label_0xC459B4;
        label_0xC459B4:
        ;
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes((-(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)))), 0));
        goto label_0xC459B8;
        label_0xC459B8:
        ;
        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0xECUL))))), 0));
        v10 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x158UL))))), 0));
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC5834CUL /* metadata target: CFUtils.get_realDeltaTimeClamped */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x24) + (0x2E8UL))))), 0));
        v3 = v0;
        v5 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F400000UL)), 0)), 0));
        v0 = v9;
        v1 = v8;
        v2 = v10;
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC58674UL /* metadata target: CFUtils.SmoothTowardsAngle */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        RuntimeMemory.WriteF32(unchecked((ulong)((x19) + (0xECUL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        goto label_0xC459EC;
        label_0xC459EC:
        ;
        x20 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x20))) & (unchecked((uint)(0x1UL)))))));
        x0 = x19;
        x1 = x23;
        x2 = unchecked((ulong)(unchecked((uint)(x20))));
        x3 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x4 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC63E00UL /* metadata target: TouchControlSpriteAnimatorBase.BeginSpriteAnim */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x0 = x19;
        x1 = unchecked((ulong)(unchecked((uint)(x20))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x60UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x50UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x8UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x40UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
        x25 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))));
        __arm64_pair_address_12868128 = unchecked((ulong)((sp) + (0x20UL)));
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12868128)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12868128) + (0x8UL))))), 0));
        __arm64_pair_address_12868132 = unchecked((ulong)((sp) + (0x10UL)));
        v11 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12868132)), 0));
        v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12868132) + (0x8UL))))), 0));
        x2 = 0x0UL;
        __arm64_load_address_12868140 = sp;
        v12 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_load_address_12868140)), 0));
        sp = unchecked((ulong)((__arm64_load_address_12868140) + (0x70UL)));
        return RuntimeCalls.InvokeDirect(0xC64384UL /* metadata target: TouchControlSpriteAnimatorBase.UpdateSpriteAnimation */);
        label_0xC45A34:
        ;
        x0 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xB7DF10UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, unchecked((ulong)(unchecked((uint)(x3)))));
        goto label_0xC45A3C;
        label_0xC45A3C:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, unchecked((ulong)(unchecked((uint)(x3)))));
        return default(ulong);
    }
```

## `TouchJoystickSpriteAnimator.GetComponent` — RVA `0xc45a40`

- Lift status: **exact**; input span: 4 bytes; span to next metadata RVA: 4 bytes.
- Metadata signature: `private MonoBehaviour ControlFreak2.Internal.ISpriteAnimator.GetComponent() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=0 (informational only).

```csharp
public static ulong TouchJoystickSpriteAnimator_GetComponent_RVAc45a40(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        return x0;
        return default(ulong);
    }
```

## `TouchJoystickSpriteAnimator.AddUsedSprites` — RVA `0xc45a44`

- Lift status: **partial**; input span: 1160 bytes; span to next metadata RVA: 1160 bytes.
- Metadata signature: `private void ControlFreak2.Internal.ISpriteAnimator.AddUsedSprites(ISpriteOptimizer optimizer) { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=192 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'b.ne' at 0xc45abc; reason: Unknown IR expression at 0xc45abc; reason: Unsupported instruction 'b.ne' at 0xc45b28; reason: Unknown IR expression at 0xc45b28; reason: Unsupported instruction 'b.ne' at 0xc45b94; reason: Unknown IR expression at 0xc45b94; reason: Unsupported instruction 'b.ne' at 0xc45c00; reason: Unknown IR expression at 0xc45c00

```csharp
public static ulong TouchJoystickSpriteAnimator_AddUsedSprites_RVAc45a44(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_flags_left_12868268 = default(ulong);
        ulong __arm64_flags_left_12868276 = default(ulong);
        ulong __arm64_flags_left_12868376 = default(ulong);
        ulong __arm64_flags_left_12868384 = default(ulong);
        ulong __arm64_flags_left_12868484 = default(ulong);
        ulong __arm64_flags_left_12868492 = default(ulong);
        ulong __arm64_flags_left_12868592 = default(ulong);
        ulong __arm64_flags_left_12868600 = default(ulong);
        ulong __arm64_flags_left_12868700 = default(ulong);
        ulong __arm64_flags_left_12868708 = default(ulong);
        ulong __arm64_flags_left_12868808 = default(ulong);
        ulong __arm64_flags_left_12868816 = default(ulong);
        ulong __arm64_flags_left_12868916 = default(ulong);
        ulong __arm64_flags_left_12868924 = default(ulong);
        ulong __arm64_flags_left_12869024 = default(ulong);
        ulong __arm64_flags_left_12869032 = default(ulong);
        ulong __arm64_flags_left_12869132 = default(ulong);
        ulong __arm64_flags_left_12869140 = default(ulong);
        ulong __arm64_flags_left_12869240 = default(ulong);
        ulong __arm64_flags_left_12869248 = default(ulong);
        ulong __arm64_flags_result_12868276 = default(ulong);
        ulong __arm64_flags_result_12868384 = default(ulong);
        ulong __arm64_flags_result_12868492 = default(ulong);
        ulong __arm64_flags_result_12868600 = default(ulong);
        ulong __arm64_flags_result_12868708 = default(ulong);
        ulong __arm64_flags_result_12868816 = default(ulong);
        ulong __arm64_flags_result_12868924 = default(ulong);
        ulong __arm64_flags_result_12869032 = default(ulong);
        ulong __arm64_flags_result_12869140 = default(ulong);
        ulong __arm64_flags_result_12869248 = default(ulong);
        ulong __arm64_flags_right_12868268 = default(ulong);
        ulong __arm64_flags_right_12868276 = default(ulong);
        ulong __arm64_flags_right_12868376 = default(ulong);
        ulong __arm64_flags_right_12868384 = default(ulong);
        ulong __arm64_flags_right_12868484 = default(ulong);
        ulong __arm64_flags_right_12868492 = default(ulong);
        ulong __arm64_flags_right_12868592 = default(ulong);
        ulong __arm64_flags_right_12868600 = default(ulong);
        ulong __arm64_flags_right_12868700 = default(ulong);
        ulong __arm64_flags_right_12868708 = default(ulong);
        ulong __arm64_flags_right_12868808 = default(ulong);
        ulong __arm64_flags_right_12868816 = default(ulong);
        ulong __arm64_flags_right_12868916 = default(ulong);
        ulong __arm64_flags_right_12868924 = default(ulong);
        ulong __arm64_flags_right_12869024 = default(ulong);
        ulong __arm64_flags_right_12869032 = default(ulong);
        ulong __arm64_flags_right_12869132 = default(ulong);
        ulong __arm64_flags_right_12869140 = default(ulong);
        ulong __arm64_flags_right_12869240 = default(ulong);
        ulong __arm64_flags_right_12869248 = default(ulong);
        ulong sp = default(ulong);
        ulong x10 = default(ulong);
        ulong x11 = default(ulong);
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
        x21 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x21FUL))))))));
        x19 = x1;
        x20 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC45A78;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB68UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x21FUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC45A78;
        label_0xC45A78:
        ;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x78UL))));
        if ((x9 == 0x0UL))
        {
            goto label_0xC45EC8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC45A80UL);
        }
        if ((x19 == 0x0UL))
        {
            goto label_0xC45EC8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x22 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(x19);
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0xB68UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0x18UL))));
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU16(unchecked((ulong)((x8) + (0x12EUL))))))));
        x1 = RuntimeMemory.ReadU64(x22);
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC45AC0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB0UL))));
        x10 = unchecked((ulong)((x10) + (0x8UL)));
        goto label_0xC45AA8;
        label_0xC45AA8:
        ;
        x11 = RuntimeMemory.ReadU64(unchecked((ulong)((x10) + (0xFFFFFFFFFFFFFFF8UL))));
        __arm64_flags_left_12868268 = x11;
        __arm64_flags_right_12868268 = x1;
        if ((unchecked((ulong)((__arm64_flags_left_12868268) - (__arm64_flags_right_12868268))) == 0x0UL))
        {
            goto label_0xC45AD0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC45AB4UL);
        }
        __arm64_flags_left_12868276 = x9;
        __arm64_flags_right_12868276 = 0x1UL;
        __arm64_flags_result_12868276 = unchecked((ulong)((__arm64_flags_left_12868276) - (__arm64_flags_right_12868276)));
        x9 = __arm64_flags_result_12868276;
        x10 = unchecked((ulong)((x10) + (0x10UL)));
        RuntimeCalls.Unsupported("b.ne", 0xC45ABCUL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC45AA8;
        }
        else
        {
            goto label_0xC45AC0;
        }
        label_0xC45AC0:
        ;
        x2 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xB80110UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC45AE0;
        label_0xC45AD0:
        ;
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(x10)));
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) + (unchecked((uint)(0x1UL)))))));
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) << (int)(unchecked((int)(unchecked((uint)(0x4UL))))))))))));
        x0 = unchecked((ulong)((x8) + (0x138UL)));
        goto label_0xC45AE0;
        label_0xC45AE0:
        ;
        x8 = RuntimeMemory.ReadU64(x0);
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x8UL))));
        x0 = x19;
        x1 = x21;
        x0 = RuntimeCalls.InvokeIndirect(x8, x0, x1, x2, x3);
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xF8UL))));
        if ((x9 == 0x0UL))
        {
            goto label_0xC45EC8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x19);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0x18UL))));
        x1 = RuntimeMemory.ReadU64(x22);
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU16(unchecked((ulong)((x8) + (0x12EUL))))))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC45B2C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB0UL))));
        x10 = unchecked((ulong)((x10) + (0x8UL)));
        goto label_0xC45B14;
        label_0xC45B14:
        ;
        x11 = RuntimeMemory.ReadU64(unchecked((ulong)((x10) + (0xFFFFFFFFFFFFFFF8UL))));
        __arm64_flags_left_12868376 = x11;
        __arm64_flags_right_12868376 = x1;
        if ((unchecked((ulong)((__arm64_flags_left_12868376) - (__arm64_flags_right_12868376))) == 0x0UL))
        {
            goto label_0xC45B3C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC45B20UL);
        }
        __arm64_flags_left_12868384 = x9;
        __arm64_flags_right_12868384 = 0x1UL;
        __arm64_flags_result_12868384 = unchecked((ulong)((__arm64_flags_left_12868384) - (__arm64_flags_right_12868384)));
        x9 = __arm64_flags_result_12868384;
        x10 = unchecked((ulong)((x10) + (0x10UL)));
        RuntimeCalls.Unsupported("b.ne", 0xC45B28UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC45B14;
        }
        else
        {
            goto label_0xC45B2C;
        }
        label_0xC45B2C:
        ;
        x2 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xB80110UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC45B4C;
        label_0xC45B3C:
        ;
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(x10)));
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) + (unchecked((uint)(0x1UL)))))));
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) << (int)(unchecked((int)(unchecked((uint)(0x4UL))))))))))));
        x0 = unchecked((ulong)((x8) + (0x138UL)));
        goto label_0xC45B4C;
        label_0xC45B4C:
        ;
        x8 = RuntimeMemory.ReadU64(x0);
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x8UL))));
        x0 = x19;
        x1 = x21;
        x0 = RuntimeCalls.InvokeIndirect(x8, x0, x1, x2, x3);
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x100UL))));
        if ((x9 == 0x0UL))
        {
            goto label_0xC45EC8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x19);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0x18UL))));
        x1 = RuntimeMemory.ReadU64(x22);
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU16(unchecked((ulong)((x8) + (0x12EUL))))))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC45B98;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB0UL))));
        x10 = unchecked((ulong)((x10) + (0x8UL)));
        goto label_0xC45B80;
        label_0xC45B80:
        ;
        x11 = RuntimeMemory.ReadU64(unchecked((ulong)((x10) + (0xFFFFFFFFFFFFFFF8UL))));
        __arm64_flags_left_12868484 = x11;
        __arm64_flags_right_12868484 = x1;
        if ((unchecked((ulong)((__arm64_flags_left_12868484) - (__arm64_flags_right_12868484))) == 0x0UL))
        {
            goto label_0xC45BA8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC45B8CUL);
        }
        __arm64_flags_left_12868492 = x9;
        __arm64_flags_right_12868492 = 0x1UL;
        __arm64_flags_result_12868492 = unchecked((ulong)((__arm64_flags_left_12868492) - (__arm64_flags_right_12868492)));
        x9 = __arm64_flags_result_12868492;
        x10 = unchecked((ulong)((x10) + (0x10UL)));
        RuntimeCalls.Unsupported("b.ne", 0xC45B94UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC45B80;
        }
        else
        {
            goto label_0xC45B98;
        }
        label_0xC45B98:
        ;
        x2 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xB80110UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC45BB8;
        label_0xC45BA8:
        ;
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(x10)));
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) + (unchecked((uint)(0x1UL)))))));
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) << (int)(unchecked((int)(unchecked((uint)(0x4UL))))))))))));
        x0 = unchecked((ulong)((x8) + (0x138UL)));
        goto label_0xC45BB8;
        label_0xC45BB8:
        ;
        x8 = RuntimeMemory.ReadU64(x0);
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x8UL))));
        x0 = x19;
        x1 = x21;
        x0 = RuntimeCalls.InvokeIndirect(x8, x0, x1, x2, x3);
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x108UL))));
        if ((x9 == 0x0UL))
        {
            goto label_0xC45EC8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x19);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0x18UL))));
        x1 = RuntimeMemory.ReadU64(x22);
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU16(unchecked((ulong)((x8) + (0x12EUL))))))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC45C04;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB0UL))));
        x10 = unchecked((ulong)((x10) + (0x8UL)));
        goto label_0xC45BEC;
        label_0xC45BEC:
        ;
        x11 = RuntimeMemory.ReadU64(unchecked((ulong)((x10) + (0xFFFFFFFFFFFFFFF8UL))));
        __arm64_flags_left_12868592 = x11;
        __arm64_flags_right_12868592 = x1;
        if ((unchecked((ulong)((__arm64_flags_left_12868592) - (__arm64_flags_right_12868592))) == 0x0UL))
        {
            goto label_0xC45C14;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC45BF8UL);
        }
        __arm64_flags_left_12868600 = x9;
        __arm64_flags_right_12868600 = 0x1UL;
        __arm64_flags_result_12868600 = unchecked((ulong)((__arm64_flags_left_12868600) - (__arm64_flags_right_12868600)));
        x9 = __arm64_flags_result_12868600;
        x10 = unchecked((ulong)((x10) + (0x10UL)));
        RuntimeCalls.Unsupported("b.ne", 0xC45C00UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC45BEC;
        }
        else
        {
            goto label_0xC45C04;
        }
        label_0xC45C04:
        ;
        x2 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xB80110UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC45C24;
        label_0xC45C14:
        ;
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(x10)));
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) + (unchecked((uint)(0x1UL)))))));
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) << (int)(unchecked((int)(unchecked((uint)(0x4UL))))))))))));
        x0 = unchecked((ulong)((x8) + (0x138UL)));
        goto label_0xC45C24;
        label_0xC45C24:
        ;
        x8 = RuntimeMemory.ReadU64(x0);
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x8UL))));
        x0 = x19;
        x1 = x21;
        x0 = RuntimeCalls.InvokeIndirect(x8, x0, x1, x2, x3);
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x110UL))));
        if ((x9 == 0x0UL))
        {
            goto label_0xC45EC8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x19);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0x18UL))));
        x1 = RuntimeMemory.ReadU64(x22);
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU16(unchecked((ulong)((x8) + (0x12EUL))))))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC45C70;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB0UL))));
        x10 = unchecked((ulong)((x10) + (0x8UL)));
        goto label_0xC45C58;
        label_0xC45C58:
        ;
        x11 = RuntimeMemory.ReadU64(unchecked((ulong)((x10) + (0xFFFFFFFFFFFFFFF8UL))));
        __arm64_flags_left_12868700 = x11;
        __arm64_flags_right_12868700 = x1;
        if ((unchecked((ulong)((__arm64_flags_left_12868700) - (__arm64_flags_right_12868700))) == 0x0UL))
        {
            goto label_0xC45C80;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC45C64UL);
        }
        __arm64_flags_left_12868708 = x9;
        __arm64_flags_right_12868708 = 0x1UL;
        __arm64_flags_result_12868708 = unchecked((ulong)((__arm64_flags_left_12868708) - (__arm64_flags_right_12868708)));
        x9 = __arm64_flags_result_12868708;
        x10 = unchecked((ulong)((x10) + (0x10UL)));
        RuntimeCalls.Unsupported("b.ne", 0xC45C6CUL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC45C58;
        }
        else
        {
            goto label_0xC45C70;
        }
        label_0xC45C70:
        ;
        x2 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xB80110UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC45C90;
        label_0xC45C80:
        ;
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(x10)));
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) + (unchecked((uint)(0x1UL)))))));
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) << (int)(unchecked((int)(unchecked((uint)(0x4UL))))))))))));
        x0 = unchecked((ulong)((x8) + (0x138UL)));
        goto label_0xC45C90;
        label_0xC45C90:
        ;
        x8 = RuntimeMemory.ReadU64(x0);
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x8UL))));
        x0 = x19;
        x1 = x21;
        x0 = RuntimeCalls.InvokeIndirect(x8, x0, x1, x2, x3);
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x118UL))));
        if ((x9 == 0x0UL))
        {
            goto label_0xC45EC8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x19);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0x18UL))));
        x1 = RuntimeMemory.ReadU64(x22);
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU16(unchecked((ulong)((x8) + (0x12EUL))))))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC45CDC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB0UL))));
        x10 = unchecked((ulong)((x10) + (0x8UL)));
        goto label_0xC45CC4;
        label_0xC45CC4:
        ;
        x11 = RuntimeMemory.ReadU64(unchecked((ulong)((x10) + (0xFFFFFFFFFFFFFFF8UL))));
        __arm64_flags_left_12868808 = x11;
        __arm64_flags_right_12868808 = x1;
        if ((unchecked((ulong)((__arm64_flags_left_12868808) - (__arm64_flags_right_12868808))) == 0x0UL))
        {
            goto label_0xC45CEC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC45CD0UL);
        }
        __arm64_flags_left_12868816 = x9;
        __arm64_flags_right_12868816 = 0x1UL;
        __arm64_flags_result_12868816 = unchecked((ulong)((__arm64_flags_left_12868816) - (__arm64_flags_right_12868816)));
        x9 = __arm64_flags_result_12868816;
        x10 = unchecked((ulong)((x10) + (0x10UL)));
        RuntimeCalls.Unsupported("b.ne", 0xC45CD8UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC45CC4;
        }
        else
        {
            goto label_0xC45CDC;
        }
        label_0xC45CDC:
        ;
        x2 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xB80110UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC45CFC;
        label_0xC45CEC:
        ;
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(x10)));
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) + (unchecked((uint)(0x1UL)))))));
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) << (int)(unchecked((int)(unchecked((uint)(0x4UL))))))))))));
        x0 = unchecked((ulong)((x8) + (0x138UL)));
        goto label_0xC45CFC;
        label_0xC45CFC:
        ;
        x8 = RuntimeMemory.ReadU64(x0);
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x8UL))));
        x0 = x19;
        x1 = x21;
        x0 = RuntimeCalls.InvokeIndirect(x8, x0, x1, x2, x3);
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x120UL))));
        if ((x9 == 0x0UL))
        {
            goto label_0xC45EC8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x19);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0x18UL))));
        x1 = RuntimeMemory.ReadU64(x22);
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU16(unchecked((ulong)((x8) + (0x12EUL))))))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC45D48;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB0UL))));
        x10 = unchecked((ulong)((x10) + (0x8UL)));
        goto label_0xC45D30;
        label_0xC45D30:
        ;
        x11 = RuntimeMemory.ReadU64(unchecked((ulong)((x10) + (0xFFFFFFFFFFFFFFF8UL))));
        __arm64_flags_left_12868916 = x11;
        __arm64_flags_right_12868916 = x1;
        if ((unchecked((ulong)((__arm64_flags_left_12868916) - (__arm64_flags_right_12868916))) == 0x0UL))
        {
            goto label_0xC45D58;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC45D3CUL);
        }
        __arm64_flags_left_12868924 = x9;
        __arm64_flags_right_12868924 = 0x1UL;
        __arm64_flags_result_12868924 = unchecked((ulong)((__arm64_flags_left_12868924) - (__arm64_flags_right_12868924)));
        x9 = __arm64_flags_result_12868924;
        x10 = unchecked((ulong)((x10) + (0x10UL)));
        RuntimeCalls.Unsupported("b.ne", 0xC45D44UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC45D30;
        }
        else
        {
            goto label_0xC45D48;
        }
        label_0xC45D48:
        ;
        x2 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xB80110UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC45D68;
        label_0xC45D58:
        ;
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(x10)));
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) + (unchecked((uint)(0x1UL)))))));
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) << (int)(unchecked((int)(unchecked((uint)(0x4UL))))))))))));
        x0 = unchecked((ulong)((x8) + (0x138UL)));
        goto label_0xC45D68;
        label_0xC45D68:
        ;
        x8 = RuntimeMemory.ReadU64(x0);
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x8UL))));
        x0 = x19;
        x1 = x21;
        x0 = RuntimeCalls.InvokeIndirect(x8, x0, x1, x2, x3);
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x128UL))));
        if ((x9 == 0x0UL))
        {
            goto label_0xC45EC8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x19);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0x18UL))));
        x1 = RuntimeMemory.ReadU64(x22);
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU16(unchecked((ulong)((x8) + (0x12EUL))))))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC45DB4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB0UL))));
        x10 = unchecked((ulong)((x10) + (0x8UL)));
        goto label_0xC45D9C;
        label_0xC45D9C:
        ;
        x11 = RuntimeMemory.ReadU64(unchecked((ulong)((x10) + (0xFFFFFFFFFFFFFFF8UL))));
        __arm64_flags_left_12869024 = x11;
        __arm64_flags_right_12869024 = x1;
        if ((unchecked((ulong)((__arm64_flags_left_12869024) - (__arm64_flags_right_12869024))) == 0x0UL))
        {
            goto label_0xC45DC4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC45DA8UL);
        }
        __arm64_flags_left_12869032 = x9;
        __arm64_flags_right_12869032 = 0x1UL;
        __arm64_flags_result_12869032 = unchecked((ulong)((__arm64_flags_left_12869032) - (__arm64_flags_right_12869032)));
        x9 = __arm64_flags_result_12869032;
        x10 = unchecked((ulong)((x10) + (0x10UL)));
        RuntimeCalls.Unsupported("b.ne", 0xC45DB0UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC45D9C;
        }
        else
        {
            goto label_0xC45DB4;
        }
        label_0xC45DB4:
        ;
        x2 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xB80110UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC45DD4;
        label_0xC45DC4:
        ;
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(x10)));
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) + (unchecked((uint)(0x1UL)))))));
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) << (int)(unchecked((int)(unchecked((uint)(0x4UL))))))))))));
        x0 = unchecked((ulong)((x8) + (0x138UL)));
        goto label_0xC45DD4;
        label_0xC45DD4:
        ;
        x8 = RuntimeMemory.ReadU64(x0);
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x8UL))));
        x0 = x19;
        x1 = x21;
        x0 = RuntimeCalls.InvokeIndirect(x8, x0, x1, x2, x3);
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x130UL))));
        if ((x9 == 0x0UL))
        {
            goto label_0xC45EC8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x19);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0x18UL))));
        x1 = RuntimeMemory.ReadU64(x22);
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU16(unchecked((ulong)((x8) + (0x12EUL))))))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC45E20;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB0UL))));
        x10 = unchecked((ulong)((x10) + (0x8UL)));
        goto label_0xC45E08;
        label_0xC45E08:
        ;
        x11 = RuntimeMemory.ReadU64(unchecked((ulong)((x10) + (0xFFFFFFFFFFFFFFF8UL))));
        __arm64_flags_left_12869132 = x11;
        __arm64_flags_right_12869132 = x1;
        if ((unchecked((ulong)((__arm64_flags_left_12869132) - (__arm64_flags_right_12869132))) == 0x0UL))
        {
            goto label_0xC45E30;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC45E14UL);
        }
        __arm64_flags_left_12869140 = x9;
        __arm64_flags_right_12869140 = 0x1UL;
        __arm64_flags_result_12869140 = unchecked((ulong)((__arm64_flags_left_12869140) - (__arm64_flags_right_12869140)));
        x9 = __arm64_flags_result_12869140;
        x10 = unchecked((ulong)((x10) + (0x10UL)));
        RuntimeCalls.Unsupported("b.ne", 0xC45E1CUL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC45E08;
        }
        else
        {
            goto label_0xC45E20;
        }
        label_0xC45E20:
        ;
        x2 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xB80110UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC45E40;
        label_0xC45E30:
        ;
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(x10)));
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) + (unchecked((uint)(0x1UL)))))));
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) << (int)(unchecked((int)(unchecked((uint)(0x4UL))))))))))));
        x0 = unchecked((ulong)((x8) + (0x138UL)));
        goto label_0xC45E40;
        label_0xC45E40:
        ;
        x8 = RuntimeMemory.ReadU64(x0);
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x8UL))));
        x0 = x19;
        x1 = x21;
        x0 = RuntimeCalls.InvokeIndirect(x8, x0, x1, x2, x3);
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x138UL))));
        if ((x9 == 0x0UL))
        {
            goto label_0xC45EC8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x19);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0x18UL))));
        x1 = RuntimeMemory.ReadU64(x22);
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU16(unchecked((ulong)((x8) + (0x12EUL))))))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC45E8C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB0UL))));
        x10 = unchecked((ulong)((x10) + (0x8UL)));
        goto label_0xC45E74;
        label_0xC45E74:
        ;
        x11 = RuntimeMemory.ReadU64(unchecked((ulong)((x10) + (0xFFFFFFFFFFFFFFF8UL))));
        __arm64_flags_left_12869240 = x11;
        __arm64_flags_right_12869240 = x1;
        if ((unchecked((ulong)((__arm64_flags_left_12869240) - (__arm64_flags_right_12869240))) == 0x0UL))
        {
            goto label_0xC45E9C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC45E80UL);
        }
        __arm64_flags_left_12869248 = x9;
        __arm64_flags_right_12869248 = 0x1UL;
        __arm64_flags_result_12869248 = unchecked((ulong)((__arm64_flags_left_12869248) - (__arm64_flags_right_12869248)));
        x9 = __arm64_flags_result_12869248;
        x10 = unchecked((ulong)((x10) + (0x10UL)));
        RuntimeCalls.Unsupported("b.ne", 0xC45E88UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC45E74;
        }
        else
        {
            goto label_0xC45E8C;
        }
        label_0xC45E8C:
        ;
        x2 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xB80110UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC45EAC;
        label_0xC45E9C:
        ;
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(x10)));
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) + (unchecked((uint)(0x1UL)))))));
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) << (int)(unchecked((int)(unchecked((uint)(0x4UL))))))))))));
        x0 = unchecked((ulong)((x8) + (0x138UL)));
        goto label_0xC45EAC;
        label_0xC45EAC:
        ;
        x3 = RuntimeMemory.ReadU64(x0);
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x8UL))));
        x0 = x19;
        x1 = x20;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeIndirect(x3);
        label_0xC45EC8:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `TouchJoystickSpriteAnimator.OnSpriteOptimization` — RVA `0xc45ecc`

- Lift status: **partial**; input span: 1280 bytes; span to next metadata RVA: 1280 bytes.
- Metadata signature: `private void ControlFreak2.Internal.ISpriteAnimator.OnSpriteOptimization(ISpriteOptimizer optimizer) { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=202 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'b.ne' at 0xc45f44; reason: Unknown IR expression at 0xc45f44; reason: Unsupported instruction 'b.ne' at 0xc45fbc; reason: Unknown IR expression at 0xc45fbc; reason: Unsupported instruction 'b.ne' at 0xc46034; reason: Unknown IR expression at 0xc46034; reason: Unsupported instruction 'b.ne' at 0xc460ac; reason: Unknown IR expression at 0xc460ac

```csharp
public static ulong TouchJoystickSpriteAnimator_OnSpriteOptimization_RVAc45ecc(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_flags_left_12869428 = default(ulong);
        ulong __arm64_flags_left_12869436 = default(ulong);
        ulong __arm64_flags_left_12869548 = default(ulong);
        ulong __arm64_flags_left_12869556 = default(ulong);
        ulong __arm64_flags_left_12869668 = default(ulong);
        ulong __arm64_flags_left_12869676 = default(ulong);
        ulong __arm64_flags_left_12869788 = default(ulong);
        ulong __arm64_flags_left_12869796 = default(ulong);
        ulong __arm64_flags_left_12869908 = default(ulong);
        ulong __arm64_flags_left_12869916 = default(ulong);
        ulong __arm64_flags_left_12870028 = default(ulong);
        ulong __arm64_flags_left_12870036 = default(ulong);
        ulong __arm64_flags_left_12870148 = default(ulong);
        ulong __arm64_flags_left_12870156 = default(ulong);
        ulong __arm64_flags_left_12870268 = default(ulong);
        ulong __arm64_flags_left_12870276 = default(ulong);
        ulong __arm64_flags_left_12870388 = default(ulong);
        ulong __arm64_flags_left_12870396 = default(ulong);
        ulong __arm64_flags_left_12870508 = default(ulong);
        ulong __arm64_flags_left_12870516 = default(ulong);
        ulong __arm64_flags_result_12869436 = default(ulong);
        ulong __arm64_flags_result_12869556 = default(ulong);
        ulong __arm64_flags_result_12869676 = default(ulong);
        ulong __arm64_flags_result_12869796 = default(ulong);
        ulong __arm64_flags_result_12869916 = default(ulong);
        ulong __arm64_flags_result_12870036 = default(ulong);
        ulong __arm64_flags_result_12870156 = default(ulong);
        ulong __arm64_flags_result_12870276 = default(ulong);
        ulong __arm64_flags_result_12870396 = default(ulong);
        ulong __arm64_flags_result_12870516 = default(ulong);
        ulong __arm64_flags_right_12869428 = default(ulong);
        ulong __arm64_flags_right_12869436 = default(ulong);
        ulong __arm64_flags_right_12869548 = default(ulong);
        ulong __arm64_flags_right_12869556 = default(ulong);
        ulong __arm64_flags_right_12869668 = default(ulong);
        ulong __arm64_flags_right_12869676 = default(ulong);
        ulong __arm64_flags_right_12869788 = default(ulong);
        ulong __arm64_flags_right_12869796 = default(ulong);
        ulong __arm64_flags_right_12869908 = default(ulong);
        ulong __arm64_flags_right_12869916 = default(ulong);
        ulong __arm64_flags_right_12870028 = default(ulong);
        ulong __arm64_flags_right_12870036 = default(ulong);
        ulong __arm64_flags_right_12870148 = default(ulong);
        ulong __arm64_flags_right_12870156 = default(ulong);
        ulong __arm64_flags_right_12870268 = default(ulong);
        ulong __arm64_flags_right_12870276 = default(ulong);
        ulong __arm64_flags_right_12870388 = default(ulong);
        ulong __arm64_flags_right_12870396 = default(ulong);
        ulong __arm64_flags_right_12870508 = default(ulong);
        ulong __arm64_flags_right_12870516 = default(ulong);
        ulong sp = default(ulong);
        ulong x10 = default(ulong);
        ulong x11 = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x22 = default(ulong);
        ulong x23 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFD0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFD0UL)))) + (0x8UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x19);
        x21 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x220UL))))))));
        x19 = x1;
        x20 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC45F00;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB68UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x220UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC45F00;
        label_0xC45F00:
        ;
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x78UL))));
        if ((x21 == 0x0UL))
        {
            goto label_0xC463C8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x18UL))));
        if ((x19 == 0x0UL))
        {
            goto label_0xC463C8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x23 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(x19);
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0xB68UL))));
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU16(unchecked((ulong)((x8) + (0x12EUL))))))));
        x1 = RuntimeMemory.ReadU64(x23);
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC45F48;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB0UL))));
        x10 = unchecked((ulong)((x10) + (0x8UL)));
        goto label_0xC45F30;
        label_0xC45F30:
        ;
        x11 = RuntimeMemory.ReadU64(unchecked((ulong)((x10) + (0xFFFFFFFFFFFFFFF8UL))));
        __arm64_flags_left_12869428 = x11;
        __arm64_flags_right_12869428 = x1;
        if ((unchecked((ulong)((__arm64_flags_left_12869428) - (__arm64_flags_right_12869428))) == 0x0UL))
        {
            goto label_0xC45F58;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC45F3CUL);
        }
        __arm64_flags_left_12869436 = x9;
        __arm64_flags_right_12869436 = 0x1UL;
        __arm64_flags_result_12869436 = unchecked((ulong)((__arm64_flags_left_12869436) - (__arm64_flags_right_12869436)));
        x9 = __arm64_flags_result_12869436;
        x10 = unchecked((ulong)((x10) + (0x10UL)));
        RuntimeCalls.Unsupported("b.ne", 0xC45F44UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC45F30;
        }
        else
        {
            goto label_0xC45F48;
        }
        label_0xC45F48:
        ;
        x0 = x19;
        x2 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x0 = RuntimeCalls.InvokeDirect(0xB80110UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC45F64;
        label_0xC45F58:
        ;
        x9 = unchecked((ulong)(unchecked((long)(RuntimeMemory.ReadS32(x10)))));
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)((x9) << (int)(unchecked((int)(0x4UL))))))));
        x0 = unchecked((ulong)((x8) + (0x138UL)));
        goto label_0xC45F64;
        label_0xC45F64:
        ;
        x8 = RuntimeMemory.ReadU64(x0);
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x8UL))));
        x0 = x19;
        x1 = x22;
        x0 = RuntimeCalls.InvokeIndirect(x8, x0, x1, x2, x3);
        x1 = x0;
        RuntimeMemory.WriteU64(x21, x0);
        x0 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xF8UL))));
        if ((x21 == 0x0UL))
        {
            goto label_0xC463C8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x18UL))));
        x8 = RuntimeMemory.ReadU64(x19);
        x1 = RuntimeMemory.ReadU64(x23);
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU16(unchecked((ulong)((x8) + (0x12EUL))))))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC45FC0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB0UL))));
        x10 = unchecked((ulong)((x10) + (0x8UL)));
        goto label_0xC45FA8;
        label_0xC45FA8:
        ;
        x11 = RuntimeMemory.ReadU64(unchecked((ulong)((x10) + (0xFFFFFFFFFFFFFFF8UL))));
        __arm64_flags_left_12869548 = x11;
        __arm64_flags_right_12869548 = x1;
        if ((unchecked((ulong)((__arm64_flags_left_12869548) - (__arm64_flags_right_12869548))) == 0x0UL))
        {
            goto label_0xC45FD0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC45FB4UL);
        }
        __arm64_flags_left_12869556 = x9;
        __arm64_flags_right_12869556 = 0x1UL;
        __arm64_flags_result_12869556 = unchecked((ulong)((__arm64_flags_left_12869556) - (__arm64_flags_right_12869556)));
        x9 = __arm64_flags_result_12869556;
        x10 = unchecked((ulong)((x10) + (0x10UL)));
        RuntimeCalls.Unsupported("b.ne", 0xC45FBCUL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC45FA8;
        }
        else
        {
            goto label_0xC45FC0;
        }
        label_0xC45FC0:
        ;
        x0 = x19;
        x2 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x0 = RuntimeCalls.InvokeDirect(0xB80110UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC45FDC;
        label_0xC45FD0:
        ;
        x9 = unchecked((ulong)(unchecked((long)(RuntimeMemory.ReadS32(x10)))));
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)((x9) << (int)(unchecked((int)(0x4UL))))))));
        x0 = unchecked((ulong)((x8) + (0x138UL)));
        goto label_0xC45FDC;
        label_0xC45FDC:
        ;
        x8 = RuntimeMemory.ReadU64(x0);
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x8UL))));
        x0 = x19;
        x1 = x22;
        x0 = RuntimeCalls.InvokeIndirect(x8, x0, x1, x2, x3);
        x1 = x0;
        RuntimeMemory.WriteU64(x21, x0);
        x0 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x100UL))));
        if ((x21 == 0x0UL))
        {
            goto label_0xC463C8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x18UL))));
        x8 = RuntimeMemory.ReadU64(x19);
        x1 = RuntimeMemory.ReadU64(x23);
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU16(unchecked((ulong)((x8) + (0x12EUL))))))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC46038;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB0UL))));
        x10 = unchecked((ulong)((x10) + (0x8UL)));
        goto label_0xC46020;
        label_0xC46020:
        ;
        x11 = RuntimeMemory.ReadU64(unchecked((ulong)((x10) + (0xFFFFFFFFFFFFFFF8UL))));
        __arm64_flags_left_12869668 = x11;
        __arm64_flags_right_12869668 = x1;
        if ((unchecked((ulong)((__arm64_flags_left_12869668) - (__arm64_flags_right_12869668))) == 0x0UL))
        {
            goto label_0xC46048;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC4602CUL);
        }
        __arm64_flags_left_12869676 = x9;
        __arm64_flags_right_12869676 = 0x1UL;
        __arm64_flags_result_12869676 = unchecked((ulong)((__arm64_flags_left_12869676) - (__arm64_flags_right_12869676)));
        x9 = __arm64_flags_result_12869676;
        x10 = unchecked((ulong)((x10) + (0x10UL)));
        RuntimeCalls.Unsupported("b.ne", 0xC46034UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC46020;
        }
        else
        {
            goto label_0xC46038;
        }
        label_0xC46038:
        ;
        x0 = x19;
        x2 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x0 = RuntimeCalls.InvokeDirect(0xB80110UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC46054;
        label_0xC46048:
        ;
        x9 = unchecked((ulong)(unchecked((long)(RuntimeMemory.ReadS32(x10)))));
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)((x9) << (int)(unchecked((int)(0x4UL))))))));
        x0 = unchecked((ulong)((x8) + (0x138UL)));
        goto label_0xC46054;
        label_0xC46054:
        ;
        x8 = RuntimeMemory.ReadU64(x0);
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x8UL))));
        x0 = x19;
        x1 = x22;
        x0 = RuntimeCalls.InvokeIndirect(x8, x0, x1, x2, x3);
        x1 = x0;
        RuntimeMemory.WriteU64(x21, x0);
        x0 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x108UL))));
        if ((x21 == 0x0UL))
        {
            goto label_0xC463C8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x18UL))));
        x8 = RuntimeMemory.ReadU64(x19);
        x1 = RuntimeMemory.ReadU64(x23);
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU16(unchecked((ulong)((x8) + (0x12EUL))))))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC460B0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB0UL))));
        x10 = unchecked((ulong)((x10) + (0x8UL)));
        goto label_0xC46098;
        label_0xC46098:
        ;
        x11 = RuntimeMemory.ReadU64(unchecked((ulong)((x10) + (0xFFFFFFFFFFFFFFF8UL))));
        __arm64_flags_left_12869788 = x11;
        __arm64_flags_right_12869788 = x1;
        if ((unchecked((ulong)((__arm64_flags_left_12869788) - (__arm64_flags_right_12869788))) == 0x0UL))
        {
            goto label_0xC460C0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC460A4UL);
        }
        __arm64_flags_left_12869796 = x9;
        __arm64_flags_right_12869796 = 0x1UL;
        __arm64_flags_result_12869796 = unchecked((ulong)((__arm64_flags_left_12869796) - (__arm64_flags_right_12869796)));
        x9 = __arm64_flags_result_12869796;
        x10 = unchecked((ulong)((x10) + (0x10UL)));
        RuntimeCalls.Unsupported("b.ne", 0xC460ACUL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC46098;
        }
        else
        {
            goto label_0xC460B0;
        }
        label_0xC460B0:
        ;
        x0 = x19;
        x2 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x0 = RuntimeCalls.InvokeDirect(0xB80110UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC460CC;
        label_0xC460C0:
        ;
        x9 = unchecked((ulong)(unchecked((long)(RuntimeMemory.ReadS32(x10)))));
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)((x9) << (int)(unchecked((int)(0x4UL))))))));
        x0 = unchecked((ulong)((x8) + (0x138UL)));
        goto label_0xC460CC;
        label_0xC460CC:
        ;
        x8 = RuntimeMemory.ReadU64(x0);
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x8UL))));
        x0 = x19;
        x1 = x22;
        x0 = RuntimeCalls.InvokeIndirect(x8, x0, x1, x2, x3);
        x1 = x0;
        RuntimeMemory.WriteU64(x21, x0);
        x0 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x110UL))));
        if ((x21 == 0x0UL))
        {
            goto label_0xC463C8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x18UL))));
        x8 = RuntimeMemory.ReadU64(x19);
        x1 = RuntimeMemory.ReadU64(x23);
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU16(unchecked((ulong)((x8) + (0x12EUL))))))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC46128;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB0UL))));
        x10 = unchecked((ulong)((x10) + (0x8UL)));
        goto label_0xC46110;
        label_0xC46110:
        ;
        x11 = RuntimeMemory.ReadU64(unchecked((ulong)((x10) + (0xFFFFFFFFFFFFFFF8UL))));
        __arm64_flags_left_12869908 = x11;
        __arm64_flags_right_12869908 = x1;
        if ((unchecked((ulong)((__arm64_flags_left_12869908) - (__arm64_flags_right_12869908))) == 0x0UL))
        {
            goto label_0xC46138;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC4611CUL);
        }
        __arm64_flags_left_12869916 = x9;
        __arm64_flags_right_12869916 = 0x1UL;
        __arm64_flags_result_12869916 = unchecked((ulong)((__arm64_flags_left_12869916) - (__arm64_flags_right_12869916)));
        x9 = __arm64_flags_result_12869916;
        x10 = unchecked((ulong)((x10) + (0x10UL)));
        RuntimeCalls.Unsupported("b.ne", 0xC46124UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC46110;
        }
        else
        {
            goto label_0xC46128;
        }
        label_0xC46128:
        ;
        x0 = x19;
        x2 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x0 = RuntimeCalls.InvokeDirect(0xB80110UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC46144;
        label_0xC46138:
        ;
        x9 = unchecked((ulong)(unchecked((long)(RuntimeMemory.ReadS32(x10)))));
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)((x9) << (int)(unchecked((int)(0x4UL))))))));
        x0 = unchecked((ulong)((x8) + (0x138UL)));
        goto label_0xC46144;
        label_0xC46144:
        ;
        x8 = RuntimeMemory.ReadU64(x0);
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x8UL))));
        x0 = x19;
        x1 = x22;
        x0 = RuntimeCalls.InvokeIndirect(x8, x0, x1, x2, x3);
        x1 = x0;
        RuntimeMemory.WriteU64(x21, x0);
        x0 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x118UL))));
        if ((x21 == 0x0UL))
        {
            goto label_0xC463C8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x18UL))));
        x8 = RuntimeMemory.ReadU64(x19);
        x1 = RuntimeMemory.ReadU64(x23);
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU16(unchecked((ulong)((x8) + (0x12EUL))))))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC461A0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB0UL))));
        x10 = unchecked((ulong)((x10) + (0x8UL)));
        goto label_0xC46188;
        label_0xC46188:
        ;
        x11 = RuntimeMemory.ReadU64(unchecked((ulong)((x10) + (0xFFFFFFFFFFFFFFF8UL))));
        __arm64_flags_left_12870028 = x11;
        __arm64_flags_right_12870028 = x1;
        if ((unchecked((ulong)((__arm64_flags_left_12870028) - (__arm64_flags_right_12870028))) == 0x0UL))
        {
            goto label_0xC461B0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC46194UL);
        }
        __arm64_flags_left_12870036 = x9;
        __arm64_flags_right_12870036 = 0x1UL;
        __arm64_flags_result_12870036 = unchecked((ulong)((__arm64_flags_left_12870036) - (__arm64_flags_right_12870036)));
        x9 = __arm64_flags_result_12870036;
        x10 = unchecked((ulong)((x10) + (0x10UL)));
        RuntimeCalls.Unsupported("b.ne", 0xC4619CUL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC46188;
        }
        else
        {
            goto label_0xC461A0;
        }
        label_0xC461A0:
        ;
        x0 = x19;
        x2 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x0 = RuntimeCalls.InvokeDirect(0xB80110UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC461BC;
        label_0xC461B0:
        ;
        x9 = unchecked((ulong)(unchecked((long)(RuntimeMemory.ReadS32(x10)))));
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)((x9) << (int)(unchecked((int)(0x4UL))))))));
        x0 = unchecked((ulong)((x8) + (0x138UL)));
        goto label_0xC461BC;
        label_0xC461BC:
        ;
        x8 = RuntimeMemory.ReadU64(x0);
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x8UL))));
        x0 = x19;
        x1 = x22;
        x0 = RuntimeCalls.InvokeIndirect(x8, x0, x1, x2, x3);
        x1 = x0;
        RuntimeMemory.WriteU64(x21, x0);
        x0 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x120UL))));
        if ((x21 == 0x0UL))
        {
            goto label_0xC463C8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x18UL))));
        x8 = RuntimeMemory.ReadU64(x19);
        x1 = RuntimeMemory.ReadU64(x23);
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU16(unchecked((ulong)((x8) + (0x12EUL))))))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC46218;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB0UL))));
        x10 = unchecked((ulong)((x10) + (0x8UL)));
        goto label_0xC46200;
        label_0xC46200:
        ;
        x11 = RuntimeMemory.ReadU64(unchecked((ulong)((x10) + (0xFFFFFFFFFFFFFFF8UL))));
        __arm64_flags_left_12870148 = x11;
        __arm64_flags_right_12870148 = x1;
        if ((unchecked((ulong)((__arm64_flags_left_12870148) - (__arm64_flags_right_12870148))) == 0x0UL))
        {
            goto label_0xC46228;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC4620CUL);
        }
        __arm64_flags_left_12870156 = x9;
        __arm64_flags_right_12870156 = 0x1UL;
        __arm64_flags_result_12870156 = unchecked((ulong)((__arm64_flags_left_12870156) - (__arm64_flags_right_12870156)));
        x9 = __arm64_flags_result_12870156;
        x10 = unchecked((ulong)((x10) + (0x10UL)));
        RuntimeCalls.Unsupported("b.ne", 0xC46214UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC46200;
        }
        else
        {
            goto label_0xC46218;
        }
        label_0xC46218:
        ;
        x0 = x19;
        x2 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x0 = RuntimeCalls.InvokeDirect(0xB80110UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC46234;
        label_0xC46228:
        ;
        x9 = unchecked((ulong)(unchecked((long)(RuntimeMemory.ReadS32(x10)))));
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)((x9) << (int)(unchecked((int)(0x4UL))))))));
        x0 = unchecked((ulong)((x8) + (0x138UL)));
        goto label_0xC46234;
        label_0xC46234:
        ;
        x8 = RuntimeMemory.ReadU64(x0);
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x8UL))));
        x0 = x19;
        x1 = x22;
        x0 = RuntimeCalls.InvokeIndirect(x8, x0, x1, x2, x3);
        x1 = x0;
        RuntimeMemory.WriteU64(x21, x0);
        x0 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x128UL))));
        if ((x21 == 0x0UL))
        {
            goto label_0xC463C8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x18UL))));
        x8 = RuntimeMemory.ReadU64(x19);
        x1 = RuntimeMemory.ReadU64(x23);
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU16(unchecked((ulong)((x8) + (0x12EUL))))))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC46290;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB0UL))));
        x10 = unchecked((ulong)((x10) + (0x8UL)));
        goto label_0xC46278;
        label_0xC46278:
        ;
        x11 = RuntimeMemory.ReadU64(unchecked((ulong)((x10) + (0xFFFFFFFFFFFFFFF8UL))));
        __arm64_flags_left_12870268 = x11;
        __arm64_flags_right_12870268 = x1;
        if ((unchecked((ulong)((__arm64_flags_left_12870268) - (__arm64_flags_right_12870268))) == 0x0UL))
        {
            goto label_0xC462A0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC46284UL);
        }
        __arm64_flags_left_12870276 = x9;
        __arm64_flags_right_12870276 = 0x1UL;
        __arm64_flags_result_12870276 = unchecked((ulong)((__arm64_flags_left_12870276) - (__arm64_flags_right_12870276)));
        x9 = __arm64_flags_result_12870276;
        x10 = unchecked((ulong)((x10) + (0x10UL)));
        RuntimeCalls.Unsupported("b.ne", 0xC4628CUL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC46278;
        }
        else
        {
            goto label_0xC46290;
        }
        label_0xC46290:
        ;
        x0 = x19;
        x2 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x0 = RuntimeCalls.InvokeDirect(0xB80110UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC462AC;
        label_0xC462A0:
        ;
        x9 = unchecked((ulong)(unchecked((long)(RuntimeMemory.ReadS32(x10)))));
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)((x9) << (int)(unchecked((int)(0x4UL))))))));
        x0 = unchecked((ulong)((x8) + (0x138UL)));
        goto label_0xC462AC;
        label_0xC462AC:
        ;
        x8 = RuntimeMemory.ReadU64(x0);
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x8UL))));
        x0 = x19;
        x1 = x22;
        x0 = RuntimeCalls.InvokeIndirect(x8, x0, x1, x2, x3);
        x1 = x0;
        RuntimeMemory.WriteU64(x21, x0);
        x0 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x130UL))));
        if ((x21 == 0x0UL))
        {
            goto label_0xC463C8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x18UL))));
        x8 = RuntimeMemory.ReadU64(x19);
        x1 = RuntimeMemory.ReadU64(x23);
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU16(unchecked((ulong)((x8) + (0x12EUL))))))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC46308;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB0UL))));
        x10 = unchecked((ulong)((x10) + (0x8UL)));
        goto label_0xC462F0;
        label_0xC462F0:
        ;
        x11 = RuntimeMemory.ReadU64(unchecked((ulong)((x10) + (0xFFFFFFFFFFFFFFF8UL))));
        __arm64_flags_left_12870388 = x11;
        __arm64_flags_right_12870388 = x1;
        if ((unchecked((ulong)((__arm64_flags_left_12870388) - (__arm64_flags_right_12870388))) == 0x0UL))
        {
            goto label_0xC46318;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC462FCUL);
        }
        __arm64_flags_left_12870396 = x9;
        __arm64_flags_right_12870396 = 0x1UL;
        __arm64_flags_result_12870396 = unchecked((ulong)((__arm64_flags_left_12870396) - (__arm64_flags_right_12870396)));
        x9 = __arm64_flags_result_12870396;
        x10 = unchecked((ulong)((x10) + (0x10UL)));
        RuntimeCalls.Unsupported("b.ne", 0xC46304UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC462F0;
        }
        else
        {
            goto label_0xC46308;
        }
        label_0xC46308:
        ;
        x0 = x19;
        x2 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x0 = RuntimeCalls.InvokeDirect(0xB80110UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC46324;
        label_0xC46318:
        ;
        x9 = unchecked((ulong)(unchecked((long)(RuntimeMemory.ReadS32(x10)))));
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)((x9) << (int)(unchecked((int)(0x4UL))))))));
        x0 = unchecked((ulong)((x8) + (0x138UL)));
        goto label_0xC46324;
        label_0xC46324:
        ;
        x8 = RuntimeMemory.ReadU64(x0);
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x8UL))));
        x0 = x19;
        x1 = x22;
        x0 = RuntimeCalls.InvokeIndirect(x8, x0, x1, x2, x3);
        x1 = x0;
        RuntimeMemory.WriteU64(x21, x0);
        x0 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x138UL))));
        if ((x20 == 0x0UL))
        {
            goto label_0xC463C8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x18UL))));
        x8 = RuntimeMemory.ReadU64(x19);
        x1 = RuntimeMemory.ReadU64(x23);
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU16(unchecked((ulong)((x8) + (0x12EUL))))))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC46380;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB0UL))));
        x10 = unchecked((ulong)((x10) + (0x8UL)));
        goto label_0xC46368;
        label_0xC46368:
        ;
        x11 = RuntimeMemory.ReadU64(unchecked((ulong)((x10) + (0xFFFFFFFFFFFFFFF8UL))));
        __arm64_flags_left_12870508 = x11;
        __arm64_flags_right_12870508 = x1;
        if ((unchecked((ulong)((__arm64_flags_left_12870508) - (__arm64_flags_right_12870508))) == 0x0UL))
        {
            goto label_0xC46390;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC46374UL);
        }
        __arm64_flags_left_12870516 = x9;
        __arm64_flags_right_12870516 = 0x1UL;
        __arm64_flags_result_12870516 = unchecked((ulong)((__arm64_flags_left_12870516) - (__arm64_flags_right_12870516)));
        x9 = __arm64_flags_result_12870516;
        x10 = unchecked((ulong)((x10) + (0x10UL)));
        RuntimeCalls.Unsupported("b.ne", 0xC4637CUL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC46368;
        }
        else
        {
            goto label_0xC46380;
        }
        label_0xC46380:
        ;
        x0 = x19;
        x2 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x0 = RuntimeCalls.InvokeDirect(0xB80110UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC4639C;
        label_0xC46390:
        ;
        x9 = unchecked((ulong)(unchecked((long)(RuntimeMemory.ReadS32(x10)))));
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)((x9) << (int)(unchecked((int)(0x4UL))))))));
        x0 = unchecked((ulong)((x8) + (0x138UL)));
        goto label_0xC4639C;
        label_0xC4639C:
        ;
        x8 = RuntimeMemory.ReadU64(x0);
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x8UL))));
        x0 = x19;
        x1 = x21;
        x0 = RuntimeCalls.InvokeIndirect(x8, x0, x1, x2, x3);
        x1 = x0;
        RuntimeMemory.WriteU64(x20, x0);
        x0 = x20;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeDirect(0xB7D8D0UL);
        label_0xC463C8:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```
