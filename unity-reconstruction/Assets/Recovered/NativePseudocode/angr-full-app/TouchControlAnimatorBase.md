# Native pseudocode: TouchControlAnimatorBase

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `TouchControlAnimatorBase.ctor` — RVA `0xc63594`

- Decompiled symbol: `TouchControlAnimatorBase_ctor`
- Metadata signature: `public void .ctor(Type sourceType) { }`
- Native interval: `48` bytes
- Result: `pseudocode`

```c
long long TouchControlAnimatorBase_ctor(unsigned long a0, unsigned long a1)
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
    ComponentBase__ctor(); /* do not return */
}
```

## `TouchControlAnimatorBase.UpdateAnimator` — RVA `0xc635c4`

- Decompiled symbol: `TouchControlAnimatorBase_UpdateAnimator`
- Metadata signature: `public void UpdateAnimator(bool skipAnim) { }`
- Native interval: `148` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    struct struct_1 *field_0;
    char padding_8[32];
    long long field_28;
} struct_2;

typedef struct struct_1 {
    char padding_0[440];
    unsigned long long field_1b8;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab2e2;

long long TouchControlAnimatorBase_UpdateAnimator(struct_2 *a0, unsigned long a1)
{
    long long v0;  // x0

    if (!(g_1fab2e2 & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab2e2 = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v0 = Object__op_Equality(a0->field_28, 0, 0);
    if (((char)v0 & 1))
        return v0;
    goto a0->field_0->field_1b8;
}
```

## `TouchControlAnimatorBase.SetSourceControl` — RVA `0xc63658`

- Decompiled symbol: `TouchControlAnimatorBase_SetSourceControl`
- Metadata signature: `public void SetSourceControl(TouchControl c) { }`
- Native interval: `292` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab2e3;

long long TouchControlAnimatorBase_SetSourceControl(void* a0, unsigned long a1)
{
    unsigned long v0;  // x21
    void* ptr;  // x20
    unsigned long v2;  // x0
    unsigned long v3;  // 4111
    long long v4;  // x0
    long long v5;  // x0

    v0 = a1;
    if (!(g_1fab2e3 & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab2e3 = 1;
    }
    ptr = a0 + 40;
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (((char)Object__op_Inequality((long long)a0[40], 0, 0) & 1))
    {
        v2 = *((long long *)ptr);
        if (v2)
        {
            TouchControl__RemoveAnimator(v2, a0);
            goto LABEL_10636d4;
        }
    }
    else
    {
LABEL_10636d4:
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        v2 = Object__op_Inequality(v0, 0, 0);
        if (!((char)v2 & 1))
        {
LABEL_1063710:
            *((unsigned long *)ptr) = v0;
            sub_f7d8d0(ptr, v0);
            if (!g_1ef0c58->field_e0)
                sub_f7da5c(g_1ef0c58);
            v4 = Object__op_Inequality(*((long long *)ptr), 0, 0);
            if (!((char)v4 & 1))
                return v4;
            v2 = *((long long *)ptr);
            if (v2)
            {
                v5 = TouchControl__AddAnimator(v2, a0);
                return TouchControl__AddAnimator(v2, a0);
            }
        }
        else if (v0)
        {
            v3 = arm64g_calculate_condition(25, (unsigned long long)((unsigned int)ComponentBase__CanBeUsed(v0) & 1), 0, 0);
            if ((char)v3)
            {
                goto LABEL_1063710;
            }
            else
            {
                v0 = 0;
                goto LABEL_1063710;
            }
        }
    }
    sub_f7db74(v2);
}
```

## `TouchControlAnimatorBase.GetSourceControlType` — RVA `0xc6377c`

- Decompiled symbol: `TouchControlAnimatorBase_GetSourceControlType`
- Metadata signature: `public Type GetSourceControlType() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[48];
    unsigned long long field_30;
} struct_0;

long long TouchControlAnimatorBase_GetSourceControlType(struct_0 *a0)
{
    return a0->field_30;
}
```

## `TouchControlAnimatorBase.FindAutoSource` — RVA `0xc63784`

- Decompiled symbol: `TouchControlAnimatorBase_FindAutoSource`
- Metadata signature: `public TouchControl FindAutoSource() { }`
- Native interval: `132` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    char padding_0[200];
    unsigned long long field_c8;
    char padding_d0[96];
    char field_130;
} struct_2;

typedef struct struct_1 {
    char padding_0[48];
    long long field_30;
} struct_1;

typedef struct struct_0 {
    char padding_0[304];
    char field_130;
} struct_0;

extern struct_0 *g_1ef1e00;
extern char g_1fab2e4;

struct_2 ** TouchControlAnimatorBase_FindAutoSource(struct_1 *a0)
{
    struct_2 **v0;  // x0
    unsigned long v1;  // x9

    if (!(g_1fab2e4 & 1))
    {
        sub_f7d92c(&g_1ef1e00);
        g_1fab2e4 = 1;
    }
    v0 = Component__GetComponentInParent(a0, a0->field_30, 0);
    if (!v0)
        return v0;
    v1 = g_1ef1e00->field_130;
    if (*(v0)->field_130 >= (unsigned int)v1 && *((long long *)(*(v0)->field_c8 + v1 * 8 - 8)) == g_1ef1e00)
        return v0;
    sub_f7df10();
}
```

## `TouchControlAnimatorBase.AutoConnectToSource` — RVA `0xc63808`

- Decompiled symbol: `TouchControlAnimatorBase_AutoConnectToSource`
- Metadata signature: `public void AutoConnectToSource() { }`
- Native interval: `136` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab2e5;

long long TouchControlAnimatorBase_AutoConnectToSource(void* a0)
{
    unsigned long v0;  // x20
    long long v1;  // x0
    long long v2;  // x0

    if (!(g_1fab2e5 & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab2e5 = 1;
    }
    v0 = TouchControlAnimatorBase__FindAutoSource(a0);
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v1 = Object__op_Inequality(v0, 0, 0);
    if (!((char)v1 & 1))
        return v1;
    v2 = TouchControlAnimatorBase__SetSourceControl(a0, v0);
    return TouchControlAnimatorBase__SetSourceControl(a0, v0);
}
```

## `TouchControlAnimatorBase.IsIllegallyAttachedToSource` — RVA `0xc63890`

- Decompiled symbol: `TouchControlAnimatorBase_IsIllegallyAttachedToSource`
- Metadata signature: `public bool IsIllegallyAttachedToSource() { }`
- Native interval: `192` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[40];
    long long field_28;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab2e6;

unsigned int TouchControlAnimatorBase_IsIllegallyAttachedToSource(struct_1 *a0)
{
    if (!(g_1fab2e6 & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab2e6 = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (!((char)Object__op_Inequality(a0->field_28, 0, 0) & 1))
        return 0;
    if (a0->field_28)
    {
        Component__get_gameObject(a0->field_28, 0);
        Component__get_gameObject(a0, 0);
        if (g_1ef0c58->field_e0)
            return Object__op_Equality();
        sub_f7da5c(g_1ef0c58);
        return Object__op_Equality();
    }
    sub_f7db74(0);
}
```

## `TouchControlAnimatorBase.InvalidateHierarchy` — RVA `0xc63950`

- Decompiled symbol: `TouchControlAnimatorBase_InvalidateHierarchy`
- Metadata signature: `public void InvalidateHierarchy() { }`
- Native interval: `140` bytes
- Result: `pseudocode`
- Heuristic layout hint: `TouchControlAnimatorBase_Recovered` matched 2 offsets against `TouchControlAnimatorBase` metadata (confidence 1.00).

```c
typedef struct TouchControlAnimatorBase_Recovered {
    char padding_0[34];
    char autoConnectToSource;
    char padding_23[5];
    long long sourceControl;
} TouchControlAnimatorBase_Recovered;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab2e7;

struct_1 * TouchControlAnimatorBase_InvalidateHierarchy(struct_1 *a0)
{
    struct_1 *v0;  // x0
    struct_1 *v1;  // x0
    struct_1 *v2;  // x0
    struct_1 *v3;  // x0
    long long v4;  // x0

    v0 = a0;
    if (!(g_1fab2e7 & 1))
    {
        v1 = sub_f7d92c(&g_1ef0c58);
        g_1fab2e7 = 1;
        v0 = v1;
    }
    v2 = v0;
    if (!a0->field_22)
        return v2;
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v3 = Object__op_Equality(a0->field_28, 0, 0);
    if (!((char)v3 & 1))
        return v3;
    v4 = TouchControlAnimatorBase__SetSourceControl(a0, TouchControlAnimatorBase__FindAutoSource(a0));
    return TouchControlAnimatorBase__SetSourceControl(a0, TouchControlAnimatorBase__FindAutoSource(a0));
}
```

## `TouchControlAnimatorBase.OnInitComponent` — RVA `0xc639dc`

- Decompiled symbol: `TouchControlAnimatorBase_OnInitComponent`
- Metadata signature: `protected override void OnInitComponent() { }`
- Native interval: `140` bytes
- Result: `pseudocode`
- Heuristic layout hint: `TouchControlAnimatorBase_Recovered` matched 2 offsets against `TouchControlAnimatorBase` metadata (confidence 1.00).

```c
typedef struct TouchControlAnimatorBase_Recovered {
    char padding_0[34];
    char autoConnectToSource;
    char padding_23[5];
    long long sourceControl;
} TouchControlAnimatorBase_Recovered;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab2e8;

long long TouchControlAnimatorBase_OnInitComponent(struct_1 *a0)
{
    long long v0;  // x0
    long long v1;  // x0

    if (!(g_1fab2e8 & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab2e8 = 1;
    }
    if (!a0->field_22)
    {
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        v0 = Object__op_Equality(a0->field_28, 0, 0);
        if (!((char)v0 & 1))
            return v0;
    }
    v1 = TouchControlAnimatorBase__SetSourceControl(a0, TouchControlAnimatorBase__FindAutoSource(a0));
    return TouchControlAnimatorBase__SetSourceControl(a0, TouchControlAnimatorBase__FindAutoSource(a0));
}
```

## `TouchControlAnimatorBase.OnDestroyComponent` — RVA `0xc63a68`

- Decompiled symbol: `TouchControlAnimatorBase_OnDestroyComponent`
- Metadata signature: `protected override void OnDestroyComponent() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long TouchControlAnimatorBase_OnDestroyComponent(void)
{
    unsigned long v0;  // x0

    return v0;
}
```

## `TouchControlAnimatorBase.OnEnableComponent` — RVA `0xc63a6c`

- Decompiled symbol: `TouchControlAnimatorBase_OnEnableComponent`
- Metadata signature: `protected override void OnEnableComponent() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long TouchControlAnimatorBase_OnEnableComponent(void)
{
    unsigned long v0;  // x0

    return v0;
}
```

## `TouchControlAnimatorBase.OnDisableComponent` — RVA `0xc63a70`

- Decompiled symbol: `TouchControlAnimatorBase_OnDisableComponent`
- Metadata signature: `protected override void OnDisableComponent() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long TouchControlAnimatorBase_OnDisableComponent(void)
{
    unsigned long v0;  // x0

    return v0;
}
```
