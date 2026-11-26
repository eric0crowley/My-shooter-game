# Native pseudocode: JoystickConfig

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `JoystickConfig.ctor` — RVA `0xc609d8`

- Decompiled symbol: `JoystickConfig_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `52` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    uint128_t field_10;
    unsigned long long field_20;
    unsigned int field_28;
    char padding_2c[4];
    long long field_30;
} struct_0;

long long JoystickConfig_ctor(struct_0 *ptr, unsigned long a1, unsigned int a2, unsigned int a3)
{
    long long v0;  // x0

    v0 = AnalogConfig__ctor(ptr, 0, a2, a3);
    *((unsigned int *)&ptr[1].padding_0[0]) = 1;
    *((unsigned int *)&ptr[1].field_10) = 0x3f000000;
    *((unsigned long *)((char *)&ptr->field_10 + 12)) = 4510805389550918042;
    return v0;
}
```

## `JoystickConfig.AnimateDirToAnalogVec` — RVA `0xc60a0c`

- Decompiled symbol: `JoystickConfig_AnimateDirToAnalogVec`
- Metadata signature: `public Vector2 AnimateDirToAnalogVec(Vector2 curVec, Dir targetDir) { }`
- Native interval: `156` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[56];
    unsigned int field_38;
} struct_0;

long long JoystickConfig_AnimateDirToAnalogVec(struct_0 *a0, unsigned int a1)
{
    long long v0;  // x0

    CFUtils__DirToVector(a1);
    Time__get_unscaledTime(0);
    v0 = CFUtils__SmoothTowardsVec2();
    return CFUtils__SmoothTowardsVec2();
}
```

## `JoystickConfig.ClampNormalizedPos` — RVA `0xc60aa8`

- Decompiled symbol: `JoystickConfig_ClampNormalizedPos`
- Metadata signature: `public Vector2 ClampNormalizedPos(Vector2 np) { }`
- Native interval: `24` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[56];
    unsigned int field_38;
} struct_0;

typedef struct struct_1 {
    char padding_0[224];
    unsigned int field_e0;
} struct_1;

long long JoystickConfig_ClampNormalizedPos(struct_0 *a0)
{
    long long v0;  // x0
    struct_1 *v1;  // x0

    if (!a0->field_38)
    {
        v1 = CFUtils__ClampInsideUnitCircle();
        return CFUtils__ClampInsideUnitCircle();
    }
    v0 = CFUtils__ClampPerAxisInsideUnitSquare();
    return CFUtils__ClampPerAxisInsideUnitSquare();
}
```
