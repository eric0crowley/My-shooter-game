# Native pseudocode: TouchGestureState

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `TouchGestureState.JustTapped` — RVA `0xc5fb40`

- Decompiled symbol: `TouchGestureState_JustTapped`
- Metadata signature: `public bool JustTapped(int howManyTimes) { }`
- Native interval: `32` bytes
- Result: `pseudocode`
- Heuristic layout hint: `TouchGestureState_Recovered` matched 2 offsets against `TouchGestureState` metadata (confidence 1.00).

```c
typedef struct TouchGestureState_Recovered {
    char padding_0[295];
    char justTapped;
    char padding_128[12];
    unsigned int tapCount;
} TouchGestureState_Recovered;

unsigned long long TouchGestureState_JustTapped(struct_0 *a0, unsigned int a1)
{
    if (!a0->field_127)
    {
        return 0;
    }
    else if (a0->field_134 != a1)
    {
        return 0;
    }
    else
    {
        return 1;
    }
}
```

## `TouchGestureState.GetConstrainedDeltaVec` — RVA `0xc5fb60`

- Decompiled symbol: `TouchGestureState_GetConstrainedDeltaVec`
- Metadata signature: `public Vector2 GetConstrainedDeltaVec() { }`
- Native interval: `16` bytes
- Result: `pseudocode`

```c
long long TouchGestureState_GetConstrainedDeltaVec(unsigned long a0)
{
    return a0;
}
```

## `TouchGestureState.GetScrollDelta` — RVA `0xc5fb70`

- Decompiled symbol: `TouchGestureState_GetScrollDelta`
- Metadata signature: `public Vector2 GetScrollDelta() { }`
- Native interval: `16` bytes
- Result: `pseudocode`

```c
long long TouchGestureState_GetScrollDelta(unsigned long a0)
{
    return a0;
}
```

## `TouchGestureState.BasicConstructor` — RVA `0xc62190`

- Decompiled symbol: `TouchGestureState_BasicConstructor`
- Metadata signature: `private void BasicConstructor(TouchGestureThresholds thresholds, TouchGestureConfig config) { }`
- Native interval: `232` bytes
- Result: `pseudocode`

```c
extern long long g_1eef5a8;
extern char g_1fab2e0;

void TouchGestureState_BasicConstructor(void* ptr, long long a1, long long a2)
{
    unsigned long long v6;  // x30
    unsigned long long v7;  // x23
    unsigned long long v8;  // x22
    unsigned long long v9;  // x21
    unsigned long long v10;  // x20
    unsigned long long v11;  // x19
    unsigned long v12;  // x20
    unsigned long v13;  // x20
    unsigned long v14;  // x20
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
    if (!(g_1fab2e0 & 1))
    {
        sub_f7d92c(&g_1eef5a8);
        g_1fab2e0 = 1;
    }
    *((long long *)&ptr[280]) = a2;
    sub_f7d8d0(ptr + 280, a2);
    *((long long *)&ptr[272]) = a1;
    sub_f7d8d0(ptr + 272, a1);
    v12 = sub_f7db70(g_1eef5a8);
    DirectionState__ctor(v12);
    *((unsigned long *)&ptr[312]) = v12;
    sub_f7d8d0(ptr + 312, v12);
    v13 = sub_f7db70(g_1eef5a8);
    DirectionState__ctor(v13);
    *((unsigned long *)&ptr[320]) = v13;
    sub_f7d8d0(ptr + 320, v13);
    v14 = sub_f7db70(g_1eef5a8);
    DirectionState__ctor(v14);
    *((unsigned long *)&ptr[328]) = v14;
    sub_f7d8d0(ptr + 328, v14);
    goto *((long long *)(*((long long *)ptr) + 376));
}
```

## `TouchGestureState.ctor` — RVA `0xc62278`

- Decompiled symbol: `TouchGestureState_ctor`
- Metadata signature: `public void .ctor(TouchGestureThresholds thresholds, TouchGestureConfig config) { }`
- Native interval: `52` bytes
- Result: `pseudocode`

```c
void TouchGestureState_ctor(void* a0, long long a1, long long a2)
{
    Object__ctor();
    TouchGestureState__BasicConstructor(a0, a1, a2); /* do not return */
}
```

## `TouchGestureState.ctor` — RVA `0xc622ac`

- Decompiled symbol: `TouchGestureState_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `36` bytes
- Result: `pseudocode`

```c
void TouchGestureState_ctor(void* a0)
{
    Object__ctor();
    TouchGestureState__BasicConstructor(a0, 0, 0); /* do not return */
}
```

## `TouchGestureState.SetThresholds` — RVA `0xc622d0`

- Decompiled symbol: `TouchGestureState_SetThresholds`
- Metadata signature: `public void SetThresholds(TouchGestureThresholds thresh) { }`
- Native interval: `16` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[272];
    unsigned long long field_110;
} struct_0;

long long TouchGestureState_SetThresholds(struct_0 *ptr, unsigned long a1)
{
    long long v0;  // x0

    ptr->field_110 = a1;
    v0 = sub_f7d8d0();
    return sub_f7d8d0();
}
```

## `TouchGestureState.SetConfig` — RVA `0xc622e0`

- Decompiled symbol: `TouchGestureState_SetConfig`
- Metadata signature: `public void SetConfig(TouchGestureConfig config) { }`
- Native interval: `16` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[280];
    unsigned long long field_118;
} struct_0;

long long TouchGestureState_SetConfig(struct_0 *ptr, unsigned long a1)
{
    long long v0;  // x0

    ptr->field_118 = a1;
    v0 = sub_f7d8d0();
    return sub_f7d8d0();
}
```

## `TouchGestureState.Reset` — RVA `0xc622f0`

- Decompiled symbol: `TouchGestureState_Reset`
- Metadata signature: `public override void Reset() { }`
- Native interval: `188` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[18];
    unsigned short field_12;
    char padding_14[4];
    unsigned long long field_14;
    unsigned short field_1c;
    char padding_1e[14];
    unsigned long long field_2c;
    unsigned int field_30;
    char padding_3c[4];
    unsigned long long field_34;
    unsigned long long field_3c;
    unsigned long long field_44;
    unsigned long long field_4c;
    char padding_54[20];
    char padding_74[4];
    unsigned long long field_68;
    unsigned long long field_70;
    char padding_78[8];
    unsigned int field_80;
    char padding_84[8];
    char padding_9c[4];
    unsigned long long field_8c;
    unsigned long long field_94;
    unsigned long long field_9c;
    char padding_a4[4];
    char padding_bc[4];
    unsigned long long field_a8;
    unsigned long long field_b0;
    unsigned long long field_b8;
    unsigned long long field_c0;
    unsigned int field_c8;
} struct_0;

typedef struct struct_1 {
    unsigned long long field_0;
} struct_1;

extern struct_0 *g_1ef22b8;
extern char g_1fab1e0;

unsigned long long [4] TouchGestureState_Reset(struct_0 *ptr)
{
    unsigned long long v0;  // d0
    unsigned long v1;  // x0
    unsigned long long v2[4];  // x0

    TouchGestureBasicState__Reset(ptr);
    *((unsigned int *)((char *)&ptr[1].field_14 + 4)) = 0;
    *((unsigned long *)&ptr[1].padding_14) = 0;
    if (!g_1fab1e0)
    {
        sub_f7d92c(&g_1ef22b8);
        g_1fab1e0 = 1;
    }
    ptr->field_c0 = g_1ef22b8->field_b8->field_0;
    v0 = g_1ef22b8->field_b8->field_0;
    *((unsigned int *)&ptr[1].field_44) = 0;
    *((unsigned int *)&ptr[1].field_68) = 0;
    *((unsigned int *)&ptr->padding_1e[2]) = 0;
    *((unsigned int *)&ptr->padding_1e[6]) = 0;
    *((char *)&ptr[1].field_70) = 0;
    *((unsigned long long *)&ptr->field_c8) = v0;
    *((unsigned short *)((char *)&ptr[1].field_34 + 3)) = 0;
    v1 = *((long long *)((char *)&ptr[1].field_44 + 4));
    *((unsigned int *)&ptr[1].field_1c) = 0;
    *((unsigned int *)&ptr[1].padding_3c[0]) = 0;
    *((unsigned short *)&ptr[1].field_34) = 0;
    if (v1)
    {
        DirectionState__Reset(v1);
        v1 = *((long long *)((char *)&ptr[1].field_4c + 4));
        if (v1)
        {
            DirectionState__Reset(v1);
            v1 = *((long long *)&ptr[1].padding_54[4]);
            if (v1)
            {
                v2 = DirectionState__Reset(v1);
                return DirectionState__Reset(v1);
            }
        }
    }
    sub_f7db74(v1);
}
```

## `TouchGestureState.PressedNormal` — RVA `0xc623ac`

- Decompiled symbol: `TouchGestureState_PressedNormal`
- Metadata signature: `public bool PressedNormal() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[260];
    char field_104;
} struct_0;

long long TouchGestureState_PressedNormal(struct_0 *a0)
{
    return a0->field_104;
}
```

## `TouchGestureState.JustPressedNormal` — RVA `0xc623b4`

- Decompiled symbol: `TouchGestureState_JustPressedNormal`
- Metadata signature: `public bool JustPressedNormal() { }`
- Native interval: `32` bytes
- Result: `pseudocode`

```c
unsigned long long TouchGestureState_JustPressedNormal(char *a0)
{
    if (!a0[260])
    {
        return 0;
    }
    else if (a0[261])
    {
        return 0;
    }
    else
    {
        return 1;
    }
}
```

## `TouchGestureState.JustReleasedNormal` — RVA `0xc623d4`

- Decompiled symbol: `TouchGestureState_JustReleasedNormal`
- Metadata signature: `public bool JustReleasedNormal() { }`
- Native interval: `32` bytes
- Result: `pseudocode`

```c
unsigned long long TouchGestureState_JustReleasedNormal(char *a0)
{
    if (a0[260])
    {
        return 0;
    }
    else if (!a0[261])
    {
        return 0;
    }
    else
    {
        return 1;
    }
}
```

## `TouchGestureState.PressedLong` — RVA `0xc623f4`

- Decompiled symbol: `TouchGestureState_PressedLong`
- Metadata signature: `public bool PressedLong() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[262];
    char field_106;
} struct_0;

long long TouchGestureState_PressedLong(struct_0 *a0)
{
    return a0->field_106;
}
```

## `TouchGestureState.JustPressedLong` — RVA `0xc623fc`

- Decompiled symbol: `TouchGestureState_JustPressedLong`
- Metadata signature: `public bool JustPressedLong() { }`
- Native interval: `32` bytes
- Result: `pseudocode`

```c
unsigned long long TouchGestureState_JustPressedLong(char *a0)
{
    if (!a0[262])
    {
        return 0;
    }
    else if (a0[263])
    {
        return 0;
    }
    else
    {
        return 1;
    }
}
```

## `TouchGestureState.JustReleasedLong` — RVA `0xc6241c`

- Decompiled symbol: `TouchGestureState_JustReleasedLong`
- Metadata signature: `public bool JustReleasedLong() { }`
- Native interval: `32` bytes
- Result: `pseudocode`

```c
unsigned long long TouchGestureState_JustReleasedLong(char *a0)
{
    if (a0[262])
    {
        return 0;
    }
    else if (!a0[263])
    {
        return 0;
    }
    else
    {
        return 1;
    }
}
```

## `TouchGestureState.GetTapPos` — RVA `0xc6243c`

- Decompiled symbol: `TouchGestureState_GetTapPos`
- Metadata signature: `public Vector2 GetTapPos() { }`
- Native interval: `12` bytes
- Result: `pseudocode`

```c
long long TouchGestureState_GetTapPos(unsigned long a0)
{
    return a0;
}
```

## `TouchGestureState.JustLongTapped` — RVA `0xc62448`

- Decompiled symbol: `TouchGestureState_JustLongTapped`
- Metadata signature: `public bool JustLongTapped() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[296];
    char field_128;
} struct_0;

long long TouchGestureState_JustLongTapped(struct_0 *a0)
{
    return a0->field_128;
}
```

## `TouchGestureState.GetSwipeDirState` — RVA `0xc62450`

- Decompiled symbol: `TouchGestureState_GetSwipeDirState`
- Metadata signature: `public DirectionState GetSwipeDirState() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[312];
    unsigned long long field_138;
} struct_0;

long long TouchGestureState_GetSwipeDirState(struct_0 *a0)
{
    return a0->field_138;
}
```

## `TouchGestureState.GetSwipeDirState4` — RVA `0xc62458`

- Decompiled symbol: `TouchGestureState_GetSwipeDirState4`
- Metadata signature: `public DirectionState GetSwipeDirState4() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[320];
    unsigned long long field_140;
} struct_0;

long long TouchGestureState_GetSwipeDirState4(struct_0 *a0)
{
    return a0->field_140;
}
```

## `TouchGestureState.GetSwipeDirState8` — RVA `0xc62460`

- Decompiled symbol: `TouchGestureState_GetSwipeDirState8`
- Metadata signature: `public DirectionState GetSwipeDirState8() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[328];
    unsigned long long field_148;
} struct_0;

long long TouchGestureState_GetSwipeDirState8(struct_0 *a0)
{
    return a0->field_148;
}
```

## `TouchGestureState.GetSegmentOrigin` — RVA `0xc62468`

- Decompiled symbol: `TouchGestureState_GetSegmentOrigin`
- Metadata signature: `public Vector2 GetSegmentOrigin() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long TouchGestureState_GetSegmentOrigin(unsigned long a0)
{
    return a0;
}
```

## `TouchGestureState.JustSwiped` — RVA `0xc62470`

- Decompiled symbol: `TouchGestureState_JustSwiped`
- Metadata signature: `public bool JustSwiped() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[289];
    char field_121;
} struct_0;

long long TouchGestureState_JustSwiped(struct_0 *a0)
{
    return a0->field_121;
}
```

## `TouchGestureState.Swiped` — RVA `0xc62478`

- Decompiled symbol: `TouchGestureState_Swiped`
- Metadata signature: `public bool Swiped() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[288];
    char field_120;
} struct_0;

long long TouchGestureState_Swiped(struct_0 *a0)
{
    return a0->field_120;
}
```

## `TouchGestureState.GetConstrainedSwipeVec` — RVA `0xc62480`

- Decompiled symbol: `TouchGestureState_GetConstrainedSwipeVec`
- Metadata signature: `public Vector2 GetConstrainedSwipeVec() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long TouchGestureState_GetConstrainedSwipeVec(unsigned long a0)
{
    return a0;
}
```

## `TouchGestureState.GetScroll` — RVA `0xc62488`

- Decompiled symbol: `TouchGestureState_GetScroll`
- Metadata signature: `public Vector2 GetScroll() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long TouchGestureState_GetScroll(unsigned long a0)
{
    return a0;
}
```

## `TouchGestureState.GetReleasedDurationRaw` — RVA `0xc62490`

- Decompiled symbol: `TouchGestureState_GetReleasedDurationRaw`
- Metadata signature: `public float GetReleasedDurationRaw() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long TouchGestureState_GetReleasedDurationRaw(unsigned long a0)
{
    return a0;
}
```

## `TouchGestureState.ForceSwipe` — RVA `0xc62498`

- Decompiled symbol: `TouchGestureState_ForceSwipe`
- Metadata signature: `public void ForceSwipe() { }`
- Native interval: `24` bytes
- Result: `pseudocode`

```c
void* TouchGestureState_ForceSwipe(void* ptr)
{
    if (!(char)ptr[288])
    {
        *((unsigned short *)&ptr[288]) = 257;
        return ptr;
    }
    return ptr;
}
```

## `TouchGestureState.OnSwipeStart` — RVA `0xc624b0`

- Decompiled symbol: `TouchGestureState_OnSwipeStart`
- Metadata signature: `private void OnSwipeStart() { }`
- Native interval: `24` bytes
- Result: `pseudocode`

```c
void* TouchGestureState_OnSwipeStart(void* ptr)
{
    if (!(char)ptr[288])
    {
        *((unsigned short *)&ptr[288]) = 257;
        return ptr;
    }
    return ptr;
}
```

## `TouchGestureState.BlockSwipe` — RVA `0xc624c8`

- Decompiled symbol: `TouchGestureState_BlockSwipe`
- Metadata signature: `public void BlockSwipe() { }`
- Native interval: `24` bytes
- Result: `pseudocode`

```c
void* TouchGestureState_BlockSwipe(void* ptr)
{
    unsigned int v0;  // w8

    v0 = (char)ptr[288];
    *((char *)&ptr[336]) = 1;
    if (v0)
        *((unsigned short *)&ptr[288]) = 0;
    return ptr;
}
```

## `TouchGestureState.HoldDelayedEvents` — RVA `0xc624e0`

- Decompiled symbol: `TouchGestureState_HoldDelayedEvents`
- Metadata signature: `public void HoldDelayedEvents(bool holdThemForNow) { }`
- Native interval: `12` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[294];
    char field_126;
} struct_0;

struct_0 * TouchGestureState_HoldDelayedEvents(struct_0 *ptr, char a1)
{
    ptr->field_126 = a1 & 1;
    return ptr;
}
```

## `TouchGestureState.CancelTap` — RVA `0xc624ec`

- Decompiled symbol: `TouchGestureState_CancelTap`
- Metadata signature: `public void CancelTap() { }`
- Native interval: `36` bytes
- Result: `pseudocode`
- Heuristic layout hint: `TouchGestureState_Recovered` matched 4 offsets against `TouchGestureState` metadata (confidence 0.80).

```c
typedef struct TouchGestureState_Recovered {
    char padding_0[28];
    char field_1c;
    char padding_1d[175];
    unsigned int elapsedSinceLastTapCandidate;
    char padding_d0[83];
    char cancelTapFlag;
    char padding_124[56];
    unsigned long long tapCandidateCount;
    char tapCandidateReleased;
} TouchGestureState_Recovered;

struct_0 * TouchGestureState_CancelTap(struct_0 *p)
{
    struct_0 *ptr;  // x8

    if (p->field_1c)
        p->field_123 = 1;
    ptr = &(&p->padding_124)[1];
    p->field_cc = 0;
    *((unsigned long long *)&ptr->padding_0[0]) = 0;
    ptr->padding_0[8] = 0;
    return p;
}
```

## `TouchGestureState.ResetTapState` — RVA `0xc62510`

- Decompiled symbol: `TouchGestureState_ResetTapState`
- Metadata signature: `private void ResetTapState() { }`
- Native interval: `20` bytes
- Result: `pseudocode`
- Heuristic layout hint: `TouchGestureState_Recovered` matched 3 offsets against `TouchGestureState` metadata (confidence 1.00).

```c
typedef struct TouchGestureState_Recovered {
    char padding_0[204];
    unsigned int elapsedSinceLastTapCandidate;
    char padding_d0[140];
    unsigned long long tapCandidateCount;
    char tapCandidateReleased;
} TouchGestureState_Recovered;

struct_0 * TouchGestureState_ResetTapState(struct_0 *p)
{
    struct_0 *ptr;  // x8

    ptr = &(&p->padding_d0)[1];
    p->field_cc = 0;
    *((unsigned long long *)&ptr->padding_0[0]) = 0;
    ptr->padding_0[8] = 0;
    return p;
}
```

## `TouchGestureState.DisableTapUntilRelease` — RVA `0xc62524`

- Decompiled symbol: `TouchGestureState_DisableTapUntilRelease`
- Metadata signature: `public void DisableTapUntilRelease() { }`
- Native interval: `28` bytes
- Result: `pseudocode`
- Heuristic layout hint: `TouchGestureState_Recovered` matched 4 offsets against `TouchGestureState` metadata (confidence 1.00).

```c
typedef struct TouchGestureState_Recovered {
    char padding_0[204];
    unsigned int elapsedSinceLastTapCandidate;
    char padding_d0[84];
    char disableTapUntilReleaseFlag;
    char padding_125[55];
    unsigned long long tapCandidateCount;
    char tapCandidateReleased;
} TouchGestureState_Recovered;

struct_0 * TouchGestureState_DisableTapUntilRelease(struct_0 *p)
{
    struct_0 *ptr;  // x9

    ptr = &(&p->padding_125)[1];
    p->field_cc = 0;
    p->field_124 = 1;
    *((unsigned long long *)&ptr->padding_0[0]) = 0;
    ptr->padding_0[8] = 0;
    return p;
}
```

## `TouchGestureState.FlushRegisteredTaps` — RVA `0xc62540`

- Decompiled symbol: `TouchGestureState_FlushRegisteredTaps`
- Metadata signature: `public void FlushRegisteredTaps() { }`
- Native interval: `12` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[293];
    char field_125;
} struct_0;

struct_0 * TouchGestureState_FlushRegisteredTaps(struct_0 *ptr)
{
    ptr->field_125 = 1;
    return ptr;
}
```

## `TouchGestureState.MarkAsNonStatic` — RVA `0xc6254c`

- Decompiled symbol: `TouchGestureState_MarkAsNonStatic`
- Metadata signature: `public void MarkAsNonStatic() { }`
- Native interval: `12` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[290];
    char field_122;
} struct_0;

struct_0 * TouchGestureState_MarkAsNonStatic(struct_0 *ptr)
{
    ptr->field_122 = 1;
    return ptr;
}
```

## `TouchGestureState.Update` — RVA `0xc62558`

- Decompiled symbol: `TouchGestureState_Update`
- Metadata signature: `public override void Update() { }`
- Native interval: `324` bytes
- Result: `pseudocode`

```c
typedef struct struct_3 {
    struct struct_1 *field_0;
    char padding_8[76];
    unsigned int field_54;
} struct_3;

typedef struct struct_1 {
    char padding_0[376];
    struct struct_2 *field_178;
    unsigned long long field_180;
} struct_1;

typedef struct struct_2 {
    unsigned long long field_0;
} struct_2;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1eeed10;
extern char g_1fab2e1;

int TouchGestureState_Update(void* ptr)
{
    struct_3 *p;  // x20
    unsigned int v1;  // s2
    char v10;  // x8
    char v11;  // x9
    unsigned long long v12;  // x10
    unsigned long long v13;  // x11
    unsigned long v14;  // x0
    int v15;  // w0
    int v16;  // w0
    unsigned int v2;  // s0
    unsigned long v3;  // 4140
    unsigned int v4;  // s0
    unsigned int v5;  // 4098
    unsigned long v6;  // 4111
    struct_1 *addr;  // x8
    unsigned long long v8;  // x1
    struct_3 *v9;  // x0

    if (!(g_1fab2e1 & 1))
    {
        sub_f7d92c(&g_1eeed10);
        g_1fab2e1 = 1;
    }
    p = (long long)ptr[272];
    if (p)
    {
        if (!g_1eeed10->field_e0)
            sub_f7da5c(g_1eeed10);
        CFScreen__get_dpi();
        v1 = p->field_54;
        v3 = arm64g_calculate_condition(128, (((((unsigned long long)(char)(CmpF(v2, 953267991)) >> 5 & 3 | (unsigned long long)(CmpF(v2, 953267991) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v2, 953267991)) >> 5 & 3 | (unsigned long long)(CmpF(v2, 953267991) & 1)) & ((unsigned long long)(char)(CmpF(v2, 953267991)) >> 5 & 3 | (unsigned long long)(CmpF(v2, 953267991) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if (!((char)v3))
            v4 = 0x42c00000;
        v5 = CmpF(v1, v4);
        v6 = (((CmpF(v1, v4) >> 5 & 3 | CmpF(v1, v4) & 1) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1;
        if (!((char)((v6 - ((CmpF(v1, v4) >> 5 & 3 | CmpF(v1, v4) & 1) & (v5 >> 5 & 3 | CmpF(v1, v4) & 1) >> 1 & 1)) * 0x10000000 >> 30)))
        {
            addr = p->field_0;
            p->field_54 = v4;
            v8 = addr->field_180;
            v9 = p;
            addr->field_178();
        }
    }
    *((unsigned short *)&ptr[295]) = 0;
    v10 = (char)ptr[260];
    v11 = (char)ptr[262];
    v12 = (long long)ptr[232];
    v13 = (long long)ptr[216];
    v14 = (long long)ptr[312];
    *((char *)&ptr[289]) = 0;
    *((char *)&ptr[261]) = v10;
    *((char *)&ptr[263]) = v11;
    *((unsigned long long *)&ptr[240]) = v12;
    *((unsigned long long *)&ptr[224]) = v13;
    if (v14)
    {
        DirectionState__BeginFrame(v14);
        v14 = (long long)ptr[320];
        if (v14)
        {
            DirectionState__BeginFrame(v14);
            v14 = (long long)ptr[328];
            if (v14)
            {
                DirectionState__BeginFrame(v14);
                TouchGestureBasicState__InternalUpdate(ptr);
                TouchGestureState__CheckTap(ptr, 0);
                v15 = TouchGestureBasicState__InternalPostUpdate(ptr);
                if (!(char)ptr[356])
                    return v15;
                v16 = CFUtils__get_realDeltaTime();
                *((unsigned int *)&ptr[204]) = (int)ptr[204] + v4;
                return v16;
            }
        }
    }
    sub_f7db74(v14);
}
```

## `TouchGestureState.CheckTap` — RVA `0xc626e0`

- Decompiled symbol: `TouchGestureState_CheckTap`
- Metadata signature: `private void CheckTap(bool lastUpdate) { }`
- Native interval: `816` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: Decompiler produced no C-like text

```c
// 0x10626e0: ldr x10, [x0, #0x110]
// 0x10626e4: cbz x10, #0x10627d4
// 0x10626e8: ldr x9, [x0, #0x118]
// 0x10626ec: cbz x9, #0x10627d4
// 0x10626f0: ldr w8, [x9, #0x10]
// 0x10626f4: cmp w8, #1
// 0x10626f8: b.lt #0x10627d4
// 0x10626fc: ldrb w11, [x0, #0x125]
// 0x1062700: add x8, x0, #0x12c
// 0x1062704: cbz w11, #0x1062748
// 0x1062708: ldr w12, [x0, #0x15c]
// 0x106270c: add x11, x0, #0x15c
// 0x1062710: cmp w12, #1
// 0x1062714: b.lt #0x1062738
// 0x1062718: ldr w13, [x0, #0x160]
// 0x106271c: cmp w12, w13
// 0x1062720: b.le #0x1062738
// 0x1062724: mov w13, #1
// 0x1062728: strb w13, [x0, #0x127]
// 0x106272c: ldr x13, [x8, #0x28]
// 0x1062730: str x13, [x8]
// 0x1062734: str w12, [x0, #0x134]
// 0x1062738: str wzr, [x0, #0xcc]
// 0x106273c: strb wzr, [x11, #8]
// 0x1062740: str xzr, [x11]
// 0x1062744: strb wzr, [x0, #0x125]
// 0x1062748: ldrb w11, [x0, #0x1c]
// 0x106274c: cbz w11, #0x10627d8
// 0x1062750: ldr w12, [x0, #0x15c]
// 0x1062754: add x11, x0, #0x15c
// 0x1062758: cmp w12, #1
// 0x106275c: b.lt #0x10627cc
// 0x1062760: ldrb w13, [x0, #0x126]
// 0x1062764: cbnz w13, #0x1062778
// 0x1062768: ldr s0, [x0, #0x24]
// 0x106276c: ldr s1, [x10, #0x2c]
// 0x1062770: fcmp s0, s1
// 0x1062774: b.gt #0x1062794
// 0x1062778: ldrb w13, [x0, #0x122]
// 0x106277c: cbnz w13, #0x1062794
// 0x1062780: ldr s0, [x10, #0x3c]
// 0x1062784: ldr s1, [x0, #0x8c]
// 0x1062788: fmul s0, s0, s0
// 0x106278c: fcmp s1, s0
// 0x1062790: b.le #0x10627cc
// 0x1062794: ldrb w13, [x9, #0x14]
// 0x1062798: cbnz w13, #0x10627bc
// 0x106279c: ldr w13, [x0, #0x160]
// 0x10627a0: cmp w12, w13
// 0x10627a4: b.le #0x10627bc
// 0x10627a8: mov w13, #1
// 0x10627ac: strb w13, [x0, #0x127]
// 0x10627b0: ldr x13, [x8, #0x28]
// 0x10627b4: str x13, [x8]
// 0x10627b8: str w12, [x0, #0x134]
// 0x10627bc: mov w12, wzr
// 0x10627c0: str wzr, [x0, #0xcc]
// 0x10627c4: strb wzr, [x11, #8]
// 0x10627c8: str xzr, [x11]
// 0x10627cc: ldrb w13, [x0, #0x1d]
// 0x10627d0: cbz w13, #0x1062868
// 0x10627d4: ret
// 0x10627d8: ldrb w11, [x0, #0x164]
// 0x10627dc: cbz w11, #0x1062834
// 0x10627e0: ldrb w11, [x0, #0x126]
// 0x10627e4: cbnz w11, #0x1062834
// 0x10627e8: ldr s0, [x0, #0xcc]
// 0x10627ec: ldr s1, [x10, #0x30]
// 0x10627f0: fcmp s0, s1
// 0x10627f4: b.le #0x1062834
// 0x10627f8: ldr w12, [x0, #0x15c]
// 0x10627fc: add x11, x0, #0x15c
// 0x1062800: cmp w12, #1
// 0x1062804: b.lt #0x1062828
// 0x1062808: ldr w13, [x0, #0x160]
// 0x106280c: cmp w12, w13
// 0x1062810: b.le #0x1062828
// 0x1062814: mov w13, #1
// 0x1062818: strb w13, [x0, #0x127]
// 0x106281c: ldr x13, [x8, #0x28]
// 0x1062820: str x13, [x8]
// 0x1062824: str w12, [x0, #0x134]
// 0x1062828: str wzr, [x0, #0xcc]
// 0x106282c: strb wzr, [x11, #8]
// 0x1062830: str xzr, [x11]
// 0x1062834: ldrb w11, [x0, #0x1d]
// 0x1062838: cbz w11, #0x10627d4
// 0x106283c: ldrb w11, [x0, #0x123]
// 0x1062840: cbnz w11, #0x106284c
// 0x1062844: ldrb w11, [x0, #0x124]
// 0x1062848: cbz w11, #0x10628dc
// 0x106284c: add x8, x0, #0x15c
// 0x1062850: str wzr, [x0, #0xcc]
// 0x1062854: str xzr, [x8]
// 0x1062858: strb wzr, [x8, #8]
// 0x106285c: add x8, x0, #0x123
// 0x1062860: strh wzr, [x8]
// 0x1062864: ret
// 0x1062868: cmp w12, #1
// 0x106286c: b.lt #0x10628cc
// 0x1062870: ldur d0, [x0, #0x34]
// 0x1062874: ldr d1, [x8, #0x28]
// 0x1062878: ldr s2, [x10, #0x40]
// 0x106287c: fsub v0.2s, v0.2s, v1.2s
// 0x1062880: fmul v0.2s, v0.2s, v0.2s
// 0x1062884: faddp s0, v0.2s
// 0x1062888: fmul s1, s2, s2
// 0x106288c: fcmp s0, s1
// 0x1062890: b.le #0x10627d4
// 0x1062894: ldrb w9, [x9, #0x14]
// 0x1062898: cbnz w9, #0x10628bc
// 0x106289c: ldr w9, [x0, #0x160]
// 0x10628a0: cmp w12, w9
// 0x10628a4: b.le #0x10628bc
// 0x10628a8: mov w9, #1
// 0x10628ac: strb w9, [x0, #0x127]
// 0x10628b0: ldr x9, [x8, #0x28]
// 0x10628b4: str x9, [x8]
// 0x10628b8: str w12, [x0, #0x134]
// 0x10628bc: str wzr, [x0, #0xcc]
// 0x10628c0: strb wzr, [x11, #8]
// 0x10628c4: str xzr, [x11]
// 0x10628c8: b #0x10628d0
// 0x10628cc: cbnz w12, #0x10627d4
// 0x10628d0: ldur x9, [x0, #0x5c]
// 0x10628d4: str x9, [x8, #0x28]
// 0x10628d8: ret
// 0x10628dc: ldrb w11, [x9, #0x16]
// 0x10628e0: ldr s0, [x0, #0x80]
// 0x10628e4: cbz w11, #0x1062930
// 0x10628e8: ldr s1, [x10, #0x34]
// 0x10628ec: fcmp s0, s1
// 0x10628f0: b.le #0x1062930
// 0x10628f4: ldrb w11, [x0, #0x122]
// 0x10628f8: cbnz w11, #0x1062930
// 0x10628fc: ldr s2, [x10, #0x38]
// 0x1062900: fadd s1, s1, s2
// 0x1062904: fcmp s0, s1
// 0x1062908: b.hi #0x1062930
// 0x106290c: ldr s1, [x10, #0x3c]
// 0x1062910: ldr s2, [x0, #0x84]
// 0x1062914: fmul s1, s1, s1
// 0x1062918: fcmp s2, s1
// 0x106291c: b.hi #0x1062930
// 0x1062920: ldr x11, [x0, #0x68]
// 0x1062924: mov w12, #1
// 0x1062928: strb w12, [x0, #0x128]
// 0x106292c: str x11, [x8]
// 0x1062930: ldr s1, [x10, #0x2c]
// 0x1062934: fcmp s0, s1
// 0x1062938: b.hi #0x1062958
// 0x106293c: ldrb w11, [x0, #0x122]
// 0x1062940: cbnz w11, #0x1062958
// 0x1062944: ldr s0, [x10, #0x3c]
// 0x1062948: ldr s1, [x0, #0x84]
// 0x106294c: fmul s0, s0, s0
// 0x1062950: fcmp s1, s0
// 0x1062954: b.ls #0x10629a4
// 0x1062958: ldrb w10, [x9, #0x14]
// 0x106295c: add x9, x0, #0x15c
// 0x1062960: cbz w10, #0x1062974
// 0x1062964: str wzr, [x0, #0xcc]
// 0x1062968: strb wzr, [x9, #8]
// 0x106296c: str xzr, [x9]
// 0x1062970: b #0x106285c
// 0x1062974: ldr w10, [x9]
// 0x1062978: cmp w10, #1
// 0x106297c: b.lt #0x1062964
// 0x1062980: ldr w11, [x0, #0x160]
// 0x1062984: cmp w10, w11
// 0x1062988: b.le #0x1062964
// 0x106298c: mov w11, #1
// 0x1062990: strb w11, [x0, #0x127]
// 0x1062994: ldr x11, [x8, #0x28]
// 0x1062998: str x11, [x8]
// 0x106299c: str w10, [x0, #0x134]
// 0x10629a0: b #0x1062964
// 0x10629a4: ldr w10, [x0, #0x15c]
// 0x10629a8: add w10, w10, #1
// 0x10629ac: str w10, [x0, #0x15c]
// 0x10629b0: ldr w11, [x9, #0x10]
// 0x10629b4: cmp w10, w11
// 0x10629b8: b.ge #0x1062a00
// 0x10629bc: cmp w10, #1
// 0x10629c0: b.lt #0x10629f0
// 0x10629c4: ldrb w9, [x9, #0x14]
// 0x10629c8: cbnz w9, #0x10629f0
// 0x10629cc: ldr w9, [x0, #0x160]
// 0x10629d0: cmp w10, w9
// 0x10629d4: b.le #0x10629f0
// 0x10629d8: mov w9, #1
// 0x10629dc: str w10, [x0, #0x160]
// 0x10629e0: strb w9, [x0, #0x127]
// 0x10629e4: ldr x9, [x8, #0x28]
// 0x10629e8: str x9, [x8]
// 0x10629ec: str w10, [x0, #0x134]
// 0x10629f0: mov w8, #1
// 0x10629f4: strb w8, [x0, #0x164]
// 0x10629f8: str wzr, [x0, #0xcc]
// 0x10629fc: b #0x106285c
// 0x1062a00: cmp w10, #1
// 0x1062a04: add x9, x0, #0x15c
// 0x1062a08: b.ge #0x1062980
// 0x1062a0c: b #0x1062964
```

## `TouchGestureState.OnRelease` — RVA `0xc62a10`

- Decompiled symbol: `TouchGestureState_OnRelease`
- Metadata signature: `protected override void OnRelease(Vector2 pos, bool cancel) { }`
- Native interval: `44` bytes
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

void TouchGestureState_OnRelease(struct_2 *p, unsigned long a1)
{
    struct_2 *ptr;  // x8

    if (((char)a1 & 1))
    {
        if (p->field_1c)
            p[3].padding_3c[3] = 1;
        ptr = &p[4].padding_2c;
        p[2].field_34 = 0;
        ptr->field_0 = 0;
        ptr->padding_8[0] = 0;
    }
    TouchGestureBasicState__OnRelease(p); /* do not return */
}
```

## `TouchGestureState.OnPress` — RVA `0xc62a3c`

- Decompiled symbol: `TouchGestureState_OnPress`
- Metadata signature: `protected override void OnPress(Vector2 startPos, Vector2 pos, float delay, bool startedByMouse, bool isPressureSensitive, float pressure) { }`
- Native interval: `212` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[36];
    unsigned long long field_24;
    unsigned int field_2c;
} struct_0;

typedef struct struct_2 {
    unsigned long long field_0;
} struct_2;

typedef struct struct_1 {
    char padding_0[184];
    struct struct_2 *field_b8;
} struct_1;

extern struct_1 *g_1ef22b8;
extern char g_1fab1e0;

unsigned long long [4] TouchGestureState_OnPress(void* ptr, char a1, char a2)
{
    unsigned long long v0;  // x9
    int v1;  // q0
    unsigned long long v2;  // d0
    struct_0 *index;  // x8
    unsigned long v5;  // x0
    unsigned long long v6[4];  // x0

    TouchGestureBasicState__OnPress(ptr, a1 & 1, a2 & 1);
    *((char *)&ptr[336]) = 0;
    *((unsigned short *)&ptr[288]) = 0;
    *((char *)&ptr[290]) = 0;
    if (!g_1fab1e0)
    {
        sub_f7d92c(&g_1ef22b8);
        g_1fab1e0 = 1;
    }
    v0 = (long long)ptr[68];
    v1 = (int)_INSERT(g_1ef22b8->field_b8->field_0, 8, g_1ef22b8->field_b8->field_0);
    ptr[216] = v1;
    v2 = g_1ef22b8->field_b8->field_0;
    index = (long long)ptr[280];
    *((unsigned long long *)&ptr[208]) = v0;
    *((unsigned int *)&ptr[0x100]) = 0;
    *((unsigned int *)&ptr[232]) = _INSERT(v2, 8, v2);
    *((unsigned long long *)&ptr[248]) = 0;
    if (index)
    {
        *((int *)&ptr[0x100]) = *((int *)((char *)&index->field_24 + 4));
        *((long long *)&ptr[248]) = *((long long *)&(&index->padding_0)[1]);
    }
    v5 = (long long)ptr[312];
    if (v5)
    {
        DirectionState__Reset(v5);
        v5 = (long long)ptr[320];
        if (v5)
        {
            DirectionState__Reset(v5);
            v5 = (long long)ptr[328];
            if (v5)
            {
                v6 = DirectionState__Reset(v5);
                return DirectionState__Reset(v5);
            }
        }
    }
    sub_f7db74(v5);
}
```

## `TouchGestureState.CheckMovement` — RVA `0xc62b10`

- Decompiled symbol: `TouchGestureState_CheckMovement`
- Metadata signature: `protected override void CheckMovement(bool itsFinalUpdate) { }`
- Native interval: `1424` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: Decompiler produced no C-like text

```c
// 0x1062b10: str d10, [sp, #-0x50]!
// 0x1062b14: stp d9, d8, [sp, #8]
// 0x1062b18: str x30, [sp, #0x18]
// 0x1062b1c: stp x24, x23, [sp, #0x20]
// 0x1062b20: stp x22, x21, [sp, #0x30]
// 0x1062b24: stp x20, x19, [sp, #0x40]
// 0x1062b28: ldur d0, [x0, #0x34]
// 0x1062b2c: ldur d1, [x0, #0x5c]
// 0x1062b30: ldur d2, [x0, #0x94]
// 0x1062b34: ldr x8, [x0, #0x110]
// 0x1062b38: fabd v3.2s, v0.2s, v1.2s
// 0x1062b3c: fcmgt v4.2s, v2.2s, v3.2s
// 0x1062b40: bif v2.8b, v3.8b, v4.8b
// 0x1062b44: ldr s3, [x0, #0x8c]
// 0x1062b48: fsub v0.2s, v0.2s, v1.2s
// 0x1062b4c: fmul v0.2s, v0.2s, v0.2s
// 0x1062b50: faddp s0, v0.2s
// 0x1062b54: fcmp s3, s0
// 0x1062b58: fcsel s0, s3, s0, gt
// 0x1062b5c: str s0, [x0, #0x8c]
// 0x1062b60: stur d2, [x0, #0x94]
// 0x1062b64: cbz x8, #0x106305c
// 0x1062b68: ldr x9, [x0, #0x118]
// 0x1062b6c: mov x19, x0
// 0x1062b70: cbz x9, #0x106305c
// 0x1062b74: ldrb w10, [x19, #0x1c]
// 0x1062b78: cbz w10, #0x1062bc4
// 0x1062b7c: ldrb w10, [x19, #0x106]
// 0x1062b80: cbz w10, #0x1062bd0
// 0x1062b84: ldrb w10, [x9, #0x17]
// 0x1062b88: cbz w10, #0x1062ba4
// 0x1062b8c: ldrb w10, [x19, #0x122]
// 0x1062b90: cbnz w10, #0x1062bb4
// 0x1062b94: ldr s1, [x8, #0x3c]
// 0x1062b98: fmul s1, s1, s1
// 0x1062b9c: fcmp s0, s1
// 0x1062ba0: b.gt #0x1062bb4
// 0x1062ba4: ldrb w8, [x9, #0x18]
// 0x1062ba8: cbz w8, #0x1062bfc
// 0x1062bac: ldrb w8, [x19, #0x120]
// 0x1062bb0: cbz w8, #0x1062bfc
// 0x1062bb4: mov w9, wzr
// 0x1062bb8: mov w8, wzr
// 0x1062bbc: strb wzr, [x19, #0x106]
// 0x1062bc0: b #0x1062c00
// 0x1062bc4: strb wzr, [x19, #0x104]
// 0x1062bc8: strb wzr, [x19, #0x106]
// 0x1062bcc: b #0x1062c24
// 0x1062bd0: ldrb w9, [x9, #0x15]
// 0x1062bd4: cbz w9, #0x1062bf4
// 0x1062bd8: ldrb w9, [x19, #0x122]
// 0x1062bdc: cbnz w9, #0x1062bf0
// 0x1062be0: ldr s1, [x8, #0x3c]
// 0x1062be4: fmul s1, s1, s1
// 0x1062be8: fcmp s0, s1
// 0x1062bec: b.le #0x1063078
// 0x1062bf0: mov w9, wzr
// 0x1062bf4: mov w8, wzr
// 0x1062bf8: b #0x1062c00
// 0x1062bfc: mov w9, #1
// 0x1062c00: ldrb w10, [x19, #0x104]
// 0x1062c04: cbnz w10, #0x1062c24
// 0x1062c08: tbnz w8, #0, #0x1062c24
// 0x1062c0c: tbnz w9, #0, #0x1062c24
// 0x1062c10: mov x0, x19
// 0x1062c14: bl #0x10630ac
// 0x1062c18: tbnz w0, #0, #0x1062c24
// 0x1062c1c: mov w8, #1
// 0x1062c20: strb w8, [x19, #0x104]
// 0x1062c24: ldp s0, s1, [x19, #0x34]
// 0x1062c28: ldp s2, s3, [x19, #0x5c]
// 0x1062c2c: ldr w8, [x19, #0x100]
// 0x1062c30: fsub s9, s0, s2
// 0x1062c34: fsub s8, s1, s3
// 0x1062c38: cbz w8, #0x1062ca8
// 0x1062c3c: cmp w8, #3
// 0x1062c40: b.ne #0x1062c8c
// 0x1062c44: ldr x8, [x19, #0x110]
// 0x1062c48: cbz x8, #0x1062d0c
// 0x1062c4c: ldr s0, [x8, #0x50]
// 0x1062c50: fabs s1, s9
// 0x1062c54: fcmp s1, s0
// 0x1062c58: b.le #0x1062c68
// 0x1062c5c: mov w8, #1
// 0x1062c60: str w8, [x19, #0x100]
// 0x1062c64: b #0x1062c6c
// 0x1062c68: mov w8, #3
// 0x1062c6c: fabs s2, s8
// 0x1062c70: fcmp s2, s1
// 0x1062c74: b.le #0x1062c8c
// 0x1062c78: fcmp s2, s0
// 0x1062c7c: b.le #0x1062c8c
// 0x1062c80: mov w8, #2
// 0x1062c84: str w8, [x19, #0x100]
// 0x1062c88: b #0x1062c9c
// 0x1062c8c: cmp w8, #1
// 0x1062c90: b.eq #0x1062ca4
// 0x1062c94: cmp w8, #2
// 0x1062c98: b.ne #0x1062ca8
// 0x1062c9c: fmov s9, wzr
// 0x1062ca0: b #0x1062ca8
// 0x1062ca4: fmov s8, wzr
// 0x1062ca8: ldr x8, [x19, #0x110]
// 0x1062cac: cbz x8, #0x1062d0c
// 0x1062cb0: mov w21, #1
// 0x1062cb4: mov w20, #0xec
// 0x1062cb8: mov w22, #0xe8
// 0x1062cbc: mov w23, #0x7f800000
// 0x1062cc0: mov w24, #-0x80000000
// 0x1062cc4: tst w21, #1
// 0x1062cc8: csel x9, x22, x20, ne
// 0x1062ccc: ldr s3, [x19, x9]
// 0x1062cd0: ldr s1, [x8, #0x50]
// 0x1062cd4: ldr s2, [x8, #0x20]
// 0x1062cd8: fmov s4, w23
// 0x1062cdc: fcsel s0, s9, s8, ne
// 0x1062ce0: fcvtzs w8, s3
// 0x1062ce4: fcmp s3, s4
// 0x1062ce8: csel w0, w24, w8, eq
// 0x1062cec: mov x1, xzr
// 0x1062cf0: bl #0x1058578
// 0x1062cf4: scvtf s0, w0
// 0x1062cf8: tbz w21, #0, #0x1062d10
// 0x1062cfc: ldr x8, [x19, #0x110]
// 0x1062d00: mov w21, wzr
// 0x1062d04: str s0, [x19, #0xe8]
// 0x1062d08: cbnz x8, #0x1062cc4
// 0x1062d0c: bl #0xf7db74
// 0x1062d10: ldur d1, [x19, #0x44]
// 0x1062d14: ldur d2, [x19, #0x5c]
// 0x1062d18: ldr w8, [x19, #0xf8]
// 0x1062d1c: str s0, [x19, #0xec]
// 0x1062d20: fsub v0.2s, v1.2s, v2.2s
// 0x1062d24: mov s1, v0.s[1]
// 0x1062d28: str d0, [x19, #0xd8]
// 0x1062d2c: cbz w8, #0x1062de8
// 0x1062d30: cmp w8, #3
// 0x1062d34: b.ne #0x1062d88
// 0x1062d38: ldr x8, [x19, #0x110]
// 0x1062d3c: cbz x8, #0x1062d0c
// 0x1062d40: ldr s2, [x19, #0x94]
// 0x1062d44: ldr s3, [x8, #0x44]
// 0x1062d48: fabs s2, s2
// 0x1062d4c: fcmp s2, s3
// 0x1062d50: b.le #0x1062d60
// 0x1062d54: mov w8, #1
// 0x1062d58: str w8, [x19, #0xf8]
// 0x1062d5c: b #0x1062d64
// 0x1062d60: mov w8, #3
// 0x1062d64: ldr s4, [x19, #0x98]
// 0x1062d68: fabs s4, s4
// 0x1062d6c: fcmp s4, s3
// 0x1062d70: b.le #0x1062d88
// 0x1062d74: fcmp s4, s2
// 0x1062d78: b.le #0x1062d88
// 0x1062d7c: mov w8, #2
// 0x1062d80: str w8, [x19, #0xf8]
// 0x1062d84: b #0x1062da4
// 0x1062d88: cmp w8, #2
// 0x1062d8c: b.eq #0x1062da4
// 0x1062d90: cmp w8, #1
// 0x1062d94: b.ne #0x1062db0
// 0x1062d98: str wzr, [x19, #0xdc]
// 0x1062d9c: fmov s1, wzr
// 0x1062da0: b #0x1062de8
// 0x1062da4: str wzr, [x19, #0xd8]
// 0x1062da8: fmov s0, wzr
// 0x1062dac: b #0x1062de8
// 0x1062db0: adrp x20, #0x1fab000
// 0x1062db4: ldrb w8, [x20, #0x1e0]
// 0x1062db8: cbnz w8, #0x1062dd0
// 0x1062dbc: adrp x0, #0x1e8c000
// 0x1062dc0: ldr x0, [x0, #0x138]
// 0x1062dc4: bl #0xf7d92c
// 0x1062dc8: mov w8, #1
// 0x1062dcc: strb w8, [x20, #0x1e0]
// 0x1062dd0: adrp x8, #0x1e8c000
// 0x1062dd4: ldr x8, [x8, #0x138]
// 0x1062dd8: ldr x8, [x8]
// 0x1062ddc: ldr x8, [x8, #0xb8]
// 0x1062de0: ldp s0, s1, [x8]
// 0x1062de4: stp s0, s1, [x19, #0xd8]
// 0x1062de8: ldrb w8, [x19, #0x120]
// 0x1062dec: cbnz w8, #0x1062e24
// 0x1062df0: ldrb w8, [x19, #0x150]
// 0x1062df4: cbnz w8, #0x1062e24
// 0x1062df8: ldr x8, [x19, #0x110]
// 0x1062dfc: cbz x8, #0x1062d0c
// 0x1062e00: ldr s2, [x8, #0x44]
// 0x1062e04: fmul s0, s0, s0
// 0x1062e08: fmul s1, s1, s1
// 0x1062e0c: fadd s0, s0, s1
// 0x1062e10: fmul s1, s2, s2
// 0x1062e14: fcmp s0, s1
// 0x1062e18: b.le #0x1062e24
// 0x1062e1c: mov w8, #0x101
// 0x1062e20: strh w8, [x19, #0x120]
// 0x1062e24: ldp s0, s1, [x19, #0x44]
// 0x1062e28: ldp s2, s3, [x19, #0xd0]
// 0x1062e2c: ldr w8, [x19, #0xfc]
// 0x1062e30: fsub s8, s0, s2
// 0x1062e34: fsub s9, s1, s3
// 0x1062e38: cbz w8, #0x1062ee0
// 0x1062e3c: cmp w8, #3
// 0x1062e40: b.ne #0x1062e8c
// 0x1062e44: ldr x8, [x19, #0x110]
// 0x1062e48: cbz x8, #0x1062d0c
// 0x1062e4c: ldr s0, [x8, #0x48]
// 0x1062e50: fabs s1, s8
// 0x1062e54: fcmp s1, s0
// 0x1062e58: b.le #0x1062e68
// 0x1062e5c: mov w8, #1
// 0x1062e60: str w8, [x19, #0xfc]
// 0x1062e64: b #0x1062e6c
// 0x1062e68: mov w8, #3
// 0x1062e6c: fabs s2, s9
// 0x1062e70: fcmp s2, s1
// 0x1062e74: b.le #0x1062e8c
// 0x1062e78: fcmp s2, s0
// 0x1062e7c: b.le #0x1062e8c
// 0x1062e80: mov w8, #2
// 0x1062e84: str w8, [x19, #0xfc]
// 0x1062e88: b #0x1062e9c
// 0x1062e8c: cmp w8, #1
// 0x1062e90: b.eq #0x1062ea4
// 0x1062e94: cmp w8, #2
// 0x1062e98: b.ne #0x1062eac
// 0x1062e9c: fmov s8, wzr
// 0x1062ea0: b #0x1062ee0
// 0x1062ea4: fmov s9, wzr
// 0x1062ea8: b #0x1062ee0
// 0x1062eac: adrp x20, #0x1fab000
// 0x1062eb0: ldrb w8, [x20, #0x1e0]
// 0x1062eb4: cbnz w8, #0x1062ecc
// 0x1062eb8: adrp x0, #0x1e8c000
// 0x1062ebc: ldr x0, [x0, #0x138]
// 0x1062ec0: bl #0xf7d92c
// 0x1062ec4: mov w8, #1
// 0x1062ec8: strb w8, [x20, #0x1e0]
// 0x1062ecc: adrp x8, #0x1e8c000
// 0x1062ed0: ldr x8, [x8, #0x138]
// 0x1062ed4: ldr x8, [x8]
// 0x1062ed8: ldr x8, [x8, #0xb8]
// 0x1062edc: ldp s8, s9, [x8]
// 0x1062ee0: ldr x8, [x19, #0x110]
// 0x1062ee4: cbz x8, #0x1062d0c
// 0x1062ee8: ldr s0, [x8, #0x48]
// 0x1062eec: fmul s1, s8, s8
// 0x1062ef0: fmul s2, s9, s9
// 0x1062ef4: fadd s10, s2, s1
// 0x1062ef8: fmul s0, s0, s0
// 0x1062efc: fcmp s10, s0
// 0x1062f00: b.le #0x106305c
// 0x1062f04: adrp x20, #0x1fab000
// 0x1062f08: ldrb w8, [x20, #0x243]
// 0x1062f0c: cbnz w8, #0x1062f24
// 0x1062f10: adrp x0, #0x1e8c000
// 0x1062f14: ldr x0, [x0, #0xa60]
// 0x1062f18: bl #0xf7d92c
// 0x1062f1c: mov w8, #1
// 0x1062f20: strb w8, [x20, #0x243]
// 0x1062f24: adrp x8, #0x1e8c000
// 0x1062f28: ldr x8, [x8, #0xa60]
// 0x1062f2c: ldr x0, [x8]
// 0x1062f30: ldr w8, [x0, #0xe0]
// 0x1062f34: cbnz w8, #0x1062f3c
// 0x1062f38: bl #0xf7da5c
// 0x1062f3c: adrp x8, #0x832000
// 0x1062f40: ldr s1, [x8, #0x41c]
// 0x1062f44: fsqrt s0, s10
// 0x1062f48: fcmp s0, s1
// 0x1062f4c: b.le #0x1062f5c
// 0x1062f50: fdiv s8, s8, s0
// 0x1062f54: fdiv s9, s9, s0
// 0x1062f58: b #0x1062f90
// 0x1062f5c: adrp x20, #0x1fab000
// 0x1062f60: ldrb w8, [x20, #0x1e0]
// 0x1062f64: cbnz w8, #0x1062f7c
// 0x1062f68: adrp x0, #0x1e8c000
// 0x1062f6c: ldr x0, [x0, #0x138]
// 0x1062f70: bl #0xf7d92c
// 0x1062f74: mov w8, #1
// 0x1062f78: strb w8, [x20, #0x1e0]
// 0x1062f7c: adrp x8, #0x1e8c000
// 0x1062f80: ldr x8, [x8, #0x138]
// 0x1062f84: ldr x8, [x8]
// 0x1062f88: ldr x8, [x8, #0xb8]
// 0x1062f8c: ldp s8, s9, [x8]
// 0x1062f90: ldr x20, [x19, #0x140]
// 0x1062f94: cbz x20, #0x1062d0c
// 0x1062f98: adrp x8, #0x832000
// 0x1062f9c: ldr s10, [x8, #0x3b8]
// 0x1062fa0: ldr w0, [x20, #0x10]
// 0x1062fa4: mov v0.16b, v8.16b
// 0x1062fa8: mov v1.16b, v9.16b
// 0x1062fac: mov v2.16b, v10.16b
// 0x1062fb0: mov w1, wzr
// 0x1062fb4: mov x2, xzr
// 0x1062fb8: bl #0x1059aac
// 0x1062fbc: ldr x8, [x19, #0x118]
// 0x1062fc0: cbz x8, #0x1062d0c
// 0x1062fc4: ldr w2, [x8, #0x20]
// 0x1062fc8: mov w1, w0
// 0x1062fcc: mov x0, x20
// 0x1062fd0: mov x3, xzr
// 0x1062fd4: bl #0x105af0c
// 0x1062fd8: ldr x20, [x19, #0x148]
// 0x1062fdc: cbz x20, #0x1062d0c
// 0x1062fe0: ldr w0, [x20, #0x10]
// 0x1062fe4: mov w1, #1
// 0x1062fe8: mov v0.16b, v8.16b
// 0x1062fec: mov v1.16b, v9.16b
// 0x1062ff0: mov v2.16b, v10.16b
// 0x1062ff4: mov x2, xzr
// 0x1062ff8: bl #0x1059aac
// 0x1062ffc: ldr x8, [x19, #0x118]
// 0x1063000: cbz x8, #0x1062d0c
// 0x1063004: ldr w2, [x8, #0x20]
// 0x1063008: mov w1, w0
// 0x106300c: mov x0, x20
// 0x1063010: mov x3, xzr
// 0x1063014: bl #0x105af0c
// 0x1063018: ldr x8, [x19, #0x118]
// 0x106301c: cbz x8, #0x1062d0c
// 0x1063020: ldr w9, [x8, #0x1c]
// 0x1063024: add x10, x19, #0x140
// 0x1063028: add x11, x19, #0x148
// 0x106302c: cmp w9, #1
// 0x1063030: csel x9, x11, x10, eq
// 0x1063034: ldr x9, [x9]
// 0x1063038: cbz x9, #0x1062d0c
// 0x106303c: ldr x0, [x19, #0x138]
// 0x1063040: cbz x0, #0x1062d0c
// 0x1063044: ldr w2, [x8, #0x20]
// 0x1063048: ldr w1, [x9, #0x10]
// 0x106304c: mov x3, xzr
// 0x1063050: bl #0x105af0c
// 0x1063054: ldur x8, [x19, #0x44]
// 0x1063058: str x8, [x19, #0xd0]
// 0x106305c: ldp x20, x19, [sp, #0x40]
// 0x1063060: ldp x22, x21, [sp, #0x30]
// 0x1063064: ldp x24, x23, [sp, #0x20]
// 0x1063068: ldr x30, [sp, #0x18]
// 0x106306c: ldp d9, d8, [sp, #8]
// 0x1063070: ldr d10, [sp], #0x50
// 0x1063074: ret
// 0x1063078: ldr s0, [x19, #0x24]
// 0x106307c: ldr s1, [x8, #0x34]
// 0x1063080: mov w8, #1
// 0x1063084: fcmp s0, s1
// 0x1063088: b.le #0x1063098
// 0x106308c: mov w9, #1
// 0x1063090: strb w8, [x19, #0x106]
// 0x1063094: b #0x1062bf4
// 0x1063098: mov w9, wzr
// 0x106309c: b #0x1062c00
```

## `TouchGestureState.IsPotentialTap` — RVA `0xc630ac`

- Decompiled symbol: `TouchGestureState_IsPotentialTap`
- Metadata signature: `public bool IsPotentialTap() { }`
- Native interval: `108` bytes
- Result: `pseudocode`
- Heuristic layout hint: `TouchGestureState_Recovered` matched 5 offsets against `TouchGestureState` metadata (confidence 0.62).

```c
typedef struct TouchGestureState_Recovered {
    char padding_0[28];
    char field_1c;
    char padding_1d[7];
    unsigned int field_24;
    char padding_28[100];
    unsigned int field_8c;
    char padding_90[128];
    struct struct_2 *thresh;
    struct struct_0 *config;
    char padding_120[2];
    char nonStaticFlag;
    char cancelTapFlag;
    char disableTapUntilReleaseFlag;
} TouchGestureState_Recovered;

typedef struct struct_0 {
    char padding_0[16];
    int field_10;
} struct_0;

typedef struct struct_2 {
    char padding_0[44];
    unsigned int field_2c;
    char padding_30[12];
    unsigned int field_3c;
} struct_2;

unsigned int TouchGestureState_IsPotentialTap(struct_1 *ptr)
{
    unsigned int p[16];  // x8
    unsigned int v1;  // s0
    unsigned int v2;  // s1
    unsigned long v3;  // 4133
    unsigned int v4;  // s1
    unsigned int v5;  // s0
    unsigned long v6;  // 4149

    p = ptr->field_110;
    if (!p)
    {
        return 0;
    }
    else if (!ptr->field_118)
    {
        return 0;
    }
    else if (!ptr->field_1c)
    {
        return 0;
    }
    else if (ptr->field_123)
    {
        return 0;
    }
    else if (ptr->field_124)
    {
        return 0;
    }
    else if (ptr->field_118->field_10 < 1)
    {
        return 0;
    }
    else if (ptr->field_122)
    {
        return 0;
    }
    else
    {
        v1 = ptr->field_24;
        v2 = p[11];
        v3 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v1, v2)) >> 5 & 3 | (unsigned long long)(CmpF(v1, v2) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v1, v2)) >> 5 & 3 | (unsigned long long)(CmpF(v1, v2) & 1)) & ((unsigned long long)(char)(CmpF(v1, v2)) >> 5 & 3 | (unsigned long long)(CmpF(v1, v2) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if ((char)v3)
            return 0;
        v4 = ptr->field_8c;
        v5 = p[15] * p[15];
        v6 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v4, v5)) >> 5 & 3 | (unsigned long long)(CmpF(v4, v5) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v4, v5)) >> 5 & 3 | (unsigned long long)(CmpF(v4, v5) & 1)) & ((unsigned long long)(char)(CmpF(v4, v5)) >> 5 & 3 | (unsigned long long)(CmpF(v4, v5) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if (!((char)v6))
            return 1;
        return 0;
    }
}
```

## `TouchGestureState.IsPotentialLongPress` — RVA `0xc63130`

- Decompiled symbol: `TouchGestureState_IsPotentialLongPress`
- Metadata signature: `public bool IsPotentialLongPress() { }`
- Native interval: `88` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[28];
    char field_1c;
    char padding_1d[7];
    unsigned int field_24;
    char padding_28[100];
    unsigned int field_8c;
    char padding_90[128];
    struct struct_2 *field_110;
    struct struct_0 *field_118;
    char padding_120[2];
    char field_122;
} struct_1;

typedef struct struct_0 {
    char padding_0[21];
    char field_15;
} struct_0;

typedef struct struct_2 {
    char padding_0[52];
    unsigned int field_34;
    char padding_38[4];
    unsigned int field_3c;
} struct_2;

unsigned int TouchGestureState_IsPotentialLongPress(struct_1 *ptr)
{
    unsigned int p[16];  // x8
    unsigned int v1;  // s0
    unsigned int v2;  // s1
    unsigned long v3;  // 4133
    unsigned int v4;  // s1
    unsigned int v5;  // s0
    unsigned long v6;  // 4149

    p = ptr->field_110;
    if (!p)
    {
        return 0;
    }
    else if (!ptr->field_118)
    {
        return 0;
    }
    else if (!ptr->field_1c)
    {
        return 0;
    }
    else if (ptr->field_122)
    {
        return 0;
    }
    else if (!ptr->field_118->field_15)
    {
        return 0;
    }
    else
    {
        v1 = ptr->field_24;
        v2 = p[13];
        v3 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v1, v2)) >> 5 & 3 | (unsigned long long)(CmpF(v1, v2) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v1, v2)) >> 5 & 3 | (unsigned long long)(CmpF(v1, v2) & 1)) & ((unsigned long long)(char)(CmpF(v1, v2)) >> 5 & 3 | (unsigned long long)(CmpF(v1, v2) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if ((char)v3)
            return 0;
        v4 = ptr->field_8c;
        v5 = p[15] * p[15];
        v6 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v4, v5)) >> 5 & 3 | (unsigned long long)(CmpF(v4, v5) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v4, v5)) >> 5 & 3 | (unsigned long long)(CmpF(v4, v5) & 1)) & ((unsigned long long)(char)(CmpF(v4, v5)) >> 5 & 3 | (unsigned long long)(CmpF(v4, v5) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if (!((char)v6))
            return 1;
        return 0;
    }
}
```

## `TouchGestureState.ReportTap` — RVA `0xc63188`

- Decompiled symbol: `TouchGestureState_ReportTap`
- Metadata signature: `private void ReportTap(bool reset) { }`
- Native interval: `76` bytes
- Result: `pseudocode`
- Heuristic layout hint: `TouchGestureState_Recovered` matched 8 offsets against `TouchGestureState` metadata (confidence 1.00).

```c
typedef struct TouchGestureState_Recovered {
    char padding_0[204];
    unsigned int elapsedSinceLastTapCandidate;
    char padding_d0[87];
    char justTapped;
    char padding_128[4];
    unsigned long long tapPos;
    unsigned int tapCount;
    char padding_138[28];
    unsigned long long tapFirstPos;
    unsigned int tapCandidateCount[2];
    char lastReportedTapCount;
    char padding_161[3];
    char tapCandidateReleased;
} TouchGestureState_Recovered;

struct_0 * TouchGestureState_ReportTap(struct_0 *ptr, unsigned long a1)
{
    unsigned int v0;  // w8
    struct_0 *p;  // x8

    v0 = *((int *)((char *)&ptr->field_154 + 4));
    if (v0 >= 1 && v0 > ptr->field_15c[0])
    {
        ptr->field_15c[0] = v0;
        ptr->field_127 = 1;
        *((long long *)&(&ptr->padding_128)[1]) = *((long long *)&ptr->padding_138[24]);
        *((unsigned int *)((char *)&ptr->field_12c + 4)) = v0;
    }
    if (((char)a1 & 1))
    {
        p = (char *)&ptr->field_154 + 4;
        ptr->field_cc = 0;
        p->padding_0[8] = 0;
        *((unsigned long *)&p->padding_0[0]) = 0;
    }
    return ptr;
}
```

## `TouchGestureState.ReportTap` — RVA `0xc631e0`

- Decompiled symbol: `TouchGestureState_ReportTap`
- Metadata signature: `private void ReportTap() { }`
- Native interval: `68` bytes
- Result: `pseudocode`
- Heuristic layout hint: `TouchGestureState_Recovered` matched 7 offsets against `TouchGestureState` metadata (confidence 1.00).

```c
typedef struct TouchGestureState_Recovered {
    char padding_0[204];
    unsigned int elapsedSinceLastTapCandidate;
    char padding_d0[87];
    char justTapped;
    char padding_128[4];
    unsigned long long tapPos;
    unsigned int tapCount;
    char padding_138[28];
    unsigned long long tapFirstPos;
    unsigned int tapCandidateCount[2];
    char tapCandidateReleased;
} TouchGestureState_Recovered;

struct_0 * TouchGestureState_ReportTap(struct_0 *ptr)
{
    unsigned int v0;  // w9
    struct_0 *p;  // x8

    v0 = *((int *)((char *)&ptr->field_154 + 4));
    p = (char *)&ptr->field_154 + 4;
    if (v0 >= 1 && v0 > ptr->field_15c[0])
    {
        ptr->field_127 = 1;
        *((long long *)&(&ptr->padding_128)[1]) = *((long long *)&ptr->padding_138[24]);
        *((unsigned int *)((char *)&ptr->field_12c + 4)) = v0;
    }
    ptr->field_cc = 0;
    p->padding_0[8] = 0;
    *((unsigned long *)&p->padding_0[0]) = 0;
    return ptr;
}
```
