# `SuperTouchZoneSpriteAnimator` — TypeDefIndex 5010

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0xF0` | `SpriteConfig` | `spriteRawPress` |
| `0xF8` | `SpriteConfig` | `spriteNormalPress` |
| `0x100` | `SpriteConfig` | `spriteLongPress` |
| `0x108` | `SpriteConfig` | `spriteTap` |
| `0x110` | `SpriteConfig` | `spriteDoubleTap` |
| `0x118` | `SpriteConfig` | `spriteLongTap` |
| `0x120` | `SpriteConfig` | `spriteNormalScrollU` |
| `0x128` | `SpriteConfig` | `spriteNormalScrollR` |
| `0x130` | `SpriteConfig` | `spriteNormalScrollD` |
| `0x138` | `SpriteConfig` | `spriteNormalScrollL` |
| `0x140` | `SpriteConfig` | `spriteLongScrollU` |
| `0x148` | `SpriteConfig` | `spriteLongScrollR` |
| `0x150` | `SpriteConfig` | `spriteLongScrollD` |
| `0x158` | `SpriteConfig` | `spriteLongScrollL` |

## `SuperTouchZoneSpriteAnimator.ctor` — RVA `0xc439f0`

- Lift status: **exact**; input span: 844 bytes; span to next metadata RVA: 844 bytes.
- Metadata signature: `public void .ctor() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=140 (informational only).

```csharp
public static ulong SuperTouchZoneSpriteAnimator_ctor_RVAc439f0(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_load_address_12860724 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
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
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x22) + (0x214UL))))))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xB50UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x3D0UL))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC43A4C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB58UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB50UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x3D0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x22) + (0x214UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC43A4C;
        label_0xC43A4C:
        ;
        x0 = RuntimeMemory.ReadU64(x21);
        x21 = 0x1A8C000UL;
        x20 = RuntimeMemory.ReadU64(x20);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xB58UL))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC43A68;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC43A64UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC43A68;
        label_0xC43A68:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1556240UL /* metadata target: Type.GetTypeFromHandle */, x0, x1, x2, x3);
        x1 = x0;
        x0 = x19;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC63A74UL /* metadata target: TouchControlSpriteAnimatorBase.ctor */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x21);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x8 = 0x432000UL;
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x3E0UL))))), 0));
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x2 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x3 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC63528UL /* metadata target: SpriteConfig.ctor */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0xF0UL))), x20);
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = RuntimeMemory.ReadU64(x21);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
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
        x2 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x3 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC63528UL /* metadata target: SpriteConfig.ctor */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = unchecked((ulong)((x19) + (0x10UL)));
        x1 = x20;
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x10UL))), x20);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = RuntimeMemory.ReadU64(x21);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x2 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x3 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC63528UL /* metadata target: SpriteConfig.ctor */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = unchecked((ulong)((x19) + (0x18UL)));
        x1 = x20;
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x18UL))), x20);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = RuntimeMemory.ReadU64(x21);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x2 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x3 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC63528UL /* metadata target: SpriteConfig.ctor */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = unchecked((ulong)((x19) + (0x20UL)));
        x1 = x20;
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x20UL))), x20);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = RuntimeMemory.ReadU64(x21);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x2 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x3 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC63528UL /* metadata target: SpriteConfig.ctor */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = unchecked((ulong)((x19) + (0x28UL)));
        x1 = x20;
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x28UL))), x20);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = RuntimeMemory.ReadU64(x21);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x2 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x3 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC63528UL /* metadata target: SpriteConfig.ctor */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = unchecked((ulong)((x19) + (0x30UL)));
        x1 = x20;
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x30UL))), x20);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = RuntimeMemory.ReadU64(x21);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x2 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x3 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC63528UL /* metadata target: SpriteConfig.ctor */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = unchecked((ulong)((x19) + (0x38UL)));
        x1 = x20;
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x38UL))), x20);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = RuntimeMemory.ReadU64(x21);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x2 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x3 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC63528UL /* metadata target: SpriteConfig.ctor */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = unchecked((ulong)((x19) + (0x40UL)));
        x1 = x20;
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x40UL))), x20);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = RuntimeMemory.ReadU64(x21);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x2 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x3 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC63528UL /* metadata target: SpriteConfig.ctor */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = unchecked((ulong)((x19) + (0x48UL)));
        x1 = x20;
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x48UL))), x20);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = RuntimeMemory.ReadU64(x21);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x2 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x3 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC63528UL /* metadata target: SpriteConfig.ctor */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = unchecked((ulong)((x19) + (0x50UL)));
        x1 = x20;
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x50UL))), x20);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = RuntimeMemory.ReadU64(x21);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x2 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x3 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC63528UL /* metadata target: SpriteConfig.ctor */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = unchecked((ulong)((x19) + (0x58UL)));
        x1 = x20;
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x58UL))), x20);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = RuntimeMemory.ReadU64(x21);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x2 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        v0 = v8;
        x3 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC63528UL /* metadata target: SpriteConfig.ctor */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = unchecked((ulong)((x19) + (0x60UL)));
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x60UL))), x20);
        x1 = x20;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        __arm64_load_address_12860724 = sp;
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_load_address_12860724)), 0));
        sp = unchecked((ulong)((__arm64_load_address_12860724) + (0x30UL)));
        return RuntimeCalls.InvokeDirect(0xB7D8D0UL);
        return default(ulong);
    }
```

## `SuperTouchZoneSpriteAnimator.SetSprite` — RVA `0xc43d3c`

- Lift status: **exact**; input span: 76 bytes; span to next metadata RVA: 76 bytes.
- Metadata signature: `public void SetSprite(Sprite sprite) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=9 (informational only).

```csharp
public static ulong SuperTouchZoneSpriteAnimator_SetSprite_RVAc43d3c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12860784 = default(uint);
        uint __arm64_flags_right_12860784 = default(uint);
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x30 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        x19 = x1;
        x20 = x0;
        x21 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xC43D50;
        label_0xC43D50:
        ;
        x0 = x20;
        x1 = unchecked((ulong)(unchecked((uint)(x21))));
        x0 = RuntimeCalls.InvokeDirect(0xC43D88UL /* metadata target: SuperTouchZoneSpriteAnimator.GetStateSpriteConfig */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC43D84;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC43D60UL);
        }
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x18UL))), x19);
        x1 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x21 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x21))) + (unchecked((uint)(0x1UL)))))));
        __arm64_flags_left_12860784 = unchecked((uint)(x21));
        __arm64_flags_right_12860784 = unchecked((uint)0xFUL);
        if ((!((unchecked((uint)((__arm64_flags_left_12860784) - (__arm64_flags_right_12860784))) == unchecked((uint)0x0UL)))))
        {
            goto label_0xC43D50;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return x0;
        label_0xC43D84:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `SuperTouchZoneSpriteAnimator.GetStateSpriteConfig` — RVA `0xc43d88`

- Lift status: **exact**; input span: 168 bytes; span to next metadata RVA: 168 bytes.
- Metadata signature: `public SpriteConfig GetStateSpriteConfig(SuperTouchZoneSpriteAnimator.ControlState state) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=38 (informational only).

```csharp
public static ulong SuperTouchZoneSpriteAnimator_GetStateSpriteConfig_RVAc43d88(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12860808 = default(uint);
        uint __arm64_flags_right_12860808 = default(uint);
        ulong x10 = default(ulong);
        ulong x11 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        __arm64_flags_left_12860808 = unchecked((uint)(x1));
        __arm64_flags_right_12860808 = unchecked((uint)0xEUL);
        if (((__arm64_flags_left_12860808 >= __arm64_flags_right_12860808) && (!((unchecked((uint)((__arm64_flags_left_12860808) - (__arm64_flags_right_12860808))) == unchecked((uint)0x0UL))))))
        {
            goto label_0xC43DB4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = 0x452000UL;
        x8 = unchecked((ulong)(unchecked((uint)(x1))));
        x9 = unchecked((ulong)((x9) + (0xBDUL)));
        x10 = 0xC43DACUL;
        x11 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x9) + (unchecked((ulong)(unchecked((uint)(x8))))))))))));
        x10 = unchecked((ulong)((x10) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x11))) << (int)(unchecked((int)(unchecked((uint)(0x2UL))))))))))));
        return RuntimeCalls.InvokeIndirect(x10);
        label_0xC43DB4:
        ;
        x0 = 0x0UL;
        return x0;
        return default(ulong);
    }
```

## `SuperTouchZoneSpriteAnimator.SetColor` — RVA `0xc43e30`

- Lift status: **exact**; input span: 100 bytes; span to next metadata RVA: 100 bytes.
- Metadata signature: `public void SetColor(Color color) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=11 (informational only).

```csharp
public static ulong SuperTouchZoneSpriteAnimator_SetColor_RVAc43e30(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12861036 = default(uint);
        uint __arm64_flags_right_12861036 = default(uint);
        ulong __arm64_pair_address_12860976 = default(ulong);
        ulong __arm64_pair_address_12860980 = default(ulong);
        ulong __arm64_pair_address_12861040 = default(ulong);
        ulong __arm64_pair_address_12861044 = default(ulong);
        ulong __arm64_pair_address_12861060 = default(ulong);
        ulong __arm64_pair_address_12861064 = default(ulong);
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
        ulong x20 = default(ulong);
        ulong x30 = default(ulong);
        __arm64_pair_address_12860976 = unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFC0UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12860976, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v11.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12860976) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v10.GetUInt64(0)))));
        sp = __arm64_pair_address_12860976;
        __arm64_pair_address_12860980 = unchecked((ulong)((sp) + (0x10UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12860980, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12860980) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x20UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))), x19);
        v8 = v3;
        v9 = v2;
        v10 = v1;
        v11 = v0;
        x19 = x0;
        x20 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xC43E58;
        label_0xC43E58:
        ;
        x0 = x19;
        x1 = unchecked((ulong)(unchecked((uint)(x20))));
        x0 = RuntimeCalls.InvokeDirect(0xC43D88UL /* metadata target: SuperTouchZoneSpriteAnimator.GetStateSpriteConfig */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC43E90;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x20))) + (unchecked((uint)(0x1UL)))))));
        __arm64_flags_left_12861036 = unchecked((uint)(x20));
        __arm64_flags_right_12861036 = unchecked((uint)0xFUL);
        __arm64_pair_address_12861040 = unchecked((ulong)((x0) + (0x20UL)));
        RuntimeMemory.WriteF32(__arm64_pair_address_12861040, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_12861040) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0));
        __arm64_pair_address_12861044 = unchecked((ulong)((x0) + (0x28UL)));
        RuntimeMemory.WriteF32(__arm64_pair_address_12861044, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_12861044) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0));
        if ((!((unchecked((uint)((__arm64_flags_left_12861036) - (__arm64_flags_right_12861036))) == unchecked((uint)0x0UL)))))
        {
            goto label_0xC43E58;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        __arm64_pair_address_12861060 = unchecked((ulong)((sp) + (0x10UL)));
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12861060)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12861060) + (0x8UL))))), 0));
        __arm64_pair_address_12861064 = sp;
        v11 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12861064)), 0));
        v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12861064) + (0x8UL))))), 0));
        return x0;
        label_0xC43E90:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        return default(ulong);
    }
```

## `SuperTouchZoneSpriteAnimator.SetStateSprite` — RVA `0xc43e94`

- Lift status: **exact**; input span: 64 bytes; span to next metadata RVA: 64 bytes.
- Metadata signature: `public void SetStateSprite(SuperTouchZoneSpriteAnimator.ControlState state, Sprite sprite) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=9 (informational only).

```csharp
public static ulong SuperTouchZoneSpriteAnimator_SetStateSprite_RVAc43e94(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
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
        x0 = RuntimeCalls.InvokeDirect(0xC43D88UL /* metadata target: SuperTouchZoneSpriteAnimator.GetStateSpriteConfig */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC43EC0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC43EACUL);
        }
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x18UL))), x19);
        x1 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0xB7D8D0UL);
        label_0xC43EC0:
        ;
        x0 = x20;
        x1 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0xC43D3CUL /* metadata target: SuperTouchZoneSpriteAnimator.SetSprite */);
        return default(ulong);
    }
```

## `SuperTouchZoneSpriteAnimator.SetStateColor` — RVA `0xc43ed4`

- Lift status: **exact**; input span: 100 bytes; span to next metadata RVA: 100 bytes.
- Metadata signature: `public void SetStateColor(SuperTouchZoneSpriteAnimator.ControlState state, Color color) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=12 (informational only).

```csharp
public static ulong SuperTouchZoneSpriteAnimator_SetStateColor_RVAc43ed4(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_pair_address_12861140 = default(ulong);
        ulong __arm64_pair_address_12861144 = default(ulong);
        ulong __arm64_pair_address_12861180 = default(ulong);
        ulong __arm64_pair_address_12861188 = default(ulong);
        ulong __arm64_pair_address_12861192 = default(ulong);
        ulong __arm64_pair_address_12861196 = default(ulong);
        ulong __arm64_pair_address_12861220 = default(ulong);
        ulong __arm64_pair_address_12861232 = default(ulong);
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
        __arm64_pair_address_12861140 = unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFD0UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12861140, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v11.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12861140) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v10.GetUInt64(0)))));
        sp = __arm64_pair_address_12861140;
        __arm64_pair_address_12861144 = unchecked((ulong)((sp) + (0x10UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12861144, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12861144) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x19);
        v8 = v3;
        v9 = v2;
        v10 = v1;
        v11 = v0;
        x19 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC43D88UL /* metadata target: SuperTouchZoneSpriteAnimator.GetStateSpriteConfig */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC43F14;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC43EFCUL);
        }
        __arm64_pair_address_12861180 = unchecked((ulong)((x0) + (0x28UL)));
        RuntimeMemory.WriteF32(__arm64_pair_address_12861180, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_12861180) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        __arm64_pair_address_12861188 = unchecked((ulong)((sp) + (0x10UL)));
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12861188)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12861188) + (0x8UL))))), 0));
        __arm64_pair_address_12861192 = unchecked((ulong)((x0) + (0x20UL)));
        RuntimeMemory.WriteF32(__arm64_pair_address_12861192, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_12861192) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0));
        __arm64_pair_address_12861196 = sp;
        v11 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12861196)), 0));
        v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12861196) + (0x8UL))))), 0));
        return x0;
        label_0xC43F14:
        ;
        x0 = x19;
        v2 = v9;
        v3 = v8;
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        __arm64_pair_address_12861220 = unchecked((ulong)((sp) + (0x10UL)));
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12861220)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12861220) + (0x8UL))))), 0));
        v0 = v11;
        v1 = v10;
        __arm64_pair_address_12861232 = sp;
        v11 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12861232)), 0));
        v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12861232) + (0x8UL))))), 0));
        sp = unchecked((ulong)((__arm64_pair_address_12861232) + (0x30UL)));
        return RuntimeCalls.InvokeDirect(0xC43E30UL /* metadata target: SuperTouchZoneSpriteAnimator.SetColor */);
        return default(ulong);
    }
```

## `SuperTouchZoneSpriteAnimator.OnInitComponent` — RVA `0xc43f38`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `protected override void OnInitComponent() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static ulong SuperTouchZoneSpriteAnimator_OnInitComponent_RVAc43f38(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x1 = 0x0UL;
        return RuntimeCalls.InvokeDirect(0xC63B4CUL /* metadata target: TouchControlSpriteAnimatorBase.OnInitComponent */);
        return default(ulong);
    }
```

## `SuperTouchZoneSpriteAnimator.OnUpdateAnimator` — RVA `0xc43f40`

- Lift status: **partial**; input span: 1012 bytes; span to next metadata RVA: 1012 bytes.
- Metadata signature: `protected override void OnUpdateAnimator(bool skipAnim) { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=124 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'b.mi' at 0xc44198; reason: Unknown IR expression at 0xc44198; reason: Unsupported instruction 'b.mi' at 0xc441a4; reason: Unknown IR expression at 0xc441a4; reason: Unsupported instruction 'b.pl' at 0xc44240; reason: Unknown IR expression at 0xc44240; reason: Unsupported instruction 'b.pl' at 0xc44284; reason: Unknown IR expression at 0xc44284

```csharp
public static ulong SuperTouchZoneSpriteAnimator_OnUpdateAnimator_RVAc43f40(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12861348 = default(uint);
        ulong __arm64_flags_left_12861368 = default(ulong);
        uint __arm64_flags_right_12861348 = default(uint);
        ulong __arm64_flags_right_12861368 = default(ulong);
        float __arm64_float_flags_left_12861828 = default(float);
        float __arm64_float_flags_left_12861840 = default(float);
        float __arm64_float_flags_left_12861852 = default(float);
        float __arm64_float_flags_left_12861868 = default(float);
        float __arm64_float_flags_left_12861880 = default(float);
        float __arm64_float_flags_left_12861904 = default(float);
        float __arm64_float_flags_left_12861928 = default(float);
        float __arm64_float_flags_left_12861972 = default(float);
        float __arm64_float_flags_left_12861984 = default(float);
        float __arm64_float_flags_left_12862024 = default(float);
        float __arm64_float_flags_left_12862048 = default(float);
        float __arm64_float_flags_left_12862060 = default(float);
        float __arm64_float_flags_right_12861828 = default(float);
        float __arm64_float_flags_right_12861840 = default(float);
        float __arm64_float_flags_right_12861852 = default(float);
        float __arm64_float_flags_right_12861868 = default(float);
        float __arm64_float_flags_right_12861880 = default(float);
        float __arm64_float_flags_right_12861904 = default(float);
        float __arm64_float_flags_right_12861928 = default(float);
        float __arm64_float_flags_right_12861972 = default(float);
        float __arm64_float_flags_right_12861984 = default(float);
        float __arm64_float_flags_right_12862024 = default(float);
        float __arm64_float_flags_right_12862048 = default(float);
        float __arm64_float_flags_right_12862060 = default(float);
        ulong __arm64_pair_address_12861248 = default(ulong);
        ulong __arm64_pair_address_12861472 = default(ulong);
        ulong __arm64_pair_address_12862240 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        RuntimeVector128 v9 = default(RuntimeVector128);
        ulong x10 = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x22 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        __arm64_pair_address_12861248 = unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFC0UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12861248, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12861248) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        sp = __arm64_pair_address_12861248;
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x10UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))), x19);
        x21 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x215UL))))))));
        x20 = unchecked((ulong)(unchecked((uint)(x1))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC43F84;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB60UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x215UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC43F84;
        label_0xC43F84:
        ;
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x28UL))));
        if ((x21 == 0x0UL))
        {
            goto label_0xC43FC0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = 0x1A8C000UL;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0xB60UL))));
        x8 = RuntimeMemory.ReadU64(x21);
        x1 = RuntimeMemory.ReadU64(x9);
        x10 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x130UL))))))));
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x1) + (0x130UL))))))));
        __arm64_flags_left_12861348 = unchecked((uint)(x10));
        __arm64_flags_right_12861348 = unchecked((uint)(x9));
        if ((!((__arm64_flags_left_12861348 >= __arm64_flags_right_12861348))))
        {
            goto label_0xC44328;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xC8UL))));
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) << (int)(unchecked((int)(unchecked((uint)(0x3UL))))))))))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xFFFFFFFFFFFFFFF8UL))));
        __arm64_flags_left_12861368 = x8;
        __arm64_flags_right_12861368 = x1;
        if ((!((unchecked((ulong)((__arm64_flags_left_12861368) - (__arm64_flags_right_12861368))) == 0x0UL))))
        {
            goto label_0xC44328;
        }
        else
        {
            goto label_0xC43FC0;
        }
        label_0xC43FC0:
        ;
        x22 = 0x1A8C000UL;
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0xD8UL))));
        x0 = RuntimeMemory.ReadU64(x22);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC43FD8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC43FD4UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC43FD8;
        label_0xC43FD8:
        ;
        x0 = x21;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179568CUL /* metadata target: Object.op_Equality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC44014;
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
            goto label_0xC44000;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC43FFCUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC44000;
        label_0xC44000:
        ;
        x0 = x22;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179568CUL /* metadata target: Object.op_Equality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC44028;
        }
        else
        {
            goto label_0xC44014;
        }
        label_0xC44014:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        __arm64_pair_address_12861472 = sp;
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12861472)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12861472) + (0x8UL))))), 0));
        sp = unchecked((ulong)((__arm64_pair_address_12861472) + (0x40UL)));
        return x0;
        label_0xC44028:
        ;
        if ((x21 == 0x0UL))
        {
            goto label_0xC44330;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xC44334UL /* metadata target: SuperTouchZone.GetScrollDelta */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x2 = unchecked((ulong)(unchecked((uint)(0x2UL))));
        x0 = x21;
        v9 = v0;
        v8 = v1;
        x0 = RuntimeCalls.InvokeDirect(0xC44394UL /* metadata target: SuperTouchZone.JustTapped */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC4407C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)(0x2UL))));
        x2 = unchecked((ulong)(unchecked((uint)(0x2UL))));
        x0 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xC44394UL /* metadata target: SuperTouchZone.JustTapped */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC4407C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)(0x3UL))));
        x2 = unchecked((ulong)(unchecked((uint)(0x2UL))));
        x0 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xC44394UL /* metadata target: SuperTouchZone.JustTapped */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC44238;
        }
        else
        {
            goto label_0xC4407C;
        }
        label_0xC4407C:
        ;
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x110UL))));
        goto label_0xC44080;
        label_0xC44080:
        ;
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x2 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xC44394UL /* metadata target: SuperTouchZone.JustTapped */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC440BC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)(0x2UL))));
        x2 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xC44394UL /* metadata target: SuperTouchZone.JustTapped */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC440BC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)(0x3UL))));
        x2 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xC44394UL /* metadata target: SuperTouchZone.JustTapped */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC440CC;
        }
        else
        {
            goto label_0xC440BC;
        }
        label_0xC440BC:
        ;
        if ((x22 == 0x0UL))
        {
            goto label_0xC440C8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x22) + (0x10UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC440CC;
        }
        else
        {
            goto label_0xC440C8;
        }
        label_0xC440C8:
        ;
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x108UL))));
        goto label_0xC440CC;
        label_0xC440CC:
        ;
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xC443C8UL /* metadata target: SuperTouchZone.JustLongTapped */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC440FC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)(0x2UL))));
        x0 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xC443C8UL /* metadata target: SuperTouchZone.JustLongTapped */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC440FC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)(0x3UL))));
        x0 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xC443C8UL /* metadata target: SuperTouchZone.JustLongTapped */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC4410C;
        }
        else
        {
            goto label_0xC440FC;
        }
        label_0xC440FC:
        ;
        if ((x22 == 0x0UL))
        {
            goto label_0xC44108;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x22) + (0x10UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC4410C;
        }
        else
        {
            goto label_0xC44108;
        }
        label_0xC44108:
        ;
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x118UL))));
        goto label_0xC4410C;
        label_0xC4410C:
        ;
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xC443F4UL /* metadata target: SuperTouchZone.PressedLong */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC4413C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)(0x2UL))));
        x0 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xC443F4UL /* metadata target: SuperTouchZone.PressedLong */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC4413C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)(0x3UL))));
        x0 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xC443F4UL /* metadata target: SuperTouchZone.PressedLong */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC44148;
        }
        else
        {
            goto label_0xC4413C;
        }
        label_0xC4413C:
        ;
        if ((x22 == 0x0UL))
        {
            goto label_0xC44190;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x22) + (0x10UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC441AC;
        }
        else
        {
            goto label_0xC44148;
        }
        label_0xC44148:
        ;
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xC44420UL /* metadata target: SuperTouchZone.PressedNormal */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC44178;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)(0x2UL))));
        x0 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xC44420UL /* metadata target: SuperTouchZone.PressedNormal */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC44178;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)(0x3UL))));
        x0 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xC44420UL /* metadata target: SuperTouchZone.PressedNormal */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC4429C;
        }
        else
        {
            goto label_0xC44178;
        }
        label_0xC44178:
        ;
        if ((x22 == 0x0UL))
        {
            goto label_0xC44214;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x22) + (0x10UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC4429C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC44184UL);
        }
        __arm64_float_flags_left_12861828 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12861828 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        if ((__arm64_float_flags_left_12861828 > __arm64_float_flags_right_12861828))
        {
            goto label_0xC4421C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC4418CUL);
        }
        goto label_0xC44220;
        label_0xC44190:
        ;
        __arm64_float_flags_left_12861840 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12861840 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        if ((__arm64_float_flags_left_12861840 > __arm64_float_flags_right_12861840))
        {
            goto label_0xC441B4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC44198UL);
        }
        RuntimeCalls.Unsupported("b.mi", 0xC44198UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC441CC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC4419CUL);
        }
        __arm64_float_flags_left_12861852 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12861852 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        if ((__arm64_float_flags_left_12861852 > __arm64_float_flags_right_12861852))
        {
            goto label_0xC441E4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC441A4UL);
        }
        RuntimeCalls.Unsupported("b.mi", 0xC441A4UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC441FC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC441A8UL);
        }
        goto label_0xC4420C;
        label_0xC441AC:
        ;
        __arm64_float_flags_left_12861868 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12861868 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        if (((__arm64_float_flags_left_12861868 <= __arm64_float_flags_right_12861868) || ((__arm64_float_flags_left_12861868 != __arm64_float_flags_left_12861868) || (__arm64_float_flags_right_12861868 != __arm64_float_flags_right_12861868))))
        {
            goto label_0xC441B8;
        }
        else
        {
            goto label_0xC441B4;
        }
        label_0xC441B4:
        ;
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x148UL))));
        goto label_0xC441B8;
        label_0xC441B8:
        ;
        __arm64_float_flags_left_12861880 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12861880 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        if (((__arm64_float_flags_left_12861880 >= __arm64_float_flags_right_12861880) || ((__arm64_float_flags_left_12861880 != __arm64_float_flags_left_12861880) || (__arm64_float_flags_right_12861880 != __arm64_float_flags_right_12861880))))
        {
            goto label_0xC441D0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC441C0UL);
        }
        if ((x22 == 0x0UL))
        {
            goto label_0xC441CC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x22) + (0x10UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC441D0;
        }
        else
        {
            goto label_0xC441CC;
        }
        label_0xC441CC:
        ;
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x158UL))));
        goto label_0xC441D0;
        label_0xC441D0:
        ;
        __arm64_float_flags_left_12861904 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12861904 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        if (((__arm64_float_flags_left_12861904 <= __arm64_float_flags_right_12861904) || ((__arm64_float_flags_left_12861904 != __arm64_float_flags_left_12861904) || (__arm64_float_flags_right_12861904 != __arm64_float_flags_right_12861904))))
        {
            goto label_0xC441E8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC441D8UL);
        }
        if ((x22 == 0x0UL))
        {
            goto label_0xC441E4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x22) + (0x10UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC441E8;
        }
        else
        {
            goto label_0xC441E4;
        }
        label_0xC441E4:
        ;
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x140UL))));
        goto label_0xC441E8;
        label_0xC441E8:
        ;
        __arm64_float_flags_left_12861928 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12861928 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        if (((__arm64_float_flags_left_12861928 >= __arm64_float_flags_right_12861928) || ((__arm64_float_flags_left_12861928 != __arm64_float_flags_left_12861928) || (__arm64_float_flags_right_12861928 != __arm64_float_flags_right_12861928))))
        {
            goto label_0xC44200;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC441F0UL);
        }
        if ((x22 == 0x0UL))
        {
            goto label_0xC441FC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x22) + (0x10UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC4429C;
        }
        else
        {
            goto label_0xC441FC;
        }
        label_0xC441FC:
        ;
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x150UL))));
        goto label_0xC44200;
        label_0xC44200:
        ;
        if ((x22 == 0x0UL))
        {
            goto label_0xC4420C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x22) + (0x10UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC4429C;
        }
        else
        {
            goto label_0xC4420C;
        }
        label_0xC4420C:
        ;
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x100UL))));
        goto label_0xC4429C;
        label_0xC44214:
        ;
        __arm64_float_flags_left_12861972 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12861972 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        if (((__arm64_float_flags_left_12861972 <= __arm64_float_flags_right_12861972) || ((__arm64_float_flags_left_12861972 != __arm64_float_flags_left_12861972) || (__arm64_float_flags_right_12861972 != __arm64_float_flags_right_12861972))))
        {
            goto label_0xC44240;
        }
        else
        {
            goto label_0xC4421C;
        }
        label_0xC4421C:
        ;
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x128UL))));
        goto label_0xC44220;
        label_0xC44220:
        ;
        __arm64_float_flags_left_12861984 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12861984 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        if (((__arm64_float_flags_left_12861984 >= __arm64_float_flags_right_12861984) || ((__arm64_float_flags_left_12861984 != __arm64_float_flags_left_12861984) || (__arm64_float_flags_right_12861984 != __arm64_float_flags_right_12861984))))
        {
            goto label_0xC44248;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC44228UL);
        }
        if ((x22 == 0x0UL))
        {
            goto label_0xC44244;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x22) + (0x10UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC44248;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC44234UL);
        }
        goto label_0xC44244;
        label_0xC44238:
        ;
        x22 = 0x0UL;
        goto label_0xC44080;
        label_0xC44240:
        ;
        RuntimeCalls.Unsupported("b.pl", 0xC44240UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC44260;
        }
        else
        {
            goto label_0xC44244;
        }
        label_0xC44244:
        ;
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x138UL))));
        goto label_0xC44248;
        label_0xC44248:
        ;
        __arm64_float_flags_left_12862024 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12862024 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        if (((__arm64_float_flags_left_12862024 <= __arm64_float_flags_right_12862024) || ((__arm64_float_flags_left_12862024 != __arm64_float_flags_left_12862024) || (__arm64_float_flags_right_12862024 != __arm64_float_flags_right_12862024))))
        {
            goto label_0xC4426C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC44250UL);
        }
        if ((x22 == 0x0UL))
        {
            goto label_0xC44268;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x22) + (0x10UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC4426C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC4425CUL);
        }
        goto label_0xC44268;
        label_0xC44260:
        ;
        __arm64_float_flags_left_12862048 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12862048 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        if (((__arm64_float_flags_left_12862048 <= __arm64_float_flags_right_12862048) || ((__arm64_float_flags_left_12862048 != __arm64_float_flags_left_12862048) || (__arm64_float_flags_right_12862048 != __arm64_float_flags_right_12862048))))
        {
            goto label_0xC44284;
        }
        else
        {
            goto label_0xC44268;
        }
        label_0xC44268:
        ;
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x120UL))));
        goto label_0xC4426C;
        label_0xC4426C:
        ;
        __arm64_float_flags_left_12862060 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12862060 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        if (((__arm64_float_flags_left_12862060 >= __arm64_float_flags_right_12862060) || ((__arm64_float_flags_left_12862060 != __arm64_float_flags_left_12862060) || (__arm64_float_flags_right_12862060 != __arm64_float_flags_right_12862060))))
        {
            goto label_0xC4428C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC44274UL);
        }
        if ((x22 == 0x0UL))
        {
            goto label_0xC44288;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x22) + (0x10UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC4429C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC44280UL);
        }
        goto label_0xC44288;
        label_0xC44284:
        ;
        RuntimeCalls.Unsupported("b.pl", 0xC44284UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC44298;
        }
        else
        {
            goto label_0xC44288;
        }
        label_0xC44288:
        ;
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x130UL))));
        goto label_0xC4428C;
        label_0xC4428C:
        ;
        if ((x22 == 0x0UL))
        {
            goto label_0xC44298;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x22) + (0x10UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC4429C;
        }
        else
        {
            goto label_0xC44298;
        }
        label_0xC44298:
        ;
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xF8UL))));
        goto label_0xC4429C;
        label_0xC4429C:
        ;
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xC4444CUL /* metadata target: SuperTouchZone.PressedRaw */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC442CC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)(0x2UL))));
        x0 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xC4444CUL /* metadata target: SuperTouchZone.PressedRaw */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC442CC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)(0x3UL))));
        x0 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xC4444CUL /* metadata target: SuperTouchZone.PressedRaw */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC442DC;
        }
        else
        {
            goto label_0xC442CC;
        }
        label_0xC442CC:
        ;
        if ((x22 == 0x0UL))
        {
            goto label_0xC442D8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x22) + (0x10UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC442EC;
        }
        else
        {
            goto label_0xC442D8;
        }
        label_0xC442D8:
        ;
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xF0UL))));
        goto label_0xC442DC;
        label_0xC442DC:
        ;
        if ((x22 == 0x0UL))
        {
            goto label_0xC442E8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x22) + (0x10UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC442EC;
        }
        else
        {
            goto label_0xC442E8;
        }
        label_0xC442E8:
        ;
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x78UL))));
        goto label_0xC442EC;
        label_0xC442EC:
        ;
        x20 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x20))) & (unchecked((uint)(0x1UL)))))));
        x0 = x19;
        x1 = x22;
        x2 = unchecked((ulong)(unchecked((uint)(x20))));
        x3 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x4 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC63E00UL /* metadata target: TouchControlSpriteAnimatorBase.BeginSpriteAnim */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x0 = x19;
        x1 = unchecked((ulong)(unchecked((uint)(x20))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x2 = 0x0UL;
        __arm64_pair_address_12862240 = sp;
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12862240)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12862240) + (0x8UL))))), 0));
        sp = unchecked((ulong)((__arm64_pair_address_12862240) + (0x40UL)));
        return RuntimeCalls.InvokeDirect(0xC64384UL /* metadata target: TouchControlSpriteAnimatorBase.UpdateSpriteAnimation */);
        label_0xC44328:
        ;
        x0 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xB7DF10UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, unchecked((ulong)(unchecked((uint)(x3)))));
        goto label_0xC44330;
        label_0xC44330:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, unchecked((ulong)(unchecked((uint)(x3)))));
        return default(ulong);
    }
```

## `SuperTouchZoneSpriteAnimator.GetComponent` — RVA `0xc44478`

- Lift status: **exact**; input span: 4 bytes; span to next metadata RVA: 4 bytes.
- Metadata signature: `private MonoBehaviour ControlFreak2.Internal.ISpriteAnimator.GetComponent() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=0 (informational only).

```csharp
public static ulong SuperTouchZoneSpriteAnimator_GetComponent_RVAc44478(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        return x0;
        return default(ulong);
    }
```

## `SuperTouchZoneSpriteAnimator.AddUsedSprites` — RVA `0xc4447c`

- Lift status: **partial**; input span: 216 bytes; span to next metadata RVA: 216 bytes.
- Metadata signature: `private void ControlFreak2.Internal.ISpriteAnimator.AddUsedSprites(ISpriteOptimizer optimizer) { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=33 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'b.ne' at 0xc44500; reason: Unknown IR expression at 0xc44500

```csharp
public static ulong SuperTouchZoneSpriteAnimator_AddUsedSprites_RVAc4447c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_flags_left_12862704 = default(ulong);
        ulong __arm64_flags_left_12862712 = default(ulong);
        uint __arm64_flags_left_12862776 = default(uint);
        ulong __arm64_flags_result_12862712 = default(ulong);
        ulong __arm64_flags_right_12862704 = default(ulong);
        ulong __arm64_flags_right_12862712 = default(ulong);
        uint __arm64_flags_right_12862776 = default(uint);
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
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x216UL))))))));
        x19 = x1;
        x20 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC444B0;
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
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x216UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC444B0;
        label_0xC444B0:
        ;
        x23 = 0x1A8C000UL;
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0xB68UL))));
        x21 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xC444BC;
        label_0xC444BC:
        ;
        x0 = x20;
        x1 = unchecked((ulong)(unchecked((uint)(x21))));
        x0 = RuntimeCalls.InvokeDirect(0xC43D88UL /* metadata target: SuperTouchZoneSpriteAnimator.GetStateSpriteConfig */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC44550;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC444CCUL);
        }
        if ((x19 == 0x0UL))
        {
            goto label_0xC44550;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x19);
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x18UL))));
        x1 = RuntimeMemory.ReadU64(x23);
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU16(unchecked((ulong)((x8) + (0x12EUL))))))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC44504;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB0UL))));
        x10 = unchecked((ulong)((x10) + (0x8UL)));
        goto label_0xC444EC;
        label_0xC444EC:
        ;
        x11 = RuntimeMemory.ReadU64(unchecked((ulong)((x10) + (0xFFFFFFFFFFFFFFF8UL))));
        __arm64_flags_left_12862704 = x11;
        __arm64_flags_right_12862704 = x1;
        if ((unchecked((ulong)((__arm64_flags_left_12862704) - (__arm64_flags_right_12862704))) == 0x0UL))
        {
            goto label_0xC44514;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC444F8UL);
        }
        __arm64_flags_left_12862712 = x9;
        __arm64_flags_right_12862712 = 0x1UL;
        __arm64_flags_result_12862712 = unchecked((ulong)((__arm64_flags_left_12862712) - (__arm64_flags_right_12862712)));
        x9 = __arm64_flags_result_12862712;
        x10 = unchecked((ulong)((x10) + (0x10UL)));
        RuntimeCalls.Unsupported("b.ne", 0xC44500UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC444EC;
        }
        else
        {
            goto label_0xC44504;
        }
        label_0xC44504:
        ;
        x2 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xB80110UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC44524;
        label_0xC44514:
        ;
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(x10)));
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) + (unchecked((uint)(0x1UL)))))));
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) << (int)(unchecked((int)(unchecked((uint)(0x4UL))))))))))));
        x0 = unchecked((ulong)((x8) + (0x138UL)));
        goto label_0xC44524;
        label_0xC44524:
        ;
        x8 = RuntimeMemory.ReadU64(x0);
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x8UL))));
        x0 = x19;
        x1 = x22;
        x0 = RuntimeCalls.InvokeIndirect(x8, x0, x1, x2, x3);
        x21 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x21))) + (unchecked((uint)(0x1UL)))))));
        __arm64_flags_left_12862776 = unchecked((uint)(x21));
        __arm64_flags_right_12862776 = unchecked((uint)0xFUL);
        if ((!((unchecked((uint)((__arm64_flags_left_12862776) - (__arm64_flags_right_12862776))) == unchecked((uint)0x0UL)))))
        {
            goto label_0xC444BC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return x0;
        label_0xC44550:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `SuperTouchZoneSpriteAnimator.OnSpriteOptimization` — RVA `0xc44554`

- Lift status: **partial**; input span: 240 bytes; span to next metadata RVA: 240 bytes.
- Metadata signature: `private void ControlFreak2.Internal.ISpriteAnimator.OnSpriteOptimization(ISpriteOptimizer optimizer) { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=36 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'b.ne' at 0xc445e0; reason: Unknown IR expression at 0xc445e0

```csharp
public static ulong SuperTouchZoneSpriteAnimator_OnSpriteOptimization_RVAc44554(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_flags_left_12862928 = default(ulong);
        ulong __arm64_flags_left_12862936 = default(ulong);
        uint __arm64_flags_left_12863012 = default(uint);
        ulong __arm64_flags_result_12862936 = default(ulong);
        ulong __arm64_flags_right_12862928 = default(ulong);
        ulong __arm64_flags_right_12862936 = default(ulong);
        uint __arm64_flags_right_12863012 = default(uint);
        ulong sp = default(ulong);
        ulong x10 = default(ulong);
        ulong x11 = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x22 = default(ulong);
        ulong x23 = default(ulong);
        ulong x24 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFC0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x24);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))), x19);
        x21 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x217UL))))))));
        x19 = x1;
        x20 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC4458C;
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
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x217UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC4458C;
        label_0xC4458C:
        ;
        x24 = 0x1A8C000UL;
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((x24) + (0xB68UL))));
        x21 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xC44598;
        label_0xC44598:
        ;
        x0 = x20;
        x1 = unchecked((ulong)(unchecked((uint)(x21))));
        x0 = RuntimeCalls.InvokeDirect(0xC43D88UL /* metadata target: SuperTouchZoneSpriteAnimator.GetStateSpriteConfig */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC44640;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x22 = x0;
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x18UL))));
        if ((x19 == 0x0UL))
        {
            goto label_0xC44640;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x19);
        x1 = RuntimeMemory.ReadU64(x24);
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU16(unchecked((ulong)((x8) + (0x12EUL))))))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC445E4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB0UL))));
        x10 = unchecked((ulong)((x10) + (0x8UL)));
        goto label_0xC445CC;
        label_0xC445CC:
        ;
        x11 = RuntimeMemory.ReadU64(unchecked((ulong)((x10) + (0xFFFFFFFFFFFFFFF8UL))));
        __arm64_flags_left_12862928 = x11;
        __arm64_flags_right_12862928 = x1;
        if ((unchecked((ulong)((__arm64_flags_left_12862928) - (__arm64_flags_right_12862928))) == 0x0UL))
        {
            goto label_0xC445F4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC445D8UL);
        }
        __arm64_flags_left_12862936 = x9;
        __arm64_flags_right_12862936 = 0x1UL;
        __arm64_flags_result_12862936 = unchecked((ulong)((__arm64_flags_left_12862936) - (__arm64_flags_right_12862936)));
        x9 = __arm64_flags_result_12862936;
        x10 = unchecked((ulong)((x10) + (0x10UL)));
        RuntimeCalls.Unsupported("b.ne", 0xC445E0UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC445CC;
        }
        else
        {
            goto label_0xC445E4;
        }
        label_0xC445E4:
        ;
        x0 = x19;
        x2 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x0 = RuntimeCalls.InvokeDirect(0xB80110UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC44600;
        label_0xC445F4:
        ;
        x9 = unchecked((ulong)(unchecked((long)(RuntimeMemory.ReadS32(x10)))));
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)((x9) << (int)(unchecked((int)(0x4UL))))))));
        x0 = unchecked((ulong)((x8) + (0x138UL)));
        goto label_0xC44600;
        label_0xC44600:
        ;
        x8 = RuntimeMemory.ReadU64(x0);
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x8UL))));
        x0 = x19;
        x1 = x23;
        x0 = RuntimeCalls.InvokeIndirect(x8, x0, x1, x2, x3);
        x1 = x0;
        RuntimeMemory.WriteU64(x22, x0);
        x0 = x22;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x21 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x21))) + (unchecked((uint)(0x1UL)))))));
        __arm64_flags_left_12863012 = unchecked((uint)(x21));
        __arm64_flags_right_12863012 = unchecked((uint)0xFUL);
        if ((!((unchecked((uint)((__arm64_flags_left_12863012) - (__arm64_flags_right_12863012))) == unchecked((uint)0x0UL)))))
        {
            goto label_0xC44598;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        label_0xC44640:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```
