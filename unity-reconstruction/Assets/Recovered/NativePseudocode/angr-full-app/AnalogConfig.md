# Native pseudocode: AnalogConfig

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `AnalogConfig.ctor` — RVA `0xc56bb8`

- Decompiled symbol: `AnalogConfig_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `432` bytes
- Result: `pseudocode`
- Heuristic layout hint: `AnalogConfig_Recovered` matched 4 offsets against `AnalogConfig` metadata (confidence 1.00).

```c
typedef struct AnalogConfig_Recovered {
    char padding_0[16];
    uint128_t analogDeadZone;
    unsigned long long digitalLeaveThresh;
    unsigned int digitalToAnalogReleaseSpeed;
    char padding_2c[4];
    long long ramp;
} AnalogConfig_Recovered;

typedef struct struct_1 {
    char padding_0[24];
    unsigned int field_18;
    char padding_1c[4];
    char field_20[28];
    char field_2c;
    char padding_2d[15];
    char field_3c[28];
    char field_48;
    char padding_49[15];
    char field_58[28];
    char field_64;
} struct_1;

extern long long g_1eee230;
extern char g_1fab2a5;

long long AnalogConfig_ctor(struct_0 *p, unsigned long a1, unsigned long a2, unsigned long a3)
{
    struct_1 *ptr;  // x20
    long long v14;  // x21
    unsigned long v15;  // x0
    int v0;  // [bp-0xe0]
    char v1;  // [bp-0xd4]
    int v2;  // [bp-0xc0]
    unsigned long long flag2;  // [bp-0xb0]
    unsigned int flag;  // [bp-0xa8]
    int v5;  // [bp-0xa0]
    char v6;  // [bp-0x94]
    int v7;  // [bp-0x80]
    unsigned long long flag3;  // [bp-0x70]
    unsigned int choice;  // [bp-0x68]
    int v10;  // [bp-0x60]
    unsigned long flag4;  // [bp-0x40]
    int v12;  // [bp-0x38]

    if (!(g_1fab2a5 & 1))
    {
        sub_f7d92c("W,");
        sub_f7d92c(&g_1eee230);
        g_1fab2a5 = 1;
    }
    Object__ctor(p, 0);
    p->field_28 = 0x3f000000;
    p->field_10 = 83741363734449699997515502020106964173;
    p->field_20 = 4539628425434680525;
    ptr = sub_f7d9d4(g_1eee230, 3);
    flag4 = 0;
    *((unsigned long long *)&v12) = 0;
    *((unsigned int *)&(&v12)[16]) = 0;
    *((unsigned long long *)&(&v12)[8]) = 0;
    Keyframe__ctor(&flag4, 0);
    if (ptr)
    {
        memcpy(&v10, &flag4, 16);
        *((uint128_t *)&(&v10)[12]) = *((uint128_t *)(&v12 + 4));
        if (ptr->field_18)
        {
            *((uint128_t *)&ptr->field_20[12]) = *((uint128_t *)(&v10 + 12));
            *((uint128_t *)&ptr->field_20[0]) = *((uint128_t *)&v10);
            *((unsigned long long *)&v7) = 0;
            *((unsigned long long *)&(&v7)[8]) = 0;
            choice = 0;
            flag3 = 0;
            Keyframe__ctor(&v7, 0);
            memcpy(&v6, &v7 - 12, 16);
            v5 = v7;
            if (ptr->field_18 > 1)
            {
                *((uint128_t *)&ptr->padding_2d[11]) = *((uint128_t *)(&v5 + 12));
                *((uint128_t *)&ptr->field_2c) = *((uint128_t *)&v5);
                *((unsigned long long *)&v2) = 0;
                *((unsigned long long *)&(&v2)[8]) = 0;
                flag = 0;
                flag2 = 0;
                Keyframe__ctor(&v2, 0);
                memcpy(&v1, &v2 - 12, 16);
                v0 = v2;
                if (ptr->field_18 > 2)
                {
                    *((uint128_t *)&ptr->field_3c[24]) = *((uint128_t *)(&v0 + 12));
                    *((uint128_t *)&ptr->field_3c[12]) = *((uint128_t *)&v0);
                    v14 = sub_f7db70(g_1eee7c8);
                    AnimationCurve__ctor(v14, ptr, 0);
                    p->field_30 = v14;
                    v15 = sub_f7d8d0((struct AnalogConfig_Recovered *)&p->field_30, v14);
                    return sub_f7d8d0((struct AnalogConfig_Recovered *)&p->field_30, v14);
                }
            }
        }
        sub_f7db7c();
    }
    sub_f7db74();
}
```

## `AnalogConfig.GetAnalogVal` — RVA `0xc574f8`

- Decompiled symbol: `AnalogConfig_GetAnalogVal`
- Metadata signature: `public float GetAnalogVal(float rawVal) { }`
- Native interval: `188` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: Decompiler produced no C-like text

```c
// 0x10574f8: str d8, [sp, #-0x10]!
// 0x10574fc: str x30, [sp, #8]
// 0x1057500: ldr s1, [x0, #0x10]
// 0x1057504: fabs s2, s0
// 0x1057508: mov v8.16b, v0.16b
// 0x105750c: fmov s0, wzr
// 0x1057510: fcmp s2, s1
// 0x1057514: b.ls #0x10575a8
// 0x1057518: ldr s0, [x0, #0x14]
// 0x105751c: fcmp s2, s0
// 0x1057520: b.ge #0x1057564
// 0x1057524: ldrb w8, [x0, #0x2c]
// 0x1057528: fsub s2, s2, s1
// 0x105752c: fsub s0, s0, s1
// 0x1057530: fdiv s0, s2, s0
// 0x1057534: cbz w8, #0x1057578
// 0x1057538: ldr x8, [x0, #0x30]
// 0x105753c: cbz x8, #0x1057578
// 0x1057540: mov x0, x8
// 0x1057544: mov x1, xzr
// 0x1057548: bl #0x1b6cda8
// 0x105754c: fcmp s0, #0.0
// 0x1057550: fmov s1, wzr
// 0x1057554: b.mi #0x105759c
// 0x1057558: fmov s1, #1.00000000
// 0x105755c: fmin s1, s0, s1
// 0x1057560: b #0x105759c
// 0x1057564: fcmp s8, #0.0
// 0x1057568: fmov s0, #-1.00000000
// 0x105756c: fmov s1, #1.00000000
// 0x1057570: fcsel s0, s1, s0, ge
// 0x1057574: b #0x10575a8
// 0x1057578: ldr s1, [x0, #0x18]
// 0x105757c: fmov s2, #1.00000000
// 0x1057580: fmin s3, s0, s2
// 0x1057584: fcmp s0, #0.0
// 0x1057588: fmov s0, wzr
// 0x105758c: fcsel s0, s3, s0, pl
// 0x1057590: fsub s2, s2, s1
// 0x1057594: fmul s0, s0, s2
// 0x1057598: fadd s1, s1, s0
// 0x105759c: fneg s0, s1
// 0x10575a0: fcmp s8, #0.0
// 0x10575a4: fcsel s0, s0, s1, lt
// 0x10575a8: ldr x30, [sp, #8]
// 0x10575ac: ldr d8, [sp], #0x10
// 0x10575b0: ret
```

## `AnalogConfig.GetSignedDigitalVal` — RVA `0xc5acc4`

- Decompiled symbol: `AnalogConfig_GetSignedDigitalVal`
- Metadata signature: `public int GetSignedDigitalVal(float rawVal, int prevDigiVal) { }`
- Native interval: `76` bytes
- Result: `pseudocode`

```c
unsigned long long AnalogConfig_GetSignedDigitalVal(unsigned long a0, unsigned int flag)
{
    unsigned int v0;  // s0
    unsigned long v1;  // 4125
    unsigned long long v10;  // x8
    unsigned int v11;  // s1
    unsigned long v12;  // 4133
    unsigned long long v2;  // x8
    unsigned long long v3;  // x9
    unsigned long v4;  // 4117
    unsigned long long v5;  // x8
    unsigned int v6;  // s1
    unsigned long v7;  // 4136
    unsigned long long v8;  // x8
    unsigned long long v9;  // x9

    v1 = arm64g_calculate_condition(160, (((((unsigned long long)(char)(CmpF(v0, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v0, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v0, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v0, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v0, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v0, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if (!((char)v1))
    {
        v2 = 28;
        v3 = 32;
        v4 = arm64g_calculate_condition(1, (unsigned long long)flag, 1, 0);
        if ((char)v4)
            v5 = v3;
        else
            v5 = v2;
        v6 = -(*((int *)(a0 + v5)));
        v7 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v6, v0)) >> 5 & 3 | (unsigned long long)(CmpF(v6, v0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v6, v0)) >> 5 & 3 | (unsigned long long)(CmpF(v6, v0) & 1)) & ((unsigned long long)(char)(CmpF(v6, v0)) >> 5 & 3 | (unsigned long long)(CmpF(v6, v0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if (!((char)v7))
            return 4294967295;
        return 0;
    }
    else
    {
        v8 = 28;
        v9 = 32;
        if (flag == 1)
            v10 = v9;
        else
            v10 = v8;
        v11 = *((int *)(a0 + v10));
        v12 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v11, v0)) >> 5 & 3 | (unsigned long long)(CmpF(v11, v0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v11, v0)) >> 5 & 3 | (unsigned long long)(CmpF(v11, v0) & 1)) & ((unsigned long long)(char)(CmpF(v11, v0)) >> 5 & 3 | (unsigned long long)(CmpF(v11, v0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if (!((char)v12))
            return 1;
        return 0;
    }
}
```

## `AnalogConfig.GetDigitalVal` — RVA `0xc5ad10`

- Decompiled symbol: `AnalogConfig_GetDigitalVal`
- Metadata signature: `public bool GetDigitalVal(float rawVal, bool prevDigiVal) { }`
- Native interval: `32` bytes
- Result: `pseudocode`

```c
unsigned int AnalogConfig_GetDigitalVal(unsigned long a0, unsigned int a1)
{
    unsigned long long v0;  // x8
    unsigned long long v1;  // x9
    unsigned long v2;  // 4114
    unsigned long long v3;  // x8
    unsigned int v4;  // s1
    unsigned int v5;  // s0
    unsigned long v6;  // 4133

    v0 = 28;
    v1 = 32;
    v2 = arm64g_calculate_condition(25, (unsigned long long)(a1 & 1), 0, 0);
    if ((char)v2)
        v3 = v1;
    else
        v3 = v0;
    v4 = *((int *)(a0 + v3));
    v6 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v4, v5)) >> 5 & 3 | (unsigned long long)(CmpF(v4, v5) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v4, v5)) >> 5 & 3 | (unsigned long long)(CmpF(v4, v5) & 1)) & ((unsigned long long)(char)(CmpF(v4, v5)) >> 5 & 3 | (unsigned long long)(CmpF(v4, v5) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if (!((char)v6))
        return 1;
    return 0;
}
```

## `AnalogConfig.AnimateDigitalToAnalog` — RVA `0xc5ad30`

- Decompiled symbol: `AnalogConfig_AnimateDigitalToAnalog`
- Metadata signature: `public float AnimateDigitalToAnalog(float curVal, float targetVal, bool pressed) { }`
- Native interval: `156` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: Decompiler produced no C-like text

```c
// 0x105ad30: str d10, [sp, #-0x20]!
// 0x105ad34: stp d9, d8, [sp, #8]
// 0x105ad38: str x30, [sp, #0x18]
// 0x105ad3c: tst w1, #1
// 0x105ad40: mov w8, #0x28
// 0x105ad44: mov w9, #0x24
// 0x105ad48: csel x8, x9, x8, ne
// 0x105ad4c: ldr s10, [x0, x8]
// 0x105ad50: mov v8.16b, v1.16b
// 0x105ad54: mov v9.16b, v0.16b
// 0x105ad58: bl #0x104e208
// 0x105ad5c: adrp x8, #0x832000
// 0x105ad60: ldr s1, [x8, #0x534]
// 0x105ad64: fabd s2, s8, s9
// 0x105ad68: fcmp s2, s1
// 0x105ad6c: b.ls #0x105adb8
// 0x105ad70: adrp x8, #0x832000
// 0x105ad74: ldr s2, [x8, #0x4f4]
// 0x105ad78: fmul s2, s10, s2
// 0x105ad7c: fcmp s2, s1
// 0x105ad80: b.mi #0x105adb8
// 0x105ad84: fdiv s3, s0, s2
// 0x105ad88: fcmp s2, s0
// 0x105ad8c: fmov s0, #1.00000000
// 0x105ad90: fmov s2, #0.75000000
// 0x105ad94: fcsel s3, s3, s0, hi
// 0x105ad98: fmin s2, s3, s2
// 0x105ad9c: fmin s0, s2, s0
// 0x105ada0: fcmp s2, #0.0
// 0x105ada4: fmov s2, wzr
// 0x105ada8: fsub s1, s8, s9
// 0x105adac: fcsel s0, s0, s2, pl
// 0x105adb0: fmul s0, s1, s0
// 0x105adb4: fadd s8, s0, s9
// 0x105adb8: mov v0.16b, v8.16b
// 0x105adbc: ldr x30, [sp, #0x18]
// 0x105adc0: ldp d9, d8, [sp, #8]
// 0x105adc4: ldr d10, [sp], #0x20
// 0x105adc8: ret
```
