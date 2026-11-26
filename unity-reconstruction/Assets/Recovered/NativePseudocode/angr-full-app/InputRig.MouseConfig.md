# Native pseudocode: InputRig.MouseConfig

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `InputRig.MouseConfig.ctor` — RVA `0xc434c4`

- Decompiled symbol: `InputRig_MouseConfig_ctor`
- Metadata signature: `public void .ctor(InputRig rig) { }`
- Native interval: `244` bytes
- Result: `pseudocode`

```c
extern long long g_1f0c3a8;
extern long long g_1f0c3b0;
extern char g_1fab20f;

void InputRig_MouseConfig_ctor(long long *addr, long long a1)
{
    unsigned long long v7;  // x30
    unsigned long long v8;  // x24
    long long v17;  // x0
    unsigned long long v9;  // x23
    unsigned long long v10;  // x22
    unsigned long long v11;  // x21
    unsigned long long v12;  // x20
    unsigned long long v13;  // x19
    long long ptr[5];  // x0
    long long v15;  // x20
    long long p[5];  // x0
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
    if (!(g_1fab20f & 1))
    {
        sub_f7d92c("g.");
        sub_f7d92c(&g_1f0c3b0);
        sub_f7d92c(&g_1f0c3a8);
        g_1fab20f = 1;
    }
    Object__ctor(addr, 0);
    ptr = addr;
    ptr[2] = a1;
    sub_f7d8d0((long long [5])&ptr[2], a1);
    v15 = sub_f7db70(g_1eee9f8);
    AxisBinding__ctor(v15, g_1f0c3a8, 0, 0, 0);
    p = addr;
    p[3] = v15;
    sub_f7d8d0((long long [5])&p[3], v15);
    v17 = sub_f7db70(g_1eee9f8);
    AxisBinding__ctor(v17, g_1f0c3b0, 0, 0, 0);
    addr[4] = v17;
    sub_f7d8d0();
    return;
}
```

## `InputRig.MouseConfig.Reset` — RVA `0xc435b8`

- Decompiled symbol: `InputRig_MouseConfig_Reset`
- Metadata signature: `public void Reset() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long InputRig_MouseConfig_Reset(void)
{
    unsigned long v0;  // x0

    return v0;
}
```

## `InputRig.MouseConfig.SetPosition` — RVA `0xc435bc`

- Decompiled symbol: `InputRig_MouseConfig_SetPosition`
- Metadata signature: `public void SetPosition(Vector2 pos, int prio) { }`
- Native interval: `24` bytes
- Result: `pseudocode`
- Heuristic layout hint: `InputRig_MouseConfig_Recovered` matched 2 offsets against `InputRig.MouseConfig` metadata (confidence 0.67).

```c
typedef struct InputRig_MouseConfig_Recovered {
    char padding_0[48];
    unsigned int frMousePos;
    unsigned int field_34;
    int frMousePosPrio;
} InputRig_MouseConfig_Recovered;

struct_0 * InputRig_MouseConfig_SetPosition(struct_0 *ptr, int a1)
{
    unsigned int v0;  // s0
    unsigned int v1;  // s1

    if (a1 > ptr->field_38)
    {
        ptr->field_30 = v0;
        ptr->field_34 = v1;
        ptr->field_38 = a1;
    }
    return ptr;
}
```

## `InputRig.MouseConfig.GetPosition` — RVA `0xc435d4`

- Decompiled symbol: `InputRig_MouseConfig_GetPosition`
- Metadata signature: `public Vector3 GetPosition() { }`
- Native interval: `12` bytes
- Result: `pseudocode`

```c
long long InputRig_MouseConfig_GetPosition(unsigned long a0)
{
    return a0;
}
```

## `InputRig.MouseConfig.IsMouseDeltaUsable` — RVA `0xc435e0`

- Decompiled symbol: `InputRig_MouseConfig_IsMouseDeltaUsable`
- Metadata signature: `private bool IsMouseDeltaUsable() { }`
- Native interval: `192` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

typedef struct struct_1 {
    char padding_0[224];
    unsigned int field_e0;
} struct_1;

extern struct_0 *g_1eeed00;
extern struct_1 *g_1eeed08;
extern char g_1fab210;

unsigned long long InputRig_MouseConfig_IsMouseDeltaUsable(void)
{
    unsigned long long v0;  // x0

    if (!(g_1fab210 & 1))
    {
        sub_f7d92c(&g_1eeed00);
        sub_f7d92c(&g_1eeed08);
        g_1fab210 = 1;
    }
    if (!g_1eeed00->field_e0)
        sub_f7da5c(g_1eeed00);
    if (!((char)CF2Input__IsInMobileMode() & 1))
        return 1;
    if (!((char)Input__get_touchSupported(0) & 1) || !((char)Input__get_mousePresent(0) & 1) || ((char)Input__get_simulateMouseWithTouches(0) & 1))
        return 0;
    if (!g_1eeed08->field_e0)
        sub_f7da5c(g_1eeed08);
    if (CFCursor__get_lockState() != 1)
        v0 = 0;
    else
        v0 = 1;
    return v0;
    return 0;
}
```

## `InputRig.MouseConfig.IsMousePositionUsable` — RVA `0xc436a0`

- Decompiled symbol: `InputRig_MouseConfig_IsMousePositionUsable`
- Metadata signature: `private bool IsMousePositionUsable() { }`
- Native interval: `192` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[224];
    unsigned int field_e0;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1eeed00;
extern struct_1 *g_1eeed08;
extern char g_1fab211;

unsigned long long InputRig_MouseConfig_IsMousePositionUsable(void)
{
    unsigned long long v0;  // x0

    if (!(g_1fab211 & 1))
    {
        sub_f7d92c(&g_1eeed00);
        sub_f7d92c(&g_1eeed08);
        g_1fab211 = 1;
    }
    if (!g_1eeed00->field_e0)
        sub_f7da5c(g_1eeed00);
    if (!((char)CF2Input__IsInMobileMode() & 1))
        return 1;
    if (!((char)Input__get_touchSupported(0) & 1) || !((char)Input__get_mousePresent(0) & 1) || ((char)Input__get_simulateMouseWithTouches(0) & 1))
        return 0;
    if (!g_1eeed08->field_e0)
        sub_f7da5c(g_1eeed08);
    if (CFCursor__get_lockState() == 1)
        v0 = 0;
    else
        v0 = 1;
    return v0;
    return 0;
}
```

## `InputRig.MouseConfig.Update` — RVA `0xc43760`

- Decompiled symbol: `InputRig_MouseConfig_Update`
- Metadata signature: `public void Update() { }`
- Native interval: `224` bytes
- Result: `pseudocode`
- Heuristic layout hint: `InputRig_MouseConfig_Recovered` matched 6 offsets against `InputRig.MouseConfig` metadata (confidence 0.86).

```c
typedef struct InputRig_MouseConfig_Recovered {
    char padding_0[16];
    long long rig;
    long long horzDeltaBinding;
    long long vertDeltaBinding;
    unsigned long long mousePos;
    unsigned long long frMousePos;
    char field_34;
    char padding_35[3];
    unsigned int frMousePosPrio;
} InputRig_MouseConfig_Recovered;

extern long long g_1f11658;
extern long long g_1f11660;
extern char g_1fab212;

unsigned long long InputRig_MouseConfig_Update(struct_0 *ptr)
{
    unsigned long long v0;  // x0
    unsigned long v1;  // 4118
    unsigned int v2;  // s0
    unsigned int v3;  // s1
    unsigned long v4;  // x8

    if (!(g_1fab212 & 1))
    {
        sub_f7d92c(&g_1f11658);
        sub_f7d92c(&g_1f11660);
        g_1fab212 = 1;
    }
    if (((char)InputRig_MouseConfig__IsMouseDeltaUsable() & 1))
    {
        Input__GetAxisRaw(g_1f11658, 0);
        if (!ptr->field_18)
            sub_f7db74();
        AxisBinding__SyncFloat(ptr->field_18, 2, ptr->field_10, 0);
        Input__GetAxisRaw(g_1f11660, 0);
        if (!ptr->field_20)
            sub_f7db74();
        AxisBinding__SyncFloat(ptr->field_20, 2, ptr->field_10, 0);
    }
    v0 = InputRig_MouseConfig__IsMousePositionUsable();
    if (((char)v0 & 1))
    {
        v0 = Input__get_mousePosition(0);
        v1 = arm64g_calculate_condition(193, (unsigned long long)(unsigned int)*((int *)&ptr->field_34), 2, 0);
        if (!((char)v1))
        {
            *((unsigned int *)&ptr->field_30) = v2;
            *((unsigned int *)((char *)&ptr->field_30 + 4)) = v3;
        }
    }
    v4 = ptr->field_30;
    *((unsigned int *)&ptr->field_34) = 4294967286;
    ptr->field_28 = v4;
    return v0;
}
```

## `InputRig.MouseConfig.IsBoundToAxis` — RVA `0xc43840`

- Decompiled symbol: `InputRig_MouseConfig_IsBoundToAxis`
- Metadata signature: `public bool IsBoundToAxis(string axisName, InputRig rig) { }`
- Native interval: `92` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    long long field_18;
} struct_0;

long long InputRig_MouseConfig_IsBoundToAxis(struct_0 *a0, unsigned long a1, unsigned long a2)
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

## `InputRig.MouseConfig.IsBoundToKey` — RVA `0xc4389c`

- Decompiled symbol: `InputRig_MouseConfig_IsBoundToKey`
- Metadata signature: `public bool IsBoundToKey(KeyCode key, InputRig rig) { }`
- Native interval: `92` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    long long field_18;
} struct_0;

long long InputRig_MouseConfig_IsBoundToKey(struct_0 *a0, unsigned long a1, unsigned long a2)
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

## `InputRig.MouseConfig.IsEmulatingTouches` — RVA `0xc438f8`

- Decompiled symbol: `InputRig_MouseConfig_IsEmulatingTouches`
- Metadata signature: `public bool IsEmulatingTouches() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
unsigned int InputRig_MouseConfig_IsEmulatingTouches(void)
{
    return 0;
}
```

## `InputRig.MouseConfig.IsEmulatingMousePosition` — RVA `0xc43900`

- Decompiled symbol: `InputRig_MouseConfig_IsEmulatingMousePosition`
- Metadata signature: `public bool IsEmulatingMousePosition() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
unsigned int InputRig_MouseConfig_IsEmulatingMousePosition(void)
{
    return 0;
}
```

## `InputRig.MouseConfig.GetSubBindingDescriptions` — RVA `0xc43908`

- Decompiled symbol: `InputRig_MouseConfig_GetSubBindingDescriptions`
- Metadata signature: `public void GetSubBindingDescriptions(BindingDescriptionList descList, Object undoObject, string parentMenuPath) { }`
- Native interval: `172` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    long long field_18;
} struct_0;

extern long long g_1f0ab60;
extern long long g_1f0f988;
extern char g_1fab213;

long long InputRig_MouseConfig_GetSubBindingDescriptions(struct_0 *a0, long long a1, long long a2, long long a3)
{
    unsigned long long v0;  // x0

    if (!(g_1fab213 & 1))
    {
        sub_f7d92c(&g_1f0ab60);
        sub_f7d92c(&g_1f0f988);
        g_1fab213 = 1;
    }
    if (a1)
    {
        BindingDescriptionList__Add(a1, a0->field_18, 2, g_1f0ab60, a3, a2, 0);
        v0 = BindingDescriptionList__Add();
        return BindingDescriptionList__Add();
    }
    sub_f7db74();
}
```
