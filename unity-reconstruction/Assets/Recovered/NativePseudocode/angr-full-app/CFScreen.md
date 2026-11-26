# Native pseudocode: CFScreen

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `CFScreen.get_dpi` — RVA `0xc3896c`

- Decompiled symbol: `CFScreen_get_dpi`
- Metadata signature: `public static float get_dpi() { }`
- Native interval: `92` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1eeed10;
extern char g_1fab18a;

long long CFScreen_get_dpi(void)
{
    struct_0 *v0;  // x0
    unsigned long long v1;  // x0

    if (!(g_1fab18a & 1))
    {
        sub_f7d92c(&g_1eeed10);
        g_1fab18a = 1;
    }
    v0 = g_1eeed10;
    if (!g_1eeed10->field_e0)
        v0 = sub_f7da5c(g_1eeed10);
    v1 = CFScreen__UpdateDpiIfNeeded(v0);
    return CFScreen__UpdateDpiIfNeeded(v0);
}
```

## `CFScreen.UpdateDpiIfNeeded` — RVA `0xc389c8`

- Decompiled symbol: `CFScreen_UpdateDpiIfNeeded`
- Metadata signature: `private static void UpdateDpiIfNeeded() { }`
- Native interval: `380` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[184];
    struct struct_0 *field_b8;
    char padding_c0[32];
    unsigned int field_e0;
} struct_1;

typedef struct struct_0 {
    char padding_0[4];
    char field_4;
    char padding_5[39];
    unsigned int field_2c;
    unsigned int field_30;
    unsigned int field_34;
} struct_0;

extern struct_1 *g_1eeed10;
extern char g_1fab196;

unsigned long long CFScreen_UpdateDpiIfNeeded(unsigned long a0, unsigned long long a1)
{
    unsigned long v2;  // x0
    struct_1 *index;  // x0
    unsigned int v12;  // s8
    unsigned long long v13;  // 4102
    unsigned int v14;  // w0
    struct_1 *v15;  // x8
    unsigned int v16;  // w0
    struct_1 *v17;  // x8
    unsigned long long v18;  // x0
    struct_1 *v19;  // x0
    unsigned long long v20;  // x0
    unsigned int v4;  // s8
    unsigned int v5;  // w0
    unsigned long long v6;  // 4104
    struct_1 *pos;  // x0
    unsigned int v8;  // s8
    unsigned int v9;  // s0
    unsigned long long v10;  // 4104
    struct_1 *idx;  // x0
    unsigned long v0;  // [bp-0x30]
    unsigned long long v1;  // [bp-0x28]

    if (!(g_1fab196 & 1))
    {
        sub_f7d92c(&g_1eeed10);
        g_1fab196 = 1;
    }
    v2 = Screen__get_currentResolution(0);
    index = g_1eeed10;
    v0 = v2;
    v1 = a1;
    if (!g_1eeed10->field_e0)
    {
        sub_f7da5c(g_1eeed10);
        index = g_1eeed10;
    }
    v4 = index->field_b8->field_2c;
    v5 = Screen__get_width(0);
    v6 = (((CmpF(v4, v5) >> 5 & 3 | CmpF(v4, v5) & 1) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - ((CmpF(v4, v5) >> 5 & 3 | CmpF(v4, v5) & 1) & (CmpF(v4, v5) >> 5 & 3 | CmpF(v4, v5) & 1) >> 1 & 1);
    if ((char)(v6 * 0x10000000 >> 30))
    {
        pos = g_1eeed10;
        if (!g_1eeed10->field_e0)
        {
            sub_f7da5c(g_1eeed10);
            pos = g_1eeed10;
        }
        v8 = pos->field_b8->field_30;
        v9 = Screen__get_height(0);
        v10 = (((CmpF(v8, v9) >> 5 & 3 | CmpF(v8, v9) & 1) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - ((CmpF(v8, v9) >> 5 & 3 | CmpF(v8, v9) & 1) & (CmpF(v8, v9) >> 5 & 3 | CmpF(v8, v9) & 1) >> 1 & 1);
        if ((char)(v10 * 0x10000000 >> 30))
        {
            idx = g_1eeed10;
            if (!g_1eeed10->field_e0)
            {
                sub_f7da5c(g_1eeed10);
                idx = g_1eeed10;
            }
            v12 = idx->field_b8->field_34;
            Screen__get_dpi(0);
            v13 = (((CmpF(v12, v9) >> 5 & 3 | CmpF(v12, v9) & 1) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - ((CmpF(v12, v9) >> 5 & 3 | CmpF(v12, v9) & 1) & (CmpF(v12, v9) >> 5 & 3 | CmpF(v12, v9) & 1) >> 1 & 1);
            if ((char)(v13 * 0x10000000 >> 30))
            {
                v14 = Resolution__get_width(&v0, 0);
                v15 = g_1eeed10;
                if (!g_1eeed10->field_e0)
                {
                    sub_f7da5c(g_1eeed10);
                    v15 = g_1eeed10;
                }
                if (v14 == (int)Resolution__get_width((struct struct_0 *)&v15->field_b8->field_4, 0))
                {
                    v16 = Resolution__get_height(&v0, 0);
                    v17 = g_1eeed10;
                    if (!g_1eeed10->field_e0)
                    {
                        sub_f7da5c(g_1eeed10);
                        v17 = g_1eeed10;
                    }
                    v18 = Resolution__get_height((struct struct_0 *)&v17->field_b8->field_4, 0);
                    if (v16 == (unsigned int)v18)
                        return v18;
                }
            }
        }
    }
    v19 = g_1eeed10;
    if (!g_1eeed10->field_e0)
        v19 = sub_f7da5c(g_1eeed10);
    v20 = CFScreen__UpdateDpi(v19);
    return CFScreen__UpdateDpi(v19);
}
```

## `CFScreen.get_dpcm` — RVA `0xc38b44`

- Decompiled symbol: `CFScreen_get_dpcm`
- Metadata signature: `public static float get_dpcm() { }`
- Native interval: `92` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1eeed10;
extern char g_1fab18b;

unsigned long long CFScreen_get_dpcm(unsigned long a0, unsigned long long a1)
{
    struct_0 *v0;  // x0
    unsigned long long v1;  // x0

    if (!(g_1fab18b & 1))
    {
        sub_f7d92c(&g_1eeed10);
        g_1fab18b = 1;
    }
    v0 = g_1eeed10;
    if (!g_1eeed10->field_e0)
        v0 = sub_f7da5c(g_1eeed10);
    v1 = CFScreen__UpdateDpiIfNeeded(v0, a1);
    return CFScreen__UpdateDpiIfNeeded(v0, a1);
}
```

## `CFScreen.get_invDpi` — RVA `0xc38ba0`

- Decompiled symbol: `CFScreen_get_invDpi`
- Metadata signature: `public static float get_invDpi() { }`
- Native interval: `92` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1eeed10;
extern char g_1fab18c;

unsigned long long CFScreen_get_invDpi(unsigned long a0, unsigned long long a1)
{
    struct_0 *v0;  // x0
    unsigned long long v1;  // x0

    if (!(g_1fab18c & 1))
    {
        sub_f7d92c(&g_1eeed10);
        g_1fab18c = 1;
    }
    v0 = g_1eeed10;
    if (!g_1eeed10->field_e0)
        v0 = sub_f7da5c(g_1eeed10);
    v1 = CFScreen__UpdateDpiIfNeeded(v0, a1);
    return CFScreen__UpdateDpiIfNeeded(v0, a1);
}
```

## `CFScreen.get_invDpcm` — RVA `0xc38bfc`

- Decompiled symbol: `CFScreen_get_invDpcm`
- Metadata signature: `public static float get_invDpcm() { }`
- Native interval: `92` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1eeed10;
extern char g_1fab18d;

unsigned long long CFScreen_get_invDpcm(unsigned long a0, unsigned long long a1)
{
    struct_0 *v0;  // x0
    unsigned long long v1;  // x0

    if (!(g_1fab18d & 1))
    {
        sub_f7d92c(&g_1eeed10);
        g_1fab18d = 1;
    }
    v0 = g_1eeed10;
    if (!g_1eeed10->field_e0)
        v0 = sub_f7da5c(g_1eeed10);
    v1 = CFScreen__UpdateDpiIfNeeded(v0, a1);
    return CFScreen__UpdateDpiIfNeeded(v0, a1);
}
```

## `CFScreen.get_width` — RVA `0xc38c58`

- Decompiled symbol: `CFScreen_get_width`
- Metadata signature: `public static float get_width() { }`
- Native interval: `24` bytes
- Result: `pseudocode`

```c
int CFScreen_get_width(void)
{
    return Screen__get_width(0);
}
```

## `CFScreen.get_height` — RVA `0xc38c70`

- Decompiled symbol: `CFScreen_get_height`
- Metadata signature: `public static float get_height() { }`
- Native interval: `24` bytes
- Result: `pseudocode`

```c
int CFScreen_get_height(void)
{
    return Screen__get_height(0);
}
```

## `CFScreen.get_lockCursor` — RVA `0xc38c88`

- Decompiled symbol: `CFScreen_get_lockCursor`
- Metadata signature: `public static bool get_lockCursor() { }`
- Native interval: `88` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1eeed08;
extern char g_1fab18e;

unsigned long long CFScreen_get_lockCursor(void)
{
    unsigned long long v1;  // x30
    unsigned long long v0;  // [bp-0x20]

    v0 = v1;
    if (!(g_1fab18e & 1))
    {
        sub_f7d92c(&g_1eeed08);
        g_1fab18e = 1;
    }
    if (!g_1eeed08->field_e0)
        sub_f7da5c(g_1eeed08);
    if (CFCursor__get_lockState() == 1)
        return 1;
    return 0;
}
```

## `CFScreen.set_lockCursor` — RVA `0xc38ce0`

- Decompiled symbol: `CFScreen_set_lockCursor`
- Metadata signature: `public static void set_lockCursor(bool value) { }`
- Native interval: `84` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1eeed08;
extern char g_1fab18f;

unsigned long long CFScreen_set_lockCursor(unsigned int a0)
{
    unsigned long long v0;  // x0

    if (!(g_1fab18f & 1))
    {
        sub_f7d92c(&g_1eeed08);
        g_1fab18f = 1;
    }
    if (!g_1eeed08->field_e0)
        sub_f7da5c(g_1eeed08);
    v0 = CFCursor__set_lockState(a0 & 1);
    return CFCursor__set_lockState(a0 & 1);
}
```

## `CFScreen.get_showCursor` — RVA `0xc38d34`

- Decompiled symbol: `CFScreen_get_showCursor`
- Metadata signature: `public static bool get_showCursor() { }`
- Native interval: `76` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1eeed08;
extern char g_1fab190;

unsigned int CFScreen_get_showCursor(void)
{
    if (!(g_1fab190 & 1))
    {
        sub_f7d92c(&g_1eeed08);
        g_1fab190 = 1;
    }
    if (!g_1eeed08->field_e0)
        sub_f7da5c(g_1eeed08);
    return CFCursor__get_visible();
}
```

## `CFScreen.set_showCursor` — RVA `0xc38d80`

- Decompiled symbol: `CFScreen_set_showCursor`
- Metadata signature: `public static void set_showCursor(bool value) { }`
- Native interval: `84` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1eeed08;
extern char g_1fab191;

void CFScreen_set_showCursor(char a0)
{
    if (!(g_1fab191 & 1))
    {
        sub_f7d92c(&g_1eeed08);
        g_1fab191 = 1;
    }
    if (!g_1eeed08->field_e0)
        sub_f7da5c(g_1eeed08);
    CFCursor__set_visible(a0 & 1); /* do not return */
}
```

## `CFScreen.get_fullScreen` — RVA `0xc38dd4`

- Decompiled symbol: `CFScreen_get_fullScreen`
- Metadata signature: `public static bool get_fullScreen() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
void CFScreen_get_fullScreen(void)
{
}
```

## `CFScreen.set_fullScreen` — RVA `0xc38ddc`

- Decompiled symbol: `CFScreen_set_fullScreen`
- Metadata signature: `public static void set_fullScreen(bool value) { }`
- Native interval: `92` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1eeed10;
extern char g_1fab192;

void CFScreen_set_fullScreen(unsigned long a0)
{
    unsigned long long v4;  // x30
    unsigned long long v5;  // x21
    unsigned long long v6;  // x20
    unsigned long long v7;  // x19
    struct_0 *v8;  // x0
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x18]
    unsigned long long v2;  // [bp-0x10]
    unsigned long long v3;  // [bp-0x8]

    v0 = v4;
    v1 = v5;
    v2 = v6;
    v3 = v7;
    if (!(g_1fab192 & 1))
    {
        sub_f7d92c(&g_1eeed10);
        g_1fab192 = 1;
    }
    v8 = g_1eeed10;
    if (!g_1eeed10->field_e0)
        v8 = sub_f7da5c(g_1eeed10);
    CFScreen__UpdateDpi(v8);
}
```

## `CFScreen.UpdateDpi` — RVA `0xc38e38`

- Decompiled symbol: `CFScreen_UpdateDpi`
- Metadata signature: `public static void UpdateDpi() { }`
- Native interval: `980` bytes
- Result: `pseudocode`

```c
typedef struct struct_3 {
    char padding_0[184];
    struct struct_2 *field_b8;
} struct_3;

typedef struct struct_1 {
    char padding_0[184];
    struct struct_0 *field_b8;
} struct_1;

typedef struct struct_0 {
    char padding_0[4];
    uint128_t field_4;
    uint128_t field_14;
    unsigned int field_24;
    unsigned int field_28;
    unsigned int field_2c;
    unsigned int field_30;
    unsigned int field_34;
    unsigned int field_38;
    unsigned int field_3c;
    unsigned int field_40;
    unsigned int field_44;
    unsigned int field_48;
} struct_0;

typedef struct struct_2 {
    char padding_0[4];
    uint128_t field_4;
    uint128_t field_14;
    unsigned int field_24;
    unsigned int field_28;
    unsigned int field_2c;
    unsigned int field_30;
    unsigned int field_34;
    unsigned int field_38;
    unsigned int field_3c;
    unsigned int field_40;
    unsigned int field_44;
    unsigned int field_48;
} struct_2;

extern struct_1 *g_1eeed10;
extern char g_1fab197;

struct_3 * CFScreen_UpdateDpi(unsigned long a0, unsigned long a1)
{
    unsigned long long v2;  // x0
    struct_1 *idx5;  // x0
    unsigned int v12;  // s0
    struct_0 *p;  // x8
    unsigned int v14;  // s1
    struct_1 *v15;  // x0
    struct_0 *addr;  // x8
    unsigned int v17;  // s8
    unsigned int v18;  // s0
    unsigned long v19;  // 4240
    unsigned int v20;  // s0
    unsigned long v21;  // 4125
    unsigned int v4;  // s8
    struct_1 *v22;  // x0
    struct_1 *idx8;  // x0
    unsigned int v24;  // s9
    unsigned int v25;  // s0
    struct_1 *ptr3;  // x0
    unsigned long v27;  // 4129
    struct_0 *ptr4;  // x8
    struct_0 *ptr;  // x8
    unsigned int v30;  // s1
    unsigned int v31;  // s0
    unsigned int v5;  // s0
    unsigned long long v6;  // 4102
    struct_1 *v7;  // x0
    struct_1 *v8;  // x0
    struct_1 *idx7;  // x0
    unsigned int v10;  // w0
    struct_1 *idx6;  // x8
    int v0;  // [bp-0x60]
    int v1;  // [bp-0x50]

    if (!(g_1fab197 & 1))
    {
        sub_f7d92c(&g_1eeed10);
        g_1fab197 = 1;
    }
    v2 = Screen__get_currentResolution(0);
    idx5 = g_1eeed10;
    *((unsigned long long *)&v1) = v2;
    *((unsigned long *)&(&v1)[8]) = a1;
    if (!*((int *)&g_1eeed10[1].padding_0[32]))
    {
        sub_f7da5c(g_1eeed10);
        idx5 = g_1eeed10;
    }
    v4 = idx5->field_b8->field_28;
    Screen__get_dpi(0);
    v6 = (((CmpF(v4, v5) >> 5 & 3 | CmpF(v4, v5) & 1) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - ((CmpF(v4, v5) >> 5 & 3 | CmpF(v4, v5) & 1) & (CmpF(v4, v5) >> 5 & 3 | CmpF(v4, v5) & 1) >> 1 & 1);
    if ((char)(v6 * 0x10000000 >> 30))
    {
        v7 = g_1eeed10;
        if (!*((int *)&g_1eeed10[1].padding_0[32]))
        {
            sub_f7da5c(g_1eeed10);
            v7 = g_1eeed10;
        }
        if ((int)Resolution__get_width((struct struct_0 *)((char *)&v7->field_b8->field_4 + 4), 0) >= 1)
        {
            v8 = g_1eeed10;
            if (!*((int *)&g_1eeed10[1].padding_0[32]))
            {
                sub_f7da5c(g_1eeed10);
                v8 = g_1eeed10;
            }
            if (0 < (int)Resolution__get_height((struct struct_0 *)((char *)&v8->field_b8->field_4 + 4), 0))
                goto LABEL_1038f44;
        }
    }
    idx7 = g_1eeed10;
    memcpy(&v0, &v1, 16);
    if (!*((int *)&g_1eeed10[1].padding_0[32]))
    {
        sub_f7da5c(g_1eeed10);
        idx7 = g_1eeed10;
    }
    *((void*)((char *)&idx7->field_b8->field_4 + 4)) = v0;
    Screen__get_dpi(0);
    g_1eeed10->field_b8->field_2c = *((unsigned int *)&v0);
LABEL_1038f44:
    v10 = Screen__get_width(0);
    idx6 = g_1eeed10;
    if (!*((int *)&g_1eeed10[1].padding_0[32]))
    {
        sub_f7da5c(g_1eeed10);
        idx6 = g_1eeed10;
    }
    *((unsigned int *)((char *)&idx6->field_b8->field_14 + 12)) = v10;
    v12 = Screen__get_height(0);
    g_1eeed10->field_b8->field_24 = v12;
    Screen__get_dpi(0);
    p = g_1eeed10->field_b8;
    p->field_28 = v12;
    v14 = [D] unsupported_Iop_SqrtF32();
    *((unsigned int *)((char *)&p->field_14 + 4)) = v14 / *((int *)((char *)&p->field_14 + 8));
    *((void*)&(&p->padding_0)[1]) = v1;
    v15 = g_1eeed10;
    addr = g_1eeed10->field_b8;
    v17 = addr->field_28;
    v18 = addr->field_2c;
    v19 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v18, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v18, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v18, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v18, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v18, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v18, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if (!((char)v19))
    {
        if (*((int *)&g_1eeed10[1].padding_0[32]))
        {
            v20 = v17;
        }
        else
        {
            sub_f7da5c();
            v15 = g_1eeed10;
            addr = g_1eeed10->field_b8;
            v20 = addr->field_28;
        }
        v21 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v20, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v20, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v20, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v20, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v20, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v20, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if (!((char)v21))
        {
            if (!*((int *)&v15[1].padding_0[32]))
            {
                sub_f7da5c();
                addr = g_1eeed10->field_b8;
            }
            if ((int)Resolution__get_width((struct struct_0 *)((char *)&addr->field_4 + 4), 0) >= 1)
            {
                v22 = g_1eeed10;
                if (!*((int *)&g_1eeed10[1].padding_0[32]))
                {
                    sub_f7da5c(g_1eeed10);
                    v22 = g_1eeed10;
                }
                if ((int)Resolution__get_height((struct struct_0 *)((char *)&v22->field_b8->field_4 + 4), 0) >= 1 && (int)Resolution__get_width(&v1, 0) >= 1 && (int)Resolution__get_height(&v1, 0) >= 1)
                {
                    idx8 = g_1eeed10;
                    if (!*((int *)&g_1eeed10[1].padding_0[32]))
                    {
                        sub_f7da5c(g_1eeed10);
                        idx8 = g_1eeed10;
                    }
                    Resolution__get_width(&v1, 0);
                    Resolution__get_width(&v1, 0);
                    Resolution__get_height(&v1, 0);
                    Resolution__get_height(&v1, 0);
                    v24 = [D] unsupported_Iop_SqrtF32();
                    Resolution__get_width((struct struct_0 *)((char *)&g_1eeed10->field_b8->field_4 + 4), 0);
                    Resolution__get_width((struct struct_0 *)((char *)&g_1eeed10->field_b8->field_4 + 4), 0);
                    Resolution__get_height((struct struct_0 *)((char *)&g_1eeed10->field_b8->field_4 + 4), 0);
                    Resolution__get_height((struct struct_0 *)((char *)&g_1eeed10->field_b8->field_4 + 4), 0);
                    v25 = [D] unsupported_Iop_SqrtF32();
                    v17 = idx8->field_b8->field_2c * v24 / v25;
                }
            }
        }
    }
    ptr3 = g_1eeed10;
    v27 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(v17, 0x3f800000)) >> 5 & 3 | (unsigned long long)(CmpF(v17, 0x3f800000) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v17, 0x3f800000)) >> 5 & 3 | (unsigned long long)(CmpF(v17, 0x3f800000) & 1)) & ((unsigned long long)(char)(CmpF(v17, 0x3f800000)) >> 5 & 3 | (unsigned long long)(CmpF(v17, 0x3f800000) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if (!((char)v27))
    {
        if (!*((int *)&g_1eeed10[1].padding_0[32]))
        {
            sub_f7da5c();
            ptr3 = g_1eeed10;
        }
        ptr4 = ptr3->field_b8;
        if (ptr4->padding_0[0])
            goto LABEL_1039188;
        if (!*((int *)&ptr3[1].padding_0[32]))
        {
            sub_f7da5c();
            ptr3 = g_1eeed10;
            ptr4 = g_1eeed10->field_b8;
        }
    }
    else
    {
LABEL_1039188:
        if (!*((int *)&ptr3[1].padding_0[32]))
        {
            sub_f7da5c();
            ptr3 = g_1eeed10;
        }
        ptr4 = ptr3->field_b8;
        v17 = *((int *)((char *)&ptr4->field_14 + 4));
    }
    ptr4->field_30 = v17;
    if (!*((int *)&ptr3[1].padding_0[32]))
    {
        sub_f7da5c();
        ptr3 = g_1eeed10;
    }
    ptr = ptr3->field_b8;
    v30 = ptr->field_30;
    v31 = ptr->field_30 / 1076006748;
    ptr->field_34 = v31;
    ptr->field_38 = 0x3f800000 / v30;
    ptr->field_3c = 0x3f800000 / v31;
    return ptr3;
}
```

## `CFScreen.SetResolution` — RVA `0xc3920c`

- Decompiled symbol: `CFScreen_SetResolution`
- Metadata signature: `public static void SetResolution(int width, int height, bool fullScreen, int refreshRate = 0) { }`
- Native interval: `132` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1eeed10;
extern char g_1fab193;

void CFScreen_SetResolution(unsigned long a0, unsigned int a1, unsigned long a2, unsigned long a3)
{
    unsigned long long v7;  // x30
    unsigned long long v8;  // x24
    unsigned long long v9;  // x23
    unsigned long long v10;  // x22
    unsigned long long v11;  // x21
    unsigned long long v12;  // x20
    unsigned long long v13;  // x19
    struct_0 *v14;  // x0
    unsigned long long v0;  // [bp-0x40]
    unsigned long long v1;  // [bp-0x30]
    unsigned long long v2;  // [bp-0x28]
    unsigned long long v3;  // [bp-0x20]
    unsigned long long v4;  // [bp-0x18]
    unsigned long long v5;  // [bp-0x10]
    unsigned long long v6;  // [bp-0x8]

    v0 = v7;
    v1 = v8;
    v2 = v9;
    v3 = v10;
    v4 = v11;
    v5 = v12;
    v6 = v13;
    if (!(g_1fab193 & 1))
    {
        sub_f7d92c(&g_1eeed10);
        g_1fab193 = 1;
    }
    v14 = g_1eeed10;
    if (!g_1eeed10->field_e0)
        v14 = sub_f7da5c(g_1eeed10);
    CFScreen__UpdateDpi(v14, a1);
}
```

## `CFScreen.ForceFallbackDpi` — RVA `0xc39290`

- Decompiled symbol: `CFScreen_ForceFallbackDpi`
- Metadata signature: `public static void ForceFallbackDpi(bool enableFallbackDpi) { }`
- Native interval: `96` bytes
- Result: `pseudocode`

```c
typedef struct struct_3 {
    char padding_0[184];
    struct struct_2 *field_b8;
} struct_3;

typedef struct struct_0 {
    char padding_0[184];
    struct struct_1 *field_b8;
    char padding_c0[32];
    unsigned int field_e0;
} struct_0;

typedef struct struct_2 {
    char padding_0[4];
    char padding_4[12];
    uint128_t field_4;
    uint128_t field_14;
    unsigned int field_24;
    unsigned int field_28;
    unsigned int field_2c;
    unsigned int field_30;
    unsigned int field_34;
    unsigned int field_38;
    unsigned int field_3c;
    unsigned int field_40;
    unsigned int field_44;
    unsigned int field_48;
} struct_2;

typedef struct struct_1 {
    char field_0;
} struct_1;

extern struct_0 *g_1eeed10;
extern char g_1fab194;

struct_3 * CFScreen_ForceFallbackDpi(char a0)
{
    struct_0 *idx;  // x0
    unsigned int v1;  // x1
    struct_3 *v2;  // x0

    if (!(g_1fab194 & 1))
    {
        sub_f7d92c(&g_1eeed10);
        g_1fab194 = 1;
    }
    idx = g_1eeed10;
    if (!g_1eeed10->field_e0)
    {
        sub_f7da5c(g_1eeed10);
        idx = g_1eeed10;
    }
    idx->field_b8->field_0 = a0 & 1;
    v2 = CFScreen__UpdateDpi(idx, v1);
    return CFScreen__UpdateDpi(idx, v1);
}
```

## `CFScreen.SetFallbackScreenDiameter` — RVA `0xc392f0`

- Decompiled symbol: `CFScreen_SetFallbackScreenDiameter`
- Metadata signature: `public static void SetFallbackScreenDiameter(float diameterInInches) { }`
- Native interval: `116` bytes
- Result: `pseudocode`

```c
typedef struct struct_3 {
    char padding_0[184];
    struct struct_2 *field_b8;
} struct_3;

typedef struct struct_0 {
    char padding_0[184];
    struct struct_1 *field_b8;
    char padding_c0[32];
    unsigned int field_e0;
} struct_0;

typedef struct struct_2 {
    char padding_0[4];
    char padding_4[12];
    uint128_t field_4;
    uint128_t field_14;
    unsigned int field_24;
    unsigned int field_28;
    unsigned int field_2c;
    unsigned int field_30;
    unsigned int field_34;
    unsigned int field_38;
    unsigned int field_3c;
    unsigned int field_40;
    unsigned int field_44;
    unsigned int field_48;
} struct_2;

typedef struct struct_1 {
    char padding_0[40];
    unsigned int field_28;
    unsigned int field_2c;
} struct_1;

extern struct_0 *g_1eeed10;
extern char g_1fab195;

struct_3 * CFScreen_SetFallbackScreenDiameter(void)
{
    struct_0 *p;  // x0
    unsigned int ptr[12];  // x8
    unsigned int v2;  // s0
    unsigned int v3;  // x1
    struct_3 *v4;  // x0

    if (!(g_1fab195 & 1))
    {
        sub_f7d92c(&g_1eeed10);
        g_1fab195 = 1;
    }
    p = g_1eeed10;
    if (!g_1eeed10->field_e0)
    {
        sub_f7da5c(g_1eeed10);
        p = g_1eeed10;
    }
    ptr = p->field_b8;
    v2 = [D] unsupported_Iop_ZeroHI96ofV128();
    ptr[11] = 0xbf800000;
    ptr[10] = v2;
    v4 = CFScreen__UpdateDpi(p, v3);
    return CFScreen__UpdateDpi(p, v3);
}
```

## `CFScreen.cctor` — RVA `0xc39364`

- Decompiled symbol: `CFScreen_cctor`
- Metadata signature: `private static void .cctor() { }`
- Native interval: `104` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char field_0;
    char padding_1[35];
    uint128_t field_24;
    uint128_t field_34;
    unsigned long long field_44;
} struct_0;

typedef struct struct_1 {
    char padding_0[184];
    struct struct_0 *field_b8;
} struct_1;

extern struct_1 *g_1eeed10;
extern char g_1fab198;

unsigned long long CFScreen_cctor(void)
{
    unsigned long long v0;  // x0
    struct_0 *ptr;  // x8

    if (!(g_1fab198 & 1))
    {
        v0 = sub_f7d92c(&g_1eeed10);
        g_1fab198 = 1;
    }
    ptr = g_1eeed10->field_b8;
    ptr->field_0 = 0;
    *((uint128_t *)&(&ptr->padding_1)[1]) = 0xbf800000bf80000040e0000042c00000;
    *((uint128_t *)((char *)&ptr->field_24 + 4)) = 0x42c8000042c80000bf800000bf800000;
    *((unsigned long long *)((char *)&ptr->field_34 + 4)) = 0x3f8000003f800000;
    return v0;
}
```
