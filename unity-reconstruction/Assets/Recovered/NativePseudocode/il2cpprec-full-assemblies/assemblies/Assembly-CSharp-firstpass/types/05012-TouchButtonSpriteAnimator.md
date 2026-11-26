# `TouchButtonSpriteAnimator` — TypeDefIndex 5012

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0xF0` | `SpriteConfig` | `spritePressed` |
| `0xF8` | `SpriteConfig` | `spriteToggled` |
| `0x100` | `SpriteConfig` | `spriteToggledAndPressed` |

## `TouchButtonSpriteAnimator.ctor` — RVA `0xc44644`

- Lift status: **exact**; input span: 384 bytes; span to next metadata RVA: 384 bytes.
- Metadata signature: `public void .ctor() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=61 (informational only).

```csharp
public static ulong TouchButtonSpriteAnimator_ctor_RVAc44644(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
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
        x22 = 0x1BAB000UL;
        x20 = 0x1A8C000UL;
        x21 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x22) + (0x218UL))))))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xB70UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x3D0UL))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
        }
        else
        {
            x0 = 0x1A8C000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB58UL))));
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x0 = 0x1A8C000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB70UL))));
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x0 = 0x1A8C000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x3D0UL))));
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
            RuntimeMemory.WriteU8(unchecked((ulong)((x22) + (0x218UL))), unchecked((byte)(unchecked((uint)(x8)))));
        }
        label_0xC4469C:
        ;
        x0 = RuntimeMemory.ReadU64(x21);
        x22 = 0x1A8C000UL;
        x20 = RuntimeMemory.ReadU64(x20);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0xB58UL))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
        }
        else
        {
            x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        }
        label_0xC446B8:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1556240UL /* metadata target: Type.GetTypeFromHandle */, x0, x1, x2, x3);
        x1 = x0;
        x0 = x19;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC63A74UL /* metadata target: TouchControlSpriteAnimatorBase.ctor */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x22);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x8 = 0x432000UL;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x3E0UL))))), 0));
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x2 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x3 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC63528UL /* metadata target: SpriteConfig.ctor */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x21 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x21) + (0xF0UL))), x20);
        x0 = x21;
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = RuntimeMemory.ReadU64(x22);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x8 = 0x432000UL;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x340UL))))), 0));
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x2 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x3 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC63528UL /* metadata target: SpriteConfig.ctor */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), x3);
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0xF8UL))), x20);
        x0 = x19;
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = RuntimeMemory.ReadU64(x22);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x8 = 0x432000UL;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x378UL))))), 0));
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x2 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x3 = 0x0UL;
        x22 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC63528UL /* metadata target: SpriteConfig.ctor */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x20 = unchecked((ulong)((x19) + (0x8UL)));
        x0 = x20;
        x1 = x22;
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x8UL))), x22);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x8 = RuntimeMemory.ReadU64(x21);
        if ((x8 == 0x0UL))
        {
        }
        else
        {
            x9 = unchecked((ulong)(unchecked((uint)(0x3FA00000UL))));
            RuntimeMemory.WriteU32(unchecked((ulong)((x8) + (0x30UL))), unchecked((uint)(x9)));
            x8 = RuntimeMemory.ReadU64(x19);
            if ((x8 == 0x0UL))
            {
            }
            else
            {
                x9 = unchecked((ulong)(unchecked((uint)(0xCCCDUL))));
                x9 = unchecked((ulong)(unchecked((uint)(unchecked((ulong)((unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) & (unchecked((uint)((~(0xFFFFUL)))))))))) | (unchecked((ulong)((unchecked((ulong)((0x3F8CUL) << (int)(unchecked((int)(0x10UL)))))) << (int)(unchecked((int)(0x0UL))))))))))));
                RuntimeMemory.WriteU32(unchecked((ulong)((x8) + (0x30UL))), unchecked((uint)(x9)));
                x8 = RuntimeMemory.ReadU64(x20);
                if ((x8 == 0x0UL))
                {
                }
                else
                {
                    x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
                    x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
                    x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
                    x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
                    x9 = unchecked((ulong)(unchecked((uint)(0x6666UL))));
                    x9 = unchecked((ulong)(unchecked((uint)(unchecked((ulong)((unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) & (unchecked((uint)((~(0xFFFFUL)))))))))) | (unchecked((ulong)((unchecked((ulong)((0x3FA6UL) << (int)(unchecked((int)(0x10UL)))))) << (int)(unchecked((int)(0x0UL))))))))))));
                    RuntimeMemory.WriteU32(unchecked((ulong)((x8) + (0x30UL))), unchecked((uint)(x9)));
                    x30 = RuntimeMemory.ReadU64(sp);
                    return x0;
                }
            }
        }
        label_0xC447C0:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        return default(ulong);
    }
```

## `TouchButtonSpriteAnimator.SetSprite` — RVA `0xc447c4`

- Lift status: **exact**; input span: 104 bytes; span to next metadata RVA: 104 bytes.
- Metadata signature: `public void SetSprite(Sprite sprite) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=11 (informational only).

```csharp
public static ulong TouchButtonSpriteAnimator_SetSprite_RVAc447c4(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
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
            goto label_0xC44828;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC447D8UL);
        }
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x18UL))), x1);
        x19 = x1;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xF0UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC44828;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC447ECUL);
        }
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x18UL))), x19);
        x1 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xF8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC44828;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC44800UL);
        }
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x18UL))), x19);
        x1 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x100UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC44828;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC44814UL);
        }
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x18UL))), x19);
        x1 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0xB7D8D0UL);
        label_0xC44828:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `TouchButtonSpriteAnimator.SetColor` — RVA `0xc4482c`

- Lift status: **exact**; input span: 80 bytes; span to next metadata RVA: 80 bytes.
- Metadata signature: `public void SetColor(Color color) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=5 (informational only).

```csharp
public static ulong TouchButtonSpriteAnimator_SetColor_RVAc4482c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_pair_address_12863544 = default(ulong);
        ulong __arm64_pair_address_12863548 = default(ulong);
        ulong __arm64_pair_address_12863560 = default(ulong);
        ulong __arm64_pair_address_12863564 = default(ulong);
        ulong __arm64_pair_address_12863576 = default(ulong);
        ulong __arm64_pair_address_12863580 = default(ulong);
        ulong __arm64_pair_address_12863592 = default(ulong);
        ulong __arm64_pair_address_12863596 = default(ulong);
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
            __arm64_pair_address_12863544 = unchecked((ulong)((x8) + (0x20UL)));
            RuntimeMemory.WriteF32(__arm64_pair_address_12863544, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
            RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_12863544) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0));
            __arm64_pair_address_12863548 = unchecked((ulong)((x8) + (0x28UL)));
            RuntimeMemory.WriteF32(__arm64_pair_address_12863548, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0));
            RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_12863548) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0));
            x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xF0UL))));
            if ((x8 == 0x0UL))
            {
            }
            else
            {
                __arm64_pair_address_12863560 = unchecked((ulong)((x8) + (0x20UL)));
                RuntimeMemory.WriteF32(__arm64_pair_address_12863560, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
                RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_12863560) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0));
                __arm64_pair_address_12863564 = unchecked((ulong)((x8) + (0x28UL)));
                RuntimeMemory.WriteF32(__arm64_pair_address_12863564, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0));
                RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_12863564) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0));
                x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xF8UL))));
                if ((x8 == 0x0UL))
                {
                }
                else
                {
                    __arm64_pair_address_12863576 = unchecked((ulong)((x8) + (0x20UL)));
                    RuntimeMemory.WriteF32(__arm64_pair_address_12863576, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
                    RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_12863576) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0));
                    __arm64_pair_address_12863580 = unchecked((ulong)((x8) + (0x28UL)));
                    RuntimeMemory.WriteF32(__arm64_pair_address_12863580, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0));
                    RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_12863580) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0));
                    x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x100UL))));
                    if ((x8 == 0x0UL))
                    {
                    }
                    else
                    {
                        __arm64_pair_address_12863592 = unchecked((ulong)((x8) + (0x20UL)));
                        RuntimeMemory.WriteF32(__arm64_pair_address_12863592, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
                        RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_12863592) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0));
                        __arm64_pair_address_12863596 = unchecked((ulong)((x8) + (0x28UL)));
                        RuntimeMemory.WriteF32(__arm64_pair_address_12863596, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0));
                        RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_12863596) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0));
                        x30 = RuntimeMemory.ReadU64(sp);
                        return x0;
                    }
                }
            }
        }
        label_0xC44878:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `TouchButtonSpriteAnimator.SetStateSprite` — RVA `0xc4487c`

- Lift status: **exact**; input span: 96 bytes; span to next metadata RVA: 96 bytes.
- Metadata signature: `public void SetStateSprite(TouchButtonSpriteAnimator.ControlState state, Sprite sprite) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=20 (informational only).

```csharp
public static ulong TouchButtonSpriteAnimator_SetStateSprite_RVAc4487c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12863612 = default(uint);
        uint __arm64_flags_right_12863612 = default(uint);
        ulong x10 = default(ulong);
        ulong x11 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        __arm64_flags_left_12863612 = unchecked((uint)(x1));
        __arm64_flags_right_12863612 = unchecked((uint)0x3UL);
        if (((__arm64_flags_left_12863612 >= __arm64_flags_right_12863612) && (!((unchecked((uint)((__arm64_flags_left_12863612) - (__arm64_flags_right_12863612))) == unchecked((uint)0x0UL))))))
        {
            goto label_0xC448D4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = 0x452000UL;
        x8 = unchecked((ulong)(unchecked((uint)(x1))));
        x9 = unchecked((ulong)((x9) + (0xCCUL)));
        x10 = 0xC448A0UL;
        x11 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x9) + (unchecked((ulong)(unchecked((uint)(x8))))))))))));
        x10 = unchecked((ulong)((x10) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x11))) << (int)(unchecked((int)(unchecked((uint)(0x2UL))))))))))));
        return RuntimeCalls.InvokeIndirect(x10);
        label_0xC448D4:
        ;
        x1 = x2;
        return RuntimeCalls.InvokeDirect(0xC447C4UL /* metadata target: TouchButtonSpriteAnimator.SetSprite */);
        return default(ulong);
    }
```

## `TouchButtonSpriteAnimator.GetStateSpriteConfig` — RVA `0xc448dc`

- Lift status: **exact**; input span: 80 bytes; span to next metadata RVA: 80 bytes.
- Metadata signature: `public SpriteConfig GetStateSpriteConfig(TouchButtonSpriteAnimator.ControlState state) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=16 (informational only).

```csharp
public static ulong TouchButtonSpriteAnimator_GetStateSpriteConfig_RVAc448dc(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12863708 = default(uint);
        uint __arm64_flags_right_12863708 = default(uint);
        ulong x10 = default(ulong);
        ulong x11 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        __arm64_flags_left_12863708 = unchecked((uint)(x1));
        __arm64_flags_right_12863708 = unchecked((uint)0x3UL);
        if (((__arm64_flags_left_12863708 >= __arm64_flags_right_12863708) && (!((unchecked((uint)((__arm64_flags_left_12863708) - (__arm64_flags_right_12863708))) == unchecked((uint)0x0UL))))))
        {
            goto label_0xC44908;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = 0x452000UL;
        x8 = unchecked((ulong)(unchecked((uint)(x1))));
        x9 = unchecked((ulong)((x9) + (0xD0UL)));
        x10 = 0xC44900UL;
        x11 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x9) + (unchecked((ulong)(unchecked((uint)(x8))))))))))));
        x10 = unchecked((ulong)((x10) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x11))) << (int)(unchecked((int)(unchecked((uint)(0x2UL))))))))))));
        return RuntimeCalls.InvokeIndirect(x10);
        label_0xC44908:
        ;
        x0 = 0x0UL;
        return x0;
        return default(ulong);
    }
```

## `TouchButtonSpriteAnimator.SetStateColor` — RVA `0xc4492c`

- Lift status: **exact**; input span: 88 bytes; span to next metadata RVA: 88 bytes.
- Metadata signature: `public void SetStateColor(TouchButtonSpriteAnimator.ControlState state, Color color) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=18 (informational only).

```csharp
public static ulong TouchButtonSpriteAnimator_SetStateColor_RVAc4492c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12863788 = default(uint);
        uint __arm64_flags_right_12863788 = default(uint);
        ulong x10 = default(ulong);
        ulong x11 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        __arm64_flags_left_12863788 = unchecked((uint)(x1));
        __arm64_flags_right_12863788 = unchecked((uint)0x3UL);
        if (((__arm64_flags_left_12863788 >= __arm64_flags_right_12863788) && (!((unchecked((uint)((__arm64_flags_left_12863788) - (__arm64_flags_right_12863788))) == unchecked((uint)0x0UL))))))
        {
            goto label_0xC44980;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = 0x452000UL;
        x8 = unchecked((ulong)(unchecked((uint)(x1))));
        x9 = unchecked((ulong)((x9) + (0xCCUL)));
        x10 = 0xC44950UL;
        x11 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x9) + (unchecked((ulong)(unchecked((uint)(x8))))))))))));
        x10 = unchecked((ulong)((x10) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x11))) << (int)(unchecked((int)(unchecked((uint)(0x2UL))))))))))));
        return RuntimeCalls.InvokeIndirect(x10);
        label_0xC44980:
        ;
        return RuntimeCalls.InvokeDirect(0xC4482CUL /* metadata target: TouchButtonSpriteAnimator.SetColor */);
        return default(ulong);
    }
```

## `TouchButtonSpriteAnimator.OnInitComponent` — RVA `0xc44984`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `protected override void OnInitComponent() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static ulong TouchButtonSpriteAnimator_OnInitComponent_RVAc44984(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x1 = 0x0UL;
        return RuntimeCalls.InvokeDirect(0xC63B4CUL /* metadata target: TouchControlSpriteAnimatorBase.OnInitComponent */);
        return default(ulong);
    }
```

## `TouchButtonSpriteAnimator.OnUpdateAnimator` — RVA `0xc4498c`

- Lift status: **exact**; input span: 392 bytes; span to next metadata RVA: 392 bytes.
- Metadata signature: `protected override void OnUpdateAnimator(bool skipAnim) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=56 (informational only).

```csharp
public static ulong TouchButtonSpriteAnimator_OnUpdateAnimator_RVAc4498c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12863980 = default(uint);
        ulong __arm64_flags_left_12864000 = default(ulong);
        uint __arm64_flags_right_12863980 = default(uint);
        ulong __arm64_flags_right_12864000 = default(ulong);
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
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x219UL))))))));
        x19 = unchecked((ulong)(unchecked((uint)(x1))));
        x20 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC449CC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB78UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x219UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC449CC;
        label_0xC449CC:
        ;
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x28UL))));
        if ((x21 == 0x0UL))
        {
            goto label_0xC44A08;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = 0x1A8C000UL;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0xB78UL))));
        x8 = RuntimeMemory.ReadU64(x21);
        x1 = RuntimeMemory.ReadU64(x9);
        x10 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x130UL))))))));
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x1) + (0x130UL))))))));
        __arm64_flags_left_12863980 = unchecked((uint)(x10));
        __arm64_flags_right_12863980 = unchecked((uint)(x9));
        if ((!((__arm64_flags_left_12863980 >= __arm64_flags_right_12863980))))
        {
            goto label_0xC44B08;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xC8UL))));
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) << (int)(unchecked((int)(unchecked((uint)(0x3UL))))))))))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xFFFFFFFFFFFFFFF8UL))));
        __arm64_flags_left_12864000 = x8;
        __arm64_flags_right_12864000 = x1;
        if ((!((unchecked((ulong)((__arm64_flags_left_12864000) - (__arm64_flags_right_12864000))) == 0x0UL))))
        {
            goto label_0xC44B08;
        }
        else
        {
            goto label_0xC44A08;
        }
        label_0xC44A08:
        ;
        x22 = 0x1A8C000UL;
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0xD8UL))));
        x0 = RuntimeMemory.ReadU64(x22);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC44A20;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC44A1CUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC44A20;
        label_0xC44A20:
        ;
        x0 = x21;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179568CUL /* metadata target: Object.op_Equality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC44A5C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(x22);
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x40UL))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC44A48;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC44A44UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC44A48;
        label_0xC44A48:
        ;
        x0 = x22;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179568CUL /* metadata target: Object.op_Equality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC44A6C;
        }
        else
        {
            goto label_0xC44A5C;
        }
        label_0xC44A5C:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        label_0xC44A6C:
        ;
        if ((x21 == 0x0UL))
        {
            goto label_0xC44B10;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xE0UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC44B10;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x1CUL))))))));
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x1C0UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC44AA4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC44A84UL);
        }
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC44AA4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x100UL))));
        if ((x1 == 0x0UL))
        {
            goto label_0xC44AA8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x1) + (0x10UL))))))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC44AA8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC44A98UL);
        }
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC44AB0;
        }
        else
        {
            goto label_0xC44A9C;
        }
        label_0xC44A9C:
        ;
        if ((x1 != 0x0UL))
        {
            goto label_0xC44ACC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC44AA0UL);
        }
        goto label_0xC44AD4;
        label_0xC44AA4:
        ;
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC44AC0;
        }
        else
        {
            goto label_0xC44AA8;
        }
        label_0xC44AA8:
        ;
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xF8UL))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC44A9C;
        }
        else
        {
            goto label_0xC44AB0;
        }
        label_0xC44AB0:
        ;
        if ((x1 == 0x0UL))
        {
            goto label_0xC44AC4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x1) + (0x10UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC44AD8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC44ABCUL);
        }
        goto label_0xC44AC4;
        label_0xC44AC0:
        ;
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC44AD4;
        }
        else
        {
            goto label_0xC44AC4;
        }
        label_0xC44AC4:
        ;
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xF0UL))));
        if ((x1 == 0x0UL))
        {
            goto label_0xC44AD4;
        }
        else
        {
            goto label_0xC44ACC;
        }
        label_0xC44ACC:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x1) + (0x10UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC44AD8;
        }
        else
        {
            goto label_0xC44AD4;
        }
        label_0xC44AD4:
        ;
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x78UL))));
        goto label_0xC44AD8;
        label_0xC44AD8:
        ;
        x0 = x20;
        x2 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x3 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x4 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC63E00UL /* metadata target: TouchControlSpriteAnimatorBase.BeginSpriteAnim */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x1 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x19))) & (unchecked((uint)(0x1UL)))))));
        x0 = x20;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x2 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0xC64384UL /* metadata target: TouchControlSpriteAnimatorBase.UpdateSpriteAnimation */);
        label_0xC44B08:
        ;
        x0 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xB7DF10UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, unchecked((ulong)(unchecked((uint)(x3)))));
        goto label_0xC44B10;
        label_0xC44B10:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, unchecked((ulong)(unchecked((uint)(x3)))));
        return default(ulong);
    }
```

## `TouchButtonSpriteAnimator.GetComponent` — RVA `0xc44b30`

- Lift status: **exact**; input span: 4 bytes; span to next metadata RVA: 4 bytes.
- Metadata signature: `private MonoBehaviour ControlFreak2.Internal.ISpriteAnimator.GetComponent() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=0 (informational only).

```csharp
public static ulong TouchButtonSpriteAnimator_GetComponent_RVAc44b30(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        return x0;
        return default(ulong);
    }
```

## `TouchButtonSpriteAnimator.AddUsedSprites` — RVA `0xc44b34`

- Lift status: **partial**; input span: 512 bytes; span to next metadata RVA: 512 bytes.
- Metadata signature: `private void ControlFreak2.Internal.ISpriteAnimator.AddUsedSprites(ISpriteOptimizer optimizer) { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=84 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'b.ne' at 0xc44bac; reason: Unknown IR expression at 0xc44bac; reason: Unsupported instruction 'b.ne' at 0xc44c18; reason: Unknown IR expression at 0xc44c18; reason: Unsupported instruction 'b.ne' at 0xc44c84; reason: Unknown IR expression at 0xc44c84; reason: Unsupported instruction 'b.ne' at 0xc44cf0; reason: Unknown IR expression at 0xc44cf0

```csharp
public static ulong TouchButtonSpriteAnimator_AddUsedSprites_RVAc44b34(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_flags_left_12864412 = default(ulong);
        ulong __arm64_flags_left_12864420 = default(ulong);
        ulong __arm64_flags_left_12864520 = default(ulong);
        ulong __arm64_flags_left_12864528 = default(ulong);
        ulong __arm64_flags_left_12864628 = default(ulong);
        ulong __arm64_flags_left_12864636 = default(ulong);
        ulong __arm64_flags_left_12864736 = default(ulong);
        ulong __arm64_flags_left_12864744 = default(ulong);
        ulong __arm64_flags_result_12864420 = default(ulong);
        ulong __arm64_flags_result_12864528 = default(ulong);
        ulong __arm64_flags_result_12864636 = default(ulong);
        ulong __arm64_flags_result_12864744 = default(ulong);
        ulong __arm64_flags_right_12864412 = default(ulong);
        ulong __arm64_flags_right_12864420 = default(ulong);
        ulong __arm64_flags_right_12864520 = default(ulong);
        ulong __arm64_flags_right_12864528 = default(ulong);
        ulong __arm64_flags_right_12864628 = default(ulong);
        ulong __arm64_flags_right_12864636 = default(ulong);
        ulong __arm64_flags_right_12864736 = default(ulong);
        ulong __arm64_flags_right_12864744 = default(ulong);
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
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x21AUL))))))));
        x19 = x1;
        x20 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC44B68;
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
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x21AUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC44B68;
        label_0xC44B68:
        ;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x78UL))));
        if ((x9 == 0x0UL))
        {
            goto label_0xC44D30;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC44B70UL);
        }
        if ((x19 == 0x0UL))
        {
            goto label_0xC44D30;
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
            goto label_0xC44BB0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB0UL))));
        x10 = unchecked((ulong)((x10) + (0x8UL)));
        goto label_0xC44B98;
        label_0xC44B98:
        ;
        x11 = RuntimeMemory.ReadU64(unchecked((ulong)((x10) + (0xFFFFFFFFFFFFFFF8UL))));
        __arm64_flags_left_12864412 = x11;
        __arm64_flags_right_12864412 = x1;
        if ((unchecked((ulong)((__arm64_flags_left_12864412) - (__arm64_flags_right_12864412))) == 0x0UL))
        {
            goto label_0xC44BC0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC44BA4UL);
        }
        __arm64_flags_left_12864420 = x9;
        __arm64_flags_right_12864420 = 0x1UL;
        __arm64_flags_result_12864420 = unchecked((ulong)((__arm64_flags_left_12864420) - (__arm64_flags_right_12864420)));
        x9 = __arm64_flags_result_12864420;
        x10 = unchecked((ulong)((x10) + (0x10UL)));
        RuntimeCalls.Unsupported("b.ne", 0xC44BACUL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC44B98;
        }
        else
        {
            goto label_0xC44BB0;
        }
        label_0xC44BB0:
        ;
        x2 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xB80110UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC44BD0;
        label_0xC44BC0:
        ;
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(x10)));
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) + (unchecked((uint)(0x1UL)))))));
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) << (int)(unchecked((int)(unchecked((uint)(0x4UL))))))))))));
        x0 = unchecked((ulong)((x8) + (0x138UL)));
        goto label_0xC44BD0;
        label_0xC44BD0:
        ;
        x8 = RuntimeMemory.ReadU64(x0);
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x8UL))));
        x0 = x19;
        x1 = x21;
        x0 = RuntimeCalls.InvokeIndirect(x8, x0, x1, x2, x3);
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xF0UL))));
        if ((x9 == 0x0UL))
        {
            goto label_0xC44D30;
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
            goto label_0xC44C1C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB0UL))));
        x10 = unchecked((ulong)((x10) + (0x8UL)));
        goto label_0xC44C04;
        label_0xC44C04:
        ;
        x11 = RuntimeMemory.ReadU64(unchecked((ulong)((x10) + (0xFFFFFFFFFFFFFFF8UL))));
        __arm64_flags_left_12864520 = x11;
        __arm64_flags_right_12864520 = x1;
        if ((unchecked((ulong)((__arm64_flags_left_12864520) - (__arm64_flags_right_12864520))) == 0x0UL))
        {
            goto label_0xC44C2C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC44C10UL);
        }
        __arm64_flags_left_12864528 = x9;
        __arm64_flags_right_12864528 = 0x1UL;
        __arm64_flags_result_12864528 = unchecked((ulong)((__arm64_flags_left_12864528) - (__arm64_flags_right_12864528)));
        x9 = __arm64_flags_result_12864528;
        x10 = unchecked((ulong)((x10) + (0x10UL)));
        RuntimeCalls.Unsupported("b.ne", 0xC44C18UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC44C04;
        }
        else
        {
            goto label_0xC44C1C;
        }
        label_0xC44C1C:
        ;
        x2 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xB80110UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC44C3C;
        label_0xC44C2C:
        ;
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(x10)));
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) + (unchecked((uint)(0x1UL)))))));
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) << (int)(unchecked((int)(unchecked((uint)(0x4UL))))))))))));
        x0 = unchecked((ulong)((x8) + (0x138UL)));
        goto label_0xC44C3C;
        label_0xC44C3C:
        ;
        x8 = RuntimeMemory.ReadU64(x0);
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x8UL))));
        x0 = x19;
        x1 = x21;
        x0 = RuntimeCalls.InvokeIndirect(x8, x0, x1, x2, x3);
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xF8UL))));
        if ((x9 == 0x0UL))
        {
            goto label_0xC44D30;
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
            goto label_0xC44C88;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB0UL))));
        x10 = unchecked((ulong)((x10) + (0x8UL)));
        goto label_0xC44C70;
        label_0xC44C70:
        ;
        x11 = RuntimeMemory.ReadU64(unchecked((ulong)((x10) + (0xFFFFFFFFFFFFFFF8UL))));
        __arm64_flags_left_12864628 = x11;
        __arm64_flags_right_12864628 = x1;
        if ((unchecked((ulong)((__arm64_flags_left_12864628) - (__arm64_flags_right_12864628))) == 0x0UL))
        {
            goto label_0xC44C98;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC44C7CUL);
        }
        __arm64_flags_left_12864636 = x9;
        __arm64_flags_right_12864636 = 0x1UL;
        __arm64_flags_result_12864636 = unchecked((ulong)((__arm64_flags_left_12864636) - (__arm64_flags_right_12864636)));
        x9 = __arm64_flags_result_12864636;
        x10 = unchecked((ulong)((x10) + (0x10UL)));
        RuntimeCalls.Unsupported("b.ne", 0xC44C84UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC44C70;
        }
        else
        {
            goto label_0xC44C88;
        }
        label_0xC44C88:
        ;
        x2 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xB80110UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC44CA8;
        label_0xC44C98:
        ;
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(x10)));
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) + (unchecked((uint)(0x1UL)))))));
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) << (int)(unchecked((int)(unchecked((uint)(0x4UL))))))))))));
        x0 = unchecked((ulong)((x8) + (0x138UL)));
        goto label_0xC44CA8;
        label_0xC44CA8:
        ;
        x8 = RuntimeMemory.ReadU64(x0);
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x8UL))));
        x0 = x19;
        x1 = x21;
        x0 = RuntimeCalls.InvokeIndirect(x8, x0, x1, x2, x3);
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x100UL))));
        if ((x9 == 0x0UL))
        {
            goto label_0xC44D30;
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
            goto label_0xC44CF4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB0UL))));
        x10 = unchecked((ulong)((x10) + (0x8UL)));
        goto label_0xC44CDC;
        label_0xC44CDC:
        ;
        x11 = RuntimeMemory.ReadU64(unchecked((ulong)((x10) + (0xFFFFFFFFFFFFFFF8UL))));
        __arm64_flags_left_12864736 = x11;
        __arm64_flags_right_12864736 = x1;
        if ((unchecked((ulong)((__arm64_flags_left_12864736) - (__arm64_flags_right_12864736))) == 0x0UL))
        {
            goto label_0xC44D04;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC44CE8UL);
        }
        __arm64_flags_left_12864744 = x9;
        __arm64_flags_right_12864744 = 0x1UL;
        __arm64_flags_result_12864744 = unchecked((ulong)((__arm64_flags_left_12864744) - (__arm64_flags_right_12864744)));
        x9 = __arm64_flags_result_12864744;
        x10 = unchecked((ulong)((x10) + (0x10UL)));
        RuntimeCalls.Unsupported("b.ne", 0xC44CF0UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC44CDC;
        }
        else
        {
            goto label_0xC44CF4;
        }
        label_0xC44CF4:
        ;
        x2 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xB80110UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC44D14;
        label_0xC44D04:
        ;
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(x10)));
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) + (unchecked((uint)(0x1UL)))))));
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) << (int)(unchecked((int)(unchecked((uint)(0x4UL))))))))))));
        x0 = unchecked((ulong)((x8) + (0x138UL)));
        goto label_0xC44D14;
        label_0xC44D14:
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
        label_0xC44D30:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `TouchButtonSpriteAnimator.OnSpriteOptimization` — RVA `0xc44d34`

- Lift status: **partial**; input span: 560 bytes; span to next metadata RVA: 560 bytes.
- Metadata signature: `private void ControlFreak2.Internal.ISpriteAnimator.OnSpriteOptimization(ISpriteOptimizer optimizer) { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=88 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'b.ne' at 0xc44dac; reason: Unknown IR expression at 0xc44dac; reason: Unsupported instruction 'b.ne' at 0xc44e24; reason: Unknown IR expression at 0xc44e24; reason: Unsupported instruction 'b.ne' at 0xc44e9c; reason: Unknown IR expression at 0xc44e9c; reason: Unsupported instruction 'b.ne' at 0xc44f14; reason: Unknown IR expression at 0xc44f14

```csharp
public static ulong TouchButtonSpriteAnimator_OnSpriteOptimization_RVAc44d34(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_flags_left_12864924 = default(ulong);
        ulong __arm64_flags_left_12864932 = default(ulong);
        ulong __arm64_flags_left_12865044 = default(ulong);
        ulong __arm64_flags_left_12865052 = default(ulong);
        ulong __arm64_flags_left_12865164 = default(ulong);
        ulong __arm64_flags_left_12865172 = default(ulong);
        ulong __arm64_flags_left_12865284 = default(ulong);
        ulong __arm64_flags_left_12865292 = default(ulong);
        ulong __arm64_flags_result_12864932 = default(ulong);
        ulong __arm64_flags_result_12865052 = default(ulong);
        ulong __arm64_flags_result_12865172 = default(ulong);
        ulong __arm64_flags_result_12865292 = default(ulong);
        ulong __arm64_flags_right_12864924 = default(ulong);
        ulong __arm64_flags_right_12864932 = default(ulong);
        ulong __arm64_flags_right_12865044 = default(ulong);
        ulong __arm64_flags_right_12865052 = default(ulong);
        ulong __arm64_flags_right_12865164 = default(ulong);
        ulong __arm64_flags_right_12865172 = default(ulong);
        ulong __arm64_flags_right_12865284 = default(ulong);
        ulong __arm64_flags_right_12865292 = default(ulong);
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
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x21BUL))))))));
        x19 = x1;
        x20 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC44D68;
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
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x21BUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC44D68;
        label_0xC44D68:
        ;
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x78UL))));
        if ((x21 == 0x0UL))
        {
            goto label_0xC44F60;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x18UL))));
        if ((x19 == 0x0UL))
        {
            goto label_0xC44F60;
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
            goto label_0xC44DB0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB0UL))));
        x10 = unchecked((ulong)((x10) + (0x8UL)));
        goto label_0xC44D98;
        label_0xC44D98:
        ;
        x11 = RuntimeMemory.ReadU64(unchecked((ulong)((x10) + (0xFFFFFFFFFFFFFFF8UL))));
        __arm64_flags_left_12864924 = x11;
        __arm64_flags_right_12864924 = x1;
        if ((unchecked((ulong)((__arm64_flags_left_12864924) - (__arm64_flags_right_12864924))) == 0x0UL))
        {
            goto label_0xC44DC0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC44DA4UL);
        }
        __arm64_flags_left_12864932 = x9;
        __arm64_flags_right_12864932 = 0x1UL;
        __arm64_flags_result_12864932 = unchecked((ulong)((__arm64_flags_left_12864932) - (__arm64_flags_right_12864932)));
        x9 = __arm64_flags_result_12864932;
        x10 = unchecked((ulong)((x10) + (0x10UL)));
        RuntimeCalls.Unsupported("b.ne", 0xC44DACUL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC44D98;
        }
        else
        {
            goto label_0xC44DB0;
        }
        label_0xC44DB0:
        ;
        x0 = x19;
        x2 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x0 = RuntimeCalls.InvokeDirect(0xB80110UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC44DCC;
        label_0xC44DC0:
        ;
        x9 = unchecked((ulong)(unchecked((long)(RuntimeMemory.ReadS32(x10)))));
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)((x9) << (int)(unchecked((int)(0x4UL))))))));
        x0 = unchecked((ulong)((x8) + (0x138UL)));
        goto label_0xC44DCC;
        label_0xC44DCC:
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
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xF0UL))));
        if ((x21 == 0x0UL))
        {
            goto label_0xC44F60;
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
            goto label_0xC44E28;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB0UL))));
        x10 = unchecked((ulong)((x10) + (0x8UL)));
        goto label_0xC44E10;
        label_0xC44E10:
        ;
        x11 = RuntimeMemory.ReadU64(unchecked((ulong)((x10) + (0xFFFFFFFFFFFFFFF8UL))));
        __arm64_flags_left_12865044 = x11;
        __arm64_flags_right_12865044 = x1;
        if ((unchecked((ulong)((__arm64_flags_left_12865044) - (__arm64_flags_right_12865044))) == 0x0UL))
        {
            goto label_0xC44E38;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC44E1CUL);
        }
        __arm64_flags_left_12865052 = x9;
        __arm64_flags_right_12865052 = 0x1UL;
        __arm64_flags_result_12865052 = unchecked((ulong)((__arm64_flags_left_12865052) - (__arm64_flags_right_12865052)));
        x9 = __arm64_flags_result_12865052;
        x10 = unchecked((ulong)((x10) + (0x10UL)));
        RuntimeCalls.Unsupported("b.ne", 0xC44E24UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC44E10;
        }
        else
        {
            goto label_0xC44E28;
        }
        label_0xC44E28:
        ;
        x0 = x19;
        x2 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x0 = RuntimeCalls.InvokeDirect(0xB80110UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC44E44;
        label_0xC44E38:
        ;
        x9 = unchecked((ulong)(unchecked((long)(RuntimeMemory.ReadS32(x10)))));
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)((x9) << (int)(unchecked((int)(0x4UL))))))));
        x0 = unchecked((ulong)((x8) + (0x138UL)));
        goto label_0xC44E44;
        label_0xC44E44:
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
            goto label_0xC44F60;
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
            goto label_0xC44EA0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB0UL))));
        x10 = unchecked((ulong)((x10) + (0x8UL)));
        goto label_0xC44E88;
        label_0xC44E88:
        ;
        x11 = RuntimeMemory.ReadU64(unchecked((ulong)((x10) + (0xFFFFFFFFFFFFFFF8UL))));
        __arm64_flags_left_12865164 = x11;
        __arm64_flags_right_12865164 = x1;
        if ((unchecked((ulong)((__arm64_flags_left_12865164) - (__arm64_flags_right_12865164))) == 0x0UL))
        {
            goto label_0xC44EB0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC44E94UL);
        }
        __arm64_flags_left_12865172 = x9;
        __arm64_flags_right_12865172 = 0x1UL;
        __arm64_flags_result_12865172 = unchecked((ulong)((__arm64_flags_left_12865172) - (__arm64_flags_right_12865172)));
        x9 = __arm64_flags_result_12865172;
        x10 = unchecked((ulong)((x10) + (0x10UL)));
        RuntimeCalls.Unsupported("b.ne", 0xC44E9CUL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC44E88;
        }
        else
        {
            goto label_0xC44EA0;
        }
        label_0xC44EA0:
        ;
        x0 = x19;
        x2 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x0 = RuntimeCalls.InvokeDirect(0xB80110UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC44EBC;
        label_0xC44EB0:
        ;
        x9 = unchecked((ulong)(unchecked((long)(RuntimeMemory.ReadS32(x10)))));
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)((x9) << (int)(unchecked((int)(0x4UL))))))));
        x0 = unchecked((ulong)((x8) + (0x138UL)));
        goto label_0xC44EBC;
        label_0xC44EBC:
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
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x100UL))));
        if ((x20 == 0x0UL))
        {
            goto label_0xC44F60;
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
            goto label_0xC44F18;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB0UL))));
        x10 = unchecked((ulong)((x10) + (0x8UL)));
        goto label_0xC44F00;
        label_0xC44F00:
        ;
        x11 = RuntimeMemory.ReadU64(unchecked((ulong)((x10) + (0xFFFFFFFFFFFFFFF8UL))));
        __arm64_flags_left_12865284 = x11;
        __arm64_flags_right_12865284 = x1;
        if ((unchecked((ulong)((__arm64_flags_left_12865284) - (__arm64_flags_right_12865284))) == 0x0UL))
        {
            goto label_0xC44F28;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC44F0CUL);
        }
        __arm64_flags_left_12865292 = x9;
        __arm64_flags_right_12865292 = 0x1UL;
        __arm64_flags_result_12865292 = unchecked((ulong)((__arm64_flags_left_12865292) - (__arm64_flags_right_12865292)));
        x9 = __arm64_flags_result_12865292;
        x10 = unchecked((ulong)((x10) + (0x10UL)));
        RuntimeCalls.Unsupported("b.ne", 0xC44F14UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC44F00;
        }
        else
        {
            goto label_0xC44F18;
        }
        label_0xC44F18:
        ;
        x0 = x19;
        x2 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x0 = RuntimeCalls.InvokeDirect(0xB80110UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC44F34;
        label_0xC44F28:
        ;
        x9 = unchecked((ulong)(unchecked((long)(RuntimeMemory.ReadS32(x10)))));
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)((x9) << (int)(unchecked((int)(0x4UL))))))));
        x0 = unchecked((ulong)((x8) + (0x138UL)));
        goto label_0xC44F34;
        label_0xC44F34:
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
        label_0xC44F60:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```
