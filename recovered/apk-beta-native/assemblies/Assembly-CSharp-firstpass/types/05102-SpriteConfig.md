# `SpriteConfig` — TypeDefIndex 5102

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x10` | `bool` | `enabled` |
| `0x18` | `Sprite` | `sprite` |
| `0x20` | `Color` | `color` |
| `0x30` | `float` | `scale` |
| `0x34` | `float` | `rotation` |
| `0x38` | `Vector2` | `offset` |
| `0x40` | `bool` | `resetOffset` |
| `0x41` | `bool` | `resetRotation` |
| `0x42` | `bool` | `resetScale` |
| `0x43` | `bool` | `oneShotState` |
| `0x44` | `float` | `duration` |
| `0x48` | `float` | `baseTransitionTime` |
| `0x4C` | `float` | `colorTransitionFactor` |
| `0x50` | `float` | `scaleTransitionFactor` |
| `0x54` | `float` | `rotationTransitionFactor` |
| `0x58` | `float` | `offsetTransitionFactor` |

## `SpriteConfig.ctor` — RVA `0xc6344c`

- Lift status: **partial**; input span: 76 bytes; span to next metadata RVA: 76 bytes.
- Metadata signature: `public void .ctor() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=6 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'fmov' at 0xc63470; reason: Unsupported instruction 'fmov' at 0xc63474

```csharp
public static ulong SpriteConfig_ctor_RVAc6344c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
        ulong x10 = default(ulong);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x8UL))), x19);
        x1 = 0x0UL;
        x19 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x1589338UL /* metadata target: Object.ctor */, x0, x1, x2, x3);
        x9 = 0x431000UL;
        x10 = 0x432000UL;
        v2 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((x9) + (0xB80UL))))), 0));
#if IL2CPPREC_RUNTIME_VECTOR128
        v3 = RuntimeMemory.ReadVector128(unchecked((ulong)((x10) + (0xEF0UL))));
#else
        v3 = __ReadVector128(unchecked((ulong)((x10) + (0xEF0UL))));
#endif
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeCalls.Unsupported("fmov", 0xC63470UL);
        RuntimeCalls.Unsupported("fmov", 0xC63474UL);
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x10UL))), unchecked((byte)(unchecked((uint)(x8)))));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x19) + (0x20UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((x19) + (0x20UL))), v0);
#endif
        RuntimeMemory.WriteF64(unchecked((ulong)((x19) + (0x54UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((x19) + (0x30UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v2.GetUInt64(0)))));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x19) + (0x44UL))), v3);
#else
        __WriteVector128(unchecked((ulong)((x19) + (0x44UL))), v3);
#endif
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x43UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return x0;
        return default(ulong);
    }
```

## `SpriteConfig.ctor` — RVA `0xc63498`

- Lift status: **partial**; input span: 144 bytes; span to next metadata RVA: 144 bytes.
- Metadata signature: `public void .ctor(Sprite sprite, Color color) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=14 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'fmov' at 0xc634e0; reason: Unsupported instruction 'fmov' at 0xc634e4

```csharp
public static ulong SpriteConfig_ctor_RVAc63498(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_pair_address_12989592 = default(ulong);
        ulong __arm64_pair_address_12989596 = default(ulong);
        ulong __arm64_pair_address_12989708 = default(ulong);
        ulong __arm64_pair_address_12989712 = default(ulong);
        ulong __arm64_pair_address_12989724 = default(ulong);
        ulong __arm64_pair_address_12989728 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v10 = default(RuntimeVector128);
        RuntimeVector128 v11 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        RuntimeVector128 v9 = default(RuntimeVector128);
        ulong x10 = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        __arm64_pair_address_12989592 = unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFC0UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12989592, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v11.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12989592) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v10.GetUInt64(0)))));
        sp = __arm64_pair_address_12989592;
        __arm64_pair_address_12989596 = unchecked((ulong)((sp) + (0x10UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12989596, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12989596) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x20UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))), x19);
        x19 = x1;
        x1 = 0x0UL;
        v8 = v3;
        v9 = v2;
        v10 = v1;
        v11 = v0;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x1589338UL /* metadata target: Object.ctor */, x0, x1, x2, x3);
        x9 = 0x431000UL;
        x10 = 0x432000UL;
        v2 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((x9) + (0xB80UL))))), 0));
#if IL2CPPREC_RUNTIME_VECTOR128
        v3 = RuntimeMemory.ReadVector128(unchecked((ulong)((x10) + (0xEF0UL))));
#else
        v3 = __ReadVector128(unchecked((ulong)((x10) + (0xEF0UL))));
#endif
        RuntimeMemory.WriteU64(unchecked((ulong)((x20) + (0x18UL))), x19);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeCalls.Unsupported("fmov", 0xC634E0UL);
        RuntimeCalls.Unsupported("fmov", 0xC634E4UL);
        x0 = x20;
        x1 = x19;
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0xFFFFFFFFFFFFFFF8UL))), unchecked((byte)(unchecked((uint)(x8)))));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x20) + (0x8UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((x20) + (0x8UL))), v0);
#endif
        RuntimeMemory.WriteF64(unchecked((ulong)((x20) + (0x3CUL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((x20) + (0x18UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v2.GetUInt64(0)))));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x20) + (0x2CUL))), v3);
#else
        __WriteVector128(unchecked((ulong)((x20) + (0x2CUL))), v3);
#endif
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x2BUL))), unchecked((byte)(unchecked((uint)0x0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        __arm64_pair_address_12989708 = unchecked((ulong)((x20) + (0x8UL)));
        RuntimeMemory.WriteF32(__arm64_pair_address_12989708, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_12989708) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0));
        __arm64_pair_address_12989712 = unchecked((ulong)((x20) + (0x10UL)));
        RuntimeMemory.WriteF32(__arm64_pair_address_12989712, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_12989712) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        __arm64_pair_address_12989724 = unchecked((ulong)((sp) + (0x10UL)));
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12989724)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12989724) + (0x8UL))))), 0));
        __arm64_pair_address_12989728 = sp;
        v11 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12989728)), 0));
        v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12989728) + (0x8UL))))), 0));
        sp = unchecked((ulong)((__arm64_pair_address_12989728) + (0x40UL)));
        return x0;
        return default(ulong);
    }
```

## `SpriteConfig.ctor` — RVA `0xc63528`

- Lift status: **partial**; input span: 108 bytes; span to next metadata RVA: 108 bytes.
- Metadata signature: `public void .ctor(bool enabled, bool oneShot, float scale) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=11 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'fmov' at 0xc6355c; reason: Unsupported instruction 'fmov' at 0xc63560

```csharp
public static ulong SpriteConfig_ctor_RVAc63528(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_load_address_12989836 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        ulong x10 = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteF64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFD0UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        sp = unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFD0UL)));
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x19);
        x21 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x1))) & (unchecked((uint)(0x1UL)))))));
        x1 = 0x0UL;
        v8 = v0;
        x19 = unchecked((ulong)(unchecked((uint)(x2))));
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x1589338UL /* metadata target: Object.ctor */, x0, x1, x2, x3);
        x8 = 0x432000UL;
#if IL2CPPREC_RUNTIME_VECTOR128
        v2 = RuntimeMemory.ReadVector128(unchecked((ulong)((x8) + (0xEF0UL))));
#else
        v2 = __ReadVector128(unchecked((ulong)((x8) + (0xEF0UL))));
#endif
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x19))) & (unchecked((uint)(0x1UL)))))));
        x10 = unchecked((ulong)(unchecked((uint)(0x1010101UL))));
        RuntimeCalls.Unsupported("fmov", 0xC6355CUL);
        RuntimeCalls.Unsupported("fmov", 0xC63560UL);
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) * (unchecked((uint)(x10)))))));
        RuntimeMemory.WritePtr(unchecked((ulong)((x20) + (0x34UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        RuntimeMemory.WriteF32(unchecked((ulong)((x20) + (0x30UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x10UL))), unchecked((byte)(unchecked((uint)(x21)))));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x20) + (0x20UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((x20) + (0x20UL))), v0);
#endif
        RuntimeMemory.WriteF64(unchecked((ulong)((x20) + (0x54UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0)))));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x20) + (0x44UL))), v2);
#else
        __WriteVector128(unchecked((ulong)((x20) + (0x44UL))), v2);
#endif
        RuntimeMemory.WriteU32(unchecked((ulong)((x20) + (0x40UL))), unchecked((uint)(x8)));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        __arm64_load_address_12989836 = sp;
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_load_address_12989836)), 0));
        sp = unchecked((ulong)((__arm64_load_address_12989836) + (0x30UL)));
        return x0;
        return default(ulong);
    }
```
