# Native pseudocode: GrainModel

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `GrainModel.get_settings` — RVA `0xcdbedc`

- Decompiled symbol: `GrainModel_get_settings`
- Metadata signature: `public GrainModel.Settings get_settings() { }`
- Native interval: `16` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[20];
    unsigned long long field_14;
} struct_0;

long long GrainModel_get_settings(struct_0 *a0)
{
    return *((long long *)&(&a0->padding_0)[1]);
}
```

## `GrainModel.set_settings` — RVA `0xcdbeec`

- Decompiled symbol: `GrainModel_set_settings`
- Metadata signature: `public void set_settings(GrainModel.Settings value) { }`
- Native interval: `12` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[20];
    unsigned long long field_14;
    unsigned long long field_1c;
} struct_0;

struct_0 * GrainModel_set_settings(struct_0 *ptr, unsigned long a1, unsigned long a2)
{
    *((unsigned long *)&(&ptr->padding_0)[1]) = a1;
    *((unsigned long *)((char *)&ptr->field_14 + 4)) = a2;
    return ptr;
}
```

## `GrainModel.Reset` — RVA `0xcdbef8`

- Decompiled symbol: `GrainModel_Reset`
- Metadata signature: `public override void Reset() { }`
- Native interval: `16` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[20];
    uint128_t field_14;
} struct_0;

struct_0 * GrainModel_Reset(struct_0 *ptr)
{
    *((uint128_t *)&(&ptr->padding_0)[1]) = 84140132168683105385858894722867658753;
    return ptr;
}
```

## `GrainModel.ctor` — RVA `0xcdbf20`

- Decompiled symbol: `GrainModel_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `20` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[20];
    uint128_t field_14;
} struct_0;

long long GrainModel_ctor(struct_0 *ptr)
{
    *((uint128_t *)&(&ptr->padding_0)[1]) = 84140132168683105385858894722867658753;
    PostProcessingModel__ctor(); /* do not return */
}
```
