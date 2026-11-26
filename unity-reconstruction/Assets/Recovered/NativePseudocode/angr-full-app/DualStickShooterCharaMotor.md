# Native pseudocode: DualStickShooterCharaMotor

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `DualStickShooterCharaMotor.OnEnable` — RVA `0xc66c3c`

- Decompiled symbol: `DualStickShooterCharaMotor_OnEnable`
- Metadata signature: `private void OnEnable() { }`
- Native interval: `144` bytes
- Result: `pseudocode`
- Heuristic layout hint: `DualStickShooterCharaMotor_Recovered` matched 3 offsets against `DualStickShooterCharaMotor` metadata (confidence 1.00).

```c
typedef struct DualStickShooterCharaMotor_Recovered {
    char padding_0[72];
    long long rb;
    char padding_50[60];
    unsigned int worldMoveAngle;
    unsigned int worldOrientAngle;
} DualStickShooterCharaMotor_Recovered;

extern long long g_1efd080;
extern char g_1fab30a;

long long DualStickShooterCharaMotor_OnEnable(struct_0 *ptr)
{
    unsigned int v0;  // s0
    long long v1;  // x1

    if (!(g_1fab30a & 1))
    {
        sub_f7d92c(&g_1efd080);
        g_1fab30a = 1;
    }
    if (Component__get_transform(ptr, 0))
    {
        Transform__get_forward();
        DualStickShooterCharaMotor__GetAngleFromDir();
        ptr->field_8c = v0;
        ptr->field_90 = v0;
        v1 = sub_1231bc8(ptr, g_1efd080);
        ptr->field_48 = v1;
        sub_f7d8d0((struct DualStickShooterCharaMotor_Recovered *)&ptr->field_48, v1);
        DualStickShooterCharaMotor__MoveOrientation(ptr); /* do not return */
    }
    sub_f7db74();
}
```

## `DualStickShooterCharaMotor.GetAngleFromDir` — RVA `0xc66ccc`

- Decompiled symbol: `DualStickShooterCharaMotor_GetAngleFromDir`
- Metadata signature: `public static float GetAngleFromDir(Vector3 dir, DualStickShooterCharaMotor.WorldPlane plane, float fallbackAngle) { }`
- Native interval: `244` bytes
- Result: `pseudocode`

```c
extern long long g_1ef22b8;
extern char g_1fab1e0;
extern char g_1fab243;

void DualStickShooterCharaMotor_GetAngleFromDir(unsigned int flag)
{
    unsigned int v0;  // s0
    unsigned int v1;  // s9
    unsigned long v9;  // 4140
    unsigned int v2;  // s2
    unsigned int v3;  // s8
    unsigned int v4;  // s8
    unsigned int v5;  // s1
    unsigned long v7;  // 4168
    unsigned int v8;  // s1

    v1 = v0;
    if (flag != 1)
    {
        v3 = v2;
        v4 = v3;
        if (!flag)
            goto LABEL_1066cf4;
        v1 = v3;
    }
    v4 = v5;
LABEL_1066cf4:
    v7 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(v1 * v1 + v4 * v4, 897988541)) >> 5 & 3 | (unsigned long long)(CmpF(v1 * v1 + v4 * v4, 897988541) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v1 * v1 + v4 * v4, 897988541)) >> 5 & 3 | (unsigned long long)(CmpF(v1 * v1 + v4 * v4, 897988541) & 1)) & ((unsigned long long)(char)(CmpF(v1 * v1 + v4 * v4, 897988541)) >> 5 & 3 | (unsigned long long)(CmpF(v1 * v1 + v4 * v4, 897988541) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if ((char)v7)
        return;
    if (!g_1fab243)
    {
        sub_f7d92c("_F");
        g_1fab243 = 1;
    }
    if (!g_1ef07e8->field_e0)
        sub_f7da5c(g_1ef07e8);
    v8 = [D] unsupported_Iop_SqrtF32();
    v9 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v8, 925353388)) >> 5 & 3 | (unsigned long long)(CmpF(v8, 925353388) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v8, 925353388)) >> 5 & 3 | (unsigned long long)(CmpF(v8, 925353388) & 1)) & ((unsigned long long)(char)(CmpF(v8, 925353388)) >> 5 & 3 | (unsigned long long)(CmpF(v8, 925353388) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if ((char)v9 && !g_1fab1e0)
    {
        sub_f7d92c(&g_1ef22b8);
        g_1fab1e0 = 1;
    }
    atan2f();
    return;
}
```

## `DualStickShooterCharaMotor.MoveOrientation` — RVA `0xc66dc0`

- Decompiled symbol: `DualStickShooterCharaMotor_MoveOrientation`
- Metadata signature: `private void MoveOrientation(float angle) { }`
- Native interval: `300` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[72];
    long long field_48;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern long long g_1ef22e8;
extern char g_1fab30b;
extern char g_1fab32c;

void DualStickShooterCharaMotor_MoveOrientation(struct_1 *ptr)
{
    unsigned long long v8;  // d11
    unsigned long long v9;  // d10
    unsigned long long v10;  // d9
    unsigned long long v11;  // d8
    unsigned long long v12;  // x30
    unsigned long long v13;  // x21
    unsigned long long v14;  // x20
    unsigned long long v15;  // x19
    long long v16;  // x0
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
    if (!(g_1fab30b & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab30b = 1;
    }
    if (!g_1fab32c)
    {
        sub_f7d92c(&g_1ef22e8);
        g_1fab32c = 1;
    }
    Quaternion__AngleAxis(0);
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (((char)Object__op_Inequality(ptr->field_48, 0, 0) & 1))
    {
        v16 = ptr->field_48;
    }
    else
    {
        v16 = Component__get_transform(ptr, 0);
        if (v16)
        {
            Transform__set_rotation();
            return;
        }
    }
    sub_f7db74(v16);
}
```

## `DualStickShooterCharaMotor.MovePosition` — RVA `0xc66eec`

- Decompiled symbol: `DualStickShooterCharaMotor_MovePosition`
- Metadata signature: `private void MovePosition(Vector3 worldPos) { }`
- Native interval: `212` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[72];
    long long field_48;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab30c;

void DualStickShooterCharaMotor_MovePosition(struct_1 *ptr)
{
    unsigned long long v7;  // d10
    unsigned long long v8;  // d9
    unsigned long long v9;  // d8
    unsigned long long v10;  // x30
    unsigned long long v11;  // x21
    unsigned long long v12;  // x20
    unsigned long long v13;  // x19
    long long v14;  // x0
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
    if (!(g_1fab30c & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab30c = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (((char)Object__op_Inequality(ptr->field_48, 0, 0) & 1))
    {
        v14 = ptr->field_48;
        if (v14)
        {
            Rigidbody__MovePosition();
            return;
        }
    }
    else
    {
        v14 = Component__get_transform(ptr, 0);
        if (v14)
        {
            Transform__set_position();
            return;
        }
    }
    sub_f7db74(v14);
}
```

## `DualStickShooterCharaMotor.Update` — RVA `0xc66fc0`

- Decompiled symbol: `DualStickShooterCharaMotor_Update`
- Metadata signature: `private void Update() { }`
- Native interval: `336` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1eeed00;
extern char g_1fab30d;

long long DualStickShooterCharaMotor_Update(long long *a0)
{
    unsigned long long v0;  // x0

    if (!(g_1fab30d & 1))
    {
        sub_f7d92c(&g_1eeed00);
        g_1fab30d = 1;
    }
    if (!((char)String__IsNullOrEmpty(a0[5], 0) & 1))
    {
        if (!g_1eeed00->field_e0)
            sub_f7da5c(g_1eeed00);
        CF2Input__GetAxis(a0[5], 0);
    }
    if (!((char)String__IsNullOrEmpty(a0[6], 0) & 1))
    {
        if (!g_1eeed00->field_e0)
            sub_f7da5c(g_1eeed00);
        CF2Input__GetAxis(a0[6], 0);
    }
    if (!((char)String__IsNullOrEmpty(a0[7], 0) & 1))
    {
        if (!g_1eeed00->field_e0)
            sub_f7da5c(g_1eeed00);
        CF2Input__GetAxis(a0[7], 0);
    }
    if (!((char)String__IsNullOrEmpty(a0[8], 0) & 1))
    {
        if (!g_1eeed00->field_e0)
            sub_f7da5c(g_1eeed00);
        CF2Input__GetAxis(a0[8], 0);
    }
    v0 = DualStickShooterCharaMotor__SetCameraRelativeInput(a0, a0[4]);
    return DualStickShooterCharaMotor__SetCameraRelativeInput(a0, a0[4]);
}
```

## `DualStickShooterCharaMotor.SetCameraRelativeInput` — RVA `0xc67110`

- Decompiled symbol: `DualStickShooterCharaMotor_SetCameraRelativeInput`
- Metadata signature: `public void SetCameraRelativeInput(Transform camTr, float moveX, float moveY, float aimX, float aimY) { }`
- Native interval: `120` bytes
- Result: `pseudocode`

```c
unsigned long long DualStickShooterCharaMotor_SetCameraRelativeInput(unsigned int *ptr, long long a1)
{
    unsigned long long v1;  // x0
    unsigned int v2;  // s0
    unsigned int v3;  // s2
    unsigned long flag;  // [bp-0x38]

    flag = 0;
    DualStickShooterCharaMotor__GetJoyAngleAndTilt(a1, 0, (unsigned long *)((char *)&flag + 4));
    v1 = DualStickShooterCharaMotor__GetJoyAngleAndTilt(a1, 0, &flag);
    ptr[37] = v2;
    ptr[38] = *((unsigned int *)((void*)&flag + 4));
    ptr[39] = v3;
    ptr[40] = flag;
    return v1;
}
```

## `DualStickShooterCharaMotor.FixedUpdate` — RVA `0xc67188`

- Decompiled symbol: `DualStickShooterCharaMotor_FixedUpdate`
- Metadata signature: `private void FixedUpdate() { }`
- Native interval: `668` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: Decompiler produced no C-like text

```c
// 0x1067188: sub sp, sp, #0x70
// 0x106718c: str d12, [sp, #0x20]
// 0x1067190: stp d11, d10, [sp, #0x30]
// 0x1067194: stp d9, d8, [sp, #0x40]
// 0x1067198: stp x30, x21, [sp, #0x50]
// 0x106719c: stp x20, x19, [sp, #0x60]
// 0x10671a0: adrp x8, #0x832000
// 0x10671a4: ldr s11, [x0, #0xa0]
// 0x10671a8: ldr s8, [x8, #0x4e0]
// 0x10671ac: mov x19, x0
// 0x10671b0: fcmp s11, s8
// 0x10671b4: b.le #0x10671c0
// 0x10671b8: add x8, x19, #0x9c
// 0x10671bc: b #0x10671d0
// 0x10671c0: ldr s11, [x19, #0x98]
// 0x10671c4: fcmp s11, s8
// 0x10671c8: b.le #0x1067274
// 0x10671cc: add x8, x19, #0x94
// 0x10671d0: fcmp s11, #0.0
// 0x10671d4: b.le #0x1067274
// 0x10671d8: ldr s10, [x8]
// 0x10671dc: ldr s9, [x19, #0x90]
// 0x10671e0: ldr s12, [x19, #0x5c]
// 0x10671e4: mov x0, xzr
// 0x10671e8: bl #0x1b89b60
// 0x10671ec: mov w8, #0x43b40000
// 0x10671f0: fsub s1, s10, s9
// 0x10671f4: fmov s2, w8
// 0x10671f8: mov w8, #-0x3c4c0000
// 0x10671fc: fdiv s6, s1, s2
// 0x1067200: fmov s5, w8
// 0x1067204: frintm s6, s6
// 0x1067208: fmul s6, s6, s5
// 0x106720c: fadd s1, s1, s6
// 0x1067210: fmov s4, wzr
// 0x1067214: mov w8, #0x43340000
// 0x1067218: fmin s2, s1, s2
// 0x106721c: fcmp s1, #0.0
// 0x1067220: fmov s6, w8
// 0x1067224: fcsel s1, s2, s4, pl
// 0x1067228: fmul s3, s11, s12
// 0x106722c: fadd s2, s1, s5
// 0x1067230: fcmp s1, s6
// 0x1067234: fcsel s2, s2, s1, gt
// 0x1067238: fnmul s1, s3, s0
// 0x106723c: fcmp s2, s1
// 0x1067240: fmul s0, s3, s0
// 0x1067244: b.le #0x1067250
// 0x1067248: fcmp s2, s0
// 0x106724c: b.mi #0x1067270
// 0x1067250: fadd s2, s9, s2
// 0x1067254: fsub s3, s2, s9
// 0x1067258: fcmp s3, #0.0
// 0x106725c: fabd s4, s2, s9
// 0x1067260: fcsel s1, s0, s1, ge
// 0x1067264: fadd s1, s9, s1
// 0x1067268: fcmp s4, s0
// 0x106726c: fcsel s10, s1, s2, hi
// 0x1067270: str s10, [x19, #0x90]
// 0x1067274: ldr s1, [x19, #0x98]
// 0x1067278: fcmp s1, s8
// 0x106727c: b.le #0x106728c
// 0x1067280: ldr s0, [x19, #0x94]
// 0x1067284: str s0, [x19, #0x8c]
// 0x1067288: b #0x1067294
// 0x106728c: ldr s0, [x19, #0x8c]
// 0x1067290: fmov s1, wzr
// 0x1067294: str s1, [x19, #0x88]
// 0x1067298: ldr s1, [x19, #0x90]
// 0x106729c: adrp x20, #0x1fab000
// 0x10672a0: ldrb w8, [x20, #0x32c]
// 0x10672a4: fsub s8, s0, s1
// 0x10672a8: cbnz w8, #0x10672c0
// 0x10672ac: adrp x0, #0x1e8c000
// 0x10672b0: ldr x0, [x0, #0x1e8]
// 0x10672b4: bl #0xf7d92c
// 0x10672b8: mov w8, #1
// 0x10672bc: strb w8, [x20, #0x32c]
// 0x10672c0: adrp x21, #0x1e8c000
// 0x10672c4: ldr x21, [x21, #0x1e8]
// 0x10672c8: mov v0.16b, v8.16b
// 0x10672cc: mov x0, xzr
// 0x10672d0: ldr x8, [x21]
// 0x10672d4: ldr x8, [x8, #0xb8]
// 0x10672d8: ldp s1, s2, [x8, #0x18]
// 0x10672dc: ldr s3, [x8, #0x20]
// 0x10672e0: bl #0x1b8b260
// 0x10672e4: fmov s4, wzr
// 0x10672e8: fmov s5, wzr
// 0x10672ec: fmov s6, #1.00000000
// 0x10672f0: mov x0, xzr
// 0x10672f4: bl #0x1b8b504
// 0x10672f8: ldp s4, s12, [x19, #0x88]
// 0x10672fc: mov w8, #0x50
// 0x1067300: mov w9, #0x58
// 0x1067304: ldr s3, [x19, #0x54]
// 0x1067308: fmul s9, s1, s4
// 0x106730c: fmul s1, s2, s4
// 0x1067310: fmul s0, s0, s4
// 0x1067314: fcmp s1, #0.0
// 0x1067318: stp s0, s9, [x19, #0x7c]
// 0x106731c: str s1, [x19, #0x84]
// 0x1067320: csel x8, x9, x8, lt
// 0x1067324: ldr s2, [x19, x8]
// 0x1067328: ldrb w8, [x20, #0x32c]
// 0x106732c: fmul s11, s0, s3
// 0x1067330: fmul s10, s1, s2
// 0x1067334: cbnz w8, #0x106734c
// 0x1067338: adrp x0, #0x1e8c000
// 0x106733c: ldr x0, [x0, #0x1e8]
// 0x1067340: bl #0xf7d92c
// 0x1067344: mov w8, #1
// 0x1067348: strb w8, [x20, #0x32c]
// 0x106734c: ldr x8, [x21]
// 0x1067350: fsub s0, s12, s8
// 0x1067354: mov x0, xzr
// 0x1067358: ldr x8, [x8, #0xb8]
// 0x106735c: ldp s1, s2, [x8, #0x18]
// 0x1067360: ldr s3, [x8, #0x20]
// 0x1067364: bl #0x1b8b260
// 0x1067368: mov v4.16b, v11.16b
// 0x106736c: mov v5.16b, v9.16b
// 0x1067370: mov v6.16b, v10.16b
// 0x1067374: mov x0, xzr
// 0x1067378: bl #0x1b8b504
// 0x106737c: mov x0, x19
// 0x1067380: mov x1, xzr
// 0x1067384: stp s0, s1, [x19, #0x70]
// 0x1067388: str s2, [x19, #0x78]
// 0x106738c: bl #0x1b92154
// 0x1067390: cbz x0, #0x1067420
// 0x1067394: mov x1, xzr
// 0x1067398: bl #0x1b9d508
// 0x106739c: ldr d9, [x19, #0x70]
// 0x10673a0: ldr s10, [x19, #0x78]
// 0x10673a4: mov x0, xzr
// 0x10673a8: str d0, [sp, #0x10]
// 0x10673ac: str d1, [sp]
// 0x10673b0: mov v8.16b, v2.16b
// 0x10673b4: bl #0x1b89b60
// 0x10673b8: ldp q3, q2, [sp]
// 0x10673bc: fmul v1.2s, v9.2s, v0.s[0]
// 0x10673c0: fmul s0, s10, s0
// 0x10673c4: ldur d9, [x19, #0x64]
// 0x10673c8: ldr s10, [x19, #0x6c]
// 0x10673cc: mov v2.s[1], v3.s[0]
// 0x10673d0: mov x0, xzr
// 0x10673d4: fadd v11.2s, v2.2s, v1.2s
// 0x10673d8: fadd s8, s8, s0
// 0x10673dc: bl #0x1b89b60
// 0x10673e0: fmul v1.2s, v9.2s, v0.s[0]
// 0x10673e4: fmul s2, s10, s0
// 0x10673e8: fadd v0.2s, v11.2s, v1.2s
// 0x10673ec: fadd s2, s8, s2
// 0x10673f0: mov s1, v0.s[1]
// 0x10673f4: mov x0, x19
// 0x10673f8: bl #0x1066eec
// 0x10673fc: ldr s0, [x19, #0x90]
// 0x1067400: mov x0, x19
// 0x1067404: ldp x20, x19, [sp, #0x60]
// 0x1067408: ldp x30, x21, [sp, #0x50]
// 0x106740c: ldp d9, d8, [sp, #0x40]
// 0x1067410: ldp d11, d10, [sp, #0x30]
// 0x1067414: ldr d12, [sp, #0x20]
// 0x1067418: add sp, sp, #0x70
// 0x106741c: b #0x1066dc0
// 0x1067420: bl #0xf7db74
```

## `DualStickShooterCharaMotor.GetOrientAngle` — RVA `0xc67424`

- Decompiled symbol: `DualStickShooterCharaMotor_GetOrientAngle`
- Metadata signature: `public float GetOrientAngle() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long DualStickShooterCharaMotor_GetOrientAngle(unsigned long a0)
{
    return a0;
}
```

## `DualStickShooterCharaMotor.GetLocalDir` — RVA `0xc6742c`

- Decompiled symbol: `DualStickShooterCharaMotor_GetLocalDir`
- Metadata signature: `public Vector3 GetLocalDir() { }`
- Native interval: `12` bytes
- Result: `pseudocode`

```c
long long DualStickShooterCharaMotor_GetLocalDir(unsigned long a0)
{
    return a0;
}
```

## `DualStickShooterCharaMotor.SetWorldInput` — RVA `0xc67438`

- Decompiled symbol: `DualStickShooterCharaMotor_SetWorldInput`
- Metadata signature: `public void SetWorldInput(float moveAngle, float moveTilt, float aimAngle, float aimTilt) { }`
- Native interval: `12` bytes
- Result: `pseudocode`

```c
unsigned int [41] DualStickShooterCharaMotor_SetWorldInput(unsigned int *ptr)
{
    unsigned int v0;  // s0
    unsigned int v1;  // s1
    unsigned int v2;  // s2
    unsigned int v3;  // s3

    ptr[37] = v0;
    ptr[38] = v1;
    ptr[39] = v2;
    ptr[40] = v3;
    return ptr;
}
```

## `DualStickShooterCharaMotor.GetJoyAngleAndTilt` — RVA `0xc67444`

- Decompiled symbol: `DualStickShooterCharaMotor_GetJoyAngleAndTilt`
- Metadata signature: `public static float GetJoyAngleAndTilt(Transform camTr, float x, float y, DualStickShooterCharaMotor.WorldPlane plane, out float tilt) { }`
- Native interval: `208` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[224];
    unsigned int field_e0;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern char g_1fab243;

struct_1 * DualStickShooterCharaMotor_GetJoyAngleAndTilt(struct_0 *a0, unsigned long a1, unsigned int *ptr)
{
    unsigned int v0;  // s0
    unsigned int v1;  // s1
    unsigned long v3;  // 4192
    unsigned int v4;  // s2
    unsigned long v5;  // 4179
    unsigned long long v7;  // x0

    v3 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(v0 * v0 + v1 * v1, 897988541)) >> 5 & 3 | (unsigned long long)(CmpF(v0 * v0 + v1 * v1, 897988541) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v0 * v0 + v1 * v1, 897988541)) >> 5 & 3 | (unsigned long long)(CmpF(v0 * v0 + v1 * v1, 897988541) & 1)) & ((unsigned long long)(char)(CmpF(v0 * v0 + v1 * v1, 897988541)) >> 5 & 3 | (unsigned long long)(CmpF(v0 * v0 + v1 * v1, 897988541) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if (!((char)v3))
    {
        DualStickShooterCharaMotor__GetWorldVecFromCamera();
        if (!g_1fab243)
        {
            sub_f7d92c("_F");
            g_1fab243 = 1;
        }
        a0 = g_1ef07e8;
        if (!g_1ef07e8->field_e0)
            a0 = sub_f7da5c(g_1ef07e8);
        v4 = [D] unsupported_Iop_SqrtF32();
        v5 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v4, 953267991)) >> 5 & 3 | (unsigned long long)(CmpF(v4, 953267991) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v4, 953267991)) >> 5 & 3 | (unsigned long long)(CmpF(v4, 953267991) & 1)) & ((unsigned long long)(char)(CmpF(v4, 953267991)) >> 5 & 3 | (unsigned long long)(CmpF(v4, 953267991) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if ((char)v5)
        {
            *(ptr) = [D] unsupported_Iop_ZeroHI96ofV128();
            v7 = atan2f();
            return atan2f();
        }
    }
    *(ptr) = 0;
    return a0;
}
```

## `DualStickShooterCharaMotor.GetWorldVecFromCamera` — RVA `0xc67514`

- Decompiled symbol: `DualStickShooterCharaMotor_GetWorldVecFromCamera`
- Metadata signature: `public static Vector3 GetWorldVecFromCamera(Transform camTr, float x, float y, DualStickShooterCharaMotor.WorldPlane plane) { }`
- Native interval: `568` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[224];
    unsigned int field_e0;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern long long g_1ef22e8;
extern char g_1fab2c8;
extern char g_1fab2c9;

struct_1 * DualStickShooterCharaMotor_GetWorldVecFromCamera(long long a0, unsigned int flag)
{
    unsigned int v0;  // s1
    unsigned long v1;  // 4196
    struct_0 *v2;  // x0
    unsigned int v3;  // s3
    unsigned long v4;  // 4188

    if (flag != 1)
    {
        if (!flag)
        {
            if (a0)
            {
                Transform__get_right(a0, 0);
                Transform__get_forward(a0, 0);
            }
            else
            {
                sub_f7db74();
            }
        }
        else
        {
            if (a0)
            {
                Transform__get_forward(a0, 0);
                Transform__get_up(a0, 0);
            }
            else
            {
                sub_f7db74();
            }
        }
    }
    else
    {
        if (a0)
        {
            Transform__get_right(a0, 0);
            Transform__get_up(a0, 0);
        }
        else
        {
            sub_f7db74();
        }
    }
    if (!g_1fab2c8)
    {
        sub_f7d92c("_F");
        g_1fab2c8 = 1;
    }
    if (!g_1ef07e8->field_e0)
        sub_f7da5c(g_1ef07e8);
    v0 = [D] unsupported_Iop_SqrtF32();
    v1 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v0, 925353388)) >> 5 & 3 | (unsigned long long)(CmpF(v0, 925353388) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v0, 925353388)) >> 5 & 3 | (unsigned long long)(CmpF(v0, 925353388) & 1)) & ((unsigned long long)(char)(CmpF(v0, 925353388)) >> 5 & 3 | (unsigned long long)(CmpF(v0, 925353388) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if ((char)v1 && !g_1fab2c9)
    {
        sub_f7d92c(&g_1ef22e8);
        g_1fab2c9 = 1;
    }
    if (!g_1fab2c8)
    {
        sub_f7d92c("_F");
        g_1fab2c8 = 1;
    }
    v2 = g_1ef07e8;
    if (!g_1ef07e8->field_e0)
        v2 = sub_f7da5c(g_1ef07e8);
    v3 = [D] unsupported_Iop_SqrtF32();
    v4 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v3, 925353388)) >> 5 & 3 | (unsigned long long)(CmpF(v3, 925353388) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v3, 925353388)) >> 5 & 3 | (unsigned long long)(CmpF(v3, 925353388) & 1)) & ((unsigned long long)(char)(CmpF(v3, 925353388)) >> 5 & 3 | (unsigned long long)(CmpF(v3, 925353388) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if (!((char)v4))
        return v2;
    if (!g_1fab2c9)
    {
        v2 = sub_f7d92c(&g_1ef22e8);
        g_1fab2c9 = 1;
    }
    return v2;
}
```

## `DualStickShooterCharaMotor.AngleToWorldVec` — RVA `0xc6774c`

- Decompiled symbol: `DualStickShooterCharaMotor_AngleToWorldVec`
- Metadata signature: `public static Vector3 AngleToWorldVec(float angle, DualStickShooterCharaMotor.WorldPlane plane) { }`
- Native interval: `108` bytes
- Result: `pseudocode`

```c
long long DualStickShooterCharaMotor_AngleToWorldVec(unsigned int flag)
{
    unsigned long v2;  // x0
    char v0;  // [bp-0x18]
    char v1;  // [bp-0x14]

    v2 = sincosf(&v1, &v0);
    if (!flag)
    {
        return v2;
    }
    else if (flag != 1)
    {
        return v2;
    }
    else
    {
        return v2;
    }
}
```

## `DualStickShooterCharaMotor.RotateVecOnPlane` — RVA `0xc677b8`

- Decompiled symbol: `DualStickShooterCharaMotor_RotateVecOnPlane`
- Metadata signature: `public static Vector3 RotateVecOnPlane(Vector3 v, float angle, DualStickShooterCharaMotor.WorldPlane plane) { }`
- Native interval: `176` bytes
- Result: `pseudocode`

```c
long long DualStickShooterCharaMotor_RotateVecOnPlane(unsigned int flag)
{
    unsigned long v2;  // x0
    char v0;  // [bp-0x28]
    char v1;  // [bp-0x24]

    v2 = sincosf(&v1, &v0);
    if (!flag)
    {
        return v2;
    }
    else if (flag == 1)
    {
        return v2;
    }
    else
    {
        return v2;
    }
}
```

## `DualStickShooterCharaMotor.ctor` — RVA `0xc67868`

- Decompiled symbol: `DualStickShooterCharaMotor_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `240` bytes
- Result: `pseudocode`
- Heuristic layout hint: `DualStickShooterCharaMotor_Recovered` matched 6 offsets against `DualStickShooterCharaMotor` metadata (confidence 0.86).

```c
typedef struct DualStickShooterCharaMotor_Recovered {
    char padding_0[40];
    long long moveHorzAxis;
    long long moveVertAxis;
    long long aimHorzAxis;
    long long aimVertAxis;
    char padding_48[8];
    uint128_t forwardSpeed;
    char padding_60[4];
    unsigned long long gravity;
    unsigned int field_6c;
} DualStickShooterCharaMotor_Recovered;

extern long long g_1f0ab18;
extern long long g_1f0ab48;
extern long long g_1f0f998;
extern long long g_1f0f9c8;
extern char g_1fab30e;

void DualStickShooterCharaMotor_ctor(struct_0 *ptr)
{
    unsigned long long v7;  // x30
    unsigned long long v8;  // x24
    struct_0 *p;  // x0
    unsigned long long v9;  // x23
    unsigned long long v10;  // x22
    unsigned long long v11;  // x21
    unsigned long long v12;  // x20
    unsigned long long v13;  // x19
    struct_0 *addr;  // x0
    struct_0 *ptr3;  // x0
    struct_0 *ptr4;  // x0
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
    if (!(g_1fab30e & 1))
    {
        sub_f7d92c(&g_1f0f9c8);
        sub_f7d92c(&g_1f0f998);
        sub_f7d92c(&g_1f0ab48);
        sub_f7d92c(&g_1f0ab18);
        g_1fab30e = 1;
    }
    addr = ptr;
    addr->field_28 = g_1f0ab18;
    sub_f7d8d0((struct DualStickShooterCharaMotor_Recovered *)&addr->field_28, g_1f0ab18);
    ptr3 = ptr;
    ptr3->field_30 = g_1f0f998;
    sub_f7d8d0((struct DualStickShooterCharaMotor_Recovered *)&ptr3->field_30, g_1f0f998);
    ptr4 = ptr;
    ptr4->field_38 = g_1f0ab48;
    sub_f7d8d0((struct DualStickShooterCharaMotor_Recovered *)&ptr4->field_38, g_1f0ab48);
    p = ptr;
    p->field_40 = g_1f0f9c8;
    sub_f7d8d0((struct DualStickShooterCharaMotor_Recovered *)&p->field_40, g_1f0f9c8);
    *((unsigned int *)((char *)&ptr->field_64 + 4)) = 0;
    *((void*)&ptr->field_50) = 0x443400004080000040c0000041200000;
    *((unsigned long *)&(&ptr->padding_60)[1]) = 0xc000000000000000;
    MonoBehaviour__ctor();
    return;
}
```
