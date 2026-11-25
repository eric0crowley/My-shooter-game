# `AI.<UpdateModelYaw>d__137` — TypeDefIndex 3333

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x10` | `int` | `<>1__state` |
| `0x18` | `object` | `<>2__current` |
| `0x20` | `AI` | `<>4__this` |

## `AI.<UpdateModelYaw>d__137.ctor` — RVA `0xc7eecc`

- Lift status: **exact**; input span: 40 bytes; span to next metadata RVA: 40 bytes.
- Metadata signature: `public void .ctor(int <>1__state) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=5 (informational only).

```csharp
public static ulong AI_UpdateModelYaw_d__137_ctor_RVAc7eecc(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x30 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        x19 = unchecked((ulong)(unchecked((uint)(x1))));
        x1 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x1589338UL /* metadata target: Object.ctor */, x0, x1, x2, x3);
        RuntimeMemory.WriteU32(unchecked((ulong)((x20) + (0x10UL))), unchecked((uint)(x19)));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        return default(ulong);
    }
```

## `AI.<UpdateModelYaw>d__137.Dispose` — RVA `0xc82340`

- Lift status: **exact**; input span: 4 bytes; span to next metadata RVA: 4 bytes.
- Metadata signature: `private void System.IDisposable.Dispose() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=0 (informational only).

```csharp
public static ulong AI_UpdateModelYaw_d__137_Dispose_RVAc82340(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        return x0;
        return default(ulong);
    }
```

## `AI.<UpdateModelYaw>d__137.MoveNext` — RVA `0xc82344`

- Lift status: **partial**; input span: 256 bytes; span to next metadata RVA: 256 bytes.
- Metadata signature: `private bool MoveNext() { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=21 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'fabd' at 0xc823b4; reason: Unsupported instruction 'fcsel' at 0xc823b8; reason: Unknown IR expression at 0xc823b8; reason: Unsupported instruction 'cset' at 0xc82434; reason: Unknown IR expression at 0xc82434

```csharp
public static uint AI_UpdateModelYaw_d__137_MoveNext_RVAc82344(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13116248 = default(uint);
        uint __arm64_flags_left_13116452 = default(uint);
        uint __arm64_flags_right_13116248 = default(uint);
        uint __arm64_flags_right_13116452 = default(uint);
        float __arm64_float_flags_left_13116292 = default(float);
        float __arm64_float_flags_left_13116336 = default(float);
        float __arm64_float_flags_left_13116352 = default(float);
        float __arm64_float_flags_right_13116292 = default(float);
        float __arm64_float_flags_right_13116336 = default(float);
        float __arm64_float_flags_right_13116352 = default(float);
        float __arm64_fp_left_13116332 = default(float);
        float __arm64_fp_right_13116332 = default(float);
        ulong __arm64_pair_address_13116228 = default(ulong);
        ulong __arm64_pair_address_13116472 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
        RuntimeVector128 v4 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        RuntimeVector128 v9 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x22 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        __arm64_pair_address_13116228 = unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFC0UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13116228, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13116228) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        sp = __arm64_pair_address_13116228;
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x10UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))), x19);
        x21 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x10UL))))));
        __arm64_flags_left_13116248 = unchecked((uint)(x21));
        __arm64_flags_right_13116248 = unchecked((uint)0x1UL);
        if (((__arm64_flags_left_13116248 >= __arm64_flags_right_13116248) && (!((unchecked((uint)((__arm64_flags_left_13116248) - (__arm64_flags_right_13116248))) == unchecked((uint)0x0UL))))))
        {
            goto label_0xC82424;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x20UL))));
        x19 = x0;
        x8 = unchecked((ulong)(unchecked((uint)(0xFFFFFFFFFFFFFFFFUL))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x0) + (0x10UL))), unchecked((uint)(x8)));
        if ((x22 == 0x0UL))
        {
            goto label_0xC82440;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC82374UL)));
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x22) + (0x1FCUL))))), 0));
        x8 = unchecked((ulong)(unchecked((uint)(0xE4UL))));
        x9 = unchecked((ulong)(unchecked((uint)(0xE8UL))));
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x22) + (0xECUL))))), 0));
        __arm64_float_flags_left_13116292 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13116292 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        x8 = ((__arm64_float_flags_left_13116292 > __arm64_float_flags_right_13116292) ? x9 : x8);
        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x22) + (x8))))), 0));
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1789B60UL /* metadata target: Time.get_deltaTime */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x43340000UL))));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0))))), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(x8))), 0)), 0));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0xC0UL))));
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0))))), 0));
        __arm64_fp_left_13116332 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_fp_right_13116332 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes((-(unchecked((float)((__arm64_fp_left_13116332) * (__arm64_fp_right_13116332)))))), 0));
        __arm64_float_flags_left_13116336 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13116336 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        RuntimeCalls.Unsupported("fabd", 0xC823B4UL);
        RuntimeCalls.Unsupported("fcsel", 0xC823B8UL);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes((__Unsupported<bool>("Unknown IR expression") ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        __arm64_float_flags_left_13116352 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13116352 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes((((__arm64_float_flags_left_13116352 > __arm64_float_flags_right_13116352) || ((__arm64_float_flags_left_13116352 != __arm64_float_flags_left_13116352) || (__arm64_float_flags_right_13116352 != __arm64_float_flags_right_13116352))) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((x22) + (0xECUL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        if ((x0 == 0x0UL))
        {
            goto label_0xC82440;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792154UL /* metadata target: Component.get_transform */, x0, x1, x2, x3);
        x8 = 0x432000UL;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x22) + (0xECUL))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x3E4UL))))), 0));
        x20 = x0;
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        x0 = 0x0UL;
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        x0 = RuntimeCalls.InvokeDirect(0x178B12CUL /* metadata target: Quaternion.Internal_FromEulerRad */, x0, x1, x2, x3);
        if ((x20 == 0x0UL))
        {
            goto label_0xC82440;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179D874UL /* metadata target: Transform.set_localRotation */, x0, x1, x2, x3);
        RuntimeMemory.WritePtr(unchecked((ulong)((x19) + (0x18UL))), 0x0UL);
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x19) + (0xFFFFFFFFFFFFFFF8UL))), unchecked((uint)(x8)));
        goto label_0xC82424;
        label_0xC82424:
        ;
        __arm64_flags_left_13116452 = unchecked((uint)(x21));
        __arm64_flags_right_13116452 = unchecked((uint)0x2UL);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        RuntimeCalls.Unsupported("cset", 0xC82434UL);
        x0 = unchecked((ulong)((__Unsupported<bool>("Unknown IR expression") ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        __arm64_pair_address_13116472 = sp;
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13116472)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13116472) + (0x8UL))))), 0));
        sp = unchecked((ulong)((__arm64_pair_address_13116472) + (0x40UL)));
        return unchecked((uint)(x0));
        label_0xC82440:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        return default(uint);
    }
```

## `AI.<UpdateModelYaw>d__137.get_Current` — RVA `0xc82444`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `private object System.Collections.Generic.IEnumerator<System.Object>.get_Current() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static ulong AI_UpdateModelYaw_d__137_get_Current_RVAc82444(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x18UL))));
        return x0;
        return default(ulong);
    }
```

## `AI.<UpdateModelYaw>d__137.Reset` — RVA `0xc8244c`

- Lift status: **exact**; input span: 56 bytes; span to next metadata RVA: 56 bytes.
- Metadata signature: `private void System.Collections.IEnumerator.Reset() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=8 (informational only).

```csharp
public static ulong AI_UpdateModelYaw_d__137_Reset_RVAc8244c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x8UL))), x19);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x3F0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D940UL, x0, x1, x2, x3);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = 0x0UL;
        x19 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x1549CD0UL /* metadata target: NotSupportedException.ctor */, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xDD8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D940UL, x0, x1, x2, x3);
        x1 = x0;
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xB7DA4CUL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `AI.<UpdateModelYaw>d__137.get_Current` — RVA `0xc82484`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `private object System.Collections.IEnumerator.get_Current() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static ulong AI_UpdateModelYaw_d__137_get_Current_RVAc82484(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x18UL))));
        return x0;
        return default(ulong);
    }
```
