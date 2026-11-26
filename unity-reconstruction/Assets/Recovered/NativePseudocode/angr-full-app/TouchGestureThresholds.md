# Native pseudocode: TouchGestureThresholds

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `TouchGestureThresholds.Recalc` — RVA `0xc6269c`

- Decompiled symbol: `TouchGestureThresholds_Recalc`
- Metadata signature: `public void Recalc(float dpi) { }`
- Native interval: `68` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    struct struct_0 *field_0;
    char padding_8[76];
    unsigned int field_54;
} struct_1;

typedef struct struct_0 {
    char padding_0[376];
    unsigned long long field_178;
} struct_0;

struct_1 * TouchGestureThresholds_Recalc(struct_1 *ptr)
{
    unsigned int v0;  // s2
    unsigned int v1;  // s1
    unsigned int v2;  // s0
    unsigned long v3;  // 4140
    unsigned int v4;  // s0
    unsigned long long v5;  // 4102
    struct_0 *v6;  // x8

    v0 = ptr->field_54;
    v1 = 0x42c00000;
    v3 = arm64g_calculate_condition(128, (((((unsigned long long)(char)(CmpF(v2, 953267991)) >> 5 & 3 | (unsigned long long)(CmpF(v2, 953267991) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v2, 953267991)) >> 5 & 3 | (unsigned long long)(CmpF(v2, 953267991) & 1)) & ((unsigned long long)(char)(CmpF(v2, 953267991)) >> 5 & 3 | (unsigned long long)(CmpF(v2, 953267991) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if ((char)v3)
        v4 = v2;
    else
        v4 = v1;
    v5 = (((CmpF(v0, v4) >> 5 & 3 | CmpF(v0, v4) & 1) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - ((CmpF(v0, v4) >> 5 & 3 | CmpF(v0, v4) & 1) & (CmpF(v0, v4) >> 5 & 3 | CmpF(v0, v4) & 1) >> 1 & 1);
    if ((char)(v5 * 0x10000000 >> 30))
        return ptr;
    v6 = ptr->field_0;
    ptr->field_54 = v4;
    goto v6->field_178;
}
```

## `TouchGestureThresholds.get_tapMoveThreshPxSq` — RVA `0xc630a0`

- Decompiled symbol: `TouchGestureThresholds_get_tapMoveThreshPxSq`
- Metadata signature: `public float get_tapMoveThreshPxSq() { }`
- Native interval: `12` bytes
- Result: `pseudocode`

```c
long long TouchGestureThresholds_get_tapMoveThreshPxSq(unsigned long a0)
{
    return a0;
}
```

## `TouchGestureThresholds.get_dragThreshPxSq` — RVA `0xc63118`

- Decompiled symbol: `TouchGestureThresholds_get_dragThreshPxSq`
- Metadata signature: `public float get_dragThreshPxSq() { }`
- Native interval: `12` bytes
- Result: `pseudocode`

```c
long long TouchGestureThresholds_get_dragThreshPxSq(unsigned long a0)
{
    return a0;
}
```

## `TouchGestureThresholds.get_swipeSegLenPxSq` — RVA `0xc63124`

- Decompiled symbol: `TouchGestureThresholds_get_swipeSegLenPxSq`
- Metadata signature: `public float get_swipeSegLenPxSq() { }`
- Native interval: `12` bytes
- Result: `pseudocode`

```c
long long TouchGestureThresholds_get_swipeSegLenPxSq(unsigned long a0)
{
    return a0;
}
```

## `TouchGestureThresholds.get_tapPosThreshPxSq` — RVA `0xc631d4`

- Decompiled symbol: `TouchGestureThresholds_get_tapPosThreshPxSq`
- Metadata signature: `public float get_tapPosThreshPxSq() { }`
- Native interval: `12` bytes
- Result: `pseudocode`

```c
long long TouchGestureThresholds_get_tapPosThreshPxSq(unsigned long a0)
{
    return a0;
}
```

## `TouchGestureThresholds.get_tapMoveThreshPx` — RVA `0xc63224`

- Decompiled symbol: `TouchGestureThresholds_get_tapMoveThreshPx`
- Metadata signature: `public float get_tapMoveThreshPx() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long TouchGestureThresholds_get_tapMoveThreshPx(unsigned long a0)
{
    return a0;
}
```

## `TouchGestureThresholds.get_tapPosThreshPx` — RVA `0xc6322c`

- Decompiled symbol: `TouchGestureThresholds_get_tapPosThreshPx`
- Metadata signature: `public float get_tapPosThreshPx() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long TouchGestureThresholds_get_tapPosThreshPx(unsigned long a0)
{
    return a0;
}
```

## `TouchGestureThresholds.get_dragThreshPx` — RVA `0xc63234`

- Decompiled symbol: `TouchGestureThresholds_get_dragThreshPx`
- Metadata signature: `public float get_dragThreshPx() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long TouchGestureThresholds_get_dragThreshPx(unsigned long a0)
{
    return a0;
}
```

## `TouchGestureThresholds.get_swipeSegLenPx` — RVA `0xc6323c`

- Decompiled symbol: `TouchGestureThresholds_get_swipeSegLenPx`
- Metadata signature: `public float get_swipeSegLenPx() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long TouchGestureThresholds_get_swipeSegLenPx(unsigned long a0)
{
    return a0;
}
```

## `TouchGestureThresholds.get_swipeJoystickRadPx` — RVA `0xc63244`

- Decompiled symbol: `TouchGestureThresholds_get_swipeJoystickRadPx`
- Metadata signature: `public float get_swipeJoystickRadPx() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long TouchGestureThresholds_get_swipeJoystickRadPx(unsigned long a0)
{
    return a0;
}
```

## `TouchGestureThresholds.get_swipeJoystickRadPxSq` — RVA `0xc6324c`

- Decompiled symbol: `TouchGestureThresholds_get_swipeJoystickRadPxSq`
- Metadata signature: `public float get_swipeJoystickRadPxSq() { }`
- Native interval: `12` bytes
- Result: `pseudocode`

```c
long long TouchGestureThresholds_get_swipeJoystickRadPxSq(unsigned long a0)
{
    return a0;
}
```

## `TouchGestureThresholds.get_scrollThreshPx` — RVA `0xc63258`

- Decompiled symbol: `TouchGestureThresholds_get_scrollThreshPx`
- Metadata signature: `public float get_scrollThreshPx() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long TouchGestureThresholds_get_scrollThreshPx(unsigned long a0)
{
    return a0;
}
```

## `TouchGestureThresholds.get_scrollThreshPxSq` — RVA `0xc63260`

- Decompiled symbol: `TouchGestureThresholds_get_scrollThreshPxSq`
- Metadata signature: `public float get_scrollThreshPxSq() { }`
- Native interval: `12` bytes
- Result: `pseudocode`

```c
long long TouchGestureThresholds_get_scrollThreshPxSq(unsigned long a0)
{
    return a0;
}
```

## `TouchGestureThresholds.ctor` — RVA `0xc6326c`

- Decompiled symbol: `TouchGestureThresholds_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `76` bytes
- Result: `pseudocode`
- Heuristic layout hint: `TouchGestureThresholds_Recovered` matched 5 offsets against `TouchGestureThresholds` metadata (confidence 1.00).

```c
typedef struct TouchGestureThresholds_Recovered {
    char padding_0[16];
    uint128_t tapMoveThreshCm;
    uint128_t scrollMagnetFactor;
    uint128_t multiTapMaxTimeGap;
    uint128_t _tapPosThreshPx;
    unsigned long long _scrollThreshPx;
} TouchGestureThresholds_Recovered;

void TouchGestureThresholds_ctor(struct_0 *ptr)
{
    Object__ctor();
    ptr->field_50 = 0xbf80000041f00000;
    ptr->field_10 = 83741363753792513111313540018386816205;
    ptr->field_20 = 83209672587556668030134433567598234829;
    ptr->field_30 = 86565973245144944351055475090224106701;
    ptr->field_40 = 0x41700000412000004120000041f00000;
    return;
}
```

## `TouchGestureThresholds.OnRecalc` — RVA `0xc632b8`

- Decompiled symbol: `TouchGestureThresholds_OnRecalc`
- Metadata signature: `protected virtual void OnRecalc(float dpcm) { }`
- Native interval: `72` bytes
- Result: `pseudocode`
- Heuristic layout hint: `TouchGestureThresholds_Recovered` matched 4 offsets against `TouchGestureThresholds` metadata (confidence 1.00).

```c
typedef struct TouchGestureThresholds_Recovered {
    char padding_0[60];
    unsigned long long _tapMoveThreshPx;
    unsigned int _dragThreshPx;
    unsigned long long _swipeSegLenPx;
    unsigned int _scrollThreshPx;
} TouchGestureThresholds_Recovered;

struct_0 * TouchGestureThresholds_OnRecalc(struct_0 *ptr)
{
    unsigned long v1;  // d3
    unsigned int v2;  // s2
    unsigned int v3;  // s0

    v1 = [D] unsupported_Iop_ZeroHI64ofV128();
    v2 = [D] unsupported_Iop_ZeroHI96ofV128();
    v3 = [D] unsupported_Iop_ZeroHI96ofV128();
    *((long long *)&(&ptr->padding_0)[1]) = [D] unsupported_Iop_ZeroHI64ofV128();
    *((unsigned int *)((char *)&ptr->field_3c + 4)) = v2;
    *((unsigned long *)&ptr->field_44) = v1;
    *((unsigned int *)&ptr->field_48) = v3;
    return ptr;
}
```
