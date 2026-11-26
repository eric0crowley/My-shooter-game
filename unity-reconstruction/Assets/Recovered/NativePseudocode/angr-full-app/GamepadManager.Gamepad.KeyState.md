# Native pseudocode: GamepadManager.Gamepad.KeyState

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `GamepadManager.Gamepad.KeyState.ctor` — RVA `0xc2da14`

- Decompiled symbol: `GamepadManager_Gamepad_KeyState_ctor`
- Metadata signature: `public void .ctor(GamepadManager.Gamepad gamepad, bool isTrigger, AnalogConfig analogConfig) { }`
- Native interval: `108` bytes
- Result: `pseudocode`
- Heuristic layout hint: `GamepadManager_Gamepad_KeyState_Recovered` matched 7 offsets against `GamepadManager.Gamepad.KeyState` metadata (confidence 0.88).

```c
typedef struct GamepadManager_Gamepad_KeyState_Recovered {
    char padding_0[16];
    long long gamepad;
    char isTrigger;
    char padding_19[7];
    long long analogConfig;
    char isConnectedToHardware;
    char padding_29[3];
    unsigned int frAnalog;
    char frDigital;
    char padding_31[3];
    unsigned long long analogCur;
    unsigned int field_3b;
} GamepadManager_Gamepad_KeyState_Recovered;

long long GamepadManager_Gamepad_KeyState_ctor(struct_0 *p, long long a1, char a2, long long a3)
{
    struct_0 *ptr;  // x21
    unsigned long v1;  // x0

    Object__ctor();
    p->field_10 = a1;
    sub_f7d8d0((struct GamepadManager_Gamepad_KeyState_Recovered *)&p->field_10, a1);
    p->field_20 = a3;
    ptr = &p->field_20;
    ptr->padding_0[8] = a2 & 1;
    v1 = sub_f7d8d0(ptr, a3);
    ptr->padding_0[8] = 0;
    *((unsigned int *)&ptr->padding_0[12]) = 0;
    *((char *)&ptr->field_10) = 0;
    *((unsigned long long *)((char *)&ptr->field_10 + 4)) = 0;
    *((unsigned int *)&ptr->padding_19[2]) = 0;
    return v1;
}
```

## `GamepadManager.Gamepad.KeyState.ConnectToJoy` — RVA `0xc2de18`

- Decompiled symbol: `GamepadManager_Gamepad_KeyState_ConnectToJoy`
- Metadata signature: `public void ConnectToJoy(GamepadProfile.KeySource src) { }`
- Native interval: `64` bytes
- Result: `pseudocode`
- Heuristic layout hint: `GamepadManager_Gamepad_KeyState_Recovered` matched 6 offsets against `GamepadManager.Gamepad.KeyState` metadata (confidence 0.86).

```c
typedef struct GamepadManager_Gamepad_KeyState_Recovered {
    char padding_0[40];
    char isConnectedToHardware;
    char padding_29[3];
    unsigned int frAnalog;
    char frDigital;
    char padding_31[3];
    unsigned long long analogCur;
    unsigned int field_3b;
    char padding_3f[1];
    unsigned long long srcAxisId;
    char srcAxisSign;
} GamepadManager_Gamepad_KeyState_Recovered;

typedef struct struct_0 {
    char padding_0[24];
    char field_18;
} struct_0;

struct_1 * GamepadManager_Gamepad_KeyState_ConnectToJoy(struct_1 *ptr, struct_0 *index)
{
    char v0;  // x8

    if (!index)
        v0 = 0;
    else
        v0 = 1;
    ptr->field_28 = v0;
    *((unsigned long long *)&ptr->field_3b) = 18446744073709551615 CONCAT 18446744073709551615;
    if (index)
    {
        *((long long *)&ptr->field_3b) = [D] unsupported_Iop_ZeroHI64ofV128();
        *((char *)&ptr->field_40) = index->field_18;
    }
    ptr->field_2c = 0;
    ptr->field_30 = 0;
    *((unsigned long long *)&(&ptr->padding_31)[1]) = 0;
    *((unsigned int *)((char *)&ptr->field_34 + 3)) = 0;
    return ptr;
}
```

## `GamepadManager.Gamepad.KeyState.Reset` — RVA `0xc2de74`

- Decompiled symbol: `GamepadManager_Gamepad_KeyState_Reset`
- Metadata signature: `public void Reset() { }`
- Native interval: `20` bytes
- Result: `pseudocode`
- Heuristic layout hint: `GamepadManager_Gamepad_KeyState_Recovered` matched 3 offsets against `GamepadManager.Gamepad.KeyState` metadata (confidence 0.75).

```c
typedef struct GamepadManager_Gamepad_KeyState_Recovered {
    char padding_0[44];
    unsigned int frAnalog;
    char frDigital;
    char padding_31[3];
    unsigned long long analogCur;
    unsigned int field_3b;
} GamepadManager_Gamepad_KeyState_Recovered;

struct_0 * GamepadManager_Gamepad_KeyState_Reset(struct_0 *ptr)
{
    ptr->field_2c = 0;
    ptr->field_30 = 0;
    *((unsigned long long *)&(&ptr->padding_31)[1]) = 0;
    *((unsigned int *)((char *)&ptr->field_34 + 3)) = 0;
    return ptr;
}
```

## `GamepadManager.Gamepad.KeyState.GetDigitalDown` — RVA `0xc2df28`

- Decompiled symbol: `GamepadManager_Gamepad_KeyState_GetDigitalDown`
- Metadata signature: `public bool GetDigitalDown() { }`
- Native interval: `32` bytes
- Result: `pseudocode`

```c
unsigned long long GamepadManager_Gamepad_KeyState_GetDigitalDown(char *a0)
{
    if (!a0[61])
    {
        return 0;
    }
    else if (a0[62])
    {
        return 0;
    }
    else
    {
        return 1;
    }
}
```

## `GamepadManager.Gamepad.KeyState.GetDigitalUp` — RVA `0xc2df98`

- Decompiled symbol: `GamepadManager_Gamepad_KeyState_GetDigitalUp`
- Metadata signature: `public bool GetDigitalUp() { }`
- Native interval: `32` bytes
- Result: `pseudocode`

```c
unsigned long long GamepadManager_Gamepad_KeyState_GetDigitalUp(char *a0)
{
    if (a0[61])
    {
        return 0;
    }
    else if (!a0[62])
    {
        return 0;
    }
    else
    {
        return 1;
    }
}
```

## `GamepadManager.Gamepad.KeyState.Update` — RVA `0xc2e4f0`

- Decompiled symbol: `GamepadManager_Gamepad_KeyState_Update`
- Metadata signature: `public void Update() { }`
- Native interval: `192` bytes
- Result: `pseudocode`
- Heuristic layout hint: `GamepadManager_Gamepad_KeyState_Recovered` matched 8 offsets against `GamepadManager.Gamepad.KeyState` metadata (confidence 1.00).

```c
typedef struct GamepadManager_Gamepad_KeyState_Recovered {
    char padding_0[32];
    long long analogConfig;
    char padding_28[4];
    unsigned int frAnalog;
    char frDigital;
    char padding_31[3];
    unsigned int analogCur;
    unsigned int analogRawCur;
    char digiCurRaw;
    char digiCur;
    char digiPrev;
} GamepadManager_Gamepad_KeyState_Recovered;

unsigned long long GamepadManager_Gamepad_KeyState_Update(struct_0 *ptr, unsigned long a1)
{
    unsigned int v0;  // w8
    unsigned int v1;  // s0
    unsigned long v2;  // x0
    struct_0 *p;  // x9
    unsigned int v4;  // w8
    unsigned long long v5;  // x0
    struct_0 *addr;  // x10
    unsigned long v7;  // 4132

    GamepadManager_Gamepad_KeyState__ReadHardwareState();
    v0 = ptr->field_30;
    v1 = ptr->field_2c;
    v2 = ptr->field_20;
    ptr->field_3e = ptr->field_3d;
    if (!v0)
        p = ptr;
    else
        p = NULL;
    ptr->field_2c = 0;
    ptr->field_30 = 0;
    ptr->field_3c = v0;
    ptr->field_38 = v1;
    if (v2)
    {
        if (v0)
            v1 = 0x3f800000;
        AnalogConfig__GetAnalogVal();
        v4 = ptr->field_3c;
        ptr->field_34 = v1;
        if (v4)
            goto LABEL_102e580;
        if (!ptr->field_20)
            sub_f7db74();
        v5 = AnalogConfig__GetDigitalVal(ptr->field_20, ptr->field_3e, 0);
    }
    else
    {
        if (!v0)
            addr = NULL;
        else
            addr = ptr;
        if (v0)
        {
            if (!addr)
                sub_f7db74();
            addr->field_34 = 0x3f800000;
LABEL_102e580:
            v5 = 1;
        }
        else if (p)
        {
            p->field_34 = v1;
            v7 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v1, 0x3f000000)) >> 5 & 3 | (unsigned long long)(CmpF(v1, 0x3f000000) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v1, 0x3f000000)) >> 5 & 3 | (unsigned long long)(CmpF(v1, 0x3f000000) & 1)) & ((unsigned long long)(char)(CmpF(v1, 0x3f000000)) >> 5 & 3 | (unsigned long long)(CmpF(v1, 0x3f000000) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
            if ((char)v7)
                v5 = 0;
            else
                v5 = 1;
        }
        else
        {
            sub_f7db74();
        }
    }
    ptr->field_3d = (char)v5 & 1;
    return v5;
}
```

## `GamepadManager.Gamepad.KeyState.SetDigital` — RVA `0xc2e5b0`

- Decompiled symbol: `GamepadManager_Gamepad_KeyState_SetDigital`
- Metadata signature: `public void SetDigital(bool state) { }`
- Native interval: `16` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[48];
    char field_30;
} struct_0;

struct_0 * GamepadManager_Gamepad_KeyState_SetDigital(struct_0 *ptr, unsigned long a1)
{
    if (((char)a1 & 1))
        ptr->field_30 = 1;
    return ptr;
}
```

## `GamepadManager.Gamepad.KeyState.SetAnalog` — RVA `0xc2e5c0`

- Decompiled symbol: `GamepadManager_Gamepad_KeyState_SetAnalog`
- Metadata signature: `public void SetAnalog(float val) { }`
- Native interval: `40` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[44];
    unsigned int field_2c;
} struct_0;

struct_0 * GamepadManager_Gamepad_KeyState_SetAnalog(struct_0 *ptr)
{
    unsigned int v0;  // s1
    unsigned int v1;  // s0
    unsigned long v2;  // 4129
    unsigned int v3;  // s0
    unsigned int flag;  // s1
    unsigned long v5;  // 4133
    unsigned int v6;  // s0

    v0 = ptr->field_2c;
    v2 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v0, v1)) >> 5 & 3 | (unsigned long long)(CmpF(v0, v1) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v0, v1)) >> 5 & 3 | (unsigned long long)(CmpF(v0, v1) & 1)) & ((unsigned long long)(char)(CmpF(v0, v1)) >> 5 & 3 | (unsigned long long)(CmpF(v0, v1) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if ((char)v2)
        return ptr;
    v3 = [D] unsupported_Iop_ZeroHI96ofV128();
    flag = 0;
    v5 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v1, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v1, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v1, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v1, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v1, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v1, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if ((char)v5)
        v6 = v3;
    else
        v6 = flag;
    ptr->field_2c = v6;
    return ptr;
}
```

## `GamepadManager.Gamepad.KeyState.SetConfig` — RVA `0xc2e808`

- Decompiled symbol: `GamepadManager_Gamepad_KeyState_SetConfig`
- Metadata signature: `public void SetConfig(AnalogConfig config) { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[32];
    unsigned long long field_20;
} struct_0;

long long GamepadManager_Gamepad_KeyState_SetConfig(struct_0 *ptr, unsigned long a1)
{
    long long v0;  // x0

    ptr->field_20 = a1;
    v0 = sub_f7d8d0();
    return sub_f7d8d0();
}
```

## `GamepadManager.Gamepad.KeyState.GetDigitalRaw` — RVA `0xc2e810`

- Decompiled symbol: `GamepadManager_Gamepad_KeyState_GetDigitalRaw`
- Metadata signature: `public bool GetDigitalRaw() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[60];
    char field_3c;
} struct_0;

long long GamepadManager_Gamepad_KeyState_GetDigitalRaw(struct_0 *a0)
{
    return a0->field_3c;
}
```

## `GamepadManager.Gamepad.KeyState.GetDigital` — RVA `0xc2e818`

- Decompiled symbol: `GamepadManager_Gamepad_KeyState_GetDigital`
- Metadata signature: `public bool GetDigital() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[61];
    char field_3d;
} struct_0;

long long GamepadManager_Gamepad_KeyState_GetDigital(struct_0 *a0)
{
    return a0->field_3d;
}
```

## `GamepadManager.Gamepad.KeyState.GetAnalog` — RVA `0xc2e820`

- Decompiled symbol: `GamepadManager_Gamepad_KeyState_GetAnalog`
- Metadata signature: `public float GetAnalog() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long GamepadManager_Gamepad_KeyState_GetAnalog(unsigned long a0)
{
    return a0;
}
```

## `GamepadManager.Gamepad.KeyState.GetAnalogRaw` — RVA `0xc2e828`

- Decompiled symbol: `GamepadManager_Gamepad_KeyState_GetAnalogRaw`
- Metadata signature: `public float GetAnalogRaw() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long GamepadManager_Gamepad_KeyState_GetAnalogRaw(unsigned long a0)
{
    return a0;
}
```

## `GamepadManager.Gamepad.KeyState.IsTrigger` — RVA `0xc2e830`

- Decompiled symbol: `GamepadManager_Gamepad_KeyState_IsTrigger`
- Metadata signature: `public bool IsTrigger() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    char field_18;
} struct_0;

long long GamepadManager_Gamepad_KeyState_IsTrigger(struct_0 *a0)
{
    return a0->field_18;
}
```

## `GamepadManager.Gamepad.KeyState.ReadHardwareState` — RVA `0xc2e838`

- Decompiled symbol: `GamepadManager_Gamepad_KeyState_ReadHardwareState`
- Metadata signature: `private void ReadHardwareState() { }`
- Native interval: `168` bytes
- Result: `pseudocode`
- Heuristic layout hint: `GamepadManager_Gamepad_KeyState_Recovered` matched 7 offsets against `GamepadManager.Gamepad.KeyState` metadata (confidence 1.00).

```c
typedef struct GamepadManager_Gamepad_KeyState_Recovered {
    char padding_0[16];
    unsigned long long gamepad;
    char padding_18[16];
    char isConnectedToHardware;
    char padding_29[3];
    unsigned int frAnalog;
    char frDigital;
    char padding_31[15];
    unsigned int srcAxisId;
    unsigned int srcKeyId;
    char srcAxisSign;
} GamepadManager_Gamepad_KeyState_Recovered;

void GamepadManager_Gamepad_KeyState_ReadHardwareState(struct_0 *ptr)
{
    unsigned long v0;  // x1
    unsigned long long v1;  // x0
    unsigned long long v2;  // x20
    unsigned long v3;  // x1
    unsigned int v4;  // s8
    unsigned int v5;  // s0
    unsigned int v6;  // s0
    unsigned long v7;  // 4125
    unsigned int v8;  // s0
    unsigned long v9;  // 4129

    if (!ptr->field_28)
        return;
    v0 = ptr->field_44;
    if (!((char)(v0 >> 31) & 1))
    {
        v1 = ptr->field_10;
        if (!v1)
            sub_f7db74(v1);
        v2 = GamepadManager_Gamepad__GetInternalKeyState(v1, v0) & 4294967295;
    }
    else
    {
        v2 = 0;
    }
    v3 = ptr->field_40;
    v4 = 0;
    if (!((char)(v3 >> 31) & 1))
    {
        v1 = ptr->field_10;
        if (!v1)
            sub_f7db74(v1);
        GamepadManager_Gamepad__GetInternalAxisAnalog(v1, v3);
        if (!ptr->field_48)
            v6 = -(v5);
        v7 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(v6, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v6, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v6, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v6, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v6, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v6, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if (!((char)v7))
            v4 = [D] unsupported_Iop_ZeroHI96ofV128();
    }
    v8 = ptr->field_2c;
    v9 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v8, v4)) >> 5 & 3 | (unsigned long long)(CmpF(v8, v4) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v8, v4)) >> 5 & 3 | (unsigned long long)(CmpF(v8, v4) & 1)) & ((unsigned long long)(char)(CmpF(v8, v4)) >> 5 & 3 | (unsigned long long)(CmpF(v8, v4) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if (!((char)v9))
        ptr->field_2c = [D] unsupported_Iop_ZeroHI96ofV128();
    if (!((char)v2 & 1))
        return;
    ptr->field_30 = 1;
    return;
}
```

## `GamepadManager.Gamepad.KeyState.SyncDigital` — RVA `0xc2e8e0`

- Decompiled symbol: `GamepadManager_Gamepad_KeyState_SyncDigital`
- Metadata signature: `public void SyncDigital(DigitalBinding bind, InputRig rig) { }`
- Native interval: `52` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[61];
    char field_3d;
} struct_0;

struct_0 * GamepadManager_Gamepad_KeyState_SyncDigital(struct_0 *a0, long long a1, unsigned long a2)
{
    unsigned long long v0;  // x0

    if (!a0->field_3d)
        return a0;
    if (a1)
    {
        v0 = DigitalBinding__Sync(a1, 1);
        return DigitalBinding__Sync(a1, 1);
    }
    sub_f7db74(a1);
}
```

## `GamepadManager.Gamepad.KeyState.SyncAnalog` — RVA `0xc2e914`

- Decompiled symbol: `GamepadManager_Gamepad_KeyState_SyncAnalog`
- Metadata signature: `public void SyncAnalog(AxisBinding bind, InputRig rig) { }`
- Native interval: `96` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[60];
    char field_3c;
} struct_0;

long long GamepadManager_Gamepad_KeyState_SyncAnalog(struct_0 *a0, long long a1, unsigned long a2)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x21
    unsigned long long v4;  // x0
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x18]

    v0 = v2;
    v1 = v3;
    if (a1)
    {
        AxisBinding__SyncFloat(a1, 1);
        v4 = AxisBinding__SyncFloat();
        return AxisBinding__SyncFloat();
    }
    sub_f7db74();
}
```
