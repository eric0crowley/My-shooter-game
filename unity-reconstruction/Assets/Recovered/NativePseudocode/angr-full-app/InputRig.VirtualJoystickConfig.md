# Native pseudocode: InputRig.VirtualJoystickConfig

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `InputRig.VirtualJoystickConfig.BasicConstructor` — RVA `0xc40708`

- Decompiled symbol: `InputRig_VirtualJoystickConfig_BasicConstructor`
- Metadata signature: `private void BasicConstructor() { }`
- Native interval: `288` bytes
- Result: `pseudocode`
- Heuristic layout hint: `InputRig_VirtualJoystickConfig_Recovered` matched 3 offsets against `InputRig.VirtualJoystickConfig` metadata (confidence 0.75).

```c
typedef struct InputRig_VirtualJoystickConfig_Recovered {
    char padding_0[16];
    long long field_10;
    char padding_18[8];
    long long joystickConfig;
    long long joystickState;
    uint128_t keyboardUp;
} InputRig_VirtualJoystickConfig_Recovered;

extern long long g_1ef0548;
extern long long g_1ef0550;
extern long long g_1ef0558;
extern long long g_1f0ba80;
extern char g_1fab1f5;

long long InputRig_VirtualJoystickConfig_BasicConstructor(struct_0 *a0)
{
    unsigned long long v6;  // x30
    unsigned long long v7;  // x23
    long long v16;  // x21
    long long v17;  // x20
    struct_0 *p;  // x0
    unsigned long long v8;  // x22
    unsigned long long v9;  // x21
    unsigned long long v10;  // x20
    unsigned long long v11;  // x19
    struct_0 *addr;  // x0
    struct_0 *ptr3;  // x20
    long long v14;  // x21
    struct_0 *ptr;  // x20
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
    if (!(g_1fab1f5 & 1))
    {
        sub_f7d92c(&g_1ef0548);
        sub_f7d92c(&g_1ef0558);
        sub_f7d92c(&g_1ef0550);
        sub_f7d92c(&g_1f0ba80);
        g_1fab1f5 = 1;
    }
    addr = a0;
    addr->field_10 = g_1f0ba80;
    sub_f7d8d0((struct InputRig_VirtualJoystickConfig_Recovered *)&addr->field_10, g_1f0ba80);
    ptr3 = a0;
    v14 = ptr3->field_20;
    ptr = &ptr3->field_20;
    *((void*)&ptr->field_10) = 7685131766005016315479858348151;
    if (!v14)
    {
        v16 = sub_f7db70(g_1ef0548);
        JoystickConfig__ctor(v16, 0);
        *((long long *)&ptr->padding_0[0]) = v16;
        sub_f7d8d0(ptr, v16);
        v14 = *((long long *)&ptr->padding_0[0]);
    }
    v17 = sub_f7db70(g_1ef0550);
    JoystickState__ctor(v17, v14, 0);
    p = a0;
    p->field_28 = v17;
    sub_f7d8d0((struct InputRig_VirtualJoystickConfig_Recovered *)&p->field_28, v17);
    JoystickStateBinding__ctor(sub_f7db70(g_1ef0558), 0, 0); /* do not return */
}
```

## `InputRig.VirtualJoystickConfig.ctor` — RVA `0xc40828`

- Decompiled symbol: `InputRig_VirtualJoystickConfig_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `28` bytes
- Result: `pseudocode`
- Heuristic layout hint: `InputRig_VirtualJoystickConfig_Recovered` matched 3 offsets against `InputRig.VirtualJoystickConfig` metadata (confidence 0.75).

```c
typedef struct InputRig_VirtualJoystickConfig_Recovered {
    char padding_0[16];
    long long field_10;
    char padding_18[8];
    long long joystickConfig;
    long long joystickState;
    uint128_t keyboardUp;
} InputRig_VirtualJoystickConfig_Recovered;

long long InputRig_VirtualJoystickConfig_ctor(struct_0 *a0)
{
    Object__ctor();
    InputRig_VirtualJoystickConfig__BasicConstructor(a0); /* do not return */
}
```

## `InputRig.VirtualJoystickConfig.ctor` — RVA `0xc40844`

- Decompiled symbol: `InputRig_VirtualJoystickConfig_ctor`
- Metadata signature: `public void .ctor(string targetName, KeyCode keyUp, KeyCode keyRight, KeyCode keyDown, KeyCode keyLeft) { }`
- Native interval: `100` bytes
- Result: `pseudocode`
- Heuristic layout hint: `InputRig_VirtualJoystickConfig_Recovered` matched 3 offsets against `InputRig.VirtualJoystickConfig` metadata (confidence 0.75).

```c
typedef struct InputRig_VirtualJoystickConfig_Recovered {
    char padding_0[16];
    long long field_10;
    char padding_18[8];
    long long joystickConfig;
    long long joystickState;
    uint128_t keyboardUp;
} InputRig_VirtualJoystickConfig_Recovered;

long long InputRig_VirtualJoystickConfig_ctor(struct_0 *a0, unsigned long a1, unsigned long a2, unsigned long a3, unsigned long a4, unsigned long a5)
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
    Object__ctor();
    InputRig_VirtualJoystickConfig__BasicConstructor(a0); /* do not return */
}
```

## `InputRig.VirtualJoystickConfig.Reset` — RVA `0xc408a8`

- Decompiled symbol: `InputRig_VirtualJoystickConfig_Reset`
- Metadata signature: `public override void Reset() { }`
- Native interval: `28` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[40];
    long long field_28;
} struct_0;

long long InputRig_VirtualJoystickConfig_Reset(struct_0 *a0, unsigned long a1)
{
    unsigned long long v0;  // x0

    if (a0->field_28)
    {
        v0 = JoystickState__Reset(a0->field_28, 0);
        return JoystickState__Reset(a0->field_28, 0);
    }
    sub_f7db74(0);
}
```

## `InputRig.VirtualJoystickConfig.Update` — RVA `0xc408c4`

- Decompiled symbol: `InputRig_VirtualJoystickConfig_Update`
- Metadata signature: `public override void Update(InputRig rig) { }`
- Native interval: `192` bytes
- Result: `pseudocode`
- Heuristic layout hint: `InputRig_VirtualJoystickConfig_Recovered` matched 6 offsets against `InputRig.VirtualJoystickConfig` metadata (confidence 1.00).

```c
typedef struct InputRig_VirtualJoystickConfig_Recovered {
    char padding_0[40];
    long long joystickState;
    unsigned int keyboardUp;
    unsigned int keyboardRight;
    unsigned int keyboardDown;
    unsigned int keyboardLeft;
    long long joyStateBinding;
} InputRig_VirtualJoystickConfig_Recovered;

long long InputRig_VirtualJoystickConfig_Update(struct_0 *a0, long long a1)
{
    unsigned int v0;  // w0
    unsigned int v1;  // w0
    unsigned int v2;  // w0
    unsigned int v3;  // w0
    unsigned long long v4;  // x0

    v0 = InputRig__GetSourceKeyState(a0->field_30);
    v1 = InputRig__GetSourceKeyState(a0->field_34);
    v2 = InputRig__GetSourceKeyState(a0->field_38);
    v3 = InputRig__GetSourceKeyState(a0->field_3c);
    if (a0->field_28)
    {
        JoystickState__ApplyDigital(a0->field_28, v0 & 1, v1 & 1, v2 & 1, v3 & 1, 0);
        if (a0->field_28)
        {
            JoystickState__Update(a0->field_28, 0);
            if (a0->field_40)
            {
                v4 = JoystickStateBinding__SyncJoyState(a0->field_40, a0->field_28, a1, 0);
                return JoystickStateBinding__SyncJoyState(a0->field_40, a0->field_28, a1, 0);
            }
        }
    }
    sub_f7db74();
}
```

## `InputRig.VirtualJoystickConfig.SetState` — RVA `0xc40984`

- Decompiled symbol: `InputRig_VirtualJoystickConfig_SetState`
- Metadata signature: `public void SetState(JoystickState state) { }`
- Native interval: `20` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[40];
    long long field_28;
} struct_0;

unsigned long long InputRig_VirtualJoystickConfig_SetState(struct_0 *a0)
{
    unsigned long long v0;  // x0

    if (!a0->field_28)
        return 0;
    v0 = JoystickState__ApplyState(a0->field_28);
    return JoystickState__ApplyState(a0->field_28);
}
```

## `InputRig.VirtualJoystickConfig.IsBoundToAxis` — RVA `0xc40998`

- Decompiled symbol: `InputRig_VirtualJoystickConfig_IsBoundToAxis`
- Metadata signature: `public bool IsBoundToAxis(string axisName, InputRig rig) { }`
- Native interval: `28` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[64];
    long long field_40;
} struct_0;

long long InputRig_VirtualJoystickConfig_IsBoundToAxis(struct_0 *a0)
{
    if (a0->field_40)
        InputBindingBase__IsBoundToAxis(a0->field_40); /* do not return */
    sub_f7db74(0);
}
```

## `InputRig.VirtualJoystickConfig.IsBoundToKey` — RVA `0xc409b4`

- Decompiled symbol: `InputRig_VirtualJoystickConfig_IsBoundToKey`
- Metadata signature: `public bool IsBoundToKey(KeyCode key, InputRig rig) { }`
- Native interval: `28` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[64];
    long long field_40;
} struct_0;

long long InputRig_VirtualJoystickConfig_IsBoundToKey(struct_0 *a0)
{
    if (a0->field_40)
        InputBindingBase__IsBoundToKey(a0->field_40); /* do not return */
    sub_f7db74(0);
}
```

## `InputRig.VirtualJoystickConfig.IsEmulatingTouches` — RVA `0xc409d0`

- Decompiled symbol: `InputRig_VirtualJoystickConfig_IsEmulatingTouches`
- Metadata signature: `public bool IsEmulatingTouches() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
unsigned int InputRig_VirtualJoystickConfig_IsEmulatingTouches(void)
{
    return 0;
}
```

## `InputRig.VirtualJoystickConfig.IsEmulatingMousePosition` — RVA `0xc409d8`

- Decompiled symbol: `InputRig_VirtualJoystickConfig_IsEmulatingMousePosition`
- Metadata signature: `public bool IsEmulatingMousePosition() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
unsigned int InputRig_VirtualJoystickConfig_IsEmulatingMousePosition(void)
{
    return 0;
}
```

## `InputRig.VirtualJoystickConfig.GetSubBindingDescriptions` — RVA `0xc409e0`

- Decompiled symbol: `InputRig_VirtualJoystickConfig_GetSubBindingDescriptions`
- Metadata signature: `public void GetSubBindingDescriptions(BindingDescriptionList descList, Object undoObject, string parentMenuPath) { }`
- Native interval: `116` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[64];
    long long field_40;
} struct_0;

extern long long g_1f0baa8;
extern char g_1fab1f6;

long long InputRig_VirtualJoystickConfig_GetSubBindingDescriptions(struct_0 *a0, long long a1, long long a2, long long a3)
{
    if (!(g_1fab1f6 & 1))
    {
        sub_f7d92c(&g_1f0baa8);
        g_1fab1f6 = 1;
    }
    if (a1)
        BindingDescriptionList__Add(a1, a0->field_40, g_1f0baa8, a3, a2, 0); /* do not return */
    sub_f7db74();
}
```
