# Native pseudocode: MainMenu

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `MainMenu.Start` — RVA `0xc9195c`

- Decompiled symbol: `MainMenu_Start`
- Metadata signature: `private void Start() { }`
- Native interval: `664` bytes
- Result: `pseudocode`
- Heuristic layout hint: `MainMenu_Recovered` matched 5 offsets against `MainMenu` metadata (confidence 1.00).

```c
typedef struct struct_1 {
    char padding_0[40];
    long long field_28;
} struct_1;

typedef struct struct_2 {
    char padding_0[588];
    char field_24c;
} struct_2;

typedef struct MainMenu_Recovered {
    char padding_0[32];
    struct struct_3 *FPSPlayerComponent;
    char padding_28[8];
    void* NpcGroups;
    char padding_38[128];
    long long aSource;
    char padding_c0[120];
    char npcGoupsNull;
    char padding_139[15];
    char hungerThirstActive;
} MainMenu_Recovered;

typedef struct struct_3 {
    char padding_0[588];
    char field_24c;
} struct_3;

typedef struct struct_5 {
    char padding_0[32];
    long long field_20;
} struct_5;

typedef struct struct_6 {
    char padding_0[32];
    long long field_20;
} struct_6;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern long long g_1efcf38;
extern long long g_1efea78;
extern long long g_1efebb8;
extern long long g_1f0a668;
extern char g_1fab455;

void MainMenu_Start(struct_4 *ptr)
{
    unsigned long long v4;  // x30
    unsigned long long v5;  // x21
    struct_4 *v14;  // x21
    unsigned long v15;  // x0
    void* v16;  // x8
    void* v17;  // x8
    void* v18;  // x8
    void* p;  // x20
    unsigned int v20;  // w8
    unsigned int v21;  // w21
    struct_5 *v22;  // x8
    void* v23;  // x20
    unsigned long long v6;  // x20
    struct_6 *v24;  // x8
    unsigned long long v7;  // x19
    struct_1 *v8;  // x0
    struct_2 *v9;  // x0
    struct_4 *addr;  // x20
    struct_4 *v11;  // x20
    long long v12;  // x0
    struct_4 *ptr3;  // x21
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x18]
    unsigned long long v2;  // [bp-0x10]
    unsigned long long v3;  // [bp-0x8]

    v0 = v4;
    v1 = v5;
    v2 = v6;
    v3 = v7;
    if (!(g_1fab455 & 1))
    {
        sub_f7d92c(&g_1efcf38);
        sub_f7d92c(&g_1efea78);
        sub_f7d92c(&g_1efebb8);
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c(&g_1f0a668);
        g_1fab455 = 1;
    }
    if (Camera__get_main(0) && !((v8 = (struct_1 *)sub_1231bc8(), !v8 || !v8->field_28)))
    {
        v9 = sub_1249224(v8->field_28, g_1efebb8);
        addr = ptr;
        addr->field_20 = v9;
        v11 = &addr->field_20;
        sub_f7d8d0(v11, v9);
        if (Component__get_gameObject(ptr, 0))
        {
            v12 = sub_124913c();
            ptr3 = ptr;
            ptr3->field_b8 = v12;
            v14 = &ptr3->field_b8;
            sub_f7d8d0(v14, v12);
            if (*((long long *)&v14->padding_0[0]) && !((AudioSource__set_spatialBlend(*((long long *)&v14->padding_0[0]), 0), !*((long long *)&v14->padding_0[0]) || (AudioSource__set_volume(*((long long *)&v14->padding_0[0]), 0), !*((long long *)&v14->padding_0[0]) || (v15 = (unsigned long)(unsigned long long)AudioSource__set_playOnAwake(*((long long *)&v14->padding_0[0]), 0, 0), !*((long long *)&v11->padding_0[0]) || (v16 = ptr->field_30, ptr->field_148 = *((char *)(*((long long *)&v11->padding_0[0]) + 588)), !v16))))))
            {
                if (!(long long)v16[24])
                {
LABEL_1091bcc:
                    ptr->field_138 = 1;
LABEL_1091bd4:
                    Behaviour__set_enabled();
                    return;
                }
                if (!(int)(long long)v16[24])
                    goto LABEL_1091bf0;
                if (!g_1ef0c58->field_e0)
                    sub_f7da5c(g_1ef0c58);
                v15 = Object__op_Inequality((long long)v16[32], 0, 0);
                if (!(v15 & 1))
                    goto LABEL_1091bcc;
                v17 = ptr->field_30;
                if (v17)
                {
                    if ((int)v17[24] <= 1)
                        goto LABEL_1091bf0;
                    if (!g_1ef0c58->field_e0)
                        sub_f7da5c(g_1ef0c58);
                    v15 = Object__op_Inequality((long long)v17[40], 0, 0);
                    if (!(v15 & 1))
                        goto LABEL_1091bcc;
                    v18 = ptr->field_30;
                    if (v18)
                    {
                        if ((int)v18[24] <= 2)
                            goto LABEL_1091bf0;
                        if (!g_1ef0c58->field_e0)
                            sub_f7da5c(g_1ef0c58);
                        v15 = Object__op_Inequality((long long)v18[48], 0, 0);
                        if (!(v15 & 1))
                            goto LABEL_1091bcc;
                        p = ptr->field_30;
                        if (p)
                        {
                            v20 = (int)p[24];
                            if ((int)p[24] >= 1)
                            {
                                v21 = 0;
                                while (true)
                                {
                                    if (v20 <= v21)
                                        goto LABEL_1091bf0;
                                    v22 = p + v21 * 8;
                                    if (!v22->field_20)
                                        break;
                                    v15 = GameObject__SetActive(v22->field_20, 0, 0);
                                    v20 = (int)p[24];
                                    v21 += 1;
                                    if (v21 >= v20)
                                        goto LABEL_1091b88;
                                }
                            }
                            else
                            {
LABEL_1091b88:
                                v23 = ptr->field_30;
                                v15 = PlayerPrefs__GetInt(g_1f0a668, 0);
                                if (v23)
                                {
                                    if ((int)v23[24] <= (unsigned int)v15)
                                        goto LABEL_1091bf0;
                                    v24 = v23 + (v15 & 4294967295) * 8;
                                    if (v24->field_20)
                                    {
                                        GameObject__SetActive(v24->field_20, 1, 0);
                                        goto LABEL_1091bd4;
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    v15 = sub_f7db74();
LABEL_1091bf0:
    sub_f7db7c(v15);
}
```

## `MainMenu.Update` — RVA `0xc91bf4`

- Decompiled symbol: `MainMenu_Update`
- Metadata signature: `private void Update() { }`
- Native interval: `88` bytes
- Result: `pseudocode`
- Heuristic layout hint: `MainMenu_Recovered` matched 2 offsets against `MainMenu` metadata (confidence 1.00).

```c
typedef struct MainMenu_Recovered {
    char padding_0[32];
    struct struct_1 *FPSPlayerComponent;
    char padding_28[137];
    char resumePress;
} MainMenu_Recovered;

typedef struct struct_1 {
    char padding_0[1128];
    char field_468;
    char padding_469[11];
    char field_474;
} struct_1;

void MainMenu_Update(struct_0 *ptr)
{
    char p[1141];  // x8

    if (!ptr->field_b1)
        return;
    if (ptr->field_20)
    {
        Time__set_timeScale(0);
        p = ptr->field_20;
        ptr->field_b1 = 0;
        if (p)
        {
            p[1140] = 0;
            p[1128] = 0;
            Behaviour__set_enabled();
            return;
        }
    }
    sub_f7db74();
}
```

## `MainMenu.OnGUI` — RVA `0xc91c4c`

- Decompiled symbol: `MainMenu_OnGUI`
- Metadata signature: `private void OnGUI() { }`
- Native interval: `2544` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: Decompiler produced no C-like text

```c
// 0x1091c4c: stp d11, d10, [sp, #-0x70]!
// 0x1091c50: stp d9, d8, [sp, #0x10]
// 0x1091c54: str x30, [sp, #0x20]
// 0x1091c58: stp x26, x25, [sp, #0x30]
// 0x1091c5c: stp x24, x23, [sp, #0x40]
// 0x1091c60: stp x22, x21, [sp, #0x50]
// 0x1091c64: stp x20, x19, [sp, #0x60]
// 0x1091c68: adrp x20, #0x1fab000
// 0x1091c6c: adrp x25, #0x1e8c000
// 0x1091c70: ldrb w8, [x20, #0x456]
// 0x1091c74: ldr x25, [x25, #0xce0]
// 0x1091c78: mov x19, x0
// 0x1091c7c: tbnz w8, #0, #0x1091ca0
// 0x1091c80: adrp x0, #0x1e8d000
// 0x1091c84: ldr x0, [x0, #0x2a8]
// 0x1091c88: bl #0xf7d92c
// 0x1091c8c: adrp x0, #0x1e8c000
// 0x1091c90: ldr x0, [x0, #0xce0]
// 0x1091c94: bl #0xf7d92c
// 0x1091c98: mov w8, #1
// 0x1091c9c: strb w8, [x20, #0x456]
// 0x1091ca0: ldr x0, [x25]
// 0x1091ca4: ldp s11, s10, [x19, #0x40]
// 0x1091ca8: ldp s9, s8, [x19, #0x48]
// 0x1091cac: ldr w8, [x0, #0xe0]
// 0x1091cb0: cbnz w8, #0x1091cb8
// 0x1091cb4: bl #0xf7da5c
// 0x1091cb8: mov v0.16b, v11.16b
// 0x1091cbc: mov v1.16b, v10.16b
// 0x1091cc0: mov v2.16b, v9.16b
// 0x1091cc4: mov v3.16b, v8.16b
// 0x1091cc8: mov x0, xzr
// 0x1091ccc: bl #0x1bb2dbc
// 0x1091cd0: ldrb w8, [x19, #0x70]
// 0x1091cd4: cbnz w8, #0x1092274
// 0x1091cd8: ldr x0, [x25]
// 0x1091cdc: ldr w8, [x0, #0xe0]
// 0x1091ce0: cbnz w8, #0x1091ce8
// 0x1091ce4: bl #0xf7da5c
// 0x1091ce8: mov x0, xzr
// 0x1091cec: bl #0x1bb388c
// 0x1091cf0: cbz x0, #0x1092638
// 0x1091cf4: mov x1, xzr
// 0x1091cf8: bl #0x1bb5514
// 0x1091cfc: adrp x26, #0x1e8d000
// 0x1091d00: ldr x26, [x26, #0x2a8]
// 0x1091d04: mov x20, x0
// 0x1091d08: ldr x8, [x26]
// 0x1091d0c: mov x0, x8
// 0x1091d10: bl #0xf7db70
// 0x1091d14: mov x1, x20
// 0x1091d18: mov x2, xzr
// 0x1091d1c: mov x21, x0
// 0x1091d20: bl #0x1bbc4a8
// 0x1091d24: add x22, x19, #0x110
// 0x1091d28: mov x0, x22
// 0x1091d2c: mov x1, x21
// 0x1091d30: str x21, [x19, #0x110]
// 0x1091d34: bl #0xf7d8d0
// 0x1091d38: mov x0, xzr
// 0x1091d3c: bl #0x1bb388c
// 0x1091d40: cbz x0, #0x1092638
// 0x1091d44: mov x1, xzr
// 0x1091d48: bl #0x1bb5514
// 0x1091d4c: ldr x8, [x26]
// 0x1091d50: mov x20, x0
// 0x1091d54: mov x0, x8
// 0x1091d58: bl #0xf7db70
// 0x1091d5c: mov x1, x20
// 0x1091d60: mov x2, xzr
// 0x1091d64: mov x21, x0
// 0x1091d68: bl #0x1bbc4a8
// 0x1091d6c: add x20, x19, #0x118
// 0x1091d70: mov x0, x20
// 0x1091d74: mov x1, x21
// 0x1091d78: str x21, [x19, #0x118]
// 0x1091d7c: bl #0xf7d8d0
// 0x1091d80: mov x0, xzr
// 0x1091d84: bl #0x1bb388c
// 0x1091d88: cbz x0, #0x1092638
// 0x1091d8c: mov x1, xzr
// 0x1091d90: bl #0x1bb5514
// 0x1091d94: ldr x8, [x26]
// 0x1091d98: mov x21, x0
// 0x1091d9c: mov x0, x8
// 0x1091da0: bl #0xf7db70
// 0x1091da4: mov x1, x21
// 0x1091da8: mov x2, xzr
// 0x1091dac: mov x23, x0
// 0x1091db0: bl #0x1bbc4a8
// 0x1091db4: add x21, x19, #0x120
// 0x1091db8: mov x0, x21
// 0x1091dbc: mov x1, x23
// 0x1091dc0: str x23, [x19, #0x120]
// 0x1091dc4: bl #0xf7d8d0
// 0x1091dc8: mov x0, xzr
// 0x1091dcc: bl #0x1bb388c
// 0x1091dd0: cbz x0, #0x1092638
// 0x1091dd4: mov x1, xzr
// 0x1091dd8: bl #0x1bb5104
// 0x1091ddc: ldr x8, [x26]
// 0x1091de0: mov x23, x0
// 0x1091de4: mov x0, x8
// 0x1091de8: bl #0xf7db70
// 0x1091dec: mov x1, x23
// 0x1091df0: mov x2, xzr
// 0x1091df4: mov x24, x0
// 0x1091df8: bl #0x1bbc4a8
// 0x1091dfc: add x0, x19, #0x140
// 0x1091e00: mov x1, x24
// 0x1091e04: str x24, [x19, #0x140]
// 0x1091e08: bl #0xf7d8d0
// 0x1091e0c: mov x0, xzr
// 0x1091e10: bl #0x1bb388c
// 0x1091e14: cbz x0, #0x1092638
// 0x1091e18: mov x1, xzr
// 0x1091e1c: bl #0x1bb5514
// 0x1091e20: ldr x8, [x26]
// 0x1091e24: mov x23, x0
// 0x1091e28: mov x0, x8
// 0x1091e2c: bl #0xf7db70
// 0x1091e30: mov x1, x23
// 0x1091e34: mov x2, xzr
// 0x1091e38: mov x24, x0
// 0x1091e3c: bl #0x1bbc4a8
// 0x1091e40: add x0, x19, #0x128
// 0x1091e44: mov x1, x24
// 0x1091e48: str x24, [x19, #0x128]
// 0x1091e4c: bl #0xf7d8d0
// 0x1091e50: mov x0, xzr
// 0x1091e54: bl #0x1bb388c
// 0x1091e58: cbz x0, #0x1092638
// 0x1091e5c: mov x1, xzr
// 0x1091e60: bl #0x1bb5514
// 0x1091e64: ldr x8, [x26]
// 0x1091e68: mov x23, x0
// 0x1091e6c: mov x0, x8
// 0x1091e70: bl #0xf7db70
// 0x1091e74: mov x1, x23
// 0x1091e78: mov x2, xzr
// 0x1091e7c: mov x24, x0
// 0x1091e80: bl #0x1bbc4a8
// 0x1091e84: add x23, x19, #0x130
// 0x1091e88: mov x0, x23
// 0x1091e8c: mov x1, x24
// 0x1091e90: str x24, [x19, #0x130]
// 0x1091e94: bl #0xf7d8d0
// 0x1091e98: ldr x0, [x19, #0x130]
// 0x1091e9c: cbz x0, #0x1092638
// 0x1091ea0: ldrb w24, [x19, #0x138]
// 0x1091ea4: mov x1, xzr
// 0x1091ea8: bl #0x1bbb5a8
// 0x1091eac: cbz w24, #0x1091f1c
// 0x1091eb0: cbz x0, #0x1092638
// 0x1091eb4: fmov s0, #0.50000000
// 0x1091eb8: fmov s1, #0.50000000
// 0x1091ebc: fmov s2, #0.50000000
// 0x1091ec0: fmov s3, #1.00000000
// 0x1091ec4: mov x1, xzr
// 0x1091ec8: bl #0x1bbb61c
// 0x1091ecc: ldr x0, [x23]
// 0x1091ed0: cbz x0, #0x1092638
// 0x1091ed4: mov x1, xzr
// 0x1091ed8: bl #0x1bbc70c
// 0x1091edc: cbz x0, #0x1092638
// 0x1091ee0: fmov s0, #0.50000000
// 0x1091ee4: fmov s1, #0.50000000
// 0x1091ee8: fmov s2, #0.50000000
// 0x1091eec: fmov s3, #1.00000000
// 0x1091ef0: mov x1, xzr
// 0x1091ef4: bl #0x1bbb61c
// 0x1091ef8: ldr x0, [x23]
// 0x1091efc: cbz x0, #0x1092638
// 0x1091f00: mov x1, xzr
// 0x1091f04: bl #0x1bbc698
// 0x1091f08: cbz x0, #0x1092638
// 0x1091f0c: fmov s0, #0.50000000
// 0x1091f10: fmov s1, #0.50000000
// 0x1091f14: fmov s2, #0.50000000
// 0x1091f18: b #0x1091f74
// 0x1091f1c: cbz x0, #0x1092638
// 0x1091f20: ldp s2, s3, [x19, #0x58]
// 0x1091f24: ldp s0, s1, [x19, #0x50]
// 0x1091f28: mov x1, xzr
// 0x1091f2c: bl #0x1bbb61c
// 0x1091f30: ldr x0, [x19, #0x130]
// 0x1091f34: cbz x0, #0x1092638
// 0x1091f38: mov x1, xzr
// 0x1091f3c: bl #0x1bbc70c
// 0x1091f40: cbz x0, #0x1092638
// 0x1091f44: ldp s2, s3, [x19, #0x58]
// 0x1091f48: ldp s0, s1, [x19, #0x50]
// 0x1091f4c: mov x1, xzr
// 0x1091f50: bl #0x1bbb61c
// 0x1091f54: ldr x0, [x19, #0x130]
// 0x1091f58: cbz x0, #0x1092638
// 0x1091f5c: mov x1, xzr
// 0x1091f60: bl #0x1bbc698
// 0x1091f64: cbz x0, #0x1092638
// 0x1091f68: fmov s0, #1.00000000
// 0x1091f6c: fmov s1, #1.00000000
// 0x1091f70: fmov s2, #1.00000000
// 0x1091f74: fmov s3, #1.00000000
// 0x1091f78: mov x1, xzr
// 0x1091f7c: bl #0x1bbb61c
// 0x1091f80: ldr x0, [x25]
// 0x1091f84: ldr w8, [x0, #0xe0]
// 0x1091f88: cbnz w8, #0x1091f90
// 0x1091f8c: bl #0xf7da5c
// 0x1091f90: mov x0, xzr
// 0x1091f94: bl #0x1bb388c
// 0x1091f98: cbz x0, #0x1092638
// 0x1091f9c: ldr x1, [x19, #0x38]
// 0x1091fa0: mov x2, xzr
// 0x1091fa4: bl #0x1bba1f0
// 0x1091fa8: ldr x8, [x19, #0x20]
// 0x1091fac: cbz x8, #0x1092638
// 0x1091fb0: ldr x0, [x22]
// 0x1091fb4: cbz x0, #0x1092638
// 0x1091fb8: ldrb w23, [x8, #0x217]
// 0x1091fbc: mov x1, xzr
// 0x1091fc0: bl #0x1bbb5a8
// 0x1091fc4: cbz w23, #0x1092020
// 0x1091fc8: cbz x0, #0x1092638
// 0x1091fcc: ldp s2, s3, [x19, #0x68]
// 0x1091fd0: ldp s0, s1, [x19, #0x60]
// 0x1091fd4: mov x1, xzr
// 0x1091fd8: bl #0x1bbb61c
// 0x1091fdc: ldr x0, [x19, #0x110]
// 0x1091fe0: cbz x0, #0x1092638
// 0x1091fe4: mov x1, xzr
// 0x1091fe8: bl #0x1bbc70c
// 0x1091fec: cbz x0, #0x1092638
// 0x1091ff0: ldp s2, s3, [x19, #0x68]
// 0x1091ff4: ldp s0, s1, [x19, #0x60]
// 0x1091ff8: mov x1, xzr
// 0x1091ffc: bl #0x1bbb61c
// 0x1092000: ldr x0, [x19, #0x110]
// 0x1092004: cbz x0, #0x1092638
// 0x1092008: mov x1, xzr
// 0x109200c: bl #0x1bbc698
// 0x1092010: cbz x0, #0x1092638
// 0x1092014: ldp s2, s3, [x19, #0x68]
// 0x1092018: ldp s0, s1, [x19, #0x60]
// 0x109201c: b #0x109208c
// 0x1092020: cbz x0, #0x1092638
// 0x1092024: fmov s0, #0.50000000
// 0x1092028: fmov s1, #0.50000000
// 0x109202c: fmov s2, #0.50000000
// 0x1092030: fmov s3, #1.00000000
// 0x1092034: mov x1, xzr
// 0x1092038: bl #0x1bbb61c
// 0x109203c: ldr x0, [x22]
// 0x1092040: cbz x0, #0x1092638
// 0x1092044: mov x1, xzr
// 0x1092048: bl #0x1bbc70c
// 0x109204c: cbz x0, #0x1092638
// 0x1092050: fmov s0, #0.50000000
// 0x1092054: fmov s1, #0.50000000
// 0x1092058: fmov s2, #0.50000000
// 0x109205c: fmov s3, #1.00000000
// 0x1092060: mov x1, xzr
// 0x1092064: bl #0x1bbb61c
// 0x1092068: ldr x0, [x22]
// 0x109206c: cbz x0, #0x1092638
// 0x1092070: mov x1, xzr
// 0x1092074: bl #0x1bbc698
// 0x1092078: cbz x0, #0x1092638
// 0x109207c: fmov s0, #0.50000000
// 0x1092080: fmov s1, #0.50000000
// 0x1092084: fmov s2, #0.50000000
// 0x1092088: fmov s3, #1.00000000
// 0x109208c: mov x1, xzr
// 0x1092090: bl #0x1bbb61c
// 0x1092094: ldr x8, [x19, #0x20]
// 0x1092098: cbz x8, #0x1092638
// 0x109209c: ldr x8, [x8, #0x90]
// 0x10920a0: cbz x8, #0x1092638
// 0x10920a4: ldr x0, [x21]
// 0x10920a8: cbz x0, #0x1092638
// 0x10920ac: ldrb w22, [x8, #0x6a]
// 0x10920b0: mov x1, xzr
// 0x10920b4: bl #0x1bbb5a8
// 0x10920b8: cbz w22, #0x1092114
// 0x10920bc: cbz x0, #0x1092638
// 0x10920c0: ldp s2, s3, [x19, #0x68]
// 0x10920c4: ldp s0, s1, [x19, #0x60]
// 0x10920c8: mov x1, xzr
// 0x10920cc: bl #0x1bbb61c
// 0x10920d0: ldr x0, [x19, #0x120]
// 0x10920d4: cbz x0, #0x1092638
// 0x10920d8: mov x1, xzr
// 0x10920dc: bl #0x1bbc70c
// 0x10920e0: cbz x0, #0x1092638
// 0x10920e4: ldp s2, s3, [x19, #0x68]
// 0x10920e8: ldp s0, s1, [x19, #0x60]
// 0x10920ec: mov x1, xzr
// 0x10920f0: bl #0x1bbb61c
// 0x10920f4: ldr x0, [x19, #0x120]
// 0x10920f8: cbz x0, #0x1092638
// 0x10920fc: mov x1, xzr
// 0x1092100: bl #0x1bbc698
// 0x1092104: cbz x0, #0x1092638
// 0x1092108: ldp s2, s3, [x19, #0x68]
// 0x109210c: ldp s0, s1, [x19, #0x60]
// 0x1092110: b #0x1092180
// 0x1092114: cbz x0, #0x1092638
// 0x1092118: fmov s0, #0.50000000
// 0x109211c: fmov s1, #0.50000000
// 0x1092120: fmov s2, #0.50000000
// 0x1092124: fmov s3, #1.00000000
// 0x1092128: mov x1, xzr
// 0x109212c: bl #0x1bbb61c
// 0x1092130: ldr x0, [x21]
// 0x1092134: cbz x0, #0x1092638
// 0x1092138: mov x1, xzr
// 0x109213c: bl #0x1bbc70c
// 0x1092140: cbz x0, #0x1092638
// 0x1092144: fmov s0, #0.50000000
// 0x1092148: fmov s1, #0.50000000
// 0x109214c: fmov s2, #0.50000000
// 0x1092150: fmov s3, #1.00000000
// 0x1092154: mov x1, xzr
// 0x1092158: bl #0x1bbb61c
// 0x109215c: ldr x0, [x21]
// 0x1092160: cbz x0, #0x1092638
// 0x1092164: mov x1, xzr
// 0x1092168: bl #0x1bbc698
// 0x109216c: cbz x0, #0x1092638
// 0x1092170: fmov s0, #0.50000000
// 0x1092174: fmov s1, #0.50000000
// 0x1092178: fmov s2, #0.50000000
// 0x109217c: fmov s3, #1.00000000
// 0x1092180: mov x1, xzr
// 0x1092184: bl #0x1bbb61c
// 0x1092188: ldr x0, [x20]
// 0x109218c: cbz x0, #0x1092638
// 0x1092190: ldrb w21, [x19, #0x148]
// 0x1092194: mov x1, xzr
// 0x1092198: bl #0x1bbb5a8
// 0x109219c: cbz w21, #0x10921f8
// 0x10921a0: cbz x0, #0x1092638
// 0x10921a4: ldp s2, s3, [x19, #0x68]
// 0x10921a8: ldp s0, s1, [x19, #0x60]
// 0x10921ac: mov x1, xzr
// 0x10921b0: bl #0x1bbb61c
// 0x10921b4: ldr x0, [x19, #0x118]
// 0x10921b8: cbz x0, #0x1092638
// 0x10921bc: mov x1, xzr
// 0x10921c0: bl #0x1bbc70c
// 0x10921c4: cbz x0, #0x1092638
// 0x10921c8: ldp s2, s3, [x19, #0x68]
// 0x10921cc: ldp s0, s1, [x19, #0x60]
// 0x10921d0: mov x1, xzr
// 0x10921d4: bl #0x1bbb61c
// 0x10921d8: ldr x0, [x19, #0x118]
// 0x10921dc: cbz x0, #0x1092638
// 0x10921e0: mov x1, xzr
// 0x10921e4: bl #0x1bbc698
// 0x10921e8: cbz x0, #0x1092638
// 0x10921ec: ldp s2, s3, [x19, #0x68]
// 0x10921f0: ldp s0, s1, [x19, #0x60]
// 0x10921f4: b #0x1092264
// 0x10921f8: cbz x0, #0x1092638
// 0x10921fc: fmov s0, #0.50000000
// 0x1092200: fmov s1, #0.50000000
// 0x1092204: fmov s2, #0.50000000
// 0x1092208: fmov s3, #1.00000000
// 0x109220c: mov x1, xzr
// 0x1092210: bl #0x1bbb61c
// 0x1092214: ldr x0, [x20]
// 0x1092218: cbz x0, #0x1092638
// 0x109221c: mov x1, xzr
// 0x1092220: bl #0x1bbc70c
// 0x1092224: cbz x0, #0x1092638
// 0x1092228: fmov s0, #0.50000000
// 0x109222c: fmov s1, #0.50000000
// 0x1092230: fmov s2, #0.50000000
// 0x1092234: fmov s3, #1.00000000
// 0x1092238: mov x1, xzr
// 0x109223c: bl #0x1bbb61c
// 0x1092240: ldr x0, [x20]
// 0x1092244: cbz x0, #0x1092638
// 0x1092248: mov x1, xzr
// 0x109224c: bl #0x1bbc698
// 0x1092250: cbz x0, #0x1092638
// 0x1092254: fmov s0, #0.50000000
// 0x1092258: fmov s1, #0.50000000
// 0x109225c: fmov s2, #0.50000000
// 0x1092260: fmov s3, #1.00000000
// 0x1092264: mov x1, xzr
// 0x1092268: bl #0x1bbb61c
// 0x109226c: mov w8, #1
// 0x1092270: strb w8, [x19, #0x70]
// 0x1092274: ldr x0, [x19, #0x128]
// 0x1092278: cbz x0, #0x1092638
// 0x109227c: mov x1, xzr
// 0x1092280: bl #0x1bbb5a8
// 0x1092284: cbz x0, #0x1092638
// 0x1092288: ldp s2, s3, [x19, #0x58]
// 0x109228c: ldp s0, s1, [x19, #0x50]
// 0x1092290: mov x1, xzr
// 0x1092294: bl #0x1bbb61c
// 0x1092298: ldr x0, [x19, #0x128]
// 0x109229c: cbz x0, #0x1092638
// 0x10922a0: mov x1, xzr
// 0x10922a4: bl #0x1bbc70c
// 0x10922a8: cbz x0, #0x1092638
// 0x10922ac: ldp s2, s3, [x19, #0x58]
// 0x10922b0: ldp s0, s1, [x19, #0x50]
// 0x10922b4: mov x1, xzr
// 0x10922b8: bl #0x1bbb61c
// 0x10922bc: ldr x0, [x19, #0x128]
// 0x10922c0: cbz x0, #0x1092638
// 0x10922c4: mov x1, xzr
// 0x10922c8: bl #0x1bbc698
// 0x10922cc: cbz x0, #0x1092638
// 0x10922d0: fmov s0, #1.00000000
// 0x10922d4: fmov s1, #1.00000000
// 0x10922d8: fmov s2, #1.00000000
// 0x10922dc: fmov s3, #1.00000000
// 0x10922e0: mov x1, xzr
// 0x10922e4: bl #0x1bbb61c
// 0x10922e8: ldrb w8, [x19, #0x29]
// 0x10922ec: cbz w8, #0x109239c
// 0x10922f0: mov x0, xzr
// 0x10922f4: bl #0x1b77c38
// 0x10922f8: ldr s0, [x19, #0x94]
// 0x10922fc: scvtf s1, w0
// 0x1092300: mov x0, xzr
// 0x1092304: fmul s0, s0, s1
// 0x1092308: str s0, [x19, #0x9c]
// 0x109230c: bl #0x1b77c10
// 0x1092310: ldr s0, [x19, #0x98]
// 0x1092314: scvtf s1, w0
// 0x1092318: mov x0, xzr
// 0x109231c: fmul s0, s0, s1
// 0x1092320: str s0, [x19, #0xa0]
// 0x1092324: bl #0x1b77c10
// 0x1092328: adrp x21, #0x1fab000
// 0x109232c: ldrb w8, [x21, #0x242]
// 0x1092330: ldr s8, [x19, #0x74]
// 0x1092334: scvtf s9, w0
// 0x1092338: cbnz w8, #0x1092350
// 0x109233c: adrp x0, #0x1e8c000
// 0x1092340: ldr x0, [x0, #0xa60]
// 0x1092344: bl #0xf7d92c
// 0x1092348: mov w8, #1
// 0x109234c: strb w8, [x21, #0x242]
// 0x1092350: adrp x22, #0x1e8c000
// 0x1092354: ldr x22, [x22, #0xa60]
// 0x1092358: fmul s9, s8, s9
// 0x109235c: ldr x0, [x22]
// 0x1092360: ldr w8, [x0, #0xe0]
// 0x1092364: cbnz w8, #0x109236c
// 0x1092368: bl #0xf7da5c
// 0x109236c: fcvt d8, s9
// 0x1092370: add x0, sp, #0x28
// 0x1092374: mov v0.16b, v8.16b
// 0x1092378: bl #0x1db0c60
// 0x109237c: fcmp s9, #0.0
// 0x1092380: b.ge #0x1092418
// 0x1092384: fmov d1, #-0.50000000
// 0x1092388: fcmp d0, d1
// 0x109238c: b.ne #0x1092440
// 0x1092390: ldr d0, [sp, #0x28]
// 0x1092394: fmov d1, #-1.00000000
// 0x1092398: b #0x109242c
// 0x109239c: ldur d0, [x19, #0x8c]
// 0x10923a0: ldr x0, [x19, #0x128]
// 0x10923a4: stur d0, [x19, #0x9c]
// 0x10923a8: cbz x0, #0x1092638
// 0x10923ac: ldr w1, [x19, #0x7c]
// 0x10923b0: mov x2, xzr
// 0x10923b4: bl #0x1bbbf28
// 0x10923b8: ldr x0, [x19, #0x130]
// 0x10923bc: cbz x0, #0x1092638
// 0x10923c0: ldr w1, [x19, #0x7c]
// 0x10923c4: mov x2, xzr
// 0x10923c8: bl #0x1bbbf28
// 0x10923cc: ldr x0, [x19, #0x110]
// 0x10923d0: cbz x0, #0x1092638
// 0x10923d4: ldr w1, [x19, #0x7c]
// 0x10923d8: mov x2, xzr
// 0x10923dc: bl #0x1bbbf28
// 0x10923e0: ldr x0, [x19, #0x118]
// 0x10923e4: cbz x0, #0x1092638
// 0x10923e8: ldr w1, [x19, #0x7c]
// 0x10923ec: mov x2, xzr
// 0x10923f0: bl #0x1bbbf28
// 0x10923f4: ldr x0, [x19, #0x120]
// 0x10923f8: cbz x0, #0x1092638
// 0x10923fc: ldr w1, [x19, #0x7c]
// 0x1092400: mov x2, xzr
// 0x1092404: bl #0x1bbbf28
// 0x1092408: ldr x0, [x19, #0x140]
// 0x109240c: cbz x0, #0x1092638
// 0x1092410: ldr w1, [x19, #0x80]
// 0x1092414: b #0x10925a0
// 0x1092418: fmov d1, #0.50000000
// 0x109241c: fcmp d0, d1
// 0x1092420: b.ne #0x109244c
// 0x1092424: ldr d0, [sp, #0x28]
// 0x1092428: fmov d1, #1.00000000
// 0x109242c: fcvtzs x8, d0
// 0x1092430: fadd d1, d0, d1
// 0x1092434: tst x8, #1
// 0x1092438: fcsel d0, d0, d1, eq
// 0x109243c: b #0x1092454
// 0x1092440: fadd d0, d8, d1
// 0x1092444: frintp d0, d0
// 0x1092448: b #0x1092454
// 0x109244c: fadd d0, d8, d1
// 0x1092450: frintm d0, d0
// 0x1092454: mov x8, #0x7ff0000000000000
// 0x1092458: ldr x0, [x19, #0x128]
// 0x109245c: fmov d1, x8
// 0x1092460: fcvtzs w9, d0
// 0x1092464: fcmp d0, d1
// 0x1092468: mov w8, #-0x80000000
// 0x109246c: csel w20, w8, w9, eq
// 0x1092470: cbz x0, #0x1092638
// 0x1092474: mov w1, w20
// 0x1092478: mov x2, xzr
// 0x109247c: bl #0x1bbbf28
// 0x1092480: ldr x0, [x19, #0x130]
// 0x1092484: cbz x0, #0x1092638
// 0x1092488: mov w1, w20
// 0x109248c: mov x2, xzr
// 0x1092490: bl #0x1bbbf28
// 0x1092494: ldr x0, [x19, #0x110]
// 0x1092498: cbz x0, #0x1092638
// 0x109249c: mov w1, w20
// 0x10924a0: mov x2, xzr
// 0x10924a4: bl #0x1bbbf28
// 0x10924a8: ldr x0, [x19, #0x118]
// 0x10924ac: cbz x0, #0x1092638
// 0x10924b0: mov w1, w20
// 0x10924b4: mov x2, xzr
// 0x10924b8: bl #0x1bbbf28
// 0x10924bc: ldr x0, [x19, #0x120]
// 0x10924c0: cbz x0, #0x1092638
// 0x10924c4: mov w1, w20
// 0x10924c8: mov x2, xzr
// 0x10924cc: bl #0x1bbbf28
// 0x10924d0: ldr x20, [x19, #0x140]
// 0x10924d4: mov x0, xzr
// 0x10924d8: bl #0x1b77c10
// 0x10924dc: ldrb w8, [x21, #0x242]
// 0x10924e0: ldr s8, [x19, #0x78]
// 0x10924e4: scvtf s9, w0
// 0x10924e8: cbnz w8, #0x1092500
// 0x10924ec: adrp x0, #0x1e8c000
// 0x10924f0: ldr x0, [x0, #0xa60]
// 0x10924f4: bl #0xf7d92c
// 0x10924f8: mov w8, #1
// 0x10924fc: strb w8, [x21, #0x242]
// 0x1092500: ldr x0, [x22]
// 0x1092504: fmul s9, s8, s9
// 0x1092508: ldr w8, [x0, #0xe0]
// 0x109250c: cbnz w8, #0x1092514
// 0x1092510: bl #0xf7da5c
// 0x1092514: fcvt d8, s9
// 0x1092518: add x0, sp, #0x28
// 0x109251c: mov v0.16b, v8.16b
// 0x1092520: bl #0x1db0c60
// 0x1092524: fcmp s9, #0.0
// 0x1092528: b.ge #0x1092544
// 0x109252c: fmov d1, #-0.50000000
// 0x1092530: fcmp d0, d1
// 0x1092534: b.ne #0x109256c
// 0x1092538: ldr d0, [sp, #0x28]
// 0x109253c: fmov d1, #-1.00000000
// 0x1092540: b #0x1092558
// 0x1092544: fmov d1, #0.50000000
// 0x1092548: fcmp d0, d1
// 0x109254c: b.ne #0x1092578
// 0x1092550: ldr d0, [sp, #0x28]
// 0x1092554: fmov d1, #1.00000000
// 0x1092558: fcvtzs x8, d0
// 0x109255c: fadd d1, d0, d1
// 0x1092560: tst x8, #1
// 0x1092564: fcsel d0, d0, d1, eq
// 0x1092568: b #0x1092580
// 0x109256c: fadd d0, d8, d1
// 0x1092570: frintp d0, d0
// 0x1092574: b #0x1092580
// 0x1092578: fadd d0, d8, d1
// 0x109257c: frintm d0, d0
// 0x1092580: cbz x20, #0x1092638
// 0x1092584: mov x8, #0x7ff0000000000000
// 0x1092588: fmov d1, x8
// 0x109258c: fcvtzs w9, d0
// 0x1092590: fcmp d0, d1
// 0x1092594: mov w8, #-0x80000000
// 0x1092598: csel w1, w8, w9, eq
// 0x109259c: mov x0, x20
// 0x10925a0: mov x2, xzr
// 0x10925a4: bl #0x1bbbf28
// 0x10925a8: ldr x0, [x19, #0x140]
// 0x10925ac: cbz x0, #0x1092638
// 0x10925b0: mov x1, xzr
// 0x10925b4: bl #0x1bbb5a8
// 0x10925b8: cbz x0, #0x1092638
// 0x10925bc: fmov s0, #1.00000000
// 0x10925c0: fmov s1, #1.00000000
// 0x10925c4: fmov s2, #1.00000000
// 0x10925c8: fmov s3, #1.00000000
// 0x10925cc: mov x1, xzr
// 0x10925d0: bl #0x1bbb61c
// 0x10925d4: mov x0, xzr
// 0x10925d8: bl #0x1b77c10
// 0x10925dc: ldr s0, [x19, #0x88]
// 0x10925e0: ldp s1, s2, [x19, #0xa0]
// 0x10925e4: scvtf s3, w0
// 0x10925e8: fmov s4, #-0.50000000
// 0x10925ec: fmul s0, s0, s3
// 0x10925f0: fsub s0, s0, s1
// 0x10925f4: fmul s1, s2, s4
// 0x10925f8: fadd s0, s0, s1
// 0x10925fc: mov x0, xzr
// 0x1092600: str s0, [x19, #0xac]
// 0x1092604: bl #0x1b77c38
// 0x1092608: ldr s0, [x19, #0x84]
// 0x109260c: scvtf s1, w0
// 0x1092610: ldp x22, x21, [sp, #0x50]
// 0x1092614: ldp x24, x23, [sp, #0x40]
// 0x1092618: fmul s0, s0, s1
// 0x109261c: str s0, [x19, #0xa8]
// 0x1092620: ldp x20, x19, [sp, #0x60]
// 0x1092624: ldp x26, x25, [sp, #0x30]
// 0x1092628: ldr x30, [sp, #0x20]
// 0x109262c: ldp d9, d8, [sp, #0x10]
// 0x1092630: ldp d11, d10, [sp], #0x70
// 0x1092634: ret
// 0x1092638: bl #0xf7db74
```

## `MainMenu.PlayButtonFx` — RVA `0xc9263c`

- Decompiled symbol: `MainMenu_PlayButtonFx`
- Metadata signature: `private void PlayButtonFx(AudioClip clip, float vol) { }`
- Native interval: `80` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[184];
    unsigned long long field_b8;
} struct_0;

void MainMenu_PlayButtonFx(struct_0 *ptr, long long a1)
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
    v6 = ptr->field_b8;
    if (v6)
    {
        AudioSource__set_volume(v6, 0);
        v6 = ptr->field_b8;
        if (v6)
        {
            AudioSource__set_clip(v6, a1, 0);
            v6 = ptr->field_b8;
            if (ptr->field_b8)
            {
                AudioSource__Play();
                return;
            }
        }
    }
    sub_f7db74(v6);
}
```

## `MainMenu.ctor` — RVA `0xc9268c`

- Decompiled symbol: `MainMenu_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `88` bytes
- Result: `pseudocode`
- Heuristic layout hint: `MainMenu_Recovered` matched 10 offsets against `MainMenu` metadata (confidence 1.00).

```c
typedef struct MainMenu_Recovered {
    char padding_0[40];
    char useMainMenu;
    char padding_29[75];
    unsigned int fontSizeScaled;
    char padding_78[4];
    unsigned long long fontSize;
    unsigned long long menuPosV;
    char padding_8c[8];
    unsigned long long buttonHeightScaled;
    char padding_9c[8];
    unsigned int buttonSpacing;
    char padding_a8[32];
    unsigned int buttonFxVol;
    char padding_cc[12];
    unsigned int invulFxVol;
    char padding_dc[12];
    unsigned int giveAllFxVol;
    char padding_ec[12];
    unsigned int beepFxVol;
} MainMenu_Recovered;

long long MainMenu_ctor(struct_0 *ptr)
{
    long long v0;  // x0

    ptr->field_28 = 1;
    *((unsigned long long *)&(&ptr->padding_78)[1]) = 60129542158;
    ptr->field_74 = 1020054733;
    *((unsigned long long *)((char *)&ptr->field_7c + 4)) = 4539628425439713690;
    *((unsigned int *)&ptr->padding_9c[4]) = 0x41200000;
    *((unsigned int *)&ptr->padding_a8[28]) = 0x3f800000;
    *((unsigned int *)&ptr->padding_cc[8]) = 0x3f800000;
    *((unsigned int *)&ptr->padding_dc[8]) = 0x3f800000;
    *((unsigned long long *)&ptr->padding_8c[4]) = 4512246540032121242;
    *((unsigned int *)&ptr->padding_ec[8]) = 0x3f800000;
    v0 = MonoBehaviour__ctor();
    return MonoBehaviour__ctor();
}
```
