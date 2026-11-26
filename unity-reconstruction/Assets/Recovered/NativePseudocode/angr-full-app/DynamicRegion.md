# Native pseudocode: DynamicRegion

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `DynamicRegion.ctor` — RVA `0xc470ac`

- Decompiled symbol: `DynamicRegion_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `32` bytes
- Result: `pseudocode`

```c
void DynamicRegion_ctor(unsigned long a0)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    TouchControl__ctor(); /* do not return */
}
```

## `DynamicRegion.GetTargetControl` — RVA `0xc470cc`

- Decompiled symbol: `DynamicRegion_GetTargetControl`
- Metadata signature: `public DynamicTouchControl GetTargetControl() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[136];
    unsigned long long field_88;
} struct_0;

long long DynamicRegion_GetTargetControl(struct_0 *a0)
{
    return a0->field_88;
}
```

## `DynamicRegion.SetTargetControl` — RVA `0xc470d4`

- Decompiled symbol: `DynamicRegion_SetTargetControl`
- Metadata signature: `public void SetTargetControl(DynamicTouchControl targetControl) { }`
- Native interval: `288` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    char padding_0[136];
    struct struct_1 *field_88;
} struct_2;

typedef struct struct_3 {
    char padding_0[192];
    unsigned long long field_c0;
    char field_c8;
} struct_3;

typedef struct struct_1 {
    char padding_0[192];
    long long field_c0;
    char field_c8;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab22a;

long long DynamicRegion_SetTargetControl(struct_2 *a0, struct_3 *a1)
{
    struct_2 *ptr;  // x21
    long long v1;  // x0
    struct_1 *p;  // x8
    long long v3;  // x22
    long long v4;  // x0
    unsigned long long v5;  // x0

    if (!(g_1fab22a & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab22a = 1;
    }
    ptr = &a0->field_88;
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v1 = Object__op_Equality(a0->field_88, a1, 0);
    if (((char)v1 & 1))
        return v1;
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (((char)Object__op_Inequality(*((long long *)&ptr->padding_0[0]), 0, 0) & 1))
    {
        p = *((long long *)&ptr->padding_0[0]);
        if (p)
        {
            if (p->field_c8)
                v3 = p->field_c0;
            else
                v3 = 0;
            if (!g_1ef0c58->field_e0)
                sub_f7da5c(g_1ef0c58);
            v4 = Object__op_Equality(v3, a0, 0);
            if (((char)v4 & 1))
                return v4;
            if (*((long long *)&ptr->padding_0[0]))
            {
                DynamicTouchControl__OnLinkToDynamicRegion();
                goto LABEL_10471c4;
            }
        }
    }
    else
    {
LABEL_10471c4:
        *((struct_3 **)&ptr->padding_0[0]) = a1;
        sub_f7d8d0(ptr, a1);
        if (*((long long *)&ptr->padding_0[0]))
        {
            v5 = DynamicTouchControl__OnLinkToDynamicRegion(*((long long *)&ptr->padding_0[0]), a0);
            return DynamicTouchControl__OnLinkToDynamicRegion(*((long long *)&ptr->padding_0[0]), a0);
        }
    }
    sub_f7db74();
}
```

## `DynamicRegion.OnInitControl` — RVA `0xc472b8`

- Decompiled symbol: `DynamicRegion_OnInitControl`
- Metadata signature: `protected override void OnInitControl() { }`
- Native interval: `16` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[664];
    unsigned long long field_298;
} struct_0;

long long DynamicRegion_OnInitControl(struct_0 **a0)
{
    goto *(a0)->field_298;
}
```

## `DynamicRegion.OnUpdateControl` — RVA `0xc472c8`

- Decompiled symbol: `DynamicRegion_OnUpdateControl`
- Metadata signature: `protected override void OnUpdateControl() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long DynamicRegion_OnUpdateControl(void)
{
    unsigned long v0;  // x0

    return v0;
}
```

## `DynamicRegion.OnDestroyControl` — RVA `0xc472cc`

- Decompiled symbol: `DynamicRegion_OnDestroyControl`
- Metadata signature: `protected override void OnDestroyControl() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long DynamicRegion_OnDestroyControl(void)
{
    unsigned long v0;  // x0

    return v0;
}
```

## `DynamicRegion.ResetControl` — RVA `0xc472d0`

- Decompiled symbol: `DynamicRegion_ResetControl`
- Metadata signature: `public override void ResetControl() { }`
- Native interval: `16` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[680];
    unsigned long long field_2a8;
} struct_0;

long long DynamicRegion_ResetControl(struct_0 **a0)
{
    goto *(a0)->field_2a8;
}
```

## `DynamicRegion.ReleaseAllTouches` — RVA `0xc472e0`

- Decompiled symbol: `DynamicRegion_ReleaseAllTouches`
- Metadata signature: `public override void ReleaseAllTouches() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long DynamicRegion_ReleaseAllTouches(void)
{
    unsigned long v0;  // x0

    return v0;
}
```

## `DynamicRegion.OnTouchStart` — RVA `0xc472e4`

- Decompiled symbol: `DynamicRegion_OnTouchStart`
- Metadata signature: `public override bool OnTouchStart(TouchObject touch, TouchControl sender, TouchControl.TouchStartType touchStartType) { }`
- Native interval: `172` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    char padding_0[136];
    struct struct_3 *field_88;
} struct_2;

typedef struct struct_1 {
    char padding_0[696];
    unsigned long long field_2b8;
} struct_1;

typedef struct struct_3 {
    struct struct_1 *field_0;
} struct_3;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab22b;

unsigned int DynamicRegion_OnTouchStart(struct_2 *a0, unsigned long a1)
{
    if (!(g_1fab22b & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab22b = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (!((char)Object__op_Inequality(a0->field_88, 0, 0) & 1))
    {
        return 0;
    }
    else if (a0->field_88)
    {
        goto a0->field_88->field_0->field_2b8;
    }
    else
    {
        sub_f7db74(0);
    }
}
```

## `DynamicRegion.OnTouchEnd` — RVA `0xc47390`

- Decompiled symbol: `DynamicRegion_OnTouchEnd`
- Metadata signature: `public override bool OnTouchEnd(TouchObject touch, TouchControl.TouchEndType touchEndType) { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
unsigned int DynamicRegion_OnTouchEnd(void)
{
    return 0;
}
```

## `DynamicRegion.OnTouchMove` — RVA `0xc47398`

- Decompiled symbol: `DynamicRegion_OnTouchMove`
- Metadata signature: `public override bool OnTouchMove(TouchObject touch) { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
unsigned int DynamicRegion_OnTouchMove(void)
{
    return 0;
}
```

## `DynamicRegion.OnTouchPressureChange` — RVA `0xc473a0`

- Decompiled symbol: `DynamicRegion_OnTouchPressureChange`
- Metadata signature: `public override bool OnTouchPressureChange(TouchObject touch) { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
unsigned int DynamicRegion_OnTouchPressureChange(void)
{
    return 0;
}
```

## `DynamicRegion.CanBeTouchedDirectly` — RVA `0xc473a8`

- Decompiled symbol: `DynamicRegion_CanBeTouchedDirectly`
- Metadata signature: `public override bool CanBeTouchedDirectly(TouchObject touchObj) { }`
- Native interval: `168` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    char padding_0[136];
    struct struct_3 *field_88;
} struct_2;

typedef struct struct_1 {
    char padding_0[936];
    unsigned long long field_3a8;
} struct_1;

typedef struct struct_3 {
    struct struct_1 *field_0;
} struct_3;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab22c;

unsigned int DynamicRegion_CanBeTouchedDirectly(struct_2 *a0, long long a1)
{
    if (!(g_1fab22c & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab22c = 1;
    }
    if (!((char)TouchControl__CanBeTouchedDirectly(a0, a1, 0) & 1))
        return 0;
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (!((char)Object__op_Inequality(a0->field_88, 0, 0) & 1))
    {
        return 0;
    }
    else if (a0->field_88)
    {
        goto a0->field_88->field_0->field_3a8;
    }
    else
    {
        sub_f7db74(0);
    }
}
```

## `DynamicRegion.CanBeSwipedOverFromNothing` — RVA `0xc47450`

- Decompiled symbol: `DynamicRegion_CanBeSwipedOverFromNothing`
- Metadata signature: `public override bool CanBeSwipedOverFromNothing(TouchObject touchObj) { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
unsigned int DynamicRegion_CanBeSwipedOverFromNothing(void)
{
    return 0;
}
```

## `DynamicRegion.CanBeSwipedOverFromRestrictedList` — RVA `0xc47458`

- Decompiled symbol: `DynamicRegion_CanBeSwipedOverFromRestrictedList`
- Metadata signature: `public override bool CanBeSwipedOverFromRestrictedList(TouchObject touchObj) { }`
- Native interval: `168` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    char padding_0[136];
    struct struct_3 *field_88;
} struct_2;

typedef struct struct_1 {
    char padding_0[936];
    unsigned long long field_3a8;
} struct_1;

typedef struct struct_3 {
    struct struct_1 *field_0;
} struct_3;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab22d;

unsigned int DynamicRegion_CanBeSwipedOverFromRestrictedList(struct_2 *a0, long long a1)
{
    if (!(g_1fab22d & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab22d = 1;
    }
    if (!((char)TouchControl__CanBeSwipedOverFromRestrictedListDefault(a0, a1, 0) & 1))
        return 0;
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (!((char)Object__op_Inequality(a0->field_88, 0, 0) & 1))
    {
        return 0;
    }
    else if (a0->field_88)
    {
        goto a0->field_88->field_0->field_3a8;
    }
    else
    {
        sub_f7db74(0);
    }
}
```

## `DynamicRegion.CanSwipeOverOthers` — RVA `0xc47500`

- Decompiled symbol: `DynamicRegion_CanSwipeOverOthers`
- Metadata signature: `public override bool CanSwipeOverOthers(TouchObject touchObj) { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
unsigned int DynamicRegion_CanSwipeOverOthers(void)
{
    return 0;
}
```

## `DynamicRegion.CanBeActivatedByOtherControl` — RVA `0xc47508`

- Decompiled symbol: `DynamicRegion_CanBeActivatedByOtherControl`
- Metadata signature: `public override bool CanBeActivatedByOtherControl(TouchControl c, TouchObject touchObj) { }`
- Native interval: `188` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    char padding_0[136];
    struct struct_3 *field_88;
} struct_2;

typedef struct struct_1 {
    char padding_0[936];
    unsigned long long field_3a8;
} struct_1;

typedef struct struct_3 {
    struct struct_1 *field_0;
} struct_3;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab22e;

unsigned int DynamicRegion_CanBeActivatedByOtherControl(struct_2 *a0, long long a1, long long a2)
{
    if (!(g_1fab22e & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab22e = 1;
    }
    if (!((char)TouchControl__CanBeActivatedByOtherControl(a0, a1, a2, 0) & 1))
        return 0;
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (!((char)Object__op_Inequality(a0->field_88, 0, 0) & 1))
    {
        return 0;
    }
    else if (a0->field_88)
    {
        goto a0->field_88->field_0->field_3a8;
    }
    else
    {
        sub_f7db74(0);
    }
}
```
