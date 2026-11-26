# Native pseudocode: MotionBlurModel

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `MotionBlurModel.get_settings` — RVA `0xcdbf34`

- Decompiled symbol: `MotionBlurModel_get_settings`
- Metadata signature: `public MotionBlurModel.Settings get_settings() { }`
- Native interval: `16` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[20];
    unsigned long long field_14;
} struct_0;

long long MotionBlurModel_get_settings(struct_0 *a0)
{
    return *((long long *)&(&a0->padding_0)[1]);
}
```

## `MotionBlurModel.set_settings` — RVA `0xcdbf44`

- Decompiled symbol: `MotionBlurModel_set_settings`
- Metadata signature: `public void set_settings(MotionBlurModel.Settings value) { }`
- Native interval: `12` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[20];
    unsigned long long field_14;
    unsigned int field_1c;
} struct_0;

struct_0 * MotionBlurModel_set_settings(struct_0 *ptr, unsigned long a1, unsigned int a2)
{
    *((unsigned long *)&(&ptr->padding_0)[1]) = a1;
    *((unsigned int *)((char *)&ptr->field_14 + 4)) = a2;
    return ptr;
}
```

## `MotionBlurModel.Reset` — RVA `0xcdbf50`

- Decompiled symbol: `MotionBlurModel_Reset`
- Metadata signature: `public override void Reset() { }`
- Native interval: `20` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[20];
    unsigned long long field_14;
    unsigned int field_1c;
} struct_0;

struct_0 * MotionBlurModel_Reset(struct_0 *ptr)
{
    *((unsigned long long *)&(&ptr->padding_0)[1]) = 0xa43870000;
    *((unsigned int *)((char *)&ptr->field_14 + 4)) = 0;
    return ptr;
}
```

## `MotionBlurModel.ctor` — RVA `0xcdbf74`

- Decompiled symbol: `MotionBlurModel_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `24` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[20];
    unsigned long long field_14;
    unsigned int field_1c;
} struct_0;

long long MotionBlurModel_ctor(struct_0 *ptr)
{
    *((unsigned long long *)&(&ptr->padding_0)[1]) = 0xa43870000;
    *((unsigned int *)((char *)&ptr->field_14 + 4)) = 0;
    PostProcessingModel__ctor(); /* do not return */
}
```
