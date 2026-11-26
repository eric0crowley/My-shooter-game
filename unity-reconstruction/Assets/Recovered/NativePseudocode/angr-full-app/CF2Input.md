# Native pseudocode: CF2Input

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `CF2Input.add_onActiveRigChange` — RVA `0xc2b7dc`

- Decompiled symbol: `CF2Input_add_onActiveRigChange`
- Metadata signature: `public static void add_onActiveRigChange(Action value) { }`
- Native interval: `220` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[184];
    struct struct_0 *field_b8;
    char padding_c0[32];
    unsigned int field_e0;
} struct_1;

typedef struct struct_0 {
    char padding_0[16];
    long long field_10;
} struct_0;

extern struct_1 *g_1eeed00;
extern char g_1fab159;

long long CF2Input_add_onActiveRigChange(long long a0)
{
    struct_1 *idx;  // x0
    long long v1;  // x20
    long long v2;  // x20
    long long v3;  // x21
    struct_1 *v4;  // x0
    long long v5;  // x20

    if (!(g_1fab159 & 1))
    {
        sub_f7d92c("++");
        sub_f7d92c(&g_1eeed00);
        g_1fab159 = 1;
    }
    idx = g_1eeed00;
    if (!g_1eeed00->field_e0)
    {
        sub_f7da5c(g_1eeed00);
        idx = g_1eeed00;
    }
    v1 = idx->field_b8->field_10;
    while (true)
    {
        v2 = v1;
        v3 = Delegate__Combine(v2, a0, 0);
        if (v3 && *((long long *)v3) != g_1eee648)
            sub_f7df10(v3);
        v4 = g_1eeed00;
        if (!g_1eeed00->field_e0)
        {
            sub_f7da5c(g_1eeed00);
            v4 = g_1eeed00;
        }
        v5 = sub_f60ebc(&v4->field_b8->field_10, v3, v2);
        v1 = v5;
        if (v2 == v1)
            return v5;
    }
}
```

## `CF2Input.remove_onActiveRigChange` — RVA `0xc2ba9c`

- Decompiled symbol: `CF2Input_remove_onActiveRigChange`
- Metadata signature: `public static void remove_onActiveRigChange(Action value) { }`
- Native interval: `220` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[184];
    struct struct_0 *field_b8;
    char padding_c0[32];
    unsigned int field_e0;
} struct_1;

typedef struct struct_0 {
    char padding_0[16];
    long long field_10;
} struct_0;

extern struct_1 *g_1eeed00;
extern char g_1fab15a;

long long CF2Input_remove_onActiveRigChange(long long a0)
{
    struct_1 *idx;  // x0
    long long v1;  // x20
    long long v2;  // x20
    long long v3;  // x21
    struct_1 *v4;  // x0
    long long v5;  // x20

    if (!(g_1fab15a & 1))
    {
        sub_f7d92c("++");
        sub_f7d92c(&g_1eeed00);
        g_1fab15a = 1;
    }
    idx = g_1eeed00;
    if (!g_1eeed00->field_e0)
    {
        sub_f7da5c(g_1eeed00);
        idx = g_1eeed00;
    }
    v1 = idx->field_b8->field_10;
    while (true)
    {
        v2 = v1;
        v3 = Delegate__Remove(v2, a0, 0);
        if (v3 && *((long long *)v3) != g_1eee648)
            sub_f7df10(v3);
        v4 = g_1eeed00;
        if (!g_1eeed00->field_e0)
        {
            sub_f7da5c(g_1eeed00);
            v4 = g_1eeed00;
        }
        v5 = sub_f60ebc(&v4->field_b8->field_10, v3, v2);
        v1 = v5;
        if (v2 == v1)
            return v5;
    }
}
```

## `CF2Input.add_onMobileModeChange` — RVA `0xc354a4`

- Decompiled symbol: `CF2Input_add_onMobileModeChange`
- Metadata signature: `public static void add_onMobileModeChange(Action value) { }`
- Native interval: `220` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[184];
    struct struct_0 *field_b8;
    char padding_c0[32];
    unsigned int field_e0;
} struct_1;

typedef struct struct_0 {
    char padding_0[8];
    long long field_8;
} struct_0;

extern struct_1 *g_1eeed00;
extern char g_1fab157;

long long CF2Input_add_onMobileModeChange(long long a0)
{
    struct_1 *idx;  // x0
    long long v1;  // x20
    long long v2;  // x20
    long long v3;  // x21
    struct_1 *v4;  // x0
    long long v5;  // x20

    if (!(g_1fab157 & 1))
    {
        sub_f7d92c("++");
        sub_f7d92c(&g_1eeed00);
        g_1fab157 = 1;
    }
    idx = g_1eeed00;
    if (!g_1eeed00->field_e0)
    {
        sub_f7da5c(g_1eeed00);
        idx = g_1eeed00;
    }
    v1 = idx->field_b8->field_8;
    while (true)
    {
        v2 = v1;
        v3 = Delegate__Combine(v2, a0, 0);
        if (v3 && *((long long *)v3) != g_1eee648)
            sub_f7df10(v3);
        v4 = g_1eeed00;
        if (!g_1eeed00->field_e0)
        {
            sub_f7da5c(g_1eeed00);
            v4 = g_1eeed00;
        }
        v5 = sub_f60ebc(&v4->field_b8->field_8, v3, v2);
        v1 = v5;
        if (v2 == v1)
            return v5;
    }
}
```

## `CF2Input.remove_onMobileModeChange` — RVA `0xc35580`

- Decompiled symbol: `CF2Input_remove_onMobileModeChange`
- Metadata signature: `public static void remove_onMobileModeChange(Action value) { }`
- Native interval: `220` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[184];
    struct struct_0 *field_b8;
    char padding_c0[32];
    unsigned int field_e0;
} struct_1;

typedef struct struct_0 {
    char padding_0[8];
    long long field_8;
} struct_0;

extern struct_1 *g_1eeed00;
extern char g_1fab158;

long long CF2Input_remove_onMobileModeChange(long long a0)
{
    struct_1 *idx;  // x0
    long long v1;  // x20
    long long v2;  // x20
    long long v3;  // x21
    struct_1 *v4;  // x0
    long long v5;  // x20

    if (!(g_1fab158 & 1))
    {
        sub_f7d92c("++");
        sub_f7d92c(&g_1eeed00);
        g_1fab158 = 1;
    }
    idx = g_1eeed00;
    if (!g_1eeed00->field_e0)
    {
        sub_f7da5c(g_1eeed00);
        idx = g_1eeed00;
    }
    v1 = idx->field_b8->field_8;
    while (true)
    {
        v2 = v1;
        v3 = Delegate__Remove(v2, a0, 0);
        if (v3 && *((long long *)v3) != g_1eee648)
            sub_f7df10(v3);
        v4 = g_1eeed00;
        if (!g_1eeed00->field_e0)
        {
            sub_f7da5c(g_1eeed00);
            v4 = g_1eeed00;
        }
        v5 = sub_f60ebc(&v4->field_b8->field_8, v3, v2);
        v1 = v5;
        if (v2 == v1)
            return v5;
    }
}
```

## `CF2Input.GetMobileMode` — RVA `0xc3565c`

- Decompiled symbol: `CF2Input_GetMobileMode`
- Metadata signature: `public static CF2Input.MobileMode GetMobileMode() { }`
- Native interval: `88` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[184];
    struct struct_1 *field_b8;
    char padding_c0[32];
    unsigned int field_e0;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

extern struct_0 *g_1eeed00;
extern char g_1fab15b;

int CF2Input_GetMobileMode(void)
{
    struct_0 *v0;  // x0

    if (!(g_1fab15b & 1))
    {
        sub_f7d92c(&g_1eeed00);
        g_1fab15b = 1;
    }
    v0 = g_1eeed00;
    if (!g_1eeed00->field_e0)
    {
        sub_f7da5c(g_1eeed00);
        v0 = g_1eeed00;
    }
    return v0->field_b8->field_0;
}
```

## `CF2Input.SetMobileMode` — RVA `0xc356b4`

- Decompiled symbol: `CF2Input_SetMobileMode`
- Metadata signature: `public static void SetMobileMode(CF2Input.MobileMode mode) { }`
- Native interval: `184` bytes
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

typedef struct struct_4 {
    char padding_0[224];
    unsigned int field_e0;
} struct_4;

typedef struct struct_2 {
    unsigned int field_0;
    char padding_4[4];
    struct struct_0 *field_8;
} struct_2;

typedef struct struct_1 {
    unsigned long long field_0;
} struct_1;

extern struct_3 *g_1eeed00;
extern struct_4 *g_1eeed08;
extern char g_1fab15c;

long long CF2Input_SetMobileMode(unsigned int a0)
{
    struct_3 *index;  // x0
    struct_0 *ptr;  // x8
    unsigned long long v2;  // x0
    unsigned long long v3;  // x1
    struct_4 *v4;  // x0
    unsigned long long v5;  // x0

    if (!(g_1fab15c & 1))
    {
        sub_f7d92c(&g_1eeed00);
        sub_f7d92c(&g_1eeed08);
        g_1fab15c = 1;
    }
    index = g_1eeed00;
    if (!g_1eeed00->field_e0)
    {
        sub_f7da5c(g_1eeed00);
        index = g_1eeed00;
    }
    ptr = index->field_b8->field_8;
    index->field_b8->field_0 = a0;
    if (ptr)
    {
        if (!index->field_e0)
        {
            sub_f7da5c();
            ptr = g_1eeed00->field_b8->field_8;
            if (!ptr)
                sub_f7db74();
        }
        v2 = ptr->field_40;
        v3 = ptr->field_28;
        ptr->field_18();
    }
    else
    {
        v4 = g_1eeed08;
        if (!g_1eeed08->field_e0)
            v4 = sub_f7da5c(g_1eeed08);
        v5 = CFCursor__InternalRefresh(v4);
        return CFCursor__InternalRefresh(v4);
    }
}
```

## `CF2Input.IsInMobileMode` — RVA `0xc358f4`

- Decompiled symbol: `CF2Input_IsInMobileMode`
- Metadata signature: `public static bool IsInMobileMode() { }`
- Native interval: `164` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[184];
    struct struct_1 *field_b8;
    char padding_c0[32];
    unsigned int field_e0;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

typedef struct struct_2 {
    char padding_0[224];
    unsigned int field_e0;
} struct_2;

extern struct_2 *g_1eee870;
extern struct_0 *g_1eeed00;
extern char g_1fab15d;
extern char g_1fab15e;

unsigned int CF2Input_IsInMobileMode(void)
{
    struct_0 *v0;  // x0

    if (!(g_1fab15d & 1))
    {
        sub_f7d92c(&g_1eeed00);
        g_1fab15d = 1;
    }
    v0 = g_1eeed00;
    if (!g_1eeed00->field_e0)
    {
        sub_f7da5c(g_1eeed00);
        v0 = g_1eeed00;
    }
    if (v0->field_b8->field_0 == 1)
        return 1;
    if (!v0->field_e0)
    {
        sub_f7da5c();
        v0 = g_1eeed00;
        if (!g_1eeed00->field_b8->field_0)
        {
LABEL_1035980:
            if (!v0->field_e0)
                sub_f7da5c();
            if (!(g_1fab15e & 1))
            {
                sub_f7d92c(&g_1eee870);
                g_1fab15e = 1;
            }
            if (g_1eee870->field_e0)
                return Application__get_isMobilePlatform();
            sub_f7da5c(g_1eee870);
            return Application__get_isMobilePlatform();
        }
    }
    else if (!v0->field_b8->field_0)
    {
        goto LABEL_1035980;
    }
    return 0;
}
```

## `CF2Input.IsMobilePlatform` — RVA `0xc35998`

- Decompiled symbol: `CF2Input_IsMobilePlatform`
- Metadata signature: `public static bool IsMobilePlatform() { }`
- Native interval: `80` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: CFGFast did not recover a function at the metadata RVA

```c
// 0x1035998: str x30, [sp, #-0x20]!
// 0x103599c: stp x20, x19, [sp, #0x10]
// 0x10359a0: adrp x19, #0x1fab000
// 0x10359a4: adrp x20, #0x1e8c000
// 0x10359a8: ldrb w8, [x19, #0x15e]
// 0x10359ac: ldr x20, [x20, #0x248]
// 0x10359b0: tbnz w8, #0, #0x10359c8
// 0x10359b4: adrp x0, #0x1e8c000
// 0x10359b8: ldr x0, [x0, #0x248]
// 0x10359bc: bl #0xf7d92c
// 0x10359c0: mov w8, #1
// 0x10359c4: strb w8, [x19, #0x15e]
// 0x10359c8: ldr x0, [x20]
// 0x10359cc: ldr w8, [x0, #0xe0]
// 0x10359d0: cbnz w8, #0x10359d8
// 0x10359d4: bl #0xf7da5c
// 0x10359d8: ldp x20, x19, [sp, #0x10]
// 0x10359dc: mov x0, xzr
// 0x10359e0: ldr x30, [sp], #0x20
// 0x10359e4: b #0x1b6d5f4
```

## `CF2Input.ControllerActive` — RVA `0xc359e8`

- Decompiled symbol: `CF2Input_ControllerActive`
- Metadata signature: `public static bool ControllerActive() { }`
- Native interval: `76` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1eeed00;
extern char g_1fab15f;

unsigned int CF2Input_ControllerActive(void)
{
    if (!(g_1fab15f & 1))
    {
        sub_f7d92c(&g_1eeed00);
        g_1fab15f = 1;
    }
    if (!g_1eeed00->field_e0)
        sub_f7da5c(g_1eeed00);
    return CF2Input__IsInMobileMode();
}
```

## `CF2Input.get_activeRig` — RVA `0xc35a34`

- Decompiled symbol: `CF2Input_get_activeRig`
- Metadata signature: `public static InputRig get_activeRig() { }`
- Native interval: `88` bytes
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
    unsigned long long field_18;
} struct_0;

extern struct_1 *g_1eeed00;
extern char g_1fab160;

long long CF2Input_get_activeRig(void)
{
    struct_1 *v0;  // x0

    if (!(g_1fab160 & 1))
    {
        sub_f7d92c(&g_1eeed00);
        g_1fab160 = 1;
    }
    v0 = g_1eeed00;
    if (!g_1eeed00->field_e0)
    {
        sub_f7da5c(g_1eeed00);
        v0 = g_1eeed00;
    }
    return v0->field_b8->field_18;
}
```

## `CF2Input.set_activeRig` — RVA `0xc35a8c`

- Decompiled symbol: `CF2Input_set_activeRig`
- Metadata signature: `public static void set_activeRig(InputRig value) { }`
- Native interval: `620` bytes
- Result: `pseudocode`

```c
typedef struct struct_4 {
    char padding_0[184];
    struct struct_3 *field_b8;
    char padding_c0[32];
    unsigned int field_e0;
} struct_4;

typedef struct struct_5 {
    char padding_0[58];
    char field_3a;
} struct_5;

typedef struct struct_2 {
    char padding_0[58];
    char field_3a;
} struct_2;

typedef struct struct_3 {
    char padding_0[4];
    char field_4;
    char padding_5[11];
    struct struct_0 *field_10;
    struct struct_2 *field_18;
} struct_3;

typedef struct struct_0 {
    char padding_0[24];
    struct struct_1 *field_18;
    char padding_20[8];
    unsigned long long field_28;
    char padding_30[16];
    unsigned long long field_40;
} struct_0;

typedef struct struct_1 {
    unsigned long long field_0;
} struct_1;

typedef struct struct_7 {
    char padding_0[224];
    unsigned int field_e0;
} struct_7;

typedef struct struct_6 {
    char padding_0[224];
    unsigned int field_e0;
} struct_6;

extern struct_4 *g_1eeed00;
extern struct_6 *g_1eeed08;
extern struct_7 *g_1ef0c58;
extern char g_1fab161;

long long CF2Input_set_activeRig(struct_5 *a0)
{
    struct_4 *v0;  // x0
    unsigned long v1;  // x0
    unsigned int v9;  // w0
    struct_4 *pos;  // x8
    long long v11;  // x0
    struct_4 *idx4;  // x0
    struct_0 *ptr;  // x8
    unsigned long long v14;  // x0
    unsigned long long v15;  // x1
    struct_5 *v16;  // x0
    struct_4 *v2;  // x0
    struct_4 *off;  // x0
    struct_2 *v4;  // x0
    struct_4 *p;  // x8
    char v6;  // x0
    struct_3 *addr;  // x0
    unsigned long long v8;  // x2

    if (!(g_1fab161 & 1))
    {
        sub_f7d92c(&g_1eeed00);
        sub_f7d92c(&g_1eeed08);
        sub_f7d92c(&g_1ef0c58);
        g_1fab161 = 1;
    }
    v0 = g_1eeed00;
    if (!g_1eeed00->field_e0)
    {
        sub_f7da5c(g_1eeed00);
        v0 = g_1eeed00;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v1 = Object__op_Equality(a0, v0->field_b8->field_18, 0);
    if (((char)v1 & 1))
        return v1;
    v2 = g_1eeed00;
    if (!g_1eeed00->field_e0)
    {
        sub_f7da5c(g_1eeed00);
        v2 = g_1eeed00;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (!((char)Object__op_Inequality(v2->field_b8->field_18, 0, 0) & 1))
    {
        v6 = Input__get_simulateMouseWithTouches(0);
        p = g_1eeed00;
        if (!g_1eeed00->field_e0)
        {
            sub_f7da5c(g_1eeed00);
            p = g_1eeed00;
        }
        p->field_b8->field_4 = v6 & 1;
        goto LABEL_1035bd4;
    }
    off = g_1eeed00;
    if (!g_1eeed00->field_e0)
    {
        sub_f7da5c(g_1eeed00);
        off = g_1eeed00;
    }
    v4 = off->field_b8->field_18;
    if (v4)
    {
        InputRig__OnDisactivateRig();
        p = g_1eeed00;
LABEL_1035bd4:
        if (!p->field_e0)
        {
            sub_f7da5c(p);
            p = g_1eeed00;
        }
        addr = p->field_b8;
        addr->field_18 = a0;
        sub_f7d8d0((struct struct_3 *)&addr->field_18, a0);
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        v8 = 0;
        v9 = Object__op_Inequality(g_1eeed00->field_b8->field_18, 0, 0);
        pos = g_1eeed00;
        if (!g_1eeed00->field_e0)
        {
            sub_f7da5c(g_1eeed00);
            pos = g_1eeed00;
        }
        if (((char)v9 & 1))
        {
            v4 = pos->field_b8->field_18;
            if (v4)
            {
                if (v4->field_3a)
                {
                    v8 = 0;
                    InputRig__ShowOrHideTouchControls();
                }
                v11 = 0;
LABEL_1035c78:
                Input__set_simulateMouseWithTouches(v11, 0);
                idx4 = g_1eeed00;
                if (!g_1eeed00->field_e0)
                {
                    sub_f7da5c(g_1eeed00);
                    idx4 = g_1eeed00;
                }
                ptr = idx4->field_b8->field_10;
                if (idx4->field_b8->field_10)
                {
                    if (idx4->field_e0 || !((v4 = (struct_2 *)(unsigned long long)sub_f7da5c(), ptr = (struct_0 *)g_1eeed00->field_b8->field_10, !ptr)))
                    {
                        v14 = ptr->field_40;
                        v15 = ptr->field_28;
                        ptr->field_18();
                    }
                }
                else
                {
                    if (!g_1eeed08->field_e0)
                        sub_f7da5c(g_1eeed08);
                    v16 = CFCursor__InternalRefresh();
                    return CFCursor__InternalRefresh();
                }
            }
        }
        else if (!pos->field_b8->field_4)
        {
            v11 = 0;
            goto LABEL_1035c78;
        }
        else
        {
            v11 = 1;
            goto LABEL_1035c78;
        }
    }
    sub_f7db74(v4);
}
```

## `CF2Input.ResetInputAxes` — RVA `0xc35d5c`

- Decompiled symbol: `CF2Input_ResetInputAxes`
- Metadata signature: `public static void ResetInputAxes() { }`
- Native interval: `192` bytes
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
extern char g_1fab162;

long long CF2Input_ResetInputAxes(void)
{
    unsigned long long v3;  // x30
    unsigned long long v4;  // x20
    unsigned long long v5;  // x19
    struct_1 *v6;  // x0
    struct_1 *v7;  // x0
    unsigned long long v8;  // x0
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x10]
    unsigned long long v2;  // [bp-0x8]

    v0 = v3;
    v1 = v4;
    v2 = v5;
    if (!(g_1fab162 & 1))
    {
        sub_f7d92c(&g_1eeed00);
        sub_f7d92c(&g_1ef0c58);
        g_1fab162 = 1;
    }
    v6 = g_1eeed00;
    if (!g_1eeed00->field_e0)
    {
        sub_f7da5c(g_1eeed00);
        v6 = g_1eeed00;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (!((char)Object__op_Inequality(v6->field_b8->field_18, 0, 0) & 1))
    {
        v8 = Input__ResetInputAxes();
        return Input__ResetInputAxes();
    }
    v7 = g_1eeed00;
    if (!g_1eeed00->field_e0)
    {
        sub_f7da5c(g_1eeed00);
        v7 = g_1eeed00;
    }
    if (v7->field_b8->field_18)
        InputRig__MuteUntilRelease(v7->field_b8->field_18); /* do not return */
    sub_f7db74(0);
}
```

## `CF2Input.GetAxis` — RVA `0xc35e20`

- Decompiled symbol: `CF2Input_GetAxis`
- Metadata signature: `public static float GetAxis(string axisName) { }`
- Native interval: `212` bytes
- Result: `pseudocode`

```c
typedef struct struct_4 {
    char padding_0[184];
    struct struct_3 *field_b8;
    char padding_c0[32];
    unsigned int field_e0;
} struct_4;

typedef struct struct_7 {
    char padding_0[184];
    struct struct_6 *field_b8;
    char padding_c0[32];
    unsigned int field_e0;
} struct_7;

typedef struct struct_1 {
    char padding_0[128];
    unsigned long long field_80;
} struct_1;

typedef struct struct_3 {
    char padding_0[24];
    struct struct_2 *field_18;
} struct_3;

typedef struct struct_6 {
    char padding_0[24];
    struct struct_5 *field_18;
} struct_6;

typedef struct struct_2 {
    char padding_0[128];
    long long field_80;
} struct_2;

typedef struct struct_5 {
    char padding_0[128];
    unsigned long long field_80;
} struct_5;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern char g_1035ef4;
extern struct_4 *g_1eeed00;
extern struct_0 *g_1ef0c58;
extern long long g_1ef9850;
extern char g_1fab163;
extern char g_1fab1b1;

unsigned long long CF2Input_GetAxis(long long a0)
{
    struct_4 **v4;  // x21
    long long v5;  // x19
    struct_7 *index;  // x0
    struct_1 *v7;  // x20
    long long v8;  // x1
    struct_7 *idx;  // x0
    struct_1 *v10;  // x0
    struct_1 *v11;  // x20
    unsigned long long v12;  // x0
    unsigned long long v13;  // x0
    unsigned long v0;  // [bp-0x20]
    struct_4 **v1;  // [bp-0x18]
    struct_1 *v2;  // [bp-0x10]
    long long v3;  // [bp-0x8]

    v4 = &g_1eeed00;
    v5 = a0;
    if (!(g_1fab163 & 1))
    {
        sub_f7d92c(&g_1eeed00);
        sub_f7d92c(&g_1ef0c58);
        g_1fab163 = 1;
    }
    index = g_1eeed00;
    if (!g_1eeed00->field_e0)
    {
        sub_f7da5c(g_1eeed00);
        index = g_1eeed00;
    }
    v7 = index->field_b8->field_18;
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v8 = 0;
    if (!((char)Object__op_Inequality(index->field_b8->field_18, 0, 0) & 1))
    {
        v13 = Input__GetAxis();
        return Input__GetAxis();
    }
    idx = g_1eeed00;
    if (!g_1eeed00->field_e0)
    {
        sub_f7da5c(g_1eeed00);
        idx = g_1eeed00;
    }
    v10 = idx->field_b8->field_18;
    if (idx->field_b8->field_18)
    {
        v8 = v5;
        v7 = v2;
        v5 = v3;
        vvar_28{r256|8b} = v0;
        v4 = v1;
    }
    else
    {
        vvar_93{r256|8b} = (int)&g_1035ef4;
        v10 = sub_f7db74(0);
    }
    v0 = vvar_28{r256|8b};
    v1 = v4;
    v2 = v7;
    v3 = v5;
    v11 = v10;
    if (!(g_1fab1b1 & 1))
    {
        sub_f7d92c(&g_1ef9850);
        g_1fab1b1 = 1;
    }
    if (v11->field_80)
    {
        if (sub_1526618(v11->field_80, v8, g_1ef9850))
        {
            v12 = InputRig_AxisConfig__GetAnalog();
            return InputRig_AxisConfig__GetAnalog();
        }
        return 0;
    }
    sub_f7db74(0);
}
```

## `CF2Input.GetAxis` — RVA `0xc35f68`

- Decompiled symbol: `CF2Input_GetAxis`
- Metadata signature: `public static float GetAxis(string axisName, ref int cachedId) { }`
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
extern char g_1fab164;

long long CF2Input_GetAxis(long long a0, long long a1)
{
    struct_1 *v0;  // x0
    struct_1 *v1;  // x0
    unsigned long long v2;  // x0
    unsigned long long v3;  // x0

    if (!(g_1fab164 & 1))
    {
        sub_f7d92c(&g_1eeed00);
        sub_f7d92c(&g_1ef0c58);
        g_1fab164 = 1;
    }
    v0 = g_1eeed00;
    if (!g_1eeed00->field_e0)
    {
        sub_f7da5c(g_1eeed00);
        v0 = g_1eeed00;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (!((char)Object__op_Inequality(v0->field_b8->field_18, 0, 0) & 1))
    {
        v3 = Input__GetAxis();
        return Input__GetAxis();
    }
    v1 = g_1eeed00;
    if (!g_1eeed00->field_e0)
    {
        sub_f7da5c(g_1eeed00);
        v1 = g_1eeed00;
    }
    if (v1->field_b8->field_18)
    {
        v2 = InputRig__GetAxis(v1->field_b8->field_18, a0, a1);
        return InputRig__GetAxis(v1->field_b8->field_18, a0, a1);
    }
    sub_f7db74(0);
}
```

## `CF2Input.GetAxisRaw` — RVA `0xc360d8`

- Decompiled symbol: `CF2Input_GetAxisRaw`
- Metadata signature: `public static float GetAxisRaw(string axisName) { }`
- Native interval: `212` bytes
- Result: `pseudocode`

```c
typedef struct struct_4 {
    char padding_0[184];
    struct struct_3 *field_b8;
    char padding_c0[32];
    unsigned int field_e0;
} struct_4;

typedef struct struct_7 {
    char padding_0[184];
    struct struct_6 *field_b8;
    char padding_c0[32];
    unsigned int field_e0;
} struct_7;

typedef struct struct_1 {
    char padding_0[128];
    unsigned long long field_80;
} struct_1;

typedef struct struct_3 {
    char padding_0[24];
    struct struct_2 *field_18;
} struct_3;

typedef struct struct_6 {
    char padding_0[24];
    struct struct_5 *field_18;
} struct_6;

typedef struct struct_2 {
    char padding_0[128];
    long long field_80;
} struct_2;

typedef struct struct_5 {
    char padding_0[128];
    unsigned long long field_80;
} struct_5;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern char g_10361ac;
extern struct_4 *g_1eeed00;
extern struct_0 *g_1ef0c58;
extern long long g_1ef9850;
extern char g_1fab165;
extern char g_1fab1b3;

unsigned long long CF2Input_GetAxisRaw(long long a0)
{
    struct_4 **v4;  // x21
    long long v5;  // x19
    struct_7 *index;  // x0
    struct_1 *v7;  // x20
    long long v8;  // x1
    struct_7 *idx;  // x0
    struct_1 *v10;  // x0
    struct_1 *v11;  // x20
    unsigned long long v12;  // x0
    unsigned long long v13;  // x0
    unsigned long v0;  // [bp-0x20]
    struct_4 **v1;  // [bp-0x18]
    struct_1 *v2;  // [bp-0x10]
    long long v3;  // [bp-0x8]

    v4 = &g_1eeed00;
    v5 = a0;
    if (!(g_1fab165 & 1))
    {
        sub_f7d92c(&g_1eeed00);
        sub_f7d92c(&g_1ef0c58);
        g_1fab165 = 1;
    }
    index = g_1eeed00;
    if (!g_1eeed00->field_e0)
    {
        sub_f7da5c(g_1eeed00);
        index = g_1eeed00;
    }
    v7 = index->field_b8->field_18;
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v8 = 0;
    if (!((char)Object__op_Inequality(index->field_b8->field_18, 0, 0) & 1))
    {
        v13 = Input__GetAxisRaw();
        return Input__GetAxisRaw();
    }
    idx = g_1eeed00;
    if (!g_1eeed00->field_e0)
    {
        sub_f7da5c(g_1eeed00);
        idx = g_1eeed00;
    }
    v10 = idx->field_b8->field_18;
    if (idx->field_b8->field_18)
    {
        v8 = v5;
        v7 = v2;
        v5 = v3;
        vvar_28{r256|8b} = v0;
        v4 = v1;
    }
    else
    {
        vvar_93{r256|8b} = (int)&g_10361ac;
        v10 = sub_f7db74(0);
    }
    v0 = vvar_28{r256|8b};
    v1 = v4;
    v2 = v7;
    v3 = v5;
    v11 = v10;
    if (!(g_1fab1b3 & 1))
    {
        sub_f7d92c(&g_1ef9850);
        g_1fab1b3 = 1;
    }
    if (v11->field_80)
    {
        if (sub_1526618(v11->field_80, v8, g_1ef9850))
        {
            v12 = InputRig_AxisConfig__GetAnalogRaw();
            return InputRig_AxisConfig__GetAnalogRaw();
        }
        return 0;
    }
    sub_f7db74(0);
}
```

## `CF2Input.GetAxisRaw` — RVA `0xc36220`

- Decompiled symbol: `CF2Input_GetAxisRaw`
- Metadata signature: `public static float GetAxisRaw(string axisName, ref int cachedId) { }`
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
extern char g_1fab166;

long long CF2Input_GetAxisRaw(long long a0, long long a1)
{
    struct_1 *v0;  // x0
    struct_1 *v1;  // x0
    unsigned long long v2;  // x0
    unsigned long long v3;  // x0

    if (!(g_1fab166 & 1))
    {
        sub_f7d92c(&g_1eeed00);
        sub_f7d92c(&g_1ef0c58);
        g_1fab166 = 1;
    }
    v0 = g_1eeed00;
    if (!g_1eeed00->field_e0)
    {
        sub_f7da5c(g_1eeed00);
        v0 = g_1eeed00;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (!((char)Object__op_Inequality(v0->field_b8->field_18, 0, 0) & 1))
    {
        v3 = Input__GetAxisRaw();
        return Input__GetAxisRaw();
    }
    v1 = g_1eeed00;
    if (!g_1eeed00->field_e0)
    {
        sub_f7da5c(g_1eeed00);
        v1 = g_1eeed00;
    }
    if (v1->field_b8->field_18)
    {
        v2 = InputRig__GetAxisRaw(v1->field_b8->field_18, a0, a1);
        return InputRig__GetAxisRaw(v1->field_b8->field_18, a0, a1);
    }
    sub_f7db74(0);
}
```

## `CF2Input.GetButton` — RVA `0xc36390`

- Decompiled symbol: `CF2Input_GetButton`
- Metadata signature: `public static bool GetButton(string axisName) { }`
- Native interval: `212` bytes
- Result: `pseudocode`

```c
typedef struct struct_5 {
    char padding_0[144];
    char field_90;
} struct_5;

typedef struct struct_4 {
    char padding_0[184];
    struct struct_3 *field_b8;
    char padding_c0[32];
    unsigned int field_e0;
} struct_4;

typedef struct struct_8 {
    char padding_0[184];
    struct struct_7 *field_b8;
    char padding_c0[32];
    unsigned int field_e0;
} struct_8;

typedef struct struct_1 {
    char padding_0[128];
    unsigned long long field_80;
} struct_1;

typedef struct struct_3 {
    char padding_0[24];
    struct struct_2 *field_18;
} struct_3;

typedef struct struct_7 {
    char padding_0[24];
    struct struct_6 *field_18;
} struct_7;

typedef struct struct_2 {
    char padding_0[128];
    long long field_80;
} struct_2;

typedef struct struct_6 {
    char padding_0[128];
    unsigned long long field_80;
} struct_6;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern char g_1036464;
extern struct_4 *g_1eeed00;
extern struct_0 *g_1ef0c58;
extern long long g_1ef9850;
extern char g_1fab167;
extern char g_1fab1b5;

struct_5 * CF2Input_GetButton(long long a0)
{
    struct_4 **v4;  // x21
    long long v5;  // x19
    struct_8 *index;  // x0
    struct_1 *v7;  // x20
    long long v8;  // x1
    struct_8 *idx;  // x0
    struct_1 *v10;  // x0
    struct_1 *v11;  // x20
    struct_5 *v12;  // x0
    unsigned long v0;  // [bp-0x20]
    struct_4 **v1;  // [bp-0x18]
    struct_1 *v2;  // [bp-0x10]
    long long v3;  // [bp-0x8]

    v4 = &g_1eeed00;
    v5 = a0;
    if (!(g_1fab167 & 1))
    {
        sub_f7d92c(&g_1eeed00);
        sub_f7d92c(&g_1ef0c58);
        g_1fab167 = 1;
    }
    index = g_1eeed00;
    if (!g_1eeed00->field_e0)
    {
        sub_f7da5c(g_1eeed00);
        index = g_1eeed00;
    }
    v7 = index->field_b8->field_18;
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v8 = 0;
    if (((char)Object__op_Inequality(index->field_b8->field_18, 0, 0) & 1))
    {
        idx = g_1eeed00;
        if (!g_1eeed00->field_e0)
        {
            sub_f7da5c(g_1eeed00);
            idx = g_1eeed00;
        }
        v10 = idx->field_b8->field_18;
        if (idx->field_b8->field_18)
        {
            v8 = v5;
            v7 = v2;
            v5 = v3;
            vvar_35{r256|8b} = v0;
            v4 = v1;
        }
        else
        {
            vvar_106{r256|8b} = (int)&g_1036464;
            v10 = sub_f7db74(0);
        }
        v0 = vvar_35{r256|8b};
        v1 = v4;
        v2 = v7;
        v3 = v5;
        v11 = v10;
        if (!(g_1fab1b5 & 1))
        {
            sub_f7d92c(&g_1ef9850);
            g_1fab1b5 = 1;
        }
        if (v11->field_80)
        {
            v12 = sub_1526618(v11->field_80, v8, g_1ef9850);
            if (!v12)
            {
                return v12;
            }
            else if (!v12->field_90)
            {
                return NULL;
            }
            else
            {
                return 0x1;
            }
        }
        sub_f7db74(0);
    }
}
```

## `CF2Input.GetButton` — RVA `0xc364d0`

- Decompiled symbol: `CF2Input_GetButton`
- Metadata signature: `public static bool GetButton(string axisName, ref int cachedId) { }`
- Native interval: `232` bytes
- Result: `pseudocode`

```c
typedef struct struct_5 {
    char padding_0[144];
    char field_90;
} struct_5;

typedef struct struct_4 {
    char padding_0[184];
    struct struct_3 *field_b8;
    char padding_c0[32];
    unsigned int field_e0;
} struct_4;

typedef struct struct_8 {
    char padding_0[184];
    struct struct_7 *field_b8;
    char padding_c0[32];
    unsigned int field_e0;
} struct_8;

typedef struct struct_1 {
    char padding_0[128];
    unsigned long long field_80;
} struct_1;

typedef struct struct_3 {
    char padding_0[24];
    struct struct_2 *field_18;
} struct_3;

typedef struct struct_7 {
    char padding_0[24];
    struct struct_6 *field_18;
} struct_7;

typedef struct struct_2 {
    char padding_0[128];
    long long field_80;
} struct_2;

typedef struct struct_6 {
    char padding_0[128];
    unsigned long long field_80;
} struct_6;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern char g_10365b8;
extern struct_4 *g_1eeed00;
extern struct_0 *g_1ef0c58;
extern long long g_1ef9858;
extern char g_1fab168;
extern char g_1fab1b6;

struct_5 * CF2Input_GetButton(long long a0, long long a1)
{
    struct_4 **v5;  // x22
    long long v6;  // x20
    struct_5 *v15;  // x0
    long long v7;  // x19
    struct_8 *index;  // x0
    struct_1 *v9;  // x21
    long long v10;  // x1
    long long v11;  // x2
    struct_8 *idx;  // x0
    struct_1 *v13;  // x0
    struct_1 *v14;  // x21
    unsigned long v0;  // [bp-0x30]
    struct_4 **v1;  // [bp-0x20]
    struct_1 *v2;  // [bp-0x18]
    long long v3;  // [bp-0x10]
    long long v4;  // [bp-0x8]

    v5 = &g_1eeed00;
    v6 = a1;
    v7 = a0;
    if (!(g_1fab168 & 1))
    {
        sub_f7d92c(&g_1eeed00);
        sub_f7d92c(&g_1ef0c58);
        g_1fab168 = 1;
    }
    index = g_1eeed00;
    if (!g_1eeed00->field_e0)
    {
        sub_f7da5c(g_1eeed00);
        index = g_1eeed00;
    }
    v9 = index->field_b8->field_18;
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v10 = 0;
    v11 = 0;
    if (((char)Object__op_Inequality(index->field_b8->field_18, 0, 0) & 1))
    {
        idx = g_1eeed00;
        if (!g_1eeed00->field_e0)
        {
            sub_f7da5c(g_1eeed00);
            idx = g_1eeed00;
        }
        v13 = idx->field_b8->field_18;
        if (idx->field_b8->field_18)
        {
            v10 = v7;
            v11 = v6;
            v6 = v3;
            v7 = v4;
            v5 = v1;
            v9 = v2;
            vvar_38{r256|8b} = v0;
        }
        else
        {
            vvar_114{r256|8b} = (int)&g_10365b8;
            v13 = sub_f7db74(0);
        }
        v0 = vvar_38{r256|8b};
        v1 = v5;
        v2 = v9;
        v3 = v6;
        v4 = v7;
        v14 = v13;
        if (!(g_1fab1b6 & 1))
        {
            sub_f7d92c(&g_1ef9858);
            g_1fab1b6 = 1;
        }
        if (v14->field_80)
        {
            v15 = sub_15264f8(v14->field_80, v10, v11, g_1ef9858);
            if (!v15)
            {
                return v15;
            }
            else if (!v15->field_90)
            {
                return NULL;
            }
            else
            {
                return 0x1;
            }
        }
        sub_f7db74(0);
    }
}
```

## `CF2Input.GetButtonDown` — RVA `0xc36634`

- Decompiled symbol: `CF2Input_GetButtonDown`
- Metadata signature: `public static bool GetButtonDown(string axisName) { }`
- Native interval: `212` bytes
- Result: `pseudocode`

```c
typedef struct struct_4 {
    char padding_0[184];
    struct struct_3 *field_b8;
    char padding_c0[32];
    unsigned int field_e0;
} struct_4;

typedef struct struct_7 {
    char padding_0[184];
    struct struct_6 *field_b8;
    char padding_c0[32];
    unsigned int field_e0;
} struct_7;

typedef struct struct_1 {
    char padding_0[128];
    unsigned long long field_80;
} struct_1;

typedef struct struct_3 {
    char padding_0[24];
    struct struct_2 *field_18;
} struct_3;

typedef struct struct_6 {
    char padding_0[24];
    struct struct_5 *field_18;
} struct_6;

typedef struct struct_2 {
    char padding_0[128];
    long long field_80;
} struct_2;

typedef struct struct_5 {
    char padding_0[128];
    unsigned long long field_80;
} struct_5;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern char g_1036708;
extern struct_4 *g_1eeed00;
extern struct_0 *g_1ef0c58;
extern long long g_1ef9850;
extern char g_1fab169;
extern char g_1fab1b7;

unsigned long long CF2Input_GetButtonDown(long long a0)
{
    struct_4 **v4;  // x21
    long long v5;  // x19
    struct_7 *index;  // x0
    struct_1 *v7;  // x20
    long long v8;  // x1
    struct_7 *idx;  // x0
    struct_1 *v10;  // x0
    struct_1 *v11;  // x20
    unsigned long long v12;  // x0
    unsigned long long v13;  // x0
    unsigned long v0;  // [bp-0x20]
    struct_4 **v1;  // [bp-0x18]
    struct_1 *v2;  // [bp-0x10]
    long long v3;  // [bp-0x8]

    v4 = &g_1eeed00;
    v5 = a0;
    if (!(g_1fab169 & 1))
    {
        sub_f7d92c(&g_1eeed00);
        sub_f7d92c(&g_1ef0c58);
        g_1fab169 = 1;
    }
    index = g_1eeed00;
    if (!g_1eeed00->field_e0)
    {
        sub_f7da5c(g_1eeed00);
        index = g_1eeed00;
    }
    v7 = index->field_b8->field_18;
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v8 = 0;
    if (!((char)Object__op_Inequality(index->field_b8->field_18, 0, 0) & 1))
    {
        v13 = Input__GetButtonDown();
        return Input__GetButtonDown();
    }
    idx = g_1eeed00;
    if (!g_1eeed00->field_e0)
    {
        sub_f7da5c(g_1eeed00);
        idx = g_1eeed00;
    }
    v10 = idx->field_b8->field_18;
    if (idx->field_b8->field_18)
    {
        v8 = v5;
        v7 = v2;
        v5 = v3;
        vvar_28{r256|8b} = v0;
        v4 = v1;
    }
    else
    {
        vvar_93{r256|8b} = (int)&g_1036708;
        v10 = sub_f7db74(0);
    }
    v0 = vvar_28{r256|8b};
    v1 = v4;
    v2 = v7;
    v3 = v5;
    v11 = v10;
    if (!(g_1fab1b7 & 1))
    {
        sub_f7d92c(&g_1ef9850);
        g_1fab1b7 = 1;
    }
    if (v11->field_80)
    {
        if (sub_1526618(v11->field_80, v8, g_1ef9850))
        {
            v12 = InputRig_AxisConfig__GetButtonDown();
            return InputRig_AxisConfig__GetButtonDown();
        }
        return 0;
    }
    sub_f7db74(0);
}
```

## `CF2Input.GetButtonDown` — RVA `0xc36778`

- Decompiled symbol: `CF2Input_GetButtonDown`
- Metadata signature: `public static bool GetButtonDown(string axisName, ref int cachedId) { }`
- Native interval: `232` bytes
- Result: `pseudocode`

```c
typedef struct struct_4 {
    char padding_0[184];
    struct struct_3 *field_b8;
    char padding_c0[32];
    unsigned int field_e0;
} struct_4;

typedef struct struct_7 {
    char padding_0[184];
    struct struct_6 *field_b8;
    char padding_c0[32];
    unsigned int field_e0;
} struct_7;

typedef struct struct_1 {
    char padding_0[128];
    unsigned long long field_80;
} struct_1;

typedef struct struct_3 {
    char padding_0[24];
    struct struct_2 *field_18;
} struct_3;

typedef struct struct_6 {
    char padding_0[24];
    struct struct_5 *field_18;
} struct_6;

typedef struct struct_2 {
    char padding_0[128];
    long long field_80;
} struct_2;

typedef struct struct_5 {
    char padding_0[128];
    unsigned long long field_80;
} struct_5;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern char g_1036860;
extern struct_4 *g_1eeed00;
extern struct_0 *g_1ef0c58;
extern long long g_1ef9858;
extern char g_1fab16a;
extern char g_1fab1b8;

unsigned long long CF2Input_GetButtonDown(long long a0, long long a1)
{
    struct_4 **v5;  // x22
    long long v6;  // x20
    unsigned long long v15;  // x0
    unsigned long long v16;  // x0
    long long v7;  // x19
    struct_7 *index;  // x0
    struct_1 *v9;  // x21
    long long v10;  // x1
    long long v11;  // x2
    struct_7 *idx;  // x0
    struct_1 *v13;  // x0
    struct_1 *v14;  // x21
    unsigned long v0;  // [bp-0x30]
    struct_4 **v1;  // [bp-0x20]
    struct_1 *v2;  // [bp-0x18]
    long long v3;  // [bp-0x10]
    long long v4;  // [bp-0x8]

    v5 = &g_1eeed00;
    v6 = a1;
    v7 = a0;
    if (!(g_1fab16a & 1))
    {
        sub_f7d92c(&g_1eeed00);
        sub_f7d92c(&g_1ef0c58);
        g_1fab16a = 1;
    }
    index = g_1eeed00;
    if (!g_1eeed00->field_e0)
    {
        sub_f7da5c(g_1eeed00);
        index = g_1eeed00;
    }
    v9 = index->field_b8->field_18;
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v10 = 0;
    v11 = 0;
    if (!((char)Object__op_Inequality(index->field_b8->field_18, 0, 0) & 1))
    {
        v16 = Input__GetButtonDown();
        return Input__GetButtonDown();
    }
    idx = g_1eeed00;
    if (!g_1eeed00->field_e0)
    {
        sub_f7da5c(g_1eeed00);
        idx = g_1eeed00;
    }
    v13 = idx->field_b8->field_18;
    if (idx->field_b8->field_18)
    {
        v10 = v7;
        v11 = v6;
        v6 = v3;
        v7 = v4;
        v5 = v1;
        v9 = v2;
        vvar_31{r256|8b} = v0;
    }
    else
    {
        vvar_101{r256|8b} = (int)&g_1036860;
        v13 = sub_f7db74(0);
    }
    v0 = vvar_31{r256|8b};
    v1 = v5;
    v2 = v9;
    v3 = v6;
    v4 = v7;
    v14 = v13;
    if (!(g_1fab1b8 & 1))
    {
        sub_f7d92c(&g_1ef9858);
        g_1fab1b8 = 1;
    }
    if (v14->field_80)
    {
        if (sub_15264f8(v14->field_80, v10, v11, g_1ef9858))
        {
            v15 = InputRig_AxisConfig__GetButtonDown();
            return InputRig_AxisConfig__GetButtonDown();
        }
        return 0;
    }
    sub_f7db74(0);
}
```

## `CF2Input.GetButtonUp` — RVA `0xc368e4`

- Decompiled symbol: `CF2Input_GetButtonUp`
- Metadata signature: `public static bool GetButtonUp(string axisName) { }`
- Native interval: `212` bytes
- Result: `pseudocode`

```c
typedef struct struct_4 {
    char padding_0[184];
    struct struct_3 *field_b8;
    char padding_c0[32];
    unsigned int field_e0;
} struct_4;

typedef struct struct_7 {
    char padding_0[184];
    struct struct_6 *field_b8;
    char padding_c0[32];
    unsigned int field_e0;
} struct_7;

typedef struct struct_1 {
    char padding_0[128];
    unsigned long long field_80;
} struct_1;

typedef struct struct_3 {
    char padding_0[24];
    struct struct_2 *field_18;
} struct_3;

typedef struct struct_6 {
    char padding_0[24];
    struct struct_5 *field_18;
} struct_6;

typedef struct struct_2 {
    char padding_0[128];
    long long field_80;
} struct_2;

typedef struct struct_5 {
    char padding_0[128];
    unsigned long long field_80;
} struct_5;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern char g_10369b8;
extern struct_4 *g_1eeed00;
extern struct_0 *g_1ef0c58;
extern long long g_1ef9850;
extern char g_1fab16b;
extern char g_1fab1b9;

unsigned long long CF2Input_GetButtonUp(long long a0)
{
    struct_4 **v4;  // x21
    long long v5;  // x19
    struct_7 *index;  // x0
    struct_1 *v7;  // x20
    long long v8;  // x1
    struct_7 *idx;  // x0
    struct_1 *v10;  // x0
    struct_1 *v11;  // x20
    unsigned long long v12;  // x0
    unsigned long v0;  // [bp-0x20]
    struct_4 **v1;  // [bp-0x18]
    struct_1 *v2;  // [bp-0x10]
    long long v3;  // [bp-0x8]

    v4 = &g_1eeed00;
    v5 = a0;
    if (!(g_1fab16b & 1))
    {
        sub_f7d92c(&g_1eeed00);
        sub_f7d92c(&g_1ef0c58);
        g_1fab16b = 1;
    }
    index = g_1eeed00;
    if (!g_1eeed00->field_e0)
    {
        sub_f7da5c(g_1eeed00);
        index = g_1eeed00;
    }
    v7 = index->field_b8->field_18;
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v8 = 0;
    if (((char)Object__op_Inequality(index->field_b8->field_18, 0, 0) & 1))
    {
        idx = g_1eeed00;
        if (!g_1eeed00->field_e0)
        {
            sub_f7da5c(g_1eeed00);
            idx = g_1eeed00;
        }
        v10 = idx->field_b8->field_18;
        if (idx->field_b8->field_18)
        {
            v8 = v5;
            v7 = v2;
            v5 = v3;
            vvar_28{r256|8b} = v0;
            v4 = v1;
        }
        else
        {
            vvar_92{r256|8b} = (int)&g_10369b8;
            v10 = sub_f7db74(0);
        }
        v0 = vvar_28{r256|8b};
        v1 = v4;
        v2 = v7;
        v3 = v5;
        v11 = v10;
        if (!(g_1fab1b9 & 1))
        {
            sub_f7d92c(&g_1ef9850);
            g_1fab1b9 = 1;
        }
        if (v11->field_80)
        {
            if (sub_1526618(v11->field_80, v8, g_1ef9850))
            {
                v12 = InputRig_AxisConfig__GetButtonUp();
                return InputRig_AxisConfig__GetButtonUp();
            }
            return 0;
        }
        sub_f7db74(0);
    }
}
```

## `CF2Input.GetButtonUp` — RVA `0xc36a28`

- Decompiled symbol: `CF2Input_GetButtonUp`
- Metadata signature: `public static bool GetButtonUp(string axisName, ref int cachedId) { }`
- Native interval: `232` bytes
- Result: `pseudocode`

```c
typedef struct struct_4 {
    char padding_0[184];
    struct struct_3 *field_b8;
    char padding_c0[32];
    unsigned int field_e0;
} struct_4;

typedef struct struct_7 {
    char padding_0[184];
    struct struct_6 *field_b8;
    char padding_c0[32];
    unsigned int field_e0;
} struct_7;

typedef struct struct_1 {
    char padding_0[128];
    unsigned long long field_80;
} struct_1;

typedef struct struct_3 {
    char padding_0[24];
    struct struct_2 *field_18;
} struct_3;

typedef struct struct_6 {
    char padding_0[24];
    struct struct_5 *field_18;
} struct_6;

typedef struct struct_2 {
    char padding_0[128];
    long long field_80;
} struct_2;

typedef struct struct_5 {
    char padding_0[128];
    unsigned long long field_80;
} struct_5;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern char g_1036b10;
extern struct_4 *g_1eeed00;
extern struct_0 *g_1ef0c58;
extern long long g_1ef9858;
extern char g_1fab16c;
extern char g_1fab1ba;

unsigned long long CF2Input_GetButtonUp(long long a0, long long a1)
{
    struct_4 **v5;  // x22
    long long v6;  // x20
    unsigned long long v15;  // x0
    long long v7;  // x19
    struct_7 *index;  // x0
    struct_1 *v9;  // x21
    long long v10;  // x1
    long long v11;  // x2
    struct_7 *idx;  // x0
    struct_1 *v13;  // x0
    struct_1 *v14;  // x21
    unsigned long v0;  // [bp-0x30]
    struct_4 **v1;  // [bp-0x20]
    struct_1 *v2;  // [bp-0x18]
    long long v3;  // [bp-0x10]
    long long v4;  // [bp-0x8]

    v5 = &g_1eeed00;
    v6 = a1;
    v7 = a0;
    if (!(g_1fab16c & 1))
    {
        sub_f7d92c(&g_1eeed00);
        sub_f7d92c(&g_1ef0c58);
        g_1fab16c = 1;
    }
    index = g_1eeed00;
    if (!g_1eeed00->field_e0)
    {
        sub_f7da5c(g_1eeed00);
        index = g_1eeed00;
    }
    v9 = index->field_b8->field_18;
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v10 = 0;
    v11 = 0;
    if (((char)Object__op_Inequality(index->field_b8->field_18, 0, 0) & 1))
    {
        idx = g_1eeed00;
        if (!g_1eeed00->field_e0)
        {
            sub_f7da5c(g_1eeed00);
            idx = g_1eeed00;
        }
        v13 = idx->field_b8->field_18;
        if (idx->field_b8->field_18)
        {
            v10 = v7;
            v11 = v6;
            v6 = v3;
            v7 = v4;
            v5 = v1;
            v9 = v2;
            vvar_31{r256|8b} = v0;
        }
        else
        {
            vvar_100{r256|8b} = (int)&g_1036b10;
            v13 = sub_f7db74(0);
        }
        v0 = vvar_31{r256|8b};
        v1 = v5;
        v2 = v9;
        v3 = v6;
        v4 = v7;
        v14 = v13;
        if (!(g_1fab1ba & 1))
        {
            sub_f7d92c(&g_1ef9858);
            g_1fab1ba = 1;
        }
        if (v14->field_80)
        {
            if (sub_15264f8(v14->field_80, v10, v11, g_1ef9858))
            {
                v15 = InputRig_AxisConfig__GetButtonUp();
                return InputRig_AxisConfig__GetButtonUp();
            }
            return 0;
        }
        sub_f7db74(0);
    }
}
```

## `CF2Input.GetKey` — RVA `0xc36b94`

- Decompiled symbol: `CF2Input_GetKey`
- Metadata signature: `public static bool GetKey(KeyCode keyCode) { }`
- Native interval: `212` bytes
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
extern char g_1fab16d;

long long CF2Input_GetKey(unsigned int a0)
{
    struct_1 *v0;  // x0
    struct_1 *v1;  // x0
    unsigned long long v2;  // x0
    unsigned long long v3;  // x0

    if (!(g_1fab16d & 1))
    {
        sub_f7d92c(&g_1eeed00);
        sub_f7d92c(&g_1ef0c58);
        g_1fab16d = 1;
    }
    v0 = g_1eeed00;
    if (!g_1eeed00->field_e0)
    {
        sub_f7da5c(g_1eeed00);
        v0 = g_1eeed00;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (!((char)Object__op_Inequality(v0->field_b8->field_18, 0, 0) & 1))
    {
        v3 = Input__GetKey();
        return Input__GetKey();
    }
    v1 = g_1eeed00;
    if (!g_1eeed00->field_e0)
    {
        sub_f7da5c(g_1eeed00);
        v1 = g_1eeed00;
    }
    if (v1->field_b8->field_18)
    {
        v2 = InputRig__GetKey(v1->field_b8->field_18, a0);
        return InputRig__GetKey(v1->field_b8->field_18, a0);
    }
    sub_f7db74(0);
}
```

## `CF2Input.GetKeyDown` — RVA `0xc36d34`

- Decompiled symbol: `CF2Input_GetKeyDown`
- Metadata signature: `public static bool GetKeyDown(KeyCode keyCode) { }`
- Native interval: `212` bytes
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
extern char g_1fab16e;

long long CF2Input_GetKeyDown(unsigned int a0)
{
    struct_1 *v0;  // x0
    struct_1 *v1;  // x0
    unsigned long long v2;  // x0
    unsigned long long v3;  // x0

    if (!(g_1fab16e & 1))
    {
        sub_f7d92c(&g_1eeed00);
        sub_f7d92c(&g_1ef0c58);
        g_1fab16e = 1;
    }
    v0 = g_1eeed00;
    if (!g_1eeed00->field_e0)
    {
        sub_f7da5c(g_1eeed00);
        v0 = g_1eeed00;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (!((char)Object__op_Inequality(v0->field_b8->field_18, 0, 0) & 1))
    {
        v3 = Input__GetKeyDown();
        return Input__GetKeyDown();
    }
    v1 = g_1eeed00;
    if (!g_1eeed00->field_e0)
    {
        sub_f7da5c(g_1eeed00);
        v1 = g_1eeed00;
    }
    if (v1->field_b8->field_18)
    {
        v2 = InputRig__GetKeyDown(v1->field_b8->field_18, a0);
        return InputRig__GetKeyDown(v1->field_b8->field_18, a0);
    }
    sub_f7db74(0);
}
```

## `CF2Input.GetKeyUp` — RVA `0xc36ef4`

- Decompiled symbol: `CF2Input_GetKeyUp`
- Metadata signature: `public static bool GetKeyUp(KeyCode keyCode) { }`
- Native interval: `212` bytes
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
extern char g_1fab16f;

long long CF2Input_GetKeyUp(unsigned int a0)
{
    struct_1 *v0;  // x0
    struct_1 *v1;  // x0
    unsigned long long v2;  // x0

    if (!(g_1fab16f & 1))
    {
        sub_f7d92c(&g_1eeed00);
        sub_f7d92c(&g_1ef0c58);
        g_1fab16f = 1;
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
        v1 = g_1eeed00;
        if (!g_1eeed00->field_e0)
        {
            sub_f7da5c(g_1eeed00);
            v1 = g_1eeed00;
        }
        if (v1->field_b8->field_18)
        {
            v2 = InputRig__GetKeyUp(v1->field_b8->field_18, a0);
            return InputRig__GetKeyUp(v1->field_b8->field_18, a0);
        }
        sub_f7db74(0);
    }
}
```

## `CF2Input.GetKey` — RVA `0xc370b4`

- Decompiled symbol: `CF2Input_GetKey`
- Metadata signature: `public static bool GetKey(string keyName) { }`
- Native interval: `224` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[184];
    void* field_b8;
    char padding_c0[32];
    unsigned int field_e0;
} struct_0;

typedef struct struct_1 {
    char padding_0[224];
    unsigned int field_e0;
} struct_1;

extern struct_0 *g_1eeed00;
extern struct_1 *g_1ef0c58;
extern char g_1fab170;

unsigned int CF2Input_GetKey(long long a0)
{
    struct_0 *v0;  // x0
    struct_0 *v1;  // x0
    unsigned int v2;  // w0

    if (!(g_1fab170 & 1))
    {
        sub_f7d92c(&g_1eeed00);
        sub_f7d92c(&g_1ef0c58);
        g_1fab170 = 1;
    }
    v0 = g_1eeed00;
    if (!g_1eeed00->field_e0)
    {
        sub_f7da5c(g_1eeed00);
        v0 = g_1eeed00;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (((char)Object__op_Inequality((long long)v0->field_b8[24], 0, 0) & 1))
    {
        v1 = g_1eeed00;
        if (!g_1eeed00->field_e0)
        {
            sub_f7da5c(g_1eeed00);
            v1 = g_1eeed00;
        }
        if ((long long)v1->field_b8[24])
        {
            v2 = InputRig__NameToKeyCode(a0);
            return InputRig__GetKey((long long)v1->field_b8[24], v2);
        }
        sub_f7db74();
    }
}
```

## `CF2Input.GetKeyDown` — RVA `0xc371b4`

- Decompiled symbol: `CF2Input_GetKeyDown`
- Metadata signature: `public static bool GetKeyDown(string keyName) { }`
- Native interval: `224` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[184];
    void* field_b8;
    char padding_c0[32];
    unsigned int field_e0;
} struct_0;

typedef struct struct_1 {
    char padding_0[224];
    unsigned int field_e0;
} struct_1;

extern struct_0 *g_1eeed00;
extern struct_1 *g_1ef0c58;
extern char g_1fab171;

unsigned int CF2Input_GetKeyDown(long long a0)
{
    struct_0 *v0;  // x0
    struct_0 *v1;  // x0
    unsigned int v2;  // w0

    if (!(g_1fab171 & 1))
    {
        sub_f7d92c(&g_1eeed00);
        sub_f7d92c(&g_1ef0c58);
        g_1fab171 = 1;
    }
    v0 = g_1eeed00;
    if (!g_1eeed00->field_e0)
    {
        sub_f7da5c(g_1eeed00);
        v0 = g_1eeed00;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (((char)Object__op_Inequality((long long)v0->field_b8[24], 0, 0) & 1))
    {
        v1 = g_1eeed00;
        if (!g_1eeed00->field_e0)
        {
            sub_f7da5c(g_1eeed00);
            v1 = g_1eeed00;
        }
        if ((long long)v1->field_b8[24])
        {
            v2 = InputRig__NameToKeyCode(a0);
            return InputRig__GetKeyDown((long long)v1->field_b8[24], v2);
        }
        sub_f7db74();
    }
}
```

## `CF2Input.GetKeyUp` — RVA `0xc372b4`

- Decompiled symbol: `CF2Input_GetKeyUp`
- Metadata signature: `public static bool GetKeyUp(string keyName) { }`
- Native interval: `224` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[184];
    void* field_b8;
    char padding_c0[32];
    unsigned int field_e0;
} struct_0;

typedef struct struct_1 {
    char padding_0[224];
    unsigned int field_e0;
} struct_1;

extern struct_0 *g_1eeed00;
extern struct_1 *g_1ef0c58;
extern char g_1fab172;

unsigned int CF2Input_GetKeyUp(long long a0)
{
    struct_0 *v0;  // x0
    struct_0 *v1;  // x0
    unsigned int v2;  // w0

    if (!(g_1fab172 & 1))
    {
        sub_f7d92c(&g_1eeed00);
        sub_f7d92c(&g_1ef0c58);
        g_1fab172 = 1;
    }
    v0 = g_1eeed00;
    if (!g_1eeed00->field_e0)
    {
        sub_f7da5c(g_1eeed00);
        v0 = g_1eeed00;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (((char)Object__op_Inequality((long long)v0->field_b8[24], 0, 0) & 1))
    {
        v1 = g_1eeed00;
        if (!g_1eeed00->field_e0)
        {
            sub_f7da5c(g_1eeed00);
            v1 = g_1eeed00;
        }
        if ((long long)v1->field_b8[24])
        {
            v2 = InputRig__NameToKeyCode(a0);
            return InputRig__GetKeyUp((long long)v1->field_b8[24], v2);
        }
        sub_f7db74();
    }
}
```

## `CF2Input.get_anyKey` — RVA `0xc373b4`

- Decompiled symbol: `CF2Input_get_anyKey`
- Metadata signature: `public static bool get_anyKey() { }`
- Native interval: `212` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    char padding_0[184];
    struct struct_1 *field_b8;
    char padding_c0[32];
    unsigned int field_e0;
} struct_2;

typedef struct struct_0 {
    char padding_0[186];
    char field_ba;
} struct_0;

typedef struct struct_1 {
    char padding_0[24];
    struct struct_0 *field_18;
} struct_1;

typedef struct struct_3 {
    char padding_0[224];
    unsigned int field_e0;
} struct_3;

extern struct_2 *g_1eeed00;
extern struct_3 *g_1ef0c58;
extern char g_1fab173;

unsigned int CF2Input_get_anyKey(void)
{
    struct_2 *v0;  // x0
    struct_2 *v1;  // x0

    if (!(g_1fab173 & 1))
    {
        sub_f7d92c(&g_1eeed00);
        sub_f7d92c(&g_1ef0c58);
        g_1fab173 = 1;
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
        v1 = g_1eeed00;
        if (!g_1eeed00->field_e0)
        {
            sub_f7da5c(g_1eeed00);
            v1 = g_1eeed00;
        }
        if (!v1->field_b8->field_18)
        {
            sub_f7db74();
        }
        else if (v1->field_b8->field_18->field_ba)
        {
            return 1;
        }
    }
}
```

## `CF2Input.get_anyKeyDown` — RVA `0xc374a0`

- Decompiled symbol: `CF2Input_get_anyKeyDown`
- Metadata signature: `public static bool get_anyKeyDown() { }`
- Native interval: `212` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    char padding_0[184];
    struct struct_1 *field_b8;
    char padding_c0[32];
    unsigned int field_e0;
} struct_2;

typedef struct struct_0 {
    char padding_0[187];
    char field_bb;
} struct_0;

typedef struct struct_1 {
    char padding_0[24];
    struct struct_0 *field_18;
} struct_1;

typedef struct struct_3 {
    char padding_0[224];
    unsigned int field_e0;
} struct_3;

extern struct_2 *g_1eeed00;
extern struct_3 *g_1ef0c58;
extern char g_1fab174;

unsigned int CF2Input_get_anyKeyDown(void)
{
    struct_2 *v0;  // x0
    struct_2 *v1;  // x0

    if (!(g_1fab174 & 1))
    {
        sub_f7d92c(&g_1eeed00);
        sub_f7d92c(&g_1ef0c58);
        g_1fab174 = 1;
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
        v1 = g_1eeed00;
        if (!g_1eeed00->field_e0)
        {
            sub_f7da5c(g_1eeed00);
            v1 = g_1eeed00;
        }
        if (!v1->field_b8->field_18)
        {
            sub_f7db74();
        }
        else if (v1->field_b8->field_18->field_bb)
        {
            return 1;
        }
    }
    return Input__get_anyKeyDown();
}
```

## `CF2Input.get_touchCount` — RVA `0xc3758c`

- Decompiled symbol: `CF2Input_get_touchCount`
- Metadata signature: `public static int get_touchCount() { }`
- Native interval: `200` bytes
- Result: `pseudocode`

```c
typedef struct struct_5 {
    char padding_0[184];
    struct struct_4 *field_b8;
    char padding_c0[32];
    unsigned int field_e0;
} struct_5;

typedef struct struct_10 {
    char padding_0[184];
    struct struct_9 *field_b8;
    char padding_c0[32];
    unsigned int field_e0;
} struct_10;

typedef struct struct_1 {
    char padding_0[360];
    struct struct_0 *field_168;
} struct_1;

typedef struct struct_11 {
    char padding_0[24];
    unsigned int field_18;
} struct_11;

typedef struct struct_4 {
    char padding_0[24];
    struct struct_3 *field_18;
} struct_4;

typedef struct struct_9 {
    char padding_0[24];
    struct struct_8 *field_18;
} struct_9;

typedef struct struct_0 {
    char padding_0[24];
    unsigned int field_18;
} struct_0;

typedef struct struct_3 {
    char padding_0[360];
    struct struct_2 *field_168;
} struct_3;

typedef struct struct_8 {
    char padding_0[360];
    struct struct_7 *field_168;
} struct_8;

typedef struct struct_2 {
    char padding_0[24];
    unsigned int field_18;
} struct_2;

typedef struct struct_7 {
    char padding_0[24];
    unsigned int field_18;
} struct_7;

typedef struct struct_6 {
    char padding_0[224];
    unsigned int field_e0;
} struct_6;

extern char g_1037654;
extern struct_5 *g_1eeed00;
extern struct_6 *g_1ef0c58;
extern long long g_1ef90f8;
extern char g_1fab175;
extern char g_1fab1d8;

int CF2Input_get_touchCount(void)
{
    struct_5 **v3;  // x20
    struct_10 *index;  // x0
    struct_1 *v5;  // x19
    struct_10 *idx;  // x0
    struct_1 *v7;  // x0
    unsigned long v0;  // [bp-0x20]
    struct_5 **v1;  // [bp-0x10]
    struct_1 *v2;  // [bp-0x8]

    v3 = &g_1eeed00;
    if (!(g_1fab175 & 1))
    {
        sub_f7d92c(&g_1eeed00);
        sub_f7d92c(&g_1ef0c58);
        g_1fab175 = 1;
    }
    index = g_1eeed00;
    if (!g_1eeed00->field_e0)
    {
        sub_f7da5c(g_1eeed00);
        index = g_1eeed00;
    }
    v5 = index->field_b8->field_18;
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (!((char)Object__op_Inequality(index->field_b8->field_18, 0, 0) & 1))
        return Input__get_touchCount();
    idx = g_1eeed00;
    if (!g_1eeed00->field_e0)
    {
        sub_f7da5c(g_1eeed00);
        idx = g_1eeed00;
    }
    v7 = idx->field_b8->field_18;
    if (idx->field_b8->field_18)
    {
        v3 = v1;
        v5 = v2;
        vvar_25{r256|8b} = v0;
    }
    else
    {
        vvar_84{r256|8b} = (int)&g_1037654;
        v7 = sub_f7db74(0);
    }
    v0 = vvar_25{r256|8b};
    v1 = v3;
    v2 = v5;
    if (!(g_1fab1d8 & 1))
    {
        sub_f7d92c(&g_1ef90f8);
        g_1fab1d8 = 1;
    }
    if (v7->field_168)
        return v7->field_168->field_18;
    sub_f7db74();
}
```

## `CF2Input.get_touches` — RVA `0xc3769c`

- Decompiled symbol: `CF2Input_get_touches`
- Metadata signature: `public static InputRig.Touch[] get_touches() { }`
- Native interval: `256` bytes
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

typedef struct struct_3 {
    char padding_0[224];
    unsigned int field_e0;
} struct_3;

extern struct_1 *g_1eeed00;
extern struct_2 *g_1ef0c58;
extern struct_3 *g_1ef3368;
extern char g_1fab176;

long long CF2Input_get_touches(void)
{
    struct_1 *v0;  // x0
    struct_1 *v1;  // x0
    unsigned long long v2;  // x0
    long long v3;  // x0
    unsigned long long v4;  // x0

    if (!(g_1fab176 & 1))
    {
        sub_f7d92c(&g_1eeed00);
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c(&g_1ef3368);
        g_1fab176 = 1;
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
        v1 = g_1eeed00;
        if (!g_1eeed00->field_e0)
        {
            sub_f7da5c(g_1eeed00);
            v1 = g_1eeed00;
        }
        if (v1->field_b8->field_18)
        {
            v2 = InputRig__GetEmuTouchArray(v1->field_b8->field_18);
            return InputRig__GetEmuTouchArray(v1->field_b8->field_18);
        }
        sub_f7db74(0);
    }
    else
    {
        v3 = Input__get_touches(0);
        if (!g_1ef3368->field_e0)
            sub_f7da5c(g_1ef3368);
        v4 = InputRig_Touch__TranslateUnityTouches(v3, 0);
        return InputRig_Touch__TranslateUnityTouches(v3, 0);
    }
}
```

## `CF2Input.GetTouch` — RVA `0xc37908`

- Decompiled symbol: `CF2Input_GetTouch`
- Metadata signature: `public static InputRig.Touch GetTouch(int i) { }`
- Native interval: `304` bytes
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
extern char g_1fab177;

long long CF2Input_GetTouch(unsigned int a0)
{
    struct_1 *v2;  // x0
    struct_1 *v3;  // x0
    unsigned long long dst;  // x0
    unsigned long v6;  // x8
    unsigned long long v7;  // x0
    char v0;  // [bp-0xc0]
    char v1;  // [bp-0x78]

    if (!(g_1fab177 & 1))
    {
        sub_f7d92c(&g_1eeed00);
        sub_f7d92c(&g_1ef0c58);
        g_1fab177 = 1;
    }
    v2 = g_1eeed00;
    if (!g_1eeed00->field_e0)
    {
        sub_f7da5c(g_1eeed00);
        v2 = g_1eeed00;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (!((char)Object__op_Inequality(v2->field_b8->field_18, 0, 0) & 1))
    {
        Input__GetTouch(a0, 0);
        memcpy(&v0, &v1, 68);
        memset(v6, 0, 68);
        v7 = InputRig_Touch__ctor(v6, &v0, 0);
        return InputRig_Touch__ctor(v6, &v0, 0);
    }
    v3 = g_1eeed00;
    if (!g_1eeed00->field_e0)
    {
        sub_f7da5c(g_1eeed00);
        v3 = g_1eeed00;
    }
    if (v3->field_b8->field_18)
    {
        InputRig__GetEmuTouch();
        dst = memcpy(v6, &v1, 68);
        return memcpy(v6, &v1, 68);
    }
    sub_f7db74(0);
}
```

## `CF2Input.GetMouseButton` — RVA `0xc37afc`

- Decompiled symbol: `CF2Input_GetMouseButton`
- Metadata signature: `public static bool GetMouseButton(int mouseButton) { }`
- Native interval: `236` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[184];
    void* field_b8;
    char padding_c0[32];
    unsigned int field_e0;
} struct_0;

typedef struct struct_1 {
    char padding_0[224];
    unsigned int field_e0;
} struct_1;

extern struct_0 *g_1eeed00;
extern struct_1 *g_1ef0c58;
extern char g_1fab178;

unsigned int CF2Input_GetMouseButton(unsigned int a0)
{
    struct_0 *v0;  // x0
    struct_0 *v1;  // x0

    if (!(g_1fab178 & 1))
    {
        sub_f7d92c(&g_1eeed00);
        sub_f7d92c(&g_1ef0c58);
        g_1fab178 = 1;
    }
    v0 = g_1eeed00;
    if (!g_1eeed00->field_e0)
    {
        sub_f7da5c(g_1eeed00);
        v0 = g_1eeed00;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (!((char)Object__op_Inequality((long long)v0->field_b8[24], 0, 0) & 1))
        return Input__GetMouseButton();
    v1 = g_1eeed00;
    if (!g_1eeed00->field_e0)
    {
        sub_f7da5c(g_1eeed00);
        v1 = g_1eeed00;
    }
    if ((long long)v1->field_b8[24])
    {
        if (6 >= a0)
            return InputRig__GetKey((long long)v1->field_b8[24], a0 + 323);
        return 0;
    }
    sub_f7db74(0);
}
```

## `CF2Input.GetMouseButtonDown` — RVA `0xc37c00`

- Decompiled symbol: `CF2Input_GetMouseButtonDown`
- Metadata signature: `public static bool GetMouseButtonDown(int mouseButton) { }`
- Native interval: `236` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[184];
    void* field_b8;
    char padding_c0[32];
    unsigned int field_e0;
} struct_0;

typedef struct struct_1 {
    char padding_0[224];
    unsigned int field_e0;
} struct_1;

extern struct_0 *g_1eeed00;
extern struct_1 *g_1ef0c58;
extern char g_1fab179;

unsigned int CF2Input_GetMouseButtonDown(unsigned int a0)
{
    struct_0 *v0;  // x0
    struct_0 *v1;  // x0

    if (!(g_1fab179 & 1))
    {
        sub_f7d92c(&g_1eeed00);
        sub_f7d92c(&g_1ef0c58);
        g_1fab179 = 1;
    }
    v0 = g_1eeed00;
    if (!g_1eeed00->field_e0)
    {
        sub_f7da5c(g_1eeed00);
        v0 = g_1eeed00;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (((char)Object__op_Inequality((long long)v0->field_b8[24], 0, 0) & 1))
    {
        v1 = g_1eeed00;
        if (!g_1eeed00->field_e0)
        {
            sub_f7da5c(g_1eeed00);
            v1 = g_1eeed00;
        }
        if ((long long)v1->field_b8[24])
        {
            if (6 >= a0)
                return InputRig__GetKeyDown((long long)v1->field_b8[24], a0 + 323);
            return 0;
        }
        sub_f7db74(0);
    }
}
```

## `CF2Input.GetMouseButtonUp` — RVA `0xc37d04`

- Decompiled symbol: `CF2Input_GetMouseButtonUp`
- Metadata signature: `public static bool GetMouseButtonUp(int mouseButton) { }`
- Native interval: `236` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[184];
    void* field_b8;
    char padding_c0[32];
    unsigned int field_e0;
} struct_0;

typedef struct struct_1 {
    char padding_0[224];
    unsigned int field_e0;
} struct_1;

extern struct_0 *g_1eeed00;
extern struct_1 *g_1ef0c58;
extern char g_1fab17a;

unsigned int CF2Input_GetMouseButtonUp(unsigned int a0)
{
    struct_0 *v0;  // x0
    struct_0 *v1;  // x0

    if (!(g_1fab17a & 1))
    {
        sub_f7d92c(&g_1eeed00);
        sub_f7d92c(&g_1ef0c58);
        g_1fab17a = 1;
    }
    v0 = g_1eeed00;
    if (!g_1eeed00->field_e0)
    {
        sub_f7da5c(g_1eeed00);
        v0 = g_1eeed00;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (((char)Object__op_Inequality((long long)v0->field_b8[24], 0, 0) & 1))
    {
        v1 = g_1eeed00;
        if (!g_1eeed00->field_e0)
        {
            sub_f7da5c(g_1eeed00);
            v1 = g_1eeed00;
        }
        if ((long long)v1->field_b8[24])
        {
            if (6 >= a0)
                return InputRig__GetKeyUp((long long)v1->field_b8[24], a0 + 323);
            return 0;
        }
        sub_f7db74(0);
    }
}
```

## `CF2Input.get_mousePosition` — RVA `0xc37e08`

- Decompiled symbol: `CF2Input_get_mousePosition`
- Metadata signature: `public static Vector3 get_mousePosition() { }`
- Native interval: `212` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    char padding_0[184];
    struct struct_1 *field_b8;
    char padding_c0[32];
    unsigned int field_e0;
} struct_2;

typedef struct struct_0 {
    char padding_0[280];
    long long field_118;
} struct_0;

typedef struct struct_1 {
    char padding_0[24];
    struct struct_0 *field_18;
} struct_1;

typedef struct struct_3 {
    char padding_0[224];
    unsigned int field_e0;
} struct_3;

extern struct_2 *g_1eeed00;
extern struct_3 *g_1ef0c58;
extern char g_1fab17b;

long long CF2Input_get_mousePosition(void)
{
    struct_2 *v0;  // x0
    unsigned long long v1;  // x0
    struct_2 *v2;  // x0
    unsigned long long v3;  // x0

    if (!(g_1fab17b & 1))
    {
        sub_f7d92c(&g_1eeed00);
        sub_f7d92c(&g_1ef0c58);
        g_1fab17b = 1;
    }
    v0 = g_1eeed00;
    if (!g_1eeed00->field_e0)
    {
        sub_f7da5c(g_1eeed00);
        v0 = g_1eeed00;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (((char)Object__op_Equality(v0->field_b8->field_18, 0, 0) & 1))
    {
        v1 = Input__get_mousePosition();
        return Input__get_mousePosition();
    }
    v2 = g_1eeed00;
    if (!g_1eeed00->field_e0)
    {
        sub_f7da5c(g_1eeed00);
        v2 = g_1eeed00;
    }
    if (v2->field_b8->field_18 && v2->field_b8->field_18->field_118)
    {
        v3 = InputRig_MouseConfig__GetPosition(v2->field_b8->field_18->field_118, 0);
        return InputRig_MouseConfig__GetPosition(v2->field_b8->field_18->field_118, 0);
    }
    sub_f7db74();
}
```

## `CF2Input.get_mouseScrollDelta` — RVA `0xc37edc`

- Decompiled symbol: `CF2Input_get_mouseScrollDelta`
- Metadata signature: `public static Vector2 get_mouseScrollDelta() { }`
- Native interval: `240` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    char padding_0[184];
    struct struct_1 *field_b8;
    char padding_c0[32];
    unsigned int field_e0;
} struct_2;

typedef struct struct_0 {
    char padding_0[288];
    long long field_120;
} struct_0;

typedef struct struct_1 {
    char padding_0[24];
    struct struct_0 *field_18;
} struct_1;

typedef struct struct_3 {
    char padding_0[224];
    unsigned int field_e0;
} struct_3;

extern struct_2 *g_1eeed00;
extern struct_3 *g_1ef0c58;
extern char g_1fab17c;

long long CF2Input_get_mouseScrollDelta(void)
{
    struct_2 *v0;  // x0
    unsigned long long v1;  // x0
    struct_2 *idx;  // x0
    struct_0 *v3;  // x8
    unsigned long long v4;  // x0

    if (!(g_1fab17c & 1))
    {
        sub_f7d92c(&g_1eeed00);
        sub_f7d92c(&g_1ef0c58);
        g_1fab17c = 1;
    }
    v0 = g_1eeed00;
    if (!g_1eeed00->field_e0)
    {
        sub_f7da5c(g_1eeed00);
        v0 = g_1eeed00;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (((char)Object__op_Equality(v0->field_b8->field_18, 0, 0) & 1))
    {
        Input__get_mouseScrollDelta(0);
        v1 = Input__get_mouseScrollDelta(0);
        return Input__get_mouseScrollDelta(0);
    }
    idx = g_1eeed00;
    if (!g_1eeed00->field_e0)
    {
        sub_f7da5c(g_1eeed00);
        idx = g_1eeed00;
    }
    v3 = idx->field_b8->field_18;
    if (v3 && v3->field_120)
    {
        v4 = InputRig_ScrollWheelState__GetDelta(v3->field_120, 0);
        return InputRig_ScrollWheelState__GetDelta(v3->field_120, 0);
    }
    sub_f7db74();
}
```

## `CF2Input.get_simulateMouseWithTouches` — RVA `0xc37fcc`

- Decompiled symbol: `CF2Input_get_simulateMouseWithTouches`
- Metadata signature: `public static bool get_simulateMouseWithTouches() { }`
- Native interval: `192` bytes
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
    char padding_5[19];
    long long field_18;
} struct_0;

typedef struct struct_2 {
    char padding_0[224];
    unsigned int field_e0;
} struct_2;

extern struct_1 *g_1eeed00;
extern struct_2 *g_1ef0c58;
extern char g_1fab17d;

long long CF2Input_get_simulateMouseWithTouches(void)
{
    struct_1 *v0;  // x0
    unsigned long long v1;  // x0
    struct_1 *v2;  // x0

    if (!(g_1fab17d & 1))
    {
        sub_f7d92c(&g_1eeed00);
        sub_f7d92c(&g_1ef0c58);
        g_1fab17d = 1;
    }
    v0 = g_1eeed00;
    if (!g_1eeed00->field_e0)
    {
        sub_f7da5c(g_1eeed00);
        v0 = g_1eeed00;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (((char)Object__op_Equality(v0->field_b8->field_18, 0, 0) & 1))
    {
        v1 = Input__get_simulateMouseWithTouches();
        return Input__get_simulateMouseWithTouches();
    }
    v2 = g_1eeed00;
    if (!g_1eeed00->field_e0)
    {
        sub_f7da5c(g_1eeed00);
        v2 = g_1eeed00;
    }
    return v2->field_b8->field_4;
}
```

## `CF2Input.set_simulateMouseWithTouches` — RVA `0xc3808c`

- Decompiled symbol: `CF2Input_set_simulateMouseWithTouches`
- Metadata signature: `public static void set_simulateMouseWithTouches(bool value) { }`
- Native interval: `200` bytes
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
    char padding_5[19];
    long long field_18;
} struct_0;

typedef struct struct_2 {
    char padding_0[224];
    unsigned int field_e0;
} struct_2;

extern struct_1 *g_1eeed00;
extern struct_2 *g_1ef0c58;
extern char g_1fab17e;

void CF2Input_set_simulateMouseWithTouches(char a0)
{
    unsigned long long v4;  // x30
    unsigned long long v5;  // x21
    unsigned long long v6;  // x20
    unsigned long long v7;  // x19
    struct_1 *ptr;  // x0
    struct_0 *p;  // x8
    struct_1 *v10;  // x0
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x18]
    unsigned long long v2;  // [bp-0x10]
    unsigned long long v3;  // [bp-0x8]

    v0 = v4;
    v1 = v5;
    v2 = v6;
    v3 = v7;
    if (!(g_1fab17e & 1))
    {
        sub_f7d92c(&g_1eeed00);
        sub_f7d92c(&g_1ef0c58);
        g_1fab17e = 1;
    }
    ptr = g_1eeed00;
    if (!g_1eeed00->field_e0)
    {
        sub_f7da5c(g_1eeed00);
        ptr = g_1eeed00;
    }
    p = ptr->field_b8;
    p->field_4 = a0 & 1;
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (((char)Object__op_Equality(p->field_18, 0, 0) & 1))
    {
        v10 = g_1eeed00;
        if (!g_1eeed00->field_e0)
        {
            sub_f7da5c(g_1eeed00);
            v10 = g_1eeed00;
        }
    }
    Input__set_simulateMouseWithTouches();
    return;
}
```

## `CF2Input.CalibrateTilt` — RVA `0xc38154`

- Decompiled symbol: `CF2Input_CalibrateTilt`
- Metadata signature: `public static void CalibrateTilt() { }`
- Native interval: `288` bytes
- Result: `pseudocode`

```c
typedef struct struct_3 {
    char padding_0[184];
    struct struct_2 *field_b8;
    char padding_c0[32];
    unsigned int field_e0;
} struct_3;

typedef struct struct_1 {
    char padding_0[272];
    struct struct_0 *field_110;
} struct_1;

typedef struct struct_0 {
    char padding_0[24];
    long long field_18;
} struct_0;

typedef struct struct_2 {
    char padding_0[24];
    struct struct_1 *field_18;
} struct_2;

typedef struct struct_4 {
    char padding_0[224];
    unsigned int field_e0;
} struct_4;

extern char g_1038274;
extern struct_3 *g_1eeed00;
extern struct_4 *g_1ef0c58;
extern char g_1fab17f;
extern char g_1fab1df;

long long CF2Input_CalibrateTilt(void)
{
    struct_3 *v1;  // x0
    long long v2;  // x0
    struct_3 *idx;  // x0
    struct_1 *v4;  // x0
    unsigned long long v5;  // x0
    unsigned long v0;  // [bp-0x10]

    if (!(g_1fab17f & 1))
    {
        sub_f7d92c(&g_1eeed00);
        sub_f7d92c(&g_1ef0c58);
        g_1fab17f = 1;
    }
    if (!g_1eeed00->field_e0)
        sub_f7da5c(g_1eeed00);
    if (!g_1fab1df)
    {
        sub_f7d92c(&g_1eeed00);
        g_1fab1df = 1;
    }
    v1 = g_1eeed00;
    if (!g_1eeed00->field_e0)
    {
        sub_f7da5c(g_1eeed00);
        v1 = g_1eeed00;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v2 = Object__op_Inequality(v1->field_b8->field_18, 0, 0);
    if (!((char)v2 & 1))
        return v2;
    if (!g_1eeed00->field_e0)
        sub_f7da5c(g_1eeed00);
    if (!g_1fab1df)
    {
        sub_f7d92c(&g_1eeed00);
        g_1fab1df = 1;
    }
    idx = g_1eeed00;
    if (!g_1eeed00->field_e0)
    {
        sub_f7da5c(g_1eeed00);
        idx = g_1eeed00;
    }
    v4 = idx->field_b8->field_18;
    if (!idx->field_b8->field_18)
    {
        vvar_123{r256|8b} = (int)&g_1038274;
        v4 = sub_f7db74(0);
    }
    v0 = vvar_44{r256|8b};
    if (v4->field_110 && v4->field_110->field_18)
    {
        v5 = TiltState__Calibate(v4->field_110->field_18, 0);
        return TiltState__Calibate(v4->field_110->field_18, 0);
    }
    sub_f7db74();
}
```

## `CF2Input.cctor` — RVA `0xc38298`

- Decompiled symbol: `CF2Input_cctor`
- Metadata signature: `private static void .cctor() { }`
- Native interval: `76` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

typedef struct struct_0 {
    char padding_0[184];
    struct struct_1 *field_b8;
} struct_0;

extern struct_0 *g_1eeed00;
extern char g_1fab180;

unsigned long long CF2Input_cctor(void)
{
    unsigned long long v0;  // x0

    if (!(g_1fab180 & 1))
    {
        v0 = sub_f7d92c(&g_1eeed00);
        g_1fab180 = 1;
    }
    g_1eeed00->field_b8->field_0 = 1;
    return v0;
}
```
