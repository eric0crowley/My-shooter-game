# `DigitalBinding.<>c__DisplayClass20_0` — TypeDefIndex 5072

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x10` | `string` | `axisName` |

## `DigitalBinding.<>c__DisplayClass20_0.ctor` — RVA `0xc5c9b4`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public void .ctor() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static ulong DigitalBinding_c__DisplayClass20_0_ctor_RVAc5c9b4(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x1 = 0x0UL;
        return RuntimeCalls.InvokeDirect(0x1589338UL /* metadata target: Object.ctor */);
        return default(ulong);
    }
```

## `DigitalBinding.<>c__DisplayClass20_0.<OnIsBoundToAxis>b__0` — RVA `0xc5c9c8`

- Lift status: **exact**; input span: 36 bytes; span to next metadata RVA: 36 bytes.
- Metadata signature: `internal bool <OnIsBoundToAxis>b__0(DigitalBinding.AxisElem x) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=5 (informational only).

```csharp
public static ulong DigitalBinding_c__DisplayClass20_0__OnIsBoundToAxis_b__0_RVAc5c9c8(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL))), x30);
        if ((x1 == 0x0UL))
        {
            goto label_0xC5C9E8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x1) + (0x10UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x10UL))));
        x2 = 0x0UL;
        x0 = x8;
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0x13F610CUL /* metadata target: String.op_Equality */);
        label_0xC5C9E8:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```
