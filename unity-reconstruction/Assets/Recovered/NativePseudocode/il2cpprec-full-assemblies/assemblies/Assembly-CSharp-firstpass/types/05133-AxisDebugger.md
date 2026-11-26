# `AxisDebugger` — TypeDefIndex 5133

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x20` | `bool` | `drawGUI` |
| `0x21` | `bool` | `drawMouseStats` |
| `0x22` | `bool` | `drawUnityAxes` |
| `0x24` | `KeyCode` | `deltaResetKey` |
| `0x28` | `Vector2` | `cfScroll` |
| `0x30` | `Vector2` | `unScroll` |
| `0x38` | `Vector2` | `cfMouseDelta` |
| `0x40` | `Vector2` | `unMouseDelta` |
| `0x48` | `GUISkin` | `skin` |

## `AxisDebugger.Update` — RVA `0xc68c04`

- Lift status: **partial**; input span: 540 bytes; span to next metadata RVA: 540 bytes.
- Metadata signature: `private void Update() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=67 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'fadd' at 0xc68cf4

```csharp
public static ulong AxisDebugger_Update_RVAc68c04(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_pair_address_13011972 = default(ulong);
        ulong __arm64_pair_address_13012504 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        RuntimeVector128 v9 = default(RuntimeVector128);
        ulong x10 = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x22 = default(ulong);
        ulong x23 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        __arm64_pair_address_13011972 = unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFC0UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13011972, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13011972) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        sp = __arm64_pair_address_13011972;
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))), x19);
        x20 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x321UL))))))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
        }
        else
        {
            x0 = 0x1A8C000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xE0UL))));
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x0 = 0x1A8C000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD8UL))));
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x0 = 0x1A8C000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x530UL))));
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x0 = 0x1A8C000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x550UL))));
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
            RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x321UL))), unchecked((byte)(unchecked((uint)(x8)))));
        }
        label_0xC68C5C:
        ;
        x0 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x24UL))))));
        x21 = 0x1A8C000UL;
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xE0UL))));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17C7824UL /* metadata target: Input.GetKeyDown */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
        }
        else
        {
            x20 = 0x1BAB000UL;
            x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x1E0UL))))))));
            if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
            {
            }
            else
            {
                x0 = 0x1A8C000UL;
                x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x138UL))));
                // Likely IL2CPP class initialization helper (guarded call).
                x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
                x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
                RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x1E0UL))), unchecked((byte)(unchecked((uint)(x8)))));
            }
            label_0xC68C94:
            ;
            x8 = 0x1A8C000UL;
            x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x138UL))));
            x8 = RuntimeMemory.ReadU64(x8);
            x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
            v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(x9)), 0));
            RuntimeMemory.WriteF64(unchecked((ulong)((x19) + (0x30UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))));
            x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
            v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(x9)), 0));
            RuntimeMemory.WriteF64(unchecked((ulong)((x19) + (0x28UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))));
            x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
            v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(x9)), 0));
            RuntimeMemory.WriteF64(unchecked((ulong)((x19) + (0x38UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))));
            x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
            v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(x8)), 0));
            RuntimeMemory.WriteF64(unchecked((ulong)((x19) + (0x40UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))));
        }
        label_0xC68CD0:
        ;
        x0 = RuntimeMemory.ReadU64(x21);
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((x19) + (0x28UL))))), 0));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
        }
        else
        {
            x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        }
        label_0xC68CE4:
        ;
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC37EDCUL /* metadata target: CF2Input.get_mouseScrollDelta */, x0, x1, x2, x3);
        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x30UL))))), 0));
        v0 = v1;
        RuntimeCalls.Unsupported("fadd", 0xC68CF4UL);
        x0 = 0x0UL;
        RuntimeMemory.WriteF64(unchecked((ulong)((x19) + (0x28UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))));
        x0 = RuntimeCalls.InvokeDirect(0x17C7A14UL /* metadata target: Input.get_mouseScrollDelta */, x0, x1, x2, x3);
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x34UL))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        x0 = 0x0UL;
        RuntimeMemory.WriteF32(unchecked((ulong)((x19) + (0x30UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        x0 = RuntimeCalls.InvokeDirect(0x17C7A14UL /* metadata target: Input.get_mouseScrollDelta */, x0, x1, x2, x3);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((x19) + (0x34UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        x20 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x1DFUL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
        }
        else
        {
            x0 = 0x1A8C000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xE0UL))));
            // Likely IL2CPP class initialization helper (guarded call).
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
            RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x1DFUL))), unchecked((byte)(unchecked((uint)(x8)))));
        }
        label_0xC68D40:
        ;
        x0 = RuntimeMemory.ReadU64(x21);
        x20 = 0x1A8C000UL;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xD8UL))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
        }
        else
        {
            x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
            x0 = RuntimeMemory.ReadU64(x21);
        }
        label_0xC68D5C:
        ;
        x8 = RuntimeMemory.ReadU64(x20);
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB8UL))));
        x10 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0xE0UL))))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0x18UL))));
        if ((unchecked((uint)(x10)) != unchecked((uint)0x0UL)))
        {
        }
        else
        {
            x0 = x8;
            x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        }
        label_0xC68D78:
        ;
        x23 = 0x1A8C000UL;
        x22 = 0x1A8C000UL;
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0x550UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x530UL))));
        x0 = x20;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794AC8UL /* metadata target: Object.op_Inequality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
        }
        else
        {
            x0 = RuntimeMemory.ReadU64(x21);
            v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x38UL))))), 0));
            x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
            if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
            {
            }
            else
            {
                x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
            }
            label_0xC68DB0:
            ;
            x0 = RuntimeMemory.ReadU64(x23);
            x1 = 0x0UL;
            x0 = RuntimeCalls.InvokeDirect(0xC35E20UL /* metadata target: CF2Input.GetAxis */, x0, x1, x2, x3);
            v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
            RuntimeMemory.WriteF32(unchecked((ulong)((x19) + (0x38UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
            x0 = RuntimeMemory.ReadU64(x22);
            v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x3CUL))))), 0));
            x1 = 0x0UL;
            x0 = RuntimeCalls.InvokeDirect(0xC35E20UL /* metadata target: CF2Input.GetAxis */, x0, x1, x2, x3);
            v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
            RuntimeMemory.WriteF32(unchecked((ulong)((x19) + (0x3CUL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        }
        label_0xC68DDC:
        ;
        x1 = RuntimeMemory.ReadU64(x23);
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x40UL))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        x0 = RuntimeCalls.InvokeDirect(0xC68E20UL /* metadata target: AxisDebugger.GetUnityAxis */, x0, x1, x2, x3);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((x19) + (0x40UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        x1 = RuntimeMemory.ReadU64(x22);
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x44UL))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        x0 = RuntimeCalls.InvokeDirect(0xC68E20UL /* metadata target: AxisDebugger.GetUnityAxis */, x0, x1, x2, x3);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((x19) + (0x44UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        __arm64_pair_address_13012504 = sp;
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13012504)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13012504) + (0x8UL))))), 0));
        sp = unchecked((ulong)((__arm64_pair_address_13012504) + (0x40UL)));
        return x0;
        return default(ulong);
    }
```

## `AxisDebugger.GetUnityAxis` — RVA `0xc68e20`

- Lift status: **exact**; input span: 156 bytes; span to next metadata RVA: 156 bytes.
- Metadata signature: `private float GetUnityAxis(string name, float defaultVal = 0.0) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=34 (informational only).

```csharp
public static ulong AxisDebugger_GetUnityAxis_RVAc68e20(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_load_address_13012548 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v8 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        RuntimeMemory.WriteF64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        sp = unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL)));
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        x0 = x1;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17C7130UL /* metadata target: Input.GetAxis */, x0, x1, x2, x3);
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        __arm64_load_address_13012548 = sp;
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_load_address_13012548)), 0));
        return x0;
        return default(ulong);
    }
```

## `AxisDebugger.OnGUI` — RVA `0xc68ebc`

- Lift status: **partial**; input span: 2796 bytes; span to next metadata RVA: 2796 bytes.
- Metadata signature: `private void OnGUI() { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=413 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'cset' at 0xc69610; reason: Unknown IR expression at 0xc69610; reason: Unsupported instruction 'cset' at 0xc69628; reason: Unknown IR expression at 0xc69628; reason: Unsupported instruction 'cset' at 0xc69760; reason: Unknown IR expression at 0xc69760; reason: Unsupported instruction 'cset' at 0xc69778; reason: Unknown IR expression at 0xc69778

```csharp
public static ulong AxisDebugger_OnGUI_RVAc68ebc(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13013672 = default(uint);
        uint __arm64_flags_left_13013704 = default(uint);
        uint __arm64_flags_left_13013772 = default(uint);
        uint __arm64_flags_left_13013804 = default(uint);
        uint __arm64_flags_left_13013872 = default(uint);
        uint __arm64_flags_left_13013904 = default(uint);
        uint __arm64_flags_left_13013964 = default(uint);
        uint __arm64_flags_left_13014192 = default(uint);
        uint __arm64_flags_left_13014576 = default(uint);
        uint __arm64_flags_left_13014912 = default(uint);
        uint __arm64_flags_left_13015272 = default(uint);
        uint __arm64_flags_right_13013672 = default(uint);
        uint __arm64_flags_right_13013704 = default(uint);
        uint __arm64_flags_right_13013772 = default(uint);
        uint __arm64_flags_right_13013804 = default(uint);
        uint __arm64_flags_right_13013872 = default(uint);
        uint __arm64_flags_right_13013904 = default(uint);
        uint __arm64_flags_right_13013964 = default(uint);
        uint __arm64_flags_right_13014192 = default(uint);
        uint __arm64_flags_right_13014576 = default(uint);
        uint __arm64_flags_right_13014912 = default(uint);
        uint __arm64_flags_right_13015272 = default(uint);
        float __arm64_float_flags_left_13014312 = default(float);
        float __arm64_float_flags_left_13014332 = default(float);
        float __arm64_float_flags_left_13014536 = default(float);
        float __arm64_float_flags_left_13014548 = default(float);
        float __arm64_float_flags_left_13014556 = default(float);
        float __arm64_float_flags_left_13014872 = default(float);
        float __arm64_float_flags_left_13014884 = default(float);
        float __arm64_float_flags_left_13014892 = default(float);
        float __arm64_float_flags_right_13014312 = default(float);
        float __arm64_float_flags_right_13014332 = default(float);
        float __arm64_float_flags_right_13014536 = default(float);
        float __arm64_float_flags_right_13014548 = default(float);
        float __arm64_float_flags_right_13014556 = default(float);
        float __arm64_float_flags_right_13014872 = default(float);
        float __arm64_float_flags_right_13014884 = default(float);
        float __arm64_float_flags_right_13014892 = default(float);
        ulong __arm64_pair_address_13012672 = default(ulong);
        ulong __arm64_pair_address_13012676 = default(ulong);
        ulong __arm64_pair_address_13012680 = default(ulong);
        ulong __arm64_pair_address_13015380 = default(ulong);
        ulong __arm64_pair_address_13015384 = default(ulong);
        ulong __arm64_pair_address_13015388 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v10 = default(RuntimeVector128);
        RuntimeVector128 v11 = default(RuntimeVector128);
        RuntimeVector128 v12 = default(RuntimeVector128);
        RuntimeVector128 v13 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        RuntimeVector128 v9 = default(RuntimeVector128);
        ulong x10 = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x22 = default(ulong);
        ulong x23 = default(ulong);
        ulong x24 = default(ulong);
        ulong x25 = default(ulong);
        ulong x26 = default(ulong);
        ulong x27 = default(ulong);
        ulong x28 = default(ulong);
        ulong x29 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        sp = unchecked((ulong)((sp) - (0xA0UL)));
        __arm64_pair_address_13012672 = unchecked((ulong)((sp) + (0x10UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13012672, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v13.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13012672) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v12.GetUInt64(0)))));
        __arm64_pair_address_13012676 = unchecked((ulong)((sp) + (0x20UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13012676, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v11.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13012676) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v10.GetUInt64(0)))));
        __arm64_pair_address_13012680 = unchecked((ulong)((sp) + (0x30UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13012680, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13012680) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x0UL))), x29);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x0UL))), x28);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x8UL))), x27);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x0UL))), x26);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x8UL))), x25);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x70UL)))) + (0x0UL))), x24);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x70UL)))) + (0x8UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x80UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x80UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x90UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x90UL)))) + (0x8UL))), x19);
        x20 = 0x1BAB000UL;
        x22 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x322UL))))))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0xE0UL))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC68FDC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x298UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xE0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x2A0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x2A8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xCE0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x8E8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x8F0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x3A0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x2B0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x2B8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x2C0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x2C8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x2D0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x230UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x2D8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x2E0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x2E8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x322UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC68FDC;
        label_0xC68FDC:
        ;
        x0 = RuntimeMemory.ReadU64(x22);
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0x0UL))), 0x0UL);
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0x8UL))), 0x0UL);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC68FF0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC68FECUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC68FF0;
        label_0xC68FF0:
        ;
        x23 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x23) + (0x1DFUL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC69010;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xE0UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x23) + (0x1DFUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC69010;
        label_0xC69010:
        ;
        x0 = RuntimeMemory.ReadU64(x22);
        x21 = 0x1A8C000UL;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xD8UL))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC6902C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC69024UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x22);
        goto label_0xC6902C;
        label_0xC6902C:
        ;
        x8 = RuntimeMemory.ReadU64(x21);
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB8UL))));
        x10 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0xE0UL))))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0x18UL))));
        if ((unchecked((uint)(x10)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC69048;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC69048;
        label_0xC69048:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179568CUL /* metadata target: Object.op_Equality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC6993C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xCE0UL))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x48UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC69078;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC69074UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC69078;
        label_0xC69078:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17B3680UL /* metadata target: GUI.set_skin */, x0, x1, x2, x3);
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17B388CUL /* metadata target: GUI.get_skin */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x21);
        x20 = x0;
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC690A4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC690A4;
        label_0xC690A4:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794AC8UL /* metadata target: Object.op_Inequality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC690E8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xCE0UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC690D0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC690CCUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC690D0;
        label_0xC690D0:
        ;
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17B388CUL /* metadata target: GUI.get_skin */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC69968;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17B5104UL /* metadata target: GUISkin.get_box */, x0, x1, x2, x3);
        goto label_0xC69108;
        label_0xC690E8:
        ;
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x2A8UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC69100;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC690FCUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC69100;
        label_0xC69100:
        ;
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17B681CUL /* metadata target: GUIStyle.get_none */, x0, x1, x2, x3);
        goto label_0xC69108;
        label_0xC69108:
        ;
        x26 = 0x1A8D000UL;
        x26 = RuntimeMemory.ReadU64(unchecked((ulong)((x26) + (0x298UL))));
        x20 = x0;
        x21 = RuntimeMemory.ReadU64(x26);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x38UL))));
        if ((x8 != 0x0UL))
        {
            goto label_0xC6912C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xB80068UL, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x38UL))));
        goto label_0xC6912C;
        label_0xC6912C:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x10UL))));
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x135UL))))))));
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC6913C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC69138UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB8000CUL, x0, x1, x2, x3);
        goto label_0xC6913C;
        label_0xC6913C:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC69148;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC69144UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC69148;
        label_0xC69148:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x38UL))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x10UL))));
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x135UL))))))));
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC6915C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC69158UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB8000CUL, x0, x1, x2, x3);
        goto label_0xC6915C;
        label_0xC6915C:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB8UL))));
        x0 = x20;
        x2 = 0x0UL;
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x17B78C4UL /* metadata target: GUILayout.BeginVertical */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x22);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC69180;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC6917CUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC69180;
        label_0xC69180:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x23) + (0x1DFUL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC6919C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xE0UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x23) + (0x1DFUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC6919C;
        label_0xC6919C:
        ;
        x0 = RuntimeMemory.ReadU64(x22);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC691B0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC691A8UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x22);
        goto label_0xC691B0;
        label_0xC691B0:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB8UL))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x18UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC69968;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1798300UL /* metadata target: Object.get_name */, x0, x1, x2, x3);
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x2B0UL))));
        x1 = x0;
        x2 = 0x0UL;
        x8 = RuntimeMemory.ReadU64(x8);
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0x13ED2C8UL /* metadata target: String.Concat */, x0, x1, x2, x3);
        x21 = RuntimeMemory.ReadU64(x26);
        x20 = x0;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x38UL))));
        if ((x8 != 0x0UL))
        {
            goto label_0xC691FC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xB80068UL, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x38UL))));
        goto label_0xC691FC;
        label_0xC691FC:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x10UL))));
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x135UL))))))));
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC6920C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC69208UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB8000CUL, x0, x1, x2, x3);
        goto label_0xC6920C;
        label_0xC6920C:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC69218;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC69214UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC69218;
        label_0xC69218:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x38UL))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x10UL))));
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x135UL))))))));
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC6922C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC69228UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB8000CUL, x0, x1, x2, x3);
        goto label_0xC6922C;
        label_0xC6922C:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB8UL))));
        x0 = x20;
        x2 = 0x0UL;
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x17B7508UL /* metadata target: GUILayout.Box */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x21UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC69450;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x3A0UL))));
        x1 = unchecked((ulong)(unchecked((uint)(0x8UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xB7D9D4UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC69968;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x18UL))))));
        x20 = x0;
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC6996C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x2D0UL))));
        x21 = x20;
        x1 = RuntimeMemory.ReadU64(x8);
        RuntimeMemory.WriteU64(unchecked((ulong)((x21) + (0x20UL))), x1);
        x0 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x28UL))));
        x0 = unchecked((ulong)((sp) + (0x8UL)));
        x1 = 0x0UL;
        x2 = 0x0UL;
        x3 = 0x0UL;
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x8UL))), x8);
        x0 = RuntimeCalls.InvokeDirect(0xC6A514UL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x21) + (0xFFFFFFFFFFFFFFF8UL))))));
        __arm64_flags_left_13013672 = unchecked((uint)(x8));
        __arm64_flags_right_13013672 = unchecked((uint)0x1UL);
        if (((!((__arm64_flags_left_13013672 >= __arm64_flags_right_13013672))) || (unchecked((uint)((__arm64_flags_left_13013672) - (__arm64_flags_right_13013672))) == unchecked((uint)0x0UL))))
        {
            goto label_0xC6996C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x21 = x20;
        RuntimeMemory.WriteU64(unchecked((ulong)((x21) + (0x28UL))), x0);
        x1 = x0;
        x0 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x21) + (0xFFFFFFFFFFFFFFF0UL))))));
        __arm64_flags_left_13013704 = unchecked((uint)(x8));
        __arm64_flags_right_13013704 = unchecked((uint)0x2UL);
        if (((!((__arm64_flags_left_13013704 >= __arm64_flags_right_13013704))) || (unchecked((uint)((__arm64_flags_left_13013704) - (__arm64_flags_right_13013704))) == unchecked((uint)0x0UL))))
        {
            goto label_0xC6996C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x24 = 0x1A8D000UL;
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((x24) + (0x2E8UL))));
        x21 = x20;
        x1 = RuntimeMemory.ReadU64(x24);
        RuntimeMemory.WriteU64(unchecked((ulong)((x21) + (0x30UL))), x1);
        x0 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x30UL))));
        x0 = unchecked((ulong)((sp) + (0x8UL)));
        x1 = 0x0UL;
        x2 = 0x0UL;
        x3 = 0x0UL;
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x8UL))), x8);
        x0 = RuntimeCalls.InvokeDirect(0xC6A514UL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x21) + (0xFFFFFFFFFFFFFFE8UL))))));
        __arm64_flags_left_13013772 = unchecked((uint)(x8));
        __arm64_flags_right_13013772 = unchecked((uint)0x3UL);
        if (((!((__arm64_flags_left_13013772 >= __arm64_flags_right_13013772))) || (unchecked((uint)((__arm64_flags_left_13013772) - (__arm64_flags_right_13013772))) == unchecked((uint)0x0UL))))
        {
            goto label_0xC6996C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x21 = x20;
        RuntimeMemory.WriteU64(unchecked((ulong)((x21) + (0x38UL))), x0);
        x1 = x0;
        x0 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x21) + (0xFFFFFFFFFFFFFFE0UL))))));
        __arm64_flags_left_13013804 = unchecked((uint)(x8));
        __arm64_flags_right_13013804 = unchecked((uint)0x4UL);
        if (((!((__arm64_flags_left_13013804 >= __arm64_flags_right_13013804))) || (unchecked((uint)((__arm64_flags_left_13013804) - (__arm64_flags_right_13013804))) == unchecked((uint)0x0UL))))
        {
            goto label_0xC6996C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x2C8UL))));
        x21 = x20;
        x1 = RuntimeMemory.ReadU64(x8);
        RuntimeMemory.WriteU64(unchecked((ulong)((x21) + (0x40UL))), x1);
        x0 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x38UL))));
        x0 = unchecked((ulong)((sp) + (0x8UL)));
        x1 = 0x0UL;
        x2 = 0x0UL;
        x3 = 0x0UL;
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x8UL))), x8);
        x0 = RuntimeCalls.InvokeDirect(0xC6A514UL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x21) + (0xFFFFFFFFFFFFFFD8UL))))));
        __arm64_flags_left_13013872 = unchecked((uint)(x8));
        __arm64_flags_right_13013872 = unchecked((uint)0x5UL);
        if (((!((__arm64_flags_left_13013872 >= __arm64_flags_right_13013872))) || (unchecked((uint)((__arm64_flags_left_13013872) - (__arm64_flags_right_13013872))) == unchecked((uint)0x0UL))))
        {
            goto label_0xC6996C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x21 = x20;
        RuntimeMemory.WriteU64(unchecked((ulong)((x21) + (0x48UL))), x0);
        x1 = x0;
        x0 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x21) + (0xFFFFFFFFFFFFFFD0UL))))));
        __arm64_flags_left_13013904 = unchecked((uint)(x8));
        __arm64_flags_right_13013904 = unchecked((uint)0x6UL);
        if (((!((__arm64_flags_left_13013904 >= __arm64_flags_right_13013904))) || (unchecked((uint)((__arm64_flags_left_13013904) - (__arm64_flags_right_13013904))) == unchecked((uint)0x0UL))))
        {
            goto label_0xC6996C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(x24);
        x21 = x20;
        RuntimeMemory.WriteU64(unchecked((ulong)((x21) + (0x50UL))), x1);
        x0 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x40UL))));
        x0 = unchecked((ulong)((sp) + (0x8UL)));
        x1 = 0x0UL;
        x2 = 0x0UL;
        x3 = 0x0UL;
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x8UL))), x8);
        x0 = RuntimeCalls.InvokeDirect(0xC6A514UL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x21) + (0xFFFFFFFFFFFFFFC8UL))))));
        __arm64_flags_left_13013964 = unchecked((uint)(x8));
        __arm64_flags_right_13013964 = unchecked((uint)0x7UL);
        if (((!((__arm64_flags_left_13013964 >= __arm64_flags_right_13013964))) || (unchecked((uint)((__arm64_flags_left_13013964) - (__arm64_flags_right_13013964))) == unchecked((uint)0x0UL))))
        {
            goto label_0xC6996C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = x0;
        x0 = x20;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x58UL))), x1);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x13F6A44UL /* metadata target: String.Concat */, x0, x1, x2, x3);
        x21 = RuntimeMemory.ReadU64(x26);
        x20 = x0;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x38UL))));
        if ((x8 != 0x0UL))
        {
            goto label_0xC6940C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xB80068UL, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x38UL))));
        goto label_0xC6940C;
        label_0xC6940C:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x10UL))));
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x135UL))))))));
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC6941C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC69418UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB8000CUL, x0, x1, x2, x3);
        goto label_0xC6941C;
        label_0xC6941C:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC69428;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC69424UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC69428;
        label_0xC69428:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x38UL))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x10UL))));
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x135UL))))))));
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC6943C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC69438UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB8000CUL, x0, x1, x2, x3);
        goto label_0xC6943C;
        label_0xC6943C:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB8UL))));
        x0 = x20;
        x2 = 0x0UL;
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x17B7508UL /* metadata target: GUILayout.Box */, x0, x1, x2, x3);
        goto label_0xC69450;
        label_0xC69450:
        ;
        x0 = RuntimeMemory.ReadU64(x22);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC69460;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC6945CUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC69460;
        label_0xC69460:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x23) + (0x1DFUL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC6947C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xE0UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x23) + (0x1DFUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC6947C;
        label_0xC6947C:
        ;
        x0 = RuntimeMemory.ReadU64(x22);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC69490;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC69488UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x22);
        goto label_0xC69490;
        label_0xC69490:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB8UL))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x18UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC69968;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x80UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC69968;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x10UL))));
        if ((x20 == 0x0UL))
        {
            goto label_0xC69968;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x20) + (0x18UL))))));
        __arm64_flags_left_13014192 = unchecked((uint)(x8));
        __arm64_flags_right_13014192 = unchecked((uint)0x1UL);
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13014192) - (__arm64_flags_right_13014192))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_13014192)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13014192)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13014192) - (__arm64_flags_right_13014192))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13014192)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC69934;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x27 = 0x1A8C000UL;
        x22 = 0x1A8D000UL;
        x28 = 0x1A8C000UL;
        x27 = RuntimeMemory.ReadU64(unchecked((ulong)((x27) + (0x8F0UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x2A0UL))));
        x28 = RuntimeMemory.ReadU64(unchecked((ulong)((x28) + (0x230UL))));
        x21 = unchecked((ulong)(unchecked((uint)0x0UL)));
        v10 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        v11 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0xBF800000UL)), 0)), 0));
        v12 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F000000UL)), 0)), 0));
        v13 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        x29 = unchecked((ulong)(unchecked((uint)(0x42C80000UL))));
        goto label_0xC694E8;
        label_0xC694E8:
        ;
        x2 = RuntimeMemory.ReadU64(x27);
        x0 = x20;
        x1 = unchecked((ulong)(unchecked((uint)(x21))));
        x0 = RuntimeCalls.InvokeDirect(0x10A30C0UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        RuntimeMemory.WritePtr(sp, 0x0UL);
        if ((x0 == 0x0UL))
        {
            goto label_0xC69968;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x23 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC41C48UL /* metadata target: InputRig.AxisConfig.GetAnalog */, x0, x1, x2, x3);
        RuntimeMemory.WriteF32(unchecked((ulong)((sp) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0x10UL))));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17C7130UL /* metadata target: Input.GetAxis */, x0, x1, x2, x3);
        RuntimeMemory.WriteF32(sp, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        x25 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((sp) + (0x4UL))))), 0));
        __arm64_float_flags_left_13014312 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13014312 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        if (((__arm64_float_flags_left_13014312 != __arm64_float_flags_right_13014312) || ((__arm64_float_flags_left_13014312 != __arm64_float_flags_left_13014312) || (__arm64_float_flags_right_13014312 != __arm64_float_flags_right_13014312))))
        {
            goto label_0xC69544;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x22UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC698E0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC69538UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(sp)), 0));
        __arm64_float_flags_left_13014332 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13014332 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        if ((__arm64_float_flags_left_13014332 == __arm64_float_flags_right_13014332))
        {
            goto label_0xC698E0;
        }
        else
        {
            goto label_0xC69544;
        }
        label_0xC69544:
        ;
        x24 = RuntimeMemory.ReadU64(x26);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x24) + (0x38UL))));
        if ((x8 != 0x0UL))
        {
            goto label_0xC6955C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x24;
        x0 = RuntimeCalls.InvokeDirect(0xB80068UL, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x24) + (0x38UL))));
        goto label_0xC6955C;
        label_0xC6955C:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x10UL))));
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x135UL))))))));
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC6956C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC69568UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB8000CUL, x0, x1, x2, x3);
        goto label_0xC6956C;
        label_0xC6956C:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC69578;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC69574UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC69578;
        label_0xC69578:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x24) + (0x38UL))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x10UL))));
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x135UL))))))));
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC6958C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC69588UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB8000CUL, x0, x1, x2, x3);
        goto label_0xC6958C;
        label_0xC6958C:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB8UL))));
        x1 = 0x0UL;
        x0 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x17B767CUL /* metadata target: GUILayout.BeginVertical */, x0, x1, x2, x3);
        x24 = RuntimeMemory.ReadU64(x26);
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0x10UL))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x24) + (0x38UL))));
        if ((x8 != 0x0UL))
        {
            goto label_0xC695B8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x24;
        x0 = RuntimeCalls.InvokeDirect(0xB80068UL, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x24) + (0x38UL))));
        goto label_0xC695B8;
        label_0xC695B8:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x10UL))));
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x135UL))))))));
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC695C8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC695C4UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB8000CUL, x0, x1, x2, x3);
        goto label_0xC695C8;
        label_0xC695C8:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC695D4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC695D0UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC695D4;
        label_0xC695D4:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x24) + (0x38UL))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x10UL))));
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x135UL))))))));
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC695E8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC695E4UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB8000CUL, x0, x1, x2, x3);
        goto label_0xC695E8;
        label_0xC695E8:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB8UL))));
        x0 = x23;
        x2 = 0x0UL;
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x17B7328UL /* metadata target: GUILayout.Label */, x0, x1, x2, x3);
        x8 = 0x1A8C000UL;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((sp) + (0x4UL))))), 0));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xCE0UL))));
        __arm64_float_flags_left_13014536 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13014536 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        x0 = RuntimeMemory.ReadU64(x8);
        RuntimeCalls.Unsupported("cset", 0xC69610UL);
        x9 = unchecked((ulong)((__Unsupported<bool>("Unknown IR expression") ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        __arm64_float_flags_left_13014548 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13014548 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0);
        x10 = unchecked((ulong)(((__arm64_float_flags_left_13014548 == __arm64_float_flags_right_13014548) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        __arm64_float_flags_left_13014556 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13014556 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) | (unchecked((uint)(x10)))))));
        RuntimeCalls.Unsupported("cset", 0xC69628UL);
        x10 = unchecked((ulong)((__Unsupported<bool>("Unknown IR expression") ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x10))) | (unchecked((uint)(x9)))))));
        __arm64_flags_left_13014576 = unchecked((uint)(x9));
        __arm64_flags_right_13014576 = unchecked((uint)0x0UL);
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((!((unchecked((uint)((__arm64_flags_left_13014576) - (__arm64_flags_right_13014576))) == unchecked((uint)0x0UL)))) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v13.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v12.GetUInt64(0)))), 0))), 0));
        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((!((unchecked((uint)((__arm64_flags_left_13014576) - (__arm64_flags_right_13014576))) == unchecked((uint)0x0UL)))) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v12.GetUInt64(0)))), 0))), 0));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC69644;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC69640UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC69644;
        label_0xC69644:
        ;
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        v0 = v8;
        v1 = v9;
        v2 = v8;
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17B2DBCUL /* metadata target: GUI.set_color */, x0, x1, x2, x3);
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x2D8UL))));
        x0 = unchecked((ulong)((sp) + (0x4UL)));
        x2 = 0x0UL;
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x1559570UL /* metadata target: Single.ToString */, x0, x1, x2, x3);
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x2E0UL))));
        x1 = x0;
        x2 = 0x0UL;
        x8 = RuntimeMemory.ReadU64(x8);
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0x13ED2C8UL /* metadata target: String.Concat */, x0, x1, x2, x3);
        x24 = RuntimeMemory.ReadU64(x26);
        x23 = x0;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x24) + (0x38UL))));
        if ((x8 != 0x0UL))
        {
            goto label_0xC696AC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x24;
        x0 = RuntimeCalls.InvokeDirect(0xB80068UL, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x24) + (0x38UL))));
        goto label_0xC696AC;
        label_0xC696AC:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x10UL))));
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x135UL))))))));
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC696BC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC696B8UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB8000CUL, x0, x1, x2, x3);
        goto label_0xC696BC;
        label_0xC696BC:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC696C8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC696C4UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC696C8;
        label_0xC696C8:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x24) + (0x38UL))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x10UL))));
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x135UL))))))));
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC696DC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC696D8UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB8000CUL, x0, x1, x2, x3);
        goto label_0xC696DC;
        label_0xC696DC:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB8UL))));
        x0 = x23;
        x2 = 0x0UL;
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x17B7328UL /* metadata target: GUILayout.Label */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x22);
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D9D4UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((sp) + (0x4UL))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(x29))), 0)), 0));
        x23 = x0;
        x0 = 0x0UL;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)((global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)), 0)) & (unchecked((uint)0x7FFFFFFFUL))))), 0)), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        x0 = RuntimeCalls.InvokeDirect(0x17B63FCUL /* metadata target: GUILayout.Width */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        if ((x23 == 0x0UL))
        {
            goto label_0xC69968;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x23) + (0x18UL))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC6996C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = x0;
        x0 = x23;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x20UL))), x1);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x28);
        x1 = x23;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17B7508UL /* metadata target: GUILayout.Box */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x22UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC698A8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8C000UL;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(sp)), 0));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xCE0UL))));
        __arm64_float_flags_left_13014872 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13014872 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        x0 = RuntimeMemory.ReadU64(x8);
        RuntimeCalls.Unsupported("cset", 0xC69760UL);
        x9 = unchecked((ulong)((__Unsupported<bool>("Unknown IR expression") ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        __arm64_float_flags_left_13014884 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13014884 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0);
        x10 = unchecked((ulong)(((__arm64_float_flags_left_13014884 == __arm64_float_flags_right_13014884) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        __arm64_float_flags_left_13014892 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13014892 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) | (unchecked((uint)(x10)))))));
        RuntimeCalls.Unsupported("cset", 0xC69778UL);
        x10 = unchecked((ulong)((__Unsupported<bool>("Unknown IR expression") ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x10))) | (unchecked((uint)(x9)))))));
        __arm64_flags_left_13014912 = unchecked((uint)(x9));
        __arm64_flags_right_13014912 = unchecked((uint)0x0UL);
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((!((unchecked((uint)((__arm64_flags_left_13014912) - (__arm64_flags_right_13014912))) == unchecked((uint)0x0UL)))) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v13.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v12.GetUInt64(0)))), 0))), 0));
        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((!((unchecked((uint)((__arm64_flags_left_13014912) - (__arm64_flags_right_13014912))) == unchecked((uint)0x0UL)))) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v12.GetUInt64(0)))), 0))), 0));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC69794;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC69790UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC69794;
        label_0xC69794:
        ;
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        v0 = v8;
        v1 = v9;
        v2 = v8;
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17B2DBCUL /* metadata target: GUI.set_color */, x0, x1, x2, x3);
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x2B8UL))));
        x23 = RuntimeMemory.ReadU64(x8);
        if ((unchecked((uint)((unchecked((uint)(x25))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC697DC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x2D8UL))));
        x0 = sp;
        x2 = 0x0UL;
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x1559570UL /* metadata target: Single.ToString */, x0, x1, x2, x3);
        x1 = x0;
        goto label_0xC697E8;
        label_0xC697DC:
        ;
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x2C0UL))));
        x1 = RuntimeMemory.ReadU64(x8);
        goto label_0xC697E8;
        label_0xC697E8:
        ;
        x0 = x23;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x13ED2C8UL /* metadata target: String.Concat */, x0, x1, x2, x3);
        x24 = RuntimeMemory.ReadU64(x26);
        x23 = x0;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x24) + (0x38UL))));
        if ((x8 != 0x0UL))
        {
            goto label_0xC69810;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x24;
        x0 = RuntimeCalls.InvokeDirect(0xB80068UL, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x24) + (0x38UL))));
        goto label_0xC69810;
        label_0xC69810:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x10UL))));
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x135UL))))))));
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC69820;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC6981CUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB8000CUL, x0, x1, x2, x3);
        goto label_0xC69820;
        label_0xC69820:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC6982C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC69828UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC6982C;
        label_0xC6982C:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x24) + (0x38UL))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x10UL))));
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x135UL))))))));
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC69840;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC6983CUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB8000CUL, x0, x1, x2, x3);
        goto label_0xC69840;
        label_0xC69840:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB8UL))));
        x0 = x23;
        x2 = 0x0UL;
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x17B7328UL /* metadata target: GUILayout.Label */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x22);
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D9D4UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(sp)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(x29))), 0)), 0));
        x23 = x0;
        x0 = 0x0UL;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)((global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)), 0)) & (unchecked((uint)0x7FFFFFFFUL))))), 0)), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        x0 = RuntimeCalls.InvokeDirect(0x17B63FCUL /* metadata target: GUILayout.Width */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        if ((x23 == 0x0UL))
        {
            goto label_0xC69968;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x23) + (0x18UL))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC6996C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = x0;
        x0 = x23;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x20UL))), x1);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x28);
        x1 = x23;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17B7508UL /* metadata target: GUILayout.Box */, x0, x1, x2, x3);
        goto label_0xC698A8;
        label_0xC698A8:
        ;
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17B7C80UL /* metadata target: GUILayout.EndVertical */, x0, x1, x2, x3);
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xCE0UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC698C8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC698C4UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC698C8;
        label_0xC698C8:
        ;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17B2DBCUL /* metadata target: GUI.set_color */, x0, x1, x2, x3);
        goto label_0xC698E0;
        label_0xC698E0:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x20) + (0x18UL))))));
        x21 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x21))) + (unchecked((uint)(0x1UL)))))));
        __arm64_flags_left_13015272 = unchecked((uint)(x21));
        __arm64_flags_right_13015272 = unchecked((uint)(x8));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13015272) - (__arm64_flags_right_13015272))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_13015272)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13015272)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13015272) - (__arm64_flags_right_13015272))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13015272)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC694E8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC698F0UL);
        }
        goto label_0xC69934;
        label_0xC69934:
        ;
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17B7C80UL /* metadata target: GUILayout.EndVertical */, x0, x1, x2, x3);
        goto label_0xC6993C;
        label_0xC6993C:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x90UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x90UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x80UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x80UL)))) + (0x8UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x70UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x70UL)))) + (0x8UL))));
        x26 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x60UL))));
        x25 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x8UL))));
        x28 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x50UL))));
        x27 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x8UL))));
        x29 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x40UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))));
        __arm64_pair_address_13015380 = unchecked((ulong)((sp) + (0x30UL)));
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13015380)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13015380) + (0x8UL))))), 0));
        __arm64_pair_address_13015384 = unchecked((ulong)((sp) + (0x20UL)));
        v11 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13015384)), 0));
        v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13015384) + (0x8UL))))), 0));
        __arm64_pair_address_13015388 = unchecked((ulong)((sp) + (0x10UL)));
        v13 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13015388)), 0));
        v12 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13015388) + (0x8UL))))), 0));
        sp = unchecked((ulong)((sp) + (0xA0UL)));
        return x0;
        label_0xC69968:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        goto label_0xC6996C;
        label_0xC6996C:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB7CUL, x0, x1, x2, x3);
        x0 = unchecked((ulong)(unchecked((uint)(0x8UL))));
        x0 = RuntimeCalls.InvokeDirect(0x19B0C20UL, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x24);
        RuntimeMemory.WriteU64(unchecked((ulong)(unchecked((uint)(x0)))), x8);
        x1 = 0x19B6000UL;
        x1 = unchecked((ulong)((x1) + (0xF08UL)));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x19B0C30UL, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        goto label_0xC69994;
        label_0xC69994:
        ;
        x24 = unchecked((ulong)(unchecked((uint)(x0))));
        x0 = RuntimeCalls.InvokeDirect(0x19B0C10UL, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        x0 = x24;
        x0 = RuntimeCalls.InvokeDirect(0xC26098UL, x0, x1, x2, x3);
        x0 = RuntimeCalls.InvokeDirect(0xA29990UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `AxisDebugger.ctor` — RVA `0xc699a8`

- Lift status: **exact**; input span: 24 bytes; span to next metadata RVA: 24 bytes.
- Metadata signature: `public void .ctor() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=3 (informational only).

```csharp
public static ulong AxisDebugger_ctor_RVAc699a8(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x9 = unchecked((ulong)(unchecked((uint)(0x11EUL))));
        x1 = 0x0UL;
        RuntimeMemory.WriteU8(unchecked((ulong)((x0) + (0x20UL))), unchecked((byte)(unchecked((uint)(x8)))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x0) + (0x24UL))), unchecked((uint)(x9)));
        return RuntimeCalls.InvokeDirect(0x1796274UL /* metadata target: MonoBehaviour.ctor */);
        return default(ulong);
    }
```
