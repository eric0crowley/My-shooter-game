# Native pseudocode: EyeAdaptationModel

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `EyeAdaptationModel.get_settings` — RVA `0xcdbda8`

- Decompiled symbol: `EyeAdaptationModel_get_settings`
- Metadata signature: `public EyeAdaptationModel.Settings get_settings() { }`
- Native interval: `24` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[20];
    uint128_t field_14;
    uint128_t field_24;
    char field_30;
} struct_0;

typedef struct struct_1 {
    uint128_t field_0;
    uint128_t field_10;
    char field_1c;
} struct_1;

struct_0 * EyeAdaptationModel_get_settings(struct_0 *p)
{
    uint128_t v0;  // q1
    uint128_t v1;  // q2
    struct_1 *ptr;  // x8

    v0 = *((int128_t *)((char *)&p->field_14 + 4));
    v1 = *((int128_t *)&(&p->padding_0)[1]);
    *((uint128_t *)((char *)&ptr->field_10 + 12)) = p->field_24;
    ptr->field_0 = v1;
    ptr->field_10 = v0;
    return p;
}
```

## `EyeAdaptationModel.set_settings` — RVA `0xcdbdc0`

- Decompiled symbol: `EyeAdaptationModel_set_settings`
- Metadata signature: `public void set_settings(EyeAdaptationModel.Settings value) { }`
- Native interval: `32` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[20];
    uint128_t field_14;
    uint128_t field_24;
    unsigned long long field_34;
    unsigned int field_3c;
} struct_1;

typedef struct struct_0 {
    uint128_t field_0;
    uint128_t field_10;
    unsigned long long field_20;
    unsigned int field_28;
} struct_0;

struct_1 * EyeAdaptationModel_set_settings(struct_1 *ptr, struct_0 *p)
{
    unsigned long long v0;  // x9
    uint128_t v1;  // q1
    uint128_t v2;  // q0

    v0 = p->field_20;
    v1 = p->field_0;
    v2 = p->field_10;
    *((unsigned int *)((char *)&ptr->field_24 + 12)) = p->field_28;
    *((unsigned long long *)((char *)&ptr->field_24 + 4)) = v0;
    *((uint128_t *)((char *)&ptr->field_14 + 4)) = v2;
    *((uint128_t *)&(&ptr->padding_0)[1]) = v1;
    return ptr;
}
```

## `EyeAdaptationModel.Reset` — RVA `0xcdbde0`

- Decompiled symbol: `EyeAdaptationModel_Reset`
- Metadata signature: `public override void Reset() { }`
- Native interval: `64` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[20];
    uint128_t field_14;
    unsigned int field_24;
    char field_28;
    unsigned short field_29;
    char field_2b;
    unsigned int field_2c;
    unsigned long long field_30;
    unsigned long long field_38;
} struct_0;

struct_0 * EyeAdaptationModel_Reset(struct_0 *ptr)
{
    *((unsigned int *)((char *)&ptr->field_14 + 4)) = 0x3e800000;
    *((uint128_t *)&(&ptr->padding_0)[1]) = 0x3f800000c0a0000042be000042340000;
    *((unsigned short *)((char *)&ptr->field_14 + 9)) = 0;
    *((char *)&ptr->field_14 + 11) = 0;
    *((unsigned int *)((char *)&ptr->field_14 + 12)) = 0;
    *((char *)&ptr->field_14 + 8) = 1;
    *((unsigned long long *)&ptr->field_24) = 0x3f80000040000000;
    *((unsigned long long *)&ptr->field_2b) = 21474836472;
    return ptr;
}
```

## `EyeAdaptationModel.ctor` — RVA `0xcdbe64`

- Decompiled symbol: `EyeAdaptationModel_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `68` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[20];
    uint128_t field_14;
    unsigned int field_24;
    char field_28;
    unsigned short field_29;
    char field_2b;
    unsigned int field_2c;
    unsigned long long field_30;
    unsigned long long field_38;
} struct_0;

long long EyeAdaptationModel_ctor(struct_0 *ptr)
{
    *((unsigned int *)((char *)&ptr->field_14 + 4)) = 0x3e800000;
    *((uint128_t *)&(&ptr->padding_0)[1]) = 0x3f800000c0a0000042be000042340000;
    *((unsigned short *)((char *)&ptr->field_14 + 9)) = 0;
    *((char *)&ptr->field_14 + 11) = 0;
    *((unsigned int *)((char *)&ptr->field_14 + 12)) = 0;
    *((char *)&ptr->field_14 + 8) = 1;
    *((unsigned long long *)&ptr->field_24) = 0x3f80000040000000;
    *((unsigned long long *)&ptr->field_2b) = 21474836472;
    PostProcessingModel__ctor(); /* do not return */
}
```
