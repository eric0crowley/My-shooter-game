# `InputRig.TiltConfig` — TypeDefIndex 5004

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x10` | `InputRig` | `rig` |
| `0x18` | `TiltState` | `tiltState` |
| `0x20` | `int` | `digitalRollDirection` |
| `0x24` | `int` | `digitalPitchDirection` |
| `0x28` | `bool` | `disabledByRigSwitches` |
| `0x30` | `DisablingConditionSet` | `disablingConditions` |
| `0x38` | `AnalogConfig` | `rollAnalogConfig` |
| `0x40` | `AnalogConfig` | `pitchAnalogConfig` |
| `0x48` | `AxisBinding` | `rollBinding` |
| `0x50` | `AxisBinding` | `pitchBinding` |
| `0x58` | `DigitalBinding` | `rollLeftBinding` |
| `0x60` | `DigitalBinding` | `rollRightBinding` |
| `0x68` | `DigitalBinding` | `pitchForwardBinding` |
| `0x70` | `DigitalBinding` | `pitchBackwardBinding` |

## `InputRig.TiltConfig.ctor` — RVA `0xc427e0`

- Lift status: **exact**; input span: 688 bytes; span to next metadata RVA: 688 bytes.
- Metadata signature: `public void .ctor(InputRig rig) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=109 (informational only).

```csharp
public static ulong InputRig_TiltConfig_ctor_RVAc427e0(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x10 = default(ulong);
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
        x22 = 0x1BAB000UL;
        x21 = 0x1A8C000UL;
        x23 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x22) + (0x20AUL))))))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xAE0UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0x68UL))));
        x20 = x1;
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC4286C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x68UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x990UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x988UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xA90UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xAE0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x538UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x548UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x22) + (0x20AUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC4286C;
        label_0xC4286C:
        ;
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1589338UL /* metadata target: Object.ctor */, x0, x1, x2, x3);
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x10UL))), x20);
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x21);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = 0x0UL;
        x21 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC616ECUL /* metadata target: TiltState.ctor */, x0, x1, x2, x3);
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x18UL))), x21);
        x1 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x23);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = 0x0UL;
        x21 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC56BB8UL /* metadata target: AnalogConfig.ctor */, x0, x1, x2, x3);
        x22 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x22) + (0x38UL))), x21);
        x0 = x22;
        x1 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x23);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = 0x0UL;
        x23 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC56BB8UL /* metadata target: AnalogConfig.ctor */, x0, x1, x2, x3);
        x21 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x21) + (0x40UL))), x23);
        x0 = x21;
        x1 = x23;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x9 = RuntimeMemory.ReadU64(x22);
        if ((x9 == 0x0UL))
        {
            goto label_0xC42A8C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(0x999AUL))));
        x8 = unchecked((ulong)(unchecked((uint)(unchecked((ulong)((unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((~(0xFFFFUL)))))))))) | (unchecked((ulong)((unchecked((ulong)((0x3E99UL) << (int)(unchecked((int)(0x10UL)))))) << (int)(unchecked((int)(0x0UL))))))))))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x9) + (0x10UL))), unchecked((uint)(x8)));
        x9 = RuntimeMemory.ReadU64(x21);
        if ((x9 == 0x0UL))
        {
            goto label_0xC42A8C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = 0x1A8C000UL;
        x10 = RuntimeMemory.ReadU64(unchecked((ulong)((x10) + (0xA90UL))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x9) + (0x10UL))), unchecked((uint)(x8)));
        x0 = RuntimeMemory.ReadU64(x10);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = x20;
        x2 = 0x0UL;
        x21 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC4F5B4UL /* metadata target: DisablingConditionSet.ctor */, x0, x1, x2, x3);
        x20 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x20) + (0x30UL))), x21);
        x0 = x20;
        x1 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x20);
        if ((x8 == 0x0UL))
        {
            goto label_0xC42A8C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x22 = 0x1A8C000UL;
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x990UL))));
        RuntimeMemory.WriteU16(unchecked((ulong)((x8) + (0x14UL))), unchecked((ushort)(unchecked((uint)0x0UL))));
        RuntimeMemory.WritePtr(unchecked((ulong)((x8) + (0x10UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        x20 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(x22);
        x23 = 0x1A8C000UL;
        x21 = 0x1A8C000UL;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x548UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0x538UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x988UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = RuntimeMemory.ReadU64(x20);
        x2 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x3 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC56D68UL /* metadata target: AxisBinding.ctor */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x48UL))), x20);
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = RuntimeMemory.ReadU64(x22);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x1 = RuntimeMemory.ReadU64(x23);
        x2 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x3 = 0x0UL;
        x4 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC56D68UL /* metadata target: AxisBinding.ctor */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x50UL))), x20);
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = RuntimeMemory.ReadU64(x21);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x1 = 0x0UL;
        x2 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC4EAA8UL /* metadata target: DigitalBinding.ctor */, x0, x1, x2, x3);
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x58UL))), x20);
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x21);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = 0x0UL;
        x2 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC4EAA8UL /* metadata target: DigitalBinding.ctor */, x0, x1, x2, x3);
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x60UL))), x20);
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x21);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = 0x0UL;
        x2 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC4EAA8UL /* metadata target: DigitalBinding.ctor */, x0, x1, x2, x3);
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x68UL))), x20);
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x21);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = 0x0UL;
        x2 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC4EAA8UL /* metadata target: DigitalBinding.ctor */, x0, x1, x2, x3);
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x70UL))), x20);
        x0 = x19;
        x1 = x20;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeDirect(0xB7D8D0UL);
        label_0xC42A8C:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `InputRig.TiltConfig.Reset` — RVA `0xc42a90`

- Lift status: **exact**; input span: 44 bytes; span to next metadata RVA: 44 bytes.
- Metadata signature: `public void Reset() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=5 (informational only).

```csharp
public static ulong InputRig_TiltConfig_Reset_RVAc42a90(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x8UL))), x19);
        x19 = x0;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x18UL))));
        RuntimeMemory.WritePtr(unchecked((ulong)((x19) + (0x20UL))), 0x0UL);
        if ((x0 == 0x0UL))
        {
            goto label_0xC42AB8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC61720UL /* metadata target: TiltState.Reset */, x0, x1, x2, x3);
        x0 = x19;
        x30 = RuntimeMemory.ReadU64(sp);
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeDirect(0xC42ABCUL /* metadata target: InputRig.TiltConfig.OnDisablingConditionsChange */);
        label_0xC42AB8:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `InputRig.TiltConfig.OnDisablingConditionsChange` — RVA `0xc42abc`

- Lift status: **exact**; input span: 44 bytes; span to next metadata RVA: 44 bytes.
- Metadata signature: `public void OnDisablingConditionsChange() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=5 (informational only).

```csharp
public static ulong InputRig_TiltConfig_OnDisablingConditionsChange_RVAc42abc(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x8UL))), x19);
        x19 = x0;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x30UL))));
        if ((x0 == 0x0UL))
        {
            label_0xC42AE4:
            ;
            x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        }
        else
        {
            x1 = 0x0UL;
            x0 = RuntimeCalls.InvokeDirect(0xC4FD60UL /* metadata target: DisablingConditionSet.IsInEffect */, x0, x1, x2, x3);
            x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)(0x1UL)))))));
            RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x28UL))), unchecked((byte)(unchecked((uint)(x8)))));
            x30 = RuntimeMemory.ReadU64(sp);
            x19 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
            return x0;
        }
        return default(ulong);
    }
```

## `InputRig.TiltConfig.IsEnabled` — RVA `0xc42ae8`

- Lift status: **exact**; input span: 16 bytes; span to next metadata RVA: 16 bytes.
- Metadata signature: `public bool IsEnabled() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static uint InputRig_TiltConfig_IsEnabled_RVAc42ae8(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12856044 = default(uint);
        uint __arm64_flags_right_12856044 = default(uint);
        ulong x8 = default(ulong);
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x28UL))))))));
        __arm64_flags_left_12856044 = unchecked((uint)(x8));
        __arm64_flags_right_12856044 = unchecked((uint)0x0UL);
        x0 = unchecked((ulong)(((unchecked((uint)((__arm64_flags_left_12856044) - (__arm64_flags_right_12856044))) == unchecked((uint)0x0UL)) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        return unchecked((uint)(x0));
        return default(uint);
    }
```

## `InputRig.TiltConfig.Update` — RVA `0xc42af8`

- Lift status: **partial**; input span: 388 bytes; span to next metadata RVA: 388 bytes.
- Metadata signature: `public void Update() { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=56 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'csel' at 0xc42c18; reason: Unknown IR expression at 0xc42c18; reason: Unsupported instruction 'csel' at 0xc42c4c; reason: Unknown IR expression at 0xc42c4c

```csharp
public static ulong InputRig_TiltConfig_Update_RVAc42af8(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12856332 = default(uint);
        uint __arm64_flags_left_12856384 = default(uint);
        uint __arm64_flags_right_12856332 = default(uint);
        uint __arm64_flags_right_12856384 = default(uint);
        ulong __arm64_pair_address_12856056 = default(ulong);
        ulong __arm64_pair_address_12856132 = default(ulong);
        ulong __arm64_pair_address_12856204 = default(ulong);
        ulong __arm64_pair_address_12856432 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        RuntimeVector128 v9 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        __arm64_pair_address_12856056 = unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFD0UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12856056, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12856056) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        sp = __arm64_pair_address_12856056;
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x10UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x19);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x18UL))));
        x19 = x0;
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17C7CBCUL /* metadata target: Input.get_acceleration */, x0, x1, x2, x3);
        if ((x20 == 0x0UL))
        {
            goto label_0xC42C78;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC61780UL /* metadata target: TiltState.InternalApplyVector */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x18UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC42C78;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC6184CUL /* metadata target: TiltState.Update */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x18UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC42C78;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x38UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC42C78;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC42B44UL);
        }
        __arm64_pair_address_12856132 = unchecked((ulong)((x8) + (0x50UL)));
        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12856132)), 0));
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12856132) + (0x4UL))))), 0));
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x20UL))))));
        x2 = 0x0UL;
        v0 = v9;
        x0 = RuntimeCalls.InvokeDirect(0xC5ACC4UL /* metadata target: AnalogConfig.GetSignedDigitalVal */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x40UL))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x19) + (0x20UL))), unchecked((uint)(x0)));
        if ((x8 == 0x0UL))
        {
            goto label_0xC42C78;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x24UL))))));
        x0 = x8;
        v0 = v8;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC5ACC4UL /* metadata target: AnalogConfig.GetSignedDigitalVal */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x28UL))))))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x19) + (0x24UL))), unchecked((uint)(x0)));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC42B94;
        }
        else
        {
            goto label_0xC42B84;
        }
        label_0xC42B84:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        __arm64_pair_address_12856204 = sp;
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12856204)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12856204) + (0x8UL))))), 0));
        sp = unchecked((ulong)((__arm64_pair_address_12856204) + (0x30UL)));
        return x0;
        label_0xC42B94:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x48UL))));
        if ((x20 == 0x0UL))
        {
            goto label_0xC42C78;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x10UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC42BCC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x38UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC42C78;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        v0 = v9;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC574F8UL /* metadata target: AnalogConfig.GetAnalogVal */, x0, x1, x2, x3);
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x10UL))));
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = x20;
        x3 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC4F160UL /* metadata target: AxisBinding.SyncFloat */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xC42BCC;
        label_0xC42BCC:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x50UL))));
        if ((x20 == 0x0UL))
        {
            goto label_0xC42C78;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x10UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC42C04;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x40UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC42C78;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        v0 = v8;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC574F8UL /* metadata target: AnalogConfig.GetAnalogVal */, x0, x1, x2, x3);
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x10UL))));
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = x20;
        x3 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC4F160UL /* metadata target: AxisBinding.SyncFloat */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xC42C04;
        label_0xC42C04:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x20UL))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC42C38;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC42C0CUL);
        }
        __arm64_flags_left_12856332 = unchecked((uint)(x8));
        __arm64_flags_right_12856332 = unchecked((uint)0x0UL);
        x8 = unchecked((ulong)(unchecked((uint)(0x60UL))));
        x9 = unchecked((ulong)(unchecked((uint)(0x58UL))));
        RuntimeCalls.Unsupported("csel", 0xC42C18UL);
        x8 = (__Unsupported<bool>("Unknown IR expression") ? x9 : x8);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (x8))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC42C78;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x10UL))));
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x3 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x4 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC4F00CUL /* metadata target: DigitalBinding.Sync */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, unchecked((ulong)(unchecked((uint)(x3)))));
        goto label_0xC42C38;
        label_0xC42C38:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x24UL))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC42B84;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC42C40UL);
        }
        __arm64_flags_left_12856384 = unchecked((uint)(x8));
        __arm64_flags_right_12856384 = unchecked((uint)0x0UL);
        x8 = unchecked((ulong)(unchecked((uint)(0x68UL))));
        x9 = unchecked((ulong)(unchecked((uint)(0x70UL))));
        RuntimeCalls.Unsupported("csel", 0xC42C4CUL);
        x8 = (__Unsupported<bool>("Unknown IR expression") ? x9 : x8);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (x8))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC42C78;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x10UL))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x3 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x4 = 0x0UL;
        __arm64_pair_address_12856432 = sp;
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12856432)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12856432) + (0x8UL))))), 0));
        sp = unchecked((ulong)((__arm64_pair_address_12856432) + (0x30UL)));
        return RuntimeCalls.InvokeDirect(0xC4F00CUL /* metadata target: DigitalBinding.Sync */);
        label_0xC42C78:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, unchecked((ulong)(unchecked((uint)(x3)))));
        return default(ulong);
    }
```

## `InputRig.TiltConfig.IsBoundToAxis` — RVA `0xc42c7c`

- Lift status: **exact**; input span: 204 bytes; span to next metadata RVA: 204 bytes.
- Metadata signature: `public bool IsBoundToAxis(string axisName, InputRig rig) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=30 (informational only).

```csharp
public static uint InputRig_TiltConfig_IsBoundToAxis_RVAc42c7c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
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
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x48UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC42D44;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x3 = 0x0UL;
        x19 = x2;
        x20 = x1;
        x0 = RuntimeCalls.InvokeDirect(0xC5DE34UL /* metadata target: InputBindingBase.IsBoundToAxis */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC42D14;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x50UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC42D44;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = x20;
        x2 = x19;
        x3 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC5DE34UL /* metadata target: InputBindingBase.IsBoundToAxis */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC42D14;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x58UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC42D44;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = x20;
        x2 = x19;
        x3 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC5DE34UL /* metadata target: InputBindingBase.IsBoundToAxis */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC42D14;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x60UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC42D44;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = x20;
        x2 = x19;
        x3 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC5DE34UL /* metadata target: InputBindingBase.IsBoundToAxis */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC42D14;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x68UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC42D44;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = x20;
        x2 = x19;
        x3 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC5DE34UL /* metadata target: InputBindingBase.IsBoundToAxis */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC42D24;
        }
        else
        {
            goto label_0xC42D14;
        }
        label_0xC42D14:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x0 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return unchecked((uint)(x0));
        label_0xC42D24:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x70UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC42D44;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = x20;
        x2 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x3 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC5DE34UL /* metadata target: InputBindingBase.IsBoundToAxis */)));
        label_0xC42D44:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(uint);
    }
```

## `InputRig.TiltConfig.IsBoundToKey` — RVA `0xc42d48`

- Lift status: **exact**; input span: 204 bytes; span to next metadata RVA: 204 bytes.
- Metadata signature: `public bool IsBoundToKey(KeyCode key, InputRig rig) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=30 (informational only).

```csharp
public static uint InputRig_TiltConfig_IsBoundToKey_RVAc42d48(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
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
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x48UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC42E10;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x3 = 0x0UL;
        x19 = x2;
        x20 = unchecked((ulong)(unchecked((uint)(x1))));
        x0 = RuntimeCalls.InvokeDirect(0xC5DE28UL /* metadata target: InputBindingBase.IsBoundToKey */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC42DE0;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x50UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC42E10;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = unchecked((ulong)(unchecked((uint)(x20))));
        x2 = x19;
        x3 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC5DE28UL /* metadata target: InputBindingBase.IsBoundToKey */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC42DE0;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x58UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC42E10;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = unchecked((ulong)(unchecked((uint)(x20))));
        x2 = x19;
        x3 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC5DE28UL /* metadata target: InputBindingBase.IsBoundToKey */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC42DE0;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x60UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC42E10;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = unchecked((ulong)(unchecked((uint)(x20))));
        x2 = x19;
        x3 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC5DE28UL /* metadata target: InputBindingBase.IsBoundToKey */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC42DE0;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x68UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC42E10;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = unchecked((ulong)(unchecked((uint)(x20))));
        x2 = x19;
        x3 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC5DE28UL /* metadata target: InputBindingBase.IsBoundToKey */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC42DF0;
        }
        else
        {
            goto label_0xC42DE0;
        }
        label_0xC42DE0:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x0 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return unchecked((uint)(x0));
        label_0xC42DF0:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x70UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC42E10;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = unchecked((ulong)(unchecked((uint)(x20))));
        x2 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x3 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC5DE28UL /* metadata target: InputBindingBase.IsBoundToKey */)));
        label_0xC42E10:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        return default(uint);
    }
```

## `InputRig.TiltConfig.IsEmulatingTouches` — RVA `0xc42e14`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public bool IsEmulatingTouches() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static uint InputRig_TiltConfig_IsEmulatingTouches_RVAc42e14(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
        return unchecked((uint)(x0));
        return default(uint);
    }
```

## `InputRig.TiltConfig.IsEmulatingMousePosition` — RVA `0xc42e1c`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public bool IsEmulatingMousePosition() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static uint InputRig_TiltConfig_IsEmulatingMousePosition_RVAc42e1c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
        return unchecked((uint)(x0));
        return default(uint);
    }
```

## `InputRig.TiltConfig.GetSubBindingDescriptions` — RVA `0xc42e24`

- Lift status: **exact**; input span: 380 bytes; span to next metadata RVA: 380 bytes.
- Metadata signature: `public void GetSubBindingDescriptions(BindingDescriptionList descList, Object undoObject, string parentMenuPath) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=74 (informational only).

```csharp
public static ulong InputRig_TiltConfig_GetSubBindingDescriptions_RVAc42e24(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x22 = default(ulong);
        ulong x23 = default(ulong);
        ulong x24 = default(ulong);
        ulong x25 = default(ulong);
        ulong x26 = default(ulong);
        ulong x27 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFB0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFB0UL)))) + (0x8UL))), x27);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x26);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x25);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x24);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))), x19);
        x23 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x23) + (0x20BUL))))))));
        x20 = x3;
        x19 = x2;
        x21 = x1;
        x22 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC42EA4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xAE8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xAF0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xAF8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB00UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB08UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB10UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x23) + (0x20BUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC42EA4;
        label_0xC42EA4:
        ;
        if ((x21 == 0x0UL))
        {
            goto label_0xC42F9C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB00UL))));
        x23 = 0x1A8C000UL;
        x24 = 0x1A8C000UL;
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0xAF8UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((x24) + (0xB08UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x48UL))));
        x3 = RuntimeMemory.ReadU64(x8);
        x25 = 0x1A8C000UL;
        x26 = 0x1A8C000UL;
        x27 = 0x1A8C000UL;
        x25 = RuntimeMemory.ReadU64(unchecked((ulong)((x25) + (0xB10UL))));
        x26 = RuntimeMemory.ReadU64(unchecked((ulong)((x26) + (0xAE8UL))));
        x27 = RuntimeMemory.ReadU64(unchecked((ulong)((x27) + (0xAF0UL))));
        x2 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xC5DAACUL /* metadata target: BindingDescriptionList.Add */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x50UL))));
        x3 = RuntimeMemory.ReadU64(x23);
        x2 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = x21;
        x6 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC5DAACUL /* metadata target: BindingDescriptionList.Add */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x58UL))));
        x2 = RuntimeMemory.ReadU64(x24);
        x0 = x21;
        x3 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xC5D750UL /* metadata target: BindingDescriptionList.Add */, x0, x1, x2, x3);
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x60UL))));
        x2 = RuntimeMemory.ReadU64(x25);
        x0 = x21;
        x3 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xC5D750UL /* metadata target: BindingDescriptionList.Add */, x0, x1, x2, x3);
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x68UL))));
        x2 = RuntimeMemory.ReadU64(x26);
        x0 = x21;
        x3 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xC5D750UL /* metadata target: BindingDescriptionList.Add */, x0, x1, x2, x3);
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x70UL))));
        x2 = RuntimeMemory.ReadU64(x27);
        x0 = x21;
        x3 = x20;
        x4 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x40UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x26 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x25 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x5 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        x27 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeDirect(0xC5D750UL /* metadata target: BindingDescriptionList.Add */);
        label_0xC42F9C:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```
