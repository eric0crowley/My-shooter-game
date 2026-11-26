# Native pseudocode: TouchSplitter

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `TouchSplitter.ctor` — RVA `0xc565bc`

- Decompiled symbol: `TouchSplitter_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `144` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[40];
    unsigned long long field_28;
    long long field_30;
    char padding_38[8];
    long long field_40;
    long long field_48;
} struct_0;

extern long long g_1eed8d0;
extern long long g_1ef89e8;
extern char g_1fab28d;

void TouchSplitter_ctor(struct_0 *a0)
{
    unsigned long long v5;  // x30
    unsigned long long v6;  // x22
    unsigned long long v7;  // x21
    unsigned long long v8;  // x20
    unsigned long long v9;  // x19
    unsigned long long v0;  // [bp-0x30]
    unsigned long long v1;  // [bp-0x20]
    unsigned long long v2;  // [bp-0x18]
    unsigned long long v3;  // [bp-0x10]
    unsigned long long v4;  // [bp-0x8]

    v0 = v5;
    v1 = v6;
    v2 = v7;
    v3 = v8;
    v4 = v9;
    if (!(g_1fab28d & 1))
    {
        sub_f7d92c(&g_1ef89e8);
        sub_f7d92c(&g_1eed8d0);
        g_1fab28d = 1;
    }
    TouchControl__ctor(a0); /* do not return */
}
```

## `TouchSplitter.OnInitControl` — RVA `0xc5664c`

- Decompiled symbol: `TouchSplitter_OnInitControl`
- Metadata signature: `protected override void OnInitControl() { }`
- Native interval: `16` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[664];
    unsigned long long field_298;
} struct_0;

long long TouchSplitter_OnInitControl(struct_0 **a0)
{
    goto *(a0)->field_298;
}
```

## `TouchSplitter.OnUpdateControl` — RVA `0xc5665c`

- Decompiled symbol: `TouchSplitter_OnUpdateControl`
- Metadata signature: `protected override void OnUpdateControl() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long TouchSplitter_OnUpdateControl(void)
{
    unsigned long v0;  // x0

    return v0;
}
```

## `TouchSplitter.OnDestroyControl` — RVA `0xc56660`

- Decompiled symbol: `TouchSplitter_OnDestroyControl`
- Metadata signature: `protected override void OnDestroyControl() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long TouchSplitter_OnDestroyControl(void)
{
    unsigned long v0;  // x0

    return v0;
}
```

## `TouchSplitter.ResetControl` — RVA `0xc56664`

- Decompiled symbol: `TouchSplitter_ResetControl`
- Metadata signature: `public override void ResetControl() { }`
- Native interval: `16` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[680];
    unsigned long long field_2a8;
} struct_0;

long long TouchSplitter_ResetControl(struct_0 **a0)
{
    goto *(a0)->field_2a8;
}
```

## `TouchSplitter.ReleaseAllTouches` — RVA `0xc56674`

- Decompiled symbol: `TouchSplitter_ReleaseAllTouches`
- Metadata signature: `public override void ReleaseAllTouches() { }`
- Native interval: `224` bytes
- Result: `pseudocode`

```c
typedef struct struct_3 {
    char padding_0[24];
    unsigned int field_18;
} struct_3;

typedef struct struct_2 {
    char padding_0[136];
    struct struct_1 *field_88;
} struct_2;

typedef struct struct_1 {
    char padding_0[24];
    int field_18;
} struct_1;

typedef struct struct_4 {
    char padding_0[680];
    struct struct_5 *field_2a8;
    unsigned long long field_2b0;
} struct_4;

typedef struct struct_5 {
    unsigned long long field_0;
} struct_5;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern long long g_1ef8a30;
extern long long g_1ef8a38;
extern char g_1fab28e;

struct_3 * TouchSplitter_ReleaseAllTouches(struct_2 *ptr)
{
    struct_1 *v0;  // x0
    int v1;  // w20
    struct_4 **v2;  // x21
    unsigned long long flag;  // x2
    struct_4 **v4;  // x0
    unsigned long v5;  // x1
    unsigned long v6;  // x0

    if (!(g_1fab28e & 1))
    {
        sub_f7d92c(&g_1ef8a30);
        sub_f7d92c(&g_1ef8a38);
        sub_f7d92c(&g_1ef0c58);
        g_1fab28e = 1;
    }
    v0 = ptr->field_88;
    if (v0)
    {
        v1 = 0;
        do
        {
            if (v0->field_18 <= v1)
                return v0;
            v2 = sub_14a30c0();
            if (!g_1ef0c58->field_e0)
                sub_f7da5c(g_1ef0c58);
            flag = 0;
            if (((char)Object__op_Inequality(v2, 0, 0) & 1))
            {
                if (v2)
                {
                    v4 = v2;
                    v5 = *(v2)->field_2b0;
                    *(v2)->field_2a8();
                }
                break;
            }
        } while ((v0 = (struct_1 *)ptr->field_88, v1 = (int)(v1 + 1), v0));
    }
    v6 = sub_f7db74(v0);
    return sub_f7db74(v0);
}
```

## `TouchSplitter.OnTouchStart` — RVA `0xc56754`

- Decompiled symbol: `TouchSplitter_OnTouchStart`
- Metadata signature: `public override bool OnTouchStart(TouchObject touch, TouchControl sender, TouchControl.TouchStartType touchStartType) { }`
- Native interval: `260` bytes
- Result: `pseudocode`

```c
typedef struct struct_4 {
    char padding_0[136];
    struct struct_3 *field_88;
} struct_4;

typedef struct struct_5 {
    char padding_0[24];
    unsigned int field_18;
} struct_5;

typedef struct struct_1 {
    char padding_0[696];
    struct struct_2 *field_2b8;
    unsigned long long field_2c0;
} struct_1;

typedef struct struct_3 {
    char padding_0[24];
    int field_18;
} struct_3;

typedef struct struct_2 {
    unsigned long long field_0;
} struct_2;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern long long g_1ef8a30;
extern long long g_1ef8a38;
extern char g_1fab28f;

unsigned int TouchSplitter_OnTouchStart(struct_4 *ptr, unsigned long long a1)
{
    struct_5 *v0;  // x0
    unsigned int v1;  // w23
    unsigned int v2;  // w21
    struct_1 **v3;  // x22
    unsigned long long flag;  // x3
    struct_1 **v5;  // x0
    unsigned long long v6;  // x1
    unsigned long v7;  // x4
    struct_4 *v8;  // x2

    if (!(g_1fab28f & 1))
    {
        sub_f7d92c(&g_1ef8a30);
        sub_f7d92c(&g_1ef8a38);
        sub_f7d92c(&g_1ef0c58);
        g_1fab28f = 1;
    }
    v0 = ptr->field_88;
    if (v0)
    {
        v1 = 0;
        v2 = 0;
        do
        {
            if (v0->field_18 <= v2)
                return 0;
            v3 = sub_14a30c0();
            if (!g_1ef0c58->field_e0)
                sub_f7da5c(g_1ef0c58);
            if (((char)Object__op_Inequality(v3, 0, 0) & 1))
            {
                if (v3)
                {
                    flag = 1;
                    v5 = v3;
                    v6 = a1;
                    v7 = *(v3)->field_2c0;
                    v8 = ptr;
                    *(v3)->field_2b8();
                }
                break;
            }
        } while ((v0 = (struct_5 *)ptr->field_88, v2 += 1, v0));
    }
    sub_f7db74(v0);
    return v1 & 1;
}
```

## `TouchSplitter.OnTouchEnd` — RVA `0xc56858`

- Decompiled symbol: `TouchSplitter_OnTouchEnd`
- Metadata signature: `public override bool OnTouchEnd(TouchObject touch, TouchControl.TouchEndType touchEndType) { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
unsigned int TouchSplitter_OnTouchEnd(void)
{
    return 0;
}
```

## `TouchSplitter.OnTouchMove` — RVA `0xc56860`

- Decompiled symbol: `TouchSplitter_OnTouchMove`
- Metadata signature: `public override bool OnTouchMove(TouchObject touch) { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
unsigned int TouchSplitter_OnTouchMove(void)
{
    return 0;
}
```

## `TouchSplitter.OnTouchPressureChange` — RVA `0xc56868`

- Decompiled symbol: `TouchSplitter_OnTouchPressureChange`
- Metadata signature: `public override bool OnTouchPressureChange(TouchObject touch) { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
unsigned int TouchSplitter_OnTouchPressureChange(void)
{
    return 0;
}
```

## `TouchSplitter.CanBeTouchedDirectly` — RVA `0xc56870`

- Decompiled symbol: `TouchSplitter_CanBeTouchedDirectly`
- Metadata signature: `public override bool CanBeTouchedDirectly(TouchObject touchObj) { }`
- Native interval: `280` bytes
- Result: `pseudocode`

```c
typedef struct struct_4 {
    char padding_0[35];
    char field_23;
    char padding_24[44];
    unsigned int field_50;
    char padding_54[52];
    struct struct_3 *field_88;
} struct_4;

typedef struct struct_5 {
    char padding_0[24];
    unsigned int field_18;
} struct_5;

typedef struct struct_1 {
    char padding_0[840];
    struct struct_2 *field_348;
    unsigned long long field_350;
} struct_1;

typedef struct struct_3 {
    char padding_0[24];
    int field_18;
} struct_3;

typedef struct struct_2 {
    unsigned long long field_0;
} struct_2;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern long long g_1ef8a30;
extern long long g_1ef8a38;
extern char g_1fab290;

unsigned int TouchSplitter_CanBeTouchedDirectly(struct_4 *ptr, unsigned long long a1)
{
    unsigned long v0;  // 4115
    struct_5 *p;  // x0
    unsigned long long v10;  // x2
    unsigned long v11;  // x3
    unsigned int v2;  // w21
    unsigned long v3;  // cc_dep1
    unsigned long v4;  // cc_dep2
    unsigned long v5;  // 4102
    unsigned long v6;  // 4102
    struct_1 **v7;  // x23
    struct_1 **v8;  // x0
    struct_4 *v9;  // x1

    if (!(g_1fab290 & 1))
    {
        sub_f7d92c(&g_1ef8a30);
        sub_f7d92c(&g_1ef8a38);
        sub_f7d92c(&g_1ef0c58);
        g_1fab290 = 1;
    }
    if (ptr->field_23)
        return 0;
    v0 = arm64g_calculate_condition(9, (unsigned long long)(ptr->field_50 & 4294967231), 0, 0);
    if ((char)v0)
    {
        p = ptr->field_88;
        if (p)
        {
            v2 = 0;
            do
            {
                v3 = v2;
                v4 = p->field_18;
                if (p->field_18 <= v2)
                {
                    v5 = arm64g_calculate_condition(163, v3, v4, 0);
                    if ((char)v5)
                        return 0;
                }
                else
                {
                    v6 = arm64g_calculate_condition(163, v3, v4, 0);
                    if ((char)v6)
                        return 1;
                }
                v7 = sub_14a30c0();
                if (!g_1ef0c58->field_e0)
                    sub_f7da5c(g_1ef0c58);
                if (!((char)Object__op_Equality(v7, 0, 0) & 1))
                {
                    if (v7)
                    {
                        v8 = v7;
                        v9 = ptr;
                        v10 = a1;
                        v11 = *(v7)->field_350;
                        *(v7)->field_348();
                    }
                    break;
                }
            } while ((p = (struct_5 *)ptr->field_88, v2 += 1, p));
        }
        sub_f7db74(p);
    }
    return 0;
}
```

## `TouchSplitter.CanSwipeOverOthers` — RVA `0xc56988`

- Decompiled symbol: `TouchSplitter_CanSwipeOverOthers`
- Metadata signature: `public override bool CanSwipeOverOthers(TouchObject touchObj) { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
unsigned int TouchSplitter_CanSwipeOverOthers(void)
{
    return 0;
}
```

## `TouchSplitter.CanBeSwipedOverFromNothing` — RVA `0xc56990`

- Decompiled symbol: `TouchSplitter_CanBeSwipedOverFromNothing`
- Metadata signature: `public override bool CanBeSwipedOverFromNothing(TouchObject touchObj) { }`
- Native interval: `32` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[38];
    char field_26;
    char padding_27[41];
    unsigned int field_50;
} struct_0;

unsigned int TouchSplitter_CanBeSwipedOverFromNothing(struct_0 *a0)
{
    unsigned long v0;  // 4118

    if (!a0->field_26)
        return 0;
    v0 = arm64g_calculate_condition(25, (unsigned long long)(a0->field_50 & 4294967231), 0, 0);
    if (!((char)v0))
        return 1;
    return 0;
}
```

## `TouchSplitter.CanBeSwipedOverFromRestrictedList` — RVA `0xc569b0`

- Decompiled symbol: `TouchSplitter_CanBeSwipedOverFromRestrictedList`
- Metadata signature: `public override bool CanBeSwipedOverFromRestrictedList(TouchObject touchObj) { }`
- Native interval: `16` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[80];
    unsigned int field_50;
} struct_0;

unsigned int TouchSplitter_CanBeSwipedOverFromRestrictedList(struct_0 *a0)
{
    unsigned long v0;  // 4118

    v0 = arm64g_calculate_condition(25, (unsigned long long)(a0->field_50 & 4294967231), 0, 0);
    if (!((char)v0))
        return 1;
    return 0;
}
```
