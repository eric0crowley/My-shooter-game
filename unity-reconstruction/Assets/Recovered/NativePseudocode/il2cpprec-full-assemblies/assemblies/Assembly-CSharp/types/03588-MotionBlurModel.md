# `MotionBlurModel` — TypeDefIndex 3588

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x14` | `MotionBlurModel.Settings` | `m_Settings` |

## `MotionBlurModel.get_settings` — RVA `0xcdbf34`

- Lift status: **exact**; input span: 16 bytes; span to next metadata RVA: 16 bytes.
- Metadata signature: `public MotionBlurModel.Settings get_settings() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=3 (informational only).

```csharp
public static ulong MotionBlurModel_get_settings_RVAcdbf34(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong x8 = default(ulong);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x14UL))));
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x1CUL))))));
        x0 = x8;
        return x0;
        return default(ulong);
    }
```

## `MotionBlurModel.set_settings` — RVA `0xcdbf44`

- Lift status: **exact**; input span: 12 bytes; span to next metadata RVA: 12 bytes.
- Metadata signature: `public void set_settings(MotionBlurModel.Settings value) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=0 (informational only).

```csharp
public static ulong MotionBlurModel_set_settings_RVAcdbf44(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x14UL))), x1);
        RuntimeMemory.WriteU32(unchecked((ulong)((x0) + (0x1CUL))), unchecked((uint)(x2)));
        return x0;
        return default(ulong);
    }
```

## `MotionBlurModel.Reset` — RVA `0xcdbf50`

- Lift status: **exact**; input span: 20 bytes; span to next metadata RVA: 20 bytes.
- Metadata signature: `public override void Reset() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=2 (informational only).

```csharp
public static ulong MotionBlurModel_Reset_RVAcdbf50(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong x8 = default(ulong);
        x8 = 0x43870000UL;
        x8 = unchecked((ulong)((unchecked((ulong)((x8) & ((~(0xFFFFUL)))))) | (unchecked((ulong)((unchecked((ulong)((0xAUL) << (int)(unchecked((int)(0x20UL)))))) << (int)(unchecked((int)(0x0UL))))))));
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x14UL))), x8);
        RuntimeMemory.WritePtr(unchecked((ulong)((x0) + (0x1CUL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        return x0;
        return default(ulong);
    }
```

## `MotionBlurModel.ctor` — RVA `0xcdbf74`

- Lift status: **exact**; input span: 24 bytes; span to next metadata RVA: 24 bytes.
- Metadata signature: `public void .ctor() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=3 (informational only).

```csharp
public static ulong MotionBlurModel_ctor_RVAcdbf74(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong x8 = default(ulong);
        x8 = 0x43870000UL;
        x8 = unchecked((ulong)((unchecked((ulong)((x8) & ((~(0xFFFFUL)))))) | (unchecked((ulong)((unchecked((ulong)((0xAUL) << (int)(unchecked((int)(0x20UL)))))) << (int)(unchecked((int)(0x0UL))))))));
        x1 = 0x0UL;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x14UL))), x8);
        RuntimeMemory.WritePtr(unchecked((ulong)((x0) + (0x1CUL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        return RuntimeCalls.InvokeDirect(0xCDE564UL /* metadata target: PostProcessingModel.ctor */);
        return default(ulong);
    }
```
