# Native pseudocode: GamepadManager.Gamepad.InternalAxisState

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `GamepadManager.Gamepad.InternalAxisState.ctor` — RVA `0xc2d8e8`

- Decompiled symbol: `GamepadManager_Gamepad_InternalAxisState_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `112` bytes
- Result: `pseudocode`
- Heuristic layout hint: `GamepadManager_Gamepad_InternalAxisState_Recovered` matched 4 offsets against `GamepadManager.Gamepad.InternalAxisState` metadata (confidence 1.00).

```c
typedef struct GamepadManager_Gamepad_InternalAxisState_Recovered {
    char padding_0[16];
    long long axisName;
    unsigned long long valCur;
    char isReadyToUse;
    char trueAnalogRange;
} GamepadManager_Gamepad_InternalAxisState_Recovered;

extern char g_1fab11c;

long long GamepadManager_Gamepad_InternalAxisState_ctor(struct_2 *ptr)
{
    long long v0;  // x1
    struct_2 *p;  // x19
    unsigned long v2;  // x0

    if (!(g_1fab11c & 1))
    {
        sub_f7d92c("MT");
        g_1fab11c = 1;
    }
    Object__ctor(ptr, 0);
    ptr->field_20 = 0;
    ptr->field_18 = 0;
    v0 = g_1ef18f0->field_b8->field_0;
    ptr->field_10 = v0;
    p = &ptr->field_10;
    v2 = sub_f7d8d0(p, v0);
    *((char *)&p->field_10 + 1) = 0;
    return v2;
}
```

## `GamepadManager.Gamepad.InternalAxisState.ConnectToHardwareAxis` — RVA `0xc2db34`

- Decompiled symbol: `GamepadManager_Gamepad_InternalAxisState_ConnectToHardwareAxis`
- Metadata signature: `public void ConnectToHardwareAxis(int joyId, int axisId) { }`
- Native interval: `52` bytes
- Result: `pseudocode`
- Heuristic layout hint: `GamepadManager_Gamepad_InternalAxisState_Recovered` matched 3 offsets against `GamepadManager.Gamepad.InternalAxisState` metadata (confidence 1.00).

```c
typedef struct GamepadManager_Gamepad_InternalAxisState_Recovered {
    char padding_0[16];
    long long axisName;
    unsigned long long valCur;
    unsigned short isReadyToUse;
} GamepadManager_Gamepad_InternalAxisState_Recovered;

long long GamepadManager_Gamepad_InternalAxisState_ConnectToHardwareAxis(struct_0 *p, unsigned int a1, unsigned int a2)
{
    long long v0;  // x0
    struct_0 *ptr;  // x19
    unsigned long v2;  // x0

    v0 = GamepadManager__GetJoyAxisName(a1, a2);
    p->field_10 = v0;
    ptr = &p->field_10;
    v2 = sub_f7d8d0(ptr, v0);
    *((unsigned short *)&ptr->field_10) = 0;
    *((unsigned long long *)&ptr->padding_0[8]) = 0;
    return v2;
}
```

## `GamepadManager.Gamepad.InternalAxisState.Reset` — RVA `0xc2de88`

- Decompiled symbol: `GamepadManager_Gamepad_InternalAxisState_Reset`
- Metadata signature: `public void Reset() { }`
- Native interval: `12` bytes
- Result: `pseudocode`
- Heuristic layout hint: `GamepadManager_Gamepad_InternalAxisState_Recovered` matched 2 offsets against `GamepadManager.Gamepad.InternalAxisState` metadata (confidence 1.00).

```c
typedef struct GamepadManager_Gamepad_InternalAxisState_Recovered {
    char padding_0[24];
    unsigned long long valCur;
    unsigned short isReadyToUse;
} GamepadManager_Gamepad_InternalAxisState_Recovered;

struct_0 * GamepadManager_Gamepad_InternalAxisState_Reset(struct_0 *ptr)
{
    ptr->field_20 = 0;
    ptr->field_18 = 0;
    return ptr;
}
```

## `GamepadManager.Gamepad.InternalAxisState.GetVal` — RVA `0xc2e160`

- Decompiled symbol: `GamepadManager_Gamepad_InternalAxisState_GetVal`
- Metadata signature: `public float GetVal() { }`
- Native interval: `24` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[32];
    char field_20;
} struct_0;

struct_0 * GamepadManager_Gamepad_InternalAxisState_GetVal(struct_0 *a0)
{
    if (!a0->field_20)
        return a0;
    return a0;
}
```

## `GamepadManager.Gamepad.InternalAxisState.GetDigital` — RVA `0xc2e1ec`

- Decompiled symbol: `GamepadManager_Gamepad_InternalAxisState_GetDigital`
- Metadata signature: `public int GetDigital() { }`
- Native interval: `60` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: Decompiler produced no C-like text

```c
// 0x102e1ec: ldrb w8, [x0, #0x20]
// 0x102e1f0: cbz w8, #0x102e218
// 0x102e1f4: ldr s0, [x0, #0x18]
// 0x102e1f8: fmov s2, #0.50000000
// 0x102e1fc: fabs s1, s0
// 0x102e200: fcmp s1, s2
// 0x102e204: b.le #0x102e218
// 0x102e208: fcmp s0, #0.0
// 0x102e20c: b.le #0x102e220
// 0x102e210: mov w0, #1
// 0x102e214: ret
// 0x102e218: mov w0, wzr
// 0x102e21c: ret
// 0x102e220: mov w0, #-1
// 0x102e224: ret
```

## `GamepadManager.Gamepad.InternalAxisState.Update` — RVA `0xc2e488`

- Decompiled symbol: `GamepadManager_Gamepad_InternalAxisState_Update`
- Metadata signature: `public void Update() { }`
- Native interval: `68` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: Decompiler produced no C-like text

```c
// 0x102e488: stp x30, x19, [sp, #-0x10]!
// 0x102e48c: ldr s0, [x0, #0x18]
// 0x102e490: mov x19, x0
// 0x102e494: str s0, [x0, #0x1c]
// 0x102e498: bl #0x102e99c
// 0x102e49c: ldrb w8, [x19, #0x20]
// 0x102e4a0: cbnz w8, #0x102e4c4
// 0x102e4a4: ldr s0, [x19, #0x18]
// 0x102e4a8: adrp x8, #0x832000
// 0x102e4ac: ldr s1, [x8, #0x3b8]
// 0x102e4b0: fabs s0, s0
// 0x102e4b4: fcmp s0, s1
// 0x102e4b8: b.pl #0x102e4c4
// 0x102e4bc: mov w8, #1
// 0x102e4c0: strb w8, [x19, #0x20]
// 0x102e4c4: ldp x30, x19, [sp], #0x10
// 0x102e4c8: ret
```

## `GamepadManager.Gamepad.InternalAxisState.ReadHardwareState` — RVA `0xc2e99c`

- Decompiled symbol: `GamepadManager_Gamepad_InternalAxisState_ReadHardwareState`
- Metadata signature: `private void ReadHardwareState() { }`
- Native interval: `104` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: Decompiler produced no C-like text

```c
// 0x102e99c: stp x30, x19, [sp, #-0x10]!
// 0x102e9a0: mov x19, x0
// 0x102e9a4: ldr x0, [x0, #0x10]
// 0x102e9a8: mov x1, xzr
// 0x102e9ac: bl #0x17f6920
// 0x102e9b0: fmov s0, wzr
// 0x102e9b4: tbnz w0, #0, #0x102e9c4
// 0x102e9b8: ldr x0, [x19, #0x10]
// 0x102e9bc: mov x1, xzr
// 0x102e9c0: bl #0x1bc71a8
// 0x102e9c4: ldrb w8, [x19, #0x21]
// 0x102e9c8: str s0, [x19, #0x18]
// 0x102e9cc: cbnz w8, #0x102e9fc
// 0x102e9d0: adrp x8, #0x832000
// 0x102e9d4: ldr s1, [x8, #0x4e0]
// 0x102e9d8: fabs s0, s0
// 0x102e9dc: fcmp s0, s1
// 0x102e9e0: b.le #0x102e9fc
// 0x102e9e4: adrp x8, #0x832000
// 0x102e9e8: ldr s1, [x8, #0x38c]
// 0x102e9ec: fcmp s0, s1
// 0x102e9f0: b.pl #0x102e9fc
// 0x102e9f4: mov w8, #1
// 0x102e9f8: strb w8, [x19, #0x21]
// 0x102e9fc: ldp x30, x19, [sp], #0x10
// 0x102ea00: ret
```

## `GamepadManager.Gamepad.InternalAxisState.SetVal` — RVA `0xc2ea04`

- Decompiled symbol: `GamepadManager_Gamepad_InternalAxisState_SetVal`
- Metadata signature: `public void SetVal(float v) { }`
- Native interval: `64` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: Decompiler produced no C-like text

```c
// 0x102ea04: ldrb w8, [x0, #0x21]
// 0x102ea08: str s0, [x0, #0x18]
// 0x102ea0c: cbz w8, #0x102ea14
// 0x102ea10: ret
// 0x102ea14: adrp x8, #0x832000
// 0x102ea18: ldr s1, [x8, #0x4e0]
// 0x102ea1c: fabs s0, s0
// 0x102ea20: fcmp s0, s1
// 0x102ea24: b.le #0x102ea10
// 0x102ea28: adrp x8, #0x832000
// 0x102ea2c: ldr s1, [x8, #0x38c]
// 0x102ea30: fcmp s0, s1
// 0x102ea34: b.pl #0x102ea10
// 0x102ea38: mov w8, #1
// 0x102ea3c: strb w8, [x0, #0x21]
// 0x102ea40: ret
```

## `GamepadManager.Gamepad.InternalAxisState.IsFullyAnalog` — RVA `0xc2ea44`

- Decompiled symbol: `GamepadManager_Gamepad_InternalAxisState_IsFullyAnalog`
- Metadata signature: `public bool IsFullyAnalog() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[33];
    char field_21;
} struct_0;

long long GamepadManager_Gamepad_InternalAxisState_IsFullyAnalog(struct_0 *a0)
{
    return a0->field_21;
}
```
