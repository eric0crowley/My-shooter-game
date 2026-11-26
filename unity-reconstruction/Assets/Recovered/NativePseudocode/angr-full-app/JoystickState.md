# Native pseudocode: JoystickState

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `JoystickState.ctor` — RVA `0xc60ac0`

- Decompiled symbol: `JoystickState_ctor`
- Metadata signature: `public void .ctor(JoystickConfig config) { }`
- Native interval: `216` bytes
- Result: `pseudocode`

```c
extern long long g_1eef5a8;
extern char g_1fab2df;

long long JoystickState_ctor(void* a0, long long a1)
{
    void* ptr;  // x0
    unsigned long v1;  // x20
    void* p;  // x0
    unsigned long v3;  // x20
    void* addr;  // x0
    unsigned long v5;  // x20
    void* ptr3;  // x0
    unsigned long long v7;  // x0

    if (!(g_1fab2df & 1))
    {
        sub_f7d92c(&g_1eef5a8);
        g_1fab2df = 1;
    }
    Object__ctor(a0, 0);
    ptr = a0;
    *((long long *)&ptr[16]) = a1;
    sub_f7d8d0(ptr + 16, a1);
    v1 = sub_f7db70(g_1eef5a8);
    DirectionState__ctor(v1);
    p = a0;
    *((unsigned long *)&p[64]) = v1;
    sub_f7d8d0(p + 64, v1);
    v3 = sub_f7db70(g_1eef5a8);
    DirectionState__ctor(v3);
    addr = a0;
    *((unsigned long *)&addr[72]) = v3;
    sub_f7d8d0(addr + 72, v3);
    v5 = sub_f7db70(g_1eef5a8);
    DirectionState__ctor(v5);
    ptr3 = a0;
    *((unsigned long *)&ptr3[80]) = v5;
    sub_f7d8d0(ptr3 + 80, v5);
    v7 = JoystickState__Reset(a0);
    return JoystickState__Reset(a0);
}
```

## `JoystickState.Reset` — RVA `0xc60b98`

- Decompiled symbol: `JoystickState_Reset`
- Metadata signature: `public void Reset() { }`
- Native interval: `236` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    unsigned long long field_0;
    char padding_8[8];
    unsigned long long field_10;
} struct_1;

typedef struct struct_0 {
    char padding_0[184];
    struct struct_1 *field_b8;
} struct_0;

extern struct_0 *g_1ef22b8;
extern char g_1fab1e0;
extern char g_1fab329;

unsigned long long [4] JoystickState_Reset(void* ptr)
{
    unsigned long v0;  // x0
    unsigned long long v1;  // d0
    unsigned long long v2[4];  // x0
    unsigned long long v3;  // d0
    int v4;  // q0

    if (!g_1fab329)
    {
        sub_f7d92c(&g_1ef22b8);
        g_1fab329 = 1;
    }
    v0 = (long long)ptr[64];
    v1 = g_1ef22b8->field_b8->field_10;
    *((unsigned int *)&ptr[32]) = 0;
    *((unsigned long long *)&ptr[52]) = v1;
    if (v0)
    {
        DirectionState__Reset(v0);
        v0 = (long long)ptr[72];
        if (v0)
        {
            DirectionState__Reset(v0);
            v0 = (long long)ptr[80];
            if (v0)
            {
                v2 = DirectionState__Reset(v0);
                *((unsigned int *)&ptr[104]) = 0;
                if (!g_1fab1e0)
                {
                    v2 = sub_f7d92c(&g_1ef22b8);
                    g_1fab1e0 = 1;
                }
                *((unsigned long long *)&ptr[96]) = g_1ef22b8->field_b8->field_0;
                v3 = g_1ef22b8->field_b8->field_0;
                *((unsigned int *)&ptr[28]) = 0;
                *((unsigned long long *)&ptr[88]) = 0;
                *((unsigned long long *)&ptr[108]) = v3;
                *((unsigned long long *)&ptr[52]) = 0x3f80000000000000;
                v4 = (int)_INSERT(g_1ef22b8->field_b8->field_0, 8, g_1ef22b8->field_b8->field_0);
                ptr[36] = v4;
                return v2;
            }
        }
    }
    sub_f7db74(v0);
}
```

## `JoystickState.GetVector` — RVA `0xc60c84`

- Decompiled symbol: `JoystickState_GetVector`
- Metadata signature: `public Vector2 GetVector() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long JoystickState_GetVector(unsigned long a0)
{
    return a0;
}
```

## `JoystickState.GetVectorRaw` — RVA `0xc60c8c`

- Decompiled symbol: `JoystickState_GetVectorRaw`
- Metadata signature: `public Vector2 GetVectorRaw() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long JoystickState_GetVectorRaw(unsigned long a0)
{
    return a0;
}
```

## `JoystickState.GetVectorEx` — RVA `0xc60c94`

- Decompiled symbol: `JoystickState_GetVectorEx`
- Metadata signature: `public Vector2 GetVectorEx(bool squareMode) { }`
- Native interval: `72` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[16];
    struct struct_0 *field_10;
} struct_1;

typedef struct struct_0 {
    char padding_0[56];
    unsigned int field_38;
} struct_0;

struct_1 * JoystickState_GetVectorEx(struct_1 *a0, unsigned long a1)
{
    unsigned int v0;  // w8
    unsigned long long v1;  // x0
    unsigned long long v2;  // x0

    if (a0->field_10)
    {
        if (a0->field_10->field_38 == 1)
            v0 = 0;
        else
            v0 = 1;
        if ((((char)v0 ^ (char)a1) & 1))
        {
            return a0;
        }
        else if (((char)a1 & 1))
        {
            v1 = CFUtils__CircularToSquareJoystickVec();
            return CFUtils__CircularToSquareJoystickVec();
        }
        else
        {
            v2 = CFUtils__SquareToCircularJoystickVec();
            return CFUtils__SquareToCircularJoystickVec();
        }
    }
    sub_f7db74();
}
```

## `JoystickState.GetVectorRawEx` — RVA `0xc60cdc`

- Decompiled symbol: `JoystickState_GetVectorRawEx`
- Metadata signature: `public Vector2 GetVectorRawEx(bool squareMode) { }`
- Native interval: `72` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[16];
    struct struct_0 *field_10;
} struct_1;

typedef struct struct_0 {
    char padding_0[56];
    unsigned int field_38;
} struct_0;

struct_1 * JoystickState_GetVectorRawEx(struct_1 *a0, unsigned long a1)
{
    unsigned int v0;  // w8
    unsigned long long v1;  // x0
    unsigned long long v2;  // x0

    if (a0->field_10)
    {
        if (a0->field_10->field_38 == 1)
            v0 = 0;
        else
            v0 = 1;
        if ((((char)v0 ^ (char)a1) & 1))
        {
            return a0;
        }
        else if (((char)a1 & 1))
        {
            v1 = CFUtils__CircularToSquareJoystickVec();
            return CFUtils__CircularToSquareJoystickVec();
        }
        else
        {
            v2 = CFUtils__SquareToCircularJoystickVec();
            return CFUtils__SquareToCircularJoystickVec();
        }
    }
    sub_f7db74();
}
```

## `JoystickState.GetAngle` — RVA `0xc60d24`

- Decompiled symbol: `JoystickState_GetAngle`
- Metadata signature: `public float GetAngle() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long JoystickState_GetAngle(unsigned long a0)
{
    return a0;
}
```

## `JoystickState.GetTilt` — RVA `0xc60d2c`

- Decompiled symbol: `JoystickState_GetTilt`
- Metadata signature: `public float GetTilt() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long JoystickState_GetTilt(unsigned long a0)
{
    return a0;
}
```

## `JoystickState.GetDirState` — RVA `0xc60d34`

- Decompiled symbol: `JoystickState_GetDirState`
- Metadata signature: `public DirectionState GetDirState() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[64];
    unsigned long long field_40;
} struct_0;

long long JoystickState_GetDirState(struct_0 *a0)
{
    return a0->field_40;
}
```

## `JoystickState.GetDirState4` — RVA `0xc60d3c`

- Decompiled symbol: `JoystickState_GetDirState4`
- Metadata signature: `public DirectionState GetDirState4() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[72];
    unsigned long long field_48;
} struct_0;

long long JoystickState_GetDirState4(struct_0 *a0)
{
    return a0->field_48;
}
```

## `JoystickState.GetDirState8` — RVA `0xc60d44`

- Decompiled symbol: `JoystickState_GetDirState8`
- Metadata signature: `public DirectionState GetDirState8() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[80];
    unsigned long long field_50;
} struct_0;

long long JoystickState_GetDirState8(struct_0 *a0)
{
    return a0->field_50;
}
```

## `JoystickState.GetDir` — RVA `0xc60d4c`

- Decompiled symbol: `JoystickState_GetDir`
- Metadata signature: `public Dir GetDir() { }`
- Native interval: `28` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[64];
    struct struct_0 *field_40;
} struct_1;

typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

int JoystickState_GetDir(struct_1 *a0)
{
    if (a0->field_40)
        return a0->field_40->field_10;
    sub_f7db74();
}
```

## `JoystickState.GetDir4` — RVA `0xc60d68`

- Decompiled symbol: `JoystickState_GetDir4`
- Metadata signature: `public Dir GetDir4() { }`
- Native interval: `28` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[72];
    struct struct_0 *field_48;
} struct_1;

typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

int JoystickState_GetDir4(struct_1 *a0)
{
    if (a0->field_48)
        return a0->field_48->field_10;
    sub_f7db74();
}
```

## `JoystickState.GetDir8` — RVA `0xc60d84`

- Decompiled symbol: `JoystickState_GetDir8`
- Metadata signature: `public Dir GetDir8() { }`
- Native interval: `28` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[80];
    struct struct_0 *field_50;
} struct_1;

typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

int JoystickState_GetDir8(struct_1 *a0)
{
    if (a0->field_50)
        return a0->field_50->field_10;
    sub_f7db74();
}
```

## `JoystickState.JustPressedDir` — RVA `0xc60da0`

- Decompiled symbol: `JoystickState_JustPressedDir`
- Metadata signature: `public bool JustPressedDir(Dir dir) { }`
- Native interval: `28` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[64];
    struct struct_0 *field_40;
} struct_0;

typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

unsigned long long JoystickState_JustPressedDir(struct_0 *a0, unsigned int a1)
{
    unsigned long long v0;  // x0

    if (a0->field_40)
    {
        v0 = DirectionState__JustPressed(a0->field_40, a1);
        return DirectionState__JustPressed(a0->field_40, a1);
    }
    sub_f7db74(0);
}
```

## `JoystickState.JustPressedDir4` — RVA `0xc60dbc`

- Decompiled symbol: `JoystickState_JustPressedDir4`
- Metadata signature: `public bool JustPressedDir4(Dir dir) { }`
- Native interval: `28` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[72];
    struct struct_0 *field_48;
} struct_0;

typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

unsigned long long JoystickState_JustPressedDir4(struct_0 *a0, unsigned int a1)
{
    unsigned long long v0;  // x0

    if (a0->field_48)
    {
        v0 = DirectionState__JustPressed(a0->field_48, a1);
        return DirectionState__JustPressed(a0->field_48, a1);
    }
    sub_f7db74(0);
}
```

## `JoystickState.JustPressedDir8` — RVA `0xc60dd8`

- Decompiled symbol: `JoystickState_JustPressedDir8`
- Metadata signature: `public bool JustPressedDir8(Dir dir) { }`
- Native interval: `28` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[80];
    struct struct_0 *field_50;
} struct_0;

typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

unsigned long long JoystickState_JustPressedDir8(struct_0 *a0, unsigned int a1)
{
    unsigned long long v0;  // x0

    if (a0->field_50)
    {
        v0 = DirectionState__JustPressed(a0->field_50, a1);
        return DirectionState__JustPressed(a0->field_50, a1);
    }
    sub_f7db74(0);
}
```

## `JoystickState.JustReleasedDir` — RVA `0xc60df4`

- Decompiled symbol: `JoystickState_JustReleasedDir`
- Metadata signature: `public bool JustReleasedDir(Dir dir) { }`
- Native interval: `28` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[64];
    struct struct_0 *field_40;
} struct_0;

typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

unsigned long long JoystickState_JustReleasedDir(struct_0 *a0, unsigned int a1)
{
    unsigned long long v0;  // x0

    if (a0->field_40)
    {
        v0 = DirectionState__JustReleased(a0->field_40, a1);
        return DirectionState__JustReleased(a0->field_40, a1);
    }
    sub_f7db74(0);
}
```

## `JoystickState.JustReleasedDir4` — RVA `0xc60e10`

- Decompiled symbol: `JoystickState_JustReleasedDir4`
- Metadata signature: `public bool JustReleasedDir4(Dir dir) { }`
- Native interval: `28` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[72];
    struct struct_0 *field_48;
} struct_0;

typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

unsigned long long JoystickState_JustReleasedDir4(struct_0 *a0, unsigned int a1)
{
    unsigned long long v0;  // x0

    if (a0->field_48)
    {
        v0 = DirectionState__JustReleased(a0->field_48, a1);
        return DirectionState__JustReleased(a0->field_48, a1);
    }
    sub_f7db74(0);
}
```

## `JoystickState.JustReleasedDir8` — RVA `0xc60e2c`

- Decompiled symbol: `JoystickState_JustReleasedDir8`
- Metadata signature: `public bool JustReleasedDir8(Dir dir) { }`
- Native interval: `28` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[80];
    struct struct_0 *field_50;
} struct_0;

typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

unsigned long long JoystickState_JustReleasedDir8(struct_0 *a0, unsigned int a1)
{
    unsigned long long v0;  // x0

    if (a0->field_50)
    {
        v0 = DirectionState__JustReleased(a0->field_50, a1);
        return DirectionState__JustReleased(a0->field_50, a1);
    }
    sub_f7db74(0);
}
```

## `JoystickState.SetConfig` — RVA `0xc60e48`

- Decompiled symbol: `JoystickState_SetConfig`
- Metadata signature: `public void SetConfig(JoystickConfig config) { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned long long field_10;
} struct_0;

long long JoystickState_SetConfig(struct_0 *ptr, unsigned long a1)
{
    long long v0;  // x0

    ptr->field_10 = a1;
    v0 = sub_f7d8d0();
    return sub_f7d8d0();
}
```

## `JoystickState.ApplyUnclampedVec` — RVA `0xc60e50`

- Decompiled symbol: `JoystickState_ApplyUnclampedVec`
- Metadata signature: `public void ApplyUnclampedVec(Vector2 v) { }`
- Native interval: `116` bytes
- Result: `pseudocode`
- Heuristic layout hint: `JoystickState_Recovered` matched 2 offsets against `JoystickState` metadata (confidence 0.67).

```c
typedef struct JoystickState_Recovered {
    char padding_0[16];
    struct struct_0 *config;
    char padding_18[72];
    unsigned int nextFramePos;
    unsigned int field_64;
} JoystickState_Recovered;

typedef struct struct_0 {
    char padding_0[56];
    unsigned int field_38;
} struct_0;

long long JoystickState_ApplyUnclampedVec(struct_1 *ptr)
{
    unsigned int v0;  // s1
    long long v1;  // x0

    if (ptr->field_10)
    {
        if (ptr->field_10->field_38)
            CFUtils__ClampInsideUnitSquare();
        else
            CFUtils__ClampInsideUnitCircle();
        CFUtils__ApplyDeltaInput();
        v0 = ptr->field_64;
        ptr->field_60 = ptr->field_60;
        v1 = CFUtils__ApplyDeltaInput();
        ptr->field_64 = v0;
        return v1;
    }
    sub_f7db74();
}
```

## `JoystickState.ApplyClampedVec` — RVA `0xc60ec4`

- Decompiled symbol: `JoystickState_ApplyClampedVec`
- Metadata signature: `public void ApplyClampedVec(Vector2 v, JoystickConfig.ClampMode clampMode) { }`
- Native interval: `136` bytes
- Result: `pseudocode`
- Heuristic layout hint: `JoystickState_Recovered` matched 2 offsets against `JoystickState` metadata (confidence 0.67).

```c
typedef struct JoystickState_Recovered {
    char padding_0[16];
    struct struct_0 *config;
    char padding_18[72];
    unsigned int nextFramePos;
    unsigned int field_64;
} JoystickState_Recovered;

typedef struct struct_0 {
    char padding_0[56];
    unsigned int field_38;
} struct_0;

long long JoystickState_ApplyClampedVec(struct_1 *ptr, unsigned int a1)
{
    unsigned int v0;  // s1
    long long v1;  // x0

    if (ptr->field_10)
    {
        if (ptr->field_10->field_38 != a1)
        {
            if (ptr->field_10->field_38)
                CFUtils__CircularToSquareJoystickVec();
            else
                CFUtils__SquareToCircularJoystickVec();
        }
        CFUtils__ApplyDeltaInput();
        v0 = ptr->field_64;
        ptr->field_60 = ptr->field_60;
        v1 = CFUtils__ApplyDeltaInput();
        ptr->field_64 = v0;
        return v1;
    }
    sub_f7db74();
}
```

## `JoystickState.ApplyDir` — RVA `0xc60f4c`

- Decompiled symbol: `JoystickState_ApplyDir`
- Metadata signature: `public void ApplyDir(Dir dir) { }`
- Native interval: `212` bytes
- Result: `pseudocode`

```c
void JoystickState_ApplyDir(char *ptr, unsigned int flag)
{
    unsigned int v0;  // w8
    unsigned int v1;  // w9
    unsigned int v8;  // w10
    char v3[108];  // x11
    char v4[108];  // x11
    unsigned int v5;  // w11
    unsigned int v6;  // w11
    unsigned int v7;  // w12

    v0 = 0;
    v1 = 1;
    if (flag == 1 || flag == 8)
    {
LABEL_1060f68:
        switch (flag)
        {
        case 6:
LABEL_1060f70:
            v8 = 1;
            break;
        case 4:
            v8 = 1;
LABEL_1060f80:
            if (flag == 7)
            {
                v5 = 1;
                goto LABEL_1060fcc;
            }
            break;
        default:
            v8 = 0;
            goto LABEL_1060f80;
        }
    }
    else
    {
        if (flag == 1)
            v3 = NULL;
        else
            v3 = ptr;
        v4 = v3;
        if (flag != 2)
            v1 = 0;
        else
            v1 = 1;
        if ((flag & 4294967294) == 2)
        {
            v8 = 0;
            v0 = 1;
            ptr = v4;
        }
        else
        {
            if (flag != 4)
                v0 = 0;
            else
                v0 = 1;
            if (flag == 5)
                goto LABEL_1060f70;
            goto LABEL_1060f68;
        }
    }
    if (flag != 8)
        v6 = 0;
    else
        v6 = 1;
    if (flag != 6)
        v7 = 0;
    else
        v7 = 1;
    v5 = v6 | v7;
LABEL_1060fcc:
    if (ptr)
    {
        if (v1)
            ptr[104] = 1;
        if (v0)
            ptr[105] = 1;
        if (v8)
            ptr[106] = 1;
        if (!v5)
            return;
        ptr[107] = 1;
        return;
    }
    sub_f7db74();
}
```

## `JoystickState.ApplyDigital` — RVA `0xc61020`

- Decompiled symbol: `JoystickState_ApplyDigital`
- Metadata signature: `public void ApplyDigital(bool digiU, bool digiR, bool digiD, bool digiL) { }`
- Native interval: `68` bytes
- Result: `pseudocode`

```c
char [108] JoystickState_ApplyDigital(char *ptr, unsigned long a1, unsigned long a2, unsigned long a3, unsigned long a4)
{
    if (!((char)a1 & 1))
    {
        if ((a2 & 1))
            goto LABEL_1061040;
LABEL_1061028:
        if ((a3 & 1))
            goto LABEL_106104c;
LABEL_106102c:
        if (!((char)a4 & 1))
            return ptr;
    }
    else
    {
        ptr[104] = 1;
        if (!(a2 & 1))
            goto LABEL_1061028;
LABEL_1061040:
        ptr[105] = 1;
        if (!(a3 & 1))
            goto LABEL_106102c;
LABEL_106104c:
        ptr[106] = 1;
        if (!((char)a4 & 1))
            return ptr;
    }
    ptr[107] = 1;
    return ptr;
}
```

## `JoystickState.ApplyState` — RVA `0xc61064`

- Decompiled symbol: `JoystickState_ApplyState`
- Metadata signature: `public void ApplyState(JoystickState state) { }`
- Native interval: `96` bytes
- Result: `pseudocode`
- Heuristic layout hint: `JoystickState_Recovered` matched 3 offsets against `JoystickState` metadata (confidence 1.00).

```c
typedef struct struct_1 {
    char padding_0[16];
    struct struct_0 *field_10;
} struct_1;

typedef struct struct_0 {
    char padding_0[64];
    unsigned int field_40;
} struct_0;

typedef struct JoystickState_Recovered {
    char padding_0[16];
    struct struct_2 *config;
    char padding_18[48];
    struct struct_3 *dirState4;
    struct struct_3 *dirState8;
} JoystickState_Recovered;

typedef struct struct_3 {
    char padding_0[16];
    unsigned int field_10;
} struct_3;

typedef struct struct_5 {
    char padding_0[16];
    unsigned int field_10;
} struct_5;

typedef struct struct_2 {
    char padding_0[56];
    unsigned int field_38;
} struct_2;

long long JoystickState_ApplyState(struct_1 *a0, struct_4 *ptr)
{
    struct_3 *v0;  // x8
    unsigned long v1;  // x0
    long long v2;  // x0

    if (a0->field_10)
    {
        if (a0->field_10->field_40)
        {
            if (ptr)
            {
                if (a0->field_10->field_40 != 1)
                {
                    v0 = ptr->field_50;
                    if (ptr->field_50)
                    {
                        v1 = (unsigned long long)JoystickState__ApplyDir(a0, v0->field_10);
                        return (unsigned long long)JoystickState__ApplyDir(a0, v0->field_10);
                    }
                }
                else if (ptr->field_48)
                {
                    v1 = (unsigned long long)JoystickState__ApplyDir(a0, ptr->field_48->field_10);
                    return (unsigned long long)JoystickState__ApplyDir(a0, ptr->field_48->field_10);
                }
            }
        }
        else
        {
            if (ptr && ptr->field_10)
            {
                v2 = JoystickState__ApplyClampedVec(a0, ptr->field_10->field_38);
                return JoystickState__ApplyClampedVec(a0, ptr->field_10->field_38);
            }
        }
    }
    sub_f7db74();
}
```

## `JoystickState.Update` — RVA `0xc610c4`

- Decompiled symbol: `JoystickState_Update`
- Metadata signature: `public void Update() { }`
- Native interval: `1576` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: Decompiler produced no C-like text

```c
// 0x10610c4: str d14, [sp, #-0x80]!
// 0x10610c8: stp d13, d12, [sp, #8]
// 0x10610cc: stp d11, d10, [sp, #0x18]
// 0x10610d0: stp d9, d8, [sp, #0x28]
// 0x10610d4: str x30, [sp, #0x38]
// 0x10610d8: stp x26, x25, [sp, #0x40]
// 0x10610dc: stp x24, x23, [sp, #0x50]
// 0x10610e0: stp x22, x21, [sp, #0x60]
// 0x10610e4: stp x20, x19, [sp, #0x70]
// 0x10610e8: mov x19, x0
// 0x10610ec: ldrb w0, [x0, #0x68]
// 0x10610f0: ldrb w1, [x19, #0x69]
// 0x10610f4: ldrb w2, [x19, #0x6a]
// 0x10610f8: ldrb w3, [x19, #0x6b]
// 0x10610fc: mov x4, xzr
// 0x1061100: bl #0x1059bc4
// 0x1061104: ldr x8, [x19, #0x10]
// 0x1061108: cbz x8, #0x10616e8
// 0x106110c: ldp s0, s1, [x19, #0x6c]
// 0x1061110: mov w1, w0
// 0x1061114: mov x0, x8
// 0x1061118: bl #0x1060a0c
// 0x106111c: mov v2.16b, v0.16b
// 0x1061120: ldr s0, [x19, #0x60]
// 0x1061124: stp s2, s1, [x19, #0x6c]
// 0x1061128: mov v1.16b, v2.16b
// 0x106112c: mov x0, xzr
// 0x1061130: bl #0x1058484
// 0x1061134: ldr s2, [x19, #0x64]
// 0x1061138: ldr s1, [x19, #0x70]
// 0x106113c: str s0, [x19, #0x2c]
// 0x1061140: mov x0, xzr
// 0x1061144: mov v0.16b, v2.16b
// 0x1061148: bl #0x1058484
// 0x106114c: str s0, [x19, #0x30]
// 0x1061150: adrp x22, #0x1fab000
// 0x1061154: ldrb w8, [x22, #0x1e0]
// 0x1061158: cbnz w8, #0x1061170
// 0x106115c: adrp x0, #0x1e8c000
// 0x1061160: ldr x0, [x0, #0x138]
// 0x1061164: bl #0xf7d92c
// 0x1061168: mov w8, #1
// 0x106116c: strb w8, [x22, #0x1e0]
// 0x1061170: adrp x23, #0x1e8c000
// 0x1061174: ldr x23, [x23, #0x138]
// 0x1061178: ldr x0, [x19, #0x10]
// 0x106117c: ldr x8, [x23]
// 0x1061180: ldr x8, [x8, #0xb8]
// 0x1061184: ldr d0, [x8]
// 0x1061188: str wzr, [x19, #0x68]
// 0x106118c: str d0, [x19, #0x60]
// 0x1061190: cbz x0, #0x10616e8
// 0x1061194: ldrb w8, [x0, #0x50]
// 0x1061198: cbz w8, #0x10611a0
// 0x106119c: str wzr, [x19, #0x2c]
// 0x10611a0: ldrb w8, [x0, #0x51]
// 0x10611a4: cbz w8, #0x10611b4
// 0x10611a8: fmov s10, wzr
// 0x10611ac: str wzr, [x19, #0x30]
// 0x10611b0: b #0x10611b8
// 0x10611b4: ldr s10, [x19, #0x30]
// 0x10611b8: ldr s11, [x19, #0x2c]
// 0x10611bc: mov v1.16b, v10.16b
// 0x10611c0: mov v0.16b, v11.16b
// 0x10611c4: bl #0x1060aa8
// 0x10611c8: stp s0, s1, [x19, #0x2c]
// 0x10611cc: adrp x24, #0x1fab000
// 0x10611d0: ldrb w8, [x24, #0x243]
// 0x10611d4: cbz w8, #0x10611e4
// 0x10611d8: mov v8.16b, v0.16b
// 0x10611dc: mov v9.16b, v1.16b
// 0x10611e0: b #0x10611fc
// 0x10611e4: adrp x0, #0x1e8c000
// 0x10611e8: ldr x0, [x0, #0xa60]
// 0x10611ec: bl #0xf7d92c
// 0x10611f0: mov w8, #1
// 0x10611f4: strb w8, [x24, #0x243]
// 0x10611f8: ldp s8, s9, [x19, #0x2c]
// 0x10611fc: adrp x25, #0x1e8c000
// 0x1061200: ldr x25, [x25, #0xa60]
// 0x1061204: mov v12.16b, v9.16b
// 0x1061208: mov v13.16b, v8.16b
// 0x106120c: ldr x0, [x25]
// 0x1061210: ldr w8, [x0, #0xe0]
// 0x1061214: cbnz w8, #0x1061220
// 0x1061218: bl #0xf7da5c
// 0x106121c: ldp s13, s12, [x19, #0x2c]
// 0x1061220: adrp x8, #0x832000
// 0x1061224: ldr s0, [x8, #0x2e8]
// 0x1061228: fmul s1, s13, s13
// 0x106122c: fmul s2, s12, s12
// 0x1061230: fadd s14, s1, s2
// 0x1061234: fcmp s14, s0
// 0x1061238: b.pl #0x106124c
// 0x106123c: ldr s9, [x19, #0x20]
// 0x1061240: str wzr, [x19, #0x18]
// 0x1061244: fmov s8, wzr
// 0x1061248: b #0x10612f4
// 0x106124c: ldrb w8, [x24, #0x243]
// 0x1061250: fmul s8, s8, s8
// 0x1061254: fmul s9, s9, s9
// 0x1061258: cbnz w8, #0x1061270
// 0x106125c: adrp x0, #0x1e8c000
// 0x1061260: ldr x0, [x0, #0xa60]
// 0x1061264: bl #0xf7d92c
// 0x1061268: mov w8, #1
// 0x106126c: strb w8, [x24, #0x243]
// 0x1061270: ldr x0, [x25]
// 0x1061274: fadd s8, s8, s9
// 0x1061278: ldr w8, [x0, #0xe0]
// 0x106127c: cbnz w8, #0x1061284
// 0x1061280: bl #0xf7da5c
// 0x1061284: adrp x8, #0x832000
// 0x1061288: ldr s0, [x8, #0x41c]
// 0x106128c: fsqrt s1, s14
// 0x1061290: fsqrt s8, s8
// 0x1061294: fcmp s1, s0
// 0x1061298: b.le #0x10612a8
// 0x106129c: fdiv s0, s13, s1
// 0x10612a0: fdiv s1, s12, s1
// 0x10612a4: b #0x10612d0
// 0x10612a8: ldrb w8, [x22, #0x1e0]
// 0x10612ac: cbnz w8, #0x10612c4
// 0x10612b0: adrp x0, #0x1e8c000
// 0x10612b4: ldr x0, [x0, #0x138]
// 0x10612b8: bl #0xf7d92c
// 0x10612bc: mov w8, #1
// 0x10612c0: strb w8, [x22, #0x1e0]
// 0x10612c4: ldr x8, [x23]
// 0x10612c8: ldr x8, [x8, #0xb8]
// 0x10612cc: ldp s0, s1, [x8]
// 0x10612d0: stp s0, s1, [x19, #0x34]
// 0x10612d4: str s8, [x19, #0x18]
// 0x10612d8: bl #0x1db0c90
// 0x10612dc: adrp x8, #0x832000
// 0x10612e0: ldr s1, [x8, #0x554]
// 0x10612e4: mov x0, xzr
// 0x10612e8: fmul s0, s0, s1
// 0x10612ec: bl #0x10592b8
// 0x10612f0: mov v9.16b, v0.16b
// 0x10612f4: ldr x9, [x19, #0x48]
// 0x10612f8: cbz x9, #0x10616e8
// 0x10612fc: ldr x10, [x19, #0x50]
// 0x1061300: cbz x10, #0x10616e8
// 0x1061304: ldr x8, [x19, #0x10]
// 0x1061308: cbz x8, #0x10616e8
// 0x106130c: ldr w11, [x8, #0x4c]
// 0x1061310: mov v12.16b, v8.16b
// 0x1061314: mov v0.16b, v8.16b
// 0x1061318: cbnz w11, #0x1061358
// 0x106131c: adrp x11, #0x832000
// 0x1061320: ldr s1, [x11, #0x410]
// 0x1061324: fabs s0, s11
// 0x1061328: fabs s2, s10
// 0x106132c: fcmp s0, s2
// 0x1061330: fcsel s0, s0, s2, gt
// 0x1061334: fmul s2, s11, s1
// 0x1061338: fmul s1, s10, s1
// 0x106133c: fadd s3, s2, s1
// 0x1061340: fabs s3, s3
// 0x1061344: fcmp s0, s3
// 0x1061348: fcsel s3, s0, s3, gt
// 0x106134c: fabd s1, s2, s1
// 0x1061350: fcmp s3, s1
// 0x1061354: fcsel s12, s3, s1, gt
// 0x1061358: adrp x11, #0x832000
// 0x106135c: ldr s1, [x11, #0x534]
// 0x1061360: ldr w20, [x10, #0x10]
// 0x1061364: ldr w9, [x9, #0x10]
// 0x1061368: mov x26, x19
// 0x106136c: fcmp s8, s1
// 0x1061370: b.pl #0x1061384
// 0x1061374: str wzr, [x26, #0x58]!
// 0x1061378: str wzr, [x26, #4]
// 0x106137c: ldr s1, [x8, #0x1c]
// 0x1061380: b #0x1061390
// 0x1061384: ldr w1, [x26, #0x58]!
// 0x1061388: ldr s1, [x8, #0x1c]
// 0x106138c: cbnz w1, #0x10613a4
// 0x1061390: ldr s2, [x8, #0x20]
// 0x1061394: mov w1, wzr
// 0x1061398: fadd s1, s1, s2
// 0x106139c: fmov s2, #0.50000000
// 0x10613a0: fmul s1, s1, s2
// 0x10613a4: fcmp s0, s1
// 0x10613a8: b.le #0x10613d0
// 0x10613ac: ldr s1, [x8, #0x48]
// 0x10613b0: mov v0.16b, v9.16b
// 0x10613b4: mov w0, wzr
// 0x10613b8: mov x2, xzr
// 0x10613bc: bl #0x105958c
// 0x10613c0: ldr x8, [x19, #0x10]
// 0x10613c4: cbz x8, #0x10616e8
// 0x10613c8: mov w21, w0
// 0x10613cc: b #0x10613dc
// 0x10613d0: ldr s1, [x8, #0x20]
// 0x10613d4: fcmp s0, s1
// 0x10613d8: csel w21, w9, wzr, gt
// 0x10613dc: ldr w1, [x19, #0x5c]
// 0x10613e0: ldr s0, [x8, #0x1c]
// 0x10613e4: cbnz w1, #0x10613f8
// 0x10613e8: ldr s1, [x8, #0x20]
// 0x10613ec: fadd s0, s0, s1
// 0x10613f0: fmov s1, #0.50000000
// 0x10613f4: fmul s0, s0, s1
// 0x10613f8: fcmp s12, s0
// 0x10613fc: b.le #0x106141c
// 0x1061400: ldr s1, [x8, #0x48]
// 0x1061404: mov w0, #1
// 0x1061408: mov v0.16b, v9.16b
// 0x106140c: mov x2, xzr
// 0x1061410: bl #0x105958c
// 0x1061414: mov w20, w0
// 0x1061418: b #0x106142c
// 0x106141c: ldr s0, [x8, #0x20]
// 0x1061420: fcmp s12, s0
// 0x1061424: b.gt #0x106142c
// 0x1061428: mov w20, wzr
// 0x106142c: cbz w21, #0x1061434
// 0x1061430: str w21, [x26]
// 0x1061434: cbz w20, #0x106143c
// 0x1061438: str w20, [x19, #0x5c]
// 0x106143c: ldr x0, [x19, #0x40]
// 0x1061440: cbz x0, #0x10616e8
// 0x1061444: mov x1, xzr
// 0x1061448: bl #0x105aef8
// 0x106144c: ldr x0, [x19, #0x48]
// 0x1061450: cbz x0, #0x10616e8
// 0x1061454: mov x1, xzr
// 0x1061458: bl #0x105aef8
// 0x106145c: ldr x0, [x19, #0x50]
// 0x1061460: cbz x0, #0x10616e8
// 0x1061464: mov x1, xzr
// 0x1061468: bl #0x105aef8
// 0x106146c: ldr x8, [x19, #0x10]
// 0x1061470: cbz x8, #0x10616e8
// 0x1061474: ldr x0, [x19, #0x48]
// 0x1061478: cbz x0, #0x10616e8
// 0x106147c: ldr w2, [x8, #0x44]
// 0x1061480: mov w1, w21
// 0x1061484: mov x3, xzr
// 0x1061488: bl #0x105af0c
// 0x106148c: ldr x8, [x19, #0x10]
// 0x1061490: cbz x8, #0x10616e8
// 0x1061494: ldr x0, [x19, #0x50]
// 0x1061498: cbz x0, #0x10616e8
// 0x106149c: ldr w2, [x8, #0x44]
// 0x10614a0: mov w1, w20
// 0x10614a4: mov x3, xzr
// 0x10614a8: bl #0x105af0c
// 0x10614ac: ldr x8, [x19, #0x10]
// 0x10614b0: cbz x8, #0x10616e8
// 0x10614b4: ldr w9, [x8, #0x40]
// 0x10614b8: ldr x0, [x19, #0x40]
// 0x10614bc: cmp w9, #1
// 0x10614c0: b.ne #0x10614d0
// 0x10614c4: ldr x9, [x19, #0x48]
// 0x10614c8: cbnz x9, #0x10614d8
// 0x10614cc: b #0x10616e8
// 0x10614d0: ldr x9, [x19, #0x50]
// 0x10614d4: cbz x9, #0x10616e8
// 0x10614d8: cbz x0, #0x10616e8
// 0x10614dc: ldr w2, [x8, #0x44]
// 0x10614e0: ldr w1, [x9, #0x10]
// 0x10614e4: mov x3, xzr
// 0x10614e8: bl #0x105af0c
// 0x10614ec: ldr x0, [x19, #0x10]
// 0x10614f0: cbz x0, #0x10616e8
// 0x10614f4: ldr w8, [x0, #0x40]
// 0x10614f8: cbz w8, #0x10615c0
// 0x10614fc: sub w8, w8, #1
// 0x1061500: cmp w8, #1
// 0x1061504: b.hi #0x10616b8
// 0x1061508: ldr x8, [x19, #0x40]
// 0x106150c: cbz x8, #0x10616e8
// 0x1061510: ldr w9, [x0, #0x38]
// 0x1061514: ldr w0, [x8, #0x10]
// 0x1061518: mov x2, xzr
// 0x106151c: cmp w9, #0
// 0x1061520: cset w1, eq
// 0x1061524: bl #0x10598b4
// 0x1061528: ldr x8, [x19, #0x40]
// 0x106152c: stp s0, s1, [x19, #0x24]
// 0x1061530: cbz x8, #0x10616e8
// 0x1061534: ldr w0, [x8, #0x10]
// 0x1061538: mov x1, xzr
// 0x106153c: bl #0x1059450
// 0x1061540: ldr x8, [x19, #0x40]
// 0x1061544: str s0, [x19, #0x1c]
// 0x1061548: cbz x8, #0x10616e8
// 0x106154c: ldr w8, [x8, #0x10]
// 0x1061550: fmov s0, #1.00000000
// 0x1061554: fmov s1, wzr
// 0x1061558: cmp w8, #0
// 0x106155c: fcsel s0, s1, s0, eq
// 0x1061560: str s0, [x19, #0x18]
// 0x1061564: cbz w8, #0x10616b8
// 0x1061568: ldrb w8, [x24, #0x243]
// 0x106156c: ldur d8, [x19, #0x24]
// 0x1061570: cbnz w8, #0x1061588
// 0x1061574: adrp x0, #0x1e8c000
// 0x1061578: ldr x0, [x0, #0xa60]
// 0x106157c: bl #0xf7d92c
// 0x1061580: mov w8, #1
// 0x1061584: strb w8, [x24, #0x243]
// 0x1061588: ldr x0, [x25]
// 0x106158c: ldr w8, [x0, #0xe0]
// 0x1061590: cbnz w8, #0x1061598
// 0x1061594: bl #0xf7da5c
// 0x1061598: adrp x8, #0x832000
// 0x106159c: ldr s1, [x8, #0x41c]
// 0x10615a0: fmul v0.2s, v8.2s, v8.2s
// 0x10615a4: faddp s0, v0.2s
// 0x10615a8: fsqrt s0, s0
// 0x10615ac: fcmp s0, s1
// 0x10615b0: b.le #0x106168c
// 0x10615b4: dup v0.2s, v0.s[0]
// 0x10615b8: fdiv v0.2s, v8.2s, v0.2s
// 0x10615bc: b #0x10616b4
// 0x10615c0: str s9, [x19, #0x1c]
// 0x10615c4: ldrb w8, [x0, #0x3c]
// 0x10615c8: cbz w8, #0x1061644
// 0x10615cc: ldr s0, [x19, #0x2c]
// 0x10615d0: mov x1, xzr
// 0x10615d4: bl #0x10574f8
// 0x10615d8: ldr x0, [x19, #0x10]
// 0x10615dc: str s0, [x19, #0x24]
// 0x10615e0: cbz x0, #0x10616e8
// 0x10615e4: ldr s0, [x19, #0x30]
// 0x10615e8: mov x1, xzr
// 0x10615ec: bl #0x10574f8
// 0x10615f0: str s0, [x19, #0x28]
// 0x10615f4: ldrb w8, [x24, #0x243]
// 0x10615f8: mov v8.16b, v0.16b
// 0x10615fc: cbnz w8, #0x1061618
// 0x1061600: adrp x0, #0x1e8c000
// 0x1061604: ldr x0, [x0, #0xa60]
// 0x1061608: bl #0xf7d92c
// 0x106160c: mov w8, #1
// 0x1061610: strb w8, [x24, #0x243]
// 0x1061614: ldr s8, [x19, #0x28]
// 0x1061618: ldr x0, [x25]
// 0x106161c: ldr s9, [x19, #0x24]
// 0x1061620: ldr w8, [x0, #0xe0]
// 0x1061624: cbnz w8, #0x106162c
// 0x1061628: bl #0xf7da5c
// 0x106162c: fmul s0, s9, s9
// 0x1061630: fmul s1, s8, s8
// 0x1061634: fadd s0, s0, s1
// 0x1061638: fsqrt s0, s0
// 0x106163c: str s0, [x19, #0x18]
// 0x1061640: b #0x10616b8
// 0x1061644: mov v0.16b, v8.16b
// 0x1061648: mov x1, xzr
// 0x106164c: bl #0x10574f8
// 0x1061650: mov v1.16b, v0.16b
// 0x1061654: ldp s0, s2, [x19, #0x34]
// 0x1061658: ldr x8, [x19, #0x10]
// 0x106165c: str s1, [x19, #0x18]
// 0x1061660: fmul s0, s1, s0
// 0x1061664: fmul s1, s1, s2
// 0x1061668: stp s0, s1, [x19, #0x24]
// 0x106166c: cbz x8, #0x10616e8
// 0x1061670: ldr w8, [x8, #0x38]
// 0x1061674: cmp w8, #1
// 0x1061678: b.ne #0x10616b8
// 0x106167c: mov x0, xzr
// 0x1061680: bl #0x1059c38
// 0x1061684: stp s0, s1, [x19, #0x24]
// 0x1061688: b #0x10616b8
// 0x106168c: ldrb w8, [x22, #0x1e0]
// 0x1061690: cbnz w8, #0x10616a8
// 0x1061694: adrp x0, #0x1e8c000
// 0x1061698: ldr x0, [x0, #0x138]
// 0x106169c: bl #0xf7d92c
// 0x10616a0: mov w8, #1
// 0x10616a4: strb w8, [x22, #0x1e0]
// 0x10616a8: ldr x8, [x23]
// 0x10616ac: ldr x8, [x8, #0xb8]
// 0x10616b0: ldr d0, [x8]
// 0x10616b4: stur d0, [x19, #0x34]
// 0x10616b8: ldr s0, [x19, #0x1c]
// 0x10616bc: ldp x22, x21, [sp, #0x60]
// 0x10616c0: ldp x24, x23, [sp, #0x50]
// 0x10616c4: ldp x26, x25, [sp, #0x40]
// 0x10616c8: str s0, [x19, #0x20]
// 0x10616cc: ldp x20, x19, [sp, #0x70]
// 0x10616d0: ldr x30, [sp, #0x38]
// 0x10616d4: ldp d9, d8, [sp, #0x28]
// 0x10616d8: ldp d11, d10, [sp, #0x18]
// 0x10616dc: ldp d13, d12, [sp, #8]
// 0x10616e0: ldr d14, [sp], #0x80
// 0x10616e4: ret
// 0x10616e8: bl #0xf7db74
```
