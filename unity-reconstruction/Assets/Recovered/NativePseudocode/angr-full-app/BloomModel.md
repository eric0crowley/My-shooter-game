# Native pseudocode: BloomModel

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `BloomModel.get_settings` — RVA `0xcdb0b8`

- Decompiled symbol: `BloomModel_get_settings`
- Metadata signature: `public BloomModel.Settings get_settings() { }`
- Native interval: `24` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    uint128_t field_18;
    uint128_t field_28;
    unsigned long long field_38;
} struct_0;

typedef struct struct_1 {
    uint128_t field_0;
    uint128_t field_10;
    unsigned long long field_20;
} struct_1;

struct_0 * BloomModel_get_settings(struct_0 *p)
{
    uint128_t v0;  // q0
    uint128_t v1;  // q1
    struct_1 *ptr;  // x8

    v0 = *((int128_t *)((char *)&p->field_18 + 8));
    v1 = *((int128_t *)&(&p->padding_0)[1]);
    ptr->field_20 = *((long long *)((char *)&p->field_28 + 8));
    ptr->field_0 = v1;
    ptr->field_10 = v0;
    return p;
}
```

## `BloomModel.set_settings` — RVA `0xcdb0d0`

- Decompiled symbol: `BloomModel_set_settings`
- Metadata signature: `public void set_settings(BloomModel.Settings value) { }`
- Native interval: `36` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    uint128_t field_0;
    uint128_t field_10;
    unsigned long long field_20;
} struct_0;

typedef struct struct_1 {
    char padding_0[24];
    uint128_t field_18;
    uint128_t field_28;
    unsigned long long field_38;
} struct_1;

long long BloomModel_set_settings(struct_1 *ptr, struct_0 *p)
{
    uint128_t v0;  // q1
    uint128_t v1;  // q0
    long long v2;  // x0

    v0 = p->field_0;
    v1 = p->field_10;
    *((unsigned long long *)((char *)&ptr->field_28 + 8)) = p->field_20;
    *((uint128_t *)((char *)&ptr->field_18 + 8)) = v1;
    *((uint128_t *)&(&ptr->padding_0)[1]) = v0;
    v2 = sub_f7d8d0();
    return sub_f7d8d0();
}
```

## `BloomModel.Reset` — RVA `0xcdb0f4`

- Decompiled symbol: `BloomModel_Reset`
- Metadata signature: `public override void Reset() { }`
- Native interval: `64` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    uint128_t field_18;
    uint128_t field_28;
    unsigned long long field_38;
} struct_0;

void BloomModel_Reset(struct_0 *ptr)
{
    unsigned long long v5;  // x30
    unsigned long long v6;  // x19
    int v0;  // [bp-0x38]
    int v1;  // [bp-0x28]
    unsigned long v2;  // [bp-0x18]
    unsigned long long v3;  // [bp-0x10]
    unsigned long long v4;  // [bp-0x8]

    v3 = v5;
    v4 = v6;
    BloomModel_Settings__get_defaultSettings();
    *((unsigned long *)((char *)&ptr->field_28 + 8)) = v2;
    *((void*)((char *)&ptr->field_18 + 8)) = v1;
    *((void*)&(&ptr->padding_0)[1]) = v0;
    sub_f7d8d0();
    return;
}
```

## `BloomModel.ctor` — RVA `0xcdb1ac`

- Decompiled symbol: `BloomModel_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `76` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    uint128_t field_18;
    uint128_t field_28;
    unsigned long long field_38;
} struct_0;

long long BloomModel_ctor(struct_0 *ptr)
{
    int v0;  // [bp-0x38]
    int v1;  // [bp-0x28]
    unsigned long v2;  // [bp-0x18]

    BloomModel_Settings__get_defaultSettings();
    *((unsigned long *)((char *)&ptr->field_28 + 8)) = v2;
    *((void*)((char *)&ptr->field_18 + 8)) = v1;
    *((void*)&(&ptr->padding_0)[1]) = v0;
    sub_f7d8d0((struct struct_0 *)&ptr->field_28, 0);
    PostProcessingModel__ctor(ptr, 0); /* do not return */
}
```
