# `SunShafts` — TypeDefIndex 3638

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x24` | `SunShafts.SunShaftsResolution` | `resolution` |
| `0x28` | `SunShafts.ShaftsScreenBlendMode` | `screenBlendMode` |
| `0x30` | `Transform` | `sunTransform` |
| `0x38` | `int` | `radialBlurIterations` |
| `0x3C` | `Color` | `sunColor` |
| `0x4C` | `Color` | `sunThreshold` |
| `0x5C` | `float` | `sunShaftBlurRadius` |
| `0x60` | `float` | `sunShaftIntensity` |
| `0x64` | `float` | `maxRadius` |
| `0x68` | `bool` | `useDepthTexture` |
| `0x70` | `Shader` | `sunShaftsShader` |
| `0x78` | `Material` | `sunShaftsMaterial` |
| `0x80` | `Shader` | `simpleClearShader` |
| `0x88` | `Material` | `simpleClearMaterial` |

## `SunShafts.CheckResources` — RVA `0xce76fc`

- Lift status: **exact**; input span: 140 bytes; span to next metadata RVA: 140 bytes.
- Metadata signature: `public override bool CheckResources() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=20 (informational only).

```csharp
public static uint SunShafts_CheckResources_RVAce76fc(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13530996 = default(uint);
        uint __arm64_flags_right_13530996 = default(uint);
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        x1 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x68UL))))))));
        x19 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xCE6708UL /* metadata target: PostEffectsBase.CheckSupport */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x20 = x19;
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x70UL))));
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x78UL))));
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xCE619CUL /* metadata target: PostEffectsBase.CheckShaderAndCreateMaterial */, x0, x1, x2, x3);
        x1 = x0;
        RuntimeMemory.WriteU64(x20, x0);
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x20 = x19;
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x80UL))));
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x88UL))));
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xCE619CUL /* metadata target: PostEffectsBase.CheckShaderAndCreateMaterial */, x0, x1, x2, x3);
        x1 = x0;
        RuntimeMemory.WriteU64(x20, x0);
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x22UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            label_0xCE7768:
            ;
            x0 = x19;
            x0 = RuntimeCalls.InvokeDirect(0xCE692CUL /* metadata target: PostEffectsBase.ReportAutoDisable */, x0, x1, x2, x3);
            x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x22UL))))))));
            __arm64_flags_left_13530996 = unchecked((uint)(x8));
            __arm64_flags_right_13530996 = unchecked((uint)0x0UL);
            x0 = unchecked((ulong)(((!((unchecked((uint)((__arm64_flags_left_13530996) - (__arm64_flags_right_13530996))) == unchecked((uint)0x0UL)))) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        }
        else
        {
            x0 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        }
        label_0xCE777C:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return unchecked((uint)(x0));
        return default(uint);
    }
```

## `SunShafts.Start` — RVA `0xce7788`

- Lift status: **exact**; input span: 512 bytes; span to next metadata RVA: 512 bytes.
- Metadata signature: `private void Start() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=72 (informational only).

```csharp
public static ulong SunShafts_Start_RVAce7788(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13531260 = default(uint);
        uint __arm64_flags_left_13531272 = default(uint);
        uint __arm64_flags_left_13531300 = default(uint);
        uint __arm64_flags_left_13531312 = default(uint);
        uint __arm64_flags_left_13531356 = default(uint);
        uint __arm64_flags_left_13531432 = default(uint);
        uint __arm64_flags_left_13531464 = default(uint);
        uint __arm64_flags_right_13531260 = default(uint);
        uint __arm64_flags_right_13531272 = default(uint);
        uint __arm64_flags_right_13531300 = default(uint);
        uint __arm64_flags_right_13531312 = default(uint);
        uint __arm64_flags_right_13531356 = default(uint);
        uint __arm64_flags_right_13531432 = default(uint);
        uint __arm64_flags_right_13531464 = default(uint);
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x22 = default(ulong);
        ulong x23 = default(ulong);
        ulong x24 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFC0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x24);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))), x19);
        x20 = 0x1BAB000UL;
        x22 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x66AUL))))))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0xD8UL))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCE77E8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x278UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x280UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x3D0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x66AUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCE77E8;
        label_0xCE77E8:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x30UL))));
        x0 = RuntimeMemory.ReadU64(x22);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCE77FC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCE77F8UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCE77FC;
        label_0xCE77FC:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1798274UL /* metadata target: Object.op_Implicit */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCE7930;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x3D0UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x280UL))));
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        x20 = RuntimeMemory.ReadU64(x8);
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCE7830;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCE782CUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCE7830;
        label_0xCE7830:
        ;
        x21 = 0x1A8E000UL;
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x278UL))));
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1556240UL /* metadata target: Type.GetTypeFromHandle */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x22);
        x20 = x0;
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCE785C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCE785C;
        label_0xCE785C:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1798B54UL /* metadata target: Object.FindObjectsOfType */, x0, x1, x2, x3);
        x1 = RuntimeMemory.ReadU64(x21);
        x0 = RuntimeCalls.InvokeDirect(0xB7DA60UL, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCE7980;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x18UL))))));
        x20 = x0;
        __arm64_flags_left_13531260 = unchecked((uint)(x8));
        __arm64_flags_right_13531260 = unchecked((uint)0x1UL);
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13531260) - (__arm64_flags_right_13531260))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_13531260)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13531260)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13531260) - (__arm64_flags_right_13531260))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13531260)) < unchecked((int)0x0UL))))))
        {
            goto label_0xCE7930;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x23 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xCE7888;
        label_0xCE7888:
        ;
        __arm64_flags_left_13531272 = unchecked((uint)(x23));
        __arm64_flags_right_13531272 = unchecked((uint)(x8));
        if ((__arm64_flags_left_13531272 >= __arm64_flags_right_13531272))
        {
            goto label_0xCE7984;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x24 = unchecked((ulong)((x20) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x23))) << (int)(unchecked((int)(unchecked((uint)(0x3UL))))))))))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x24) + (0x20UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCE7980;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177BA6CUL /* metadata target: Light.get_type */, x0, x1, x2, x3);
        __arm64_flags_left_13531300 = unchecked((uint)(x0));
        __arm64_flags_right_13531300 = unchecked((uint)0x1UL);
        if ((!((unchecked((uint)((__arm64_flags_left_13531300) - (__arm64_flags_right_13531300))) == unchecked((uint)0x0UL)))))
        {
            goto label_0xCE7920;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x20) + (0x18UL))))));
        __arm64_flags_left_13531312 = unchecked((uint)(x23));
        __arm64_flags_right_13531312 = unchecked((uint)(x8));
        if ((__arm64_flags_left_13531312 >= __arm64_flags_right_13531312))
        {
            goto label_0xCE7984;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(x24);
        if ((x0 == 0x0UL))
        {
            goto label_0xCE7980;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792190UL /* metadata target: Component.get_gameObject */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCE7980;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794D50UL /* metadata target: GameObject.get_activeInHierarchy */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCE7920;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x20) + (0x18UL))))));
        __arm64_flags_left_13531356 = unchecked((uint)(x23));
        __arm64_flags_right_13531356 = unchecked((uint)(x8));
        if ((__arm64_flags_left_13531356 >= __arm64_flags_right_13531356))
        {
            goto label_0xCE7984;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(x24);
        if ((x0 == 0x0UL))
        {
            goto label_0xCE7980;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177BF00UL /* metadata target: Light.get_cookie */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x22);
        x21 = x0;
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCE790C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCE790C;
        label_0xCE790C:
        ;
        x0 = x21;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179568CUL /* metadata target: Object.op_Equality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCE7944;
        }
        else
        {
            goto label_0xCE7920;
        }
        label_0xCE7920:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x20) + (0x18UL))))));
        x23 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x23))) + (unchecked((uint)(0x1UL)))))));
        __arm64_flags_left_13531432 = unchecked((uint)(x23));
        __arm64_flags_right_13531432 = unchecked((uint)(x8));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13531432) - (__arm64_flags_right_13531432))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_13531432)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13531432)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13531432) - (__arm64_flags_right_13531432))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13531432)) < unchecked((int)0x0UL))))))
        {
            goto label_0xCE7888;
        }
        else
        {
            goto label_0xCE7930;
        }
        label_0xCE7930:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        label_0xCE7944:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x20) + (0x18UL))))));
        __arm64_flags_left_13531464 = unchecked((uint)(x23));
        __arm64_flags_right_13531464 = unchecked((uint)(x8));
        if ((__arm64_flags_left_13531464 >= __arm64_flags_right_13531464))
        {
            goto label_0xCE7984;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(x24);
        if ((x0 == 0x0UL))
        {
            goto label_0xCE7980;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792154UL /* metadata target: Component.get_transform */, x0, x1, x2, x3);
        x1 = x0;
        RuntimeMemory.WriteU64(x19, x0);
        x0 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0xB7D8D0UL);
        label_0xCE7980:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        goto label_0xCE7984;
        label_0xCE7984:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB7CUL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `SunShafts.OnRenderImage` — RVA `0xce7988`

- Lift status: **partial**; input span: 1764 bytes; span to next metadata RVA: 1764 bytes.
- Metadata signature: `private void OnRenderImage(RenderTexture source, RenderTexture destination) { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=266 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'csel' at 0xce7aa8; reason: Unknown IR expression at 0xce7aa8; reason: Unsupported instruction 'csel' at 0xce7cd4; reason: Unknown IR expression at 0xce7cd4; reason: Unsupported instruction 'fmul' at 0xce7fac; reason: Unsupported instruction 'mov' at 0xce7fb8; reason: Unsupported instruction 'mov' at 0xce7fbc; reason: Unsupported instruction 'mov' at 0xce7fc0

```csharp
public static ulong SunShafts_OnRenderImage_RVAce7988(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13531800 = default(uint);
        uint __arm64_flags_left_13531808 = default(uint);
        uint __arm64_flags_left_13532352 = default(uint);
        uint __arm64_flags_left_13532584 = default(uint);
        uint __arm64_flags_left_13532592 = default(uint);
        uint __arm64_flags_left_13532692 = default(uint);
        uint __arm64_flags_left_13533000 = default(uint);
        uint __arm64_flags_left_13533196 = default(uint);
        uint __arm64_flags_result_13532352 = default(uint);
        uint __arm64_flags_right_13531800 = default(uint);
        uint __arm64_flags_right_13531808 = default(uint);
        uint __arm64_flags_right_13532352 = default(uint);
        uint __arm64_flags_right_13532584 = default(uint);
        uint __arm64_flags_right_13532592 = default(uint);
        uint __arm64_flags_right_13532692 = default(uint);
        uint __arm64_flags_right_13533000 = default(uint);
        uint __arm64_flags_right_13533196 = default(uint);
        float __arm64_float_flags_left_13533012 = default(float);
        float __arm64_float_flags_right_13533012 = default(float);
        ulong __arm64_load_address_13532032 = default(ulong);
        ulong __arm64_load_address_13533280 = default(ulong);
        ulong __arm64_pair_address_13531532 = default(ulong);
        ulong __arm64_pair_address_13531536 = default(ulong);
        ulong __arm64_pair_address_13532020 = default(ulong);
        ulong __arm64_pair_address_13532024 = default(ulong);
        ulong __arm64_pair_address_13532228 = default(ulong);
        ulong __arm64_pair_address_13532232 = default(ulong);
        ulong __arm64_pair_address_13533268 = default(ulong);
        ulong __arm64_pair_address_13533272 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v10 = default(RuntimeVector128);
        RuntimeVector128 v11 = default(RuntimeVector128);
        RuntimeVector128 v12 = default(RuntimeVector128);
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
        RuntimeMemory.WriteF64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFF70UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v12.GetUInt64(0)))));
        sp = unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFF70UL)));
        __arm64_pair_address_13531532 = unchecked((ulong)((sp) + (0x10UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13531532, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v11.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13531532) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v10.GetUInt64(0)))));
        __arm64_pair_address_13531536 = unchecked((ulong)((sp) + (0x20UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13531536, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13531536) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x0UL))), x29);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x0UL))), x28);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))), x27);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x0UL))), x26);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x8UL))), x25);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x0UL))), x24);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x8UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x70UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x70UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x80UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x80UL)))) + (0x8UL))), x19);
        x19 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x66BUL))))))));
        x29 = x2;
        x20 = x1;
        x21 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCE7A38;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x170UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xC68UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xBA0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xBA8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xBB0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xBB8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xBC0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xBC8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x66BUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCE7A38;
        label_0xCE7A38:
        ;
        x8 = RuntimeMemory.ReadU64(x21);
        x0 = x21;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x178UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x178UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCE7B3C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x68UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCE7A88;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x170UL))));
        x0 = x21;
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xE31BC8UL, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCE8068;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x22 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x176ED24UL /* metadata target: Camera.get_depthTextureMode */, x0, x1, x2, x3);
        x1 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) | (unchecked((uint)(0x1UL)))))));
        x0 = x22;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x176ED60UL /* metadata target: Camera.set_depthTextureMode */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xCE7A88;
        label_0xCE7A88:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x21) + (0x24UL))))));
        x22 = 0x1BAB000UL;
        x10 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x22) + (0x1E1UL))))))));
        x9 = unchecked((ulong)(unchecked((uint)(0x4UL))));
        __arm64_flags_left_13531800 = unchecked((uint)(x8));
        __arm64_flags_right_13531800 = unchecked((uint)0x2UL);
        x9 = unchecked((ulong)(((!((unchecked((uint)((__arm64_flags_left_13531800) - (__arm64_flags_right_13531800))) == unchecked((uint)0x0UL)))) ? unchecked((uint)(x9)) : unchecked((uint)((unchecked((uint)0x0UL)) + (unchecked((uint)0x1UL)))))));
        __arm64_flags_left_13531808 = unchecked((uint)(x8));
        __arm64_flags_right_13531808 = unchecked((uint)0x1UL);
        x8 = unchecked((ulong)(unchecked((uint)(0x2UL))));
        RuntimeCalls.Unsupported("csel", 0xCE7AA8UL);
        x19 = unchecked((ulong)((__Unsupported<bool>("Unknown IR expression") ? unchecked((uint)(x8)) : unchecked((uint)(x9)))));
        if ((unchecked((uint)(x10)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCE7AC4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x1E8UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x22) + (0x1E1UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCE7AC4;
        label_0xCE7AC4:
        ;
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xD8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x30UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCE7AE0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCE7ADCUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xCE7AE0;
        label_0xCE7AE0:
        ;
        x0 = x22;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1798274UL /* metadata target: Object.op_Implicit */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCE7B88;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x170UL))));
        x0 = x21;
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xE31BC8UL, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x30UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCE8068;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x22 = x0;
        x0 = x8;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179D508UL /* metadata target: Transform.get_position */, x0, x1, x2, x3);
        if ((x22 == 0x0UL))
        {
            goto label_0xCE8068;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x22;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x176F6C0UL /* metadata target: Camera.WorldToViewportPoint */, x0, x1, x2, x3);
        v9 = v0;
        v10 = v1;
        v8 = v2;
        goto label_0xCE7B94;
        label_0xCE7B3C:
        ;
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xC68UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCE7B54;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCE7B50UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCE7B54;
        label_0xCE7B54:
        ;
        x0 = x20;
        x1 = x29;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x80UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x80UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x70UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x70UL)))) + (0x8UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x60UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x8UL))));
        x26 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x50UL))));
        x25 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x8UL))));
        x28 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x40UL))));
        x27 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))));
        x29 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))));
        __arm64_pair_address_13532020 = unchecked((ulong)((sp) + (0x20UL)));
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13532020)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13532020) + (0x8UL))))), 0));
        __arm64_pair_address_13532024 = unchecked((ulong)((sp) + (0x10UL)));
        v11 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13532024)), 0));
        v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13532024) + (0x8UL))))), 0));
        x2 = 0x0UL;
        __arm64_load_address_13532032 = sp;
        v12 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_load_address_13532032)), 0));
        sp = unchecked((ulong)((__arm64_load_address_13532032) + (0x90UL)));
        return RuntimeCalls.InvokeDirect(0x1778598UL /* metadata target: Graphics.Blit */);
        label_0xCE7B88:
        ;
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F000000UL)), 0)), 0));
        v10 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F000000UL)), 0)), 0));
        goto label_0xCE7B94;
        label_0xCE7B94:
        ;
        if ((x20 == 0x0UL))
        {
            goto label_0xCE8068;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x20);
        x0 = x20;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x178UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x178UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x20);
        x23 = unchecked((ulong)(unchecked((uint)(unchecked((int)((unchecked((int)(unchecked((uint)(x0))))) / (unchecked((int)(unchecked((uint)(x19)))))))))));
        x0 = x20;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x198UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x198UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        x24 = unchecked((ulong)(unchecked((uint)(unchecked((int)((unchecked((int)(unchecked((uint)(x0))))) / (unchecked((int)(unchecked((uint)(x19)))))))))));
        x0 = unchecked((ulong)(unchecked((uint)(x23))));
        x1 = unchecked((ulong)(unchecked((uint)(x24))));
        x2 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x3 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1783EA0UL /* metadata target: RenderTexture.GetTemporary */, unchecked((ulong)(unchecked((uint)(x0)))), unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x78UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCE8068;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x27 = 0x1A8F000UL;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x21) + (0x5CUL))))), 0));
        x27 = RuntimeMemory.ReadU64(unchecked((ulong)((x27) + (0xBC8UL))));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        x22 = unchecked((ulong)(unchecked((uint)(x0))));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        x1 = RuntimeMemory.ReadU64(x27);
        x0 = x8;
        v1 = v0;
        v3 = v2;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177B76CUL /* metadata target: Material.SetVector */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x78UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCE8068;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x28 = 0x1A8F000UL;
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x21) + (0x64UL))))), 0));
        x28 = RuntimeMemory.ReadU64(unchecked((ulong)((x28) + (0xBC0UL))));
        v0 = v9;
        v1 = v10;
        v2 = v8;
        x1 = RuntimeMemory.ReadU64(x28);
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177B76CUL /* metadata target: Material.SetVector */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x78UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCE8068;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8F000UL;
        __arm64_pair_address_13532228 = unchecked((ulong)((x21) + (0x4CUL)));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13532228)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13532228) + (0x4UL))))), 0));
        __arm64_pair_address_13532232 = unchecked((ulong)((x21) + (0x54UL)));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13532232)), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13532232) + (0x4UL))))), 0));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xBB8UL))));
        x2 = 0x0UL;
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x177B76CUL /* metadata target: Material.SetVector */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x68UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCE7C9C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xC68UL))));
        x25 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x78UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCE7C80;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCE7C7CUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCE7C80;
        label_0xCE7C80:
        ;
        x3 = unchecked((ulong)(unchecked((uint)(0x2UL))));
        x0 = x20;
        x1 = x22;
        x2 = x25;
        x4 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177861CUL /* metadata target: Graphics.Blit */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        goto label_0xCE7D90;
        label_0xCE7C9C:
        ;
        x19 = 0x1A8D000UL;
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x170UL))));
        x0 = x21;
        x1 = RuntimeMemory.ReadU64(x19);
        x0 = RuntimeCalls.InvokeDirect(0xE31BC8UL, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCE8068;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x176E824UL /* metadata target: Camera.get_allowHDR */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x8 = RuntimeMemory.ReadU64(x20);
        __arm64_flags_left_13532352 = unchecked((uint)(x0));
        __arm64_flags_right_13532352 = unchecked((uint)0x1UL);
        __arm64_flags_result_13532352 = unchecked((uint)((__arm64_flags_left_13532352) & (__arm64_flags_right_13532352)));
        x10 = unchecked((ulong)(unchecked((uint)(0x9UL))));
        x0 = x20;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x178UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x178UL)))) + (0x8UL))));
        x8 = unchecked((ulong)(unchecked((uint)(0x7UL))));
        RuntimeCalls.Unsupported("csel", 0xCE7CD4UL);
        x25 = unchecked((ulong)((__Unsupported<bool>("Unknown IR expression") ? unchecked((uint)(x10)) : unchecked((uint)(x8)))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x8 = RuntimeMemory.ReadU64(x20);
        x26 = unchecked((ulong)(unchecked((uint)(x0))));
        x0 = x20;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x198UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x198UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x1 = unchecked((ulong)(unchecked((uint)(x0))));
        x0 = unchecked((ulong)(unchecked((uint)(x26))));
        x2 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x3 = unchecked((ulong)(unchecked((uint)(x25))));
        x4 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1783E74UL /* metadata target: RenderTexture.GetTemporary */, unchecked((ulong)(unchecked((uint)(x0)))), unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x1 = 0x0UL;
        x25 = unchecked((ulong)(unchecked((uint)(x0))));
        x0 = RuntimeCalls.InvokeDirect(0x1782264UL /* metadata target: RenderTexture.set_active */, unchecked((ulong)(unchecked((uint)(x0)))), x1, unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x1 = RuntimeMemory.ReadU64(x19);
        x0 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xE31BC8UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x1 = x0;
        x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1778EDCUL /* metadata target: GL.ClearWithSkybox */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x78UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCE8068;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8F000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xBA0UL))));
        x2 = x25;
        x3 = 0x0UL;
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x177AA8CUL /* metadata target: Material.SetTexture */, x0, x1, x2, x3);
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xC68UL))));
        x26 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x78UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCE7D6C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCE7D68UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCE7D6C;
        label_0xCE7D6C:
        ;
        x3 = unchecked((ulong)(unchecked((uint)(0x3UL))));
        x0 = x20;
        x1 = x22;
        x2 = x26;
        x4 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177861CUL /* metadata target: Graphics.Blit */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x0 = x25;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1782724UL /* metadata target: RenderTexture.ReleaseTemporary */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        goto label_0xCE7D90;
        label_0xCE7D90:
        ;
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x88UL))));
        x1 = x22;
        x0 = RuntimeCalls.InvokeDirect(0xCE6BACUL /* metadata target: PostEffectsBase.DrawBorder */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x21) + (0x38UL))))));
        x9 = unchecked((ulong)(unchecked((uint)(0x4UL))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x78UL))));
        __arm64_flags_left_13532584 = unchecked((uint)(x8));
        __arm64_flags_right_13532584 = unchecked((uint)0x4UL);
        x8 = unchecked((ulong)((((unchecked((int)(unchecked((uint)((__arm64_flags_left_13532584) - (__arm64_flags_right_13532584))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_13532584)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13532584)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13532584) - (__arm64_flags_right_13532584))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13532584)) < unchecked((int)0x0UL))))) ? unchecked((uint)(x8)) : unchecked((uint)(x9)))));
        __arm64_flags_left_13532592 = unchecked((uint)(x8));
        __arm64_flags_right_13532592 = unchecked((uint)0x1UL);
        x8 = unchecked((ulong)((((!((unchecked((uint)((__arm64_flags_left_13532592) - (__arm64_flags_right_13532592))) == unchecked((uint)0x0UL)))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13532592) - (__arm64_flags_right_13532592))))) < unchecked((int)0x0UL)) == (((unchecked((int)(__arm64_flags_left_13532592)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13532592)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13532592) - (__arm64_flags_right_13532592))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13532592)) < unchecked((int)0x0UL)))))) ? unchecked((uint)(x8)) : unchecked((uint)((unchecked((uint)0x0UL)) + (unchecked((uint)0x1UL)))))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x21) + (0x38UL))), unchecked((uint)(x8)));
        if ((x0 == 0x0UL))
        {
            goto label_0xCE8068;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x432000UL;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x21) + (0x5CUL))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x418UL))))), 0));
        x1 = RuntimeMemory.ReadU64(x27);
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v1 = v0;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177B76CUL /* metadata target: Material.SetVector */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x78UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCE8068;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCE7DF0UL);
        }
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x21) + (0x64UL))))), 0));
        x1 = RuntimeMemory.ReadU64(x28);
        v0 = v9;
        v1 = v10;
        v2 = v8;
        x2 = 0x0UL;
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x8UL))), x29);
        x0 = RuntimeCalls.InvokeDirect(0x177B76CUL /* metadata target: Material.SetVector */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x21) + (0x38UL))))));
        __arm64_flags_left_13532692 = unchecked((uint)(x8));
        __arm64_flags_right_13532692 = unchecked((uint)0x1UL);
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13532692) - (__arm64_flags_right_13532692))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_13532692)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13532692)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13532692) - (__arm64_flags_right_13532692))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13532692)) < unchecked((int)0x0UL))))))
        {
            goto label_0xCE7F50;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x29 = 0x1A8D000UL;
        x29 = RuntimeMemory.ReadU64(unchecked((ulong)((x29) + (0xC68UL))));
        x28 = unchecked((ulong)(unchecked((uint)0x0UL)));
        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        v10 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x40C00000UL)), 0)), 0));
        x19 = unchecked((ulong)(unchecked((uint)(0x44400000UL))));
        v11 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x40000000UL)), 0)), 0));
        goto label_0xCE7E38;
        label_0xCE7E38:
        ;
        x0 = unchecked((ulong)(unchecked((uint)(x23))));
        x1 = unchecked((ulong)(unchecked((uint)(x24))));
        x2 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x3 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1783EA0UL /* metadata target: RenderTexture.GetTemporary */, unchecked((ulong)(unchecked((uint)(x0)))), unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x8 = RuntimeMemory.ReadU64(x29);
        x26 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x78UL))));
        x25 = unchecked((ulong)(unchecked((uint)(x0))));
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCE7E68;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xCE7E68;
        label_0xCE7E68:
        ;
        x3 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = x22;
        x1 = x25;
        x2 = x26;
        x4 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177861CUL /* metadata target: Graphics.Blit */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x0 = x22;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1782724UL /* metadata target: RenderTexture.ReleaseTemporary */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x78UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCE8068;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCE7E94UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x21) + (0x5CUL))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)(unchecked((int)(unchecked((uint)(x28))))))), 0));
        v12 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v12.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0))))), 0));
        x1 = RuntimeMemory.ReadU64(x27);
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(x19))), 0)), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        v1 = v0;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177B76CUL /* metadata target: Material.SetVector */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x0 = unchecked((ulong)(unchecked((uint)(x23))));
        x1 = unchecked((ulong)(unchecked((uint)(x24))));
        x2 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x3 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1783EA0UL /* metadata target: RenderTexture.GetTemporary */, unchecked((ulong)(unchecked((uint)(x0)))), unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x78UL))));
        x22 = unchecked((ulong)(unchecked((uint)(x0))));
        x3 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = x25;
        x1 = x22;
        x4 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177861CUL /* metadata target: Graphics.Blit */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x0 = x25;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1782724UL /* metadata target: RenderTexture.ReleaseTemporary */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x78UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCE8068;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCE7F10UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x21) + (0x5CUL))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v12.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0))))), 0));
        x1 = RuntimeMemory.ReadU64(x27);
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(x19))), 0)), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        v1 = v0;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177B76CUL /* metadata target: Material.SetVector */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x21) + (0x38UL))))));
        x28 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x28))) + (unchecked((uint)(0x1UL)))))));
        __arm64_flags_left_13533000 = unchecked((uint)(x28));
        __arm64_flags_right_13533000 = unchecked((uint)(x8));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13533000) - (__arm64_flags_right_13533000))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_13533000)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13533000)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13533000) - (__arm64_flags_right_13533000))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13533000)) < unchecked((int)0x0UL))))))
        {
            goto label_0xCE7E38;
        }
        else
        {
            goto label_0xCE7F50;
        }
        label_0xCE7F50:
        ;
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x78UL))));
        __arm64_float_flags_left_13533012 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13533012 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        if ((__arm64_float_flags_left_13533012 >= __arm64_float_flags_right_13533012))
        {
            goto label_0xCE7F9C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x19 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x67FUL))))))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCE7F80;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xBD0UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x67FUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCE7F80;
        label_0xCE7F80:
        ;
        if ((x23 == 0x0UL))
        {
            goto label_0xCE8068;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8F000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xBD0UL))));
        x8 = RuntimeMemory.ReadU64(x8);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(x8);
#else
        v0 = __ReadVector128(x8);
#endif
        goto label_0xCE7FB0;
        label_0xCE7F9C:
        ;
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        if ((x23 == 0x0UL))
        {
            goto label_0xCE8068;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCE7FA4UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x21) + (0x60UL))))), 0));
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((x21) + (0x3CUL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((x21) + (0x3CUL))));
#endif
        RuntimeCalls.Unsupported("fmul", 0xCE7FACUL);
        goto label_0xCE7FB0;
        label_0xCE7FB0:
        ;
        x8 = 0x1A8F000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xBB0UL))));
        RuntimeCalls.Unsupported("mov", 0xCE7FB8UL);
        RuntimeCalls.Unsupported("mov", 0xCE7FBCUL);
        RuntimeCalls.Unsupported("mov", 0xCE7FC0UL);
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = x23;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177B76CUL /* metadata target: Material.SetVector */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x78UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCE8068;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8F000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xBA8UL))));
        x2 = x22;
        x3 = 0x0UL;
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x177AA8CUL /* metadata target: Material.SetTexture */, x0, x1, x2, x3);
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xC68UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x21) + (0x28UL))))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x78UL))));
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        __arm64_flags_left_13533196 = unchecked((uint)(x8));
        __arm64_flags_right_13533196 = unchecked((uint)0x0UL);
        x8 = unchecked((ulong)(((!((unchecked((uint)((__arm64_flags_left_13533196) - (__arm64_flags_right_13533196))) == unchecked((uint)0x0UL)))) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        x23 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) << (int)(unchecked((int)(unchecked((uint)(0x2UL)))))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCE8020;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCE801CUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCE8020;
        label_0xCE8020:
        ;
        x0 = x20;
        x1 = x24;
        x2 = x21;
        x3 = unchecked((ulong)(unchecked((uint)(x23))));
        x4 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177861CUL /* metadata target: Graphics.Blit */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x0 = x22;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x80UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x80UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x70UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x70UL)))) + (0x8UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x60UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x8UL))));
        x26 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x50UL))));
        x25 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x8UL))));
        x28 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x40UL))));
        x27 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))));
        x29 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))));
        __arm64_pair_address_13533268 = unchecked((ulong)((sp) + (0x20UL)));
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13533268)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13533268) + (0x8UL))))), 0));
        __arm64_pair_address_13533272 = unchecked((ulong)((sp) + (0x10UL)));
        v11 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13533272)), 0));
        v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13533272) + (0x8UL))))), 0));
        x1 = 0x0UL;
        __arm64_load_address_13533280 = sp;
        v12 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_load_address_13533280)), 0));
        sp = unchecked((ulong)((__arm64_load_address_13533280) + (0x90UL)));
        return RuntimeCalls.InvokeDirect(0x1782724UL /* metadata target: RenderTexture.ReleaseTemporary */);
        label_0xCE8068:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        return default(ulong);
    }
```

## `SunShafts.ctor` — RVA `0xce806c`

- Lift status: **partial**; input span: 76 bytes; span to next metadata RVA: 76 bytes.
- Metadata signature: `public void .ctor() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=6 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'fmov' at 0xce806c

```csharp
public static ulong SunShafts_ctor_RVAce806c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        RuntimeVector128 v0 = default(RuntimeVector128);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeCalls.Unsupported("fmov", 0xCE806CUL);
        x9 = 0x432000UL;
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x0) + (0x3CUL))), v0);
#else
        __WriteVector128(unchecked((ulong)((x0) + (0x3CUL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((x9) + (0xDE0UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((x9) + (0xDE0UL))));
#endif
        x9 = unchecked((ulong)(unchecked((uint)(0x2UL))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x0) + (0x38UL))), unchecked((uint)(x9)));
        x9 = 0x431000UL;
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x0) + (0x4CUL))), v0);
#else
        __WriteVector128(unchecked((ulong)((x0) + (0x4CUL))), v0);
#endif
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((x9) + (0xDF0UL))))), 0));
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x9 = unchecked((ulong)(unchecked((uint)(0x3F400000UL))));
        x1 = 0x0UL;
        RuntimeMemory.WriteU32(unchecked((ulong)((x0) + (0x24UL))), unchecked((uint)(x8)));
        RuntimeMemory.WriteU32(unchecked((ulong)((x0) + (0x64UL))), unchecked((uint)(x9)));
        RuntimeMemory.WriteU8(unchecked((ulong)((x0) + (0x68UL))), unchecked((byte)(unchecked((uint)(x8)))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x0) + (0x20UL))), unchecked((byte)(unchecked((uint)(x8)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((x0) + (0x5CUL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x0) + (0x22UL))), unchecked((byte)(unchecked((uint)(x8)))));
        return RuntimeCalls.InvokeDirect(0x1796274UL /* metadata target: MonoBehaviour.ctor */);
        return default(ulong);
    }
```
