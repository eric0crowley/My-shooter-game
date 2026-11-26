# `AmbientOcclusionModel` — TypeDefIndex 3544

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x14` | `AmbientOcclusionModel.Settings` | `m_Settings` |

## `AmbientOcclusionModel.get_settings` — RVA `0xcdadc4`

- Lift status: **exact**; input span: 16 bytes; span to next metadata RVA: 16 bytes.
- Metadata signature: `public AmbientOcclusionModel.Settings get_settings() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=3 (informational only).

```csharp
public static ulong AmbientOcclusionModel_get_settings_RVAcdadc4(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong x8 = default(ulong);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x14UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x1CUL))));
        x0 = x8;
        return x0;
        return default(ulong);
    }
```

## `AmbientOcclusionModel.set_settings` — RVA `0xcdadd4`

- Lift status: **exact**; input span: 12 bytes; span to next metadata RVA: 12 bytes.
- Metadata signature: `public void set_settings(AmbientOcclusionModel.Settings value) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=0 (informational only).

```csharp
public static ulong AmbientOcclusionModel_set_settings_RVAcdadd4(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x14UL))), x1);
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x1CUL))), x2);
        return x0;
        return default(ulong);
    }
```

## `AmbientOcclusionModel.Reset` — RVA `0xcdade0`

- Lift status: **exact**; input span: 16 bytes; span to next metadata RVA: 16 bytes.
- Metadata signature: `public override void Reset() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static ulong AmbientOcclusionModel_Reset_RVAcdade0(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        RuntimeVector128 v0 = default(RuntimeVector128);
        ulong x8 = default(ulong);
        x8 = 0x432000UL;
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((x8) + (0xD00UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((x8) + (0xD00UL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x0) + (0x14UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((x0) + (0x14UL))), v0);
#endif
        return x0;
        return default(ulong);
    }
```

## `AmbientOcclusionModel.ctor` — RVA `0xcdae08`

- Lift status: **exact**; input span: 20 bytes; span to next metadata RVA: 20 bytes.
- Metadata signature: `public void .ctor() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=2 (informational only).

```csharp
public static ulong AmbientOcclusionModel_ctor_RVAcdae08(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        RuntimeVector128 v0 = default(RuntimeVector128);
        ulong x8 = default(ulong);
        x8 = 0x432000UL;
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((x8) + (0xD00UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((x8) + (0xD00UL))));
#endif
        x1 = 0x0UL;
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x0) + (0x14UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((x0) + (0x14UL))), v0);
#endif
        return RuntimeCalls.InvokeDirect(0xCDE564UL /* metadata target: PostProcessingModel.ctor */);
        return default(ulong);
    }
```
