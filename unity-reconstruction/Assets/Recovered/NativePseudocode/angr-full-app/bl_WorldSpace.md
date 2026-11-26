# Native pseudocode: bl_WorldSpace

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `bl_WorldSpace.OnDrawGizmosSelected` — RVA `0xcca2d0`

- Decompiled symbol: `bl_WorldSpace_OnDrawGizmosSelected`
- Metadata signature: `private void OnDrawGizmosSelected() { }`
- Native interval: `232` bytes
- Result: `pseudocode`

```c
extern long long g_1efd060;
extern char g_1fab571;

void bl_WorldSpace_OnDrawGizmosSelected(long long a0)
{
    unsigned long long v9;  // d12
    unsigned long long v10;  // d11
    unsigned long long v11;  // d10
    unsigned long long v12;  // d9
    unsigned long long v13;  // d8
    unsigned long long v14;  // x30
    unsigned long long v15;  // x21
    unsigned long long v16;  // x20
    unsigned long long v17;  // x19
    long long v18;  // x0
    unsigned long long v0;  // [bp-0x50]
    unsigned long long v1;  // [bp-0x40]
    unsigned long long v2;  // [bp-0x38]
    unsigned long long v3;  // [bp-0x30]
    unsigned long long v4;  // [bp-0x28]
    unsigned long long v5;  // [bp-0x20]
    unsigned long long v6;  // [bp-0x18]
    unsigned long long v7;  // [bp-0x10]
    unsigned long long v8;  // [bp-0x8]

    v0 = v9;
    v1 = v10;
    v2 = v11;
    v3 = v12;
    v4 = v13;
    v5 = v14;
    v6 = v15;
    v7 = v16;
    v8 = v17;
    if (!(g_1fab571 & 1))
    {
        sub_f7d92c(&g_1efd060);
        g_1fab571 = 1;
    }
    v18 = sub_1231bc8(a0, g_1efd060);
    if (!v18)
        sub_f7db74();
    RectTransform__get_sizeDelta();
    Transform__get_localPosition(v18, 0);
    Gizmos__set_color(0);
    Gizmos__DrawCube(0);
}
```

## `bl_WorldSpace.ctor` — RVA `0xcca3b8`

- Decompiled symbol: `bl_WorldSpace_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `20` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[32];
    uint128_t field_20;
} struct_0;

long long bl_WorldSpace_ctor(struct_0 *ptr)
{
    long long v0;  // x0

    ptr->field_20 = 0x3f4000003f8000003f8000003f800000;
    v0 = MonoBehaviour__ctor();
    return MonoBehaviour__ctor();
}
```
