# `PostProcessingComponentBase` — TypeDefIndex 3602

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x10` | `PostProcessingContext` | `context` |

## `PostProcessingComponentBase.GetCameraFlags` — RVA `0xcde410`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public virtual DepthTextureMode GetCameraFlags() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static uint PostProcessingComponentBase_GetCameraFlags_RVAcde410(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
        return unchecked((uint)(x0));
        return default(uint);
    }
```

## `PostProcessingComponentBase.OnEnable` — RVA `0xcde418`

- Lift status: **exact**; input span: 4 bytes; span to next metadata RVA: 4 bytes.
- Metadata signature: `public virtual void OnEnable() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=0 (informational only).

```csharp
public static ulong PostProcessingComponentBase_OnEnable_RVAcde418(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        return x0;
        return default(ulong);
    }
```

## `PostProcessingComponentBase.OnDisable` — RVA `0xcde41c`

- Lift status: **exact**; input span: 4 bytes; span to next metadata RVA: 4 bytes.
- Metadata signature: `public virtual void OnDisable() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=0 (informational only).

```csharp
public static ulong PostProcessingComponentBase_OnDisable_RVAcde41c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        return x0;
        return default(ulong);
    }
```

## `PostProcessingComponentBase.ctor` — RVA `0xcde420`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `protected void .ctor() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static ulong PostProcessingComponentBase_ctor_RVAcde420(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x1 = 0x0UL;
        return RuntimeCalls.InvokeDirect(0x1589338UL /* metadata target: Object.ctor */);
        return default(ulong);
    }
```
