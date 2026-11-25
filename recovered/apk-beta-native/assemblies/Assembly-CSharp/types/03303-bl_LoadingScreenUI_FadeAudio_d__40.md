# `bl_LoadingScreenUI.<FadeAudio>d__40` — TypeDefIndex 3303

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x10` | `int` | `<>1__state` |
| `0x18` | `object` | `<>2__current` |
| `0x20` | `bl_LoadingScreenUI` | `<>4__this` |
| `0x28` | `bool` | `FadeIn` |

## `bl_LoadingScreenUI.<FadeAudio>d__40.ctor` — RVA `0xc78948`

- Lift status: **exact**; input span: 40 bytes; span to next metadata RVA: 40 bytes.
- Metadata signature: `public void .ctor(int <>1__state) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=5 (informational only).

```csharp
public static ulong bl_LoadingScreenUI_FadeAudio_d__40_ctor_RVAc78948(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
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

## `bl_LoadingScreenUI.<FadeAudio>d__40.Dispose` — RVA `0xc78ed8`

- Lift status: **exact**; input span: 4 bytes; span to next metadata RVA: 4 bytes.
- Metadata signature: `private void System.IDisposable.Dispose() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=0 (informational only).

```csharp
public static ulong bl_LoadingScreenUI_FadeAudio_d__40_Dispose_RVAc78ed8(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        return x0;
        return default(ulong);
    }
```

## `bl_LoadingScreenUI.<FadeAudio>d__40.MoveNext` — RVA `0xc78edc`

- Lift status: **exact**; input span: 544 bytes; span to next metadata RVA: 544 bytes.
- Metadata signature: `private bool MoveNext() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=70 (informational only).

```csharp
public static uint bl_LoadingScreenUI_FadeAudio_d__40_MoveNext_RVAc78edc(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13078304 = default(uint);
        uint __arm64_flags_left_13078312 = default(uint);
        uint __arm64_flags_right_13078304 = default(uint);
        uint __arm64_flags_right_13078312 = default(uint);
        float __arm64_float_flags_left_13078436 = default(float);
        float __arm64_float_flags_left_13078624 = default(float);
        float __arm64_float_flags_right_13078436 = default(float);
        float __arm64_float_flags_right_13078624 = default(float);
        ulong __arm64_load_address_13078768 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
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
        x20 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x3C6UL))))))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC78F18;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xA80UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x3C6UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC78F18;
        label_0xC78F18:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x10UL))))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x20UL))));
        __arm64_flags_left_13078304 = unchecked((uint)(x8));
        __arm64_flags_right_13078304 = unchecked((uint)0x2UL);
        if ((unchecked((uint)((__arm64_flags_left_13078304) - (__arm64_flags_right_13078304))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC78F84;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC78F28UL)));
        }
        __arm64_flags_left_13078312 = unchecked((uint)(x8));
        __arm64_flags_right_13078312 = unchecked((uint)0x1UL);
        if ((unchecked((uint)((__arm64_flags_left_13078312) - (__arm64_flags_right_13078312))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC79034;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC78F30UL)));
        }
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC790E4;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)(unchecked((uint)(0xFFFFFFFFFFFFFFFFUL))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x19) + (0x10UL))), unchecked((uint)(x8)));
        if ((x20 == 0x0UL))
        {
            goto label_0xC790F8;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xB0UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC790F8;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x9 = 0x1A8C000UL;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0xD8UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x88UL))));
        x0 = RuntimeMemory.ReadU64(x9);
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC78F64;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC78F60UL)));
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC78F64;
        label_0xC78F64:
        ;
        x0 = x21;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179568CUL /* metadata target: Object.op_Equality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC790E4;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x28UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC79040;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC78F80UL)));
        }
        goto label_0xC78F90;
        label_0xC78F84:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(0xFFFFFFFFFFFFFFFFUL))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x19) + (0x10UL))), unchecked((uint)(x8)));
        if ((x20 == 0x0UL))
        {
            goto label_0xC790F8;
        }
        else
        {
            goto label_0xC78F90;
        }
        label_0xC78F90:
        ;
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xC78394UL /* metadata target: bl_LoadingScreenUI.get_Source */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC790F8;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x176A43CUL /* metadata target: AudioSource.get_volume */, x0, x1, x2, x3);
        __arm64_float_flags_left_13078436 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13078436 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        if (((__arm64_float_flags_left_13078436 <= __arm64_float_flags_right_13078436) || ((__arm64_float_flags_left_13078436 != __arm64_float_flags_left_13078436) || (__arm64_float_flags_right_13078436 != __arm64_float_flags_right_13078436))))
        {
            goto label_0xC790E4;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xC78394UL /* metadata target: bl_LoadingScreenUI.get_Source */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC790F8;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = 0x0UL;
        x21 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x176A43CUL /* metadata target: AudioSource.get_volume */, x0, x1, x2, x3);
        x0 = x20;
        v8 = v0;
        x0 = RuntimeCalls.InvokeDirect(0xC78B24UL /* metadata target: bl_LoadingScreenUI.get_DeltaTime */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xB0UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC790F8;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC78FD8UL)));
        }
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x74UL))))), 0));
        x0 = x21;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x176A478UL /* metadata target: AudioSource.set_volume */, x0, x1, x2, x3);
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xA80UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x1799AF0UL /* metadata target: WaitForEndOfFrame.ctor */, x0, x1, x2, x3);
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x18UL))), x20);
        x0 = x19;
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x2UL))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x19) + (0xFFFFFFFFFFFFFFF8UL))), unchecked((uint)(x8)));
        x0 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        goto label_0xC790E8;
        label_0xC79034:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(0xFFFFFFFFFFFFFFFFUL))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x19) + (0x10UL))), unchecked((uint)(x8)));
        if ((x20 == 0x0UL))
        {
            goto label_0xC790F8;
        }
        else
        {
            goto label_0xC79040;
        }
        label_0xC79040:
        ;
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xC78394UL /* metadata target: bl_LoadingScreenUI.get_Source */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC790F8;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x176A43CUL /* metadata target: AudioSource.get_volume */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xB0UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC790F8;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC7905CUL)));
        }
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x70UL))))), 0));
        __arm64_float_flags_left_13078624 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13078624 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_13078624 >= __arm64_float_flags_right_13078624) || ((__arm64_float_flags_left_13078624 != __arm64_float_flags_left_13078624) || (__arm64_float_flags_right_13078624 != __arm64_float_flags_right_13078624))))
        {
            goto label_0xC790E4;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xC78394UL /* metadata target: bl_LoadingScreenUI.get_Source */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC790F8;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = 0x0UL;
        x21 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x176A43CUL /* metadata target: AudioSource.get_volume */, x0, x1, x2, x3);
        x0 = x20;
        v8 = v0;
        x0 = RuntimeCalls.InvokeDirect(0xC78B24UL /* metadata target: bl_LoadingScreenUI.get_DeltaTime */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xB0UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC790F8;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC79094UL)));
        }
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x74UL))))), 0));
        x0 = x21;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x176A478UL /* metadata target: AudioSource.set_volume */, x0, x1, x2, x3);
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xA80UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x1799AF0UL /* metadata target: WaitForEndOfFrame.ctor */, x0, x1, x2, x3);
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x18UL))), x20);
        x0 = x19;
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x19) + (0xFFFFFFFFFFFFFFF8UL))), unchecked((uint)(x0)));
        goto label_0xC790E8;
        label_0xC790E4:
        ;
        x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xC790E8;
        label_0xC790E8:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        __arm64_load_address_13078768 = sp;
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_load_address_13078768)), 0));
        return unchecked((uint)(x0));
        label_0xC790F8:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        return default(uint);
    }
```

## `bl_LoadingScreenUI.<FadeAudio>d__40.get_Current` — RVA `0xc790fc`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `private object System.Collections.Generic.IEnumerator<System.Object>.get_Current() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static ulong bl_LoadingScreenUI_FadeAudio_d__40_get_Current_RVAc790fc(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x18UL))));
        return x0;
        return default(ulong);
    }
```

## `bl_LoadingScreenUI.<FadeAudio>d__40.Reset` — RVA `0xc79104`

- Lift status: **exact**; input span: 56 bytes; span to next metadata RVA: 56 bytes.
- Metadata signature: `private void System.Collections.IEnumerator.Reset() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=8 (informational only).

```csharp
public static ulong bl_LoadingScreenUI_FadeAudio_d__40_Reset_RVAc79104(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
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
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB20UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D940UL, x0, x1, x2, x3);
        x1 = x0;
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xB7DA4CUL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `bl_LoadingScreenUI.<FadeAudio>d__40.get_Current` — RVA `0xc7913c`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `private object System.Collections.IEnumerator.get_Current() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static ulong bl_LoadingScreenUI_FadeAudio_d__40_get_Current_RVAc7913c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x18UL))));
        return x0;
        return default(ulong);
    }
```
