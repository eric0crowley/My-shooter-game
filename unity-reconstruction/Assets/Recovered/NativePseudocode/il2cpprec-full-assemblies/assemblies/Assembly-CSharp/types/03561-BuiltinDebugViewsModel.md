# `BuiltinDebugViewsModel` — TypeDefIndex 3561

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x14` | `BuiltinDebugViewsModel.Settings` | `m_Settings` |

## `BuiltinDebugViewsModel.IsModeActive` — RVA `0xccdb34`

- Lift status: **exact**; input span: 16 bytes; span to next metadata RVA: 16 bytes.
- Metadata signature: `public bool IsModeActive(BuiltinDebugViewsModel.Mode mode) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static uint BuiltinDebugViewsModel_IsModeActive_RVAccdb34(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13425464 = default(uint);
        uint __arm64_flags_right_13425464 = default(uint);
        ulong x8 = default(ulong);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x14UL))))));
        __arm64_flags_left_13425464 = unchecked((uint)(x8));
        __arm64_flags_right_13425464 = unchecked((uint)(x1));
        x0 = unchecked((ulong)(((unchecked((uint)((__arm64_flags_left_13425464) - (__arm64_flags_right_13425464))) == unchecked((uint)0x0UL)) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        return unchecked((uint)(x0));
        return default(uint);
    }
```

## `BuiltinDebugViewsModel.get_settings` — RVA `0xcdb260`

- Lift status: **exact**; input span: 16 bytes; span to next metadata RVA: 16 bytes.
- Metadata signature: `public BuiltinDebugViewsModel.Settings get_settings() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=0 (informational only).

```csharp
public static ulong BuiltinDebugViewsModel_get_settings_RVAcdb260(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_pair_address_13480552 = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        ulong x8 = default(ulong);
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((x0) + (0x24UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((x0) + (0x24UL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((x0) + (0x14UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((x0) + (0x14UL))));
#endif
        __arm64_pair_address_13480552 = x8;
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13480552, v1);
#else
        __WriteVector128(__arm64_pair_address_13480552, v1);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13480552) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13480552) + (0x10UL))), v0);
#endif
        return x0;
        return default(ulong);
    }
```

## `BuiltinDebugViewsModel.set_settings` — RVA `0xcdb270`

- Lift status: **exact**; input span: 16 bytes; span to next metadata RVA: 16 bytes.
- Metadata signature: `public void set_settings(BuiltinDebugViewsModel.Settings value) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=0 (informational only).

```csharp
public static ulong BuiltinDebugViewsModel_set_settings_RVAcdb270(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_pair_address_13480560 = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        __arm64_pair_address_13480560 = x1;
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(__arm64_pair_address_13480560);
#else
        v1 = __ReadVector128(__arm64_pair_address_13480560);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13480560) + (0x10UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13480560) + (0x10UL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x0) + (0x24UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((x0) + (0x24UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x0) + (0x14UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((x0) + (0x14UL))), v1);
#endif
        return x0;
        return default(ulong);
    }
```

## `BuiltinDebugViewsModel.get_willInterrupt` — RVA `0xcdb280`

- Lift status: **exact**; input span: 36 bytes; span to next metadata RVA: 36 bytes.
- Metadata signature: `public bool get_willInterrupt() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=5 (informational only).

```csharp
public static uint BuiltinDebugViewsModel_get_willInterrupt_RVAcdb280(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13480580 = default(uint);
        uint __arm64_flags_right_13480580 = default(uint);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x14UL))))));
        __arm64_flags_left_13480580 = unchecked((uint)(x8));
        __arm64_flags_right_13480580 = unchecked((uint)0x9UL);
        if (((__arm64_flags_left_13480580 >= __arm64_flags_right_13480580) && (!((unchecked((uint)((__arm64_flags_left_13480580) - (__arm64_flags_right_13480580))) == unchecked((uint)0x0UL))))))
        {
            label_0xCDB29C:
            ;
            x0 = unchecked((ulong)(unchecked((uint)(0x1UL))));
            return unchecked((uint)(x0));
        }
        else
        {
            x9 = unchecked((ulong)(unchecked((uint)(0x5EUL))));
            x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) >> (int)(unchecked((int)(unchecked((uint)(x8)))))))));
            x0 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)(0x1UL)))))));
            return unchecked((uint)(x0));
        }
        return default(uint);
    }
```

## `BuiltinDebugViewsModel.Reset` — RVA `0xcdb2a4`

- Lift status: **exact**; input span: 40 bytes; span to next metadata RVA: 40 bytes.
- Metadata signature: `public override void Reset() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=4 (informational only).

```csharp
public static ulong BuiltinDebugViewsModel_Reset_RVAcdb2a4(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        RuntimeVector128 v0 = default(RuntimeVector128);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        x8 = 0x432000UL;
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((x8) + (0xC70UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((x8) + (0xC70UL))));
#endif
        x8 = 0x3F800000UL;
        x8 = unchecked((ulong)((unchecked((ulong)((x8) & ((~(0xFFFFUL)))))) | (unchecked((ulong)((unchecked((ulong)((0x18UL) << (int)(unchecked((int)(0x20UL)))))) << (int)(unchecked((int)(0x0UL))))))));
        x9 = unchecked((ulong)(unchecked((uint)(0x42800000UL))));
        RuntimeMemory.WritePtr(unchecked((ulong)((x0) + (0x14UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x28UL))), x8);
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x0) + (0x18UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((x0) + (0x18UL))), v0);
#endif
        RuntimeMemory.WriteU32(unchecked((ulong)((x0) + (0x30UL))), unchecked((uint)(x9)));
        return x0;
        return default(ulong);
    }
```

## `BuiltinDebugViewsModel.ctor` — RVA `0xcdb2f4`

- Lift status: **exact**; input span: 44 bytes; span to next metadata RVA: 44 bytes.
- Metadata signature: `public void .ctor() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=5 (informational only).

```csharp
public static ulong BuiltinDebugViewsModel_ctor_RVAcdb2f4(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        RuntimeVector128 v0 = default(RuntimeVector128);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        x8 = 0x432000UL;
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((x8) + (0xC70UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((x8) + (0xC70UL))));
#endif
        x8 = 0x3F800000UL;
        x8 = unchecked((ulong)((unchecked((ulong)((x8) & ((~(0xFFFFUL)))))) | (unchecked((ulong)((unchecked((ulong)((0x18UL) << (int)(unchecked((int)(0x20UL)))))) << (int)(unchecked((int)(0x0UL))))))));
        x9 = unchecked((ulong)(unchecked((uint)(0x42800000UL))));
        x1 = 0x0UL;
        RuntimeMemory.WritePtr(unchecked((ulong)((x0) + (0x14UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x28UL))), x8);
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x0) + (0x18UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((x0) + (0x18UL))), v0);
#endif
        RuntimeMemory.WriteU32(unchecked((ulong)((x0) + (0x30UL))), unchecked((uint)(x9)));
        return RuntimeCalls.InvokeDirect(0xCDE564UL /* metadata target: PostProcessingModel.ctor */);
        return default(ulong);
    }
```
