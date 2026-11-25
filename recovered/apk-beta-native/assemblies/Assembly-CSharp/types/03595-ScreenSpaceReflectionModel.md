# `ScreenSpaceReflectionModel` — TypeDefIndex 3595

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x14` | `ScreenSpaceReflectionModel.Settings` | `m_Settings` |

## `ScreenSpaceReflectionModel.get_settings` — RVA `0xcdbf8c`

- Lift status: **exact**; input span: 32 bytes; span to next metadata RVA: 32 bytes.
- Metadata signature: `public ScreenSpaceReflectionModel.Settings get_settings() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static ulong ScreenSpaceReflectionModel_get_settings_RVAcdbf8c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_pair_address_13483936 = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x44UL))))));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((x0) + (0x34UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((x0) + (0x34UL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((x0) + (0x24UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((x0) + (0x24UL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v2 = RuntimeMemory.ReadVector128(unchecked((ulong)((x0) + (0x14UL))));
#else
        v2 = __ReadVector128(unchecked((ulong)((x0) + (0x14UL))));
#endif
        RuntimeMemory.WriteU32(unchecked((ulong)((x8) + (0x30UL))), unchecked((uint)(x9)));
        __arm64_pair_address_13483936 = unchecked((ulong)((x8) + (0x10UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13483936, v1);
#else
        __WriteVector128(__arm64_pair_address_13483936, v1);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13483936) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13483936) + (0x10UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(x8, v2);
#else
        __WriteVector128(x8, v2);
#endif
        return x0;
        return default(ulong);
    }
```

## `ScreenSpaceReflectionModel.set_settings` — RVA `0xcdbfac`

- Lift status: **exact**; input span: 32 bytes; span to next metadata RVA: 32 bytes.
- Metadata signature: `public void set_settings(ScreenSpaceReflectionModel.Settings value) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static ulong ScreenSpaceReflectionModel_set_settings_RVAcdbfac(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_pair_address_13483952 = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        ulong x8 = default(ulong);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x1) + (0x30UL))))));
        __arm64_pair_address_13483952 = unchecked((ulong)((x1) + (0x10UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(__arm64_pair_address_13483952);
#else
        v1 = __ReadVector128(__arm64_pair_address_13483952);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13483952) + (0x10UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13483952) + (0x10UL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v2 = RuntimeMemory.ReadVector128(x1);
#else
        v2 = __ReadVector128(x1);
#endif
        RuntimeMemory.WriteU32(unchecked((ulong)((x0) + (0x44UL))), unchecked((uint)(x8)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x0) + (0x34UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((x0) + (0x34UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x0) + (0x24UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((x0) + (0x24UL))), v1);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x0) + (0x14UL))), v2);
#else
        __WriteVector128(unchecked((ulong)((x0) + (0x14UL))), v2);
#endif
        return x0;
        return default(ulong);
    }
```

## `ScreenSpaceReflectionModel.Reset` — RVA `0xcdbfcc`

- Lift status: **exact**; input span: 80 bytes; span to next metadata RVA: 80 bytes.
- Metadata signature: `public override void Reset() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=7 (informational only).

```csharp
public static ulong ScreenSpaceReflectionModel_Reset_RVAcdbfcc(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_pair_address_13484032 = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        ulong x8 = default(ulong);
        x8 = 0x431000UL;
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((x8) + (0xBD8UL))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((x8) + (0xED0UL))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((x8) + (0xA58UL))))), 0));
        x8 = 0x432000UL;
        RuntimeMemory.WriteF64(unchecked((ulong)((x0) + (0x14UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((x8) + (0xB30UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((x8) + (0xB30UL))));
#endif
        x8 = unchecked((ulong)(unchecked((uint)(0x42C80000UL))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x0) + (0x1CUL))), unchecked((uint)(x8)));
        x8 = unchecked((ulong)(unchecked((uint)(0xC28FUL))));
        x8 = unchecked((ulong)(unchecked((uint)(unchecked((ulong)((unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((~(0xFFFFUL)))))))))) | (unchecked((ulong)((unchecked((ulong)((0x3CF5UL) << (int)(unchecked((int)(0x10UL)))))) << (int)(unchecked((int)(0x0UL))))))))))));
        __arm64_pair_address_13484032 = unchecked((ulong)((x0) + (0x20UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13484032, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13484032) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v2.GetUInt64(0)))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x0) + (0x30UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        RuntimeMemory.WriteU16(unchecked((ulong)((x0) + (0x31UL))), unchecked((ushort)(unchecked((uint)0x0UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x0) + (0x33UL))), unchecked((byte)(unchecked((uint)0x0UL))));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x0) + (0x34UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((x0) + (0x34UL))), v0);
#endif
        RuntimeMemory.WriteU32(unchecked((ulong)((x0) + (0x44UL))), unchecked((uint)(x8)));
        return x0;
        return default(ulong);
    }
```

## `ScreenSpaceReflectionModel.ctor` — RVA `0xcdc070`

- Lift status: **exact**; input span: 84 bytes; span to next metadata RVA: 84 bytes.
- Metadata signature: `public void .ctor() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=8 (informational only).

```csharp
public static ulong ScreenSpaceReflectionModel_ctor_RVAcdc070(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_pair_address_13484200 = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        ulong x8 = default(ulong);
        x8 = 0x431000UL;
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((x8) + (0xBD8UL))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((x8) + (0xED0UL))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((x8) + (0xA58UL))))), 0));
        x8 = 0x432000UL;
        RuntimeMemory.WriteF64(unchecked((ulong)((x0) + (0x14UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((x8) + (0xB30UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((x8) + (0xB30UL))));
#endif
        x8 = unchecked((ulong)(unchecked((uint)(0x42C80000UL))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x0) + (0x1CUL))), unchecked((uint)(x8)));
        x8 = unchecked((ulong)(unchecked((uint)(0xC28FUL))));
        x8 = unchecked((ulong)(unchecked((uint)(unchecked((ulong)((unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((~(0xFFFFUL)))))))))) | (unchecked((ulong)((unchecked((ulong)((0x3CF5UL) << (int)(unchecked((int)(0x10UL)))))) << (int)(unchecked((int)(0x0UL))))))))))));
        x1 = 0x0UL;
        __arm64_pair_address_13484200 = unchecked((ulong)((x0) + (0x20UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13484200, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13484200) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v2.GetUInt64(0)))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x0) + (0x30UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        RuntimeMemory.WriteU16(unchecked((ulong)((x0) + (0x31UL))), unchecked((ushort)(unchecked((uint)0x0UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x0) + (0x33UL))), unchecked((byte)(unchecked((uint)0x0UL))));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x0) + (0x34UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((x0) + (0x34UL))), v0);
#endif
        RuntimeMemory.WriteU32(unchecked((ulong)((x0) + (0x44UL))), unchecked((uint)(x8)));
        return RuntimeCalls.InvokeDirect(0xCDE564UL /* metadata target: PostProcessingModel.ctor */);
        return default(ulong);
    }
```
