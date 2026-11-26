# Native pseudocode: bl_IconItem

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `bl_IconItem.Awake` — RVA `0xcc59b8`

- Decompiled symbol: `bl_IconItem_Awake`
- Metadata signature: `private void Awake() { }`
- Native interval: `516` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern long long g_1efcf08;
extern long long g_1efcf48;
extern long long g_1efeaa0;
extern char g_1fab542;

long long bl_IconItem_Awake(long long *a0)
{
    long long v0;  // x0
    long long v1;  // x0
    long long v2;  // x1
    long long ptr[11];  // x0
    long long v4;  // x0
    long long v5;  // x1
    long long p[11];  // x0
    long long v7;  // x0
    long long v8;  // x0

    if (!(g_1fab542 & 1))
    {
        sub_f7d92c(&g_1efcf08);
        sub_f7d92c(&g_1efcf48);
        sub_f7d92c(&g_1efeaa0);
        sub_f7d92c(&g_1ef0c58);
        g_1fab542 = 1;
    }
    v0 = sub_1231bc8(a0, g_1efcf48);
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (((char)Object__op_Inequality(v0, 0, 0) & 1))
    {
        v1 = sub_1231bc8(a0, g_1efcf48);
        goto LABEL_10c5a84;
    }
    if (Component__get_gameObject(a0, 0))
    {
        v1 = sub_124913c();
LABEL_10c5a84:
        v2 = v1;
        ptr = a0;
        ptr[9] = v2;
        sub_f7d8d0((long long [11])&ptr[9], v2);
        v4 = sub_1231bc8(a0, g_1efcf08);
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        if (((char)Object__op_Inequality(v4, 0, 0) & 1))
        {
            v5 = sub_1231bc8(a0, g_1efcf08);
            p = a0;
            p[10] = v5;
            sub_f7d8d0((long long [11])&p[10], v5);
        }
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        if (!((char)Object__op_Inequality(a0[10], 0, 0) & 1))
        {
LABEL_10c5b2c:
            if (a0[9])
            {
                CanvasGroup__set_ignoreParentGroups(a0[9], 1, 0);
                if (a0[9])
                {
                    CanvasGroup__set_alpha(a0[9], 0);
                    if (!g_1ef0c58->field_e0)
                        sub_f7da5c(g_1ef0c58);
                    v7 = Object__op_Inequality(a0[6], 0, 0);
                    if (!((char)v7 & 1))
                        return v7;
                    if (a0[6] && Component__get_gameObject(a0[6], 0))
                    {
                        v8 = GameObject__SetActive();
                        return GameObject__SetActive();
                    }
                }
            }
        }
        else if (a0[10])
        {
            Behaviour__set_enabled(a0[10], 0, 0);
            goto LABEL_10c5b2c;
        }
    }
    sub_f7db74();
}
```

## `bl_IconItem.DestroyIcon` — RVA `0xcc5bbc`

- Decompiled symbol: `bl_IconItem_DestroyIcon`
- Metadata signature: `public void DestroyIcon(bool inmediate) { }`
- Native interval: `224` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab543;

void bl_IconItem_DestroyIcon(long long *a0, unsigned int a1, unsigned long a2)
{
    unsigned long long v5;  // d8
    unsigned long long v6;  // x30
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
    if (!(g_1fab543 & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab543 = 1;
    }
    if (((char)a1 & 1))
    {
        Component__get_gameObject(a0, 0);
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        Object__Destroy();
        return;
    }
    if (a0[5])
    {
        Image__set_sprite(a0[5], a0[7], 0);
        Component__get_gameObject(a0, 0);
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        Object__Destroy();
        return;
    }
    sub_f7db74(0);
}
```

## `bl_IconItem.DestroyIcon` — RVA `0xcc5c9c`

- Decompiled symbol: `bl_IconItem_DestroyIcon`
- Metadata signature: `public void DestroyIcon(bool inmediate, Sprite death) { }`
- Native interval: `240` bytes
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
extern char g_1fab544;

void bl_IconItem_DestroyIcon(struct_1 *a0, unsigned int a1, long long a2)
{
    unsigned long long v6;  // d8
    unsigned long long v7;  // x30
    unsigned long long v8;  // x22
    unsigned long long v9;  // x21
    unsigned long long v10;  // x20
    unsigned long long v11;  // x19
    unsigned long long v0;  // [bp-0x30]
    unsigned long long v1;  // [bp-0x28]
    unsigned long long v2;  // [bp-0x20]
    unsigned long long v3;  // [bp-0x18]
    unsigned long long v4;  // [bp-0x10]
    unsigned long long v5;  // [bp-0x8]

    v0 = v6;
    v1 = v7;
    v2 = v8;
    v3 = v9;
    v4 = v10;
    v5 = v11;
    if (!(g_1fab544 & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab544 = 1;
    }
    if (((char)a1 & 1))
    {
        Component__get_gameObject(a0, 0);
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        Object__Destroy();
        return;
    }
    if (a0->field_28)
    {
        Image__set_sprite(a0->field_28, a2, 0);
        Component__get_gameObject(a0, 0);
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        Object__Destroy();
        return;
    }
    sub_f7db74(0);
}
```

## `bl_IconItem.GetInfoItem` — RVA `0xcc5d8c`

- Decompiled symbol: `bl_IconItem_GetInfoItem`
- Metadata signature: `public void GetInfoItem(string info) { }`
- Native interval: `160` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    char padding_0[64];
    struct struct_3 *field_40;
} struct_2;

typedef struct struct_1 {
    char padding_0[1512];
    unsigned long long field_5e8;
} struct_1;

typedef struct struct_3 {
    struct struct_1 *field_0;
} struct_3;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab545;

long long bl_IconItem_GetInfoItem(struct_2 *a0, unsigned long a1)
{
    long long v0;  // x0

    if (!(g_1fab545 & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab545 = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v0 = Object__op_Equality(a0->field_40, 0, 0);
    if (((char)v0 & 1))
        return v0;
    if (!a0->field_40)
        sub_f7db74(0);
    goto a0->field_40->field_0->field_5e8;
}
```

## `bl_IconItem.SetIcon` — RVA `0xcc5e2c`

- Decompiled symbol: `bl_IconItem_SetIcon`
- Metadata signature: `public void SetIcon(Sprite ico) { }`
- Native interval: `28` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[40];
    unsigned long long field_28;
} struct_0;

void bl_IconItem_SetIcon(struct_0 *a0)
{
    unsigned long long v1;  // x30
    unsigned long long v0;  // [bp-0x10]

    v0 = v1;
    if (a0->field_28)
    {
        Image__set_sprite();
        return;
    }
    sub_f7db74(0);
}
```

## `bl_IconItem.SetCircleArea` — RVA `0xcc5e48`

- Decompiled symbol: `bl_IconItem_SetCircleArea`
- Metadata signature: `public RectTransform SetCircleArea(float radius, Color AreaColor) { }`
- Native interval: `436` bytes
- Result: `pseudocode`
- Heuristic layout hint: `bl_IconItem_Recovered` matched 2 offsets against `bl_IconItem` metadata (confidence 1.00).

```c
typedef struct bl_IconItem_Recovered {
    char padding_0[48];
    long long CircleAreaRect;
    char padding_38[40];
    struct struct_1 *MaskHelper;
} bl_IconItem_Recovered;

typedef struct struct_3 {
    char padding_0[72];
    unsigned long long field_48;
} struct_3;

typedef struct struct_1 {
    char padding_0[72];
    long long field_48;
} struct_1;

typedef struct struct_4 {
    char padding_0[1064];
    struct struct_5 *field_428;
    unsigned long long field_430;
} struct_4;

typedef struct struct_5 {
    unsigned long long field_0;
} struct_5;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern long long g_1efcfd0;
extern long long g_1efd158;
extern char g_1fab546;

unsigned int bl_IconItem_SetCircleArea(struct_2 *ptr)
{
    struct_3 *v0;  // x0
    struct_2 *v1;  // x20
    struct_4 **v2;  // x0
    unsigned long long flag;  // x1
    unsigned long long choice;  // x2
    unsigned long long v5;  // x3

    if (!(g_1fab546 & 1))
    {
        sub_f7d92c(&g_1efd158);
        sub_f7d92c(&g_1efcfd0);
        sub_f7d92c(&g_1ef0c58);
        g_1fab546 = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (((char)Object__op_Equality(ptr->field_30, 0, 0) & 1))
        return 0;
    if (Component__get_transform(ptr, 0) && Transform__get_root())
    {
        v0 = sub_1231e2c();
        ptr->field_60 = v0;
        v1 = &ptr->field_60;
        sub_f7d8d0(v1, v0);
        if (*((long long *)&v1->padding_0[0]) && v1->field_30)
        {
            Transform__SetParent(v1->field_30, *((long long *)(*((long long *)&v1->padding_0[0]) + 72)), 0);
            if (bl_MiniMapUtils__GetMiniMap(0) && ptr->field_30)
            {
                RectTransform__set_sizeDelta(ptr->field_30, 0);
                if (ptr->field_30)
                {
                    v2 = sub_1231bc8(ptr->field_30, g_1efcfd0);
                    if (v2)
                    {
                        flag = 1;
                        choice = 1;
                        v5 = *(v2)->field_430;
                        *(v2)->field_428();
                    }
                }
            }
        }
    }
    sub_f7db74();
}
```

## `bl_IconItem.HideCircleArea` — RVA `0xcc60ac`

- Decompiled symbol: `bl_IconItem_HideCircleArea`
- Metadata signature: `public void HideCircleArea() { }`
- Native interval: `88` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[48];
    long long field_30;
} struct_0;

void bl_IconItem_HideCircleArea(struct_0 *a0)
{
    unsigned long long v3;  // x30
    unsigned long long v4;  // x20
    unsigned long long v5;  // x19
    unsigned long v6;  // x0
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x10]
    unsigned long long v2;  // [bp-0x8]

    v0 = v3;
    v1 = v4;
    v2 = v5;
    v6 = Component__get_transform();
    if (a0->field_30)
    {
        Transform__SetParent(a0->field_30, v6, 0);
        if (a0->field_30 && Component__get_gameObject(a0->field_30, 0))
        {
            GameObject__SetActive();
            return;
        }
    }
    sub_f7db74();
}
```

## `bl_IconItem.FadeIcon` — RVA `0xcc6104`

- Decompiled symbol: `bl_IconItem_FadeIcon`
- Metadata signature: `private IEnumerator FadeIcon() { }`
- Native interval: `108` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[12];
    long long field_20;
} struct_0;

extern long long g_1ef4148;
extern char g_1fab547;

struct_0 * bl_IconItem_FadeIcon(long long a0)
{
    struct_0 *v0;  // x20
    struct_0 *ptr;  // x0

    if (!(g_1fab547 & 1))
    {
        sub_f7d92c(&g_1ef4148);
        g_1fab547 = 1;
    }
    v0 = sub_f7db70(g_1ef4148);
    Object__ctor(v0, 0);
    ptr = v0;
    ptr->field_10 = 0;
    ptr->field_20 = a0;
    sub_f7d8d0((struct struct_0 *)&ptr->field_20, a0);
    return ptr;
}
```

## `bl_IconItem.<FadeIcon>d__16.ctor` — RVA `0xcc6170`

- Decompiled symbol: `bl_IconItem_FadeIcon_d__16_ctor`
- Metadata signature: `public void .ctor(int <>1__state) { }`
- Native interval: `40` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

void bl_IconItem_FadeIcon_d__16_ctor(struct_0 *ptr, unsigned int a1)
{
    Object__ctor();
    ptr->field_10 = a1;
    return;
}
```

## `bl_IconItem.InfoItem` — RVA `0xcc6198`

- Decompiled symbol: `bl_IconItem_InfoItem`
- Metadata signature: `public void InfoItem() { }`
- Native interval: `128` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[104];
    char field_68;
} struct_0;

extern long long g_1efcf08;
extern long long g_1f0cbe8;
extern char g_1fab548;

void bl_IconItem_InfoItem(struct_0 *ptr)
{
    unsigned long long v4;  // x30
    unsigned long long v5;  // x21
    unsigned long long v6;  // x20
    unsigned long long v7;  // x19
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x18]
    unsigned long long v2;  // [bp-0x10]
    unsigned long long v3;  // [bp-0x8]

    v0 = v4;
    v1 = v5;
    v2 = v6;
    v3 = v7;
    if (!(g_1fab548 & 1))
    {
        sub_f7d92c(&g_1efcf08);
        sub_f7d92c(&g_1f0cbe8);
        g_1fab548 = 1;
    }
    ptr->field_68 = ptr->field_68 ^ 1;
    if (sub_1231bc8(ptr, g_1efcf08))
    {
        Animator__SetBool();
        return;
    }
    sub_f7db74();
}
```

## `bl_IconItem.DelayStart` — RVA `0xcc6218`

- Decompiled symbol: `bl_IconItem_DelayStart`
- Metadata signature: `public void DelayStart(float v) { }`
- Native interval: `36` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[88];
    unsigned int field_58;
} struct_0;

void bl_IconItem_DelayStart(struct_0 *ptr)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    unsigned int v4;  // s0
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    ptr->field_58 = v4;
    bl_IconItem__FadeIcon(ptr);
    MonoBehaviour__StartCoroutine();
    return;
}
```

## `bl_IconItem.ctor` — RVA `0xcc623c`

- Decompiled symbol: `bl_IconItem_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `28` bytes
- Result: `pseudocode`

```c
long long bl_IconItem_ctor(unsigned int *ptr)
{
    long long v0;  // x0

    ptr[8] = 0x40a00000;
    ptr[22] = 1036831949;
    v0 = MonoBehaviour__ctor();
    return MonoBehaviour__ctor();
}
```

## `bl_IconItem.<FadeIcon>d__16.Dispose` — RVA `0xcc6258`

- Decompiled symbol: `bl_IconItem_FadeIcon_d__16_Dispose`
- Metadata signature: `private void System.IDisposable.Dispose() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long bl_IconItem_FadeIcon_d__16_Dispose(void)
{
    unsigned long v0;  // x0

    return v0;
}
```

## `bl_IconItem.<FadeIcon>d__16.MoveNext` — RVA `0xcc625c`

- Decompiled symbol: `bl_IconItem_FadeIcon_d__16_MoveNext`
- Metadata signature: `private bool MoveNext() { }`
- Native interval: `376` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[4];
    long long field_18;
    struct struct_2 *field_20;
} struct_1;

typedef struct struct_2 {
    char padding_0[72];
    long long field_48;
    long long field_50;
} struct_2;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern long long g_1ef2440;
extern char g_1fab549;

unsigned int bl_IconItem_FadeIcon_d__16_MoveNext(struct_1 *ptr)
{
    long long p[11];  // x20
    unsigned int v1;  // s0
    unsigned long v2;  // 4125
    long long v3;  // x20
    struct_1 *addr;  // x19
    long long v5;  // x20
    struct_1 *ptr3;  // x19

    if (!(g_1fab549 & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c(&g_1ef2440);
        g_1fab549 = 1;
    }
    p = ptr->field_20;
    if (2 > ptr->field_10 - 1)
    {
        ptr->field_10 = 4294967295;
        if (p && p[9])
        {
            CanvasGroup__get_alpha(p[9], 0);
            v2 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v1, 0x3f800000)) >> 5 & 3 | (unsigned long long)(CmpF(v1, 0x3f800000) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v1, 0x3f800000)) >> 5 & 3 | (unsigned long long)(CmpF(v1, 0x3f800000) & 1)) & ((unsigned long long)(char)(CmpF(v1, 0x3f800000)) >> 5 & 3 | (unsigned long long)(CmpF(v1, 0x3f800000) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
            if (!((char)v2))
            {
                v3 = p[9];
                if (v3)
                {
                    CanvasGroup__get_alpha(v3, 0);
                    Time__get_deltaTime(0);
                    CanvasGroup__set_alpha(v3, 0);
                    ptr->field_18 = 0;
                    addr = &ptr->field_18;
                    sub_f7d8d0(addr, 0);
                    *((unsigned int *)&addr->padding_0[8]) = 2;
                    return 1;
                }
            }
            else
            {
                if (!g_1ef0c58->field_e0)
                    sub_f7da5c(g_1ef0c58);
                if (!((char)Object__op_Inequality(p[10], 0, 0) & 1))
                    return 0;
                if (p[10])
                {
                    Behaviour__set_enabled(p[10], 1, 0);
                    return 0;
                }
            }
        }
    }
    else if (!ptr->field_10)
    {
        ptr->field_10 = 4294967295;
        if (p)
        {
            v5 = sub_f7db70(g_1ef2440);
            WaitForSeconds__ctor(v5, 0);
            ptr->field_18 = v5;
            ptr3 = &ptr->field_18;
            sub_f7d8d0(ptr3, v5);
            *((unsigned int *)&ptr3->padding_0[8]) = 1;
            return 1;
        }
    }
    else
    {
        return 0;
    }
    sub_f7db74();
}
```

## `bl_IconItem.<FadeIcon>d__16.get_Current` — RVA `0xcc63d4`

- Decompiled symbol: `bl_IconItem_FadeIcon_d__16_get_Current`
- Metadata signature: `private object System.Collections.Generic.IEnumerator<System.Object>.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long bl_IconItem_FadeIcon_d__16_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```

## `bl_IconItem.<FadeIcon>d__16.Reset` — RVA `0xcc63dc`

- Decompiled symbol: `bl_IconItem_FadeIcon_d__16_Reset`
- Metadata signature: `private void System.Collections.IEnumerator.Reset() { }`
- Native interval: `56` bytes
- Result: `pseudocode`

```c
extern long long g_1ef0bd8;
extern long long g_1f054c8;

void bl_IconItem_FadeIcon_d__16_Reset(void)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    long long v4;  // x0
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    v4 = sub_f7db70(sub_f7d940(&g_1ef0bd8));
    NotSupportedException__ctor(v4, 0);
    sub_f7da4c(v4, sub_f7d940(&g_1f054c8));
}
```

## `bl_IconItem.<FadeIcon>d__16.get_Current` — RVA `0xcc6414`

- Decompiled symbol: `bl_IconItem_FadeIcon_d__16_get_Current`
- Metadata signature: `private object System.Collections.IEnumerator.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long bl_IconItem_FadeIcon_d__16_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```
