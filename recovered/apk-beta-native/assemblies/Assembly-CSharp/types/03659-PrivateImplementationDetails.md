# `<PrivateImplementationDetails>` — TypeDefIndex 3659

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## `<PrivateImplementationDetails>.ComputeStringHash` — RVA `0xceb858`

- Lift status: **partial**; input span: 124 bytes; span to next metadata RVA: 6962684 bytes.
- Metadata signature: `internal static uint ComputeStringHash(string s) { }`
- Next metadata RVA is far away; input was limited to the first Capstone-decoded `ret` (boundary heuristic, not proof). Inspect this method independently.
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=20 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'b.lt' at 0xceb8b4; reason: Unknown IR expression at 0xceb8b4

```csharp
public static uint PrivateImplementationDetails__ComputeStringHash_RVAceb858(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13547640 = default(uint);
        uint __arm64_flags_left_13547692 = default(uint);
        uint __arm64_flags_right_13547640 = default(uint);
        uint __arm64_flags_right_13547692 = default(uint);
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x22 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFD0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x19);
        if ((x0 == 0x0UL))
        {
            goto label_0xCEB8BC;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x10UL))))));
        x20 = unchecked((ulong)(unchecked((uint)(0x9DC5UL))));
        x19 = x0;
        x20 = unchecked((ulong)(unchecked((uint)(unchecked((ulong)((unchecked((ulong)(unchecked((uint)((unchecked((uint)(x20))) & (unchecked((uint)((~(0xFFFFUL)))))))))) | (unchecked((ulong)((unchecked((ulong)((0x811CUL) << (int)(unchecked((int)(0x10UL)))))) << (int)(unchecked((int)(0x0UL))))))))))));
        __arm64_flags_left_13547640 = unchecked((uint)(x8));
        __arm64_flags_right_13547640 = unchecked((uint)0x1UL);
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13547640) - (__arm64_flags_right_13547640))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_13547640)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13547640)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13547640) - (__arm64_flags_right_13547640))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13547640)) < unchecked((int)0x0UL))))))
        {
            goto label_0xCEB8C0;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x22 = unchecked((ulong)(unchecked((uint)(0x193UL))));
        x21 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x22 = unchecked((ulong)(unchecked((uint)(unchecked((ulong)((unchecked((ulong)(unchecked((uint)((unchecked((uint)(x22))) & (unchecked((uint)((~(0xFFFFUL)))))))))) | (unchecked((ulong)((unchecked((ulong)((0x100UL) << (int)(unchecked((int)(0x10UL)))))) << (int)(unchecked((int)(0x0UL))))))))))));
        goto label_0xCEB88C;
        label_0xCEB88C:
        ;
        x0 = x19;
        x1 = unchecked((ulong)(unchecked((uint)(x21))));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x13F1BD0UL /* metadata target: String.get_Chars */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x10UL))))));
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)(0xFFFFUL)))))));
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x20))) ^ (unchecked((uint)(x9)))))));
        x21 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x21))) + (unchecked((uint)(0x1UL)))))));
        __arm64_flags_left_13547692 = unchecked((uint)(x21));
        __arm64_flags_right_13547692 = unchecked((uint)(x8));
        x20 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) * (unchecked((uint)(x22)))))));
        RuntimeCalls.Unsupported("b.lt", 0xCEB8B4UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xCEB88C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xCEB8B8UL)));
        }
        goto label_0xCEB8C0;
        label_0xCEB8BC:
        ;
        x20 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xCEB8C0;
        label_0xCEB8C0:
        ;
        x0 = unchecked((ulong)(unchecked((uint)(x20))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return unchecked((uint)(x0));
        return default(uint);
    }
```
