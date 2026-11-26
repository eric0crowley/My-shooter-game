# Native pseudocode: InputRig.GamepadConfig

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `InputRig.GamepadConfig.BasicConstructor` — RVA `0xc3f68c`

- Decompiled symbol: `InputRig_GamepadConfig_BasicConstructor`
- Metadata signature: `private void BasicConstructor(InputRig rig) { }`
- Native interval: `792` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    char field_10;
} struct_0;

extern long long g_1ef0558;
extern char g_1fab1f3;

long long InputRig_GamepadConfig_BasicConstructor(struct_0 *ptr)
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
    if (!(g_1fab1f3 & 1))
    {
        sub_f7d92c("g.");
        sub_f7d92c("y7");
        sub_f7d92c(&g_1ef0558);
        g_1fab1f3 = 1;
    }
    ptr->field_10 = 0;
    DigitalBinding__ctor(sub_f7db70(g_1eef590), 0, 0); /* do not return */
}
```

## `InputRig.GamepadConfig.ctor` — RVA `0xc3f9a4`

- Decompiled symbol: `InputRig_GamepadConfig_ctor`
- Metadata signature: `public void .ctor(InputRig rig) { }`
- Native interval: `28` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    char field_10;
} struct_0;

long long InputRig_GamepadConfig_ctor(struct_0 *a0)
{
    Object__ctor();
    InputRig_GamepadConfig__BasicConstructor(a0); /* do not return */
}
```

## `InputRig.GamepadConfig.SyncGamepad` — RVA `0xc3f9c0`

- Decompiled symbol: `InputRig_GamepadConfig_SyncGamepad`
- Metadata signature: `public void SyncGamepad(GamepadManager.Gamepad gamepad, InputRig rig) { }`
- Native interval: `740` bytes
- Result: `pseudocode`
- Heuristic layout hint: `InputRig_GamepadConfig_Recovered` matched 18 offsets against `InputRig.GamepadConfig` metadata (confidence 1.00).

```c
typedef struct InputRig_GamepadConfig_Recovered {
    char padding_0[16];
    char enabled;
    char padding_11[7];
    long long digiFaceDownBinding;
    long long digiFaceRightBinding;
    long long digiFaceLeftBinding;
    long long digiFaceUpBinding;
    long long digiStartBinding;
    long long digiSelectBinding;
    long long digiL1Binding;
    long long digiR1Binding;
    long long digiL2Binding;
    long long digiR2Binding;
    long long digiL3Binding;
    long long digiR3Binding;
    long long analogL2Binding;
    long long analogR2Binding;
    long long leftStickStateBinding;
    long long rightStickStateBinding;
    long long dpadStateBinding;
} InputRig_GamepadConfig_Recovered;

struct_0 * InputRig_GamepadConfig_SyncGamepad(struct_0 *a0, void* ptr, unsigned int a2, unsigned long a3)
{
    unsigned long v0;  // x0
    void* p;  // x8
    void* addr;  // x8
    void* ptr3;  // x8
    void* ptr4;  // x8
    void* ptr5;  // x8
    void* ptr6;  // x8
    long long v15;  // x0
    void* ptr7;  // x8
    void* ptr8;  // x8
    void* ptr9;  // x8
    void* ptr10;  // x8
    void* ptr11;  // x8
    void* ptr12;  // x8
    void* ptr13;  // x8
    void* ptr14;  // x8

    if (!ptr)
    {
        return a0;
    }
    else if (a0->field_10)
    {
        v0 = (long long)ptr[56];
        if (v0)
        {
            GamepadManager_Gamepad_JoyState__SyncJoyState(v0, a0->field_88, a2);
            v0 = (long long)ptr[64];
            if (v0)
            {
                GamepadManager_Gamepad_JoyState__SyncJoyState(v0, a0->field_90, a2);
                v0 = (long long)ptr[72];
                if (v0)
                {
                    v0 = GamepadManager_Gamepad_JoyState__SyncJoyState(v0, a0->field_98, a2);
                    p = (long long)ptr[80];
                    if (p)
                    {
                        if ((int)p[24])
                        {
                            v0 = (long long)p[32];
                            if (v0)
                            {
                                v0 = GamepadManager_Gamepad_KeyState__SyncDigital(v0, a0->field_18, a2);
                                ptr7 = (long long)ptr[80];
                                if (ptr7)
                                {
                                    if ((int)ptr7[24] > 1)
                                    {
                                        v0 = (long long)ptr7[40];
                                        if (v0)
                                        {
                                            v0 = GamepadManager_Gamepad_KeyState__SyncDigital(v0, a0->field_20, a2);
                                            ptr8 = (long long)ptr[80];
                                            if (ptr8)
                                            {
                                                if ((int)ptr8[24] > 3)
                                                {
                                                    v0 = (long long)ptr8[56];
                                                    if (v0)
                                                    {
                                                        v0 = GamepadManager_Gamepad_KeyState__SyncDigital(v0, a0->field_28, a2);
                                                        ptr9 = (long long)ptr[80];
                                                        if (ptr9)
                                                        {
                                                            if ((int)ptr9[24] > 2)
                                                            {
                                                                v0 = (long long)ptr9[48];
                                                                if (v0)
                                                                {
                                                                    v0 = GamepadManager_Gamepad_KeyState__SyncDigital(v0, a0->field_30, a2);
                                                                    ptr10 = (long long)ptr[80];
                                                                    if (ptr10)
                                                                    {
                                                                        if ((int)ptr10[24] > 4)
                                                                        {
                                                                            v0 = (long long)ptr10[64];
                                                                            if (v0)
                                                                            {
                                                                                v0 = GamepadManager_Gamepad_KeyState__SyncDigital(v0, a0->field_38, a2);
                                                                                ptr11 = (long long)ptr[80];
                                                                                if (ptr11)
                                                                                {
                                                                                    if ((int)ptr11[24] > 5)
                                                                                    {
                                                                                        v0 = (long long)ptr11[72];
                                                                                        if (v0)
                                                                                        {
                                                                                            v0 = GamepadManager_Gamepad_KeyState__SyncDigital(v0, a0->field_40, a2);
                                                                                            ptr12 = (long long)ptr[80];
                                                                                            if (ptr12)
                                                                                            {
                                                                                                if ((int)ptr12[24] > 6)
                                                                                                {
                                                                                                    v0 = (long long)ptr12[80];
                                                                                                    if (v0)
                                                                                                    {
                                                                                                        v0 = GamepadManager_Gamepad_KeyState__SyncDigital(v0, a0->field_48, a2);
                                                                                                        ptr13 = (long long)ptr[80];
                                                                                                        if (ptr13)
                                                                                                        {
                                                                                                            if ((int)ptr13[24] > 7)
                                                                                                            {
                                                                                                                v0 = (long long)ptr13[88];
                                                                                                                if (v0)
                                                                                                                {
                                                                                                                    v0 = GamepadManager_Gamepad_KeyState__SyncDigital(v0, a0->field_50, a2);
                                                                                                                    ptr14 = (long long)ptr[80];
                                                                                                                    if (ptr14)
                                                                                                                    {
                                                                                                                        if ((int)ptr14[24] > 8)
                                                                                                                        {
                                                                                                                            v0 = (long long)ptr14[96];
                                                                                                                            if (v0)
                                                                                                                            {
                                                                                                                                v0 = GamepadManager_Gamepad_KeyState__SyncDigital(v0, a0->field_58, a2);
                                                                                                                                addr = (long long)ptr[80];
                                                                                                                                if (addr)
                                                                                                                                {
                                                                                                                                    if ((int)addr[24] > 9)
                                                                                                                                    {
                                                                                                                                        v0 = (long long)addr[104];
                                                                                                                                        if (v0)
                                                                                                                                        {
                                                                                                                                            v0 = GamepadManager_Gamepad_KeyState__SyncDigital(v0, a0->field_60, a2);
                                                                                                                                            ptr3 = (long long)ptr[80];
                                                                                                                                            if (ptr3)
                                                                                                                                            {
                                                                                                                                                if ((int)ptr3[24] > 10)
                                                                                                                                                {
                                                                                                                                                    v0 = (long long)ptr3[112];
                                                                                                                                                    if (v0)
                                                                                                                                                    {
                                                                                                                                                        v0 = GamepadManager_Gamepad_KeyState__SyncDigital(v0, a0->field_68, a2);
                                                                                                                                                        ptr4 = (long long)ptr[80];
                                                                                                                                                        if (ptr4)
                                                                                                                                                        {
                                                                                                                                                            if ((int)ptr4[24] > 11)
                                                                                                                                                            {
                                                                                                                                                                v0 = (long long)ptr4[120];
                                                                                                                                                                if (v0)
                                                                                                                                                                {
                                                                                                                                                                    v0 = GamepadManager_Gamepad_KeyState__SyncDigital(v0, a0->field_70, a2);
                                                                                                                                                                    ptr5 = (long long)ptr[80];
                                                                                                                                                                    if (ptr5)
                                                                                                                                                                    {
                                                                                                                                                                        if ((int)ptr5[24] > 8)
                                                                                                                                                                        {
                                                                                                                                                                            v0 = (long long)ptr5[96];
                                                                                                                                                                            if (v0)
                                                                                                                                                                            {
                                                                                                                                                                                v0 = GamepadManager_Gamepad_KeyState__SyncAnalog(v0, a0->field_78, a2);
                                                                                                                                                                                ptr6 = (long long)ptr[80];
                                                                                                                                                                                if (ptr6)
                                                                                                                                                                                {
                                                                                                                                                                                    if ((int)ptr6[24] > 9)
                                                                                                                                                                                    {
                                                                                                                                                                                        v0 = (long long)ptr6[104];
                                                                                                                                                                                        if (v0)
                                                                                                                                                                                        {
                                                                                                                                                                                            v15 = GamepadManager_Gamepad_KeyState__SyncAnalog(v0, a0->field_80, a2);
                                                                                                                                                                                            return GamepadManager_Gamepad_KeyState__SyncAnalog(v0, a0->field_80, a2);
                                                                                                                                                                                        }
                                                                                                                                                                                    }
                                                                                                                                                                                    else
                                                                                                                                                                                    {
                                                                                                                                                                                        sub_f7db7c(v0);
                                                                                                                                                                                    }
                                                                                                                                                                                }
                                                                                                                                                                            }
                                                                                                                                                                        }
                                                                                                                                                                        else
                                                                                                                                                                        {
                                                                                                                                                                            sub_f7db7c(v0);
                                                                                                                                                                        }
                                                                                                                                                                    }
                                                                                                                                                                }
                                                                                                                                                            }
                                                                                                                                                            else
                                                                                                                                                            {
                                                                                                                                                                sub_f7db7c(v0);
                                                                                                                                                            }
                                                                                                                                                        }
                                                                                                                                                    }
                                                                                                                                                }
                                                                                                                                                else
                                                                                                                                                {
                                                                                                                                                    sub_f7db7c(v0);
                                                                                                                                                }
                                                                                                                                            }
                                                                                                                                        }
                                                                                                                                    }
                                                                                                                                    else
                                                                                                                                    {
                                                                                                                                        sub_f7db7c(v0);
                                                                                                                                    }
                                                                                                                                }
                                                                                                                            }
                                                                                                                        }
                                                                                                                        else
                                                                                                                        {
                                                                                                                            sub_f7db7c(v0);
                                                                                                                        }
                                                                                                                    }
                                                                                                                }
                                                                                                            }
                                                                                                            else
                                                                                                            {
                                                                                                                sub_f7db7c(v0);
                                                                                                            }
                                                                                                        }
                                                                                                    }
                                                                                                }
                                                                                                else
                                                                                                {
                                                                                                    sub_f7db7c(v0);
                                                                                                }
                                                                                            }
                                                                                        }
                                                                                    }
                                                                                    else
                                                                                    {
                                                                                        sub_f7db7c(v0);
                                                                                    }
                                                                                }
                                                                            }
                                                                        }
                                                                        else
                                                                        {
                                                                            sub_f7db7c(v0);
                                                                        }
                                                                    }
                                                                }
                                                            }
                                                            else
                                                            {
                                                                sub_f7db7c(v0);
                                                            }
                                                        }
                                                    }
                                                }
                                                else
                                                {
                                                    sub_f7db7c(v0);
                                                }
                                            }
                                        }
                                    }
                                    else
                                    {
                                        sub_f7db7c(v0);
                                    }
                                }
                            }
                        }
                        else
                        {
                            sub_f7db7c(v0);
                        }
                    }
                }
            }
        }
        sub_f7db7c(sub_f7db74(v0));
    }
    else
    {
        return a0;
    }
}
```

## `InputRig.GamepadConfig.GetSubBindingDescriptions` — RVA `0xc3fca4`

- Decompiled symbol: `InputRig_GamepadConfig_GetSubBindingDescriptions`
- Metadata signature: `public void GetSubBindingDescriptions(BindingDescriptionList descList, Object undoObject, string parentMenuPath) { }`
- Native interval: `908` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    long long field_18;
} struct_0;

extern long long g_1f09828;
extern long long g_1f0bba8;
extern long long g_1f0bbb0;
extern long long g_1f0bbb8;
extern long long g_1f0bbc0;
extern long long g_1f0bc68;
extern long long g_1f0bc70;
extern long long g_1f0d1b8;
extern long long g_1f0d1c0;
extern long long g_1f0d1c8;
extern long long g_1f0d1d0;
extern long long g_1f0d630;
extern long long g_1f0d638;
extern long long g_1f0d878;
extern long long g_1f0dc80;
extern char g_1fab1f4;

long long InputRig_GamepadConfig_GetSubBindingDescriptions(struct_0 *a0, long long a1, long long a2, long long a3)
{
    unsigned long long v13;  // x30
    unsigned long long v14;  // x28
    unsigned long long v23;  // x19
    unsigned long long v15;  // x27
    unsigned long long v16;  // x26
    unsigned long long v17;  // x25
    unsigned long long v18;  // x24
    unsigned long long v19;  // x23
    unsigned long long v20;  // x22
    unsigned long long v21;  // x21
    unsigned long long v22;  // x20
    char *v0;  // [bp-0x60]
    unsigned long long v1;  // [bp-0x58]
    unsigned long long v2;  // [bp-0x50]
    unsigned long long v3;  // [bp-0x48]
    unsigned long long v4;  // [bp-0x40]
    unsigned long long v5;  // [bp-0x38]
    unsigned long long v6;  // [bp-0x30]
    unsigned long long v7;  // [bp-0x28]
    unsigned long long v8;  // [bp-0x20]
    unsigned long long v9;  // [bp-0x18]
    unsigned long long v10;  // [bp-0x10]
    unsigned long long v11;  // [bp-0x8]
    char v12;  // [bp+0x0]

    v0 = &v12;
    v1 = v13;
    v2 = v14;
    v3 = v15;
    v4 = v16;
    v5 = v17;
    v6 = v18;
    v7 = v19;
    v8 = v20;
    v9 = v21;
    v10 = v22;
    v11 = v23;
    if (!(g_1fab1f4 & 1))
    {
        sub_f7d92c(&g_1f0bbb8);
        sub_f7d92c(&g_1f0bba8);
        sub_f7d92c(&g_1f0d630);
        sub_f7d92c(&g_1f0bc68);
        sub_f7d92c(&g_1f0d878);
        sub_f7d92c("+\n");
        sub_f7d92c(&g_1f0bbc0);
        sub_f7d92c(&g_1f0dc80);
        sub_f7d92c(&g_1f0d1b8);
        sub_f7d92c(&g_1f0d1c0);
        sub_f7d92c(&g_1f0bbb0);
        sub_f7d92c(&g_1f09828);
        sub_f7d92c(&g_1f0d1d0);
        sub_f7d92c(&g_1f0d1c8);
        sub_f7d92c(&g_1f0bc70);
        sub_f7d92c(&g_1f0d638);
        sub_f7d92c("##");
        g_1fab1f4 = 1;
    }
    if (a1)
        BindingDescriptionList__Add(a1, a0->field_18, g_1f08ac8, a3, a2, 0); /* do not return */
    sub_f7db74();
}
```

## `InputRig.GamepadConfig.IsBoundToKey` — RVA `0xc40030`

- Decompiled symbol: `InputRig_GamepadConfig_IsBoundToKey`
- Metadata signature: `public bool IsBoundToKey(KeyCode key, InputRig rig) { }`
- Native interval: `512` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    long long field_18;
} struct_0;

long long InputRig_GamepadConfig_IsBoundToKey(struct_0 *a0, unsigned long a1, unsigned long a2)
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
    if (a0->field_18)
        InputBindingBase__IsBoundToKey(a0->field_18); /* do not return */
    sub_f7db74(0);
}
```

## `InputRig.GamepadConfig.IsBoundToAxis` — RVA `0xc40230`

- Decompiled symbol: `InputRig_GamepadConfig_IsBoundToAxis`
- Metadata signature: `public bool IsBoundToAxis(string axisName, InputRig rig) { }`
- Native interval: `512` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    long long field_18;
} struct_0;

long long InputRig_GamepadConfig_IsBoundToAxis(struct_0 *a0, unsigned long a1, unsigned long a2)
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
    if (a0->field_18)
        InputBindingBase__IsBoundToAxis(a0->field_18); /* do not return */
    sub_f7db74(0);
}
```

## `InputRig.GamepadConfig.IsEmulatingTouches` — RVA `0xc40430`

- Decompiled symbol: `InputRig_GamepadConfig_IsEmulatingTouches`
- Metadata signature: `public bool IsEmulatingTouches() { }`
- Native interval: `364` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    long long field_18;
} struct_0;

long long InputRig_GamepadConfig_IsEmulatingTouches(struct_0 *a0)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    if (a0->field_18)
        InputBindingBase__IsEmulatingTouches(a0->field_18, 0); /* do not return */
    sub_f7db74(0);
}
```

## `InputRig.GamepadConfig.IsEmulatingMousePosition` — RVA `0xc4059c`

- Decompiled symbol: `InputRig_GamepadConfig_IsEmulatingMousePosition`
- Metadata signature: `public bool IsEmulatingMousePosition() { }`
- Native interval: `364` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    long long field_18;
} struct_0;

long long InputRig_GamepadConfig_IsEmulatingMousePosition(struct_0 *a0)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    if (a0->field_18)
        InputBindingBase__IsEmulatingMousePosition(a0->field_18, 0); /* do not return */
    sub_f7db74(0);
}
```
