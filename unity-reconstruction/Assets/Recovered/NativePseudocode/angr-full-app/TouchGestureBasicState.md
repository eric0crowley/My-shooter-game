# Native pseudocode: TouchGestureBasicState

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `TouchGestureBasicState.ctor` — RVA `0xc61ae0`

- Decompiled symbol: `TouchGestureBasicState_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long TouchGestureBasicState_ctor(void)
{
    long long v0;  // x0

    v0 = Object__ctor();
    return Object__ctor();
}
```

## `TouchGestureBasicState.Reset` — RVA `0xc61ae8`

- Decompiled symbol: `TouchGestureBasicState_Reset`
- Metadata signature: `public virtual void Reset() { }`
- Native interval: `248` bytes
- Result: `pseudocode`
- Heuristic layout hint: `TouchGestureBasicState_Recovered` matched 20 offsets against `TouchGestureBasicState` metadata (confidence 1.00).

```c
typedef struct TouchGestureBasicState_Recovered {
    char padding_0[18];
    unsigned short isPressureSensitive;
    unsigned long long pressureCur;
    unsigned short pressCur;
    char padding_1e[14];
    unsigned long long curDist;
    unsigned int releasedDist;
    unsigned long long posCurRaw;
    unsigned long long posPrevRaw;
    unsigned long long posCurSmooth;
    unsigned long long posPrevSmooth;
    char padding_54[20];
    unsigned long long relStartPos;
    unsigned long long relEndPos;
    char padding_78[8];
    unsigned int relDur;
    char padding_84[8];
    unsigned long long extremeDistCurSq;
    unsigned long long extremeDistPerAxisCur;
    unsigned long long extremeDistPerAxisPrev;
    char padding_a4[4];
    unsigned long long prepollState;
    unsigned long long pollCurPos;
    unsigned long long pollPressStartPos;
    unsigned long long pollReleasePos;
    unsigned int pollPressStartDelay;
} TouchGestureBasicState_Recovered;

typedef struct struct_2 {
    unsigned long long field_0;
} struct_2;

typedef struct struct_1 {
    char padding_0[184];
    struct struct_2 *field_b8;
} struct_1;

extern struct_1 *g_1ef22b8;
extern char g_1fab1e0;

struct_0 * TouchGestureBasicState_Reset(struct_0 *ptr)
{
    struct_0 *v0;  // x0
    struct_0 *v1;  // x0
    unsigned long long v2;  // d1
    unsigned long long v3;  // d0

    *((unsigned short *)((char *)&ptr->field_14 + 4)) = 0;
    ptr->field_12 = 0;
    ptr->field_94 = 0x3f80000000000000;
    *((unsigned long *)&(&ptr->field_12)[1]) = 0x3f8000003f800000;
    v0 = ptr;
    if (!g_1fab1e0)
    {
        v1 = sub_f7d92c(&g_1ef22b8);
        g_1fab1e0 = 1;
        v0 = v1;
    }
    ptr->field_9c = g_1ef22b8->field_b8->field_0;
    *((unsigned long long *)&ptr->padding_a4) = g_1ef22b8->field_b8->field_0;
    v2 = g_1ef22b8->field_b8->field_0;
    *((unsigned long *)&ptr->padding_78[4]) = 0;
    *((unsigned long *)&ptr->padding_1e[10]) = 0;
    *((unsigned int *)&ptr->field_b0) = 0;
    ptr->field_a8 = v2;
    *((unsigned long long *)&ptr->padding_84[0]) = g_1ef22b8->field_b8->field_0;
    *((unsigned long long *)&(&ptr->padding_84)[1]) = g_1ef22b8->field_b8->field_0;
    *((unsigned long long *)((char *)&ptr->field_2c + 4)) = g_1ef22b8->field_b8->field_0;
    *((unsigned long long *)((char *)&ptr->field_34 + 4)) = g_1ef22b8->field_b8->field_0;
    *((unsigned long long *)&(&ptr->field_30)[1]) = g_1ef22b8->field_b8->field_0;
    *((unsigned long long *)((char *)&ptr->field_3c + 4)) = g_1ef22b8->field_b8->field_0;
    v3 = g_1ef22b8->field_b8->field_0;
    *((unsigned int *)&ptr->field_70) = 0;
    *((unsigned int *)&ptr->field_2c) = 0;
    *((unsigned long long *)&ptr->padding_54[16]) = v3;
    *((unsigned long long *)&ptr->padding_54[8]) = g_1ef22b8->field_b8->field_0;
    return v0;
}
```

## `TouchGestureBasicState.SetSmoothingTime` — RVA `0xc61be0`

- Decompiled symbol: `TouchGestureBasicState_SetSmoothingTime`
- Metadata signature: `public void SetSmoothingTime(float smt) { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[164];
    unsigned int field_a4;
} struct_0;

struct_0 * TouchGestureBasicState_SetSmoothingTime(struct_0 *ptr)
{
    unsigned int v0;  // s0

    ptr->field_a4 = v0;
    return ptr;
}
```

## `TouchGestureBasicState.PressedRaw` — RVA `0xc61be8`

- Decompiled symbol: `TouchGestureBasicState_PressedRaw`
- Metadata signature: `public bool PressedRaw() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[28];
    char field_1c;
} struct_0;

long long TouchGestureBasicState_PressedRaw(struct_0 *a0)
{
    return a0->field_1c;
}
```

## `TouchGestureBasicState.JustPressedRaw` — RVA `0xc61bf0`

- Decompiled symbol: `TouchGestureBasicState_JustPressedRaw`
- Metadata signature: `public bool JustPressedRaw() { }`
- Native interval: `32` bytes
- Result: `pseudocode`

```c
unsigned long long TouchGestureBasicState_JustPressedRaw(char *a0)
{
    if (!a0[28])
    {
        return 0;
    }
    else if (a0[29])
    {
        return 0;
    }
    else
    {
        return 1;
    }
}
```

## `TouchGestureBasicState.JustReleasedRaw` — RVA `0xc61c10`

- Decompiled symbol: `TouchGestureBasicState_JustReleasedRaw`
- Metadata signature: `public bool JustReleasedRaw() { }`
- Native interval: `32` bytes
- Result: `pseudocode`

```c
unsigned long long TouchGestureBasicState_JustReleasedRaw(char *a0)
{
    if (a0[28])
    {
        return 0;
    }
    else if (!a0[29])
    {
        return 0;
    }
    else
    {
        return 1;
    }
}
```

## `TouchGestureBasicState.GetCurPosRaw` — RVA `0xc61c30`

- Decompiled symbol: `TouchGestureBasicState_GetCurPosRaw`
- Metadata signature: `public Vector2 GetCurPosRaw() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long TouchGestureBasicState_GetCurPosRaw(unsigned long a0)
{
    return a0;
}
```

## `TouchGestureBasicState.GetCurPosSmooth` — RVA `0xc61c38`

- Decompiled symbol: `TouchGestureBasicState_GetCurPosSmooth`
- Metadata signature: `public Vector2 GetCurPosSmooth() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long TouchGestureBasicState_GetCurPosSmooth(unsigned long a0)
{
    return a0;
}
```

## `TouchGestureBasicState.GetStartPos` — RVA `0xc61c40`

- Decompiled symbol: `TouchGestureBasicState_GetStartPos`
- Metadata signature: `public Vector2 GetStartPos() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long TouchGestureBasicState_GetStartPos(unsigned long a0)
{
    return a0;
}
```

## `TouchGestureBasicState.GetReleasedStartPos` — RVA `0xc61c48`

- Decompiled symbol: `TouchGestureBasicState_GetReleasedStartPos`
- Metadata signature: `public Vector2 GetReleasedStartPos() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long TouchGestureBasicState_GetReleasedStartPos(unsigned long a0)
{
    return a0;
}
```

## `TouchGestureBasicState.GetReleasedEndPos` — RVA `0xc61c50`

- Decompiled symbol: `TouchGestureBasicState_GetReleasedEndPos`
- Metadata signature: `public Vector2 GetReleasedEndPos() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long TouchGestureBasicState_GetReleasedEndPos(unsigned long a0)
{
    return a0;
}
```

## `TouchGestureBasicState.GetSwipeVecRaw` — RVA `0xc61c58`

- Decompiled symbol: `TouchGestureBasicState_GetSwipeVecRaw`
- Metadata signature: `public Vector2 GetSwipeVecRaw() { }`
- Native interval: `20` bytes
- Result: `pseudocode`

```c
long long TouchGestureBasicState_GetSwipeVecRaw(unsigned long a0)
{
    return a0;
}
```

## `TouchGestureBasicState.GetSwipeVecSmooth` — RVA `0xc61c6c`

- Decompiled symbol: `TouchGestureBasicState_GetSwipeVecSmooth`
- Metadata signature: `public Vector2 GetSwipeVecSmooth() { }`
- Native interval: `20` bytes
- Result: `pseudocode`

```c
long long TouchGestureBasicState_GetSwipeVecSmooth(unsigned long a0)
{
    return a0;
}
```

## `TouchGestureBasicState.GetDeltaVecRaw` — RVA `0xc61c80`

- Decompiled symbol: `TouchGestureBasicState_GetDeltaVecRaw`
- Metadata signature: `public Vector2 GetDeltaVecRaw() { }`
- Native interval: `20` bytes
- Result: `pseudocode`

```c
long long TouchGestureBasicState_GetDeltaVecRaw(unsigned long a0)
{
    return a0;
}
```

## `TouchGestureBasicState.GetDeltaVecSmooth` — RVA `0xc61c94`

- Decompiled symbol: `TouchGestureBasicState_GetDeltaVecSmooth`
- Metadata signature: `public Vector2 GetDeltaVecSmooth() { }`
- Native interval: `20` bytes
- Result: `pseudocode`

```c
long long TouchGestureBasicState_GetDeltaVecSmooth(unsigned long a0)
{
    return a0;
}
```

## `TouchGestureBasicState.Moved` — RVA `0xc61ca8`

- Decompiled symbol: `TouchGestureBasicState_Moved`
- Metadata signature: `public bool Moved(float threshSquared) { }`
- Native interval: `16` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[140];
    unsigned int field_8c;
} struct_0;

unsigned int TouchGestureBasicState_Moved(struct_0 *ptr)
{
    unsigned int v0;  // s1
    unsigned int v1;  // s0
    unsigned long v2;  // 4132

    v0 = ptr->field_8c;
    v2 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v0, v1)) >> 5 & 3 | (unsigned long long)(CmpF(v0, v1) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v0, v1)) >> 5 & 3 | (unsigned long long)(CmpF(v0, v1) & 1)) & ((unsigned long long)(char)(CmpF(v0, v1)) >> 5 & 3 | (unsigned long long)(CmpF(v0, v1) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if (!((char)v2))
        return 1;
    return 0;
}
```

## `TouchGestureBasicState.JustMoved` — RVA `0xc61cb8`

- Decompiled symbol: `TouchGestureBasicState_JustMoved`
- Metadata signature: `public bool JustMoved(float threshSquared) { }`
- Native interval: `36` bytes
- Result: `pseudocode`

```c
unsigned int TouchGestureBasicState_JustMoved(unsigned int *ptr)
{
    unsigned int v0;  // s1
    unsigned int v1;  // s0
    unsigned long v2;  // 4129
    unsigned int v3;  // s1
    unsigned long v4;  // 4132

    v0 = ptr[35];
    v2 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v0, v1)) >> 5 & 3 | (unsigned long long)(CmpF(v0, v1) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v0, v1)) >> 5 & 3 | (unsigned long long)(CmpF(v0, v1) & 1)) & ((unsigned long long)(char)(CmpF(v0, v1)) >> 5 & 3 | (unsigned long long)(CmpF(v0, v1) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if ((char)v2)
        return 0;
    v3 = ptr[36];
    v4 = arm64g_calculate_condition(128, (((((unsigned long long)(char)(CmpF(v3, v1)) >> 5 & 3 | (unsigned long long)(CmpF(v3, v1) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v3, v1)) >> 5 & 3 | (unsigned long long)(CmpF(v3, v1) & 1)) & ((unsigned long long)(char)(CmpF(v3, v1)) >> 5 & 3 | (unsigned long long)(CmpF(v3, v1) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if (!((char)v4))
        return 1;
    return 0;
}
```

## `TouchGestureBasicState.IsControlledByMouse` — RVA `0xc61cdc`

- Decompiled symbol: `TouchGestureBasicState_IsControlledByMouse`
- Metadata signature: `public bool IsControlledByMouse() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    char field_10;
} struct_0;

long long TouchGestureBasicState_IsControlledByMouse(struct_0 *a0)
{
    return a0->field_10;
}
```

## `TouchGestureBasicState.IsPressureSensitive` — RVA `0xc61ce4`

- Decompiled symbol: `TouchGestureBasicState_IsPressureSensitive`
- Metadata signature: `public bool IsPressureSensitive() { }`
- Native interval: `32` bytes
- Result: `pseudocode`

```c
unsigned long long TouchGestureBasicState_IsPressureSensitive(char *a0)
{
    if (!a0[28])
    {
        return 0;
    }
    else if (!a0[18])
    {
        return 0;
    }
    else
    {
        return 1;
    }
}
```

## `TouchGestureBasicState.GetPressure` — RVA `0xc61d04`

- Decompiled symbol: `TouchGestureBasicState_GetPressure`
- Metadata signature: `public float GetPressure() { }`
- Native interval: `24` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[28];
    char field_1c;
} struct_0;

struct_0 * TouchGestureBasicState_GetPressure(struct_0 *a0)
{
    if (!a0->field_1c)
        return a0;
    return a0;
}
```

## `TouchGestureBasicState.Update` — RVA `0xc61d1c`

- Decompiled symbol: `TouchGestureBasicState_Update`
- Metadata signature: `public virtual void Update() { }`
- Native interval: `24` bytes
- Result: `pseudocode`

```c
long long TouchGestureBasicState_Update(long long a0)
{
    unsigned long long v0;  // x0

    TouchGestureBasicState__InternalUpdate();
    v0 = TouchGestureBasicState__InternalPostUpdate(a0);
    return TouchGestureBasicState__InternalPostUpdate(a0);
}
```

## `TouchGestureBasicState.InternalUpdate` — RVA `0xc61d34`

- Decompiled symbol: `TouchGestureBasicState_InternalUpdate`
- Metadata signature: `protected void InternalUpdate() { }`
- Native interval: `388` bytes
- Result: `pseudocode`

```c
typedef struct struct_3 {
    char padding_0[408];
    struct struct_4 *field_198;
    unsigned long long field_1a0;
    struct struct_5 *field_1a8;
    unsigned long long field_1b0;
    unsigned long long field_1b8;
} struct_3;

typedef struct struct_4 {
    unsigned long long field_0;
} struct_4;

typedef struct struct_5 {
    unsigned long long field_0;
} struct_5;

void TouchGestureBasicState_InternalUpdate(void* ptr)
{
    unsigned long v0;  // x8
    char v1;  // x10
    unsigned long v10;  // x1
    unsigned long v11;  // x2
    unsigned long v12;  // x3
    void* v13;  // x0
    unsigned int v14;  // s8
    unsigned int v15;  // s2
    unsigned int v2;  // s0
    unsigned long v3;  // x11
    unsigned int v4;  // w12
    unsigned long v5;  // x8
    struct_3 *p;  // x9
    unsigned long v7;  // x1
    unsigned long v8;  // x2
    void* v9;  // x0

    v0 = (long long)ptr[68];
    v1 = (char)ptr[28];
    v2 = (int)ptr[140];
    v3 = (long long)ptr[148];
    v4 = (char)ptr[170];
    *((long long *)&ptr[60]) = (long long)ptr[52];
    *((unsigned long *)&ptr[76]) = v0;
    *((char *)&ptr[29]) = v1;
    *((unsigned int *)&ptr[144]) = v2;
    *((unsigned long *)&ptr[156]) = v3;
    if (v4 && (char)ptr[168])
    {
        v5 = (long long)ptr[192];
        p = *((long long *)ptr);
        v7 = (char)ptr[171];
        *((unsigned long *)&ptr[52]) = v5;
        *((unsigned long *)&ptr[68]) = v5;
        v8 = p->field_1b0;
        v9 = ptr;
        p->field_1a8();
    }
    if ((char)ptr[169] && !(char)ptr[168])
    {
        v10 = (char)ptr[17];
        v11 = (char)ptr[19];
        v12 = *((long long *)(*((long long *)ptr) + 416));
        v13 = ptr;
        (*((long long *)(*((long long *)ptr) + 408)))();
    }
    v14 = (int)ptr[72];
    *((long long *)&ptr[52]) = (long long)ptr[176];
    CFUtils__get_realDeltaTime();
    CFUtils__SmoothTowardsVec2();
    v15 = (int)ptr[172];
    *((unsigned int *)&ptr[68]) = v0;
    *((unsigned int *)&ptr[72]) = v14;
    *((unsigned int *)&ptr[20]) = v15;
    if (!(char)ptr[28])
        return;
    goto *((long long *)(*((long long *)ptr) + 440));
}
```

## `TouchGestureBasicState.InternalPostUpdate` — RVA `0xc61eb8`

- Decompiled symbol: `TouchGestureBasicState_InternalPostUpdate`
- Metadata signature: `protected void InternalPostUpdate() { }`
- Native interval: `84` bytes
- Result: `pseudocode`

```c
int TouchGestureBasicState_InternalPostUpdate(unsigned int *ptr)
{
    unsigned int v0;  // s9
    unsigned int v1;  // s0
    unsigned int v2;  // s0
    unsigned int v3;  // s8
    unsigned int v4;  // s0
    int v5;  // w0

    CFUtils__get_realDeltaTime();
    v0 = ptr[10];
    v2 = ptr[9] + v1;
    ptr[9] = v2;
    CFUtils__get_realDeltaTime();
    v3 = ptr[25];
    v4 = v0 + v2;
    ptr[10] = v4;
    v5 = CFUtils__get_realDeltaTime();
    ptr[25] = v3 + v4;
    return v5;
}
```

## `TouchGestureBasicState.OnTouchStart` — RVA `0xc61f0c`

- Decompiled symbol: `TouchGestureBasicState_OnTouchStart`
- Metadata signature: `public void OnTouchStart(Vector2 startPos, Vector2 curPos, float timeElapsed, TouchObject touchObj) { }`
- Native interval: `88` bytes
- Result: `pseudocode`
- Heuristic layout hint: `TouchGestureBasicState_Recovered` matched 3 offsets against `TouchGestureBasicState` metadata (confidence 1.00).

```c
typedef struct TouchGestureBasicState_Recovered {
    char padding_0[17];
    char pollStartedByMouse;
    char isPressureSensitive;
    char padding_13[1];
    unsigned int pressureCur;
} TouchGestureBasicState_Recovered;

typedef struct struct_1 {
    char padding_0[17];
    char field_11;
    char padding_12[1];
    char field_13;
    char padding_14[4];
    unsigned int field_18;
    char padding_1c[140];
    char field_a8;
    char field_a9;
    char field_aa;
    char padding_ab[5];
    unsigned int field_b0;
    unsigned int field_b4;
    unsigned int field_b8;
    unsigned int field_bc;
    char padding_c0[8];
    unsigned int field_c8;
} struct_1;

void TouchGestureBasicState_OnTouchStart(struct_1 *ptr, struct_0 *p)
{
    char v0;  // x8
    char v1;  // x9
    unsigned int v2;  // s5
    unsigned int v3;  // s0
    unsigned int v4;  // s1
    unsigned int v5;  // s4
    unsigned int v6;  // s2
    unsigned int v7;  // s3

    if (p)
    {
        v0 = p->field_11;
        v1 = p->field_12;
        v2 = p->field_14;
        if (!ptr->field_a8)
        {
            ptr->field_aa = 0;
        }
        else if (!ptr->field_aa)
        {
            return;
        }
        ptr->field_b8 = v3;
        ptr->field_bc = v4;
        ptr->field_c8 = v5;
        ptr->field_11 = v0;
        ptr->field_13 = v1;
        ptr->field_18 = v2;
        ptr->field_a9 = 1;
        ptr->field_b0 = v6;
        ptr->field_b4 = v7;
        return;
    }
    sub_f7db74();
}
```

## `TouchGestureBasicState.OnTouchStart` — RVA `0xc61f64`

- Decompiled symbol: `TouchGestureBasicState_OnTouchStart`
- Metadata signature: `public void OnTouchStart(Vector2 startPos, Vector2 curPos, float timeElapsed, bool controlledByMouse, bool isPressureSensitive, float pressure) { }`
- Native interval: `68` bytes
- Result: `pseudocode`
- Heuristic layout hint: `TouchGestureBasicState_Recovered` matched 9 offsets against `TouchGestureBasicState` metadata (confidence 0.82).

```c
typedef struct TouchGestureBasicState_Recovered {
    char padding_0[17];
    char pollStartedByMouse;
    char padding_12[1];
    char pollStartPressureSensitive;
    char padding_14[4];
    unsigned int pollStartPressure;
    char padding_1c[140];
    char prepollState;
    char pollStartedPress;
    char pollReleased;
    char padding_ab[5];
    unsigned int pollCurPos;
    unsigned int field_b4;
    unsigned int pollPressStartPos;
    unsigned int field_bc;
    char padding_c0[8];
    unsigned int pollPressStartDelay;
} TouchGestureBasicState_Recovered;

struct_0 * TouchGestureBasicState_OnTouchStart(struct_0 *ptr, char a1, char a2)
{
    unsigned int v0;  // s0
    unsigned int v1;  // s1
    unsigned int v2;  // s4
    unsigned int v3;  // s5
    unsigned int v4;  // s2
    unsigned int v5;  // s3

    if (!ptr->field_a8)
    {
        ptr->field_aa = 0;
    }
    else if (!ptr->field_aa)
    {
        return ptr;
    }
    ptr->field_b8 = v0;
    ptr->field_bc = v1;
    ptr->field_c8 = v2;
    ptr->field_18 = v3;
    ptr->field_a9 = 1;
    ptr->field_11 = a1 & 1;
    ptr->field_13 = a2 & 1;
    ptr->field_b0 = v4;
    ptr->field_b4 = v5;
    return ptr;
}
```

## `TouchGestureBasicState.OnTouchPressureChange` — RVA `0xc61fa8`

- Decompiled symbol: `TouchGestureBasicState_OnTouchPressureChange`
- Metadata signature: `public void OnTouchPressureChange(float pressure) { }`
- Native interval: `16` bytes
- Result: `pseudocode`
- Heuristic layout hint: `TouchGestureBasicState_Recovered` matched 2 offsets against `TouchGestureBasicState` metadata (confidence 1.00).

```c
typedef struct TouchGestureBasicState_Recovered {
    char padding_0[18];
    char isPressureSensitive;
    char padding_13[153];
    unsigned int pollCurPressure;
} TouchGestureBasicState_Recovered;

struct_0 * TouchGestureBasicState_OnTouchPressureChange(struct_0 *ptr)
{
    unsigned int v0;  // s0

    ptr->field_12 = 1;
    ptr->field_ac = v0;
    return ptr;
}
```

## `TouchGestureBasicState.OnTouchMove` — RVA `0xc61fb8`

- Decompiled symbol: `TouchGestureBasicState_OnTouchMove`
- Metadata signature: `public void OnTouchMove(Vector2 pos) { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
unsigned int [46] TouchGestureBasicState_OnTouchMove(unsigned int *ptr)
{
    unsigned int v0;  // s0
    unsigned int v1;  // s1

    ptr[44] = v0;
    ptr[45] = v1;
    return ptr;
}
```

## `TouchGestureBasicState.OnTouchMoveByDelta` — RVA `0xc61fc0`

- Decompiled symbol: `TouchGestureBasicState_OnTouchMoveByDelta`
- Metadata signature: `public void OnTouchMoveByDelta(Vector2 delta) { }`
- Native interval: `20` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[176];
    unsigned long long field_b0;
} struct_0;

struct_0 * TouchGestureBasicState_OnTouchMoveByDelta(struct_0 *ptr)
{
    ptr->field_b0 = [D] unsupported_Iop_ZeroHI64ofV128();
    return ptr;
}
```

## `TouchGestureBasicState.OnTouchEnd` — RVA `0xc61fd4`

- Decompiled symbol: `TouchGestureBasicState_OnTouchEnd`
- Metadata signature: `public void OnTouchEnd(Vector2 pos, bool cancel) { }`
- Native interval: `52` bytes
- Result: `pseudocode`
- Heuristic layout hint: `TouchGestureBasicState_Recovered` matched 5 offsets against `TouchGestureBasicState` metadata (confidence 0.83).

```c
typedef struct TouchGestureBasicState_Recovered {
    char padding_0[168];
    char prepollState;
    char pollStartedPress;
    char pollReleased;
    char pollReleasedAsCancel;
    char padding_ac[20];
    unsigned int pollReleasePos;
    unsigned int field_c4;
} TouchGestureBasicState_Recovered;

struct_0 * TouchGestureBasicState_OnTouchEnd(struct_0 *ptr, char a1)
{
    unsigned int v0;  // s0
    unsigned int v1;  // s1

    if (ptr->field_a8)
    {
        if (ptr->field_aa)
            return ptr;
    }
    else
    {
        if (!ptr->field_a9)
            return ptr;
    }
    ptr->field_aa = 1;
    ptr->field_ab = a1 & 1;
    ptr->field_c0 = v0;
    ptr->field_c4 = v1;
    return ptr;
}
```

## `TouchGestureBasicState.OnTouchEnd` — RVA `0xc62008`

- Decompiled symbol: `TouchGestureBasicState_OnTouchEnd`
- Metadata signature: `public void OnTouchEnd(bool cancel) { }`
- Native interval: `56` bytes
- Result: `pseudocode`
- Heuristic layout hint: `TouchGestureBasicState_Recovered` matched 6 offsets against `TouchGestureBasicState` metadata (confidence 1.00).

```c
typedef struct TouchGestureBasicState_Recovered {
    char padding_0[168];
    char prepollState;
    char pollStartedPress;
    char pollReleased;
    char pollReleasedAsCancel;
    char padding_ac[4];
    unsigned long long pollCurPos;
    char padding_b8[8];
    unsigned long long pollReleasePos;
} TouchGestureBasicState_Recovered;

struct_0 * TouchGestureBasicState_OnTouchEnd(struct_0 *ptr, char a1)
{
    unsigned long long v0;  // d0

    v0 = ptr->field_b0;
    if (ptr->field_a8)
    {
        if (ptr->field_aa)
            return ptr;
    }
    else
    {
        if (!ptr->field_a9)
            return ptr;
    }
    ptr->field_aa = 1;
    ptr->field_ab = a1 & 1;
    ptr->field_c0 = v0;
    return ptr;
}
```

## `TouchGestureBasicState.OnPress` — RVA `0xc62040`

- Decompiled symbol: `TouchGestureBasicState_OnPress`
- Metadata signature: `protected virtual void OnPress(Vector2 startPos, Vector2 pos, float delay, bool startedByMouse, bool isPressureSensitive = false, float pressure = 1.0) { }`
- Native interval: `144` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    unsigned long long field_0;
} struct_1;

typedef struct struct_0 {
    char padding_0[184];
    struct struct_1 *field_b8;
} struct_0;

extern struct_0 *g_1ef22b8;
extern char g_1fab1e0;

void* TouchGestureBasicState_OnPress(void* ptr, char a1, char a2)
{
    unsigned int v0;  // s0
    unsigned int v1;  // s1
    unsigned long v2;  // x8
    unsigned int v3;  // s4
    unsigned int v4;  // s2
    unsigned int v5;  // s3
    unsigned int v6;  // s5
    void* v7;  // x0
    void* v8;  // x0
    unsigned long long v9;  // d0

    *((unsigned int *)&ptr[60]) = v0;
    *((unsigned int *)&ptr[64]) = v1;
    *((char *)&ptr[16]) = a1 & 1;
    v2 = (long long)ptr[60];
    *((unsigned int *)&ptr[36]) = v3;
    *((unsigned int *)&ptr[92]) = v0;
    *((unsigned int *)&ptr[96]) = v1;
    *((unsigned int *)&ptr[52]) = v4;
    *((unsigned int *)&ptr[56]) = v5;
    *((unsigned int *)&ptr[68]) = v4;
    *((unsigned int *)&ptr[72]) = v5;
    *((unsigned int *)&ptr[20]) = v6;
    *((unsigned int *)&ptr[140]) = 0;
    *((unsigned int *)&ptr[144]) = 0;
    *((char *)&ptr[28]) = 1;
    *((char *)&ptr[18]) = a2 & 1;
    *((unsigned long *)&ptr[76]) = v2;
    v7 = ptr;
    if (!g_1fab1e0)
    {
        v8 = sub_f7d92c(&g_1ef22b8);
        g_1fab1e0 = 1;
        v7 = v8;
    }
    v9 = g_1ef22b8->field_b8->field_0;
    *((unsigned int *)&ptr[100]) = 0;
    *((unsigned int *)&ptr[148]) = _INSERT(v9, 8, v9);
    return v7;
}
```

## `TouchGestureBasicState.OnRelease` — RVA `0xc620d0`

- Decompiled symbol: `TouchGestureBasicState_OnRelease`
- Metadata signature: `protected virtual void OnRelease(Vector2 pos, bool cancel) { }`
- Native interval: `132` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    struct struct_0 *field_0;
    char padding_8[20];
    char field_1c;
    char padding_1d[11];
    unsigned int field_28;
    char padding_2c[8];
    unsigned int field_34;
    unsigned int field_38;
    char padding_3c[8];
    unsigned int field_44;
    unsigned int field_48;
} struct_2;

typedef struct struct_0 {
    char padding_0[440];
    struct struct_1 *field_1b8;
    unsigned long long field_1c0;
} struct_0;

typedef struct struct_1 {
    unsigned long long field_0;
} struct_1;

void TouchGestureBasicState_OnRelease(struct_2 *ptr)
{
    unsigned long long v4;  // d9
    unsigned long long v5;  // d8
    unsigned long long v6;  // x30
    unsigned long long v7;  // x19
    struct_0 *p;  // x8
    unsigned int v9;  // s0
    unsigned int v10;  // s1
    unsigned long long v11;  // x2
    unsigned long long flag;  // x1
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x18]
    unsigned long long v2;  // [bp-0x10]
    unsigned long long v3;  // [bp-0x8]

    v0 = v4;
    v1 = v5;
    v2 = v6;
    v3 = v7;
    p = ptr->field_0;
    ptr->field_28 = 0;
    ptr->field_34 = v9;
    ptr->field_38 = v10;
    ptr->field_44 = v9;
    ptr->field_48 = v10;
    ptr->field_1c = 0;
    v11 = p->field_1c0;
    flag = 1;
    p->field_1b8();
}
```

## `TouchGestureBasicState.CheckMovement` — RVA `0xc62154`

- Decompiled symbol: `TouchGestureBasicState_CheckMovement`
- Metadata signature: `protected virtual void CheckMovement(bool itsFinalUpdate) { }`
- Native interval: `60` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: Decompiler produced no C-like text

```c
// 0x1062154: ldur d0, [x0, #0x34]
// 0x1062158: ldur d1, [x0, #0x5c]
// 0x106215c: ldr s2, [x0, #0x8c]
// 0x1062160: ldur d3, [x0, #0x94]
// 0x1062164: fsub v4.2s, v0.2s, v1.2s
// 0x1062168: fabd v0.2s, v0.2s, v1.2s
// 0x106216c: fmul v1.2s, v4.2s, v4.2s
// 0x1062170: faddp s1, v1.2s
// 0x1062174: fcmgt v4.2s, v3.2s, v0.2s
// 0x1062178: fcmp s2, s1
// 0x106217c: bit v0.8b, v3.8b, v4.8b
// 0x1062180: fcsel s1, s2, s1, gt
// 0x1062184: str s1, [x0, #0x8c]
// 0x1062188: stur d0, [x0, #0x94]
// 0x106218c: ret
```
