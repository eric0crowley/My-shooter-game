# Native pseudocode: maxCamera

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `maxCamera.Start` — RVA `0xc6abd4`

- Decompiled symbol: `maxCamera_Start`
- Metadata signature: `private void Start() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long maxCamera_Start(unsigned long a0)
{
    unsigned long long v0;  // x0

    v0 = maxCamera__Init();
    return maxCamera__Init();
}
```

## `maxCamera.Init` — RVA `0xc6abd8`

- Decompiled symbol: `maxCamera_Init`
- Metadata signature: `public void Init() { }`
- Native interval: `1244` bytes
- Result: `pseudocode`
- Heuristic layout hint: `maxCamera_Recovered` matched 10 offsets against `maxCamera` metadata (confidence 0.77).

```c
typedef struct struct_3 {
    char padding_0[224];
    unsigned int field_e0;
} struct_3;

typedef struct maxCamera_Recovered {
    char padding_0[32];
    long long target;
    char padding_28[12];
    unsigned int distance;
    char padding_38[36];
    unsigned int xDeg;
    unsigned int yDeg;
    unsigned int currentDistance;
    unsigned int desiredDistance;
    unsigned int currentRotation;
    char padding_70[8];
    unsigned int field_78;
    unsigned int desiredRotation;
    char padding_80[8];
    unsigned int field_88;
    unsigned int rotation;
    char padding_90[8];
    unsigned int field_98;
    unsigned int position;
} maxCamera_Recovered;

typedef struct struct_2 {
    char padding_0[224];
    unsigned int field_e0;
} struct_2;

typedef struct struct_5 {
    char padding_0[24];
    unsigned int field_18;
    unsigned int field_1c;
    unsigned int field_20;
    char padding_24[24];
    unsigned int field_3c;
    unsigned int field_40;
    unsigned int field_44;
} struct_5;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

typedef struct struct_4 {
    char padding_0[184];
    struct struct_5 *field_b8;
} struct_4;

extern long long g_1eefaf0;
extern struct_0 *g_1ef0c58;
extern struct_4 *g_1ef22e8;
extern long long g_1f08dc0;
extern char g_1fab32c;
extern char g_1fab32f;
extern char g_1fab3e0;
extern char g_1fab3e1;
extern char g_1fab3e2;

struct_3 * maxCamera_Init(struct_1 *ptr)
{
    struct_1 *ptr3;  // x20
    long long v2;  // x21
    unsigned int v11;  // s2
    unsigned int v12;  // s0
    unsigned int p[18];  // x8
    unsigned int v14;  // s13
    unsigned int v15;  // s14
    unsigned int v16;  // s12
    unsigned int v17;  // s0
    unsigned int v18;  // s1
    unsigned long v19;  // 4157
    unsigned int v20;  // s2
    long long v3;  // x22
    struct_2 *v21;  // x0
    unsigned int v22;  // s0
    unsigned int v23;  // s2
    unsigned int v24;  // s1
    unsigned long v25;  // 4221
    unsigned int v26;  // s8
    unsigned int addr[18];  // x8
    unsigned int v28;  // s13
    unsigned int v29;  // s14
    unsigned int v30;  // s12
    unsigned int v4;  // s3
    struct_2 *v31;  // x0
    unsigned int v32;  // s0
    unsigned int v33;  // s1
    unsigned long v34;  // 4153
    struct_2 *v35;  // x0
    unsigned int v36;  // s0
    unsigned int v37;  // s1
    unsigned long v38;  // 4221
    unsigned int v39;  // s8
    unsigned int v5;  // s2
    unsigned int v6;  // s2
    unsigned int v7;  // s1
    unsigned int v8;  // s1
    long long v9;  // x0
    unsigned int v10;  // s1
    unsigned int v0;  // [bp-0x74]

    if (!(g_1fab32f & 1))
    {
        sub_f7d92c(&g_1eefaf0);
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c(&g_1f08dc0);
        g_1fab32f = 1;
    }
    ptr3 = &ptr->field_20;
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (!((char)Object__op_Implicit(ptr->field_20, 0) & 1))
    {
        v2 = sub_f7db70(g_1eefaf0);
        GameObject__ctor(v2, g_1f08dc0, 0);
        if (!v2 || !((v3 = (long long)(unsigned long long)GameObject__get_transform(v2, 0), Component__get_transform(ptr, 0) && (Transform__get_position(), Component__get_transform(ptr, 0) && (Transform__get_forward(), v3)))))
            goto LABEL_106b0b0;
        v4 = ptr->field_34;
        v6 = v5 + v5 * v4;
        v8 = v7 + v7 * v4;
        Transform__set_position(v3, 0);
        v9 = GameObject__get_transform(v2, 0);
        *((long long *)&ptr3->padding_0[0]) = v9;
        sub_f7d8d0(ptr3, v9);
    }
    if (Component__get_transform(ptr, 0))
    {
        Transform__get_position();
        if (*((long long *)&ptr3->padding_0[0]))
        {
            Transform__get_position(*((long long *)&ptr3->padding_0[0]), 0);
            if (!g_1fab3e0)
            {
                sub_f7d92c("_F");
                g_1fab3e0 = 1;
            }
            if (!g_1ef07e8->field_e0)
                sub_f7da5c(g_1ef07e8);
            v10 = (v8 - v8) * (v8 - v8);
            v11 = (v6 - v6) * (v6 - v6);
            v12 = [D] unsupported_Iop_SqrtF32();
            ptr->field_34 = v12;
            ptr->field_64 = v12;
            ptr->field_68 = v12;
            if (Component__get_transform(ptr, 0))
            {
                Transform__get_position();
                ptr->field_9c = v12;
                *((unsigned int *)&ptr[1].padding_0[0]) = v10;
                *((unsigned int *)&ptr[1].padding_0[4]) = v11;
                if (Component__get_transform(ptr, 0))
                {
                    Transform__get_rotation();
                    ptr->field_8c = v12;
                    *((unsigned int *)&ptr->padding_90[0]) = v10;
                    *((unsigned int *)&ptr->padding_90[4]) = v11;
                    ptr->field_98 = v4;
                    if (Component__get_transform(ptr, 0))
                    {
                        Transform__get_rotation();
                        ptr->field_6c = v12;
                        *((unsigned int *)&ptr->padding_70[0]) = v10;
                        *((unsigned int *)&ptr->padding_70[4]) = v11;
                        ptr->field_78 = v4;
                        if (Component__get_transform(ptr, 0))
                        {
                            Transform__get_rotation();
                            ptr->field_7c = v12;
                            *((unsigned int *)&ptr->padding_80[0]) = v10;
                            *((unsigned int *)&ptr->padding_80[4]) = v11;
                            ptr->field_88 = v4;
                            if (!g_1fab3e1)
                            {
                                sub_f7d92c(&g_1ef22e8);
                                g_1fab3e1 = 1;
                            }
                            p = g_1ef22e8->field_b8;
                            v14 = p[15];
                            v15 = p[16];
                            v16 = p[17];
                            if (Component__get_transform(ptr, 0))
                            {
                                Transform__get_right();
                                if (!g_1fab3e2)
                                {
                                    sub_f7d92c("_F");
                                    g_1fab3e2 = 1;
                                }
                                if (!g_1ef07e8->field_e0)
                                    sub_f7da5c(g_1ef07e8);
                                v17 = [D] unsupported_Iop_SqrtF32();
                                v0 = 646978941;
                                v18 = 0;
                                v19 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(v17, 646978941)) >> 5 & 3 | (unsigned long long)(CmpF(v17, 646978941) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v17, 646978941)) >> 5 & 3 | (unsigned long long)(CmpF(v17, 646978941) & 1)) & ((unsigned long long)(char)(CmpF(v17, 646978941)) >> 5 & 3 | (unsigned long long)(CmpF(v17, 646978941) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                                v20 = v11;
                                if (!((char)v19))
                                {
                                    v21 = g_1ef07e8;
                                    v22 = (v16 * v11 + v14 * v12 + v15 * v10) / v17;
                                    v23 = 0xbf800000;
                                    v24 = [D] unsupported_Iop_ZeroHI96ofV128();
                                    v25 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v22, 0xbf800000)) >> 5 & 3 | (unsigned long long)(CmpF(v22, 0xbf800000) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF((v16 * v11 + v14 * v12 + v15 * v10) / v17, 0xbf800000)) >> 5 & 3 | (unsigned long long)(CmpF((v16 * v11 + v14 * v12 + v15 * v10) / v17, 0xbf800000) & 1)) & ((unsigned long long)(char)(CmpF(v22, 0xbf800000)) >> 5 & 3 | (unsigned long long)(CmpF((v16 * v11 + v14 * v12 + v15 * v10) / v17, 0xbf800000) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                                    if ((char)v25)
                                        v26 = v24;
                                    else
                                        v26 = 0xbf800000;
                                    if (!g_1ef07e8->field_e0)
                                        v21 = sub_f7da5c(g_1ef07e8);
                                    acos(v21);
                                    v17 = v26;
                                    v18 = v17 * 1113927393;
                                    v20 = v23;
                                }
                                ptr->field_5c = v18;
                                if (!g_1fab32c)
                                {
                                    sub_f7d92c(&g_1ef22e8);
                                    g_1fab32c = 1;
                                }
                                addr = g_1ef22e8->field_b8;
                                v28 = addr[6];
                                v29 = addr[7];
                                v30 = addr[8];
                                if (Component__get_transform(ptr, 0))
                                {
                                    Transform__get_up();
                                    if (!g_1fab3e2)
                                    {
                                        sub_f7d92c("_F");
                                        g_1fab3e2 = 1;
                                    }
                                    v31 = g_1ef07e8;
                                    if (!g_1ef07e8->field_e0)
                                        v31 = sub_f7da5c(g_1ef07e8);
                                    v32 = [D] unsupported_Iop_SqrtF32();
                                    v33 = 0;
                                    v34 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(v32, v0)) >> 5 & 3 | (unsigned long long)(CmpF(v32, v0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v32, v0)) >> 5 & 3 | (unsigned long long)(CmpF(v32, v0) & 1)) & ((unsigned long long)(char)(CmpF(v32, v0)) >> 5 & 3 | (unsigned long long)(CmpF(v32, v0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                                    if (!((char)v34))
                                    {
                                        v35 = g_1ef07e8;
                                        v36 = (v30 * v20 + v28 * v17 + v29 * v18) / v32;
                                        v37 = [D] unsupported_Iop_ZeroHI96ofV128();
                                        v38 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v36, 0xbf800000)) >> 5 & 3 | (unsigned long long)(CmpF(v36, 0xbf800000) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF((v30 * v20 + v28 * v17 + v29 * v18) / v32, 0xbf800000)) >> 5 & 3 | (unsigned long long)(CmpF((v30 * v20 + v28 * v17 + v29 * v18) / v32, 0xbf800000) & 1)) & ((unsigned long long)(char)(CmpF(v36, 0xbf800000)) >> 5 & 3 | (unsigned long long)(CmpF((v30 * v20 + v28 * v17 + v29 * v18) / v32, 0xbf800000) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                                        if ((char)v38)
                                            v39 = v37;
                                        else
                                            v39 = 0xbf800000;
                                        if (!g_1ef07e8->field_e0)
                                            v35 = sub_f7da5c(g_1ef07e8);
                                        v31 = acos(v35);
                                        v33 = v39 * 1113927393;
                                    }
                                    ptr->field_60 = v33;
                                    return v31;
                                }
                            }
                        }
                    }
                }
            }
        }
    }
LABEL_106b0b0:
    sub_f7db74();
}
```

## `maxCamera.OnEnable` — RVA `0xc6b0b4`

- Decompiled symbol: `maxCamera_OnEnable`
- Metadata signature: `private void OnEnable() { }`
- Native interval: `4` bytes
- Result: `pseudocode`
- Heuristic layout hint: `maxCamera_Recovered` matched 10 offsets against `maxCamera` metadata (confidence 0.77).

```c
typedef struct struct_3 {
    char padding_0[224];
    unsigned int field_e0;
} struct_3;

typedef struct maxCamera_Recovered {
    char padding_0[32];
    long long target;
    char padding_28[12];
    unsigned int distance;
    char padding_38[36];
    unsigned int xDeg;
    unsigned int yDeg;
    unsigned int currentDistance;
    unsigned int desiredDistance;
    unsigned int currentRotation;
    char padding_70[8];
    unsigned int field_78;
    unsigned int desiredRotation;
    char padding_80[8];
    unsigned int field_88;
    unsigned int rotation;
    char padding_90[8];
    unsigned int field_98;
    unsigned int position;
} maxCamera_Recovered;

struct_3 * maxCamera_OnEnable(struct_1 *a0)
{
    struct_3 *v0;  // x0

    v0 = maxCamera__Init(a0);
    return maxCamera__Init(a0);
}
```

## `maxCamera.LateUpdate` — RVA `0xc6b0b8`

- Decompiled symbol: `maxCamera_LateUpdate`
- Metadata signature: `private void LateUpdate() { }`
- Native interval: `1476` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: Decompiler produced no C-like text

```c
// 0x106b0b8: sub sp, sp, #0xa0
// 0x106b0bc: stp d15, d14, [sp, #0x30]
// 0x106b0c0: stp d13, d12, [sp, #0x40]
// 0x106b0c4: stp d11, d10, [sp, #0x50]
// 0x106b0c8: stp d9, d8, [sp, #0x60]
// 0x106b0cc: stp x30, x23, [sp, #0x70]
// 0x106b0d0: stp x22, x21, [sp, #0x80]
// 0x106b0d4: stp x20, x19, [sp, #0x90]
// 0x106b0d8: adrp x20, #0x1fab000
// 0x106b0dc: adrp x22, #0x1e8c000
// 0x106b0e0: ldrb w8, [x20, #0x330]
// 0x106b0e4: ldr x22, [x22, #0xe0]
// 0x106b0e8: mov x19, x0
// 0x106b0ec: tbnz w8, #0, #0x106b128
// 0x106b0f0: adrp x0, #0x1e8c000
// 0x106b0f4: ldr x0, [x0, #0xe0]
// 0x106b0f8: bl #0xf7d92c
// 0x106b0fc: adrp x0, #0x1e8c000
// 0x106b100: ldr x0, [x0, #0x530]
// 0x106b104: bl #0xf7d92c
// 0x106b108: adrp x0, #0x1e8c000
// 0x106b10c: ldr x0, [x0, #0x550]
// 0x106b110: bl #0xf7d92c
// 0x106b114: adrp x0, #0x1e8c000
// 0x106b118: ldr x0, [x0, #0x578]
// 0x106b11c: bl #0xf7d92c
// 0x106b120: mov w8, #1
// 0x106b124: strb w8, [x20, #0x330]
// 0x106b128: ldr x0, [x22]
// 0x106b12c: ldr w8, [x0, #0xe0]
// 0x106b130: cbnz w8, #0x106b138
// 0x106b134: bl #0xf7da5c
// 0x106b138: mov w0, #2
// 0x106b13c: mov x1, xzr
// 0x106b140: bl #0x1037afc
// 0x106b144: adrp x21, #0x1e8c000
// 0x106b148: ldr x21, [x21, #0x1e8]
// 0x106b14c: tbz w0, #0, #0x106b1f4
// 0x106b150: ldr x0, [x22]
// 0x106b154: ldr w8, [x0, #0xe0]
// 0x106b158: cbnz w8, #0x106b160
// 0x106b15c: bl #0xf7da5c
// 0x106b160: mov w0, #0x134
// 0x106b164: mov x1, xzr
// 0x106b168: bl #0x1036b94
// 0x106b16c: tbz w0, #0, #0x106b1f4
// 0x106b170: ldr x0, [x22]
// 0x106b174: ldr w8, [x0, #0xe0]
// 0x106b178: cbnz w8, #0x106b180
// 0x106b17c: bl #0xf7da5c
// 0x106b180: mov w0, #0x132
// 0x106b184: mov x1, xzr
// 0x106b188: bl #0x1036b94
// 0x106b18c: tbz w0, #0, #0x106b1f4
// 0x106b190: ldr x0, [x22]
// 0x106b194: ldr s9, [x19, #0x68]
// 0x106b198: ldr w8, [x0, #0xe0]
// 0x106b19c: cbnz w8, #0x106b1a4
// 0x106b1a0: bl #0xf7da5c
// 0x106b1a4: adrp x8, #0x1e8c000
// 0x106b1a8: ldr x8, [x8, #0x530]
// 0x106b1ac: mov x1, xzr
// 0x106b1b0: ldr x0, [x8]
// 0x106b1b4: bl #0x1035e20
// 0x106b1b8: mov x0, xzr
// 0x106b1bc: mov v8.16b, v0.16b
// 0x106b1c0: bl #0x1b89b60
// 0x106b1c4: ldr s2, [x19, #0x50]
// 0x106b1c8: ldr s1, [x19, #0x68]
// 0x106b1cc: fmul s0, s8, s0
// 0x106b1d0: scvtf s2, s2
// 0x106b1d4: fmul s0, s0, s2
// 0x106b1d8: fmov s2, #-0.12500000
// 0x106b1dc: fabs s1, s1
// 0x106b1e0: fmul s0, s0, s2
// 0x106b1e4: fmul s0, s1, s0
// 0x106b1e8: fadd s0, s9, s0
// 0x106b1ec: str s0, [x19, #0x68]
// 0x106b1f0: b #0x106b4f4
// 0x106b1f4: ldr x0, [x22]
// 0x106b1f8: ldr w8, [x0, #0xe0]
// 0x106b1fc: cbnz w8, #0x106b204
// 0x106b200: bl #0xf7da5c
// 0x106b204: mov w0, #2
// 0x106b208: mov x1, xzr
// 0x106b20c: bl #0x1037afc
// 0x106b210: tbz w0, #0, #0x106b3b0
// 0x106b214: ldr x0, [x22]
// 0x106b218: ldr w8, [x0, #0xe0]
// 0x106b21c: cbnz w8, #0x106b224
// 0x106b220: bl #0xf7da5c
// 0x106b224: mov w0, #0x134
// 0x106b228: mov x1, xzr
// 0x106b22c: bl #0x1036b94
// 0x106b230: tbz w0, #0, #0x106b3b0
// 0x106b234: ldr x0, [x22]
// 0x106b238: ldr s8, [x19, #0x5c]
// 0x106b23c: ldr w8, [x0, #0xe0]
// 0x106b240: cbnz w8, #0x106b248
// 0x106b244: bl #0xf7da5c
// 0x106b248: adrp x8, #0x1e8c000
// 0x106b24c: ldr x8, [x8, #0x550]
// 0x106b250: mov x1, xzr
// 0x106b254: ldr x0, [x8]
// 0x106b258: bl #0x1035e20
// 0x106b25c: ldr s1, [x19, #0x40]
// 0x106b260: adrp x8, #0x832000
// 0x106b264: ldr s9, [x8, #0x45c]
// 0x106b268: adrp x8, #0x1e8c000
// 0x106b26c: fmul s0, s0, s1
// 0x106b270: ldr s10, [x19, #0x60]
// 0x106b274: fmul s0, s0, s9
// 0x106b278: fadd s0, s8, s0
// 0x106b27c: str s0, [x19, #0x5c]
// 0x106b280: ldr x8, [x8, #0x530]
// 0x106b284: mov x1, xzr
// 0x106b288: ldr x0, [x8]
// 0x106b28c: bl #0x1035e20
// 0x106b290: ldp s1, s2, [x19, #0x44]
// 0x106b294: mov w8, #0x43b40000
// 0x106b298: ldr s3, [x19, #0x4c]
// 0x106b29c: mov x0, xzr
// 0x106b2a0: fmul s0, s0, s1
// 0x106b2a4: fmov s1, w8
// 0x106b2a8: mov w8, #-0x3c4c0000
// 0x106b2ac: fmul s0, s0, s9
// 0x106b2b0: fmov s4, w8
// 0x106b2b4: fsub s0, s10, s0
// 0x106b2b8: fadd s5, s0, s1
// 0x106b2bc: fcmp s0, s4
// 0x106b2c0: fcsel s0, s5, s0, mi
// 0x106b2c4: adrp x8, #0x832000
// 0x106b2c8: fcmp s0, s1
// 0x106b2cc: fadd s4, s0, s4
// 0x106b2d0: ldr s5, [x19, #0x5c]
// 0x106b2d4: ldr s1, [x8, #0x3e4]
// 0x106b2d8: scvtf s3, s3
// 0x106b2dc: fcsel s0, s4, s0, gt
// 0x106b2e0: scvtf s2, s2
// 0x106b2e4: fcmp s0, s3
// 0x106b2e8: fcsel s3, s3, s0, gt
// 0x106b2ec: fcmp s0, s2
// 0x106b2f0: fcsel s0, s3, s2, pl
// 0x106b2f4: str s0, [x19, #0x60]
// 0x106b2f8: fmul s0, s0, s1
// 0x106b2fc: fmul s1, s5, s1
// 0x106b300: fmov s2, wzr
// 0x106b304: bl #0x1b8b12c
// 0x106b308: mov x0, x19
// 0x106b30c: mov x1, xzr
// 0x106b310: stp s0, s1, [x19, #0x7c]
// 0x106b314: stp s2, s3, [x19, #0x84]
// 0x106b318: bl #0x1b92154
// 0x106b31c: cbz x0, #0x106b678
// 0x106b320: mov x1, xzr
// 0x106b324: bl #0x1b9d6f0
// 0x106b328: ldp s12, s13, [x19, #0x7c]
// 0x106b32c: ldp s14, s15, [x19, #0x84]
// 0x106b330: mov x0, xzr
// 0x106b334: mov v8.16b, v0.16b
// 0x106b338: mov v9.16b, v1.16b
// 0x106b33c: mov v10.16b, v2.16b
// 0x106b340: mov v11.16b, v3.16b
// 0x106b344: stp s0, s1, [x19, #0x6c]
// 0x106b348: stp s2, s3, [x19, #0x74]
// 0x106b34c: bl #0x1b89b60
// 0x106b350: ldr s1, [x19, #0x58]
// 0x106b354: mov v2.16b, v10.16b
// 0x106b358: mov v3.16b, v11.16b
// 0x106b35c: mov v4.16b, v12.16b
// 0x106b360: fmul s0, s0, s1
// 0x106b364: str s0, [sp]
// 0x106b368: mov v0.16b, v8.16b
// 0x106b36c: mov v1.16b, v9.16b
// 0x106b370: mov v5.16b, v13.16b
// 0x106b374: mov v6.16b, v14.16b
// 0x106b378: mov v7.16b, v15.16b
// 0x106b37c: mov x0, xzr
// 0x106b380: bl #0x1b8b058
// 0x106b384: mov x0, x19
// 0x106b388: mov x1, xzr
// 0x106b38c: stp s0, s1, [x19, #0x8c]
// 0x106b390: stp s2, s3, [x19, #0x94]
// 0x106b394: bl #0x1b92154
// 0x106b398: cbz x0, #0x106b678
// 0x106b39c: ldp s2, s3, [x19, #0x94]
// 0x106b3a0: ldp s0, s1, [x19, #0x8c]
// 0x106b3a4: mov x1, xzr
// 0x106b3a8: bl #0x1b9d774
// 0x106b3ac: b #0x106b4f4
// 0x106b3b0: ldr x0, [x22]
// 0x106b3b4: ldr w8, [x0, #0xe0]
// 0x106b3b8: cbnz w8, #0x106b3c0
// 0x106b3bc: bl #0xf7da5c
// 0x106b3c0: mov w0, #2
// 0x106b3c4: mov x1, xzr
// 0x106b3c8: bl #0x1037afc
// 0x106b3cc: tbz w0, #0, #0x106b4f4
// 0x106b3d0: ldr x20, [x19, #0x20]
// 0x106b3d4: mov x0, x19
// 0x106b3d8: mov x1, xzr
// 0x106b3dc: bl #0x1b92154
// 0x106b3e0: cbz x0, #0x106b678
// 0x106b3e4: mov x1, xzr
// 0x106b3e8: bl #0x1b9d6f0
// 0x106b3ec: cbz x20, #0x106b678
// 0x106b3f0: mov x0, x20
// 0x106b3f4: mov x1, xzr
// 0x106b3f8: bl #0x1b9d774
// 0x106b3fc: adrp x23, #0x1fab000
// 0x106b400: ldrb w8, [x23, #0x3e1]
// 0x106b404: ldr x20, [x19, #0x20]
// 0x106b408: cbnz w8, #0x106b420
// 0x106b40c: adrp x0, #0x1e8c000
// 0x106b410: ldr x0, [x0, #0x1e8]
// 0x106b414: bl #0xf7d92c
// 0x106b418: mov w8, #1
// 0x106b41c: strb w8, [x23, #0x3e1]
// 0x106b420: ldr x8, [x21]
// 0x106b424: ldr x0, [x22]
// 0x106b428: ldr x8, [x8, #0xb8]
// 0x106b42c: ldr w9, [x0, #0xe0]
// 0x106b430: ldp s8, s9, [x8, #0x3c]
// 0x106b434: ldr s10, [x8, #0x44]
// 0x106b438: cbnz w9, #0x106b440
// 0x106b43c: bl #0xf7da5c
// 0x106b440: adrp x8, #0x1e8c000
// 0x106b444: ldr x8, [x8, #0x550]
// 0x106b448: mov x1, xzr
// 0x106b44c: ldr x0, [x8]
// 0x106b450: bl #0x1035e20
// 0x106b454: cbz x20, #0x106b678
// 0x106b458: ldr s3, [x19, #0x54]
// 0x106b45c: fneg s0, s0
// 0x106b460: fmul s1, s10, s0
// 0x106b464: fmul s4, s9, s0
// 0x106b468: fmul s0, s8, s0
// 0x106b46c: fmul s2, s1, s3
// 0x106b470: fmul s1, s4, s3
// 0x106b474: fmul s0, s0, s3
// 0x106b478: mov x0, x20
// 0x106b47c: mov x1, xzr
// 0x106b480: bl #0x1b9e084
// 0x106b484: ldr x20, [x19, #0x20]
// 0x106b488: mov x0, x19
// 0x106b48c: mov x1, xzr
// 0x106b490: bl #0x1b92154
// 0x106b494: cbz x0, #0x106b678
// 0x106b498: mov x1, xzr
// 0x106b49c: bl #0x1b9d940
// 0x106b4a0: adrp x8, #0x1e8c000
// 0x106b4a4: ldr x8, [x8, #0x530]
// 0x106b4a8: mov x1, xzr
// 0x106b4ac: mov v8.16b, v0.16b
// 0x106b4b0: mov v9.16b, v1.16b
// 0x106b4b4: ldr x0, [x8]
// 0x106b4b8: mov v10.16b, v2.16b
// 0x106b4bc: bl #0x1035e20
// 0x106b4c0: cbz x20, #0x106b678
// 0x106b4c4: ldr s3, [x19, #0x54]
// 0x106b4c8: fneg s0, s0
// 0x106b4cc: fmul s1, s10, s0
// 0x106b4d0: fmul s4, s9, s0
// 0x106b4d4: fmul s0, s8, s0
// 0x106b4d8: fmul s2, s1, s3
// 0x106b4dc: fmul s1, s4, s3
// 0x106b4e0: fmul s0, s0, s3
// 0x106b4e4: mov x0, x20
// 0x106b4e8: mov w1, wzr
// 0x106b4ec: mov x2, xzr
// 0x106b4f0: bl #0x1b9df94
// 0x106b4f4: ldr x0, [x22]
// 0x106b4f8: adrp x20, #0x1e8c000
// 0x106b4fc: ldr s9, [x19, #0x68]
// 0x106b500: ldr w8, [x0, #0xe0]
// 0x106b504: ldr x20, [x20, #0x578]
// 0x106b508: cbnz w8, #0x106b510
// 0x106b50c: bl #0xf7da5c
// 0x106b510: ldr x0, [x20]
// 0x106b514: mov x1, xzr
// 0x106b518: bl #0x1035e20
// 0x106b51c: mov x0, xzr
// 0x106b520: mov v8.16b, v0.16b
// 0x106b524: bl #0x1b89b60
// 0x106b528: ldr s1, [x19, #0x50]
// 0x106b52c: fmul s0, s8, s0
// 0x106b530: ldp s8, s4, [x19, #0x64]
// 0x106b534: ldp s3, s2, [x19, #0x38]
// 0x106b538: scvtf s1, s1
// 0x106b53c: fmul s0, s0, s1
// 0x106b540: fabs s1, s4
// 0x106b544: fmul s0, s0, s1
// 0x106b548: fsub s0, s9, s0
// 0x106b54c: fcmp s0, s3
// 0x106b550: fcsel s1, s3, s0, gt
// 0x106b554: fcmp s0, s2
// 0x106b558: fcsel s9, s1, s2, pl
// 0x106b55c: mov x0, xzr
// 0x106b560: str s9, [x19, #0x68]
// 0x106b564: bl #0x1b89b60
// 0x106b568: ldr s1, [x19, #0x58]
// 0x106b56c: fmov s2, #1.00000000
// 0x106b570: fmov s3, wzr
// 0x106b574: ldr x0, [x19, #0x20]
// 0x106b578: fmul s0, s0, s1
// 0x106b57c: fmin s1, s0, s2
// 0x106b580: fcmp s0, #0.0
// 0x106b584: fcsel s0, s1, s3, pl
// 0x106b588: fsub s1, s9, s8
// 0x106b58c: fmul s0, s1, s0
// 0x106b590: fadd s0, s8, s0
// 0x106b594: str s0, [x19, #0x64]
// 0x106b598: cbz x0, #0x106b678
// 0x106b59c: mov x1, xzr
// 0x106b5a0: bl #0x1b9d508
// 0x106b5a4: adrp x20, #0x1fab000
// 0x106b5a8: ldp s9, s10, [x19, #0x8c]
// 0x106b5ac: ldrb w8, [x20, #0x3e3]
// 0x106b5b0: ldp s12, s11, [x19, #0x94]
// 0x106b5b4: mov v8.16b, v2.16b
// 0x106b5b8: str d0, [sp, #0x20]
// 0x106b5bc: str d1, [sp, #0x10]
// 0x106b5c0: cbnz w8, #0x106b5d8
// 0x106b5c4: adrp x0, #0x1e8c000
// 0x106b5c8: ldr x0, [x0, #0x1e8]
// 0x106b5cc: bl #0xf7d92c
// 0x106b5d0: mov w8, #1
// 0x106b5d4: strb w8, [x20, #0x3e3]
// 0x106b5d8: ldr x8, [x21]
// 0x106b5dc: mov v0.16b, v9.16b
// 0x106b5e0: mov v1.16b, v10.16b
// 0x106b5e4: mov v2.16b, v12.16b
// 0x106b5e8: ldr x8, [x8, #0xb8]
// 0x106b5ec: mov v3.16b, v11.16b
// 0x106b5f0: mov x0, xzr
// 0x106b5f4: ldp s4, s5, [x8, #0x48]
// 0x106b5f8: ldr s6, [x8, #0x50]
// 0x106b5fc: bl #0x1b8b504
// 0x106b600: ldp q4, q5, [sp, #0x10]
// 0x106b604: ldr s3, [x19, #0x64]
// 0x106b608: mov v0.s[1], v1.s[0]
// 0x106b60c: ldr s1, [x19, #0x30]
// 0x106b610: mov v5.s[1], v4.s[0]
// 0x106b614: ldr d4, [x19, #0x28]
// 0x106b618: fmul v0.2s, v0.2s, v3.s[0]
// 0x106b61c: fmul s2, s2, s3
// 0x106b620: fadd s1, s2, s1
// 0x106b624: fadd v0.2s, v0.2s, v4.2s
// 0x106b628: fsub v0.2s, v5.2s, v0.2s
// 0x106b62c: fsub s1, s8, s1
// 0x106b630: mov x0, x19
// 0x106b634: mov x1, xzr
// 0x106b638: stur d0, [x19, #0x9c]
// 0x106b63c: str s1, [x19, #0xa4]
// 0x106b640: bl #0x1b92154
// 0x106b644: cbz x0, #0x106b678
// 0x106b648: ldp s1, s2, [x19, #0xa0]
// 0x106b64c: ldr s0, [x19, #0x9c]
// 0x106b650: ldp x20, x19, [sp, #0x90]
// 0x106b654: ldp x22, x21, [sp, #0x80]
// 0x106b658: ldp x30, x23, [sp, #0x70]
// 0x106b65c: ldp d9, d8, [sp, #0x60]
// 0x106b660: ldp d11, d10, [sp, #0x50]
// 0x106b664: ldp d13, d12, [sp, #0x40]
// 0x106b668: ldp d15, d14, [sp, #0x30]
// 0x106b66c: mov x1, xzr
// 0x106b670: add sp, sp, #0xa0
// 0x106b674: b #0x1b9d5a8
// 0x106b678: bl #0xf7db74
```

## `maxCamera.ClampAngle` — RVA `0xc6b67c`

- Decompiled symbol: `maxCamera_ClampAngle`
- Metadata signature: `private static float ClampAngle(float angle, float min, float max) { }`
- Native interval: `60` bytes
- Result: `pseudocode`

```c
long long maxCamera_ClampAngle(void)
{
    unsigned int v0;  // s0
    unsigned int v1;  // s4
    unsigned long v10;  // 4129
    unsigned long v11;  // x0
    unsigned long v12;  // x0
    unsigned long v2;  // 4148
    unsigned int v3;  // s0
    unsigned int v4;  // s4
    unsigned long v5;  // 4142
    unsigned int v6;  // s0
    unsigned int v7;  // s2
    unsigned long v8;  // 4129
    unsigned int v9;  // s1

    v1 = v0 + 0x43b40000;
    v2 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(v0, 0xc3b40000)) >> 5 & 3 | (unsigned long long)(CmpF(v0, 0xc3b40000) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v0, 0xc3b40000)) >> 5 & 3 | (unsigned long long)(CmpF(v0, 0xc3b40000) & 1)) & ((unsigned long long)(char)(CmpF(v0, 0xc3b40000)) >> 5 & 3 | (unsigned long long)(CmpF(v0, 0xc3b40000) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if ((char)v2)
        v3 = v1;
    else
        v3 = v0;
    v4 = v3 + 0xc3b40000;
    v5 = arm64g_calculate_condition(192, (((((unsigned long long)(char)(CmpF(v3, 0x43b40000)) >> 5 & 3 | (unsigned long long)(CmpF(v3, 0x43b40000) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v3, 0x43b40000)) >> 5 & 3 | (unsigned long long)(CmpF(v3, 0x43b40000) & 1)) & ((unsigned long long)(char)(CmpF(v3, 0x43b40000)) >> 5 & 3 | (unsigned long long)(CmpF(v3, 0x43b40000) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if ((char)v5)
        v6 = v4;
    else
        v6 = v3;
    v8 = arm64g_calculate_condition(192, (((((unsigned long long)(char)(CmpF(v6, v7)) >> 5 & 3 | (unsigned long long)(CmpF(v6, v7) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v6, v7)) >> 5 & 3 | (unsigned long long)(CmpF(v6, v7) & 1)) & ((unsigned long long)(char)(CmpF(v6, v7)) >> 5 & 3 | (unsigned long long)(CmpF(v6, v7) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    v10 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v6, v9)) >> 5 & 3 | (unsigned long long)(CmpF(v6, v9) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v6, v9)) >> 5 & 3 | (unsigned long long)(CmpF(v6, v9) & 1)) & ((unsigned long long)(char)(CmpF(v6, v9)) >> 5 & 3 | (unsigned long long)(CmpF(v6, v9) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if (!((char)v10))
        return v12;
    return v11;
}
```

## `maxCamera.ctor` — RVA `0xc6b6b8`

- Decompiled symbol: `maxCamera_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `60` bytes
- Result: `pseudocode`
- Heuristic layout hint: `maxCamera_Recovered` matched 5 offsets against `maxCamera` metadata (confidence 1.00).

```c
typedef struct maxCamera_Recovered {
    char padding_0[52];
    uint128_t distance;
    unsigned int ySpeed;
    unsigned long long yMinLimit;
    unsigned int zoomRate;
    unsigned long long panSpeed;
} maxCamera_Recovered;

long long maxCamera_ctor(struct_0 *ptr)
{
    long long v0;  // x0

    *((uint128_t *)&(&ptr->padding_0)[1]) = 0x434800003f19999a41a0000040a00000;
    *((unsigned int *)((char *)&ptr->field_34 + 4)) = 0x43480000;
    *((unsigned long long *)((char *)&ptr->field_34 + 8)) = 347892350896;
    ptr->field_44 = 40;
    *((unsigned long long *)&(&ptr->field_44)[1]) = 4656722015751346586;
    v0 = MonoBehaviour__ctor();
    return MonoBehaviour__ctor();
}
```
