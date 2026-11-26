# Native pseudocode: SuperTouchZone.FingerState

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `SuperTouchZone.FingerState.ctor` — RVA `0xc4943c`

- Decompiled symbol: `SuperTouchZone_FingerState_ctor`
- Metadata signature: `public void .ctor(SuperTouchZone zone) { }`
- Native interval: `200` bytes
- Result: `pseudocode`
- Heuristic layout hint: `SuperTouchZone_FingerState_Recovered` matched 2 offsets against `SuperTouchZone.FingerState` metadata (confidence 1.00).

```c
typedef struct SuperTouchZone_FingerState_Recovered {
    char padding_0[16];
    long long zone;
    unsigned long long touchObj;
} SuperTouchZone_FingerState_Recovered;

extern long long g_1ef1e08;
extern char g_1fab23d;

long long SuperTouchZone_FingerState_ctor(struct_0 *a0, long long a1)
{
    unsigned long long v5;  // x30
    unsigned long long v6;  // x22
    unsigned long long v7;  // x21
    unsigned long long v8;  // x20
    unsigned long long v9;  // x19
    struct_0 *ptr;  // x0
    struct_0 *p;  // x0
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
    if (!(g_1fab23d & 1))
    {
        sub_f7d92c(&g_1ef1e08);
        g_1fab23d = 1;
    }
    Object__ctor(a0, 0);
    ptr = a0;
    ptr->field_10 = a1;
    sub_f7d8d0((struct SuperTouchZone_FingerState_Recovered *)&ptr->field_10, a1);
    p = a0;
    p->field_18 = 0;
    sub_f7d8d0((struct SuperTouchZone_FingerState_Recovered *)&p->field_18, 0);
    TouchGestureBasicState__ctor(sub_f7db70(g_1ef1e08), 0); /* do not return */
}
```

## `SuperTouchZone.FingerState.Reset` — RVA `0xc49b48`

- Decompiled symbol: `SuperTouchZone_FingerState_Reset`
- Metadata signature: `public void Reset() { }`
- Native interval: `56` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    char padding_0[40];
    struct struct_3 *field_28;
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

void SuperTouchZone_FingerState_Reset(struct_2 *ptr, unsigned long a1)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    struct_0 **v4;  // x0
    unsigned long long v5;  // x1
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    v4 = ptr->field_28;
    if (!ptr->field_28)
        sub_f7db74(0);
    v5 = ptr->field_28->field_0->field_180;
    ptr->field_28->field_0->field_178();
}
```

## `SuperTouchZone.FingerState.Update` — RVA `0xc4b078`

- Decompiled symbol: `SuperTouchZone_FingerState_Update`
- Metadata signature: `public void Update() { }`
- Native interval: `56` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    char padding_0[40];
    struct struct_3 *field_28;
} struct_2;

typedef struct struct_0 {
    char padding_0[392];
    struct struct_1 *field_188;
    unsigned long long field_190;
} struct_0;

typedef struct struct_3 {
    struct struct_0 *field_0;
} struct_3;

typedef struct struct_1 {
    unsigned long long field_0;
} struct_1;

void SuperTouchZone_FingerState_Update(struct_2 *ptr)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    struct_0 **v4;  // x0
    unsigned long long v5;  // x1
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    v4 = ptr->field_28;
    if (!ptr->field_28)
        sub_f7db74(0);
    v5 = ptr->field_28->field_0->field_190;
    ptr->field_28->field_0->field_188();
}
```

## `SuperTouchZone.FingerState.OnTouchStart` — RVA `0xc4bed8`

- Decompiled symbol: `SuperTouchZone_FingerState_OnTouchStart`
- Metadata signature: `public bool OnTouchStart(TouchObject touchObj, float delay, TouchControl.TouchStartType touchStartType) { }`
- Native interval: `280` bytes
- Result: `pseudocode`
- Heuristic layout hint: `SuperTouchZone_FingerState_Recovered` matched 4 offsets against `SuperTouchZone.FingerState` metadata (confidence 1.00).

```c
typedef struct SuperTouchZone_FingerState_Recovered {
    char padding_0[16];
    long long zone;
    struct struct_0 *touchObj;
    unsigned int touchStartType;
    char padding_24[4];
    unsigned long long touchScreen;
} SuperTouchZone_FingerState_Recovered;

typedef struct struct_0 {
    char padding_0[48];
    unsigned long long field_30;
} struct_0;

typedef struct struct_2 {
    char padding_0[48];
    long long field_30;
} struct_2;

unsigned long long SuperTouchZone_FingerState_OnTouchStart(struct_1 *ptr, struct_2 *a1, unsigned int a2)
{
    unsigned long long v1;  // d10
    unsigned long v2;  // cc_dep1
    unsigned long v3;  // 4105
    unsigned long v4;  // 4105
    unsigned long long v0;  // [bp-0x50]

    v0 = v1;
    if (!ptr->field_18)
    {
        ptr->field_18 = a1;
        sub_f7d8d0((struct SuperTouchZone_FingerState_Recovered *)&ptr->field_18);
        ptr->field_20 = a2;
        if (a1 && ptr->field_28)
        {
            v2 = a2;
            if (!a2)
            {
                v3 = arm64g_calculate_condition(3, v2, 0, 0);
                if (!((char)v3))
                    goto LABEL_104bf3e;
LABEL_104bf3d:
            }
            else
            {
                v4 = arm64g_calculate_condition(3, v2, 0, 0);
                if ((char)v4)
                    goto LABEL_104bf3d;
LABEL_104bf3e:
            }
            TouchGestureBasicState__OnTouchStart();
            if (ptr->field_10)
                TouchControl__ScreenToOrientedPos(ptr->field_10, a1->field_30, 0); /* do not return */
        }
        sub_f7db74();
    }
    else if (ptr->field_18)
    {
        return 0;
    }
    else
    {
        return 1;
    }
}
```

## `SuperTouchZone.FingerState.OnTouchEnd` — RVA `0xc4c098`

- Decompiled symbol: `SuperTouchZone_FingerState_OnTouchEnd`
- Metadata signature: `public bool OnTouchEnd(TouchObject touchObj, TouchControl.TouchEndType touchEndType) { }`
- Native interval: `184` bytes
- Result: `pseudocode`
- Heuristic layout hint: `SuperTouchZone_FingerState_Recovered` matched 3 offsets against `SuperTouchZone.FingerState` metadata (confidence 1.00).

```c
typedef struct SuperTouchZone_FingerState_Recovered {
    char padding_0[16];
    long long zone;
    struct struct_0 *touchObj;
    char padding_20[8];
    unsigned long long touchScreen;
} SuperTouchZone_FingerState_Recovered;

typedef struct struct_0 {
    char padding_0[48];
    long long field_30;
} struct_0;

long long SuperTouchZone_FingerState_OnTouchEnd(struct_1 *ptr, struct_0 *a1, unsigned int a2)
{
    unsigned long long v6;  // x30
    unsigned long long v7;  // x23
    unsigned long long v8;  // x22
    unsigned long long v9;  // x21
    unsigned long long v10;  // x20
    unsigned long long v11;  // x19
    struct_0 *v12;  // x23
    unsigned int v13;  // w8
    unsigned int v14;  // w9
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
    v12 = ptr->field_18;
    if (v12 == a1 && v12)
    {
        if (a1 && ptr->field_28)
        {
            TouchGestureBasicState__OnTouchEnd();
            if (ptr->field_10)
                TouchControl__ScreenToOrientedPos(ptr->field_10, a1->field_30, 0); /* do not return */
        }
        sub_f7db74();
    }
    if (!v12)
        v13 = 0;
    else
        v13 = 1;
    if (v12 != a1)
        v14 = 0;
    else
        v14 = 1;
    return v14 & v13;
}
```

## `SuperTouchZone.FingerState.OnTouchMove` — RVA `0xc4c1f0`

- Decompiled symbol: `SuperTouchZone_FingerState_OnTouchMove`
- Metadata signature: `public bool OnTouchMove(TouchObject touchObj) { }`
- Native interval: `156` bytes
- Result: `pseudocode`
- Heuristic layout hint: `SuperTouchZone_FingerState_Recovered` matched 3 offsets against `SuperTouchZone.FingerState` metadata (confidence 1.00).

```c
typedef struct SuperTouchZone_FingerState_Recovered {
    char padding_0[16];
    long long zone;
    struct struct_0 *touchObj;
    char padding_20[8];
    struct struct_1 *touchScreen;
} SuperTouchZone_FingerState_Recovered;

typedef struct struct_0 {
    char padding_0[32];
    unsigned long long field_20;
    char padding_28[8];
    long long field_30;
} struct_0;

typedef struct struct_1 {
    char padding_0[176];
    unsigned long long field_b0;
} struct_1;

long long SuperTouchZone_FingerState_OnTouchMove(struct_2 *ptr, struct_0 *index)
{
    unsigned long long v5;  // x30
    unsigned long long v6;  // x22
    unsigned long long v7;  // x21
    unsigned long long v8;  // x20
    unsigned long long v9;  // x19
    struct_0 *v10;  // x21
    unsigned int v11;  // w8
    unsigned int v12;  // w9
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
    v10 = ptr->field_18;
    if (v10 == index && v10)
    {
        if (index && ptr->field_28)
        {
            ptr->field_28->field_b0 = index->field_20;
            if (ptr->field_10)
                TouchControl__ScreenToOrientedPos(ptr->field_10, index->field_30, 0); /* do not return */
        }
        sub_f7db74();
    }
    if (!v10)
        v11 = 0;
    else
        v11 = 1;
    if (v10 != index)
        v12 = 0;
    else
        v12 = 1;
    return v12 & v11;
}
```

## `SuperTouchZone.FingerState.OnTouchPressureChange` — RVA `0xc4c304`

- Decompiled symbol: `SuperTouchZone_FingerState_OnTouchPressureChange`
- Metadata signature: `public bool OnTouchPressureChange(TouchObject touchObj) { }`
- Native interval: `112` bytes
- Result: `pseudocode`
- Heuristic layout hint: `SuperTouchZone_FingerState_Recovered` matched 3 offsets against `SuperTouchZone.FingerState` metadata (confidence 1.00).

```c
typedef struct SuperTouchZone_FingerState_Recovered {
    char padding_0[24];
    unsigned long long touchObj;
    char padding_20[8];
    long long touchScreen;
    long long touchOriented;
} SuperTouchZone_FingerState_Recovered;

long long SuperTouchZone_FingerState_OnTouchPressureChange(struct_0 *ptr, unsigned long long a1)
{
    unsigned long long v4;  // x30
    unsigned long long v5;  // x21
    unsigned long long v6;  // x20
    unsigned long long v7;  // x19
    unsigned long long v8;  // x21
    unsigned int v9;  // w8
    unsigned int v10;  // w9
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x18]
    unsigned long long v2;  // [bp-0x10]
    unsigned long long v3;  // [bp-0x8]

    v0 = v4;
    v1 = v5;
    v2 = v6;
    v3 = v7;
    v8 = ptr->field_18;
    if (v8 == a1 && v8)
    {
        if (a1 && ptr->field_28 && (TouchGestureBasicState__OnTouchPressureChange(ptr->field_28, 0), ptr->field_30))
            TouchGestureBasicState__OnTouchPressureChange(ptr->field_30, 0);
        else
            sub_f7db74();
    }
    if (!v8)
        v9 = 0;
    else
        v9 = 1;
    if (v8 != a1)
        v10 = 0;
    else
        v10 = 1;
    return v10 & v9;
}
```

## `SuperTouchZone.FingerState.ReleaseTouch` — RVA `0xc4c46c`

- Decompiled symbol: `SuperTouchZone_FingerState_ReleaseTouch`
- Metadata signature: `public void ReleaseTouch(bool cancel) { }`
- Native interval: `116` bytes
- Result: `pseudocode`

```c
long long SuperTouchZone_FingerState_ReleaseTouch(long long *ptr, unsigned int a1)
{
    long long v0;  // x0
    unsigned long long v1;  // x0

    if (ptr[3])
    {
        TouchObject__ReleaseControl(ptr[3], ptr[2], a1 & 1, 0);
        ptr[3] = 0;
        sub_f7d8d0(ptr + 3, 0);
    }
    v0 = ptr[5];
    if (v0)
    {
        TouchGestureBasicState__OnTouchEnd(v0, a1 & 1, 0);
        v0 = ptr[6];
        if (v0)
        {
            v1 = TouchGestureBasicState__OnTouchEnd();
            return TouchGestureBasicState__OnTouchEnd();
        }
    }
    sub_f7db74(v0);
}
```

## `SuperTouchZone.FingerState.get_IsActive` — RVA `0xc4cdc4`

- Decompiled symbol: `SuperTouchZone_FingerState_get_IsActive`
- Metadata signature: `public bool get_IsActive() { }`
- Native interval: `16` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

unsigned long long SuperTouchZone_FingerState_get_IsActive(struct_0 *a0)
{
    if (a0->field_18)
        return 1;
    return 0;
}
```

## `SuperTouchZone.FingerState.IsControlledByMouse` — RVA `0xc4cdd4`

- Decompiled symbol: `SuperTouchZone_FingerState_IsControlledByMouse`
- Metadata signature: `public bool IsControlledByMouse() { }`
- Native interval: `32` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[24];
    struct struct_0 *field_18;
} struct_1;

typedef struct struct_0 {
    char padding_0[17];
    char field_11;
} struct_0;

unsigned long long SuperTouchZone_FingerState_IsControlledByMouse(struct_1 *a0)
{
    if (!a0->field_18)
    {
        return 0;
    }
    else if (!a0->field_18->field_11)
    {
        return 0;
    }
    else
    {
        return 1;
    }
}
```
