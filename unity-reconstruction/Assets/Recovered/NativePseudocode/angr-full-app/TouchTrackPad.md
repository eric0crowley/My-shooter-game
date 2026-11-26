# Native pseudocode: TouchTrackPad

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `TouchTrackPad.ctor` — RVA `0xc57978`

- Decompiled symbol: `TouchTrackPad_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `400` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[40];
    unsigned long long field_28;
    long long field_30;
    char padding_38[8];
    long long field_40;
    long long field_48;
} struct_0;

extern long long g_1ef1e08;
extern long long g_1f0c3a8;
extern long long g_1f0c3b0;
extern char g_1fab294;

void TouchTrackPad_ctor(struct_0 *a0)
{
    unsigned long long v8;  // x30
    unsigned long long v9;  // x25
    unsigned long long v10;  // x24
    unsigned long long v11;  // x23
    unsigned long long v12;  // x22
    unsigned long long v13;  // x21
    unsigned long long v14;  // x20
    unsigned long long v15;  // x19
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
    if (!(g_1fab294 & 1))
    {
        sub_f7d92c("g.");
        sub_f7d92c("y7");
        sub_f7d92c(&g_1ef1e08);
        sub_f7d92c(&g_1f0c3b0);
        sub_f7d92c(&g_1f0c3a8);
        g_1fab294 = 1;
    }
    TouchControl__ctor(a0); /* do not return */
}
```

## `TouchTrackPad.Pressed` — RVA `0xc57b08`

- Decompiled symbol: `TouchTrackPad_Pressed`
- Metadata signature: `public bool Pressed() { }`
- Native interval: `28` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[200];
    struct struct_0 *field_c8;
} struct_1;

typedef struct struct_0 {
    char padding_0[28];
    char field_1c;
} struct_0;

long long TouchTrackPad_Pressed(struct_1 *a0)
{
    if (a0->field_c8)
        return a0->field_c8->field_1c;
    sub_f7db74();
}
```

## `TouchTrackPad.JustPressed` — RVA `0xc57b24`

- Decompiled symbol: `TouchTrackPad_JustPressed`
- Metadata signature: `public bool JustPressed() { }`
- Native interval: `28` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[200];
    long long field_c8;
} struct_0;

long long TouchTrackPad_JustPressed(struct_0 *a0)
{
    unsigned long v0;  // x0

    if (a0->field_c8)
    {
        v0 = TouchGestureBasicState__JustPressedRaw(a0->field_c8, 0);
        return TouchGestureBasicState__JustPressedRaw(a0->field_c8, 0);
    }
    sub_f7db74(0);
}
```

## `TouchTrackPad.JustReleased` — RVA `0xc57b40`

- Decompiled symbol: `TouchTrackPad_JustReleased`
- Metadata signature: `public bool JustReleased() { }`
- Native interval: `28` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[200];
    long long field_c8;
} struct_0;

long long TouchTrackPad_JustReleased(struct_0 *a0)
{
    unsigned long v0;  // x0

    if (a0->field_c8)
    {
        v0 = TouchGestureBasicState__JustReleasedRaw(a0->field_c8, 0);
        return TouchGestureBasicState__JustReleasedRaw(a0->field_c8, 0);
    }
    sub_f7db74(0);
}
```

## `TouchTrackPad.IsTouchPressureSensitive` — RVA `0xc57b5c`

- Decompiled symbol: `TouchTrackPad_IsTouchPressureSensitive`
- Metadata signature: `public bool IsTouchPressureSensitive() { }`
- Native interval: `48` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[200];
    struct struct_0 *field_c8;
} struct_1;

typedef struct struct_0 {
    char padding_0[28];
    char field_1c;
} struct_0;

unsigned long long TouchTrackPad_IsTouchPressureSensitive(struct_1 *a0)
{
    unsigned long long v0;  // x0

    if (a0->field_c8)
    {
        if (a0->field_c8->field_1c)
        {
            v0 = TouchGestureBasicState__IsPressureSensitive();
            return TouchGestureBasicState__IsPressureSensitive();
        }
        return 0;
    }
    sub_f7db74(0);
}
```

## `TouchTrackPad.GetTouchPressure` — RVA `0xc57b8c`

- Decompiled symbol: `TouchTrackPad_GetTouchPressure`
- Metadata signature: `public float GetTouchPressure() { }`
- Native interval: `48` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    char padding_0[28];
    char field_1c;
} struct_2;

typedef struct struct_1 {
    char padding_0[200];
    struct struct_0 *field_c8;
} struct_1;

typedef struct struct_0 {
    char padding_0[28];
    char field_1c;
} struct_0;

struct_2 * TouchTrackPad_GetTouchPressure(struct_1 *ptr)
{
    struct_0 *v0;  // x0
    unsigned long long v1;  // x0

    v0 = ptr->field_c8;
    if (v0)
    {
        if (v0->field_1c)
        {
            v1 = TouchGestureBasicState__GetPressure();
            return TouchGestureBasicState__GetPressure();
        }
        return v0;
    }
    sub_f7db74(0);
}
```

## `TouchTrackPad.GetSwipeDelta` — RVA `0xc57bbc`

- Decompiled symbol: `TouchTrackPad_GetSwipeDelta`
- Metadata signature: `public Vector2 GetSwipeDelta() { }`
- Native interval: `28` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[200];
    long long field_c8;
} struct_0;

long long TouchTrackPad_GetSwipeDelta(struct_0 *a0)
{
    unsigned long long v0;  // x0

    if (a0->field_c8)
    {
        v0 = TouchGestureBasicState__GetDeltaVecSmooth(a0->field_c8, 0);
        return TouchGestureBasicState__GetDeltaVecSmooth(a0->field_c8, 0);
    }
    sub_f7db74(0);
}
```

## `TouchTrackPad.SetTouchSmoothing` — RVA `0xc57bd8`

- Decompiled symbol: `TouchTrackPad_SetTouchSmoothing`
- Metadata signature: `public void SetTouchSmoothing(float smTime) { }`
- Native interval: `64` bytes
- Result: `pseudocode`
- Heuristic layout hint: `TouchTrackPad_Recovered` matched 2 offsets against `TouchTrackPad` metadata (confidence 1.00).

```c
typedef struct TouchTrackPad_Recovered {
    char padding_0[136];
    unsigned int touchSmoothing;
    char padding_8c[60];
    struct struct_0 *touchState;
} TouchTrackPad_Recovered;

typedef struct struct_0 {
    char padding_0[164];
    unsigned int field_a4;
} struct_0;

void TouchTrackPad_SetTouchSmoothing(struct_1 *ptr)
{
    struct_0 *p;  // x8
    unsigned int v1;  // s1
    unsigned int flag;  // s0
    unsigned int v3;  // s0
    unsigned long v4;  // 4142
    unsigned int v5;  // s0

    p = ptr->field_c8;
    v1 = [D] unsupported_Iop_ZeroHI96ofV128();
    flag = 0;
    v4 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v3, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v3, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v3, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v3, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v3, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v3, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if ((char)v4)
        v5 = v1;
    else
        v5 = flag;
    ptr->field_88 = v5;
    if (p)
    {
        p->field_a4 = v5 * 1036831949;
        return;
    }
    sub_f7db74();
}
```

## `TouchTrackPad.OnInitControl` — RVA `0xc57c18`

- Decompiled symbol: `TouchTrackPad_OnInitControl`
- Metadata signature: `protected override void OnInitControl() { }`
- Native interval: `88` bytes
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

void TouchTrackPad_OnInitControl(struct_0 **a0)
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

## `TouchTrackPad.OnDestroyControl` — RVA `0xc57c70`

- Decompiled symbol: `TouchTrackPad_OnDestroyControl`
- Metadata signature: `protected override void OnDestroyControl() { }`
- Native interval: `16` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[664];
    unsigned long long field_298;
} struct_0;

long long TouchTrackPad_OnDestroyControl(struct_0 **a0)
{
    goto *(a0)->field_298;
}
```

## `TouchTrackPad.ResetControl` — RVA `0xc57c80`

- Decompiled symbol: `TouchTrackPad_ResetControl`
- Metadata signature: `public override void ResetControl() { }`
- Native interval: `52` bytes
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

void TouchTrackPad_ResetControl(struct_0 **a0)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    unsigned long long v4;  // x1
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    v4 = *(a0)->field_2b0;
    *(a0)->field_2a8();
}
```

## `TouchTrackPad.OnUpdateControl` — RVA `0xc57cb4`

- Decompiled symbol: `TouchTrackPad_OnUpdateControl`
- Metadata signature: `protected override void OnUpdateControl() { }`
- Native interval: `180` bytes
- Result: `pseudocode`
- Heuristic layout hint: `TouchTrackPad_Recovered` matched 2 offsets against `TouchTrackPad` metadata (confidence 0.67).

```c
typedef struct TouchTrackPad_Recovered {
    char padding_0[88];
    struct struct_4 *field_58;
    char padding_60[88];
    unsigned long long touchObj;
    char padding_c0[8];
    struct struct_4 *touchState;
} TouchTrackPad_Recovered;

typedef struct struct_1 {
    char padding_0[392];
    struct struct_2 *field_188;
    unsigned long long field_190;
} struct_1;

typedef struct struct_4 {
    struct struct_1 *field_0;
} struct_4;

typedef struct struct_2 {
    unsigned long long field_0;
} struct_2;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab295;

void TouchTrackPad_OnUpdateControl(struct_3 *ptr)
{
    unsigned long long v3;  // x30
    unsigned long long v4;  // x20
    unsigned long long v5;  // x19
    unsigned long long v6;  // x2
    struct_1 **v7;  // x0
    unsigned long long v8;  // x1
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x10]
    unsigned long long v2;  // [bp-0x8]

    v0 = v3;
    v1 = v4;
    v2 = v5;
    if (!(g_1fab295 & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab295 = 1;
    }
    if (ptr->field_b8)
    {
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        v6 = 0;
        if (((char)Object__op_Inequality(ptr->field_58, 0, 0) & 1))
        {
            v7 = ptr->field_58;
            if (!v7)
                goto LABEL_1057d64;
            InputRig__WakeTouchControlsUp(v7);
        }
    }
    v7 = ptr->field_c8;
    if (v7)
    {
        v8 = *(v7)->field_190;
        *(v7)->field_188();
    }
LABEL_1057d64:
    sub_f7db74(v7);
}
```

## `TouchTrackPad.SyncRigState` — RVA `0xc57d68`

- Decompiled symbol: `TouchTrackPad_SyncRigState`
- Metadata signature: `private void SyncRigState() { }`
- Native interval: `212` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: CFGFast did not recover a function at the metadata RVA

```c
// 0x1057d68: str d8, [sp, #-0x20]!
// 0x1057d6c: str x30, [sp, #8]
// 0x1057d70: stp x20, x19, [sp, #0x10]
// 0x1057d74: ldr x8, [x0, #0xc8]
// 0x1057d78: cbz x8, #0x1057e38
// 0x1057d7c: ldrb w8, [x8, #0x1c]
// 0x1057d80: mov x19, x0
// 0x1057d84: cbz w8, #0x1057dec
// 0x1057d88: ldr x0, [x19, #0x90]
// 0x1057d8c: cbz x0, #0x1057e38
// 0x1057d90: ldr x2, [x19, #0x58]
// 0x1057d94: mov w1, #1
// 0x1057d98: mov w3, wzr
// 0x1057d9c: bl #0x104f00c
// 0x1057da0: mov x0, x19
// 0x1057da4: bl #0x1057b5c
// 0x1057da8: tbz w0, #0, #0x1057dcc
// 0x1057dac: ldr x20, [x19, #0xb0]
// 0x1057db0: mov x0, x19
// 0x1057db4: bl #0x1057b8c
// 0x1057db8: cbz x20, #0x1057e38
// 0x1057dbc: ldr x2, [x19, #0x58]
// 0x1057dc0: mov w1, #1
// 0x1057dc4: mov x0, x20
// 0x1057dc8: b #0x1057de8
// 0x1057dcc: ldrb w8, [x19, #0xa8]
// 0x1057dd0: cbz w8, #0x1057dec
// 0x1057dd4: ldr x0, [x19, #0xb0]
// 0x1057dd8: cbz x0, #0x1057e38
// 0x1057ddc: ldr x2, [x19, #0x58]
// 0x1057de0: fmov s0, #1.00000000
// 0x1057de4: mov w1, wzr
// 0x1057de8: bl #0x104f160
// 0x1057dec: ldr x0, [x19, #0xc8]
// 0x1057df0: cbz x0, #0x1057e38
// 0x1057df4: mov x1, xzr
// 0x1057df8: bl #0x1061c94
// 0x1057dfc: ldr x0, [x19, #0x98]
// 0x1057e00: cbz x0, #0x1057e38
// 0x1057e04: ldr x2, [x19, #0x58]
// 0x1057e08: mov w1, #3
// 0x1057e0c: mov v8.16b, v1.16b
// 0x1057e10: bl #0x104f160
// 0x1057e14: ldr x0, [x19, #0xa0]
// 0x1057e18: cbz x0, #0x1057e38
// 0x1057e1c: ldr x2, [x19, #0x58]
// 0x1057e20: ldp x20, x19, [sp, #0x10]
// 0x1057e24: ldr x30, [sp, #8]
// 0x1057e28: mov w1, #3
// 0x1057e2c: mov v0.16b, v8.16b
// 0x1057e30: ldr d8, [sp], #0x20
// 0x1057e34: b #0x104f160
// 0x1057e38: bl #0xf7db74
```

## `TouchTrackPad.OnIsBoundToAxis` — RVA `0xc57e3c`

- Decompiled symbol: `TouchTrackPad_OnIsBoundToAxis`
- Metadata signature: `protected override bool OnIsBoundToAxis(string axisName, InputRig rig) { }`
- Native interval: `148` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[144];
    long long field_90;
} struct_0;

long long TouchTrackPad_OnIsBoundToAxis(struct_0 *a0, unsigned long a1, unsigned long a2)
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
    if (a0->field_90)
        InputBindingBase__IsBoundToAxis(a0->field_90); /* do not return */
    sub_f7db74(0);
}
```

## `TouchTrackPad.OnIsBoundToKey` — RVA `0xc57ed0`

- Decompiled symbol: `TouchTrackPad_OnIsBoundToKey`
- Metadata signature: `protected override bool OnIsBoundToKey(KeyCode key, InputRig rig) { }`
- Native interval: `148` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[144];
    long long field_90;
} struct_0;

long long TouchTrackPad_OnIsBoundToKey(struct_0 *a0, unsigned long a1, unsigned long a2, unsigned long a3)
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
    if (a0->field_90)
        InputBindingBase__IsBoundToKey(a0->field_90); /* do not return */
    sub_f7db74(0);
}
```

## `TouchTrackPad.OnGetSubBindingDescriptions` — RVA `0xc57f64`

- Decompiled symbol: `TouchTrackPad_OnGetSubBindingDescriptions`
- Metadata signature: `protected override void OnGetSubBindingDescriptions(BindingDescriptionList descList, Object undoObject, string parentMenuPath) { }`
- Native interval: `276` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[144];
    long long field_90;
} struct_0;

extern long long g_1f0ab68;
extern long long g_1f0d040;
extern long long g_1f0f990;
extern char g_1fab296;

long long TouchTrackPad_OnGetSubBindingDescriptions(struct_0 *a0, long long a1, unsigned long a2, long long a3)
{
    unsigned long long v7;  // x30
    unsigned long long v8;  // x24
    unsigned long long v9;  // x23
    unsigned long long v10;  // x22
    unsigned long long v11;  // x21
    unsigned long long v12;  // x20
    unsigned long long v13;  // x19
    unsigned long long v0;  // [bp-0x40]
    unsigned long long v1;  // [bp-0x30]
    unsigned long long v2;  // [bp-0x28]
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
    if (!(g_1fab296 & 1))
    {
        sub_f7d92c(&g_1f0f990);
        sub_f7d92c(&g_1f0d040);
        sub_f7d92c("+#");
        sub_f7d92c(&g_1f0ab68);
        g_1fab296 = 1;
    }
    if (a1)
        BindingDescriptionList__Add(a1, a0->field_90, g_1f0d040, a3, a0, 0); /* do not return */
    sub_f7db74();
}
```

## `TouchTrackPad.CanBeTouchedDirectly` — RVA `0xc58078`

- Decompiled symbol: `TouchTrackPad_CanBeTouchedDirectly`
- Metadata signature: `public override bool CanBeTouchedDirectly(TouchObject touchObj) { }`
- Native interval: `44` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[35];
    char field_23;
    char padding_24[44];
    unsigned int field_50;
    char padding_54[100];
    unsigned long long field_b8;
} struct_0;

unsigned long long TouchTrackPad_CanBeTouchedDirectly(struct_0 *a0)
{
    unsigned long v0;  // 4115

    if (a0->field_23)
        return 0;
    v0 = arm64g_calculate_condition(9, (unsigned long long)(a0->field_50 & 4294967231), 0, 0);
    if (!((char)v0))
    {
        return 0;
    }
    else if (a0->field_b8)
    {
        return 0;
    }
    else
    {
        return 1;
    }
}
```

## `TouchTrackPad.CanBeActivatedByOtherControl` — RVA `0xc580a4`

- Decompiled symbol: `TouchTrackPad_CanBeActivatedByOtherControl`
- Metadata signature: `public override bool CanBeActivatedByOtherControl(TouchControl c, TouchObject touchObj) { }`
- Native interval: `36` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[80];
    unsigned int field_50;
    char padding_54[100];
    unsigned long long field_b8;
} struct_0;

unsigned long long TouchTrackPad_CanBeActivatedByOtherControl(struct_0 *a0)
{
    unsigned long v0;  // 4115

    v0 = arm64g_calculate_condition(9, (unsigned long long)(a0->field_50 & 4294967231), 0, 0);
    if (!((char)v0))
    {
        return 0;
    }
    else if (a0->field_b8)
    {
        return 0;
    }
    else
    {
        return 1;
    }
}
```

## `TouchTrackPad.CanBeSwipedOverFromNothing` — RVA `0xc580c8`

- Decompiled symbol: `TouchTrackPad_CanBeSwipedOverFromNothing`
- Metadata signature: `public override bool CanBeSwipedOverFromNothing(TouchObject touchObj) { }`
- Native interval: `44` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[38];
    char field_26;
    char padding_27[41];
    unsigned int field_50;
    char padding_54[100];
    unsigned long long field_b8;
} struct_0;

unsigned long long TouchTrackPad_CanBeSwipedOverFromNothing(struct_0 *a0)
{
    unsigned long v0;  // 4115

    if (!a0->field_26)
        return 0;
    v0 = arm64g_calculate_condition(9, (unsigned long long)(a0->field_50 & 4294967231), 0, 0);
    if (!((char)v0))
    {
        return 0;
    }
    else if (a0->field_b8)
    {
        return 0;
    }
    else
    {
        return 1;
    }
}
```

## `TouchTrackPad.CanBeSwipedOverFromRestrictedList` — RVA `0xc580f4`

- Decompiled symbol: `TouchTrackPad_CanBeSwipedOverFromRestrictedList`
- Metadata signature: `public override bool CanBeSwipedOverFromRestrictedList(TouchObject touchObj) { }`
- Native interval: `36` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[80];
    unsigned int field_50;
    char padding_54[100];
    unsigned long long field_b8;
} struct_0;

unsigned long long TouchTrackPad_CanBeSwipedOverFromRestrictedList(struct_0 *a0)
{
    unsigned long v0;  // 4115

    v0 = arm64g_calculate_condition(9, (unsigned long long)(a0->field_50 & 4294967231), 0, 0);
    if (!((char)v0))
    {
        return 0;
    }
    else if (a0->field_b8)
    {
        return 0;
    }
    else
    {
        return 1;
    }
}
```

## `TouchTrackPad.CanSwipeOverOthers` — RVA `0xc58118`

- Decompiled symbol: `TouchTrackPad_CanSwipeOverOthers`
- Metadata signature: `public override bool CanSwipeOverOthers(TouchObject touchObj) { }`
- Native interval: `68` bytes
- Result: `pseudocode`
- Heuristic layout hint: `TouchTrackPad_Recovered` matched 2 offsets against `TouchTrackPad` metadata (confidence 0.67).

```c
typedef struct TouchTrackPad_Recovered {
    char padding_0[40];
    unsigned int field_28;
    char padding_2c[140];
    unsigned long long touchObj;
    unsigned int touchStartType;
} TouchTrackPad_Recovered;

unsigned long long TouchTrackPad_CanSwipeOverOthers(struct_0 *a0, unsigned long a1)
{
    unsigned int v0;  // w8
    unsigned int v1;  // w9

    if (a0->field_b8 != a1)
    {
        return 0;
    }
    else if (a0->field_28 == 1)
    {
        return 1;
    }
    else
    {
        if (a0->field_28 != 2)
            v0 = 0;
        else
            v0 = 1;
        if (a0->field_c0 == 2)
            v1 = 0;
        else
            v1 = 1;
        return v1 & v0;
    }
}
```

## `TouchTrackPad.ReleaseAllTouches` — RVA `0xc5815c`

- Decompiled symbol: `TouchTrackPad_ReleaseAllTouches`
- Metadata signature: `public override void ReleaseAllTouches() { }`
- Native interval: `72` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[184];
    void* field_b8;
} struct_0;

long long TouchTrackPad_ReleaseAllTouches(struct_0 *ptr)
{
    long long v0;  // x0

    if (!ptr->field_b8)
        return 0;
    TouchObject__ReleaseControl(ptr->field_b8, ptr, 1);
    ptr->field_b8 = NULL;
    v0 = sub_f7d8d0();
    return sub_f7d8d0();
}
```

## `TouchTrackPad.OnTouchStart` — RVA `0xc581a4`

- Decompiled symbol: `TouchTrackPad_OnTouchStart`
- Metadata signature: `public override bool OnTouchStart(TouchObject touchObj, TouchControl sender, TouchControl.TouchStartType touchStartType) { }`
- Native interval: `136` bytes
- Result: `pseudocode`

```c
unsigned long long TouchTrackPad_OnTouchStart(void* ptr, unsigned long a1, unsigned long a2, unsigned int a3)
{
    unsigned long long v1;  // x30
    unsigned long v2;  // x0
    unsigned long long v0;  // [bp-0x30]

    v0 = v1;
    if (!(long long)ptr[184])
    {
        *((unsigned long *)&ptr[184]) = a1;
        sub_f7d8d0(ptr + 184);
        v2 = (long long)ptr[184];
        *((unsigned int *)&ptr[192]) = a3;
        if (v2)
        {
            v2 = TouchObject__AddControl(v2, ptr);
            if (a1)
                TouchControl__ScreenToOrientedPos(ptr); /* do not return */
        }
        sub_f7db74(v2);
    }
    else if ((long long)ptr[184])
    {
        return 0;
    }
    else
    {
        return 1;
    }
}
```

## `TouchTrackPad.OnTouchEnd` — RVA `0xc5822c`

- Decompiled symbol: `TouchTrackPad_OnTouchEnd`
- Metadata signature: `public override bool OnTouchEnd(TouchObject touchObj, TouchControl.TouchEndType touchEndType) { }`
- Native interval: `104` bytes
- Result: `pseudocode`

```c
unsigned int TouchTrackPad_OnTouchEnd(unsigned long long *ptr, unsigned long long a1, unsigned int a2)
{
    unsigned int v0;  // w9
    unsigned int v1;  // w8

    if (!ptr[23])
        v0 = 0;
    else
        v0 = 1;
    if (ptr[23] != a1)
        v1 = 0;
    else
        v1 = 1;
    if ((v0 & v1) == 1)
    {
        ptr[23] = 0;
        sub_f7d8d0(ptr + 23, 0);
        if (!ptr[25])
            sub_f7db74(0);
        TouchGestureBasicState__OnTouchEnd();
    }
    return v0 & v1;
}
```

## `TouchTrackPad.OnTouchMove` — RVA `0xc58294`

- Decompiled symbol: `TouchTrackPad_OnTouchMove`
- Metadata signature: `public override bool OnTouchMove(TouchObject touchObj) { }`
- Native interval: `108` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[184];
    unsigned long long field_b8;
} struct_0;

unsigned int TouchTrackPad_OnTouchMove(struct_0 *a0, unsigned long long a1)
{
    unsigned int v0;  // w9
    unsigned int v1;  // w8

    if (!a0->field_b8)
        v0 = 0;
    else
        v0 = 1;
    if (a0->field_b8 != a1)
        v1 = 0;
    else
        v1 = 1;
    if ((v0 & v1) != 1)
        return v0 & v1;
    if (a1)
        TouchControl__ScreenToOrientedPos(a0); /* do not return */
    sub_f7db74();
}
```

## `TouchTrackPad.OnTouchPressureChange` — RVA `0xc58300`

- Decompiled symbol: `TouchTrackPad_OnTouchPressureChange`
- Metadata signature: `public override bool OnTouchPressureChange(TouchObject touchObj) { }`
- Native interval: `76` bytes
- Result: `pseudocode`
- Heuristic layout hint: `TouchTrackPad_Recovered` matched 2 offsets against `TouchTrackPad` metadata (confidence 1.00).

```c
typedef struct TouchTrackPad_Recovered {
    char padding_0[184];
    unsigned long long touchObj;
    char padding_c0[8];
    long long touchState;
} TouchTrackPad_Recovered;

unsigned int TouchTrackPad_OnTouchPressureChange(struct_0 *a0, unsigned long long a1)
{
    unsigned int v0;  // w9
    unsigned int v1;  // w8

    if (!a0->field_b8)
        v0 = 0;
    else
        v0 = 1;
    if (a0->field_b8 != a1)
        v1 = 0;
    else
        v1 = 1;
    if ((v0 & v1) == 1)
    {
        if (a1 && a0->field_c8)
            TouchGestureBasicState__OnTouchPressureChange(a0->field_c8, 0);
        else
            sub_f7db74();
    }
    return v0 & v1;
}
```
