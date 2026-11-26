# Native pseudocode: TouchControl.HitPool

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `TouchControl.HitPool.ctor` — RVA `0xc534a4`

- Decompiled symbol: `TouchControl_HitPool_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `136` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[32];
    long long field_20;
} struct_0;

extern long long g_1ef3c88;
extern long long g_1ef9be8;
extern char g_1fab25e;

void TouchControl_HitPool_ctor(struct_0 *ptr)
{
    unsigned long long v5;  // x30
    unsigned long long v6;  // x22
    unsigned long long v7;  // x21
    unsigned long long v8;  // x20
    unsigned long long v9;  // x19
    long long v10;  // x0
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
    if (!(g_1fab25e & 1))
    {
        sub_f7d92c(&g_1ef3c88);
        sub_f7d92c(&g_1ef9be8);
        g_1fab25e = 1;
    }
    sub_155e530(ptr, g_1ef9be8);
    v10 = sub_f7db70(g_1ef3c88);
    Object__ctor(v10, 0);
    ptr->field_20 = v10;
    sub_f7d8d0();
    return;
}
```

## `TouchControl.HitPool.HitTestAny` — RVA `0xc5352c`

- Decompiled symbol: `TouchControl_HitPool_HitTestAny`
- Metadata signature: `public bool HitTestAny(List<TouchControl> controlList, Vector2 screenPos, Camera cam, float fingerRadPx = 0.0, TouchControl.HitPool.TouchControlFilterFunc filter) { }`
- Native interval: `460` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[32];
    struct struct_0 *field_20;
} struct_1;

typedef struct struct_2 {
    char padding_0[24];
    int field_18;
} struct_2;

typedef struct struct_3 {
    char padding_0[24];
    struct struct_4 *field_18;
    char padding_20[8];
    unsigned long long field_28;
    char padding_30[16];
    unsigned long long field_40;
} struct_3;

typedef struct struct_0 {
    char padding_0[16];
    unsigned long long field_10;
} struct_0;

typedef struct struct_4 {
    unsigned long long field_0;
} struct_4;

extern struct_0 *g_1ef0c58;
extern long long g_1ef8a30;
extern long long g_1ef8a38;
extern long long g_1ef9bf0;
extern long long g_1ef9bf8;
extern long long g_1ef9c08;
extern char g_1fab25f;

unsigned int TouchControl_HitPool_HitTestAny(struct_1 *a0, struct_2 *p, long long a2, struct_3 *ptr, unsigned long a4)
{
    unsigned int v0;  // w25
    int v1;  // w23
    unsigned long v2;  // x24
    unsigned long v3;  // cc_dep1
    unsigned long v4;  // cc_dep2
    unsigned long v5;  // 4102
    unsigned long v6;  // 4102
    unsigned long long v7;  // x0
    unsigned long long v8;  // x2
    unsigned long v9;  // x1

    if (!(g_1fab25f & 1))
    {
        sub_f7d92c(&g_1ef8a30);
        sub_f7d92c(&g_1ef8a38);
        sub_f7d92c(&g_1ef9bf0);
        sub_f7d92c(&g_1ef9bf8);
        sub_f7d92c(&g_1ef9c08);
        sub_f7d92c(&g_1ef0c58);
        g_1fab25f = 1;
    }
    sub_155ea34(a0, 1, g_1ef9bf8);
    sub_155e84c(a0, g_1ef9bf0);
    if (!p)
        sub_f7db74();
    if (p->field_18 <= 0)
        v0 = 0;
    else
        v0 = 1;
    if (p->field_18 < 1)
        return v0 & 1;
    v1 = 0;
    while (true)
    {
        v2 = sub_14a30c0(p, v1, g_1ef8a38);
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        if (!((char)Object__op_Equality(v2, 0, 0) & 1))
            break;
        v1 += 1;
        v3 = v1;
        v4 = p->field_18;
        if (p->field_18 <= v1)
        {
            v5 = arm64g_calculate_condition(179, v3, v4, 0);
            if (!((char)v5))
                return 0;
        }
        else
        {
            v6 = arm64g_calculate_condition(179, v3, v4, 0);
            if (!((char)v6))
                return 1;
        }
    }
    if (ptr)
    {
        v7 = ptr->field_40;
        v8 = ptr->field_28;
        v9 = v2;
        ptr->field_18();
    }
    if (v2)
        TouchControl__HitTest(v2, a2, a0->field_20); /* do not return */
    sub_f7db74();
}
```

## `TouchControl.HitPool.HitTest` — RVA `0xc536f8`

- Decompiled symbol: `TouchControl_HitPool_HitTest`
- Metadata signature: `public int HitTest(List<TouchControl> controlList, Vector2 screenPos, Camera cam, int maxHits = 8, float fingerRadPx = 0.0, TouchControl.HitPool.TouchControlFilterFunc filter) { }`
- Native interval: `812` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[32];
    struct struct_0 *field_20;
} struct_1;

typedef struct struct_2 {
    char padding_0[24];
    int field_18;
} struct_2;

typedef struct struct_3 {
    char padding_0[24];
    struct struct_4 *field_18;
    char padding_20[8];
    unsigned long long field_28;
    char padding_30[16];
    unsigned long long field_40;
} struct_3;

typedef struct struct_0 {
    char padding_0[16];
    unsigned long long field_10;
} struct_0;

typedef struct struct_4 {
    unsigned long long field_0;
} struct_4;

extern struct_0 *g_1ef0c58;
extern long long g_1ef8a30;
extern long long g_1ef8a38;
extern long long g_1ef9360;
extern long long g_1ef9368;
extern long long g_1ef9370;
extern long long g_1ef9378;
extern long long g_1ef9bf0;
extern long long g_1ef9bf8;
extern long long g_1ef9c00;
extern long long g_1ef9c08;
extern long long g_1ef9c10;
extern char g_1fab260;

void TouchControl_HitPool_HitTest(struct_1 *a0, struct_2 *a1, long long a2, int a3, struct_3 *ptr)
{
    unsigned long long v17;  // d10
    unsigned long long v18;  // d9
    unsigned long long v27;  // x22
    unsigned long long v28;  // x21
    unsigned long long v29;  // x20
    unsigned long long v30;  // x19
    int v31;  // w23
    int v32;  // w24
    unsigned long v33;  // x26
    unsigned long long v34;  // x0
    unsigned long long v35;  // x2
    unsigned long v36;  // x1
    unsigned long long v19;  // d8
    unsigned long long v20;  // x30
    unsigned long long v21;  // x28
    unsigned long long v22;  // x27
    unsigned long long v23;  // x26
    unsigned long long v24;  // x25
    unsigned long long v25;  // x24
    unsigned long long v26;  // x23
    unsigned long long v0;  // [bp-0x80]
    int v1;  // [bp-0x74]
    unsigned long long v2;  // [bp-0x70]
    unsigned long long v3;  // [bp-0x68]
    char *v4;  // [bp-0x60]
    unsigned long long v5;  // [bp-0x58]
    unsigned long long v6;  // [bp-0x50]
    unsigned long long v7;  // [bp-0x48]
    unsigned long long v8;  // [bp-0x40]
    unsigned long long v9;  // [bp-0x38]
    unsigned long long v10;  // [bp-0x30]
    unsigned long long v11;  // [bp-0x28]
    unsigned long long v12;  // [bp-0x20]
    unsigned long long v13;  // [bp-0x18]
    unsigned long long v14;  // [bp-0x10]
    unsigned long long v15;  // [bp-0x8]
    char v16;  // [bp+0x0]

    v0 = v17;
    v2 = v18;
    v3 = v19;
    v4 = &v16;
    v5 = v20;
    v6 = v21;
    v7 = v22;
    v8 = v23;
    v9 = v24;
    v10 = v25;
    v11 = v26;
    v12 = v27;
    v13 = v28;
    v14 = v29;
    v15 = v30;
    v31 = a3;
    if (!(g_1fab260 & 1))
    {
        sub_f7d92c(&g_1ef9360);
        sub_f7d92c(&g_1ef9368);
        sub_f7d92c(&g_1ef9370);
        sub_f7d92c(&g_1ef8a30);
        sub_f7d92c(&g_1ef8a38);
        sub_f7d92c(&g_1ef9378);
        sub_f7d92c(&g_1ef9bf0);
        sub_f7d92c(&g_1ef9bf8);
        sub_f7d92c(&g_1ef9c00);
        sub_f7d92c(&g_1ef9c08);
        sub_f7d92c(&g_1ef9c10);
        sub_f7d92c(&g_1ef0c58);
        g_1fab260 = 1;
    }
    if (1 >= v31)
        v31 = 1;
    sub_155e84c();
    v1 = v31;
    sub_155ea34(a0, v31, g_1ef9bf8);
    if (a1)
    {
        if (a1->field_18 >= 1)
        {
            v32 = 0;
            while (true)
            {
                v33 = sub_14a30c0(a1, v32, g_1ef8a38);
                if (!g_1ef0c58->field_e0)
                    sub_f7da5c(g_1ef0c58);
                if (!((char)Object__op_Equality(v33, 0, 0) & 1))
                    break;
                v32 += 1;
                if (v32 >= a1->field_18)
                {
                    sub_155e608();
                    return;
                }
            }
            if (ptr)
            {
                v34 = ptr->field_40;
                v35 = ptr->field_28;
                v36 = v33;
                ptr->field_18();
            }
            else if (v33)
            {
                TouchControl__HitTest(v33, a2, a0->field_20); /* do not return */
            }
        }
        else
        {
            sub_155e608();
            return;
        }
    }
    sub_f7db74();
}
```

## `TouchControl.HitPool.CreateInternalObject` — RVA `0xc53a24`

- Decompiled symbol: `TouchControl_HitPool_CreateInternalObject`
- Metadata signature: `protected override TouchControl.Hit CreateInternalObject() { }`
- Native interval: `84` bytes
- Result: `pseudocode`

```c
extern long long g_1ef3c88;
extern char g_1fab261;

long long TouchControl_HitPool_CreateInternalObject(void)
{
    long long v0;  // x0

    if (!(g_1fab261 & 1))
    {
        sub_f7d92c(&g_1ef3c88);
        g_1fab261 = 1;
    }
    v0 = sub_f7db70(g_1ef3c88);
    Object__ctor(v0, 0);
    return v0;
}
```
