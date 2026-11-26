# `DitheringModel` — TypeDefIndex 3579

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x11` | `DitheringModel.Settings` | `m_Settings` |

## `DitheringModel.get_settings` — RVA `0xcdbd7c`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public DitheringModel.Settings get_settings() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static uint DitheringModel_get_settings_RVAcdbd7c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x0 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x11UL))))))));
        return unchecked((uint)(x0));
        return default(uint);
    }
```

## `DitheringModel.set_settings` — RVA `0xcdbd84`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public void set_settings(DitheringModel.Settings value) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=0 (informational only).

```csharp
public static ulong DitheringModel_set_settings_RVAcdbd84(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        RuntimeMemory.WriteU8(unchecked((ulong)((x0) + (0x11UL))), unchecked((byte)(unchecked((uint)(x1)))));
        return x0;
        return default(ulong);
    }
```

## `DitheringModel.Reset` — RVA `0xcdbd8c`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public override void Reset() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=0 (informational only).

```csharp
public static ulong DitheringModel_Reset_RVAcdbd8c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        RuntimeMemory.WriteU8(unchecked((ulong)((x0) + (0x11UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        return x0;
        return default(ulong);
    }
```

## `DitheringModel.ctor` — RVA `0xcdbd9c`

- Lift status: **exact**; input span: 12 bytes; span to next metadata RVA: 12 bytes.
- Metadata signature: `public void .ctor() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static ulong DitheringModel_ctor_RVAcdbd9c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x1 = 0x0UL;
        RuntimeMemory.WriteU8(unchecked((ulong)((x0) + (0x11UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        return RuntimeCalls.InvokeDirect(0xCDE564UL /* metadata target: PostProcessingModel.ctor */);
        return default(ulong);
    }
```
