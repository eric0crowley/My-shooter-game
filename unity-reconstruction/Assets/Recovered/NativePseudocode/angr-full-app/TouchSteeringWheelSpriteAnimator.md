# Native pseudocode: TouchSteeringWheelSpriteAnimator

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `TouchSteeringWheelSpriteAnimator.ctor` — RVA `0xc463cc`

- Decompiled symbol: `TouchSteeringWheelSpriteAnimator_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `232` bytes
- Result: `pseudocode`
- Heuristic layout hint: `TouchSteeringWheelSpriteAnimator_Recovered` matched 2 offsets against `TouchSteeringWheelSpriteAnimator` metadata (confidence 1.00).

```c
typedef struct TouchSteeringWheelSpriteAnimator_Recovered {
    char padding_0[240];
    long long spritePressed;
    unsigned long long rotationRange;
} TouchSteeringWheelSpriteAnimator_Recovered;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern long long g_1ef1838;
extern struct_0 *g_1ef1f08;
extern char g_1fab221;

void TouchSteeringWheelSpriteAnimator_ctor(struct_1 *ptr)
{
    unsigned long long v5;  // x30
    unsigned long long v6;  // x22
    unsigned long long v7;  // x21
    unsigned long long v8;  // x20
    unsigned long long v9;  // x19
    long long v11;  // x0
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
    if (!(g_1fab221 & 1))
    {
        sub_f7d92c(&g_1ef1838);
        sub_f7d92c("KY");
        sub_f7d92c(&g_1ef1f08);
        g_1fab221 = 1;
    }
    ptr->field_f8 = 0x3dcccccd42340000;
    if (!g_1ef1f08->field_e0)
        sub_f7da5c(g_1ef1f08);
    TouchControlSpriteAnimatorBase__ctor(ptr, Type__GetTypeFromHandle(g_1eebad8, 0), 0);
    ptr->field_f8 = 0x3d4ccccd42340000;
    v11 = sub_f7db70(g_1ef1838);
    SpriteConfig__ctor(v11, 1, 0, 0);
    ptr->field_f0 = v11;
    sub_f7d8d0();
    return;
}
```

## `TouchSteeringWheelSpriteAnimator.SetSprite` — RVA `0xc464b4`

- Decompiled symbol: `TouchSteeringWheelSpriteAnimator_SetSprite`
- Metadata signature: `public void SetSprite(Sprite sprite) { }`
- Native interval: `64` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

void TouchSteeringWheelSpriteAnimator_SetSprite(struct_0 **ptr, unsigned long a1)
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
            sub_f7d8d0();
            return;
        }
    }
    sub_f7db74(p);
}
```

## `TouchSteeringWheelSpriteAnimator.SetColor` — RVA `0xc464f4`

- Decompiled symbol: `TouchSteeringWheelSpriteAnimator_SetColor`
- Metadata signature: `public void SetColor(Color color) { }`
- Native interval: `48` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[120];
    struct struct_1 *field_78;
    char padding_80[112];
    struct struct_2 *field_f0;
} struct_0;

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

void TouchSteeringWheelSpriteAnimator_SetColor(struct_0 *addr, unsigned long a1)
{
    unsigned int ptr[12];  // x8
    unsigned int v1;  // s0
    unsigned int v2;  // s1
    unsigned int v3;  // s2
    unsigned int v4;  // s3
    unsigned int p[12];  // x8

    ptr = addr->field_78;
    if (ptr)
    {
        ptr[8] = v1;
        ptr[9] = v2;
        ptr[10] = v3;
        ptr[11] = v4;
        p = addr->field_f0;
        if (p)
        {
            p[8] = v1;
            p[9] = v2;
            p[10] = v3;
            p[11] = v4;
            return;
        }
    }
    sub_f7db74();
}
```

## `TouchSteeringWheelSpriteAnimator.SetStateSprite` — RVA `0xc46524`

- Decompiled symbol: `TouchSteeringWheelSpriteAnimator_SetStateSprite`
- Metadata signature: `public void SetStateSprite(TouchSteeringWheelSpriteAnimator.ControlState state, Sprite sprite) { }`
- Native interval: `56` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[120];
    struct struct_0 *field_78;
} struct_1;

typedef struct struct_0 {
    char padding_0[24];
    unsigned int field_18;
} struct_0;

void TouchSteeringWheelSpriteAnimator_SetStateSprite(struct_1 *a0, unsigned int flag, unsigned int a2)
{
    struct_1 *v0;  // x8

    if (flag == 1)
    {
        v0 = &a0[1].padding_0[112];
    }
    else if (!flag)
    {
        v0 = &a0->field_78;
    }
    else
    {
        TouchSteeringWheelSpriteAnimator__SetSprite(a0, a2);
        return;
    }
    if (!*((long long *)&v0->padding_0[0]))
    {
        TouchSteeringWheelSpriteAnimator__SetSprite(a0, a2);
        return;
    }
    *((unsigned int *)(*((long long *)&v0->padding_0[0]) + 24)) = a2;
    sub_f7d8d0();
    return;
}
```

## `TouchSteeringWheelSpriteAnimator.GetStateSpriteConfig` — RVA `0xc4655c`

- Decompiled symbol: `TouchSteeringWheelSpriteAnimator_GetStateSpriteConfig`
- Metadata signature: `public SpriteConfig GetStateSpriteConfig(TouchSteeringWheelSpriteAnimator.ControlState state) { }`
- Native interval: `40` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[120];
    unsigned long long field_78;
} struct_0;

unsigned long long TouchSteeringWheelSpriteAnimator_GetStateSpriteConfig(struct_0 *a0, unsigned int flag)
{
    struct_0 *v0;  // x8

    if (flag == 1)
    {
        v0 = &a0[1].padding_0[112];
    }
    else if (!flag)
    {
        v0 = &a0->field_78;
    }
    else
    {
        return 0;
    }
    return *((long long *)&v0->padding_0[0]);
}
```

## `TouchSteeringWheelSpriteAnimator.SetStateColor` — RVA `0xc46584`

- Decompiled symbol: `TouchSteeringWheelSpriteAnimator_SetStateColor`
- Metadata signature: `public void SetStateColor(TouchSteeringWheelSpriteAnimator.ControlState state, Color color) { }`
- Native interval: `48` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[120];
    struct struct_1 *field_78;
} struct_0;

typedef struct struct_1 {
    char padding_0[32];
    unsigned int field_20;
    unsigned int field_24;
    unsigned int field_28;
    unsigned int field_2c;
} struct_1;

struct_0 * TouchSteeringWheelSpriteAnimator_SetStateColor(struct_0 *a0, unsigned int a1)
{
    struct_0 *p;  // x8
    unsigned int ptr[12];  // x8
    unsigned int v2;  // s0
    unsigned int v3;  // s1
    unsigned int v4;  // s2
    unsigned int v5;  // s3
    unsigned long v6;  // x0

    if (a1 == 1)
    {
        p = &a0[1].padding_0[112];
    }
    else if (!a1)
    {
        p = &a0->field_78;
    }
    else
    {
        v6 = (unsigned long long)TouchSteeringWheelSpriteAnimator__SetColor(a0, a1);
        return (unsigned long long)TouchSteeringWheelSpriteAnimator__SetColor(a0, a1);
    }
    ptr = *((long long *)&p->padding_0[0]);
    if (!ptr)
    {
        v6 = (unsigned long long)TouchSteeringWheelSpriteAnimator__SetColor(a0, a1);
        return (unsigned long long)TouchSteeringWheelSpriteAnimator__SetColor(a0, a1);
    }
    ptr[8] = v2;
    ptr[9] = v3;
    ptr[10] = v4;
    ptr[11] = v5;
    return a0;
}
```

## `TouchSteeringWheelSpriteAnimator.OnInitComponent` — RVA `0xc465b4`

- Decompiled symbol: `TouchSteeringWheelSpriteAnimator_OnInitComponent`
- Metadata signature: `protected override void OnInitComponent() { }`
- Native interval: `288` bytes
- Result: `pseudocode`

```c
typedef struct struct_4 {
    char padding_0[64];
    struct struct_1 *field_40;
    char padding_48[48];
    struct struct_2 *field_78;
    char padding_80[112];
    struct struct_3 *field_f0;
} struct_4;

typedef struct struct_1 {
    char padding_0[216];
    long long field_d8;
} struct_1;

typedef struct struct_2 {
    char padding_0[24];
    long long field_18;
} struct_2;

typedef struct struct_3 {
    char padding_0[24];
    long long field_18;
} struct_3;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab222;

long long TouchSteeringWheelSpriteAnimator_OnInitComponent(struct_4 *ptr)
{
    long long v0;  // x0
    long long v1;  // x0
    long long v2;  // x0
    struct_2 *p;  // x0
    long long v4;  // x1
    long long v5;  // x0

    if (!(g_1fab222 & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab222 = 1;
    }
    TouchControlSpriteAnimatorBase__OnInitComponent(ptr, 0);
    if (ptr->field_40)
    {
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        v0 = Object__op_Inequality(ptr->field_40->field_d8, 0, 0);
        if (!((char)v0 & 1))
        {
            return v0;
        }
        else if (ptr->field_78)
        {
            if (!g_1ef0c58->field_e0)
                sub_f7da5c(g_1ef0c58);
            v1 = Object__op_Equality(ptr->field_78->field_18, 0, 0);
            if (!((char)v1 & 1))
            {
                return v1;
            }
            else if (ptr->field_f0)
            {
                if (!g_1ef0c58->field_e0)
                    sub_f7da5c(g_1ef0c58);
                v2 = Object__op_Equality(ptr->field_f0->field_18, 0, 0);
                if (!((char)v2 & 1))
                {
                    return v2;
                }
                else if (ptr->field_40)
                {
                    p = ptr->field_78;
                    if (p)
                    {
                        v4 = ptr->field_40->field_d8;
                        p->field_18 = v4;
                        sub_f7d8d0((struct struct_2 *)&p->field_18, v4);
                        if (ptr->field_40 && ptr->field_f0)
                        {
                            ptr->field_f0->field_18 = ptr->field_40->field_d8;
                            v5 = sub_f7d8d0();
                            return sub_f7d8d0();
                        }
                    }
                }
            }
        }
    }
    sub_f7db74();
}
```

## `TouchSteeringWheelSpriteAnimator.OnUpdateAnimator` — RVA `0xc466d4`

- Decompiled symbol: `TouchSteeringWheelSpriteAnimator_OnUpdateAnimator`
- Metadata signature: `protected override void OnUpdateAnimator(bool skipAnim) { }`
- Native interval: `480` bytes
- Result: `pseudocode`

```c
typedef struct struct_6 {
    char padding_0[40];
    struct struct_4 *field_28;
    char padding_30[16];
    long long field_40;
    char padding_48[48];
    struct struct_5 *field_78;
    char padding_80[108];
    unsigned int field_ec;
    struct struct_5 *field_f0;
} struct_6;

typedef struct struct_4 {
    struct struct_2 *field_0;
    char padding_8[216];
    struct struct_3 *field_e0;
    char padding_e8[140];
    unsigned int field_174;
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

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab223;

long long TouchSteeringWheelSpriteAnimator_OnUpdateAnimator(struct_6 *ptr, unsigned int a1)
{
    long long v0;  // x0
    long long v1;  // x0
    struct_4 *v2;  // x22
    unsigned long v3;  // x9
    struct_7 *v4;  // x21
    unsigned int v5;  // w20
    unsigned long long v6;  // x0

    if (!(g_1fab223 & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c("KY");
        g_1fab223 = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v0 = Object__op_Equality(ptr->field_28, 0, 0);
    if (((char)v0 & 1))
        return v0;
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v1 = Object__op_Equality(ptr->field_40, 0, 0);
    if (((char)v1 & 1))
        return v1;
    v2 = ptr->field_28;
    if (v2)
    {
        v3 = g_1ef1e58->field_130;
        if (!(v2->field_0->field_130 >= (unsigned int)v3 && *((long long *)(v2->field_0->field_c8 + v3 * 8 - 8)) == g_1ef1e58))
        {
            sub_f7df10(v2);
        }
        else if (v2->field_e0)
        {
            if (!v2->field_e0->field_1c || (v4 = (struct_7 *)ptr->field_f0, !v4 || !v4->field_10))
                v4 = ptr->field_78;
            if (((char)CFUtils__get_editorStopped(0) & 1) || ((char)TouchControlAnimatorBase__IsIllegallyAttachedToSource(ptr, 0) & 1))
            {
                ptr->field_ec = 0;
            }
            else
            {
                CFUtils__get_realDeltaTimeClamped();
                CFUtils__SmoothTowardsAngle(0);
                ptr->field_ec = ptr->field_ec;
            }
            v5 = a1 & 1;
            TouchControlSpriteAnimatorBase__BeginSpriteAnim(ptr, v4, v5, 0, 0);
            v6 = TouchControlSpriteAnimatorBase__UpdateSpriteAnimation(ptr, v5, 0);
            return TouchControlSpriteAnimatorBase__UpdateSpriteAnimation(ptr, v5, 0);
        }
    }
    sub_f7db74();
}
```

## `TouchSteeringWheelSpriteAnimator.GetComponent` — RVA `0xc468b4`

- Decompiled symbol: `TouchSteeringWheelSpriteAnimator_GetComponent`
- Metadata signature: `private MonoBehaviour ControlFreak2.Internal.ISpriteAnimator.GetComponent() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long TouchSteeringWheelSpriteAnimator_GetComponent(void)
{
    unsigned long v0;  // x0

    return v0;
}
```

## `TouchSteeringWheelSpriteAnimator.AddUsedSprites` — RVA `0xc468b8`

- Decompiled symbol: `TouchSteeringWheelSpriteAnimator_AddUsedSprites`
- Metadata signature: `private void ControlFreak2.Internal.ISpriteAnimator.AddUsedSprites(ISpriteOptimizer optimizer) { }`
- Native interval: `296` bytes
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

extern char g_1fab224;

void TouchSteeringWheelSpriteAnimator_AddUsedSprites(struct_1 *pos, struct_5 **p)
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
    if (!(g_1fab224 & 1))
    {
        sub_f7d92c("eA");
        g_1fab224 = 1;
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
                    goto LABEL_1046954;
                }
            } while ((v14 = (unsigned long)(v13 - 1), cur = (unsigned long)(cur + 16), v11 = (unsigned long)(v13 - 1), v13 != 1));
        }
        addr = sub_f80110(p);
LABEL_1046954:
        v16 = *((long long *)&addr->padding_0[8]);
        v17 = p;
        v18 = pos->field_78->field_18;
        (*((long long *)&addr->padding_0[0]))();
    }
    sub_f7db74();
}
```

## `TouchSteeringWheelSpriteAnimator.OnSpriteOptimization` — RVA `0xc469e0`

- Decompiled symbol: `TouchSteeringWheelSpriteAnimator_OnSpriteOptimization`
- Metadata signature: `private void ControlFreak2.Internal.ISpriteAnimator.OnSpriteOptimization(ISpriteOptimizer optimizer) { }`
- Native interval: `320` bytes
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

extern char g_1fab225;

void TouchSteeringWheelSpriteAnimator_OnSpriteOptimization(struct_1 *pos, struct_5 **p)
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
    if (!(g_1fab225 & 1))
    {
        sub_f7d92c("eA");
        g_1fab225 = 1;
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
                    goto LABEL_1046a78;
                }
            } while ((v16 = (unsigned long)(v15 - 1), cur = (unsigned long)(cur + 16), v13 = (unsigned long)(v15 - 1), v15 != 1));
        }
        addr = sub_f80110(p);
LABEL_1046a78:
        v18 = *((long long *)&addr->padding_0[8]);
        v19 = p;
        v20 = pos->field_78->field_18;
        (*((long long *)&addr->padding_0[0]))();
    }
    sub_f7db74();
}
```
