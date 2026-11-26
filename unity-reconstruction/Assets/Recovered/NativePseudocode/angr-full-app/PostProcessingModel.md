# Native pseudocode: PostProcessingModel

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `PostProcessingModel.get_enabled` — RVA `0xcde53c`

- Decompiled symbol: `PostProcessingModel_get_enabled`
- Metadata signature: `public bool get_enabled() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    char field_10;
} struct_0;

long long PostProcessingModel_get_enabled(struct_0 *a0)
{
    return a0->field_10;
}
```

## `PostProcessingModel.set_enabled` — RVA `0xcde544`

- Decompiled symbol: `PostProcessingModel_set_enabled`
- Metadata signature: `public void set_enabled(bool value) { }`
- Native interval: `28` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    struct struct_0 *field_0;
    char padding_8[8];
    char field_10;
} struct_1;

typedef struct struct_0 {
    char padding_0[392];
    unsigned long long field_188;
} struct_0;

struct_1 * PostProcessingModel_set_enabled(struct_1 *ptr, unsigned long a1)
{
    ptr->field_10 = (char)a1 & 1;
    if (!((char)a1 & 1))
        return ptr;
    goto ptr->field_0->field_188;
}
```

## `PostProcessingModel.OnValidate` — RVA `0xcde560`

- Decompiled symbol: `PostProcessingModel_OnValidate`
- Metadata signature: `public virtual void OnValidate() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long PostProcessingModel_OnValidate(void)
{
    unsigned long v0;  // x0

    return v0;
}
```

## `PostProcessingModel.ctor` — RVA `0xcde564`

- Decompiled symbol: `PostProcessingModel_ctor`
- Metadata signature: `protected void .ctor() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long PostProcessingModel_ctor(void)
{
    long long v0;  // x0

    v0 = Object__ctor();
    return Object__ctor();
}
```
