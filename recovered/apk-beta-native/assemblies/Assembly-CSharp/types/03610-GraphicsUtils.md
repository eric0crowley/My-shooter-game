# `GraphicsUtils` — TypeDefIndex 3610

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## `GraphicsUtils.get_isLinearColorSpace` — RVA `0xcdec1c`

- Lift status: **exact**; input span: 28 bytes; span to next metadata RVA: 28 bytes.
- Metadata signature: `public static bool get_isLinearColorSpace() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=2 (informational only).

```csharp
public static uint GraphicsUtils_get_isLinearColorSpace_RVAcdec1c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13495336 = default(uint);
        uint __arm64_flags_right_13495336 = default(uint);
        ulong sp = default(ulong);
        ulong x30 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL))), x30);
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1779320UL /* metadata target: QualitySettings.get_activeColorSpace */, x0, x1, x2, x3);
        __arm64_flags_left_13495336 = unchecked((uint)(x0));
        __arm64_flags_right_13495336 = unchecked((uint)0x1UL);
        x0 = unchecked((ulong)(((unchecked((uint)((__arm64_flags_left_13495336) - (__arm64_flags_right_13495336))) == unchecked((uint)0x0UL)) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return unchecked((uint)(x0));
        return default(uint);
    }
```

## `GraphicsUtils.get_supportsDX11` — RVA `0xcdec38`

- Lift status: **exact**; input span: 44 bytes; span to next metadata RVA: 44 bytes.
- Metadata signature: `public static bool get_supportsDX11() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=5 (informational only).

```csharp
public static uint GraphicsUtils_get_supportsDX11_RVAcdec38(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13495364 = default(uint);
        uint __arm64_flags_right_13495364 = default(uint);
        ulong sp = default(ulong);
        ulong x30 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL))), x30);
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179A7C4UL /* metadata target: SystemInfo.get_graphicsShaderLevel */, x0, x1, x2, x3);
        __arm64_flags_left_13495364 = unchecked((uint)(x0));
        __arm64_flags_right_13495364 = unchecked((uint)0x32UL);
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13495364) - (__arm64_flags_right_13495364))))) < unchecked((int)0x0UL)) == (((unchecked((int)(__arm64_flags_left_13495364)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13495364)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13495364) - (__arm64_flags_right_13495364))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13495364)) < unchecked((int)0x0UL))))))
        {
            goto label_0xCDEC58;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x30 = RuntimeMemory.ReadU64(sp);
        return unchecked((uint)(x0));
        label_0xCDEC58:
        ;
        x0 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        return unchecked((uint)(RuntimeCalls.InvokeDirect(0x179A86CUL /* metadata target: SystemInfo.get_supportsComputeShaders */)));
        return default(uint);
    }
```

## `GraphicsUtils.get_whiteTexture` — RVA `0xcdec64`

- Lift status: **exact**; input span: 300 bytes; span to next metadata RVA: 300 bytes.
- Metadata signature: `public static Texture2D get_whiteTexture() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=54 (informational only).

```csharp
public static ulong GraphicsUtils_get_whiteTexture_RVAcdec64(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
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
        x21 = 0x1BAB000UL;
        x20 = 0x1A8F000UL;
        x19 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x624UL))))))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x868UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xD8UL))));
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCDECB4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x868UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xE68UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x624UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCDECB4;
        label_0xCDECB4:
        ;
        x8 = RuntimeMemory.ReadU64(x20);
        x0 = RuntimeMemory.ReadU64(x19);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        x19 = RuntimeMemory.ReadU64(x8);
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCDECD0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCDECCCUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCDECD0;
        label_0xCDECD0:
        ;
        x0 = x19;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794AC8UL /* metadata target: Object.op_Inequality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCDED74;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xE68UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x2 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x3 = unchecked((ulong)(unchecked((uint)(0x5UL))));
        x19 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x177F454UL /* metadata target: Texture2D.ctor */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x8 = RuntimeMemory.ReadU64(x20);
        x1 = x19;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        RuntimeMemory.WriteU64(x8, x19);
        x8 = RuntimeMemory.ReadU64(x20);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x8 = RuntimeMemory.ReadU64(x20);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        if ((x0 == 0x0UL))
        {
            goto label_0xCDED8C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x2 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x3 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177F5ACUL /* metadata target: Texture2D.SetPixel */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x8 = RuntimeMemory.ReadU64(x20);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        if ((x0 == 0x0UL))
        {
            goto label_0xCDED8C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177F858UL /* metadata target: Texture2D.Apply */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xCDED74;
        label_0xCDED74:
        ;
        x8 = RuntimeMemory.ReadU64(x20);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return x0;
        label_0xCDED8C:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        return default(ulong);
    }
```

## `GraphicsUtils.get_quad` — RVA `0xcded90`

- Lift status: **partial**; input span: 624 bytes; span to next metadata RVA: 624 bytes.
- Metadata signature: `public static Mesh get_quad() { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=85 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'fmov' at 0xcdee6c; reason: Unsupported instruction 'b.eq' at 0xcdee7c; reason: Unknown IR expression at 0xcdee7c; reason: Unsupported instruction 'fmov' at 0xcdee80; reason: Unsupported instruction 'b.ls' at 0xcdee90; reason: Unknown IR expression at 0xcdee90; reason: Unsupported instruction 'b.eq' at 0xcdeea8; reason: Unknown IR expression at 0xcdeea8

```csharp
public static ulong GraphicsUtils_get_quad_RVAcded90(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13495920 = default(uint);
        uint __arm64_flags_left_13495940 = default(uint);
        uint __arm64_flags_left_13495964 = default(uint);
        uint __arm64_flags_left_13496032 = default(uint);
        uint __arm64_flags_left_13496044 = default(uint);
        uint __arm64_flags_left_13496064 = default(uint);
        uint __arm64_flags_right_13495920 = default(uint);
        uint __arm64_flags_right_13495940 = default(uint);
        uint __arm64_flags_right_13495964 = default(uint);
        uint __arm64_flags_right_13496032 = default(uint);
        uint __arm64_flags_right_13496044 = default(uint);
        uint __arm64_flags_right_13496064 = default(uint);
        ulong __arm64_load_address_13496304 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x22 = default(ulong);
        ulong x23 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteF64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFC0UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        sp = unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFC0UL)));
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))), x19);
        x20 = 0x1BAB000UL;
        x23 = 0x1A8F000UL;
        x19 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x625UL))))))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0x868UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xD8UL))));
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCDEE18;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x868UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xDE8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xE20UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x870UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xC70UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB90UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x625UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCDEE18;
        label_0xCDEE18:
        ;
        x8 = RuntimeMemory.ReadU64(x23);
        x0 = RuntimeMemory.ReadU64(x19);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x8UL))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCDEE34;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCDEE30UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCDEE34;
        label_0xCDEE34:
        ;
        x0 = x19;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794AC8UL /* metadata target: Object.op_Inequality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCDEFD8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB90UL))));
        x1 = unchecked((ulong)(unchecked((uint)(0x4UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xB7D9D4UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCDEFFC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x18UL))))));
        x19 = x0;
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCDEFF8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCDEE6CUL);
        }
        RuntimeCalls.Unsupported("fmov", 0xCDEE6CUL);
        __arm64_flags_left_13495920 = unchecked((uint)(x8));
        __arm64_flags_right_13495920 = unchecked((uint)0x1UL);
        RuntimeMemory.WriteF64(unchecked((ulong)((x19) + (0x20UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))));
        RuntimeMemory.WritePtr(unchecked((ulong)((x19) + (0x28UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        RuntimeCalls.Unsupported("b.eq", 0xCDEE7CUL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xCDEFF8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCDEE80UL);
        }
        RuntimeCalls.Unsupported("fmov", 0xCDEE80UL);
        __arm64_flags_left_13495940 = unchecked((uint)(x8));
        __arm64_flags_right_13495940 = unchecked((uint)0x2UL);
        RuntimeMemory.WriteF64(unchecked((ulong)((x19) + (0x2CUL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        RuntimeMemory.WritePtr(unchecked((ulong)((x19) + (0x34UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        RuntimeCalls.Unsupported("b.ls", 0xCDEE90UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xCDEFF8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = 0x431000UL;
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((x9) + (0xD30UL))))), 0));
        __arm64_flags_left_13495964 = unchecked((uint)(x8));
        __arm64_flags_right_13495964 = unchecked((uint)0x3UL);
        RuntimeMemory.WritePtr(unchecked((ulong)((x19) + (0x40UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        RuntimeMemory.WriteF64(unchecked((ulong)((x19) + (0x38UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))));
        RuntimeCalls.Unsupported("b.eq", 0xCDEEA8UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xCDEFF8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x431000UL;
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((x8) + (0xE60UL))))), 0));
        RuntimeMemory.WritePtr(unchecked((ulong)((x19) + (0x4CUL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        x8 = 0x1A8E000UL;
        x1 = unchecked((ulong)(unchecked((uint)(0x4UL))));
        RuntimeMemory.WriteF64(unchecked((ulong)((x19) + (0x44UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xC70UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xB7D9D4UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCDEFFC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x18UL))))));
        x20 = x0;
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCDEFF8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCDEEE0UL);
        }
        __arm64_flags_left_13496032 = unchecked((uint)(x8));
        __arm64_flags_right_13496032 = unchecked((uint)0x1UL);
        RuntimeMemory.WritePtr(unchecked((ulong)((x20) + (0x20UL))), 0x0UL);
        RuntimeCalls.Unsupported("b.eq", 0xCDEEE8UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xCDEFF8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCDEEECUL);
        }
        __arm64_flags_left_13496044 = unchecked((uint)(x8));
        __arm64_flags_right_13496044 = unchecked((uint)0x2UL);
        RuntimeMemory.WriteF64(unchecked((ulong)((x20) + (0x28UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        if (((!((__arm64_flags_left_13496044 >= __arm64_flags_right_13496044))) || (unchecked((uint)((__arm64_flags_left_13496044) - (__arm64_flags_right_13496044))) == unchecked((uint)0x0UL))))
        {
            goto label_0xCDEFF8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = 0x431000UL;
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((x9) + (0xB80UL))))), 0));
        __arm64_flags_left_13496064 = unchecked((uint)(x8));
        __arm64_flags_right_13496064 = unchecked((uint)0x3UL);
        RuntimeMemory.WriteF64(unchecked((ulong)((x20) + (0x30UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))));
        if ((unchecked((uint)((__arm64_flags_left_13496064) - (__arm64_flags_right_13496064))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCDEFF8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x432000UL;
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((x8) + (0x78UL))))), 0));
        x8 = 0x1A8E000UL;
        x1 = unchecked((ulong)(unchecked((uint)(0x6UL))));
        RuntimeMemory.WriteF64(unchecked((ulong)((x20) + (0x38UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xDE8UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xB7D9D4UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = 0x1A8F000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x870UL))));
        x2 = 0x0UL;
        x21 = x0;
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x148E41CUL /* metadata target: RuntimeHelpers.InitializeArray */, x0, x1, x2, x3);
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xE20UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = 0x0UL;
        x22 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x177C0DCUL /* metadata target: Mesh.ctor */, x0, x1, x2, x3);
        if ((x22 == 0x0UL))
        {
            goto label_0xCDEFFC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x22;
        x1 = x19;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177CA40UL /* metadata target: Mesh.set_vertices */, x0, x1, x2, x3);
        x0 = x22;
        x1 = x20;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177CC44UL /* metadata target: Mesh.set_uv */, x0, x1, x2, x3);
        x0 = x22;
        x1 = x21;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177D68CUL /* metadata target: Mesh.set_triangles */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x23);
        x1 = x22;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x8UL))), x22);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x23);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCDEFFC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177DE6CUL /* metadata target: Mesh.RecalculateNormals */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x23);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCDEFFC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177DD70UL /* metadata target: Mesh.RecalculateBounds */, x0, x1, x2, x3);
        goto label_0xCDEFD8;
        label_0xCDEFD8:
        ;
        x8 = RuntimeMemory.ReadU64(x23);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x8UL))));
        __arm64_load_address_13496304 = sp;
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_load_address_13496304)), 0));
        sp = unchecked((ulong)((__arm64_load_address_13496304) + (0x40UL)));
        return x0;
        label_0xCDEFF8:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB7CUL, x0, x1, x2, x3);
        goto label_0xCDEFFC;
        label_0xCDEFFC:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `GraphicsUtils.Blit` — RVA `0xcdf000`

- Lift status: **exact**; input span: 252 bytes; span to next metadata RVA: 252 bytes.
- Metadata signature: `public static void Blit(Material material, int pass) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=40 (informational only).

```csharp
public static ulong GraphicsUtils_Blit_RVAcdf000(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_load_address_13496560 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteF64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        sp = unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL)));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x8UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        x20 = x0;
        x0 = 0x0UL;
        x19 = unchecked((ulong)(unchecked((uint)(x1))));
        x0 = RuntimeCalls.InvokeDirect(0x1778B44UL /* metadata target: GL.PushMatrix */, x0, x1, x2, x3);
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1778BBCUL /* metadata target: GL.LoadOrtho */, x0, x1, x2, x3);
        if ((x20 == 0x0UL))
        {
            goto label_0xCDF0F8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x20;
        x1 = unchecked((ulong)(unchecked((uint)(x19))));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177AF98UL /* metadata target: Material.SetPass */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = unchecked((ulong)(unchecked((uint)(0x5UL))));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1778D0CUL /* metadata target: GL.Begin */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17788ECUL /* metadata target: GL.TexCoord2 */, x0, x1, x2, x3);
        x8 = 0x432000UL;
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x3B8UL))))), 0));
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177884CUL /* metadata target: GL.Vertex3 */, x0, x1, x2, x3);
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17788ECUL /* metadata target: GL.TexCoord2 */, x0, x1, x2, x3);
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177884CUL /* metadata target: GL.Vertex3 */, x0, x1, x2, x3);
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17788ECUL /* metadata target: GL.TexCoord2 */, x0, x1, x2, x3);
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177884CUL /* metadata target: GL.Vertex3 */, x0, x1, x2, x3);
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17788ECUL /* metadata target: GL.TexCoord2 */, x0, x1, x2, x3);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        v2 = v8;
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177884CUL /* metadata target: GL.Vertex3 */, x0, x1, x2, x3);
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1778D48UL /* metadata target: GL.End */, x0, x1, x2, x3);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        x0 = 0x0UL;
        __arm64_load_address_13496560 = sp;
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_load_address_13496560)), 0));
        sp = unchecked((ulong)((__arm64_load_address_13496560) + (0x20UL)));
        return RuntimeCalls.InvokeDirect(0x1778B6CUL /* metadata target: GL.PopMatrix */);
        label_0xCDF0F8:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `GraphicsUtils.ClearAndBlit` — RVA `0xcdf0fc`

- Lift status: **exact**; input span: 408 bytes; span to next metadata RVA: 408 bytes.
- Metadata signature: `public static void ClearAndBlit(Texture source, RenderTexture destination, Material material, int pass, bool clearColor = true, bool clearDepth = false) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=68 (informational only).

```csharp
public static ulong GraphicsUtils_ClearAndBlit_RVAcdf0fc(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_load_address_13496968 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x22 = default(ulong);
        ulong x23 = default(ulong);
        ulong x24 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteF64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFC0UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        sp = unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFC0UL)));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x8UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x24);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))), x19);
        x19 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x626UL))))))));
        x23 = unchecked((ulong)(unchecked((uint)(x4))));
        x20 = unchecked((ulong)(unchecked((uint)(x3))));
        x21 = x2;
        x24 = x1;
        x22 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCDF144;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD10UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x626UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCDF144;
        label_0xCDF144:
        ;
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x178223CUL /* metadata target: RenderTexture.get_active */, x0, x1, x2, x3);
        x19 = x0;
        x0 = x24;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1782264UL /* metadata target: RenderTexture.set_active */, x0, x1, x2, x3);
        x1 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x23))) & (unchecked((uint)(0x1UL)))))));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1778E4CUL /* metadata target: GL.Clear */, unchecked((ulong)(unchecked((uint)(x0)))), unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1778B44UL /* metadata target: GL.PushMatrix */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1778BBCUL /* metadata target: GL.LoadOrtho */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        if ((x21 == 0x0UL))
        {
            goto label_0xCDF290;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xD10UL))));
        x0 = x21;
        x2 = x22;
        x3 = 0x0UL;
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x177AA8CUL /* metadata target: Material.SetTexture */, x0, x1, x2, x3);
        x0 = x21;
        x1 = unchecked((ulong)(unchecked((uint)(x20))));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177AF98UL /* metadata target: Material.SetPass */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = unchecked((ulong)(unchecked((uint)(0x5UL))));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1778D0CUL /* metadata target: GL.Begin */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17788ECUL /* metadata target: GL.TexCoord2 */, x0, x1, x2, x3);
        x8 = 0x432000UL;
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x3B8UL))))), 0));
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177884CUL /* metadata target: GL.Vertex3 */, x0, x1, x2, x3);
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17788ECUL /* metadata target: GL.TexCoord2 */, x0, x1, x2, x3);
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177884CUL /* metadata target: GL.Vertex3 */, x0, x1, x2, x3);
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17788ECUL /* metadata target: GL.TexCoord2 */, x0, x1, x2, x3);
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177884CUL /* metadata target: GL.Vertex3 */, x0, x1, x2, x3);
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17788ECUL /* metadata target: GL.TexCoord2 */, x0, x1, x2, x3);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        v2 = v8;
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177884CUL /* metadata target: GL.Vertex3 */, x0, x1, x2, x3);
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1778D48UL /* metadata target: GL.End */, x0, x1, x2, x3);
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1778B6CUL /* metadata target: GL.PopMatrix */, x0, x1, x2, x3);
        x0 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        x1 = 0x0UL;
        __arm64_load_address_13496968 = sp;
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_load_address_13496968)), 0));
        sp = unchecked((ulong)((__arm64_load_address_13496968) + (0x40UL)));
        return RuntimeCalls.InvokeDirect(0x1782264UL /* metadata target: RenderTexture.set_active */);
        label_0xCDF290:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `GraphicsUtils.Destroy` — RVA `0xcdf294`

- Lift status: **exact**; input span: 136 bytes; span to next metadata RVA: 136 bytes.
- Metadata signature: `public static void Destroy(Object obj) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=21 (informational only).

```csharp
public static ulong GraphicsUtils_Destroy_RVAcdf294(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
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
        x21 = 0x1BAB000UL;
        x20 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x627UL))))))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xD8UL))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCDF2C8;
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
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x627UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCDF2C8;
        label_0xCDF2C8:
        ;
        x0 = RuntimeMemory.ReadU64(x20);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCDF2D8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCDF2D4UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCDF2D8;
        label_0xCDF2D8:
        ;
        x0 = x19;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794AC8UL /* metadata target: Object.op_Inequality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCDF310;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(x20);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCDF2FC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCDF2F8UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCDF2FC;
        label_0xCDF2FC:
        ;
        x0 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x1 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeDirect(0x1798A20UL /* metadata target: Object.Destroy */);
        label_0xCDF310:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return x0;
        return default(ulong);
    }
```

## `GraphicsUtils.Dispose` — RVA `0xcdf31c`

- Lift status: **exact**; input span: 72 bytes; span to next metadata RVA: 72 bytes.
- Metadata signature: `public static void Dispose() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=12 (informational only).

```csharp
public static ulong GraphicsUtils_Dispose_RVAcdf31c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        x19 = 0x1BAB000UL;
        x20 = 0x1A8F000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x628UL))))))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x868UL))));
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCDF34C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x868UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x628UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCDF34C;
        label_0xCDF34C:
        ;
        x8 = RuntimeMemory.ReadU64(x20);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0xCDF294UL /* metadata target: GraphicsUtils.Destroy */);
        return default(ulong);
    }
```
