# Native pseudocode: TouchButton

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `TouchButton.ctor` — RVA `0xc4e98c`

- Decompiled symbol: `TouchButton_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `284` bytes
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

extern char g_1fab247;

long long TouchButton_ctor(struct_0 *a0)
{
    unsigned long long v5;  // x30
    unsigned long long v6;  // x22
    unsigned long long v7;  // x21
    unsigned long long v8;  // x20
    unsigned long long v9;  // x19
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
    if (!(g_1fab247 & 1))
    {
        sub_f7d92c("g.");
        sub_f7d92c("y7");
        g_1fab247 = 1;
    }
    DynamicTouchControl__ctor(a0); /* do not return */
}
```

## `TouchButton.Toggled` — RVA `0xc4eae0`

- Decompiled symbol: `TouchButton_Toggled`
- Metadata signature: `public bool Toggled() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[448];
    char field_1c0;
} struct_0;

long long TouchButton_Toggled(struct_0 *a0)
{
    return a0->field_1c0;
}
```

## `TouchButton.JustToggled` — RVA `0xc4eae8`

- Decompiled symbol: `TouchButton_JustToggled`
- Metadata signature: `public bool JustToggled() { }`
- Native interval: `32` bytes
- Result: `pseudocode`

```c
unsigned long long TouchButton_JustToggled(char *a0)
{
    if (!a0[448])
    {
        return 0;
    }
    else if (a0[449])
    {
        return 0;
    }
    else
    {
        return 1;
    }
}
```

## `TouchButton.JustUntoggled` — RVA `0xc4eb08`

- Decompiled symbol: `TouchButton_JustUntoggled`
- Metadata signature: `public bool JustUntoggled() { }`
- Native interval: `32` bytes
- Result: `pseudocode`

```c
unsigned long long TouchButton_JustUntoggled(char *a0)
{
    if (a0[448])
    {
        return 0;
    }
    else if (!a0[449])
    {
        return 0;
    }
    else
    {
        return 1;
    }
}
```

## `TouchButton.PressedOrToggled` — RVA `0xc4eb28`

- Decompiled symbol: `TouchButton_PressedOrToggled`
- Metadata signature: `public bool PressedOrToggled() { }`
- Native interval: `48` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[224];
    struct struct_0 *field_e0;
} struct_1;

typedef struct struct_0 {
    char padding_0[28];
    char field_1c;
} struct_0;

unsigned long long TouchButton_PressedOrToggled(struct_1 *a0)
{
    if (((char)DynamicTouchControl__Pressed(a0) & 1))
    {
        return 1;
    }
    else if (!a0[1].padding_0[216])
    {
        return 0;
    }
    else
    {
        return 1;
    }
}
```

## `TouchButton.OnInitControl` — RVA `0xc4eb58`

- Decompiled symbol: `TouchButton_OnInitControl`
- Metadata signature: `protected override void OnInitControl() { }`
- Native interval: `224` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab248;
extern char g_1fab249;

void TouchButton_OnInitControl(void* ptr)
{
    unsigned long long v4;  // x30
    unsigned long long v5;  // x21
    unsigned long long v6;  // x20
    unsigned long long v7;  // x19
    char v8;  // x0
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x18]
    unsigned long long v2;  // [bp-0x10]
    unsigned long long v3;  // [bp-0x8]

    v0 = v4;
    v1 = v5;
    v2 = v6;
    v3 = v7;
    if (!(g_1fab248 & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab248 = 1;
    }
    DynamicTouchControl__OnInitControl(ptr);
    if ((char)ptr[372] && (char)ptr[392])
    {
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        if (((char)Object__op_Inequality((long long)ptr[88], 0, 0) & 1))
        {
            if ((long long)ptr[88])
            {
                v8 = InputRig__GetSwitchState((long long)ptr[88], (long long)ptr[400], ptr + 408, 0);
                if (!(g_1fab249 & 1))
                {
                    sub_f7d92c(&g_1ef0c58);
                    g_1fab249 = 1;
                }
                *((char *)&ptr[448]) = v8 & 1;
                *((unsigned int *)&ptr[452]) = 0;
            }
            else
            {
                sub_f7db74(0);
            }
        }
    }
    goto *((long long *)(*((long long *)ptr) + 664));
}
```

## `TouchButton.ChangeToggleState` — RVA `0xc4ec38`

- Decompiled symbol: `TouchButton_ChangeToggleState`
- Metadata signature: `private void ChangeToggleState(bool toggleState, bool syncRigSwitch) { }`
- Native interval: `196` bytes
- Result: `pseudocode`
- Heuristic layout hint: `TouchButton_Recovered` matched 4 offsets against `TouchButton` metadata (confidence 0.80).

```c
typedef struct TouchButton_Recovered {
    char padding_0[88];
    struct struct_1 *field_58;
    char padding_60[296];
    char linkToggleToRigSwitch;
    char padding_189[7];
    long long toggleRigSwitchName;
    char padding_198[40];
    char toggledCur;
    char padding_1c1[3];
    unsigned int elapsedSinceToggled;
} TouchButton_Recovered;

typedef struct struct_3 {
    char padding_0[248];
    unsigned long long field_f8;
} struct_3;

typedef struct struct_1 {
    char padding_0[25];
    char field_19;
} struct_1;

typedef struct struct_1 {
    char padding_0[248];
    struct struct_0 *field_f8;
} struct_1;

typedef struct struct_0 {
    char padding_0[32];
    char field_20;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab249;

struct_2 * TouchButton_ChangeToggleState(struct_2 *ptr, unsigned int a1, unsigned int a2)
{
    struct_2 *v0;  // x0
    struct_2 *v1;  // x0
    struct_2 *v2;  // x0
    struct_2 *v3;  // x0
    struct_1 *v4;  // x0

    v0 = ptr;
    if (!(g_1fab249 & 1))
    {
        v1 = sub_f7d92c(&g_1ef0c58);
        g_1fab249 = 1;
        v0 = v1;
    }
    v2 = v0;
    ptr->field_1c0 = (char)a1 & 1;
    ptr->field_1c4 = 0;
    if (!((char)a2 & 1))
    {
        return v2;
    }
    else if (ptr->field_188)
    {
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        v3 = Object__op_Inequality(ptr->field_58, 0, 0);
        if (!((char)v3 & 1))
            return v3;
        if (ptr->field_58 && ptr->field_58->field_f8)
        {
            v4 = InputRig_RigSwitchCollection__SetSwitchState(ptr->field_58->field_f8, ptr->field_190, &ptr->padding_198, a1 & 1);
            return InputRig_RigSwitchCollection__SetSwitchState(ptr->field_58->field_f8, ptr->field_190, &ptr->padding_198, a1 & 1);
        }
        sub_f7db74();
    }
    else
    {
        return v2;
    }
}
```

## `TouchButton.ResetControl` — RVA `0xc4ecfc`

- Decompiled symbol: `TouchButton_ResetControl`
- Metadata signature: `public override void ResetControl() { }`
- Native interval: `104` bytes
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

void TouchButton_ResetControl(struct_0 *a0)
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

## `TouchButton.OnUpdateControl` — RVA `0xc4ed64`

- Decompiled symbol: `TouchButton_OnUpdateControl`
- Metadata signature: `protected override void OnUpdateControl() { }`
- Native interval: `460` bytes
- Result: `pseudocode`
- Heuristic layout hint: `TouchButton_Recovered` matched 11 offsets against `TouchButton` metadata (confidence 0.79).

```c
typedef struct struct_3 {
    char padding_0[28];
    char field_1c;
} struct_3;

typedef struct TouchButton_Recovered {
    char padding_0[80];
    unsigned int field_50;
    char padding_54[4];
    struct struct_1 *field_58;
    char padding_60[128];
    struct struct_0 *field_e0;
    char padding_e8[140];
    char toggle;
    char padding_175[3];
    unsigned int toggleOnAction;
    unsigned int toggleOffAction;
    char padding_180[1];
    char autoToggleOff;
    char padding_182[2];
    unsigned int autoToggleOffTimeOut;
    char linkToggleToRigSwitch;
    char padding_189[7];
    long long toggleRigSwitchName;
    char padding_198[40];
    char toggledCur;
    char toggledPrev;
    char curTouchToggledOn;
    char padding_1c3[1];
    unsigned int elapsedSinceToggled;
} TouchButton_Recovered;

typedef struct struct_1 {
    char padding_0[248];
    struct struct_0 *field_f8;
} struct_1;

typedef struct struct_0 {
    char padding_0[28];
    char field_1c;
} struct_0;

extern long long g_1ef0c58;
extern char g_1fab249;

struct_3 * TouchButton_OnUpdateControl(struct_2 *ptr, unsigned long a1, unsigned long long a2, unsigned int a3)
{
    struct_3 *v0;  // x0
    unsigned int v1;  // w8
    unsigned long v10;  // 4146
    unsigned long v11;  // 4115
    unsigned long long v12;  // x0
    unsigned int v2;  // w9
    unsigned int flag;  // w8
    unsigned int v4;  // w8
    unsigned int v5;  // w1
    unsigned int v6;  // w20
    unsigned int v7;  // s1
    unsigned int v8;  // s0
    unsigned int v9;  // s0

    v0 = (unsigned long long)DynamicTouchControl__OnUpdateControl(ptr, 0, a2, a3);
    v1 = ptr->field_1c0;
    v2 = ptr->field_174;
    ptr->field_1c1 = v1;
    if (!v2)
    {
        ptr->field_1c0 = 0;
        goto LABEL_104eefc;
    }
    if (v1)
        flag = ptr->field_17c;
    else
        flag = ptr->field_178;
    if (flag != 1)
    {
        if (!flag)
        {
            v0 = ptr->field_e0;
            if (!v0)
                sub_f7db74(v0);
            v0 = TouchGestureBasicState__JustPressedRaw(v0, 0);
            if (((char)v0 & 1))
            {
                v4 = 1;
                ptr->field_1c2 = 1;
                goto LABEL_104edfc;
            }
        }
    }
    else
    {
        if (!ptr->field_1c2)
        {
            v0 = ptr->field_e0;
            if (!v0)
                sub_f7db74(v0);
            v0 = TouchGestureBasicState__JustReleasedRaw(v0, 0);
            if (((char)v0 & 1))
            {
                v4 = 1;
                ptr->field_1c2 = 0;
                goto LABEL_104edfc;
            }
        }
    }
    v4 = 0;
LABEL_104edfc:
    if (!ptr->field_e0)
        sub_f7db74(v0);
    if (!ptr->field_e0->field_1c)
    {
        ptr->field_1c2 = 0;
        if (!v4)
        {
LABEL_104ee34:
            if (ptr->field_174 && ptr->field_188)
            {
                if (!ptr->field_58)
                    sub_f7db74(v0);
                v0 = ptr->field_58->field_f8;
                if (!v0)
                    sub_f7db74(v0);
                v0 = InputRig_RigSwitchCollection__GetSwitchState(v0, ptr->field_190, &ptr->padding_198, ptr->field_1c0);
                v6 = (unsigned int)v0 & 1;
                if (!(g_1fab249 & 1))
                {
                    v0 = sub_f7d92c(&g_1ef0c58);
                    g_1fab249 = 1;
                }
                ptr->field_1c0 = v6;
                ptr->field_1c4 = 0;
                if (v6)
                    goto LABEL_104eea4;
            }
            else
            {
LABEL_104ee9c:
                if (ptr->field_1c0)
                {
LABEL_104eea4:
                    if (ptr->field_181 || ptr->field_17c == 2)
                    {
                        v0 = DynamicTouchControl__Pressed(ptr);
                        if (((char)v0 & 1))
                        {
                            ptr->field_1c4 = 0;
                        }
                        else
                        {
                            v0 = CFUtils__get_realDeltaTime();
                            v7 = ptr->field_184;
                            v9 = ptr->field_1c4 + v8;
                            ptr->field_1c4 = v9;
                            v10 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v9, v7)) >> 5 & 3 | (unsigned long long)(CmpF(v9, v7) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v9, v7)) >> 5 & 3 | (unsigned long long)(CmpF(v9, v7) & 1)) & ((unsigned long long)(char)(CmpF(v9, v7)) >> 5 & 3 | (unsigned long long)(CmpF(v9, v7) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                            if (!((char)v10))
                                v0 = TouchButton__ChangeToggleState(ptr, 0, 1);
                        }
                    }
                }
            }
LABEL_104eefc:
            v11 = arm64g_calculate_condition(9, (unsigned long long)(ptr->field_50 & 4294967231), 0, 0);
            if ((char)v11)
            {
                v12 = TouchButton__SyncRigState(ptr);
                return TouchButton__SyncRigState(ptr);
            }
            return v0;
        }
    }
    else if (!v4)
    {
        goto LABEL_104ee34;
    }
    if (ptr->field_1c0)
        v5 = 0;
    else
        v5 = 1;
    v0 = TouchButton__ChangeToggleState(ptr, v5, 1);
    goto LABEL_104ee9c;
}
```

## `TouchButton.SyncRigState` — RVA `0xc4ef40`

- Decompiled symbol: `TouchButton_SyncRigState`
- Metadata signature: `private void SyncRigState() { }`
- Native interval: `204` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[224];
    struct struct_0 *field_e0;
} struct_1;

typedef struct struct_0 {
    char padding_0[28];
    char field_1c;
} struct_0;

long long TouchButton_SyncRigState(struct_1 *ptr, unsigned long a1, unsigned long a2, unsigned long a3)
{
    unsigned long v0;  // x0
    unsigned long v1;  // x0
    unsigned long v2;  // x0
    unsigned long long v3;  // x0

    if (((char)DynamicTouchControl__Pressed(ptr) & 1) || ptr[1].padding_0[216])
    {
        if (*((long long *)&ptr[1].padding_0[184]))
            DigitalBinding__Sync();
        else
            sub_f7db74(*((long long *)&ptr[1].padding_0[184]));
    }
    v0 = *((long long *)&ptr[1].padding_0[192]);
    if (*((long long *)&ptr[1].padding_0[192]))
    {
        DigitalBinding__Sync();
        v1 = DynamicTouchControl__Pressed(ptr);
        if (!((char)v1 & 1))
            return v1;
        v2 = DynamicTouchControl__IsTouchPressureSensitive(ptr);
        if (((char)v2 & 1))
        {
            v0 = DynamicTouchControl__GetTouchPressure(ptr);
            if (*((long long *)&ptr[1].padding_0[208]))
            {
                v3 = AxisBinding__SyncFloat();
                return AxisBinding__SyncFloat();
            }
        }
        else if (ptr[1].padding_0[200])
        {
            v0 = *((long long *)&ptr[1].padding_0[208]);
            if (*((long long *)&ptr[1].padding_0[208]))
            {
                v3 = AxisBinding__SyncFloat();
                return AxisBinding__SyncFloat();
            }
        }
        else
        {
            return v2;
        }
    }
    sub_f7db74(v0);
}
```

## `TouchButton.OnGetSubBindingDescriptions` — RVA `0xc4f250`

- Decompiled symbol: `TouchButton_OnGetSubBindingDescriptions`
- Metadata signature: `protected override void OnGetSubBindingDescriptions(BindingDescriptionList descList, Object undoObject, string parentMenuPath) { }`
- Native interval: `244` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[416];
    long long field_1a0;
} struct_0;

extern long long g_1f0d040;
extern long long g_1f0edd8;
extern char g_1fab24a;

long long TouchButton_OnGetSubBindingDescriptions(struct_0 *a0, long long a1, unsigned long a2, long long a3)
{
    unsigned long long v5;  // x30
    unsigned long long v6;  // x22
    unsigned long long v7;  // x21
    unsigned long long v8;  // x20
    unsigned long long v9;  // x19
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
    if (!(g_1fab24a & 1))
    {
        sub_f7d92c(&g_1f0d040);
        sub_f7d92c("+#");
        sub_f7d92c(&g_1f0edd8);
        g_1fab24a = 1;
    }
    if (a1)
        BindingDescriptionList__Add(a1, a0->field_1a0, g_1f0d040, a3, a0, 0); /* do not return */
    sub_f7db74();
}
```

## `TouchButton.OnIsBoundToAxis` — RVA `0xc4f344`

- Decompiled symbol: `TouchButton_OnIsBoundToAxis`
- Metadata signature: `protected override bool OnIsBoundToAxis(string axisName, InputRig rig) { }`
- Native interval: `120` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[416];
    long long field_1a0;
} struct_0;

long long TouchButton_OnIsBoundToAxis(struct_0 *a0, unsigned long a1, unsigned long a2)
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
    if (a0->field_1a0)
        InputBindingBase__IsBoundToAxis(a0->field_1a0); /* do not return */
    sub_f7db74(0);
}
```

## `TouchButton.OnIsBoundToKey` — RVA `0xc4f3bc`

- Decompiled symbol: `TouchButton_OnIsBoundToKey`
- Metadata signature: `protected override bool OnIsBoundToKey(KeyCode key, InputRig rig) { }`
- Native interval: `120` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[416];
    long long field_1a0;
} struct_0;

long long TouchButton_OnIsBoundToKey(struct_0 *a0, unsigned long a1, unsigned long a2)
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
    if (a0->field_1a0)
        InputBindingBase__IsBoundToKey(a0->field_1a0); /* do not return */
    sub_f7db74(0);
}
```

## `TouchButton.ReleaseAllTouches` — RVA `0xc4f434`

- Decompiled symbol: `TouchButton_ReleaseAllTouches`
- Metadata signature: `public override void ReleaseAllTouches() { }`
- Native interval: `36` bytes
- Result: `pseudocode`
- Heuristic layout hint: `TouchButton_Recovered` matched 4 offsets against `TouchButton` metadata (confidence 0.80).

```c
typedef struct TouchButton_Recovered {
    char padding_0[88];
    struct struct_1 *field_58;
    char padding_60[296];
    char linkToggleToRigSwitch;
    char padding_189[7];
    long long toggleRigSwitchName;
    char padding_198[40];
    char toggledCur;
    char padding_1c1[3];
    unsigned int elapsedSinceToggled;
} TouchButton_Recovered;

typedef struct struct_0 {
    char padding_0[384];
    char field_180;
} struct_0;

typedef struct struct_1 {
    char padding_0[248];
    struct struct_0 *field_f8;
} struct_1;

typedef struct struct_0 {
    char padding_0[32];
    char field_20;
} struct_0;

struct_2 * TouchButton_ReleaseAllTouches(struct_0 *a0)
{
    struct_2 *v0;  // x0

    DynamicTouchControl__ReleaseAllTouches(a0);
    v0 = TouchButton__ChangeToggleState(a0, 0, a0->field_180);
    return TouchButton__ChangeToggleState(a0, 0, a0->field_180);
}
```
