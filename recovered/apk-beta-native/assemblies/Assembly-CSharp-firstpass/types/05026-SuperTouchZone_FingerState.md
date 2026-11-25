# `SuperTouchZone.FingerState` — TypeDefIndex 5026

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x10` | `SuperTouchZone` | `zone` |
| `0x18` | `TouchObject` | `touchObj` |
| `0x20` | `TouchControl.TouchStartType` | `touchStartType` |
| `0x24` | `int` | `emuTouchId` |
| `0x28` | `TouchGestureBasicState` | `touchScreen` |
| `0x30` | `TouchGestureBasicState` | `touchOriented` |

## `SuperTouchZone.FingerState.ctor` — RVA `0xc4943c`

- Lift status: **exact**; input span: 200 bytes; span to next metadata RVA: 200 bytes.
- Metadata signature: `public void .ctor(SuperTouchZone zone) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=29 (informational only).

```csharp
public static ulong SuperTouchZone_FingerState_ctor_RVAc4943c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x22 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFD0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x19);
        x22 = 0x1BAB000UL;
        x21 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x22) + (0x23DUL))))))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x958UL))));
        x20 = x1;
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
        }
        else
        {
            x0 = 0x1A8C000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x958UL))));
            // Likely IL2CPP class initialization helper (guarded call).
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
            RuntimeMemory.WriteU8(unchecked((ulong)((x22) + (0x23DUL))), unchecked((byte)(unchecked((uint)(x8)))));
        }
        label_0xC49478:
        ;
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1589338UL /* metadata target: Object.ctor */, x0, x1, x2, x3);
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x10UL))), x20);
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = x19;
        RuntimeMemory.WritePtr(unchecked((ulong)((x0) + (0x18UL))), 0x0UL);
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x21);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC61AE0UL /* metadata target: TouchGestureBasicState.ctor */, x0, x1, x2, x3);
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x28UL))), x20);
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x21);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC61AE0UL /* metadata target: TouchGestureBasicState.ctor */, x0, x1, x2, x3);
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x30UL))), x20);
        x0 = x19;
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0xFFFFFFFFFFFFFFFFUL))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x19) + (0xFFFFFFFFFFFFFFF4UL))), unchecked((uint)(x8)));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        return default(ulong);
    }
```

## `SuperTouchZone.FingerState.Reset` — RVA `0xc49b48`

- Lift status: **exact**; input span: 56 bytes; span to next metadata RVA: 56 bytes.
- Metadata signature: `public void Reset() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=8 (informational only).

```csharp
public static ulong SuperTouchZone_FingerState_Reset_RVAc49b48(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x8UL))), x19);
        x19 = x0;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x28UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC49B7C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x178UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x178UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x30UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC49B7C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x178UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x178UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeIndirect(x2);
        label_0xC49B7C:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `SuperTouchZone.FingerState.Update` — RVA `0xc4b078`

- Lift status: **exact**; input span: 56 bytes; span to next metadata RVA: 56 bytes.
- Metadata signature: `public void Update() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=8 (informational only).

```csharp
public static ulong SuperTouchZone_FingerState_Update_RVAc4b078(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x8UL))), x19);
        x19 = x0;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x28UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC4B0AC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x188UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x188UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x30UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC4B0AC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x188UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x188UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeIndirect(x2);
        label_0xC4B0AC:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `SuperTouchZone.FingerState.OnTouchStart` — RVA `0xc4bed8`

- Lift status: **partial**; input span: 280 bytes; span to next metadata RVA: 280 bytes.
- Metadata signature: `public bool OnTouchStart(TouchObject touchObj, float delay, TouchControl.TouchStartType touchStartType) { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=39 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'csel' at 0xc4bf38; reason: Unknown IR expression at 0xc4bf38; reason: Unsupported instruction 'csel' at 0xc4bf3c; reason: Unknown IR expression at 0xc4bf3c; reason: Unsupported instruction 'cset' at 0xc4bfe0; reason: Unknown IR expression at 0xc4bfe0

```csharp
public static uint SuperTouchZone_FingerState_OnTouchStart_RVAc4bed8(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12893988 = default(uint);
        ulong __arm64_flags_left_12894156 = default(ulong);
        uint __arm64_flags_right_12893988 = default(uint);
        ulong __arm64_flags_right_12894156 = default(ulong);
        ulong __arm64_load_address_12894180 = default(ulong);
        ulong __arm64_pair_address_12893916 = default(ulong);
        ulong __arm64_pair_address_12894028 = default(ulong);
        ulong __arm64_pair_address_12894104 = default(ulong);
        ulong __arm64_pair_address_12894172 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v10 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
        RuntimeVector128 v4 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        RuntimeVector128 v9 = default(RuntimeVector128);
        ulong x10 = default(ulong);
        ulong x11 = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x22 = default(ulong);
        ulong x23 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteF64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFB0UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v10.GetUInt64(0)))));
        sp = unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFB0UL)));
        __arm64_pair_address_12893916 = unchecked((ulong)((sp) + (0x10UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12893916, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12893916) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))), x19);
        x19 = x0;
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x18UL))));
        if ((x23 != 0x0UL))
        {
            goto label_0xC4BFCC;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x21 = x0;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x18UL))), x1);
        x0 = x19;
        x22 = unchecked((ulong)(unchecked((uint)(x2))));
        v8 = v0;
        x20 = x1;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        RuntimeMemory.WriteU32(unchecked((ulong)((x21) + (0x20UL))), unchecked((uint)(x22)));
        if ((x20 == 0x0UL))
        {
            goto label_0xC4BFEC;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x28UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC4BFEC;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC4BF24UL)));
        }
        __arm64_flags_left_12893988 = unchecked((uint)(x22));
        __arm64_flags_right_12893988 = unchecked((uint)0x0UL);
        x8 = unchecked((ulong)(unchecked((uint)(0x24UL))));
        x9 = unchecked((ulong)(unchecked((uint)(0x2CUL))));
        x10 = unchecked((ulong)(unchecked((uint)(0x20UL))));
        x11 = unchecked((ulong)(unchecked((uint)(0x28UL))));
        RuntimeCalls.Unsupported("csel", 0xC4BF38UL);
        x8 = (__Unsupported<bool>("Unknown IR expression") ? x9 : x8);
        RuntimeCalls.Unsupported("csel", 0xC4BF3CUL);
        x9 = (__Unsupported<bool>("Unknown IR expression") ? x11 : x10);
        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x20) + (x8))))), 0));
        v10 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x20) + (x9))))), 0));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x18UL))));
        __arm64_pair_address_12894028 = unchecked((ulong)((x20) + (0x20UL)));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12894028)), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12894028) + (0x4UL))))), 0));
        v1 = v9;
        v0 = v10;
        v4 = v8;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC61F0CUL /* metadata target: TouchGestureBasicState.OnTouchStart */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x10UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC4BFEC;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x30UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x30UL))));
        v0 = v10;
        v1 = v9;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC51588UL /* metadata target: TouchControl.ScreenToOrientedPos */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x10UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC4BFEC;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        v9 = v0;
        v10 = v1;
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x30UL))));
        __arm64_pair_address_12894104 = unchecked((ulong)((x20) + (0x20UL)));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12894104)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12894104) + (0x4UL))))), 0));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC51588UL /* metadata target: TouchControl.ScreenToOrientedPos */, x0, x1, x2, x3);
        if ((x22 == 0x0UL))
        {
            goto label_0xC4BFEC;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = RuntimeMemory.ReadU64(x19);
        v2 = v0;
        v3 = v1;
        x0 = x22;
        v0 = v9;
        v1 = v10;
        v4 = v8;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC61F0CUL /* metadata target: TouchGestureBasicState.OnTouchStart */, x0, x1, x2, x3);
        goto label_0xC4BFCC;
        label_0xC4BFCC:
        ;
        __arm64_flags_left_12894156 = x23;
        __arm64_flags_right_12894156 = 0x0UL;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x40UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        __arm64_pair_address_12894172 = unchecked((ulong)((sp) + (0x10UL)));
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12894172)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12894172) + (0x8UL))))), 0));
        RuntimeCalls.Unsupported("cset", 0xC4BFE0UL);
        x0 = unchecked((ulong)((__Unsupported<bool>("Unknown IR expression") ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        __arm64_load_address_12894180 = sp;
        v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_load_address_12894180)), 0));
        sp = unchecked((ulong)((__arm64_load_address_12894180) + (0x50UL)));
        return unchecked((uint)(x0));
        label_0xC4BFEC:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        return default(uint);
    }
```

## `SuperTouchZone.FingerState.OnTouchEnd` — RVA `0xc4c098`

- Lift status: **partial**; input span: 184 bytes; span to next metadata RVA: 184 bytes.
- Metadata signature: `public bool OnTouchEnd(TouchObject touchObj, TouchControl.TouchEndType touchEndType) { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=19 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'cset' at 0xc4c0d8; reason: Unknown IR expression at 0xc4c0d8; reason: Unsupported instruction 'cset' at 0xc4c13c; reason: Unknown IR expression at 0xc4c13c

```csharp
public static uint SuperTouchZone_FingerState_OnTouchEnd_RVAc4c098(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_flags_left_12894384 = default(ulong);
        uint __arm64_flags_left_12894416 = default(uint);
        uint __arm64_flags_left_12894468 = default(uint);
        ulong __arm64_flags_left_12894504 = default(ulong);
        ulong __arm64_flags_left_12894512 = default(ulong);
        ulong __arm64_flags_right_12894384 = default(ulong);
        uint __arm64_flags_right_12894416 = default(uint);
        uint __arm64_flags_right_12894468 = default(uint);
        ulong __arm64_flags_right_12894504 = default(ulong);
        ulong __arm64_flags_right_12894512 = default(ulong);
        ulong __arm64_pair_address_12894412 = default(ulong);
        ulong __arm64_pair_address_12894448 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
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
        x20 = x0;
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x18UL))));
        x19 = x1;
        __arm64_flags_left_12894384 = x23;
        __arm64_flags_right_12894384 = x1;
        if ((!((unchecked((ulong)((__arm64_flags_left_12894384) - (__arm64_flags_right_12894384))) == 0x0UL))))
        {
            goto label_0xC4C128;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC4C0B8UL)));
        }
        if ((x23 == 0x0UL))
        {
            goto label_0xC4C128;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC4C0BCUL)));
        }
        if ((x19 == 0x0UL))
        {
            goto label_0xC4C14C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x22 = x0;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x28UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC4C14C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC4C0CCUL)));
        }
        __arm64_pair_address_12894412 = unchecked((ulong)((x19) + (0x20UL)));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12894412)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12894412) + (0x4UL))))), 0));
        __arm64_flags_left_12894416 = unchecked((uint)(x2));
        __arm64_flags_right_12894416 = unchecked((uint)0x0UL);
        x21 = unchecked((ulong)(unchecked((uint)(x2))));
        RuntimeCalls.Unsupported("cset", 0xC4C0D8UL);
        x1 = unchecked((ulong)((__Unsupported<bool>("Unknown IR expression") ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC61FD4UL /* metadata target: TouchGestureBasicState.OnTouchEnd */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x10UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC4C14C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x30UL))));
        __arm64_pair_address_12894448 = unchecked((ulong)((x19) + (0x20UL)));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12894448)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12894448) + (0x4UL))))), 0));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x30UL))));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC51588UL /* metadata target: TouchControl.ScreenToOrientedPos */, x0, x1, x2, x3);
        if ((x22 == 0x0UL))
        {
            goto label_0xC4C14C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC4C104UL)));
        }
        __arm64_flags_left_12894468 = unchecked((uint)(x21));
        __arm64_flags_right_12894468 = unchecked((uint)0x0UL);
        x1 = unchecked((ulong)(((!((unchecked((uint)((__arm64_flags_left_12894468) - (__arm64_flags_right_12894468))) == unchecked((uint)0x0UL)))) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        x0 = x22;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC61FD4UL /* metadata target: TouchGestureBasicState.OnTouchEnd */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = x20;
        x1 = 0x0UL;
        RuntimeMemory.WritePtr(x20, 0x0UL);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        goto label_0xC4C128;
        label_0xC4C128:
        ;
        __arm64_flags_left_12894504 = x23;
        __arm64_flags_right_12894504 = 0x0UL;
        x8 = unchecked((ulong)(((!((unchecked((ulong)((__arm64_flags_left_12894504) - (__arm64_flags_right_12894504))) == 0x0UL))) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        __arm64_flags_left_12894512 = x23;
        __arm64_flags_right_12894512 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        RuntimeCalls.Unsupported("cset", 0xC4C13CUL);
        x9 = unchecked((ulong)((__Unsupported<bool>("Unknown IR expression") ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        x0 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) & (unchecked((uint)(x8)))))));
        x30 = RuntimeMemory.ReadU64(sp);
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return unchecked((uint)(x0));
        label_0xC4C14C:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        return default(uint);
    }
```

## `SuperTouchZone.FingerState.OnTouchMove` — RVA `0xc4c1f0`

- Lift status: **partial**; input span: 156 bytes; span to next metadata RVA: 156 bytes.
- Metadata signature: `public bool OnTouchMove(TouchObject touchObj) { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=16 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'cset' at 0xc4c278; reason: Unknown IR expression at 0xc4c278

```csharp
public static uint SuperTouchZone_FingerState_OnTouchMove_RVAc4c1f0(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_flags_left_12894724 = default(ulong);
        ulong __arm64_flags_left_12894820 = default(ulong);
        ulong __arm64_flags_left_12894828 = default(ulong);
        ulong __arm64_flags_right_12894724 = default(ulong);
        ulong __arm64_flags_right_12894820 = default(ulong);
        ulong __arm64_flags_right_12894828 = default(ulong);
        ulong __arm64_pair_address_12894772 = default(ulong);
        ulong __arm64_pair_address_12894792 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x22 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFD0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x19);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x18UL))));
        x19 = x1;
        __arm64_flags_left_12894724 = x21;
        __arm64_flags_right_12894724 = x1;
        if ((!((unchecked((ulong)((__arm64_flags_left_12894724) - (__arm64_flags_right_12894724))) == 0x0UL))))
        {
            goto label_0xC4C264;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC4C20CUL)));
        }
        if ((x21 == 0x0UL))
        {
            goto label_0xC4C264;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC4C210UL)));
        }
        if ((x19 == 0x0UL))
        {
            goto label_0xC4C288;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x28UL))));
        x20 = x0;
        if ((x8 == 0x0UL))
        {
            goto label_0xC4C288;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC4C220UL)));
        }
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((x19) + (0x20UL))))), 0));
        RuntimeMemory.WriteF64(unchecked((ulong)((x8) + (0xB0UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x10UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC4C288;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x30UL))));
        __arm64_pair_address_12894772 = unchecked((ulong)((x19) + (0x20UL)));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12894772)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12894772) + (0x4UL))))), 0));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x30UL))));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC51588UL /* metadata target: TouchControl.ScreenToOrientedPos */, x0, x1, x2, x3);
        if ((x22 == 0x0UL))
        {
            goto label_0xC4C288;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC4C248UL)));
        }
        __arm64_pair_address_12894792 = unchecked((ulong)((x22) + (0xB0UL)));
        RuntimeMemory.WriteF32(__arm64_pair_address_12894792, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_12894792) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x10UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC4C288;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x2 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x20) + (0x20UL))))));
        x1 = x19;
        x3 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC4F6E0UL /* metadata target: TouchControl.CheckSwipeOff */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC4C264;
        label_0xC4C264:
        ;
        __arm64_flags_left_12894820 = x21;
        __arm64_flags_right_12894820 = 0x0UL;
        x8 = unchecked((ulong)(((!((unchecked((ulong)((__arm64_flags_left_12894820) - (__arm64_flags_right_12894820))) == 0x0UL))) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        __arm64_flags_left_12894828 = x21;
        __arm64_flags_right_12894828 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        RuntimeCalls.Unsupported("cset", 0xC4C278UL);
        x9 = unchecked((ulong)((__Unsupported<bool>("Unknown IR expression") ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        x0 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) & (unchecked((uint)(x8)))))));
        x30 = RuntimeMemory.ReadU64(sp);
        return unchecked((uint)(x0));
        label_0xC4C288:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, unchecked((ulong)(unchecked((uint)(x0)))), x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        return default(uint);
    }
```

## `SuperTouchZone.FingerState.OnTouchPressureChange` — RVA `0xc4c304`

- Lift status: **partial**; input span: 112 bytes; span to next metadata RVA: 112 bytes.
- Metadata signature: `public bool OnTouchPressureChange(TouchObject touchObj) { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=10 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'cset' at 0xc4c360; reason: Unknown IR expression at 0xc4c360

```csharp
public static uint SuperTouchZone_FingerState_OnTouchPressureChange_RVAc4c304(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_flags_left_12894996 = default(ulong);
        ulong __arm64_flags_left_12895056 = default(ulong);
        ulong __arm64_flags_left_12895064 = default(ulong);
        ulong __arm64_flags_right_12894996 = default(ulong);
        ulong __arm64_flags_right_12895056 = default(ulong);
        ulong __arm64_flags_right_12895064 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
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
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x18UL))));
        x19 = x1;
        __arm64_flags_left_12894996 = x21;
        __arm64_flags_right_12894996 = x1;
        if ((!((unchecked((ulong)((__arm64_flags_left_12894996) - (__arm64_flags_right_12894996))) == 0x0UL))))
        {
            goto label_0xC4C350;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC4C31CUL)));
        }
        if ((x21 == 0x0UL))
        {
            goto label_0xC4C350;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC4C320UL)));
        }
        if ((x19 == 0x0UL))
        {
            goto label_0xC4C370;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x20 = x0;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x28UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC4C370;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC4C330UL)));
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x14UL))))), 0));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC61FA8UL /* metadata target: TouchGestureBasicState.OnTouchPressureChange */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x30UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC4C370;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC4C344UL)));
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x14UL))))), 0));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC61FA8UL /* metadata target: TouchGestureBasicState.OnTouchPressureChange */, x0, x1, x2, x3);
        goto label_0xC4C350;
        label_0xC4C350:
        ;
        __arm64_flags_left_12895056 = x21;
        __arm64_flags_right_12895056 = 0x0UL;
        x8 = unchecked((ulong)(((!((unchecked((ulong)((__arm64_flags_left_12895056) - (__arm64_flags_right_12895056))) == 0x0UL))) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        __arm64_flags_left_12895064 = x21;
        __arm64_flags_right_12895064 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        RuntimeCalls.Unsupported("cset", 0xC4C360UL);
        x9 = unchecked((ulong)((__Unsupported<bool>("Unknown IR expression") ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        x0 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) & (unchecked((uint)(x8)))))));
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return unchecked((uint)(x0));
        label_0xC4C370:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        return default(uint);
    }
```

## `SuperTouchZone.FingerState.ReleaseTouch` — RVA `0xc4c46c`

- Lift status: **exact**; input span: 116 bytes; span to next metadata RVA: 116 bytes.
- Metadata signature: `public void ReleaseTouch(bool cancel) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=18 (informational only).

```csharp
public static ulong SuperTouchZone_FingerState_ReleaseTouch_RVAc4c46c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x30 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        x21 = x0;
        x19 = x0;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x18UL))));
        x20 = unchecked((ulong)(unchecked((uint)(x1))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC4C4A8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x10UL))));
        x2 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x20))) & (unchecked((uint)(0x1UL)))))));
        x3 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC4D288UL /* metadata target: TouchObject.ReleaseControl */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = x21;
        x1 = 0x0UL;
        RuntimeMemory.WritePtr(unchecked((ulong)((x19) + (0x18UL))), 0x0UL);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC4C4A8;
        label_0xC4C4A8:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x28UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC4C4DC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x20))) & (unchecked((uint)(0x1UL)))))));
        x1 = unchecked((ulong)(unchecked((uint)(x20))));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC62008UL /* metadata target: TouchGestureBasicState.OnTouchEnd */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x30UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC4C4DC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)(x20))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x2 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeDirect(0xC62008UL /* metadata target: TouchGestureBasicState.OnTouchEnd */);
        label_0xC4C4DC:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        return default(ulong);
    }
```

## `SuperTouchZone.FingerState.get_IsActive` — RVA `0xc4cdc4`

- Lift status: **exact**; input span: 16 bytes; span to next metadata RVA: 16 bytes.
- Metadata signature: `public bool get_IsActive() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static uint SuperTouchZone_FingerState_get_IsActive_RVAc4cdc4(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_flags_left_12897736 = default(ulong);
        ulong __arm64_flags_right_12897736 = default(ulong);
        ulong x8 = default(ulong);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x18UL))));
        __arm64_flags_left_12897736 = x8;
        __arm64_flags_right_12897736 = 0x0UL;
        x0 = unchecked((ulong)(((!((unchecked((ulong)((__arm64_flags_left_12897736) - (__arm64_flags_right_12897736))) == 0x0UL))) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        return unchecked((uint)(x0));
        return default(uint);
    }
```

## `SuperTouchZone.FingerState.IsControlledByMouse` — RVA `0xc4cdd4`

- Lift status: **exact**; input span: 32 bytes; span to next metadata RVA: 32 bytes.
- Metadata signature: `public bool IsControlledByMouse() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=3 (informational only).

```csharp
public static uint SuperTouchZone_FingerState_IsControlledByMouse_RVAc4cdd4(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12897760 = default(uint);
        uint __arm64_flags_right_12897760 = default(uint);
        ulong x8 = default(ulong);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x18UL))));
        if ((x8 == 0x0UL))
        {
            label_0xC4CDEC:
            ;
            x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
            return unchecked((uint)(x0));
        }
        else
        {
            x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x11UL))))))));
            __arm64_flags_left_12897760 = unchecked((uint)(x8));
            __arm64_flags_right_12897760 = unchecked((uint)0x0UL);
            x0 = unchecked((ulong)(((!((unchecked((uint)((__arm64_flags_left_12897760) - (__arm64_flags_right_12897760))) == unchecked((uint)0x0UL)))) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
            return unchecked((uint)(x0));
        }
        return default(uint);
    }
```
