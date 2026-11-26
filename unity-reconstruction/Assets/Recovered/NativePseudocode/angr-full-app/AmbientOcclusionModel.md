# Native pseudocode: AmbientOcclusionModel

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `AmbientOcclusionModel.get_settings` — RVA `0xcdadc4`

- Decompiled symbol: `AmbientOcclusionModel_get_settings`
- Metadata signature: `public AmbientOcclusionModel.Settings get_settings() { }`
- Native interval: `16` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[20];
    unsigned long long field_14;
} struct_0;

long long AmbientOcclusionModel_get_settings(struct_0 *a0)
{
    return *((long long *)&(&a0->padding_0)[1]);
}
```

## `AmbientOcclusionModel.set_settings` — RVA `0xcdadd4`

- Decompiled symbol: `AmbientOcclusionModel_set_settings`
- Metadata signature: `public void set_settings(AmbientOcclusionModel.Settings value) { }`
- Native interval: `12` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[20];
    unsigned long long field_14;
    unsigned long long field_1c;
} struct_0;

struct_0 * AmbientOcclusionModel_set_settings(struct_0 *ptr, unsigned long a1, unsigned long a2)
{
    *((unsigned long *)&(&ptr->padding_0)[1]) = a1;
    *((unsigned long *)((char *)&ptr->field_14 + 4)) = a2;
    return ptr;
}
```

## `AmbientOcclusionModel.Reset` — RVA `0xcdade0`

- Decompiled symbol: `AmbientOcclusionModel_Reset`
- Metadata signature: `public override void Reset() { }`
- Native interval: `16` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[20];
    uint128_t field_14;
} struct_0;

struct_0 * AmbientOcclusionModel_Reset(struct_0 *ptr)
{
    *((uint128_t *)&(&ptr->padding_0)[1]) = 0x10000000a3e99999a3f800000;
    return ptr;
}
```

## `AmbientOcclusionModel.ctor` — RVA `0xcdae08`

- Decompiled symbol: `AmbientOcclusionModel_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `20` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[20];
    uint128_t field_14;
} struct_0;

long long AmbientOcclusionModel_ctor(struct_0 *ptr)
{
    *((uint128_t *)&(&ptr->padding_0)[1]) = 0x10000000a3e99999a3f800000;
    PostProcessingModel__ctor(); /* do not return */
}
```
