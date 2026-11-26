# `AntialiasingModel` — TypeDefIndex 3552

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x14` | `AntialiasingModel.Settings` | `m_Settings` |

## `AntialiasingModel.get_settings` — RVA `0xcdae1c`

- Lift status: **exact**; input span: 20 bytes; span to next metadata RVA: 20 bytes.
- Metadata signature: `public AntialiasingModel.Settings get_settings() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static ulong AntialiasingModel_get_settings_RVAcdae1c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        RuntimeVector128 v0 = default(RuntimeVector128);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x24UL))));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((x0) + (0x14UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((x0) + (0x14UL))));
#endif
        RuntimeMemory.WriteU64(unchecked((ulong)((x8) + (0x10UL))), x9);
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(x8, v0);
#else
        __WriteVector128(x8, v0);
#endif
        return x0;
        return default(ulong);
    }
```

## `AntialiasingModel.set_settings` — RVA `0xcdae30`

- Lift status: **exact**; input span: 20 bytes; span to next metadata RVA: 20 bytes.
- Metadata signature: `public void set_settings(AntialiasingModel.Settings value) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static ulong AntialiasingModel_set_settings_RVAcdae30(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        RuntimeVector128 v0 = default(RuntimeVector128);
        ulong x8 = default(ulong);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x1) + (0x10UL))));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(x1);
#else
        v0 = __ReadVector128(x1);
#endif
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x24UL))), x8);
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x0) + (0x14UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((x0) + (0x14UL))), v0);
#endif
        return x0;
        return default(ulong);
    }
```

## `AntialiasingModel.Reset` — RVA `0xcdae44`

- Lift status: **exact**; input span: 28 bytes; span to next metadata RVA: 28 bytes.
- Metadata signature: `public override void Reset() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=2 (informational only).

```csharp
public static ulong AntialiasingModel_Reset_RVAcdae44(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        x8 = 0x431000UL;
        x9 = 0x433000UL;
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((x8) + (0xBD8UL))))), 0));
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((x9) + (0x1F0UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((x9) + (0x1F0UL))));
#endif
        RuntimeMemory.WriteF64(unchecked((ulong)((x0) + (0x14UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x0) + (0x1CUL))), v1);
#else
        __WriteVector128(unchecked((ulong)((x0) + (0x1CUL))), v1);
#endif
        return x0;
        return default(ulong);
    }
```

## `AntialiasingModel.ctor` — RVA `0xcdae7c`

- Lift status: **exact**; input span: 32 bytes; span to next metadata RVA: 32 bytes.
- Metadata signature: `public void .ctor() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=3 (informational only).

```csharp
public static ulong AntialiasingModel_ctor_RVAcdae7c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        x8 = 0x431000UL;
        x9 = 0x433000UL;
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((x8) + (0xBD8UL))))), 0));
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((x9) + (0x1F0UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((x9) + (0x1F0UL))));
#endif
        x1 = 0x0UL;
        RuntimeMemory.WriteF64(unchecked((ulong)((x0) + (0x14UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x0) + (0x1CUL))), v1);
#else
        __WriteVector128(unchecked((ulong)((x0) + (0x1CUL))), v1);
#endif
        return RuntimeCalls.InvokeDirect(0xCDE564UL /* metadata target: PostProcessingModel.ctor */);
        return default(ulong);
    }
```
