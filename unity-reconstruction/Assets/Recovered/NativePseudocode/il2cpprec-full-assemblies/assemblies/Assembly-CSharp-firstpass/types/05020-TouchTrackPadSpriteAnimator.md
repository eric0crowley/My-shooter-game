# `TouchTrackPadSpriteAnimator` — TypeDefIndex 5020

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0xF0` | `SpriteConfig` | `spritePressed` |

## `TouchTrackPadSpriteAnimator.ctor` — RVA `0xc46b20`

- Lift status: **exact**; input span: 208 bytes; span to next metadata RVA: 208 bytes.
- Metadata signature: `public void .ctor() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=35 (informational only).

```csharp
public static ulong TouchTrackPadSpriteAnimator_ctor_RVAc46b20(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x22 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFD0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x19);
        x22 = 0x1BAB000UL;
        x20 = 0x1A8C000UL;
        x21 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x22) + (0x226UL))))))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xBA0UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x3D0UL))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC46B78;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB58UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xBA0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x3D0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x22) + (0x226UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC46B78;
        label_0xC46B78:
        ;
        x0 = RuntimeMemory.ReadU64(x21);
        x21 = 0x1A8C000UL;
        x20 = RuntimeMemory.ReadU64(x20);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xB58UL))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC46B94;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC46B90UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC46B94;
        label_0xC46B94:
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
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x3E0UL))))), 0));
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x2 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x3 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC63528UL /* metadata target: SpriteConfig.ctor */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), x3);
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0xF0UL))), x20);
        x0 = x19;
        x1 = x20;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0xB7D8D0UL);
        return default(ulong);
    }
```

## `TouchTrackPadSpriteAnimator.SetSprite` — RVA `0xc46bf0`

- Lift status: **exact**; input span: 64 bytes; span to next metadata RVA: 64 bytes.
- Metadata signature: `public void SetSprite(Sprite sprite) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=7 (informational only).

```csharp
public static ulong TouchTrackPadSpriteAnimator_SetSprite_RVAc46bf0(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
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
            goto label_0xC46C2C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC46C04UL);
        }
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x18UL))), x1);
        x19 = x1;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xF0UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC46C2C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC46C18UL);
        }
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x18UL))), x19);
        x1 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0xB7D8D0UL);
        label_0xC46C2C:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `TouchTrackPadSpriteAnimator.SetColor` — RVA `0xc46c30`

- Lift status: **exact**; input span: 48 bytes; span to next metadata RVA: 48 bytes.
- Metadata signature: `public void SetColor(Color color) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=3 (informational only).

```csharp
public static ulong TouchTrackPadSpriteAnimator_SetColor_RVAc46c30(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_pair_address_12872764 = default(ulong);
        ulong __arm64_pair_address_12872768 = default(ulong);
        ulong __arm64_pair_address_12872780 = default(ulong);
        ulong __arm64_pair_address_12872784 = default(ulong);
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
            __arm64_pair_address_12872764 = unchecked((ulong)((x8) + (0x20UL)));
            RuntimeMemory.WriteF32(__arm64_pair_address_12872764, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
            RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_12872764) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0));
            __arm64_pair_address_12872768 = unchecked((ulong)((x8) + (0x28UL)));
            RuntimeMemory.WriteF32(__arm64_pair_address_12872768, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0));
            RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_12872768) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0));
            x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xF0UL))));
            if ((x8 == 0x0UL))
            {
            }
            else
            {
                __arm64_pair_address_12872780 = unchecked((ulong)((x8) + (0x20UL)));
                RuntimeMemory.WriteF32(__arm64_pair_address_12872780, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
                RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_12872780) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0));
                __arm64_pair_address_12872784 = unchecked((ulong)((x8) + (0x28UL)));
                RuntimeMemory.WriteF32(__arm64_pair_address_12872784, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0));
                RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_12872784) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0));
                x30 = RuntimeMemory.ReadU64(sp);
                return x0;
            }
        }
        label_0xC46C5C:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `TouchTrackPadSpriteAnimator.SetStateSprite` — RVA `0xc46c60`

- Lift status: **exact**; input span: 56 bytes; span to next metadata RVA: 56 bytes.
- Metadata signature: `public void SetStateSprite(TouchTrackPadSpriteAnimator.ControlState state, Sprite sprite) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=6 (informational only).

```csharp
public static ulong TouchTrackPadSpriteAnimator_SetStateSprite_RVAc46c60(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12872800 = default(uint);
        uint __arm64_flags_right_12872800 = default(uint);
        ulong x8 = default(ulong);
        __arm64_flags_left_12872800 = unchecked((uint)(x1));
        __arm64_flags_right_12872800 = unchecked((uint)0x1UL);
        if ((unchecked((uint)((__arm64_flags_left_12872800) - (__arm64_flags_right_12872800))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC46C74;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC46C68UL);
        }
        if ((unchecked((uint)(x1)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC46C90;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)((x0) + (0x78UL)));
        goto label_0xC46C78;
        label_0xC46C74:
        ;
        x8 = unchecked((ulong)((x0) + (0xF0UL)));
        goto label_0xC46C78;
        label_0xC46C78:
        ;
        x8 = RuntimeMemory.ReadU64(x8);
        if ((x8 == 0x0UL))
        {
            goto label_0xC46C90;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC46C80UL);
        }
        RuntimeMemory.WriteU64(unchecked((ulong)((x8) + (0x18UL))), x2);
        x0 = x8;
        x1 = x2;
        return RuntimeCalls.InvokeDirect(0xB7D8D0UL);
        label_0xC46C90:
        ;
        x1 = x2;
        return RuntimeCalls.InvokeDirect(0xC46BF0UL /* metadata target: TouchTrackPadSpriteAnimator.SetSprite */);
        return default(ulong);
    }
```

## `TouchTrackPadSpriteAnimator.GetStateSpriteConfig` — RVA `0xc46c98`

- Lift status: **exact**; input span: 40 bytes; span to next metadata RVA: 40 bytes.
- Metadata signature: `public SpriteConfig GetStateSpriteConfig(TouchTrackPadSpriteAnimator.ControlState state) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=4 (informational only).

```csharp
public static ulong TouchTrackPadSpriteAnimator_GetStateSpriteConfig_RVAc46c98(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12872856 = default(uint);
        uint __arm64_flags_right_12872856 = default(uint);
        ulong x8 = default(ulong);
        __arm64_flags_left_12872856 = unchecked((uint)(x1));
        __arm64_flags_right_12872856 = unchecked((uint)0x1UL);
        if ((unchecked((uint)((__arm64_flags_left_12872856) - (__arm64_flags_right_12872856))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC46CAC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC46CA0UL);
        }
        if ((unchecked((uint)(x1)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC46CB8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)((x0) + (0x78UL)));
        goto label_0xC46CB0;
        label_0xC46CAC:
        ;
        x8 = unchecked((ulong)((x0) + (0xF0UL)));
        goto label_0xC46CB0;
        label_0xC46CB0:
        ;
        x0 = RuntimeMemory.ReadU64(x8);
        return x0;
        label_0xC46CB8:
        ;
        x0 = 0x0UL;
        return x0;
        return default(ulong);
    }
```

## `TouchTrackPadSpriteAnimator.SetStateColor` — RVA `0xc46cc0`

- Lift status: **exact**; input span: 48 bytes; span to next metadata RVA: 48 bytes.
- Metadata signature: `public void SetStateColor(TouchTrackPadSpriteAnimator.ControlState state, Color color) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=3 (informational only).

```csharp
public static ulong TouchTrackPadSpriteAnimator_SetStateColor_RVAc46cc0(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12872896 = default(uint);
        uint __arm64_flags_right_12872896 = default(uint);
        ulong __arm64_pair_address_12872928 = default(ulong);
        ulong __arm64_pair_address_12872932 = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
        ulong x8 = default(ulong);
        __arm64_flags_left_12872896 = unchecked((uint)(x1));
        __arm64_flags_right_12872896 = unchecked((uint)0x1UL);
        if ((unchecked((uint)((__arm64_flags_left_12872896) - (__arm64_flags_right_12872896))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC46CD4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC46CC8UL);
        }
        if ((unchecked((uint)(x1)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC46CEC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)((x0) + (0x78UL)));
        goto label_0xC46CD8;
        label_0xC46CD4:
        ;
        x8 = unchecked((ulong)((x0) + (0xF0UL)));
        goto label_0xC46CD8;
        label_0xC46CD8:
        ;
        x8 = RuntimeMemory.ReadU64(x8);
        if ((x8 == 0x0UL))
        {
            goto label_0xC46CEC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC46CE0UL);
        }
        __arm64_pair_address_12872928 = unchecked((ulong)((x8) + (0x20UL)));
        RuntimeMemory.WriteF32(__arm64_pair_address_12872928, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_12872928) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0));
        __arm64_pair_address_12872932 = unchecked((ulong)((x8) + (0x28UL)));
        RuntimeMemory.WriteF32(__arm64_pair_address_12872932, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_12872932) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0));
        return x0;
        label_0xC46CEC:
        ;
        return RuntimeCalls.InvokeDirect(0xC46C30UL /* metadata target: TouchTrackPadSpriteAnimator.SetColor */);
        return default(ulong);
    }
```

## `TouchTrackPadSpriteAnimator.OnInitComponent` — RVA `0xc46cf0`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `protected override void OnInitComponent() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static ulong TouchTrackPadSpriteAnimator_OnInitComponent_RVAc46cf0(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x1 = 0x0UL;
        return RuntimeCalls.InvokeDirect(0xC63B4CUL /* metadata target: TouchControlSpriteAnimatorBase.OnInitComponent */);
        return default(ulong);
    }
```

## `TouchTrackPadSpriteAnimator.OnUpdateAnimator` — RVA `0xc46cf8`

- Lift status: **exact**; input span: 328 bytes; span to next metadata RVA: 328 bytes.
- Metadata signature: `protected override void OnUpdateAnimator(bool skipAnim) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=52 (informational only).

```csharp
public static ulong TouchTrackPadSpriteAnimator_OnUpdateAnimator_RVAc46cf8(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12873048 = default(uint);
        ulong __arm64_flags_left_12873068 = default(ulong);
        uint __arm64_flags_right_12873048 = default(uint);
        ulong __arm64_flags_right_12873068 = default(ulong);
        ulong sp = default(ulong);
        ulong x10 = default(ulong);
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
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x227UL))))))));
        x20 = unchecked((ulong)(unchecked((uint)(x1))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC46D38;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xBA8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x227UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC46D38;
        label_0xC46D38:
        ;
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x28UL))));
        if ((x21 == 0x0UL))
        {
            goto label_0xC46D74;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = 0x1A8C000UL;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0xBA8UL))));
        x8 = RuntimeMemory.ReadU64(x21);
        x1 = RuntimeMemory.ReadU64(x9);
        x10 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x130UL))))))));
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x1) + (0x130UL))))))));
        __arm64_flags_left_12873048 = unchecked((uint)(x10));
        __arm64_flags_right_12873048 = unchecked((uint)(x9));
        if ((!((__arm64_flags_left_12873048 >= __arm64_flags_right_12873048))))
        {
            goto label_0xC46E34;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xC8UL))));
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) << (int)(unchecked((int)(unchecked((uint)(0x3UL))))))))))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xFFFFFFFFFFFFFFF8UL))));
        __arm64_flags_left_12873068 = x8;
        __arm64_flags_right_12873068 = x1;
        if ((!((unchecked((ulong)((__arm64_flags_left_12873068) - (__arm64_flags_right_12873068))) == 0x0UL))))
        {
            goto label_0xC46E34;
        }
        else
        {
            goto label_0xC46D74;
        }
        label_0xC46D74:
        ;
        x22 = 0x1A8C000UL;
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0xD8UL))));
        x0 = RuntimeMemory.ReadU64(x22);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC46D8C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC46D88UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC46D8C;
        label_0xC46D8C:
        ;
        x0 = x21;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179568CUL /* metadata target: Object.op_Equality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC46DC8;
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
            goto label_0xC46DB4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC46DB0UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC46DB4;
        label_0xC46DB4:
        ;
        x0 = x22;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179568CUL /* metadata target: Object.op_Equality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC46DD8;
        }
        else
        {
            goto label_0xC46DC8;
        }
        label_0xC46DC8:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        label_0xC46DD8:
        ;
        if ((x21 == 0x0UL))
        {
            goto label_0xC46E3C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x21;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC57B08UL /* metadata target: TouchTrackPad.Pressed */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC46DFC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xF0UL))));
        if ((x1 == 0x0UL))
        {
            goto label_0xC46DFC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x1) + (0x10UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC46E00;
        }
        else
        {
            goto label_0xC46DFC;
        }
        label_0xC46DFC:
        ;
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x78UL))));
        goto label_0xC46E00;
        label_0xC46E00:
        ;
        x20 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x20))) & (unchecked((uint)(0x1UL)))))));
        x0 = x19;
        x2 = unchecked((ulong)(unchecked((uint)(x20))));
        x3 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x4 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC63E00UL /* metadata target: TouchControlSpriteAnimatorBase.BeginSpriteAnim */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x0 = x19;
        x1 = unchecked((ulong)(unchecked((uint)(x20))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x2 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0xC64384UL /* metadata target: TouchControlSpriteAnimatorBase.UpdateSpriteAnimation */);
        label_0xC46E34:
        ;
        x0 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xB7DF10UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, unchecked((ulong)(unchecked((uint)(x3)))));
        goto label_0xC46E3C;
        label_0xC46E3C:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, unchecked((ulong)(unchecked((uint)(x3)))));
        return default(ulong);
    }
```

## `TouchTrackPadSpriteAnimator.GetComponent` — RVA `0xc46e40`

- Lift status: **exact**; input span: 4 bytes; span to next metadata RVA: 4 bytes.
- Metadata signature: `private MonoBehaviour ControlFreak2.Internal.ISpriteAnimator.GetComponent() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=0 (informational only).

```csharp
public static ulong TouchTrackPadSpriteAnimator_GetComponent_RVAc46e40(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        return x0;
        return default(ulong);
    }
```

## `TouchTrackPadSpriteAnimator.AddUsedSprites` — RVA `0xc46e44`

- Lift status: **partial**; input span: 296 bytes; span to next metadata RVA: 296 bytes.
- Metadata signature: `private void ControlFreak2.Internal.ISpriteAnimator.AddUsedSprites(ISpriteOptimizer optimizer) { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=48 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'b.ne' at 0xc46ebc; reason: Unknown IR expression at 0xc46ebc; reason: Unsupported instruction 'b.ne' at 0xc46f28; reason: Unknown IR expression at 0xc46f28

```csharp
public static ulong TouchTrackPadSpriteAnimator_AddUsedSprites_RVAc46e44(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_flags_left_12873388 = default(ulong);
        ulong __arm64_flags_left_12873396 = default(ulong);
        ulong __arm64_flags_left_12873496 = default(ulong);
        ulong __arm64_flags_left_12873504 = default(ulong);
        ulong __arm64_flags_result_12873396 = default(ulong);
        ulong __arm64_flags_result_12873504 = default(ulong);
        ulong __arm64_flags_right_12873388 = default(ulong);
        ulong __arm64_flags_right_12873396 = default(ulong);
        ulong __arm64_flags_right_12873496 = default(ulong);
        ulong __arm64_flags_right_12873504 = default(ulong);
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
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x228UL))))))));
        x19 = x1;
        x20 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC46E78;
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
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x228UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC46E78;
        label_0xC46E78:
        ;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x78UL))));
        if ((x9 == 0x0UL))
        {
            goto label_0xC46F68;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC46E80UL);
        }
        if ((x19 == 0x0UL))
        {
            goto label_0xC46F68;
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
            goto label_0xC46EC0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB0UL))));
        x10 = unchecked((ulong)((x10) + (0x8UL)));
        goto label_0xC46EA8;
        label_0xC46EA8:
        ;
        x11 = RuntimeMemory.ReadU64(unchecked((ulong)((x10) + (0xFFFFFFFFFFFFFFF8UL))));
        __arm64_flags_left_12873388 = x11;
        __arm64_flags_right_12873388 = x1;
        if ((unchecked((ulong)((__arm64_flags_left_12873388) - (__arm64_flags_right_12873388))) == 0x0UL))
        {
            goto label_0xC46ED0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC46EB4UL);
        }
        __arm64_flags_left_12873396 = x9;
        __arm64_flags_right_12873396 = 0x1UL;
        __arm64_flags_result_12873396 = unchecked((ulong)((__arm64_flags_left_12873396) - (__arm64_flags_right_12873396)));
        x9 = __arm64_flags_result_12873396;
        x10 = unchecked((ulong)((x10) + (0x10UL)));
        RuntimeCalls.Unsupported("b.ne", 0xC46EBCUL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC46EA8;
        }
        else
        {
            goto label_0xC46EC0;
        }
        label_0xC46EC0:
        ;
        x2 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xB80110UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC46EE0;
        label_0xC46ED0:
        ;
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(x10)));
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) + (unchecked((uint)(0x1UL)))))));
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) << (int)(unchecked((int)(unchecked((uint)(0x4UL))))))))))));
        x0 = unchecked((ulong)((x8) + (0x138UL)));
        goto label_0xC46EE0;
        label_0xC46EE0:
        ;
        x8 = RuntimeMemory.ReadU64(x0);
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x8UL))));
        x0 = x19;
        x1 = x21;
        x0 = RuntimeCalls.InvokeIndirect(x8, x0, x1, x2, x3);
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xF0UL))));
        if ((x9 == 0x0UL))
        {
            goto label_0xC46F68;
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
            goto label_0xC46F2C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB0UL))));
        x10 = unchecked((ulong)((x10) + (0x8UL)));
        goto label_0xC46F14;
        label_0xC46F14:
        ;
        x11 = RuntimeMemory.ReadU64(unchecked((ulong)((x10) + (0xFFFFFFFFFFFFFFF8UL))));
        __arm64_flags_left_12873496 = x11;
        __arm64_flags_right_12873496 = x1;
        if ((unchecked((ulong)((__arm64_flags_left_12873496) - (__arm64_flags_right_12873496))) == 0x0UL))
        {
            goto label_0xC46F3C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC46F20UL);
        }
        __arm64_flags_left_12873504 = x9;
        __arm64_flags_right_12873504 = 0x1UL;
        __arm64_flags_result_12873504 = unchecked((ulong)((__arm64_flags_left_12873504) - (__arm64_flags_right_12873504)));
        x9 = __arm64_flags_result_12873504;
        x10 = unchecked((ulong)((x10) + (0x10UL)));
        RuntimeCalls.Unsupported("b.ne", 0xC46F28UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC46F14;
        }
        else
        {
            goto label_0xC46F2C;
        }
        label_0xC46F2C:
        ;
        x2 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xB80110UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC46F4C;
        label_0xC46F3C:
        ;
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(x10)));
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) + (unchecked((uint)(0x1UL)))))));
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) << (int)(unchecked((int)(unchecked((uint)(0x4UL))))))))))));
        x0 = unchecked((ulong)((x8) + (0x138UL)));
        goto label_0xC46F4C;
        label_0xC46F4C:
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
        label_0xC46F68:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `TouchTrackPadSpriteAnimator.OnSpriteOptimization` — RVA `0xc46f6c`

- Lift status: **partial**; input span: 320 bytes; span to next metadata RVA: 320 bytes.
- Metadata signature: `private void ControlFreak2.Internal.ISpriteAnimator.OnSpriteOptimization(ISpriteOptimizer optimizer) { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=50 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'b.ne' at 0xc46fe4; reason: Unknown IR expression at 0xc46fe4; reason: Unsupported instruction 'b.ne' at 0xc4705c; reason: Unknown IR expression at 0xc4705c

```csharp
public static ulong TouchTrackPadSpriteAnimator_OnSpriteOptimization_RVAc46f6c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_flags_left_12873684 = default(ulong);
        ulong __arm64_flags_left_12873692 = default(ulong);
        ulong __arm64_flags_left_12873804 = default(ulong);
        ulong __arm64_flags_left_12873812 = default(ulong);
        ulong __arm64_flags_result_12873692 = default(ulong);
        ulong __arm64_flags_result_12873812 = default(ulong);
        ulong __arm64_flags_right_12873684 = default(ulong);
        ulong __arm64_flags_right_12873692 = default(ulong);
        ulong __arm64_flags_right_12873804 = default(ulong);
        ulong __arm64_flags_right_12873812 = default(ulong);
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
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x229UL))))))));
        x19 = x1;
        x20 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC46FA0;
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
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x229UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC46FA0;
        label_0xC46FA0:
        ;
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x78UL))));
        if ((x21 == 0x0UL))
        {
            goto label_0xC470A8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x18UL))));
        if ((x19 == 0x0UL))
        {
            goto label_0xC470A8;
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
            goto label_0xC46FE8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB0UL))));
        x10 = unchecked((ulong)((x10) + (0x8UL)));
        goto label_0xC46FD0;
        label_0xC46FD0:
        ;
        x11 = RuntimeMemory.ReadU64(unchecked((ulong)((x10) + (0xFFFFFFFFFFFFFFF8UL))));
        __arm64_flags_left_12873684 = x11;
        __arm64_flags_right_12873684 = x1;
        if ((unchecked((ulong)((__arm64_flags_left_12873684) - (__arm64_flags_right_12873684))) == 0x0UL))
        {
            goto label_0xC46FF8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC46FDCUL);
        }
        __arm64_flags_left_12873692 = x9;
        __arm64_flags_right_12873692 = 0x1UL;
        __arm64_flags_result_12873692 = unchecked((ulong)((__arm64_flags_left_12873692) - (__arm64_flags_right_12873692)));
        x9 = __arm64_flags_result_12873692;
        x10 = unchecked((ulong)((x10) + (0x10UL)));
        RuntimeCalls.Unsupported("b.ne", 0xC46FE4UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC46FD0;
        }
        else
        {
            goto label_0xC46FE8;
        }
        label_0xC46FE8:
        ;
        x0 = x19;
        x2 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x0 = RuntimeCalls.InvokeDirect(0xB80110UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC47004;
        label_0xC46FF8:
        ;
        x9 = unchecked((ulong)(unchecked((long)(RuntimeMemory.ReadS32(x10)))));
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)((x9) << (int)(unchecked((int)(0x4UL))))))));
        x0 = unchecked((ulong)((x8) + (0x138UL)));
        goto label_0xC47004;
        label_0xC47004:
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
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xF0UL))));
        if ((x20 == 0x0UL))
        {
            goto label_0xC470A8;
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
            goto label_0xC47060;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB0UL))));
        x10 = unchecked((ulong)((x10) + (0x8UL)));
        goto label_0xC47048;
        label_0xC47048:
        ;
        x11 = RuntimeMemory.ReadU64(unchecked((ulong)((x10) + (0xFFFFFFFFFFFFFFF8UL))));
        __arm64_flags_left_12873804 = x11;
        __arm64_flags_right_12873804 = x1;
        if ((unchecked((ulong)((__arm64_flags_left_12873804) - (__arm64_flags_right_12873804))) == 0x0UL))
        {
            goto label_0xC47070;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC47054UL);
        }
        __arm64_flags_left_12873812 = x9;
        __arm64_flags_right_12873812 = 0x1UL;
        __arm64_flags_result_12873812 = unchecked((ulong)((__arm64_flags_left_12873812) - (__arm64_flags_right_12873812)));
        x9 = __arm64_flags_result_12873812;
        x10 = unchecked((ulong)((x10) + (0x10UL)));
        RuntimeCalls.Unsupported("b.ne", 0xC4705CUL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC47048;
        }
        else
        {
            goto label_0xC47060;
        }
        label_0xC47060:
        ;
        x0 = x19;
        x2 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x0 = RuntimeCalls.InvokeDirect(0xB80110UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC4707C;
        label_0xC47070:
        ;
        x9 = unchecked((ulong)(unchecked((long)(RuntimeMemory.ReadS32(x10)))));
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)((x9) << (int)(unchecked((int)(0x4UL))))))));
        x0 = unchecked((ulong)((x8) + (0x138UL)));
        goto label_0xC4707C;
        label_0xC4707C:
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
        label_0xC470A8:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```
