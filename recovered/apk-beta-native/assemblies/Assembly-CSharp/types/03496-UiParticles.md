# `UiParticles` — TypeDefIndex 3496

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0xD8` | `ParticleSystem` | `m_ParticleSystem` |
| `0xE0` | `UiParticleRenderMode` | `m_RenderMode` |
| `0xE4` | `float` | `m_StretchedSpeedScale` |
| `0xE8` | `float` | `m_StretchedLenghScale` |
| `0xEC` | `bool` | `m_IgnoreTimescale` |
| `0xF0` | `ParticleSystemRenderer` | `m_ParticleSystemRenderer` |
| `0xF8` | `ParticleSystem.Particle[]` | `m_Particles` |

## `UiParticles.get_ParticleSystem` — RVA `0xccc604`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public ParticleSystem get_ParticleSystem() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static ulong UiParticles_get_ParticleSystem_RVAccc604(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD8UL))));
        return x0;
        return default(ulong);
    }
```

## `UiParticles.set_ParticleSystem` — RVA `0xccc60c`

- Lift status: **exact**; input span: 128 bytes; span to next metadata RVA: 128 bytes.
- Metadata signature: `public void set_ParticleSystem(ParticleSystem value) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=22 (informational only).

```csharp
public static ulong UiParticles_set_ParticleSystem_RVAccc60c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
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
        x21 = 0x1A8E000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x22) + (0x592UL))))))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xC58UL))));
        x20 = x1;
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCCC648;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xC58UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x22) + (0x592UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCCC648;
        label_0xCCC648:
        ;
        x2 = RuntimeMemory.ReadU64(x21);
        x0 = unchecked((ulong)((x19) + (0xD8UL)));
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xD398ECUL, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCCC67C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x19);
        x0 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x2D8UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x2E0UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeIndirect(x2);
        label_0xCCC67C:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        return default(ulong);
    }
```

## `UiParticles.get_mainTexture` — RVA `0xccc68c`

- Lift status: **exact**; input span: 296 bytes; span to next metadata RVA: 296 bytes.
- Metadata signature: `public override Texture get_mainTexture() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=49 (informational only).

```csharp
public static ulong UiParticles_get_mainTexture_RVAccc68c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
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
        x20 = 0x1BAB000UL;
        x21 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x593UL))))))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xD8UL))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCCC6CC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xE68UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x593UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCCC6CC;
        label_0xCCC6CC:
        ;
        x8 = RuntimeMemory.ReadU64(x19);
        x0 = x19;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x338UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x340UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x21);
        x20 = x0;
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCCC6F8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCCC6F8;
        label_0xCCC6F8:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794AC8UL /* metadata target: Object.op_Inequality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCCC780;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x19);
        x0 = x19;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x338UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x340UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCCC7B0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177A80CUL /* metadata target: Material.get_mainTexture */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x21);
        x20 = x0;
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCCC744;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCCC744;
        label_0xCCC744:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794AC8UL /* metadata target: Object.op_Inequality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCCC780;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x19);
        x0 = x19;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x338UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x340UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCCC7B0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x1 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeDirect(0x177A80CUL /* metadata target: Material.get_mainTexture */);
        label_0xCCC780:
        ;
        x19 = 0x1A8C000UL;
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xE68UL))));
        x0 = RuntimeMemory.ReadU64(x19);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCCC79C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCCC794UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x19);
        goto label_0xCCC79C;
        label_0xCCC79C:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB8UL))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return x0;
        label_0xCCC7B0:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `UiParticles.get_RenderMode` — RVA `0xccc7b4`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public UiParticleRenderMode get_RenderMode() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static uint UiParticles_get_RenderMode_RVAccc7b4(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x0 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        return unchecked((uint)(x0));
        return default(uint);
    }
```

## `UiParticles.set_RenderMode` — RVA `0xccc7bc`

- Lift status: **exact**; input span: 128 bytes; span to next metadata RVA: 128 bytes.
- Metadata signature: `public void set_RenderMode(UiParticleRenderMode value) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=22 (informational only).

```csharp
public static ulong UiParticles_set_RenderMode_RVAccc7bc(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
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
        x21 = 0x1A8E000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x22) + (0x594UL))))))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xC60UL))));
        x20 = unchecked((ulong)(unchecked((uint)(x1))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCCC7F8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xC60UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x22) + (0x594UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCCC7F8;
        label_0xCCC7F8:
        ;
        x2 = RuntimeMemory.ReadU64(x21);
        x0 = unchecked((ulong)((x19) + (0xE0UL)));
        x1 = unchecked((ulong)(unchecked((uint)(x20))));
        x0 = RuntimeCalls.InvokeDirect(0xD39948UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCCC82C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x19);
        x0 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x2D8UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x2E0UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeIndirect(x2);
        label_0xCCC82C:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        return default(ulong);
    }
```

## `UiParticles.Awake` — RVA `0xccc83c`

- Lift status: **exact**; input span: 304 bytes; span to next metadata RVA: 304 bytes.
- Metadata signature: `protected override void Awake() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=47 (informational only).

```csharp
public static ulong UiParticles_Awake_RVAccc83c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13420832 = default(uint);
        uint __arm64_flags_right_13420832 = default(uint);
        ulong sp = default(ulong);
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
        x23 = 0x1A8E000UL;
        x20 = 0x1A8E000UL;
        x21 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x22) + (0x595UL))))))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0xA8UL))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xC68UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xD8UL))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCCC89C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xC68UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xA8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x22) + (0x595UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCCC89C;
        label_0xCCC89C:
        ;
        x1 = RuntimeMemory.ReadU64(x23);
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xE31BC8UL, x0, x1, x2, x3);
        x1 = RuntimeMemory.ReadU64(x20);
        x20 = x0;
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xE31BC8UL, x0, x1, x2, x3);
        x22 = x19;
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x20UL))));
        x8 = RuntimeMemory.ReadU64(x21);
        x21 = x0;
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCCC8D8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCCC8D8;
        label_0xCCC8D8:
        ;
        x0 = x23;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179568CUL /* metadata target: Object.op_Equality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCCC910;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCCC8ECUL);
        }
        if ((x21 == 0x0UL))
        {
            goto label_0xCCC968;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x21;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1779C08UL /* metadata target: Renderer.get_sharedMaterial */, x0, x1, x2, x3);
        x1 = x0;
        RuntimeMemory.WriteU64(x22, x0);
        x0 = x22;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        goto label_0xCCC914;
        label_0xCCC910:
        ;
        if ((x21 == 0x0UL))
        {
            goto label_0xCCC968;
        }
        else
        {
            goto label_0xCCC914;
        }
        label_0xCCC914:
        ;
        x0 = x21;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17CA864UL /* metadata target: ParticleSystemRenderer.get_renderMode */, x0, x1, x2, x3);
        __arm64_flags_left_13420832 = unchecked((uint)(x0));
        __arm64_flags_right_13420832 = unchecked((uint)0x1UL);
        if ((!((unchecked((uint)((__arm64_flags_left_13420832) - (__arm64_flags_right_13420832))) == unchecked((uint)0x0UL)))))
        {
            goto label_0xCCC934;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xCCC7BCUL /* metadata target: UiParticles.set_RenderMode */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xCCC934;
        label_0xCCC934:
        ;
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x19A78D4UL /* metadata target: UIBehaviour.Awake */, x0, x1, x2, x3);
        x0 = x19;
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xCCC60CUL /* metadata target: UiParticles.set_ParticleSystem */, x0, x1, x2, x3);
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0xF0UL))), x21);
        x0 = x19;
        x1 = x21;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeDirect(0xB7D8D0UL);
        label_0xCCC968:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `UiParticles.SetMaterialDirty` — RVA `0xccc96c`

- Lift status: **exact**; input span: 148 bytes; span to next metadata RVA: 148 bytes.
- Metadata signature: `public override void SetMaterialDirty() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=23 (informational only).

```csharp
public static ulong UiParticles_SetMaterialDirty_RVAccc96c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
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
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x596UL))))))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xD8UL))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCCC9A0;
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
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x596UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCCC9A0;
        label_0xCCC9A0:
        ;
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x181BED4UL /* metadata target: Graphic.SetMaterialDirty */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x20);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xF0UL))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCCC9C0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCCC9BCUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCCC9C0;
        label_0xCCC9C0:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794AC8UL /* metadata target: Object.op_Inequality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCCC9F0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xF0UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCCC9FC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x20UL))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x2 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeDirect(0x1779C44UL /* metadata target: Renderer.set_sharedMaterial */);
        label_0xCCC9F0:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return x0;
        label_0xCCC9FC:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `UiParticles.OnPopulateMesh` — RVA `0xccca00`

- Lift status: **exact**; input span: 152 bytes; span to next metadata RVA: 152 bytes.
- Metadata signature: `protected override void OnPopulateMesh(VertexHelper toFill) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=26 (informational only).

```csharp
public static ulong UiParticles_OnPopulateMesh_RVAccca00(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
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
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x22) + (0x597UL))))))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xD8UL))));
        x19 = x1;
        x20 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCCCA3C;
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
        RuntimeMemory.WriteU8(unchecked((ulong)((x22) + (0x597UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCCCA3C;
        label_0xCCCA3C:
        ;
        x0 = RuntimeMemory.ReadU64(x21);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xD8UL))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCCCA50;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCCCA4CUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCCCA50;
        label_0xCCCA50:
        ;
        x0 = x21;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179568CUL /* metadata target: Object.op_Equality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCCCA80;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x20;
        x1 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x2 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0x181DC74UL /* metadata target: Graphic.OnPopulateMesh */);
        label_0xCCCA80:
        ;
        x0 = x20;
        x1 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0xCCCA98UL /* metadata target: UiParticles.GenerateParticlesBillboards */);
        return default(ulong);
    }
```

## `UiParticles.GenerateParticlesBillboards` — RVA `0xccca98`

- Lift status: **partial**; input span: 184 bytes; span to next metadata RVA: 184 bytes.
- Metadata signature: `private void GenerateParticlesBillboards(VertexHelper vh) { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=26 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'b.ne' at 0xcccb30; reason: Unknown IR expression at 0xcccb30

```csharp
public static ulong UiParticles_GenerateParticlesBillboards_RVAccca98(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13421276 = default(uint);
        ulong __arm64_flags_left_13421308 = default(ulong);
        ulong __arm64_flags_left_13421352 = default(ulong);
        uint __arm64_flags_right_13421276 = default(uint);
        ulong __arm64_flags_right_13421308 = default(ulong);
        ulong __arm64_flags_right_13421352 = default(ulong);
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x22 = default(ulong);
        ulong x23 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        sp = unchecked((ulong)((sp) - (0xC0UL)));
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x90UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x90UL)))) + (0x8UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xA0UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xA0UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xB0UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xB0UL)))) + (0x8UL))), x19);
        x19 = x1;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xCCCC7CUL /* metadata target: UiParticles.InitParticlesBuffer */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xD8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCCCB48;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xF8UL))));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17C99D8UL /* metadata target: ParticleSystem.GetParticles */, x0, x1, x2, x3);
        if ((x19 == 0x0UL))
        {
            goto label_0xCCCB48;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x21 = unchecked((ulong)(unchecked((uint)(x0))));
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x198544CUL /* metadata target: VertexHelper.Clear */, x0, x1, x2, x3);
        __arm64_flags_left_13421276 = unchecked((uint)(x21));
        __arm64_flags_right_13421276 = unchecked((uint)0x1UL);
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13421276) - (__arm64_flags_right_13421276))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_13421276)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13421276)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13421276) - (__arm64_flags_right_13421276))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13421276)) < unchecked((int)0x0UL))))))
        {
            goto label_0xCCCB34;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x22 = 0x0UL;
        x21 = unchecked((ulong)(unchecked((uint)(x21))));
        x23 = unchecked((ulong)(unchecked((uint)(0x20UL))));
        goto label_0xCCCAF0;
        label_0xCCCAF0:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xF8UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCCCB48;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_13421308 = x22;
        __arm64_flags_right_13421308 = x9;
        if ((__arm64_flags_left_13421308 >= __arm64_flags_right_13421308))
        {
            goto label_0xCCCB4C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)((x8) + (unchecked((ulong)(unchecked((uint)(x23)))))));
        x0 = unchecked((ulong)((sp) + (0x8UL)));
        x2 = unchecked((ulong)(unchecked((uint)(0x84UL))));
        x0 = RuntimeCalls.InvokeDirect(0x19B0CD0UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x1 = unchecked((ulong)((sp) + (0x8UL)));
        x0 = x20;
        x2 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xCCCD44UL /* metadata target: UiParticles.DrawParticleBillboard */, x0, x1, x2, x3);
        x22 = unchecked((ulong)((x22) + (0x1UL)));
        __arm64_flags_left_13421352 = x21;
        __arm64_flags_right_13421352 = x22;
        x23 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x23))) + (unchecked((uint)(0x84UL)))))));
        RuntimeCalls.Unsupported("b.ne", 0xCCCB30UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xCCCAF0;
        }
        else
        {
            goto label_0xCCCB34;
        }
        label_0xCCCB34:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0xB0UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xB0UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0xA0UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xA0UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x90UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x90UL)))) + (0x8UL))));
        sp = unchecked((ulong)((sp) + (0xC0UL)));
        return x0;
        label_0xCCCB48:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        goto label_0xCCCB4C;
        label_0xCCCB4C:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB7CUL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `UiParticles.Update` — RVA `0xcccb50`

- Lift status: **exact**; input span: 300 bytes; span to next metadata RVA: 300 bytes.
- Metadata signature: `protected virtual void Update() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=44 (informational only).

```csharp
public static ulong UiParticles_Update_RVAcccb50(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
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
        x20 = 0x1BAB000UL;
        x21 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x598UL))))))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xD8UL))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCCCB88;
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
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x598UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCCCB88;
        label_0xCCCB88:
        ;
        x0 = RuntimeMemory.ReadU64(x21);
        x22 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0xECUL))))))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xD8UL))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCCCBA0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCCCB9CUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCCCBA0;
        label_0xCCCBA0:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794AC8UL /* metadata target: Object.op_Inequality */, x0, x1, x2, x3);
        if ((unchecked((uint)(x22)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCCCBE0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCCCBB4UL);
        }
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCCCC0C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xD8UL))));
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179ADA8UL /* metadata target: Time.get_unscaledDeltaTime */, x0, x1, x2, x3);
        if ((x20 == 0x0UL))
        {
            goto label_0xCCCC78;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = x20;
        x2 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x3 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17C9A90UL /* metadata target: ParticleSystem.Simulate */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xCCCBF8;
        label_0xCCCBE0:
        ;
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCCCC0C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xD8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCCCC78;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17C9690UL /* metadata target: ParticleSystem.get_isPlaying */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCCCC0C;
        }
        else
        {
            goto label_0xCCCBF8;
        }
        label_0xCCCBF8:
        ;
        x8 = RuntimeMemory.ReadU64(x19);
        x0 = x19;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x2F8UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x300UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xCCCC0C;
        label_0xCCCC0C:
        ;
        x0 = RuntimeMemory.ReadU64(x21);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xF0UL))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCCCC20;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCCCC1CUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xCCCC20;
        label_0xCCCC20:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794AC8UL /* metadata target: Object.op_Inequality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCCCC68;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xF0UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCCCC78;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1779994UL /* metadata target: Renderer.get_enabled */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCCCC68;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xF0UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCCCC78;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x2 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0x17799D0UL /* metadata target: Renderer.set_enabled */);
        label_0xCCCC68:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        label_0xCCCC78:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        return default(ulong);
    }
```

## `UiParticles.InitParticlesBuffer` — RVA `0xcccc7c`

- Lift status: **exact**; input span: 200 bytes; span to next metadata RVA: 200 bytes.
- Metadata signature: `private void InitParticlesBuffer() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=28 (informational only).

```csharp
public static ulong UiParticles_InitParticlesBuffer_RVAcccc7c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13421792 = default(uint);
        uint __arm64_flags_right_13421792 = default(uint);
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        sp = unchecked((ulong)((sp) - (0x30UL)));
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x19);
        x19 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x599UL))))))));
        x20 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCCCCAC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xA0UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x599UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCCCCAC;
        label_0xCCCCAC:
        ;
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0x8UL))), 0x0UL);
        x19 = x20;
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xF8UL))));
        if ((x21 == 0x0UL))
        {
            goto label_0xCCCCE8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xD8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCCCD40;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17C9580UL /* metadata target: ParticleSystem.get_main */, x0, x1, x2, x3);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x8UL))), x0);
        x0 = unchecked((ulong)((sp) + (0x8UL)));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17C9ED8UL /* metadata target: ParticleSystem.MainModule.get_maxParticles */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x21) + (0x18UL))))));
        __arm64_flags_left_13421792 = unchecked((uint)(x0));
        __arm64_flags_right_13421792 = unchecked((uint)(x8));
        if (((unchecked((uint)((__arm64_flags_left_13421792) - (__arm64_flags_right_13421792))) == unchecked((uint)0x0UL)) || ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13421792) - (__arm64_flags_right_13421792))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_13421792)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13421792)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13421792) - (__arm64_flags_right_13421792))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13421792)) < unchecked((int)0x0UL)))))))
        {
            goto label_0xCCCD30;
        }
        else
        {
            goto label_0xCCCCE8;
        }
        label_0xCCCCE8:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xD8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCCCD40;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = 0x1A8E000UL;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xA0UL))));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17C9580UL /* metadata target: ParticleSystem.get_main */, x0, x1, x2, x3);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x8UL))), x0);
        x0 = unchecked((ulong)((sp) + (0x8UL)));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17C9ED8UL /* metadata target: ParticleSystem.MainModule.get_maxParticles */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x20);
        x1 = unchecked((ulong)(unchecked((uint)(x0))));
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0xB7D9D4UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x1 = x0;
        RuntimeMemory.WriteU64(x19, x0);
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        goto label_0xCCCD30;
        label_0xCCCD30:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        return x0;
        label_0xCCCD40:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `UiParticles.DrawParticleBillboard` — RVA `0xcccd44`

- Lift status: **exact**; input span: 1160 bytes; span to next metadata RVA: 1160 bytes.
- Metadata signature: `private void DrawParticleBillboard(ParticleSystem.Particle particle, VertexHelper vh) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=178 (informational only).

```csharp
public static ulong UiParticles_DrawParticleBillboard_RVAcccd44(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13422104 = default(uint);
        uint __arm64_flags_left_13422256 = default(uint);
        uint __arm64_flags_left_13422776 = default(uint);
        uint __arm64_flags_left_13422836 = default(uint);
        uint __arm64_flags_left_13422896 = default(uint);
        uint __arm64_flags_right_13422104 = default(uint);
        uint __arm64_flags_right_13422256 = default(uint);
        uint __arm64_flags_right_13422776 = default(uint);
        uint __arm64_flags_right_13422836 = default(uint);
        uint __arm64_flags_right_13422896 = default(uint);
        ulong __arm64_pair_address_13421896 = default(ulong);
        ulong __arm64_pair_address_13421900 = default(ulong);
        ulong __arm64_pair_address_13421904 = default(ulong);
        ulong __arm64_pair_address_13421908 = default(ulong);
        ulong __arm64_pair_address_13422248 = default(ulong);
        ulong __arm64_pair_address_13422392 = default(ulong);
        ulong __arm64_pair_address_13422436 = default(ulong);
        ulong __arm64_pair_address_13422656 = default(ulong);
        ulong __arm64_pair_address_13422728 = default(ulong);
        ulong __arm64_pair_address_13422784 = default(ulong);
        ulong __arm64_pair_address_13422792 = default(ulong);
        ulong __arm64_pair_address_13422844 = default(ulong);
        ulong __arm64_pair_address_13422852 = default(ulong);
        ulong __arm64_pair_address_13422908 = default(ulong);
        ulong __arm64_pair_address_13423020 = default(ulong);
        ulong __arm64_pair_address_13423024 = default(ulong);
        ulong __arm64_pair_address_13423028 = default(ulong);
        ulong __arm64_pair_address_13423032 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v10 = default(RuntimeVector128);
        RuntimeVector128 v11 = default(RuntimeVector128);
        RuntimeVector128 v12 = default(RuntimeVector128);
        RuntimeVector128 v13 = default(RuntimeVector128);
        RuntimeVector128 v14 = default(RuntimeVector128);
        RuntimeVector128 v15 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
        RuntimeVector128 v4 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        RuntimeVector128 v9 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x22 = default(ulong);
        ulong x23 = default(ulong);
        ulong x24 = default(ulong);
        ulong x29 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        sp = unchecked((ulong)((sp) - (0x1F0UL)));
        __arm64_pair_address_13421896 = unchecked((ulong)((sp) + (0x170UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13421896, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v15.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13421896) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v14.GetUInt64(0)))));
        __arm64_pair_address_13421900 = unchecked((ulong)((sp) + (0x180UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13421900, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v13.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13421900) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v12.GetUInt64(0)))));
        __arm64_pair_address_13421904 = unchecked((ulong)((sp) + (0x190UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13421904, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v11.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13421904) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v10.GetUInt64(0)))));
        __arm64_pair_address_13421908 = unchecked((ulong)((sp) + (0x1A0UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13421908, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13421908) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x1B0UL)))) + (0x0UL))), x29);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x1B0UL)))) + (0x8UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x1C0UL)))) + (0x0UL))), x24);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x1C0UL)))) + (0x8UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x1D0UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x1D0UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x1E0UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x1E0UL)))) + (0x8UL))), x19);
        x22 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x22) + (0x59AUL))))))));
        x19 = x2;
        x21 = x1;
        x20 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCCCD94;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xC70UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x22) + (0x59AUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCCCD94;
        label_0xCCCD94:
        ;
        x0 = x21;
        x1 = 0x0UL;
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0x140UL))), 0x0UL);
        x0 = RuntimeCalls.InvokeDirect(0x17CA430UL /* metadata target: ParticleSystem.Particle.get_position */, x0, x1, x2, x3);
        x0 = x21;
        x1 = 0x0UL;
        v8 = v0;
        v9 = v1;
        v10 = v2;
        x0 = RuntimeCalls.InvokeDirect(0x17CA460UL /* metadata target: ParticleSystem.Particle.get_rotation3D */, x0, x1, x2, x3);
        x8 = 0x432000UL;
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x3E4UL))))), 0));
        x0 = 0x0UL;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0))))), 0));
        x0 = RuntimeCalls.InvokeDirect(0x178B12CUL /* metadata target: Quaternion.Internal_FromEulerRad */, x0, x1, x2, x3);
        RuntimeMemory.WriteF32(unchecked((ulong)((sp) + (0x160UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((sp) + (0x164UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((sp) + (0x168UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((sp) + (0x16CUL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xD8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCCD1C4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        v12 = v0;
        v13 = v1;
        v14 = v2;
        v15 = v3;
        x0 = RuntimeCalls.InvokeDirect(0x17C9580UL /* metadata target: ParticleSystem.get_main */, x0, x1, x2, x3);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x148UL))), x0);
        x0 = unchecked((ulong)((sp) + (0x148UL)));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17C9E60UL /* metadata target: ParticleSystem.MainModule.get_simulationSpace */, x0, x1, x2, x3);
        __arm64_flags_left_13422104 = unchecked((uint)(x0));
        __arm64_flags_right_13422104 = unchecked((uint)0x1UL);
        if ((!((unchecked((uint)((__arm64_flags_left_13422104) - (__arm64_flags_right_13422104))) == unchecked((uint)0x0UL)))))
        {
            goto label_0xCCCE54;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x181BDD4UL /* metadata target: Graphic.get_rectTransform */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCCD1C4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        v0 = v8;
        v1 = v9;
        v2 = v10;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179E940UL /* metadata target: Transform.InverseTransformPoint */, x0, x1, x2, x3);
        v9 = v1;
        v10 = v2;
        RuntimeMemory.WriteF32(unchecked((ulong)((sp) + (0x20UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        goto label_0xCCCE58;
        label_0xCCCE54:
        ;
        RuntimeMemory.WriteF32(unchecked((ulong)((sp) + (0x20UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0));
        goto label_0xCCCE58;
        label_0xCCCE58:
        ;
        x0 = x21;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17CA450UL /* metadata target: ParticleSystem.Particle.get_startLifetime */, x0, x1, x2, x3);
        x0 = x21;
        x1 = 0x0UL;
        v11 = v0;
        x0 = RuntimeCalls.InvokeDirect(0x17CA448UL /* metadata target: ParticleSystem.Particle.get_remainingLifetime */, x0, x1, x2, x3);
        x0 = x21;
        x1 = 0x0UL;
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        x0 = RuntimeCalls.InvokeDirect(0x17CA450UL /* metadata target: ParticleSystem.Particle.get_startLifetime */, x0, x1, x2, x3);
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xD8UL))));
        x0 = x21;
        x2 = 0x0UL;
        v11 = v0;
        x0 = RuntimeCalls.InvokeDirect(0x17CA480UL /* metadata target: ParticleSystem.Particle.GetCurrentSize3D */, x0, x1, x2, x3);
        RuntimeMemory.WriteF32(unchecked((ulong)((sp) + (0x150UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((sp) + (0x154UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((sp) + (0x158UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x20) + (0xE0UL))))));
        __arm64_pair_address_13422248 = unchecked((ulong)((sp) + (0x24UL)));
        RuntimeMemory.WriteF32(__arm64_pair_address_13422248, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_13422248) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((sp) + (0x2CUL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0));
        __arm64_flags_left_13422256 = unchecked((uint)(x8));
        __arm64_flags_right_13422256 = unchecked((uint)0x1UL);
        if ((!((unchecked((uint)((__arm64_flags_left_13422256) - (__arm64_flags_right_13422256))) == unchecked((uint)0x0UL)))))
        {
            goto label_0xCCCEFC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = unchecked((ulong)((sp) + (0xB8UL)));
        x2 = unchecked((ulong)(unchecked((uint)(0x84UL))));
        x1 = x21;
        x0 = RuntimeCalls.InvokeDirect(0x19B0C40UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x1 = unchecked((ulong)((sp) + (0xB8UL)));
        x2 = unchecked((ulong)((sp) + (0x150UL)));
        x3 = unchecked((ulong)((sp) + (0x160UL)));
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xCCD1CCUL /* metadata target: UiParticles.GetStrechedBillboardsSizeAndRotation */, x0, x1, x2, x3);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((sp) + (0x150UL))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((sp) + (0x154UL))))), 0));
        v12 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((sp) + (0x160UL))))), 0));
        v13 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((sp) + (0x164UL))))), 0));
        v14 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((sp) + (0x168UL))))), 0));
        v15 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((sp) + (0x16CUL))))), 0));
        goto label_0xCCCEFC;
        label_0xCCCEFC:
        ;
        v0 = v12;
        v1 = v13;
        v2 = v14;
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x178B504UL /* metadata target: Quaternion.op_Multiply */, x0, x1, x2, x3);
        __arm64_pair_address_13422392 = unchecked((ulong)((sp) + (0x18UL)));
        RuntimeMemory.WriteF32(__arm64_pair_address_13422392, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_13422392) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((sp) + (0x14UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0));
        v0 = v12;
        v1 = v13;
        v2 = v14;
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x178B504UL /* metadata target: Quaternion.op_Multiply */, x0, x1, x2, x3);
        __arm64_pair_address_13422436 = unchecked((ulong)((sp) + (0xCUL)));
        RuntimeMemory.WriteF32(__arm64_pair_address_13422436, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_13422436) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((sp) + (0x8UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0));
        v0 = v12;
        v1 = v13;
        v2 = v14;
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x178B504UL /* metadata target: Quaternion.op_Multiply */, x0, x1, x2, x3);
        v8 = v0;
        v9 = v1;
        RuntimeMemory.WriteF32(unchecked((ulong)((sp) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0));
        v0 = v12;
        v1 = v13;
        v2 = v14;
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x178B504UL /* metadata target: Quaternion.op_Multiply */, x0, x1, x2, x3);
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xD8UL))));
        x0 = x21;
        x2 = 0x0UL;
        v14 = v0;
        v12 = v1;
        v13 = v2;
        x0 = RuntimeCalls.InvokeDirect(0x17CA49CUL /* metadata target: ParticleSystem.Particle.GetCurrentColor */, x0, x1, x2, x3);
        if ((x19 == 0x0UL))
        {
            goto label_0xCCD1C4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCCCFE0UL);
        }
        RuntimeMemory.WriteF32(sp, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0));
        x22 = 0x1A8E000UL;
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0xC70UL))));
        x24 = x0;
        x0 = x19;
        x1 = 0x0UL;
        v15 = v9;
        x0 = RuntimeCalls.InvokeDirect(0x1995B18UL /* metadata target: VertexHelper.get_currentVertCount */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x22);
        x22 = unchecked((ulong)(unchecked((uint)(x0))));
        x1 = unchecked((ulong)(unchecked((uint)(0x4UL))));
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0xB7D9D4UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xD8UL))));
        v11 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((sp) + (0x2CUL))))), 0));
        if ((x8 == 0x0UL))
        {
            goto label_0xCCD1C4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x23 = x0;
        x0 = x8;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17C9D04UL /* metadata target: ParticleSystem.get_textureSheetAnimation */, x0, x1, x2, x3);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x140UL))), x0);
        x0 = unchecked((ulong)((sp) + (0x140UL)));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17CA078UL /* metadata target: ParticleSystem.TextureSheetAnimationModule.get_enabled */, x0, x1, x2, x3);
        __arm64_pair_address_13422656 = unchecked((ulong)((sp) + (0x20UL)));
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13422656)), 0));
        v10 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13422656) + (0x4UL))))), 0));
        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((sp) + (0x28UL))))), 0));
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCCD074;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = unchecked((ulong)((sp) + (0x30UL)));
        x2 = unchecked((ulong)(unchecked((uint)(0x84UL))));
        x1 = x21;
        x0 = RuntimeCalls.InvokeDirect(0x19B0C40UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x1 = unchecked((ulong)((sp) + (0x30UL)));
        x0 = x20;
        x2 = x23;
        x0 = RuntimeCalls.InvokeDirect(0xCCD574UL /* metadata target: UiParticles.EvaluateTexturesheetUVs */, x0, x1, x2, x3);
        goto label_0xCCD07C;
        label_0xCCD074:
        ;
        x1 = x23;
        x0 = RuntimeCalls.InvokeDirect(0xCCD518UL /* metadata target: UiParticles.EvaluateQuadUVs */, x0, x1, x2, x3);
        goto label_0xCCD07C;
        label_0xCCD07C:
        ;
        if ((x23 == 0x0UL))
        {
            goto label_0xCCD1C4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x23) + (0x18UL))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCCD1C8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCCD088UL);
        }
        __arm64_pair_address_13422728 = unchecked((ulong)((x23) + (0x20UL)));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13422728)), 0));
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13422728) + (0x4UL))))), 0));
        x20 = unchecked((ulong)((x24) & (0xFFFFFFFFUL)));
        x0 = x19;
        x1 = x20;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1985568UL /* metadata target: VertexHelper.AddVert */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x23) + (0x18UL))))));
        __arm64_flags_left_13422776 = unchecked((uint)(x8));
        __arm64_flags_right_13422776 = unchecked((uint)0x1UL);
        if (((!((__arm64_flags_left_13422776 >= __arm64_flags_right_13422776))) || (unchecked((uint)((__arm64_flags_left_13422776) - (__arm64_flags_right_13422776))) == unchecked((uint)0x0UL))))
        {
            goto label_0xCCD1C8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCCD0C0UL);
        }
        __arm64_pair_address_13422784 = unchecked((ulong)((sp) + (0x18UL)));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13422784)), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13422784) + (0x4UL))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((sp) + (0x14UL))))), 0));
        __arm64_pair_address_13422792 = unchecked((ulong)((x23) + (0x28UL)));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13422792)), 0));
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13422792) + (0x4UL))))), 0));
        x0 = x19;
        x1 = x20;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1985568UL /* metadata target: VertexHelper.AddVert */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x23) + (0x18UL))))));
        __arm64_flags_left_13422836 = unchecked((uint)(x8));
        __arm64_flags_right_13422836 = unchecked((uint)0x2UL);
        if (((!((__arm64_flags_left_13422836 >= __arm64_flags_right_13422836))) || (unchecked((uint)((__arm64_flags_left_13422836) - (__arm64_flags_right_13422836))) == unchecked((uint)0x0UL))))
        {
            goto label_0xCCD1C8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCCD0FCUL);
        }
        __arm64_pair_address_13422844 = unchecked((ulong)((sp) + (0xCUL)));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13422844)), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13422844) + (0x4UL))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((sp) + (0x8UL))))), 0));
        __arm64_pair_address_13422852 = unchecked((ulong)((x23) + (0x30UL)));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13422852)), 0));
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13422852) + (0x4UL))))), 0));
        x0 = x19;
        x1 = x20;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1985568UL /* metadata target: VertexHelper.AddVert */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x23) + (0x18UL))))));
        __arm64_flags_left_13422896 = unchecked((uint)(x8));
        __arm64_flags_right_13422896 = unchecked((uint)0x3UL);
        if (((!((__arm64_flags_left_13422896 >= __arm64_flags_right_13422896))) || (unchecked((uint)((__arm64_flags_left_13422896) - (__arm64_flags_right_13422896))) == unchecked((uint)0x0UL))))
        {
            goto label_0xCCD1C8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCCD138UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((sp) + (0x4UL))))), 0));
        __arm64_pair_address_13422908 = unchecked((ulong)((x23) + (0x38UL)));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13422908)), 0));
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13422908) + (0x4UL))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(sp)), 0));
        x0 = x19;
        x1 = x20;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1985568UL /* metadata target: VertexHelper.AddVert */, x0, x1, x2, x3);
        x20 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x22))) + (unchecked((uint)(0x2UL)))))));
        x2 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x22))) + (unchecked((uint)(0x1UL)))))));
        x0 = x19;
        x1 = unchecked((ulong)(unchecked((uint)(x22))));
        x3 = unchecked((ulong)(unchecked((uint)(x20))));
        x0 = RuntimeCalls.InvokeDirect(0x1985698UL /* metadata target: VertexHelper.AddTriangle */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x2 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x22))) + (unchecked((uint)(0x3UL)))))));
        x0 = x19;
        x1 = unchecked((ulong)(unchecked((uint)(x20))));
        x3 = unchecked((ulong)(unchecked((uint)(x22))));
        x0 = RuntimeCalls.InvokeDirect(0x1985698UL /* metadata target: VertexHelper.AddTriangle */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x1E0UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x1E0UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x1D0UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x1D0UL)))) + (0x8UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x1C0UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x1C0UL)))) + (0x8UL))));
        x29 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x1B0UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x1B0UL)))) + (0x8UL))));
        __arm64_pair_address_13423020 = unchecked((ulong)((sp) + (0x1A0UL)));
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13423020)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13423020) + (0x8UL))))), 0));
        __arm64_pair_address_13423024 = unchecked((ulong)((sp) + (0x190UL)));
        v11 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13423024)), 0));
        v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13423024) + (0x8UL))))), 0));
        __arm64_pair_address_13423028 = unchecked((ulong)((sp) + (0x180UL)));
        v13 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13423028)), 0));
        v12 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13423028) + (0x8UL))))), 0));
        __arm64_pair_address_13423032 = unchecked((ulong)((sp) + (0x170UL)));
        v15 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13423032)), 0));
        v14 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13423032) + (0x8UL))))), 0));
        return x0;
        label_0xCCD1C4:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        goto label_0xCCD1C8;
        label_0xCCD1C8:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB7CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        return default(ulong);
    }
```

## `UiParticles.GetStrechedBillboardsSizeAndRotation` — RVA `0xccd1cc`

- Lift status: **exact**; input span: 844 bytes; span to next metadata RVA: 844 bytes.
- Metadata signature: `private void GetStrechedBillboardsSizeAndRotation(ParticleSystem.Particle particle, float timeAlive01, ref Vector3 size3D, out Quaternion rotation) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=85 (informational only).

```csharp
public static ulong UiParticles_GetStrechedBillboardsSizeAndRotation_RVAccd1cc(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        float __arm64_float_flags_left_13423608 = default(float);
        float __arm64_float_flags_left_13423664 = default(float);
        float __arm64_float_flags_left_13423716 = default(float);
        float __arm64_float_flags_right_13423608 = default(float);
        float __arm64_float_flags_right_13423664 = default(float);
        float __arm64_float_flags_right_13423716 = default(float);
        float __arm64_fp_left_13423660 = default(float);
        float __arm64_fp_right_13423660 = default(float);
        ulong __arm64_pair_address_13423056 = default(ulong);
        ulong __arm64_pair_address_13423060 = default(ulong);
        ulong __arm64_pair_address_13423064 = default(ulong);
        ulong __arm64_pair_address_13423068 = default(ulong);
        ulong __arm64_pair_address_13423120 = default(ulong);
        ulong __arm64_pair_address_13423176 = default(ulong);
        ulong __arm64_pair_address_13423244 = default(ulong);
        ulong __arm64_pair_address_13423256 = default(ulong);
        ulong __arm64_pair_address_13423308 = default(ulong);
        ulong __arm64_pair_address_13423320 = default(ulong);
        ulong __arm64_pair_address_13423372 = default(ulong);
        ulong __arm64_pair_address_13423384 = default(ulong);
        ulong __arm64_pair_address_13423496 = default(ulong);
        ulong __arm64_pair_address_13423744 = default(ulong);
        ulong __arm64_pair_address_13423748 = default(ulong);
        ulong __arm64_pair_address_13423756 = default(ulong);
        ulong __arm64_pair_address_13423848 = default(ulong);
        ulong __arm64_pair_address_13423868 = default(ulong);
        ulong __arm64_pair_address_13423872 = default(ulong);
        ulong __arm64_pair_address_13423876 = default(ulong);
        ulong __arm64_pair_address_13423880 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v10 = default(RuntimeVector128);
        RuntimeVector128 v11 = default(RuntimeVector128);
        RuntimeVector128 v12 = default(RuntimeVector128);
        RuntimeVector128 v13 = default(RuntimeVector128);
        RuntimeVector128 v14 = default(RuntimeVector128);
        RuntimeVector128 v15 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        RuntimeVector128 v9 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x22 = default(ulong);
        ulong x23 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        sp = unchecked((ulong)((sp) - (0xD0UL)));
        __arm64_pair_address_13423056 = unchecked((ulong)((sp) + (0x60UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13423056, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v15.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13423056) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v14.GetUInt64(0)))));
        __arm64_pair_address_13423060 = unchecked((ulong)((sp) + (0x70UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13423060, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v13.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13423060) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v12.GetUInt64(0)))));
        __arm64_pair_address_13423064 = unchecked((ulong)((sp) + (0x80UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13423064, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v11.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13423064) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v10.GetUInt64(0)))));
        __arm64_pair_address_13423068 = unchecked((ulong)((sp) + (0x90UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13423068, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13423068) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xA0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xA0UL)))) + (0x8UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xB0UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xB0UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xC0UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xC0UL)))) + (0x8UL))), x19);
        x23 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x23) + (0x2C9UL))))))));
        x21 = x3;
        x19 = x2;
        v8 = v0;
        x22 = x1;
        x20 = x0;
        v0 = (RuntimeVector128.Zero.WithUInt64(0, 0x0UL) | RuntimeVector128.Zero.WithUInt64(0, 0x0UL).ShiftLeftLogical(unchecked((int)0x40UL)));
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0x58UL))), 0x0UL);
        __arm64_pair_address_13423120 = unchecked((ulong)((sp) + (0x30UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13423120, v0);
#else
        __WriteVector128(__arm64_pair_address_13423120, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13423120) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13423120) + (0x10UL))), v0);
#endif
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCCD22C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x1E8UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x23) + (0x2C9UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCCD22C;
        label_0xCCD22C:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xD8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCCD514;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x23 = 0x1A8C000UL;
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0x1E8UL))));
        x1 = 0x0UL;
        x8 = RuntimeMemory.ReadU64(x23);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        __arm64_pair_address_13423176 = unchecked((ulong)((x8) + (0x4UL)));
        v11 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13423176)), 0));
        v10 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13423176) + (0x4UL))))), 0));
        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(x8)), 0));
        x0 = RuntimeCalls.InvokeDirect(0x17C9CDCUL /* metadata target: ParticleSystem.get_velocityOverLifetime */, x0, x1, x2, x3);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x58UL))), x0);
        x0 = unchecked((ulong)((sp) + (0x58UL)));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17CA600UL /* metadata target: ParticleSystem.VelocityOverLifetimeModule.get_enabled */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCCD328;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xD8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCCD514;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17C9CDCUL /* metadata target: ParticleSystem.get_velocityOverLifetime */, x0, x1, x2, x3);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x58UL))), x0);
        x0 = unchecked((ulong)((sp) + (0x58UL)));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17CA678UL /* metadata target: ParticleSystem.VelocityOverLifetimeModule.get_x */, x0, x1, x2, x3);
        __arm64_pair_address_13423244 = unchecked((ulong)((sp) + (0x10UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13423244);
#else
        v0 = __ReadVector128(__arm64_pair_address_13423244);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13423244) + (0x10UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13423244) + (0x10UL))));
#endif
        x0 = unchecked((ulong)((sp) + (0x30UL)));
        x1 = 0x0UL;
        __arm64_pair_address_13423256 = unchecked((ulong)((sp) + (0x30UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13423256, v0);
#else
        __WriteVector128(__arm64_pair_address_13423256, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13423256) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13423256) + (0x10UL))), v1);
#endif
        v0 = v8;
        x0 = RuntimeCalls.InvokeDirect(0x17CA510UL /* metadata target: ParticleSystem.MinMaxCurve.Evaluate */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xD8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCCD514;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        v9 = v0;
        x0 = RuntimeCalls.InvokeDirect(0x17C9CDCUL /* metadata target: ParticleSystem.get_velocityOverLifetime */, x0, x1, x2, x3);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x58UL))), x0);
        x0 = unchecked((ulong)((sp) + (0x58UL)));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17CA71CUL /* metadata target: ParticleSystem.VelocityOverLifetimeModule.get_y */, x0, x1, x2, x3);
        __arm64_pair_address_13423308 = unchecked((ulong)((sp) + (0x10UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13423308);
#else
        v0 = __ReadVector128(__arm64_pair_address_13423308);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13423308) + (0x10UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13423308) + (0x10UL))));
#endif
        x0 = unchecked((ulong)((sp) + (0x30UL)));
        x1 = 0x0UL;
        __arm64_pair_address_13423320 = unchecked((ulong)((sp) + (0x30UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13423320, v0);
#else
        __WriteVector128(__arm64_pair_address_13423320, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13423320) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13423320) + (0x10UL))), v1);
#endif
        v0 = v8;
        x0 = RuntimeCalls.InvokeDirect(0x17CA510UL /* metadata target: ParticleSystem.MinMaxCurve.Evaluate */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xD8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCCD514;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        v11 = v0;
        x0 = RuntimeCalls.InvokeDirect(0x17C9CDCUL /* metadata target: ParticleSystem.get_velocityOverLifetime */, x0, x1, x2, x3);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x58UL))), x0);
        x0 = unchecked((ulong)((sp) + (0x58UL)));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17CA7C0UL /* metadata target: ParticleSystem.VelocityOverLifetimeModule.get_z */, x0, x1, x2, x3);
        __arm64_pair_address_13423372 = unchecked((ulong)((sp) + (0x10UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13423372);
#else
        v0 = __ReadVector128(__arm64_pair_address_13423372);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13423372) + (0x10UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13423372) + (0x10UL))));
#endif
        x0 = unchecked((ulong)((sp) + (0x30UL)));
        x1 = 0x0UL;
        __arm64_pair_address_13423384 = unchecked((ulong)((sp) + (0x30UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13423384, v0);
#else
        __WriteVector128(__arm64_pair_address_13423384, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13423384) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13423384) + (0x10UL))), v1);
#endif
        v0 = v8;
        x0 = RuntimeCalls.InvokeDirect(0x17CA510UL /* metadata target: ParticleSystem.MinMaxCurve.Evaluate */, x0, x1, x2, x3);
        v10 = v0;
        goto label_0xCCD328;
        label_0xCCD328:
        ;
        x0 = x22;
        x1 = 0x0UL;
        RuntimeMemory.WriteF32(unchecked((ulong)((sp) + (0xCUL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0));
        v10 = v11;
        x0 = RuntimeCalls.InvokeDirect(0x17CA43CUL /* metadata target: ParticleSystem.Particle.get_velocity */, x0, x1, x2, x3);
        x22 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x22) + (0x32CUL))))))));
        v8 = v0;
        v12 = v1;
        v13 = v2;
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCCD368;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x1E8UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x22) + (0x32CUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCCD368;
        label_0xCCD368:
        ;
        x8 = RuntimeMemory.ReadU64(x23);
        x22 = 0x1BAB000UL;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((sp) + (0xCUL))))), 0));
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x22) + (0x3E2UL))))))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0))))), 0));
        v12 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v12.GetUInt64(0)))), 0))))), 0));
        v10 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v13.GetUInt64(0)))), 0))))), 0));
        __arm64_pair_address_13423496 = unchecked((ulong)((x8) + (0x18UL)));
        v11 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13423496)), 0));
        v15 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13423496) + (0x4UL))))), 0));
        v14 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x20UL))))), 0));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCCD3A8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xA60UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x22) + (0x3E2UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCCD3A8;
        label_0xCCD3A8:
        ;
        x22 = 0x1A8C000UL;
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0xA60UL))));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v12.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v12.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        x0 = RuntimeMemory.ReadU64(x22);
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0))))), 0));
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0))))), 0));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v15.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v15.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v14.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v14.GetUInt64(0)))), 0))))), 0));
        v13 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCCD3E8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCCD3E4UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCCD3E8;
        label_0xCCD3E8:
        ;
        x8 = 0x432000UL;
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x344UL))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v13.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)(global::System.Math.Sqrt(unchecked((double)(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))))), 0));
        __arm64_float_flags_left_13423608 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13423608 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        if ((__arm64_float_flags_left_13423608 < __arm64_float_flags_right_13423608))
        {
            goto label_0xCCD458;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(x22);
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v12.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v15.GetUInt64(0)))), 0))))), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v14.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0xBF800000UL)), 0)), 0));
        __arm64_fp_left_13423660 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_fp_right_13423660 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_fp_left_13423660 != __arm64_fp_left_13423660) ? __arm64_fp_left_13423660 : ((__arm64_fp_right_13423660 != __arm64_fp_right_13423660) ? __arm64_fp_right_13423660 : (((__arm64_fp_left_13423660 == global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)) && (__arm64_fp_right_13423660 == global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0))) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)((global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(__arm64_fp_left_13423660), 0)) | (global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(__arm64_fp_right_13423660), 0))))), 0) : ((__arm64_fp_left_13423660 <= __arm64_fp_right_13423660) ? __arm64_fp_left_13423660 : __arm64_fp_right_13423660))))), 0));
        __arm64_float_flags_left_13423664 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13423664 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0);
        v10 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes((((__arm64_float_flags_left_13423664 >= __arm64_float_flags_right_13423664) || ((__arm64_float_flags_left_13423664 != __arm64_float_flags_left_13423664) || (__arm64_float_flags_right_13423664 != __arm64_float_flags_right_13423664))) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))), 0));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCCD440;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCCD43CUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCCD440;
        label_0xCCD440:
        ;
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(unchecked((double)(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0)))), 0));
        x0 = RuntimeCalls.InvokeDirect(0x19B0CA0UL, x0, x1, x2, x3);
        x8 = 0x432000UL;
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x554UL))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)(global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0))))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        goto label_0xCCD458;
        label_0xCCD458:
        ;
        x8 = 0x432000UL;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x3E4UL))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes((-(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)))), 0));
        __arm64_float_flags_left_13423716 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13423716 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_13423716 < __arm64_float_flags_right_13423716) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x178B12CUL /* metadata target: Quaternion.Internal_FromEulerRad */, x0, x1, x2, x3);
        __arm64_pair_address_13423744 = x21;
        RuntimeMemory.WriteF32(__arm64_pair_address_13423744, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_13423744) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0));
        __arm64_pair_address_13423748 = unchecked((ulong)((x21) + (0x8UL)));
        RuntimeMemory.WriteF32(__arm64_pair_address_13423748, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_13423748) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x20) + (0xE8UL))))), 0));
        __arm64_pair_address_13423756 = x19;
        v10 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13423756)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13423756) + (0x4UL))))), 0));
        x21 = 0x1BAB000UL;
        v11 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x8UL))))), 0));
        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((x19) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0));
        v12 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x20) + (0xE4UL))))), 0));
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x3DFUL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCCD4C0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xA60UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x3DFUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCCD4C0;
        label_0xCCD4C0:
        ;
        x0 = RuntimeMemory.ReadU64(x22);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCCD4D0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCCD4CCUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCCD4D0;
        label_0xCCD4D0:
        ;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)(global::System.Math.Sqrt(unchecked((double)(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0))))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v12.GetUInt64(0)))), 0))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        __arm64_pair_address_13423848 = x19;
        RuntimeMemory.WriteF32(__arm64_pair_address_13423848, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_13423848) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((x19) + (0x8UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0xC0UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xC0UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0xB0UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xB0UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0xA0UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xA0UL)))) + (0x8UL))));
        __arm64_pair_address_13423868 = unchecked((ulong)((sp) + (0x90UL)));
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13423868)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13423868) + (0x8UL))))), 0));
        __arm64_pair_address_13423872 = unchecked((ulong)((sp) + (0x80UL)));
        v11 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13423872)), 0));
        v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13423872) + (0x8UL))))), 0));
        __arm64_pair_address_13423876 = unchecked((ulong)((sp) + (0x70UL)));
        v13 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13423876)), 0));
        v12 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13423876) + (0x8UL))))), 0));
        __arm64_pair_address_13423880 = unchecked((ulong)((sp) + (0x60UL)));
        v15 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13423880)), 0));
        v14 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13423880) + (0x8UL))))), 0));
        return x0;
        label_0xCCD514:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `UiParticles.EvaluateQuadUVs` — RVA `0xccd518`

- Lift status: **partial**; input span: 92 bytes; span to next metadata RVA: 92 bytes.
- Metadata signature: `private void EvaluateQuadUVs(Vector2[] uvs) { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=4 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'b.eq' at 0xccd530; reason: Unknown IR expression at 0xccd530; reason: Unsupported instruction 'fmov' at 0xccd548

```csharp
public static ulong UiParticles_EvaluateQuadUVs_RVAccd518(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13423912 = default(uint);
        uint __arm64_flags_left_13423932 = default(uint);
        uint __arm64_flags_left_13423948 = default(uint);
        uint __arm64_flags_right_13423912 = default(uint);
        uint __arm64_flags_right_13423932 = default(uint);
        uint __arm64_flags_right_13423948 = default(uint);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL))), x30);
        if ((x1 == 0x0UL))
        {
        }
        else
        {
            x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x1) + (0x18UL))))));
            if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
            {
            }
            else
            {
                __arm64_flags_left_13423912 = unchecked((uint)(x8));
                __arm64_flags_right_13423912 = unchecked((uint)0x1UL);
                RuntimeMemory.WritePtr(unchecked((ulong)((x1) + (0x20UL))), 0x0UL);
                RuntimeCalls.Unsupported("b.eq", 0xCCD530UL);
                if (__Unsupported<bool>("Unknown IR expression"))
                {
                }
                else
                {
                    x9 = 0x432000UL;
                    v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((x9) + (0x78UL))))), 0));
                    __arm64_flags_left_13423932 = unchecked((uint)(x8));
                    __arm64_flags_right_13423932 = unchecked((uint)0x2UL);
                    RuntimeMemory.WriteF64(unchecked((ulong)((x1) + (0x28UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))));
                    if (((!((__arm64_flags_left_13423932 >= __arm64_flags_right_13423932))) || (unchecked((uint)((__arm64_flags_left_13423932) - (__arm64_flags_right_13423932))) == unchecked((uint)0x0UL))))
                    {
                    }
                    else
                    {
                        RuntimeCalls.Unsupported("fmov", 0xCCD548UL);
                        __arm64_flags_left_13423948 = unchecked((uint)(x8));
                        __arm64_flags_right_13423948 = unchecked((uint)0x3UL);
                        RuntimeMemory.WriteF64(unchecked((ulong)((x1) + (0x30UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))));
                        if ((unchecked((uint)((__arm64_flags_left_13423948) - (__arm64_flags_right_13423948))) == unchecked((uint)0x0UL)))
                        {
                        }
                        else
                        {
                            x8 = 0x431000UL;
                            v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((x8) + (0xB80UL))))), 0));
                            RuntimeMemory.WriteF64(unchecked((ulong)((x1) + (0x38UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))));
                            x30 = RuntimeMemory.ReadU64(sp);
                            return x0;
                        }
                    }
                }
            }
            label_0xCCD56C:
            ;
            x0 = RuntimeCalls.InvokeDirect(0xB7DB7CUL, x0, x1, x2, x3);
        }
        label_0xCCD570:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `UiParticles.EvaluateTexturesheetUVs` — RVA `0xccd574`

- Lift status: **partial**; input span: 688 bytes; span to next metadata RVA: 688 bytes.
- Metadata signature: `private void EvaluateTexturesheetUVs(ParticleSystem.Particle particle, float timeAlive, Vector2[] uvs) { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=77 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'frintm' at 0xccd698; reason: Unsupported instruction 'fcsel' at 0xccd6c0; reason: Unknown IR expression at 0xccd6c0; reason: Unsupported instruction 'frintm' at 0xccd65c; reason: Unsupported instruction 'csel' at 0xccd754; reason: Unknown IR expression at 0xccd754

```csharp
public static ulong UiParticles_EvaluateTexturesheetUVs_RVAccd574(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        float __arm64_fcvtz_source_13424448 = default(float);
        uint __arm64_flags_left_13424192 = default(uint);
        uint __arm64_flags_left_13424588 = default(uint);
        uint __arm64_flags_left_13424608 = default(uint);
        uint __arm64_flags_left_13424624 = default(uint);
        uint __arm64_flags_right_13424192 = default(uint);
        uint __arm64_flags_right_13424588 = default(uint);
        uint __arm64_flags_right_13424608 = default(uint);
        uint __arm64_flags_right_13424624 = default(uint);
        float __arm64_float_flags_left_13424224 = default(float);
        float __arm64_float_flags_left_13424240 = default(float);
        float __arm64_float_flags_left_13424296 = default(float);
        float __arm64_float_flags_left_13424304 = default(float);
        float __arm64_float_flags_left_13424452 = default(float);
        float __arm64_float_flags_right_13424224 = default(float);
        float __arm64_float_flags_right_13424240 = default(float);
        float __arm64_float_flags_right_13424296 = default(float);
        float __arm64_float_flags_right_13424304 = default(float);
        float __arm64_float_flags_right_13424452 = default(float);
        ulong __arm64_pair_address_13423992 = default(ulong);
        ulong __arm64_pair_address_13424020 = default(ulong);
        ulong __arm64_pair_address_13424152 = default(ulong);
        ulong __arm64_pair_address_13424164 = default(ulong);
        ulong __arm64_pair_address_13424596 = default(ulong);
        ulong __arm64_pair_address_13424612 = default(ulong);
        ulong __arm64_pair_address_13424628 = default(ulong);
        ulong __arm64_pair_address_13424636 = default(ulong);
        ulong __arm64_pair_address_13424656 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
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
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        sp = unchecked((ulong)((sp) - (0x90UL)));
        __arm64_pair_address_13423992 = unchecked((ulong)((sp) + (0x40UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13423992, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13423992) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x50UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x0UL))), x24);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x8UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x70UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x70UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x80UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x80UL)))) + (0x8UL))), x19);
        v8 = v0;
        v0 = (RuntimeVector128.Zero.WithUInt64(0, 0x0UL) | RuntimeVector128.Zero.WithUInt64(0, 0x0UL).ShiftLeftLogical(unchecked((int)0x40UL)));
        __arm64_pair_address_13424020 = unchecked((ulong)((sp) + (0x20UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13424020, v0);
#else
        __WriteVector128(__arm64_pair_address_13424020, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13424020) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13424020) + (0x10UL))), v0);
#endif
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD8UL))));
        if ((x0 == 0x0UL))
        {
        }
        else
        {
            x20 = x1;
            x1 = 0x0UL;
            x19 = x2;
            x0 = RuntimeCalls.InvokeDirect(0x17C9D04UL /* metadata target: ParticleSystem.get_textureSheetAnimation */, x0, x1, x2, x3);
            RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x58UL))), x0);
            x0 = x20;
            x1 = 0x0UL;
            x0 = RuntimeCalls.InvokeDirect(0x17CA450UL /* metadata target: ParticleSystem.Particle.get_startLifetime */, x0, x1, x2, x3);
            x0 = unchecked((ulong)((sp) + (0x58UL)));
            x1 = 0x0UL;
            v9 = v0;
            x0 = RuntimeCalls.InvokeDirect(0x17CA338UL /* metadata target: ParticleSystem.TextureSheetAnimationModule.get_cycleCount */, x0, x1, x2, x3);
            v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)(unchecked((int)(unchecked((uint)(x0))))))), 0));
            v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
            v0 = v8;
            v1 = v9;
            x0 = RuntimeCalls.InvokeDirect(0x19B0CB0UL, x0, x1, x2, x3);
            x0 = unchecked((ulong)((sp) + (0x58UL)));
            x1 = 0x0UL;
            v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0))))), 0));
            x0 = RuntimeCalls.InvokeDirect(0x17CA168UL /* metadata target: ParticleSystem.TextureSheetAnimationModule.get_numTilesY */, x0, x1, x2, x3);
            x21 = unchecked((ulong)(unchecked((uint)(x0))));
            x0 = unchecked((ulong)((sp) + (0x58UL)));
            x1 = 0x0UL;
            x0 = RuntimeCalls.InvokeDirect(0x17CA0F0UL /* metadata target: ParticleSystem.TextureSheetAnimationModule.get_numTilesX */, x0, x1, x2, x3);
            x22 = unchecked((ulong)(unchecked((uint)(x0))));
            x8 = sp;
            x0 = unchecked((ulong)((sp) + (0x58UL)));
            x1 = 0x0UL;
            x0 = RuntimeCalls.InvokeDirect(0x17CA294UL /* metadata target: ParticleSystem.TextureSheetAnimationModule.get_frameOverTime */, x0, x1, x2, x3);
            __arm64_pair_address_13424152 = sp;
#if IL2CPPREC_RUNTIME_VECTOR128
            v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13424152);
#else
            v0 = __ReadVector128(__arm64_pair_address_13424152);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
            v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13424152) + (0x10UL))));
#else
            v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13424152) + (0x10UL))));
#endif
            x0 = unchecked((ulong)((sp) + (0x20UL)));
            x1 = 0x0UL;
            __arm64_pair_address_13424164 = unchecked((ulong)((sp) + (0x20UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
            RuntimeMemory.WriteVector128(__arm64_pair_address_13424164, v0);
#else
            __WriteVector128(__arm64_pair_address_13424164, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
            RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13424164) + (0x10UL))), v1);
#else
            __WriteVector128(unchecked((ulong)((__arm64_pair_address_13424164) + (0x10UL))), v1);
#endif
            v0 = v8;
            x0 = RuntimeCalls.InvokeDirect(0x17CA510UL /* metadata target: ParticleSystem.MinMaxCurve.Evaluate */, x0, x1, x2, x3);
            x0 = unchecked((ulong)((sp) + (0x58UL)));
            x1 = 0x0UL;
            v8 = v0;
            x0 = RuntimeCalls.InvokeDirect(0x17CA1E0UL /* metadata target: ParticleSystem.TextureSheetAnimationModule.get_animation */, x0, x1, x2, x3);
            __arm64_flags_left_13424192 = unchecked((uint)(x0));
            __arm64_flags_right_13424192 = unchecked((uint)0x1UL);
            if ((unchecked((uint)((__arm64_flags_left_13424192) - (__arm64_flags_right_13424192))) == unchecked((uint)0x0UL)))
            {
                label_0xCCD67C:
                ;
                x0 = unchecked((ulong)((sp) + (0x58UL)));
                x1 = 0x0UL;
                x0 = RuntimeCalls.InvokeDirect(0x17CA0F0UL /* metadata target: ParticleSystem.TextureSheetAnimationModule.get_numTilesX */, x0, x1, x2, x3);
                v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)(unchecked((int)(unchecked((uint)(x0))))))), 0));
                v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
                x0 = unchecked((ulong)((sp) + (0x58UL)));
                x1 = 0x0UL;
                RuntimeCalls.Unsupported("frintm", 0xCCD698UL);
                x0 = RuntimeCalls.InvokeDirect(0x17CA0F0UL /* metadata target: ParticleSystem.TextureSheetAnimationModule.get_numTilesX */, x0, x1, x2, x3);
                x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) - (unchecked((uint)(0x1UL)))))));
                v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)(unchecked((int)(unchecked((uint)(x8))))))), 0));
                __arm64_float_flags_left_13424296 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0);
                __arm64_float_flags_right_13424296 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
                v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_13424296 > __arm64_float_flags_right_13424296) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0))), 0));
                __arm64_float_flags_left_13424304 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0);
                __arm64_float_flags_right_13424304 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
                v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
                x0 = unchecked((ulong)((sp) + (0x58UL)));
                x1 = 0x0UL;
                RuntimeCalls.Unsupported("fcsel", 0xCCD6C0UL);
                v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes((__Unsupported<bool>("Unknown IR expression") ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))), 0));
                x0 = RuntimeCalls.InvokeDirect(0x17CA3B0UL /* metadata target: ParticleSystem.TextureSheetAnimationModule.get_rowIndex */, x0, x1, x2, x3);
                x21 = unchecked((ulong)(unchecked((uint)(x0))));
                x0 = unchecked((ulong)((sp) + (0x58UL)));
                x1 = 0x0UL;
                x0 = RuntimeCalls.InvokeDirect(0x17C9FF4UL /* metadata target: ParticleSystem.TextureSheetAnimationModule.get_useRandomRow */, x0, x1, x2, x3);
                if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
                {
                }
                else
                {
                    x0 = x20;
                    x1 = 0x0UL;
                    x0 = RuntimeCalls.InvokeDirect(0x17CA458UL /* metadata target: ParticleSystem.Particle.get_randomSeed */, x0, x1, x2, x3);
                    x1 = 0x0UL;
                    x0 = RuntimeCalls.InvokeDirect(0x17900F0UL /* metadata target: Random.InitState */, x0, x1, x2, x3);
                    x0 = unchecked((ulong)((sp) + (0x58UL)));
                    x1 = 0x0UL;
                    x0 = RuntimeCalls.InvokeDirect(0x17CA168UL /* metadata target: ParticleSystem.TextureSheetAnimationModule.get_numTilesY */, x0, x1, x2, x3);
                    x1 = unchecked((ulong)(unchecked((uint)(x0))));
                    x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
                    x2 = 0x0UL;
                    x0 = RuntimeCalls.InvokeDirect(0x179016CUL /* metadata target: Random.Range */, unchecked((ulong)(unchecked((uint)(x0)))), unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
                    x21 = unchecked((ulong)(unchecked((uint)(x0))));
                }
                label_0xCCD710:
                ;
                x0 = unchecked((ulong)((sp) + (0x58UL)));
                x1 = 0x0UL;
                x0 = RuntimeCalls.InvokeDirect(0x17CA0F0UL /* metadata target: ParticleSystem.TextureSheetAnimationModule.get_numTilesX */, x0, x1, x2, x3);
                x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) * (unchecked((uint)(x21)))))));
                v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)(unchecked((int)(unchecked((uint)(x8))))))), 0));
                v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
            }
            else
            {
                v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
                if ((unchecked((uint)(x0)) != unchecked((uint)0x0UL)))
                {
                }
                else
                {
                    x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x22))) * (unchecked((uint)(x21)))))));
                    v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)(unchecked((int)(unchecked((uint)(x8))))))), 0));
                    v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
                    RuntimeCalls.Unsupported("frintm", 0xCCD65CUL);
                    __arm64_float_flags_left_13424224 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
                    __arm64_float_flags_right_13424224 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
                    if ((__arm64_float_flags_left_13424224 < __arm64_float_flags_right_13424224))
                    {
                    }
                    else
                    {
                        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) - (unchecked((uint)(0x1UL)))))));
                        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)(unchecked((int)(unchecked((uint)(x8))))))), 0));
                        __arm64_float_flags_left_13424240 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
                        __arm64_float_flags_right_13424240 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
                        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_13424240 > __arm64_float_flags_right_13424240) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))), 0));
                    }
                }
            }
            label_0xCCD728:
            ;
            x0 = unchecked((ulong)((sp) + (0x58UL)));
            x1 = 0x0UL;
            x0 = RuntimeCalls.InvokeDirect(0x17CA0F0UL /* metadata target: ParticleSystem.TextureSheetAnimationModule.get_numTilesX */, x0, x1, x2, x3);
            x8 = unchecked((ulong)(unchecked((uint)(0x7F800000UL))));
            v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(x8))), 0)), 0));
            x20 = unchecked((ulong)(unchecked((uint)(x0))));
            __arm64_fcvtz_source_13424448 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0);
            x9 = unchecked((ulong)(unchecked((uint)(((__arm64_fcvtz_source_13424448 != __arm64_fcvtz_source_13424448) ? unchecked((int)0x0UL) : ((__arm64_fcvtz_source_13424448 >= global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x4F000000UL)), 0)) ? unchecked((int)0x7FFFFFFFUL) : ((__arm64_fcvtz_source_13424448 < global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0xCF000000UL)), 0)) ? unchecked((int)0x80000000UL) : unchecked((int)(__arm64_fcvtz_source_13424448)))))))));
            __arm64_float_flags_left_13424452 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0);
            __arm64_float_flags_right_13424452 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
            x8 = unchecked((ulong)(unchecked((uint)(0xFFFFFFFF80000000UL))));
            x0 = unchecked((ulong)((sp) + (0x58UL)));
            x1 = 0x0UL;
            RuntimeCalls.Unsupported("csel", 0xCCD754UL);
            x24 = unchecked((ulong)((__Unsupported<bool>("Unknown IR expression") ? unchecked((uint)(x8)) : unchecked((uint)(x9)))));
            x0 = RuntimeCalls.InvokeDirect(0x17CA0F0UL /* metadata target: ParticleSystem.TextureSheetAnimationModule.get_numTilesX */, x0, x1, x2, x3);
            x21 = unchecked((ulong)(unchecked((uint)(x0))));
            x0 = unchecked((ulong)((sp) + (0x58UL)));
            x1 = 0x0UL;
            x0 = RuntimeCalls.InvokeDirect(0x17CA0F0UL /* metadata target: ParticleSystem.TextureSheetAnimationModule.get_numTilesX */, x0, x1, x2, x3);
            x22 = unchecked((ulong)(unchecked((uint)(x0))));
            x0 = unchecked((ulong)((sp) + (0x58UL)));
            x1 = 0x0UL;
            x0 = RuntimeCalls.InvokeDirect(0x17CA168UL /* metadata target: ParticleSystem.TextureSheetAnimationModule.get_numTilesY */, x0, x1, x2, x3);
            x23 = unchecked((ulong)(unchecked((uint)(x0))));
            x0 = unchecked((ulong)((sp) + (0x58UL)));
            x1 = 0x0UL;
            x0 = RuntimeCalls.InvokeDirect(0x17CA168UL /* metadata target: ParticleSystem.TextureSheetAnimationModule.get_numTilesY */, x0, x1, x2, x3);
            if ((x19 == 0x0UL))
            {
            }
            else
            {
                x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x18UL))))));
                if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
                {
                }
                else
                {
                    x9 = unchecked((ulong)(unchecked((uint)(unchecked((int)((unchecked((int)(unchecked((uint)(x24))))) / (unchecked((int)(unchecked((uint)(x20)))))))))));
                    x10 = unchecked((ulong)(unchecked((uint)(unchecked((int)((unchecked((int)(unchecked((uint)(x24))))) / (unchecked((int)(unchecked((uint)(x21)))))))))));
                    v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)(unchecked((int)(unchecked((uint)(x22))))))), 0));
                    v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
                    x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x24))) - (unchecked((uint)((unchecked((uint)(x9))) * (unchecked((uint)(x20))))))))));
                    x10 = unchecked((ulong)((~(unchecked((uint)(x10))))));
                    v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)(unchecked((int)(unchecked((uint)(x23))))))), 0));
                    v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
                    x10 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) + (unchecked((uint)(x10)))))));
                    v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)(unchecked((int)(unchecked((uint)(x9))))))), 0));
                    v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0))))), 0));
                    v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
                    v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)(unchecked((int)(unchecked((uint)(x10))))))), 0));
                    __arm64_flags_left_13424588 = unchecked((uint)(x8));
                    __arm64_flags_right_13424588 = unchecked((uint)0x1UL);
                    v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
                    __arm64_pair_address_13424596 = unchecked((ulong)((x19) + (0x20UL)));
                    RuntimeMemory.WriteF32(__arm64_pair_address_13424596, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0));
                    RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_13424596) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
                    if ((unchecked((uint)((__arm64_flags_left_13424588) - (__arm64_flags_right_13424588))) == unchecked((uint)0x0UL)))
                    {
                    }
                    else
                    {
                        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
                        __arm64_flags_left_13424608 = unchecked((uint)(x8));
                        __arm64_flags_right_13424608 = unchecked((uint)0x2UL);
                        __arm64_pair_address_13424612 = unchecked((ulong)((x19) + (0x28UL)));
                        RuntimeMemory.WriteF32(__arm64_pair_address_13424612, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0));
                        RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_13424612) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0));
                        if (((!((__arm64_flags_left_13424608 >= __arm64_flags_right_13424608))) || (unchecked((uint)((__arm64_flags_left_13424608) - (__arm64_flags_right_13424608))) == unchecked((uint)0x0UL))))
                        {
                        }
                        else
                        {
                            v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
                            __arm64_flags_left_13424624 = unchecked((uint)(x8));
                            __arm64_flags_right_13424624 = unchecked((uint)0x3UL);
                            __arm64_pair_address_13424628 = unchecked((ulong)((x19) + (0x30UL)));
                            RuntimeMemory.WriteF32(__arm64_pair_address_13424628, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0));
                            RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_13424628) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0));
                            if ((unchecked((uint)((__arm64_flags_left_13424624) - (__arm64_flags_right_13424624))) == unchecked((uint)0x0UL)))
                            {
                            }
                            else
                            {
                                __arm64_pair_address_13424636 = unchecked((ulong)((x19) + (0x38UL)));
                                RuntimeMemory.WriteF32(__arm64_pair_address_13424636, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0));
                                RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_13424636) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
                                x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x80UL))));
                                x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x80UL)))) + (0x8UL))));
                                x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x70UL))));
                                x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x70UL)))) + (0x8UL))));
                                x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x60UL))));
                                x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x8UL))));
                                x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x50UL))));
                                __arm64_pair_address_13424656 = unchecked((ulong)((sp) + (0x40UL)));
                                v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13424656)), 0));
                                v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13424656) + (0x8UL))))), 0));
                                sp = unchecked((ulong)((sp) + (0x90UL)));
                                return x0;
                            }
                        }
                    }
                }
                label_0xCCD81C:
                ;
                x0 = RuntimeCalls.InvokeDirect(0xB7DB7CUL, x0, x1, x2, x3);
            }
        }
        label_0xCCD820:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `UiParticles.ctor` — RVA `0xccd824`

- Lift status: **partial**; input span: 16 bytes; span to next metadata RVA: 16 bytes.
- Metadata signature: `public void .ctor() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'fmov' at 0xccd824

```csharp
public static ulong UiParticles_ctor_RVAccd824(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeCalls.Unsupported("fmov", 0xCCD824UL);
        x1 = 0x0UL;
        RuntimeMemory.WriteF64(unchecked((ulong)((x0) + (0xE4UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))));
        return RuntimeCalls.InvokeDirect(0x1983BD4UL /* metadata target: MaskableGraphic.ctor */);
        return default(ulong);
    }
```
