# Native pseudocode: TouchObject

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `TouchObject.ctor` — RVA `0xc4d03c`

- Decompiled symbol: `TouchObject_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `204` bytes
- Result: `pseudocode`
- Heuristic layout hint: `TouchObject_Recovered` matched 6 offsets against `TouchObject` metadata (confidence 1.00).

```c
typedef struct TouchObject_Recovered {
    char padding_0[16];
    char isOn;
    char padding_11[1];
    char isPressureSensitive;
    char padding_13[1];
    unsigned int normalizedPressure;
    long long controls;
    char padding_20[24];
    char isSwipeOverRestricted;
    char padding_39[7];
    long long swipeOverTargetList;
} TouchObject_Recovered;

extern long long g_1eed8d0;
extern long long g_1ef89e8;
extern char g_1fab281;

long long TouchObject_ctor(struct_0 *p)
{
    long long v0;  // x20
    long long v1;  // x20
    struct_0 *ptr;  // x19
    unsigned long v3;  // x0

    if (!(g_1fab281 & 1))
    {
        sub_f7d92c(&g_1ef89e8);
        sub_f7d92c(&g_1eed8d0);
        g_1fab281 = 1;
    }
    Object__ctor(p, 0);
    v0 = sub_f7db70(g_1eed8d0);
    sub_14a2bd4(v0, 8, g_1ef89e8);
    p->field_18 = v0;
    sub_f7d8d0((struct TouchObject_Recovered *)&p->field_18, v0);
    v1 = sub_f7db70(g_1eed8d0);
    sub_14a2bd4(v1, 16, g_1ef89e8);
    p->field_40 = v1;
    ptr = &p->field_40;
    v3 = sub_f7d8d0(ptr, v1);
    ptr->padding_0[8] = 0;
    ptr->padding_20[16] = 0;
    ptr->padding_20[14] = 0;
    *((unsigned int *)&ptr->padding_20[12]) = 0x3f800000;
    return v3;
}
```

## `TouchObject.ReleaseControl` — RVA `0xc4d288`

- Decompiled symbol: `TouchObject_ReleaseControl`
- Metadata signature: `public void ReleaseControl(TouchControl c, TouchControl.TouchEndType touchEndType) { }`
- Native interval: `204` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[712];
    struct struct_1 *field_2c8;
    unsigned long long field_2d0;
} struct_0;

typedef struct struct_1 {
    unsigned long long field_0;
} struct_1;

extern long long g_1ef8a18;
extern long long g_1ef8a28;
extern char g_1fab287;

long long TouchObject_ReleaseControl(void* ptr, struct_0 **a1, unsigned int a2)
{
    unsigned long v0;  // x0
    struct_0 **v1;  // x0
    void* v2;  // x1
    unsigned long v3;  // x3
    unsigned long v4;  // x2

    if (!(g_1fab287 & 1))
    {
        sub_f7d92c(&g_1ef8a18);
        sub_f7d92c(&g_1ef8a28);
        g_1fab287 = 1;
    }
    v0 = (long long)ptr[24];
    if (v0)
    {
        v0 = sub_14a3dc8(v0, a1, g_1ef8a18);
        if (((char)(v0 >> 31) & 1))
        {
            return v0;
        }
        else if (a1)
        {
            v1 = a1;
            v2 = ptr;
            v3 = *(a1)->field_2d0;
            v4 = a2;
            *(a1)->field_2c8();
        }
    }
    sub_f7db74(v0);
}
```

## `TouchObject.End` — RVA `0xc4d3bc`

- Decompiled symbol: `TouchObject_End`
- Metadata signature: `public void End(bool cancel) { }`
- Native interval: `276` bytes
- Result: `pseudocode`
- Heuristic layout hint: `TouchObject_Recovered` matched 3 offsets against `TouchObject` metadata (confidence 1.00).

```c
typedef struct TouchObject_Recovered {
    char padding_0[16];
    char isOn;
    char padding_11[7];
    struct struct_2 *controls;
    char padding_20[32];
    struct struct_3 *swipeOverTargetList;
} TouchObject_Recovered;

typedef struct struct_8 {
    struct struct_6 *field_0;
    char padding_8[8];
    unsigned long long field_10;
    unsigned int field_18;
    unsigned int field_1c;
} struct_8;

typedef struct struct_5 {
    char padding_0[16];
    unsigned long long field_10;
    unsigned int field_18;
    unsigned int field_1c;
} struct_5;

typedef struct struct_2 {
    struct struct_0 *field_0;
    char padding_8[8];
    long long field_10;
    int field_18;
    unsigned int field_1c;
} struct_2;

typedef struct struct_3 {
    char padding_0[16];
    long long field_10;
    int field_18;
    unsigned int field_1c;
} struct_3;

typedef struct struct_6 {
    char padding_0[712];
    struct struct_7 *field_2c8;
    unsigned long long field_2d0;
} struct_6;

typedef struct struct_0 {
    char padding_0[712];
    struct struct_1 *field_2c8;
    unsigned long long field_2d0;
} struct_0;

typedef struct struct_7 {
    unsigned long long field_0;
} struct_7;

typedef struct struct_1 {
    unsigned long long field_0;
} struct_1;

extern long long g_1ef89f8;
extern long long g_1ef8a30;
extern long long g_1ef8a38;
extern char g_1fab285;

long long TouchObject_End(struct_4 *addr, unsigned int a1, unsigned long a2)
{
    struct_8 *ptr;  // x0
    unsigned int v1;  // w2
    struct_4 *v2;  // x1
    unsigned long v3;  // x2
    unsigned long v4;  // x3
    unsigned int v5;  // w8
    struct_5 *p;  // x8
    unsigned int v7;  // w2
    unsigned int v8;  // w9
    unsigned long long v9;  // x0

    if (!(g_1fab285 & 1))
    {
        sub_f7d92c(&g_1ef89f8);
        sub_f7d92c(&g_1ef8a30);
        sub_f7d92c(&g_1ef8a38);
        g_1fab285 = 1;
    }
    ptr = addr->field_18;
    addr->field_10 = 0;
    if (ptr)
    {
        v1 = ptr->field_18;
        if (v1 > 0)
        {
            ptr = sub_14a30c0();
            if (ptr)
            {
                v2 = addr;
                v3 = a1 & 1;
                v4 = ptr->field_0->field_2d0;
                ptr->field_0->field_2c8();
            }
        }
        else
        {
            v5 = ptr->field_1c;
            ptr->field_18 = 0;
            ptr->field_1c = v5 + 1;
            if (v1 >= 1)
                ptr = Array__Clear(ptr->field_10, 0);
            p = addr->field_40;
            if (p)
            {
                v7 = p->field_18;
                v8 = p->field_1c;
                p->field_18 = 0;
                p->field_1c = v8 + 1;
                if (v7 >= 1)
                    Array__Clear(p->field_10, 0);
                v9 = TouchObject__OnControlListChange(addr);
                return TouchObject__OnControlListChange(addr);
            }
        }
    }
    sub_f7db74(ptr);
}
```

## `TouchObject.AddControl` — RVA `0xc4d6e4`

- Decompiled symbol: `TouchObject_AddControl`
- Metadata signature: `public void AddControl(TouchControl c) { }`
- Native interval: `300` bytes
- Result: `pseudocode`
- Heuristic layout hint: `TouchObject_Recovered` matched 2 offsets against `TouchObject` metadata (confidence 0.67).

```c
typedef struct struct_3 {
    char padding_0[24];
    struct TouchObject_Recovered *field_18;
} struct_3;

typedef struct TouchObject_Recovered {
    char padding_0[16];
    unsigned long long isOn;
    unsigned int controls;
    unsigned int field_1c;
} TouchObject_Recovered;

typedef struct struct_1 {
    char padding_0[32];
    long long field_20;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern long long g_1ef89f0;
extern long long g_1ef8a00;
extern char g_1fab288;

long long TouchObject_AddControl(struct_3 *p, long long a1)
{
    long long v0;  // x0
    struct_2 *ptr;  // x0
    long long v2;  // x0
    unsigned long long v3;  // x8
    unsigned long v4;  // x10
    struct_1 *addr;  // x8
    unsigned long long v6;  // x0

    if (!(g_1fab288 & 1))
    {
        sub_f7d92c(&g_1ef89f0);
        sub_f7d92c(&g_1ef8a00);
        sub_f7d92c(&g_1ef0c58);
        g_1fab288 = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v0 = Object__op_Equality(a1, 0, 0);
    if (((char)v0 & 1))
        return v0;
    ptr = p->field_18;
    if (ptr)
    {
        v2 = sub_14a36c0(ptr, a1, g_1ef8a00);
        if (((char)v2 & 1))
            return v2;
        ptr = p->field_18;
        if (ptr)
        {
            v3 = ptr->field_10;
            ptr->field_1c = ptr->field_1c + 1;
            if (v3)
            {
                v4 = ptr->field_18;
                if (*((int *)(v3 + 24)) > (unsigned int)v4)
                {
                    addr = v3 + v4 * 8;
                    ptr->field_18 = (unsigned int)v4 + 1;
                    addr->field_20 = a1;
                    sub_f7d8d0((struct struct_1 *)&addr->field_20, a1);
                }
                else
                {
                    sub_14a3390();
                }
                v6 = TouchObject__OnControlListChange(p);
                return TouchObject__OnControlListChange(p);
            }
        }
    }
    sub_f7db74(ptr);
}
```

## `TouchObject.Start` — RVA `0xc4dac4`

- Decompiled symbol: `TouchObject_Start`
- Metadata signature: `public void Start(Vector2 screenPosStart, Vector2 screenPosCur, Camera cam, bool isMouse, bool isPressureSensitive, float pressure) { }`
- Native interval: `232` bytes
- Result: `pseudocode`
- Heuristic layout hint: `TouchObject_Recovered` matched 9 offsets against `TouchObject` metadata (confidence 0.82).

```c
typedef struct TouchObject_Recovered {
    char padding_0[16];
    char isOn;
    char isMouse;
    char isPressureSensitive;
    char padding_13[1];
    unsigned int normalizedPressure;
    char padding_18[8];
    unsigned int screenPosCur;
    unsigned int field_24;
    unsigned int screenPosStart;
    unsigned int field_2c;
    long long cam;
    char isSwipeOverRestricted;
    char padding_39[7];
    struct struct_0 *swipeOverTargetList;
} TouchObject_Recovered;

typedef struct struct_0 {
    char padding_0[16];
    long long field_10;
    int field_18;
    unsigned int field_1c;
} struct_0;

extern long long g_1ef89f8;
extern char g_1fab283;

long long TouchObject_Start(struct_1 *p, long long a1, char a2, char a3)
{
    struct_1 *ptr;  // x23
    struct_0 *addr;  // x8
    unsigned int v2;  // s0
    unsigned int v3;  // s1
    unsigned int v4;  // s2
    unsigned int v5;  // s3
    int v6;  // w2
    unsigned int v7;  // w9
    unsigned int v8;  // s4
    unsigned long long v9;  // x0

    if (!(g_1fab283 & 1))
    {
        sub_f7d92c(&g_1ef89f8);
        g_1fab283 = 1;
    }
    p->field_30 = a1;
    ptr = &p->field_30;
    sub_f7d8d0(ptr, a1);
    addr = *((long long *)&ptr->field_10);
    *((unsigned int *)&ptr->padding_0[8]) = v2;
    *((unsigned int *)&ptr->padding_0[4]) = v3;
    *((unsigned int *)&ptr->field_10) = v4;
    *((unsigned int *)&ptr->padding_0[12]) = v5;
    ptr->padding_0[8] = 0;
    if (addr)
    {
        v6 = addr->field_18;
        v7 = addr->field_1c;
        addr->field_18 = 0;
        addr->field_1c = v7 + 1;
        if (v6 >= 1)
            Array__Clear(addr->field_10, 0);
        p->field_14 = v8;
        p->field_11 = a2 & 1;
        p->field_12 = a3 & 1;
        p->field_10 = 1;
        v9 = TouchObject__OnControlListChange(p);
        return TouchObject__OnControlListChange(p);
    }
    sub_f7db74();
}
```

## `TouchObject.MoveIfNeeded` — RVA `0xc4e244`

- Decompiled symbol: `TouchObject_MoveIfNeeded`
- Metadata signature: `public void MoveIfNeeded(Vector2 screenPos, Camera cam) { }`
- Native interval: `60` bytes
- Result: `pseudocode`

```c
unsigned int [10] TouchObject_MoveIfNeeded(unsigned int *ptr, unsigned long a1)
{
    unsigned int v0;  // s0
    unsigned int v1;  // s2
    unsigned int v2;  // s1
    unsigned int v3;  // s3
    unsigned long v5;  // 4202
    unsigned long long v6;  // x0

    if (a1 == *((long long *)&ptr[12]))
    {
        v1 = v0 - ptr[8];
        v3 = (v2 - ptr[9]) * (v2 - ptr[9]);
        v5 = arm64g_calculate_condition(64, ..., 0, 0);
        if ((char)v5)
            return ptr;
    }
    v6 = TouchObject__Move();
    return TouchObject__Move();
}
```

## `TouchObject.GetControlCount` — RVA `0xc5486c`

- Decompiled symbol: `TouchObject_GetControlCount`
- Metadata signature: `public int GetControlCount() { }`
- Native interval: `72` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[24];
    struct struct_0 *field_18;
} struct_1;

typedef struct struct_0 {
    char padding_0[24];
    unsigned int field_18;
} struct_0;

extern long long g_1ef8a30;
extern char g_1fab282;

int TouchObject_GetControlCount(struct_1 *a0, unsigned long a1)
{
    if (!(g_1fab282 & 1))
    {
        sub_f7d92c(&g_1ef8a30);
        g_1fab282 = 1;
    }
    if (a0->field_18)
        return a0->field_18->field_18;
    sub_f7db74();
}
```

## `TouchObject.Move` — RVA `0xc54c28`

- Decompiled symbol: `TouchObject_Move`
- Metadata signature: `public void Move(Vector2 screenPos, Camera cam) { }`
- Native interval: `272` bytes
- Result: `pseudocode`
- Heuristic layout hint: `TouchObject_Recovered` matched 3 offsets against `TouchObject` metadata (confidence 0.75).

```c
typedef struct TouchObject_Recovered {
    char padding_0[24];
    long long controls;
    unsigned int screenPosCur;
    unsigned int field_24;
    char padding_28[8];
    long long cam;
} TouchObject_Recovered;

typedef struct struct_2 {
    char padding_0[728];
    struct struct_3 *field_2d8;
    unsigned long long field_2e0;
} struct_2;

typedef struct struct_3 {
    unsigned long long field_0;
} struct_3;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern long long g_1ef8a30;
extern long long g_1ef8a38;
extern char g_1fab284;

long long TouchObject_Move(struct_1 *addr, long long a1)
{
    struct_1 *p;  // x21
    struct_1 *ptr;  // x21
    unsigned long v9;  // x2
    unsigned long v10;  // x0
    long long v2;  // x0, Other Possible Types: unsigned long
    unsigned int v3;  // s0
    unsigned int v4;  // s1
    int v5;  // w20
    struct_2 **v6;  // x21
    struct_2 **v7;  // x0
    struct_1 *v8;  // x1

    if (!(g_1fab284 & 1))
    {
        sub_f7d92c(&g_1ef8a30);
        sub_f7d92c(&g_1ef8a38);
        sub_f7d92c(&g_1ef0c58);
        g_1fab284 = 1;
    }
    p = addr;
    p->field_30 = a1;
    ptr = &p->field_30;
    sub_f7d8d0(ptr, a1);
    v2 = ptr->field_18;
    *((unsigned int *)&ptr->padding_0[16]) = v3;
    *((unsigned int *)&ptr->padding_0[12]) = v4;
    if (v2)
    {
        v5 = 0;
        do
        {
            if (*((int *)(v2 + 24)) <= v5)
                return v2;
            v6 = sub_14a30c0();
            if (!g_1ef0c58->field_e0)
                sub_f7da5c(g_1ef0c58);
            if (((char)Object__op_Inequality(v6, 0, 0) & 1))
            {
                if (v6)
                {
                    v7 = v6;
                    v8 = addr;
                    v9 = *(v6)->field_2e0;
                    *(v6)->field_2d8();
                }
                break;
            }
        } while ((v2 = addr->field_18, v5 = (int)(v5 + 1), v2));
    }
    v10 = sub_f7db74(v2);
    return sub_f7db74(v2);
}
```

## `TouchObject.GetRestrictedSwipeOverTargetList` — RVA `0xc54d38`

- Decompiled symbol: `TouchObject_GetRestrictedSwipeOverTargetList`
- Metadata signature: `public List<TouchControl> GetRestrictedSwipeOverTargetList() { }`
- Native interval: `24` bytes
- Result: `pseudocode`
- Heuristic layout hint: `TouchObject_Recovered` matched 2 offsets against `TouchObject` metadata (confidence 1.00).

```c
typedef struct TouchObject_Recovered {
    char padding_0[56];
    char isSwipeOverRestricted;
    char padding_39[7];
    unsigned long long swipeOverTargetList;
} TouchObject_Recovered;

unsigned long long TouchObject_GetRestrictedSwipeOverTargetList(struct_0 *a0)
{
    if (!a0->field_38)
        return 0;
    return a0->field_40;
}
```

## `TouchObject.SetPressure` — RVA `0xc55004`

- Decompiled symbol: `TouchObject_SetPressure`
- Metadata signature: `public void SetPressure(float rawPressure, float maxPressure) { }`
- Native interval: `280` bytes
- Result: `pseudocode`
- Heuristic layout hint: `TouchObject_Recovered` matched 3 offsets against `TouchObject` metadata (confidence 1.00).

```c
typedef struct struct_3 {
    char padding_0[24];
    unsigned int field_18;
} struct_3;

typedef struct TouchObject_Recovered {
    char padding_0[18];
    char isPressureSensitive;
    char padding_13[1];
    unsigned int normalizedPressure;
    struct struct_1 *controls;
} TouchObject_Recovered;

typedef struct struct_4 {
    char padding_0[744];
    struct struct_5 *field_2e8;
    unsigned long long field_2f0;
} struct_4;

typedef struct struct_1 {
    char padding_0[24];
    int field_18;
} struct_1;

typedef struct struct_5 {
    unsigned long long field_0;
} struct_5;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern long long g_1ef8a30;
extern long long g_1ef8a38;
extern char g_1fab286;

struct_3 * TouchObject_SetPressure(struct_2 *ptr)
{
    struct_3 *v0;  // x0
    unsigned int v1;  // s0
    unsigned long v10;  // x0
    unsigned int v2;  // s1
    unsigned long v3;  // 4151
    unsigned int v4;  // s0
    unsigned int v5;  // w20
    struct_4 **v6;  // x21
    struct_4 **v7;  // x0
    struct_2 *v8;  // x1
    unsigned long v9;  // x2

    if (!(g_1fab286 & 1))
    {
        sub_f7d92c(&g_1ef8a30);
        sub_f7d92c(&g_1ef8a38);
        sub_f7d92c(&g_1ef0c58);
        g_1fab286 = 1;
    }
    v0 = ptr->field_18;
    v1 = 0x3f800000;
    v3 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(v2, 981668463)) >> 5 & 3 | (unsigned long long)(CmpF(v2, 981668463) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v2, 981668463)) >> 5 & 3 | (unsigned long long)(CmpF(v2, 981668463) & 1)) & ((unsigned long long)(char)(CmpF(v2, 981668463)) >> 5 & 3 | (unsigned long long)(CmpF(v2, 981668463) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if (!((char)v3))
        v1 = v4 / v2;
    ptr->field_12 = 1;
    ptr->field_14 = v1;
    if (v0)
    {
        v5 = 0;
        do
        {
            if (v0->field_18 <= v5)
                return v0;
            v6 = sub_14a30c0();
            if (!g_1ef0c58->field_e0)
                sub_f7da5c(g_1ef0c58);
            if (((char)Object__op_Inequality(v6, 0, 0) & 1))
            {
                if (v6)
                {
                    v7 = v6;
                    v8 = ptr;
                    v9 = *(v6)->field_2f0;
                    *(v6)->field_2e8();
                }
                break;
            }
        } while ((v0 = (struct_3 *)ptr->field_18, v5 += 1, v0));
    }
    v10 = sub_f7db74(v0);
    return sub_f7db74(v0);
}
```

## `TouchObject.IsOn` — RVA `0xc560f4`

- Decompiled symbol: `TouchObject_IsOn`
- Metadata signature: `public bool IsOn() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    char field_10;
} struct_0;

long long TouchObject_IsOn(struct_0 *a0)
{
    return a0->field_10;
}
```

## `TouchObject.IsMouse` — RVA `0xc560fc`

- Decompiled symbol: `TouchObject_IsMouse`
- Metadata signature: `public bool IsMouse() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[17];
    char field_11;
} struct_0;

long long TouchObject_IsMouse(struct_0 *a0)
{
    return a0->field_11;
}
```

## `TouchObject.IsPressureSensitive` — RVA `0xc56104`

- Decompiled symbol: `TouchObject_IsPressureSensitive`
- Metadata signature: `public bool IsPressureSensitive() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[18];
    char field_12;
} struct_0;

long long TouchObject_IsPressureSensitive(struct_0 *a0)
{
    return a0->field_12;
}
```

## `TouchObject.GetPressure` — RVA `0xc5610c`

- Decompiled symbol: `TouchObject_GetPressure`
- Metadata signature: `public float GetPressure() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long TouchObject_GetPressure(unsigned long a0)
{
    return a0;
}
```

## `TouchObject.OnControlListChange` — RVA `0xc56114`

- Decompiled symbol: `TouchObject_OnControlListChange`
- Metadata signature: `protected void OnControlListChange() { }`
- Native interval: `620` bytes
- Result: `pseudocode`
- Heuristic layout hint: `TouchObject_Recovered` matched 3 offsets against `TouchObject` metadata (confidence 1.00).

```c
typedef struct struct_1 {
    char padding_0[24];
    unsigned int field_18;
} struct_1;

typedef struct TouchObject_Recovered {
    char padding_0[24];
    struct struct_2 *controls;
    char padding_20[24];
    char isSwipeOverRestricted;
    char padding_39[7];
    struct struct_3 *swipeOverTargetList;
} TouchObject_Recovered;

typedef struct struct_7 {
    char padding_0[16];
    unsigned long long field_10;
    unsigned int field_18;
    unsigned int field_1c;
} struct_7;

typedef struct struct_5 {
    char padding_0[808];
    struct struct_6 *field_328;
    unsigned long long field_330;
} struct_5;

typedef struct struct_2 {
    char padding_0[24];
    int field_18;
} struct_2;

typedef struct struct_3 {
    char padding_0[16];
    long long field_10;
    int field_18;
    unsigned int field_1c;
} struct_3;

typedef struct struct_6 {
    unsigned long long field_0;
} struct_6;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern long long g_1ef89f0;
extern long long g_1ef89f8;
extern long long g_1ef8a00;
extern long long g_1ef8a30;
extern long long g_1ef8a38;
extern char g_1fab289;

struct_1 * TouchObject_OnControlListChange(struct_4 *ptr)
{
    struct_7 *p;  // x8
    unsigned int v1;  // w2
    unsigned long v10;  // x0
    unsigned int v2;  // w9
    unsigned long long v3;  // x3
    struct_1 *v4;  // x0
    unsigned int v5;  // w20
    struct_5 **v6;  // x21
    struct_5 **v7;  // x0
    struct_4 *v8;  // x1
    unsigned long v9;  // x2

    if (!(g_1fab289 & 1))
    {
        sub_f7d92c(&g_1ef89f0);
        sub_f7d92c(&g_1ef89f8);
        sub_f7d92c(&g_1ef8a00);
        sub_f7d92c(&g_1ef8a30);
        sub_f7d92c(&g_1ef8a38);
        sub_f7d92c(&g_1ef0c58);
        g_1fab289 = 1;
    }
    p = ptr->field_40;
    ptr->field_38 = 0;
    if (p)
    {
        v1 = p->field_18;
        v2 = p->field_1c + 1;
        p->field_18 = 0;
        p->field_1c = v2;
        if (v1 >= 1)
        {
            v3 = 0;
            Array__Clear(p->field_10, 0);
        }
        v4 = ptr->field_18;
        if (ptr->field_18)
        {
            v5 = 0;
            do
            {
                if (v4->field_18 <= v5)
                    return v4;
                v6 = sub_14a30c0();
                if (!g_1ef0c58->field_e0)
                    sub_f7da5c(g_1ef0c58);
                if (!((char)Object__op_Equality(v6, 0, 0) & 1))
                {
                    if (v6)
                    {
                        v7 = v6;
                        v8 = ptr;
                        v9 = *(v6)->field_330;
                        *(v6)->field_328();
                    }
                    break;
                }
            } while ((v4 = (struct_1 *)ptr->field_18, v5 += 1, v4));
        }
    }
    v10 = sub_f7db74();
    return sub_f7db74();
}
```

## `TouchObject.CanAcceptControl` — RVA `0xc56380`

- Decompiled symbol: `TouchObject_CanAcceptControl`
- Metadata signature: `public bool CanAcceptControl(TouchControl c) { }`
- Native interval: `252` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    char padding_0[24];
    struct struct_1 *field_18;
} struct_2;

typedef struct struct_1 {
    char padding_0[24];
    unsigned int field_18;
} struct_1;

typedef struct struct_3 {
    char padding_0[24];
    unsigned int field_18;
} struct_3;

typedef struct struct_4 {
    char padding_0[760];
    struct struct_5 *field_2f8;
    unsigned long long field_300;
} struct_4;

typedef struct struct_5 {
    unsigned long long field_0;
} struct_5;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern long long g_1ef8a30;
extern long long g_1ef8a38;
extern int g_1fab000;
extern char g_1fab28a;

unsigned long long TouchObject_CanAcceptControl(struct_2 *ptr, unsigned long long a1)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x25
    int v10;  // w21
    struct_1 *p;  // x0, Other Possible Types: struct_3 *
    unsigned long v5;  // x25
    struct_4 **v6;  // x22
    struct_4 **v7;  // x0
    unsigned long long v8;  // x1
    unsigned long v9;  // x2
    unsigned long long v0;  // [bp-0x40]
    unsigned long long v1;  // [bp-0x38]

    v0 = v2;
    v1 = v3;
    v10 = (int)&g_1fab000;
    if (!(g_1fab28a & 1))
    {
        sub_f7d92c(&g_1ef8a30);
        sub_f7d92c(&g_1ef8a38);
        sub_f7d92c(&g_1ef0c58);
        g_1fab28a = 1;
    }
    p = ptr->field_18;
    if (p)
    {
        v10 = 0;
        do
        {
            if (p->field_18 <= v10)
                goto LABEL_1056460;
            v6 = sub_14a30c0();
            if (!g_1ef0c58->field_e0)
                sub_f7da5c(g_1ef0c58);
            if (((char)Object__op_Inequality(v6, 0, 0) & 1))
            {
                if (v6)
                {
                    v7 = v6;
                    v8 = a1;
                    v9 = *(v6)->field_300;
                    *(v6)->field_2f8();
                }
                break;
            }
            p = ptr->field_18;
            v10 += 1;
        } while (p);
        goto LABEL_1056460;
    }
    sub_f7db74(p);
LABEL_1056460:
    if (v10 >= (unsigned int)v5)
        return 1;
    return 0;
}
```

## `TouchObject.SwipeOverFromNothingControlFilter` — RVA `0xc5647c`

- Decompiled symbol: `TouchObject_SwipeOverFromNothingControlFilter`
- Metadata signature: `public bool SwipeOverFromNothingControlFilter(TouchControl c) { }`
- Native interval: `160` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[776];
    unsigned long long field_308;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab28b;

unsigned int TouchObject_SwipeOverFromNothingControlFilter(unsigned long a0, struct_1 **a1)
{
    if (!(g_1fab28b & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab28b = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (!((char)Object__op_Inequality(a1, 0, 0) & 1))
    {
        return 0;
    }
    else if (a1)
    {
        goto *(a1)->field_308;
    }
    else
    {
        sub_f7db74();
    }
}
```

## `TouchObject.DirectTouchControlFilter` — RVA `0xc5651c`

- Decompiled symbol: `TouchObject_DirectTouchControlFilter`
- Metadata signature: `public bool DirectTouchControlFilter(TouchControl c) { }`
- Native interval: `160` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[824];
    unsigned long long field_338;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab28c;

unsigned int TouchObject_DirectTouchControlFilter(unsigned long a0, struct_1 **a1)
{
    if (!(g_1fab28c & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab28c = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (!((char)Object__op_Inequality(a1, 0, 0) & 1))
    {
        return 0;
    }
    else if (a1)
    {
        goto *(a1)->field_338;
    }
    else
    {
        sub_f7db74();
    }
}
```
