# Native pseudocode: FogModel

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `FogModel.get_settings` — RVA `0xcdbea8`

- Decompiled symbol: `FogModel_get_settings`
- Metadata signature: `public FogModel.Settings get_settings() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[17];
    char field_11;
} struct_0;

long long FogModel_get_settings(struct_0 *a0)
{
    return a0->field_11;
}
```

## `FogModel.set_settings` — RVA `0xcdbeb0`

- Decompiled symbol: `FogModel_set_settings`
- Metadata signature: `public void set_settings(FogModel.Settings value) { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[17];
    char field_11;
} struct_0;

struct_0 * FogModel_set_settings(struct_0 *ptr, char a1)
{
    ptr->field_11 = a1;
    return ptr;
}
```

## `FogModel.Reset` — RVA `0xcdbeb8`

- Decompiled symbol: `FogModel_Reset`
- Metadata signature: `public override void Reset() { }`
- Native interval: `12` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[17];
    char field_11;
} struct_0;

struct_0 * FogModel_Reset(struct_0 *ptr)
{
    ptr->field_11 = 1;
    return ptr;
}
```

## `FogModel.ctor` — RVA `0xcdbecc`

- Decompiled symbol: `FogModel_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `16` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[17];
    char field_11;
} struct_0;

long long FogModel_ctor(struct_0 *ptr)
{
    ptr->field_11 = 1;
    PostProcessingModel__ctor(); /* do not return */
}
```
