# Native pseudocode: TouchJoystickSpriteAnimator

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `TouchJoystickSpriteAnimator.ctor` — RVA `0xc44f64`

- Decompiled symbol: `TouchJoystickSpriteAnimator_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `656` bytes
- Result: `pseudocode`
- Heuristic layout hint: `TouchJoystickSpriteAnimator_Recovered` matched 16 offsets against `TouchJoystickSpriteAnimator` metadata (confidence 1.00).

```c
typedef struct TouchJoystickSpriteAnimator_Recovered {
    char padding_0[248];
    long long spriteNeutralPressed;
    long long spriteUp;
    long long spriteUpRight;
    long long spriteRight;
    long long spriteDownRight;
    long long spriteDown;
    long long spriteDownLeft;
    long long spriteLeft;
    long long spriteUpLeft;
    char animateTransl;
    char padding_141[3];
    unsigned long long moveScale;
    unsigned int translationSmoothingTime;
    unsigned int rotationMode;
    unsigned long long simpleRotationRange;
    unsigned int rotationSmoothingTime;
    unsigned int lastSafeCompassAngle;
} TouchJoystickSpriteAnimator_Recovered;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern long long g_1eebad0;
extern long long g_1ef1838;
extern struct_0 *g_1ef1f08;
extern char g_1fab21c;

void TouchJoystickSpriteAnimator_ctor(struct_1 *p)
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
    long long v23;  // x0
    unsigned long long v8;  // x22
    unsigned long long v9;  // x21
    unsigned long long v10;  // x20
    unsigned long long v11;  // x19
    struct_1 *addr;  // x22
    long long v14;  // x20
    struct_1 *ptr;  // x19
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
    if (!(g_1fab21c & 1))
    {
        sub_f7d92c(&g_1ef1838);
        sub_f7d92c(&g_1eebad0);
        sub_f7d92c(&g_1ef1f08);
        g_1fab21c = 1;
    }
    *((unsigned int *)((char *)&p->field_144 + 4)) = 1036831949;
    *((unsigned int *)&p->field_154) = 1036831949;
    addr = &(&p->padding_141)[1];
    if (!g_1ef1f08->field_e0)
        sub_f7da5c(g_1ef1f08);
    TouchControlSpriteAnimatorBase__ctor(p, Type__GetTypeFromHandle(g_1eebad0, 0), 0);
    p->field_140 = 0;
    *((unsigned long long *)&addr->padding_0[0]) = 0x3f0000003f000000;
    p->field_14c = 0;
    *((unsigned long long *)&addr->padding_0[16]) = 0x3c23d70a42340000;
    *((unsigned int *)((char *)&p->field_154 + 4)) = 0;
    v14 = sub_f7db70(g_1ef1838);
    SpriteConfig__ctor(v14, 1, 0, 0);
    p->field_f8 = v14;
    ptr = &p->field_f8;
    sub_f7d8d0(ptr, v14);
    v16 = sub_f7db70(g_1ef1838);
    SpriteConfig__ctor(v16, 0, 0, 0);
    *((long long *)&ptr->padding_0[8]) = v16;
    sub_f7d8d0((struct TouchJoystickSpriteAnimator_Recovered *)&ptr->padding_0[8], v16);
    v17 = sub_f7db70(g_1ef1838);
    SpriteConfig__ctor(v17, 0, 0, 0);
    *((long long *)&ptr->padding_0[16]) = v17;
    sub_f7d8d0((struct TouchJoystickSpriteAnimator_Recovered *)&ptr->padding_0[16], v17);
    v18 = sub_f7db70(g_1ef1838);
    SpriteConfig__ctor(v18, 0, 0, 0);
    *((long long *)&ptr->padding_0[24]) = v18;
    sub_f7d8d0((struct TouchJoystickSpriteAnimator_Recovered *)&ptr->padding_0[24], v18);
    v19 = sub_f7db70(g_1ef1838);
    SpriteConfig__ctor(v19, 0, 0, 0);
    *((long long *)&ptr->padding_0[32]) = v19;
    sub_f7d8d0((struct TouchJoystickSpriteAnimator_Recovered *)&ptr->padding_0[32], v19);
    v20 = sub_f7db70(g_1ef1838);
    SpriteConfig__ctor(v20, 0, 0, 0);
    *((long long *)&ptr->padding_0[40]) = v20;
    sub_f7d8d0((struct TouchJoystickSpriteAnimator_Recovered *)&ptr->padding_0[40], v20);
    v21 = sub_f7db70(g_1ef1838);
    SpriteConfig__ctor(v21, 0, 0, 0);
    *((long long *)&ptr->padding_0[48]) = v21;
    sub_f7d8d0((struct TouchJoystickSpriteAnimator_Recovered *)&ptr->padding_0[48], v21);
    v22 = sub_f7db70(g_1ef1838);
    SpriteConfig__ctor(v22, 0, 0, 0);
    *((long long *)&ptr->padding_0[56]) = v22;
    sub_f7d8d0((struct TouchJoystickSpriteAnimator_Recovered *)&ptr->padding_0[56], v22);
    v23 = sub_f7db70(g_1ef1838);
    SpriteConfig__ctor(v23, 0, 0, 0);
    *((long long *)&ptr->padding_0[64]) = v23;
    sub_f7d8d0();
    return;
}
```

## `TouchJoystickSpriteAnimator.SetSprite` — RVA `0xc451f4`

- Decompiled symbol: `TouchJoystickSpriteAnimator_SetSprite`
- Metadata signature: `public void SetSprite(Sprite sprite) { }`
- Native interval: `224` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    long long field_18;
} struct_0;

void TouchJoystickSpriteAnimator_SetSprite(struct_0 **ptr, long long a1)
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
        p = ptr[31];
        if (p)
        {
            p->field_18 = a1;
            sub_f7d8d0((struct struct_0 *)&p->field_18, a1);
            p = ptr[32];
            if (p)
            {
                p->field_18 = a1;
                sub_f7d8d0((struct struct_0 *)&p->field_18, a1);
                p = ptr[33];
                if (p)
                {
                    p->field_18 = a1;
                    sub_f7d8d0((struct struct_0 *)&p->field_18, a1);
                    p = ptr[34];
                    if (p)
                    {
                        p->field_18 = a1;
                        sub_f7d8d0((struct struct_0 *)&p->field_18, a1);
                        p = ptr[35];
                        if (p)
                        {
                            p->field_18 = a1;
                            sub_f7d8d0((struct struct_0 *)&p->field_18, a1);
                            p = ptr[36];
                            if (p)
                            {
                                p->field_18 = a1;
                                sub_f7d8d0((struct struct_0 *)&p->field_18, a1);
                                p = ptr[37];
                                if (p)
                                {
                                    p->field_18 = a1;
                                    sub_f7d8d0((struct struct_0 *)&p->field_18, a1);
                                    p = ptr[38];
                                    if (p)
                                    {
                                        p->field_18 = a1;
                                        sub_f7d8d0((struct struct_0 *)&p->field_18, a1);
                                        p = ptr[39];
                                        if (p)
                                        {
                                            p->field_18 = a1;
                                            sub_f7d8d0();
                                            return;
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    sub_f7db74(p);
}
```

## `TouchJoystickSpriteAnimator.SetColor` — RVA `0xc452d4`

- Decompiled symbol: `TouchJoystickSpriteAnimator_SetColor`
- Metadata signature: `public void SetColor(Color color) { }`
- Native interval: `176` bytes
- Result: `pseudocode`
- Heuristic layout hint: `TouchJoystickSpriteAnimator_Recovered` matched 9 offsets against `TouchJoystickSpriteAnimator` metadata (confidence 0.90).

```c
typedef struct TouchJoystickSpriteAnimator_Recovered {
    char padding_0[120];
    struct struct_1 *field_78;
    char padding_80[120];
    struct struct_2 *spriteNeutralPressed;
    struct struct_3 *spriteUp;
    struct struct_4 *spriteUpRight;
    struct struct_5 *spriteRight;
    struct struct_6 *spriteDownRight;
    struct struct_7 *spriteDown;
    struct struct_8 *spriteDownLeft;
    struct struct_9 *spriteLeft;
    struct struct_10 *spriteUpLeft;
} TouchJoystickSpriteAnimator_Recovered;

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

typedef struct struct_5 {
    char padding_0[32];
    unsigned int field_20;
    unsigned int field_24;
    unsigned int field_28;
    unsigned int field_2c;
} struct_5;

typedef struct struct_6 {
    char padding_0[32];
    unsigned int field_20;
    unsigned int field_24;
    unsigned int field_28;
    unsigned int field_2c;
} struct_6;

typedef struct struct_7 {
    char padding_0[32];
    unsigned int field_20;
    unsigned int field_24;
    unsigned int field_28;
    unsigned int field_2c;
} struct_7;

typedef struct struct_8 {
    char padding_0[32];
    unsigned int field_20;
    unsigned int field_24;
    unsigned int field_28;
    unsigned int field_2c;
} struct_8;

typedef struct struct_9 {
    char padding_0[32];
    unsigned int field_20;
    unsigned int field_24;
    unsigned int field_28;
    unsigned int field_2c;
} struct_9;

typedef struct struct_10 {
    char padding_0[32];
    unsigned int field_20;
    unsigned int field_24;
    unsigned int field_28;
    unsigned int field_2c;
} struct_10;

void TouchJoystickSpriteAnimator_SetColor(struct_0 *ptr, unsigned long a1, unsigned long a2)
{
    unsigned int p[12];  // x8
    unsigned int v1;  // s0
    unsigned int addr[12];  // x8
    unsigned int ptr3[12];  // x8
    unsigned int ptr4[12];  // x8
    unsigned int ptr5[12];  // x8
    unsigned int v2;  // s1
    unsigned int v3;  // s2
    unsigned int v4;  // s3
    unsigned int ptr6[12];  // x8
    unsigned int ptr7[12];  // x8
    unsigned int ptr8[12];  // x8
    unsigned int ptr9[12];  // x8
    unsigned int ptr10[12];  // x8

    p = ptr->field_78;
    if (p)
    {
        p[8] = v1;
        p[9] = v2;
        p[10] = v3;
        p[11] = v4;
        ptr6 = ptr->field_f8;
        if (ptr6)
        {
            ptr6[8] = v1;
            ptr6[9] = v2;
            ptr6[10] = v3;
            ptr6[11] = v4;
            ptr7 = ptr->field_100;
            if (ptr7)
            {
                ptr7[8] = v1;
                ptr7[9] = v2;
                ptr7[10] = v3;
                ptr7[11] = v4;
                ptr8 = ptr->field_108;
                if (ptr8)
                {
                    ptr8[8] = v1;
                    ptr8[9] = v2;
                    ptr8[10] = v3;
                    ptr8[11] = v4;
                    ptr9 = ptr->field_110;
                    if (ptr9)
                    {
                        ptr9[8] = v1;
                        ptr9[9] = v2;
                        ptr9[10] = v3;
                        ptr9[11] = v4;
                        ptr10 = ptr->field_118;
                        if (ptr10)
                        {
                            ptr10[8] = v1;
                            ptr10[9] = v2;
                            ptr10[10] = v3;
                            ptr10[11] = v4;
                            addr = ptr->field_120;
                            if (addr)
                            {
                                addr[8] = v1;
                                addr[9] = v2;
                                addr[10] = v3;
                                addr[11] = v4;
                                ptr3 = ptr->field_128;
                                if (ptr3)
                                {
                                    ptr3[8] = v1;
                                    ptr3[9] = v2;
                                    ptr3[10] = v3;
                                    ptr3[11] = v4;
                                    ptr4 = ptr->field_130;
                                    if (ptr4)
                                    {
                                        ptr4[8] = v1;
                                        ptr4[9] = v2;
                                        ptr4[10] = v3;
                                        ptr4[11] = v4;
                                        ptr5 = ptr->field_138;
                                        if (ptr5)
                                        {
                                            ptr5[8] = v1;
                                            ptr5[9] = v2;
                                            ptr5[10] = v3;
                                            ptr5[11] = v4;
                                            return;
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    sub_f7db74();
}
```

## `TouchJoystickSpriteAnimator.SetStateSprite` — RVA `0xc45384`

- Decompiled symbol: `TouchJoystickSpriteAnimator_SetStateSprite`
- Metadata signature: `public void SetStateSprite(TouchJoystickSpriteAnimator.ControlState state, Sprite sprite) { }`
- Native interval: `64` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    long long field_18;
} struct_0;

void TouchJoystickSpriteAnimator_SetStateSprite(struct_0 **a0, unsigned long a1, long long a2)
{
    struct_0 *ptr;  // x0

    ptr = TouchJoystickSpriteAnimator__GetStateSpriteConfig();
    if (!ptr)
    {
        TouchJoystickSpriteAnimator__SetSprite(a0, a2);
        return;
    }
    ptr->field_18 = a2;
    sub_f7d8d0();
    return;
}
```

## `TouchJoystickSpriteAnimator.GetStateSpriteConfig` — RVA `0xc453c4`

- Decompiled symbol: `TouchJoystickSpriteAnimator_GetStateSpriteConfig`
- Metadata signature: `public SpriteConfig GetStateSpriteConfig(TouchJoystickSpriteAnimator.ControlState state) { }`
- Native interval: `128` bytes
- Result: `pseudocode`

```c
extern char g_8520d4;

unsigned int TouchJoystickSpriteAnimator_GetStateSpriteConfig(unsigned long a0, unsigned int a1)
{
    if (9 < a1)
        return 0;
    goto sub_10453e8 + (&g_8520d4)[a1] * 4;
}
```

## `TouchJoystickSpriteAnimator.SetStateColor` — RVA `0xc45444`

- Decompiled symbol: `TouchJoystickSpriteAnimator_SetStateColor`
- Metadata signature: `public void SetStateColor(TouchJoystickSpriteAnimator.ControlState state, Color color) { }`
- Native interval: `100` bytes
- Result: `pseudocode`
- Heuristic layout hint: `TouchJoystickSpriteAnimator_Recovered` matched 9 offsets against `TouchJoystickSpriteAnimator` metadata (confidence 0.90).

```c
typedef struct TouchJoystickSpriteAnimator_Recovered {
    char padding_0[120];
    struct struct_1 *field_78;
    char padding_80[120];
    struct struct_2 *spriteNeutralPressed;
    struct struct_3 *spriteUp;
    struct struct_4 *spriteUpRight;
    struct struct_5 *spriteRight;
    struct struct_6 *spriteDownRight;
    struct struct_7 *spriteDown;
    struct struct_8 *spriteDownLeft;
    struct struct_9 *spriteLeft;
    struct struct_10 *spriteUpLeft;
} TouchJoystickSpriteAnimator_Recovered;

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

typedef struct struct_5 {
    char padding_0[32];
    unsigned int field_20;
    unsigned int field_24;
    unsigned int field_28;
    unsigned int field_2c;
} struct_5;

typedef struct struct_6 {
    char padding_0[32];
    unsigned int field_20;
    unsigned int field_24;
    unsigned int field_28;
    unsigned int field_2c;
} struct_6;

typedef struct struct_7 {
    char padding_0[32];
    unsigned int field_20;
    unsigned int field_24;
    unsigned int field_28;
    unsigned int field_2c;
} struct_7;

typedef struct struct_8 {
    char padding_0[32];
    unsigned int field_20;
    unsigned int field_24;
    unsigned int field_28;
    unsigned int field_2c;
} struct_8;

typedef struct struct_9 {
    char padding_0[32];
    unsigned int field_20;
    unsigned int field_24;
    unsigned int field_28;
    unsigned int field_2c;
} struct_9;

typedef struct struct_10 {
    char padding_0[32];
    unsigned int field_20;
    unsigned int field_24;
    unsigned int field_28;
    unsigned int field_2c;
} struct_10;

int TouchJoystickSpriteAnimator_SetStateColor(struct_0 *a0)
{
    unsigned int v0;  // x1
    unsigned int ptr[12];  // x0
    unsigned int v2;  // s2
    unsigned int v3;  // s3
    unsigned int v4;  // s0
    unsigned int v5;  // s1
    unsigned int v6;  // x2

    ptr = TouchJoystickSpriteAnimator__GetStateSpriteConfig(a0, v0);
    if (!ptr)
        return (unsigned long long)TouchJoystickSpriteAnimator__SetColor(a0, v0, v6);
    ptr[10] = v2;
    ptr[11] = v3;
    ptr[8] = v4;
    ptr[9] = v5;
    return *((unsigned int *)&ptr);
}
```

## `TouchJoystickSpriteAnimator.OnInitComponent` — RVA `0xc454a8`

- Decompiled symbol: `TouchJoystickSpriteAnimator_OnInitComponent`
- Metadata signature: `protected override void OnInitComponent() { }`
- Native interval: `504` bytes
- Result: `pseudocode`
- Heuristic layout hint: `TouchJoystickSpriteAnimator_Recovered` matched 9 offsets against `TouchJoystickSpriteAnimator` metadata (confidence 0.82).

```c
typedef struct TouchJoystickSpriteAnimator_Recovered {
    char padding_0[64];
    struct struct_1 *field_40;
    char padding_48[48];
    struct struct_2 *field_78;
    char padding_80[120];
    struct struct_3 *spriteNeutralPressed;
    struct struct_4 *spriteUp;
    struct struct_5 *spriteUpRight;
    struct struct_6 *spriteRight;
    struct struct_7 *spriteDownRight;
    struct struct_8 *spriteDown;
    struct struct_9 *spriteDownLeft;
    struct struct_10 *spriteLeft;
    struct struct_11 *spriteUpLeft;
} TouchJoystickSpriteAnimator_Recovered;

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

typedef struct struct_4 {
    char padding_0[24];
    long long field_18;
} struct_4;

typedef struct struct_5 {
    char padding_0[24];
    long long field_18;
} struct_5;

typedef struct struct_6 {
    char padding_0[24];
    long long field_18;
} struct_6;

typedef struct struct_7 {
    char padding_0[24];
    long long field_18;
} struct_7;

typedef struct struct_8 {
    char padding_0[24];
    long long field_18;
} struct_8;

typedef struct struct_9 {
    char padding_0[24];
    long long field_18;
} struct_9;

typedef struct struct_10 {
    char padding_0[24];
    long long field_18;
} struct_10;

typedef struct struct_11 {
    char padding_0[24];
    long long field_18;
} struct_11;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab21d;

long long TouchJoystickSpriteAnimator_OnInitComponent(struct_12 *ptr)
{
    long long v0;  // x0
    long long v1;  // x0
    long long v10;  // x1
    struct_6 *p;  // x0
    long long v12;  // x1
    struct_7 *addr;  // x0
    long long v14;  // x1
    struct_8 *ptr3;  // x0
    long long v16;  // x1
    struct_9 *ptr4;  // x0
    long long v18;  // x1
    struct_10 *ptr5;  // x0
    long long v2;  // x0
    long long v20;  // x1
    long long v21;  // x0
    struct_2 *ptr6;  // x0
    long long v4;  // x1
    struct_3 *ptr7;  // x0
    long long v6;  // x1
    struct_4 *ptr8;  // x0
    long long v8;  // x1
    struct_5 *ptr9;  // x0

    if (!(g_1fab21d & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab21d = 1;
    }
    TouchControlSpriteAnimatorBase__OnInitComponent(ptr, 0);
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v0 = Object__op_Inequality(ptr->field_40, 0, 0);
    if (!((char)v0 & 1))
        return v0;
    if (ptr->field_40)
    {
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        v1 = Object__op_Inequality(ptr->field_40->field_d8, 0, 0);
        if (!((char)v1 & 1))
        {
            return v1;
        }
        else if (ptr->field_78)
        {
            if (!g_1ef0c58->field_e0)
                sub_f7da5c(g_1ef0c58);
            v2 = Object__op_Equality(ptr->field_78->field_18, 0, 0);
            if (!((char)v2 & 1))
            {
                return v2;
            }
            else if (ptr->field_40)
            {
                ptr6 = ptr->field_78;
                if (ptr6)
                {
                    v4 = ptr->field_40->field_d8;
                    ptr6->field_18 = v4;
                    sub_f7d8d0((struct struct_2 *)&ptr6->field_18, v4);
                    if (ptr->field_40)
                    {
                        ptr7 = ptr->field_f8;
                        if (ptr7)
                        {
                            v6 = ptr->field_40->field_d8;
                            ptr7->field_18 = v6;
                            sub_f7d8d0((struct struct_3 *)&ptr7->field_18, v6);
                            if (ptr->field_40)
                            {
                                ptr8 = ptr->field_100;
                                if (ptr8)
                                {
                                    v8 = ptr->field_40->field_d8;
                                    ptr8->field_18 = v8;
                                    sub_f7d8d0((struct struct_4 *)&ptr8->field_18, v8);
                                    if (ptr->field_40)
                                    {
                                        ptr9 = ptr->field_108;
                                        if (ptr9)
                                        {
                                            v10 = ptr->field_40->field_d8;
                                            ptr9->field_18 = v10;
                                            sub_f7d8d0((struct struct_5 *)&ptr9->field_18, v10);
                                            if (ptr->field_40)
                                            {
                                                p = ptr->field_110;
                                                if (p)
                                                {
                                                    v12 = ptr->field_40->field_d8;
                                                    p->field_18 = v12;
                                                    sub_f7d8d0((struct struct_6 *)&p->field_18, v12);
                                                    if (ptr->field_40)
                                                    {
                                                        addr = ptr->field_118;
                                                        if (addr)
                                                        {
                                                            v14 = ptr->field_40->field_d8;
                                                            addr->field_18 = v14;
                                                            sub_f7d8d0((struct struct_7 *)&addr->field_18, v14);
                                                            if (ptr->field_40)
                                                            {
                                                                ptr3 = ptr->field_120;
                                                                if (ptr3)
                                                                {
                                                                    v16 = ptr->field_40->field_d8;
                                                                    ptr3->field_18 = v16;
                                                                    sub_f7d8d0((struct struct_8 *)&ptr3->field_18, v16);
                                                                    if (ptr->field_40)
                                                                    {
                                                                        ptr4 = ptr->field_128;
                                                                        if (ptr4)
                                                                        {
                                                                            v18 = ptr->field_40->field_d8;
                                                                            ptr4->field_18 = v18;
                                                                            sub_f7d8d0((struct struct_9 *)&ptr4->field_18, v18);
                                                                            if (ptr->field_40)
                                                                            {
                                                                                ptr5 = ptr->field_130;
                                                                                if (ptr5)
                                                                                {
                                                                                    v20 = ptr->field_40->field_d8;
                                                                                    ptr5->field_18 = v20;
                                                                                    sub_f7d8d0((struct struct_10 *)&ptr5->field_18, v20);
                                                                                    if (ptr->field_40 && ptr->field_138)
                                                                                    {
                                                                                        ptr->field_138->field_18 = ptr->field_40->field_d8;
                                                                                        v21 = sub_f7d8d0();
                                                                                        return sub_f7d8d0();
                                                                                    }
                                                                                }
                                                                            }
                                                                        }
                                                                    }
                                                                }
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    sub_f7db74();
}
```

## `TouchJoystickSpriteAnimator.OnUpdateAnimator` — RVA `0xc456a0`

- Decompiled symbol: `TouchJoystickSpriteAnimator_OnUpdateAnimator`
- Metadata signature: `protected override void OnUpdateAnimator(bool skipAnim) { }`
- Native interval: `928` bytes
- Result: `pseudocode`

```c
typedef struct struct_4 {
    struct struct_2 *field_0;
    char padding_8[48];
    unsigned int field_38;
    char padding_3c[164];
    struct struct_3 *field_e0;
    char padding_e8[152];
    struct struct_5 *field_180;
} struct_4;

typedef struct struct_7 {
    char padding_0[16];
    char field_10;
} struct_7;

typedef struct struct_3 {
    char padding_0[28];
    char field_1c;
} struct_3;

typedef struct struct_2 {
    char padding_0[200];
    unsigned long long field_c8;
    char padding_d0[96];
    char field_130;
} struct_2;

typedef struct struct_5 {
    char padding_0[28];
    unsigned int field_1c;
    char padding_20[4];
    unsigned int field_24;
    unsigned int field_28;
} struct_5;

typedef struct struct_9 {
    unsigned long long field_0;
} struct_9;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

typedef struct struct_8 {
    char padding_0[184];
    struct struct_9 *field_b8;
} struct_8;

typedef struct struct_1 {
    char padding_0[304];
    char field_130;
} struct_1;

extern struct_0 *g_1ef0c58;
extern struct_1 *g_1ef1e28;
extern struct_8 *g_1ef22b8;
extern char g_1fab1e0;
extern char g_1fab21e;
extern char g_8520de;

long long TouchJoystickSpriteAnimator_OnUpdateAnimator(void* ptr, unsigned int a1)
{
    struct_4 *addr;  // x21
    unsigned long v1;  // x9
    unsigned int v9;  // s1
    unsigned long v11;  // 4168
    unsigned int v12;  // w20
    unsigned long long v13;  // x0
    unsigned long v2;  // x0
    unsigned long v3;  // x0
    unsigned int p[11];  // x22
    struct_7 *v5;  // x23
    unsigned int v6;  // s9
    unsigned int flag;  // w8
    unsigned int v8;  // s0

    if (!(g_1fab21e & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c(&g_1ef1e28);
        g_1fab21e = 1;
    }
    addr = (long long)ptr[40];
    if (!addr || !((v1 = (unsigned long)(unsigned long long)g_1ef1e28->field_130, (unsigned int)addr->field_0->field_130 < (unsigned int)v1 || *((long long *)(addr->field_0->field_c8 + v1 * 8 - 8)) != g_1ef1e28)))
    {
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        v3 = Object__op_Equality(addr, 0, 0);
        if (((char)v3 & 1))
            return v3;
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        v2 = Object__op_Equality((long long)ptr[64], 0, 0);
        if (((char)v2 & 1))
            return v2;
        if (addr)
        {
            p = addr->field_180;
            if ((int)ptr[240] != 2)
            {
                if ((int)ptr[240] != 1)
                    goto LABEL_104580c;
                if (p)
                {
                    v2 = JoystickState__GetDir4(p, 0);
                    goto LABEL_10457e0;
                }
            }
            else if (p)
            {
                v2 = JoystickState__GetDir8(p, 0);
LABEL_10457e0:
                if (7 >= (unsigned int)v2 - 1)
                    goto sub_1045804 + (&g_8520de)[1 + v2] * 4;
LABEL_104580c:
                v5 = NULL;
                if (addr->field_e0)
                {
                    if (addr->field_e0->field_1c)
                        v5 = (long long)ptr[248];
                    if (!v5 || !v5->field_10)
                        v5 = (long long)ptr[120];
                    if (!(!((char)CFUtils__get_editorStopped(0) & 1) && (v2 = (unsigned long)TouchControlAnimatorBase__IsIllegallyAttachedToSource(ptr, 0), !((char)v2 & 1))))
                    {
LABEL_10459ec:
                        v12 = a1 & 1;
                        TouchControlSpriteAnimatorBase__BeginSpriteAnim(ptr, v5, v12, 0, 0);
                        v13 = TouchControlSpriteAnimatorBase__UpdateSpriteAnimation(ptr, v12, 0);
                        return TouchControlSpriteAnimatorBase__UpdateSpriteAnimation(ptr, v12, 0);
                    }
                    else if (p)
                    {
                        v2 = JoystickState__GetVectorEx();
                        if ((char)ptr[320])
                        {
                            v6 = (int)ptr[224];
                            CFUtils__get_realDeltaTimeClamped(0);
                            v2 = CFUtils__SmoothTowardsVec2(0);
                            *((int *)&ptr[220]) = (int)ptr[220];
                            *((unsigned int *)&ptr[224]) = v6;
                        }
                        else
                        {
                            if (!g_1fab1e0)
                            {
                                v2 = sub_f7d92c(&g_1ef22b8);
                                g_1fab1e0 = 1;
                            }
                            *((unsigned long long *)&ptr[220]) = g_1ef22b8->field_b8->field_0;
                        }
                        flag = (int)ptr[336];
                        if (!flag)
                            goto LABEL_10459ec;
                        if (addr->field_e0)
                        {
                            if (addr->field_e0->field_1c)
                            {
                                v8 = p[9];
                                v9 = p[10];
                                switch (flag)
                                {
                                case 3:
                                    v11 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(p[9] * p[9] + p[10] * p[10], 953267991)) >> 5 & 3 | (unsigned long long)(CmpF(v8 * v8 + v9 * v9, 953267991) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v8 * v8 + v9 * v9, 953267991)) >> 5 & 3 | (unsigned long long)(CmpF(v8 * v8 + v9 * v9, 953267991) & 1)) & ((unsigned long long)(char)(CmpF(v8 * v8 + v9 * v9, 953267991)) >> 5 & 3 | (unsigned long long)(CmpF(v8 * v8 + v9 * v9, 953267991) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                                    if (!((char)v11))
                                        *((unsigned int *)&ptr[348]) = p[7];
                                    goto LABEL_10459b8;
                                case 1:
                                    break;
                                default:
                                    break;
                                }
                            }
                            else
                            {
                                *((unsigned int *)&ptr[348]) = 0;
                            }
LABEL_10459b8:
                            CFUtils__get_realDeltaTimeClamped(0);
                            CFUtils__SmoothTowardsAngle(0);
                            *((int *)&ptr[236]) = (int)ptr[236];
                            goto LABEL_10459ec;
                        }
                    }
                }
            }
        }
    }
    else
    {
        v2 = sub_f7df10(addr);
    }
    sub_f7db74(v2);
}
```

## `TouchJoystickSpriteAnimator.GetComponent` — RVA `0xc45a40`

- Decompiled symbol: `TouchJoystickSpriteAnimator_GetComponent`
- Metadata signature: `private MonoBehaviour ControlFreak2.Internal.ISpriteAnimator.GetComponent() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long TouchJoystickSpriteAnimator_GetComponent(void)
{
    unsigned long v0;  // x0

    return v0;
}
```

## `TouchJoystickSpriteAnimator.AddUsedSprites` — RVA `0xc45a44`

- Decompiled symbol: `TouchJoystickSpriteAnimator_AddUsedSprites`
- Metadata signature: `private void ControlFreak2.Internal.ISpriteAnimator.AddUsedSprites(ISpriteOptimizer optimizer) { }`
- Native interval: `1160` bytes
- Result: `pseudocode`
- Heuristic layout hint: `TouchJoystickSpriteAnimator_Recovered` matched 2 offsets against `TouchJoystickSpriteAnimator` metadata (confidence 1.00).

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

typedef struct TouchJoystickSpriteAnimator_Recovered {
    char padding_0[312];
    struct struct_3 *spriteUpLeft;
    unsigned long long animateTransl;
} TouchJoystickSpriteAnimator_Recovered;

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

extern char g_1fab21f;

void TouchJoystickSpriteAnimator_AddUsedSprites(struct_1 *pos, struct_5 **p)
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
    if (!(g_1fab21f & 1))
    {
        sub_f7d92c("eA");
        g_1fab21f = 1;
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
                    goto LABEL_1045ae0;
                }
            } while ((v14 = (unsigned long)(v13 - 1), cur = (unsigned long)(cur + 16), v11 = (unsigned long)(v13 - 1), v13 != 1));
        }
        addr = sub_f80110(p);
LABEL_1045ae0:
        v16 = *((long long *)&addr->padding_0[8]);
        v17 = p;
        v18 = pos->field_78->field_18;
        (*((long long *)&addr->padding_0[0]))();
    }
    sub_f7db74();
}
```

## `TouchJoystickSpriteAnimator.OnSpriteOptimization` — RVA `0xc45ecc`

- Decompiled symbol: `TouchJoystickSpriteAnimator_OnSpriteOptimization`
- Metadata signature: `private void ControlFreak2.Internal.ISpriteAnimator.OnSpriteOptimization(ISpriteOptimizer optimizer) { }`
- Native interval: `1280` bytes
- Result: `pseudocode`
- Heuristic layout hint: `TouchJoystickSpriteAnimator_Recovered` matched 2 offsets against `TouchJoystickSpriteAnimator` metadata (confidence 1.00).

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

typedef struct TouchJoystickSpriteAnimator_Recovered {
    char padding_0[312];
    struct struct_3 *spriteUpLeft;
    unsigned long long animateTransl;
} TouchJoystickSpriteAnimator_Recovered;

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

extern char g_1fab220;

void TouchJoystickSpriteAnimator_OnSpriteOptimization(struct_1 *pos, struct_5 **p)
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
    if (!(g_1fab220 & 1))
    {
        sub_f7d92c("eA");
        g_1fab220 = 1;
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
                    goto LABEL_1045f64;
                }
            } while ((v16 = (unsigned long)(v15 - 1), cur = (unsigned long)(cur + 16), v13 = (unsigned long)(v15 - 1), v15 != 1));
        }
        addr = sub_f80110(p);
LABEL_1045f64:
        v18 = *((long long *)&addr->padding_0[8]);
        v19 = p;
        v20 = pos->field_78->field_18;
        (*((long long *)&addr->padding_0[0]))();
    }
    sub_f7db74();
}
```
