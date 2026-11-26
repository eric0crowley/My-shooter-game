# Native pseudocode: bl_MMItemInfo

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `bl_MMItemInfo.ctor` — RVA `0xccaa18`

- Decompiled symbol: `bl_MMItemInfo_ctor`
- Metadata signature: `public void .ctor(Vector3 position) { }`
- Native interval: `92` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
    unsigned int field_14;
    unsigned int field_18;
    char padding_1c[12];
    uint128_t field_28;
    unsigned int field_38;
    char padding_3c[12];
    unsigned int field_48;
} struct_0;

void bl_MMItemInfo_ctor(struct_0 *ptr)
{
    unsigned int v0;  // s0
    unsigned int v1;  // s1
    unsigned int v2;  // s2

    *((unsigned int *)((char *)&ptr->field_28 + 8)) = 1064514355;
    *((uint128_t *)&(&ptr->padding_1c)[1]) = 0x3f8000003f8000003f80000041400000;
    *((unsigned int *)&ptr->padding_3c[4]) = 1;
    Object__ctor();
    ptr->field_10 = v0;
    ptr->field_14 = v1;
    ptr->field_18 = v2;
    return;
}
```

## `bl_MMItemInfo.ctor` — RVA `0xccaa74`

- Decompiled symbol: `bl_MMItemInfo_ctor`
- Metadata signature: `public void .ctor(Transform target) { }`
- Native interval: `80` bytes
- Result: `pseudocode`
- Heuristic layout hint: `bl_MMItemInfo_Recovered` matched 3 offsets against `bl_MMItemInfo` metadata (confidence 0.75).

```c
typedef struct bl_MMItemInfo_Recovered {
    char padding_0[32];
    unsigned long long Target;
    uint128_t Size;
    unsigned int field_38;
    char padding_3c[12];
    unsigned int Effect;
} bl_MMItemInfo_Recovered;

void bl_MMItemInfo_ctor(struct_0 *ptr, unsigned long a1)
{
    unsigned long long v3;  // x30
    unsigned long long v4;  // x20
    unsigned long long v5;  // x19
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x10]
    unsigned long long v2;  // [bp-0x8]

    v0 = v3;
    v1 = v4;
    v2 = v5;
    *((unsigned int *)((char *)&ptr->field_28 + 8)) = 1064514355;
    *((uint128_t *)&(&ptr->field_20)[1]) = 0x3f8000003f8000003f80000041400000;
    *((unsigned int *)&ptr->padding_3c[4]) = 1;
    Object__ctor();
    ptr->field_20 = a1;
    sub_f7d8d0();
    return;
}
```
