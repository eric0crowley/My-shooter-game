# `bl_MiniMapUtils` — TypeDefIndex 3486

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## `bl_MiniMapUtils.GetMiniMap` — RVA `0xcc6020`

- Lift status: **exact**; input span: 140 bytes; span to next metadata RVA: 140 bytes.
- Metadata signature: `public static bl_MiniMap GetMiniMap(int id = 0) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=20 (informational only).

```csharp
public static ulong bl_MiniMapUtils_GetMiniMap_RVAcc6020(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13394056 = default(uint);
        uint __arm64_flags_right_13394056 = default(uint);
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
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x57CUL))))))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xD8UL))));
        x19 = unchecked((ulong)(unchecked((uint)(x0))));
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
        }
        else
        {
            x0 = 0x1A8E000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x9E8UL))));
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x0 = 0x1A8C000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD8UL))));
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
            RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x57CUL))), unchecked((byte)(unchecked((uint)(x8)))));
        }
        label_0xCC6060:
        ;
        x0 = RuntimeMemory.ReadU64(x20);
        x20 = 0x1A8E000UL;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x9E8UL))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
        }
        else
        {
            x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        }
        label_0xCC6078:
        ;
        x0 = RuntimeMemory.ReadU64(x20);
        x0 = RuntimeCalls.InvokeDirect(0xD29EA4UL, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            label_0xCC60A4:
            ;
            x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        }
        else
        {
            x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x18UL))))));
            __arm64_flags_left_13394056 = unchecked((uint)(x8));
            __arm64_flags_right_13394056 = unchecked((uint)(x19));
            if (((!((__arm64_flags_left_13394056 >= __arm64_flags_right_13394056))) || (unchecked((uint)((__arm64_flags_left_13394056) - (__arm64_flags_right_13394056))) == unchecked((uint)0x0UL))))
            {
            }
            else
            {
                x8 = unchecked((ulong)((x0) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x19))) << (int)(unchecked((int)(unchecked((uint)(0x3UL))))))))))));
                x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
                x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
                x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
                x30 = RuntimeMemory.ReadU64(sp);
                x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
                return x0;
            }
        }
        label_0xCC60A8:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB7CUL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `bl_MiniMapUtils.CalculateMiniMapPosition` — RVA `0xcc791c`

- Lift status: **exact**; input span: 144 bytes; span to next metadata RVA: 144 bytes.
- Metadata signature: `public static Vector3 CalculateMiniMapPosition(Vector3 viewPoint, RectTransform maxAnchor) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=22 (informational only).

```csharp
public static ulong bl_MiniMapUtils_CalculateMiniMapPosition_RVAcc791c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_load_address_13400480 = default(ulong);
        ulong __arm64_pair_address_13400352 = default(ulong);
        ulong __arm64_pair_address_13400356 = default(ulong);
        ulong __arm64_pair_address_13400456 = default(ulong);
        ulong __arm64_pair_address_13400460 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v10 = default(RuntimeVector128);
        RuntimeVector128 v11 = default(RuntimeVector128);
        RuntimeVector128 v12 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        RuntimeVector128 v9 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        RuntimeMemory.WriteF64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFC0UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v12.GetUInt64(0)))));
        sp = unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFC0UL)));
        __arm64_pair_address_13400352 = unchecked((ulong)((sp) + (0x10UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13400352, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v11.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13400352) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v10.GetUInt64(0)))));
        __arm64_pair_address_13400356 = unchecked((ulong)((sp) + (0x20UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13400356, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13400356) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))), x19);
        if ((x0 == 0x0UL))
        {
            label_0xCC79A8:
            ;
            x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        }
        else
        {
            x1 = 0x0UL;
            x19 = x0;
            x0 = RuntimeCalls.InvokeDirect(0x179C8ACUL /* metadata target: RectTransform.get_sizeDelta */, x0, x1, x2, x3);
            x0 = x19;
            x1 = 0x0UL;
            x0 = RuntimeCalls.InvokeDirect(0x179C8ACUL /* metadata target: RectTransform.get_sizeDelta */, x0, x1, x2, x3);
            x0 = x19;
            x1 = 0x0UL;
            x0 = RuntimeCalls.InvokeDirect(0x179C8ACUL /* metadata target: RectTransform.get_sizeDelta */, x0, x1, x2, x3);
            x0 = x19;
            x1 = 0x0UL;
            x0 = RuntimeCalls.InvokeDirect(0x179C8ACUL /* metadata target: RectTransform.get_sizeDelta */, x0, x1, x2, x3);
            x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
            x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))));
            __arm64_pair_address_13400456 = unchecked((ulong)((sp) + (0x20UL)));
            v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13400456)), 0));
            v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13400456) + (0x8UL))))), 0));
            __arm64_pair_address_13400460 = unchecked((ulong)((sp) + (0x10UL)));
            v11 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13400460)), 0));
            v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13400460) + (0x8UL))))), 0));
            __arm64_load_address_13400480 = sp;
            v12 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_load_address_13400480)), 0));
            return x0;
        }
        return default(ulong);
    }
```
