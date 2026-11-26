# Native pseudocode: GamepadManager.Gamepad.JoyState

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `GamepadManager.Gamepad.JoyState.ctor` — RVA `0xc2d97c`

- Decompiled symbol: `GamepadManager_Gamepad_JoyState_ctor`
- Metadata signature: `public void .ctor(GamepadManager.Gamepad gamepad, JoystickConfig config) { }`
- Native interval: `152` bytes
- Result: `pseudocode`
- Heuristic layout hint: `GamepadManager_Gamepad_JoyState_Recovered` matched 3 offsets against `GamepadManager.Gamepad.JoyState` metadata (confidence 1.00).

```c
typedef struct GamepadManager_Gamepad_JoyState_Recovered {
    char padding_0[16];
    long long gamepad;
    long long state;
    char isConnectedToHardware;
} GamepadManager_Gamepad_JoyState_Recovered;

extern long long g_1ef0550;
extern char g_1fab11b;

long long GamepadManager_Gamepad_JoyState_ctor(struct_0 *ptr, long long a1, long long a2)
{
    long long v0;  // x21
    struct_0 *p;  // x19
    unsigned long v2;  // x0

    if (!(g_1fab11b & 1))
    {
        sub_f7d92c(&g_1ef0550);
        g_1fab11b = 1;
    }
    Object__ctor(ptr, 0);
    ptr->field_10 = a1;
    sub_f7d8d0((struct GamepadManager_Gamepad_JoyState_Recovered *)&ptr->field_10, a1);
    v0 = sub_f7db70(g_1ef0550);
    JoystickState__ctor(v0, a2, 0);
    ptr->field_18 = v0;
    p = &ptr->field_18;
    v2 = sub_f7d8d0(p, v0);
    p->padding_0[8] = 0;
    return v2;
}
```

## `GamepadManager.Gamepad.JoyState.SetConfig` — RVA `0xc2db18`

- Decompiled symbol: `GamepadManager_Gamepad_JoyState_SetConfig`
- Metadata signature: `public void SetConfig(JoystickConfig config) { }`
- Native interval: `28` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[24];
    struct struct_0 *field_18;
} struct_1;

typedef struct struct_0 {
    char padding_0[16];
    unsigned long long field_10;
} struct_0;

void GamepadManager_Gamepad_JoyState_SetConfig(struct_1 *idx, unsigned long a1, unsigned long a2)
{
    unsigned long long v1;  // x30
    unsigned long long v0;  // [bp-0x10]

    v0 = v1;
    if (idx->field_18)
    {
        idx->field_18->field_10 = a1;
        sub_f7d8d0();
        return;
    }
    sub_f7db74(0);
}
```

## `GamepadManager.Gamepad.JoyState.ConnectToJoy` — RVA `0xc2dccc`

- Decompiled symbol: `GamepadManager_Gamepad_JoyState_ConnectToJoy`
- Metadata signature: `public void ConnectToJoy(GamepadProfile.JoystickSource joySrc) { }`
- Native interval: `188` bytes
- Result: `pseudocode`
- Heuristic layout hint: `GamepadManager_Gamepad_JoyState_Recovered` matched 14 offsets against `GamepadManager.Gamepad.JoyState` metadata (confidence 1.00).

```c
typedef struct struct_4 {
    char padding_0[16];
    struct struct_0 *field_10;
    struct struct_1 *field_18;
    struct struct_2 *field_20;
    struct struct_3 *field_28;
} struct_4;

typedef struct GamepadManager_Gamepad_JoyState_Recovered {
    char padding_0[24];
    struct GamepadManager_Gamepad_JoyState_Recovered *state;
    char isConnectedToHardware;
    char padding_21[3];
    unsigned int srcAxisIdL;
    unsigned int srcAxisIdR;
    unsigned int srcAxisIdU;
    unsigned int srcAxisIdD;
    char srcAxisFlipL;
    char srcAxisFlipR;
    char srcAxisFlipU;
    char srcAxisFlipD;
    unsigned int srcKeyU;
    unsigned int srcKeyR;
    unsigned int srcKeyD;
    unsigned int srcKeyL;
} GamepadManager_Gamepad_JoyState_Recovered;

typedef struct struct_3 {
    char padding_0[16];
    unsigned int field_10;
    unsigned int field_14;
    char field_18;
} struct_3;

typedef struct struct_2 {
    char padding_0[16];
    unsigned int field_10;
    unsigned int field_14;
    char field_18;
} struct_2;

typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
    unsigned int field_14;
    char field_18;
} struct_0;

typedef struct struct_1 {
    char padding_0[16];
    unsigned int field_10;
    unsigned int field_14;
    char field_18;
} struct_1;

long long GamepadManager_Gamepad_JoyState_ConnectToJoy(struct_5 *cur, struct_4 *ptr)
{
    char v0;  // x8
    struct_3 *pos;  // x8
    struct_2 *off;  // x9
    struct_0 *idx4;  // x10
    struct_1 *idx5;  // x11
    unsigned long long v5;  // x0

    if (!ptr)
        v0 = 0;
    else
        v0 = 1;
    cur->field_20 = v0;
    if (ptr)
    {
        pos = ptr->field_28;
        if (!pos)
            sub_f7db74(cur);
        cur->field_24 = pos->field_14;
        cur->field_34 = pos->field_18 ^ 1;
        off = ptr->field_20;
        if (!off)
            sub_f7db74(cur);
        cur->field_28 = off->field_14;
        cur->field_35 = off->field_18 ^ 1;
        idx4 = ptr->field_10;
        if (!idx4)
            sub_f7db74(cur);
        cur->field_2c = idx4->field_14;
        cur->field_36 = idx4->field_18 ^ 1;
        idx5 = ptr->field_18;
        if (!idx5)
            sub_f7db74(cur);
        cur->field_30 = idx5->field_14;
        cur->field_37 = idx5->field_18 ^ 1;
        cur->field_44 = pos->field_10;
        cur->field_3c = off->field_10;
        cur->field_38 = idx4->field_10;
        cur->field_40 = idx5->field_10;
    }
    cur = cur->field_18;
    if (cur)
    {
        v5 = JoystickState__Reset(cur, 0);
        return JoystickState__Reset(cur, 0);
    }
    sub_f7db74(cur);
}
```

## `GamepadManager.Gamepad.JoyState.Reset` — RVA `0xc2de58`

- Decompiled symbol: `GamepadManager_Gamepad_JoyState_Reset`
- Metadata signature: `public void Reset() { }`
- Native interval: `28` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    long long field_18;
} struct_0;

long long GamepadManager_Gamepad_JoyState_Reset(struct_0 *a0)
{
    unsigned long long v0;  // x0

    if (a0->field_18)
    {
        v0 = JoystickState__Reset(a0->field_18, 0);
        return JoystickState__Reset(a0->field_18, 0);
    }
    sub_f7db74(0);
}
```

## `GamepadManager.Gamepad.JoyState.Update` — RVA `0xc2e4cc`

- Decompiled symbol: `GamepadManager_Gamepad_JoyState_Update`
- Metadata signature: `public void Update() { }`
- Native interval: `36` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    long long field_18;
} struct_0;

long long GamepadManager_Gamepad_JoyState_Update(struct_0 *a0)
{
    unsigned long long v0;  // x0

    GamepadManager_Gamepad_JoyState__ReadHardwareState();
    if (a0->field_18)
    {
        v0 = JoystickState__Update(a0->field_18, 0);
        return JoystickState__Update(a0->field_18, 0);
    }
    sub_f7db74(0);
}
```

## `GamepadManager.Gamepad.JoyState.ReadHardwareState` — RVA `0xc2e5e8`

- Decompiled symbol: `GamepadManager_Gamepad_JoyState_ReadHardwareState`
- Metadata signature: `private void ReadHardwareState() { }`
- Native interval: `336` bytes
- Result: `pseudocode`
- Heuristic layout hint: `GamepadManager_Gamepad_JoyState_Recovered` matched 15 offsets against `GamepadManager.Gamepad.JoyState` metadata (confidence 1.00).

```c
typedef struct GamepadManager_Gamepad_JoyState_Recovered {
    char padding_0[16];
    unsigned long long gamepad;
    unsigned long long state;
    char isConnectedToHardware;
    char padding_21[3];
    unsigned int srcAxisIdL;
    unsigned int srcAxisIdR;
    unsigned int srcAxisIdU;
    unsigned int srcAxisIdD;
    char srcAxisFlipL;
    char srcAxisFlipR;
    char srcAxisFlipU;
    char srcAxisFlipD;
    unsigned int srcKeyU;
    unsigned int srcKeyR;
    unsigned int srcKeyD;
    unsigned int srcKeyL;
} GamepadManager_Gamepad_JoyState_Recovered;

extern long long g_1ef22b8;
extern char g_1fab1e0;

struct_0 * GamepadManager_Gamepad_JoyState_ReadHardwareState(struct_0 *ptr)
{
    unsigned long v0;  // x1
    unsigned long long v1;  // x0
    unsigned int v2;  // w20
    unsigned long v3;  // x1
    unsigned int v4;  // w21
    unsigned long v5;  // x1
    unsigned int v6;  // w22
    unsigned long v7;  // x1
    unsigned int v8;  // w23
    unsigned long long v9;  // x0

    if (!ptr->field_20)
        return ptr;
    if (!g_1fab1e0)
    {
        sub_f7d92c(&g_1ef22b8);
        g_1fab1e0 = 1;
    }
    GamepadManager_Gamepad_JoyState__GetCompositeAnalogVal(ptr, ptr->field_28, ptr->field_35, ptr->field_24, ptr->field_34);
    GamepadManager_Gamepad_JoyState__GetCompositeAnalogVal(ptr, ptr->field_2c, ptr->field_36, ptr->field_30, ptr->field_37);
    v0 = ptr->field_38;
    if (((char)(v0 >> 31) & 1))
    {
        v2 = 0;
        goto LABEL_102e688;
    }
    v1 = ptr->field_10;
    if (v1)
    {
        v2 = GamepadManager_Gamepad__GetInternalKeyState(v1, v0);
LABEL_102e688:
        v3 = ptr->field_40;
        if (((char)(v3 >> 31) & 1))
        {
            v4 = 0;
            goto LABEL_102e6a8;
        }
        v1 = ptr->field_10;
        if (v1)
        {
            v4 = GamepadManager_Gamepad__GetInternalKeyState(v1, v3);
LABEL_102e6a8:
            v5 = ptr->field_3c;
            if (!((char)(v5 >> 31) & 1))
            {
                v1 = ptr->field_10;
                if (v1)
                {
                    v6 = GamepadManager_Gamepad__GetInternalKeyState(v1, v5);
LABEL_102e6c8:
                    v7 = ptr->field_44;
                    if (!((char)(v7 >> 31) & 1))
                    {
                        v1 = ptr->field_10;
                        if (v1)
                        {
                            v8 = GamepadManager_Gamepad__GetInternalKeyState(v1, v7);
                            goto LABEL_102e6e8;
                        }
                    }
                    else
                    {
                        v8 = 0;
LABEL_102e6e8:
                        v1 = ptr->field_18;
                        if (v1)
                        {
                            JoystickState__ApplyClampedVec(v1, 1, 0);
                            v1 = ptr->field_18;
                            if (v1)
                            {
                                v9 = JoystickState__ApplyDigital(v1, v2 & 1, v6 & 1, v4 & 1, v8 & 1, 0);
                                return JoystickState__ApplyDigital(v1, v2 & 1, v6 & 1, v4 & 1, v8 & 1, 0);
                            }
                        }
                    }
                }
            }
            else
            {
                v6 = 0;
                goto LABEL_102e6c8;
            }
        }
    }
    sub_f7db74(v1);
}
```

## `GamepadManager.Gamepad.JoyState.GetCompositeAnalogVal` — RVA `0xc2e738`

- Decompiled symbol: `GamepadManager_Gamepad_JoyState_GetCompositeAnalogVal`
- Metadata signature: `private float GetCompositeAnalogVal(int posAxisId, bool posFlip, int negAxisId, bool negFlip) { }`
- Native interval: `172` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned long long field_10;
} struct_0;

void GamepadManager_Gamepad_JoyState_GetCompositeAnalogVal(struct_0 *ptr, unsigned long long a1, unsigned int a2, unsigned int a3, unsigned int a4)
{
    unsigned long long v0;  // x0
    unsigned long long v1;  // x22
    unsigned int v8;  // s0
    unsigned long v9;  // 4133
    unsigned long v10;  // 4133
    unsigned long v2;  // 4116
    unsigned int v3;  // s0
    unsigned int v5;  // s8
    unsigned int v6;  // s8
    unsigned long v7;  // 4116

    v0 = ptr->field_10;
    if (v0)
    {
        v1 = a1 & 4294967295;
        GamepadManager_Gamepad__GetInternalAxisAnalog(v0, a1);
        v2 = arm64g_calculate_condition(25, (unsigned long long)(a2 & 1), 0, 0);
        if ((char)v2)
            v5 = -(v3);
        else
            v5 = v3;
        v6 = v5;
        if (!((char)(v1 >> 31) & 1) && (unsigned int)v1 == a3)
            return;
        v0 = ptr->field_10;
        if (v0)
        {
            GamepadManager_Gamepad__GetInternalAxisAnalog(v0, a3);
            v7 = arm64g_calculate_condition(25, (unsigned long long)(a4 & 1), 0, 0);
            if ((char)v7)
                v8 = -(v3);
            v9 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v6, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v6, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v6, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v6, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v6, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v6, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
            v10 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v8, 0xbf800000)) >> 5 & 3 | (unsigned long long)(CmpF(v8, 0xbf800000) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v8, 0xbf800000)) >> 5 & 3 | (unsigned long long)(CmpF(v8, 0xbf800000) & 1)) & ((unsigned long long)(char)(CmpF(v8, 0xbf800000)) >> 5 & 3 | (unsigned long long)(CmpF(v8, 0xbf800000) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
            return;
        }
    }
    sub_f7db74(v0);
}
```

## `GamepadManager.Gamepad.JoyState.SyncJoyState` — RVA `0xc2e7e4`

- Decompiled symbol: `GamepadManager_Gamepad_JoyState_SyncJoyState`
- Metadata signature: `public void SyncJoyState(JoystickStateBinding bind, InputRig rig) { }`
- Native interval: `36` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    long long field_18;
} struct_0;

long long GamepadManager_Gamepad_JoyState_SyncJoyState(struct_0 *a0, long long a1, unsigned long a2)
{
    unsigned long long v0;  // x0

    if (a1)
    {
        v0 = JoystickStateBinding__SyncJoyState(a1, a0->field_18);
        return JoystickStateBinding__SyncJoyState(a1, a0->field_18);
    }
    sub_f7db74();
}
```
