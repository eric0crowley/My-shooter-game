# Native pseudocode: ScreenSpaceReflectionModel

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `ScreenSpaceReflectionModel.get_settings` — RVA `0xcdbf8c`

- Decompiled symbol: `ScreenSpaceReflectionModel_get_settings`
- Metadata signature: `public ScreenSpaceReflectionModel.Settings get_settings() { }`
- Native interval: `32` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[20];
    uint128_t field_14;
    uint128_t field_24;
    uint128_t field_34;
    unsigned int field_44;
} struct_0;

typedef struct struct_1 {
    uint128_t field_0;
    uint128_t field_10;
    uint128_t field_20;
    unsigned int field_30;
} struct_1;

struct_0 * ScreenSpaceReflectionModel_get_settings(struct_0 *p)
{
    uint128_t v0;  // q0
    uint128_t v1;  // q1
    uint128_t v2;  // q2
    struct_1 *ptr;  // x8

    v0 = *((int128_t *)((char *)&p->field_24 + 4));
    v1 = *((int128_t *)((char *)&p->field_14 + 4));
    v2 = *((int128_t *)&(&p->padding_0)[1]);
    ptr->field_30 = *((int *)((char *)&p->field_34 + 4));
    ptr->field_10 = v1;
    ptr->field_20 = v0;
    ptr->field_0 = v2;
    return p;
}
```

## `ScreenSpaceReflectionModel.set_settings` — RVA `0xcdbfac`

- Decompiled symbol: `ScreenSpaceReflectionModel_set_settings`
- Metadata signature: `public void set_settings(ScreenSpaceReflectionModel.Settings value) { }`
- Native interval: `32` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[20];
    uint128_t field_14;
    uint128_t field_24;
    uint128_t field_34;
    unsigned int field_44;
} struct_1;

typedef struct struct_0 {
    uint128_t field_0;
    uint128_t field_10;
    uint128_t field_20;
    unsigned int field_30;
} struct_0;

struct_1 * ScreenSpaceReflectionModel_set_settings(struct_1 *ptr, struct_0 *p)
{
    uint128_t v0;  // q1
    uint128_t v1;  // q0
    uint128_t v2;  // q2

    v0 = p->field_10;
    v1 = p->field_20;
    v2 = p->field_0;
    *((unsigned int *)((char *)&ptr->field_34 + 4)) = p->field_30;
    *((uint128_t *)((char *)&ptr->field_24 + 4)) = v1;
    *((uint128_t *)((char *)&ptr->field_14 + 4)) = v0;
    *((uint128_t *)&(&ptr->padding_0)[1]) = v2;
    return ptr;
}
```

## `ScreenSpaceReflectionModel.Reset` — RVA `0xcdbfcc`

- Decompiled symbol: `ScreenSpaceReflectionModel_Reset`
- Metadata signature: `public override void Reset() { }`
- Native interval: `80` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[20];
    unsigned long long field_14;
    unsigned int field_1c;
    unsigned long long field_20;
    unsigned long long field_28;
    char field_30;
    unsigned short field_31;
    char field_33;
    uint128_t field_34;
    unsigned int field_44;
} struct_0;

struct_0 * ScreenSpaceReflectionModel_Reset(struct_0 *ptr)
{
    *((unsigned long long *)&(&ptr->padding_0)[1]) = 0x200000000;
    *((unsigned int *)((char *)&ptr->field_14 + 4)) = 0x42c80000;
    *((unsigned long long *)&ptr->field_1c) = 0x300000100;
    ptr->field_20 = 0x3f8000003f000000;
    *((char *)&ptr->field_28) = 0;
    *((unsigned short *)((char *)&ptr->field_28 + 1)) = 0;
    *((char *)&ptr->field_28 + 3) = 0;
    *((uint128_t *)((char *)&ptr->field_28 + 4)) = 0x3f8000003f80000042c800003f800000;
    *((unsigned int *)((char *)&ptr->field_34 + 4)) = 1022739087;
    return ptr;
}
```

## `ScreenSpaceReflectionModel.ctor` — RVA `0xcdc070`

- Decompiled symbol: `ScreenSpaceReflectionModel_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `84` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[20];
    unsigned long long field_14;
    unsigned int field_1c;
    unsigned long long field_20;
    unsigned long long field_28;
    char field_30;
    unsigned short field_31;
    char field_33;
    uint128_t field_34;
    unsigned int field_44;
} struct_0;

long long ScreenSpaceReflectionModel_ctor(struct_0 *ptr)
{
    *((unsigned long long *)&(&ptr->padding_0)[1]) = 0x200000000;
    *((unsigned int *)((char *)&ptr->field_14 + 4)) = 0x42c80000;
    *((unsigned long long *)&ptr->field_1c) = 0x300000100;
    ptr->field_20 = 0x3f8000003f000000;
    *((char *)&ptr->field_28) = 0;
    *((unsigned short *)((char *)&ptr->field_28 + 1)) = 0;
    *((char *)&ptr->field_28 + 3) = 0;
    *((uint128_t *)((char *)&ptr->field_28 + 4)) = 0x3f8000003f80000042c800003f800000;
    *((unsigned int *)((char *)&ptr->field_34 + 4)) = 1022739087;
    PostProcessingModel__ctor(); /* do not return */
}
```
