# Native pseudocode: WeaponPivot

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `WeaponPivot.Start` — RVA `0xcbe58c`

- Decompiled symbol: `WeaponPivot_Start`
- Metadata signature: `private void Start() { }`
- Native interval: `656` bytes
- Result: `pseudocode`
- Heuristic layout hint: `WeaponPivot_Recovered` matched 13 offsets against `WeaponPivot` metadata (confidence 1.00).

```c
typedef struct WeaponPivot_Recovered {
    char padding_0[32];
    struct struct_3 *GunSwayComponent;
    struct struct_6 *FPSPlayerComponent;
    long long FPSWalkerComponent;
    char padding_38[8];
    struct struct_4 *SmoothMouseLookComponent;
    long long InputComponent;
    long long PlayerWeaponsComponent;
    long long IronsightsComponent;
    long long playerObj;
    char padding_68[1];
    char deadzoneLooking;
    char padding_6a[30];
    long long childTransform;
    long long myTransform;
    char padding_98[64];
    long long PivotAnimatorComponent;
    char padding_e0[32];
    unsigned int swayAmt;
} WeaponPivot_Recovered;

typedef struct struct_0 {
    char padding_0[80];
    unsigned long long field_50;
    char padding_58[124];
    unsigned int field_d4;
} struct_0;

typedef struct struct_1 {
    char padding_0[168];
    char field_a8;
} struct_1;

typedef struct struct_2 {
    char padding_0[40];
    long long field_28;
} struct_2;

typedef struct struct_3 {
    char padding_0[80];
    long long field_50;
    char padding_58[124];
    unsigned int field_d4;
} struct_3;

typedef struct struct_6 {
    char padding_0[80];
    long long field_50;
    char padding_58[16];
    long long field_68;
} struct_6;

typedef struct struct_4 {
    char padding_0[168];
    char field_a8;
} struct_4;

extern long long g_1efcf08;
extern long long g_1efcf38;
extern long long g_1efcfc8;
extern long long g_1efebb8;
extern long long g_1efebc0;
extern long long g_1efec08;
extern long long g_1efecd8;
extern char g_1fab4f4;

long long WeaponPivot_Start(struct_5 *ptr)
{
    struct_0 *v0;  // x0
    struct_5 *p;  // x20
    unsigned long long v10[14];  // x0
    struct_5 *addr;  // x21
    struct_5 *v12;  // x21
    long long v13;  // x0
    struct_5 *ptr3;  // x21
    struct_5 *v15;  // x21
    long long v16;  // x0
    struct_5 *ptr4;  // x21
    struct_5 *v18;  // x21
    unsigned long v19;  // x1
    struct_5 *v2;  // x20
    struct_5 *ptr5;  // x21
    struct_5 *v21;  // x21
    unsigned long v22;  // x1
    struct_5 *ptr6;  // x0
    long long v24;  // x1
    struct_5 *ptr7;  // x0
    long long v26;  // x0
    struct_5 *ptr8;  // x21
    struct_5 *v28;  // x21
    long long v29;  // x0
    struct_1 *v3;  // x0
    struct_5 *ptr9;  // x21
    struct_5 *v31;  // x21
    unsigned long v32;  // x0
    unsigned int v33;  // w8
    struct_5 *ptr10;  // x20
    struct_5 *v5;  // x20
    struct_2 *ptr12;  // x0
    long long v7;  // x1
    struct_5 *ptr11;  // x21
    struct_5 *v9;  // x21

    if (!(g_1fab4f4 & 1))
    {
        sub_f7d92c(&g_1efcf08);
        sub_f7d92c(&g_1efcf38);
        sub_f7d92c(&g_1efcfc8);
        sub_f7d92c(&g_1efebb8);
        sub_f7d92c(&g_1efebc0);
        sub_f7d92c(&g_1efec08);
        sub_f7d92c(&g_1efecd8);
        g_1fab4f4 = 1;
    }
    if (Component__get_transform(ptr, 0) && Transform__get_parent() && Component__get_transform())
    {
        v0 = sub_1231bc8();
        p = ptr;
        p->field_20 = v0;
        v2 = &p->field_20;
        sub_f7d8d0(v2, v0);
        if (*((long long *)&v2->padding_0[0]) && *((long long *)(*((long long *)&v2->padding_0[0]) + 80)))
        {
            v3 = sub_1249224(*((long long *)(*((long long *)&v2->padding_0[0]) + 80)), g_1efecd8);
            ptr10 = ptr;
            ptr10->field_40 = v3;
            v5 = &ptr10->field_40;
            sub_f7d8d0(v5, v3);
            if (Camera__get_main(0) && Component__get_transform())
            {
                ptr12 = sub_1231bc8();
                if (ptr12)
                {
                    v7 = ptr12->field_28;
                    ptr11 = ptr;
                    ptr11->field_60 = v7;
                    v9 = &ptr11->field_60;
                    sub_f7d8d0(v9, v7);
                    if (*((long long *)&v9->padding_0[0]))
                    {
                        v10 = sub_1249224(*((long long *)&v9->padding_0[0]), g_1efebb8);
                        addr = ptr;
                        addr->field_28 = v10;
                        v12 = &addr->field_28;
                        sub_f7d8d0(v12, v10);
                        if (v12->padding_38)
                        {
                            v13 = sub_1249224(v12->padding_38, g_1efebc0);
                            ptr3 = ptr;
                            ptr3->field_30 = v13;
                            v15 = &ptr3->field_30;
                            sub_f7d8d0(v15, v13);
                            if (v15->field_30)
                            {
                                v16 = sub_1249224(v15->field_30, g_1efec08);
                                ptr4 = ptr;
                                ptr4->field_48 = v16;
                                v18 = &ptr4->field_48;
                                sub_f7d8d0(v18, v16);
                                if (v18->field_20)
                                {
                                    v19 = *((long long *)&v18->field_20->padding_58[16]);
                                    ptr5 = ptr;
                                    ptr5->field_50 = v19;
                                    v21 = &ptr5->field_50;
                                    sub_f7d8d0(v21, v19);
                                    if (v21->field_28)
                                    {
                                        v22 = v21->field_28->field_50;
                                        ptr6 = ptr;
                                        ptr6->field_58 = v22;
                                        sub_f7d8d0(&ptr6->field_58, v22);
                                        v24 = sub_1231bc8(ptr, g_1efcf08);
                                        ptr7 = ptr;
                                        ptr7->field_d8 = v24;
                                        sub_f7d8d0(&ptr7->field_d8, v24);
                                        v26 = Component__get_transform(ptr, 0);
                                        ptr8 = ptr;
                                        ptr8->field_90 = v26;
                                        v28 = &ptr8->field_90;
                                        sub_f7d8d0(v28, v26);
                                        if (*((long long *)&v28->padding_0[0]))
                                        {
                                            v29 = Transform__GetChild(*((long long *)&v28->padding_0[0]), 0, 0);
                                            ptr9 = ptr;
                                            ptr9->field_88 = v29;
                                            v31 = &ptr9->field_88;
                                            v32 = sub_f7d8d0(v31, v29);
                                            if (*((long long *)&v31->padding_68))
                                            {
                                                v33 = ptr->field_69;
                                                ptr->field_100 = *((int *)(*((long long *)&v31->padding_68) + 212));
                                                if (!v33)
                                                {
                                                    return v32;
                                                }
                                                else if (*((long long *)&v5->padding_0[0]))
                                                {
                                                    *((char *)(*((long long *)&v5->padding_0[0]) + 168)) = 1;
                                                    return v32;
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
    sub_f7db74();
}
```


## `WeaponPivot.Update` — RVA `0xcbe81c`

- Decompiled symbol: `WeaponPivot_Update`
- Metadata signature: `private void Update() { }`
- Native interval: `3652` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: Decompiler produced no C-like text

```c
// 0x10be81c: sub sp, sp, #0x90
// 0x10be820: stp d15, d14, [sp, #0x10]
// 0x10be824: stp d13, d12, [sp, #0x20]
// 0x10be828: stp d11, d10, [sp, #0x30]
// 0x10be82c: stp d9, d8, [sp, #0x40]
// 0x10be830: str x30, [sp, #0x50]
// 0x10be834: stp x24, x23, [sp, #0x60]
// 0x10be838: stp x22, x21, [sp, #0x70]
// 0x10be83c: stp x20, x19, [sp, #0x80]
// 0x10be840: adrp x20, #0x1fab000
// 0x10be844: ldrb w8, [x20, #0x4f5]
// 0x10be848: mov x19, x0
// 0x10be84c: tbnz w8, #0, #0x10be864
// 0x10be850: adrp x0, #0x1e8c000
// 0x10be854: ldr x0, [x0, #0x458]
// 0x10be858: bl #0xf7d92c
// 0x10be85c: mov w8, #1
// 0x10be860: strb w8, [x20, #0x4f5]
// 0x10be864: ldr x8, [x19, #0x50]
// 0x10be868: cbz x8, #0x10bf640
// 0x10be86c: ldr x1, [x8, #0x98]
// 0x10be870: mov x20, x19
// 0x10be874: str x1, [x20, #0x38]!
// 0x10be878: mov x0, x20
// 0x10be87c: bl #0xf7d8d0
// 0x10be880: mov x0, xzr
// 0x10be884: bl #0x1b9ae58
// 0x10be888: fcmp s0, #0.0
// 0x10be88c: b.le #0x10becdc
// 0x10be890: mov x0, xzr
// 0x10be894: bl #0x1b9ae30
// 0x10be898: fcmp s0, #0.0
// 0x10be89c: b.le #0x10becdc
// 0x10be8a0: mov x0, xzr
// 0x10be8a4: bl #0x1b89b60
// 0x10be8a8: fcmp s0, #0.0
// 0x10be8ac: b.le #0x10becdc
// 0x10be8b0: ldrb w8, [x19, #0x68]
// 0x10be8b4: cbnz w8, #0x10be8c8
// 0x10be8b8: ldr x8, [x19, #0x40]
// 0x10be8bc: cbz x8, #0x10bf640
// 0x10be8c0: ldrb w8, [x8, #0xaa]
// 0x10be8c4: cbz w8, #0x10bed6c
// 0x10be8c8: strb wzr, [x19, #0x69]
// 0x10be8cc: ldr x0, [x19, #0x90]
// 0x10be8d0: cbz x0, #0x10bf640
// 0x10be8d4: mov x1, xzr
// 0x10be8d8: bl #0x1b9d7c8
// 0x10be8dc: ldr x0, [x19, #0x90]
// 0x10be8e0: cbz x0, #0x10bf640
// 0x10be8e4: mov x1, xzr
// 0x10be8e8: mov v8.16b, v1.16b
// 0x10be8ec: bl #0x1b9d7c8
// 0x10be8f0: mov w8, #0x43b40000
// 0x10be8f4: mov w9, #0x43340000
// 0x10be8f8: ldr x0, [x19, #0x88]
// 0x10be8fc: fmov s2, w8
// 0x10be900: fneg s0, s1
// 0x10be904: fsub s1, s2, s1
// 0x10be908: fmov s2, w9
// 0x10be90c: fcmp s8, s2
// 0x10be910: fcsel s0, s0, s1, mi
// 0x10be914: str s0, [x19, #0xa0]
// 0x10be918: cbz x0, #0x10bf640
// 0x10be91c: mov x1, xzr
// 0x10be920: bl #0x1b9d7c8
// 0x10be924: ldr x0, [x19, #0x88]
// 0x10be928: cbz x0, #0x10bf640
// 0x10be92c: mov x1, xzr
// 0x10be930: mov v8.16b, v0.16b
// 0x10be934: bl #0x1b9d7c8
// 0x10be938: mov w8, #0x43b40000
// 0x10be93c: mov w9, #0x43340000
// 0x10be940: ldr x0, [x19, #0x88]
// 0x10be944: fmov s2, w8
// 0x10be948: fneg s1, s0
// 0x10be94c: fsub s0, s2, s0
// 0x10be950: fmov s2, w9
// 0x10be954: fcmp s8, s2
// 0x10be958: fcsel s0, s1, s0, mi
// 0x10be95c: str s0, [x19, #0x9c]
// 0x10be960: cbz x0, #0x10bf640
// 0x10be964: mov x1, xzr
// 0x10be968: bl #0x1b9d7c8
// 0x10be96c: ldr x0, [x19, #0x88]
// 0x10be970: cbz x0, #0x10bf640
// 0x10be974: mov x1, xzr
// 0x10be978: mov v8.16b, v0.16b
// 0x10be97c: bl #0x1b9d7c8
// 0x10be980: mov w8, #0x43b40000
// 0x10be984: mov w9, #0x43340000
// 0x10be988: ldrb w10, [x19, #0x69]
// 0x10be98c: fmov s1, w8
// 0x10be990: fsub s1, s1, s0
// 0x10be994: fmov s2, w9
// 0x10be998: fneg s1, s1
// 0x10be99c: fcmp s8, s2
// 0x10be9a0: fcsel s0, s1, s0, gt
// 0x10be9a4: str s0, [x19, #0x98]
// 0x10be9a8: cbz w10, #0x10be9cc
// 0x10be9ac: ldr x8, [x20]
// 0x10be9b0: cbz x8, #0x10bf640
// 0x10be9b4: ldrb w8, [x8, #0x1f5]
// 0x10be9b8: cbnz w8, #0x10be9cc
// 0x10be9bc: ldr x8, [x19, #0x40]
// 0x10be9c0: cbz x8, #0x10bf640
// 0x10be9c4: ldrb w9, [x8, #0xaa]
// 0x10be9c8: cbz w9, #0x10bf074
// 0x10be9cc: ldrb w8, [x19, #0xf8]
// 0x10be9d0: cbnz w8, #0x10bea34
// 0x10be9d4: ldr x8, [x19, #0x28]
// 0x10be9d8: cbz x8, #0x10bf640
// 0x10be9dc: ldrb w8, [x8, #0x2d0]
// 0x10be9e0: cbz w8, #0x10bea14
// 0x10be9e4: ldr x20, [x19, #0x40]
// 0x10be9e8: cbz x20, #0x10bf640
// 0x10be9ec: ldr s1, [x20, #0x54]
// 0x10be9f0: fsub s0, s1, s0
// 0x10be9f4: str s0, [x20, #0x54]
// 0x10be9f8: ldr x0, [x19, #0x90]
// 0x10be9fc: cbz x0, #0x10bf640
// 0x10bea00: ldr s8, [x20, #0x50]
// 0x10bea04: mov x1, xzr
// 0x10bea08: bl #0x1b9d7c8
// 0x10bea0c: fadd s0, s8, s1
// 0x10bea10: str s0, [x20, #0x50]
// 0x10bea14: ldr x8, [x19, #0x40]
// 0x10bea18: cbz x8, #0x10bf640
// 0x10bea1c: strb wzr, [x8, #0xa8]
// 0x10bea20: ldr x8, [x19, #0x20]
// 0x10bea24: cbz x8, #0x10bf640
// 0x10bea28: strb wzr, [x8, #0xf0]
// 0x10bea2c: mov w8, #1
// 0x10bea30: strb w8, [x19, #0xf8]
// 0x10bea34: ldr x20, [x19, #0x90]
// 0x10bea38: cbz x20, #0x10bf640
// 0x10bea3c: mov x0, x20
// 0x10bea40: mov x1, xzr
// 0x10bea44: bl #0x1b9cb18
// 0x10bea48: adrp x21, #0x1fab000
// 0x10bea4c: ldrb w8, [x21, #0x2c9]
// 0x10bea50: mov v8.16b, v0.16b
// 0x10bea54: mov v10.16b, v1.16b
// 0x10bea58: mov v15.16b, v2.16b
// 0x10bea5c: cbnz w8, #0x10bea74
// 0x10bea60: adrp x0, #0x1e8c000
// 0x10bea64: ldr x0, [x0, #0x1e8]
// 0x10bea68: bl #0xf7d92c
// 0x10bea6c: mov w8, #1
// 0x10bea70: strb w8, [x21, #0x2c9]
// 0x10bea74: adrp x23, #0x1e8c000
// 0x10bea78: ldr x23, [x23, #0x1e8]
// 0x10bea7c: mov x0, xzr
// 0x10bea80: ldr x8, [x23]
// 0x10bea84: ldr x8, [x8, #0xb8]
// 0x10bea88: ldp s11, s12, [x8]
// 0x10bea8c: ldr s13, [x8, #8]
// 0x10bea90: bl #0x1b9ae30
// 0x10bea94: adrp x22, #0x1fab000
// 0x10bea98: ldrb w8, [x22, #0x4d2]
// 0x10bea9c: mov v14.16b, v0.16b
// 0x10beaa0: adrp x24, #0x832000
// 0x10beaa4: cbnz w8, #0x10beabc
// 0x10beaa8: adrp x0, #0x1e8c000
// 0x10beaac: ldr x0, [x0, #0xa60]
// 0x10beab0: bl #0xf7d92c
// 0x10beab4: mov w8, #1
// 0x10beab8: strb w8, [x22, #0x4d2]
// 0x10beabc: fsub s9, s11, s8
// 0x10beac0: mov v3.16b, v8.16b
// 0x10beac4: fsub s8, s12, s10
// 0x10beac8: ldr s2, [x24, #0x538]
// 0x10beacc: mov v5.16b, v15.16b
// 0x10bead0: fsub s15, s13, s15
// 0x10bead4: fmul s0, s9, s9
// 0x10bead8: fmul s1, s8, s8
// 0x10beadc: fadd s0, s0, s1
// 0x10beae0: fmul s1, s15, s15
// 0x10beae4: mov v4.16b, v10.16b
// 0x10beae8: fadd s10, s1, s0
// 0x10beaec: fcmp s10, #0.0
// 0x10beaf0: str s2, [sp, #0x5c]
// 0x10beaf4: b.eq #0x10beb64
// 0x10beaf8: fmul s14, s14, s2
// 0x10beafc: fcmp s14, #0.0
// 0x10beb00: stp s5, s4, [sp, #8]
// 0x10beb04: str s3, [sp, #0x58]
// 0x10beb08: b.lt #0x10beb18
// 0x10beb0c: fmul s0, s14, s14
// 0x10beb10: fcmp s10, s0
// 0x10beb14: b.ls #0x10beb64
// 0x10beb18: adrp x8, #0x1e8c000
// 0x10beb1c: ldr x8, [x8, #0xa60]
// 0x10beb20: ldr x0, [x8]
// 0x10beb24: ldr w8, [x0, #0xe0]
// 0x10beb28: cbnz w8, #0x10beb30
// 0x10beb2c: bl #0xf7da5c
// 0x10beb30: ldr s3, [sp, #0x58]
// 0x10beb34: fsqrt s0, s10
// 0x10beb38: fdiv s1, s9, s0
// 0x10beb3c: fmul s1, s14, s1
// 0x10beb40: fadd s11, s3, s1
// 0x10beb44: ldr s1, [sp, #0xc]
// 0x10beb48: fdiv s2, s8, s0
// 0x10beb4c: fmul s2, s14, s2
// 0x10beb50: fdiv s0, s15, s0
// 0x10beb54: fadd s12, s1, s2
// 0x10beb58: ldr s1, [sp, #8]
// 0x10beb5c: fmul s0, s14, s0
// 0x10beb60: fadd s13, s1, s0
// 0x10beb64: mov x0, x20
// 0x10beb68: mov v0.16b, v11.16b
// 0x10beb6c: mov v1.16b, v12.16b
// 0x10beb70: mov v2.16b, v13.16b
// 0x10beb74: mov x1, xzr
// 0x10beb78: bl #0x1b9cba4
// 0x10beb7c: ldr x20, [x19, #0x88]
// 0x10beb80: cbz x20, #0x10bf640
// 0x10beb84: mov x0, x20
// 0x10beb88: mov x1, xzr
// 0x10beb8c: bl #0x1b9cb18
// 0x10beb90: ldrb w8, [x21, #0x2c9]
// 0x10beb94: mov v8.16b, v0.16b
// 0x10beb98: mov v10.16b, v1.16b
// 0x10beb9c: mov v15.16b, v2.16b
// 0x10beba0: cbnz w8, #0x10bebb8
// 0x10beba4: adrp x0, #0x1e8c000
// 0x10beba8: ldr x0, [x0, #0x1e8]
// 0x10bebac: bl #0xf7d92c
// 0x10bebb0: mov w8, #1
// 0x10bebb4: strb w8, [x21, #0x2c9]
// 0x10bebb8: ldr x8, [x23]
// 0x10bebbc: mov x0, xzr
// 0x10bebc0: ldr x8, [x8, #0xb8]
// 0x10bebc4: ldp s11, s12, [x8]
// 0x10bebc8: ldr s13, [x8, #8]
// 0x10bebcc: bl #0x1b9ae30
// 0x10bebd0: ldrb w8, [x22, #0x4d2]
// 0x10bebd4: mov v14.16b, v0.16b
// 0x10bebd8: cbnz w8, #0x10bebf0
// 0x10bebdc: adrp x0, #0x1e8c000
// 0x10bebe0: ldr x0, [x0, #0xa60]
// 0x10bebe4: bl #0xf7d92c
// 0x10bebe8: mov w8, #1
// 0x10bebec: strb w8, [x22, #0x4d2]
// 0x10bebf0: fsub s9, s11, s8
// 0x10bebf4: mov v2.16b, v8.16b
// 0x10bebf8: fsub s8, s12, s10
// 0x10bebfc: mov v4.16b, v15.16b
// 0x10bec00: fsub s15, s13, s15
// 0x10bec04: fmul s0, s9, s9
// 0x10bec08: fmul s1, s8, s8
// 0x10bec0c: fadd s0, s0, s1
// 0x10bec10: fmul s1, s15, s15
// 0x10bec14: mov v3.16b, v10.16b
// 0x10bec18: fadd s10, s1, s0
// 0x10bec1c: fcmp s10, #0.0
// 0x10bec20: b.eq #0x10bec94
// 0x10bec24: ldr s0, [sp, #0x5c]
// 0x10bec28: stp s4, s3, [sp, #8]
// 0x10bec2c: str s2, [sp, #0x58]
// 0x10bec30: fmul s14, s14, s0
// 0x10bec34: fcmp s14, #0.0
// 0x10bec38: b.lt #0x10bec48
// 0x10bec3c: fmul s0, s14, s14
// 0x10bec40: fcmp s10, s0
// 0x10bec44: b.ls #0x10bec94
// 0x10bec48: adrp x8, #0x1e8c000
// 0x10bec4c: ldr x8, [x8, #0xa60]
// 0x10bec50: ldr x0, [x8]
// 0x10bec54: ldr w8, [x0, #0xe0]
// 0x10bec58: cbnz w8, #0x10bec60
// 0x10bec5c: bl #0xf7da5c
// 0x10bec60: ldr s3, [sp, #0x58]
// 0x10bec64: fsqrt s0, s10
// 0x10bec68: fdiv s1, s9, s0
// 0x10bec6c: fmul s1, s14, s1
// 0x10bec70: fadd s11, s3, s1
// 0x10bec74: ldr s1, [sp, #0xc]
// 0x10bec78: fdiv s2, s8, s0
// 0x10bec7c: fmul s2, s14, s2
// 0x10bec80: fdiv s0, s15, s0
// 0x10bec84: fadd s12, s1, s2
// 0x10bec88: ldr s1, [sp, #8]
// 0x10bec8c: fmul s0, s14, s0
// 0x10bec90: fadd s13, s1, s0
// 0x10bec94: mov x0, x20
// 0x10bec98: mov v0.16b, v11.16b
// 0x10bec9c: mov v1.16b, v12.16b
// 0x10beca0: mov v2.16b, v13.16b
// 0x10beca4: mov x1, xzr
// 0x10beca8: bl #0x1b9cba4
// 0x10becac: ldrb w8, [x19, #0x6b]
// 0x10becb0: cbz w8, #0x10bed04
// 0x10becb4: ldrb w8, [x19, #0x6d]
// 0x10becb8: cbz w8, #0x10beccc
// 0x10becbc: ldr x8, [x19, #0x40]
// 0x10becc0: cbz x8, #0x10bf640
// 0x10becc4: ldrb w8, [x8, #0xaa]
// 0x10becc8: cbz w8, #0x10beda4
// 0x10beccc: ldr x8, [x19, #0x28]
// 0x10becd0: cbz x8, #0x10bf640
// 0x10becd4: mov w9, wzr
// 0x10becd8: b #0x10bedb0
// 0x10becdc: ldp x20, x19, [sp, #0x80]
// 0x10bece0: ldp x22, x21, [sp, #0x70]
// 0x10bece4: ldp x24, x23, [sp, #0x60]
// 0x10bece8: ldr x30, [sp, #0x50]
// 0x10becec: ldp d9, d8, [sp, #0x40]
// 0x10becf0: ldp d11, d10, [sp, #0x30]
// 0x10becf4: ldp d13, d12, [sp, #0x20]
// 0x10becf8: ldp d15, d14, [sp, #0x10]
// 0x10becfc: add sp, sp, #0x90
// 0x10bed00: ret
// 0x10bed04: ldr x8, [x19, #0x28]
// 0x10bed08: cbz x8, #0x10bf640
// 0x10bed0c: strb wzr, [x8, #0x3cc]
// 0x10bed10: ldr x9, [x19, #0x20]
// 0x10bed14: cbz x9, #0x10bf640
// 0x10bed18: ldr s0, [x19, #0x100]
// 0x10bed1c: str s0, [x9, #0xd4]
// 0x10bed20: ldrb w8, [x8, #0x2d0]
// 0x10bed24: ldr s8, [x19, #0xec]
// 0x10bed28: ldr s10, [x19, #0xa0]
// 0x10bed2c: ldr s11, [x19, #0x7c]
// 0x10bed30: cbnz w8, #0x10bede8
// 0x10bed34: ldr x8, [x19, #0x58]
// 0x10bed38: cbz x8, #0x10bf640
// 0x10bed3c: ldr x9, [x8, #0x28]
// 0x10bed40: cbz x9, #0x10bf640
// 0x10bed44: ldr s12, [x9, #0x44]
// 0x10bed48: ldr s13, [x8, #0x1d8]
// 0x10bed4c: mov x0, xzr
// 0x10bed50: add x20, x19, #0xc8
// 0x10bed54: bl #0x1b9ae30
// 0x10bed58: mov v9.16b, v0.16b
// 0x10bed5c: fmul s0, s10, s11
// 0x10bed60: fmul s1, s12, s13
// 0x10bed64: fsub s10, s0, s1
// 0x10bed68: b #0x10bedfc
// 0x10bed6c: ldr x8, [x19, #0x28]
// 0x10bed70: cbz x8, #0x10bf640
// 0x10bed74: ldrb w9, [x8, #0x2d0]
// 0x10bed78: cbz w9, #0x10bf3d4
// 0x10bed7c: ldrb w9, [x19, #0x69]
// 0x10bed80: ldr x8, [x19, #0x30]
// 0x10bed84: cbz w9, #0x10bf430
// 0x10bed88: cbz x8, #0x10bf640
// 0x10bed8c: ldrb w9, [x8, #0x2b1]
// 0x10bed90: cbz w9, #0x10bf434
// 0x10bed94: mov w9, #1
// 0x10bed98: strb wzr, [x19, #0x69]
// 0x10bed9c: strb w9, [x19, #0xf9]
// 0x10beda0: b #0x10bf434
// 0x10beda4: ldr x8, [x19, #0x28]
// 0x10beda8: cbz x8, #0x10bf640
// 0x10bedac: mov w9, #1
// 0x10bedb0: ldrb w10, [x8, #0x2d0]
// 0x10bedb4: strb w9, [x8, #0x3cc]
// 0x10bedb8: cbnz w10, #0x10bedcc
// 0x10bedbc: ldr x8, [x19, #0x30]
// 0x10bedc0: cbz x8, #0x10bf640
// 0x10bedc4: ldrb w8, [x8, #0x2b1]
// 0x10bedc8: cbz w8, #0x10bf0f4
// 0x10bedcc: ldr x8, [x19, #0x20]
// 0x10bedd0: cbz x8, #0x10bf640
// 0x10bedd4: ldr s0, [x19, #0x100]
// 0x10bedd8: str s0, [x8, #0xd4]
// 0x10beddc: ldr s8, [x19, #0xec]
// 0x10bede0: ldr s10, [x19, #0xa0]
// 0x10bede4: ldr s11, [x19, #0x7c]
// 0x10bede8: mov x0, xzr
// 0x10bedec: add x20, x19, #0xc8
// 0x10bedf0: bl #0x1b9ae30
// 0x10bedf4: mov v9.16b, v0.16b
// 0x10bedf8: fmul s10, s10, s11
// 0x10bedfc: mov x0, xzr
// 0x10bee00: bl #0x1b89b60
// 0x10bee04: mov w8, #0x43b40000
// 0x10bee08: mov v4.16b, v0.16b
// 0x10bee0c: fsub s0, s10, s8
// 0x10bee10: fmov s11, w8
// 0x10bee14: mov w8, #-0x3c4c0000
// 0x10bee18: fdiv s1, s0, s11
// 0x10bee1c: fmov s13, w8
// 0x10bee20: frintm s1, s1
// 0x10bee24: fmul s1, s1, s13
// 0x10bee28: fadd s0, s0, s1
// 0x10bee2c: fmov s2, wzr
// 0x10bee30: mov w8, #0x43340000
// 0x10bee34: fmin s1, s0, s11
// 0x10bee38: fcmp s0, #0.0
// 0x10bee3c: fmov s14, w8
// 0x10bee40: fcsel s0, s1, s2, pl
// 0x10bee44: fadd s1, s0, s13
// 0x10bee48: fcmp s0, s14
// 0x10bee4c: mov w8, #0x7f800000
// 0x10bee50: fcsel s0, s1, s0, gt
// 0x10bee54: fmov s10, w8
// 0x10bee58: fadd s1, s8, s0
// 0x10bee5c: mov v0.16b, v8.16b
// 0x10bee60: mov x0, x20
// 0x10bee64: mov v2.16b, v9.16b
// 0x10bee68: mov v3.16b, v10.16b
// 0x10bee6c: mov x1, xzr
// 0x10bee70: bl #0x1b8c860
// 0x10bee74: ldr s8, [x19, #0xe0]
// 0x10bee78: ldr s15, [x19, #0x9c]
// 0x10bee7c: ldr s12, [x19, #0x7c]
// 0x10bee80: mov x0, xzr
// 0x10bee84: str s0, [x19, #0xec]
// 0x10bee88: add x20, x19, #0xd0
// 0x10bee8c: bl #0x1b9ae30
// 0x10bee90: mov x0, xzr
// 0x10bee94: mov v9.16b, v0.16b
// 0x10bee98: fmul s12, s15, s12
// 0x10bee9c: bl #0x1b89b60
// 0x10beea0: mov v4.16b, v0.16b
// 0x10beea4: fsub s0, s12, s8
// 0x10beea8: fdiv s1, s0, s11
// 0x10beeac: frintm s1, s1
// 0x10beeb0: fmul s1, s1, s13
// 0x10beeb4: fadd s0, s0, s1
// 0x10beeb8: fmin s1, s0, s11
// 0x10beebc: fcmp s0, #0.0
// 0x10beec0: fmov s0, wzr
// 0x10beec4: fcsel s0, s1, s0, pl
// 0x10beec8: fadd s1, s0, s13
// 0x10beecc: fcmp s0, s14
// 0x10beed0: fcsel s0, s1, s0, gt
// 0x10beed4: fadd s1, s8, s0
// 0x10beed8: mov v0.16b, v8.16b
// 0x10beedc: mov x0, x20
// 0x10beee0: mov v2.16b, v9.16b
// 0x10beee4: mov v3.16b, v10.16b
// 0x10beee8: mov x1, xzr
// 0x10beeec: bl #0x1b8c860
// 0x10beef0: ldr x8, [x19, #0x38]
// 0x10beef4: str s0, [x19, #0xe0]
// 0x10beef8: cbz x8, #0x10bf640
// 0x10beefc: ldr s0, [x19, #0xf4]
// 0x10bef00: ldr s2, [x19, #0xec]
// 0x10bef04: ldr s1, [x8, #0x234]
// 0x10bef08: fadd s2, s0, s2
// 0x10bef0c: fneg s3, s1
// 0x10bef10: fcmp s2, s3
// 0x10bef14: b.pl #0x10bef28
// 0x10bef18: fsub s0, s3, s0
// 0x10bef1c: str s0, [x19, #0xec]
// 0x10bef20: str s3, [x19, #0xf4]
// 0x10bef24: b #0x10bef3c
// 0x10bef28: fcmp s2, s1
// 0x10bef2c: b.le #0x10bef48
// 0x10bef30: fsub s0, s1, s0
// 0x10bef34: str s0, [x19, #0xec]
// 0x10bef38: str s1, [x19, #0xf4]
// 0x10bef3c: mov x0, x19
// 0x10bef40: bl #0x10bf660
// 0x10bef44: b #0x10bef4c
// 0x10bef48: str s2, [x19, #0xf4]
// 0x10bef4c: ldr x8, [x19, #0x38]
// 0x10bef50: cbz x8, #0x10bf640
// 0x10bef54: ldr s0, [x19, #0xe8]
// 0x10bef58: ldr s1, [x19, #0xe0]
// 0x10bef5c: ldr s2, [x8, #0x22c]
// 0x10bef60: fadd s1, s0, s1
// 0x10bef64: fneg s2, s2
// 0x10bef68: fcmp s1, s2
// 0x10bef6c: b.mi #0x10bef7c
// 0x10bef70: ldr s2, [x8, #0x230]
// 0x10bef74: fcmp s1, s2
// 0x10bef78: b.le #0x10bef94
// 0x10bef7c: fsub s0, s2, s0
// 0x10bef80: mov x0, x19
// 0x10bef84: str s0, [x19, #0xe0]
// 0x10bef88: str s2, [x19, #0xe8]
// 0x10bef8c: bl #0x10bf720
// 0x10bef90: b #0x10bef98
// 0x10bef94: str s1, [x19, #0xe8]
// 0x10bef98: ldr x0, [x19, #0x80]
// 0x10bef9c: cbz x0, #0x10bf640
// 0x10befa0: ldr x20, [x19, #0x90]
// 0x10befa4: mov x1, xzr
// 0x10befa8: bl #0x1b9d508
// 0x10befac: ldr x0, [x19, #0x90]
// 0x10befb0: cbz x0, #0x10bf640
// 0x10befb4: mov x1, xzr
// 0x10befb8: mov v8.16b, v0.16b
// 0x10befbc: mov v9.16b, v1.16b
// 0x10befc0: mov v10.16b, v2.16b
// 0x10befc4: bl #0x1b9d940
// 0x10befc8: cbz x20, #0x10bf640
// 0x10befcc: ldr s6, [x19, #0xec]
// 0x10befd0: mov v3.16b, v0.16b
// 0x10befd4: mov v4.16b, v1.16b
// 0x10befd8: mov v5.16b, v2.16b
// 0x10befdc: mov x0, x20
// 0x10befe0: mov v0.16b, v8.16b
// 0x10befe4: mov v1.16b, v9.16b
// 0x10befe8: mov v2.16b, v10.16b
// 0x10befec: mov x1, xzr
// 0x10beff0: bl #0x1b9e490
// 0x10beff4: ldr x0, [x19, #0x80]
// 0x10beff8: cbz x0, #0x10bf640
// 0x10beffc: ldr x20, [x19, #0x88]
// 0x10bf000: mov x1, xzr
// 0x10bf004: bl #0x1b9d508
// 0x10bf008: ldr x0, [x19, #0x90]
// 0x10bf00c: cbz x0, #0x10bf640
// 0x10bf010: mov x1, xzr
// 0x10bf014: mov v8.16b, v0.16b
// 0x10bf018: mov v9.16b, v1.16b
// 0x10bf01c: mov v10.16b, v2.16b
// 0x10bf020: bl #0x1b9d8c8
// 0x10bf024: cbz x20, #0x10bf640
// 0x10bf028: mov v3.16b, v0.16b
// 0x10bf02c: mov v4.16b, v1.16b
// 0x10bf030: mov v5.16b, v2.16b
// 0x10bf034: ldr s6, [x19, #0xe0]
// 0x10bf038: mov x0, x20
// 0x10bf03c: mov v0.16b, v8.16b
// 0x10bf040: mov v1.16b, v9.16b
// 0x10bf044: mov v2.16b, v10.16b
// 0x10bf048: ldp x20, x19, [sp, #0x80]
// 0x10bf04c: ldp x22, x21, [sp, #0x70]
// 0x10bf050: ldp x24, x23, [sp, #0x60]
// 0x10bf054: ldr x30, [sp, #0x50]
// 0x10bf058: ldp d9, d8, [sp, #0x40]
// 0x10bf05c: ldp d11, d10, [sp, #0x30]
// 0x10bf060: ldp d13, d12, [sp, #0x20]
// 0x10bf064: ldp d15, d14, [sp, #0x10]
// 0x10bf068: mov x1, xzr
// 0x10bf06c: add sp, sp, #0x90
// 0x10bf070: b #0x1b9e490
// 0x10bf074: ldrb w9, [x19, #0xf8]
// 0x10bf078: cbz w9, #0x10bf09c
// 0x10bf07c: mov w9, #1
// 0x10bf080: strb w9, [x8, #0xa8]
// 0x10bf084: ldr x8, [x19, #0x20]
// 0x10bf088: cbz x8, #0x10bf640
// 0x10bf08c: ldr s0, [x19, #0x100]
// 0x10bf090: strb w9, [x8, #0xf0]
// 0x10bf094: str s0, [x8, #0xd4]
// 0x10bf098: strb wzr, [x19, #0xf8]
// 0x10bf09c: adrp x8, #0x1e8c000
// 0x10bf0a0: ldr x8, [x8, #0x458]
// 0x10bf0a4: ldr x0, [x8]
// 0x10bf0a8: ldr w8, [x0, #0xe0]
// 0x10bf0ac: cbnz w8, #0x10bf0b4
// 0x10bf0b0: bl #0xf7da5c
// 0x10bf0b4: mov w0, #1
// 0x10bf0b8: mov x1, xzr
// 0x10bf0bc: bl #0x10384e4
// 0x10bf0c0: mov w0, wzr
// 0x10bf0c4: mov x1, xzr
// 0x10bf0c8: bl #0x103881c
// 0x10bf0cc: ldr x8, [x19, #0x48]
// 0x10bf0d0: cbz x8, #0x10bf640
// 0x10bf0d4: ldr s0, [x8, #0xe4]
// 0x10bf0d8: ldp s2, s1, [x19, #0x70]
// 0x10bf0dc: fmul s0, s0, s1
// 0x10bf0e0: str s0, [x19, #0xec]
// 0x10bf0e4: ldr s0, [x8, #0xe8]
// 0x10bf0e8: fneg s0, s0
// 0x10bf0ec: fmul s0, s2, s0
// 0x10bf0f0: b #0x10beef0
// 0x10bf0f4: ldr x8, [x19, #0x20]
// 0x10bf0f8: cbz x8, #0x10bf640
// 0x10bf0fc: str wzr, [x8, #0xd4]
// 0x10bf100: ldr x8, [x19, #0x48]
// 0x10bf104: cbz x8, #0x10bf640
// 0x10bf108: ldr s8, [x19, #0x10c]
// 0x10bf10c: ldr s10, [x8, #0xe4]
// 0x10bf110: mov x0, xzr
// 0x10bf114: add x20, x19, #0x104
// 0x10bf118: bl #0x1b9ae30
// 0x10bf11c: mov x0, xzr
// 0x10bf120: mov v9.16b, v0.16b
// 0x10bf124: bl #0x1b89b60
// 0x10bf128: mov w8, #0x43b40000
// 0x10bf12c: mov v4.16b, v0.16b
// 0x10bf130: fsub s0, s10, s8
// 0x10bf134: fmov s1, w8
// 0x10bf138: mov w8, #-0x3c4c0000
// 0x10bf13c: fdiv s2, s0, s1
// 0x10bf140: fmov s3, w8
// 0x10bf144: frintm s2, s2
// 0x10bf148: fmul s2, s2, s3
// 0x10bf14c: fadd s0, s0, s2
// 0x10bf150: fmov s10, wzr
// 0x10bf154: mov w8, #0x43340000
// 0x10bf158: fmin s1, s0, s1
// 0x10bf15c: fcmp s0, #0.0
// 0x10bf160: fmov s0, w8
// 0x10bf164: fcsel s1, s1, s10, pl
// 0x10bf168: fadd s2, s1, s3
// 0x10bf16c: fcmp s1, s0
// 0x10bf170: fcsel s0, s2, s1, gt
// 0x10bf174: mov w8, #0x7f800000
// 0x10bf178: fadd s1, s8, s0
// 0x10bf17c: fmov s3, w8
// 0x10bf180: mov v0.16b, v8.16b
// 0x10bf184: mov x0, x20
// 0x10bf188: mov v2.16b, v9.16b
// 0x10bf18c: mov x1, xzr
// 0x10bf190: bl #0x1b8c860
// 0x10bf194: ldr x8, [x19, #0x48]
// 0x10bf198: str s0, [x19, #0x10c]
// 0x10bf19c: cbz x8, #0x10bf640
// 0x10bf1a0: ldr s8, [x19, #0x110]
// 0x10bf1a4: ldr s11, [x8, #0xe8]
// 0x10bf1a8: mov x0, xzr
// 0x10bf1ac: add x20, x19, #0x108
// 0x10bf1b0: bl #0x1b9ae30
// 0x10bf1b4: mov x0, xzr
// 0x10bf1b8: mov v9.16b, v0.16b
// 0x10bf1bc: fneg s11, s11
// 0x10bf1c0: bl #0x1b89b60
// 0x10bf1c4: mov w8, #0x43b40000
// 0x10bf1c8: mov v4.16b, v0.16b
// 0x10bf1cc: fmov s0, w8
// 0x10bf1d0: fsub s1, s11, s8
// 0x10bf1d4: mov w8, #-0x3c4c0000
// 0x10bf1d8: fdiv s3, s1, s0
// 0x10bf1dc: fmov s2, w8
// 0x10bf1e0: frintm s3, s3
// 0x10bf1e4: fmul s3, s3, s2
// 0x10bf1e8: fadd s1, s1, s3
// 0x10bf1ec: mov w8, #0x43340000
// 0x10bf1f0: fmin s0, s1, s0
// 0x10bf1f4: fcmp s1, #0.0
// 0x10bf1f8: fmov s3, w8
// 0x10bf1fc: fcsel s0, s0, s10, pl
// 0x10bf200: fadd s1, s0, s2
// 0x10bf204: fcmp s0, s3
// 0x10bf208: fcsel s0, s1, s0, gt
// 0x10bf20c: mov w8, #0x7f800000
// 0x10bf210: fadd s1, s8, s0
// 0x10bf214: fmov s3, w8
// 0x10bf218: mov v0.16b, v8.16b
// 0x10bf21c: mov x0, x20
// 0x10bf220: mov v2.16b, v9.16b
// 0x10bf224: mov x1, xzr
// 0x10bf228: bl #0x1b8c860
// 0x10bf22c: ldr x8, [x19, #0x48]
// 0x10bf230: str s0, [x19, #0x110]
// 0x10bf234: cbz x8, #0x10bf640
// 0x10bf238: ldr s0, [x8, #0xe4]
// 0x10bf23c: ldr s1, [x19, #0xa0]
// 0x10bf240: ldp s2, s3, [x19, #0x78]
// 0x10bf244: ldr s8, [x19, #0xec]
// 0x10bf248: mov w8, #0x43b40000
// 0x10bf24c: fmov s11, w8
// 0x10bf250: fmul s0, s0, s2
// 0x10bf254: fmul s1, s1, s3
// 0x10bf258: fadd s0, s0, s1
// 0x10bf25c: fsub s0, s0, s8
// 0x10bf260: mov w8, #-0x3c4c0000
// 0x10bf264: fdiv s1, s0, s11
// 0x10bf268: fmov s12, w8
// 0x10bf26c: frintm s1, s1
// 0x10bf270: fmul s1, s1, s12
// 0x10bf274: fadd s0, s0, s1
// 0x10bf278: fmov s10, wzr
// 0x10bf27c: mov w8, #0x43340000
// 0x10bf280: fmin s1, s0, s11
// 0x10bf284: fcmp s0, #0.0
// 0x10bf288: fmov s13, w8
// 0x10bf28c: fcsel s0, s1, s10, pl
// 0x10bf290: fadd s1, s0, s12
// 0x10bf294: fcmp s0, s13
// 0x10bf298: mov x0, xzr
// 0x10bf29c: fcsel s14, s1, s0, gt
// 0x10bf2a0: add x20, x19, #0xc8
// 0x10bf2a4: bl #0x1b9ae30
// 0x10bf2a8: mov x0, xzr
// 0x10bf2ac: mov v9.16b, v0.16b
// 0x10bf2b0: bl #0x1b89b60
// 0x10bf2b4: mov v4.16b, v0.16b
// 0x10bf2b8: fsub s0, s14, s8
// 0x10bf2bc: fdiv s1, s0, s11
// 0x10bf2c0: frintm s1, s1
// 0x10bf2c4: fmul s1, s1, s12
// 0x10bf2c8: fadd s0, s0, s1
// 0x10bf2cc: fmin s1, s0, s11
// 0x10bf2d0: fcmp s0, #0.0
// 0x10bf2d4: fcsel s0, s1, s10, pl
// 0x10bf2d8: fadd s1, s0, s12
// 0x10bf2dc: fcmp s0, s13
// 0x10bf2e0: fcsel s0, s1, s0, gt
// 0x10bf2e4: mov w8, #0x7f800000
// 0x10bf2e8: fadd s1, s8, s0
// 0x10bf2ec: fmov s3, w8
// 0x10bf2f0: mov v0.16b, v8.16b
// 0x10bf2f4: mov x0, x20
// 0x10bf2f8: mov v2.16b, v9.16b
// 0x10bf2fc: mov x1, xzr
// 0x10bf300: bl #0x1b8c860
// 0x10bf304: ldr x8, [x19, #0x48]
// 0x10bf308: str s0, [x19, #0xec]
// 0x10bf30c: cbz x8, #0x10bf640
// 0x10bf310: ldr s0, [x8, #0xe8]
// 0x10bf314: ldr s1, [x19, #0x9c]
// 0x10bf318: ldp s2, s3, [x19, #0x78]
// 0x10bf31c: ldr s8, [x19, #0xe0]
// 0x10bf320: mov w8, #0x43b40000
// 0x10bf324: fmov s11, w8
// 0x10bf328: fmul s1, s1, s3
// 0x10bf32c: fmul s0, s0, s2
// 0x10bf330: fsub s0, s1, s0
// 0x10bf334: fsub s0, s0, s8
// 0x10bf338: mov w8, #-0x3c4c0000
// 0x10bf33c: fdiv s1, s0, s11
// 0x10bf340: fmov s12, w8
// 0x10bf344: frintm s1, s1
// 0x10bf348: fmul s1, s1, s12
// 0x10bf34c: fadd s0, s0, s1
// 0x10bf350: mov w8, #0x43340000
// 0x10bf354: fmin s1, s0, s11
// 0x10bf358: fcmp s0, #0.0
// 0x10bf35c: fmov s13, w8
// 0x10bf360: fcsel s0, s1, s10, pl
// 0x10bf364: fadd s1, s0, s12
// 0x10bf368: fcmp s0, s13
// 0x10bf36c: mov x0, xzr
// 0x10bf370: fcsel s14, s1, s0, gt
// 0x10bf374: add x20, x19, #0xd0
// 0x10bf378: bl #0x1b9ae30
// 0x10bf37c: mov x0, xzr
// 0x10bf380: mov v9.16b, v0.16b
// 0x10bf384: bl #0x1b89b60
// 0x10bf388: mov v4.16b, v0.16b
// 0x10bf38c: fsub s0, s14, s8
// 0x10bf390: fdiv s1, s0, s11
// 0x10bf394: frintm s1, s1
// 0x10bf398: fmul s1, s1, s12
// 0x10bf39c: fadd s0, s0, s1
// 0x10bf3a0: fmin s1, s0, s11
// 0x10bf3a4: fcmp s0, #0.0
// 0x10bf3a8: fcsel s0, s1, s10, pl
// 0x10bf3ac: fadd s1, s0, s12
// 0x10bf3b0: fcmp s0, s13
// 0x10bf3b4: fcsel s0, s1, s0, gt
// 0x10bf3b8: mov w8, #0x7f800000
// 0x10bf3bc: fadd s1, s8, s0
// 0x10bf3c0: fmov s3, w8
// 0x10bf3c4: mov v0.16b, v8.16b
// 0x10bf3c8: mov x0, x20
// 0x10bf3cc: mov v2.16b, v9.16b
// 0x10bf3d0: b #0x10beee8
// 0x10bf3d4: ldr x9, [x19, #0x48]
// 0x10bf3d8: cbz x9, #0x10bf640
// 0x10bf3dc: ldrb w9, [x9, #0x9c]
// 0x10bf3e0: cbz w9, #0x10bed7c
// 0x10bf3e4: ldrb w9, [x19, #0x69]
// 0x10bf3e8: cbz w9, #0x10bf644
// 0x10bf3ec: ldrb w9, [x19, #0x6c]
// 0x10bf3f0: cbz w9, #0x10bf428
// 0x10bf3f4: mov w9, #1
// 0x10bf3f8: strb w9, [x19, #0x6a]
// 0x10bf3fc: ldr x0, [x8, #0x178]
// 0x10bf400: str wzr, [x8, #0x33c]
// 0x10bf404: cbz x0, #0x10bf640
// 0x10bf408: ldr x9, [x0]
// 0x10bf40c: ldr s2, [x8, #0x338]
// 0x10bf410: ldr s1, [x8, #0x334]
// 0x10bf414: ldr s0, [x8, #0x330]
// 0x10bf418: ldr x8, [x9, #0x2a8]
// 0x10bf41c: ldr x1, [x9, #0x2b0]
// 0x10bf420: fmov s3, wzr
// 0x10bf424: blr x8
// 0x10bf428: strb wzr, [x19, #0x69]
// 0x10bf42c: b #0x10bed7c
// 0x10bf430: cbz x8, #0x10bf640
// 0x10bf434: ldrb w8, [x8, #0x2b1]
// 0x10bf438: cbnz w8, #0x10bf484
// 0x10bf43c: ldr x8, [x20]
// 0x10bf440: cbz x8, #0x10bf640
// 0x10bf444: ldr s8, [x8, #0x3a8]
// 0x10bf448: ldr s9, [x8, #0x3dc]
// 0x10bf44c: mov x0, xzr
// 0x10bf450: bl #0x1b9ad30
// 0x10bf454: adrp x8, #0x832000
// 0x10bf458: ldr s1, [x8, #0x3b8]
// 0x10bf45c: fadd s2, s8, s9
// 0x10bf460: fadd s1, s2, s1
// 0x10bf464: fcmp s1, s0
// 0x10bf468: b.pl #0x10bf484
// 0x10bf46c: ldrb w8, [x19, #0xf9]
// 0x10bf470: cbz w8, #0x10bf484
// 0x10bf474: mov w8, #1
// 0x10bf478: strb w8, [x19, #0x69]
// 0x10bf47c: strb wzr, [x19, #0xf9]
// 0x10bf480: b #0x10bf48c
// 0x10bf484: ldrb w8, [x19, #0x69]
// 0x10bf488: cbz w8, #0x10bf4b4
// 0x10bf48c: ldr x8, [x19, #0x30]
// 0x10bf490: cbz x8, #0x10bf640
// 0x10bf494: ldrb w9, [x8, #0x2e8]
// 0x10bf498: cbz w9, #0x10bf4bc
// 0x10bf49c: ldrb w9, [x8, #0x2dc]
// 0x10bf4a0: cbz w9, #0x10bf4bc
// 0x10bf4a4: mov w9, #1
// 0x10bf4a8: strb wzr, [x19, #0x69]
// 0x10bf4ac: strb w9, [x19, #0xfa]
// 0x10bf4b0: b #0x10bf4bc
// 0x10bf4b4: ldr x8, [x19, #0x30]
// 0x10bf4b8: cbz x8, #0x10bf640
// 0x10bf4bc: ldrb w9, [x8, #0x2e8]
// 0x10bf4c0: cbz w9, #0x10bf4d0
// 0x10bf4c4: ldrb w8, [x8, #0x2dc]
// 0x10bf4c8: cbnz w8, #0x10bf520
// 0x10bf4cc: b #0x10bf508
// 0x10bf4d0: ldrb w9, [x8, #0x2dc]
// 0x10bf4d4: cbz w9, #0x10bf4c4
// 0x10bf4d8: ldr x8, [x20]
// 0x10bf4dc: cbz x8, #0x10bf640
// 0x10bf4e0: ldr s8, [x8, #0x3a8]
// 0x10bf4e4: ldr s9, [x8, #0x3dc]
// 0x10bf4e8: mov x0, xzr
// 0x10bf4ec: bl #0x1b9ad30
// 0x10bf4f0: adrp x8, #0x832000
// 0x10bf4f4: ldr s1, [x8, #0x3b8]
// 0x10bf4f8: fadd s2, s8, s9
// 0x10bf4fc: fadd s1, s2, s1
// 0x10bf500: fcmp s1, s0
// 0x10bf504: b.pl #0x10bf638
// 0x10bf508: ldrb w8, [x19, #0xfa]
// 0x10bf50c: cbz w8, #0x10bf520
// 0x10bf510: mov w8, #1
// 0x10bf514: strb w8, [x19, #0x69]
// 0x10bf518: strb wzr, [x19, #0xfa]
// 0x10bf51c: b #0x10bf528
// 0x10bf520: ldrb w8, [x19, #0x69]
// 0x10bf524: cbz w8, #0x10bf54c
// 0x10bf528: ldr x9, [x19, #0x30]
// 0x10bf52c: cbz x9, #0x10bf640
// 0x10bf530: ldrb w10, [x9, #0x295]
// 0x10bf534: cbz w10, #0x10bf558
// 0x10bf538: mov w10, #1
// 0x10bf53c: mov w8, wzr
// 0x10bf540: strb wzr, [x19, #0x69]
// 0x10bf544: strb w10, [x19, #0xfb]
// 0x10bf548: b #0x10bf558
// 0x10bf54c: ldr x9, [x19, #0x30]
// 0x10bf550: cbz x9, #0x10bf640
// 0x10bf554: mov w8, wzr
// 0x10bf558: ldrb w9, [x9, #0x295]
// 0x10bf55c: cbnz w9, #0x10bf574
// 0x10bf560: ldrb w9, [x19, #0xfb]
// 0x10bf564: cbz w9, #0x10bf574
// 0x10bf568: mov w8, #1
// 0x10bf56c: strb w8, [x19, #0x69]
// 0x10bf570: strb wzr, [x19, #0xfb]
// 0x10bf574: ldrb w9, [x19, #0x6a]
// 0x10bf578: cbz w9, #0x10bf5e8
// 0x10bf57c: ldr x8, [x19, #0x28]
// 0x10bf580: cbz x8, #0x10bf640
// 0x10bf584: ldrb w9, [x8, #0x2d0]
// 0x10bf588: cbz w9, #0x10bf5c0
// 0x10bf58c: ldr x9, [x20]
// 0x10bf590: cbz x9, #0x10bf640
// 0x10bf594: ldrb w10, [x9, #0x239]
// 0x10bf598: cbnz w10, #0x10bf5c0
// 0x10bf59c: ldr s0, [x9, #0x24c]
// 0x10bf5a0: ldr s1, [x19, #0x114]
// 0x10bf5a4: fcmp s0, s1
// 0x10bf5a8: b.le #0x10bf5c0
// 0x10bf5ac: ldr x9, [x19, #0x58]
// 0x10bf5b0: mov w10, #1
// 0x10bf5b4: strb w10, [x19, #0x69]
// 0x10bf5b8: cbnz x9, #0x10bf5d0
// 0x10bf5bc: b #0x10bf640
// 0x10bf5c0: ldr x9, [x19, #0x58]
// 0x10bf5c4: strb wzr, [x19, #0x69]
// 0x10bf5c8: cbz x9, #0x10bf640
// 0x10bf5cc: mov w10, wzr
// 0x10bf5d0: strb w10, [x9, #0x10c]
// 0x10bf5d4: strb w10, [x8, #0x2e8]
// 0x10bf5d8: mov w8, #1
// 0x10bf5dc: strb w8, [x19, #0xfd]
// 0x10bf5e0: strb w8, [x19, #0x6c]
// 0x10bf5e4: b #0x10be8cc
// 0x10bf5e8: ldr x9, [x19, #0x58]
// 0x10bf5ec: cbz x9, #0x10bf640
// 0x10bf5f0: strb wzr, [x9, #0x10c]
// 0x10bf5f4: ldr x9, [x19, #0x28]
// 0x10bf5f8: cbz x9, #0x10bf640
// 0x10bf5fc: ldrb w10, [x9, #0x2d0]
// 0x10bf600: strb wzr, [x9, #0x2e8]
// 0x10bf604: cbz w8, #0x10bf61c
// 0x10bf608: cbz w10, #0x10bf620
// 0x10bf60c: mov w8, #1
// 0x10bf610: strb wzr, [x19, #0x69]
// 0x10bf614: strb w8, [x19, #0xfc]
// 0x10bf618: b #0x10be8cc
// 0x10bf61c: cbnz w10, #0x10be8cc
// 0x10bf620: ldrb w8, [x19, #0xfc]
// 0x10bf624: cbz w8, #0x10be8cc
// 0x10bf628: ldrb w8, [x19, #0xfd]
// 0x10bf62c: cbz w8, #0x10bf650
// 0x10bf630: strh wzr, [x19, #0xfc]
// 0x10bf634: b #0x10be8cc
// 0x10bf638: ldr x8, [x19, #0x30]
// 0x10bf63c: cbnz x8, #0x10bf4c4
// 0x10bf640: bl #0xf7db74
// 0x10bf644: mov w8, #1
// 0x10bf648: sturh w8, [x19, #0x69]
// 0x10bf64c: b #0x10bed7c
// 0x10bf650: mov w8, #1
// 0x10bf654: strb w8, [x19, #0x69]
// 0x10bf658: strb wzr, [x19, #0xfc]
// 0x10bf65c: b #0x10be8cc
```


## `WeaponPivot.HorizontalLook` — RVA `0xcbf660`

- Decompiled symbol: `WeaponPivot_HorizontalLook`
- Metadata signature: `private void HorizontalLook() { }`
- Native interval: `192` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: Decompiler produced no C-like text

```c
// 0x10bf660: str d10, [sp, #-0x30]!
// 0x10bf664: stp d9, d8, [sp, #8]
// 0x10bf668: str x30, [sp, #0x18]
// 0x10bf66c: stp x20, x19, [sp, #0x20]
// 0x10bf670: ldr x20, [x0, #0x40]
// 0x10bf674: cbz x20, #0x10bf71c
// 0x10bf678: ldr s8, [x20, #0x50]
// 0x10bf67c: mov x19, x0
// 0x10bf680: str s8, [x20, #0x7c]
// 0x10bf684: ldr x8, [x0, #0x48]
// 0x10bf688: cbz x8, #0x10bf71c
// 0x10bf68c: ldr s9, [x8, #0xe4]
// 0x10bf690: ldr s10, [x20, #0x3c]
// 0x10bf694: mov x0, xzr
// 0x10bf698: bl #0x1b9ae58
// 0x10bf69c: fmul s1, s9, s10
// 0x10bf6a0: fmul s0, s1, s0
// 0x10bf6a4: fadd s0, s8, s0
// 0x10bf6a8: str s0, [x20, #0x50]
// 0x10bf6ac: ldr x8, [x19, #0x40]
// 0x10bf6b0: cbz x8, #0x10bf71c
// 0x10bf6b4: ldr s0, [x8, #0x7c]
// 0x10bf6b8: ldr s1, [x8, #0x50]
// 0x10bf6bc: mov w9, #0x43b40000
// 0x10bf6c0: fmov s2, w9
// 0x10bf6c4: mov w10, #-0x3c4c0000
// 0x10bf6c8: fsub s0, s1, s0
// 0x10bf6cc: fdiv s1, s0, s2
// 0x10bf6d0: fmov s3, w10
// 0x10bf6d4: frintm s1, s1
// 0x10bf6d8: fmul s1, s1, s3
// 0x10bf6dc: fadd s0, s0, s1
// 0x10bf6e0: fmov s1, wzr
// 0x10bf6e4: mov w9, #0x43340000
// 0x10bf6e8: fmin s2, s0, s2
// 0x10bf6ec: fcmp s0, #0.0
// 0x10bf6f0: fmov s0, w9
// 0x10bf6f4: fcsel s1, s2, s1, pl
// 0x10bf6f8: ldp x20, x19, [sp, #0x20]
// 0x10bf6fc: ldr x30, [sp, #0x18]
// 0x10bf700: ldp d9, d8, [sp, #8]
// 0x10bf704: fadd s2, s1, s3
// 0x10bf708: fcmp s1, s0
// 0x10bf70c: fcsel s0, s2, s1, gt
// 0x10bf710: str s0, [x8, #0x7c]
// 0x10bf714: ldr d10, [sp], #0x30
// 0x10bf718: ret
// 0x10bf71c: bl #0xf7db74
```


## `WeaponPivot.VerticalLook` — RVA `0xcbf720`

- Decompiled symbol: `WeaponPivot_VerticalLook`
- Metadata signature: `private void VerticalLook() { }`
- Native interval: `84` bytes
- Result: `pseudocode`
- Heuristic layout hint: `WeaponPivot_Recovered` matched 2 offsets against `WeaponPivot` metadata (confidence 1.00).

```c
typedef struct WeaponPivot_Recovered {
    char padding_0[64];
    struct struct_2 *SmoothMouseLookComponent;
    struct struct_0 *InputComponent;
} WeaponPivot_Recovered;

typedef struct struct_0 {
    char padding_0[232];
    unsigned int field_e8;
} struct_0;

typedef struct struct_2 {
    char padding_0[60];
    unsigned int field_3c;
    char padding_40[20];
    unsigned int field_54;
} struct_2;

int WeaponPivot_VerticalLook(struct_1 *ptr)
{
    unsigned int p[22];  // x19
    unsigned int v1;  // w0
    unsigned int v2;  // s0

    p = ptr->field_40;
    if (p && ptr->field_48)
    {
        v1 = Time__get_timeScale(0);
        p[21] = p[21] + ptr->field_48->field_e8 * p[15] * v2;
        return v1;
    }
    sub_f7db74();
}
```


## `WeaponPivot.PlayJumpAnim` — RVA `0xcbf774`

- Decompiled symbol: `WeaponPivot_PlayJumpAnim`
- Metadata signature: `public void PlayJumpAnim() { }`
- Native interval: `112` bytes
- Result: `pseudocode`
- Heuristic layout hint: `WeaponPivot_Recovered` matched 2 offsets against `WeaponPivot` metadata (confidence 1.00).

```c
typedef struct WeaponPivot_Recovered {
    char padding_0[48];
    struct struct_0 *FPSWalkerComponent;
    char padding_38[160];
    unsigned long long PivotAnimatorComponent;
} WeaponPivot_Recovered;

typedef struct struct_0 {
    char padding_0[418];
    char field_1a2;
} struct_0;

extern char g_1fab4f6;

void WeaponPivot_PlayJumpAnim(struct_1 *a0)
{
    if (!(g_1fab4f6 & 1))
    {
        sub_f7d92c("c&");
        g_1fab4f6 = 1;
    }
    if (a0->field_30)
    {
        if (!a0->field_30->field_1a2)
        {
            return;
        }
        else if (a0->field_d8)
        {
            Animator__SetTrigger();
            return;
        }
    }
    sub_f7db74();
}
```


## `WeaponPivot.PlayLandAnim` — RVA `0xcbf7e4`

- Decompiled symbol: `WeaponPivot_PlayLandAnim`
- Metadata signature: `public void PlayLandAnim() { }`
- Native interval: `112` bytes
- Result: `pseudocode`
- Heuristic layout hint: `WeaponPivot_Recovered` matched 2 offsets against `WeaponPivot` metadata (confidence 1.00).

```c
typedef struct WeaponPivot_Recovered {
    char padding_0[48];
    struct struct_0 *FPSWalkerComponent;
    char padding_38[160];
    unsigned long long PivotAnimatorComponent;
} WeaponPivot_Recovered;

typedef struct struct_0 {
    char padding_0[418];
    char field_1a2;
} struct_0;

extern char g_1fab4f7;

void WeaponPivot_PlayLandAnim(struct_1 *a0)
{
    if (!(g_1fab4f7 & 1))
    {
        sub_f7d92c("e&");
        g_1fab4f7 = 1;
    }
    if (a0->field_30)
    {
        if (!a0->field_30->field_1a2)
        {
            return;
        }
        else if (a0->field_d8)
        {
            Animator__SetTrigger();
            return;
        }
    }
    sub_f7db74();
}
```


## `WeaponPivot.ToggleDeadzoneZooming` — RVA `0xcbf854`

- Decompiled symbol: `WeaponPivot_ToggleDeadzoneZooming`
- Metadata signature: `public void ToggleDeadzoneZooming() { }`
- Native interval: `108` bytes
- Result: `pseudocode`
- Heuristic layout hint: `WeaponPivot_Recovered` matched 3 offsets against `WeaponPivot` metadata (confidence 1.00).

```c
typedef struct WeaponPivot_Recovered {
    char padding_0[40];
    struct struct_2 *FPSPlayerComponent;
    char padding_30[58];
    char deadzoneZooming;
    char padding_6b[1];
    char wasDeadzoneZooming;
} WeaponPivot_Recovered;

typedef struct struct_2 {
    char padding_0[376];
    struct struct_3 *field_178;
    char padding_180[444];
    unsigned int field_33c;
} struct_2;

typedef struct struct_0 {
    char padding_0[680];
    struct struct_1 *field_2a8;
    unsigned long long field_2b0;
} struct_0;

typedef struct struct_3 {
    struct struct_0 *field_0;
} struct_3;

typedef struct struct_1 {
    unsigned long long field_0;
} struct_1;

void WeaponPivot_ToggleDeadzoneZooming(struct_4 *ptr)
{
    struct_2 *p;  // x8
    struct_0 **v1;  // x0
    unsigned long long v2;  // x1

    if (ptr->field_6a)
    {
        ptr->field_6c = 0;
        ptr->field_6a = 0;
        return;
    }
    p = ptr->field_28;
    ptr->field_6c = 1;
    ptr->field_6a = 1;
    if (p)
    {
        v1 = p->field_178;
        p->field_33c = 0;
        if (v1)
        {
            v2 = *(v1)->field_2b0;
            *(v1)->field_2a8();
        }
    }
    sub_f7db74();
}
```


## `WeaponPivot.ToggleSwayLeadingMode` — RVA `0xcbf8c0`

- Decompiled symbol: `WeaponPivot_ToggleSwayLeadingMode`
- Metadata signature: `public void ToggleSwayLeadingMode() { }`
- Native interval: `16` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[107];
    char field_6b;
} struct_0;

struct_0 * WeaponPivot_ToggleSwayLeadingMode(struct_0 *ptr)
{
    ptr->field_6b = ptr->field_6b ^ 1;
    return ptr;
}
```


## `WeaponPivot.ClampAngle` — RVA `0xcbf8d0`

- Decompiled symbol: `WeaponPivot_ClampAngle`
- Metadata signature: `public static float ClampAngle(float angle, float min, float max) { }`
- Native interval: `136` bytes
- Result: `pseudocode`

```c
void WeaponPivot_ClampAngle(void)
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


## `WeaponPivot.ctor` — RVA `0xcbf958`

- Decompiled symbol: `WeaponPivot_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `44` bytes
- Result: `pseudocode`
- Heuristic layout hint: `WeaponPivot_Recovered` matched 4 offsets against `WeaponPivot` metadata (confidence 1.00).

```c
typedef struct WeaponPivot_Recovered {
    char padding_0[109];
    char swayLeadingFollowCrosshair;
    char padding_6e[2];
    uint128_t verticalSpeed;
    char padding_80[64];
    unsigned int animSpeed;
    char padding_c4[80];
    unsigned int maxFreeAimFOV;
} WeaponPivot_Recovered;

long long WeaponPivot_ctor(struct_0 *ptr)
{
    ptr->field_6d = 1;
    ptr->field_c0 = 0x3f800000;
    ptr->field_70 = 0x3e4ccccd3f8000003f8000003f800000;
    ptr->field_114 = 0x41700000;
}
```
