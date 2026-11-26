# Native pseudocode: VignetteModel

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `VignetteModel.get_settings` — RVA `0xcdc1ac`

- Decompiled symbol: `VignetteModel_get_settings`
- Metadata signature: `public VignetteModel.Settings get_settings() { }`
- Native interval: `32` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    uint128_t field_18;
    uint128_t field_28;
    uint128_t field_38;
    unsigned long long field_48;
} struct_0;

typedef struct struct_1 {
    uint128_t field_0;
    uint128_t field_10;
    uint128_t field_20;
    unsigned long long field_30;
} struct_1;

struct_0 * VignetteModel_get_settings(struct_0 *p)
{
    uint128_t v0;  // q0
    uint128_t v1;  // q1
    uint128_t v2;  // q2
    struct_1 *ptr;  // x8

    v0 = *((int128_t *)((char *)&p->field_28 + 8));
    v1 = *((int128_t *)((char *)&p->field_18 + 8));
    v2 = *((int128_t *)&(&p->padding_0)[1]);
    ptr->field_30 = *((long long *)((char *)&p->field_38 + 8));
    ptr->field_10 = v1;
    ptr->field_20 = v0;
    ptr->field_0 = v2;
    return p;
}
```

## `VignetteModel.set_settings` — RVA `0xcdc1cc`

- Decompiled symbol: `VignetteModel_set_settings`
- Metadata signature: `public void set_settings(VignetteModel.Settings value) { }`
- Native interval: `44` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    uint128_t field_0;
    uint128_t field_10;
    uint128_t field_20;
    unsigned long long field_30;
} struct_0;

typedef struct struct_1 {
    char padding_0[24];
    uint128_t field_18;
    uint128_t field_28;
    uint128_t field_38;
    unsigned long long field_48;
} struct_1;

long long VignetteModel_set_settings(struct_1 *ptr, struct_0 *p)
{
    uint128_t v0;  // q2
    unsigned long long v1;  // x9
    uint128_t v2;  // q1
    long long v3;  // x0

    v0 = p->field_10;
    v1 = p->field_30;
    v2 = p->field_0;
    *((uint128_t *)((char *)&ptr->field_28 + 8)) = p->field_20;
    *((unsigned long long *)((char *)&ptr->field_38 + 8)) = v1;
    *((uint128_t *)((char *)&ptr->field_18 + 8)) = v0;
    *((uint128_t *)&(&ptr->padding_0)[1]) = v2;
    v3 = sub_f7d8d0();
    return sub_f7d8d0();
}
```

## `VignetteModel.Reset` — RVA `0xcdc1f8`

- Decompiled symbol: `VignetteModel_Reset`
- Metadata signature: `public override void Reset() { }`
- Native interval: `156` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[40];
    uint128_t field_28;
    uint128_t field_38;
    unsigned long long field_48;
} struct_0;

long long VignetteModel_Reset(struct_0 *ptr)
{
    unsigned long v8;  // x0
    uint128_t v0;  // [bp-0xa0]
    int v1;  // [bp-0x90]
    int v2;  // [bp-0x80]
    unsigned long long v3;  // [bp-0x70]
    uint128_t choice;  // [bp-0x60]
    int v5;  // [bp-0x50], Other Possible Types: uint128_t
    uint128_t flag;  // [bp-0x40]
    unsigned long v7;  // [bp-0x30], Other Possible Types: unsigned long long

    v5 = 0;
    flag = 0;
    choice = 0;
    v5 = (int)_INSERT(v5 CONCAT 0, 4, 0x3f0000003f000000);
    *((unsigned int *)&v5) = 0x3f800000;
    *((unsigned int *)&(&v5)[20]) = 0x3f800000;
    *((unsigned long long *)&(&v5)[12]) = 4489188110477190758;
    *((unsigned long long *)&(&v5)[24]) = 0;
    v7 = 0;
    sub_f7d8d0(&v5 - 24, 0);
    *((unsigned int *)&v7) = 0x3f800000;
    *((char *)&v7 + 4) = 0;
    v1 = (int)*((uint128_t *)&v5);
    v2 = (int)*((uint128_t *)(&v5 + 16));
    v0 = choice;
    v3 = v7;
    *((unsigned long long *)((char *)&ptr->field_38 + 8)) = v7;
    *((void*)((char *)&ptr->field_28 + 8)) = v2;
    *((void*)&(&ptr->padding_0)[1]) = v1;
    *((uint128_t *)&ptr->padding_0[24]) = choice;
    v8 = sub_f7d8d0((struct struct_0 *)&ptr->field_38, 0);
    return sub_f7d8d0((struct struct_0 *)&ptr->field_38, 0);
}
```

## `VignetteModel.ctor` — RVA `0xcdc314`

- Decompiled symbol: `VignetteModel_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `168` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[40];
    uint128_t field_28;
    uint128_t field_38;
    unsigned long long field_48;
} struct_0;

long long VignetteModel_ctor(struct_0 *ptr)
{
    unsigned long long v11;  // x30
    unsigned long long v12;  // x20
    unsigned long long v13;  // x19
    uint128_t v0;  // [bp-0xa0]
    int v1;  // [bp-0x90]
    int v2;  // [bp-0x80]
    unsigned long long v3;  // [bp-0x70]
    uint128_t choice;  // [bp-0x60]
    int v5;  // [bp-0x50], Other Possible Types: uint128_t
    uint128_t flag;  // [bp-0x40]
    unsigned long v7;  // [bp-0x30], Other Possible Types: unsigned long long
    unsigned long long v8;  // [bp-0x20]
    unsigned long long v9;  // [bp-0x10]
    unsigned long long v10;  // [bp-0x8]

    v8 = v11;
    v9 = v12;
    v10 = v13;
    v5 = 0;
    flag = 0;
    choice = 0;
    v5 = (int)_INSERT(v5 CONCAT 0, 4, 0x3f0000003f000000);
    *((unsigned int *)&v5) = 0x3f800000;
    *((unsigned int *)&(&v5)[20]) = 0x3f800000;
    *((unsigned long long *)&(&v5)[12]) = 4489188110477190758;
    *((unsigned long long *)&(&v5)[24]) = 0;
    v7 = 0;
    sub_f7d8d0(&v5 - 24, 0);
    *((unsigned int *)&v7) = 0x3f800000;
    *((char *)&v7 + 4) = 0;
    v1 = (int)*((uint128_t *)&v5);
    v2 = (int)*((uint128_t *)(&v5 + 16));
    v0 = choice;
    v3 = v7;
    *((unsigned long long *)((char *)&ptr->field_38 + 8)) = v7;
    *((void*)((char *)&ptr->field_28 + 8)) = v2;
    *((void*)&(&ptr->padding_0)[1]) = v1;
    *((uint128_t *)&ptr->padding_0[24]) = choice;
    sub_f7d8d0((struct struct_0 *)&ptr->field_38, 0);
    PostProcessingModel__ctor(ptr, 0); /* do not return */
}
```
