# Native pseudocode: SuperTouchZone.MultiFingerTouch

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `SuperTouchZone.MultiFingerTouch.ctor` — RVA `0xc49504`

- Decompiled symbol: `SuperTouchZone_MultiFingerTouch_ctor`
- Metadata signature: `public void .ctor(int fingerCount, SuperTouchZone zone) { }`
- Native interval: `364` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    long long field_10;
} struct_0;

extern long long g_1ef0550;
extern long long g_1ef1e18;
extern char g_1fab23f;

long long SuperTouchZone_MultiFingerTouch_ctor(struct_0 *ptr, unsigned long a1, long long a2)
{
    unsigned long long v9;  // x30
    unsigned long long v10;  // x26
    unsigned long long v11;  // x25
    unsigned long long v12;  // x24
    unsigned long long v13;  // x23
    unsigned long long v14;  // x22
    unsigned long long v15;  // x21
    unsigned long long v16;  // x20
    unsigned long long v17;  // x19
    unsigned long long v0;  // [bp-0x50]
    unsigned long long v1;  // [bp-0x40]
    unsigned long long v2;  // [bp-0x38]
    unsigned long long v3;  // [bp-0x30]
    unsigned long long v4;  // [bp-0x28]
    unsigned long long v5;  // [bp-0x20]
    unsigned long long v6;  // [bp-0x18]
    unsigned long long v7;  // [bp-0x10]
    unsigned long long v8;  // [bp-0x8]

    v0 = v9;
    v1 = v10;
    v2 = v11;
    v3 = v12;
    v4 = v13;
    v5 = v14;
    v6 = v15;
    v7 = v16;
    v8 = v17;
    if (!(g_1fab23f & 1))
    {
        sub_f7d92c("u*");
        sub_f7d92c(&g_1ef0550);
        sub_f7d92c(&g_1ef1e18);
        sub_f7d92c("%Y");
        g_1fab23f = 1;
    }
    Object__ctor(ptr, 0);
    ptr->field_10 = a2;
    sub_f7d8d0((struct struct_0 *)&ptr->field_10, a2);
    TouchGestureState__ctor(sub_f7db70(g_1ef1e18), 0); /* do not return */
}
```

## `SuperTouchZone.MultiFingerTouch.Init` — RVA `0xc49870`

- Decompiled symbol: `SuperTouchZone_MultiFingerTouch_Init`
- Metadata signature: `public void Init(SuperTouchZone.MultiFingerTouchConfig config) { }`
- Native interval: `212` bytes
- Result: `pseudocode`
- Heuristic layout hint: `SuperTouchZone_MultiFingerTouch_Recovered` matched 5 offsets against `SuperTouchZone.MultiFingerTouch` metadata (confidence 1.00).

```c
typedef struct SuperTouchZone_MultiFingerTouch_Recovered {
    char padding_0[16];
    struct struct_0 *zone;
    struct struct_1 *touchScreen;
    struct struct_2 *touchOriented;
    char padding_28[56];
    struct struct_3 *swipeJoyState;
    struct struct_5 *config;
} SuperTouchZone_MultiFingerTouch_Recovered;

typedef struct struct_1 {
    char padding_0[272];
    long long field_110;
    unsigned long long field_118;
} struct_1;

typedef struct struct_2 {
    char padding_0[272];
    long long field_110;
    unsigned long long field_118;
} struct_2;

typedef struct struct_0 {
    char padding_0[136];
    long long field_88;
} struct_0;

typedef struct struct_3 {
    char padding_0[16];
    unsigned long long field_10;
} struct_3;

typedef struct struct_5 {
    char padding_0[136];
    unsigned long long field_88;
    unsigned long long field_90;
} struct_5;

void SuperTouchZone_MultiFingerTouch_Init(struct_4 *ptr, unsigned long long *p)
{
    unsigned long long v4;  // x30
    unsigned long long v5;  // x21
    long long v14;  // x1
    struct_2 *addr;  // x9
    long long v16;  // x1
    unsigned long long v6;  // x20
    unsigned long long v7;  // x19
    struct_4 *ptr3;  // x21
    struct_1 *ptr4;  // x8
    unsigned long long v10;  // x1
    struct_2 *ptr5;  // x8
    unsigned long long v12;  // x1
    struct_1 *ptr6;  // x9
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x18]
    unsigned long long v2;  // [bp-0x10]
    unsigned long long v3;  // [bp-0x8]

    v0 = v4;
    v1 = v5;
    v2 = v6;
    v3 = v7;
    ptr->field_68 = p;
    ptr3 = &ptr->field_68;
    sub_f7d8d0(ptr3);
    ptr4 = *((long long *)&ptr3->padding_28[40]);
    if (p)
    {
        v10 = p[17];
        if (ptr4)
            goto LABEL_10498ac;
    }
    else
    {
        v10 = 0;
        if (ptr4)
        {
LABEL_10498ac:
            ptr4->field_118 = v10;
            sub_f7d8d0((struct struct_1 *)&ptr4->field_118);
            ptr5 = ptr->field_20;
            if (p)
            {
                v12 = p[17];
                if (ptr5)
                    goto LABEL_10498d4;
            }
            else
            {
                v12 = 0;
                if (ptr5)
                {
LABEL_10498d4:
                    ptr5->field_118 = v12;
                    sub_f7d8d0((struct struct_2 *)&ptr5->field_118);
                    if (ptr->field_10)
                    {
                        ptr6 = ptr->field_18;
                        if (ptr6)
                        {
                            v14 = ptr->field_10->field_88;
                            ptr6->field_110 = v14;
                            sub_f7d8d0((struct struct_1 *)&ptr6->field_110, v14);
                            if (ptr->field_10)
                            {
                                addr = ptr->field_20;
                                if (addr)
                                {
                                    v16 = ptr->field_10->field_88;
                                    addr->field_110 = v16;
                                    sub_f7d8d0((struct struct_2 *)&addr->field_110, v16);
                                    if (p && ptr->field_60)
                                    {
                                        ptr->field_60->field_10 = p[18];
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
    sub_f7db74();
}
```

## `SuperTouchZone.MultiFingerTouch.Reset` — RVA `0xc49af8`

- Decompiled symbol: `SuperTouchZone_MultiFingerTouch_Reset`
- Metadata signature: `public void Reset() { }`
- Native interval: `80` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    char padding_0[24];
    struct struct_3 *field_18;
} struct_2;

typedef struct struct_0 {
    char padding_0[376];
    struct struct_1 *field_178;
    unsigned long long field_180;
} struct_0;

typedef struct struct_3 {
    struct struct_0 *field_0;
} struct_3;

typedef struct struct_1 {
    unsigned long long field_0;
} struct_1;

void SuperTouchZone_MultiFingerTouch_Reset(struct_2 *ptr)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    struct_0 **v4;  // x0
    unsigned long long v5;  // x1
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    v4 = ptr->field_18;
    if (!ptr->field_18)
        sub_f7db74(0);
    v5 = ptr->field_18->field_0->field_180;
    ptr->field_18->field_0->field_178();
}
```

## `SuperTouchZone.MultiFingerTouch.GetFingerCount` — RVA `0xc4a4a0`

- Decompiled symbol: `SuperTouchZone_MultiFingerTouch_GetFingerCount`
- Metadata signature: `public int GetFingerCount() { }`
- Native interval: `28` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[48];
    struct struct_0 *field_30;
} struct_1;

typedef struct struct_0 {
    char padding_0[24];
    unsigned int field_18;
} struct_0;

int SuperTouchZone_MultiFingerTouch_GetFingerCount(struct_1 *a0)
{
    if (a0->field_30)
        return a0->field_30->field_18;
    sub_f7db74();
}
```

## `SuperTouchZone.MultiFingerTouch.Start` — RVA `0xc4a4bc`

- Decompiled symbol: `SuperTouchZone_MultiFingerTouch_Start`
- Metadata signature: `public void Start(SuperTouchZone.FingerState[] fingers, Vector2 startScreenPos, Vector2 startOrientedPos, bool quietMode, float quietAlreadyElapsed) { }`
- Native interval: `452` bytes
- Result: `pseudocode`
- Heuristic layout hint: `SuperTouchZone_MultiFingerTouch_Recovered` matched 11 offsets against `SuperTouchZone.MultiFingerTouch` metadata (confidence 0.73).

```c
typedef struct SuperTouchZone_MultiFingerTouch_Recovered {
    char padding_0[24];
    long long touchScreen;
    unsigned long long touchOriented;
    unsigned int quietModeElapsed;
    char padding_2c[4];
    void* fingers;
    char active;
    char quietMode;
    char padding_3a[2];
    unsigned int posStartScreen;
    unsigned int field_40;
    unsigned int posStartOriented;
    unsigned int field_48;
    unsigned int posCurScreen;
    unsigned int field_50;
    unsigned int posCurOriented;
    unsigned int field_58;
    char controlledByMouse;
} SuperTouchZone_MultiFingerTouch_Recovered;

typedef struct struct_0 {
    char padding_0[32];
    long long field_20;
} struct_0;

struct_2 * SuperTouchZone_MultiFingerTouch_Start(struct_2 *ptr, unsigned long long a1, unsigned int a2)
{
    void* p;  // x23
    unsigned int i;  // w8
    struct_0 *addr;  // x0
    unsigned int v11;  // s4
    unsigned int v12;  // s0
    unsigned int v13;  // s1
    unsigned int v14;  // s2
    unsigned int v15;  // s3
    unsigned long long v16;  // x0
    unsigned long v2;  // x20
    struct_2 *v3;  // x0
    unsigned long long v4;  // x24
    struct_2 *v5;  // x0
    struct_2 *v6;  // x0
    unsigned long long v7;  // x25
    unsigned long v8;  // x22

    p = ptr->field_30;
    ptr->field_5c = 1;
    if (p)
    {
        i = (int)p[24];
        v2 = a2;
        v3 = ptr;
        if (i >= 1)
        {
            v4 = 0;
            v5 = ptr;
            do
            {
                v6 = v5;
                if (!a1)
                    goto LABEL_104a66c;
                if (*((int *)(a1 + 24)) <= (unsigned int)v4)
                    goto LABEL_104a670;
                v7 = v4 * 0x100000000 >> 63 & 0xffffffff00000000 | v4 & 4294967295;
                v8 = *((long long *)(a1 + v7 * 8 + 32));
                if (v8)
                {
                    v6 = sub_f7da60(v8, *((long long *)(*((long long *)p) + 64)));
                    if (!v6)
                        sub_f7da4c(sub_f7db98(v6), 0);
                    i = (int)p[24];
                }
                if (i <= (unsigned int)v4)
                    goto LABEL_104a670;
                addr = p + v7 * 8;
                addr->field_20 = v8;
                v6 = sub_f7d8d0((struct struct_0 *)&addr->field_20, v8);
                p = ptr->field_30;
                if (!p)
                    goto LABEL_104a66c;
                i = (long long)p[24];
                if (i <= (unsigned int)v4)
                    goto LABEL_104a670;
                if (!*((long long *)(32 + (char *)p + 8 * v7)))
                    goto LABEL_104a66c;
                else
                    goto LABEL_104a588;
LABEL_104a588:
                if (!*((long long *)(*((long long *)(32 + (char *)p + 8 * v7)) + 24)) || !*((char *)(*((long long *)(*((long long *)(32 + (char *)p + 8 * v7)) + 24)) + 17)))
                    ptr->field_5c = 0;
                v4 = (unsigned int)v4 + 1;
                v5 = v6;
                v3 = v6;
            } while ((unsigned int)v4 < i);
            goto LABEL_104a670;
        }
        else
        {
            ptr->field_28 = v11;
            ptr->field_3c = v12;
            ptr->field_40 = v13;
            ptr->field_44 = v14;
            ptr->field_48 = v15;
            ptr->field_4c = v12;
            ptr->field_50 = v13;
            ptr->field_38 = 1;
            ptr->field_39 = (char)v2 & 1;
            ptr->field_54 = v14;
            ptr->field_58 = v15;
            if (((char)v2 & 1))
            {
                return v3;
            }
            else if (ptr->field_18)
            {
                TouchGestureBasicState__OnTouchStart(ptr->field_18, ptr->field_5c, 0, 0);
                if (ptr->field_20)
                {
                    v16 = TouchGestureBasicState__OnTouchStart();
                    return TouchGestureBasicState__OnTouchStart();
                }
            }
        }
    }
LABEL_104a66c:
    v6 = sub_f7db74();
LABEL_104a670:
    v6 = sub_f7db7c(v6);
    sub_f7da4c(sub_f7db98(v6), 0);
}
```

## `SuperTouchZone.MultiFingerTouch.End` — RVA `0xc4a8c0`

- Decompiled symbol: `SuperTouchZone_MultiFingerTouch_End`
- Metadata signature: `public void End(bool cancel) { }`
- Native interval: `132` bytes
- Result: `pseudocode`
- Heuristic layout hint: `SuperTouchZone_MultiFingerTouch_Recovered` matched 4 offsets against `SuperTouchZone.MultiFingerTouch` metadata (confidence 1.00).

```c
typedef struct SuperTouchZone_MultiFingerTouch_Recovered {
    char padding_0[24];
    unsigned long long touchScreen;
    unsigned long long touchOriented;
    char padding_28[16];
    char active;
    char quietMode;
} SuperTouchZone_MultiFingerTouch_Recovered;

struct_0 * SuperTouchZone_MultiFingerTouch_End(struct_0 *ptr, unsigned long a1)
{
    unsigned long long v0;  // x0
    unsigned long long v1;  // x0

    if (!ptr->field_38)
        return ptr;
    v0 = ptr->field_18;
    ptr->field_38 = 0;
    if (v0)
    {
        TouchGestureBasicState__OnTouchEnd();
        if (ptr->field_20)
        {
            v1 = TouchGestureBasicState__OnTouchEnd();
            return TouchGestureBasicState__OnTouchEnd();
        }
    }
    sub_f7db74();
}
```

## `SuperTouchZone.MultiFingerTouch.EndAndReport` — RVA `0xc4a944`

- Decompiled symbol: `SuperTouchZone_MultiFingerTouch_EndAndReport`
- Metadata signature: `public void EndAndReport() { }`
- Native interval: `92` bytes
- Result: `pseudocode`
- Heuristic layout hint: `SuperTouchZone_MultiFingerTouch_Recovered` matched 4 offsets against `SuperTouchZone.MultiFingerTouch` metadata (confidence 1.00).

```c
typedef struct SuperTouchZone_MultiFingerTouch_Recovered {
    char padding_0[24];
    long long touchScreen;
    unsigned long long touchOriented;
    char padding_28[16];
    char active;
    char quietMode;
} SuperTouchZone_MultiFingerTouch_Recovered;

struct_0 * SuperTouchZone_MultiFingerTouch_EndAndReport(struct_0 *ptr)
{
    unsigned long v0;  // x0
    unsigned long long v1;  // x0

    if (!ptr->field_38)
        return ptr;
    if (ptr->field_39)
        SuperTouchZone_MultiFingerTouch__StartOfficially(ptr);
    v0 = ptr->field_18;
    ptr->field_38 = 0;
    if (v0)
    {
        TouchGestureBasicState__OnTouchEnd(v0, 0, 0);
        v0 = ptr->field_20;
        if (v0)
        {
            v1 = TouchGestureBasicState__OnTouchEnd();
            return TouchGestureBasicState__OnTouchEnd();
        }
    }
    sub_f7db74(v0);
}
```

## `SuperTouchZone.MultiFingerTouch.DisableTapUntilRelease` — RVA `0xc4b0b0`

- Decompiled symbol: `SuperTouchZone_MultiFingerTouch_DisableTapUntilRelease`
- Metadata signature: `public void DisableTapUntilRelease() { }`
- Native interval: `48` bytes
- Result: `pseudocode`

```c
long long SuperTouchZone_MultiFingerTouch_DisableTapUntilRelease(unsigned long long *ptr)
{
    unsigned long v0;  // x0
    unsigned long long v1;  // x0

    v0 = ptr[4];
    if (v0)
    {
        TouchGestureState__DisableTapUntilRelease(v0, 0);
        v0 = ptr[3];
        if (ptr[3])
        {
            v1 = TouchGestureState__DisableTapUntilRelease();
            return TouchGestureState__DisableTapUntilRelease();
        }
    }
    sub_f7db74(v0);
}
```

## `SuperTouchZone.MultiFingerTouch.SetPos` — RVA `0xc4b0e0`

- Decompiled symbol: `SuperTouchZone_MultiFingerTouch_SetPos`
- Metadata signature: `public void SetPos(Vector2 screenPos, Vector2 orientedPos) { }`
- Native interval: `12` bytes
- Result: `pseudocode`

```c
unsigned int [23] SuperTouchZone_MultiFingerTouch_SetPos(unsigned int *ptr)
{
    unsigned int v0;  // s0
    unsigned int v1;  // s1
    unsigned int v2;  // s2
    unsigned int v3;  // s3

    ptr[19] = v0;
    ptr[20] = v1;
    ptr[21] = v2;
    ptr[22] = v3;
    return ptr;
}
```

## `SuperTouchZone.MultiFingerTouch.Update` — RVA `0xc4b0ec`

- Decompiled symbol: `SuperTouchZone_MultiFingerTouch_Update`
- Metadata signature: `public void Update() { }`
- Native interval: `1792` bytes
- Result: `pseudocode`
- Heuristic layout hint: `SuperTouchZone_MultiFingerTouch_Recovered` matched 9 offsets against `SuperTouchZone.MultiFingerTouch` metadata (confidence 1.00).

```c
typedef struct SuperTouchZone_MultiFingerTouch_Recovered {
    char padding_0[16];
    struct struct_3 *zone;
    struct struct_3 *touchScreen;
    struct struct_3 *touchOriented;
    unsigned int quietModeElapsed;
    char padding_2c[4];
    struct struct_3 *fingers;
    char active;
    char quietMode;
    char padding_3a[18];
    unsigned long long posCurScreen;
    unsigned long long posCurOriented;
} SuperTouchZone_MultiFingerTouch_Recovered;

typedef struct struct_8 {
    struct struct_5 *field_0;
    char padding_8[32];
    struct struct_7 *field_28;
    char padding_30[88];
    unsigned long long field_88;
    char padding_90[12];
    unsigned int field_9c;
    char padding_a0[16];
    unsigned long long field_b0;
    char padding_b8[110];
    char field_126;
} struct_8;

typedef struct struct_9 {
    char padding_0[28];
    char field_1c;
} struct_9;

typedef struct struct_3 {
    struct struct_0 *field_0;
    char padding_8[32];
    struct struct_2 *field_28;
    char padding_30[88];
    unsigned long long field_88;
    char padding_90[12];
    unsigned int field_9c;
    char padding_a0[16];
    unsigned long long field_b0;
    char padding_b8[110];
    char field_126;
} struct_3;

typedef struct struct_5 {
    char padding_0[392];
    struct struct_6 *field_188;
    unsigned long long field_190;
} struct_5;

typedef struct struct_7 {
    char padding_0[28];
    char field_1c;
} struct_7;

typedef struct struct_0 {
    char padding_0[392];
    struct struct_1 *field_188;
    unsigned long long field_190;
} struct_0;

typedef struct struct_2 {
    char padding_0[28];
    char field_1c;
} struct_2;

typedef struct struct_6 {
    unsigned long long field_0;
} struct_6;

typedef struct struct_1 {
    unsigned long long field_0;
} struct_1;

extern long long g_1ef0c58;
extern char g_1fab240;

void SuperTouchZone_MultiFingerTouch_Update(struct_4 *ptr, unsigned long a1)
{
    unsigned long long v8;  // d9
    unsigned long long v9;  // d8
    struct_4 *v17;  // x22
    unsigned long long v18;  // x21
    struct_8 *p;  // x8
    struct_9 *v20;  // x20
    unsigned int v21;  // s0
    unsigned int v22;  // s0
    unsigned int v23;  // s1
    unsigned long v24;  // 4129
    struct_8 *v25;  // x0
    unsigned long v26;  // x1
    unsigned long long v10;  // x30
    unsigned long long v11;  // x23
    unsigned long long v12;  // x22
    unsigned long long v13;  // x21
    unsigned long long v14;  // x20
    unsigned long long v15;  // x19
    char v16;  // x9
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
    if (!(g_1fab240 & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab240 = 1;
    }
    p = ptr->field_18;
    if (ptr->field_38 && p)
    {
        v16 = ptr->field_39;
        p->field_126 = v16;
        p = ptr->field_20;
        v17 = &ptr->field_20;
        if (p)
        {
            p->field_126 = v16;
            p = ptr->field_30;
            if (p)
            {
                v18 = 0;
                do
                {
                    if (*((int *)&p->padding_8[16]) > (unsigned int)v18)
                    {
                        if (*((int *)&p->padding_8[16]) <= (unsigned int)v18)
                            sub_f7db7c();
                        p = *((long long *)&p->padding_8[24 + 8 * v18]);
                        if (!p || !((v20 = (struct_9 *)p->field_28, v20)))
                            break;
                        if (v20->field_1c)
                        {
                            p = ptr->field_10;
                            if (!p || !p->field_88)
                                break;
                            TouchGestureThresholds__get_tapMoveThreshPxSq(p->field_88, 0);
                            if (!(TouchGestureBasicState__Moved(v20, 0) & 1))
                                continue;
                            if (!ptr->field_18 || !((TouchGestureState__MarkAsNonStatic(ptr->field_18, 0), *((long long *)&v17->padding_0[0]))))
                                break;
                            TouchGestureState__MarkAsNonStatic(*((long long *)&v17->padding_0[0]), 0);
                            if (ptr->field_39)
                                SuperTouchZone_MultiFingerTouch__StartOfficially(ptr);
                        }
                        else
                        {
                            SuperTouchZone_MultiFingerTouch__EndAndReport(ptr);
                            goto LABEL_104b210;
                        }
                    }
                    else
                    {
LABEL_104b210:
                        if (ptr->field_38)
                        {
                            if (ptr->field_39)
                            {
                                CFUtils__get_realDeltaTime(0);
                                p = ptr->field_10;
                                v22 = ptr->field_28 + v21;
                                ptr->field_28 = v22;
                                if (p)
                                {
                                    v23 = p->field_9c;
                                    v24 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v22, v23)) >> 5 & 3 | (unsigned long long)(CmpF(v22, v23) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v22, v23)) >> 5 & 3 | (unsigned long long)(CmpF(v22, v23) & 1)) & ((unsigned long long)(char)(CmpF(v22, v23)) >> 5 & 3 | (unsigned long long)(CmpF(v22, v23) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                                    if (!((char)v24))
                                        SuperTouchZone_MultiFingerTouch__StartOfficially(ptr);
                                }
                            }
                            else
                            {
                                p = ptr->field_18;
                                if (p)
                                {
                                    p->field_b0 = *((long long *)&(&ptr->padding_3a)[1]);
                                    p = ptr->field_20;
                                    if (p)
                                        p->field_b0 = *((long long *)((char *)&ptr->field_4c + 4));
                                }
                            }
                        }
                    }
                } while ((p = (struct_8 *)ptr->field_30, v18 += 1, p));
            }
        }
    }
    do
    {
        do
        {
            do
            {
                sub_f7db74();
            } while (!p);
        } while ((p->field_126 = 0, p = (struct_8 *)ptr->field_20, !p));
    } while ((p->field_126 = 0, v25 = (struct_8 *)ptr->field_18, !v25));
    v26 = v25->field_0->field_190;
    v25->field_0->field_188();
}
```

## `SuperTouchZone.MultiFingerTouch.SyncToRig` — RVA `0xc4bac8`

- Decompiled symbol: `SuperTouchZone_MultiFingerTouch_SyncToRig`
- Metadata signature: `public void SyncToRig() { }`
- Native interval: `68` bytes
- Result: `pseudocode`
- Heuristic layout hint: `SuperTouchZone_MultiFingerTouch_Recovered` matched 5 offsets against `SuperTouchZone.MultiFingerTouch` metadata (confidence 1.00).

```c
typedef struct SuperTouchZone_MultiFingerTouch_Recovered {
    char padding_0[16];
    struct struct_0 *zone;
    long long touchScreen;
    long long touchOriented;
    char padding_28[56];
    long long swipeJoyState;
    struct struct_1 *config;
} SuperTouchZone_MultiFingerTouch_Recovered;

typedef struct struct_1 {
    char padding_0[16];
    long long field_10;
} struct_1;

typedef struct struct_0 {
    char padding_0[88];
    long long field_58;
} struct_0;

struct_2 * SuperTouchZone_MultiFingerTouch_SyncToRig(struct_2 *a0)
{
    unsigned long long v0;  // x0

    if (!a0->field_68)
        return a0;
    if (a0->field_10 && a0->field_68->field_10)
    {
        v0 = TouchGestureStateBinding__SyncTouchState(a0->field_68->field_10, a0->field_18, a0->field_20, a0->field_60, a0->field_10->field_58, 0);
        return TouchGestureStateBinding__SyncTouchState(a0->field_68->field_10, a0->field_18, a0->field_20, a0->field_60, a0->field_10->field_58, 0);
    }
    sub_f7db74();
}
```

## `SuperTouchZone.MultiFingerTouch.GetFinger` — RVA `0xc4bb0c`

- Decompiled symbol: `SuperTouchZone_MultiFingerTouch_GetFinger`
- Metadata signature: `public SuperTouchZone.FingerState GetFinger(int i) { }`
- Native interval: `48` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[48];
    struct struct_0 *field_30;
} struct_1;

typedef struct struct_0 {
    char padding_0[24];
    unsigned int field_18;
} struct_0;

long long SuperTouchZone_MultiFingerTouch_GetFinger(struct_1 *ptr, unsigned int a1)
{
    struct_0 *v0;  // x8

    v0 = ptr->field_30;
    if (!v0)
    {
        ptr = sub_f7db74();
    }
    else if (v0->field_18 > a1)
    {
        return *((long long *)&v0[1].padding_0[4 + 8 * a1]);
    }
    sub_f7db7c(ptr);
}
```

## `SuperTouchZone.MultiFingerTouch.EndDrivingTouch` — RVA `0xc4c4e0`

- Decompiled symbol: `SuperTouchZone_MultiFingerTouch_EndDrivingTouch`
- Metadata signature: `public void EndDrivingTouch(bool cancel) { }`
- Native interval: `32` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[112];
    long long field_70;
} struct_0;

long long SuperTouchZone_MultiFingerTouch_EndDrivingTouch(struct_0 *a0, unsigned int a1, unsigned long a2)
{
    unsigned long long v0;  // x0

    if (a0->field_70)
    {
        v0 = TouchObject__End(a0->field_70, a1 & 1, 0);
        return TouchObject__End(a0->field_70, a1 & 1, 0);
    }
    sub_f7db74(0);
}
```

## `SuperTouchZone.MultiFingerTouch.IsActive` — RVA `0xc4cdf4`

- Decompiled symbol: `SuperTouchZone_MultiFingerTouch_IsActive`
- Metadata signature: `public bool IsActive() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[56];
    char field_38;
} struct_0;

long long SuperTouchZone_MultiFingerTouch_IsActive(struct_0 *a0)
{
    return a0->field_38;
}
```

## `SuperTouchZone.MultiFingerTouch.IsQuiet` — RVA `0xc4cdfc`

- Decompiled symbol: `SuperTouchZone_MultiFingerTouch_IsQuiet`
- Metadata signature: `public bool IsQuiet() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[57];
    char field_39;
} struct_0;

long long SuperTouchZone_MultiFingerTouch_IsQuiet(struct_0 *a0)
{
    return a0->field_39;
}
```

## `SuperTouchZone.MultiFingerTouch.StartOfficially` — RVA `0xc4ce04`

- Decompiled symbol: `SuperTouchZone_MultiFingerTouch_StartOfficially`
- Metadata signature: `public void StartOfficially() { }`
- Native interval: `124` bytes
- Result: `pseudocode`
- Heuristic layout hint: `SuperTouchZone_MultiFingerTouch_Recovered` matched 5 offsets against `SuperTouchZone.MultiFingerTouch` metadata (confidence 1.00).

```c
typedef struct SuperTouchZone_MultiFingerTouch_Recovered {
    char padding_0[24];
    long long touchScreen;
    long long touchOriented;
    char padding_28[16];
    char active;
    char quietMode;
    char padding_3a[34];
    char controlledByMouse;
} SuperTouchZone_MultiFingerTouch_Recovered;

struct_0 * SuperTouchZone_MultiFingerTouch_StartOfficially(struct_0 *ptr)
{
    long long v0;  // x0
    unsigned long long v1;  // x0

    if (!ptr->field_38)
    {
        return ptr;
    }
    else if (ptr->field_39)
    {
        v0 = ptr->field_18;
        ptr->field_39 = 0;
        if (v0)
        {
            TouchGestureBasicState__OnTouchStart(v0, ptr->field_5c, 0, 0);
            v0 = ptr->field_20;
            if (v0)
            {
                v1 = TouchGestureBasicState__OnTouchStart();
                return TouchGestureBasicState__OnTouchStart();
            }
        }
        sub_f7db74(v0);
    }
    else
    {
        return ptr;
    }
}
```

## `SuperTouchZone.MultiFingerTouch.IsPotentialTapPossible` — RVA `0xc4ce80`

- Decompiled symbol: `SuperTouchZone_MultiFingerTouch_IsPotentialTapPossible`
- Metadata signature: `private bool IsPotentialTapPossible() { }`
- Native interval: `32` bytes
- Result: `pseudocode`

```c
unsigned long long SuperTouchZone_MultiFingerTouch_IsPotentialTapPossible(char *a0)
{
    if (!a0[56])
    {
        return 0;
    }
    else if (!a0[57])
    {
        return 0;
    }
    else
    {
        return 1;
    }
}
```

## `SuperTouchZone.MultiFingerTouch.CancelTap` — RVA `0xc4cea0`

- Decompiled symbol: `SuperTouchZone_MultiFingerTouch_CancelTap`
- Metadata signature: `public void CancelTap() { }`
- Native interval: `48` bytes
- Result: `pseudocode`

```c
long long SuperTouchZone_MultiFingerTouch_CancelTap(unsigned long long *ptr, unsigned long a1)
{
    unsigned long v0;  // x0
    unsigned long long v1;  // x0

    v0 = ptr[4];
    if (v0)
    {
        TouchGestureState__CancelTap(v0, 0);
        v0 = ptr[3];
        if (ptr[3])
        {
            v1 = TouchGestureState__CancelTap();
            return TouchGestureState__CancelTap();
        }
    }
    sub_f7db74(v0);
}
```

## `SuperTouchZone.MultiFingerTouch.StartDrivingControl` — RVA `0xc4ced0`

- Decompiled symbol: `SuperTouchZone_MultiFingerTouch_StartDrivingControl`
- Metadata signature: `private void StartDrivingControl(TouchControl c) { }`
- Native interval: `320` bytes
- Result: `pseudocode`
- Heuristic layout hint: `SuperTouchZone_MultiFingerTouch_Recovered` matched 3 offsets against `SuperTouchZone.MultiFingerTouch` metadata (confidence 1.00).

```c
typedef struct struct_3 {
    char padding_0[696];
    struct struct_4 *field_2b8;
    unsigned long long field_2c0;
} struct_3;

typedef struct SuperTouchZone_MultiFingerTouch_Recovered {
    char padding_0[16];
    long long zone;
    unsigned long long touchScreen;
    char padding_20[80];
    struct struct_1 *drivingTouch;
} SuperTouchZone_MultiFingerTouch_Recovered;

typedef struct struct_1 {
    char padding_0[16];
    char field_10;
} struct_1;

typedef struct struct_4 {
    unsigned long long field_0;
} struct_4;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab241;

long long SuperTouchZone_MultiFingerTouch_StartDrivingControl(struct_2 *ptr, struct_3 **a1)
{
    long long v0;  // x0
    long long v1;  // x0
    struct_1 *v2;  // x21
    struct_1 *v4;  // x1
    long long v5;  // x2
    unsigned long long flag;  // x3
    unsigned long v7;  // x4
    struct_3 **v8;  // x0

    if (!(g_1fab241 & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab241 = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v0 = Object__op_Equality(a1, 0, 0);
    if (((char)v0 & 1))
        return v0;
    if (a1)
    {
        v1 = TouchControl__IsActive(a1, 0);
        if (!((char)v1 & 1))
            return v1;
        v2 = ptr->field_70;
        if (v2)
        {
            if (v2->field_10)
            {
                return v1;
            }
            else if (ptr->field_18 && ptr->field_10)
            {
                TouchObject__Start(v2, TouchControl__GetCamera(ptr->field_10, 0), 0, 0, 0);
                v4 = ptr->field_70;
                v5 = ptr->field_10;
                flag = 1;
                v7 = *(a1)->field_2c0;
                v8 = a1;
                *(a1)->field_2b8();
            }
        }
    }
    sub_f7db74();
}
```
