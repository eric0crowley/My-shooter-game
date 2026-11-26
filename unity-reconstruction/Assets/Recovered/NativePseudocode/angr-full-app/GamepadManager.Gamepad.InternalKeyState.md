# Native pseudocode: GamepadManager.Gamepad.InternalKeyState

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `GamepadManager.Gamepad.InternalKeyState.ctor` — RVA `0xc2d958`

- Decompiled symbol: `GamepadManager_Gamepad_InternalKeyState_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `36` bytes
- Result: `pseudocode`
- Heuristic layout hint: `GamepadManager_Gamepad_InternalKeyState_Recovered` matched 3 offsets against `GamepadManager.Gamepad.InternalKeyState` metadata (confidence 1.00).

```c
typedef struct GamepadManager_Gamepad_InternalKeyState_Recovered {
    char padding_0[16];
    unsigned int key;
    char stateCur;
    char padding_15[1];
    char isReadyToUse;
} GamepadManager_Gamepad_InternalKeyState_Recovered;

void GamepadManager_Gamepad_InternalKeyState_ctor(struct_0 *ptr)
{
    Object__ctor();
    ptr->field_16 = 0;
    ptr->field_14 = 0;
    ptr->field_10 = 0;
    return;
}
```

## `GamepadManager.Gamepad.InternalKeyState.ConnectToHardwareKey` — RVA `0xc2db68`

- Decompiled symbol: `GamepadManager_Gamepad_InternalKeyState_ConnectToHardwareKey`
- Metadata signature: `public void ConnectToHardwareKey(int joyId, int keyId) { }`
- Native interval: `52` bytes
- Result: `pseudocode`
- Heuristic layout hint: `GamepadManager_Gamepad_InternalKeyState_Recovered` matched 3 offsets against `GamepadManager.Gamepad.InternalKeyState` metadata (confidence 1.00).

```c
typedef struct GamepadManager_Gamepad_InternalKeyState_Recovered {
    char padding_0[16];
    unsigned int key;
    unsigned short stateCur;
    char isReadyToUse;
} GamepadManager_Gamepad_InternalKeyState_Recovered;

struct_0 * GamepadManager_Gamepad_InternalKeyState_ConnectToHardwareKey(struct_0 *ptr, unsigned int a1, unsigned long long a2)
{
    unsigned int v0;  // w8

    v0 = 0;
    if (3 >= a1 && !((char)(a2 >> 31) & 1))
    {
        if ((unsigned int)a2 < 20)
            v0 = (unsigned int)a2 + 20 * a1 + 350;
        else
            v0 = 0;
    }
    ptr->field_10 = v0;
    ptr->field_14 = 0;
    ptr->field_16 = 0;
    return ptr;
}
```

## `GamepadManager.Gamepad.InternalKeyState.Reset` — RVA `0xc2de94`

- Decompiled symbol: `GamepadManager_Gamepad_InternalKeyState_Reset`
- Metadata signature: `public void Reset() { }`
- Native interval: `12` bytes
- Result: `pseudocode`
- Heuristic layout hint: `GamepadManager_Gamepad_InternalKeyState_Recovered` matched 2 offsets against `GamepadManager.Gamepad.InternalKeyState` metadata (confidence 1.00).

```c
typedef struct GamepadManager_Gamepad_InternalKeyState_Recovered {
    char padding_0[20];
    unsigned short stateCur;
    char isReadyToUse;
} GamepadManager_Gamepad_InternalKeyState_Recovered;

struct_0 * GamepadManager_Gamepad_InternalKeyState_Reset(struct_0 *ptr)
{
    ptr->field_14 = 0;
    ptr->field_16 = 0;
    return ptr;
}
```

## `GamepadManager.Gamepad.InternalKeyState.GetState` — RVA `0xc2e0f4`

- Decompiled symbol: `GamepadManager_Gamepad_InternalKeyState_GetState`
- Metadata signature: `public bool GetState() { }`
- Native interval: `32` bytes
- Result: `pseudocode`

```c
unsigned long long GamepadManager_Gamepad_InternalKeyState_GetState(char *a0)
{
    if (!a0[22])
    {
        return 0;
    }
    else if (!a0[20])
    {
        return 0;
    }
    else
    {
        return 1;
    }
}
```

## `GamepadManager.Gamepad.InternalKeyState.Update` — RVA `0xc2e444`

- Decompiled symbol: `GamepadManager_Gamepad_InternalKeyState_Update`
- Metadata signature: `public void Update() { }`
- Native interval: `68` bytes
- Result: `pseudocode`
- Heuristic layout hint: `GamepadManager_Gamepad_InternalKeyState_Recovered` matched 4 offsets against `GamepadManager.Gamepad.InternalKeyState` metadata (confidence 1.00).

```c
typedef struct GamepadManager_Gamepad_InternalKeyState_Recovered {
    char padding_0[16];
    unsigned int key;
    char stateCur;
    char statePrev;
    char isReadyToUse;
} GamepadManager_Gamepad_InternalKeyState_Recovered;

int GamepadManager_Gamepad_InternalKeyState_Update(struct_0 *ptr)
{
    unsigned long v0;  // x0
    unsigned int v1;  // w8

    v0 = ptr->field_10;
    ptr->field_15 = ptr->field_14;
    if ((unsigned int)v0)
        v0 = Input__GetKey(v0, 0);
    v1 = ptr->field_16;
    ptr->field_14 = (char)v0 & 1;
    if (!v1 && !((char)v0 & 1))
        ptr->field_16 = 1;
    return v0;
}
```

## `GamepadManager.Gamepad.InternalKeyState.ReadHardwareState` — RVA `0xc2e974`

- Decompiled symbol: `GamepadManager_Gamepad_InternalKeyState_ReadHardwareState`
- Metadata signature: `private void ReadHardwareState() { }`
- Native interval: `40` bytes
- Result: `pseudocode`
- Heuristic layout hint: `GamepadManager_Gamepad_InternalKeyState_Recovered` matched 2 offsets against `GamepadManager.Gamepad.InternalKeyState` metadata (confidence 1.00).

```c
typedef struct GamepadManager_Gamepad_InternalKeyState_Recovered {
    char padding_0[16];
    unsigned int key;
    char stateCur;
} GamepadManager_Gamepad_InternalKeyState_Recovered;

int GamepadManager_Gamepad_InternalKeyState_ReadHardwareState(struct_0 *ptr)
{
    unsigned long v0;  // x0

    v0 = ptr->field_10;
    if ((unsigned int)v0)
        v0 = Input__GetKey(v0, 0);
    ptr->field_14 = (char)v0 & 1;
    return v0;
}
```
