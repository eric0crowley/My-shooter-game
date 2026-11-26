# Native pseudocode: bl_RawImageOffset

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `bl_RawImageOffset.Awake` — RVA `0xce8af4`

- Decompiled symbol: `bl_RawImageOffset_Awake`
- Metadata signature: `private void Awake() { }`
- Native interval: `88` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[40];
    long long field_28;
} struct_0;

extern long long g_1efd058;
extern char g_1fab675;

void bl_RawImageOffset_Awake(struct_0 *ptr)
{
    unsigned long long v4;  // x30
    unsigned long long v5;  // x21
    unsigned long long v6;  // x20
    unsigned long long v7;  // x19
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x18]
    unsigned long long v2;  // [bp-0x10]
    unsigned long long v3;  // [bp-0x8]

    v0 = v4;
    v1 = v5;
    v2 = v6;
    v3 = v7;
    if (!(g_1fab675 & 1))
    {
        sub_f7d92c(&g_1efd058);
        g_1fab675 = 1;
    }
    ptr->field_28 = sub_1231bc8(ptr, g_1efd058);
    sub_f7d8d0();
    return;
}
```

## `bl_RawImageOffset.Update` — RVA `0xce8b4c`

- Decompiled symbol: `bl_RawImageOffset_Update`
- Metadata signature: `private void Update() { }`
- Native interval: `60` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[40];
    struct struct_1 *field_28;
    unsigned long long field_30;
    unsigned int field_38;
    unsigned int field_3c;
} struct_0;

typedef struct struct_1 {
    char padding_0[232];
    unsigned int field_e8;
    unsigned int field_ec;
} struct_1;

void bl_RawImageOffset_Update(struct_0 *ptr)
{
    unsigned long long v1;  // x30
    unsigned int p[60];  // x0
    unsigned int v3;  // s3
    unsigned long v4;  // d0
    unsigned long long v0;  // [bp-0x10]

    v0 = v1;
    p = ptr->field_28;
    if (!p)
        sub_f7db74(0);
    v3 = p[59];
    v4 = [D] unsupported_Iop_ZeroHI64ofV128();
    ptr->field_38 = p[58];
    ptr->field_3c = v3;
    ptr->field_30 = v4;
}
```

## `bl_RawImageOffset.ctor` — RVA `0xce8b88`

- Decompiled symbol: `bl_RawImageOffset_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `20` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[32];
    unsigned long long field_20;
} struct_0;

long long bl_RawImageOffset_ctor(struct_0 *ptr)
{
    long long v0;  // x0

    ptr->field_20 = 0x3f80000000000000;
    v0 = MonoBehaviour__ctor();
    return MonoBehaviour__ctor();
}
```
