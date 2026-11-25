# `InputRig.RigSwitch` — TypeDefIndex 4989

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x18` | `bool` | `defaultState` |
| `0x19` | `bool` | `state` |

## `InputRig.RigSwitch.ctor` — RVA `0xc3f138`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public void .ctor() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static ulong InputRig_RigSwitch_ctor_RVAc3f138(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x1 = 0x0UL;
        return RuntimeCalls.InvokeDirect(0x1589338UL /* metadata target: Object.ctor */);
        return default(ulong);
    }
```

## `InputRig.RigSwitch.ToggleState` — RVA `0xc3f380`

- Lift status: **exact**; input span: 28 bytes; span to next metadata RVA: 28 bytes.
- Metadata signature: `public bool ToggleState() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=3 (informational only).

```csharp
public static uint InputRig_RigSwitch_ToggleState_RVAc3f380(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12841860 = default(uint);
        uint __arm64_flags_right_12841860 = default(uint);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x19UL))))))));
        __arm64_flags_left_12841860 = unchecked((uint)(x9));
        __arm64_flags_right_12841860 = unchecked((uint)0x0UL);
        x8 = unchecked((ulong)(((unchecked((uint)((__arm64_flags_left_12841860) - (__arm64_flags_right_12841860))) == unchecked((uint)0x0UL)) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) ^ (unchecked((uint)(0x1UL)))))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x0) + (0x19UL))), unchecked((byte)(unchecked((uint)(x9)))));
        x0 = unchecked((ulong)(unchecked((uint)(x8))));
        return unchecked((uint)(x0));
        return default(uint);
    }
```

## `InputRig.RigSwitch.ctor` — RVA `0xc3f63c`

- Lift status: **exact**; input span: 48 bytes; span to next metadata RVA: 48 bytes.
- Metadata signature: `public void .ctor(string name) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=7 (informational only).

```csharp
public static ulong InputRig_RigSwitch_ctor_RVAc3f63c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x30 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        x19 = x1;
        x1 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x1589338UL /* metadata target: Object.ctor */, x0, x1, x2, x3);
        RuntimeMemory.WriteU64(unchecked((ulong)((x20) + (0x10UL))), x19);
        x0 = x20;
        x1 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0xB7D8D0UL);
        return default(ulong);
    }
```

## `InputRig.RigSwitch.SetState` — RVA `0xc3f66c`

- Lift status: **exact**; input span: 12 bytes; span to next metadata RVA: 12 bytes.
- Metadata signature: `public void SetState(bool state) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static ulong InputRig_RigSwitch_SetState_RVAc3f66c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong x8 = default(ulong);
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x1))) & (unchecked((uint)(0x1UL)))))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x0) + (0x19UL))), unchecked((byte)(unchecked((uint)(x8)))));
        return x0;
        return default(ulong);
    }
```

## `InputRig.RigSwitch.GetState` — RVA `0xc3f678`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public bool GetState() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static uint InputRig_RigSwitch_GetState_RVAc3f678(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x0 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x19UL))))))));
        return unchecked((uint)(x0));
        return default(uint);
    }
```

## `InputRig.RigSwitch.Reset` — RVA `0xc3f680`

- Lift status: **exact**; input span: 12 bytes; span to next metadata RVA: 12 bytes.
- Metadata signature: `public override void Reset() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static ulong InputRig_RigSwitch_Reset_RVAc3f680(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong x8 = default(ulong);
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x18UL))))))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x0) + (0x19UL))), unchecked((byte)(unchecked((uint)(x8)))));
        return x0;
        return default(ulong);
    }
```
