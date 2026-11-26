# Native pseudocode: PostProcessingContext

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `PostProcessingContext.get_interrupted` — RVA `0xcde428`

- Decompiled symbol: `PostProcessingContext_get_interrupted`
- Metadata signature: `public bool get_interrupted() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[48];
    char field_30;
} struct_0;

long long PostProcessingContext_get_interrupted(struct_0 *a0)
{
    return a0->field_30;
}
```

## `PostProcessingContext.set_interrupted` — RVA `0xcde430`

- Decompiled symbol: `PostProcessingContext_set_interrupted`
- Metadata signature: `private void set_interrupted(bool value) { }`
- Native interval: `12` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[48];
    char field_30;
} struct_0;

struct_0 * PostProcessingContext_set_interrupted(struct_0 *ptr, char a1)
{
    ptr->field_30 = a1 & 1;
    return ptr;
}
```

## `PostProcessingContext.Interrupt` — RVA `0xcde43c`

- Decompiled symbol: `PostProcessingContext_Interrupt`
- Metadata signature: `public void Interrupt() { }`
- Native interval: `12` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[48];
    char field_30;
} struct_0;

struct_0 * PostProcessingContext_Interrupt(struct_0 *ptr)
{
    ptr->field_30 = 1;
    return ptr;
}
```

## `PostProcessingContext.Reset` — RVA `0xcde448`

- Decompiled symbol: `PostProcessingContext_Reset`
- Metadata signature: `public PostProcessingContext Reset() { }`
- Native interval: `84` bytes
- Result: `pseudocode`
- Heuristic layout hint: `PostProcessingContext_Recovered` matched 5 offsets against `PostProcessingContext` metadata (confidence 1.00).

```c
typedef struct PostProcessingContext_Recovered {
    char padding_0[16];
    unsigned long long profile;
    unsigned long long camera;
    unsigned long long materialFactory;
    unsigned long long renderTextureFactory;
    char k__BackingField;
} PostProcessingContext_Recovered;

struct_0 * PostProcessingContext_Reset(struct_0 *ptr)
{
    struct_0 *p;  // x0
    struct_0 *addr;  // x0
    struct_0 *ptr3;  // x0

    ptr->field_10 = 0;
    sub_f7d8d0((struct PostProcessingContext_Recovered *)&ptr->field_10, 0);
    p = ptr;
    p->field_18 = 0;
    sub_f7d8d0((struct PostProcessingContext_Recovered *)&p->field_18, 0);
    addr = ptr;
    addr->field_20 = 0;
    sub_f7d8d0((struct PostProcessingContext_Recovered *)&addr->field_20, 0);
    ptr3 = ptr;
    ptr3->field_28 = 0;
    sub_f7d8d0((struct PostProcessingContext_Recovered *)&ptr3->field_28, 0);
    ptr->field_30 = 0;
    return ptr;
}
```

## `PostProcessingContext.get_isGBufferAvailable` — RVA `0xcde49c`

- Decompiled symbol: `PostProcessingContext_get_isGBufferAvailable`
- Metadata signature: `public bool get_isGBufferAvailable() { }`
- Native interval: `40` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    long long field_18;
} struct_0;

unsigned long long PostProcessingContext_get_isGBufferAvailable(struct_0 *a0)
{
    unsigned long long v1;  // x30
    unsigned long long v0;  // [bp-0x10]

    v0 = v1;
    if (a0->field_18)
    {
        if (Camera__get_actualRenderingPath(a0->field_18, 0) != 3)
            return 0;
        return 1;
    }
    sub_f7db74(0);
}
```

## `PostProcessingContext.get_isHdr` — RVA `0xcde4c4`

- Decompiled symbol: `PostProcessingContext_get_isHdr`
- Metadata signature: `public bool get_isHdr() { }`
- Native interval: `28` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

void PostProcessingContext_get_isHdr(struct_0 *a0)
{
    unsigned long long v1;  // x30
    unsigned long long v0;  // [bp-0x10]

    v0 = v1;
    if (a0->field_18)
    {
        Camera__get_allowHDR();
        return;
    }
    sub_f7db74(0);
}
```

## `PostProcessingContext.get_width` — RVA `0xcde4e0`

- Decompiled symbol: `PostProcessingContext_get_width`
- Metadata signature: `public int get_width() { }`
- Native interval: `28` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

void PostProcessingContext_get_width(struct_0 *a0)
{
    unsigned long long v1;  // x30
    unsigned long long v0;  // [bp-0x10]

    v0 = v1;
    if (a0->field_18)
    {
        Camera__get_pixelWidth();
        return;
    }
    sub_f7db74(0);
}
```

## `PostProcessingContext.get_height` — RVA `0xcde4fc`

- Decompiled symbol: `PostProcessingContext_get_height`
- Metadata signature: `public int get_height() { }`
- Native interval: `28` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

void PostProcessingContext_get_height(struct_0 *a0)
{
    unsigned long long v1;  // x30
    unsigned long long v0;  // [bp-0x10]

    v0 = v1;
    if (a0->field_18)
    {
        Camera__get_pixelHeight();
        return;
    }
    sub_f7db74(0);
}
```

## `PostProcessingContext.get_viewport` — RVA `0xcde518`

- Decompiled symbol: `PostProcessingContext_get_viewport`
- Metadata signature: `public Rect get_viewport() { }`
- Native interval: `28` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

void PostProcessingContext_get_viewport(struct_0 *a0)
{
    unsigned long long v1;  // x30
    unsigned long long v0;  // [bp-0x10]

    v0 = v1;
    if (a0->field_18)
    {
        Camera__get_rect();
        return;
    }
    sub_f7db74(0);
}
```

## `PostProcessingContext.ctor` — RVA `0xcde534`

- Decompiled symbol: `PostProcessingContext_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long PostProcessingContext_ctor(void)
{
    long long v0;  // x0

    v0 = Object__ctor();
    return Object__ctor();
}
```
