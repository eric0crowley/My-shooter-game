# Native pseudocode: TouchControlPanelUnityUiAddOn

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `TouchControlPanelUnityUiAddOn.IsConnectedToPanel` — RVA `0xc551c8`

- Decompiled symbol: `TouchControlPanelUnityUiAddOn_IsConnectedToPanel`
- Metadata signature: `public bool IsConnectedToPanel() { }`
- Native interval: `96` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab273;

void TouchControlPanelUnityUiAddOn_IsConnectedToPanel(unsigned long a0)
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
    if (!(g_1fab273 & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab273 = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    Object__op_Inequality();
    return;
}
```

## `TouchControlPanelUnityUiAddOn.ctor` — RVA `0xc55228`

- Decompiled symbol: `TouchControlPanelUnityUiAddOn_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `144` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[176];
    long long field_b0;
} struct_1;

extern char g_1fab274;

void TouchControlPanelUnityUiAddOn_ctor(struct_1 *ptr)
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
    if (!(g_1fab274 & 1))
    {
        sub_f7d92c("W=");
        sub_f7d92c("Cs");
        g_1fab274 = 1;
    }
    if (!g_1eefba0->field_e0)
        sub_f7da5c(g_1eefba0);
    Graphic__ctor(ptr, 0);
    v8 = sub_f7db70(g_1ef3ca0);
    Object__ctor(v8, 0);
    ptr->field_b0 = v8;
    sub_f7d8d0();
    return;
}
```

## `TouchControlPanelUnityUiAddOn.TranslateEvent` — RVA `0xc552b8`

- Decompiled symbol: `TouchControlPanelUnityUiAddOn_TranslateEvent`
- Metadata signature: `private TouchControlPanel.SystemTouchEventData TranslateEvent(PointerEventData data) { }`
- Native interval: `112` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned long long field_10;
    unsigned long long field_18;
    unsigned int field_20;
    char field_24;
} struct_0;

typedef struct struct_1 {
    char padding_0[256];
    unsigned int field_100;
    unsigned long long field_104;
} struct_1;

typedef struct struct_3 {
    char padding_0[176];
    struct struct_2 *field_b0;
} struct_3;

typedef struct struct_2 {
    char padding_0[16];
    unsigned long long field_10;
    long long field_18;
    unsigned int field_20;
    char field_24;
} struct_2;

struct_0 * TouchControlPanelUnityUiAddOn_TranslateEvent(struct_3 *ptr, struct_1 *off)
{
    struct_2 *p;  // x8
    struct_2 *addr;  // x20
    long long v2;  // x0

    if (off)
    {
        p = ptr->field_b0;
        if (p)
        {
            p->field_20 = off->field_100;
            p->field_10 = *((long long *)&(&off->field_100)[1]);
            addr = ptr->field_b0;
            if (addr)
            {
                addr->field_24 = ((char)off->field_100 * 2 | (char)(off->field_100 >> 31)) & 1;
                v2 = PointerEventData__get_pressEventCamera(off, 0);
                addr->field_18 = v2;
                sub_f7d8d0((struct struct_2 *)&addr->field_18, v2);
                return ptr->field_b0;
            }
        }
    }
    sub_f7db74();
}
```

## `TouchControlPanelUnityUiAddOn.Awake` — RVA `0xc55328`

- Decompiled symbol: `TouchControlPanelUnityUiAddOn_Awake`
- Metadata signature: `protected override void Awake() { }`
- Native interval: `100` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[168];
    long long field_a8;
} struct_0;

extern long long g_1efd0c0;
extern char g_1fab275;

void TouchControlPanelUnityUiAddOn_Awake(struct_0 *ptr)
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
    if (!(g_1fab275 & 1))
    {
        sub_f7d92c(&g_1efd0c0);
        g_1fab275 = 1;
    }
    UIBehaviour__Awake(ptr, 0);
    ptr->field_a8 = sub_1231bc8(ptr, g_1efd0c0);
    sub_f7d8d0();
    return;
}
```

## `TouchControlPanelUnityUiAddOn.OnEnable` — RVA `0xc5538c`

- Decompiled symbol: `TouchControlPanelUnityUiAddOn_OnEnable`
- Metadata signature: `protected override void OnEnable() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long TouchControlPanelUnityUiAddOn_OnEnable(void)
{
}
```

## `TouchControlPanelUnityUiAddOn.Raycast` — RVA `0xc55394`

- Decompiled symbol: `TouchControlPanelUnityUiAddOn_Raycast`
- Metadata signature: `public override bool Raycast(Vector2 sp, Camera eventCamera) { }`
- Native interval: `180` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab276;

unsigned int TouchControlPanelUnityUiAddOn_Raycast(void* a0, long long a1)
{
    long long v0;  // x0

    if (!(g_1fab276 & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab276 = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v0 = Object__op_Equality((long long)a0[168], 0, 0);
    if (((char)Object__op_Equality((long long)a0[168], 0, 0) & 1))
        return 0;
    if ((long long)a0[168])
        return TouchControlPanel__Raycast((long long)a0[168], a1);
    sub_f7db74(0);
}
```

## `TouchControlPanelUnityUiAddOn.OnPointerDown` — RVA `0xc55448`

- Decompiled symbol: `TouchControlPanelUnityUiAddOn_OnPointerDown`
- Metadata signature: `private void UnityEngine.EventSystems.IPointerDownHandler.OnPointerDown(PointerEventData data) { }`
- Native interval: `164` bytes
- Result: `pseudocode`

```c
typedef struct struct_3 {
    char padding_0[176];
    struct struct_2 *field_b0;
} struct_3;

typedef struct struct_1 {
    char padding_0[256];
    unsigned int field_100;
    char padding_104[4];
    unsigned long long field_104;
} struct_1;

typedef struct struct_2 {
    char padding_0[16];
    unsigned long long field_10;
    long long field_18;
    unsigned int field_20;
    char field_24;
} struct_2;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab277;

long long TouchControlPanelUnityUiAddOn_OnPointerDown(struct_3 *a0, struct_1 *a1)
{
    unsigned long v0;  // x0
    void* v1;  // x0
    void* v2;  // x0

    if (!(g_1fab277 & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab277 = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v0 = Object__op_Inequality(*((long long *)&a0->padding_0[168]), 0, 0);
    if (!((char)v0 & 1))
        return v0;
    v1 = TouchControlPanelUnityUiAddOn__TranslateEvent(a0, a1);
    if (*((long long *)&a0->padding_0[168]))
    {
        v2 = TouchControlPanel__OnSystemTouchStart(*((long long *)&a0->padding_0[168]), v1);
        return TouchControlPanel__OnSystemTouchStart(*((long long *)&a0->padding_0[168]), v1);
    }
    sub_f7db74();
}
```

## `TouchControlPanelUnityUiAddOn.OnPointerUp` — RVA `0xc554ec`

- Decompiled symbol: `TouchControlPanelUnityUiAddOn_OnPointerUp`
- Metadata signature: `private void UnityEngine.EventSystems.IPointerUpHandler.OnPointerUp(PointerEventData data) { }`
- Native interval: `164` bytes
- Result: `pseudocode`

```c
typedef struct struct_3 {
    char padding_0[176];
    struct struct_2 *field_b0;
} struct_3;

typedef struct struct_1 {
    char padding_0[256];
    unsigned int field_100;
    char padding_104[4];
    unsigned long long field_104;
} struct_1;

typedef struct struct_2 {
    char padding_0[16];
    unsigned long long field_10;
    long long field_18;
    unsigned int field_20;
    char field_24;
} struct_2;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab278;

long long TouchControlPanelUnityUiAddOn_OnPointerUp(struct_3 *a0, struct_1 *a1)
{
    unsigned long v0;  // x0
    unsigned long v1;  // x0
    void* v2;  // x0

    if (!(g_1fab278 & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab278 = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v0 = Object__op_Inequality(*((long long *)&a0->padding_0[168]), 0, 0);
    if (!((char)v0 & 1))
        return v0;
    v1 = TouchControlPanelUnityUiAddOn__TranslateEvent(a0, a1);
    if (*((long long *)&a0->padding_0[168]))
    {
        v2 = TouchControlPanel__OnSystemTouchEnd(*((long long *)&a0->padding_0[168]), v1);
        return TouchControlPanel__OnSystemTouchEnd(*((long long *)&a0->padding_0[168]), v1);
    }
    sub_f7db74();
}
```

## `TouchControlPanelUnityUiAddOn.OnDrag` — RVA `0xc55590`

- Decompiled symbol: `TouchControlPanelUnityUiAddOn_OnDrag`
- Metadata signature: `private void UnityEngine.EventSystems.IDragHandler.OnDrag(PointerEventData data) { }`
- Native interval: `164` bytes
- Result: `pseudocode`

```c
typedef struct struct_3 {
    char padding_0[176];
    struct struct_2 *field_b0;
} struct_3;

typedef struct struct_1 {
    char padding_0[256];
    unsigned int field_100;
    char padding_104[4];
    unsigned long long field_104;
} struct_1;

typedef struct struct_2 {
    char padding_0[16];
    unsigned long long field_10;
    long long field_18;
    unsigned int field_20;
    char field_24;
} struct_2;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab279;

long long TouchControlPanelUnityUiAddOn_OnDrag(struct_3 *a0, struct_1 *a1)
{
    unsigned long v0;  // x0
    void* v1;  // x0
    void* v2;  // x0

    if (!(g_1fab279 & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab279 = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v0 = Object__op_Inequality(*((long long *)&a0->padding_0[168]), 0, 0);
    if (!((char)v0 & 1))
        return v0;
    v1 = TouchControlPanelUnityUiAddOn__TranslateEvent(a0, a1);
    if (*((long long *)&a0->padding_0[168]))
    {
        v2 = TouchControlPanel__OnSystemTouchMove(*((long long *)&a0->padding_0[168]), v1);
        return TouchControlPanel__OnSystemTouchMove(*((long long *)&a0->padding_0[168]), v1);
    }
    sub_f7db74();
}
```

## `TouchControlPanelUnityUiAddOn.UpdateGeometry` — RVA `0xc55634`

- Decompiled symbol: `TouchControlPanelUnityUiAddOn_UpdateGeometry`
- Metadata signature: `protected override void UpdateGeometry() { }`
- Native interval: `156` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab27a;

long long TouchControlPanelUnityUiAddOn_UpdateGeometry(long long a0)
{
    long long v0;  // x0
    long long v1;  // x0

    if (!(g_1fab27a & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab27a = 1;
    }
    v0 = Graphic__get_canvasRenderer(a0, 0);
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v1 = Object__op_Inequality(v0, 0, 0);
    if (!((char)v1 & 1))
    {
        return v1;
    }
    else if (!Graphic__get_canvasRenderer(a0, 0))
    {
        sub_f7db74();
    }
}
```

## `TouchControlPanelUnityUiAddOn.OnDrawGizmos` — RVA `0xc556d0`

- Decompiled symbol: `TouchControlPanelUnityUiAddOn_OnDrawGizmos`
- Metadata signature: `private void OnDrawGizmos() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long TouchControlPanelUnityUiAddOn_OnDrawGizmos(unsigned long a0)
{
    unsigned long long v0;  // x0

    v0 = TouchControlPanelUnityUiAddOn__DrawGizmos();
    return TouchControlPanelUnityUiAddOn__DrawGizmos();
}
```

## `TouchControlPanelUnityUiAddOn.DrawGizmos` — RVA `0xc556d8`

- Decompiled symbol: `TouchControlPanelUnityUiAddOn_DrawGizmos`
- Metadata signature: `private void DrawGizmos(bool selected) { }`
- Native interval: `352` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern unsigned long long g_1ef1170;
extern char g_1fab27b;

long long TouchControlPanelUnityUiAddOn_DrawGizmos(long long a0, unsigned int a1)
{
    long long v8;  // x0
    long long v9;  // x19
    long long v10;  // x0
    unsigned long v11;  // 4113
    unsigned long long v12;  // x0
    char v0;  // [bp-0xb0]
    uint128_t v1;  // [bp-0xa0]
    uint128_t v2;  // [bp-0x90]
    uint128_t v3;  // [bp-0x80]
    char v4;  // [bp-0x70]
    uint128_t v5;  // [bp-0x60]
    uint128_t v6;  // [bp-0x50]
    uint128_t v7;  // [bp-0x40]

    if (!(g_1fab27b & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c(&g_1ef1170);
        g_1fab27b = 1;
    }
    v8 = Component__get_transform(a0, 0);
    if (v8)
    {
        if (*((long long *)v8) == g_1ef1170)
            v9 = v8;
        else
            v9 = 0;
    }
    else
    {
        v9 = 0;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v10 = Object__op_Equality(v9, 0, 0);
    if (((char)v10 & 1))
        return v10;
    v11 = arm64g_calculate_condition(25, (unsigned long long)(a1 & 1), 0, 0);
    Gizmos__set_color();
    if (v9)
    {
        Transform__get_localToWorldMatrix(v9, 0);
        memcpy(&v0, &v4, 16);
        v1 = v5;
        v2 = v6;
        v3 = v7;
        Gizmos__set_matrix(&v0, 0);
        RectTransform__get_rect(v9, 0);
        RectTransform__get_rect(v9, 0);
        v12 = Gizmos__DrawWireCube(0);
        return Gizmos__DrawWireCube(0);
    }
    sub_f7db74();
}
```

## `TouchControlPanelUnityUiAddOn.OnDrawGizmosSelected` — RVA `0xc55838`

- Decompiled symbol: `TouchControlPanelUnityUiAddOn_OnDrawGizmosSelected`
- Metadata signature: `private void OnDrawGizmosSelected() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long TouchControlPanelUnityUiAddOn_OnDrawGizmosSelected(long long a0)
{
    long long v0;  // x0

    v0 = TouchControlPanelUnityUiAddOn__DrawGizmos(a0, 1);
    return TouchControlPanelUnityUiAddOn__DrawGizmos(a0, 1);
}
```
