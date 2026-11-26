# Native pseudocode: bl_MMCompass

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `bl_MMCompass.Start` — RVA `0xcc9eb0`

- Decompiled symbol: `bl_MMCompass_Start`
- Metadata signature: `private void Start() { }`
- Native interval: `244` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[32];
    char field_20;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern long long g_1efd0f0;
extern char g_1fab56e;

long long bl_MMCompass_Start(struct_1 *ptr)
{
    long long v0;  // x0
    long long v1;  // x0
    long long v2;  // x0
    unsigned long v3;  // x0
    long long v4;  // x0

    if (!(g_1fab56e & 1))
    {
        sub_f7d92c(&g_1efd0f0);
        sub_f7d92c(&g_1ef0c58);
        g_1fab56e = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v0 = Object__op_Equality(*((long long *)&ptr->field_20), 0, 0);
    if (!((char)v0 & 1))
        return v0;
    v1 = sub_1231bc8(ptr, g_1efd0f0);
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v2 = Object__op_Inequality(v1, 0, 0);
    if (!((char)v2 & 1))
        return v2;
    v3 = sub_1231bc8(ptr, g_1efd0f0);
    if (v3)
    {
        *((unsigned long long *)&ptr->field_20) = (unsigned long long)bl_MiniMap__get_Target(v3);
        v4 = sub_f7d8d0();
        return sub_f7d8d0();
    }
    sub_f7db74();
}
```

## `bl_MMCompass.Update` — RVA `0xcc9fa4`

- Decompiled symbol: `bl_MMCompass_Update`
- Metadata signature: `private void Update() { }`
- Native interval: `636` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: Decompiler produced no C-like text

```c
// 0x10c9fa4: str d8, [sp, #-0x30]!
// 0x10c9fa8: stp x30, x21, [sp, #0x10]
// 0x10c9fac: stp x20, x19, [sp, #0x20]
// 0x10c9fb0: adrp x21, #0x1fab000
// 0x10c9fb4: adrp x20, #0x1e8c000
// 0x10c9fb8: ldrb w8, [x21, #0x56f]
// 0x10c9fbc: ldr x20, [x20, #0xd8]
// 0x10c9fc0: mov x19, x0
// 0x10c9fc4: tbnz w8, #0, #0x10c9fdc
// 0x10c9fc8: adrp x0, #0x1e8c000
// 0x10c9fcc: ldr x0, [x0, #0xd8]
// 0x10c9fd0: bl #0xf7d92c
// 0x10c9fd4: mov w8, #1
// 0x10c9fd8: strb w8, [x21, #0x56f]
// 0x10c9fdc: ldr x0, [x20]
// 0x10c9fe0: ldr x20, [x19, #0x20]
// 0x10c9fe4: ldr w8, [x0, #0xe0]
// 0x10c9fe8: cbnz w8, #0x10c9ff0
// 0x10c9fec: bl #0xf7da5c
// 0x10c9ff0: mov x0, x20
// 0x10c9ff4: mov x1, xzr
// 0x10c9ff8: mov x2, xzr
// 0x10c9ffc: bl #0x1b94ac8
// 0x10ca000: tbz w0, #0, #0x10ca010
// 0x10ca004: ldr x0, [x19, #0x20]
// 0x10ca008: cbnz x0, #0x10ca01c
// 0x10ca00c: b #0x10ca21c
// 0x10ca010: mov x0, x19
// 0x10ca014: bl #0x10ca220
// 0x10ca018: cbz x0, #0x10ca21c
// 0x10ca01c: mov x1, xzr
// 0x10ca020: bl #0x1b9d6c8
// 0x10ca024: mov w8, #0x7f800000
// 0x10ca028: fabs s0, s1
// 0x10ca02c: fmov s1, w8
// 0x10ca030: fcvtzs w9, s0
// 0x10ca034: fcmp s0, s1
// 0x10ca038: mov w8, #-0x80000000
// 0x10ca03c: csel w8, w8, w9, eq
// 0x10ca040: cmp w8, #0x169
// 0x10ca044: str w8, [x19, #0x54]
// 0x10ca048: b.lt #0x10ca06c
// 0x10ca04c: mov w10, #0x6c17
// 0x10ca050: lsr w9, w8, #3
// 0x10ca054: movk w10, #0x16c1, lsl #16
// 0x10ca058: umull x9, w9, w10
// 0x10ca05c: lsr x9, x9, #0x22
// 0x10ca060: mov w10, #0x168
// 0x10ca064: msub w8, w9, w10, w8
// 0x10ca068: str w8, [x19, #0x54]
// 0x10ca06c: ldr x0, [x19, #0x28]
// 0x10ca070: sub w9, w8, #0x168
// 0x10ca074: cmp w8, #0xb5
// 0x10ca078: csel w8, w8, w9, lt
// 0x10ca07c: str w8, [x19, #0x50]
// 0x10ca080: cbz x0, #0x10ca21c
// 0x10ca084: ldr x20, [x19, #0x30]
// 0x10ca088: mov x1, xzr
// 0x10ca08c: bl #0x1b9c8ac
// 0x10ca090: ldr x0, [x19, #0x28]
// 0x10ca094: cbz x0, #0x10ca21c
// 0x10ca098: ldr w21, [x19, #0x50]
// 0x10ca09c: mov x1, xzr
// 0x10ca0a0: mov v8.16b, v0.16b
// 0x10ca0a4: bl #0x1b9c8ac
// 0x10ca0a8: cbz x20, #0x10ca21c
// 0x10ca0ac: fmov s1, #0.50000000
// 0x10ca0b0: lsl w8, w21, #1
// 0x10ca0b4: fmul s2, s8, s1
// 0x10ca0b8: scvtf s3, w8
// 0x10ca0bc: fsub s2, s2, s3
// 0x10ca0c0: fmul s0, s0, s1
// 0x10ca0c4: fsub s0, s2, s0
// 0x10ca0c8: fmov s1, wzr
// 0x10ca0cc: mov x0, x20
// 0x10ca0d0: mov x1, xzr
// 0x10ca0d4: bl #0x1b9c820
// 0x10ca0d8: ldr x0, [x19, #0x28]
// 0x10ca0dc: cbz x0, #0x10ca21c
// 0x10ca0e0: ldr x20, [x19, #0x38]
// 0x10ca0e4: mov x1, xzr
// 0x10ca0e8: bl #0x1b9c8ac
// 0x10ca0ec: ldr x0, [x19, #0x28]
// 0x10ca0f0: cbz x0, #0x10ca21c
// 0x10ca0f4: ldr w21, [x19, #0x54]
// 0x10ca0f8: mov x1, xzr
// 0x10ca0fc: mov v8.16b, v0.16b
// 0x10ca100: bl #0x1b9c8ac
// 0x10ca104: cbz x20, #0x10ca21c
// 0x10ca108: fmov s1, #0.50000000
// 0x10ca10c: lsl w8, w21, #1
// 0x10ca110: mov w9, #0x43b40000
// 0x10ca114: fmul s2, s8, s1
// 0x10ca118: scvtf s3, w8
// 0x10ca11c: fmov s4, w9
// 0x10ca120: fsub s2, s2, s3
// 0x10ca124: fadd s2, s2, s4
// 0x10ca128: fmul s0, s0, s1
// 0x10ca12c: fsub s0, s2, s0
// 0x10ca130: fmov s1, wzr
// 0x10ca134: mov x0, x20
// 0x10ca138: mov x1, xzr
// 0x10ca13c: bl #0x1b9c820
// 0x10ca140: ldr x0, [x19, #0x28]
// 0x10ca144: cbz x0, #0x10ca21c
// 0x10ca148: ldr x20, [x19, #0x40]
// 0x10ca14c: mov x1, xzr
// 0x10ca150: bl #0x1b9c8ac
// 0x10ca154: ldr x0, [x19, #0x28]
// 0x10ca158: cbz x0, #0x10ca21c
// 0x10ca15c: ldr w21, [x19, #0x50]
// 0x10ca160: mov x1, xzr
// 0x10ca164: mov v8.16b, v0.16b
// 0x10ca168: bl #0x1b9c8ac
// 0x10ca16c: cbz x20, #0x10ca21c
// 0x10ca170: fmov s1, #0.50000000
// 0x10ca174: lsl w8, w21, #1
// 0x10ca178: mov w9, #0x43340000
// 0x10ca17c: fmul s2, s8, s1
// 0x10ca180: scvtf s3, w8
// 0x10ca184: fmov s4, w9
// 0x10ca188: fsub s2, s2, s3
// 0x10ca18c: fadd s2, s2, s4
// 0x10ca190: fmul s0, s0, s1
// 0x10ca194: fsub s0, s2, s0
// 0x10ca198: fmov s1, wzr
// 0x10ca19c: mov x0, x20
// 0x10ca1a0: mov x1, xzr
// 0x10ca1a4: bl #0x1b9c820
// 0x10ca1a8: ldr x0, [x19, #0x28]
// 0x10ca1ac: cbz x0, #0x10ca21c
// 0x10ca1b0: ldr x20, [x19, #0x48]
// 0x10ca1b4: mov x1, xzr
// 0x10ca1b8: bl #0x1b9c8ac
// 0x10ca1bc: ldr x0, [x19, #0x28]
// 0x10ca1c0: cbz x0, #0x10ca21c
// 0x10ca1c4: ldr w19, [x19, #0x54]
// 0x10ca1c8: mov x1, xzr
// 0x10ca1cc: mov v8.16b, v0.16b
// 0x10ca1d0: bl #0x1b9c8ac
// 0x10ca1d4: cbz x20, #0x10ca21c
// 0x10ca1d8: fmov s1, #0.50000000
// 0x10ca1dc: lsl w8, w19, #1
// 0x10ca1e0: mov w9, #0x44070000
// 0x10ca1e4: fmul s2, s8, s1
// 0x10ca1e8: scvtf s3, w8
// 0x10ca1ec: mov x0, x20
// 0x10ca1f0: ldp x20, x19, [sp, #0x20]
// 0x10ca1f4: ldp x30, x21, [sp, #0x10]
// 0x10ca1f8: fmov s4, w9
// 0x10ca1fc: fmul s0, s0, s1
// 0x10ca200: fsub s1, s2, s3
// 0x10ca204: fadd s1, s1, s4
// 0x10ca208: fsub s0, s1, s0
// 0x10ca20c: fmov s1, wzr
// 0x10ca210: mov x1, xzr
// 0x10ca214: ldr d8, [sp], #0x30
// 0x10ca218: b #0x1b9c820
// 0x10ca21c: bl #0xf7db74
```

## `bl_MMCompass.get_m_Transform` — RVA `0xcca220`

- Decompiled symbol: `bl_MMCompass_get_m_Transform`
- Metadata signature: `private Transform get_m_Transform() { }`
- Native interval: `168` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[88];
    long long field_58;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern long long g_1efd0c8;
extern char g_1fab570;

long long bl_MMCompass_get_m_Transform(struct_1 *ptr)
{
    long long v0;  // x0

    if (!(g_1fab570 & 1))
    {
        sub_f7d92c(&g_1efd0c8);
        sub_f7d92c(&g_1ef0c58);
        g_1fab570 = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (((char)Object__op_Equality(ptr->field_58, 0, 0) & 1))
    {
        v0 = sub_1231bc8(ptr, g_1efd0c8);
        ptr->field_58 = v0;
        sub_f7d8d0((struct struct_1 *)&ptr->field_58, v0);
    }
    return ptr->field_58;
}
```

## `bl_MMCompass.ctor` — RVA `0xcca2c8`

- Decompiled symbol: `bl_MMCompass_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long bl_MMCompass_ctor(void)
{
    long long v0;  // x0

    v0 = MonoBehaviour__ctor();
    return MonoBehaviour__ctor();
}
```
