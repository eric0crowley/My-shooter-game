# `ComponentBase` — TypeDefIndex 5062

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x20` | `bool` | `isReady` |
| `0x21` | `bool` | `isDestroyed` |

## `ComponentBase.ctor` — RVA `0xc4f5ac`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `protected void .ctor() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static ulong ComponentBase_ctor_RVAc4f5ac(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x1 = 0x0UL;
        return RuntimeCalls.InvokeDirect(0x1796274UL /* metadata target: MonoBehaviour.ctor */);
        return default(ulong);
    }
```

## `ComponentBase.CanBeUsed` — RVA `0xc502e0`

- Lift status: **exact**; input span: 56 bytes; span to next metadata RVA: 56 bytes.
- Metadata signature: `public bool CanBeUsed() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=6 (informational only).

```csharp
public static uint ComponentBase_CanBeUsed_RVAc502e0(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12911368 = default(uint);
        uint __arm64_flags_right_12911368 = default(uint);
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x8UL))), x19);
        x19 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x21UL))))))));
        if ((unchecked((uint)(x19)) != unchecked((uint)0x0UL)))
        {
        }
        else
        {
            x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x20UL))))))));
            if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
            {
            }
            else
            {
                x8 = RuntimeMemory.ReadU64(x0);
                x9 = unchecked((ulong)(unchecked((uint)(0x1UL))));
                RuntimeMemory.WriteU8(unchecked((ulong)((x0) + (0x20UL))), unchecked((byte)(unchecked((uint)(x9)))));
                x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x178UL))));
                x1 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x178UL)))) + (0x8UL))));
                x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
            }
        }
        label_0xC50308:
        ;
        __arm64_flags_left_12911368 = unchecked((uint)(x19));
        __arm64_flags_right_12911368 = unchecked((uint)0x0UL);
        x0 = unchecked((ulong)(((unchecked((uint)((__arm64_flags_left_12911368) - (__arm64_flags_right_12911368))) == unchecked((uint)0x0UL)) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return unchecked((uint)(x0));
        return default(uint);
    }
```

## `ComponentBase.get_IsInitialized` — RVA `0xc5adcc`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public bool get_IsInitialized() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static uint ComponentBase_get_IsInitialized_RVAc5adcc(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x0 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x20UL))))))));
        return unchecked((uint)(x0));
        return default(uint);
    }
```

## `ComponentBase.get_IsDestroyed` — RVA `0xc5add4`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public bool get_IsDestroyed() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static uint ComponentBase_get_IsDestroyed_RVAc5add4(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x0 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x21UL))))))));
        return unchecked((uint)(x0));
        return default(uint);
    }
```

## `ComponentBase.Init` — RVA `0xc5addc`

- Lift status: **exact**; input span: 32 bytes; span to next metadata RVA: 32 bytes.
- Metadata signature: `public void Init() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=4 (informational only).

```csharp
public static ulong ComponentBase_Init_RVAc5addc(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x20UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC5ADE8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC5ADE4UL);
        }
        return x0;
        label_0xC5ADE8:
        ;
        x8 = RuntimeMemory.ReadU64(x0);
        x9 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x0) + (0x20UL))), unchecked((byte)(unchecked((uint)(x9)))));
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x178UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x178UL)))) + (0x8UL))));
        return RuntimeCalls.InvokeIndirect(x2);
        return default(ulong);
    }
```

## `ComponentBase.ForceInit` — RVA `0xc5adfc`

- Lift status: **exact**; input span: 20 bytes; span to next metadata RVA: 20 bytes.
- Metadata signature: `public void ForceInit() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=3 (informational only).

```csharp
public static ulong ComponentBase_ForceInit_RVAc5adfc(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        x8 = RuntimeMemory.ReadU64(x0);
        x9 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x0) + (0x20UL))), unchecked((byte)(unchecked((uint)(x9)))));
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x178UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x178UL)))) + (0x8UL))));
        return RuntimeCalls.InvokeIndirect(x2);
        return default(ulong);
    }
```

## `ComponentBase.OnEnable` — RVA `0xc5ae10`

- Lift status: **exact**; input span: 60 bytes; span to next metadata RVA: 60 bytes.
- Metadata signature: `private void OnEnable() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=10 (informational only).

```csharp
public static ulong ComponentBase_OnEnable_RVAc5ae10(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x8UL))), x19);
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x20UL))))))));
        x19 = x0;
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC5AE38;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x19);
        x9 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x20UL))), unchecked((byte)(unchecked((uint)(x9)))));
        x0 = x19;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x178UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x178UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        goto label_0xC5AE38;
        label_0xC5AE38:
        ;
        x8 = RuntimeMemory.ReadU64(x19);
        x0 = x19;
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x198UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x198UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeIndirect(x2);
        return default(ulong);
    }
```

## `ComponentBase.OnDisable` — RVA `0xc5ae4c`

- Lift status: **exact**; input span: 12 bytes; span to next metadata RVA: 12 bytes.
- Metadata signature: `private void OnDisable() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=2 (informational only).

```csharp
public static ulong ComponentBase_OnDisable_RVAc5ae4c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong x8 = default(ulong);
        x8 = RuntimeMemory.ReadU64(x0);
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x1A8UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x1A8UL)))) + (0x8UL))));
        return RuntimeCalls.InvokeIndirect(x2);
        return default(ulong);
    }
```

## `ComponentBase.OnDestroy` — RVA `0xc5ae58`

- Lift status: **exact**; input span: 20 bytes; span to next metadata RVA: 20 bytes.
- Metadata signature: `private void OnDestroy() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=3 (informational only).

```csharp
public static ulong ComponentBase_OnDestroy_RVAc5ae58(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        x8 = RuntimeMemory.ReadU64(x0);
        x9 = unchecked((ulong)(unchecked((uint)(0x100UL))));
        RuntimeMemory.WriteU16(unchecked((ulong)((x0) + (0x20UL))), unchecked((ushort)(unchecked((uint)(x9)))));
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x188UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x188UL)))) + (0x8UL))));
        return RuntimeCalls.InvokeIndirect(x2);
        return default(ulong);
    }
```
