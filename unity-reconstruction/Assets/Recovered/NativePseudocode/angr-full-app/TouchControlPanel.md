# Native pseudocode: TouchControlPanel

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `TouchControlPanel.RemoveControl` — RVA `0xc50478`

- Decompiled symbol: `TouchControlPanel_RemoveControl`
- Metadata signature: `public void RemoveControl(TouchControl c) { }`
- Native interval: `136` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    struct struct_0 *field_0;
    char padding_8[24];
    char field_20;
    char field_21;
    char padding_22[14];
    struct struct_2 *field_30;
} struct_2;

typedef struct struct_3 {
    char padding_0[376];
    struct struct_4 *field_178;
    unsigned long long field_180;
} struct_3;

typedef struct struct_0 {
    char padding_0[376];
    struct struct_1 *field_178;
    unsigned long long field_180;
} struct_0;

typedef struct struct_4 {
    unsigned long long field_0;
} struct_4;

typedef struct struct_1 {
    unsigned long long field_0;
} struct_1;

extern long long g_1ef8a20;
extern char g_1fab266;

struct_2 * TouchControlPanel_RemoveControl(struct_2 *ptr, unsigned long a1)
{
    struct_2 *v0;  // x0
    struct_2 *v1;  // x0
    struct_2 *v2;  // x0
    struct_3 *p;  // x8
    struct_2 *v4;  // x0
    unsigned long v5;  // x1

    v0 = ptr;
    if (!(g_1fab266 & 1))
    {
        v1 = sub_f7d92c(&g_1ef8a20);
        g_1fab266 = 1;
        v0 = v1;
    }
    v2 = v0;
    if (ptr->field_21)
    {
        return v2;
    }
    else if (!ptr->field_20)
    {
        p = ptr->field_0;
        ptr->field_20 = 1;
        v4 = ptr;
        v5 = p->field_180;
        p->field_178();
    }
    else if (!ptr->field_30)
    {
        return ptr->field_30;
    }
}
```

## `TouchControlPanel.AddControl` — RVA `0xc50500`

- Decompiled symbol: `TouchControlPanel_AddControl`
- Metadata signature: `public void AddControl(TouchControl c) { }`
- Native interval: `268` bytes
- Result: `pseudocode`

```c
typedef struct struct_3 {
    struct struct_0 *field_0;
    char padding_8[24];
    char field_20;
    char field_21;
    char padding_22[14];
    struct struct_2 *field_30;
} struct_3;

typedef struct struct_5 {
    char padding_0[376];
    struct struct_6 *field_178;
    unsigned long long field_180;
} struct_5;

typedef struct struct_4 {
    char padding_0[16];
    unsigned long long field_10;
    unsigned int field_18;
    unsigned int field_1c;
} struct_4;

typedef struct struct_0 {
    char padding_0[376];
    struct struct_1 *field_178;
    unsigned long long field_180;
} struct_0;

typedef struct struct_2 {
    char padding_0[16];
    unsigned long long field_10;
    unsigned int field_18;
    unsigned int field_1c;
} struct_2;

typedef struct struct_6 {
    unsigned long long field_0;
} struct_6;

typedef struct struct_1 {
    unsigned long long field_0;
} struct_1;

extern long long g_1ef89f0;
extern long long g_1ef8a00;
extern char g_1fab265;

struct_3 * TouchControlPanel_AddControl(struct_3 *ptr, long long a1)
{
    struct_3 *v0;  // x0
    struct_3 *v1;  // x0
    long long v10;  // x0
    long long v11;  // x0
    struct_3 *v2;  // x0
    struct_5 *addr;  // x8
    struct_3 *v4;  // x0
    unsigned long v5;  // x1
    struct_4 *p;  // x0
    struct_3 *v7;  // x0
    unsigned long v8;  // x8
    unsigned long v9;  // x10

    v0 = ptr;
    if (!(g_1fab265 & 1))
    {
        sub_f7d92c(&g_1ef89f0);
        v1 = sub_f7d92c(&g_1ef8a00);
        g_1fab265 = 1;
        v0 = v1;
    }
    v2 = v0;
    if (ptr->field_21)
    {
        return v2;
    }
    else if (!ptr->field_20)
    {
        addr = ptr->field_0;
        ptr->field_20 = 1;
        v4 = ptr;
        v5 = addr->field_180;
        addr->field_178();
    }
    else
    {
        p = ptr->field_30;
        if (p)
        {
            v7 = sub_14a36c0(p, a1, g_1ef8a00);
            if (((char)v7 & 1))
                return v7;
            p = ptr->field_30;
            if (p)
            {
                v8 = p->field_10;
                p->field_1c = p->field_1c + 1;
                if (v8)
                {
                    v9 = p->field_18;
                    if (*((int *)(v8 + 24)) <= (unsigned int)v9)
                    {
                        v11 = sub_14a3390();
                        return sub_14a3390();
                    }
                    p->field_18 = (unsigned int)v9 + 1;
                    *((long long *)(v8 + v9 * 8 + 32)) = a1;
                    v10 = sub_f7d8d0();
                    return sub_f7d8d0();
                }
            }
        }
        sub_f7db74(p);
    }
}
```

## `TouchControlPanel.ctor` — RVA `0xc53bdc`

- Decompiled symbol: `TouchControlPanel_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `500` bytes
- Result: `pseudocode`
- Heuristic layout hint: `TouchControlPanel_Recovered` matched 2 offsets against `TouchControlPanel` metadata (confidence 1.00).

```c
typedef struct TouchControlPanel_Recovered {
    char padding_0[34];
    char autoConnectToRig;
    char padding_23[13];
    long long controls;
} TouchControlPanel_Recovered;

extern long long g_1eed8d0;
extern long long g_1eeda80;
extern long long g_1ef3c90;
extern long long g_1ef89e8;
extern long long g_1ef9380;
extern long long g_1ef9388;
extern long long g_1ef9bf8;
extern char g_1fab262;

void TouchControlPanel_ctor(struct_0 *ptr)
{
    unsigned long long v6;  // x30
    unsigned long long v7;  // x23
    unsigned long long v8;  // x22
    unsigned long long v9;  // x21
    unsigned long long v10;  // x20
    unsigned long long v11;  // x19
    long long v12;  // x20
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
    if (!(g_1fab262 & 1))
    {
        sub_f7d92c(&g_1ef3c90);
        sub_f7d92c(&g_1ef9388);
        sub_f7d92c(&g_1ef89e8);
        sub_f7d92c(&g_1ef9380);
        sub_f7d92c(&g_1eed8d0);
        sub_f7d92c(&g_1eeda80);
        sub_f7d92c(&g_1ef9bf8);
        sub_f7d92c("As");
        g_1fab262 = 1;
    }
    ptr->field_22 = 1;
    MonoBehaviour__ctor(ptr, 0);
    v12 = sub_f7db70(g_1eed8d0);
    sub_14a2bd4(v12, 16, g_1ef89e8);
    ptr->field_30 = v12;
    sub_f7d8d0((struct TouchControlPanel_Recovered *)&ptr->field_30, v12);
    TouchControl_HitPool__ctor(sub_f7db70(g_1ef3c90)); /* do not return */
}
```

## `TouchControlPanel.OnInitComponent` — RVA `0xc53e40`

- Decompiled symbol: `TouchControlPanel_OnInitComponent`
- Metadata signature: `protected override void OnInitComponent() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long TouchControlPanel_OnInitComponent(unsigned long a0)
{
    unsigned long long v0;  // x0

    v0 = TouchControlPanel__InvalidateHierarchy();
    return TouchControlPanel__InvalidateHierarchy();
}
```

## `TouchControlPanel.InvalidateHierarchy` — RVA `0xc53e44`

- Decompiled symbol: `TouchControlPanel_InvalidateHierarchy`
- Metadata signature: `public void InvalidateHierarchy() { }`
- Native interval: `260` bytes
- Result: `pseudocode`
- Heuristic layout hint: `TouchControlPanel_Recovered` matched 2 offsets against `TouchControlPanel` metadata (confidence 1.00).

```c
typedef struct TouchControlPanel_Recovered {
    char padding_0[34];
    char autoConnectToRig;
    char padding_23[5];
    long long rig;
} TouchControlPanel_Recovered;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern long long g_1efcfe0;
extern long long g_1efd170;
extern char g_1fab264;

long long TouchControlPanel_InvalidateHierarchy(struct_1 *ptr)
{
    long long v0;  // x0
    long long v1;  // x0
    struct_1 *v2;  // x20
    long long v3;  // x0
    long long v4;  // x0

    if (!(g_1fab264 & 1))
    {
        sub_f7d92c(&g_1efd170);
        sub_f7d92c(&g_1efcfe0);
        sub_f7d92c(&g_1ef0c58);
        g_1fab264 = 1;
    }
    if (!ptr->field_22)
    {
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        v0 = Object__op_Equality(ptr->field_28, 0, 0);
        if (!((char)v0 & 1))
            return v0;
    }
    v1 = sub_1231bc8(ptr, g_1efcfe0);
    ptr->field_28 = v1;
    v2 = &ptr->field_28;
    sub_f7d8d0(v2, v1);
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v3 = Object__op_Equality(*((long long *)&v2->padding_0[0]), 0, 0);
    if (!((char)v3 & 1))
        return v3;
    ptr->field_28 = sub_123204c(ptr, g_1efd170);
    v4 = sub_f7d8d0();
    return sub_f7d8d0();
}
```

## `TouchControlPanel.OnDestroyComponent` — RVA `0xc53f48`

- Decompiled symbol: `TouchControlPanel_OnDestroyComponent`
- Metadata signature: `protected override void OnDestroyComponent() { }`
- Native interval: `416` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[48];
    long long field_30;
} struct_1;

typedef struct struct_2 {
    struct struct_0 *field_0;
    char padding_8[24];
    char field_20;
    char field_21;
} struct_2;

typedef struct struct_0 {
    char padding_0[376];
    struct struct_1 *field_178;
    unsigned long long field_180;
} struct_0;

typedef struct struct_1 {
    unsigned long long field_0;
} struct_1;

extern struct_0 *g_1ef0c58;
extern long long g_1ef6498;
extern long long g_1ef64a0;
extern long long g_1ef64a8;
extern long long g_1ef8a10;
extern char g_1fab263;

long long TouchControlPanel_OnDestroyComponent(struct_1 *ptr)
{
    long long v3;  // x0
    unsigned long long v4;  // x0
    long long v5;  // x19
    unsigned long flag;  // [bp-0x48]
    unsigned long long choice;  // [bp-0x40]
    unsigned long flag2;  // [bp-0x38]

    if (!(g_1fab263 & 1))
    {
        sub_f7d92c(&g_1ef6498);
        sub_f7d92c(&g_1ef64a0);
        sub_f7d92c(&g_1ef64a8);
        sub_f7d92c(&g_1ef8a10);
        sub_f7d92c(&g_1ef0c58);
        g_1fab263 = 1;
    }
    flag = 0;
    choice = 0;
    flag2 = 0;
    TouchControlPanel__ReleaseAll(ptr, 1);
    v3 = ptr->field_30;
    if (!v3)
        return v3;
    sub_14a3cf0(v3, g_1ef8a10);
    while (true)
    {
        do
        {
            if (!((char)sub_130ea88(&flag, g_1ef64a0) & 1))
            {
                v4 = sub_130ea84(&flag, g_1ef6498);
                return sub_130ea84(&flag, g_1ef6498);
            }
            if (!g_1ef0c58->field_e0)
                sub_f7da5c(g_1ef0c58);
        } while (!((char)Object__op_Inequality(flag2, 0, 0) & 1));
        if (!flag2)
            break;
        TouchControl__SetTouchControlPanel(flag2, NULL);
    }
    v5 = sub_f7db74();
    sub_130ea84(&flag, g_1ef6498);
    sub_1026098(v5);
    sub_e29990(sub_f1bd40(0));
}
```

## `TouchControlPanel.ReleaseAll` — RVA `0xc540e8`

- Decompiled symbol: `TouchControlPanel_ReleaseAll`
- Metadata signature: `private void ReleaseAll(bool cancel) { }`
- Native interval: `164` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    char padding_0[16];
    struct struct_2 *field_10;
} struct_2;

typedef struct struct_1 {
    char padding_0[56];
    struct struct_0 *field_38;
} struct_1;

typedef struct struct_0 {
    char padding_0[16];
    struct struct_0 *field_10;
} struct_0;

extern long long g_1ef9390;
extern unsigned int g_1ef9398;
extern char g_1fab26e;

struct_2 * TouchControlPanel_ReleaseAll(struct_1 *ptr, unsigned int a1)
{
    struct_0 *cur;  // x0, Other Possible Types: struct_2 *
    int v1;  // w20
    unsigned long v2;  // x0

    if (!(g_1fab26e & 1))
    {
        sub_f7d92c(&g_1ef9390);
        sub_f7d92c(&g_1ef9398);
        g_1fab26e = 1;
    }
    cur = ptr->field_38;
    if (cur)
    {
        v1 = 0;
        do
        {
            if (*((int *)&cur[1].padding_0[0]) <= v1)
                return cur;
        } while ((cur = (struct_0 *)sub_14a30c0(), cur && (cur = (struct_0 *)cur->field_10, cur && (TouchObject__End(cur, a1 & 1, *((long long *)&g_1ef9398)), cur = (struct_0 *)ptr->field_38, v1 = (int)(v1 + 1), cur))));
    }
    v2 = sub_f7db74(cur);
    return sub_f7db74(cur);
}
```

## `TouchControlPanel.OnEnableComponent` — RVA `0xc5418c`

- Decompiled symbol: `TouchControlPanel_OnEnableComponent`
- Metadata signature: `protected override void OnEnableComponent() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long TouchControlPanel_OnEnableComponent(void)
{
    unsigned long v0;  // x0

    return v0;
}
```

## `TouchControlPanel.OnDisableComponent` — RVA `0xc54190`

- Decompiled symbol: `TouchControlPanel_OnDisableComponent`
- Metadata signature: `protected override void OnDisableComponent() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    char padding_0[16];
    void* field_10;
} struct_2;

typedef struct struct_1 {
    char padding_0[56];
    struct struct_0 *field_38;
} struct_1;

typedef struct struct_0 {
    char padding_0[16];
    void* field_10;
} struct_0;

struct_2 * TouchControlPanel_OnDisableComponent(struct_1 *a0)
{
    struct_2 *v0;  // x0

    v0 = TouchControlPanel__ReleaseAll(a0, 1);
    return TouchControlPanel__ReleaseAll(a0, 1);
}
```

## `TouchControlPanel.Update` — RVA `0xc54198`

- Decompiled symbol: `TouchControlPanel_Update`
- Metadata signature: `private void Update() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long TouchControlPanel_Update(unsigned long a0)
{
    unsigned long long v0;  // x0

    v0 = TouchControlPanel__UpdateTouches();
    return TouchControlPanel__UpdateTouches();
}
```

## `TouchControlPanel.UpdatePanel` — RVA `0xc5419c`

- Decompiled symbol: `TouchControlPanel_UpdatePanel`
- Metadata signature: `public void UpdatePanel() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long TouchControlPanel_UpdatePanel(unsigned long a0)
{
    unsigned long long v0;  // x0

    v0 = TouchControlPanel__UpdateTouches();
    return TouchControlPanel__UpdateTouches();
}
```

## `TouchControlPanel.UpdateTouches` — RVA `0xc541a0`

- Decompiled symbol: `TouchControlPanel_UpdateTouches`
- Metadata signature: `public void UpdateTouches() { }`
- Native interval: `140` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[56];
    unsigned long long field_38;
} struct_0;

extern long long g_1ef9390;
extern long long g_1ef9398;
extern char g_1fab26d;

long long TouchControlPanel_UpdateTouches(struct_0 *ptr)
{
    unsigned long long v0;  // x0
    int v1;  // w20
    unsigned long long v2;  // x0

    if (!(g_1fab26d & 1))
    {
        sub_f7d92c(&g_1ef9390);
        sub_f7d92c(&g_1ef9398);
        g_1fab26d = 1;
    }
    v0 = ptr->field_38;
    if (v0)
    {
        v1 = 0;
        do
        {
            if (*((int *)(v0 + 24)) <= v1)
            {
                v2 = TouchControlPanel__UpdateTouchPressure(ptr);
                return TouchControlPanel__UpdateTouchPressure(ptr);
            }
        } while ((v0 = (unsigned long long)sub_14a30c0(), v0 && (TouchControlPanel_SystemTouch__Update(), v0 = ptr->field_38, v1 = (int)(v1 + 1), v0)));
    }
    sub_f7db74(v0);
    v2 = TouchControlPanel__UpdateTouchPressure(ptr);
    return TouchControlPanel__UpdateTouchPressure(ptr);
}
```

## `TouchControlPanel.GetControlList` — RVA `0xc5422c`

- Decompiled symbol: `TouchControlPanel_GetControlList`
- Metadata signature: `public List<TouchControl> GetControlList() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[48];
    unsigned long long field_30;
} struct_0;

long long TouchControlPanel_GetControlList(struct_0 *a0)
{
    return a0->field_30;
}
```

## `TouchControlPanel.Prepare` — RVA `0xc54234`

- Decompiled symbol: `TouchControlPanel_Prepare`
- Metadata signature: `private void Prepare() { }`
- Native interval: `192` bytes
- Result: `pseudocode`
- Heuristic layout hint: `TouchControlPanel_Recovered` matched 2 offsets against `TouchControlPanel` metadata (confidence 1.00).

```c
typedef struct TouchControlPanel_Recovered {
    char padding_0[40];
    struct struct_2 *rig;
    char padding_30[24];
    unsigned int fingerRadInPx;
} TouchControlPanel_Recovered;

typedef struct struct_2 {
    char padding_0[76];
    unsigned int field_4c;
} struct_2;

typedef struct struct_1 {
    char padding_0[224];
    unsigned int field_e0;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1eeed10;
extern struct_1 *g_1ef0c58;
extern char g_1fab267;

unsigned long long TouchControlPanel_Prepare(struct_3 *ptr)
{
    unsigned int v0;  // s8
    unsigned long long v1;  // x0
    unsigned int v2;  // s0

    if (!(g_1fab267 & 1))
    {
        sub_f7d92c(&g_1eeed10);
        sub_f7d92c(&g_1ef0c58);
        g_1fab267 = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (!((char)Object__op_Inequality(ptr->field_28, 0, 0) & 1))
    {
        v0 = 1036831949;
    }
    else if (ptr->field_28)
    {
        v0 = ptr->field_28->field_4c;
    }
    else
    {
        sub_f7db74();
    }
    if (!g_1eeed10->field_e0)
        sub_f7da5c(g_1eeed10);
    v1 = CFScreen__get_dpcm(0, 0);
    ptr->field_48 = v0 * v2;
    return v1;
}
```

## `TouchControlPanel.Raycast` — RVA `0xc542f4`

- Decompiled symbol: `TouchControlPanel_Raycast`
- Metadata signature: `public bool Raycast(Vector2 sp, Camera eventCamera) { }`
- Native interval: `340` bytes
- Result: `pseudocode`
- Heuristic layout hint: `TouchControlPanel_Recovered` matched 3 offsets against `TouchControlPanel` metadata (confidence 1.00).

```c
typedef struct TouchControlPanel_Recovered {
    char padding_0[40];
    struct struct_2 *rig;
    struct struct_2 *controls;
    char padding_38[8];
    struct TouchControlPanel_Recovered *hitPool;
} TouchControlPanel_Recovered;

typedef struct struct_2 {
    char padding_0[80];
    char field_50;
    char padding_51[35];
    char field_74;
    char padding_75[187];
    char field_130;
} struct_2;

typedef struct struct_2 {
    char padding_0[24];
    int field_18;
} struct_2;

typedef struct TouchControlPanel_Recovered {
    char padding_0[32];
    struct struct_0 *field_20;
} struct_1;

typedef struct struct_0 {
    char padding_0[16];
    unsigned long long field_10;
} struct_0;

extern struct_0 *g_1ef0c58;
extern long long g_1ef42a0;
extern struct_0 *g_1f024a0;
extern char g_1fab268;

unsigned int TouchControlPanel_Raycast(struct_1 *ptr, long long a1)
{
    char v0[305];  // x8
    void* v1;  // x0
    unsigned int v2;  // x4

    if (!(g_1fab268 & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c(&g_1ef42a0);
        sub_f7d92c(&g_1f024a0);
        g_1fab268 = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (((char)Object__op_Inequality(ptr->field_28, 0, 0) & 1))
    {
        v0 = ptr->field_28;
        if (!v0)
        {
            sub_f7db74();
        }
        else if (v0[304])
        {
            return 0;
        }
        else if (v0[116] || v0[80])
        {
            return 1;
        }
    }
    TouchControlPanel__Prepare(ptr);
    v1 = sub_f7db70(g_1ef42a0);
    TouchControl_HitPool_TouchControlFilterFunc__ctor(v1, ptr, g_1f024a0);
    if (ptr->field_40)
        return TouchControl_HitPool__HitTestAny(ptr->field_40, ptr->field_30, a1, v1, v2);
    sub_f7db74();
}
```

## `TouchControlPanel.RaycastControlFilter` — RVA `0xc54448`

- Decompiled symbol: `TouchControlPanel_RaycastControlFilter`
- Metadata signature: `private bool RaycastControlFilter(TouchControl c) { }`
- Native interval: `144` bytes
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
extern char g_1fab269;

unsigned int TouchControlPanel_RaycastControlFilter(unsigned long a0, struct_1 **a1)
{
    if (!(g_1fab269 & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab269 = 1;
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

## `TouchControlPanel.OnSystemTouchStart` — RVA `0xc544d8`

- Decompiled symbol: `TouchControlPanel_OnSystemTouchStart`
- Metadata signature: `public void OnSystemTouchStart(TouchControlPanel.SystemTouchEventData data) { }`
- Native interval: `584` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[24];
    long long field_18;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern long long g_1ef42a0;
extern long long g_1ef9370;
extern long long g_1ef9378;
extern long long g_1ef9c00;
extern struct_0 *g_1f024a8;
extern char g_1fab26a;

void* TouchControlPanel_OnSystemTouchStart(void* ptr, struct_1 *a1)
{
    void* v0;  // x0
    void* v1;  // x0
    unsigned long v3;  // x0
    void* v4;  // x0
    void* v5;  // x0
    unsigned long v6;  // x0

    v0 = ptr;
    if (!(g_1fab26a & 1))
    {
        sub_f7d92c(&g_1ef9370);
        sub_f7d92c(&g_1ef9378);
        sub_f7d92c(&g_1ef9c00);
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c(&g_1ef42a0);
        v1 = sub_f7d92c(&g_1f024a8);
        g_1fab26a = 1;
        v0 = v1;
    }
    if (!(char)ptr[32])
        return v0;
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (((char)Object__op_Inequality((long long)ptr[40], 0, 0) & 1))
    {
        v3 = (long long)ptr[40];
        if (!v3)
        {
            v6 = sub_f7db74(v3);
            return sub_f7db74(v3);
        }
        InputRig__WakeTouchControlsUp(v3);
    }
    v4 = TouchControlPanel__StartNewTouch(ptr, a1);
    if (!v4)
        return v4;
    v3 = TouchControlPanel__Prepare(ptr);
    if (!a1)
    {
        v6 = sub_f7db74(v3);
        return sub_f7db74(v3);
    }
    v5 = sub_f7db70(g_1ef42a0);
    v3 = (unsigned long long)TouchControl_HitPool_TouchControlFilterFunc__ctor(v5, (long long)v4[16], g_1f024a8);
    if (!(long long)ptr[64])
    {
        v6 = sub_f7db74(v3);
        return sub_f7db74(v3);
    }
    TouchControl_HitPool__HitTest((long long)ptr[64], (long long)ptr[48], a1->field_18, 8, v5); /* do not return */
}
```

## `TouchControlPanel.StartNewTouch` — RVA `0xc54720`

- Decompiled symbol: `TouchControlPanel_StartNewTouch`
- Metadata signature: `private TouchControlPanel.SystemTouch StartNewTouch(TouchControlPanel.SystemTouchEventData data) { }`
- Native interval: `332` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[16];
    char field_10;
    char field_11;
    char field_12;
    char padding_13[1];
    unsigned int field_14;
    char padding_18[8];
    unsigned int field_20;
    unsigned int field_24;
    unsigned int field_28;
    unsigned int field_2c;
    long long field_30;
    char field_38;
    char padding_39[7];
    struct struct_0 *field_40;
} struct_1;

typedef struct struct_0 {
    char padding_0[16];
    struct struct_0 *field_10;
    int field_18;
    char padding_1c[4];
    unsigned int field_20;
} struct_0;

typedef struct struct_2 {
    char padding_0[24];
    long long field_18;
    char padding_20[4];
    char field_24;
} struct_2;

typedef struct struct_0 {
    char padding_0[16];
    long long field_10;
    int field_18;
    unsigned int field_1c;
} struct_0;

extern long long g_1ef9390;
extern unsigned int g_1ef9398;
extern char g_1fab270;

struct_1 * TouchControlPanel_StartNewTouch(struct_1 *p, struct_2 *off)
{
    struct_0 *cur;  // x0
    struct_1 *ptr;  // x20
    int v3;  // w22
    struct_0 *v4;  // x8
    unsigned int v0;  // [bp-0x34]

    if (!(g_1fab270 & 1))
    {
        sub_f7d92c(&g_1ef9390);
        sub_f7d92c(&g_1ef9398);
        g_1fab270 = 1;
    }
    cur = *((long long *)&p->field_38);
    if (cur)
    {
        ptr = NULL;
        v3 = 0;
        do
        {
            if (cur->field_18 > v3)
            {
                cur = sub_14a30c0();
                if (!cur || !((v4 = cur, cur = (struct_0 *)cur->field_10, cur)))
                    break;
                if ((char)cur->field_10)
                {
                    if (!off)
                        break;
                    if (v4->field_18 == off->padding_20)
                        TouchObject__End(cur, 1, *((long long *)&g_1ef9398));
                }
                else
                {
                    ptr = v4;
                }
            }
            else if (ptr)
            {
                *((unsigned int *)&ptr->padding_18[4]) = 0;
                if (off)
                {
                    *((char [4])&ptr->padding_18[0]) = off->padding_20;
                    ptr->field_20 = Time__get_frameCount(0);
                    v0 = 0x3f800000;
                    if (off->field_24)
                        cur = NULL;
                    else
                        cur = TouchControlPanel__IsTouchPressureSensitive();
                    if (*((long long *)&ptr->field_10))
                    {
                        TouchObject__Start(*((long long *)&ptr->field_10), off->field_18, off->field_24, (char)cur & 1);
                        return ptr;
                    }
                    break;
                }
            }
            else
            {
                return ptr;
            }
        } while ((cur = (struct_0 *)*((long long *)&p->field_38), v3 = (int)(v3 + 1), cur));
    }
    sub_f7db74(cur);
}
```

## `TouchControlPanel.OnSystemTouchEnd` — RVA `0xc548b4`

- Decompiled symbol: `TouchControlPanel_OnSystemTouchEnd`
- Metadata signature: `public void OnSystemTouchEnd(TouchControlPanel.SystemTouchEventData data) { }`
- Native interval: `180` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab26b;

void* TouchControlPanel_OnSystemTouchEnd(void* a0, unsigned long long a1)
{
    void* v0;  // x0
    void* v1;  // x0
    void* v3;  // x0
    long long v4;  // x0

    v0 = a0;
    if (!(g_1fab26b & 1))
    {
        v1 = sub_f7d92c(&g_1ef0c58);
        g_1fab26b = 1;
        v0 = v1;
    }
    if (!(char)a0[32])
        return v0;
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (((char)Object__op_Inequality((long long)a0[40], 0, 0) & 1))
    {
        if ((long long)a0[40])
            InputRig__WakeTouchControlsUp((long long)a0[40]);
        else
            sub_f7db74();
    }
    if (!a1)
        sub_f7db74();
    v3 = TouchControlPanel__FindTouch();
    if (!v3)
        return v3;
    if ((long long)v3[16])
    {
        v4 = TouchObject__End((long long)v3[16], 0, 0);
        return TouchObject__End((long long)v3[16], 0, 0);
    }
    sub_f7db74();
}
```

## `TouchControlPanel.FindTouch` — RVA `0xc54968`

- Decompiled symbol: `TouchControlPanel_FindTouch`
- Metadata signature: `private TouchControlPanel.SystemTouch FindTouch(int hwId) { }`
- Native interval: `176` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    char padding_0[56];
    struct struct_1 *field_38;
} struct_2;

typedef struct struct_1 {
    char padding_0[16];
    struct struct_0 *field_10;
    unsigned int field_18;
} struct_1;

typedef struct struct_4 {
    char padding_0[16];
    struct struct_3 *field_10;
    unsigned int field_18;
} struct_4;

typedef struct struct_0 {
    char padding_0[16];
    char field_10;
} struct_0;

typedef struct struct_3 {
    char padding_0[16];
    char field_10;
} struct_3;

extern long long g_1ef9390;
extern long long g_1ef9398;
extern char g_1fab26f;

int TouchControlPanel_FindTouch(struct_2 *ptr, unsigned int a1)
{
    struct_1 *v0;  // x0, Other Possible Types: struct_4 *
    int v1;  // w21

    if (!(g_1fab26f & 1))
    {
        sub_f7d92c(&g_1ef9390);
        sub_f7d92c(&g_1ef9398);
        g_1fab26f = 1;
    }
    v0 = ptr->field_38;
    if (v0)
    {
        v1 = 0;
        while (true)
        {
            if (v0->field_18 <= v1)
                goto LABEL_1054a04;
            v0 = sub_14a30c0();
            if (!v0 || !v0->field_10)
                goto LABEL_1054a00;
            if (v0->field_10->field_10 && v0->field_18 == a1)
                break;
            v0 = ptr->field_38;
            v1 += 1;
            goto LABEL_1054a00;
        }
    }
    else
    {
LABEL_1054a00:
        sub_f7db74(v0);
LABEL_1054a04:
        v0 = NULL;
    }
    return *((unsigned int *)&v0);
}
```

## `TouchControlPanel.OnSystemTouchMove` — RVA `0xc54a18`

- Decompiled symbol: `TouchControlPanel_OnSystemTouchMove`
- Metadata signature: `public void OnSystemTouchMove(TouchControlPanel.SystemTouchEventData data) { }`
- Native interval: `520` bytes
- Result: `pseudocode`
- Heuristic layout hint: `TouchControlPanel_Recovered` matched 3 offsets against `TouchControlPanel` metadata (confidence 1.00).

```c
typedef struct struct_1 {
    char padding_0[24];
    long long field_18;
    unsigned int field_20;
} struct_1;

typedef struct TouchControlPanel_Recovered {
    char padding_0[48];
    unsigned long long controls;
    char touchList;
    char padding_39[7];
    struct struct_6 *hitPool;
} TouchControlPanel_Recovered;

typedef struct struct_6 {
    char padding_0[24];
    unsigned int field_18;
} struct_6;

typedef struct struct_3 {
    char padding_0[24];
    struct struct_4 *field_18;
    char padding_20[8];
    unsigned long long field_28;
    char padding_30[16];
    unsigned long long field_40;
} struct_3;

typedef struct struct_4 {
    unsigned long long field_0;
} struct_4;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern long long g_1ef8a30;
extern long long g_1ef9370;
extern long long g_1ef9378;
extern long long g_1ef9c00;
extern char g_1fab26c;

void* TouchControlPanel_OnSystemTouchMove(void* p, struct_1 *a1)
{
    void* v0;  // x0
    void* v1;  // x0
    void* v2;  // x0
    void* addr;  // x0
    void* ptr;  // x20
    struct_7 *v5;  // x0
    void* v6;  // x0
    struct_7 *ptr3;  // x8
    struct_6 *v8;  // x1
    unsigned long v9;  // x0

    v0 = p;
    if (!(g_1fab26c & 1))
    {
        sub_f7d92c(&g_1ef9370);
        sub_f7d92c(&g_1ef8a30);
        sub_f7d92c(&g_1ef9378);
        sub_f7d92c(&g_1ef9c00);
        v1 = sub_f7d92c(&g_1ef0c58);
        g_1fab26c = 1;
        v0 = v1;
    }
    v2 = v0;
    if (!(char)p[32])
        return v2;
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (!((char)Object__op_Inequality((long long)p[40], 0, 0) & 1))
    {
LABEL_1054ac8:
        if (a1)
        {
            addr = TouchControlPanel__FindTouch(p, a1->field_20);
            if (!addr)
                return addr;
            ptr = addr;
            v5 = (long long)addr[16];
            *((unsigned int *)&ptr[28]) = 0;
            if (v5 && (v6 = (void*)TouchObject__Move(v5, a1->field_18), ptr3 = (struct_7 *)(long long)ptr[16], ptr3))
            {
                if (ptr3->field_38 && (v8 = (struct_6 *)ptr3->field_40, v8))
                {
                    goto LABEL_1054b24;
                }
                else
                {
                    v8 = (long long)p[48];
                    if (v8)
                    {
LABEL_1054b24:
                        if (v8->field_18 < 1)
                            return v6;
                        if ((long long)p[64])
                            TouchControl_HitPool__HitTest((long long)p[64], v8, ptr3->field_30, 8, NULL); /* do not return */
                    }
                }
            }
        }
    }
    else if ((long long)p[40])
    {
        InputRig__WakeTouchControlsUp((long long)p[40]);
        goto LABEL_1054ac8;
    }
    v9 = sub_f7db74();
    return sub_f7db74();
}
```

## `TouchControlPanel.UpdateTouchPressure` — RVA `0xc54df0`

- Decompiled symbol: `TouchControlPanel_UpdateTouchPressure`
- Metadata signature: `private void UpdateTouchPressure() { }`
- Native interval: `264` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    char padding_0[56];
    struct struct_1 *field_38;
} struct_2;

typedef struct struct_0 {
    char padding_0[16];
    long long field_10;
} struct_0;

typedef struct struct_1 {
    char padding_0[16];
    struct struct_0 *field_10;
    unsigned int field_18;
} struct_1;

typedef struct struct_0 {
    char padding_0[16];
    char field_10;
} struct_0;

int TouchControlPanel_UpdateTouchPressure(struct_2 *a0)
{
    unsigned long long v6;  // x0
    unsigned int v7;  // w20
    struct_0 *v8;  // x0
    char v0;  // [bp-0xc8]
    int flag3;  // [bp-0x80]
    uint128_t flag4;  // [bp-0x70]
    uint128_t choice;  // [bp-0x60]
    uint128_t flag2;  // [bp-0x50]
    unsigned int flag;  // [bp-0x40]

    flag = 0;
    choice = 0;
    flag2 = 0;
    flag3 = 0;
    flag4 = 0;
    v6 = Input__get_touchPressureSupported(0);
    if (((char)v6 & 1))
    {
        v6 = Input__get_touchCount(0);
        if ((unsigned int)v6 >= 1)
        {
            v7 = 0;
            do
            {
                Input__GetTouch(v7, 0);
                memcpy(&flag3, &v0, 68);
                if (Touch__get_phase(&flag3, 0) != 4 && Touch__get_phase(&flag3, 0) != 3)
                {
                    v8 = TouchControlPanel__FindTouch(a0, Touch__get_fingerId(&flag3, 0));
                    if (v8)
                    {
                        Touch__get_pressure(&flag3, 0);
                        Touch__get_maximumPossiblePressure(&flag3, 0);
                        if (!v8->field_10)
                            sub_f7db74();
                        TouchObject__SetPressure(v8->field_10);
                    }
                }
            } while ((v7 += 1, v6 = (unsigned long long)Input__get_touchCount(0), v7 < (unsigned int)v6));
        }
    }
    return v6;
}
```

## `TouchControlPanel.IsTouchPressureSensitive` — RVA `0xc54ef8`

- Decompiled symbol: `TouchControlPanel_IsTouchPressureSensitive`
- Metadata signature: `private bool IsTouchPressureSensitive(int touchId, out float pressureOut) { }`
- Native interval: `268` bytes
- Result: `pseudocode`

```c
unsigned int TouchControlPanel_IsTouchPressureSensitive(unsigned long a0, unsigned int a1, unsigned int *ptr)
{
    int v6;  // w21
    char v0;  // [bp-0xc8]
    int flag3;  // [bp-0x80]
    uint128_t flag4;  // [bp-0x70]
    uint128_t choice;  // [bp-0x60]
    uint128_t flag2;  // [bp-0x50]
    unsigned int flag;  // [bp-0x40]

    flag = 0;
    choice = 0;
    flag2 = 0;
    flag3 = 0;
    flag4 = 0;
    *(ptr) = 0x3f800000;
    if (!((char)Input__get_touchPressureSupported(0) & 1))
        return 0;
    if (Input__get_touchCount(0) < 1)
        return 0;
    v6 = 0;
    do
    {
        Input__GetTouch(v6, 0);
        memcpy(&flag3, &v0, 68);
        if (Touch__get_phase(&flag3, 0) != 4 && Touch__get_phase(&flag3, 0) != 3 && (int)Touch__get_fingerId(&flag3, 0) == a1)
        {
            Touch__get_pressure(&flag3, 0);
            Touch__get_maximumPossiblePressure(&flag3, 0);
            *(ptr) = 0 / 0;
            return 1;
        }
    } while ((v6 = (int)(v6 + 1), v6 < (unsigned int)(unsigned long long)Input__get_touchCount(0)));
    return 0;
}
```

## `TouchControlPanel.GetActiveTouchCount` — RVA `0xc5511c`

- Decompiled symbol: `TouchControlPanel_GetActiveTouchCount`
- Metadata signature: `public int GetActiveTouchCount() { }`
- Native interval: `164` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    char padding_0[56];
    struct struct_1 *field_38;
} struct_2;

typedef struct struct_1 {
    char padding_0[16];
    struct struct_0 *field_10;
} struct_1;

typedef struct struct_4 {
    char padding_0[16];
    struct struct_3 *field_10;
} struct_4;

typedef struct struct_0 {
    char padding_0[16];
    char field_10;
} struct_0;

typedef struct struct_3 {
    char padding_0[16];
    char field_10;
} struct_3;

extern long long g_1ef9390;
extern long long g_1ef9398;
extern unsigned long long g_1fab000;
extern char g_1fab271;

int TouchControlPanel_GetActiveTouchCount(struct_2 *ptr)
{
    unsigned long long v0;  // x20
    struct_1 *v1;  // x0
    int v2;  // w21
    struct_4 *v3;  // x0

    v0 = &g_1fab000;
    if (!(g_1fab271 & 1))
    {
        sub_f7d92c(&g_1ef9390);
        sub_f7d92c(&g_1ef9398);
        g_1fab271 = 1;
    }
    v1 = ptr->field_38;
    if (v1)
    {
        v0 = 0;
        v2 = 0;
        do
        {
            if (*((int *)&v1[1].padding_0[0]) <= v2)
                return v0;
        } while ((v3 = (struct_4 *)sub_14a30c0(), v1 = (struct_1 *)v3, v1 && (v1 = (struct_1 *)v3, v1->field_10 && (v1 = (struct_1 *)ptr->field_38, v2 = (int)(v2 + 1), v0 += (unsigned long long)v3->field_10->field_10, v1 = v1, v1))));
    }
    sub_f7db74(v1);
    return v0;
}
```
