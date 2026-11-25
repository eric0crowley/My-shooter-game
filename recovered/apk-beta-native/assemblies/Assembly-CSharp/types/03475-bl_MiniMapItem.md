# `bl_MiniMapItem` — TypeDefIndex 3475

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x20` | `GameObject` | `GraphicPrefab` |
| `0x28` | `Transform` | `Target` |
| `0x30` | `Vector3` | `OffSet` |
| `0x40` | `Sprite` | `Icon` |
| `0x48` | `Sprite` | `DeathIcon` |
| `0x50` | `Color` | `IconColor` |
| `0x60` | `float` | `Size` |
| `0x64` | `bool` | `ShowCircleArea` |
| `0x68` | `float` | `CircleAreaRadius` |
| `0x6C` | `Color` | `CircleAreaColor` |
| `0x7C` | `bool` | `isInteractable` |
| `0x80` | `string` | `InfoItem` |
| `0x88` | `bool` | `OffScreen` |
| `0x8C` | `float` | `BorderOffScreen` |
| `0x90` | `float` | `OffScreenSize` |
| `0x94` | `float` | `RenderDelay` |
| `0x98` | `ItemEffect` | `m_Effect` |
| `0xA0` | `Image` | `Graphic` |
| `0xA8` | `RectTransform` | `RectRoot` |
| `0xB0` | `GameObject` | `cacheItem` |
| `0xB8` | `RectTransform` | `CircleAreaRect` |
| `0xC0` | `Vector3` | `position` |
| `0xD0` | `bl_MiniMap` | `MiniMap` |
| `0xD8` | `bl_MiniMap` | `_minimap` |

## `bl_MiniMapItem.Start` — RVA `0xcc8b68`

- Lift status: **exact**; input span: 248 bytes; span to next metadata RVA: 248 bytes.
- Metadata signature: `private void Start() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=42 (informational only).

```csharp
public static ulong bl_MiniMapItem_Start_RVAcc8b68(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
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
        x21 = 0x1A8E000UL;
        x20 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x22) + (0x561UL))))))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xA08UL))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xD8UL))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCC8BCC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x398UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xAD0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xA08UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x22) + (0x561UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCC8BCC;
        label_0xCC8BCC:
        ;
        x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x0 = RuntimeCalls.InvokeDirect(0xCC6020UL /* metadata target: bl_MiniMapUtils.GetMiniMap */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        x1 = unchecked((ulong)(unchecked((uint)(x0))));
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0xD0UL))), x1);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x21);
        x0 = RuntimeMemory.ReadU64(x20);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x10UL))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCC8C00;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCC8BFCUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCC8C00;
        label_0xCC8C00:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794AC8UL /* metadata target: Object.op_Inequality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCC8C28;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0xCC8C60UL /* metadata target: bl_MiniMapItem.CreateIcon */);
        label_0xCC8C28:
        ;
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x398UL))));
        x19 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(x8);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xAD0UL))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCC8C48;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCC8C44UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCC8C48;
        label_0xCC8C48:
        ;
        x0 = RuntimeMemory.ReadU64(x19);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x1 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0x1770B68UL /* metadata target: Debug.Log */);
        return default(ulong);
    }
```

## `bl_MiniMapItem.CreateIcon` — RVA `0xcc8c60`

- Lift status: **exact**; input span: 712 bytes; span to next metadata RVA: 712 bytes.
- Metadata signature: `private void CreateIcon() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=110 (informational only).

```csharp
public static ulong bl_MiniMapItem_CreateIcon_RVAcc8c60(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_pair_address_13405596 = default(ulong);
        ulong __arm64_pair_address_13405600 = default(ulong);
        ulong __arm64_pair_address_13405768 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
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
        x20 = 0x1BAB000UL;
        x23 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x562UL))))))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0xD8UL))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCC8CE0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xBB0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xA18UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x160UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xBF8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xAD8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x9E0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x562UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCC8CE0;
        label_0xCC8CE0:
        ;
        x0 = RuntimeMemory.ReadU64(x23);
        x21 = 0x1A8D000UL;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x20UL))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x9E0UL))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCC8CFC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCC8CF8UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCC8CFC;
        label_0xCC8CFC:
        ;
        x1 = RuntimeMemory.ReadU64(x21);
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xD29F50UL, x0, x1, x2, x3);
        x20 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x20) + (0xB0UL))), x0);
        x1 = x0;
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x0 = RuntimeCalls.InvokeDirect(0xCC6020UL /* metadata target: bl_MiniMapUtils.GetMiniMap */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        if ((unchecked((uint)(x0)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCC8F24;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)(unchecked((uint)(x0))))) + (0x178UL))));
        x22 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x22) + (0xA8UL))), x1);
        x0 = x22;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCC8F24;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xBF8UL))));
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xE49224UL, x0, x1, x2, x3);
        x21 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x21) + (0xA0UL))), x0);
        x1 = x0;
        x0 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xFFFFFFFFFFFFFFA0UL))));
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794AC8UL /* metadata target: Object.op_Inequality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCC8DB0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(x21);
        if ((x0 == 0x0UL))
        {
            goto label_0xCC8F24;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x40UL))));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1813790UL /* metadata target: Image.set_sprite */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xA0UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCC8F24;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x0);
        __arm64_pair_address_13405596 = unchecked((ulong)((x19) + (0x58UL)));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13405596)), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13405596) + (0x4UL))))), 0));
        __arm64_pair_address_13405600 = unchecked((ulong)((x19) + (0x50UL)));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13405600)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13405600) + (0x4UL))))), 0));
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x2A8UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x2B0UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        goto label_0xCC8DB0;
        label_0xCC8DB0:
        ;
        x0 = RuntimeMemory.ReadU64(x20);
        if ((x0 == 0x0UL))
        {
            goto label_0xCC8F24;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794C14UL /* metadata target: GameObject.get_transform */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x22);
        if ((x8 == 0x0UL))
        {
            goto label_0xCC8F24;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x22 = x0;
        x0 = x8;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792154UL /* metadata target: Component.get_transform */, x0, x1, x2, x3);
        if ((x22 == 0x0UL))
        {
            goto label_0xCC8F24;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = x0;
        x0 = x22;
        x2 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x3 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179DE4CUL /* metadata target: Transform.SetParent */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = RuntimeMemory.ReadU64(x21);
        if ((x0 == 0x0UL))
        {
            goto label_0xCC8F24;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xBB0UL))));
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xE31BC8UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x22 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x22) + (0x1E0UL))))))));
        x21 = x0;
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCC8E2C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x138UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x22) + (0x1E0UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCC8E2C;
        label_0xCC8E2C:
        ;
        if ((x21 == 0x0UL))
        {
            goto label_0xCC8F24;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x138UL))));
        x0 = x21;
        x1 = 0x0UL;
        x8 = RuntimeMemory.ReadU64(x8);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        __arm64_pair_address_13405768 = x8;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13405768)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13405768) + (0x4UL))))), 0));
        x0 = RuntimeCalls.InvokeDirect(0x179C820UL /* metadata target: RectTransform.set_anchoredPosition */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = RuntimeMemory.ReadU64(x20);
        if ((x0 == 0x0UL))
        {
            goto label_0xCC8F24;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x160UL))));
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xE49224UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCC8F24;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x7CUL))))))));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x196DE5CUL /* metadata target: CanvasGroup.set_interactable */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x20 = x19;
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x28UL))));
        x0 = RuntimeMemory.ReadU64(x23);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCC8E90;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCC8E8CUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xCC8E90;
        label_0xCC8E90:
        ;
        x0 = x21;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179568CUL /* metadata target: Object.op_Equality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCC8EC8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xA18UL))));
        x0 = x19;
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xE31BC8UL, x0, x1, x2, x3);
        x1 = x0;
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x28UL))), x0);
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        goto label_0xCC8EC8;
        label_0xCC8EC8:
        ;
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xCC8F28UL /* metadata target: bl_MiniMapItem.StartEffect */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xB0UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCC8F24;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xAD8UL))));
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xE49224UL, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCC8F24;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCC8EECUL);
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x94UL))))), 0));
        x20 = x0;
        RuntimeMemory.WriteF32(unchecked((ulong)((x0) + (0x58UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        x0 = RuntimeCalls.InvokeDirect(0xCC6104UL /* metadata target: bl_IconItem.FadeIcon */, x0, x1, x2, x3);
        x1 = x0;
        x0 = x20;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1795D40UL /* metadata target: MonoBehaviour.StartCoroutine */, x0, x1, x2, x3);
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x80UL))));
        x0 = x20;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeDirect(0xCC5D8CUL /* metadata target: bl_IconItem.GetInfoItem */);
        label_0xCC8F24:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `bl_MiniMapItem.StartEffect` — RVA `0xcc8f28`

- Lift status: **exact**; input span: 160 bytes; span to next metadata RVA: 160 bytes.
- Metadata signature: `private void StartEffect() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=23 (informational only).

```csharp
public static ulong bl_MiniMapItem_StartEffect_RVAcc8f28(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13406076 = default(uint);
        uint __arm64_flags_right_13406076 = default(uint);
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        x20 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x564UL))))))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCC8F60;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x178UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xAE0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x564UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCC8F60;
        label_0xCC8F60:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xA0UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCC8FC4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x178UL))));
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xE31BC8UL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x98UL))))));
        __arm64_flags_left_13406076 = unchecked((uint)(x8));
        __arm64_flags_right_13406076 = unchecked((uint)0x1UL);
        if ((unchecked((uint)((__arm64_flags_left_13406076) - (__arm64_flags_right_13406076))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCC8F94;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCC8F84UL);
        }
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCC8FB8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCC8F88UL);
        }
        if ((x0 == 0x0UL))
        {
            goto label_0xCC8FC4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x2 = unchecked((ulong)(unchecked((uint)(0x2UL))));
        goto label_0xCC8F9C;
        label_0xCC8F94:
        ;
        if ((x0 == 0x0UL))
        {
            goto label_0xCC8FC4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x2 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        goto label_0xCC8F9C;
        label_0xCC8F9C:
        ;
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xAE0UL))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x3 = 0x0UL;
        x1 = RuntimeMemory.ReadU64(x8);
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0x1767734UL /* metadata target: Animator.SetInteger */);
        label_0xCC8FB8:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        label_0xCC8FC4:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        return default(ulong);
    }
```

## `bl_MiniMapItem.Update` — RVA `0xcc8fc8`

- Lift status: **partial**; input span: 1848 bytes; span to next metadata RVA: 1848 bytes.
- Metadata signature: `private void Update() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=191 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'fdiv' at 0xcc9364; reason: Unsupported instruction 'fmul' at 0xcc9464; reason: Unsupported instruction 'fmul' at 0xcc946c; reason: Unsupported instruction 'ld1' at 0xcc94b8; reason: Unsupported instruction 'fmul' at 0xcc94c4; reason: Unsupported instruction 'fadd' at 0xcc94c8

```csharp
public static ulong bl_MiniMapItem_Update_RVAcc8fc8(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        float __arm64_float_flags_left_13406664 = default(float);
        float __arm64_float_flags_left_13406672 = default(float);
        float __arm64_float_flags_left_13406752 = default(float);
        float __arm64_float_flags_left_13406760 = default(float);
        float __arm64_float_flags_left_13407060 = default(float);
        float __arm64_float_flags_left_13407120 = default(float);
        float __arm64_float_flags_left_13407164 = default(float);
        float __arm64_float_flags_left_13407208 = default(float);
        float __arm64_float_flags_left_13407256 = default(float);
        float __arm64_float_flags_left_13407356 = default(float);
        float __arm64_float_flags_left_13407596 = default(float);
        float __arm64_float_flags_right_13406664 = default(float);
        float __arm64_float_flags_right_13406672 = default(float);
        float __arm64_float_flags_right_13406752 = default(float);
        float __arm64_float_flags_right_13406760 = default(float);
        float __arm64_float_flags_right_13407060 = default(float);
        float __arm64_float_flags_right_13407120 = default(float);
        float __arm64_float_flags_right_13407164 = default(float);
        float __arm64_float_flags_right_13407208 = default(float);
        float __arm64_float_flags_right_13407256 = default(float);
        float __arm64_float_flags_right_13407356 = default(float);
        float __arm64_float_flags_right_13407596 = default(float);
        float __arm64_fp_left_13407592 = default(float);
        float __arm64_fp_right_13407592 = default(float);
        ulong __arm64_pair_address_13406156 = default(ulong);
        ulong __arm64_pair_address_13406160 = default(ulong);
        ulong __arm64_pair_address_13406164 = default(ulong);
        ulong __arm64_pair_address_13406168 = default(ulong);
        ulong __arm64_pair_address_13406352 = default(ulong);
        ulong __arm64_pair_address_13406356 = default(ulong);
        ulong __arm64_pair_address_13406360 = default(ulong);
        ulong __arm64_pair_address_13406364 = default(ulong);
        ulong __arm64_pair_address_13406436 = default(ulong);
        ulong __arm64_pair_address_13406580 = default(ulong);
        ulong __arm64_pair_address_13406976 = default(ulong);
        ulong __arm64_pair_address_13406984 = default(ulong);
        ulong __arm64_pair_address_13407016 = default(ulong);
        ulong __arm64_pair_address_13407024 = default(ulong);
        ulong __arm64_pair_address_13407448 = default(ulong);
        ulong __arm64_pair_address_13407716 = default(ulong);
        ulong __arm64_pair_address_13407760 = default(ulong);
        ulong __arm64_pair_address_13407764 = default(ulong);
        ulong __arm64_pair_address_13407768 = default(ulong);
        ulong __arm64_pair_address_13407772 = default(ulong);
        ulong __arm64_pair_address_13407872 = default(ulong);
        ulong __arm64_pair_address_13407968 = default(ulong);
        ulong __arm64_pair_address_13407972 = default(ulong);
        ulong __arm64_pair_address_13407976 = default(ulong);
        ulong __arm64_pair_address_13407980 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v10 = default(RuntimeVector128);
        RuntimeVector128 v11 = default(RuntimeVector128);
        RuntimeVector128 v12 = default(RuntimeVector128);
        RuntimeVector128 v13 = default(RuntimeVector128);
        RuntimeVector128 v14 = default(RuntimeVector128);
        RuntimeVector128 v15 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
        RuntimeVector128 v4 = default(RuntimeVector128);
        RuntimeVector128 v5 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        RuntimeVector128 v9 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x22 = default(ulong);
        ulong x23 = default(ulong);
        ulong x24 = default(ulong);
        ulong x25 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        sp = unchecked((ulong)((sp) - (0xB0UL)));
        __arm64_pair_address_13406156 = unchecked((ulong)((sp) + (0x30UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13406156, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v15.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13406156) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v14.GetUInt64(0)))));
        __arm64_pair_address_13406160 = unchecked((ulong)((sp) + (0x40UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13406160, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v13.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13406160) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v12.GetUInt64(0)))));
        __arm64_pair_address_13406164 = unchecked((ulong)((sp) + (0x50UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13406164, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v11.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13406164) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v10.GetUInt64(0)))));
        __arm64_pair_address_13406168 = unchecked((ulong)((sp) + (0x60UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13406168, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13406168) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x70UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x70UL)))) + (0x8UL))), x25);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x80UL)))) + (0x0UL))), x24);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x80UL)))) + (0x8UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x90UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x90UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xA0UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xA0UL)))) + (0x8UL))), x19);
        x20 = 0x1BAB000UL;
        x21 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x563UL))))))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xD8UL))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCC9030;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xBB0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xA08UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x563UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCC9030;
        label_0xCC9030:
        ;
        x0 = RuntimeMemory.ReadU64(x21);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x28UL))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCC9044;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCC9040UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCC9044;
        label_0xCC9044:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179568CUL /* metadata target: Object.op_Equality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCC9080;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(x21);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xA0UL))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCC906C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCC9068UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCC906C;
        label_0xCC906C:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179568CUL /* metadata target: Object.op_Equality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCC90A8;
        }
        else
        {
            goto label_0xCC9080;
        }
        label_0xCC9080:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0xA0UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xA0UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x90UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x90UL)))) + (0x8UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x80UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x80UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x70UL))));
        x25 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x70UL)))) + (0x8UL))));
        __arm64_pair_address_13406352 = unchecked((ulong)((sp) + (0x60UL)));
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13406352)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13406352) + (0x8UL))))), 0));
        __arm64_pair_address_13406356 = unchecked((ulong)((sp) + (0x50UL)));
        v11 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13406356)), 0));
        v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13406356) + (0x8UL))))), 0));
        __arm64_pair_address_13406360 = unchecked((ulong)((sp) + (0x40UL)));
        v13 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13406360)), 0));
        v12 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13406360) + (0x8UL))))), 0));
        __arm64_pair_address_13406364 = unchecked((ulong)((sp) + (0x30UL)));
        v15 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13406364)), 0));
        v14 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13406364) + (0x8UL))))), 0));
        sp = unchecked((ulong)((sp) + (0xB0UL)));
        return x0;
        label_0xCC90A8:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xA0UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCC96FC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xBB0UL))));
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xE31BC8UL, x0, x1, x2, x3);
        x20 = x0;
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xCC9700UL /* metadata target: bl_MiniMapItem.get_TargetPosition */, x0, x1, x2, x3);
        x23 = 0x1A8E000UL;
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0xA08UL))));
        x8 = RuntimeMemory.ReadU64(x23);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCC96FC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCC90E4UL);
        }
        __arm64_pair_address_13406436 = unchecked((ulong)((x19) + (0x34UL)));
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13406436)), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13406436) + (0x4UL))))), 0));
        v5 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x30UL))))), 0));
        x1 = 0x0UL;
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v5.GetUInt64(0)))), 0))))), 0));
        x0 = RuntimeCalls.InvokeDirect(0x176F6C0UL /* metadata target: Camera.WorldToViewportPoint */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xA8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCC96FC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        v9 = v0;
        v8 = v1;
        x0 = RuntimeCalls.InvokeDirect(0x179C8ACUL /* metadata target: RectTransform.get_sizeDelta */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xA8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCC96FC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        v10 = v0;
        x0 = RuntimeCalls.InvokeDirect(0x179C8ACUL /* metadata target: RectTransform.get_sizeDelta */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xA8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCC96FC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        v11 = v0;
        x0 = RuntimeCalls.InvokeDirect(0x179C8ACUL /* metadata target: RectTransform.get_sizeDelta */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xA8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCC96FC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        v12 = v1;
        x0 = RuntimeCalls.InvokeDirect(0x179C8ACUL /* metadata target: RectTransform.get_sizeDelta */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x88UL))))))));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F000000UL)), 0)), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0))))), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v12.GetUInt64(0)))), 0))))), 0));
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0))))), 0));
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        __arm64_pair_address_13406580 = unchecked((ulong)((x19) + (0xC0UL)));
        RuntimeMemory.WriteF32(__arm64_pair_address_13406580, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_13406580) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0));
        RuntimeMemory.WritePtr(unchecked((ulong)((x19) + (0xC8UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCC9234;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xA8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCC96FC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179C8ACUL /* metadata target: RectTransform.get_sizeDelta */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xA8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCC96FC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCC9198UL);
        }
        v11 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x8CUL))))), 0));
        x1 = 0x0UL;
        v10 = v0;
        x0 = RuntimeCalls.InvokeDirect(0x179C8ACUL /* metadata target: RectTransform.get_sizeDelta */, x0, x1, x2, x3);
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x8CUL))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F000000UL)), 0)), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xA8UL))));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes((-(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0)))), 0));
        __arm64_float_flags_left_13406664 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13406664 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_13406664 > __arm64_float_flags_right_13406664) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0))), 0));
        __arm64_float_flags_left_13406672 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13406672 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes((((__arm64_float_flags_left_13406672 >= __arm64_float_flags_right_13406672) || ((__arm64_float_flags_left_13406672 != __arm64_float_flags_left_13406672) || (__arm64_float_flags_right_13406672 != __arm64_float_flags_right_13406672))) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((x19) + (0xC0UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        if ((x0 == 0x0UL))
        {
            goto label_0xCC96FC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCC91E0UL);
        }
        v11 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0xC4UL))))), 0));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179C8ACUL /* metadata target: RectTransform.get_sizeDelta */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xA8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCC96FC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCC91F4UL);
        }
        v12 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x8CUL))))), 0));
        x1 = 0x0UL;
        v10 = v1;
        x0 = RuntimeCalls.InvokeDirect(0x179C8ACUL /* metadata target: RectTransform.get_sizeDelta */, x0, x1, x2, x3);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x8CUL))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F000000UL)), 0)), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v12.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes((-(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0)))), 0));
        __arm64_float_flags_left_13406752 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13406752 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_13406752 > __arm64_float_flags_right_13406752) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0))), 0));
        __arm64_float_flags_left_13406760 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13406760 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes((((__arm64_float_flags_left_13406760 >= __arm64_float_flags_right_13406760) || ((__arm64_float_flags_left_13406760 != __arm64_float_flags_left_13406760) || (__arm64_float_flags_right_13406760 != __arm64_float_flags_right_13406760))) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((x19) + (0xC4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        goto label_0xCC9234;
        label_0xCC9234:
        ;
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xCC97DCUL /* metadata target: bl_MiniMapItem.get_m_miniMap */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCC96FC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x6CUL))))))));
        x22 = unchecked((ulong)((x19) + (0x60UL)));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCC936C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x24 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x24) + (0x2C9UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCC926C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x1E8UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x24) + (0x2C9UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCC926C;
        label_0xCC926C:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x28UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCC96FC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x25 = 0x1A8C000UL;
        x25 = RuntimeMemory.ReadU64(unchecked((ulong)((x25) + (0x1E8UL))));
        x1 = 0x0UL;
        x8 = RuntimeMemory.ReadU64(x25);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x8UL))))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((sp) + (0x2CUL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        x0 = RuntimeCalls.InvokeDirect(0x179D508UL /* metadata target: Transform.get_position */, x0, x1, x2, x3);
        x0 = x19;
        v10 = v0;
        v11 = v1;
        v12 = v2;
        x0 = RuntimeCalls.InvokeDirect(0xCC97DCUL /* metadata target: bl_MiniMapItem.get_m_miniMap */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCC96FC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCC92ACUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xCC7830UL /* metadata target: bl_MiniMap.get_TargetPosition */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x23);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCC96FC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        v13 = v0;
        v14 = v1;
        v15 = v2;
        x0 = RuntimeCalls.InvokeDirect(0x1792154UL /* metadata target: Component.get_transform */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCC96FC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCC92D8UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v13.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v14.GetUInt64(0)))), 0))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v12.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v15.GetUInt64(0)))), 0))))), 0));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179E7C8UL /* metadata target: Transform.InverseTransformDirection */, x0, x1, x2, x3);
        x23 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x23) + (0x2C8UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCC9314;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xA60UL))));
        __arm64_pair_address_13406976 = sp;
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13406976, v1);
#else
        __WriteVector128(__arm64_pair_address_13406976, v1);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13406976) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13406976) + (0x10UL))), v0);
#endif
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        __arm64_pair_address_13406984 = sp;
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(__arm64_pair_address_13406984);
#else
        v1 = __ReadVector128(__arm64_pair_address_13406984);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13406984) + (0x10UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13406984) + (0x10UL))));
#endif
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x23) + (0x2C8UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCC9314;
        label_0xCC9314:
        ;
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xA60UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCC9334;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCC9328UL);
        }
        __arm64_pair_address_13407016 = sp;
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13407016, v1);
#else
        __WriteVector128(__arm64_pair_address_13407016, v1);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13407016) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13407016) + (0x10UL))), v0);
#endif
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        __arm64_pair_address_13407024 = sp;
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(__arm64_pair_address_13407024);
#else
        v1 = __ReadVector128(__arm64_pair_address_13407024);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13407024) + (0x10UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13407024) + (0x10UL))));
#endif
        goto label_0xCC9334;
        label_0xCC9334:
        ;
        x8 = 0x432000UL;
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x41CUL))))), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)(global::System.Math.Sqrt(unchecked((double)(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))))), 0));
        __arm64_float_flags_left_13407060 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13407060 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_13407060 <= __arm64_float_flags_right_13407060) || ((__arm64_float_flags_left_13407060 != __arm64_float_flags_left_13407060) || (__arm64_float_flags_right_13407060 != __arm64_float_flags_right_13407060))))
        {
            goto label_0xCC9424;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        v0 = v1;
        v1 = (RuntimeVector128.Zero.WithUInt32(0, v2.GetUInt32(0)) | RuntimeVector128.Zero.WithUInt32(0, v2.GetUInt32(0)).ShiftLeftLogical(unchecked((int)0x20UL)));
        RuntimeCalls.Unsupported("fdiv", 0xCC9364UL);
        goto label_0xCC944C;
        label_0xCC936C:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xA8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCC96FC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCC9374UL);
        }
        v10 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0xC0UL))))), 0));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179C8ACUL /* metadata target: RectTransform.get_sizeDelta */, x0, x1, x2, x3);
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x8CUL))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F000000UL)), 0)), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        __arm64_float_flags_left_13407120 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13407120 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        if ((__arm64_float_flags_left_13407120 == __arm64_float_flags_right_13407120))
        {
            goto label_0xCC94D0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xA8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCC96FC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCC93A0UL);
        }
        v10 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0xC4UL))))), 0));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179C8ACUL /* metadata target: RectTransform.get_sizeDelta */, x0, x1, x2, x3);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x8CUL))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F000000UL)), 0)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        __arm64_float_flags_left_13407164 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13407164 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        if ((__arm64_float_flags_left_13407164 == __arm64_float_flags_right_13407164))
        {
            goto label_0xCC94D0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xA8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCC96FC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCC93CCUL);
        }
        v10 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0xC0UL))))), 0));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179C8ACUL /* metadata target: RectTransform.get_sizeDelta */, x0, x1, x2, x3);
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x8CUL))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0xBF000000UL)), 0)), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        __arm64_float_flags_left_13407208 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13407208 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        if ((__arm64_float_flags_left_13407208 == __arm64_float_flags_right_13407208))
        {
            goto label_0xCC94D0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xA8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCC96FC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCC93F8UL);
        }
        v10 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0xC4UL))))), 0));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179C8ACUL /* metadata target: RectTransform.get_sizeDelta */, x0, x1, x2, x3);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x8CUL))))), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F000000UL)), 0)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes((-(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0)))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        __arm64_float_flags_left_13407256 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13407256 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0);
        if ((__arm64_float_flags_left_13407256 == __arm64_float_flags_right_13407256))
        {
            goto label_0xCC94D0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCC9420UL);
        }
        goto label_0xCC94D4;
        label_0xCC9424:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x24) + (0x2C9UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCC9440;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x1E8UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x24) + (0x2C9UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCC9440;
        label_0xCC9440:
        ;
        x8 = RuntimeMemory.ReadU64(x25);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(x8)), 0));
        goto label_0xCC944C;
        label_0xCC944C:
        ;
        v11 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0xC0UL))))), 0));
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xCC97DCUL /* metadata target: bl_MiniMapItem.get_m_miniMap */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCC96FC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCC945CUL);
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x0) + (0x70UL))))), 0));
        v1 = (RuntimeVector128.Zero.WithUInt32(0, unchecked((uint)((unchecked((uint)0x3FUL)) << (int)(unchecked((int)(unchecked((uint)0x18UL))))))) | RuntimeVector128.Zero.WithUInt32(0, unchecked((uint)((unchecked((uint)0x3FUL)) << (int)(unchecked((int)(unchecked((uint)0x18UL))))))).ShiftLeftLogical(unchecked((int)0x20UL)));
        RuntimeCalls.Unsupported("fmul", 0xCC9464UL);
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F000000UL)), 0)), 0));
        RuntimeCalls.Unsupported("fmul", 0xCC946CUL);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)((global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0)), 0)) & (unchecked((uint)0x7FFFFFFFUL))))), 0)), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)((global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)), 0)) & (unchecked((uint)0x7FFFFFFFUL))))), 0)), 0));
        __arm64_float_flags_left_13407356 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13407356 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_13407356 < __arm64_float_flags_right_13407356) || ((__arm64_float_flags_left_13407356 != __arm64_float_flags_left_13407356) || (__arm64_float_flags_right_13407356 != __arm64_float_flags_right_13407356))))
        {
            goto label_0xCC94D4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x19;
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x10UL))), v3);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x10UL))), v3);
#endif
        x0 = RuntimeCalls.InvokeDirect(0xCC97DCUL /* metadata target: bl_MiniMapItem.get_m_miniMap */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCC96FC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCC9494UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x0) + (0x70UL))))), 0));
        x0 = x19;
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(sp, v0);
#else
        __WriteVector128(sp, v0);
#endif
        x0 = RuntimeCalls.InvokeDirect(0xCC97DCUL /* metadata target: bl_MiniMapItem.get_m_miniMap */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCC96FC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCC94A8UL);
        }
#if IL2CPPREC_RUNTIME_VECTOR128
        v2 = RuntimeMemory.ReadVector128(sp);
#else
        v2 = __ReadVector128(sp);
#endif
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((sp) + (0x2CUL))))), 0));
        x8 = unchecked((ulong)((x0) + (0x70UL)));
        v0 = (RuntimeVector128.Zero.WithUInt32(0, unchecked((uint)((unchecked((uint)0x3FUL)) << (int)(unchecked((int)(unchecked((uint)0x18UL))))))) | RuntimeVector128.Zero.WithUInt32(0, unchecked((uint)((unchecked((uint)0x3FUL)) << (int)(unchecked((int)(unchecked((uint)0x18UL))))))).ShiftLeftLogical(unchecked((int)0x20UL)));
        RuntimeCalls.Unsupported("ld1", 0xCC94B8UL);
        RuntimeMemory.WriteF32(unchecked((ulong)((x19) + (0xC8UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0));
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x10UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((sp) + (0x10UL))));
#endif
        RuntimeCalls.Unsupported("fmul", 0xCC94C4UL);
        RuntimeCalls.Unsupported("fadd", 0xCC94C8UL);
        RuntimeMemory.WriteF64(unchecked((ulong)((x19) + (0xC0UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))));
        goto label_0xCC94D0;
        label_0xCC94D0:
        ;
        x22 = unchecked((ulong)((x19) + (0x90UL)));
        goto label_0xCC94D4;
        label_0xCC94D4:
        ;
        if ((x20 == 0x0UL))
        {
            goto label_0xCC96FC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCC94D8UL);
        }
        __arm64_pair_address_13407448 = unchecked((ulong)((x19) + (0xC0UL)));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13407448)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13407448) + (0x4UL))))), 0));
        v10 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(x22)), 0));
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179C820UL /* metadata target: RectTransform.set_anchoredPosition */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x21);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xB8UL))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCC9500;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCC94FCUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCC9500;
        label_0xCC9500:
        ;
        x0 = x21;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794AC8UL /* metadata target: Object.op_Inequality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCC952C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xB8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCC96FC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        v0 = v9;
        v1 = v8;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179C820UL /* metadata target: RectTransform.set_anchoredPosition */, x0, x1, x2, x3);
        goto label_0xCC952C;
        label_0xCC952C:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xD0UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCC96FC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCC9534UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x4CUL))))), 0));
        x0 = x20;
        x1 = 0x0UL;
        v10 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        x0 = RuntimeCalls.InvokeDirect(0x179C8ACUL /* metadata target: RectTransform.get_sizeDelta */, x0, x1, x2, x3);
        x0 = 0x0UL;
        v8 = v0;
        v9 = v1;
        x0 = RuntimeCalls.InvokeDirect(0x1789B60UL /* metadata target: Time.get_deltaTime */, x0, x1, x2, x3);
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x41000000UL)), 0)), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        __arm64_fp_left_13407592 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_fp_right_13407592 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0);
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_fp_left_13407592 != __arm64_fp_left_13407592) ? __arm64_fp_left_13407592 : ((__arm64_fp_right_13407592 != __arm64_fp_right_13407592) ? __arm64_fp_right_13407592 : (((__arm64_fp_left_13407592 == global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)) && (__arm64_fp_right_13407592 == global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0))) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)((global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(__arm64_fp_left_13407592), 0)) | (global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(__arm64_fp_right_13407592), 0))))), 0) : ((__arm64_fp_left_13407592 <= __arm64_fp_right_13407592) ? __arm64_fp_left_13407592 : __arm64_fp_right_13407592))))), 0));
        __arm64_float_flags_left_13407596 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13407596 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0))))), 0));
        v5 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes((((__arm64_float_flags_left_13407596 >= __arm64_float_flags_right_13407596) || ((__arm64_float_flags_left_13407596 != __arm64_float_flags_left_13407596) || (__arm64_float_flags_right_13407596 != __arm64_float_flags_right_13407596))) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v5.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179C93CUL /* metadata target: RectTransform.set_sizeDelta */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xD0UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCC96FC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x74UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCC962C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x21 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x2CBUL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCC95C8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD88UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x2CBUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCC95C8;
        label_0xCC95C8:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x28UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCC96FC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xD88UL))));
        x1 = 0x0UL;
        x8 = RuntimeMemory.ReadU64(x8);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        __arm64_pair_address_13407716 = unchecked((ulong)((x8) + (0x8UL)));
        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13407716)), 0));
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13407716) + (0x4UL))))), 0));
        v10 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x4UL))))), 0));
        x0 = RuntimeCalls.InvokeDirect(0x179D6F0UL /* metadata target: Transform.get_rotation */, x0, x1, x2, x3);
        x0 = x20;
        v1 = v10;
        v2 = v9;
        v3 = v8;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0xA0UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xA0UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x90UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x90UL)))) + (0x8UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x80UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x80UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x70UL))));
        x25 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x70UL)))) + (0x8UL))));
        __arm64_pair_address_13407760 = unchecked((ulong)((sp) + (0x60UL)));
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13407760)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13407760) + (0x8UL))))), 0));
        __arm64_pair_address_13407764 = unchecked((ulong)((sp) + (0x50UL)));
        v11 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13407764)), 0));
        v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13407764) + (0x8UL))))), 0));
        __arm64_pair_address_13407768 = unchecked((ulong)((sp) + (0x40UL)));
        v13 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13407768)), 0));
        v12 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13407768) + (0x8UL))))), 0));
        __arm64_pair_address_13407772 = unchecked((ulong)((sp) + (0x30UL)));
        v15 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13407772)), 0));
        v14 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13407772) + (0x8UL))))), 0));
        x1 = 0x0UL;
        sp = unchecked((ulong)((sp) + (0xB0UL)));
        return RuntimeCalls.InvokeDirect(0x179D874UL /* metadata target: Transform.set_localRotation */);
        label_0xCC962C:
        ;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792154UL /* metadata target: Component.get_transform */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCC96FC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179D6C8UL /* metadata target: Transform.get_eulerAngles */, x0, x1, x2, x3);
        x21 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x2C9UL))))))));
        v8 = v1;
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCC9664;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x1E8UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x2C9UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCC9664;
        label_0xCC9664:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x28UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCC96FC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x1E8UL))));
        x1 = 0x0UL;
        x8 = RuntimeMemory.ReadU64(x8);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        __arm64_pair_address_13407872 = x8;
        v10 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13407872)), 0));
        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13407872) + (0x4UL))))), 0));
        x0 = RuntimeCalls.InvokeDirect(0x179D6F0UL /* metadata target: Transform.get_rotation */, x0, x1, x2, x3);
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x178B1C4UL /* metadata target: Quaternion.Internal_ToEulerRad */, x0, x1, x2, x3);
        x8 = 0x432000UL;
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x554UL))))), 0));
        x0 = 0x0UL;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0))))), 0));
        x0 = RuntimeCalls.InvokeDirect(0x178B63CUL /* metadata target: Quaternion.Internal_MakePositive */, x0, x1, x2, x3);
        x8 = 0x432000UL;
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x3E4UL))))), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        x0 = 0x0UL;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
        x0 = RuntimeCalls.InvokeDirect(0x178B12CUL /* metadata target: Quaternion.Internal_FromEulerRad */, x0, x1, x2, x3);
        x0 = x20;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0xA0UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xA0UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x90UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x90UL)))) + (0x8UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x80UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x80UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x70UL))));
        x25 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x70UL)))) + (0x8UL))));
        __arm64_pair_address_13407968 = unchecked((ulong)((sp) + (0x60UL)));
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13407968)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13407968) + (0x8UL))))), 0));
        __arm64_pair_address_13407972 = unchecked((ulong)((sp) + (0x50UL)));
        v11 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13407972)), 0));
        v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13407972) + (0x8UL))))), 0));
        __arm64_pair_address_13407976 = unchecked((ulong)((sp) + (0x40UL)));
        v13 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13407976)), 0));
        v12 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13407976) + (0x8UL))))), 0));
        __arm64_pair_address_13407980 = unchecked((ulong)((sp) + (0x30UL)));
        v15 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13407980)), 0));
        v14 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13407980) + (0x8UL))))), 0));
        x1 = 0x0UL;
        sp = unchecked((ulong)((sp) + (0xB0UL)));
        return RuntimeCalls.InvokeDirect(0x179D774UL /* metadata target: Transform.set_rotation */);
        label_0xCC96FC:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `bl_MiniMapItem.get_TargetPosition` — RVA `0xcc9700`

- Lift status: **exact**; input span: 220 bytes; span to next metadata RVA: 220 bytes.
- Metadata signature: `public Vector3 get_TargetPosition() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=32 (informational only).

```csharp
public static ulong bl_MiniMapItem_get_TargetPosition_RVAcc9700(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_load_address_13408208 = default(ulong);
        ulong __arm64_pair_address_13408144 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteF64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFD0UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        sp = unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFD0UL)));
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x19);
        x21 = 0x1BAB000UL;
        x20 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x56BUL))))))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xD8UL))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCC9738;
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
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x56BUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCC9738;
        label_0xCC9738:
        ;
        x0 = RuntimeMemory.ReadU64(x20);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x28UL))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCC974C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCC9748UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCC974C;
        label_0xCC974C:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179568CUL /* metadata target: Object.op_Equality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCC979C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x19 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x2C9UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCC9780;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x1E8UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x2C9UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCC9780;
        label_0xCC9780:
        ;
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x1E8UL))));
        x8 = RuntimeMemory.ReadU64(x8);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        __arm64_pair_address_13408144 = x8;
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13408144)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13408144) + (0x4UL))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x8UL))))), 0));
        goto label_0xCC97C4;
        label_0xCC979C:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x28UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCC97D8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179D508UL /* metadata target: Transform.get_position */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x28UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCC97D8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        v8 = v0;
        x0 = RuntimeCalls.InvokeDirect(0x179D508UL /* metadata target: Transform.get_position */, x0, x1, x2, x3);
        goto label_0xCC97C4;
        label_0xCC97C4:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        __arm64_load_address_13408208 = sp;
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_load_address_13408208)), 0));
        return x0;
        label_0xCC97D8:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `bl_MiniMapItem.get_m_miniMap` — RVA `0xcc97dc`

- Lift status: **exact**; input span: 200 bytes; span to next metadata RVA: 200 bytes.
- Metadata signature: `private bl_MiniMap get_m_miniMap() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=29 (informational only).

```csharp
public static ulong bl_MiniMapItem_get_m_miniMap_RVAcc97dc(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
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
        x19 = 0x1BAB000UL;
        x22 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x56CUL))))))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0xD8UL))));
        x20 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCC9820;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xAE8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x56CUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCC9820;
        label_0xCC9820:
        ;
        x19 = x20;
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xD8UL))));
        x0 = RuntimeMemory.ReadU64(x22);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCC9838;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCC9834UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCC9838;
        label_0xCC9838:
        ;
        x0 = x21;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179568CUL /* metadata target: Object.op_Equality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCC988C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xB0UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCC98A0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794C14UL /* metadata target: GameObject.get_transform */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCC98A0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179E9FCUL /* metadata target: Transform.get_root */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCC98A0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xAE8UL))));
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xE31E2CUL, x0, x1, x2, x3);
        x1 = x0;
        RuntimeMemory.WriteU64(x19, x0);
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        goto label_0xCC988C;
        label_0xCC988C:
        ;
        x0 = RuntimeMemory.ReadU64(x19);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        label_0xCC98A0:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `bl_MiniMapItem.DestroyItem` — RVA `0xcc98a4`

- Lift status: **exact**; input span: 384 bytes; span to next metadata RVA: 384 bytes.
- Metadata signature: `public void DestroyItem(bool inmediate) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=66 (informational only).

```csharp
public static ulong bl_MiniMapItem_DestroyItem_RVAcc98a4(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
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
        x22 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x565UL))))))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0xD8UL))));
        x20 = unchecked((ulong)(unchecked((uint)(x1))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCC9910;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xAF0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x398UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xAF8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB00UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x565UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCC9910;
        label_0xCC9910:
        ;
        x0 = RuntimeMemory.ReadU64(x22);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xA0UL))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCC9924;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCC9920UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCC9924;
        label_0xCC9924:
        ;
        x0 = x21;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179568CUL /* metadata target: Object.op_Equality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCC99A4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = 0x1A8E000UL;
        x21 = 0x1A8E000UL;
        x22 = 0x1A8C000UL;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xB00UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xAF8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x398UL))));
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1798300UL /* metadata target: Object.get_name */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x20);
        x2 = RuntimeMemory.ReadU64(x21);
        x1 = x0;
        x3 = 0x0UL;
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0x13F661CUL /* metadata target: String.Concat */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x22);
        x19 = x0;
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCC998C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCC998C;
        label_0xCC998C:
        ;
        x0 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x1 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0x1770B68UL /* metadata target: Debug.Log */);
        label_0xCC99A4:
        ;
        x0 = RuntimeMemory.ReadU64(x22);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x48UL))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCC99B8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCC99B4UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCC99B8;
        label_0xCC99B8:
        ;
        x0 = x21;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179568CUL /* metadata target: Object.op_Equality */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xA0UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCC9A20;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = 0x1A8E000UL;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0xAF0UL))));
        x21 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) | (unchecked((uint)(x20)))))));
        x0 = x8;
        x1 = RuntimeMemory.ReadU64(x9);
        x0 = RuntimeCalls.InvokeDirect(0xE31BC8UL, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x21))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCC9A04;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCC99ECUL);
        }
        if ((x0 == 0x0UL))
        {
            goto label_0xCC9A20;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x20))) & (unchecked((uint)(0x1UL)))))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0xCC5BBCUL /* metadata target: bl_IconItem.DestroyIcon */);
        label_0xCC9A04:
        ;
        if ((x0 == 0x0UL))
        {
            goto label_0xCC9A20;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x48UL))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0xCC5C9CUL /* metadata target: bl_IconItem.DestroyIcon */);
        label_0xCC9A20:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        return default(ulong);
    }
```

## `bl_MiniMapItem.SetIcon` — RVA `0xcc9a24`

- Lift status: **exact**; input span: 256 bytes; span to next metadata RVA: 256 bytes.
- Metadata signature: `public void SetIcon(Sprite ico) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=42 (informational only).

```csharp
public static ulong bl_MiniMapItem_SetIcon_RVAcc9a24(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
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
        x21 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x22) + (0x566UL))))))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xD8UL))));
        x19 = x1;
        x20 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCC9A84;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x398UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xAD8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB08UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x22) + (0x566UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCC9A84;
        label_0xCC9A84:
        ;
        x0 = RuntimeMemory.ReadU64(x21);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xB0UL))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCC9A98;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCC9A94UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCC9A98;
        label_0xCC9A98:
        ;
        x0 = x21;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179568CUL /* metadata target: Object.op_Equality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCC9AE4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x398UL))));
        x19 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(x8);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xB08UL))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCC9ACC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCC9AC8UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCC9ACC;
        label_0xCC9ACC:
        ;
        x0 = RuntimeMemory.ReadU64(x19);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x1 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0x17714B0UL /* metadata target: Debug.LogWarning */);
        label_0xCC9AE4:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xB0UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCC9B20;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xAD8UL))));
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xE49224UL, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCC9B20;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x28UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCC9B20;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x2 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0x1813790UL /* metadata target: Image.set_sprite */);
        label_0xCC9B20:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `bl_MiniMapItem.SetCircleArea` — RVA `0xcc9b24`

- Lift status: **exact**; input span: 168 bytes; span to next metadata RVA: 168 bytes.
- Metadata signature: `public void SetCircleArea(float radius, Color AreaColor) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=24 (informational only).

```csharp
public static ulong bl_MiniMapItem_SetCircleArea_RVAcc9b24(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_load_address_13409216 = default(ulong);
        ulong __arm64_pair_address_13409064 = default(ulong);
        ulong __arm64_pair_address_13409068 = default(ulong);
        ulong __arm64_pair_address_13409208 = default(ulong);
        ulong __arm64_pair_address_13409212 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v10 = default(RuntimeVector128);
        RuntimeVector128 v11 = default(RuntimeVector128);
        RuntimeVector128 v12 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
        RuntimeVector128 v4 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        RuntimeVector128 v9 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteF64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFC0UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v12.GetUInt64(0)))));
        sp = unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFC0UL)));
        __arm64_pair_address_13409064 = unchecked((ulong)((sp) + (0x8UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13409064, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v11.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13409064) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v10.GetUInt64(0)))));
        __arm64_pair_address_13409068 = unchecked((ulong)((sp) + (0x18UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13409068, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13409068) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x28UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))), x19);
        x20 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x567UL))))))));
        v8 = v4;
        v9 = v3;
        v10 = v2;
        v11 = v1;
        v12 = v0;
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCC9B70;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xAD8UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x567UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCC9B70;
        label_0xCC9B70:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xB0UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCC9BC8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xAD8UL))));
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xE49224UL, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCC9BC8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        v0 = v12;
        v1 = v11;
        v2 = v10;
        v3 = v9;
        v4 = v8;
        x0 = RuntimeCalls.InvokeDirect(0xCC5E48UL /* metadata target: bl_IconItem.SetCircleArea */, x0, x1, x2, x3);
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0xB8UL))), x0);
        x1 = x0;
        x0 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x28UL))));
        __arm64_pair_address_13409208 = unchecked((ulong)((sp) + (0x18UL)));
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13409208)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13409208) + (0x8UL))))), 0));
        __arm64_pair_address_13409212 = unchecked((ulong)((sp) + (0x8UL)));
        v11 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13409212)), 0));
        v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13409212) + (0x8UL))))), 0));
        __arm64_load_address_13409216 = sp;
        v12 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_load_address_13409216)), 0));
        sp = unchecked((ulong)((__arm64_load_address_13409216) + (0x40UL)));
        return RuntimeCalls.InvokeDirect(0xB7D8D0UL);
        label_0xCC9BC8:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `bl_MiniMapItem.HideCircleArea` — RVA `0xcc9bcc`

- Lift status: **exact**; input span: 104 bytes; span to next metadata RVA: 104 bytes.
- Metadata signature: `public void HideCircleArea() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=14 (informational only).

```csharp
public static ulong bl_MiniMapItem_HideCircleArea_RVAcc9bcc(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        x20 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x568UL))))))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCC9BF8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xAD8UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x568UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCC9BF8;
        label_0xCC9BF8:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xB0UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCC9C30;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xAD8UL))));
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xE49224UL, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCC9C30;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCC9C14UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xCC60ACUL /* metadata target: bl_IconItem.HideCircleArea */, x0, x1, x2, x3);
        RuntimeMemory.WritePtr(unchecked((ulong)((x19) + (0xB8UL))), 0x0UL);
        x0 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x1 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0xB7D8D0UL);
        label_0xCC9C30:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `bl_MiniMapItem.HideItem` — RVA `0xcc9c34`

- Lift status: **exact**; input span: 200 bytes; span to next metadata RVA: 200 bytes.
- Metadata signature: `public void HideItem() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=33 (informational only).

```csharp
public static ulong bl_MiniMapItem_HideItem_RVAcc9c34(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        x21 = 0x1BAB000UL;
        x20 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x569UL))))))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xD8UL))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCC9C80;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x398UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB10UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x569UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCC9C80;
        label_0xCC9C80:
        ;
        x0 = RuntimeMemory.ReadU64(x20);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xB0UL))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCC9C94;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCC9C90UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCC9C94;
        label_0xCC9C94:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794AC8UL /* metadata target: Object.op_Inequality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCC9CC4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xB0UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCC9CF8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x2 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeDirect(0x1794CD0UL /* metadata target: GameObject.SetActive */);
        label_0xCC9CC4:
        ;
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x398UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCC9CDC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCC9CD8UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xCC9CDC;
        label_0xCC9CDC:
        ;
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB10UL))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x1 = 0x0UL;
        x0 = RuntimeMemory.ReadU64(x8);
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeDirect(0x1770B68UL /* metadata target: Debug.Log */);
        label_0xCC9CF8:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `bl_MiniMapItem.ShowItem` — RVA `0xcc9cfc`

- Lift status: **exact**; input span: 200 bytes; span to next metadata RVA: 200 bytes.
- Metadata signature: `public void ShowItem() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=33 (informational only).

```csharp
public static ulong bl_MiniMapItem_ShowItem_RVAcc9cfc(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        x21 = 0x1BAB000UL;
        x20 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x56AUL))))))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xD8UL))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCC9D48;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x398UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB18UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x56AUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCC9D48;
        label_0xCC9D48:
        ;
        x0 = RuntimeMemory.ReadU64(x20);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xB0UL))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCC9D5C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCC9D58UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCC9D5C;
        label_0xCC9D5C:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794AC8UL /* metadata target: Object.op_Inequality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCC9D8C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xB0UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCC9DC0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x2 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeDirect(0x1794CD0UL /* metadata target: GameObject.SetActive */);
        label_0xCC9D8C:
        ;
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x398UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCC9DA4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCC9DA0UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xCC9DA4;
        label_0xCC9DA4:
        ;
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB18UL))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x1 = 0x0UL;
        x0 = RuntimeMemory.ReadU64(x8);
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeDirect(0x1770B68UL /* metadata target: Debug.Log */);
        label_0xCC9DC0:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `bl_MiniMapItem.ctor` — RVA `0xcc9dc4`

- Lift status: **exact**; input span: 236 bytes; span to next metadata RVA: 236 bytes.
- Metadata signature: `public void .ctor() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=33 (informational only).

```csharp
public static ulong bl_MiniMapItem_ctor_RVAcc9dc4(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
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
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x56DUL))))))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCC9DF0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB20UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x56DUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCC9DF0;
        label_0xCC9DF0:
        ;
        x21 = 0x1BAB000UL;
        x20 = 0x1A8E000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x2C9UL))))))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xB20UL))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCC9E18;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x1E8UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x2C9UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCC9E18;
        label_0xCC9E18:
        ;
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x1E8UL))));
        x9 = 0x433000UL;
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((x9) + (0x160UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((x9) + (0x160UL))));
#endif
        x9 = 0x433000UL;
        x8 = RuntimeMemory.ReadU64(x8);
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((x9) + (0x1D0UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((x9) + (0x1D0UL))));
#endif
        x9 = unchecked((ulong)(unchecked((uint)(0x6666UL))));
        x9 = unchecked((ulong)(unchecked((uint)(unchecked((ulong)((unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) & (unchecked((uint)((~(0xFFFFUL)))))))))) | (unchecked((ulong)((unchecked((ulong)((0x3F66UL) << (int)(unchecked((int)(0x10UL)))))) << (int)(unchecked((int)(0x0UL))))))))))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x21 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = x19;
        v2 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(x8)), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x8UL))))), 0));
        x8 = unchecked((ulong)(unchecked((uint)(0x42200000UL))));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x19) + (0x50UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((x19) + (0x50UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x19) + (0x68UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((x19) + (0x68UL))), v1);
#endif
        RuntimeMemory.WriteU32(unchecked((ulong)((x19) + (0x60UL))), unchecked((uint)(x8)));
        RuntimeMemory.WriteU32(unchecked((ulong)((x19) + (0x78UL))), unchecked((uint)(x9)));
        RuntimeMemory.WriteF64(unchecked((ulong)((x19) + (0x30UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v2.GetUInt64(0)))));
        RuntimeMemory.WriteF32(unchecked((ulong)((x19) + (0x38UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x7CUL))), unchecked((byte)(unchecked((uint)(x21)))));
        x1 = RuntimeMemory.ReadU64(x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x80UL))), x1);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x8 = 0x431000UL;
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((x8) + (0xD50UL))))), 0));
        x8 = 0x999AUL;
        x8 = unchecked((ulong)((unchecked((ulong)((x8) & ((~(0xFFFFUL)))))) | (unchecked((ulong)((unchecked((ulong)((0x3E99UL) << (int)(unchecked((int)(0x10UL)))))) << (int)(unchecked((int)(0x0UL))))))));
        x8 = unchecked((ulong)((unchecked((ulong)((x8) & ((~(0xFFFFUL)))))) | (unchecked((ulong)((unchecked((ulong)((0x2UL) << (int)(unchecked((int)(0x20UL)))))) << (int)(unchecked((int)(0x0UL))))))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x88UL))), unchecked((byte)(unchecked((uint)(x21)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((x19) + (0x8CUL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x94UL))), x8);
        x0 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x1 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeDirect(0x1796274UL /* metadata target: MonoBehaviour.ctor */);
        return default(ulong);
    }
```
