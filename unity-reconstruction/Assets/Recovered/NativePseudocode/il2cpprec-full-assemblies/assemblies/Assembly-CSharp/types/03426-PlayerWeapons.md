# `PlayerWeapons` — TypeDefIndex 3426

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x20` | `GameObject` | `Joystick` |
| `0x28` | `GameObject` | `NextWeapon` |
| `0x30` | `GameObject` | `PreviousWeapon` |
| `0x38` | `GameObject` | `Sprintbutton` |
| `0x40` | `GameObject` | `WeaponPivot` |
| `0x48` | `GameObject` | `Autoshootbutt` |
| `0x50` | `int` | `LevelNum` |
| `0x54` | `int` | `weaponindex` |
| `0x58` | `Material` | `MaterialObj` |
| `0x60` | `Texture` | `MAt1` |
| `0x68` | `Texture` | `MAt2` |
| `0x70` | `GameObject` | `playerObj` |
| `0x78` | `GameObject` | `cameraObj` |
| `0x80` | `InputControl` | `InputComponent` |
| `0x88` | `FPSRigidBodyWalker` | `FPSWalkerComponent` |
| `0x90` | `FPSPlayer` | `FPSPlayerComponent` |
| `0x98` | `WeaponBehavior` | `CurrentWeaponBehaviorComponent` |
| `0xA0` | `Ironsights` | `IronsightsComponent` |
| `0xA8` | `CameraControl` | `CameraControlComponent` |
| `0xB0` | `Animator` | `WeaponObjAnimatorComponent` |
| `0xB8` | `Animator` | `CurWeaponObjAnimatorComponent` |
| `0xC0` | `Animator` | `CameraAnimatorComponent` |
| `0xC8` | `int` | `firstWeapon` |
| `0xCC` | `int` | `maxWeapons` |
| `0xD0` | `int` | `backupWeapon` |
| `0xD4` | `int` | `grenadeWeapon` |
| `0xD8` | `int` | `totalWeapons` |
| `0xDC` | `int` | `currentWeapon` |
| `0xE0` | `int` | `currentGrenade` |
| `0xE8` | `GameObject[]` | `weaponOrder` |
| `0xF0` | `WeaponBehavior[]` | `weaponBehaviors` |
| `0xF8` | `GameObject[]` | `grenadeOrder` |
| `0x100` | `Transform` | `myTransform` |
| `0x108` | `Transform` | `mainCamTransform` |
| `0x110` | `Color` | `waterMuzzleFlashColor` |
| `0x120` | `float` | `switchTime` |
| `0x124` | `float` | `sprintSwitchTime` |
| `0x128` | `bool` | `switching` |
| `0x129` | `bool` | `displayingGrenade` |
| `0x12C` | `float` | `grenDisplayTime` |
| `0x130` | `bool` | `sprintSwitching` |
| `0x131` | `bool` | `proneMove` |
| `0x132` | `bool` | `cameraToggleState` |
| `0x134` | `float` | `cameraToggleTime` |
| `0x138` | `bool` | `dropWeapon` |
| `0x139` | `bool` | `deadDropped` |
| `0x140` | `AudioClip` | `changesnd` |
| `0x148` | `bool` | `audioPaused` |
| `0x150` | `AudioSource[]` | `aSources` |
| `0x158` | `AudioSource` | `aSource` |
| `0x160` | `Transform` | `sunLightObj` |
| `0x168` | `Color` | `shadeColor` |
| `0x178` | `int` | `prevWepToGrenIndex` |
| `0x17C` | `bool` | `pullGrenadeState` |
| `0x17D` | `bool` | `grenadeThrownState` |
| `0x17E` | `bool` | `offhandThrowActive` |
| `0x180` | `WeaponBehavior` | `GrenadeWeaponBehaviorComponent` |
| `0x188` | `float` | `shellParentTime` |
| `0x18C` | `float` | `shellDzParentTime` |
| `0x190` | `float` | `shellBtParentTime` |

## `PlayerWeapons.Start` — RVA `0xcb1e14`

- Lift status: **partial**; input span: 2176 bytes; span to next metadata RVA: 2176 bytes.
- Metadata signature: `private void Start() { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=305 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'b.hi' at 0xcb22cc; reason: Unknown IR expression at 0xcb22cc

```csharp
public static ulong PlayerWeapons_Start_RVAcb1e14(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13312188 = default(uint);
        uint __arm64_flags_left_13312260 = default(uint);
        uint __arm64_flags_left_13312528 = default(uint);
        uint __arm64_flags_left_13312580 = default(uint);
        uint __arm64_flags_left_13312588 = default(uint);
        uint __arm64_flags_left_13312708 = default(uint);
        ulong __arm64_flags_left_13312740 = default(ulong);
        uint __arm64_flags_left_13312760 = default(uint);
        ulong __arm64_flags_left_13312916 = default(ulong);
        uint __arm64_flags_left_13312936 = default(uint);
        uint __arm64_flags_left_13313020 = default(uint);
        uint __arm64_flags_left_13313076 = default(uint);
        uint __arm64_flags_left_13313136 = default(uint);
        uint __arm64_flags_left_13313196 = default(uint);
        uint __arm64_flags_left_13313440 = default(uint);
        uint __arm64_flags_left_13313456 = default(uint);
        uint __arm64_flags_left_13313484 = default(uint);
        uint __arm64_flags_left_13313496 = default(uint);
        uint __arm64_flags_left_13313544 = default(uint);
        uint __arm64_flags_left_13313572 = default(uint);
        uint __arm64_flags_left_13313636 = default(uint);
        ulong __arm64_flags_result_13312740 = default(ulong);
        uint __arm64_flags_right_13312188 = default(uint);
        uint __arm64_flags_right_13312260 = default(uint);
        uint __arm64_flags_right_13312528 = default(uint);
        uint __arm64_flags_right_13312580 = default(uint);
        uint __arm64_flags_right_13312588 = default(uint);
        uint __arm64_flags_right_13312708 = default(uint);
        ulong __arm64_flags_right_13312740 = default(ulong);
        uint __arm64_flags_right_13312760 = default(uint);
        ulong __arm64_flags_right_13312916 = default(ulong);
        uint __arm64_flags_right_13312936 = default(uint);
        uint __arm64_flags_right_13313020 = default(uint);
        uint __arm64_flags_right_13313076 = default(uint);
        uint __arm64_flags_right_13313136 = default(uint);
        uint __arm64_flags_right_13313196 = default(uint);
        uint __arm64_flags_right_13313440 = default(uint);
        uint __arm64_flags_right_13313456 = default(uint);
        uint __arm64_flags_right_13313484 = default(uint);
        uint __arm64_flags_right_13313496 = default(uint);
        uint __arm64_flags_right_13313544 = default(uint);
        uint __arm64_flags_right_13313572 = default(uint);
        uint __arm64_flags_right_13313636 = default(uint);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
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
        x21 = 0x1BAB000UL;
        x22 = 0x1A8D000UL;
        x20 = 0x1A8E000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x4D4UL))))))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0xE28UL))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x620UL))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCB1F08;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xCD8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x628UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x168UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xAB0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x5A0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD10UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xFB0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xFB8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x158UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
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
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x620UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x630UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xE28UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x4D4UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCB1F08;
        label_0xCB1F08:
        ;
        x0 = RuntimeMemory.ReadU64(x22);
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x178FAB8UL /* metadata target: PlayerPrefs.GetInt */, x0, x1, x2, x3);
        RuntimeMemory.WriteU32(unchecked((ulong)((x19) + (0x50UL))), unchecked((uint)(x0)));
        x0 = RuntimeMemory.ReadU64(x20);
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x178FAB8UL /* metadata target: PlayerPrefs.GetInt */, x0, x1, x2, x3);
        RuntimeMemory.WriteU32(unchecked((ulong)((x19) + (0x54UL))), unchecked((uint)(x0)));
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792154UL /* metadata target: Component.get_transform */, x0, x1, x2, x3);
        x20 = unchecked((ulong)((x19) + (0x100UL)));
        x1 = x0;
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x100UL))), x0);
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x176F8DCUL /* metadata target: Camera.get_main */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCB227C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792154UL /* metadata target: Component.get_transform */, x0, x1, x2, x3);
        x1 = x0;
        x0 = unchecked((ulong)((x19) + (0x108UL)));
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x108UL))), x1);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x108UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCB227C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xCD8UL))));
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xE31BC8UL, x0, x1, x2, x3);
        x21 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x21) + (0xA8UL))), x0);
        x1 = x0;
        x0 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x21);
        if ((x8 == 0x0UL))
        {
            goto label_0xCB227C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x28UL))));
        x21 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x21) + (0x70UL))), x1);
        x0 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x38UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCB227C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792154UL /* metadata target: Component.get_transform */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCB227C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179D400UL /* metadata target: Transform.get_parent */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCB227C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792154UL /* metadata target: Component.get_transform */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCB227C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792190UL /* metadata target: Component.get_gameObject */, x0, x1, x2, x3);
        x21 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x21) + (0x78UL))), x0);
        x1 = x0;
        x0 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xFFFFFFFFFFFFFFF8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCB227C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xFB0UL))));
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xE49224UL, x0, x1, x2, x3);
        x21 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x21) + (0x80UL))), x0);
        x1 = x0;
        x0 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xFFFFFFFFFFFFFFF0UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCB227C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xD10UL))));
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xE49224UL, x0, x1, x2, x3);
        x21 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x21) + (0x88UL))), x0);
        x1 = x0;
        x0 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xFFFFFFFFFFFFFFE8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCB227C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x5A0UL))));
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xE49224UL, x0, x1, x2, x3);
        x21 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x21) + (0x90UL))), x0);
        x1 = x0;
        x0 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xFFFFFFFFFFFFFFE0UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCB227C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xFB8UL))));
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xE49224UL, x0, x1, x2, x3);
        x21 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x21) + (0xA0UL))), x0);
        x1 = x0;
        x0 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x48UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCB227C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(unchecked((long)(RuntimeMemory.ReadS32(unchecked((ulong)((x21) + (0x28UL))))))));
        x10 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_13312188 = unchecked((uint)(x9));
        __arm64_flags_right_13312188 = unchecked((uint)(x10));
        if ((__arm64_flags_left_13312188 >= __arm64_flags_right_13312188))
        {
            goto label_0xCB2690;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)((x9) << (int)(unchecked((int)(0x3UL))))))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCB227C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x22 = 0x1A8E000UL;
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x158UL))));
        x1 = RuntimeMemory.ReadU64(x22);
        x0 = RuntimeCalls.InvokeDirect(0xE49224UL, x0, x1, x2, x3);
        x21 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x21) + (0x98UL))), x0);
        x1 = x0;
        x0 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x50UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCB227C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(unchecked((long)(RuntimeMemory.ReadS32(unchecked((ulong)((x21) + (0x38UL))))))));
        x10 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_13312260 = unchecked((uint)(x9));
        __arm64_flags_right_13312260 = unchecked((uint)(x10));
        if ((__arm64_flags_left_13312260 >= __arm64_flags_right_13312260))
        {
            goto label_0xCB2690;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)((x9) << (int)(unchecked((int)(0x3UL))))))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCB227C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(x22);
        x0 = RuntimeCalls.InvokeDirect(0xE49224UL, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x20);
        if ((x8 == 0x0UL))
        {
            goto label_0xCB227C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = 0x1A8E000UL;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0x628UL))));
        x20 = x0;
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = x8;
        x2 = RuntimeMemory.ReadU64(x9);
        x0 = RuntimeCalls.InvokeDirect(0xE3247CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x1 = x0;
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0xF0UL))), x1);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792154UL /* metadata target: Component.get_transform */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCB227C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x168UL))));
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xE3226CUL, x0, x1, x2, x3);
        x1 = x0;
        x0 = unchecked((ulong)((x19) + (0x150UL)));
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x150UL))), x1);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x70UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCB227C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xAB0UL))));
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xE4913CUL, x0, x1, x2, x3);
        x21 = unchecked((ulong)((x19) + (0x158UL)));
        x1 = x0;
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x158UL))), x0);
        x0 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x158UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCB227C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCB21B8UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x176AAA8UL /* metadata target: AudioSource.set_spatialBlend */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x21);
        if ((x0 == 0x0UL))
        {
            goto label_0xCB227C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x21 = 0x1A8E000UL;
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x630UL))));
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x176AB7CUL /* metadata target: AudioSource.set_playOnAwake */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = RuntimeMemory.ReadU64(x21);
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x178FAB8UL /* metadata target: PlayerPrefs.GetInt */, x0, x1, x2, x3);
        if ((unchecked((uint)(x0)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCB2204;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x58UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCB227C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x60UL))));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177A970UL /* metadata target: Material.set_mainTexture */, x0, x1, x2, x3);
        goto label_0xCB2204;
        label_0xCB2204:
        ;
        x0 = RuntimeMemory.ReadU64(x21);
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x178FAB8UL /* metadata target: PlayerPrefs.GetInt */, x0, x1, x2, x3);
        __arm64_flags_left_13312528 = unchecked((uint)(x0));
        __arm64_flags_right_13312528 = unchecked((uint)0x1UL);
        if ((!((unchecked((uint)((__arm64_flags_left_13312528) - (__arm64_flags_right_13312528))) == unchecked((uint)0x0UL)))))
        {
            goto label_0xCB222C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x58UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCB227C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x68UL))));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177A970UL /* metadata target: Material.set_mainTexture */, x0, x1, x2, x3);
        goto label_0xCB222C;
        label_0xCB222C:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xE8UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCB227C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x21 = 0x1A8C000UL;
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xD8UL))));
        x23 = 0x0UL;
        goto label_0xCB2240;
        label_0xCB2240:
        ;
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_13312580 = unchecked((uint)(x23));
        __arm64_flags_right_13312580 = unchecked((uint)(x9));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13312580) - (__arm64_flags_right_13312580))))) < unchecked((int)0x0UL)) == (((unchecked((int)(__arm64_flags_left_13312580)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13312580)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13312580) - (__arm64_flags_right_13312580))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13312580)) < unchecked((int)0x0UL))))))
        {
            goto label_0xCB2280;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCB224CUL);
        }
        __arm64_flags_left_13312588 = unchecked((uint)(x23));
        __arm64_flags_right_13312588 = unchecked((uint)(x9));
        if ((__arm64_flags_left_13312588 >= __arm64_flags_right_13312588))
        {
            goto label_0xCB2690;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)((x23) << (int)(unchecked((int)(0x3UL))))))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCB227C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(x22);
        x0 = RuntimeCalls.InvokeDirect(0xE49224UL, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCB227C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCB226CUL);
        }
        RuntimeMemory.WriteU32(unchecked((ulong)((x0) + (0x124UL))), unchecked((uint)(x23)));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xE8UL))));
        x23 = unchecked((ulong)((x23) + (0x1UL)));
        if ((x8 != 0x0UL))
        {
            goto label_0xCB2240;
        }
        else
        {
            goto label_0xCB227C;
        }
        label_0xCB227C:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        goto label_0xCB2280;
        label_0xCB2280:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xF8UL))));
        RuntimeMemory.WritePtr(unchecked((ulong)((x19) + (0xE0UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCB227C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCB2690;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCB227C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(x22);
        x0 = RuntimeCalls.InvokeDirect(0xE49224UL, x0, x1, x2, x3);
        x1 = x0;
        x0 = unchecked((ulong)((x19) + (0x180UL)));
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x180UL))), x1);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x180UL))));
        if ((x9 == 0x0UL))
        {
            goto label_0xCB227C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x50UL))))));
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x9) + (0x124UL))))));
        __arm64_flags_left_13312708 = unchecked((uint)(x8));
        __arm64_flags_right_13312708 = unchecked((uint)0x20UL);
        RuntimeMemory.WriteU32(unchecked((ulong)((x19) + (0xD4UL))), unchecked((uint)(x9)));
        RuntimeCalls.Unsupported("b.hi", 0xCB22CCUL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xCB23D4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = 0x1124UL;
        x9 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x10 = unchecked((ulong)((unchecked((ulong)((x10) & ((~(0xFFFFUL)))))) | (unchecked((ulong)((unchecked((ulong)((0x11UL) << (int)(unchecked((int)(0x10UL)))))) << (int)(unchecked((int)(0x0UL))))))));
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) << (int)(unchecked((int)(unchecked((uint)(x8)))))))));
        x10 = unchecked((ulong)((unchecked((ulong)((x10) & ((~(0xFFFFUL)))))) | (unchecked((ulong)((unchecked((ulong)((0x1UL) << (int)(unchecked((int)(0x20UL)))))) << (int)(unchecked((int)(0x0UL))))))));
        __arm64_flags_left_13312740 = x9;
        __arm64_flags_right_13312740 = x10;
        __arm64_flags_result_13312740 = unchecked((ulong)((__arm64_flags_left_13312740) & (__arm64_flags_right_13312740)));
        if ((__arm64_flags_result_13312740 == 0x0UL))
        {
            goto label_0xCB2394;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xE8UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCB227C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_13312760 = unchecked((uint)(x9));
        __arm64_flags_right_13312760 = unchecked((uint)0xCUL);
        if (((!((__arm64_flags_left_13312760 >= __arm64_flags_right_13312760))) || (unchecked((uint)((__arm64_flags_left_13312760) - (__arm64_flags_right_13312760))) == unchecked((uint)0x0UL))))
        {
            goto label_0xCB2690;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x80UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCB227C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(x22);
        x0 = RuntimeCalls.InvokeDirect(0xE49224UL, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCB227C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x0) + (0x120UL))), unchecked((byte)(unchecked((uint)(x8)))));
        x1 = unchecked((ulong)(unchecked((uint)(0xCUL))));
        x0 = x19;
        x2 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x3 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x0 = RuntimeCalls.InvokeDirect(0xCB2694UL /* metadata target: PlayerWeapons.SelectWeapon */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x1 = x0;
        x0 = x19;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1795D40UL /* metadata target: MonoBehaviour.StartCoroutine */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x20UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCB227C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794CD0UL /* metadata target: GameObject.SetActive */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x38UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCB227C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794CD0UL /* metadata target: GameObject.SetActive */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x8 = unchecked((ulong)(unchecked((uint)(0x42B00000UL))));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(x8))), 0)), 0));
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1779D1CUL /* metadata target: RenderSettings.set_fogStartDistance */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x48UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCB227C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794CD0UL /* metadata target: GameObject.SetActive */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, unchecked((ulong)(unchecked((uint)(x3)))));
        if ((x20 != 0x0UL))
        {
            goto label_0xCB2500;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCB2390UL);
        }
        goto label_0xCB227C;
        label_0xCB2394:
        ;
        __arm64_flags_left_13312916 = x8;
        __arm64_flags_right_13312916 = 0x1FUL;
        if ((!((unchecked((ulong)((__arm64_flags_left_13312916) - (__arm64_flags_right_13312916))) == 0x0UL))))
        {
            goto label_0xCB23D4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xE8UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCB227C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_13312936 = unchecked((uint)(x9));
        __arm64_flags_right_13312936 = unchecked((uint)0xDUL);
        if (((!((__arm64_flags_left_13312936 >= __arm64_flags_right_13312936))) || (unchecked((uint)((__arm64_flags_left_13312936) - (__arm64_flags_right_13312936))) == unchecked((uint)0x0UL))))
        {
            goto label_0xCB2690;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x88UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCB227C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(x22);
        x0 = RuntimeCalls.InvokeDirect(0xE49224UL, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCB227C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x0) + (0x120UL))), unchecked((byte)(unchecked((uint)(x8)))));
        x1 = unchecked((ulong)(unchecked((uint)(0xDUL))));
        goto label_0xCB24DC;
        label_0xCB23D4:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x48UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCB227C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794CD0UL /* metadata target: GameObject.SetActive */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xE8UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCB227C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x54UL))))));
        x10 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) + (unchecked((uint)(0x1UL)))))));
        __arm64_flags_left_13313020 = unchecked((uint)(x9));
        __arm64_flags_right_13313020 = unchecked((uint)(x10));
        if ((__arm64_flags_left_13313020 >= __arm64_flags_right_13313020))
        {
            goto label_0xCB2690;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) << (int)(unchecked((int)(unchecked((uint)(0x3UL))))))))))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCB227C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(x22);
        x0 = RuntimeCalls.InvokeDirect(0xE49224UL, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCB227C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x120UL))))))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xE8UL))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCB2460;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCB2428UL);
        }
        if ((x8 == 0x0UL))
        {
            goto label_0xCB227C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(unchecked((long)(RuntimeMemory.ReadS32(unchecked((ulong)((x19) + (0xC8UL))))))));
        x10 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_13313076 = unchecked((uint)(x9));
        __arm64_flags_right_13313076 = unchecked((uint)(x10));
        if ((__arm64_flags_left_13313076 >= __arm64_flags_right_13313076))
        {
            goto label_0xCB2690;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)((x9) << (int)(unchecked((int)(0x3UL))))))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCB227C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(x22);
        x0 = RuntimeCalls.InvokeDirect(0xE49224UL, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCB227C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x0) + (0x120UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCB24D4;
        label_0xCB2460:
        ;
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCB227C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x54UL))))));
        x10 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((unchecked((ulong)(unchecked((uint)(x8))))) + (0x18UL))))));
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) + (unchecked((uint)(0x1UL)))))));
        __arm64_flags_left_13313136 = unchecked((uint)(x9));
        __arm64_flags_right_13313136 = unchecked((uint)(x10));
        if ((__arm64_flags_left_13313136 >= __arm64_flags_right_13313136))
        {
            goto label_0xCB2690;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) + (unchecked((uint)((unchecked((uint)(x9))) << (int)(unchecked((int)(unchecked((uint)(0x3UL))))))))))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCB227C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(x22);
        x0 = RuntimeCalls.InvokeDirect(0xE49224UL, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCB227C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x0) + (0x120UL))), unchecked((byte)(unchecked((uint)(x8)))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xE8UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCB227C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x54UL))))));
        x10 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) + (unchecked((uint)(0x1UL)))))));
        __arm64_flags_left_13313196 = unchecked((uint)(x9));
        __arm64_flags_right_13313196 = unchecked((uint)(x10));
        if ((__arm64_flags_left_13313196 >= __arm64_flags_right_13313196))
        {
            goto label_0xCB2690;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) << (int)(unchecked((int)(unchecked((uint)(0x3UL))))))))))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCB227C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(x22);
        x0 = RuntimeCalls.InvokeDirect(0xE49224UL, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCB227C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x120UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCB2658;
        }
        else
        {
            goto label_0xCB24D4;
        }
        label_0xCB24D4:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x54UL))))));
        x1 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) + (unchecked((uint)(0x1UL)))))));
        goto label_0xCB24DC;
        label_0xCB24DC:
        ;
        x0 = x19;
        x2 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x3 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x0 = RuntimeCalls.InvokeDirect(0xCB2694UL /* metadata target: PlayerWeapons.SelectWeapon */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x1 = x0;
        x0 = x19;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1795D40UL /* metadata target: MonoBehaviour.StartCoroutine */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        if ((x20 == 0x0UL))
        {
            goto label_0xCB227C;
        }
        else
        {
            goto label_0xCB2500;
        }
        label_0xCB2500:
        ;
        x0 = x19;
        RuntimeMemory.WriteU16(unchecked((ulong)((x20) + (0x122UL))), unchecked((ushort)(unchecked((uint)0x0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xCB2730UL /* metadata target: PlayerWeapons.UpdateTotalWeapons */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x0 = RuntimeMemory.ReadU64(x21);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x160UL))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCB2520;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCB251CUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        goto label_0xCB2520;
        label_0xCB2520:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1798274UL /* metadata target: Object.op_Implicit */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCB2610;
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
            goto label_0xCB2554;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCB2550UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        goto label_0xCB2554;
        label_0xCB2554:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1556240UL /* metadata target: Type.GetTypeFromHandle */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x8 = RuntimeMemory.ReadU64(x21);
        x20 = x0;
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCB2578;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        goto label_0xCB2578;
        label_0xCB2578:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1798B54UL /* metadata target: Object.FindObjectsOfType */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x278UL))));
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xB7DA60UL, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCB227C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x18UL))))));
        x20 = x0;
        __arm64_flags_left_13313440 = unchecked((uint)(x8));
        __arm64_flags_right_13313440 = unchecked((uint)0x1UL);
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13313440) - (__arm64_flags_right_13313440))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_13313440)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13313440)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13313440) - (__arm64_flags_right_13313440))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13313440)) < unchecked((int)0x0UL))))))
        {
            goto label_0xCB2610;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x21 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x19 = unchecked((ulong)((x19) + (0x160UL)));
        goto label_0xCB25B0;
        label_0xCB25B0:
        ;
        __arm64_flags_left_13313456 = unchecked((uint)(x21));
        __arm64_flags_right_13313456 = unchecked((uint)(x8));
        if ((__arm64_flags_left_13313456 >= __arm64_flags_right_13313456))
        {
            goto label_0xCB2690;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x22 = unchecked((ulong)((x20) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x21))) << (int)(unchecked((int)(unchecked((uint)(0x3UL))))))))))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x20UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCB227C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177BA6CUL /* metadata target: Light.get_type */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        __arm64_flags_left_13313484 = unchecked((uint)(x0));
        __arm64_flags_right_13313484 = unchecked((uint)0x1UL);
        if ((!((unchecked((uint)((__arm64_flags_left_13313484) - (__arm64_flags_right_13313484))) == unchecked((uint)0x0UL)))))
        {
            goto label_0xCB2600;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x20) + (0x18UL))))));
        __arm64_flags_left_13313496 = unchecked((uint)(x21));
        __arm64_flags_right_13313496 = unchecked((uint)(x8));
        if ((__arm64_flags_left_13313496 >= __arm64_flags_right_13313496))
        {
            goto label_0xCB2690;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(x22);
        if ((x0 == 0x0UL))
        {
            goto label_0xCB227C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792190UL /* metadata target: Component.get_gameObject */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCB227C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794D50UL /* metadata target: GameObject.get_activeInHierarchy */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCB2620;
        }
        else
        {
            goto label_0xCB2600;
        }
        label_0xCB2600:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x20) + (0x18UL))))));
        x21 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x21))) + (unchecked((uint)(0x1UL)))))));
        __arm64_flags_left_13313544 = unchecked((uint)(x21));
        __arm64_flags_right_13313544 = unchecked((uint)(x8));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13313544) - (__arm64_flags_right_13313544))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_13313544)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13313544)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13313544) - (__arm64_flags_right_13313544))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13313544)) < unchecked((int)0x0UL))))))
        {
            goto label_0xCB25B0;
        }
        else
        {
            goto label_0xCB2610;
        }
        label_0xCB2610:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return x0;
        label_0xCB2620:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x20) + (0x18UL))))));
        __arm64_flags_left_13313572 = unchecked((uint)(x21));
        __arm64_flags_right_13313572 = unchecked((uint)(x8));
        if ((__arm64_flags_left_13313572 >= __arm64_flags_right_13313572))
        {
            goto label_0xCB2690;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(x22);
        if ((x0 == 0x0UL))
        {
            goto label_0xCB227C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792154UL /* metadata target: Component.get_transform */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x1 = x0;
        RuntimeMemory.WriteU64(x19, x0);
        x0 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeDirect(0xB7D8D0UL);
        label_0xCB2658:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xE8UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCB227C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_13313636 = unchecked((uint)(x9));
        __arm64_flags_right_13313636 = unchecked((uint)0x1UL);
        if (((!((__arm64_flags_left_13313636 >= __arm64_flags_right_13313636))) || (unchecked((uint)((__arm64_flags_left_13313636) - (__arm64_flags_right_13313636))) == unchecked((uint)0x0UL))))
        {
            goto label_0xCB2690;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x28UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCB227C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(x22);
        x0 = RuntimeCalls.InvokeDirect(0xE49224UL, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCB227C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x0) + (0x120UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCB24DC;
        label_0xCB2690:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB7CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, unchecked((ulong)(unchecked((uint)(x3)))));
        return default(ulong);
    }
```

## `PlayerWeapons.SelectWeapon` — RVA `0xcb2694`

- Lift status: **exact**; input span: 156 bytes; span to next metadata RVA: 156 bytes.
- Metadata signature: `public IEnumerator SelectWeapon(int index, bool isOffhandThrow = false, bool endOffhandThrow = false) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=23 (informational only).

```csharp
public static ulong PlayerWeapons_SelectWeapon_RVAcb2694(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
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
        x24 = 0x1BAB000UL;
        x23 = 0x1A8E000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x24) + (0x4D9UL))))))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0x638UL))));
        x21 = unchecked((ulong)(unchecked((uint)(x3))));
        x22 = unchecked((ulong)(unchecked((uint)(x2))));
        x19 = unchecked((ulong)(unchecked((uint)(x1))));
        x20 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
        }
        else
        {
            x0 = 0x1A8E000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x638UL))));
            // Likely IL2CPP class initialization helper (guarded call).
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
            RuntimeMemory.WriteU8(unchecked((ulong)((x24) + (0x4D9UL))), unchecked((byte)(unchecked((uint)(x8)))));
        }
        label_0xCB26DC:
        ;
        x0 = RuntimeMemory.ReadU64(x23);
        x23 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x21))) & (unchecked((uint)(0x1UL)))))));
        x22 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x22))) & (unchecked((uint)(0x1UL)))))));
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = 0x0UL;
        x21 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x1589338UL /* metadata target: Object.ctor */, x0, x1, x2, x3);
        x0 = x21;
        RuntimeMemory.WritePtr(unchecked((ulong)((x21) + (0x10UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x20UL))), x20);
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        RuntimeMemory.WriteU32(unchecked((ulong)((x21) + (0x28UL))), unchecked((uint)(x19)));
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x2CUL))), unchecked((byte)(unchecked((uint)(x22)))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x2DUL))), unchecked((byte)(unchecked((uint)(x23)))));
        x0 = x21;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        return default(ulong);
    }
```

## `PlayerWeapons.UpdateTotalWeapons` — RVA `0xcb2730`

- Lift status: **exact**; input span: 220 bytes; span to next metadata RVA: 220 bytes.
- Metadata signature: `public void UpdateTotalWeapons() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=27 (informational only).

```csharp
public static ulong PlayerWeapons_UpdateTotalWeapons_RVAcb2730(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13313920 = default(uint);
        uint __arm64_flags_left_13313928 = default(uint);
        uint __arm64_flags_left_13313976 = default(uint);
        uint __arm64_flags_right_13313920 = default(uint);
        uint __arm64_flags_right_13313928 = default(uint);
        uint __arm64_flags_right_13313976 = default(uint);
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
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x4D8UL))))))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCB2760;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x158UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x4D8UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCB2760;
        label_0xCB2760:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xE8UL))));
        RuntimeMemory.WritePtr(unchecked((ulong)((x19) + (0xD8UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCB27F4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = 0x1A8E000UL;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x158UL))));
        x21 = unchecked((ulong)(unchecked((uint)(0x5UL))));
        goto label_0xCB2778;
        label_0xCB2778:
        ;
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        x22 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x21))) - (unchecked((uint)(0x4UL)))))));
        __arm64_flags_left_13313920 = unchecked((uint)(x22));
        __arm64_flags_right_13313920 = unchecked((uint)(x9));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13313920) - (__arm64_flags_right_13313920))))) < unchecked((int)0x0UL)) == (((unchecked((int)(__arm64_flags_left_13313920)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13313920)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13313920) - (__arm64_flags_right_13313920))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13313920)) < unchecked((int)0x0UL))))))
        {
            goto label_0xCB27F8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCB2788UL);
        }
        __arm64_flags_left_13313928 = unchecked((uint)(x22));
        __arm64_flags_right_13313928 = unchecked((uint)(x9));
        if ((__arm64_flags_left_13313928 >= __arm64_flags_right_13313928))
        {
            goto label_0xCB2808;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (unchecked((ulong)(unchecked((uint)(x21))))))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCB27F4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(x20);
        x0 = RuntimeCalls.InvokeDirect(0xE49224UL, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCB27F4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x120UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCB27E8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xE8UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCB27F4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_13313976 = unchecked((uint)(x22));
        __arm64_flags_right_13313976 = unchecked((uint)(x9));
        if ((__arm64_flags_left_13313976 >= __arm64_flags_right_13313976))
        {
            goto label_0xCB2808;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (unchecked((ulong)(unchecked((uint)(x21))))))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCB27F4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(x20);
        x0 = RuntimeCalls.InvokeDirect(0xE49224UL, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCB27F4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x123UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCB27E8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0xD8UL))))));
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) + (unchecked((uint)(0x1UL)))))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x19) + (0xD8UL))), unchecked((uint)(x8)));
        goto label_0xCB27E8;
        label_0xCB27E8:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xE8UL))));
        x21 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x21))) + (unchecked((uint)(0x1UL)))))));
        if ((x8 != 0x0UL))
        {
            goto label_0xCB2778;
        }
        else
        {
            goto label_0xCB27F4;
        }
        label_0xCB27F4:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        goto label_0xCB27F8;
        label_0xCB27F8:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        label_0xCB2808:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB7CUL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `PlayerWeapons.Update` — RVA `0xcb280c`

- Lift status: **partial**; input span: 3456 bytes; span to next metadata RVA: 3456 bytes.
- Metadata signature: `private void Update() { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=418 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'b.gt' at 0xcb2c78; reason: Unknown IR expression at 0xcb2c78

```csharp
public static ulong PlayerWeapons_Update_RVAcb280c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13314244 = default(uint);
        uint __arm64_flags_left_13314444 = default(uint);
        uint __arm64_flags_left_13314760 = default(uint);
        uint __arm64_flags_left_13314780 = default(uint);
        uint __arm64_flags_left_13315120 = default(uint);
        uint __arm64_flags_left_13315172 = default(uint);
        uint __arm64_flags_left_13315184 = default(uint);
        uint __arm64_flags_left_13315212 = default(uint);
        uint __arm64_flags_left_13315224 = default(uint);
        uint __arm64_flags_left_13315276 = default(uint);
        uint __arm64_flags_left_13315284 = default(uint);
        uint __arm64_flags_left_13315488 = default(uint);
        uint __arm64_flags_left_13315536 = default(uint);
        uint __arm64_flags_left_13315576 = default(uint);
        uint __arm64_flags_left_13315652 = default(uint);
        uint __arm64_flags_left_13315740 = default(uint);
        uint __arm64_flags_left_13315872 = default(uint);
        uint __arm64_flags_left_13315940 = default(uint);
        uint __arm64_flags_left_13315976 = default(uint);
        uint __arm64_flags_left_13316012 = default(uint);
        uint __arm64_flags_left_13316084 = default(uint);
        uint __arm64_flags_left_13316204 = default(uint);
        uint __arm64_flags_left_13316224 = default(uint);
        uint __arm64_flags_left_13316276 = default(uint);
        uint __arm64_flags_left_13316284 = default(uint);
        uint __arm64_flags_left_13316400 = default(uint);
        uint __arm64_flags_left_13316408 = default(uint);
        uint __arm64_flags_left_13316424 = default(uint);
        uint __arm64_flags_left_13316476 = default(uint);
        uint __arm64_flags_left_13316496 = default(uint);
        uint __arm64_flags_left_13316508 = default(uint);
        uint __arm64_flags_left_13316540 = default(uint);
        uint __arm64_flags_left_13316552 = default(uint);
        uint __arm64_flags_left_13316564 = default(uint);
        uint __arm64_flags_left_13316616 = default(uint);
        uint __arm64_flags_left_13316636 = default(uint);
        uint __arm64_flags_left_13316648 = default(uint);
        uint __arm64_flags_left_13316684 = default(uint);
        uint __arm64_flags_left_13316748 = default(uint);
        uint __arm64_flags_left_13316764 = default(uint);
        uint __arm64_flags_left_13316784 = default(uint);
        uint __arm64_flags_left_13316836 = default(uint);
        uint __arm64_flags_left_13316856 = default(uint);
        uint __arm64_flags_left_13316868 = default(uint);
        uint __arm64_flags_left_13316904 = default(uint);
        uint __arm64_flags_left_13317012 = default(uint);
        uint __arm64_flags_left_13317024 = default(uint);
        uint __arm64_flags_left_13317064 = default(uint);
        uint __arm64_flags_left_13317096 = default(uint);
        uint __arm64_flags_left_13317128 = default(uint);
        uint __arm64_flags_left_13317160 = default(uint);
        uint __arm64_flags_left_13317192 = default(uint);
        uint __arm64_flags_left_13317224 = default(uint);
        uint __arm64_flags_left_13317256 = default(uint);
        uint __arm64_flags_left_13317288 = default(uint);
        uint __arm64_flags_left_13317300 = default(uint);
        uint __arm64_flags_left_13317320 = default(uint);
        uint __arm64_flags_left_13317340 = default(uint);
        uint __arm64_flags_left_13317360 = default(uint);
        uint __arm64_flags_left_13317380 = default(uint);
        uint __arm64_flags_left_13317400 = default(uint);
        uint __arm64_flags_left_13317420 = default(uint);
        uint __arm64_flags_left_13317440 = default(uint);
        uint __arm64_flags_result_13315212 = default(uint);
        uint __arm64_flags_result_13315284 = default(uint);
        uint __arm64_flags_result_13316204 = default(uint);
        uint __arm64_flags_result_13316284 = default(uint);
        uint __arm64_flags_right_13314244 = default(uint);
        uint __arm64_flags_right_13314444 = default(uint);
        uint __arm64_flags_right_13314760 = default(uint);
        uint __arm64_flags_right_13314780 = default(uint);
        uint __arm64_flags_right_13315120 = default(uint);
        uint __arm64_flags_right_13315172 = default(uint);
        uint __arm64_flags_right_13315184 = default(uint);
        uint __arm64_flags_right_13315212 = default(uint);
        uint __arm64_flags_right_13315224 = default(uint);
        uint __arm64_flags_right_13315276 = default(uint);
        uint __arm64_flags_right_13315284 = default(uint);
        uint __arm64_flags_right_13315488 = default(uint);
        uint __arm64_flags_right_13315536 = default(uint);
        uint __arm64_flags_right_13315576 = default(uint);
        uint __arm64_flags_right_13315652 = default(uint);
        uint __arm64_flags_right_13315740 = default(uint);
        uint __arm64_flags_right_13315872 = default(uint);
        uint __arm64_flags_right_13315940 = default(uint);
        uint __arm64_flags_right_13315976 = default(uint);
        uint __arm64_flags_right_13316012 = default(uint);
        uint __arm64_flags_right_13316084 = default(uint);
        uint __arm64_flags_right_13316204 = default(uint);
        uint __arm64_flags_right_13316224 = default(uint);
        uint __arm64_flags_right_13316276 = default(uint);
        uint __arm64_flags_right_13316284 = default(uint);
        uint __arm64_flags_right_13316400 = default(uint);
        uint __arm64_flags_right_13316408 = default(uint);
        uint __arm64_flags_right_13316424 = default(uint);
        uint __arm64_flags_right_13316476 = default(uint);
        uint __arm64_flags_right_13316496 = default(uint);
        uint __arm64_flags_right_13316508 = default(uint);
        uint __arm64_flags_right_13316540 = default(uint);
        uint __arm64_flags_right_13316552 = default(uint);
        uint __arm64_flags_right_13316564 = default(uint);
        uint __arm64_flags_right_13316616 = default(uint);
        uint __arm64_flags_right_13316636 = default(uint);
        uint __arm64_flags_right_13316648 = default(uint);
        uint __arm64_flags_right_13316684 = default(uint);
        uint __arm64_flags_right_13316748 = default(uint);
        uint __arm64_flags_right_13316764 = default(uint);
        uint __arm64_flags_right_13316784 = default(uint);
        uint __arm64_flags_right_13316836 = default(uint);
        uint __arm64_flags_right_13316856 = default(uint);
        uint __arm64_flags_right_13316868 = default(uint);
        uint __arm64_flags_right_13316904 = default(uint);
        uint __arm64_flags_right_13317012 = default(uint);
        uint __arm64_flags_right_13317024 = default(uint);
        uint __arm64_flags_right_13317064 = default(uint);
        uint __arm64_flags_right_13317096 = default(uint);
        uint __arm64_flags_right_13317128 = default(uint);
        uint __arm64_flags_right_13317160 = default(uint);
        uint __arm64_flags_right_13317192 = default(uint);
        uint __arm64_flags_right_13317224 = default(uint);
        uint __arm64_flags_right_13317256 = default(uint);
        uint __arm64_flags_right_13317288 = default(uint);
        uint __arm64_flags_right_13317300 = default(uint);
        uint __arm64_flags_right_13317320 = default(uint);
        uint __arm64_flags_right_13317340 = default(uint);
        uint __arm64_flags_right_13317360 = default(uint);
        uint __arm64_flags_right_13317380 = default(uint);
        uint __arm64_flags_right_13317400 = default(uint);
        uint __arm64_flags_right_13317420 = default(uint);
        uint __arm64_flags_right_13317440 = default(uint);
        float __arm64_float_flags_left_13314620 = default(float);
        float __arm64_float_flags_left_13314636 = default(float);
        float __arm64_float_flags_left_13314716 = default(float);
        float __arm64_float_flags_left_13314876 = default(float);
        float __arm64_float_flags_left_13315028 = default(float);
        float __arm64_float_flags_left_13315048 = default(float);
        float __arm64_float_flags_left_13315384 = default(float);
        float __arm64_float_flags_left_13315404 = default(float);
        float __arm64_float_flags_left_13315444 = default(float);
        float __arm64_float_flags_left_13315464 = default(float);
        float __arm64_float_flags_left_13316340 = default(float);
        float __arm64_float_flags_right_13314620 = default(float);
        float __arm64_float_flags_right_13314636 = default(float);
        float __arm64_float_flags_right_13314716 = default(float);
        float __arm64_float_flags_right_13314876 = default(float);
        float __arm64_float_flags_right_13315028 = default(float);
        float __arm64_float_flags_right_13315048 = default(float);
        float __arm64_float_flags_right_13315384 = default(float);
        float __arm64_float_flags_right_13315404 = default(float);
        float __arm64_float_flags_right_13315444 = default(float);
        float __arm64_float_flags_right_13315464 = default(float);
        float __arm64_float_flags_right_13316340 = default(float);
        ulong __arm64_pair_address_13314060 = default(ulong);
        ulong __arm64_pair_address_13315620 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        RuntimeVector128 v9 = default(RuntimeVector128);
        ulong x10 = default(ulong);
        ulong x11 = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x22 = default(ulong);
        ulong x23 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        __arm64_pair_address_13314060 = unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFC0UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13314060, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13314060) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        sp = __arm64_pair_address_13314060;
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))), x19);
        x20 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x4D5UL))))))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCB2888;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x68UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x538UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x158UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x640UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x648UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(x0);
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x4D5UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCB2888;
        label_0xCB2888:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x132UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCB29FC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x98UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCB3584;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x124UL))))));
        x0 = x19;
        x2 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x3 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x0 = RuntimeCalls.InvokeDirect(0xCB2694UL /* metadata target: PlayerWeapons.SelectWeapon */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x98UL))));
        if ((x9 == 0x0UL))
        {
            goto label_0xCB3584;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xE8UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCB3584;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(unchecked((long)(RuntimeMemory.ReadS32(unchecked((ulong)((x9) + (0x124UL))))))));
        x10 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_13314244 = unchecked((uint)(x9));
        __arm64_flags_right_13314244 = unchecked((uint)(x10));
        if ((__arm64_flags_left_13314244 >= __arm64_flags_right_13314244))
        {
            goto label_0xCB3588;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)((x9) << (int)(unchecked((int)(0x3UL))))))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCB3584;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x538UL))));
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xE49224UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x20 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x20) + (0xB8UL))), x0);
        x1 = x0;
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x0 = RuntimeMemory.ReadU64(x20);
        if ((x0 == 0x0UL))
        {
            goto label_0xCB3584;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x648UL))));
        x2 = 0x0UL;
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x1767884UL /* metadata target: Animator.SetTrigger */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x21 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x2C9UL))))))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x98UL))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCB293C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x1E8UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x2C9UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCB293C;
        label_0xCB293C:
        ;
        if ((x20 == 0x0UL))
        {
            goto label_0xCB3584;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x1E8UL))));
        x8 = RuntimeMemory.ReadU64(x8);
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(x9)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x9) + (0x8UL))))), 0));
        x9 = unchecked((ulong)((x20) + (0x38CUL)));
        RuntimeMemory.WriteF64(x9, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))));
        RuntimeMemory.WriteF32(unchecked((ulong)((x9) + (0x8UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0));
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xA8UL))));
        if ((x9 == 0x0UL))
        {
            goto label_0xCB3584;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(x8)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x8UL))))), 0));
        RuntimeMemory.WriteF64(unchecked((ulong)((x9) + (0xB4UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))));
        RuntimeMemory.WriteF32(unchecked((ulong)((x9) + (0xBCUL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x98UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCB3584;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x134UL))))));
        __arm64_flags_left_13314444 = unchecked((uint)(x9));
        __arm64_flags_right_13314444 = unchecked((uint)0x1UL);
        if (((!((unchecked((uint)((__arm64_flags_left_13314444) - (__arm64_flags_right_13314444))) == unchecked((uint)0x0UL)))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13314444) - (__arm64_flags_right_13314444))))) < unchecked((int)0x0UL)) == (((unchecked((int)(__arm64_flags_left_13314444)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13314444)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13314444) - (__arm64_flags_right_13314444))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13314444)) < unchecked((int)0x0UL)))))))
        {
            goto label_0xCB29C0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x124UL))))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCB29C0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x110UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCB3584;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(x8);
        x2 = 0x0UL;
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x1767884UL /* metadata target: Animator.SetTrigger */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x98UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCB3584;
        }
        else
        {
            goto label_0xCB29C0;
        }
        label_0xCB29C0:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x118UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCB3584;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCB29C8UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1767EB4UL /* metadata target: Animator.set_speed */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x98UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCB3584;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x118UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCB3584;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x640UL))));
        x2 = 0x0UL;
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x1767884UL /* metadata target: Animator.SetTrigger */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x132UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        goto label_0xCB29FC;
        label_0xCB29FC:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x17DUL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCB2A30;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x178UL))))));
        x3 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = x19;
        x2 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x0 = RuntimeCalls.InvokeDirect(0xCB2694UL /* metadata target: PlayerWeapons.SelectWeapon */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x1 = x0;
        x0 = x19;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1795D40UL /* metadata target: MonoBehaviour.StartCoroutine */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        RuntimeMemory.WriteU16(unchecked((ulong)((x19) + (0x17CUL))), unchecked((ushort)(unchecked((uint)0x0UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x17EUL))), unchecked((byte)(unchecked((uint)0x0UL))));
        goto label_0xCB2A30;
        label_0xCB2A30:
        ;
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179AD58UL /* metadata target: Time.get_timeSinceLevelLoad */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x40000000UL)), 0)), 0));
        __arm64_float_flags_left_13314620 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13314620 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_13314620 <= __arm64_float_flags_right_13314620) || ((__arm64_float_flags_left_13314620 != __arm64_float_flags_left_13314620) || (__arm64_float_flags_right_13314620 != __arm64_float_flags_right_13314620))))
        {
            goto label_0xCB2D18;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179AE58UL /* metadata target: Time.get_timeScale */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        __arm64_float_flags_left_13314636 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13314636 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        if (((__arm64_float_flags_left_13314636 <= __arm64_float_flags_right_13314636) || ((__arm64_float_flags_left_13314636 != __arm64_float_flags_left_13314636) || (__arm64_float_flags_right_13314636 != __arm64_float_flags_right_13314636))))
        {
            goto label_0xCB2D18;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x88UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCB3584;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x228UL))))))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCB2D10;
        }
        else
        {
            goto label_0xCB2A64;
        }
        label_0xCB2A64:
        ;
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x128UL))))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCB2D18;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x80UL))));
        if ((x9 == 0x0UL))
        {
            goto label_0xCB3584;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x9) + (0x99UL))))))));
        if ((unchecked((uint)(x10)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCB2D18;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x98UL))));
        if ((x10 == 0x0UL))
        {
            goto label_0xCB3584;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x10) + (0x3A5UL))))))));
        if ((unchecked((uint)(x10)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCB2AA4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x90UL))));
        if ((x10 == 0x0UL))
        {
            goto label_0xCB3584;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCB2A94UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x10) + (0x20CUL))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        __arm64_float_flags_left_13314716 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13314716 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_13314716 >= __arm64_float_flags_right_13314716) || ((__arm64_float_flags_left_13314716 != __arm64_float_flags_left_13314716) || (__arm64_float_flags_right_13314716 != __arm64_float_flags_right_13314716))))
        {
            goto label_0xCB2D18;
        }
        else
        {
            goto label_0xCB2AA4;
        }
        label_0xCB2AA4:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x198UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCB2D18;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x9) + (0xAAUL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCB2ABC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x129UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCB2E2C;
        }
        else
        {
            goto label_0xCB2ABC;
        }
        label_0xCB2ABC:
        ;
        x22 = x19;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x22) + (0xDCUL))))));
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x22) + (0xFFFFFFFFFFFFFFF8UL))))));
        __arm64_flags_left_13314760 = unchecked((uint)(x8));
        __arm64_flags_right_13314760 = unchecked((uint)(x9));
        if ((unchecked((uint)((__arm64_flags_left_13314760) - (__arm64_flags_right_13314760))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCB2AEC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x180UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCB3584;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x128UL))))));
        __arm64_flags_left_13314780 = unchecked((uint)(x8));
        __arm64_flags_right_13314780 = unchecked((uint)0x1UL);
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13314780) - (__arm64_flags_right_13314780))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_13314780)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13314780)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13314780) - (__arm64_flags_right_13314780))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13314780)) < unchecked((int)0x0UL))))))
        {
            goto label_0xCB2AEC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x129UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCB2EAC;
        }
        else
        {
            goto label_0xCB2AEC;
        }
        label_0xCB2AEC:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x130UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCB2D18;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x80UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCB3584;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0xA0UL))))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCB2B0C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0xF3UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCB2B2C;
        }
        else
        {
            goto label_0xCB2B0C;
        }
        label_0xCB2B0C:
        ;
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(x22)));
        if ((unchecked((uint)(x1)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCB2B2C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x17CUL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCB2B2C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x88UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCB3584;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x2B1UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCB30D0;
        }
        else
        {
            goto label_0xCB2B2C;
        }
        label_0xCB2B2C:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x90UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCB3584;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCB2B34UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x20CUL))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        __arm64_float_flags_left_13314876 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13314876 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_13314876 >= __arm64_float_flags_right_13314876) || ((__arm64_float_flags_left_13314876 != __arm64_float_flags_left_13314876) || (__arm64_float_flags_right_13314876 != __arm64_float_flags_right_13314876))))
        {
            goto label_0xCB2BCC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x139UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCB2BCC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x98UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCB3584;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x8) + (0x122UL))), unchecked((byte)(unchecked((uint)(x9)))));
        x9 = 0x1A8C000UL;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0xD8UL))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x448UL))));
        x0 = RuntimeMemory.ReadU64(x9);
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCB2B78;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCB2B74UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, unchecked((ulong)(unchecked((uint)(x3)))));
        goto label_0xCB2B78;
        label_0xCB2B78:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1798274UL /* metadata target: Object.op_Implicit */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCB2BB8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x98UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCB3584;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x448UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCB3584;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x68UL))));
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xE31BC8UL, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCB3584;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17799D0UL /* metadata target: Renderer.set_enabled */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, unchecked((ulong)(unchecked((uint)(x3)))));
        goto label_0xCB2BB8;
        label_0xCB2BB8:
        ;
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0xDCUL))))));
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = x19;
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x139UL))), unchecked((byte)(unchecked((uint)(x8)))));
        x0 = RuntimeCalls.InvokeDirect(0xCB3684UL /* metadata target: PlayerWeapons.DropWeapon */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, unchecked((ulong)(unchecked((uint)(x3)))));
        goto label_0xCB2BCC;
        label_0xCB2BCC:
        ;
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179AE58UL /* metadata target: Time.get_timeScale */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, unchecked((ulong)(unchecked((uint)(x3)))));
        __arm64_float_flags_left_13315028 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13315028 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        if (((__arm64_float_flags_left_13315028 <= __arm64_float_flags_right_13315028) || ((__arm64_float_flags_left_13315028 != __arm64_float_flags_left_13315028) || (__arm64_float_flags_right_13315028 != __arm64_float_flags_right_13315028))))
        {
            goto label_0xCB3358;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x80UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCB3584;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCB2BE4UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0xB8UL))))), 0));
        __arm64_float_flags_left_13315048 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13315048 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        if (((__arm64_float_flags_left_13315048 >= __arm64_float_flags_right_13315048) || ((__arm64_float_flags_left_13315048 != __arm64_float_flags_left_13315048) || (__arm64_float_flags_right_13315048 != __arm64_float_flags_right_13315048))))
        {
            goto label_0xCB2C00;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xA8UL))));
        if ((x9 == 0x0UL))
        {
            goto label_0xCB3584;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x9) + (0x1A5UL))))))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCB2C10;
        }
        else
        {
            goto label_0xCB2C00;
        }
        label_0xCB2C00:
        ;
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0xA9UL))))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCB2C10;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0xF0UL))))))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCB30F4;
        }
        else
        {
            goto label_0xCB2C10;
        }
        label_0xCB2C10:
        ;
        x20 = unchecked((ulong)(RuntimeMemory.ReadU32(x22)));
        if ((unchecked((uint)(x20)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCB3060;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCB2C18UL);
        }
        if ((unchecked((uint)((unchecked((uint)(x20))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x1FUL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCB3358;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x23 = 0x1A8E000UL;
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0x158UL))));
        goto label_0xCB2C24;
        label_0xCB2C24:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xE8UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCB3584;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_13315120 = unchecked((uint)(x20));
        __arm64_flags_right_13315120 = unchecked((uint)(x9));
        if ((__arm64_flags_left_13315120 >= __arm64_flags_right_13315120))
        {
            goto label_0xCB3588;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x20))) << (int)(unchecked((int)(unchecked((uint)(0x3UL))))))))))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCB3584;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(x23);
        x0 = RuntimeCalls.InvokeDirect(0xE49224UL, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCB3584;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x120UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCB2C6C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x121UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCB2C6C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(x22)));
        __arm64_flags_left_13315172 = unchecked((uint)(x20));
        __arm64_flags_right_13315172 = unchecked((uint)(x8));
        if ((!((unchecked((uint)((__arm64_flags_left_13315172) - (__arm64_flags_right_13315172))) == unchecked((uint)0x0UL)))))
        {
            goto label_0xCB3334;
        }
        else
        {
            goto label_0xCB2C6C;
        }
        label_0xCB2C6C:
        ;
        if ((unchecked((uint)(x20)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCB2C80;
        }
        else
        {
            goto label_0xCB2C70;
        }
        label_0xCB2C70:
        ;
        __arm64_flags_left_13315184 = unchecked((uint)(x20));
        __arm64_flags_right_13315184 = unchecked((uint)0x0UL);
        x20 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x20))) - (unchecked((uint)(0x1UL)))))));
        RuntimeCalls.Unsupported("b.gt", 0xCB2C78UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xCB2C24;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCB2C7CUL);
        }
        goto label_0xCB3358;
        label_0xCB2C80:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xE8UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCB3584;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_13315212 = unchecked((uint)(x9));
        __arm64_flags_right_13315212 = unchecked((uint)0x1UL);
        __arm64_flags_result_13315212 = unchecked((uint)((__arm64_flags_left_13315212) - (__arm64_flags_right_13315212)));
        x21 = unchecked((ulong)(__arm64_flags_result_13315212));
        if ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13315212) - (__arm64_flags_right_13315212))))) < unchecked((int)0x0UL)))
        {
            goto label_0xCB3358;
        }
        else
        {
            goto label_0xCB2C94;
        }
        label_0xCB2C94:
        ;
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_13315224 = unchecked((uint)(x21));
        __arm64_flags_right_13315224 = unchecked((uint)(x9));
        if ((__arm64_flags_left_13315224 >= __arm64_flags_right_13315224))
        {
            goto label_0xCB3588;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x21))) << (int)(unchecked((int)(unchecked((uint)(0x3UL))))))))))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCB3584;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(x23);
        x0 = RuntimeCalls.InvokeDirect(0xE49224UL, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCB3584;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x120UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCB2CD4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x121UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCB2CD4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(x22)));
        __arm64_flags_left_13315276 = unchecked((uint)(x21));
        __arm64_flags_right_13315276 = unchecked((uint)(x8));
        if ((!((unchecked((uint)((__arm64_flags_left_13315276) - (__arm64_flags_right_13315276))) == unchecked((uint)0x0UL)))))
        {
            goto label_0xCB2CE8;
        }
        else
        {
            goto label_0xCB2CD4;
        }
        label_0xCB2CD4:
        ;
        __arm64_flags_left_13315284 = unchecked((uint)(x21));
        __arm64_flags_right_13315284 = unchecked((uint)0x1UL);
        __arm64_flags_result_13315284 = unchecked((uint)((__arm64_flags_left_13315284) - (__arm64_flags_right_13315284)));
        x21 = unchecked((ulong)(__arm64_flags_result_13315284));
        if ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13315284) - (__arm64_flags_right_13315284))))) < unchecked((int)0x0UL)))
        {
            goto label_0xCB2C70;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xE8UL))));
        if ((x8 != 0x0UL))
        {
            goto label_0xCB2C94;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCB2CE4UL);
        }
        goto label_0xCB3584;
        label_0xCB2CE8:
        ;
        x0 = x19;
        x1 = unchecked((ulong)(unchecked((uint)(x21))));
        x2 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x3 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x0 = RuntimeCalls.InvokeDirect(0xCB2694UL /* metadata target: PlayerWeapons.SelectWeapon */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x1 = x0;
        x0 = x19;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1795D40UL /* metadata target: MonoBehaviour.StartCoroutine */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        goto label_0xCB2C70;
        label_0xCB2D10:
        ;
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x2B1UL))))))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCB2A64;
        }
        else
        {
            goto label_0xCB2D18;
        }
        label_0xCB2D18:
        ;
        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x120UL))))), 0));
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179AD30UL /* metadata target: Time.get_time */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x8 = 0x432000UL;
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x4A4UL))))), 0));
        x0 = 0x0UL;
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x12CUL))))), 0));
        __arm64_float_flags_left_13315384 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13315384 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        x8 = unchecked((ulong)(((__arm64_float_flags_left_13315384 > __arm64_float_flags_right_13315384) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x128UL))), unchecked((byte)(unchecked((uint)(x8)))));
        x0 = RuntimeCalls.InvokeDirect(0x179AD30UL /* metadata target: Time.get_time */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0))))), 0));
        __arm64_float_flags_left_13315404 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13315404 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_13315404 >= __arm64_float_flags_right_13315404) || ((__arm64_float_flags_left_13315404 != __arm64_float_flags_left_13315404) || (__arm64_float_flags_right_13315404 != __arm64_float_flags_right_13315404))))
        {
            goto label_0xCB2D58;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCB2D54UL);
        }
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x129UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        goto label_0xCB2D58;
        label_0xCB2D58:
        ;
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x124UL))))), 0));
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179AD30UL /* metadata target: Time.get_time */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x8 = 0x432000UL;
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x4D8UL))))), 0));
        x0 = 0x0UL;
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        __arm64_float_flags_left_13315444 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13315444 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        x8 = unchecked((ulong)(((__arm64_float_flags_left_13315444 > __arm64_float_flags_right_13315444) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x130UL))), unchecked((byte)(unchecked((uint)(x8)))));
        x0 = RuntimeCalls.InvokeDirect(0x179AE58UL /* metadata target: Time.get_timeScale */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x148UL))))))));
        __arm64_float_flags_left_13315464 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13315464 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        if (((__arm64_float_flags_left_13315464 <= __arm64_float_flags_right_13315464) || ((__arm64_float_flags_left_13315464 != __arm64_float_flags_left_13315464) || (__arm64_float_flags_right_13315464 != __arm64_float_flags_right_13315464))))
        {
            goto label_0xCB2DC0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCB2D90UL);
        }
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCB2E18;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x150UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCB3584;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_13315488 = unchecked((uint)(x9));
        __arm64_flags_right_13315488 = unchecked((uint)0x1UL);
        if (((!((__arm64_flags_left_13315488 >= __arm64_flags_right_13315488))) || (unchecked((uint)((__arm64_flags_left_13315488) - (__arm64_flags_right_13315488))) == unchecked((uint)0x0UL))))
        {
            goto label_0xCB3588;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x28UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCB3584;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x176A5CCUL /* metadata target: AudioSource.Play */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x148UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        goto label_0xCB2E18;
        label_0xCB2DC0:
        ;
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCB2E18;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x150UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCB3584;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_13315536 = unchecked((uint)(x9));
        __arm64_flags_right_13315536 = unchecked((uint)0x1UL);
        if (((!((__arm64_flags_left_13315536 >= __arm64_flags_right_13315536))) || (unchecked((uint)((__arm64_flags_left_13315536) - (__arm64_flags_right_13315536))) == unchecked((uint)0x0UL))))
        {
            goto label_0xCB3588;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x28UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCB3584;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x176A7E4UL /* metadata target: AudioSource.get_isPlaying */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCB2E18;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x150UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCB3584;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_13315576 = unchecked((uint)(x9));
        __arm64_flags_right_13315576 = unchecked((uint)0x1UL);
        if (((!((__arm64_flags_left_13315576 >= __arm64_flags_right_13315576))) || (unchecked((uint)((__arm64_flags_left_13315576) - (__arm64_flags_right_13315576))) == unchecked((uint)0x0UL))))
        {
            goto label_0xCB3588;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x28UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCB3584;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x176A7A8UL /* metadata target: AudioSource.Pause */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x148UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCB2E18;
        label_0xCB2E18:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        __arm64_pair_address_13315620 = sp;
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13315620)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13315620) + (0x8UL))))), 0));
        sp = unchecked((ulong)((__arm64_pair_address_13315620) + (0x40UL)));
        return x0;
        label_0xCB2E2C:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xF8UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCB3584;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0xE0UL))))));
        x10 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) + (unchecked((uint)(0x1UL)))))));
        x11 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x10))) - (unchecked((uint)(0x1UL)))))));
        __arm64_flags_left_13315652 = unchecked((uint)(x9));
        __arm64_flags_right_13315652 = unchecked((uint)(x11));
        if (((unchecked((uint)((__arm64_flags_left_13315652) - (__arm64_flags_right_13315652))) == unchecked((uint)0x0UL)) || ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13315652) - (__arm64_flags_right_13315652))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_13315652)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13315652)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13315652) - (__arm64_flags_right_13315652))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13315652)) < unchecked((int)0x0UL)))))))
        {
            goto label_0xCB2F20;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCB2E4CUL);
        }
        if ((unchecked((uint)(x10)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCB3588;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCB3584;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = 0x1A8E000UL;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x158UL))));
        x1 = RuntimeMemory.ReadU64(x20);
        x0 = RuntimeCalls.InvokeDirect(0xE49224UL, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCB3584;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x120UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCB2F9C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xF8UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCB3584;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCB3588;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCB3584;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(x20);
        x0 = RuntimeCalls.InvokeDirect(0xE49224UL, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCB3584;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x128UL))))));
        __arm64_flags_left_13315740 = unchecked((uint)(x8));
        __arm64_flags_right_13315740 = unchecked((uint)0x1UL);
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13315740) - (__arm64_flags_right_13315740))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_13315740)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13315740)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13315740) - (__arm64_flags_right_13315740))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13315740)) < unchecked((int)0x0UL))))))
        {
            goto label_0xCB2F9C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCB2EA4UL);
        }
        RuntimeMemory.WritePtr(unchecked((ulong)((x19) + (0xE0UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        goto label_0xCB2F9C;
        label_0xCB2EAC:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x80UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCB3584;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x9BUL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCB2AEC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x17CUL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCB2AEC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xA8UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCB3584;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x1A5UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCB2AEC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x98UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCB3584;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x0 = RuntimeCalls.InvokeDirect(0xCB35F8UL /* metadata target: WeaponBehavior.CancelWeaponPull */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0xDCUL))))));
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0xD4UL))))));
        x20 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x2 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = x19;
        x3 = unchecked((ulong)(unchecked((uint)0x0UL)));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x17EUL))), unchecked((byte)(unchecked((uint)(x20)))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x19) + (0x178UL))), unchecked((uint)(x8)));
        x0 = RuntimeCalls.InvokeDirect(0xCB2694UL /* metadata target: PlayerWeapons.SelectWeapon */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x1 = x0;
        x0 = x19;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1795D40UL /* metadata target: MonoBehaviour.StartCoroutine */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        RuntimeMemory.WriteU16(unchecked((ulong)((x19) + (0x17CUL))), unchecked((ushort)(unchecked((uint)(x20)))));
        goto label_0xCB2AEC;
        label_0xCB2F20:
        ;
        __arm64_flags_left_13315872 = unchecked((uint)(x9));
        __arm64_flags_right_13315872 = unchecked((uint)(x10));
        if ((__arm64_flags_left_13315872 >= __arm64_flags_right_13315872))
        {
            goto label_0xCB3588;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) + (unchecked((uint)((unchecked((uint)(x9))) << (int)(unchecked((int)(unchecked((uint)(0x3UL))))))))))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCB3584;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = 0x1A8E000UL;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x158UL))));
        x1 = RuntimeMemory.ReadU64(x20);
        x0 = RuntimeCalls.InvokeDirect(0xE49224UL, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCB3584;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x120UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCB2F9C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xF8UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCB3584;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0xE0UL))))));
        x10 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) + (unchecked((uint)(0x1UL)))))));
        __arm64_flags_left_13315940 = unchecked((uint)(x9));
        __arm64_flags_right_13315940 = unchecked((uint)(x10));
        if ((__arm64_flags_left_13315940 >= __arm64_flags_right_13315940))
        {
            goto label_0xCB3588;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) << (int)(unchecked((int)(unchecked((uint)(0x3UL))))))))))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCB3584;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(x20);
        x0 = RuntimeCalls.InvokeDirect(0xE49224UL, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCB3584;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x128UL))))));
        __arm64_flags_left_13315976 = unchecked((uint)(x8));
        __arm64_flags_right_13315976 = unchecked((uint)0x1UL);
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13315976) - (__arm64_flags_right_13315976))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_13315976)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13315976)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13315976) - (__arm64_flags_right_13315976))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13315976)) < unchecked((int)0x0UL))))))
        {
            goto label_0xCB2F9C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0xE0UL))))));
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) + (unchecked((uint)(0x1UL)))))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x19) + (0xE0UL))), unchecked((uint)(x8)));
        goto label_0xCB2F9C;
        label_0xCB2F9C:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xF8UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCB3584;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(unchecked((long)(RuntimeMemory.ReadS32(unchecked((ulong)((x19) + (0xE0UL))))))));
        x10 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_13316012 = unchecked((uint)(x9));
        __arm64_flags_right_13316012 = unchecked((uint)(x10));
        if ((__arm64_flags_left_13316012 >= __arm64_flags_right_13316012))
        {
            goto label_0xCB3588;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)((x9) << (int)(unchecked((int)(0x3UL))))))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCB3584;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x158UL))));
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xE49224UL, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x1 = x0;
        x0 = unchecked((ulong)((x19) + (0x180UL)));
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x180UL))), x1);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x180UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCB3584;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x120UL))))))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCB2ABC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x128UL))))));
        __arm64_flags_left_13316084 = unchecked((uint)(x9));
        __arm64_flags_right_13316084 = unchecked((uint)0x1UL);
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13316084) - (__arm64_flags_right_13316084))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_13316084)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13316084)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13316084) - (__arm64_flags_right_13316084))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13316084)) < unchecked((int)0x0UL))))))
        {
            goto label_0xCB2ABC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x124UL))))));
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0xDCUL))))));
        x10 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = 0x0UL;
        RuntimeMemory.WriteU32(unchecked((ulong)((x19) + (0xD4UL))), unchecked((uint)(x8)));
        RuntimeMemory.WriteU32(unchecked((ulong)((x19) + (0x178UL))), unchecked((uint)(x9)));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x129UL))), unchecked((byte)(unchecked((uint)(x10)))));
        x0 = RuntimeCalls.InvokeDirect(0x179AD30UL /* metadata target: Time.get_time */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0xD4UL))))));
        x2 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = x19;
        x3 = unchecked((ulong)(unchecked((uint)0x0UL)));
        RuntimeMemory.WriteF32(unchecked((ulong)((x19) + (0x12CUL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        x0 = RuntimeCalls.InvokeDirect(0xCB2694UL /* metadata target: PlayerWeapons.SelectWeapon */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x1 = x0;
        x0 = x19;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1795D40UL /* metadata target: MonoBehaviour.StartCoroutine */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xCB358CUL /* metadata target: PlayerWeapons.DisplayGrenadeSwitch */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x1 = x0;
        x0 = x19;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1795D40UL /* metadata target: MonoBehaviour.StartCoroutine */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        goto label_0xCB2ABC;
        label_0xCB3060:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xE8UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCB3584;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_13316204 = unchecked((uint)(x9));
        __arm64_flags_right_13316204 = unchecked((uint)0x1UL);
        __arm64_flags_result_13316204 = unchecked((uint)((__arm64_flags_left_13316204) - (__arm64_flags_right_13316204)));
        x20 = unchecked((ulong)(__arm64_flags_result_13316204));
        if ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13316204) - (__arm64_flags_right_13316204))))) < unchecked((int)0x0UL)))
        {
            goto label_0xCB3358;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x21 = 0x1A8E000UL;
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x158UL))));
        goto label_0xCB307C;
        label_0xCB307C:
        ;
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_13316224 = unchecked((uint)(x20));
        __arm64_flags_right_13316224 = unchecked((uint)(x9));
        if ((__arm64_flags_left_13316224 >= __arm64_flags_right_13316224))
        {
            goto label_0xCB3588;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x20))) << (int)(unchecked((int)(unchecked((uint)(0x3UL))))))))))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCB3584;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(x21);
        x0 = RuntimeCalls.InvokeDirect(0xE49224UL, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCB3584;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x120UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCB30BC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x121UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCB30BC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(x22)));
        __arm64_flags_left_13316276 = unchecked((uint)(x20));
        __arm64_flags_right_13316276 = unchecked((uint)(x8));
        if ((!((unchecked((uint)((__arm64_flags_left_13316276) - (__arm64_flags_right_13316276))) == unchecked((uint)0x0UL)))))
        {
            goto label_0xCB3334;
        }
        else
        {
            goto label_0xCB30BC;
        }
        label_0xCB30BC:
        ;
        __arm64_flags_left_13316284 = unchecked((uint)(x20));
        __arm64_flags_right_13316284 = unchecked((uint)0x1UL);
        __arm64_flags_result_13316284 = unchecked((uint)((__arm64_flags_left_13316284) - (__arm64_flags_right_13316284)));
        x20 = unchecked((ulong)(__arm64_flags_result_13316284));
        if ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13316284) - (__arm64_flags_right_13316284))))) < unchecked((int)0x0UL)))
        {
            goto label_0xCB3358;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xE8UL))));
        if ((x8 != 0x0UL))
        {
            goto label_0xCB307C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCB30CCUL);
        }
        goto label_0xCB3584;
        label_0xCB30D0:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x98UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCB3584;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x122UL))))))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCB2B2C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x25DUL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCB2B2C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xCB3684UL /* metadata target: PlayerWeapons.DropWeapon */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        goto label_0xCB2B2C;
        label_0xCB30F4:
        ;
        __arm64_float_flags_left_13316340 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13316340 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        if (((__arm64_float_flags_left_13316340 <= __arm64_float_flags_right_13316340) || ((__arm64_float_flags_left_13316340 != __arm64_float_flags_left_13316340) || (__arm64_float_flags_right_13316340 != __arm64_float_flags_right_13316340))))
        {
            goto label_0xCB310C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xA8UL))));
        if ((x9 == 0x0UL))
        {
            goto label_0xCB3584;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x9) + (0x1A5UL))))))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCB311C;
        }
        else
        {
            goto label_0xCB310C;
        }
        label_0xCB310C:
        ;
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((unchecked((ulong)(unchecked((uint)(x8))))) + (0xA8UL))))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCB311C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((unchecked((ulong)(unchecked((uint)(x8))))) + (0xF1UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCB3570;
        }
        else
        {
            goto label_0xCB311C;
        }
        label_0xCB311C:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xE8UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCB3584;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x18UL))));
        x20 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0xDCUL))))));
        x10 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) - (unchecked((uint)(0x1UL)))))));
        __arm64_flags_left_13316400 = unchecked((uint)(x20));
        __arm64_flags_right_13316400 = unchecked((uint)(x10));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13316400) - (__arm64_flags_right_13316400))))) < unchecked((int)0x0UL)) == (((unchecked((int)(__arm64_flags_left_13316400)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13316400)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13316400) - (__arm64_flags_right_13316400))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13316400)) < unchecked((int)0x0UL))))))
        {
            goto label_0xCB3298;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCB3138UL);
        }
        __arm64_flags_left_13316408 = unchecked((uint)(x20));
        __arm64_flags_right_13316408 = unchecked((uint)(x9));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13316408) - (__arm64_flags_right_13316408))))) < unchecked((int)0x0UL)) == (((unchecked((int)(__arm64_flags_left_13316408)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13316408)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13316408) - (__arm64_flags_right_13316408))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13316408)) < unchecked((int)0x0UL))))))
        {
            goto label_0xCB3358;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x23 = 0x1A8E000UL;
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0x158UL))));
        goto label_0xCB3148;
        label_0xCB3148:
        ;
        __arm64_flags_left_13316424 = unchecked((uint)(x20));
        __arm64_flags_right_13316424 = unchecked((uint)(x9));
        if ((__arm64_flags_left_13316424 >= __arm64_flags_right_13316424))
        {
            goto label_0xCB3588;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x20))) << (int)(unchecked((int)(unchecked((uint)(0x3UL))))))))))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCB3584;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(x23);
        x0 = RuntimeCalls.InvokeDirect(0xE49224UL, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCB3584;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x120UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCB31AC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x121UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCB31AC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(x22)));
        __arm64_flags_left_13316476 = unchecked((uint)(x20));
        __arm64_flags_right_13316476 = unchecked((uint)(x8));
        if ((unchecked((uint)((__arm64_flags_left_13316476) - (__arm64_flags_right_13316476))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCB318C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x138UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCB3334;
        }
        else
        {
            goto label_0xCB318C;
        }
        label_0xCB318C:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(x22)));
        __arm64_flags_left_13316496 = unchecked((uint)(x20));
        __arm64_flags_right_13316496 = unchecked((uint)(x8));
        if ((unchecked((uint)((__arm64_flags_left_13316496) - (__arm64_flags_right_13316496))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCB31AC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0xD0UL))))));
        __arm64_flags_left_13316508 = unchecked((uint)(x20));
        __arm64_flags_right_13316508 = unchecked((uint)(x8));
        if ((unchecked((uint)((__arm64_flags_left_13316508) - (__arm64_flags_right_13316508))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCB31AC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x138UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCB3334;
        }
        else
        {
            goto label_0xCB31AC;
        }
        label_0xCB31AC:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xE8UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCB3584;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x18UL))));
        x10 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) - (unchecked((uint)(0x1UL)))))));
        __arm64_flags_left_13316540 = unchecked((uint)(x20));
        __arm64_flags_right_13316540 = unchecked((uint)(x10));
        if ((!((unchecked((uint)((__arm64_flags_left_13316540) - (__arm64_flags_right_13316540))) == unchecked((uint)0x0UL)))))
        {
            goto label_0xCB3284;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) - (unchecked((uint)(0x1UL)))))));
        __arm64_flags_left_13316552 = unchecked((uint)(x10));
        __arm64_flags_right_13316552 = unchecked((uint)0x1UL);
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13316552) - (__arm64_flags_right_13316552))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_13316552)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13316552)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13316552) - (__arm64_flags_right_13316552))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13316552)) < unchecked((int)0x0UL))))))
        {
            goto label_0xCB3284;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x21 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xCB31D4;
        label_0xCB31D4:
        ;
        __arm64_flags_left_13316564 = unchecked((uint)(x21));
        __arm64_flags_right_13316564 = unchecked((uint)(x9));
        if ((__arm64_flags_left_13316564 >= __arm64_flags_right_13316564))
        {
            goto label_0xCB3588;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x21))) << (int)(unchecked((int)(unchecked((uint)(0x3UL))))))))))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCB3584;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(x23);
        x0 = RuntimeCalls.InvokeDirect(0xE49224UL, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCB3584;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x120UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCB3238;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x121UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCB3238;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(x22)));
        __arm64_flags_left_13316616 = unchecked((uint)(x21));
        __arm64_flags_right_13316616 = unchecked((uint)(x8));
        if ((unchecked((uint)((__arm64_flags_left_13316616) - (__arm64_flags_right_13316616))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCB3218;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x138UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCB3258;
        }
        else
        {
            goto label_0xCB3218;
        }
        label_0xCB3218:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(x22)));
        __arm64_flags_left_13316636 = unchecked((uint)(x21));
        __arm64_flags_right_13316636 = unchecked((uint)(x8));
        if ((unchecked((uint)((__arm64_flags_left_13316636) - (__arm64_flags_right_13316636))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCB3238;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0xD0UL))))));
        __arm64_flags_left_13316648 = unchecked((uint)(x21));
        __arm64_flags_right_13316648 = unchecked((uint)(x8));
        if ((unchecked((uint)((__arm64_flags_left_13316648) - (__arm64_flags_right_13316648))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCB3238;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x138UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCB3258;
        }
        else
        {
            goto label_0xCB3238;
        }
        label_0xCB3238:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xE8UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCB3584;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        x21 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x21))) + (unchecked((uint)(0x1UL)))))));
        x10 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) - (unchecked((uint)(0x1UL)))))));
        __arm64_flags_left_13316684 = unchecked((uint)(x21));
        __arm64_flags_right_13316684 = unchecked((uint)(x10));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13316684) - (__arm64_flags_right_13316684))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_13316684)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13316684)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13316684) - (__arm64_flags_right_13316684))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13316684)) < unchecked((int)0x0UL))))))
        {
            goto label_0xCB31D4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCB3254UL);
        }
        goto label_0xCB3284;
        label_0xCB3258:
        ;
        x0 = x19;
        x1 = unchecked((ulong)(unchecked((uint)(x21))));
        x2 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x3 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x0 = RuntimeCalls.InvokeDirect(0xCB2694UL /* metadata target: PlayerWeapons.SelectWeapon */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x1 = x0;
        x0 = x19;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1795D40UL /* metadata target: MonoBehaviour.StartCoroutine */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xE8UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCB3584;
        }
        else
        {
            goto label_0xCB3284;
        }
        label_0xCB3284:
        ;
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        x20 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x20))) + (unchecked((uint)(0x1UL)))))));
        __arm64_flags_left_13316748 = unchecked((uint)(x20));
        __arm64_flags_right_13316748 = unchecked((uint)(x9));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13316748) - (__arm64_flags_right_13316748))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_13316748)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13316748)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13316748) - (__arm64_flags_right_13316748))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13316748)) < unchecked((int)0x0UL))))))
        {
            goto label_0xCB3148;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCB3294UL);
        }
        goto label_0xCB3358;
        label_0xCB3298:
        ;
        x10 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) - (unchecked((uint)(0x1UL)))))));
        __arm64_flags_left_13316764 = unchecked((uint)(x10));
        __arm64_flags_right_13316764 = unchecked((uint)0x1UL);
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13316764) - (__arm64_flags_right_13316764))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_13316764)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13316764)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13316764) - (__arm64_flags_right_13316764))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13316764)) < unchecked((int)0x0UL))))))
        {
            goto label_0xCB3358;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x21 = 0x1A8E000UL;
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x158UL))));
        x20 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xCB32B0;
        label_0xCB32B0:
        ;
        __arm64_flags_left_13316784 = unchecked((uint)(x20));
        __arm64_flags_right_13316784 = unchecked((uint)(x9));
        if ((__arm64_flags_left_13316784 >= __arm64_flags_right_13316784))
        {
            goto label_0xCB3588;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x20))) << (int)(unchecked((int)(unchecked((uint)(0x3UL))))))))))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCB3584;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(x21);
        x0 = RuntimeCalls.InvokeDirect(0xE49224UL, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCB3584;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x120UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCB3314;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x121UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCB3314;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(x22)));
        __arm64_flags_left_13316836 = unchecked((uint)(x20));
        __arm64_flags_right_13316836 = unchecked((uint)(x8));
        if ((unchecked((uint)((__arm64_flags_left_13316836) - (__arm64_flags_right_13316836))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCB32F4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x138UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCB3334;
        }
        else
        {
            goto label_0xCB32F4;
        }
        label_0xCB32F4:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(x22)));
        __arm64_flags_left_13316856 = unchecked((uint)(x20));
        __arm64_flags_right_13316856 = unchecked((uint)(x8));
        if ((unchecked((uint)((__arm64_flags_left_13316856) - (__arm64_flags_right_13316856))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCB3314;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0xD0UL))))));
        __arm64_flags_left_13316868 = unchecked((uint)(x20));
        __arm64_flags_right_13316868 = unchecked((uint)(x8));
        if ((unchecked((uint)((__arm64_flags_left_13316868) - (__arm64_flags_right_13316868))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCB3314;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x138UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCB3334;
        }
        else
        {
            goto label_0xCB3314;
        }
        label_0xCB3314:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xE8UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCB3584;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        x20 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x20))) + (unchecked((uint)(0x1UL)))))));
        x10 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) - (unchecked((uint)(0x1UL)))))));
        __arm64_flags_left_13316904 = unchecked((uint)(x20));
        __arm64_flags_right_13316904 = unchecked((uint)(x10));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13316904) - (__arm64_flags_right_13316904))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_13316904)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13316904)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13316904) - (__arm64_flags_right_13316904))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13316904)) < unchecked((int)0x0UL))))))
        {
            goto label_0xCB32B0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCB3330UL);
        }
        goto label_0xCB3358;
        label_0xCB3334:
        ;
        x0 = x19;
        x1 = unchecked((ulong)(unchecked((uint)(x20))));
        x2 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x3 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x0 = RuntimeCalls.InvokeDirect(0xCB2694UL /* metadata target: PlayerWeapons.SelectWeapon */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x1 = x0;
        x0 = x19;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1795D40UL /* metadata target: MonoBehaviour.StartCoroutine */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        goto label_0xCB3358;
        label_0xCB3358:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x80UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCB3584;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x9FUL))))))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCB337C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(x22)));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCB2D18;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x19;
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xCB3550;
        label_0xCB337C:
        ;
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((unchecked((ulong)(unchecked((uint)(x8))))) + (0xABUL))))))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCB33B0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xE8UL))));
        if ((x9 == 0x0UL))
        {
            goto label_0xCB3584;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x9) + (0x18UL))))));
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) - (unchecked((uint)(0x1UL)))))));
        __arm64_flags_left_13317012 = unchecked((uint)(x9));
        __arm64_flags_right_13317012 = unchecked((uint)0x1UL);
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13317012) - (__arm64_flags_right_13317012))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_13317012)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13317012)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13317012) - (__arm64_flags_right_13317012))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13317012)) < unchecked((int)0x0UL))))))
        {
            goto label_0xCB33B0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(x22)));
        __arm64_flags_left_13317024 = unchecked((uint)(x8));
        __arm64_flags_right_13317024 = unchecked((uint)0x1UL);
        if ((unchecked((uint)((__arm64_flags_left_13317024) - (__arm64_flags_right_13317024))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCB2D18;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        goto label_0xCB354C;
        label_0xCB33B0:
        ;
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((unchecked((ulong)(unchecked((uint)(x8))))) + (0xACUL))))))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCB33D0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xE8UL))));
        if ((x9 == 0x0UL))
        {
            goto label_0xCB3584;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x9) + (0x18UL))))));
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) - (unchecked((uint)(0x1UL)))))));
        __arm64_flags_left_13317064 = unchecked((uint)(x9));
        __arm64_flags_right_13317064 = unchecked((uint)0x2UL);
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13317064) - (__arm64_flags_right_13317064))))) < unchecked((int)0x0UL)) == (((unchecked((int)(__arm64_flags_left_13317064)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13317064)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13317064) - (__arm64_flags_right_13317064))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13317064)) < unchecked((int)0x0UL))))))
        {
            goto label_0xCB34C4;
        }
        else
        {
            goto label_0xCB33D0;
        }
        label_0xCB33D0:
        ;
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((unchecked((ulong)(unchecked((uint)(x8))))) + (0xADUL))))))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCB33F0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xE8UL))));
        if ((x9 == 0x0UL))
        {
            goto label_0xCB3584;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x9) + (0x18UL))))));
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) - (unchecked((uint)(0x1UL)))))));
        __arm64_flags_left_13317096 = unchecked((uint)(x9));
        __arm64_flags_right_13317096 = unchecked((uint)0x3UL);
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13317096) - (__arm64_flags_right_13317096))))) < unchecked((int)0x0UL)) == (((unchecked((int)(__arm64_flags_left_13317096)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13317096)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13317096) - (__arm64_flags_right_13317096))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13317096)) < unchecked((int)0x0UL))))))
        {
            goto label_0xCB34D8;
        }
        else
        {
            goto label_0xCB33F0;
        }
        label_0xCB33F0:
        ;
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((unchecked((ulong)(unchecked((uint)(x8))))) + (0xAEUL))))))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCB3410;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xE8UL))));
        if ((x9 == 0x0UL))
        {
            goto label_0xCB3584;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x9) + (0x18UL))))));
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) - (unchecked((uint)(0x1UL)))))));
        __arm64_flags_left_13317128 = unchecked((uint)(x9));
        __arm64_flags_right_13317128 = unchecked((uint)0x4UL);
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13317128) - (__arm64_flags_right_13317128))))) < unchecked((int)0x0UL)) == (((unchecked((int)(__arm64_flags_left_13317128)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13317128)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13317128) - (__arm64_flags_right_13317128))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13317128)) < unchecked((int)0x0UL))))))
        {
            goto label_0xCB34EC;
        }
        else
        {
            goto label_0xCB3410;
        }
        label_0xCB3410:
        ;
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((unchecked((ulong)(unchecked((uint)(x8))))) + (0xAFUL))))))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCB3430;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xE8UL))));
        if ((x9 == 0x0UL))
        {
            goto label_0xCB3584;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x9) + (0x18UL))))));
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) - (unchecked((uint)(0x1UL)))))));
        __arm64_flags_left_13317160 = unchecked((uint)(x9));
        __arm64_flags_right_13317160 = unchecked((uint)0x5UL);
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13317160) - (__arm64_flags_right_13317160))))) < unchecked((int)0x0UL)) == (((unchecked((int)(__arm64_flags_left_13317160)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13317160)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13317160) - (__arm64_flags_right_13317160))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13317160)) < unchecked((int)0x0UL))))))
        {
            goto label_0xCB3500;
        }
        else
        {
            goto label_0xCB3430;
        }
        label_0xCB3430:
        ;
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((unchecked((ulong)(unchecked((uint)(x8))))) + (0xB0UL))))))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCB3450;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xE8UL))));
        if ((x9 == 0x0UL))
        {
            goto label_0xCB3584;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x9) + (0x18UL))))));
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) - (unchecked((uint)(0x1UL)))))));
        __arm64_flags_left_13317192 = unchecked((uint)(x9));
        __arm64_flags_right_13317192 = unchecked((uint)0x6UL);
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13317192) - (__arm64_flags_right_13317192))))) < unchecked((int)0x0UL)) == (((unchecked((int)(__arm64_flags_left_13317192)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13317192)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13317192) - (__arm64_flags_right_13317192))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13317192)) < unchecked((int)0x0UL))))))
        {
            goto label_0xCB3514;
        }
        else
        {
            goto label_0xCB3450;
        }
        label_0xCB3450:
        ;
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((unchecked((ulong)(unchecked((uint)(x8))))) + (0xB1UL))))))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCB3470;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xE8UL))));
        if ((x9 == 0x0UL))
        {
            goto label_0xCB3584;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x9) + (0x18UL))))));
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) - (unchecked((uint)(0x1UL)))))));
        __arm64_flags_left_13317224 = unchecked((uint)(x9));
        __arm64_flags_right_13317224 = unchecked((uint)0x7UL);
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13317224) - (__arm64_flags_right_13317224))))) < unchecked((int)0x0UL)) == (((unchecked((int)(__arm64_flags_left_13317224)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13317224)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13317224) - (__arm64_flags_right_13317224))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13317224)) < unchecked((int)0x0UL))))))
        {
            goto label_0xCB3528;
        }
        else
        {
            goto label_0xCB3470;
        }
        label_0xCB3470:
        ;
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((unchecked((ulong)(unchecked((uint)(x8))))) + (0xB2UL))))))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCB3490;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xE8UL))));
        if ((x9 == 0x0UL))
        {
            goto label_0xCB3584;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x9) + (0x18UL))))));
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) - (unchecked((uint)(0x1UL)))))));
        __arm64_flags_left_13317256 = unchecked((uint)(x9));
        __arm64_flags_right_13317256 = unchecked((uint)0x8UL);
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13317256) - (__arm64_flags_right_13317256))))) < unchecked((int)0x0UL)) == (((unchecked((int)(__arm64_flags_left_13317256)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13317256)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13317256) - (__arm64_flags_right_13317256))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13317256)) < unchecked((int)0x0UL))))))
        {
            goto label_0xCB353C;
        }
        else
        {
            goto label_0xCB3490;
        }
        label_0xCB3490:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((unchecked((ulong)(unchecked((uint)(x8))))) + (0xB3UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCB2D18;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xE8UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCB3584;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) - (unchecked((uint)(0x1UL)))))));
        __arm64_flags_left_13317288 = unchecked((uint)(x8));
        __arm64_flags_right_13317288 = unchecked((uint)0x9UL);
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13317288) - (__arm64_flags_right_13317288))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_13317288)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13317288)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13317288) - (__arm64_flags_right_13317288))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13317288)) < unchecked((int)0x0UL))))))
        {
            goto label_0xCB2D18;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(x22)));
        __arm64_flags_left_13317300 = unchecked((uint)(x8));
        __arm64_flags_right_13317300 = unchecked((uint)0x9UL);
        if ((unchecked((uint)((__arm64_flags_left_13317300) - (__arm64_flags_right_13317300))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCB2D18;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)(0x9UL))));
        goto label_0xCB354C;
        label_0xCB34C4:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(x22)));
        __arm64_flags_left_13317320 = unchecked((uint)(x8));
        __arm64_flags_right_13317320 = unchecked((uint)0x2UL);
        if ((unchecked((uint)((__arm64_flags_left_13317320) - (__arm64_flags_right_13317320))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCB2D18;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)(0x2UL))));
        goto label_0xCB354C;
        label_0xCB34D8:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(x22)));
        __arm64_flags_left_13317340 = unchecked((uint)(x8));
        __arm64_flags_right_13317340 = unchecked((uint)0x3UL);
        if ((unchecked((uint)((__arm64_flags_left_13317340) - (__arm64_flags_right_13317340))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCB2D18;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)(0x3UL))));
        goto label_0xCB354C;
        label_0xCB34EC:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(x22)));
        __arm64_flags_left_13317360 = unchecked((uint)(x8));
        __arm64_flags_right_13317360 = unchecked((uint)0x4UL);
        if ((unchecked((uint)((__arm64_flags_left_13317360) - (__arm64_flags_right_13317360))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCB2D18;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)(0x4UL))));
        goto label_0xCB354C;
        label_0xCB3500:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(x22)));
        __arm64_flags_left_13317380 = unchecked((uint)(x8));
        __arm64_flags_right_13317380 = unchecked((uint)0x5UL);
        if ((unchecked((uint)((__arm64_flags_left_13317380) - (__arm64_flags_right_13317380))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCB2D18;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)(0x5UL))));
        goto label_0xCB354C;
        label_0xCB3514:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(x22)));
        __arm64_flags_left_13317400 = unchecked((uint)(x8));
        __arm64_flags_right_13317400 = unchecked((uint)0x6UL);
        if ((unchecked((uint)((__arm64_flags_left_13317400) - (__arm64_flags_right_13317400))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCB2D18;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)(0x6UL))));
        goto label_0xCB354C;
        label_0xCB3528:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(x22)));
        __arm64_flags_left_13317420 = unchecked((uint)(x8));
        __arm64_flags_right_13317420 = unchecked((uint)0x7UL);
        if ((unchecked((uint)((__arm64_flags_left_13317420) - (__arm64_flags_right_13317420))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCB2D18;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)(0x7UL))));
        goto label_0xCB354C;
        label_0xCB353C:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(x22)));
        __arm64_flags_left_13317440 = unchecked((uint)(x8));
        __arm64_flags_right_13317440 = unchecked((uint)0x8UL);
        if ((unchecked((uint)((__arm64_flags_left_13317440) - (__arm64_flags_right_13317440))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCB2D18;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)(0x8UL))));
        goto label_0xCB354C;
        label_0xCB354C:
        ;
        x0 = x19;
        goto label_0xCB3550;
        label_0xCB3550:
        ;
        x2 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x3 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x0 = RuntimeCalls.InvokeDirect(0xCB2694UL /* metadata target: PlayerWeapons.SelectWeapon */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x1 = x0;
        x0 = x19;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1795D40UL /* metadata target: MonoBehaviour.StartCoroutine */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        goto label_0xCB2D18;
        label_0xCB3570:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x138UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCB3358;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0xD8UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCB311C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCB3580UL);
        }
        goto label_0xCB3358;
        label_0xCB3584:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        goto label_0xCB3588;
        label_0xCB3588:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB7CUL, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        return default(ulong);
    }
```

## `PlayerWeapons.DisplayGrenadeSwitch` — RVA `0xcb358c`

- Lift status: **exact**; input span: 108 bytes; span to next metadata RVA: 108 bytes.
- Metadata signature: `private IEnumerator DisplayGrenadeSwitch() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=16 (informational only).

```csharp
public static ulong PlayerWeapons_DisplayGrenadeSwitch_RVAcb358c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
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
        x21 = 0x1A8E000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x4D6UL))))))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x650UL))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
        }
        else
        {
            x0 = 0x1A8E000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x650UL))));
            // Likely IL2CPP class initialization helper (guarded call).
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
            RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x4D6UL))), unchecked((byte)(unchecked((uint)(x8)))));
        }
        label_0xCB35C0:
        ;
        x0 = RuntimeMemory.ReadU64(x21);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x1589338UL /* metadata target: Object.ctor */, x0, x1, x2, x3);
        x0 = x20;
        RuntimeMemory.WritePtr(unchecked((ulong)((x20) + (0x10UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x20UL))), x19);
        x1 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = x20;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return x0;
        return default(ulong);
    }
```

## `PlayerWeapons.DropWeapon` — RVA `0xcb3684`

- Lift status: **partial**; input span: 1416 bytes; span to next metadata RVA: 1416 bytes.
- Metadata signature: `public void DropWeapon(int weapon) { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=168 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'b.gt' at 0xcb37a4; reason: Unknown IR expression at 0xcb37a4; reason: Unsupported instruction 'b.gt' at 0xcb37b4; reason: Unknown IR expression at 0xcb37b4; reason: Unsupported instruction 'b.mi' at 0xcb37bc; reason: Unknown IR expression at 0xcb37bc; reason: Unsupported instruction 'fmov' at 0xcb392c; reason: Unsupported instruction 'fmul' at 0xcb3938

```csharp
public static ulong PlayerWeapons_DropWeapon_RVAcb3684(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13317888 = default(uint);
        uint __arm64_flags_left_13317952 = default(uint);
        uint __arm64_flags_left_13318000 = default(uint);
        uint __arm64_flags_left_13318092 = default(uint);
        uint __arm64_flags_left_13318100 = default(uint);
        uint __arm64_flags_left_13318148 = default(uint);
        uint __arm64_flags_left_13318248 = default(uint);
        uint __arm64_flags_left_13319076 = default(uint);
        uint __arm64_flags_left_13319096 = default(uint);
        uint __arm64_flags_right_13317888 = default(uint);
        uint __arm64_flags_right_13317952 = default(uint);
        uint __arm64_flags_right_13318000 = default(uint);
        uint __arm64_flags_right_13318092 = default(uint);
        uint __arm64_flags_right_13318100 = default(uint);
        uint __arm64_flags_right_13318148 = default(uint);
        uint __arm64_flags_right_13318248 = default(uint);
        uint __arm64_flags_right_13319076 = default(uint);
        uint __arm64_flags_right_13319096 = default(uint);
        float __arm64_float_flags_left_13318040 = default(float);
        float __arm64_float_flags_left_13318712 = default(float);
        float __arm64_float_flags_left_13318832 = default(float);
        float __arm64_float_flags_left_13319152 = default(float);
        float __arm64_float_flags_right_13318040 = default(float);
        float __arm64_float_flags_right_13318712 = default(float);
        float __arm64_float_flags_right_13318832 = default(float);
        float __arm64_float_flags_right_13319152 = default(float);
        ulong __arm64_pair_address_13317768 = default(ulong);
        ulong __arm64_pair_address_13317772 = default(ulong);
        ulong __arm64_pair_address_13317776 = default(ulong);
        ulong __arm64_pair_address_13318404 = default(ulong);
        ulong __arm64_pair_address_13318412 = default(ulong);
        ulong __arm64_pair_address_13318436 = default(ulong);
        ulong __arm64_pair_address_13318792 = default(ulong);
        ulong __arm64_pair_address_13318912 = default(ulong);
        ulong __arm64_pair_address_13318992 = default(ulong);
        ulong __arm64_pair_address_13318996 = default(ulong);
        ulong __arm64_pair_address_13319000 = default(ulong);
        ulong __arm64_pair_address_13319044 = default(ulong);
        ulong __arm64_pair_address_13319048 = default(ulong);
        ulong __arm64_pair_address_13319052 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v10 = default(RuntimeVector128);
        RuntimeVector128 v11 = default(RuntimeVector128);
        RuntimeVector128 v12 = default(RuntimeVector128);
        RuntimeVector128 v13 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
        RuntimeVector128 v4 = default(RuntimeVector128);
        RuntimeVector128 v5 = default(RuntimeVector128);
        RuntimeVector128 v6 = default(RuntimeVector128);
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
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        sp = unchecked((ulong)((sp) - (0xC0UL)));
        __arm64_pair_address_13317768 = unchecked((ulong)((sp) + (0x40UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13317768, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v13.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13317768) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v12.GetUInt64(0)))));
        __arm64_pair_address_13317772 = unchecked((ulong)((sp) + (0x50UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13317772, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v11.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13317772) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v10.GetUInt64(0)))));
        __arm64_pair_address_13317776 = unchecked((ulong)((sp) + (0x60UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13317776, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13317776) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x70UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x80UL)))) + (0x0UL))), x26);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x80UL)))) + (0x8UL))), x25);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x90UL)))) + (0x0UL))), x24);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x90UL)))) + (0x8UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xA0UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xA0UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xB0UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xB0UL)))) + (0x8UL))), x19);
        x21 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x4D7UL))))))));
        x20 = unchecked((ulong)(unchecked((uint)(x1))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCB36F4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x10UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x158UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x9C8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x4D7UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCB36F4;
        label_0xCB36F4:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xE8UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCB3C04;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_13317888 = unchecked((uint)(x9));
        __arm64_flags_right_13317888 = unchecked((uint)(x20));
        if (((!((__arm64_flags_left_13317888 >= __arm64_flags_right_13317888))) || (unchecked((uint)((__arm64_flags_left_13317888) - (__arm64_flags_right_13317888))) == unchecked((uint)0x0UL))))
        {
            goto label_0xCB3C08;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x23 = unchecked((ulong)(unchecked((int)(unchecked((uint)(x20))))));
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)((x23) << (int)(unchecked((int)(0x3UL))))))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCB3C04;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x22 = 0x1A8E000UL;
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x158UL))));
        x1 = RuntimeMemory.ReadU64(x22);
        x0 = RuntimeCalls.InvokeDirect(0xE49224UL, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCB3C04;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x120UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCB3B70;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xE8UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCB3C04;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_13317952 = unchecked((uint)(x9));
        __arm64_flags_right_13317952 = unchecked((uint)(x20));
        if (((!((__arm64_flags_left_13317952 >= __arm64_flags_right_13317952))) || (unchecked((uint)((__arm64_flags_left_13317952) - (__arm64_flags_right_13317952))) == unchecked((uint)0x0UL))))
        {
            goto label_0xCB3C08;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)((x23) << (int)(unchecked((int)(0x3UL))))))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCB3C04;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(x22);
        x0 = RuntimeCalls.InvokeDirect(0xE49224UL, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCB3C04;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCB3760UL);
        }
        RuntimeMemory.WriteU8(unchecked((ulong)((x0) + (0x120UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x150UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCB3C04;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_13318000 = unchecked((uint)(x9));
        __arm64_flags_right_13318000 = unchecked((uint)0x1UL);
        if (((!((__arm64_flags_left_13318000 >= __arm64_flags_right_13318000))) || (unchecked((uint)((__arm64_flags_left_13318000) - (__arm64_flags_right_13318000))) == unchecked((uint)0x0UL))))
        {
            goto label_0xCB3C08;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x28UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCB3C04;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x176A768UL /* metadata target: AudioSource.Stop */, x0, x1, x2, x3);
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x88UL))));
        if ((x9 == 0x0UL))
        {
            goto label_0xCB3C04;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCB3790UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x9) + (0xC4UL))))), 0));
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x139UL))))))));
        __arm64_float_flags_left_13318040 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13318040 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCB37B0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCB37A0UL);
        }
        v13 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x40800000UL)), 0)), 0));
        RuntimeCalls.Unsupported("b.gt", 0xCB37A4UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xCB37C4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCB37A8UL);
        }
        v13 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x40000000UL)), 0)), 0));
        goto label_0xCB37C4;
        label_0xCB37B0:
        ;
        v13 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x41000000UL)), 0)), 0));
        RuntimeCalls.Unsupported("b.gt", 0xCB37B4UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xCB37C4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCB37B8UL);
        }
        v13 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x40000000UL)), 0)), 0));
        RuntimeCalls.Unsupported("b.mi", 0xCB37BCUL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xCB37C4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCB37C0UL);
        }
        v13 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x40800000UL)), 0)), 0));
        goto label_0xCB37C4;
        label_0xCB37C4:
        ;
        x10 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0xDCUL))))));
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0xD0UL))))));
        __arm64_flags_left_13318092 = unchecked((uint)(x8));
        __arm64_flags_right_13318092 = unchecked((uint)0x0UL);
        x8 = unchecked((ulong)(((unchecked((uint)((__arm64_flags_left_13318092) - (__arm64_flags_right_13318092))) == unchecked((uint)0x0UL)) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        __arm64_flags_left_13318100 = unchecked((uint)(x10));
        __arm64_flags_right_13318100 = unchecked((uint)(x9));
        x9 = unchecked((ulong)(((unchecked((uint)((__arm64_flags_left_13318100) - (__arm64_flags_right_13318100))) == unchecked((uint)0x0UL)) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        if ((unchecked((uint)(x10)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCB37F0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)(x9)))))));
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCB37F0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x138UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCB37F0;
        label_0xCB37F0:
        ;
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xCB2730UL /* metadata target: PlayerWeapons.UpdateTotalWeapons */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xE8UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCB3C04;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_13318148 = unchecked((uint)(x9));
        __arm64_flags_right_13318148 = unchecked((uint)(x20));
        if (((!((__arm64_flags_left_13318148 >= __arm64_flags_right_13318148))) || (unchecked((uint)((__arm64_flags_left_13318148) - (__arm64_flags_right_13318148))) == unchecked((uint)0x0UL))))
        {
            goto label_0xCB3C08;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)((x23) << (int)(unchecked((int)(0x3UL))))))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCB3C04;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(x22);
        x0 = RuntimeCalls.InvokeDirect(0xE49224UL, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCB3C04;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x25 = 0x1A8C000UL;
        x25 = RuntimeMemory.ReadU64(unchecked((ulong)((x25) + (0xD8UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD8UL))));
        x8 = RuntimeMemory.ReadU64(x25);
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCB3844;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCB3844;
        label_0xCB3844:
        ;
        x0 = x21;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1798274UL /* metadata target: Object.op_Implicit */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCB3B18;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xA8UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCB3C04;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xE8UL))));
        if ((x9 == 0x0UL))
        {
            goto label_0xCB3C04;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x9) + (0x18UL))))));
        __arm64_flags_left_13318248 = unchecked((uint)(x10));
        __arm64_flags_right_13318248 = unchecked((uint)(x20));
        if (((!((__arm64_flags_left_13318248 >= __arm64_flags_right_13318248))) || (unchecked((uint)((__arm64_flags_left_13318248) - (__arm64_flags_right_13318248))) == unchecked((uint)0x0UL))))
        {
            goto label_0xCB3C08;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)((x9) + (unchecked((ulong)((x23) << (int)(unchecked((int)(0x3UL))))))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0x20UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCB3C04;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(x22);
        x21 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x106UL))))))));
        x0 = RuntimeCalls.InvokeDirect(0xE49224UL, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCB3C04;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x23 = 0x1A8C000UL;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD8UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0x1E8UL))));
        x24 = 0x1BAB000UL;
        if ((unchecked((uint)(x21)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCB38B8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x70UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCB3C04;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794C14UL /* metadata target: GameObject.get_transform */, x0, x1, x2, x3);
        if ((x0 != 0x0UL))
        {
            goto label_0xCB38C0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCB38B4UL);
        }
        goto label_0xCB3C04;
        label_0xCB38B8:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x108UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCB3C04;
        }
        else
        {
            goto label_0xCB38C0;
        }
        label_0xCB38C0:
        ;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179D508UL /* metadata target: Transform.get_position */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x70UL))));
        RuntimeMemory.WriteF64(unchecked((ulong)((sp) + (0x30UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((sp) + (0x20UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0)))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCB3C04;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        v8 = v2;
        x0 = RuntimeCalls.InvokeDirect(0x1794C14UL /* metadata target: GameObject.get_transform */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCB3C04;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179D9B8UL /* metadata target: Transform.get_forward */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x24) + (0x32CUL))))))));
        v9 = v2;
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCB3918;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x1E8UL))));
        __arm64_pair_address_13318404 = sp;
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13318404, v1);
#else
        __WriteVector128(__arm64_pair_address_13318404, v1);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13318404) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13318404) + (0x10UL))), v0);
#endif
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        __arm64_pair_address_13318412 = sp;
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(__arm64_pair_address_13318412);
#else
        v1 = __ReadVector128(__arm64_pair_address_13318412);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13318412) + (0x10UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13318412) + (0x10UL))));
#endif
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x24) + (0x32CUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCB3918;
        label_0xCB3918:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x108UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCB3C04;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x23);
        __arm64_pair_address_13318436 = unchecked((ulong)((sp) + (0x20UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v2 = RuntimeMemory.ReadVector128(__arm64_pair_address_13318436);
#else
        v2 = __ReadVector128(__arm64_pair_address_13318436);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v3 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13318436) + (0x10UL))));
#else
        v3 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13318436) + (0x10UL))));
#endif
        v0 = v1;
        RuntimeCalls.Unsupported("fmov", 0xCB392CUL);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        v3 = v2;
        RuntimeCalls.Unsupported("fmul", 0xCB3938UL);
        RuntimeCalls.Unsupported("fadd", 0xCB393CUL);
        v3 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((x8) + (0x18UL))))), 0));
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x20UL))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3E800000UL)), 0)), 0));
        RuntimeCalls.Unsupported("fmov", 0xCB394CUL);
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v5 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0xBE800000UL)), 0)), 0));
        RuntimeCalls.Unsupported("fmul", 0xCB3958UL);
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v5.GetUInt64(0)))), 0))))), 0));
        RuntimeCalls.Unsupported("fadd", 0xCB3964UL);
        x1 = 0x0UL;
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x30UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x30UL))), v0);
#endif
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0))))), 0));
        x0 = RuntimeCalls.InvokeDirect(0x179D6F0UL /* metadata target: Transform.get_rotation */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x25);
        v9 = v0;
        v10 = v1;
        v11 = v2;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        v12 = v3;
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCB3998;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCB3994UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCB3998;
        label_0xCB3998:
        ;
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x9C8UL))));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x30UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((sp) + (0x30UL))));
#endif
        x0 = x20;
        v2 = v8;
        x1 = RuntimeMemory.ReadU64(x8);
        RuntimeCalls.Unsupported("mov", 0xCB39B0UL);
        v3 = v9;
        v4 = v10;
        v5 = v11;
        v6 = v12;
        x0 = RuntimeCalls.InvokeDirect(0xD2A1ACUL, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCB3C04;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x25 = 0x1A8E000UL;
        x25 = RuntimeMemory.ReadU64(unchecked((ulong)((x25) + (0x10UL))));
        x20 = x0;
        x1 = RuntimeMemory.ReadU64(x25);
        x0 = RuntimeCalls.InvokeDirect(0xE49224UL, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x70UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCB3C04;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x21 = x0;
        x0 = x8;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794C14UL /* metadata target: GameObject.get_transform */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCB3C04;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179D9B8UL /* metadata target: Transform.get_forward */, x0, x1, x2, x3);
        if ((x21 == 0x0UL))
        {
            goto label_0xCB3C04;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCB3A08UL);
        }
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v13.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v13.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v13.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = x21;
        x2 = 0x0UL;
        x26 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = RuntimeCalls.InvokeDirect(0x17CF5B8UL /* metadata target: Rigidbody.AddForce */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17901F4UL /* metadata target: Random.get_value */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x1 = RuntimeMemory.ReadU64(x25);
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F000000UL)), 0)), 0));
        __arm64_float_flags_left_13318712 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13318712 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0xC0E00000UL)), 0)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x40E00000UL)), 0)), 0));
        x0 = x20;
        RuntimeCalls.Unsupported("fcsel", 0xCB3A48UL);
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes((__Unsupported<bool>("Unknown IR expression") ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))), 0));
        x0 = RuntimeCalls.InvokeDirect(0xE49224UL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x24) + (0x32CUL))))))));
        x21 = x0;
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCB3A6C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x1E8UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        RuntimeMemory.WriteU8(unchecked((ulong)((x24) + (0x32CUL))), unchecked((byte)(unchecked((uint)(x26)))));
        goto label_0xCB3A6C;
        label_0xCB3A6C:
        ;
        if ((x21 == 0x0UL))
        {
            goto label_0xCB3C04;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x23);
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = x21;
        x2 = 0x0UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x24 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        __arm64_pair_address_13318792 = unchecked((ulong)((x8) + (0x1CUL)));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13318792)), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13318792) + (0x4UL))))), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x18UL))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0))))), 0));
        x0 = RuntimeCalls.InvokeDirect(0x17CF670UL /* metadata target: Rigidbody.AddRelativeTorque */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17901F4UL /* metadata target: Random.get_value */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x1 = RuntimeMemory.ReadU64(x25);
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F000000UL)), 0)), 0));
        __arm64_float_flags_left_13318832 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13318832 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0xC0E00000UL)), 0)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x40E00000UL)), 0)), 0));
        x0 = x20;
        RuntimeCalls.Unsupported("fcsel", 0xCB3AC0UL);
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes((__Unsupported<bool>("Unknown IR expression") ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))), 0));
        x0 = RuntimeCalls.InvokeDirect(0xE49224UL, x0, x1, x2, x3);
        x21 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x3E1UL))))))));
        x20 = x0;
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCB3AE8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x1E8UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x3E1UL))), unchecked((byte)(unchecked((uint)(x24)))));
        goto label_0xCB3AE8;
        label_0xCB3AE8:
        ;
        if ((x20 == 0x0UL))
        {
            goto label_0xCB3C04;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x23);
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = x20;
        x2 = 0x0UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        __arm64_pair_address_13318912 = unchecked((ulong)((x8) + (0x40UL)));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13318912)), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13318912) + (0x4UL))))), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x3CUL))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0))))), 0));
        x0 = RuntimeCalls.InvokeDirect(0x17CF670UL /* metadata target: Rigidbody.AddRelativeTorque */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xCB3B18;
        label_0xCB3B18:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x139UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCB3B68;
        }
        else
        {
            goto label_0xCB3B20;
        }
        label_0xCB3B20:
        ;
        x0 = x19;
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xCB3B28;
        label_0xCB3B28:
        ;
        x2 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x3 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x0 = RuntimeCalls.InvokeDirect(0xCB2694UL /* metadata target: PlayerWeapons.SelectWeapon */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x1 = x0;
        x0 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0xB0UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xB0UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0xA0UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xA0UL)))) + (0x8UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x90UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x90UL)))) + (0x8UL))));
        x26 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x80UL))));
        x25 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x80UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x70UL))));
        __arm64_pair_address_13318992 = unchecked((ulong)((sp) + (0x60UL)));
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13318992)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13318992) + (0x8UL))))), 0));
        __arm64_pair_address_13318996 = unchecked((ulong)((sp) + (0x50UL)));
        v11 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13318996)), 0));
        v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13318996) + (0x8UL))))), 0));
        __arm64_pair_address_13319000 = unchecked((ulong)((sp) + (0x40UL)));
        v13 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13319000)), 0));
        v12 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13319000) + (0x8UL))))), 0));
        x2 = 0x0UL;
        sp = unchecked((ulong)((sp) + (0xC0UL)));
        return RuntimeCalls.InvokeDirect(0x1795D40UL /* metadata target: MonoBehaviour.StartCoroutine */);
        label_0xCB3B68:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0xD8UL))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCB3B98;
        }
        else
        {
            goto label_0xCB3B70;
        }
        label_0xCB3B70:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0xB0UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xB0UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0xA0UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xA0UL)))) + (0x8UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x90UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x90UL)))) + (0x8UL))));
        x26 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x80UL))));
        x25 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x80UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x70UL))));
        __arm64_pair_address_13319044 = unchecked((ulong)((sp) + (0x60UL)));
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13319044)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13319044) + (0x8UL))))), 0));
        __arm64_pair_address_13319048 = unchecked((ulong)((sp) + (0x50UL)));
        v11 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13319048)), 0));
        v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13319048) + (0x8UL))))), 0));
        __arm64_pair_address_13319052 = unchecked((ulong)((sp) + (0x40UL)));
        v13 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13319052)), 0));
        v12 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13319052) + (0x8UL))))), 0));
        sp = unchecked((ulong)((sp) + (0xC0UL)));
        return x0;
        label_0xCB3B98:
        ;
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0xDCUL))))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCB3B70;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((long)(RuntimeMemory.ReadS32(unchecked((ulong)((x19) + (0xD0UL))))))));
        __arm64_flags_left_13319076 = unchecked((uint)(x9));
        __arm64_flags_right_13319076 = unchecked((uint)(x8));
        if ((unchecked((uint)((__arm64_flags_left_13319076) - (__arm64_flags_right_13319076))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCB3B70;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xE8UL))));
        if ((x9 == 0x0UL))
        {
            goto label_0xCB3C04;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x9) + (0x18UL))))));
        __arm64_flags_left_13319096 = unchecked((uint)(x8));
        __arm64_flags_right_13319096 = unchecked((uint)(x10));
        if ((__arm64_flags_left_13319096 >= __arm64_flags_right_13319096))
        {
            goto label_0xCB3C08;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)((x9) + (unchecked((ulong)((x8) << (int)(unchecked((int)(0x3UL))))))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCB3C04;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(x22);
        x0 = RuntimeCalls.InvokeDirect(0xE49224UL, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCB3C04;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x120UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCB3B20;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x90UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCB3C04;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCB3BE8UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x20CUL))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        __arm64_float_flags_left_13319152 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13319152 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_13319152 <= __arm64_float_flags_right_13319152) || ((__arm64_float_flags_left_13319152 != __arm64_float_flags_left_13319152) || (__arm64_float_flags_right_13319152 != __arm64_float_flags_right_13319152))))
        {
            goto label_0xCB3B20;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0xD0UL))))));
        x0 = x19;
        goto label_0xCB3B28;
        label_0xCB3C04:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, unchecked((ulong)(unchecked((uint)(x3)))));
        goto label_0xCB3C08;
        label_0xCB3C08:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB7CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, unchecked((ulong)(unchecked((uint)(x3)))));
        return default(ulong);
    }
```

## `PlayerWeapons.LateUpdate` — RVA `0xcb3c0c`

- Lift status: **exact**; input span: 104 bytes; span to next metadata RVA: 104 bytes.
- Metadata signature: `private void LateUpdate() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=14 (informational only).

```csharp
public static ulong PlayerWeapons_LateUpdate_RVAcb3c0c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_pair_address_13319180 = default(ulong);
        ulong __arm64_pair_address_13319272 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        RuntimeVector128 v9 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        __arm64_pair_address_13319180 = unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13319180, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13319180) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        sp = __arm64_pair_address_13319180;
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        x19 = x0;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x108UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCB3C70;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179D508UL /* metadata target: Transform.get_position */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x108UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCB3C70;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        v8 = v0;
        x0 = RuntimeCalls.InvokeDirect(0x179D508UL /* metadata target: Transform.get_position */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x108UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCB3C70;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        v9 = v1;
        x0 = RuntimeCalls.InvokeDirect(0x179D508UL /* metadata target: Transform.get_position */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x100UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCB3C70;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        v0 = v8;
        v1 = v9;
        x1 = 0x0UL;
        __arm64_pair_address_13319272 = sp;
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13319272)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13319272) + (0x8UL))))), 0));
        sp = unchecked((ulong)((__arm64_pair_address_13319272) + (0x20UL)));
        return RuntimeCalls.InvokeDirect(0x179D5A8UL /* metadata target: Transform.set_position */);
        label_0xCB3C70:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `PlayerWeapons.SniperCallAnim` — RVA `0xcb3cc4`

- Lift status: **exact**; input span: 44 bytes; span to next metadata RVA: 44 bytes.
- Metadata signature: `public void SniperCallAnim() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=8 (informational only).

```csharp
public static ulong PlayerWeapons_SniperCallAnim_RVAcb3cc4(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x8UL))), x19);
        x1 = unchecked((ulong)(unchecked((uint)(0xBUL))));
        x2 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x3 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x19 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xCB2694UL /* metadata target: PlayerWeapons.SelectWeapon */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x1 = x0;
        x0 = x19;
        x2 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeDirect(0x1795D40UL /* metadata target: MonoBehaviour.StartCoroutine */);
        return default(ulong);
    }
```

## `PlayerWeapons.GiveAllWeaponsAndAmmo` — RVA `0xcb3cf0`

- Lift status: **partial**; input span: 92 bytes; span to next metadata RVA: 92 bytes.
- Metadata signature: `public void GiveAllWeaponsAndAmmo() { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=9 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'b.ne' at 0xcb3d38; reason: Unknown IR expression at 0xcb3d38

```csharp
public static ulong PlayerWeapons_GiveAllWeaponsAndAmmo_RVAcb3cf0(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13319424 = default(uint);
        uint __arm64_flags_left_13319440 = default(uint);
        uint __arm64_flags_left_13319468 = default(uint);
        uint __arm64_flags_right_13319424 = default(uint);
        uint __arm64_flags_right_13319440 = default(uint);
        uint __arm64_flags_right_13319468 = default(uint);
        ulong sp = default(ulong);
        ulong x10 = default(ulong);
        ulong x11 = default(ulong);
        ulong x12 = default(ulong);
        ulong x13 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL))), x30);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xF0UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCB3D48;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_13319424 = unchecked((uint)(x9));
        __arm64_flags_right_13319424 = unchecked((uint)0x1UL);
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13319424) - (__arm64_flags_right_13319424))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_13319424)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13319424)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13319424) - (__arm64_flags_right_13319424))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13319424)) < unchecked((int)0x0UL))))))
        {
            goto label_0xCB3D3C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x11 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        goto label_0xCB3D10;
        label_0xCB3D10:
        ;
        __arm64_flags_left_13319440 = unchecked((uint)(x9));
        __arm64_flags_right_13319440 = unchecked((uint)(x10));
        if ((unchecked((uint)((__arm64_flags_left_13319440) - (__arm64_flags_right_13319440))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCB3D44;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x12 = unchecked((ulong)((x8) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x10))) << (int)(unchecked((int)(unchecked((uint)(0x3UL))))))))))));
        x12 = RuntimeMemory.ReadU64(unchecked((ulong)((x12) + (0x20UL))));
        if ((x12 == 0x0UL))
        {
            goto label_0xCB3D48;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x13 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x12) + (0x138UL))))));
        x10 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x10))) + (unchecked((uint)(0x1UL)))))));
        __arm64_flags_left_13319468 = unchecked((uint)(x9));
        __arm64_flags_right_13319468 = unchecked((uint)(x10));
        RuntimeMemory.WriteU8(unchecked((ulong)((x12) + (0x120UL))), unchecked((byte)(unchecked((uint)(x11)))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x12) + (0x128UL))), unchecked((uint)(x13)));
        RuntimeCalls.Unsupported("b.ne", 0xCB3D38UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xCB3D10;
        }
        else
        {
            goto label_0xCB3D3C;
        }
        label_0xCB3D3C:
        ;
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        label_0xCB3D44:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB7CUL, x0, x1, x2, x3);
        goto label_0xCB3D48;
        label_0xCB3D48:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `PlayerWeapons.HaveWeaponfalse` — RVA `0xcb3d4c`

- Lift status: **exact**; input span: 32 bytes; span to next metadata RVA: 32 bytes.
- Metadata signature: `public void HaveWeaponfalse() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=4 (informational only).

```csharp
public static ulong PlayerWeapons_HaveWeaponfalse_RVAcb3d4c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x30 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL))), x30);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x40UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCB3D68;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x2 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0x1794CD0UL /* metadata target: GameObject.SetActive */);
        label_0xCB3D68:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        return default(ulong);
    }
```

## `PlayerWeapons.ctor` — RVA `0xcb3d6c`

- Lift status: **exact**; input span: 44 bytes; span to next metadata RVA: 44 bytes.
- Metadata signature: `public void .ctor() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=5 (informational only).

```csharp
public static ulong PlayerWeapons_ctor_RVAcb3d6c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        x8 = 0x432000UL;
        x9 = 0x431000UL;
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((x8) + (0x210UL))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((x9) + (0xEB0UL))))), 0));
        x8 = unchecked((ulong)(unchecked((uint)(0xCCCDUL))));
        x8 = unchecked((ulong)(unchecked((uint)(unchecked((ulong)((unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((~(0xFFFFUL)))))))))) | (unchecked((ulong)((unchecked((ulong)((0x3E4CUL) << (int)(unchecked((int)(0x10UL)))))) << (int)(unchecked((int)(0x0UL))))))))))));
        x1 = 0x0UL;
        RuntimeMemory.WriteF64(unchecked((ulong)((x0) + (0xCCUL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((x0) + (0x188UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0)))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x0) + (0x190UL))), unchecked((uint)(x8)));
        return RuntimeCalls.InvokeDirect(0x1796274UL /* metadata target: MonoBehaviour.ctor */);
        return default(ulong);
    }
```
