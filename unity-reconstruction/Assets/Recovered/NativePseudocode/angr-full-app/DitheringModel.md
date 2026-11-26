# Native pseudocode: DitheringModel

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `DitheringModel.get_settings` — RVA `0xcdbd7c`

- Decompiled symbol: `DitheringModel_get_settings`
- Metadata signature: `public DitheringModel.Settings get_settings() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[17];
    char field_11;
} struct_0;

long long DitheringModel_get_settings(struct_0 *a0)
{
    return a0->field_11;
}
```

## `DitheringModel.set_settings` — RVA `0xcdbd84`

- Decompiled symbol: `DitheringModel_set_settings`
- Metadata signature: `public void set_settings(DitheringModel.Settings value) { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[17];
    char field_11;
} struct_0;

struct_0 * DitheringModel_set_settings(struct_0 *ptr, char a1)
{
    ptr->field_11 = a1;
    return ptr;
}
```

## `DitheringModel.Reset` — RVA `0xcdbd8c`

- Decompiled symbol: `DitheringModel_Reset`
- Metadata signature: `public override void Reset() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[17];
    char field_11;
} struct_0;

struct_0 * DitheringModel_Reset(struct_0 *ptr)
{
    ptr->field_11 = 0;
    return ptr;
}
```

## `DitheringModel.ctor` — RVA `0xcdbd9c`

- Decompiled symbol: `DitheringModel_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `12` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[17];
    char field_11;
} struct_0;

long long DitheringModel_ctor(struct_0 *ptr)
{
    ptr->field_11 = 0;
    PostProcessingModel__ctor(); /* do not return */
}
```
