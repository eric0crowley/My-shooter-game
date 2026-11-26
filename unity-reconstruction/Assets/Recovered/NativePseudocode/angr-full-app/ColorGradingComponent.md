# Native pseudocode: ColorGradingComponent

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `ColorGradingComponent.get_active` — RVA `0xcd0a60`

- Decompiled symbol: `ColorGradingComponent_get_active`
- Metadata signature: `public override bool get_active() { }`
- Native interval: `104` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    char padding_0[16];
    struct struct_0 *field_10;
    struct struct_1 *field_18;
} struct_2;

typedef struct struct_1 {
    char padding_0[16];
    char field_10;
} struct_1;

typedef struct struct_0 {
    char padding_0[48];
    char field_30;
} struct_0;

extern long long g_1efa0e0;
extern char g_1fab5b6;

unsigned long long ColorGradingComponent_get_active(struct_2 *a0)
{
    unsigned long long v0;  // x0

    if (!(g_1fab5b6 & 1))
    {
        sub_f7d92c(&g_1efa0e0);
        g_1fab5b6 = 1;
    }
    if (a0->field_18)
    {
        if (!a0->field_18->field_10)
        {
            return 0;
        }
        else if (a0->field_10)
        {
            if (a0->field_10->field_30)
                v0 = 0;
            else
                v0 = 1;
            return v0;
        }
    }
    sub_f7db74();
}
```

## `ColorGradingComponent.StandardIlluminantY` — RVA `0xcd0ac8`

- Decompiled symbol: `ColorGradingComponent_StandardIlluminantY`
- Metadata signature: `private float StandardIlluminantY(float x) { }`
- Native interval: `44` bytes
- Result: `pseudocode`

```c
long long ColorGradingComponent_StandardIlluminantY(void)
{
    unsigned long v0;  // x0

    return v0;
}
```

## `ColorGradingComponent.CIExyToLMS` — RVA `0xcd0af4`

- Decompiled symbol: `ColorGradingComponent_CIExyToLMS`
- Metadata signature: `private Vector3 CIExyToLMS(float x, float y) { }`
- Native interval: `144` bytes
- Result: `pseudocode`

```c
long long ColorGradingComponent_CIExyToLMS(void)
{
    unsigned long v0;  // x0

    return v0;
}
```

## `ColorGradingComponent.CalculateColorBalance` — RVA `0xcd0b84`

- Decompiled symbol: `ColorGradingComponent_CalculateColorBalance`
- Metadata signature: `private Vector3 CalculateColorBalance(float temperature, float tint) { }`
- Native interval: `260` bytes
- Result: `pseudocode`

```c
long long ColorGradingComponent_CalculateColorBalance(void)
{
    unsigned int v0;  // s0
    unsigned long v1;  // 4147
    unsigned long v2;  // x0
    unsigned long v3;  // x0

    v1 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v0 / 0x425c0000, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v0 / 0x425c0000, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v0 / 0x425c0000, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v0 / 0x425c0000, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v0 / 0x425c0000, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v0 / 0x425c0000, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if (!((char)v1))
        return v3;
    return v2;
}
```

## `ColorGradingComponent.NormalizeColor` — RVA `0xcd0c88`

- Decompiled symbol: `ColorGradingComponent_NormalizeColor`
- Metadata signature: `private static Color NormalizeColor(Color c) { }`
- Native interval: `200` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: Decompiler produced no C-like text

```c
// 0x10d0c88: str d12, [sp, #-0x40]!
// 0x10d0c8c: stp d11, d10, [sp, #0x10]
// 0x10d0c90: stp d9, d8, [sp, #0x20]
// 0x10d0c94: stp x30, x19, [sp, #0x30]
// 0x10d0c98: adrp x19, #0x1fab000
// 0x10d0c9c: ldrb w8, [x19, #0x2ca]
// 0x10d0ca0: mov v11.16b, v0.16b
// 0x10d0ca4: fadd s0, s0, s1
// 0x10d0ca8: mov v10.16b, v1.16b
// 0x10d0cac: fadd s0, s2, s0
// 0x10d0cb0: fmov s1, #3.00000000
// 0x10d0cb4: mov v8.16b, v3.16b
// 0x10d0cb8: mov v9.16b, v2.16b
// 0x10d0cbc: fdiv s12, s0, s1
// 0x10d0cc0: cbnz w8, #0x10d0cd8
// 0x10d0cc4: adrp x0, #0x1e8c000
// 0x10d0cc8: ldr x0, [x0, #0xd80]
// 0x10d0ccc: bl #0xf7d92c
// 0x10d0cd0: mov w8, #1
// 0x10d0cd4: strb w8, [x19, #0x2ca]
// 0x10d0cd8: adrp x8, #0x1e8c000
// 0x10d0cdc: ldr x8, [x8, #0xd80]
// 0x10d0ce0: adrp x9, #0x832000
// 0x10d0ce4: ldr s0, [x9, #0x474]
// 0x10d0ce8: fabs s1, s12
// 0x10d0cec: ldr x8, [x8]
// 0x10d0cf0: fmov s2, wzr
// 0x10d0cf4: fmaxnm s1, s1, s2
// 0x10d0cf8: fmul s1, s1, s0
// 0x10d0cfc: ldr x8, [x8, #0xb8]
// 0x10d0d00: fmov s0, #8.00000000
// 0x10d0d04: fabd s2, s2, s12
// 0x10d0d08: ldr s3, [x8]
// 0x10d0d0c: fmul s3, s3, s0
// 0x10d0d10: fcmp s1, s3
// 0x10d0d14: fcsel s1, s1, s3, gt
// 0x10d0d18: fmov s0, #1.00000000
// 0x10d0d1c: fcmp s2, s1
// 0x10d0d20: fmov s1, #1.00000000
// 0x10d0d24: fmov s2, #1.00000000
// 0x10d0d28: b.mi #0x10d0d38
// 0x10d0d2c: fdiv s0, s11, s12
// 0x10d0d30: fdiv s1, s10, s12
// 0x10d0d34: fdiv s2, s9, s12
// 0x10d0d38: mov v3.16b, v8.16b
// 0x10d0d3c: ldp x30, x19, [sp, #0x30]
// 0x10d0d40: ldp d9, d8, [sp, #0x20]
// 0x10d0d44: ldp d11, d10, [sp, #0x10]
// 0x10d0d48: ldr d12, [sp], #0x40
// 0x10d0d4c: ret
```

## `ColorGradingComponent.ClampVector` — RVA `0xcd0d50`

- Decompiled symbol: `ColorGradingComponent_ClampVector`
- Metadata signature: `private static Vector3 ClampVector(Vector3 v, float min, float max) { }`
- Native interval: `52` bytes
- Result: `pseudocode`

```c
long long ColorGradingComponent_ClampVector(void)
{
    unsigned int v0;  // s0
    unsigned int v1;  // s4
    unsigned long v10;  // 4129
    unsigned long v11;  // x0
    unsigned long v12;  // x0
    unsigned long v2;  // 4129
    unsigned int v3;  // s3
    unsigned long v4;  // 4129
    unsigned int v5;  // s1
    unsigned long v6;  // 4129
    unsigned long v7;  // 4129
    unsigned int v8;  // s2
    unsigned long v9;  // 4129

    v2 = arm64g_calculate_condition(192, (((((unsigned long long)(char)(CmpF(v0, v1)) >> 5 & 3 | (unsigned long long)(CmpF(v0, v1) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v0, v1)) >> 5 & 3 | (unsigned long long)(CmpF(v0, v1) & 1)) & ((unsigned long long)(char)(CmpF(v0, v1)) >> 5 & 3 | (unsigned long long)(CmpF(v0, v1) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    v4 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v0, v3)) >> 5 & 3 | (unsigned long long)(CmpF(v0, v3) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v0, v3)) >> 5 & 3 | (unsigned long long)(CmpF(v0, v3) & 1)) & ((unsigned long long)(char)(CmpF(v0, v3)) >> 5 & 3 | (unsigned long long)(CmpF(v0, v3) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    v6 = arm64g_calculate_condition(192, (((((unsigned long long)(char)(CmpF(v5, v1)) >> 5 & 3 | (unsigned long long)(CmpF(v5, v1) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v5, v1)) >> 5 & 3 | (unsigned long long)(CmpF(v5, v1) & 1)) & ((unsigned long long)(char)(CmpF(v5, v1)) >> 5 & 3 | (unsigned long long)(CmpF(v5, v1) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    v7 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v5, v3)) >> 5 & 3 | (unsigned long long)(CmpF(v5, v3) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v5, v3)) >> 5 & 3 | (unsigned long long)(CmpF(v5, v3) & 1)) & ((unsigned long long)(char)(CmpF(v5, v3)) >> 5 & 3 | (unsigned long long)(CmpF(v5, v3) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    v9 = arm64g_calculate_condition(192, (((((unsigned long long)(char)(CmpF(v8, v1)) >> 5 & 3 | (unsigned long long)(CmpF(v8, v1) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v8, v1)) >> 5 & 3 | (unsigned long long)(CmpF(v8, v1) & 1)) & ((unsigned long long)(char)(CmpF(v8, v1)) >> 5 & 3 | (unsigned long long)(CmpF(v8, v1) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    v10 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v8, v3)) >> 5 & 3 | (unsigned long long)(CmpF(v8, v3) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v8, v3)) >> 5 & 3 | (unsigned long long)(CmpF(v8, v3) & 1)) & ((unsigned long long)(char)(CmpF(v8, v3)) >> 5 & 3 | (unsigned long long)(CmpF(v8, v3) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if (!((char)v10))
        return v12;
    return v11;
}
```

## `ColorGradingComponent.GetLiftValue` — RVA `0xcd0d84`

- Decompiled symbol: `ColorGradingComponent_GetLiftValue`
- Metadata signature: `public static Vector3 GetLiftValue(Color lift) { }`
- Native interval: `132` bytes
- Result: `pseudocode`

```c
unsigned long long ColorGradingComponent_GetLiftValue(void)
{
    unsigned long long v1;  // d8
    unsigned long long v2;  // x0
    unsigned long v11;  // 4301
    unsigned long v12;  // 4133
    unsigned long v13;  // 4129
    unsigned int v3;  // s2
    unsigned int v4;  // s0
    unsigned int v5;  // s1
    unsigned int v6;  // s3
    unsigned int v7;  // s3
    unsigned int v8;  // s0
    unsigned int v9;  // s1
    unsigned int v10;  // s2
    unsigned long long v0;  // [bp-0x10]

    v0 = v1;
    v2 = ColorGradingComponent__NormalizeColor();
    v6 = (v3 + v4 + v5) / 0x40400000;
    v8 = v7 + (v4 - v6) * 1036831949;
    v9 = v7 + (v5 - v6) * 1036831949;
    v10 = v7 + (v3 - v6) * 1036831949;
    v11 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v8, 0xbf800000)) >> 5 & 3 | (unsigned long long)(CmpF(v8, 0xbf800000) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v7 + (v4 - v6) * 1036831949, 0xbf800000)) >> 5 & 3 | (unsigned long long)(CmpF(v7 + (v4 - v6) * 1036831949, 0xbf800000) & 1)) & ((unsigned long long)(char)(CmpF(v7 + (v4 - v6) * 1036831949, 0xbf800000)) >> 5 & 3 | (unsigned long long)(CmpF(v7 + (v4 - v6) * 1036831949, 0xbf800000) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    v12 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v9, 0xbf800000)) >> 5 & 3 | (unsigned long long)(CmpF(v9, 0xbf800000) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v7 + (v5 - v6) * 1036831949, 0xbf800000)) >> 5 & 3 | (unsigned long long)(CmpF(v7 + (v5 - v6) * 1036831949, 0xbf800000) & 1)) & ((unsigned long long)(char)(CmpF(v7 + (v5 - v6) * 1036831949, 0xbf800000)) >> 5 & 3 | (unsigned long long)(CmpF(v7 + (v5 - v6) * 1036831949, 0xbf800000) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    v13 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v10, 0xbf800000)) >> 5 & 3 | (unsigned long long)(CmpF(v10, 0xbf800000) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v7 + (v3 - v6) * 1036831949, 0xbf800000)) >> 5 & 3 | (unsigned long long)(CmpF(v7 + (v3 - v6) * 1036831949, 0xbf800000) & 1)) & ((unsigned long long)(char)(CmpF(v7 + (v3 - v6) * 1036831949, 0xbf800000)) >> 5 & 3 | (unsigned long long)(CmpF(v7 + (v3 - v6) * 1036831949, 0xbf800000) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if (!((char)v13))
        return v2;
    return v2;
}
```

## `ColorGradingComponent.GetGammaValue` — RVA `0xcd0e08`

- Decompiled symbol: `ColorGradingComponent_GetGammaValue`
- Metadata signature: `public static Vector3 GetGammaValue(Color gamma) { }`
- Native interval: `228` bytes
- Result: `pseudocode`

```c
void ColorGradingComponent_GetGammaValue(void)
{
    unsigned long long v1;  // d14
    unsigned int v2;  // s3
    unsigned long v3;  // 4193
    unsigned int v5;  // s3
    unsigned int v6;  // s4
    unsigned int v7;  // s0
    unsigned long v8;  // 4237
    unsigned long v9;  // 4129
    unsigned long v10;  // 4129
    unsigned long long v0;  // [bp-0x40]

    v0 = v1;
    ColorGradingComponent__NormalizeColor();
    v3 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(v2, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v2, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v2, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v2, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v2, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v2, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    exp2f(exp2f(exp2f()));
    v5 = [D] unsupported_Iop_ZeroHI96ofV128();
    v6 = [D] unsupported_Iop_ZeroHI96ofV128();
    v7 = [D] unsupported_Iop_ZeroHI96ofV128();
    v8 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(0x3f800000 / v5, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(0x3f800000 / v5, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(0x3f800000 / v5, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(0x3f800000 / v5, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(0x3f800000 / v5, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(0x3f800000 / v5, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    v9 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(0x3f800000 / v6, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(0x3f800000 / v6, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(0x3f800000 / v6, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(0x3f800000 / v6, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(0x3f800000 / v6, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(0x3f800000 / v6, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    v10 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(0x3f800000 / v7, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(0x3f800000 / v7, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(0x3f800000 / v7, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(0x3f800000 / v7, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(0x3f800000 / v7, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(0x3f800000 / v7, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if (!((char)v10))
        return;
    return;
}
```

## `ColorGradingComponent.GetGainValue` — RVA `0xcd0eec`

- Decompiled symbol: `ColorGradingComponent_GetGainValue`
- Metadata signature: `public static Vector3 GetGainValue(Color gain) { }`
- Native interval: `184` bytes
- Result: `pseudocode`

```c
void ColorGradingComponent_GetGainValue(void)
{
    unsigned long long v7;  // d13
    unsigned long long v8;  // d12
    unsigned int v17;  // s11
    unsigned int v18;  // s3
    unsigned int v19;  // s3
    unsigned long v20;  // 4189
    unsigned int v21;  // s12
    unsigned int v23;  // s9
    unsigned int v24;  // s2
    unsigned int v25;  // s0
    unsigned long v26;  // 4163
    unsigned long long v9;  // d11
    unsigned long v27;  // 4153
    unsigned long v28;  // 4129
    unsigned long long v10;  // d10
    unsigned long long v11;  // d9
    unsigned long long v12;  // d8
    unsigned long long v13;  // x30
    unsigned int v14;  // s2
    unsigned int v15;  // s0
    unsigned int v16;  // s1
    unsigned long long v0;  // [bp-0x40]
    unsigned long long v1;  // [bp-0x38]
    unsigned long long v2;  // [bp-0x30]
    unsigned long long v3;  // [bp-0x28]
    unsigned long long v4;  // [bp-0x20]
    unsigned long long v5;  // [bp-0x18]
    unsigned long long v6;  // [bp-0x10]

    v0 = v7;
    v1 = v8;
    v2 = v9;
    v3 = v10;
    v4 = v11;
    v5 = v12;
    v6 = v13;
    ColorGradingComponent__NormalizeColor();
    v17 = (v14 + v15 + v16) / 0x40400000;
    v18 = 0x3f800000;
    v20 = arm64g_calculate_condition(192, (((((unsigned long long)(char)(CmpF(v19, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v19, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v19, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v19, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v19, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v19, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if ((char)v20)
        v18 = 0x40400000;
    v21 = v19 * v18;
    v23 = v21 + (v16 - v17) * 0x3f000000;
    exp2f(exp2f(exp2f()));
    v24 = v21 + (v14 - v17) * 0x3f000000;
    v25 = v21 + (v15 - v17) * 0x3f000000;
    v26 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v25, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v25, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v21 + (v15 - v17) * 0x3f000000, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v21 + (v15 - v17) * 0x3f000000, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v21 + (v15 - v17) * 0x3f000000, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v21 + (v15 - v17) * 0x3f000000, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    v27 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v23, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v23, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v21 + (v16 - v17) * 0x3f000000, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v21 + (v16 - v17) * 0x3f000000, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v21 + (v16 - v17) * 0x3f000000, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v21 + (v16 - v17) * 0x3f000000, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    v28 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v24, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v24, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v21 + (v14 - v17) * 0x3f000000, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v21 + (v14 - v17) * 0x3f000000, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v21 + (v14 - v17) * 0x3f000000, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v21 + (v14 - v17) * 0x3f000000, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if (!((char)v28))
        return;
    return;
}
```

## `ColorGradingComponent.CalculateLiftGammaGain` — RVA `0xcd0fa4`

- Decompiled symbol: `ColorGradingComponent_CalculateLiftGammaGain`
- Metadata signature: `public static void CalculateLiftGammaGain(Color lift, Color gamma, Color gain, out Vector3 outLift, out Vector3 outGamma, out Vector3 outGain) { }`
- Native interval: `156` bytes
- Result: `pseudocode`

```c
void ColorGradingComponent_CalculateLiftGammaGain(unsigned int *ptr, unsigned int *p, unsigned int *addr)
{
    unsigned int v3;  // s0
    unsigned int v4;  // s1
    unsigned int v5;  // s2
    unsigned int v6;  // s4
    unsigned int v7;  // s5
    unsigned int v8;  // s6
    unsigned int v0;  // [bp+0x0]
    unsigned int v1;  // [bp+0x4]
    unsigned int v2;  // [bp+0x8]

    ColorGradingComponent__GetLiftValue();
    *(ptr) = v3;
    ptr[1] = v4;
    ptr[2] = v5;
    ColorGradingComponent__GetGammaValue();
    *(p) = v6;
    p[1] = v7;
    p[2] = v8;
    ColorGradingComponent__GetGainValue();
    *(addr) = v0;
    addr[1] = v1;
    addr[2] = v2;
    return;
}
```

## `ColorGradingComponent.GetSlopeValue` — RVA `0xcd1040`

- Decompiled symbol: `ColorGradingComponent_GetSlopeValue`
- Metadata signature: `public static Vector3 GetSlopeValue(Color slope) { }`
- Native interval: `156` bytes
- Result: `pseudocode`

```c
unsigned long long ColorGradingComponent_GetSlopeValue(void)
{
    unsigned long long v1;  // d8
    unsigned long long v2;  // x0
    unsigned int v11;  // s2
    unsigned long v12;  // 4353
    unsigned long v13;  // 4133
    unsigned long v14;  // 4129
    unsigned int v3;  // s2
    unsigned int v4;  // s0
    unsigned int v5;  // s1
    unsigned int v6;  // s3
    unsigned int v7;  // s3
    unsigned int v8;  // s5
    unsigned int v9;  // s0
    unsigned int v10;  // s1
    unsigned long long v0;  // [bp-0x10]

    v0 = v1;
    v2 = ColorGradingComponent__NormalizeColor();
    v6 = (v3 + v4 + v5) / 0x40400000;
    v8 = v7 * 0x3f000000;
    v9 = v8 + (v4 - v6) * 1036831949 + 0x3f800000;
    v10 = v8 + (v5 - v6) * 1036831949 + 0x3f800000;
    v11 = v8 + (v3 - v6) * 1036831949 + 0x3f800000;
    v12 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v9, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v9, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v8 + (v4 - v6) * 1036831949 + 0x3f800000, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v8 + (v4 - v6) * 1036831949 + 0x3f800000, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v9, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v8 + (v4 - v6) * 1036831949 + 0x3f800000, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    v13 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v10, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v10, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v8 + (v5 - v6) * 1036831949 + 0x3f800000, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v8 + (v5 - v6) * 1036831949 + 0x3f800000, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v10, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v8 + (v5 - v6) * 1036831949 + 0x3f800000, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    v14 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v11, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v11, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v8 + (v3 - v6) * 1036831949 + 0x3f800000, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v8 + (v3 - v6) * 1036831949 + 0x3f800000, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v11, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v8 + (v3 - v6) * 1036831949 + 0x3f800000, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if (!((char)v14))
        return v2;
    return v2;
}
```

## `ColorGradingComponent.GetPowerValue` — RVA `0xcd10dc`

- Decompiled symbol: `ColorGradingComponent_GetPowerValue`
- Metadata signature: `public static Vector3 GetPowerValue(Color power) { }`
- Native interval: `184` bytes
- Result: `pseudocode`

```c
unsigned long long ColorGradingComponent_GetPowerValue(void)
{
    unsigned long long v1;  // d8
    unsigned long long v2;  // x0
    unsigned int v3;  // s0
    unsigned int v4;  // s1
    unsigned int v5;  // s2
    unsigned long v6;  // 4408
    unsigned long v7;  // 4133
    unsigned long v8;  // 4129
    unsigned long long v0;  // [bp-0x10]

    v0 = v1;
    v2 = ColorGradingComponent__NormalizeColor();
    v3 = [D] unsupported_Iop_ZeroHI96ofV128();
    v4 = [D] unsupported_Iop_ZeroHI96ofV128();
    v5 = [D] unsupported_Iop_ZeroHI96ofV128();
    v6 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(0x3f800000 / v3, 0x3f000000)) >> 5 & 3 | (unsigned long long)(CmpF(0x3f800000 / v3, 0x3f000000) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(0x3f800000 / v3, 0x3f000000)) >> 5 & 3 | (unsigned long long)(CmpF(0x3f800000 / v3, 0x3f000000) & 1)) & ((unsigned long long)(char)(CmpF(0x3f800000 / v3, 0x3f000000)) >> 5 & 3 | (unsigned long long)(CmpF(0x3f800000 / v3, 0x3f000000) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    v7 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(0x3f800000 / v4, 0x3f000000)) >> 5 & 3 | (unsigned long long)(CmpF(0x3f800000 / v4, 0x3f000000) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(0x3f800000 / v4, 0x3f000000)) >> 5 & 3 | (unsigned long long)(CmpF(0x3f800000 / v4, 0x3f000000) & 1)) & ((unsigned long long)(char)(CmpF(0x3f800000 / v4, 0x3f000000)) >> 5 & 3 | (unsigned long long)(CmpF(0x3f800000 / v4, 0x3f000000) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    v8 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(0x3f800000 / v5, 0x3f000000)) >> 5 & 3 | (unsigned long long)(CmpF(0x3f800000 / v5, 0x3f000000) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(0x3f800000 / v5, 0x3f000000)) >> 5 & 3 | (unsigned long long)(CmpF(0x3f800000 / v5, 0x3f000000) & 1)) & ((unsigned long long)(char)(CmpF(0x3f800000 / v5, 0x3f000000)) >> 5 & 3 | (unsigned long long)(CmpF(0x3f800000 / v5, 0x3f000000) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if (!((char)v8))
        return v2;
    return v2;
}
```

## `ColorGradingComponent.GetOffsetValue` — RVA `0xcd1194`

- Decompiled symbol: `ColorGradingComponent_GetOffsetValue`
- Metadata signature: `public static Vector3 GetOffsetValue(Color offset) { }`
- Native interval: `148` bytes
- Result: `pseudocode`

```c
unsigned long long ColorGradingComponent_GetOffsetValue(void)
{
    unsigned long long v1;  // d8
    unsigned long long v2;  // x0
    unsigned int v11;  // s2
    unsigned long v12;  // 4322
    unsigned long v13;  // 4133
    unsigned long v14;  // 4129
    unsigned int v3;  // s2
    unsigned int v4;  // s0
    unsigned int v5;  // s1
    unsigned int v6;  // s3
    unsigned int v7;  // s3
    unsigned int v8;  // s4
    unsigned int v9;  // s0
    unsigned int v10;  // s1
    unsigned long long v0;  // [bp-0x10]

    v0 = v1;
    v2 = ColorGradingComponent__NormalizeColor();
    v6 = (v3 + v4 + v5) / 0x40400000;
    v8 = v7 * 0x3f000000;
    v9 = v8 + (v4 - v6) * 1028443341;
    v10 = v8 + (v5 - v6) * 1028443341;
    v11 = v8 + (v3 - v6) * 1028443341;
    v12 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v9, 3209481421)) >> 5 & 3 | (unsigned long long)(CmpF(v9, 3209481421) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v8 + (v4 - v6) * 1028443341, 3209481421)) >> 5 & 3 | (unsigned long long)(CmpF(v8 + (v4 - v6) * 1028443341, 3209481421) & 1)) & ((unsigned long long)(char)(CmpF(v8 + (v4 - v6) * 1028443341, 3209481421)) >> 5 & 3 | (unsigned long long)(CmpF(v8 + (v4 - v6) * 1028443341, 3209481421) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    v13 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v10, 3209481421)) >> 5 & 3 | (unsigned long long)(CmpF(v10, 3209481421) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v8 + (v5 - v6) * 1028443341, 3209481421)) >> 5 & 3 | (unsigned long long)(CmpF(v8 + (v5 - v6) * 1028443341, 3209481421) & 1)) & ((unsigned long long)(char)(CmpF(v8 + (v5 - v6) * 1028443341, 3209481421)) >> 5 & 3 | (unsigned long long)(CmpF(v8 + (v5 - v6) * 1028443341, 3209481421) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    v14 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v11, 3209481421)) >> 5 & 3 | (unsigned long long)(CmpF(v11, 3209481421) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v8 + (v3 - v6) * 1028443341, 3209481421)) >> 5 & 3 | (unsigned long long)(CmpF(v8 + (v3 - v6) * 1028443341, 3209481421) & 1)) & ((unsigned long long)(char)(CmpF(v8 + (v3 - v6) * 1028443341, 3209481421)) >> 5 & 3 | (unsigned long long)(CmpF(v8 + (v3 - v6) * 1028443341, 3209481421) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if (!((char)v14))
        return v2;
    return v2;
}
```

## `ColorGradingComponent.CalculateSlopePowerOffset` — RVA `0xcd1228`

- Decompiled symbol: `ColorGradingComponent_CalculateSlopePowerOffset`
- Metadata signature: `public static void CalculateSlopePowerOffset(Color slope, Color power, Color offset, out Vector3 outSlope, out Vector3 outPower, out Vector3 outOffset) { }`
- Native interval: `156` bytes
- Result: `pseudocode`

```c
unsigned long long ColorGradingComponent_CalculateSlopePowerOffset(unsigned int *ptr, unsigned int *p, unsigned int *addr)
{
    unsigned int v3;  // s0
    unsigned int v4;  // s1
    unsigned int v5;  // s2
    unsigned int v6;  // s4
    unsigned int v7;  // s5
    unsigned int v8;  // s6
    unsigned long long v9;  // x0
    unsigned int v0;  // [bp+0x0]
    unsigned int v1;  // [bp+0x4]
    unsigned int v2;  // [bp+0x8]

    ColorGradingComponent__GetSlopeValue();
    *(ptr) = v3;
    ptr[1] = v4;
    ptr[2] = v5;
    ColorGradingComponent__GetPowerValue();
    *(p) = v6;
    p[1] = v7;
    p[2] = v8;
    v9 = ColorGradingComponent__GetOffsetValue();
    *(addr) = v0;
    addr[1] = v1;
    addr[2] = v2;
    return v9;
}
```

## `ColorGradingComponent.GetCurveFormat` — RVA `0xcd12c4`

- Decompiled symbol: `ColorGradingComponent_GetCurveFormat`
- Metadata signature: `private TextureFormat GetCurveFormat() { }`
- Native interval: `40` bytes
- Result: `pseudocode`

```c
unsigned int ColorGradingComponent_GetCurveFormat(void)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    unsigned long v4;  // 4116
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    v4 = arm64g_calculate_condition(25, (unsigned long long)((unsigned int)(unsigned long long)SystemInfo__SupportsTextureFormat(17, 0) & 1), 0, 0);
    if (!((char)v4))
        return 4;
    return 17;
}
```

## `ColorGradingComponent.GetCurveTexture` — RVA `0xcd12ec`

- Decompiled symbol: `ColorGradingComponent_GetCurveTexture`
- Metadata signature: `private Texture2D GetCurveTexture() { }`
- Native interval: `820` bytes
- Result: `pseudocode`
- Heuristic layout hint: `ColorGradingComponent_Recovered` matched 2 offsets against `ColorGradingComponent` metadata (confidence 0.67).

```c
typedef struct ColorGradingComponent_Recovered {
    char padding_0[24];
    struct struct_3 *field_18;
    long long m_GradingCurves;
    struct struct_1 *m_pixels;
} ColorGradingComponent_Recovered;

typedef struct struct_1 {
    char padding_0[24];
    unsigned int field_18;
} struct_1;

typedef struct struct_3 {
    char padding_0[216];
    long long field_d8;
    long long field_e0;
    long long field_e8;
    long long field_f0;
    long long field_f8;
    long long field_100;
    long long field_108;
    long long field_110;
} struct_3;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern long long g_1ef1cc0;
extern long long g_1efa0e0;
extern long long g_1f0b0f0;
extern char g_1fab5b7;

long long ColorGradingComponent_GetCurveTexture(struct_2 *ptr3)
{
    struct_2 *ptr4;  // x23
    unsigned long v4;  // 4120
    long long v13;  // x26
    long long v14;  // x27
    long long v15;  // x28
    unsigned long v16;  // x29
    unsigned long long v17;  // x20
    unsigned int v18;  // s8
    unsigned long v19;  // x0
    struct_1 *v20;  // x8
    void* addr;  // x8
    struct_1 *v22;  // x8
    unsigned int v5;  // w22
    void* p;  // x8
    long long v6;  // x21
    long long ptr[35];  // x8
    long long v8;  // x21
    long long v9;  // x22
    long long v10;  // x23
    long long v11;  // x24
    long long v12;  // x25
    struct_2 *v0;  // [bp-0x88]
    char *v1;  // [bp-0x60]
    char v2;  // [bp+0x0]

    v1 = &v2;
    if (!(g_1fab5b7 & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c(&g_1efa0e0);
        sub_f7d92c(&g_1ef1cc0);
        sub_f7d92c(&g_1f0b0f0);
        g_1fab5b7 = 1;
    }
    ptr4 = &ptr3->field_20;
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (((char)Object__op_Equality(ptr3->field_20, 0, 0) & 1))
    {
        v4 = arm64g_calculate_condition(25, (unsigned long long)((unsigned int)(unsigned long long)SystemInfo__SupportsTextureFormat(17, 0) & 1), 0, 0);
        if ((char)v4)
            v5 = 17;
        else
            v5 = 4;
        v6 = sub_f7db70();
        Texture2D__ctor(v6, 128, 2, v5, 0, 1, 0);
        if (!v6)
            sub_f7db7c(sub_f7db74());
        Object__set_name(v6, g_1f0b0f0, 0);
        Object__set_hideFlags(v6, 52, 0);
        Texture__set_anisoLevel(v6, 0, 0);
        Texture__set_wrapMode(v6, 1, 0);
        Texture__set_filterMode(v6, 1, 0);
        *((long long *)&ptr4->padding_0[0]) = v6;
        sub_f7d8d0(ptr4, v6);
    }
    ptr = ptr3->field_18;
    if (ptr)
    {
        v8 = ptr[31];
        if (v8)
        {
            v0 = ptr4;
            v9 = ptr[27];
            v10 = ptr[28];
            v11 = ptr[29];
            v12 = ptr[30];
            v13 = ptr[32];
            v14 = ptr[33];
            v15 = ptr[34];
            ColorGradingCurve__Cache(v8, 0);
            if (v13)
            {
                ColorGradingCurve__Cache(v13, 0);
                v16 = 0;
                v17 = 2092;
                while (true)
                {
                    v18 = (int)v16 * 0x3c000000;
                    ColorGradingCurve__Evaluate(v8, 0);
                    ColorGradingCurve__Evaluate(v13, 0);
                    if (!v14 || !((ColorGradingCurve__Evaluate(v14, 0), v15 && (v19 = (unsigned long)(unsigned long long)ColorGradingCurve__Evaluate(v15, 0), v20 = (struct_1 *)ptr3->field_28, v20))))
                        break;
                    if (v20->field_18 <= v16)
                        sub_f7db7c(ColorGradingCurve__Evaluate(v15, 0));
                    addr = &v20->padding_0[v17];
                    *((unsigned int *)&addr[2060]) = v18;
                    *((unsigned int *)&addr[2056]) = v18;
                    *((unsigned int *)&addr[2052]) = v18;
                    *((unsigned int *)&addr[0x800]) = v18;
                    if (!v9 || !((ColorGradingCurve__Evaluate(v9, 0), v10 && (ColorGradingCurve__Evaluate(v10, 0), v11 && (ColorGradingCurve__Evaluate(v11, 0), v12 && (v19 = (unsigned long)(unsigned long long)ColorGradingCurve__Evaluate(v12, 0), v22 = (struct_1 *)ptr3->field_28, v22))))))
                        break;
                    if (v22->field_18 <= v16 + 128)
                        sub_f7db7c(ColorGradingCurve__Evaluate(v12, 0));
                    v16 += 1;
                    p = &v22->padding_0[v17];
                    v17 += 16;
                    *((unsigned int *)&p[12]) = v18;
                    *((unsigned int *)&p[8]) = v18;
                    *((unsigned int *)&p[4]) = v18;
                    *((unsigned int *)p) = v18;
                    if (v16 == 128 && *((long long *)&v0->padding_0[0]))
                    {
                        Texture2D__SetPixels(*((long long *)&v0->padding_0[0]), ptr3->field_28, 0);
                        if (ptr3->field_20)
                        {
                            Texture2D__Apply(ptr3->field_20, 0, 0, 0);
                            return *((long long *)&v0->padding_0[0]);
                        }
                        break;
                    }
                }
            }
        }
    }
    sub_f7db7c(sub_f7db74());
}
```

## `ColorGradingComponent.IsLogLutValid` — RVA `0xcd1620`

- Decompiled symbol: `ColorGradingComponent_IsLogLutValid`
- Metadata signature: `private bool IsLogLutValid(RenderTexture lut) { }`
- Native interval: `156` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[408];
    struct struct_2 *field_198;
    unsigned long long field_1a0;
} struct_1;

typedef struct struct_2 {
    unsigned long long field_0;
} struct_2;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab5b8;

unsigned int ColorGradingComponent_IsLogLutValid(unsigned long a0, struct_1 **a1)
{
    unsigned long long flag;  // x2
    struct_1 **v1;  // x0
    unsigned long v2;  // x1

    if (!(g_1fab5b8 & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab5b8 = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    flag = 0;
    if (!((char)Object__op_Inequality(a1, 0, 0) & 1))
    {
        return 0;
    }
    else if (!a1)
    {
        sub_f7db74();
    }
    else if (((char)RenderTexture__IsCreated(a1, 0) & 1))
    {
        v1 = a1;
        v2 = *(a1)->field_1a0;
        *(a1)->field_198();
    }
    else
    {
        return 0;
    }
}
```

## `ColorGradingComponent.GetLutFormat` — RVA `0xcd16bc`

- Decompiled symbol: `ColorGradingComponent_GetLutFormat`
- Metadata signature: `private RenderTextureFormat GetLutFormat() { }`
- Native interval: `36` bytes
- Result: `pseudocode`

```c
unsigned int ColorGradingComponent_GetLutFormat(void)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    unsigned long v4;  // 4113
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    v4 = arm64g_calculate_condition(25, (unsigned long long)((unsigned int)(unsigned long long)SystemInfo__SupportsRenderTextureFormat(2, 0) & 1), 0, 0);
    if (!((char)v4))
        return 0;
    return 2;
}
```

## `ColorGradingComponent.GenerateLut` — RVA `0xcd16e0`

- Decompiled symbol: `ColorGradingComponent_GenerateLut`
- Metadata signature: `private void GenerateLut() { }`
- Native interval: `1868` bytes
- Result: `pseudocode`
- Heuristic layout hint: `ColorGradingComponent_Recovered` matched 2 offsets against `ColorGradingComponent` metadata (confidence 0.67).

```c
typedef struct ColorGradingComponent_Recovered {
    char padding_0[24];
    struct struct_3 *field_18;
    long long m_GradingCurves;
    struct struct_1 *m_pixels;
} ColorGradingComponent_Recovered;

typedef struct struct_6 {
    char padding_0[24];
    unsigned int field_18;
    char padding_1c[16];
    unsigned int field_2c;
    unsigned int field_30;
    char padding_34[4];
    unsigned int field_38;
    unsigned int field_3c;
    unsigned int field_40;
    unsigned int field_44;
    unsigned int field_48;
    unsigned int field_4c;
    unsigned int field_50;
    unsigned int field_54;
    char padding_58[4];
    unsigned int field_5c;
    unsigned int field_60;
    char padding_64[20];
    unsigned int field_78;
    unsigned int field_7c;
    unsigned int field_80;
    unsigned int field_84;
    unsigned int field_88;
    unsigned int field_8c;
    unsigned int field_90;
    unsigned int field_94;
    unsigned int field_98;
    unsigned int field_9c;
    unsigned int field_a0;
    unsigned int field_a4;
    unsigned int field_a8;
    unsigned int field_ac;
    unsigned int field_b0;
    unsigned int field_b4;
    unsigned int field_b8;
    unsigned int field_bc;
    unsigned int field_c0;
    unsigned int field_c4;
    unsigned int field_c8;
    unsigned int field_cc;
    unsigned int field_d0;
    unsigned int field_d4;
    char padding_d8[80];
    unsigned long long field_128;
} struct_6;

typedef struct struct_3 {
    char padding_0[32];
    unsigned long long field_20;
} struct_3;

typedef struct struct_1 {
    char padding_0[184];
    struct ColorGradingComponent_Recovered *field_b8;
    char padding_c0[32];
    unsigned int field_e0;
} struct_1;

typedef struct struct_3 {
    char padding_0[216];
    long long field_d8;
    long long field_e0;
    long long field_e8;
    long long field_f0;
    long long field_f8;
    long long field_100;
    long long field_108;
    long long field_110;
} struct_3;

typedef struct struct_1 {
    char padding_0[24];
    unsigned int field_18;
} struct_1;

typedef struct ColorGradingComponent_Recovered {
    unsigned int field_0;
    unsigned int field_4;
    unsigned int field_8;
    unsigned int field_c;
    unsigned int field_10;
    unsigned int field_14;
    unsigned int field_18;
    unsigned int field_1c;
    unsigned int field_20;
    unsigned int field_24;
    unsigned int field_28;
    unsigned int field_2c;
    unsigned int field_30;
    unsigned int field_34;
    unsigned int field_38;
    unsigned int field_3c;
    unsigned int field_40;
} struct_2;

extern long long g_1ef1298;
extern struct_1 *g_1ef2de0;
extern long long g_1efa0e0;
extern long long g_1f093c8;
extern long long g_1f0aa90;
extern long long g_1f0e090;
extern long long g_1f0e098;
extern char g_1fab5b9;

void ColorGradingComponent_GenerateLut(struct_2 *p, unsigned long a1)
{
    unsigned long long v68;  // d15
    unsigned long long v69;  // d14
    unsigned long long v78;  // x22
    unsigned long long v79;  // x21
    unsigned long long v80;  // x20
    unsigned long long v81;  // x19
    struct_2 *v82;  // x0
    struct_2 *v83;  // x0
    struct_2 *v84;  // x0
    struct_6 *ptr;  // x8
    unsigned int flag12;  // w23
    struct_6 *addr;  // x22
    unsigned long long v70;  // d13
    unsigned long v88;  // 4117
    unsigned int v89;  // w21
    long long v90;  // x20
    long long v91;  // x20
    struct_1 *v92;  // x0
    struct_1 *v93;  // x0
    long long v94;  // x0
    unsigned long long v71;  // d12
    unsigned long long v72;  // d11
    unsigned long long v73;  // d10
    unsigned long long v74;  // d9
    unsigned long long v75;  // d8
    unsigned long long v76;  // x30
    unsigned long long v77;  // x23
    unsigned int v0;  // [bp-0x180]
    unsigned int v1;  // [bp-0x17c]
    unsigned int v2;  // [bp-0x178]
    unsigned int v3;  // [bp-0x174]
    unsigned int v4;  // [bp-0x168]
    unsigned int v5;  // [bp-0x164]
    unsigned int v6;  // [bp-0x160]
    unsigned int v7;  // [bp-0x15c]
    unsigned int v8;  // [bp-0x158]
    unsigned int v9;  // [bp-0x154]
    unsigned int v10;  // [bp-0x150]
    unsigned int v11;  // [bp-0x14c]
    unsigned int v12;  // [bp-0x148]
    unsigned int v13;  // [bp-0x144]
    unsigned int v14;  // [bp-0x140]
    unsigned int v15;  // [bp-0x13c]
    unsigned int v16;  // [bp-0x138]
    unsigned int v17;  // [bp-0x134]
    unsigned int v18;  // [bp-0x130]
    unsigned int v19;  // [bp-0x12c]
    unsigned int v20;  // [bp-0x128]
    unsigned int v21;  // [bp-0x124]
    unsigned int v22;  // [bp-0x120]
    unsigned int v23;  // [bp-0x11c]
    unsigned int v24;  // [bp-0x118]
    unsigned int v25;  // [bp-0x114]
    unsigned int v26;  // [bp-0x110]
    unsigned int v27;  // [bp-0x10c]
    unsigned int v28;  // [bp-0x108]
    unsigned int v29;  // [bp-0x104]
    unsigned int v30;  // [bp-0x100]
    unsigned int v31;  // [bp-0xfc]
    unsigned int v32;  // [bp-0xf8]
    unsigned int v33;  // [bp-0xf4]
    unsigned int v34;  // [bp-0xf0]
    unsigned int v35;  // [bp-0xec]
    unsigned int v36;  // [bp-0xe8]
    unsigned int v37;  // [bp-0xe4]
    unsigned int flag11[2];  // [bp-0xe0]
    unsigned int flag5;  // [bp-0xd8]
    unsigned int flag10[2];  // [bp-0xd0]
    unsigned int flag4;  // [bp-0xc8]
    unsigned int flag9[2];  // [bp-0xc0]
    unsigned int flag3;  // [bp-0xb8]
    unsigned int flag8[2];  // [bp-0xb0]
    unsigned int flag2;  // [bp-0xa8]
    unsigned int flag7[2];  // [bp-0xa0]
    unsigned int choice;  // [bp-0x98]
    unsigned int flag6[2];  // [bp-0x90]
    unsigned int flag;  // [bp-0x88]
    unsigned long long v50;  // [bp-0x80]
    unsigned long long v51;  // [bp-0x78]
    unsigned long long v52;  // [bp-0x70]
    unsigned long long v53;  // [bp-0x68]
    unsigned long long v54;  // [bp-0x60]
    unsigned long long v55;  // [bp-0x58]
    unsigned long long v56;  // [bp-0x50]
    unsigned long long v57;  // [bp-0x48]
    char *v58;  // [bp-0x40]
    unsigned int v59;  // [bp-0x38]
    unsigned int v60;  // [bp-0x34]
    unsigned long long v61;  // [bp-0x30]
    unsigned long long v62;  // [bp-0x28]
    unsigned long long v63;  // [bp-0x20]
    unsigned long long v64;  // [bp-0x18]
    unsigned long long v65;  // [bp-0x10]
    unsigned long long v66;  // [bp-0x8]
    char v67;  // [bp+0x0]

    v50 = v68;
    v51 = v69;
    v52 = v70;
    v53 = v71;
    v54 = v72;
    v55 = v73;
    v56 = v74;
    v57 = v75;
    v58 = &v67;
    v61 = v76;
    v62 = v77;
    v63 = v78;
    v64 = v79;
    v65 = v80;
    v66 = v81;
    v82 = p;
    if (!(g_1fab5b9 & 1))
    {
        sub_f7d92c("g=");
        sub_f7d92c(&g_1efa0e0);
        sub_f7d92c(&g_1ef1298);
        sub_f7d92c(&g_1ef2de0);
        sub_f7d92c(&g_1f0e098);
        sub_f7d92c(&g_1f093c8);
        sub_f7d92c(&g_1f0e090);
        v83 = sub_f7d92c(&g_1f0aa90);
        g_1fab5b9 = 1;
        v82 = v83;
    }
    v84 = v82;
    flag = 0;
    flag6 = 0;
    choice = 0;
    flag7 = 0;
    flag2 = 0;
    flag8 = 0;
    flag3 = 0;
    flag9 = 0;
    flag4 = 0;
    flag10 = 0;
    flag5 = 0;
    flag11 = 0;
    ptr = p->field_18;
    if (ptr)
    {
        flag12 = ptr->field_18;
        v4 = ptr->field_30;
        v5 = ptr->field_2c;
        v21 = ptr->field_3c;
        v22 = ptr->field_38;
        v6 = ptr->field_40;
        v9 = ptr->field_44;
        v10 = ptr->field_48;
        v36 = ptr->field_50;
        v37 = ptr->field_4c;
        v60 = ptr->field_5c;
        v59 = ptr->field_60;
        v34 = ptr->field_78;
        v35 = ptr->field_54;
        v32 = ptr->field_80;
        v33 = ptr->field_7c;
        v30 = ptr->field_88;
        v31 = ptr->field_84;
        v28 = ptr->field_90;
        v29 = ptr->field_8c;
        v26 = ptr->field_98;
        v27 = ptr->field_94;
        v24 = ptr->field_a0;
        v25 = ptr->field_9c;
        v23 = ptr->field_a4;
        v19 = ptr->field_b0;
        v20 = ptr->field_ac;
        v17 = ptr->field_b8;
        v18 = ptr->field_b4;
        v15 = ptr->field_c0;
        v16 = ptr->field_bc;
        v13 = ptr->field_a8;
        v14 = ptr->field_c4;
        v11 = ptr->field_cc;
        v12 = ptr->field_c8;
        v7 = ptr->field_d4;
        v8 = ptr->field_d0;
        if (((char)ColorGradingComponent__IsLogLutValid(v84, ptr->field_128) & 1))
        {
LABEL_10d1980:
            if (*((long long *)&p->padding_0[16]) && *((long long *)(*((long long *)&p->padding_0[16]) + 32)))
            {
                v91 = MaterialFactory__Get(*((long long *)(*((long long *)&p->padding_0[16]) + 32)), g_1f0aa90, 0);
                if (!g_1ef2de0->field_e0)
                    sub_f7da5c(g_1ef2de0);
                if (v91)
                {
                    Material__SetVector(v91, g_1ef2de0->field_b8->field_0, 0);
                    Material__set_shaderKeywords(v91, 0, 0);
                    if (flag12 != 1)
                    {
                        if (flag12 == 2)
                        {
                            Material__EnableKeyword(v91, g_1f0e098, 0);
                            v92 = g_1ef2de0;
                            if (!g_1ef2de0->field_e0)
                            {
                                sub_f7da5c(g_1ef2de0);
                                v92 = g_1ef2de0;
                            }
                            Material__SetVector(v91, v92->field_b8->field_4, 0);
                            Material__SetVector(v91, g_1ef2de0->field_b8->field_8, 0);
                        }
                    }
                    else
                    {
                        Material__EnableKeyword(v91, g_1f0e090, 0);
                    }
                    v93 = g_1ef2de0;
                    if (!g_1ef2de0->field_e0)
                    {
                        sub_f7da5c(g_1ef2de0);
                        v93 = g_1ef2de0;
                    }
                    Material__SetFloat(v91, v93->field_b8->field_c, 0);
                    Material__SetFloat(v91, g_1ef2de0->field_b8->field_10, 0);
                    Material__SetFloat(v91, g_1ef2de0->field_b8->field_14, 0);
                    ColorGradingComponent__CalculateColorBalance();
                    Material__SetVector(v91, g_1ef2de0->field_b8->field_18, 0);
                    v2 = v8;
                    v3 = v7;
                    v0 = v12;
                    v1 = v11;
                    ColorGradingComponent__CalculateLiftGammaGain(&flag6, &flag7, &flag8);
                    Material__SetVector(v91, g_1ef2de0->field_b8->field_1c, 0);
                    Material__SetVector(v91, g_1ef2de0->field_b8->field_20, 0);
                    Material__SetVector(v91, g_1ef2de0->field_b8->field_24, 0);
                    v3 = v23;
                    v2 = v24;
                    v1 = v25;
                    v0 = v26;
                    ColorGradingComponent__CalculateSlopePowerOffset(&flag9, &flag10, &flag11);
                    Material__SetVector(v91, g_1ef2de0->field_b8->field_28, 0);
                    Material__SetVector(v91, g_1ef2de0->field_b8->field_2c, 0);
                    Material__SetVector(v91, g_1ef2de0->field_b8->field_30, 0);
                    Material__SetVector(v91, g_1ef2de0->field_b8->field_34, 0);
                    Material__SetVector(v91, g_1ef2de0->field_b8->field_38, 0);
                    Material__SetVector(v91, g_1ef2de0->field_b8->field_3c, 0);
                    v94 = ColorGradingComponent__GetCurveTexture(p);
                    Material__SetTexture(v91, g_1ef2de0->field_b8->field_40, v94, 0);
                    if (p->field_18)
                    {
                        if (!g_1eefbb8->field_e0)
                            sub_f7da5c(g_1eefbb8);
                        Graphics__Blit();
                        return;
                    }
                }
            }
        }
        else if (p->field_18)
        {
            GraphicsUtils__Destroy(*((long long *)&p->field_18[1].padding_0[16]), 0);
            addr = p->field_18;
            v88 = arm64g_calculate_condition(25, (unsigned long long)((unsigned int)(unsigned long long)SystemInfo__SupportsRenderTextureFormat(2, 0) & 1), 0, 0);
            if ((char)v88)
                v89 = 2;
            else
                v89 = 0;
            v90 = sub_f7db70();
            RenderTexture__ctor(v90, 0x400, 32, 0, v89, 0);
            if (v90)
            {
                Object__set_name(v90, g_1f093c8, 0);
                Object__set_hideFlags(v90, 52, 0);
                Texture__set_filterMode(v90, 1, 0);
                Texture__set_wrapMode(v90, 1, 0);
                Texture__set_anisoLevel(v90, 0, 0);
                if (addr)
                {
                    addr->field_128 = v90;
                    sub_f7d8d0((struct struct_6 *)&addr->field_128, v90);
                    goto LABEL_10d1980;
                }
            }
        }
    }
    sub_f7db74();
}
```

## `ColorGradingComponent.Prepare` — RVA `0xcd1e2c`

- Decompiled symbol: `ColorGradingComponent_Prepare`
- Metadata signature: `public override void Prepare(Material uberMaterial) { }`
- Native interval: `472` bytes
- Result: `pseudocode`
- Heuristic layout hint: `ColorGradingComponent_Recovered` matched 2 offsets against `ColorGradingComponent` metadata (confidence 0.67).

```c
typedef struct ColorGradingComponent_Recovered {
    char padding_0[24];
    struct struct_3 *field_18;
    long long m_GradingCurves;
    struct struct_1 *m_pixels;
} ColorGradingComponent_Recovered;

typedef struct struct_13 {
    char padding_0[288];
    char field_120;
    char padding_121[7];
    struct struct_14 *field_128;
} struct_13;

typedef struct struct_11 {
    char padding_0[376];
    struct struct_12 *field_178;
    unsigned long long field_180;
} struct_11;

typedef struct struct_6 {
    char padding_0[16];
    struct struct_7 *field_10;
} struct_6;

typedef struct struct_5 {
    char padding_0[24];
    struct struct_4 *field_18;
} struct_5;

typedef struct struct_4 {
    char padding_0[20];
    unsigned int field_14;
} struct_4;

typedef struct struct_1 {
    char padding_0[184];
    struct struct_0 *field_b8;
    char padding_c0[32];
    unsigned int field_e0;
} struct_1;

typedef struct struct_3 {
    char padding_0[216];
    long long field_d8;
    long long field_e0;
    long long field_e8;
    long long field_f0;
    long long field_f8;
    long long field_100;
    long long field_108;
    long long field_110;
} struct_3;

typedef struct struct_1 {
    char padding_0[24];
    unsigned int field_18;
} struct_1;

typedef struct struct_14 {
    struct struct_11 *field_0;
} struct_14;

typedef struct struct_12 {
    unsigned long long field_0;
} struct_12;

typedef struct struct_7 {
    char padding_0[24];
    struct struct_8 *field_18;
} struct_7;

typedef struct struct_0 {
    char padding_0[68];
    unsigned int field_44;
} struct_0;

typedef struct struct_8 {
    char padding_0[20];
    unsigned int field_14;
} struct_8;

extern struct_1 *g_1ef2de0;
extern long long g_1efa0e0;
extern long long g_1f08c78;
extern long long g_1f08c80;
extern char g_1fab5ba;

void ColorGradingComponent_Prepare(struct_2 *ptr, struct_2 **a1)
{
    unsigned long long v8;  // x30
    unsigned long long v9;  // x25
    struct_2 *v18;  // x0
    struct_13 *p;  // x8
    struct_2 **v20;  // x1
    struct_11 **v21;  // x1
    struct_11 **v22;  // x21
    struct_1 *v23;  // x0
    struct_11 **v24;  // x2
    unsigned long long flag;  // x3
    struct_11 **v26;  // x0
    unsigned long v27;  // x1
    unsigned long long v10;  // x24
    unsigned long long v11;  // x23
    unsigned long long v12;  // x22
    unsigned long long v13;  // x21
    unsigned long long v14;  // x20
    unsigned long long v15;  // x19
    struct_2 *v16;  // x0
    struct_2 *v17;  // x0
    unsigned long long v0;  // [bp-0x40]
    unsigned long long v1;  // [bp-0x38]
    unsigned long long v2;  // [bp-0x30]
    unsigned long long v3;  // [bp-0x28]
    unsigned long long v4;  // [bp-0x20]
    unsigned long long v5;  // [bp-0x18]
    unsigned long long v6;  // [bp-0x10]
    unsigned long long v7;  // [bp-0x8]

    v0 = v8;
    v1 = v9;
    v2 = v10;
    v3 = v11;
    v4 = v12;
    v5 = v13;
    v6 = v14;
    v7 = v15;
    v16 = ptr;
    if (!(g_1fab5ba & 1))
    {
        sub_f7d92c(&g_1efa0e0);
        sub_f7d92c(&g_1ef2de0);
        sub_f7d92c(&g_1f08c78);
        v17 = sub_f7d92c(&g_1f08c80);
        g_1fab5ba = 1;
        v16 = v17;
    }
    v18 = v16;
    p = ptr->field_18;
    if (p)
    {
        v20 = a1;
        if (p->field_120 || !((v21 = (struct_11 **)p->field_128, v20 = (struct_2 **)p->field_128, ((char)(unsigned long long)ColorGradingComponent__IsLogLutValid(v18, v20) & 1))))
        {
            ColorGradingComponent__GenerateLut(ptr, v20); /* do not return */
        }
        else if (*((long long *)&ptr->padding_0[16]) && *((long long *)(*((long long *)&ptr->padding_0[16]) + 16)) && *((long long *)(*((long long *)(*((long long *)&ptr->padding_0[16]) + 16)) + 24)) && a1)
        {
            Material__EnableKeyword();
            if (ptr->field_18)
            {
                v22 = *((long long *)&ptr->field_18[1].padding_0[16]);
                v23 = g_1ef2de0;
                if (!g_1ef2de0->field_e0)
                {
                    sub_f7da5c(g_1ef2de0);
                    v23 = g_1ef2de0;
                }
                v24 = v22;
                flag = 0;
                Material__SetTexture(a1, v23->field_b8->field_44, v22, 0);
                if (v22)
                {
                    v26 = v22;
                    v27 = *(v22)->field_180;
                    *(v22)->field_178();
                }
            }
        }
    }
    sub_f7db74();
}
```

## `ColorGradingComponent.OnGUI` — RVA `0xcd2004`

- Decompiled symbol: `ColorGradingComponent_OnGUI`
- Metadata signature: `public void OnGUI() { }`
- Native interval: `240` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    long long field_10;
    unsigned long long field_18;
} struct_0;

extern long long g_1efa0e0;
extern char g_1fab5bb;

long long ColorGradingComponent_OnGUI(struct_0 *a0)
{
    unsigned long long v6;  // d8
    unsigned long long v7;  // x30
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
    if (!(g_1fab5bb & 1))
    {
        sub_f7d92c("O<");
        sub_f7d92c(&g_1efa0e0);
        g_1fab5bb = 1;
    }
    if (a0->field_18 && a0->field_10)
        PostProcessingContext__get_viewport(a0->field_10, 0); /* do not return */
    sub_f7db74();
}
```

## `ColorGradingComponent.OnDisable` — RVA `0xcd20f4`

- Decompiled symbol: `ColorGradingComponent_OnDisable`
- Metadata signature: `public override void OnDisable() { }`
- Native interval: `132` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[24];
    struct struct_0 *field_18;
    long long field_20;
} struct_1;

typedef struct struct_0 {
    char padding_0[296];
    long long field_128;
} struct_0;

extern long long g_1efa0e0;
extern char g_1fab5bc;

void ColorGradingComponent_OnDisable(struct_1 *ptr)
{
    unsigned long long v3;  // x30
    unsigned long long v4;  // x20
    unsigned long long v5;  // x19
    struct_1 *v6;  // x20
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x10]
    unsigned long long v2;  // [bp-0x8]

    v0 = v3;
    v1 = v4;
    v2 = v5;
    if (!(g_1fab5bc & 1))
    {
        sub_f7d92c(&g_1efa0e0);
        g_1fab5bc = 1;
    }
    v6 = &ptr->field_20;
    GraphicsUtils__Destroy(ptr->field_20, 0);
    if (*((long long *)&v6->padding_0[8]))
    {
        GraphicsUtils__Destroy(*((long long *)(*((long long *)&v6->padding_0[8]) + 296)), 0);
        ptr->field_20 = 0;
        sub_f7d8d0(v6, 0);
        if (ptr->field_18)
        {
            ptr->field_18->field_128 = 0;
            sub_f7d8d0();
            return;
        }
    }
    sub_f7db74();
}
```

## `ColorGradingComponent.ctor` — RVA `0xcd2178`

- Decompiled symbol: `ColorGradingComponent_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `128` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[40];
    long long field_28;
} struct_0;

extern long long g_1eee028;
extern long long g_1efa080;
extern char g_1fab5bd;

void ColorGradingComponent_ctor(struct_0 *ptr)
{
    unsigned long long v5;  // x30
    unsigned long long v6;  // x22
    unsigned long long v7;  // x21
    unsigned long long v8;  // x20
    unsigned long long v9;  // x19
    long long v10;  // x1
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
    if (!(g_1fab5bd & 1))
    {
        sub_f7d92c(&g_1eee028);
        sub_f7d92c(&g_1efa080);
        g_1fab5bd = 1;
    }
    v10 = sub_f7d9d4(g_1eee028, 0x100);
    ptr->field_28 = v10;
    sub_f7d8d0((struct struct_0 *)&ptr->field_28, v10);
}
```
