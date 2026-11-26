# Native pseudocode: AntialiasingModel

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `AntialiasingModel.get_settings` — RVA `0xcdae1c`

- Decompiled symbol: `AntialiasingModel_get_settings`
- Metadata signature: `public AntialiasingModel.Settings get_settings() { }`
- Native interval: `20` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[20];
    uint128_t field_14;
    unsigned long long field_24;
} struct_0;

typedef struct struct_1 {
    uint128_t field_0;
    unsigned long long field_10;
} struct_1;

struct_0 * AntialiasingModel_get_settings(struct_0 *p)
{
    uint128_t v0;  // q0
    struct_1 *ptr;  // x8

    v0 = *((int128_t *)&(&p->padding_0)[1]);
    ptr->field_10 = *((long long *)((char *)&p->field_14 + 4));
    ptr->field_0 = v0;
    return p;
}
```

## `AntialiasingModel.set_settings` — RVA `0xcdae30`

- Decompiled symbol: `AntialiasingModel_set_settings`
- Metadata signature: `public void set_settings(AntialiasingModel.Settings value) { }`
- Native interval: `20` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[20];
    uint128_t field_14;
    unsigned long long field_24;
} struct_1;

typedef struct struct_0 {
    uint128_t field_0;
    unsigned long long field_10;
} struct_0;

struct_1 * AntialiasingModel_set_settings(struct_1 *ptr, struct_0 *p)
{
    uint128_t v0;  // q0

    v0 = p->field_0;
    *((unsigned long long *)((char *)&ptr->field_14 + 4)) = p->field_10;
    *((uint128_t *)&(&ptr->padding_0)[1]) = v0;
    return ptr;
}
```

## `AntialiasingModel.Reset` — RVA `0xcdae44`

- Decompiled symbol: `AntialiasingModel_Reset`
- Metadata signature: `public override void Reset() { }`
- Native interval: `28` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[20];
    unsigned long long field_14;
    uint128_t field_1c;
} struct_0;

struct_0 * AntialiasingModel_Reset(struct_0 *ptr)
{
    *((unsigned long long *)&(&ptr->padding_0)[1]) = 0x200000000;
    *((uint128_t *)((char *)&ptr->field_14 + 4)) = 0x3f59999a3f7333333e99999a3f400000;
    return ptr;
}
```

## `AntialiasingModel.ctor` — RVA `0xcdae7c`

- Decompiled symbol: `AntialiasingModel_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `32` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[20];
    unsigned long long field_14;
    uint128_t field_1c;
} struct_0;

long long AntialiasingModel_ctor(struct_0 *ptr)
{
    *((unsigned long long *)&(&ptr->padding_0)[1]) = 0x200000000;
    *((uint128_t *)((char *)&ptr->field_14 + 4)) = 0x3f59999a3f7333333e99999a3f400000;
    PostProcessingModel__ctor(); /* do not return */
}
```
