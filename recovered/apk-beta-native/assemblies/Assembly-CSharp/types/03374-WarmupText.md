# `WarmupText` — TypeDefIndex 3374

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x20` | `float` | `warmupGui` |
| `0x24` | `float` | `oldWarmup` |
| `0x28` | `Color` | `textColor` |
| `0x38` | `bool` | `waveBegins` |
| `0x39` | `bool` | `waveComplete` |
| `0x40` | `Text` | `uiTextComponent` |

## `WarmupText.OnEnable` — RVA `0xc9281c`

- Lift status: **exact**; input span: 100 bytes; span to next metadata RVA: 100 bytes.
- Metadata signature: `private void OnEnable() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=15 (informational only).

```csharp
public static ulong WarmupText_OnEnable_RVAc9281c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
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
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x459UL))))))));
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
            RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x459UL))), unchecked((byte)(unchecked((uint)(x8)))));
        }
        label_0xC92850:
        ;
        x1 = RuntimeMemory.ReadU64(x21);
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xE31BC8UL, x0, x1, x2, x3);
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x40UL))), x0);
        x1 = x0;
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0xFFFFFFFFC4000000UL))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x19) + (0xFFFFFFFFFFFFFFE4UL))), unchecked((uint)(x8)));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return x0;
        return default(ulong);
    }
```

## `WarmupText.Update` — RVA `0xc92880`

- Lift status: **partial**; input span: 424 bytes; span to next metadata RVA: 424 bytes.
- Metadata signature: `private void Update() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=46 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'frintp' at 0xc9298c; reason: Unsupported instruction 'frintm' at 0xc9299c

```csharp
public static ulong WarmupText_Update_RVAc92880(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        double __arm64_fcvtz_source_13183340 = default(double);
        ulong __arm64_flags_left_13183352 = default(ulong);
        ulong __arm64_flags_result_13183352 = default(ulong);
        ulong __arm64_flags_right_13183352 = default(ulong);
        float __arm64_float_flags_left_13183188 = default(float);
        float __arm64_float_flags_left_13183288 = default(float);
        double __arm64_float_flags_left_13183300 = default(double);
        double __arm64_float_flags_left_13183324 = default(double);
        float __arm64_float_flags_right_13183188 = default(float);
        float __arm64_float_flags_right_13183288 = default(float);
        double __arm64_float_flags_right_13183300 = default(double);
        double __arm64_float_flags_right_13183324 = default(double);
        ulong __arm64_pair_address_13183184 = default(ulong);
        ulong __arm64_pair_address_13183476 = default(ulong);
        ulong __arm64_pair_address_13183480 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        sp = unchecked((ulong)((sp) - (0x30UL)));
        RuntimeMemory.WriteF64(unchecked((ulong)((sp) + (0x10UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x18UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x19);
        x20 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x45AUL))))))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC928CC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x130UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x138UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x140UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x45AUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC928CC;
        label_0xC928CC:
        ;
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0x4UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        __arm64_pair_address_13183184 = unchecked((ulong)((x19) + (0x20UL)));
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13183184)), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13183184) + (0x4UL))))), 0));
        __arm64_float_flags_left_13183188 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13183188 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        if ((__arm64_float_flags_left_13183188 == __arm64_float_flags_right_13183188))
        {
            goto label_0xC92A10;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x39UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC92908;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x40UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC92A24;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(x0);
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0x138UL))));
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x5F0UL))));
        x1 = RuntimeMemory.ReadU64(x9);
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x5E8UL))));
        goto label_0xC929E4;
        label_0xC92908:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x38UL))))))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x40UL))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC9292C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC92914UL);
        }
        if ((x20 == 0x0UL))
        {
            goto label_0xC92A24;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(x20);
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0x130UL))));
        x1 = RuntimeMemory.ReadU64(x9);
        goto label_0xC929D8;
        label_0xC9292C:
        ;
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(unchecked((double)(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)))), 0));
        x0 = unchecked((ulong)((sp) + (0x8UL)));
        x0 = RuntimeCalls.InvokeDirect(0x19B0C60UL, x0, x1, x2, x3);
        __arm64_float_flags_left_13183288 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13183288 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        if ((__arm64_float_flags_left_13183288 >= __arm64_float_flags_right_13183288))
        {
            goto label_0xC92958;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC92940UL);
        }
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(global::System.BitConverter.Int64BitsToDouble(unchecked((long)0xBFE0000000000000UL))), 0));
        __arm64_float_flags_left_13183300 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0))));
        __arm64_float_flags_right_13183300 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0))));
        if (((__arm64_float_flags_left_13183300 != __arm64_float_flags_right_13183300) || ((__arm64_float_flags_left_13183300 != __arm64_float_flags_left_13183300) || (__arm64_float_flags_right_13183300 != __arm64_float_flags_right_13183300))))
        {
            goto label_0xC92984;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC9294CUL);
        }
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((sp) + (0x8UL))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0xBF800000UL)), 0)), 0));
        goto label_0xC9296C;
        label_0xC92958:
        ;
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(global::System.BitConverter.Int64BitsToDouble(unchecked((long)0x3FE0000000000000UL))), 0));
        __arm64_float_flags_left_13183324 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0))));
        __arm64_float_flags_right_13183324 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0))));
        if (((__arm64_float_flags_left_13183324 != __arm64_float_flags_right_13183324) || ((__arm64_float_flags_left_13183324 != __arm64_float_flags_left_13183324) || (__arm64_float_flags_right_13183324 != __arm64_float_flags_right_13183324))))
        {
            goto label_0xC92994;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC92964UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((sp) + (0x8UL))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        goto label_0xC9296C;
        label_0xC9296C:
        ;
        __arm64_fcvtz_source_13183340 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0))));
        x8 = unchecked((ulong)(((__arm64_fcvtz_source_13183340 != __arm64_fcvtz_source_13183340) ? unchecked((long)0x0UL) : ((__arm64_fcvtz_source_13183340 >= global::System.BitConverter.Int64BitsToDouble(unchecked((long)0x43E0000000000000UL))) ? unchecked((long)0x7FFFFFFFFFFFFFFFUL) : ((__arm64_fcvtz_source_13183340 < global::System.BitConverter.Int64BitsToDouble(unchecked((long)0xC3E0000000000000UL))) ? unchecked((long)0x8000000000000000UL) : unchecked((long)(__arm64_fcvtz_source_13183340)))))));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)(global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0))))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        __arm64_flags_left_13183352 = x8;
        __arm64_flags_right_13183352 = 0x1UL;
        __arm64_flags_result_13183352 = unchecked((ulong)((__arm64_flags_left_13183352) & (__arm64_flags_right_13183352)));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_flags_result_13183352 == 0x0UL) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))), 0));
        goto label_0xC929A0;
        label_0xC92984:
        ;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0xBF000000UL)), 0)), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        RuntimeCalls.Unsupported("frintp", 0xC9298CUL);
        goto label_0xC929A0;
        label_0xC92994:
        ;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F000000UL)), 0)), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        RuntimeCalls.Unsupported("frintm", 0xC9299CUL);
        goto label_0xC929A0;
        label_0xC929A0:
        ;
        x0 = unchecked((ulong)((sp) + (0x4UL)));
        x1 = 0x0UL;
        RuntimeMemory.WriteF32(unchecked((ulong)((sp) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        x0 = RuntimeCalls.InvokeDirect(0x1559468UL /* metadata target: Single.ToString */, x0, x1, x2, x3);
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x140UL))));
        x1 = x0;
        x2 = 0x0UL;
        x8 = RuntimeMemory.ReadU64(x8);
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0x13ED2C8UL /* metadata target: String.Concat */, x0, x1, x2, x3);
        if ((x20 == 0x0UL))
        {
            goto label_0xC92A24;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x20);
        x1 = x0;
        goto label_0xC929D8;
        label_0xC929D8:
        ;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x5E8UL))));
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x5F0UL))));
        x0 = x20;
        goto label_0xC929E4;
        label_0xC929E4:
        ;
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x40UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC92A24;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x0);
        __arm64_pair_address_13183476 = unchecked((ulong)((x19) + (0x30UL)));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13183476)), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13183476) + (0x4UL))))), 0));
        __arm64_pair_address_13183480 = unchecked((ulong)((x19) + (0x28UL)));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13183480)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13183480) + (0x4UL))))), 0));
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x2A8UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x2B0UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x20UL))))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((x19) + (0x24UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        goto label_0xC92A10;
        label_0xC92A10:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x18UL))));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((sp) + (0x10UL))))), 0));
        sp = unchecked((ulong)((sp) + (0x30UL)));
        return x0;
        label_0xC92A24:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `WarmupText.ctor` — RVA `0xc92a28`

- Lift status: **exact**; input span: 16 bytes; span to next metadata RVA: 16 bytes.
- Metadata signature: `public void .ctor() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=2 (informational only).

```csharp
public static ulong WarmupText_ctor_RVAc92a28(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong x8 = default(ulong);
        x8 = unchecked((ulong)(unchecked((uint)(0xFFFFFFFFC4000000UL))));
        x1 = 0x0UL;
        RuntimeMemory.WriteU32(unchecked((ulong)((x0) + (0x24UL))), unchecked((uint)(x8)));
        return RuntimeCalls.InvokeDirect(0x1796274UL /* metadata target: MonoBehaviour.ctor */);
        return default(ulong);
    }
```
