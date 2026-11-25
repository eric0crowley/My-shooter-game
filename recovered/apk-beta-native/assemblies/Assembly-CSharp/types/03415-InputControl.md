# `InputControl` — TypeDefIndex 3415

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x20` | `FPSPlayer` | `FPSPlayerComponent` |
| `0x28` | `GameObject` | `AimCrossshare` |
| `0x30` | `GameObject` | `MainCamera` |
| `0x38` | `GameObject` | `Sniper_Anim` |
| `0x40` | `GameObject` | `Sniper_Anim2` |
| `0x48` | `GameObject` | `ScopeImage1` |
| `0x50` | `GameObject` | `ScopeImage2` |
| `0x58` | `Sprite` | `onbutt` |
| `0x60` | `Sprite` | `offbutt` |
| `0x68` | `Button` | `Sourcebutton` |
| `0x70` | `bool` | `onoff` |
| `0x71` | `bool` | `SniperAnim` |
| `0x78` | `AudioClip` | `AudioClip` |
| `0x80` | `AudioSource` | `AudioObject` |
| `0x88` | `bool` | `istime` |
| `0x89` | `bool` | `fireHold` |
| `0x8A` | `bool` | `firePress` |
| `0x8B` | `bool` | `reloadPress` |
| `0x8C` | `bool` | `fireModePress` |
| `0x8D` | `bool` | `jumpHold` |
| `0x8E` | `bool` | `jumpPress` |
| `0x8F` | `bool` | `crouchHold` |
| `0x90` | `bool` | `proneHold` |
| `0x91` | `bool` | `sprintHold` |
| `0x92` | `bool` | `zoomHold` |
| `0x93` | `bool` | `zoomPress` |
| `0x94` | `bool` | `leanLeftHold` |
| `0x95` | `bool` | `leanRightHold` |
| `0x96` | `bool` | `useHold` |
| `0x97` | `bool` | `usePress` |
| `0x98` | `bool` | `usePressUp` |
| `0x99` | `bool` | `toggleCameraHold` |
| `0x9A` | `bool` | `toggleCameraDown` |
| `0x9B` | `bool` | `grenadeHold` |
| `0x9C` | `bool` | `deadzonePress` |
| `0x9D` | `bool` | `meleePress` |
| `0x9E` | `bool` | `flashlightPress` |
| `0x9F` | `bool` | `holsterPress` |
| `0xA0` | `bool` | `dropPress` |
| `0xA1` | `bool` | `bulletTimePress` |
| `0xA2` | `bool` | `moveHold` |
| `0xA3` | `bool` | `movePress` |
| `0xA4` | `bool` | `throwHold` |
| `0xA5` | `bool` | `helpPress` |
| `0xA6` | `bool` | `menuPress` |
| `0xA7` | `bool` | `pausePress` |
| `0xA8` | `bool` | `selectNextPress` |
| `0xA9` | `bool` | `selectPrevPress` |
| `0xAA` | `bool` | `selectGrenPress` |
| `0xAB` | `bool` | `selectWeap1Press` |
| `0xAC` | `bool` | `selectWeap2Press` |
| `0xAD` | `bool` | `selectWeap3Press` |
| `0xAE` | `bool` | `selectWeap4Press` |
| `0xAF` | `bool` | `selectWeap5Press` |
| `0xB0` | `bool` | `selectWeap6Press` |
| `0xB1` | `bool` | `selectWeap7Press` |
| `0xB2` | `bool` | `selectWeap8Press` |
| `0xB3` | `bool` | `selectWeap9Press` |
| `0xB4` | `bool` | `selectWeap0Press` |
| `0xB8` | `float` | `mouseWheel` |
| `0xBC` | `bool` | `leftHold` |
| `0xBD` | `bool` | `rightHold` |
| `0xBE` | `bool` | `forwardHold` |
| `0xBF` | `bool` | `backHold` |
| `0xC0` | `float` | `moveXButton` |
| `0xC4` | `float` | `moveYButton` |
| `0xC8` | `float` | `deadzone` |
| `0xCC` | `Vector2` | `moveInput` |
| `0xD4` | `Vector2` | `lookInput` |
| `0xDC` | `float` | `moveX` |
| `0xE0` | `float` | `moveY` |
| `0xE4` | `float` | `lookX` |
| `0xE8` | `float` | `lookY` |
| `0xEC` | `bool` | `xboxDpadLeftHold` |
| `0xED` | `bool` | `xboxDpadRightHold` |
| `0xEE` | `bool` | `xboxDpadUpHold` |
| `0xEF` | `bool` | `xboxDpadDownHold` |
| `0xF0` | `bool` | `xboxDpadLeftPress` |
| `0xF1` | `bool` | `xboxDpadRightPress` |
| `0xF2` | `bool` | `xboxDpadUpPress` |
| `0xF3` | `bool` | `xboxDpadDownPress` |
| `0xF4` | `bool` | `xbdpLstate` |
| `0xF5` | `bool` | `xbdpRstate` |
| `0xF6` | `bool` | `xbdpUstate` |
| `0xF7` | `bool` | `xbdpDstate` |
| `0xF8` | `bool` | `onetime` |

## `InputControl.Start` — RVA `0xca6368`

- Lift status: **exact**; input span: 88 bytes; span to next metadata RVA: 88 bytes.
- Metadata signature: `private void Start() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=14 (informational only).

```csharp
public static ulong InputControl_Start_RVAca6368(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
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
        x21 = 0x1A8D000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x4BDUL))))))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x598UL))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCA639C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x598UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x4BDUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCA639C;
        label_0xCA639C:
        ;
        x1 = RuntimeMemory.ReadU64(x21);
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xE31BC8UL, x0, x1, x2, x3);
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x20UL))), x0);
        x1 = x0;
        x0 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeDirect(0xB7D8D0UL);
        return default(ulong);
    }
```

## `InputControl.Update` — RVA `0xca63c0`

- Lift status: **partial**; input span: 4664 bytes; span to next metadata RVA: 4664 bytes.
- Metadata signature: `private void Update() { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=648 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'b.pl' at 0xca6a08; reason: Unknown IR expression at 0xca6a08; reason: Unsupported instruction 'fmul' at 0xca6a78; reason: Unsupported instruction 'faddp' at 0xca6a7c; reason: Unsupported instruction 'fdiv' at 0xca6a90; reason: Unsupported instruction 'fmul' at 0xca6b20; reason: Unsupported instruction 'fabs' at 0xca6b80; reason: Unsupported instruction 'fmul' at 0xca6ba0

```csharp
public static ulong InputControl_Update_RVAca63c0(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        float __arm64_float_flags_left_13265408 = default(float);
        float __arm64_float_flags_left_13265540 = default(float);
        float __arm64_float_flags_left_13265916 = default(float);
        float __arm64_float_flags_left_13266044 = default(float);
        float __arm64_float_flags_left_13266352 = default(float);
        float __arm64_float_flags_left_13266892 = default(float);
        float __arm64_float_flags_left_13266948 = default(float);
        float __arm64_float_flags_left_13267044 = default(float);
        float __arm64_float_flags_left_13267108 = default(float);
        float __arm64_float_flags_left_13267224 = default(float);
        float __arm64_float_flags_left_13267288 = default(float);
        float __arm64_float_flags_right_13265408 = default(float);
        float __arm64_float_flags_right_13265540 = default(float);
        float __arm64_float_flags_right_13265916 = default(float);
        float __arm64_float_flags_right_13266044 = default(float);
        float __arm64_float_flags_right_13266352 = default(float);
        float __arm64_float_flags_right_13266892 = default(float);
        float __arm64_float_flags_right_13266948 = default(float);
        float __arm64_float_flags_right_13267044 = default(float);
        float __arm64_float_flags_right_13267108 = default(float);
        float __arm64_float_flags_right_13267224 = default(float);
        float __arm64_float_flags_right_13267288 = default(float);
        ulong __arm64_pair_address_13263816 = default(ulong);
        ulong __arm64_pair_address_13263820 = default(ulong);
        ulong __arm64_pair_address_13263824 = default(ulong);
        ulong __arm64_pair_address_13264544 = default(ulong);
        ulong __arm64_pair_address_13264672 = default(ulong);
        ulong __arm64_pair_address_13265020 = default(ulong);
        ulong __arm64_pair_address_13265024 = default(ulong);
        ulong __arm64_pair_address_13265028 = default(ulong);
        ulong __arm64_pair_address_13265304 = default(ulong);
        ulong __arm64_pair_address_13265360 = default(ulong);
        ulong __arm64_pair_address_13265644 = default(ulong);
        ulong __arm64_pair_address_13266148 = default(ulong);
        ulong __arm64_pair_address_13266556 = default(ulong);
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
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        sp = unchecked((ulong)((sp) - (0xE0UL)));
        RuntimeMemory.WriteF64(unchecked((ulong)((sp) + (0x50UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v14.GetUInt64(0)))));
        __arm64_pair_address_13263816 = unchecked((ulong)((sp) + (0x58UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13263816, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v13.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13263816) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v12.GetUInt64(0)))));
        __arm64_pair_address_13263820 = unchecked((ulong)((sp) + (0x68UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13263820, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v11.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13263820) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v10.GetUInt64(0)))));
        __arm64_pair_address_13263824 = unchecked((ulong)((sp) + (0x78UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13263824, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13263824) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x88UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x90UL)))) + (0x0UL))), x28);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x90UL)))) + (0x8UL))), x27);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xA0UL)))) + (0x0UL))), x26);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xA0UL)))) + (0x8UL))), x25);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xB0UL)))) + (0x0UL))), x24);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xB0UL)))) + (0x8UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xC0UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xC0UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xD0UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xD0UL)))) + (0x8UL))), x19);
        x20 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x4BEUL))))))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCA6698;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xE0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x4A8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x3A0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x3A8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xFD0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x530UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x3B0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x3B8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x3C0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x620UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x3C8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x3D0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x3D8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x3E0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x3E8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x3F0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x3F8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x400UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x408UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x410UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x540UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x418UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x420UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x428UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x430UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x438UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x440UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x550UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x448UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x450UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x458UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x460UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x468UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x470UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x478UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x480UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x488UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x490UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x498UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x4A0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x4A8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x4B0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xFD0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x4B8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x4C0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x4C8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x4D0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x4D8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x4E0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x4E8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x4F0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x4F8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x4BEUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCA6698;
        label_0xCA6698:
        ;
        v0 = (RuntimeVector128.Zero.WithUInt64(0, 0x0UL) | RuntimeVector128.Zero.WithUInt64(0, 0x0UL).ShiftLeftLogical(unchecked((int)0x40UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x3CUL))), v0);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x3CUL))), v0);
#endif
        __arm64_pair_address_13264544 = unchecked((ulong)((sp) + (0x20UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13264544, v0);
#else
        __WriteVector128(__arm64_pair_address_13264544, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13264544) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13264544) + (0x10UL))), v0);
#endif
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x30UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCA75F4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794C14UL /* metadata target: GameObject.get_transform */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCA75F4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179D508UL /* metadata target: Transform.get_position */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x30UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCA75F4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        v8 = v0;
        v9 = v1;
        v10 = v2;
        x0 = RuntimeCalls.InvokeDirect(0x1794C14UL /* metadata target: GameObject.get_transform */, x0, x1, x2, x3);
        x23 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x23) + (0x3E3UL))))))));
        x20 = x0;
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCA6700;
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
        RuntimeMemory.WriteU8(unchecked((ulong)((x23) + (0x3E3UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCA6700;
        label_0xCA6700:
        ;
        if ((x20 == 0x0UL))
        {
            goto label_0xCA75F4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x24 = 0x1A8C000UL;
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((x24) + (0x1E8UL))));
        x22 = 0x1A8D000UL;
        x0 = x20;
        x1 = 0x0UL;
        x8 = RuntimeMemory.ReadU64(x24);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        __arm64_pair_address_13264672 = unchecked((ulong)((x8) + (0x4CUL)));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13264672)), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13264672) + (0x4UL))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x48UL))))), 0));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x4A8UL))));
        x0 = RuntimeCalls.InvokeDirect(0x179E01CUL /* metadata target: Transform.TransformDirection */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x22);
        v11 = v0;
        v12 = v1;
        v13 = v2;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCA674C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCA6748UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCA674C;
        label_0xCA674C:
        ;
        x0 = unchecked((ulong)((sp) + (0x20UL)));
        v0 = v8;
        v1 = v9;
        v2 = v10;
        v3 = v11;
        v4 = v12;
        v5 = v13;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17CBDECUL /* metadata target: Physics.Raycast */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCA6824;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = unchecked((ulong)((sp) + (0x20UL)));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17CEC58UL /* metadata target: RaycastHit.get_collider */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCA75F4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792704UL /* metadata target: Component.get_tag */, x0, x1, x2, x3);
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x2 = 0x0UL;
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x13F610CUL /* metadata target: String.op_Equality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCA67D4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = unchecked((ulong)((sp) + (0x20UL)));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17CEC58UL /* metadata target: RaycastHit.get_collider */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCA75F4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792704UL /* metadata target: Component.get_tag */, x0, x1, x2, x3);
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x3C8UL))));
        x2 = 0x0UL;
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x13F610CUL /* metadata target: String.op_Equality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCA6810;
        }
        else
        {
            goto label_0xCA67D4;
        }
        label_0xCA67D4:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x28UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCA75F4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794CD0UL /* metadata target: GameObject.SetActive */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x88UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCA6824;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x80UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCA75F4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x78UL))));
        x2 = 0x0UL;
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0x176A664UL /* metadata target: AudioSource.PlayOneShot */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x88UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCA6824;
        label_0xCA6810:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x28UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCA75F4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794CD0UL /* metadata target: GameObject.SetActive */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xCA6824;
        label_0xCA6824:
        ;
        x26 = 0x1A8C000UL;
        x26 = RuntimeMemory.ReadU64(unchecked((ulong)((x26) + (0xD8UL))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x20UL))));
        x0 = RuntimeMemory.ReadU64(x26);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCA6840;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCA683CUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xCA6840;
        label_0xCA6840:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1798274UL /* metadata target: Object.op_Implicit */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCA6860;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x20UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCA75F4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x3CEUL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCA6894;
        }
        else
        {
            goto label_0xCA6860;
        }
        label_0xCA6860:
        ;
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x89UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        goto label_0xCA6864;
        label_0xCA6864:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0xD0UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xD0UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0xC0UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xC0UL)))) + (0x8UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0xB0UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xB0UL)))) + (0x8UL))));
        x26 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0xA0UL))));
        x25 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xA0UL)))) + (0x8UL))));
        x28 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x90UL))));
        x27 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x90UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x88UL))));
        __arm64_pair_address_13265020 = unchecked((ulong)((sp) + (0x78UL)));
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13265020)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13265020) + (0x8UL))))), 0));
        __arm64_pair_address_13265024 = unchecked((ulong)((sp) + (0x68UL)));
        v11 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13265024)), 0));
        v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13265024) + (0x8UL))))), 0));
        __arm64_pair_address_13265028 = unchecked((ulong)((sp) + (0x58UL)));
        v13 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13265028)), 0));
        v12 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13265028) + (0x8UL))))), 0));
        v14 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((sp) + (0x50UL))))), 0));
        sp = unchecked((ulong)((sp) + (0xE0UL)));
        return x0;
        label_0xCA6894:
        ;
        x21 = 0x1A8C000UL;
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xE0UL))));
        x0 = RuntimeMemory.ReadU64(x21);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCA68AC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCA68A8UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCA68AC;
        label_0xCA68AC:
        ;
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x8UL))));
        x1 = 0x0UL;
        x0 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xC36390UL /* metadata target: CF2Input.GetButton */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)(0x1UL)))))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0xBCUL))), unchecked((byte)(unchecked((uint)(x8)))));
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xFD0UL))));
        x1 = 0x0UL;
        x0 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xC36390UL /* metadata target: CF2Input.GetButton */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)(0x1UL)))))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0xBDUL))), unchecked((byte)(unchecked((uint)(x8)))));
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x418UL))));
        x1 = 0x0UL;
        x0 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xC36390UL /* metadata target: CF2Input.GetButton */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)(0x1UL)))))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0xBEUL))), unchecked((byte)(unchecked((uint)(x8)))));
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x3E8UL))));
        x1 = 0x0UL;
        x0 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xC36390UL /* metadata target: CF2Input.GetButton */, x0, x1, x2, x3);
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0xBCUL))))))));
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0xBDUL))))))));
        x10 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)(0x1UL)))))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0xBFUL))), unchecked((byte)(unchecked((uint)(x10)))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCA6934;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCA6928UL);
        }
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCA693C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCA692CUL);
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0xBF800000UL)), 0)), 0));
        goto label_0xCA6940;
        label_0xCA6934:
        ;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCA6940;
        }
        else
        {
            goto label_0xCA693C;
        }
        label_0xCA693C:
        ;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        goto label_0xCA6940;
        label_0xCA6940:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0xBEUL))))))));
        RuntimeMemory.WriteF32(unchecked((ulong)((x19) + (0xC0UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCA69B0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCA694CUL);
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCA6958;
        }
        else
        {
            goto label_0xCA6954;
        }
        label_0xCA6954:
        ;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        goto label_0xCA6958;
        label_0xCA6958:
        ;
        RuntimeMemory.WriteF32(unchecked((ulong)((x19) + (0xC4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        x0 = RuntimeMemory.ReadU64(x21);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCA696C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCA6968UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCA696C;
        label_0xCA696C:
        ;
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x4E8UL))));
        x1 = 0x0UL;
        x0 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xC35E20UL /* metadata target: CF2Input.GetAxis */, x0, x1, x2, x3);
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x428UL))));
        x1 = 0x0UL;
        v8 = v0;
        x0 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xC35E20UL /* metadata target: CF2Input.GetAxis */, x0, x1, x2, x3);
        __arm64_pair_address_13265304 = unchecked((ulong)((x19) + (0xCCUL)));
        RuntimeMemory.WriteF32(__arm64_pair_address_13265304, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_13265304) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        x20 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x243UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCA69BC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        v9 = v0;
        goto label_0xCA69D4;
        label_0xCA69B0:
        ;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0xBF800000UL)), 0)), 0));
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCA6954;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCA69B8UL);
        }
        goto label_0xCA6958;
        label_0xCA69BC:
        ;
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xA60UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x243UL))), unchecked((byte)(unchecked((uint)(x8)))));
        __arm64_pair_address_13265360 = unchecked((ulong)((x19) + (0xCCUL)));
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13265360)), 0));
        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13265360) + (0x4UL))))), 0));
        goto label_0xCA69D4;
        label_0xCA69D4:
        ;
        x25 = 0x1A8C000UL;
        x25 = RuntimeMemory.ReadU64(unchecked((ulong)((x25) + (0xA60UL))));
        x0 = RuntimeMemory.ReadU64(x25);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCA69EC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCA69E8UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCA69EC;
        label_0xCA69EC:
        ;
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0xC8UL))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)(global::System.Math.Sqrt(unchecked((double)(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))))), 0));
        __arm64_float_flags_left_13265408 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13265408 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        x27 = 0x432000UL;
        RuntimeCalls.Unsupported("b.pl", 0xCA6A08UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xCA6A44;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x28 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x28) + (0x1E0UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCA6A2C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x138UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x28) + (0x1E0UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCA6A2C;
        label_0xCA6A2C:
        ;
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x138UL))));
        x8 = RuntimeMemory.ReadU64(x8);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(x8)), 0));
        goto label_0xCA6B24;
        label_0xCA6A44:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x243UL))))))));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((x19) + (0xCCUL))))), 0));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCA6A64;
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
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x243UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCA6A64;
        label_0xCA6A64:
        ;
        x0 = RuntimeMemory.ReadU64(x25);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCA6A74;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCA6A70UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCA6A74;
        label_0xCA6A74:
        ;
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x27) + (0x41CUL))))), 0));
        RuntimeCalls.Unsupported("fmul", 0xCA6A78UL);
        RuntimeCalls.Unsupported("faddp", 0xCA6A7CUL);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)(global::System.Math.Sqrt(unchecked((double)(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))))), 0));
        __arm64_float_flags_left_13265540 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13265540 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_13265540 <= __arm64_float_flags_right_13265540) || ((__arm64_float_flags_left_13265540 != __arm64_float_flags_left_13265540) || (__arm64_float_flags_right_13265540 != __arm64_float_flags_right_13265540))))
        {
            goto label_0xCA6A98;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCA6A8CUL);
        }
        v0 = (RuntimeVector128.Zero.WithUInt32(0, v0.GetUInt32(0)) | RuntimeVector128.Zero.WithUInt32(0, v0.GetUInt32(0)).ShiftLeftLogical(unchecked((int)0x20UL)));
        RuntimeCalls.Unsupported("fdiv", 0xCA6A90UL);
        goto label_0xCA6ACC;
        label_0xCA6A98:
        ;
        x28 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x28) + (0x1E0UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCA6AB8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x138UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x28) + (0x1E0UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCA6AB8;
        label_0xCA6AB8:
        ;
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x138UL))));
        x8 = RuntimeMemory.ReadU64(x8);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(x8)), 0));
        goto label_0xCA6ACC;
        label_0xCA6ACC:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x243UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCA6AE8;
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
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x243UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCA6AE8;
        label_0xCA6AE8:
        ;
        x0 = RuntimeMemory.ReadU64(x25);
        __arm64_pair_address_13265644 = unchecked((ulong)((x19) + (0xCCUL)));
        v10 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13265644)), 0));
        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13265644) + (0x4UL))))), 0));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCA6AFC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCA6AF8UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCA6AFC;
        label_0xCA6AFC:
        ;
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0xC8UL))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)(global::System.Math.Sqrt(unchecked((double)(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        RuntimeCalls.Unsupported("fmul", 0xCA6B20UL);
        goto label_0xCA6B24;
        label_0xCA6B24:
        ;
        RuntimeMemory.WriteF64(unchecked((ulong)((x19) + (0xCCUL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))));
        x0 = RuntimeMemory.ReadU64(x21);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCA6B38;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCA6B34UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCA6B38;
        label_0xCA6B38:
        ;
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x410UL))));
        x1 = 0x0UL;
        x0 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xC35E20UL /* metadata target: CF2Input.GetAxis */, x0, x1, x2, x3);
        x0 = 0x0UL;
        RuntimeMemory.WriteF64(unchecked((ulong)((sp) + (0x10UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))));
        x0 = RuntimeCalls.InvokeDirect(0x179AE30UL /* metadata target: Time.get_smoothDeltaTime */, x0, x1, x2, x3);
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x4F0UL))));
        x1 = 0x0UL;
        RuntimeMemory.WriteF64(sp, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))));
        x0 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xC35E20UL /* metadata target: CF2Input.GetAxis */, x0, x1, x2, x3);
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x10UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((sp) + (0x10UL))));
#endif
        x0 = 0x0UL;
        v1 = v0;
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x10UL))), v1);
#endif
        RuntimeCalls.Unsupported("fabs", 0xCA6B80UL);
        x0 = RuntimeCalls.InvokeDirect(0x179AE30UL /* metadata target: Time.get_smoothDeltaTime */, x0, x1, x2, x3);
#if IL2CPPREC_RUNTIME_VECTOR128
        v3 = RuntimeMemory.ReadVector128(sp);
#else
        v3 = __ReadVector128(sp);
#endif
        v1 = (RuntimeVector128.Zero.WithUInt32(0, unchecked((uint)((unchecked((uint)0x3EUL)) << (int)(unchecked((int)(unchecked((uint)0x18UL))))))) | RuntimeVector128.Zero.WithUInt32(0, unchecked((uint)((unchecked((uint)0x3EUL)) << (int)(unchecked((int)(unchecked((uint)0x18UL))))))).ShiftLeftLogical(unchecked((int)0x20UL)));
        v2 = (RuntimeVector128.Zero.WithUInt32(0, unchecked((uint)((unchecked((uint)0x41UL)) << (int)(unchecked((int)(unchecked((uint)0x18UL))))))) | RuntimeVector128.Zero.WithUInt32(0, unchecked((uint)((unchecked((uint)0x41UL)) << (int)(unchecked((int)(unchecked((uint)0x18UL))))))).ShiftLeftLogical(unchecked((int)0x20UL)));
        x8 = unchecked((ulong)(unchecked((uint)(0x42700000UL))));
        v3 = v0;
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x10UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((sp) + (0x10UL))));
#endif
        RuntimeCalls.Unsupported("fmul", 0xCA6BA0UL);
        RuntimeCalls.Unsupported("fmul", 0xCA6BA4UL);
        RuntimeCalls.Unsupported("fmul", 0xCA6BA8UL);
        RuntimeCalls.Unsupported("fmul", 0xCA6BACUL);
        v1 = (RuntimeVector128.Zero.WithUInt32(0, unchecked((uint)(x8))) | RuntimeVector128.Zero.WithUInt32(0, unchecked((uint)(x8))).ShiftLeftLogical(unchecked((int)0x20UL)));
        RuntimeCalls.Unsupported("fmul", 0xCA6BB4UL);
        RuntimeMemory.WriteF64(unchecked((ulong)((x19) + (0xD4UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x243UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCA6BDC;
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
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x243UL))), unchecked((byte)(unchecked((uint)(x8)))));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((x19) + (0xD4UL))))), 0));
        goto label_0xCA6BDC;
        label_0xCA6BDC:
        ;
        x0 = RuntimeMemory.ReadU64(x25);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCA6BEC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCA6BE8UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCA6BEC;
        label_0xCA6BEC:
        ;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0xC8UL))))), 0));
        RuntimeCalls.Unsupported("fmul", 0xCA6BF0UL);
        RuntimeCalls.Unsupported("faddp", 0xCA6BF4UL);
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)(global::System.Math.Sqrt(unchecked((double)(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))))), 0));
        __arm64_float_flags_left_13265916 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13265916 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_13265916 >= __arm64_float_flags_right_13265916) || ((__arm64_float_flags_left_13265916 != __arm64_float_flags_left_13265916) || (__arm64_float_flags_right_13265916 != __arm64_float_flags_right_13265916))))
        {
            goto label_0xCA6C3C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x1E0UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCA6C24;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x138UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x1E0UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCA6C24;
        label_0xCA6C24:
        ;
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x138UL))));
        x8 = RuntimeMemory.ReadU64(x8);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(x8)), 0));
        goto label_0xCA6D1C;
        label_0xCA6C3C:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x243UL))))))));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((x19) + (0xD4UL))))), 0));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCA6C5C;
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
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x243UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCA6C5C;
        label_0xCA6C5C:
        ;
        x0 = RuntimeMemory.ReadU64(x25);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCA6C6C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCA6C68UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCA6C6C;
        label_0xCA6C6C:
        ;
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x27) + (0x41CUL))))), 0));
        RuntimeCalls.Unsupported("fmul", 0xCA6C70UL);
        RuntimeCalls.Unsupported("faddp", 0xCA6C74UL);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)(global::System.Math.Sqrt(unchecked((double)(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))))), 0));
        __arm64_float_flags_left_13266044 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13266044 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_13266044 <= __arm64_float_flags_right_13266044) || ((__arm64_float_flags_left_13266044 != __arm64_float_flags_left_13266044) || (__arm64_float_flags_right_13266044 != __arm64_float_flags_right_13266044))))
        {
            goto label_0xCA6C90;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCA6C84UL);
        }
        v0 = (RuntimeVector128.Zero.WithUInt32(0, v0.GetUInt32(0)) | RuntimeVector128.Zero.WithUInt32(0, v0.GetUInt32(0)).ShiftLeftLogical(unchecked((int)0x20UL)));
        RuntimeCalls.Unsupported("fdiv", 0xCA6C88UL);
        goto label_0xCA6CC4;
        label_0xCA6C90:
        ;
        x27 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x27) + (0x1E0UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCA6CB0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x138UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x27) + (0x1E0UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCA6CB0;
        label_0xCA6CB0:
        ;
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x138UL))));
        x8 = RuntimeMemory.ReadU64(x8);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(x8)), 0));
        goto label_0xCA6CC4;
        label_0xCA6CC4:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x243UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCA6CE0;
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
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x243UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCA6CE0;
        label_0xCA6CE0:
        ;
        x0 = RuntimeMemory.ReadU64(x25);
        __arm64_pair_address_13266148 = unchecked((ulong)((x19) + (0xD4UL)));
        v10 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13266148)), 0));
        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13266148) + (0x4UL))))), 0));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCA6CF4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCA6CF0UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCA6CF4;
        label_0xCA6CF4:
        ;
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0xC8UL))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)(global::System.Math.Sqrt(unchecked((double)(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        RuntimeCalls.Unsupported("fmul", 0xCA6D18UL);
        goto label_0xCA6D1C;
        label_0xCA6D1C:
        ;
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((x19) + (0xC0UL))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((x19) + (0xCCUL))))), 0));
        RuntimeMemory.WriteF64(unchecked((ulong)((x19) + (0xD4UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))));
        RuntimeCalls.Unsupported("fmov", 0xCA6D28UL);
        RuntimeCalls.Unsupported("fmov", 0xCA6D2CUL);
        RuntimeCalls.Unsupported("fadd", 0xCA6D30UL);
        RuntimeCalls.Unsupported("fcmgt", 0xCA6D34UL);
        RuntimeCalls.Unsupported("fmin", 0xCA6D38UL);
        RuntimeCalls.Unsupported("bif", 0xCA6D3CUL);
        RuntimeMemory.WriteF64(unchecked((ulong)((x19) + (0xDCUL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))));
        x0 = RuntimeMemory.ReadU64(x21);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCA6D54;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCA6D50UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCA6D54;
        label_0xCA6D54:
        ;
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x550UL))));
        x1 = 0x0UL;
        x0 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xC360D8UL /* metadata target: CF2Input.GetAxisRaw */, x0, x1, x2, x3);
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0xD4UL))))), 0));
        x8 = 0x1A8C000UL;
        x1 = 0x0UL;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((x19) + (0xE4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x530UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xC360D8UL /* metadata target: CF2Input.GetAxisRaw */, x0, x1, x2, x3);
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0xD8UL))))), 0));
        x8 = 0x1A8E000UL;
        x1 = 0x0UL;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((x19) + (0xE8UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x440UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xC360D8UL /* metadata target: CF2Input.GetAxisRaw */, x0, x1, x2, x3);
        x8 = 0x432000UL;
        v14 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x3B8UL))))), 0));
        __arm64_float_flags_left_13266352 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13266352 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v14.GetUInt64(0)))), 0);
        if ((__arm64_float_flags_left_13266352 > __arm64_float_flags_right_13266352))
        {
            goto label_0xCA6DE0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(x21);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCA6DC8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCA6DC4UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCA6DC8;
        label_0xCA6DC8:
        ;
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x4B8UL))));
        x1 = 0x0UL;
        x0 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xC36390UL /* metadata target: CF2Input.GetButton */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCA6DEC;
        }
        else
        {
            goto label_0xCA6DE0;
        }
        label_0xCA6DE0:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x89UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCA6FE0;
        label_0xCA6DEC:
        ;
        x0 = RuntimeMemory.ReadU64(x26);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x58UL))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCA6E00;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCA6DFCUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCA6E00;
        label_0xCA6E00:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1798274UL /* metadata target: Object.op_Implicit */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCA6FDC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x30UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCA75F4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794C14UL /* metadata target: GameObject.get_transform */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCA75F4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179D508UL /* metadata target: Transform.get_position */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x30UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCA75F4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        v8 = v0;
        v9 = v1;
        v10 = v2;
        x0 = RuntimeCalls.InvokeDirect(0x1794C14UL /* metadata target: GameObject.get_transform */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x23) + (0x3E3UL))))))));
        x20 = x0;
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCA6E68;
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
        RuntimeMemory.WriteU8(unchecked((ulong)((x23) + (0x3E3UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCA6E68;
        label_0xCA6E68:
        ;
        if ((x20 == 0x0UL))
        {
            goto label_0xCA75F4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x24);
        x0 = x20;
        x1 = 0x0UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        __arm64_pair_address_13266556 = unchecked((ulong)((x8) + (0x4CUL)));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13266556)), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13266556) + (0x4UL))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x48UL))))), 0));
        x0 = RuntimeCalls.InvokeDirect(0x179E01CUL /* metadata target: Transform.TransformDirection */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x22);
        v11 = v0;
        v12 = v1;
        v13 = v2;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCA6EA4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCA6EA0UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCA6EA4;
        label_0xCA6EA4:
        ;
        x0 = unchecked((ulong)((sp) + (0x20UL)));
        v0 = v8;
        v1 = v9;
        v2 = v10;
        v3 = v11;
        v4 = v12;
        v5 = v13;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17CBDECUL /* metadata target: Physics.Raycast */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCA6FDC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = unchecked((ulong)((sp) + (0x20UL)));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17CEC58UL /* metadata target: RaycastHit.get_collider */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCA75F4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792704UL /* metadata target: Component.get_tag */, x0, x1, x2, x3);
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x2 = 0x0UL;
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x13F610CUL /* metadata target: String.op_Equality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCA6F2C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = unchecked((ulong)((sp) + (0x20UL)));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17CEC58UL /* metadata target: RaycastHit.get_collider */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCA75F4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792704UL /* metadata target: Component.get_tag */, x0, x1, x2, x3);
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x3C8UL))));
        x2 = 0x0UL;
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x13F610CUL /* metadata target: String.op_Equality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCA6FDC;
        }
        else
        {
            goto label_0xCA6F2C;
        }
        label_0xCA6F2C:
        ;
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792154UL /* metadata target: Component.get_transform */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCA75F4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179D508UL /* metadata target: Transform.get_position */, x0, x1, x2, x3);
        x0 = unchecked((ulong)((sp) + (0x20UL)));
        x1 = 0x0UL;
        v8 = v0;
        v9 = v1;
        v10 = v2;
        x0 = RuntimeCalls.InvokeDirect(0x17CED24UL /* metadata target: RaycastHit.get_transform */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCA75F4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179D508UL /* metadata target: Transform.get_position */, x0, x1, x2, x3);
        x20 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x3E0UL))))))));
        v11 = v0;
        v12 = v1;
        v13 = v2;
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCA6F94;
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
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x3E0UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCA6F94;
        label_0xCA6F94:
        ;
        x0 = RuntimeMemory.ReadU64(x25);
        v11 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0))))), 0));
        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v12.GetUInt64(0)))), 0))))), 0));
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v13.GetUInt64(0)))), 0))))), 0));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCA6FB0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCA6FACUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCA6FB0;
        label_0xCA6FB0:
        ;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)(global::System.Math.Sqrt(unchecked((double)(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x41F00000UL)), 0)), 0));
        __arm64_float_flags_left_13266892 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13266892 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_13266892 > __arm64_float_flags_right_13266892) || ((__arm64_float_flags_left_13266892 != __arm64_float_flags_left_13266892) || (__arm64_float_flags_right_13266892 != __arm64_float_flags_right_13266892))))
        {
            goto label_0xCA6FE0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x70UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCA6DE0;
        }
        else
        {
            goto label_0xCA6FDC;
        }
        label_0xCA6FDC:
        ;
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x89UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        goto label_0xCA6FE0;
        label_0xCA6FE0:
        ;
        x0 = RuntimeMemory.ReadU64(x21);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCA6FF0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCA6FECUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCA6FF0;
        label_0xCA6FF0:
        ;
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x4A0UL))));
        x1 = 0x0UL;
        x0 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xC360D8UL /* metadata target: CF2Input.GetAxisRaw */, x0, x1, x2, x3);
        __arm64_float_flags_left_13266948 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13266948 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v14.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_13266948 <= __arm64_float_flags_right_13266948) || ((__arm64_float_flags_left_13266948 != __arm64_float_flags_left_13266948) || (__arm64_float_flags_right_13266948 != __arm64_float_flags_right_13266948))))
        {
            goto label_0xCA7014;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        goto label_0xCA703C;
        label_0xCA7014:
        ;
        x0 = RuntimeMemory.ReadU64(x21);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCA7024;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCA7020UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCA7024;
        label_0xCA7024:
        ;
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x3B0UL))));
        x1 = 0x0UL;
        x0 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xC36390UL /* metadata target: CF2Input.GetButton */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)(0x1UL)))))));
        goto label_0xCA703C;
        label_0xCA703C:
        ;
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x92UL))), unchecked((byte)(unchecked((uint)(x8)))));
        x0 = RuntimeMemory.ReadU64(x21);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCA7050;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCA704CUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCA7050;
        label_0xCA7050:
        ;
        x20 = 0x1A8E000UL;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x4E0UL))));
        x1 = 0x0UL;
        x0 = RuntimeMemory.ReadU64(x20);
        x0 = RuntimeCalls.InvokeDirect(0xC35E20UL /* metadata target: CF2Input.GetAxis */, x0, x1, x2, x3);
        __arm64_float_flags_left_13267044 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13267044 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        if (((__arm64_float_flags_left_13267044 <= __arm64_float_flags_right_13267044) || ((__arm64_float_flags_left_13267044 != __arm64_float_flags_left_13267044) || (__arm64_float_flags_right_13267044 != __arm64_float_flags_right_13267044))))
        {
            goto label_0xCA7088;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0xF5UL))))))));
        x9 = unchecked((ulong)(unchecked((uint)(0x100UL))));
        RuntimeMemory.WriteU16(unchecked((ulong)((x19) + (0xECUL))), unchecked((ushort)(unchecked((uint)(x9)))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0xF4UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCA70DC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCA7080UL);
        }
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0xF1UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        goto label_0xCA70F4;
        label_0xCA7088:
        ;
        x0 = RuntimeMemory.ReadU64(x21);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCA7098;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCA7094UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCA7098;
        label_0xCA7098:
        ;
        x0 = RuntimeMemory.ReadU64(x20);
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC35E20UL /* metadata target: CF2Input.GetAxis */, x0, x1, x2, x3);
        __arm64_float_flags_left_13267108 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13267108 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0xEDUL))), unchecked((byte)(unchecked((uint)0x0UL))));
        RuntimeCalls.Unsupported("b.pl", 0xCA70ACUL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xCA70CC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0xF4UL))))))));
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0xECUL))), unchecked((byte)(unchecked((uint)(x8)))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0xF5UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCA70EC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCA70C4UL);
        }
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0xF0UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        goto label_0xCA70F4;
        label_0xCA70CC:
        ;
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0xECUL))), unchecked((byte)(unchecked((uint)0x0UL))));
        RuntimeMemory.WriteU16(unchecked((ulong)((x19) + (0xF0UL))), unchecked((ushort)(unchecked((uint)0x0UL))));
        RuntimeMemory.WriteU16(unchecked((ulong)((x19) + (0xF4UL))), unchecked((ushort)(unchecked((uint)0x0UL))));
        goto label_0xCA70F4;
        label_0xCA70DC:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0xF1UL))), unchecked((byte)(unchecked((uint)(x8)))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0xF5UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCA70F4;
        label_0xCA70EC:
        ;
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0xF0UL))), unchecked((byte)(unchecked((uint)(x8)))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0xF4UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCA70F4;
        label_0xCA70F4:
        ;
        x0 = RuntimeMemory.ReadU64(x21);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCA7104;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCA7100UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCA7104;
        label_0xCA7104:
        ;
        x20 = 0x1A8E000UL;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x3D8UL))));
        x1 = 0x0UL;
        x0 = RuntimeMemory.ReadU64(x20);
        x0 = RuntimeCalls.InvokeDirect(0xC35E20UL /* metadata target: CF2Input.GetAxis */, x0, x1, x2, x3);
        __arm64_float_flags_left_13267224 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13267224 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        if (((__arm64_float_flags_left_13267224 <= __arm64_float_flags_right_13267224) || ((__arm64_float_flags_left_13267224 != __arm64_float_flags_left_13267224) || (__arm64_float_flags_right_13267224 != __arm64_float_flags_right_13267224))))
        {
            goto label_0xCA713C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0xF6UL))))))));
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU16(unchecked((ulong)((x19) + (0xEEUL))), unchecked((ushort)(unchecked((uint)(x8)))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0xF7UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCA7190;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCA7134UL);
        }
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0xF2UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        goto label_0xCA71A4;
        label_0xCA713C:
        ;
        x0 = RuntimeMemory.ReadU64(x21);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCA714C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCA7148UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCA714C;
        label_0xCA714C:
        ;
        x0 = RuntimeMemory.ReadU64(x20);
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC35E20UL /* metadata target: CF2Input.GetAxis */, x0, x1, x2, x3);
        __arm64_float_flags_left_13267288 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13267288 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0xEEUL))), unchecked((byte)(unchecked((uint)0x0UL))));
        RuntimeCalls.Unsupported("b.pl", 0xCA7160UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xCA7180;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0xF7UL))))))));
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0xEFUL))), unchecked((byte)(unchecked((uint)(x8)))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0xF6UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCA719C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCA7178UL);
        }
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0xF3UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        goto label_0xCA71A4;
        label_0xCA7180:
        ;
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0xEFUL))), unchecked((byte)(unchecked((uint)0x0UL))));
        RuntimeMemory.WriteU16(unchecked((ulong)((x19) + (0xF2UL))), unchecked((ushort)(unchecked((uint)0x0UL))));
        RuntimeMemory.WriteU16(unchecked((ulong)((x19) + (0xF6UL))), unchecked((ushort)(unchecked((uint)0x0UL))));
        goto label_0xCA71A4;
        label_0xCA7190:
        ;
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0xF2UL))), unchecked((byte)(unchecked((uint)(x8)))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0xF6UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCA71A4;
        label_0xCA719C:
        ;
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0xF3UL))), unchecked((byte)(unchecked((uint)(x8)))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0xF7UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCA71A4;
        label_0xCA71A4:
        ;
        x0 = RuntimeMemory.ReadU64(x21);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCA71B4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCA71B0UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCA71B4;
        label_0xCA71B4:
        ;
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xFD0UL))));
        x1 = 0x0UL;
        x0 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xC35E20UL /* metadata target: CF2Input.GetAxis */, x0, x1, x2, x3);
        RuntimeMemory.WriteF32(unchecked((ulong)((x19) + (0xB8UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x4B8UL))));
        x1 = 0x0UL;
        x0 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xC36634UL /* metadata target: CF2Input.GetButtonDown */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)(0x1UL)))))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x8AUL))), unchecked((byte)(unchecked((uint)(x8)))));
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x3B0UL))));
        x1 = 0x0UL;
        x0 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xC36634UL /* metadata target: CF2Input.GetButtonDown */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)(0x1UL)))))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x93UL))), unchecked((byte)(unchecked((uint)(x8)))));
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x498UL))));
        x1 = 0x0UL;
        x0 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xC36634UL /* metadata target: CF2Input.GetButtonDown */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)(0x1UL)))))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x8BUL))), unchecked((byte)(unchecked((uint)(x8)))));
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x3A0UL))));
        x1 = 0x0UL;
        x0 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xC36634UL /* metadata target: CF2Input.GetButtonDown */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)(0x1UL)))))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x8CUL))), unchecked((byte)(unchecked((uint)(x8)))));
        x20 = 0x1A8C000UL;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x540UL))));
        x1 = 0x0UL;
        x0 = RuntimeMemory.ReadU64(x20);
        x0 = RuntimeCalls.InvokeDirect(0xC36390UL /* metadata target: CF2Input.GetButton */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)(0x1UL)))))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x8DUL))), unchecked((byte)(unchecked((uint)(x8)))));
        x0 = RuntimeMemory.ReadU64(x20);
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC36634UL /* metadata target: CF2Input.GetButtonDown */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)(0x1UL)))))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x8EUL))), unchecked((byte)(unchecked((uint)(x8)))));
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x620UL))));
        x1 = 0x0UL;
        x0 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xC36390UL /* metadata target: CF2Input.GetButton */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)(0x1UL)))))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x8FUL))), unchecked((byte)(unchecked((uint)(x8)))));
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x3B8UL))));
        x1 = 0x0UL;
        x0 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xC36390UL /* metadata target: CF2Input.GetButton */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)(0x1UL)))))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x90UL))), unchecked((byte)(unchecked((uint)(x8)))));
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x3A8UL))));
        x1 = 0x0UL;
        x0 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xC36390UL /* metadata target: CF2Input.GetButton */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)(0x1UL)))))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x91UL))), unchecked((byte)(unchecked((uint)(x8)))));
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x470UL))));
        x1 = 0x0UL;
        x0 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xC36390UL /* metadata target: CF2Input.GetButton */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)(0x1UL)))))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x94UL))), unchecked((byte)(unchecked((uint)(x8)))));
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x3F0UL))));
        x1 = 0x0UL;
        x0 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xC36390UL /* metadata target: CF2Input.GetButton */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)(0x1UL)))))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x95UL))), unchecked((byte)(unchecked((uint)(x8)))));
        x20 = 0x1A8E000UL;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x4D0UL))));
        x1 = 0x0UL;
        x0 = RuntimeMemory.ReadU64(x20);
        x0 = RuntimeCalls.InvokeDirect(0xC36390UL /* metadata target: CF2Input.GetButton */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)(0x1UL)))))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x96UL))), unchecked((byte)(unchecked((uint)(x8)))));
        x0 = RuntimeMemory.ReadU64(x20);
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC36634UL /* metadata target: CF2Input.GetButtonDown */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)(0x1UL)))))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x97UL))), unchecked((byte)(unchecked((uint)(x8)))));
        x0 = RuntimeMemory.ReadU64(x20);
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC368E4UL /* metadata target: CF2Input.GetButtonUp */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)(0x1UL)))))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x98UL))), unchecked((byte)(unchecked((uint)(x8)))));
        x20 = 0x1A8E000UL;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x3C0UL))));
        x1 = 0x0UL;
        x0 = RuntimeMemory.ReadU64(x20);
        x0 = RuntimeCalls.InvokeDirect(0xC36390UL /* metadata target: CF2Input.GetButton */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)(0x1UL)))))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x99UL))), unchecked((byte)(unchecked((uint)(x8)))));
        x0 = RuntimeMemory.ReadU64(x20);
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC36634UL /* metadata target: CF2Input.GetButtonDown */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)(0x1UL)))))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x9AUL))), unchecked((byte)(unchecked((uint)(x8)))));
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x3F8UL))));
        x1 = 0x0UL;
        x0 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xC36390UL /* metadata target: CF2Input.GetButton */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)(0x1UL)))))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x9BUL))), unchecked((byte)(unchecked((uint)(x8)))));
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x448UL))));
        x1 = 0x0UL;
        x0 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xC36634UL /* metadata target: CF2Input.GetButtonDown */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)(0x1UL)))))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x9DUL))), unchecked((byte)(unchecked((uint)(x8)))));
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x450UL))));
        x1 = 0x0UL;
        x0 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xC36634UL /* metadata target: CF2Input.GetButtonDown */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)(0x1UL)))))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x9EUL))), unchecked((byte)(unchecked((uint)(x8)))));
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x438UL))));
        x1 = 0x0UL;
        x0 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xC36634UL /* metadata target: CF2Input.GetButtonDown */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)(0x1UL)))))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x9FUL))), unchecked((byte)(unchecked((uint)(x8)))));
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x488UL))));
        x1 = 0x0UL;
        x0 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xC36634UL /* metadata target: CF2Input.GetButtonDown */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)(0x1UL)))))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0xA0UL))), unchecked((byte)(unchecked((uint)(x8)))));
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x420UL))));
        x1 = 0x0UL;
        x0 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xC36634UL /* metadata target: CF2Input.GetButtonDown */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)(0x1UL)))))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0xA1UL))), unchecked((byte)(unchecked((uint)(x8)))));
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x4F8UL))));
        x1 = 0x0UL;
        x0 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xC36634UL /* metadata target: CF2Input.GetButtonDown */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)(0x1UL)))))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x9CUL))), unchecked((byte)(unchecked((uint)(x8)))));
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x468UL))));
        x1 = 0x0UL;
        x0 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xC36634UL /* metadata target: CF2Input.GetButtonDown */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)(0x1UL)))))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0xA5UL))), unchecked((byte)(unchecked((uint)(x8)))));
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x480UL))));
        x1 = 0x0UL;
        x0 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xC36634UL /* metadata target: CF2Input.GetButtonDown */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)(0x1UL)))))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0xA6UL))), unchecked((byte)(unchecked((uint)(x8)))));
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x478UL))));
        x1 = 0x0UL;
        x0 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xC36634UL /* metadata target: CF2Input.GetButtonDown */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)(0x1UL)))))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0xA7UL))), unchecked((byte)(unchecked((uint)(x8)))));
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x430UL))));
        x1 = 0x0UL;
        x0 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xC36634UL /* metadata target: CF2Input.GetButtonDown */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)(0x1UL)))))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0xA8UL))), unchecked((byte)(unchecked((uint)(x8)))));
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x4B0UL))));
        x1 = 0x0UL;
        x0 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xC36634UL /* metadata target: CF2Input.GetButtonDown */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)(0x1UL)))))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0xA9UL))), unchecked((byte)(unchecked((uint)(x8)))));
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x4C0UL))));
        x1 = 0x0UL;
        x0 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xC36634UL /* metadata target: CF2Input.GetButtonDown */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)(0x1UL)))))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0xAAUL))), unchecked((byte)(unchecked((uint)(x8)))));
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x400UL))));
        x1 = 0x0UL;
        x0 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xC36634UL /* metadata target: CF2Input.GetButtonDown */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)(0x1UL)))))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0xABUL))), unchecked((byte)(unchecked((uint)(x8)))));
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x4A8UL))));
        x1 = 0x0UL;
        x0 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xC36634UL /* metadata target: CF2Input.GetButtonDown */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)(0x1UL)))))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0xACUL))), unchecked((byte)(unchecked((uint)(x8)))));
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x460UL))));
        x1 = 0x0UL;
        x0 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xC36634UL /* metadata target: CF2Input.GetButtonDown */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)(0x1UL)))))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0xADUL))), unchecked((byte)(unchecked((uint)(x8)))));
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x4D8UL))));
        x1 = 0x0UL;
        x0 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xC36634UL /* metadata target: CF2Input.GetButtonDown */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)(0x1UL)))))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0xAEUL))), unchecked((byte)(unchecked((uint)(x8)))));
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x408UL))));
        x1 = 0x0UL;
        x0 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xC36634UL /* metadata target: CF2Input.GetButtonDown */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)(0x1UL)))))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0xAFUL))), unchecked((byte)(unchecked((uint)(x8)))));
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x490UL))));
        x1 = 0x0UL;
        x0 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xC36634UL /* metadata target: CF2Input.GetButtonDown */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)(0x1UL)))))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0xB0UL))), unchecked((byte)(unchecked((uint)(x8)))));
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x4C8UL))));
        x1 = 0x0UL;
        x0 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xC36634UL /* metadata target: CF2Input.GetButtonDown */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)(0x1UL)))))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0xB1UL))), unchecked((byte)(unchecked((uint)(x8)))));
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x3D0UL))));
        x1 = 0x0UL;
        x0 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xC36634UL /* metadata target: CF2Input.GetButtonDown */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)(0x1UL)))))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0xB2UL))), unchecked((byte)(unchecked((uint)(x8)))));
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x3E0UL))));
        x1 = 0x0UL;
        x0 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xC36634UL /* metadata target: CF2Input.GetButtonDown */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)(0x1UL)))))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0xB3UL))), unchecked((byte)(unchecked((uint)(x8)))));
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x458UL))));
        x1 = 0x0UL;
        x0 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xC36634UL /* metadata target: CF2Input.GetButtonDown */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)(0x1UL)))))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0xB4UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCA6864;
        label_0xCA75F4:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `InputControl.AccelerateInput` — RVA `0xca75f8`

- Lift status: **exact**; input span: 72 bytes; span to next metadata RVA: 72 bytes.
- Metadata signature: `private float AccelerateInput(float input) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=13 (informational only).

```csharp
public static ulong InputControl_AccelerateInput_RVAca75f8(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_pair_address_13268472 = default(ulong);
        ulong __arm64_pair_address_13268536 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v8 = default(RuntimeVector128);
        RuntimeVector128 v9 = default(RuntimeVector128);
        ulong x30 = default(ulong);
        __arm64_pair_address_13268472 = unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13268472, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13268472) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        sp = __arm64_pair_address_13268472;
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x10UL))), x30);
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179AE30UL /* metadata target: Time.get_smoothDeltaTime */, x0, x1, x2, x3);
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        __arm64_pair_address_13268536 = sp;
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13268536)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13268536) + (0x8UL))))), 0));
        return x0;
        return default(ulong);
    }
```

## `InputControl.OnOffMehtod` — RVA `0xca7640`

- Lift status: **exact**; input span: 116 bytes; span to next metadata RVA: 116 bytes.
- Metadata signature: `public void OnOffMehtod() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=14 (informational only).

```csharp
public static ulong InputControl_OnOffMehtod_RVAca7640(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x8UL))), x19);
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x70UL))))))));
        x19 = x0;
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) ^ (unchecked((uint)(0x1UL)))))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x0) + (0x70UL))), unchecked((byte)(unchecked((uint)(x8)))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCA7664;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCA7658UL);
        }
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCA768C;
        }
        else
        {
            goto label_0xCA765C;
        }
        label_0xCA765C:
        ;
        x30 = RuntimeMemory.ReadU64(sp);
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return x0;
        label_0xCA7664:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x68UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCA76B0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x198CDF4UL /* metadata target: Selectable.get_image */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCA76B0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x58UL))));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1820A3CUL /* metadata target: Image.set_overrideSprite */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x70UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCA765C;
        }
        else
        {
            goto label_0xCA768C;
        }
        label_0xCA768C:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x68UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCA76B0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x198CDF4UL /* metadata target: Selectable.get_image */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCA76B0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x60UL))));
        x2 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeDirect(0x1820A3CUL /* metadata target: Image.set_overrideSprite */);
        label_0xCA76B0:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `InputControl.ctor` — RVA `0xca76b4`

- Lift status: **exact**; input span: 20 bytes; span to next metadata RVA: 20 bytes.
- Metadata signature: `public void .ctor() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=3 (informational only).

```csharp
public static ulong InputControl_ctor_RVAca76b4(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong x8 = default(ulong);
        x8 = unchecked((ulong)(unchecked((uint)(0xCCCDUL))));
        x8 = unchecked((ulong)(unchecked((uint)(unchecked((ulong)((unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((~(0xFFFFUL)))))))))) | (unchecked((ulong)((unchecked((ulong)((0x3E4CUL) << (int)(unchecked((int)(0x10UL)))))) << (int)(unchecked((int)(0x0UL))))))))))));
        x1 = 0x0UL;
        RuntimeMemory.WriteU32(unchecked((ulong)((x0) + (0xC8UL))), unchecked((uint)(x8)));
        return RuntimeCalls.InvokeDirect(0x1796274UL /* metadata target: MonoBehaviour.ctor */);
        return default(ulong);
    }
```
