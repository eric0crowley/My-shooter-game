# `AmmoPickup` — TypeDefIndex 3376

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x20` | `GameObject` | `weaponObj` |
| `0x28` | `WeaponBehavior` | `WeaponBehaviorComponent` |
| `0x30` | `PlayerWeapons` | `PlayerWeaponsComponent` |
| `0x38` | `Transform` | `myTransform` |
| `0x40` | `int` | `weaponNumber` |
| `0x44` | `int` | `objectPoolIndex` |
| `0x48` | `bool` | `removeOnUse` |
| `0x50` | `AudioClip` | `pickupSound` |
| `0x58` | `AudioClip` | `fullSound` |
| `0x60` | `int` | `ammoToAdd` |
| `0x68` | `Sprite` | `ammoPickupReticle` |

## `AmmoPickup.Start` — RVA `0xc92bac`

- Lift status: **exact**; input span: 556 bytes; span to next metadata RVA: 556 bytes.
- Metadata signature: `private void Start() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=80 (informational only).

```csharp
public static ulong AmmoPickup_Start_RVAc92bac(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13184288 = default(uint);
        uint __arm64_flags_left_13184296 = default(uint);
        uint __arm64_flags_left_13184332 = default(uint);
        uint __arm64_flags_left_13184396 = default(uint);
        uint __arm64_flags_right_13184288 = default(uint);
        uint __arm64_flags_right_13184296 = default(uint);
        uint __arm64_flags_right_13184332 = default(uint);
        uint __arm64_flags_right_13184396 = default(uint);
        ulong sp = default(ulong);
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
        x20 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x45DUL))))))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC92C10;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xCD8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xEA8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD08UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x158UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x4A8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x45DUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC92C10;
        label_0xC92C10:
        ;
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792154UL /* metadata target: Component.get_transform */, x0, x1, x2, x3);
        x1 = x0;
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x38UL))), x1);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x176F8DCUL /* metadata target: Camera.get_main */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC92D60;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792154UL /* metadata target: Component.get_transform */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC92D60;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xCD8UL))));
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xE31BC8UL, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC92D60;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x30UL))));
        x20 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x20) + (0x20UL))), x1);
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x20);
        if ((x0 == 0x0UL))
        {
            goto label_0xC92D60;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xD08UL))));
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xE49488UL, x0, x1, x2, x3);
        x21 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x21) + (0x30UL))), x0);
        x1 = x0;
        x0 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC92D60;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xEA8UL))));
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xE31BC8UL, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x21);
        if ((x8 == 0x0UL))
        {
            goto label_0xC92D60;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x90UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC92D60;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x60UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC92D60;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = 0x1A8D000UL;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0x4A8UL))));
        x22 = x0;
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x238UL))));
        x0 = RuntimeMemory.ReadU64(x9);
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC92CE8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC92CE4UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC92CE8;
        label_0xC92CE8:
        ;
        x2 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = x22;
        x1 = x23;
        x3 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17CB368UL /* metadata target: Physics.IgnoreCollision */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x8 = RuntimeMemory.ReadU64(x21);
        if ((x8 == 0x0UL))
        {
            goto label_0xC92D60;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x22 = 0x1A8E000UL;
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x158UL))));
        x23 = unchecked((ulong)(unchecked((uint)(0x4UL))));
        goto label_0xC92D10;
        label_0xC92D10:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xE8UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC92D60;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        x24 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x23))) - (unchecked((uint)(0x4UL)))))));
        __arm64_flags_left_13184288 = unchecked((uint)(x24));
        __arm64_flags_right_13184288 = unchecked((uint)(x9));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13184288) - (__arm64_flags_right_13184288))))) < unchecked((int)0x0UL)) == (((unchecked((int)(__arm64_flags_left_13184288)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13184288)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13184288) - (__arm64_flags_right_13184288))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13184288)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC92D64;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC92D28UL);
        }
        __arm64_flags_left_13184296 = unchecked((uint)(x24));
        __arm64_flags_right_13184296 = unchecked((uint)(x9));
        if ((__arm64_flags_left_13184296 >= __arm64_flags_right_13184296))
        {
            goto label_0xC92DD4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (unchecked((ulong)(unchecked((uint)(x23))))))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC92D60;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(x22);
        x0 = RuntimeCalls.InvokeDirect(0xE49224UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC92D60;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x124UL))))));
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x40UL))))));
        __arm64_flags_left_13184332 = unchecked((uint)(x8));
        __arm64_flags_right_13184332 = unchecked((uint)(x9));
        if ((unchecked((uint)((__arm64_flags_left_13184332) - (__arm64_flags_right_13184332))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC92D78;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x21);
        x23 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x23))) + (unchecked((uint)(0x1UL)))))));
        if ((x8 != 0x0UL))
        {
            goto label_0xC92D10;
        }
        else
        {
            goto label_0xC92D60;
        }
        label_0xC92D60:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC92D64;
        label_0xC92D64:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        label_0xC92D78:
        ;
        x8 = RuntimeMemory.ReadU64(x21);
        if ((x8 == 0x0UL))
        {
            goto label_0xC92D60;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xE8UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC92D60;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_13184396 = unchecked((uint)(x24));
        __arm64_flags_right_13184396 = unchecked((uint)(x9));
        if ((__arm64_flags_left_13184396 >= __arm64_flags_right_13184396))
        {
            goto label_0xC92DD4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (x23))));
        x0 = x20;
        RuntimeMemory.WriteU64(x20, x1);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = RuntimeMemory.ReadU64(x20);
        if ((x0 == 0x0UL))
        {
            goto label_0xC92D60;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(x22);
        x0 = RuntimeCalls.InvokeDirect(0xE49224UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x28UL))), x0);
        x1 = x0;
        x0 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0xB7D8D0UL);
        label_0xC92DD4:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB7CUL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        return default(ulong);
    }
```

## `AmmoPickup.PickUpItem` — RVA `0xc92dd8`

- Lift status: **exact**; input span: 548 bytes; span to next metadata RVA: 548 bytes.
- Metadata signature: `public void PickUpItem() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=80 (informational only).

```csharp
public static ulong AmmoPickup_PickUpItem_RVAc92dd8(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13184544 = default(uint);
        uint __arm64_flags_left_13184564 = default(uint);
        uint __arm64_flags_right_13184544 = default(uint);
        uint __arm64_flags_right_13184564 = default(uint);
        ulong sp = default(ulong);
        RuntimeVector128 v3 = default(RuntimeVector128);
        RuntimeVector128 v4 = default(RuntimeVector128);
        RuntimeVector128 v5 = default(RuntimeVector128);
        RuntimeVector128 v6 = default(RuntimeVector128);
        RuntimeVector128 v7 = default(RuntimeVector128);
        ulong x10 = default(ulong);
        ulong x11 = default(ulong);
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
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x45EUL))))))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC92E10;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x30UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x45EUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC92E10;
        label_0xC92E10:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x28UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC92FF8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x128UL))))));
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x138UL))))));
        __arm64_flags_left_13184544 = unchecked((uint)(x10));
        __arm64_flags_right_13184544 = unchecked((uint)(x9));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13184544) - (__arm64_flags_right_13184544))))) < unchecked((int)0x0UL)) == (((unchecked((int)(__arm64_flags_left_13184544)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13184544)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13184544) - (__arm64_flags_right_13184544))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13184544)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC92F4C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x11 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x60UL))))));
        x21 = 0x1A8C000UL;
        x10 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x11))) + (unchecked((uint)(x10)))))));
        __arm64_flags_left_13184564 = unchecked((uint)(x10));
        __arm64_flags_right_13184564 = unchecked((uint)(x9));
        x9 = unchecked((ulong)((((!((unchecked((uint)((__arm64_flags_left_13184564) - (__arm64_flags_right_13184564))) == unchecked((uint)0x0UL)))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13184564) - (__arm64_flags_right_13184564))))) < unchecked((int)0x0UL)) == (((unchecked((int)(__arm64_flags_left_13184564)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13184564)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13184564) - (__arm64_flags_right_13184564))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13184564)) < unchecked((int)0x0UL)))))) ? unchecked((uint)(x9)) : unchecked((uint)(x10)))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x8) + (0x128UL))), unchecked((uint)(x9)));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xD8UL))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x50UL))));
        x0 = RuntimeMemory.ReadU64(x21);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC92E58;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC92E54UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC92E58;
        label_0xC92E58:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1798274UL /* metadata target: Object.op_Implicit */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC92E9C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x38UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC92FF8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x50UL))));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179D508UL /* metadata target: Transform.get_position */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x43FA0000UL))));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F400000UL)), 0)), 0));
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        v5 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        v6 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        v7 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(x8))), 0)), 0));
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xC8D260UL /* metadata target: PlayAudioAtPos.PlayClipAt */, x0, x1, x2, x3);
        goto label_0xC92E9C;
        label_0xC92E9C:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x28UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC92FF8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x1F6UL))))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC92EF4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x120UL))))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC92EF4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x1F7UL))))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC92EF4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x8) + (0x120UL))), unchecked((byte)(unchecked((uint)(x9)))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x30UL))));
        if ((x20 == 0x0UL))
        {
            goto label_0xC92FF8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x124UL))))));
        x0 = x20;
        x2 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x3 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x4 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xCB2694UL /* metadata target: PlayerWeapons.SelectWeapon */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x1 = x0;
        x0 = x20;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1795D40UL /* metadata target: MonoBehaviour.StartCoroutine */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        goto label_0xC92EF4;
        label_0xC92EF4:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x48UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC92FB4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xC92FFCUL /* metadata target: AmmoPickup.FreePooledObjects */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x20 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x44UL))))));
        if ((unchecked((uint)(x20)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC92FC0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x38UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC92FF8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x30UL))));
        x1 = 0x0UL;
        x8 = RuntimeMemory.ReadU64(x8);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x19 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x1792190UL /* metadata target: Component.get_gameObject */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        if ((x19 == 0x0UL))
        {
            goto label_0xC92FF8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x2 = x0;
        x0 = x19;
        x1 = unchecked((ulong)(unchecked((uint)(x20))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeDirect(0xC931ECUL /* metadata target: AzuObjectPool.RecyclePooledObj */);
        label_0xC92F4C:
        ;
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xD8UL))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x58UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC92F68;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC92F64UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, unchecked((ulong)(unchecked((uint)(x3)))));
        goto label_0xC92F68;
        label_0xC92F68:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1798274UL /* metadata target: Object.op_Implicit */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC92FB4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x38UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC92FF8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x58UL))));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179D508UL /* metadata target: Transform.get_position */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x0 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x8 = unchecked((ulong)(unchecked((uint)(0x43FA0000UL))));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F400000UL)), 0)), 0));
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        v5 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        v6 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        v7 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(x8))), 0)), 0));
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeDirect(0xC8D260UL /* metadata target: PlayAudioAtPos.PlayClipAt */);
        label_0xC92FB4:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return x0;
        label_0xC92FC0:
        ;
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792190UL /* metadata target: Component.get_gameObject */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x8 = RuntimeMemory.ReadU64(x21);
        x19 = x0;
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC92FE4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        goto label_0xC92FE4;
        label_0xC92FE4:
        ;
        x0 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x1 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeDirect(0x1798A20UL /* metadata target: Object.Destroy */);
        label_0xC92FF8:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        return default(ulong);
    }
```

## `AmmoPickup.FreePooledObjects` — RVA `0xc92ffc`

- Lift status: **exact**; input span: 496 bytes; span to next metadata RVA: 496 bytes.
- Metadata signature: `private void FreePooledObjects() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=72 (informational only).

```csharp
public static ulong AmmoPickup_FreePooledObjects_RVAc92ffc(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13185156 = default(uint);
        uint __arm64_flags_left_13185176 = default(uint);
        uint __arm64_flags_left_13185272 = default(uint);
        uint __arm64_flags_left_13185328 = default(uint);
        uint __arm64_flags_left_13185352 = default(uint);
        uint __arm64_flags_left_13185480 = default(uint);
        uint __arm64_flags_right_13185156 = default(uint);
        uint __arm64_flags_right_13185176 = default(uint);
        uint __arm64_flags_right_13185272 = default(uint);
        uint __arm64_flags_right_13185328 = default(uint);
        uint __arm64_flags_right_13185352 = default(uint);
        uint __arm64_flags_right_13185480 = default(uint);
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x22 = default(ulong);
        ulong x23 = default(ulong);
        ulong x24 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFC0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x24);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))), x19);
        x20 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x45FUL))))))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC93054;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x30UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xE30UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x160UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xE48UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x45FUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC93054;
        label_0xC93054:
        ;
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792190UL /* metadata target: Component.get_gameObject */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC931E4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x160UL))));
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x2 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xE49EC4UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC931E4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x18UL))))));
        x20 = x0;
        __arm64_flags_left_13185156 = unchecked((uint)(x8));
        __arm64_flags_right_13185156 = unchecked((uint)0x1UL);
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13185156) - (__arm64_flags_right_13185156))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_13185156)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13185156)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13185156) - (__arm64_flags_right_13185156))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13185156)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC93100;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x23 = 0x1A8E000UL;
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0x30UL))));
        x22 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xC93098;
        label_0xC93098:
        ;
        __arm64_flags_left_13185176 = unchecked((uint)(x22));
        __arm64_flags_right_13185176 = unchecked((uint)(x8));
        if ((__arm64_flags_left_13185176 >= __arm64_flags_right_13185176))
        {
            goto label_0xC931E8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)((x20) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x22))) << (int)(unchecked((int)(unchecked((uint)(0x3UL))))))))))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        if ((x24 == 0x0UL))
        {
            goto label_0xC931E4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x23);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        if ((x0 == 0x0UL))
        {
            goto label_0xC931E4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x24) + (0x48UL))));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792154UL /* metadata target: Component.get_transform */, x0, x1, x2, x3);
        if ((x21 == 0x0UL))
        {
            goto label_0xC931E4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = x0;
        x0 = x21;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179DCB4UL /* metadata target: Transform.set_parent */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x24) + (0x40UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC931E4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794CD0UL /* metadata target: GameObject.SetActive */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x20) + (0x18UL))))));
        x22 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x22))) + (unchecked((uint)(0x1UL)))))));
        __arm64_flags_left_13185272 = unchecked((uint)(x22));
        __arm64_flags_right_13185272 = unchecked((uint)(x8));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13185272) - (__arm64_flags_right_13185272))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_13185272)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13185272)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13185272) - (__arm64_flags_right_13185272))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13185272)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC93098;
        }
        else
        {
            goto label_0xC93100;
        }
        label_0xC93100:
        ;
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792190UL /* metadata target: Component.get_gameObject */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC931E4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xE30UL))));
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x2 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xE49EC4UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC931E4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x18UL))))));
        x19 = x0;
        __arm64_flags_left_13185328 = unchecked((uint)(x8));
        __arm64_flags_right_13185328 = unchecked((uint)0x1UL);
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13185328) - (__arm64_flags_right_13185328))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_13185328)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13185328)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13185328) - (__arm64_flags_right_13185328))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13185328)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC931D0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x22 = 0x1A8D000UL;
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0xE48UL))));
        x21 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x23 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        goto label_0xC93148;
        label_0xC93148:
        ;
        __arm64_flags_left_13185352 = unchecked((uint)(x21));
        __arm64_flags_right_13185352 = unchecked((uint)(x8));
        if ((__arm64_flags_left_13185352 >= __arm64_flags_right_13185352))
        {
            goto label_0xC931E8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)((x19) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x21))) << (int)(unchecked((int)(unchecked((uint)(0x3UL))))))))))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        if ((x20 == 0x0UL))
        {
            goto label_0xC931E4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792154UL /* metadata target: Component.get_transform */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC931E4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179DCB4UL /* metadata target: Transform.set_parent */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x20UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC931E4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17CF2D0UL /* metadata target: Rigidbody.set_isKinematic */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x78UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC931E4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17CF9B8UL /* metadata target: Collider.set_isTrigger */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792190UL /* metadata target: Component.get_gameObject */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC931E4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(x22);
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794D8CUL /* metadata target: GameObject.set_tag */, x0, x1, x2, x3);
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x31UL))), unchecked((byte)(unchecked((uint)(x23)))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x18UL))))));
        x21 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x21))) + (unchecked((uint)(0x1UL)))))));
        __arm64_flags_left_13185480 = unchecked((uint)(x21));
        __arm64_flags_right_13185480 = unchecked((uint)(x8));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13185480) - (__arm64_flags_right_13185480))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_13185480)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13185480)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13185480) - (__arm64_flags_right_13185480))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13185480)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC93148;
        }
        else
        {
            goto label_0xC931D0;
        }
        label_0xC931D0:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        label_0xC931E4:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        goto label_0xC931E8;
        label_0xC931E8:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB7CUL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `AmmoPickup.ctor` — RVA `0xc932fc`

- Lift status: **exact**; input span: 20 bytes; span to next metadata RVA: 20 bytes.
- Metadata signature: `public void .ctor() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=2 (informational only).

```csharp
public static ulong AmmoPickup_ctor_RVAc932fc(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong x8 = default(ulong);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x1 = 0x0UL;
        RuntimeMemory.WriteU8(unchecked((ulong)((x0) + (0x48UL))), unchecked((byte)(unchecked((uint)(x8)))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x0) + (0x60UL))), unchecked((uint)(x8)));
        return RuntimeCalls.InvokeDirect(0x1796274UL /* metadata target: MonoBehaviour.ctor */);
        return default(ulong);
    }
```
