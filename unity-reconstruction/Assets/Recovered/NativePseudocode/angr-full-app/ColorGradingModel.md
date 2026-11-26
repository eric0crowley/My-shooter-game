# Native pseudocode: ColorGradingModel

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `ColorGradingModel.get_settings` — RVA `0xcdb438`

- Decompiled symbol: `ColorGradingModel_get_settings`
- Metadata signature: `public ColorGradingModel.Settings get_settings() { }`
- Native interval: `16` bytes
- Result: `pseudocode`

```c
void ColorGradingModel_get_settings(unsigned long a0)
{
    memcpy();
    return;
}
```

## `ColorGradingModel.set_settings` — RVA `0xcdb448`

- Decompiled symbol: `ColorGradingModel_set_settings`
- Metadata signature: `public void set_settings(ColorGradingModel.Settings value) { }`
- Native interval: `52` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[392];
    unsigned long long field_188;
} struct_0;

void ColorGradingModel_set_settings(struct_0 **a0)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    memmove(a0 + 3);
    sub_f7d8d0(a0 + 27, 0);
    goto *(a0)->field_188;
}
```

## `ColorGradingModel.get_isDirty` — RVA `0xcdb47c`

- Decompiled symbol: `ColorGradingModel_get_isDirty`
- Metadata signature: `public bool get_isDirty() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[288];
    char field_120;
} struct_0;

long long ColorGradingModel_get_isDirty(struct_0 *a0)
{
    return a0->field_120;
}
```

## `ColorGradingModel.set_isDirty` — RVA `0xcdb484`

- Decompiled symbol: `ColorGradingModel_set_isDirty`
- Metadata signature: `internal void set_isDirty(bool value) { }`
- Native interval: `12` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[288];
    char field_120;
} struct_0;

struct_0 * ColorGradingModel_set_isDirty(struct_0 *ptr, char a1)
{
    ptr->field_120 = a1 & 1;
    return ptr;
}
```

## `ColorGradingModel.get_bakedLut` — RVA `0xcdb490`

- Decompiled symbol: `ColorGradingModel_get_bakedLut`
- Metadata signature: `public RenderTexture get_bakedLut() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[296];
    unsigned long long field_128;
} struct_0;

long long ColorGradingModel_get_bakedLut(struct_0 *a0)
{
    return a0->field_128;
}
```

## `ColorGradingModel.set_bakedLut` — RVA `0xcdb498`

- Decompiled symbol: `ColorGradingModel_set_bakedLut`
- Metadata signature: `internal void set_bakedLut(RenderTexture value) { }`
- Native interval: `16` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[296];
    unsigned long long field_128;
} struct_0;

long long ColorGradingModel_set_bakedLut(struct_0 *ptr, unsigned long a1)
{
    long long v0;  // x0

    ptr->field_128 = a1;
    v0 = sub_f7d8d0();
    return sub_f7d8d0();
}
```

## `ColorGradingModel.Reset` — RVA `0xcdb4a8`

- Decompiled symbol: `ColorGradingModel_Reset`
- Metadata signature: `public override void Reset() { }`
- Native interval: `80` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[392];
    unsigned long long field_188;
} struct_0;

void ColorGradingModel_Reset(struct_0 **a0)
{
    unsigned long long v5;  // x30
    unsigned long long v6;  // x19
    char v0;  // [bp-0x128]
    char *v1;  // [bp-0x20]
    unsigned long long v2;  // [bp-0x10]
    unsigned long long v3;  // [bp-0x8]
    char v4;  // [bp+0x0]

    v1 = &v4;
    v2 = v5;
    v3 = v6;
    ColorGradingModel_Settings__get_defaultSettings();
    memcpy(a0 + 3, &v0, 264);
    sub_f7d8d0(a0 + 27, 0);
    goto *(a0)->field_188;
}
```

## `ColorGradingModel.OnValidate` — RVA `0xcdb5c4`

- Decompiled symbol: `ColorGradingModel_OnValidate`
- Metadata signature: `public override void OnValidate() { }`
- Native interval: `12` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[288];
    char field_120;
} struct_0;

struct_0 * ColorGradingModel_OnValidate(struct_0 *ptr)
{
    ptr->field_120 = 1;
    return ptr;
}
```

## `ColorGradingModel.ctor` — RVA `0xcdb5d0`

- Decompiled symbol: `ColorGradingModel_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `76` bytes
- Result: `pseudocode`

```c
long long ColorGradingModel_ctor(long long a0)
{
    char v0;  // [bp-0x128]
    char *v1;  // [bp-0x20]
    char v2;  // [bp+0x0]

    v1 = &v2;
    ColorGradingModel_Settings__get_defaultSettings();
    memcpy(a0 + 24, &v0, 264);
    sub_f7d8d0(a0 + 216, 0);
    PostProcessingModel__ctor(a0, 0); /* do not return */
}
```
