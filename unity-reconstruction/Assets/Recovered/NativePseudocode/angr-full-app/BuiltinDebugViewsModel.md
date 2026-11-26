# Native pseudocode: BuiltinDebugViewsModel

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `BuiltinDebugViewsModel.IsModeActive` — RVA `0xccdb34`

- Decompiled symbol: `BuiltinDebugViewsModel_IsModeActive`
- Metadata signature: `public bool IsModeActive(BuiltinDebugViewsModel.Mode mode) { }`
- Native interval: `16` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[20];
    unsigned int field_14;
} struct_0;

unsigned long long BuiltinDebugViewsModel_IsModeActive(struct_0 *a0, unsigned int a1)
{
    if (a0->field_14 == a1)
        return 1;
    return 0;
}
```

## `BuiltinDebugViewsModel.get_settings` — RVA `0xcdb260`

- Decompiled symbol: `BuiltinDebugViewsModel_get_settings`
- Metadata signature: `public BuiltinDebugViewsModel.Settings get_settings() { }`
- Native interval: `16` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[20];
    uint128_t field_14;
    uint128_t field_24;
} struct_0;

struct_0 * BuiltinDebugViewsModel_get_settings(struct_0 *p)
{
    uint128_t v0;  // q0
    uint128_t ptr[2];  // x8

    v0 = *((int128_t *)((char *)&p->field_14 + 4));
    ptr[0] = *((int128_t *)&(&p->padding_0)[1]);
    ptr[1] = v0;
    return p;
}
```

## `BuiltinDebugViewsModel.set_settings` — RVA `0xcdb270`

- Decompiled symbol: `BuiltinDebugViewsModel_set_settings`
- Metadata signature: `public void set_settings(BuiltinDebugViewsModel.Settings value) { }`
- Native interval: `16` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[20];
    uint128_t field_14;
    uint128_t field_24;
} struct_0;

struct_0 * BuiltinDebugViewsModel_set_settings(struct_0 *ptr, uint128_t *p)
{
    uint128_t v0;  // q1

    v0 = *(p);
    *((uint128_t *)((char *)&ptr->field_14 + 4)) = p[1];
    *((uint128_t *)&(&ptr->padding_0)[1]) = v0;
    return ptr;
}
```

## `BuiltinDebugViewsModel.get_willInterrupt` — RVA `0xcdb280`

- Decompiled symbol: `BuiltinDebugViewsModel_get_willInterrupt`
- Metadata signature: `public bool get_willInterrupt() { }`
- Native interval: `36` bytes
- Result: `pseudocode`

```c
unsigned int BuiltinDebugViewsModel_get_willInterrupt(unsigned long a0)
{
    if (9 < *((int *)(a0 + 20)))
        return 1;
    return 94 >> ((char)*((int *)(a0 + 20)) & 31) & 1;
}
```

## `BuiltinDebugViewsModel.Reset` — RVA `0xcdb2a4`

- Decompiled symbol: `BuiltinDebugViewsModel_Reset`
- Metadata signature: `public override void Reset() { }`
- Native interval: `40` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[20];
    unsigned int field_14;
    uint128_t field_18;
    unsigned long long field_28;
    unsigned int field_30;
} struct_0;

struct_0 * BuiltinDebugViewsModel_Reset(struct_0 *ptr)
{
    ptr->field_14 = 0;
    *((unsigned long long *)((char *)&ptr->field_18 + 8)) = 0x183f800000;
    *((uint128_t *)&(&ptr->field_14)[1]) = 0x41800000000000003f8000003f800000;
    *((unsigned int *)&ptr->field_28) = 0x42800000;
    return ptr;
}
```

## `BuiltinDebugViewsModel.ctor` — RVA `0xcdb2f4`

- Decompiled symbol: `BuiltinDebugViewsModel_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `44` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[20];
    unsigned int field_14;
    uint128_t field_18;
    unsigned long long field_28;
    unsigned int field_30;
} struct_0;

long long BuiltinDebugViewsModel_ctor(struct_0 *ptr)
{
    ptr->field_14 = 0;
    *((unsigned long long *)((char *)&ptr->field_18 + 8)) = 0x183f800000;
    *((uint128_t *)&(&ptr->field_14)[1]) = 0x41800000000000003f8000003f800000;
    *((unsigned int *)&ptr->field_28) = 0x42800000;
    PostProcessingModel__ctor(); /* do not return */
}
```
