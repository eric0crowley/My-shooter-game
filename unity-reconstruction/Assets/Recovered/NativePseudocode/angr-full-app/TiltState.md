# Native pseudocode: TiltState

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `TiltState.ctor` — RVA `0xc616ec`

- Decompiled symbol: `TiltState_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `52` bytes
- Result: `pseudocode`
- Heuristic layout hint: `TiltState_Recovered` matched 3 offsets against `TiltState` metadata (confidence 1.00).

```c
typedef struct TiltState_Recovered {
    char padding_0[16];
    unsigned long long analogRange;
    char padding_18[24];
    unsigned long long anglesNeutral;
    char padding_38[32];
    char calibrated;
} TiltState_Recovered;

long long TiltState_ctor(struct_0 *ptr)
{
    unsigned long long v0;  // x0

    Object__ctor();
    ptr->field_10 = 0x41c8000041c80000;
    ptr->field_58 = 0;
    ptr->field_30 = 0x4307000000000000;
    v0 = TiltState__Reset(ptr);
    return TiltState__Reset(ptr);
}
```

## `TiltState.Reset` — RVA `0xc61720`

- Decompiled symbol: `TiltState_Reset`
- Metadata signature: `public void Reset() { }`
- Native interval: `96` bytes
- Result: `pseudocode`
- Heuristic layout hint: `TiltState_Recovered` matched 3 offsets against `TiltState` metadata (confidence 1.00).

```c
typedef struct TiltState_Recovered {
    char padding_0[72];
    unsigned long long anglesCur;
    unsigned long long analogCur;
    char calibrated;
} TiltState_Recovered;

typedef struct struct_2 {
    unsigned long long field_0;
} struct_2;

typedef struct struct_1 {
    char padding_0[184];
    struct struct_2 *field_b8;
} struct_1;

extern struct_1 *g_1ef22b8;
extern char g_1fab1e0;

struct_0 * TiltState_Reset(struct_0 *ptr)
{
    struct_0 *v0;  // x0
    struct_0 *v1;  // x0

    ptr->field_58 = 0;
    v0 = ptr;
    if (!g_1fab1e0)
    {
        v1 = sub_f7d92c(&g_1ef22b8);
        g_1fab1e0 = 1;
        v0 = v1;
    }
    ptr->field_50 = g_1ef22b8->field_b8->field_0;
    ptr->field_48 = g_1ef22b8->field_b8->field_0;
    return v0;
}
```

## `TiltState.InternalApplyVector` — RVA `0xc61780`

- Decompiled symbol: `TiltState_InternalApplyVector`
- Metadata signature: `public void InternalApplyVector(Vector3 v) { }`
- Native interval: `32` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[36];
    unsigned long long field_24;
    unsigned int field_2c;
} struct_0;

struct_0 * TiltState_InternalApplyVector(struct_0 *ptr)
{
    unsigned int v0;  // s4
    unsigned int v2;  // s2

    v0 = *((int *)((char *)&ptr->field_24 + 4));
    *((long long *)&(&ptr->padding_0)[1]) = [D] unsupported_Iop_ZeroHI64ofV128();
    *((unsigned int *)((char *)&ptr->field_24 + 4)) = v2 + v0;
    return ptr;
}
```

## `TiltState.IsAvailable` — RVA `0xc617a0`

- Decompiled symbol: `TiltState_IsAvailable`
- Metadata signature: `public static bool IsAvailable() { }`
- Native interval: `152` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    unsigned int field_0;
    unsigned int field_4;
    unsigned int field_8;
} struct_1;

typedef struct struct_0 {
    char padding_0[184];
    struct struct_1 *field_b8;
} struct_0;

extern struct_0 *g_1ef22e8;
extern char g_1fab2c9;

unsigned int TiltState_IsAvailable(void)
{
    unsigned long long v1;  // d10
    unsigned int ptr[3];  // x8
    unsigned int v3;  // s2
    unsigned int v4;  // s2
    unsigned int v5;  // s0
    unsigned int v6;  // s0
    unsigned int v7;  // s1
    unsigned int v8;  // s1
    unsigned long v10;  // 4276
    unsigned long long v0;  // [bp-0x30]

    v0 = v1;
    Input__get_acceleration(0);
    if (!g_1fab2c9)
    {
        sub_f7d92c(&g_1ef22e8);
        g_1fab2c9 = 1;
    }
    ptr = g_1ef22e8->field_b8;
    v4 = v3 - ptr[2];
    v6 = (v5 - ptr[0]) * (v5 - ptr[0]);
    v8 = (v7 - ptr[1]) * (v7 - ptr[1]);
    v10 = arm64g_calculate_condition(64, ..., 0, 0);
    if (!((char)v10))
        return 1;
    return 0;
}
```

## `TiltState.Calibate` — RVA `0xc61838`

- Decompiled symbol: `TiltState_Calibate`
- Metadata signature: `public void Calibate() { }`
- Native interval: `12` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[89];
    char field_59;
} struct_0;

struct_0 * TiltState_Calibate(struct_0 *ptr)
{
    ptr->field_59 = 1;
    return ptr;
}
```

## `TiltState.IsCalibrated` — RVA `0xc61844`

- Decompiled symbol: `TiltState_IsCalibrated`
- Metadata signature: `public bool IsCalibrated() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[88];
    char field_58;
} struct_0;

long long TiltState_IsCalibrated(struct_0 *a0)
{
    return a0->field_58;
}
```

## `TiltState.Update` — RVA `0xc6184c`

- Decompiled symbol: `TiltState_Update`
- Metadata signature: `public void Update() { }`
- Native interval: `604` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: Decompiler produced no C-like text

```c
// 0x106184c: str d10, [sp, #-0x40]!
// 0x1061850: stp d9, d8, [sp, #8]
// 0x1061854: str x30, [sp, #0x18]
// 0x1061858: stp x22, x21, [sp, #0x20]
// 0x106185c: stp x20, x19, [sp, #0x30]
// 0x1061860: ldur x8, [x0, #0x24]
// 0x1061864: ldr w9, [x0, #0x2c]
// 0x1061868: adrp x20, #0x1fab000
// 0x106186c: mov x19, x0
// 0x1061870: str x8, [x0, #0x18]
// 0x1061874: str w9, [x0, #0x20]
// 0x1061878: ldrb w8, [x20, #0x2c9]
// 0x106187c: cbnz w8, #0x1061894
// 0x1061880: adrp x0, #0x1e8c000
// 0x1061884: ldr x0, [x0, #0x1e8]
// 0x1061888: bl #0xf7d92c
// 0x106188c: mov w8, #1
// 0x1061890: strb w8, [x20, #0x2c9]
// 0x1061894: adrp x21, #0x1e8c000
// 0x1061898: ldr x21, [x21, #0x1e8]
// 0x106189c: ldp s0, s9, [x19, #0x18]
// 0x10618a0: adrp x9, #0x832000
// 0x10618a4: ldr s1, [x9, #0x474]
// 0x10618a8: ldr x8, [x21]
// 0x10618ac: ldr s8, [x19, #0x20]
// 0x10618b0: fmul s2, s0, s0
// 0x10618b4: fmul s3, s9, s9
// 0x10618b8: ldr x9, [x8, #0xb8]
// 0x10618bc: fadd s2, s2, s3
// 0x10618c0: fmul s4, s8, s8
// 0x10618c4: fadd s10, s2, s4
// 0x10618c8: ldr d3, [x9]
// 0x10618cc: ldr s5, [x9, #8]
// 0x10618d0: fcmp s10, s1
// 0x10618d4: stur d3, [x19, #0x24]
// 0x10618d8: str s5, [x19, #0x2c]
// 0x10618dc: b.pl #0x1061900
// 0x10618e0: ldr x8, [x8, #0xb8]
// 0x10618e4: ldr d0, [x8]
// 0x10618e8: ldr s1, [x8, #8]
// 0x10618ec: ldr x8, [x19, #0x30]
// 0x10618f0: str d0, [x19, #0x18]
// 0x10618f4: str s1, [x19, #0x20]
// 0x10618f8: str x8, [x19, #0x40]
// 0x10618fc: b #0x10619f4
// 0x1061900: adrp x8, #0x832000
// 0x1061904: ldr s1, [x8, #0x534]
// 0x1061908: fmov s2, #-1.00000000
// 0x106190c: fadd s2, s10, s2
// 0x1061910: fabs s2, s2
// 0x1061914: fcmp s2, s1
// 0x1061918: b.le #0x10619b8
// 0x106191c: adrp x22, #0x1fab000
// 0x1061920: ldrb w8, [x22, #0x2c8]
// 0x1061924: cbnz w8, #0x106193c
// 0x1061928: adrp x0, #0x1e8c000
// 0x106192c: ldr x0, [x0, #0xa60]
// 0x1061930: bl #0xf7d92c
// 0x1061934: mov w8, #1
// 0x1061938: strb w8, [x22, #0x2c8]
// 0x106193c: adrp x8, #0x1e8c000
// 0x1061940: ldr x8, [x8, #0xa60]
// 0x1061944: ldr x0, [x8]
// 0x1061948: ldr w8, [x0, #0xe0]
// 0x106194c: cbnz w8, #0x1061954
// 0x1061950: bl #0xf7da5c
// 0x1061954: adrp x8, #0x832000
// 0x1061958: ldr s0, [x8, #0x41c]
// 0x106195c: fsqrt s1, s10
// 0x1061960: fcmp s1, s0
// 0x1061964: b.le #0x1061980
// 0x1061968: ldr d0, [x19, #0x18]
// 0x106196c: ldr s2, [x19, #0x20]
// 0x1061970: dup v3.2s, v1.s[0]
// 0x1061974: fdiv v0.2s, v0.2s, v3.2s
// 0x1061978: fdiv s8, s2, s1
// 0x106197c: b #0x10619ac
// 0x1061980: ldrb w8, [x20, #0x2c9]
// 0x1061984: cbnz w8, #0x106199c
// 0x1061988: adrp x0, #0x1e8c000
// 0x106198c: ldr x0, [x0, #0x1e8]
// 0x1061990: bl #0xf7d92c
// 0x1061994: mov w8, #1
// 0x1061998: strb w8, [x20, #0x2c9]
// 0x106199c: ldr x8, [x21]
// 0x10619a0: ldr x8, [x8, #0xb8]
// 0x10619a4: ldr d0, [x8]
// 0x10619a8: ldr s8, [x8, #8]
// 0x10619ac: mov s9, v0.s[1]
// 0x10619b0: str d0, [x19, #0x18]
// 0x10619b4: str s8, [x19, #0x20]
// 0x10619b8: fabs s1, s9
// 0x10619bc: fabs s2, s8
// 0x10619c0: fcmp s1, s2
// 0x10619c4: fcsel s1, s1, s2, gt
// 0x10619c8: bl #0x1db0c90
// 0x10619cc: adrp x8, #0x832000
// 0x10619d0: ldr s10, [x8, #0x554]
// 0x10619d4: mov v1.16b, v8.16b
// 0x10619d8: fmul s0, s0, s10
// 0x10619dc: str s0, [x19, #0x40]
// 0x10619e0: fneg s0, s9
// 0x10619e4: bl #0x1db0c90
// 0x10619e8: fmul s0, s0, s10
// 0x10619ec: str s0, [x19, #0x44]
// 0x10619f0: ldr x8, [x19, #0x40]
// 0x10619f4: ldrb w9, [x19, #0x59]
// 0x10619f8: lsr x10, x8, #0x20
// 0x10619fc: fmov s0, w8
// 0x1061a00: fmov s1, w10
// 0x1061a04: str x8, [x19, #0x38]
// 0x1061a08: cbz w9, #0x1061a28
// 0x1061a0c: mov w9, #1
// 0x1061a10: str x8, [x19, #0x30]
// 0x1061a14: str wzr, [x19, #0x30]
// 0x1061a18: fsub s1, s1, s1
// 0x1061a1c: strh w9, [x19, #0x58]
// 0x1061a20: str w8, [x19, #0x48]
// 0x1061a24: b #0x1061a48
// 0x1061a28: ldp s2, s3, [x19, #0x30]
// 0x1061a2c: ldrb w8, [x19, #0x58]
// 0x1061a30: fmov s4, wzr
// 0x1061a34: fsub s1, s1, s3
// 0x1061a38: cmp w8, #0
// 0x1061a3c: fsub s0, s0, s2
// 0x1061a40: fcsel s1, s4, s1, eq
// 0x1061a44: str s0, [x19, #0x48]
// 0x1061a48: ldp s2, s4, [x19, #0x10]
// 0x1061a4c: fabs s3, s0
// 0x1061a50: ldp x22, x21, [sp, #0x20]
// 0x1061a54: ldr x30, [sp, #0x18]
// 0x1061a58: fcmp s3, s2
// 0x1061a5c: fdiv s2, s3, s2
// 0x1061a60: fmov s3, #1.00000000
// 0x1061a64: fcsel s2, s2, s3, lt
// 0x1061a68: fcmp s0, #0.0
// 0x1061a6c: fneg s0, s2
// 0x1061a70: fcsel s0, s0, s2, mi
// 0x1061a74: fabs s2, s1
// 0x1061a78: fcmp s2, s4
// 0x1061a7c: fdiv s2, s2, s4
// 0x1061a80: stp s1, s0, [x19, #0x4c]
// 0x1061a84: fcsel s0, s2, s3, lt
// 0x1061a88: fneg s2, s0
// 0x1061a8c: fcmp s1, #0.0
// 0x1061a90: fcsel s0, s2, s0, mi
// 0x1061a94: str s0, [x19, #0x54]
// 0x1061a98: ldp x20, x19, [sp, #0x30]
// 0x1061a9c: ldp d9, d8, [sp, #8]
// 0x1061aa0: ldr d10, [sp], #0x40
// 0x1061aa4: ret
```

## `TiltState.GetAngles` — RVA `0xc61aa8`

- Decompiled symbol: `TiltState_GetAngles`
- Metadata signature: `public Vector2 GetAngles() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long TiltState_GetAngles(unsigned long a0)
{
    return a0;
}
```

## `TiltState.GetAnalog` — RVA `0xc61ab0`

- Decompiled symbol: `TiltState_GetAnalog`
- Metadata signature: `public Vector2 GetAnalog() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long TiltState_GetAnalog(unsigned long a0)
{
    return a0;
}
```
