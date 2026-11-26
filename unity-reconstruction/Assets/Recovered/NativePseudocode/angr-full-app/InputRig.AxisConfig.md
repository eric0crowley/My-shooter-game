# Native pseudocode: InputRig.AxisConfig

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `InputRig.AxisConfig.get_frDigitalPos` — RVA `0xc40bdc`

- Decompiled symbol: `InputRig_AxisConfig_get_frDigitalPos`
- Metadata signature: `public bool get_frDigitalPos() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[207];
    char field_cf;
} struct_0;

long long InputRig_AxisConfig_get_frDigitalPos(struct_0 *a0)
{
    return a0->field_cf;
}
```

## `InputRig.AxisConfig.set_frDigitalPos` — RVA `0xc40be4`

- Decompiled symbol: `InputRig_AxisConfig_set_frDigitalPos`
- Metadata signature: `protected void set_frDigitalPos(bool value) { }`
- Native interval: `12` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[207];
    char field_cf;
} struct_0;

struct_0 * InputRig_AxisConfig_set_frDigitalPos(struct_0 *ptr, char a1)
{
    ptr->field_cf = a1 & 1;
    return ptr;
}
```

## `InputRig.AxisConfig.get_frDigitalNeg` — RVA `0xc40bf0`

- Decompiled symbol: `InputRig_AxisConfig_get_frDigitalNeg`
- Metadata signature: `public bool get_frDigitalNeg() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[208];
    char field_d0;
} struct_0;

long long InputRig_AxisConfig_get_frDigitalNeg(struct_0 *a0)
{
    return a0->field_d0;
}
```

## `InputRig.AxisConfig.set_frDigitalNeg` — RVA `0xc40bf8`

- Decompiled symbol: `InputRig_AxisConfig_set_frDigitalNeg`
- Metadata signature: `protected void set_frDigitalNeg(bool value) { }`
- Native interval: `12` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[208];
    char field_d0;
} struct_0;

struct_0 * InputRig_AxisConfig_set_frDigitalNeg(struct_0 *ptr, char a1)
{
    ptr->field_d0 = a1 & 1;
    return ptr;
}
```

## `InputRig.AxisConfig.get_frAnalogPos` — RVA `0xc40c04`

- Decompiled symbol: `InputRig_AxisConfig_get_frAnalogPos`
- Metadata signature: `public float get_frAnalogPos() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long InputRig_AxisConfig_get_frAnalogPos(unsigned long a0)
{
    return a0;
}
```

## `InputRig.AxisConfig.set_frAnalogPos` — RVA `0xc40c0c`

- Decompiled symbol: `InputRig_AxisConfig_set_frAnalogPos`
- Metadata signature: `protected void set_frAnalogPos(float value) { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[212];
    unsigned int field_d4;
} struct_0;

struct_0 * InputRig_AxisConfig_set_frAnalogPos(struct_0 *ptr)
{
    unsigned int v0;  // s0

    ptr->field_d4 = v0;
    return ptr;
}
```

## `InputRig.AxisConfig.get_frAnalogNeg` — RVA `0xc40c14`

- Decompiled symbol: `InputRig_AxisConfig_get_frAnalogNeg`
- Metadata signature: `public float get_frAnalogNeg() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long InputRig_AxisConfig_get_frAnalogNeg(unsigned long a0)
{
    return a0;
}
```

## `InputRig.AxisConfig.set_frAnalogNeg` — RVA `0xc40c1c`

- Decompiled symbol: `InputRig_AxisConfig_set_frAnalogNeg`
- Metadata signature: `protected void set_frAnalogNeg(float value) { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[216];
    unsigned int field_d8;
} struct_0;

struct_0 * InputRig_AxisConfig_set_frAnalogNeg(struct_0 *ptr)
{
    unsigned int v0;  // s0

    ptr->field_d8 = v0;
    return ptr;
}
```

## `InputRig.AxisConfig.get_frMouseDeltaPos` — RVA `0xc40c24`

- Decompiled symbol: `InputRig_AxisConfig_get_frMouseDeltaPos`
- Metadata signature: `public float get_frMouseDeltaPos() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long InputRig_AxisConfig_get_frMouseDeltaPos(unsigned long a0)
{
    return a0;
}
```

## `InputRig.AxisConfig.set_frMouseDeltaPos` — RVA `0xc40c2c`

- Decompiled symbol: `InputRig_AxisConfig_set_frMouseDeltaPos`
- Metadata signature: `protected void set_frMouseDeltaPos(float value) { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[220];
    unsigned int field_dc;
} struct_0;

struct_0 * InputRig_AxisConfig_set_frMouseDeltaPos(struct_0 *ptr)
{
    unsigned int v0;  // s0

    ptr->field_dc = v0;
    return ptr;
}
```

## `InputRig.AxisConfig.get_frMouseDeltaNeg` — RVA `0xc40c34`

- Decompiled symbol: `InputRig_AxisConfig_get_frMouseDeltaNeg`
- Metadata signature: `public float get_frMouseDeltaNeg() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long InputRig_AxisConfig_get_frMouseDeltaNeg(unsigned long a0)
{
    return a0;
}
```

## `InputRig.AxisConfig.set_frMouseDeltaNeg` — RVA `0xc40c3c`

- Decompiled symbol: `InputRig_AxisConfig_set_frMouseDeltaNeg`
- Metadata signature: `protected void set_frMouseDeltaNeg(float value) { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

struct_0 * InputRig_AxisConfig_set_frMouseDeltaNeg(struct_0 *ptr)
{
    unsigned int v0;  // s0

    ptr->field_e0 = v0;
    return ptr;
}
```

## `InputRig.AxisConfig.get_frTouchDeltaPos` — RVA `0xc40c44`

- Decompiled symbol: `InputRig_AxisConfig_get_frTouchDeltaPos`
- Metadata signature: `public float get_frTouchDeltaPos() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long InputRig_AxisConfig_get_frTouchDeltaPos(unsigned long a0)
{
    return a0;
}
```

## `InputRig.AxisConfig.set_frTouchDeltaPos` — RVA `0xc40c4c`

- Decompiled symbol: `InputRig_AxisConfig_set_frTouchDeltaPos`
- Metadata signature: `protected void set_frTouchDeltaPos(float value) { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[228];
    unsigned int field_e4;
} struct_0;

struct_0 * InputRig_AxisConfig_set_frTouchDeltaPos(struct_0 *ptr)
{
    unsigned int v0;  // s0

    ptr->field_e4 = v0;
    return ptr;
}
```

## `InputRig.AxisConfig.get_frTouchDeltaNeg` — RVA `0xc40c54`

- Decompiled symbol: `InputRig_AxisConfig_get_frTouchDeltaNeg`
- Metadata signature: `public float get_frTouchDeltaNeg() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long InputRig_AxisConfig_get_frTouchDeltaNeg(unsigned long a0)
{
    return a0;
}
```

## `InputRig.AxisConfig.set_frTouchDeltaNeg` — RVA `0xc40c5c`

- Decompiled symbol: `InputRig_AxisConfig_set_frTouchDeltaNeg`
- Metadata signature: `protected void set_frTouchDeltaNeg(float value) { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[232];
    unsigned int field_e8;
} struct_0;

struct_0 * InputRig_AxisConfig_set_frTouchDeltaNeg(struct_0 *ptr)
{
    unsigned int v0;  // s0

    ptr->field_e8 = v0;
    return ptr;
}
```

## `InputRig.AxisConfig.get_frNormalizedDeltaPos` — RVA `0xc40c64`

- Decompiled symbol: `InputRig_AxisConfig_get_frNormalizedDeltaPos`
- Metadata signature: `public float get_frNormalizedDeltaPos() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long InputRig_AxisConfig_get_frNormalizedDeltaPos(unsigned long a0)
{
    return a0;
}
```

## `InputRig.AxisConfig.set_frNormalizedDeltaPos` — RVA `0xc40c6c`

- Decompiled symbol: `InputRig_AxisConfig_set_frNormalizedDeltaPos`
- Metadata signature: `protected void set_frNormalizedDeltaPos(float value) { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[236];
    unsigned int field_ec;
} struct_0;

struct_0 * InputRig_AxisConfig_set_frNormalizedDeltaPos(struct_0 *ptr)
{
    unsigned int v0;  // s0

    ptr->field_ec = v0;
    return ptr;
}
```

## `InputRig.AxisConfig.get_frNormalizedDeltaNeg` — RVA `0xc40c74`

- Decompiled symbol: `InputRig_AxisConfig_get_frNormalizedDeltaNeg`
- Metadata signature: `public float get_frNormalizedDeltaNeg() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long InputRig_AxisConfig_get_frNormalizedDeltaNeg(unsigned long a0)
{
    return a0;
}
```

## `InputRig.AxisConfig.set_frNormalizedDeltaNeg` — RVA `0xc40c7c`

- Decompiled symbol: `InputRig_AxisConfig_set_frNormalizedDeltaNeg`
- Metadata signature: `protected void set_frNormalizedDeltaNeg(float value) { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[240];
    unsigned int field_f0;
} struct_0;

struct_0 * InputRig_AxisConfig_set_frNormalizedDeltaNeg(struct_0 *ptr)
{
    unsigned int v0;  // s0

    ptr->field_f0 = v0;
    return ptr;
}
```

## `InputRig.AxisConfig.get_frScrollDelta` — RVA `0xc40c84`

- Decompiled symbol: `InputRig_AxisConfig_get_frScrollDelta`
- Metadata signature: `public int get_frScrollDelta() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[244];
    unsigned int field_f4;
} struct_0;

int InputRig_AxisConfig_get_frScrollDelta(struct_0 *a0)
{
    return a0->field_f4;
}
```

## `InputRig.AxisConfig.set_frScrollDelta` — RVA `0xc40c8c`

- Decompiled symbol: `InputRig_AxisConfig_set_frScrollDelta`
- Metadata signature: `protected void set_frScrollDelta(int value) { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[244];
    unsigned int field_f4;
} struct_0;

struct_0 * InputRig_AxisConfig_set_frScrollDelta(struct_0 *ptr, unsigned int a1)
{
    ptr->field_f4 = a1;
    return ptr;
}
```

## `InputRig.AxisConfig.ctor` — RVA `0xc40c94`

- Decompiled symbol: `InputRig_AxisConfig_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `188` bytes
- Result: `pseudocode`
- Heuristic layout hint: `InputRig_AxisConfig_Recovered` matched 10 offsets against `InputRig.AxisConfig` metadata (confidence 0.83).

```c
typedef struct InputRig_AxisConfig_Recovered {
    struct struct_0 *field_0;
    char padding_8[8];
    long long field_10;
    unsigned long long axisType;
    char padding_20[4];
    unsigned int scale;
    char affectSourceKeys;
    char padding_29[11];
    unsigned int keyboardPositive;
    char padding_38[12];
    unsigned int keyboardNegative;
    char padding_48[12];
    uint128_t analogToDigitalThresh;
    unsigned int digitalToAnalogDecelTime;
    char digitalToScrollAutoRepeat;
    char padding_69[3];
    uint128_t digitalToScrollRepeatInterval;
    unsigned int scrollToDeltaSmoothingTime;
} InputRig_AxisConfig_Recovered;

typedef struct struct_0 {
    char padding_0[376];
    unsigned long long field_178;
} struct_0;

extern long long g_1f08948;
extern char g_1fab1f9;

void InputRig_AxisConfig_ctor(struct_1 *ptr)
{
    unsigned long long v4;  // x30
    unsigned long long v5;  // x21
    unsigned long long v6;  // x20
    unsigned long long v7;  // x19
    struct_0 *v8;  // x8
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x18]
    unsigned long long v2;  // [bp-0x10]
    unsigned long long v3;  // [bp-0x8]

    v0 = v4;
    v1 = v5;
    v2 = v6;
    v3 = v7;
    if (!(g_1fab1f9 & 1))
    {
        sub_f7d92c(&g_1f08948);
        g_1fab1f9 = 1;
    }
    Object__ctor(ptr, 0);
    ptr->field_10 = g_1f08948;
    sub_f7d8d0((struct InputRig_AxisConfig_Recovered *)&ptr->field_10, g_1f08948);
    *((unsigned int *)((char *)&ptr->field_54 + 4)) = 0x3e800000;
    ptr->field_18 = 4294967298;
    ptr->field_24 = 0x3f800000;
    *((uint128_t *)&(&ptr->padding_48)[1]) = 0x3e80000000000000000000003e000000;
    v8 = ptr->field_0;
    ptr->field_28 = 1;
    *((char *)&ptr->field_54 + 8) = 1;
    ptr->field_34 = 0;
    ptr->field_44 = 0;
    *((unsigned int *)&(&ptr->padding_69)[2 + 1]) = 1036831949;
    *((uint128_t *)((char *)&ptr->field_54 + 12)) = 0x3dcccccd3d4ccccd3f8000003f000000;
    goto v8->field_178;
}
```

## `InputRig.AxisConfig.CreateDigital` — RVA `0xc40d50`

- Decompiled symbol: `InputRig_AxisConfig_CreateDigital`
- Metadata signature: `public static InputRig.AxisConfig CreateDigital(string name, KeyCode key) { }`
- Native interval: `136` bytes
- Result: `pseudocode`
- Heuristic layout hint: `InputRig_AxisConfig_Recovered` matched 10 offsets against `InputRig.AxisConfig` metadata (confidence 0.83).

```c
typedef struct InputRig_AxisConfig_Recovered {
    struct struct_0 *field_0;
    char padding_8[8];
    long long field_10;
    unsigned long long axisType;
    char padding_20[4];
    unsigned int scale;
    char affectSourceKeys;
    char padding_29[11];
    unsigned int keyboardPositive;
    char padding_38[12];
    unsigned int keyboardNegative;
    char padding_48[12];
    char padding_54[12];
    uint128_t analogToDigitalThresh;
    unsigned int digitalToAnalogDecelTime;
    char digitalToScrollAutoRepeat;
    char padding_69[3];
    char padding_78[8];
    uint128_t digitalToScrollRepeatInterval;
    unsigned int scrollToDeltaSmoothingTime;
} InputRig_AxisConfig_Recovered;

typedef struct struct_0 {
    char padding_0[376];
    unsigned long long field_178;
} struct_0;

extern long long g_1ef3320;
extern char g_1fab1fa;

void InputRig_AxisConfig_CreateDigital(unsigned long a0, unsigned long a1)
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
    if (!(g_1fab1fa & 1))
    {
        sub_f7d92c(&g_1ef3320);
        g_1fab1fa = 1;
    }
    InputRig_AxisConfig__ctor(sub_f7db70(g_1ef3320)); /* do not return */
}
```

## `InputRig.AxisConfig.CreateScrollWheel` — RVA `0xc40dd8`

- Decompiled symbol: `InputRig_AxisConfig_CreateScrollWheel`
- Metadata signature: `public static InputRig.AxisConfig CreateScrollWheel(string name, KeyCode keyPositive, KeyCode keyNegative) { }`
- Native interval: `140` bytes
- Result: `pseudocode`
- Heuristic layout hint: `InputRig_AxisConfig_Recovered` matched 10 offsets against `InputRig.AxisConfig` metadata (confidence 0.83).

```c
typedef struct InputRig_AxisConfig_Recovered {
    struct struct_0 *field_0;
    char padding_8[8];
    long long field_10;
    unsigned long long axisType;
    char padding_20[4];
    unsigned int scale;
    char affectSourceKeys;
    char padding_29[11];
    unsigned int keyboardPositive;
    char padding_38[12];
    unsigned int keyboardNegative;
    char padding_48[12];
    char padding_54[12];
    uint128_t analogToDigitalThresh;
    unsigned int digitalToAnalogDecelTime;
    char digitalToScrollAutoRepeat;
    char padding_69[3];
    char padding_78[8];
    uint128_t digitalToScrollRepeatInterval;
    unsigned int scrollToDeltaSmoothingTime;
} InputRig_AxisConfig_Recovered;

typedef struct struct_0 {
    char padding_0[376];
    unsigned long long field_178;
} struct_0;

extern long long g_1ef3320;
extern char g_1fab1fb;

void InputRig_AxisConfig_CreateScrollWheel(unsigned long a0, unsigned long a1, unsigned long a2)
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
    if (!(g_1fab1fb & 1))
    {
        sub_f7d92c(&g_1ef3320);
        g_1fab1fb = 1;
    }
    InputRig_AxisConfig__ctor(sub_f7db70(g_1ef3320)); /* do not return */
}
```

## `InputRig.AxisConfig.CreateAnalog` — RVA `0xc40e64`

- Decompiled symbol: `InputRig_AxisConfig_CreateAnalog`
- Metadata signature: `public static InputRig.AxisConfig CreateAnalog(string name, KeyCode keyPositive) { }`
- Native interval: `132` bytes
- Result: `pseudocode`
- Heuristic layout hint: `InputRig_AxisConfig_Recovered` matched 10 offsets against `InputRig.AxisConfig` metadata (confidence 0.83).

```c
typedef struct InputRig_AxisConfig_Recovered {
    struct struct_0 *field_0;
    char padding_8[8];
    long long field_10;
    unsigned long long axisType;
    char padding_20[4];
    unsigned int scale;
    char affectSourceKeys;
    char padding_29[11];
    unsigned int keyboardPositive;
    char padding_38[12];
    unsigned int keyboardNegative;
    char padding_48[12];
    char padding_54[12];
    uint128_t analogToDigitalThresh;
    unsigned int digitalToAnalogDecelTime;
    char digitalToScrollAutoRepeat;
    char padding_69[3];
    char padding_78[8];
    uint128_t digitalToScrollRepeatInterval;
    unsigned int scrollToDeltaSmoothingTime;
} InputRig_AxisConfig_Recovered;

typedef struct struct_0 {
    char padding_0[376];
    unsigned long long field_178;
} struct_0;

extern long long g_1ef3320;
extern char g_1fab1fc;

void InputRig_AxisConfig_CreateAnalog(unsigned long a0, unsigned long a1)
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
    if (!(g_1fab1fc & 1))
    {
        sub_f7d92c(&g_1ef3320);
        g_1fab1fc = 1;
    }
    InputRig_AxisConfig__ctor(sub_f7db70(g_1ef3320)); /* do not return */
}
```

## `InputRig.AxisConfig.CreateSignedAnalog` — RVA `0xc40ee8`

- Decompiled symbol: `InputRig_AxisConfig_CreateSignedAnalog`
- Metadata signature: `public static InputRig.AxisConfig CreateSignedAnalog(string name, KeyCode keyPositive, KeyCode keyNegative) { }`
- Native interval: `140` bytes
- Result: `pseudocode`
- Heuristic layout hint: `InputRig_AxisConfig_Recovered` matched 10 offsets against `InputRig.AxisConfig` metadata (confidence 0.83).

```c
typedef struct InputRig_AxisConfig_Recovered {
    struct struct_0 *field_0;
    char padding_8[8];
    long long field_10;
    unsigned long long axisType;
    char padding_20[4];
    unsigned int scale;
    char affectSourceKeys;
    char padding_29[11];
    unsigned int keyboardPositive;
    char padding_38[12];
    unsigned int keyboardNegative;
    char padding_48[12];
    char padding_54[12];
    uint128_t analogToDigitalThresh;
    unsigned int digitalToAnalogDecelTime;
    char digitalToScrollAutoRepeat;
    char padding_69[3];
    char padding_78[8];
    uint128_t digitalToScrollRepeatInterval;
    unsigned int scrollToDeltaSmoothingTime;
} InputRig_AxisConfig_Recovered;

typedef struct struct_0 {
    char padding_0[376];
    unsigned long long field_178;
} struct_0;

extern long long g_1ef3320;
extern char g_1fab1fd;

void InputRig_AxisConfig_CreateSignedAnalog(unsigned long a0, unsigned long a1, unsigned long a2)
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
    if (!(g_1fab1fd & 1))
    {
        sub_f7d92c(&g_1ef3320);
        g_1fab1fd = 1;
    }
    InputRig_AxisConfig__ctor(sub_f7db70(g_1ef3320)); /* do not return */
}
```

## `InputRig.AxisConfig.CreateDelta` — RVA `0xc40f74`

- Decompiled symbol: `InputRig_AxisConfig_CreateDelta`
- Metadata signature: `public static InputRig.AxisConfig CreateDelta(string name, KeyCode keyPositive, KeyCode keyNegative) { }`
- Native interval: `140` bytes
- Result: `pseudocode`
- Heuristic layout hint: `InputRig_AxisConfig_Recovered` matched 10 offsets against `InputRig.AxisConfig` metadata (confidence 0.83).

```c
typedef struct InputRig_AxisConfig_Recovered {
    struct struct_0 *field_0;
    char padding_8[8];
    long long field_10;
    unsigned long long axisType;
    char padding_20[4];
    unsigned int scale;
    char affectSourceKeys;
    char padding_29[11];
    unsigned int keyboardPositive;
    char padding_38[12];
    unsigned int keyboardNegative;
    char padding_48[12];
    char padding_54[12];
    uint128_t analogToDigitalThresh;
    unsigned int digitalToAnalogDecelTime;
    char digitalToScrollAutoRepeat;
    char padding_69[3];
    char padding_78[8];
    uint128_t digitalToScrollRepeatInterval;
    unsigned int scrollToDeltaSmoothingTime;
} InputRig_AxisConfig_Recovered;

typedef struct struct_0 {
    char padding_0[376];
    unsigned long long field_178;
} struct_0;

extern long long g_1ef3320;
extern char g_1fab1fe;

void InputRig_AxisConfig_CreateDelta(unsigned long a0, unsigned long a1, unsigned long a2)
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
    if (!(g_1fab1fe & 1))
    {
        sub_f7d92c(&g_1ef3320);
        g_1fab1fe = 1;
    }
    InputRig_AxisConfig__ctor(sub_f7db70(g_1ef3320)); /* do not return */
}
```

## `InputRig.AxisConfig.Reset` — RVA `0xc41000`

- Decompiled symbol: `InputRig_AxisConfig_Reset`
- Metadata signature: `public override void Reset() { }`
- Native interval: `52` bytes
- Result: `pseudocode`
- Heuristic layout hint: `InputRig_AxisConfig_Recovered` matched 9 offsets against `InputRig.AxisConfig` metadata (confidence 1.00).

```c
typedef struct InputRig_AxisConfig_Recovered {
    char padding_0[128];
    unsigned long long valRaw;
    char padding_88[20];
    unsigned long long valSmoothVel;
    char padding_a4[16];
    unsigned long long deltaAccumTarget;
    unsigned long long deltaAccumSmoothPrev;
    unsigned long long deltaAccumRawPrev;
    unsigned int digiToScrollPositivePrev;
    char k__BackingField;
    char padding_d1[3];
    uint128_t k__BackingField;
    uint128_t k__BackingField;
} InputRig_AxisConfig_Recovered;

struct_0 * InputRig_AxisConfig_Reset(struct_0 *ptr)
{
    *((char *)&ptr->field_cc) = 0;
    *((unsigned long long *)&ptr->padding_a4[12]) = 0;
    *((unsigned long long *)((char *)&ptr->field_bc + 4)) = 0;
    *((unsigned long long *)((char *)&ptr->field_b4 + 4)) = 0;
    ptr->field_80 = 0;
    *((unsigned long long *)&(&ptr->padding_88)[1]) = 0;
    *((unsigned int *)((char *)&ptr->field_c4 + 4)) = 0x10000;
    *((uint128_t *)&ptr->field_d0) = 0;
    *((uint128_t *)((char *)&ptr->field_d4 + 4)) = 0;
    return ptr;
}
```

## `InputRig.AxisConfig.MuteUntilRelease` — RVA `0xc41034`

- Decompiled symbol: `InputRig_AxisConfig_MuteUntilRelease`
- Metadata signature: `public void MuteUntilRelease() { }`
- Native interval: `12` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[146];
    char field_92;
} struct_0;

struct_0 * InputRig_AxisConfig_MuteUntilRelease(struct_0 *ptr)
{
    ptr->field_92 = 1;
    return ptr;
}
```

## `InputRig.AxisConfig.IsMuted` — RVA `0xc41040`

- Decompiled symbol: `InputRig_AxisConfig_IsMuted`
- Metadata signature: `public bool IsMuted() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[146];
    char field_92;
} struct_0;

long long InputRig_AxisConfig_IsMuted(struct_0 *a0)
{
    return a0->field_92;
}
```

## `InputRig.AxisConfig.ApplyKeyboardInput` — RVA `0xc41048`

- Decompiled symbol: `InputRig_AxisConfig_ApplyKeyboardInput`
- Metadata signature: `public void ApplyKeyboardInput() { }`
- Native interval: `160` bytes
- Result: `pseudocode`
- Heuristic layout hint: `InputRig_AxisConfig_Recovered` matched 10 offsets against `InputRig.AxisConfig` metadata (confidence 1.00).

```c
typedef struct InputRig_AxisConfig_Recovered {
    char padding_0[52];
    unsigned int keyboardPositive;
    unsigned int keyboardPositiveAlt0;
    unsigned int keyboardPositiveAlt1;
    unsigned int keyboardPositiveAlt2;
    unsigned int keyboardNegative;
    unsigned int keyboardNegativeAlt0;
    unsigned int keyboardNegativeAlt1;
    unsigned int keyboardNegativeAlt2;
    char padding_54[123];
    char k__BackingField;
    char k__BackingField;
} InputRig_AxisConfig_Recovered;

int InputRig_AxisConfig_ApplyKeyboardInput(struct_0 *ptr)
{
    unsigned long long v0;  // x0

    if (((char)InputRig__GetSourceKeyState(ptr->field_34) & 1) || ((char)InputRig__GetSourceKeyState(ptr->field_38) & 1) || ((char)InputRig__GetSourceKeyState(ptr->field_3c) & 1) || ((char)InputRig__GetSourceKeyState(ptr->field_40) & 1))
        ptr->field_cf = 1;
    v0 = InputRig__GetSourceKeyState(ptr->field_44);
    if (((char)v0 & 1) || (v0 = (unsigned long long)InputRig__GetSourceKeyState(ptr->field_48), ((char)v0 & 1) || (v0 = (unsigned long long)InputRig__GetSourceKeyState(ptr->field_4c), ((char)v0 & 1) || (v0 = (unsigned long long)InputRig__GetSourceKeyState(ptr->field_50), ((char)v0 & 1)))))
        ptr->field_d0 = 1;
    return v0;
}
```

## `InputRig.AxisConfig.SetSignedDigital` — RVA `0xc410e8`

- Decompiled symbol: `InputRig_AxisConfig_SetSignedDigital`
- Metadata signature: `public void SetSignedDigital(bool vpositive) { }`
- Native interval: `24` bytes
- Result: `pseudocode`

```c
char [209] InputRig_AxisConfig_SetSignedDigital(char *ptr, unsigned long a1)
{
    if (!((char)a1 & 1))
    {
        ptr[208] = 1;
        return ptr;
    }
    ptr[207] = 1;
    return ptr;
}
```

## `InputRig.AxisConfig.Update` — RVA `0xc41100`

- Decompiled symbol: `InputRig_AxisConfig_Update`
- Metadata signature: `public override void Update(InputRig rig) { }`
- Native interval: `2028` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: Decompiler produced no C-like text

```c
// 0x1041100: stp d11, d10, [sp, #-0x60]!
// 0x1041104: stp d9, d8, [sp, #0x10]
// 0x1041108: str x30, [sp, #0x20]
// 0x104110c: stp x24, x23, [sp, #0x30]
// 0x1041110: stp x22, x21, [sp, #0x40]
// 0x1041114: stp x20, x19, [sp, #0x50]
// 0x1041118: ldr w8, [x0, #0x8c]
// 0x104111c: ldrb w9, [x0, #0x90]
// 0x1041120: mov x22, x0
// 0x1041124: mov x20, x1
// 0x1041128: str w8, [x0, #0x88]
// 0x104112c: strb w9, [x0, #0x91]
// 0x1041130: ldr s0, [x22, #0xd4]!
// 0x1041134: ldr s1, [x0, #0xd8]
// 0x1041138: ldr s2, [x0, #0x54]
// 0x104113c: ldrb w8, [x0, #0xd0]
// 0x1041140: ldrb w9, [x0, #0xcf]
// 0x1041144: fadd s0, s0, s1
// 0x1041148: fneg s1, s2
// 0x104114c: fcmp s0, s1
// 0x1041150: cset w11, mi
// 0x1041154: fcmp s0, s2
// 0x1041158: orr w10, w9, w8
// 0x104115c: strb w11, [x0, #0x98]
// 0x1041160: cset w11, gt
// 0x1041164: tst w10, #0xff
// 0x1041168: mov w10, #0x60
// 0x104116c: strb w11, [x0, #0x99]
// 0x1041170: mov w11, #0x64
// 0x1041174: csel x10, x11, x10, eq
// 0x1041178: ldr s8, [x0, x10]
// 0x104117c: ldrb w10, [x0, #0x20]
// 0x1041180: ldr s10, [x0, #0x94]
// 0x1041184: and w8, w8, #1
// 0x1041188: sub w8, w9, w8
// 0x104118c: mov x19, x0
// 0x1041190: scvtf s9, w8
// 0x1041194: cbz w10, #0x10411c8
// 0x1041198: adrp x9, #0x832000
// 0x104119c: ldr s0, [x9, #0x3b8]
// 0x10411a0: fabs s1, s9
// 0x10411a4: fcmp s1, s0
// 0x10411a8: b.le #0x10411c8
// 0x10411ac: fcmp s10, #0.0
// 0x10411b0: mvn w8, w8
// 0x10411b4: cset w9, ge
// 0x10411b8: cmp w9, w8, lsr #31
// 0x10411bc: b.eq #0x10411c8
// 0x10411c0: fmov s10, wzr
// 0x10411c4: str wzr, [x19, #0x94]
// 0x10411c8: mov x0, xzr
// 0x10411cc: bl #0x104e208
// 0x10411d0: adrp x8, #0x832000
// 0x10411d4: ldr s4, [x8, #0x4e0]
// 0x10411d8: mov v3.16b, v0.16b
// 0x10411dc: mov v0.16b, v10.16b
// 0x10411e0: mov v1.16b, v9.16b
// 0x10411e4: mov v2.16b, v8.16b
// 0x10411e8: mov x0, xzr
// 0x10411ec: bl #0x10574ac
// 0x10411f0: mov v1.16b, v0.16b
// 0x10411f4: ldp s2, s0, [x19, #0xd4]
// 0x10411f8: mov x0, xzr
// 0x10411fc: str s1, [x19, #0x94]
// 0x1041200: fadd s0, s0, s2
// 0x1041204: bl #0x1058484
// 0x1041208: ldr w8, [x19, #0x18]
// 0x104120c: fmov s1, #1.00000000
// 0x1041210: fmov s2, #-1.00000000
// 0x1041214: fmin s1, s0, s1
// 0x1041218: fcmp s0, s2
// 0x104121c: fcsel s8, s1, s2, pl
// 0x1041220: cmp w8, #4
// 0x1041224: b.hi #0x1041788
// 0x1041228: adrp x9, #0x852000
// 0x104122c: add x9, x9, #0xb2
// 0x1041230: adr x10, #0x1041240
// 0x1041234: ldrb w11, [x9, x8]
// 0x1041238: add x10, x10, x11, lsl #2
// 0x104123c: br x10
// 0x1041240: ldr s10, [x19, #0xa4]
// 0x1041244: fcmp s10, #0.0
// 0x1041248: b.eq #0x104127c
// 0x104124c: mov x0, xzr
// 0x1041250: bl #0x105834c
// 0x1041254: fmov s1, wzr
// 0x1041258: fsub s3, s1, s10
// 0x104125c: fneg s2, s0
// 0x1041260: fcmp s3, #0.0
// 0x1041264: fabd s4, s1, s10
// 0x1041268: fcsel s2, s0, s2, ge
// 0x104126c: fadd s2, s10, s2
// 0x1041270: fcmp s4, s0
// 0x1041274: fcsel s10, s2, s1, hi
// 0x1041278: str s10, [x19, #0xa4]
// 0x104127c: ldr w8, [x19, #0xf4]
// 0x1041280: cbz w8, #0x1041298
// 0x1041284: ldr s0, [x19, #0x78]
// 0x1041288: scvtf s1, w8
// 0x104128c: fmul s0, s0, s1
// 0x1041290: fadd s10, s10, s0
// 0x1041294: str s10, [x19, #0xa4]
// 0x1041298: ldr s9, [x19, #0xa8]
// 0x104129c: fcmp s10, #0.0
// 0x10412a0: adrp x23, #0x832000
// 0x10412a4: b.ne #0x10414a8
// 0x10412a8: fcmp s9, #0.0
// 0x10412ac: b.eq #0x10414f8
// 0x10412b0: fmov s10, wzr
// 0x10412b4: b #0x10414b4
// 0x10412b8: ldr w8, [x19, #0xac]
// 0x10412bc: ldr w9, [x19, #0xf4]
// 0x10412c0: ldrb w10, [x19, #0xb0]
// 0x10412c4: add w9, w9, w8
// 0x10412c8: str w9, [x19, #0xac]
// 0x10412cc: cbz w10, #0x1041530
// 0x10412d0: mov w8, wzr
// 0x10412d4: strb wzr, [x19, #0xb0]
// 0x10412d8: ldrb w10, [x19, #0xd0]
// 0x10412dc: cmp w10, #0
// 0x10412e0: csel x9, x19, xzr, eq
// 0x10412e4: cbz w10, #0x1041650
// 0x10412e8: mov w8, #1
// 0x10412ec: mov x9, x19
// 0x10412f0: b #0x10416cc
// 0x10412f4: ldrb w8, [x19, #0xcf]
// 0x10412f8: cbz w8, #0x1041550
// 0x10412fc: mov w23, #1
// 0x1041300: b #0x1041554
// 0x1041304: cbz x20, #0x10413f8
// 0x1041308: ldp s1, s0, [x19, #0xe4]
// 0x104130c: ldr w1, [x19, #0x1c]
// 0x1041310: mov x0, x20
// 0x1041314: mov x2, xzr
// 0x1041318: fadd s0, s0, s1
// 0x104131c: bl #0x103de2c
// 0x1041320: mov v9.16b, v0.16b
// 0x1041324: ldp s0, s1, [x19, #0xdc]
// 0x1041328: ldr w1, [x19, #0x1c]
// 0x104132c: mov x0, x20
// 0x1041330: mov x2, xzr
// 0x1041334: fadd s0, s0, s1
// 0x1041338: bl #0x103de18
// 0x104133c: mov v1.16b, v0.16b
// 0x1041340: mov v0.16b, v9.16b
// 0x1041344: mov x0, xzr
// 0x1041348: bl #0x1058484
// 0x104134c: mov v9.16b, v0.16b
// 0x1041350: ldp s0, s1, [x19, #0xec]
// 0x1041354: ldr w1, [x19, #0x1c]
// 0x1041358: mov x0, x20
// 0x104135c: mov x2, xzr
// 0x1041360: fadd s0, s0, s1
// 0x1041364: bl #0x103de4c
// 0x1041368: mov v1.16b, v0.16b
// 0x104136c: mov v0.16b, v9.16b
// 0x1041370: mov x0, xzr
// 0x1041374: bl #0x1058484
// 0x1041378: mov v9.16b, v0.16b
// 0x104137c: ldr s0, [x19, #0xf4]
// 0x1041380: ldr w1, [x19, #0x1c]
// 0x1041384: mov x0, x20
// 0x1041388: mov x2, xzr
// 0x104138c: scvtf s0, s0
// 0x1041390: bl #0x103de64
// 0x1041394: mov v1.16b, v0.16b
// 0x1041398: mov v0.16b, v9.16b
// 0x104139c: mov x0, xzr
// 0x10413a0: bl #0x1058484
// 0x10413a4: ldr x8, [x20, #0x128]
// 0x10413a8: cbz x8, #0x10413f8
// 0x10413ac: mov v9.16b, v0.16b
// 0x10413b0: mov w21, #-1
// 0x10413b4: ldr w9, [x8, #0x24]
// 0x10413b8: add w21, w21, #1
// 0x10413bc: cmp w21, w9
// 0x10413c0: b.ge #0x10413fc
// 0x10413c4: ldr s0, [x8, #0x14]
// 0x10413c8: ldr w1, [x19, #0x1c]
// 0x10413cc: mov x0, x20
// 0x10413d0: mov x2, xzr
// 0x10413d4: fmul s0, s8, s0
// 0x10413d8: bl #0x103de8c
// 0x10413dc: mov v1.16b, v0.16b
// 0x10413e0: mov v0.16b, v9.16b
// 0x10413e4: mov x0, xzr
// 0x10413e8: bl #0x1058484
// 0x10413ec: ldr x8, [x20, #0x128]
// 0x10413f0: mov v9.16b, v0.16b
// 0x10413f4: cbnz x8, #0x10413b4
// 0x10413f8: bl #0xf7db74
// 0x10413fc: ldp s1, s8, [x19, #0xb4]
// 0x1041400: ldr s0, [x19, #0xc0]
// 0x1041404: ldr s10, [x19, #0x5c]
// 0x1041408: mov x0, xzr
// 0x104140c: fadd s9, s9, s1
// 0x1041410: str s0, [x19, #0xc4]
// 0x1041414: str s8, [x19, #0xbc]
// 0x1041418: str s9, [x19, #0xb4]
// 0x104141c: add x21, x19, #0x9c
// 0x1041420: bl #0x104e208
// 0x1041424: adrp x8, #0x832000
// 0x1041428: ldr s11, [x8, #0x41c]
// 0x104142c: mov v3.16b, v0.16b
// 0x1041430: mov v0.16b, v8.16b
// 0x1041434: mov v1.16b, v9.16b
// 0x1041438: mov x0, x21
// 0x104143c: mov v2.16b, v10.16b
// 0x1041440: mov v4.16b, v11.16b
// 0x1041444: mov x1, xzr
// 0x1041448: bl #0x10589b8
// 0x104144c: ldr s8, [x19, #0xc0]
// 0x1041450: ldr s9, [x19, #0xb4]
// 0x1041454: ldr s10, [x19, #0x58]
// 0x1041458: mov x0, xzr
// 0x104145c: str s0, [x19, #0xb8]
// 0x1041460: str s8, [x19, #0xc4]
// 0x1041464: add x21, x19, #0xa0
// 0x1041468: bl #0x104e208
// 0x104146c: mov v3.16b, v0.16b
// 0x1041470: mov v0.16b, v8.16b
// 0x1041474: mov v1.16b, v9.16b
// 0x1041478: mov x0, x21
// 0x104147c: mov v2.16b, v10.16b
// 0x1041480: mov v4.16b, v11.16b
// 0x1041484: mov x1, xzr
// 0x1041488: bl #0x10589b8
// 0x104148c: ldp s1, s2, [x19, #0xb8]
// 0x1041490: ldr s3, [x19, #0xc4]
// 0x1041494: str s0, [x19, #0xc0]
// 0x1041498: fsub s1, s1, s2
// 0x104149c: fsub s0, s0, s3
// 0x10414a0: stp s0, s1, [x19, #0x80]
// 0x10414a4: b #0x1041788
// 0x10414a8: fmov s10, #1.00000000
// 0x10414ac: b.pl #0x10414b4
// 0x10414b0: fmov s10, #-1.00000000
// 0x10414b4: ldr s11, [x19, #0x74]
// 0x10414b8: mov x0, xzr
// 0x10414bc: bl #0x105834c
// 0x10414c0: ldr s4, [x23, #0x534]
// 0x10414c4: mov v3.16b, v0.16b
// 0x10414c8: fmov s5, #0.75000000
// 0x10414cc: mov v0.16b, v9.16b
// 0x10414d0: mov v1.16b, v10.16b
// 0x10414d4: mov v2.16b, v11.16b
// 0x10414d8: mov x0, xzr
// 0x10414dc: bl #0x105861c
// 0x10414e0: mov v1.16b, v0.16b
// 0x10414e4: str s0, [x19, #0xa8]
// 0x10414e8: mov v0.16b, v8.16b
// 0x10414ec: mov x0, xzr
// 0x10414f0: bl #0x1058484
// 0x10414f4: mov v8.16b, v0.16b
// 0x10414f8: ldrb w8, [x19, #0xd0]
// 0x10414fc: cmp w8, #0
// 0x1041500: csel x10, x19, xzr, eq
// 0x1041504: cbz w8, #0x1041514
// 0x1041508: mov w9, #1
// 0x104150c: mov x8, x19
// 0x1041510: b #0x10416fc
// 0x1041514: ldrb w9, [x19, #0xcf]
// 0x1041518: cmp w9, #0
// 0x104151c: csel x8, x10, xzr, eq
// 0x1041520: cbz w9, #0x104166c
// 0x1041524: mov w9, #1
// 0x1041528: mov x8, x19
// 0x104152c: b #0x10416f8
// 0x1041530: cbz w9, #0x1041680
// 0x1041534: mov w8, #1
// 0x1041538: subs w10, w9, #1
// 0x104153c: strb w8, [x19, #0xb0]
// 0x1041540: b.lt #0x10416a8
// 0x1041544: str w10, [x19, #0xac]
// 0x1041548: strb w8, [x19, #0xcf]
// 0x104154c: b #0x10412d8
// 0x1041550: ldrb w23, [x19, #0x99]
// 0x1041554: ldrb w8, [x19, #0xd0]
// 0x1041558: cbz w8, #0x1041564
// 0x104155c: mov w24, #1
// 0x1041560: b #0x1041568
// 0x1041564: ldrb w24, [x19, #0x98]
// 0x1041568: cmp w23, #0
// 0x104156c: ldr w0, [x19, #0xf4]
// 0x1041570: cset w8, ne
// 0x1041574: cmp w24, #0
// 0x1041578: cset w9, ne
// 0x104157c: sub w21, w8, w9
// 0x1041580: cbnz w0, #0x10415f0
// 0x1041584: ldrb w8, [x19, #0xcc]
// 0x1041588: cmp w23, w8
// 0x104158c: b.ne #0x10415f0
// 0x1041590: ldrb w8, [x19, #0xcd]
// 0x1041594: cmp w24, w8
// 0x1041598: b.ne #0x10415f0
// 0x104159c: mov w0, wzr
// 0x10415a0: cbz w21, #0x1041620
// 0x10415a4: ldrb w8, [x19, #0x68]
// 0x10415a8: cbz w8, #0x1041620
// 0x10415ac: ldr s8, [x19, #0xc8]
// 0x10415b0: mov x0, xzr
// 0x10415b4: bl #0x105834c
// 0x10415b8: ldrb w8, [x19, #0xce]
// 0x10415bc: fadd s0, s8, s0
// 0x10415c0: mov w9, #0x70
// 0x10415c4: str s0, [x19, #0xc8]
// 0x10415c8: cmp w8, #0
// 0x10415cc: mov w8, #0x6c
// 0x10415d0: csel x8, x8, x9, eq
// 0x10415d4: ldr s1, [x19, x8]
// 0x10415d8: fcmp s0, s1
// 0x10415dc: b.le #0x10418e4
// 0x10415e0: ldr w0, [x19, #0xf4]
// 0x10415e4: strb wzr, [x19, #0xce]
// 0x10415e8: str wzr, [x19, #0xc8]
// 0x10415ec: b #0x1041610
// 0x10415f0: mov w8, #1
// 0x10415f4: strb w8, [x19, #0xce]
// 0x10415f8: str wzr, [x19, #0xc8]
// 0x10415fc: cbz w21, #0x1041620
// 0x1041600: ldrb w8, [x19, #0xcd]
// 0x1041604: cbnz w8, #0x1041620
// 0x1041608: ldrb w8, [x19, #0xcc]
// 0x104160c: cbnz w8, #0x1041620
// 0x1041610: mov w1, w21
// 0x1041614: mov x2, xzr
// 0x1041618: bl #0x10584c4
// 0x104161c: str w0, [x19, #0xf4]
// 0x1041620: ldp w9, w8, [x19, #0x88]
// 0x1041624: cmp w0, #0
// 0x1041628: cset w10, ne
// 0x104162c: strb w23, [x19, #0xcc]
// 0x1041630: add w8, w0, w8
// 0x1041634: str w8, [x19, #0x8c]
// 0x1041638: sub w8, w8, w9
// 0x104163c: scvtf s0, w8
// 0x1041640: strb w24, [x19, #0xcd]
// 0x1041644: stp s0, s0, [x19, #0x80]
// 0x1041648: strb w10, [x19, #0x90]
// 0x104164c: b #0x1041788
// 0x1041650: ldrb w11, [x19, #0xcf]
// 0x1041654: cmp w11, #0
// 0x1041658: csel x10, x9, xzr, eq
// 0x104165c: cbz w11, #0x1041688
// 0x1041660: mov w8, #1
// 0x1041664: mov x9, x19
// 0x1041668: b #0x10416c8
// 0x104166c: ldrb w9, [x19, #0x98]
// 0x1041670: cbz w9, #0x1041698
// 0x1041674: mov w9, #1
// 0x1041678: mov x8, x10
// 0x104167c: b #0x10416f8
// 0x1041680: mov w8, wzr
// 0x1041684: b #0x10412d8
// 0x1041688: ldrb w11, [x19, #0x98]
// 0x104168c: cbz w11, #0x10416b8
// 0x1041690: mov w8, #1
// 0x1041694: b #0x10416c8
// 0x1041698: ldrb w9, [x19, #0x99]
// 0x104169c: cbz w9, #0x10416ec
// 0x10416a0: mov w9, #1
// 0x10416a4: b #0x10416f8
// 0x10416a8: add w9, w9, #1
// 0x10416ac: str w9, [x19, #0xac]
// 0x10416b0: strb w8, [x19, #0xd0]
// 0x10416b4: b #0x10412ec
// 0x10416b8: ldrb w9, [x19, #0x99]
// 0x10416bc: cmp w9, #0
// 0x10416c0: csinc w8, w8, wzr, eq
// 0x10416c4: mov x9, x10
// 0x10416c8: cbz x9, #0x10413f8
// 0x10416cc: strb w8, [x9, #0x90]
// 0x10416d0: ldrb w8, [x19, #0x90]
// 0x10416d4: fmov s0, #1.00000000
// 0x10416d8: fmov s1, wzr
// 0x10416dc: cmp w8, #0
// 0x10416e0: fcsel s0, s1, s0, eq
// 0x10416e4: stp s0, s0, [x19, #0x80]
// 0x10416e8: b #0x1041788
// 0x10416ec: ldr s0, [x19, #0xa4]
// 0x10416f0: fcmp s0, #0.0
// 0x10416f4: cset w9, ne
// 0x10416f8: cbz x8, #0x10413f8
// 0x10416fc: strb w9, [x8, #0x90]
// 0x1041700: ldr w8, [x19, #0x18]
// 0x1041704: ldr s9, [x19, #0x80]
// 0x1041708: ldr s10, [x19, #0x58]
// 0x104170c: fmov s0, wzr
// 0x1041710: cmp w8, #0
// 0x1041714: fccmp s8, s0, #0, eq
// 0x1041718: mov x0, xzr
// 0x104171c: fcsel s8, s0, s8, mi
// 0x1041720: add x21, x19, #0xa0
// 0x1041724: bl #0x104e208
// 0x1041728: ldr s11, [x23, #0x534]
// 0x104172c: mov v3.16b, v0.16b
// 0x1041730: mov v0.16b, v9.16b
// 0x1041734: mov v1.16b, v8.16b
// 0x1041738: mov x0, x21
// 0x104173c: mov v2.16b, v10.16b
// 0x1041740: mov v4.16b, v11.16b
// 0x1041744: mov x1, xzr
// 0x1041748: bl #0x10589b8
// 0x104174c: ldr s9, [x19, #0x84]
// 0x1041750: ldr s10, [x19, #0x5c]
// 0x1041754: mov x0, xzr
// 0x1041758: str s0, [x19, #0x80]
// 0x104175c: add x21, x19, #0x9c
// 0x1041760: bl #0x104e208
// 0x1041764: mov v3.16b, v0.16b
// 0x1041768: mov v0.16b, v9.16b
// 0x104176c: mov v1.16b, v8.16b
// 0x1041770: mov x0, x21
// 0x1041774: mov v2.16b, v10.16b
// 0x1041778: mov v4.16b, v11.16b
// 0x104177c: mov x1, xzr
// 0x1041780: bl #0x10589b8
// 0x1041784: str s0, [x19, #0x84]
// 0x1041788: ldrb w8, [x19, #0x92]
// 0x104178c: cbz w8, #0x10417e0
// 0x1041790: ldrb w8, [x19, #0xd0]
// 0x1041794: movi d0, #0000000000000000
// 0x1041798: str d0, [x19, #0x80]
// 0x104179c: stur d0, [x19, #0x9c]
// 0x10417a0: strh wzr, [x19, #0x90]
// 0x10417a4: str wzr, [x19, #0x94]
// 0x10417a8: cbnz w8, #0x10417d0
// 0x10417ac: ldrb w8, [x19, #0xcf]
// 0x10417b0: cbnz w8, #0x10417d0
// 0x10417b4: ldrb w8, [x19, #0x98]
// 0x10417b8: cbnz w8, #0x10417d0
// 0x10417bc: ldrb w8, [x19, #0x99]
// 0x10417c0: cbnz w8, #0x10417d0
// 0x10417c4: ldr w8, [x19, #0xf4]
// 0x10417c8: cbnz w8, #0x10417d0
// 0x10417cc: strb wzr, [x19, #0x92]
// 0x10417d0: ldr w8, [x19, #0x18]
// 0x10417d4: cmp w8, #4
// 0x10417d8: b.ne #0x10417e0
// 0x10417dc: strb wzr, [x19, #0x92]
// 0x10417e0: ldrb w8, [x19, #0x98]
// 0x10417e4: cbnz w8, #0x10417f0
// 0x10417e8: ldrb w8, [x19, #0xd0]
// 0x10417ec: cbz w8, #0x104184c
// 0x10417f0: ldrb w8, [x19, #0x28]
// 0x10417f4: cbz w8, #0x1041804
// 0x10417f8: cbz x20, #0x10413f8
// 0x10417fc: add x8, x19, #0x30
// 0x1041800: b #0x104183c
// 0x1041804: cbz x20, #0x10413f8
// 0x1041808: ldr w1, [x19, #0x44]
// 0x104180c: mov x0, x20
// 0x1041810: mov x2, xzr
// 0x1041814: bl #0x103dd94
// 0x1041818: ldr w1, [x19, #0x48]
// 0x104181c: mov x0, x20
// 0x1041820: mov x2, xzr
// 0x1041824: bl #0x103dd94
// 0x1041828: ldr w1, [x19, #0x4c]
// 0x104182c: mov x0, x20
// 0x1041830: mov x2, xzr
// 0x1041834: bl #0x103dd94
// 0x1041838: add x8, x19, #0x50
// 0x104183c: ldr w1, [x8]
// 0x1041840: mov x0, x20
// 0x1041844: mov x2, xzr
// 0x1041848: bl #0x103dd94
// 0x104184c: ldrb w8, [x19, #0x99]
// 0x1041850: cbnz w8, #0x104185c
// 0x1041854: ldrb w8, [x19, #0xcf]
// 0x1041858: cbz w8, #0x10418b8
// 0x104185c: ldrb w8, [x19, #0x28]
// 0x1041860: cbz w8, #0x1041870
// 0x1041864: cbz x20, #0x10413f8
// 0x1041868: add x8, x19, #0x2c
// 0x104186c: b #0x10418a8
// 0x1041870: cbz x20, #0x10413f8
// 0x1041874: ldr w1, [x19, #0x34]
// 0x1041878: mov x0, x20
// 0x104187c: mov x2, xzr
// 0x1041880: bl #0x103dd94
// 0x1041884: ldr w1, [x19, #0x38]
// 0x1041888: mov x0, x20
// 0x104188c: mov x2, xzr
// 0x1041890: bl #0x103dd94
// 0x1041894: ldr w1, [x19, #0x3c]
// 0x1041898: mov x0, x20
// 0x104189c: mov x2, xzr
// 0x10418a0: bl #0x103dd94
// 0x10418a4: add x8, x19, #0x40
// 0x10418a8: ldr w1, [x8]
// 0x10418ac: mov x0, x20
// 0x10418b0: mov x2, xzr
// 0x10418b4: bl #0x103dd94
// 0x10418b8: movi v0.2d, #0000000000000000
// 0x10418bc: sturh wzr, [x19, #0xcf]
// 0x10418c0: str wzr, [x22, #0x20]
// 0x10418c4: stp q0, q0, [x22]
// 0x10418c8: ldp x20, x19, [sp, #0x50]
// 0x10418cc: ldp x22, x21, [sp, #0x40]
// 0x10418d0: ldp x24, x23, [sp, #0x30]
// 0x10418d4: ldr x30, [sp, #0x20]
// 0x10418d8: ldp d9, d8, [sp, #0x10]
// 0x10418dc: ldp d11, d10, [sp], #0x60
// 0x10418e0: ret
// 0x10418e4: ldr w0, [x19, #0xf4]
// 0x10418e8: b #0x1041620
```

## `InputRig.AxisConfig.Set` — RVA `0xc418ec`

- Decompiled symbol: `InputRig_AxisConfig_Set`
- Metadata signature: `public void Set(float v, InputRig.InputSource source) { }`
- Native interval: `512` bytes
- Result: `pseudocode`

```c
extern char g_8520b7;

long long InputRig_AxisConfig_Set(unsigned long a0, unsigned int a1)
{
    if (5 < a1)
        return a0;
    goto sub_1041924 + (&g_8520b7)[a1] * 4;
}
```

## `InputRig.AxisConfig.SetAnalog` — RVA `0xc41aec`

- Decompiled symbol: `InputRig_AxisConfig_SetAnalog`
- Metadata signature: `public void SetAnalog(float v) { }`
- Native interval: `76` bytes
- Result: `pseudocode`

```c
int InputRig_AxisConfig_SetAnalog(unsigned int *ptr)
{
    unsigned int v0;  // s1
    unsigned int v1;  // w0

    CFUtils__ApplyPositveDeltaInput(0);
    v0 = ptr[54];
    ptr[53] = ptr[53];
    v1 = CFUtils__ApplyNegativeDeltaInput(0);
    ptr[54] = v0;
    return v1;
}
```

## `InputRig.AxisConfig.SetMouseDelta` — RVA `0xc41b38`

- Decompiled symbol: `InputRig_AxisConfig_SetMouseDelta`
- Metadata signature: `public void SetMouseDelta(float mouseDelta) { }`
- Native interval: `76` bytes
- Result: `pseudocode`

```c
int InputRig_AxisConfig_SetMouseDelta(unsigned int *ptr)
{
    unsigned int v0;  // s1
    unsigned int v1;  // w0

    CFUtils__ApplyPositveDeltaInput(0);
    v0 = ptr[56];
    ptr[55] = ptr[55];
    v1 = CFUtils__ApplyNegativeDeltaInput(0);
    ptr[56] = v0;
    return v1;
}
```

## `InputRig.AxisConfig.SetTouchDelta` — RVA `0xc41b84`

- Decompiled symbol: `InputRig_AxisConfig_SetTouchDelta`
- Metadata signature: `public void SetTouchDelta(float touchDelta) { }`
- Native interval: `76` bytes
- Result: `pseudocode`

```c
int InputRig_AxisConfig_SetTouchDelta(unsigned int *ptr)
{
    unsigned int v0;  // s1
    unsigned int v1;  // w0

    CFUtils__ApplyPositveDeltaInput(0);
    v0 = ptr[58];
    ptr[57] = ptr[57];
    v1 = CFUtils__ApplyNegativeDeltaInput(0);
    ptr[58] = v0;
    return v1;
}
```

## `InputRig.AxisConfig.SetNormalizedDelta` — RVA `0xc41bd0`

- Decompiled symbol: `InputRig_AxisConfig_SetNormalizedDelta`
- Metadata signature: `public void SetNormalizedDelta(float normalizedDelta) { }`
- Native interval: `76` bytes
- Result: `pseudocode`

```c
int InputRig_AxisConfig_SetNormalizedDelta(unsigned int *ptr)
{
    unsigned int v0;  // s1
    unsigned int v1;  // w0

    CFUtils__ApplyPositveDeltaInput(0);
    v0 = ptr[60];
    ptr[59] = ptr[59];
    v1 = CFUtils__ApplyNegativeDeltaInput(0);
    ptr[60] = v0;
    return v1;
}
```

## `InputRig.AxisConfig.SetScrollDelta` — RVA `0xc41c1c`

- Decompiled symbol: `InputRig_AxisConfig_SetScrollDelta`
- Metadata signature: `public void SetScrollDelta(int scrollDelta) { }`
- Native interval: `32` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[244];
    unsigned int field_f4;
} struct_0;

int InputRig_AxisConfig_SetScrollDelta(struct_0 *ptr)
{
    unsigned int v0;  // w0

    v0 = CFUtils__ApplyDeltaInputInt(ptr->field_f4);
    ptr->field_f4 = v0;
    return v0;
}
```

## `InputRig.AxisConfig.SetDigital` — RVA `0xc41c3c`

- Decompiled symbol: `InputRig_AxisConfig_SetDigital`
- Metadata signature: `public void SetDigital() { }`
- Native interval: `12` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[207];
    char field_cf;
} struct_0;

struct_0 * InputRig_AxisConfig_SetDigital(struct_0 *ptr)
{
    ptr->field_cf = 1;
    return ptr;
}
```

## `InputRig.AxisConfig.GetAnalog` — RVA `0xc41c48`

- Decompiled symbol: `InputRig_AxisConfig_GetAnalog`
- Metadata signature: `public float GetAnalog() { }`
- Native interval: `28` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned int field_18;
} struct_0;

struct_0 * InputRig_AxisConfig_GetAnalog(struct_0 *a0)
{
    return a0;
}
```

## `InputRig.AxisConfig.GetAnalogRaw` — RVA `0xc41c64`

- Decompiled symbol: `InputRig_AxisConfig_GetAnalogRaw`
- Metadata signature: `public float GetAnalogRaw() { }`
- Native interval: `28` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned int field_18;
} struct_0;

struct_0 * InputRig_AxisConfig_GetAnalogRaw(struct_0 *a0)
{
    return a0;
}
```

## `InputRig.AxisConfig.IsControlledByInput` — RVA `0xc41c80`

- Decompiled symbol: `InputRig_AxisConfig_IsControlledByInput`
- Metadata signature: `public bool IsControlledByInput() { }`
- Native interval: `176` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: Decompiler produced no C-like text

```c
// 0x1041c80: ldrb w8, [x0, #0xd0]
// 0x1041c84: cbnz w8, #0x1041d18
// 0x1041c88: ldrb w8, [x0, #0xcf]
// 0x1041c8c: cbnz w8, #0x1041d18
// 0x1041c90: ldr s1, [x0, #0xd8]
// 0x1041c94: adrp x8, #0x832000
// 0x1041c98: ldr s0, [x8, #0x534]
// 0x1041c9c: fabs s1, s1
// 0x1041ca0: fcmp s1, s0
// 0x1041ca4: b.gt #0x1041d18
// 0x1041ca8: ldr s1, [x0, #0xd4]
// 0x1041cac: fabs s1, s1
// 0x1041cb0: fcmp s1, s0
// 0x1041cb4: b.gt #0x1041d18
// 0x1041cb8: ldr s1, [x0, #0xe0]
// 0x1041cbc: fabs s1, s1
// 0x1041cc0: fcmp s1, s0
// 0x1041cc4: b.gt #0x1041d18
// 0x1041cc8: ldr s1, [x0, #0xdc]
// 0x1041ccc: fabs s1, s1
// 0x1041cd0: fcmp s1, s0
// 0x1041cd4: b.gt #0x1041d18
// 0x1041cd8: ldr s1, [x0, #0xf0]
// 0x1041cdc: fabs s1, s1
// 0x1041ce0: fcmp s1, s0
// 0x1041ce4: b.gt #0x1041d18
// 0x1041ce8: ldr s1, [x0, #0xec]
// 0x1041cec: fabs s1, s1
// 0x1041cf0: fcmp s1, s0
// 0x1041cf4: b.gt #0x1041d18
// 0x1041cf8: ldr s1, [x0, #0xe8]
// 0x1041cfc: fabs s1, s1
// 0x1041d00: fcmp s1, s0
// 0x1041d04: b.gt #0x1041d18
// 0x1041d08: ldr s1, [x0, #0xe4]
// 0x1041d0c: fabs s1, s1
// 0x1041d10: fcmp s1, s0
// 0x1041d14: b.le #0x1041d20
// 0x1041d18: mov w0, #1
// 0x1041d1c: ret
// 0x1041d20: ldr w8, [x0, #0xf4]
// 0x1041d24: cmp w8, #0
// 0x1041d28: cset w0, ne
// 0x1041d2c: ret
```

## `InputRig.AxisConfig.GetButton` — RVA `0xc41d30`

- Decompiled symbol: `InputRig_AxisConfig_GetButton`
- Metadata signature: `public bool GetButton() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[144];
    char field_90;
} struct_0;

long long InputRig_AxisConfig_GetButton(struct_0 *a0)
{
    return a0->field_90;
}
```

## `InputRig.AxisConfig.GetButtonDown` — RVA `0xc41d38`

- Decompiled symbol: `InputRig_AxisConfig_GetButtonDown`
- Metadata signature: `public bool GetButtonDown() { }`
- Native interval: `32` bytes
- Result: `pseudocode`

```c
unsigned long long InputRig_AxisConfig_GetButtonDown(char *a0)
{
    if (a0[145])
    {
        return 0;
    }
    else if (!a0[144])
    {
        return 0;
    }
    else
    {
        return 1;
    }
}
```

## `InputRig.AxisConfig.GetButtonUp` — RVA `0xc41d58`

- Decompiled symbol: `InputRig_AxisConfig_GetButtonUp`
- Metadata signature: `public bool GetButtonUp() { }`
- Native interval: `32` bytes
- Result: `pseudocode`

```c
unsigned long long InputRig_AxisConfig_GetButtonUp(char *a0)
{
    if (!a0[145])
    {
        return 0;
    }
    else if (a0[144])
    {
        return 0;
    }
    else
    {
        return 1;
    }
}
```

## `InputRig.AxisConfig.GetSupportedInputSourceMask` — RVA `0xc41d78`

- Decompiled symbol: `InputRig_AxisConfig_GetSupportedInputSourceMask`
- Metadata signature: `public int GetSupportedInputSourceMask() { }`
- Native interval: `36` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned int field_18;
} struct_0;

extern unsigned int g_8520f4[4];

unsigned int InputRig_AxisConfig_GetSupportedInputSourceMask(struct_0 *ptr)
{
    unsigned long v0;  // x8

    v0 = ptr->field_18;
    if (4 < (unsigned int)v0)
        return 0;
    return g_8520f4[v0];
}
```

## `InputRig.AxisConfig.DoesSupportInputSource` — RVA `0xc41d9c`

- Decompiled symbol: `InputRig_AxisConfig_DoesSupportInputSource`
- Metadata signature: `public bool DoesSupportInputSource(InputRig.InputSource source) { }`
- Native interval: `44` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned int field_18;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
    unsigned int field_4;
    unsigned int field_8;
    unsigned int field_c;
} struct_1;

extern struct_1 g_8520f4;

unsigned int InputRig_AxisConfig_DoesSupportInputSource(struct_0 *ptr, char a1)
{
    unsigned long idx;  // x8
    unsigned int v1;  // w8

    idx = ptr->field_18;
    if (4 >= (unsigned int)idx)
        v1 = (&g_8520f4.field_0)[idx];
    else
        v1 = 0;
    return v1 >> (a1 & 31) & 1;
}
```

## `InputRig.AxisConfig.IsSignedAxis` — RVA `0xc41dc8`

- Decompiled symbol: `InputRig_AxisConfig_IsSignedAxis`
- Metadata signature: `private bool IsSignedAxis() { }`
- Native interval: `44` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned int field_18;
} struct_0;

unsigned int InputRig_AxisConfig_IsSignedAxis(struct_0 *ptr)
{
    unsigned int v0;  // w8

    v0 = ptr->field_18 - 1;
    if (3 < v0)
        return 0;
    return 13 >> ((char)v0 & 15 & 31) & 1;
}
```

## `InputRig.AxisConfig.DoesAffectKeyCode` — RVA `0xc41df4`

- Decompiled symbol: `InputRig_AxisConfig_DoesAffectKeyCode`
- Metadata signature: `public bool DoesAffectKeyCode(KeyCode key) { }`
- Native interval: `204` bytes
- Result: `pseudocode`
- Heuristic layout hint: `InputRig_AxisConfig_Recovered` matched 4 offsets against `InputRig.AxisConfig` metadata (confidence 1.00).

```c
typedef struct InputRig_AxisConfig_Recovered {
    char padding_0[24];
    unsigned int axisType;
    char padding_1c[12];
    char affectSourceKeys;
    char padding_29[3];
    unsigned int affectedKeyPositive;
    unsigned int affectedKeyNegative;
} InputRig_AxisConfig_Recovered;

unsigned int InputRig_AxisConfig_DoesAffectKeyCode(struct_0 *ptr, unsigned int a1)
{
    unsigned long v0;  // 4125
    unsigned int v1;  // w8
    unsigned long v2;  // 4125

    if (ptr->field_28)
    {
        if (*((int *)&ptr[1].padding_0[0]) == a1)
        {
            return 1;
        }
        else if (*((int *)&ptr[1].padding_0[4]) == a1)
        {
            return 1;
        }
        else if (*((int *)&ptr[1].padding_0[8]) == a1)
        {
            return 1;
        }
        else if (*((int *)&ptr[1].padding_0[12]) == a1)
        {
            return 1;
        }
        else if (4 >= ptr->field_18)
        {
            v0 = arm64g_calculate_condition(9, (unsigned long long)(1 << ((char)ptr->field_18 & 31) & 26), 0, 0);
            if ((char)v0)
            {
                return 0;
            }
            else if (*((int *)&ptr[1].padding_0[16]) == a1)
            {
                return 1;
            }
            else if (*((int *)&ptr[1].padding_0[20]) == a1)
            {
                return 1;
            }
            else if (ptr[1].field_18 != a1)
            {
                v1 = *((int *)&ptr[1].padding_1c[0]);
            }
            else
            {
                return 1;
            }
        }
        else
        {
            return 0;
        }
    }
    else
    {
        if (ptr->field_2c == a1)
        {
            return 1;
        }
        else if (4 >= ptr->field_18)
        {
            v2 = arm64g_calculate_condition(9, (unsigned long long)(1 << ((char)ptr->field_18 & 31) & 26), 0, 0);
            if ((char)v2)
                return 0;
            v1 = ptr->field_30;
        }
        else
        {
            return 0;
        }
    }
    if (v1 != a1)
        return 0;
    return 1;
}
```
