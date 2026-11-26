# Native pseudocode: TouchControl

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `TouchControl.GetCamera` — RVA `0xc4da28`

- Decompiled symbol: `TouchControl_GetCamera`
- Metadata signature: `public Camera GetCamera() { }`
- Native interval: `156` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[96];
    unsigned long long field_60;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab252;

unsigned int TouchControl_GetCamera(struct_1 *ptr, unsigned long a1, unsigned long a2, unsigned long a3)
{
    unsigned long long v0;  // x0

    if (!(g_1fab252 & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab252 = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (!((char)Object__op_Inequality(ptr->field_60, 0, 0) & 1))
        return 0;
    v0 = ptr->field_60;
    if (v0)
    {
        if (Canvas__get_renderMode(v0, 0))
            v0 = ptr->field_60;
        else
            return 0;
    }
    sub_f7db74(v0);
}
```

## `TouchControl.GetScreenSpaceCenter` — RVA `0xc4e150`

- Decompiled symbol: `TouchControl_GetScreenSpaceCenter`
- Metadata signature: `public Vector2 GetScreenSpaceCenter(Camera cam) { }`
- Native interval: `184` bytes
- Result: `pseudocode`

```c
extern long long g_1ef0c58;
extern char g_1fab25a;

long long TouchControl_GetScreenSpaceCenter(long long a0, unsigned long a1)
{
    unsigned long long v7;  // d9
    unsigned long long v8;  // d8
    unsigned long long v9;  // x30
    unsigned long long v10;  // x22
    unsigned long long v11;  // x21
    unsigned long long v12;  // x20
    unsigned long long v13;  // x19
    unsigned long long v0;  // [bp-0x40]
    unsigned long long v1;  // [bp-0x38]
    unsigned long long v2;  // [bp-0x30]
    unsigned long long v3;  // [bp-0x20]
    unsigned long long v4;  // [bp-0x18]
    unsigned long long v5;  // [bp-0x10]
    unsigned long long v6;  // [bp-0x8]

    v0 = v7;
    v1 = v8;
    v2 = v9;
    v3 = v10;
    v4 = v11;
    v5 = v12;
    v6 = v13;
    if (!(g_1fab25a & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab25a = 1;
    }
    TouchControl__GetWorldSpaceCenter(a0); /* do not return */
}
```

## `TouchControl.IsActive` — RVA `0xc4ef30`

- Decompiled symbol: `TouchControl_IsActive`
- Metadata signature: `public bool IsActive() { }`
- Native interval: `16` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[80];
    unsigned int field_50;
} struct_0;

unsigned int TouchControl_IsActive(struct_0 *a0)
{
    unsigned long v0;  // 4118

    v0 = arm64g_calculate_condition(25, (unsigned long long)(a0->field_50 & 4294967231), 0, 0);
    if (!((char)v0))
        return 1;
    return 0;
}
```

## `TouchControl.get_rig` — RVA `0xc4f458`

- Decompiled symbol: `TouchControl_get_rig`
- Metadata signature: `public InputRig get_rig() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[88];
    unsigned long long field_58;
} struct_0;

long long TouchControl_get_rig(struct_0 *a0)
{
    return a0->field_58;
}
```

## `TouchControl.set_rig` — RVA `0xc4f460`

- Decompiled symbol: `TouchControl_set_rig`
- Metadata signature: `protected void set_rig(InputRig value) { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[88];
    unsigned long long field_58;
} struct_0;

long long TouchControl_set_rig(struct_0 *ptr, unsigned long a1)
{
    long long v0;  // x0

    ptr->field_58 = a1;
    v0 = sub_f7d8d0();
    return sub_f7d8d0();
}
```

## `TouchControl.get_canvas` — RVA `0xc4f468`

- Decompiled symbol: `TouchControl_get_canvas`
- Metadata signature: `public Canvas get_canvas() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[96];
    unsigned long long field_60;
} struct_0;

long long TouchControl_get_canvas(struct_0 *a0)
{
    return a0->field_60;
}
```

## `TouchControl.set_canvas` — RVA `0xc4f470`

- Decompiled symbol: `TouchControl_set_canvas`
- Metadata signature: `protected void set_canvas(Canvas value) { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[96];
    unsigned long long field_60;
} struct_0;

long long TouchControl_set_canvas(struct_0 *ptr, unsigned long a1)
{
    long long v0;  // x0

    ptr->field_60 = a1;
    v0 = sub_f7d8d0();
    return sub_f7d8d0();
}
```

## `TouchControl.get_panel` — RVA `0xc4f478`

- Decompiled symbol: `TouchControl_get_panel`
- Metadata signature: `public TouchControlPanel get_panel() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[104];
    unsigned long long field_68;
} struct_0;

long long TouchControl_get_panel(struct_0 *a0)
{
    return a0->field_68;
}
```

## `TouchControl.set_panel` — RVA `0xc4f480`

- Decompiled symbol: `TouchControl_set_panel`
- Metadata signature: `protected void set_panel(TouchControlPanel value) { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[104];
    unsigned long long field_68;
} struct_0;

long long TouchControl_set_panel(struct_0 *ptr, unsigned long a1)
{
    long long v0;  // x0

    ptr->field_68 = a1;
    v0 = sub_f7d8d0();
    return sub_f7d8d0();
}
```

## `TouchControl.ctor` — RVA `0xc4f488`

- Decompiled symbol: `TouchControl_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `292` bytes
- Result: `pseudocode`
- Heuristic layout hint: `TouchControl_Recovered` matched 4 offsets against `TouchControl` metadata (confidence 1.00).

```c
typedef struct TouchControl_Recovered {
    char padding_0[40];
    unsigned long long swipeOverOthersMode;
    long long swipeOverTargetList;
    char padding_38[8];
    long long animatorList;
    long long disablingConditions;
} TouchControl_Recovered;

extern long long g_1eed8d0;
extern long long g_1eed8d8;
extern long long g_1eef5c0;
extern long long g_1ef89e8;
extern long long g_1ef8a40;
extern char g_1fab24b;

void TouchControl_ctor(struct_0 *ptr)
{
    unsigned long long v8;  // x30
    unsigned long long v9;  // x25
    long long v18;  // x20
    struct_0 *p;  // x0
    long long v20;  // x0
    unsigned long long v10;  // x24
    unsigned long long v11;  // x23
    unsigned long long v12;  // x22
    unsigned long long v13;  // x21
    unsigned long long v14;  // x20
    unsigned long long v15;  // x19
    long long v16;  // x20
    struct_0 *addr;  // x0
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
    if (!(g_1fab24b & 1))
    {
        sub_f7d92c(&g_1eef5c0);
        sub_f7d92c(&g_1ef8a40);
        sub_f7d92c(&g_1ef89e8);
        sub_f7d92c(&g_1eed8d8);
        sub_f7d92c(&g_1eed8d0);
        g_1fab24b = 1;
    }
    ptr->field_28 = 8589934594;
    MonoBehaviour__ctor(ptr, 0);
    v16 = sub_f7db70(g_1eef5c0);
    DisablingConditionSet__ctor(v16, 0);
    addr = ptr;
    addr->field_48 = v16;
    sub_f7d8d0((struct TouchControl_Recovered *)&addr->field_48, v16);
    v18 = sub_f7db70(g_1eed8d8);
    sub_14a2bd4(v18, 2, g_1ef8a40);
    p = ptr;
    p->field_40 = v18;
    sub_f7d8d0((struct TouchControl_Recovered *)&p->field_40, v18);
    v20 = sub_f7db70(g_1eed8d0);
    sub_14a2bd4(v20, 2, g_1ef89e8);
    ptr->field_30 = v20;
    sub_f7d8d0();
    return;
}
```

## `TouchControl.GetSubBindingDescriptions` — RVA `0xc4f664`

- Decompiled symbol: `TouchControl_GetSubBindingDescriptions`
- Metadata signature: `public void GetSubBindingDescriptions(BindingDescriptionList descList, Object undoObject, string parentMenuPath) { }`
- Native interval: `16` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[584];
    unsigned long long field_248;
} struct_0;

long long TouchControl_GetSubBindingDescriptions(struct_0 **a0)
{
    goto *(a0)->field_248;
}
```

## `TouchControl.IsBoundToAxis` — RVA `0xc4f674`

- Decompiled symbol: `TouchControl_IsBoundToAxis`
- Metadata signature: `public bool IsBoundToAxis(string axisName, InputRig rig) { }`
- Native interval: `16` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[600];
    unsigned long long field_258;
} struct_0;

long long TouchControl_IsBoundToAxis(struct_0 **a0)
{
    goto *(a0)->field_258;
}
```

## `TouchControl.IsBoundToKey` — RVA `0xc4f684`

- Decompiled symbol: `TouchControl_IsBoundToKey`
- Metadata signature: `public bool IsBoundToKey(KeyCode key, InputRig rig) { }`
- Native interval: `16` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[616];
    unsigned long long field_268;
} struct_0;

long long TouchControl_IsBoundToKey(struct_0 **a0)
{
    goto *(a0)->field_268;
}
```

## `TouchControl.IsEmulatingTouches` — RVA `0xc4f694`

- Decompiled symbol: `TouchControl_IsEmulatingTouches`
- Metadata signature: `public bool IsEmulatingTouches() { }`
- Native interval: `16` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[632];
    unsigned long long field_278;
} struct_0;

long long TouchControl_IsEmulatingTouches(struct_0 **a0)
{
    goto *(a0)->field_278;
}
```

## `TouchControl.IsEmulatingMousePosition` — RVA `0xc4f6a4`

- Decompiled symbol: `TouchControl_IsEmulatingMousePosition`
- Metadata signature: `public bool IsEmulatingMousePosition() { }`
- Native interval: `16` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[648];
    unsigned long long field_288;
} struct_0;

long long TouchControl_IsEmulatingMousePosition(struct_0 **a0)
{
    goto *(a0)->field_288;
}
```

## `TouchControl.IsUsingKeyForEmulation` — RVA `0xc4f6b4`

- Decompiled symbol: `TouchControl_IsUsingKeyForEmulation`
- Metadata signature: `public virtual bool IsUsingKeyForEmulation(KeyCode key) { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
unsigned int TouchControl_IsUsingKeyForEmulation(void)
{
    return 0;
}
```

## `TouchControl.OnGetSubBindingDescriptions` — RVA `0xc4f6bc`

- Decompiled symbol: `TouchControl_OnGetSubBindingDescriptions`
- Metadata signature: `protected virtual void OnGetSubBindingDescriptions(BindingDescriptionList descList, Object undoObject, string parentMenuPath) { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long TouchControl_OnGetSubBindingDescriptions(void)
{
    unsigned long v0;  // x0

    return v0;
}
```

## `TouchControl.OnIsBoundToAxis` — RVA `0xc4f6c0`

- Decompiled symbol: `TouchControl_OnIsBoundToAxis`
- Metadata signature: `protected virtual bool OnIsBoundToAxis(string axisName, InputRig rig) { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
unsigned int TouchControl_OnIsBoundToAxis(void)
{
    return 0;
}
```

## `TouchControl.OnIsBoundToKey` — RVA `0xc4f6c8`

- Decompiled symbol: `TouchControl_OnIsBoundToKey`
- Metadata signature: `protected virtual bool OnIsBoundToKey(KeyCode key, InputRig rig) { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
unsigned int TouchControl_OnIsBoundToKey(void)
{
    return 0;
}
```

## `TouchControl.OnIsEmulatingTouches` — RVA `0xc4f6d0`

- Decompiled symbol: `TouchControl_OnIsEmulatingTouches`
- Metadata signature: `protected virtual bool OnIsEmulatingTouches() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
unsigned int TouchControl_OnIsEmulatingTouches(void)
{
    return 0;
}
```

## `TouchControl.OnIsEmulatingMousePosition` — RVA `0xc4f6d8`

- Decompiled symbol: `TouchControl_OnIsEmulatingMousePosition`
- Metadata signature: `protected virtual bool OnIsEmulatingMousePosition() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
unsigned int TouchControl_OnIsEmulatingMousePosition(void)
{
    return 0;
}
```

## `TouchControl.CheckSwipeOff` — RVA `0xc4f6e0`

- Decompiled symbol: `TouchControl_CheckSwipeOff`
- Metadata signature: `protected bool CheckSwipeOff(TouchObject touchObj, TouchControl.TouchStartType touchStartType) { }`
- Native interval: `112` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[48];
    long long field_30;
} struct_0;

typedef struct struct_1 {
    char padding_0[44];
    unsigned int field_2c;
} struct_1;

unsigned long long TouchControl_CheckSwipeOff(struct_1 *a0, struct_0 *a1, unsigned int a2)
{
    if (!a1)
    {
        return 0;
    }
    else if (a0->field_2c)
    {
        if (a2 != 2 && a0->field_2c == 2)
            return 0;
        TouchControl__ScreenToLocalPos(a0, a1->field_30);
        TouchControl__RaycastLocal(a0); /* do not return */
    }
    else
    {
        return 0;
    }
}
```

## `TouchControl.RaycastScreen` — RVA `0xc4f750`

- Decompiled symbol: `TouchControl_RaycastScreen`
- Metadata signature: `public bool RaycastScreen(Vector2 screenPos, Camera cam) { }`
- Native interval: `24` bytes
- Result: `pseudocode`

```c
long long TouchControl_RaycastScreen(long long a0)
{
    TouchControl__ScreenToLocalPos();
    TouchControl__RaycastLocal(a0); /* do not return */
}
```

## `TouchControl.CanShareTouchWith` — RVA `0xc4f768`

- Decompiled symbol: `TouchControl_CanShareTouchWith`
- Metadata signature: `public virtual bool CanShareTouchWith(TouchControl c) { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
unsigned int TouchControl_CanShareTouchWith(void)
{
    return 1;
}
```

## `TouchControl.CanBeSwipedOverFromNothingDefault` — RVA `0xc4f770`

- Decompiled symbol: `TouchControl_CanBeSwipedOverFromNothingDefault`
- Metadata signature: `protected bool CanBeSwipedOverFromNothingDefault(TouchObject touchObj) { }`
- Native interval: `32` bytes
- Result: `pseudocode`
- Heuristic layout hint: `TouchControl_Recovered` matched 2 offsets against `TouchControl` metadata (confidence 1.00).

```c
typedef struct TouchControl_Recovered {
    char padding_0[38];
    char canBeSwipedOver;
    char padding_27[41];
    unsigned int hidingFlagsCur;
} TouchControl_Recovered;

unsigned int TouchControl_CanBeSwipedOverFromNothingDefault(struct_0 *a0)
{
    unsigned long v0;  // 4118

    if (!a0->field_26)
        return 0;
    v0 = arm64g_calculate_condition(25, (unsigned long long)(a0->field_50 & 4294967231), 0, 0);
    if (!((char)v0))
        return 1;
    return 0;
}
```

## `TouchControl.CanBeSwipedOverFromRestrictedListDefault` — RVA `0xc4f790`

- Decompiled symbol: `TouchControl_CanBeSwipedOverFromRestrictedListDefault`
- Metadata signature: `protected bool CanBeSwipedOverFromRestrictedListDefault(TouchObject touchObj) { }`
- Native interval: `16` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[80];
    unsigned int field_50;
} struct_0;

unsigned int TouchControl_CanBeSwipedOverFromRestrictedListDefault(struct_0 *a0)
{
    unsigned long v0;  // 4118

    v0 = arm64g_calculate_condition(25, (unsigned long long)(a0->field_50 & 4294967231), 0, 0);
    if (!((char)v0))
        return 1;
    return 0;
}
```

## `TouchControl.CanSwipeOverOthersDefault` — RVA `0xc4f7a0`

- Decompiled symbol: `TouchControl_CanSwipeOverOthersDefault`
- Metadata signature: `protected bool CanSwipeOverOthersDefault(TouchObject touchObj, TouchObject myTouchObj, TouchControl.TouchStartType touchStartType) { }`
- Native interval: `56` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[40];
    unsigned int field_28;
} struct_0;

unsigned long long TouchControl_CanSwipeOverOthersDefault(struct_0 *a0, unsigned long a1, unsigned long a2, unsigned int a3)
{
    unsigned int v0;  // w8
    unsigned int v1;  // w9

    if (a2 == a1 && a0->field_28 != 1)
    {
        if (a0->field_28 != 2)
            v0 = 0;
        else
            v0 = 1;
        if (a3 == 2)
            v1 = 0;
        else
            v1 = 1;
        return v1 & v0;
    }
    if (a2 == a1)
        return 1;
    return 0;
}
```

## `TouchControl.CanBeTouchedDirectly` — RVA `0xc4f7d8`

- Decompiled symbol: `TouchControl_CanBeTouchedDirectly`
- Metadata signature: `public virtual bool CanBeTouchedDirectly(TouchObject touchObj) { }`
- Native interval: `32` bytes
- Result: `pseudocode`
- Heuristic layout hint: `TouchControl_Recovered` matched 2 offsets against `TouchControl` metadata (confidence 1.00).

```c
typedef struct TouchControl_Recovered {
    char padding_0[35];
    char cantBeControlledDirectly;
    char padding_24[44];
    unsigned int hidingFlagsCur;
} TouchControl_Recovered;

unsigned int TouchControl_CanBeTouchedDirectly(struct_0 *a0)
{
    unsigned long v0;  // 4118

    if (a0->field_23)
        return 0;
    v0 = arm64g_calculate_condition(25, (unsigned long long)(a0->field_50 & 4294967231), 0, 0);
    if (!((char)v0))
        return 1;
    return 0;
}
```

## `TouchControl.CanBeActivatedByOtherControl` — RVA `0xc4f7f8`

- Decompiled symbol: `TouchControl_CanBeActivatedByOtherControl`
- Metadata signature: `public virtual bool CanBeActivatedByOtherControl(TouchControl c, TouchObject touchObj) { }`
- Native interval: `16` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[80];
    unsigned int field_50;
} struct_0;

unsigned int TouchControl_CanBeActivatedByOtherControl(struct_0 *a0)
{
    unsigned long v0;  // 4118

    v0 = arm64g_calculate_condition(25, (unsigned long long)(a0->field_50 & 4294967231), 0, 0);
    if (!((char)v0))
        return 1;
    return 0;
}
```

## `TouchControl.CompareByDepth` — RVA `0xc4f808`

- Decompiled symbol: `TouchControl_CompareByDepth`
- Metadata signature: `public static int CompareByDepth(TouchControl a, TouchControl b) { }`
- Native interval: `376` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: Decompiler produced no C-like text

```c
// 0x104f808: str d8, [sp, #-0x30]!
// 0x104f80c: str x30, [sp, #8]
// 0x104f810: stp x22, x21, [sp, #0x10]
// 0x104f814: stp x20, x19, [sp, #0x20]
// 0x104f818: adrp x22, #0x1fab000
// 0x104f81c: adrp x21, #0x1e8c000
// 0x104f820: ldrb w8, [x22, #0x24c]
// 0x104f824: ldr x21, [x21, #0xd8]
// 0x104f828: mov x20, x1
// 0x104f82c: mov x19, x0
// 0x104f830: tbnz w8, #0, #0x104f848
// 0x104f834: adrp x0, #0x1e8c000
// 0x104f838: ldr x0, [x0, #0xd8]
// 0x104f83c: bl #0xf7d92c
// 0x104f840: mov w8, #1
// 0x104f844: strb w8, [x22, #0x24c]
// 0x104f848: ldr x0, [x21]
// 0x104f84c: ldr w8, [x0, #0xe0]
// 0x104f850: cbnz w8, #0x104f858
// 0x104f854: bl #0xf7da5c
// 0x104f858: mov x0, x19
// 0x104f85c: mov x1, xzr
// 0x104f860: mov x2, xzr
// 0x104f864: bl #0x1b9568c
// 0x104f868: tbnz w0, #0, #0x104f890
// 0x104f86c: ldr x0, [x21]
// 0x104f870: ldr w8, [x0, #0xe0]
// 0x104f874: cbnz w8, #0x104f87c
// 0x104f878: bl #0xf7da5c
// 0x104f87c: mov x0, x20
// 0x104f880: mov x1, xzr
// 0x104f884: mov x2, xzr
// 0x104f888: bl #0x1b9568c
// 0x104f88c: tbz w0, #0, #0x104f908
// 0x104f890: ldr x0, [x21]
// 0x104f894: ldr w8, [x0, #0xe0]
// 0x104f898: cbnz w8, #0x104f8a0
// 0x104f89c: bl #0xf7da5c
// 0x104f8a0: mov x0, x19
// 0x104f8a4: mov x1, xzr
// 0x104f8a8: mov x2, xzr
// 0x104f8ac: bl #0x1b9568c
// 0x104f8b0: tbz w0, #0, #0x104f8d8
// 0x104f8b4: ldr x0, [x21]
// 0x104f8b8: ldr w8, [x0, #0xe0]
// 0x104f8bc: cbnz w8, #0x104f8c4
// 0x104f8c0: bl #0xf7da5c
// 0x104f8c4: mov x0, x20
// 0x104f8c8: mov x1, xzr
// 0x104f8cc: mov x2, xzr
// 0x104f8d0: bl #0x1b9568c
// 0x104f8d4: tbnz w0, #0, #0x104f964
// 0x104f8d8: ldr x0, [x21]
// 0x104f8dc: ldr w8, [x0, #0xe0]
// 0x104f8e0: cbnz w8, #0x104f8e8
// 0x104f8e4: bl #0xf7da5c
// 0x104f8e8: mov x0, x19
// 0x104f8ec: mov x1, xzr
// 0x104f8f0: mov x2, xzr
// 0x104f8f4: bl #0x1b9568c
// 0x104f8f8: tst w0, #1
// 0x104f8fc: mov w8, #1
// 0x104f900: cneg w0, w8, eq
// 0x104f904: b #0x104f968
// 0x104f908: cbz x19, #0x104f97c
// 0x104f90c: mov x0, x19
// 0x104f910: mov x1, xzr
// 0x104f914: bl #0x1b92154
// 0x104f918: cbz x0, #0x104f97c
// 0x104f91c: mov x1, xzr
// 0x104f920: bl #0x1b9d508
// 0x104f924: mov x0, x19
// 0x104f928: mov x1, xzr
// 0x104f92c: mov v8.16b, v2.16b
// 0x104f930: bl #0x1b92154
// 0x104f934: cbz x0, #0x104f97c
// 0x104f938: mov x1, xzr
// 0x104f93c: bl #0x1b9d508
// 0x104f940: adrp x8, #0x832000
// 0x104f944: ldr s0, [x8, #0x534]
// 0x104f948: fabd s1, s8, s2
// 0x104f94c: fcmp s1, s0
// 0x104f950: b.mi #0x104f964
// 0x104f954: fcmp s8, s2
// 0x104f958: mov w8, #-1
// 0x104f95c: csinc w0, w8, wzr, mi
// 0x104f960: b #0x104f968
// 0x104f964: mov w0, wzr
// 0x104f968: ldp x20, x19, [sp, #0x20]
// 0x104f96c: ldp x22, x21, [sp, #0x10]
// 0x104f970: ldr x30, [sp, #8]
// 0x104f974: ldr d8, [sp], #0x30
// 0x104f978: ret
// 0x104f97c: bl #0xf7db74
```

## `TouchControl.ShowOrHideControl` — RVA `0xc4f980`

- Decompiled symbol: `TouchControl_ShowOrHideControl`
- Metadata signature: `public void ShowOrHideControl(bool show, bool noAnim = false) { }`
- Native interval: `80` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    struct struct_0 *field_0;
    char padding_8[72];
    unsigned int field_50;
} struct_2;

typedef struct struct_0 {
    char padding_0[680];
    struct struct_1 *field_2a8;
    unsigned long long field_2b0;
} struct_0;

typedef struct struct_1 {
    unsigned long long field_0;
} struct_1;

long long TouchControl_ShowOrHideControl(struct_2 *ptr, unsigned int a1, unsigned int a2)
{
    unsigned int v0;  // w8
    unsigned long v1;  // 4169
    struct_2 *v2;  // x0
    unsigned long v3;  // x1
    unsigned long long v4;  // x0

    v0 = ptr->field_50 & 4294967294 | (ptr->field_50 & 4294967294 | ~(a1) & 1) & 1;
    ptr->field_50 = v0;
    v1 = arm64g_calculate_condition(9, (unsigned long long)(v0 & 4294967231), 0, 0);
    if ((char)v1)
    {
        v4 = TouchControl__SyncBaseAlphaToHidingConditions(ptr, a2 & 1);
        return TouchControl__SyncBaseAlphaToHidingConditions(ptr, a2 & 1);
    }
    v2 = ptr;
    v3 = ptr->field_0->field_2b0;
    ptr->field_0->field_2a8();
}
```

## `TouchControl.SetHidingFlag` — RVA `0xc4f9d0`

- Decompiled symbol: `TouchControl_SetHidingFlag`
- Metadata signature: `public void SetHidingFlag(int flagBit, bool state) { }`
- Native interval: `68` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    struct struct_0 *field_0;
    char padding_8[72];
    unsigned int field_50;
} struct_1;

typedef struct struct_0 {
    char padding_0[680];
    unsigned long long field_2a8;
} struct_0;

struct_1 * TouchControl_SetHidingFlag(struct_1 *ptr, unsigned int a1, unsigned int a2)
{
    unsigned int v0;  // w9
    unsigned long v1;  // 4152
    unsigned int v2;  // w8
    unsigned long v3;  // 4114

    if (31 < a1)
        return ptr;
    v0 = 1 << ((char)a1 & 31);
    v1 = arm64g_calculate_condition(25, (unsigned long long)(a2 & 1), 0, 0);
    if ((char)v1)
        v2 = ptr->field_50 | v0;
    else
        v2 = ptr->field_50 & ~(v0);
    ptr->field_50 = v2;
    v3 = arm64g_calculate_condition(9, (unsigned long long)(v2 & 4294967231), 0, 0);
    if ((char)v3)
        return ptr;
    goto ptr->field_0->field_2a8;
}
```

## `TouchControl.SyncBaseAlphaToHidingConditions` — RVA `0xc4fa14`

- Decompiled symbol: `TouchControl_SyncBaseAlphaToHidingConditions`
- Metadata signature: `private void SyncBaseAlphaToHidingConditions(bool noAnim) { }`
- Native interval: `252` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: Decompiler produced no C-like text

```c
// 0x104fa14: stp d9, d8, [sp, #-0x30]!
// 0x104fa18: stp x30, x21, [sp, #0x10]
// 0x104fa1c: stp x20, x19, [sp, #0x20]
// 0x104fa20: adrp x21, #0x1fab000
// 0x104fa24: ldrb w8, [x21, #0x251]
// 0x104fa28: mov w20, w1
// 0x104fa2c: mov x19, x0
// 0x104fa30: tbnz w8, #0, #0x104fa48
// 0x104fa34: adrp x0, #0x1e8c000
// 0x104fa38: ldr x0, [x0, #0xd8]
// 0x104fa3c: bl #0xf7d92c
// 0x104fa40: mov w8, #1
// 0x104fa44: strb w8, [x21, #0x251]
// 0x104fa48: ldr w8, [x19, #0x50]
// 0x104fa4c: ldrb w9, [x19, #0x71]
// 0x104fa50: fmov s8, wzr
// 0x104fa54: fmov s0, #1.00000000
// 0x104fa58: cmp w8, #0
// 0x104fa5c: mov w10, #0x78
// 0x104fa60: mov w11, #0x7c
// 0x104fa64: fcsel s9, s0, s8, eq
// 0x104fa68: cmp w9, #0
// 0x104fa6c: csel x8, x11, x10, eq
// 0x104fa70: ldr s0, [x19, x8]
// 0x104fa74: adrp x8, #0x832000
// 0x104fa78: ldr s1, [x8, #0x534]
// 0x104fa7c: fabd s0, s9, s0
// 0x104fa80: fcmp s0, s1
// 0x104fa84: b.le #0x104fafc
// 0x104fa88: tbnz w20, #0, #0x104fac8
// 0x104fa8c: adrp x8, #0x1e8c000
// 0x104fa90: ldr x8, [x8, #0xd8]
// 0x104fa94: ldr x20, [x19, #0x58]
// 0x104fa98: ldr x0, [x8]
// 0x104fa9c: ldr w8, [x0, #0xe0]
// 0x104faa0: cbnz w8, #0x104faa8
// 0x104faa4: bl #0xf7da5c
// 0x104faa8: mov x0, x20
// 0x104faac: mov x1, xzr
// 0x104fab0: mov x2, xzr
// 0x104fab4: bl #0x1b9568c
// 0x104fab8: tbnz w0, #0, #0x104fac8
// 0x104fabc: ldr x8, [x19, #0x58]
// 0x104fac0: cbz x8, #0x104fb0c
// 0x104fac4: ldr s8, [x8, #0x54]
// 0x104fac8: adrp x8, #0x832000
// 0x104facc: ldr s0, [x8, #0x2e8]
// 0x104fad0: ldr s1, [x19, #0x7c]
// 0x104fad4: fcmp s8, s0
// 0x104fad8: stp s1, s9, [x19, #0x74]
// 0x104fadc: b.ls #0x104faf4
// 0x104fae0: mov w8, #1
// 0x104fae4: str wzr, [x19, #0x84]
// 0x104fae8: strb w8, [x19, #0x71]
// 0x104faec: str s8, [x19, #0x80]
// 0x104faf0: b #0x104fafc
// 0x104faf4: strb wzr, [x19, #0x71]
// 0x104faf8: str s9, [x19, #0x7c]
// 0x104fafc: ldp x20, x19, [sp, #0x20]
// 0x104fb00: ldp x30, x21, [sp, #0x10]
// 0x104fb04: ldp d9, d8, [sp], #0x30
// 0x104fb08: ret
// 0x104fb0c: bl #0xf7db74
```

## `TouchControl.ShowControl` — RVA `0xc4fb10`

- Decompiled symbol: `TouchControl_ShowControl`
- Metadata signature: `public void ShowControl(bool noAnim = false) { }`
- Native interval: `12` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    struct struct_0 *field_0;
    char padding_8[72];
    unsigned int field_50;
} struct_2;

typedef struct struct_0 {
    char padding_0[680];
    struct struct_1 *field_2a8;
    unsigned long long field_2b0;
} struct_0;

typedef struct struct_1 {
    unsigned long long field_0;
} struct_1;

long long TouchControl_ShowControl(struct_2 *a0, unsigned int a1)
{
    long long v0;  // x0

    v0 = TouchControl__ShowOrHideControl(a0, 1, a1 & 1);
    return TouchControl__ShowOrHideControl(a0, 1, a1 & 1);
}
```

## `TouchControl.HideControl` — RVA `0xc4fb1c`

- Decompiled symbol: `TouchControl_HideControl`
- Metadata signature: `public void HideControl(bool noAnim = false) { }`
- Native interval: `12` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    struct struct_0 *field_0;
    char padding_8[72];
    unsigned int field_50;
} struct_2;

typedef struct struct_0 {
    char padding_0[680];
    struct struct_1 *field_2a8;
    unsigned long long field_2b0;
} struct_0;

typedef struct struct_1 {
    unsigned long long field_0;
} struct_1;

long long TouchControl_HideControl(struct_2 *a0, unsigned int a1)
{
    long long v0;  // x0

    v0 = TouchControl__ShowOrHideControl(a0, 0, a1 & 1);
    return TouchControl__ShowOrHideControl(a0, 0, a1 & 1);
}
```

## `TouchControl.IsHiddenManually` — RVA `0xc4fb28`

- Decompiled symbol: `TouchControl_IsHiddenManually`
- Metadata signature: `public bool IsHiddenManually() { }`
- Native interval: `16` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[80];
    unsigned int field_50;
} struct_0;

unsigned long long TouchControl_IsHiddenManually(struct_0 *a0)
{
    if (a0->field_50)
        return 1;
    return 0;
}
```

## `TouchControl.ToggleVisibility` — RVA `0xc4fb38`

- Decompiled symbol: `TouchControl_ToggleVisibility`
- Metadata signature: `public void ToggleVisibility(bool noAnim) { }`
- Native interval: `24` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    struct struct_0 *field_0;
    char padding_8[72];
    unsigned int field_50;
} struct_2;

typedef struct struct_0 {
    char padding_0[680];
    struct struct_1 *field_2a8;
    unsigned long long field_2b0;
} struct_0;

typedef struct struct_1 {
    unsigned long long field_0;
} struct_1;

long long TouchControl_ToggleVisibility(struct_2 *a0, unsigned int a1)
{
    unsigned int v0;  // w8
    long long v1;  // x0

    if (!a0->field_50)
        v0 = 0;
    else
        v0 = 1;
    v1 = TouchControl__ShowOrHideControl(a0, v0, a1 & 1);
    return TouchControl__ShowOrHideControl(a0, v0, a1 & 1);
}
```

## `TouchControl.ToggleVisibility` — RVA `0xc4fb50`

- Decompiled symbol: `TouchControl_ToggleVisibility`
- Metadata signature: `public void ToggleVisibility() { }`
- Native interval: `20` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    struct struct_0 *field_0;
    char padding_8[72];
    unsigned int field_50;
} struct_2;

typedef struct struct_0 {
    char padding_0[680];
    struct struct_1 *field_2a8;
    unsigned long long field_2b0;
} struct_0;

typedef struct struct_1 {
    unsigned long long field_0;
} struct_1;

long long TouchControl_ToggleVisibility(struct_2 *a0)
{
    unsigned int v0;  // w1
    long long v1;  // x0

    if (!a0->field_50)
        v0 = 0;
    else
        v0 = 1;
    v1 = TouchControl__ShowOrHideControl(a0, v0, 0);
    return TouchControl__ShowOrHideControl(a0, v0, 0);
}
```

## `TouchControl.IsActiveButInvisible` — RVA `0xc4fb64`

- Decompiled symbol: `TouchControl_IsActiveButInvisible`
- Metadata signature: `public bool IsActiveButInvisible() { }`
- Native interval: `64` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    struct struct_0 *field_0;
    char padding_8[72];
    unsigned int field_50;
} struct_2;

typedef struct struct_0 {
    char padding_0[856];
    struct struct_1 *field_358;
    unsigned long long field_360;
} struct_0;

typedef struct struct_1 {
    unsigned long long field_0;
} struct_1;

unsigned int TouchControl_IsActiveButInvisible(struct_2 *a0)
{
    unsigned long v0;  // 4120
    unsigned long long v1;  // x1

    v0 = arm64g_calculate_condition(9, (unsigned long long)(a0->field_50 & 4294967231), 0, 0);
    if (!((char)v0))
        return 0;
    v1 = a0->field_0->field_360;
    a0->field_0->field_358();
}
```

## `TouchControl.IsActiveAndVisible` — RVA `0xc4fba4`

- Decompiled symbol: `TouchControl_IsActiveAndVisible`
- Metadata signature: `public bool IsActiveAndVisible() { }`
- Native interval: `64` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    struct struct_0 *field_0;
    char padding_8[72];
    unsigned int field_50;
} struct_2;

typedef struct struct_0 {
    char padding_0[856];
    struct struct_1 *field_358;
    unsigned long long field_360;
} struct_0;

typedef struct struct_1 {
    unsigned long long field_0;
} struct_1;

unsigned int TouchControl_IsActiveAndVisible(struct_2 *a0)
{
    unsigned long v0;  // 4120
    unsigned long long v1;  // x1

    v0 = arm64g_calculate_condition(9, (unsigned long long)(a0->field_50 & 4294967231), 0, 0);
    if (!((char)v0))
        return 0;
    v1 = a0->field_0->field_360;
    a0->field_0->field_358();
}
```

## `TouchControl.SyncDisablingConditions` — RVA `0xc4fbe4`

- Decompiled symbol: `TouchControl_SyncDisablingConditions`
- Metadata signature: `public void SyncDisablingConditions(bool skipAnim) { }`
- Native interval: `380` bytes
- Result: `pseudocode`
- Heuristic layout hint: `TouchControl_Recovered` matched 3 offsets against `TouchControl` metadata (confidence 0.75).

```c
typedef struct TouchControl_Recovered {
    struct struct_1 *field_0;
    char padding_8[64];
    unsigned long long disablingConditions;
    unsigned int hidingFlagsCur;
    char padding_54[4];
    struct struct_3 *_rig;
} TouchControl_Recovered;

typedef struct struct_5 {
    char padding_0[304];
    char field_130;
} struct_5;

typedef struct struct_1 {
    char padding_0[680];
    struct struct_2 *field_2a8;
    unsigned long long field_2b0;
} struct_1;

typedef struct struct_3 {
    char padding_0[304];
    char field_130;
} struct_3;

typedef struct struct_2 {
    unsigned long long field_0;
} struct_2;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab24d;

unsigned long long TouchControl_SyncDisablingConditions(struct_4 *ptr, unsigned int a1)
{
    unsigned long v0;  // x20
    unsigned long v1;  // 4114
    unsigned int v10;  // w8
    unsigned long v11;  // 4128
    struct_4 *v12;  // x0
    unsigned long v13;  // x1
    unsigned int v14;  // w8
    unsigned long v15;  // 4140
    struct_4 *v16;  // x0
    unsigned long v17;  // x1
    unsigned long long v18;  // x0
    unsigned long long v19;  // x0
    unsigned int v2;  // w8
    unsigned int v3;  // w8
    unsigned long v4;  // 4138
    struct_4 *v5;  // x0
    unsigned long v6;  // x1
    unsigned long long flag;  // x2
    unsigned long v8;  // 4120
    unsigned int v9;  // w9

    v0 = a1;
    if (!(g_1fab24d & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab24d = 1;
    }
    if (!((char)Behaviour__get_enabled(ptr, 0) & 1))
    {
        v2 = 2;
    }
    else if (Component__get_gameObject(ptr, 0))
    {
        v1 = arm64g_calculate_condition(25, (unsigned long long)((unsigned int)(unsigned long long)GameObject__get_activeInHierarchy() & 1), 0, 0);
        if ((char)v1)
            v2 = 0;
        else
            v2 = 2;
    }
    else
    {
        sub_f7db74();
    }
    if (ptr)
    {
        v3 = ptr->field_50 & 4294967293 | v2;
        ptr->field_50 = v3;
        v4 = arm64g_calculate_condition(9, (unsigned long long)(v3 & 4294967231), 0, 0);
        if (!((char)v4))
        {
            v5 = ptr;
            v6 = ptr->field_0->field_2b0;
            ptr->field_0->field_2a8();
        }
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        flag = 0;
        if (!((char)Object__op_Inequality(ptr->field_58, 0, 0) & 1))
        {
LABEL_104fd2c:
            v18 = TouchControl__SyncBaseAlphaToHidingConditions(ptr, (unsigned int)v0 & 1);
            if (!((char)v0 & 1))
                return v18;
            v19 = TouchControl__UpdateAnimators(ptr, 1);
            return TouchControl__UpdateAnimators(ptr, 1);
        }
        else if (ptr->field_48)
        {
            v8 = arm64g_calculate_condition(25, (unsigned long long)((unsigned int)(unsigned long long)DisablingConditionSet__IsInEffect() & 1), 0, 0);
            if ((char)v8)
                v9 = 16;
            else
                v9 = 0;
            v10 = ptr->field_50 & 4294967279 | v9;
            ptr->field_50 = v10;
            v11 = arm64g_calculate_condition(9, (unsigned long long)(v10 & 4294967231), 0, 0);
            if (!((char)v11))
            {
                v12 = ptr;
                v13 = ptr->field_0->field_2b0;
                ptr->field_0->field_2a8();
            }
            if (ptr->field_58)
            {
                v14 = ptr->field_50 & 4294967263 | ptr->field_58->field_130 * 32;
                ptr->field_50 = v14;
                v15 = arm64g_calculate_condition(9, (unsigned long long)(v14 & 4294967231), 0, 0);
                if (!((char)v15))
                {
                    v16 = ptr;
                    v17 = ptr->field_0->field_2b0;
                    ptr->field_0->field_2a8();
                }
                goto LABEL_104fd2c;
            }
        }
    }
    sub_f7db74();
}
```

## `TouchControl.UpdateAnimators` — RVA `0xc4fe90`

- Decompiled symbol: `TouchControl_UpdateAnimators`
- Metadata signature: `protected void UpdateAnimators(bool skipAnim) { }`
- Native interval: `160` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    char padding_0[24];
    unsigned int field_18;
} struct_2;

typedef struct struct_1 {
    char padding_0[64];
    struct struct_0 *field_40;
} struct_1;

typedef struct struct_0 {
    char padding_0[24];
    int field_18;
} struct_0;

extern long long g_1ef8a60;
extern long long g_1ef8a68;
extern char g_1fab250;

struct_2 * TouchControl_UpdateAnimators(struct_1 *ptr, unsigned long a1)
{
    struct_0 *v0;  // x0
    int v1;  // w20
    unsigned long v2;  // x0

    if (!(g_1fab250 & 1))
    {
        sub_f7d92c(&g_1ef8a60);
        sub_f7d92c(&g_1ef8a68);
        g_1fab250 = 1;
    }
    v0 = ptr->field_40;
    if (v0)
    {
        v1 = 0;
        do
        {
            if (v0->field_18 <= v1)
                return v0;
        } while ((v0 = (struct_0 *)(unsigned long long)sub_14a30c0(), v0 && (TouchControlAnimatorBase__UpdateAnimator(), v0 = (struct_0 *)ptr->field_40, v1 = (int)(v1 + 1), v0)));
    }
    v2 = sub_f7db74(v0);
    return sub_f7db74(v0);
}
```

## `TouchControl.AddAnimator` — RVA `0xc4ff30`

- Decompiled symbol: `TouchControl_AddAnimator`
- Metadata signature: `public void AddAnimator(TouchControlAnimatorBase a) { }`
- Native interval: `228` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[64];
    struct struct_0 *field_40;
} struct_1;

typedef struct struct_0 {
    char padding_0[16];
    unsigned long long field_10;
    unsigned int field_18;
    unsigned int field_1c;
} struct_0;

extern long long g_1ef8a48;
extern long long g_1ef8a50;
extern char g_1fab24e;

long long TouchControl_AddAnimator(struct_1 *p, long long a1)
{
    struct_0 *ptr;  // x0
    long long v1;  // x0
    unsigned long long v2;  // x8
    unsigned long v3;  // x10
    long long v4;  // x0
    long long v5;  // x0

    if (!(g_1fab24e & 1))
    {
        sub_f7d92c(&g_1ef8a48);
        sub_f7d92c(&g_1ef8a50);
        g_1fab24e = 1;
    }
    ptr = p->field_40;
    if (ptr)
    {
        v1 = sub_14a36c0(ptr, a1, g_1ef8a50);
        if (((char)v1 & 1))
            return v1;
        ptr = p->field_40;
        if (ptr)
        {
            v2 = ptr->field_10;
            ptr->field_1c = ptr->field_1c + 1;
            if (v2)
            {
                v3 = ptr->field_18;
                if (*((int *)(v2 + 24)) <= (unsigned int)v3)
                {
                    v5 = sub_14a3390();
                    return sub_14a3390();
                }
                ptr->field_18 = (unsigned int)v3 + 1;
                *((long long *)(v2 + v3 * 8 + 32)) = a1;
                v4 = sub_f7d8d0();
                return sub_f7d8d0();
            }
        }
    }
    sub_f7db74(ptr);
}
```

## `TouchControl.RemoveAnimator` — RVA `0xc50014`

- Decompiled symbol: `TouchControl_RemoveAnimator`
- Metadata signature: `public void RemoveAnimator(TouchControlAnimatorBase a) { }`
- Native interval: `144` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[64];
    unsigned long long field_40;
} struct_0;

extern long long g_1ef8a50;
extern long long g_1ef8a58;
extern char g_1fab24f;

long long TouchControl_RemoveAnimator(struct_0 *ptr, long long a1)
{
    unsigned long long v0;  // x0
    long long v1;  // x0

    if (!(g_1fab24f & 1))
    {
        sub_f7d92c(&g_1ef8a50);
        sub_f7d92c(&g_1ef8a58);
        g_1fab24f = 1;
    }
    v0 = ptr->field_40;
    if (v0)
    {
        v1 = sub_14a36c0(v0, a1, g_1ef8a50);
        if (!((char)v1 & 1))
            return v1;
        v0 = ptr->field_40;
    }
    sub_f7db74(v0);
}
```

## `TouchControl.GetAnimatorList` — RVA `0xc500a4`

- Decompiled symbol: `TouchControl_GetAnimatorList`
- Metadata signature: `public List<TouchControlAnimatorBase> GetAnimatorList() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[64];
    unsigned long long field_40;
} struct_0;

long long TouchControl_GetAnimatorList(struct_0 *a0)
{
    return a0->field_40;
}
```

## `TouchControl.StartAlphaAnim` — RVA `0xc500ac`

- Decompiled symbol: `TouchControl_StartAlphaAnim`
- Metadata signature: `private void StartAlphaAnim(float targetAlpha, float duration) { }`
- Native interval: `56` bytes
- Result: `pseudocode`
- Heuristic layout hint: `TouchControl_Recovered` matched 6 offsets against `TouchControl` metadata (confidence 1.00).

```c
typedef struct TouchControl_Recovered {
    char padding_0[113];
    char baseAlphaAnimOn;
    char padding_72[2];
    unsigned int baseAlphaStart;
    unsigned int baseAlphaEnd;
    unsigned int baseAlphaCur;
    unsigned int baseAlphaAnimDur;
    unsigned int baseAlphaAnimElapsed;
} TouchControl_Recovered;

struct_0 * TouchControl_StartAlphaAnim(struct_0 *ptr)
{
    unsigned int v0;  // s0
    unsigned int v1;  // s1
    unsigned long v2;  // 4141

    ptr->field_74 = ptr->field_7c;
    ptr->field_78 = v0;
    v2 = arm64g_calculate_condition(144, (((((unsigned long long)(char)(CmpF(v1, 953267991)) >> 5 & 3 | (unsigned long long)(CmpF(v1, 953267991) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v1, 953267991)) >> 5 & 3 | (unsigned long long)(CmpF(v1, 953267991) & 1)) & ((unsigned long long)(char)(CmpF(v1, 953267991)) >> 5 & 3 | (unsigned long long)(CmpF(v1, 953267991) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if ((char)v2)
    {
        ptr->field_71 = 0;
        ptr->field_7c = v0;
        return ptr;
    }
    ptr->field_84 = 0;
    ptr->field_71 = 1;
    ptr->field_80 = v1;
    return ptr;
}
```

## `TouchControl.UpdateBaseAlpha` — RVA `0xc500e4`

- Decompiled symbol: `TouchControl_UpdateBaseAlpha`
- Metadata signature: `private void UpdateBaseAlpha() { }`
- Native interval: `116` bytes
- Result: `pseudocode`
- Heuristic layout hint: `TouchControl_Recovered` matched 6 offsets against `TouchControl` metadata (confidence 1.00).

```c
typedef struct TouchControl_Recovered {
    char padding_0[113];
    char baseAlphaAnimOn;
    char padding_72[2];
    unsigned int baseAlphaStart;
    unsigned int baseAlphaEnd;
    unsigned int baseAlphaCur;
    unsigned int baseAlphaAnimDur;
    unsigned int baseAlphaAnimElapsed;
} TouchControl_Recovered;

void TouchControl_UpdateBaseAlpha(struct_0 *ptr)
{
    unsigned int v0;  // s1
    unsigned int v1;  // s0
    unsigned int v2;  // s0
    unsigned long v3;  // 4146
    unsigned int v4;  // s1
    unsigned int v5;  // s0
    unsigned long v6;  // 4154
    unsigned int v7;  // s0

    if (!ptr->field_71)
        return;
    CFUtils__get_realDeltaTime();
    v0 = ptr->field_80;
    v2 = ptr->field_84 + v1;
    ptr->field_84 = v2;
    v3 = arm64g_calculate_condition(160, (((((unsigned long long)(char)(CmpF(v2, v0)) >> 5 & 3 | (unsigned long long)(CmpF(v2, v0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v2, v0)) >> 5 & 3 | (unsigned long long)(CmpF(v2, v0) & 1)) & ((unsigned long long)(char)(CmpF(v2, v0)) >> 5 & 3 | (unsigned long long)(CmpF(v2, v0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if (!((char)v3))
    {
        v4 = [D] unsupported_Iop_ZeroHI96ofV128();
        v5 = 0;
        v6 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v2 / v0, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v2 / v0, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v2 / v0, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v2 / v0, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v2 / v0, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v2 / v0, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if ((char)v6)
            v5 = v4;
        v7 = ptr->field_74 + v5 * (ptr->field_78 - ptr->field_74);
    }
    else
    {
        v7 = ptr->field_78;
        ptr->field_71 = 0;
    }
    ptr->field_7c = v7;
    return;
}
```

## `TouchControl.GetBaseAlpha` — RVA `0xc50158`

- Decompiled symbol: `TouchControl_GetBaseAlpha`
- Metadata signature: `public float GetBaseAlpha() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long TouchControl_GetBaseAlpha(unsigned long a0)
{
    return a0;
}
```

## `TouchControl.GetAlpha` — RVA `0xc50160`

- Decompiled symbol: `TouchControl_GetAlpha`
- Metadata signature: `public virtual float GetAlpha() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long TouchControl_GetAlpha(unsigned long a0)
{
    return a0;
}
```

## `TouchControl.SetRig` — RVA `0xc50168`

- Decompiled symbol: `TouchControl_SetRig`
- Metadata signature: `public void SetRig(InputRig rig) { }`
- Native interval: `376` bytes
- Result: `pseudocode`
- Heuristic layout hint: `TouchControl_Recovered` matched 2 offsets against `TouchControl` metadata (confidence 1.00).

```c
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

typedef struct TouchControl_Recovered {
    char padding_0[72];
    struct struct_6 *disablingConditions;
    char padding_50[8];
    struct struct_5 *_rig;
} TouchControl_Recovered;

typedef struct struct_6 {
    char padding_0[32];
    struct struct_5 *field_20;
} struct_6;

typedef struct struct_1 {
    unsigned long long field_0;
} struct_1;

typedef struct struct_5 {
    struct struct_3 *field_0;
    char padding_8[24];
    char field_20;
    char field_21;
} struct_5;

typedef struct struct_3 {
    char padding_0[376];
    struct struct_4 *field_178;
    unsigned long long field_180;
} struct_3;

typedef struct struct_4 {
    unsigned long long field_0;
} struct_4;

typedef struct struct_8 {
    char padding_0[224];
    unsigned int field_e0;
} struct_8;

extern struct_8 *g_1ef0c58;
extern char g_1fab253;
extern char g_20;

unsigned long long TouchControl_SetRig(struct_7 *p, struct_2 *a1)
{
    struct_2 *ptr;  // x20
    unsigned long long flag;  // x2
    struct_0 *ptr3;  // x8
    struct_2 *v3;  // x0
    unsigned long long v4;  // x1
    struct_7 *addr;  // x21
    struct_6 *ptr4;  // x0
    struct_2 *v7;  // x1
    unsigned long long v8;  // x0

    ptr = a1;
    if (!(g_1fab253 & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab253 = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    flag = 0;
    if (!((char)Object__op_Inequality(ptr, 0, 0) & 1))
    {
LABEL_10501fc:
        addr = &p->field_58;
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        if (((char)Object__op_Inequality(p->field_58, ptr, 0) & 1))
        {
            if (!g_1ef0c58->field_e0)
                sub_f7da5c(g_1ef0c58);
            if (((char)Object__op_Inequality(*((long long *)&addr->padding_0[0]), 0, 0) & 1))
            {
                if (*((long long *)&addr->padding_0[0]))
                {
                    InputRig__RemoveControl(*((long long *)&addr->padding_0[0]), p);
                    goto LABEL_1050264;
                }
            }
            else
            {
LABEL_1050264:
                *((struct_2 **)&addr->padding_0[0]) = ptr;
                sub_f7d8d0(addr, ptr);
                if (!g_1ef0c58->field_e0)
                    sub_f7da5c(g_1ef0c58);
                if (!(Object__op_Inequality(*((long long *)&addr->padding_0[0]), 0, 0) & 1))
                    goto LABEL_10502b0;
                if (*((long long *)&addr->padding_0[0]))
                {
                    InputRig__AddControl(*((long long *)&addr->padding_0[0]), p);
                    goto LABEL_10502b0;
                }
            }
        }
        else
        {
LABEL_10502b0:
            ptr4 = p->field_48;
            if (ptr4)
            {
                v7 = p->field_58;
                ptr4->field_20 = v7;
                sub_f7d8d0((struct struct_6 *)&ptr4->field_20, v7);
                v8 = TouchControl__SyncDisablingConditions(p, 1);
                return TouchControl__SyncDisablingConditions(p, 1);
            }
        }
    }
    else if (ptr)
    {
        if (ptr->field_21)
        {
            ptr = NULL;
            goto LABEL_10501fc;
        }
        else if (!ptr->field_20)
        {
            ptr3 = ptr->field_0;
            ptr->field_20 = 1;
            v3 = ptr;
            v4 = ptr3->field_180;
            ptr3->field_178();
        }
    }
    sub_f7db74();
}
```

## `TouchControl.SetTouchControlPanel` — RVA `0xc50318`

- Decompiled symbol: `TouchControl_SetTouchControlPanel`
- Metadata signature: `public void SetTouchControlPanel(TouchControlPanel panel) { }`
- Native interval: `352` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    struct struct_0 *field_0;
    char padding_8[24];
    char field_20;
    char field_21;
} struct_2;

typedef struct struct_6 {
    char padding_0[104];
    struct struct_5 *field_68;
} struct_6;

typedef struct struct_5 {
    struct struct_3 *field_0;
    char padding_8[24];
    char field_20;
    char field_21;
} struct_5;

typedef struct struct_0 {
    char padding_0[376];
    struct struct_1 *field_178;
    unsigned long long field_180;
} struct_0;

typedef struct struct_3 {
    char padding_0[376];
    struct struct_4 *field_178;
    unsigned long long field_180;
} struct_3;

typedef struct struct_1 {
    unsigned long long field_0;
} struct_1;

typedef struct struct_4 {
    unsigned long long field_0;
} struct_4;

typedef struct struct_7 {
    char padding_0[224];
    unsigned int field_e0;
} struct_7;

extern struct_7 *g_1ef0c58;
extern char g_1fab254;
extern char g_20;

long long TouchControl_SetTouchControlPanel(struct_6 *a0, struct_2 *a1)
{
    struct_2 *p;  // x21
    struct_6 *ptr;  // x20
    long long v2;  // x0
    struct_5 *v3;  // x0
    unsigned long long flag;  // x2
    struct_0 *addr;  // x8
    struct_2 *v6;  // x0
    unsigned long long v7;  // x1
    long long v8;  // x0
    unsigned long long v9;  // x0

    p = a1;
    if (!(g_1fab254 & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab254 = 1;
    }
    ptr = &a0->field_68;
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v2 = Object__op_Equality(a0->field_68, p, 0);
    if (((char)v2 & 1))
        return v2;
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (((char)Object__op_Inequality(*((long long *)&ptr->padding_0[0]), 0, 0) & 1))
    {
        v3 = *((long long *)&ptr->padding_0[0]);
        if (v3)
        {
            TouchControlPanel__RemoveControl();
            goto LABEL_10503b8;
        }
    }
    else
    {
LABEL_10503b8:
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        flag = 0;
        v3 = Object__op_Inequality(p, 0, 0);
        if (!((char)v3 & 1))
        {
LABEL_1050410:
            *((struct_2 **)&ptr->padding_0[0]) = p;
            sub_f7d8d0(ptr, p);
            if (!g_1ef0c58->field_e0)
                sub_f7da5c(g_1ef0c58);
            v8 = Object__op_Inequality(*((long long *)&ptr->padding_0[0]), 0, 0);
            if (!((char)v8 & 1))
                return v8;
            v3 = *((long long *)&ptr->padding_0[0]);
            if (v3)
            {
                v9 = TouchControlPanel__AddControl(v3, a0);
                return TouchControlPanel__AddControl(v3, a0);
            }
        }
        else if (p)
        {
            if (p->field_21)
            {
                p = NULL;
                goto LABEL_1050410;
            }
            else if (!p->field_20)
            {
                addr = p->field_0;
                p->field_20 = 1;
                v6 = p;
                v7 = addr->field_180;
                addr->field_178();
            }
        }
    }
    sub_f7db74(v3);
}
```

## `TouchControl.InvalidateHierarchy` — RVA `0xc5060c`

- Decompiled symbol: `TouchControl_InvalidateHierarchy`
- Metadata signature: `public virtual void InvalidateHierarchy() { }`
- Native interval: `808` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern long long g_1efcf40;
extern long long g_1efcfe0;
extern long long g_1efd0c0;
extern char g_1fab255;

long long TouchControl_InvalidateHierarchy(long long *ptr)
{
    long long v2;  // x0
    long long v3;  // x22
    unsigned long v10;  // x21
    unsigned long v11;  // x20
    long long v12[14];  // x23
    long long v13;  // x0
    long long v14;  // x0
    unsigned long v4;  // x26
    unsigned long v5;  // x25
    long long v6;  // x24
    unsigned long v7;  // 4112
    unsigned long v8;  // 4112
    unsigned long v9;  // 4112
    char *v0;  // [bp-0x60]
    char v1;  // [bp+0x0]

    v0 = &v1;
    if (!(g_1fab255 & 1))
    {
        sub_f7d92c(&g_1efcf40);
        sub_f7d92c(&g_1efcfe0);
        sub_f7d92c(&g_1efd0c0);
        sub_f7d92c(&g_1ef0c58);
        g_1fab255 = 1;
    }
    v2 = Component__get_transform(ptr, 0);
    if (v2)
    {
        v3 = 0;
        v11 = 0;
        v10 = 0;
        while (true)
        {
            v2 = Transform__get_parent(v2, 0);
            if (!g_1ef0c58->field_e0)
                sub_f7da5c(g_1ef0c58);
            if (!((char)Object__op_Inequality(v2, 0, 0) & 1))
                break;
            if (!v2)
                sub_f7db74();
            v4 = sub_1231bc8(v2, g_1efd0c0);
            v5 = sub_1231bc8(v2, g_1efcfe0);
            v6 = sub_1231bc8(v2, g_1efcf40);
            if (!g_1ef0c58->field_e0)
                sub_f7da5c(g_1ef0c58);
            if (((char)Object__op_Equality(v11, 0, 0) & 1))
            {
                if (!g_1ef0c58->field_e0)
                    sub_f7da5c(g_1ef0c58);
                v7 = arm64g_calculate_condition(25, (unsigned long long)((int)Object__op_Inequality(v4, 0, 0) & 1), 0, 0);
                if ((char)v7)
                    v11 = v4;
            }
            if (!g_1ef0c58->field_e0)
                sub_f7da5c(g_1ef0c58);
            if (((char)Object__op_Equality(v10, 0, 0) & 1))
            {
                if (!g_1ef0c58->field_e0)
                    sub_f7da5c(g_1ef0c58);
                v8 = arm64g_calculate_condition(25, (unsigned long long)((int)Object__op_Inequality(v5, 0, 0) & 1), 0, 0);
                if ((char)v8)
                    v10 = v5;
            }
            if (!g_1ef0c58->field_e0)
                sub_f7da5c(g_1ef0c58);
            if (((char)Object__op_Equality(v3, 0, 0) & 1))
            {
                if (!g_1ef0c58->field_e0)
                    sub_f7da5c(g_1ef0c58);
                v9 = arm64g_calculate_condition(25, (unsigned long long)((int)Object__op_Inequality(v6, 0, 0) & 1), 0, 0);
                if ((char)v9)
                    v3 = v6;
            }
            if (!g_1ef0c58->field_e0)
                sub_f7da5c(g_1ef0c58);
            if (!(Object__op_Inequality(v10, 0, 0) & 1))
                continue;
            if (!g_1ef0c58->field_e0)
                sub_f7da5c(g_1ef0c58);
            if (!(Object__op_Inequality(v11, 0, 0) & 1))
                continue;
            if (!g_1ef0c58->field_e0)
                sub_f7da5c(g_1ef0c58);
            if (((char)Object__op_Inequality(v3, 0, 0) & 1))
                break;
        }
        ptr[12] = v3;
        v12 = ptr + 12;
        sub_f7d8d0(v12, v3);
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        if (((char)Object__op_Inequality(v12[1], v10, 0) & 1))
            TouchControl__SetRig(ptr, v10);
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        v13 = Object__op_Inequality(ptr[13], v11, 0);
        if (!((char)v13 & 1))
            return v13;
        v14 = TouchControl__SetTouchControlPanel(ptr, v11);
        return TouchControl__SetTouchControlPanel(ptr, v11);
    }
    sub_f7db74();
}
```

## `TouchControl.GetWorldPos` — RVA `0xc50934`

- Decompiled symbol: `TouchControl_GetWorldPos`
- Metadata signature: `public Vector3 GetWorldPos() { }`
- Native interval: `32` bytes
- Result: `pseudocode`

```c
void TouchControl_GetWorldPos(void)
{
    unsigned long long v1;  // x30
    unsigned long long v0;  // [bp-0x10]

    v0 = v1;
    if (Component__get_transform())
    {
        Transform__get_position();
        return;
    }
    sub_f7db74();
}
```

## `TouchControl.SetWorldPos` — RVA `0xc50954`

- Decompiled symbol: `TouchControl_SetWorldPos`
- Metadata signature: `public virtual void SetWorldPos(Vector2 pos2D) { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
void TouchControl_SetWorldPos(void)
{
    unsigned long long v0;  // x0

    v0 = TouchControl__SetWorldPosRaw();
    return;
}
```

## `TouchControl.SetWorldPosRaw` — RVA `0xc50958`

- Decompiled symbol: `TouchControl_SetWorldPosRaw`
- Metadata signature: `protected void SetWorldPosRaw(Vector2 pos2D) { }`
- Native interval: `72` bytes
- Result: `pseudocode`

```c
void TouchControl_SetWorldPosRaw(void)
{
    unsigned long long v4;  // d9
    unsigned long long v5;  // d8
    unsigned long long v6;  // x30
    unsigned long long v7;  // x19
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x18]
    unsigned long long v2;  // [bp-0x10]
    unsigned long long v3;  // [bp-0x8]

    v0 = v4;
    v1 = v5;
    v2 = v6;
    v3 = v7;
    if (Component__get_transform())
    {
        Transform__get_position();
        Transform__set_position();
        return;
    }
    sub_f7db74();
}
```

## `TouchControl.GetLocalRect` — RVA `0xc509a0`

- Decompiled symbol: `TouchControl_GetLocalRect`
- Metadata signature: `public virtual Rect GetLocalRect() { }`
- Native interval: `260` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[56];
    unsigned int field_38;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern unsigned long long g_1ef1170;
extern char g_1fab256;

long long TouchControl_GetLocalRect(struct_1 *a0)
{
    long long v0;  // x0
    long long v1;  // x20
    long long v2;  // x0
    long long v3;  // x0
    unsigned int v4;  // s2
    unsigned int v5;  // s3
    unsigned long v6;  // 4155

    if (!(g_1fab256 & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c(&g_1ef1170);
        g_1fab256 = 1;
    }
    v0 = Component__get_transform(a0, 0);
    if (v0)
    {
        if (*((long long *)v0) == g_1ef1170)
            v1 = v0;
        else
            v1 = 0;
    }
    else
    {
        v1 = 0;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v2 = Object__op_Equality(v1, 0, 0);
    if (((char)v2 & 1))
        return v2;
    if (v1)
    {
        v3 = RectTransform__get_rect(v1, 0);
        if (1 < a0->field_38 - 1)
            return v3;
        v6 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(v4, v5)) >> 5 & 3 | (unsigned long long)(CmpF(v4, v5) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v4, v5)) >> 5 & 3 | (unsigned long long)(CmpF(v4, v5) & 1)) & ((unsigned long long)(char)(CmpF(v4, v5)) >> 5 & 3 | (unsigned long long)(CmpF(v4, v5) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        return v3;
    }
    sub_f7db74();
}
```

## `TouchControl.ScreenToWorldPos` — RVA `0xc50aa4`

- Decompiled symbol: `TouchControl_ScreenToWorldPos`
- Metadata signature: `protected Vector3 ScreenToWorldPos(Vector2 sp, Camera cam) { }`
- Native interval: `844` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: Decompiler produced no C-like text

```c
// 0x1050aa4: sub sp, sp, #0xa0
// 0x1050aa8: stp d15, d14, [sp, #0x30]
// 0x1050aac: stp d13, d12, [sp, #0x40]
// 0x1050ab0: stp d11, d10, [sp, #0x50]
// 0x1050ab4: stp d9, d8, [sp, #0x60]
// 0x1050ab8: str x30, [sp, #0x70]
// 0x1050abc: stp x22, x21, [sp, #0x80]
// 0x1050ac0: stp x20, x19, [sp, #0x90]
// 0x1050ac4: adrp x22, #0x1fab000
// 0x1050ac8: adrp x21, #0x1e8c000
// 0x1050acc: ldrb w8, [x22, #0x257]
// 0x1050ad0: ldr x21, [x21, #0xd8]
// 0x1050ad4: mov x19, x1
// 0x1050ad8: mov v9.16b, v1.16b
// 0x1050adc: mov v8.16b, v0.16b
// 0x1050ae0: mov x20, x0
// 0x1050ae4: tbnz w8, #0, #0x1050afc
// 0x1050ae8: adrp x0, #0x1e8c000
// 0x1050aec: ldr x0, [x0, #0xd8]
// 0x1050af0: bl #0xf7d92c
// 0x1050af4: mov w8, #1
// 0x1050af8: strb w8, [x22, #0x257]
// 0x1050afc: mov x0, x20
// 0x1050b00: mov x1, xzr
// 0x1050b04: bl #0x1b92154
// 0x1050b08: ldr x8, [x21]
// 0x1050b0c: mov x20, x0
// 0x1050b10: ldr w9, [x8, #0xe0]
// 0x1050b14: cbnz w9, #0x1050b20
// 0x1050b18: mov x0, x8
// 0x1050b1c: bl #0xf7da5c
// 0x1050b20: mov x0, x19
// 0x1050b24: mov x1, xzr
// 0x1050b28: mov x2, xzr
// 0x1050b2c: bl #0x1b94ac8
// 0x1050b30: cbz x20, #0x1050dec
// 0x1050b34: tbz w0, #0, #0x1050db4
// 0x1050b38: mov x0, x20
// 0x1050b3c: mov x1, xzr
// 0x1050b40: bl #0x1b9d9b8
// 0x1050b44: cbz x19, #0x1050dec
// 0x1050b48: mov x0, x19
// 0x1050b4c: mov x1, xzr
// 0x1050b50: mov v11.16b, v0.16b
// 0x1050b54: mov v12.16b, v1.16b
// 0x1050b58: mov v10.16b, v2.16b
// 0x1050b5c: bl #0x1b92154
// 0x1050b60: cbz x0, #0x1050dec
// 0x1050b64: mov x1, xzr
// 0x1050b68: bl #0x1b9d9b8
// 0x1050b6c: fmul s0, s11, s0
// 0x1050b70: fmul s1, s12, s1
// 0x1050b74: adrp x8, #0x832000
// 0x1050b78: fadd s0, s0, s1
// 0x1050b7c: ldr s1, [x8, #0x3c0]
// 0x1050b80: fmul s2, s10, s2
// 0x1050b84: fadd s0, s2, s0
// 0x1050b88: fabs s0, s0
// 0x1050b8c: fcmp s0, s1
// 0x1050b90: b.ge #0x1050d94
// 0x1050b94: add x8, sp, #0x18
// 0x1050b98: fmov s2, wzr
// 0x1050b9c: mov x0, x19
// 0x1050ba0: mov v0.16b, v8.16b
// 0x1050ba4: mov v1.16b, v9.16b
// 0x1050ba8: mov x1, xzr
// 0x1050bac: bl #0x1b6f898
// 0x1050bb0: ldr s3, [sp, #0x18]
// 0x1050bb4: ldr s0, [sp, #0x1c]
// 0x1050bb8: mov x0, x20
// 0x1050bbc: mov x1, xzr
// 0x1050bc0: stp s3, s0, [sp, #0xc]
// 0x1050bc4: ldr s0, [sp, #0x20]
// 0x1050bc8: ldr s3, [sp, #0x24]
// 0x1050bcc: str s0, [sp, #0x14]
// 0x1050bd0: ldp s0, s12, [sp, #0x28]
// 0x1050bd4: stp s0, s3, [sp, #0x78]
// 0x1050bd8: bl #0x1b9d9b8
// 0x1050bdc: mov x0, x20
// 0x1050be0: mov x1, xzr
// 0x1050be4: mov v13.16b, v0.16b
// 0x1050be8: mov v14.16b, v1.16b
// 0x1050bec: mov v15.16b, v2.16b
// 0x1050bf0: bl #0x1b9d508
// 0x1050bf4: adrp x21, #0x1fab000
// 0x1050bf8: ldrb w8, [x21, #0x2c8]
// 0x1050bfc: mov v11.16b, v2.16b
// 0x1050c00: stp s1, s0, [sp, #4]
// 0x1050c04: cbnz w8, #0x1050c1c
// 0x1050c08: adrp x0, #0x1e8c000
// 0x1050c0c: ldr x0, [x0, #0xa60]
// 0x1050c10: bl #0xf7d92c
// 0x1050c14: mov w8, #1
// 0x1050c18: strb w8, [x21, #0x2c8]
// 0x1050c1c: adrp x8, #0x1e8c000
// 0x1050c20: ldr x8, [x8, #0xa60]
// 0x1050c24: ldr x0, [x8]
// 0x1050c28: ldr w8, [x0, #0xe0]
// 0x1050c2c: cbnz w8, #0x1050c34
// 0x1050c30: bl #0xf7da5c
// 0x1050c34: fmul s0, s13, s13
// 0x1050c38: fmul s1, s14, s14
// 0x1050c3c: adrp x8, #0x832000
// 0x1050c40: fadd s0, s0, s1
// 0x1050c44: ldr s1, [x8, #0x41c]
// 0x1050c48: fmul s2, s15, s15
// 0x1050c4c: fadd s0, s2, s0
// 0x1050c50: fsqrt s0, s0
// 0x1050c54: fcmp s0, s1
// 0x1050c58: b.le #0x1050c6c
// 0x1050c5c: fdiv s10, s13, s0
// 0x1050c60: fdiv s14, s14, s0
// 0x1050c64: fdiv s13, s15, s0
// 0x1050c68: b #0x1050ca4
// 0x1050c6c: adrp x21, #0x1fab000
// 0x1050c70: ldrb w8, [x21, #0x2c9]
// 0x1050c74: cbnz w8, #0x1050c8c
// 0x1050c78: adrp x0, #0x1e8c000
// 0x1050c7c: ldr x0, [x0, #0x1e8]
// 0x1050c80: bl #0xf7d92c
// 0x1050c84: mov w8, #1
// 0x1050c88: strb w8, [x21, #0x2c9]
// 0x1050c8c: adrp x8, #0x1e8c000
// 0x1050c90: ldr x8, [x8, #0x1e8]
// 0x1050c94: ldr x8, [x8]
// 0x1050c98: ldr x8, [x8, #0xb8]
// 0x1050c9c: ldp s10, s14, [x8]
// 0x1050ca0: ldr s13, [x8, #8]
// 0x1050ca4: ldp s1, s0, [sp, #0x78]
// 0x1050ca8: adrp x21, #0x1fab000
// 0x1050cac: ldrb w8, [x21, #0x2ca]
// 0x1050cb0: fmul s0, s0, s10
// 0x1050cb4: fmul s1, s1, s14
// 0x1050cb8: fadd s0, s0, s1
// 0x1050cbc: fmul s1, s12, s13
// 0x1050cc0: fadd s15, s1, s0
// 0x1050cc4: cbnz w8, #0x1050cdc
// 0x1050cc8: adrp x0, #0x1e8c000
// 0x1050ccc: ldr x0, [x0, #0xd80]
// 0x1050cd0: bl #0xf7d92c
// 0x1050cd4: mov w8, #1
// 0x1050cd8: strb w8, [x21, #0x2ca]
// 0x1050cdc: adrp x8, #0x1e8c000
// 0x1050ce0: ldr x8, [x8, #0xd80]
// 0x1050ce4: adrp x9, #0x832000
// 0x1050ce8: ldr s0, [x9, #0x474]
// 0x1050cec: fabs s1, s15
// 0x1050cf0: ldr x8, [x8]
// 0x1050cf4: fmov s2, wzr
// 0x1050cf8: fmaxnm s1, s1, s2
// 0x1050cfc: fmul s0, s1, s0
// 0x1050d00: ldr x8, [x8, #0xb8]
// 0x1050d04: fmov s1, #8.00000000
// 0x1050d08: ldr s3, [x8]
// 0x1050d0c: fmul s1, s3, s1
// 0x1050d10: fcmp s0, s1
// 0x1050d14: fcsel s0, s0, s1, gt
// 0x1050d18: fabd s1, s2, s15
// 0x1050d1c: fcmp s1, s0
// 0x1050d20: b.mi #0x1050d94
// 0x1050d24: ldp s1, s0, [sp, #4]
// 0x1050d28: ldp s2, s3, [sp, #0xc]
// 0x1050d2c: ldr s5, [sp, #0x14]
// 0x1050d30: fmul s4, s11, s13
// 0x1050d34: fmul s0, s0, s10
// 0x1050d38: fmul s1, s1, s14
// 0x1050d3c: fmul s2, s2, s10
// 0x1050d40: fmul s3, s3, s14
// 0x1050d44: fmul s5, s5, s13
// 0x1050d48: fadd s0, s0, s1
// 0x1050d4c: fadd s1, s2, s3
// 0x1050d50: fadd s0, s4, s0
// 0x1050d54: fadd s1, s5, s1
// 0x1050d58: fsub s0, s0, s1
// 0x1050d5c: fdiv s0, s0, s15
// 0x1050d60: fcmp s0, #0.0
// 0x1050d64: b.le #0x1050d94
// 0x1050d68: ldp s2, s1, [sp, #0x78]
// 0x1050d6c: ldr s3, [sp, #0xc]
// 0x1050d70: fmul s1, s1, s0
// 0x1050d74: fadd s8, s3, s1
// 0x1050d78: ldr s1, [sp, #0x10]
// 0x1050d7c: fmul s2, s2, s0
// 0x1050d80: fmul s0, s12, s0
// 0x1050d84: fadd s9, s1, s2
// 0x1050d88: ldr s1, [sp, #0x14]
// 0x1050d8c: fadd s2, s1, s0
// 0x1050d90: b #0x1050dc0
// 0x1050d94: fmov s2, wzr
// 0x1050d98: mov x0, x19
// 0x1050d9c: mov v0.16b, v8.16b
// 0x1050da0: mov v1.16b, v9.16b
// 0x1050da4: mov x1, xzr
// 0x1050da8: bl #0x1b6f6c8
// 0x1050dac: mov v8.16b, v0.16b
// 0x1050db0: mov v9.16b, v1.16b
// 0x1050db4: mov x0, x20
// 0x1050db8: mov x1, xzr
// 0x1050dbc: bl #0x1b9d508
// 0x1050dc0: mov v0.16b, v8.16b
// 0x1050dc4: mov v1.16b, v9.16b
// 0x1050dc8: ldp x20, x19, [sp, #0x90]
// 0x1050dcc: ldp x22, x21, [sp, #0x80]
// 0x1050dd0: ldr x30, [sp, #0x70]
// 0x1050dd4: ldp d9, d8, [sp, #0x60]
// 0x1050dd8: ldp d11, d10, [sp, #0x50]
// 0x1050ddc: ldp d13, d12, [sp, #0x40]
// 0x1050de0: ldp d15, d14, [sp, #0x30]
// 0x1050de4: add sp, sp, #0xa0
// 0x1050de8: ret
// 0x1050dec: bl #0xf7db74
```

## `TouchControl.WorldToLocalPos` — RVA `0xc50df0`

- Decompiled symbol: `TouchControl_WorldToLocalPos`
- Metadata signature: `protected Vector2 WorldToLocalPos(Vector3 wp, Vector2 worldOffset) { }`
- Native interval: `148` bytes
- Result: `pseudocode`

```c
long long TouchControl_WorldToLocalPos(void)
{
    unsigned long long v8;  // x0
    char v0;  // [bp-0xb0]
    uint128_t v1;  // [bp-0xa0]
    uint128_t v2;  // [bp-0x90]
    uint128_t v3;  // [bp-0x80]
    char flag;  // [bp-0x70], Other Possible Types: uint128_t
    uint128_t v5;  // [bp-0x60]
    uint128_t v6;  // [bp-0x50]
    uint128_t v7;  // [bp-0x40]

    v6 = 0;
    v7 = 0;
    flag = 0;
    v5 = 0;
    if (Component__get_transform())
    {
        Transform__get_worldToLocalMatrix();
        memcpy(&flag, &v0, 16);
        v5 = v1;
        v6 = v2;
        v7 = v3;
        v8 = Matrix4x4__MultiplyPoint3x4(&flag, 0);
        return Matrix4x4__MultiplyPoint3x4(&flag, 0);
    }
    sub_f7db74();
}
```

## `TouchControl.WorldToLocalPos` — RVA `0xc50e84`

- Decompiled symbol: `TouchControl_WorldToLocalPos`
- Metadata signature: `protected Vector2 WorldToLocalPos(Vector3 wp) { }`
- Native interval: `120` bytes
- Result: `pseudocode`

```c
extern long long g_1ef22b8;
extern char g_1fab1e0;

long long TouchControl_WorldToLocalPos(unsigned long a0)
{
    long long v0;  // x0

    if (!g_1fab1e0)
    {
        sub_f7d92c(&g_1ef22b8);
        g_1fab1e0 = 1;
    }
    v0 = TouchControl__WorldToLocalPos();
    return TouchControl__WorldToLocalPos();
}
```

## `TouchControl.ScreenToLocalPos` — RVA `0xc50efc`

- Decompiled symbol: `TouchControl_ScreenToLocalPos`
- Metadata signature: `protected Vector2 ScreenToLocalPos(Vector2 sp, Camera cam, Vector2 worldOffset) { }`
- Native interval: `48` bytes
- Result: `pseudocode`

```c
long long TouchControl_ScreenToLocalPos(long long a0, long long a1)
{
    long long v0;  // x0

    TouchControl__ScreenToWorldPos(a0, a1);
    v0 = TouchControl__WorldToLocalPos();
    return TouchControl__WorldToLocalPos();
}
```

## `TouchControl.ScreenToLocalPos` — RVA `0xc50f2c`

- Decompiled symbol: `TouchControl_ScreenToLocalPos`
- Metadata signature: `protected Vector2 ScreenToLocalPos(Vector2 sp, Camera cam) { }`
- Native interval: `112` bytes
- Result: `pseudocode`

```c
extern long long g_1ef22b8;
extern char g_1fab1e0;

long long TouchControl_ScreenToLocalPos(long long a0, long long a1)
{
    long long v0;  // x0

    if (!g_1fab1e0)
    {
        sub_f7d92c(&g_1ef22b8);
        g_1fab1e0 = 1;
    }
    v0 = TouchControl__ScreenToLocalPos(a0, a1);
    return TouchControl__ScreenToLocalPos(a0, a1);
}
```

## `TouchControl.ScreenToNormalizedPos` — RVA `0xc50f9c`

- Decompiled symbol: `TouchControl_ScreenToNormalizedPos`
- Metadata signature: `protected Vector2 ScreenToNormalizedPos(Vector2 sp, Camera cam, Vector2 worldOffset) { }`
- Native interval: `116` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[904];
    struct struct_1 *field_388;
    unsigned long long field_390;
} struct_0;

typedef struct struct_1 {
    unsigned long long field_0;
} struct_1;

void TouchControl_ScreenToNormalizedPos(struct_0 **a0, long long a1)
{
    unsigned long long v4;  // d9
    unsigned long long v5;  // d8
    unsigned long long v6;  // x30
    unsigned long long v7;  // x19
    struct_0 **v8;  // x0
    unsigned long v9;  // x1
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x18]
    unsigned long long v2;  // [bp-0x10]
    unsigned long long v3;  // [bp-0x8]

    v0 = v4;
    v1 = v5;
    v2 = v6;
    v3 = v7;
    TouchControl__ScreenToWorldPos(a0, a1);
    TouchControl__WorldToLocalPos();
    v8 = a0;
    v9 = *(a0)->field_390;
    *(a0)->field_388();
}
```

## `TouchControl.LocalToNormalizedPos` — RVA `0xc51010`

- Decompiled symbol: `TouchControl_LocalToNormalizedPos`
- Metadata signature: `protected Vector2 LocalToNormalizedPos(Vector2 lp) { }`
- Native interval: `80` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[904];
    struct struct_1 *field_388;
    unsigned long long field_390;
} struct_0;

typedef struct struct_1 {
    unsigned long long field_0;
} struct_1;

void TouchControl_LocalToNormalizedPos(struct_0 **a0)
{
    unsigned long long v3;  // d9
    unsigned long long v4;  // d8
    unsigned long long v5;  // x30
    unsigned long long v6;  // x1
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x18]
    unsigned long long v2;  // [bp-0x10]

    v0 = v3;
    v1 = v4;
    v2 = v5;
    v6 = *(a0)->field_390;
    *(a0)->field_388();
}
```

## `TouchControl.ScreenToNormalizedPos` — RVA `0xc51060`

- Decompiled symbol: `TouchControl_ScreenToNormalizedPos`
- Metadata signature: `protected Vector2 ScreenToNormalizedPos(Vector2 sp, Camera cam) { }`
- Native interval: `112` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[904];
    struct struct_1 *field_388;
    unsigned long long field_390;
} struct_0;

typedef struct struct_1 {
    unsigned long long field_0;
} struct_1;

extern long long g_1ef22b8;
extern char g_1fab1e0;

void TouchControl_ScreenToNormalizedPos(struct_0 **a0, long long a1)
{
    if (!g_1fab1e0)
    {
        sub_f7d92c(&g_1ef22b8);
        g_1fab1e0 = 1;
    }
    TouchControl__ScreenToNormalizedPos(a0, a1); /* do not return */
}
```

## `TouchControl.WorldToNormalizedPos` — RVA `0xc510d0`

- Decompiled symbol: `TouchControl_WorldToNormalizedPos`
- Metadata signature: `protected Vector2 WorldToNormalizedPos(Vector2 wp, Vector2 worldOffset) { }`
- Native interval: `104` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[904];
    struct struct_1 *field_388;
    unsigned long long field_390;
} struct_0;

typedef struct struct_1 {
    unsigned long long field_0;
} struct_1;

void TouchControl_WorldToNormalizedPos(struct_0 **a0)
{
    unsigned long long v4;  // d9
    unsigned long long v5;  // d8
    unsigned long long v6;  // x30
    unsigned long long v7;  // x19
    struct_0 **v8;  // x0
    unsigned long v9;  // x1
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x18]
    unsigned long long v2;  // [bp-0x10]
    unsigned long long v3;  // [bp-0x8]

    v0 = v4;
    v1 = v5;
    v2 = v6;
    v3 = v7;
    TouchControl__WorldToLocalPos();
    v8 = a0;
    v9 = *(a0)->field_390;
    *(a0)->field_388();
}
```

## `TouchControl.WorldToNormalizedPos` — RVA `0xc51138`

- Decompiled symbol: `TouchControl_WorldToNormalizedPos`
- Metadata signature: `protected Vector2 WorldToNormalizedPos(Vector2 wp) { }`
- Native interval: `104` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[904];
    struct struct_1 *field_388;
    unsigned long long field_390;
} struct_0;

typedef struct struct_1 {
    unsigned long long field_0;
} struct_1;

extern long long g_1ef22b8;
extern char g_1fab1e0;

void TouchControl_WorldToNormalizedPos(struct_0 **a0)
{
    if (!g_1fab1e0)
    {
        sub_f7d92c(&g_1ef22b8);
        g_1fab1e0 = 1;
    }
    TouchControl__WorldToNormalizedPos(a0); /* do not return */
}
```

## `TouchControl.NormalizedToLocalPos` — RVA `0xc511a0`

- Decompiled symbol: `TouchControl_NormalizedToLocalPos`
- Metadata signature: `protected Vector2 NormalizedToLocalPos(Vector2 np) { }`
- Native interval: `80` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[904];
    struct struct_1 *field_388;
    unsigned long long field_390;
} struct_0;

typedef struct struct_1 {
    unsigned long long field_0;
} struct_1;

void TouchControl_NormalizedToLocalPos(struct_0 **a0)
{
    unsigned long long v3;  // d9
    unsigned long long v4;  // d8
    unsigned long long v5;  // x30
    unsigned long long v6;  // x1
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x18]
    unsigned long long v2;  // [bp-0x10]

    v0 = v3;
    v1 = v4;
    v2 = v5;
    v6 = *(a0)->field_390;
    *(a0)->field_388();
}
```

## `TouchControl.NormalizedToLocalOffset` — RVA `0xc511f0`

- Decompiled symbol: `TouchControl_NormalizedToLocalOffset`
- Metadata signature: `protected Vector2 NormalizedToLocalOffset(Vector2 np) { }`
- Native interval: `64` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[904];
    struct struct_1 *field_388;
    unsigned long long field_390;
} struct_0;

typedef struct struct_1 {
    unsigned long long field_0;
} struct_1;

void TouchControl_NormalizedToLocalOffset(struct_0 **a0)
{
    unsigned long long v3;  // d9
    unsigned long long v4;  // d8
    unsigned long long v5;  // x30
    unsigned long long v6;  // x1
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x18]
    unsigned long long v2;  // [bp-0x10]

    v0 = v3;
    v1 = v4;
    v2 = v5;
    v6 = *(a0)->field_390;
    *(a0)->field_388();
}
```

## `TouchControl.NormalizedToWorldPos` — RVA `0xc51230`

- Decompiled symbol: `TouchControl_NormalizedToWorldPos`
- Metadata signature: `protected Vector3 NormalizedToWorldPos(Vector2 np) { }`
- Native interval: `208` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[904];
    struct struct_1 *field_388;
    unsigned long long field_390;
} struct_0;

typedef struct struct_1 {
    unsigned long long field_0;
} struct_1;

void TouchControl_NormalizedToWorldPos(struct_0 **a0)
{
    unsigned long long v12;  // d13
    unsigned long long v13;  // d12
    unsigned long long v14;  // d11
    unsigned long long v15;  // d10
    unsigned long long v16;  // d9
    unsigned long long v17;  // d8
    unsigned long long v18;  // x30
    unsigned long long v19;  // x19
    unsigned long long v20;  // x1
    uint128_t flag2;  // [bp-0x80]
    uint128_t flag3;  // [bp-0x70]
    uint128_t flag;  // [bp-0x60]
    uint128_t choice;  // [bp-0x50]
    unsigned long long v4;  // [bp-0x40]
    unsigned long long v5;  // [bp-0x38]
    unsigned long long v6;  // [bp-0x30]
    unsigned long long v7;  // [bp-0x28]
    unsigned long long v8;  // [bp-0x20]
    unsigned long long v9;  // [bp-0x18]
    unsigned long long v10;  // [bp-0x10]
    unsigned long long v11;  // [bp-0x8]

    v4 = v12;
    v5 = v13;
    v6 = v14;
    v7 = v15;
    v8 = v16;
    v9 = v17;
    v10 = v18;
    v11 = v19;
    flag = 0;
    choice = 0;
    flag2 = 0;
    flag3 = 0;
    v20 = *(a0)->field_390;
    *(a0)->field_388();
}
```

## `TouchControl.NormalizedToWorldOffset` — RVA `0xc51300`

- Decompiled symbol: `TouchControl_NormalizedToWorldOffset`
- Metadata signature: `protected Vector2 NormalizedToWorldOffset(Vector2 np) { }`
- Native interval: `176` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[904];
    struct struct_1 *field_388;
    unsigned long long field_390;
} struct_0;

typedef struct struct_1 {
    unsigned long long field_0;
} struct_1;

void TouchControl_NormalizedToWorldOffset(struct_0 **a0)
{
    unsigned long long v10;  // d11
    unsigned long long v11;  // d10
    unsigned long long v12;  // d9
    unsigned long long v13;  // d8
    unsigned long long v14;  // x30
    unsigned long long v15;  // x19
    unsigned long long v16;  // x1
    uint128_t flag2;  // [bp-0x70]
    uint128_t flag3;  // [bp-0x60]
    uint128_t flag;  // [bp-0x50]
    uint128_t choice;  // [bp-0x40]
    unsigned long long v4;  // [bp-0x30]
    unsigned long long v5;  // [bp-0x28]
    unsigned long long v6;  // [bp-0x20]
    unsigned long long v7;  // [bp-0x18]
    unsigned long long v8;  // [bp-0x10]
    unsigned long long v9;  // [bp-0x8]

    v4 = v10;
    v5 = v11;
    v6 = v12;
    v7 = v13;
    v8 = v14;
    v9 = v15;
    flag = 0;
    choice = 0;
    flag2 = 0;
    flag3 = 0;
    v16 = *(a0)->field_390;
    *(a0)->field_388();
}
```

## `TouchControl.WorldToScreenPos` — RVA `0xc513b0`

- Decompiled symbol: `TouchControl_WorldToScreenPos`
- Metadata signature: `protected Vector3 WorldToScreenPos(Vector3 wp, Camera cam) { }`
- Native interval: `184` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab258;

long long TouchControl_WorldToScreenPos(unsigned long a0, long long a1)
{
    long long v0;  // x0
    unsigned long long v1;  // x0

    if (!(g_1fab258 & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab258 = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v0 = Object__op_Inequality(a1, 0, 0);
    if (!((char)v0 & 1))
        return v0;
    if (a1)
    {
        v1 = Camera__WorldToScreenPoint(a1, 0);
        return Camera__WorldToScreenPoint(a1, 0);
    }
    sub_f7db74();
}
```

## `TouchControl.LocalToScreenPos` — RVA `0xc51468`

- Decompiled symbol: `TouchControl_LocalToScreenPos`
- Metadata signature: `protected Vector2 LocalToScreenPos(Vector2 lp, Camera cam) { }`
- Native interval: `288` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab259;

long long TouchControl_LocalToScreenPos(long long a0, long long a1)
{
    unsigned int v8;  // w0
    unsigned long long v9;  // x0
    unsigned long long v10;  // x0
    char v0;  // [bp-0xc0]
    uint128_t v1;  // [bp-0xb0]
    uint128_t v2;  // [bp-0xa0]
    uint128_t v3;  // [bp-0x90]
    uint128_t flag;  // [bp-0x80], Other Possible Types: char
    uint128_t v5;  // [bp-0x70]
    uint128_t v6;  // [bp-0x60]
    uint128_t v7;  // [bp-0x50]

    if (!(g_1fab259 & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab259 = 1;
    }
    v6 = 0;
    v7 = 0;
    flag = 0;
    v5 = 0;
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v8 = Object__op_Inequality(a1, 0, 0);
    if (Component__get_transform(a0, 0))
    {
        if (((char)v8 & 1))
        {
            Transform__get_localToWorldMatrix();
            memcpy(&flag, &v0, 16);
            v5 = v1;
            v6 = v2;
            v7 = v3;
            Matrix4x4__MultiplyPoint3x4(&flag, 0);
            if (a1)
            {
                v9 = Camera__WorldToScreenPoint(a1, 0);
                return Camera__WorldToScreenPoint(a1, 0);
            }
        }
        else
        {
            Transform__get_localToWorldMatrix();
            memcpy(&flag, &v0, 16);
            v5 = v1;
            v6 = v2;
            v7 = v3;
            v10 = Matrix4x4__MultiplyPoint3x4(&flag, 0);
            return Matrix4x4__MultiplyPoint3x4(&flag, 0);
        }
    }
    sub_f7db74();
}
```

## `TouchControl.ScreenToOrientedPos` — RVA `0xc51588`

- Decompiled symbol: `TouchControl_ScreenToOrientedPos`
- Metadata signature: `public Vector2 ScreenToOrientedPos(Vector2 sp, Camera cam) { }`
- Native interval: `124` bytes
- Result: `pseudocode`

```c
extern char g_1fab2cb;

void TouchControl_ScreenToOrientedPos(long long a0)
{
    unsigned long long v5;  // d9
    unsigned long long v6;  // d8
    unsigned long long v7;  // x30
    unsigned long long v8;  // x20
    unsigned long long v9;  // x19
    unsigned long long v0;  // [bp-0x30]
    unsigned long long v1;  // [bp-0x28]
    unsigned long long v2;  // [bp-0x20]
    unsigned long long v3;  // [bp-0x10]
    unsigned long long v4;  // [bp-0x8]

    v0 = v5;
    v1 = v6;
    v2 = v7;
    v3 = v8;
    v4 = v9;
    if (!g_1fab2cb)
    {
        sub_f7d92c("-M");
        g_1fab2cb = 1;
    }
    if (Component__get_transform(a0, 0))
    {
        Transform__get_rotation();
        Quaternion__Inverse(0);
        Quaternion__op_Multiply();
        return;
    }
    sub_f7db74();
}
```

## `TouchControl.GetWorldSpaceCenter` — RVA `0xc51604`

- Decompiled symbol: `TouchControl_GetWorldSpaceCenter`
- Metadata signature: `public Vector3 GetWorldSpaceCenter() { }`
- Native interval: `292` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[904];
    struct struct_1 *field_388;
    unsigned long long field_390;
} struct_0;

typedef struct struct_1 {
    unsigned long long field_0;
} struct_1;

void TouchControl_GetWorldSpaceCenter(struct_0 **a0)
{
    unsigned long long v13;  // d13
    unsigned long long v14;  // d12
    unsigned long long v15;  // d11
    unsigned long long v16;  // d10
    unsigned long long v17;  // d9
    unsigned long long v18;  // d8
    unsigned long long v19;  // x30
    unsigned long long v20;  // x20
    unsigned long long v21;  // x19
    unsigned long long v22;  // x1
    uint128_t flag2;  // [bp-0x90]
    uint128_t flag3;  // [bp-0x80]
    uint128_t flag;  // [bp-0x70]
    uint128_t choice;  // [bp-0x60]
    unsigned long long v4;  // [bp-0x50]
    unsigned long long v5;  // [bp-0x48]
    unsigned long long v6;  // [bp-0x40]
    unsigned long long v7;  // [bp-0x38]
    unsigned long long v8;  // [bp-0x30]
    unsigned long long v9;  // [bp-0x28]
    unsigned long long v10;  // [bp-0x20]
    unsigned long long v11;  // [bp-0x10]
    unsigned long long v12;  // [bp-0x8]

    v4 = v13;
    v5 = v14;
    v6 = v15;
    v7 = v16;
    v8 = v17;
    v9 = v18;
    v10 = v19;
    v11 = v20;
    v12 = v21;
    flag = 0;
    choice = 0;
    flag2 = 0;
    flag3 = 0;
    v22 = *(a0)->field_390;
    *(a0)->field_388();
}
```

## `TouchControl.GetWorldSpaceSize` — RVA `0xc51728`

- Decompiled symbol: `TouchControl_GetWorldSpaceSize`
- Metadata signature: `public Vector3 GetWorldSpaceSize() { }`
- Native interval: `48` bytes
- Result: `pseudocode`

```c
void TouchControl_GetWorldSpaceSize(void)
{
    unsigned long long v1;  // x30
    unsigned long long v0;  // [bp-0x10]

    v0 = v1;
    TouchControl__GetWorldSpaceAABB(); /* do not return */
}
```

## `TouchControl.GetWorldSpaceAABB` — RVA `0xc51758`

- Decompiled symbol: `TouchControl_GetWorldSpaceAABB`
- Metadata signature: `public Bounds GetWorldSpaceAABB() { }`
- Native interval: `256` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[904];
    struct struct_1 *field_388;
    unsigned long long field_390;
} struct_0;

typedef struct struct_1 {
    unsigned long long field_0;
} struct_1;

void TouchControl_GetWorldSpaceAABB(struct_0 **a0)
{
    unsigned long long v9;  // d11
    unsigned long long v10;  // d10
    unsigned long long v11;  // d9
    unsigned long long v12;  // d8
    unsigned long long v13;  // x30
    unsigned long long v14;  // x20
    unsigned long long v15;  // x19
    unsigned long long v16;  // x1
    unsigned long long v0;  // [bp-0x40]
    unsigned long long v1;  // [bp-0x38]
    unsigned long long v2;  // [bp-0x30]
    unsigned long long v3;  // [bp-0x28]
    char *v4;  // [bp-0x20]
    unsigned long long v5;  // [bp-0x18]
    unsigned long long v6;  // [bp-0x10]
    unsigned long long v7;  // [bp-0x8]
    char v8;  // [bp+0x0]

    v0 = v9;
    v1 = v10;
    v2 = v11;
    v3 = v12;
    v4 = &v8;
    v5 = v13;
    v6 = v14;
    v7 = v15;
    v16 = *(a0)->field_390;
    *(a0)->field_388();
}
```

## `TouchControl.GetWorldToNormalizedMatrix` — RVA `0xc51b9c`

- Decompiled symbol: `TouchControl_GetWorldToNormalizedMatrix`
- Metadata signature: `public Matrix4x4 GetWorldToNormalizedMatrix() { }`
- Native interval: `500` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[904];
    struct struct_1 *field_388;
    unsigned long long field_390;
} struct_0;

typedef struct struct_1 {
    unsigned long long field_0;
} struct_1;

void TouchControl_GetWorldToNormalizedMatrix(struct_0 **a0)
{
    unsigned long long v12;  // d13
    unsigned long long v13;  // d12
    unsigned long long v22;  // x1
    unsigned long long v14;  // d11
    unsigned long long v15;  // d10
    unsigned long long v16;  // d9
    unsigned long long v17;  // d8
    unsigned long long v18;  // x30
    unsigned long long v19;  // x21
    unsigned long long v20;  // x20
    unsigned long long v21;  // x19
    unsigned long long v0;  // [bp-0x60]
    unsigned long long v1;  // [bp-0x58]
    unsigned long long v2;  // [bp-0x50]
    unsigned long long v3;  // [bp-0x48]
    unsigned long long v4;  // [bp-0x40]
    unsigned long long v5;  // [bp-0x38]
    char *v6;  // [bp-0x30]
    unsigned long long v7;  // [bp-0x20]
    unsigned long long v8;  // [bp-0x18]
    unsigned long long v9;  // [bp-0x10]
    unsigned long long v10;  // [bp-0x8]
    char v11;  // [bp+0x0]

    v0 = v12;
    v1 = v13;
    v2 = v14;
    v3 = v15;
    v4 = v16;
    v5 = v17;
    v6 = &v11;
    v7 = v18;
    v8 = v19;
    v9 = v20;
    v10 = v21;
    v22 = *(a0)->field_390;
    *(a0)->field_388();
}
```

## `TouchControl.GetNormalizedToWorldMatrix` — RVA `0xc51d90`

- Decompiled symbol: `TouchControl_GetNormalizedToWorldMatrix`
- Metadata signature: `public Matrix4x4 GetNormalizedToWorldMatrix() { }`
- Native interval: `304` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[904];
    struct struct_1 *field_388;
    unsigned long long field_390;
} struct_0;

typedef struct struct_1 {
    unsigned long long field_0;
} struct_1;

void TouchControl_GetNormalizedToWorldMatrix(struct_0 **a0)
{
    unsigned long long v9;  // d11
    unsigned long long v10;  // d10
    unsigned long long v11;  // d9
    unsigned long long v12;  // d8
    unsigned long long v13;  // x30
    unsigned long long v14;  // x20
    unsigned long long v15;  // x19
    unsigned long long v16;  // x1
    unsigned long long v0;  // [bp-0x40]
    unsigned long long v1;  // [bp-0x38]
    unsigned long long v2;  // [bp-0x30]
    unsigned long long v3;  // [bp-0x28]
    char *v4;  // [bp-0x20]
    unsigned long long v5;  // [bp-0x18]
    unsigned long long v6;  // [bp-0x10]
    unsigned long long v7;  // [bp-0x8]
    char v8;  // [bp+0x0]

    v0 = v9;
    v1 = v10;
    v2 = v11;
    v3 = v12;
    v4 = &v8;
    v5 = v13;
    v6 = v14;
    v7 = v15;
    v16 = *(a0)->field_390;
    *(a0)->field_388();
}
```

## `TouchControl.GetFollowPos` — RVA `0xc51ec0`

- Decompiled symbol: `TouchControl_GetFollowPos`
- Metadata signature: `protected Vector3 GetFollowPos(Vector3 targetWorldPos, Vector2 worldOffset, out bool posWasOutside) { }`
- Native interval: `260` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[904];
    struct struct_1 *field_388;
    unsigned long long field_390;
} struct_0;

typedef struct struct_1 {
    unsigned long long field_0;
} struct_1;

void TouchControl_GetFollowPos(struct_0 **a0, unsigned long a1)
{
    unsigned long long v9;  // d13
    unsigned long long v10;  // d12
    unsigned long long v11;  // d11
    unsigned long long v12;  // d10
    unsigned long long v13;  // d9
    unsigned long long v14;  // d8
    unsigned long long v15;  // x30
    unsigned long long v16;  // x20
    unsigned long long v17;  // x19
    unsigned long long v0;  // [bp-0x50]
    unsigned long long v1;  // [bp-0x48]
    unsigned long long v2;  // [bp-0x40]
    unsigned long long v3;  // [bp-0x38]
    unsigned long long v4;  // [bp-0x30]
    unsigned long long v5;  // [bp-0x28]
    unsigned long long v6;  // [bp-0x20]
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
    TouchControl__WorldToNormalizedPos(a0); /* do not return */
}
```

## `TouchControl.GetFollowPos` — RVA `0xc520fc`

- Decompiled symbol: `TouchControl_GetFollowPos`
- Metadata signature: `protected Vector3 GetFollowPos(Vector3 targetWorldPos, Vector3 worldOffset) { }`
- Native interval: `24` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[904];
    struct struct_1 *field_388;
    unsigned long long field_390;
} struct_0;

typedef struct struct_1 {
    unsigned long long field_0;
} struct_1;

void TouchControl_GetFollowPos(void)
{
    struct_0 **v1;  // x0
    char flag;  // [bp-0x4]

    flag = 0;
    TouchControl__GetFollowPos(v1, &flag);
    return;
}
```

## `TouchControl.ClampInsideCanvas` — RVA `0xc52114`

- Decompiled symbol: `TouchControl_ClampInsideCanvas`
- Metadata signature: `protected Vector3 ClampInsideCanvas(Vector3 targetWorldPos, Canvas limiterCanvas) { }`
- Native interval: `784` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[904];
    struct struct_2 *field_388;
    unsigned long long field_390;
} struct_1;

typedef struct struct_2 {
    unsigned long long field_0;
} struct_2;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern unsigned long long g_1ef1170;
extern char g_1fab25b;

long long TouchControl_ClampInsideCanvas(struct_1 **a0, long long a1)
{
    long long v6;  // x0
    long long v7;  // x0
    long long v8;  // x21
    unsigned long long flag;  // x2
    long long v10;  // x0
    struct_1 **v11;  // x0
    unsigned long v12;  // x1
    uint128_t flag3;  // [bp-0xf0]
    uint128_t flag4;  // [bp-0xe0]
    uint128_t choice;  // [bp-0xd0]
    uint128_t flag2;  // [bp-0xc0]
    char *v4;  // [bp-0x30]
    char v5;  // [bp+0x0]

    v4 = &v5;
    if (!(g_1fab25b & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c(&g_1ef1170);
        g_1fab25b = 1;
    }
    choice = 0;
    flag2 = 0;
    flag3 = 0;
    flag4 = 0;
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v6 = Object__op_Equality(a1, 0, 0);
    if (((char)v6 & 1))
    {
        return v6;
    }
    else if (a1)
    {
        v7 = Component__get_transform(a1, 0);
        if (v7)
        {
            if (*((long long *)v7) == g_1ef1170)
                v8 = v7;
            else
                v8 = 0;
        }
        else
        {
            v8 = 0;
        }
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        flag = 0;
        v10 = Object__op_Equality(v8, 0, 0);
        if (((char)v10 & 1))
            return v10;
        v11 = a0;
        v12 = *(a0)->field_390;
        *(a0)->field_388();
    }
    else
    {
        sub_f7db74();
    }
}
```

## `TouchControl.ClampInsideOther` — RVA `0xc524b8`

- Decompiled symbol: `TouchControl_ClampInsideOther`
- Metadata signature: `protected Vector3 ClampInsideOther(Vector3 targetWorldPos, TouchControl limiter) { }`
- Native interval: `636` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[904];
    struct struct_1 *field_388;
    unsigned long long field_390;
} struct_0;

typedef struct struct_1 {
    unsigned long long field_0;
} struct_1;

void TouchControl_ClampInsideOther(struct_0 **a0, unsigned long a1)
{
    unsigned long long v17;  // d15
    unsigned long long v18;  // d14
    unsigned long long v27;  // x19
    unsigned long long v28;  // x1
    unsigned long long v19;  // d13
    unsigned long long v20;  // d12
    unsigned long long v21;  // d11
    unsigned long long v22;  // d10
    unsigned long long v23;  // d9
    unsigned long long v24;  // d8
    unsigned long long v25;  // x30
    unsigned long long v26;  // x20
    uint128_t flag2;  // [bp-0xe0]
    uint128_t flag3;  // [bp-0xd0]
    uint128_t flag;  // [bp-0xc0]
    uint128_t choice;  // [bp-0xb0]
    unsigned long long v4;  // [bp-0x60]
    unsigned long long v5;  // [bp-0x58]
    unsigned long long v6;  // [bp-0x50]
    unsigned long long v7;  // [bp-0x48]
    unsigned long long v8;  // [bp-0x40]
    unsigned long long v9;  // [bp-0x38]
    unsigned long long v10;  // [bp-0x30]
    unsigned long long v11;  // [bp-0x28]
    char *v12;  // [bp-0x20]
    unsigned long long v13;  // [bp-0x18]
    unsigned long long v14;  // [bp-0x10]
    unsigned long long v15;  // [bp-0x8]
    char v16;  // [bp+0x0]

    v4 = v17;
    v5 = v18;
    v6 = v19;
    v7 = v20;
    v8 = v21;
    v9 = v22;
    v10 = v23;
    v11 = v24;
    v12 = &v16;
    v13 = v25;
    v14 = v26;
    v15 = v27;
    flag = 0;
    choice = 0;
    flag2 = 0;
    flag3 = 0;
    v28 = *(a0)->field_390;
    *(a0)->field_388();
}
```

## `TouchControl.RaycastLocal` — RVA `0xc52734`

- Decompiled symbol: `TouchControl_RaycastLocal`
- Metadata signature: `public bool RaycastLocal(Vector2 localPos) { }`
- Native interval: `236` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[904];
    struct struct_1 *field_388;
    unsigned long long field_390;
} struct_0;

typedef struct struct_1 {
    unsigned long long field_0;
} struct_1;

void TouchControl_RaycastLocal(struct_0 **a0)
{
    unsigned long long v4;  // d9
    unsigned long long v5;  // d8
    unsigned long long v6;  // x30
    unsigned long long v7;  // x19
    unsigned long long v8;  // x1
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x18]
    unsigned long long v2;  // [bp-0x10]
    unsigned long long v3;  // [bp-0x8]

    v0 = v4;
    v1 = v5;
    v2 = v6;
    v3 = v7;
    v8 = *(a0)->field_390;
    *(a0)->field_388();
}
```

## `TouchControl.HitTest` — RVA `0xc52820`

- Decompiled symbol: `TouchControl_HitTest`
- Metadata signature: `public bool HitTest(Vector2 sp, Camera cam, float fingerRadPx, TouchControl.Hit hit) { }`
- Native interval: `1144` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned long long field_10;
} struct_0;

typedef struct struct_3 {
    struct struct_1 *field_0;
    char padding_8[26];
    char field_22;
} struct_3;

typedef struct struct_1 {
    char padding_0[904];
    struct struct_2 *field_388;
    unsigned long long field_390;
} struct_1;

typedef struct struct_2 {
    unsigned long long field_0;
} struct_2;

void TouchControl_HitTest(struct_3 *a0, long long a1, struct_0 *ptr)
{
    unsigned long long v22;  // d15
    unsigned long long v23;  // d14
    unsigned long long v32;  // x25
    unsigned long long v33;  // x24
    unsigned long long v34;  // x23
    unsigned long long v35;  // x22
    unsigned long long v36;  // x21
    unsigned long long v37;  // x20
    unsigned long long v38;  // x19
    unsigned int v39;  // s2
    unsigned long v40;  // 4128
    unsigned int v41;  // s0
    unsigned long long v24;  // d13
    unsigned int v42;  // s1
    struct_3 *v43;  // x0
    unsigned long v44;  // x1
    unsigned long long v25;  // d12
    unsigned long long v26;  // d11
    unsigned long long v27;  // d10
    unsigned long long v28;  // d9
    unsigned long long v29;  // d8
    unsigned long long v30;  // x30
    unsigned long long v31;  // x26
    unsigned int v0;  // [bp-0xa0]
    unsigned int v1;  // [bp-0x98]
    unsigned int v2;  // [bp-0x94]
    unsigned long long v3;  // [bp-0x90]
    unsigned long long v4;  // [bp-0x88]
    unsigned long long v5;  // [bp-0x80]
    unsigned long long v6;  // [bp-0x78]
    unsigned long long v7;  // [bp-0x70]
    unsigned long long v8;  // [bp-0x68]
    unsigned long long v9;  // [bp-0x60]
    unsigned long long v10;  // [bp-0x58]
    unsigned long long v11;  // [bp-0x50]
    unsigned int v12;  // [bp-0x48]
    unsigned int v13;  // [bp-0x44]
    unsigned long long v14;  // [bp-0x40]
    unsigned long long v15;  // [bp-0x38]
    unsigned long long v16;  // [bp-0x30]
    unsigned long long v17;  // [bp-0x28]
    unsigned long long v18;  // [bp-0x20]
    unsigned long long v19;  // [bp-0x18]
    unsigned long long v20;  // [bp-0x10]
    unsigned long long v21;  // [bp-0x8]

    v3 = v22;
    v4 = v23;
    v5 = v24;
    v6 = v25;
    v7 = v26;
    v8 = v27;
    v9 = v28;
    v10 = v29;
    v11 = v30;
    v14 = v31;
    v15 = v32;
    v16 = v33;
    v17 = v34;
    v18 = v35;
    v19 = v36;
    v20 = v37;
    v21 = v38;
    if (!ptr)
        sub_f7db74();
    ptr->field_10 = 0;
    sub_f7d8d0((struct struct_0 *)&ptr->field_10, 0);
    v40 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(v39, 981668463)) >> 5 & 3 | (unsigned long long)(CmpF(v39, 981668463) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v39, 981668463)) >> 5 & 3 | (unsigned long long)(CmpF(v39, 981668463) & 1)) & ((unsigned long long)(char)(CmpF(v39, 981668463)) >> 5 & 3 | (unsigned long long)(CmpF(v39, 981668463) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    v0 = v39;
    v1 = v41;
    v2 = v42;
    TouchControl__ScreenToLocalPos(a0, a1);
    v43 = a0;
    v12 = v41;
    v13 = v42;
    v44 = a0->field_0->field_390;
    a0->field_0->field_388();
}
```

## `TouchControl.OnInitComponent` — RVA `0xc52d44`

- Decompiled symbol: `TouchControl_OnInitComponent`
- Metadata signature: `protected override void OnInitComponent() { }`
- Native interval: `80` bytes
- Result: `pseudocode`
- Heuristic layout hint: `TouchControl_Recovered` matched 4 offsets against `TouchControl` metadata (confidence 0.80).

```c
typedef struct TouchControl_Recovered {
    struct struct_0 *field_0;
    char padding_8[105];
    char baseAlphaAnimOn;
    char padding_72[2];
    unsigned int baseAlphaStart;
    unsigned long long baseAlphaEnd;
    char baseAlphaCur;
} TouchControl_Recovered;

typedef struct struct_0 {
    char padding_0[872];
    struct struct_1 *field_368;
    unsigned long long field_370;
} struct_0;

typedef struct struct_1 {
    unsigned long long field_0;
} struct_1;

void TouchControl_OnInitComponent(struct_2 *ptr)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    unsigned int v4;  // s0
    struct_0 *p;  // x8
    unsigned long long v6;  // x1
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    v4 = *((int *)((char *)&ptr->field_78 + 4));
    p = ptr->field_0;
    ptr->field_71 = 0;
    ptr->field_78 = 0x3f8000003f800000;
    ptr->field_74 = v4;
    v6 = p->field_370;
    p->field_368();
}
```

## `TouchControl.OnEnableComponent` — RVA `0xc52d94`

- Decompiled symbol: `TouchControl_OnEnableComponent`
- Metadata signature: `protected override void OnEnableComponent() { }`
- Native interval: `40` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[664];
    struct struct_1 *field_298;
    unsigned long long field_2a0;
} struct_0;

typedef struct struct_1 {
    unsigned long long field_0;
} struct_1;

void TouchControl_OnEnableComponent(struct_0 **a0)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    unsigned long long v4;  // x1
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    v4 = *(a0)->field_2a0;
    *(a0)->field_298();
}
```

## `TouchControl.OnDisableComponent` — RVA `0xc52dbc`

- Decompiled symbol: `TouchControl_OnDisableComponent`
- Metadata signature: `protected override void OnDisableComponent() { }`
- Native interval: `60` bytes
- Result: `pseudocode`
- Heuristic layout hint: `TouchControl_Recovered` matched 3 offsets against `TouchControl` metadata (confidence 0.75).

```c
typedef struct TouchControl_Recovered {
    struct struct_1 *field_0;
    char padding_8[64];
    unsigned long long disablingConditions;
    unsigned int hidingFlagsCur;
    char padding_54[4];
    struct struct_3 *_rig;
} TouchControl_Recovered;

typedef struct struct_1 {
    char padding_0[680];
    struct struct_2 *field_2a8;
    unsigned long long field_2b0;
} struct_1;

typedef struct struct_3 {
    char padding_0[304];
    char field_130;
} struct_3;

typedef struct struct_2 {
    unsigned long long field_0;
} struct_2;

void TouchControl_OnDisableComponent(struct_4 *a0)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    struct_4 *v4;  // x0
    unsigned long v5;  // x1
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    TouchControl__SyncDisablingConditions(a0, 1);
    v4 = a0;
    v5 = a0->field_0->field_2b0;
    a0->field_0->field_2a8();
}
```

## `TouchControl.OnDestroyComponent` — RVA `0xc52df8`

- Decompiled symbol: `TouchControl_OnDestroyComponent`
- Metadata signature: `protected override void OnDestroyComponent() { }`
- Native interval: `52` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[552];
    unsigned long long field_228;
} struct_0;

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

void TouchControl_OnDestroyComponent(struct_0 **a0)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    TouchControl__SetRig(a0, NULL);
    TouchControl__SetTouchControlPanel(a0, NULL);
    goto *(a0)->field_228;
}
```

## `TouchControl.UpdateControl` — RVA `0xc52e2c`

- Decompiled symbol: `TouchControl_UpdateControl`
- Metadata signature: `public void UpdateControl() { }`
- Native interval: `100` bytes
- Result: `pseudocode`
- Heuristic layout hint: `TouchControl_Recovered` matched 6 offsets against `TouchControl` metadata (confidence 1.00).

```c
typedef struct TouchControl_Recovered {
    char padding_0[113];
    char baseAlphaAnimOn;
    char padding_72[2];
    unsigned int baseAlphaStart;
    unsigned int baseAlphaEnd;
    unsigned int baseAlphaCur;
    unsigned int baseAlphaAnimDur;
    unsigned int baseAlphaAnimElapsed;
} TouchControl_Recovered;

void TouchControl_UpdateControl(struct_0 *ptr)
{
    struct_0 *p;  // x8
    struct_0 *v1;  // x0
    unsigned long v2;  // x1
    struct_0 *v3;  // x0
    unsigned long v4;  // x1

    if (ptr->padding_0[33])
        return;
    if (ptr->padding_0[32])
    {
        TouchControl__UpdateBaseAlpha(ptr);
        v3 = ptr;
        v4 = *((long long *)(*((long long *)&ptr->padding_0[0]) + 544));
        (*((long long *)(*((long long *)&ptr->padding_0[0]) + 536)))();
    }
    p = *((long long *)&ptr->padding_0[0]);
    ptr->padding_0[32] = 1;
    v1 = ptr;
    v2 = *((long long *)&p[2].padding_0[112]);
    (*((long long *)&p[2].padding_0[104]))();
}
```

## `TouchControl.DrawDefaultGizmo` — RVA `0xc52e90`

- Decompiled symbol: `TouchControl_DrawDefaultGizmo`
- Metadata signature: `protected void DrawDefaultGizmo(bool drawFullRect) { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long TouchControl_DrawDefaultGizmo(void)
{
    unsigned long v0;  // x0

    return v0;
}
```

## `TouchControl.DrawDefaultGizmo` — RVA `0xc52e94`

- Decompiled symbol: `TouchControl_DrawDefaultGizmo`
- Metadata signature: `protected void DrawDefaultGizmo(bool drawFullRect, float fullRectColorShade) { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long TouchControl_DrawDefaultGizmo(void)
{
    unsigned long v0;  // x0

    return v0;
}
```

## `TouchControl.DrawCustomGizmos` — RVA `0xc52e98`

- Decompiled symbol: `TouchControl_DrawCustomGizmos`
- Metadata signature: `protected virtual void DrawCustomGizmos(bool selected) { }`
- Native interval: `112` bytes
- Result: `pseudocode`

```c
void TouchControl_DrawCustomGizmos(unsigned long a0, unsigned int a1)
{
    unsigned long long v6;  // d11
    unsigned long long v7;  // d10
    unsigned long long v8;  // d9
    unsigned long long v9;  // d8
    unsigned long long v10;  // x30
    unsigned long long v11;  // x19
    unsigned long v12;  // 4121
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
    Gizmos__get_color(0);
    v12 = arm64g_calculate_condition(25, (unsigned long long)(a1 & 1), 0, 0);
    Gizmos__set_color();
    Gizmos__set_color();
    return;
}
```

## `TouchControl.OnDrawGizmos` — RVA `0xc52f08`

- Decompiled symbol: `TouchControl_OnDrawGizmos`
- Metadata signature: `private void OnDrawGizmos() { }`
- Native interval: `32` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    struct struct_0 *field_0;
    char padding_8[24];
    char field_20;
} struct_1;

typedef struct struct_0 {
    char padding_0[920];
    unsigned long long field_398;
} struct_0;

struct_1 * TouchControl_OnDrawGizmos(struct_1 *a0)
{
    if (!a0->field_20)
        return a0;
    goto a0->field_0->field_398;
}
```

## `TouchControl.OnDrawGizmosSelected` — RVA `0xc52f28`

- Decompiled symbol: `TouchControl_OnDrawGizmosSelected`
- Metadata signature: `private void OnDrawGizmosSelected() { }`
- Native interval: `32` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    struct struct_0 *field_0;
    char padding_8[24];
    char field_20;
} struct_1;

typedef struct struct_0 {
    char padding_0[920];
    unsigned long long field_398;
} struct_0;

struct_1 * TouchControl_OnDrawGizmosSelected(struct_1 *a0)
{
    if (!a0->field_20)
        return a0;
    goto a0->field_0->field_398;
}
```
