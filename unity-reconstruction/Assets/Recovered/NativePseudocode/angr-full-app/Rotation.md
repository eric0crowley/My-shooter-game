# Native pseudocode: Rotation

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `Rotation.Start` — RVA `0xcbf984`

- Decompiled symbol: `Rotation_Start`
- Metadata signature: `private void Start() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long Rotation_Start(void)
{
    unsigned long v0;  // x0

    return v0;
}
```

## `Rotation.Update` — RVA `0xcbf988`

- Decompiled symbol: `Rotation_Update`
- Metadata signature: `private void Update() { }`
- Native interval: `136` bytes
- Result: `pseudocode`

```c
void Rotation_Update(unsigned long a0)
{
    unsigned long long v8;  // d12
    unsigned long long v9;  // d11
    unsigned long long v10;  // d10
    unsigned long long v11;  // d9
    unsigned long long v12;  // d8
    unsigned long long v13;  // x30
    unsigned long long v14;  // x20
    unsigned long long v15;  // x19
    long long v16;  // x0
    unsigned long long v0;  // [bp-0x40]
    unsigned long long v1;  // [bp-0x38]
    unsigned long long v2;  // [bp-0x30]
    unsigned long long v3;  // [bp-0x28]
    unsigned long long v4;  // [bp-0x20]
    unsigned long long v5;  // [bp-0x18]
    unsigned long long v6;  // [bp-0x10]
    unsigned long long v7;  // [bp-0x8]

    v0 = v8;
    v1 = v9;
    v2 = v10;
    v3 = v11;
    v4 = v12;
    v5 = v13;
    v6 = v14;
    v7 = v15;
    v16 = Component__get_transform();
    Time__get_deltaTime(0);
    Time__get_deltaTime(0);
    Time__get_deltaTime(0);
    if (!v16)
        sub_f7db74();
}
```

## `Rotation.ctor` — RVA `0xcbfa10`

- Decompiled symbol: `Rotation_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long Rotation_ctor(void)
{
    long long v0;  // x0

    v0 = MonoBehaviour__ctor();
    return MonoBehaviour__ctor();
}
```
