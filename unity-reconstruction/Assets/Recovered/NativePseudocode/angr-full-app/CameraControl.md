# Native pseudocode: CameraControl

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `CameraControl.Start` — RVA `0xc88d1c`

- Decompiled symbol: `CameraControl_Start`
- Metadata signature: `private void Start() { }`
- Native interval: `876` bytes
- Result: `pseudocode`
- Heuristic layout hint: `CameraControl_Recovered` matched 19 offsets against `CameraControl` metadata (confidence 1.00).

```c
typedef struct CameraControl_Recovered {
    char padding_0[40];
    long long playerObj;
    long long weaponObj;
    long long myTransform;
    long long FPSWalkerComponent;
    long long IronsightsComponent;
    long long MouseLookComponent;
    long long WorldRecenterComponent;
    struct struct_2 *FPSPlayerComponent;
    long long InputComponent;
    long long GunSwayComponent;
    long long CamAndWeapAnimsComponent;
    char padding_80[8];
    long long AnimatorComponent;
    long long PlayerWeaponsComponent;
    char padding_98[136];
    long long playerObjTransform;
    long long mainCameraTransform;
    char padding_130[68];
    unsigned long long offset;
    unsigned long long offsetAmt;
    char padding_184[36];
    unsigned int zoomDistance;
    char padding_1ac[24];
    unsigned int currentDistance;
} CameraControl_Recovered;

typedef struct struct_1 {
    char padding_0[200];
    unsigned long long field_c8;
} struct_1;

typedef struct struct_2 {
    char padding_0[200];
    long long field_c8;
} struct_2;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern long long g_1efcf08;
extern long long g_1efcf28;
extern long long g_1efd098;
extern long long g_1efebb8;
extern long long g_1efebc0;
extern long long g_1efebd8;
extern long long g_1efec08;
extern long long g_1efec18;
extern long long g_1efec90;
extern long long g_1efed30;
extern char g_1fab432;

long long CameraControl_Start(struct_3 *ptr)
{
    long long v0;  // x0
    struct_3 *addr;  // x20
    struct_3 *ptr3;  // x0
    long long v11;  // x0
    struct_3 *ptr4;  // x20
    struct_3 *ptr13;  // x20
    long long v14;  // x0
    struct_3 *ptr5;  // x20
    struct_3 *ptr14;  // x20
    long long v17;  // x0
    struct_3 *ptr6;  // x20
    struct_3 *ptr15;  // x20
    struct_3 *ptr16;  // x20
    long long v20;  // x1
    struct_3 *ptr7;  // x0
    long long v22;  // x0
    struct_3 *ptr8;  // x20
    struct_3 *ptr17;  // x20
    long long v25;  // x0
    struct_3 *ptr9;  // x20
    struct_3 *ptr18;  // x20
    long long v28;  // x0
    struct_3 *ptr10;  // x20
    unsigned long v3;  // x0
    struct_3 *ptr19;  // x20
    long long v31;  // x0
    long long v32;  // x1
    struct_3 *ptr11;  // x0
    long long v34;  // x0
    struct_3 *p;  // x19
    unsigned long v36;  // x0
    long long v4;  // x1
    long long v5;  // x1
    struct_1 *v6;  // x0
    struct_3 *ptr12;  // x20
    struct_3 *v8;  // x20
    unsigned long v9;  // x1

    if (!(g_1fab432 & 1))
    {
        sub_f7d92c(&g_1efcf08);
        sub_f7d92c(&g_1efcf28);
        sub_f7d92c(&g_1efd098);
        sub_f7d92c(&g_1efebb8);
        sub_f7d92c(&g_1efebc0);
        sub_f7d92c(&g_1efebd8);
        sub_f7d92c(&g_1efec08);
        sub_f7d92c(&g_1efec18);
        sub_f7d92c(&g_1efec90);
        sub_f7d92c(&g_1efed30);
        sub_f7d92c(&g_1ef0c58);
        g_1fab432 = 1;
    }
    v0 = Component__get_transform(ptr, 0);
    addr = ptr;
    addr->field_38 = v0;
    ptr16 = &addr->field_38;
    sub_f7d8d0(ptr16, v0);
    v3 = *((long long *)&ptr16->padding_0[16]);
    if (v3)
    {
        v4 = GameObject__get_transform(v3, 0);
        ptr->field_120 = v4;
        sub_f7d8d0((struct CameraControl_Recovered *)&ptr->field_120, v4);
        v3 = Camera__get_main(0);
        if (v3)
        {
            v5 = Component__get_transform();
            ptr->field_128 = v5;
            sub_f7d8d0((struct CameraControl_Recovered *)&ptr->field_128, v5);
            v3 = ptr->field_28;
            if (v3)
            {
                v6 = sub_1249224(v3, g_1efebb8);
                ptr12 = ptr;
                ptr12->field_60 = v6;
                v8 = &ptr12->field_60;
                v3 = sub_f7d8d0(v8, v6);
                if (*((long long *)&v8->padding_0[0]))
                {
                    v9 = *((long long *)(*((long long *)&v8->padding_0[0]) + 200));
                    ptr3 = ptr;
                    ptr3->field_30 = v9;
                    sub_f7d8d0((struct CameraControl_Recovered *)&ptr3->field_30, v9);
                    v3 = Component__get_transform(ptr, 0);
                    if (v3)
                    {
                        v3 = Transform__get_parent();
                        if (v3)
                        {
                            v3 = Component__get_transform();
                            if (v3)
                            {
                                v11 = sub_1231bc8();
                                ptr4 = ptr;
                                ptr4->field_50 = v11;
                                ptr13 = &ptr4->field_50;
                                sub_f7d8d0(ptr13, v11);
                                v3 = *((long long *)&ptr13->padding_0[32]);
                                if (v3)
                                {
                                    v14 = sub_1249224(v3, g_1efebd8);
                                    ptr5 = ptr;
                                    ptr5->field_70 = v14;
                                    ptr14 = &ptr5->field_70;
                                    sub_f7d8d0(ptr14, v14);
                                    v3 = ptr14->field_48;
                                    if (v3)
                                    {
                                        v17 = sub_1249224(v3, g_1efebc0);
                                        ptr6 = ptr;
                                        ptr6->field_40 = v17;
                                        ptr15 = &ptr6->field_40;
                                        sub_f7d8d0(ptr15, v17);
                                        v3 = *((long long *)&ptr15->padding_0[24]);
                                        if (v3)
                                        {
                                            v20 = sub_1249224(v3, g_1efec18);
                                            ptr7 = ptr;
                                            ptr7->field_48 = v20;
                                            sub_f7d8d0((struct CameraControl_Recovered *)&ptr7->field_48, v20);
                                            v3 = Component__get_transform(ptr, 0);
                                            if (v3)
                                            {
                                                v3 = Transform__get_parent();
                                                if (v3)
                                                {
                                                    v3 = Component__get_transform();
                                                    if (v3)
                                                    {
                                                        v22 = sub_1231bc8();
                                                        ptr8 = ptr;
                                                        ptr8->field_78 = v22;
                                                        ptr17 = &ptr8->field_78;
                                                        sub_f7d8d0(ptr17, v22);
                                                        v3 = ptr17->field_48;
                                                        if (v3)
                                                        {
                                                            v25 = sub_1249224(v3, g_1efec90);
                                                            ptr9 = ptr;
                                                            ptr9->field_90 = v25;
                                                            ptr18 = &ptr9->field_90;
                                                            sub_f7d8d0(ptr18, v25);
                                                            v3 = ptr18->field_68;
                                                            if (v3)
                                                            {
                                                                v28 = sub_1249224(v3, g_1efec08);
                                                                ptr10 = ptr;
                                                                ptr10->field_68 = v28;
                                                                ptr19 = &ptr10->field_68;
                                                                sub_f7d8d0(ptr19, v28);
                                                                v3 = ptr19->field_40;
                                                                if (v3)
                                                                {
                                                                    v31 = sub_1249224(v3, g_1efed30);
                                                                    if (!g_1ef0c58->field_e0)
                                                                        sub_f7da5c(g_1ef0c58);
                                                                    if (!((char)Object__op_Implicit(v31, 0) & 1))
                                                                    {
                                                                        v34 = sub_1231bc8(ptr, g_1efcf08);
                                                                        ptr->field_88 = v34;
                                                                        p = &ptr->field_88;
                                                                        v36 = sub_f7d8d0(p, v34);
                                                                        *((long long *)((char *)&ptr->field_174 + 4)) = *((long long *)&(&ptr->padding_130)[1]);
                                                                        *((unsigned int *)&p->padding_130[12]) = 0;
                                                                        *((unsigned int *)&p->field_120) = 0;
                                                                        return v36;
                                                                    }
                                                                    v3 = ptr->field_28;
                                                                    if (v3)
                                                                    {
                                                                        v32 = sub_1249224(v3, g_1efed30);
                                                                        ptr11 = ptr;
                                                                        ptr11->field_58 = v32;
                                                                        sub_f7d8d0((struct CameraControl_Recovered *)&ptr11->field_58, v32);
                                                                        v34 = sub_1231bc8(ptr, g_1efcf08);
                                                                        ptr->field_88 = v34;
                                                                        p = &ptr->field_88;
                                                                        v36 = sub_f7d8d0(p, v34);
                                                                        *((long long *)((char *)&ptr->field_174 + 4)) = *((long long *)&(&ptr->padding_130)[1]);
                                                                        *((unsigned int *)&p->padding_130[12]) = 0;
                                                                        *((unsigned int *)&p->field_120) = 0;
                                                                        return v36;
                                                                    }
                                                                }
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    sub_f7db74(v3);
}
```

## `CameraControl.Update` — RVA `0xc89088`

- Decompiled symbol: `CameraControl_Update`
- Metadata signature: `private void Update() { }`
- Native interval: `6312` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: Decompiler produced no C-like text

```c
// 0x1089088: sub sp, sp, #0x120
// 0x108908c: stp d15, d14, [sp, #0xa0]
// 0x1089090: stp d13, d12, [sp, #0xb0]
// 0x1089094: stp d11, d10, [sp, #0xc0]
// 0x1089098: stp d9, d8, [sp, #0xd0]
// 0x108909c: stp x29, x30, [sp, #0xe0]
// 0x10890a0: stp x24, x23, [sp, #0xf0]
// 0x10890a4: stp x22, x21, [sp, #0x100]
// 0x10890a8: stp x20, x19, [sp, #0x110]
// 0x10890ac: adrp x20, #0x1fab000
// 0x10890b0: ldrb w8, [x20, #0x433]
// 0x10890b4: mov x19, x0
// 0x10890b8: tbnz w8, #0, #0x10890e8
// 0x10890bc: adrp x0, #0x1e8c000
// 0x10890c0: ldr x0, [x0, #0xe0]
// 0x10890c4: bl #0xf7d92c
// 0x10890c8: adrp x0, #0x1e8c000
// 0x10890cc: ldr x0, [x0, #0xd8]
// 0x10890d0: bl #0xf7d92c
// 0x10890d4: adrp x0, #0x1e8d000
// 0x10890d8: ldr x0, [x0, #0xfd0]
// 0x10890dc: bl #0xf7d92c
// 0x10890e0: mov w8, #1
// 0x10890e4: strb w8, [x20, #0x433]
// 0x10890e8: movi v0.2d, #0000000000000000
// 0x10890ec: mov x0, xzr
// 0x10890f0: str wzr, [sp, #0x90]
// 0x10890f4: stp q0, q0, [sp, #0x70]
// 0x10890f8: bl #0x1b9ae58
// 0x10890fc: fcmp s0, #0.0
// 0x1089100: b.le #0x108a7c0
// 0x1089104: mov x0, xzr
// 0x1089108: bl #0x1b89b60
// 0x108910c: fcmp s0, #0.0
// 0x1089110: b.le #0x108a7c0
// 0x1089114: mov x0, xzr
// 0x1089118: bl #0x1b9ae30
// 0x108911c: fcmp s0, #0.0
// 0x1089120: b.le #0x108a7c0
// 0x1089124: mov x0, xzr
// 0x1089128: bl #0x1b9ad30
// 0x108912c: fcmp s0, #0.0
// 0x1089130: b.le #0x108a7c0
// 0x1089134: ldr x8, [x19, #0x90]
// 0x1089138: cbz x8, #0x108a92c
// 0x108913c: ldr x1, [x8, #0x98]
// 0x1089140: mov x20, x19
// 0x1089144: str x1, [x20, #0x98]!
// 0x1089148: mov x0, x20
// 0x108914c: bl #0xf7d8d0
// 0x1089150: ldrb w8, [x20, #0x6c]
// 0x1089154: cbz w8, #0x108921c
// 0x1089158: ldr x8, [x19, #0x68]
// 0x108915c: cbz x8, #0x108a92c
// 0x1089160: ldrb w8, [x8, #0x9a]
// 0x1089164: cbz w8, #0x108918c
// 0x1089168: mov x0, xzr
// 0x108916c: bl #0x1b9ad30
// 0x1089170: ldrb w8, [x19, #0x106]
// 0x1089174: str s0, [x19, #0x1a0]
// 0x1089178: strb wzr, [x19, #0x1a4]
// 0x108917c: cbnz w8, #0x108918c
// 0x1089180: mov w8, #1
// 0x1089184: strb w8, [x19, #0x106]
// 0x1089188: strb w8, [x19, #0x1a4]
// 0x108918c: ldr x8, [x19, #0x68]
// 0x1089190: cbz x8, #0x108a92c
// 0x1089194: ldrb w8, [x8, #0x99]
// 0x1089198: ldr s9, [x19, #0x1a0]
// 0x108919c: mov x0, xzr
// 0x10891a0: cbz w8, #0x10891d8
// 0x10891a4: bl #0x1b9ad30
// 0x10891a8: adrp x8, #0x832000
// 0x10891ac: ldr s1, [x8, #0x4f4]
// 0x10891b0: fadd s1, s9, s1
// 0x10891b4: fcmp s1, s0
// 0x10891b8: b.pl #0x108921c
// 0x10891bc: ldr x8, [x19, #0x60]
// 0x10891c0: cbz x8, #0x108a92c
// 0x10891c4: ldrb w8, [x8, #0x2d0]
// 0x10891c8: cbnz w8, #0x108921c
// 0x10891cc: mov w8, #1
// 0x10891d0: strb w8, [x19, #0x1a5]
// 0x10891d4: b #0x108921c
// 0x10891d8: bl #0x1b89b60
// 0x10891dc: mov x0, xzr
// 0x10891e0: mov v8.16b, v0.16b
// 0x10891e4: bl #0x1b9ad30
// 0x10891e8: fmov s1, #30.00000000
// 0x10891ec: fmul s1, s8, s1
// 0x10891f0: fadd s1, s9, s1
// 0x10891f4: fcmp s1, s0
// 0x10891f8: b.le #0x1089204
// 0x10891fc: ldrb w8, [x19, #0x1a4]
// 0x1089200: cbz w8, #0x108a4c0
// 0x1089204: ldrb w8, [x19, #0x1a6]
// 0x1089208: strb wzr, [x19, #0x1a5]
// 0x108920c: cbz w8, #0x1089214
// 0x1089210: strb wzr, [x19, #0x1a7]
// 0x1089214: mov w8, #1
// 0x1089218: strb w8, [x19, #0x1a4]
// 0x108921c: ldr x8, [x20]
// 0x1089220: cbz x8, #0x108a92c
// 0x1089224: ldrb w9, [x8, #0x25c]
// 0x1089228: cbz w9, #0x1089294
// 0x108922c: ldr x9, [x19, #0x60]
// 0x1089230: cbz x9, #0x108a92c
// 0x1089234: ldrb w9, [x9, #0x2d0]
// 0x1089238: cbz w9, #0x1089274
// 0x108923c: ldrb w9, [x19, #0x106]
// 0x1089240: cbz w9, #0x1089274
// 0x1089244: ldr x9, [x19, #0x90]
// 0x1089248: cbz x9, #0x108a92c
// 0x108924c: ldr s8, [x9, #0x120]
// 0x1089250: ldr s9, [x8, #0x3d4]
// 0x1089254: mov x0, xzr
// 0x1089258: bl #0x1b9ad30
// 0x108925c: fadd s1, s8, s9
// 0x1089260: fcmp s1, s0
// 0x1089264: b.pl #0x1089274
// 0x1089268: mov w8, #1
// 0x108926c: strb w8, [x19, #0x211]
// 0x1089270: strb wzr, [x19, #0x106]
// 0x1089274: ldrb w8, [x19, #0x211]
// 0x1089278: cbz w8, #0x1089298
// 0x108927c: ldr x8, [x19, #0x60]
// 0x1089280: cbz x8, #0x108a92c
// 0x1089284: ldrb w8, [x8, #0x2d0]
// 0x1089288: cbnz w8, #0x1089298
// 0x108928c: mov w8, #1
// 0x1089290: strb w8, [x19, #0x106]
// 0x1089294: strb wzr, [x19, #0x211]
// 0x1089298: ldr x0, [x19, #0x88]
// 0x108929c: cbz x0, #0x108a92c
// 0x10892a0: add x8, sp, #0x48
// 0x10892a4: mov w1, wzr
// 0x10892a8: mov x2, xzr
// 0x10892ac: bl #0x1b67df8
// 0x10892b0: ldur q0, [sp, #0x48]
// 0x10892b4: ldur q1, [sp, #0x58]
// 0x10892b8: ldr w8, [sp, #0x68]
// 0x10892bc: add x0, sp, #0x70
// 0x10892c0: mov x1, xzr
// 0x10892c4: stp q0, q1, [sp, #0x70]
// 0x10892c8: str w8, [sp, #0x90]
// 0x10892cc: bl #0x1b67398
// 0x10892d0: adrp x8, #0x832000
// 0x10892d4: ldr s1, [x8, #0x38c]
// 0x10892d8: fcmp s0, s1
// 0x10892dc: b.le #0x1089320
// 0x10892e0: adrp x21, #0x1fab000
// 0x10892e4: ldrb w8, [x21, #0x2c9]
// 0x10892e8: cbnz w8, #0x1089300
// 0x10892ec: adrp x0, #0x1e8c000
// 0x10892f0: ldr x0, [x0, #0x1e8]
// 0x10892f4: bl #0xf7d92c
// 0x10892f8: mov w8, #1
// 0x10892fc: strb w8, [x21, #0x2c9]
// 0x1089300: adrp x8, #0x1e8c000
// 0x1089304: ldr x8, [x8, #0x1e8]
// 0x1089308: ldr x8, [x8]
// 0x108930c: ldr x8, [x8, #0xb8]
// 0x1089310: ldr d0, [x8]
// 0x1089314: ldr s1, [x8, #8]
// 0x1089318: stur d0, [x19, #0xb4]
// 0x108931c: str s1, [x19, #0xbc]
// 0x1089320: ldr x0, [x19, #0x120]
// 0x1089324: cbz x0, #0x108a92c
// 0x1089328: ldrb w21, [x19, #0x106]
// 0x108932c: mov x1, xzr
// 0x1089330: bl #0x1b9d508
// 0x1089334: mov v8.16b, v0.16b
// 0x1089338: mov v9.16b, v1.16b
// 0x108933c: mov v10.16b, v2.16b
// 0x1089340: cbnz w21, #0x1089378
// 0x1089344: ldr x0, [x19, #0x120]
// 0x1089348: cbz x0, #0x108a92c
// 0x108934c: mov x1, xzr
// 0x1089350: bl #0x1b9d8c8
// 0x1089354: ldr x8, [x19, #0x40]
// 0x1089358: cbz x8, #0x108a92c
// 0x108935c: ldr s3, [x8, #0x174]
// 0x1089360: fmul s0, s0, s3
// 0x1089364: fmul s1, s1, s3
// 0x1089368: fmul s2, s2, s3
// 0x108936c: fadd s8, s8, s0
// 0x1089370: fadd s9, s9, s1
// 0x1089374: fadd s10, s10, s2
// 0x1089378: str s8, [x19, #0x134]
// 0x108937c: str s9, [x19, #0x138]
// 0x1089380: str s10, [x19, #0x13c]
// 0x1089384: adrp x23, #0x1e8c000
// 0x1089388: ldr x23, [x23, #0xd8]
// 0x108938c: ldr x21, [x19, #0x58]
// 0x1089390: ldr x0, [x23]
// 0x1089394: ldr w8, [x0, #0xe0]
// 0x1089398: cbnz w8, #0x10893a0
// 0x108939c: bl #0xf7da5c
// 0x10893a0: mov x0, x21
// 0x10893a4: mov x1, xzr
// 0x10893a8: bl #0x1b98274
// 0x10893ac: tbz w0, #0, #0x108940c
// 0x10893b0: ldr x8, [x19, #0x58]
// 0x10893b4: cbz x8, #0x108a92c
// 0x10893b8: ldr s9, [x8, #0x30]
// 0x10893bc: mov x0, xzr
// 0x10893c0: bl #0x1b9ae58
// 0x10893c4: mov x0, xzr
// 0x10893c8: mov v8.16b, v0.16b
// 0x10893cc: bl #0x1b9ad30
// 0x10893d0: adrp x8, #0x832000
// 0x10893d4: ldr s1, [x8, #0x3b8]
// 0x10893d8: fmul s1, s8, s1
// 0x10893dc: fadd s1, s9, s1
// 0x10893e0: fcmp s1, s0
// 0x10893e4: b.le #0x108940c
// 0x10893e8: ldr x0, [x19, #0x120]
// 0x10893ec: cbz x0, #0x108a92c
// 0x10893f0: mov x1, xzr
// 0x10893f4: bl #0x1b9d508
// 0x10893f8: ldr s8, [x19, #0x118]
// 0x10893fc: str s0, [x19, #0x158]
// 0x1089400: str s1, [x19, #0x15c]
// 0x1089404: str s2, [x19, #0x160]
// 0x1089408: b #0x108956c
// 0x108940c: ldr s8, [x19, #0x130]
// 0x1089410: mov x0, xzr
// 0x1089414: bl #0x1b9ad30
// 0x1089418: fmov s1, #0.75000000
// 0x108941c: fadd s1, s8, s1
// 0x1089420: fcmp s1, s0
// 0x1089424: b.le #0x1089434
// 0x1089428: str wzr, [x19, #0x118]
// 0x108942c: fmov s8, wzr
// 0x1089430: b #0x108956c
// 0x1089434: ldr x8, [x19, #0x60]
// 0x1089438: cbz x8, #0x108a92c
// 0x108943c: ldrb w9, [x8, #0x208]
// 0x1089440: cbz w9, #0x1089494
// 0x1089444: ldr x0, [x19, #0x28]
// 0x1089448: cbz x0, #0x108a92c
// 0x108944c: mov x1, xzr
// 0x1089450: bl #0x1b94c14
// 0x1089454: cbz x0, #0x108a92c
// 0x1089458: mov x1, xzr
// 0x108945c: bl #0x1b9d400
// 0x1089460: ldr x8, [x23]
// 0x1089464: mov x21, x0
// 0x1089468: ldr w9, [x8, #0xe0]
// 0x108946c: cbnz w9, #0x1089478
// 0x1089470: mov x0, x8
// 0x1089474: bl #0xf7da5c
// 0x1089478: mov x0, x21
// 0x108947c: mov x1, xzr
// 0x1089480: mov x2, xzr
// 0x1089484: bl #0x1b9568c
// 0x1089488: tbnz w0, #0, #0x1089500
// 0x108948c: ldr x8, [x19, #0x60]
// 0x1089490: cbz x8, #0x108a92c
// 0x1089494: ldrb w8, [x8, #0x208]
// 0x1089498: cbnz w8, #0x1089534
// 0x108949c: ldr x0, [x19, #0x28]
// 0x10894a0: cbz x0, #0x108a92c
// 0x10894a4: mov x1, xzr
// 0x10894a8: bl #0x1b94c14
// 0x10894ac: cbz x0, #0x108a92c
// 0x10894b0: mov x1, xzr
// 0x10894b4: bl #0x1b9d400
// 0x10894b8: ldr x8, [x19, #0x40]
// 0x10894bc: cbz x8, #0x108a92c
// 0x10894c0: mov x21, x0
// 0x10894c4: ldr x0, [x8, #0x48]
// 0x10894c8: cbz x0, #0x108a92c
// 0x10894cc: mov x1, xzr
// 0x10894d0: bl #0x1b94c14
// 0x10894d4: ldr x8, [x23]
// 0x10894d8: mov x22, x0
// 0x10894dc: ldr w9, [x8, #0xe0]
// 0x10894e0: cbnz w9, #0x10894ec
// 0x10894e4: mov x0, x8
// 0x10894e8: bl #0xf7da5c
// 0x10894ec: mov x0, x21
// 0x10894f0: mov x1, x22
// 0x10894f4: mov x2, xzr
// 0x10894f8: bl #0x1b9568c
// 0x10894fc: tbz w0, #0, #0x1089534
// 0x1089500: ldr s8, [x19, #0x118]
// 0x1089504: ldr s9, [x19, #0x114]
// 0x1089508: mov x0, xzr
// 0x108950c: bl #0x1b89b60
// 0x1089510: fsub s1, s9, s8
// 0x1089514: fneg s3, s0
// 0x1089518: fcmp s1, #0.0
// 0x108951c: fabd s2, s9, s8
// 0x1089520: fcsel s1, s0, s3, ge
// 0x1089524: fadd s1, s8, s1
// 0x1089528: fcmp s2, s0
// 0x108952c: fcsel s8, s1, s9, hi
// 0x1089530: b #0x1089568
// 0x1089534: ldr s8, [x19, #0x118]
// 0x1089538: mov x0, xzr
// 0x108953c: bl #0x1b89b60
// 0x1089540: adrp x8, #0x832000
// 0x1089544: ldr s1, [x8, #0x4e0]
// 0x1089548: fneg s2, s0
// 0x108954c: fsub s3, s1, s8
// 0x1089550: fcmp s3, #0.0
// 0x1089554: fabd s4, s1, s8
// 0x1089558: fcsel s2, s0, s2, ge
// 0x108955c: fadd s2, s8, s2
// 0x1089560: fcmp s4, s0
// 0x1089564: fcsel s8, s2, s1, hi
// 0x1089568: str s8, [x19, #0x118]
// 0x108956c: ldr s9, [x19, #0x158]
// 0x1089570: ldr s10, [x19, #0x15c]
// 0x1089574: ldr s11, [x19, #0x160]
// 0x1089578: ldr s12, [x19, #0x134]
// 0x108957c: ldr s13, [x19, #0x138]
// 0x1089580: ldr s14, [x19, #0x13c]
// 0x1089584: mov x0, xzr
// 0x1089588: add x21, x19, #0x108
// 0x108958c: bl #0x1b9ae30
// 0x1089590: mov w8, #0x7f800000
// 0x1089594: str s0, [sp]
// 0x1089598: fmov s7, w8
// 0x108959c: mov v0.16b, v9.16b
// 0x10895a0: mov v1.16b, v10.16b
// 0x10895a4: mov v2.16b, v11.16b
// 0x10895a8: mov v3.16b, v12.16b
// 0x10895ac: mov v4.16b, v13.16b
// 0x10895b0: mov v5.16b, v14.16b
// 0x10895b4: mov x0, x21
// 0x10895b8: mov v6.16b, v8.16b
// 0x10895bc: mov x1, xzr
// 0x10895c0: bl #0x1b89b88
// 0x10895c4: ldr x8, [x19, #0x40]
// 0x10895c8: str s0, [x19, #0x158]
// 0x10895cc: str s1, [x19, #0x15c]
// 0x10895d0: str s2, [x19, #0x160]
// 0x10895d4: cbz x8, #0x108a92c
// 0x10895d8: ldr s8, [x19, #0x224]
// 0x10895dc: ldr s9, [x8, #0x2cc]
// 0x10895e0: ldr s10, [x8, #0x2ec]
// 0x10895e4: mov x0, xzr
// 0x10895e8: add x21, x19, #0x220
// 0x10895ec: bl #0x1b9ae30
// 0x10895f0: mov w8, #0x7f800000
// 0x10895f4: mov v4.16b, v0.16b
// 0x10895f8: fmov s3, w8
// 0x10895fc: mov v0.16b, v8.16b
// 0x1089600: mov v1.16b, v9.16b
// 0x1089604: mov x0, x21
// 0x1089608: mov v2.16b, v10.16b
// 0x108960c: mov x1, xzr
// 0x1089610: bl #0x1b8c860
// 0x1089614: ldr x8, [x19, #0x40]
// 0x1089618: str s0, [x19, #0x224]
// 0x108961c: cbz x8, #0x108a92c
// 0x1089620: ldrb w9, [x8, #0x2d0]
// 0x1089624: cbz w9, #0x108963c
// 0x1089628: ldrb w9, [x8, #0x2e8]
// 0x108962c: cbz w9, #0x108963c
// 0x1089630: ldr s0, [x19, #0x180]
// 0x1089634: fmov s1, #0.50000000
// 0x1089638: b #0x1089650
// 0x108963c: ldrb w9, [x8, #0x2dc]
// 0x1089640: cbz w9, #0x108a03c
// 0x1089644: adrp x8, #0x832000
// 0x1089648: ldr s0, [x19, #0x180]
// 0x108964c: ldr s1, [x8, #0x47c]
// 0x1089650: fmul s8, s0, s1
// 0x1089654: ldr s9, [x19, #0x22c]
// 0x1089658: mov x0, xzr
// 0x108965c: str s8, [x19, #0x228]
// 0x1089660: bl #0x1b89b60
// 0x1089664: fmov s1, #4.00000000
// 0x1089668: fmov s2, #1.00000000
// 0x108966c: fmul s0, s0, s1
// 0x1089670: fmov s3, wzr
// 0x1089674: ldr x0, [x19, #0x120]
// 0x1089678: fmin s1, s0, s2
// 0x108967c: fcmp s0, #0.0
// 0x1089680: fcsel s0, s1, s3, pl
// 0x1089684: fsub s1, s8, s9
// 0x1089688: fmul s0, s1, s0
// 0x108968c: fadd s0, s9, s0
// 0x1089690: str s0, [x19, #0x22c]
// 0x1089694: cbz x0, #0x108a92c
// 0x1089698: ldr d8, [x19, #0x158]
// 0x108969c: ldrb w8, [x19, #0x106]
// 0x10896a0: ldr s9, [x19, #0x160]
// 0x10896a4: mov x1, xzr
// 0x10896a8: cbz w8, #0x10896cc
// 0x10896ac: bl #0x1b9d940
// 0x10896b0: ldr s3, [x19, #0x22c]
// 0x10896b4: mov v0.s[1], v1.s[0]
// 0x10896b8: fmul v0.2s, v0.2s, v3.s[0]
// 0x10896bc: fmul s2, s2, s3
// 0x10896c0: fadd v1.2s, v8.2s, v0.2s
// 0x10896c4: fadd s0, s9, s2
// 0x10896c8: b #0x1089724
// 0x10896cc: bl #0x1b9d8c8
// 0x10896d0: ldr x8, [x19, #0x78]
// 0x10896d4: cbz x8, #0x108a92c
// 0x10896d8: ldr x9, [x19, #0x48]
// 0x10896dc: cbz x9, #0x108a92c
// 0x10896e0: ldr s3, [x9, #0x1b8]
// 0x10896e4: ldp s4, s5, [x8, #0x20]
// 0x10896e8: ldr s6, [x9, #0x1bc]
// 0x10896ec: mov v0.s[1], v1.s[0]
// 0x10896f0: fmul s1, s4, s3
// 0x10896f4: ldr s4, [x19, #0x224]
// 0x10896f8: fmul s3, s5, s6
// 0x10896fc: fmul v0.2s, v0.2s, v1.s[0]
// 0x1089700: fmul s1, s2, s1
// 0x1089704: movi d2, #0000000000000000
// 0x1089708: fadd s3, s4, s3
// 0x108970c: fmov s4, wzr
// 0x1089710: fadd v0.2s, v8.2s, v0.2s
// 0x1089714: fadd s5, s9, s1
// 0x1089718: mov v2.s[1], v3.s[0]
// 0x108971c: fadd v1.2s, v0.2s, v2.2s
// 0x1089720: fadd s0, s5, s4
// 0x1089724: add x22, x19, #0x14c
// 0x1089728: str d1, [x22]
// 0x108972c: ldrb w9, [x19, #0x106]
// 0x1089730: ldrb w8, [x19, #0x19d]
// 0x1089734: str s0, [x19, #0x154]
// 0x1089738: cbz w9, #0x1089cf8
// 0x108973c: cbnz w8, #0x1089820
// 0x1089740: ldr x21, [x19, #0x50]
// 0x1089744: mov x0, xzr
// 0x1089748: bl #0x1b9ad30
// 0x108974c: cbz x21, #0x108a92c
// 0x1089750: str s0, [x21, #0x84]
// 0x1089754: ldr x0, [x19, #0x128]
// 0x1089758: cbz x0, #0x108a92c
// 0x108975c: ldr x21, [x19, #0x50]
// 0x1089760: mov x1, xzr
// 0x1089764: bl #0x1b9d400
// 0x1089768: cbz x0, #0x108a92c
// 0x108976c: mov x1, xzr
// 0x1089770: bl #0x1b92154
// 0x1089774: cbz x0, #0x108a92c
// 0x1089778: mov x1, xzr
// 0x108977c: bl #0x1b9d6c8
// 0x1089780: cbz x21, #0x108a92c
// 0x1089784: str s1, [x21, #0x50]
// 0x1089788: ldr x0, [x19, #0x128]
// 0x108978c: cbz x0, #0x108a92c
// 0x1089790: mov x1, xzr
// 0x1089794: bl #0x1b9d400
// 0x1089798: cbz x0, #0x108a92c
// 0x108979c: mov x1, xzr
// 0x10897a0: bl #0x1b92154
// 0x10897a4: cbz x0, #0x108a92c
// 0x10897a8: mov x1, xzr
// 0x10897ac: bl #0x1b9d6f0
// 0x10897b0: ldr x8, [x19, #0x40]
// 0x10897b4: str s0, [x19, #0x200]
// 0x10897b8: str s1, [x19, #0x204]
// 0x10897bc: str s2, [x19, #0x208]
// 0x10897c0: str s3, [x19, #0x20c]
// 0x10897c4: str wzr, [x19, #0x1c4]
// 0x10897c8: cbz x8, #0x108a92c
// 0x10897cc: ldrb w8, [x8, #0x2b1]
// 0x10897d0: adrp x9, #0x832000
// 0x10897d4: add x9, x9, #0xc8
// 0x10897d8: adrp x10, #0x832000
// 0x10897dc: cmp w8, #0
// 0x10897e0: cset w8, eq
// 0x10897e4: ldr s0, [x19, #0x218]
// 0x10897e8: ldr s1, [x19, #0x188]
// 0x10897ec: ldr s2, [x10, #0x440]
// 0x10897f0: ldr s3, [x9, w8, uxtw #2]
// 0x10897f4: ldr x0, [x19, #0x70]
// 0x10897f8: fmul s1, s1, s2
// 0x10897fc: fadd s0, s0, s3
// 0x1089800: str s0, [x19, #0x1bc]
// 0x1089804: str s1, [x19, #0x1a8]
// 0x1089808: cbz x0, #0x108a92c
// 0x108980c: mov w1, wzr
// 0x1089810: mov x2, xzr
// 0x1089814: bl #0x1b91660
// 0x1089818: mov w8, #1
// 0x108981c: strb w8, [x19, #0x19d]
// 0x1089820: ldr x0, [x19, #0x30]
// 0x1089824: cbz x0, #0x108a92c
// 0x1089828: mov x1, xzr
// 0x108982c: bl #0x1b94c14
// 0x1089830: ldr x8, [x19, #0x128]
// 0x1089834: cbz x8, #0x108a92c
// 0x1089838: mov x21, x0
// 0x108983c: mov x0, x8
// 0x1089840: mov x1, xzr
// 0x1089844: bl #0x1b9d6f0
// 0x1089848: cbz x21, #0x108a92c
// 0x108984c: mov x0, x21
// 0x1089850: mov x1, xzr
// 0x1089854: bl #0x1b9d774
// 0x1089858: ldr x8, [x19, #0x50]
// 0x108985c: cbz x8, #0x108a92c
// 0x1089860: mov w9, #1
// 0x1089864: ldp s8, s0, [x8, #0x50]
// 0x1089868: ldr s1, [x8, #0xa4]
// 0x108986c: strb w9, [x8, #0xaa]
// 0x1089870: ldr s9, [x19, #0x194]
// 0x1089874: ldr s10, [x19, #0x198]
// 0x1089878: mov w8, #0x43b40000
// 0x108987c: fadd s0, s0, s1
// 0x1089880: fmov s1, w8
// 0x1089884: bl #0x1db0cb0
// 0x1089888: mov w8, #-0x3c4c0000
// 0x108988c: fmov s1, w8
// 0x1089890: fcmp s0, s1
// 0x1089894: b.lt #0x10898d8
// 0x1089898: mov w8, #0x43b40000
// 0x108989c: fmov s1, w8
// 0x10898a0: fcmp s0, s1
// 0x10898a4: b.hi #0x10898d8
// 0x10898a8: mov w8, #0x43b40000
// 0x10898ac: mov w9, #-0x3c4c0000
// 0x10898b0: fmov s1, w8
// 0x10898b4: fmov s3, w9
// 0x10898b8: fadd s2, s0, s1
// 0x10898bc: fcmp s0, s3
// 0x10898c0: fcsel s0, s2, s0, mi
// 0x10898c4: fcmp s0, s1
// 0x10898c8: b.le #0x10898d8
// 0x10898cc: mov w8, #-0x3c4c0000
// 0x10898d0: fmov s1, w8
// 0x10898d4: fadd s0, s0, s1
// 0x10898d8: fcmp s0, s10
// 0x10898dc: fcsel s1, s10, s0, gt
// 0x10898e0: fcmp s0, s9
// 0x10898e4: fcsel s0, s1, s9, pl
// 0x10898e8: mov w8, #0x43b40000
// 0x10898ec: str s0, [x19, #0x18c]
// 0x10898f0: fmov s1, w8
// 0x10898f4: mov v0.16b, v8.16b
// 0x10898f8: bl #0x1db0cb0
// 0x10898fc: mov w8, #-0x3c4c0000
// 0x1089900: fmov s1, w8
// 0x1089904: fcmp s0, s1
// 0x1089908: b.lt #0x108994c
// 0x108990c: mov w8, #0x43b40000
// 0x1089910: fmov s1, w8
// 0x1089914: fcmp s0, s1
// 0x1089918: b.hi #0x108994c
// 0x108991c: mov w8, #0x43b40000
// 0x1089920: mov w9, #-0x3c4c0000
// 0x1089924: fmov s1, w8
// 0x1089928: fmov s3, w9
// 0x108992c: fadd s2, s0, s1
// 0x1089930: fcmp s0, s3
// 0x1089934: fcsel s0, s2, s0, mi
// 0x1089938: fcmp s0, s1
// 0x108993c: b.le #0x108994c
// 0x1089940: mov w8, #-0x3c4c0000
// 0x1089944: fmov s1, w8
// 0x1089948: fadd s0, s0, s1
// 0x108994c: mov w8, #0x43b40000
// 0x1089950: mov w9, #-0x3c4c0000
// 0x1089954: ldr s8, [x19, #0x1bc]
// 0x1089958: ldr s9, [x19, #0x1a8]
// 0x108995c: fmov s1, w8
// 0x1089960: fmov s2, w9
// 0x1089964: fmin s1, s0, s1
// 0x1089968: fcmp s0, s2
// 0x108996c: fcsel s0, s1, s2, pl
// 0x1089970: mov x0, xzr
// 0x1089974: str s0, [x19, #0x190]
// 0x1089978: bl #0x1b9ae30
// 0x108997c: fmov s1, #9.00000000
// 0x1089980: fmov s2, #1.00000000
// 0x1089984: fmul s0, s0, s1
// 0x1089988: fmov s3, wzr
// 0x108998c: ldr x0, [x19, #0x120]
// 0x1089990: fmin s1, s0, s2
// 0x1089994: fcmp s0, #0.0
// 0x1089998: fcsel s0, s1, s3, pl
// 0x108999c: fsub s1, s9, s8
// 0x10899a0: fmul s0, s1, s0
// 0x10899a4: fadd s0, s8, s0
// 0x10899a8: str s0, [x19, #0x1bc]
// 0x10899ac: cbz x0, #0x108a92c
// 0x10899b0: ldr s8, [x19, #0x154]
// 0x10899b4: ldr d11, [x22]
// 0x10899b8: mov x1, xzr
// 0x10899bc: bl #0x1b9d940
// 0x10899c0: ldr s3, [x19, #0x180]
// 0x10899c4: adrp x8, #0x832000
// 0x10899c8: mov v0.s[1], v1.s[0]
// 0x10899cc: ldr s1, [x19, #0x18c]
// 0x10899d0: fmul v0.2s, v0.2s, v3.s[0]
// 0x10899d4: fmul s2, s2, s3
// 0x10899d8: ldr s3, [x8, #0x394]
// 0x10899dc: fmov v4.2s, #1.25000000
// 0x10899e0: fmul v4.2s, v0.2s, v4.2s
// 0x10899e4: adrp x8, #0x832000
// 0x10899e8: fmul s0, s1, s3
// 0x10899ec: ldr s1, [x19, #0x190]
// 0x10899f0: fadd v3.2s, v11.2s, v4.2s
// 0x10899f4: ldr s4, [x8, #0x3e4]
// 0x10899f8: fmov s5, #1.25000000
// 0x10899fc: ldr s6, [x19, #0x200]
// 0x1089a00: ldr s9, [x19, #0x204]
// 0x1089a04: fmul s2, s2, s5
// 0x1089a08: ldr s10, [x19, #0x208]
// 0x1089a0c: ldr s11, [x19, #0x20c]
// 0x1089a10: fadd s2, s8, s2
// 0x1089a14: str s2, [x19, #0x148]
// 0x1089a18: fmul s1, s1, s4
// 0x1089a1c: fmov s2, wzr
// 0x1089a20: mov x0, xzr
// 0x1089a24: str s6, [sp, #0x44]
// 0x1089a28: str d3, [x19, #0x140]
// 0x1089a2c: bl #0x1b8b12c
// 0x1089a30: mov x0, xzr
// 0x1089a34: mov v12.16b, v0.16b
// 0x1089a38: mov v13.16b, v1.16b
// 0x1089a3c: mov v14.16b, v2.16b
// 0x1089a40: mov v15.16b, v3.16b
// 0x1089a44: bl #0x1b9ae30
// 0x1089a48: mov x0, xzr
// 0x1089a4c: mov v8.16b, v0.16b
// 0x1089a50: bl #0x1b9ae58
// 0x1089a54: adrp x8, #0x832000
// 0x1089a58: ldr s1, [x8, #0x330]
// 0x1089a5c: mov w8, #0x42700000
// 0x1089a60: fmov s2, w8
// 0x1089a64: mov v3.16b, v11.16b
// 0x1089a68: fmul s1, s8, s1
// 0x1089a6c: fmul s1, s1, s2
// 0x1089a70: fdiv s0, s1, s0
// 0x1089a74: str s0, [sp]
// 0x1089a78: ldr s0, [sp, #0x44]
// 0x1089a7c: mov v1.16b, v9.16b
// 0x1089a80: mov v2.16b, v10.16b
// 0x1089a84: mov v4.16b, v12.16b
// 0x1089a88: mov v5.16b, v13.16b
// 0x1089a8c: mov v6.16b, v14.16b
// 0x1089a90: mov v7.16b, v15.16b
// 0x1089a94: mov x0, xzr
// 0x1089a98: bl #0x1b8af84
// 0x1089a9c: mov v8.16b, v0.16b
// 0x1089aa0: ldr s0, [x19, #0x1bc]
// 0x1089aa4: str s8, [x19, #0x200]
// 0x1089aa8: str s1, [x19, #0x204]
// 0x1089aac: str s2, [x19, #0x208]
// 0x1089ab0: fcmp s0, #0.0
// 0x1089ab4: str s3, [x19, #0x20c]
// 0x1089ab8: b.eq #0x1089b78
// 0x1089abc: adrp x21, #0x1fab000
// 0x1089ac0: ldrb w8, [x21, #0x3e3]
// 0x1089ac4: mov v9.16b, v1.16b
// 0x1089ac8: mov v10.16b, v2.16b
// 0x1089acc: mov v11.16b, v3.16b
// 0x1089ad0: cbnz w8, #0x1089ae8
// 0x1089ad4: adrp x0, #0x1e8c000
// 0x1089ad8: ldr x0, [x0, #0x1e8]
// 0x1089adc: bl #0xf7d92c
// 0x1089ae0: mov w8, #1
// 0x1089ae4: strb w8, [x21, #0x3e3]
// 0x1089ae8: adrp x21, #0x1e8c000
// 0x1089aec: ldr x21, [x21, #0x1e8]
// 0x1089af0: adrp x24, #0x1fab000
// 0x1089af4: ldrb w9, [x24, #0x3e1]
// 0x1089af8: ldr x8, [x21]
// 0x1089afc: ldr x8, [x8, #0xb8]
// 0x1089b00: ldr d0, [x8, #0x48]
// 0x1089b04: ldr s1, [x8, #0x50]
// 0x1089b08: fneg v13.2s, v0.2s
// 0x1089b0c: fneg s12, s1
// 0x1089b10: cbnz w9, #0x1089b2c
// 0x1089b14: mov x0, x21
// 0x1089b18: bl #0xf7d92c
// 0x1089b1c: ldr x8, [x21]
// 0x1089b20: mov w9, #1
// 0x1089b24: strb w9, [x24, #0x3e1]
// 0x1089b28: ldr x8, [x8, #0xb8]
// 0x1089b2c: ldr s0, [x19, #0x17c]
// 0x1089b30: ldr s1, [x19, #0x1bc]
// 0x1089b34: ldur d2, [x8, #0x3c]
// 0x1089b38: ldr s3, [x8, #0x44]
// 0x1089b3c: mov x0, xzr
// 0x1089b40: fdiv s0, s0, s1
// 0x1089b44: fmul v1.2s, v2.2s, v0.s[0]
// 0x1089b48: fmul s0, s3, s0
// 0x1089b4c: fsub v4.2s, v13.2s, v1.2s
// 0x1089b50: fsub s6, s12, s0
// 0x1089b54: mov s5, v4.s[1]
// 0x1089b58: mov v0.16b, v8.16b
// 0x1089b5c: mov v1.16b, v9.16b
// 0x1089b60: mov v2.16b, v10.16b
// 0x1089b64: mov v3.16b, v11.16b
// 0x1089b68: bl #0x1b8b504
// 0x1089b6c: str s0, [x19, #0x1f4]
// 0x1089b70: str s1, [x19, #0x1f8]
// 0x1089b74: str s2, [x19, #0x1fc]
// 0x1089b78: ldrb w8, [x19, #0x210]
// 0x1089b7c: cbz w8, #0x1089eec
// 0x1089b80: ldr s8, [x19, #0x17c]
// 0x1089b84: mov x0, xzr
// 0x1089b88: bl #0x1b9ae30
// 0x1089b8c: fmov s9, #6.00000000
// 0x1089b90: fmov s10, #1.00000000
// 0x1089b94: fmul s0, s0, s9
// 0x1089b98: fmov s11, wzr
// 0x1089b9c: fmin s2, s0, s10
// 0x1089ba0: fcmp s0, #0.0
// 0x1089ba4: ldr s12, [x19, #0x180]
// 0x1089ba8: fsub s1, s11, s8
// 0x1089bac: fcsel s0, s2, s11, pl
// 0x1089bb0: ldr s13, [x19, #0x214]
// 0x1089bb4: fmul s0, s1, s0
// 0x1089bb8: fadd s0, s8, s0
// 0x1089bbc: mov x0, xzr
// 0x1089bc0: str s0, [x19, #0x17c]
// 0x1089bc4: bl #0x1b9ae30
// 0x1089bc8: fmul s0, s0, s9
// 0x1089bcc: ldr s2, [x19, #0x218]
// 0x1089bd0: fmin s3, s0, s10
// 0x1089bd4: fcmp s0, #0.0
// 0x1089bd8: fsub s1, s13, s12
// 0x1089bdc: ldr s8, [x19, #0x1c4]
// 0x1089be0: fcsel s0, s3, s11, pl
// 0x1089be4: fmul s0, s1, s0
// 0x1089be8: fadd s0, s12, s0
// 0x1089bec: mov x0, xzr
// 0x1089bf0: str s2, [x19, #0x1a8]
// 0x1089bf4: str s0, [x19, #0x180]
// 0x1089bf8: add x21, x19, #0x21c
// 0x1089bfc: bl #0x1b89b60
// 0x1089c00: adrp x8, #0x832000
// 0x1089c04: ldr s2, [x8, #0x520]
// 0x1089c08: mov w8, #0x7f800000
// 0x1089c0c: mov v4.16b, v0.16b
// 0x1089c10: fmov s1, wzr
// 0x1089c14: fmov s3, w8
// 0x1089c18: mov v0.16b, v8.16b
// 0x1089c1c: mov x0, x21
// 0x1089c20: mov x1, xzr
// 0x1089c24: bl #0x1b8c860
// 0x1089c28: adrp x8, #0x832000
// 0x1089c2c: ldr s1, [x19, #0x218]
// 0x1089c30: ldr s2, [x8, #0x4f4]
// 0x1089c34: ldr s3, [x19, #0x1bc]
// 0x1089c38: str s0, [x19, #0x1c4]
// 0x1089c3c: fadd s1, s1, s2
// 0x1089c40: fcmp s3, s1
// 0x1089c44: b.pl #0x108a0f0
// 0x1089c48: str wzr, [x19, #0x1c4]
// 0x1089c4c: str xzr, [x22, #0x70]
// 0x1089c50: str wzr, [x19, #0x1a8]
// 0x1089c54: ldr x0, [x23]
// 0x1089c58: ldr x21, [x19, #0xa8]
// 0x1089c5c: ldr w8, [x0, #0xe0]
// 0x1089c60: cbnz w8, #0x1089c68
// 0x1089c64: bl #0xf7da5c
// 0x1089c68: mov x0, x21
// 0x1089c6c: mov x1, xzr
// 0x1089c70: bl #0x1b98274
// 0x1089c74: tbz w0, #0, #0x1089c8c
// 0x1089c78: ldr x21, [x19, #0xa8]
// 0x1089c7c: mov x0, xzr
// 0x1089c80: bl #0x1b9ad30
// 0x1089c84: cbz x21, #0x108a92c
// 0x1089c88: str s0, [x21, #0x310]
// 0x1089c8c: ldr x0, [x19, #0x120]
// 0x1089c90: cbz x0, #0x108a92c
// 0x1089c94: ldr d8, [x22]
// 0x1089c98: ldr s9, [x19, #0x154]
// 0x1089c9c: mov x1, xzr
// 0x1089ca0: bl #0x1b9d940
// 0x1089ca4: ldr x8, [x19, #0x40]
// 0x1089ca8: cbz x8, #0x108a92c
// 0x1089cac: ldr x0, [x8, #0x238]
// 0x1089cb0: cbz x0, #0x108a92c
// 0x1089cb4: ldr s3, [x19, #0x180]
// 0x1089cb8: mov v0.s[1], v1.s[0]
// 0x1089cbc: mov x1, xzr
// 0x1089cc0: fmul v10.2s, v0.2s, v3.s[0]
// 0x1089cc4: fmul s11, s2, s3
// 0x1089cc8: bl #0x1bcfdf0
// 0x1089ccc: fmov s1, #0.50000000
// 0x1089cd0: fmul s0, s0, s1
// 0x1089cd4: fmul v1.2s, v10.2s, v0.s[0]
// 0x1089cd8: fmul s0, s11, s0
// 0x1089cdc: fadd v1.2s, v8.2s, v1.2s
// 0x1089ce0: fadd s0, s9, s0
// 0x1089ce4: strb wzr, [x19, #0x106]
// 0x1089ce8: str d1, [x19, #0x140]
// 0x1089cec: str s0, [x19, #0x148]
// 0x1089cf0: strb wzr, [x19, #0x210]
// 0x1089cf4: b #0x108a0f0
// 0x1089cf8: cbz w8, #0x1089e70
// 0x1089cfc: ldr x20, [x19, #0x50]
// 0x1089d00: mov x0, xzr
// 0x1089d04: bl #0x1b9ad30
// 0x1089d08: cbz x20, #0x108a92c
// 0x1089d0c: str s0, [x20, #0x84]
// 0x1089d10: ldr x0, [x19, #0x50]
// 0x1089d14: cbz x0, #0x108a92c
// 0x1089d18: mov w1, wzr
// 0x1089d1c: mov x2, xzr
// 0x1089d20: bl #0x1b91660
// 0x1089d24: ldr x0, [x19, #0x128]
// 0x1089d28: cbz x0, #0x108a92c
// 0x1089d2c: mov x1, xzr
// 0x1089d30: bl #0x1b9d400
// 0x1089d34: cbz x0, #0x108a92c
// 0x1089d38: mov x1, xzr
// 0x1089d3c: bl #0x1b92154
// 0x1089d40: adrp x8, #0x832000
// 0x1089d44: adrp x9, #0x832000
// 0x1089d48: ldr s0, [x19, #0x18c]
// 0x1089d4c: ldr s1, [x19, #0x190]
// 0x1089d50: ldr s2, [x8, #0x394]
// 0x1089d54: ldr s3, [x9, #0x3e4]
// 0x1089d58: mov x20, x0
// 0x1089d5c: mov x0, xzr
// 0x1089d60: fmul s0, s0, s2
// 0x1089d64: fmul s1, s1, s3
// 0x1089d68: fmov s2, wzr
// 0x1089d6c: bl #0x1b8b12c
// 0x1089d70: cbz x20, #0x108a92c
// 0x1089d74: mov x0, x20
// 0x1089d78: mov x1, xzr
// 0x1089d7c: bl #0x1b9d774
// 0x1089d80: ldr x20, [x19, #0x128]
// 0x1089d84: cbz x20, #0x108a92c
// 0x1089d88: mov x0, x20
// 0x1089d8c: mov x1, xzr
// 0x1089d90: bl #0x1b9d400
// 0x1089d94: cbz x0, #0x108a92c
// 0x1089d98: mov x1, xzr
// 0x1089d9c: bl #0x1b92154
// 0x1089da0: cbz x0, #0x108a92c
// 0x1089da4: mov x1, xzr
// 0x1089da8: bl #0x1b9d6f0
// 0x1089dac: mov x0, x20
// 0x1089db0: mov x1, xzr
// 0x1089db4: bl #0x1b9d774
// 0x1089db8: ldr x0, [x19, #0x50]
// 0x1089dbc: cbz x0, #0x108a92c
// 0x1089dc0: mov w1, #1
// 0x1089dc4: mov x2, xzr
// 0x1089dc8: bl #0x1b91660
// 0x1089dcc: ldr x20, [x19, #0x50]
// 0x1089dd0: cbz x20, #0x108a92c
// 0x1089dd4: ldr d0, [x22, #0x40]
// 0x1089dd8: fmov s1, wzr
// 0x1089ddc: fmov s2, wzr
// 0x1089de0: mov x0, xzr
// 0x1089de4: rev64 v0.2s, v0.2s
// 0x1089de8: str d0, [x20, #0x50]
// 0x1089dec: fmov s0, wzr
// 0x1089df0: str wzr, [x20, #0x7c]
// 0x1089df4: str xzr, [x20, #0xa0]
// 0x1089df8: bl #0x1b8b12c
// 0x1089dfc: stp s0, s1, [x20, #0x58]
// 0x1089e00: stp s2, s3, [x20, #0x60]
// 0x1089e04: ldr x20, [x19, #0x50]
// 0x1089e08: fmov s0, wzr
// 0x1089e0c: fmov s1, wzr
// 0x1089e10: fmov s2, wzr
// 0x1089e14: mov x0, xzr
// 0x1089e18: bl #0x1b8b12c
// 0x1089e1c: cbz x20, #0x108a92c
// 0x1089e20: stp s0, s1, [x20, #0x68]
// 0x1089e24: stp s2, s3, [x20, #0x70]
// 0x1089e28: ldr x20, [x19, #0x50]
// 0x1089e2c: fmov s0, wzr
// 0x1089e30: fmov s1, wzr
// 0x1089e34: fmov s2, wzr
// 0x1089e38: mov x0, xzr
// 0x1089e3c: bl #0x1b8b12c
// 0x1089e40: cbz x20, #0x108a92c
// 0x1089e44: stp s0, s1, [x20, #0x88]
// 0x1089e48: stp s2, s3, [x20, #0x90]
// 0x1089e4c: ldr x0, [x19, #0x70]
// 0x1089e50: cbz x0, #0x108a92c
// 0x1089e54: mov w1, #1
// 0x1089e58: mov x2, xzr
// 0x1089e5c: bl #0x1b91660
// 0x1089e60: ldr x8, [x19, #0x70]
// 0x1089e64: cbz x8, #0x108a92c
// 0x1089e68: str xzr, [x8, #0xa8]
// 0x1089e6c: strb wzr, [x19, #0x19d]
// 0x1089e70: ldr x0, [x19, #0x128]
// 0x1089e74: cbz x0, #0x108a92c
// 0x1089e78: mov x1, xzr
// 0x1089e7c: bl #0x1b9d400
// 0x1089e80: cbz x0, #0x108a92c
// 0x1089e84: mov x1, xzr
// 0x1089e88: bl #0x1b92154
// 0x1089e8c: cbz x0, #0x108a92c
// 0x1089e90: ldr s2, [x19, #0x154]
// 0x1089e94: ldr s1, [x19, #0x150]
// 0x1089e98: ldr s0, [x19, #0x14c]
// 0x1089e9c: mov x1, xzr
// 0x1089ea0: bl #0x1b9d5a8
// 0x1089ea4: ldr x0, [x19, #0x128]
// 0x1089ea8: cbz x0, #0x108a92c
// 0x1089eac: ldr s2, [x19, #0x154]
// 0x1089eb0: ldr s1, [x19, #0x150]
// 0x1089eb4: ldr s0, [x19, #0x14c]
// 0x1089eb8: mov x1, xzr
// 0x1089ebc: bl #0x1b9d5a8
// 0x1089ec0: ldr x8, [x19, #0x50]
// 0x1089ec4: cbz x8, #0x108a92c
// 0x1089ec8: mov x0, xzr
// 0x1089ecc: strb wzr, [x8, #0xaa]
// 0x1089ed0: bl #0x1b9ad58
// 0x1089ed4: fmov s1, #1.00000000
// 0x1089ed8: fcmp s0, s1
// 0x1089edc: b.pl #0x108a068
// 0x1089ee0: mov w8, #0x42000000
// 0x1089ee4: fmov s0, w8
// 0x1089ee8: b #0x108a424
// 0x1089eec: ldr s0, [x19, #0x140]
// 0x1089ef0: ldr s1, [x19, #0x144]
// 0x1089ef4: ldr s2, [x19, #0x148]
// 0x1089ef8: ldr s3, [x19, #0x1f4]
// 0x1089efc: ldr s4, [x19, #0x1f8]
// 0x1089f00: ldr s5, [x19, #0x1fc]
// 0x1089f04: mov x0, x19
// 0x1089f08: bl #0x108a9b8
// 0x1089f0c: ldr s9, [x19, #0x1c4]
// 0x1089f10: mov x0, xzr
// 0x1089f14: mov v8.16b, v0.16b
// 0x1089f18: str s0, [x19, #0x1c0]
// 0x1089f1c: add x21, x19, #0x21c
// 0x1089f20: bl #0x1b89b60
// 0x1089f24: adrp x8, #0x832000
// 0x1089f28: ldr s2, [x8, #0x2f8]
// 0x1089f2c: mov w8, #0x7f800000
// 0x1089f30: mov v4.16b, v0.16b
// 0x1089f34: fmov s3, w8
// 0x1089f38: mov v0.16b, v9.16b
// 0x1089f3c: mov v1.16b, v8.16b
// 0x1089f40: mov x0, x21
// 0x1089f44: mov x1, xzr
// 0x1089f48: bl #0x1b8c860
// 0x1089f4c: fmov s1, #0.50000000
// 0x1089f50: ldr s9, [x19, #0x17c]
// 0x1089f54: fadd s1, s8, s1
// 0x1089f58: ldr s8, [x19, #0x174]
// 0x1089f5c: fcmp s1, s0
// 0x1089f60: fcsel s0, s1, s0, mi
// 0x1089f64: mov x0, xzr
// 0x1089f68: str s0, [x19, #0x1c4]
// 0x1089f6c: bl #0x1b9ae30
// 0x1089f70: fmov s10, #6.00000000
// 0x1089f74: fmov s11, #1.00000000
// 0x1089f78: fmul s0, s0, s10
// 0x1089f7c: fmov s12, wzr
// 0x1089f80: fmin s2, s0, s11
// 0x1089f84: fcmp s0, #0.0
// 0x1089f88: fsub s1, s8, s9
// 0x1089f8c: ldr s8, [x19, #0x180]
// 0x1089f90: fcsel s0, s2, s12, pl
// 0x1089f94: ldr s13, [x19, #0x178]
// 0x1089f98: fmul s0, s1, s0
// 0x1089f9c: fadd s0, s9, s0
// 0x1089fa0: mov x0, xzr
// 0x1089fa4: str s0, [x19, #0x17c]
// 0x1089fa8: bl #0x1b9ae30
// 0x1089fac: fmul s0, s0, s10
// 0x1089fb0: ldr x8, [x19, #0x60]
// 0x1089fb4: fmin s1, s0, s11
// 0x1089fb8: fcmp s0, #0.0
// 0x1089fbc: fcsel s0, s1, s12, pl
// 0x1089fc0: fsub s1, s13, s8
// 0x1089fc4: fmul s0, s1, s0
// 0x1089fc8: fadd s0, s8, s0
// 0x1089fcc: str s0, [x19, #0x180]
// 0x1089fd0: cbz x8, #0x108a92c
// 0x1089fd4: ldrb w9, [x8, #0x2d0]
// 0x1089fd8: ldrb w8, [x19, #0x1b0]
// 0x1089fdc: cbz w9, #0x108a080
// 0x1089fe0: cbnz w8, #0x1089ff4
// 0x1089fe4: ldr s0, [x19, #0x1a8]
// 0x1089fe8: mov w8, #1
// 0x1089fec: strb w8, [x19, #0x1b0]
// 0x1089ff0: str s0, [x19, #0x1ac]
// 0x1089ff4: ldr x8, [x19, #0x90]
// 0x1089ff8: cbz x8, #0x108a92c
// 0x1089ffc: ldr x9, [x20]
// 0x108a000: cbz x9, #0x108a92c
// 0x108a004: ldr s8, [x8, #0x120]
// 0x108a008: ldr s9, [x9, #0x3d4]
// 0x108a00c: mov x0, xzr
// 0x108a010: bl #0x1b9ad30
// 0x108a014: fadd s1, s8, s9
// 0x108a018: fcmp s1, s0
// 0x108a01c: b.pl #0x108a0f0
// 0x108a020: ldr x8, [x20]
// 0x108a024: cbz x8, #0x108a92c
// 0x108a028: ldr s0, [x8, #0x204]
// 0x108a02c: fcmp s0, #0.0
// 0x108a030: b.ne #0x108a0f0
// 0x108a034: ldr s0, [x19, #0x184]
// 0x108a038: b #0x108a0ec
// 0x108a03c: ldrb w8, [x8, #0x258]
// 0x108a040: fmov s8, wzr
// 0x108a044: cbz w8, #0x1089654
// 0x108a048: ldr x8, [x19, #0x60]
// 0x108a04c: cbz x8, #0x108a92c
// 0x108a050: ldrb w8, [x8, #0x2d0]
// 0x108a054: cbz w8, #0x1089654
// 0x108a058: adrp x8, #0x832000
// 0x108a05c: ldr s0, [x19, #0x180]
// 0x108a060: ldr s1, [x8, #0x46c]
// 0x108a064: b #0x1089650
// 0x108a068: ldr x8, [x19, #0x48]
// 0x108a06c: cbz x8, #0x108a92c
// 0x108a070: ldrb w9, [x19, #0x230]
// 0x108a074: cbz w9, #0x108a420
// 0x108a078: ldr s0, [x8, #0x1fc]
// 0x108a07c: b #0x108a424
// 0x108a080: cbz w8, #0x108a090
// 0x108a084: ldr s0, [x19, #0x1ac]
// 0x108a088: strb wzr, [x19, #0x1b0]
// 0x108a08c: str s0, [x19, #0x1a8]
// 0x108a090: ldrb w8, [x19, #0x1a5]
// 0x108a094: cbz w8, #0x108a0f0
// 0x108a098: adrp x8, #0x1e8c000
// 0x108a09c: ldr x8, [x8, #0xe0]
// 0x108a0a0: ldr s8, [x19, #0x1a8]
// 0x108a0a4: ldr x0, [x8]
// 0x108a0a8: ldr w8, [x0, #0xe0]
// 0x108a0ac: cbnz w8, #0x108a0b4
// 0x108a0b0: bl #0xf7da5c
// 0x108a0b4: adrp x8, #0x1e8d000
// 0x108a0b8: ldr x8, [x8, #0xfd0]
// 0x108a0bc: mov x1, xzr
// 0x108a0c0: ldr x0, [x8]
// 0x108a0c4: bl #0x1035e20
// 0x108a0c8: ldr s2, [x19, #0x188]
// 0x108a0cc: ldr s1, [x19, #0x184]
// 0x108a0d0: fmov s3, #-5.00000000
// 0x108a0d4: fmul s0, s0, s3
// 0x108a0d8: fadd s0, s8, s0
// 0x108a0dc: fcmp s0, s2
// 0x108a0e0: fcsel s2, s2, s0, gt
// 0x108a0e4: fcmp s0, s1
// 0x108a0e8: fcsel s0, s2, s1, pl
// 0x108a0ec: str s0, [x19, #0x1a8]
// 0x108a0f0: ldrb w8, [x19, #0x1a5]
// 0x108a0f4: cbz w8, #0x108a178
// 0x108a0f8: ldrb w8, [x19, #0x19c]
// 0x108a0fc: cbz w8, #0x108a148
// 0x108a100: ldr x0, [x19, #0x128]
// 0x108a104: cbz x0, #0x108a92c
// 0x108a108: mov x1, xzr
// 0x108a10c: bl #0x1b9d400
// 0x108a110: cbz x0, #0x108a92c
// 0x108a114: mov x1, xzr
// 0x108a118: bl #0x1b92154
// 0x108a11c: ldr x8, [x19, #0x128]
// 0x108a120: cbz x8, #0x108a92c
// 0x108a124: mov x20, x0
// 0x108a128: mov x0, x8
// 0x108a12c: mov x1, xzr
// 0x108a130: bl #0x1b9d6f0
// 0x108a134: cbz x20, #0x108a92c
// 0x108a138: mov x0, x20
// 0x108a13c: mov x1, xzr
// 0x108a140: bl #0x1b9d774
// 0x108a144: strb wzr, [x19, #0x19c]
// 0x108a148: ldrb w8, [x19, #0x1a5]
// 0x108a14c: cbz w8, #0x108a170
// 0x108a150: ldr x8, [x19, #0x68]
// 0x108a154: cbz x8, #0x108a92c
// 0x108a158: ldr s0, [x8, #0xdc]
// 0x108a15c: fcmp s0, #0.0
// 0x108a160: b.ne #0x108a350
// 0x108a164: ldr s0, [x8, #0xe0]
// 0x108a168: fcmp s0, #0.0
// 0x108a16c: b.ne #0x108a350
// 0x108a170: mov w8, #1
// 0x108a174: b #0x108a35c
// 0x108a178: ldr x8, [x19, #0x68]
// 0x108a17c: cbz x8, #0x108a92c
// 0x108a180: ldr s0, [x8, #0xdc]
// 0x108a184: fcmp s0, #0.0
// 0x108a188: b.ne #0x108a200
// 0x108a18c: ldr s0, [x8, #0xe0]
// 0x108a190: fcmp s0, #0.0
// 0x108a194: b.ne #0x108a200
// 0x108a198: ldrb w9, [x8, #0x89]
// 0x108a19c: cbnz w9, #0x108a200
// 0x108a1a0: ldrb w9, [x8, #0x9b]
// 0x108a1a4: cbnz w9, #0x108a200
// 0x108a1a8: ldrb w8, [x8, #0x9d]
// 0x108a1ac: cbnz w8, #0x108a200
// 0x108a1b0: ldr x8, [x20]
// 0x108a1b4: cbz x8, #0x108a92c
// 0x108a1b8: ldr s8, [x8, #0x1c0]
// 0x108a1bc: mov x0, xzr
// 0x108a1c0: bl #0x1b9ad30
// 0x108a1c4: adrp x8, #0x832000
// 0x108a1c8: ldr s1, [x8, #0x3b8]
// 0x108a1cc: fadd s1, s8, s1
// 0x108a1d0: fcmp s1, s0
// 0x108a1d4: b.gt #0x108a200
// 0x108a1d8: ldr x8, [x19, #0x90]
// 0x108a1dc: cbz x8, #0x108a92c
// 0x108a1e0: ldrb w8, [x8, #0x17e]
// 0x108a1e4: cbnz w8, #0x108a200
// 0x108a1e8: ldrb w8, [x19, #0xb0]
// 0x108a1ec: cbnz w8, #0x108a200
// 0x108a1f0: ldr x8, [x19, #0x60]
// 0x108a1f4: cbz x8, #0x108a92c
// 0x108a1f8: ldrb w8, [x8, #0x2d0]
// 0x108a1fc: cbz w8, #0x108a0f8
// 0x108a200: ldrb w8, [x19, #0x19c]
// 0x108a204: cbnz w8, #0x108a2c0
// 0x108a208: ldrb w8, [x19, #0x1a7]
// 0x108a20c: cbz w8, #0x108a248
// 0x108a210: ldr x0, [x19, #0x128]
// 0x108a214: cbz x0, #0x108a92c
// 0x108a218: ldr x20, [x19, #0x50]
// 0x108a21c: mov x1, xzr
// 0x108a220: bl #0x1b9d400
// 0x108a224: cbz x0, #0x108a92c
// 0x108a228: mov x1, xzr
// 0x108a22c: bl #0x1b92154
// 0x108a230: cbz x0, #0x108a92c
// 0x108a234: mov x1, xzr
// 0x108a238: bl #0x1b9d6c8
// 0x108a23c: cbz x20, #0x108a92c
// 0x108a240: str s1, [x20, #0x50]
// 0x108a244: strb wzr, [x19, #0x1a7]
// 0x108a248: ldr x20, [x19, #0x128]
// 0x108a24c: cbz x20, #0x108a92c
// 0x108a250: mov x0, x20
// 0x108a254: mov x1, xzr
// 0x108a258: bl #0x1b9d400
// 0x108a25c: cbz x0, #0x108a92c
// 0x108a260: mov x1, xzr
// 0x108a264: bl #0x1b92154
// 0x108a268: cbz x0, #0x108a92c
// 0x108a26c: mov x1, xzr
// 0x108a270: bl #0x1b9d508
// 0x108a274: mov x0, x20
// 0x108a278: mov x1, xzr
// 0x108a27c: bl #0x1b9d5a8
// 0x108a280: ldr x20, [x19, #0x128]
// 0x108a284: cbz x20, #0x108a92c
// 0x108a288: mov x0, x20
// 0x108a28c: mov x1, xzr
// 0x108a290: bl #0x1b9d400
// 0x108a294: cbz x0, #0x108a92c
// 0x108a298: mov x1, xzr
// 0x108a29c: bl #0x1b92154
// 0x108a2a0: cbz x0, #0x108a92c
// 0x108a2a4: mov x1, xzr
// 0x108a2a8: bl #0x1b9d6f0
// 0x108a2ac: mov x0, x20
// 0x108a2b0: mov x1, xzr
// 0x108a2b4: bl #0x1b9d774
// 0x108a2b8: mov w8, #1
// 0x108a2bc: strb w8, [x19, #0x19c]
// 0x108a2c0: ldr x8, [x19, #0x50]
// 0x108a2c4: strb wzr, [x19, #0x1a6]
// 0x108a2c8: cbz x8, #0x108a92c
// 0x108a2cc: strb wzr, [x8, #0xab]
// 0x108a2d0: ldr x0, [x19, #0x128]
// 0x108a2d4: cbz x0, #0x108a92c
// 0x108a2d8: mov x1, xzr
// 0x108a2dc: bl #0x1b9d400
// 0x108a2e0: cbz x0, #0x108a92c
// 0x108a2e4: mov x1, xzr
// 0x108a2e8: bl #0x1b92154
// 0x108a2ec: cbz x0, #0x108a92c
// 0x108a2f0: ldr s3, [x19, #0x20c]
// 0x108a2f4: ldr s2, [x19, #0x208]
// 0x108a2f8: ldr s1, [x19, #0x204]
// 0x108a2fc: ldr s0, [x19, #0x200]
// 0x108a300: mov x1, xzr
// 0x108a304: bl #0x1b9d774
// 0x108a308: ldr x0, [x19, #0x128]
// 0x108a30c: cbz x0, #0x108a92c
// 0x108a310: mov x1, xzr
// 0x108a314: bl #0x1b9d400
// 0x108a318: cbz x0, #0x108a92c
// 0x108a31c: mov x1, xzr
// 0x108a320: bl #0x1b92154
// 0x108a324: ldr x8, [x19, #0x120]
// 0x108a328: cbz x8, #0x108a92c
// 0x108a32c: ldr s12, [x19, #0x1c4]
// 0x108a330: ldr s13, [x19, #0x1bc]
// 0x108a334: ldr d10, [x19, #0x150]
// 0x108a338: ldr d11, [x19, #0x1f8]
// 0x108a33c: ldr s8, [x19, #0x14c]
// 0x108a340: ldr s9, [x19, #0x1f4]
// 0x108a344: mov x20, x0
// 0x108a348: mov x0, x8
// 0x108a34c: b #0x108a3b4
// 0x108a350: mov w8, wzr
// 0x108a354: mov w9, #1
// 0x108a358: strb w9, [x19, #0x1a7]
// 0x108a35c: ldr x9, [x19, #0x50]
// 0x108a360: strb w8, [x19, #0x1a6]
// 0x108a364: cbz x9, #0x108a92c
// 0x108a368: mov w8, #1
// 0x108a36c: strb w8, [x9, #0xab]
// 0x108a370: ldr x0, [x19, #0x128]
// 0x108a374: cbz x0, #0x108a92c
// 0x108a378: ldr s3, [x19, #0x20c]
// 0x108a37c: ldr s2, [x19, #0x208]
// 0x108a380: ldr s1, [x19, #0x204]
// 0x108a384: ldr s0, [x19, #0x200]
// 0x108a388: mov x1, xzr
// 0x108a38c: bl #0x1b9d774
// 0x108a390: ldr x0, [x19, #0x120]
// 0x108a394: cbz x0, #0x108a92c
// 0x108a398: ldr x20, [x19, #0x128]
// 0x108a39c: ldr s12, [x19, #0x1c4]
// 0x108a3a0: ldr s13, [x19, #0x1bc]
// 0x108a3a4: ldr d10, [x19, #0x150]
// 0x108a3a8: ldr d11, [x19, #0x1f8]
// 0x108a3ac: ldr s8, [x19, #0x14c]
// 0x108a3b0: ldr s9, [x19, #0x1f4]
// 0x108a3b4: mov x1, xzr
// 0x108a3b8: bl #0x1b9d940
// 0x108a3bc: cbz x20, #0x108a92c
// 0x108a3c0: ldr s3, [x19, #0x180]
// 0x108a3c4: fadd s4, s12, s13
// 0x108a3c8: mov v1.s[1], v2.s[0]
// 0x108a3cc: fmul v2.2s, v11.2s, v4.s[0]
// 0x108a3d0: fadd v2.2s, v10.2s, v2.2s
// 0x108a3d4: fmul v1.2s, v1.2s, v3.s[0]
// 0x108a3d8: fadd v1.2s, v2.2s, v1.2s
// 0x108a3dc: fmul s2, s4, s9
// 0x108a3e0: fadd s2, s8, s2
// 0x108a3e4: fmul s0, s0, s3
// 0x108a3e8: fadd s0, s2, s0
// 0x108a3ec: mov s2, v1.s[1]
// 0x108a3f0: mov x0, x20
// 0x108a3f4: mov x1, xzr
// 0x108a3f8: bl #0x1b9d5a8
// 0x108a3fc: ldr x8, [x19, #0x40]
// 0x108a400: cbz x8, #0x108a92c
// 0x108a404: ldrb w8, [x8, #0x2e8]
// 0x108a408: cbnz w8, #0x108a7c0
// 0x108a40c: ldr x8, [x19, #0x48]
// 0x108a410: cbz x8, #0x108a92c
// 0x108a414: movi d0, #0000000000000000
// 0x108a418: str d0, [x8, #0x250]
// 0x108a41c: b #0x108a7c0
// 0x108a420: ldr s0, [x8, #0x1f8]
// 0x108a424: ldr x9, [x19, #0x40]
// 0x108a428: str s0, [x19, #0xe0]
// 0x108a42c: cbz x9, #0x108a92c
// 0x108a430: ldr x8, [x19, #0x48]
// 0x108a434: cbz x8, #0x108a92c
// 0x108a438: ldrb w9, [x9, #0x2b1]
// 0x108a43c: cbz w9, #0x108a474
// 0x108a440: ldr s0, [x8, #0x1e4]
// 0x108a444: mov x0, xzr
// 0x108a448: str s0, [x19, #0x164]
// 0x108a44c: bl #0x1b9ae58
// 0x108a450: ldr x8, [x19, #0x48]
// 0x108a454: cbz x8, #0x108a92c
// 0x108a458: ldr s1, [x8, #0x1f0]
// 0x108a45c: fmov s2, #1.00000000
// 0x108a460: mov w8, #-0x3b860000
// 0x108a464: fsub s0, s2, s0
// 0x108a468: fmov s2, w8
// 0x108a46c: fmul s0, s0, s2
// 0x108a470: b #0x108a4f8
// 0x108a474: ldr s0, [x8, #0x1e8]
// 0x108a478: ldrb w9, [x19, #0x230]
// 0x108a47c: str s0, [x19, #0x164]
// 0x108a480: cbz w9, #0x108a48c
// 0x108a484: ldr s0, [x8, #0x1f4]
// 0x108a488: b #0x108a4f0
// 0x108a48c: mov x0, xzr
// 0x108a490: bl #0x1b9ae58
// 0x108a494: fmov s1, #1.00000000
// 0x108a498: fcmp s0, s1
// 0x108a49c: b.pl #0x108a4e4
// 0x108a4a0: mov x0, xzr
// 0x108a4a4: bl #0x1b9ae58
// 0x108a4a8: ldr x8, [x19, #0x48]
// 0x108a4ac: cbz x8, #0x108a92c
// 0x108a4b0: ldr s1, [x8, #0x1f0]
// 0x108a4b4: fmov s2, #1.00000000
// 0x108a4b8: mov w8, #-0x3c060000
// 0x108a4bc: b #0x108a464
// 0x108a4c0: ldrb w8, [x19, #0x106]
// 0x108a4c4: cbz w8, #0x108a920
// 0x108a4c8: ldrb w8, [x19, #0x105]
// 0x108a4cc: cbz w8, #0x1089204
// 0x108a4d0: ldrb w8, [x19, #0x210]
// 0x108a4d4: cbnz w8, #0x1089204
// 0x108a4d8: mov w8, #1
// 0x108a4dc: strb w8, [x19, #0x210]
// 0x108a4e0: b #0x1089204
// 0x108a4e4: ldr x8, [x19, #0x48]
// 0x108a4e8: cbz x8, #0x108a92c
// 0x108a4ec: ldr s0, [x8, #0x1ec]
// 0x108a4f0: mov w8, #-0x3d380000
// 0x108a4f4: fmov s1, w8
// 0x108a4f8: ldr x20, [x19, #0x38]
// 0x108a4fc: fmul s0, s0, s1
// 0x108a500: str s0, [x19, #0x168]
// 0x108a504: cbz x20, #0x108a92c
// 0x108a508: mov x0, x20
// 0x108a50c: mov x1, xzr
// 0x108a510: bl #0x1b9d7f0
// 0x108a514: adrp x21, #0x1fab000
// 0x108a518: ldrb w8, [x21, #0x2cb]
// 0x108a51c: mov v8.16b, v0.16b
// 0x108a520: mov v9.16b, v1.16b
// 0x108a524: mov v10.16b, v2.16b
// 0x108a528: mov v11.16b, v3.16b
// 0x108a52c: cbnz w8, #0x108a544
// 0x108a530: adrp x0, #0x1e8c000
// 0x108a534: ldr x0, [x0, #0xd88]
// 0x108a538: bl #0xf7d92c
// 0x108a53c: mov w8, #1
// 0x108a540: strb w8, [x21, #0x2cb]
// 0x108a544: adrp x8, #0x1e8c000
// 0x108a548: ldr x8, [x8, #0xd88]
// 0x108a54c: mov x0, xzr
// 0x108a550: ldr x8, [x8]
// 0x108a554: ldr x8, [x8, #0xb8]
// 0x108a558: ldp s12, s13, [x8]
// 0x108a55c: ldp s14, s15, [x8, #8]
// 0x108a560: bl #0x1b89b60
// 0x108a564: ldr s1, [x19, #0xe0]
// 0x108a568: mov v2.16b, v10.16b
// 0x108a56c: mov v3.16b, v11.16b
// 0x108a570: mov v4.16b, v12.16b
// 0x108a574: fmul s0, s0, s1
// 0x108a578: str s0, [sp]
// 0x108a57c: mov v0.16b, v8.16b
// 0x108a580: mov v1.16b, v9.16b
// 0x108a584: mov v5.16b, v13.16b
// 0x108a588: mov v6.16b, v14.16b
// 0x108a58c: mov v7.16b, v15.16b
// 0x108a590: mov x0, xzr
// 0x108a594: bl #0x1b8af84
// 0x108a598: mov x0, x20
// 0x108a59c: mov x1, xzr
// 0x108a5a0: bl #0x1b9d874
// 0x108a5a4: mov x0, xzr
// 0x108a5a8: bl #0x1b89b60
// 0x108a5ac: fmov s1, #1.00000000
// 0x108a5b0: mov w8, #0x42960000
// 0x108a5b4: ldr x0, [x19, #0x128]
// 0x108a5b8: fcmp s0, #0.0
// 0x108a5bc: fmin s0, s0, s1
// 0x108a5c0: fmov s1, w8
// 0x108a5c4: fmul s0, s0, s1
// 0x108a5c8: fmov s1, wzr
// 0x108a5cc: fcsel s0, s0, s1, pl
// 0x108a5d0: str s0, [x19, #0xdc]
// 0x108a5d4: cbz x0, #0x108a92c
// 0x108a5d8: mov x1, xzr
// 0x108a5dc: bl #0x1b9d7c8
// 0x108a5e0: ldr x8, [x19, #0x78]
// 0x108a5e4: cbz x8, #0x108a92c
// 0x108a5e8: ldr x9, [x19, #0x48]
// 0x108a5ec: cbz x9, #0x108a92c
// 0x108a5f0: ldr x0, [x19, #0x128]
// 0x108a5f4: cbz x0, #0x108a92c
// 0x108a5f8: ldr s12, [x8, #0x30]
// 0x108a5fc: ldr s15, [x9, #0x1c4]
// 0x108a600: ldr s9, [x19, #0xdc]
// 0x108a604: ldr s14, [x19, #0xb4]
// 0x108a608: mov x1, xzr
// 0x108a60c: mov v8.16b, v0.16b
// 0x108a610: bl #0x1b9d7c8
// 0x108a614: ldr x8, [x19, #0x78]
// 0x108a618: cbz x8, #0x108a92c
// 0x108a61c: ldr x9, [x19, #0x48]
// 0x108a620: cbz x9, #0x108a92c
// 0x108a624: ldr x0, [x19, #0x128]
// 0x108a628: cbz x0, #0x108a92c
// 0x108a62c: ldr s2, [x9, #0x1c0]
// 0x108a630: ldr s0, [x19, #0xb8]
// 0x108a634: ldr s10, [x8, #0x2c]
// 0x108a638: ldr s13, [x19, #0xdc]
// 0x108a63c: mov x1, xzr
// 0x108a640: mov v11.16b, v1.16b
// 0x108a644: stp s2, s0, [sp, #0x40]
// 0x108a648: bl #0x1b9d7c8
// 0x108a64c: ldr x8, [x19, #0x78]
// 0x108a650: cbz x8, #0x108a92c
// 0x108a654: ldr x9, [x19, #0x48]
// 0x108a658: cbz x9, #0x108a92c
// 0x108a65c: ldr x10, [x19, #0x40]
// 0x108a660: stp s10, s2, [sp, #0x38]
// 0x108a664: cbz x10, #0x108a92c
// 0x108a668: ldr s0, [x9, #0x1c8]
// 0x108a66c: ldr s1, [x8, #0x34]
// 0x108a670: ldr s10, [x19, #0xdc]
// 0x108a674: mov x0, xzr
// 0x108a678: str s0, [sp, #0x24]
// 0x108a67c: ldr s0, [x19, #0xbc]
// 0x108a680: stp s0, s1, [sp, #0x28]
// 0x108a684: ldr s0, [x10, #0x170]
// 0x108a688: str s0, [sp, #0x34]
// 0x108a68c: bl #0x1b89b60
// 0x108a690: ldr x8, [x19, #0x40]
// 0x108a694: str s0, [sp, #0x30]
// 0x108a698: cbz x8, #0x108a92c
// 0x108a69c: ldr s0, [x19, #0xe0]
// 0x108a6a0: ldr s1, [x8, #0xc0]
// 0x108a6a4: mov x0, xzr
// 0x108a6a8: stp s11, s8, [sp, #0x1c]
// 0x108a6ac: str s0, [sp, #0x18]
// 0x108a6b0: ldr s0, [x19, #0x164]
// 0x108a6b4: stp s0, s1, [sp, #0xc]
// 0x108a6b8: bl #0x1b89b60
// 0x108a6bc: ldr x8, [x19, #0x48]
// 0x108a6c0: str s0, [sp, #0x14]
// 0x108a6c4: cbz x8, #0x108a92c
// 0x108a6c8: ldr s0, [x19, #0xe0]
// 0x108a6cc: ldr s8, [x8, #0x250]
// 0x108a6d0: ldr s11, [x19, #0x168]
// 0x108a6d4: mov x0, xzr
// 0x108a6d8: str s0, [sp, #8]
// 0x108a6dc: bl #0x1b89b60
// 0x108a6e0: ldp s19, s4, [sp, #0x34]
// 0x108a6e4: fmov s16, #-3.00000000
// 0x108a6e8: ldp s18, s17, [sp, #0xc]
// 0x108a6ec: fmul s2, s12, s15
// 0x108a6f0: fmul s16, s19, s16
// 0x108a6f4: ldr s19, [sp, #0x14]
// 0x108a6f8: fmul s17, s17, s18
// 0x108a6fc: ldr s5, [sp, #0x40]
// 0x108a700: fmul s2, s2, s9
// 0x108a704: fmul s17, s17, s19
// 0x108a708: ldr s19, [sp, #0x20]
// 0x108a70c: fmul s4, s4, s5
// 0x108a710: ldr s6, [sp, #0x2c]
// 0x108a714: ldr s7, [sp, #0x24]
// 0x108a718: fsub s2, s19, s2
// 0x108a71c: ldr s19, [sp, #0x1c]
// 0x108a720: fmul s4, s4, s13
// 0x108a724: ldr s5, [sp, #0x44]
// 0x108a728: fmul s6, s6, s7
// 0x108a72c: fsub s4, s19, s4
// 0x108a730: ldr s19, [sp, #0x3c]
// 0x108a734: fmul s6, s6, s10
// 0x108a738: fmul s3, s9, s14
// 0x108a73c: fmul s5, s13, s5
// 0x108a740: fsub s6, s19, s6
// 0x108a744: ldr s19, [sp, #0x30]
// 0x108a748: ldr s7, [sp, #0x28]
// 0x108a74c: fadd s2, s2, s3
// 0x108a750: fadd s3, s4, s5
// 0x108a754: ldr s5, [sp, #0x18]
// 0x108a758: fmul s16, s16, s19
// 0x108a75c: ldr s19, [sp, #8]
// 0x108a760: ldr s1, [x19, #0xe0]
// 0x108a764: fmul s18, s8, s11
// 0x108a768: adrp x8, #0x832000
// 0x108a76c: fmul s7, s10, s7
// 0x108a770: fmul s0, s18, s0
// 0x108a774: ldr s18, [x8, #0x3e4]
// 0x108a778: fadd s4, s6, s7
// 0x108a77c: fmul s5, s16, s5
// 0x108a780: fmul s17, s17, s19
// 0x108a784: fadd s4, s4, s5
// 0x108a788: fmul s1, s0, s1
// 0x108a78c: fsub s4, s4, s17
// 0x108a790: fmul s0, s2, s18
// 0x108a794: fsub s2, s4, s1
// 0x108a798: fmul s1, s3, s18
// 0x108a79c: fmul s2, s2, s18
// 0x108a7a0: mov x0, xzr
// 0x108a7a4: bl #0x1b8b12c
// 0x108a7a8: ldr x0, [x19, #0x38]
// 0x108a7ac: stp s0, s1, [x19, #0xcc]
// 0x108a7b0: stp s2, s3, [x19, #0xd4]
// 0x108a7b4: cbz x0, #0x108a92c
// 0x108a7b8: mov x1, xzr
// 0x108a7bc: bl #0x1b9d874
// 0x108a7c0: ldr x8, [x19, #0x40]
// 0x108a7c4: cbz x8, #0x108a92c
// 0x108a7c8: ldr s0, [x8, #0x290]
// 0x108a7cc: fmov s1, #1.25000000
// 0x108a7d0: fcmp s0, s1
// 0x108a7d4: b.pl #0x108a7e0
// 0x108a7d8: ldrb w8, [x8, #0x2a0]
// 0x108a7dc: cbz w8, #0x108a808
// 0x108a7e0: ldrb w8, [x19, #0xe4]
// 0x108a7e4: cbz w8, #0x108a824
// 0x108a7e8: ldp s8, s9, [x19, #0xe8]
// 0x108a7ec: mov x0, xzr
// 0x108a7f0: bl #0x1b9ad30
// 0x108a7f4: fadd s1, s8, s9
// 0x108a7f8: fcmp s1, s0
// 0x108a7fc: b.pl #0x108a824
// 0x108a800: strb wzr, [x19, #0xe4]
// 0x108a804: b #0x108a824
// 0x108a808: ldrb w8, [x19, #0xe4]
// 0x108a80c: cbnz w8, #0x108a824
// 0x108a810: mov x0, xzr
// 0x108a814: bl #0x1b9ad30
// 0x108a818: mov w8, #1
// 0x108a81c: str s0, [x19, #0xe8]
// 0x108a820: strb w8, [x19, #0xe4]
// 0x108a824: ldp s8, s9, [x19, #0xe8]
// 0x108a828: mov x0, xzr
// 0x108a82c: bl #0x1b9ad30
// 0x108a830: fadd s1, s8, s9
// 0x108a834: fcmp s1, s0
// 0x108a838: b.le #0x108a884
// 0x108a83c: ldp s10, s11, [x19, #0xe8]
// 0x108a840: mov x0, xzr
// 0x108a844: bl #0x1b9ad30
// 0x108a848: ldp s12, s9, [x19, #0xf0]
// 0x108a84c: mov v8.16b, v0.16b
// 0x108a850: fmov s0, #0.50000000
// 0x108a854: fmul s0, s11, s0
// 0x108a858: mov x0, xzr
// 0x108a85c: fadd s10, s10, s0
// 0x108a860: bl #0x1b89b60
// 0x108a864: adrp x8, #0x832000
// 0x108a868: ldr s1, [x8, #0x3b8]
// 0x108a86c: fcmp s10, s8
// 0x108a870: fmin s0, s0, s1
// 0x108a874: fmul s0, s12, s0
// 0x108a878: b.pl #0x108a890
// 0x108a87c: fadd s0, s9, s0
// 0x108a880: b #0x108a894
// 0x108a884: fmov s0, wzr
// 0x108a888: str wzr, [x19, #0xf4]
// 0x108a88c: b #0x108a898
// 0x108a890: fsub s0, s9, s0
// 0x108a894: str s0, [x19, #0xf4]
// 0x108a898: ldr x8, [x19, #0x60]
// 0x108a89c: cbz x8, #0x108a92c
// 0x108a8a0: ldrb w8, [x8, #0x2d0]
// 0x108a8a4: adrp x9, #0x832000
// 0x108a8a8: add x9, x9, #0x220
// 0x108a8ac: ldr s8, [x19, #0x130]
// 0x108a8b0: cmp w8, #0
// 0x108a8b4: cset w8, eq
// 0x108a8b8: ldr s1, [x9, w8, uxtw #2]
// 0x108a8bc: mov x0, xzr
// 0x108a8c0: fmul s0, s0, s1
// 0x108a8c4: str s0, [x19, #0xf8]
// 0x108a8c8: bl #0x1b9ad30
// 0x108a8cc: ldr x8, [x19, #0x48]
// 0x108a8d0: fmov s1, #0.75000000
// 0x108a8d4: fadd s1, s8, s1
// 0x108a8d8: fcmp s1, s0
// 0x108a8dc: b.pl #0x108a8ec
// 0x108a8e0: cbz x8, #0x108a92c
// 0x108a8e4: ldr s0, [x19, #0xf8]
// 0x108a8e8: b #0x108a8f4
// 0x108a8ec: fmov s0, wzr
// 0x108a8f0: cbz x8, #0x108a92c
// 0x108a8f4: ldp x20, x19, [sp, #0x110]
// 0x108a8f8: ldp x22, x21, [sp, #0x100]
// 0x108a8fc: ldp x24, x23, [sp, #0xf0]
// 0x108a900: ldp x29, x30, [sp, #0xe0]
// 0x108a904: ldp d9, d8, [sp, #0xd0]
// 0x108a908: ldp d11, d10, [sp, #0xc0]
// 0x108a90c: ldp d13, d12, [sp, #0xb0]
// 0x108a910: ldp d15, d14, [sp, #0xa0]
// 0x108a914: str s0, [x8, #0x244]
// 0x108a918: add sp, sp, #0x120
// 0x108a91c: ret
// 0x108a920: mov w8, #1
// 0x108a924: strb w8, [x19, #0x106]
// 0x108a928: b #0x1089204
// 0x108a92c: bl #0xf7db74
```

## `CameraControl.ClampAngle` — RVA `0xc8a930`

- Decompiled symbol: `CameraControl_ClampAngle`
- Metadata signature: `public static float ClampAngle(float angle, float min, float max) { }`
- Native interval: `136` bytes
- Result: `pseudocode`

```c
void CameraControl_ClampAngle(void)
{
    unsigned long long v2;  // d9
    unsigned long long v3;  // d8
    unsigned int v12;  // s1
    unsigned long v13;  // 4129
    unsigned int v4;  // s0
    unsigned long v5;  // 4128
    unsigned long v6;  // 4128
    unsigned long v7;  // 4148
    unsigned int v8;  // s0
    unsigned long v9;  // 4125
    unsigned int v10;  // s2
    unsigned long v11;  // 4133
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x18]

    v0 = v2;
    v1 = v3;
    fmodf();
    v5 = arm64g_calculate_condition(176, (((((unsigned long long)(char)(CmpF(v4, 0xc3b40000)) >> 5 & 3 | (unsigned long long)(CmpF(v4, 0xc3b40000) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v4, 0xc3b40000)) >> 5 & 3 | (unsigned long long)(CmpF(v4, 0xc3b40000) & 1)) & ((unsigned long long)(char)(CmpF(v4, 0xc3b40000)) >> 5 & 3 | (unsigned long long)(CmpF(v4, 0xc3b40000) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if (!((char)v5))
    {
        v6 = arm64g_calculate_condition(128, (((((unsigned long long)(char)(CmpF(v4, 0x43b40000)) >> 5 & 3 | (unsigned long long)(CmpF(v4, 0x43b40000) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v4, 0x43b40000)) >> 5 & 3 | (unsigned long long)(CmpF(v4, 0x43b40000) & 1)) & ((unsigned long long)(char)(CmpF(v4, 0x43b40000)) >> 5 & 3 | (unsigned long long)(CmpF(v4, 0x43b40000) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if (!((char)v6))
        {
            v7 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(v4, 0xc3b40000)) >> 5 & 3 | (unsigned long long)(CmpF(v4, 0xc3b40000) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v4, 0xc3b40000)) >> 5 & 3 | (unsigned long long)(CmpF(v4, 0xc3b40000) & 1)) & ((unsigned long long)(char)(CmpF(v4, 0xc3b40000)) >> 5 & 3 | (unsigned long long)(CmpF(v4, 0xc3b40000) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
            if ((char)v7)
                v8 = v4 + 0x43b40000;
            v9 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v8, 0x43b40000)) >> 5 & 3 | (unsigned long long)(CmpF(v8, 0x43b40000) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v8, 0x43b40000)) >> 5 & 3 | (unsigned long long)(CmpF(v8, 0x43b40000) & 1)) & ((unsigned long long)(char)(CmpF(v8, 0x43b40000)) >> 5 & 3 | (unsigned long long)(CmpF(v8, 0x43b40000) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
            if (!((char)v9))
                v8 += 0xc3b40000;
        }
    }
    v11 = arm64g_calculate_condition(192, (((((unsigned long long)(char)(CmpF(v8, v10)) >> 5 & 3 | (unsigned long long)(CmpF(v8, v10) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v8, v10)) >> 5 & 3 | (unsigned long long)(CmpF(v8, v10) & 1)) & ((unsigned long long)(char)(CmpF(v8, v10)) >> 5 & 3 | (unsigned long long)(CmpF(v8, v10) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    v13 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v8, v12)) >> 5 & 3 | (unsigned long long)(CmpF(v8, v12) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v8, v12)) >> 5 & 3 | (unsigned long long)(CmpF(v8, v12) & 1)) & ((unsigned long long)(char)(CmpF(v8, v12)) >> 5 & 3 | (unsigned long long)(CmpF(v8, v12) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if (!((char)v13))
        return;
    return;
}
```

## `CameraControl.AdjustLineOfSight` — RVA `0xc8a9b8`

- Decompiled symbol: `CameraControl_AdjustLineOfSight`
- Metadata signature: `private float AdjustLineOfSight(Vector3 target, Vector3 direction) { }`
- Native interval: `420` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[564];
    unsigned int field_234;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0e48;
extern long long g_1f0c700;
extern char g_1fab434;

unsigned long long CameraControl_AdjustLineOfSight(struct_1 *a0)
{
    unsigned int v3;  // w0
    unsigned long long v4;  // x0
    long long v5;  // x0
    unsigned long long v6;  // x0
    long long v7;  // x0
    unsigned long long v8;  // x0
    unsigned long long v9;  // x0
    int choice;  // [bp-0x90]
    uint128_t flag2;  // [bp-0x80]
    uint128_t flag;  // [bp-0x74]

    if (!(g_1fab434 & 1))
    {
        sub_f7d92c(&g_1ef0e48);
        sub_f7d92c("s%");
        sub_f7d92c(&g_1f0c700);
        g_1fab434 = 1;
    }
    flag = 0;
    choice = 0;
    flag2 = 0;
    v3 = LayerMask__op_Implicit(a0->field_234, 0);
    if (!g_1ef0e48->field_e0)
        sub_f7da5c(g_1ef0e48);
    v4 = Physics__SphereCast(&choice, v3, 0);
    if (!((char)v4 & 1))
        return v4;
    if (RaycastHit__get_collider(&choice, 0) && Component__get_gameObject())
    {
        v5 = GameObject__get_tag();
        v6 = String__op_Inequality(v5, g_1f0f7c0, 0);
        if (!((char)v6 & 1))
        {
            return v6;
        }
        else if (RaycastHit__get_collider(&choice, 0) && Component__get_gameObject())
        {
            v7 = GameObject__get_tag();
            v8 = String__op_Inequality(v7, g_1f0c700, 0);
            if (!((char)v8 & 1))
                return v8;
            v9 = RaycastHit__get_distance(&choice, 0);
            return RaycastHit__get_distance(&choice, 0);
        }
    }
    sub_f7db74();
}
```

## `CameraControl.ctor` — RVA `0xc8ab5c`

- Decompiled symbol: `CameraControl_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `304` bytes
- Result: `pseudocode`
- Heuristic layout hint: `CameraControl_Recovered` matched 14 offsets against `CameraControl` metadata (confidence 0.78).

```c
typedef struct struct_1 {
    char padding_0[184];
    struct struct_0 *field_b8;
} struct_1;

typedef struct CameraControl_Recovered {
    char padding_0[180];
    unsigned long long CameraAnglesAnim;
    unsigned int field_bc;
    unsigned long long bobAngles;
    unsigned int field_c8;
    char padding_cc[20];
    unsigned int returnSpeedAmt;
    char padding_e4[8];
    unsigned long long landTime;
    char padding_f4[16];
    unsigned short allowThirdPerson;
    char padding_106[14];
    unsigned int camSmoothSpeed;
    char padding_118[28];
    unsigned long long targetPos;
    unsigned int field_13c;
    char padding_140[24];
    unsigned long long tempLerpPos;
    unsigned int field_160;
    char padding_164[8];
    unsigned long long horizontalRotateSpeed;
    char padding_174[16];
    unsigned long long minZoom;
    char padding_18c[8];
    unsigned long long verticalMin;
    char padding_19c[8];
    char tpPressState;
    char padding_1a5[15];
    unsigned long long sphereSizeTpCol;
    char padding_1bc[88];
    unsigned long long fpZoomHeadHeight;
} CameraControl_Recovered;

typedef struct struct_0 {
    unsigned long long field_0;
    unsigned int field_8;
    unsigned long long field_c;
    unsigned int field_14;
} struct_0;

extern struct_1 *g_1ef22e8;
extern char g_1fab1e1;
extern char g_1fab2c9;

void CameraControl_ctor(struct_2 *ptr)
{
    unsigned long long v5;  // x30
    unsigned long long v6;  // x22
    unsigned int v15;  // s1
    unsigned int v16;  // s1
    unsigned long long v7;  // x21
    unsigned long long v8;  // x20
    unsigned long long v9;  // x19
    struct_1 *pos;  // x8
    struct_2 *p;  // x21
    unsigned int v12;  // s1
    unsigned long long v13;  // d1
    unsigned int v14;  // s2
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
    if (!g_1fab2c9)
    {
        sub_f7d92c(&g_1ef22e8);
        g_1fab2c9 = 1;
    }
    pos = g_1ef22e8;
    p = &ptr->padding_118[16];
    v12 = g_1ef22e8->field_b8->field_8;
    *((unsigned long long *)&(&ptr->padding_0)[1]) = g_1ef22e8->field_b8->field_0;
    *((unsigned int *)((char *)&ptr->field_b4 + 4)) = v12;
    v13 = g_1ef22e8->field_b8->field_0;
    v14 = g_1ef22e8->field_b8->field_8;
    *((unsigned long long *)&ptr->padding_e4[0]) = 4575657222460355379;
    *((unsigned int *)&ptr->padding_cc[12]) = 0x40800000;
    *((unsigned short *)&ptr->padding_f4[4]) = 257;
    *((unsigned int *)&ptr->padding_106[2]) = 1033476506;
    *((unsigned long long *)&ptr->field_bc) = v13;
    *((unsigned int *)&ptr->field_c0) = v14;
    if (!g_1fab1e1)
    {
        sub_f7d92c(&g_1ef22e8);
        pos = g_1ef22e8;
        g_1fab1e1 = 1;
    }
    v15 = *((int *)((char *)&pos->field_b8->field_c + 4));
    *((long long *)&p->padding_0[0]) = *((long long *)&(&pos->field_b8->field_8)[1]);
    *((unsigned int *)&ptr->padding_118[24]) = v15;
    v16 = *((int *)((char *)&pos->field_b8->field_c + 4));
    *((long long *)&ptr->padding_140[12]) = *((long long *)&(&pos->field_b8->field_8)[1]);
    *((unsigned int *)&ptr->padding_140[20]) = v16;
    *((unsigned long long *)&p->padding_0[56]) = 0x40a0000040a00000;
    *((unsigned long long *)&p->padding_0[80]) = 4692750812789184922;
    *((unsigned long long *)&p->padding_0[96]) = 0x42aa0000c1c80000;
    ptr->padding_18c[4] = 1;
    *((unsigned long long *)&p->padding_0[128]) = 13763000462294489498;
    *((unsigned long long *)&p->padding_cc[12]) = 4550437062844780380;
    MonoBehaviour__ctor();
    return;
}
```
