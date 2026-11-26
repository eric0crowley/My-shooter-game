# Native pseudocode: TouchJoystick

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `TouchJoystick.ctor` — RVA `0xc55840`

- Decompiled symbol: `TouchJoystick_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `396` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[136];
    char field_88;
    char padding_89[7];
    unsigned long long field_90;
    unsigned int field_98;
    unsigned short field_9c;
    char padding_9e[2];
    unsigned short field_a0;
    char padding_a2[22];
    unsigned int field_b8;
} struct_0;

extern long long g_1ef0548;
extern long long g_1ef0550;
extern long long g_1ef0558;
extern char g_1fab27c;

long long TouchJoystick_ctor(struct_0 *a0)
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
    if (!(g_1fab27c & 1))
    {
        sub_f7d92c("g.");
        sub_f7d92c("y7");
        sub_f7d92c(&g_1ef0548);
        sub_f7d92c(&g_1ef0558);
        sub_f7d92c(&g_1ef0550);
        g_1fab27c = 1;
    }
    DynamicTouchControl__ctor(a0); /* do not return */
}
```

## `TouchJoystick.OnInitControl` — RVA `0xc559cc`

- Decompiled symbol: `TouchJoystick_OnInitControl`
- Metadata signature: `protected override void OnInitControl() { }`
- Native interval: `40` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[664];
    unsigned long long field_298;
} struct_0;

void TouchJoystick_OnInitControl(struct_0 **a0)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    DynamicTouchControl__OnInitControl(a0);
    goto *(a0)->field_298;
}
```

## `TouchJoystick.GetVector` — RVA `0xc559f4`

- Decompiled symbol: `TouchJoystick_GetVector`
- Metadata signature: `public Vector2 GetVector() { }`
- Native interval: `28` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[384];
    unsigned long long field_180;
} struct_0;

void TouchJoystick_GetVector(struct_0 *a0)
{
    if (a0->field_180)
        return;
    sub_f7db74();
}
```

## `TouchJoystick.GetVectorRaw` — RVA `0xc55a10`

- Decompiled symbol: `TouchJoystick_GetVectorRaw`
- Metadata signature: `public Vector2 GetVectorRaw() { }`
- Native interval: `28` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[384];
    unsigned long long field_180;
} struct_0;

void TouchJoystick_GetVectorRaw(struct_0 *a0)
{
    if (a0->field_180)
        return;
    sub_f7db74();
}
```

## `TouchJoystick.GetDir` — RVA `0xc55a2c`

- Decompiled symbol: `TouchJoystick_GetDir`
- Metadata signature: `public Dir GetDir() { }`
- Native interval: `28` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[384];
    long long field_180;
} struct_0;

long long TouchJoystick_GetDir(struct_0 *a0)
{
    unsigned long long v0;  // x0

    if (a0->field_180)
    {
        v0 = JoystickState__GetDir(a0->field_180, 0);
        return JoystickState__GetDir(a0->field_180, 0);
    }
    sub_f7db74(0);
}
```

## `TouchJoystick.GetState` — RVA `0xc55a48`

- Decompiled symbol: `TouchJoystick_GetState`
- Metadata signature: `public JoystickState GetState() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[384];
    unsigned long long field_180;
} struct_0;

long long TouchJoystick_GetState(struct_0 *a0)
{
    return a0->field_180;
}
```

## `TouchJoystick.ResetControl` — RVA `0xc55a50`

- Decompiled symbol: `TouchJoystick_ResetControl`
- Metadata signature: `public override void ResetControl() { }`
- Native interval: `120` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[136];
    char field_88;
    char padding_89[143];
    char field_118;
    char field_119;
    char field_11a;
    char padding_11b[5];
    unsigned int field_120;
    char padding_124[4];
    unsigned int field_128;
    unsigned int field_12c;
    unsigned int field_130;
} struct_0;

void TouchJoystick_ResetControl(struct_0 *a0)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    struct_0 *v4;  // x0
    unsigned long v5;  // x1
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    DynamicTouchControl__ResetControl(a0);
    v4 = a0;
    v5 = *((long long *)(*((long long *)&a0->padding_0[0]) + 688));
    (*((long long *)(*((long long *)&a0->padding_0[0]) + 680)))();
}
```

## `TouchJoystick.OnUpdateControl` — RVA `0xc55ac8`

- Decompiled symbol: `TouchJoystick_OnUpdateControl`
- Metadata signature: `protected override void OnUpdateControl() { }`
- Native interval: `168` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[28];
    char field_1c;
} struct_1;

extern char g_1055b70;

unsigned long long TouchJoystick_OnUpdateControl(void* a0, unsigned long a1, unsigned long long a2, unsigned int a3)
{
    void* v3;  // x19
    unsigned long long v4;  // x0
    unsigned long long v13;  // x0
    unsigned long v5;  // 4115
    void* v6;  // x19
    void* v7;  // x0
    void* ptr;  // x19
    unsigned long v10;  // x0
    unsigned long v11;  // x2
    unsigned long long v12;  // x1
    unsigned long v0;  // [bp-0x20]
    void* v2;  // [bp-0x8]

    v3 = a0;
    DynamicTouchControl__OnUpdateControl(a0, 0, a2, a3);
    if ((long long)v3[224])
    {
        if (*((char *)((long long)v3[224] + 28)))
        {
            DynamicTouchControl__GetOriginOffset(v3);
            TouchControl__WorldToNormalizedPos(v3); /* do not return */
        }
        if (!(long long)v3[384])
            goto LABEL_1055b6c;
        v4 = JoystickState__Update((long long)v3[384], 0);
        v5 = arm64g_calculate_condition(9, (unsigned long long)((int)v3[80] & 4294967231), 0, 0);
        if (!((char)v5))
            return v4;
        v6 = v2;
        v7 = v3;
    }
    else
    {
LABEL_1055b6c:
        vvar_98{r256|8b} = (int)&g_1055b70;
        v6 = v3;
        v7 = sub_f7db74();
    }
    v0 = vvar_71{r256|8b};
    v2 = v6;
    ptr = v7;
    if (((char)DynamicTouchControl__Pressed(v7) & 1))
    {
        v10 = (long long)ptr[392];
        if (v10)
        {
            DigitalBinding__Sync(v10, 1, (long long)ptr[88], 0);
            if (((char)DynamicTouchControl__IsTouchPressureSensitive(ptr) & 1))
            {
                v10 = (long long)ptr[416];
                v10 = DynamicTouchControl__GetTouchPressure(ptr);
                if ((long long)ptr[416])
                {
                    v11 = (long long)ptr[88];
                    v12 = 1;
                    goto LABEL_1055bf0;
                }
            }
            else
            {
                if (!(char)ptr[408])
                    goto LABEL_1055bf4;
                v10 = (long long)ptr[416];
                if (v10)
                {
                    v11 = (long long)ptr[88];
                    v12 = 0;
LABEL_1055bf0:
                    AxisBinding__SyncFloat(v10, v12, v11);
                    goto LABEL_1055bf4;
                }
            }
        }
    }
    else
    {
LABEL_1055bf4:
        v10 = (long long)ptr[400];
        if (v10)
        {
            v13 = JoystickStateBinding__SyncJoyState(v10, (long long)ptr[384], (long long)ptr[88], 0);
            return JoystickStateBinding__SyncJoyState(v10, (long long)ptr[384], (long long)ptr[88], 0);
        }
    }
    sub_f7db74(v10);
}
```

## `TouchJoystick.SyncRigState` — RVA `0xc55b70`

- Decompiled symbol: `TouchJoystick_SyncRigState`
- Metadata signature: `private void SyncRigState() { }`
- Native interval: `168` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: CFGFast did not recover a function at the metadata RVA

```c
// 0x1055b70: str x30, [sp, #-0x20]!
// 0x1055b74: stp x20, x19, [sp, #0x10]
// 0x1055b78: mov x1, xzr
// 0x1055b7c: mov x19, x0
// 0x1055b80: bl #0x1044b14
// 0x1055b84: tbz w0, #0, #0x1055bf4
// 0x1055b88: ldr x0, [x19, #0x188]
// 0x1055b8c: cbz x0, #0x1055c14
// 0x1055b90: ldr x2, [x19, #0x58]
// 0x1055b94: mov w1, #1
// 0x1055b98: mov w3, wzr
// 0x1055b9c: bl #0x104f00c
// 0x1055ba0: mov x0, x19
// 0x1055ba4: mov x1, xzr
// 0x1055ba8: bl #0x1047cb0
// 0x1055bac: tbz w0, #0, #0x1055bd4
// 0x1055bb0: ldr x20, [x19, #0x1a0]
// 0x1055bb4: mov x0, x19
// 0x1055bb8: mov x1, xzr
// 0x1055bbc: bl #0x1047ce0
// 0x1055bc0: cbz x20, #0x1055c14
// 0x1055bc4: ldr x2, [x19, #0x58]
// 0x1055bc8: mov w1, #1
// 0x1055bcc: mov x0, x20
// 0x1055bd0: b #0x1055bf0
// 0x1055bd4: ldrb w8, [x19, #0x198]
// 0x1055bd8: cbz w8, #0x1055bf4
// 0x1055bdc: ldr x0, [x19, #0x1a0]
// 0x1055be0: cbz x0, #0x1055c14
// 0x1055be4: ldr x2, [x19, #0x58]
// 0x1055be8: fmov s0, #1.00000000
// 0x1055bec: mov w1, wzr
// 0x1055bf0: bl #0x104f160
// 0x1055bf4: ldr x0, [x19, #0x190]
// 0x1055bf8: cbz x0, #0x1055c14
// 0x1055bfc: ldr x2, [x19, #0x58]
// 0x1055c00: ldr x1, [x19, #0x180]
// 0x1055c04: ldp x20, x19, [sp, #0x10]
// 0x1055c08: mov x3, xzr
// 0x1055c0c: ldr x30, [sp], #0x20
// 0x1055c10: b #0x105dffc
// 0x1055c14: bl #0xf7db74
```

## `TouchJoystick.OnIsBoundToAxis` — RVA `0xc55c18`

- Decompiled symbol: `TouchJoystick_OnIsBoundToAxis`
- Metadata signature: `protected override bool OnIsBoundToAxis(string axisName, InputRig rig) { }`
- Native interval: `120` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[392];
    long long field_188;
} struct_0;

long long TouchJoystick_OnIsBoundToAxis(struct_0 *a0, unsigned long a1, unsigned long a2)
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
    if (a0->field_188)
        InputBindingBase__IsBoundToAxis(a0->field_188); /* do not return */
    sub_f7db74(0);
}
```

## `TouchJoystick.OnIsBoundToKey` — RVA `0xc55c90`

- Decompiled symbol: `TouchJoystick_OnIsBoundToKey`
- Metadata signature: `protected override bool OnIsBoundToKey(KeyCode key, InputRig rig) { }`
- Native interval: `120` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[392];
    long long field_188;
} struct_0;

long long TouchJoystick_OnIsBoundToKey(struct_0 *a0, unsigned long a1, unsigned long a2, unsigned long a3)
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
    if (a0->field_188)
        InputBindingBase__IsBoundToKey(a0->field_188); /* do not return */
    sub_f7db74(0);
}
```

## `TouchJoystick.OnGetSubBindingDescriptions` — RVA `0xc55d08`

- Decompiled symbol: `TouchJoystick_OnGetSubBindingDescriptions`
- Metadata signature: `protected override void OnGetSubBindingDescriptions(BindingDescriptionList descList, Object undoObject, string parentMenuPath) { }`
- Native interval: `212` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[392];
    long long field_188;
} struct_0;

extern long long g_1f0ba70;
extern long long g_1f0d040;
extern char g_1fab27d;

long long TouchJoystick_OnGetSubBindingDescriptions(struct_0 *a0, long long a1, unsigned long a2, long long a3)
{
    unsigned long long v6;  // x30
    unsigned long long v7;  // x23
    unsigned long long v8;  // x22
    unsigned long long v9;  // x21
    unsigned long long v10;  // x20
    unsigned long long v11;  // x19
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
    if (!(g_1fab27d & 1))
    {
        sub_f7d92c(&g_1f0ba70);
        sub_f7d92c(&g_1f0d040);
        sub_f7d92c("+#");
        g_1fab27d = 1;
    }
    if (a1)
        BindingDescriptionList__Add(a1, a0->field_188, g_1f0d040, a3, a0, 0); /* do not return */
    sub_f7db74();
}
```

## `TouchJoystick.IsUsingKeyForEmulation` — RVA `0xc55ddc`

- Decompiled symbol: `TouchJoystick_IsUsingKeyForEmulation`
- Metadata signature: `public override bool IsUsingKeyForEmulation(KeyCode key) { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
unsigned int TouchJoystick_IsUsingKeyForEmulation(void)
{
    return 0;
}
```
