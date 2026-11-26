# Native pseudocode: CFCursor

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `CFCursor.InternalRefresh` — RVA `0xc3576c`

- Decompiled symbol: `CFCursor_InternalRefresh`
- Metadata signature: `public static void InternalRefresh() { }`
- Native interval: `392` bytes
- Result: `pseudocode`

```c
typedef struct struct_5 {
    char padding_0[184];
    struct struct_4 *field_b8;
    char padding_c0[32];
    unsigned int field_e0;
} struct_5;

typedef struct struct_2 {
    char padding_0[184];
    struct struct_1 *field_b8;
    char padding_c0[32];
    unsigned int field_e0;
} struct_2;

typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

typedef struct struct_4 {
    struct struct_3 *field_0;
    unsigned int field_8;
    char field_c;
} struct_4;

typedef struct struct_1 {
    struct struct_0 *field_0;
    unsigned int field_8;
    char field_c;
} struct_1;

typedef struct struct_3 {
    char padding_0[24];
    unsigned long long field_18;
} struct_3;

extern struct_2 *g_1eeed08;
extern char g_1fab189;

struct_5 * CFCursor_InternalRefresh(void)
{
    struct_2 *v0;  // x0
    unsigned long long v1;  // x19
    struct_0 *v9;  // x8
    unsigned long long v10;  // x0
    unsigned int v2;  // w0
    unsigned int v3;  // w0
    unsigned int v4;  // w0
    unsigned int v5;  // w0
    struct_2 *idx;  // x0
    unsigned int v7;  // w8
    unsigned int v8;  // w10

    if (!(g_1fab189 & 1))
    {
        sub_f7d92c(&g_1eeed08);
        g_1fab189 = 1;
    }
    v0 = g_1eeed08;
    if (!g_1eeed08->field_e0)
        v0 = sub_f7da5c(g_1eeed08);
    v1 = CFCursor__IsCursorLockingAllowed(v0) & 4294967295;
    if (!g_1eeed08->field_e0)
    {
        sub_f7da5c(g_1eeed08);
        if (!((char)v1 & 1))
        {
LABEL_10358c4:
            Cursor__set_lockState(0, 0);
            v10 = Cursor__set_visible();
            return Cursor__set_visible();
        }
    }
    else if (!(v1 & 1))
    {
        goto LABEL_10358c4;
    }
    v2 = Cursor__get_lockState(0);
    v3 = Cursor__get_visible(0);
    Cursor__set_lockState(g_1eeed08->field_b8->field_8, 0);
    Cursor__set_visible(g_1eeed08->field_b8->field_c, 0);
    v4 = Cursor__get_lockState(0);
    g_1eeed08->field_b8->field_8 = v4;
    v5 = Cursor__get_visible(0);
    idx = g_1eeed08;
    v7 = v5 & 1;
    v8 = g_1eeed08->field_b8->field_8;
    g_1eeed08->field_b8->field_c = v7;
    if (v8 == v2)
    {
        if (!g_1eeed08->field_e0)
        {
            sub_f7da5c();
            idx = g_1eeed08;
            v7 = g_1eeed08->field_b8->field_c;
        }
        if (v7 == (v3 & 1))
            return idx;
    }
    if (!idx->field_e0)
    {
        sub_f7da5c();
        idx = g_1eeed08;
    }
    v9 = idx->field_b8->field_0;
    if (!idx->field_b8->field_0)
        return idx;
    if (!idx->field_e0)
    {
        sub_f7da5c();
        v9 = g_1eeed08->field_b8->field_0;
        if (!v9)
            sub_f7db74();
    }
    goto v9->field_18;
}
```

## `CFCursor.add_onLockStateChange` — RVA `0xc382e4`

- Decompiled symbol: `CFCursor_add_onLockStateChange`
- Metadata signature: `public static void add_onLockStateChange(Action value) { }`
- Native interval: `216` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[184];
    struct struct_1 *field_b8;
    char padding_c0[32];
    unsigned int field_e0;
} struct_0;

typedef struct struct_1 {
    long long field_0;
} struct_1;

extern struct_0 *g_1eeed08;
extern char g_1fab181;

long long CFCursor_add_onLockStateChange(long long a0)
{
    struct_0 *idx;  // x0
    long long v1;  // x20
    long long v2;  // x20
    long long v3;  // x21
    struct_0 *v4;  // x0
    long long v5;  // x20

    if (!(g_1fab181 & 1))
    {
        sub_f7d92c("++");
        sub_f7d92c(&g_1eeed08);
        g_1fab181 = 1;
    }
    idx = g_1eeed08;
    if (!g_1eeed08->field_e0)
    {
        sub_f7da5c(g_1eeed08);
        idx = g_1eeed08;
    }
    v1 = idx->field_b8->field_0;
    while (true)
    {
        v2 = v1;
        v3 = Delegate__Combine(v2, a0, 0);
        if (v3 && *((long long *)v3) != g_1eee648)
            sub_f7df10(v3);
        v4 = g_1eeed08;
        if (!g_1eeed08->field_e0)
        {
            sub_f7da5c(g_1eeed08);
            v4 = g_1eeed08;
        }
        v5 = sub_f60ebc(v4->field_b8, v3, v2);
        v1 = v5;
        if (v2 == v1)
            return v5;
    }
}
```

## `CFCursor.remove_onLockStateChange` — RVA `0xc383bc`

- Decompiled symbol: `CFCursor_remove_onLockStateChange`
- Metadata signature: `public static void remove_onLockStateChange(Action value) { }`
- Native interval: `216` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[184];
    struct struct_1 *field_b8;
    char padding_c0[32];
    unsigned int field_e0;
} struct_0;

typedef struct struct_1 {
    long long field_0;
} struct_1;

extern struct_0 *g_1eeed08;
extern char g_1fab182;

long long CFCursor_remove_onLockStateChange(long long a0)
{
    struct_0 *idx;  // x0
    long long v1;  // x20
    long long v2;  // x20
    long long v3;  // x21
    struct_0 *v4;  // x0
    long long v5;  // x20

    if (!(g_1fab182 & 1))
    {
        sub_f7d92c("++");
        sub_f7d92c(&g_1eeed08);
        g_1fab182 = 1;
    }
    idx = g_1eeed08;
    if (!g_1eeed08->field_e0)
    {
        sub_f7da5c(g_1eeed08);
        idx = g_1eeed08;
    }
    v1 = idx->field_b8->field_0;
    while (true)
    {
        v2 = v1;
        v3 = Delegate__Remove(v2, a0, 0);
        if (v3 && *((long long *)v3) != g_1eee648)
            sub_f7df10(v3);
        v4 = g_1eeed08;
        if (!g_1eeed08->field_e0)
        {
            sub_f7da5c(g_1eeed08);
            v4 = g_1eeed08;
        }
        v5 = sub_f60ebc(v4->field_b8, v3, v2);
        v1 = v5;
        if (v2 == v1)
            return v5;
    }
}
```

## `CFCursor.cctor` — RVA `0xc38494`

- Decompiled symbol: `CFCursor_cctor`
- Metadata signature: `private static void .cctor() { }`
- Native interval: `80` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[8];
    unsigned int field_8;
    char field_c;
} struct_0;

typedef struct struct_1 {
    char padding_0[184];
    struct struct_0 *field_b8;
} struct_1;

extern struct_1 *g_1eeed08;
extern char g_1fab183;

unsigned long long CFCursor_cctor(void)
{
    unsigned long long v0;  // x0
    struct_0 *ptr;  // x8

    if (!(g_1fab183 & 1))
    {
        v0 = sub_f7d92c(&g_1eeed08);
        g_1fab183 = 1;
    }
    ptr = g_1eeed08->field_b8;
    ptr->field_8 = 0;
    ptr->field_c = 1;
    return v0;
}
```

## `CFCursor.set_lockState` — RVA `0xc384e4`

- Decompiled symbol: `CFCursor_set_lockState`
- Metadata signature: `public static void set_lockState(CursorLockMode value) { }`
- Native interval: `324` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    char padding_0[184];
    struct struct_1 *field_b8;
    char padding_c0[32];
    unsigned int field_e0;
} struct_2;

typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

typedef struct struct_1 {
    struct struct_0 *field_0;
    unsigned int field_8;
} struct_1;

extern struct_2 *g_1eeed08;
extern char g_1fab184;

unsigned long long CFCursor_set_lockState(unsigned int a0)
{
    struct_2 *idx;  // x0
    unsigned int v1;  // w22
    unsigned long long v2;  // x20
    unsigned long long v3;  // x0
    struct_2 *index;  // x8
    struct_0 *v5;  // x9

    if (!(g_1fab184 & 1))
    {
        sub_f7d92c(&g_1eeed08);
        g_1fab184 = 1;
    }
    idx = g_1eeed08;
    if (!g_1eeed08->field_e0)
    {
        sub_f7da5c(g_1eeed08);
        idx = g_1eeed08;
    }
    v1 = idx->field_b8->field_8;
    idx->field_b8->field_8 = a0;
    v2 = CFCursor__IsCursorLockingAllowed(idx) & 4294967295;
    if (g_1eeed08->field_e0)
    {
        if (!(v2 & 1))
            goto LABEL_1038584;
LABEL_1038554:
        Cursor__set_lockState(a0, 0);
        v3 = Cursor__get_lockState(0);
        index = g_1eeed08;
        g_1eeed08->field_b8->field_8 = v3;
    }
    else
    {
        sub_f7da5c(g_1eeed08);
        if ((v2 & 1))
            goto LABEL_1038554;
LABEL_1038584:
        v3 = Cursor__set_lockState(0, 0);
        index = g_1eeed08;
    }
    if (!index->field_e0)
    {
        v3 = sub_f7da5c(index);
        index = g_1eeed08;
    }
    if (v1 == index->field_b8->field_8)
        return v3;
    if (!index->field_e0)
    {
        v3 = sub_f7da5c(index);
        index = g_1eeed08;
    }
    v5 = index->field_b8->field_0;
    if (!index->field_b8->field_0)
        return v3;
    if (!index->field_e0)
    {
        sub_f7da5c(index);
        v5 = g_1eeed08->field_b8->field_0;
        if (!v5)
            sub_f7db74();
    }
    goto v5->field_18;
}
```

## `CFCursor.IsCursorLockingAllowed` — RVA `0xc38628`

- Decompiled symbol: `CFCursor_IsCursorLockingAllowed`
- Metadata signature: `private static bool IsCursorLockingAllowed() { }`
- Native interval: `232` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[184];
    struct struct_0 *field_b8;
    char padding_c0[32];
    unsigned int field_e0;
} struct_1;

typedef struct struct_0 {
    char padding_0[24];
    long long field_18;
} struct_0;

typedef struct struct_2 {
    char padding_0[224];
    unsigned int field_e0;
} struct_2;

extern struct_1 *g_1eeed00;
extern struct_2 *g_1ef0c58;
extern char g_1fab188;
extern char g_1fab1df;

unsigned int CFCursor_IsCursorLockingAllowed(void)
{
    struct_1 *v0;  // x0
    unsigned int v1;  // w8

    if (!(g_1fab188 & 1))
    {
        sub_f7d92c(&g_1eeed00);
        sub_f7d92c(&g_1ef0c58);
        g_1fab188 = 1;
    }
    if (!g_1eeed00->field_e0)
        sub_f7da5c(g_1eeed00);
    if (!g_1fab1df)
    {
        sub_f7d92c(&g_1eeed00);
        g_1fab1df = 1;
    }
    v0 = g_1eeed00;
    if (!g_1eeed00->field_e0)
    {
        sub_f7da5c(g_1eeed00);
        v0 = g_1eeed00;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (((char)Object__op_Inequality(v0->field_b8->field_18, 0, 0) & 1))
    {
        if (!g_1eeed00->field_e0)
            sub_f7da5c(g_1eeed00);
        v1 = CF2Input__IsInMobileMode() ^ 1;
    }
    else
    {
        v1 = 1;
    }
    return v1 & 1;
}
```

## `CFCursor.InternalSetLockMode` — RVA `0xc38710`

- Decompiled symbol: `CFCursor_InternalSetLockMode`
- Metadata signature: `private static void InternalSetLockMode(CursorLockMode mode) { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long CFCursor_InternalSetLockMode(void)
{
    unsigned long long v0;  // x0

    v0 = Cursor__set_lockState();
    return Cursor__set_lockState();
}
```

## `CFCursor.InternalGetLockMode` — RVA `0xc38718`

- Decompiled symbol: `CFCursor_InternalGetLockMode`
- Metadata signature: `private static CursorLockMode InternalGetLockMode() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
void CFCursor_InternalGetLockMode(void)
{
    Cursor__get_lockState();
    return;
}
```

## `CFCursor.get_lockState` — RVA `0xc38720`

- Decompiled symbol: `CFCursor_get_lockState`
- Metadata signature: `public static CursorLockMode get_lockState() { }`
- Native interval: `252` bytes
- Result: `pseudocode`

```c
typedef struct struct_3 {
    char padding_0[184];
    struct struct_2 *field_b8;
    char padding_c0[32];
    unsigned int field_e0;
} struct_3;

typedef struct struct_0 {
    char padding_0[24];
    struct struct_1 *field_18;
    char padding_20[8];
    unsigned long long field_28;
    char padding_30[16];
    unsigned long long field_40;
} struct_0;

typedef struct struct_2 {
    struct struct_0 *field_0;
    unsigned int field_8;
} struct_2;

typedef struct struct_1 {
    unsigned long long field_0;
} struct_1;

extern struct_3 *g_1eeed08;
extern char g_1fab185;

unsigned int CFCursor_get_lockState(void)
{
    struct_3 *v0;  // x0
    unsigned int v1;  // w0
    unsigned int v2;  // w0
    struct_3 *index;  // x8
    struct_0 *v4;  // x10
    struct_0 *ptr;  // x8
    unsigned long long v6;  // x0
    unsigned long long v7;  // x1
    struct_3 *v8;  // x0

    if (!(g_1fab185 & 1))
    {
        sub_f7d92c(&g_1eeed08);
        g_1fab185 = 1;
    }
    if (!g_1eeed08->field_e0)
        sub_f7da5c(g_1eeed08);
    if (((char)CFCursor__IsCursorLockingAllowed() & 1))
    {
        v0 = g_1eeed08;
        if (!g_1eeed08->field_e0)
        {
            sub_f7da5c(g_1eeed08);
            v0 = g_1eeed08;
        }
        v1 = Cursor__get_lockState(0);
        if (v0->field_b8->field_8 != v1)
        {
            if (!g_1eeed08->field_e0)
                sub_f7da5c(g_1eeed08);
            v2 = Cursor__get_lockState(0);
            index = g_1eeed08;
            v4 = g_1eeed08->field_b8->field_0;
            g_1eeed08->field_b8->field_8 = v2;
            if (v4)
            {
                if (!g_1eeed08->field_e0)
                {
                    sub_f7da5c(g_1eeed08);
                    index = g_1eeed08;
                }
                ptr = index->field_b8->field_0;
                if (!ptr)
                    sub_f7db74();
                v6 = ptr->field_40;
                v7 = ptr->field_28;
                ptr->field_18();
            }
        }
    }
    v8 = g_1eeed08;
    if (!g_1eeed08->field_e0)
    {
        sub_f7da5c(g_1eeed08);
        v8 = g_1eeed08;
    }
    return v8->field_b8->field_8;
}
```

## `CFCursor.set_visible` — RVA `0xc3881c`

- Decompiled symbol: `CFCursor_set_visible`
- Metadata signature: `public static void set_visible(bool value) { }`
- Native interval: `144` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[184];
    struct struct_0 *field_b8;
    char padding_c0[32];
    unsigned int field_e0;
} struct_1;

typedef struct struct_0 {
    char padding_0[12];
    char field_c;
} struct_0;

extern struct_1 *g_1eeed08;
extern char g_1fab186;

void CFCursor_set_visible(char a0)
{
    unsigned long long v5;  // x30
    unsigned long long v6;  // x22
    unsigned long long v7;  // x21
    unsigned long long v8;  // x20
    unsigned long long v9;  // x19
    struct_1 *idx;  // x0
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
    if (!(g_1fab186 & 1))
    {
        sub_f7d92c(&g_1eeed08);
        g_1fab186 = 1;
    }
    idx = g_1eeed08;
    if (!g_1eeed08->field_e0)
    {
        sub_f7da5c(g_1eeed08);
        idx = g_1eeed08;
    }
    idx->field_b8->field_c = a0 & 1;
    CFCursor__IsCursorLockingAllowed();
    if (!g_1eeed08->field_e0)
        sub_f7da5c(g_1eeed08);
    Cursor__set_visible();
    return;
}
```

## `CFCursor.InternalSetVisible` — RVA `0xc388ac`

- Decompiled symbol: `CFCursor_InternalSetVisible`
- Metadata signature: `private static void InternalSetVisible(bool visible) { }`
- Native interval: `12` bytes
- Result: `pseudocode`

```c
void CFCursor_InternalSetVisible(unsigned long a0)
{
    Cursor__set_visible();
    return;
}
```

## `CFCursor.get_visible` — RVA `0xc388b8`

- Decompiled symbol: `CFCursor_get_visible`
- Metadata signature: `public static bool get_visible() { }`
- Native interval: `164` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[12];
    char field_c;
} struct_0;

typedef struct struct_1 {
    char padding_0[184];
    struct struct_0 *field_b8;
    char padding_c0[32];
    unsigned int field_e0;
} struct_1;

extern struct_1 *g_1eeed08;
extern char g_1fab187;

unsigned int CFCursor_get_visible(void)
{
    unsigned long long v0;  // x19
    unsigned int v1;  // w0

    if (!(g_1fab187 & 1))
    {
        sub_f7d92c(&g_1eeed08);
        g_1fab187 = 1;
    }
    if (!g_1eeed08->field_e0)
        sub_f7da5c(g_1eeed08);
    v0 = CFCursor__IsCursorLockingAllowed() & 4294967295;
    if (g_1eeed08->field_e0)
    {
        if (!(v0 & 1))
            goto LABEL_1038938;
LABEL_1038910:
        v1 = Cursor__get_visible(0);
        g_1eeed08->field_b8->field_c = (char)v1 & 1;
    }
    else
    {
        sub_f7da5c(g_1eeed08);
        if ((v0 & 1))
            goto LABEL_1038910;
LABEL_1038938:
        if (!g_1eeed08->field_b8->field_c)
            v1 = 0;
        else
            v1 = 1;
    }
    return v1 & 1;
}
```

## `CFCursor.InternalIsVisible` — RVA `0xc3895c`

- Decompiled symbol: `CFCursor_InternalIsVisible`
- Metadata signature: `private static bool InternalIsVisible() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
void CFCursor_InternalIsVisible(void)
{
    Cursor__get_visible();
    return;
}
```

## `CFCursor.SetCursor` — RVA `0xc38964`

- Decompiled symbol: `CFCursor_SetCursor`
- Metadata signature: `public static void SetCursor(Texture2D tex, Vector2 hotSpot, CursorMode mode) { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long CFCursor_SetCursor(void)
{
}
```
