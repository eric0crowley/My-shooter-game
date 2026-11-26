# Native pseudocode: walkShoot

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `walkShoot.Start` — RVA `0xc72688`

- Decompiled symbol: `walkShoot_Start`
- Metadata signature: `private void Start() { }`
- Native interval: `52` bytes
- Result: `pseudocode`
- Heuristic layout hint: `walkShoot_Recovered` matched 2 offsets against `walkShoot` metadata (confidence 1.00).

```c
typedef struct walkShoot_Recovered {
    char padding_0[56];
    long long anim;
    unsigned long long chest;
} walkShoot_Recovered;

void walkShoot_Start(struct_0 *ptr)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    if (ptr->field_38)
    {
        ptr->field_40 = Animator__GetBoneTransform(ptr->field_38, 7, 0);
        sub_f7d8d0();
        return;
    }
    sub_f7db74(0);
}
```

## `walkShoot.LateUpdate` — RVA `0xc726bc`

- Decompiled symbol: `walkShoot_LateUpdate`
- Metadata signature: `private void LateUpdate() { }`
- Native interval: `272` bytes
- Result: `pseudocode`

```c
void walkShoot_LateUpdate(long long *ptr)
{
    unsigned long long v7;  // d11
    unsigned long long v8;  // d10
    unsigned long long v9;  // d9
    unsigned long long v10;  // d8
    unsigned long long v11;  // x30
    unsigned long long v12;  // x20
    unsigned long long v13;  // x19
    long long v14;  // x0
    unsigned long long v0;  // [bp-0x40]
    unsigned long long v1;  // [bp-0x38]
    unsigned long long v2;  // [bp-0x30]
    unsigned long long v3;  // [bp-0x28]
    unsigned long long v4;  // [bp-0x20]
    unsigned long long v5;  // [bp-0x10]
    unsigned long long v6;  // [bp-0x8]

    v0 = v7;
    v1 = v8;
    v2 = v9;
    v3 = v10;
    v4 = v11;
    v5 = v12;
    v6 = v13;
    v14 = ptr[4];
    if (v14)
    {
        v14 = Transform__get_position(v14, 0);
        if (ptr[8])
        {
            v14 = Transform__LookAt(ptr[8], 0);
            if (ptr[8])
            {
                Transform__get_rotation(ptr[8], 0);
                Quaternion__Internal_FromEulerRad(0);
                Transform__set_rotation();
                return;
            }
        }
    }
    sub_f7db74(v14);
}
```

## `walkShoot.ctor` — RVA `0xc727cc`

- Decompiled symbol: `walkShoot_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long walkShoot_ctor(void)
{
}
```
