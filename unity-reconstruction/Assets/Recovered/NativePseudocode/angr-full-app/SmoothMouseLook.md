# Native pseudocode: SmoothMouseLook

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `SmoothMouseLook.Start` — RVA `0xc8d640`

- Decompiled symbol: `SmoothMouseLook_Start`
- Metadata signature: `private void Start() { }`
- Native interval: `564` bytes
- Result: `pseudocode`
- Heuristic layout hint: `SmoothMouseLook_Recovered` matched 7 offsets against `SmoothMouseLook` metadata (confidence 0.70).

```c
typedef struct struct_2 {
    char padding_0[40];
    long long field_28;
} struct_2;

typedef struct SmoothMouseLook_Recovered {
    char padding_0[32];
    long long InputComponent;
    long long playerObj;
    long long FPSPlayerComponent;
    unsigned int sensitivity;
    unsigned int sensitivityAmt;
    char padding_40[72];
    unsigned int originalRotation;
    unsigned int field_8c;
    unsigned int field_90;
    unsigned int field_94;
    long long myTransform;
} SmoothMouseLook_Recovered;

typedef struct struct_1 {
    char padding_0[224];
    unsigned int field_e0;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1eeed08;
extern struct_1 *g_1ef0c58;
extern long long g_1efcf38;
extern long long g_1efd080;
extern long long g_1efebb8;
extern long long g_1efec08;
extern char g_1fab43d;

void SmoothMouseLook_Start(struct_3 *ptr)
{
    unsigned long long v5;  // d8
    unsigned long long v6;  // x30
    struct_3 *p;  // x20
    struct_3 *v16;  // x20
    long long v17;  // x1
    struct_3 *addr;  // x0
    long long v19;  // x0
    long long v20;  // x0
    struct_3 *ptr3;  // x20
    struct_3 *v22;  // x20
    unsigned int v23;  // s4
    unsigned int v24;  // s0
    unsigned long long v7;  // x21
    unsigned int v25;  // s1
    unsigned int v26;  // s3
    unsigned long long v8;  // x20
    unsigned long long v9;  // x19
    struct_2 *ptr5;  // x0
    long long v11;  // x1
    struct_3 *ptr4;  // x20
    struct_3 *v13;  // x20
    long long v14;  // x0
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
    if (!(g_1fab43d & 1))
    {
        sub_f7d92c(&g_1eeed08);
        sub_f7d92c(&g_1efcf38);
        sub_f7d92c(&g_1efd080);
        sub_f7d92c(&g_1efebb8);
        sub_f7d92c(&g_1efec08);
        sub_f7d92c(&g_1ef0c58);
        g_1fab43d = 1;
    }
    if (Camera__get_main(0) && Component__get_transform() && (ptr5 = (struct_2 *)sub_1231bc8(), ptr5))
    {
        v11 = ptr5->field_28;
        ptr4 = ptr;
        ptr4->field_28 = v11;
        v13 = &ptr4->field_28;
        sub_f7d8d0(v13, v11);
        if (*((long long *)&v13->padding_0[0]))
        {
            v14 = sub_1249224(*((long long *)&v13->padding_0[0]), g_1efec08);
            p = ptr;
            p->field_20 = v14;
            v16 = &p->field_20;
            sub_f7d8d0(v16, v14);
            if (*((long long *)&v16->padding_0[8]))
            {
                v17 = sub_1249224(*((long long *)&v16->padding_0[8]), g_1efebb8);
                addr = ptr;
                addr->field_30 = v17;
                sub_f7d8d0((struct SmoothMouseLook_Recovered *)&addr->field_30, v17);
                v19 = sub_1231bc8(ptr, g_1efd080);
                if (!g_1ef0c58->field_e0)
                    sub_f7da5c(g_1ef0c58);
                if (!((char)Object__op_Implicit(v19, 0) & 1))
                {
LABEL_108d7a0:
                    v20 = Component__get_transform(ptr, 0);
                    ptr3 = ptr;
                    ptr3->field_98 = v20;
                    v22 = &ptr3->field_98;
                    sub_f7d8d0(v22, v20);
                    if (*((long long *)&v22->padding_0[0]) && Transform__get_parent(*((long long *)&v22->padding_0[0]), 0) && Component__get_transform())
                    {
                        Transform__get_eulerAngles();
                        if (*((long long *)&v22->padding_0[0]) && Transform__get_parent(*((long long *)&v22->padding_0[0]), 0) && Component__get_transform())
                        {
                            Transform__get_eulerAngles();
                            Quaternion__Internal_FromEulerRad(0);
                            v23 = ptr->field_38;
                            ptr->field_88 = v24 * 1016003125;
                            ptr->field_8c = v25 * 1016003125;
                            ptr->field_90 = 0;
                            ptr->field_94 = v26;
                            ptr->field_3c = v23;
                            if (!g_1eeed08->field_e0)
                                sub_f7da5c(g_1eeed08);
                            CFCursor__set_visible();
                            return;
                        }
                    }
                }
                else if (sub_1231bc8(ptr, g_1efd080))
                {
                    Rigidbody__set_freezeRotation();
                    goto LABEL_108d7a0;
                }
            }
        }
    }
    sub_f7db74();
}
```

## `SmoothMouseLook.Update` — RVA `0xc8d874`

- Decompiled symbol: `SmoothMouseLook_Update`
- Metadata signature: `private void Update() { }`
- Native interval: `1852` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: Decompiler produced no C-like text

```c
// 0x108d874: sub sp, sp, #0x70
// 0x108d878: stp d15, d14, [sp, #0x10]
// 0x108d87c: stp d13, d12, [sp, #0x20]
// 0x108d880: stp d11, d10, [sp, #0x30]
// 0x108d884: stp d9, d8, [sp, #0x40]
// 0x108d888: stp x30, x21, [sp, #0x50]
// 0x108d88c: stp x20, x19, [sp, #0x60]
// 0x108d890: adrp x20, #0x1fab000
// 0x108d894: ldrb w8, [x20, #0x43e]
// 0x108d898: mov x19, x0
// 0x108d89c: tbnz w8, #0, #0x108d8b4
// 0x108d8a0: adrp x0, #0x1e8c000
// 0x108d8a4: ldr x0, [x0, #0x458]
// 0x108d8a8: bl #0xf7d92c
// 0x108d8ac: mov w8, #1
// 0x108d8b0: strb w8, [x20, #0x43e]
// 0x108d8b4: adrp x20, #0x1e8c000
// 0x108d8b8: ldr x20, [x20, #0x458]
// 0x108d8bc: mov x0, xzr
// 0x108d8c0: bl #0x1b9ae58
// 0x108d8c4: fcmp s0, #0.0
// 0x108d8c8: b.le #0x108dc24
// 0x108d8cc: mov x0, xzr
// 0x108d8d0: bl #0x1b9ae30
// 0x108d8d4: fcmp s0, #0.0
// 0x108d8d8: b.le #0x108dc24
// 0x108d8dc: ldr x0, [x20]
// 0x108d8e0: ldr w8, [x0, #0xe0]
// 0x108d8e4: cbnz w8, #0x108d8ec
// 0x108d8e8: bl #0xf7da5c
// 0x108d8ec: mov w0, #1
// 0x108d8f0: mov x1, xzr
// 0x108d8f4: bl #0x10384e4
// 0x108d8f8: mov w0, wzr
// 0x108d8fc: mov x1, xzr
// 0x108d900: bl #0x103881c
// 0x108d904: ldr s8, [x19, #0x50]
// 0x108d908: ldrb w8, [x19, #0xa8]
// 0x108d90c: str s8, [x19, #0x7c]
// 0x108d910: cbnz w8, #0x108d978
// 0x108d914: ldr x8, [x19, #0x20]
// 0x108d918: cbz x8, #0x108dfac
// 0x108d91c: ldr s9, [x8, #0xe4]
// 0x108d920: ldr s10, [x19, #0x3c]
// 0x108d924: mov x0, xzr
// 0x108d928: bl #0x1b9ae58
// 0x108d92c: ldr x8, [x19, #0x20]
// 0x108d930: fmul s1, s9, s10
// 0x108d934: fmul s0, s1, s0
// 0x108d938: fadd s0, s8, s0
// 0x108d93c: str s0, [x19, #0x50]
// 0x108d940: cbz x8, #0x108dfac
// 0x108d944: ldr s8, [x19, #0x54]
// 0x108d948: ldrb w20, [x19, #0xa9]
// 0x108d94c: ldr s9, [x8, #0xe8]
// 0x108d950: ldr s10, [x19, #0x3c]
// 0x108d954: mov x0, xzr
// 0x108d958: bl #0x1b9ae58
// 0x108d95c: fmul s1, s9, s10
// 0x108d960: fmul s2, s1, s0
// 0x108d964: fnmul s0, s1, s0
// 0x108d968: cmp w20, #0
// 0x108d96c: fcsel s0, s2, s0, eq
// 0x108d970: fadd s0, s8, s0
// 0x108d974: str s0, [x19, #0x54]
// 0x108d978: ldr x8, [x19, #0x20]
// 0x108d97c: cbz x8, #0x108dfac
// 0x108d980: ldr s8, [x19, #0x4c]
// 0x108d984: ldr s9, [x8, #0xe8]
// 0x108d988: ldr s10, [x19, #0x3c]
// 0x108d98c: mov x0, xzr
// 0x108d990: bl #0x1b9ae58
// 0x108d994: ldr s1, [x19, #0xa4]
// 0x108d998: fmul s2, s9, s10
// 0x108d99c: fmul s0, s2, s0
// 0x108d9a0: fsub s0, s8, s0
// 0x108d9a4: fcmp s0, s1
// 0x108d9a8: b.pl #0x108d9bc
// 0x108d9ac: ldr s0, [x19, #0x54]
// 0x108d9b0: str wzr, [x19, #0xa4]
// 0x108d9b4: fadd s0, s1, s0
// 0x108d9b8: str s0, [x19, #0x54]
// 0x108d9bc: ldr x8, [x19, #0x20]
// 0x108d9c0: cbz x8, #0x108dfac
// 0x108d9c4: ldr s9, [x19, #0x44]
// 0x108d9c8: ldr s10, [x8, #0xe4]
// 0x108d9cc: ldr s11, [x19, #0x3c]
// 0x108d9d0: mov x0, xzr
// 0x108d9d4: bl #0x1b9ae58
// 0x108d9d8: ldr s8, [x19, #0xa0]
// 0x108d9dc: fmul s1, s10, s11
// 0x108d9e0: fmul s1, s1, s0
// 0x108d9e4: ldr s0, [x19, #0x50]
// 0x108d9e8: fsub s1, s9, s1
// 0x108d9ec: fcmp s1, s8
// 0x108d9f0: b.pl #0x108da00
// 0x108d9f4: fadd s0, s8, s0
// 0x108d9f8: fmov s8, wzr
// 0x108d9fc: str wzr, [x19, #0xa0]
// 0x108da00: ldp s9, s10, [x19, #0x40]
// 0x108da04: mov w8, #0x43b40000
// 0x108da08: fmov s1, w8
// 0x108da0c: bl #0x1db0cb0
// 0x108da10: mov w8, #-0x3c4c0000
// 0x108da14: fmov s1, w8
// 0x108da18: fcmp s0, s1
// 0x108da1c: b.lt #0x108da60
// 0x108da20: mov w8, #0x43b40000
// 0x108da24: fmov s1, w8
// 0x108da28: fcmp s0, s1
// 0x108da2c: b.hi #0x108da60
// 0x108da30: mov w8, #0x43b40000
// 0x108da34: mov w9, #-0x3c4c0000
// 0x108da38: fmov s1, w8
// 0x108da3c: fmov s3, w9
// 0x108da40: fadd s2, s0, s1
// 0x108da44: fcmp s0, s3
// 0x108da48: fcsel s0, s2, s0, mi
// 0x108da4c: fcmp s0, s1
// 0x108da50: b.le #0x108da60
// 0x108da54: mov w8, #-0x3c4c0000
// 0x108da58: fmov s1, w8
// 0x108da5c: fadd s0, s0, s1
// 0x108da60: ldr s2, [x19, #0x54]
// 0x108da64: ldr s11, [x19, #0xa4]
// 0x108da68: ldp s1, s3, [x19, #0x48]
// 0x108da6c: fcmp s0, s10
// 0x108da70: fcsel s4, s10, s0, gt
// 0x108da74: fcmp s0, s9
// 0x108da78: mov w8, #0x43b40000
// 0x108da7c: fcsel s9, s4, s9, pl
// 0x108da80: fsub s10, s1, s11
// 0x108da84: fmov s1, w8
// 0x108da88: mov v0.16b, v2.16b
// 0x108da8c: str s9, [x19, #0x50]
// 0x108da90: fsub s12, s3, s11
// 0x108da94: bl #0x1db0cb0
// 0x108da98: mov w8, #-0x3c4c0000
// 0x108da9c: fmov s1, w8
// 0x108daa0: fcmp s0, s1
// 0x108daa4: b.lt #0x108dae8
// 0x108daa8: mov w8, #0x43b40000
// 0x108daac: fmov s1, w8
// 0x108dab0: fcmp s0, s1
// 0x108dab4: b.hi #0x108dae8
// 0x108dab8: mov w8, #0x43b40000
// 0x108dabc: mov w9, #-0x3c4c0000
// 0x108dac0: fmov s1, w8
// 0x108dac4: fmov s3, w9
// 0x108dac8: fadd s2, s0, s1
// 0x108dacc: fcmp s0, s3
// 0x108dad0: fcsel s0, s2, s0, mi
// 0x108dad4: fcmp s0, s1
// 0x108dad8: b.le #0x108dae8
// 0x108dadc: mov w8, #-0x3c4c0000
// 0x108dae0: fmov s1, w8
// 0x108dae4: fadd s0, s0, s1
// 0x108dae8: fcmp s0, s12
// 0x108daec: fcsel s1, s12, s0, gt
// 0x108daf0: fcmp s0, s10
// 0x108daf4: fcsel s0, s1, s10, pl
// 0x108daf8: str s0, [x19, #0x54]
// 0x108dafc: fadd s0, s11, s0
// 0x108db00: str s0, [x19, #0x78]
// 0x108db04: adrp x20, #0x1fab000
// 0x108db08: ldrb w8, [x20, #0x32c]
// 0x108db0c: cbnz w8, #0x108db24
// 0x108db10: adrp x0, #0x1e8c000
// 0x108db14: ldr x0, [x0, #0x1e8]
// 0x108db18: bl #0xf7d92c
// 0x108db1c: mov w8, #1
// 0x108db20: strb w8, [x20, #0x32c]
// 0x108db24: adrp x20, #0x1e8c000
// 0x108db28: ldr x20, [x20, #0x1e8]
// 0x108db2c: fadd s0, s9, s8
// 0x108db30: mov x0, xzr
// 0x108db34: ldr x8, [x20]
// 0x108db38: ldr x8, [x8, #0xb8]
// 0x108db3c: ldp s1, s2, [x8, #0x18]
// 0x108db40: ldr s3, [x8, #0x20]
// 0x108db44: bl #0x1b8b260
// 0x108db48: stp s0, s1, [x19, #0x58]
// 0x108db4c: stp s2, s3, [x19, #0x60]
// 0x108db50: adrp x21, #0x1fab000
// 0x108db54: ldr s8, [x19, #0x54]
// 0x108db58: ldrb w8, [x21, #0x3e1]
// 0x108db5c: ldr s9, [x19, #0xa4]
// 0x108db60: cbnz w8, #0x108db78
// 0x108db64: adrp x0, #0x1e8c000
// 0x108db68: ldr x0, [x0, #0x1e8]
// 0x108db6c: bl #0xf7d92c
// 0x108db70: mov w8, #1
// 0x108db74: strb w8, [x21, #0x3e1]
// 0x108db78: ldr x8, [x20]
// 0x108db7c: mov x0, xzr
// 0x108db80: ldr x8, [x8, #0xb8]
// 0x108db84: ldp s0, s2, [x8, #0x3c]
// 0x108db88: ldr s3, [x8, #0x44]
// 0x108db8c: fneg s1, s0
// 0x108db90: fneg s2, s2
// 0x108db94: fneg s3, s3
// 0x108db98: fadd s0, s8, s9
// 0x108db9c: bl #0x1b8b260
// 0x108dba0: stp s0, s1, [x19, #0x68]
// 0x108dba4: ldr s0, [x19, #0x7c]
// 0x108dba8: ldr s1, [x19, #0x50]
// 0x108dbac: mov w8, #0x43b40000
// 0x108dbb0: fmov s4, w8
// 0x108dbb4: mov w8, #-0x3c4c0000
// 0x108dbb8: fsub s0, s1, s0
// 0x108dbbc: fdiv s1, s0, s4
// 0x108dbc0: stp s2, s3, [x19, #0x70]
// 0x108dbc4: fmov s2, w8
// 0x108dbc8: frintm s1, s1
// 0x108dbcc: fmul s1, s1, s2
// 0x108dbd0: fadd s0, s0, s1
// 0x108dbd4: mov w8, #0x43340000
// 0x108dbd8: fmov s1, wzr
// 0x108dbdc: fmin s3, s0, s4
// 0x108dbe0: fcmp s0, #0.0
// 0x108dbe4: fmov s0, w8
// 0x108dbe8: ldrb w8, [x19, #0xaa]
// 0x108dbec: fcsel s1, s3, s1, pl
// 0x108dbf0: fadd s2, s1, s2
// 0x108dbf4: fcmp s1, s0
// 0x108dbf8: fcsel s0, s2, s1, gt
// 0x108dbfc: str s0, [x19, #0x7c]
// 0x108dc00: cbz w8, #0x108dc68
// 0x108dc04: ldp x20, x19, [sp, #0x60]
// 0x108dc08: ldp x30, x21, [sp, #0x50]
// 0x108dc0c: ldp d9, d8, [sp, #0x40]
// 0x108dc10: ldp d11, d10, [sp, #0x30]
// 0x108dc14: ldp d13, d12, [sp, #0x20]
// 0x108dc18: ldp d15, d14, [sp, #0x10]
// 0x108dc1c: add sp, sp, #0x70
// 0x108dc20: ret
// 0x108dc24: ldr x0, [x20]
// 0x108dc28: ldr w8, [x0, #0xe0]
// 0x108dc2c: cbnz w8, #0x108dc34
// 0x108dc30: bl #0xf7da5c
// 0x108dc34: mov w0, wzr
// 0x108dc38: mov x1, xzr
// 0x108dc3c: bl #0x10384e4
// 0x108dc40: ldp x20, x19, [sp, #0x60]
// 0x108dc44: ldp x30, x21, [sp, #0x50]
// 0x108dc48: ldp d9, d8, [sp, #0x40]
// 0x108dc4c: ldp d11, d10, [sp, #0x30]
// 0x108dc50: ldp d13, d12, [sp, #0x20]
// 0x108dc54: ldp d15, d14, [sp, #0x10]
// 0x108dc58: mov w0, #1
// 0x108dc5c: mov x1, xzr
// 0x108dc60: add sp, sp, #0x70
// 0x108dc64: b #0x103881c
// 0x108dc68: ldr s8, [x19, #0x84]
// 0x108dc6c: mov x0, xzr
// 0x108dc70: bl #0x1b9ad30
// 0x108dc74: adrp x8, #0x832000
// 0x108dc78: ldr s1, [x8, #0x3b8]
// 0x108dc7c: ldr x20, [x19, #0x98]
// 0x108dc80: fadd s1, s8, s1
// 0x108dc84: fcmp s1, s0
// 0x108dc88: b.pl #0x108ddf8
// 0x108dc8c: cbz x20, #0x108dfac
// 0x108dc90: mov x0, x20
// 0x108dc94: mov x1, xzr
// 0x108dc98: bl #0x1b9d6f0
// 0x108dc9c: stp s1, s0, [sp, #8]
// 0x108dca0: mov v10.16b, v2.16b
// 0x108dca4: mov v11.16b, v3.16b
// 0x108dca8: ldp s0, s1, [x19, #0x90]
// 0x108dcac: ldp s2, s7, [x19, #0x58]
// 0x108dcb0: ldp s3, s4, [x19, #0x60]
// 0x108dcb4: ldp s5, s6, [x19, #0x88]
// 0x108dcb8: ldr s9, [x19, #0x80]
// 0x108dcbc: fmul s16, s1, s2
// 0x108dcc0: fmul s19, s0, s7
// 0x108dcc4: fmul s17, s5, s4
// 0x108dcc8: fmul s18, s6, s3
// 0x108dccc: fmul s20, s1, s7
// 0x108dcd0: fmul s21, s6, s4
// 0x108dcd4: fmul s22, s0, s2
// 0x108dcd8: fmul s23, s5, s3
// 0x108dcdc: fmul s24, s5, s7
// 0x108dce0: fmul s5, s5, s2
// 0x108dce4: fmul s2, s6, s2
// 0x108dce8: fmul s6, s6, s7
// 0x108dcec: fmul s7, s1, s3
// 0x108dcf0: fmul s1, s1, s4
// 0x108dcf4: fmul s4, s0, s4
// 0x108dcf8: fmul s0, s0, s3
// 0x108dcfc: fadd s3, s16, s17
// 0x108dd00: ldp s16, s17, [x19, #0x68]
// 0x108dd04: fadd s20, s20, s21
// 0x108dd08: fadd s4, s7, s4
// 0x108dd0c: ldp s7, s21, [x19, #0x70]
// 0x108dd10: fsub s1, s1, s5
// 0x108dd14: fadd s3, s18, s3
// 0x108dd18: fadd s5, s22, s20
// 0x108dd1c: fadd s4, s24, s4
// 0x108dd20: fsub s1, s1, s6
// 0x108dd24: fsub s3, s3, s19
// 0x108dd28: fsub s5, s5, s23
// 0x108dd2c: fsub s2, s4, s2
// 0x108dd30: fsub s0, s1, s0
// 0x108dd34: fmul s1, s16, s0
// 0x108dd38: fmul s4, s3, s21
// 0x108dd3c: fmul s6, s7, s5
// 0x108dd40: fmul s18, s17, s2
// 0x108dd44: fmul s19, s17, s0
// 0x108dd48: fmul s20, s5, s21
// 0x108dd4c: fmul s22, s16, s2
// 0x108dd50: fmul s23, s7, s3
// 0x108dd54: fmul s24, s17, s3
// 0x108dd58: fmul s3, s16, s3
// 0x108dd5c: fmul s16, s16, s5
// 0x108dd60: fmul s5, s17, s5
// 0x108dd64: fmul s17, s7, s0
// 0x108dd68: fmul s0, s0, s21
// 0x108dd6c: fmul s21, s2, s21
// 0x108dd70: fmul s2, s7, s2
// 0x108dd74: fadd s1, s1, s4
// 0x108dd78: fadd s4, s19, s20
// 0x108dd7c: fadd s7, s17, s21
// 0x108dd80: fsub s0, s0, s3
// 0x108dd84: fadd s1, s6, s1
// 0x108dd88: fadd s3, s22, s4
// 0x108dd8c: fadd s4, s24, s7
// 0x108dd90: fsub s0, s0, s5
// 0x108dd94: mov x0, xzr
// 0x108dd98: fsub s12, s1, s18
// 0x108dd9c: fsub s13, s3, s23
// 0x108dda0: fsub s14, s4, s16
// 0x108dda4: fsub s15, s0, s2
// 0x108dda8: bl #0x1b9ae30
// 0x108ddac: mov x0, xzr
// 0x108ddb0: mov v8.16b, v0.16b
// 0x108ddb4: bl #0x1b9ae58
// 0x108ddb8: mov w8, #0x42700000
// 0x108ddbc: fmul s1, s9, s8
// 0x108ddc0: fmov s2, w8
// 0x108ddc4: fmul s1, s1, s2
// 0x108ddc8: fdiv s0, s1, s0
// 0x108ddcc: str s0, [sp]
// 0x108ddd0: ldp s1, s0, [sp, #8]
// 0x108ddd4: mov v2.16b, v10.16b
// 0x108ddd8: mov v3.16b, v11.16b
// 0x108dddc: mov v4.16b, v12.16b
// 0x108dde0: mov v5.16b, v13.16b
// 0x108dde4: mov v6.16b, v14.16b
// 0x108dde8: mov v7.16b, v15.16b
// 0x108ddec: mov x0, xzr
// 0x108ddf0: bl #0x1b8af84
// 0x108ddf4: b #0x108def4
// 0x108ddf8: cbz x20, #0x108dfac
// 0x108ddfc: ldp s0, s1, [x19, #0x90]
// 0x108de00: ldp s2, s7, [x19, #0x58]
// 0x108de04: ldp s3, s4, [x19, #0x60]
// 0x108de08: ldp s5, s6, [x19, #0x88]
// 0x108de0c: fmul s16, s1, s2
// 0x108de10: fmul s19, s0, s7
// 0x108de14: fmul s17, s5, s4
// 0x108de18: fmul s18, s6, s3
// 0x108de1c: fmul s20, s1, s7
// 0x108de20: fmul s21, s6, s4
// 0x108de24: fmul s22, s0, s2
// 0x108de28: fmul s23, s5, s3
// 0x108de2c: fmul s24, s5, s7
// 0x108de30: fmul s5, s5, s2
// 0x108de34: fmul s2, s6, s2
// 0x108de38: fmul s6, s6, s7
// 0x108de3c: fmul s7, s1, s3
// 0x108de40: fmul s1, s1, s4
// 0x108de44: fmul s4, s0, s4
// 0x108de48: fmul s0, s0, s3
// 0x108de4c: fadd s3, s16, s17
// 0x108de50: ldp s16, s17, [x19, #0x68]
// 0x108de54: fadd s20, s20, s21
// 0x108de58: fadd s4, s7, s4
// 0x108de5c: ldp s7, s21, [x19, #0x70]
// 0x108de60: fsub s1, s1, s5
// 0x108de64: fadd s3, s18, s3
// 0x108de68: fadd s5, s22, s20
// 0x108de6c: fadd s4, s24, s4
// 0x108de70: fsub s1, s1, s6
// 0x108de74: fsub s3, s3, s19
// 0x108de78: fsub s5, s5, s23
// 0x108de7c: fsub s2, s4, s2
// 0x108de80: fsub s0, s1, s0
// 0x108de84: fmul s1, s0, s21
// 0x108de88: fmul s4, s16, s3
// 0x108de8c: fmul s6, s17, s5
// 0x108de90: fmul s18, s7, s2
// 0x108de94: fmul s19, s17, s3
// 0x108de98: fmul s20, s7, s0
// 0x108de9c: fmul s22, s2, s21
// 0x108dea0: fmul s23, s16, s5
// 0x108dea4: fmul s24, s5, s21
// 0x108dea8: fmul s5, s7, s5
// 0x108deac: fmul s7, s7, s3
// 0x108deb0: fmul s3, s3, s21
// 0x108deb4: fmul s21, s16, s2
// 0x108deb8: fmul s16, s16, s0
// 0x108debc: fmul s0, s17, s0
// 0x108dec0: fmul s17, s17, s2
// 0x108dec4: fsub s1, s1, s4
// 0x108dec8: fadd s2, s20, s22
// 0x108decc: fadd s0, s0, s24
// 0x108ded0: fadd s3, s16, s3
// 0x108ded4: fsub s1, s1, s6
// 0x108ded8: fadd s2, s19, s2
// 0x108dedc: fadd s0, s21, s0
// 0x108dee0: fadd s4, s5, s3
// 0x108dee4: fsub s3, s1, s18
// 0x108dee8: fsub s2, s2, s23
// 0x108deec: fsub s1, s0, s7
// 0x108def0: fsub s0, s4, s17
// 0x108def4: mov x0, x20
// 0x108def8: mov x1, xzr
// 0x108defc: bl #0x1b9d774
// 0x108df00: ldr x20, [x19, #0x98]
// 0x108df04: cbz x20, #0x108dfac
// 0x108df08: mov x0, x20
// 0x108df0c: mov x1, xzr
// 0x108df10: bl #0x1b9d6f0
// 0x108df14: mov x0, xzr
// 0x108df18: bl #0x1b8b1c4
// 0x108df1c: adrp x8, #0x832000
// 0x108df20: ldr s9, [x8, #0x554]
// 0x108df24: mov x0, xzr
// 0x108df28: fmul s0, s0, s9
// 0x108df2c: fmul s1, s1, s9
// 0x108df30: fmul s2, s2, s9
// 0x108df34: bl #0x1b8b63c
// 0x108df38: ldr x0, [x19, #0x98]
// 0x108df3c: cbz x0, #0x108dfac
// 0x108df40: mov x1, xzr
// 0x108df44: mov v8.16b, v0.16b
// 0x108df48: bl #0x1b9d6f0
// 0x108df4c: mov x0, xzr
// 0x108df50: bl #0x1b8b1c4
// 0x108df54: fmul s0, s0, s9
// 0x108df58: fmul s1, s1, s9
// 0x108df5c: fmul s2, s2, s9
// 0x108df60: mov x0, xzr
// 0x108df64: bl #0x1b8b63c
// 0x108df68: adrp x8, #0x832000
// 0x108df6c: ldr s2, [x8, #0x3e4]
// 0x108df70: mov x0, xzr
// 0x108df74: fmul s0, s8, s2
// 0x108df78: fmul s1, s1, s2
// 0x108df7c: fmov s2, wzr
// 0x108df80: bl #0x1b8b12c
// 0x108df84: mov x0, x20
// 0x108df88: ldp x20, x19, [sp, #0x60]
// 0x108df8c: ldp x30, x21, [sp, #0x50]
// 0x108df90: ldp d9, d8, [sp, #0x40]
// 0x108df94: ldp d11, d10, [sp, #0x30]
// 0x108df98: ldp d13, d12, [sp, #0x20]
// 0x108df9c: ldp d15, d14, [sp, #0x10]
// 0x108dfa0: mov x1, xzr
// 0x108dfa4: add sp, sp, #0x70
// 0x108dfa8: b #0x1b9d774
// 0x108dfac: bl #0xf7db74
```

## `SmoothMouseLook.ClampAngle` — RVA `0xc8dfb0`

- Decompiled symbol: `SmoothMouseLook_ClampAngle`
- Metadata signature: `public static float ClampAngle(float angle, float min, float max) { }`
- Native interval: `136` bytes
- Result: `pseudocode`

```c
void SmoothMouseLook_ClampAngle(void)
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

## `SmoothMouseLook.ctor` — RVA `0xc8e038`

- Decompiled symbol: `SmoothMouseLook_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `44` bytes
- Result: `pseudocode`
- Heuristic layout hint: `SmoothMouseLook_Recovered` matched 3 offsets against `SmoothMouseLook` metadata (confidence 1.00).

```c
typedef struct SmoothMouseLook_Recovered {
    char padding_0[56];
    uint128_t sensitivity;
    unsigned long long minimumY;
    char padding_50[48];
    unsigned int smoothSpeed;
} SmoothMouseLook_Recovered;

long long SmoothMouseLook_ctor(struct_0 *ptr)
{
    long long v0;  // x0

    *((uint128_t *)&(&ptr->padding_0)[1]) = 0x43b40000c3b400004080000040800000;
    *((unsigned long long *)((char *)&ptr->field_38 + 8)) = 0x42aa0000c2aa0000;
    *((unsigned int *)&ptr->padding_50[40]) = 1051931443;
    v0 = MonoBehaviour__ctor();
    return MonoBehaviour__ctor();
}
```
