# Native pseudocode: TouchControlSpriteAnimatorBase

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `TouchControlSpriteAnimatorBase.ctor` — RVA `0xc63a74`

- Decompiled symbol: `TouchControlSpriteAnimatorBase_ctor`
- Metadata signature: `public void .ctor(Type sourceType) { }`
- Native interval: `216` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[48];
    long long field_30;
    char padding_38[64];
    struct struct_0 *field_78;
} struct_1;

typedef struct struct_2 {
    char padding_0[16];
    char field_10;
    char padding_11[15];
    uint128_t field_20;
    unsigned long long field_30;
    char padding_38[11];
    char field_43;
    uint128_t field_44;
    unsigned long long field_54;
} struct_2;

typedef struct struct_0 {
    char padding_0[16];
    char field_10;
    char padding_11[15];
    uint128_t field_20;
    unsigned long long field_30;
    char padding_38[11];
    char field_43;
    uint128_t field_44;
    unsigned long long field_54;
} struct_0;

extern long long g_1ef1838;
extern char g_1fab2e9;

long long TouchControlSpriteAnimatorBase_ctor(struct_1 *p, long long a1)
{
    struct_2 *ptr;  // x20
    struct_1 *v1;  // x19
    unsigned long v2;  // x0

    if (!(g_1fab2e9 & 1))
    {
        sub_f7d92c(&g_1ef1838);
        g_1fab2e9 = 1;
    }
    ComponentBase__ctor(p, 0);
    p->field_30 = a1;
    sub_f7d8d0((struct struct_1 *)&p->field_30, a1);
    ptr = sub_f7db70(g_1ef1838);
    Object__ctor(ptr, 0);
    ptr->field_43 = 0;
    ptr->field_10 = 1;
    *((unsigned long long *)&ptr->field_20) = 0x3f8000003f800000 CONCAT 0x3f8000003f800000;
    *((unsigned long long *)((char *)&ptr->field_44 + 4)) = 0x3f8000003f800000;
    ptr->field_30 = 0x3f800000;
    *((uint128_t *)&(&ptr->field_43)[1]) = 84405977751994456057500319505265249485;
    p->field_78 = ptr;
    v1 = &p->field_78;
    v2 = sub_f7d8d0(v1, ptr);
    if (*((long long *)&v1->padding_0[0]))
    {
        *((uint128_t *)(*((long long *)&v1->padding_0[0]) + 32)) = 0x3ea8f5c33f8000003f8000003f800000;
        return v2;
    }
    sub_f7db74();
}
```

## `TouchControlSpriteAnimatorBase.OnInitComponent` — RVA `0xc63b4c`

- Decompiled symbol: `TouchControlSpriteAnimatorBase_OnInitComponent`
- Metadata signature: `protected override void OnInitComponent() { }`
- Native interval: `692` bytes
- Result: `pseudocode`

```c
typedef struct struct_3 {
    char padding_0[56];
    long long field_38;
    struct struct_4 *field_40;
    long long field_48;
    unsigned int field_50;
    unsigned int field_54;
    unsigned int field_58;
    unsigned int field_5c;
    unsigned int field_60;
    unsigned int field_64;
    unsigned int field_68;
    unsigned int field_6c;
    unsigned int field_70;
    unsigned int field_74;
    long long field_78;
    char padding_80[20];
    uint128_t field_94;
    uint128_t field_a4;
    uint128_t field_b4;
    uint128_t field_c4;
    unsigned long long field_d4;
    unsigned long long field_dc;
    unsigned long long field_e4;
    unsigned int field_ec;
} struct_3;

typedef struct struct_5 {
    char padding_0[712];
    struct struct_6 *field_2c8;
    unsigned long long field_2d0;
} struct_5;

typedef struct struct_7 {
    char padding_0[184];
    struct struct_8 *field_b8;
} struct_7;

typedef struct struct_4 {
    struct struct_1 *field_0;
} struct_4;

typedef struct struct_6 {
    unsigned long long field_0;
} struct_6;

typedef struct struct_8 {
    unsigned long long field_0;
    unsigned long long field_8;
} struct_8;

typedef struct struct_1 {
    char padding_0[712];
    struct struct_2 *field_2c8;
    unsigned long long field_2d0;
} struct_1;

typedef struct struct_2 {
    unsigned long long field_0;
} struct_2;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern struct_7 *g_1ef22b8;
extern long long g_1efcfd0;
extern long long g_1efd060;
extern long long g_1efeab8;
extern long long g_1efeb78;
extern char g_1fab1e0;
extern char g_1fab2ea;
extern char g_1fab32a;

long long TouchControlSpriteAnimatorBase_OnInitComponent(struct_3 *ptr)
{
    long long v0;  // x1
    struct_3 *addr;  // x0
    struct_3 *ptr3;  // x0
    struct_5 **v11;  // x20
    unsigned int v12;  // s0
    unsigned int v13;  // s1
    unsigned int v14;  // s2
    unsigned int v15;  // s3
    struct_7 *off;  // x8
    unsigned long long v17;  // d0
    unsigned long long v19;  // d2
    struct_3 *v2;  // x20
    int v20;  // q2
    unsigned long v21;  // x1
    unsigned long long v22;  // x0
    struct_3 *p;  // x20
    struct_5 **v4;  // x0
    struct_5 **v5;  // x0
    struct_5 **v6;  // x0
    unsigned long long flag;  // x1
    unsigned long v8;  // x2
    long long v9;  // x1

    if (!(g_1fab2ea & 1))
    {
        sub_f7d92c(&g_1efcfd0);
        sub_f7d92c(&g_1efd060);
        sub_f7d92c(&g_1efeab8);
        sub_f7d92c(&g_1efeb78);
        sub_f7d92c(&g_1ef0c58);
        g_1fab2ea = 1;
    }
    TouchControlAnimatorBase__OnInitComponent(ptr);
    v0 = sub_1231bc8(ptr, g_1efd060);
    addr = ptr;
    addr->field_38 = v0;
    sub_f7d8d0((struct struct_3 *)&addr->field_38, v0);
    v2 = ptr;
    p = &v2->field_40;
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (((char)Object__op_Equality(v2->field_40, 0, 0) & 1))
    {
        v4 = sub_1231bc8(ptr, g_1efcfd0);
        ptr->field_40 = v4;
        sub_f7d8d0(p, v4);
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        if (((char)Object__op_Equality(ptr->field_40, 0, 0) & 1))
        {
            v5 = Component__get_gameObject(ptr, 0);
            if (!v5)
                sub_f7db74(v5);
            v6 = sub_124913c();
            *((struct_5 ***)&p->padding_0[0]) = v6;
            sub_f7d8d0(p, v6);
        }
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (((char)Object__op_Inequality(*((long long *)&p->padding_0[0]), 0, 0) & 1))
    {
        v5 = *((long long *)&p->padding_0[0]);
        if (v5)
        {
            flag = 0;
            v8 = *(v5)->field_2d0;
            *(v5)->field_2c8();
        }
    }
    else
    {
        v5 = Component__get_gameObject(ptr, 0);
        if (v5)
        {
            v9 = sub_1249224();
            ptr3 = ptr;
            ptr3->field_48 = v9;
            sub_f7d8d0((struct struct_3 *)&ptr3->field_48, v9);
            v5 = Component__get_transform(ptr, 0);
            if (v5)
            {
                v11 = v5;
                Transform__get_localPosition();
                ptr->field_50 = v12;
                ptr->field_54 = v13;
                ptr->field_58 = v14;
                Transform__get_localScale(v11, 0);
                ptr->field_5c = v12;
                ptr->field_60 = v13;
                ptr->field_64 = v14;
                Transform__get_localRotation(v11, 0);
                ptr->field_68 = v12;
                ptr->field_6c = v13;
                ptr->field_70 = v14;
                ptr->field_74 = v15;
                if (!g_1fab1e0)
                {
                    sub_f7d92c(&g_1ef22b8);
                    g_1fab1e0 = 1;
                }
                off = g_1ef22b8;
                v17 = g_1ef22b8->field_b8->field_0;
                *((unsigned long long *)((char *)&ptr->field_c4 + 12)) = v17;
                *((unsigned int *)&(&ptr->padding_80)[1]) = _INSERT(v17, 8, v17);
                if (!g_1fab32a)
                {
                    sub_f7d92c(&g_1ef22b8);
                    off = g_1ef22b8;
                    g_1fab32a = 1;
                }
                v19 = off->field_b8->field_8;
                *((unsigned long *)((char *)&ptr->field_c4 + 4)) = 0x3f8000003f800000;
                *((void*)((char *)&ptr->field_a4 + 4)) = 0x3f8000003f8000000000000000000000;
                *((unsigned long long *)((char *)&ptr->field_d4 + 4)) = v19;
                v20 = (int)_INSERT(v19, 8, v19);
                v21 = ptr->field_78;
                *((unsigned int *)((char *)&ptr->field_dc + 4)) = 0;
                *((void*)((char *)&ptr->field_94 + 4)) = v20;
                *((unsigned long long *)((char *)&ptr->field_b4 + 4)) = 0x3f8000003f800000 CONCAT 0x3f8000003f800000;
                v22 = TouchControlSpriteAnimatorBase__BeginSpriteAnim(ptr, v21, 1, 1);
                return TouchControlSpriteAnimatorBase__BeginSpriteAnim(ptr, v21, 1, 1);
            }
        }
    }
    sub_f7db74(v5);
}
```

## `TouchControlSpriteAnimatorBase.BeginSpriteAnim` — RVA `0xc63e00`

- Decompiled symbol: `TouchControlSpriteAnimatorBase_BeginSpriteAnim`
- Metadata signature: `protected void BeginSpriteAnim(SpriteConfig spriteConfig, bool skipAnim, bool forceStart = false) { }`
- Native interval: `492` bytes
- Result: `pseudocode`

```c
typedef struct struct_4 {
    char padding_0[32];
    uint128_t field_20;
    char padding_30[4];
    unsigned int field_34;
    unsigned long long field_38;
    char field_40;
    char field_41;
    char field_42;
    char field_43;
} struct_4;

typedef struct struct_1 {
    unsigned long long field_0;
    unsigned long long field_8;
} struct_1;

typedef struct struct_0 {
    char padding_0[184];
    struct struct_1 *field_b8;
} struct_0;

extern struct_0 *g_1ef22b8;
extern char g_1fab1e0;
extern char g_1fab32a;

void* TouchControlSpriteAnimatorBase_BeginSpriteAnim(void* ptr, struct_4 *p, unsigned int a2, unsigned long a3)
{
    struct_4 *v2;  // x8
    void* addr;  // x20
    unsigned long v12;  // x10
    unsigned int v13;  // s0
    struct_4 *v14;  // x8
    unsigned long v4;  // x22
    unsigned long v5;  // x0
    void* v6;  // x0
    unsigned long v8;  // d0
    unsigned int v10;  // s0
    void* v11;  // x0
    int v0;  // [bp-0x50]
    int v1;  // [bp-0x40]

    v2 = (long long)ptr[128];
    addr = ptr + 128;
    v4 = a2;
    if (v2 == p)
    {
        if (!p)
        {
            sub_f7db74();
        }
        else if (!p->field_43 && !((char)v4 & 1))
        {
            return ptr;
        }
    }
    if (v2 && v2->field_43 && !((char)v4 & 1) && !((char)a3 & 1))
    {
        *((struct_4 **)&ptr[136]) = p;
        v5 = sub_f7d8d0(ptr + 136, p);
        return sub_f7d8d0(ptr + 136, p);
    }
    *((struct_4 **)&ptr[128]) = p;
    sub_f7d8d0(addr, p);
    *((unsigned int *)&ptr[144]) = 0;
    if (!((char)v4 & 1))
    {
        *((int128_t *)&ptr[188]) = (int128_t)ptr[204];
        v11 = CFUtils__get_editorStopped(0);
        if (((char)v11 & 1))
            return v11;
        v12 = (long long)ptr[172];
        v13 = (int)ptr[184];
        v14 = (long long)ptr[128];
        *((long long *)&ptr[148]) = (long long)ptr[156];
        *((unsigned long *)&ptr[164]) = v12;
        *((unsigned int *)&ptr[180]) = v13;
        if (v14)
        {
            if (v14->field_42)
            {
                if (!g_1fab32a)
                {
                    v11 = sub_f7d92c(&g_1ef22b8);
                    g_1fab32a = 1;
                    v14 = *((long long *)addr);
                }
                *((unsigned long long *)&ptr[164]) = g_1ef22b8->field_b8->field_8;
                if (v14)
                    goto LABEL_1063f88;
            }
            else
            {
LABEL_1063f88:
                if (v14->field_40)
                {
                    if (!g_1fab1e0)
                    {
                        v11 = sub_f7d92c(&g_1ef22b8);
                        g_1fab1e0 = 1;
                        v14 = *((long long *)addr);
                    }
                    *((unsigned long long *)&ptr[148]) = g_1ef22b8->field_b8->field_0;
                    if (v14)
                        goto LABEL_1063fc8;
                }
                else
                {
LABEL_1063fc8:
                    if (!v14->field_41)
                        return v11;
                    *((unsigned int *)&ptr[180]) = 0;
                    return v11;
                }
            }
        }
    }
    else if (p)
    {
        v0 = (int)p->field_20;
        v1 = (int)p->field_20;
        *((uint128_t *)&ptr[204]) = p->field_20;
        ptr[188] = v1;
        v6 = CFUtils__get_editorStopped(0);
        if (((char)v6 & 1))
            return v6;
        *((unsigned int *)&ptr[148]) = _INSERT(p->field_38, 8, p->field_38);
        if (!g_1fab32a)
        {
            sub_f7d92c(&g_1ef22b8);
            g_1fab32a = 1;
        }
        v8 = [D] unsupported_Iop_ZeroHI64ofV128();
        *((unsigned int *)&ptr[164]) = _INSERT(v8, 8, v8);
        v10 = p->field_34;
        *((unsigned int *)&ptr[180]) = v10;
        *((unsigned int *)&ptr[184]) = v10;
        TouchControlSpriteAnimatorBase__ApplySpriteAnimation(ptr); /* do not return */
    }
    sub_f7db74();
}
```

## `TouchControlSpriteAnimatorBase.OnDisableComponent` — RVA `0xc63fec`

- Decompiled symbol: `TouchControlSpriteAnimatorBase_OnDisableComponent`
- Metadata signature: `protected override void OnDisableComponent() { }`
- Native interval: `132` bytes
- Result: `pseudocode`

```c
int TouchControlSpriteAnimatorBase_OnDisableComponent(long long a0)
{
    unsigned long long v0;  // x0

    v0 = CFUtils__get_editorStopped(0);
    if (((char)v0 & 1))
        return v0;
    if (Component__get_transform(a0, 0))
    {
        Transform__set_localPosition();
        if (Component__get_transform(a0, 0))
        {
            Transform__set_localScale();
            if (Component__get_transform(a0, 0))
                return Transform__set_localRotation();
        }
    }
    sub_f7db74();
}
```

## `TouchControlSpriteAnimatorBase.ApplySpriteAnimation` — RVA `0xc64070`

- Decompiled symbol: `TouchControlSpriteAnimatorBase_ApplySpriteAnimation`
- Metadata signature: `public void ApplySpriteAnimation() { }`
- Native interval: `788` bytes
- Result: `pseudocode`
- Heuristic layout hint: `TouchControlSpriteAnimatorBase_Recovered` matched 2 offsets against `TouchControlSpriteAnimatorBase` metadata (confidence 0.67).

```c
typedef struct TouchControlSpriteAnimatorBase_Recovered {
    char padding_0[64];
    struct struct_4 *image;
    struct struct_4 *canvasGroup;
    char padding_50[136];
    unsigned int field_d8;
} TouchControlSpriteAnimatorBase_Recovered;

typedef struct struct_1 {
    char padding_0[680];
    struct struct_2 *field_2a8;
    unsigned long long field_2b0;
} struct_1;

typedef struct struct_4 {
    struct struct_1 *field_0;
} struct_4;

typedef struct struct_2 {
    unsigned long long field_0;
} struct_2;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab2eb;

void TouchControlSpriteAnimatorBase_ApplySpriteAnimation(struct_3 *ptr, unsigned long a1)
{
    unsigned long long v8;  // d11
    unsigned long long v9;  // d10
    unsigned long v18;  // 4132
    unsigned int v19;  // w8
    struct_1 **v20;  // x20
    unsigned long long flag;  // x2
    unsigned long long v23;  // x1
    unsigned long long v10;  // d9
    unsigned long long v11;  // d8
    unsigned long long v12;  // x30
    unsigned long long v13;  // x21
    unsigned long long v14;  // x20
    unsigned long long v15;  // x19
    struct_1 **v16;  // x0
    unsigned int v17;  // s8
    unsigned long long v0;  // [bp-0x40]
    unsigned long long v1;  // [bp-0x38]
    unsigned long long v2;  // [bp-0x30]
    unsigned long long v3;  // [bp-0x28]
    unsigned long long v4;  // [bp-0x20]
    unsigned long long v5;  // [bp-0x18]
    unsigned long long v6;  // [bp-0x10]
    unsigned long long v7;  // [bp-0x8]

    v0 = v8;
    v1 = v9;
    v2 = v10;
    v3 = v11;
    v4 = v12;
    v5 = v13;
    v6 = v14;
    v7 = v15;
    if (!(g_1fab2eb & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab2eb = 1;
    }
    v16 = ptr->field_40;
    if (v16)
    {
        v17 = ptr->field_d8;
        v16 = Behaviour__get_enabled(v16, 0);
        v18 = arm64g_calculate_condition(192, (((((unsigned long long)(char)(CmpF(v17, 925353388)) >> 5 & 3 | (unsigned long long)(CmpF(v17, 925353388) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v17, 925353388)) >> 5 & 3 | (unsigned long long)(CmpF(v17, 925353388) & 1)) & ((unsigned long long)(char)(CmpF(v17, 925353388)) >> 5 & 3 | (unsigned long long)(CmpF(v17, 925353388) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if ((char)v18)
            v19 = 0;
        else
            v19 = 1;
        if (!(((char)v19 ^ (char)v16) & 1))
        {
            v20 = ptr->field_40;
            if (v20)
            {
                Behaviour__set_enabled(v20, ~((unsigned int)Behaviour__get_enabled(v20, 0)) & 1, 0);
                goto LABEL_10640fc;
            }
        }
        else
        {
LABEL_10640fc:
            if (!g_1ef0c58->field_e0)
                sub_f7da5c(g_1ef0c58);
            flag = 0;
            if (((char)Object__op_Inequality(ptr->field_48, 0, 0) & 1))
            {
                v16 = ptr->field_48;
                if (v16)
                {
                    CanvasGroup__set_alpha(v16, 0);
                    goto LABEL_106414c;
                }
            }
            else
            {
LABEL_106414c:
                v16 = ptr->field_40;
                if (v16)
                {
                    v23 = *(v16)->field_2b0;
                    *(v16)->field_2a8();
                }
            }
        }
    }
    sub_f7db74(v16);
}
```

## `TouchControlSpriteAnimatorBase.UpdateSpriteAnimation` — RVA `0xc64384`

- Decompiled symbol: `TouchControlSpriteAnimatorBase_UpdateSpriteAnimation`
- Metadata signature: `protected void UpdateSpriteAnimation(bool skipAnim) { }`
- Native interval: `700` bytes
- Result: `pseudocode`
- Heuristic layout hint: `TouchControlSpriteAnimatorBase_Recovered` matched 5 offsets against `TouchControlSpriteAnimatorBase` metadata (confidence 0.71).

```c
typedef struct TouchControlSpriteAnimatorBase_Recovered {
    struct struct_4 *field_0;
    char padding_8[32];
    struct struct_4 *field_28;
    char padding_30[80];
    struct struct_2 *curSprite;
    unsigned long long nextSprite;
    unsigned int spriteAnimElapsed;
    char padding_94[40];
    uint128_t animColorStart;
    uint128_t animColorCur;
} TouchControlSpriteAnimatorBase_Recovered;

typedef struct struct_2 {
    char padding_0[32];
    uint128_t field_20;
    char padding_30[19];
    char field_43;
    unsigned int field_44;
    unsigned int field_48;
    unsigned int field_4c;
} struct_2;

typedef struct struct_0 {
    char padding_0[856];
    struct struct_1 *field_358;
    unsigned long long field_360;
} struct_0;

typedef struct struct_4 {
    char padding_0[32];
    uint128_t field_20;
    char padding_30[4];
    unsigned int field_34;
    unsigned long long field_38;
    char field_40;
    char field_41;
    char field_42;
    char field_43;
} struct_4;

typedef struct struct_4 {
    struct struct_0 *field_0;
} struct_4;

typedef struct struct_1 {
    unsigned long long field_0;
} struct_1;

void TouchControlSpriteAnimatorBase_UpdateSpriteAnimation(struct_3 *ptr, unsigned int a1)
{
    unsigned long long v7;  // d9
    unsigned long long v8;  // d8
    unsigned int v17;  // s1
    unsigned long v18;  // 4129
    unsigned long long v19;  // x2
    unsigned long long v20;  // x3
    unsigned long long v21;  // x8
    unsigned int v22;  // s2
    unsigned int v23;  // s3
    unsigned int v24;  // s4
    struct_0 **v25;  // x0
    unsigned long v26;  // 4162
    unsigned long long v9;  // x30
    unsigned long long v27;  // cc_dep1
    unsigned long v28;  // 4106
    unsigned int v29;  // s4
    unsigned int v30;  // s3
    unsigned long v31;  // 4133
    unsigned long long v32;  // x1
    unsigned long long v10;  // x21
    unsigned long long v11;  // x20
    unsigned long long v12;  // x19
    unsigned long v13;  // x20
    struct_2 *p;  // x8
    unsigned int v15;  // s0
    unsigned int v16;  // s0
    uint128_t v0;  // [bp-0x40]
    unsigned long long v1;  // [bp-0x30]
    unsigned long long v2;  // [bp-0x28]
    unsigned long long v3;  // [bp-0x20]
    unsigned long long v4;  // [bp-0x18]
    unsigned long long v5;  // [bp-0x10]
    unsigned long long v6;  // [bp-0x8]

    v1 = v7;
    v2 = v8;
    v3 = v9;
    v4 = v10;
    v5 = v11;
    v6 = v12;
    v13 = a1;
    CFUtils__get_realDeltaTimeClamped(0);
    p = ptr->field_80;
    v16 = ptr->field_90 + v15;
    ptr->field_90 = v16;
    if (p)
    {
        if (p->field_43)
        {
            v17 = p->field_44;
            v18 = arm64g_calculate_condition(176, (((((unsigned long long)(char)(CmpF(v16, v17)) >> 5 & 3 | (unsigned long long)(CmpF(v16, v17) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v16, v17)) >> 5 & 3 | (unsigned long long)(CmpF(v16, v17) & 1)) & ((unsigned long long)(char)(CmpF(v16, v17)) >> 5 & 3 | (unsigned long long)(CmpF(v16, v17) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
            if (!((char)v18))
            {
                v19 = (unsigned int)v13 & 1;
                v20 = 1;
                v21 = 120;
                if (ptr->field_88)
                    v21 = 136;
                TouchControlSpriteAnimatorBase__BeginSpriteAnim(ptr, *((long long *)((char *)ptr + v21)), v19, 1);
                p = ptr->field_80;
            }
        }
        if (p)
        {
            v22 = 0;
            v23 = 0;
            if (!((char)v13 & 1))
                v23 = p->field_4c * p->field_48;
            v24 = ptr->field_90;
            v25 = ptr->field_28;
            v26 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v24, v23)) >> 5 & 3 | (unsigned long long)(CmpF(v24, v23) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v24, v23)) >> 5 & 3 | (unsigned long long)(CmpF(v24, v23) & 1)) & ((unsigned long long)(char)(CmpF(v24, v23)) >> 5 & 3 | (unsigned long long)(CmpF(v24, v23) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
            if ((char)v26)
                v27 = ((((CmpF(v23, 925353388) >> 5 & 3 | CmpF(v23, 925353388) & 1) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - ((CmpF(v23, 925353388) >> 5 & 3 | CmpF(v23, 925353388) & 1) & (CmpF(v23, 925353388) >> 5 & 3 | CmpF(v23, 925353388) & 1) >> 1 & 1)) * 0x10000000;
            else
                v27 = 0x80000000;
            v28 = arm64g_calculate_condition(64, v27, 0, 0);
            if ((char)v28)
                v29 = 0x3f800000;
            else
                v29 = v24 / v23;
            v30 = [D] unsupported_Iop_ZeroHI96ofV128();
            v31 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v29, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v29, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v29, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v29, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v29, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v29, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
            if ((char)v31)
                v22 = v30;
            v0 = *((int128_t *)&(&ptr->padding_94)[1]) + (p->field_20 - *((int128_t *)&(&ptr->padding_94)[1])) * ((int)v22 * 0x100000000 | (int)v22 CONCAT (int)v22 * 0x100000000 | (int)v22);
            *((uint128_t *)((char *)&ptr->field_bc + 12)) = v0;
            if (v25)
            {
                v32 = *(v25)->field_360;
                *(v25)->field_358();
            }
        }
    }
    sub_f7db74();
}
```

## `TouchControlSpriteAnimatorBase.GetAnimLerpFactor` — RVA `0xc64640`

- Decompiled symbol: `TouchControlSpriteAnimatorBase_GetAnimLerpFactor`
- Metadata signature: `private float GetAnimLerpFactor(float duration) { }`
- Native interval: `36` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: previous decompile attempt stalled on this RVA; preserve it as instruction fallback

```c
// 0x1064640: ldr s1, [x0, #0x90]
// 0x1064644: adrp x8, #0x832000
// 0x1064648: ldr s2, [x8, #0x41c]
// 0x106464c: fcmp s1, s0
// 0x1064650: fdiv s1, s1, s0
// 0x1064654: fccmp s0, s2, #8, le
// 0x1064658: fmov s0, #1.00000000
// 0x106465c: fcsel s0, s0, s1, mi
// 0x1064660: ret
```
