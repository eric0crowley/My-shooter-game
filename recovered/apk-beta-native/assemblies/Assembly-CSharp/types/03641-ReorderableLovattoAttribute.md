# `ReorderableLovattoAttribute` — TypeDefIndex 3641

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x14` | `bool` | `add` |
| `0x15` | `bool` | `remove` |
| `0x16` | `bool` | `draggable` |
| `0x17` | `bool` | `singleLine` |
| `0x18` | `bool` | `paginate` |
| `0x1C` | `int` | `pageSize` |
| `0x20` | `string` | `elementNameProperty` |
| `0x28` | `string` | `elementNameOverride` |
| `0x30` | `string` | `elementIconPath` |

## `ReorderableLovattoAttribute.ctor` — RVA `0xce80b8`

- Lift status: **exact**; input span: 28 bytes; span to next metadata RVA: 28 bytes.
- Metadata signature: `public void .ctor() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=6 (informational only).

```csharp
public static ulong ReorderableLovattoAttribute_ctor_RVAce80b8(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x2 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x3 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x4 = 0x0UL;
        x5 = 0x0UL;
        x6 = 0x0UL;
        return RuntimeCalls.InvokeDirect(0xCE80F0UL /* metadata target: ReorderableLovattoAttribute.ctor */);
        return default(ulong);
    }
```

## `ReorderableLovattoAttribute.ctor` — RVA `0xce80d4`

- Lift status: **exact**; input span: 28 bytes; span to next metadata RVA: 28 bytes.
- Metadata signature: `public void .ctor(string elementNameProperty) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=6 (informational only).

```csharp
public static ulong ReorderableLovattoAttribute_ctor_RVAce80d4(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x4 = x1;
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x2 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x3 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x5 = 0x0UL;
        x6 = 0x0UL;
        return RuntimeCalls.InvokeDirect(0xCE80F0UL /* metadata target: ReorderableLovattoAttribute.ctor */);
        return default(ulong);
    }
```

## `ReorderableLovattoAttribute.ctor` — RVA `0xce80f0`

- Lift status: **exact**; input span: 128 bytes; span to next metadata RVA: 128 bytes.
- Metadata signature: `public void .ctor(bool add, bool remove, bool draggable, string elementNameProperty, string elementNameOverride, string elementIconPath) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=18 (informational only).

```csharp
public static ulong ReorderableLovattoAttribute_ctor_RVAce80f0(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x22 = default(ulong);
        ulong x23 = default(ulong);
        ulong x24 = default(ulong);
        ulong x25 = default(ulong);
        ulong x30 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFC0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFC0UL)))) + (0x8UL))), x25);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x24);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))), x19);
        x23 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x1))) & (unchecked((uint)(0x1UL)))))));
        x1 = 0x0UL;
        x19 = x6;
        x20 = x5;
        x21 = x4;
        x22 = x0;
        x24 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x2))) & (unchecked((uint)(0x1UL)))))));
        x25 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x3))) & (unchecked((uint)(0x1UL)))))));
        x0 = RuntimeCalls.InvokeDirect(0x178FCF8UL /* metadata target: PropertyAttribute.ctor */, x0, x1, x2, x3);
        x0 = x22;
        RuntimeMemory.WriteU8(unchecked((ulong)((x22) + (0x14UL))), unchecked((byte)(unchecked((uint)(x23)))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x22) + (0x15UL))), unchecked((byte)(unchecked((uint)(x24)))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x22) + (0x16UL))), unchecked((byte)(unchecked((uint)(x25)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x20UL))), x21);
        x1 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = x22;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x28UL))), x20);
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        RuntimeMemory.WriteU64(unchecked((ulong)((x22) + (0x30UL))), x19);
        x0 = x22;
        x1 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x25 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeDirect(0xB7D8D0UL);
        return default(ulong);
    }
```

## `ReorderableLovattoAttribute.ctor` — RVA `0xce8170`

- Lift status: **exact**; input span: 28 bytes; span to next metadata RVA: 28 bytes.
- Metadata signature: `public void .ctor(string elementNameProperty, string elementIconPath) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=6 (informational only).

```csharp
public static ulong ReorderableLovattoAttribute_ctor_RVAce8170(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x6 = x2;
        x4 = x1;
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x2 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x3 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x5 = 0x0UL;
        return RuntimeCalls.InvokeDirect(0xCE80F0UL /* metadata target: ReorderableLovattoAttribute.ctor */);
        return default(ulong);
    }
```

## `ReorderableLovattoAttribute.ctor` — RVA `0xce818c`

- Lift status: **exact**; input span: 28 bytes; span to next metadata RVA: 28 bytes.
- Metadata signature: `public void .ctor(string elementNameProperty, string elementNameOverride, string elementIconPath) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=6 (informational only).

```csharp
public static ulong ReorderableLovattoAttribute_ctor_RVAce818c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x6 = x3;
        x5 = x2;
        x4 = x1;
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x2 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x3 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        return RuntimeCalls.InvokeDirect(0xCE80F0UL /* metadata target: ReorderableLovattoAttribute.ctor */);
        return default(ulong);
    }
```

## `ReorderableLovattoAttribute.ctor` — RVA `0xce81a8`

- Lift status: **exact**; input span: 24 bytes; span to next metadata RVA: 24 bytes.
- Metadata signature: `public void .ctor(bool add, bool remove, bool draggable, string elementNameProperty, string elementIconPath) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=5 (informational only).

```csharp
public static ulong ReorderableLovattoAttribute_ctor_RVAce81a8(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x6 = x5;
        x1 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x1))) & (unchecked((uint)(0x1UL)))))));
        x2 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x2))) & (unchecked((uint)(0x1UL)))))));
        x3 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x3))) & (unchecked((uint)(0x1UL)))))));
        x5 = 0x0UL;
        return RuntimeCalls.InvokeDirect(0xCE80F0UL /* metadata target: ReorderableLovattoAttribute.ctor */);
        return default(ulong);
    }
```
