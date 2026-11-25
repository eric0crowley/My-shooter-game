# `PressureLevelBinding` — TypeDefIndex 5132

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x20` | `InputRig` | `rig` |
| `0x28` | `string` | `sourceAxis` |
| `0x30` | `int` | `sourceAxisId` |
| `0x38` | `List<PressureLevelBinding.RangeConfig>` | `rangeConfigList` |

## `PressureLevelBinding.ctor` — RVA `0xc686e4`

- Lift status: **exact**; input span: 288 bytes; span to next metadata RVA: 288 bytes.
- Metadata signature: `public void .ctor() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=44 (informational only).

```csharp
public static ulong PressureLevelBinding_ctor_RVAc686e4(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
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
        x22 = 0x1BAB000UL;
        x21 = 0x1A8D000UL;
        x20 = 0x1A8D000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x22) + (0x31CUL))))))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x260UL))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x268UL))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC68748;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x270UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x278UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x260UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x268UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x22) + (0x31CUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC68748;
        label_0xC68748:
        ;
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1796274UL /* metadata target: MonoBehaviour.ctor */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x21);
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D9D4UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = RuntimeMemory.ReadU64(x20);
        x20 = x0;
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x21 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC68804UL /* metadata target: PressureLevelBinding.RangeConfig.ctor */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        if ((x20 == 0x0UL))
        {
            goto label_0xC687F0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC6877CUL);
        }
        if ((x21 == 0x0UL))
        {
            goto label_0xC68794;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x20);
        x0 = x21;
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x40UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7DA60UL, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC687F8;
        }
        else
        {
            goto label_0xC68794;
        }
        label_0xC68794:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x20) + (0x18UL))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC687F4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x22 = 0x1A8D000UL;
        x23 = 0x1A8D000UL;
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x278UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0x270UL))));
        x0 = x20;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x20UL))), x21);
        x1 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x22);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x2 = RuntimeMemory.ReadU64(x23);
        x1 = x20;
        x21 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x10A2C8CUL, x0, x1, x2, x3);
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x38UL))), x21);
        x0 = x19;
        x1 = x21;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeDirect(0xB7D8D0UL);
        label_0xC687F0:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        goto label_0xC687F4;
        label_0xC687F4:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB7CUL, x0, x1, x2, x3);
        goto label_0xC687F8;
        label_0xC687F8:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB98UL, x0, x1, x2, x3);
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xB7DA4CUL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `PressureLevelBinding.OnEnable` — RVA `0xc68870`

- Lift status: **exact**; input span: 312 bytes; span to next metadata RVA: 312 bytes.
- Metadata signature: `private void OnEnable() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=52 (informational only).

```csharp
public static ulong PressureLevelBinding_OnEnable_RVAc68870(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
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
        x20 = 0x1BAB000UL;
        x22 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x31DUL))))))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0xD8UL))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC688CC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x40UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xE18UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x280UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x31DUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC688CC;
        label_0xC688CC:
        ;
        x20 = x19;
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x20UL))));
        x0 = RuntimeMemory.ReadU64(x22);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC688E4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC688E0UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC688E4;
        label_0xC688E4:
        ;
        x0 = x21;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179568CUL /* metadata target: Object.op_Equality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC6891C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xE18UL))));
        x0 = x19;
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xE3204CUL, x0, x1, x2, x3);
        x1 = x0;
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x20UL))), x0);
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        goto label_0xC6891C;
        label_0xC6891C:
        ;
        x0 = RuntimeMemory.ReadU64(x22);
        x20 = RuntimeMemory.ReadU64(x20);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC68930;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC6892CUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC68930;
        label_0xC68930:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794AC8UL /* metadata target: Object.op_Inequality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC68994;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8C000UL;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x20UL))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x40UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x280UL))));
        x1 = x19;
        x3 = 0x0UL;
        x21 = x0;
        x2 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x14E3EACUL /* metadata target: Action.ctor */, x0, x1, x2, x3);
        if ((x20 == 0x0UL))
        {
            goto label_0xC689A4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x20;
        x1 = x21;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x2 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0xC39504UL /* metadata target: InputRig.add_onAddExtraInput */);
        label_0xC68994:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        label_0xC689A4:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `PressureLevelBinding.OnDisable` — RVA `0xc689a8`

- Lift status: **exact**; input span: 208 bytes; span to next metadata RVA: 208 bytes.
- Metadata signature: `private void OnDisable() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=35 (informational only).

```csharp
public static ulong PressureLevelBinding_OnDisable_RVAc689a8(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
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
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x31EUL))))))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xD8UL))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC689F4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x40UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x280UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x31EUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC689F4;
        label_0xC689F4:
        ;
        x0 = RuntimeMemory.ReadU64(x20);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x20UL))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC68A08;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC68A04UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC68A08;
        label_0xC68A08:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794AC8UL /* metadata target: Object.op_Inequality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC68A68;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8C000UL;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x20UL))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x40UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x280UL))));
        x1 = x19;
        x3 = 0x0UL;
        x21 = x0;
        x2 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x14E3EACUL /* metadata target: Action.ctor */, x0, x1, x2, x3);
        if ((x20 == 0x0UL))
        {
            goto label_0xC68A74;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x20;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x1 = x21;
        x2 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeDirect(0xC395A0UL /* metadata target: InputRig.remove_onAddExtraInput */);
        label_0xC68A68:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return x0;
        label_0xC68A74:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `PressureLevelBinding.UpdateRanges` — RVA `0xc68a78`

- Lift status: **exact**; input span: 256 bytes; span to next metadata RVA: 256 bytes.
- Metadata signature: `protected void UpdateRanges() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=38 (informational only).

```csharp
public static ulong PressureLevelBinding_UpdateRanges_RVAc68a78(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13011780 = default(uint);
        uint __arm64_flags_right_13011780 = default(uint);
        ulong __arm64_load_address_13011720 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
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
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x31FUL))))))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xD8UL))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC68AC8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x288UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x290UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x31FUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC68AC8;
        label_0xC68AC8:
        ;
        x0 = RuntimeMemory.ReadU64(x20);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x20UL))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC68ADC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC68AD8UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC68ADC;
        label_0xC68ADC:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179568CUL /* metadata target: Object.op_Equality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC68B00;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x28UL))));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x13F6920UL /* metadata target: String.IsNullOrEmpty */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC68B10;
        }
        else
        {
            goto label_0xC68B00;
        }
        label_0xC68B00:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        __arm64_load_address_13011720 = sp;
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_load_address_13011720)), 0));
        return x0;
        label_0xC68B10:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x20UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC68B74;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x28UL))));
        x2 = unchecked((ulong)((x19) + (0x30UL)));
        x3 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC36308UL /* metadata target: InputRig.GetAxisRaw */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x38UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC68B74;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x21 = 0x1A8D000UL;
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x290UL))));
        v8 = v0;
        x20 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xC68B40;
        label_0xC68B40:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x18UL))))));
        __arm64_flags_left_13011780 = unchecked((uint)(x20));
        __arm64_flags_right_13011780 = unchecked((uint)(x8));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13011780) - (__arm64_flags_right_13011780))))) < unchecked((int)0x0UL)) == (((unchecked((int)(__arm64_flags_left_13011780)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13011780)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13011780) - (__arm64_flags_right_13011780))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13011780)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC68B00;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x2 = RuntimeMemory.ReadU64(x21);
        x1 = unchecked((ulong)(unchecked((uint)(x20))));
        x0 = RuntimeCalls.InvokeDirect(0x10A30C0UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC68B74;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x20UL))));
        x0 = RuntimeCalls.InvokeDirect(0xC68B78UL /* metadata target: PressureLevelBinding.RangeConfig.Update */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x38UL))));
        x20 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x20))) + (unchecked((uint)(0x1UL)))))));
        if ((x0 != 0x0UL))
        {
            goto label_0xC68B40;
        }
        else
        {
            goto label_0xC68B74;
        }
        label_0xC68B74:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```
