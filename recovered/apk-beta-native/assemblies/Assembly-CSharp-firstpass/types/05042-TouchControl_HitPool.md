# `TouchControl.HitPool` — TypeDefIndex 5042

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x20` | `TouchControl.Hit` | `tempHit` |

## `TouchControl.HitPool.ctor` — RVA `0xc534a4`

- Lift status: **exact**; input span: 136 bytes; span to next metadata RVA: 136 bytes.
- Metadata signature: `public void .ctor() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=22 (informational only).

```csharp
public static ulong TouchControl_HitPool_ctor_RVAc534a4(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
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
        x21 = 0x1BAB000UL;
        x22 = 0x1A8C000UL;
        x20 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x25EUL))))))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0xD98UL))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xDA0UL))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC534F0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xDA0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD98UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x25EUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC534F0;
        label_0xC534F0:
        ;
        x1 = RuntimeMemory.ReadU64(x22);
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0x115E530UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x20);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x1589338UL /* metadata target: Object.ctor */, x0, x1, x2, x3);
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x20UL))), x20);
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

## `TouchControl.HitPool.HitTestAny` — RVA `0xc5352c`

- Lift status: **exact**; input span: 460 bytes; span to next metadata RVA: 460 bytes.
- Metadata signature: `public bool HitTestAny(List<TouchControl> controlList, Vector2 screenPos, Camera cam, float fingerRadPx = 0.0, TouchControl.HitPool.TouchControlFilterFunc filter) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=71 (informational only).

```csharp
public static uint TouchControl_HitPool_HitTestAny_RVAc5352c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12924404 = default(uint);
        uint __arm64_flags_left_12924412 = default(uint);
        uint __arm64_flags_left_12924572 = default(uint);
        uint __arm64_flags_right_12924404 = default(uint);
        uint __arm64_flags_right_12924412 = default(uint);
        uint __arm64_flags_right_12924572 = default(uint);
        ulong __arm64_load_address_12924652 = default(ulong);
        ulong __arm64_pair_address_12924208 = default(ulong);
        ulong __arm64_pair_address_12924648 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v10 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
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
        ulong x27 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteF64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFF90UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v10.GetUInt64(0)))));
        sp = unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFF90UL)));
        __arm64_pair_address_12924208 = unchecked((ulong)((sp) + (0x10UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12924208, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12924208) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x27);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x0UL))), x26);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))), x25);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x0UL))), x24);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x8UL))), x19);
        x24 = 0x1BAB000UL;
        x25 = 0x1A8C000UL;
        x23 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x24) + (0x25FUL))))))));
        x25 = RuntimeMemory.ReadU64(unchecked((ulong)((x25) + (0xDA8UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0xDB0UL))));
        x20 = x3;
        v8 = v2;
        x21 = x2;
        v9 = v1;
        v10 = v0;
        x22 = x1;
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC535D0;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x5A0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x5A8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xDB0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xDA8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xDB8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x24) + (0x25FUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC535D0;
        label_0xC535D0:
        ;
        x2 = RuntimeMemory.ReadU64(x25);
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0x115EA34UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x1 = RuntimeMemory.ReadU64(x23);
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0x115E84CUL, x0, x1, x2, x3);
        if ((x22 == 0x0UL))
        {
            goto label_0xC536F4;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x22) + (0x18UL))))));
        __arm64_flags_left_12924404 = unchecked((uint)(x8));
        __arm64_flags_right_12924404 = unchecked((uint)0x0UL);
        x25 = unchecked((ulong)((((!((unchecked((uint)((__arm64_flags_left_12924404) - (__arm64_flags_right_12924404))) == unchecked((uint)0x0UL)))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12924404) - (__arm64_flags_right_12924404))))) < unchecked((int)0x0UL)) == (((unchecked((int)(__arm64_flags_left_12924404)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12924404)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12924404) - (__arm64_flags_right_12924404))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12924404)) < unchecked((int)0x0UL)))))) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        __arm64_flags_left_12924412 = unchecked((uint)(x8));
        __arm64_flags_right_12924412 = unchecked((uint)0x1UL);
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_12924412) - (__arm64_flags_right_12924412))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_12924412)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12924412)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12924412) - (__arm64_flags_right_12924412))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12924412)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC536D0;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x26 = 0x1A8C000UL;
        x27 = 0x1A8C000UL;
        x26 = RuntimeMemory.ReadU64(unchecked((ulong)((x26) + (0x5A8UL))));
        x27 = RuntimeMemory.ReadU64(unchecked((ulong)((x27) + (0xD8UL))));
        x23 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xC53618;
        label_0xC53618:
        ;
        x2 = RuntimeMemory.ReadU64(x26);
        x0 = x22;
        x1 = unchecked((ulong)(unchecked((uint)(x23))));
        x0 = RuntimeCalls.InvokeDirect(0x10A30C0UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = RuntimeMemory.ReadU64(x27);
        x24 = x0;
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC53640;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xC53640;
        label_0xC53640:
        ;
        x0 = x24;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179568CUL /* metadata target: Object.op_Equality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC53694;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC53654UL)));
        }
        if ((x20 == 0x0UL))
        {
            goto label_0xC53670;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x18UL))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x40UL))));
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x28UL))));
        x1 = x24;
        x0 = RuntimeCalls.InvokeIndirect(x8, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC53694;
        }
        else
        {
            goto label_0xC53670;
        }
        label_0xC53670:
        ;
        if ((x24 == 0x0UL))
        {
            goto label_0xC536F4;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x20UL))));
        x0 = x24;
        v0 = v10;
        v1 = v9;
        x1 = x21;
        v2 = v8;
        x0 = RuntimeCalls.InvokeDirect(0xC52820UL /* metadata target: TouchControl.HitTest */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC536AC;
        }
        else
        {
            goto label_0xC53694;
        }
        label_0xC53694:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x22) + (0x18UL))))));
        x23 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x23))) + (unchecked((uint)(0x1UL)))))));
        __arm64_flags_left_12924572 = unchecked((uint)(x23));
        __arm64_flags_right_12924572 = unchecked((uint)(x8));
        x25 = unchecked((ulong)((((unchecked((int)(unchecked((uint)((__arm64_flags_left_12924572) - (__arm64_flags_right_12924572))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_12924572)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12924572)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12924572) - (__arm64_flags_right_12924572))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12924572)) < unchecked((int)0x0UL))))) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_12924572) - (__arm64_flags_right_12924572))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_12924572)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12924572)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12924572) - (__arm64_flags_right_12924572))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12924572)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC53618;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC536A8UL)));
        }
        goto label_0xC536D0;
        label_0xC536AC:
        ;
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xDB8UL))));
        x1 = unchecked((ulong)(unchecked((uint)(0xFFFFFFFFFFFFFFFFUL))));
        x0 = x19;
        x2 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x115E648UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC536F4;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x20UL))));
        x0 = RuntimeCalls.InvokeDirect(0xC52FA8UL /* metadata target: TouchControl.Hit.CopyFrom */, x0, x1, x2, x3);
        goto label_0xC536D0;
        label_0xC536D0:
        ;
        x0 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x25))) & (unchecked((uint)(0x1UL)))))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x60UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x50UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x8UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x40UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))));
        x26 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
        x25 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x27 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        __arm64_pair_address_12924648 = unchecked((ulong)((sp) + (0x10UL)));
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12924648)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12924648) + (0x8UL))))), 0));
        __arm64_load_address_12924652 = sp;
        v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_load_address_12924652)), 0));
        sp = unchecked((ulong)((__arm64_load_address_12924652) + (0x70UL)));
        return unchecked((uint)(x0));
        label_0xC536F4:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        return default(uint);
    }
```

## `TouchControl.HitPool.HitTest` — RVA `0xc536f8`

- Lift status: **partial**; input span: 812 bytes; span to next metadata RVA: 812 bytes.
- Metadata signature: `public int HitTest(List<TouchControl> controlList, Vector2 screenPos, Camera cam, int maxHits = 8, float fingerRadPx = 0.0, TouchControl.HitPool.TouchControlFilterFunc filter) { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=130 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'csinc' at 0xc537f8; reason: Unknown IR expression at 0xc537f8

```csharp
public static ulong TouchControl_HitPool_HitTest_RVAc536f8(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12924912 = default(uint);
        uint __arm64_flags_left_12924956 = default(uint);
        uint __arm64_flags_left_12925144 = default(uint);
        uint __arm64_flags_left_12925244 = default(uint);
        uint __arm64_flags_left_12925412 = default(uint);
        uint __arm64_flags_right_12924912 = default(uint);
        uint __arm64_flags_right_12924956 = default(uint);
        uint __arm64_flags_right_12925144 = default(uint);
        uint __arm64_flags_right_12925244 = default(uint);
        uint __arm64_flags_right_12925412 = default(uint);
        ulong __arm64_load_address_12925464 = default(ulong);
        ulong __arm64_pair_address_12924668 = default(ulong);
        ulong __arm64_pair_address_12925460 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v10 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
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
        ulong x27 = default(ulong);
        ulong x28 = default(ulong);
        ulong x29 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteF64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFF80UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v10.GetUInt64(0)))));
        sp = unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFF80UL)));
        __arm64_pair_address_12924668 = unchecked((ulong)((sp) + (0x10UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12924668, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12924668) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x29);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x0UL))), x28);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))), x27);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x0UL))), x26);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))), x25);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x0UL))), x24);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x8UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x70UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x70UL)))) + (0x8UL))), x19);
        x26 = 0x1BAB000UL;
        x25 = 0x1A8C000UL;
        x24 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x26) + (0x260UL))))))));
        x25 = RuntimeMemory.ReadU64(unchecked((ulong)((x25) + (0xDB0UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((x24) + (0xDA8UL))));
        x19 = x4;
        v8 = v2;
        x23 = unchecked((ulong)(unchecked((uint)(x3))));
        x20 = x2;
        v9 = v1;
        v10 = v0;
        x22 = x1;
        x21 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC537EC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xDC0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xDC8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xDD0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x5A0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x5A8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xDD8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xDB0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xDA8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xDE0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xDB8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xDE8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x26) + (0x260UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC537EC;
        label_0xC537EC:
        ;
        x1 = RuntimeMemory.ReadU64(x25);
        __arm64_flags_left_12924912 = unchecked((uint)(x23));
        __arm64_flags_right_12924912 = unchecked((uint)0x1UL);
        x0 = x21;
        RuntimeCalls.Unsupported("csinc", 0xC537F8UL);
        x23 = unchecked((ulong)((__Unsupported<bool>("Unknown IR expression") ? unchecked((uint)(x23)) : unchecked((uint)((unchecked((uint)0x0UL)) + (unchecked((uint)0x1UL)))))));
        x0 = RuntimeCalls.InvokeDirect(0x115E84CUL, x0, x1, x2, x3);
        x2 = RuntimeMemory.ReadU64(x24);
        x0 = x21;
        x1 = unchecked((ulong)(unchecked((uint)(x23))));
        RuntimeMemory.WriteU32(unchecked((ulong)((sp) + (0xCUL))), unchecked((uint)(x23)));
        x0 = RuntimeCalls.InvokeDirect(0x115EA34UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        if ((x22 == 0x0UL))
        {
            goto label_0xC53A20;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x22) + (0x18UL))))));
        __arm64_flags_left_12924956 = unchecked((uint)(x8));
        __arm64_flags_right_12924956 = unchecked((uint)0x1UL);
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_12924956) - (__arm64_flags_right_12924956))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_12924956)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12924956)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12924956) - (__arm64_flags_right_12924956))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12924956)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC539EC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x29 = 0x1A8C000UL;
        x28 = 0x1A8C000UL;
        x25 = 0x1A8C000UL;
        x29 = RuntimeMemory.ReadU64(unchecked((ulong)((x29) + (0x5A8UL))));
        x28 = RuntimeMemory.ReadU64(unchecked((ulong)((x28) + (0xD8UL))));
        x25 = RuntimeMemory.ReadU64(unchecked((ulong)((x25) + (0xDD8UL))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((sp) + (0xCUL))))));
        x24 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x27 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) - (unchecked((uint)(0x1UL)))))));
        x23 = unchecked((ulong)(unchecked((uint)(x27))));
        goto label_0xC5384C;
        label_0xC5384C:
        ;
        x2 = RuntimeMemory.ReadU64(x29);
        x0 = x22;
        x1 = unchecked((ulong)(unchecked((uint)(x24))));
        x0 = RuntimeCalls.InvokeDirect(0x10A30C0UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = RuntimeMemory.ReadU64(x28);
        x26 = x0;
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC53874;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xC53874;
        label_0xC53874:
        ;
        x0 = x26;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179568CUL /* metadata target: Object.op_Equality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC539DC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC53888UL);
        }
        if ((x19 == 0x0UL))
        {
            goto label_0xC538A4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x18UL))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x40UL))));
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x28UL))));
        x1 = x26;
        x0 = RuntimeCalls.InvokeIndirect(x8, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC539DC;
        }
        else
        {
            goto label_0xC538A4;
        }
        label_0xC538A4:
        ;
        if ((x26 == 0x0UL))
        {
            goto label_0xC53A20;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x20UL))));
        x0 = x26;
        v0 = v10;
        v1 = v9;
        x1 = x20;
        v2 = v8;
        x0 = RuntimeCalls.InvokeDirect(0xC52820UL /* metadata target: TouchControl.HitTest */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC539DC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x10UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC53A20;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x26 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xC538D4;
        label_0xC538D4:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x18UL))))));
        __arm64_flags_left_12925144 = unchecked((uint)(x26));
        __arm64_flags_right_12925144 = unchecked((uint)(x8));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_12925144) - (__arm64_flags_right_12925144))))) < unchecked((int)0x0UL)) == (((unchecked((int)(__arm64_flags_left_12925144)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12925144)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12925144) - (__arm64_flags_right_12925144))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12925144)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC53918;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x2 = RuntimeMemory.ReadU64(x25);
        x27 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x20UL))));
        x1 = unchecked((ulong)(unchecked((uint)(x26))));
        x0 = RuntimeCalls.InvokeDirect(0x10A30C0UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        if ((x27 == 0x0UL))
        {
            goto label_0xC53A20;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = x0;
        x0 = x27;
        x0 = RuntimeCalls.InvokeDirect(0xC53014UL /* metadata target: TouchControl.Hit.IsHigherThan */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC53920;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x10UL))));
        x26 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x26))) + (unchecked((uint)(0x1UL)))))));
        x27 = unchecked((ulong)(unchecked((uint)(x23))));
        if ((x0 != 0x0UL))
        {
            goto label_0xC538D4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC53914UL);
        }
        goto label_0xC53A20;
        label_0xC53918:
        ;
        x26 = unchecked((ulong)(unchecked((uint)(0xFFFFFFFFFFFFFFFFUL))));
        goto label_0xC53924;
        label_0xC53920:
        ;
        x27 = unchecked((ulong)(unchecked((uint)(x23))));
        goto label_0xC53924;
        label_0xC53924:
        ;
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xDE8UL))));
        x0 = x21;
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x115E608UL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((sp) + (0xCUL))))));
        __arm64_flags_left_12925244 = unchecked((uint)(x0));
        __arm64_flags_right_12925244 = unchecked((uint)(x8));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_12925244) - (__arm64_flags_right_12925244))))) < unchecked((int)0x0UL)) == (((unchecked((int)(__arm64_flags_left_12925244)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12925244)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12925244) - (__arm64_flags_right_12925244))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12925244)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC5396C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xDB8UL))));
        x0 = x21;
        x1 = unchecked((ulong)(unchecked((uint)(x26))));
        x2 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x115E648UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC53A20;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x20UL))));
        x0 = RuntimeCalls.InvokeDirect(0xC52FA8UL /* metadata target: TouchControl.Hit.CopyFrom */, x0, x1, x2, x3);
        goto label_0xC539DC;
        label_0xC5396C:
        ;
        if ((unchecked((uint)((unchecked((uint)(x26))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x1FUL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC539DC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x10UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC53A20;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x2 = RuntimeMemory.ReadU64(x25);
        x1 = unchecked((ulong)(unchecked((uint)(x27))));
        x0 = RuntimeCalls.InvokeDirect(0x10A30C0UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x10UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC53A20;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = 0x1A8C000UL;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0xDC8UL))));
        x1 = unchecked((ulong)(unchecked((uint)(x27))));
        x27 = x0;
        x0 = x8;
        x2 = RuntimeMemory.ReadU64(x9);
        x0 = RuntimeCalls.InvokeDirect(0x10A48FCUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x10UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC53A20;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xDC0UL))));
        x1 = unchecked((ulong)(unchecked((uint)(x26))));
        x2 = x27;
        x3 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x10A3ED8UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        if ((x27 == 0x0UL))
        {
            goto label_0xC53A20;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x20UL))));
        x0 = x27;
        x0 = RuntimeCalls.InvokeDirect(0xC52FA8UL /* metadata target: TouchControl.Hit.CopyFrom */, x0, x1, x2, x3);
        x27 = unchecked((ulong)(unchecked((uint)(x23))));
        goto label_0xC539DC;
        label_0xC539DC:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x22) + (0x18UL))))));
        x24 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x24))) + (unchecked((uint)(0x1UL)))))));
        __arm64_flags_left_12925412 = unchecked((uint)(x24));
        __arm64_flags_right_12925412 = unchecked((uint)(x8));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_12925412) - (__arm64_flags_right_12925412))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_12925412)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12925412)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12925412) - (__arm64_flags_right_12925412))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12925412)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC5384C;
        }
        else
        {
            goto label_0xC539EC;
        }
        label_0xC539EC:
        ;
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xDE8UL))));
        x0 = x21;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x70UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x70UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x60UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x8UL))));
        x1 = RuntimeMemory.ReadU64(x8);
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x50UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x8UL))));
        x26 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x40UL))));
        x25 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))));
        x28 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
        x27 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))));
        x29 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        __arm64_pair_address_12925460 = unchecked((ulong)((sp) + (0x10UL)));
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12925460)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12925460) + (0x8UL))))), 0));
        __arm64_load_address_12925464 = sp;
        v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_load_address_12925464)), 0));
        sp = unchecked((ulong)((__arm64_load_address_12925464) + (0x80UL)));
        return RuntimeCalls.InvokeDirect(0x115E608UL);
        label_0xC53A20:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `TouchControl.HitPool.CreateInternalObject` — RVA `0xc53a24`

- Lift status: **exact**; input span: 84 bytes; span to next metadata RVA: 84 bytes.
- Metadata signature: `protected override TouchControl.Hit CreateInternalObject() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=13 (informational only).

```csharp
public static ulong TouchControl_HitPool_CreateInternalObject_RVAc53a24(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        x19 = 0x1BAB000UL;
        x20 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x261UL))))))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xDA0UL))));
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
        }
        else
        {
            x0 = 0x1A8C000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xDA0UL))));
            // Likely IL2CPP class initialization helper (guarded call).
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
            RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x261UL))), unchecked((byte)(unchecked((uint)(x8)))));
        }
        label_0xC53A54:
        ;
        x0 = RuntimeMemory.ReadU64(x20);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = 0x0UL;
        x19 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x1589338UL /* metadata target: Object.ctor */, x0, x1, x2, x3);
        x0 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        return default(ulong);
    }
```
