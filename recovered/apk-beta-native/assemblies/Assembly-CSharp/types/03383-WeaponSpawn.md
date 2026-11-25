# `WeaponSpawn` — TypeDefIndex 3383

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x20` | `GameObject` | `gunPrefab` |
| `0x28` | `float` | `spawnTime` |
| `0x30` | `GameObject` | `gunInstance` |
| `0x38` | `float` | `timeLeft` |

## `WeaponSpawn.Start` — RVA `0xc94f74`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `private void Start() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=0 (informational only).

```csharp
public static ulong WeaponSpawn_Start_RVAc94f74(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        RuntimeMemory.WritePtr(unchecked((ulong)((x0) + (0x38UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        return x0;
        return default(ulong);
    }
```

## `WeaponSpawn.Update` — RVA `0xc94f7c`

- Lift status: **exact**; input span: 216 bytes; span to next metadata RVA: 216 bytes.
- Metadata signature: `private void Update() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=22 (informational only).

```csharp
public static ulong WeaponSpawn_Update_RVAc94f7c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        float __arm64_float_flags_left_13193148 = default(float);
        float __arm64_float_flags_left_13193276 = default(float);
        float __arm64_float_flags_right_13193148 = default(float);
        float __arm64_float_flags_right_13193276 = default(float);
        ulong __arm64_load_address_13193264 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteF64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFD0UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        sp = unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFD0UL)));
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x19);
        x20 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x471UL))))))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC94FAC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD8UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x471UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC94FAC;
        label_0xC94FAC:
        ;
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x38UL))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x28UL))))), 0));
        x21 = 0x1A8C000UL;
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xD8UL))));
        __arm64_float_flags_left_13193148 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13193148 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        if ((__arm64_float_flags_left_13193148 > __arm64_float_flags_right_13193148))
        {
            goto label_0xC94FEC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(x21);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x30UL))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC94FD8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC94FD4UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC94FD8;
        label_0xC94FD8:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1798274UL /* metadata target: Object.op_Implicit */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC95038;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC94FE8UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x28UL))))), 0));
        goto label_0xC94FEC;
        label_0xC94FEC:
        ;
        RuntimeMemory.WriteF32(unchecked((ulong)((x19) + (0x38UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        goto label_0xC94FF0;
        label_0xC94FF0:
        ;
        x0 = RuntimeMemory.ReadU64(x21);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x30UL))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC95004;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC95000UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC95004;
        label_0xC95004:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1798274UL /* metadata target: Object.op_Implicit */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC95028;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC95014UL);
        }
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x38UL))))), 0));
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1789B60UL /* metadata target: Time.get_deltaTime */, x0, x1, x2, x3);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((x19) + (0x38UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        goto label_0xC95028;
        label_0xC95028:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        __arm64_load_address_13193264 = sp;
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_load_address_13193264)), 0));
        return x0;
        label_0xC95038:
        ;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x38UL))))), 0));
        __arm64_float_flags_left_13193276 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13193276 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        if (((__arm64_float_flags_left_13193276 > __arm64_float_flags_right_13193276) || ((__arm64_float_flags_left_13193276 != __arm64_float_flags_left_13193276) || (__arm64_float_flags_right_13193276 != __arm64_float_flags_right_13193276))))
        {
            goto label_0xC94FF0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x19;
        RuntimeMemory.WritePtr(unchecked((ulong)((x19) + (0x38UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xC95054UL /* metadata target: WeaponSpawn.Spawn */, x0, x1, x2, x3);
        goto label_0xC94FF0;
        return default(ulong);
    }
```

## `WeaponSpawn.Spawn` — RVA `0xc95054`

- Lift status: **exact**; input span: 288 bytes; span to next metadata RVA: 288 bytes.
- Metadata signature: `private void Spawn() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=42 (informational only).

```csharp
public static ulong WeaponSpawn_Spawn_RVAc95054(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_load_address_13193576 = default(ulong);
        ulong __arm64_pair_address_13193304 = default(ulong);
        ulong __arm64_pair_address_13193308 = default(ulong);
        ulong __arm64_pair_address_13193312 = default(ulong);
        ulong __arm64_pair_address_13193556 = default(ulong);
        ulong __arm64_pair_address_13193568 = default(ulong);
        ulong __arm64_pair_address_13193572 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v10 = default(RuntimeVector128);
        RuntimeVector128 v11 = default(RuntimeVector128);
        RuntimeVector128 v12 = default(RuntimeVector128);
        RuntimeVector128 v13 = default(RuntimeVector128);
        RuntimeVector128 v14 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        RuntimeVector128 v9 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x22 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteF64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFA0UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v14.GetUInt64(0)))));
        sp = unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFA0UL)));
        __arm64_pair_address_13193304 = unchecked((ulong)((sp) + (0x8UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13193304, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v13.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13193304) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v12.GetUInt64(0)))));
        __arm64_pair_address_13193308 = unchecked((ulong)((sp) + (0x18UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13193308, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v11.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13193308) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v10.GetUInt64(0)))));
        __arm64_pair_address_13193312 = unchecked((ulong)((sp) + (0x28UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13193312, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13193312) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x38UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x8UL))), x19);
        x20 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x472UL))))))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
        }
        else
        {
            x0 = 0x1A8D000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x9C8UL))));
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x0 = 0x1A8C000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD8UL))));
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
            RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x472UL))), unchecked((byte)(unchecked((uint)(x8)))));
        }
        label_0xC950A0:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x20UL))));
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792154UL /* metadata target: Component.get_transform */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
        }
        else
        {
            x1 = 0x0UL;
            x0 = RuntimeCalls.InvokeDirect(0x179D508UL /* metadata target: Transform.get_position */, x0, x1, x2, x3);
            x0 = x19;
            x1 = 0x0UL;
            v8 = v0;
            v9 = v1;
            v10 = v2;
            x0 = RuntimeCalls.InvokeDirect(0x1792154UL /* metadata target: Component.get_transform */, x0, x1, x2, x3);
            if ((x0 == 0x0UL))
            {
            }
            else
            {
                x22 = 0x1A8C000UL;
                x21 = 0x1A8D000UL;
                x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0xD8UL))));
                x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x9C8UL))));
                x1 = 0x0UL;
                x0 = RuntimeCalls.InvokeDirect(0x179D6F0UL /* metadata target: Transform.get_rotation */, x0, x1, x2, x3);
                x0 = RuntimeMemory.ReadU64(x22);
                v11 = v0;
                v12 = v1;
                v13 = v2;
                x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
                v14 = v3;
                if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
                {
                }
                else
                {
                    x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
                }
                label_0xC95110:
                ;
                x1 = RuntimeMemory.ReadU64(x21);
                x0 = x20;
                x0 = RuntimeCalls.InvokeDirect(0xD2A1ACUL, x0, x1, x2, x3);
                RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x30UL))), x0);
                x1 = x0;
                x0 = x19;
                x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
                v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0xFFFFFFFFFFFFFFF8UL))))), 0));
                x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x40UL))));
                x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))));
                x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x38UL))));
                __arm64_pair_address_13193556 = unchecked((ulong)((sp) + (0x28UL)));
                v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13193556)), 0));
                v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13193556) + (0x8UL))))), 0));
                RuntimeMemory.WriteF32(unchecked((ulong)((x19) + (0x8UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
                x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x50UL))));
                x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x8UL))));
                __arm64_pair_address_13193568 = unchecked((ulong)((sp) + (0x18UL)));
                v11 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13193568)), 0));
                v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13193568) + (0x8UL))))), 0));
                __arm64_pair_address_13193572 = unchecked((ulong)((sp) + (0x8UL)));
                v13 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13193572)), 0));
                v12 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13193572) + (0x8UL))))), 0));
                __arm64_load_address_13193576 = sp;
                v14 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_load_address_13193576)), 0));
                return x0;
            }
        }
        label_0xC95170:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `WeaponSpawn.ctor` — RVA `0xc95174`

- Lift status: **exact**; input span: 16 bytes; span to next metadata RVA: 16 bytes.
- Metadata signature: `public void .ctor() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=2 (informational only).

```csharp
public static ulong WeaponSpawn_ctor_RVAc95174(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong x8 = default(ulong);
        x8 = unchecked((ulong)(unchecked((uint)(0x41F00000UL))));
        x1 = 0x0UL;
        RuntimeMemory.WriteU32(unchecked((ulong)((x0) + (0x28UL))), unchecked((uint)(x8)));
        return RuntimeCalls.InvokeDirect(0x1796274UL /* metadata target: MonoBehaviour.ctor */);
        return default(ulong);
    }
```
