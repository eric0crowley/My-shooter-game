# Native pseudocode: DepthOfFieldModel

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `DepthOfFieldModel.get_settings` — RVA `0xcdbccc`

- Decompiled symbol: `DepthOfFieldModel_get_settings`
- Metadata signature: `public DepthOfFieldModel.Settings get_settings() { }`
- Native interval: `20` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[20];
    uint128_t field_14;
    unsigned int field_24;
} struct_0;

typedef struct struct_1 {
    uint128_t field_0;
    unsigned int field_10;
} struct_1;

struct_0 * DepthOfFieldModel_get_settings(struct_0 *p)
{
    uint128_t v0;  // q0
    struct_1 *ptr;  // x8

    v0 = *((int128_t *)&(&p->padding_0)[1]);
    ptr->field_10 = *((int *)((char *)&p->field_14 + 4));
    ptr->field_0 = v0;
    return p;
}
```

## `DepthOfFieldModel.set_settings` — RVA `0xcdbce0`

- Decompiled symbol: `DepthOfFieldModel_set_settings`
- Metadata signature: `public void set_settings(DepthOfFieldModel.Settings value) { }`
- Native interval: `20` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[20];
    uint128_t field_14;
    unsigned int field_24;
} struct_1;

typedef struct struct_0 {
    uint128_t field_0;
    unsigned int field_10;
} struct_0;

struct_1 * DepthOfFieldModel_set_settings(struct_1 *ptr, struct_0 *p)
{
    uint128_t v0;  // q0

    v0 = p->field_0;
    *((unsigned int *)((char *)&ptr->field_14 + 4)) = p->field_10;
    *((uint128_t *)&(&ptr->padding_0)[1]) = v0;
    return ptr;
}
```

## `DepthOfFieldModel.Reset` — RVA `0xcdbcf4`

- Decompiled symbol: `DepthOfFieldModel_Reset`
- Metadata signature: `public override void Reset() { }`
- Native interval: `44` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[20];
    unsigned long long field_14;
    unsigned int field_1c;
    char field_20;
    unsigned short field_21;
    char field_23;
    unsigned int field_24;
} struct_0;

struct_0 * DepthOfFieldModel_Reset(struct_0 *ptr)
{
    *((char *)&ptr->field_1c) = 0;
    *((unsigned short *)((char *)&ptr->field_1c + 1)) = 0;
    *((char *)&ptr->field_1c + 3) = 0;
    *((unsigned int *)((char *)&ptr->field_14 + 4)) = 0x42480000;
    *((unsigned long long *)&(&ptr->padding_0)[1]) = 0x40b3333341200000;
    *((unsigned int *)&ptr->field_20) = 1;
    return ptr;
}
```

## `DepthOfFieldModel.ctor` — RVA `0xcdbd4c`

- Decompiled symbol: `DepthOfFieldModel_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `48` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[20];
    unsigned long long field_14;
    unsigned int field_1c;
    char field_20;
    unsigned short field_21;
    char field_23;
    unsigned int field_24;
} struct_0;

long long DepthOfFieldModel_ctor(struct_0 *ptr)
{
    *((char *)&ptr->field_1c) = 0;
    *((unsigned short *)((char *)&ptr->field_1c + 1)) = 0;
    *((char *)&ptr->field_1c + 3) = 0;
    *((unsigned int *)((char *)&ptr->field_14 + 4)) = 0x42480000;
    *((unsigned long long *)&(&ptr->padding_0)[1]) = 0x40b3333341200000;
    *((unsigned int *)&ptr->field_20) = 1;
    PostProcessingModel__ctor(); /* do not return */
}
```
