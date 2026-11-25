# `FogModel` — TypeDefIndex 3584

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x11` | `FogModel.Settings` | `m_Settings` |

## `FogModel.get_settings` — RVA `0xcdbea8`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public FogModel.Settings get_settings() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static uint FogModel_get_settings_RVAcdbea8(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x0 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x11UL))))))));
        return unchecked((uint)(x0));
        return default(uint);
    }
```

## `FogModel.set_settings` — RVA `0xcdbeb0`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public void set_settings(FogModel.Settings value) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=0 (informational only).

```csharp
public static ulong FogModel_set_settings_RVAcdbeb0(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        RuntimeMemory.WriteU8(unchecked((ulong)((x0) + (0x11UL))), unchecked((byte)(unchecked((uint)(x1)))));
        return x0;
        return default(ulong);
    }
```

## `FogModel.Reset` — RVA `0xcdbeb8`

- Lift status: **exact**; input span: 12 bytes; span to next metadata RVA: 12 bytes.
- Metadata signature: `public override void Reset() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static ulong FogModel_Reset_RVAcdbeb8(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong x8 = default(ulong);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x0) + (0x11UL))), unchecked((byte)(unchecked((uint)(x8)))));
        return x0;
        return default(ulong);
    }
```

## `FogModel.ctor` — RVA `0xcdbecc`

- Lift status: **exact**; input span: 16 bytes; span to next metadata RVA: 16 bytes.
- Metadata signature: `public void .ctor() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=2 (informational only).

```csharp
public static ulong FogModel_ctor_RVAcdbecc(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong x8 = default(ulong);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x1 = 0x0UL;
        RuntimeMemory.WriteU8(unchecked((ulong)((x0) + (0x11UL))), unchecked((byte)(unchecked((uint)(x8)))));
        return RuntimeCalls.InvokeDirect(0xCDE564UL /* metadata target: PostProcessingModel.ctor */);
        return default(ulong);
    }
```
