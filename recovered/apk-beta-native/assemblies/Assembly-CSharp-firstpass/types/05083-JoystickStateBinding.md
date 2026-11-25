# `JoystickStateBinding` — TypeDefIndex 5083

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x20` | `AxisBinding` | `horzAxisBinding` |
| `0x28` | `AxisBinding` | `vertAxisBinding` |
| `0x30` | `DirectionBinding` | `dirBinding` |

## `JoystickStateBinding.ctor` — RVA `0xc5de7c`

- Lift status: **exact**; input span: 248 bytes; span to next metadata RVA: 248 bytes.
- Metadata signature: `public void .ctor(InputBindingBase parent) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=38 (informational only).

```csharp
public static ulong JoystickStateBinding_ctor_RVAc5de7c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x22 = default(ulong);
        ulong x23 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFD0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFD0UL)))) + (0x8UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x19);
        x23 = 0x1BAB000UL;
        x22 = 0x1A8C000UL;
        x21 = 0x1A8D000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x23) + (0x2D4UL))))))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x990UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x38UL))));
        x20 = x1;
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC5DECC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x990UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x38UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x23) + (0x2D4UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC5DECC;
        label_0xC5DECC:
        ;
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1589338UL /* metadata target: Object.ctor */, x0, x1, x2, x3);
        x0 = x19;
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x10UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x18UL))), x20);
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x10UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        x0 = RuntimeMemory.ReadU64(x22);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = x19;
        x2 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC4EAC4UL /* metadata target: AxisBinding.ctor */, x0, x1, x2, x3);
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x20UL))), x20);
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x22);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = x19;
        x2 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC4EAC4UL /* metadata target: AxisBinding.ctor */, x0, x1, x2, x3);
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x28UL))), x20);
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x21);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = x19;
        x2 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC5C9ECUL /* metadata target: DirectionBinding.ctor */, x0, x1, x2, x3);
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x30UL))), x20);
        x0 = x19;
        x1 = x20;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeDirect(0xB7D8D0UL);
        return default(ulong);
    }
```

## `JoystickStateBinding.CopyFrom` — RVA `0xc5df74`

- Lift status: **exact**; input span: 136 bytes; span to next metadata RVA: 136 bytes.
- Metadata signature: `public void CopyFrom(JoystickStateBinding b) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=19 (informational only).

```csharp
public static ulong JoystickStateBinding_CopyFrom_RVAc5df74(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        if ((x1 == 0x0UL))
        {
            goto label_0xC5DFF8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x1) + (0x10UL))))))));
        x19 = x1;
        x20 = x0;
        RuntimeMemory.WriteU8(unchecked((ulong)((x0) + (0x10UL))), unchecked((byte)(unchecked((uint)(x8)))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC5DFEC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x9 = x20;
        goto label_0xC5DF9C;
        label_0xC5DF9C:
        ;
        RuntimeMemory.WriteU8(unchecked((ulong)((x9) + (0x10UL))), unchecked((byte)(unchecked((uint)(x8)))));
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0x18UL))));
        if ((x9 != 0x0UL))
        {
            goto label_0xC5DF9C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x30UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC5DFF8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x30UL))));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC5CC2CUL /* metadata target: DirectionBinding.CopyFrom */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x20UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC5DFF8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x20UL))));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC5B53CUL /* metadata target: AxisBinding.CopyFrom */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x28UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC5DFF8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x28UL))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x2 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0xC5B53CUL /* metadata target: AxisBinding.CopyFrom */);
        label_0xC5DFEC:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        label_0xC5DFF8:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `JoystickStateBinding.SyncJoyState` — RVA `0xc5dffc`

- Lift status: **exact**; input span: 236 bytes; span to next metadata RVA: 236 bytes.
- Metadata signature: `public void SyncJoyState(JoystickState state, InputRig rig) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=35 (informational only).

```csharp
public static ulong JoystickStateBinding_SyncJoyState_RVAc5dffc(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_load_address_12968060 = default(ulong);
        ulong __arm64_load_address_12968156 = default(ulong);
        ulong __arm64_pair_address_12968076 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x22 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteF64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFD0UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        sp = unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFD0UL)));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x8UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x19);
        x22 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x22) + (0x2D5UL))))))));
        x19 = x2;
        x20 = x1;
        x21 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC5E038;
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
        RuntimeMemory.WriteU8(unchecked((ulong)((x22) + (0x2D5UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC5E038;
        label_0xC5E038:
        ;
        if ((x20 == 0x0UL))
        {
            goto label_0xC5E070;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x10UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC5E070;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xD8UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC5E05C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC5E058UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC5E05C;
        label_0xC5E05C:
        ;
        x0 = x19;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179568CUL /* metadata target: Object.op_Equality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC5E084;
        }
        else
        {
            goto label_0xC5E070;
        }
        label_0xC5E070:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        __arm64_load_address_12968060 = sp;
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_load_address_12968060)), 0));
        return x0;
        label_0xC5E084:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x20UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC5E0E4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC5E08CUL);
        }
        __arm64_pair_address_12968076 = unchecked((ulong)((x20) + (0x24UL)));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12968076)), 0));
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12968076) + (0x4UL))))), 0));
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x2 = x19;
        x3 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC4F160UL /* metadata target: AxisBinding.SyncFloat */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x28UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC5E0E4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        v0 = v8;
        x2 = x19;
        x3 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC4F160UL /* metadata target: AxisBinding.SyncFloat */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x30UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC5E0E4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x40UL))));
        x2 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        x3 = 0x0UL;
        __arm64_load_address_12968156 = sp;
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_load_address_12968156)), 0));
        sp = unchecked((ulong)((__arm64_load_address_12968156) + (0x30UL)));
        return RuntimeCalls.InvokeDirect(0xC5CFA0UL /* metadata target: DirectionBinding.SyncDirectionState */);
        label_0xC5E0E4:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `JoystickStateBinding.OnIsBoundToAxis` — RVA `0xc5e0e8`

- Lift status: **exact**; input span: 148 bytes; span to next metadata RVA: 148 bytes.
- Metadata signature: `protected override bool OnIsBoundToAxis(string axisName, InputRig rig) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=23 (informational only).

```csharp
public static uint JoystickStateBinding_OnIsBoundToAxis_RVAc5e0e8(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
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
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x10UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC5E144;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x21 = x0;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x20UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC5E178;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x19 = x2;
        x20 = x1;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x1E8UL))));
        x3 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x1E8UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC5E13C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x28UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC5E178;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x1 = x20;
        x2 = x19;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x1E8UL))));
        x3 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x1E8UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC5E154;
        }
        else
        {
            goto label_0xC5E13C;
        }
        label_0xC5E13C:
        ;
        x0 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        goto label_0xC5E148;
        label_0xC5E144:
        ;
        x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xC5E148;
        label_0xC5E148:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return unchecked((uint)(x0));
        label_0xC5E154:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x30UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC5E178;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x1 = x20;
        x2 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x4 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x1E8UL))));
        x3 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x1E8UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return unchecked((uint)(RuntimeCalls.InvokeIndirect(x4)));
        label_0xC5E178:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(uint);
    }
```

## `JoystickStateBinding.OnIsBoundToKey` — RVA `0xc5e17c`

- Lift status: **exact**; input span: 148 bytes; span to next metadata RVA: 148 bytes.
- Metadata signature: `protected override bool OnIsBoundToKey(KeyCode keyCode, InputRig rig) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=23 (informational only).

```csharp
public static uint JoystickStateBinding_OnIsBoundToKey_RVAc5e17c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
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
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x10UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC5E1D8;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x21 = x0;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x20UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC5E20C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x19 = x2;
        x20 = unchecked((ulong)(unchecked((uint)(x1))));
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x1D8UL))));
        x3 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x1D8UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC5E1D0;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x28UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC5E20C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x1 = unchecked((ulong)(unchecked((uint)(x20))));
        x2 = x19;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x1D8UL))));
        x3 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x1D8UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC5E1E8;
        }
        else
        {
            goto label_0xC5E1D0;
        }
        label_0xC5E1D0:
        ;
        x0 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        goto label_0xC5E1DC;
        label_0xC5E1D8:
        ;
        x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xC5E1DC;
        label_0xC5E1DC:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return unchecked((uint)(x0));
        label_0xC5E1E8:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x30UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC5E20C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x1 = unchecked((ulong)(unchecked((uint)(x20))));
        x2 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x4 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x1D8UL))));
        x3 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x1D8UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return unchecked((uint)(RuntimeCalls.InvokeIndirect(x4)));
        label_0xC5E20C:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        return default(uint);
    }
```

## `JoystickStateBinding.OnGetSubBindingDescriptions` — RVA `0xc5e210`

- Lift status: **exact**; input span: 216 bytes; span to next metadata RVA: 216 bytes.
- Metadata signature: `protected override void OnGetSubBindingDescriptions(BindingDescriptionList descList, Object undoObject, string parentMenuPath) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=40 (informational only).

```csharp
public static ulong JoystickStateBinding_OnGetSubBindingDescriptions_RVAc5e210(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x22 = default(ulong);
        ulong x23 = default(ulong);
        ulong x24 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFC0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x24);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))), x19);
        x23 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x23) + (0x2D6UL))))))));
        x20 = x3;
        x19 = x2;
        x21 = x1;
        x22 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC5E268;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x538UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x548UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x40UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x23) + (0x2D6UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC5E268;
        label_0xC5E268:
        ;
        if ((x21 == 0x0UL))
        {
            goto label_0xC5E2E4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x548UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x20UL))));
        x23 = 0x1A8C000UL;
        x24 = 0x1A8D000UL;
        x3 = RuntimeMemory.ReadU64(x8);
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0x538UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((x24) + (0x40UL))));
        x2 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xC5DAACUL /* metadata target: BindingDescriptionList.Add */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x28UL))));
        x3 = RuntimeMemory.ReadU64(x23);
        x2 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = x21;
        x5 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xC5DAACUL /* metadata target: BindingDescriptionList.Add */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x30UL))));
        x2 = RuntimeMemory.ReadU64(x24);
        x0 = x21;
        x3 = x20;
        x4 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0xC5D750UL /* metadata target: BindingDescriptionList.Add */);
        label_0xC5E2E4:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```
