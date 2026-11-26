# `WeaponBehavior.<Reload>d__361` — TypeDefIndex 3435

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x10` | `int` | `<>1__state` |
| `0x18` | `object` | `<>2__current` |
| `0x20` | `WeaponBehavior` | `<>4__this` |

## `WeaponBehavior.<Reload>d__361.ctor` — RVA `0xcbd868`

- Lift status: **exact**; input span: 40 bytes; span to next metadata RVA: 40 bytes.
- Metadata signature: `public void .ctor(int <>1__state) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=5 (informational only).

```csharp
public static ulong WeaponBehavior_Reload_d__361_ctor_RVAcbd868(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
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

## `WeaponBehavior.<Reload>d__361.Dispose` — RVA `0xcbd890`

- Lift status: **exact**; input span: 4 bytes; span to next metadata RVA: 4 bytes.
- Metadata signature: `private void System.IDisposable.Dispose() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=0 (informational only).

```csharp
public static ulong WeaponBehavior_Reload_d__361_Dispose_RVAcbd890(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        return x0;
        return default(ulong);
    }
```

## `WeaponBehavior.<Reload>d__361.MoveNext` — RVA `0xcbd894`

- Lift status: **partial**; input span: 1492 bytes; span to next metadata RVA: 1492 bytes.
- Metadata signature: `private bool MoveNext() { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=190 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'b.ne' at 0xcbda98; reason: Unknown IR expression at 0xcbda98

```csharp
public static uint WeaponBehavior_Reload_d__361_MoveNext_RVAcbd894(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13359428 = default(uint);
        uint __arm64_flags_left_13359568 = default(uint);
        uint __arm64_flags_left_13359596 = default(uint);
        uint __arm64_flags_left_13359760 = default(uint);
        uint __arm64_flags_left_13359792 = default(uint);
        uint __arm64_flags_left_13359820 = default(uint);
        uint __arm64_flags_left_13359828 = default(uint);
        uint __arm64_flags_left_13359868 = default(uint);
        uint __arm64_flags_left_13359916 = default(uint);
        uint __arm64_flags_left_13360004 = default(uint);
        uint __arm64_flags_left_13360016 = default(uint);
        uint __arm64_flags_left_13360540 = default(uint);
        uint __arm64_flags_left_13360660 = default(uint);
        uint __arm64_flags_left_13360672 = default(uint);
        uint __arm64_flags_result_13359792 = default(uint);
        uint __arm64_flags_result_13359828 = default(uint);
        uint __arm64_flags_result_13359868 = default(uint);
        uint __arm64_flags_right_13359428 = default(uint);
        uint __arm64_flags_right_13359568 = default(uint);
        uint __arm64_flags_right_13359596 = default(uint);
        uint __arm64_flags_right_13359760 = default(uint);
        uint __arm64_flags_right_13359792 = default(uint);
        uint __arm64_flags_right_13359820 = default(uint);
        uint __arm64_flags_right_13359828 = default(uint);
        uint __arm64_flags_right_13359868 = default(uint);
        uint __arm64_flags_right_13359916 = default(uint);
        uint __arm64_flags_right_13360004 = default(uint);
        uint __arm64_flags_right_13360016 = default(uint);
        uint __arm64_flags_right_13360540 = default(uint);
        uint __arm64_flags_right_13360660 = default(uint);
        uint __arm64_flags_right_13360672 = default(uint);
        float __arm64_float_flags_left_13359488 = default(float);
        float __arm64_float_flags_left_13359524 = default(float);
        float __arm64_float_flags_left_13359540 = default(float);
        float __arm64_float_flags_right_13359488 = default(float);
        float __arm64_float_flags_right_13359524 = default(float);
        float __arm64_float_flags_right_13359540 = default(float);
        ulong __arm64_load_address_13359724 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        ulong x10 = default(ulong);
        ulong x11 = default(ulong);
        ulong x12 = default(ulong);
        ulong x13 = default(ulong);
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
        x19 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x4F2UL))))))));
        x20 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCBD93C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x3E8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x808UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x810UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x818UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(x0);
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x820UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x498UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x828UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x830UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x7F0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x4F2UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCBD93C;
        label_0xCBD93C:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x20) + (0x10UL))))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x20UL))));
        __arm64_flags_left_13359428 = unchecked((uint)(x8));
        __arm64_flags_right_13359428 = unchecked((uint)0x1UL);
        if ((unchecked((uint)((__arm64_flags_left_13359428) - (__arm64_flags_right_13359428))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCBDA74;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xCBD94CUL)));
        }
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCBDA5C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)(unchecked((uint)(0xFFFFFFFFFFFFFFFFUL))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x20) + (0x10UL))), unchecked((uint)(x8)));
        if ((x19 == 0x0UL))
        {
            goto label_0xCBDE64;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x229UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCBDA5C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x80UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCBDE64;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x1A0UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCBDA5C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179AD58UL /* metadata target: Time.get_timeSinceLevelLoad */, x0, x1, x2, x3);
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x40000000UL)), 0)), 0));
        __arm64_float_flags_left_13359488 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13359488 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_13359488 <= __arm64_float_flags_right_13359488) || ((__arm64_float_flags_left_13359488 != __arm64_float_flags_left_13359488) || (__arm64_float_flags_right_13359488 != __arm64_float_flags_right_13359488))))
        {
            goto label_0xCBDA5C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x80UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCBDE64;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x2B1UL))))))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCBD9CC;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xCBD998UL)));
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x3ACUL))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)((global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)), 0)) & (unchecked((uint)0x7FFFFFFFUL))))), 0)), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F400000UL)), 0)), 0));
        __arm64_float_flags_left_13359524 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13359524 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        if ((__arm64_float_flags_left_13359524 > __arm64_float_flags_right_13359524))
        {
            goto label_0xCBD9BC;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xCBD9ACUL)));
        }
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x3B0UL))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)((global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)), 0)) & (unchecked((uint)0x7FFFFFFFUL))))), 0)), 0));
        __arm64_float_flags_left_13359540 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13359540 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_13359540 <= __arm64_float_flags_right_13359540) || ((__arm64_float_flags_left_13359540 != __arm64_float_flags_left_13359540) || (__arm64_float_flags_right_13359540 != __arm64_float_flags_right_13359540))))
        {
            goto label_0xCBD9CC;
        }
        else
        {
            goto label_0xCBD9BC;
        }
        label_0xCBD9BC:
        ;
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x2C2UL))))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCBD9CC;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x147UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCBDA5C;
        }
        else
        {
            goto label_0xCBD9CC;
        }
        label_0xCBD9CC:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x128UL))))));
        __arm64_flags_left_13359568 = unchecked((uint)(x8));
        __arm64_flags_right_13359568 = unchecked((uint)0x1UL);
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13359568) - (__arm64_flags_right_13359568))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_13359568)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13359568)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13359568) - (__arm64_flags_right_13359568))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13359568)) < unchecked((int)0x0UL))))))
        {
            goto label_0xCBDA5C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x98UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCBDE64;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xCBD9E0UL)));
        }
        RuntimeMemory.WriteU8(unchecked((ulong)((x8) + (0x2D0UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x134UL))))));
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x130UL))))));
        __arm64_flags_left_13359596 = unchecked((uint)(x8));
        __arm64_flags_right_13359596 = unchecked((uint)(x9));
        if ((!((unchecked((uint)((__arm64_flags_left_13359596) - (__arm64_flags_right_13359596))) == unchecked((uint)0x0UL)))))
        {
            goto label_0xCBDDE8;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x690UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCBDE64;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xCBD9FCUL)));
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x176A478UL /* metadata target: AudioSource.set_volume */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x690UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCBDE64;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x6B0UL))));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x176A588UL /* metadata target: AudioSource.set_clip */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x690UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCBDE64;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x176A5CCUL /* metadata target: AudioSource.Play */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x118UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCBDE64;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xCBDA34UL)));
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1767EB4UL /* metadata target: Animator.set_speed */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x344UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCBDD90;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x118UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCBDE64;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x810UL))));
        goto label_0xCBDDC0;
        label_0xCBDA5C:
        ;
        x21 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xCBDA60;
        label_0xCBDA60:
        ;
        x0 = unchecked((ulong)(unchecked((uint)(x21))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        __arm64_load_address_13359724 = sp;
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_load_address_13359724)), 0));
        sp = unchecked((ulong)((__arm64_load_address_13359724) + (0x30UL)));
        return unchecked((uint)(x0));
        label_0xCBDA74:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(0xFFFFFFFFFFFFFFFFUL))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x20) + (0x10UL))), unchecked((uint)(x8)));
        if ((x19 == 0x0UL))
        {
            goto label_0xCBDE64;
        }
        else
        {
            goto label_0xCBDA80;
        }
        label_0xCBDA80:
        ;
        x10 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x130UL))))));
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x12CUL))))));
        x11 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x134UL))))));
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x10))) - (unchecked((uint)(x9)))))));
        __arm64_flags_left_13359760 = unchecked((uint)(x11));
        __arm64_flags_right_13359760 = unchecked((uint)(x10));
        RuntimeMemory.WriteU32(unchecked((ulong)((x19) + (0x3B4UL))), unchecked((uint)(x8)));
        RuntimeCalls.Unsupported("b.ne", 0xCBDA98UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xCBDAC8;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x11 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x90UL))));
        if ((x11 == 0x0UL))
        {
            goto label_0xCBDE64;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xCBDAA4UL)));
        }
        RuntimeMemory.WriteU8(unchecked((ulong)((x11) + (0x129UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        x11 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x128UL))))));
        x21 = unchecked((ulong)(unchecked((uint)0x0UL)));
        __arm64_flags_left_13359792 = unchecked((uint)(x11));
        __arm64_flags_right_13359792 = unchecked((uint)(x8));
        __arm64_flags_result_13359792 = unchecked((uint)((__arm64_flags_left_13359792) - (__arm64_flags_right_13359792)));
        x8 = unchecked((ulong)(__arm64_flags_result_13359792));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13359792) - (__arm64_flags_right_13359792))))) < unchecked((int)0x0UL)) == (((unchecked((int)(__arm64_flags_left_13359792)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13359792)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13359792) - (__arm64_flags_right_13359792))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13359792)) < unchecked((int)0x0UL))))))
        {
            goto label_0xCBDAF0;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x11))) + (unchecked((uint)(x9)))))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x19) + (0x12CUL))), unchecked((uint)(x8)));
        RuntimeMemory.WritePtr(unchecked((ulong)((x19) + (0x128UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        goto label_0xCBDA60;
        label_0xCBDAC8:
        ;
        x12 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x128UL))))));
        __arm64_flags_left_13359820 = unchecked((uint)(x8));
        __arm64_flags_right_13359820 = unchecked((uint)(x11));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13359820) - (__arm64_flags_right_13359820))))) < unchecked((int)0x0UL)) == (((unchecked((int)(__arm64_flags_left_13359820)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13359820)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13359820) - (__arm64_flags_right_13359820))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13359820)) < unchecked((int)0x0UL))))))
        {
            goto label_0xCBDAFC;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xCBDAD4UL)));
        }
        __arm64_flags_left_13359828 = unchecked((uint)(x12));
        __arm64_flags_right_13359828 = unchecked((uint)(x8));
        __arm64_flags_result_13359828 = unchecked((uint)((__arm64_flags_left_13359828) - (__arm64_flags_right_13359828)));
        x13 = unchecked((ulong)(__arm64_flags_result_13359828));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13359828) - (__arm64_flags_right_13359828))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_13359828)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13359828)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13359828) - (__arm64_flags_right_13359828))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13359828)) < unchecked((int)0x0UL))))))
        {
            goto label_0xCBDB04;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x3B8UL))))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x19) + (0x12CUL))), unchecked((uint)(x10)));
        RuntimeMemory.WriteU32(unchecked((ulong)((x19) + (0x128UL))), unchecked((uint)(x13)));
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) + (unchecked((uint)(x11)))))));
        goto label_0xCBDB28;
        label_0xCBDAF0:
        ;
        RuntimeMemory.WriteU32(unchecked((ulong)((x19) + (0x128UL))), unchecked((uint)(x8)));
        RuntimeMemory.WriteU32(unchecked((ulong)((x19) + (0x12CUL))), unchecked((uint)(x10)));
        goto label_0xCBDA60;
        label_0xCBDAFC:
        ;
        __arm64_flags_left_13359868 = unchecked((uint)(x12));
        __arm64_flags_right_13359868 = unchecked((uint)(x11));
        __arm64_flags_result_13359868 = unchecked((uint)((__arm64_flags_left_13359868) - (__arm64_flags_right_13359868)));
        x10 = unchecked((ulong)(__arm64_flags_result_13359868));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13359868) - (__arm64_flags_right_13359868))))) < unchecked((int)0x0UL)) == (((unchecked((int)(__arm64_flags_left_13359868)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13359868)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13359868) - (__arm64_flags_right_13359868))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13359868)) < unchecked((int)0x0UL))))))
        {
            goto label_0xCBDB14;
        }
        else
        {
            goto label_0xCBDB04;
        }
        label_0xCBDB04:
        ;
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x12))) + (unchecked((uint)(x9)))))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x19) + (0x12CUL))), unchecked((uint)(x9)));
        RuntimeMemory.WritePtr(unchecked((ulong)((x19) + (0x128UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        goto label_0xCBDB2C;
        label_0xCBDB14:
        ;
        x12 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x3B8UL))))));
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x11))) + (unchecked((uint)(x9)))))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x19) + (0x12CUL))), unchecked((uint)(x9)));
        RuntimeMemory.WriteU32(unchecked((ulong)((x19) + (0x128UL))), unchecked((uint)(x10)));
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x12))) + (unchecked((uint)(x11)))))));
        goto label_0xCBDB28;
        label_0xCBDB28:
        ;
        RuntimeMemory.WriteU32(unchecked((ulong)((x19) + (0x3B8UL))), unchecked((uint)(x9)));
        goto label_0xCBDB2C;
        label_0xCBDB2C:
        ;
        __arm64_flags_left_13359916 = unchecked((uint)(x8));
        __arm64_flags_right_13359916 = unchecked((uint)0x1UL);
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13359916) - (__arm64_flags_right_13359916))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_13359916)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13359916)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13359916) - (__arm64_flags_right_13359916))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13359916)) < unchecked((int)0x0UL))))))
        {
            goto label_0xCBDD78;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x20 = 0x1A8E000UL;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x498UL))));
        x0 = x19;
        x2 = 0x0UL;
        x1 = RuntimeMemory.ReadU64(x20);
        x0 = RuntimeCalls.InvokeDirect(0x1795B9CUL /* metadata target: MonoBehaviour.StartCoroutine */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x110UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCBDE64;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = RuntimeMemory.ReadU64(x20);
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1767884UL /* metadata target: Animator.SetTrigger */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x118UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCBDE64;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x818UL))));
        x2 = 0x0UL;
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x1767884UL /* metadata target: Animator.SetTrigger */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x3B4UL))))));
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x134UL))))));
        __arm64_flags_left_13360004 = unchecked((uint)(x8));
        __arm64_flags_right_13360004 = unchecked((uint)(x9));
        if (((unchecked((uint)((__arm64_flags_left_13360004) - (__arm64_flags_right_13360004))) == unchecked((uint)0x0UL)) || ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13360004) - (__arm64_flags_right_13360004))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_13360004)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13360004)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13360004) - (__arm64_flags_right_13360004))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13360004)) < unchecked((int)0x0UL)))))))
        {
            goto label_0xCBDC08;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x128UL))))));
        __arm64_flags_left_13360016 = unchecked((uint)(x8));
        __arm64_flags_right_13360016 = unchecked((uint)0x0UL);
        if (((unchecked((uint)((__arm64_flags_left_13360016) - (__arm64_flags_right_13360016))) == unchecked((uint)0x0UL)) || ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13360016) - (__arm64_flags_right_13360016))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_13360016)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13360016)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13360016) - (__arm64_flags_right_13360016))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13360016)) < unchecked((int)0x0UL)))))))
        {
            goto label_0xCBDC08;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x690UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCBDE64;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x6B0UL))));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x176A588UL /* metadata target: AudioSource.set_clip */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x80UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCBDE64;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x2DCUL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCBDCCC;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xD8UL))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x20UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCBDBD8;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xCBDBD4UL)));
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCBDBD8;
        label_0xCBDBD8:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1798274UL /* metadata target: Object.op_Implicit */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCBDCCC;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x20UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCBDE64;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x830UL))));
        x2 = 0x0UL;
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x1767884UL /* metadata target: Animator.SetTrigger */, x0, x1, x2, x3);
        goto label_0xCBDCCC;
        label_0xCBDC08:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x690UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCBDE64;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x6B8UL))));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x176A588UL /* metadata target: AudioSource.set_clip */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x110UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCBDE64;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(x8);
        x2 = 0x0UL;
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x1767884UL /* metadata target: Animator.SetTrigger */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x80UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCBDE64;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x2DCUL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCBDCB4;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xD8UL))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x20UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCBDC64;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xCBDC60UL)));
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCBDC64;
        label_0xCBDC64:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1798274UL /* metadata target: Object.op_Implicit */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCBDCB4;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x20UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCBDE64;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x808UL))));
        x2 = 0x0UL;
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x1767884UL /* metadata target: Animator.SetTrigger */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x36CUL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCBDCB4;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x30UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCBDE64;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x7F0UL))));
        x2 = 0x0UL;
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x1767884UL /* metadata target: Animator.SetTrigger */, x0, x1, x2, x3);
        goto label_0xCBDCB4;
        label_0xCBDCB4:
        ;
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179AD30UL /* metadata target: Time.get_time */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x90UL))));
        RuntimeMemory.WriteF32(unchecked((ulong)((x19) + (0x3E8UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        if ((x8 == 0x0UL))
        {
            goto label_0xCBDE64;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xCBDCC8UL)));
        }
        RuntimeMemory.WriteU8(unchecked((ulong)((x8) + (0x129UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        goto label_0xCBDCCC;
        label_0xCBDCCC:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x690UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCBDE64;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xCBDCD4UL)));
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x176A478UL /* metadata target: AudioSource.set_volume */, x0, x1, x2, x3);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x690UL))));
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179AE58UL /* metadata target: Time.get_timeScale */, x0, x1, x2, x3);
        x0 = 0x0UL;
        v8 = v0;
        x0 = RuntimeCalls.InvokeDirect(0x179AE58UL /* metadata target: Time.get_timeScale */, x0, x1, x2, x3);
        x8 = 0x432000UL;
        v1 = v0;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x400UL))))), 0));
        x0 = 0x0UL;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        x0 = RuntimeCalls.InvokeDirect(0x179012CUL /* metadata target: Random.Range */, x0, x1, x2, x3);
        if ((x20 == 0x0UL))
        {
            goto label_0xCBDE64;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x176A500UL /* metadata target: AudioSource.set_pitch */, x0, x1, x2, x3);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x690UL))));
        if ((x20 == 0x0UL))
        {
            goto label_0xCBDE64;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x176A54CUL /* metadata target: AudioSource.get_clip */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x690UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCBDE64;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x21 = x0;
        x0 = x8;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x176A43CUL /* metadata target: AudioSource.get_volume */, x0, x1, x2, x3);
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        x0 = x20;
        x1 = x21;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x176A66CUL /* metadata target: AudioSource.PlayOneShot */, x0, x1, x2, x3);
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179AD30UL /* metadata target: Time.get_time */, x0, x1, x2, x3);
        x21 = unchecked((ulong)(unchecked((uint)0x0UL)));
        RuntimeMemory.WriteF32(unchecked((ulong)((x19) + (0x3C8UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        goto label_0xCBDA60;
        label_0xCBDD78:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x90UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCBDE64;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x21 = unchecked((ulong)(unchecked((uint)0x0UL)));
        RuntimeMemory.WriteU8(unchecked((ulong)((x8) + (0x129UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        RuntimeMemory.WritePtr(unchecked((ulong)((x19) + (0x3B8UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        goto label_0xCBDA60;
        label_0xCBDD90:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x124UL))))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x118UL))));
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) - (unchecked((uint)(0x5UL)))))));
        __arm64_flags_left_13360540 = unchecked((uint)(x8));
        __arm64_flags_right_13360540 = unchecked((uint)0x2UL);
        if (((__arm64_flags_left_13360540 >= __arm64_flags_right_13360540) && (!((unchecked((uint)((__arm64_flags_left_13360540) - (__arm64_flags_right_13360540))) == unchecked((uint)0x0UL))))))
        {
            goto label_0xCBDDB4;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xCBDDA4UL)));
        }
        if ((x0 == 0x0UL))
        {
            goto label_0xCBDE64;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x828UL))));
        goto label_0xCBDDC0;
        label_0xCBDDB4:
        ;
        if ((x0 == 0x0UL))
        {
            goto label_0xCBDE64;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x820UL))));
        goto label_0xCBDDC0;
        label_0xCBDDC0:
        ;
        x1 = RuntimeMemory.ReadU64(x8);
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1767884UL /* metadata target: Animator.SetTrigger */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x110UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCBDE64;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x498UL))));
        x2 = 0x0UL;
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x1767884UL /* metadata target: Animator.SetTrigger */, x0, x1, x2, x3);
        goto label_0xCBDDE8;
        label_0xCBDDE8:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x90UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCBDE64;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x21 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = 0x0UL;
        RuntimeMemory.WriteU8(unchecked((ulong)((x8) + (0x129UL))), unchecked((byte)(unchecked((uint)(x21)))));
        x0 = RuntimeCalls.InvokeDirect(0x179AD30UL /* metadata target: Time.get_time */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x134UL))))));
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x130UL))))));
        RuntimeMemory.WriteF32(unchecked((ulong)((x19) + (0x3C0UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x1E8UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        RuntimeMemory.WritePtr(unchecked((ulong)((x19) + (0x1ECUL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        __arm64_flags_left_13360660 = unchecked((uint)(x8));
        __arm64_flags_right_13360660 = unchecked((uint)(x9));
        if ((unchecked((uint)((__arm64_flags_left_13360660) - (__arm64_flags_right_13360660))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCBDE28;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x3B8UL))))));
        __arm64_flags_left_13360672 = unchecked((uint)(x8));
        __arm64_flags_right_13360672 = unchecked((uint)0x1UL);
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13360672) - (__arm64_flags_right_13360672))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_13360672)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13360672)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13360672) - (__arm64_flags_right_13360672))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13360672)) < unchecked((int)0x0UL))))))
        {
            goto label_0xCBDA80;
        }
        else
        {
            goto label_0xCBDE28;
        }
        label_0xCBDE28:
        ;
        x8 = 0x1A8D000UL;
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x3BCUL))))), 0));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x3E8UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        v0 = v8;
        x1 = 0x0UL;
        x19 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x1799B00UL /* metadata target: WaitForSeconds.ctor */, x0, x1, x2, x3);
        RuntimeMemory.WriteU64(unchecked((ulong)((x20) + (0x18UL))), x19);
        x0 = x20;
        x1 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        RuntimeMemory.WriteU32(unchecked((ulong)((x20) + (0xFFFFFFFFFFFFFFF8UL))), unchecked((uint)(x21)));
        goto label_0xCBDA60;
        label_0xCBDE64:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(uint);
    }
```

## `WeaponBehavior.<Reload>d__361.get_Current` — RVA `0xcbde68`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `private object System.Collections.Generic.IEnumerator<System.Object>.get_Current() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static ulong WeaponBehavior_Reload_d__361_get_Current_RVAcbde68(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x18UL))));
        return x0;
        return default(ulong);
    }
```

## `WeaponBehavior.<Reload>d__361.Reset` — RVA `0xcbde70`

- Lift status: **exact**; input span: 56 bytes; span to next metadata RVA: 56 bytes.
- Metadata signature: `private void System.Collections.IEnumerator.Reset() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=8 (informational only).

```csharp
public static ulong WeaponBehavior_Reload_d__361_Reset_RVAcbde70(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
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
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x838UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D940UL, x0, x1, x2, x3);
        x1 = x0;
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xB7DA4CUL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `WeaponBehavior.<Reload>d__361.get_Current` — RVA `0xcbdea8`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `private object System.Collections.IEnumerator.get_Current() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static ulong WeaponBehavior_Reload_d__361_get_Current_RVAcbdea8(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x18UL))));
        return x0;
        return default(ulong);
    }
```
