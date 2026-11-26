# Native pseudocode: InputBindingBase

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `InputBindingBase.ctor` — RVA `0xc5d544`

- Decompiled symbol: `InputBindingBase_ctor`
- Metadata signature: `public void .ctor(InputBindingBase parent) { }`
- Native interval: `52` bytes
- Result: `pseudocode`

```c
void InputBindingBase_ctor(void* ptr, unsigned long a1)
{
    unsigned long long v3;  // x30
    unsigned long long v4;  // x20
    unsigned long long v5;  // x19
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x10]
    unsigned long long v2;  // [bp-0x8]

    v0 = v3;
    v1 = v4;
    v2 = v5;
    Object__ctor();
    *((unsigned long *)&ptr[24]) = a1;
    *((char *)&ptr[16]) = 0;
    sub_f7d8d0();
    return;
}
```

## `InputBindingBase.Enable` — RVA `0xc5d59c`

- Decompiled symbol: `InputBindingBase_Enable`
- Metadata signature: `public void Enable() { }`
- Native interval: `24` bytes
- Result: `pseudocode`
- Heuristic layout hint: `InputBindingBase_Recovered` matched 2 offsets against `InputBindingBase` metadata (confidence 1.00).

```c
typedef struct InputBindingBase_Recovered {
    char padding_0[16];
    char enabled;
    char padding_11[7];
    struct InputBindingBase_Recovered *parent;
} InputBindingBase_Recovered;

struct_0 * InputBindingBase_Enable(struct_0 *cur)
{
    if (!cur)
        return cur;
    do
    {
        cur->field_10 = 1;
        cur = cur->field_18;
    } while (cur);
    return cur;
}
```

## `InputBindingBase.GetSubBindingDescriptions` — RVA `0xc5daa0`

- Decompiled symbol: `InputBindingBase_GetSubBindingDescriptions`
- Metadata signature: `public void GetSubBindingDescriptions(BindingDescriptionList descList, Object undoObject, string parentMenuPath) { }`
- Native interval: `12` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[456];
    unsigned long long field_1c8;
} struct_0;

long long InputBindingBase_GetSubBindingDescriptions(struct_0 **a0)
{
    goto *(a0)->field_1c8;
}
```

## `InputBindingBase.GetParent` — RVA `0xc5ddf0`

- Decompiled symbol: `InputBindingBase_GetParent`
- Metadata signature: `public InputBindingBase GetParent() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long InputBindingBase_GetParent(struct_0 *a0)
{
    return a0->field_18;
}
```

## `InputBindingBase.IsEnabledInHierarchy` — RVA `0xc5ddf8`

- Decompiled symbol: `InputBindingBase_IsEnabledInHierarchy`
- Metadata signature: `public bool IsEnabledInHierarchy() { }`
- Native interval: `44` bytes
- Result: `pseudocode`
- Heuristic layout hint: `InputBindingBase_Recovered` matched 2 offsets against `InputBindingBase` metadata (confidence 1.00).

```c
typedef struct InputBindingBase_Recovered {
    char padding_0[16];
    char enabled;
    char padding_11[7];
    struct InputBindingBase_Recovered *parent;
} InputBindingBase_Recovered;

unsigned long long InputBindingBase_IsEnabledInHierarchy(struct_0 *a0)
{
    unsigned long long v1;  // x30
    struct_0 *ptr;  // x0
    unsigned int v3;  // w8
    struct_0 *v4;  // x0
    unsigned long long v0;  // [bp-0x10]

    v0 = v1;
    do
    {
        if (!a0)
            sub_f7db74();
    } while ((v3 = (unsigned int)ptr->field_10, v3 && (v4 = (struct_0 *)ptr->field_18, a0 = (struct_0 *)ptr->field_18, ptr->field_18)));
    if (v3)
        return 1;
    return 0;
}
```

## `InputBindingBase.OnGetSubBindingDescriptions` — RVA `0xc5de24`

- Decompiled symbol: `InputBindingBase_OnGetSubBindingDescriptions`
- Metadata signature: `protected virtual void OnGetSubBindingDescriptions(BindingDescriptionList descList, Object undoObject, string parentMenuPath) { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long InputBindingBase_OnGetSubBindingDescriptions(void)
{
    unsigned long v0;  // x0

    return v0;
}
```

## `InputBindingBase.IsBoundToKey` — RVA `0xc5de28`

- Decompiled symbol: `InputBindingBase_IsBoundToKey`
- Metadata signature: `public bool IsBoundToKey(KeyCode key, InputRig rig) { }`
- Native interval: `12` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[472];
    unsigned long long field_1d8;
} struct_0;

long long InputBindingBase_IsBoundToKey(struct_0 **a0)
{
    goto *(a0)->field_1d8;
}
```

## `InputBindingBase.IsBoundToAxis` — RVA `0xc5de34`

- Decompiled symbol: `InputBindingBase_IsBoundToAxis`
- Metadata signature: `public bool IsBoundToAxis(string axisName, InputRig rig) { }`
- Native interval: `12` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[488];
    unsigned long long field_1e8;
} struct_0;

long long InputBindingBase_IsBoundToAxis(struct_0 **a0)
{
    goto *(a0)->field_1e8;
}
```

## `InputBindingBase.IsEmulatingTouches` — RVA `0xc5de40`

- Decompiled symbol: `InputBindingBase_IsEmulatingTouches`
- Metadata signature: `public bool IsEmulatingTouches() { }`
- Native interval: `12` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[504];
    unsigned long long field_1f8;
} struct_0;

long long InputBindingBase_IsEmulatingTouches(struct_0 **a0)
{
    goto *(a0)->field_1f8;
}
```

## `InputBindingBase.IsEmulatingMousePosition` — RVA `0xc5de4c`

- Decompiled symbol: `InputBindingBase_IsEmulatingMousePosition`
- Metadata signature: `public bool IsEmulatingMousePosition() { }`
- Native interval: `16` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[520];
    unsigned long long field_208;
} struct_0;

long long InputBindingBase_IsEmulatingMousePosition(struct_0 **a0)
{
    goto *(a0)->field_208;
}
```

## `InputBindingBase.OnIsBoundToKey` — RVA `0xc5de5c`

- Decompiled symbol: `InputBindingBase_OnIsBoundToKey`
- Metadata signature: `protected virtual bool OnIsBoundToKey(KeyCode key, InputRig rig) { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
unsigned int InputBindingBase_OnIsBoundToKey(void)
{
    return 0;
}
```

## `InputBindingBase.OnIsBoundToAxis` — RVA `0xc5de64`

- Decompiled symbol: `InputBindingBase_OnIsBoundToAxis`
- Metadata signature: `protected virtual bool OnIsBoundToAxis(string axisName, InputRig rig) { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
unsigned int InputBindingBase_OnIsBoundToAxis(void)
{
    return 0;
}
```

## `InputBindingBase.OnIsEmulatingTouches` — RVA `0xc5de6c`

- Decompiled symbol: `InputBindingBase_OnIsEmulatingTouches`
- Metadata signature: `protected virtual bool OnIsEmulatingTouches() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
unsigned int InputBindingBase_OnIsEmulatingTouches(void)
{
    return 0;
}
```

## `InputBindingBase.OnIsEmulatingMousePosition` — RVA `0xc5de74`

- Decompiled symbol: `InputBindingBase_OnIsEmulatingMousePosition`
- Metadata signature: `protected virtual bool OnIsEmulatingMousePosition() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
unsigned int InputBindingBase_OnIsEmulatingMousePosition(void)
{
    return 0;
}
```
