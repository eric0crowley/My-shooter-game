# `BuiltinDebugViewsComponent.Uniforms` — TypeDefIndex 3507

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## `BuiltinDebugViewsComponent.Uniforms.cctor` — RVA `0xcd04ac`

- Lift status: **exact**; input span: 392 bytes; span to next metadata RVA: 392 bytes.
- Metadata signature: `private static void .cctor() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=68 (informational only).

```csharp
public static ulong BuiltinDebugViewsComponent_Uniforms_cctor_RVAcd04ac(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
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
        x26 = 0x1BAB000UL;
        x27 = 0x1A8E000UL;
        x19 = 0x1A8E000UL;
        x25 = 0x1A8E000UL;
        x24 = 0x1A8E000UL;
        x23 = 0x1A8E000UL;
        x22 = 0x1A8E000UL;
        x21 = 0x1A8E000UL;
        x20 = 0x1A8E000UL;
        x27 = RuntimeMemory.ReadU64(unchecked((ulong)((x27) + (0xE30UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xDD8UL))));
        x25 = RuntimeMemory.ReadU64(unchecked((ulong)((x25) + (0xD18UL))));
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x26) + (0x5B0UL))))))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((x24) + (0xE38UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0xD10UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0xE40UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xE48UL))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xE50UL))));
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
        }
        else
        {
            x0 = 0x1A8E000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xDD8UL))));
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x0 = 0x1A8E000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xE30UL))));
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x0 = 0x1A8E000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD10UL))));
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x0 = 0x1A8E000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xE38UL))));
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x0 = 0x1A8E000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD18UL))));
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x0 = 0x1A8E000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xE50UL))));
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x0 = 0x1A8E000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xE40UL))));
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x0 = 0x1A8E000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xE48UL))));
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
            RuntimeMemory.WriteU8(unchecked((ulong)((x26) + (0x5B0UL))), unchecked((byte)(unchecked((uint)(x8)))));
        }
        label_0xCD0574:
        ;
        x0 = RuntimeMemory.ReadU64(x27);
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177A220UL /* metadata target: Shader.PropertyToID */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x19);
        x1 = 0x0UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        RuntimeMemory.WriteU32(x8, unchecked((uint)(x0)));
        x0 = RuntimeMemory.ReadU64(x25);
        x0 = RuntimeCalls.InvokeDirect(0x177A220UL /* metadata target: Shader.PropertyToID */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x19);
        x1 = 0x0UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x8) + (0x4UL))), unchecked((uint)(x0)));
        x0 = RuntimeMemory.ReadU64(x24);
        x0 = RuntimeCalls.InvokeDirect(0x177A220UL /* metadata target: Shader.PropertyToID */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x19);
        x1 = 0x0UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x8) + (0x8UL))), unchecked((uint)(x0)));
        x0 = RuntimeMemory.ReadU64(x23);
        x0 = RuntimeCalls.InvokeDirect(0x177A220UL /* metadata target: Shader.PropertyToID */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x19);
        x1 = 0x0UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x8) + (0xCUL))), unchecked((uint)(x0)));
        x0 = RuntimeMemory.ReadU64(x22);
        x0 = RuntimeCalls.InvokeDirect(0x177A220UL /* metadata target: Shader.PropertyToID */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x19);
        x1 = 0x0UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x8) + (0x10UL))), unchecked((uint)(x0)));
        x0 = RuntimeMemory.ReadU64(x21);
        x0 = RuntimeCalls.InvokeDirect(0x177A220UL /* metadata target: Shader.PropertyToID */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x19);
        x1 = 0x0UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x8) + (0x14UL))), unchecked((uint)(x0)));
        x0 = RuntimeMemory.ReadU64(x20);
        x0 = RuntimeCalls.InvokeDirect(0x177A220UL /* metadata target: Shader.PropertyToID */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x19);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x40UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x26 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x25 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x8) + (0x18UL))), unchecked((uint)(x0)));
        x30 = RuntimeMemory.ReadU64(sp);
        x27 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return x0;
        return default(ulong);
    }
```
