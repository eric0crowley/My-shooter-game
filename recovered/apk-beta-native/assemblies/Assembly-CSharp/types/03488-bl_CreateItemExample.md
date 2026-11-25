# `bl_CreateItemExample` — TypeDefIndex 3488

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x20` | `bl_MMExampleManager` | `exampler` |
| `0x28` | `bl_MiniMap` | `MiniMap` |

## `bl_CreateItemExample.Start` — RVA `0xccaedc`

- Lift status: **exact**; input span: 124 bytes; span to next metadata RVA: 124 bytes.
- Metadata signature: `private void Start() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=18 (informational only).

```csharp
public static ulong bl_CreateItemExample_Start_RVAccaedc(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
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
        x20 = 0x1BAB000UL;
        x21 = 0x1A8E000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x582UL))))))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xB58UL))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCCAF10;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB58UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x582UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCCAF10;
        label_0xCCAF10:
        ;
        x1 = RuntimeMemory.ReadU64(x21);
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xE31BC8UL, x0, x1, x2, x3);
        x20 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x20) + (0x20UL))), x0);
        x1 = x0;
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x20);
        if ((x0 == 0x0UL))
        {
            goto label_0xCCAF54;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCCAF38UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xCCAF58UL /* metadata target: bl_MMExampleManager.get_GetActiveMiniMap */, x0, x1, x2, x3);
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x28UL))), x0);
        x1 = x0;
        x0 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeDirect(0xB7D8D0UL);
        label_0xCCAF54:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `bl_CreateItemExample.Update` — RVA `0xccafc8`

- Lift status: **exact**; input span: 188 bytes; span to next metadata RVA: 188 bytes.
- Metadata signature: `private void Update() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=28 (informational only).

```csharp
public static ulong bl_CreateItemExample_Update_RVAccafc8(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
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
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x583UL))))))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xD8UL))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCCB008;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x570UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x583UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCCB008;
        label_0xCCB008:
        ;
        x0 = RuntimeMemory.ReadU64(x20);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x28UL))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCCB01C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCCB018UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCCB01C;
        label_0xCCB01C:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179568CUL /* metadata target: Object.op_Equality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCCB074;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x570UL))));
        x1 = 0x0UL;
        x0 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x17C7298UL /* metadata target: Input.GetButtonDown */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCCB050;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xCCB084UL /* metadata target: bl_CreateItemExample.CreateItem */, x0, x1, x2, x3);
        goto label_0xCCB050;
        label_0xCCB050:
        ;
        x0 = unchecked((ulong)(unchecked((uint)(0x68UL))));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17C7824UL /* metadata target: Input.GetKeyDown */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCCB074;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x28UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCCB080;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeDirect(0xCC8198UL /* metadata target: bl_MiniMap.DoHitEffect */);
        label_0xCCB074:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return x0;
        label_0xCCB080:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `bl_CreateItemExample.CreateItem` — RVA `0xccb084`

- Lift status: **exact**; input span: 468 bytes; span to next metadata RVA: 468 bytes.
- Metadata signature: `private void CreateItem() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=65 (informational only).

```csharp
public static ulong bl_CreateItemExample_CreateItem_RVAccb084(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_pair_address_13414536 = default(ulong);
        ulong __arm64_pair_address_13414540 = default(ulong);
        ulong __arm64_pair_address_13414544 = default(ulong);
        ulong __arm64_pair_address_13414628 = default(ulong);
        ulong __arm64_pair_address_13414688 = default(ulong);
        ulong __arm64_pair_address_13414744 = default(ulong);
        ulong __arm64_pair_address_13414944 = default(ulong);
        ulong __arm64_pair_address_13414976 = default(ulong);
        ulong __arm64_pair_address_13414980 = default(ulong);
        ulong __arm64_pair_address_13414984 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v10 = default(RuntimeVector128);
        RuntimeVector128 v11 = default(RuntimeVector128);
        RuntimeVector128 v12 = default(RuntimeVector128);
        RuntimeVector128 v13 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        RuntimeVector128 v9 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        sp = unchecked((ulong)((sp) - (0xD0UL)));
        __arm64_pair_address_13414536 = unchecked((ulong)((sp) + (0x80UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13414536, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v13.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13414536) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v12.GetUInt64(0)))));
        __arm64_pair_address_13414540 = unchecked((ulong)((sp) + (0x90UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13414540, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v11.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13414540) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v10.GetUInt64(0)))));
        __arm64_pair_address_13414544 = unchecked((ulong)((sp) + (0xA0UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13414544, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13414544) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xB0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xB0UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xC0UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xC0UL)))) + (0x8UL))), x19);
        x20 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x584UL))))))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCCB0D8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x398UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x4A8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB68UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x584UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCCB0D8;
        label_0xCCB0D8:
        ;
        v0 = (RuntimeVector128.Zero.WithUInt64(0, 0x0UL) | RuntimeVector128.Zero.WithUInt64(0, 0x0UL).ShiftLeftLogical(unchecked((int)0x40UL)));
        x0 = 0x0UL;
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x5CUL))), v0);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x5CUL))), v0);
#endif
        __arm64_pair_address_13414628 = unchecked((ulong)((sp) + (0x40UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13414628, v0);
#else
        __WriteVector128(__arm64_pair_address_13414628, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13414628) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13414628) + (0x10UL))), v0);
#endif
        x0 = RuntimeCalls.InvokeDirect(0x176F8DCUL /* metadata target: Camera.get_main */, x0, x1, x2, x3);
        x20 = x0;
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17C798CUL /* metadata target: Input.get_mousePosition */, x0, x1, x2, x3);
        if ((x20 == 0x0UL))
        {
            goto label_0xCCB254;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x21 = 0x1A8D000UL;
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x4A8UL))));
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x176F898UL /* metadata target: Camera.ScreenPointToRay */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((sp) + (0x3CUL))))));
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x34UL))));
        x0 = RuntimeMemory.ReadU64(x21);
        __arm64_pair_address_13414688 = unchecked((ulong)((sp) + (0x28UL)));
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13414688)), 0));
        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13414688) + (0x4UL))))), 0));
        v10 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((sp) + (0x30UL))))), 0));
        RuntimeMemory.WriteU32(unchecked((ulong)((sp) + (0x78UL))), unchecked((uint)(x8)));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x70UL))), x9);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x28UL))), x9);
        RuntimeMemory.WriteU32(unchecked((ulong)((sp) + (0x30UL))), unchecked((uint)(x8)));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCCB144;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCCB140UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCCB144;
        label_0xCCB144:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x28UL))));
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((sp) + (0x30UL))))));
        x0 = unchecked((ulong)((sp) + (0x10UL)));
        x1 = unchecked((ulong)((sp) + (0x40UL)));
        x2 = 0x0UL;
        __arm64_pair_address_13414744 = unchecked((ulong)((sp) + (0x10UL)));
        RuntimeMemory.WriteF32(__arm64_pair_address_13414744, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_13414744) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((sp) + (0x18UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x1CUL))), x8);
        RuntimeMemory.WriteU32(unchecked((ulong)((sp) + (0x24UL))), unchecked((uint)(x9)));
        x0 = RuntimeCalls.InvokeDirect(0x17CC300UL /* metadata target: Physics.Raycast */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCCB238;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = unchecked((ulong)((sp) + (0x40UL)));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17CED04UL /* metadata target: RaycastHit.get_point */, x0, x1, x2, x3);
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x398UL))));
        v11 = v0;
        v12 = v1;
        v13 = v2;
        x0 = RuntimeMemory.ReadU64(x8);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCCB1A0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCCB19CUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCCB1A0;
        label_0xCCB1A0:
        ;
        x8 = 0x3F80000000000000UL;
        x9 = unchecked((ulong)(unchecked((uint)(0x3F800000UL))));
        v0 = v8;
        v1 = v9;
        v2 = v10;
        x0 = 0x0UL;
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x0UL))), unchecked((ulong)(unchecked((uint)(x9)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x8UL))), x8);
        x0 = RuntimeCalls.InvokeDirect(0x1770690UL /* metadata target: Debug.DrawLine */, x0, x1, x2, x3);
        x0 = unchecked((ulong)((sp) + (0x40UL)));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17CED04UL /* metadata target: RaycastHit.get_point */, x0, x1, x2, x3);
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB68UL))));
        v8 = v0;
        v9 = v1;
        v10 = v2;
        x0 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x8 = 0x432000UL;
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((x8) + (0x9D0UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((x8) + (0x9D0UL))));
#endif
        x8 = unchecked((ulong)(unchecked((uint)(0x3333UL))));
        x8 = unchecked((ulong)(unchecked((uint)(unchecked((ulong)((unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((~(0xFFFFUL)))))))))) | (unchecked((ulong)((unchecked((ulong)((0x3F73UL) << (int)(unchecked((int)(0x10UL)))))) << (int)(unchecked((int)(0x0UL))))))))))));
        x9 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x1 = 0x0UL;
        x20 = x0;
        RuntimeMemory.WriteU32(unchecked((ulong)((x0) + (0x38UL))), unchecked((uint)(x8)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x0) + (0x28UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((x0) + (0x28UL))), v0);
#endif
        RuntimeMemory.WriteU32(unchecked((ulong)((x0) + (0x48UL))), unchecked((uint)(x9)));
        x0 = RuntimeCalls.InvokeDirect(0x1589338UL /* metadata target: Object.ctor */, x0, x1, x2, x3);
        __arm64_pair_address_13414944 = unchecked((ulong)((x20) + (0x10UL)));
        RuntimeMemory.WriteF32(__arm64_pair_address_13414944, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_13414944) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((x20) + (0x18UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x28UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCCB254;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xCC8290UL /* metadata target: bl_MiniMap.CreateNewItem */, x0, x1, x2, x3);
        goto label_0xCCB238;
        label_0xCCB238:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0xC0UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xC0UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0xB0UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xB0UL)))) + (0x8UL))));
        __arm64_pair_address_13414976 = unchecked((ulong)((sp) + (0xA0UL)));
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13414976)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13414976) + (0x8UL))))), 0));
        __arm64_pair_address_13414980 = unchecked((ulong)((sp) + (0x90UL)));
        v11 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13414980)), 0));
        v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13414980) + (0x8UL))))), 0));
        __arm64_pair_address_13414984 = unchecked((ulong)((sp) + (0x80UL)));
        v13 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13414984)), 0));
        v12 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13414984) + (0x8UL))))), 0));
        return x0;
        label_0xCCB254:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `bl_CreateItemExample.ctor` — RVA `0xccb258`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public void .ctor() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static ulong bl_CreateItemExample_ctor_RVAccb258(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x1 = 0x0UL;
        return RuntimeCalls.InvokeDirect(0x1796274UL /* metadata target: MonoBehaviour.ctor */);
        return default(ulong);
    }
```
