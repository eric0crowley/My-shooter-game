# Native pseudocode: LookAt

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `LookAt.Start` — RVA `0xc6e760`

- Decompiled symbol: `LookAt_Start`
- Metadata signature: `private void Start() { }`
- Native interval: `308` bytes
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

extern struct_0 *g_1eef458;
extern struct_1 *g_1ef0c58;
extern long long g_1f0c670;
extern char g_1fab352;

unsigned long long LookAt_Start(void* ptr)
{
    long long v0;  // x0
    unsigned long long v1;  // x0
    unsigned int v2;  // s0
    unsigned int v3;  // s1
    unsigned int v4;  // s2
    unsigned int v5;  // w9
    unsigned long long v6;  // x0

    if (!(g_1fab352 & 1))
    {
        sub_f7d92c(&g_1eef458);
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c(&g_1f0c670);
        g_1fab352 = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (((char)Object__op_Implicit((long long)ptr[32], 0) & 1))
    {
        v0 = (long long)ptr[32];
        if (v0)
        {
            Transform__get_position(v0, 0);
            v0 = Component__get_transform(ptr, 0);
            if (v0)
            {
                v1 = Transform__get_forward();
                *((unsigned int *)&ptr[40]) = v2 * 2;
                *((unsigned int *)&ptr[44]) = v3 * 2;
                *((unsigned int *)&ptr[48]) = v4 * 2;
                v5 = (int)ptr[48];
                *((long long *)&ptr[64]) = (long long)ptr[40];
                *((unsigned int *)&ptr[72]) = v5;
                return v1;
            }
        }
        sub_f7db74(v0);
    }
    else
    {
        if (!g_1eef458->field_e0)
            sub_f7da5c(g_1eef458);
        Debug__LogError(g_1f0c670, 0);
        v6 = Behaviour__set_enabled();
        return Behaviour__set_enabled();
    }
}
```


## `LookAt.OnAnimatorIK` — RVA `0xc6e894`

- Decompiled symbol: `LookAt_OnAnimatorIK`
- Metadata signature: `private void OnAnimatorIK() { }`
- Native interval: `404` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: Decompiler produced no C-like text

```c
// 0x106e894: str d14, [sp, #-0x50]!
// 0x106e898: stp d13, d12, [sp, #0x10]
// 0x106e89c: stp d11, d10, [sp, #0x20]
// 0x106e8a0: stp d9, d8, [sp, #0x30]
// 0x106e8a4: stp x30, x19, [sp, #0x40]
// 0x106e8a8: mov x19, x0
// 0x106e8ac: ldr x0, [x0, #0x20]
// 0x106e8b0: cbz x0, #0x106ea24
// 0x106e8b4: mov x1, xzr
// 0x106e8b8: bl #0x1b9d508
// 0x106e8bc: ldrb w8, [x19, #0x3c]
// 0x106e8c0: ldr x0, [x19, #0x20]
// 0x106e8c4: str s1, [x19, #0x2c]
// 0x106e8c8: fmov s0, #1.00000000
// 0x106e8cc: cmp w8, #0
// 0x106e8d0: fmov s1, wzr
// 0x106e8d4: fcsel s14, s1, s0, eq
// 0x106e8d8: cbz x0, #0x106ea24
// 0x106e8dc: ldp s9, s8, [x19, #0x44]
// 0x106e8e0: ldr s10, [x19, #0x40]
// 0x106e8e4: mov x1, xzr
// 0x106e8e8: bl #0x1b9d508
// 0x106e8ec: ldr x0, [x19, #0x20]
// 0x106e8f0: cbz x0, #0x106ea24
// 0x106e8f4: ldp s12, s13, [x19, #0x2c]
// 0x106e8f8: ldr s11, [x19, #0x28]
// 0x106e8fc: mov x1, xzr
// 0x106e900: fsub s8, s8, s2
// 0x106e904: fsub s9, s9, s1
// 0x106e908: fsub s10, s10, s0
// 0x106e90c: bl #0x1b9d508
// 0x106e910: mov x0, xzr
// 0x106e914: fsub s11, s11, s0
// 0x106e918: fsub s12, s12, s1
// 0x106e91c: fsub s13, s13, s2
// 0x106e920: bl #0x1b89b60
// 0x106e924: adrp x8, #0x832000
// 0x106e928: ldr s1, [x8, #0x4c0]
// 0x106e92c: mov w8, #0x7f800000
// 0x106e930: fmov s7, w8
// 0x106e934: mov v2.16b, v8.16b
// 0x106e938: fmul s6, s0, s1
// 0x106e93c: mov v0.16b, v10.16b
// 0x106e940: mov v1.16b, v9.16b
// 0x106e944: mov v3.16b, v11.16b
// 0x106e948: mov v4.16b, v12.16b
// 0x106e94c: mov v5.16b, v13.16b
// 0x106e950: mov x0, xzr
// 0x106e954: bl #0x1b89854
// 0x106e958: ldr x0, [x19, #0x20]
// 0x106e95c: cbz x0, #0x106ea24
// 0x106e960: mov x1, xzr
// 0x106e964: mov v8.16b, v0.16b
// 0x106e968: mov v9.16b, v1.16b
// 0x106e96c: mov v10.16b, v2.16b
// 0x106e970: bl #0x1b9d508
// 0x106e974: fadd s0, s8, s0
// 0x106e978: ldr s8, [x19, #0x58]
// 0x106e97c: fadd s1, s9, s1
// 0x106e980: fadd s2, s10, s2
// 0x106e984: mov w8, #0x34
// 0x106e988: fcmp s14, s8
// 0x106e98c: mov w9, #0x38
// 0x106e990: stp s0, s1, [x19, #0x40]
// 0x106e994: str s2, [x19, #0x48]
// 0x106e998: csel x8, x9, x8, gt
// 0x106e99c: ldr s9, [x19, x8]
// 0x106e9a0: mov x0, xzr
// 0x106e9a4: bl #0x1b89b60
// 0x106e9a8: fdiv s0, s0, s9
// 0x106e9ac: fsub s1, s14, s8
// 0x106e9b0: ldr x0, [x19, #0x50]
// 0x106e9b4: fneg s3, s0
// 0x106e9b8: fcmp s1, #0.0
// 0x106e9bc: fabd s2, s14, s8
// 0x106e9c0: fcsel s1, s0, s3, ge
// 0x106e9c4: fadd s1, s8, s1
// 0x106e9c8: fcmp s2, s0
// 0x106e9cc: fcsel s0, s1, s14, hi
// 0x106e9d0: str s0, [x19, #0x58]
// 0x106e9d4: cbz x0, #0x106ea24
// 0x106e9d8: adrp x8, #0x832000
// 0x106e9dc: adrp x9, #0x832000
// 0x106e9e0: ldr s1, [x8, #0x4f4]
// 0x106e9e4: ldr s3, [x9, #0x3e8]
// 0x106e9e8: fmov s2, #0.50000000
// 0x106e9ec: fmov s4, #0.50000000
// 0x106e9f0: mov x1, xzr
// 0x106e9f4: bl #0x1b67c08
// 0x106e9f8: ldr x0, [x19, #0x50]
// 0x106e9fc: cbz x0, #0x106ea24
// 0x106ea00: ldp s1, s2, [x19, #0x44]
// 0x106ea04: ldr s0, [x19, #0x40]
// 0x106ea08: ldp x30, x19, [sp, #0x40]
// 0x106ea0c: ldp d9, d8, [sp, #0x30]
// 0x106ea10: ldp d11, d10, [sp, #0x20]
// 0x106ea14: ldp d13, d12, [sp, #0x10]
// 0x106ea18: mov x1, xzr
// 0x106ea1c: ldr d14, [sp], #0x50
// 0x106ea20: b #0x1b67a60
// 0x106ea24: bl #0xf7db74
```


## `LookAt.ctor` — RVA `0xc6ea28`

- Decompiled symbol: `LookAt_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `32` bytes
- Result: `pseudocode`
- Heuristic layout hint: `LookAt_Recovered` matched 2 offsets against `LookAt` metadata (confidence 1.00).

```c
typedef struct LookAt_Recovered {
    char padding_0[52];
    unsigned long long lookAtCoolTime;
    char looking;
} LookAt_Recovered;

long long LookAt_ctor(struct_0 *ptr)
{
    *((unsigned long long *)&(&ptr->padding_0)[1]) = 4489188110467124429;
    *((char *)&ptr->field_34 + 4) = 1;
}
```
