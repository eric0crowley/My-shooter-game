# Native pseudocode: SuperTouchZoneSpriteAnimator

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `SuperTouchZoneSpriteAnimator.ctor` — RVA `0xc439f0`

- Decompiled symbol: `SuperTouchZoneSpriteAnimator_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `844` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern long long g_1ef1838;
extern struct_0 *g_1ef1f08;
extern char g_1fab214;

void SuperTouchZoneSpriteAnimator_ctor(long long *p)
{
    unsigned long long v6;  // d8
    unsigned long long v7;  // x30
    long long v16;  // x20
    long long v17;  // x20
    long long v18;  // x20
    long long v19;  // x20
    long long v20;  // x20
    long long v21;  // x20
    long long v22;  // x20
    long long v23;  // x20
    long long v24;  // x20
    long long v25;  // x20
    unsigned long long v8;  // x22
    long long v26;  // x20
    long long v27;  // x0
    unsigned long long v9;  // x21
    unsigned long long v10;  // x20
    unsigned long long v11;  // x19
    long long v13;  // x20
    long long v14;  // x20
    long long ptr[44];  // x19
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
    if (!(g_1fab214 & 1))
    {
        sub_f7d92c(&g_1ef1838);
        sub_f7d92c("{U");
        sub_f7d92c(&g_1ef1f08);
        g_1fab214 = 1;
    }
    if (!g_1ef1f08->field_e0)
        sub_f7da5c(g_1ef1f08);
    TouchControlSpriteAnimatorBase__ctor(p, Type__GetTypeFromHandle(g_1eeba58, 0), 0);
    v13 = sub_f7db70(g_1ef1838);
    SpriteConfig__ctor(v13, 1, 0, 0);
    p[30] = v13;
    sub_f7d8d0(p + 30, v13);
    v14 = sub_f7db70(g_1ef1838);
    SpriteConfig__ctor(v14, 0, 0, 0);
    p[31] = v14;
    ptr = p + 31;
    sub_f7d8d0(ptr, v14);
    v16 = sub_f7db70(g_1ef1838);
    SpriteConfig__ctor(v16, 0, 0, 0);
    ptr[1] = v16;
    sub_f7d8d0((long long [44])&ptr[1], v16);
    v17 = sub_f7db70(g_1ef1838);
    SpriteConfig__ctor(v17, 0, 1, 0);
    ptr[2] = v17;
    sub_f7d8d0((long long [44])&ptr[2], v17);
    v18 = sub_f7db70(g_1ef1838);
    SpriteConfig__ctor(v18, 0, 1, 0);
    ptr[3] = v18;
    sub_f7d8d0((long long [44])&ptr[3], v18);
    v19 = sub_f7db70(g_1ef1838);
    SpriteConfig__ctor(v19, 0, 1, 0);
    ptr[4] = v19;
    sub_f7d8d0((long long [44])&ptr[4], v19);
    v20 = sub_f7db70(g_1ef1838);
    SpriteConfig__ctor(v20, 0, 1, 0);
    ptr[5] = v20;
    sub_f7d8d0((long long [44])&ptr[5], v20);
    v21 = sub_f7db70(g_1ef1838);
    SpriteConfig__ctor(v21, 0, 1, 0);
    ptr[6] = v21;
    sub_f7d8d0((long long [44])&ptr[6], v21);
    v22 = sub_f7db70(g_1ef1838);
    SpriteConfig__ctor(v22, 0, 1, 0);
    ptr[7] = v22;
    sub_f7d8d0((long long [44])&ptr[7], v22);
    v23 = sub_f7db70(g_1ef1838);
    SpriteConfig__ctor(v23, 0, 1, 0);
    ptr[8] = v23;
    sub_f7d8d0((long long [44])&ptr[8], v23);
    v24 = sub_f7db70(g_1ef1838);
    SpriteConfig__ctor(v24, 0, 1, 0);
    ptr[9] = v24;
    sub_f7d8d0((long long [44])&ptr[9], v24);
    v25 = sub_f7db70(g_1ef1838);
    SpriteConfig__ctor(v25, 0, 1, 0);
    ptr[10] = v25;
    sub_f7d8d0((long long [44])&ptr[10], v25);
    v26 = sub_f7db70(g_1ef1838);
    SpriteConfig__ctor(v26, 0, 1, 0);
    ptr[11] = v26;
    sub_f7d8d0((long long [44])&ptr[11], v26);
    v27 = sub_f7db70(g_1ef1838);
    SpriteConfig__ctor(v27, 0, 1, 0);
    ptr[12] = v27;
    sub_f7d8d0();
    return;
}
```

## `SuperTouchZoneSpriteAnimator.SetSprite` — RVA `0xc43d3c`

- Decompiled symbol: `SuperTouchZoneSpriteAnimator_SetSprite`
- Metadata signature: `public void SetSprite(Sprite sprite) { }`
- Native interval: `76` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    long long field_18;
} struct_0;

long long SuperTouchZoneSpriteAnimator_SetSprite(long long a0, long long a1)
{
    unsigned int v0;  // w21
    struct_0 *ptr;  // x0
    unsigned long v2;  // x0

    v0 = 0;
    while (true)
    {
        ptr = SuperTouchZoneSpriteAnimator__GetStateSpriteConfig(a0, v0);
        if (!ptr)
            sub_f7db74();
        ptr->field_18 = a1;
        v2 = sub_f7d8d0((struct struct_0 *)&ptr->field_18, a1);
        v0 += 1;
        if (v0 == 15)
            return v2;
    }
}
```

## `SuperTouchZoneSpriteAnimator.GetStateSpriteConfig` — RVA `0xc43d88`

- Decompiled symbol: `SuperTouchZoneSpriteAnimator_GetStateSpriteConfig`
- Metadata signature: `public SpriteConfig GetStateSpriteConfig(SuperTouchZoneSpriteAnimator.ControlState state) { }`
- Native interval: `168` bytes
- Result: `pseudocode`

```c
extern char g_8520bd;

unsigned int SuperTouchZoneSpriteAnimator_GetStateSpriteConfig(unsigned long a0, unsigned int a1)
{
    if (14 < a1)
        return 0;
    goto sub_1043dac + (&g_8520bd)[a1] * 4;
}
```

## `SuperTouchZoneSpriteAnimator.SetColor` — RVA `0xc43e30`

- Decompiled symbol: `SuperTouchZoneSpriteAnimator_SetColor`
- Metadata signature: `public void SetColor(Color color) { }`
- Native interval: `100` bytes
- Result: `pseudocode`

```c
int SuperTouchZoneSpriteAnimator_SetColor(unsigned int a0, unsigned long a1, unsigned long a2)
{
    unsigned int v0;  // w20
    unsigned int ptr[12];  // x0
    unsigned int v2;  // s0
    unsigned int v3;  // s1
    unsigned int v4;  // s2
    unsigned int v5;  // s3

    v0 = 0;
    while (true)
    {
        ptr = SuperTouchZoneSpriteAnimator__GetStateSpriteConfig(a0, v0);
        if (!ptr)
            sub_f7db74();
        v0 += 1;
        ptr[8] = v2;
        ptr[9] = v3;
        ptr[10] = v4;
        ptr[11] = v5;
        if (v0 == 15)
            return *((unsigned int *)&ptr);
    }
}
```

## `SuperTouchZoneSpriteAnimator.SetStateSprite` — RVA `0xc43e94`

- Decompiled symbol: `SuperTouchZoneSpriteAnimator_SetStateSprite`
- Metadata signature: `public void SetStateSprite(SuperTouchZoneSpriteAnimator.ControlState state, Sprite sprite) { }`
- Native interval: `64` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    long long field_18;
} struct_0;

long long SuperTouchZoneSpriteAnimator_SetStateSprite(long long a0, unsigned int a1, long long a2)
{
    struct_0 *ptr;  // x0
    long long v1;  // x0
    long long v2;  // x0

    ptr = SuperTouchZoneSpriteAnimator__GetStateSpriteConfig(a0, a1);
    if (!ptr)
    {
        v2 = SuperTouchZoneSpriteAnimator__SetSprite(a0, a2);
        return SuperTouchZoneSpriteAnimator__SetSprite(a0, a2);
    }
    ptr->field_18 = a2;
    v1 = sub_f7d8d0();
    return sub_f7d8d0();
}
```

## `SuperTouchZoneSpriteAnimator.SetStateColor` — RVA `0xc43ed4`

- Decompiled symbol: `SuperTouchZoneSpriteAnimator_SetStateColor`
- Metadata signature: `public void SetStateColor(SuperTouchZoneSpriteAnimator.ControlState state, Color color) { }`
- Native interval: `100` bytes
- Result: `pseudocode`

```c
int SuperTouchZoneSpriteAnimator_SetStateColor(unsigned int a0)
{
    unsigned int v0;  // x1
    unsigned int ptr[12];  // x0
    unsigned int v2;  // s2
    unsigned int v3;  // s3
    unsigned int v4;  // s0
    unsigned int v5;  // s1
    unsigned int v6;  // x2

    ptr = SuperTouchZoneSpriteAnimator__GetStateSpriteConfig(a0, v0);
    if (!ptr)
        return SuperTouchZoneSpriteAnimator__SetColor(a0, v0, v6);
    ptr[10] = v2;
    ptr[11] = v3;
    ptr[8] = v4;
    ptr[9] = v5;
    return *((unsigned int *)&ptr);
}
```

## `SuperTouchZoneSpriteAnimator.OnInitComponent` — RVA `0xc43f38`

- Decompiled symbol: `SuperTouchZoneSpriteAnimator_OnInitComponent`
- Metadata signature: `protected override void OnInitComponent() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long SuperTouchZoneSpriteAnimator_OnInitComponent(unsigned long a0)
{
    unsigned long long v0;  // x0

    v0 = TouchControlSpriteAnimatorBase__OnInitComponent();
    return TouchControlSpriteAnimatorBase__OnInitComponent();
}
```

## `SuperTouchZoneSpriteAnimator.OnUpdateAnimator` — RVA `0xc43f40`

- Decompiled symbol: `SuperTouchZoneSpriteAnimator_OnUpdateAnimator`
- Metadata signature: `protected override void OnUpdateAnimator(bool skipAnim) { }`
- Native interval: `1012` bytes
- Result: `pseudocode`
- Heuristic layout hint: `SuperTouchZoneSpriteAnimator_Recovered` matched 14 offsets against `SuperTouchZoneSpriteAnimator` metadata (confidence 0.82).

```c
typedef struct SuperTouchZoneSpriteAnimator_Recovered {
    char padding_0[40];
    struct struct_5 *field_28;
    char padding_30[16];
    long long field_40;
    char padding_48[48];
    struct struct_3 *field_78;
    char padding_80[112];
    struct struct_3 *spriteRawPress;
    struct struct_3 *spriteNormalPress;
    struct struct_3 *spriteLongPress;
    struct struct_3 *spriteTap;
    struct struct_3 *spriteDoubleTap;
    struct struct_3 *spriteLongTap;
    struct struct_3 *spriteNormalScrollU;
    struct struct_3 *spriteNormalScrollR;
    struct struct_3 *spriteNormalScrollD;
    struct struct_3 *spriteNormalScrollL;
    struct struct_3 *spriteLongScrollU;
    struct struct_3 *spriteLongScrollR;
    struct struct_3 *spriteLongScrollD;
    struct struct_3 *spriteLongScrollL;
} SuperTouchZoneSpriteAnimator_Recovered;

typedef struct struct_2 {
    char padding_0[200];
    unsigned long long field_c8;
    char padding_d0[96];
    char field_130;
} struct_2;

typedef struct struct_6 {
    char padding_0[16];
    char field_10;
} struct_6;

typedef struct struct_5 {
    struct struct_2 *field_0;
} struct_5;

typedef struct struct_3 {
    char padding_0[16];
    char field_10;
} struct_3;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab215;

long long SuperTouchZoneSpriteAnimator_OnUpdateAnimator(struct_4 *ptr, unsigned int a1)
{
    struct_2 **v0;  // x21
    unsigned long v1;  // x9
    unsigned int v7;  // s0
    unsigned long v8;  // 4125
    unsigned long v9;  // 4102
    unsigned int v10;  // s1
    unsigned long v11;  // 4125
    unsigned long v12;  // 4125
    unsigned long v2;  // x0
    unsigned long v13;  // 4125
    unsigned long v14;  // 4102
    unsigned long v3;  // x0
    unsigned long v15;  // 4125
    unsigned long v16;  // 4125
    unsigned long v17;  // 4102
    unsigned long v18;  // 4125
    unsigned long v19;  // 4102
    struct_6 *v4;  // x22
    unsigned long v20;  // 4125
    unsigned long v21;  // 4125
    unsigned long v22;  // 4125
    unsigned int v23;  // w20
    unsigned long v5;  // 4125
    unsigned long long v24;  // x0
    unsigned long v6;  // 4125

    if (!(g_1fab215 & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c("{U");
        g_1fab215 = 1;
    }
    v0 = ptr->field_28;
    if (!v0 || (v1 = (unsigned long)(unsigned long long)g_1ef1a70->field_130, (unsigned int)*(v0)->field_130 >= (unsigned int)v1 && *((long long *)(*(v0)->field_c8 + v1 * 8 - 8)) == g_1ef1a70))
    {
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        v3 = Object__op_Equality(v0, 0, 0);
        if (((char)v3 & 1))
            return v3;
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        v2 = Object__op_Equality(ptr->field_40, 0, 0);
        if (((char)v2 & 1))
        {
            return v2;
        }
        else if (v0)
        {
            SuperTouchZone__GetScrollDelta();
            if (((char)SuperTouchZone__JustTapped(v0, 1, 2) & 1) || ((char)SuperTouchZone__JustTapped(v0, 2, 2) & 1) || ((char)SuperTouchZone__JustTapped(v0, 3, 2) & 1))
                v4 = ptr->field_110;
            else
                v4 = NULL;
            if ((((char)SuperTouchZone__JustTapped(v0, 1, 1) & 1) || ((char)SuperTouchZone__JustTapped(v0, 2, 1) & 1) || ((char)SuperTouchZone__JustTapped(v0, 3, 1) & 1)) && (!v4 || !v4->field_10))
                v4 = ptr->field_108;
            if ((((char)SuperTouchZone__JustLongTapped(v0, 1) & 1) || ((char)SuperTouchZone__JustLongTapped(v0, 2) & 1) || ((char)SuperTouchZone__JustLongTapped(v0, 3) & 1)) && (!v4 || !v4->field_10))
                v4 = ptr->field_118;
            if (!((char)SuperTouchZone__PressedLong(v0, 1) & 1) && !((char)SuperTouchZone__PressedLong(v0, 2) & 1) && !((char)SuperTouchZone__PressedLong(v0, 3) & 1))
            {
LABEL_1044148:
                if (((char)SuperTouchZone__PressedNormal(v0, 1) & 1) || ((char)SuperTouchZone__PressedNormal(v0, 2) & 1) || ((char)SuperTouchZone__PressedNormal(v0, 3) & 1))
                {
                    if (v4)
                    {
                        if (v4->field_10)
                            goto LABEL_104429c;
                        v5 = arm64g_calculate_condition(192, (((((unsigned long long)(char)(CmpF(v7, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v7, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v7, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v7, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v7, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v7, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                        if ((char)v5)
                        {
LABEL_104421c:
                            v4 = ptr->field_128;
                        }
                        v8 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v7, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v7, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v7, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v7, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v7, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v7, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                        if (!((char)v8) && (!v4 || !v4->field_10))
                        {
LABEL_1044244:
                            v4 = ptr->field_138;
                        }
                        v11 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v10, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v10, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v10, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v10, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v10, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v10, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                        if ((char)v11 || v4 && v4->field_10)
                            goto LABEL_104426c;
                        goto LABEL_1044268;
                    }
                    else
                    {
                        v6 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v7, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v7, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v7, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v7, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v7, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v7, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                        if (!((char)v6))
                            goto LABEL_104421c;
                        v9 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v7, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v7, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v7, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v7, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v7, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v7, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                        if (!((char)v9))
                            goto LABEL_1044244;
                        v12 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v10, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v10, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v10, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v10, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v10, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v10, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                        if (!((char)v12))
                        {
LABEL_1044268:
                            v4 = ptr->field_120;
LABEL_104426c:
                            v13 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v10, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v10, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v10, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v10, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v10, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v10, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                            if ((char)v13)
                                goto LABEL_104428c;
                            if (!v4 || !v4->field_10)
                                goto LABEL_1044288;
                            goto LABEL_104429c;
                        }
                        else
                        {
                            v14 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v10, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v10, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v10, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v10, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v10, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v10, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                            if ((char)v14)
                                goto LABEL_1044298;
LABEL_1044288:
                            v4 = ptr->field_130;
LABEL_104428c:
                            if (!v4 || !v4->field_10)
                            {
LABEL_1044298:
                                v4 = ptr->field_f8;
                                goto LABEL_104429c;
                            }
                        }
                    }
                }
            }
            if (v4)
            {
                if (v4->field_10)
                    goto LABEL_1044148;
                v15 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v7, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v7, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v7, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v7, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v7, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v7, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                if ((char)v15)
                    goto LABEL_10441b8;
LABEL_10441b4:
                v4 = ptr->field_148;
LABEL_10441b8:
                v20 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v7, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v7, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v7, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v7, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v7, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v7, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                if ((char)v20 || v4 && v4->field_10)
                    goto LABEL_10441d0;
LABEL_10441cc:
                v4 = ptr->field_158;
LABEL_10441d0:
                v21 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v10, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v10, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v10, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v10, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v10, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v10, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                if ((char)v21 || v4 && v4->field_10)
                    goto LABEL_10441e8;
            }
            else
            {
                v16 = arm64g_calculate_condition(192, (((((unsigned long long)(char)(CmpF(v7, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v7, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v7, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v7, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v7, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v7, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                if ((char)v16)
                    goto LABEL_10441b4;
                v17 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(v7, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v7, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v7, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v7, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v7, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v7, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                if ((char)v17)
                    goto LABEL_10441cc;
                v18 = arm64g_calculate_condition(192, (((((unsigned long long)(char)(CmpF(v10, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v10, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v10, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v10, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v10, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v10, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                if (!((char)v18))
                {
                    v19 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(v10, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v10, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v10, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v10, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v10, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v10, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                    if (!((char)v19))
                        goto LABEL_104420c;
                    goto LABEL_10441fc;
                }
            }
            v4 = ptr->field_140;
LABEL_10441e8:
            v22 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v10, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v10, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v10, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v10, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v10, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v10, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
            if ((char)v22)
                goto LABEL_1044200;
            if (!v4 || !v4->field_10)
            {
LABEL_10441fc:
                v4 = ptr->field_150;
LABEL_1044200:
                if (!v4 || !v4->field_10)
                {
LABEL_104420c:
                    v4 = ptr->field_100;
                }
            }
LABEL_104429c:
            if (((char)SuperTouchZone__PressedRaw(v0, 1) & 1) || ((char)SuperTouchZone__PressedRaw(v0, 2) & 1) || ((char)SuperTouchZone__PressedRaw(v0, 3) & 1))
            {
                if (v4 && v4->field_10)
                    goto LABEL_10442ec;
                v4 = ptr->field_f0;
            }
            if (!v4 || !v4->field_10)
                v4 = ptr->field_78;
LABEL_10442ec:
            v23 = a1 & 1;
            TouchControlSpriteAnimatorBase__BeginSpriteAnim(ptr, v4, v23, 0, 0);
            v24 = TouchControlSpriteAnimatorBase__UpdateSpriteAnimation(ptr, v23, 0);
            return TouchControlSpriteAnimatorBase__UpdateSpriteAnimation(ptr, v23, 0);
        }
    }
    else
    {
        v2 = sub_f7df10(v0);
    }
    sub_f7db74(v2);
}
```

## `SuperTouchZoneSpriteAnimator.GetComponent` — RVA `0xc44478`

- Decompiled symbol: `SuperTouchZoneSpriteAnimator_GetComponent`
- Metadata signature: `private MonoBehaviour ControlFreak2.Internal.ISpriteAnimator.GetComponent() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long SuperTouchZoneSpriteAnimator_GetComponent(void)
{
    unsigned long v0;  // x0

    return v0;
}
```

## `SuperTouchZoneSpriteAnimator.AddUsedSprites` — RVA `0xc4447c`

- Decompiled symbol: `SuperTouchZoneSpriteAnimator_AddUsedSprites`
- Metadata signature: `private void ControlFreak2.Internal.ISpriteAnimator.AddUsedSprites(ISpriteOptimizer optimizer) { }`
- Native interval: `216` bytes
- Result: `pseudocode`
- Heuristic layout hint: `SuperTouchZoneSpriteAnimator_Recovered` matched 2 offsets against `SuperTouchZoneSpriteAnimator` metadata (confidence 1.00).

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

typedef struct struct_4 {
    char padding_0[176];
    struct struct_3 *field_b0;
    char padding_b8[118];
    unsigned short field_12e;
} struct_4;

typedef struct struct_6 {
    char padding_0[176];
    struct struct_5 *field_b0;
    char padding_b8[118];
    unsigned short field_12e;
} struct_6;

typedef struct SuperTouchZoneSpriteAnimator_Recovered {
    char padding_0[312];
    struct struct_2 *spriteNormalScrollL;
    unsigned long long spriteLongScrollU;
} SuperTouchZoneSpriteAnimator_Recovered;

typedef struct struct_3 {
    char padding_0[8];
    unsigned int field_8;
} struct_3;

typedef struct struct_5 {
    char padding_0[8];
    unsigned int field_8;
} struct_5;

typedef struct struct_2 {
    unsigned long long field_0;
} struct_2;

extern char g_1fab216;

void SuperTouchZoneSpriteAnimator_AddUsedSprites(unsigned int a0, struct_4 **p)
{
    unsigned long long v6;  // x30
    unsigned long long v7;  // x23
    unsigned long v16;  // x9
    unsigned long v17;  // x9
    struct_1 *addr;  // x0
    unsigned long long v19;  // x2
    struct_4 **v20;  // x0
    unsigned long long v21;  // x1
    unsigned long long v8;  // x22
    unsigned long long v9;  // x21
    unsigned long long v10;  // x20
    unsigned long long v11;  // x19
    struct_0 *ptr4;  // x0
    struct_6 *ptr;  // x8
    unsigned long v14;  // x9
    unsigned long cur;  // x10
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
    if (!(g_1fab216 & 1))
    {
        sub_f7d92c("eA");
        g_1fab216 = 1;
    }
    ptr4 = SuperTouchZoneSpriteAnimator__GetStateSpriteConfig(a0, 0);
    if (ptr4 && p)
    {
        ptr = *(p);
        v14 = ptr->field_12e;
        if (v14)
        {
            cur = &ptr->field_b0->field_8;
            do
            {
                v16 = v14;
                if (*((long long *)(cur - 8)) == g_1ef0270)
                {
                    addr = &ptr->padding_0[16 + 16 * *((int *)cur) + 312];
                    goto LABEL_1044524;
                }
            } while ((v17 = (unsigned long)(v16 - 1), cur = (unsigned long)(cur + 16), v14 = (unsigned long)(v16 - 1), v16 != 1));
        }
        addr = sub_f80110(p);
LABEL_1044524:
        v19 = *((long long *)&addr->padding_0[8]);
        v20 = p;
        v21 = ptr4->field_18;
        (*((long long *)&addr->padding_0[0]))();
    }
    sub_f7db74();
}
```

## `SuperTouchZoneSpriteAnimator.OnSpriteOptimization` — RVA `0xc44554`

- Decompiled symbol: `SuperTouchZoneSpriteAnimator_OnSpriteOptimization`
- Metadata signature: `private void ControlFreak2.Internal.ISpriteAnimator.OnSpriteOptimization(ISpriteOptimizer optimizer) { }`
- Native interval: `240` bytes
- Result: `pseudocode`
- Heuristic layout hint: `SuperTouchZoneSpriteAnimator_Recovered` matched 2 offsets against `SuperTouchZoneSpriteAnimator` metadata (confidence 1.00).

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

typedef struct struct_4 {
    char padding_0[176];
    struct struct_3 *field_b0;
    char padding_b8[118];
    unsigned short field_12e;
} struct_4;

typedef struct struct_6 {
    char padding_0[176];
    struct struct_5 *field_b0;
    char padding_b8[118];
    unsigned short field_12e;
} struct_6;

typedef struct SuperTouchZoneSpriteAnimator_Recovered {
    char padding_0[312];
    struct struct_2 *spriteNormalScrollL;
    unsigned long long spriteLongScrollU;
} SuperTouchZoneSpriteAnimator_Recovered;

typedef struct struct_3 {
    char padding_0[8];
    unsigned int field_8;
} struct_3;

typedef struct struct_5 {
    char padding_0[8];
    unsigned int field_8;
} struct_5;

typedef struct struct_2 {
    unsigned long long field_0;
} struct_2;

extern char g_1fab217;

void SuperTouchZoneSpriteAnimator_OnSpriteOptimization(unsigned int a0, struct_4 **p)
{
    unsigned long long v7;  // x30
    unsigned long long v8;  // x24
    unsigned long cur;  // x10
    unsigned long v18;  // x9
    unsigned long v19;  // x9
    struct_1 *addr;  // x0
    unsigned long long v21;  // x2
    struct_4 **v22;  // x0
    unsigned long long v23;  // x1
    unsigned long long v9;  // x23
    unsigned long long v10;  // x22
    unsigned long long v11;  // x21
    unsigned long long v12;  // x20
    unsigned long long v13;  // x19
    struct_0 *ptr4;  // x0
    struct_6 *ptr;  // x8
    unsigned long v16;  // x9
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
    if (!(g_1fab217 & 1))
    {
        sub_f7d92c("eA");
        g_1fab217 = 1;
    }
    ptr4 = SuperTouchZoneSpriteAnimator__GetStateSpriteConfig(a0, 0);
    if (ptr4 && p)
    {
        ptr = *(p);
        v16 = ptr->field_12e;
        if (v16)
        {
            cur = &ptr->field_b0->field_8;
            do
            {
                v18 = v16;
                if (*((long long *)(cur - 8)) == g_1ef0270)
                {
                    addr = &ptr->padding_0[16 * *((int *)cur) + 312];
                    goto LABEL_1044600;
                }
            } while ((v19 = (unsigned long)(v18 - 1), cur = (unsigned long)(cur + 16), v16 = (unsigned long)(v18 - 1), v18 != 1));
        }
        addr = sub_f80110(p);
LABEL_1044600:
        v21 = *((long long *)&addr->padding_0[8]);
        v22 = p;
        v23 = ptr4->field_18;
        (*((long long *)&addr->padding_0[0]))();
    }
    sub_f7db74();
}
```
