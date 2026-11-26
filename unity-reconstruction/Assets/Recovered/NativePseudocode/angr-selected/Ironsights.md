# Native pseudocode: Ironsights

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `Ironsights.Start` — RVA `0xcaef78`

- Decompiled symbol: `Ironsights_Start`
- Metadata signature: `private void Start() { }`
- Native interval: `824` bytes
- Result: `pseudocode`
- Heuristic layout hint: `Ironsights_Recovered` matched 14 offsets against `Ironsights` metadata (confidence 0.93).

```c
typedef struct Ironsights_Recovered {
    char padding_0[32];
    long long SmoothMouseLook;
    long long CamAndWeapAnimsComponent;
    char CamAndWeapAnimator;
    char padding_31[7];
    long long PlayerWeaponsComponent;
    long long FPSWalker;
    struct struct_0 *FPSPlayerComponent;
    long long InputComponent;
    char padding_58[8];
    long long WeaponPivotComponent;
    char padding_68[8];
    long long CameraControlComponent;
    long long playerObj;
    long long weaponObj;
    long long CameraObj;
    char padding_90[84];
    unsigned long long tempGunPos;
    unsigned int field_ec;
    char padding_f0[360];
    char aSource;
} Ironsights_Recovered;

typedef struct struct_2 {
    char padding_0[144];
    unsigned long long field_90;
} struct_2;

typedef struct struct_0 {
    char padding_0[144];
    long long field_90;
} struct_0;

typedef struct struct_3 {
    unsigned long long field_0;
    unsigned int field_8;
} struct_3;

typedef struct struct_4 {
    char padding_0[184];
    struct struct_3 *field_b8;
} struct_4;

extern struct_4 *g_1ef22e8;
extern long long g_1efcf38;
extern long long g_1efea78;
extern long long g_1efeb28;
extern long long g_1efeb58;
extern long long g_1efebb8;
extern long long g_1efebc0;
extern long long g_1efec08;
extern long long g_1efec90;
extern long long g_1efecd8;
extern long long g_1f0ae70;
extern long long g_1f0dc18;
extern char g_1fab2c9;
extern char g_1fab4cd;

void Ironsights_Start(struct_1 *ptr)
{
    unsigned long long v4;  // x30
    unsigned long long v5;  // x21
    struct_1 *ptr12;  // x20
    long long v15;  // x0
    struct_1 *addr;  // x20
    struct_1 *ptr13;  // x20
    struct_2 *v18;  // x0
    struct_1 *ptr3;  // x20
    struct_1 *ptr14;  // x20
    long long v21;  // x0
    struct_1 *ptr4;  // x20
    struct_1 *v23;  // x20
    unsigned long long v6;  // x20
    unsigned long v24;  // x1
    struct_1 *ptr5;  // x20
    struct_1 *ptr15;  // x20
    long long v27;  // x0
    struct_1 *ptr6;  // x20
    struct_1 *ptr16;  // x20
    unsigned long v30;  // x0
    struct_1 *ptr7;  // x20
    struct_1 *p;  // x20
    long long v33;  // x1
    unsigned long long v7;  // x19
    struct_1 *ptr8;  // x0
    unsigned int v35;  // s1
    unsigned long v36;  // x0
    struct_1 *ptr11;  // x21
    unsigned long v8;  // x0
    long long v9;  // x0
    struct_1 *ptr9;  // x20
    struct_1 *ptr17;  // x20
    long long v12;  // x0
    struct_1 *ptr10;  // x20
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x18]
    unsigned long long v2;  // [bp-0x10]
    unsigned long long v3;  // [bp-0x8]

    v0 = v4;
    v1 = v5;
    v2 = v6;
    v3 = v7;
    if (!(g_1fab4cd & 1))
    {
        sub_f7d92c(&g_1efcf38);
        sub_f7d92c(&g_1efea78);
        sub_f7d92c(&g_1efeb28);
        sub_f7d92c(&g_1efeb58);
        sub_f7d92c(&g_1efebb8);
        sub_f7d92c(&g_1efebc0);
        sub_f7d92c(&g_1efec08);
        sub_f7d92c(&g_1efec90);
        sub_f7d92c(&g_1efecd8);
        sub_f7d92c("M&");
        sub_f7d92c(&g_1f0ae70);
        sub_f7d92c(&g_1f0dc18);
        g_1fab4cd = 1;
    }
    v8 = ptr->field_88;
    if (v8)
    {
        v9 = sub_1249224(v8, g_1efecd8);
        ptr9 = ptr;
        ptr9->field_20 = v9;
        ptr17 = &ptr9->field_20;
        sub_f7d8d0(ptr17, v9);
        v8 = ptr17->field_60;
        if (v8)
        {
            v12 = sub_1249224(v8, g_1efec90);
            ptr10 = ptr;
            ptr10->field_38 = v12;
            ptr12 = &ptr10->field_38;
            sub_f7d8d0(ptr12, v12);
            v8 = ptr12->field_40;
            if (v8)
            {
                v15 = sub_1249224(v8, g_1efebc0);
                addr = ptr;
                addr->field_40 = v15;
                ptr13 = &addr->field_40;
                sub_f7d8d0(ptr13, v15);
                v8 = ptr13->field_38;
                if (v8)
                {
                    v18 = sub_1249224(v8, g_1efebb8);
                    ptr3 = ptr;
                    ptr3->field_48 = v18;
                    ptr14 = &ptr3->field_48;
                    sub_f7d8d0(ptr14, v18);
                    v8 = *((long long *)&ptr14->field_30);
                    if (v8)
                    {
                        v21 = sub_1249224(v8, g_1efec08);
                        ptr4 = ptr;
                        ptr4->field_50 = v21;
                        v23 = &ptr4->field_50;
                        v8 = sub_f7d8d0(v23, v21);
                        if (*((long long *)&v23->padding_0[8]))
                        {
                            v24 = *((long long *)(*((long long *)&v23->padding_0[8]) + 144));
                            ptr5 = ptr;
                            ptr5->field_60 = v24;
                            ptr15 = &ptr5->field_60;
                            sub_f7d8d0(ptr15, v24);
                            v8 = ptr15->field_28;
                            if (v8)
                            {
                                v27 = sub_1249224(v8, g_1efeb58);
                                ptr6 = ptr;
                                ptr6->field_28 = v27;
                                ptr16 = &ptr6->field_28;
                                sub_f7d8d0(ptr16, v27);
                                v8 = ptr16->field_60;
                                if (v8)
                                {
                                    v30 = sub_1249224(v8, g_1efeb28);
                                    ptr7 = ptr;
                                    *((unsigned long *)&ptr7->field_30) = v30;
                                    p = &ptr7->field_30;
                                    sub_f7d8d0(p, v30);
                                    v8 = Camera__get_main(0);
                                    if (v8)
                                    {
                                        v8 = Component__get_transform();
                                        if (v8)
                                        {
                                            v33 = sub_1231bc8();
                                            ptr8 = ptr;
                                            ptr8->field_70 = v33;
                                            sub_f7d8d0(&ptr8->field_70, v33);
                                            if (!g_1fab2c9)
                                            {
                                                sub_f7d92c(&g_1ef22e8);
                                                g_1fab2c9 = 1;
                                            }
                                            v8 = ptr->field_78;
                                            v35 = g_1ef22e8->field_b8->field_8;
                                            *((unsigned long long *)&(&ptr->padding_90)[1]) = g_1ef22e8->field_b8->field_0;
                                            *((unsigned int *)((char *)&ptr->field_e4 + 4)) = v35;
                                            if (v8)
                                            {
                                                v36 = sub_124913c(v8, g_1efea78);
                                                ptr11 = &ptr->padding_f0[356];
                                                *((unsigned long *)&ptr->padding_f0[356]) = v36;
                                                sub_f7d8d0(ptr11, v36);
                                                v8 = *((long long *)&ptr->padding_f0[356]);
                                                if (v8)
                                                {
                                                    AudioSource__set_spatialBlend(v8, 0);
                                                    v8 = *((long long *)&ptr11->padding_0[0]);
                                                    if (v8)
                                                    {
                                                        AudioSource__set_playOnAwake(v8, 0, 0);
                                                        v8 = *((long long *)&p->padding_0[0]);
                                                        if (v8)
                                                        {
                                                            Animator__SetBool(v8, g_1f0fb20, 0, 0);
                                                            v8 = *((long long *)&p->padding_0[0]);
                                                            if (v8)
                                                            {
                                                                Animator__SetBool(v8, g_1f0dc18, 0, 0);
                                                                v8 = *((long long *)&p->padding_0[0]);
                                                                if (v8)
                                                                {
                                                                    Animator__SetBool();
                                                                    return;
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
    sub_f7db74(v8);
}
```


## `Ironsights.Update` — RVA `0xcaf2b0`

- Decompiled symbol: `Ironsights_Update`
- Metadata signature: `private void Update() { }`
- Native interval: `9528` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: Decompiler produced no C-like text

```c
// 0x10af2b0: sub sp, sp, #0x90
// 0x10af2b4: stp d15, d14, [sp, #0x20]
// 0x10af2b8: stp d13, d12, [sp, #0x30]
// 0x10af2bc: stp d11, d10, [sp, #0x40]
// 0x10af2c0: stp d9, d8, [sp, #0x50]
// 0x10af2c4: str x30, [sp, #0x60]
// 0x10af2c8: stp x22, x21, [sp, #0x70]
// 0x10af2cc: stp x20, x19, [sp, #0x80]
// 0x10af2d0: adrp x20, #0x1fab000
// 0x10af2d4: ldrb w8, [x20, #0x4ce]
// 0x10af2d8: mov x19, x0
// 0x10af2dc: tbnz w8, #0, #0x10af2f4
// 0x10af2e0: adrp x0, #0x1e8c000
// 0x10af2e4: ldr x0, [x0, #0xd8]
// 0x10af2e8: bl #0xf7d92c
// 0x10af2ec: mov w8, #1
// 0x10af2f0: strb w8, [x20, #0x4ce]
// 0x10af2f4: mov x0, xzr
// 0x10af2f8: bl #0x1b9ae58
// 0x10af2fc: fcmp s0, #0.0
// 0x10af300: b.le #0x10b0c7c
// 0x10af304: mov x0, xzr
// 0x10af308: bl #0x1b89b60
// 0x10af30c: fcmp s0, #0.0
// 0x10af310: b.le #0x10b0c7c
// 0x10af314: mov x0, xzr
// 0x10af318: bl #0x1b9ae30
// 0x10af31c: fcmp s0, #0.0
// 0x10af320: b.le #0x10b0c7c
// 0x10af324: ldr s8, [x19, #0x224]
// 0x10af328: ldr s9, [x19, #0x220]
// 0x10af32c: mov x0, xzr
// 0x10af330: bl #0x1b89b60
// 0x10af334: fsub s1, s9, s8
// 0x10af338: fneg s3, s0
// 0x10af33c: ldr x8, [x19, #0x20]
// 0x10af340: fcmp s1, #0.0
// 0x10af344: fabd s2, s9, s8
// 0x10af348: fcsel s1, s0, s3, ge
// 0x10af34c: fadd s1, s8, s1
// 0x10af350: fcmp s2, s0
// 0x10af354: fcsel s0, s1, s9, hi
// 0x10af358: str s0, [x19, #0x224]
// 0x10af35c: cbz x8, #0x10b17e4
// 0x10af360: ldr s8, [x8, #0x84]
// 0x10af364: mov x0, xzr
// 0x10af368: bl #0x1b9ad30
// 0x10af36c: adrp x8, #0x832000
// 0x10af370: ldr d1, [x8, #0x60]
// 0x10af374: fcvt d2, s8
// 0x10af378: fcvt d0, s0
// 0x10af37c: fadd d1, d2, d1
// 0x10af380: fcmp d1, d0
// 0x10af384: b.mi #0x10af398
// 0x10af388: ldr x8, [x19, #0x40]
// 0x10af38c: cbz x8, #0x10b17e4
// 0x10af390: ldrb w8, [x8, #0x2e8]
// 0x10af394: cbz w8, #0x10af5d4
// 0x10af398: ldr s9, [x19, #0xc0]
// 0x10af39c: ldr s10, [x19, #0xb4]
// 0x10af3a0: ldr s11, [x19, #0x224]
// 0x10af3a4: mov x0, xzr
// 0x10af3a8: add x20, x19, #0xd8
// 0x10af3ac: bl #0x1b89b60
// 0x10af3b0: mov w8, #0x7f800000
// 0x10af3b4: fmov s8, w8
// 0x10af3b8: mov v4.16b, v0.16b
// 0x10af3bc: mov v0.16b, v9.16b
// 0x10af3c0: mov v1.16b, v10.16b
// 0x10af3c4: mov x0, x20
// 0x10af3c8: mov v2.16b, v11.16b
// 0x10af3cc: mov v3.16b, v8.16b
// 0x10af3d0: mov x1, xzr
// 0x10af3d4: bl #0x1b8c860
// 0x10af3d8: ldr s9, [x19, #0xc4]
// 0x10af3dc: ldr s10, [x19, #0xb8]
// 0x10af3e0: ldr s11, [x19, #0x224]
// 0x10af3e4: mov x0, xzr
// 0x10af3e8: str s0, [x19, #0xc0]
// 0x10af3ec: add x20, x19, #0xdc
// 0x10af3f0: bl #0x1b89b60
// 0x10af3f4: mov v4.16b, v0.16b
// 0x10af3f8: mov v0.16b, v9.16b
// 0x10af3fc: mov v1.16b, v10.16b
// 0x10af400: mov x0, x20
// 0x10af404: mov v2.16b, v11.16b
// 0x10af408: mov v3.16b, v8.16b
// 0x10af40c: mov x1, xzr
// 0x10af410: bl #0x1b8c860
// 0x10af414: ldr s9, [x19, #0xc8]
// 0x10af418: ldr s10, [x19, #0xbc]
// 0x10af41c: ldr s11, [x19, #0x228]
// 0x10af420: mov x0, xzr
// 0x10af424: str s0, [x19, #0xc4]
// 0x10af428: add x20, x19, #0xe0
// 0x10af42c: bl #0x1b89b60
// 0x10af430: mov v4.16b, v0.16b
// 0x10af434: mov v0.16b, v9.16b
// 0x10af438: mov v1.16b, v10.16b
// 0x10af43c: mov x0, x20
// 0x10af440: mov v2.16b, v11.16b
// 0x10af444: mov v3.16b, v8.16b
// 0x10af448: mov x1, xzr
// 0x10af44c: bl #0x1b8c860
// 0x10af450: ldp s10, s9, [x19, #0xa8]
// 0x10af454: mov x0, xzr
// 0x10af458: str s0, [x19, #0xc8]
// 0x10af45c: add x20, x19, #0xb0
// 0x10af460: bl #0x1b89b60
// 0x10af464: mov v4.16b, v0.16b
// 0x10af468: fmov s2, #0.25000000
// 0x10af46c: mov v0.16b, v9.16b
// 0x10af470: mov v1.16b, v10.16b
// 0x10af474: mov x0, x20
// 0x10af478: mov v3.16b, v8.16b
// 0x10af47c: mov x1, xzr
// 0x10af480: bl #0x1b8c860
// 0x10af484: str s0, [x19, #0xac]
// 0x10af488: mov x0, xzr
// 0x10af48c: bl #0x1b6f8dc
// 0x10af490: cbz x0, #0x10b17e4
// 0x10af494: mov x1, xzr
// 0x10af498: bl #0x1b6e71c
// 0x10af49c: ldr s9, [x19, #0xfc]
// 0x10af4a0: ldr s10, [x19, #0x104]
// 0x10af4a4: mov x0, xzr
// 0x10af4a8: mov v8.16b, v0.16b
// 0x10af4ac: add x20, x19, #0x108
// 0x10af4b0: bl #0x1b89b60
// 0x10af4b4: mov w8, #0x7f800000
// 0x10af4b8: mov v4.16b, v0.16b
// 0x10af4bc: fmov s3, w8
// 0x10af4c0: mov v0.16b, v8.16b
// 0x10af4c4: mov v1.16b, v9.16b
// 0x10af4c8: mov x0, x20
// 0x10af4cc: mov v2.16b, v10.16b
// 0x10af4d0: mov x1, xzr
// 0x10af4d4: bl #0x1b8c860
// 0x10af4d8: str s0, [x19, #0x100]
// 0x10af4dc: adrp x8, #0x1e8c000
// 0x10af4e0: ldr x8, [x8, #0xd8]
// 0x10af4e4: ldr x20, [x19, #0x90]
// 0x10af4e8: ldr x0, [x8]
// 0x10af4ec: ldr w8, [x0, #0xe0]
// 0x10af4f0: cbnz w8, #0x10af4f8
// 0x10af4f4: bl #0xf7da5c
// 0x10af4f8: mov x0, x20
// 0x10af4fc: mov x1, xzr
// 0x10af500: bl #0x1b98274
// 0x10af504: tbz w0, #0, #0x10af538
// 0x10af508: ldr x20, [x19, #0x90]
// 0x10af50c: mov x0, xzr
// 0x10af510: bl #0x1b6f8dc
// 0x10af514: cbz x0, #0x10b17e4
// 0x10af518: mov x1, xzr
// 0x10af51c: bl #0x1b6e71c
// 0x10af520: cbz x20, #0x10b17e4
// 0x10af524: ldr s1, [x19, #0xf8]
// 0x10af528: mov x0, x20
// 0x10af52c: mov x1, xzr
// 0x10af530: fsub s0, s0, s1
// 0x10af534: bl #0x1b6e758
// 0x10af538: mov x0, xzr
// 0x10af53c: bl #0x1b6f8dc
// 0x10af540: cbz x0, #0x10b17e4
// 0x10af544: ldr s0, [x19, #0x100]
// 0x10af548: mov x1, xzr
// 0x10af54c: bl #0x1b6e758
// 0x10af550: ldr x8, [x19, #0x40]
// 0x10af554: cbz x8, #0x10b17e4
// 0x10af558: ldr x9, [x19, #0x58]
// 0x10af55c: cbz x9, #0x10b17e4
// 0x10af560: ldr s1, [x8, #0xc0]
// 0x10af564: ldr s0, [x8, #0xc4]
// 0x10af568: ldr s8, [x9, #0x1fc]
// 0x10af56c: mov x0, xzr
// 0x10af570: stp s1, s0, [sp, #0x68]
// 0x10af574: bl #0x1b9ad30
// 0x10af578: adrp x8, #0x832000
// 0x10af57c: ldr s1, [x8, #0x3b8]
// 0x10af580: str q1, [sp, #0x10]
// 0x10af584: fadd s1, s8, s1
// 0x10af588: fcmp s1, s0
// 0x10af58c: b.le #0x10af5b0
// 0x10af590: ldr x8, [x19, #0x48]
// 0x10af594: cbz x8, #0x10b17e4
// 0x10af598: ldr x20, [x19, #0x58]
// 0x10af59c: cbz x20, #0x10b17e4
// 0x10af5a0: ldrb w8, [x8, #0x2d0]
// 0x10af5a4: cbz w8, #0x10af5f0
// 0x10af5a8: ldr s0, [x20, #0x5e0]
// 0x10af5ac: b #0x10af5f4
// 0x10af5b0: ldr x20, [x19, #0x58]
// 0x10af5b4: cbz x20, #0x10b17e4
// 0x10af5b8: ldr s1, [x20, #0x1d0]
// 0x10af5bc: fmov s0, wzr
// 0x10af5c0: fcmp s1, #0.0
// 0x10af5c4: b.eq #0x10af5f4
// 0x10af5c8: ldr s0, [x20, #0x1cc]
// 0x10af5cc: fmul s0, s1, s0
// 0x10af5d0: b #0x10af5f4
// 0x10af5d4: ldur d0, [x19, #0xb4]
// 0x10af5d8: ldr s1, [x19, #0xbc]
// 0x10af5dc: ldr s2, [x19, #0xa8]
// 0x10af5e0: str d0, [x19, #0xc0]
// 0x10af5e4: str s1, [x19, #0xc8]
// 0x10af5e8: str s2, [x19, #0xac]
// 0x10af5ec: b #0x10af488
// 0x10af5f0: ldr s0, [x20, #0x5dc]
// 0x10af5f4: ldr x8, [x19, #0x40]
// 0x10af5f8: str s0, [x19, #0xa8]
// 0x10af5fc: cbz x8, #0x10b17e4
// 0x10af600: ldrb w9, [x8, #0x2e8]
// 0x10af604: cbz w9, #0x10af6a0
// 0x10af608: movi d0, #0000000000000000
// 0x10af60c: str d0, [x19, #0x248]
// 0x10af610: ldrb w9, [x8, #0x2b1]
// 0x10af614: cbz w9, #0x10af640
// 0x10af618: ldrb w10, [x8, #0x2d0]
// 0x10af61c: cbnz w10, #0x10af640
// 0x10af620: ldrb w10, [x8, #0x2c2]
// 0x10af624: cbnz w10, #0x10af640
// 0x10af628: ldr s0, [x8, #0x2cc]
// 0x10af62c: ldr s1, [x8, #0x3bc]
// 0x10af630: fcmp s0, s1
// 0x10af634: b.lt #0x10af640
// 0x10af638: ldrb w10, [x8, #0x2dd]
// 0x10af63c: cbnz w10, #0x10af664
// 0x10af640: ldrb w10, [x19, #0x129]
// 0x10af644: cbnz w10, #0x10af68c
// 0x10af648: ldrb w10, [x8, #0x2dd]
// 0x10af64c: cbnz w10, #0x10af68c
// 0x10af650: ldrb w10, [x8, #0x2d0]
// 0x10af654: cbnz w10, #0x10af68c
// 0x10af658: ldrb w10, [x8, #0x2dc]
// 0x10af65c: orr w9, w10, w9
// 0x10af660: cbz w9, #0x10af68c
// 0x10af664: ldr s0, [x8, #0x290]
// 0x10af668: fmov s1, #0.75000000
// 0x10af66c: fcmp s0, s1
// 0x10af670: b.pl #0x10af68c
// 0x10af674: ldr x9, [x19, #0x48]
// 0x10af678: cbz x9, #0x10b17e4
// 0x10af67c: ldrb w9, [x9, #0x2d0]
// 0x10af680: cbnz w9, #0x10af68c
// 0x10af684: ldrb w9, [x8, #0x2a0]
// 0x10af688: cbz w9, #0x10b1274
// 0x10af68c: ldrb w8, [x8, #0x228]
// 0x10af690: cbz w8, #0x10af6fc
// 0x10af694: mov x0, x19
// 0x10af698: bl #0x10b1948
// 0x10af69c: b #0x10af704
// 0x10af6a0: mov x0, x19
// 0x10af6a4: bl #0x10b1898
// 0x10af6a8: ldr s0, [x19, #0xf0]
// 0x10af6ac: ldr x8, [x19, #0x58]
// 0x10af6b0: str s0, [x19, #0xfc]
// 0x10af6b4: cbz x8, #0x10b17e4
// 0x10af6b8: ldr s8, [x19, #0x214]
// 0x10af6bc: ldr s0, [x8, #0x260]
// 0x10af6c0: fcmp s8, #0.0
// 0x10af6c4: str s0, [x19, #0x210]
// 0x10af6c8: b.le #0x10af6e4
// 0x10af6cc: mov x0, xzr
// 0x10af6d0: bl #0x1b89b60
// 0x10af6d4: fmov s1, #-0.25000000
// 0x10af6d8: fmul s0, s0, s1
// 0x10af6dc: fadd s0, s8, s0
// 0x10af6e0: str s0, [x19, #0x214]
// 0x10af6e4: ldrb w8, [x19, #0x129]
// 0x10af6e8: cbz w8, #0x10af7dc
// 0x10af6ec: ldr s0, [x19, #0xf0]
// 0x10af6f0: str wzr, [x19, #0x230]
// 0x10af6f4: str s0, [x19, #0xfc]
// 0x10af6f8: b #0x10af81c
// 0x10af6fc: mov x0, x19
// 0x10af700: bl #0x10b1898
// 0x10af704: ldr s8, [x19, #0x214]
// 0x10af708: mov w8, #0x3f800000
// 0x10af70c: mov x0, xzr
// 0x10af710: str w8, [x19, #0x21c]
// 0x10af714: bl #0x1b89b60
// 0x10af718: fmov s2, wzr
// 0x10af71c: fmov s1, #16.00000000
// 0x10af720: fsub s4, s2, s8
// 0x10af724: ldr x20, [x19, #0x58]
// 0x10af728: fmul s3, s0, s1
// 0x10af72c: fnmul s0, s0, s1
// 0x10af730: fcmp s4, #0.0
// 0x10af734: fabd s5, s2, s8
// 0x10af738: fcsel s0, s3, s0, ge
// 0x10af73c: fadd s0, s8, s0
// 0x10af740: fcmp s5, s3
// 0x10af744: fcsel s0, s0, s2, hi
// 0x10af748: str s0, [x19, #0x214]
// 0x10af74c: cbz x20, #0x10b17e4
// 0x10af750: ldr s1, [x20, #0x260]
// 0x10af754: ldrb w8, [x19, #0x129]
// 0x10af758: ldr s2, [x19, #0xf0]
// 0x10af75c: fadd s0, s0, s1
// 0x10af760: str s0, [x19, #0x210]
// 0x10af764: str s2, [x19, #0xfc]
// 0x10af768: cbz w8, #0x10af778
// 0x10af76c: movi d0, #0000000000000000
// 0x10af770: str d0, [x19, #0x230]
// 0x10af774: b #0x10af94c
// 0x10af778: ldr x8, [x19, #0x48]
// 0x10af77c: cbz x8, #0x10b17e4
// 0x10af780: ldrb w8, [x8, #0x2d0]
// 0x10af784: cbz w8, #0x10af79c
// 0x10af788: ldr s0, [x20, #0x204]
// 0x10af78c: fcmp s0, #0.0
// 0x10af790: b.ne #0x10af79c
// 0x10af794: str wzr, [x19, #0x230]
// 0x10af798: b #0x10af94c
// 0x10af79c: ldr x8, [x19, #0x40]
// 0x10af7a0: cbz x8, #0x10b17e4
// 0x10af7a4: ldrb w9, [x8, #0x2d0]
// 0x10af7a8: cbnz w9, #0x10af7c8
// 0x10af7ac: adrp x9, #0x832000
// 0x10af7b0: ldr s0, [x8, #0x3bc]
// 0x10af7b4: ldr s1, [x9, #0x4a0]
// 0x10af7b8: ldr s2, [x8, #0x2cc]
// 0x10af7bc: fmul s0, s0, s1
// 0x10af7c0: fcmp s2, s0
// 0x10af7c4: b.pl #0x10b1004
// 0x10af7c8: ldr s0, [x20, #0x29c]
// 0x10af7cc: str s0, [x19, #0x230]
// 0x10af7d0: ldr s0, [x20, #0x2a4]
// 0x10af7d4: str s0, [x19, #0x234]
// 0x10af7d8: b #0x10af94c
// 0x10af7dc: ldr x8, [x19, #0x40]
// 0x10af7e0: cbz x8, #0x10b17e4
// 0x10af7e4: ldrb w9, [x8, #0x2d0]
// 0x10af7e8: cbnz w9, #0x10af808
// 0x10af7ec: adrp x9, #0x832000
// 0x10af7f0: ldr s0, [x8, #0x3bc]
// 0x10af7f4: ldr s1, [x9, #0x4a0]
// 0x10af7f8: ldr s2, [x8, #0x2cc]
// 0x10af7fc: fmul s0, s0, s1
// 0x10af800: fcmp s2, s0
// 0x10af804: b.pl #0x10af818
// 0x10af808: ldr x8, [x19, #0x48]
// 0x10af80c: cbz x8, #0x10b17e4
// 0x10af810: ldrb w8, [x8, #0x2d0]
// 0x10af814: cbz w8, #0x10b0fec
// 0x10af818: str wzr, [x19, #0x230]
// 0x10af81c: fmov s0, wzr
// 0x10af820: ldr x8, [x19, #0x48]
// 0x10af824: str s0, [x19, #0x234]
// 0x10af828: cbz x8, #0x10b17e4
// 0x10af82c: ldrb w8, [x8, #0x2d0]
// 0x10af830: cbz w8, #0x10af8a0
// 0x10af834: ldr x8, [x19, #0x58]
// 0x10af838: cbz x8, #0x10b17e4
// 0x10af83c: ldr s0, [x8, #0x204]
// 0x10af840: fcmp s0, #0.0
// 0x10af844: b.ne #0x10af8a0
// 0x10af848: mov x0, xzr
// 0x10af84c: bl #0x1b9ad30
// 0x10af850: ldr x20, [x19, #0x58]
// 0x10af854: cbz x20, #0x10b17e4
// 0x10af858: fmov s1, #1.25000000
// 0x10af85c: fmul s0, s0, s1
// 0x10af860: bl #0x1db0c80
// 0x10af864: adrp x8, #0x832000
// 0x10af868: ldr s8, [x8, #0x4e4]
// 0x10af86c: ldr s1, [x20, #0x340]
// 0x10af870: mov x0, xzr
// 0x10af874: fmul s0, s0, s8
// 0x10af878: fmul s0, s0, s1
// 0x10af87c: str s0, [x19, #0x248]
// 0x10af880: bl #0x1b9ad30
// 0x10af884: ldr x20, [x19, #0x58]
// 0x10af888: cbz x20, #0x10b17e4
// 0x10af88c: fmov s1, #1.50000000
// 0x10af890: fmul s0, s0, s1
// 0x10af894: bl #0x1db0c80
// 0x10af898: ldr s1, [x20, #0x340]
// 0x10af89c: b #0x10af940
// 0x10af8a0: ldr x8, [x19, #0x40]
// 0x10af8a4: cbz x8, #0x10b17e4
// 0x10af8a8: ldrb w20, [x8, #0x258]
// 0x10af8ac: mov x0, xzr
// 0x10af8b0: bl #0x1b9ad30
// 0x10af8b4: fmov s1, #1.25000000
// 0x10af8b8: fmul s0, s0, s1
// 0x10af8bc: bl #0x1db0c80
// 0x10af8c0: ldr x8, [x19, #0x58]
// 0x10af8c4: cbz x8, #0x10b17e4
// 0x10af8c8: cbz w20, #0x10af908
// 0x10af8cc: adrp x9, #0x832000
// 0x10af8d0: ldr s8, [x9, #0x384]
// 0x10af8d4: ldr s1, [x8, #0x33c]
// 0x10af8d8: mov x0, xzr
// 0x10af8dc: fmul s0, s0, s8
// 0x10af8e0: fmul s0, s0, s1
// 0x10af8e4: str s0, [x19, #0x248]
// 0x10af8e8: bl #0x1b9ad30
// 0x10af8ec: ldr x20, [x19, #0x58]
// 0x10af8f0: cbz x20, #0x10b17e4
// 0x10af8f4: fmov s1, #1.50000000
// 0x10af8f8: fmul s0, s0, s1
// 0x10af8fc: bl #0x1db0c80
// 0x10af900: ldr s1, [x20, #0x33c]
// 0x10af904: b #0x10af940
// 0x10af908: adrp x9, #0x832000
// 0x10af90c: ldr s8, [x9, #0x3cc]
// 0x10af910: ldr s1, [x8, #0x338]
// 0x10af914: mov x0, xzr
// 0x10af918: fmul s0, s0, s8
// 0x10af91c: fmul s0, s0, s1
// 0x10af920: str s0, [x19, #0x248]
// 0x10af924: bl #0x1b9ad30
// 0x10af928: ldr x20, [x19, #0x58]
// 0x10af92c: cbz x20, #0x10b17e4
// 0x10af930: fmov s1, #1.50000000
// 0x10af934: fmul s0, s0, s1
// 0x10af938: bl #0x1db0c80
// 0x10af93c: ldr s1, [x20, #0x338]
// 0x10af940: fmul s0, s0, s8
// 0x10af944: fmul s0, s0, s1
// 0x10af948: str s0, [x19, #0x24c]
// 0x10af94c: ldr x8, [x19, #0x28]
// 0x10af950: cbz x8, #0x10b17e4
// 0x10af954: add x21, x19, #0x12c
// 0x10af958: ldr d0, [x8, #0x38]
// 0x10af95c: ldr d1, [x21, #0xa0]
// 0x10af960: ldr d2, [x19, #0xc0]
// 0x10af964: ldr s3, [x19, #0xc8]
// 0x10af968: fmul v0.2s, v0.2s, v1.2s
// 0x10af96c: fadd v0.2s, v2.2s, v0.2s
// 0x10af970: stur d0, [x19, #0xe4]
// 0x10af974: ldr s1, [x19, #0xac]
// 0x10af978: ldr s0, [x8, #0x40]
// 0x10af97c: ldr s2, [x19, #0x1d4]
// 0x10af980: fadd s1, s3, s1
// 0x10af984: fmul s0, s0, s2
// 0x10af988: fsub s0, s1, s0
// 0x10af98c: str s0, [x19, #0xec]
// 0x10af990: ldrb w8, [x20, #0x1f5]
// 0x10af994: cbnz w8, #0x10af9c8
// 0x10af998: mov x0, xzr
// 0x10af99c: bl #0x1b9ad58
// 0x10af9a0: adrp x8, #0x832000
// 0x10af9a4: ldr s1, [x8, #0x550]
// 0x10af9a8: fcmp s0, s1
// 0x10af9ac: b.le #0x10af9c8
// 0x10af9b0: ldr x0, [x19, #0xa0]
// 0x10af9b4: cbz x0, #0x10b17e4
// 0x10af9b8: ldp s1, s2, [x19, #0xe8]
// 0x10af9bc: ldr s0, [x19, #0xe4]
// 0x10af9c0: mov x1, xzr
// 0x10af9c4: bl #0x1b9cba4
// 0x10af9c8: ldr x0, [x19, #0xa0]
// 0x10af9cc: cbz x0, #0x10b17e4
// 0x10af9d0: mov x1, xzr
// 0x10af9d4: bl #0x1b92154
// 0x10af9d8: cbz x0, #0x10b17e4
// 0x10af9dc: mov x1, xzr
// 0x10af9e0: bl #0x1b9d400
// 0x10af9e4: cbz x0, #0x10b17e4
// 0x10af9e8: mov x1, xzr
// 0x10af9ec: bl #0x1b92154
// 0x10af9f0: ldr x8, [x19, #0xa0]
// 0x10af9f4: cbz x8, #0x10b17e4
// 0x10af9f8: mov x20, x0
// 0x10af9fc: mov x0, x8
// 0x10afa00: mov x1, xzr
// 0x10afa04: bl #0x1b92154
// 0x10afa08: cbz x0, #0x10b17e4
// 0x10afa0c: mov x1, xzr
// 0x10afa10: bl #0x1b9d400
// 0x10afa14: cbz x0, #0x10b17e4
// 0x10afa18: mov x1, xzr
// 0x10afa1c: bl #0x1b92154
// 0x10afa20: cbz x0, #0x10b17e4
// 0x10afa24: mov x1, xzr
// 0x10afa28: bl #0x1b9cb18
// 0x10afa2c: adrp x22, #0x1fab000
// 0x10afa30: ldrb w8, [x22, #0x2c9]
// 0x10afa34: mov v8.16b, v0.16b
// 0x10afa38: mov v10.16b, v1.16b
// 0x10afa3c: mov v15.16b, v2.16b
// 0x10afa40: cbnz w8, #0x10afa58
// 0x10afa44: adrp x0, #0x1e8c000
// 0x10afa48: ldr x0, [x0, #0x1e8]
// 0x10afa4c: bl #0xf7d92c
// 0x10afa50: mov w8, #1
// 0x10afa54: strb w8, [x22, #0x2c9]
// 0x10afa58: adrp x8, #0x1e8c000
// 0x10afa5c: ldr x8, [x8, #0x1e8]
// 0x10afa60: mov x0, xzr
// 0x10afa64: ldr x8, [x8]
// 0x10afa68: ldr x8, [x8, #0xb8]
// 0x10afa6c: ldp s11, s12, [x8]
// 0x10afa70: ldr s13, [x8, #8]
// 0x10afa74: bl #0x1b9ae30
// 0x10afa78: adrp x22, #0x1fab000
// 0x10afa7c: ldrb w8, [x22, #0x4d2]
// 0x10afa80: mov v14.16b, v0.16b
// 0x10afa84: cbnz w8, #0x10afa9c
// 0x10afa88: adrp x0, #0x1e8c000
// 0x10afa8c: ldr x0, [x0, #0xa60]
// 0x10afa90: bl #0xf7d92c
// 0x10afa94: mov w8, #1
// 0x10afa98: strb w8, [x22, #0x4d2]
// 0x10afa9c: fsub s9, s11, s8
// 0x10afaa0: mov v2.16b, v8.16b
// 0x10afaa4: fsub s8, s12, s10
// 0x10afaa8: mov v4.16b, v15.16b
// 0x10afaac: fsub s15, s13, s15
// 0x10afab0: fmul s0, s9, s9
// 0x10afab4: fmul s1, s8, s8
// 0x10afab8: fadd s0, s0, s1
// 0x10afabc: fmul s1, s15, s15
// 0x10afac0: mov v3.16b, v10.16b
// 0x10afac4: fadd s10, s1, s0
// 0x10afac8: fcmp s10, #0.0
// 0x10afacc: b.eq #0x10afb44
// 0x10afad0: adrp x8, #0x832000
// 0x10afad4: ldr s0, [x8, #0x538]
// 0x10afad8: stp s4, s3, [sp, #4]
// 0x10afadc: str s2, [sp, #0xc]
// 0x10afae0: fmul s14, s14, s0
// 0x10afae4: fcmp s14, #0.0
// 0x10afae8: b.lt #0x10afaf8
// 0x10afaec: fmul s0, s14, s14
// 0x10afaf0: fcmp s10, s0
// 0x10afaf4: b.ls #0x10afb44
// 0x10afaf8: adrp x8, #0x1e8c000
// 0x10afafc: ldr x8, [x8, #0xa60]
// 0x10afb00: ldr x0, [x8]
// 0x10afb04: ldr w8, [x0, #0xe0]
// 0x10afb08: cbnz w8, #0x10afb10
// 0x10afb0c: bl #0xf7da5c
// 0x10afb10: ldr s3, [sp, #0xc]
// 0x10afb14: fsqrt s0, s10
// 0x10afb18: fdiv s1, s9, s0
// 0x10afb1c: fmul s1, s14, s1
// 0x10afb20: fadd s11, s3, s1
// 0x10afb24: ldr s1, [sp, #8]
// 0x10afb28: fdiv s2, s8, s0
// 0x10afb2c: fmul s2, s14, s2
// 0x10afb30: fdiv s0, s15, s0
// 0x10afb34: fadd s12, s1, s2
// 0x10afb38: ldr s1, [sp, #4]
// 0x10afb3c: fmul s0, s14, s0
// 0x10afb40: fadd s13, s1, s0
// 0x10afb44: cbz x20, #0x10b17e4
// 0x10afb48: mov x0, x20
// 0x10afb4c: mov v0.16b, v11.16b
// 0x10afb50: mov v1.16b, v12.16b
// 0x10afb54: mov v2.16b, v13.16b
// 0x10afb58: mov x1, xzr
// 0x10afb5c: bl #0x1b9cba4
// 0x10afb60: ldr x8, [x19, #0x60]
// 0x10afb64: cbz x8, #0x10b17e4
// 0x10afb68: ldr x9, [x19, #0x28]
// 0x10afb6c: cbz x9, #0x10b17e4
// 0x10afb70: ldr s8, [x19, #0x268]
// 0x10afb74: ldr s9, [x8, #0xb4]
// 0x10afb78: ldr s10, [x9, #0x48]
// 0x10afb7c: ldr s11, [x19, #0x1dc]
// 0x10afb80: mov x0, xzr
// 0x10afb84: add x20, x19, #0x26c
// 0x10afb88: bl #0x1b9ae30
// 0x10afb8c: mov v4.16b, v0.16b
// 0x10afb90: fmov s0, #6.00000000
// 0x10afb94: fmul s1, s10, s11
// 0x10afb98: fmov s2, #6.50000000
// 0x10afb9c: fmul s0, s9, s0
// 0x10afba0: fmul s1, s1, s2
// 0x10afba4: mov w8, #0x43b40000
// 0x10afba8: fadd s0, s0, s1
// 0x10afbac: fmov s3, w8
// 0x10afbb0: fsub s0, s0, s8
// 0x10afbb4: mov w8, #-0x3c4c0000
// 0x10afbb8: fdiv s1, s0, s3
// 0x10afbbc: fmov s2, w8
// 0x10afbc0: frintm s1, s1
// 0x10afbc4: fmul s1, s1, s2
// 0x10afbc8: fadd s0, s0, s1
// 0x10afbcc: fmov s1, wzr
// 0x10afbd0: mov w8, #0x43340000
// 0x10afbd4: fmin s3, s0, s3
// 0x10afbd8: fcmp s0, #0.0
// 0x10afbdc: fmov s0, w8
// 0x10afbe0: fcsel s1, s3, s1, pl
// 0x10afbe4: fadd s2, s1, s2
// 0x10afbe8: fcmp s1, s0
// 0x10afbec: adrp x8, #0x832000
// 0x10afbf0: fcsel s0, s2, s1, gt
// 0x10afbf4: ldr s2, [x8, #0x488]
// 0x10afbf8: mov w8, #0x7f800000
// 0x10afbfc: fadd s1, s8, s0
// 0x10afc00: fmov s3, w8
// 0x10afc04: mov v0.16b, v8.16b
// 0x10afc08: mov x0, x20
// 0x10afc0c: mov x1, xzr
// 0x10afc10: bl #0x1b8c860
// 0x10afc14: ldr x0, [x19, #0xa0]
// 0x10afc18: str s0, [x19, #0x268]
// 0x10afc1c: cbz x0, #0x10b17e4
// 0x10afc20: mov x1, xzr
// 0x10afc24: bl #0x1b92154
// 0x10afc28: cbz x0, #0x10b17e4
// 0x10afc2c: mov x1, xzr
// 0x10afc30: bl #0x1b9d400
// 0x10afc34: cbz x0, #0x10b17e4
// 0x10afc38: mov x1, xzr
// 0x10afc3c: bl #0x1b92154
// 0x10afc40: cbz x0, #0x10b17e4
// 0x10afc44: mov x1, xzr
// 0x10afc48: bl #0x1b9d7c8
// 0x10afc4c: ldr s1, [x19, #0x268]
// 0x10afc50: mov w8, #0x43b40000
// 0x10afc54: fmov s2, w8
// 0x10afc58: mov w9, #-0x3c4c0000
// 0x10afc5c: fsub s0, s1, s0
// 0x10afc60: fdiv s1, s0, s2
// 0x10afc64: fmov s3, w9
// 0x10afc68: frintm s1, s1
// 0x10afc6c: fmul s1, s1, s3
// 0x10afc70: fadd s0, s0, s1
// 0x10afc74: fmov s1, wzr
// 0x10afc78: mov w8, #0x43340000
// 0x10afc7c: fmin s2, s0, s2
// 0x10afc80: fcmp s0, #0.0
// 0x10afc84: ldr x0, [x19, #0xa0]
// 0x10afc88: fmov s0, w8
// 0x10afc8c: fcsel s1, s2, s1, pl
// 0x10afc90: fadd s2, s1, s3
// 0x10afc94: fcmp s1, s0
// 0x10afc98: fcsel s0, s2, s1, gt
// 0x10afc9c: str s0, [x19, #0x270]
// 0x10afca0: cbz x0, #0x10b17e4
// 0x10afca4: mov x1, xzr
// 0x10afca8: bl #0x1b92154
// 0x10afcac: cbz x0, #0x10b17e4
// 0x10afcb0: mov x1, xzr
// 0x10afcb4: bl #0x1b9d400
// 0x10afcb8: cbz x0, #0x10b17e4
// 0x10afcbc: mov x1, xzr
// 0x10afcc0: bl #0x1b92154
// 0x10afcc4: ldr x8, [x19, #0x260]
// 0x10afcc8: cbz x8, #0x10b17e4
// 0x10afccc: mov x20, x0
// 0x10afcd0: mov x0, x8
// 0x10afcd4: mov x1, xzr
// 0x10afcd8: bl #0x1b9d508
// 0x10afcdc: ldr x0, [x19, #0xa0]
// 0x10afce0: cbz x0, #0x10b17e4
// 0x10afce4: mov x1, xzr
// 0x10afce8: mov v8.16b, v0.16b
// 0x10afcec: mov v9.16b, v1.16b
// 0x10afcf0: mov v10.16b, v2.16b
// 0x10afcf4: bl #0x1b92154
// 0x10afcf8: cbz x0, #0x10b17e4
// 0x10afcfc: mov x1, xzr
// 0x10afd00: bl #0x1b9d400
// 0x10afd04: cbz x0, #0x10b17e4
// 0x10afd08: mov x1, xzr
// 0x10afd0c: bl #0x1b92154
// 0x10afd10: cbz x0, #0x10b17e4
// 0x10afd14: mov x1, xzr
// 0x10afd18: bl #0x1b9d8c8
// 0x10afd1c: cbz x20, #0x10b17e4
// 0x10afd20: ldr s6, [x19, #0x270]
// 0x10afd24: mov v3.16b, v0.16b
// 0x10afd28: mov v4.16b, v1.16b
// 0x10afd2c: mov v5.16b, v2.16b
// 0x10afd30: mov x0, x20
// 0x10afd34: mov v0.16b, v8.16b
// 0x10afd38: mov v1.16b, v9.16b
// 0x10afd3c: mov v2.16b, v10.16b
// 0x10afd40: mov x1, xzr
// 0x10afd44: bl #0x1b9e490
// 0x10afd48: ldr x8, [x19, #0x40]
// 0x10afd4c: cbz x8, #0x10b17e4
// 0x10afd50: ldrb w9, [x8, #0x2a0]
// 0x10afd54: cbnz w9, #0x10afd68
// 0x10afd58: ldr s0, [x8, #0x290]
// 0x10afd5c: fmov s1, #1.25000000
// 0x10afd60: fcmp s0, s1
// 0x10afd64: b.le #0x10afdb0
// 0x10afd68: ldr x9, [x19, #0x48]
// 0x10afd6c: cbz x9, #0x10b17e4
// 0x10afd70: ldrb w9, [x9, #0x2d0]
// 0x10afd74: cbz w9, #0x10afd84
// 0x10afd78: mov w8, #0xd70a
// 0x10afd7c: movk w8, #0xbc23, lsl #16
// 0x10afd80: b #0x10afdc0
// 0x10afd84: ldr s8, [x8, #0x27c]
// 0x10afd88: mov x0, xzr
// 0x10afd8c: bl #0x1b9ad30
// 0x10afd90: adrp x8, #0x832000
// 0x10afd94: ldr s1, [x8, #0x48c]
// 0x10afd98: fadd s1, s8, s1
// 0x10afd9c: fcmp s1, s0
// 0x10afda0: b.le #0x10afdb8
// 0x10afda4: mov w8, #0xc28f
// 0x10afda8: movk w8, #0x3c75, lsl #16
// 0x10afdac: b #0x10afdc0
// 0x10afdb0: str wzr, [x19, #0x240]
// 0x10afdb4: b #0x10afdc4
// 0x10afdb8: mov w8, #0xcccd
// 0x10afdbc: movk w8, #0xbccc, lsl #16
// 0x10afdc0: str w8, [x19, #0x240]
// 0x10afdc4: ldr x8, [x19, #0x40]
// 0x10afdc8: cbz x8, #0x10b17e4
// 0x10afdcc: ldrb w9, [x8, #0x258]
// 0x10afdd0: fmov s8, #1.00000000
// 0x10afdd4: fmov s0, #1.00000000
// 0x10afdd8: cbz w9, #0x10afdec
// 0x10afddc: adrp x9, #0x832000
// 0x10afde0: ldr s0, [x19, #0x1a8]
// 0x10afde4: ldr s1, [x9, #0x4e0]
// 0x10afde8: fmax s0, s0, s1
// 0x10afdec: str s0, [x19, #0x1ac]
// 0x10afdf0: ldrb w9, [x8, #0x2b1]
// 0x10afdf4: cbnz w9, #0x10afe30
// 0x10afdf8: ldr x9, [x19, #0x50]
// 0x10afdfc: cbz x9, #0x10b17e4
// 0x10afe00: ldp s0, s1, [x8, #0xc0]
// 0x10afe04: ldr s2, [x9, #0xc8]
// 0x10afe08: fmov s3, #1.00000000
// 0x10afe0c: fabs s1, s1
// 0x10afe10: fabs s0, s0
// 0x10afe14: fadd s1, s1, s2
// 0x10afe18: fcmp s0, s1
// 0x10afe1c: fcsel s0, s0, s1, gt
// 0x10afe20: fmin s1, s0, s3
// 0x10afe24: fcmp s0, #0.0
// 0x10afe28: fmov s0, wzr
// 0x10afe2c: fcsel s8, s1, s0, pl
// 0x10afe30: ldr s9, [x19, #0x1b0]
// 0x10afe34: mov x0, xzr
// 0x10afe38: str s8, [x19, #0x1b4]
// 0x10afe3c: bl #0x1b89b60
// 0x10afe40: fmov s1, #3.50000000
// 0x10afe44: fsub s2, s8, s9
// 0x10afe48: ldr x8, [x19, #0x48]
// 0x10afe4c: fmul s4, s0, s1
// 0x10afe50: fnmul s0, s0, s1
// 0x10afe54: fcmp s2, #0.0
// 0x10afe58: fabd s3, s8, s9
// 0x10afe5c: fcsel s0, s4, s0, ge
// 0x10afe60: fadd s0, s9, s0
// 0x10afe64: fcmp s3, s4
// 0x10afe68: fcsel s0, s0, s8, hi
// 0x10afe6c: str s0, [x19, #0x1b0]
// 0x10afe70: cbz x8, #0x10b17e4
// 0x10afe74: ldrb w9, [x8, #0x2d0]
// 0x10afe78: cbz w9, #0x10b037c
// 0x10afe7c: ldr s0, [x8, #0x20c]
// 0x10afe80: fmov s1, #1.00000000
// 0x10afe84: fcmp s0, s1
// 0x10afe88: b.le #0x10b0394
// 0x10afe8c: ldr x8, [x19, #0x38]
// 0x10afe90: cbz x8, #0x10b17e4
// 0x10afe94: ldr x9, [x19, #0x58]
// 0x10afe98: cbz x9, #0x10b17e4
// 0x10afe9c: ldr s8, [x8, #0x120]
// 0x10afea0: ldr s9, [x9, #0x3d4]
// 0x10afea4: mov x0, xzr
// 0x10afea8: bl #0x1b9ad30
// 0x10afeac: fadd s1, s8, s9
// 0x10afeb0: fcmp s1, s0
// 0x10afeb4: b.pl #0x10b0394
// 0x10afeb8: ldrb w8, [x19, #0x129]
// 0x10afebc: cbnz w8, #0x10b0394
// 0x10afec0: ldr x8, [x19, #0x38]
// 0x10afec4: cbz x8, #0x10b17e4
// 0x10afec8: ldr w8, [x8, #0xdc]
// 0x10afecc: cbz w8, #0x10b0394
// 0x10afed0: ldr x8, [x19, #0x48]
// 0x10afed4: cbz x8, #0x10b17e4
// 0x10afed8: ldrb w9, [x8, #0x460]
// 0x10afedc: ldr x8, [x19, #0x58]
// 0x10afee0: cbz w9, #0x10b1014
// 0x10afee4: cbz x8, #0x10b17e4
// 0x10afee8: ldr s8, [x8, #0x3e8]
// 0x10afeec: ldr s9, [x8, #0x3e4]
// 0x10afef0: mov x0, xzr
// 0x10afef4: bl #0x1b9ad30
// 0x10afef8: fadd s1, s8, s9
// 0x10afefc: fcmp s1, s0
// 0x10aff00: b.pl #0x10b0394
// 0x10aff04: ldrb w9, [x19, #0x10c]
// 0x10aff08: ldrb w8, [x19, #0x129]
// 0x10aff0c: ldr s8, [x19, #0x208]
// 0x10aff10: fmov s9, wzr
// 0x10aff14: cbz w9, #0x10b1050
// 0x10aff18: cbnz w8, #0x10aff28
// 0x10aff1c: ldr x8, [x19, #0x58]
// 0x10aff20: cbz x8, #0x10b17e4
// 0x10aff24: ldr s9, [x8, #0x360]
// 0x10aff28: mov x0, xzr
// 0x10aff2c: bl #0x1b89b60
// 0x10aff30: fmov s1, #16.00000000
// 0x10aff34: fsub s2, s9, s8
// 0x10aff38: ldr x8, [x19, #0x40]
// 0x10aff3c: fmul s4, s0, s1
// 0x10aff40: fnmul s0, s0, s1
// 0x10aff44: fcmp s2, #0.0
// 0x10aff48: fabd s3, s9, s8
// 0x10aff4c: fcsel s0, s4, s0, ge
// 0x10aff50: fadd s0, s8, s0
// 0x10aff54: fcmp s3, s4
// 0x10aff58: fcsel s0, s0, s9, hi
// 0x10aff5c: str s0, [x19, #0x208]
// 0x10aff60: cbz x8, #0x10b17e4
// 0x10aff64: ldr s3, [x19, #0x248]
// 0x10aff68: ldr s4, [x19, #0x250]
// 0x10aff6c: ldr s5, [x8, #0x170]
// 0x10aff70: ldr s6, [x8, #0xc0]
// 0x10aff74: mov w8, #0x42700000
// 0x10aff78: ldr s2, [x19, #0x234]
// 0x10aff7c: fadd s3, s3, s4
// 0x10aff80: fmov s4, w8
// 0x10aff84: ldr s1, [x19, #0x210]
// 0x10aff88: fdiv s4, s5, s4
// 0x10aff8c: ldr q5, [sp, #0x10]
// 0x10aff90: ldr x8, [x19, #0x58]
// 0x10aff94: fadd s2, s2, s3
// 0x10aff98: fadd s1, s1, s2
// 0x10aff9c: fmul s5, s6, s5
// 0x10affa0: fadd s1, s4, s1
// 0x10affa4: fmul s0, s5, s0
// 0x10affa8: fadd s0, s1, s0
// 0x10affac: str s0, [x19, #0xb4]
// 0x10affb0: cbz x8, #0x10b17e4
// 0x10affb4: ldr s2, [x19, #0x23c]
// 0x10affb8: ldr s5, [x19, #0x230]
// 0x10affbc: ldr s6, [x19, #0x238]
// 0x10affc0: ldr s1, [x19, #0x244]
// 0x10affc4: ldr s0, [x19, #0x240]
// 0x10affc8: ldr s3, [x19, #0x24c]
// 0x10affcc: ldr s4, [x19, #0x254]
// 0x10affd0: fadd s2, s2, s5
// 0x10affd4: ldr s7, [x8, #0x264]
// 0x10affd8: fadd s2, s6, s2
// 0x10affdc: fadd s1, s1, s2
// 0x10affe0: fadd s3, s3, s4
// 0x10affe4: fadd s0, s0, s1
// 0x10affe8: fadd s0, s3, s0
// 0x10affec: fadd s0, s7, s0
// 0x10afff0: str s0, [x19, #0xb8]
// 0x10afff4: ldr s0, [x8, #0x268]
// 0x10afff8: str s0, [x19, #0xbc]
// 0x10afffc: ldr s0, [x8, #0x254]
// 0x10b0000: str s0, [x19, #0xfc]
// 0x10b0004: mov w9, #0x51ec
// 0x10b0008: ldr x8, [x19, #0x48]
// 0x10b000c: movk w9, #0x3db8, lsl #16
// 0x10b0010: str w9, [x19, #0x104]
// 0x10b0014: str w9, [x19, #0x220]
// 0x10b0018: mov w9, #0x999a
// 0x10b001c: movk w9, #0x3e19, lsl #16
// 0x10b0020: str w9, [x19, #0x228]
// 0x10b0024: cbz x8, #0x10b17e4
// 0x10b0028: ldrb w8, [x8, #0x460]
// 0x10b002c: cbnz w8, #0x10b0c7c
// 0x10b0030: ldr x8, [x19, #0x40]
// 0x10b0034: cbz x8, #0x10b17e4
// 0x10b0038: mov w9, #1
// 0x10b003c: strb w9, [x8, #0x114]
// 0x10b0040: ldr x8, [x19, #0x58]
// 0x10b0044: cbz x8, #0x10b17e4
// 0x10b0048: ldrb w9, [x8, #0x239]
// 0x10b004c: cbnz w9, #0x10b0068
// 0x10b0050: ldr x9, [x19, #0x20]
// 0x10b0054: cbz x9, #0x10b17e4
// 0x10b0058: ldr s0, [x9, #0x38]
// 0x10b005c: ldr s1, [x8, #0x258]
// 0x10b0060: fmul s0, s0, s1
// 0x10b0064: str s0, [x9, #0x3c]
// 0x10b0068: ldr d9, [x19, #0x1b8]
// 0x10b006c: ldr d10, [x21, #0x60]
// 0x10b0070: mov x0, xzr
// 0x10b0074: bl #0x1b9ae30
// 0x10b0078: adrp x20, #0x1fab000
// 0x10b007c: ldrb w8, [x20, #0x4d3]
// 0x10b0080: mov v8.16b, v0.16b
// 0x10b0084: cbnz w8, #0x10b009c
// 0x10b0088: adrp x0, #0x1e8c000
// 0x10b008c: ldr x0, [x0, #0xa60]
// 0x10b0090: bl #0xf7d92c
// 0x10b0094: mov w8, #1
// 0x10b0098: strb w8, [x20, #0x4d3]
// 0x10b009c: fsub v11.2s, v10.2s, v9.2s
// 0x10b00a0: fmul v0.2s, v11.2s, v11.2s
// 0x10b00a4: faddp s12, v0.2s
// 0x10b00a8: fcmp s12, #0.0
// 0x10b00ac: b.eq #0x10b0100
// 0x10b00b0: fmov s0, #24.00000000
// 0x10b00b4: fmul s1, s8, s0
// 0x10b00b8: fcmp s1, #0.0
// 0x10b00bc: b.lt #0x10b00cc
// 0x10b00c0: fmul s0, s1, s1
// 0x10b00c4: fcmp s12, s0
// 0x10b00c8: b.ls #0x10b0100
// 0x10b00cc: adrp x8, #0x1e8c000
// 0x10b00d0: ldr x8, [x8, #0xa60]
// 0x10b00d4: ldr x0, [x8]
// 0x10b00d8: ldr w8, [x0, #0xe0]
// 0x10b00dc: cbnz w8, #0x10b00ec
// 0x10b00e0: str q1, [sp, #0x10]
// 0x10b00e4: bl #0xf7da5c
// 0x10b00e8: ldr q1, [sp, #0x10]
// 0x10b00ec: fsqrt s0, s12
// 0x10b00f0: dup v0.2s, v0.s[0]
// 0x10b00f4: fdiv v0.2s, v11.2s, v0.2s
// 0x10b00f8: fmul v0.2s, v0.2s, v1.s[0]
// 0x10b00fc: fadd v10.2s, v9.2s, v0.2s
// 0x10b0100: str d10, [x19, #0x1b8]
// 0x10b0104: ldr d9, [x19, #0x1c0]
// 0x10b0108: ldr s10, [x19, #0x1c8]
// 0x10b010c: ldr d11, [x21, #0x68]
// 0x10b0110: ldr s12, [x19, #0x19c]
// 0x10b0114: mov x0, xzr
// 0x10b0118: bl #0x1b9ae30
// 0x10b011c: ldrb w8, [x22, #0x4d2]
// 0x10b0120: mov v8.16b, v0.16b
// 0x10b0124: cbnz w8, #0x10b013c
// 0x10b0128: adrp x0, #0x1e8c000
// 0x10b012c: ldr x0, [x0, #0xa60]
// 0x10b0130: bl #0xf7d92c
// 0x10b0134: mov w8, #1
// 0x10b0138: strb w8, [x22, #0x4d2]
// 0x10b013c: fsub v13.2s, v11.2s, v9.2s
// 0x10b0140: fsub s14, s12, s10
// 0x10b0144: fmul v0.2s, v13.2s, v13.2s
// 0x10b0148: faddp s0, v0.2s
// 0x10b014c: fmul s1, s14, s14
// 0x10b0150: fadd s15, s1, s0
// 0x10b0154: fcmp s15, #0.0
// 0x10b0158: b.eq #0x10b01b8
// 0x10b015c: fmov s0, #24.00000000
// 0x10b0160: fmul s2, s8, s0
// 0x10b0164: fcmp s2, #0.0
// 0x10b0168: b.lt #0x10b0178
// 0x10b016c: fmul s0, s2, s2
// 0x10b0170: fcmp s15, s0
// 0x10b0174: b.ls #0x10b01b8
// 0x10b0178: adrp x8, #0x1e8c000
// 0x10b017c: ldr x8, [x8, #0xa60]
// 0x10b0180: ldr x0, [x8]
// 0x10b0184: ldr w8, [x0, #0xe0]
// 0x10b0188: cbnz w8, #0x10b0198
// 0x10b018c: str q2, [sp, #0x10]
// 0x10b0190: bl #0xf7da5c
// 0x10b0194: ldr q2, [sp, #0x10]
// 0x10b0198: fsqrt s0, s15
// 0x10b019c: dup v1.2s, v0.s[0]
// 0x10b01a0: fdiv s0, s14, s0
// 0x10b01a4: fdiv v1.2s, v13.2s, v1.2s
// 0x10b01a8: fmul s0, s2, s0
// 0x10b01ac: fmul v1.2s, v1.2s, v2.s[0]
// 0x10b01b0: fadd v11.2s, v9.2s, v1.2s
// 0x10b01b4: fadd s12, s10, s0
// 0x10b01b8: ldr x8, [x19, #0x58]
// 0x10b01bc: str d11, [x19, #0x1c0]
// 0x10b01c0: str s12, [x19, #0x1c8]
// 0x10b01c4: cbz x8, #0x10b17e4
// 0x10b01c8: add x8, x8, #0x2f4
// 0x10b01cc: ldr d9, [x21, #0xa0]
// 0x10b01d0: ldr s10, [x19, #0x1d4]
// 0x10b01d4: ldr d12, [x8]
// 0x10b01d8: ldr s11, [x8, #8]
// 0x10b01dc: mov x0, xzr
// 0x10b01e0: bl #0x1b9ae30
// 0x10b01e4: ldrb w8, [x22, #0x4d2]
// 0x10b01e8: mov v8.16b, v0.16b
// 0x10b01ec: cbnz w8, #0x10b0204
// 0x10b01f0: adrp x0, #0x1e8c000
// 0x10b01f4: ldr x0, [x0, #0xa60]
// 0x10b01f8: bl #0xf7d92c
// 0x10b01fc: mov w8, #1
// 0x10b0200: strb w8, [x22, #0x4d2]
// 0x10b0204: fsub v13.2s, v12.2s, v9.2s
// 0x10b0208: fsub s14, s11, s10
// 0x10b020c: fmul v0.2s, v13.2s, v13.2s
// 0x10b0210: faddp s0, v0.2s
// 0x10b0214: fmul s1, s14, s14
// 0x10b0218: fadd s15, s1, s0
// 0x10b021c: fcmp s15, #0.0
// 0x10b0220: b.eq #0x10b0280
// 0x10b0224: fmov s0, #24.00000000
// 0x10b0228: fmul s2, s8, s0
// 0x10b022c: fcmp s2, #0.0
// 0x10b0230: b.lt #0x10b0240
// 0x10b0234: fmul s0, s2, s2
// 0x10b0238: fcmp s15, s0
// 0x10b023c: b.ls #0x10b0280
// 0x10b0240: adrp x8, #0x1e8c000
// 0x10b0244: ldr x8, [x8, #0xa60]
// 0x10b0248: ldr x0, [x8]
// 0x10b024c: ldr w8, [x0, #0xe0]
// 0x10b0250: cbnz w8, #0x10b0260
// 0x10b0254: str q2, [sp, #0x10]
// 0x10b0258: bl #0xf7da5c
// 0x10b025c: ldr q2, [sp, #0x10]
// 0x10b0260: fsqrt s0, s15
// 0x10b0264: dup v1.2s, v0.s[0]
// 0x10b0268: fdiv s0, s14, s0
// 0x10b026c: fdiv v1.2s, v13.2s, v1.2s
// 0x10b0270: fmul s0, s2, s0
// 0x10b0274: fmul v1.2s, v1.2s, v2.s[0]
// 0x10b0278: fadd v12.2s, v9.2s, v1.2s
// 0x10b027c: fadd s11, s10, s0
// 0x10b0280: str d12, [x21, #0xa0]
// 0x10b0284: ldr x8, [x19, #0x58]
// 0x10b0288: str s11, [x19, #0x1d4]
// 0x10b028c: cbz x8, #0x10b17e4
// 0x10b0290: ldr d9, [x19, #0x1d8]
// 0x10b0294: ldr s10, [x19, #0x1e0]
// 0x10b0298: ldr d11, [x8, #0x2e8]
// 0x10b029c: ldr s12, [x8, #0x2f0]
// 0x10b02a0: mov x0, xzr
// 0x10b02a4: bl #0x1b9ae30
// 0x10b02a8: ldrb w8, [x22, #0x4d2]
// 0x10b02ac: mov v8.16b, v0.16b
// 0x10b02b0: cbnz w8, #0x10b02c8
// 0x10b02b4: adrp x0, #0x1e8c000
// 0x10b02b8: ldr x0, [x0, #0xa60]
// 0x10b02bc: bl #0xf7d92c
// 0x10b02c0: mov w8, #1
// 0x10b02c4: strb w8, [x22, #0x4d2]
// 0x10b02c8: fsub v13.2s, v11.2s, v9.2s
// 0x10b02cc: fsub s14, s12, s10
// 0x10b02d0: fmul v0.2s, v13.2s, v13.2s
// 0x10b02d4: faddp s0, v0.2s
// 0x10b02d8: fmul s1, s14, s14
// 0x10b02dc: fadd s15, s1, s0
// 0x10b02e0: fcmp s15, #0.0
// 0x10b02e4: b.eq #0x10b0344
// 0x10b02e8: fmov s0, #24.00000000
// 0x10b02ec: fmul s2, s8, s0
// 0x10b02f0: fcmp s2, #0.0
// 0x10b02f4: b.lt #0x10b0304
// 0x10b02f8: fmul s0, s2, s2
// 0x10b02fc: fcmp s15, s0
// 0x10b0300: b.ls #0x10b0344
// 0x10b0304: adrp x8, #0x1e8c000
// 0x10b0308: ldr x8, [x8, #0xa60]
// 0x10b030c: ldr x0, [x8]
// 0x10b0310: ldr w8, [x0, #0xe0]
// 0x10b0314: cbnz w8, #0x10b0324
// 0x10b0318: str q2, [sp, #0x10]
// 0x10b031c: bl #0xf7da5c
// 0x10b0320: ldr q2, [sp, #0x10]
// 0x10b0324: fsqrt s0, s15
// 0x10b0328: dup v1.2s, v0.s[0]
// 0x10b032c: fdiv s0, s14, s0
// 0x10b0330: fdiv v1.2s, v13.2s, v1.2s
// 0x10b0334: fmul s0, s2, s0
// 0x10b0338: fmul v1.2s, v1.2s, v2.s[0]
// 0x10b033c: fadd v11.2s, v9.2s, v1.2s
// 0x10b0340: fadd s12, s10, s0
// 0x10b0344: ldr x8, [x19, #0x40]
// 0x10b0348: str d11, [x19, #0x1d8]
// 0x10b034c: str s12, [x19, #0x1e0]
// 0x10b0350: cbz x8, #0x10b17e4
// 0x10b0354: ldr x20, [x19, #0x30]
// 0x10b0358: cbz x20, #0x10b17e4
// 0x10b035c: ldrb w21, [x8, #0x2d0]
// 0x10b0360: mov x0, x20
// 0x10b0364: mov x1, xzr
// 0x10b0368: bl #0x1b67e78
// 0x10b036c: mov v8.16b, v0.16b
// 0x10b0370: cbz w21, #0x10b1148
// 0x10b0374: ldr s9, [x19, #0x1a4]
// 0x10b0378: b #0x10b114c
// 0x10b037c: ldrb w9, [x8, #0x460]
// 0x10b0380: cbz w9, #0x10b0394
// 0x10b0384: ldr x9, [x19, #0x58]
// 0x10b0388: cbz x9, #0x10b17e4
// 0x10b038c: ldrb w9, [x9, #0x3a5]
// 0x10b0390: cbz w9, #0x10afe7c
// 0x10b0394: ldr x8, [x19, #0x38]
// 0x10b0398: mov w9, #0x51ec
// 0x10b039c: movk w9, #0x3e38, lsl #16
// 0x10b03a0: str w9, [x19, #0x104]
// 0x10b03a4: cbz x8, #0x10b17e4
// 0x10b03a8: ldrb w8, [x8, #0x128]
// 0x10b03ac: adrp x9, #0x832000
// 0x10b03b0: add x9, x9, #0x230
// 0x10b03b4: cmp w8, #0
// 0x10b03b8: cset w8, eq
// 0x10b03bc: ldr s0, [x9, w8, uxtw #2]
// 0x10b03c0: ldr x8, [x19, #0x40]
// 0x10b03c4: mov w9, #0xcccd
// 0x10b03c8: movk w9, #0x3dcc, lsl #16
// 0x10b03cc: str s0, [x19, #0x220]
// 0x10b03d0: str w9, [x19, #0x228]
// 0x10b03d4: cbz x8, #0x10b17e4
// 0x10b03d8: ldr s2, [x19, #0x248]
// 0x10b03dc: ldr s3, [x19, #0x250]
// 0x10b03e0: ldr s4, [x8, #0x170]
// 0x10b03e4: mov w9, #0x42700000
// 0x10b03e8: ldr s1, [x19, #0x234]
// 0x10b03ec: fadd s2, s2, s3
// 0x10b03f0: fmov s3, w9
// 0x10b03f4: ldr s0, [x19, #0x210]
// 0x10b03f8: ldr s5, [x8, #0xc0]
// 0x10b03fc: fdiv s3, s4, s3
// 0x10b0400: ldr q4, [sp, #0x10]
// 0x10b0404: ldr s6, [x19, #0x208]
// 0x10b0408: ldr x9, [x19, #0x58]
// 0x10b040c: fadd s1, s1, s2
// 0x10b0410: fmul s4, s5, s4
// 0x10b0414: fadd s0, s0, s1
// 0x10b0418: fadd s0, s3, s0
// 0x10b041c: fmul s1, s4, s6
// 0x10b0420: fadd s0, s0, s1
// 0x10b0424: str s0, [x19, #0xb4]
// 0x10b0428: cbz x9, #0x10b17e4
// 0x10b042c: ldr s2, [x19, #0x23c]
// 0x10b0430: ldr s5, [x19, #0x230]
// 0x10b0434: ldr s6, [x19, #0x238]
// 0x10b0438: ldr s1, [x19, #0x244]
// 0x10b043c: ldr s0, [x19, #0x240]
// 0x10b0440: ldr s3, [x19, #0x24c]
// 0x10b0444: ldr s4, [x19, #0x254]
// 0x10b0448: fadd s2, s2, s5
// 0x10b044c: ldr s7, [x9, #0x264]
// 0x10b0450: fadd s2, s6, s2
// 0x10b0454: fadd s1, s1, s2
// 0x10b0458: fadd s3, s3, s4
// 0x10b045c: fadd s0, s0, s1
// 0x10b0460: fadd s0, s3, s0
// 0x10b0464: fadd s0, s7, s0
// 0x10b0468: str s0, [x19, #0xb8]
// 0x10b046c: ldr s0, [x9, #0x268]
// 0x10b0470: str s0, [x19, #0xbc]
// 0x10b0474: strb wzr, [x8, #0x114]
// 0x10b0478: ldrb w8, [x19, #0x128]
// 0x10b047c: cbz w8, #0x10b088c
// 0x10b0480: ldr x8, [x19, #0x20]
// 0x10b0484: cbz x8, #0x10b17e4
// 0x10b0488: ldr s0, [x8, #0x38]
// 0x10b048c: str s0, [x8, #0x3c]
// 0x10b0490: ldr x8, [x19, #0x40]
// 0x10b0494: cbz x8, #0x10b17e4
// 0x10b0498: ldrb w9, [x8, #0x2b1]
// 0x10b049c: cbz w9, #0x10b0528
// 0x10b04a0: ldr s0, [sp, #0x6c]
// 0x10b04a4: ldrb w9, [x8, #0x146]
// 0x10b04a8: fmov s1, #0.75000000
// 0x10b04ac: fabs s0, s0
// 0x10b04b0: fcmp s0, s1
// 0x10b04b4: b.pl #0x10b04c8
// 0x10b04b8: ldr s0, [sp, #0x68]
// 0x10b04bc: fcmp s0, #0.0
// 0x10b04c0: b.eq #0x10b04c8
// 0x10b04c4: cbnz w9, #0x10b0528
// 0x10b04c8: ldr s0, [sp, #0x6c]
// 0x10b04cc: fcmp s0, #0.0
// 0x10b04d0: b.ne #0x10b04e0
// 0x10b04d4: cbnz w9, #0x10b0528
// 0x10b04d8: ldrb w9, [x8, #0x2e8]
// 0x10b04dc: cbz w9, #0x10b0528
// 0x10b04e0: ldrb w9, [x8, #0x2c2]
// 0x10b04e4: cbnz w9, #0x10b0528
// 0x10b04e8: ldrb w9, [x8, #0x2d0]
// 0x10b04ec: cbnz w9, #0x10b0528
// 0x10b04f0: ldrb w9, [x8, #0x2dc]
// 0x10b04f4: cbnz w9, #0x10b0528
// 0x10b04f8: ldr s0, [x8, #0x2cc]
// 0x10b04fc: ldr s1, [x8, #0x3bc]
// 0x10b0500: fcmp s0, s1
// 0x10b0504: b.lt #0x10b0528
// 0x10b0508: ldr x8, [x19, #0x48]
// 0x10b050c: cbz x8, #0x10b17e4
// 0x10b0510: ldrb w8, [x8, #0x2d0]
// 0x10b0514: cbnz w8, #0x10b0528
// 0x10b0518: ldr x8, [x19, #0x50]
// 0x10b051c: cbz x8, #0x10b17e4
// 0x10b0520: ldrb w8, [x8, #0x89]
// 0x10b0524: cbz w8, #0x10b12cc
// 0x10b0528: ldrb w8, [x19, #0x129]
// 0x10b052c: ldr s8, [x19, #0x208]
// 0x10b0530: fmov s9, wzr
// 0x10b0534: cbnz w8, #0x10b0544
// 0x10b0538: ldr x8, [x19, #0x58]
// 0x10b053c: cbz x8, #0x10b17e4
// 0x10b0540: ldr s9, [x8, #0x35c]
// 0x10b0544: mov x0, xzr
// 0x10b0548: bl #0x1b89b60
// 0x10b054c: fmov s1, #16.00000000
// 0x10b0550: fsub s2, s9, s8
// 0x10b0554: ldr x8, [x19, #0x40]
// 0x10b0558: fmul s4, s0, s1
// 0x10b055c: fnmul s0, s0, s1
// 0x10b0560: fcmp s2, #0.0
// 0x10b0564: fabd s3, s9, s8
// 0x10b0568: fcsel s0, s4, s0, ge
// 0x10b056c: fadd s0, s8, s0
// 0x10b0570: fcmp s3, s4
// 0x10b0574: fcsel s0, s0, s9, hi
// 0x10b0578: str s0, [x19, #0x208]
// 0x10b057c: cbz x8, #0x10b17e4
// 0x10b0580: ldrb w9, [x8, #0x2d0]
// 0x10b0584: cbz w9, #0x10b0900
// 0x10b0588: ldr d9, [x19, #0x1b8]
// 0x10b058c: ldr d10, [x21, #0x30]
// 0x10b0590: mov x0, xzr
// 0x10b0594: bl #0x1b9ae30
// 0x10b0598: adrp x20, #0x1fab000
// 0x10b059c: ldrb w8, [x20, #0x4d3]
// 0x10b05a0: mov v8.16b, v0.16b
// 0x10b05a4: cbnz w8, #0x10b05bc
// 0x10b05a8: adrp x0, #0x1e8c000
// 0x10b05ac: ldr x0, [x0, #0xa60]
// 0x10b05b0: bl #0xf7d92c
// 0x10b05b4: mov w8, #1
// 0x10b05b8: strb w8, [x20, #0x4d3]
// 0x10b05bc: fsub v11.2s, v10.2s, v9.2s
// 0x10b05c0: fmul v0.2s, v11.2s, v11.2s
// 0x10b05c4: faddp s12, v0.2s
// 0x10b05c8: fcmp s12, #0.0
// 0x10b05cc: b.eq #0x10b0620
// 0x10b05d0: fmov s0, #16.00000000
// 0x10b05d4: fmul s1, s8, s0
// 0x10b05d8: fcmp s1, #0.0
// 0x10b05dc: b.lt #0x10b05ec
// 0x10b05e0: fmul s0, s1, s1
// 0x10b05e4: fcmp s12, s0
// 0x10b05e8: b.ls #0x10b0620
// 0x10b05ec: adrp x8, #0x1e8c000
// 0x10b05f0: ldr x8, [x8, #0xa60]
// 0x10b05f4: ldr x0, [x8]
// 0x10b05f8: ldr w8, [x0, #0xe0]
// 0x10b05fc: cbnz w8, #0x10b060c
// 0x10b0600: str q1, [sp, #0x10]
// 0x10b0604: bl #0xf7da5c
// 0x10b0608: ldr q1, [sp, #0x10]
// 0x10b060c: fsqrt s0, s12
// 0x10b0610: dup v0.2s, v0.s[0]
// 0x10b0614: fdiv v0.2s, v11.2s, v0.2s
// 0x10b0618: fmul v0.2s, v0.2s, v1.s[0]
// 0x10b061c: fadd v10.2s, v9.2s, v0.2s
// 0x10b0620: str d10, [x19, #0x1b8]
// 0x10b0624: ldr d9, [x19, #0x1c0]
// 0x10b0628: ldr s10, [x19, #0x1c8]
// 0x10b062c: ldr d11, [x21, #0x38]
// 0x10b0630: ldr s12, [x19, #0x16c]
// 0x10b0634: mov x0, xzr
// 0x10b0638: bl #0x1b9ae30
// 0x10b063c: ldrb w8, [x22, #0x4d2]
// 0x10b0640: mov v8.16b, v0.16b
// 0x10b0644: cbnz w8, #0x10b065c
// 0x10b0648: adrp x0, #0x1e8c000
// 0x10b064c: ldr x0, [x0, #0xa60]
// 0x10b0650: bl #0xf7d92c
// 0x10b0654: mov w8, #1
// 0x10b0658: strb w8, [x22, #0x4d2]
// 0x10b065c: fsub v13.2s, v11.2s, v9.2s
// 0x10b0660: fsub s14, s12, s10
// 0x10b0664: fmul v0.2s, v13.2s, v13.2s
// 0x10b0668: faddp s0, v0.2s
// 0x10b066c: fmul s1, s14, s14
// 0x10b0670: fadd s15, s1, s0
// 0x10b0674: fcmp s15, #0.0
// 0x10b0678: b.eq #0x10b06d8
// 0x10b067c: fmov s0, #16.00000000
// 0x10b0680: fmul s2, s8, s0
// 0x10b0684: fcmp s2, #0.0
// 0x10b0688: b.lt #0x10b0698
// 0x10b068c: fmul s0, s2, s2
// 0x10b0690: fcmp s15, s0
// 0x10b0694: b.ls #0x10b06d8
// 0x10b0698: adrp x8, #0x1e8c000
// 0x10b069c: ldr x8, [x8, #0xa60]
// 0x10b06a0: ldr x0, [x8]
// 0x10b06a4: ldr w8, [x0, #0xe0]
// 0x10b06a8: cbnz w8, #0x10b06b8
// 0x10b06ac: str q2, [sp, #0x10]
// 0x10b06b0: bl #0xf7da5c
// 0x10b06b4: ldr q2, [sp, #0x10]
// 0x10b06b8: fsqrt s0, s15
// 0x10b06bc: dup v1.2s, v0.s[0]
// 0x10b06c0: fdiv s0, s14, s0
// 0x10b06c4: fdiv v1.2s, v13.2s, v1.2s
// 0x10b06c8: fmul s0, s2, s0
// 0x10b06cc: fmul v1.2s, v1.2s, v2.s[0]
// 0x10b06d0: fadd v11.2s, v9.2s, v1.2s
// 0x10b06d4: fadd s12, s10, s0
// 0x10b06d8: ldr x8, [x19, #0x58]
// 0x10b06dc: str d11, [x19, #0x1c0]
// 0x10b06e0: str s12, [x19, #0x1c8]
// 0x10b06e4: cbz x8, #0x10b17e4
// 0x10b06e8: add x8, x8, #0x30c
// 0x10b06ec: ldr d9, [x21, #0xa0]
// 0x10b06f0: ldr s10, [x19, #0x1d4]
// 0x10b06f4: ldr d12, [x8]
// 0x10b06f8: ldr s11, [x8, #8]
// 0x10b06fc: mov x0, xzr
// 0x10b0700: bl #0x1b9ae30
// 0x10b0704: ldrb w8, [x22, #0x4d2]
// 0x10b0708: mov v8.16b, v0.16b
// 0x10b070c: cbnz w8, #0x10b0724
// 0x10b0710: adrp x0, #0x1e8c000
// 0x10b0714: ldr x0, [x0, #0xa60]
// 0x10b0718: bl #0xf7d92c
// 0x10b071c: mov w8, #1
// 0x10b0720: strb w8, [x22, #0x4d2]
// 0x10b0724: fsub v13.2s, v12.2s, v9.2s
// 0x10b0728: fsub s14, s11, s10
// 0x10b072c: fmul v0.2s, v13.2s, v13.2s
// 0x10b0730: faddp s0, v0.2s
// 0x10b0734: fmul s1, s14, s14
// 0x10b0738: fadd s15, s1, s0
// 0x10b073c: fcmp s15, #0.0
// 0x10b0740: b.eq #0x10b07a0
// 0x10b0744: fmov s0, #24.00000000
// 0x10b0748: fmul s2, s8, s0
// 0x10b074c: fcmp s2, #0.0
// 0x10b0750: b.lt #0x10b0760
// 0x10b0754: fmul s0, s2, s2
// 0x10b0758: fcmp s15, s0
// 0x10b075c: b.ls #0x10b07a0
// 0x10b0760: adrp x8, #0x1e8c000
// 0x10b0764: ldr x8, [x8, #0xa60]
// 0x10b0768: ldr x0, [x8]
// 0x10b076c: ldr w8, [x0, #0xe0]
// 0x10b0770: cbnz w8, #0x10b0780
// 0x10b0774: str q2, [sp, #0x10]
// 0x10b0778: bl #0xf7da5c
// 0x10b077c: ldr q2, [sp, #0x10]
// 0x10b0780: fsqrt s0, s15
// 0x10b0784: dup v1.2s, v0.s[0]
// 0x10b0788: fdiv s0, s14, s0
// 0x10b078c: fdiv v1.2s, v13.2s, v1.2s
// 0x10b0790: fmul s0, s2, s0
// 0x10b0794: fmul v1.2s, v1.2s, v2.s[0]
// 0x10b0798: fadd v12.2s, v9.2s, v1.2s
// 0x10b079c: fadd s11, s10, s0
// 0x10b07a0: str d12, [x21, #0xa0]
// 0x10b07a4: ldr x8, [x19, #0x58]
// 0x10b07a8: str s11, [x19, #0x1d4]
// 0x10b07ac: cbz x8, #0x10b17e4
// 0x10b07b0: ldr d9, [x19, #0x1d8]
// 0x10b07b4: ldr s10, [x19, #0x1e0]
// 0x10b07b8: ldr d11, [x8, #0x300]
// 0x10b07bc: ldr s12, [x8, #0x308]
// 0x10b07c0: mov x0, xzr
// 0x10b07c4: bl #0x1b9ae30
// 0x10b07c8: ldrb w8, [x22, #0x4d2]
// 0x10b07cc: mov v8.16b, v0.16b
// 0x10b07d0: cbnz w8, #0x10b07e8
// 0x10b07d4: adrp x0, #0x1e8c000
// 0x10b07d8: ldr x0, [x0, #0xa60]
// 0x10b07dc: bl #0xf7d92c
// 0x10b07e0: mov w8, #1
// 0x10b07e4: strb w8, [x22, #0x4d2]
// 0x10b07e8: fsub v13.2s, v11.2s, v9.2s
// 0x10b07ec: fsub s14, s12, s10
// 0x10b07f0: fmul v0.2s, v13.2s, v13.2s
// 0x10b07f4: faddp s0, v0.2s
// 0x10b07f8: fmul s1, s14, s14
// 0x10b07fc: fadd s15, s1, s0
// 0x10b0800: fcmp s15, #0.0
// 0x10b0804: b.eq #0x10b0864
// 0x10b0808: fmov s0, #24.00000000
// 0x10b080c: fmul s2, s8, s0
// 0x10b0810: fcmp s2, #0.0
// 0x10b0814: b.lt #0x10b0824
// 0x10b0818: fmul s0, s2, s2
// 0x10b081c: fcmp s15, s0
// 0x10b0820: b.ls #0x10b0864
// 0x10b0824: adrp x8, #0x1e8c000
// 0x10b0828: ldr x8, [x8, #0xa60]
// 0x10b082c: ldr x0, [x8]
// 0x10b0830: ldr w8, [x0, #0xe0]
// 0x10b0834: cbnz w8, #0x10b0844
// 0x10b0838: str q2, [sp, #0x10]
// 0x10b083c: bl #0xf7da5c
// 0x10b0840: ldr q2, [sp, #0x10]
// 0x10b0844: fsqrt s0, s15
// 0x10b0848: dup v1.2s, v0.s[0]
// 0x10b084c: fdiv s0, s14, s0
// 0x10b0850: fdiv v1.2s, v13.2s, v1.2s
// 0x10b0854: fmul s0, s2, s0
// 0x10b0858: fmul v1.2s, v1.2s, v2.s[0]
// 0x10b085c: fadd v11.2s, v9.2s, v1.2s
// 0x10b0860: fadd s12, s10, s0
// 0x10b0864: ldr x20, [x19, #0x30]
// 0x10b0868: str d11, [x19, #0x1d8]
// 0x10b086c: str s12, [x19, #0x1e0]
// 0x10b0870: cbz x20, #0x10b17e4
// 0x10b0874: mov x0, x20
// 0x10b0878: mov x1, xzr
// 0x10b087c: bl #0x1b67e78
// 0x10b0880: ldr s9, [x19, #0x1b0]
// 0x10b0884: ldr s10, [x19, #0x170]
// 0x10b0888: b #0x10b0c08
// 0x10b088c: ldr s0, [x9, #0x204]
// 0x10b0890: fcmp s0, #0.0
// 0x10b0894: b.ne #0x10b0480
// 0x10b0898: ldrb w8, [x9, #0x1f5]
// 0x10b089c: cbnz w8, #0x10b0480
// 0x10b08a0: ldr x0, [x19, #0x258]
// 0x10b08a4: cbz x0, #0x10b17e4
// 0x10b08a8: ldr x1, [x19, #0x120]
// 0x10b08ac: mov x2, xzr
// 0x10b08b0: bl #0x1b6a588
// 0x10b08b4: ldr x0, [x19, #0x258]
// 0x10b08b8: cbz x0, #0x10b17e4
// 0x10b08bc: fmov s0, #1.00000000
// 0x10b08c0: mov x1, xzr
// 0x10b08c4: bl #0x1b6a478
// 0x10b08c8: ldr x20, [x19, #0x258]
// 0x10b08cc: mov x0, xzr
// 0x10b08d0: bl #0x1b9ae58
// 0x10b08d4: cbz x20, #0x10b17e4
// 0x10b08d8: mov x0, x20
// 0x10b08dc: mov x1, xzr
// 0x10b08e0: bl #0x1b6a500
// 0x10b08e4: ldr x0, [x19, #0x258]
// 0x10b08e8: cbz x0, #0x10b17e4
// 0x10b08ec: mov x1, xzr
// 0x10b08f0: bl #0x1b6a5cc
// 0x10b08f4: mov w8, #1
// 0x10b08f8: strb w8, [x19, #0x128]
// 0x10b08fc: b #0x10b0480
// 0x10b0900: ldrb w9, [x8, #0x2dc]
// 0x10b0904: cbz w9, #0x10b0c6c
// 0x10b0908: ldr d9, [x19, #0x1b8]
// 0x10b090c: ldr d10, [x21, #0x48]
// 0x10b0910: mov x0, xzr
// 0x10b0914: bl #0x1b9ae30
// 0x10b0918: adrp x20, #0x1fab000
// 0x10b091c: ldrb w8, [x20, #0x4d3]
// 0x10b0920: mov v8.16b, v0.16b
// 0x10b0924: cbnz w8, #0x10b093c
// 0x10b0928: adrp x0, #0x1e8c000
// 0x10b092c: ldr x0, [x0, #0xa60]
// 0x10b0930: bl #0xf7d92c
// 0x10b0934: mov w8, #1
// 0x10b0938: strb w8, [x20, #0x4d3]
// 0x10b093c: fsub v11.2s, v10.2s, v9.2s
// 0x10b0940: fmul v0.2s, v11.2s, v11.2s
// 0x10b0944: faddp s12, v0.2s
// 0x10b0948: fcmp s12, #0.0
// 0x10b094c: b.eq #0x10b09a0
// 0x10b0950: fmov s0, #16.00000000
// 0x10b0954: fmul s1, s8, s0
// 0x10b0958: fcmp s1, #0.0
// 0x10b095c: b.lt #0x10b096c
// 0x10b0960: fmul s0, s1, s1
// 0x10b0964: fcmp s12, s0
// 0x10b0968: b.ls #0x10b09a0
// 0x10b096c: adrp x8, #0x1e8c000
// 0x10b0970: ldr x8, [x8, #0xa60]
// 0x10b0974: ldr x0, [x8]
// 0x10b0978: ldr w8, [x0, #0xe0]
// 0x10b097c: cbnz w8, #0x10b098c
// 0x10b0980: str q1, [sp, #0x10]
// 0x10b0984: bl #0xf7da5c
// 0x10b0988: ldr q1, [sp, #0x10]
// 0x10b098c: fsqrt s0, s12
// 0x10b0990: dup v0.2s, v0.s[0]
// 0x10b0994: fdiv v0.2s, v11.2s, v0.2s
// 0x10b0998: fmul v0.2s, v0.2s, v1.s[0]
// 0x10b099c: fadd v10.2s, v9.2s, v0.2s
// 0x10b09a0: str d10, [x19, #0x1b8]
// 0x10b09a4: ldr d9, [x19, #0x1c0]
// 0x10b09a8: ldr s10, [x19, #0x1c8]
// 0x10b09ac: ldr d11, [x21, #0x50]
// 0x10b09b0: ldr s12, [x19, #0x184]
// 0x10b09b4: mov x0, xzr
// 0x10b09b8: bl #0x1b9ae30
// 0x10b09bc: ldrb w8, [x22, #0x4d2]
// 0x10b09c0: mov v8.16b, v0.16b
// 0x10b09c4: cbnz w8, #0x10b09dc
// 0x10b09c8: adrp x0, #0x1e8c000
// 0x10b09cc: ldr x0, [x0, #0xa60]
// 0x10b09d0: bl #0xf7d92c
// 0x10b09d4: mov w8, #1
// 0x10b09d8: strb w8, [x22, #0x4d2]
// 0x10b09dc: fsub v13.2s, v11.2s, v9.2s
// 0x10b09e0: fsub s14, s12, s10
// 0x10b09e4: fmul v0.2s, v13.2s, v13.2s
// 0x10b09e8: faddp s0, v0.2s
// 0x10b09ec: fmul s1, s14, s14
// 0x10b09f0: fadd s15, s1, s0
// 0x10b09f4: fcmp s15, #0.0
// 0x10b09f8: b.eq #0x10b0a58
// 0x10b09fc: fmov s0, #16.00000000
// 0x10b0a00: fmul s2, s8, s0
// 0x10b0a04: fcmp s2, #0.0
// 0x10b0a08: b.lt #0x10b0a18
// 0x10b0a0c: fmul s0, s2, s2
// 0x10b0a10: fcmp s15, s0
// 0x10b0a14: b.ls #0x10b0a58
// 0x10b0a18: adrp x8, #0x1e8c000
// 0x10b0a1c: ldr x8, [x8, #0xa60]
// 0x10b0a20: ldr x0, [x8]
// 0x10b0a24: ldr w8, [x0, #0xe0]
// 0x10b0a28: cbnz w8, #0x10b0a38
// 0x10b0a2c: str q2, [sp, #0x10]
// 0x10b0a30: bl #0xf7da5c
// 0x10b0a34: ldr q2, [sp, #0x10]
// 0x10b0a38: fsqrt s0, s15
// 0x10b0a3c: dup v1.2s, v0.s[0]
// 0x10b0a40: fdiv s0, s14, s0
// 0x10b0a44: fdiv v1.2s, v13.2s, v1.2s
// 0x10b0a48: fmul s0, s2, s0
// 0x10b0a4c: fmul v1.2s, v1.2s, v2.s[0]
// 0x10b0a50: fadd v11.2s, v9.2s, v1.2s
// 0x10b0a54: fadd s12, s10, s0
// 0x10b0a58: ldr x8, [x19, #0x58]
// 0x10b0a5c: str d11, [x19, #0x1c0]
// 0x10b0a60: str s12, [x19, #0x1c8]
// 0x10b0a64: cbz x8, #0x10b17e4
// 0x10b0a68: add x8, x8, #0x324
// 0x10b0a6c: ldr d9, [x21, #0xa0]
// 0x10b0a70: ldr s10, [x19, #0x1d4]
// 0x10b0a74: ldr d12, [x8]
// 0x10b0a78: ldr s11, [x8, #8]
// 0x10b0a7c: mov x0, xzr
// 0x10b0a80: bl #0x1b9ae30
// 0x10b0a84: ldrb w8, [x22, #0x4d2]
// 0x10b0a88: mov v8.16b, v0.16b
// 0x10b0a8c: cbnz w8, #0x10b0aa4
// 0x10b0a90: adrp x0, #0x1e8c000
// 0x10b0a94: ldr x0, [x0, #0xa60]
// 0x10b0a98: bl #0xf7d92c
// 0x10b0a9c: mov w8, #1
// 0x10b0aa0: strb w8, [x22, #0x4d2]
// 0x10b0aa4: fsub v13.2s, v12.2s, v9.2s
// 0x10b0aa8: fsub s14, s11, s10
// 0x10b0aac: fmul v0.2s, v13.2s, v13.2s
// 0x10b0ab0: faddp s0, v0.2s
// 0x10b0ab4: fmul s1, s14, s14
// 0x10b0ab8: fadd s15, s1, s0
// 0x10b0abc: fcmp s15, #0.0
// 0x10b0ac0: b.eq #0x10b0b20
// 0x10b0ac4: fmov s0, #24.00000000
// 0x10b0ac8: fmul s2, s8, s0
// 0x10b0acc: fcmp s2, #0.0
// 0x10b0ad0: b.lt #0x10b0ae0
// 0x10b0ad4: fmul s0, s2, s2
// 0x10b0ad8: fcmp s15, s0
// 0x10b0adc: b.ls #0x10b0b20
// 0x10b0ae0: adrp x8, #0x1e8c000
// 0x10b0ae4: ldr x8, [x8, #0xa60]
// 0x10b0ae8: ldr x0, [x8]
// 0x10b0aec: ldr w8, [x0, #0xe0]
// 0x10b0af0: cbnz w8, #0x10b0b00
// 0x10b0af4: str q2, [sp, #0x10]
// 0x10b0af8: bl #0xf7da5c
// 0x10b0afc: ldr q2, [sp, #0x10]
// 0x10b0b00: fsqrt s0, s15
// 0x10b0b04: dup v1.2s, v0.s[0]
// 0x10b0b08: fdiv s0, s14, s0
// 0x10b0b0c: fdiv v1.2s, v13.2s, v1.2s
// 0x10b0b10: fmul s0, s2, s0
// 0x10b0b14: fmul v1.2s, v1.2s, v2.s[0]
// 0x10b0b18: fadd v12.2s, v9.2s, v1.2s
// 0x10b0b1c: fadd s11, s10, s0
// 0x10b0b20: str d12, [x21, #0xa0]
// 0x10b0b24: ldr x8, [x19, #0x58]
// 0x10b0b28: str s11, [x19, #0x1d4]
// 0x10b0b2c: cbz x8, #0x10b17e4
// 0x10b0b30: ldr d9, [x19, #0x1d8]
// 0x10b0b34: ldr s10, [x19, #0x1e0]
// 0x10b0b38: ldr d11, [x8, #0x318]
// 0x10b0b3c: ldr s12, [x8, #0x320]
// 0x10b0b40: mov x0, xzr
// 0x10b0b44: bl #0x1b9ae30
// 0x10b0b48: ldrb w8, [x22, #0x4d2]
// 0x10b0b4c: mov v8.16b, v0.16b
// 0x10b0b50: cbnz w8, #0x10b0b68
// 0x10b0b54: adrp x0, #0x1e8c000
// 0x10b0b58: ldr x0, [x0, #0xa60]
// 0x10b0b5c: bl #0xf7d92c
// 0x10b0b60: mov w8, #1
// 0x10b0b64: strb w8, [x22, #0x4d2]
// 0x10b0b68: fsub v13.2s, v11.2s, v9.2s
// 0x10b0b6c: fsub s14, s12, s10
// 0x10b0b70: fmul v0.2s, v13.2s, v13.2s
// 0x10b0b74: faddp s0, v0.2s
// 0x10b0b78: fmul s1, s14, s14
// 0x10b0b7c: fadd s15, s1, s0
// 0x10b0b80: fcmp s15, #0.0
// 0x10b0b84: b.eq #0x10b0be4
// 0x10b0b88: fmov s0, #24.00000000
// 0x10b0b8c: fmul s2, s8, s0
// 0x10b0b90: fcmp s2, #0.0
// 0x10b0b94: b.lt #0x10b0ba4
// 0x10b0b98: fmul s0, s2, s2
// 0x10b0b9c: fcmp s15, s0
// 0x10b0ba0: b.ls #0x10b0be4
// 0x10b0ba4: adrp x8, #0x1e8c000
// 0x10b0ba8: ldr x8, [x8, #0xa60]
// 0x10b0bac: ldr x0, [x8]
// 0x10b0bb0: ldr w8, [x0, #0xe0]
// 0x10b0bb4: cbnz w8, #0x10b0bc4
// 0x10b0bb8: str q2, [sp, #0x10]
// 0x10b0bbc: bl #0xf7da5c
// 0x10b0bc0: ldr q2, [sp, #0x10]
// 0x10b0bc4: fsqrt s0, s15
// 0x10b0bc8: dup v1.2s, v0.s[0]
// 0x10b0bcc: fdiv s0, s14, s0
// 0x10b0bd0: fdiv v1.2s, v13.2s, v1.2s
// 0x10b0bd4: fmul s0, s2, s0
// 0x10b0bd8: fmul v1.2s, v1.2s, v2.s[0]
// 0x10b0bdc: fadd v11.2s, v9.2s, v1.2s
// 0x10b0be0: fadd s12, s10, s0
// 0x10b0be4: ldr x20, [x19, #0x30]
// 0x10b0be8: str d11, [x19, #0x1d8]
// 0x10b0bec: str s12, [x19, #0x1e0]
// 0x10b0bf0: cbz x20, #0x10b17e4
// 0x10b0bf4: mov x0, x20
// 0x10b0bf8: mov x1, xzr
// 0x10b0bfc: bl #0x1b67e78
// 0x10b0c00: ldr s9, [x19, #0x1b0]
// 0x10b0c04: ldr s10, [x19, #0x188]
// 0x10b0c08: mov x0, xzr
// 0x10b0c0c: mov v8.16b, v0.16b
// 0x10b0c10: bl #0x1b9ae30
// 0x10b0c14: fmul s1, s8, s9
// 0x10b0c18: fmov s2, #16.00000000
// 0x10b0c1c: fsub s4, s10, s1
// 0x10b0c20: fmul s3, s0, s2
// 0x10b0c24: fnmul s0, s0, s2
// 0x10b0c28: fcmp s4, #0.0
// 0x10b0c2c: fabd s5, s10, s1
// 0x10b0c30: fcsel s0, s3, s0, ge
// 0x10b0c34: fadd s0, s1, s0
// 0x10b0c38: fcmp s5, s3
// 0x10b0c3c: fcsel s0, s0, s10, hi
// 0x10b0c40: mov x0, x20
// 0x10b0c44: ldp x20, x19, [sp, #0x80]
// 0x10b0c48: ldp x22, x21, [sp, #0x70]
// 0x10b0c4c: ldr x30, [sp, #0x60]
// 0x10b0c50: ldp d9, d8, [sp, #0x50]
// 0x10b0c54: ldp d11, d10, [sp, #0x40]
// 0x10b0c58: ldp d13, d12, [sp, #0x30]
// 0x10b0c5c: ldp d15, d14, [sp, #0x20]
// 0x10b0c60: mov x1, xzr
// 0x10b0c64: add sp, sp, #0x90
// 0x10b0c68: b #0x1b67eb4
// 0x10b0c6c: ldr s0, [x8, #0x2cc]
// 0x10b0c70: ldr s1, [x8, #0x3bc]
// 0x10b0c74: fcmp s0, s1
// 0x10b0c78: b.ge #0x10b0ca0
// 0x10b0c7c: ldp x20, x19, [sp, #0x80]
// 0x10b0c80: ldp x22, x21, [sp, #0x70]
// 0x10b0c84: ldr x30, [sp, #0x60]
// 0x10b0c88: ldp d9, d8, [sp, #0x50]
// 0x10b0c8c: ldp d11, d10, [sp, #0x40]
// 0x10b0c90: ldp d13, d12, [sp, #0x30]
// 0x10b0c94: ldp d15, d14, [sp, #0x20]
// 0x10b0c98: add sp, sp, #0x90
// 0x10b0c9c: ret
// 0x10b0ca0: ldr d9, [x19, #0x1b8]
// 0x10b0ca4: ldr d10, [x21]
// 0x10b0ca8: mov x0, xzr
// 0x10b0cac: bl #0x1b9ae30
// 0x10b0cb0: adrp x20, #0x1fab000
// 0x10b0cb4: ldrb w8, [x20, #0x4d3]
// 0x10b0cb8: mov v8.16b, v0.16b
// 0x10b0cbc: cbnz w8, #0x10b0cd4
// 0x10b0cc0: adrp x0, #0x1e8c000
// 0x10b0cc4: ldr x0, [x0, #0xa60]
// 0x10b0cc8: bl #0xf7d92c
// 0x10b0ccc: mov w8, #1
// 0x10b0cd0: strb w8, [x20, #0x4d3]
// 0x10b0cd4: fsub v11.2s, v10.2s, v9.2s
// 0x10b0cd8: fmul v0.2s, v11.2s, v11.2s
// 0x10b0cdc: faddp s12, v0.2s
// 0x10b0ce0: fcmp s12, #0.0
// 0x10b0ce4: b.eq #0x10b0d38
// 0x10b0ce8: fmov s0, #16.00000000
// 0x10b0cec: fmul s1, s8, s0
// 0x10b0cf0: fcmp s1, #0.0
// 0x10b0cf4: b.lt #0x10b0d04
// 0x10b0cf8: fmul s0, s1, s1
// 0x10b0cfc: fcmp s12, s0
// 0x10b0d00: b.ls #0x10b0d38
// 0x10b0d04: adrp x8, #0x1e8c000
// 0x10b0d08: ldr x8, [x8, #0xa60]
// 0x10b0d0c: ldr x0, [x8]
// 0x10b0d10: ldr w8, [x0, #0xe0]
// 0x10b0d14: cbnz w8, #0x10b0d24
// 0x10b0d18: str q1, [sp, #0x10]
// 0x10b0d1c: bl #0xf7da5c
// 0x10b0d20: ldr q1, [sp, #0x10]
// 0x10b0d24: fsqrt s0, s12
// 0x10b0d28: dup v0.2s, v0.s[0]
// 0x10b0d2c: fdiv v0.2s, v11.2s, v0.2s
// 0x10b0d30: fmul v0.2s, v0.2s, v1.s[0]
// 0x10b0d34: fadd v10.2s, v9.2s, v0.2s
// 0x10b0d38: ldr s8, [x19, #0x1c0]
// 0x10b0d3c: ldr s9, [x19, #0x134]
// 0x10b0d40: mov x0, xzr
// 0x10b0d44: str d10, [x19, #0x1b8]
// 0x10b0d48: bl #0x1b9ae30
// 0x10b0d4c: fmov s10, #16.00000000
// 0x10b0d50: fsub s1, s9, s8
// 0x10b0d54: fmul s3, s0, s10
// 0x10b0d58: fnmul s0, s0, s10
// 0x10b0d5c: fcmp s1, #0.0
// 0x10b0d60: fabd s2, s9, s8
// 0x10b0d64: ldr s11, [x19, #0x1c4]
// 0x10b0d68: ldr s12, [x19, #0x138]
// 0x10b0d6c: fcsel s0, s3, s0, ge
// 0x10b0d70: fadd s0, s8, s0
// 0x10b0d74: fcmp s2, s3
// 0x10b0d78: fcsel s0, s0, s9, hi
// 0x10b0d7c: mov x0, xzr
// 0x10b0d80: str s0, [x19, #0x1c0]
// 0x10b0d84: bl #0x1b9ae30
// 0x10b0d88: fsub s2, s12, s11
// 0x10b0d8c: fmul s1, s0, s10
// 0x10b0d90: fnmul s0, s0, s10
// 0x10b0d94: ldr x8, [x19, #0x58]
// 0x10b0d98: fcmp s2, #0.0
// 0x10b0d9c: fabd s3, s12, s11
// 0x10b0da0: fcsel s0, s1, s0, ge
// 0x10b0da4: fadd s0, s11, s0
// 0x10b0da8: fcmp s3, s1
// 0x10b0dac: fcsel s0, s0, s12, hi
// 0x10b0db0: str s0, [x19, #0x1c4]
// 0x10b0db4: cbz x8, #0x10b17e4
// 0x10b0db8: add x8, x8, #0x2c4
// 0x10b0dbc: ldr d9, [x21, #0xa0]
// 0x10b0dc0: ldr s10, [x19, #0x1d4]
// 0x10b0dc4: ldr d12, [x8]
// 0x10b0dc8: ldr s11, [x8, #8]
// 0x10b0dcc: mov x0, xzr
// 0x10b0dd0: bl #0x1b9ae30
// 0x10b0dd4: ldrb w8, [x22, #0x4d2]
// 0x10b0dd8: mov v8.16b, v0.16b
// 0x10b0ddc: cbnz w8, #0x10b0df4
// 0x10b0de0: adrp x0, #0x1e8c000
// 0x10b0de4: ldr x0, [x0, #0xa60]
// 0x10b0de8: bl #0xf7d92c
// 0x10b0dec: mov w8, #1
// 0x10b0df0: strb w8, [x22, #0x4d2]
// 0x10b0df4: fsub v13.2s, v12.2s, v9.2s
// 0x10b0df8: fsub s14, s11, s10
// 0x10b0dfc: fmul v0.2s, v13.2s, v13.2s
// 0x10b0e00: faddp s0, v0.2s
// 0x10b0e04: fmul s1, s14, s14
// 0x10b0e08: fadd s15, s1, s0
// 0x10b0e0c: fcmp s15, #0.0
// 0x10b0e10: b.eq #0x10b0e70
// 0x10b0e14: fmov s0, #24.00000000
// 0x10b0e18: fmul s2, s8, s0
// 0x10b0e1c: fcmp s2, #0.0
// 0x10b0e20: b.lt #0x10b0e30
// 0x10b0e24: fmul s0, s2, s2
// 0x10b0e28: fcmp s15, s0
// 0x10b0e2c: b.ls #0x10b0e70
// 0x10b0e30: adrp x8, #0x1e8c000
// 0x10b0e34: ldr x8, [x8, #0xa60]
// 0x10b0e38: ldr x0, [x8]
// 0x10b0e3c: ldr w8, [x0, #0xe0]
// 0x10b0e40: cbnz w8, #0x10b0e50
// 0x10b0e44: str q2, [sp, #0x10]
// 0x10b0e48: bl #0xf7da5c
// 0x10b0e4c: ldr q2, [sp, #0x10]
// 0x10b0e50: fsqrt s0, s15
// 0x10b0e54: dup v1.2s, v0.s[0]
// 0x10b0e58: fdiv s0, s14, s0
// 0x10b0e5c: fdiv v1.2s, v13.2s, v1.2s
// 0x10b0e60: fmul s0, s2, s0
// 0x10b0e64: fmul v1.2s, v1.2s, v2.s[0]
// 0x10b0e68: fadd v12.2s, v9.2s, v1.2s
// 0x10b0e6c: fadd s11, s10, s0
// 0x10b0e70: str d12, [x21, #0xa0]
// 0x10b0e74: ldr x8, [x19, #0x58]
// 0x10b0e78: str s11, [x19, #0x1d4]
// 0x10b0e7c: cbz x8, #0x10b17e4
// 0x10b0e80: ldr s9, [x19, #0x1d8]
// 0x10b0e84: ldr s10, [x8, #0x2b8]
// 0x10b0e88: mov x0, xzr
// 0x10b0e8c: bl #0x1b9ae30
// 0x10b0e90: fmov s8, #24.00000000
// 0x10b0e94: fsub s1, s10, s9
// 0x10b0e98: ldr x8, [x19, #0x58]
// 0x10b0e9c: fmul s3, s0, s8
// 0x10b0ea0: fnmul s0, s0, s8
// 0x10b0ea4: fcmp s1, #0.0
// 0x10b0ea8: fabd s2, s10, s9
// 0x10b0eac: fcsel s0, s3, s0, ge
// 0x10b0eb0: fadd s0, s9, s0
// 0x10b0eb4: fcmp s2, s3
// 0x10b0eb8: fcsel s0, s0, s10, hi
// 0x10b0ebc: str s0, [x19, #0x1d8]
// 0x10b0ec0: cbz x8, #0x10b17e4
// 0x10b0ec4: ldr s9, [x19, #0x1dc]
// 0x10b0ec8: ldr s10, [x8, #0x2bc]
// 0x10b0ecc: mov x0, xzr
// 0x10b0ed0: bl #0x1b9ae30
// 0x10b0ed4: fsub s2, s10, s9
// 0x10b0ed8: fmul s1, s0, s8
// 0x10b0edc: fnmul s0, s0, s8
// 0x10b0ee0: fcmp s2, #0.0
// 0x10b0ee4: fabd s3, s10, s9
// 0x10b0ee8: ldr s8, [x19, #0x1c8]
// 0x10b0eec: ldr s11, [x19, #0x13c]
// 0x10b0ef0: ldr s12, [x19, #0x1ac]
// 0x10b0ef4: fcsel s0, s1, s0, ge
// 0x10b0ef8: fadd s0, s9, s0
// 0x10b0efc: fcmp s3, s1
// 0x10b0f00: fcsel s0, s0, s10, hi
// 0x10b0f04: mov x0, xzr
// 0x10b0f08: str s0, [x19, #0x1dc]
// 0x10b0f0c: bl #0x1b9ae30
// 0x10b0f10: fdiv s1, s11, s12
// 0x10b0f14: fmov s2, #16.00000000
// 0x10b0f18: fsub s4, s1, s8
// 0x10b0f1c: ldr x8, [x19, #0x58]
// 0x10b0f20: fmul s3, s0, s2
// 0x10b0f24: fnmul s0, s0, s2
// 0x10b0f28: fcmp s4, #0.0
// 0x10b0f2c: fabd s5, s1, s8
// 0x10b0f30: fcsel s0, s3, s0, ge
// 0x10b0f34: fadd s0, s8, s0
// 0x10b0f38: fcmp s5, s3
// 0x10b0f3c: fcsel s0, s0, s1, hi
// 0x10b0f40: str s0, [x19, #0x1c8]
// 0x10b0f44: cbz x8, #0x10b17e4
// 0x10b0f48: ldr s8, [x19, #0x1e0]
// 0x10b0f4c: ldr s9, [x8, #0x2c0]
// 0x10b0f50: ldr s10, [x19, #0x1ac]
// 0x10b0f54: mov x0, xzr
// 0x10b0f58: bl #0x1b9ae30
// 0x10b0f5c: fdiv s1, s9, s10
// 0x10b0f60: fmov s2, #24.00000000
// 0x10b0f64: fsub s4, s1, s8
// 0x10b0f68: ldr x20, [x19, #0x30]
// 0x10b0f6c: fmul s3, s0, s2
// 0x10b0f70: fnmul s0, s0, s2
// 0x10b0f74: fcmp s4, #0.0
// 0x10b0f78: fabd s5, s1, s8
// 0x10b0f7c: fcsel s0, s3, s0, ge
// 0x10b0f80: fadd s0, s8, s0
// 0x10b0f84: fcmp s5, s3
// 0x10b0f88: fcsel s0, s0, s1, hi
// 0x10b0f8c: str s0, [x19, #0x1e0]
// 0x10b0f90: cbz x20, #0x10b17e4
// 0x10b0f94: mov x0, x20
// 0x10b0f98: mov x1, xzr
// 0x10b0f9c: bl #0x1b67e78
// 0x10b0fa0: ldr s9, [x19, #0x140]
// 0x10b0fa4: ldr s10, [x19, #0x1ac]
// 0x10b0fa8: ldr s11, [x19, #0x1b0]
// 0x10b0fac: mov v8.16b, v0.16b
// 0x10b0fb0: mov x0, xzr
// 0x10b0fb4: bl #0x1b9ae30
// 0x10b0fb8: fmul s1, s9, s10
// 0x10b0fbc: fmov s2, #16.00000000
// 0x10b0fc0: fmul s1, s1, s11
// 0x10b0fc4: fmul s3, s0, s2
// 0x10b0fc8: fnmul s0, s0, s2
// 0x10b0fcc: fsub s2, s1, s8
// 0x10b0fd0: fcmp s2, #0.0
// 0x10b0fd4: fabd s4, s1, s8
// 0x10b0fd8: fcsel s0, s3, s0, ge
// 0x10b0fdc: fadd s0, s8, s0
// 0x10b0fe0: fcmp s4, s3
// 0x10b0fe4: fcsel s0, s0, s1, hi
// 0x10b0fe8: b #0x10b0c40
// 0x10b0fec: ldr x8, [x19, #0x58]
// 0x10b0ff0: cbz x8, #0x10b17e4
// 0x10b0ff4: ldr s0, [x8, #0x2a0]
// 0x10b0ff8: str s0, [x19, #0x230]
// 0x10b0ffc: ldr s0, [x8, #0x2a4]
// 0x10b1000: b #0x10af820
// 0x10b1004: ldr s0, [x20, #0x2a8]
// 0x10b1008: str wzr, [x19, #0x234]
// 0x10b100c: str s0, [x19, #0x230]
// 0x10b1010: b #0x10af94c
// 0x10b1014: cbz x8, #0x10b17e4
// 0x10b1018: ldrb w9, [x8, #0x239]
// 0x10b101c: cbz w9, #0x10b113c
// 0x10b1020: ldr s8, [x8, #0x1fc]
// 0x10b1024: ldr s9, [x8, #0x150]
// 0x10b1028: mov x0, xzr
// 0x10b102c: bl #0x1b9ad30
// 0x10b1030: ldr x8, [x19, #0x58]
// 0x10b1034: fadd s1, s8, s9
// 0x10b1038: fcmp s1, s0
// 0x10b103c: b.pl #0x10b1130
// 0x10b1040: cbz x8, #0x10b17e4
// 0x10b1044: ldrb w9, [x8, #0x249]
// 0x10b1048: cbnz w9, #0x10b1134
// 0x10b104c: b #0x10afee8
// 0x10b1050: cbnz w8, #0x10b1060
// 0x10b1054: ldr x8, [x19, #0x58]
// 0x10b1058: cbz x8, #0x10b17e4
// 0x10b105c: ldr s9, [x8, #0x360]
// 0x10b1060: mov x0, xzr
// 0x10b1064: bl #0x1b89b60
// 0x10b1068: fmov s1, #16.00000000
// 0x10b106c: fsub s2, s9, s8
// 0x10b1070: ldr x9, [x19, #0x48]
// 0x10b1074: fmul s4, s0, s1
// 0x10b1078: fnmul s0, s0, s1
// 0x10b107c: fcmp s2, #0.0
// 0x10b1080: fabd s3, s9, s8
// 0x10b1084: fcsel s0, s4, s0, ge
// 0x10b1088: fadd s0, s8, s0
// 0x10b108c: fcmp s3, s4
// 0x10b1090: fcsel s0, s0, s9, hi
// 0x10b1094: str s0, [x19, #0x208]
// 0x10b1098: cbz x9, #0x10b17e4
// 0x10b109c: ldr x8, [x19, #0x58]
// 0x10b10a0: cbz x8, #0x10b17e4
// 0x10b10a4: ldrb w11, [x9, #0x460]
// 0x10b10a8: ldr x10, [x19, #0x40]
// 0x10b10ac: add x9, x8, #0x26c
// 0x10b10b0: cbz w11, #0x10b1158
// 0x10b10b4: cbz x10, #0x10b17e4
// 0x10b10b8: ldr d3, [x19, #0x250]
// 0x10b10bc: ldr q17, [sp, #0x10]
// 0x10b10c0: ldr s5, [x19, #0x230]
// 0x10b10c4: ldr s6, [x19, #0x238]
// 0x10b10c8: ldr d2, [x9, #0x10]
// 0x10b10cc: ldr s7, [x19, #0x23c]
// 0x10b10d0: fmov v16.2s, #1.50000000
// 0x10b10d4: ldr s1, [x10, #0xc0]
// 0x10b10d8: add x9, x19, #0x244
// 0x10b10dc: fdiv v3.2s, v3.2s, v16.2s
// 0x10b10e0: mov v16.16b, v17.16b
// 0x10b10e4: add x10, x19, #0x240
// 0x10b10e8: fadd s5, s5, s6
// 0x10b10ec: mov v6.16b, v0.16b
// 0x10b10f0: ld1 {v16.s}[1], [x9]
// 0x10b10f4: ld1 {v6.s}[1], [x10]
// 0x10b10f8: ldr d4, [x19, #0x248]
// 0x10b10fc: fadd v2.2s, v2.2s, v3.2s
// 0x10b1100: fadd s3, s5, s7
// 0x10b1104: fmul v17.2s, v1.2s, v17.2s
// 0x10b1108: mov v1.s[1], v3.s[0]
// 0x10b110c: fadd v1.2s, v1.2s, v16.2s
// 0x10b1110: fmul v0.2s, v17.2s, v0.2s
// 0x10b1114: fadd v1.2s, v1.2s, v6.2s
// 0x10b1118: fadd v2.2s, v4.2s, v2.2s
// 0x10b111c: mov v0.s[1], v1.s[1]
// 0x10b1120: fadd v0.2s, v2.2s, v0.2s
// 0x10b1124: add x9, x8, #0x284
// 0x10b1128: stur d0, [x19, #0xb4]
// 0x10b112c: b #0x10b11d0
// 0x10b1130: cbz x8, #0x10b17e4
// 0x10b1134: ldrb w9, [x8, #0x249]
// 0x10b1138: cbnz w9, #0x10afee8
// 0x10b113c: ldrb w9, [x8, #0x239]
// 0x10b1140: cbnz w9, #0x10b0394
// 0x10b1144: b #0x10afee8
// 0x10b1148: ldr s9, [x19, #0x1a0]
// 0x10b114c: ldr s10, [x19, #0x1ac]
// 0x10b1150: ldr s11, [x19, #0x1b0]
// 0x10b1154: b #0x10b0fb0
// 0x10b1158: cbz x10, #0x10b17e4
// 0x10b115c: ldr d3, [x19, #0x250]
// 0x10b1160: ldr q17, [sp, #0x10]
// 0x10b1164: ldr s5, [x19, #0x230]
// 0x10b1168: ldr s6, [x19, #0x238]
// 0x10b116c: ldr d2, [x9]
// 0x10b1170: ldr s7, [x19, #0x23c]
// 0x10b1174: fmov v16.2s, #1.50000000
// 0x10b1178: ldr s1, [x10, #0xc0]
// 0x10b117c: add x9, x19, #0x244
// 0x10b1180: fdiv v3.2s, v3.2s, v16.2s
// 0x10b1184: mov v16.16b, v17.16b
// 0x10b1188: add x10, x19, #0x240
// 0x10b118c: fadd s5, s5, s6
// 0x10b1190: mov v6.16b, v0.16b
// 0x10b1194: ld1 {v16.s}[1], [x9]
// 0x10b1198: ld1 {v6.s}[1], [x10]
// 0x10b119c: ldr d4, [x19, #0x248]
// 0x10b11a0: fadd v2.2s, v2.2s, v3.2s
// 0x10b11a4: fadd s3, s5, s7
// 0x10b11a8: fmul v17.2s, v1.2s, v17.2s
// 0x10b11ac: mov v1.s[1], v3.s[0]
// 0x10b11b0: fadd v1.2s, v1.2s, v16.2s
// 0x10b11b4: fmul v0.2s, v17.2s, v0.2s
// 0x10b11b8: fadd v1.2s, v1.2s, v6.2s
// 0x10b11bc: fadd v2.2s, v4.2s, v2.2s
// 0x10b11c0: mov v0.s[1], v1.s[1]
// 0x10b11c4: fadd v0.2s, v2.2s, v0.2s
// 0x10b11c8: stur d0, [x19, #0xb4]
// 0x10b11cc: add x9, x8, #0x274
// 0x10b11d0: ldr s0, [x9]
// 0x10b11d4: str s0, [x19, #0xbc]
// 0x10b11d8: ldr s0, [x8, #0x250]
// 0x10b11dc: fcmp s0, #0.0
// 0x10b11e0: b.le #0x10b11f4
// 0x10b11e4: ldr x9, [x19, #0x70]
// 0x10b11e8: cbz x9, #0x10b17e4
// 0x10b11ec: ldrb w9, [x9, #0x106]
// 0x10b11f0: cbnz w9, #0x10b11f8
// 0x10b11f4: ldr s0, [x8, #0x24c]
// 0x10b11f8: ldrb w9, [x19, #0x128]
// 0x10b11fc: str s0, [x19, #0xfc]
// 0x10b1200: cbz w9, #0x10b0004
// 0x10b1204: ldr s0, [x8, #0x204]
// 0x10b1208: fcmp s0, #0.0
// 0x10b120c: b.ne #0x10b0004
// 0x10b1210: ldrb w8, [x8, #0x1f5]
// 0x10b1214: cbnz w8, #0x10b0004
// 0x10b1218: ldr x0, [x19, #0x258]
// 0x10b121c: cbz x0, #0x10b17e4
// 0x10b1220: ldr x1, [x19, #0x118]
// 0x10b1224: mov x2, xzr
// 0x10b1228: bl #0x1b6a588
// 0x10b122c: ldr x0, [x19, #0x258]
// 0x10b1230: cbz x0, #0x10b17e4
// 0x10b1234: fmov s0, #1.00000000
// 0x10b1238: mov x1, xzr
// 0x10b123c: bl #0x1b6a478
// 0x10b1240: ldr x20, [x19, #0x258]
// 0x10b1244: mov x0, xzr
// 0x10b1248: bl #0x1b9ae58
// 0x10b124c: cbz x20, #0x10b17e4
// 0x10b1250: mov x0, x20
// 0x10b1254: mov x1, xzr
// 0x10b1258: bl #0x1b6a500
// 0x10b125c: ldr x0, [x19, #0x258]
// 0x10b1260: cbz x0, #0x10b17e4
// 0x10b1264: mov x1, xzr
// 0x10b1268: bl #0x1b6a5cc
// 0x10b126c: strb wzr, [x19, #0x128]
// 0x10b1270: b #0x10b0004
// 0x10b1274: ldrb w9, [x8, #0x2c2]
// 0x10b1278: cbz w9, #0x10b12a8
// 0x10b127c: ldr s0, [x19, #0xf0]
// 0x10b1280: mov w10, #0xd70a
// 0x10b1284: mov w9, #0x3f800000
// 0x10b1288: movk w10, #0xbc23, lsl #16
// 0x10b128c: str w9, [x19, #0x21c]
// 0x10b1290: str s0, [x19, #0xfc]
// 0x10b1294: str w10, [x19, #0x230]
// 0x10b1298: ldrb w8, [x8, #0x2dc]
// 0x10b129c: cbnz w8, #0x10af94c
// 0x10b12a0: str wzr, [x19, #0x238]
// 0x10b12a4: b #0x10af94c
// 0x10b12a8: ldrb w9, [x19, #0x129]
// 0x10b12ac: cbz w9, #0x10b12b8
// 0x10b12b0: ldrb w9, [x8, #0x147]
// 0x10b12b4: cbz w9, #0x10b127c
// 0x10b12b8: ldrb w8, [x8, #0x228]
// 0x10b12bc: cbz w8, #0x10b1688
// 0x10b12c0: mov x0, x19
// 0x10b12c4: bl #0x10b17e8
// 0x10b12c8: b #0x10b1690
// 0x10b12cc: ldrb w8, [x19, #0x129]
// 0x10b12d0: ldr s8, [x19, #0x208]
// 0x10b12d4: fmov s9, wzr
// 0x10b12d8: cbnz w8, #0x10b12e8
// 0x10b12dc: ldr x8, [x19, #0x58]
// 0x10b12e0: cbz x8, #0x10b17e4
// 0x10b12e4: ldr s9, [x8, #0x364]
// 0x10b12e8: mov x0, xzr
// 0x10b12ec: bl #0x1b89b60
// 0x10b12f0: fmov s11, #16.00000000
// 0x10b12f4: fsub s1, s9, s8
// 0x10b12f8: fmul s3, s0, s11
// 0x10b12fc: fnmul s0, s0, s11
// 0x10b1300: fcmp s1, #0.0
// 0x10b1304: fabd s2, s9, s8
// 0x10b1308: fcsel s0, s3, s0, ge
// 0x10b130c: fcmp s2, s3
// 0x10b1310: fadd s0, s8, s0
// 0x10b1314: fcsel s0, s0, s9, hi
// 0x10b1318: str s0, [x19, #0x208]
// 0x10b131c: ldr d9, [x19, #0x1b8]
// 0x10b1320: ldr d10, [x21, #0x18]
// 0x10b1324: mov x0, xzr
// 0x10b1328: bl #0x1b9ae30
// 0x10b132c: adrp x20, #0x1fab000
// 0x10b1330: ldrb w8, [x20, #0x4d3]
// 0x10b1334: mov v8.16b, v0.16b
// 0x10b1338: cbnz w8, #0x10b1350
// 0x10b133c: adrp x0, #0x1e8c000
// 0x10b1340: ldr x0, [x0, #0xa60]
// 0x10b1344: bl #0xf7d92c
// 0x10b1348: mov w8, #1
// 0x10b134c: strb w8, [x20, #0x4d3]
// 0x10b1350: fsub v12.2s, v10.2s, v9.2s
// 0x10b1354: fmul v0.2s, v12.2s, v12.2s
// 0x10b1358: faddp s13, v0.2s
// 0x10b135c: fcmp s13, #0.0
// 0x10b1360: b.eq #0x10b13b4
// 0x10b1364: fmul s0, s8, s11
// 0x10b1368: fcmp s0, #0.0
// 0x10b136c: str q0, [sp, #0x10]
// 0x10b1370: b.lt #0x10b1384
// 0x10b1374: ldr q0, [sp, #0x10]
// 0x10b1378: fmul s0, s0, s0
// 0x10b137c: fcmp s13, s0
// 0x10b1380: b.ls #0x10b13b4
// 0x10b1384: adrp x8, #0x1e8c000
// 0x10b1388: ldr x8, [x8, #0xa60]
// 0x10b138c: ldr x0, [x8]
// 0x10b1390: ldr w8, [x0, #0xe0]
// 0x10b1394: cbnz w8, #0x10b139c
// 0x10b1398: bl #0xf7da5c
// 0x10b139c: ldr q1, [sp, #0x10]
// 0x10b13a0: fsqrt s0, s13
// 0x10b13a4: dup v0.2s, v0.s[0]
// 0x10b13a8: fdiv v0.2s, v12.2s, v0.2s
// 0x10b13ac: fmul v0.2s, v0.2s, v1.s[0]
// 0x10b13b0: fadd v10.2s, v9.2s, v0.2s
// 0x10b13b4: str d10, [x19, #0x1b8]
// 0x10b13b8: ldr d9, [x19, #0x1c0]
// 0x10b13bc: ldr s10, [x19, #0x1c8]
// 0x10b13c0: ldr d11, [x21, #0x20]
// 0x10b13c4: ldr s12, [x19, #0x154]
// 0x10b13c8: mov x0, xzr
// 0x10b13cc: bl #0x1b9ae30
// 0x10b13d0: ldrb w8, [x22, #0x4d2]
// 0x10b13d4: mov v8.16b, v0.16b
// 0x10b13d8: cbnz w8, #0x10b13f0
// 0x10b13dc: adrp x0, #0x1e8c000
// 0x10b13e0: ldr x0, [x0, #0xa60]
// 0x10b13e4: bl #0xf7d92c
// 0x10b13e8: mov w8, #1
// 0x10b13ec: strb w8, [x22, #0x4d2]
// 0x10b13f0: fsub v13.2s, v11.2s, v9.2s
// 0x10b13f4: fsub s14, s12, s10
// 0x10b13f8: fmul v0.2s, v13.2s, v13.2s
// 0x10b13fc: faddp s0, v0.2s
// 0x10b1400: fmul s1, s14, s14
// 0x10b1404: fadd s15, s1, s0
// 0x10b1408: fcmp s15, #0.0
// 0x10b140c: b.eq #0x10b1470
// 0x10b1410: fmov s0, #16.00000000
// 0x10b1414: fmul s0, s8, s0
// 0x10b1418: fcmp s0, #0.0
// 0x10b141c: str q0, [sp, #0x10]
// 0x10b1420: b.lt #0x10b1434
// 0x10b1424: ldr q0, [sp, #0x10]
// 0x10b1428: fmul s0, s0, s0
// 0x10b142c: fcmp s15, s0
// 0x10b1430: b.ls #0x10b1470
// 0x10b1434: adrp x8, #0x1e8c000
// 0x10b1438: ldr x8, [x8, #0xa60]
// 0x10b143c: ldr x0, [x8]
// 0x10b1440: ldr w8, [x0, #0xe0]
// 0x10b1444: cbnz w8, #0x10b144c
// 0x10b1448: bl #0xf7da5c
// 0x10b144c: ldr q2, [sp, #0x10]
// 0x10b1450: fsqrt s0, s15
// 0x10b1454: dup v1.2s, v0.s[0]
// 0x10b1458: fdiv s0, s14, s0
// 0x10b145c: fdiv v1.2s, v13.2s, v1.2s
// 0x10b1460: fmul s0, s2, s0
// 0x10b1464: fmul v1.2s, v1.2s, v2.s[0]
// 0x10b1468: fadd v11.2s, v9.2s, v1.2s
// 0x10b146c: fadd s12, s10, s0
// 0x10b1470: ldr x8, [x19, #0x58]
// 0x10b1474: str d11, [x19, #0x1c0]
// 0x10b1478: str s12, [x19, #0x1c8]
// 0x10b147c: cbz x8, #0x10b17e4
// 0x10b1480: add x8, x8, #0x2dc
// 0x10b1484: ldr d9, [x21, #0xa0]
// 0x10b1488: ldr s10, [x19, #0x1d4]
// 0x10b148c: ldr d12, [x8]
// 0x10b1490: ldr s11, [x8, #8]
// 0x10b1494: mov x0, xzr
// 0x10b1498: bl #0x1b9ae30
// 0x10b149c: ldrb w8, [x22, #0x4d2]
// 0x10b14a0: mov v8.16b, v0.16b
// 0x10b14a4: cbnz w8, #0x10b14bc
// 0x10b14a8: adrp x0, #0x1e8c000
// 0x10b14ac: ldr x0, [x0, #0xa60]
// 0x10b14b0: bl #0xf7d92c
// 0x10b14b4: mov w8, #1
// 0x10b14b8: strb w8, [x22, #0x4d2]
// 0x10b14bc: fsub v13.2s, v12.2s, v9.2s
// 0x10b14c0: fsub s14, s11, s10
// 0x10b14c4: fmul v0.2s, v13.2s, v13.2s
// 0x10b14c8: faddp s0, v0.2s
// 0x10b14cc: fmul s1, s14, s14
// 0x10b14d0: fadd s15, s1, s0
// 0x10b14d4: fcmp s15, #0.0
// 0x10b14d8: b.eq #0x10b153c
// 0x10b14dc: fmov s0, #24.00000000
// 0x10b14e0: fmul s0, s8, s0
// 0x10b14e4: fcmp s0, #0.0
// 0x10b14e8: str q0, [sp, #0x10]
// 0x10b14ec: b.lt #0x10b1500
// 0x10b14f0: ldr q0, [sp, #0x10]
// 0x10b14f4: fmul s0, s0, s0
// 0x10b14f8: fcmp s15, s0
// 0x10b14fc: b.ls #0x10b153c
// 0x10b1500: adrp x8, #0x1e8c000
// 0x10b1504: ldr x8, [x8, #0xa60]
// 0x10b1508: ldr x0, [x8]
// 0x10b150c: ldr w8, [x0, #0xe0]
// 0x10b1510: cbnz w8, #0x10b1518
// 0x10b1514: bl #0xf7da5c
// 0x10b1518: ldr q2, [sp, #0x10]
// 0x10b151c: fsqrt s0, s15
// 0x10b1520: dup v1.2s, v0.s[0]
// 0x10b1524: fdiv s0, s14, s0
// 0x10b1528: fdiv v1.2s, v13.2s, v1.2s
// 0x10b152c: fmul s0, s2, s0
// 0x10b1530: fmul v1.2s, v1.2s, v2.s[0]
// 0x10b1534: fadd v12.2s, v9.2s, v1.2s
// 0x10b1538: fadd s11, s10, s0
// 0x10b153c: str d12, [x21, #0xa0]
// 0x10b1540: ldr x8, [x19, #0x58]
// 0x10b1544: str s11, [x19, #0x1d4]
// 0x10b1548: cbz x8, #0x10b17e4
// 0x10b154c: ldr d9, [x19, #0x1d8]
// 0x10b1550: ldr s10, [x19, #0x1e0]
// 0x10b1554: ldr d11, [x8, #0x2d0]
// 0x10b1558: ldr s12, [x8, #0x2d8]
// 0x10b155c: mov x0, xzr
// 0x10b1560: bl #0x1b9ae30
// 0x10b1564: ldrb w8, [x22, #0x4d2]
// 0x10b1568: mov v8.16b, v0.16b
// 0x10b156c: cbnz w8, #0x10b1584
// 0x10b1570: adrp x0, #0x1e8c000
// 0x10b1574: ldr x0, [x0, #0xa60]
// 0x10b1578: bl #0xf7d92c
// 0x10b157c: mov w8, #1
// 0x10b1580: strb w8, [x22, #0x4d2]
// 0x10b1584: fsub v13.2s, v11.2s, v9.2s
// 0x10b1588: fsub s14, s12, s10
// 0x10b158c: fmul v0.2s, v13.2s, v13.2s
// 0x10b1590: faddp s0, v0.2s
// 0x10b1594: fmul s1, s14, s14
// 0x10b1598: fadd s15, s1, s0
// 0x10b159c: fcmp s15, #0.0
// 0x10b15a0: b.eq #0x10b1604
// 0x10b15a4: fmov s0, #24.00000000
// 0x10b15a8: fmul s0, s8, s0
// 0x10b15ac: fcmp s0, #0.0
// 0x10b15b0: str q0, [sp, #0x10]
// 0x10b15b4: b.lt #0x10b15c8
// 0x10b15b8: ldr q0, [sp, #0x10]
// 0x10b15bc: fmul s0, s0, s0
// 0x10b15c0: fcmp s15, s0
// 0x10b15c4: b.ls #0x10b1604
// 0x10b15c8: adrp x8, #0x1e8c000
// 0x10b15cc: ldr x8, [x8, #0xa60]
// 0x10b15d0: ldr x0, [x8]
// 0x10b15d4: ldr w8, [x0, #0xe0]
// 0x10b15d8: cbnz w8, #0x10b15e0
// 0x10b15dc: bl #0xf7da5c
// 0x10b15e0: ldr q2, [sp, #0x10]
// 0x10b15e4: fsqrt s0, s15
// 0x10b15e8: dup v1.2s, v0.s[0]
// 0x10b15ec: fdiv s0, s14, s0
// 0x10b15f0: fdiv v1.2s, v13.2s, v1.2s
// 0x10b15f4: fmul s0, s2, s0
// 0x10b15f8: fmul v1.2s, v1.2s, v2.s[0]
// 0x10b15fc: fadd v11.2s, v9.2s, v1.2s
// 0x10b1600: fadd s12, s10, s0
// 0x10b1604: ldr x20, [x19, #0x30]
// 0x10b1608: str d11, [x19, #0x1d8]
// 0x10b160c: str s12, [x19, #0x1e0]
// 0x10b1610: cbz x20, #0x10b17e4
// 0x10b1614: mov x0, x20
// 0x10b1618: mov x1, xzr
// 0x10b161c: bl #0x1b67e78
// 0x10b1620: ldr s9, [x19, #0x1b0]
// 0x10b1624: ldr s10, [x19, #0x158]
// 0x10b1628: mov x0, xzr
// 0x10b162c: mov v8.16b, v0.16b
// 0x10b1630: bl #0x1b9ae30
// 0x10b1634: fmul s1, s8, s9
// 0x10b1638: fmov s2, #16.00000000
// 0x10b163c: fsub s4, s10, s1
// 0x10b1640: fmul s3, s0, s2
// 0x10b1644: fnmul s0, s0, s2
// 0x10b1648: fcmp s4, #0.0
// 0x10b164c: fabd s5, s10, s1
// 0x10b1650: fcsel s0, s3, s0, ge
// 0x10b1654: fadd s0, s1, s0
// 0x10b1658: fcmp s5, s3
// 0x10b165c: fcsel s0, s0, s10, hi
// 0x10b1660: mov x0, x20
// 0x10b1664: mov x1, xzr
// 0x10b1668: bl #0x1b67eb4
// 0x10b166c: ldrb w8, [x19, #0x129]
// 0x10b1670: cbnz w8, #0x10b0c7c
// 0x10b1674: ldr x8, [x19, #0x58]
// 0x10b1678: cbz x8, #0x10b17e4
// 0x10b167c: ldr s0, [x8, #0x2b4]
// 0x10b1680: str s0, [x19, #0xbc]
// 0x10b1684: b #0x10b0c7c
// 0x10b1688: mov x0, x19
// 0x10b168c: bl #0x10b1898
// 0x10b1690: ldr x8, [x19, #0x40]
// 0x10b1694: cbz x8, #0x10b17e4
// 0x10b1698: ldr s0, [x8, #0xc4]
// 0x10b169c: ldrb w9, [x8, #0x146]
// 0x10b16a0: fcmp s0, #0.0
// 0x10b16a4: b.ne #0x10b16b0
// 0x10b16a8: cbnz w9, #0x10b16c4
// 0x10b16ac: b #0x10b16b4
// 0x10b16b0: cbnz w9, #0x10b16bc
// 0x10b16b4: ldrb w9, [x8, #0x2e8]
// 0x10b16b8: cbz w9, #0x10b16c4
// 0x10b16bc: ldrb w8, [x8, #0x2dc]
// 0x10b16c0: cbz w8, #0x10b17dc
// 0x10b16c4: add x8, x19, #0xf0
// 0x10b16c8: ldr s0, [x8]
// 0x10b16cc: ldrb w8, [x19, #0x129]
// 0x10b16d0: str s0, [x19, #0xfc]
// 0x10b16d4: cbz w8, #0x10b173c
// 0x10b16d8: ldr s8, [x19, #0x214]
// 0x10b16dc: mov w8, #0x3f800000
// 0x10b16e0: movi d0, #0000000000000000
// 0x10b16e4: mov x0, xzr
// 0x10b16e8: str w8, [x19, #0x21c]
// 0x10b16ec: str d0, [x19, #0x230]
// 0x10b16f0: bl #0x1b89b60
// 0x10b16f4: fmov s2, wzr
// 0x10b16f8: fmov s1, #16.00000000
// 0x10b16fc: fsub s4, s2, s8
// 0x10b1700: ldr x20, [x19, #0x58]
// 0x10b1704: fmul s3, s0, s1
// 0x10b1708: fnmul s0, s0, s1
// 0x10b170c: fcmp s4, #0.0
// 0x10b1710: fabd s5, s2, s8
// 0x10b1714: fcsel s0, s3, s0, ge
// 0x10b1718: fadd s0, s8, s0
// 0x10b171c: fcmp s5, s3
// 0x10b1720: fcsel s0, s0, s2, hi
// 0x10b1724: str s0, [x19, #0x214]
// 0x10b1728: cbz x20, #0x10b17e4
// 0x10b172c: ldr s1, [x20, #0x260]
// 0x10b1730: fadd s0, s0, s1
// 0x10b1734: str s0, [x19, #0x210]
// 0x10b1738: b #0x10af94c
// 0x10b173c: ldr x8, [x19, #0x58]
// 0x10b1740: cbz x8, #0x10b17e4
// 0x10b1744: ldr s8, [x19, #0x214]
// 0x10b1748: ldr s9, [x8, #0x2ac]
// 0x10b174c: mov x0, xzr
// 0x10b1750: bl #0x1b89b60
// 0x10b1754: fmov s1, #16.00000000
// 0x10b1758: fsub s2, s9, s8
// 0x10b175c: ldr x20, [x19, #0x58]
// 0x10b1760: fmul s4, s0, s1
// 0x10b1764: fnmul s0, s0, s1
// 0x10b1768: fcmp s2, #0.0
// 0x10b176c: fabd s3, s9, s8
// 0x10b1770: fcsel s0, s4, s0, ge
// 0x10b1774: fadd s0, s8, s0
// 0x10b1778: fcmp s3, s4
// 0x10b177c: fcsel s0, s0, s9, hi
// 0x10b1780: str s0, [x19, #0x214]
// 0x10b1784: cbz x20, #0x10b17e4
// 0x10b1788: adrp x8, #0x832000
// 0x10b178c: ldr s1, [x20, #0x260]
// 0x10b1790: ldr s8, [x19, #0x21c]
// 0x10b1794: ldr s2, [x8, #0x380]
// 0x10b1798: fadd s0, s0, s1
// 0x10b179c: str s0, [x19, #0x210]
// 0x10b17a0: fcmp s8, s2
// 0x10b17a4: b.pl #0x10b17c8
// 0x10b17a8: mov x0, xzr
// 0x10b17ac: bl #0x1b89b60
// 0x10b17b0: ldr x20, [x19, #0x58]
// 0x10b17b4: fmov s1, #0.25000000
// 0x10b17b8: fmul s0, s0, s1
// 0x10b17bc: fadd s0, s8, s0
// 0x10b17c0: str s0, [x19, #0x21c]
// 0x10b17c4: cbz x20, #0x10b17e4
// 0x10b17c8: ldr s0, [x19, #0x218]
// 0x10b17cc: ldr s1, [x20, #0x2b0]
// 0x10b17d0: str wzr, [x19, #0x234]
// 0x10b17d4: fadd s0, s0, s1
// 0x10b17d8: b #0x10b100c
// 0x10b17dc: add x8, x19, #0xf4
// 0x10b17e0: b #0x10b16c8
// 0x10b17e4: bl #0xf7db74
```


## `Ironsights.PlaySprintingAnim` — RVA `0xcb17e8`

- Decompiled symbol: `Ironsights_PlaySprintingAnim`
- Metadata signature: `private void PlaySprintingAnim() { }`
- Native interval: `176` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[48];
    unsigned long long field_30;
} struct_0;

extern long long g_1f0ae70;
extern long long g_1f0dc18;
extern char g_1fab4d0;

void Ironsights_PlaySprintingAnim(struct_0 *ptr)
{
    unsigned long long v3;  // x30
    unsigned long long v4;  // x20
    unsigned long long v5;  // x19
    unsigned long long v6;  // x0
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x10]
    unsigned long long v2;  // [bp-0x8]

    v0 = v3;
    v1 = v4;
    v2 = v5;
    if (!(g_1fab4d0 & 1))
    {
        sub_f7d92c("M&");
        sub_f7d92c(&g_1f0ae70);
        sub_f7d92c(&g_1f0dc18);
        g_1fab4d0 = 1;
    }
    v6 = ptr->field_30;
    if (v6)
    {
        Animator__SetBool(v6, g_1f0fb20, 0, 0);
        v6 = ptr->field_30;
        if (v6)
        {
            Animator__SetBool(v6, g_1f0dc18, 1, 0);
            v6 = ptr->field_30;
            if (v6)
            {
                Animator__SetBool();
                return;
            }
        }
    }
    sub_f7db74(v6);
}
```


## `Ironsights.PlayIdleAnim` — RVA `0xcb1898`

- Decompiled symbol: `Ironsights_PlayIdleAnim`
- Metadata signature: `private void PlayIdleAnim() { }`
- Native interval: `176` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[48];
    unsigned long long field_30;
} struct_0;

extern long long g_1f0ae70;
extern long long g_1f0dc18;
extern char g_1fab4d1;

void Ironsights_PlayIdleAnim(struct_0 *ptr)
{
    unsigned long long v3;  // x30
    unsigned long long v4;  // x20
    unsigned long long v5;  // x19
    unsigned long long v6;  // x0
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x10]
    unsigned long long v2;  // [bp-0x8]

    v0 = v3;
    v1 = v4;
    v2 = v5;
    if (!(g_1fab4d1 & 1))
    {
        sub_f7d92c("M&");
        sub_f7d92c(&g_1f0ae70);
        sub_f7d92c(&g_1f0dc18);
        g_1fab4d1 = 1;
    }
    v6 = ptr->field_30;
    if (v6)
    {
        Animator__SetBool(v6, g_1f0fb20, 0, 0);
        v6 = ptr->field_30;
        if (v6)
        {
            Animator__SetBool(v6, g_1f0dc18, 0, 0);
            v6 = ptr->field_30;
            if (v6)
            {
                Animator__SetBool();
                return;
            }
        }
    }
    sub_f7db74(v6);
}
```


## `Ironsights.PlayWalkingAnim` — RVA `0xcb1948`

- Decompiled symbol: `Ironsights_PlayWalkingAnim`
- Metadata signature: `private void PlayWalkingAnim() { }`
- Native interval: `176` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[48];
    unsigned long long field_30;
} struct_0;

extern long long g_1f0ae70;
extern long long g_1f0dc18;
extern char g_1fab4cf;

void Ironsights_PlayWalkingAnim(struct_0 *ptr)
{
    unsigned long long v3;  // x30
    unsigned long long v4;  // x20
    unsigned long long v5;  // x19
    unsigned long long v6;  // x0
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x10]
    unsigned long long v2;  // [bp-0x8]

    v0 = v3;
    v1 = v4;
    v2 = v5;
    if (!(g_1fab4cf & 1))
    {
        sub_f7d92c("M&");
        sub_f7d92c(&g_1f0ae70);
        sub_f7d92c(&g_1f0dc18);
        g_1fab4cf = 1;
    }
    v6 = ptr->field_30;
    if (v6)
    {
        Animator__SetBool(v6, g_1f0fb20, 1, 0);
        v6 = ptr->field_30;
        if (v6)
        {
            Animator__SetBool(v6, g_1f0dc18, 0, 0);
            v6 = ptr->field_30;
            if (v6)
            {
                Animator__SetBool();
                return;
            }
        }
    }
    sub_f7db74(v6);
}
```


## `Ironsights.ctor` — RVA `0xcb19f8`

- Decompiled symbol: `Ironsights_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `1052` bytes
- Result: `pseudocode`
- Heuristic layout hint: `Ironsights_Recovered` matched 32 offsets against `Ironsights` metadata (confidence 0.76).

```c
typedef struct Ironsights_Recovered {
    char padding_0[216];
    unsigned long long dampVel;
    unsigned int field_e0;
    unsigned long long tempGunPos;
    unsigned int field_ec;
    uint128_t defaultFov;
    unsigned long long newFov;
    char padding_108[8];
    unsigned long long zoomMode;
    char padding_118[16];
    char zoomSfxState;
    char padding_129[3];
    unsigned long long walkPositionBob;
    unsigned long long walkAngleBob;
    unsigned int field_13c;
    unsigned int walkBobSpeed;
    unsigned long long sprintPositionBob;
    unsigned long long sprintAngleBob;
    unsigned int field_154;
    unsigned int sprintBobSpeed;
    unsigned long long crouchPositionBob;
    unsigned long long crouchAngleBob;
    unsigned int field_16c;
    unsigned int crouchBobSpeed;
    unsigned long long pronePositionBob;
    unsigned long long proneAngleBob;
    unsigned int field_184;
    unsigned int proneBobSpeed;
    unsigned long long zoomPositionBob;
    unsigned long long zoomAngleBob;
    unsigned int field_19c;
    unsigned long long zoomBobSpeed;
    unsigned int swimBobSpeedFactor;
    char padding_1ac[12];
    unsigned long long camPositionBobAmt;
    unsigned long long camAngleBobAmt;
    unsigned int field_1c8;
    unsigned long long weapPositionBobAmt;
    unsigned int field_1d4;
    unsigned long long weapAngleBobAmt;
    unsigned int field_1e0;
    uint128_t sprintStrafeRoll;
    uint128_t swimLookRoll;
    unsigned int swimBobAmt;
    char padding_208[8];
    unsigned int horizontalGunPosAmt;
    char padding_214[4];
    unsigned long long gunup;
    char padding_220[12];
    unsigned int bobDampSpeed;
} Ironsights_Recovered;

typedef struct struct_0 {
    unsigned long long field_0;
    unsigned int field_8;
    unsigned long long field_c;
    unsigned int field_14;
} struct_0;

typedef struct struct_4 {
    unsigned long long field_0;
    unsigned long long field_8;
} struct_4;

typedef struct struct_1 {
    char padding_0[184];
    struct struct_0 *field_b8;
} struct_1;

typedef struct struct_3 {
    char padding_0[184];
    struct struct_4 *field_b8;
} struct_3;

extern struct_3 *g_1ef22b8;
extern struct_1 *g_1ef22e8;
extern char g_1fab1e0;
extern char g_1fab1e1;
extern char g_1fab2c9;
extern char g_1fab32a;

void Ironsights_ctor(struct_2 *ptr)
{
    unsigned long long v9;  // x30
    unsigned long long v10;  // x26
    unsigned int v19;  // s1
    unsigned long long v20;  // d2
    unsigned int v21;  // s3
    unsigned int v22;  // w8
    unsigned int v23;  // s1
    unsigned int v24;  // s1
    unsigned int v25;  // s1
    unsigned int v26;  // s1
    unsigned int v27;  // s1
    unsigned int v28;  // s1
    unsigned long long v11;  // x25
    unsigned int v29;  // s1
    unsigned int v30;  // s1
    unsigned long long v12;  // x24
    unsigned long long v13;  // x23
    unsigned long long v14;  // x22
    unsigned long long v15;  // x21
    unsigned long long v16;  // x20
    unsigned long long v17;  // x19
    struct_2 *p;  // x22
    unsigned long long v0;  // [bp-0x50]
    unsigned long long v1;  // [bp-0x40]
    unsigned long long v2;  // [bp-0x38]
    unsigned long long v3;  // [bp-0x30]
    unsigned long long v4;  // [bp-0x28]
    unsigned long long v5;  // [bp-0x20]
    unsigned long long v6;  // [bp-0x18]
    unsigned long long v7;  // [bp-0x10]
    unsigned long long v8;  // [bp-0x8]

    v0 = v9;
    v1 = v10;
    v2 = v11;
    v3 = v12;
    v4 = v13;
    v5 = v14;
    v6 = v15;
    v7 = v16;
    v8 = v17;
    if (!g_1fab2c9)
    {
        sub_f7d92c(&g_1ef22e8);
        g_1fab2c9 = 1;
    }
    p = &ptr->padding_118[4];
    v19 = g_1ef22e8->field_b8->field_8;
    ptr->field_d8 = g_1ef22e8->field_b8->field_0;
    ptr->field_e0 = v19;
    v20 = g_1ef22e8->field_b8->field_0;
    v21 = g_1ef22e8->field_b8->field_8;
    *((uint128_t *)&ptr->field_ec) = 0x4296000041a0000042aa000042960000;
    *((unsigned long long *)&ptr->field_f0) = 0x3e19999a42960000;
    ptr->field_100 = 4539628424389459970;
    ptr->padding_118[0] = 1;
    *((unsigned long long *)&(&ptr->field_e0)[1]) = v20;
    *((unsigned int *)((char *)&ptr->field_e4 + 4)) = v21;
    if (!g_1fab32a)
    {
        sub_f7d92c(&g_1ef22b8);
        g_1fab32a = 1;
    }
    *((unsigned long long *)&p->padding_0[0]) = g_1ef22b8->field_b8->field_8;
    if (g_1fab1e1)
    {
        v22 = 0;
    }
    else
    {
        sub_f7d92c(&g_1ef22e8);
        g_1fab1e1 = 1;
        if (g_1fab32a)
            v22 = 0;
        else
            v22 = 1;
    }
    v23 = *((int *)((char *)&g_1ef22e8->field_b8->field_c + 4));
    *((long long *)&p->padding_0[8]) = *((long long *)&(&g_1ef22e8->field_b8->field_8)[1]);
    *((unsigned int *)&(&ptr->padding_129)[1]) = v23;
    *((unsigned int *)&ptr->field_12c) = 0x3f800000;
    if (v22)
    {
        sub_f7d92c(&g_1ef22b8);
        g_1fab32a = 1;
        *((unsigned long long *)&p->padding_0[24]) = g_1ef22b8->field_b8->field_8;
        if (g_1fab1e1)
        {
            v22 = 0;
        }
        else
        {
            sub_f7d92c(&g_1ef22e8);
            g_1fab1e1 = 1;
            if (g_1fab32a)
                v22 = 0;
            else
                v22 = 1;
        }
    }
    else
    {
        *((unsigned long long *)&p->padding_0[24]) = g_1ef22b8->field_b8->field_8;
    }
    v24 = *((int *)((char *)&g_1ef22e8->field_b8->field_c + 4));
    *((long long *)&p->padding_0[32]) = *((long long *)&(&g_1ef22e8->field_b8->field_8)[1]);
    ptr->field_140 = v24;
    *((unsigned int *)&ptr->field_144) = 0x3f800000;
    if (v22)
    {
        sub_f7d92c(&g_1ef22b8);
        g_1fab32a = 1;
        *((unsigned long long *)&p->padding_0[48]) = g_1ef22b8->field_b8->field_8;
        if (g_1fab1e1)
        {
            v22 = 0;
        }
        else
        {
            sub_f7d92c(&g_1ef22e8);
            g_1fab1e1 = 1;
            if (g_1fab32a)
                v22 = 0;
            else
                v22 = 1;
        }
    }
    else
    {
        *((unsigned long long *)&p->padding_0[48]) = g_1ef22b8->field_b8->field_8;
    }
    v25 = *((int *)((char *)&g_1ef22e8->field_b8->field_c + 4));
    *((long long *)&p->padding_0[56]) = *((long long *)&(&g_1ef22e8->field_b8->field_8)[1]);
    ptr->field_158 = v25;
    *((unsigned int *)&ptr->field_15c) = 0x3f800000;
    if (v22)
    {
        sub_f7d92c(&g_1ef22b8);
        g_1fab32a = 1;
        *((unsigned long long *)&p->padding_0[72]) = g_1ef22b8->field_b8->field_8;
        if (g_1fab1e1)
        {
            v22 = 0;
        }
        else
        {
            sub_f7d92c(&g_1ef22e8);
            g_1fab1e1 = 1;
            if (g_1fab32a)
                v22 = 0;
            else
                v22 = 1;
        }
    }
    else
    {
        *((unsigned long long *)&p->padding_0[72]) = g_1ef22b8->field_b8->field_8;
    }
    v26 = *((int *)((char *)&g_1ef22e8->field_b8->field_c + 4));
    *((long long *)&p->padding_0[80]) = *((long long *)&(&g_1ef22e8->field_b8->field_8)[1]);
    ptr->field_170 = v26;
    *((unsigned int *)&ptr->field_174) = 0x3f800000;
    if (v22)
    {
        sub_f7d92c(&g_1ef22b8);
        g_1fab32a = 1;
        *((unsigned long long *)&p->padding_0[96]) = g_1ef22b8->field_b8->field_8;
        if (!g_1fab1e1)
        {
            sub_f7d92c(&g_1ef22e8);
            g_1fab1e1 = 1;
        }
    }
    else
    {
        *((unsigned long long *)&p->padding_0[96]) = g_1ef22b8->field_b8->field_8;
    }
    v27 = *((int *)((char *)&g_1ef22e8->field_b8->field_c + 4));
    *((long long *)&p->padding_0[104]) = *((long long *)&(&g_1ef22e8->field_b8->field_8)[1]);
    ptr->field_188 = v27;
    ptr->field_18c = 0x3f8000003f800000;
    *((unsigned int *)&ptr->field_194) = 1058642330;
    if (!g_1fab1e0)
    {
        sub_f7d92c(&g_1ef22b8);
        g_1fab1e0 = 1;
    }
    ptr->field_1a0 = g_1ef22b8->field_b8->field_0;
    if (!g_1fab2c9)
    {
        sub_f7d92c(&g_1ef22e8);
        g_1fab2c9 = 1;
    }
    v28 = g_1ef22e8->field_b8->field_8;
    *((unsigned long long *)&ptr->field_1a8) = g_1ef22e8->field_b8->field_0;
    *((unsigned int *)&ptr->padding_1ac[4]) = v28;
    v29 = g_1ef22e8->field_b8->field_8;
    *((unsigned long long *)&p->padding_0[160]) = g_1ef22e8->field_b8->field_0;
    *((unsigned int *)((char *)&ptr->field_1b8 + 4)) = v29;
    v30 = g_1ef22e8->field_b8->field_8;
    ptr->field_1c0 = g_1ef22e8->field_b8->field_0;
    ptr->field_1c8 = v30;
    *((uint128_t *)&p->padding_0[184]) = 0x3f8000003f8000003f80000040000000;
    *((uint128_t *)&p->padding_0[200]) = 0x3f80000040000000408000003f800000;
    (&ptr->field_1e0)[1] = 0x3f800000;
    *((unsigned int *)&ptr->field_1e4) = 3164854026;
    *((unsigned long long *)((char *)&ptr->field_1e4 + 8)) = 4575657222422774415;
    *((unsigned int *)((char *)&ptr->field_1f4 + 12)) = 1036831949;
}
```
