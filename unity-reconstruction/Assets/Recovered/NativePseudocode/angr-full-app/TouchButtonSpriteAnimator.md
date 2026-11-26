# Native pseudocode: TouchButtonSpriteAnimator

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `TouchButtonSpriteAnimator.ctor` — RVA `0xc44644`

- Decompiled symbol: `TouchButtonSpriteAnimator_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `384` bytes
- Result: `pseudocode`
- Heuristic layout hint: `TouchButtonSpriteAnimator_Recovered` matched 3 offsets against `TouchButtonSpriteAnimator` metadata (confidence 1.00).

```c
typedef struct TouchButtonSpriteAnimator_Recovered {
    char padding_0[240];
    struct struct_1 *spritePressed;
    struct struct_2 *spriteToggled;
    struct struct_3 *spriteToggledAndPressed;
} TouchButtonSpriteAnimator_Recovered;

typedef struct struct_5 {
    char padding_0[48];
    unsigned int field_30;
} struct_5;

typedef struct struct_6 {
    char padding_0[48];
    unsigned int field_30;
} struct_6;

typedef struct struct_7 {
    char padding_0[48];
    unsigned int field_30;
} struct_7;

typedef struct struct_1 {
    char padding_0[48];
    unsigned int field_30;
} struct_1;

typedef struct struct_2 {
    char padding_0[48];
    unsigned int field_30;
} struct_2;

typedef struct struct_3 {
    char padding_0[48];
    unsigned int field_30;
} struct_3;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern long long g_1eebac8;
extern long long g_1ef1838;
extern struct_0 *g_1ef1f08;
extern char g_1fab218;

void TouchButtonSpriteAnimator_ctor(struct_4 *ptr)
{
    struct_5 *v1;  // x20
    struct_4 *v2;  // x21
    struct_6 *v3;  // x20
    struct_4 *p;  // x19
    struct_7 *v5;  // x22
    struct_4 *v6;  // x20

    if (!(g_1fab218 & 1))
    {
        sub_f7d92c(&g_1ef1838);
        sub_f7d92c(&g_1eebac8);
        sub_f7d92c(&g_1ef1f08);
        g_1fab218 = 1;
    }
    if (!g_1ef1f08->field_e0)
        sub_f7da5c(g_1ef1f08);
    TouchControlSpriteAnimatorBase__ctor(ptr, Type__GetTypeFromHandle(g_1eebac8, 0), 0);
    v1 = sub_f7db70(g_1ef1838);
    SpriteConfig__ctor(v1, 1, 0, 0);
    ptr->field_f0 = v1;
    v2 = &ptr->field_f0;
    sub_f7d8d0(v2, v1);
    v3 = sub_f7db70(g_1ef1838);
    SpriteConfig__ctor(v3, 0, 0, 0);
    ptr->field_f8 = v3;
    p = &ptr->field_f8;
    sub_f7d8d0(p, v3);
    v5 = sub_f7db70(g_1ef1838);
    SpriteConfig__ctor(v5, 0, 0, 0);
    v6 = &p->padding_0[8];
    *((struct_7 **)&p->padding_0[8]) = v5;
    sub_f7d8d0(v6, v5);
    if (*((long long *)&v2->padding_0[0]))
    {
        *((unsigned int *)(*((long long *)&v2->padding_0[0]) + 48)) = 0x3fa00000;
        if (*((long long *)&p->padding_0[0]))
        {
            *((unsigned int *)(*((long long *)&p->padding_0[0]) + 48)) = 1066192077;
            if (*((long long *)&v6->padding_0[0]))
            {
                *((unsigned int *)(*((long long *)&v6->padding_0[0]) + 48)) = 1067869798;
                return;
            }
        }
    }
    sub_f7db74();
}
```

## `TouchButtonSpriteAnimator.SetSprite` — RVA `0xc447c4`

- Decompiled symbol: `TouchButtonSpriteAnimator_SetSprite`
- Metadata signature: `public void SetSprite(Sprite sprite) { }`
- Native interval: `104` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    long long field_18;
} struct_0;

void TouchButtonSpriteAnimator_SetSprite(struct_0 **ptr, long long a1)
{
    unsigned long long v3;  // x30
    unsigned long long v4;  // x20
    unsigned long long v5;  // x19
    struct_0 *p;  // x0
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x10]
    unsigned long long v2;  // [bp-0x8]

    v0 = v3;
    v1 = v4;
    v2 = v5;
    p = ptr[15];
    if (p)
    {
        p->field_18 = a1;
        sub_f7d8d0((struct struct_0 *)&p->field_18);
        p = ptr[30];
        if (p)
        {
            p->field_18 = a1;
            sub_f7d8d0((struct struct_0 *)&p->field_18, a1);
            p = ptr[31];
            if (p)
            {
                p->field_18 = a1;
                sub_f7d8d0((struct struct_0 *)&p->field_18, a1);
                p = ptr[32];
                if (p)
                {
                    p->field_18 = a1;
                    sub_f7d8d0();
                    return;
                }
            }
        }
    }
    sub_f7db74(p);
}
```

## `TouchButtonSpriteAnimator.SetColor` — RVA `0xc4482c`

- Decompiled symbol: `TouchButtonSpriteAnimator_SetColor`
- Metadata signature: `public void SetColor(Color color) { }`
- Native interval: `80` bytes
- Result: `pseudocode`
- Heuristic layout hint: `TouchButtonSpriteAnimator_Recovered` matched 3 offsets against `TouchButtonSpriteAnimator` metadata (confidence 0.75).

```c
typedef struct TouchButtonSpriteAnimator_Recovered {
    char padding_0[120];
    struct struct_1 *field_78;
    char padding_80[112];
    struct struct_2 *spritePressed;
    struct struct_3 *spriteToggled;
    struct struct_4 *spriteToggledAndPressed;
} TouchButtonSpriteAnimator_Recovered;

typedef struct struct_1 {
    char padding_0[32];
    unsigned int field_20;
    unsigned int field_24;
    unsigned int field_28;
    unsigned int field_2c;
} struct_1;

typedef struct struct_2 {
    char padding_0[32];
    unsigned int field_20;
    unsigned int field_24;
    unsigned int field_28;
    unsigned int field_2c;
} struct_2;

typedef struct struct_3 {
    char padding_0[32];
    unsigned int field_20;
    unsigned int field_24;
    unsigned int field_28;
    unsigned int field_2c;
} struct_3;

typedef struct struct_4 {
    char padding_0[32];
    unsigned int field_20;
    unsigned int field_24;
    unsigned int field_28;
    unsigned int field_2c;
} struct_4;

void TouchButtonSpriteAnimator_SetColor(struct_0 *ptr, unsigned long a1)
{
    unsigned int p[12];  // x8
    unsigned int v1;  // s0
    unsigned int v2;  // s1
    unsigned int v3;  // s2
    unsigned int v4;  // s3
    unsigned int addr[12];  // x8
    unsigned int ptr3[12];  // x8
    unsigned int ptr4[12];  // x8

    p = ptr->field_78;
    if (p)
    {
        p[8] = v1;
        p[9] = v2;
        p[10] = v3;
        p[11] = v4;
        addr = ptr->field_f0;
        if (addr)
        {
            addr[8] = v1;
            addr[9] = v2;
            addr[10] = v3;
            addr[11] = v4;
            ptr3 = ptr->field_f8;
            if (ptr3)
            {
                ptr3[8] = v1;
                ptr3[9] = v2;
                ptr3[10] = v3;
                ptr3[11] = v4;
                ptr4 = ptr->field_100;
                if (ptr4)
                {
                    ptr4[8] = v1;
                    ptr4[9] = v2;
                    ptr4[10] = v3;
                    ptr4[11] = v4;
                    return;
                }
            }
        }
    }
    sub_f7db74();
}
```

## `TouchButtonSpriteAnimator.SetStateSprite` — RVA `0xc4487c`

- Decompiled symbol: `TouchButtonSpriteAnimator_SetStateSprite`
- Metadata signature: `public void SetStateSprite(TouchButtonSpriteAnimator.ControlState state, Sprite sprite) { }`
- Native interval: `96` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    long long field_18;
} struct_0;

extern char g_8520cc;

void TouchButtonSpriteAnimator_SetStateSprite(struct_0 **a0, unsigned int a1, long long a2)
{
    if (3 < a1)
    {
        TouchButtonSpriteAnimator__SetSprite(a0, a2);
        return;
    }
    goto sub_10448a0 + (&g_8520cc)[a1] * 4;
}
```

## `TouchButtonSpriteAnimator.GetStateSpriteConfig` — RVA `0xc448dc`

- Decompiled symbol: `TouchButtonSpriteAnimator_GetStateSpriteConfig`
- Metadata signature: `public SpriteConfig GetStateSpriteConfig(TouchButtonSpriteAnimator.ControlState state) { }`
- Native interval: `80` bytes
- Result: `pseudocode`

```c
extern char g_8520d0;

unsigned int TouchButtonSpriteAnimator_GetStateSpriteConfig(unsigned long a0, unsigned int a1)
{
    if (3 < a1)
        return 0;
    goto sub_1044900 + (&g_8520d0)[a1] * 4;
}
```

## `TouchButtonSpriteAnimator.SetStateColor` — RVA `0xc4492c`

- Decompiled symbol: `TouchButtonSpriteAnimator_SetStateColor`
- Metadata signature: `public void SetStateColor(TouchButtonSpriteAnimator.ControlState state, Color color) { }`
- Native interval: `88` bytes
- Result: `pseudocode`
- Heuristic layout hint: `TouchButtonSpriteAnimator_Recovered` matched 3 offsets against `TouchButtonSpriteAnimator` metadata (confidence 0.75).

```c
typedef struct TouchButtonSpriteAnimator_Recovered {
    char padding_0[120];
    struct struct_1 *field_78;
    char padding_80[112];
    struct struct_2 *spritePressed;
    struct struct_3 *spriteToggled;
    struct struct_4 *spriteToggledAndPressed;
} TouchButtonSpriteAnimator_Recovered;

typedef struct struct_1 {
    char padding_0[32];
    unsigned int field_20;
    unsigned int field_24;
    unsigned int field_28;
    unsigned int field_2c;
} struct_1;

typedef struct struct_2 {
    char padding_0[32];
    unsigned int field_20;
    unsigned int field_24;
    unsigned int field_28;
    unsigned int field_2c;
} struct_2;

typedef struct struct_3 {
    char padding_0[32];
    unsigned int field_20;
    unsigned int field_24;
    unsigned int field_28;
    unsigned int field_2c;
} struct_3;

typedef struct struct_4 {
    char padding_0[32];
    unsigned int field_20;
    unsigned int field_24;
    unsigned int field_28;
    unsigned int field_2c;
} struct_4;

extern char g_8520cc;

long long TouchButtonSpriteAnimator_SetStateColor(struct_0 *a0, unsigned int a1)
{
    unsigned long v0;  // x0

    if (3 < a1)
    {
        v0 = (unsigned long long)TouchButtonSpriteAnimator__SetColor(a0, a1);
        return (unsigned long long)TouchButtonSpriteAnimator__SetColor(a0, a1);
    }
    goto sub_1044950 + (&g_8520cc)[a1 & 4294967295] * 4;
}
```

## `TouchButtonSpriteAnimator.OnInitComponent` — RVA `0xc44984`

- Decompiled symbol: `TouchButtonSpriteAnimator_OnInitComponent`
- Metadata signature: `protected override void OnInitComponent() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long TouchButtonSpriteAnimator_OnInitComponent(unsigned long a0)
{
    unsigned long long v0;  // x0

    v0 = TouchControlSpriteAnimatorBase__OnInitComponent();
    return TouchControlSpriteAnimatorBase__OnInitComponent();
}
```

## `TouchButtonSpriteAnimator.OnUpdateAnimator` — RVA `0xc4498c`

- Decompiled symbol: `TouchButtonSpriteAnimator_OnUpdateAnimator`
- Metadata signature: `protected override void OnUpdateAnimator(bool skipAnim) { }`
- Native interval: `392` bytes
- Result: `pseudocode`
- Heuristic layout hint: `TouchButtonSpriteAnimator_Recovered` matched 3 offsets against `TouchButtonSpriteAnimator` metadata (confidence 0.60).

```c
typedef struct TouchButtonSpriteAnimator_Recovered {
    char padding_0[40];
    struct struct_4 *field_28;
    char padding_30[16];
    long long field_40;
    char padding_48[168];
    struct struct_5 *spritePressed;
    struct struct_5 *spriteToggled;
    struct struct_5 *spriteToggledAndPressed;
} TouchButtonSpriteAnimator_Recovered;

typedef struct struct_4 {
    struct struct_2 *field_0;
    char padding_8[216];
    struct struct_3 *field_e0;
    char padding_e8[216];
    char field_1c0;
} struct_4;

typedef struct struct_3 {
    char padding_0[28];
    char field_1c;
} struct_3;

typedef struct struct_7 {
    char padding_0[16];
    char field_10;
} struct_7;

typedef struct struct_5 {
    char padding_0[16];
    char field_10;
} struct_5;

typedef struct struct_2 {
    char padding_0[200];
    unsigned long long field_c8;
    char padding_d0[96];
    char field_130;
} struct_2;

typedef struct struct_1 {
    char padding_0[304];
    char field_130;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern struct_1 *g_1ef1df8;
extern char g_1fab219;

long long TouchButtonSpriteAnimator_OnUpdateAnimator(struct_6 *ptr, unsigned int a1)
{
    struct_4 *p;  // x21
    unsigned long v1;  // x9
    unsigned long v2;  // x0
    unsigned long v3;  // x0
    unsigned int v4;  // w8
    unsigned int v5;  // w9
    struct_7 *v6;  // x1
    unsigned long long v7;  // x0

    if (!(g_1fab219 & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c(&g_1ef1df8);
        g_1fab219 = 1;
    }
    p = ptr->field_28;
    if (!p || (v1 = (unsigned long)(unsigned long long)g_1ef1df8->field_130, (unsigned int)p->field_0->field_130 >= (unsigned int)v1 && *((long long *)(p->field_0->field_c8 + v1 * 8 - 8)) == g_1ef1df8))
    {
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        v3 = Object__op_Equality(p, 0, 0);
        if (((char)v3 & 1))
            return v3;
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        v2 = Object__op_Equality(ptr->field_40, 0, 0);
        if (((char)v2 & 1))
        {
            return v2;
        }
        else if (p && p->field_e0)
        {
            v4 = p->field_e0->field_1c;
            v5 = p->field_1c0;
            if (v4 && v5)
            {
                v6 = ptr->field_100;
                if (!v6 || !v6->field_10)
                    goto LABEL_1044aa8;
                if (!v4)
                {
LABEL_1044a9c:
                    goto LABEL_1044ad4;
                }
            }
            else if (v5)
            {
LABEL_1044aa8:
                v6 = ptr->field_f8;
                if (!v4)
                    goto LABEL_1044a9c;
            }
            else if (!v4 || (v6 = (struct_7 *)ptr->field_f0, !ptr->field_f0 || !v6->field_10))
            {
LABEL_1044ad4:
            }
            TouchControlSpriteAnimatorBase__BeginSpriteAnim(ptr);
            v7 = TouchControlSpriteAnimatorBase__UpdateSpriteAnimation(ptr, a1 & 1, 0);
            return TouchControlSpriteAnimatorBase__UpdateSpriteAnimation(ptr, a1 & 1, 0);
        }
    }
    else
    {
        v2 = sub_f7df10(p);
    }
    sub_f7db74(v2);
}
```

## `TouchButtonSpriteAnimator.GetComponent` — RVA `0xc44b30`

- Decompiled symbol: `TouchButtonSpriteAnimator_GetComponent`
- Metadata signature: `private MonoBehaviour ControlFreak2.Internal.ISpriteAnimator.GetComponent() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long TouchButtonSpriteAnimator_GetComponent(void)
{
    unsigned long v0;  // x0

    return v0;
}
```

## `TouchButtonSpriteAnimator.AddUsedSprites` — RVA `0xc44b34`

- Decompiled symbol: `TouchButtonSpriteAnimator_AddUsedSprites`
- Metadata signature: `private void ControlFreak2.Internal.ISpriteAnimator.AddUsedSprites(ISpriteOptimizer optimizer) { }`
- Native interval: `512` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[120];
    struct struct_0 *field_78;
} struct_1;

typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

typedef struct struct_5 {
    char padding_0[176];
    struct struct_4 *field_b0;
    char padding_b8[118];
    unsigned short field_12e;
} struct_5;

typedef struct struct_7 {
    char padding_0[176];
    struct struct_6 *field_b0;
    char padding_b8[118];
    unsigned short field_12e;
} struct_7;

typedef struct struct_2 {
    char padding_0[312];
    struct struct_3 *field_138;
    unsigned long long field_140;
} struct_2;

typedef struct struct_4 {
    char padding_0[8];
    unsigned int field_8;
} struct_4;

typedef struct struct_6 {
    char padding_0[8];
    unsigned int field_8;
} struct_6;

typedef struct struct_3 {
    unsigned long long field_0;
} struct_3;

extern char g_1fab21a;

void TouchButtonSpriteAnimator_AddUsedSprites(struct_1 *pos, struct_5 **p)
{
    unsigned long long v5;  // x30
    unsigned long long v6;  // x22
    struct_2 *addr;  // x0
    unsigned long long v16;  // x2
    struct_5 **v17;  // x0
    unsigned long long v18;  // x1
    unsigned long long v7;  // x21
    unsigned long long v8;  // x20
    unsigned long long v9;  // x19
    struct_7 *ptr;  // x8
    unsigned long v11;  // x9
    unsigned long cur;  // x10
    unsigned long v13;  // x9
    unsigned long v14;  // x9
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
    if (!(g_1fab21a & 1))
    {
        sub_f7d92c("eA");
        g_1fab21a = 1;
    }
    if (pos->field_78 && p)
    {
        ptr = *(p);
        v11 = ptr->field_12e;
        if (v11)
        {
            cur = &ptr->field_b0->field_8;
            do
            {
                v13 = v11;
                if (*((long long *)(cur - 8)) == g_1ef0270)
                {
                    addr = &ptr->padding_0[16 + 16 * *((int *)cur) + 312];
                    goto LABEL_1044bd0;
                }
            } while ((v14 = (unsigned long)(v13 - 1), cur = (unsigned long)(cur + 16), v11 = (unsigned long)(v13 - 1), v13 != 1));
        }
        addr = sub_f80110(p);
LABEL_1044bd0:
        v16 = *((long long *)&addr->padding_0[8]);
        v17 = p;
        v18 = pos->field_78->field_18;
        (*((long long *)&addr->padding_0[0]))();
    }
    sub_f7db74();
}
```

## `TouchButtonSpriteAnimator.OnSpriteOptimization` — RVA `0xc44d34`

- Decompiled symbol: `TouchButtonSpriteAnimator_OnSpriteOptimization`
- Metadata signature: `private void ControlFreak2.Internal.ISpriteAnimator.OnSpriteOptimization(ISpriteOptimizer optimizer) { }`
- Native interval: `560` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[120];
    struct struct_0 *field_78;
} struct_1;

typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

typedef struct struct_5 {
    char padding_0[176];
    struct struct_4 *field_b0;
    char padding_b8[118];
    unsigned short field_12e;
} struct_5;

typedef struct struct_7 {
    char padding_0[176];
    struct struct_6 *field_b0;
    char padding_b8[118];
    unsigned short field_12e;
} struct_7;

typedef struct struct_2 {
    char padding_0[312];
    struct struct_3 *field_138;
    unsigned long long field_140;
} struct_2;

typedef struct struct_4 {
    char padding_0[8];
    unsigned int field_8;
} struct_4;

typedef struct struct_6 {
    char padding_0[8];
    unsigned int field_8;
} struct_6;

typedef struct struct_3 {
    unsigned long long field_0;
} struct_3;

extern char g_1fab21b;

void TouchButtonSpriteAnimator_OnSpriteOptimization(struct_1 *pos, struct_5 **p)
{
    unsigned long long v6;  // x30
    unsigned long long v7;  // x23
    unsigned long v16;  // x9
    struct_2 *addr;  // x0
    unsigned long long v18;  // x2
    struct_5 **v19;  // x0
    unsigned long long v20;  // x1
    unsigned long long v8;  // x22
    unsigned long long v9;  // x21
    unsigned long long v10;  // x20
    unsigned long long v11;  // x19
    struct_7 *ptr;  // x8
    unsigned long v13;  // x9
    unsigned long cur;  // x10
    unsigned long v15;  // x9
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
    if (!(g_1fab21b & 1))
    {
        sub_f7d92c("eA");
        g_1fab21b = 1;
    }
    if (pos->field_78 && p)
    {
        ptr = *(p);
        v13 = ptr->field_12e;
        if (v13)
        {
            cur = &ptr->field_b0->field_8;
            do
            {
                v15 = v13;
                if (*((long long *)(cur - 8)) == g_1ef0270)
                {
                    addr = &ptr->padding_0[16 * *((int *)cur) + 312];
                    goto LABEL_1044dcc;
                }
            } while ((v16 = (unsigned long)(v15 - 1), cur = (unsigned long)(cur + 16), v13 = (unsigned long)(v15 - 1), v15 != 1));
        }
        addr = sub_f80110(p);
LABEL_1044dcc:
        v18 = *((long long *)&addr->padding_0[8]);
        v19 = p;
        v20 = pos->field_78->field_18;
        (*((long long *)&addr->padding_0[0]))();
    }
    sub_f7db74();
}
```
