# `RunTime_Terrain_Convertion` — TypeDefIndex 3492

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x20` | `Terrain` | `sourceTerrain` |
| `0x28` | `TerrainConvertInfo` | `convertInfo` |
| `0x30` | `bool` | `generateBasemap` |
| `0x31` | `bool` | `attachMeshCollider` |

## `RunTime_Terrain_Convertion.Start` — RVA `0xccb7a8`

- Lift status: **partial**; input span: 1100 bytes; span to next metadata RVA: 1100 bytes.
- Metadata signature: `private void Start() { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=173 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'b.lt' at 0xccba44; reason: Unknown IR expression at 0xccba44

```csharp
public static ulong RunTime_Terrain_Convertion_Start_RVAccb7a8(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13416648 = default(uint);
        uint __arm64_flags_left_13417068 = default(uint);
        uint __arm64_flags_left_13417284 = default(uint);
        uint __arm64_flags_left_13417416 = default(uint);
        uint __arm64_flags_right_13416648 = default(uint);
        uint __arm64_flags_right_13417068 = default(uint);
        uint __arm64_flags_right_13417284 = default(uint);
        uint __arm64_flags_right_13417416 = default(uint);
        ulong __arm64_pair_address_13417256 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
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
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFA0UL)))) + (0x0UL))), x29);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFA0UL)))) + (0x8UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x28);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x27);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x26);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x25);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x0UL))), x24);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x8UL))), x19);
        x20 = 0x1BAB000UL;
        x23 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x58BUL))))))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0xD8UL))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCCB840;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB98UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xBA0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xBA8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xBB0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xAA8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xBC0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xBB8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x58BUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCCB840;
        label_0xCCB840:
        ;
        x0 = RuntimeMemory.ReadU64(x23);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x20UL))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCCB854;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCCB850UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCCB854;
        label_0xCCB854:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794AC8UL /* metadata target: Object.op_Inequality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCCBBD0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xBB8UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x20UL))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x19) + (0x20UL)))) + (0x8UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCCB884;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCCB880UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCCB884;
        label_0xCCB884:
        ;
        x0 = x21;
        x1 = x20;
        x2 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x3 = 0x0UL;
        x4 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x19A8A2CUL /* metadata target: TerrainToMeshConverter.Convert */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCCBBD0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x30UL))))))));
        x21 = x0;
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCCB8B8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xCCBBF4UL /* metadata target: RunTime_Terrain_Convertion.GenerateMaterial_Basemap */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xCCB8C0;
        label_0xCCB8B8:
        ;
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xCCBDB0UL /* metadata target: RunTime_Terrain_Convertion.GenerateMaterial_Splatmap */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xCCB8C0;
        label_0xCCB8C0:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x21) + (0x18UL))))));
        x20 = x0;
        __arm64_flags_left_13416648 = unchecked((uint)(x8));
        __arm64_flags_right_13416648 = unchecked((uint)0x1UL);
        if ((!((unchecked((uint)((__arm64_flags_left_13416648) - (__arm64_flags_right_13416648))) == unchecked((uint)0x0UL)))))
        {
            goto label_0xCCBA44;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792190UL /* metadata target: Component.get_gameObject */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCCBBEC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xBB0UL))));
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xE49224UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x8 = RuntimeMemory.ReadU64(x23);
        x22 = x0;
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCCB908;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xCCB908;
        label_0xCCB908:
        ;
        x0 = x22;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179568CUL /* metadata target: Object.op_Equality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCCB940;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792190UL /* metadata target: Component.get_gameObject */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCCBBEC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xBA0UL))));
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xE4913CUL, x0, x1, x2, x3);
        x22 = x0;
        goto label_0xCCB940;
        label_0xCCB940:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x21) + (0x18UL))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCCBBF0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCCB948UL);
        }
        if ((x22 == 0x0UL))
        {
            goto label_0xCCBBEC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x20UL))));
        x0 = x22;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177C048UL /* metadata target: MeshFilter.set_sharedMesh */, x0, x1, x2, x3);
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792190UL /* metadata target: Component.get_gameObject */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCCBBEC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xAA8UL))));
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xE49224UL, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x23);
        x21 = x0;
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCCB994;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCCB994;
        label_0xCCB994:
        ;
        x0 = x21;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179568CUL /* metadata target: Object.op_Equality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCCB9CC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792190UL /* metadata target: Component.get_gameObject */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCCBBEC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xBA8UL))));
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xE4913CUL, x0, x1, x2, x3);
        x21 = x0;
        goto label_0xCCB9CC;
        label_0xCCB9CC:
        ;
        if ((x21 == 0x0UL))
        {
            goto label_0xCCBBEC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x21;
        x1 = x20;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1779C44UL /* metadata target: Renderer.set_sharedMaterial */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x31UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCCBBD0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792190UL /* metadata target: Component.get_gameObject */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCCBBEC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB98UL))));
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xE4913CUL, x0, x1, x2, x3);
        x19 = x0;
        x0 = x22;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177C00CUL /* metadata target: MeshFilter.get_sharedMesh */, x0, x1, x2, x3);
        if ((x19 == 0x0UL))
        {
            goto label_0xCCBBEC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = x0;
        x0 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x50UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x40UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))));
        x26 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x25 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x28 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x27 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x2 = 0x0UL;
        x29 = RuntimeMemory.ReadU64(sp);
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeDirect(0x17CFD24UL /* metadata target: MeshCollider.set_sharedMesh */);
        label_0xCCBA44:
        ;
        RuntimeCalls.Unsupported("b.lt", 0xCCBA44UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xCCBBD0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x22 = 0x1A8C000UL;
        x29 = 0x1A8E000UL;
        x27 = 0x1A8E000UL;
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x1E8UL))));
        x29 = RuntimeMemory.ReadU64(unchecked((ulong)((x29) + (0xBA0UL))));
        x27 = RuntimeMemory.ReadU64(unchecked((ulong)((x27) + (0xBA8UL))));
        x25 = 0x0UL;
        x26 = unchecked((ulong)((x21) + (0x20UL)));
        x28 = 0x1BAB000UL;
        goto label_0xCCBA6C;
        label_0xCCBA6C:
        ;
        __arm64_flags_left_13417068 = unchecked((uint)(x25));
        __arm64_flags_right_13417068 = unchecked((uint)(x8));
        if ((__arm64_flags_left_13417068 >= __arm64_flags_right_13417068))
        {
            goto label_0xCCBBF0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x26) + (x25))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCCBBEC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1798300UL /* metadata target: Object.get_name */, x0, x1, x2, x3);
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xBC0UL))));
        x24 = x0;
        x8 = RuntimeMemory.ReadU64(x8);
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = x24;
        x2 = 0x0UL;
        x23 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x1794EA4UL /* metadata target: GameObject.ctor */, x0, x1, x2, x3);
        if ((x23 == 0x0UL))
        {
            goto label_0xCCBBEC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x23;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794C14UL /* metadata target: GameObject.get_transform */, x0, x1, x2, x3);
        x24 = x0;
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792190UL /* metadata target: Component.get_gameObject */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCCBBEC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794C14UL /* metadata target: GameObject.get_transform */, x0, x1, x2, x3);
        if ((x24 == 0x0UL))
        {
            goto label_0xCCBBEC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = x0;
        x0 = x24;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179DCB4UL /* metadata target: Transform.set_parent */, x0, x1, x2, x3);
        x0 = x23;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794C14UL /* metadata target: GameObject.get_transform */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x28) + (0x2C9UL))))))));
        x24 = x0;
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCCBB14;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x22;
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x28) + (0x2C9UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCCBB14;
        label_0xCCBB14:
        ;
        if ((x24 == 0x0UL))
        {
            goto label_0xCCBBEC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x22);
        x0 = x24;
        x1 = 0x0UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        __arm64_pair_address_13417256 = unchecked((ulong)((x8) + (0x4UL)));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13417256)), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13417256) + (0x4UL))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(x8)), 0));
        x0 = RuntimeCalls.InvokeDirect(0x179CBA4UL /* metadata target: Transform.set_localPosition */, x0, x1, x2, x3);
        x1 = RuntimeMemory.ReadU64(x29);
        x0 = x23;
        x0 = RuntimeCalls.InvokeDirect(0xE4913CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x21) + (0x18UL))))));
        __arm64_flags_left_13417284 = unchecked((uint)(x25));
        __arm64_flags_right_13417284 = unchecked((uint)(x8));
        if ((__arm64_flags_left_13417284 >= __arm64_flags_right_13417284))
        {
            goto label_0xCCBBF0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x24 = x0;
        if ((x0 == 0x0UL))
        {
            goto label_0xCCBBEC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x26) + (x25))));
        x0 = x24;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177C048UL /* metadata target: MeshFilter.set_sharedMesh */, x0, x1, x2, x3);
        x1 = RuntimeMemory.ReadU64(x27);
        x0 = x23;
        x0 = RuntimeCalls.InvokeDirect(0xE4913CUL, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCCBBEC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = x20;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1779C44UL /* metadata target: Renderer.set_sharedMaterial */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x31UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCCBBC0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB98UL))));
        x0 = x23;
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xE4913CUL, x0, x1, x2, x3);
        x23 = x0;
        x0 = x24;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177C00CUL /* metadata target: MeshFilter.get_sharedMesh */, x0, x1, x2, x3);
        if ((x23 == 0x0UL))
        {
            goto label_0xCCBBEC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = x0;
        x0 = x23;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17CFD24UL /* metadata target: MeshCollider.set_sharedMesh */, x0, x1, x2, x3);
        goto label_0xCCBBC0;
        label_0xCCBBC0:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x21) + (0x18UL))))));
        x25 = unchecked((ulong)((x25) + (0x1UL)));
        __arm64_flags_left_13417416 = unchecked((uint)(x25));
        __arm64_flags_right_13417416 = unchecked((uint)(x8));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13417416) - (__arm64_flags_right_13417416))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_13417416)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13417416)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13417416) - (__arm64_flags_right_13417416))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13417416)) < unchecked((int)0x0UL))))))
        {
            goto label_0xCCBA6C;
        }
        else
        {
            goto label_0xCCBBD0;
        }
        label_0xCCBBD0:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x50UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x40UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))));
        x26 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x25 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x28 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x27 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x29 = RuntimeMemory.ReadU64(sp);
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return x0;
        label_0xCCBBEC:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        goto label_0xCCBBF0;
        label_0xCCBBF0:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB7CUL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `RunTime_Terrain_Convertion.GenerateMaterial_Basemap` — RVA `0xccbbf4`

- Lift status: **exact**; input span: 444 bytes; span to next metadata RVA: 444 bytes.
- Metadata signature: `private Material GenerateMaterial_Basemap() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=76 (informational only).

```csharp
public static ulong RunTime_Terrain_Convertion_GenerateMaterial_Basemap_RVAccbbf4(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13417732 = default(uint);
        uint __arm64_flags_result_13417732 = default(uint);
        uint __arm64_flags_right_13417732 = default(uint);
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
        sp = unchecked((ulong)((sp) - (0x50UL)));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x10UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x24);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))), x19);
        x21 = 0x1BAB000UL;
        x20 = 0x1A8E000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x58CUL))))))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xBB8UL))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
        }
        else
        {
            x0 = 0x1A8D000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xC50UL))));
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x0 = 0x1A8C000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD8UL))));
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x0 = 0x1A8E000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xBB8UL))));
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x0 = 0x1A8E000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xBC0UL))));
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x0 = 0x1A8E000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xBC8UL))));
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x0 = 0x1A8E000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xBD0UL))));
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
            RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x58CUL))), unchecked((byte)(unchecked((uint)(x8)))));
        }
        label_0xCCBC70:
        ;
        x21 = 0x1A8C000UL;
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xD8UL))));
        x0 = 0x0UL;
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0x18UL))), 0x0UL);
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0x8UL))), 0x0UL);
        x0 = RuntimeCalls.InvokeDirect(0x1779320UL /* metadata target: QualitySettings.get_activeColorSpace */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x20);
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x20UL))));
        x20 = unchecked((ulong)(unchecked((uint)(x0))));
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
        }
        else
        {
            x0 = x8;
            x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        }
        label_0xCCBCA4:
        ;
        x23 = 0x1A8E000UL;
        x24 = 0x1A8E000UL;
        x22 = 0x1A8D000UL;
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0xBD0UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((x24) + (0xBC8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0xC50UL))));
        x1 = unchecked((ulong)((sp) + (0x18UL)));
        x2 = unchecked((ulong)((sp) + (0x8UL)));
        x3 = unchecked((ulong)(unchecked((uint)(0x400UL))));
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0x19AC674UL /* metadata target: TerrainToMeshConverter.ExtractBasemap */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x0 = RuntimeMemory.ReadU64(x21);
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
        }
        else
        {
            x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        }
        label_0xCCBCF4:
        ;
        x0 = x19;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794AC8UL /* metadata target: Object.op_Inequality */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        __arm64_flags_left_13417732 = unchecked((uint)(x0));
        __arm64_flags_right_13417732 = unchecked((uint)0x1UL);
        __arm64_flags_result_13417732 = unchecked((uint)((__arm64_flags_left_13417732) & (__arm64_flags_right_13417732)));
        x8 = ((!((__arm64_flags_result_13417732 == unchecked((uint)0x0UL)))) ? x23 : x24);
        x0 = RuntimeMemory.ReadU64(x8);
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177A080UL /* metadata target: Shader.Find */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x8 = RuntimeMemory.ReadU64(x22);
        x20 = x0;
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x1 = x20;
        x2 = 0x0UL;
        x19 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x177A378UL /* metadata target: Material.ctor */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        if ((x19 == 0x0UL))
        {
            label_0xCCBDAC:
            ;
            x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        }
        else
        {
            x1 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x18UL))));
            x0 = x19;
            x2 = 0x0UL;
            x0 = RuntimeCalls.InvokeDirect(0x177A970UL /* metadata target: Material.set_mainTexture */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
            x0 = RuntimeMemory.ReadU64(x21);
            x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
            x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
            if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
            {
            }
            else
            {
                x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
            }
            label_0xCCBD60:
            ;
            x0 = x20;
            x1 = 0x0UL;
            x2 = 0x0UL;
            x0 = RuntimeCalls.InvokeDirect(0x1794AC8UL /* metadata target: Object.op_Inequality */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
            if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
            {
            }
            else
            {
                x8 = 0x1A8E000UL;
                x2 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
                x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xBC0UL))));
                x0 = x19;
                x3 = 0x0UL;
                x1 = RuntimeMemory.ReadU64(x8);
                x0 = RuntimeCalls.InvokeDirect(0x177AA8CUL /* metadata target: Material.SetTexture */, x0, x1, x2, x3);
            }
            label_0xCCBD90:
            ;
            x0 = x19;
            x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x40UL))));
            x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))));
            x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
            x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))));
            x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
            x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
            x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
            return x0;
        }
        return default(ulong);
    }
```

## `RunTime_Terrain_Convertion.GenerateMaterial_Splatmap` — RVA `0xccbdb0`

- Lift status: **partial**; input span: 1796 bytes; span to next metadata RVA: 1796 bytes.
- Metadata signature: `private Material GenerateMaterial_Splatmap() { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=290 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'csel' at 0xccc070; reason: Unknown IR expression at 0xccc070; reason: Unsupported instruction 'csel' at 0xccc098; reason: Unknown IR expression at 0xccc098; reason: Unsupported instruction 'cset' at 0xccc0a4; reason: Unknown IR expression at 0xccc0a4; reason: Unsupported instruction 'b.ne' at 0xccc4a4; reason: Unknown IR expression at 0xccc4a4

```csharp
public static ulong RunTime_Terrain_Convertion_GenerateMaterial_Splatmap_RVAccbdb0(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13418336 = default(uint);
        uint __arm64_flags_left_13418600 = default(uint);
        uint __arm64_flags_left_13418628 = default(uint);
        ulong __arm64_flags_left_13418652 = default(ulong);
        uint __arm64_flags_left_13418664 = default(uint);
        uint __arm64_flags_left_13418672 = default(uint);
        uint __arm64_flags_left_13419008 = default(uint);
        uint __arm64_flags_left_13419036 = default(uint);
        uint __arm64_flags_left_13419176 = default(uint);
        ulong __arm64_flags_left_13419312 = default(ulong);
        ulong __arm64_flags_left_13419392 = default(ulong);
        ulong __arm64_flags_left_13419468 = default(ulong);
        ulong __arm64_flags_left_13419548 = default(ulong);
        ulong __arm64_flags_left_13419640 = default(ulong);
        ulong __arm64_flags_left_13419672 = default(ulong);
        uint __arm64_flags_result_13418672 = default(uint);
        uint __arm64_flags_right_13418336 = default(uint);
        uint __arm64_flags_right_13418600 = default(uint);
        uint __arm64_flags_right_13418628 = default(uint);
        ulong __arm64_flags_right_13418652 = default(ulong);
        uint __arm64_flags_right_13418664 = default(uint);
        uint __arm64_flags_right_13418672 = default(uint);
        uint __arm64_flags_right_13419008 = default(uint);
        uint __arm64_flags_right_13419036 = default(uint);
        uint __arm64_flags_right_13419176 = default(uint);
        ulong __arm64_flags_right_13419312 = default(ulong);
        ulong __arm64_flags_right_13419392 = default(ulong);
        ulong __arm64_flags_right_13419468 = default(ulong);
        ulong __arm64_flags_right_13419548 = default(ulong);
        ulong __arm64_flags_right_13419640 = default(ulong);
        ulong __arm64_flags_right_13419672 = default(ulong);
        ulong __arm64_pair_address_13418504 = default(ulong);
        ulong __arm64_pair_address_13418536 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        ulong x10 = default(ulong);
        ulong x11 = default(ulong);
        ulong x12 = default(ulong);
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
        sp = unchecked((ulong)((sp) - (0xB0UL)));
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x0UL))), x29);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x8UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x0UL))), x28);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x8UL))), x27);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x70UL)))) + (0x0UL))), x26);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x70UL)))) + (0x8UL))), x25);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x80UL)))) + (0x0UL))), x24);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x80UL)))) + (0x8UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x90UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x90UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xA0UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xA0UL)))) + (0x8UL))), x19);
        x20 = 0x1BAB000UL;
        x21 = 0x1A8E000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x58DUL))))))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xBB8UL))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCCBEDC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x398UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x1C0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xC50UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xBB8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xBD8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xBE0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xBE8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xBF0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xBF8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xC00UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xC08UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xC10UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xC18UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xC20UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xC28UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xC30UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xC38UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xBC8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xC40UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x58DUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCCBEDC;
        label_0xCCBEDC:
        ;
        x0 = RuntimeMemory.ReadU64(x21);
        RuntimeMemory.WritePtr(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x0UL))), 0x0UL);
        RuntimeMemory.WritePtr(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))), 0x0UL);
        RuntimeMemory.WritePtr(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x0UL))), 0x0UL);
        RuntimeMemory.WritePtr(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))), 0x0UL);
        RuntimeMemory.WritePtr(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), 0x0UL);
        RuntimeMemory.WritePtr(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), 0x0UL);
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0x1CUL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x20UL))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCCBF00;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCCBEFCUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCCBF00;
        label_0xCCBF00:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x19ABB1CUL /* metadata target: TerrainToMeshConverter.ExtractSplatmaps */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCCC1B4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x18UL))));
        x20 = x0;
        if ((x8 == 0x0UL))
        {
            goto label_0xCCC1B4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(x21);
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x20UL))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCCBF30;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCCBF2CUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCCBF30;
        label_0xCCBF30:
        ;
        x1 = unchecked((ulong)((sp) + (0x48UL)));
        x2 = unchecked((ulong)((sp) + (0x40UL)));
        x3 = unchecked((ulong)((sp) + (0x38UL)));
        x4 = unchecked((ulong)((sp) + (0x30UL)));
        x5 = unchecked((ulong)((sp) + (0x28UL)));
        x6 = unchecked((ulong)((sp) + (0x20UL)));
        x0 = x19;
        x7 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x19AD4DCUL /* metadata target: TerrainToMeshConverter.ExtractTexturesInfo */, x0, x1, x2, x3);
        if ((unchecked((uint)(x0)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCCC03C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x48UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCCC03C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCCBF60UL);
        }
        __arm64_flags_left_13418336 = unchecked((uint)(x0));
        __arm64_flags_right_13418336 = unchecked((uint)0x1UL);
        if ((!((unchecked((uint)((__arm64_flags_left_13418336) - (__arm64_flags_right_13418336))) == unchecked((uint)0x0UL)))))
        {
            goto label_0xCCC064;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xBC8UL))));
        x1 = 0x0UL;
        x0 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x177A080UL /* metadata target: Shader.Find */, x0, x1, x2, x3);
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xD8UL))));
        x20 = x0;
        x8 = RuntimeMemory.ReadU64(x8);
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCCBF9C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCCBF9C;
        label_0xCCBF9C:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794AC8UL /* metadata target: Object.op_Inequality */, x0, x1, x2, x3);
        x19 = 0x0UL;
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCCC1B8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xC50UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = x20;
        x2 = 0x0UL;
        x19 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x177A378UL /* metadata target: Material.ctor */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x48UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCCC4AC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCCC4B0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCCBFE4UL);
        }
        if ((x19 == 0x0UL))
        {
            goto label_0xCCC4AC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        x0 = x19;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177A970UL /* metadata target: Material.set_mainTexture */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x38UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCCC4AC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCCC4B0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCCC008UL);
        }
        __arm64_pair_address_13418504 = unchecked((ulong)((x8) + (0x20UL)));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13418504)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13418504) + (0x4UL))))), 0));
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177AC24UL /* metadata target: Material.set_mainTextureScale */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCCC4AC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCCC4B0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCCC028UL);
        }
        __arm64_pair_address_13418536 = unchecked((ulong)((x8) + (0x20UL)));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13418536)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13418536) + (0x4UL))))), 0));
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177AB0CUL /* metadata target: Material.set_mainTextureOffset */, x0, x1, x2, x3);
        goto label_0xCCC1B8;
        label_0xCCC03C:
        ;
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x398UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCCC054;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCCC050UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCCC054;
        label_0xCCC054:
        ;
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xC10UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        goto label_0xCCC1AC;
        label_0xCCC064:
        ;
        x10 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x40UL))));
        __arm64_flags_left_13418600 = unchecked((uint)(x0));
        __arm64_flags_right_13418600 = unchecked((uint)0x8UL);
        x8 = unchecked((ulong)(unchecked((uint)(0x8UL))));
        RuntimeCalls.Unsupported("csel", 0xCCC070UL);
        x8 = unchecked((ulong)((__Unsupported<bool>("Unknown IR expression") ? unchecked((uint)(x0)) : unchecked((uint)(x8)))));
        x9 = unchecked((ulong)(unchecked((uint)(0x2UL))));
        x25 = 0x1A8E000UL;
        x11 = 0x1A8E000UL;
        x12 = 0x1A8E000UL;
        __arm64_flags_left_13418628 = unchecked((uint)(x8));
        __arm64_flags_right_13418628 = unchecked((uint)0x2UL);
        x25 = RuntimeMemory.ReadU64(unchecked((ulong)((x25) + (0xC38UL))));
        x11 = RuntimeMemory.ReadU64(unchecked((ulong)((x11) + (0xBF0UL))));
        x12 = RuntimeMemory.ReadU64(unchecked((ulong)((x12) + (0xC00UL))));
        x26 = 0x1A8E000UL;
        RuntimeCalls.Unsupported("csel", 0xCCC098UL);
        x24 = unchecked((ulong)((__Unsupported<bool>("Unknown IR expression") ? unchecked((uint)(x8)) : unchecked((uint)(x9)))));
        __arm64_flags_left_13418652 = x10;
        __arm64_flags_right_13418652 = 0x0UL;
        x26 = RuntimeMemory.ReadU64(unchecked((ulong)((x26) + (0xBF8UL))));
        RuntimeCalls.Unsupported("cset", 0xCCC0A4UL);
        x8 = unchecked((ulong)((__Unsupported<bool>("Unknown IR expression") ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        __arm64_flags_left_13418664 = unchecked((uint)(x24));
        __arm64_flags_right_13418664 = unchecked((uint)0x5UL);
        x9 = unchecked((ulong)((((unchecked((int)(unchecked((uint)((__arm64_flags_left_13418664) - (__arm64_flags_right_13418664))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_13418664)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13418664)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13418664) - (__arm64_flags_right_13418664))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13418664)) < unchecked((int)0x0UL))))) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        __arm64_flags_left_13418672 = unchecked((uint)(x9));
        __arm64_flags_right_13418672 = unchecked((uint)(x8));
        __arm64_flags_result_13418672 = unchecked((uint)((__arm64_flags_left_13418672) & (__arm64_flags_right_13418672)));
        x23 = unchecked((ulong)(__arm64_flags_result_13418672));
        x27 = ((!((__arm64_flags_result_13418672 == unchecked((uint)0x0UL)))) ? x12 : x11);
        x0 = RuntimeMemory.ReadU64(x25);
        x1 = RuntimeMemory.ReadU64(x27);
        x2 = RuntimeMemory.ReadU64(x26);
        x3 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x13F661CUL /* metadata target: String.Concat */, x0, x1, x2, x3);
        x22 = 0x1A8C000UL;
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x1C0UL))));
        x19 = x0;
        x1 = unchecked((ulong)((sp) + (0x18UL)));
        RuntimeMemory.WriteU32(unchecked((ulong)((sp) + (0x18UL))), unchecked((uint)(x24)));
        x0 = RuntimeMemory.ReadU64(x22);
        x0 = RuntimeCalls.InvokeDirect(0xB7DA64UL, x0, x1, x2, x3);
        x1 = x0;
        x0 = x19;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x13EDEE0UL /* metadata target: String.Format */, x0, x1, x2, x3);
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177A080UL /* metadata target: Shader.Find */, x0, x1, x2, x3);
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xD8UL))));
        x21 = x0;
        x8 = RuntimeMemory.ReadU64(x8);
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCCC120;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCCC120;
        label_0xCCC120:
        ;
        x0 = x21;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179568CUL /* metadata target: Object.op_Equality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCCC1DC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(x25);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xC18UL))));
        x1 = RuntimeMemory.ReadU64(x27);
        x2 = RuntimeMemory.ReadU64(x26);
        x3 = 0x0UL;
        x19 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x13F661CUL /* metadata target: String.Concat */, x0, x1, x2, x3);
        x20 = x0;
        x0 = RuntimeMemory.ReadU64(x22);
        x1 = unchecked((ulong)((sp) + (0x18UL)));
        RuntimeMemory.WriteU32(unchecked((ulong)((sp) + (0x18UL))), unchecked((uint)(x24)));
        x0 = RuntimeCalls.InvokeDirect(0xB7DA64UL, x0, x1, x2, x3);
        x1 = x0;
        x0 = x20;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x13EDEE0UL /* metadata target: String.Format */, x0, x1, x2, x3);
        x1 = x0;
        x0 = x19;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x13ED2C8UL /* metadata target: String.Concat */, x0, x1, x2, x3);
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x398UL))));
        x19 = x0;
        x8 = RuntimeMemory.ReadU64(x8);
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCCC1A8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCCC1A8;
        label_0xCCC1A8:
        ;
        x0 = x19;
        goto label_0xCCC1AC;
        label_0xCCC1AC:
        ;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17714B0UL /* metadata target: Debug.LogWarning */, x0, x1, x2, x3);
        goto label_0xCCC1B4;
        label_0xCCC1B4:
        ;
        x19 = 0x0UL;
        goto label_0xCCC1B8;
        label_0xCCC1B8:
        ;
        x0 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0xA0UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xA0UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x90UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x90UL)))) + (0x8UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x80UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x80UL)))) + (0x8UL))));
        x26 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x70UL))));
        x25 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x70UL)))) + (0x8UL))));
        x28 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x60UL))));
        x27 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x8UL))));
        x29 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x50UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x8UL))));
        sp = unchecked((ulong)((sp) + (0xB0UL)));
        return x0;
        label_0xCCC1DC:
        ;
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xC50UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = x21;
        x2 = 0x0UL;
        x19 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x177A378UL /* metadata target: Material.ctor */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x18UL))));
        __arm64_flags_left_13419008 = unchecked((uint)(x8));
        __arm64_flags_right_13419008 = unchecked((uint)0x1UL);
        if ((!((unchecked((uint)((__arm64_flags_left_13419008) - (__arm64_flags_right_13419008))) == unchecked((uint)0x0UL)))))
        {
            goto label_0xCCC21C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCCC208UL);
        }
        if ((x19 == 0x0UL))
        {
            goto label_0xCCC4AC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = 0x1A8E000UL;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0xC20UL))));
        x8 = unchecked((ulong)((x20) + (0x20UL)));
        goto label_0xCCC2BC;
        label_0xCCC21C:
        ;
        __arm64_flags_left_13419036 = unchecked((uint)(x8));
        __arm64_flags_right_13419036 = unchecked((uint)0x3UL);
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13419036) - (__arm64_flags_right_13419036))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_13419036)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13419036)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13419036) - (__arm64_flags_right_13419036))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13419036)) < unchecked((int)0x0UL))))))
        {
            goto label_0xCCC280;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = unchecked((ulong)((sp) + (0x1CUL)));
        x1 = 0x0UL;
        RuntimeMemory.WriteU32(unchecked((ulong)((sp) + (0x1CUL))), unchecked((uint)(x8)));
        x0 = RuntimeCalls.InvokeDirect(0x1545824UL /* metadata target: Int32.ToString */, x0, x1, x2, x3);
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xBE8UL))));
        x1 = x0;
        x2 = 0x0UL;
        x8 = RuntimeMemory.ReadU64(x8);
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0x13ED2C8UL /* metadata target: String.Concat */, x0, x1, x2, x3);
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x398UL))));
        x21 = x0;
        x8 = RuntimeMemory.ReadU64(x8);
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCCC270;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCCC270;
        label_0xCCC270:
        ;
        x0 = x21;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1770B68UL /* metadata target: Debug.Log */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x18UL))));
        goto label_0xCCC280;
        label_0xCCC280:
        ;
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCCC4B0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCCC284UL);
        }
        if ((x19 == 0x0UL))
        {
            goto label_0xCCC4AC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8E000UL;
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x20UL))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xC20UL))));
        x0 = x19;
        x3 = 0x0UL;
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x177AA8CUL /* metadata target: Material.SetTexture */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x20) + (0x18UL))))));
        __arm64_flags_left_13419176 = unchecked((uint)(x8));
        __arm64_flags_right_13419176 = unchecked((uint)0x1UL);
        if (((!((__arm64_flags_left_13419176 >= __arm64_flags_right_13419176))) || (unchecked((uint)((__arm64_flags_left_13419176) - (__arm64_flags_right_13419176))) == unchecked((uint)0x0UL))))
        {
            goto label_0xCCC4B0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = 0x1A8E000UL;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0xC30UL))));
        x8 = unchecked((ulong)((x20) + (0x28UL)));
        goto label_0xCCC2BC;
        label_0xCCC2BC:
        ;
        x2 = RuntimeMemory.ReadU64(x8);
        x1 = RuntimeMemory.ReadU64(x9);
        x0 = x19;
        x3 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177AA8CUL /* metadata target: Material.SetTexture */, x0, x1, x2, x3);
        x20 = unchecked((ulong)(unchecked((uint)(x24))));
        x24 = 0x1A8E000UL;
        x25 = 0x1A8E000UL;
        x26 = 0x1A8E000UL;
        x27 = 0x1A8E000UL;
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((x24) + (0xBE0UL))));
        x25 = RuntimeMemory.ReadU64(unchecked((ulong)((x25) + (0xBD8UL))));
        x26 = RuntimeMemory.ReadU64(unchecked((ulong)((x26) + (0xC08UL))));
        x27 = RuntimeMemory.ReadU64(unchecked((ulong)((x27) + (0xC28UL))));
        x29 = 0x0UL;
        x21 = unchecked((ulong)(unchecked((uint)(0x20UL))));
        goto label_0xCCC2FC;
        label_0xCCC2FC:
        ;
        x0 = RuntimeMemory.ReadU64(x22);
        x28 = unchecked((ulong)((x29) + (0x1UL)));
        x1 = unchecked((ulong)((sp) + (0x18UL)));
        RuntimeMemory.WriteU32(unchecked((ulong)((sp) + (0x18UL))), unchecked((uint)(x28)));
        x0 = RuntimeCalls.InvokeDirect(0xB7DA64UL, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x24);
        x1 = x0;
        x2 = 0x0UL;
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0x13EDEE0UL /* metadata target: String.Format */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x48UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCCC4AC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_13419312 = x29;
        __arm64_flags_right_13419312 = x9;
        if ((__arm64_flags_left_13419312 >= __arm64_flags_right_13419312))
        {
            goto label_0xCCC4B0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)((x29) << (int)(unchecked((int)(0x3UL))))))));
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        x1 = x0;
        x0 = x19;
        x3 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177AA8CUL /* metadata target: Material.SetTexture */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x22);
        x1 = unchecked((ulong)((sp) + (0x14UL)));
        RuntimeMemory.WriteU32(unchecked((ulong)((sp) + (0x14UL))), unchecked((uint)(x28)));
        x0 = RuntimeCalls.InvokeDirect(0xB7DA64UL, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x25);
        x1 = x0;
        x2 = 0x0UL;
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0x13EDEE0UL /* metadata target: String.Format */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x38UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCCC4AC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_13419392 = x29;
        __arm64_flags_right_13419392 = x9;
        if ((__arm64_flags_left_13419392 >= __arm64_flags_right_13419392))
        {
            goto label_0xCCC4B0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCCC388UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (x21))))), 0));
        x1 = x0;
        x0 = x19;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177B698UL /* metadata target: Material.SetFloat */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x22);
        x1 = unchecked((ulong)((sp) + (0x10UL)));
        RuntimeMemory.WriteU32(unchecked((ulong)((sp) + (0x10UL))), unchecked((uint)(x28)));
        x0 = RuntimeCalls.InvokeDirect(0xB7DA64UL, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x26);
        x1 = x0;
        x2 = 0x0UL;
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0x13EDEE0UL /* metadata target: String.Format */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x28UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCCC4AC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_13419468 = x29;
        __arm64_flags_right_13419468 = x9;
        if ((__arm64_flags_left_13419468 >= __arm64_flags_right_13419468))
        {
            goto label_0xCCC4B0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)((x29) << (int)(unchecked((int)(0x2UL))))))));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x20UL))))), 0));
        x1 = x0;
        x0 = x19;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177B698UL /* metadata target: Material.SetFloat */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x22);
        x1 = unchecked((ulong)((sp) + (0xCUL)));
        RuntimeMemory.WriteU32(unchecked((ulong)((sp) + (0xCUL))), unchecked((uint)(x28)));
        x0 = RuntimeCalls.InvokeDirect(0xB7DA64UL, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x27);
        x1 = x0;
        x2 = 0x0UL;
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0x13EDEE0UL /* metadata target: String.Format */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCCC4AC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_13419548 = x29;
        __arm64_flags_right_13419548 = x9;
        if ((__arm64_flags_left_13419548 >= __arm64_flags_right_13419548))
        {
            goto label_0xCCC4B0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)((x29) << (int)(unchecked((int)(0x2UL))))))));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x20UL))))), 0));
        x1 = x0;
        x0 = x19;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177B698UL /* metadata target: Material.SetFloat */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x23))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCCC498;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(x22);
        x1 = unchecked((ulong)((sp) + (0x18UL)));
        RuntimeMemory.WriteU32(unchecked((ulong)((sp) + (0x18UL))), unchecked((uint)(x28)));
        x0 = RuntimeCalls.InvokeDirect(0xB7DA64UL, x0, x1, x2, x3);
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xC40UL))));
        x1 = x0;
        x2 = 0x0UL;
        x8 = RuntimeMemory.ReadU64(x8);
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0x13EDEE0UL /* metadata target: String.Format */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x40UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCCC4AC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_13419640 = x29;
        __arm64_flags_right_13419640 = x9;
        if ((__arm64_flags_left_13419640 >= __arm64_flags_right_13419640))
        {
            goto label_0xCCC4B0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)((x29) << (int)(unchecked((int)(0x3UL))))))));
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        x1 = x0;
        x0 = x19;
        x3 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177AA8CUL /* metadata target: Material.SetTexture */, x0, x1, x2, x3);
        goto label_0xCCC498;
        label_0xCCC498:
        ;
        __arm64_flags_left_13419672 = x20;
        __arm64_flags_right_13419672 = x28;
        x21 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x21))) + (unchecked((uint)(0x8UL)))))));
        x29 = x28;
        RuntimeCalls.Unsupported("b.ne", 0xCCC4A4UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xCCC2FC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCCC4A8UL);
        }
        goto label_0xCCC1B8;
        label_0xCCC4AC:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        goto label_0xCCC4B0;
        label_0xCCC4B0:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB7CUL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `RunTime_Terrain_Convertion.ctor` — RVA `0xccc4b4`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public void .ctor() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static ulong RunTime_Terrain_Convertion_ctor_RVAccc4b4(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x1 = 0x0UL;
        return RuntimeCalls.InvokeDirect(0x1796274UL /* metadata target: MonoBehaviour.ctor */);
        return default(ulong);
    }
```
