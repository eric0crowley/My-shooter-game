# Native pseudocode: Cam_Follow_Player

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `Cam_Follow_Player.LateUpdate` — RVA `0xc7a0a8`

- Decompiled symbol: `Cam_Follow_Player_LateUpdate`
- Metadata signature: `private void LateUpdate() { }`
- Native interval: `176` bytes
- Result: `pseudocode`

```c
void Cam_Follow_Player_LateUpdate(unsigned long long *ptr)
{
    unsigned long long v5;  // d9
    unsigned long long v6;  // d8
    unsigned long long v7;  // x30
    unsigned long long v8;  // x20
    unsigned long long v9;  // x19
    unsigned long v10;  // x0
    unsigned long long v0;  // [bp-0x30]
    unsigned long long v1;  // [bp-0x28]
    unsigned long long v2;  // [bp-0x20]
    unsigned long long v3;  // [bp-0x10]
    unsigned long long v4;  // [bp-0x8]

    v0 = v5;
    v1 = v6;
    v2 = v7;
    v3 = v8;
    v4 = v9;
    v10 = ptr[5];
    if (v10)
    {
        Transform__get_position(v10, 0);
        v10 = ptr[4];
        if (v10)
        {
            Transform__get_position(v10, 0);
            v10 = ptr[5];
            if (v10)
            {
                v10 = Transform__get_position(v10, 0);
                if (ptr[4])
                {
                    Transform__set_position(ptr[4], 0);
                    v10 = ptr[5];
                    if (v10)
                    {
                        Transform__get_rotation(v10, 0);
                        v10 = ptr[5];
                        if (v10)
                        {
                            Transform__get_eulerAngles(v10, 0);
                            Quaternion__Internal_FromEulerRad();
                            return;
                        }
                    }
                }
            }
        }
    }
    sub_f7db74(v10);
}
```

## `Cam_Follow_Player.ctor` — RVA `0xc7a158`

- Decompiled symbol: `Cam_Follow_Player_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long Cam_Follow_Player_ctor(void)
{
    long long v0;  // x0

    v0 = MonoBehaviour__ctor();
    return MonoBehaviour__ctor();
}
```
