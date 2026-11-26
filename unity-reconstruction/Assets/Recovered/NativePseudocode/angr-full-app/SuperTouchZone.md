# Native pseudocode: SuperTouchZone

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `SuperTouchZone.GetScrollDelta` — RVA `0xc44334`

- Decompiled symbol: `SuperTouchZone_GetScrollDelta`
- Metadata signature: `public Vector2 GetScrollDelta(int fingerCount) { }`
- Native interval: `96` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[32];
    long long field_20;
} struct_0;

extern long long g_1ef22b8;
extern char g_1fab1e0;

struct_0 * SuperTouchZone_GetScrollDelta(unsigned long a0, unsigned long a1, unsigned long a2)
{
    struct_0 *v0;  // x0
    unsigned long long v1;  // x0

    v0 = SuperTouchZone__GetMultiFingerTouch();
    if (v0)
    {
        if (v0->field_20)
        {
            v1 = TouchGestureState__GetScrollDelta(v0->field_20, 0);
            return TouchGestureState__GetScrollDelta(v0->field_20, 0);
        }
        sub_f7db74(0);
    }
    else
    {
        if (!g_1fab1e0)
        {
            v0 = sub_f7d92c(&g_1ef22b8);
            g_1fab1e0 = 1;
        }
        return v0;
    }
}
```

## `SuperTouchZone.JustTapped` — RVA `0xc44394`

- Decompiled symbol: `SuperTouchZone_JustTapped`
- Metadata signature: `public bool JustTapped(int fingerCount, int howManyTimes) { }`
- Native interval: `52` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    long long field_18;
} struct_0;

unsigned long long SuperTouchZone_JustTapped(unsigned long a0, unsigned long a1, unsigned int a2)
{
    struct_0 *v0;  // x0
    unsigned long long v1;  // x0

    v0 = SuperTouchZone__GetMultiFingerTouch();
    if (!v0)
        return 0;
    if (v0->field_18)
    {
        v1 = TouchGestureState__JustTapped(v0->field_18, a2, 0);
        return TouchGestureState__JustTapped(v0->field_18, a2, 0);
    }
    sub_f7db74(0);
}
```

## `SuperTouchZone.JustLongTapped` — RVA `0xc443c8`

- Decompiled symbol: `SuperTouchZone_JustLongTapped`
- Metadata signature: `public bool JustLongTapped(int fingerCount) { }`
- Native interval: `44` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[24];
    struct struct_0 *field_18;
} struct_1;

typedef struct struct_2 {
    char padding_0[296];
    char field_128;
} struct_2;

typedef struct struct_0 {
    char padding_0[296];
    char field_128;
} struct_0;

struct_1 * SuperTouchZone_JustLongTapped(void)
{
    struct_1 *v0;  // x0

    v0 = SuperTouchZone__GetMultiFingerTouch();
    if (!v0)
        return v0;
    if (v0->field_18)
    {
        if (!v0->field_18->field_128)
            return NULL;
        return 0x1;
    }
    sub_f7db74();
}
```

## `SuperTouchZone.PressedLong` — RVA `0xc443f4`

- Decompiled symbol: `SuperTouchZone_PressedLong`
- Metadata signature: `public bool PressedLong(int fingerCount) { }`
- Native interval: `44` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[24];
    struct struct_0 *field_18;
} struct_1;

typedef struct struct_2 {
    char padding_0[262];
    char field_106;
} struct_2;

typedef struct struct_0 {
    char padding_0[262];
    char field_106;
} struct_0;

struct_1 * SuperTouchZone_PressedLong(void)
{
    struct_1 *v0;  // x0

    v0 = SuperTouchZone__GetMultiFingerTouch();
    if (!v0)
        return v0;
    if (v0->field_18)
    {
        if (!v0->field_18->field_106)
            return NULL;
        return 0x1;
    }
    sub_f7db74();
}
```

## `SuperTouchZone.PressedNormal` — RVA `0xc44420`

- Decompiled symbol: `SuperTouchZone_PressedNormal`
- Metadata signature: `public bool PressedNormal(int fingerCount) { }`
- Native interval: `44` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[24];
    struct struct_0 *field_18;
} struct_1;

typedef struct struct_0 {
    char padding_0[260];
    char field_104;
} struct_0;

struct_1 * SuperTouchZone_PressedNormal(void)
{
    struct_1 *v0;  // x0

    v0 = SuperTouchZone__GetMultiFingerTouch();
    if (!v0)
        return v0;
    if (v0->field_18)
    {
        if (!v0->field_18->field_104)
            return NULL;
        return 0x1;
    }
    sub_f7db74();
}
```

## `SuperTouchZone.PressedRaw` — RVA `0xc4444c`

- Decompiled symbol: `SuperTouchZone_PressedRaw`
- Metadata signature: `public bool PressedRaw(int fingerCount) { }`
- Native interval: `44` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[24];
    struct struct_0 *field_18;
} struct_1;

typedef struct struct_2 {
    char padding_0[28];
    char field_1c;
} struct_2;

typedef struct struct_0 {
    char padding_0[28];
    char field_1c;
} struct_0;

struct_1 * SuperTouchZone_PressedRaw(void)
{
    struct_1 *v0;  // x0

    v0 = SuperTouchZone__GetMultiFingerTouch();
    if (!v0)
        return v0;
    if (v0->field_18)
    {
        if (!v0->field_18->field_1c)
            return NULL;
        return 0x1;
    }
    sub_f7db74();
}
```

## `SuperTouchZone.ctor` — RVA `0xc48e34`

- Decompiled symbol: `SuperTouchZone_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `1544` bytes
- Result: `pseudocode`
- Heuristic layout hint: `SuperTouchZone_Recovered` matched 5 offsets against `SuperTouchZone` metadata (confidence 1.00).

```c
typedef struct SuperTouchZone_Recovered {
    char padding_0[144];
    unsigned long long maxFingers;
    char padding_98[288];
    unsigned long long emuMouseTwoFingersKey;
    unsigned int emuMousePinchKey;
    char padding_1c4[8];
    unsigned int emuMouseTwistAxis;
    uint128_t emuKeySwipeSpeed;
} SuperTouchZone_Recovered;

extern long long g_1eee580;
extern long long g_1eee588;
extern long long g_1eee758;
extern long long g_1eef6e0;
extern long long g_1ef0af8;
extern long long g_1ef3ad0;
extern long long g_1ef3ad8;
extern long long g_1ef3ae0;
extern char g_1fab239;

long long SuperTouchZone_ctor(struct_0 *ptr)
{
    unsigned long long v13;  // x30
    unsigned long long v14;  // x28
    unsigned long long v23;  // x19
    unsigned long long v15;  // x27
    unsigned long long v16;  // x26
    unsigned long long v17;  // x25
    unsigned long long v18;  // x24
    unsigned long long v19;  // x23
    unsigned long long v20;  // x22
    unsigned long long v21;  // x21
    unsigned long long v22;  // x20
    char *v0;  // [bp-0x60]
    unsigned long long v1;  // [bp-0x58]
    unsigned long long v2;  // [bp-0x50]
    unsigned long long v3;  // [bp-0x48]
    unsigned long long v4;  // [bp-0x40]
    unsigned long long v5;  // [bp-0x38]
    unsigned long long v6;  // [bp-0x30]
    unsigned long long v7;  // [bp-0x28]
    unsigned long long v8;  // [bp-0x20]
    unsigned long long v9;  // [bp-0x18]
    unsigned long long v10;  // [bp-0x10]
    unsigned long long v11;  // [bp-0x8]
    char v12;  // [bp+0x0]

    v0 = &v12;
    v1 = v13;
    v2 = v14;
    v3 = v15;
    v4 = v16;
    v5 = v17;
    v6 = v18;
    v7 = v19;
    v8 = v20;
    v9 = v21;
    v10 = v22;
    v11 = v23;
    if (!(g_1fab239 & 1))
    {
        sub_f7d92c(&g_1eee758);
        sub_f7d92c("g.");
        sub_f7d92c("y7");
        sub_f7d92c(&g_1eef6e0);
        sub_f7d92c("u*");
        sub_f7d92c(&g_1ef3ad0);
        sub_f7d92c(&g_1eee588);
        sub_f7d92c(&g_1ef3ae0);
        sub_f7d92c(&g_1eee580);
        sub_f7d92c(&g_1ef3ad8);
        sub_f7d92c(&g_1ef0af8);
        sub_f7d92c("5Q");
        g_1fab239 = 1;
    }
    ptr->field_90 = 4539628424389459971;
    ptr->field_1b8 = 1305670058290;
    ptr->field_1c0 = 304;
    ptr->field_1cc = 1;
    ptr->field_1d0 = 0x3e99999a423400003e8000003e800000;
    TouchControl__ctor(ptr, 0); /* do not return */
}
```

## `SuperTouchZone.InitEmulatedFingers` — RVA `0xc4975c`

- Decompiled symbol: `SuperTouchZone_InitEmulatedFingers`
- Metadata signature: `private void InitEmulatedFingers() { }`
- Native interval: `100` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[488];
    long long field_1e8;
} struct_0;

extern long long g_1ef3ac8;
extern char g_1fab23c;

void SuperTouchZone_InitEmulatedFingers(struct_0 *ptr)
{
    unsigned long long v4;  // x30
    unsigned long long v5;  // x21
    unsigned long long v6;  // x20
    unsigned long long v7;  // x19
    long long v8;  // x0
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x18]
    unsigned long long v2;  // [bp-0x10]
    unsigned long long v3;  // [bp-0x8]

    v0 = v4;
    v1 = v5;
    v2 = v6;
    v3 = v7;
    if (!(g_1fab23c & 1))
    {
        sub_f7d92c(&g_1ef3ac8);
        g_1fab23c = 1;
    }
    v8 = sub_f7db70(g_1ef3ac8);
    SuperTouchZone_EmulatedFingerSystem__ctor(v8, ptr, 0);
    ptr->field_1e8 = v8;
    sub_f7d8d0();
    return;
}
```

## `SuperTouchZone.OnDestroyControl` — RVA `0xc497c0`

- Decompiled symbol: `SuperTouchZone_OnDestroyControl`
- Metadata signature: `protected override void OnDestroyControl() { }`
- Native interval: `16` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[664];
    unsigned long long field_298;
} struct_0;

long long SuperTouchZone_OnDestroyControl(struct_0 **a0)
{
    goto *(a0)->field_298;
}
```

## `SuperTouchZone.OnInitControl` — RVA `0xc497d0`

- Decompiled symbol: `SuperTouchZone_OnInitControl`
- Metadata signature: `protected override void OnInitControl() { }`
- Native interval: `160` bytes
- Result: `pseudocode`
- Heuristic layout hint: `SuperTouchZone_Recovered` matched 2 offsets against `SuperTouchZone` metadata (confidence 0.67).

```c
typedef struct SuperTouchZone_Recovered {
    struct struct_0 *field_0;
    char padding_8[176];
    struct struct_1 *multiFingerTouch;
    unsigned long long multiFingerConfigs;
} SuperTouchZone_Recovered;

typedef struct struct_3 {
    char padding_0[24];
    unsigned int field_18;
} struct_3;

typedef struct struct_0 {
    char padding_0[664];
    unsigned long long field_298;
} struct_0;

typedef struct struct_1 {
    char padding_0[24];
    int field_18;
} struct_1;

void SuperTouchZone_OnInitControl(struct_2 *p, unsigned long a1)
{
    unsigned long long v3;  // x30
    unsigned long long v4;  // x20
    unsigned long long v5;  // x19
    struct_3 *v6;  // x8
    struct_2 *ptr;  // x19
    unsigned long long v8;  // x20
    unsigned int v9;  // w9
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x10]
    unsigned long long v2;  // [bp-0x8]

    v0 = v3;
    v1 = v4;
    v2 = v5;
    v6 = p->field_b8;
    if (p->field_b8)
    {
        ptr = p;
        v8 = 4;
    }
    else
    {
LABEL_1049840:
        sub_f7db74();
        goto LABEL_1049844;
    }
    while (true)
    {
        v9 = v8 - 4;
        if (v6->field_18 <= v9)
            break;
        if (v6->field_18 <= v9)
        {
LABEL_104986c:
            sub_f7db7c();
        }
        if (!ptr->field_c0)
            goto LABEL_1049840;
        if (*((int *)(ptr->field_c0 + 24)) > v9 && *((int *)(ptr->field_c0 + 24)) <= v9)
            goto LABEL_104986c;
        goto LABEL_1049840;
    }
LABEL_1049844:
    SuperTouchZone__SetTouchSmoothing(ptr);
    goto ptr->field_0->field_298;
}
```

## `SuperTouchZone.SetTouchSmoothing` — RVA `0xc49944`

- Decompiled symbol: `SuperTouchZone_SetTouchSmoothing`
- Metadata signature: `public void SetTouchSmoothing(float smPow) { }`
- Native interval: `216` bytes
- Result: `pseudocode`
- Heuristic layout hint: `SuperTouchZone_Recovered` matched 3 offsets against `SuperTouchZone` metadata (confidence 1.00).

```c
typedef struct SuperTouchZone_Recovered {
    char padding_0[148];
    unsigned int touchSmoothing;
    char padding_98[32];
    struct struct_0 *multiFingerTouch;
    char padding_c0[8];
    struct struct_1 *fingers;
} SuperTouchZone_Recovered;

typedef struct struct_1 {
    char padding_0[24];
    int field_18;
} struct_1;

typedef struct struct_9 {
    char padding_0[40];
    struct struct_7 *field_28;
    struct struct_8 *field_30;
} struct_9;

typedef struct struct_7 {
    char padding_0[164];
    unsigned int field_a4;
} struct_7;

typedef struct struct_8 {
    char padding_0[164];
    unsigned int field_a4;
} struct_8;

typedef struct struct_0 {
    char padding_0[24];
    int field_18;
} struct_0;

typedef struct struct_5 {
    char padding_0[24];
    struct struct_3 *field_18;
    struct struct_6 *field_20;
} struct_5;

typedef struct struct_3 {
    char padding_0[164];
    unsigned int field_a4;
} struct_3;

typedef struct struct_4 {
    char padding_0[164];
    unsigned int field_a4;
} struct_4;

typedef struct struct_6 {
    char padding_0[164];
    unsigned int field_a4;
} struct_6;

void SuperTouchZone_SetTouchSmoothing(struct_2 *ptr)
{
    struct_1 *p;  // x8
    unsigned int v1;  // s1
    struct_0 *addr;  // x8
    int v11;  // w9
    int v12;  // w10
    struct_5 *pos;  // x11
    unsigned int v3;  // s0
    unsigned long v4;  // 4142
    unsigned int v5;  // s0
    int v6;  // w9
    unsigned int v7;  // s0
    int i;  // w10
    struct_9 *index;  // x11

    p = ptr->field_c8;
    v1 = [D] unsupported_Iop_ZeroHI96ofV128();
    v4 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v3, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v3, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v3, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v3, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v3, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v3, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if ((char)v4)
        v5 = v1;
    else
        v5 = 0;
    ptr->field_94 = v5;
    if (p)
    {
        v6 = p->field_18;
        v7 = v5 * 1036831949;
        if (v6 >= 1)
        {
            i = 0;
            do
            {
                if (v6 <= i)
                    sub_f7db7c(ptr);
                index = *((long long *)&p[1].padding_0[4 + 8 * i]);
                if (!index)
                    sub_f7db7c(sub_f7db74());
                if (!index->field_28)
                    sub_f7db7c(sub_f7db74());
                index->field_28->field_a4 = v7;
                if (!index->field_30)
                    sub_f7db7c(sub_f7db74());
                i += 1;
                index->field_30->field_a4 = v7;
            } while (i < v6);
        }
        addr = ptr->field_b8;
        if (addr)
        {
            v11 = addr->field_18;
            if (v11 < 1)
                return;
            v12 = 0;
            while (true)
            {
                if (v11 <= v12)
                    sub_f7db7c(ptr);
                pos = *((long long *)&addr[1].padding_0[4 + 8 * v12]);
                if (!pos || !pos->field_18 || !((pos->field_18->field_a4 = v7, pos->field_20)))
                    break;
                v12 += 1;
                pos->field_20->field_a4 = v7;
                if (v12 >= v11)
                    return;
            }
        }
    }
    sub_f7db7c(sub_f7db74());
}
```

## `SuperTouchZone.ResetControl` — RVA `0xc49a1c`

- Decompiled symbol: `SuperTouchZone_ResetControl`
- Metadata signature: `public override void ResetControl() { }`
- Native interval: `220` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[680];
    struct struct_1 *field_2a8;
    unsigned long long field_2b0;
} struct_0;

typedef struct struct_1 {
    unsigned long long field_0;
} struct_1;

void SuperTouchZone_ResetControl(struct_0 **a0)
{
    unsigned long long v3;  // x30
    unsigned long long v4;  // x20
    unsigned long long v5;  // x19
    unsigned long long v6;  // x1
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x10]
    unsigned long long v2;  // [bp-0x8]

    v0 = v3;
    v1 = v4;
    v2 = v5;
    v6 = *(a0)->field_2b0;
    *(a0)->field_2a8();
}
```

## `SuperTouchZone.GetMultiFingerTouch` — RVA `0xc49b80`

- Decompiled symbol: `SuperTouchZone_GetMultiFingerTouch`
- Metadata signature: `protected SuperTouchZone.MultiFingerTouch GetMultiFingerTouch(int fingerCount) { }`
- Native interval: `72` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[184];
    unsigned long long field_b8;
} struct_0;

unsigned long long SuperTouchZone_GetMultiFingerTouch(struct_0 *ptr, int a1)
{
    unsigned long long v0;  // x9

    if (a1 < 1)
        return 0;
    v0 = ptr->field_b8;
    if (!v0)
    {
        ptr = sub_f7db74();
    }
    else if (a1 > *((int *)(v0 + 24)))
    {
        return 0;
    }
    else if (*((int *)(v0 + 24)) > a1 - 1)
    {
        return *((long long *)(v0 + (a1 - 1) * 8 + 32));
    }
    sub_f7db7c(ptr);
}
```

## `SuperTouchZone.JustPressedRaw` — RVA `0xc49bc8`

- Decompiled symbol: `SuperTouchZone_JustPressedRaw`
- Metadata signature: `public bool JustPressedRaw(int fingerCount) { }`
- Native interval: `44` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[184];
    unsigned long long field_b8;
} struct_0;

long long SuperTouchZone_JustPressedRaw(void)
{
    struct_0 *v0;  // x0
    int v1;  // w1
    struct_0 *v2;  // x0
    unsigned long v3;  // x0

    v2 = SuperTouchZone__GetMultiFingerTouch(v0, v1);
    if (!v2)
        return 0;
    if (*((long long *)&v2->padding_0[24]))
    {
        v3 = TouchGestureBasicState__JustPressedRaw(*((long long *)&v2->padding_0[24]), 0);
        return TouchGestureBasicState__JustPressedRaw(*((long long *)&v2->padding_0[24]), 0);
    }
    sub_f7db74(0);
}
```

## `SuperTouchZone.JustReleasedRaw` — RVA `0xc49bf4`

- Decompiled symbol: `SuperTouchZone_JustReleasedRaw`
- Metadata signature: `public bool JustReleasedRaw(int fingerCount) { }`
- Native interval: `44` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[184];
    unsigned long long field_b8;
} struct_0;

long long SuperTouchZone_JustReleasedRaw(void)
{
    struct_0 *v0;  // x0
    int v1;  // w1
    struct_0 *v2;  // x0
    unsigned long v3;  // x0

    v2 = SuperTouchZone__GetMultiFingerTouch(v0, v1);
    if (!v2)
        return 0;
    if (*((long long *)&v2->padding_0[24]))
    {
        v3 = TouchGestureBasicState__JustReleasedRaw(*((long long *)&v2->padding_0[24]), 0);
        return TouchGestureBasicState__JustReleasedRaw(*((long long *)&v2->padding_0[24]), 0);
    }
    sub_f7db74(0);
}
```

## `SuperTouchZone.JustPressedNormal` — RVA `0xc49c20`

- Decompiled symbol: `SuperTouchZone_JustPressedNormal`
- Metadata signature: `public bool JustPressedNormal(int fingerCount) { }`
- Native interval: `44` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[184];
    unsigned long long field_b8;
} struct_0;

unsigned long long SuperTouchZone_JustPressedNormal(void)
{
    struct_0 *v0;  // x0
    int v1;  // w1
    struct_0 *v2;  // x0
    unsigned long long v3;  // x0

    v2 = SuperTouchZone__GetMultiFingerTouch(v0, v1);
    if (!v2)
        return 0;
    if (*((long long *)&v2->padding_0[24]))
    {
        v3 = TouchGestureState__JustPressedNormal(*((long long *)&v2->padding_0[24]), 0);
        return TouchGestureState__JustPressedNormal(*((long long *)&v2->padding_0[24]), 0);
    }
    sub_f7db74(0);
}
```

## `SuperTouchZone.JustReleasedNormal` — RVA `0xc49c4c`

- Decompiled symbol: `SuperTouchZone_JustReleasedNormal`
- Metadata signature: `public bool JustReleasedNormal(int fingerCount) { }`
- Native interval: `44` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[184];
    unsigned long long field_b8;
} struct_0;

unsigned long long SuperTouchZone_JustReleasedNormal(void)
{
    struct_0 *v0;  // x0
    int v1;  // w1
    struct_0 *v2;  // x0
    unsigned long long v3;  // x0

    v2 = SuperTouchZone__GetMultiFingerTouch(v0, v1);
    if (!v2)
        return 0;
    if (*((long long *)&v2->padding_0[24]))
    {
        v3 = TouchGestureState__JustReleasedNormal(*((long long *)&v2->padding_0[24]), 0);
        return TouchGestureState__JustReleasedNormal(*((long long *)&v2->padding_0[24]), 0);
    }
    sub_f7db74(0);
}
```

## `SuperTouchZone.JustPressedLong` — RVA `0xc49c78`

- Decompiled symbol: `SuperTouchZone_JustPressedLong`
- Metadata signature: `public bool JustPressedLong(int fingerCount) { }`
- Native interval: `44` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[184];
    unsigned long long field_b8;
} struct_0;

unsigned long long SuperTouchZone_JustPressedLong(void)
{
    struct_0 *v0;  // x0
    int v1;  // w1
    struct_0 *v2;  // x0
    unsigned long long v3;  // x0

    v2 = SuperTouchZone__GetMultiFingerTouch(v0, v1);
    if (!v2)
        return 0;
    if (*((long long *)&v2->padding_0[24]))
    {
        v3 = TouchGestureState__JustPressedLong(*((long long *)&v2->padding_0[24]), 0);
        return TouchGestureState__JustPressedLong(*((long long *)&v2->padding_0[24]), 0);
    }
    sub_f7db74(0);
}
```

## `SuperTouchZone.JustReleasedLong` — RVA `0xc49ca4`

- Decompiled symbol: `SuperTouchZone_JustReleasedLong`
- Metadata signature: `public bool JustReleasedLong(int fingerCount) { }`
- Native interval: `44` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[184];
    unsigned long long field_b8;
} struct_0;

unsigned long long SuperTouchZone_JustReleasedLong(void)
{
    struct_0 *v0;  // x0
    int v1;  // w1
    struct_0 *v2;  // x0
    unsigned long long v3;  // x0

    v2 = SuperTouchZone__GetMultiFingerTouch(v0, v1);
    if (!v2)
        return 0;
    if (*((long long *)&v2->padding_0[24]))
    {
        v3 = TouchGestureState__JustReleasedLong(*((long long *)&v2->padding_0[24]), 0);
        return TouchGestureState__JustReleasedLong(*((long long *)&v2->padding_0[24]), 0);
    }
    sub_f7db74(0);
}
```

## `SuperTouchZone.SwipeActive` — RVA `0xc49cd0`

- Decompiled symbol: `SuperTouchZone_SwipeActive`
- Metadata signature: `public bool SwipeActive(int fingerCount) { }`
- Native interval: `44` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[32];
    struct struct_0 *field_20;
} struct_1;

typedef struct struct_0 {
    char padding_0[184];
    unsigned long long field_b8;
} struct_0;

typedef struct struct_2 {
    char padding_0[288];
    char field_120;
} struct_2;

typedef struct struct_0 {
    char padding_0[288];
    char field_120;
} struct_0;

struct_1 * SuperTouchZone_SwipeActive(void)
{
    struct_0 *v0;  // x0
    int v1;  // w1
    struct_1 *v2;  // x0

    v2 = SuperTouchZone__GetMultiFingerTouch(v0, v1);
    if (!v2)
        return v2;
    if (v2->field_20)
    {
        if (!v2->field_20->field_120)
            return NULL;
        return 0x1;
    }
    sub_f7db74();
}
```

## `SuperTouchZone.SwipeJustActivated` — RVA `0xc49cfc`

- Decompiled symbol: `SuperTouchZone_SwipeJustActivated`
- Metadata signature: `public bool SwipeJustActivated(int fingerCount) { }`
- Native interval: `44` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[32];
    struct struct_0 *field_20;
} struct_1;

typedef struct struct_0 {
    char padding_0[184];
    unsigned long long field_b8;
} struct_0;

typedef struct struct_2 {
    char padding_0[289];
    char field_121;
} struct_2;

typedef struct struct_0 {
    char padding_0[289];
    char field_121;
} struct_0;

struct_1 * SuperTouchZone_SwipeJustActivated(void)
{
    struct_0 *v0;  // x0
    int v1;  // w1
    struct_1 *v2;  // x0

    v2 = SuperTouchZone__GetMultiFingerTouch(v0, v1);
    if (!v2)
        return v2;
    if (v2->field_20)
    {
        if (!v2->field_20->field_121)
            return NULL;
        return 0x1;
    }
    sub_f7db74();
}
```

## `SuperTouchZone.GetCurPos` — RVA `0xc49d28`

- Decompiled symbol: `SuperTouchZone_GetCurPos`
- Metadata signature: `public Vector2 GetCurPos(int fingerCount) { }`
- Native interval: `104` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

extern long long g_1ef22b8;
extern char g_1fab1e0;

struct_0 * SuperTouchZone_GetCurPos(void)
{
    struct_0 *v0;  // x0
    int v1;  // w1
    struct_0 *v2;  // x0

    v2 = SuperTouchZone__GetMultiFingerTouch(v0, v1);
    if (v2)
    {
        if (v2->field_18)
            return v2;
        sub_f7db74();
    }
    else
    {
        if (!g_1fab1e0)
        {
            v2 = sub_f7d92c(&g_1ef22b8);
            g_1fab1e0 = 1;
        }
        return v2;
    }
}
```

## `SuperTouchZone.GetStartPos` — RVA `0xc49d90`

- Decompiled symbol: `SuperTouchZone_GetStartPos`
- Metadata signature: `public Vector2 GetStartPos(int fingerCount) { }`
- Native interval: `104` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

extern long long g_1ef22b8;
extern char g_1fab1e0;

struct_0 * SuperTouchZone_GetStartPos(void)
{
    struct_0 *v0;  // x0
    int v1;  // w1
    struct_0 *v2;  // x0

    v2 = SuperTouchZone__GetMultiFingerTouch(v0, v1);
    if (v2)
    {
        if (v2->field_18)
            return v2;
        sub_f7db74();
    }
    else
    {
        if (!g_1fab1e0)
        {
            v2 = sub_f7d92c(&g_1ef22b8);
            g_1fab1e0 = 1;
        }
        return v2;
    }
}
```

## `SuperTouchZone.GetTapPos` — RVA `0xc49df8`

- Decompiled symbol: `SuperTouchZone_GetTapPos`
- Metadata signature: `public Vector2 GetTapPos(int fingerCount) { }`
- Native interval: `104` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

extern long long g_1ef22b8;
extern char g_1fab1e0;

struct_0 * SuperTouchZone_GetTapPos(void)
{
    struct_0 *v0;  // x0
    int v1;  // w1
    struct_0 *v2;  // x0

    v2 = SuperTouchZone__GetMultiFingerTouch(v0, v1);
    if (v2)
    {
        if (v2->field_18)
            return v2;
        sub_f7db74();
    }
    else
    {
        if (!g_1fab1e0)
        {
            v2 = sub_f7d92c(&g_1ef22b8);
            g_1fab1e0 = 1;
        }
        return v2;
    }
}
```

## `SuperTouchZone.GetRawSwipeVector` — RVA `0xc49e60`

- Decompiled symbol: `SuperTouchZone_GetRawSwipeVector`
- Metadata signature: `public Vector2 GetRawSwipeVector(int fingerCount) { }`
- Native interval: `96` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[32];
    long long field_20;
} struct_0;

extern long long g_1ef22b8;
extern char g_1fab1e0;

struct_0 * SuperTouchZone_GetRawSwipeVector(void)
{
    struct_0 *v0;  // x0
    int v1;  // w1
    struct_0 *v2;  // x0
    unsigned long long v3;  // x0

    v2 = SuperTouchZone__GetMultiFingerTouch(v0, v1);
    if (v2)
    {
        if (v2->field_20)
        {
            v3 = TouchGestureBasicState__GetSwipeVecRaw(v2->field_20, 0);
            return TouchGestureBasicState__GetSwipeVecRaw(v2->field_20, 0);
        }
        sub_f7db74(0);
    }
    else
    {
        if (!g_1fab1e0)
        {
            v2 = sub_f7d92c(&g_1ef22b8);
            g_1fab1e0 = 1;
        }
        return v2;
    }
}
```

## `SuperTouchZone.GetRawSwipeDelta` — RVA `0xc49ec0`

- Decompiled symbol: `SuperTouchZone_GetRawSwipeDelta`
- Metadata signature: `public Vector2 GetRawSwipeDelta(int fingerCount) { }`
- Native interval: `96` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[32];
    long long field_20;
} struct_0;

extern long long g_1ef22b8;
extern char g_1fab1e0;

struct_0 * SuperTouchZone_GetRawSwipeDelta(void)
{
    struct_0 *v0;  // x0
    int v1;  // w1
    struct_0 *v2;  // x0
    unsigned long long v3;  // x0

    v2 = SuperTouchZone__GetMultiFingerTouch(v0, v1);
    if (v2)
    {
        if (v2->field_20)
        {
            v3 = TouchGestureBasicState__GetDeltaVecRaw(v2->field_20, 0);
            return TouchGestureBasicState__GetDeltaVecRaw(v2->field_20, 0);
        }
        sub_f7db74(0);
    }
    else
    {
        if (!g_1fab1e0)
        {
            v2 = sub_f7d92c(&g_1ef22b8);
            g_1fab1e0 = 1;
        }
        return v2;
    }
}
```

## `SuperTouchZone.GetUnconstrainedSwipeVector` — RVA `0xc49f20`

- Decompiled symbol: `SuperTouchZone_GetUnconstrainedSwipeVector`
- Metadata signature: `public Vector2 GetUnconstrainedSwipeVector(int fingerCount) { }`
- Native interval: `96` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[32];
    long long field_20;
} struct_0;

extern long long g_1ef22b8;
extern char g_1fab1e0;

struct_0 * SuperTouchZone_GetUnconstrainedSwipeVector(void)
{
    struct_0 *v0;  // x0
    int v1;  // w1
    struct_0 *v2;  // x0
    unsigned long long v3;  // x0

    v2 = SuperTouchZone__GetMultiFingerTouch(v0, v1);
    if (v2)
    {
        if (v2->field_20)
        {
            v3 = TouchGestureBasicState__GetSwipeVecSmooth(v2->field_20, 0);
            return TouchGestureBasicState__GetSwipeVecSmooth(v2->field_20, 0);
        }
        sub_f7db74(0);
    }
    else
    {
        if (!g_1fab1e0)
        {
            v2 = sub_f7d92c(&g_1ef22b8);
            g_1fab1e0 = 1;
        }
        return v2;
    }
}
```

## `SuperTouchZone.GetUnconstrainedSwipeDelta` — RVA `0xc49f80`

- Decompiled symbol: `SuperTouchZone_GetUnconstrainedSwipeDelta`
- Metadata signature: `public Vector2 GetUnconstrainedSwipeDelta(int fingerCount) { }`
- Native interval: `96` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[32];
    long long field_20;
} struct_0;

extern long long g_1ef22b8;
extern char g_1fab1e0;

struct_0 * SuperTouchZone_GetUnconstrainedSwipeDelta(void)
{
    struct_0 *v0;  // x0
    int v1;  // w1
    struct_0 *v2;  // x0
    unsigned long long v3;  // x0

    v2 = SuperTouchZone__GetMultiFingerTouch(v0, v1);
    if (v2)
    {
        if (v2->field_20)
        {
            v3 = TouchGestureBasicState__GetDeltaVecSmooth(v2->field_20, 0);
            return TouchGestureBasicState__GetDeltaVecSmooth(v2->field_20, 0);
        }
        sub_f7db74(0);
    }
    else
    {
        if (!g_1fab1e0)
        {
            v2 = sub_f7d92c(&g_1ef22b8);
            g_1fab1e0 = 1;
        }
        return v2;
    }
}
```

## `SuperTouchZone.GetSwipeVector` — RVA `0xc49fe0`

- Decompiled symbol: `SuperTouchZone_GetSwipeVector`
- Metadata signature: `public Vector2 GetSwipeVector(int fingerCount) { }`
- Native interval: `104` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[32];
    unsigned long long field_20;
} struct_0;

extern long long g_1ef22b8;
extern char g_1fab1e0;

struct_0 * SuperTouchZone_GetSwipeVector(void)
{
    struct_0 *v0;  // x0
    int v1;  // w1
    struct_0 *v2;  // x0

    v2 = SuperTouchZone__GetMultiFingerTouch(v0, v1);
    if (v2)
    {
        if (v2->field_20)
            return v2;
        sub_f7db74();
    }
    else
    {
        if (!g_1fab1e0)
        {
            v2 = sub_f7d92c(&g_1ef22b8);
            g_1fab1e0 = 1;
        }
        return v2;
    }
}
```

## `SuperTouchZone.GetSwipeDelta` — RVA `0xc4a048`

- Decompiled symbol: `SuperTouchZone_GetSwipeDelta`
- Metadata signature: `public Vector2 GetSwipeDelta(int fingerCount) { }`
- Native interval: `96` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[32];
    long long field_20;
} struct_0;

extern long long g_1ef22b8;
extern char g_1fab1e0;

struct_0 * SuperTouchZone_GetSwipeDelta(void)
{
    struct_0 *v0;  // x0
    int v1;  // w1
    struct_0 *v2;  // x0
    unsigned long long v3;  // x0

    v2 = SuperTouchZone__GetMultiFingerTouch(v0, v1);
    if (v2)
    {
        if (v2->field_20)
        {
            v3 = TouchGestureState__GetConstrainedDeltaVec(v2->field_20, 0);
            return TouchGestureState__GetConstrainedDeltaVec(v2->field_20, 0);
        }
        sub_f7db74(0);
    }
    else
    {
        if (!g_1fab1e0)
        {
            v2 = sub_f7d92c(&g_1ef22b8);
            g_1fab1e0 = 1;
        }
        return v2;
    }
}
```

## `SuperTouchZone.GetSwipeDir` — RVA `0xc4a0a8`

- Decompiled symbol: `SuperTouchZone_GetSwipeDir`
- Metadata signature: `public Dir GetSwipeDir(int fingerCount) { }`
- Native interval: `44` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    char padding_0[32];
    struct struct_1 *field_20;
} struct_2;

typedef struct struct_0 {
    char padding_0[184];
    unsigned long long field_b8;
} struct_0;

typedef struct struct_1 {
    char padding_0[312];
    struct struct_0 *field_138;
} struct_1;

typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

struct_2 * SuperTouchZone_GetSwipeDir(void)
{
    struct_0 *v0;  // x0
    int v1;  // w1
    struct_2 *v2;  // x0

    v2 = SuperTouchZone__GetMultiFingerTouch(v0, v1);
    if (!v2)
        return v2;
    if (v2->field_20 && v2->field_20->field_138)
        return v2->field_20->field_138->field_10;
    sub_f7db74();
}
```

## `SuperTouchZone.GetScroll` — RVA `0xc4a0d4`

- Decompiled symbol: `SuperTouchZone_GetScroll`
- Metadata signature: `public Vector2 GetScroll(int fingerCount) { }`
- Native interval: `104` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[32];
    unsigned long long field_20;
} struct_0;

extern long long g_1ef22b8;
extern char g_1fab1e0;

struct_0 * SuperTouchZone_GetScroll(void)
{
    struct_0 *v0;  // x0
    int v1;  // w1
    struct_0 *v2;  // x0

    v2 = SuperTouchZone__GetMultiFingerTouch(v0, v1);
    if (v2)
    {
        if (v2->field_20)
            return v2;
        sub_f7db74();
    }
    else
    {
        if (!g_1fab1e0)
        {
            v2 = sub_f7d92c(&g_1ef22b8);
            g_1fab1e0 = 1;
        }
        return v2;
    }
}
```

## `SuperTouchZone.PinchActive` — RVA `0xc4a13c`

- Decompiled symbol: `SuperTouchZone_PinchActive`
- Metadata signature: `public bool PinchActive() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[232];
    char field_e8;
} struct_0;

long long SuperTouchZone_PinchActive(struct_0 *a0)
{
    return a0->field_e8;
}
```

## `SuperTouchZone.PinchJustActivated` — RVA `0xc4a144`

- Decompiled symbol: `SuperTouchZone_PinchJustActivated`
- Metadata signature: `public bool PinchJustActivated() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[233];
    char field_e9;
} struct_0;

long long SuperTouchZone_PinchJustActivated(struct_0 *a0)
{
    return a0->field_e9;
}
```

## `SuperTouchZone.GetPinchScale` — RVA `0xc4a14c`

- Decompiled symbol: `SuperTouchZone_GetPinchScale`
- Metadata signature: `public float GetPinchScale() { }`
- Native interval: `12` bytes
- Result: `pseudocode`

```c
long long SuperTouchZone_GetPinchScale(unsigned long a0)
{
    return a0;
}
```

## `SuperTouchZone.GetPinchScaleDelta` — RVA `0xc4a158`

- Decompiled symbol: `SuperTouchZone_GetPinchScaleDelta`
- Metadata signature: `public float GetPinchScaleDelta() { }`
- Native interval: `12` bytes
- Result: `pseudocode`

```c
long long SuperTouchZone_GetPinchScaleDelta(unsigned long a0)
{
    return a0;
}
```

## `SuperTouchZone.GetPinchDist` — RVA `0xc4a164`

- Decompiled symbol: `SuperTouchZone_GetPinchDist`
- Metadata signature: `public float GetPinchDist() { }`
- Native interval: `12` bytes
- Result: `pseudocode`

```c
long long SuperTouchZone_GetPinchDist(unsigned long a0)
{
    return a0;
}
```

## `SuperTouchZone.GetPinchDistDelta` — RVA `0xc4a170`

- Decompiled symbol: `SuperTouchZone_GetPinchDistDelta`
- Metadata signature: `public float GetPinchDistDelta() { }`
- Native interval: `12` bytes
- Result: `pseudocode`

```c
long long SuperTouchZone_GetPinchDistDelta(unsigned long a0)
{
    return a0;
}
```

## `SuperTouchZone.TwistActive` — RVA `0xc4a17c`

- Decompiled symbol: `SuperTouchZone_TwistActive`
- Metadata signature: `public bool TwistActive() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[234];
    char field_ea;
} struct_0;

long long SuperTouchZone_TwistActive(struct_0 *a0)
{
    return a0->field_ea;
}
```

## `SuperTouchZone.TwistJustActivated` — RVA `0xc4a184`

- Decompiled symbol: `SuperTouchZone_TwistJustActivated`
- Metadata signature: `public bool TwistJustActivated() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[235];
    char field_eb;
} struct_0;

long long SuperTouchZone_TwistJustActivated(struct_0 *a0)
{
    return a0->field_eb;
}
```

## `SuperTouchZone.GetTwist` — RVA `0xc4a18c`

- Decompiled symbol: `SuperTouchZone_GetTwist`
- Metadata signature: `public float GetTwist() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long SuperTouchZone_GetTwist(unsigned long a0)
{
    return a0;
}
```

## `SuperTouchZone.GetTwistDelta` — RVA `0xc4a194`

- Decompiled symbol: `SuperTouchZone_GetTwistDelta`
- Metadata signature: `public float GetTwistDelta() { }`
- Native interval: `16` bytes
- Result: `pseudocode`

```c
long long SuperTouchZone_GetTwistDelta(unsigned long a0)
{
    return a0;
}
```

## `SuperTouchZone.GetTwistScrollDelta` — RVA `0xc4a1a4`

- Decompiled symbol: `SuperTouchZone_GetTwistScrollDelta`
- Metadata signature: `public int GetTwistScrollDelta() { }`
- Native interval: `16` bytes
- Result: `pseudocode`

```c
int SuperTouchZone_GetTwistScrollDelta(unsigned int *a0)
{
    return a0[68] - a0[67];
}
```

## `SuperTouchZone.GetPinchScrollDelta` — RVA `0xc4a1b4`

- Decompiled symbol: `SuperTouchZone_GetPinchScrollDelta`
- Metadata signature: `public int GetPinchScrollDelta() { }`
- Native interval: `16` bytes
- Result: `pseudocode`

```c
int SuperTouchZone_GetPinchScrollDelta(unsigned int *a0)
{
    return a0[70] - a0[69];
}
```

## `SuperTouchZone.GetReleasedDuration` — RVA `0xc4a1c4`

- Decompiled symbol: `SuperTouchZone_GetReleasedDuration`
- Metadata signature: `public float GetReleasedDuration(int fingerCount) { }`
- Native interval: `44` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

struct_0 * SuperTouchZone_GetReleasedDuration(void)
{
    struct_0 *v0;  // x0
    int v1;  // w1
    struct_0 *v2;  // x0

    v2 = SuperTouchZone__GetMultiFingerTouch(v0, v1);
    if (!v2)
        return v2;
    if (v2->field_18)
        return v2;
    sub_f7db74();
}
```

## `SuperTouchZone.GetThresholds` — RVA `0xc4a1f0`

- Decompiled symbol: `SuperTouchZone_GetThresholds`
- Metadata signature: `public MultiTouchGestureThresholds GetThresholds() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[136];
    unsigned long long field_88;
} struct_0;

long long SuperTouchZone_GetThresholds(struct_0 *a0)
{
    return a0->field_88;
}
```

## `SuperTouchZone.GetAveragedFingerPos` — RVA `0xc4a1f8`

- Decompiled symbol: `SuperTouchZone_GetAveragedFingerPos`
- Metadata signature: `private Vector2 GetAveragedFingerPos(SuperTouchZone.FingerState[] fingers, int count, bool orientedSpace, bool useSmoothPos) { }`
- Native interval: `336` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    int field_18;
} struct_0;

typedef struct struct_2 {
    unsigned int field_0;
    unsigned int field_4;
} struct_2;

typedef struct struct_1 {
    char padding_0[184];
    struct struct_2 *field_b8;
} struct_1;

extern struct_1 *g_1ef22b8;
extern char g_1fab1e0;

void SuperTouchZone_GetAveragedFingerPos(unsigned long a0, struct_0 *ptr, int a2, unsigned int a3, unsigned int a4)
{
    int v0;  // w8
    int v1;  // w8
    unsigned long v10;  // x16
    unsigned long v11;  // cc_dep1
    unsigned long v12;  // 4112
    unsigned long long v13;  // x17
    unsigned long v14;  // 4105
    unsigned long v15;  // 4105
    unsigned int v16;  // s2
    unsigned int v17;  // s3
    unsigned long v18;  // 4129
    int v2;  // w8
    unsigned long v19;  // 4129
    unsigned long v20;  // 4129
    unsigned long v21;  // 4129
    unsigned int v3;  // s0
    unsigned int v4;  // s1
    int v5;  // w8
    unsigned int v6;  // s0
    unsigned int v7;  // s1
    unsigned long v8;  // 4112
    unsigned long long v9;  // x17

    if (ptr)
    {
        v0 = ptr->field_18;
        if (ptr->field_18 < a2)
            v1 = v0;
        else
            v1 = a2;
        v2 = v1;
        if (a2 < 0)
            v2 = 0;
        if (!g_1fab1e0)
        {
            a0 = sub_f7d92c(&g_1ef22b8);
            g_1fab1e0 = 1;
        }
        v3 = g_1ef22b8->field_b8->field_0;
        v4 = g_1ef22b8->field_b8->field_4;
        if (v2 < 1)
            return;
        v5 = 0;
        v6 = v3;
        v7 = v4;
        while (true)
        {
            if (ptr->field_18 == v5)
                break;
            if (!*((long long *)&ptr[1].padding_0[4 + 8 * v5]))
                goto LABEL_104a340;
            v8 = arm64g_calculate_condition(25, (unsigned long long)(a3 & 1), 0, 0);
            if ((char)v8)
                v9 = 48;
            else
                v9 = 40;
            v10 = *((long long *)(*((long long *)&ptr[1].padding_0[4 + 8 * v5]) + v9));
            if (!v10)
                goto LABEL_104a340;
            v11 = a4 & 1;
            v12 = arm64g_calculate_condition(25, (unsigned long long)(a4 & 1), 0, 0);
            if ((char)v12)
            {
                v13 = 68;
                v14 = arm64g_calculate_condition(25, v11, 0, 0);
                if (!((char)v14))
                    goto LABEL_104a2ba;
                goto LABEL_104a2b9;
            }
            else
            {
                v13 = 52;
                v15 = arm64g_calculate_condition(25, v11, 0, 0);
                if ((char)v15)
                {
LABEL_104a2b9:
                    a0 = 72;
                    goto LABEL_104a2bc;
                }
                else
                {
LABEL_104a2ba:
                    a0 = 56;
LABEL_104a2bc:
                    v16 = *((int *)(v10 + a0));
                    v17 = *((int *)(v10 + v13));
                    if (v5)
                    {
                        v18 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(v6, v17)) >> 5 & 3 | (unsigned long long)(CmpF(v6, v17) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v6, v17)) >> 5 & 3 | (unsigned long long)(CmpF(v6, v17) & 1)) & ((unsigned long long)(char)(CmpF(v6, v17)) >> 5 & 3 | (unsigned long long)(CmpF(v6, v17) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                        if (!((char)v18))
                            v6 = v17;
                        v19 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(v7, v16)) >> 5 & 3 | (unsigned long long)(CmpF(v7, v16) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v7, v16)) >> 5 & 3 | (unsigned long long)(CmpF(v7, v16) & 1)) & ((unsigned long long)(char)(CmpF(v7, v16)) >> 5 & 3 | (unsigned long long)(CmpF(v7, v16) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                        if (!((char)v19))
                            v7 = v16;
                        v20 = arm64g_calculate_condition(192, (((((unsigned long long)(char)(CmpF(v3, v17)) >> 5 & 3 | (unsigned long long)(CmpF(v3, v17) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v3, v17)) >> 5 & 3 | (unsigned long long)(CmpF(v3, v17) & 1)) & ((unsigned long long)(char)(CmpF(v3, v17)) >> 5 & 3 | (unsigned long long)(CmpF(v3, v17) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                        if ((char)v20)
                            v17 = v3;
                        v21 = arm64g_calculate_condition(192, (((((unsigned long long)(char)(CmpF(v4, v16)) >> 5 & 3 | (unsigned long long)(CmpF(v4, v16) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v4, v16)) >> 5 & 3 | (unsigned long long)(CmpF(v4, v16) & 1)) & ((unsigned long long)(char)(CmpF(v4, v16)) >> 5 & 3 | (unsigned long long)(CmpF(v4, v16) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                        if ((char)v21)
                            v16 = v4;
                    }
                    else
                    {
                        v7 = v16;
                        v6 = v17;
                    }
                    v5 += 1;
                    v3 = v17;
                    v4 = v16;
                    if (v2 == v5)
                        return;
                }
            }
        }
    }
    else
    {
LABEL_104a340:
        a0 = sub_f7db74();
    }
    sub_f7db7c(a0);
}
```

## `SuperTouchZone.StartMultiFingerTouch` — RVA `0xc4a348`

- Decompiled symbol: `SuperTouchZone_StartMultiFingerTouch`
- Metadata signature: `private void StartMultiFingerTouch(int fingerNum, SuperTouchZone.FingerState[] fingers, Vector2 startScreenPos, Vector2 startOrientedPos, bool quietMode) { }`
- Native interval: `344` bytes
- Result: `pseudocode`
- Heuristic layout hint: `SuperTouchZone_Recovered` matched 3 offsets against `SuperTouchZone` metadata (confidence 1.00).

```c
typedef struct SuperTouchZone_Recovered {
    char padding_0[184];
    struct struct_0 *multiFingerTouch;
    char padding_c0[44];
    unsigned int pinchDistQuietInitial;
    char padding_f0[12];
    unsigned int twistAngleQuietInitial;
} SuperTouchZone_Recovered;

typedef struct struct_3 {
    char padding_0[24];
    unsigned int field_18;
} struct_3;

typedef struct struct_4 {
    char padding_0[24];
    unsigned long long field_18;
    unsigned long long field_20;
    char padding_28[8];
    struct struct_2 *field_30;
} struct_4;

typedef struct struct_2 {
    char padding_0[24];
    unsigned int field_18;
} struct_2;

typedef struct struct_0 {
    char padding_0[24];
    int field_18;
} struct_0;

struct_1 * SuperTouchZone_StartMultiFingerTouch(struct_1 *ptr, unsigned int a1, long long a2, unsigned int a3)
{
    struct_3 *v0;  // x8
    unsigned long long v1;  // x24
    struct_1 *v2;  // x0
    struct_1 *v3;  // x0
    struct_4 *v4;  // x23
    struct_1 *v5;  // x0
    unsigned int v6;  // s0
    unsigned long v7;  // 4102
    unsigned long v8;  // x0

    v0 = ptr->field_b8;
    if (v0)
    {
        v1 = 0;
        v2 = ptr;
        do
        {
            v3 = v2;
            if (v0->field_18 <= (unsigned int)v1)
                return v3;
            if (v0->field_18 <= (unsigned int)v1)
                sub_f7db7c();
            v4 = *((long long *)&v0[1].padding_0[4 + 8 * v1]);
            if (!v4 || !v4->field_30)
                break;
            if (v4->field_30->field_18 == a1)
            {
                v5 = SuperTouchZone_MultiFingerTouch__Start(v4, a2, a3 & 1);
                if (!v4->field_30)
                    break;
                if (v4->field_30->field_18 == 2)
                {
                    SuperTouchZone__GetTwoFingerDist(ptr);
                    ptr->field_ec = v6;
                    v5 = SuperTouchZone__GetTwoFingerAngle(ptr);
                    ptr->field_fc = 0;
                }
            }
            else
            {
                v7 = arm64g_calculate_condition(163, (unsigned long long)v4->field_30->field_18, (unsigned long long)a1, 0);
                if (!((char)v7))
                    v5 = SuperTouchZone_MultiFingerTouch__End(v4, 1);
                else
                    v5 = SuperTouchZone_MultiFingerTouch__EndAndReport(v4);
                if (a1 < 1)
                    continue;
                if (!v4->field_30)
                    break;
                if (a1 <= v4->field_30->field_18)
                    continue;
                if (!v4->field_18 || !((TouchGestureState__CancelTap(v4->field_18, 0), v4->field_20)))
                    break;
                v5 = TouchGestureState__CancelTap(v4->field_20, 0);
            }
        } while ((v0 = (struct_3 *)ptr->field_b8, v1 += 1, v2 = v5, ptr->field_b8));
    }
    v8 = sub_f7db74();
    return sub_f7db74();
}
```

## `SuperTouchZone.GetTwoFingerDist` — RVA `0xc4a680`

- Decompiled symbol: `SuperTouchZone_GetTwoFingerDist`
- Metadata signature: `private float GetTwoFingerDist() { }`
- Native interval: `196` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: Decompiler produced no C-like text

```c
// 0x104a680: stp d9, d8, [sp, #-0x30]!
// 0x104a684: str x30, [sp, #0x10]
// 0x104a688: stp x20, x19, [sp, #0x20]
// 0x104a68c: mov w1, #2
// 0x104a690: bl #0x1049b80
// 0x104a694: fmov s8, wzr
// 0x104a698: cbz x0, #0x104a72c
// 0x104a69c: mov w1, wzr
// 0x104a6a0: mov x19, x0
// 0x104a6a4: bl #0x104bb0c
// 0x104a6a8: cbz x0, #0x104a72c
// 0x104a6ac: mov x20, x0
// 0x104a6b0: mov w1, #1
// 0x104a6b4: mov x0, x19
// 0x104a6b8: bl #0x104bb0c
// 0x104a6bc: cbz x0, #0x104a72c
// 0x104a6c0: ldr x8, [x20, #0x28]
// 0x104a6c4: cbz x8, #0x104a740
// 0x104a6c8: ldr x9, [x0, #0x28]
// 0x104a6cc: cbz x9, #0x104a740
// 0x104a6d0: adrp x19, #0x1fab000
// 0x104a6d4: ldur d8, [x8, #0x44]
// 0x104a6d8: ldrb w8, [x19, #0x243]
// 0x104a6dc: ldur d9, [x9, #0x44]
// 0x104a6e0: cbnz w8, #0x104a6f8
// 0x104a6e4: adrp x0, #0x1e8c000
// 0x104a6e8: ldr x0, [x0, #0xa60]
// 0x104a6ec: bl #0xf7d92c
// 0x104a6f0: mov w8, #1
// 0x104a6f4: strb w8, [x19, #0x243]
// 0x104a6f8: adrp x8, #0x1e8c000
// 0x104a6fc: ldr x8, [x8, #0xa60]
// 0x104a700: fsub v8.2s, v8.2s, v9.2s
// 0x104a704: ldr x0, [x8]
// 0x104a708: ldr w8, [x0, #0xe0]
// 0x104a70c: cbnz w8, #0x104a714
// 0x104a710: bl #0xf7da5c
// 0x104a714: adrp x8, #0x832000
// 0x104a718: ldr s0, [x8, #0x3b8]
// 0x104a71c: fmul v1.2s, v8.2s, v8.2s
// 0x104a720: faddp s1, v1.2s
// 0x104a724: fsqrt s1, s1
// 0x104a728: fmax s8, s1, s0
// 0x104a72c: ldp x20, x19, [sp, #0x20]
// 0x104a730: ldr x30, [sp, #0x10]
// 0x104a734: mov v0.16b, v8.16b
// 0x104a738: ldp d9, d8, [sp], #0x30
// 0x104a73c: ret
// 0x104a740: bl #0xf7db74
```

## `SuperTouchZone.GetTwoFingerAngle` — RVA `0xc4a744`

- Decompiled symbol: `SuperTouchZone_GetTwoFingerAngle`
- Metadata signature: `private float GetTwoFingerAngle(float defaultAngle) { }`
- Native interval: `380` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: Decompiler produced no C-like text

```c
// 0x104a744: stp d11, d10, [sp, #-0x40]!
// 0x104a748: stp d9, d8, [sp, #0x10]
// 0x104a74c: str x30, [sp, #0x20]
// 0x104a750: stp x20, x19, [sp, #0x30]
// 0x104a754: mov w1, #2
// 0x104a758: mov v8.16b, v0.16b
// 0x104a75c: bl #0x1049b80
// 0x104a760: cbz x0, #0x104a8a4
// 0x104a764: mov w1, wzr
// 0x104a768: mov x19, x0
// 0x104a76c: bl #0x104bb0c
// 0x104a770: cbz x0, #0x104a8a4
// 0x104a774: mov x20, x0
// 0x104a778: mov w1, #1
// 0x104a77c: mov x0, x19
// 0x104a780: bl #0x104bb0c
// 0x104a784: cbz x0, #0x104a8a4
// 0x104a788: ldr x8, [x20, #0x28]
// 0x104a78c: cbz x8, #0x104a8bc
// 0x104a790: ldr x9, [x0, #0x28]
// 0x104a794: cbz x9, #0x104a8bc
// 0x104a798: ldp s1, s0, [x8, #0x44]
// 0x104a79c: ldp s2, s3, [x9, #0x44]
// 0x104a7a0: adrp x8, #0x832000
// 0x104a7a4: ldr s4, [x8, #0x3b8]
// 0x104a7a8: fsub s10, s1, s2
// 0x104a7ac: fsub s9, s0, s3
// 0x104a7b0: fmul s0, s10, s10
// 0x104a7b4: fmul s1, s9, s9
// 0x104a7b8: fadd s11, s0, s1
// 0x104a7bc: fcmp s11, s4
// 0x104a7c0: b.ls #0x104a8a4
// 0x104a7c4: adrp x19, #0x1fab000
// 0x104a7c8: ldrb w8, [x19, #0x243]
// 0x104a7cc: cbnz w8, #0x104a7e4
// 0x104a7d0: adrp x0, #0x1e8c000
// 0x104a7d4: ldr x0, [x0, #0xa60]
// 0x104a7d8: bl #0xf7d92c
// 0x104a7dc: mov w8, #1
// 0x104a7e0: strb w8, [x19, #0x243]
// 0x104a7e4: adrp x8, #0x1e8c000
// 0x104a7e8: ldr x8, [x8, #0xa60]
// 0x104a7ec: ldr x0, [x8]
// 0x104a7f0: ldr w8, [x0, #0xe0]
// 0x104a7f4: cbnz w8, #0x104a7fc
// 0x104a7f8: bl #0xf7da5c
// 0x104a7fc: adrp x8, #0x832000
// 0x104a800: ldr s0, [x8, #0x41c]
// 0x104a804: fsqrt s1, s11
// 0x104a808: fcmp s1, s0
// 0x104a80c: b.le #0x104a81c
// 0x104a810: fdiv s0, s10, s1
// 0x104a814: fdiv s1, s9, s1
// 0x104a818: b #0x104a850
// 0x104a81c: adrp x19, #0x1fab000
// 0x104a820: ldrb w8, [x19, #0x1e0]
// 0x104a824: cbnz w8, #0x104a83c
// 0x104a828: adrp x0, #0x1e8c000
// 0x104a82c: ldr x0, [x0, #0x138]
// 0x104a830: bl #0xf7d92c
// 0x104a834: mov w8, #1
// 0x104a838: strb w8, [x19, #0x1e0]
// 0x104a83c: adrp x8, #0x1e8c000
// 0x104a840: ldr x8, [x8, #0x138]
// 0x104a844: ldr x8, [x8]
// 0x104a848: ldr x8, [x8, #0xb8]
// 0x104a84c: ldp s0, s1, [x8]
// 0x104a850: mov x0, xzr
// 0x104a854: bl #0x105929c
// 0x104a858: mov w8, #0x43b40000
// 0x104a85c: fsub s0, s0, s8
// 0x104a860: fmov s1, w8
// 0x104a864: mov w8, #-0x3c4c0000
// 0x104a868: fdiv s2, s0, s1
// 0x104a86c: fmov s3, w8
// 0x104a870: frintm s2, s2
// 0x104a874: fmul s2, s2, s3
// 0x104a878: fadd s0, s0, s2
// 0x104a87c: fmov s2, wzr
// 0x104a880: mov w8, #0x43340000
// 0x104a884: fmin s1, s0, s1
// 0x104a888: fcmp s0, #0.0
// 0x104a88c: fmov s0, w8
// 0x104a890: fcsel s1, s1, s2, pl
// 0x104a894: fadd s2, s1, s3
// 0x104a898: fcmp s1, s0
// 0x104a89c: fcsel s0, s2, s1, gt
// 0x104a8a0: fadd s8, s0, s8
// 0x104a8a4: mov v0.16b, v8.16b
// 0x104a8a8: ldp x20, x19, [sp, #0x30]
// 0x104a8ac: ldr x30, [sp, #0x20]
// 0x104a8b0: ldp d9, d8, [sp, #0x10]
// 0x104a8b4: ldp d11, d10, [sp], #0x40
// 0x104a8b8: ret
// 0x104a8bc: bl #0xf7db74
```

## `SuperTouchZone.CancelTapsOnMultiFingersOtherThan` — RVA `0xc4a9a0`

- Decompiled symbol: `SuperTouchZone_CancelTapsOnMultiFingersOtherThan`
- Metadata signature: `private void CancelTapsOnMultiFingersOtherThan(int howManyFingers) { }`
- Native interval: `152` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[184];
    struct struct_0 *field_b8;
} struct_1;

typedef struct struct_3 {
    char padding_0[24];
    unsigned int field_18;
} struct_3;

typedef struct struct_4 {
    char padding_0[24];
    unsigned long long field_18;
    unsigned long long field_20;
    char padding_28[8];
    struct struct_2 *field_30;
} struct_4;

typedef struct struct_2 {
    char padding_0[24];
    unsigned int field_18;
} struct_2;

typedef struct struct_0 {
    char padding_0[24];
    int field_18;
} struct_0;

struct_1 * SuperTouchZone_CancelTapsOnMultiFingersOtherThan(struct_1 *ptr, unsigned int a1)
{
    struct_3 *v0;  // x8
    unsigned long long v1;  // x21
    struct_1 *v2;  // x0
    struct_1 *v3;  // x0
    struct_4 *v4;  // x22
    unsigned long v5;  // x0

    v0 = ptr->field_b8;
    if (ptr->field_b8)
    {
        v1 = 0;
        v2 = ptr;
        do
        {
            v3 = v2;
            if (v0->field_18 <= (unsigned int)v1)
                return v3;
            if (v0->field_18 <= (unsigned int)v1)
                sub_f7db7c();
            v4 = *((long long *)&v0[1].padding_0[4 + 8 * v1]);
            if (!v4 || !v4->field_30)
                break;
            if (v4->field_30->field_18 == a1)
                continue;
            if (!v4->field_20 || !((TouchGestureState__CancelTap(v4->field_20, 0), v4->field_18)))
                break;
            v3 = TouchGestureState__CancelTap(v4->field_18, 0);
            v0 = ptr->field_b8;
        } while ((v1 += 1, v2 = v3, v0));
    }
    v5 = sub_f7db74();
    return sub_f7db74();
}
```

## `SuperTouchZone.OnUpdateControl` — RVA `0xc4aa38`

- Decompiled symbol: `SuperTouchZone_OnUpdateControl`
- Metadata signature: `protected override void OnUpdateControl() { }`
- Native interval: `1572` bytes
- Result: `pseudocode`

```c
typedef struct struct_13 {
    char padding_0[24];
    unsigned int field_18;
} struct_13;

typedef struct struct_18 {
    char padding_0[40];
    struct struct_19 *field_28;
} struct_18;

typedef struct struct_20 {
    char padding_0[64];
    unsigned long long field_40;
} struct_20;

typedef struct struct_3 {
    char padding_0[32];
    struct struct_1 *field_20;
} struct_3;

typedef struct struct_15 {
    char padding_0[24];
    unsigned int field_18;
} struct_15;

typedef struct struct_16 {
    char padding_0[24];
    struct struct_17 *field_18;
    char padding_20[16];
    unsigned long long field_30;
    char padding_38[20];
    unsigned int field_4c;
    unsigned int field_50;
    unsigned int field_54;
    unsigned int field_58;
} struct_16;

typedef struct struct_11 {
    char padding_0[16];
    char field_10;
} struct_11;

typedef struct struct_10 {
    char padding_0[40];
    unsigned long long field_28;
} struct_10;

typedef struct struct_12 {
    char padding_0[16];
    char field_10;
} struct_12;

typedef struct struct_14 {
    char padding_0[16];
    char field_10;
} struct_14;

typedef struct struct_19 {
    char padding_0[16];
    char field_10;
    char padding_11[11];
    char field_1c;
} struct_19;

typedef struct struct_1 {
    char padding_0[40];
    struct struct_2 *field_28;
} struct_1;

typedef struct struct_17 {
    char padding_0[16];
    char field_10;
    char padding_11[11];
    char field_1c;
} struct_17;

typedef struct struct_2 {
    char padding_0[16];
    char field_10;
    char padding_11[11];
    char field_1c;
} struct_2;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab23a;

char [29] SuperTouchZone_OnUpdateControl(void* ptr)
{
    char i[29];  // x0
    unsigned int v1;  // w9
    unsigned long v10;  // x0
    unsigned int v11;  // w1
    unsigned int v12;  // w8
    unsigned int v13;  // w9
    unsigned long v14;  // 4105
    unsigned int v15;  // w9
    struct_20 **v16;  // x2
    char v17;  // x8
    void* ptr4;  // x0
    struct_13 *v2;  // x8
    unsigned int v19;  // w3
    unsigned int v20;  // s1
    unsigned int v21;  // s0
    unsigned int v22;  // s0
    unsigned long v23;  // 4146
    struct_20 **v24;  // x2
    unsigned int v25;  // w1
    unsigned int v26;  // w8
    struct_15 *v27;  // x8
    unsigned long long v28;  // x21
    unsigned long long v3;  // x23
    struct_16 *p;  // x20
    unsigned int v30;  // s1
    struct_13 *v31;  // x8
    unsigned long long v32;  // x20
    struct_10 *v33;  // x8
    struct_15 *v34;  // x8
    unsigned long long v35;  // x20
    unsigned int addr[40];  // x21
    unsigned int v4;  // w21
    struct_12 *v38;  // x20
    unsigned int v39;  // s2
    unsigned int v40;  // s0
    unsigned long v41;  // 4150
    unsigned long v42;  // 4102
    struct_14 *v43;  // x20
    unsigned int v44;  // s0
    unsigned int v45;  // s1
    struct_18 *ptr3;  // x20
    unsigned long v46;  // 4133
    unsigned long v47;  // 4125
    unsigned long long v48;  // x0
    struct_20 **v6;  // x24
    unsigned long v7;  // x25
    unsigned long v8;  // x0
    struct_3 *ptr5;  // x0

    if (!(g_1fab23a & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab23a = 1;
    }
    i = (long long)ptr[488];
    if (i)
    {
        i = SuperTouchZone_EmulatedFingerSystem__Update(i, 0);
        v1 = (int)ptr[216];
        v2 = (long long)ptr[200];
        *((unsigned int *)&ptr[216]) = 0;
        *((unsigned int *)&ptr[220]) = v1;
        if (v2)
        {
            v3 = 0;
            v4 = 0;
            while (v2->field_18 > (unsigned int)v3)
            {
                if (v2->field_18 <= (unsigned int)v3)
                    goto LABEL_104b04c;
                ptr3 = *((long long *)&v2[1].padding_0[4 + 8 * v3]);
                if (!ptr3 || !((SuperTouchZone_FingerState__Update(ptr3), i = (char [29])ptr3->field_28, i)))
                    goto LABEL_104ae34;
                if (i[28])
                {
                    v6 = (long long)ptr[208];
                    if (v6)
                    {
                        v7 = (int)ptr[216];
                        if (!sub_f7da60(ptr3, *(v6)->field_40))
                            goto LABEL_104b050;
                        if ((int)v6[3] <= (unsigned int)v7)
                            goto LABEL_104b04c;
                        ptr5 = &v6[v7];
                        ptr5->field_20 = ptr3;
                        sub_f7d8d0((struct struct_3 *)&ptr5->field_20, ptr3);
                        *((unsigned int *)&ptr[216]) = (int)ptr[216] + 1;
                        if (ptr3->field_28)
                            goto LABEL_104ab30;
                        goto LABEL_104ae34;
                    }
                }
LABEL_104ab30:
                i = TouchGestureBasicState__JustReleasedRaw();
                v4 |= (unsigned int)i;
                v3 += 1;
                if (!(long long)ptr[200])
                    goto LABEL_104ae34;
            }
            v10 = (unsigned long long)SuperTouchZone__GetAveragedFingerPos(i, (long long)ptr[208], (int)ptr[216], 0, 0);
            i = (unsigned long long)SuperTouchZone__GetAveragedFingerPos(v10, (long long)ptr[208], (int)ptr[216], 1, 0);
            v11 = (int)ptr[216];
            if ((int)ptr[216] >= 1)
            {
                if (!g_1ef0c58->field_e0)
                    sub_f7da5c(g_1ef0c58);
                i = Object__op_Inequality((long long)ptr[88], 0, 0);
                if (!((char)i & 1))
                {
LABEL_104abc8:
                    v11 = (int)ptr[216];
                    goto LABEL_104abcc;
                }
                i = (long long)ptr[88];
                if (!i)
                    goto LABEL_104ae34;
                i = InputRig__WakeTouchControlsUp(i);
                goto LABEL_104abc8;
            }
LABEL_104abcc:
            if (!v11)
            {
                *((unsigned int *)&ptr[228]) = 0;
                *((char *)&ptr[224]) = 0;
            }
            if ((char)ptr[152] && (int)ptr[144] > 1)
            {
                v12 = (int)ptr[220];
                if (v11 != v12)
                    v13 = 0;
                else
                    v13 = 1;
                if (!(v13 & ~(v4) & 1))
                {
                    v14 = arm64g_calculate_condition(179, (unsigned long long)v11, (unsigned long long)v12, 0);
                    if ((char)v14)
                        v15 = 0;
                    else
                        v15 = 1;
                    if (!(v15 & ~(v4) & 1))
                    {
                        v16 = (long long)ptr[208];
                        if (v11 <= 0)
                            v17 = 0;
                        else
                            v17 = 1;
                        ptr4 = ptr;
                        v11 = 0;
                        v19 = 0;
                        *((char *)&ptr[224]) = v17;
                    }
                    else
                    {
                        if (!v12)
                        {
                            *((char *)&ptr[225]) = 1;
                            *((unsigned int *)&ptr[228]) = 0;
                        }
                        v16 = (long long)ptr[208];
                        v19 = 1;
                        ptr4 = ptr;
                    }
                    i = SuperTouchZone__StartMultiFingerTouch(ptr4, v11, v16, v19);
                }
                else
                {
                    if (v11 >= 1 && (char)ptr[225])
                    {
                        i = CFUtils__get_realDeltaTime(0);
                        v20 = (int)ptr[156];
                        v22 = (int)ptr[228] + v21;
                        *((unsigned int *)&ptr[228]) = v22;
                        v23 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v22, v20)) >> 5 & 3 | (unsigned long long)(CmpF(v22, v20) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v22, v20)) >> 5 & 3 | (unsigned long long)(CmpF(v22, v20) & 1)) & ((unsigned long long)(char)(CmpF(v22, v20)) >> 5 & 3 | (unsigned long long)(CmpF(v22, v20) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                        if (!((char)v23))
                            *((unsigned short *)&ptr[224]) = 1;
                    }
                }
            }
            else if (v11 != (int)ptr[220])
            {
                v24 = (long long)ptr[208];
                *((unsigned int *)&ptr[228]) = 0;
                i = SuperTouchZone__StartMultiFingerTouch(ptr, v11, v24, 0);
                v25 = (int)ptr[216];
                v26 = (int)ptr[220];
                *((unsigned short *)&ptr[224]) = 0;
                if (v26 > v25)
                {
                    i = SuperTouchZone__GetMultiFingerTouch(ptr, v25);
                    if (i)
                        i = SuperTouchZone_MultiFingerTouch__DisableTapUntilRelease();
                }
            }
            if ((long long)ptr[184])
            {
                v28 = 0;
                while (v27->field_18 > (unsigned int)v28)
                {
                    if (v27->field_18 <= (unsigned int)v28)
                        goto LABEL_104b04c;
                    p = *((long long *)&v27[1].padding_0[4 + 8 * v28]);
                    if (!p || !p->field_30)
                        goto LABEL_104ae34;
                    if ((int)ptr[216] == *((int *)(p->field_30 + 24)))
                    {
                        p->field_4c = v21;
                        p->field_50 = v30;
                        p->field_54 = v21;
                        p->field_58 = v30;
                    }
                    SuperTouchZone_MultiFingerTouch__Update(p);
                    i = p->field_18;
                    if (!i)
                        goto LABEL_104ae34;
                    i = TouchGestureBasicState__JustPressedRaw(i, 0);
                    if (((char)i & 1))
                    {
                        if (!p->field_30)
                            goto LABEL_104ae34;
                        i = SuperTouchZone__CancelTapsOnMultiFingersOtherThan(ptr, *((int *)(p->field_30 + 24)));
                    }
                    v28 += 1;
                    if (!(long long)ptr[184])
                        goto LABEL_104ae34;
                }
                i = SuperTouchZone__UpdateTwistAndPinch(ptr, 0);
                if (!(long long)ptr[288])
                    goto LABEL_104ae34;
                if (*((char *)((long long)ptr[288] + 16)))
                {
                    v31 = (long long)ptr[200];
                    if (!(long long)ptr[200])
                        goto LABEL_104ae34;
                    v32 = 0;
                }
                else
                {
LABEL_104adf8:
                    v34 = (long long)ptr[184];
                    if (!(long long)ptr[184])
                        goto LABEL_104ae34;
                    for (v35 = 0; v34->field_18 > (unsigned int)v35; i = *((long long *)&v34[1].padding_0[4 + 8 * v35]))
                    {
                        if (v34->field_18 <= (unsigned int)v35)
                            goto LABEL_104b04c;
                    }
                }
                while (true)
                {
                    if (v31->field_18 <= (unsigned int)v32)
                        goto LABEL_104adf8;
                    if (v31->field_18 <= (unsigned int)v32)
                        break;
                    v33 = *((long long *)&v31[1].padding_0[4 + 8 * v32]);
                }
LABEL_104b04c:
                v8 = sub_f7db7c();
LABEL_104b050:
                sub_f7da4c(sub_f7db98(v8), 0);
            }
        }
    }
    while (true)
    {
        do
        {
            do
            {
LABEL_104ae34:
                i = sub_f7db74(i);
                if (!(long long)ptr[136])
                    return i;
                i = (long long)ptr[344];
            } while (!i);
        } while ((ScrollDeltaBinding__SyncScrollDelta(i, (unsigned long long)(unsigned int)(int)ptr[280] - (unsigned long long)(unsigned int)(int)ptr[276], (long long)ptr[88], 0), i = (char [29])(long long)ptr[352], !i));
        i = ScrollDeltaBinding__SyncScrollDelta(i, (int)ptr[272] - (int)ptr[268], (long long)ptr[88], 0);
        if ((char)ptr[232])
        {
            v38 = (long long)ptr[360];
            if (!v38)
                continue;
            if (v38->field_10)
            {
                i = (long long)ptr[304];
                if (!i)
                    continue;
                AnalogConfig__GetAnalogVal(i, 0);
                AxisBinding__SyncFloat(v38, 1, (long long)ptr[88], 0);
            }
            i = (long long)ptr[368];
            if (!i)
                continue;
            if (i[16])
                i = AxisBinding__SyncFloat();
            v39 = addr[39];
            v40 = (int)ptr[244] - (int)ptr[240];
            v41 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v40, v39)) >> 5 & 3 | (unsigned long long)(CmpF(v40, v39) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v40, v39)) >> 5 & 3 | (unsigned long long)(CmpF(v40, v39) & 1)) & ((unsigned long long)(char)(CmpF(v40, v39)) >> 5 & 3 | (unsigned long long)(CmpF(v40, v39) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
            if (!((char)v41))
            {
                i = (long long)ptr[384];
                if (!i)
                    continue;
                goto LABEL_104af28;
            }
            else
            {
                v42 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v40, v39)) >> 5 & 3 | (unsigned long long)(CmpF(v40, v39) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v40, v39)) >> 5 & 3 | (unsigned long long)(CmpF(v40, v39) & 1)) & ((unsigned long long)(char)(CmpF(v40, v39)) >> 5 & 3 | (unsigned long long)(CmpF(v40, v39) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                if (!((char)v42))
                {
                    i = (long long)ptr[376];
                    if (!i)
                        continue;
LABEL_104af28:
                    i = DigitalBinding__Sync(i, 1, (long long)ptr[88], 0, 0);
                }
            }
        }
        if (!(char)ptr[234])
            return i;
        v43 = (long long)ptr[312];
        if (!v43)
            continue;
        if (v43->field_10)
        {
            i = (long long)ptr[296];
            if (!i)
                continue;
            AnalogConfig__GetAnalogVal(i, 0);
            AxisBinding__SyncFloat(v43, 1, (long long)ptr[88], 0);
        }
        i = (long long)ptr[320];
        if (!i)
            continue;
        if (i[16])
            i = AxisBinding__SyncFloat();
        v44 = (int)ptr[260];
        v45 = addr[32];
        v46 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v44, v45)) >> 5 & 3 | (unsigned long long)(CmpF(v44, v45) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v44, v45)) >> 5 & 3 | (unsigned long long)(CmpF(v44, v45) & 1)) & ((unsigned long long)(char)(CmpF(v44, v45)) >> 5 & 3 | (unsigned long long)(CmpF(v44, v45) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if (!((char)v46))
        {
            i = (long long)ptr[328];
            if (!i)
                continue;
            i = DigitalBinding__Sync(i, 1, (long long)ptr[88], 0, 0);
            v44 = (int)ptr[260];
            v45 = addr[32];
        }
        v47 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v44, v45)) >> 5 & 3 | (unsigned long long)(CmpF(v44, v45) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v44, v45)) >> 5 & 3 | (unsigned long long)(CmpF(v44, v45) & 1)) & ((unsigned long long)(char)(CmpF(v44, v45)) >> 5 & 3 | (unsigned long long)(CmpF(v44, v45) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if ((char)v47)
            return i;
        i = (long long)ptr[336];
        if (i)
            break;
    }
    v48 = DigitalBinding__Sync();
    return DigitalBinding__Sync();
}
```

## `SuperTouchZone.UpdateEmulatedFingers` — RVA `0xc4b05c`

- Decompiled symbol: `SuperTouchZone_UpdateEmulatedFingers`
- Metadata signature: `private void UpdateEmulatedFingers() { }`
- Native interval: `28` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[488];
    long long field_1e8;
} struct_0;

long long SuperTouchZone_UpdateEmulatedFingers(struct_0 *a0)
{
    unsigned long v0;  // x0

    if (a0->field_1e8)
    {
        v0 = SuperTouchZone_EmulatedFingerSystem__Update(a0->field_1e8, 0);
        return SuperTouchZone_EmulatedFingerSystem__Update(a0->field_1e8, 0);
    }
    sub_f7db74(0);
}
```

## `SuperTouchZone.UpdateTwistAndPinch` — RVA `0xc4b7ec`

- Decompiled symbol: `SuperTouchZone_UpdateTwistAndPinch`
- Metadata signature: `private void UpdateTwistAndPinch(bool lastUpdateMode) { }`
- Native interval: `732` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: Decompiler produced no C-like text

```c
// 0x104b7ec: str x30, [sp, #-0x40]!
// 0x104b7f0: stp x24, x23, [sp, #0x10]
// 0x104b7f4: stp x22, x21, [sp, #0x20]
// 0x104b7f8: stp x20, x19, [sp, #0x30]
// 0x104b7fc: tbnz w1, #0, #0x104bab0
// 0x104b800: ldr s0, [x0, #0xf4]
// 0x104b804: ldr s1, [x0, #0x104]
// 0x104b808: ldr w8, [x0, #0x110]
// 0x104b80c: ldr w9, [x0, #0x118]
// 0x104b810: ldr x24, [x0, #0x88]
// 0x104b814: mov w1, #2
// 0x104b818: mov x19, x0
// 0x104b81c: strb wzr, [x0, #0xe9]
// 0x104b820: str s0, [x0, #0xf8]
// 0x104b824: str s1, [x0, #0x108]
// 0x104b828: str w8, [x0, #0x10c]
// 0x104b82c: str w9, [x0, #0x114]
// 0x104b830: strb wzr, [x0, #0xeb]
// 0x104b834: bl #0x1049b80
// 0x104b838: cbz x0, #0x104bab0
// 0x104b83c: mov x20, x0
// 0x104b840: ldr x0, [x0, #0x18]
// 0x104b844: cbz x0, #0x104bac4
// 0x104b848: mov x1, xzr
// 0x104b84c: bl #0x1061bf0
// 0x104b850: tbz w0, #0, #0x104b87c
// 0x104b854: ldr s0, [x19, #0xec]
// 0x104b858: ldr s1, [x19, #0xfc]
// 0x104b85c: add x8, x19, #0x104
// 0x104b860: str wzr, [x19, #0xe8]
// 0x104b864: stp s0, s0, [x19, #0xf0]
// 0x104b868: str s0, [x19, #0xf8]
// 0x104b86c: str s1, [x19, #0x100]
// 0x104b870: stp xzr, xzr, [x8, #8]
// 0x104b874: str xzr, [x8]
// 0x104b878: b #0x104bab0
// 0x104b87c: ldr x8, [x20, #0x18]
// 0x104b880: cbz x8, #0x104bac4
// 0x104b884: ldrb w9, [x8, #0x1c]
// 0x104b888: cbz w9, #0x104b8f0
// 0x104b88c: ldrb w22, [x8, #0x121]
// 0x104b890: mov x0, x19
// 0x104b894: bl #0x104a680
// 0x104b898: ldrb w8, [x19, #0xe8]
// 0x104b89c: str s0, [x19, #0xf4]
// 0x104b8a0: cbnz w8, #0x104b8c4
// 0x104b8a4: cbz x24, #0x104bac4
// 0x104b8a8: ldr s1, [x19, #0xf0]
// 0x104b8ac: ldr s2, [x24, #0x90]
// 0x104b8b0: fabd s0, s1, s0
// 0x104b8b4: fcmp s0, s2
// 0x104b8b8: b.le #0x104b8c4
// 0x104b8bc: mov w21, #1
// 0x104b8c0: b #0x104b8c8
// 0x104b8c4: mov w21, wzr
// 0x104b8c8: ldr s0, [x19, #0x104]
// 0x104b8cc: mov x0, x19
// 0x104b8d0: bl #0x104a744
// 0x104b8d4: ldr s1, [x19, #0x100]
// 0x104b8d8: ldrb w8, [x19, #0xea]
// 0x104b8dc: fsub s0, s0, s1
// 0x104b8e0: str s0, [x19, #0x104]
// 0x104b8e4: cbz w8, #0x104b908
// 0x104b8e8: cbnz x24, #0x104b934
// 0x104b8ec: b #0x104bac4
// 0x104b8f0: ldr s0, [x19, #0xf4]
// 0x104b8f4: ldr s1, [x19, #0x104]
// 0x104b8f8: str wzr, [x19, #0xe8]
// 0x104b8fc: str s0, [x19, #0xf0]
// 0x104b900: str s1, [x19, #0x100]
// 0x104b904: b #0x104bab0
// 0x104b908: cbz x24, #0x104bac4
// 0x104b90c: ldr s1, [x19, #0xf4]
// 0x104b910: ldr s2, [x24, #0xa4]
// 0x104b914: fcmp s1, s2
// 0x104b918: b.le #0x104b934
// 0x104b91c: ldr s1, [x24, #0x74]
// 0x104b920: fabs s0, s0
// 0x104b924: fcmp s0, s1
// 0x104b928: b.le #0x104b934
// 0x104b92c: mov w23, #1
// 0x104b930: b #0x104b938
// 0x104b934: mov w23, wzr
// 0x104b938: ldp s3, s0, [x19, #0xf0]
// 0x104b93c: ldr w0, [x19, #0x118]
// 0x104b940: ldr s1, [x24, #0xa0]
// 0x104b944: ldr s2, [x24, #0x6c]
// 0x104b948: fsub s0, s3, s0
// 0x104b94c: mov x1, xzr
// 0x104b950: bl #0x1058578
// 0x104b954: str w0, [x19, #0x118]
// 0x104b958: ldr s0, [x19, #0x104]
// 0x104b95c: ldr w0, [x19, #0x110]
// 0x104b960: ldp s1, s2, [x24, #0x84]
// 0x104b964: mov x1, xzr
// 0x104b968: bl #0x1058578
// 0x104b96c: ldrsw x8, [x19, #0xb0]
// 0x104b970: str w0, [x19, #0x110]
// 0x104b974: cmp w8, #5
// 0x104b978: b.hi #0x104b98c
// 0x104b97c: adrp x9, #0x852000
// 0x104b980: add x9, x9, #0x108
// 0x104b984: ldr w8, [x9, x8, lsl #2]
// 0x104b988: b #0x104b990
// 0x104b98c: mov w8, wzr
// 0x104b990: mov w9, wzr
// 0x104b994: mov w10, wzr
// 0x104b998: lsr w11, w8, w9
// 0x104b99c: and w11, w11, #7
// 0x104b9a0: cmp w11, #2
// 0x104b9a4: b.eq #0x104b9e0
// 0x104b9a8: cmp w11, #1
// 0x104b9ac: b.eq #0x104ba18
// 0x104b9b0: cbnz w11, #0x104ba48
// 0x104b9b4: ldrb w11, [x19, #0xea]
// 0x104b9b8: and w12, w23, #1
// 0x104b9bc: orr w11, w11, w12
// 0x104b9c0: cbz w11, #0x104ba48
// 0x104b9c4: ldrb w11, [x19, #0xa6]
// 0x104b9c8: ldrb w12, [x19, #0xa2]
// 0x104b9cc: cmp w11, #0
// 0x104b9d0: cset w11, ne
// 0x104b9d4: cmp w12, #0
// 0x104b9d8: orr w10, w10, w11
// 0x104b9dc: b #0x104ba0c
// 0x104b9e0: ldr x11, [x20, #0x18]
// 0x104b9e4: cbz x11, #0x104bac4
// 0x104b9e8: ldrb w11, [x11, #0x120]
// 0x104b9ec: orr w11, w11, w22
// 0x104b9f0: cbz w11, #0x104ba48
// 0x104b9f4: ldrb w11, [x19, #0xa3]
// 0x104b9f8: ldrb w12, [x19, #0xa1]
// 0x104b9fc: cmp w11, #0
// 0x104ba00: cset w11, eq
// 0x104ba04: cmp w12, #0
// 0x104ba08: and w23, w23, w11
// 0x104ba0c: cset w11, eq
// 0x104ba10: and w21, w21, w11
// 0x104ba14: b #0x104ba48
// 0x104ba18: ldrb w11, [x19, #0xe8]
// 0x104ba1c: and w12, w21, #1
// 0x104ba20: orr w11, w11, w12
// 0x104ba24: cbz w11, #0x104ba48
// 0x104ba28: ldrb w11, [x19, #0xa5]
// 0x104ba2c: ldrb w12, [x19, #0xa4]
// 0x104ba30: cmp w11, #0
// 0x104ba34: cset w11, ne
// 0x104ba38: cmp w12, #0
// 0x104ba3c: orr w10, w10, w11
// 0x104ba40: cset w11, eq
// 0x104ba44: and w23, w23, w11
// 0x104ba48: add w9, w9, #3
// 0x104ba4c: cmp w9, #9
// 0x104ba50: b.ne #0x104b998
// 0x104ba54: tbz w10, #0, #0x104ba7c
// 0x104ba58: ldr x0, [x20, #0x18]
// 0x104ba5c: cbz x0, #0x104bac4
// 0x104ba60: mov x1, xzr
// 0x104ba64: bl #0x10624c8
// 0x104ba68: ldr x0, [x20, #0x20]
// 0x104ba6c: cbz x0, #0x104bac4
// 0x104ba70: mov x1, xzr
// 0x104ba74: bl #0x10624c8
// 0x104ba78: b #0x104ba88
// 0x104ba7c: cbz w22, #0x104ba88
// 0x104ba80: mov x0, x19
// 0x104ba84: bl #0x104bb44
// 0x104ba88: tbz w21, #0, #0x104ba94
// 0x104ba8c: mov x0, x19
// 0x104ba90: bl #0x104bbc0
// 0x104ba94: tbz w23, #0, #0x104bab0
// 0x104ba98: mov x0, x19
// 0x104ba9c: ldp x20, x19, [sp, #0x30]
// 0x104baa0: ldp x22, x21, [sp, #0x20]
// 0x104baa4: ldp x24, x23, [sp, #0x10]
// 0x104baa8: ldr x30, [sp], #0x40
// 0x104baac: b #0x104bc04
// 0x104bab0: ldp x20, x19, [sp, #0x30]
// 0x104bab4: ldp x22, x21, [sp, #0x20]
// 0x104bab8: ldp x24, x23, [sp, #0x10]
// 0x104babc: ldr x30, [sp], #0x40
// 0x104bac0: ret
// 0x104bac4: bl #0xf7db74
```

## `SuperTouchZone.UpdateTwistAndPinch` — RVA `0xc4bb3c`

- Decompiled symbol: `SuperTouchZone_UpdateTwistAndPinch`
- Metadata signature: `private void UpdateTwistAndPinch() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[184];
    unsigned long long field_b8;
} struct_0;

long long SuperTouchZone_UpdateTwistAndPinch(void)
{
    struct_0 *v0;  // x0
    unsigned long long v1;  // x0

    v1 = SuperTouchZone__UpdateTwistAndPinch(v0, 0);
    return SuperTouchZone__UpdateTwistAndPinch(v0, 0);
}
```

## `SuperTouchZone.OnTwoFingerDragStart` — RVA `0xc4bb44`

- Decompiled symbol: `SuperTouchZone_OnTwoFingerDragStart`
- Metadata signature: `private void OnTwoFingerDragStart() { }`
- Native interval: `124` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    struct struct_0 *field_18;
    struct struct_0 *field_20;
    char padding_28[248];
    char field_120;
} struct_0;

struct_0 * SuperTouchZone_OnTwoFingerDragStart(char *a0)
{
    struct_0 *ptr;  // x0
    struct_0 *v1;  // x0
    struct_0 *v2;  // x0
    unsigned long long v3;  // x0

    ptr = SuperTouchZone__GetMultiFingerTouch(a0, 2);
    if (!ptr)
        return ptr;
    v1 = ptr->field_18;
    if (v1)
    {
        if (v1->field_120)
            return v1;
        TouchGestureState__ForceSwipe();
        v1 = ptr->field_20;
        if (v1)
        {
            v2 = TouchGestureState__ForceSwipe(v1, 0);
            if (a0[171])
                v2 = SuperTouchZone__OnTwistStart(a0);
            if (a0[168])
            {
                v3 = SuperTouchZone__OnPinchStart(a0);
                return SuperTouchZone__OnPinchStart(a0);
            }
            return v2;
        }
    }
    sub_f7db74(v1);
}
```

## `SuperTouchZone.OnPinchStart` — RVA `0xc4bbc0`

- Decompiled symbol: `SuperTouchZone_OnPinchStart`
- Metadata signature: `private void OnPinchStart() { }`
- Native interval: `68` bytes
- Result: `pseudocode`

```c
void* SuperTouchZone_OnPinchStart(void* ptr)
{
    unsigned int v0;  // w8
    void* v1;  // x0
    void* v3;  // x0
    unsigned long v4;  // x0

    if ((char)ptr[232])
        return ptr;
    v0 = (char)ptr[169];
    *((unsigned short *)&ptr[232]) = 257;
    v1 = ptr;
    if (v0)
        v1 = SuperTouchZone__OnTwoFingerDragStart(ptr);
    v3 = v1;
    if ((char)ptr[172])
    {
        v4 = SuperTouchZone__OnTwistStart(ptr);
        return SuperTouchZone__OnTwistStart(ptr);
    }
    return v3;
}
```

## `SuperTouchZone.OnTwistStart` — RVA `0xc4bc04`

- Decompiled symbol: `SuperTouchZone_OnTwistStart`
- Metadata signature: `private void OnTwistStart() { }`
- Native interval: `68` bytes
- Result: `pseudocode`

```c
void* SuperTouchZone_OnTwistStart(void* ptr)
{
    unsigned int v0;  // w8
    void* v1;  // x0
    void* v3;  // x0
    void* v4;  // x0

    if ((char)ptr[234])
        return ptr;
    v0 = (char)ptr[170];
    *((unsigned short *)&ptr[234]) = 257;
    v1 = ptr;
    if (v0)
        v1 = SuperTouchZone__OnTwoFingerDragStart(ptr);
    v3 = v1;
    if ((char)ptr[167])
    {
        v4 = SuperTouchZone__OnPinchStart(ptr);
        return SuperTouchZone__OnPinchStart(ptr);
    }
    return v3;
}
```

## `SuperTouchZone.GetFirstUnusedFinger` — RVA `0xc4bc48`

- Decompiled symbol: `SuperTouchZone_GetFirstUnusedFinger`
- Metadata signature: `private SuperTouchZone.FingerState GetFirstUnusedFinger(TouchObject newTouchObj) { }`
- Native interval: `116` bytes
- Result: `pseudocode`
- Heuristic layout hint: `SuperTouchZone_Recovered` matched 4 offsets against `SuperTouchZone` metadata (confidence 1.00).

```c
typedef struct struct_1 {
    char padding_0[24];
    unsigned long long field_18;
} struct_1;

typedef struct SuperTouchZone_Recovered {
    char padding_0[144];
    int maxFingers;
    char padding_94[4];
    char strictMultiTouch;
    char padding_99[47];
    unsigned long long fingers;
    char padding_d0[16];
    char dontAllowNewFingers;
} SuperTouchZone_Recovered;

struct_1 * SuperTouchZone_GetFirstUnusedFinger(struct_0 *ptr, unsigned long a1)
{
    unsigned long long p;  // x8
    int v2;  // w9
    int v3;  // w10
    int i;  // w10
    int v5;  // w11
    struct_1 *v6;  // x0

    if (!ptr->field_98 || !ptr->field_e0)
    {
        p = ptr->field_c8;
        if (!p)
            sub_f7db74();
        v2 = *((int *)(p + 24));
        if (ptr->field_90 < v2)
            v3 = ptr->field_90;
        else
            v3 = v2;
        i = v3;
        if (i >= 1)
        {
            v5 = 0;
            do
            {
                if (v2 == v5)
                {
                    sub_f7db7c();
                    sub_f7db74();
                }
                v6 = *((long long *)(p + v5 * 8 + 32));
                if (!v6)
                    sub_f7db74();
                if (!v6->field_18)
                    return v6;
                v5 += 1;
            } while (i != v5);
        }
    }
    return NULL;
}
```

## `SuperTouchZone.GetFingerByTouch` — RVA `0xc4bcbc`

- Decompiled symbol: `SuperTouchZone_GetFingerByTouch`
- Metadata signature: `private SuperTouchZone.FingerState GetFingerByTouch(TouchObject touchObj) { }`
- Native interval: `96` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[200];
    struct struct_0 *field_c8;
} struct_1;

typedef struct struct_0 {
    char padding_0[24];
    int field_18;
} struct_0;

unsigned long long SuperTouchZone_GetFingerByTouch(struct_1 *ptr, unsigned long long a1)
{
    struct_0 *p;  // x8
    int v1;  // w9
    int i;  // w10
    unsigned long long v3;  // x0

    if (!a1)
        return 0;
    p = ptr->field_c8;
    if (!p)
        sub_f7db74();
    v1 = p->field_18;
    if (v1 >= 1)
    {
        i = 0;
        do
        {
            if (v1 <= i)
            {
                sub_f7db7c();
                sub_f7db74();
            }
            v3 = *((long long *)&p[1].padding_0[4 + 8 * i]);
            if (!v3)
                sub_f7db74();
            if (a1 == *((long long *)(v3 + 24)))
                return v3;
            i += 1;
        } while (i < v1);
    }
    return 0;
}
```

## `SuperTouchZone.CanBeActivatedByOtherControl` — RVA `0xc4bd1c`

- Decompiled symbol: `SuperTouchZone_CanBeActivatedByOtherControl`
- Metadata signature: `public override bool CanBeActivatedByOtherControl(TouchControl c, TouchObject touchObj) { }`
- Native interval: `52` bytes
- Result: `pseudocode`
- Heuristic layout hint: `SuperTouchZone_Recovered` matched 4 offsets against `SuperTouchZone` metadata (confidence 1.00).

```c
typedef struct SuperTouchZone_Recovered {
    char padding_0[144];
    int maxFingers;
    char padding_94[4];
    char strictMultiTouch;
    char padding_99[47];
    unsigned long long fingers;
    char padding_d0[16];
    char dontAllowNewFingers;
} SuperTouchZone_Recovered;

typedef struct struct_1 {
    char padding_0[24];
    unsigned long long field_18;
} struct_1;

unsigned long long SuperTouchZone_CanBeActivatedByOtherControl(struct_0 *a0, unsigned int a1)
{
    unsigned long long v0;  // x0

    if (!((char)TouchControl__CanBeActivatedByOtherControl() & 1))
        return 0;
    if (!SuperTouchZone__GetFirstUnusedFinger(a0, a1))
        v0 = 0;
    else
        v0 = 1;
    return v0;
}
```

## `SuperTouchZone.CanBeTouchedDirectly` — RVA `0xc4bd50`

- Decompiled symbol: `SuperTouchZone_CanBeTouchedDirectly`
- Metadata signature: `public override bool CanBeTouchedDirectly(TouchObject touchObj) { }`
- Native interval: `52` bytes
- Result: `pseudocode`
- Heuristic layout hint: `SuperTouchZone_Recovered` matched 4 offsets against `SuperTouchZone` metadata (confidence 1.00).

```c
typedef struct SuperTouchZone_Recovered {
    char padding_0[144];
    int maxFingers;
    char padding_94[4];
    char strictMultiTouch;
    char padding_99[47];
    unsigned long long fingers;
    char padding_d0[16];
    char dontAllowNewFingers;
} SuperTouchZone_Recovered;

typedef struct struct_1 {
    char padding_0[24];
    unsigned long long field_18;
} struct_1;

unsigned long long SuperTouchZone_CanBeTouchedDirectly(struct_0 *a0, unsigned int a1)
{
    unsigned long long v0;  // x0

    if (!((char)TouchControl__CanBeTouchedDirectly() & 1))
        return 0;
    if (!SuperTouchZone__GetFirstUnusedFinger(a0, a1))
        v0 = 0;
    else
        v0 = 1;
    return v0;
}
```

## `SuperTouchZone.CanBeSwipedOverFromNothing` — RVA `0xc4bd84`

- Decompiled symbol: `SuperTouchZone_CanBeSwipedOverFromNothing`
- Metadata signature: `public override bool CanBeSwipedOverFromNothing(TouchObject touchObj) { }`
- Native interval: `52` bytes
- Result: `pseudocode`
- Heuristic layout hint: `SuperTouchZone_Recovered` matched 4 offsets against `SuperTouchZone` metadata (confidence 1.00).

```c
typedef struct SuperTouchZone_Recovered {
    char padding_0[144];
    int maxFingers;
    char padding_94[4];
    char strictMultiTouch;
    char padding_99[47];
    unsigned long long fingers;
    char padding_d0[16];
    char dontAllowNewFingers;
} SuperTouchZone_Recovered;

typedef struct struct_1 {
    char padding_0[24];
    unsigned long long field_18;
} struct_1;

unsigned long long SuperTouchZone_CanBeSwipedOverFromNothing(struct_0 *a0, unsigned int a1)
{
    unsigned long long v0;  // x0

    if (!((char)TouchControl__CanBeSwipedOverFromNothingDefault() & 1))
        return 0;
    if (!SuperTouchZone__GetFirstUnusedFinger(a0, a1))
        v0 = 0;
    else
        v0 = 1;
    return v0;
}
```

## `SuperTouchZone.CanBeSwipedOverFromRestrictedList` — RVA `0xc4bdb8`

- Decompiled symbol: `SuperTouchZone_CanBeSwipedOverFromRestrictedList`
- Metadata signature: `public override bool CanBeSwipedOverFromRestrictedList(TouchObject touchObj) { }`
- Native interval: `52` bytes
- Result: `pseudocode`
- Heuristic layout hint: `SuperTouchZone_Recovered` matched 4 offsets against `SuperTouchZone` metadata (confidence 1.00).

```c
typedef struct SuperTouchZone_Recovered {
    char padding_0[144];
    int maxFingers;
    char padding_94[4];
    char strictMultiTouch;
    char padding_99[47];
    unsigned long long fingers;
    char padding_d0[16];
    char dontAllowNewFingers;
} SuperTouchZone_Recovered;

typedef struct struct_1 {
    char padding_0[24];
    unsigned long long field_18;
} struct_1;

unsigned long long SuperTouchZone_CanBeSwipedOverFromRestrictedList(struct_0 *a0, unsigned int a1)
{
    unsigned long long v0;  // x0

    if (!((char)TouchControl__CanBeSwipedOverFromRestrictedListDefault() & 1))
        return 0;
    if (!SuperTouchZone__GetFirstUnusedFinger(a0, a1))
        v0 = 0;
    else
        v0 = 1;
    return v0;
}
```

## `SuperTouchZone.CanSwipeOverOthers` — RVA `0xc4bdec`

- Decompiled symbol: `SuperTouchZone_CanSwipeOverOthers`
- Metadata signature: `public override bool CanSwipeOverOthers(TouchObject touchObj) { }`
- Native interval: `80` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[40];
    unsigned int field_28;
} struct_0;

typedef struct struct_1 {
    char padding_0[32];
    unsigned int field_20;
} struct_1;

unsigned long long SuperTouchZone_CanSwipeOverOthers(struct_0 *a0, unsigned long a1)
{
    struct_1 *v0;  // x0
    unsigned long long v1;  // x0

    if (!a0->field_28)
        return 0;
    v0 = SuperTouchZone__GetFingerByTouch(a0, a1);
    if (!v0)
        return 0;
    v1 = TouchControl__CanSwipeOverOthersDefault(a0, a1, a1, v0->field_20, 0);
    return TouchControl__CanSwipeOverOthersDefault(a0, a1, a1, v0->field_20, 0);
}
```

## `SuperTouchZone.OnTouchStart` — RVA `0xc4be3c`

- Decompiled symbol: `SuperTouchZone_OnTouchStart`
- Metadata signature: `public override bool OnTouchStart(TouchObject touch, TouchControl sender, TouchControl.TouchStartType touchStartType) { }`
- Native interval: `156` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[24];
    unsigned long long field_18;
} struct_1;

typedef struct struct_0 {
    char padding_0[32];
    char field_20;
    char padding_21[455];
    long long field_1e8;
} struct_0;

struct_1 * SuperTouchZone_OnTouchStart(struct_0 *ptr, long long a1, long long a2, unsigned int a3)
{
    struct_1 *v0;  // x0
    long long v1;  // x0

    if (!ptr->field_20)
        return NULL;
    v0 = SuperTouchZone__GetFirstUnusedFinger(ptr, a1);
    if (!v0)
        return v0;
    v1 = ptr->field_1e8;
    if (v1)
    {
        if (((char)SuperTouchZone_EmulatedFingerSystem__OnSystemTouchStart(v1, a1, a2, a3, 0) & 1))
            return 0x1;
        v1 = SuperTouchZone_FingerState__OnTouchStart();
        if (!((char)v1 & 1))
        {
            return NULL;
        }
        else if (a1)
        {
            TouchObject__AddControl(a1, ptr, 0);
        }
        else
        {
            sub_f7db74(v1);
        }
        return 0x1;
    }
    sub_f7db74(v1);
}
```

## `SuperTouchZone.OnTouchEnd` — RVA `0xc4bff0`

- Decompiled symbol: `SuperTouchZone_OnTouchEnd`
- Metadata signature: `public override bool OnTouchEnd(TouchObject touch, TouchControl.TouchEndType touchEndType) { }`
- Native interval: `168` bytes
- Result: `pseudocode`
- Heuristic layout hint: `SuperTouchZone_Recovered` matched 2 offsets against `SuperTouchZone` metadata (confidence 0.67).

```c
typedef struct SuperTouchZone_Recovered {
    char padding_0[32];
    char field_20;
    char padding_21[167];
    struct struct_0 *fingers;
    char padding_d0[280];
    long long emulatedFingers;
} SuperTouchZone_Recovered;

typedef struct struct_0 {
    char padding_0[24];
    int field_18;
} struct_0;

typedef struct struct_2 {
    char padding_0[32];
    long long field_20;
} struct_2;

unsigned int SuperTouchZone_OnTouchEnd(struct_1 *ptr, unsigned long a1, unsigned long a2)
{
    long long v0;  // x0
    struct_0 *p;  // x8
    unsigned long long v2;  // x23
    int v3;  // w9
    unsigned long long v4;  // cc_dep1
    unsigned long v5;  // cc_dep2
    unsigned int v6;  // w22
    unsigned long v7;  // 4102
    unsigned long v8;  // 4102
    struct_2 *addr;  // x8

    if (!ptr->field_20)
        return 0;
    v0 = ptr->field_1e8;
    if (v0)
    {
        v0 = SuperTouchZone_EmulatedFingerSystem__OnSystemTouchEnd(v0);
        if (((char)v0 & 1))
            return 1;
        p = ptr->field_c8;
        if (ptr->field_c8)
        {
            v2 = 0;
            do
            {
                v3 = p->field_18;
                v4 = v2 & 4294967295;
                v5 = v3;
                if (v3 <= (unsigned int)v2)
                {
                    v6 = 0;
                    v7 = arm64g_calculate_condition(163, v4, v5, 0);
                    if ((char)v7)
                        return 0;
                }
                else
                {
                    v6 = 1;
                    v8 = arm64g_calculate_condition(163, v4, v5, 0);
                    if ((char)v8)
                        return 1;
                }
                if (v3 <= (unsigned int)v2)
                    sub_f7db7c(v0);
                addr = &p->padding_0[8 * v2];
                v0 = addr->field_20;
                if (!addr->field_20)
                    break;
                v0 = SuperTouchZone_FingerState__OnTouchEnd();
                if (((char)v0 & 1))
                    return v6;
                p = ptr->field_c8;
                v2 += 1;
            } while (ptr->field_c8);
        }
    }
    v0 = sub_f7db74(v0);
    sub_f7db7c(v0);
}
```

## `SuperTouchZone.OnTouchMove` — RVA `0xc4c150`

- Decompiled symbol: `SuperTouchZone_OnTouchMove`
- Metadata signature: `public override bool OnTouchMove(TouchObject touch) { }`
- Native interval: `160` bytes
- Result: `pseudocode`
- Heuristic layout hint: `SuperTouchZone_Recovered` matched 2 offsets against `SuperTouchZone` metadata (confidence 0.67).

```c
typedef struct SuperTouchZone_Recovered {
    char padding_0[32];
    char field_20;
    char padding_21[167];
    struct struct_0 *fingers;
    char padding_d0[280];
    long long emulatedFingers;
} SuperTouchZone_Recovered;

typedef struct struct_0 {
    char padding_0[24];
    int field_18;
} struct_0;

typedef struct struct_2 {
    char padding_0[32];
    long long field_20;
} struct_2;

unsigned int SuperTouchZone_OnTouchMove(struct_1 *ptr, unsigned long a1)
{
    long long v0;  // x0
    struct_0 *p;  // x8
    unsigned long long v2;  // x22
    int v3;  // w9
    unsigned long long v4;  // cc_dep1
    unsigned long v5;  // cc_dep2
    unsigned int v6;  // w21
    unsigned long v7;  // 4102
    unsigned long v8;  // 4102
    struct_2 *addr;  // x8

    if (!ptr->field_20)
        return 0;
    v0 = ptr->field_1e8;
    if (v0)
    {
        v0 = SuperTouchZone_EmulatedFingerSystem__OnSystemTouchMove(v0);
        if (((char)v0 & 1))
            return 1;
        p = ptr->field_c8;
        if (ptr->field_c8)
        {
            v2 = 0;
            do
            {
                v3 = p->field_18;
                v4 = v2 & 4294967295;
                v5 = v3;
                if (v3 <= (unsigned int)v2)
                {
                    v6 = 0;
                    v7 = arm64g_calculate_condition(163, v4, v5, 0);
                    if ((char)v7)
                        return 0;
                }
                else
                {
                    v6 = 1;
                    v8 = arm64g_calculate_condition(163, v4, v5, 0);
                    if ((char)v8)
                        return 1;
                }
                if (v3 <= (unsigned int)v2)
                    sub_f7db7c(v0);
                addr = &p->padding_0[8 * v2];
                v0 = addr->field_20;
                if (!addr->field_20)
                    break;
                v0 = SuperTouchZone_FingerState__OnTouchMove();
                if (((char)v0 & 1))
                    return v6;
                p = ptr->field_c8;
                v2 += 1;
            } while (ptr->field_c8);
        }
    }
    v0 = sub_f7db74(v0);
    sub_f7db7c(v0);
}
```

## `SuperTouchZone.OnTouchPressureChange` — RVA `0xc4c28c`

- Decompiled symbol: `SuperTouchZone_OnTouchPressureChange`
- Metadata signature: `public override bool OnTouchPressureChange(TouchObject touch) { }`
- Native interval: `120` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[200];
    struct struct_0 *field_c8;
} struct_1;

typedef struct struct_0 {
    char padding_0[24];
    int field_18;
} struct_0;

unsigned long long SuperTouchZone_OnTouchPressureChange(struct_1 *ptr, unsigned long a1)
{
    unsigned long long v1;  // x30
    struct_0 *p;  // x8
    unsigned long long v3;  // x21
    int v4;  // w22
    unsigned long long v0;  // [bp-0x30]

    v0 = v1;
    p = ptr->field_c8;
    if (ptr->field_c8)
    {
        v3 = 0;
    }
    else
    {
LABEL_104c2e4:
        sub_f7db74();
        goto LABEL_104c2e8;
    }
    while (true)
    {
        v4 = p->field_18;
        if (v4 <= (unsigned int)v3)
            break;
        if (v4 <= (unsigned int)v3)
            sub_f7db7c();
        if (!*((long long *)&p[1].padding_0[4 + 8 * v3]))
            goto LABEL_104c2e4;
        if ((SuperTouchZone_FingerState__OnTouchPressureChange() & 1))
            break;
        p = ptr->field_c8;
        v3 += 1;
        goto LABEL_104c2e4;
    }
LABEL_104c2e8:
    if (v4 > (unsigned int)v3)
        return 1;
    return 0;
}
```

## `SuperTouchZone.ReleaseAllTouches` — RVA `0xc4c374`

- Decompiled symbol: `SuperTouchZone_ReleaseAllTouches`
- Metadata signature: `public override void ReleaseAllTouches() { }`
- Native interval: `248` bytes
- Result: `pseudocode`
- Heuristic layout hint: `SuperTouchZone_Recovered` matched 4 offsets against `SuperTouchZone` metadata (confidence 0.80).

```c
typedef struct SuperTouchZone_Recovered {
    char padding_0[32];
    char field_20;
    char padding_21[151];
    struct struct_0 *multiFingerTouch;
    char padding_c0[8];
    struct struct_1 *fingers;
    char padding_d0[8];
    unsigned int rawFingersPressedCur;
    char padding_dc[268];
    long long emulatedFingers;
} SuperTouchZone_Recovered;

typedef struct struct_3 {
    char padding_0[24];
    unsigned int field_18;
} struct_3;

typedef struct struct_4 {
    char padding_0[24];
    unsigned int field_18;
} struct_4;

typedef struct struct_0 {
    char padding_0[24];
    int field_18;
} struct_0;

typedef struct struct_1 {
    char padding_0[24];
    int field_18;
} struct_1;

struct_2 * SuperTouchZone_ReleaseAllTouches(struct_2 *ptr, unsigned long a1)
{
    struct_3 *v0;  // x8
    unsigned long long v1;  // x20
    struct_2 *v2;  // x0
    struct_2 *v3;  // x0
    struct_2 *v4;  // x0
    struct_4 *v5;  // x8
    unsigned long long v6;  // x20
    unsigned int v7;  // w21
    struct_4 *v8;  // x8
    struct_2 *v9;  // x0

    if (!ptr->field_20)
        return ptr;
    v0 = ptr->field_c8;
    if (ptr->field_c8)
    {
        v1 = 0;
        v2 = ptr;
        do
        {
            v3 = v2;
            if (v0->field_18 <= (unsigned int)v1)
            {
                v5 = ptr->field_b8;
                if (ptr->field_b8)
                {
                    v6 = 4;
                    do
                    {
                        v7 = v6 - 4;
                        if (v5->field_18 > v7)
                        {
                            if (v5->field_18 <= v7)
                                sub_f7db7c(v3);
                            if (!*((long long *)&v5->padding_0[8 * v6]) || !((v3 = (struct_2 *)SuperTouchZone_MultiFingerTouch__End(*((long long *)&v5->padding_0[8 * v6]), 1), v8 = (struct_4 *)ptr->field_b8, v8)))
                                break;
                        }
                        else
                        {
                            if (ptr->field_1e8)
                            {
                                v9 = SuperTouchZone_EmulatedFingerSystem__EndMouseAndTouches(ptr->field_1e8, 1, 0);
                                ptr->field_d8 = 0;
                                return v9;
                            }
                            break;
                        }
                        if (v8->field_18 <= v7)
                            sub_f7db7c(SuperTouchZone_MultiFingerTouch__End(*((long long *)&v5->padding_0[8 * v6]), 1));
                    } while (*((long long *)&v8->padding_0[8 * v6]) && *((long long *)(*((long long *)&v8->padding_0[8 * v6]) + 112)) && (v3 = (struct_2 *)(unsigned long long)TouchObject__End(*((long long *)(*((long long *)&v8->padding_0[8 * v6]) + 112)), 1, 0), v5 = (struct_4 *)ptr->field_b8, v6 += 1, ptr->field_b8));
                }
            }
            if (v0->field_18 <= (unsigned int)v1)
                sub_f7db7c(v3);
        } while (*((long long *)&v0[1].padding_0[4 + 8 * v1]) && (v4 = (struct_2 *)(unsigned long long)SuperTouchZone_FingerState__ReleaseTouch(), v0 = (struct_3 *)ptr->field_c8, v1 += 1, v2 = (struct_2 *)(unsigned long long)SuperTouchZone_FingerState__ReleaseTouch(), ptr->field_c8));
    }
    sub_f7db7c(sub_f7db74());
}
```

## `SuperTouchZone.OnIsBoundToAxis` — RVA `0xc4c500`

- Decompiled symbol: `SuperTouchZone_OnIsBoundToAxis`
- Metadata signature: `protected override bool OnIsBoundToAxis(string axisName, InputRig rig) { }`
- Native interval: `444` bytes
- Result: `pseudocode`
- Heuristic layout hint: `SuperTouchZone_Recovered` matched 3 offsets against `SuperTouchZone` metadata (confidence 1.00).

```c
typedef struct SuperTouchZone_Recovered {
    char padding_0[144];
    int maxFingers;
    char padding_94[44];
    struct struct_2 *multiFingerConfigs;
    char padding_c8[112];
    struct SuperTouchZone_Recovered *twistAnalogBinding;
} SuperTouchZone_Recovered;

typedef struct struct_2 {
    char padding_0[24];
    unsigned int field_18;
    char padding_1c[4];
    struct struct_0 *field_20;
} struct_2;

typedef struct struct_0 {
    char padding_0[16];
    struct SuperTouchZone_Recovered *field_10;
} struct_0;

long long SuperTouchZone_OnIsBoundToAxis(struct_1 *cur, long long a1, long long a2)
{
    unsigned long long v6;  // x30
    unsigned long long v7;  // x23
    unsigned long long v8;  // x22
    unsigned long long v9;  // x21
    unsigned long long v10;  // x20
    unsigned long long v11;  // x19
    struct_2 *index;  // x8
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
    if (cur->field_90 >= 1)
    {
        index = cur->field_c0;
        if (index)
        {
            if (index->field_18 <= 0)
            {
                sub_f7db7c(cur);
            }
            else if (index->field_20)
            {
                cur = index->field_20->field_10;
                if (cur)
                    InputBindingBase__IsBoundToAxis(cur, a1, a2, 0); /* do not return */
            }
        }
    }
    else
    {
        cur = cur->field_138;
        if (cur)
            InputBindingBase__IsBoundToAxis(cur, a1, a2, 0); /* do not return */
    }
    cur = sub_f7db74(cur);
    sub_f7db7c(cur);
}
```

## `SuperTouchZone.OnIsBoundToKey` — RVA `0xc4c6bc`

- Decompiled symbol: `SuperTouchZone_OnIsBoundToKey`
- Metadata signature: `protected override bool OnIsBoundToKey(KeyCode key, InputRig rig) { }`
- Native interval: `416` bytes
- Result: `pseudocode`
- Heuristic layout hint: `SuperTouchZone_Recovered` matched 3 offsets against `SuperTouchZone` metadata (confidence 1.00).

```c
typedef struct SuperTouchZone_Recovered {
    char padding_0[144];
    int maxFingers;
    char padding_94[44];
    struct struct_2 *multiFingerConfigs;
    char padding_c8[112];
    struct SuperTouchZone_Recovered *twistAnalogBinding;
} SuperTouchZone_Recovered;

typedef struct struct_2 {
    char padding_0[24];
    unsigned int field_18;
    char padding_1c[4];
    struct struct_0 *field_20;
} struct_2;

typedef struct struct_0 {
    char padding_0[16];
    struct SuperTouchZone_Recovered *field_10;
} struct_0;

long long SuperTouchZone_OnIsBoundToKey(struct_1 *cur, unsigned int a1, long long a2)
{
    unsigned long long v6;  // x30
    unsigned long long v7;  // x23
    unsigned long long v8;  // x22
    unsigned long long v9;  // x21
    unsigned long long v10;  // x20
    unsigned long long v11;  // x19
    struct_2 *index;  // x8
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
    if (cur->field_90 >= 1)
    {
        index = cur->field_c0;
        if (index)
        {
            if (index->field_18 <= 0)
            {
                sub_f7db7c(cur);
            }
            else if (index->field_20)
            {
                cur = index->field_20->field_10;
                if (cur)
                    InputBindingBase__IsBoundToKey(cur, a1, a2, 0); /* do not return */
            }
        }
    }
    else
    {
        cur = cur->field_138;
        if (cur)
            InputBindingBase__IsBoundToKey(cur, a1, a2, 0); /* do not return */
    }
    cur = sub_f7db74(cur);
    sub_f7db7c(cur);
}
```

## `SuperTouchZone.IsUsingKeyForEmulation` — RVA `0xc4c85c`

- Decompiled symbol: `SuperTouchZone_IsUsingKeyForEmulation`
- Metadata signature: `public override bool IsUsingKeyForEmulation(KeyCode key) { }`
- Native interval: `208` bytes
- Result: `pseudocode`
- Heuristic layout hint: `SuperTouchZone_Recovered` matched 2 offsets against `SuperTouchZone` metadata (confidence 1.00).

```c
typedef struct SuperTouchZone_Recovered {
    char padding_0[392];
    char emuWithKeys;
    char padding_189[3];
    unsigned int emuKeyOneFinger;
} SuperTouchZone_Recovered;

unsigned long long SuperTouchZone_IsUsingKeyForEmulation(struct_0 *a0, unsigned int a1)
{
    if (!a0->field_188)
    {
        return 0;
    }
    else if (a0->field_18c == a1)
    {
        return 1;
    }
    else if (*((int *)&a0[1].padding_0[0]) == a1)
    {
        return 1;
    }
    else if (*((int *)&a0[1].padding_0[4]) == a1)
    {
        return 1;
    }
    else if (*((int *)&a0[1].padding_0[32]) == a1)
    {
        return 1;
    }
    else if (*((int *)&a0[1].padding_0[36]) == a1)
    {
        return 1;
    }
    else if (*((int *)&a0[1].padding_0[28]) == a1)
    {
        return 1;
    }
    else if (*((int *)&a0[1].padding_0[24]) == a1)
    {
        return 1;
    }
    else if (*((int *)&a0[1].padding_0[8]) == a1)
    {
        return 1;
    }
    else if (*((int *)&a0[1].padding_0[12]) == a1)
    {
        return 1;
    }
    else if (*((int *)&a0[1].padding_0[16]) == a1)
    {
        return 1;
    }
    else if (*((int *)&a0[1].padding_0[20]) == a1)
    {
        return 1;
    }
    else if (*((int *)&a0[1].padding_0[40]) == a1)
    {
        return 1;
    }
    else if (*((int *)&a0[1].padding_0[52]) == a1)
    {
        return 1;
    }
    else if (*((int *)&a0[1].padding_0[48]) == a1)
    {
        return 1;
    }
    else if (*((int *)&a0[1].padding_0[44]) != a1)
    {
        return 0;
    }
    else
    {
        return 1;
    }
}
```

## `SuperTouchZone.OnIsEmulatingTouches` — RVA `0xc4c92c`

- Decompiled symbol: `SuperTouchZone_OnIsEmulatingTouches`
- Metadata signature: `protected override bool OnIsEmulatingTouches() { }`
- Native interval: `168` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[288];
    long long field_120;
} struct_0;

long long SuperTouchZone_OnIsEmulatingTouches(struct_0 *a0)
{
    unsigned long long v4;  // x30
    unsigned long long v5;  // x21
    unsigned long long v6;  // x20
    unsigned long long v7;  // x19
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x18]
    unsigned long long v2;  // [bp-0x10]
    unsigned long long v3;  // [bp-0x8]

    v0 = v4;
    v1 = v5;
    v2 = v6;
    v3 = v7;
    if (a0->field_120)
        InputBindingBase__IsEmulatingTouches(a0->field_120, 0); /* do not return */
    sub_f7db7c(sub_f7db74(0));
}
```

## `SuperTouchZone.OnIsEmulatingMousePosition` — RVA `0xc4c9d4`

- Decompiled symbol: `SuperTouchZone_OnIsEmulatingMousePosition`
- Metadata signature: `protected override bool OnIsEmulatingMousePosition() { }`
- Native interval: `140` bytes
- Result: `pseudocode`
- Heuristic layout hint: `SuperTouchZone_Recovered` matched 2 offsets against `SuperTouchZone` metadata (confidence 1.00).

```c
typedef struct SuperTouchZone_Recovered {
    char padding_0[144];
    int maxFingers;
    char padding_94[44];
    struct struct_1 *multiFingerConfigs;
} SuperTouchZone_Recovered;

typedef struct struct_1 {
    char padding_0[24];
    unsigned int field_18;
    char padding_1c[4];
    struct struct_0 *field_20;
} struct_1;

typedef struct struct_0 {
    char padding_0[16];
    long long field_10;
} struct_0;

unsigned long long SuperTouchZone_OnIsEmulatingMousePosition(struct_2 *ptr, unsigned long a1, unsigned long a2, unsigned long a3)
{
    struct_1 *v0;  // x8

    if (ptr->field_90 < 1)
        return 0;
    v0 = ptr->field_c0;
    if (v0)
    {
        if (v0->field_18 <= 0)
        {
            sub_f7db7c(ptr);
        }
        else if (v0->field_20 && v0->field_20->field_10)
        {
            InputBindingBase__IsEmulatingMousePosition(v0->field_20->field_10, 0); /* do not return */
        }
    }
    ptr = sub_f7db74();
    sub_f7db7c(ptr);
}
```

## `SuperTouchZone.OnGetSubBindingDescriptions` — RVA `0xc4ca60`

- Decompiled symbol: `SuperTouchZone_OnGetSubBindingDescriptions`
- Metadata signature: `protected override void OnGetSubBindingDescriptions(BindingDescriptionList descList, Object undoObject, string parentMenuPath) { }`
- Native interval: `808` bytes
- Result: `pseudocode`
- Heuristic layout hint: `SuperTouchZone_Recovered` matched 3 offsets against `SuperTouchZone` metadata (confidence 1.00).

```c
typedef struct SuperTouchZone_Recovered {
    char padding_0[144];
    unsigned int maxFingers;
    char padding_94[44];
    struct struct_0 *multiFingerConfigs;
    char padding_c8[88];
    long long separateFingersAsEmuTouchesBinding;
} SuperTouchZone_Recovered;

typedef struct struct_3 {
    char padding_0[24];
    unsigned int field_18;
} struct_3;

typedef struct struct_2 {
    char padding_0[44];
    char field_2c;
} struct_2;

typedef struct struct_0 {
    char padding_0[24];
    unsigned int field_18;
} struct_0;

extern long long g_1f07458;
extern long long g_1f0cf48;
extern long long g_1f0cf50;
extern long long g_1f0cf58;
extern long long g_1f0d918;
extern long long g_1f0dc00;
extern char g_1fab23b;

long long SuperTouchZone_OnGetSubBindingDescriptions(struct_1 *ptr, struct_2 *a1, unsigned long a2, long long a3)
{
    unsigned long long v14;  // x30
    unsigned long long v15;  // x28
    unsigned long long v24;  // x19
    struct_1 *v25;  // x0
    struct_1 *v26;  // x0
    struct_1 *v27;  // x0
    struct_3 *p;  // x8
    unsigned long long v29;  // x25
    unsigned long long v30;  // x9
    long long v31;  // x0
    long long v32;  // x0
    unsigned long long v16;  // x27
    unsigned long long v17;  // x26
    unsigned long long v18;  // x25
    unsigned long long v19;  // x24
    unsigned long long v20;  // x23
    unsigned long long v21;  // x22
    unsigned long long v22;  // x21
    unsigned long long v23;  // x20
    unsigned int v0;  // [bp-0x64]
    char *v1;  // [bp-0x60]
    unsigned long long v2;  // [bp-0x58]
    unsigned long long v3;  // [bp-0x50]
    unsigned long long v4;  // [bp-0x48]
    unsigned long long v5;  // [bp-0x40]
    unsigned long long v6;  // [bp-0x38]
    unsigned long long v7;  // [bp-0x30]
    unsigned long long v8;  // [bp-0x28]
    unsigned long long v9;  // [bp-0x20]
    unsigned long long v10;  // [bp-0x18]
    unsigned long long v11;  // [bp-0x10]
    unsigned long long v12;  // [bp-0x8]
    char v13;  // [bp+0x0]

    v1 = &v13;
    v2 = v14;
    v3 = v15;
    v4 = v16;
    v5 = v17;
    v6 = v18;
    v7 = v19;
    v8 = v20;
    v9 = v21;
    v10 = v22;
    v11 = v23;
    v12 = v24;
    v25 = ptr;
    if (!(g_1fab23b & 1))
    {
        sub_f7d92c(&g_1f07458);
        sub_f7d92c("_#");
        sub_f7d92c(&g_1f0dc00);
        sub_f7d92c("]#");
        sub_f7d92c(&g_1f0cf58);
        sub_f7d92c("[#");
        sub_f7d92c(&g_1f0cf48);
        sub_f7d92c("a#");
        sub_f7d92c(&g_1f0cf50);
        v26 = sub_f7d92c(&g_1f0d918);
        g_1fab23b = 1;
        v25 = v26;
    }
    v0 = 0;
    p = ptr->field_c0;
    if (p)
    {
        v29 = 0;
        do
        {
            v30 = p->field_18;
            if ((v30 & 4294967295) > v29)
            {
                if (!a1)
                    break;
                if (a1->field_2c || ptr->field_90 > v29)
                {
                    if (v30 > v29)
                    {
                        if (*((long long *)&p[1].padding_0[4 + 8 * v29]))
                        {
                            v0 = (unsigned int)v29 + 1;
                            v31 = Int32__ToString(&v0, 0);
                            v32 = String__Concat(v31, g_1f07458, 0);
                            BindingDescriptionList__Add(a1, *((long long *)(*((long long *)&p[1].padding_0[4 + 8 * v29]) + 16)), v32, a3, ptr, 0); /* do not return */
                        }
                        break;
                    }
                    else
                    {
                        sub_f7db7c(v25);
                    }
                }
            }
            else
            {
                if (a1)
                    BindingDescriptionList__Add(a1, ptr->field_120, g_1f0d918, a3, ptr, 0); /* do not return */
                break;
            }
        } while ((v29 += 1, p));
    }
    v27 = sub_f7db74();
    sub_f7db7c(v27);
}
```

## `SuperTouchZone.DrawMarkerGUI` — RVA `0xc4cd88`

- Decompiled symbol: `SuperTouchZone_DrawMarkerGUI`
- Metadata signature: `public void DrawMarkerGUI() { }`
- Native interval: `28` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[488];
    long long field_1e8;
} struct_0;

long long SuperTouchZone_DrawMarkerGUI(struct_0 *a0)
{
    unsigned long long v0;  // x0

    if (a0->field_1e8)
    {
        v0 = SuperTouchZone_EmulatedFingerSystem__DrawMarkers(a0->field_1e8, 0);
        return SuperTouchZone_EmulatedFingerSystem__DrawMarkers(a0->field_1e8, 0);
    }
    sub_f7db74(0);
}
```

## `SuperTouchZone.ReleaseEmulatedFingers` — RVA `0xc4cda4`

- Decompiled symbol: `SuperTouchZone_ReleaseEmulatedFingers`
- Metadata signature: `private void ReleaseEmulatedFingers(bool cancel) { }`
- Native interval: `32` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[488];
    long long field_1e8;
} struct_0;

long long SuperTouchZone_ReleaseEmulatedFingers(struct_0 *a0, unsigned int a1)
{
    unsigned long long v0;  // x0

    if (a0->field_1e8)
    {
        v0 = SuperTouchZone_EmulatedFingerSystem__EndTouches(a0->field_1e8, a1 & 1, 0);
        return SuperTouchZone_EmulatedFingerSystem__EndTouches(a0->field_1e8, a1 & 1, 0);
    }
    sub_f7db74(0);
}
```
