# `AmmoText` — TypeDefIndex 3368

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x20` | `int` | `ammoGui` |
| `0x24` | `int` | `ammoGui2` |
| `0x28` | `bool` | `showMags` |
| `0x2C` | `int` | `oldAmmo` |
| `0x30` | `int` | `oldAmmo2` |
| `0x34` | `Color` | `textColor` |
| `0x48` | `Text` | `uiTextComponent` |

## `AmmoText.OnEnable` — RVA `0xc91100`

- Lift status: **partial**; input span: 100 bytes; span to next metadata RVA: 100 bytes.
- Metadata signature: `private void OnEnable() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=14 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'mvni' at 0xc91150

```csharp
public static ulong AmmoText_OnEnable_RVAc91100(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        x20 = 0x1BAB000UL;
        x21 = 0x1A8D000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x44DUL))))))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xF28UL))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
        }
        else
        {
            x0 = 0x1A8D000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xF28UL))));
            // Likely IL2CPP class initialization helper (guarded call).
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
            RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x44DUL))), unchecked((byte)(unchecked((uint)(x8)))));
        }
        label_0xC91134:
        ;
        x1 = RuntimeMemory.ReadU64(x21);
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xE31BC8UL, x0, x1, x2, x3);
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x48UL))), x0);
        x1 = x0;
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        RuntimeCalls.Unsupported("mvni", 0xC91150UL);
        RuntimeMemory.WriteF64(unchecked((ulong)((x19) + (0xFFFFFFFFFFFFFFE4UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return x0;
        return default(ulong);
    }
```

## `AmmoText.Update` — RVA `0xc91164`

- Lift status: **partial**; input span: 268 bytes; span to next metadata RVA: 268 bytes.
- Metadata signature: `private void Update() { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=41 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'csel' at 0xc9124c; reason: Unknown IR expression at 0xc9124c

```csharp
public static ulong AmmoText_Update_RVAc91164(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13177256 = default(uint);
        uint __arm64_flags_left_13177272 = default(uint);
        ulong __arm64_flags_left_13177404 = default(ulong);
        uint __arm64_flags_right_13177256 = default(uint);
        uint __arm64_flags_right_13177272 = default(uint);
        ulong __arm64_flags_right_13177404 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        ulong x10 = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        x20 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x44EUL))))))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC9119C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xF8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x230UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x44EUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC9119C;
        label_0xC9119C:
        ;
        x0 = x19;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x20UL))))));
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xCUL))))));
        __arm64_flags_left_13177256 = unchecked((uint)(x8));
        __arm64_flags_right_13177256 = unchecked((uint)(x9));
        if ((!((unchecked((uint)((__arm64_flags_left_13177256) - (__arm64_flags_right_13177256))) == unchecked((uint)0x0UL)))))
        {
            goto label_0xC911C0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x24UL))))));
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x30UL))))));
        __arm64_flags_left_13177272 = unchecked((uint)(x8));
        __arm64_flags_right_13177272 = unchecked((uint)(x9));
        if ((unchecked((uint)((__arm64_flags_left_13177272) - (__arm64_flags_right_13177272))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC91260;
        }
        else
        {
            goto label_0xC911C0;
        }
        label_0xC911C0:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x28UL))))))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x48UL))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC91220;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1545824UL /* metadata target: Int32.ToString */, x0, x1, x2, x3);
        x21 = x0;
        x0 = unchecked((ulong)((x19) + (0x24UL)));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1545824UL /* metadata target: Int32.ToString */, x0, x1, x2, x3);
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xF8UL))));
        x2 = x0;
        x0 = x21;
        x3 = 0x0UL;
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x13F661CUL /* metadata target: String.Concat */, x0, x1, x2, x3);
        if ((x20 == 0x0UL))
        {
            goto label_0xC9126C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x20);
        x1 = x0;
        x0 = x20;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x5E8UL))));
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x5F0UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        goto label_0xC91258;
        label_0xC91220:
        ;
        x0 = unchecked((ulong)((x19) + (0x24UL)));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1545824UL /* metadata target: Int32.ToString */, x0, x1, x2, x3);
        if ((x20 == 0x0UL))
        {
            goto label_0xC9126C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(x20);
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0x230UL))));
        __arm64_flags_left_13177404 = x0;
        __arm64_flags_right_13177404 = 0x0UL;
        x10 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x5E8UL))));
        x9 = RuntimeMemory.ReadU64(x9);
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x5F0UL))));
        RuntimeCalls.Unsupported("csel", 0xC9124CUL);
        x1 = (__Unsupported<bool>("Unknown IR expression") ? x9 : x0);
        x0 = x20;
        x0 = RuntimeCalls.InvokeIndirect(x10, x0, x1, x2, x3);
        goto label_0xC91258;
        label_0xC91258:
        ;
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((x19) + (0x20UL))))), 0));
        RuntimeMemory.WriteF64(unchecked((ulong)((x19) + (0x2CUL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))));
        goto label_0xC91260;
        label_0xC91260:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return x0;
        label_0xC9126C:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `AmmoText.ctor` — RVA `0xc91270`

- Lift status: **partial**; input span: 24 bytes; span to next metadata RVA: 24 bytes.
- Metadata signature: `public void .ctor() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=2 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'mvni' at 0xc91274

```csharp
public static ulong AmmoText_ctor_RVAc91270(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        RuntimeVector128 v0 = default(RuntimeVector128);
        ulong x8 = default(ulong);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeCalls.Unsupported("mvni", 0xC91274UL);
        x1 = 0x0UL;
        RuntimeMemory.WriteU8(unchecked((ulong)((x0) + (0x28UL))), unchecked((byte)(unchecked((uint)(x8)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((x0) + (0x2CUL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))));
        return RuntimeCalls.InvokeDirect(0x1796274UL /* metadata target: MonoBehaviour.ctor */);
        return default(ulong);
    }
```
