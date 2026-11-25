# `ChromaticAberrationModel.Settings` — TypeDefIndex 3562

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x0` | `Texture2D` | `spectralTexture` |
| `0x8` | `float` | `intensity` |

## `ChromaticAberrationModel.Settings.get_defaultSettings` — RVA `0xcdb3ac`

- Lift status: **exact**; input span: 52 bytes; span to next metadata RVA: 52 bytes.
- Metadata signature: `public static ChromaticAberrationModel.Settings get_defaultSettings() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=8 (informational only).

```csharp
public static ulong ChromaticAberrationModel_Settings_get_defaultSettings_RVAcdb3ac(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        sp = unchecked((ulong)((sp) - (0x20UL)));
        RuntimeMemory.WritePtr(unchecked((ulong)((unchecked((ulong)((sp) + (0x8UL)))) + (0x0UL))), 0x0UL);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x8UL)))) + (0x8UL))), x30);
        x0 = sp;
        x1 = 0x0UL;
        RuntimeMemory.WritePtr(sp, 0x0UL);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0xCCCDUL))));
        x8 = unchecked((ulong)(unchecked((uint)(unchecked((ulong)((unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((~(0xFFFFUL)))))))))) | (unchecked((ulong)((unchecked((ulong)((0x3DCCUL) << (int)(unchecked((int)(0x10UL)))))) << (int)(unchecked((int)(0x0UL))))))))))));
        RuntimeMemory.WriteU32(unchecked((ulong)((sp) + (0x8UL))), unchecked((uint)(x8)));
        x0 = RuntimeMemory.ReadU64(sp);
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        return x0;
        return default(ulong);
    }
```
