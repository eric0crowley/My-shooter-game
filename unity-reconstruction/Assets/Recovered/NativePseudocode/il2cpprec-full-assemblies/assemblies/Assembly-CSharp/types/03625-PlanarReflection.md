# `PlanarReflection` — TypeDefIndex 3625

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x20` | `LayerMask` | `reflectionMask` |
| `0x24` | `bool` | `reflectSkybox` |
| `0x28` | `Color` | `clearColor` |
| `0x38` | `string` | `reflectionSampler` |
| `0x40` | `float` | `clipPlaneOffset` |
| `0x44` | `Vector3` | `m_Oldpos` |
| `0x50` | `Camera` | `m_ReflectionCamera` |
| `0x58` | `Material` | `m_SharedMaterial` |
| `0x60` | `Dictionary<Camera, bool>` | `m_HelperCameras` |

## `PlanarReflection.Start` — RVA `0xce1ec8`

- Lift status: **exact**; input span: 252 bytes; span to next metadata RVA: 252 bytes.
- Metadata signature: `public void Start() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=40 (informational only).

```csharp
public static ulong PlanarReflection_Start_RVAce1ec8(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13508484 = default(uint);
        ulong __arm64_flags_left_13508504 = default(ulong);
        uint __arm64_flags_right_13508484 = default(uint);
        ulong __arm64_flags_right_13508504 = default(ulong);
        ulong sp = default(ulong);
        ulong x10 = default(ulong);
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
        x22 = 0x1BAB000UL;
        x20 = 0x1A8F000UL;
        x21 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x22) + (0x642UL))))))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x9D0UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x3D0UL))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCE1F20;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x3D0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x9D0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x9D8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x22) + (0x642UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCE1F20;
        label_0xCE1F20:
        ;
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792190UL /* metadata target: Component.get_gameObject */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x21);
        x21 = RuntimeMemory.ReadU64(x20);
        x20 = x0;
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCE1F48;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCE1F48;
        label_0xCE1F48:
        ;
        x0 = x21;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1556240UL /* metadata target: Type.GetTypeFromHandle */, x0, x1, x2, x3);
        if ((x20 == 0x0UL))
        {
            goto label_0xCE1FBC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = x0;
        x0 = x20;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792244UL /* metadata target: GameObject.GetComponent */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCE1FBC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = 0x1A8F000UL;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0x9D8UL))));
        x8 = RuntimeMemory.ReadU64(x0);
        x1 = RuntimeMemory.ReadU64(x9);
        x10 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x130UL))))))));
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x1) + (0x130UL))))))));
        __arm64_flags_left_13508484 = unchecked((uint)(x10));
        __arm64_flags_right_13508484 = unchecked((uint)(x9));
        if ((!((__arm64_flags_left_13508484 >= __arm64_flags_right_13508484))))
        {
            goto label_0xCE1FC0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xC8UL))));
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) << (int)(unchecked((int)(unchecked((uint)(0x3UL))))))))))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xFFFFFFFFFFFFFFF8UL))));
        __arm64_flags_left_13508504 = x8;
        __arm64_flags_right_13508504 = x1;
        if ((!((unchecked((ulong)((__arm64_flags_left_13508504) - (__arm64_flags_right_13508504))) == 0x0UL))))
        {
            goto label_0xCE1FC0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x20UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x58UL))), x1);
        x0 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0xB7D8D0UL);
        label_0xCE1FBC:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        goto label_0xCE1FC0;
        label_0xCE1FC0:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DF10UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `PlanarReflection.CreateReflectionCameraFor` — RVA `0xce1fc4`

- Lift status: **partial**; input span: 780 bytes; span to next metadata RVA: 780 bytes.
- Metadata signature: `private Camera CreateReflectionCameraFor(Camera cam) { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=123 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'cinc' at 0xce2240; reason: Unknown IR expression at 0xce2240

```csharp
public static ulong PlanarReflection_CreateReflectionCameraFor_RVAce1fc4(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13509176 = default(uint);
        uint __arm64_flags_right_13509176 = default(uint);
        ulong __arm64_pair_address_13509144 = default(ulong);
        ulong __arm64_pair_address_13509148 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x22 = default(ulong);
        ulong x23 = default(ulong);
        ulong x24 = default(ulong);
        ulong x25 = default(ulong);
        ulong x26 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFB0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x26);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x25);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x24);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))), x19);
        x21 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x643UL))))))));
        x19 = x1;
        x20 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCE2048;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x9E0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x5E0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xBC0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x3F0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x3D0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x9E8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x643UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCE2048;
        label_0xCE2048:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792190UL /* metadata target: Component.get_gameObject */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCE22BC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1798300UL /* metadata target: Object.get_name */, x0, x1, x2, x3);
        if ((x19 == 0x0UL))
        {
            goto label_0xCE22BC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x22 = 0x1A8F000UL;
        x24 = 0x1A8C000UL;
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x9E8UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((x24) + (0xD8UL))));
        x21 = x0;
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1798300UL /* metadata target: Object.get_name */, x0, x1, x2, x3);
        x1 = RuntimeMemory.ReadU64(x22);
        x2 = x0;
        x0 = x21;
        x3 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x13F661CUL /* metadata target: String.Concat */, x0, x1, x2, x3);
        x1 = 0x0UL;
        x22 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x179510CUL /* metadata target: GameObject.Find */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x24);
        x21 = x0;
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCE20BC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCE20BC;
        label_0xCE20BC:
        ;
        x25 = 0x1A8F000UL;
        x26 = 0x1A8C000UL;
        x25 = RuntimeMemory.ReadU64(unchecked((ulong)((x25) + (0x9E0UL))));
        x26 = RuntimeMemory.ReadU64(unchecked((ulong)((x26) + (0x3D0UL))));
        x0 = x21;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1798274UL /* metadata target: Object.op_Implicit */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCE2174;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x3F0UL))));
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xB7D9D4UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = RuntimeMemory.ReadU64(x26);
        x21 = RuntimeMemory.ReadU64(x25);
        x23 = x0;
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCE210C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xCE210C;
        label_0xCE210C:
        ;
        x0 = x21;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1556240UL /* metadata target: Type.GetTypeFromHandle */, x0, x1, x2, x3);
        if ((x23 == 0x0UL))
        {
            goto label_0xCE22BC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x21 = x0;
        if ((x0 == 0x0UL))
        {
            goto label_0xCE2138;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x23);
        x0 = x21;
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x40UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7DA60UL, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCE22C4;
        }
        else
        {
            goto label_0xCE2138;
        }
        label_0xCE2138:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x23) + (0x18UL))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCE22C0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x23;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x20UL))), x21);
        x1 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xBC0UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = x22;
        x2 = x23;
        x3 = 0x0UL;
        x21 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x1794FFCUL /* metadata target: GameObject.ctor */, x0, x1, x2, x3);
        goto label_0xCE2174;
        label_0xCE2174:
        ;
        x0 = RuntimeMemory.ReadU64(x26);
        x22 = RuntimeMemory.ReadU64(x25);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCE2188;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCE2184UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCE2188;
        label_0xCE2188:
        ;
        x0 = x22;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1556240UL /* metadata target: Type.GetTypeFromHandle */, x0, x1, x2, x3);
        if ((x21 == 0x0UL))
        {
            goto label_0xCE22BC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = x0;
        x0 = x21;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792244UL /* metadata target: GameObject.GetComponent */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x24);
        x22 = x0;
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCE21C0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCE21C0;
        label_0xCE21C0:
        ;
        x23 = 0x1A8E000UL;
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0x5E0UL))));
        x0 = x22;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1798274UL /* metadata target: Object.op_Implicit */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCE2208;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(x26);
        x22 = RuntimeMemory.ReadU64(x25);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCE21EC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCE21E8UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCE21EC;
        label_0xCE21EC:
        ;
        x0 = x22;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1556240UL /* metadata target: Type.GetTypeFromHandle */, x0, x1, x2, x3);
        x1 = x0;
        x0 = x21;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794BD0UL /* metadata target: GameObject.AddComponent */, x0, x1, x2, x3);
        goto label_0xCE2208;
        label_0xCE2208:
        ;
        x1 = RuntimeMemory.ReadU64(x23);
        x0 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xE49224UL, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCE22BC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCE2218UL);
        }
        __arm64_pair_address_13509144 = unchecked((ulong)((x20) + (0x30UL)));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13509144)), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13509144) + (0x4UL))))), 0));
        __arm64_pair_address_13509148 = unchecked((ulong)((x20) + (0x28UL)));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13509148)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13509148) + (0x4UL))))), 0));
        x1 = 0x0UL;
        x21 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x176EC0CUL /* metadata target: Camera.set_backgroundColor */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x24UL))))))));
        x0 = x21;
        x2 = 0x0UL;
        __arm64_flags_left_13509176 = unchecked((uint)(x8));
        __arm64_flags_right_13509176 = unchecked((uint)0x0UL);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeCalls.Unsupported("cinc", 0xCE2240UL);
        x1 = unchecked((ulong)((__Unsupported<bool>("Unknown IR expression") ? unchecked((uint)((unchecked((uint)(x8))) + (unchecked((uint)0x1UL)))) : unchecked((uint)(x8)))));
        x0 = RuntimeCalls.InvokeDirect(0x176ECE0UL /* metadata target: Camera.set_clearFlags */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x2 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x20) + (0x20UL))))));
        x1 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xCE22D0UL /* metadata target: PlanarReflection.SetStandardCameraParameter */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = x21;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x176EF54UL /* metadata target: Camera.get_targetTexture */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x8 = RuntimeMemory.ReadU64(x24);
        x20 = x0;
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCE2278;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xCE2278;
        label_0xCE2278:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1798274UL /* metadata target: Object.op_Implicit */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCE22A0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xCE2384UL /* metadata target: PlanarReflection.CreateTextureFor */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x1 = x0;
        x0 = x21;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x176EF90UL /* metadata target: Camera.set_targetTexture */, x0, x1, x2, x3);
        goto label_0xCE22A0;
        label_0xCE22A0:
        ;
        x0 = x21;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x40UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x26 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x25 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        label_0xCE22BC:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        goto label_0xCE22C0;
        label_0xCE22C0:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB7CUL, x0, x1, x2, x3);
        goto label_0xCE22C4;
        label_0xCE22C4:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB98UL, x0, x1, x2, x3);
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xB7DA4CUL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `PlanarReflection.SetStandardCameraParameter` — RVA `0xce22d0`

- Lift status: **exact**; input span: 180 bytes; span to next metadata RVA: 180 bytes.
- Metadata signature: `private void SetStandardCameraParameter(Camera cam, LayerMask mask) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=27 (informational only).

```csharp
public static ulong PlanarReflection_SetStandardCameraParameter_RVAce22d0(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
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
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x22) + (0x644UL))))))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xB0UL))));
        x20 = x2;
        x19 = x1;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCE230C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB0UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x22) + (0x644UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCE230C;
        label_0xCE230C:
        ;
        x0 = unchecked((ulong)((x20) & (0xFFFFFFFFUL)));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179515CUL /* metadata target: LayerMask.op_Implicit */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x21);
        x20 = unchecked((ulong)(unchecked((uint)(x0))));
        x1 = 0x0UL;
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0x17951ACUL /* metadata target: LayerMask.NameToLayer */, x0, x1, x2, x3);
        if ((x19 == 0x0UL))
        {
            goto label_0xCE2380;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) << (int)(unchecked((int)(unchecked((uint)(x0)))))))));
        x1 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x20))) & ((~(unchecked((uint)(x8)))))))));
        x0 = x19;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x176EA68UL /* metadata target: Camera.set_cullingMask */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x176EC0CUL /* metadata target: Camera.set_backgroundColor */, x0, x1, x2, x3);
        x0 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x2 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0x1791660UL /* metadata target: Behaviour.set_enabled */);
        label_0xCE2380:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        return default(ulong);
    }
```

## `PlanarReflection.CreateTextureFor` — RVA `0xce2384`

- Lift status: **partial**; input span: 348 bytes; span to next metadata RVA: 348 bytes.
- Metadata signature: `private RenderTexture CreateTextureFor(Camera cam) { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=44 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'frintm' at 0xce2410; reason: Unsupported instruction 'fcvtms' at 0xce2418; reason: Unsupported instruction 'csel' at 0xce242c; reason: Unknown IR expression at 0xce242c; reason: Unsupported instruction 'frintm' at 0xce247c; reason: Unsupported instruction 'fcvtms' at 0xce2484; reason: Unsupported instruction 'csel' at 0xce2490; reason: Unknown IR expression at 0xce2490

```csharp
public static ulong PlanarReflection_CreateTextureFor_RVAce2384(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        float __arm64_float_flags_left_13509660 = default(float);
        float __arm64_float_flags_left_13509768 = default(float);
        float __arm64_float_flags_right_13509660 = default(float);
        float __arm64_float_flags_right_13509768 = default(float);
        ulong __arm64_pair_address_13509508 = default(ulong);
        ulong __arm64_pair_address_13509844 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        RuntimeVector128 v9 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x22 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        __arm64_pair_address_13509508 = unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFC0UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13509508, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13509508) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        sp = __arm64_pair_address_13509508;
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x10UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))), x19);
        x20 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x645UL))))))));
        x19 = x1;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
        }
        else
        {
            x0 = 0x1A8E000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xEB0UL))));
            // Likely IL2CPP class initialization helper (guarded call).
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
            RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x645UL))), unchecked((byte)(unchecked((uint)(x8)))));
        }
        label_0xCE23B8:
        ;
        if ((x19 == 0x0UL))
        {
        }
        else
        {
            x0 = x19;
            x1 = 0x0UL;
            x0 = RuntimeCalls.InvokeDirect(0x176EEDCUL /* metadata target: Camera.get_pixelWidth */, x0, x1, x2, x3);
            x21 = 0x1BAB000UL;
            x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x2CCUL))))))));
            v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)(unchecked((int)(unchecked((uint)(x0))))))), 0));
            v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F000000UL)), 0)), 0));
            if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
            {
            }
            else
            {
                x0 = 0x1A8C000UL;
                x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xA60UL))));
                // Likely IL2CPP class initialization helper (guarded call).
                x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
                x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
                RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x2CCUL))), unchecked((byte)(unchecked((uint)(x8)))));
            }
            label_0xCE23F0:
            ;
            x22 = 0x1A8C000UL;
            x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0xA60UL))));
            v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0))))), 0));
            x0 = RuntimeMemory.ReadU64(x22);
            x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
            if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
            {
            }
            else
            {
                x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
            }
            label_0xCE240C:
            ;
            x8 = unchecked((ulong)(unchecked((uint)(0x7F800000UL))));
            RuntimeCalls.Unsupported("frintm", 0xCE2410UL);
            v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(x8))), 0)), 0));
            RuntimeCalls.Unsupported("fcvtms", 0xCE2418UL);
            __arm64_float_flags_left_13509660 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
            __arm64_float_flags_right_13509660 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
            x8 = unchecked((ulong)(unchecked((uint)(0xFFFFFFFF80000000UL))));
            x0 = x19;
            x1 = 0x0UL;
            RuntimeCalls.Unsupported("csel", 0xCE242CUL);
            x20 = unchecked((ulong)((__Unsupported<bool>("Unknown IR expression") ? unchecked((uint)(x8)) : unchecked((uint)(x9)))));
            x0 = RuntimeCalls.InvokeDirect(0x176EF18UL /* metadata target: Camera.get_pixelHeight */, x0, x1, x2, x3);
            x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x2CCUL))))))));
            v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)(unchecked((int)(unchecked((uint)(x0))))))), 0));
            v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F000000UL)), 0)), 0));
            if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
            {
            }
            else
            {
                x0 = 0x1A8C000UL;
                x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xA60UL))));
                // Likely IL2CPP class initialization helper (guarded call).
                x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
                x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
                RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x2CCUL))), unchecked((byte)(unchecked((uint)(x8)))));
            }
            label_0xCE2458:
            ;
            x0 = RuntimeMemory.ReadU64(x22);
            x19 = 0x1A8E000UL;
            v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0))))), 0));
            x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
            x19 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xEB0UL))));
            if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
            {
            }
            else
            {
                x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
            }
            label_0xCE2474:
            ;
            x0 = RuntimeMemory.ReadU64(x19);
            x9 = unchecked((ulong)(unchecked((uint)(0x7F800000UL))));
            RuntimeCalls.Unsupported("frintm", 0xCE247CUL);
            v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(x9))), 0)), 0));
            RuntimeCalls.Unsupported("fcvtms", 0xCE2484UL);
            __arm64_float_flags_left_13509768 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
            __arm64_float_flags_right_13509768 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
            x9 = unchecked((ulong)(unchecked((uint)(0xFFFFFFFF80000000UL))));
            RuntimeCalls.Unsupported("csel", 0xCE2490UL);
            x21 = unchecked((ulong)((__Unsupported<bool>("Unknown IR expression") ? unchecked((uint)(x9)) : unchecked((uint)(x8)))));
            x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
            x3 = unchecked((ulong)(unchecked((uint)(0x18UL))));
            x1 = unchecked((ulong)(unchecked((uint)(x20))));
            x2 = unchecked((ulong)(unchecked((uint)(x21))));
            x4 = 0x0UL;
            x19 = x0;
            x0 = RuntimeCalls.InvokeDirect(0x1783954UL /* metadata target: RenderTexture.ctor */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
            if ((x19 == 0x0UL))
            {
            }
            else
            {
                x1 = unchecked((ulong)(unchecked((uint)(0x34UL))));
                x0 = x19;
                x2 = 0x0UL;
                x0 = RuntimeCalls.InvokeDirect(0x1798C88UL /* metadata target: Object.set_hideFlags */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, unchecked((ulong)(unchecked((uint)(x3)))));
                x0 = x19;
                x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
                x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))));
                x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
                x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
                x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
                __arm64_pair_address_13509844 = sp;
                v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13509844)), 0));
                v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13509844) + (0x8UL))))), 0));
                sp = unchecked((ulong)((__arm64_pair_address_13509844) + (0x40UL)));
                return x0;
            }
        }
        label_0xCE24DC:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, unchecked((ulong)(unchecked((uint)(x3)))));
        return default(ulong);
    }
```

## `PlanarReflection.RenderHelpCameras` — RVA `0xce24e0`

- Lift status: **exact**; input span: 440 bytes; span to next metadata RVA: 440 bytes.
- Metadata signature: `public void RenderHelpCameras(Camera currentCam) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=73 (informational only).

```csharp
public static ulong PlanarReflection_RenderHelpCameras_RVAce24e0(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
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
        x21 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x646UL))))))));
        x19 = x1;
        x20 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCE255C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x9F0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x9F8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xA00UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xA08UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xA10UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xA18UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x646UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCE255C;
        label_0xCE255C:
        ;
        x21 = x20;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x60UL))));
        if ((x0 != 0x0UL))
        {
            goto label_0xCE25A4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8F000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xA18UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x8 = 0x1A8F000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xA00UL))));
        x22 = x0;
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xEA78F8UL, x0, x1, x2, x3);
        x0 = x21;
        x1 = x22;
        RuntimeMemory.WriteU64(x21, x22);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x21);
        if ((x0 == 0x0UL))
        {
            goto label_0xCE2694;
        }
        else
        {
            goto label_0xCE25A4;
        }
        label_0xCE25A4:
        ;
        x8 = 0x1A8F000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x9F8UL))));
        x1 = x19;
        x2 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xEA7DF4UL, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCE25DC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(x21);
        if ((x0 == 0x0UL))
        {
            goto label_0xCE2694;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8F000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x9F0UL))));
        x1 = x19;
        x2 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x3 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xEA7BECUL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xCE25DC;
        label_0xCE25DC:
        ;
        x0 = RuntimeMemory.ReadU64(x21);
        if ((x0 == 0x0UL))
        {
            goto label_0xCE2694;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8F000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xA08UL))));
        x1 = x19;
        x2 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xEA7B60UL, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCE260C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        label_0xCE260C:
        ;
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xD8UL))));
        x21 = x20;
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x50UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCE262C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCE2628UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCE262C;
        label_0xCE262C:
        ;
        x0 = x22;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1798274UL /* metadata target: Object.op_Implicit */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCE2658;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x20;
        x1 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xCE1FC4UL /* metadata target: PlanarReflection.CreateReflectionCameraFor */, x0, x1, x2, x3);
        x1 = x0;
        RuntimeMemory.WriteU64(unchecked((ulong)((x20) + (0x50UL))), x0);
        x0 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        goto label_0xCE2658;
        label_0xCE2658:
        ;
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x50UL))));
        x0 = x20;
        x1 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xCE2698UL /* metadata target: PlanarReflection.RenderReflectionFor */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x60UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCE2694;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8F000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xA10UL))));
        x1 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x3 = RuntimeMemory.ReadU64(x8);
        x2 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0xEA7BD4UL);
        label_0xCE2694:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        return default(ulong);
    }
```

## `PlanarReflection.RenderReflectionFor` — RVA `0xce2698`

- Lift status: **exact**; input span: 1692 bytes; span to next metadata RVA: 1692 bytes.
- Metadata signature: `private void RenderReflectionFor(Camera cam, Camera reflectCamera) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=246 (informational only).

```csharp
public static uint PlanarReflection_RenderReflectionFor_RVAce2698(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13510660 = default(uint);
        ulong __arm64_flags_left_13510908 = default(ulong);
        ulong __arm64_flags_left_13511036 = default(ulong);
        ulong __arm64_flags_left_13511104 = default(ulong);
        uint __arm64_flags_right_13510660 = default(uint);
        ulong __arm64_flags_right_13510908 = default(ulong);
        ulong __arm64_flags_right_13511036 = default(ulong);
        ulong __arm64_flags_right_13511104 = default(ulong);
        ulong __arm64_pair_address_13510296 = default(ulong);
        ulong __arm64_pair_address_13510300 = default(ulong);
        ulong __arm64_pair_address_13510304 = default(ulong);
        ulong __arm64_pair_address_13510308 = default(ulong);
        ulong __arm64_pair_address_13510448 = default(ulong);
        ulong __arm64_pair_address_13510452 = default(ulong);
        ulong __arm64_pair_address_13510456 = default(ulong);
        ulong __arm64_pair_address_13510460 = default(ulong);
        ulong __arm64_pair_address_13510628 = default(ulong);
        ulong __arm64_pair_address_13510632 = default(ulong);
        ulong __arm64_pair_address_13511432 = default(ulong);
        ulong __arm64_pair_address_13511436 = default(ulong);
        ulong __arm64_pair_address_13511448 = default(ulong);
        ulong __arm64_pair_address_13511452 = default(ulong);
        ulong __arm64_pair_address_13511456 = default(ulong);
        ulong __arm64_pair_address_13511460 = default(ulong);
        ulong __arm64_pair_address_13511516 = default(ulong);
        ulong __arm64_pair_address_13511556 = default(ulong);
        ulong __arm64_pair_address_13511560 = default(ulong);
        ulong __arm64_pair_address_13511572 = default(ulong);
        ulong __arm64_pair_address_13511576 = default(ulong);
        ulong __arm64_pair_address_13511580 = default(ulong);
        ulong __arm64_pair_address_13511584 = default(ulong);
        ulong __arm64_pair_address_13511596 = default(ulong);
        ulong __arm64_pair_address_13511600 = default(ulong);
        ulong __arm64_pair_address_13511608 = default(ulong);
        ulong __arm64_pair_address_13511612 = default(ulong);
        ulong __arm64_pair_address_13511628 = default(ulong);
        ulong __arm64_pair_address_13511632 = default(ulong);
        ulong __arm64_pair_address_13511712 = default(ulong);
        ulong __arm64_pair_address_13511716 = default(ulong);
        ulong __arm64_pair_address_13511728 = default(ulong);
        ulong __arm64_pair_address_13511732 = default(ulong);
        ulong __arm64_pair_address_13511736 = default(ulong);
        ulong __arm64_pair_address_13511740 = default(ulong);
        ulong __arm64_pair_address_13511764 = default(ulong);
        ulong __arm64_pair_address_13511768 = default(ulong);
        ulong __arm64_pair_address_13511784 = default(ulong);
        ulong __arm64_pair_address_13511788 = default(ulong);
        ulong __arm64_pair_address_13511956 = default(ulong);
        ulong __arm64_pair_address_13511960 = default(ulong);
        ulong __arm64_pair_address_13511964 = default(ulong);
        ulong __arm64_pair_address_13511968 = default(ulong);
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
        ulong x24 = default(ulong);
        ulong x25 = default(ulong);
        ulong x26 = default(ulong);
        ulong x27 = default(ulong);
        ulong x29 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        __arm64_pair_address_13510296 = unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFF60UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13510296, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v15.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13510296) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v14.GetUInt64(0)))));
        sp = __arm64_pair_address_13510296;
        __arm64_pair_address_13510300 = unchecked((ulong)((sp) + (0x10UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13510300, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v13.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13510300) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v12.GetUInt64(0)))));
        __arm64_pair_address_13510304 = unchecked((ulong)((sp) + (0x20UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13510304, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v11.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13510304) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v10.GetUInt64(0)))));
        __arm64_pair_address_13510308 = unchecked((ulong)((sp) + (0x30UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13510308, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13510308) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x40UL))), x29);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x8UL))), x27);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x0UL))), x26);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x8UL))), x25);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x70UL)))) + (0x0UL))), x24);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x70UL)))) + (0x8UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x80UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x80UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x90UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x90UL)))) + (0x8UL))), x19);
        sp = unchecked((ulong)((sp) - (0x240UL)));
        x22 = 0x1BAB000UL;
        x24 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x22) + (0x64BUL))))))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((x24) + (0xD8UL))));
        x19 = x2;
        x20 = x1;
        x21 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCE2728;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xA20UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xA28UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x3D0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x22) + (0x64BUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCE2728;
        label_0xCE2728:
        ;
        x0 = RuntimeMemory.ReadU64(x24);
        v0 = (RuntimeVector128.Zero.WithUInt64(0, 0x0UL) | RuntimeVector128.Zero.WithUInt64(0, 0x0UL).ShiftLeftLogical(unchecked((int)0x40UL)));
        __arm64_pair_address_13510448 = unchecked((ulong)((sp) + (0x220UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13510448, v0);
#else
        __WriteVector128(__arm64_pair_address_13510448, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13510448) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13510448) + (0x10UL))), v0);
#endif
        __arm64_pair_address_13510452 = unchecked((ulong)((sp) + (0x200UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13510452, v0);
#else
        __WriteVector128(__arm64_pair_address_13510452, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13510452) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13510452) + (0x10UL))), v0);
#endif
        __arm64_pair_address_13510456 = unchecked((ulong)((sp) + (0x1E0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13510456, v0);
#else
        __WriteVector128(__arm64_pair_address_13510456, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13510456) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13510456) + (0x10UL))), v0);
#endif
        __arm64_pair_address_13510460 = unchecked((ulong)((sp) + (0x1C0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13510460, v0);
#else
        __WriteVector128(__arm64_pair_address_13510460, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13510460) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13510460) + (0x10UL))), v0);
#endif
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCE274C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xCE2748UL)));
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCE274C;
        label_0xCE274C:
        ;
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1798274UL /* metadata target: Object.op_Implicit */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCE2CF8;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(x24);
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x58UL))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCE2770;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xCE276CUL)));
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCE2770;
        label_0xCE2770:
        ;
        x0 = x22;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1798274UL /* metadata target: Object.op_Implicit */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCE2798;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x58UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCE2D28;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x38UL))));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177AD80UL /* metadata target: Material.HasProperty */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCE2CF8;
        }
        else
        {
            goto label_0xCE2798;
        }
        label_0xCE2798:
        ;
        x0 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x21) + (0x20UL))))));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179515CUL /* metadata target: LayerMask.op_Implicit */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB0UL))));
        x22 = unchecked((ulong)(unchecked((uint)(x0))));
        x1 = 0x0UL;
        x8 = RuntimeMemory.ReadU64(x8);
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0x17951ACUL /* metadata target: LayerMask.NameToLayer */, x0, x1, x2, x3);
        if ((x19 == 0x0UL))
        {
            goto label_0xCE2D28;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x23 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x23))) << (int)(unchecked((int)(unchecked((uint)(x0)))))))));
        x1 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x22))) & ((~(unchecked((uint)(x8)))))))));
        x0 = x19;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x176EA68UL /* metadata target: Camera.set_cullingMask */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x1 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xCE2F34UL /* metadata target: PlanarReflection.SaneCameraSettings */, x0, x1, x2, x3);
        __arm64_pair_address_13510628 = unchecked((ulong)((x21) + (0x28UL)));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13510628)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13510628) + (0x4UL))))), 0));
        __arm64_pair_address_13510632 = unchecked((ulong)((x21) + (0x30UL)));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13510632)), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13510632) + (0x4UL))))), 0));
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x176EC0CUL /* metadata target: Camera.set_backgroundColor */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x24UL))))))));
        x0 = x19;
        x2 = 0x0UL;
        __arm64_flags_left_13510660 = unchecked((uint)(x8));
        __arm64_flags_right_13510660 = unchecked((uint)0x0UL);
        x1 = unchecked((ulong)(((unchecked((uint)((__arm64_flags_left_13510660) - (__arm64_flags_right_13510660))) == unchecked((uint)0x0UL)) ? unchecked((uint)((unchecked((uint)(x23))) + (unchecked((uint)0x1UL)))) : unchecked((uint)(x23)))));
        x0 = RuntimeCalls.InvokeDirect(0x176ECE0UL /* metadata target: Camera.set_clearFlags */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x24UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCE29E4;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xCE2818UL)));
        }
        if ((x20 == 0x0UL))
        {
            goto label_0xCE2D28;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792190UL /* metadata target: Component.get_gameObject */, x0, x1, x2, x3);
        x26 = 0x1A8C000UL;
        x26 = RuntimeMemory.ReadU64(unchecked((ulong)((x26) + (0x3D0UL))));
        x25 = 0x1A8F000UL;
        x22 = x0;
        x8 = RuntimeMemory.ReadU64(x26);
        x25 = RuntimeMemory.ReadU64(unchecked((ulong)((x25) + (0xA20UL))));
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0xE0UL))))));
        x23 = RuntimeMemory.ReadU64(x25);
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCE2854;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCE2854;
        label_0xCE2854:
        ;
        x0 = x23;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1556240UL /* metadata target: Type.GetTypeFromHandle */, x0, x1, x2, x3);
        if ((x22 == 0x0UL))
        {
            goto label_0xCE2D28;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = x0;
        x0 = x22;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792244UL /* metadata target: GameObject.GetComponent */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x24);
        x22 = x0;
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCE288C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCE288C;
        label_0xCE288C:
        ;
        x0 = x22;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1798274UL /* metadata target: Object.op_Implicit */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCE29E4;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792190UL /* metadata target: Component.get_gameObject */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x26);
        x23 = RuntimeMemory.ReadU64(x25);
        x22 = x0;
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCE28C4;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCE28C4;
        label_0xCE28C4:
        ;
        x0 = x23;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1556240UL /* metadata target: Type.GetTypeFromHandle */, x0, x1, x2, x3);
        if ((x22 == 0x0UL))
        {
            goto label_0xCE2D28;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = x0;
        x0 = x22;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792244UL /* metadata target: GameObject.GetComponent */, x0, x1, x2, x3);
        x27 = 0x1A8F000UL;
        x27 = RuntimeMemory.ReadU64(unchecked((ulong)((x27) + (0xA28UL))));
        x22 = x0;
        if ((x0 == 0x0UL))
        {
            goto label_0xCE2904;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = RuntimeMemory.ReadU64(x27);
        x8 = RuntimeMemory.ReadU64(x22);
        __arm64_flags_left_13510908 = x8;
        __arm64_flags_right_13510908 = x1;
        if ((!((unchecked((ulong)((__arm64_flags_left_13510908) - (__arm64_flags_right_13510908))) == 0x0UL))))
        {
            goto label_0xCE2D2C;
        }
        else
        {
            goto label_0xCE2904;
        }
        label_0xCE2904:
        ;
        x0 = RuntimeMemory.ReadU64(x24);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCE2914;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xCE2910UL)));
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCE2914;
        label_0xCE2914:
        ;
        x0 = x22;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1798274UL /* metadata target: Object.op_Implicit */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCE2984;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792190UL /* metadata target: Component.get_gameObject */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x26);
        x23 = RuntimeMemory.ReadU64(x25);
        x22 = x0;
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCE294C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCE294C;
        label_0xCE294C:
        ;
        x0 = x23;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1556240UL /* metadata target: Type.GetTypeFromHandle */, x0, x1, x2, x3);
        if ((x22 == 0x0UL))
        {
            goto label_0xCE2D28;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = x0;
        x0 = x22;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794BD0UL /* metadata target: GameObject.AddComponent */, x0, x1, x2, x3);
        x22 = x0;
        if ((x0 == 0x0UL))
        {
            goto label_0xCE2984;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = RuntimeMemory.ReadU64(x27);
        x8 = RuntimeMemory.ReadU64(x22);
        __arm64_flags_left_13511036 = x8;
        __arm64_flags_right_13511036 = x1;
        if ((!((unchecked((ulong)((__arm64_flags_left_13511036) - (__arm64_flags_right_13511036))) == 0x0UL))))
        {
            goto label_0xCE2D2C;
        }
        else
        {
            goto label_0xCE2984;
        }
        label_0xCE2984:
        ;
        x0 = RuntimeMemory.ReadU64(x26);
        x23 = RuntimeMemory.ReadU64(x25);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCE2998;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xCE2994UL)));
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCE2998;
        label_0xCE2998:
        ;
        x0 = x23;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1556240UL /* metadata target: Type.GetTypeFromHandle */, x0, x1, x2, x3);
        x1 = x0;
        x0 = x20;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17921CCUL /* metadata target: Component.GetComponent */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCE2D28;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = RuntimeMemory.ReadU64(x27);
        x8 = RuntimeMemory.ReadU64(x0);
        __arm64_flags_left_13511104 = x8;
        __arm64_flags_right_13511104 = x1;
        if ((!((unchecked((ulong)((__arm64_flags_left_13511104) - (__arm64_flags_right_13511104))) == 0x0UL))))
        {
            goto label_0xCE2D30;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177BF88UL /* metadata target: Skybox.get_material */, x0, x1, x2, x3);
        if ((x22 == 0x0UL))
        {
            goto label_0xCE2D28;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = x0;
        x0 = x22;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177BFC4UL /* metadata target: Skybox.set_material */, x0, x1, x2, x3);
        goto label_0xCE29E4;
        label_0xCE29E4:
        ;
        x0 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1778A44UL /* metadata target: GL.set_invertCulling */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        x0 = x21;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792154UL /* metadata target: Component.get_transform */, x0, x1, x2, x3);
        if ((x20 == 0x0UL))
        {
            goto label_0xCE2D28;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x22 = x0;
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792154UL /* metadata target: Component.get_transform */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCE2D28;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179D6C8UL /* metadata target: Transform.get_eulerAngles */, x0, x1, x2, x3);
        x0 = x19;
        x1 = 0x0UL;
        v10 = v0;
        v8 = v1;
        v9 = v2;
        x0 = RuntimeCalls.InvokeDirect(0x1792154UL /* metadata target: Component.get_transform */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCE2D28;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xCE2A38UL)));
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes((-(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0)))), 0));
        v1 = v8;
        v2 = v9;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179D748UL /* metadata target: Transform.set_eulerAngles */, x0, x1, x2, x3);
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792154UL /* metadata target: Component.get_transform */, x0, x1, x2, x3);
        x23 = x0;
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792154UL /* metadata target: Component.get_transform */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCE2D28;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179D508UL /* metadata target: Transform.get_position */, x0, x1, x2, x3);
        if ((x23 == 0x0UL))
        {
            goto label_0xCE2D28;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = x23;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179D5A8UL /* metadata target: Transform.set_position */, x0, x1, x2, x3);
        if ((x22 == 0x0UL))
        {
            goto label_0xCE2D28;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = x22;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792154UL /* metadata target: Component.get_transform */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCE2D28;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179D508UL /* metadata target: Transform.get_position */, x0, x1, x2, x3);
        x0 = x22;
        x1 = 0x0UL;
        v8 = v0;
        v9 = v2;
        x0 = RuntimeCalls.InvokeDirect(0x179D508UL /* metadata target: Transform.get_position */, x0, x1, x2, x3);
        x0 = x22;
        x1 = 0x0UL;
        v10 = v1;
        x0 = RuntimeCalls.InvokeDirect(0x1792154UL /* metadata target: Component.get_transform */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCE2D28;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179D940UL /* metadata target: Transform.get_up */, x0, x1, x2, x3);
        v11 = v0;
        v12 = v1;
        v13 = v2;
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x21) + (0x40UL))))), 0));
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1787350UL /* metadata target: Matrix4x4.get_zero */, x0, x1, x2, x3);
        __arm64_pair_address_13511432 = unchecked((ulong)((sp) + (0x1A0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(__arm64_pair_address_13511432);
#else
        v1 = __ReadVector128(__arm64_pair_address_13511432);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13511432) + (0x10UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13511432) + (0x10UL))));
#endif
        __arm64_pair_address_13511436 = unchecked((ulong)((sp) + (0x180UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v3 = RuntimeMemory.ReadVector128(__arm64_pair_address_13511436);
#else
        v3 = __ReadVector128(__arm64_pair_address_13511436);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v2 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13511436) + (0x10UL))));
#else
        v2 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13511436) + (0x10UL))));
#endif
        x0 = unchecked((ulong)((sp) + (0x140UL)));
        __arm64_pair_address_13511448 = unchecked((ulong)((sp) + (0x220UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13511448, v1);
#else
        __WriteVector128(__arm64_pair_address_13511448, v1);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13511448) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13511448) + (0x10UL))), v0);
#endif
        __arm64_pair_address_13511452 = unchecked((ulong)((sp) + (0x200UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13511452, v3);
#else
        __WriteVector128(__arm64_pair_address_13511452, v3);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13511452) + (0x10UL))), v2);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13511452) + (0x10UL))), v2);
#endif
        __arm64_pair_address_13511456 = unchecked((ulong)((sp) + (0x140UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13511456, v3);
#else
        __WriteVector128(__arm64_pair_address_13511456, v3);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13511456) + (0x10UL))), v2);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13511456) + (0x10UL))), v2);
#endif
        __arm64_pair_address_13511460 = unchecked((ulong)((sp) + (0x160UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13511460, v1);
#else
        __WriteVector128(__arm64_pair_address_13511460, v1);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13511460) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13511460) + (0x10UL))), v0);
#endif
        v0 = v11;
        v1 = v12;
        v2 = v13;
        x0 = RuntimeCalls.InvokeDirect(0xCE2F94UL /* metadata target: PlanarReflection.CalculateReflectionMatrix */, x0, x1, x2, x3);
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792154UL /* metadata target: Component.get_transform */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCE2D28;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179D508UL /* metadata target: Transform.get_position */, x0, x1, x2, x3);
        x0 = unchecked((ulong)((sp) + (0x200UL)));
        x1 = 0x0UL;
        __arm64_pair_address_13511516 = unchecked((ulong)((x21) + (0x44UL)));
        RuntimeMemory.WriteF32(__arm64_pair_address_13511516, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_13511516) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((x21) + (0x4CUL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0));
        x0 = RuntimeCalls.InvokeDirect(0x178716CUL /* metadata target: Matrix4x4.MultiplyPoint */, x0, x1, x2, x3);
        x0 = x20;
        x1 = 0x0UL;
        v14 = v0;
        v15 = v1;
        RuntimeMemory.WriteF32(unchecked((ulong)((sp) + (0x28CUL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0));
        x0 = RuntimeCalls.InvokeDirect(0x176F010UL /* metadata target: Camera.get_worldToCameraMatrix */, x0, x1, x2, x3);
        __arm64_pair_address_13511556 = unchecked((ulong)((sp) + (0x180UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13511556);
#else
        v0 = __ReadVector128(__arm64_pair_address_13511556);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13511556) + (0x10UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13511556) + (0x10UL))));
#endif
        __arm64_pair_address_13511560 = unchecked((ulong)((sp) + (0x1A0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v2 = RuntimeMemory.ReadVector128(__arm64_pair_address_13511560);
#else
        v2 = __ReadVector128(__arm64_pair_address_13511560);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v3 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13511560) + (0x10UL))));
#else
        v3 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13511560) + (0x10UL))));
#endif
        x0 = unchecked((ulong)((sp) + (0x100UL)));
        __arm64_pair_address_13511572 = unchecked((ulong)((sp) + (0x100UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13511572, v0);
#else
        __WriteVector128(__arm64_pair_address_13511572, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13511572) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13511572) + (0x10UL))), v1);
#endif
        __arm64_pair_address_13511576 = unchecked((ulong)((sp) + (0x200UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13511576);
#else
        v0 = __ReadVector128(__arm64_pair_address_13511576);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13511576) + (0x10UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13511576) + (0x10UL))));
#endif
        __arm64_pair_address_13511580 = unchecked((ulong)((sp) + (0x120UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13511580, v2);
#else
        __WriteVector128(__arm64_pair_address_13511580, v2);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13511580) + (0x10UL))), v3);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13511580) + (0x10UL))), v3);
#endif
        __arm64_pair_address_13511584 = unchecked((ulong)((sp) + (0x220UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v2 = RuntimeMemory.ReadVector128(__arm64_pair_address_13511584);
#else
        v2 = __ReadVector128(__arm64_pair_address_13511584);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v3 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13511584) + (0x10UL))));
#else
        v3 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13511584) + (0x10UL))));
#endif
        x1 = unchecked((ulong)((sp) + (0xC0UL)));
        x2 = 0x0UL;
        __arm64_pair_address_13511596 = unchecked((ulong)((sp) + (0xC0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13511596, v0);
#else
        __WriteVector128(__arm64_pair_address_13511596, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13511596) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13511596) + (0x10UL))), v1);
#endif
        __arm64_pair_address_13511600 = unchecked((ulong)((sp) + (0xE0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13511600, v2);
#else
        __WriteVector128(__arm64_pair_address_13511600, v2);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13511600) + (0x10UL))), v3);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13511600) + (0x10UL))), v3);
#endif
        x0 = RuntimeCalls.InvokeDirect(0x1786E8CUL /* metadata target: Matrix4x4.op_Multiply */, x0, x1, x2, x3);
        __arm64_pair_address_13511608 = unchecked((ulong)((sp) + (0x180UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13511608);
#else
        v0 = __ReadVector128(__arm64_pair_address_13511608);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13511608) + (0x10UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13511608) + (0x10UL))));
#endif
        __arm64_pair_address_13511612 = unchecked((ulong)((sp) + (0x1A0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v2 = RuntimeMemory.ReadVector128(__arm64_pair_address_13511612);
#else
        v2 = __ReadVector128(__arm64_pair_address_13511612);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v3 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13511612) + (0x10UL))));
#else
        v3 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13511612) + (0x10UL))));
#endif
        x1 = unchecked((ulong)((sp) + (0x80UL)));
        x0 = x19;
        x2 = 0x0UL;
        __arm64_pair_address_13511628 = unchecked((ulong)((sp) + (0x80UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13511628, v0);
#else
        __WriteVector128(__arm64_pair_address_13511628, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13511628) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13511628) + (0x10UL))), v1);
#endif
        __arm64_pair_address_13511632 = unchecked((ulong)((sp) + (0xA0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13511632, v2);
#else
        __WriteVector128(__arm64_pair_address_13511632, v2);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13511632) + (0x10UL))), v3);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13511632) + (0x10UL))), v3);
#endif
        x0 = RuntimeCalls.InvokeDirect(0x176F0C0UL /* metadata target: Camera.set_worldToCameraMatrix */, x0, x1, x2, x3);
        x0 = x21;
        x1 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xCE303CUL /* metadata target: PlanarReflection.CameraSpacePlane */, x0, x1, x2, x3);
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x176F148UL /* metadata target: Camera.get_projectionMatrix */, x0, x1, x2, x3);
        __arm64_pair_address_13511712 = unchecked((ulong)((sp) + (0x1A0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(__arm64_pair_address_13511712);
#else
        v1 = __ReadVector128(__arm64_pair_address_13511712);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13511712) + (0x10UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13511712) + (0x10UL))));
#endif
        __arm64_pair_address_13511716 = unchecked((ulong)((sp) + (0x180UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v3 = RuntimeMemory.ReadVector128(__arm64_pair_address_13511716);
#else
        v3 = __ReadVector128(__arm64_pair_address_13511716);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v2 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13511716) + (0x10UL))));
#else
        v2 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13511716) + (0x10UL))));
#endif
        x0 = unchecked((ulong)((sp) + (0x40UL)));
        __arm64_pair_address_13511728 = unchecked((ulong)((sp) + (0x1E0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13511728, v1);
#else
        __WriteVector128(__arm64_pair_address_13511728, v1);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13511728) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13511728) + (0x10UL))), v0);
#endif
        __arm64_pair_address_13511732 = unchecked((ulong)((sp) + (0x1C0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13511732, v3);
#else
        __WriteVector128(__arm64_pair_address_13511732, v3);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13511732) + (0x10UL))), v2);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13511732) + (0x10UL))), v2);
#endif
        __arm64_pair_address_13511736 = unchecked((ulong)((sp) + (0x40UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13511736, v3);
#else
        __WriteVector128(__arm64_pair_address_13511736, v3);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13511736) + (0x10UL))), v2);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13511736) + (0x10UL))), v2);
#endif
        __arm64_pair_address_13511740 = unchecked((ulong)((sp) + (0x60UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13511740, v1);
#else
        __WriteVector128(__arm64_pair_address_13511740, v1);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13511740) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13511740) + (0x10UL))), v0);
#endif
        x0 = RuntimeCalls.InvokeDirect(0xCE31E4UL /* metadata target: PlanarReflection.CalculateObliqueMatrix */, x0, x1, x2, x3);
        __arm64_pair_address_13511764 = unchecked((ulong)((sp) + (0x1C0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13511764);
#else
        v0 = __ReadVector128(__arm64_pair_address_13511764);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13511764) + (0x10UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13511764) + (0x10UL))));
#endif
        __arm64_pair_address_13511768 = unchecked((ulong)((sp) + (0x1E0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v2 = RuntimeMemory.ReadVector128(__arm64_pair_address_13511768);
#else
        v2 = __ReadVector128(__arm64_pair_address_13511768);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v3 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13511768) + (0x10UL))));
#else
        v3 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13511768) + (0x10UL))));
#endif
        x1 = sp;
        x0 = x19;
        x2 = 0x0UL;
        __arm64_pair_address_13511784 = sp;
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13511784, v0);
#else
        __WriteVector128(__arm64_pair_address_13511784, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13511784) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13511784) + (0x10UL))), v1);
#endif
        __arm64_pair_address_13511788 = unchecked((ulong)((sp) + (0x20UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13511788, v2);
#else
        __WriteVector128(__arm64_pair_address_13511788, v2);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13511788) + (0x10UL))), v3);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13511788) + (0x10UL))), v3);
#endif
        x0 = RuntimeCalls.InvokeDirect(0x176F1F8UL /* metadata target: Camera.set_projectionMatrix */, x0, x1, x2, x3);
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792154UL /* metadata target: Component.get_transform */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCE2D28;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xCE2C84UL)));
        }
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((sp) + (0x28CUL))))), 0));
        v0 = v14;
        v1 = v15;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179D5A8UL /* metadata target: Transform.set_position */, x0, x1, x2, x3);
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792154UL /* metadata target: Component.get_transform */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCE2D28;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179D6C8UL /* metadata target: Transform.get_eulerAngles */, x0, x1, x2, x3);
        x0 = x19;
        x1 = 0x0UL;
        v10 = v0;
        v8 = v1;
        v9 = v2;
        x0 = RuntimeCalls.InvokeDirect(0x1792154UL /* metadata target: Component.get_transform */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCE2D28;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179D748UL /* metadata target: Transform.set_eulerAngles */, x0, x1, x2, x3);
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x176FA90UL /* metadata target: Camera.Render */, x0, x1, x2, x3);
        x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1778A44UL /* metadata target: GL.set_invertCulling */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        goto label_0xCE2CF8;
        label_0xCE2CF8:
        ;
        sp = unchecked((ulong)((sp) + (0x240UL)));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x90UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x90UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x80UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x80UL)))) + (0x8UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x70UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x70UL)))) + (0x8UL))));
        x26 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x60UL))));
        x25 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x50UL))));
        x27 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x8UL))));
        x29 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x40UL))));
        __arm64_pair_address_13511956 = unchecked((ulong)((sp) + (0x30UL)));
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13511956)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13511956) + (0x8UL))))), 0));
        __arm64_pair_address_13511960 = unchecked((ulong)((sp) + (0x20UL)));
        v11 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13511960)), 0));
        v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13511960) + (0x8UL))))), 0));
        __arm64_pair_address_13511964 = unchecked((ulong)((sp) + (0x10UL)));
        v13 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13511964)), 0));
        v12 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13511964) + (0x8UL))))), 0));
        __arm64_pair_address_13511968 = sp;
        v15 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13511968)), 0));
        v14 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13511968) + (0x8UL))))), 0));
        return unchecked((uint)(x0));
        label_0xCE2D28:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        goto label_0xCE2D2C;
        label_0xCE2D2C:
        ;
        x0 = x22;
        goto label_0xCE2D30;
        label_0xCE2D30:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DF10UL, x0, x1, x2, x3);
        return default(uint);
    }
```

## `PlanarReflection.LateUpdate` — RVA `0xce2d34`

- Lift status: **exact**; input span: 88 bytes; span to next metadata RVA: 88 bytes.
- Metadata signature: `public void LateUpdate() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=14 (informational only).

```csharp
public static ulong PlanarReflection_LateUpdate_RVAce2d34(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        x20 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x647UL))))))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCE2D60;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xA30UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x647UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCE2D60;
        label_0xCE2D60:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x60UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCE2D80;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8F000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xA30UL))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x1 = RuntimeMemory.ReadU64(x8);
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0xEA7D88UL);
        label_0xCE2D80:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        return default(ulong);
    }
```

## `PlanarReflection.WaterTileBeingRendered` — RVA `0xce2d8c`

- Lift status: **exact**; input span: 224 bytes; span to next metadata RVA: 224 bytes.
- Metadata signature: `public void WaterTileBeingRendered(Transform tr, Camera currentCam) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=35 (informational only).

```csharp
public static ulong PlanarReflection_WaterTileBeingRendered_RVAce2d8c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
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
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x22) + (0x648UL))))))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xD8UL))));
        x20 = x2;
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCE2DC8;
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
        RuntimeMemory.WriteU8(unchecked((ulong)((x22) + (0x648UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCE2DC8;
        label_0xCE2DC8:
        ;
        x0 = x19;
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xCE24E0UL /* metadata target: PlanarReflection.RenderHelpCameras */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x21);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x50UL))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCE2DE8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCE2DE4UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCE2DE8;
        label_0xCE2DE8:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1798274UL /* metadata target: Object.op_Implicit */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCE2E58;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(x21);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x58UL))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCE2E0C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCE2E08UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCE2E0C;
        label_0xCE2E0C:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1798274UL /* metadata target: Object.op_Implicit */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCE2E58;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x50UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCE2E68;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x58UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x38UL))));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x176EF54UL /* metadata target: Camera.get_targetTexture */, x0, x1, x2, x3);
        if ((x20 == 0x0UL))
        {
            goto label_0xCE2E68;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x2 = x0;
        x0 = x20;
        x1 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x3 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0x177AA8CUL /* metadata target: Material.SetTexture */);
        label_0xCE2E58:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        label_0xCE2E68:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `PlanarReflection.OnEnable` — RVA `0xce2e6c`

- Lift status: **exact**; input span: 100 bytes; span to next metadata RVA: 100 bytes.
- Metadata signature: `public void OnEnable() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=17 (informational only).

```csharp
public static ulong PlanarReflection_OnEnable_RVAce2e6c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
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
        x20 = 0x1BAB000UL;
        x21 = 0x1A8F000UL;
        x19 = 0x1A8F000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x649UL))))))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xA38UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xA40UL))));
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCE2EB0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xA38UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xA40UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x649UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCE2EB0;
        label_0xCE2EB0:
        ;
        x0 = RuntimeMemory.ReadU64(x21);
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177A16CUL /* metadata target: Shader.EnableKeyword */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x19);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x1 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeDirect(0x177A1A8UL /* metadata target: Shader.DisableKeyword */);
        return default(ulong);
    }
```

## `PlanarReflection.OnDisable` — RVA `0xce2ed0`

- Lift status: **exact**; input span: 100 bytes; span to next metadata RVA: 100 bytes.
- Metadata signature: `public void OnDisable() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=17 (informational only).

```csharp
public static ulong PlanarReflection_OnDisable_RVAce2ed0(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
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
        x20 = 0x1BAB000UL;
        x21 = 0x1A8F000UL;
        x19 = 0x1A8F000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x64AUL))))))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xA40UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xA38UL))));
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCE2F14;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xA38UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xA40UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x64AUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCE2F14;
        label_0xCE2F14:
        ;
        x0 = RuntimeMemory.ReadU64(x21);
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177A16CUL /* metadata target: Shader.EnableKeyword */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x19);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x1 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeDirect(0x177A1A8UL /* metadata target: Shader.DisableKeyword */);
        return default(ulong);
    }
```

## `PlanarReflection.SaneCameraSettings` — RVA `0xce2f34`

- Lift status: **exact**; input span: 96 bytes; span to next metadata RVA: 96 bytes.
- Metadata signature: `private void SaneCameraSettings(Camera helperCam) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=13 (informational only).

```csharp
public static ulong PlanarReflection_SaneCameraSettings_RVAce2f34(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x8UL))), x19);
        if ((x1 == 0x0UL))
        {
            goto label_0xCE2F90;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x19 = x1;
        x0 = x1;
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x176ED60UL /* metadata target: Camera.set_depthTextureMode */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x176EC0CUL /* metadata target: Camera.set_backgroundColor */, x0, x1, x2, x3);
        x1 = unchecked((ulong)(unchecked((uint)(0x2UL))));
        x0 = x19;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x176ECE0UL /* metadata target: Camera.set_clearFlags */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = x19;
        x2 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeDirect(0x176E7A4UL /* metadata target: Camera.set_renderingPath */);
        label_0xCE2F90:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        return default(ulong);
    }
```

## `PlanarReflection.CalculateReflectionMatrix` — RVA `0xce2f94`

- Lift status: **exact**; input span: 168 bytes; span to next metadata RVA: 168 bytes.
- Metadata signature: `private static Matrix4x4 CalculateReflectionMatrix(Matrix4x4 reflectionMat, Vector4 plane) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static ulong PlanarReflection_CalculateReflectionMatrix_RVAce2f94(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_pair_address_13512696 = default(ulong);
        ulong __arm64_pair_address_13512700 = default(ulong);
        ulong __arm64_pair_address_13512720 = default(ulong);
        ulong __arm64_pair_address_13512724 = default(ulong);
        ulong __arm64_pair_address_13512744 = default(ulong);
        ulong __arm64_pair_address_13512748 = default(ulong);
        ulong __arm64_pair_address_13512752 = default(ulong);
        ulong __arm64_pair_address_13512756 = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v16 = default(RuntimeVector128);
        RuntimeVector128 v17 = default(RuntimeVector128);
        RuntimeVector128 v18 = default(RuntimeVector128);
        RuntimeVector128 v19 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v20 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
        RuntimeVector128 v4 = default(RuntimeVector128);
        RuntimeVector128 v5 = default(RuntimeVector128);
        RuntimeVector128 v6 = default(RuntimeVector128);
        RuntimeVector128 v7 = default(RuntimeVector128);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v6 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0xC0000000UL)), 0)), 0));
        v7 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v16 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
        v5 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0))))), 0));
        v17 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v6.GetUInt64(0)))), 0))))), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v6.GetUInt64(0)))), 0))))), 0));
        v18 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v6.GetUInt64(0)))), 0))))), 0));
        v7 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v7.GetUInt64(0)))), 0))))), 0));
        v6 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v6.GetUInt64(0)))), 0))))), 0));
        v16 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v16.GetUInt64(0)))), 0))))), 0));
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v5.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0))))), 0));
        v19 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v17.GetUInt64(0)))), 0))))), 0));
        v17 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v17.GetUInt64(0)))), 0))))), 0));
        v20 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0))))), 0));
        v7 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v5.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v7.GetUInt64(0)))), 0))))), 0));
        v5 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v5.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v16.GetUInt64(0)))), 0))))), 0));
        v16 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v18.GetUInt64(0)))), 0))))), 0));
        v18 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v18.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v6.GetUInt64(0)))), 0))))), 0));
        v6 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v6.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0))))), 0));
        x9 = unchecked((ulong)(unchecked((uint)(0x3F800000UL))));
        __arm64_pair_address_13512696 = x0;
        RuntimeMemory.WriteF32(__arm64_pair_address_13512696, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_13512696) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v16.GetUInt64(0)))), 0));
        __arm64_pair_address_13512700 = unchecked((ulong)((x0) + (0x10UL)));
        RuntimeMemory.WriteF32(__arm64_pair_address_13512700, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v19.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_13512700) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v7.GetUInt64(0)))), 0));
        RuntimeMemory.WritePtr(unchecked((ulong)((x0) + (0xCUL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        RuntimeMemory.WritePtr(unchecked((ulong)((x0) + (0x1CUL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        RuntimeMemory.WritePtr(unchecked((ulong)((x0) + (0x2CUL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x0) + (0x3CUL))), unchecked((uint)(x9)));
        __arm64_pair_address_13512720 = unchecked((ulong)((x0) + (0x20UL)));
        RuntimeMemory.WriteF32(__arm64_pair_address_13512720, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v17.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_13512720) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v18.GetUInt64(0)))), 0));
        __arm64_pair_address_13512724 = unchecked((ulong)((x0) + (0x30UL)));
        RuntimeMemory.WriteF32(__arm64_pair_address_13512724, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v20.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_13512724) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((x0) + (0x8UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((x0) + (0x28UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v5.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((x0) + (0x38UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((x0) + (0x18UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v6.GetUInt64(0)))), 0));
        __arm64_pair_address_13512744 = unchecked((ulong)((x0) + (0x20UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13512744);
#else
        v0 = __ReadVector128(__arm64_pair_address_13512744);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13512744) + (0x10UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13512744) + (0x10UL))));
#endif
        __arm64_pair_address_13512748 = x0;
#if IL2CPPREC_RUNTIME_VECTOR128
        v2 = RuntimeMemory.ReadVector128(__arm64_pair_address_13512748);
#else
        v2 = __ReadVector128(__arm64_pair_address_13512748);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v3 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13512748) + (0x10UL))));
#else
        v3 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13512748) + (0x10UL))));
#endif
        __arm64_pair_address_13512752 = unchecked((ulong)((x8) + (0x20UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13512752, v0);
#else
        __WriteVector128(__arm64_pair_address_13512752, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13512752) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13512752) + (0x10UL))), v1);
#endif
        __arm64_pair_address_13512756 = x8;
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13512756, v2);
#else
        __WriteVector128(__arm64_pair_address_13512756, v2);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13512756) + (0x10UL))), v3);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13512756) + (0x10UL))), v3);
#endif
        return x0;
        return default(ulong);
    }
```

## `PlanarReflection.CameraSpacePlane` — RVA `0xce303c`

- Lift status: **exact**; input span: 424 bytes; span to next metadata RVA: 424 bytes.
- Metadata signature: `private Vector4 CameraSpacePlane(Camera cam, Vector3 pos, Vector3 normal, float sideSign) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=54 (informational only).

```csharp
public static ulong PlanarReflection_CameraSpacePlane_RVAce303c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        float __arm64_float_flags_left_13513040 = default(float);
        float __arm64_float_flags_right_13513040 = default(float);
        ulong __arm64_pair_address_13512772 = default(ulong);
        ulong __arm64_pair_address_13512776 = default(ulong);
        ulong __arm64_pair_address_13512780 = default(ulong);
        ulong __arm64_pair_address_13512796 = default(ulong);
        ulong __arm64_pair_address_13512800 = default(ulong);
        ulong __arm64_pair_address_13512864 = default(ulong);
        ulong __arm64_pair_address_13512868 = default(ulong);
        ulong __arm64_pair_address_13512880 = default(ulong);
        ulong __arm64_pair_address_13512884 = default(ulong);
        ulong __arm64_pair_address_13513112 = default(ulong);
        ulong __arm64_pair_address_13513152 = default(ulong);
        ulong __arm64_pair_address_13513156 = default(ulong);
        ulong __arm64_pair_address_13513160 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v10 = default(RuntimeVector128);
        RuntimeVector128 v11 = default(RuntimeVector128);
        RuntimeVector128 v12 = default(RuntimeVector128);
        RuntimeVector128 v13 = default(RuntimeVector128);
        RuntimeVector128 v14 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
        RuntimeVector128 v4 = default(RuntimeVector128);
        RuntimeVector128 v5 = default(RuntimeVector128);
        RuntimeVector128 v6 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        RuntimeVector128 v9 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        sp = unchecked((ulong)((sp) - (0xD0UL)));
        RuntimeMemory.WriteF64(unchecked((ulong)((sp) + (0x80UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v14.GetUInt64(0)))));
        __arm64_pair_address_13512772 = unchecked((ulong)((sp) + (0x90UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13512772, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v13.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13512772) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v12.GetUInt64(0)))));
        __arm64_pair_address_13512776 = unchecked((ulong)((sp) + (0xA0UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13512776, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v11.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13512776) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v10.GetUInt64(0)))));
        __arm64_pair_address_13512780 = unchecked((ulong)((sp) + (0xB0UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13512780, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13512780) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xC0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xC0UL)))) + (0x8UL))), x19);
        v14 = v3;
        v3 = (RuntimeVector128.Zero.WithUInt64(0, 0x0UL) | RuntimeVector128.Zero.WithUInt64(0, 0x0UL).ShiftLeftLogical(unchecked((int)0x40UL)));
        __arm64_pair_address_13512796 = unchecked((ulong)((sp) + (0x60UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13512796, v3);
#else
        __WriteVector128(__arm64_pair_address_13512796, v3);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13512796) + (0x10UL))), v3);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13512796) + (0x10UL))), v3);
#endif
        __arm64_pair_address_13512800 = unchecked((ulong)((sp) + (0x40UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13512800, v3);
#else
        __WriteVector128(__arm64_pair_address_13512800, v3);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13512800) + (0x10UL))), v3);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13512800) + (0x10UL))), v3);
#endif
        if ((x1 == 0x0UL))
        {
            label_0xCE31E0:
            ;
            x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        }
        else
        {
            v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x0) + (0x40UL))))), 0));
            v13 = v4;
            v12 = v5;
            v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v5.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0))))), 0));
            v5 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v13.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0))))), 0));
            v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v14.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0))))), 0));
            x0 = x1;
            x1 = 0x0UL;
            v8 = v6;
            v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0))))), 0));
            v10 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v5.GetUInt64(0)))), 0))))), 0));
            v11 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0))))), 0));
            x0 = RuntimeCalls.InvokeDirect(0x176F010UL /* metadata target: Camera.get_worldToCameraMatrix */, x0, x1, x2, x3);
            __arm64_pair_address_13512864 = sp;
#if IL2CPPREC_RUNTIME_VECTOR128
            v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13512864);
#else
            v0 = __ReadVector128(__arm64_pair_address_13512864);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
            v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13512864) + (0x10UL))));
#else
            v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13512864) + (0x10UL))));
#endif
            __arm64_pair_address_13512868 = unchecked((ulong)((sp) + (0x20UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
            v2 = RuntimeMemory.ReadVector128(__arm64_pair_address_13512868);
#else
            v2 = __ReadVector128(__arm64_pair_address_13512868);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
            v3 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13512868) + (0x10UL))));
#else
            v3 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13512868) + (0x10UL))));
#endif
            x0 = unchecked((ulong)((sp) + (0x40UL)));
            x1 = 0x0UL;
            __arm64_pair_address_13512880 = unchecked((ulong)((sp) + (0x40UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
            RuntimeMemory.WriteVector128(__arm64_pair_address_13512880, v0);
#else
            __WriteVector128(__arm64_pair_address_13512880, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
            RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13512880) + (0x10UL))), v1);
#else
            __WriteVector128(unchecked((ulong)((__arm64_pair_address_13512880) + (0x10UL))), v1);
#endif
            __arm64_pair_address_13512884 = unchecked((ulong)((sp) + (0x60UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
            RuntimeMemory.WriteVector128(__arm64_pair_address_13512884, v2);
#else
            __WriteVector128(__arm64_pair_address_13512884, v2);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
            RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13512884) + (0x10UL))), v3);
#else
            __WriteVector128(unchecked((ulong)((__arm64_pair_address_13512884) + (0x10UL))), v3);
#endif
            v0 = v11;
            v1 = v10;
            v2 = v9;
            x0 = RuntimeCalls.InvokeDirect(0x178716CUL /* metadata target: Matrix4x4.MultiplyPoint */, x0, x1, x2, x3);
            v10 = v0;
            v11 = v1;
            v9 = v2;
            x0 = unchecked((ulong)((sp) + (0x40UL)));
            v0 = v14;
            v1 = v13;
            v2 = v12;
            x1 = 0x0UL;
            x0 = RuntimeCalls.InvokeDirect(0x1787244UL /* metadata target: Matrix4x4.MultiplyVector */, x0, x1, x2, x3);
            x19 = 0x1BAB000UL;
            x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x2C8UL))))))));
            v12 = v0;
            v13 = v1;
            v14 = v2;
            if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
            {
            }
            else
            {
                x0 = 0x1A8C000UL;
                x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xA60UL))));
                // Likely IL2CPP class initialization helper (guarded call).
                x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
                x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
                RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x2C8UL))), unchecked((byte)(unchecked((uint)(x8)))));
            }
            label_0xCE3118:
            ;
            x8 = 0x1A8C000UL;
            x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xA60UL))));
            x0 = RuntimeMemory.ReadU64(x8);
            x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
            if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
            {
            }
            else
            {
                x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
            }
            label_0xCE3130:
            ;
            v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v12.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v12.GetUInt64(0)))), 0))))), 0));
            v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v13.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v13.GetUInt64(0)))), 0))))), 0));
            x8 = 0x432000UL;
            v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
            v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x41CUL))))), 0));
            v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v14.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v14.GetUInt64(0)))), 0))))), 0));
            v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
            v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)(global::System.Math.Sqrt(unchecked((double)(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))))), 0));
            __arm64_float_flags_left_13513040 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0);
            __arm64_float_flags_right_13513040 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
            if (((__arm64_float_flags_left_13513040 <= __arm64_float_flags_right_13513040) || ((__arm64_float_flags_left_13513040 != __arm64_float_flags_left_13513040) || (__arm64_float_flags_right_13513040 != __arm64_float_flags_right_13513040))))
            {
                label_0xCE3168:
                ;
                x19 = 0x1BAB000UL;
                x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x2C9UL))))))));
                if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
                {
                }
                else
                {
                    x0 = 0x1A8C000UL;
                    x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x1E8UL))));
                    // Likely IL2CPP class initialization helper (guarded call).
                    x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
                    x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
                    RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x2C9UL))), unchecked((byte)(unchecked((uint)(x8)))));
                }
                label_0xCE3188:
                ;
                x8 = 0x1A8C000UL;
                x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x1E8UL))));
                x8 = RuntimeMemory.ReadU64(x8);
                x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
                __arm64_pair_address_13513112 = x8;
                v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13513112)), 0));
                v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13513112) + (0x4UL))))), 0));
                v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x8UL))))), 0));
            }
            else
            {
                v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v12.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
                v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v13.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
                v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v14.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
            }
            label_0xCE31A0:
            ;
            x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0xC0UL))));
            x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xC0UL)))) + (0x8UL))));
            __arm64_pair_address_13513152 = unchecked((ulong)((sp) + (0xB0UL)));
            v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13513152)), 0));
            v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13513152) + (0x8UL))))), 0));
            __arm64_pair_address_13513156 = unchecked((ulong)((sp) + (0xA0UL)));
            v11 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13513156)), 0));
            v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13513156) + (0x8UL))))), 0));
            __arm64_pair_address_13513160 = unchecked((ulong)((sp) + (0x90UL)));
            v13 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13513160)), 0));
            v12 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13513160) + (0x8UL))))), 0));
            v14 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((sp) + (0x80UL))))), 0));
            return x0;
        }
        return default(ulong);
    }
```

## `PlanarReflection.CalculateObliqueMatrix` — RVA `0xce31e4`

- Lift status: **partial**; input span: 392 bytes; span to next metadata RVA: 392 bytes.
- Metadata signature: `private static Matrix4x4 CalculateObliqueMatrix(Matrix4x4 projection, Vector4 clipPlane) { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=38 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'b.mi' at 0xce3240; reason: Unknown IR expression at 0xce3240; reason: Unsupported instruction 'b.mi' at 0xce3254; reason: Unknown IR expression at 0xce3254

```csharp
public static ulong PlanarReflection_CalculateObliqueMatrix_RVAce31e4(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        float __arm64_float_flags_left_13513256 = default(float);
        float __arm64_float_flags_left_13513288 = default(float);
        float __arm64_float_flags_right_13513256 = default(float);
        float __arm64_float_flags_right_13513288 = default(float);
        ulong __arm64_pair_address_13513192 = default(ulong);
        ulong __arm64_pair_address_13513196 = default(ulong);
        ulong __arm64_pair_address_13513244 = default(ulong);
        ulong __arm64_pair_address_13513248 = default(ulong);
        ulong __arm64_pair_address_13513260 = default(ulong);
        ulong __arm64_pair_address_13513268 = default(ulong);
        ulong __arm64_pair_address_13513308 = default(ulong);
        ulong __arm64_pair_address_13513312 = default(ulong);
        ulong __arm64_pair_address_13513324 = default(ulong);
        ulong __arm64_pair_address_13513336 = default(ulong);
        ulong __arm64_pair_address_13513540 = default(ulong);
        ulong __arm64_pair_address_13513544 = default(ulong);
        ulong __arm64_pair_address_13513552 = default(ulong);
        ulong __arm64_pair_address_13513556 = default(ulong);
        ulong __arm64_pair_address_13513560 = default(ulong);
        ulong __arm64_pair_address_13513568 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v10 = default(RuntimeVector128);
        RuntimeVector128 v11 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
        RuntimeVector128 v4 = default(RuntimeVector128);
        RuntimeVector128 v5 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        RuntimeVector128 v9 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        sp = unchecked((ulong)((sp) - (0x100UL)));
        __arm64_pair_address_13513192 = unchecked((ulong)((sp) + (0xC0UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13513192, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v11.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13513192) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v10.GetUInt64(0)))));
        __arm64_pair_address_13513196 = unchecked((ulong)((sp) + (0xD0UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13513196, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13513196) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xE0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xF0UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xF0UL)))) + (0x8UL))), x19);
        x19 = x8;
        x8 = unchecked((ulong)((sp) + (0x40UL)));
        x1 = 0x0UL;
        v8 = v3;
        v9 = v2;
        v10 = v1;
        v11 = v0;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x17864E0UL /* metadata target: Matrix4x4.get_inverse */, x0, x1, x2, x3);
        __arm64_pair_address_13513244 = unchecked((ulong)((sp) + (0x40UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13513244);
#else
        v0 = __ReadVector128(__arm64_pair_address_13513244);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v2 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13513244) + (0x10UL))));
#else
        v2 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13513244) + (0x10UL))));
#endif
        __arm64_pair_address_13513248 = unchecked((ulong)((sp) + (0x60UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v3 = RuntimeMemory.ReadVector128(__arm64_pair_address_13513248);
#else
        v3 = __ReadVector128(__arm64_pair_address_13513248);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v4 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13513248) + (0x10UL))));
#else
        v4 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13513248) + (0x10UL))));
#endif
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        __arm64_float_flags_left_13513256 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13513256 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        __arm64_pair_address_13513260 = unchecked((ulong)((sp) + (0x80UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13513260, v0);
#else
        __WriteVector128(__arm64_pair_address_13513260, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13513260) + (0x10UL))), v2);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13513260) + (0x10UL))), v2);
#endif
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        __arm64_pair_address_13513268 = unchecked((ulong)((sp) + (0xA0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13513268, v3);
#else
        __WriteVector128(__arm64_pair_address_13513268, v3);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13513268) + (0x10UL))), v4);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13513268) + (0x10UL))), v4);
#endif
        if ((__arm64_float_flags_left_13513256 > __arm64_float_flags_right_13513256))
        {
        }
        else
        {
            v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0xBF800000UL)), 0)), 0));
            RuntimeCalls.Unsupported("b.mi", 0xCE3240UL);
            if (__Unsupported<bool>("Unknown IR expression"))
            {
            }
            else
            {
                v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
            }
        }
        label_0xCE3248:
        ;
        __arm64_float_flags_left_13513288 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13513288 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        if ((__arm64_float_flags_left_13513288 > __arm64_float_flags_right_13513288))
        {
        }
        else
        {
            v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0xBF800000UL)), 0)), 0));
            RuntimeCalls.Unsupported("b.mi", 0xCE3254UL);
            if (__Unsupported<bool>("Unknown IR expression"))
            {
            }
            else
            {
                v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
            }
        }
        label_0xCE325C:
        ;
        __arm64_pair_address_13513308 = unchecked((ulong)((sp) + (0x80UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v2 = RuntimeMemory.ReadVector128(__arm64_pair_address_13513308);
#else
        v2 = __ReadVector128(__arm64_pair_address_13513308);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v3 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13513308) + (0x10UL))));
#else
        v3 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13513308) + (0x10UL))));
#endif
        __arm64_pair_address_13513312 = unchecked((ulong)((sp) + (0xA0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v4 = RuntimeMemory.ReadVector128(__arm64_pair_address_13513312);
#else
        v4 = __ReadVector128(__arm64_pair_address_13513312);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v5 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13513312) + (0x10UL))));
#else
        v5 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13513312) + (0x10UL))));
#endif
        x0 = sp;
        x1 = 0x0UL;
        __arm64_pair_address_13513324 = sp;
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13513324, v2);
#else
        __WriteVector128(__arm64_pair_address_13513324, v2);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13513324) + (0x10UL))), v3);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13513324) + (0x10UL))), v3);
#endif
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        __arm64_pair_address_13513336 = unchecked((ulong)((sp) + (0x20UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13513336, v4);
#else
        __WriteVector128(__arm64_pair_address_13513336, v4);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13513336) + (0x10UL))), v5);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13513336) + (0x10UL))), v5);
#endif
        x0 = RuntimeCalls.InvokeDirect(0x1786F84UL /* metadata target: Matrix4x4.op_Multiply */, x0, x1, x2, x3);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x40000000UL)), 0)), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        x1 = unchecked((ulong)(unchecked((uint)(0x3UL))));
        x0 = x20;
        x2 = 0x0UL;
        v11 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v10 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        x0 = RuntimeCalls.InvokeDirect(0x17868A4UL /* metadata target: Matrix4x4.get_Item */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        x1 = unchecked((ulong)(unchecked((uint)(0x2UL))));
        x0 = x20;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17867B4UL /* metadata target: Matrix4x4.set_Item */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x1 = unchecked((ulong)(unchecked((uint)(0x7UL))));
        x0 = x20;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17868A4UL /* metadata target: Matrix4x4.get_Item */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        x1 = unchecked((ulong)(unchecked((uint)(0x6UL))));
        x0 = x20;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17867B4UL /* metadata target: Matrix4x4.set_Item */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x1 = unchecked((ulong)(unchecked((uint)(0xBUL))));
        x0 = x20;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17868A4UL /* metadata target: Matrix4x4.get_Item */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        x1 = unchecked((ulong)(unchecked((uint)(0xAUL))));
        x0 = x20;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17867B4UL /* metadata target: Matrix4x4.set_Item */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x1 = unchecked((ulong)(unchecked((uint)(0xFUL))));
        x0 = x20;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17868A4UL /* metadata target: Matrix4x4.get_Item */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        x1 = unchecked((ulong)(unchecked((uint)(0xEUL))));
        x0 = x20;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17867B4UL /* metadata target: Matrix4x4.set_Item */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        __arm64_pair_address_13513540 = unchecked((ulong)((x20) + (0x20UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(__arm64_pair_address_13513540);
#else
        v1 = __ReadVector128(__arm64_pair_address_13513540);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13513540) + (0x10UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13513540) + (0x10UL))));
#endif
        __arm64_pair_address_13513544 = x20;
#if IL2CPPREC_RUNTIME_VECTOR128
        v3 = RuntimeMemory.ReadVector128(__arm64_pair_address_13513544);
#else
        v3 = __ReadVector128(__arm64_pair_address_13513544);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v2 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13513544) + (0x10UL))));
#else
        v2 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13513544) + (0x10UL))));
#endif
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0xE0UL))));
        __arm64_pair_address_13513552 = unchecked((ulong)((sp) + (0xD0UL)));
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13513552)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13513552) + (0x8UL))))), 0));
        __arm64_pair_address_13513556 = unchecked((ulong)((x19) + (0x20UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13513556, v1);
#else
        __WriteVector128(__arm64_pair_address_13513556, v1);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13513556) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13513556) + (0x10UL))), v0);
#endif
        __arm64_pair_address_13513560 = x19;
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13513560, v3);
#else
        __WriteVector128(__arm64_pair_address_13513560, v3);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13513560) + (0x10UL))), v2);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13513560) + (0x10UL))), v2);
#endif
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0xF0UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xF0UL)))) + (0x8UL))));
        __arm64_pair_address_13513568 = unchecked((ulong)((sp) + (0xC0UL)));
        v11 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13513568)), 0));
        v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13513568) + (0x8UL))))), 0));
        sp = unchecked((ulong)((sp) + (0x100UL)));
        return x0;
        return default(ulong);
    }
```

## `PlanarReflection.Sgn` — RVA `0xce336c`

- Lift status: **partial**; input span: 28 bytes; span to next metadata RVA: 28 bytes.
- Metadata signature: `private static float Sgn(float a) { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=0 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'b.mi' at 0xce337c; reason: Unknown IR expression at 0xce337c

```csharp
public static ulong PlanarReflection_Sgn_RVAce336c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        float __arm64_float_flags_left_13513580 = default(float);
        float __arm64_float_flags_right_13513580 = default(float);
        RuntimeVector128 v0 = default(RuntimeVector128);
        __arm64_float_flags_left_13513580 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13513580 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        if ((__arm64_float_flags_left_13513580 > __arm64_float_flags_right_13513580))
        {
        }
        else
        {
            v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0xBF800000UL)), 0)), 0));
            RuntimeCalls.Unsupported("b.mi", 0xCE337CUL);
            if (__Unsupported<bool>("Unknown IR expression"))
            {
            }
            else
            {
                v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
            }
        }
        label_0xCE3384:
        ;
        return x0;
        return default(ulong);
    }
```

## `PlanarReflection.ctor` — RVA `0xce3388`

- Lift status: **exact**; input span: 112 bytes; span to next metadata RVA: 112 bytes.
- Metadata signature: `public void .ctor() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=17 (informational only).

```csharp
public static ulong PlanarReflection_ctor_RVAce3388(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
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
        x20 = 0x1A8F000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x64CUL))))))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xA48UL))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCE33BC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xA48UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x64CUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCE33BC;
        label_0xCE33BC:
        ;
        x8 = 0x432000UL;
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((x8) + (0x730UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((x8) + (0x730UL))));
#endif
        x0 = x19;
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x19) + (0x28UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((x19) + (0x28UL))), v0);
#endif
        x1 = RuntimeMemory.ReadU64(x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x38UL))), x1);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x5C29UL))));
        x8 = unchecked((ulong)(unchecked((uint)(unchecked((ulong)((unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((~(0xFFFFUL)))))))))) | (unchecked((ulong)((unchecked((ulong)((0x3D8FUL) << (int)(unchecked((int)(0x10UL)))))) << (int)(unchecked((int)(0x0UL))))))))))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x19) + (0x40UL))), unchecked((uint)(x8)));
        x0 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x1 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeDirect(0x1796274UL /* metadata target: MonoBehaviour.ctor */);
        return default(ulong);
    }
```
