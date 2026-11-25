# `ReconfigurePrefab` — TypeDefIndex 3418

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x20` | `bool` | `TwoCameraSetup` |
| `0x28` | `FPSPlayer` | `FPSPlayerComponent` |
| `0x30` | `CameraControl` | `CameraControlComponent` |
| `0x38` | `GameObject` | `WeaponCamera` |
| `0x40` | `GameObject` | `MainCamera` |
| `0x48` | `GameObject` | `WeaponObj` |
| `0x50` | `float` | `twoCamWeaponScale` |
| `0x54` | `float` | `oneCamWeaponScale` |
| `0x58` | `float` | `oneCamNearPlane` |
| `0x5C` | `float` | `twoCamNearPlane` |
| `0x60` | `float` | `weaponCamNearPlane` |
| `0x64` | `bool` | `shadeWeaponByRaycast` |
| `0x68` | `WeaponBehavior[]` | `WeaponBehaviorComponents` |
| `0x70` | `LayerMask` | `mainTwoCamMask` |
| `0x74` | `LayerMask` | `mainOneCamMask` |
| `0x78` | `bool` | `TwoCamState` |
| `0x79` | `bool` | `OneCamState` |

## `ReconfigurePrefab.Start` — RVA `0xcac87c`

- Lift status: **exact**; input span: 296 bytes; span to next metadata RVA: 296 bytes.
- Metadata signature: `private void Start() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=43 (informational only).

```csharp
public static ulong ReconfigurePrefab_Start_RVAcac87c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
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
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x4C4UL))))))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCAC8C0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xCD8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x20UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x5D8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x4C4UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCAC8C0;
        label_0xCAC8C0:
        ;
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x176F8DCUL /* metadata target: Camera.get_main */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCAC9A0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xCD8UL))));
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xE31BC8UL, x0, x1, x2, x3);
        x20 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x20) + (0x30UL))), x0);
        x1 = x0;
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x20);
        if ((x0 == 0x0UL))
        {
            goto label_0xCAC9A0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792154UL /* metadata target: Component.get_transform */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCAC9A0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792190UL /* metadata target: Component.get_gameObject */, x0, x1, x2, x3);
        x20 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x20) + (0x40UL))), x0);
        x1 = x0;
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xFFFFFFFFFFFFFFF0UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCAC9A0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x30UL))));
        x20 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x20) + (0x48UL))), x1);
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x20);
        if ((x0 == 0x0UL))
        {
            goto label_0xCAC9A0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x5D8UL))));
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x2 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xE49EC4UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x20 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x20) + (0x68UL))), x0);
        x1 = x0;
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xFFFFFFFFFFFFFFD8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCAC9A0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xE49224UL, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCAC9A0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x60UL))));
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x28UL))), x1);
        x0 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0xB7D8D0UL);
        label_0xCAC9A0:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `ReconfigurePrefab.Update` — RVA `0xcac9a4`

- Lift status: **exact**; input span: 788 bytes; span to next metadata RVA: 788 bytes.
- Metadata signature: `private void Update() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=105 (informational only).

```csharp
public static ulong ReconfigurePrefab_Update_RVAcac9a4(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13290132 = default(uint);
        uint __arm64_flags_left_13290152 = default(uint);
        uint __arm64_flags_left_13290244 = default(uint);
        uint __arm64_flags_left_13290512 = default(uint);
        uint __arm64_flags_left_13290532 = default(uint);
        uint __arm64_flags_left_13290620 = default(uint);
        uint __arm64_flags_right_13290132 = default(uint);
        uint __arm64_flags_right_13290152 = default(uint);
        uint __arm64_flags_right_13290244 = default(uint);
        uint __arm64_flags_right_13290512 = default(uint);
        uint __arm64_flags_right_13290532 = default(uint);
        uint __arm64_flags_right_13290620 = default(uint);
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
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFC0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x24);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))), x19);
        x20 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x4C5UL))))))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCAC9E4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x5E0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x4C5UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCAC9E4;
        label_0xCAC9E4:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x20UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCACB54;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x78UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCACB5C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x176F8DCUL /* metadata target: Camera.get_main */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x70UL))))));
        x20 = x0;
        x1 = 0x0UL;
        x0 = unchecked((ulong)(unchecked((uint)(x8))));
        x0 = RuntimeCalls.InvokeDirect(0x179515CUL /* metadata target: LayerMask.op_Implicit */, x0, x1, x2, x3);
        if ((x20 == 0x0UL))
        {
            goto label_0xCACCB0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)(x0))));
        x0 = x20;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x176EA68UL /* metadata target: Camera.set_cullingMask */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x176F8DCUL /* metadata target: Camera.get_main */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCACCB0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCACA30UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x5CUL))))), 0));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x176E648UL /* metadata target: Camera.set_nearClipPlane */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x48UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCACCB0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794C14UL /* metadata target: GameObject.get_transform */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCACCB0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCACA50UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x50UL))))), 0));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179DBE0UL /* metadata target: Transform.set_localScale */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x28UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCACCB0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x60UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCACCB0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x240UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCACCB0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17CF938UL /* metadata target: Collider.set_enabled */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x68UL))));
        if ((x21 == 0x0UL))
        {
            goto label_0xCACCB0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x21) + (0x18UL))))));
        __arm64_flags_left_13290132 = unchecked((uint)(x8));
        __arm64_flags_right_13290132 = unchecked((uint)0x1UL);
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13290132) - (__arm64_flags_right_13290132))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_13290132)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13290132)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13290132) - (__arm64_flags_right_13290132))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13290132)) < unchecked((int)0x0UL))))))
        {
            goto label_0xCACB0C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x23 = 0x1A8C000UL;
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0xD8UL))));
        x22 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xCACAA8;
        label_0xCACAA8:
        ;
        __arm64_flags_left_13290152 = unchecked((uint)(x22));
        __arm64_flags_right_13290152 = unchecked((uint)(x8));
        if ((__arm64_flags_left_13290152 >= __arm64_flags_right_13290152))
        {
            goto label_0xCACCB4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)((x21) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x22))) << (int)(unchecked((int)(unchecked((uint)(0x3UL))))))))))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        if ((x24 == 0x0UL))
        {
            goto label_0xCACCB0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x64UL))))))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x24) + (0x750UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x24) + (0x538UL))), unchecked((byte)(unchecked((uint)(x8)))));
        x0 = RuntimeMemory.ReadU64(x23);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCACAD8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCACAD4UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xCACAD8;
        label_0xCACAD8:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1798274UL /* metadata target: Object.op_Implicit */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCACAFC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x24) + (0x750UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCACCB0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCACAF0UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x24) + (0x758UL))))), 0));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177BD90UL /* metadata target: Light.set_range */, x0, x1, x2, x3);
        goto label_0xCACAFC;
        label_0xCACAFC:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x21) + (0x18UL))))));
        x22 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x22))) + (unchecked((uint)(0x1UL)))))));
        __arm64_flags_left_13290244 = unchecked((uint)(x22));
        __arm64_flags_right_13290244 = unchecked((uint)(x8));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13290244) - (__arm64_flags_right_13290244))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_13290244)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13290244)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13290244) - (__arm64_flags_right_13290244))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13290244)) < unchecked((int)0x0UL))))))
        {
            goto label_0xCACAA8;
        }
        else
        {
            goto label_0xCACB0C;
        }
        label_0xCACB0C:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x38UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCACCB0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x5E0UL))));
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xE49224UL, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCACCB0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCACB28UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x60UL))))), 0));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x176E648UL /* metadata target: Camera.set_nearClipPlane */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x38UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCACCB0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x2 = 0x0UL;
        x20 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = RuntimeCalls.InvokeDirect(0x1794CD0UL /* metadata target: GameObject.SetActive */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        RuntimeMemory.WriteU16(unchecked((ulong)((x19) + (0x78UL))), unchecked((ushort)(unchecked((uint)(x20)))));
        goto label_0xCACB5C;
        label_0xCACB54:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x79UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCACB70;
        }
        else
        {
            goto label_0xCACB5C;
        }
        label_0xCACB5C:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        label_0xCACB70:
        ;
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x176F8DCUL /* metadata target: Camera.get_main */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x74UL))))));
        x20 = x0;
        x1 = 0x0UL;
        x0 = unchecked((ulong)(unchecked((uint)(x8))));
        x0 = RuntimeCalls.InvokeDirect(0x179515CUL /* metadata target: LayerMask.op_Implicit */, x0, x1, x2, x3);
        if ((x20 == 0x0UL))
        {
            goto label_0xCACCB0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)(x0))));
        x0 = x20;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x176EA68UL /* metadata target: Camera.set_cullingMask */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x176F8DCUL /* metadata target: Camera.get_main */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCACCB0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCACBACUL);
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x58UL))))), 0));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x176E648UL /* metadata target: Camera.set_nearClipPlane */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x48UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCACCB0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794C14UL /* metadata target: GameObject.get_transform */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCACCB0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCACBCCUL);
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x54UL))))), 0));
        x1 = 0x0UL;
        v1 = v0;
        v2 = v0;
        x0 = RuntimeCalls.InvokeDirect(0x179DBE0UL /* metadata target: Transform.set_localScale */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x28UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCACCB0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x60UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCACCB0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x240UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCACCB0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17CF938UL /* metadata target: Collider.set_enabled */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x68UL))));
        if ((x21 == 0x0UL))
        {
            goto label_0xCACCB0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x21) + (0x18UL))))));
        __arm64_flags_left_13290512 = unchecked((uint)(x8));
        __arm64_flags_right_13290512 = unchecked((uint)0x1UL);
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13290512) - (__arm64_flags_right_13290512))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_13290512)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13290512)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13290512) - (__arm64_flags_right_13290512))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13290512)) < unchecked((int)0x0UL))))))
        {
            goto label_0xCACC84;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x23 = 0x1A8C000UL;
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0xD8UL))));
        x22 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xCACC24;
        label_0xCACC24:
        ;
        __arm64_flags_left_13290532 = unchecked((uint)(x22));
        __arm64_flags_right_13290532 = unchecked((uint)(x8));
        if ((__arm64_flags_left_13290532 >= __arm64_flags_right_13290532))
        {
            goto label_0xCACCB4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)((x21) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x22))) << (int)(unchecked((int)(unchecked((uint)(0x3UL))))))))))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        if ((x24 == 0x0UL))
        {
            goto label_0xCACCB0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCACC38UL);
        }
        RuntimeMemory.WriteU8(unchecked((ulong)((x24) + (0x538UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        x0 = RuntimeMemory.ReadU64(x23);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x24) + (0x750UL))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCACC50;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCACC4CUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xCACC50;
        label_0xCACC50:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1798274UL /* metadata target: Object.op_Implicit */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCACC74;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x24) + (0x750UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCACCB0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCACC68UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x24) + (0x75CUL))))), 0));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177BD90UL /* metadata target: Light.set_range */, x0, x1, x2, x3);
        goto label_0xCACC74;
        label_0xCACC74:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x21) + (0x18UL))))));
        x22 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x22))) + (unchecked((uint)(0x1UL)))))));
        __arm64_flags_left_13290620 = unchecked((uint)(x22));
        __arm64_flags_right_13290620 = unchecked((uint)(x8));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13290620) - (__arm64_flags_right_13290620))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_13290620)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13290620)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13290620) - (__arm64_flags_right_13290620))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13290620)) < unchecked((int)0x0UL))))))
        {
            goto label_0xCACC24;
        }
        else
        {
            goto label_0xCACC84;
        }
        label_0xCACC84:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x38UL))));
        x8 = unchecked((ulong)(unchecked((uint)(0x100UL))));
        RuntimeMemory.WriteU16(unchecked((ulong)((x19) + (0x78UL))), unchecked((ushort)(unchecked((uint)(x8)))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCACCB0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x2 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0x1794CD0UL /* metadata target: GameObject.SetActive */);
        label_0xCACCB0:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xCACCB4;
        label_0xCACCB4:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB7CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        return default(ulong);
    }
```

## `ReconfigurePrefab.ctor` — RVA `0xcaccb8`

- Lift status: **exact**; input span: 44 bytes; span to next metadata RVA: 44 bytes.
- Metadata signature: `public void .ctor() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=5 (informational only).

```csharp
public static ulong ReconfigurePrefab_ctor_RVAcaccb8(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        RuntimeVector128 v0 = default(RuntimeVector128);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        x9 = 0x432000UL;
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((x9) + (0x6A0UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((x9) + (0x6A0UL))));
#endif
        x9 = unchecked((ulong)(unchecked((uint)(0x6666UL))));
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x9 = unchecked((ulong)(unchecked((uint)(unchecked((ulong)((unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) & (unchecked((uint)((~(0xFFFFUL)))))))))) | (unchecked((ulong)((unchecked((ulong)((0x3EE6UL) << (int)(unchecked((int)(0x10UL)))))) << (int)(unchecked((int)(0x0UL))))))))))));
        x1 = 0x0UL;
        RuntimeMemory.WriteU8(unchecked((ulong)((x0) + (0x20UL))), unchecked((byte)(unchecked((uint)(x8)))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x0) + (0x60UL))), unchecked((uint)(x9)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x0) + (0x50UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((x0) + (0x50UL))), v0);
#endif
        RuntimeMemory.WriteU8(unchecked((ulong)((x0) + (0x64UL))), unchecked((byte)(unchecked((uint)(x8)))));
        return RuntimeCalls.InvokeDirect(0x1796274UL /* metadata target: MonoBehaviour.ctor */);
        return default(ulong);
    }
```
