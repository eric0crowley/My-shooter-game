# Native pseudocode: GunSway

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `GunSway.Start` — RVA `0xcae3e8`

- Decompiled symbol: `GunSway_Start`
- Metadata signature: `private void Start() { }`
- Native interval: `516` bytes
- Result: `pseudocode`
- Heuristic layout hint: `GunSway_Recovered` matched 11 offsets against `GunSway` metadata (confidence 1.00).

```c
typedef struct GunSway_Recovered {
    char padding_0[32];
    long long FPSWalkerComponent;
    long long IronsightsComponent;
    char padding_30[8];
    long long FPSPlayerComponent;
    long long InputComponent;
    struct struct_1 *CameraControlComponent;
    long long cameraObj;
    long long playerObj;
    long long myTransform;
    char padding_68[100];
    unsigned long long gunBobRoll;
    char padding_d4[20];
    unsigned int sprintBobYawAmount;
    unsigned int sprintBobRollAmount;
} GunSway_Recovered;

typedef struct struct_0 {
    char padding_0[40];
    unsigned long long field_28;
} struct_0;

typedef struct struct_1 {
    char padding_0[40];
    long long field_28;
} struct_1;

extern long long g_1efcf38;
extern long long g_1efebb8;
extern long long g_1efebc0;
extern long long g_1efec08;
extern long long g_1efec18;
extern char g_1fab4cc;

long long GunSway_Start(struct_2 *ptr8)
{
    unsigned long long v3;  // x30
    unsigned long long v4;  // x20
    struct_2 *v13;  // x20
    long long v14;  // x0
    struct_2 *p;  // x20
    struct_2 *v16;  // x20
    long long v17;  // x0
    struct_2 *addr;  // x20
    struct_2 *v19;  // x20
    long long v20;  // x0
    struct_2 *ptr3;  // x20
    struct_2 *v22;  // x20
    unsigned long long v5;  // x19
    long long v23;  // x0
    struct_2 *ptr4;  // x20
    struct_2 *v25;  // x20
    long long v26;  // x0
    struct_2 *ptr;  // x19
    unsigned long v28;  // x0
    unsigned int v29;  // s2
    unsigned int v30;  // s3
    unsigned int v31;  // s2
    unsigned int v32;  // s0
    long long v6;  // x1
    unsigned long v33;  // 4153
    unsigned long v34;  // d3
    unsigned long v35;  // 4147
    struct_2 *ptr5;  // x0
    struct_0 *v8;  // x0
    struct_2 *ptr6;  // x20
    struct_2 *v10;  // x20
    unsigned long v11;  // x1
    struct_2 *ptr7;  // x20
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x10]
    unsigned long long v2;  // [bp-0x8]

    v0 = v3;
    v1 = v4;
    v2 = v5;
    if (!(g_1fab4cc & 1))
    {
        sub_f7d92c(&g_1efcf38);
        sub_f7d92c(&g_1efebb8);
        sub_f7d92c(&g_1efebc0);
        sub_f7d92c(&g_1efec08);
        sub_f7d92c(&g_1efec18);
        g_1fab4cc = 1;
    }
    v6 = Component__get_transform(ptr8, 0);
    ptr5 = ptr8;
    ptr5->field_60 = v6;
    sub_f7d8d0((struct GunSway_Recovered *)&ptr5->field_60, v6);
    if (Camera__get_main(0))
    {
        v8 = sub_1231bc8();
        ptr6 = ptr8;
        ptr6->field_48 = v8;
        v10 = &ptr6->field_48;
        sub_f7d8d0(v10, v8);
        if (*((long long *)&v10->padding_0[0]))
        {
            v11 = *((long long *)(*((long long *)&v10->padding_0[0]) + 40));
            ptr7 = ptr8;
            ptr7->field_58 = v11;
            v13 = &ptr7->field_58;
            sub_f7d8d0(v13, v11);
            if (*((long long *)&v13->padding_0[16]) && Component__get_transform(*((long long *)&v13->padding_0[16]), 0) && Transform__get_parent() && Component__get_transform())
            {
                v14 = Component__get_gameObject();
                p = ptr8;
                p->field_50 = v14;
                v16 = &p->field_50;
                sub_f7d8d0(v16, v14);
                if (*((long long *)&v16->padding_0[8]))
                {
                    v17 = sub_1249224(*((long long *)&v16->padding_0[8]), g_1efebc0);
                    addr = ptr8;
                    addr->field_20 = v17;
                    v19 = &addr->field_20;
                    sub_f7d8d0(v19, v17);
                    if (v19->field_38)
                    {
                        v20 = sub_1249224(v19->field_38, g_1efec18);
                        ptr3 = ptr8;
                        ptr3->field_28 = v20;
                        v22 = &ptr3->field_28;
                        sub_f7d8d0(v22, v20);
                        if (v22->padding_30)
                        {
                            v23 = sub_1249224(v22->padding_30, g_1efebb8);
                            ptr4 = ptr8;
                            ptr4->field_38 = v23;
                            v25 = &ptr4->field_38;
                            sub_f7d8d0(v25, v23);
                            if (v25->field_20)
                            {
                                v26 = sub_1249224(v25->field_20, g_1efec08);
                                ptr8->field_40 = v26;
                                ptr = &ptr8->field_40;
                                v28 = sub_f7d8d0(ptr, v26);
                                v29 = *((int *)&ptr->padding_68[64]);
                                v30 = *((int *)&ptr->padding_68[68]);
                                v31 = [D] unsupported_Iop_ZeroHI96ofV128();
                                v32 = [D] unsupported_Iop_ZeroHI96ofV128();
                                v33 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v29, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v29, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v29, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v29, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v29, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v29, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                                if (!((char)v33))
                                    v31 = 0;
                                v34 = [D] unsupported_Iop_ZeroHI64ofV128();
                                v35 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v30, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v30, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v30, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v30, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v30, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v30, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                                if (!((char)v35))
                                    v32 = 0;
                                *((unsigned int *)&ptr->padding_68[64]) = v31;
                                *((unsigned int *)&ptr->padding_68[68]) = v32;
                                *((unsigned long *)&ptr->padding_68[36]) = v34;
                                return v28;
                            }
                        }
                    }
                }
            }
        }
    }
    sub_f7db74();
}
```

## `GunSway.Update` — RVA `0xcae5ec`

- Decompiled symbol: `GunSway_Update`
- Metadata signature: `private void Update() { }`
- Native interval: `2384` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: Decompiler produced no C-like text

```c
// 0x10ae5ec: stp d15, d14, [sp, #-0x60]!
// 0x10ae5f0: stp d13, d12, [sp, #0x10]
// 0x10ae5f4: stp d11, d10, [sp, #0x20]
// 0x10ae5f8: stp d9, d8, [sp, #0x30]
// 0x10ae5fc: stp x30, x21, [sp, #0x40]
// 0x10ae600: stp x20, x19, [sp, #0x50]
// 0x10ae604: ldr x8, [x0, #0x38]
// 0x10ae608: cbz x8, #0x10aef38
// 0x10ae60c: ldr x1, [x8, #0x78]
// 0x10ae610: mov x20, x0
// 0x10ae614: mov x19, x0
// 0x10ae618: str x1, [x20, #0x30]!
// 0x10ae61c: mov x0, x20
// 0x10ae620: bl #0xf7d8d0
// 0x10ae624: ldr x8, [x20, #8]
// 0x10ae628: cbz x8, #0x10aef38
// 0x10ae62c: ldr s0, [x19, #0xd4]
// 0x10ae630: ldrb w8, [x8, #0x2d0]
// 0x10ae634: fmov s1, #0.50000000
// 0x10ae638: mov x0, xzr
// 0x10ae63c: fmul s1, s0, s1
// 0x10ae640: cmp w8, #0
// 0x10ae644: fcsel s0, s0, s1, eq
// 0x10ae648: str s0, [x19, #0xd8]
// 0x10ae64c: bl #0x1b9ae58
// 0x10ae650: fcmp s0, #0.0
// 0x10ae654: b.le #0x10ae71c
// 0x10ae658: mov x0, xzr
// 0x10ae65c: bl #0x1b89b60
// 0x10ae660: fcmp s0, #0.0
// 0x10ae664: b.le #0x10ae71c
// 0x10ae668: ldr x8, [x19, #0x20]
// 0x10ae66c: cbz x8, #0x10aef38
// 0x10ae670: ldrb w8, [x8, #0x2b0]
// 0x10ae674: adrp x21, #0x832000
// 0x10ae678: cbz w8, #0x10ae738
// 0x10ae67c: ldr x8, [x20]
// 0x10ae680: cbz x8, #0x10aef38
// 0x10ae684: ldr s0, [x8, #0x330]
// 0x10ae688: adrp x8, #0x832000
// 0x10ae68c: ldp s1, s2, [x19, #0xd8]
// 0x10ae690: ldr s4, [x19, #0xe8]
// 0x10ae694: ldr d5, [x8, #0x2b8]
// 0x10ae698: ldr s8, [x19, #0xd0]
// 0x10ae69c: fmov s3, wzr
// 0x10ae6a0: fmul s2, s2, s3
// 0x10ae6a4: fmov s3, #12.00000000
// 0x10ae6a8: fmul s3, s4, s3
// 0x10ae6ac: fmul v1.2s, v5.2s, v1.s[0]
// 0x10ae6b0: fcmp s8, s3
// 0x10ae6b4: fmul s2, s0, s2
// 0x10ae6b8: fmul v0.2s, v1.2s, v0.s[0]
// 0x10ae6bc: str d0, [x19, #0xb0]
// 0x10ae6c0: str s2, [x19, #0xc0]
// 0x10ae6c4: b.pl #0x10ae6e4
// 0x10ae6c8: mov x0, xzr
// 0x10ae6cc: bl #0x1b89b60
// 0x10ae6d0: mov w8, #0x42700000
// 0x10ae6d4: fmov s1, w8
// 0x10ae6d8: fmul s0, s0, s1
// 0x10ae6dc: fadd s0, s8, s0
// 0x10ae6e0: str s0, [x19, #0xd0]
// 0x10ae6e4: ldr s0, [x19, #0xec]
// 0x10ae6e8: ldr s8, [x19, #0xcc]
// 0x10ae6ec: fmov s1, #15.00000000
// 0x10ae6f0: fmul s0, s0, s1
// 0x10ae6f4: fcmp s8, s0
// 0x10ae6f8: b.pl #0x10ae7f8
// 0x10ae6fc: mov x0, xzr
// 0x10ae700: bl #0x1b89b60
// 0x10ae704: mov w8, #0x42700000
// 0x10ae708: fmov s1, w8
// 0x10ae70c: fmul s0, s0, s1
// 0x10ae710: fadd s0, s8, s0
// 0x10ae714: str s0, [x19, #0xcc]
// 0x10ae718: b #0x10ae7f8
// 0x10ae71c: ldp x20, x19, [sp, #0x50]
// 0x10ae720: ldp x30, x21, [sp, #0x40]
// 0x10ae724: ldp d9, d8, [sp, #0x30]
// 0x10ae728: ldp d11, d10, [sp, #0x20]
// 0x10ae72c: ldp d13, d12, [sp, #0x10]
// 0x10ae730: ldp d15, d14, [sp], #0x60
// 0x10ae734: ret
// 0x10ae738: ldr s0, [x19, #0xe0]
// 0x10ae73c: ldr s8, [x19, #0xd0]
// 0x10ae740: fmov s1, #-16.00000000
// 0x10ae744: fmul s0, s0, s1
// 0x10ae748: fcmp s8, s0
// 0x10ae74c: b.le #0x10ae76c
// 0x10ae750: mov x0, xzr
// 0x10ae754: bl #0x1b89b60
// 0x10ae758: mov w8, #-0x3d900000
// 0x10ae75c: fmov s1, w8
// 0x10ae760: fmul s0, s0, s1
// 0x10ae764: fadd s0, s8, s0
// 0x10ae768: str s0, [x19, #0xd0]
// 0x10ae76c: ldr s0, [x19, #0xe4]
// 0x10ae770: ldr s8, [x19, #0xcc]
// 0x10ae774: fmov s1, #15.00000000
// 0x10ae778: fmul s0, s0, s1
// 0x10ae77c: fcmp s8, s0
// 0x10ae780: b.le #0x10ae7a0
// 0x10ae784: mov x0, xzr
// 0x10ae788: bl #0x1b89b60
// 0x10ae78c: mov w8, #-0x3d900000
// 0x10ae790: fmov s1, w8
// 0x10ae794: fmul s0, s0, s1
// 0x10ae798: fadd s0, s8, s0
// 0x10ae79c: str s0, [x19, #0xcc]
// 0x10ae7a0: ldr x8, [x19, #0x38]
// 0x10ae7a4: cbz x8, #0x10aef38
// 0x10ae7a8: ldrb w8, [x8, #0x2d0]
// 0x10ae7ac: cbz w8, #0x10ae7c0
// 0x10ae7b0: ldr x8, [x19, #0x28]
// 0x10ae7b4: cbz x8, #0x10aef38
// 0x10ae7b8: ldrb w8, [x8, #0x129]
// 0x10ae7bc: cbz w8, #0x10aeefc
// 0x10ae7c0: ldr x8, [x20]
// 0x10ae7c4: cbz x8, #0x10aef38
// 0x10ae7c8: adrp x9, #0x831000
// 0x10ae7cc: adrp x10, #0x832000
// 0x10ae7d0: ldp s0, s1, [x19, #0xd8]
// 0x10ae7d4: ldr d2, [x9, #0xfc0]
// 0x10ae7d8: ldr s3, [x10, #0x304]
// 0x10ae7dc: ldr s4, [x8, #0x330]
// 0x10ae7e0: fmul v0.2s, v2.2s, v0.s[0]
// 0x10ae7e4: fmul s1, s1, s3
// 0x10ae7e8: fmul v0.2s, v0.2s, v4.s[0]
// 0x10ae7ec: fmul s1, s4, s1
// 0x10ae7f0: str d0, [x19, #0xb0]
// 0x10ae7f4: str s1, [x19, #0xc0]
// 0x10ae7f8: mov x0, xzr
// 0x10ae7fc: bl #0x1b6f8dc
// 0x10ae800: cbz x0, #0x10aef38
// 0x10ae804: mov x1, xzr
// 0x10ae808: bl #0x1b92154
// 0x10ae80c: cbz x0, #0x10aef38
// 0x10ae810: mov x1, xzr
// 0x10ae814: bl #0x1b9d7c8
// 0x10ae818: ldr x0, [x19, #0x50]
// 0x10ae81c: str s2, [x19, #0xc4]
// 0x10ae820: cbz x0, #0x10aef38
// 0x10ae824: mov x1, xzr
// 0x10ae828: bl #0x1b94c14
// 0x10ae82c: cbz x0, #0x10aef38
// 0x10ae830: mov x1, xzr
// 0x10ae834: bl #0x1b9d7c8
// 0x10ae838: ldr x0, [x19, #0x50]
// 0x10ae83c: str s2, [x19, #0xc8]
// 0x10ae840: cbz x0, #0x10aef38
// 0x10ae844: mov x1, xzr
// 0x10ae848: bl #0x1b94c14
// 0x10ae84c: cbz x0, #0x10aef38
// 0x10ae850: mov x1, xzr
// 0x10ae854: bl #0x1b9d6c8
// 0x10ae858: ldr x8, [x19, #0x38]
// 0x10ae85c: str s0, [x19, #0x7c]
// 0x10ae860: cbz x8, #0x10aef38
// 0x10ae864: ldr x0, [x19, #0x50]
// 0x10ae868: cbz x0, #0x10aef38
// 0x10ae86c: ldrb w20, [x8, #0x208]
// 0x10ae870: mov x1, xzr
// 0x10ae874: bl #0x1b94c14
// 0x10ae878: cbz x0, #0x10aef38
// 0x10ae87c: mov x1, xzr
// 0x10ae880: cbz w20, #0x10ae88c
// 0x10ae884: bl #0x1b9d6c8
// 0x10ae888: b #0x10ae890
// 0x10ae88c: bl #0x1b9d7c8
// 0x10ae890: ldp s8, s9, [x19, #0xc4]
// 0x10ae894: mov x0, xzr
// 0x10ae898: str s1, [x19, #0x80]
// 0x10ae89c: bl #0x1b89b60
// 0x10ae8a0: mov w8, #0x3d800000
// 0x10ae8a4: fmov s3, w8
// 0x10ae8a8: mov w8, #0x43b40000
// 0x10ae8ac: fsub s1, s9, s8
// 0x10ae8b0: fmov s2, w8
// 0x10ae8b4: mov w8, #-0x3c4c0000
// 0x10ae8b8: fdiv s6, s1, s2
// 0x10ae8bc: fmov s5, w8
// 0x10ae8c0: frintm s6, s6
// 0x10ae8c4: fmul s6, s6, s5
// 0x10ae8c8: fadd s1, s1, s6
// 0x10ae8cc: fmov s4, wzr
// 0x10ae8d0: mov w8, #0x43340000
// 0x10ae8d4: fmin s2, s1, s2
// 0x10ae8d8: fcmp s1, #0.0
// 0x10ae8dc: fmov s6, w8
// 0x10ae8e0: fcsel s1, s2, s4, pl
// 0x10ae8e4: fadd s2, s1, s5
// 0x10ae8e8: fcmp s1, s6
// 0x10ae8ec: fcsel s2, s2, s1, gt
// 0x10ae8f0: fnmul s1, s0, s3
// 0x10ae8f4: fcmp s2, s1
// 0x10ae8f8: fmul s0, s0, s3
// 0x10ae8fc: b.le #0x10ae908
// 0x10ae900: fcmp s2, s0
// 0x10ae904: b.mi #0x10ae928
// 0x10ae908: fadd s2, s8, s2
// 0x10ae90c: fsub s3, s2, s8
// 0x10ae910: fcmp s3, #0.0
// 0x10ae914: fabd s4, s2, s8
// 0x10ae918: fcsel s1, s0, s1, ge
// 0x10ae91c: fadd s1, s8, s1
// 0x10ae920: fcmp s4, s0
// 0x10ae924: fcsel s9, s1, s2, hi
// 0x10ae928: ldr x8, [x19, #0x48]
// 0x10ae92c: str s9, [x19, #0x84]
// 0x10ae930: cbz x8, #0x10aef38
// 0x10ae934: ldr x8, [x8, #0x50]
// 0x10ae938: cbz x8, #0x10aef38
// 0x10ae93c: ldr s9, [x8, #0x84]
// 0x10ae940: mov x0, xzr
// 0x10ae944: bl #0x1b9ae58
// 0x10ae948: mov x0, xzr
// 0x10ae94c: mov v8.16b, v0.16b
// 0x10ae950: bl #0x1b9ad30
// 0x10ae954: adrp x8, #0x832000
// 0x10ae958: ldr s1, [x8, #0x4f4]
// 0x10ae95c: fmul s1, s8, s1
// 0x10ae960: fadd s1, s9, s1
// 0x10ae964: fcmp s1, s0
// 0x10ae968: b.pl #0x10ae998
// 0x10ae96c: ldrb w8, [x19, #0xf0]
// 0x10ae970: cbz w8, #0x10ae9a0
// 0x10ae974: ldr x8, [x19, #0x40]
// 0x10ae978: cbz x8, #0x10aef38
// 0x10ae97c: ldur d0, [x8, #0xe4]
// 0x10ae980: mov w8, #0x126f
// 0x10ae984: movk w8, #0xbb03, lsl #16
// 0x10ae988: dup v1.2s, w8
// 0x10ae98c: fmul v0.2s, v0.2s, v1.2s
// 0x10ae990: str d0, [x19, #0xa8]
// 0x10ae994: b #0x10aea58
// 0x10ae998: ldr s0, [x19, #0xa8]
// 0x10ae99c: b #0x10aea58
// 0x10ae9a0: ldr s0, [x19, #0x88]
// 0x10ae9a4: ldr s1, [x19, #0x7c]
// 0x10ae9a8: mov w8, #0x43b40000
// 0x10ae9ac: fmov s8, w8
// 0x10ae9b0: mov w8, #-0x3c4c0000
// 0x10ae9b4: fsub s0, s1, s0
// 0x10ae9b8: fdiv s1, s0, s8
// 0x10ae9bc: fmov s10, w8
// 0x10ae9c0: frintm s1, s1
// 0x10ae9c4: fmul s1, s1, s10
// 0x10ae9c8: fadd s0, s0, s1
// 0x10ae9cc: fmov s9, wzr
// 0x10ae9d0: mov w8, #0x43340000
// 0x10ae9d4: ldr s11, [x19, #0xb4]
// 0x10ae9d8: fmin s1, s0, s8
// 0x10ae9dc: fcmp s0, #0.0
// 0x10ae9e0: fmov s12, w8
// 0x10ae9e4: fcsel s0, s1, s9, pl
// 0x10ae9e8: fadd s1, s0, s10
// 0x10ae9ec: fcmp s0, s12
// 0x10ae9f0: mov x0, xzr
// 0x10ae9f4: fcsel s13, s1, s0, gt
// 0x10ae9f8: bl #0x1b89b60
// 0x10ae9fc: ldr s1, [x19, #0x8c]
// 0x10aea00: ldr s2, [x19, #0x80]
// 0x10aea04: fdiv s0, s11, s0
// 0x10aea08: fmul s0, s0, s13
// 0x10aea0c: str s0, [x19, #0xac]
// 0x10aea10: fsub s0, s2, s1
// 0x10aea14: fdiv s1, s0, s8
// 0x10aea18: frintm s1, s1
// 0x10aea1c: fmul s1, s1, s10
// 0x10aea20: fadd s0, s0, s1
// 0x10aea24: ldr s11, [x19, #0xb4]
// 0x10aea28: fmin s1, s0, s8
// 0x10aea2c: fcmp s0, #0.0
// 0x10aea30: fcsel s0, s1, s9, pl
// 0x10aea34: fadd s1, s0, s10
// 0x10aea38: fcmp s0, s12
// 0x10aea3c: mov x0, xzr
// 0x10aea40: fcsel s8, s1, s0, gt
// 0x10aea44: bl #0x1b89b60
// 0x10aea48: fneg s1, s11
// 0x10aea4c: fdiv s0, s1, s0
// 0x10aea50: fmul s0, s0, s8
// 0x10aea54: str s0, [x19, #0xa8]
// 0x10aea58: ldr x8, [x19, #0x28]
// 0x10aea5c: cbz x8, #0x10aef38
// 0x10aea60: ldr s1, [x19, #0xb0]
// 0x10aea64: mov w9, #0x43b40000
// 0x10aea68: fmov s12, w9
// 0x10aea6c: mov w10, #-0x3c4c0000
// 0x10aea70: fneg s2, s1
// 0x10aea74: fcmp s0, s1
// 0x10aea78: fcsel s3, s1, s0, gt
// 0x10aea7c: fcmp s0, s2
// 0x10aea80: fcsel s0, s3, s2, pl
// 0x10aea84: str s0, [x8, #0x250]
// 0x10aea88: ldr s0, [x19, #0xac]
// 0x10aea8c: fmov s11, w10
// 0x10aea90: fmov s14, wzr
// 0x10aea94: mov x0, xzr
// 0x10aea98: fcmp s0, s1
// 0x10aea9c: fcsel s1, s1, s0, gt
// 0x10aeaa0: fcmp s0, s2
// 0x10aeaa4: fcsel s0, s1, s2, pl
// 0x10aeaa8: str s0, [x8, #0x254]
// 0x10aeaac: ldr s0, [x19, #0x94]
// 0x10aeab0: ldr s1, [x19, #0x80]
// 0x10aeab4: mov w8, #0x43340000
// 0x10aeab8: ldr s8, [x19, #0xb8]
// 0x10aeabc: ldr s9, [x19, #0xc0]
// 0x10aeac0: fsub s0, s1, s0
// 0x10aeac4: fdiv s1, s0, s12
// 0x10aeac8: frintm s1, s1
// 0x10aeacc: fmul s1, s1, s11
// 0x10aead0: fadd s0, s0, s1
// 0x10aead4: fmin s1, s0, s12
// 0x10aead8: fcmp s0, #0.0
// 0x10aeadc: fmov s13, w8
// 0x10aeae0: fcsel s0, s1, s14, pl
// 0x10aeae4: fadd s1, s0, s11
// 0x10aeae8: fcmp s0, s13
// 0x10aeaec: fcsel s10, s1, s0, gt
// 0x10aeaf0: bl #0x1b89b60
// 0x10aeaf4: fneg s1, s9
// 0x10aeaf8: ldr s2, [x19, #0x98]
// 0x10aeafc: ldr s3, [x19, #0x7c]
// 0x10aeb00: fmov s4, #3.00000000
// 0x10aeb04: fmul s1, s10, s1
// 0x10aeb08: fmul s1, s1, s4
// 0x10aeb0c: fsub s1, s1, s8
// 0x10aeb10: fsub s2, s3, s2
// 0x10aeb14: fdiv s3, s1, s12
// 0x10aeb18: frintm s3, s3
// 0x10aeb1c: fmul s3, s3, s11
// 0x10aeb20: fadd s1, s1, s3
// 0x10aeb24: fdiv s3, s2, s12
// 0x10aeb28: frintm s3, s3
// 0x10aeb2c: fcmp s1, #0.0
// 0x10aeb30: fmin s1, s1, s12
// 0x10aeb34: fmul s3, s3, s11
// 0x10aeb38: fcsel s1, s1, s14, pl
// 0x10aeb3c: fmov s10, #5.00000000
// 0x10aeb40: fadd s2, s2, s3
// 0x10aeb44: fadd s3, s1, s11
// 0x10aeb48: fcmp s1, s13
// 0x10aeb4c: fcsel s1, s3, s1, gt
// 0x10aeb50: fmov s3, #1.00000000
// 0x10aeb54: fmul s0, s0, s10
// 0x10aeb58: fcmp s0, #0.0
// 0x10aeb5c: fmin s0, s0, s3
// 0x10aeb60: fcsel s0, s0, s14, pl
// 0x10aeb64: fmul s0, s0, s1
// 0x10aeb68: fadd s0, s8, s0
// 0x10aeb6c: ldp s9, s8, [x19, #0xbc]
// 0x10aeb70: fcmp s2, #0.0
// 0x10aeb74: fmin s1, s2, s12
// 0x10aeb78: fcsel s1, s1, s14, pl
// 0x10aeb7c: str s0, [x19, #0xb8]
// 0x10aeb80: fadd s0, s1, s11
// 0x10aeb84: fcmp s1, s13
// 0x10aeb88: mov x0, xzr
// 0x10aeb8c: fcsel s15, s0, s1, gt
// 0x10aeb90: bl #0x1b89b60
// 0x10aeb94: fneg s1, s8
// 0x10aeb98: fmul s1, s15, s1
// 0x10aeb9c: fmov s2, #3.00000000
// 0x10aeba0: fmul s1, s1, s2
// 0x10aeba4: fsub s1, s1, s9
// 0x10aeba8: fdiv s2, s1, s12
// 0x10aebac: frintm s2, s2
// 0x10aebb0: fmul s2, s2, s11
// 0x10aebb4: fadd s1, s1, s2
// 0x10aebb8: fmin s2, s1, s12
// 0x10aebbc: fcmp s1, #0.0
// 0x10aebc0: fcsel s1, s2, s14, pl
// 0x10aebc4: fadd s2, s1, s11
// 0x10aebc8: fcmp s1, s13
// 0x10aebcc: fmul s0, s0, s10
// 0x10aebd0: fcsel s1, s2, s1, gt
// 0x10aebd4: fmov s2, #1.00000000
// 0x10aebd8: fmin s2, s0, s2
// 0x10aebdc: fcmp s0, #0.0
// 0x10aebe0: ldr s8, [x19, #0x88]
// 0x10aebe4: ldr s15, [x19, #0x7c]
// 0x10aebe8: ldr s10, [x19, #0x68]
// 0x10aebec: fcsel s0, s2, s14, pl
// 0x10aebf0: fmul s0, s0, s1
// 0x10aebf4: fadd s0, s9, s0
// 0x10aebf8: mov x0, xzr
// 0x10aebfc: str s0, [x19, #0xbc]
// 0x10aec00: add x20, x19, #0x6c
// 0x10aec04: bl #0x1b89b60
// 0x10aec08: mov v4.16b, v0.16b
// 0x10aec0c: fsub s0, s15, s8
// 0x10aec10: fdiv s1, s0, s12
// 0x10aec14: frintm s1, s1
// 0x10aec18: fmul s1, s1, s11
// 0x10aec1c: fadd s0, s0, s1
// 0x10aec20: fmin s1, s0, s12
// 0x10aec24: fcmp s0, #0.0
// 0x10aec28: fcsel s0, s1, s14, pl
// 0x10aec2c: fadd s1, s0, s11
// 0x10aec30: fcmp s0, s13
// 0x10aec34: mov w8, #0x7f800000
// 0x10aec38: fcsel s0, s1, s0, gt
// 0x10aec3c: fmov s9, w8
// 0x10aec40: fadd s1, s8, s0
// 0x10aec44: mov v0.16b, v8.16b
// 0x10aec48: mov x0, x20
// 0x10aec4c: mov v2.16b, v10.16b
// 0x10aec50: mov v3.16b, v9.16b
// 0x10aec54: mov x1, xzr
// 0x10aec58: bl #0x1b8c860
// 0x10aec5c: ldr s8, [x19, #0x8c]
// 0x10aec60: ldr s15, [x19, #0x80]
// 0x10aec64: ldr s10, [x19, #0x68]
// 0x10aec68: mov x0, xzr
// 0x10aec6c: str s0, [x19, #0x88]
// 0x10aec70: add x20, x19, #0x70
// 0x10aec74: bl #0x1b89b60
// 0x10aec78: mov v4.16b, v0.16b
// 0x10aec7c: fsub s0, s15, s8
// 0x10aec80: fdiv s1, s0, s12
// 0x10aec84: frintm s1, s1
// 0x10aec88: fmul s1, s1, s11
// 0x10aec8c: fadd s0, s0, s1
// 0x10aec90: fmin s1, s0, s12
// 0x10aec94: fcmp s0, #0.0
// 0x10aec98: fcsel s0, s1, s14, pl
// 0x10aec9c: fadd s1, s0, s11
// 0x10aeca0: fcmp s0, s13
// 0x10aeca4: fcsel s0, s1, s0, gt
// 0x10aeca8: fadd s1, s8, s0
// 0x10aecac: mov v0.16b, v8.16b
// 0x10aecb0: mov x0, x20
// 0x10aecb4: mov v2.16b, v10.16b
// 0x10aecb8: mov v3.16b, v9.16b
// 0x10aecbc: mov x1, xzr
// 0x10aecc0: bl #0x1b8c860
// 0x10aecc4: ldr s10, [x19, #0x94]
// 0x10aecc8: ldr s8, [x19, #0x80]
// 0x10aeccc: mov x0, xzr
// 0x10aecd0: str s0, [x19, #0x8c]
// 0x10aecd4: add x20, x19, #0x74
// 0x10aecd8: bl #0x1b89b60
// 0x10aecdc: mov v4.16b, v0.16b
// 0x10aece0: fsub s0, s8, s10
// 0x10aece4: fdiv s1, s0, s12
// 0x10aece8: frintm s1, s1
// 0x10aecec: fmul s1, s1, s11
// 0x10aecf0: fadd s0, s0, s1
// 0x10aecf4: fmin s1, s0, s12
// 0x10aecf8: fcmp s0, #0.0
// 0x10aecfc: ldr s8, [x21, #0x520]
// 0x10aed00: fcsel s0, s1, s14, pl
// 0x10aed04: fadd s1, s0, s11
// 0x10aed08: fcmp s0, s13
// 0x10aed0c: fcsel s0, s1, s0, gt
// 0x10aed10: fadd s1, s10, s0
// 0x10aed14: mov v0.16b, v10.16b
// 0x10aed18: mov x0, x20
// 0x10aed1c: mov v2.16b, v8.16b
// 0x10aed20: mov v3.16b, v9.16b
// 0x10aed24: mov x1, xzr
// 0x10aed28: bl #0x1b8c860
// 0x10aed2c: ldr s10, [x19, #0x98]
// 0x10aed30: ldr s15, [x19, #0x7c]
// 0x10aed34: mov x0, xzr
// 0x10aed38: str s0, [x19, #0x94]
// 0x10aed3c: add x20, x19, #0x78
// 0x10aed40: bl #0x1b89b60
// 0x10aed44: mov v4.16b, v0.16b
// 0x10aed48: fsub s0, s15, s10
// 0x10aed4c: fdiv s1, s0, s12
// 0x10aed50: frintm s1, s1
// 0x10aed54: fmul s1, s1, s11
// 0x10aed58: fadd s0, s0, s1
// 0x10aed5c: fmin s1, s0, s12
// 0x10aed60: fcmp s0, #0.0
// 0x10aed64: fcsel s0, s1, s14, pl
// 0x10aed68: fadd s1, s0, s11
// 0x10aed6c: fcmp s0, s13
// 0x10aed70: fcsel s0, s1, s0, gt
// 0x10aed74: fadd s1, s10, s0
// 0x10aed78: mov v0.16b, v10.16b
// 0x10aed7c: mov x0, x20
// 0x10aed80: mov v2.16b, v8.16b
// 0x10aed84: mov v3.16b, v9.16b
// 0x10aed88: mov x1, xzr
// 0x10aed8c: bl #0x1b8c860
// 0x10aed90: ldr x8, [x19, #0x30]
// 0x10aed94: str s0, [x19, #0x98]
// 0x10aed98: cbz x8, #0x10aef38
// 0x10aed9c: ldrb w9, [x8, #0x3a5]
// 0x10aeda0: ldr s9, [x19, #0xf8]
// 0x10aeda4: cbz w9, #0x10aee08
// 0x10aeda8: ldr s10, [x8, #0x604]
// 0x10aedac: mov x0, xzr
// 0x10aedb0: add x20, x19, #0xf4
// 0x10aedb4: bl #0x1b89b60
// 0x10aedb8: mov w8, #0x43b40000
// 0x10aedbc: mov v4.16b, v0.16b
// 0x10aedc0: fsub s0, s10, s9
// 0x10aedc4: fmov s1, w8
// 0x10aedc8: mov w8, #-0x3c4c0000
// 0x10aedcc: fdiv s2, s0, s1
// 0x10aedd0: fmov s3, w8
// 0x10aedd4: frintm s2, s2
// 0x10aedd8: fmul s2, s2, s3
// 0x10aeddc: fadd s0, s0, s2
// 0x10aede0: fmov s2, wzr
// 0x10aede4: mov w8, #0x43340000
// 0x10aede8: fmin s1, s0, s1
// 0x10aedec: fcmp s0, #0.0
// 0x10aedf0: fmov s0, w8
// 0x10aedf4: fcsel s1, s1, s2, pl
// 0x10aedf8: fadd s2, s1, s3
// 0x10aedfc: fcmp s1, s0
// 0x10aee00: fcsel s0, s2, s1, gt
// 0x10aee04: b #0x10aee60
// 0x10aee08: mov x0, xzr
// 0x10aee0c: add x20, x19, #0xf4
// 0x10aee10: bl #0x1b89b60
// 0x10aee14: mov w8, #0x43b40000
// 0x10aee18: fmov s1, wzr
// 0x10aee1c: mov v4.16b, v0.16b
// 0x10aee20: fmov s0, w8
// 0x10aee24: fsub s3, s1, s9
// 0x10aee28: mov w8, #-0x3c4c0000
// 0x10aee2c: fdiv s5, s3, s0
// 0x10aee30: fmov s2, w8
// 0x10aee34: frintm s5, s5
// 0x10aee38: fmul s5, s5, s2
// 0x10aee3c: fadd s3, s3, s5
// 0x10aee40: mov w8, #0x43340000
// 0x10aee44: fmin s0, s3, s0
// 0x10aee48: fcmp s3, #0.0
// 0x10aee4c: fmov s5, w8
// 0x10aee50: fcsel s0, s0, s1, pl
// 0x10aee54: fadd s1, s0, s2
// 0x10aee58: fcmp s0, s5
// 0x10aee5c: fcsel s0, s1, s0, gt
// 0x10aee60: mov w8, #0x7f800000
// 0x10aee64: fadd s1, s9, s0
// 0x10aee68: fmov s3, w8
// 0x10aee6c: mov v0.16b, v9.16b
// 0x10aee70: mov x0, x20
// 0x10aee74: mov v2.16b, v8.16b
// 0x10aee78: mov x1, xzr
// 0x10aee7c: bl #0x1b8c860
// 0x10aee80: ldr x8, [x19, #0x20]
// 0x10aee84: str s0, [x19, #0xf8]
// 0x10aee88: cbz x8, #0x10aef38
// 0x10aee8c: ldr s3, [x8, #0x174]
// 0x10aee90: ldr s4, [x19, #0x84]
// 0x10aee94: fmov s5, #-10.00000000
// 0x10aee98: adrp x8, #0x832000
// 0x10aee9c: ldp s1, s2, [x19, #0x7c]
// 0x10aeea0: fmul s3, s3, s5
// 0x10aeea4: ldr s5, [x8, #0x3e4]
// 0x10aeea8: ldr x20, [x19, #0x60]
// 0x10aeeac: fadd s4, s4, s3
// 0x10aeeb0: fadd s0, s0, s4
// 0x10aeeb4: fmul s3, s1, s5
// 0x10aeeb8: stp s1, s2, [x19, #0x9c]
// 0x10aeebc: fmul s1, s2, s5
// 0x10aeec0: str s0, [x19, #0xa4]
// 0x10aeec4: fmul s2, s0, s5
// 0x10aeec8: mov v0.16b, v3.16b
// 0x10aeecc: mov x0, xzr
// 0x10aeed0: bl #0x1b8b12c
// 0x10aeed4: cbz x20, #0x10aef38
// 0x10aeed8: mov x0, x20
// 0x10aeedc: ldp x20, x19, [sp, #0x50]
// 0x10aeee0: ldp x30, x21, [sp, #0x40]
// 0x10aeee4: ldp d9, d8, [sp, #0x30]
// 0x10aeee8: ldp d11, d10, [sp, #0x20]
// 0x10aeeec: ldp d13, d12, [sp, #0x10]
// 0x10aeef0: mov x1, xzr
// 0x10aeef4: ldp d15, d14, [sp], #0x60
// 0x10aeef8: b #0x1b9d874
// 0x10aeefc: ldr x8, [x20]
// 0x10aef00: cbz x8, #0x10aef38
// 0x10aef04: ldr s0, [x8, #0x204]
// 0x10aef08: fcmp s0, #0.0
// 0x10aef0c: b.ne #0x10ae7c0
// 0x10aef10: adrp x9, #0x832000
// 0x10aef14: ldp s0, s1, [x19, #0xd8]
// 0x10aef18: ldr s2, [x21, #0x520]
// 0x10aef1c: ldr d3, [x9, #0x88]
// 0x10aef20: ldr s4, [x8, #0x334]
// 0x10aef24: fmul s1, s1, s2
// 0x10aef28: fmul v0.2s, v3.2s, v0.s[0]
// 0x10aef2c: fmul s1, s4, s1
// 0x10aef30: fmul v0.2s, v0.2s, v4.s[0]
// 0x10aef34: b #0x10ae7f0
// 0x10aef38: bl #0xf7db74
```

## `GunSway.ctor` — RVA `0xcaef3c`

- Decompiled symbol: `GunSway_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `60` bytes
- Result: `pseudocode`
- Heuristic layout hint: `GunSway_Recovered` matched 5 offsets against `GunSway` metadata (confidence 1.00).

```c
typedef struct GunSway_Recovered {
    char padding_0[104];
    unsigned int dampSpeed;
    char padding_6c[68];
    unsigned long long swingAmt;
    char padding_b8[20];
    uint128_t gunBobRoll;
    uint128_t rollSwayAmount;
    unsigned int sprintBobRollAmount;
} GunSway_Recovered;

long long GunSway_ctor(struct_0 *ptr)
{
    long long v0;  // x0

    ptr->field_68 = 981668463;
    *((unsigned long long *)((char *)&ptr->field_cc + 12)) = 0x3f8000003f800000 CONCAT 0x3f8000003f800000;
    ptr->field_b0 = 4688247213117103145;
    *((uint128_t *)&(&ptr->padding_b8)[1]) = 0x3f8000003f8000004180000041200000;
    *((unsigned int *)((char *)&ptr->field_dc + 12)) = 0x3f800000;
    v0 = MonoBehaviour__ctor();
    return MonoBehaviour__ctor();
}
```
