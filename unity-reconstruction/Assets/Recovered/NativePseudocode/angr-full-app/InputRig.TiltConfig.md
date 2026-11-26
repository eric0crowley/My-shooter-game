# Native pseudocode: InputRig.TiltConfig

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `InputRig.TiltConfig.ctor` — RVA `0xc427e0`

- Decompiled symbol: `InputRig_TiltConfig_ctor`
- Metadata signature: `public void .ctor(InputRig rig) { }`
- Native interval: `688` bytes
- Result: `pseudocode`
- Heuristic layout hint: `InputRig_TiltConfig_Recovered` matched 7 offsets against `InputRig.TiltConfig` metadata (confidence 1.00).

```c
typedef struct InputRig_TiltConfig_Recovered {
    char padding_0[16];
    long long rig;
    long long tiltState;
    char padding_20[16];
    struct struct_2 *disablingConditions;
    struct struct_3 *rollAnalogConfig;
    struct struct_4 *pitchAnalogConfig;
    long long rollBinding;
    long long pitchBinding;
} InputRig_TiltConfig_Recovered;

typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

typedef struct struct_1 {
    char padding_0[16];
    unsigned int field_10;
} struct_1;

typedef struct struct_4 {
    char padding_0[16];
    unsigned int field_10;
} struct_4;

typedef struct struct_6 {
    char padding_0[16];
    unsigned int field_10;
    unsigned short field_14;
} struct_6;

typedef struct struct_2 {
    char padding_0[16];
    unsigned int field_10;
    unsigned short field_14;
} struct_2;

typedef struct struct_3 {
    char padding_0[16];
    unsigned int field_10;
} struct_3;

extern long long g_1eee758;
extern long long g_1eef5c0;
extern long long g_1f0ab18;
extern long long g_1f0f998;
extern char g_1fab20a;

long long InputRig_TiltConfig_ctor(struct_5 *a0, long long a1)
{
    unsigned long long v6;  // x30
    unsigned long long v7;  // x23
    struct_5 *addr;  // x22
    struct_5 *v17;  // x22
    struct_1 *v18;  // x23
    struct_5 *ptr3;  // x21
    struct_5 *v20;  // x21
    struct_6 *v21;  // x21
    struct_5 *ptr4;  // x20
    struct_5 *p;  // x20
    struct_6 *ptr;  // x8
    long long v25;  // x20
    unsigned long long v8;  // x22
    struct_5 *ptr5;  // x0
    long long v27;  // x20
    struct_5 *ptr6;  // x0
    unsigned long long v9;  // x21
    unsigned long long v10;  // x20
    unsigned long long v11;  // x19
    struct_5 *ptr7;  // x0
    long long v13;  // x21
    struct_5 *ptr8;  // x0
    struct_0 *v15;  // x21
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
    if (!(g_1fab20a & 1))
    {
        sub_f7d92c(&g_1eee758);
        sub_f7d92c("g.");
        sub_f7d92c("y7");
        sub_f7d92c(&g_1eef5c0);
        sub_f7d92c("OX");
        sub_f7d92c(&g_1f0f998);
        sub_f7d92c(&g_1f0ab18);
        g_1fab20a = 1;
    }
    Object__ctor(a0, 0);
    ptr7 = a0;
    ptr7->field_10 = a1;
    sub_f7d8d0((struct InputRig_TiltConfig_Recovered *)&ptr7->field_10, a1);
    v13 = sub_f7db70(g_1ef1d50);
    TiltState__ctor(v13, 0);
    ptr8 = a0;
    ptr8->field_18 = v13;
    sub_f7d8d0((struct InputRig_TiltConfig_Recovered *)&ptr8->field_18, v13);
    v15 = sub_f7db70(g_1eee758);
    AnalogConfig__ctor(v15, 0);
    addr = a0;
    addr->field_38 = v15;
    v17 = &addr->field_38;
    sub_f7d8d0(v17, v15);
    v18 = sub_f7db70(g_1eee758);
    AnalogConfig__ctor(v18, 0);
    ptr3 = a0;
    ptr3->field_40 = v18;
    v20 = &ptr3->field_40;
    sub_f7d8d0(v20, v18);
    if (*((long long *)&v17->padding_0[0]))
    {
        *((unsigned int *)(*((long long *)&v17->padding_0[0]) + 16)) = 1050253722;
        if (*((long long *)&v20->padding_0[0]))
        {
            *((unsigned int *)(*((long long *)&v20->padding_0[0]) + 16)) = 1050253722;
            v21 = sub_f7db70(g_1eef5c0);
            DisablingConditionSet__ctor(v21, a1, 0);
            ptr4 = a0;
            ptr4->field_30 = v21;
            p = &ptr4->field_30;
            sub_f7d8d0(p, v21);
            ptr = *((long long *)&p->padding_0[0]);
            if (ptr)
            {
                ptr->field_14 = 0;
                ptr->field_10 = 0;
                v25 = sub_f7db70(g_1eee9f8);
                AxisBinding__ctor(v25, g_1f0ab18, 0, 0, 0);
                ptr5 = a0;
                ptr5->field_48 = v25;
                sub_f7d8d0((struct InputRig_TiltConfig_Recovered *)&ptr5->field_48, v25);
                v27 = sub_f7db70(g_1eee9f8);
                AxisBinding__ctor(v27, g_1f0f998, 0, 0, 0);
                ptr6 = a0;
                ptr6->field_50 = v27;
                sub_f7d8d0((struct InputRig_TiltConfig_Recovered *)&ptr6->field_50, v27);
                DigitalBinding__ctor(sub_f7db70(g_1eef590), 0, 0); /* do not return */
            }
        }
    }
    sub_f7db74();
}
```

## `InputRig.TiltConfig.Reset` — RVA `0xc42a90`

- Decompiled symbol: `InputRig_TiltConfig_Reset`
- Metadata signature: `public void Reset() { }`
- Native interval: `44` bytes
- Result: `pseudocode`
- Heuristic layout hint: `InputRig_TiltConfig_Recovered` matched 2 offsets against `InputRig.TiltConfig` metadata (confidence 1.00).

```c
typedef struct InputRig_TiltConfig_Recovered {
    char padding_0[24];
    long long tiltState;
    unsigned long long digitalRollDirection;
} InputRig_TiltConfig_Recovered;

long long InputRig_TiltConfig_Reset(struct_0 *ptr)
{
    long long v0;  // x0
    unsigned long v1;  // x0

    v0 = ptr->field_18;
    ptr->field_20 = 0;
    if (v0)
    {
        TiltState__Reset(v0, 0);
        v1 = InputRig_TiltConfig__OnDisablingConditionsChange(ptr);
        return InputRig_TiltConfig__OnDisablingConditionsChange(ptr);
    }
    sub_f7db74(0);
}
```

## `InputRig.TiltConfig.OnDisablingConditionsChange` — RVA `0xc42abc`

- Decompiled symbol: `InputRig_TiltConfig_OnDisablingConditionsChange`
- Metadata signature: `public void OnDisablingConditionsChange() { }`
- Native interval: `44` bytes
- Result: `pseudocode`
- Heuristic layout hint: `InputRig_TiltConfig_Recovered` matched 2 offsets against `InputRig.TiltConfig` metadata (confidence 1.00).

```c
typedef struct InputRig_TiltConfig_Recovered {
    char padding_0[40];
    char disabledByRigSwitches;
    char padding_29[7];
    long long disablingConditions;
} InputRig_TiltConfig_Recovered;

unsigned long long InputRig_TiltConfig_OnDisablingConditionsChange(struct_0 *ptr)
{
    unsigned long long v0;  // x0

    if (ptr->field_30)
    {
        v0 = DisablingConditionSet__IsInEffect(ptr->field_30, 0);
        ptr->field_28 = (char)v0 & 1;
        return v0;
    }
    sub_f7db74(0);
}
```

## `InputRig.TiltConfig.IsEnabled` — RVA `0xc42ae8`

- Decompiled symbol: `InputRig_TiltConfig_IsEnabled`
- Metadata signature: `public bool IsEnabled() { }`
- Native interval: `16` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[40];
    char field_28;
} struct_0;

unsigned long long InputRig_TiltConfig_IsEnabled(struct_0 *a0)
{
    if (!a0->field_28)
        return 1;
    return 0;
}
```

## `InputRig.TiltConfig.Update` — RVA `0xc42af8`

- Decompiled symbol: `InputRig_TiltConfig_Update`
- Metadata signature: `public void Update() { }`
- Native interval: `388` bytes
- Result: `pseudocode`
- Heuristic layout hint: `InputRig_TiltConfig_Recovered` matched 9 offsets against `InputRig.TiltConfig` metadata (confidence 0.90).

```c
typedef struct InputRig_TiltConfig_Recovered {
    long long field_0;
    char padding_8[8];
    long long rig;
    long long tiltState;
    int digitalRollDirection;
    int digitalPitchDirection;
    char disabledByRigSwitches;
    char padding_29[15];
    long long rollAnalogConfig;
    long long pitchAnalogConfig;
    struct struct_0 *rollBinding;
    struct struct_1 *pitchBinding;
} InputRig_TiltConfig_Recovered;

typedef struct struct_0 {
    char padding_0[16];
    char field_10;
} struct_0;

typedef struct struct_1 {
    char padding_0[16];
    char field_10;
} struct_1;

unsigned long long InputRig_TiltConfig_Update(struct_2 *ptr)
{
    unsigned int v0;  // w0
    long long v1;  // x8
    unsigned long long v2;  // x0
    unsigned int v3;  // w8
    struct_0 *v4;  // x20
    struct_1 *v5;  // x20
    unsigned long long v6;  // x8
    unsigned long long v7;  // x8
    unsigned long long v8;  // x0

    Input__get_acceleration(0);
    if (ptr->field_18 && (TiltState__InternalApplyVector(ptr->field_18, 0), ptr->field_18 && (TiltState__Update(ptr->field_18, 0), ptr->field_18 && ptr->field_38 && (v0 = (unsigned int)(unsigned long long)AnalogConfig__GetSignedDigitalVal(ptr->field_38, (unsigned long long)(unsigned int)ptr->field_20, 0), v1 = ptr->field_40, ptr->field_20 = (int)(unsigned int)(unsigned long long)AnalogConfig__GetSignedDigitalVal(ptr->field_38, (unsigned long long)(unsigned int)ptr->field_20, 0), v1))))
    {
        v2 = AnalogConfig__GetSignedDigitalVal(v1, ptr->field_24, 0);
        v3 = ptr->field_28;
        ptr->field_24 = v2;
        if (v3)
            return v2;
        v4 = ptr->field_48;
        if (v4)
        {
            if (!v4->field_10)
            {
LABEL_1042bcc:
                v5 = ptr->field_50;
                if (v5)
                {
                    if (v5->field_10)
                    {
                        if (ptr->field_40)
                        {
                            AnalogConfig__GetAnalogVal(ptr->field_40, 0);
                            v2 = AxisBinding__SyncFloat(v5, 1, ptr->field_10, 0);
                            goto LABEL_1042c04;
                        }
                    }
                    else
                    {
LABEL_1042c04:
                        if (ptr->field_20)
                        {
                            v6 = 96;
                            if (ptr->field_20 < 0)
                                v6 = 88;
                            if (*((long long *)((char *)ptr + v6)))
                            {
                                v2 = DigitalBinding__Sync(*((long long *)((char *)ptr + v6)), 1, ptr->field_10, 0, 0);
                                goto LABEL_1042c38;
                            }
                        }
                        else
                        {
LABEL_1042c38:
                            if (!ptr->field_24)
                                return v2;
                            v7 = 104;
                            if (ptr->field_24 < 0)
                                v7 = 112;
                            if (*((long long *)((char *)ptr + v7)))
                            {
                                v8 = DigitalBinding__Sync();
                                return DigitalBinding__Sync();
                            }
                        }
                    }
                }
            }
            else if (ptr->field_38)
            {
                AnalogConfig__GetAnalogVal(ptr->field_38, 0);
                v2 = AxisBinding__SyncFloat(v4, 1, ptr->field_10, 0);
                goto LABEL_1042bcc;
            }
        }
    }
    sub_f7db74();
}
```

## `InputRig.TiltConfig.IsBoundToAxis` — RVA `0xc42c7c`

- Decompiled symbol: `InputRig_TiltConfig_IsBoundToAxis`
- Metadata signature: `public bool IsBoundToAxis(string axisName, InputRig rig) { }`
- Native interval: `204` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[72];
    long long field_48;
} struct_0;

long long InputRig_TiltConfig_IsBoundToAxis(struct_0 *a0, unsigned long a1, unsigned long a2)
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
    if (a0->field_48)
        InputBindingBase__IsBoundToAxis(a0->field_48); /* do not return */
    sub_f7db74(0);
}
```

## `InputRig.TiltConfig.IsBoundToKey` — RVA `0xc42d48`

- Decompiled symbol: `InputRig_TiltConfig_IsBoundToKey`
- Metadata signature: `public bool IsBoundToKey(KeyCode key, InputRig rig) { }`
- Native interval: `204` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[72];
    long long field_48;
} struct_0;

long long InputRig_TiltConfig_IsBoundToKey(struct_0 *a0, unsigned long a1, unsigned long a2)
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
    if (a0->field_48)
        InputBindingBase__IsBoundToKey(a0->field_48); /* do not return */
    sub_f7db74(0);
}
```

## `InputRig.TiltConfig.IsEmulatingTouches` — RVA `0xc42e14`

- Decompiled symbol: `InputRig_TiltConfig_IsEmulatingTouches`
- Metadata signature: `public bool IsEmulatingTouches() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
unsigned int InputRig_TiltConfig_IsEmulatingTouches(void)
{
    return 0;
}
```

## `InputRig.TiltConfig.IsEmulatingMousePosition` — RVA `0xc42e1c`

- Decompiled symbol: `InputRig_TiltConfig_IsEmulatingMousePosition`
- Metadata signature: `public bool IsEmulatingMousePosition() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
unsigned int InputRig_TiltConfig_IsEmulatingMousePosition(void)
{
    return 0;
}
```

## `InputRig.TiltConfig.GetSubBindingDescriptions` — RVA `0xc42e24`

- Decompiled symbol: `InputRig_TiltConfig_GetSubBindingDescriptions`
- Metadata signature: `public void GetSubBindingDescriptions(BindingDescriptionList descList, Object undoObject, string parentMenuPath) { }`
- Native interval: `380` bytes
- Result: `pseudocode`

```c
extern long long g_1f0cf68;
extern long long g_1f0cf70;
extern long long g_1f0cf78;
extern long long g_1f0d690;
extern long long g_1f0d698;
extern long long g_1f0d6a0;
extern char g_1fab20b;

long long InputRig_TiltConfig_GetSubBindingDescriptions(long long *a0, long long a1, long long a2, long long a3)
{
    unsigned long long v10;  // x30
    unsigned long long v11;  // x27
    unsigned long long v12;  // x26
    unsigned long long v13;  // x25
    unsigned long long v14;  // x24
    unsigned long long v15;  // x23
    unsigned long long v16;  // x22
    unsigned long long v17;  // x21
    unsigned long long v18;  // x20
    unsigned long long v19;  // x19
    unsigned long long v0;  // [bp-0x50]
    unsigned long long v1;  // [bp-0x48]
    unsigned long long v2;  // [bp-0x40]
    unsigned long long v3;  // [bp-0x38]
    unsigned long long v4;  // [bp-0x30]
    unsigned long long v5;  // [bp-0x28]
    unsigned long long v6;  // [bp-0x20]
    unsigned long long v7;  // [bp-0x18]
    unsigned long long v8;  // [bp-0x10]
    unsigned long long v9;  // [bp-0x8]

    v0 = v10;
    v1 = v11;
    v2 = v12;
    v3 = v13;
    v4 = v14;
    v5 = v15;
    v6 = v16;
    v7 = v17;
    v8 = v18;
    v9 = v19;
    if (!(g_1fab20b & 1))
    {
        sub_f7d92c(&g_1f0cf78);
        sub_f7d92c(&g_1f0cf70);
        sub_f7d92c(&g_1f0cf68);
        sub_f7d92c(&g_1f0d690);
        sub_f7d92c(&g_1f0d698);
        sub_f7d92c(&g_1f0d6a0);
        g_1fab20b = 1;
    }
    if (a1)
    {
        BindingDescriptionList__Add(a1, a0[9], 1, g_1f0d690, a3, a2, 0);
        BindingDescriptionList__Add(a1, a0[10], 1, g_1f0cf68, a3, a2, 0);
        BindingDescriptionList__Add(a1, a0[11], g_1f0d698, a3, a2, 0); /* do not return */
    }
    sub_f7db74();
}
```
