# `AxisEvent` — TypeDefIndex 5126

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x20` | `string` | `axisName` |
| `0x28` | `float` | `axisDeadzone` |
| `0x2C` | `int` | `axisId` |
| `0x30` | `int` | `prevAxisDir` |
| `0x34` | `AxisEvent.EventType` | `eventType` |
| `0x38` | `UnityEvent` | `positiveEvent` |
| `0x40` | `UnityEvent` | `negativeEvent` |

## `AxisEvent.ctor` — RVA `0xc681f0`

- Lift status: **exact**; input span: 196 bytes; span to next metadata RVA: 196 bytes.
- Metadata signature: `public void .ctor() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=30 (informational only).

```csharp
public static ulong AxisEvent_ctor_RVAc681f0(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
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
        x20 = 0x1BAB000UL;
        x22 = 0x1A8C000UL;
        x21 = 0x1A8D000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x316UL))))))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x548UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x258UL))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC6823C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x258UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x548UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x316UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC6823C;
        label_0xC6823C:
        ;
        x1 = RuntimeMemory.ReadU64(x22);
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x20UL))), x1);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x3F000000UL))));
        x0 = x19;
        x1 = 0x0UL;
        RuntimeMemory.WriteU32(unchecked((ulong)((x19) + (0x28UL))), unchecked((uint)(x8)));
        x0 = RuntimeCalls.InvokeDirect(0x1796274UL /* metadata target: MonoBehaviour.ctor */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x21);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x17A2850UL /* metadata target: UnityEvent.ctor */, x0, x1, x2, x3);
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x38UL))), x20);
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x21);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x17A2850UL /* metadata target: UnityEvent.ctor */, x0, x1, x2, x3);
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x40UL))), x20);
        x0 = x19;
        x1 = x20;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0xB7D8D0UL);
        return default(ulong);
    }
```

## `AxisEvent.OnEnable` — RVA `0xc682b4`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `private void OnEnable() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=0 (informational only).

```csharp
public static ulong AxisEvent_OnEnable_RVAc682b4(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        RuntimeMemory.WritePtr(unchecked((ulong)((x0) + (0x30UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        return x0;
        return default(ulong);
    }
```

## `AxisEvent.Update` — RVA `0xc682bc`

- Lift status: **partial**; input span: 292 bytes; span to next metadata RVA: 292 bytes.
- Metadata signature: `private void Update() { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=34 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'csel' at 0xc68394; reason: Unknown IR expression at 0xc68394; reason: Unsupported instruction 'csel' at 0xc683b8; reason: Unknown IR expression at 0xc683b8

```csharp
public static ulong AxisEvent_Update_RVAc682bc(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13009756 = default(uint);
        uint __arm64_flags_left_13009764 = default(uint);
        uint __arm64_flags_left_13009784 = default(uint);
        uint __arm64_flags_left_13009800 = default(uint);
        uint __arm64_flags_left_13009828 = default(uint);
        uint __arm64_flags_left_13009836 = default(uint);
        uint __arm64_flags_right_13009756 = default(uint);
        uint __arm64_flags_right_13009764 = default(uint);
        uint __arm64_flags_right_13009784 = default(uint);
        uint __arm64_flags_right_13009800 = default(uint);
        uint __arm64_flags_right_13009828 = default(uint);
        uint __arm64_flags_right_13009836 = default(uint);
        float __arm64_float_flags_left_13009696 = default(float);
        float __arm64_float_flags_left_13009708 = default(float);
        float __arm64_float_flags_right_13009696 = default(float);
        float __arm64_float_flags_right_13009708 = default(float);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        ulong x10 = default(ulong);
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
        x21 = 0x1BAB000UL;
        x20 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x317UL))))))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xE0UL))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC682F0;
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
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x317UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC682F0;
        label_0xC682F0:
        ;
        x0 = RuntimeMemory.ReadU64(x20);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x20UL))));
        x20 = unchecked((ulong)((x19) + (0x2CUL)));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC68308;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC68304UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC68308;
        label_0xC68308:
        ;
        x0 = x21;
        x1 = x20;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC36220UL /* metadata target: CF2Input.GetAxisRaw */, x0, x1, x2, x3);
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x28UL))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)((global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)), 0)) & (unchecked((uint)0x7FFFFFFFUL))))), 0)), 0));
        __arm64_float_flags_left_13009696 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13009696 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_13009696 <= __arm64_float_flags_right_13009696) || ((__arm64_float_flags_left_13009696 != __arm64_float_flags_left_13009696) || (__arm64_float_flags_right_13009696 != __arm64_float_flags_right_13009696))))
        {
            goto label_0xC68340;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(unchecked((uint)0x0UL)));
        __arm64_float_flags_left_13009708 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13009708 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        if (((__arm64_float_flags_left_13009708 <= __arm64_float_flags_right_13009708) || ((__arm64_float_flags_left_13009708 != __arm64_float_flags_left_13009708) || (__arm64_float_flags_right_13009708 != __arm64_float_flags_right_13009708))))
        {
            goto label_0xC68350;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x20 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        goto label_0xC68358;
        label_0xC68340:
        ;
        x8 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x20 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x9 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        goto label_0xC68358;
        label_0xC68350:
        ;
        x8 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x20 = unchecked((ulong)(unchecked((uint)(0xFFFFFFFFFFFFFFFFUL))));
        goto label_0xC68358;
        label_0xC68358:
        ;
        x10 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x34UL))))));
        __arm64_flags_left_13009756 = unchecked((uint)(x10));
        __arm64_flags_right_13009756 = unchecked((uint)0x2UL);
        if ((unchecked((uint)((__arm64_flags_left_13009756) - (__arm64_flags_right_13009756))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC68384;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC68364UL);
        }
        __arm64_flags_left_13009764 = unchecked((uint)(x10));
        __arm64_flags_right_13009764 = unchecked((uint)0x1UL);
        if ((unchecked((uint)((__arm64_flags_left_13009764) - (__arm64_flags_right_13009764))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC6839C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC6836CUL);
        }
        if ((unchecked((uint)(x10)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC683CC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC68370UL);
        }
        if ((unchecked((uint)((unchecked((uint)(x9))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC683CC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x30UL))))));
        __arm64_flags_left_13009784 = unchecked((uint)(x9));
        __arm64_flags_right_13009784 = unchecked((uint)(x20));
        if ((!((unchecked((uint)((__arm64_flags_left_13009784) - (__arm64_flags_right_13009784))) == unchecked((uint)0x0UL)))))
        {
            goto label_0xC68388;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC68380UL);
        }
        goto label_0xC683CC;
        label_0xC68384:
        ;
        if ((unchecked((uint)((unchecked((uint)(x9))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC683CC;
        }
        else
        {
            goto label_0xC68388;
        }
        label_0xC68388:
        ;
        __arm64_flags_left_13009800 = unchecked((uint)(x8));
        __arm64_flags_right_13009800 = unchecked((uint)0x0UL);
        x8 = unchecked((ulong)(unchecked((uint)(0x40UL))));
        x9 = unchecked((ulong)(unchecked((uint)(0x38UL))));
        RuntimeCalls.Unsupported("csel", 0xC68394UL);
        x8 = (__Unsupported<bool>("Unknown IR expression") ? x9 : x8);
        goto label_0xC683BC;
        label_0xC6839C:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x30UL))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC683CC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC683A4UL);
        }
        __arm64_flags_left_13009828 = unchecked((uint)(x20));
        __arm64_flags_right_13009828 = unchecked((uint)(x8));
        if ((unchecked((uint)((__arm64_flags_left_13009828) - (__arm64_flags_right_13009828))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC683CC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC683ACUL);
        }
        __arm64_flags_left_13009836 = unchecked((uint)(x8));
        __arm64_flags_right_13009836 = unchecked((uint)0x0UL);
        x8 = unchecked((ulong)(unchecked((uint)(0x40UL))));
        x9 = unchecked((ulong)(unchecked((uint)(0x38UL))));
        RuntimeCalls.Unsupported("csel", 0xC683B8UL);
        x8 = (__Unsupported<bool>("Unknown IR expression") ? x9 : x8);
        goto label_0xC683BC;
        label_0xC683BC:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (x8))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC683DC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17A29C8UL /* metadata target: UnityEvent.Invoke */, x0, x1, x2, x3);
        goto label_0xC683CC;
        label_0xC683CC:
        ;
        RuntimeMemory.WriteU32(unchecked((ulong)((x19) + (0x30UL))), unchecked((uint)(x20)));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return x0;
        label_0xC683DC:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```
