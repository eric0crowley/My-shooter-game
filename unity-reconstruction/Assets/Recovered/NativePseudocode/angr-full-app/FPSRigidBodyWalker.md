# Native pseudocode: FPSRigidBodyWalker

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `FPSRigidBodyWalker.OnDrawGizmos` — RVA `0xca1764`

- Decompiled symbol: `FPSRigidBodyWalker_OnDrawGizmos`
- Metadata signature: `private void OnDrawGizmos() { }`
- Native interval: `64` bytes
- Result: `pseudocode`

```c
void FPSRigidBodyWalker_OnDrawGizmos(unsigned long a0)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    Gizmos__set_color(0);
    Gizmos__DrawSphere();
    return;
}
```

## `FPSRigidBodyWalker.OnEnable` — RVA `0xca17a4`

- Decompiled symbol: `FPSRigidBodyWalker_OnEnable`
- Metadata signature: `private void OnEnable() { }`
- Native interval: `284` bytes
- Result: `pseudocode`

```c
extern long long g_1efcf58;
extern long long g_1efd080;
extern long long g_1efd0a0;
extern long long g_1efeb88;
extern char g_1fab4b7;

void FPSRigidBodyWalker_OnEnable(long long *ptr)
{
    unsigned long long v4;  // x30
    unsigned long long v5;  // x21
    unsigned long long v6;  // x20
    unsigned long long v7;  // x19
    long long v8;  // x0
    long long p[73];  // x20
    long long v10;  // x0
    long long v11;  // x1
    long long v12;  // x1
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x18]
    unsigned long long v2;  // [bp-0x10]
    unsigned long long v3;  // [bp-0x8]

    v0 = v4;
    v1 = v5;
    v2 = v6;
    v3 = v7;
    if (!(g_1fab4b7 & 1))
    {
        sub_f7d92c(&g_1efcf58);
        sub_f7d92c(&g_1efd080);
        sub_f7d92c(&g_1efd0a0);
        sub_f7d92c(&g_1efeb88);
        g_1fab4b7 = 1;
    }
    v8 = sub_1231bc8(ptr, g_1efd080);
    ptr[19] = v8;
    p = ptr + 19;
    sub_f7d8d0(p, v8);
    v10 = p[0];
    if (v10)
    {
        Rigidbody__set_freezeRotation(v10, 1, 0);
        v10 = p[0];
        if (v10)
        {
            Rigidbody__set_useGravity(v10, 1, 0);
            v11 = sub_1231bc8(ptr, g_1efcf58);
            ptr[71] = v11;
            sub_f7d8d0(ptr + 71, v11);
            v10 = ptr[44];
            if (v10)
            {
                v12 = sub_1249224(v10, g_1efeb88);
                ptr[45] = v12;
                sub_f7d8d0(ptr + 45, v12);
                ptr[72] = sub_1231bc8(ptr, g_1efd0a0);
                sub_f7d8d0();
                return;
            }
        }
    }
    sub_f7db74(v10);
}
```

## `FPSRigidBodyWalker.Start` — RVA `0xca18c0`

- Decompiled symbol: `FPSRigidBodyWalker_Start`
- Metadata signature: `private void Start() { }`
- Native interval: `848` bytes
- Result: `pseudocode`
- Heuristic layout hint: `FPSRigidBodyWalker_Recovered` matched 27 offsets against `FPSRigidBodyWalker` metadata (confidence 0.90).

```c
typedef struct FPSRigidBodyWalker_Recovered {
    char padding_0[32];
    long long SmoothMouseLookComponent;
    long long FPSPlayerComponent;
    long long InputComponent;
    long long FootstepsComponent;
    char padding_40[24];
    long long CameraObj;
    char myTransform;
    char padding_61[7];
    unsigned long long upVec;
    unsigned int field_70;
    unsigned int myUpVec;
    unsigned int field_78;
    unsigned int field_7c;
    long long mainCamTransform;
    long long CameraAnimatorComponent;
    struct struct_1 *CameraControlComponent;
    char padding_98[72];
    unsigned int jumpSpeed;
    char padding_e4[4];
    unsigned int moveSpeedMult;
    char padding_ec[60];
    unsigned int sprintMode;
    unsigned int sprintDelay;
    char padding_130[12];
    unsigned int staminaForSprint;
    unsigned int staminaForSprintAmt;
    char padding_144[36];
    long long leanCol;
    char padding_170[84];
    unsigned int cameraSmoothSpeedAmt;
    char padding_1c8[112];
    long long capsule;
    char padding_240[176];
    unsigned int lowpos;
    char padding_2f4[20];
    long long playerPhysicMaterial;
    char padding_310[184];
    unsigned int standingCapsuleheight;
    char padding_3cc[4];
    unsigned int capsuleCastHeight;
    char padding_3d4[4];
    unsigned int rayCastHeight;
    unsigned int playerHeightMod;
    unsigned int capsuleCheckRadius;
} FPSRigidBodyWalker_Recovered;

typedef struct struct_0 {
    char padding_0[276];
    unsigned int field_114;
} struct_0;

typedef struct struct_1 {
    char padding_0[276];
    unsigned int field_114;
} struct_1;

typedef struct struct_3 {
    char padding_0[24];
    unsigned long long field_18;
    unsigned int field_20;
} struct_3;

typedef struct struct_4 {
    char padding_0[184];
    struct struct_3 *field_b8;
} struct_4;

extern struct_4 *g_1ef22e8;
extern long long g_1efcf08;
extern long long g_1efcf38;
extern long long g_1efcf98;
extern long long g_1efcfd8;
extern long long g_1efebc8;
extern long long g_1efecd8;
extern char g_1fab32c;
extern char g_1fab4b8;
extern unsigned int g_852284[4];

long long FPSRigidBodyWalker_Start(struct_2 *ptr)
{
    unsigned long v0;  // x0
    long long v1;  // x1
    struct_0 *v10;  // x1
    struct_2 *p;  // x0
    long long v12;  // x0
    struct_2 *addr;  // x20
    struct_2 *idx11;  // x20
    unsigned long v15;  // x1
    struct_2 *ptr3;  // x0
    long long v17;  // x1
    struct_2 *ptr4;  // x0
    unsigned long long v19;  // d0
    struct_2 *ptr5;  // x0
    unsigned int v20;  // s1
    unsigned int v21;  // s0
    unsigned int v22;  // s2
    unsigned int v23;  // s0
    unsigned int v24;  // s0
    unsigned int v25;  // s0
    unsigned int v26;  // s0
    long long v27;  // x1
    unsigned long v28;  // x0
    unsigned long idx4;  // x8
    long long v3;  // x1
    struct_2 *ptr6;  // x0
    long long v5;  // x0
    struct_2 *ptr7;  // x20
    struct_2 *ptr9;  // x20
    long long v8;  // x1
    struct_2 *ptr8;  // x0

    if (!(g_1fab4b8 & 1))
    {
        sub_f7d92c(&g_1efcf08);
        sub_f7d92c(&g_1efcf38);
        sub_f7d92c(&g_1efcf98);
        sub_f7d92c(&g_1efcfd8);
        sub_f7d92c(&g_1efebc8);
        sub_f7d92c(&g_1efecd8);
        g_1fab4b8 = 1;
    }
    v0 = ptr->field_58;
    if (v0)
    {
        v1 = sub_1249224(v0, g_1efecd8);
        ptr5 = ptr;
        ptr5->field_20 = v1;
        sub_f7d8d0(&ptr5->field_20, v1);
        v3 = sub_1231bc8(ptr, g_1efcf98);
        ptr6 = ptr;
        ptr6->field_28 = v3;
        sub_f7d8d0(&ptr6->field_28, v3);
        v5 = sub_1231bc8(ptr, g_1efcfd8);
        ptr7 = ptr;
        ptr7->field_30 = v5;
        ptr9 = &ptr7->field_30;
        sub_f7d8d0(ptr9, v5);
        v0 = ptr9->field_28;
        if (v0)
        {
            v8 = sub_1249224(v0, g_1efebc8);
            ptr8 = ptr;
            ptr8->field_38 = v8;
            sub_f7d8d0(&ptr8->field_38, v8);
            v0 = Camera__get_main(0);
            if (v0)
            {
                v0 = Component__get_transform();
                if (v0)
                {
                    v10 = sub_1231bc8();
                    p = ptr;
                    p->field_90 = v10;
                    sub_f7d8d0(&p->field_90, v10);
                    v0 = Camera__get_main(0);
                    if (v0)
                    {
                        v12 = sub_1231bc8();
                        addr = ptr;
                        addr->field_88 = v12;
                        idx11 = &addr->field_88;
                        v0 = sub_f7d8d0(idx11, v12);
                        if (*((long long *)&idx11->padding_0[8]))
                        {
                            ptr->field_1c4 = *((int *)(*((long long *)&idx11->padding_0[8]) + 276));
                            v15 = Component__get_transform(ptr, 0);
                            ptr3 = ptr;
                            *((unsigned long *)&ptr3->field_60) = v15;
                            sub_f7d8d0(&ptr3->field_60, v15);
                            v0 = Camera__get_main(0);
                            if (v0)
                            {
                                v17 = Component__get_transform();
                                ptr4 = ptr;
                                ptr4->field_80 = v17;
                                sub_f7d8d0(&ptr4->field_80, v17);
                                if (!g_1fab32c)
                                {
                                    sub_f7d92c(&g_1ef22e8);
                                    g_1fab32c = 1;
                                }
                                v0 = *((long long *)&ptr->field_60);
                                v19 = g_1ef22e8->field_b8->field_18;
                                v20 = g_1ef22e8->field_b8->field_20;
                                ptr->field_68 = v19;
                                ptr->field_70 = v20;
                                if (v0)
                                {
                                    Transform__get_up(v0, 0);
                                    ptr->field_74 = v19;
                                    ptr->field_78 = v20;
                                    v21 = ptr->field_13c;
                                    v0 = ptr->field_238;
                                    ptr->field_7c = v22;
                                    ptr->field_140 = v21;
                                    ptr->field_e8 = 0x3f800000;
                                    if (v0)
                                    {
                                        CapsuleCollider__set_height(v0, 0);
                                        v0 = ptr->field_238;
                                        v23 = ptr->field_3c8 + 3222232105;
                                        ptr->field_3dc = v23;
                                        if (v0)
                                        {
                                            CapsuleCollider__get_radius(v0, 0);
                                            v0 = ptr->field_168;
                                            v24 = v23 * 1063675494;
                                            ptr->field_3e0 = v24;
                                            if (v0)
                                            {
                                                CapsuleCollider__set_radius(v0, 0);
                                                v0 = ptr->field_238;
                                                if (v0)
                                                {
                                                    CapsuleCollider__get_height(v0, 0);
                                                    v0 = ptr->field_238;
                                                    v25 = v24 * 1055286886;
                                                    ptr->field_3d0 = v25;
                                                    if (v0)
                                                    {
                                                        CapsuleCollider__get_height(v0, 0);
                                                        v0 = ptr->field_238;
                                                        v26 = v25 * 1067869798;
                                                        ptr->field_3d8 = v26;
                                                        if (v0)
                                                        {
                                                            CapsuleCollider__get_height(v0, 0);
                                                            v0 = *((long long *)&ptr->field_60);
                                                            ptr->field_e0 = ptr->field_e0 / (0x3f800000 - ptr->field_3dc / v26);
                                                            if (v0)
                                                            {
                                                                Transform__get_position(v0, 0);
                                                                v0 = ptr->field_238;
                                                                ptr->field_2f0 = 0x3f800000;
                                                                if (v0)
                                                                {
                                                                    v27 = Collider__get_material(v0, 0);
                                                                    ptr->field_308 = v27;
                                                                    v28 = sub_f7d8d0(&ptr->field_308, v27);
                                                                    idx4 = ptr->field_128;
                                                                    if (2 < (unsigned int)idx4)
                                                                        return v28;
                                                                    ptr->field_12c = g_852284[idx4];
                                                                    return v28;
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
    sub_f7db74(v0);
}
```

## `FPSRigidBodyWalker.Update` — RVA `0xca1c10`

- Decompiled symbol: `FPSRigidBodyWalker_Update`
- Metadata signature: `private void Update() { }`
- Native interval: `3468` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: Decompiler produced no C-like text

```c
// 0x10a1c10: sub sp, sp, #0xe0
// 0x10a1c14: stp d15, d14, [sp, #0x70]
// 0x10a1c18: stp d13, d12, [sp, #0x80]
// 0x10a1c1c: stp d11, d10, [sp, #0x90]
// 0x10a1c20: stp d9, d8, [sp, #0xa0]
// 0x10a1c24: str x30, [sp, #0xb0]
// 0x10a1c28: stp x22, x21, [sp, #0xc0]
// 0x10a1c2c: stp x20, x19, [sp, #0xd0]
// 0x10a1c30: adrp x20, #0x1fab000
// 0x10a1c34: ldrb w8, [x20, #0x4b9]
// 0x10a1c38: mov x19, x0
// 0x10a1c3c: tbnz w8, #0, #0x10a1c78
// 0x10a1c40: adrp x0, #0x1e8c000
// 0x10a1c44: ldr x0, [x0, #0xd8]
// 0x10a1c48: bl #0xf7d92c
// 0x10a1c4c: adrp x0, #0x1e8d000
// 0x10a1c50: ldr x0, [x0, #0x4a8]
// 0x10a1c54: bl #0xf7d92c
// 0x10a1c58: adrp x0, #0x1e8e000
// 0x10a1c5c: ldr x0, [x0, #0x380]
// 0x10a1c60: bl #0xf7d92c
// 0x10a1c64: adrp x0, #0x1e8e000
// 0x10a1c68: ldr x0, [x0, #0x388]
// 0x10a1c6c: bl #0xf7d92c
// 0x10a1c70: mov w8, #1
// 0x10a1c74: strb w8, [x20, #0x4b9]
// 0x10a1c78: ldr x8, [x19, #0x28]
// 0x10a1c7c: cbz x8, #0x10a2998
// 0x10a1c80: ldr s0, [x8, #0x20c]
// 0x10a1c84: fcmp s0, #0.0
// 0x10a1c88: b.hi #0x10a1cc0
// 0x10a1c8c: mov x0, xzr
// 0x10a1c90: bl #0x1b89b60
// 0x10a1c94: fmov s8, wzr
// 0x10a1c98: fmul s0, s0, s8
// 0x10a1c9c: mov x0, xzr
// 0x10a1ca0: str s0, [x19, #0x120]
// 0x10a1ca4: bl #0x1b89b60
// 0x10a1ca8: fmul s0, s0, s8
// 0x10a1cac: mov x0, xzr
// 0x10a1cb0: str s0, [x19, #0xd8]
// 0x10a1cb4: bl #0x1b89b60
// 0x10a1cb8: fmul s0, s0, s8
// 0x10a1cbc: str s0, [x19, #0xd4]
// 0x10a1cc0: ldr x0, [x19, #0x238]
// 0x10a1cc4: cbz x0, #0x10a2998
// 0x10a1cc8: mov x1, xzr
// 0x10a1ccc: bl #0x1bcfd68
// 0x10a1cd0: adrp x8, #0x832000
// 0x10a1cd4: ldr s1, [x8, #0x3bc]
// 0x10a1cd8: ldr x0, [x19, #0x60]
// 0x10a1cdc: fmul s0, s0, s1
// 0x10a1ce0: str s1, [sp, #0xbc]
// 0x10a1ce4: str s0, [x19, #0x3e0]
// 0x10a1ce8: cbz x0, #0x10a2998
// 0x10a1cec: mov x1, xzr
// 0x10a1cf0: bl #0x1b9d508
// 0x10a1cf4: ldr x0, [x19, #0x60]
// 0x10a1cf8: cbz x0, #0x10a2998
// 0x10a1cfc: ldp s11, s12, [x19, #0x68]
// 0x10a1d00: ldr s13, [x19, #0x70]
// 0x10a1d04: mov x1, xzr
// 0x10a1d08: mov v8.16b, v0.16b
// 0x10a1d0c: mov v9.16b, v1.16b
// 0x10a1d10: mov v10.16b, v2.16b
// 0x10a1d14: bl #0x1b9d508
// 0x10a1d18: ldr x0, [x19, #0x238]
// 0x10a1d1c: cbz x0, #0x10a2998
// 0x10a1d20: add x8, sp, #0x58
// 0x10a1d24: mov x1, xzr
// 0x10a1d28: stp s1, s13, [sp, #4]
// 0x10a1d2c: stp s12, s11, [sp, #0xc]
// 0x10a1d30: stp s10, s9, [sp, #0x14]
// 0x10a1d34: str s8, [sp, #0x1c]
// 0x10a1d38: bl #0x1bcf9fc
// 0x10a1d3c: ldr x0, [x19, #0x60]
// 0x10a1d40: cbz x0, #0x10a2998
// 0x10a1d44: ldr s0, [x19, #0x68]
// 0x10a1d48: ldr s1, [x19, #0x6c]
// 0x10a1d4c: ldr s10, [sp, #0x5c]
// 0x10a1d50: ldr s14, [sp, #0x68]
// 0x10a1d54: str s0, [sp, #0xb8]
// 0x10a1d58: ldr s0, [x19, #0x70]
// 0x10a1d5c: ldr s8, [x19, #0x3e0]
// 0x10a1d60: ldr s9, [x19, #0x3c8]
// 0x10a1d64: mov x1, xzr
// 0x10a1d68: stp s0, s1, [sp, #0x38]
// 0x10a1d6c: ldr s0, [x19, #0x3cc]
// 0x10a1d70: str s0, [sp]
// 0x10a1d74: bl #0x1b9d508
// 0x10a1d78: ldr x0, [x19, #0x238]
// 0x10a1d7c: str d0, [sp, #0x40]
// 0x10a1d80: str d1, [sp, #0x20]
// 0x10a1d84: cbz x0, #0x10a2998
// 0x10a1d88: ldur d15, [x19, #0x74]
// 0x10a1d8c: ldr s13, [x19, #0x7c]
// 0x10a1d90: add x8, sp, #0x58
// 0x10a1d94: mov x1, xzr
// 0x10a1d98: mov v12.16b, v2.16b
// 0x10a1d9c: bl #0x1bcf9fc
// 0x10a1da0: ldr x0, [x19, #0x60]
// 0x10a1da4: cbz x0, #0x10a2998
// 0x10a1da8: ldr s0, [sp, #0x5c]
// 0x10a1dac: ldr s1, [sp, #0x68]
// 0x10a1db0: mov x1, xzr
// 0x10a1db4: fsub s11, s0, s1
// 0x10a1db8: bl #0x1b9d508
// 0x10a1dbc: fsub s0, s11, s1
// 0x10a1dc0: ldr q5, [sp, #0x40]
// 0x10a1dc4: ldr q1, [sp, #0x20]
// 0x10a1dc8: ldr s2, [x19, #0x7c]
// 0x10a1dcc: ldr s4, [x19, #0x3ac]
// 0x10a1dd0: ldr x0, [x19, #0x58]
// 0x10a1dd4: mov v5.s[1], v1.s[0]
// 0x10a1dd8: ldur d1, [x19, #0x74]
// 0x10a1ddc: fmul v3.2s, v15.2s, v0.s[0]
// 0x10a1de0: fmul s0, s13, s0
// 0x10a1de4: fsub v3.2s, v5.2s, v3.2s
// 0x10a1de8: fsub s0, s12, s0
// 0x10a1dec: fmul v1.2s, v1.2s, v4.s[0]
// 0x10a1df0: fmul s2, s2, s4
// 0x10a1df4: fadd v1.2s, v3.2s, v1.2s
// 0x10a1df8: fadd s0, s0, s2
// 0x10a1dfc: str d1, [x19, #0x3b0]
// 0x10a1e00: str s0, [x19, #0x3b8]
// 0x10a1e04: cbz x0, #0x10a2998
// 0x10a1e08: mov x1, xzr
// 0x10a1e0c: bl #0x1b94c14
// 0x10a1e10: cbz x0, #0x10a2998
// 0x10a1e14: mov x1, xzr
// 0x10a1e18: bl #0x1b9d7c8
// 0x10a1e1c: ldr x0, [x19, #0x60]
// 0x10a1e20: cbz x0, #0x10a2998
// 0x10a1e24: fmov s0, wzr
// 0x10a1e28: fmov s2, wzr
// 0x10a1e2c: mov x1, xzr
// 0x10a1e30: bl #0x1b9d848
// 0x10a1e34: ldr x0, [x19, #0x58]
// 0x10a1e38: cbz x0, #0x10a2998
// 0x10a1e3c: mov x1, xzr
// 0x10a1e40: bl #0x1b94c14
// 0x10a1e44: cbz x0, #0x10a2998
// 0x10a1e48: mov x1, xzr
// 0x10a1e4c: bl #0x1b9d6c8
// 0x10a1e50: ldr x0, [x19, #0x60]
// 0x10a1e54: cbz x0, #0x10a2998
// 0x10a1e58: adrp x8, #0x832000
// 0x10a1e5c: adrp x21, #0x1e8d000
// 0x10a1e60: fsub s0, s10, s14
// 0x10a1e64: ldr s14, [x8, #0x4f8]
// 0x10a1e68: ldr x21, [x21, #0x4a8]
// 0x10a1e6c: ldp s2, s5, [sp, #4]
// 0x10a1e70: fadd s0, s0, s8
// 0x10a1e74: fadd s12, s8, s8
// 0x10a1e78: fadd s3, s9, s14
// 0x10a1e7c: fadd s2, s2, s14
// 0x10a1e80: fsub s0, s2, s0
// 0x10a1e84: fsub s2, s3, s12
// 0x10a1e88: ldp s4, s3, [sp, #0xc]
// 0x10a1e8c: ldp s7, s6, [sp, #0x38]
// 0x10a1e90: mov x1, xzr
// 0x10a1e94: fmul s3, s3, s0
// 0x10a1e98: fmul s4, s4, s0
// 0x10a1e9c: fmul s0, s5, s0
// 0x10a1ea0: ldr s5, [sp, #0xb8]
// 0x10a1ea4: fmul s6, s6, s2
// 0x10a1ea8: fmul s5, s5, s2
// 0x10a1eac: fmul s2, s7, s2
// 0x10a1eb0: ldr s7, [sp, #0x1c]
// 0x10a1eb4: fsub s8, s7, s3
// 0x10a1eb8: ldr s3, [sp, #0x18]
// 0x10a1ebc: fadd s15, s8, s5
// 0x10a1ec0: fsub s9, s3, s4
// 0x10a1ec4: ldr s3, [sp, #0x14]
// 0x10a1ec8: fadd s13, s9, s6
// 0x10a1ecc: fsub s10, s3, s0
// 0x10a1ed0: fadd s0, s10, s2
// 0x10a1ed4: str s0, [sp, #0x40]
// 0x10a1ed8: fmov s0, wzr
// 0x10a1edc: fmov s2, wzr
// 0x10a1ee0: bl #0x1b9d748
// 0x10a1ee4: ldrb w8, [x19, #0x14b]
// 0x10a1ee8: cbz w8, #0x10a1ff0
// 0x10a1eec: ldr x8, [x19, #0x30]
// 0x10a1ef0: cbz x8, #0x10a2998
// 0x10a1ef4: ldrb w8, [x8, #0x8f]
// 0x10a1ef8: cbz w8, #0x10a1f0c
// 0x10a1efc: ldrb w8, [x19, #0x258]
// 0x10a1f00: cbnz w8, #0x10a1f0c
// 0x10a1f04: ldrb w8, [x19, #0x295]
// 0x10a1f08: cbz w8, #0x10a250c
// 0x10a1f0c: ldrb w8, [x19, #0x2b1]
// 0x10a1f10: strb wzr, [x19, #0x2d2]
// 0x10a1f14: cbnz w8, #0x10a1f28
// 0x10a1f18: ldrb w8, [x19, #0x295]
// 0x10a1f1c: cbnz w8, #0x10a1f28
// 0x10a1f20: ldrb w8, [x19, #0x258]
// 0x10a1f24: cbz w8, #0x10a1ff0
// 0x10a1f28: ldr x0, [x19, #0x60]
// 0x10a1f2c: str s10, [sp, #0xb8]
// 0x10a1f30: cbz x0, #0x10a2998
// 0x10a1f34: mov x1, xzr
// 0x10a1f38: mov v10.16b, v9.16b
// 0x10a1f3c: mov v9.16b, v8.16b
// 0x10a1f40: mov v8.16b, v13.16b
// 0x10a1f44: mov v13.16b, v15.16b
// 0x10a1f48: bl #0x1b9d508
// 0x10a1f4c: ldp s3, s4, [x19, #0x74]
// 0x10a1f50: ldr s5, [x19, #0x7c]
// 0x10a1f54: ldr s12, [x19, #0x3e0]
// 0x10a1f58: fmov s6, #0.75000000
// 0x10a1f5c: fmul s3, s3, s6
// 0x10a1f60: fmul s4, s4, s6
// 0x10a1f64: fmul s5, s5, s6
// 0x10a1f68: add x0, x19, #0x304
// 0x10a1f6c: mov x1, xzr
// 0x10a1f70: fadd s14, s0, s3
// 0x10a1f74: fadd s15, s1, s4
// 0x10a1f78: fadd s11, s2, s5
// 0x10a1f7c: bl #0x1b95168
// 0x10a1f80: ldr x8, [x21]
// 0x10a1f84: mov w20, w0
// 0x10a1f88: ldr w9, [x8, #0xe0]
// 0x10a1f8c: cbnz w9, #0x10a1f98
// 0x10a1f90: mov x0, x8
// 0x10a1f94: bl #0xf7da5c
// 0x10a1f98: ldr s0, [sp, #0xbc]
// 0x10a1f9c: ldr s5, [sp, #0x40]
// 0x10a1fa0: mov w1, #1
// 0x10a1fa4: mov v1.16b, v15.16b
// 0x10a1fa8: fmul s6, s12, s0
// 0x10a1fac: mov v0.16b, v14.16b
// 0x10a1fb0: mov v2.16b, v11.16b
// 0x10a1fb4: mov v3.16b, v13.16b
// 0x10a1fb8: mov v4.16b, v8.16b
// 0x10a1fbc: mov w0, w20
// 0x10a1fc0: mov x2, xzr
// 0x10a1fc4: mov v15.16b, v13.16b
// 0x10a1fc8: mov v13.16b, v8.16b
// 0x10a1fcc: bl #0x1bcdfcc
// 0x10a1fd0: mov v8.16b, v9.16b
// 0x10a1fd4: mov v9.16b, v10.16b
// 0x10a1fd8: ldr s10, [sp, #0xb8]
// 0x10a1fdc: tbnz w0, #0, #0x10a1ff0
// 0x10a1fe0: mov w8, #0xcccd
// 0x10a1fe4: movk w8, #0x3e4c, lsl #16
// 0x10a1fe8: str w8, [x19, #0x2ec]
// 0x10a1fec: strb wzr, [x19, #0x2d0]
// 0x10a1ff0: ldrb w8, [x19, #0x149]
// 0x10a1ff4: cbz w8, #0x10a21d8
// 0x10a1ff8: ldr x8, [x19, #0x30]
// 0x10a1ffc: cbz x8, #0x10a2998
// 0x10a2000: ldrb w8, [x8, #0x90]
// 0x10a2004: cbz w8, #0x10a2018
// 0x10a2008: ldrb w8, [x19, #0x258]
// 0x10a200c: cbnz w8, #0x10a2018
// 0x10a2010: ldrb w8, [x19, #0x295]
// 0x10a2014: cbz w8, #0x10a25f4
// 0x10a2018: ldrb w8, [x19, #0x2b1]
// 0x10a201c: strb wzr, [x19, #0x2de]
// 0x10a2020: cbnz w8, #0x10a2034
// 0x10a2024: ldrb w8, [x19, #0x295]
// 0x10a2028: cbnz w8, #0x10a2034
// 0x10a202c: ldrb w8, [x19, #0x258]
// 0x10a2030: cbz w8, #0x10a20a0
// 0x10a2034: ldr s11, [x19, #0x3e0]
// 0x10a2038: add x0, x19, #0x304
// 0x10a203c: mov x1, xzr
// 0x10a2040: bl #0x1b95168
// 0x10a2044: ldr x8, [x21]
// 0x10a2048: mov w20, w0
// 0x10a204c: ldr w9, [x8, #0xe0]
// 0x10a2050: cbnz w9, #0x10a205c
// 0x10a2054: mov x0, x8
// 0x10a2058: bl #0xf7da5c
// 0x10a205c: ldr s0, [sp, #0xbc]
// 0x10a2060: ldr s5, [sp, #0x40]
// 0x10a2064: mov w1, #1
// 0x10a2068: mov v1.16b, v9.16b
// 0x10a206c: fmul s6, s11, s0
// 0x10a2070: mov v0.16b, v8.16b
// 0x10a2074: mov v2.16b, v10.16b
// 0x10a2078: mov v3.16b, v15.16b
// 0x10a207c: mov v4.16b, v13.16b
// 0x10a2080: mov w0, w20
// 0x10a2084: mov x2, xzr
// 0x10a2088: bl #0x1bcdfcc
// 0x10a208c: tbnz w0, #0, #0x10a20a0
// 0x10a2090: mov w8, #0xcccd
// 0x10a2094: movk w8, #0x3e4c, lsl #16
// 0x10a2098: str w8, [x19, #0x2ec]
// 0x10a209c: strb wzr, [x19, #0x2dc]
// 0x10a20a0: ldr x8, [x19, #0x30]
// 0x10a20a4: cbz x8, #0x10a2998
// 0x10a20a8: ldrb w8, [x8, #0x8d]
// 0x10a20ac: cbz w8, #0x10a2154
// 0x10a20b0: ldrb w8, [x19, #0x2d0]
// 0x10a20b4: cbnz w8, #0x10a20c0
// 0x10a20b8: ldrb w8, [x19, #0x2dc]
// 0x10a20bc: cbz w8, #0x10a2154
// 0x10a20c0: ldr s11, [x19, #0x3e0]
// 0x10a20c4: add x0, x19, #0x304
// 0x10a20c8: mov x1, xzr
// 0x10a20cc: bl #0x1b95168
// 0x10a20d0: ldr x8, [x21]
// 0x10a20d4: mov w20, w0
// 0x10a20d8: ldr w9, [x8, #0xe0]
// 0x10a20dc: cbnz w9, #0x10a20e8
// 0x10a20e0: mov x0, x8
// 0x10a20e4: bl #0xf7da5c
// 0x10a20e8: ldr s0, [sp, #0xbc]
// 0x10a20ec: ldr s5, [sp, #0x40]
// 0x10a20f0: mov w1, #1
// 0x10a20f4: mov v1.16b, v9.16b
// 0x10a20f8: fmul s6, s11, s0
// 0x10a20fc: mov v0.16b, v8.16b
// 0x10a2100: mov v2.16b, v10.16b
// 0x10a2104: mov v3.16b, v15.16b
// 0x10a2108: mov v4.16b, v13.16b
// 0x10a210c: mov w0, w20
// 0x10a2110: mov x2, xzr
// 0x10a2114: bl #0x1bcdfcc
// 0x10a2118: tbnz w0, #0, #0x10a2154
// 0x10a211c: mov w8, #0xcccd
// 0x10a2120: movk w8, #0x3e4c, lsl #16
// 0x10a2124: mov x0, xzr
// 0x10a2128: strb wzr, [x19, #0x2d0]
// 0x10a212c: str w8, [x19, #0x2ec]
// 0x10a2130: strb wzr, [x19, #0x2dc]
// 0x10a2134: bl #0x1b9ad30
// 0x10a2138: mov x0, xzr
// 0x10a213c: str s0, [x19, #0x2e0]
// 0x10a2140: bl #0x1b9ad30
// 0x10a2144: mov x0, xzr
// 0x10a2148: str s0, [x19, #0x2d4]
// 0x10a214c: bl #0x1b9ad30
// 0x10a2150: str s0, [x19, #0x2ac]
// 0x10a2154: ldr x0, [x19, #0x80]
// 0x10a2158: cbz x0, #0x10a2998
// 0x10a215c: mov x1, xzr
// 0x10a2160: bl #0x1b9d508
// 0x10a2164: ldr x0, [x19, #0x60]
// 0x10a2168: cbz x0, #0x10a2998
// 0x10a216c: mov x1, xzr
// 0x10a2170: mov v8.16b, v1.16b
// 0x10a2174: bl #0x1b9d508
// 0x10a2178: adrp x8, #0x832000
// 0x10a217c: ldr s0, [x19, #0x3bc]
// 0x10a2180: ldr s2, [x8, #0x400]
// 0x10a2184: fsub s1, s8, s1
// 0x10a2188: fmul s0, s0, s2
// 0x10a218c: fcmp s1, s0
// 0x10a2190: b.le #0x10a21b8
// 0x10a2194: ldrb w8, [x19, #0x2dd]
// 0x10a2198: mov w9, #0xcccd
// 0x10a219c: movk w9, #0x3dcc, lsl #16
// 0x10a21a0: str w9, [x19, #0x2ec]
// 0x10a21a4: cbnz w8, #0x10a21b8
// 0x10a21a8: ldrb w8, [x19, #0x2dc]
// 0x10a21ac: cbnz w8, #0x10a21b8
// 0x10a21b0: mov w8, #1
// 0x10a21b4: strb w8, [x19, #0x2dd]
// 0x10a21b8: ldrb w8, [x19, #0x2e8]
// 0x10a21bc: cbz w8, #0x10a21d0
// 0x10a21c0: ldrb w8, [x19, #0x2dc]
// 0x10a21c4: cbz w8, #0x10a21d0
// 0x10a21c8: mov w8, #1
// 0x10a21cc: b #0x10a21d4
// 0x10a21d0: mov w8, wzr
// 0x10a21d4: strb w8, [x19, #0x2df]
// 0x10a21d8: ldr x0, [x19, #0x80]
// 0x10a21dc: cbz x0, #0x10a2998
// 0x10a21e0: mov x1, xzr
// 0x10a21e4: bl #0x1b9d508
// 0x10a21e8: ldr x0, [x19, #0x60]
// 0x10a21ec: cbz x0, #0x10a2998
// 0x10a21f0: mov x1, xzr
// 0x10a21f4: mov v8.16b, v1.16b
// 0x10a21f8: bl #0x1b9d508
// 0x10a21fc: ldr s0, [x19, #0x3c0]
// 0x10a2200: fmov s2, #0.50000000
// 0x10a2204: fsub s1, s8, s1
// 0x10a2208: fmul s0, s0, s2
// 0x10a220c: fcmp s1, s0
// 0x10a2210: b.le #0x10a2230
// 0x10a2214: ldrb w8, [x19, #0x2d1]
// 0x10a2218: cbnz w8, #0x10a2230
// 0x10a221c: mov w8, #0xcccd
// 0x10a2220: movk w8, #0x3dcc, lsl #16
// 0x10a2224: mov w9, #1
// 0x10a2228: str w8, [x19, #0x2ec]
// 0x10a222c: strb w9, [x19, #0x2d1]
// 0x10a2230: ldr s1, [x19, #0xc4]
// 0x10a2234: adrp x8, #0x832000
// 0x10a2238: ldr s0, [x8, #0x2f8]
// 0x10a223c: fabs s1, s1
// 0x10a2240: fcmp s1, s0
// 0x10a2244: b.gt #0x10a2258
// 0x10a2248: ldr s1, [x19, #0xc0]
// 0x10a224c: fabs s1, s1
// 0x10a2250: fcmp s1, s0
// 0x10a2254: b.le #0x10a2304
// 0x10a2258: ldrb w8, [x19, #0x220]
// 0x10a225c: mov w9, #1
// 0x10a2260: strb w9, [x19, #0x2e8]
// 0x10a2264: cbz w8, #0x10a23a4
// 0x10a2268: ldrb w8, [x19, #0x221]
// 0x10a226c: cbz w8, #0x10a23a4
// 0x10a2270: ldr x0, [x19, #0x238]
// 0x10a2274: cbz x0, #0x10a2998
// 0x10a2278: mov x1, xzr
// 0x10a227c: bl #0x1bcfaa8
// 0x10a2280: cbz x0, #0x10a2998
// 0x10a2284: mov w1, #2
// 0x10a2288: mov x2, xzr
// 0x10a228c: bl #0x1bcec14
// 0x10a2290: ldr x0, [x19, #0x238]
// 0x10a2294: cbz x0, #0x10a2998
// 0x10a2298: mov x1, xzr
// 0x10a229c: bl #0x1bcfaa8
// 0x10a22a0: cbz x0, #0x10a2998
// 0x10a22a4: adrp x8, #0x832000
// 0x10a22a8: ldr s8, [x8, #0x4e0]
// 0x10a22ac: mov x1, xzr
// 0x10a22b0: mov v0.16b, v8.16b
// 0x10a22b4: bl #0x1bceb7c
// 0x10a22b8: ldr x0, [x19, #0x238]
// 0x10a22bc: cbz x0, #0x10a2998
// 0x10a22c0: mov x1, xzr
// 0x10a22c4: bl #0x1bcfaa8
// 0x10a22c8: cbz x0, #0x10a2998
// 0x10a22cc: mov v0.16b, v8.16b
// 0x10a22d0: mov x1, xzr
// 0x10a22d4: bl #0x1bcebc8
// 0x10a22d8: ldr x20, [x19, #0x238]
// 0x10a22dc: cbz x20, #0x10a2998
// 0x10a22e0: mov x0, x20
// 0x10a22e4: mov x1, xzr
// 0x10a22e8: bl #0x1bcfaa8
// 0x10a22ec: mov x1, x0
// 0x10a22f0: mov x0, x20
// 0x10a22f4: mov x2, xzr
// 0x10a22f8: bl #0x1bcfae4
// 0x10a22fc: strb wzr, [x19, #0x221]
// 0x10a2300: b #0x10a23a4
// 0x10a2304: ldrb w8, [x19, #0x220]
// 0x10a2308: strb wzr, [x19, #0x2e8]
// 0x10a230c: cbz w8, #0x10a23a4
// 0x10a2310: ldrb w8, [x19, #0x221]
// 0x10a2314: cbnz w8, #0x10a23a4
// 0x10a2318: ldr x0, [x19, #0x238]
// 0x10a231c: cbz x0, #0x10a2998
// 0x10a2320: mov x1, xzr
// 0x10a2324: bl #0x1bcfaa8
// 0x10a2328: cbz x0, #0x10a2998
// 0x10a232c: mov w1, #3
// 0x10a2330: mov x2, xzr
// 0x10a2334: bl #0x1bcec14
// 0x10a2338: ldr x0, [x19, #0x238]
// 0x10a233c: cbz x0, #0x10a2998
// 0x10a2340: mov x1, xzr
// 0x10a2344: bl #0x1bcfaa8
// 0x10a2348: cbz x0, #0x10a2998
// 0x10a234c: fmov s0, #1.00000000
// 0x10a2350: mov x1, xzr
// 0x10a2354: bl #0x1bceb7c
// 0x10a2358: ldr x0, [x19, #0x238]
// 0x10a235c: cbz x0, #0x10a2998
// 0x10a2360: mov x1, xzr
// 0x10a2364: bl #0x1bcfaa8
// 0x10a2368: cbz x0, #0x10a2998
// 0x10a236c: fmov s0, #1.00000000
// 0x10a2370: mov x1, xzr
// 0x10a2374: bl #0x1bcebc8
// 0x10a2378: ldr x20, [x19, #0x238]
// 0x10a237c: cbz x20, #0x10a2998
// 0x10a2380: mov x0, x20
// 0x10a2384: mov x1, xzr
// 0x10a2388: bl #0x1bcfaa8
// 0x10a238c: mov x1, x0
// 0x10a2390: mov x0, x20
// 0x10a2394: mov x2, xzr
// 0x10a2398: bl #0x1bcfae4
// 0x10a239c: mov w8, #1
// 0x10a23a0: strb w8, [x19, #0x221]
// 0x10a23a4: ldrb w8, [x19, #0x228]
// 0x10a23a8: cbz w8, #0x10a24b0
// 0x10a23ac: ldrb w8, [x19, #0x2a0]
// 0x10a23b0: cbz w8, #0x10a24d8
// 0x10a23b4: ldr s8, [x19, #0x2a4]
// 0x10a23b8: mov x0, xzr
// 0x10a23bc: bl #0x1b9ad30
// 0x10a23c0: adrp x8, #0x832000
// 0x10a23c4: ldr s1, [x8, #0x3b8]
// 0x10a23c8: fadd s1, s8, s1
// 0x10a23cc: fcmp s1, s0
// 0x10a23d0: b.pl #0x10a2700
// 0x10a23d4: ldrb w8, [x19, #0x255]
// 0x10a23d8: cbnz w8, #0x10a2470
// 0x10a23dc: adrp x8, #0x1e8c000
// 0x10a23e0: ldr x8, [x8, #0xd8]
// 0x10a23e4: ldr x20, [x19, #0x2f8]
// 0x10a23e8: ldr x0, [x8]
// 0x10a23ec: ldr w8, [x0, #0xe0]
// 0x10a23f0: cbnz w8, #0x10a23f8
// 0x10a23f4: bl #0xf7da5c
// 0x10a23f8: mov x0, x20
// 0x10a23fc: mov x1, xzr
// 0x10a2400: bl #0x1b98274
// 0x10a2404: tbz w0, #0, #0x10a2470
// 0x10a2408: ldrb w8, [x19, #0x300]
// 0x10a240c: cbnz w8, #0x10a2470
// 0x10a2410: ldr x0, [x19, #0x80]
// 0x10a2414: cbz x0, #0x10a2998
// 0x10a2418: ldr x20, [x19, #0x2f8]
// 0x10a241c: mov x1, xzr
// 0x10a2420: bl #0x1b9d508
// 0x10a2424: mov w8, #0x43fa0000
// 0x10a2428: fmov s3, #1.00000000
// 0x10a242c: fmov s4, wzr
// 0x10a2430: fmov s5, #1.00000000
// 0x10a2434: fmov s6, #1.00000000
// 0x10a2438: fmov s7, w8
// 0x10a243c: mov x0, x20
// 0x10a2440: mov x1, xzr
// 0x10a2444: bl #0x108d260
// 0x10a2448: ldr x8, [x19, #0x28]
// 0x10a244c: cbz x8, #0x10a2998
// 0x10a2450: ldr x8, [x8, #0x50]
// 0x10a2454: cbz x8, #0x10a2998
// 0x10a2458: ldr x0, [x8, #0x60]
// 0x10a245c: cbz x0, #0x10a2998
// 0x10a2460: mov x1, xzr
// 0x10a2464: bl #0x10bf7e4
// 0x10a2468: mov w8, #1
// 0x10a246c: strb w8, [x19, #0x300]
// 0x10a2470: ldr x0, [x19, #0x88]
// 0x10a2474: cbz x0, #0x10a2998
// 0x10a2478: fmov s0, #1.00000000
// 0x10a247c: mov x1, xzr
// 0x10a2480: bl #0x1b67eb4
// 0x10a2484: ldr x0, [x19, #0x88]
// 0x10a2488: cbz x0, #0x10a2998
// 0x10a248c: adrp x8, #0x1e8e000
// 0x10a2490: ldr x8, [x8, #0x388]
// 0x10a2494: mov x2, xzr
// 0x10a2498: ldr x1, [x8]
// 0x10a249c: bl #0x1b67884
// 0x10a24a0: mov w8, #1
// 0x10a24a4: strh w8, [x19, #0x2a8]
// 0x10a24a8: strb wzr, [x19, #0x2a0]
// 0x10a24ac: b #0x10a2700
// 0x10a24b0: ldr s8, [x19, #0x27c]
// 0x10a24b4: mov x0, xzr
// 0x10a24b8: bl #0x1b9ad30
// 0x10a24bc: adrp x8, #0x832000
// 0x10a24c0: ldr s1, [x8, #0x4f4]
// 0x10a24c4: fadd s1, s8, s1
// 0x10a24c8: fcmp s1, s0
// 0x10a24cc: b.pl #0x10a2700
// 0x10a24d0: strb wzr, [x19, #0x300]
// 0x10a24d4: b #0x10a2700
// 0x10a24d8: ldrb w8, [x19, #0x14a]
// 0x10a24dc: cbz w8, #0x10a2700
// 0x10a24e0: ldr x8, [x19, #0x30]
// 0x10a24e4: cbz x8, #0x10a2998
// 0x10a24e8: ldrb w8, [x8, #0x8e]
// 0x10a24ec: cbz w8, #0x10a26cc
// 0x10a24f0: ldr x8, [x19, #0x28]
// 0x10a24f4: cbz x8, #0x10a2998
// 0x10a24f8: ldrb w9, [x8, #0x2d0]
// 0x10a24fc: ldr x8, [x19, #0x40]
// 0x10a2500: cbz w9, #0x10a2698
// 0x10a2504: cbnz x8, #0x10a26a4
// 0x10a2508: b #0x10a2998
// 0x10a250c: ldrb w8, [x19, #0x2d2]
// 0x10a2510: cbnz w8, #0x10a1ff0
// 0x10a2514: ldr s11, [x19, #0x2d4]
// 0x10a2518: str s15, [sp, #0x20]
// 0x10a251c: ldr s15, [x19, #0x2d8]
// 0x10a2520: mov x0, xzr
// 0x10a2524: bl #0x1b9ad30
// 0x10a2528: fadd s1, s11, s15
// 0x10a252c: ldr s15, [sp, #0x20]
// 0x10a2530: fcmp s1, s0
// 0x10a2534: b.pl #0x10a1ff0
// 0x10a2538: ldrb w8, [x19, #0x2d0]
// 0x10a253c: cbz w8, #0x10a2724
// 0x10a2540: ldr x0, [x19, #0x60]
// 0x10a2544: cbz x0, #0x10a2998
// 0x10a2548: mov x1, xzr
// 0x10a254c: bl #0x1b9d508
// 0x10a2550: ldp s3, s4, [x19, #0x74]
// 0x10a2554: ldr s5, [x19, #0x7c]
// 0x10a2558: ldr s11, [x19, #0x3e0]
// 0x10a255c: fmov s6, #0.75000000
// 0x10a2560: fmul s3, s3, s6
// 0x10a2564: fmul s4, s4, s6
// 0x10a2568: fmul s5, s5, s6
// 0x10a256c: add x0, x19, #0x304
// 0x10a2570: mov x1, xzr
// 0x10a2574: fadd s12, s0, s3
// 0x10a2578: fadd s15, s1, s4
// 0x10a257c: fadd s14, s2, s5
// 0x10a2580: bl #0x1b95168
// 0x10a2584: ldr x8, [x21]
// 0x10a2588: mov w20, w0
// 0x10a258c: ldr w9, [x8, #0xe0]
// 0x10a2590: cbnz w9, #0x10a259c
// 0x10a2594: mov x0, x8
// 0x10a2598: bl #0xf7da5c
// 0x10a259c: ldr s0, [sp, #0xbc]
// 0x10a25a0: mov v1.16b, v15.16b
// 0x10a25a4: ldr s15, [sp, #0x20]
// 0x10a25a8: ldr s5, [sp, #0x40]
// 0x10a25ac: fmul s6, s11, s0
// 0x10a25b0: mov w1, #1
// 0x10a25b4: mov v0.16b, v12.16b
// 0x10a25b8: mov v2.16b, v14.16b
// 0x10a25bc: mov v3.16b, v15.16b
// 0x10a25c0: mov v4.16b, v13.16b
// 0x10a25c4: mov w0, w20
// 0x10a25c8: mov x2, xzr
// 0x10a25cc: bl #0x1bcdfcc
// 0x10a25d0: tbnz w0, #0, #0x10a298c
// 0x10a25d4: mov w8, #0xcccd
// 0x10a25d8: movk w8, #0x3e4c, lsl #16
// 0x10a25dc: mov x0, xzr
// 0x10a25e0: str w8, [x19, #0x2ec]
// 0x10a25e4: strb wzr, [x19, #0x2d0]
// 0x10a25e8: bl #0x1b9ad30
// 0x10a25ec: str s0, [x19, #0x2d4]
// 0x10a25f0: b #0x10a298c
// 0x10a25f4: ldrb w8, [x19, #0x228]
// 0x10a25f8: cbz w8, #0x10a2018
// 0x10a25fc: ldrb w8, [x19, #0x2de]
// 0x10a2600: cbnz w8, #0x10a20a0
// 0x10a2604: ldr s11, [x19, #0x2e0]
// 0x10a2608: ldr s12, [x19, #0x2e4]
// 0x10a260c: mov x0, xzr
// 0x10a2610: bl #0x1b9ad30
// 0x10a2614: fadd s1, s11, s12
// 0x10a2618: fcmp s1, s0
// 0x10a261c: b.pl #0x10a20a0
// 0x10a2620: ldrb w8, [x19, #0x2dc]
// 0x10a2624: cbz w8, #0x10a27d8
// 0x10a2628: ldr s11, [x19, #0x3e0]
// 0x10a262c: add x0, x19, #0x304
// 0x10a2630: mov x1, xzr
// 0x10a2634: bl #0x1b95168
// 0x10a2638: ldr x8, [x21]
// 0x10a263c: mov w20, w0
// 0x10a2640: ldr w9, [x8, #0xe0]
// 0x10a2644: cbnz w9, #0x10a2650
// 0x10a2648: mov x0, x8
// 0x10a264c: bl #0xf7da5c
// 0x10a2650: ldr s0, [sp, #0xbc]
// 0x10a2654: ldr s5, [sp, #0x40]
// 0x10a2658: mov w1, #1
// 0x10a265c: mov v1.16b, v9.16b
// 0x10a2660: fmul s6, s11, s0
// 0x10a2664: mov v0.16b, v8.16b
// 0x10a2668: mov v2.16b, v10.16b
// 0x10a266c: mov v3.16b, v15.16b
// 0x10a2670: mov v4.16b, v13.16b
// 0x10a2674: mov w0, w20
// 0x10a2678: mov x2, xzr
// 0x10a267c: bl #0x1bcdfcc
// 0x10a2680: tbnz w0, #0, #0x10a27f4
// 0x10a2684: mov w8, #0xcccd
// 0x10a2688: movk w8, #0x3e4c, lsl #16
// 0x10a268c: str w8, [x19, #0x2ec]
// 0x10a2690: strb wzr, [x19, #0x2dc]
// 0x10a2694: b #0x10a27f4
// 0x10a2698: cbz x8, #0x10a2998
// 0x10a269c: ldrb w9, [x8, #0x23a]
// 0x10a26a0: cbz w9, #0x10a26ac
// 0x10a26a4: ldrb w8, [x8, #0x23a]
// 0x10a26a8: cbz w8, #0x10a26cc
// 0x10a26ac: ldrb w8, [x19, #0x2a9]
// 0x10a26b0: cbz w8, #0x10a26cc
// 0x10a26b4: ldrb w8, [x19, #0x2d0]
// 0x10a26b8: cbnz w8, #0x10a26cc
// 0x10a26bc: ldrb w8, [x19, #0x2dc]
// 0x10a26c0: cbnz w8, #0x10a26cc
// 0x10a26c4: ldrb w8, [x19, #0x257]
// 0x10a26c8: cbz w8, #0x10a2820
// 0x10a26cc: ldr x8, [x19, #0x30]
// 0x10a26d0: cbz x8, #0x10a2998
// 0x10a26d4: ldrb w8, [x8, #0x8d]
// 0x10a26d8: cbnz w8, #0x10a2700
// 0x10a26dc: ldr s8, [x19, #0x2ac]
// 0x10a26e0: ldr s9, [x19, #0x29c]
// 0x10a26e4: mov x0, xzr
// 0x10a26e8: bl #0x1b9ad30
// 0x10a26ec: fadd s1, s8, s9
// 0x10a26f0: fcmp s1, s0
// 0x10a26f4: b.pl #0x10a2700
// 0x10a26f8: mov w8, #1
// 0x10a26fc: strb w8, [x19, #0x2a9]
// 0x10a2700: ldp x20, x19, [sp, #0xd0]
// 0x10a2704: ldp x22, x21, [sp, #0xc0]
// 0x10a2708: ldr x30, [sp, #0xb0]
// 0x10a270c: ldp d9, d8, [sp, #0xa0]
// 0x10a2710: ldp d11, d10, [sp, #0x90]
// 0x10a2714: ldp d13, d12, [sp, #0x80]
// 0x10a2718: ldp d15, d14, [sp, #0x70]
// 0x10a271c: add sp, sp, #0xe0
// 0x10a2720: ret
// 0x10a2724: ldrb w8, [x19, #0x2d1]
// 0x10a2728: cbz w8, #0x10a2540
// 0x10a272c: ldrb w8, [x19, #0x2dc]
// 0x10a2730: cbz w8, #0x10a295c
// 0x10a2734: ldr s0, [sp]
// 0x10a2738: ldr s1, [sp, #0xb8]
// 0x10a273c: ldp s3, s2, [sp, #0x38]
// 0x10a2740: ldr s11, [x19, #0x3e0]
// 0x10a2744: fadd s0, s0, s14
// 0x10a2748: fsub s0, s0, s12
// 0x10a274c: fmul s1, s1, s0
// 0x10a2750: fmul s2, s2, s0
// 0x10a2754: fmul s0, s3, s0
// 0x10a2758: add x0, x19, #0x304
// 0x10a275c: mov x1, xzr
// 0x10a2760: fadd s15, s8, s1
// 0x10a2764: fadd s14, s9, s2
// 0x10a2768: fadd s12, s10, s0
// 0x10a276c: bl #0x1b95168
// 0x10a2770: ldr x8, [x21]
// 0x10a2774: mov w20, w0
// 0x10a2778: ldr w9, [x8, #0xe0]
// 0x10a277c: cbnz w9, #0x10a2788
// 0x10a2780: mov x0, x8
// 0x10a2784: bl #0xf7da5c
// 0x10a2788: mov w1, #1
// 0x10a278c: mov v0.16b, v8.16b
// 0x10a2790: mov v1.16b, v9.16b
// 0x10a2794: mov v2.16b, v10.16b
// 0x10a2798: mov v3.16b, v15.16b
// 0x10a279c: mov v4.16b, v14.16b
// 0x10a27a0: mov v5.16b, v12.16b
// 0x10a27a4: mov v6.16b, v11.16b
// 0x10a27a8: mov w0, w20
// 0x10a27ac: mov x2, xzr
// 0x10a27b0: mov w22, #1
// 0x10a27b4: bl #0x1bcdfcc
// 0x10a27b8: ldr s15, [sp, #0x20]
// 0x10a27bc: tbnz w0, #0, #0x10a2970
// 0x10a27c0: mov w8, #0x999a
// 0x10a27c4: movk w8, #0x3e19, lsl #16
// 0x10a27c8: strh w22, [x19, #0x2d0]
// 0x10a27cc: str w8, [x19, #0x2ec]
// 0x10a27d0: strb wzr, [x19, #0x2dc]
// 0x10a27d4: b #0x10a2970
// 0x10a27d8: mov w8, #0xcccd
// 0x10a27dc: movk w8, #0x3dcc, lsl #16
// 0x10a27e0: mov w9, #1
// 0x10a27e4: strb wzr, [x19, #0x2d0]
// 0x10a27e8: str w8, [x19, #0x2ec]
// 0x10a27ec: strb w9, [x19, #0x2dc]
// 0x10a27f0: strb wzr, [x19, #0x2b1]
// 0x10a27f4: mov x0, xzr
// 0x10a27f8: bl #0x1b9ad30
// 0x10a27fc: mov x0, xzr
// 0x10a2800: str s0, [x19, #0x2e0]
// 0x10a2804: bl #0x1b9ad30
// 0x10a2808: add x8, x19, #0x2dd
// 0x10a280c: mov w9, #0x100
// 0x10a2810: str s0, [x19, #0x2d4]
// 0x10a2814: strb wzr, [x19, #0x2d1]
// 0x10a2818: strh w9, [x8]
// 0x10a281c: b #0x10a20a0
// 0x10a2820: ldrb w8, [x19, #0x259]
// 0x10a2824: cbz w8, #0x10a26cc
// 0x10a2828: ldrb w8, [x19, #0x295]
// 0x10a282c: cbnz w8, #0x10a26cc
// 0x10a2830: ldr s8, [x19, #0x2ac]
// 0x10a2834: ldr s9, [x19, #0x29c]
// 0x10a2838: mov x0, xzr
// 0x10a283c: bl #0x1b9ad30
// 0x10a2840: fadd s1, s8, s9
// 0x10a2844: fcmp s1, s0
// 0x10a2848: b.pl #0x10a26cc
// 0x10a284c: ldrb w8, [x19, #0x229]
// 0x10a2850: cbz w8, #0x10a285c
// 0x10a2854: ldrb w8, [x19, #0x255]
// 0x10a2858: cbz w8, #0x10a26cc
// 0x10a285c: mov x0, xzr
// 0x10a2860: bl #0x1b9ad30
// 0x10a2864: ldrb w8, [x19, #0x2a8]
// 0x10a2868: str s0, [x19, #0x2a4]
// 0x10a286c: cbz w8, #0x10a28b4
// 0x10a2870: ldr x8, [x19, #0x28]
// 0x10a2874: cbz x8, #0x10a2998
// 0x10a2878: ldr x0, [x19, #0x80]
// 0x10a287c: cbz x0, #0x10a2998
// 0x10a2880: ldr x20, [x8, #0x408]
// 0x10a2884: mov x1, xzr
// 0x10a2888: bl #0x1b9d508
// 0x10a288c: mov w8, #0x43fa0000
// 0x10a2890: fmov s3, #1.00000000
// 0x10a2894: fmov s4, wzr
// 0x10a2898: fmov s5, #1.00000000
// 0x10a289c: fmov s6, #1.00000000
// 0x10a28a0: fmov s7, w8
// 0x10a28a4: mov x0, x20
// 0x10a28a8: mov x1, xzr
// 0x10a28ac: bl #0x108d260
// 0x10a28b0: strb wzr, [x19, #0x2a8]
// 0x10a28b4: ldr x8, [x19, #0x28]
// 0x10a28b8: cbz x8, #0x10a2998
// 0x10a28bc: ldr x8, [x8, #0x50]
// 0x10a28c0: cbz x8, #0x10a2998
// 0x10a28c4: ldr x0, [x8, #0x60]
// 0x10a28c8: cbz x0, #0x10a2998
// 0x10a28cc: mov x1, xzr
// 0x10a28d0: bl #0x10bf774
// 0x10a28d4: ldr x0, [x19, #0x88]
// 0x10a28d8: cbz x0, #0x10a2998
// 0x10a28dc: fmov s0, #1.00000000
// 0x10a28e0: mov x1, xzr
// 0x10a28e4: bl #0x1b67eb4
// 0x10a28e8: ldr x0, [x19, #0x88]
// 0x10a28ec: cbz x0, #0x10a2998
// 0x10a28f0: adrp x8, #0x1e8e000
// 0x10a28f4: ldr x8, [x8, #0x380]
// 0x10a28f8: mov x2, xzr
// 0x10a28fc: ldr x1, [x8]
// 0x10a2900: bl #0x1b67884
// 0x10a2904: ldr x0, [x21]
// 0x10a2908: ldr x20, [x19, #0x98]
// 0x10a290c: ldr s8, [x19, #0xe0]
// 0x10a2910: ldr w8, [x0, #0xe0]
// 0x10a2914: cbnz w8, #0x10a291c
// 0x10a2918: bl #0xf7da5c
// 0x10a291c: mov x0, xzr
// 0x10a2920: bl #0x1bcb1c0
// 0x10a2924: cbz x20, #0x10a2998
// 0x10a2928: fadd s0, s8, s8
// 0x10a292c: fneg s1, s1
// 0x10a2930: fmul s0, s0, s1
// 0x10a2934: fsqrt s1, s0
// 0x10a2938: fmov s0, wzr
// 0x10a293c: fmov s2, wzr
// 0x10a2940: mov w1, #2
// 0x10a2944: mov x0, x20
// 0x10a2948: mov x2, xzr
// 0x10a294c: bl #0x1bcf5b8
// 0x10a2950: mov w8, #1
// 0x10a2954: strb w8, [x19, #0x2a0]
// 0x10a2958: b #0x10a26cc
// 0x10a295c: mov w8, #0xcccd
// 0x10a2960: movk w8, #0x3dcc, lsl #16
// 0x10a2964: mov w9, #1
// 0x10a2968: str w8, [x19, #0x2ec]
// 0x10a296c: strb w9, [x19, #0x2d0]
// 0x10a2970: mov x0, xzr
// 0x10a2974: bl #0x1b9ad30
// 0x10a2978: mov x0, xzr
// 0x10a297c: str s0, [x19, #0x2d4]
// 0x10a2980: bl #0x1b9ad30
// 0x10a2984: str s0, [x19, #0x2e0]
// 0x10a2988: strb wzr, [x19, #0x2b1]
// 0x10a298c: mov w8, #1
// 0x10a2990: strb w8, [x19, #0x2d2]
// 0x10a2994: b #0x10a1ff0
// 0x10a2998: bl #0xf7db74
```

## `FPSRigidBodyWalker.FixedUpdate` — RVA `0xca299c`

- Decompiled symbol: `FPSRigidBodyWalker_FixedUpdate`
- Metadata signature: `private void FixedUpdate() { }`
- Native interval: `11628` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: Decompiler produced no C-like text

```c
// 0x10a299c: sub sp, sp, #0x170
// 0x10a29a0: stp d15, d14, [sp, #0xd0]
// 0x10a29a4: stp d13, d12, [sp, #0xe0]
// 0x10a29a8: stp d11, d10, [sp, #0xf0]
// 0x10a29ac: stp d9, d8, [sp, #0x100]
// 0x10a29b0: stp x29, x30, [sp, #0x110]
// 0x10a29b4: stp x28, x27, [sp, #0x120]
// 0x10a29b8: stp x26, x25, [sp, #0x130]
// 0x10a29bc: stp x24, x23, [sp, #0x140]
// 0x10a29c0: stp x22, x21, [sp, #0x150]
// 0x10a29c4: stp x20, x19, [sp, #0x160]
// 0x10a29c8: adrp x20, #0x1fab000
// 0x10a29cc: ldrb w8, [x20, #0x4ba]
// 0x10a29d0: mov x19, x0
// 0x10a29d4: tbnz w8, #0, #0x10a2a40
// 0x10a29d8: adrp x0, #0x1e8c000
// 0x10a29dc: ldr x0, [x0, #0xd8]
// 0x10a29e0: bl #0xf7d92c
// 0x10a29e4: adrp x0, #0x1e8d000
// 0x10a29e8: ldr x0, [x0, #0x4a8]
// 0x10a29ec: bl #0xf7d92c
// 0x10a29f0: adrp x0, #0x1e8e000
// 0x10a29f4: ldr x0, [x0, #0xb0]
// 0x10a29f8: bl #0xf7d92c
// 0x10a29fc: adrp x0, #0x1e8e000
// 0x10a2a00: ldr x0, [x0, #0xc8]
// 0x10a2a04: bl #0xf7d92c
// 0x10a2a08: adrp x0, #0x1e8e000
// 0x10a2a0c: ldr x0, [x0, #0xd0]
// 0x10a2a10: bl #0xf7d92c
// 0x10a2a14: adrp x0, #0x1e8e000
// 0x10a2a18: ldr x0, [x0, #0xd8]
// 0x10a2a1c: bl #0xf7d92c
// 0x10a2a20: adrp x0, #0x1e8e000
// 0x10a2a24: ldr x0, [x0, #0x388]
// 0x10a2a28: bl #0xf7d92c
// 0x10a2a2c: adrp x0, #0x1e8e000
// 0x10a2a30: ldr x0, [x0, #0xe0]
// 0x10a2a34: bl #0xf7d92c
// 0x10a2a38: mov w8, #1
// 0x10a2a3c: strb w8, [x20, #0x4ba]
// 0x10a2a40: movi v0.2d, #0000000000000000
// 0x10a2a44: mov x0, xzr
// 0x10a2a48: stur q0, [sp, #0xbc]
// 0x10a2a4c: stp q0, q0, [sp, #0xa0]
// 0x10a2a50: bl #0x1b9ae58
// 0x10a2a54: fcmp s0, #0.0
// 0x10a2a58: b.le #0x10a4ec8
// 0x10a2a5c: ldr x8, [x19, #0x28]
// 0x10a2a60: cbz x8, #0x10a5704
// 0x10a2a64: ldr x1, [x8, #0x78]
// 0x10a2a68: mov x20, x19
// 0x10a2a6c: str x1, [x20, #0x40]!
// 0x10a2a70: mov x0, x20
// 0x10a2a74: bl #0xf7d8d0
// 0x10a2a78: ldr x0, [x20, #0x20]
// 0x10a2a7c: cbz x0, #0x10a5704
// 0x10a2a80: ldrb w21, [x19, #0x2dc]
// 0x10a2a84: mov x1, xzr
// 0x10a2a88: bl #0x1b9d508
// 0x10a2a8c: mov v8.16b, v2.16b
// 0x10a2a90: str s0, [x19, #0x394]
// 0x10a2a94: str s1, [x19, #0x398]
// 0x10a2a98: str s2, [x19, #0x39c]
// 0x10a2a9c: stp q1, q0, [sp, #0x60]
// 0x10a2aa0: cbz w21, #0x10a2b4c
// 0x10a2aa4: ldr x0, [x19, #0x238]
// 0x10a2aa8: cbz x0, #0x10a5704
// 0x10a2aac: ldr s9, [x19, #0x70]
// 0x10a2ab0: ldr d10, [x19, #0x68]
// 0x10a2ab4: mov x1, xzr
// 0x10a2ab8: bl #0x1bcfdf0
// 0x10a2abc: ldp q2, q4, [sp, #0x60]
// 0x10a2ac0: adrp x8, #0x832000
// 0x10a2ac4: ldr s1, [x19, #0x3e0]
// 0x10a2ac8: ldr x0, [x19, #0x60]
// 0x10a2acc: mov v4.s[1], v2.s[0]
// 0x10a2ad0: ldr s2, [x8, #0x4d4]
// 0x10a2ad4: fmov s3, #0.25000000
// 0x10a2ad8: fmul s1, s1, s3
// 0x10a2adc: str s1, [x19, #0x3d4]
// 0x10a2ae0: fmul s0, s0, s2
// 0x10a2ae4: fmul v2.2s, v10.2s, v0.s[0]
// 0x10a2ae8: fmul s0, s9, s0
// 0x10a2aec: fadd v2.2s, v4.2s, v2.2s
// 0x10a2af0: fadd s0, s8, s0
// 0x10a2af4: str d2, [x19, #0x3a0]
// 0x10a2af8: str s0, [x19, #0x3a8]
// 0x10a2afc: cbz x0, #0x10a5704
// 0x10a2b00: mov x1, xzr
// 0x10a2b04: bl #0x1b9d508
// 0x10a2b08: ldr x0, [x19, #0x60]
// 0x10a2b0c: str s0, [x19, #0x270]
// 0x10a2b10: str s1, [x19, #0x274]
// 0x10a2b14: str s2, [x19, #0x278]
// 0x10a2b18: cbz x0, #0x10a5704
// 0x10a2b1c: mov x1, xzr
// 0x10a2b20: bl #0x1b9d508
// 0x10a2b24: ldr d3, [x19, #0x68]
// 0x10a2b28: ldr s4, [x19, #0x3e0]
// 0x10a2b2c: ldr s5, [x19, #0x70]
// 0x10a2b30: fmov v6.2s, #0.25000000
// 0x10a2b34: fmov s7, #0.25000000
// 0x10a2b38: fmul v3.2s, v3.2s, v4.s[0]
// 0x10a2b3c: fmul s4, s5, s4
// 0x10a2b40: fmul v3.2s, v3.2s, v6.2s
// 0x10a2b44: fmul s4, s4, s7
// 0x10a2b48: b #0x10a2c38
// 0x10a2b4c: ldr x0, [x19, #0x238]
// 0x10a2b50: cbz x0, #0x10a5704
// 0x10a2b54: ldr s9, [x19, #0x7c]
// 0x10a2b58: ldur d10, [x19, #0x74]
// 0x10a2b5c: mov x1, xzr
// 0x10a2b60: bl #0x1bcfdf0
// 0x10a2b64: adrp x8, #0x832000
// 0x10a2b68: ldr s2, [x8, #0x3c8]
// 0x10a2b6c: adrp x8, #0x832000
// 0x10a2b70: ldr s1, [x19, #0x3dc]
// 0x10a2b74: ldr s3, [x8, #0x4f4]
// 0x10a2b78: ldp q5, q4, [sp, #0x60]
// 0x10a2b7c: ldrb w21, [x19, #0x2d0]
// 0x10a2b80: ldr x0, [x19, #0x60]
// 0x10a2b84: fmul s0, s0, s2
// 0x10a2b88: mov v4.s[1], v5.s[0]
// 0x10a2b8c: fmul s1, s1, s3
// 0x10a2b90: fmov s2, #0.50000000
// 0x10a2b94: fmul v3.2s, v10.2s, v0.s[0]
// 0x10a2b98: fmul s0, s9, s0
// 0x10a2b9c: fadd s1, s1, s2
// 0x10a2ba0: fadd v2.2s, v4.2s, v3.2s
// 0x10a2ba4: fadd s0, s8, s0
// 0x10a2ba8: str d2, [x19, #0x3a0]
// 0x10a2bac: str s0, [x19, #0x3a8]
// 0x10a2bb0: str s1, [x19, #0x3d4]
// 0x10a2bb4: cbz x0, #0x10a5704
// 0x10a2bb8: mov x1, xzr
// 0x10a2bbc: bl #0x1b9d508
// 0x10a2bc0: adrp x8, #0x832000
// 0x10a2bc4: ldr s4, [x19, #0x3e0]
// 0x10a2bc8: ldr s5, [x8, #0x550]
// 0x10a2bcc: ldr d3, [x19, #0x68]
// 0x10a2bd0: ldr s6, [x19, #0x70]
// 0x10a2bd4: ldr x0, [x19, #0x60]
// 0x10a2bd8: mov v0.s[1], v1.s[0]
// 0x10a2bdc: fmul s1, s4, s5
// 0x10a2be0: fmul v3.2s, v3.2s, v1.s[0]
// 0x10a2be4: fmul s1, s6, s1
// 0x10a2be8: fsub v0.2s, v0.2s, v3.2s
// 0x10a2bec: fsub s1, s2, s1
// 0x10a2bf0: str d0, [x19, #0x270]
// 0x10a2bf4: str s1, [x19, #0x278]
// 0x10a2bf8: cbz x0, #0x10a5704
// 0x10a2bfc: mov x1, xzr
// 0x10a2c00: bl #0x1b9d508
// 0x10a2c04: ldr d3, [x19, #0x68]
// 0x10a2c08: ldr s4, [x19, #0x3e0]
// 0x10a2c0c: ldr s5, [x19, #0x70]
// 0x10a2c10: fmul v3.2s, v3.2s, v4.s[0]
// 0x10a2c14: fmul s4, s5, s4
// 0x10a2c18: cbz w21, #0x10a2c28
// 0x10a2c1c: movi v5.2s, #0x3f, lsl #24
// 0x10a2c20: fmov s6, #0.50000000
// 0x10a2c24: b #0x10a2c30
// 0x10a2c28: fmov v5.2s, #0.75000000
// 0x10a2c2c: fmov s6, #0.75000000
// 0x10a2c30: fmul v3.2s, v3.2s, v5.2s
// 0x10a2c34: fmul s4, s4, s6
// 0x10a2c38: ldr x0, [x19, #0x98]
// 0x10a2c3c: mov v0.s[1], v1.s[0]
// 0x10a2c40: fadd v0.2s, v0.2s, v3.2s
// 0x10a2c44: fadd s1, s2, s4
// 0x10a2c48: str d0, [x19, #0x248]
// 0x10a2c4c: str s1, [x19, #0x250]
// 0x10a2c50: cbz x0, #0x10a5704
// 0x10a2c54: mov x1, xzr
// 0x10a2c58: bl #0x1bceef8
// 0x10a2c5c: ldr x8, [x19, #0x28]
// 0x10a2c60: str s0, [x19, #0x22c]
// 0x10a2c64: str s1, [x19, #0x230]
// 0x10a2c68: str s2, [x19, #0x234]
// 0x10a2c6c: cbz x8, #0x10a5704
// 0x10a2c70: ldr s0, [x8, #0x20c]
// 0x10a2c74: fcmp s0, #0.0
// 0x10a2c78: b.lt #0x10a3040
// 0x10a2c7c: ldr x8, [x19, #0x30]
// 0x10a2c80: cbz x8, #0x10a5704
// 0x10a2c84: ldr s1, [x19, #0xec]
// 0x10a2c88: ldp s0, s2, [x8, #0xdc]
// 0x10a2c8c: ldr x0, [x19, #0x60]
// 0x10a2c90: str wzr, [x19, #0x3e8]
// 0x10a2c94: fmul s0, s0, s1
// 0x10a2c98: fmul s2, s1, s2
// 0x10a2c9c: str s0, [x19, #0x3e4]
// 0x10a2ca0: str s2, [x19, #0x3ec]
// 0x10a2ca4: cbz x0, #0x10a5704
// 0x10a2ca8: fmov s1, wzr
// 0x10a2cac: mov x1, xzr
// 0x10a2cb0: bl #0x1b9e01c
// 0x10a2cb4: mov v8.16b, v0.16b
// 0x10a2cb8: str s0, [x19, #0x3e4]
// 0x10a2cbc: ldr s0, [x19, #0x270]
// 0x10a2cc0: ldr s3, [x19, #0x274]
// 0x10a2cc4: ldr s12, [x19, #0x248]
// 0x10a2cc8: ldr s13, [x19, #0x24c]
// 0x10a2ccc: str s0, [sp, #0x70]
// 0x10a2cd0: ldr s0, [x19, #0x278]
// 0x10a2cd4: ldr s14, [x19, #0x250]
// 0x10a2cd8: ldr s10, [x19, #0x3e0]
// 0x10a2cdc: ldr s11, [x19, #0x3d4]
// 0x10a2ce0: add x0, x19, #0x304
// 0x10a2ce4: mov x1, xzr
// 0x10a2ce8: mov v15.16b, v1.16b
// 0x10a2cec: mov v9.16b, v2.16b
// 0x10a2cf0: str s1, [x19, #0x3e8]
// 0x10a2cf4: stp s0, s3, [sp, #0x5c]
// 0x10a2cf8: str s2, [x19, #0x3ec]
// 0x10a2cfc: add x21, x19, #0x368
// 0x10a2d00: bl #0x1b95168
// 0x10a2d04: adrp x8, #0x1e8d000
// 0x10a2d08: ldr x8, [x8, #0x4a8]
// 0x10a2d0c: mov w22, w0
// 0x10a2d10: ldr x8, [x8]
// 0x10a2d14: ldr w9, [x8, #0xe0]
// 0x10a2d18: cbnz w9, #0x10a2d24
// 0x10a2d1c: mov x0, x8
// 0x10a2d20: bl #0xf7da5c
// 0x10a2d24: adrp x8, #0x832000
// 0x10a2d28: ldr s0, [x8, #0x3c8]
// 0x10a2d2c: ldp s2, s1, [sp, #0x5c]
// 0x10a2d30: mov w2, #1
// 0x10a2d34: mov v3.16b, v12.16b
// 0x10a2d38: fmul s6, s10, s0
// 0x10a2d3c: ldr s0, [sp, #0x70]
// 0x10a2d40: mov v4.16b, v13.16b
// 0x10a2d44: mov v5.16b, v14.16b
// 0x10a2d48: mov x0, x21
// 0x10a2d4c: mov w1, w22
// 0x10a2d50: mov x3, xzr
// 0x10a2d54: str s11, [sp, #0x10]
// 0x10a2d58: stp s15, s9, [sp, #4]
// 0x10a2d5c: str s8, [sp]
// 0x10a2d60: bl #0x1bcc7c4
// 0x10a2d64: tbz w0, #0, #0x10a2d70
// 0x10a2d68: ldrb w8, [x19, #0x295]
// 0x10a2d6c: cbz w8, #0x10a2e60
// 0x10a2d70: ldrb w8, [x19, #0x2b1]
// 0x10a2d74: cbz w8, #0x10a2d8c
// 0x10a2d78: ldrb w8, [x19, #0x146]
// 0x10a2d7c: cbz w8, #0x10a2dd8
// 0x10a2d80: mov w8, #0x3f800000
// 0x10a2d84: str w8, [x19, #0xc4]
// 0x10a2d88: b #0x10a2e40
// 0x10a2d8c: ldrb w8, [x19, #0x2dc]
// 0x10a2d90: cbz w8, #0x10a2db8
// 0x10a2d94: ldr x8, [x19, #0x20]
// 0x10a2d98: cbz x8, #0x10a5704
// 0x10a2d9c: ldr s0, [x8, #0x78]
// 0x10a2da0: fmov s1, #25.00000000
// 0x10a2da4: fcmp s0, s1
// 0x10a2da8: b.le #0x10a2db8
// 0x10a2dac: str wzr, [x19, #0xc4]
// 0x10a2db0: str wzr, [x19, #0xbc]
// 0x10a2db4: b #0x10a2e40
// 0x10a2db8: ldr x8, [x19, #0x30]
// 0x10a2dbc: cbz x8, #0x10a5704
// 0x10a2dc0: ldr s0, [x8, #0xe0]
// 0x10a2dc4: ldr s1, [x8, #0xc8]
// 0x10a2dc8: fabs s2, s0
// 0x10a2dcc: fcmp s2, s1
// 0x10a2dd0: b.gt #0x10a2e34
// 0x10a2dd4: b #0x10a2e3c
// 0x10a2dd8: ldr x8, [x19, #0x30]
// 0x10a2ddc: cbz x8, #0x10a5704
// 0x10a2de0: ldr s0, [x8, #0xe0]
// 0x10a2de4: ldr s1, [x8, #0xc8]
// 0x10a2de8: fabs s2, s0
// 0x10a2dec: fcmp s2, s1
// 0x10a2df0: b.le #0x10a2e3c
// 0x10a2df4: ldr s8, [x19, #0xc4]
// 0x10a2df8: fcmp s0, #0.0
// 0x10a2dfc: fmov s0, #-1.00000000
// 0x10a2e00: fmov s9, #1.00000000
// 0x10a2e04: mov x0, xzr
// 0x10a2e08: fcsel s10, s9, s0, ge
// 0x10a2e0c: bl #0x1b89b60
// 0x10a2e10: ldr s1, [x19, #0xc8]
// 0x10a2e14: fmov s2, wzr
// 0x10a2e18: fmul s0, s0, s1
// 0x10a2e1c: fmin s1, s0, s9
// 0x10a2e20: fcmp s0, #0.0
// 0x10a2e24: fcsel s0, s1, s2, pl
// 0x10a2e28: fsub s1, s10, s8
// 0x10a2e2c: fmul s0, s1, s0
// 0x10a2e30: fadd s0, s8, s0
// 0x10a2e34: str s0, [x19, #0xc4]
// 0x10a2e38: b #0x10a2e40
// 0x10a2e3c: str wzr, [x19, #0xc4]
// 0x10a2e40: ldrb w8, [x19, #0x258]
// 0x10a2e44: cbz w8, #0x10a2e54
// 0x10a2e48: mov w8, #0x40400000
// 0x10a2e4c: str w8, [x19, #0xc8]
// 0x10a2e50: b #0x10a2f24
// 0x10a2e54: ldr s0, [x19, #0xd0]
// 0x10a2e58: str s0, [x19, #0xc8]
// 0x10a2e5c: b #0x10a2f24
// 0x10a2e60: mov x0, x21
// 0x10a2e64: mov x1, xzr
// 0x10a2e68: bl #0x1bcee00
// 0x10a2e6c: adrp x8, #0x1e8c000
// 0x10a2e70: ldr x8, [x8, #0xd8]
// 0x10a2e74: mov x22, x0
// 0x10a2e78: ldr x8, [x8]
// 0x10a2e7c: ldr w9, [x8, #0xe0]
// 0x10a2e80: cbnz w9, #0x10a2e8c
// 0x10a2e84: mov x0, x8
// 0x10a2e88: bl #0xf7da5c
// 0x10a2e8c: mov x0, x22
// 0x10a2e90: mov x1, xzr
// 0x10a2e94: bl #0x1b98274
// 0x10a2e98: tbnz w0, #0, #0x10a2ea4
// 0x10a2e9c: ldrb w8, [x19, #0x228]
// 0x10a2ea0: cbnz w8, #0x10a2ec0
// 0x10a2ea4: ldr s8, [x19, #0x27c]
// 0x10a2ea8: mov x0, xzr
// 0x10a2eac: bl #0x1b9ad30
// 0x10a2eb0: fmov s1, #0.50000000
// 0x10a2eb4: fadd s1, s8, s1
// 0x10a2eb8: fcmp s1, s0
// 0x10a2ebc: b.le #0x10a2edc
// 0x10a2ec0: mov x0, x21
// 0x10a2ec4: mov x1, xzr
// 0x10a2ec8: bl #0x1bcec58
// 0x10a2ecc: cbz x0, #0x10a5704
// 0x10a2ed0: mov x1, xzr
// 0x10a2ed4: bl #0x1bcf97c
// 0x10a2ed8: tbz w0, #0, #0x10a34c8
// 0x10a2edc: ldrb w8, [x19, #0x2dc]
// 0x10a2ee0: cbz w8, #0x10a2efc
// 0x10a2ee4: ldr x8, [x19, #0x20]
// 0x10a2ee8: cbz x8, #0x10a5704
// 0x10a2eec: ldr s0, [x8, #0x78]
// 0x10a2ef0: fmov s1, #25.00000000
// 0x10a2ef4: fcmp s0, s1
// 0x10a2ef8: b.gt #0x10a2f20
// 0x10a2efc: ldr x8, [x19, #0x30]
// 0x10a2f00: cbz x8, #0x10a5704
// 0x10a2f04: ldr s0, [x8, #0xe0]
// 0x10a2f08: ldr s1, [x8, #0xc8]
// 0x10a2f0c: fabs s2, s0
// 0x10a2f10: fcmp s2, s1
// 0x10a2f14: b.le #0x10a2f20
// 0x10a2f18: str s0, [x19, #0xc4]
// 0x10a2f1c: b #0x10a2f24
// 0x10a2f20: str wzr, [x19, #0xc4]
// 0x10a2f24: ldrb w8, [x19, #0x258]
// 0x10a2f28: fmov s0, #3.00000000
// 0x10a2f2c: cbnz w8, #0x10a2f34
// 0x10a2f30: ldr s0, [x19, #0xd0]
// 0x10a2f34: ldrb w8, [x19, #0x2b1]
// 0x10a2f38: str s0, [x19, #0xcc]
// 0x10a2f3c: cbz w8, #0x10a2f74
// 0x10a2f40: ldr x8, [x19, #0x30]
// 0x10a2f44: cbz x8, #0x10a5704
// 0x10a2f48: ldr s0, [x8, #0xdc]
// 0x10a2f4c: adrp x8, #0x832000
// 0x10a2f50: ldr s1, [x8, #0x4d4]
// 0x10a2f54: fabs s2, s0
// 0x10a2f58: fcmp s2, s1
// 0x10a2f5c: b.le #0x10a2fa0
// 0x10a2f60: fcmp s0, #0.0
// 0x10a2f64: fmov s0, #-1.00000000
// 0x10a2f68: fmov s1, #1.00000000
// 0x10a2f6c: fcsel s8, s1, s0, ge
// 0x10a2f70: b #0x10a2fb8
// 0x10a2f74: ldrb w8, [x19, #0x2dc]
// 0x10a2f78: cbz w8, #0x10a2fac
// 0x10a2f7c: ldr x8, [x19, #0x20]
// 0x10a2f80: cbz x8, #0x10a5704
// 0x10a2f84: ldr s0, [x8, #0x78]
// 0x10a2f88: fmov s1, #25.00000000
// 0x10a2f8c: fcmp s0, s1
// 0x10a2f90: b.le #0x10a2fac
// 0x10a2f94: str wzr, [x19, #0xc0]
// 0x10a2f98: str wzr, [x19, #0xb8]
// 0x10a2f9c: b #0x10a2fa4
// 0x10a2fa0: str wzr, [x19, #0xc0]
// 0x10a2fa4: fmov s8, wzr
// 0x10a2fa8: b #0x10a2fbc
// 0x10a2fac: ldr x8, [x19, #0x30]
// 0x10a2fb0: cbz x8, #0x10a5704
// 0x10a2fb4: ldr s8, [x8, #0xdc]
// 0x10a2fb8: str s8, [x19, #0xc0]
// 0x10a2fbc: ldr x8, [x19, #0x28]
// 0x10a2fc0: cbz x8, #0x10a5704
// 0x10a2fc4: ldrb w8, [x8, #0x3ce]
// 0x10a2fc8: cbz w8, #0x10a2fd4
// 0x10a2fcc: fmov s8, wzr
// 0x10a2fd0: str xzr, [x19, #0xc0]
// 0x10a2fd4: ldr s9, [x19, #0xb8]
// 0x10a2fd8: mov x0, xzr
// 0x10a2fdc: bl #0x1b89b60
// 0x10a2fe0: ldr s1, [x19, #0xcc]
// 0x10a2fe4: fmov s10, #1.00000000
// 0x10a2fe8: fmov s11, wzr
// 0x10a2fec: fsub s2, s8, s9
// 0x10a2ff0: fmul s0, s0, s1
// 0x10a2ff4: fmin s1, s0, s10
// 0x10a2ff8: fcmp s0, #0.0
// 0x10a2ffc: ldr s8, [x19, #0xbc]
// 0x10a3000: fcsel s0, s1, s11, pl
// 0x10a3004: ldr s12, [x19, #0xc4]
// 0x10a3008: fmul s0, s2, s0
// 0x10a300c: fadd s0, s9, s0
// 0x10a3010: mov x0, xzr
// 0x10a3014: str s0, [x19, #0xb8]
// 0x10a3018: bl #0x1b89b60
// 0x10a301c: ldr s1, [x19, #0xc8]
// 0x10a3020: fmul s0, s0, s1
// 0x10a3024: fmin s1, s0, s10
// 0x10a3028: fcmp s0, #0.0
// 0x10a302c: fcsel s0, s1, s11, pl
// 0x10a3030: fsub s1, s12, s8
// 0x10a3034: fmul s0, s1, s0
// 0x10a3038: fadd s0, s8, s0
// 0x10a303c: str s0, [x19, #0xbc]
// 0x10a3040: ldrb w8, [x19, #0x256]
// 0x10a3044: cbz w8, #0x10a3050
// 0x10a3048: ldrb w8, [x19, #0x196]
// 0x10a304c: cbnz w8, #0x10a3070
// 0x10a3050: ldrb w8, [x19, #0x295]
// 0x10a3054: cbz w8, #0x10a3060
// 0x10a3058: ldrb w8, [x19, #0x195]
// 0x10a305c: cbnz w8, #0x10a3070
// 0x10a3060: ldrb w8, [x19, #0x198]
// 0x10a3064: cbz w8, #0x10a30b8
// 0x10a3068: ldrb w8, [x19, #0x197]
// 0x10a306c: cbz w8, #0x10a30b8
// 0x10a3070: ldrb w8, [x19, #0x1a1]
// 0x10a3074: mov w9, #1
// 0x10a3078: strb w9, [x19, #0x1a0]
// 0x10a307c: cbnz w8, #0x10a30c8
// 0x10a3080: ldr x8, [x19, #0x28]
// 0x10a3084: cbz x8, #0x10a5704
// 0x10a3088: ldr x8, [x8, #0x68]
// 0x10a308c: cbz x8, #0x10a5704
// 0x10a3090: strh wzr, [x8, #0x17c]
// 0x10a3094: strb wzr, [x8, #0x17e]
// 0x10a3098: ldr x0, [x20]
// 0x10a309c: cbz x0, #0x10a5704
// 0x10a30a0: mov w1, #1
// 0x10a30a4: mov x2, xzr
// 0x10a30a8: mov w21, #1
// 0x10a30ac: bl #0x10b35f8
// 0x10a30b0: strb w21, [x19, #0x1a1]
// 0x10a30b4: b #0x10a30c8
// 0x10a30b8: ldrb w8, [x19, #0x1a1]
// 0x10a30bc: cbz w8, #0x10a30c4
// 0x10a30c0: strb wzr, [x19, #0x1a1]
// 0x10a30c4: strb wzr, [x19, #0x1a0]
// 0x10a30c8: ldrb w8, [x19, #0x228]
// 0x10a30cc: add x25, x19, #0x17c
// 0x10a30d0: adrp x26, #0x832000
// 0x10a30d4: adrp x24, #0x832000
// 0x10a30d8: cbz w8, #0x10a31ec
// 0x10a30dc: ldr x0, [x19, #0x238]
// 0x10a30e0: cbz x0, #0x10a5704
// 0x10a30e4: mov x1, xzr
// 0x10a30e8: bl #0x1bcfd68
// 0x10a30ec: adrp x8, #0x832000
// 0x10a30f0: ldr s1, [x8, #0x434]
// 0x10a30f4: ldr x0, [x19, #0x60]
// 0x10a30f8: fmul s0, s0, s1
// 0x10a30fc: str s0, [x19, #0x1c0]
// 0x10a3100: cbz x0, #0x10a5704
// 0x10a3104: mov x1, xzr
// 0x10a3108: bl #0x1b9d508
// 0x10a310c: ldr x0, [x19, #0x60]
// 0x10a3110: cbz x0, #0x10a5704
// 0x10a3114: ldp s12, s13, [x19, #0x68]
// 0x10a3118: ldr s11, [x19, #0x70]
// 0x10a311c: mov x1, xzr
// 0x10a3120: mov v9.16b, v0.16b
// 0x10a3124: mov v10.16b, v1.16b
// 0x10a3128: mov v8.16b, v2.16b
// 0x10a312c: bl #0x1b9d508
// 0x10a3130: ldr x0, [x19, #0x238]
// 0x10a3134: cbz x0, #0x10a5704
// 0x10a3138: add x8, sp, #0x88
// 0x10a313c: mov x1, xzr
// 0x10a3140: mov v15.16b, v1.16b
// 0x10a3144: bl #0x1bcf9fc
// 0x10a3148: ldr x0, [x19, #0x238]
// 0x10a314c: cbz x0, #0x10a5704
// 0x10a3150: stp s13, s12, [sp, #0x54]
// 0x10a3154: ldr s12, [sp, #0x8c]
// 0x10a3158: ldr s13, [sp, #0x98]
// 0x10a315c: mov x1, xzr
// 0x10a3160: stp s8, s10, [sp, #0x5c]
// 0x10a3164: str s9, [sp, #0x70]
// 0x10a3168: bl #0x1bcfd68
// 0x10a316c: ldr x0, [x19, #0x60]
// 0x10a3170: cbz x0, #0x10a5704
// 0x10a3174: mov x1, xzr
// 0x10a3178: mov v8.16b, v0.16b
// 0x10a317c: bl #0x1b9d508
// 0x10a3180: ldr x0, [x19, #0x60]
// 0x10a3184: cbz x0, #0x10a5704
// 0x10a3188: mov v9.16b, v0.16b
// 0x10a318c: ldr s3, [x19, #0x68]
// 0x10a3190: ldr s0, [x19, #0x6c]
// 0x10a3194: mov x1, xzr
// 0x10a3198: mov v10.16b, v1.16b
// 0x10a319c: mov v14.16b, v2.16b
// 0x10a31a0: stp s0, s3, [sp, #0x48]
// 0x10a31a4: ldr s0, [x19, #0x70]
// 0x10a31a8: str s0, [sp, #0x50]
// 0x10a31ac: bl #0x1b9d508
// 0x10a31b0: ldr x0, [x19, #0x238]
// 0x10a31b4: str s1, [sp, #0x44]
// 0x10a31b8: cbz x0, #0x10a5704
// 0x10a31bc: add x8, sp, #0x88
// 0x10a31c0: mov x1, xzr
// 0x10a31c4: bl #0x1bcf9fc
// 0x10a31c8: ldrb w8, [x19, #0x2d0]
// 0x10a31cc: cbz w8, #0x10a3248
// 0x10a31d0: mov x0, xzr
// 0x10a31d4: bl #0x1b9ad30
// 0x10a31d8: adrp x8, #0x832000
// 0x10a31dc: ldr s1, [x8, #0x444]
// 0x10a31e0: fadd s0, s0, s1
// 0x10a31e4: str s0, [x19, #0x1bc]
// 0x10a31e8: b #0x10a38a0
// 0x10a31ec: ldrb w8, [x19, #0x280]
// 0x10a31f0: cbz w8, #0x10a3204
// 0x10a31f4: mov x0, xzr
// 0x10a31f8: bl #0x1b9ad30
// 0x10a31fc: str s0, [x19, #0x27c]
// 0x10a3200: strb wzr, [x19, #0x280]
// 0x10a3204: ldr x0, [x19, #0x60]
// 0x10a3208: cbz x0, #0x10a5704
// 0x10a320c: ldr s8, [x19, #0x28c]
// 0x10a3210: mov x1, xzr
// 0x10a3214: bl #0x1b9d508
// 0x10a3218: ldrb w8, [x19, #0x294]
// 0x10a321c: fsub s0, s8, s1
// 0x10a3220: str s0, [x19, #0x290]
// 0x10a3224: cbnz w8, #0x10a42b0
// 0x10a3228: ldr x0, [x19, #0x60]
// 0x10a322c: mov w8, #1
// 0x10a3230: strb w8, [x19, #0x294]
// 0x10a3234: cbz x0, #0x10a5704
// 0x10a3238: mov x1, xzr
// 0x10a323c: bl #0x1b9d508
// 0x10a3240: str s1, [x19, #0x28c]
// 0x10a3244: b #0x10a42b0
// 0x10a3248: ldr s1, [sp, #0x8c]
// 0x10a324c: ldr s0, [sp, #0x98]
// 0x10a3250: adrp x8, #0x832000
// 0x10a3254: adrp x27, #0x1fab000
// 0x10a3258: stp s14, s10, [sp, #0x38]
// 0x10a325c: stp s0, s1, [sp, #0x2c]
// 0x10a3260: ldr s0, [x19, #0x1b0]
// 0x10a3264: str s9, [sp, #0x40]
// 0x10a3268: ldr s14, [x19, #0x3e4]
// 0x10a326c: ldr s9, [x19, #0x3e8]
// 0x10a3270: str s0, [sp, #0x34]
// 0x10a3274: ldr s0, [x8, #0x47c]
// 0x10a3278: ldrb w8, [x27, #0x2c8]
// 0x10a327c: ldr s10, [x19, #0x3ec]
// 0x10a3280: fsub s1, s12, s13
// 0x10a3284: fsub s12, s15, s1
// 0x10a3288: fmul s8, s8, s0
// 0x10a328c: cbnz w8, #0x10a32a4
// 0x10a3290: adrp x0, #0x1e8c000
// 0x10a3294: ldr x0, [x0, #0xa60]
// 0x10a3298: bl #0xf7d92c
// 0x10a329c: mov w8, #1
// 0x10a32a0: strb w8, [x27, #0x2c8]
// 0x10a32a4: adrp x29, #0x1e8c000
// 0x10a32a8: ldr x29, [x29, #0xa60]
// 0x10a32ac: fadd s8, s12, s8
// 0x10a32b0: ldr x0, [x29]
// 0x10a32b4: ldr w8, [x0, #0xe0]
// 0x10a32b8: cbnz w8, #0x10a32c0
// 0x10a32bc: bl #0xf7da5c
// 0x10a32c0: ldr s0, [sp, #0x58]
// 0x10a32c4: adrp x8, #0x832000
// 0x10a32c8: fmul s1, s9, s9
// 0x10a32cc: ldr s2, [x8, #0x41c]
// 0x10a32d0: fmul s12, s0, s8
// 0x10a32d4: ldr s0, [sp, #0x54]
// 0x10a32d8: str s2, [sp, #0x54]
// 0x10a32dc: fmul s15, s0, s8
// 0x10a32e0: fmul s0, s14, s14
// 0x10a32e4: fadd s0, s0, s1
// 0x10a32e8: fmul s1, s10, s10
// 0x10a32ec: fadd s0, s1, s0
// 0x10a32f0: fsqrt s0, s0
// 0x10a32f4: fcmp s0, s2
// 0x10a32f8: fmul s8, s11, s8
// 0x10a32fc: b.le #0x10a3314
// 0x10a3300: fdiv s1, s14, s0
// 0x10a3304: str s1, [sp, #0x58]
// 0x10a3308: fdiv s11, s9, s0
// 0x10a330c: fdiv s9, s10, s0
// 0x10a3310: b #0x10a3350
// 0x10a3314: adrp x21, #0x1fab000
// 0x10a3318: ldrb w8, [x21, #0x2c9]
// 0x10a331c: cbnz w8, #0x10a3334
// 0x10a3320: adrp x0, #0x1e8c000
// 0x10a3324: ldr x0, [x0, #0x1e8]
// 0x10a3328: bl #0xf7d92c
// 0x10a332c: mov w8, #1
// 0x10a3330: strb w8, [x21, #0x2c9]
// 0x10a3334: adrp x8, #0x1e8c000
// 0x10a3338: ldr x8, [x8, #0x1e8]
// 0x10a333c: ldr x8, [x8]
// 0x10a3340: ldr x8, [x8, #0xb8]
// 0x10a3344: ldp s0, s11, [x8]
// 0x10a3348: ldr s9, [x8, #8]
// 0x10a334c: str s0, [sp, #0x58]
// 0x10a3350: ldr s0, [sp, #0x70]
// 0x10a3354: ldr s1, [sp, #0x60]
// 0x10a3358: ldr s10, [x19, #0x1c0]
// 0x10a335c: add x21, x19, #0x304
// 0x10a3360: fsub s13, s0, s12
// 0x10a3364: ldr s0, [sp, #0x5c]
// 0x10a3368: mov x0, x21
// 0x10a336c: mov x1, xzr
// 0x10a3370: fsub s14, s1, s15
// 0x10a3374: fsub s12, s0, s8
// 0x10a3378: add x22, x19, #0x1f4
// 0x10a337c: bl #0x1b95168
// 0x10a3380: adrp x28, #0x1e8d000
// 0x10a3384: ldr x28, [x28, #0x4a8]
// 0x10a3388: mov w23, w0
// 0x10a338c: ldr x8, [x28]
// 0x10a3390: ldr w9, [x8, #0xe0]
// 0x10a3394: cbnz w9, #0x10a33a0
// 0x10a3398: mov x0, x8
// 0x10a339c: bl #0xf7da5c
// 0x10a33a0: ldr s3, [sp, #0x58]
// 0x10a33a4: mov w2, #1
// 0x10a33a8: mov v0.16b, v13.16b
// 0x10a33ac: mov v1.16b, v14.16b
// 0x10a33b0: mov v2.16b, v12.16b
// 0x10a33b4: mov v4.16b, v11.16b
// 0x10a33b8: mov v5.16b, v9.16b
// 0x10a33bc: mov x0, x22
// 0x10a33c0: mov v6.16b, v10.16b
// 0x10a33c4: mov w1, w23
// 0x10a33c8: mov x3, xzr
// 0x10a33cc: bl #0x1bcb984
// 0x10a33d0: tbz w0, #0, #0x10a38a0
// 0x10a33d4: ldr s8, [x19, #0x1bc]
// 0x10a33d8: ldr s9, [x19, #0x1b8]
// 0x10a33dc: mov x0, xzr
// 0x10a33e0: bl #0x1b9ad30
// 0x10a33e4: fadd s1, s8, s9
// 0x10a33e8: fcmp s1, s0
// 0x10a33ec: b.pl #0x10a38a0
// 0x10a33f0: mov x0, x22
// 0x10a33f4: mov x1, xzr
// 0x10a33f8: bl #0x1bcee00
// 0x10a33fc: adrp x8, #0x1e8c000
// 0x10a3400: ldr x8, [x8, #0xd8]
// 0x10a3404: mov x23, x0
// 0x10a3408: ldr x8, [x8]
// 0x10a340c: ldr w9, [x8, #0xe0]
// 0x10a3410: cbnz w9, #0x10a341c
// 0x10a3414: mov x0, x8
// 0x10a3418: bl #0xf7da5c
// 0x10a341c: mov x0, x23
// 0x10a3420: mov x1, xzr
// 0x10a3424: bl #0x1b98274
// 0x10a3428: tbnz w0, #0, #0x10a38a0
// 0x10a342c: ldp s1, s0, [sp, #0x2c]
// 0x10a3430: ldr s11, [x19, #0x3e4]
// 0x10a3434: ldr s12, [x19, #0x3e8]
// 0x10a3438: ldrb w8, [x27, #0x2c8]
// 0x10a343c: fsub s0, s0, s1
// 0x10a3440: ldr s1, [sp, #0x44]
// 0x10a3444: ldr s13, [x19, #0x3ec]
// 0x10a3448: fsub s8, s1, s0
// 0x10a344c: cbnz w8, #0x10a3464
// 0x10a3450: adrp x0, #0x1e8c000
// 0x10a3454: ldr x0, [x0, #0xa60]
// 0x10a3458: bl #0xf7d92c
// 0x10a345c: mov w8, #1
// 0x10a3460: strb w8, [x27, #0x2c8]
// 0x10a3464: ldr x0, [x29]
// 0x10a3468: ldr s0, [sp, #0x34]
// 0x10a346c: ldr w8, [x0, #0xe0]
// 0x10a3470: fsub s10, s8, s0
// 0x10a3474: cbnz w8, #0x10a347c
// 0x10a3478: bl #0xf7da5c
// 0x10a347c: ldr s0, [sp, #0x4c]
// 0x10a3480: fmul s1, s12, s12
// 0x10a3484: fmul s8, s0, s10
// 0x10a3488: ldr s0, [sp, #0x48]
// 0x10a348c: fmul s9, s0, s10
// 0x10a3490: fmul s0, s11, s11
// 0x10a3494: fadd s0, s0, s1
// 0x10a3498: fmul s1, s13, s13
// 0x10a349c: fadd s0, s1, s0
// 0x10a34a0: ldr s1, [sp, #0x54]
// 0x10a34a4: fsqrt s0, s0
// 0x10a34a8: fcmp s0, s1
// 0x10a34ac: ldr s1, [sp, #0x50]
// 0x10a34b0: fmul s10, s1, s10
// 0x10a34b4: b.le #0x10a3518
// 0x10a34b8: fdiv s11, s11, s0
// 0x10a34bc: fdiv s12, s12, s0
// 0x10a34c0: fdiv s13, s13, s0
// 0x10a34c4: b #0x10a3550
// 0x10a34c8: ldr x8, [x19, #0x30]
// 0x10a34cc: cbz x8, #0x10a5704
// 0x10a34d0: ldr s0, [x8, #0xc8]
// 0x10a34d4: ldr s1, [x8, #0xe0]
// 0x10a34d8: fneg s0, s0
// 0x10a34dc: fcmp s1, s0
// 0x10a34e0: fmov s0, wzr
// 0x10a34e4: b.pl #0x10a350c
// 0x10a34e8: ldrb w8, [x19, #0x2dc]
// 0x10a34ec: cbz w8, #0x10a3508
// 0x10a34f0: ldr x8, [x19, #0x20]
// 0x10a34f4: cbz x8, #0x10a5704
// 0x10a34f8: ldr s2, [x8, #0x78]
// 0x10a34fc: fmov s3, #25.00000000
// 0x10a3500: fcmp s2, s3
// 0x10a3504: b.gt #0x10a350c
// 0x10a3508: mov v0.16b, v1.16b
// 0x10a350c: mov w8, #0x43000000
// 0x10a3510: str s0, [x19, #0xc4]
// 0x10a3514: b #0x10a2e4c
// 0x10a3518: adrp x23, #0x1fab000
// 0x10a351c: ldrb w8, [x23, #0x2c9]
// 0x10a3520: cbnz w8, #0x10a3538
// 0x10a3524: adrp x0, #0x1e8c000
// 0x10a3528: ldr x0, [x0, #0x1e8]
// 0x10a352c: bl #0xf7d92c
// 0x10a3530: mov w8, #1
// 0x10a3534: strb w8, [x23, #0x2c9]
// 0x10a3538: adrp x8, #0x1e8c000
// 0x10a353c: ldr x8, [x8, #0x1e8]
// 0x10a3540: ldr x8, [x8]
// 0x10a3544: ldr x8, [x8, #0xb8]
// 0x10a3548: ldp s11, s12, [x8]
// 0x10a354c: ldr s13, [x8, #8]
// 0x10a3550: ldr s0, [sp, #0x40]
// 0x10a3554: ldr s14, [x19, #0x1c0]
// 0x10a3558: mov x0, x21
// 0x10a355c: mov x1, xzr
// 0x10a3560: fsub s8, s0, s8
// 0x10a3564: ldr s0, [sp, #0x3c]
// 0x10a3568: fsub s9, s0, s9
// 0x10a356c: ldr s0, [sp, #0x38]
// 0x10a3570: fsub s10, s0, s10
// 0x10a3574: bl #0x1b95168
// 0x10a3578: ldr x8, [x28]
// 0x10a357c: mov w23, w0
// 0x10a3580: ldr w9, [x8, #0xe0]
// 0x10a3584: cbnz w9, #0x10a3590
// 0x10a3588: mov x0, x8
// 0x10a358c: bl #0xf7da5c
// 0x10a3590: mov w1, #1
// 0x10a3594: mov v0.16b, v8.16b
// 0x10a3598: mov v1.16b, v9.16b
// 0x10a359c: mov v2.16b, v10.16b
// 0x10a35a0: mov v3.16b, v11.16b
// 0x10a35a4: mov v4.16b, v12.16b
// 0x10a35a8: mov v5.16b, v13.16b
// 0x10a35ac: mov v6.16b, v14.16b
// 0x10a35b0: mov w0, w23
// 0x10a35b4: mov x2, xzr
// 0x10a35b8: str s8, [sp, #0x70]
// 0x10a35bc: bl #0x1bcb498
// 0x10a35c0: tbnz w0, #0, #0x10a38a0
// 0x10a35c4: mov x0, x22
// 0x10a35c8: mov x1, xzr
// 0x10a35cc: stp s10, s9, [sp, #0x5c]
// 0x10a35d0: bl #0x1bced10
// 0x10a35d4: adrp x22, #0x1fab000
// 0x10a35d8: ldp s14, s15, [x19, #0x74]
// 0x10a35dc: ldrb w8, [x22, #0x3e2]
// 0x10a35e0: ldr s8, [x19, #0x7c]
// 0x10a35e4: mov v11.16b, v0.16b
// 0x10a35e8: mov v12.16b, v1.16b
// 0x10a35ec: mov v13.16b, v2.16b
// 0x10a35f0: cbnz w8, #0x10a3608
// 0x10a35f4: adrp x0, #0x1e8c000
// 0x10a35f8: ldr x0, [x0, #0xa60]
// 0x10a35fc: bl #0xf7d92c
// 0x10a3600: mov w8, #1
// 0x10a3604: strb w8, [x22, #0x3e2]
// 0x10a3608: ldr x0, [x29]
// 0x10a360c: fmul s0, s11, s11
// 0x10a3610: fmul s1, s12, s12
// 0x10a3614: fadd s0, s0, s1
// 0x10a3618: fmul s1, s13, s13
// 0x10a361c: ldr w8, [x0, #0xe0]
// 0x10a3620: fadd s9, s1, s0
// 0x10a3624: fmul s0, s14, s14
// 0x10a3628: fmul s1, s15, s15
// 0x10a362c: fadd s0, s0, s1
// 0x10a3630: fmul s1, s8, s8
// 0x10a3634: fadd s10, s1, s0
// 0x10a3638: cbnz w8, #0x10a3640
// 0x10a363c: bl #0xf7da5c
// 0x10a3640: adrp x8, #0x832000
// 0x10a3644: ldr s1, [x8, #0x344]
// 0x10a3648: fmul s0, s9, s10
// 0x10a364c: ldp s10, s9, [sp, #0x5c]
// 0x10a3650: fsqrt s0, s0
// 0x10a3654: fcmp s0, s1
// 0x10a3658: b.mi #0x10a38a0
// 0x10a365c: ldr x0, [x29]
// 0x10a3660: fmul s1, s11, s14
// 0x10a3664: fmul s2, s12, s15
// 0x10a3668: fmul s3, s13, s8
// 0x10a366c: fadd s1, s1, s2
// 0x10a3670: fadd s1, s3, s1
// 0x10a3674: ldr w8, [x0, #0xe0]
// 0x10a3678: fdiv s0, s1, s0
// 0x10a367c: fmov s1, #1.00000000
// 0x10a3680: fmov s2, #-1.00000000
// 0x10a3684: fmin s1, s0, s1
// 0x10a3688: fcmp s0, s2
// 0x10a368c: fcsel s8, s1, s2, pl
// 0x10a3690: cbnz w8, #0x10a3698
// 0x10a3694: bl #0xf7da5c
// 0x10a3698: fcvt d0, s8
// 0x10a369c: bl #0x1db0ca0
// 0x10a36a0: adrp x8, #0x832000
// 0x10a36a4: ldr s1, [x8, #0x554]
// 0x10a36a8: fcvt s0, d0
// 0x10a36ac: mov w8, #0x42aa0000
// 0x10a36b0: fmul s0, s0, s1
// 0x10a36b4: fmov s1, w8
// 0x10a36b8: fcmp s0, s1
// 0x10a36bc: b.le #0x10a38a0
// 0x10a36c0: ldr s8, [x19, #0x3e4]
// 0x10a36c4: ldr s11, [x19, #0x3e8]
// 0x10a36c8: ldrb w8, [x27, #0x2c8]
// 0x10a36cc: ldr s12, [x19, #0x3ec]
// 0x10a36d0: cbnz w8, #0x10a36e8
// 0x10a36d4: adrp x0, #0x1e8c000
// 0x10a36d8: ldr x0, [x0, #0xa60]
// 0x10a36dc: bl #0xf7d92c
// 0x10a36e0: mov w8, #1
// 0x10a36e4: strb w8, [x27, #0x2c8]
// 0x10a36e8: ldr x0, [x29]
// 0x10a36ec: ldr w8, [x0, #0xe0]
// 0x10a36f0: cbnz w8, #0x10a36f8
// 0x10a36f4: bl #0xf7da5c
// 0x10a36f8: fmul s0, s8, s8
// 0x10a36fc: fmul s1, s11, s11
// 0x10a3700: fadd s0, s0, s1
// 0x10a3704: fmul s1, s12, s12
// 0x10a3708: fadd s0, s1, s0
// 0x10a370c: fsqrt s2, s0
// 0x10a3710: ldr s0, [sp, #0x54]
// 0x10a3714: fcmp s2, s0
// 0x10a3718: b.le #0x10a372c
// 0x10a371c: fdiv s0, s8, s2
// 0x10a3720: fdiv s1, s11, s2
// 0x10a3724: fdiv s2, s12, s2
// 0x10a3728: b #0x10a3764
// 0x10a372c: adrp x22, #0x1fab000
// 0x10a3730: ldrb w8, [x22, #0x2c9]
// 0x10a3734: cbnz w8, #0x10a374c
// 0x10a3738: adrp x0, #0x1e8c000
// 0x10a373c: ldr x0, [x0, #0x1e8]
// 0x10a3740: bl #0xf7d92c
// 0x10a3744: mov w8, #1
// 0x10a3748: strb w8, [x22, #0x2c9]
// 0x10a374c: adrp x8, #0x1e8c000
// 0x10a3750: ldr x8, [x8, #0x1e8]
// 0x10a3754: ldr x8, [x8]
// 0x10a3758: ldr x8, [x8, #0xb8]
// 0x10a375c: ldp s0, s1, [x8]
// 0x10a3760: ldr s2, [x8, #8]
// 0x10a3764: ldr s3, [x19, #0x1c0]
// 0x10a3768: ldr s7, [sp, #0x70]
// 0x10a376c: ldp s4, s5, [x19, #0x74]
// 0x10a3770: ldr s6, [x19, #0x7c]
// 0x10a3774: ldr s11, [x19, #0x1b0]
// 0x10a3778: fmul s0, s0, s3
// 0x10a377c: fmul s1, s1, s3
// 0x10a3780: fmul s2, s2, s3
// 0x10a3784: mov x0, x21
// 0x10a3788: mov x1, xzr
// 0x10a378c: fneg s12, s4
// 0x10a3790: fneg s13, s5
// 0x10a3794: fneg s14, s6
// 0x10a3798: fadd s8, s7, s0
// 0x10a379c: fadd s9, s9, s1
// 0x10a37a0: fadd s10, s10, s2
// 0x10a37a4: add x22, x19, #0x1c8
// 0x10a37a8: bl #0x1b95168
// 0x10a37ac: ldr x8, [x28]
// 0x10a37b0: mov w21, w0
// 0x10a37b4: ldr w9, [x8, #0xe0]
// 0x10a37b8: cbnz w9, #0x10a37c4
// 0x10a37bc: mov x0, x8
// 0x10a37c0: bl #0xf7da5c
// 0x10a37c4: mov w2, #1
// 0x10a37c8: mov v0.16b, v8.16b
// 0x10a37cc: mov v1.16b, v9.16b
// 0x10a37d0: mov v2.16b, v10.16b
// 0x10a37d4: mov v3.16b, v12.16b
// 0x10a37d8: mov v4.16b, v13.16b
// 0x10a37dc: mov v5.16b, v14.16b
// 0x10a37e0: mov x0, x22
// 0x10a37e4: mov v6.16b, v11.16b
// 0x10a37e8: mov w1, w21
// 0x10a37ec: mov x3, xzr
// 0x10a37f0: bl #0x1bcb984
// 0x10a37f4: ldr s9, [x19, #0x1b0]
// 0x10a37f8: mov x0, x22
// 0x10a37fc: mov x1, xzr
// 0x10a3800: bl #0x1bced1c
// 0x10a3804: ldr x0, [x19, #0x238]
// 0x10a3808: cbz x0, #0x10a5704
// 0x10a380c: mov x1, xzr
// 0x10a3810: mov v8.16b, v0.16b
// 0x10a3814: bl #0x1bcfd68
// 0x10a3818: ldr s1, [x24, #0x3bc]
// 0x10a381c: fsub s2, s9, s8
// 0x10a3820: fmul s0, s0, s1
// 0x10a3824: fcmp s2, s0
// 0x10a3828: b.le #0x10a38a0
// 0x10a382c: ldr x0, [x19, #0x60]
// 0x10a3830: cbz x0, #0x10a5704
// 0x10a3834: mov x1, xzr
// 0x10a3838: bl #0x1b9d508
// 0x10a383c: ldp s11, s12, [x19, #0x68]
// 0x10a3840: ldr s13, [x19, #0x70]
// 0x10a3844: ldr s14, [x19, #0x1b0]
// 0x10a3848: mov x0, x22
// 0x10a384c: mov x1, xzr
// 0x10a3850: mov v8.16b, v0.16b
// 0x10a3854: mov v9.16b, v1.16b
// 0x10a3858: mov v10.16b, v2.16b
// 0x10a385c: bl #0x1bced1c
// 0x10a3860: ldr x0, [x19, #0x60]
// 0x10a3864: cbz x0, #0x10a5704
// 0x10a3868: fsub s0, s14, s0
// 0x10a386c: fmov s1, #0.50000000
// 0x10a3870: fmul s0, s0, s1
// 0x10a3874: fmul s1, s13, s0
// 0x10a3878: fmul s3, s12, s0
// 0x10a387c: fmul s0, s11, s0
// 0x10a3880: fadd s2, s10, s1
// 0x10a3884: fadd s1, s9, s3
// 0x10a3888: fadd s0, s8, s0
// 0x10a388c: mov x1, xzr
// 0x10a3890: bl #0x1b9d5a8
// 0x10a3894: mov x0, xzr
// 0x10a3898: bl #0x1b9ad30
// 0x10a389c: b #0x10a31e4
// 0x10a38a0: ldr s8, [x19, #0x1bc]
// 0x10a38a4: mov x0, xzr
// 0x10a38a8: bl #0x1b9ad30
// 0x10a38ac: ldr x8, [x19, #0x28]
// 0x10a38b0: cbz x8, #0x10a5704
// 0x10a38b4: adrp x9, #0x832000
// 0x10a38b8: ldr s1, [x9, #0x550]
// 0x10a38bc: ldr x8, [x8, #0x98]
// 0x10a38c0: fadd s1, s8, s1
// 0x10a38c4: fcmp s1, s0
// 0x10a38c8: b.pl #0x10a38d8
// 0x10a38cc: cbz x8, #0x10a5704
// 0x10a38d0: ldr s0, [x19, #0x1c4]
// 0x10a38d4: b #0x10a38e4
// 0x10a38d8: cbz x8, #0x10a5704
// 0x10a38dc: adrp x9, #0x832000
// 0x10a38e0: ldr s0, [x9, #0x34c]
// 0x10a38e4: str s0, [x8, #0x114]
// 0x10a38e8: ldrb w8, [x19, #0x294]
// 0x10a38ec: mov w9, #1
// 0x10a38f0: strb w9, [x19, #0x280]
// 0x10a38f4: cbz w8, #0x10a3a44
// 0x10a38f8: mov x0, xzr
// 0x10a38fc: str wzr, [x19, #0x290]
// 0x10a3900: bl #0x1b9ad30
// 0x10a3904: ldr x0, [x19, #0x60]
// 0x10a3908: str s0, [x19, #0x2ac]
// 0x10a390c: cbz x0, #0x10a5704
// 0x10a3910: ldr s8, [x19, #0x28c]
// 0x10a3914: mov x1, xzr
// 0x10a3918: bl #0x1b9d508
// 0x10a391c: fsub s0, s8, s1
// 0x10a3920: fmov s1, #2.00000000
// 0x10a3924: fcmp s0, s1
// 0x10a3928: b.le #0x10a39f8
// 0x10a392c: ldrb w8, [x19, #0x255]
// 0x10a3930: cbnz w8, #0x10a39c8
// 0x10a3934: adrp x8, #0x1e8c000
// 0x10a3938: ldr x8, [x8, #0xd8]
// 0x10a393c: ldr x21, [x19, #0x2f8]
// 0x10a3940: ldr x0, [x8]
// 0x10a3944: ldr w8, [x0, #0xe0]
// 0x10a3948: cbnz w8, #0x10a3950
// 0x10a394c: bl #0xf7da5c
// 0x10a3950: mov x0, x21
// 0x10a3954: mov x1, xzr
// 0x10a3958: bl #0x1b98274
// 0x10a395c: tbz w0, #0, #0x10a39c8
// 0x10a3960: ldrb w8, [x19, #0x300]
// 0x10a3964: cbnz w8, #0x10a39c8
// 0x10a3968: ldr x0, [x19, #0x80]
// 0x10a396c: cbz x0, #0x10a5704
// 0x10a3970: ldr x21, [x19, #0x2f8]
// 0x10a3974: mov x1, xzr
// 0x10a3978: bl #0x1b9d508
// 0x10a397c: mov w8, #0x43fa0000
// 0x10a3980: fmov s3, #1.00000000
// 0x10a3984: fmov s4, wzr
// 0x10a3988: fmov s5, #1.00000000
// 0x10a398c: fmov s6, #1.00000000
// 0x10a3990: fmov s7, w8
// 0x10a3994: mov x0, x21
// 0x10a3998: mov x1, xzr
// 0x10a399c: bl #0x108d260
// 0x10a39a0: ldr x8, [x19, #0x28]
// 0x10a39a4: cbz x8, #0x10a5704
// 0x10a39a8: ldr x8, [x8, #0x50]
// 0x10a39ac: cbz x8, #0x10a5704
// 0x10a39b0: ldr x0, [x8, #0x60]
// 0x10a39b4: cbz x0, #0x10a5704
// 0x10a39b8: mov x1, xzr
// 0x10a39bc: bl #0x10bf7e4
// 0x10a39c0: mov w8, #1
// 0x10a39c4: strb w8, [x19, #0x300]
// 0x10a39c8: ldr x0, [x19, #0x88]
// 0x10a39cc: cbz x0, #0x10a5704
// 0x10a39d0: fmov s0, #1.00000000
// 0x10a39d4: mov x1, xzr
// 0x10a39d8: bl #0x1b67eb4
// 0x10a39dc: ldr x0, [x19, #0x88]
// 0x10a39e0: cbz x0, #0x10a5704
// 0x10a39e4: adrp x8, #0x1e8e000
// 0x10a39e8: ldr x8, [x8, #0x388]
// 0x10a39ec: mov x2, xzr
// 0x10a39f0: ldr x1, [x8]
// 0x10a39f4: bl #0x1b67884
// 0x10a39f8: ldr x0, [x19, #0x60]
// 0x10a39fc: cbz x0, #0x10a5704
// 0x10a3a00: mov x1, xzr
// 0x10a3a04: bl #0x1b9d508
// 0x10a3a08: ldr s8, [x19, #0x28c]
// 0x10a3a0c: ldr s0, [x19, #0x284]
// 0x10a3a10: fsub s0, s8, s0
// 0x10a3a14: fcmp s1, s0
// 0x10a3a18: b.pl #0x10a3a40
// 0x10a3a1c: ldrb w8, [x19, #0x255]
// 0x10a3a20: cbnz w8, #0x10a3a40
// 0x10a3a24: ldr x0, [x19, #0x60]
// 0x10a3a28: cbz x0, #0x10a5704
// 0x10a3a2c: mov x1, xzr
// 0x10a3a30: bl #0x1b9d508
// 0x10a3a34: fsub s0, s8, s1
// 0x10a3a38: mov x0, x19
// 0x10a3a3c: bl #0x10a5708
// 0x10a3a40: strb wzr, [x19, #0x294]
// 0x10a3a44: ldrb w8, [x19, #0x124]
// 0x10a3a48: cbz w8, #0x10a3b3c
// 0x10a3a4c: ldr s0, [x19, #0xc4]
// 0x10a3a50: fcmp s0, #0.0
// 0x10a3a54: b.mi #0x10a3a94
// 0x10a3a58: b.gt #0x10a3a94
// 0x10a3a5c: ldrb w8, [x19, #0x146]
// 0x10a3a60: cbz w8, #0x10a3a78
// 0x10a3a64: ldr x8, [x19, #0x30]
// 0x10a3a68: cbz x8, #0x10a5704
// 0x10a3a6c: ldrb w8, [x8, #0x91]
// 0x10a3a70: cbnz w8, #0x10a3b3c
// 0x10a3a74: b #0x10a3b38
// 0x10a3a78: ldr s1, [x19, #0xc0]
// 0x10a3a7c: fcmp s1, #0.0
// 0x10a3a80: b.mi #0x10a3a94
// 0x10a3a84: b.gt #0x10a3a94
// 0x10a3a88: fcmp s0, #0.0
// 0x10a3a8c: b.eq #0x10a3a64
// 0x10a3a90: b.vs #0x10a3a64
// 0x10a3a94: ldr x8, [x19, #0x30]
// 0x10a3a98: cbz x8, #0x10a5704
// 0x10a3a9c: ldrb w8, [x8, #0x91]
// 0x10a3aa0: cbz w8, #0x10a3af8
// 0x10a3aa4: ldrb w8, [x19, #0x2c1]
// 0x10a3aa8: cbnz w8, #0x10a3b3c
// 0x10a3aac: mov x0, xzr
// 0x10a3ab0: bl #0x1b9ad30
// 0x10a3ab4: ldr s9, [x19, #0x2bc]
// 0x10a3ab8: ldr s10, [x19, #0x12c]
// 0x10a3abc: mov w8, #0x100
// 0x10a3ac0: mov x0, xzr
// 0x10a3ac4: mov v8.16b, v0.16b
// 0x10a3ac8: str s0, [x19, #0x2b8]
// 0x10a3acc: strh w8, [x19, #0x2c0]
// 0x10a3ad0: bl #0x1b9ae58
// 0x10a3ad4: fsub s1, s9, s8
// 0x10a3ad8: fmul s0, s10, s0
// 0x10a3adc: fcmp s1, s0
// 0x10a3ae0: b.pl #0x10a3b3c
// 0x10a3ae4: ldrb w8, [x19, #0x2b1]
// 0x10a3ae8: cbnz w8, #0x10a3b38
// 0x10a3aec: mov w8, #1
// 0x10a3af0: strb w8, [x19, #0x2b1]
// 0x10a3af4: b #0x10a3b3c
// 0x10a3af8: ldrb w8, [x19, #0x2c0]
// 0x10a3afc: cbnz w8, #0x10a3b3c
// 0x10a3b00: mov x0, xzr
// 0x10a3b04: bl #0x1b9ad30
// 0x10a3b08: ldr s9, [x19, #0x2b8]
// 0x10a3b0c: ldr s10, [x19, #0x12c]
// 0x10a3b10: mov w8, #1
// 0x10a3b14: mov x0, xzr
// 0x10a3b18: mov v8.16b, v0.16b
// 0x10a3b1c: str s0, [x19, #0x2bc]
// 0x10a3b20: strh w8, [x19, #0x2c0]
// 0x10a3b24: bl #0x1b9ae58
// 0x10a3b28: fsub s1, s8, s9
// 0x10a3b2c: fmul s0, s10, s0
// 0x10a3b30: fcmp s1, s0
// 0x10a3b34: b.le #0x10a3b3c
// 0x10a3b38: strb wzr, [x19, #0x2b1]
// 0x10a3b3c: ldrb w8, [x19, #0x2b1]
// 0x10a3b40: cbz w8, #0x10a3b6c
// 0x10a3b44: ldr x9, [x19, #0x30]
// 0x10a3b48: cbz x9, #0x10a5704
// 0x10a3b4c: ldrb w10, [x9, #0x89]
// 0x10a3b50: cbnz w10, #0x10a3c60
// 0x10a3b54: ldrb w9, [x9, #0x92]
// 0x10a3b58: cbz w9, #0x10a3b6c
// 0x10a3b5c: ldr x9, [x20]
// 0x10a3b60: cbz x9, #0x10a5704
// 0x10a3b64: ldrb w9, [x9, #0x238]
// 0x10a3b68: cbnz w9, #0x10a3c60
// 0x10a3b6c: ldr x9, [x19, #0x28]
// 0x10a3b70: cbz x9, #0x10a5704
// 0x10a3b74: ldrb w9, [x9, #0x2d0]
// 0x10a3b78: cbz w9, #0x10a3b8c
// 0x10a3b7c: ldr x9, [x19, #0x30]
// 0x10a3b80: cbz x9, #0x10a5704
// 0x10a3b84: ldrb w9, [x9, #0x89]
// 0x10a3b88: cbnz w9, #0x10a3c60
// 0x10a3b8c: ldr s0, [x19, #0xc4]
// 0x10a3b90: fcmp s0, #0.0
// 0x10a3b94: b.ls #0x10a3c48
// 0x10a3b98: ldr x9, [x19, #0x30]
// 0x10a3b9c: cbz x9, #0x10a5704
// 0x10a3ba0: ldr s1, [x9, #0xe0]
// 0x10a3ba4: fcmp s1, #0.0
// 0x10a3ba8: b.hi #0x10a3bb4
// 0x10a3bac: ldrb w10, [x19, #0x146]
// 0x10a3bb0: cbnz w10, #0x10a3c60
// 0x10a3bb4: fcmp s0, #0.0
// 0x10a3bb8: b.pl #0x10a3bc4
// 0x10a3bbc: ldrb w10, [x19, #0x146]
// 0x10a3bc0: cbnz w10, #0x10a3c60
// 0x10a3bc4: ldrb w10, [x19, #0x2a0]
// 0x10a3bc8: cbz w10, #0x10a3bd4
// 0x10a3bcc: ldrb w10, [x19, #0x148]
// 0x10a3bd0: cbnz w10, #0x10a3c60
// 0x10a3bd4: ldrb w10, [x19, #0x258]
// 0x10a3bd8: cbnz w10, #0x10a3c60
// 0x10a3bdc: ldrb w10, [x19, #0x295]
// 0x10a3be0: cbnz w10, #0x10a3c60
// 0x10a3be4: ldr x0, [x20]
// 0x10a3be8: cbz x0, #0x10a5704
// 0x10a3bec: ldrb w10, [x0, #0x229]
// 0x10a3bf0: cbnz w10, #0x10a3c60
// 0x10a3bf4: ldrb w10, [x19, #0x130]
// 0x10a3bf8: cbz w10, #0x10a3c08
// 0x10a3bfc: ldr s0, [x19, #0x140]
// 0x10a3c00: fcmp s0, #0.0
// 0x10a3c04: b.ls #0x10a3c60
// 0x10a3c08: cbz w8, #0x10a3c6c
// 0x10a3c0c: ldrb w8, [x9, #0x8b]
// 0x10a3c10: cbz w8, #0x10a3c6c
// 0x10a3c14: ldrb w8, [x19, #0x147]
// 0x10a3c18: cbnz w8, #0x10a3c6c
// 0x10a3c1c: mov x1, xzr
// 0x10a3c20: bl #0x10ba3b0
// 0x10a3c24: tbz w0, #0, #0x10a3c6c
// 0x10a3c28: ldr x0, [x19, #0x40]
// 0x10a3c2c: mov w8, #1
// 0x10a3c30: strb w8, [x19, #0x2c2]
// 0x10a3c34: strb wzr, [x19, #0x2b1]
// 0x10a3c38: cbz x0, #0x10a5704
// 0x10a3c3c: mov x1, xzr
// 0x10a3c40: bl #0x10ba3b0
// 0x10a3c44: b #0x10a3c6c
// 0x10a3c48: ldr s1, [x19, #0xc0]
// 0x10a3c4c: fcmp s1, #0.0
// 0x10a3c50: b.eq #0x10a3b98
// 0x10a3c54: b.vs #0x10a3b98
// 0x10a3c58: ldrb w9, [x19, #0x146]
// 0x10a3c5c: cbz w9, #0x10a3b98
// 0x10a3c60: mov w8, #1
// 0x10a3c64: strb w8, [x19, #0x2c2]
// 0x10a3c68: strb wzr, [x19, #0x2b1]
// 0x10a3c6c: ldrb w8, [x19, #0x130]
// 0x10a3c70: cbz w8, #0x10a3d0c
// 0x10a3c74: ldr s0, [x19, #0x140]
// 0x10a3c78: fcmp s0, #0.0
// 0x10a3c7c: b.hi #0x10a3d0c
// 0x10a3c80: ldrb w8, [x19, #0x138]
// 0x10a3c84: cbnz w8, #0x10a3d0c
// 0x10a3c88: ldr x8, [x19, #0x28]
// 0x10a3c8c: cbz x8, #0x10a5704
// 0x10a3c90: adrp x9, #0x1e8c000
// 0x10a3c94: ldr x9, [x9, #0xd8]
// 0x10a3c98: ldr x20, [x8, #0x3f0]
// 0x10a3c9c: ldr x0, [x9]
// 0x10a3ca0: ldr w9, [x0, #0xe0]
// 0x10a3ca4: cbnz w9, #0x10a3cac
// 0x10a3ca8: bl #0xf7da5c
// 0x10a3cac: mov x0, x20
// 0x10a3cb0: mov x1, xzr
// 0x10a3cb4: bl #0x1b98274
// 0x10a3cb8: tbz w0, #0, #0x10a3d0c
// 0x10a3cbc: ldrb w8, [x19, #0x144]
// 0x10a3cc0: cbz w8, #0x10a3d0c
// 0x10a3cc4: ldr x8, [x19, #0x28]
// 0x10a3cc8: cbz x8, #0x10a5704
// 0x10a3ccc: ldr x0, [x19, #0x80]
// 0x10a3cd0: cbz x0, #0x10a5704
// 0x10a3cd4: ldr x20, [x8, #0x3f0]
// 0x10a3cd8: mov x1, xzr
// 0x10a3cdc: bl #0x1b9d508
// 0x10a3ce0: mov w8, #0x43fa0000
// 0x10a3ce4: fmov s3, #1.00000000
// 0x10a3ce8: fmov s4, wzr
// 0x10a3cec: fmov s5, #1.00000000
// 0x10a3cf0: fmov s6, #1.00000000
// 0x10a3cf4: fmov s7, w8
// 0x10a3cf8: mov x0, x20
// 0x10a3cfc: mov x1, xzr
// 0x10a3d00: bl #0x108d260
// 0x10a3d04: mov w8, #1
// 0x10a3d08: strb w8, [x19, #0x138]
// 0x10a3d0c: ldrb w9, [x19, #0x2b1]
// 0x10a3d10: cbz w9, #0x10a3dd4
// 0x10a3d14: ldrb w8, [x19, #0x130]
// 0x10a3d18: cbz w8, #0x10a3d30
// 0x10a3d1c: ldr s0, [x19, #0x140]
// 0x10a3d20: fcmp s0, #0.0
// 0x10a3d24: b.hi #0x10a3d30
// 0x10a3d28: mov w10, #1
// 0x10a3d2c: strb w10, [x19, #0x145]
// 0x10a3d30: ldr s0, [x19, #0xc4]
// 0x10a3d34: fcmp s0, #0.0
// 0x10a3d38: b.le #0x10a3d4c
// 0x10a3d3c: ldrb w10, [x19, #0x146]
// 0x10a3d40: cbz w10, #0x10a3d4c
// 0x10a3d44: cbnz w9, #0x10a3d60
// 0x10a3d48: b #0x10a3d78
// 0x10a3d4c: ldrb w10, [x19, #0x2e8]
// 0x10a3d50: cbz w10, #0x10a3d78
// 0x10a3d54: cbz w9, #0x10a3d78
// 0x10a3d58: ldrb w9, [x19, #0x146]
// 0x10a3d5c: cbnz w9, #0x10a3d78
// 0x10a3d60: ldrb w9, [x19, #0x2d0]
// 0x10a3d64: cbnz w9, #0x10a3d78
// 0x10a3d68: ldrb w9, [x19, #0x2dc]
// 0x10a3d6c: cbnz w9, #0x10a3d78
// 0x10a3d70: ldrb w9, [x19, #0x2c2]
// 0x10a3d74: cbz w9, #0x10a51d8
// 0x10a3d78: ldrb w9, [x19, #0x2c8]
// 0x10a3d7c: cbz w9, #0x10a3d94
// 0x10a3d80: mov x0, xzr
// 0x10a3d84: bl #0x1b9ad30
// 0x10a3d88: ldrb w8, [x19, #0x130]
// 0x10a3d8c: str s0, [x19, #0x2c4]
// 0x10a3d90: strb wzr, [x19, #0x2c8]
// 0x10a3d94: strb wzr, [x19, #0x2b0]
// 0x10a3d98: cbz w8, #0x10a3e3c
// 0x10a3d9c: ldrb w8, [x19, #0x131]
// 0x10a3da0: cbz w8, #0x10a3df4
// 0x10a3da4: ldrb w8, [x19, #0x145]
// 0x10a3da8: cbz w8, #0x10a3e1c
// 0x10a3dac: ldr s8, [x19, #0x2c4]
// 0x10a3db0: ldr s9, [x19, #0x134]
// 0x10a3db4: mov x0, xzr
// 0x10a3db8: bl #0x1b9ad30
// 0x10a3dbc: fadd s1, s8, s9
// 0x10a3dc0: fcmp s1, s0
// 0x10a3dc4: b.pl #0x10a3e3c
// 0x10a3dc8: ldr s0, [x19, #0x13c]
// 0x10a3dcc: strb wzr, [x19, #0x145]
// 0x10a3dd0: b #0x10a3e10
// 0x10a3dd4: ldrb w8, [x19, #0x2c2]
// 0x10a3dd8: cbz w8, #0x10a3d14
// 0x10a3ddc: ldr x8, [x19, #0x30]
// 0x10a3de0: cbz x8, #0x10a5704
// 0x10a3de4: ldrb w8, [x8, #0x92]
// 0x10a3de8: cbnz w8, #0x10a3d14
// 0x10a3dec: strb wzr, [x19, #0x2c2]
// 0x10a3df0: b #0x10a3d14
// 0x10a3df4: ldr s8, [x19, #0x140]
// 0x10a3df8: ldr s0, [x19, #0x13c]
// 0x10a3dfc: fcmp s8, s0
// 0x10a3e00: b.pl #0x10a3e3c
// 0x10a3e04: mov x0, xzr
// 0x10a3e08: bl #0x1b89b60
// 0x10a3e0c: fadd s0, s8, s0
// 0x10a3e10: str s0, [x19, #0x140]
// 0x10a3e14: strb wzr, [x19, #0x138]
// 0x10a3e18: b #0x10a3e3c
// 0x10a3e1c: ldr s8, [x19, #0x140]
// 0x10a3e20: ldr s0, [x19, #0x13c]
// 0x10a3e24: fcmp s8, s0
// 0x10a3e28: b.pl #0x10a3e3c
// 0x10a3e2c: mov x0, xzr
// 0x10a3e30: bl #0x1b89b60
// 0x10a3e34: fadd s0, s8, s0
// 0x10a3e38: str s0, [x19, #0x140]
// 0x10a3e3c: ldrb w8, [x19, #0x2b0]
// 0x10a3e40: cbz w8, #0x10a3e70
// 0x10a3e44: adrp x8, #0x832000
// 0x10a3e48: ldr s0, [x19, #0xd8]
// 0x10a3e4c: ldr s1, [x8, #0x4f8]
// 0x10a3e50: ldr s8, [x19, #0x120]
// 0x10a3e54: fadd s1, s0, s1
// 0x10a3e58: fcmp s8, s1
// 0x10a3e5c: b.pl #0x10a3e90
// 0x10a3e60: mov x0, xzr
// 0x10a3e64: bl #0x1b89b60
// 0x10a3e68: fmov s1, #12.00000000
// 0x10a3e6c: b #0x10a3f04
// 0x10a3e70: ldrb w8, [x19, #0x258]
// 0x10a3e74: ldr s8, [x19, #0x120]
// 0x10a3e78: cbz w8, #0x10a3eb4
// 0x10a3e7c: adrp x8, #0x832000
// 0x10a3e80: ldr s0, [x19, #0xdc]
// 0x10a3e84: ldr s1, [x8, #0x3b8]
// 0x10a3e88: fadd s1, s0, s1
// 0x10a3e8c: b #0x10a3ecc
// 0x10a3e90: adrp x8, #0x832000
// 0x10a3e94: ldr s1, [x8, #0x3b8]
// 0x10a3e98: fadd s0, s0, s1
// 0x10a3e9c: fcmp s8, s0
// 0x10a3ea0: b.le #0x10a3f10
// 0x10a3ea4: mov x0, xzr
// 0x10a3ea8: bl #0x1b89b60
// 0x10a3eac: fmov s1, #-12.00000000
// 0x10a3eb0: b #0x10a3f04
// 0x10a3eb4: ldr s0, [x19, #0xd4]
// 0x10a3eb8: ldr s1, [x19, #0xe8]
// 0x10a3ebc: adrp x8, #0x832000
// 0x10a3ec0: ldr s2, [x8, #0x3b8]
// 0x10a3ec4: fmul s0, s0, s1
// 0x10a3ec8: fadd s1, s0, s2
// 0x10a3ecc: fcmp s8, s1
// 0x10a3ed0: b.le #0x10a3ee4
// 0x10a3ed4: mov x0, xzr
// 0x10a3ed8: bl #0x1b89b60
// 0x10a3edc: fmov s1, #-16.00000000
// 0x10a3ee0: b #0x10a3f04
// 0x10a3ee4: adrp x8, #0x832000
// 0x10a3ee8: ldr s1, [x8, #0x4f8]
// 0x10a3eec: fadd s0, s0, s1
// 0x10a3ef0: fcmp s8, s0
// 0x10a3ef4: b.pl #0x10a3f10
// 0x10a3ef8: mov x0, xzr
// 0x10a3efc: bl #0x1b89b60
// 0x10a3f00: fmov s1, #16.00000000
// 0x10a3f04: fmul s0, s0, s1
// 0x10a3f08: fadd s0, s8, s0
// 0x10a3f0c: str s0, [x19, #0x120]
// 0x10a3f10: ldrb w8, [x19, #0x114]
// 0x10a3f14: ldr s8, [x19, #0x11c]
// 0x10a3f18: cbz w8, #0x10a3f38
// 0x10a3f1c: ldr s0, [x19, #0x118]
// 0x10a3f20: fcmp s8, s0
// 0x10a3f24: b.le #0x10a3f54
// 0x10a3f28: mov x0, xzr
// 0x10a3f2c: bl #0x1b89b60
// 0x10a3f30: fsub s0, s8, s0
// 0x10a3f34: b #0x10a3f50
// 0x10a3f38: fmov s0, #1.00000000
// 0x10a3f3c: fcmp s8, s0
// 0x10a3f40: b.pl #0x10a3f54
// 0x10a3f44: mov x0, xzr
// 0x10a3f48: bl #0x1b89b60
// 0x10a3f4c: fadd s0, s8, s0
// 0x10a3f50: str s0, [x19, #0x11c]
// 0x10a3f54: ldrb w8, [x19, #0x2d0]
// 0x10a3f58: cbnz w8, #0x10a3f6c
// 0x10a3f5c: ldr s0, [x19, #0x2cc]
// 0x10a3f60: ldr s1, [x19, #0x3bc]
// 0x10a3f64: fcmp s0, s1
// 0x10a3f68: b.pl #0x10a4208
// 0x10a3f6c: ldp s0, s8, [x19, #0xf8]
// 0x10a3f70: fcmp s8, s0
// 0x10a3f74: b.le #0x10a3f88
// 0x10a3f78: mov x0, xzr
// 0x10a3f7c: bl #0x1b89b60
// 0x10a3f80: fsub s0, s8, s0
// 0x10a3f84: str s0, [x19, #0xfc]
// 0x10a3f88: ldrb w8, [x19, #0x2dc]
// 0x10a3f8c: cbz w8, #0x10a3fc0
// 0x10a3f90: ldr s0, [x19, #0x2cc]
// 0x10a3f94: ldr s1, [x19, #0x3bc]
// 0x10a3f98: fcmp s0, s1
// 0x10a3f9c: b.pl #0x10a3fc0
// 0x10a3fa0: ldr s8, [x19, #0x104]
// 0x10a3fa4: ldr s0, [x19, #0x100]
// 0x10a3fa8: fcmp s8, s0
// 0x10a3fac: b.le #0x10a3fe0
// 0x10a3fb0: mov x0, xzr
// 0x10a3fb4: bl #0x1b89b60
// 0x10a3fb8: fsub s0, s8, s0
// 0x10a3fbc: b #0x10a3fdc
// 0x10a3fc0: ldr s8, [x19, #0x104]
// 0x10a3fc4: fmov s0, #1.00000000
// 0x10a3fc8: fcmp s8, s0
// 0x10a3fcc: b.pl #0x10a3fe0
// 0x10a3fd0: mov x0, xzr
// 0x10a3fd4: bl #0x1b89b60
// 0x10a3fd8: fadd s0, s8, s0
// 0x10a3fdc: str s0, [x19, #0x104]
// 0x10a3fe0: ldr s0, [x19, #0xc4]
// 0x10a3fe4: ldr s8, [x19, #0x10c]
// 0x10a3fe8: fcmp s0, #0.0
// 0x10a3fec: b.ge #0x10a400c
// 0x10a3ff0: ldr s0, [x19, #0xf4]
// 0x10a3ff4: fcmp s8, s0
// 0x10a3ff8: b.le #0x10a4028
// 0x10a3ffc: mov x0, xzr
// 0x10a4000: bl #0x1b89b60
// 0x10a4004: fsub s0, s8, s0
// 0x10a4008: b #0x10a4024
// 0x10a400c: fmov s0, #1.00000000
// 0x10a4010: fcmp s8, s0
// 0x10a4014: b.pl #0x10a4028
// 0x10a4018: mov x0, xzr
// 0x10a401c: bl #0x1b89b60
// 0x10a4020: fadd s0, s8, s0
// 0x10a4024: str s0, [x19, #0x10c]
// 0x10a4028: ldr s0, [x19, #0xc0]
// 0x10a402c: fcmp s0, #0.0
// 0x10a4030: b.ne #0x10a4054
// 0x10a4034: ldr s8, [x19, #0x110]
// 0x10a4038: fmov s0, #1.00000000
// 0x10a403c: fcmp s8, s0
// 0x10a4040: b.pl #0x10a4080
// 0x10a4044: mov x0, xzr
// 0x10a4048: bl #0x1b89b60
// 0x10a404c: fadd s0, s8, s0
// 0x10a4050: b #0x10a407c
// 0x10a4054: ldr s0, [x19, #0xc4]
// 0x10a4058: fcmp s0, #0.0
// 0x10a405c: b.ne #0x10a4034
// 0x10a4060: ldr s8, [x19, #0x110]
// 0x10a4064: ldr s0, [x19, #0x108]
// 0x10a4068: fcmp s8, s0
// 0x10a406c: b.le #0x10a4080
// 0x10a4070: mov x0, xzr
// 0x10a4074: bl #0x1b89b60
// 0x10a4078: fsub s0, s8, s0
// 0x10a407c: str s0, [x19, #0x110]
// 0x10a4080: ldr s8, [x19, #0x3dc]
// 0x10a4084: mov x0, xzr
// 0x10a4088: bl #0x1b9ad58
// 0x10a408c: fmov s1, #0.50000000
// 0x10a4090: fcmp s0, s1
// 0x10a4094: b.le #0x10a40c8
// 0x10a4098: ldrb w8, [x19, #0x2dc]
// 0x10a409c: cbz w8, #0x10a4228
// 0x10a40a0: ldr s0, [x19, #0x3c4]
// 0x10a40a4: ldr x0, [x19, #0x238]
// 0x10a40a8: str s0, [x19, #0x2cc]
// 0x10a40ac: cbz x0, #0x10a5704
// 0x10a40b0: adrp x8, #0x832000
// 0x10a40b4: ldr s0, [x19, #0x3cc]
// 0x10a40b8: ldr s1, [x8, #0x548]
// 0x10a40bc: fdiv s0, s0, s1
// 0x10a40c0: mov x1, xzr
// 0x10a40c4: bl #0x1bcfe2c
// 0x10a40c8: ldrb w8, [x19, #0x14c]
// 0x10a40cc: cbz w8, #0x10a41ec
// 0x10a40d0: ldr s0, [x19, #0x150]
// 0x10a40d4: fcmp s0, #0.0
// 0x10a40d8: b.le #0x10a42b0
// 0x10a40dc: mov x0, xzr
// 0x10a40e0: bl #0x1b9ad58
// 0x10a40e4: fmov s1, #0.50000000
// 0x10a40e8: fcmp s0, s1
// 0x10a40ec: fmov s12, wzr
// 0x10a40f0: b.le #0x10a4118
// 0x10a40f4: ldr x8, [x19, #0x28]
// 0x10a40f8: cbz x8, #0x10a5704
// 0x10a40fc: ldr s0, [x8, #0x20c]
// 0x10a4100: fcmp s0, #0.0
// 0x10a4104: b.le #0x10a4118
// 0x10a4108: ldrb w8, [x19, #0x2b1]
// 0x10a410c: cbnz w8, #0x10a4118
// 0x10a4110: ldrb w8, [x19, #0x2dc]
// 0x10a4114: cbz w8, #0x10a52f0
// 0x10a4118: ldr x0, [x19, #0x240]
// 0x10a411c: str s12, [x19, #0x170]
// 0x10a4120: cbz x0, #0x10a5704
// 0x10a4124: mov x1, xzr
// 0x10a4128: bl #0x1bcf8fc
// 0x10a412c: tbz w0, #0, #0x10a4170
// 0x10a4130: ldr x0, [x19, #0x240]
// 0x10a4134: cbz x0, #0x10a5704
// 0x10a4138: ldr s8, [x19, #0x170]
// 0x10a413c: mov x1, xzr
// 0x10a4140: bl #0x1bcff20
// 0x10a4144: ldr x0, [x19, #0x240]
// 0x10a4148: cbz x0, #0x10a5704
// 0x10a414c: mov x1, xzr
// 0x10a4150: mov v9.16b, v1.16b
// 0x10a4154: bl #0x1bcff20
// 0x10a4158: ldr x0, [x19, #0x240]
// 0x10a415c: cbz x0, #0x10a5704
// 0x10a4160: mov v0.16b, v8.16b
// 0x10a4164: mov v1.16b, v9.16b
// 0x10a4168: mov x1, xzr
// 0x10a416c: bl #0x1bcffc0
// 0x10a4170: ldr s9, [x19, #0x174]
// 0x10a4174: ldr s10, [x19, #0x170]
// 0x10a4178: mov x0, xzr
// 0x10a417c: add x20, x19, #0x178
// 0x10a4180: bl #0x1b89b60
// 0x10a4184: adrp x8, #0x832000
// 0x10a4188: ldr s8, [x8, #0x3b8]
// 0x10a418c: mov w8, #0x7f800000
// 0x10a4190: mov v4.16b, v0.16b
// 0x10a4194: fmov s3, w8
// 0x10a4198: mov v0.16b, v9.16b
// 0x10a419c: mov v1.16b, v10.16b
// 0x10a41a0: mov x0, x20
// 0x10a41a4: mov v2.16b, v8.16b
// 0x10a41a8: mov x1, xzr
// 0x10a41ac: bl #0x1b8c860
// 0x10a41b0: ldr x0, [x19, #0x168]
// 0x10a41b4: str s0, [x19, #0x174]
// 0x10a41b8: cbz x0, #0x10a5704
// 0x10a41bc: ldr s0, [x19, #0x170]
// 0x10a41c0: mov x2, xzr
// 0x10a41c4: fabs s0, s0
// 0x10a41c8: fcmp s0, s8
// 0x10a41cc: cset w1, gt
// 0x10a41d0: bl #0x1bcf938
// 0x10a41d4: ldr x0, [x19, #0x168]
// 0x10a41d8: cbz x0, #0x10a5704
// 0x10a41dc: ldrb w8, [x19, #0x2d0]
// 0x10a41e0: cbz w8, #0x10a42a4
// 0x10a41e4: fmov s0, #0.75000000
// 0x10a41e8: b #0x10a42a8
// 0x10a41ec: ldr x0, [x19, #0x168]
// 0x10a41f0: cbz x0, #0x10a5704
// 0x10a41f4: mov w1, wzr
// 0x10a41f8: mov x2, xzr
// 0x10a41fc: bl #0x1bcf938
// 0x10a4200: str wzr, [x19, #0x170]
// 0x10a4204: b #0x10a42b0
// 0x10a4208: ldr s8, [x19, #0xfc]
// 0x10a420c: fmov s0, #1.00000000
// 0x10a4210: fcmp s8, s0
// 0x10a4214: b.pl #0x10a3f88
// 0x10a4218: mov x0, xzr
// 0x10a421c: bl #0x1b89b60
// 0x10a4220: fadd s0, s8, s0
// 0x10a4224: b #0x10a3f84
// 0x10a4228: adrp x8, #0x832000
// 0x10a422c: ldr s0, [x8, #0x448]
// 0x10a4230: ldrb w9, [x19, #0x2d0]
// 0x10a4234: ldr x8, [x19, #0x28]
// 0x10a4238: fmov s1, #1.00000000
// 0x10a423c: fdiv s0, s8, s0
// 0x10a4240: fadd s9, s0, s1
// 0x10a4244: cbz w9, #0x10a4c70
// 0x10a4248: cbz x8, #0x10a5704
// 0x10a424c: ldr s0, [x8, #0x20c]
// 0x10a4250: fmov s1, #1.00000000
// 0x10a4254: fcmp s0, s1
// 0x10a4258: b.mi #0x10a40a0
// 0x10a425c: ldr s0, [x19, #0x3c0]
// 0x10a4260: ldr x20, [x19, #0x238]
// 0x10a4264: str s0, [x19, #0x2cc]
// 0x10a4268: cbz x20, #0x10a5704
// 0x10a426c: mov x0, x20
// 0x10a4270: mov x1, xzr
// 0x10a4274: bl #0x1bcfdf0
// 0x10a4278: mov x0, xzr
// 0x10a427c: mov v8.16b, v0.16b
// 0x10a4280: bl #0x1b89b60
// 0x10a4284: ldr s1, [x19, #0x3cc]
// 0x10a4288: fmul s0, s9, s0
// 0x10a428c: fmov s2, #-4.00000000
// 0x10a4290: fmul s0, s0, s2
// 0x10a4294: fadd s0, s8, s0
// 0x10a4298: fcmp s0, s1
// 0x10a429c: fcsel s0, s0, s1, gt
// 0x10a42a0: b #0x10a52e8
// 0x10a42a4: fmov s0, #1.50000000
// 0x10a42a8: mov x1, xzr
// 0x10a42ac: bl #0x1bcfe2c
// 0x10a42b0: ldrb w8, [x19, #0x295]
// 0x10a42b4: cbnz w8, #0x10a42c0
// 0x10a42b8: ldrb w9, [x19, #0x258]
// 0x10a42bc: cbz w9, #0x10a4368
// 0x10a42c0: ldrb w9, [x19, #0x2a0]
// 0x10a42c4: cbnz w9, #0x10a4368
// 0x10a42c8: ldr x9, [x19, #0x30]
// 0x10a42cc: cbz x9, #0x10a5704
// 0x10a42d0: ldr s0, [x9, #0xe0]
// 0x10a42d4: adrp x9, #0x832000
// 0x10a42d8: ldr s1, [x9, #0x3b8]
// 0x10a42dc: fcmp s0, s1
// 0x10a42e0: b.le #0x10a434c
// 0x10a42e4: cbz w8, #0x10a48a8
// 0x10a42e8: ldr x8, [x19, #0x20]
// 0x10a42ec: cbz x8, #0x10a5704
// 0x10a42f0: ldr s1, [x8, #0x78]
// 0x10a42f4: ldr s0, [x19, #0xe4]
// 0x10a42f8: mov w8, #0x42400000
// 0x10a42fc: fmov s3, w8
// 0x10a4300: adrp x8, #0x832000
// 0x10a4304: fdiv s1, s1, s3
// 0x10a4308: ldr s3, [x8, #0x4f4]
// 0x10a430c: fmov s2, #0.25000000
// 0x10a4310: fmul s2, s0, s2
// 0x10a4314: fmul s1, s2, s1
// 0x10a4318: fadd s1, s1, s3
// 0x10a431c: fneg s2, s0
// 0x10a4320: fcmp s1, s0
// 0x10a4324: fcsel s0, s0, s1, gt
// 0x10a4328: fcmp s1, s2
// 0x10a432c: fcsel s0, s0, s2, pl
// 0x10a4330: str s0, [x19, #0x298]
// 0x10a4334: ldr x0, [x19, #0x98]
// 0x10a4338: cbz x0, #0x10a5704
// 0x10a433c: ldr s2, [x19, #0x234]
// 0x10a4340: ldr s1, [x19, #0x298]
// 0x10a4344: ldr s0, [x19, #0x22c]
// 0x10a4348: b #0x10a4360
// 0x10a434c: ldr x0, [x19, #0x98]
// 0x10a4350: cbz x0, #0x10a5704
// 0x10a4354: ldr s2, [x19, #0x234]
// 0x10a4358: ldr s0, [x19, #0x22c]
// 0x10a435c: fmov s1, wzr
// 0x10a4360: mov x1, xzr
// 0x10a4364: bl #0x1bcef98
// 0x10a4368: ldr x8, [x19, #0x28]
// 0x10a436c: cbz x8, #0x10a5704
// 0x10a4370: ldrb w9, [x8, #0x217]
// 0x10a4374: cbz w9, #0x10a44e0
// 0x10a4378: ldr x0, [x19, #0x238]
// 0x10a437c: cbz x0, #0x10a5704
// 0x10a4380: ldr s12, [x19, #0x394]
// 0x10a4384: ldr s13, [x19, #0x398]
// 0x10a4388: ldr s14, [x19, #0x39c]
// 0x10a438c: ldp s9, s8, [x19, #0x78]
// 0x10a4390: ldr s10, [x19, #0x74]
// 0x10a4394: mov x1, xzr
// 0x10a4398: bl #0x1bcfd68
// 0x10a439c: ldr s1, [x26, #0x390]
// 0x10a43a0: ldr s6, [x19, #0x3e0]
// 0x10a43a4: ldp s2, s3, [x19, #0x74]
// 0x10a43a8: add x21, x19, #0x304
// 0x10a43ac: fmul s0, s0, s1
// 0x10a43b0: ldr s1, [x19, #0x7c]
// 0x10a43b4: fmul s4, s10, s0
// 0x10a43b8: ldr s10, [x19, #0x3d0]
// 0x10a43bc: fmul s5, s9, s0
// 0x10a43c0: fneg s9, s1
// 0x10a43c4: fadd s1, s12, s4
// 0x10a43c8: fmul s0, s8, s0
// 0x10a43cc: stp s6, s1, [sp, #0x5c]
// 0x10a43d0: fadd s1, s13, s5
// 0x10a43d4: mov x0, x21
// 0x10a43d8: mov x1, xzr
// 0x10a43dc: add x20, x19, #0x33c
// 0x10a43e0: fneg s15, s2
// 0x10a43e4: fneg s8, s3
// 0x10a43e8: mov v11.16b, v12.16b
// 0x10a43ec: mov v12.16b, v13.16b
// 0x10a43f0: str s1, [sp, #0x70]
// 0x10a43f4: mov v13.16b, v14.16b
// 0x10a43f8: fadd s14, s14, s0
// 0x10a43fc: bl #0x1b95168
// 0x10a4400: adrp x26, #0x1e8d000
// 0x10a4404: ldr x26, [x26, #0x4a8]
// 0x10a4408: mov w22, w0
// 0x10a440c: ldr x8, [x26]
// 0x10a4410: ldr w9, [x8, #0xe0]
// 0x10a4414: cbnz w9, #0x10a4420
// 0x10a4418: mov x0, x8
// 0x10a441c: bl #0xf7da5c
// 0x10a4420: adrp x8, #0x832000
// 0x10a4424: ldr s0, [x8, #0x3e0]
// 0x10a4428: ldr s1, [x24, #0x3bc]
// 0x10a442c: ldp s2, s3, [sp, #0x5c]
// 0x10a4430: ldr s4, [sp, #0x70]
// 0x10a4434: fmul s0, s10, s0
// 0x10a4438: str s1, [sp, #0x58]
// 0x10a443c: fmul s6, s2, s1
// 0x10a4440: str s0, [sp, #0x10]
// 0x10a4444: mov v0.16b, v11.16b
// 0x10a4448: mov v1.16b, v12.16b
// 0x10a444c: mov v2.16b, v13.16b
// 0x10a4450: mov v5.16b, v14.16b
// 0x10a4454: mov x0, x20
// 0x10a4458: mov w1, w22
// 0x10a445c: mov x2, xzr
// 0x10a4460: stp s8, s9, [sp, #4]
// 0x10a4464: str s15, [sp]
// 0x10a4468: bl #0x1bcc8c8
// 0x10a446c: ldrb w8, [x19, #0x295]
// 0x10a4470: tbz w0, #0, #0x10a4484
// 0x10a4474: mov w9, #1
// 0x10a4478: strb w9, [x19, #0x228]
// 0x10a447c: cbnz w8, #0x10a4490
// 0x10a4480: b #0x10a4584
// 0x10a4484: cbz w8, #0x10a4574
// 0x10a4488: mov w8, #1
// 0x10a448c: strb w8, [x19, #0x228]
// 0x10a4490: ldr x8, [x19, #0x38]
// 0x10a4494: cbz x8, #0x10a5704
// 0x10a4498: adrp x9, #0x1e8c000
// 0x10a449c: ldr x9, [x9, #0xd8]
// 0x10a44a0: ldr x0, [x9]
// 0x10a44a4: ldr x22, [x8, #0x138]
// 0x10a44a8: ldr w9, [x0, #0xe0]
// 0x10a44ac: cbnz w9, #0x10a44b4
// 0x10a44b0: bl #0xf7da5c
// 0x10a44b4: mov x0, x22
// 0x10a44b8: mov x1, xzr
// 0x10a44bc: bl #0x1b98274
// 0x10a44c0: tbz w0, #0, #0x10a4684
// 0x10a44c4: ldr x8, [x19, #0x38]
// 0x10a44c8: cbz x8, #0x10a5704
// 0x10a44cc: ldr x1, [x8, #0x138]
// 0x10a44d0: add x0, x19, #0x2f8
// 0x10a44d4: str x1, [x19, #0x2f8]
// 0x10a44d8: bl #0xf7d8d0
// 0x10a44dc: b #0x10a4684
// 0x10a44e0: ldrb w9, [x19, #0x256]
// 0x10a44e4: cbz w9, #0x10a4618
// 0x10a44e8: mov x0, xzr
// 0x10a44ec: bl #0x1b9ad30
// 0x10a44f0: ldr s1, [x19, #0x264]
// 0x10a44f4: ldr s2, [x19, #0x1a4]
// 0x10a44f8: fmov s3, #1.50000000
// 0x10a44fc: fsub s0, s0, s1
// 0x10a4500: fdiv s1, s2, s3
// 0x10a4504: fcmp s0, s1
// 0x10a4508: b.le #0x10a4514
// 0x10a450c: mov w8, #1
// 0x10a4510: strb w8, [x19, #0x268]
// 0x10a4514: mov x0, xzr
// 0x10a4518: bl #0x1b9ad30
// 0x10a451c: ldr s1, [x19, #0x264]
// 0x10a4520: ldr s2, [x19, #0x1a4]
// 0x10a4524: fsub s0, s0, s1
// 0x10a4528: fcmp s0, s2
// 0x10a452c: b.le #0x10a4378
// 0x10a4530: ldr s8, [x19, #0x26c]
// 0x10a4534: mov x0, xzr
// 0x10a4538: bl #0x1b9ad30
// 0x10a453c: fcmp s8, s0
// 0x10a4540: b.pl #0x10a4378
// 0x10a4544: ldr x0, [x19, #0x28]
// 0x10a4548: cbz x0, #0x10a5704
// 0x10a454c: ldr s0, [x19, #0x1a8]
// 0x10a4550: mov x1, xzr
// 0x10a4554: mov w2, wzr
// 0x10a4558: bl #0x109fed8
// 0x10a455c: mov x0, xzr
// 0x10a4560: bl #0x1b9ad30
// 0x10a4564: fmov s1, #1.75000000
// 0x10a4568: fadd s0, s0, s1
// 0x10a456c: str s0, [x19, #0x26c]
// 0x10a4570: b #0x10a4378
// 0x10a4574: ldrb w8, [x19, #0x258]
// 0x10a4578: cbz w8, #0x10a4660
// 0x10a457c: mov w8, #1
// 0x10a4580: strb w8, [x19, #0x228]
// 0x10a4584: ldrb w8, [x19, #0x255]
// 0x10a4588: cbnz w8, #0x10a4684
// 0x10a458c: ldrb w8, [x19, #0x258]
// 0x10a4590: cbnz w8, #0x10a4684
// 0x10a4594: mov x0, x20
// 0x10a4598: mov x1, xzr
// 0x10a459c: bl #0x1bcec58
// 0x10a45a0: cbz x0, #0x10a5704
// 0x10a45a4: mov x1, xzr
// 0x10a45a8: bl #0x1b92190
// 0x10a45ac: cbz x0, #0x10a5704
// 0x10a45b0: mov x1, xzr
// 0x10a45b4: bl #0x1b92774
// 0x10a45b8: adrp x8, #0x1e8e000
// 0x10a45bc: ldr x8, [x8, #0xb0]
// 0x10a45c0: mov x2, xzr
// 0x10a45c4: mov x22, x0
// 0x10a45c8: ldr x1, [x8]
// 0x10a45cc: bl #0x17f610c
// 0x10a45d0: tbz w0, #0, #0x10a4da0
// 0x10a45d4: ldr x8, [x19, #0x38]
// 0x10a45d8: cbz x8, #0x10a5704
// 0x10a45dc: adrp x9, #0x1e8c000
// 0x10a45e0: ldr x9, [x9, #0xd8]
// 0x10a45e4: ldr x22, [x8, #0x150]
// 0x10a45e8: ldr x0, [x9]
// 0x10a45ec: ldr w9, [x0, #0xe0]
// 0x10a45f0: cbnz w9, #0x10a45f8
// 0x10a45f4: bl #0xf7da5c
// 0x10a45f8: mov x0, x22
// 0x10a45fc: mov x1, xzr
// 0x10a4600: bl #0x1b98274
// 0x10a4604: tbz w0, #0, #0x10a4684
// 0x10a4608: ldr x8, [x19, #0x38]
// 0x10a460c: cbz x8, #0x10a5704
// 0x10a4610: ldr x1, [x8, #0x150]
// 0x10a4614: b #0x10a44d0
// 0x10a4618: ldrb w9, [x19, #0x268]
// 0x10a461c: cbz w9, #0x10a4378
// 0x10a4620: ldr x0, [x19, #0x80]
// 0x10a4624: cbz x0, #0x10a5704
// 0x10a4628: ldr x20, [x8, #0x3e8]
// 0x10a462c: mov x1, xzr
// 0x10a4630: bl #0x1b9d508
// 0x10a4634: mov w8, #0x43fa0000
// 0x10a4638: fmov s3, #0.75000000
// 0x10a463c: fmov s4, wzr
// 0x10a4640: fmov s5, #1.00000000
// 0x10a4644: fmov s6, #1.00000000
// 0x10a4648: fmov s7, w8
// 0x10a464c: mov x0, x20
// 0x10a4650: mov x1, xzr
// 0x10a4654: bl #0x108d260
// 0x10a4658: strb wzr, [x19, #0x268]
// 0x10a465c: b #0x10a4378
// 0x10a4660: ldr s8, [x19, #0x1bc]
// 0x10a4664: mov x0, xzr
// 0x10a4668: bl #0x1b9ad30
// 0x10a466c: adrp x8, #0x832000
// 0x10a4670: ldr s1, [x8, #0x550]
// 0x10a4674: fadd s1, s8, s1
// 0x10a4678: fcmp s1, s0
// 0x10a467c: b.pl #0x10a4684
// 0x10a4680: strb wzr, [x19, #0x228]
// 0x10a4684: ldr x0, [x19, #0x60]
// 0x10a4688: cbz x0, #0x10a5704
// 0x10a468c: mov x1, xzr
// 0x10a4690: bl #0x1b9d508
// 0x10a4694: mov v8.16b, v0.16b
// 0x10a4698: mov v9.16b, v1.16b
// 0x10a469c: mov v10.16b, v2.16b
// 0x10a46a0: ldp s0, s1, [x19, #0x74]
// 0x10a46a4: ldr s2, [x19, #0x7c]
// 0x10a46a8: ldr s11, [x19, #0x3d8]
// 0x10a46ac: mov x0, x21
// 0x10a46b0: mov x1, xzr
// 0x10a46b4: fneg s14, s0
// 0x10a46b8: fneg s13, s1
// 0x10a46bc: fneg s12, s2
// 0x10a46c0: add x22, x19, #0x310
// 0x10a46c4: bl #0x1b95168
// 0x10a46c8: ldr x8, [x26]
// 0x10a46cc: mov w23, w0
// 0x10a46d0: ldr w9, [x8, #0xe0]
// 0x10a46d4: cbnz w9, #0x10a46e0
// 0x10a46d8: mov x0, x8
// 0x10a46dc: bl #0xf7da5c
// 0x10a46e0: mov v0.16b, v8.16b
// 0x10a46e4: mov v1.16b, v9.16b
// 0x10a46e8: mov v2.16b, v10.16b
// 0x10a46ec: mov v3.16b, v14.16b
// 0x10a46f0: mov v4.16b, v13.16b
// 0x10a46f4: mov v5.16b, v12.16b
// 0x10a46f8: mov x0, x22
// 0x10a46fc: mov v6.16b, v11.16b
// 0x10a4700: mov w1, w23
// 0x10a4704: mov x2, xzr
// 0x10a4708: bl #0x1bcbc48
// 0x10a470c: tbz w0, #0, #0x10a4b0c
// 0x10a4710: mov x0, x22
// 0x10a4714: mov x1, xzr
// 0x10a4718: bl #0x1bced10
// 0x10a471c: adrp x23, #0x1fab000
// 0x10a4720: ldp s11, s12, [x19, #0x68]
// 0x10a4724: ldrb w8, [x23, #0x3e2]
// 0x10a4728: ldr s13, [x19, #0x70]
// 0x10a472c: mov v8.16b, v0.16b
// 0x10a4730: mov v9.16b, v1.16b
// 0x10a4734: mov v10.16b, v2.16b
// 0x10a4738: cbnz w8, #0x10a4750
// 0x10a473c: adrp x0, #0x1e8c000
// 0x10a4740: ldr x0, [x0, #0xa60]
// 0x10a4744: bl #0xf7d92c
// 0x10a4748: mov w8, #1
// 0x10a474c: strb w8, [x23, #0x3e2]
// 0x10a4750: adrp x23, #0x1e8c000
// 0x10a4754: ldr x23, [x23, #0xa60]
// 0x10a4758: fmul s0, s8, s8
// 0x10a475c: fmul s1, s9, s9
// 0x10a4760: fadd s0, s0, s1
// 0x10a4764: ldr x0, [x23]
// 0x10a4768: fmul s1, s10, s10
// 0x10a476c: fadd s14, s1, s0
// 0x10a4770: fmul s0, s11, s11
// 0x10a4774: ldr w8, [x0, #0xe0]
// 0x10a4778: fmul s1, s12, s12
// 0x10a477c: fadd s0, s0, s1
// 0x10a4780: fmul s1, s13, s13
// 0x10a4784: fadd s15, s1, s0
// 0x10a4788: cbnz w8, #0x10a4790
// 0x10a478c: bl #0xf7da5c
// 0x10a4790: adrp x8, #0x832000
// 0x10a4794: ldr s1, [x8, #0x344]
// 0x10a4798: fmul s0, s14, s15
// 0x10a479c: fsqrt s0, s0
// 0x10a47a0: fcmp s0, s1
// 0x10a47a4: fmov s1, wzr
// 0x10a47a8: b.mi #0x10a4800
// 0x10a47ac: ldr x0, [x23]
// 0x10a47b0: fmul s1, s8, s11
// 0x10a47b4: fmul s2, s9, s12
// 0x10a47b8: fmul s3, s10, s13
// 0x10a47bc: fadd s1, s1, s2
// 0x10a47c0: fadd s1, s3, s1
// 0x10a47c4: ldr w8, [x0, #0xe0]
// 0x10a47c8: fdiv s0, s1, s0
// 0x10a47cc: fmov s1, #1.00000000
// 0x10a47d0: fmov s2, #-1.00000000
// 0x10a47d4: fmin s1, s0, s1
// 0x10a47d8: fcmp s0, s2
// 0x10a47dc: fcsel s8, s1, s2, pl
// 0x10a47e0: cbnz w8, #0x10a47e8
// 0x10a47e4: bl #0xf7da5c
// 0x10a47e8: fcvt d0, s8
// 0x10a47ec: bl #0x1db0ca0
// 0x10a47f0: adrp x8, #0x832000
// 0x10a47f4: ldr s1, [x8, #0x554]
// 0x10a47f8: fcvt s0, d0
// 0x10a47fc: fmul s1, s0, s1
// 0x10a4800: ldr s0, [x19, #0x1ac]
// 0x10a4804: scvtf s0, s0
// 0x10a4808: fcmp s1, s0
// 0x10a480c: b.le #0x10a49e8
// 0x10a4810: ldrb w8, [x19, #0x255]
// 0x10a4814: cbnz w8, #0x10a49e8
// 0x10a4818: ldr x0, [x19, #0x60]
// 0x10a481c: cbz x0, #0x10a5704
// 0x10a4820: mov x1, xzr
// 0x10a4824: bl #0x1b9d508
// 0x10a4828: adrp x24, #0x1fab000
// 0x10a482c: ldr s11, [x19, #0x3f4]
// 0x10a4830: ldr s12, [x19, #0x3f8]
// 0x10a4834: ldrb w8, [x24, #0x2c8]
// 0x10a4838: ldr s13, [x19, #0x3fc]
// 0x10a483c: mov v8.16b, v0.16b
// 0x10a4840: mov v9.16b, v1.16b
// 0x10a4844: mov v10.16b, v2.16b
// 0x10a4848: cbnz w8, #0x10a4860
// 0x10a484c: adrp x0, #0x1e8c000
// 0x10a4850: ldr x0, [x0, #0xa60]
// 0x10a4854: bl #0xf7d92c
// 0x10a4858: mov w8, #1
// 0x10a485c: strb w8, [x24, #0x2c8]
// 0x10a4860: ldr x0, [x23]
// 0x10a4864: ldr w8, [x0, #0xe0]
// 0x10a4868: cbnz w8, #0x10a4870
// 0x10a486c: bl #0xf7da5c
// 0x10a4870: fmul s0, s11, s11
// 0x10a4874: fmul s1, s12, s12
// 0x10a4878: adrp x8, #0x832000
// 0x10a487c: fadd s0, s0, s1
// 0x10a4880: ldr s1, [x8, #0x41c]
// 0x10a4884: fmul s2, s13, s13
// 0x10a4888: fadd s0, s2, s0
// 0x10a488c: fsqrt s2, s0
// 0x10a4890: fcmp s2, s1
// 0x10a4894: b.le #0x10a4904
// 0x10a4898: fdiv s0, s11, s2
// 0x10a489c: fdiv s1, s12, s2
// 0x10a48a0: fdiv s2, s13, s2
// 0x10a48a4: b #0x10a493c
// 0x10a48a8: ldrb w8, [x19, #0x258]
// 0x10a48ac: cbz w8, #0x10a4334
// 0x10a48b0: ldr s0, [x19, #0xdc]
// 0x10a48b4: ldr s1, [x19, #0x298]
// 0x10a48b8: ldr x8, [x19, #0x20]
// 0x10a48bc: fneg s2, s0
// 0x10a48c0: fcmp s1, s0
// 0x10a48c4: fcsel s3, s0, s1, gt
// 0x10a48c8: fcmp s1, s2
// 0x10a48cc: fcsel s1, s3, s2, pl
// 0x10a48d0: str s1, [x19, #0x298]
// 0x10a48d4: cbz x8, #0x10a5704
// 0x10a48d8: ldrb w9, [x19, #0x257]
// 0x10a48dc: ldr s1, [x8, #0x78]
// 0x10a48e0: cbz w9, #0x10a51a8
// 0x10a48e4: fmov s2, #-15.00000000
// 0x10a48e8: fcmp s1, s2
// 0x10a48ec: b.le #0x10a5218
// 0x10a48f0: mov w8, #0x42400000
// 0x10a48f4: fmov s2, w8
// 0x10a48f8: fdiv s1, s1, s2
// 0x10a48fc: fmul s0, s0, s1
// 0x10a4900: b #0x10a5354
// 0x10a4904: adrp x23, #0x1fab000
// 0x10a4908: ldrb w8, [x23, #0x2c9]
// 0x10a490c: cbnz w8, #0x10a4924
// 0x10a4910: adrp x0, #0x1e8c000
// 0x10a4914: ldr x0, [x0, #0x1e8]
// 0x10a4918: bl #0xf7d92c
// 0x10a491c: mov w8, #1
// 0x10a4920: strb w8, [x23, #0x2c9]
// 0x10a4924: adrp x8, #0x1e8c000
// 0x10a4928: ldr x8, [x8, #0x1e8]
// 0x10a492c: ldr x8, [x8]
// 0x10a4930: ldr x8, [x8, #0xb8]
// 0x10a4934: ldp s0, s1, [x8]
// 0x10a4938: ldr s2, [x8, #8]
// 0x10a493c: ldr s3, [x19, #0x3e0]
// 0x10a4940: ldp s4, s5, [x19, #0x74]
// 0x10a4944: ldr s6, [x19, #0x7c]
// 0x10a4948: ldr s11, [x19, #0x3d8]
// 0x10a494c: fmul s0, s0, s3
// 0x10a4950: fmul s1, s1, s3
// 0x10a4954: fmul s2, s2, s3
// 0x10a4958: mov x0, x21
// 0x10a495c: mov x1, xzr
// 0x10a4960: fneg s12, s4
// 0x10a4964: fneg s13, s5
// 0x10a4968: fadd s14, s8, s0
// 0x10a496c: fadd s9, s9, s1
// 0x10a4970: fadd s10, s10, s2
// 0x10a4974: fneg s8, s6
// 0x10a4978: bl #0x1b95168
// 0x10a497c: ldr x8, [x26]
// 0x10a4980: mov w23, w0
// 0x10a4984: ldr w9, [x8, #0xe0]
// 0x10a4988: cbnz w9, #0x10a4994
// 0x10a498c: mov x0, x8
// 0x10a4990: bl #0xf7da5c
// 0x10a4994: add x0, sp, #0xa0
// 0x10a4998: mov v0.16b, v14.16b
// 0x10a499c: mov v1.16b, v9.16b
// 0x10a49a0: mov v2.16b, v10.16b
// 0x10a49a4: mov v3.16b, v12.16b
// 0x10a49a8: mov v4.16b, v13.16b
// 0x10a49ac: mov v5.16b, v8.16b
// 0x10a49b0: mov v6.16b, v11.16b
// 0x10a49b4: mov w1, w23
// 0x10a49b8: mov x2, xzr
// 0x10a49bc: bl #0x1bcbc48
// 0x10a49c0: add x0, sp, #0xa0
// 0x10a49c4: mov x1, xzr
// 0x10a49c8: bl #0x1bced04
// 0x10a49cc: mov x0, x22
// 0x10a49d0: mov x1, xzr
// 0x10a49d4: mov v8.16b, v1.16b
// 0x10a49d8: bl #0x1bced04
// 0x10a49dc: fsub s0, s8, s1
// 0x10a49e0: fcmp s0, #0.0
// 0x10a49e4: b.ge #0x10a4c64
// 0x10a49e8: strb wzr, [x19, #0x229]
// 0x10a49ec: mov x0, xzr
// 0x10a49f0: bl #0x1bd6eac
// 0x10a49f4: adrp x24, #0x1e8c000
// 0x10a49f8: ldr x24, [x24, #0xd8]
// 0x10a49fc: mov x23, x0
// 0x10a4a00: ldr x8, [x24]
// 0x10a4a04: ldr w9, [x8, #0xe0]
// 0x10a4a08: cbnz w9, #0x10a4a14
// 0x10a4a0c: mov x0, x8
// 0x10a4a10: bl #0xf7da5c
// 0x10a4a14: mov x0, x23
// 0x10a4a18: mov x1, xzr
// 0x10a4a1c: bl #0x1b98274
// 0x10a4a20: tbz w0, #0, #0x10a4ab0
// 0x10a4a24: mov x0, xzr
// 0x10a4a28: bl #0x1bd6eac
// 0x10a4a2c: ldr x8, [x24]
// 0x10a4a30: mov x23, x0
// 0x10a4a34: ldr w9, [x8, #0xe0]
// 0x10a4a38: cbnz w9, #0x10a4a44
// 0x10a4a3c: mov x0, x8
// 0x10a4a40: bl #0xf7da5c
// 0x10a4a44: mov x0, x23
// 0x10a4a48: mov x1, xzr
// 0x10a4a4c: bl #0x1b98274
// 0x10a4a50: tbz w0, #0, #0x10a4afc
// 0x10a4a54: mov x0, x22
// 0x10a4a58: mov x1, xzr
// 0x10a4a5c: bl #0x1bcec58
// 0x10a4a60: cbz x0, #0x10a5704
// 0x10a4a64: mov x1, xzr
// 0x10a4a68: bl #0x1b92190
// 0x10a4a6c: mov x23, x0
// 0x10a4a70: mov x0, xzr
// 0x10a4a74: bl #0x1bd6eac
// 0x10a4a78: cbz x0, #0x10a5704
// 0x10a4a7c: mov x1, xzr
// 0x10a4a80: bl #0x1b92190
// 0x10a4a84: ldr x8, [x24]
// 0x10a4a88: mov x24, x0
// 0x10a4a8c: ldr w9, [x8, #0xe0]
// 0x10a4a90: cbnz w9, #0x10a4a9c
// 0x10a4a94: mov x0, x8
// 0x10a4a98: bl #0xf7da5c
// 0x10a4a9c: mov x0, x23
// 0x10a4aa0: mov x1, x24
// 0x10a4aa4: mov x2, xzr
// 0x10a4aa8: bl #0x1b94ac8
// 0x10a4aac: tbz w0, #0, #0x10a4afc
// 0x10a4ab0: ldr x23, [x19, #0x38]
// 0x10a4ab4: mov x0, x22
// 0x10a4ab8: mov x1, xzr
// 0x10a4abc: bl #0x1bcec58
// 0x10a4ac0: cbz x0, #0x10a5704
// 0x10a4ac4: mov x1, xzr
// 0x10a4ac8: bl #0x1b92190
// 0x10a4acc: cbz x0, #0x10a5704
// 0x10a4ad0: mov x1, xzr
// 0x10a4ad4: bl #0x1b92774
// 0x10a4ad8: cbz x23, #0x10a5704
// 0x10a4adc: str x0, [x23, #0x40]!
// 0x10a4ae0: mov x1, x0
// 0x10a4ae4: mov x0, x23
// 0x10a4ae8: bl #0xf7d8d0
// 0x10a4aec: ldr x8, [x19, #0x38]
// 0x10a4af0: cbz x8, #0x10a5704
// 0x10a4af4: mov w9, wzr
// 0x10a4af8: b #0x10a4b08
// 0x10a4afc: ldr x8, [x19, #0x38]
// 0x10a4b00: cbz x8, #0x10a5704
// 0x10a4b04: mov w9, #1
// 0x10a4b08: strb w9, [x8, #0x5c]
// 0x10a4b0c: ldr s0, [x19, #0xc0]
// 0x10a4b10: fmov s1, #0.50000000
// 0x10a4b14: fabs s0, s0
// 0x10a4b18: fcmp s0, s1
// 0x10a4b1c: fmov s0, #1.00000000
// 0x10a4b20: b.le #0x10a4b38
// 0x10a4b24: ldr s2, [x19, #0xc4]
// 0x10a4b28: fabs s2, s2
// 0x10a4b2c: fcmp s2, s1
// 0x10a4b30: b.le #0x10a4b38
// 0x10a4b34: ldr s0, [x19, #0xf0]
// 0x10a4b38: ldrb w8, [x19, #0x228]
// 0x10a4b3c: str s0, [x19, #0xec]
// 0x10a4b40: cbnz w8, #0x10a4b74
// 0x10a4b44: ldrb w8, [x19, #0x295]
// 0x10a4b48: cbnz w8, #0x10a4b74
// 0x10a4b4c: ldrb w8, [x19, #0x258]
// 0x10a4b50: cbnz w8, #0x10a4b74
// 0x10a4b54: ldr s8, [x19, #0x27c]
// 0x10a4b58: mov x0, xzr
// 0x10a4b5c: bl #0x1b9ad30
// 0x10a4b60: adrp x8, #0x832000
// 0x10a4b64: ldr s1, [x8, #0x3c8]
// 0x10a4b68: fadd s1, s8, s1
// 0x10a4b6c: fcmp s1, s0
// 0x10a4b70: b.le #0x10a4d50
// 0x10a4b74: ldr x8, [x19, #0x28]
// 0x10a4b78: cbz x8, #0x10a5704
// 0x10a4b7c: ldr s0, [x8, #0x20c]
// 0x10a4b80: fmov s1, #1.00000000
// 0x10a4b84: fcmp s0, s1
// 0x10a4b88: b.le #0x10a4b94
// 0x10a4b8c: ldrb w9, [x8, #0x3ce]
// 0x10a4b90: cbz w9, #0x10a4bc4
// 0x10a4b94: ldr s0, [x8, #0x20c]
// 0x10a4b98: fmov s1, #1.00000000
// 0x10a4b9c: fcmp s0, s1
// 0x10a4ba0: b.mi #0x10a4bac
// 0x10a4ba4: ldrb w8, [x8, #0x3ce]
// 0x10a4ba8: cbz w8, #0x10a4e54
// 0x10a4bac: ldr x0, [x19, #0x20]
// 0x10a4bb0: cbz x0, #0x10a5704
// 0x10a4bb4: mov w1, wzr
// 0x10a4bb8: mov x2, xzr
// 0x10a4bbc: bl #0x1b91660
// 0x10a4bc0: b #0x10a4e54
// 0x10a4bc4: ldr s1, [x19, #0xec]
// 0x10a4bc8: ldp s0, s2, [x19, #0xb8]
// 0x10a4bcc: ldr x0, [x19, #0x60]
// 0x10a4bd0: str wzr, [x19, #0x3f8]
// 0x10a4bd4: fmul s0, s0, s1
// 0x10a4bd8: fmul s2, s1, s2
// 0x10a4bdc: str s0, [x19, #0x3f4]
// 0x10a4be0: str s2, [x19, #0x3fc]
// 0x10a4be4: cbz x0, #0x10a5704
// 0x10a4be8: fmov s1, wzr
// 0x10a4bec: mov x1, xzr
// 0x10a4bf0: fmov s8, wzr
// 0x10a4bf4: bl #0x1b9e01c
// 0x10a4bf8: ldr s3, [x19, #0x120]
// 0x10a4bfc: ldr s4, [x19, #0x110]
// 0x10a4c00: mov v0.s[1], v1.s[0]
// 0x10a4c04: ldr s1, [x19, #0x10c]
// 0x10a4c08: fmul v0.2s, v0.2s, v3.s[0]
// 0x10a4c0c: fmul s2, s2, s3
// 0x10a4c10: ldr s3, [x19, #0xfc]
// 0x10a4c14: fmul v0.2s, v0.2s, v4.s[0]
// 0x10a4c18: fmul s2, s2, s4
// 0x10a4c1c: ldr s4, [x19, #0x104]
// 0x10a4c20: fmul v0.2s, v0.2s, v1.s[0]
// 0x10a4c24: fmul s1, s2, s1
// 0x10a4c28: ldr s2, [x19, #0x11c]
// 0x10a4c2c: fmul v0.2s, v0.2s, v3.s[0]
// 0x10a4c30: fmul v0.2s, v0.2s, v4.s[0]
// 0x10a4c34: fmul s1, s1, s3
// 0x10a4c38: fmul v0.2s, v0.2s, v2.s[0]
// 0x10a4c3c: str d0, [x25, #0x278]
// 0x10a4c40: ldrb w9, [x19, #0x22a]
// 0x10a4c44: ldrb w8, [x19, #0x295]
// 0x10a4c48: fmul s1, s1, s4
// 0x10a4c4c: fmul s1, s1, s2
// 0x10a4c50: str s1, [x19, #0x3fc]
// 0x10a4c54: cbz w9, #0x10a4c9c
// 0x10a4c58: cbz w8, #0x10a4c90
// 0x10a4c5c: mov w8, #1
// 0x10a4c60: b #0x10a4c9c
// 0x10a4c64: mov w8, #1
// 0x10a4c68: strb w8, [x19, #0x229]
// 0x10a4c6c: b #0x10a49ec
// 0x10a4c70: cbz x8, #0x10a5704
// 0x10a4c74: ldr s0, [x8, #0x20c]
// 0x10a4c78: fmov s1, #1.00000000
// 0x10a4c7c: fcmp s0, s1
// 0x10a4c80: b.pl #0x10a4d5c
// 0x10a4c84: fcmp s0, #0.0
// 0x10a4c88: b.ls #0x10a40a0
// 0x10a4c8c: b #0x10a40c8
// 0x10a4c90: ldrb w8, [x19, #0x258]
// 0x10a4c94: cbz w8, #0x10a519c
// 0x10a4c98: mov w8, wzr
// 0x10a4c9c: ldr s2, [x19, #0x22c]
// 0x10a4ca0: ldr s3, [x19, #0x230]
// 0x10a4ca4: ldr w9, [x19, #0x3f0]
// 0x10a4ca8: ldr s4, [x19, #0x234]
// 0x10a4cac: mov s5, v0.s[1]
// 0x10a4cb0: ldr s6, [x19, #0xe0]
// 0x10a4cb4: fsub s0, s0, s2
// 0x10a4cb8: fsub s2, s5, s3
// 0x10a4cbc: neg w10, w9
// 0x10a4cc0: scvtf s3, w9
// 0x10a4cc4: fsub s1, s1, s4
// 0x10a4cc8: scvtf s4, w10
// 0x10a4ccc: fcmp s0, s3
// 0x10a4cd0: fcsel s5, s3, s0, gt
// 0x10a4cd4: fcmp s0, s4
// 0x10a4cd8: fneg s7, s6
// 0x10a4cdc: fcsel s0, s5, s4, pl
// 0x10a4ce0: fcmp s2, s6
// 0x10a4ce4: fcsel s5, s6, s2, gt
// 0x10a4ce8: fcmp s2, s7
// 0x10a4cec: fcsel s2, s5, s7, pl
// 0x10a4cf0: fcmp s1, s3
// 0x10a4cf4: str s2, [x19, #0x404]
// 0x10a4cf8: fcsel s2, s3, s1, gt
// 0x10a4cfc: fcmp s1, s4
// 0x10a4d00: fcsel s2, s2, s4, pl
// 0x10a4d04: str s0, [x19, #0x400]
// 0x10a4d08: str s2, [x19, #0x408]
// 0x10a4d0c: cbz w8, #0x10a4e38
// 0x10a4d10: ldr x8, [x19, #0x30]
// 0x10a4d14: cbz x8, #0x10a5704
// 0x10a4d18: adrp x9, #0x832000
// 0x10a4d1c: ldr s1, [x8, #0xe0]
// 0x10a4d20: ldr s3, [x9, #0x3b8]
// 0x10a4d24: fcmp s1, s3
// 0x10a4d28: b.le #0x10a4d34
// 0x10a4d2c: ldr s8, [x19, #0x298]
// 0x10a4d30: b #0x10a4e38
// 0x10a4d34: ldrb w9, [x8, #0x8d]
// 0x10a4d38: cbz w9, #0x10a4e1c
// 0x10a4d3c: ldr s1, [x19, #0xe4]
// 0x10a4d40: mov w8, #0x3f800000
// 0x10a4d44: str w8, [x19, #0xc4]
// 0x10a4d48: fmov s3, #0.75000000
// 0x10a4d4c: b #0x10a4e34
// 0x10a4d50: ldr x8, [x19, #0x28]
// 0x10a4d54: cbnz x8, #0x10a4b94
// 0x10a4d58: b #0x10a5704
// 0x10a4d5c: ldr s0, [x19, #0x3bc]
// 0x10a4d60: ldr x8, [x19, #0x90]
// 0x10a4d64: str s0, [x19, #0x2cc]
// 0x10a4d68: cbz x8, #0x10a5704
// 0x10a4d6c: ldr x20, [x19, #0x238]
// 0x10a4d70: cbz x20, #0x10a5704
// 0x10a4d74: ldrb w21, [x8, #0x106]
// 0x10a4d78: mov x0, x20
// 0x10a4d7c: mov x1, xzr
// 0x10a4d80: bl #0x1bcfdf0
// 0x10a4d84: mov x0, xzr
// 0x10a4d88: mov v8.16b, v0.16b
// 0x10a4d8c: bl #0x1b89b60
// 0x10a4d90: ldr s1, [x19, #0x3c8]
// 0x10a4d94: cbz w21, #0x10a52c8
// 0x10a4d98: fadd s2, s9, s9
// 0x10a4d9c: b #0x10a52d0
// 0x10a4da0: adrp x8, #0x1e8e000
// 0x10a4da4: ldr x8, [x8, #0xd0]
// 0x10a4da8: mov x0, x22
// 0x10a4dac: mov x2, xzr
// 0x10a4db0: ldr x1, [x8]
// 0x10a4db4: bl #0x17f610c
// 0x10a4db8: tbnz w0, #0, #0x10a4490
// 0x10a4dbc: adrp x8, #0x1e8e000
// 0x10a4dc0: ldr x8, [x8, #0xe0]
// 0x10a4dc4: mov x0, x22
// 0x10a4dc8: mov x2, xzr
// 0x10a4dcc: ldr x1, [x8]
// 0x10a4dd0: bl #0x17f610c
// 0x10a4dd4: tbz w0, #0, #0x10a5360
// 0x10a4dd8: ldr x8, [x19, #0x38]
// 0x10a4ddc: cbz x8, #0x10a5704
// 0x10a4de0: adrp x9, #0x1e8c000
// 0x10a4de4: ldr x9, [x9, #0xd8]
// 0x10a4de8: ldr x22, [x8, #0x148]
// 0x10a4dec: ldr x0, [x9]
// 0x10a4df0: ldr w9, [x0, #0xe0]
// 0x10a4df4: cbnz w9, #0x10a4dfc
// 0x10a4df8: bl #0xf7da5c
// 0x10a4dfc: mov x0, x22
// 0x10a4e00: mov x1, xzr
// 0x10a4e04: bl #0x1b98274
// 0x10a4e08: tbz w0, #0, #0x10a4684
// 0x10a4e0c: ldr x8, [x19, #0x38]
// 0x10a4e10: cbz x8, #0x10a5704
// 0x10a4e14: ldr x1, [x8, #0x148]
// 0x10a4e18: b #0x10a44d0
// 0x10a4e1c: ldrb w8, [x8, #0x8f]
// 0x10a4e20: cbz w8, #0x10a4e38
// 0x10a4e24: ldr s1, [x19, #0xe4]
// 0x10a4e28: mov w8, #-0x40800000
// 0x10a4e2c: fmov s3, #-0.75000000
// 0x10a4e30: str w8, [x19, #0xc4]
// 0x10a4e34: fmul s8, s1, s3
// 0x10a4e38: ldr x0, [x19, #0x98]
// 0x10a4e3c: str s8, [x19, #0x404]
// 0x10a4e40: cbz x0, #0x10a5704
// 0x10a4e44: mov w1, #2
// 0x10a4e48: mov v1.16b, v8.16b
// 0x10a4e4c: mov x2, xzr
// 0x10a4e50: bl #0x1bcf5b8
// 0x10a4e54: ldrb w8, [x19, #0x295]
// 0x10a4e58: cbz w8, #0x10a4ef8
// 0x10a4e5c: ldr x0, [x19, #0x98]
// 0x10a4e60: cbz x0, #0x10a5704
// 0x10a4e64: mov w1, wzr
// 0x10a4e68: mov x2, xzr
// 0x10a4e6c: bl #0x1bcf250
// 0x10a4e70: ldr x0, [x19, #0x98]
// 0x10a4e74: cbz x0, #0x10a5704
// 0x10a4e78: mov x1, xzr
// 0x10a4e7c: bl #0x1bceef8
// 0x10a4e80: ldr s0, [x19, #0x224]
// 0x10a4e84: fcmp s1, s0
// 0x10a4e88: b.le #0x10a4ec8
// 0x10a4e8c: ldr x0, [x19, #0x98]
// 0x10a4e90: cbz x0, #0x10a5704
// 0x10a4e94: mov x1, xzr
// 0x10a4e98: bl #0x1bceef8
// 0x10a4e9c: ldr x0, [x19, #0x98]
// 0x10a4ea0: cbz x0, #0x10a5704
// 0x10a4ea4: ldr s3, [x19, #0x224]
// 0x10a4ea8: mov w8, #-0x3c060000
// 0x10a4eac: fmov s4, w8
// 0x10a4eb0: mov x1, xzr
// 0x10a4eb4: fcmp s1, s3
// 0x10a4eb8: fcsel s3, s3, s1, gt
// 0x10a4ebc: fcmp s1, s4
// 0x10a4ec0: fcsel s1, s3, s4, pl
// 0x10a4ec4: bl #0x1bcef98
// 0x10a4ec8: ldp x20, x19, [sp, #0x160]
// 0x10a4ecc: ldp x22, x21, [sp, #0x150]
// 0x10a4ed0: ldp x24, x23, [sp, #0x140]
// 0x10a4ed4: ldp x26, x25, [sp, #0x130]
// 0x10a4ed8: ldp x28, x27, [sp, #0x120]
// 0x10a4edc: ldp x29, x30, [sp, #0x110]
// 0x10a4ee0: ldp d9, d8, [sp, #0x100]
// 0x10a4ee4: ldp d11, d10, [sp, #0xf0]
// 0x10a4ee8: ldp d13, d12, [sp, #0xe0]
// 0x10a4eec: ldp d15, d14, [sp, #0xd0]
// 0x10a4ef0: add sp, sp, #0x170
// 0x10a4ef4: ret
// 0x10a4ef8: ldrb w8, [x19, #0x258]
// 0x10a4efc: cbz w8, #0x10a4fec
// 0x10a4f00: ldr s8, [x19, #0x260]
// 0x10a4f04: mov x0, xzr
// 0x10a4f08: bl #0x1b9ad30
// 0x10a4f0c: adrp x8, #0x832000
// 0x10a4f10: ldr s1, [x8, #0x4f4]
// 0x10a4f14: fadd s1, s8, s1
// 0x10a4f18: fcmp s1, s0
// 0x10a4f1c: b.le #0x10a5060
// 0x10a4f20: ldr s8, [x19, #0x2ac]
// 0x10a4f24: mov x0, xzr
// 0x10a4f28: bl #0x1b9ad30
// 0x10a4f2c: adrp x8, #0x832000
// 0x10a4f30: ldr s1, [x8, #0x550]
// 0x10a4f34: fadd s1, s8, s1
// 0x10a4f38: fcmp s1, s0
// 0x10a4f3c: b.le #0x10a4e5c
// 0x10a4f40: ldr s0, [x19, #0x394]
// 0x10a4f44: ldr s1, [x19, #0x398]
// 0x10a4f48: ldr s2, [x19, #0x7c]
// 0x10a4f4c: ldr s11, [x19, #0x3a0]
// 0x10a4f50: str s0, [sp, #0x70]
// 0x10a4f54: ldr s0, [x19, #0x39c]
// 0x10a4f58: ldr s12, [x19, #0x3a4]
// 0x10a4f5c: ldr s13, [x19, #0x3a8]
// 0x10a4f60: ldr s14, [x19, #0x3e0]
// 0x10a4f64: stp s0, s1, [sp, #0x5c]
// 0x10a4f68: ldp s0, s1, [x19, #0x74]
// 0x10a4f6c: ldr s9, [x19, #0x3d0]
// 0x10a4f70: mov x0, x21
// 0x10a4f74: mov x1, xzr
// 0x10a4f78: fneg s15, s0
// 0x10a4f7c: fneg s8, s1
// 0x10a4f80: fneg s10, s2
// 0x10a4f84: bl #0x1b95168
// 0x10a4f88: ldr x8, [x26]
// 0x10a4f8c: mov w21, w0
// 0x10a4f90: ldr w9, [x8, #0xe0]
// 0x10a4f94: cbnz w9, #0x10a4fa0
// 0x10a4f98: mov x0, x8
// 0x10a4f9c: bl #0xf7da5c
// 0x10a4fa0: ldp s0, s2, [sp, #0x58]
// 0x10a4fa4: ldr s1, [sp, #0x60]
// 0x10a4fa8: mov v3.16b, v11.16b
// 0x10a4fac: mov v4.16b, v12.16b
// 0x10a4fb0: fmul s6, s14, s0
// 0x10a4fb4: ldr s0, [sp, #0x70]
// 0x10a4fb8: mov v5.16b, v13.16b
// 0x10a4fbc: mov x0, x20
// 0x10a4fc0: mov w1, w21
// 0x10a4fc4: mov x2, xzr
// 0x10a4fc8: str s9, [sp, #0x10]
// 0x10a4fcc: stp s8, s10, [sp, #4]
// 0x10a4fd0: str s15, [sp]
// 0x10a4fd4: bl #0x1bcc8c8
// 0x10a4fd8: tbnz w0, #0, #0x10a4e5c
// 0x10a4fdc: ldr x0, [x19, #0x98]
// 0x10a4fe0: cbz x0, #0x10a5704
// 0x10a4fe4: ldr s1, [x19, #0x25c]
// 0x10a4fe8: b #0x10a5184
// 0x10a4fec: ldrb w8, [x19, #0x2dc]
// 0x10a4ff0: cbnz w8, #0x10a4ffc
// 0x10a4ff4: ldrb w8, [x19, #0x2d0]
// 0x10a4ff8: cbz w8, #0x10a5004
// 0x10a4ffc: ldrb w8, [x19, #0x228]
// 0x10a5000: cbnz w8, #0x10a5050
// 0x10a5004: ldr x0, [x26]
// 0x10a5008: ldr x20, [x19, #0x98]
// 0x10a500c: ldr w8, [x0, #0xe0]
// 0x10a5010: cbnz w8, #0x10a5018
// 0x10a5014: bl #0xf7da5c
// 0x10a5018: mov x0, xzr
// 0x10a501c: bl #0x1bcb1c0
// 0x10a5020: ldr x0, [x19, #0x98]
// 0x10a5024: cbz x0, #0x10a5704
// 0x10a5028: mov x1, xzr
// 0x10a502c: mov v8.16b, v1.16b
// 0x10a5030: bl #0x1bcf1d8
// 0x10a5034: cbz x20, #0x10a5704
// 0x10a5038: fmul s1, s8, s0
// 0x10a503c: fmov s0, wzr
// 0x10a5040: fmov s2, wzr
// 0x10a5044: mov x0, x20
// 0x10a5048: mov x1, xzr
// 0x10a504c: bl #0x1bcf668
// 0x10a5050: ldr x0, [x19, #0x98]
// 0x10a5054: cbz x0, #0x10a5704
// 0x10a5058: mov w1, #1
// 0x10a505c: b #0x10a4e68
// 0x10a5060: ldr x8, [x19, #0x30]
// 0x10a5064: cbz x8, #0x10a5704
// 0x10a5068: ldrb w9, [x8, #0x8d]
// 0x10a506c: cbz w9, #0x10a50c4
// 0x10a5070: ldrb w8, [x19, #0x257]
// 0x10a5074: cbz w8, #0x10a5154
// 0x10a5078: ldr s8, [x19, #0x25c]
// 0x10a507c: mov x0, xzr
// 0x10a5080: bl #0x1b89b60
// 0x10a5084: fmov s2, #3.00000000
// 0x10a5088: fmov s1, #4.00000000
// 0x10a508c: fsub s4, s2, s8
// 0x10a5090: ldrb w8, [x19, #0x256]
// 0x10a5094: fmul s3, s0, s1
// 0x10a5098: fnmul s0, s0, s1
// 0x10a509c: fcmp s4, #0.0
// 0x10a50a0: fabd s5, s2, s8
// 0x10a50a4: fcsel s0, s3, s0, ge
// 0x10a50a8: fadd s0, s8, s0
// 0x10a50ac: fcmp s5, s3
// 0x10a50b0: fcsel s1, s0, s2, hi
// 0x10a50b4: str s1, [x19, #0x25c]
// 0x10a50b8: cbz w8, #0x10a515c
// 0x10a50bc: strb wzr, [x19, #0x259]
// 0x10a50c0: b #0x10a515c
// 0x10a50c4: ldrb w8, [x8, #0x8f]
// 0x10a50c8: cbz w8, #0x10a5108
// 0x10a50cc: ldr s8, [x19, #0x25c]
// 0x10a50d0: mov x0, xzr
// 0x10a50d4: bl #0x1b89b60
// 0x10a50d8: fmov s2, #-3.00000000
// 0x10a50dc: fmov s1, #4.00000000
// 0x10a50e0: fsub s4, s2, s8
// 0x10a50e4: fmul s3, s0, s1
// 0x10a50e8: fnmul s0, s0, s1
// 0x10a50ec: fcmp s4, #0.0
// 0x10a50f0: fabd s5, s2, s8
// 0x10a50f4: fcsel s0, s3, s0, ge
// 0x10a50f8: fadd s0, s8, s0
// 0x10a50fc: fcmp s5, s3
// 0x10a5100: fcsel s1, s0, s2, hi
// 0x10a5104: b #0x10a514c
// 0x10a5108: ldrb w8, [x19, #0x257]
// 0x10a510c: cbz w8, #0x10a5154
// 0x10a5110: ldr s8, [x19, #0x25c]
// 0x10a5114: mov x0, xzr
// 0x10a5118: bl #0x1b89b60
// 0x10a511c: adrp x8, #0x832000
// 0x10a5120: ldr s1, [x8, #0x4ac]
// 0x10a5124: fmov s2, #4.00000000
// 0x10a5128: fmul s3, s0, s2
// 0x10a512c: fnmul s0, s0, s2
// 0x10a5130: fsub s2, s1, s8
// 0x10a5134: fcmp s2, #0.0
// 0x10a5138: fabd s4, s1, s8
// 0x10a513c: fcsel s0, s3, s0, ge
// 0x10a5140: fadd s0, s8, s0
// 0x10a5144: fcmp s4, s3
// 0x10a5148: fcsel s1, s0, s1, hi
// 0x10a514c: str s1, [x19, #0x25c]
// 0x10a5150: b #0x10a515c
// 0x10a5154: fmov s1, wzr
// 0x10a5158: str wzr, [x19, #0x25c]
// 0x10a515c: ldrb w8, [x19, #0x257]
// 0x10a5160: cbnz w8, #0x10a517c
// 0x10a5164: ldr x8, [x19, #0x30]
// 0x10a5168: cbz x8, #0x10a5704
// 0x10a516c: ldrb w8, [x8, #0x8d]
// 0x10a5170: cbnz w8, #0x10a517c
// 0x10a5174: mov w8, #1
// 0x10a5178: strb w8, [x19, #0x259]
// 0x10a517c: ldr x0, [x19, #0x98]
// 0x10a5180: cbz x0, #0x10a5704
// 0x10a5184: fmov s0, wzr
// 0x10a5188: fmov s2, wzr
// 0x10a518c: mov w1, #2
// 0x10a5190: mov x2, xzr
// 0x10a5194: bl #0x1bcf5b8
// 0x10a5198: b #0x10a4e5c
// 0x10a519c: ldrb w8, [x19, #0x229]
// 0x10a51a0: cbnz w8, #0x10a4e54
// 0x10a51a4: b #0x10a4c9c
// 0x10a51a8: mov w8, #-0x3da40000
// 0x10a51ac: fmov s2, w8
// 0x10a51b0: fcmp s1, s2
// 0x10a51b4: b.pl #0x10a52c0
// 0x10a51b8: mov w8, #0x42400000
// 0x10a51bc: fmov s2, w8
// 0x10a51c0: fdiv s1, s1, s2
// 0x10a51c4: fabs s1, s1
// 0x10a51c8: fmul s0, s0, s1
// 0x10a51cc: fmov s1, #1.00000000
// 0x10a51d0: fsub s0, s1, s0
// 0x10a51d4: b #0x10a4330
// 0x10a51d8: ldrb w9, [x19, #0x228]
// 0x10a51dc: cbz w9, #0x10a3d78
// 0x10a51e0: ldr x10, [x19, #0x28]
// 0x10a51e4: mov w9, #1
// 0x10a51e8: strb w9, [x19, #0x2b0]
// 0x10a51ec: cbz x10, #0x10a5704
// 0x10a51f0: strb wzr, [x10, #0x2d0]
// 0x10a51f4: strb w9, [x19, #0x2c8]
// 0x10a51f8: cbz w8, #0x10a3e3c
// 0x10a51fc: ldr s8, [x19, #0x140]
// 0x10a5200: fcmp s8, #0.0
// 0x10a5204: b.le #0x10a3e3c
// 0x10a5208: mov x0, xzr
// 0x10a520c: bl #0x1b89b60
// 0x10a5210: fsub s0, s8, s0
// 0x10a5214: b #0x10a3e38
// 0x10a5218: ldr s0, [x19, #0x394]
// 0x10a521c: ldr s1, [x19, #0x398]
// 0x10a5220: ldr s2, [x19, #0x7c]
// 0x10a5224: ldr s11, [x19, #0x3a0]
// 0x10a5228: str s0, [sp, #0x70]
// 0x10a522c: ldr s0, [x19, #0x39c]
// 0x10a5230: ldr s12, [x19, #0x3a4]
// 0x10a5234: ldr s13, [x19, #0x3a8]
// 0x10a5238: ldr s14, [x19, #0x3e0]
// 0x10a523c: stp s0, s1, [sp, #0x5c]
// 0x10a5240: ldp s0, s1, [x19, #0x74]
// 0x10a5244: ldr s9, [x19, #0x3d0]
// 0x10a5248: add x0, x19, #0x304
// 0x10a524c: mov x1, xzr
// 0x10a5250: add x20, x19, #0x33c
// 0x10a5254: fneg s15, s0
// 0x10a5258: fneg s8, s1
// 0x10a525c: fneg s10, s2
// 0x10a5260: bl #0x1b95168
// 0x10a5264: adrp x8, #0x1e8d000
// 0x10a5268: ldr x8, [x8, #0x4a8]
// 0x10a526c: mov w21, w0
// 0x10a5270: ldr x8, [x8]
// 0x10a5274: ldr w9, [x8, #0xe0]
// 0x10a5278: cbnz w9, #0x10a5284
// 0x10a527c: mov x0, x8
// 0x10a5280: bl #0xf7da5c
// 0x10a5284: ldr s0, [x24, #0x3bc]
// 0x10a5288: ldp s2, s1, [sp, #0x5c]
// 0x10a528c: mov v3.16b, v11.16b
// 0x10a5290: mov v4.16b, v12.16b
// 0x10a5294: fmul s6, s14, s0
// 0x10a5298: ldr s0, [sp, #0x70]
// 0x10a529c: mov v5.16b, v13.16b
// 0x10a52a0: mov x0, x20
// 0x10a52a4: mov w1, w21
// 0x10a52a8: mov x2, xzr
// 0x10a52ac: str s9, [sp, #0x10]
// 0x10a52b0: stp s8, s10, [sp, #4]
// 0x10a52b4: str s15, [sp]
// 0x10a52b8: bl #0x1bcc8c8
// 0x10a52bc: tbz w0, #0, #0x10a5334
// 0x10a52c0: str wzr, [x19, #0x298]
// 0x10a52c4: b #0x10a4334
// 0x10a52c8: ldr s2, [x24, #0x3bc]
// 0x10a52cc: fmul s2, s9, s2
// 0x10a52d0: fmul s0, s2, s0
// 0x10a52d4: fmov s2, #4.00000000
// 0x10a52d8: fmul s0, s0, s2
// 0x10a52dc: fadd s0, s8, s0
// 0x10a52e0: fcmp s0, s1
// 0x10a52e4: fcsel s0, s0, s1, mi
// 0x10a52e8: mov x0, x20
// 0x10a52ec: b #0x10a40c0
// 0x10a52f0: ldrb w8, [x19, #0x228]
// 0x10a52f4: cbz w8, #0x10a4118
// 0x10a52f8: ldr x8, [x19, #0x30]
// 0x10a52fc: cbz x8, #0x10a5704
// 0x10a5300: ldrb w9, [x8, #0x94]
// 0x10a5304: ldrb w8, [x8, #0x95]
// 0x10a5308: cbz w9, #0x10a5420
// 0x10a530c: cbnz w8, #0x10a4118
// 0x10a5310: ldr x0, [x19, #0x60]
// 0x10a5314: cbz x0, #0x10a5704
// 0x10a5318: ldrb w20, [x19, #0x2d0]
// 0x10a531c: mov x1, xzr
// 0x10a5320: bl #0x1b9d508
// 0x10a5324: cbz w20, #0x10a5448
// 0x10a5328: add x8, x19, #0x158
// 0x10a532c: mov v0.s[1], v1.s[0]
// 0x10a5330: b #0x10a546c
// 0x10a5334: ldr x8, [x19, #0x20]
// 0x10a5338: cbz x8, #0x10a5704
// 0x10a533c: ldr s0, [x8, #0x78]
// 0x10a5340: ldr s1, [x19, #0xdc]
// 0x10a5344: mov w8, #0x42400000
// 0x10a5348: fmov s2, w8
// 0x10a534c: fdiv s0, s0, s2
// 0x10a5350: fmul s0, s1, s0
// 0x10a5354: fmov s1, #1.00000000
// 0x10a5358: fadd s0, s0, s1
// 0x10a535c: b #0x10a4330
// 0x10a5360: adrp x8, #0x1e8e000
// 0x10a5364: ldr x8, [x8, #0xd8]
// 0x10a5368: mov x0, x22
// 0x10a536c: mov x2, xzr
// 0x10a5370: ldr x1, [x8]
// 0x10a5374: bl #0x17f610c
// 0x10a5378: tbz w0, #0, #0x10a53c0
// 0x10a537c: ldr x8, [x19, #0x38]
// 0x10a5380: cbz x8, #0x10a5704
// 0x10a5384: adrp x9, #0x1e8c000
// 0x10a5388: ldr x9, [x9, #0xd8]
// 0x10a538c: ldr x22, [x8, #0x140]
// 0x10a5390: ldr x0, [x9]
// 0x10a5394: ldr w9, [x0, #0xe0]
// 0x10a5398: cbnz w9, #0x10a53a0
// 0x10a539c: bl #0xf7da5c
// 0x10a53a0: mov x0, x22
// 0x10a53a4: mov x1, xzr
// 0x10a53a8: bl #0x1b98274
// 0x10a53ac: tbz w0, #0, #0x10a4684
// 0x10a53b0: ldr x8, [x19, #0x38]
// 0x10a53b4: cbz x8, #0x10a5704
// 0x10a53b8: ldr x1, [x8, #0x140]
// 0x10a53bc: b #0x10a44d0
// 0x10a53c0: adrp x8, #0x1e8e000
// 0x10a53c4: ldr x8, [x8, #0xc8]
// 0x10a53c8: mov x0, x22
// 0x10a53cc: mov x2, xzr
// 0x10a53d0: ldr x1, [x8]
// 0x10a53d4: bl #0x17f610c
// 0x10a53d8: ldr x8, [x19, #0x38]
// 0x10a53dc: cbz x8, #0x10a5704
// 0x10a53e0: adrp x9, #0x1e8c000
// 0x10a53e4: ldr x9, [x9, #0xd8]
// 0x10a53e8: tbz w0, #0, #0x10a44a0
// 0x10a53ec: ldr x0, [x9]
// 0x10a53f0: ldr x22, [x8, #0x158]
// 0x10a53f4: ldr w9, [x0, #0xe0]
// 0x10a53f8: cbnz w9, #0x10a5400
// 0x10a53fc: bl #0xf7da5c
// 0x10a5400: mov x0, x22
// 0x10a5404: mov x1, xzr
// 0x10a5408: bl #0x1b98274
// 0x10a540c: tbz w0, #0, #0x10a4684
// 0x10a5410: ldr x8, [x19, #0x38]
// 0x10a5414: cbz x8, #0x10a5704
// 0x10a5418: ldr x1, [x8, #0x158]
// 0x10a541c: b #0x10a44d0
// 0x10a5420: cbz w8, #0x10a4118
// 0x10a5424: ldr x0, [x19, #0x60]
// 0x10a5428: cbz x0, #0x10a5704
// 0x10a542c: ldrb w20, [x19, #0x2d0]
// 0x10a5430: mov x1, xzr
// 0x10a5434: bl #0x1b9d508
// 0x10a5438: cbz w20, #0x10a55ac
// 0x10a543c: add x8, x19, #0x158
// 0x10a5440: mov v0.s[1], v1.s[0]
// 0x10a5444: b #0x10a55d0
// 0x10a5448: ldr d3, [x19, #0x68]
// 0x10a544c: ldr s4, [x19, #0x3e0]
// 0x10a5450: ldr s5, [x19, #0x70]
// 0x10a5454: mov v0.s[1], v1.s[0]
// 0x10a5458: add x8, x19, #0x154
// 0x10a545c: fmul v1.2s, v3.2s, v4.s[0]
// 0x10a5460: fmul s3, s5, s4
// 0x10a5464: fadd v0.2s, v0.2s, v1.2s
// 0x10a5468: fadd s2, s2, s3
// 0x10a546c: ldr s1, [x8]
// 0x10a5470: str d0, [x25]
// 0x10a5474: ldr x0, [x19, #0x60]
// 0x10a5478: str s2, [x19, #0x184]
// 0x10a547c: str s1, [x19, #0x15c]
// 0x10a5480: cbz x0, #0x10a5704
// 0x10a5484: mov x1, xzr
// 0x10a5488: bl #0x1b9d508
// 0x10a548c: ldr x0, [x19, #0x238]
// 0x10a5490: cbz x0, #0x10a5704
// 0x10a5494: ldp s13, s10, [x19, #0x6c]
// 0x10a5498: ldr s14, [x19, #0x68]
// 0x10a549c: mov x1, xzr
// 0x10a54a0: mov v8.16b, v0.16b
// 0x10a54a4: mov v9.16b, v1.16b
// 0x10a54a8: mov v11.16b, v2.16b
// 0x10a54ac: bl #0x1bcfdf0
// 0x10a54b0: ldr s15, [x19, #0x3e0]
// 0x10a54b4: fmov s1, #0.50000000
// 0x10a54b8: ldr x0, [x19, #0x60]
// 0x10a54bc: fmul s0, s0, s1
// 0x10a54c0: fsub s0, s0, s15
// 0x10a54c4: fmul s1, s14, s0
// 0x10a54c8: fmul s2, s13, s0
// 0x10a54cc: fmul s0, s10, s0
// 0x10a54d0: fadd s10, s8, s1
// 0x10a54d4: fadd s9, s9, s2
// 0x10a54d8: fadd s8, s11, s0
// 0x10a54dc: str s10, [x19, #0x188]
// 0x10a54e0: str s9, [x19, #0x18c]
// 0x10a54e4: str s8, [x19, #0x190]
// 0x10a54e8: cbz x0, #0x10a5704
// 0x10a54ec: ldr s1, [x19, #0x17c]
// 0x10a54f0: ldr s0, [x19, #0x180]
// 0x10a54f4: mov x1, xzr
// 0x10a54f8: stp s1, s0, [sp, #0x5c]
// 0x10a54fc: ldr s0, [x19, #0x184]
// 0x10a5500: str s0, [sp, #0x70]
// 0x10a5504: bl #0x1b9d8c8
// 0x10a5508: ldr s11, [x19, #0x150]
// 0x10a550c: ldr s14, [x19, #0x15c]
// 0x10a5510: fneg s3, s0
// 0x10a5514: fneg s0, s1
// 0x10a5518: add x0, x19, #0x304
// 0x10a551c: mov x1, xzr
// 0x10a5520: stp s0, s3, [sp, #0x54]
// 0x10a5524: fneg s13, s2
// 0x10a5528: add x20, x19, #0x33c
// 0x10a552c: bl #0x1b95168
// 0x10a5530: adrp x8, #0x1e8d000
// 0x10a5534: ldr x8, [x8, #0x4a8]
// 0x10a5538: mov w21, w0
// 0x10a553c: ldr x8, [x8]
// 0x10a5540: ldr w9, [x8, #0xe0]
// 0x10a5544: cbnz w9, #0x10a5550
// 0x10a5548: mov x0, x8
// 0x10a554c: bl #0xf7da5c
// 0x10a5550: ldr s0, [x26, #0x390]
// 0x10a5554: ldr s2, [sp, #0x70]
// 0x10a5558: mov v3.16b, v10.16b
// 0x10a555c: mov v4.16b, v9.16b
// 0x10a5560: fmul s6, s15, s0
// 0x10a5564: fmul s0, s11, s14
// 0x10a5568: str s0, [sp, #0x10]
// 0x10a556c: ldr s0, [sp, #0x54]
// 0x10a5570: mov v5.16b, v8.16b
// 0x10a5574: mov x0, x20
// 0x10a5578: mov w1, w21
// 0x10a557c: stp s0, s13, [sp, #4]
// 0x10a5580: ldr s0, [sp, #0x58]
// 0x10a5584: mov x2, xzr
// 0x10a5588: str s0, [sp]
// 0x10a558c: ldp s0, s1, [sp, #0x5c]
// 0x10a5590: bl #0x1bcc8c8
// 0x10a5594: tbnz w0, #0, #0x10a4118
// 0x10a5598: ldr s0, [x19, #0x150]
// 0x10a559c: ldr s1, [x19, #0x15c]
// 0x10a55a0: fneg s0, s0
// 0x10a55a4: fmul s12, s1, s0
// 0x10a55a8: b #0x10a4118
// 0x10a55ac: ldr d3, [x19, #0x68]
// 0x10a55b0: ldr s4, [x19, #0x3e0]
// 0x10a55b4: ldr s5, [x19, #0x70]
// 0x10a55b8: mov v0.s[1], v1.s[0]
// 0x10a55bc: add x8, x19, #0x154
// 0x10a55c0: fmul v1.2s, v3.2s, v4.s[0]
// 0x10a55c4: fmul s3, s5, s4
// 0x10a55c8: fadd v0.2s, v0.2s, v1.2s
// 0x10a55cc: fadd s2, s2, s3
// 0x10a55d0: ldr s1, [x8]
// 0x10a55d4: str d0, [x25]
// 0x10a55d8: ldr x0, [x19, #0x60]
// 0x10a55dc: str s2, [x19, #0x184]
// 0x10a55e0: str s1, [x19, #0x15c]
// 0x10a55e4: cbz x0, #0x10a5704
// 0x10a55e8: mov x1, xzr
// 0x10a55ec: bl #0x1b9d508
// 0x10a55f0: ldr x0, [x19, #0x238]
// 0x10a55f4: cbz x0, #0x10a5704
// 0x10a55f8: ldp s14, s10, [x19, #0x6c]
// 0x10a55fc: ldr s15, [x19, #0x68]
// 0x10a5600: mov x1, xzr
// 0x10a5604: mov v8.16b, v0.16b
// 0x10a5608: mov v9.16b, v1.16b
// 0x10a560c: mov v11.16b, v2.16b
// 0x10a5610: bl #0x1bcfdf0
// 0x10a5614: ldr s13, [x19, #0x3e0]
// 0x10a5618: fmov s1, #0.50000000
// 0x10a561c: ldr x0, [x19, #0x60]
// 0x10a5620: fmul s0, s0, s1
// 0x10a5624: fsub s0, s0, s13
// 0x10a5628: fmul s1, s15, s0
// 0x10a562c: fmul s2, s14, s0
// 0x10a5630: fmul s0, s10, s0
// 0x10a5634: fadd s10, s8, s1
// 0x10a5638: fadd s9, s9, s2
// 0x10a563c: fadd s8, s11, s0
// 0x10a5640: str s10, [x19, #0x188]
// 0x10a5644: str s9, [x19, #0x18c]
// 0x10a5648: str s8, [x19, #0x190]
// 0x10a564c: cbz x0, #0x10a5704
// 0x10a5650: ldr s1, [x19, #0x17c]
// 0x10a5654: ldr s0, [x19, #0x180]
// 0x10a5658: mov x1, xzr
// 0x10a565c: stp s1, s0, [sp, #0x5c]
// 0x10a5660: ldr s0, [x19, #0x184]
// 0x10a5664: str s0, [sp, #0x70]
// 0x10a5668: bl #0x1b9d8c8
// 0x10a566c: ldr s14, [x19, #0x150]
// 0x10a5670: ldr s15, [x19, #0x15c]
// 0x10a5674: add x0, x19, #0x304
// 0x10a5678: mov x1, xzr
// 0x10a567c: stp s1, s0, [sp, #0x54]
// 0x10a5680: mov v11.16b, v2.16b
// 0x10a5684: add x20, x19, #0x33c
// 0x10a5688: bl #0x1b95168
// 0x10a568c: adrp x8, #0x1e8d000
// 0x10a5690: ldr x8, [x8, #0x4a8]
// 0x10a5694: mov w21, w0
// 0x10a5698: ldr x8, [x8]
// 0x10a569c: ldr w9, [x8, #0xe0]
// 0x10a56a0: cbnz w9, #0x10a56ac
// 0x10a56a4: mov x0, x8
// 0x10a56a8: bl #0xf7da5c
// 0x10a56ac: ldr s0, [x26, #0x390]
// 0x10a56b0: ldr s2, [sp, #0x70]
// 0x10a56b4: mov v3.16b, v10.16b
// 0x10a56b8: mov v4.16b, v9.16b
// 0x10a56bc: fmul s6, s13, s0
// 0x10a56c0: fmul s0, s14, s15
// 0x10a56c4: str s0, [sp, #0x10]
// 0x10a56c8: ldr s0, [sp, #0x54]
// 0x10a56cc: mov v5.16b, v8.16b
// 0x10a56d0: mov x0, x20
// 0x10a56d4: mov w1, w21
// 0x10a56d8: stp s0, s11, [sp, #4]
// 0x10a56dc: ldr s0, [sp, #0x58]
// 0x10a56e0: mov x2, xzr
// 0x10a56e4: str s0, [sp]
// 0x10a56e8: ldp s0, s1, [sp, #0x5c]
// 0x10a56ec: bl #0x1bcc8c8
// 0x10a56f0: tbnz w0, #0, #0x10a4118
// 0x10a56f4: ldr s0, [x19, #0x150]
// 0x10a56f8: ldr s1, [x19, #0x15c]
// 0x10a56fc: fmul s12, s0, s1
// 0x10a5700: b #0x10a4118
// 0x10a5704: bl #0xf7db74
```

## `FPSRigidBodyWalker.CalculateFallingDamage` — RVA `0xca5708`

- Decompiled symbol: `FPSRigidBodyWalker_CalculateFallingDamage`
- Metadata signature: `private void CalculateFallingDamage(float fallDistance) { }`
- Native interval: `56` bytes
- Result: `pseudocode`
- Heuristic layout hint: `FPSRigidBodyWalker_Recovered` matched 2 offsets against `FPSRigidBodyWalker` metadata (confidence 1.00).

```c
typedef struct struct_0 {
    char padding_0[40];
    void* field_28;
    char padding_30[600];
    unsigned int field_288;
} struct_0;

typedef struct FPSRigidBodyWalker_Recovered {
    char padding_0[200];
    unsigned long long InputYLerpSpeed;
    char padding_d0[96];
    char limitedSprint;
} FPSRigidBodyWalker_Recovered;

void FPSRigidBodyWalker_CalculateFallingDamage(struct_0 *ptr, unsigned long a1)
{
    unsigned int v0;  // s1
    unsigned long v1;  // 4134

    v0 = ptr->field_288;
    v1 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v0, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v0, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v0, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v0, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v0, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v0, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if ((char)v1)
        return;
    if (ptr->field_28)
    {
        FPSPlayer__ApplyDamage(ptr->field_28, NULL, 0);
        return;
    }
    sub_f7db74(0);
}
```

## `FPSRigidBodyWalker.OnCollisionExit` — RVA `0xca5740`

- Decompiled symbol: `FPSRigidBodyWalker_OnCollisionExit`
- Metadata signature: `private void OnCollisionExit(Collision col) { }`
- Native interval: `560` bytes
- Result: `pseudocode`
- Heuristic layout hint: `FPSRigidBodyWalker_Recovered` matched 9 offsets against `FPSRigidBodyWalker` metadata (confidence 1.00).

```c
typedef struct struct_3 {
    char padding_0[40];
    struct struct_1 *field_28;
    char padding_30[24];
    struct struct_3 *field_48;
    char padding_50[8];
    struct struct_3 *field_58;
    struct struct_3 *field_60;
    char padding_68[56];
    char field_a0;
    char padding_a1[15];
    struct struct_2 *field_b0;
    char padding_b8[370];
    char field_22a;
    char padding_22b[41];
    unsigned short field_254;
    char padding_256[154];
    unsigned int field_2f0;
} struct_3;

typedef struct struct_6 {
    char padding_0[520];
    char field_208;
} struct_6;

typedef struct struct_9 {
    char padding_0[184];
    struct FPSRigidBodyWalker_Recovered *field_b8;
} struct_9;

typedef struct struct_1 {
    char padding_0[520];
    char field_208;
} struct_1;

typedef struct struct_2 {
    char padding_0[184];
    struct struct_3 *field_b8;
} struct_2;

typedef struct FPSRigidBodyWalker_Recovered {
    char padding_0[40];
    struct struct_7 *FPSPlayerComponent;
    char padding_30[24];
    struct FPSRigidBodyWalker_Recovered *mainObj;
    char padding_50[8];
    struct FPSRigidBodyWalker_Recovered *CameraObj;
    struct FPSRigidBodyWalker_Recovered *myTransform;
    char padding_68[56];
    char playerParented;
    char padding_a1[15];
    struct struct_9 *PlayerCharacterComponent;
    char padding_b8[370];
    char capsuleTooSteep;
    char padding_22b[41];
    unsigned short parentState;
    char padding_256[154];
    unsigned int lowpos;
} FPSRigidBodyWalker_Recovered;

typedef struct struct_7 {
    char padding_0[520];
    char field_208;
} struct_7;

typedef struct struct_4 {
    char padding_0[16];
    unsigned int field_10;
} struct_4;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

typedef struct struct_5 {
    char padding_0[184];
    struct struct_4 *field_b8;
} struct_5;

extern struct_0 *g_1ef0c58;
extern struct_5 *g_1ef22e8;
extern long long g_1efec68;
extern long long g_1efec70;
extern char g_1fab1e1;
extern char g_1fab4bb;

long long FPSRigidBodyWalker_OnCollisionExit(struct_3 *ptr, long long a1)
{
    struct_3 *v0;  // x0
    struct_3 *v1;  // x0
    struct_3 *v2;  // x0
    long long v3;  // x0
    long long v4;  // x0
    struct_3 *v5;  // x20
    struct_3 *v6;  // x20
    unsigned int v7;  // s1
    unsigned long v8;  // x0

    v0 = ptr;
    if (!(g_1fab4bb & 1))
    {
        sub_f7d92c(&g_1efec68);
        sub_f7d92c(&g_1efec70);
        v1 = sub_f7d92c(&g_1ef0c58);
        g_1fab4bb = 1;
        v0 = v1;
    }
    v2 = v0;
    if (!ptr->field_a0)
    {
LABEL_10a5940:
        v2 = ptr->field_60;
        ptr->field_254 = 0;
        ptr->field_22a = 0;
        if (v2)
        {
            v8 = Transform__get_position(v2, 0);
            ptr->field_2f0 = v7;
            return v8;
        }
    }
    else if (a1 && (v2 = (struct_3 *)(unsigned long long)Collision__get_gameObject(a1, 0), v2))
    {
        v3 = sub_1249224();
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        v2 = Object__op_Implicit(v3, 0);
        if (!((char)v2 & 1))
        {
            v2 = Collision__get_gameObject(a1, 0);
            if (v2)
            {
                v4 = sub_1249224();
                if (!g_1ef0c58->field_e0)
                    sub_f7da5c(g_1ef0c58);
                v2 = Object__op_Implicit(v4, 0);
                if ((v2 & 1))
                    goto LABEL_10a5830;
                goto LABEL_10a5940;
            }
        }
        else
        {
LABEL_10a5830:
            if (ptr->field_28)
            {
                v5 = ptr->field_60;
                if (!ptr->field_28->field_208)
                {
                    v2 = ptr->field_48;
                    if (v2 && (v2 = (struct_3 *)GameObject__get_transform(v2, 0), v5) && (Transform__set_parent(v5), v2 = (struct_3 *)ptr->field_58, v2 && (v2 = (struct_3 *)GameObject__get_transform(v2, 0), v2)))
                    {
                        Transform__set_parent();
                        if (!g_1ef0c58->field_e0)
                            sub_f7da5c(g_1ef0c58);
                        v2 = Object__op_Implicit(ptr->field_b0, 0);
                        if (!((char)v2 & 1))
                        {
LABEL_10a58e0:
                            v2 = ptr->field_58;
                            if (v2)
                            {
                                v2 = GameObject__get_transform(v2, 0);
                                v6 = v2;
                                if (!g_1fab1e1)
                                {
                                    v2 = sub_f7d92c(&g_1ef22e8);
                                    g_1fab1e1 = 1;
                                }
                                if (v6)
                                {
                                    v7 = g_1ef22e8->field_b8->field_10;
                                    Transform__set_localScale(v6, 0);
                                    ptr->field_a0 = 0;
                                    goto LABEL_10a5940;
                                }
                            }
                        }
                        else if (ptr->field_b0 && (v2 = (struct_3 *)ptr->field_b0->field_b8, v2 && (v2 = (struct_3 *)GameObject__get_transform(v2, 0), v2)))
                        {
                            Transform__set_parent();
                            goto LABEL_10a58e0;
                        }
                    }
                }
            }
        }
    }
    sub_f7db74(v2);
}
```

## `FPSRigidBodyWalker.OnCollisionEnter` — RVA `0xca5970`

- Decompiled symbol: `FPSRigidBodyWalker_OnCollisionEnter`
- Metadata signature: `private void OnCollisionEnter(Collision col) { }`
- Native interval: `1024` bytes
- Result: `pseudocode`
- Heuristic layout hint: `FPSRigidBodyWalker_Recovered` matched 8 offsets against `FPSRigidBodyWalker` metadata (confidence 0.80).

```c
typedef struct FPSRigidBodyWalker_Recovered {
    char padding_0[88];
    void* CameraObj;
    long long myTransform;
    unsigned int upVec;
    unsigned int field_6c;
    unsigned int field_70;
    char padding_74[44];
    char playerParented;
    char padding_a1[15];
    struct struct_1 *PlayerCharacterComponent;
    char padding_b8[384];
    void* capsule;
    char padding_240[20];
    char parentState;
    char padding_255[395];
    unsigned int capsuleCheckRadius;
} FPSRigidBodyWalker_Recovered;

typedef struct struct_3 {
    char padding_0[224];
    unsigned int field_e0;
} struct_3;

typedef struct struct_1 {
    char padding_0[184];
    void* field_b8;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern long long g_1ef22e8;
extern long long g_1efec68;
extern long long g_1efec70;
extern char g_1fab1e1;
extern char g_1fab3e2;
extern char g_1fab4bc;

void* FPSRigidBodyWalker_OnCollisionEnter(struct_2 *ptr, long long a1, unsigned long a2, unsigned long a3, unsigned long a4, unsigned long a5, unsigned long a6, unsigned long a7, char a8, unsigned long a9, unsigned int a10, unsigned long a11, unsigned int a12)
{
    void* addr;  // x0
    unsigned int v8;  // w8
    unsigned long v16;  // 4125
    unsigned int v17;  // s12
    unsigned int v18;  // s15
    unsigned int v19;  // s11
    unsigned int v20;  // s0
    unsigned long v21;  // 4279
    struct_3 *v22;  // x0
    unsigned int v23;  // s1
    unsigned int v24;  // s0
    void* p;  // x21
    unsigned int v25;  // s1
    unsigned long v26;  // 4221
    unsigned int v27;  // s8
    unsigned int v28;  // s0
    unsigned long v29;  // 4157
    long long v30;  // x0
    long long v31;  // x0
    long long v32;  // x24
    long long v33;  // x24
    void* v34;  // x24
    unsigned int v10;  // s13
    unsigned long i;  // x25
    unsigned long cur;  // x29
    int v13;  // q1
    int v14;  // q0
    int v15;  // q2
    unsigned int v0;  // [bp-0xec]
    unsigned int v1;  // [bp-0xe4]
    unsigned int v2;  // [bp-0xd8]
    int v3;  // [bp-0xd0], Other Possible Types: uint128_t
    int v4;  // [bp-0xc0], Other Possible Types: uint128_t
    int v5;  // [bp-0xb0], Other Possible Types: uint128_t
    unsigned long v6;  // [bp-0x60]

    v6 = &vvar_8;
    if (!(g_1fab4bc & 1))
    {
        sub_f7d92c(&g_1efec68);
        sub_f7d92c(&g_1efec70);
        sub_f7d92c(&g_1ef0c58);
        g_1fab4bc = 1;
    }
    v4 = 0;
    v5 = 0;
    v3 = 0;
    addr = ptr->field_238;
    if (addr && !((addr = (void*)Collider__get_bounds(addr, 0), !a1 || (addr = (void*)(unsigned long long)Collision__get_contacts(a1, 0), !addr))))
    {
        p = addr;
        if ((int)(long long)addr[24] < 1)
            return addr;
        v10 = v1 - v2 + ptr->field_3e0;
        v0 = 1113927393;
        i = 0;
        cur = p + 32;
        while (v8 > i)
        {
            v13 = (int)*((int128_t *)(cur + 16));
            v14 = (int)*((int128_t *)(cur + 32));
            v15 = (int)*((int128_t *)cur);
            v4 = v13;
            v5 = v14;
            v3 = v15;
            addr = ContactPoint__get_point(&v3, 0);
            v16 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(*((unsigned int *)(void*)&v13), v10)) >> 5 & 3 | (unsigned long long)(CmpF(*((unsigned int *)(void*)&v13), v10) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(*((unsigned int *)(void*)&v13), v10)) >> 5 & 3 | (unsigned long long)(CmpF(*((unsigned int *)(void*)&v13), v10) & 1)) & ((unsigned long long)(char)(CmpF(*((unsigned int *)(void*)&v13), v10)) >> 5 & 3 | (unsigned long long)(CmpF(*((unsigned int *)(void*)&v13), v10) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
            if (!((char)v16) && !ptr->field_254)
            {
                ContactPoint__get_normal(&v3, 0);
                v17 = ptr->field_68;
                v18 = ptr->field_6c;
                v19 = ptr->field_70;
                if (!g_1fab3e2)
                {
                    sub_f7d92c("_F");
                    g_1fab3e2 = 1;
                }
                if (!g_1ef07e8->field_e0)
                    sub_f7da5c(g_1ef07e8);
                v20 = [D] unsupported_Iop_SqrtF32();
                v21 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(v20, 646978941)) >> 5 & 3 | (unsigned long long)(CmpF(v20, 646978941) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v20, 646978941)) >> 5 & 3 | (unsigned long long)(CmpF(v20, 646978941) & 1)) & ((unsigned long long)(char)(CmpF(v20, 646978941)) >> 5 & 3 | (unsigned long long)(CmpF(v20, 646978941) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                if (!((char)v21))
                {
                    v22 = g_1ef07e8;
                    v23 = *((unsigned int *)&v14) * v17 + *((unsigned int *)&v13) * v18;
                    v24 = (*((unsigned int *)&v15) * v19 + *((unsigned int *)&v14) * v17 + *((unsigned int *)&v13) * v18) / v20;
                    v25 = [D] unsupported_Iop_ZeroHI96ofV128();
                    v26 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v24, 0xbf800000)) >> 5 & 3 | (unsigned long long)(CmpF(v24, 0xbf800000) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF((*((unsigned int *)(void*)&v15) * v19 + v23) / v20, 0xbf800000)) >> 5 & 3 | (unsigned long long)(CmpF((*((unsigned int *)(void*)&v15) * v19 + *((unsigned int *)(void*)&v14) * v17 + *((unsigned int *)(void*)&v13) * v18) / v20, 0xbf800000) & 1)) & ((unsigned long long)(char)(CmpF(v24, 0xbf800000)) >> 5 & 3 | (unsigned long long)(CmpF((*((unsigned int *)(void*)&v15) * v19 + v23) / v20, 0xbf800000) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                    if ((char)v26)
                        v27 = v25;
                    else
                        v27 = 0xbf800000;
                    if (!g_1ef07e8->field_e0)
                        v22 = sub_f7da5c(g_1ef07e8);
                    addr = acos(v22);
                    v28 = v27 * v0;
                    v29 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v28, 0x428c0000)) >> 5 & 3 | (unsigned long long)(CmpF(v28, 0x428c0000) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF((unsigned int)(unsigned long long)v27 * v0, 0x428c0000)) >> 5 & 3 | (unsigned long long)(CmpF((unsigned int)(unsigned long long)v27 * v0, 0x428c0000) & 1)) & ((unsigned long long)(char)(CmpF((unsigned int)(unsigned long long)v27 * v0, 0x428c0000)) >> 5 & 3 | (unsigned long long)(CmpF((unsigned int)(unsigned long long)v27 * v0, 0x428c0000) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                    if ((char)v29)
                        goto LABEL_10a5d24;
                }
                if (!Collision__get_gameObject(a1, 0))
                    goto LABEL_10a5d68;
                v30 = sub_1249224();
                if (!g_1ef0c58->field_e0)
                    sub_f7da5c(g_1ef0c58);
                if (!((char)Object__op_Implicit(v30, 0) & 1))
                {
                    if (!Collision__get_gameObject(a1, 0))
                        goto LABEL_10a5d68;
                    v31 = sub_1249224();
                    if (!g_1ef0c58->field_e0)
                        sub_f7da5c(g_1ef0c58);
                    addr = Object__op_Implicit(v31, 0);
                    if (!(addr & 1))
                        goto LABEL_10a5d24;
                }
                addr = Collision__get_transform(a1, 0);
                if (!ptr->field_60 || !((Transform__set_parent(ptr->field_60, addr, 0), addr = ptr->field_58, addr)))
                    goto LABEL_10a5d68;
                v32 = GameObject__get_transform(addr, 0);
                if (!v32)
                    goto LABEL_10a5d68;
                Transform__set_parent(v32, Collision__get_transform(a1, 0), 0);
                if (!g_1ef0c58->field_e0)
                    sub_f7da5c(g_1ef0c58);
                if (((char)Object__op_Implicit(ptr->field_b0, 0) & 1))
                {
                    if (!ptr->field_b0 || !((addr = ptr->field_b0->field_b8, addr)))
                        goto LABEL_10a5d68;
                    v33 = GameObject__get_transform(addr, 0);
                    if (!v33)
                        goto LABEL_10a5d68;
                    Transform__set_parent(v33, Collision__get_transform(a1, 0), 0);
                }
                addr = ptr->field_58;
                if (!addr)
                    goto LABEL_10a5d68;
                addr = GameObject__get_transform(addr, 0);
                v34 = addr;
                if (!g_1fab1e1)
                {
                    addr = sub_f7d92c(&g_1ef22e8);
                    g_1fab1e1 = 1;
                }
                if (!v34)
                    goto LABEL_10a5d68;
                addr = Transform__set_localScale(v34, 0);
                ptr->field_a0 = 1;
                ptr->field_254 = 1;
            }
LABEL_10a5d24:
            cur += 48;
            if (i + 1 >= (int)p[24])
                return addr;
        }
    }
    else
    {
LABEL_10a5d68:
        addr = sub_f7db74(addr);
    }
    sub_f7db7c(addr);
}
```

## `FPSRigidBodyWalker.OnCollisionStay` — RVA `0xca5d70`

- Decompiled symbol: `FPSRigidBodyWalker_OnCollisionStay`
- Metadata signature: `private void OnCollisionStay(Collision col) { }`
- Native interval: `644` bytes
- Result: `pseudocode`
- Heuristic layout hint: `FPSRigidBodyWalker_Recovered` matched 7 offsets against `FPSRigidBodyWalker` metadata (confidence 0.78).

```c
typedef struct FPSRigidBodyWalker_Recovered {
    char padding_0[104];
    unsigned int upVec;
    unsigned int field_6c;
    unsigned int field_70;
    char padding_74[312];
    unsigned int slopeLimit;
    char padding_1b0[122];
    char capsuleTooSteep;
    char padding_22b[13];
    void* capsule;
    char padding_240[21];
    char inWater;
    char padding_256[154];
    unsigned int lowpos;
    char padding_2f4[236];
    unsigned int capsuleCheckRadius;
} FPSRigidBodyWalker_Recovered;

extern char g_1fab3e2;

void* FPSRigidBodyWalker_OnCollisionStay(struct_0 *ptr, long long a1)
{
    void* addr;  // x0
    unsigned int v8;  // w8
    unsigned int v17;  // s0
    unsigned long v18;  // 4129
    unsigned int v19;  // s14
    unsigned int v20;  // s12
    unsigned int v21;  // s15
    unsigned int v22;  // s0
    unsigned int v23;  // s1
    unsigned long v24;  // 4279
    void* v25;  // x0
    unsigned int v26;  // s1
    void* p;  // x20
    unsigned int v27;  // s0
    unsigned int v28;  // s1
    unsigned long v29;  // 4221
    unsigned int v30;  // s8
    unsigned int v31;  // s0
    unsigned long v32;  // 4140
    unsigned int v33;  // s8
    unsigned long v35;  // 4163
    char v36;  // x8
    unsigned int v10;  // s13
    unsigned long v11;  // x22
    unsigned long cur;  // x23
    int v13;  // q1
    int v14;  // q2
    void* v15;  // x0
    unsigned long v16;  // 4125
    unsigned int v0;  // [bp-0xd0]
    unsigned int v1;  // [bp-0xcc]
    unsigned int v2;  // [bp-0xc4]
    unsigned int v3;  // [bp-0xb8]
    int v4;  // [bp-0xb0], Other Possible Types: uint128_t
    int v5;  // [bp-0xa0], Other Possible Types: uint128_t
    int v6;  // [bp-0x90], Other Possible Types: uint128_t

    v5 = 0;
    v6 = 0;
    v4 = 0;
    addr = ptr->field_238;
    if (addr)
    {
        addr = Collider__get_bounds(addr, 0);
        if (a1)
        {
            addr = Collision__get_contacts(a1, 0);
            if (addr)
            {
                v8 = (long long)addr[24];
                p = addr;
                if (v8 < 1)
                    return addr;
                v10 = v2 - v3 + ptr->field_3e0;
                v11 = 0;
                cur = p + 32;
                v1 = 1113927393;
                v0 = 3192704205;
                while (true)
                {
                    if (v8 <= v11)
                    {
                        addr = sub_f7db7c();
                        break;
                    }
                    v13 = (int)*((int128_t *)(cur + 16));
                    v14 = (int)*((int128_t *)cur);
                    v5 = v13;
                    v6 = (int)*((int128_t *)(cur + 32));
                    v4 = v14;
                    v15 = ContactPoint__get_point(&v4, 0);
                    v16 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(*((unsigned int *)(void*)&v13), v10)) >> 5 & 3 | (unsigned long long)(CmpF(*((unsigned int *)(void*)&v13), v10) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(*((unsigned int *)(void*)&v13), v10)) >> 5 & 3 | (unsigned long long)(CmpF(*((unsigned int *)(void*)&v13), v10) & 1)) & ((unsigned long long)(char)(CmpF(*((unsigned int *)(void*)&v13), v10)) >> 5 & 3 | (unsigned long long)(CmpF(*((unsigned int *)(void*)&v13), v10) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                    if (!((char)v16))
                    {
                        ContactPoint__get_point(&v4, 0);
                        v17 = ptr->field_2f0;
                        v18 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(*((unsigned int *)(void*)&v13), v17)) >> 5 & 3 | (unsigned long long)(CmpF(*((unsigned int *)(void*)&v13), v17) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(*((unsigned int *)(void*)&v13), v17)) >> 5 & 3 | (unsigned long long)(CmpF(*((unsigned int *)(void*)&v13), v17) & 1)) & ((unsigned long long)(char)(CmpF(*((unsigned int *)(void*)&v13), v17)) >> 5 & 3 | (unsigned long long)(CmpF(*((unsigned int *)(void*)&v13), v17) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                        if (!((char)v18))
                        {
                            ContactPoint__get_point(&v4, 0);
                            ptr->field_2f0 = *((unsigned int *)&v13);
                        }
                        ContactPoint__get_normal(&v4, 0);
                        v19 = ptr->field_68;
                        v20 = ptr->field_6c;
                        v21 = ptr->field_70;
                        if (!g_1fab3e2)
                        {
                            sub_f7d92c("_F");
                            g_1fab3e2 = 1;
                        }
                        v15 = g_1ef07e8;
                        if (!(int)g_1ef07e8[224])
                            v15 = sub_f7da5c(g_1ef07e8);
                        v22 = [D] unsupported_Iop_SqrtF32();
                        v23 = 0;
                        v24 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(v22, 646978941)) >> 5 & 3 | (unsigned long long)(CmpF(v22, 646978941) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v22, 646978941)) >> 5 & 3 | (unsigned long long)(CmpF(v22, 646978941) & 1)) & ((unsigned long long)(char)(CmpF(v22, 646978941)) >> 5 & 3 | (unsigned long long)(CmpF(v22, 646978941) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                        if (!((char)v24))
                        {
                            v25 = g_1ef07e8;
                            v26 = v17 * v19 + *((unsigned int *)&v13) * v20;
                            v27 = (*((unsigned int *)&v14) * v21 + v17 * v19 + *((unsigned int *)&v13) * v20) / v22;
                            v28 = [D] unsupported_Iop_ZeroHI96ofV128();
                            v29 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v27, 0xbf800000)) >> 5 & 3 | (unsigned long long)(CmpF(v27, 0xbf800000) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF((*((unsigned int *)(void*)&v14) * v21 + v26) / v22, 0xbf800000)) >> 5 & 3 | (unsigned long long)(CmpF((*((unsigned int *)(void*)&v14) * v21 + v17 * v19 + *((unsigned int *)(void*)&v13) * v20) / v22, 0xbf800000) & 1)) & ((unsigned long long)(char)(CmpF(v27, 0xbf800000)) >> 5 & 3 | (unsigned long long)(CmpF((*((unsigned int *)(void*)&v14) * v21 + v26) / v22, 0xbf800000) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                            if ((char)v29)
                                v30 = v28;
                            else
                                v30 = 0xbf800000;
                            if (!(int)g_1ef07e8[224])
                                v25 = sub_f7da5c(g_1ef07e8);
                            v15 = acos(v25);
                            v23 = v30 * v1;
                        }
                        v31 = ptr->field_1ac;
                        v32 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v23, v31)) >> 5 & 3 | (unsigned long long)(CmpF(v23, v31) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v23, v31)) >> 5 & 3 | (unsigned long long)(CmpF(v23, v31) & 1)) & ((unsigned long long)(char)(CmpF(v23, v31)) >> 5 & 3 | (unsigned long long)(CmpF(v23, v31) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                        if (!((char)v32) && !ptr->field_255)
                        {
                            addr = ptr->field_238;
                            if (!addr)
                                break;
                            v33 = ptr->field_2f0;
                            v15 = Collider__get_bounds(addr, 0);
                            v35 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v33, v2 - v3 + v0)) >> 5 & 3 | (unsigned long long)(CmpF(v33, v2 - v3 + v0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v33, v2 - v3 + v0)) >> 5 & 3 | (unsigned long long)(CmpF(v33, v2 - v3 + v0) & 1)) & ((unsigned long long)(char)(CmpF(v33, v2 - v3 + v0)) >> 5 & 3 | (unsigned long long)(CmpF(v33, v2 - v3 + v0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                            if (!((char)v35))
                            {
                                v36 = 1;
                                goto LABEL_10a5fac;
                            }
                        }
                        v36 = 0;
LABEL_10a5fac:
                        ptr->field_22a = v36;
                        goto LABEL_10a5fb0;
                    }
                    else
                    {
LABEL_10a5fb0:
                        v8 = (int)p[24];
                        v11 += 1;
                        cur += 48;
                        if (v11 >= (int)p[24])
                            return v15;
                    }
                }
            }
        }
    }
    sub_f7db74(addr);
}
```

## `FPSRigidBodyWalker.ctor` — RVA `0xca5ff4`

- Decompiled symbol: `FPSRigidBodyWalker_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `884` bytes
- Result: `pseudocode`
- Heuristic layout hint: `FPSRigidBodyWalker_Recovered` matched 42 offsets against `FPSRigidBodyWalker` metadata (confidence 0.93).

```c
typedef struct FPSRigidBodyWalker_Recovered {
    char padding_0[208];
    unsigned long long InputLerpSpeed;
    unsigned int sprintSpeed;
    char padding_dc[4];
    unsigned long long jumpSpeed;
    unsigned int moveSpeedMult;
    char padding_ec[4];
    uint128_t diagonalStrafeAmt;
    uint128_t proneSpeedPercentage;
    unsigned int speedAmtX;
    char padding_114[4];
    unsigned long long zoomSpeedPercentage;
    char padding_120[4];
    char allowSprinting;
    char padding_125[3];
    unsigned long long sprintMode;
    unsigned short limitedSprint;
    char padding_132[2];
    unsigned int sprintRegenTime;
    char padding_138[4];
    unsigned int staminaForSprint;
    char padding_140[4];
    char catchBreathSound;
    char padding_145[1];
    char forwardSprintOnly;
    char padding_147[9];
    uint128_t leanDistance;
    char padding_160[53];
    unsigned short lowerGunForClimb;
    char lowerGunForHold;
    char padding_198[10];
    char jumpingAnims;
    char padding_1a3[1];
    unsigned long long holdBreathDuration;
    unsigned int slopeLimit;
    uint128_t maxStepHeight;
    char padding_1c0[96];
    char lowerMoveFriction;
    char padding_221[3];
    unsigned int verticalSpeedLimit;
    char padding_228[4];
    unsigned long long velocity;
    unsigned int field_234;
    char padding_238[33];
    char canWaterJump;
    char padding_25a[42];
    unsigned long long fallDamageThreshold;
    char padding_28c[12];
    unsigned long long verticalSpeedAmt;
    char padding_2a0[8];
    unsigned short jumpfxstate;
    char padding_2aa[6];
    char canRun;
    char padding_2b1[7];
    unsigned int sprintStart;
    char padding_2bc[12];
    char sprintStopState;
    char padding_2c9[3];
    unsigned int midPos;
    char padding_2d0[8];
    unsigned int crouchDelay;
    char padding_2dc[8];
    unsigned int proneDelay;
    char padding_2e8[196];
    unsigned int eyeHeight;
    char padding_3b0[12];
    uint128_t standingCamHeight;
    uint128_t crouchingCapsuleHeight;
    char padding_3dc[4];
    unsigned int capsuleCheckRadius;
    char padding_3e4[12];
    unsigned int maxVelocityChange;
    unsigned long long moveDirection;
    unsigned int field_3fc;
    unsigned long long velocityChange;
    unsigned int field_408;
} FPSRigidBodyWalker_Recovered;

typedef struct struct_1 {
    unsigned long long field_0;
    unsigned int field_8;
} struct_1;

typedef struct struct_2 {
    char padding_0[184];
    struct struct_1 *field_b8;
} struct_2;

extern char g_1010101;
extern struct_2 *g_1ef22e8;
extern char g_1fab2c9;

void FPSRigidBodyWalker_ctor(struct_0 *ptr)
{
    unsigned long long v7;  // x30
    unsigned long long v8;  // x24
    unsigned int v17;  // s1
    unsigned int v18;  // s1
    unsigned long long v9;  // x23
    unsigned long long v10;  // x22
    unsigned long long v11;  // x21
    unsigned long long v12;  // x20
    unsigned long long v13;  // x19
    struct_0 *addr;  // x22
    struct_0 *p;  // x23
    unsigned int v16;  // s1
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
    ptr->field_e0 = 0x4080000040800000;
    ptr->field_e8 = 0x3f800000;
    ptr->field_110 = 0x3f800000;
    ptr->field_d0 = 0x4080000041400000;
    ptr->field_134 = 0x40400000;
    ptr->field_f0 = 84405977751855187806863737912212915329;
    ptr->field_100 = 84405977751932559059347897215286142566;
    addr = &ptr->padding_147[2];
    ptr->field_128 = 4525216906440867842;
    ptr->field_13c = 0x40a00000;
    ptr->field_118 = 4575657222467066266;
    ptr->field_d8 = 0x41100000;
    ptr->field_124 = 1;
    ptr->field_130 = 257;
    ptr->field_144 = 1;
    ptr->field_146 = 1;
    *((char **)&addr->padding_0[0]) = &g_1010101;
    ptr->field_150 = 0x3f8000003f8000003f8000003f400000;
    *((unsigned short *)&(&ptr->padding_160)[1]) = 257;
    *((char *)&ptr->field_195 + 1) = 1;
    ptr->padding_198[9] = 1;
    *((unsigned long long *)&ptr->padding_1a3) = 0x40e0000041700000;
    *((unsigned int *)((char *)&ptr->field_1a4 + 4)) = 40;
    *((uint128_t *)&ptr->field_1ac) = 258534845199292310894919488485316152525;
    ptr->padding_1c0[80] = 1;
    *((unsigned int *)&ptr->padding_1c0[84]) = 0x41100000;
    p = &ptr->padding_25a[22];
    if (!g_1fab2c9)
    {
        sub_f7d92c(&g_1ef22e8);
        g_1fab2c9 = 1;
    }
    v16 = g_1ef22e8->field_b8->field_8;
    *((unsigned long long *)((char *)&addr->field_e0 + 3)) = g_1ef22e8->field_b8->field_0;
    ptr->field_224 = v16;
    ptr->padding_238[13] = 1;
    *((unsigned long long *)&p->padding_0[0]) = 0x4000000040b00000;
    ptr->field_284 = 0x3eb3333340800000;
    *((unsigned int *)&ptr->padding_2a0[0]) = 0xc0000000;
    *((unsigned int *)&ptr->padding_2b1[3]) = 1063675494;
    *((unsigned int *)&ptr->padding_2bc[4]) = 1058139013;
    ptr->field_2cc = 1061997773;
    *((unsigned int *)&ptr->padding_2e8[172]) = 3201092813;
    *((unsigned short *)&ptr->padding_28c[8]) = 257;
    *((char *)&ptr->field_298) = 1;
    ptr->field_2b0 = 1;
    *((uint128_t *)&p->padding_138) = 85070591789129613243067389915340986122;
    *((uint128_t *)&p->padding_147[1]) = 0x402666663ecccccd3f4000003fa00000;
    *((unsigned int *)&ptr->field_3bc) = 0x3f000000;
    *((unsigned int *)&ptr->field_3cc) = 5;
    v17 = g_1ef22e8->field_b8->field_8;
    *((unsigned long long *)&p->padding_160[16]) = g_1ef22e8->field_b8->field_0;
    *((unsigned int *)((char *)&ptr->field_3cc + 12)) = v17;
    v18 = g_1ef22e8->field_b8->field_8;
    *((unsigned long long *)&ptr->padding_3dc) = g_1ef22e8->field_b8->field_0;
    *((unsigned int *)&ptr->padding_3e4[0]) = v18;
}
```
