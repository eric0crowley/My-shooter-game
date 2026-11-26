# Native pseudocode: ComponentBase

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `ComponentBase.ctor` — RVA `0xc4f5ac`

- Decompiled symbol: `ComponentBase_ctor`
- Metadata signature: `protected void .ctor() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long ComponentBase_ctor(void)
{
    long long v0;  // x0

    v0 = MonoBehaviour__ctor();
    return MonoBehaviour__ctor();
}
```

## `ComponentBase.CanBeUsed` — RVA `0xc502e0`

- Decompiled symbol: `ComponentBase_CanBeUsed`
- Metadata signature: `public bool CanBeUsed() { }`
- Native interval: `56` bytes
- Result: `pseudocode`
- Heuristic layout hint: `ComponentBase_Recovered` matched 2 offsets against `ComponentBase` metadata (confidence 0.67).

```c
typedef struct ComponentBase_Recovered {
    struct struct_0 *field_0;
    char padding_8[24];
    char isReady;
    char isDestroyed;
} ComponentBase_Recovered;

typedef struct struct_0 {
    char padding_0[376];
    struct struct_1 *field_178;
    unsigned long long field_180;
} struct_0;

typedef struct struct_1 {
    unsigned long long field_0;
} struct_1;

unsigned long long ComponentBase_CanBeUsed(struct_2 *ptr)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    unsigned int v4;  // w19
    struct_0 *p;  // x8
    unsigned long long v6;  // x1
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    v4 = ptr->field_21;
    if (!v4 && !ptr->field_20)
    {
        p = ptr->field_0;
        ptr->field_20 = 1;
        v6 = p->field_180;
        p->field_178();
    }
    if (!v4)
        return 1;
    return 0;
}
```

## `ComponentBase.get_IsInitialized` — RVA `0xc5adcc`

- Decompiled symbol: `ComponentBase_get_IsInitialized`
- Metadata signature: `public bool get_IsInitialized() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[32];
    char field_20;
} struct_0;

long long ComponentBase_get_IsInitialized(struct_0 *a0)
{
    return a0->field_20;
}
```

## `ComponentBase.get_IsDestroyed` — RVA `0xc5add4`

- Decompiled symbol: `ComponentBase_get_IsDestroyed`
- Metadata signature: `public bool get_IsDestroyed() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[33];
    char field_21;
} struct_0;

long long ComponentBase_get_IsDestroyed(struct_0 *a0)
{
    return a0->field_21;
}
```

## `ComponentBase.Init` — RVA `0xc5addc`

- Decompiled symbol: `ComponentBase_Init`
- Metadata signature: `public void Init() { }`
- Native interval: `32` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    struct struct_0 *field_0;
    char padding_8[24];
    char field_20;
} struct_1;

typedef struct struct_0 {
    char padding_0[376];
    unsigned long long field_178;
} struct_0;

struct_1 * ComponentBase_Init(struct_1 *ptr)
{
    struct_0 *v0;  // x8

    if (ptr->field_20)
        return ptr;
    v0 = ptr->field_0;
    ptr->field_20 = 1;
    goto v0->field_178;
}
```

## `ComponentBase.ForceInit` — RVA `0xc5adfc`

- Decompiled symbol: `ComponentBase_ForceInit`
- Metadata signature: `public void ForceInit() { }`
- Native interval: `20` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    struct struct_0 *field_0;
    char padding_8[24];
    char field_20;
} struct_1;

typedef struct struct_0 {
    char padding_0[376];
    unsigned long long field_178;
} struct_0;

long long ComponentBase_ForceInit(struct_1 *ptr)
{
    struct_0 *v0;  // x8

    v0 = ptr->field_0;
    ptr->field_20 = 1;
    goto v0->field_178;
}
```

## `ComponentBase.OnEnable` — RVA `0xc5ae10`

- Decompiled symbol: `ComponentBase_OnEnable`
- Metadata signature: `private void OnEnable() { }`
- Native interval: `60` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    struct struct_0 *field_0;
    char padding_8[24];
    char field_20;
} struct_2;

typedef struct struct_3 {
    char padding_0[376];
    struct struct_4 *field_178;
    unsigned long long field_180;
    char padding_188[16];
    unsigned long long field_198;
} struct_3;

typedef struct struct_0 {
    char padding_0[376];
    struct struct_1 *field_178;
    unsigned long long field_180;
    char padding_188[16];
    unsigned long long field_198;
} struct_0;

typedef struct struct_4 {
    unsigned long long field_0;
} struct_4;

typedef struct struct_1 {
    unsigned long long field_0;
} struct_1;

void ComponentBase_OnEnable(struct_2 *ptr)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    struct_3 *p;  // x8
    struct_2 *v5;  // x0
    unsigned long v6;  // x1
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    if (!ptr->field_20)
    {
        p = ptr->field_0;
        ptr->field_20 = 1;
        v5 = ptr;
        v6 = p->field_180;
        p->field_178();
    }
    goto ptr->field_0->field_198;
}
```

## `ComponentBase.OnDisable` — RVA `0xc5ae4c`

- Decompiled symbol: `ComponentBase_OnDisable`
- Metadata signature: `private void OnDisable() { }`
- Native interval: `12` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[424];
    unsigned long long field_1a8;
} struct_0;

long long ComponentBase_OnDisable(struct_0 **a0)
{
    goto *(a0)->field_1a8;
}
```

## `ComponentBase.OnDestroy` — RVA `0xc5ae58`

- Decompiled symbol: `ComponentBase_OnDestroy`
- Metadata signature: `private void OnDestroy() { }`
- Native interval: `20` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    struct struct_0 *field_0;
    char padding_8[24];
    unsigned short field_20;
} struct_1;

typedef struct struct_0 {
    char padding_0[392];
    unsigned long long field_188;
} struct_0;

long long ComponentBase_OnDestroy(struct_1 *ptr)
{
    struct_0 *v0;  // x8

    v0 = ptr->field_0;
    ptr->field_20 = 0x100;
    goto v0->field_188;
}
```
