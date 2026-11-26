# `BloomModel` — TypeDefIndex 3556

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x18` | `BloomModel.Settings` | `m_Settings` |

## `BloomModel.get_settings` — RVA `0xcdb0b8`

- Lift status: **exact**; input span: 24 bytes; span to next metadata RVA: 24 bytes.
- Metadata signature: `public BloomModel.Settings get_settings() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static ulong BloomModel_get_settings_RVAcdb0b8(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_pair_address_13480136 = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x38UL))));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((x0) + (0x28UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((x0) + (0x28UL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((x0) + (0x18UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((x0) + (0x18UL))));
#endif
        RuntimeMemory.WriteU64(unchecked((ulong)((x8) + (0x20UL))), x9);
        __arm64_pair_address_13480136 = x8;
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13480136, v1);
#else
        __WriteVector128(__arm64_pair_address_13480136, v1);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13480136) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13480136) + (0x10UL))), v0);
#endif
        return x0;
        return default(ulong);
    }
```

## `BloomModel.set_settings` — RVA `0xcdb0d0`

- Lift status: **exact**; input span: 36 bytes; span to next metadata RVA: 36 bytes.
- Metadata signature: `public void set_settings(BloomModel.Settings value) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=4 (informational only).

```csharp
public static ulong BloomModel_set_settings_RVAcdb0d0(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_pair_address_13480148 = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x1) + (0x20UL))));
        __arm64_pair_address_13480148 = x1;
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(__arm64_pair_address_13480148);
#else
        v1 = __ReadVector128(__arm64_pair_address_13480148);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13480148) + (0x10UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13480148) + (0x10UL))));
#endif
        x8 = unchecked((ulong)((x0) + (0x30UL)));
        x1 = 0x0UL;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x38UL))), x9);
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x0) + (0x28UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((x0) + (0x28UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x0) + (0x18UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((x0) + (0x18UL))), v1);
#endif
        x0 = x8;
        return RuntimeCalls.InvokeDirect(0xB7D8D0UL);
        return default(ulong);
    }
```

## `BloomModel.Reset` — RVA `0xcdb0f4`

- Lift status: **exact**; input span: 64 bytes; span to next metadata RVA: 64 bytes.
- Metadata signature: `public override void Reset() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=8 (informational only).

```csharp
public static ulong BloomModel_Reset_RVAcdb0f4(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        sp = unchecked((ulong)((sp) - (0x40UL)));
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))), x19);
        x19 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xCDB134UL /* metadata target: BloomModel.Settings.get_defaultSettings */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x28UL))));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x18UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((sp) + (0x18UL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x8UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((sp) + (0x8UL))));
#endif
        x0 = unchecked((ulong)((x19) + (0x30UL)));
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x38UL))), x8);
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x19) + (0x28UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((x19) + (0x28UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x19) + (0x18UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((x19) + (0x18UL))), v1);
#endif
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))));
        x1 = 0x0UL;
        sp = unchecked((ulong)((sp) + (0x40UL)));
        return RuntimeCalls.InvokeDirect(0xB7D8D0UL);
        return default(ulong);
    }
```

## `BloomModel.ctor` — RVA `0xcdb1ac`

- Lift status: **exact**; input span: 76 bytes; span to next metadata RVA: 76 bytes.
- Metadata signature: `public void .ctor() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=10 (informational only).

```csharp
public static ulong BloomModel_ctor_RVAcdb1ac(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        sp = unchecked((ulong)((sp) - (0x40UL)));
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))), x19);
        x19 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xCDB134UL /* metadata target: BloomModel.Settings.get_defaultSettings */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x28UL))));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x18UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((sp) + (0x18UL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x8UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((sp) + (0x8UL))));
#endif
        x0 = unchecked((ulong)((x19) + (0x30UL)));
        x1 = 0x0UL;
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x38UL))), x8);
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x19) + (0x28UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((x19) + (0x28UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x19) + (0x18UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((x19) + (0x18UL))), v1);
#endif
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = x19;
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))));
        x1 = 0x0UL;
        sp = unchecked((ulong)((sp) + (0x40UL)));
        return RuntimeCalls.InvokeDirect(0xCDE564UL /* metadata target: PostProcessingModel.ctor */);
        return default(ulong);
    }
```
