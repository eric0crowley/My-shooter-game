# Native pseudocode: WaterMove

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `WaterMove.Start` — RVA `0xcc4ab4`

- Decompiled symbol: `WaterMove_Start`
- Metadata signature: `private void Start() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long WaterMove_Start(void)
{
    unsigned long v0;  // x0

    return v0;
}
```

## `WaterMove.Update` — RVA `0xcc4ab8`

- Decompiled symbol: `WaterMove_Update`
- Metadata signature: `private void Update() { }`
- Native interval: `156` bytes
- Result: `pseudocode`

```c
extern long long g_1efd070;
extern char g_1fab537;

void WaterMove_Update(long long a0)
{
    unsigned long long v8;  // d11
    unsigned long long v9;  // d10
    unsigned long long v10;  // d9
    unsigned long long v11;  // d8
    unsigned long long v12;  // x30
    unsigned long long v13;  // x21
    unsigned long long v14;  // x20
    unsigned long long v15;  // x19
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
    if (!(g_1fab537 & 1))
    {
        sub_f7d92c(&g_1efd070);
        g_1fab537 = 1;
    }
    Time__get_time(0);
    Time__get_time(0);
    if (sub_1231bc8(a0, g_1efd070) && Renderer__get_material())
    {
        Material__set_mainTextureOffset();
        return;
    }
    sub_f7db74();
}
```

## `WaterMove.ctor` — RVA `0xcc4b54`

- Decompiled symbol: `WaterMove_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `24` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[32];
    unsigned long long field_20;
} struct_0;

long long WaterMove_ctor(struct_0 *ptr)
{
    long long v0;  // x0

    ptr->field_20 = 4489188110467124429;
    v0 = MonoBehaviour__ctor();
    return MonoBehaviour__ctor();
}
```
