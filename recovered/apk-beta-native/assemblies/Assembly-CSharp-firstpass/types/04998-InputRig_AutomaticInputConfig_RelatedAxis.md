# `InputRig.AutomaticInputConfig.RelatedAxis` — TypeDefIndex 4998

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x10` | `string` | `axisName` |
| `0x18` | `bool` | `mustBeControlledByInput` |
| `0x1C` | `int` | `axisId` |

## `InputRig.AutomaticInputConfig.RelatedAxis.IsEnabling` — RVA `0xc424a8`

- Lift status: **exact**; input span: 80 bytes; span to next metadata RVA: 80 bytes.
- Metadata signature: `public bool IsEnabling(InputRig rig) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=10 (informational only).

```csharp
public static uint InputRig_AutomaticInputConfig_RelatedAxis_IsEnabling_RVAc424a8(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12854492 = default(uint);
        uint __arm64_flags_right_12854492 = default(uint);
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x8UL))), x19);
        if ((x1 == 0x0UL))
        {
            label_0xC424F4:
            ;
            x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        }
        else
        {
            x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x10UL))));
            x19 = x0;
            x2 = unchecked((ulong)((x0) + (0x1CUL)));
            x0 = x1;
            x1 = x8;
            x3 = 0x0UL;
            x0 = RuntimeCalls.InvokeDirect(0xC3DA8CUL /* metadata target: InputRig.GetAxisConfig */, x0, x1, x2, x3);
            if ((x0 == 0x0UL))
            {
                label_0xC424E8:
                ;
                x0 = unchecked((ulong)(unchecked((uint)(0x1UL))));
            }
            else
            {
                x0 = RuntimeCalls.InvokeDirect(0xC41C80UL /* metadata target: InputRig.AxisConfig.IsControlledByInput */, x0, x1, x2, x3);
                x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x18UL))))))));
                x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)(0x1UL)))))));
                __arm64_flags_left_12854492 = unchecked((uint)(x8));
                __arm64_flags_right_12854492 = unchecked((uint)(x9));
                x0 = unchecked((ulong)(((unchecked((uint)((__arm64_flags_left_12854492) - (__arm64_flags_right_12854492))) == unchecked((uint)0x0UL)) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
            }
            label_0xC424EC:
            ;
            x30 = RuntimeMemory.ReadU64(sp);
            x19 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
            return unchecked((uint)(x0));
        }
        return default(uint);
    }
```

## `InputRig.AutomaticInputConfig.RelatedAxis.ctor` — RVA `0xc424f8`

- Lift status: **exact**; input span: 96 bytes; span to next metadata RVA: 96 bytes.
- Metadata signature: `public void .ctor() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=16 (informational only).

```csharp
public static ulong InputRig_AutomaticInputConfig_RelatedAxis_ctor_RVAc424f8(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        x21 = 0x1BAB000UL;
        x20 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x205UL))))))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x48UL))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC4252C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x48UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x205UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC4252C;
        label_0xC4252C:
        ;
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1589338UL /* metadata target: Object.ctor */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x20);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x1 = RuntimeMemory.ReadU64(x8);
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x10UL))), x1);
        x0 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeDirect(0xB7D8D0UL);
        return default(ulong);
    }
```
