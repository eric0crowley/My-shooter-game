# `UserLutModel` — TypeDefIndex 3597

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x18` | `UserLutModel.Settings` | `m_Settings` |

## `UserLutModel.get_settings` — RVA `0xcdc0c4`

- Lift status: **exact**; input span: 12 bytes; span to next metadata RVA: 12 bytes.
- Metadata signature: `public UserLutModel.Settings get_settings() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=2 (informational only).

```csharp
public static ulong UserLutModel_get_settings_RVAcdc0c4(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong x8 = default(ulong);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x18UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x0) + (0x18UL)))) + (0x8UL))));
        x0 = x8;
        return x0;
        return default(ulong);
    }
```

## `UserLutModel.set_settings` — RVA `0xcdc0d0`

- Lift status: **exact**; input span: 16 bytes; span to next metadata RVA: 16 bytes.
- Metadata signature: `public void set_settings(UserLutModel.Settings value) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static ulong UserLutModel_set_settings_RVAcdc0d0(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x18UL))), x1);
        x1 = 0x0UL;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x8UL))), x2);
        return RuntimeCalls.InvokeDirect(0xB7D8D0UL);
        return default(ulong);
    }
```

## `UserLutModel.Reset` — RVA `0xcdc0e0`

- Lift status: **exact**; input span: 72 bytes; span to next metadata RVA: 72 bytes.
- Metadata signature: `public override void Reset() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=10 (informational only).

```csharp
public static ulong UserLutModel_Reset_RVAcdc0e0(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        sp = unchecked((ulong)((sp) - (0x20UL)));
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        x19 = x0;
        x0 = sp;
        x1 = 0x0UL;
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0x0UL))), 0x0UL);
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0x8UL))), 0x0UL);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x3F800000UL))));
        RuntimeMemory.WriteU32(unchecked((ulong)((sp) + (0x8UL))), unchecked((uint)(x8)));
        x8 = RuntimeMemory.ReadU64(sp);
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        x1 = 0x0UL;
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x18UL))), x8);
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x8UL))), x9);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        return x0;
        return default(ulong);
    }
```

## `UserLutModel.ctor` — RVA `0xcdc158`

- Lift status: **exact**; input span: 84 bytes; span to next metadata RVA: 84 bytes.
- Metadata signature: `public void .ctor() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=12 (informational only).

```csharp
public static ulong UserLutModel_ctor_RVAcdc158(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        sp = unchecked((ulong)((sp) - (0x20UL)));
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        x19 = x0;
        x0 = sp;
        x1 = 0x0UL;
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0x0UL))), 0x0UL);
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0x8UL))), 0x0UL);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x3F800000UL))));
        RuntimeMemory.WriteU32(unchecked((ulong)((sp) + (0x8UL))), unchecked((uint)(x8)));
        x8 = RuntimeMemory.ReadU64(sp);
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        x0 = x19;
        x1 = 0x0UL;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x18UL))), x8);
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x20UL))), x9);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xCDE564UL /* metadata target: PostProcessingModel.ctor */, x0, x1, x2, x3);
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        return x0;
        return default(ulong);
    }
```
