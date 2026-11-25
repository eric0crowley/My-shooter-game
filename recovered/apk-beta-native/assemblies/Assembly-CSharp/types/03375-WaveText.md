# `WaveText` — TypeDefIndex 3375

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x20` | `int` | `waveGui` |
| `0x24` | `int` | `waveGui2` |
| `0x28` | `int` | `oldWave` |
| `0x2C` | `int` | `oldWave2` |
| `0x30` | `Color` | `textColor` |
| `0x40` | `Text` | `uiTextComponent` |

## `WaveText.OnEnable` — RVA `0xc92a38`

- Lift status: **partial**; input span: 100 bytes; span to next metadata RVA: 100 bytes.
- Metadata signature: `private void OnEnable() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=14 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'mvni' at 0xc92a88

```csharp
public static ulong WaveText_OnEnable_RVAc92a38(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
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
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x45BUL))))))));
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
            RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x45BUL))), unchecked((byte)(unchecked((uint)(x8)))));
        }
        label_0xC92A6C:
        ;
        x1 = RuntimeMemory.ReadU64(x21);
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xE31BC8UL, x0, x1, x2, x3);
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x40UL))), x0);
        x1 = x0;
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        RuntimeCalls.Unsupported("mvni", 0xC92A88UL);
        RuntimeMemory.WriteF64(unchecked((ulong)((x19) + (0xFFFFFFFFFFFFFFE8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return x0;
        return default(ulong);
    }
```

## `WaveText.Update` — RVA `0xc92a9c`

- Lift status: **exact**; input span: 256 bytes; span to next metadata RVA: 256 bytes.
- Metadata signature: `private void Update() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=40 (informational only).

```csharp
public static ulong WaveText_Update_RVAc92a9c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13183716 = default(uint);
        uint __arm64_flags_left_13183732 = default(uint);
        uint __arm64_flags_right_13183716 = default(uint);
        uint __arm64_flags_right_13183732 = default(uint);
        ulong __arm64_pair_address_13183852 = default(ulong);
        ulong __arm64_pair_address_13183856 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x22 = default(ulong);
        ulong x23 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFD0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFD0UL)))) + (0x8UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x19);
        x20 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x45CUL))))))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC92AD8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x148UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x150UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x45CUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC92AD8;
        label_0xC92AD8:
        ;
        x0 = x19;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x20UL))))));
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x8UL))))));
        __arm64_flags_left_13183716 = unchecked((uint)(x8));
        __arm64_flags_right_13183716 = unchecked((uint)(x9));
        if ((!((unchecked((uint)((__arm64_flags_left_13183716) - (__arm64_flags_right_13183716))) == unchecked((uint)0x0UL)))))
        {
            goto label_0xC92AFC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x24UL))))));
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x2CUL))))));
        __arm64_flags_left_13183732 = unchecked((uint)(x8));
        __arm64_flags_right_13183732 = unchecked((uint)(x9));
        if ((unchecked((uint)((__arm64_flags_left_13183732) - (__arm64_flags_right_13183732))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC92B88;
        }
        else
        {
            goto label_0xC92AFC;
        }
        label_0xC92AFC:
        ;
        x22 = 0x1A8E000UL;
        x23 = 0x1A8E000UL;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x40UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x150UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0x148UL))));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1545824UL /* metadata target: Int32.ToString */, x0, x1, x2, x3);
        x21 = x0;
        x0 = unchecked((ulong)((x19) + (0x24UL)));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1545824UL /* metadata target: Int32.ToString */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x22);
        x2 = RuntimeMemory.ReadU64(x23);
        x3 = x0;
        x1 = x21;
        x0 = x8;
        x4 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x13F693CUL /* metadata target: String.Concat */, x0, x1, x2, x3);
        if ((x20 == 0x0UL))
        {
            goto label_0xC92B98;
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
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x40UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC92B98;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x0);
        __arm64_pair_address_13183852 = unchecked((ulong)((x19) + (0x38UL)));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13183852)), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13183852) + (0x4UL))))), 0));
        __arm64_pair_address_13183856 = unchecked((ulong)((x19) + (0x30UL)));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13183856)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13183856) + (0x4UL))))), 0));
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x2A8UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x2B0UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((x19) + (0x20UL))))), 0));
        RuntimeMemory.WriteF64(unchecked((ulong)((x19) + (0x28UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))));
        goto label_0xC92B88;
        label_0xC92B88:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return x0;
        label_0xC92B98:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `WaveText.ctor` — RVA `0xc92b9c`

- Lift status: **partial**; input span: 16 bytes; span to next metadata RVA: 16 bytes.
- Metadata signature: `public void .ctor() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'mvni' at 0xc92b9c

```csharp
public static ulong WaveText_ctor_RVAc92b9c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeCalls.Unsupported("mvni", 0xC92B9CUL);
        x1 = 0x0UL;
        RuntimeMemory.WriteF64(unchecked((ulong)((x0) + (0x28UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))));
        return RuntimeCalls.InvokeDirect(0x1796274UL /* metadata target: MonoBehaviour.ctor */);
        return default(ulong);
    }
```
