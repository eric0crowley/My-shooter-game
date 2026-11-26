# Native pseudocode: TouchSteeringWheel

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `TouchSteeringWheel.ctor` — RVA `0xc569c0`

- Decompiled symbol: `TouchSteeringWheel_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `504` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[136];
    char field_88;
    char padding_89[7];
    unsigned long long field_90;
    unsigned int field_98;
    unsigned short field_9c;
    char padding_9e[2];
    unsigned short field_a0;
    char padding_a2[22];
    unsigned int field_b8;
} struct_0;

extern long long g_1eee758;
extern long long g_1f0ab18;
extern char g_1fab291;

long long TouchSteeringWheel_ctor(struct_0 *ptr)
{
    unsigned long long v7;  // x30
    unsigned long long v8;  // x24
    unsigned long long v9;  // x23
    unsigned long long v10;  // x22
    unsigned long long v11;  // x21
    unsigned long long v12;  // x20
    unsigned long long v13;  // x19
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
    if (!(g_1fab291 & 1))
    {
        sub_f7d92c(&g_1eee758);
        sub_f7d92c("g.");
        sub_f7d92c("y7");
        sub_f7d92c(&g_1f0ab18);
        g_1fab291 = 1;
    }
    *((void*)&ptr[2].padding_0[4]) = 81481676178022385856365452945695493325;
    *((unsigned int *)&ptr[2].padding_0[24]) = 0x40000000;
    DynamicTouchControl__ctor(ptr); /* do not return */
}
```

## `TouchSteeringWheel.GetValue` — RVA `0xc56e90`

- Decompiled symbol: `TouchSteeringWheel_GetValue`
- Metadata signature: `public float GetValue() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long TouchSteeringWheel_GetValue(unsigned long a0)
{
    return a0;
}
```

## `TouchSteeringWheel.GetValueDelta` — RVA `0xc56e98`

- Decompiled symbol: `TouchSteeringWheel_GetValueDelta`
- Metadata signature: `public float GetValueDelta() { }`
- Native interval: `16` bytes
- Result: `pseudocode`

```c
long long TouchSteeringWheel_GetValueDelta(unsigned long a0)
{
    return a0;
}
```

## `TouchSteeringWheel.OnInitControl` — RVA `0xc56ea8`

- Decompiled symbol: `TouchSteeringWheel_OnInitControl`
- Metadata signature: `protected override void OnInitControl() { }`
- Native interval: `40` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[664];
    unsigned long long field_298;
} struct_0;

void TouchSteeringWheel_OnInitControl(struct_0 **a0)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    DynamicTouchControl__OnInitControl(a0);
    goto *(a0)->field_298;
}
```

## `TouchSteeringWheel.ResetControl` — RVA `0xc56ed0`

- Decompiled symbol: `TouchSteeringWheel_ResetControl`
- Metadata signature: `public override void ResetControl() { }`
- Native interval: `200` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[136];
    char field_88;
    char padding_89[143];
    char field_118;
    char field_119;
    char field_11a;
    char padding_11b[5];
    unsigned int field_120;
    char padding_124[4];
    unsigned int field_128;
    unsigned int field_12c;
    unsigned int field_130;
} struct_0;

void TouchSteeringWheel_ResetControl(struct_0 *a0)
{
    unsigned long long v3;  // x30
    unsigned long long v4;  // x20
    unsigned long long v5;  // x19
    struct_0 *v6;  // x0
    unsigned long v7;  // x1
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x10]
    unsigned long long v2;  // [bp-0x8]

    v0 = v3;
    v1 = v4;
    v2 = v5;
    DynamicTouchControl__ResetControl(a0);
    v6 = a0;
    v7 = *((long long *)(*((long long *)&a0->padding_0[0]) + 688));
    (*((long long *)(*((long long *)&a0->padding_0[0]) + 680)))();
}
```

## `TouchSteeringWheel.OnUpdateControl` — RVA `0xc56f98`

- Decompiled symbol: `TouchSteeringWheel_OnUpdateControl`
- Metadata signature: `protected override void OnUpdateControl() { }`
- Native interval: `992` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: Decompiler produced no C-like text

```c
// 0x1056f98: str d10, [sp, #-0x30]!
// 0x1056f9c: stp d9, d8, [sp, #8]
// 0x1056fa0: str x30, [sp, #0x18]
// 0x1056fa4: stp x20, x19, [sp, #0x20]
// 0x1056fa8: adrp x20, #0x1fab000
// 0x1056fac: ldrb w8, [x20, #0x292]
// 0x1056fb0: mov x19, x0
// 0x1056fb4: tbnz w8, #0, #0x1056fcc
// 0x1056fb8: adrp x0, #0x1e8c000
// 0x1056fbc: ldr x0, [x0, #0x490]
// 0x1056fc0: bl #0xf7d92c
// 0x1056fc4: mov w8, #1
// 0x1056fc8: strb w8, [x20, #0x292]
// 0x1056fcc: mov x0, x19
// 0x1056fd0: mov x1, xzr
// 0x1056fd4: bl #0x10482a8
// 0x1056fd8: ldr s0, [x19, #0x1dc]
// 0x1056fdc: ldr x0, [x19, #0xe0]
// 0x1056fe0: str s0, [x19, #0x1e0]
// 0x1056fe4: cbz x0, #0x1057374
// 0x1056fe8: mov x1, xzr
// 0x1056fec: bl #0x1061bf0
// 0x1056ff0: tbz w0, #0, #0x10570a4
// 0x1056ff4: ldr s0, [x19, #0x1d8]
// 0x1056ff8: ldr w8, [x19, #0x174]
// 0x1056ffc: str s0, [x19, #0x1ec]
// 0x1057000: cbz w8, #0x105704c
// 0x1057004: ldr x8, [x19, #0xe0]
// 0x1057008: cbz x8, #0x1057374
// 0x105700c: ldp s8, s9, [x8, #0x5c]
// 0x1057010: mov x0, x19
// 0x1057014: mov x1, xzr
// 0x1057018: bl #0x1047fa0
// 0x105701c: mov v2.16b, v0.16b
// 0x1057020: mov v3.16b, v1.16b
// 0x1057024: mov x0, x19
// 0x1057028: mov v0.16b, v8.16b
// 0x105702c: mov v1.16b, v9.16b
// 0x1057030: bl #0x10510d0
// 0x1057034: add x8, x19, #0x1f0
// 0x1057038: str s0, [x19, #0x1e4]
// 0x105703c: str s1, [x19, #0x1e8]
// 0x1057040: str xzr, [x19, #0x1f0]
// 0x1057044: stur xzr, [x8, #5]
// 0x1057048: b #0x10570a4
// 0x105704c: ldrb w8, [x19, #0x18c]
// 0x1057050: cbz w8, #0x105706c
// 0x1057054: ldr x8, [x19, #0xd0]
// 0x1057058: cbz x8, #0x1057374
// 0x105705c: ldur d0, [x8, #0x44]
// 0x1057060: add x8, x19, #0x1e4
// 0x1057064: str d0, [x8]
// 0x1057068: b #0x10570a4
// 0x105706c: ldr x8, [x19, #0xe0]
// 0x1057070: cbz x8, #0x1057374
// 0x1057074: ldp s8, s9, [x8, #0x5c]
// 0x1057078: mov x0, x19
// 0x105707c: mov x1, xzr
// 0x1057080: bl #0x1047fa0
// 0x1057084: mov v2.16b, v0.16b
// 0x1057088: mov v3.16b, v1.16b
// 0x105708c: mov x0, x19
// 0x1057090: mov v0.16b, v8.16b
// 0x1057094: mov v1.16b, v9.16b
// 0x1057098: bl #0x10510d0
// 0x105709c: str s0, [x19, #0x1e4]
// 0x10570a0: str s1, [x19, #0x1e8]
// 0x10570a4: ldr x8, [x19, #0xe0]
// 0x10570a8: cbz x8, #0x1057374
// 0x10570ac: ldrb w9, [x8, #0x1c]
// 0x10570b0: cbz w9, #0x1057114
// 0x10570b4: ldr w9, [x19, #0x174]
// 0x10570b8: cbz w9, #0x105717c
// 0x10570bc: ldp s8, s9, [x8, #0x44]
// 0x10570c0: mov x0, x19
// 0x10570c4: mov x1, xzr
// 0x10570c8: bl #0x1047fa0
// 0x10570cc: mov v2.16b, v0.16b
// 0x10570d0: mov v3.16b, v1.16b
// 0x10570d4: mov x0, x19
// 0x10570d8: mov v0.16b, v8.16b
// 0x10570dc: mov v1.16b, v9.16b
// 0x10570e0: bl #0x10510d0
// 0x10570e4: ldr s4, [x19, #0x188]
// 0x10570e8: fmul s2, s0, s0
// 0x10570ec: fmul s3, s1, s1
// 0x10570f0: fadd s2, s2, s3
// 0x10570f4: fmov s3, wzr
// 0x10570f8: fadd s2, s2, s3
// 0x10570fc: fmul s3, s4, s4
// 0x1057100: fcmp s2, s3
// 0x1057104: b.pl #0x10571d0
// 0x1057108: ldr s0, [x19, #0x1f4]
// 0x105710c: strb wzr, [x19, #0x1fc]
// 0x1057110: b #0x10571fc
// 0x1057114: ldrb w8, [x19, #0x178]
// 0x1057118: fmov s8, wzr
// 0x105711c: fmov s9, wzr
// 0x1057120: cbz w8, #0x1057128
// 0x1057124: ldr s9, [x19, #0x180]
// 0x1057128: ldr s10, [x19, #0x1d8]
// 0x105712c: bl #0x104e208
// 0x1057130: fcmp s9, s0
// 0x1057134: b.ls #0x10572e0
// 0x1057138: adrp x8, #0x832000
// 0x105713c: ldr s2, [x8, #0x534]
// 0x1057140: fabd s1, s8, s10
// 0x1057144: fcmp s1, s2
// 0x1057148: b.ls #0x10572e0
// 0x105714c: fcmp s9, s2
// 0x1057150: b.mi #0x10572e0
// 0x1057154: fsub s2, s8, s10
// 0x1057158: fdiv s0, s0, s9
// 0x105715c: fneg s3, s0
// 0x1057160: fcmp s2, #0.0
// 0x1057164: fcsel s2, s0, s3, ge
// 0x1057168: fcmp s1, s0
// 0x105716c: fadd s0, s10, s2
// 0x1057170: fmov s1, wzr
// 0x1057174: fcsel s8, s0, s1, hi
// 0x1057178: b #0x10572e0
// 0x105717c: ldrb w9, [x19, #0x18c]
// 0x1057180: cbz w9, #0x1057340
// 0x1057184: ldr x8, [x19, #0xd0]
// 0x1057188: cbz x8, #0x1057374
// 0x105718c: adrp x9, #0x1e8c000
// 0x1057190: ldr x9, [x9, #0x490]
// 0x1057194: ldr s8, [x8, #0x44]
// 0x1057198: ldr s9, [x19, #0x1e4]
// 0x105719c: ldr s10, [x19, #0x190]
// 0x10571a0: ldr x0, [x9]
// 0x10571a4: ldr w8, [x0, #0xe0]
// 0x10571a8: cbnz w8, #0x10571b0
// 0x10571ac: bl #0xf7da5c
// 0x10571b0: mov x0, xzr
// 0x10571b4: bl #0x1038b44
// 0x10571b8: fmul s0, s10, s0
// 0x10571bc: fmov s2, #0.50000000
// 0x10571c0: fsub s1, s8, s9
// 0x10571c4: fmul s0, s0, s2
// 0x10571c8: fdiv s0, s1, s0
// 0x10571cc: b #0x1057278
// 0x10571d0: ldr s2, [x19, #0x1f4]
// 0x10571d4: mov x0, x19
// 0x10571d8: bl #0x1057378
// 0x10571dc: ldrb w8, [x19, #0x1fc]
// 0x10571e0: str s0, [x19, #0x1f4]
// 0x10571e4: cbnz w8, #0x10571fc
// 0x10571e8: ldr s1, [x19, #0x1d8]
// 0x10571ec: mov w8, #1
// 0x10571f0: str s0, [x19, #0x1f0]
// 0x10571f4: strb w8, [x19, #0x1fc]
// 0x10571f8: str s1, [x19, #0x1ec]
// 0x10571fc: ldr s1, [x19, #0x1f0]
// 0x1057200: ldr s2, [x19, #0x1f8]
// 0x1057204: mov w8, #0x43b40000
// 0x1057208: fmov s3, w8
// 0x105720c: mov w8, #-0x3c4c0000
// 0x1057210: fadd s1, s1, s2
// 0x1057214: fsub s0, s0, s1
// 0x1057218: fdiv s1, s0, s3
// 0x105721c: fmov s5, w8
// 0x1057220: frintm s1, s1
// 0x1057224: fmul s1, s1, s5
// 0x1057228: fadd s0, s0, s1
// 0x105722c: ldr s1, [x19, #0x184]
// 0x1057230: fmov s4, wzr
// 0x1057234: mov w8, #0x43340000
// 0x1057238: fcmp s0, #0.0
// 0x105723c: fmin s0, s0, s3
// 0x1057240: fcsel s0, s0, s4, pl
// 0x1057244: fmov s4, w8
// 0x1057248: fcmp s0, s4
// 0x105724c: fsub s4, s5, s1
// 0x1057250: fadd s5, s0, s5
// 0x1057254: fcsel s0, s5, s0, gt
// 0x1057258: fadd s3, s1, s3
// 0x105725c: fadd s0, s2, s0
// 0x1057260: fcmp s0, s3
// 0x1057264: fcsel s2, s3, s0, gt
// 0x1057268: fcmp s0, s4
// 0x105726c: fcsel s0, s2, s4, pl
// 0x1057270: str s0, [x19, #0x1f8]
// 0x1057274: fdiv s0, s0, s1
// 0x1057278: ldrb w8, [x19, #0x178]
// 0x105727c: ldr s1, [x19, #0x1ec]
// 0x1057280: cbz w8, #0x105728c
// 0x1057284: ldr s9, [x19, #0x17c]
// 0x1057288: b #0x1057290
// 0x105728c: fmov s9, wzr
// 0x1057290: ldr s10, [x19, #0x1d8]
// 0x1057294: fadd s8, s0, s1
// 0x1057298: bl #0x104e208
// 0x105729c: fcmp s9, s0
// 0x10572a0: b.ls #0x10572e0
// 0x10572a4: adrp x8, #0x832000
// 0x10572a8: ldr s2, [x8, #0x534]
// 0x10572ac: fabd s1, s8, s10
// 0x10572b0: fcmp s1, s2
// 0x10572b4: b.ls #0x10572e0
// 0x10572b8: fcmp s9, s2
// 0x10572bc: b.mi #0x10572e0
// 0x10572c0: fsub s2, s8, s10
// 0x10572c4: fdiv s0, s0, s9
// 0x10572c8: fneg s3, s0
// 0x10572cc: fcmp s2, #0.0
// 0x10572d0: fcsel s2, s0, s3, ge
// 0x10572d4: fadd s2, s10, s2
// 0x10572d8: fcmp s1, s0
// 0x10572dc: fcsel s8, s2, s8, hi
// 0x10572e0: ldr x0, [x19, #0x198]
// 0x10572e4: fmov s0, #1.00000000
// 0x10572e8: fmov s1, #-1.00000000
// 0x10572ec: fmin s0, s8, s0
// 0x10572f0: fcmp s8, s1
// 0x10572f4: fcsel s0, s0, s1, pl
// 0x10572f8: str s0, [x19, #0x1d8]
// 0x10572fc: cbz x0, #0x1057374
// 0x1057300: bl #0x10574f8
// 0x1057304: ldr w8, [x19, #0x50]
// 0x1057308: str s0, [x19, #0x1dc]
// 0x105730c: tst w8, #0xffffffbf
// 0x1057310: b.eq #0x1057328
// 0x1057314: ldp x20, x19, [sp, #0x20]
// 0x1057318: ldr x30, [sp, #0x18]
// 0x105731c: ldp d9, d8, [sp, #8]
// 0x1057320: ldr d10, [sp], #0x30
// 0x1057324: ret
// 0x1057328: mov x0, x19
// 0x105732c: ldp x20, x19, [sp, #0x20]
// 0x1057330: ldr x30, [sp, #0x18]
// 0x1057334: ldp d9, d8, [sp, #8]
// 0x1057338: ldr d10, [sp], #0x30
// 0x105733c: b #0x10575b4
// 0x1057340: ldp s8, s9, [x8, #0x44]
// 0x1057344: mov x0, x19
// 0x1057348: mov x1, xzr
// 0x105734c: bl #0x1047fa0
// 0x1057350: mov v2.16b, v0.16b
// 0x1057354: mov v3.16b, v1.16b
// 0x1057358: mov x0, x19
// 0x105735c: mov v0.16b, v8.16b
// 0x1057360: mov v1.16b, v9.16b
// 0x1057364: bl #0x10510d0
// 0x1057368: ldr s1, [x19, #0x1e4]
// 0x105736c: fsub s0, s0, s1
// 0x1057370: b #0x1057278
// 0x1057374: bl #0xf7db74
```

## `TouchSteeringWheel.GetWheelAngle` — RVA `0xc57378`

- Decompiled symbol: `TouchSteeringWheel_GetWheelAngle`
- Metadata signature: `private float GetWheelAngle(Vector2 np, float fallbackAngle) { }`
- Native interval: `224` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[392];
    unsigned int field_188;
} struct_0;

extern long long g_1ef22b8;
extern char g_1fab1e0;
extern char g_1fab243;

void TouchSteeringWheel_GetWheelAngle(struct_0 *ptr)
{
    unsigned int v0;  // s0
    unsigned int v1;  // s1
    unsigned int v2;  // s10
    unsigned int v3;  // s0
    unsigned long v4;  // 4212
    unsigned int v5;  // s1
    unsigned long v6;  // 4140

    v2 = v0 * v0 + v1 * v1;
    v3 = ptr->field_188 * ptr->field_188;
    v4 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(v2, v3)) >> 5 & 3 | (unsigned long long)(CmpF(v0 * v0 + v1 * v1, v3) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v0 * v0 + v1 * v1, v3)) >> 5 & 3 | (unsigned long long)(CmpF(v0 * v0 + v1 * v1, v3) & 1)) & ((unsigned long long)(char)(CmpF(v0 * v0 + v1 * v1, v3)) >> 5 & 3 | (unsigned long long)(CmpF(v0 * v0 + v1 * v1, v3) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if ((char)v4)
        return;
    if (!g_1fab243)
    {
        sub_f7d92c("_F");
        g_1fab243 = 1;
    }
    if (!g_1ef07e8->field_e0)
        sub_f7da5c(g_1ef07e8);
    v5 = [D] unsupported_Iop_SqrtF32();
    v6 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v5, 925353388)) >> 5 & 3 | (unsigned long long)(CmpF(v5, 925353388) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v5, 925353388)) >> 5 & 3 | (unsigned long long)(CmpF(v5, 925353388) & 1)) & ((unsigned long long)(char)(CmpF(v5, 925353388)) >> 5 & 3 | (unsigned long long)(CmpF(v5, 925353388) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if ((char)v6 && !g_1fab1e0)
    {
        sub_f7d92c(&g_1ef22b8);
        g_1fab1e0 = 1;
    }
    atan2f();
    return;
}
```

## `TouchSteeringWheel.SyncRigState` — RVA `0xc575b4`

- Decompiled symbol: `TouchSteeringWheel_SyncRigState`
- Metadata signature: `private void SyncRigState() { }`
- Native interval: `292` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[224];
    struct struct_0 *field_e0;
} struct_1;

typedef struct struct_0 {
    char padding_0[28];
    unsigned int field_1c;
} struct_0;

typedef struct struct_3 {
    char padding_0[24];
    unsigned int field_18;
} struct_3;

typedef struct struct_0 {
    char padding_0[28];
    char field_1c;
} struct_0;

long long TouchSteeringWheel_SyncRigState(struct_1 *ptr)
{
    unsigned long v0;  // x0
    unsigned long v1;  // x0
    struct_3 *v9;  // x0
    unsigned int v2;  // s0
    unsigned int v3;  // s1
    unsigned long v4;  // 4136
    unsigned long v5;  // 4125
    unsigned long v6;  // x0
    unsigned long v7;  // x2
    unsigned long long v8;  // x1

    if (((char)DynamicTouchControl__Pressed(ptr) & 1) || ptr[1].padding_0[172])
    {
        v0 = *((long long *)&ptr[1].padding_0[192]);
        if (!v0)
            sub_f7db74(v0);
        AxisBinding__SyncFloat(v0, 1, *((long long *)&ptr->padding_0[88]));
    }
    v1 = DynamicTouchControl__Pressed(ptr);
    if (!((char)v1 & 1))
        return v1;
    v0 = DynamicTouchControl__Pressed(ptr);
    if (*((long long *)&ptr[1].padding_0[184]) && (v0 = (unsigned long)DigitalBinding__Sync(*((long long *)&ptr[1].padding_0[184]), (unsigned int)v0 & 1, *((long long *)&ptr->padding_0[88]), 0), *((long long *)&ptr[1].padding_0[176])))
    {
        v2 = *((int *)(*((long long *)&ptr[1].padding_0[176]) + 28));
        v3 = *((int *)&ptr[2].padding_0[12]);
        v4 = arm64g_calculate_condition(144, (((((unsigned long long)(char)(CmpF(v3, -(v2))) >> 5 & 3 | (unsigned long long)(CmpF(v3, -(v2)) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v3, -(v2))) >> 5 & 3 | (unsigned long long)(CmpF(v3, -(v2)) & 1)) & ((unsigned long long)(char)(CmpF(v3, -(v2))) >> 5 & 3 | (unsigned long long)(CmpF(v3, -(v2)) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if (!((char)v4))
        {
            v5 = arm64g_calculate_condition(176, (((((unsigned long long)(char)(CmpF(v3, v2)) >> 5 & 3 | (unsigned long long)(CmpF(v3, v2) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v3, v2)) >> 5 & 3 | (unsigned long long)(CmpF(v3, v2) & 1)) & ((unsigned long long)(char)(CmpF(v3, v2)) >> 5 & 3 | (unsigned long long)(CmpF(v3, v2) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
            if ((char)v5)
                goto LABEL_105766c;
            v0 = *((long long *)&ptr[1].padding_0[200]);
            if (v0)
                goto LABEL_105765c;
        }
        else
        {
            v0 = *((long long *)&ptr[1].padding_0[208]);
            if (v0)
            {
LABEL_105765c:
                DigitalBinding__Sync(v0, 1, *((long long *)&ptr->padding_0[88]), 0);
LABEL_105766c:
                v6 = DynamicTouchControl__IsTouchPressureSensitive(ptr);
                if (((char)v6 & 1))
                {
                    v0 = DynamicTouchControl__GetTouchPressure(ptr);
                    if (ptr[1].field_e0)
                    {
                        v8 = 1;
                        v7 = *((long long *)&ptr->padding_0[88]);
                        v9 = AxisBinding__SyncFloat(ptr[1].field_e0, 1, *((long long *)&ptr->padding_0[88]));
                        return AxisBinding__SyncFloat(ptr[1].field_e0, 1, *((long long *)&ptr->padding_0[88]));
                    }
                }
                else if (ptr[1].padding_0[216])
                {
                    v0 = ptr[1].field_e0;
                    if (v0)
                    {
                        v7 = *((long long *)&ptr->padding_0[88]);
                        v8 = 0;
                        v9 = AxisBinding__SyncFloat(v0, 0, v7);
                        return AxisBinding__SyncFloat(v0, 0, v7);
                    }
                }
                else
                {
                    return v6;
                }
            }
        }
    }
    sub_f7db74(v0);
}
```

## `TouchSteeringWheel.OnIsBoundToAxis` — RVA `0xc576d8`

- Decompiled symbol: `TouchSteeringWheel_OnIsBoundToAxis`
- Metadata signature: `protected override bool OnIsBoundToAxis(string axisName, InputRig rig) { }`
- Native interval: `176` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[424];
    long long field_1a8;
} struct_0;

long long TouchSteeringWheel_OnIsBoundToAxis(struct_0 *a0, unsigned long a1, unsigned long a2)
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
    if (a0->field_1a8)
        InputBindingBase__IsBoundToAxis(a0->field_1a8); /* do not return */
    sub_f7db74(0);
}
```

## `TouchSteeringWheel.OnIsBoundToKey` — RVA `0xc57788`

- Decompiled symbol: `TouchSteeringWheel_OnIsBoundToKey`
- Metadata signature: `protected override bool OnIsBoundToKey(KeyCode key, InputRig rig) { }`
- Native interval: `176` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[424];
    long long field_1a8;
} struct_0;

long long TouchSteeringWheel_OnIsBoundToKey(struct_0 *a0, unsigned long a1, unsigned long a2, unsigned long a3)
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
    if (a0->field_1a8)
        InputBindingBase__IsBoundToKey(a0->field_1a8); /* do not return */
    sub_f7db74(0);
}
```

## `TouchSteeringWheel.OnGetSubBindingDescriptions` — RVA `0xc57838`

- Decompiled symbol: `TouchSteeringWheel_OnGetSubBindingDescriptions`
- Metadata signature: `protected override void OnGetSubBindingDescriptions(BindingDescriptionList descList, Object undoObject, string parentMenuPath) { }`
- Native interval: `320` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[416];
    long long field_1a0;
} struct_0;

extern long long g_1f08568;
extern long long g_1f0d040;
extern char g_1fab293;

long long TouchSteeringWheel_OnGetSubBindingDescriptions(struct_0 *a0, long long a1, unsigned long a2, long long a3)
{
    unsigned long long v8;  // x30
    unsigned long long v9;  // x25
    unsigned long long v10;  // x24
    unsigned long long v11;  // x23
    unsigned long long v12;  // x22
    unsigned long long v13;  // x21
    unsigned long long v14;  // x20
    unsigned long long v15;  // x19
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
    if (!(g_1fab293 & 1))
    {
        sub_f7d92c("U#");
        sub_f7d92c(&g_1f0d040);
        sub_f7d92c("W#");
        sub_f7d92c("+#");
        sub_f7d92c(&g_1f08568);
        g_1fab293 = 1;
    }
    if (a1)
        BindingDescriptionList__Add(a1, a0->field_1a0, g_1f0d040, a3, a0, 0); /* do not return */
    sub_f7db74();
}
```
