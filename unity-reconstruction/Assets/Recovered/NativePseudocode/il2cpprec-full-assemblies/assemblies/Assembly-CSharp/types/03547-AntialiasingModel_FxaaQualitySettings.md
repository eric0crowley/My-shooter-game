# `AntialiasingModel.FxaaQualitySettings` — TypeDefIndex 3547

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x0` | `float` | `subpixelAliasingRemovalAmount` |
| `0x4` | `float` | `edgeDetectionThreshold` |
| `0x8` | `float` | `minimumRequiredLuminance` |

## `AntialiasingModel.FxaaQualitySettings.cctor` — RVA `0xcdae9c`

- Lift status: **partial**; input span: 272 bytes; span to next metadata RVA: 272 bytes.
- Metadata signature: `private static void .cctor() { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=32 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'b.eq' at 0xcdaf10; reason: Unknown IR expression at 0xcdaf10; reason: Unsupported instruction 'fmov' at 0xcdaf14; reason: Unsupported instruction 'b.ls' at 0xcdaf24; reason: Unknown IR expression at 0xcdaf24; reason: Unsupported instruction 'b.eq' at 0xcdaf44; reason: Unknown IR expression at 0xcdaf44; reason: Unsupported instruction 'b.ls' at 0xcdaf60

```csharp
public static ulong AntialiasingModel_FxaaQualitySettings_cctor_RVAcdae9c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13479684 = default(uint);
        uint __arm64_flags_left_13479704 = default(uint);
        uint __arm64_flags_left_13479736 = default(uint);
        uint __arm64_flags_left_13479764 = default(uint);
        uint __arm64_flags_right_13479684 = default(uint);
        uint __arm64_flags_right_13479704 = default(uint);
        uint __arm64_flags_right_13479736 = default(uint);
        uint __arm64_flags_right_13479764 = default(uint);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        x19 = 0x1BAB000UL;
        x20 = 0x1A8F000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x605UL))))))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x4F0UL))));
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCDAED8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x4F0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x138UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x605UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCDAED8;
        label_0xCDAED8:
        ;
        x0 = RuntimeMemory.ReadU64(x20);
        x1 = unchecked((ulong)(unchecked((uint)(0x5UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D9D4UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCDAFA8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x18UL))))));
        x1 = x0;
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCDAFA4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = 0x431000UL;
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((x9) + (0xAF0UL))))), 0));
        x9 = unchecked((ulong)(unchecked((uint)(0x9931UL))));
        x9 = unchecked((ulong)(unchecked((uint)(unchecked((ulong)((unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) & (unchecked((uint)((~(0xFFFFUL)))))))))) | (unchecked((ulong)((unchecked((ulong)((0x3DAAUL) << (int)(unchecked((int)(0x10UL)))))) << (int)(unchecked((int)(0x0UL))))))))))));
        __arm64_flags_left_13479684 = unchecked((uint)(x8));
        __arm64_flags_right_13479684 = unchecked((uint)0x1UL);
        RuntimeMemory.WriteF64(unchecked((ulong)((x1) + (0x20UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x1) + (0x28UL))), unchecked((uint)(x9)));
        RuntimeCalls.Unsupported("b.eq", 0xCDAF10UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xCDAFA4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCDAF14UL);
        }
        RuntimeCalls.Unsupported("fmov", 0xCDAF14UL);
        __arm64_flags_left_13479704 = unchecked((uint)(x8));
        __arm64_flags_right_13479704 = unchecked((uint)0x2UL);
        RuntimeMemory.WriteF64(unchecked((ulong)((x1) + (0x2CUL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x1) + (0x34UL))), unchecked((uint)(x9)));
        RuntimeCalls.Unsupported("b.ls", 0xCDAF24UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xCDAFA4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = 0x431000UL;
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((x9) + (0xBE0UL))))), 0));
        x9 = unchecked((ulong)(unchecked((uint)(0x9931UL))));
        x9 = unchecked((ulong)(unchecked((uint)(unchecked((ulong)((unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) & (unchecked((uint)((~(0xFFFFUL)))))))))) | (unchecked((ulong)((unchecked((ulong)((0x3DAAUL) << (int)(unchecked((int)(0x10UL)))))) << (int)(unchecked((int)(0x0UL))))))))))));
        __arm64_flags_left_13479736 = unchecked((uint)(x8));
        __arm64_flags_right_13479736 = unchecked((uint)0x3UL);
        RuntimeMemory.WriteF64(unchecked((ulong)((x1) + (0x38UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x1) + (0x40UL))), unchecked((uint)(x9)));
        RuntimeCalls.Unsupported("b.eq", 0xCDAF44UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xCDAFA4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = 0x431000UL;
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((x9) + (0xD28UL))))), 0));
        x9 = unchecked((ulong)(unchecked((uint)(0x3D800000UL))));
        __arm64_flags_left_13479764 = unchecked((uint)(x8));
        __arm64_flags_right_13479764 = unchecked((uint)0x4UL);
        RuntimeMemory.WriteU32(unchecked((ulong)((x1) + (0x4CUL))), unchecked((uint)(x9)));
        RuntimeMemory.WriteF64(unchecked((ulong)((x1) + (0x44UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))));
        RuntimeCalls.Unsupported("b.ls", 0xCDAF60UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xCDAFA4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x432000UL;
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((x8) + (0x130UL))))), 0));
        x8 = 0x1A8F000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x138UL))));
        x9 = unchecked((ulong)(unchecked((uint)(0x9724UL))));
        x9 = unchecked((ulong)(unchecked((uint)(unchecked((ulong)((unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) & (unchecked((uint)((~(0xFFFFUL)))))))))) | (unchecked((ulong)((unchecked((ulong)((0x3CFFUL) << (int)(unchecked((int)(0x10UL)))))) << (int)(unchecked((int)(0x0UL))))))))))));
        RuntimeMemory.WriteF64(unchecked((ulong)((x1) + (0x50UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x1) + (0x58UL))), unchecked((uint)(x9)));
        x9 = RuntimeMemory.ReadU64(x8);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0xB8UL))));
        RuntimeMemory.WriteU64(x9, x1);
        x8 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0xB7D8D0UL);
        label_0xCDAFA4:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB7CUL, x0, x1, x2, x3);
        goto label_0xCDAFA8;
        label_0xCDAFA8:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```
