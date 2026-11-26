# Native pseudocode: bl_MiniMapItem

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `bl_MiniMapItem.Start` — RVA `0xcc8b68`

- Decompiled symbol: `bl_MiniMapItem_Start`
- Metadata signature: `private void Start() { }`
- Native interval: `248` bytes
- Result: `pseudocode`
- Heuristic layout hint: `bl_MiniMapItem_Recovered` matched 9 offsets against `bl_MiniMapItem` metadata (confidence 1.00).

```c
typedef struct bl_MiniMapItem_Recovered {
    char padding_0[32];
    long long GraphicPrefab;
    long long Target;
    char padding_30[16];
    long long Icon;
    char padding_48[56];
    unsigned int InfoItem;
    char padding_84[16];
    unsigned int RenderDelay;
    char padding_98[8];
    struct struct_7 *Graphic;
    long long RectRoot;
    long long cacheItem;
    char padding_b8[24];
    long long MiniMap;
} bl_MiniMapItem_Recovered;

typedef struct struct_8 {
    char padding_0[376];
    long long field_178;
} struct_8;

typedef struct struct_9 {
    char padding_0[680];
    struct struct_10 *field_2a8;
    unsigned long long field_2b0;
} struct_9;

typedef struct struct_11 {
    char padding_0[88];
    unsigned int field_58;
} struct_11;

typedef struct struct_7 {
    struct struct_4 *field_0;
} struct_7;

typedef struct struct_10 {
    unsigned long long field_0;
} struct_10;

typedef struct struct_4 {
    char padding_0[680];
    struct struct_5 *field_2a8;
    unsigned long long field_2b0;
} struct_4;

typedef struct struct_5 {
    unsigned long long field_0;
} struct_5;

typedef struct struct_2 {
    char padding_0[16];
    long long field_10;
} struct_2;

typedef struct struct_3 {
    char padding_0[184];
    struct struct_2 *field_b8;
} struct_3;

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
extern long long g_1ef22b8;
extern struct_3 *g_1ef2b00;
extern long long g_1efd060;
extern long long g_1efd0c8;
extern long long g_1efeb78;
extern long long g_1efec00;
extern long long g_1efed38;
extern long long g_1f00238;
extern char g_1fab1e0;
extern char g_1fab561;
extern char g_1fab562;

long long bl_MiniMapItem_Start(struct_6 *a0)
{
    long long v1;  // x1
    struct_6 *ptr4;  // x0
    struct_6 *v11;  // x22
    struct_9 **v12;  // x0
    struct_6 *p;  // x21
    struct_6 *v14;  // x21
    unsigned long long flag;  // x2
    struct_9 **v16;  // x0
    unsigned long v17;  // x1
    long long v18;  // x0
    long long v19;  // x22
    unsigned long v20;  // x0
    unsigned long long v3;  // x23
    long long v21;  // x21
    struct_6 *v22;  // x20
    long long v23;  // x0
    struct_11 *ptr5;  // x0
    struct_11 *v25;  // x20
    long long v27;  // x0
    unsigned long long v28;  // x0
    struct_6 *ptr;  // x19
    long long v5;  // x0
    struct_6 *addr;  // x20
    struct_6 *v7;  // x20
    struct_8 *ptr6;  // x0
    long long v9;  // x1
    struct_6 *ptr3;  // x22
    unsigned long long v0;  // [bp-0x28]

    if (!(g_1fab561 & 1))
    {
        sub_f7d92c(&g_1eef458);
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c("!'");
        sub_f7d92c(&g_1ef2b00);
        g_1fab561 = 1;
    }
    v1 = bl_MiniMapUtils__GetMiniMap(0);
    ptr4 = a0;
    ptr4->field_d0 = v1;
    sub_f7d8d0((struct bl_MiniMapItem_Recovered *)&ptr4->field_d0, v1);
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (((char)Object__op_Inequality(g_1ef2b00->field_b8->field_10, 0, 0) & 1))
    {
        v0 = v3;
        ptr = a0;
        if (!(g_1fab562 & 1))
        {
            sub_f7d92c(&g_1efd060);
            sub_f7d92c(&g_1efd0c8);
            sub_f7d92c(&g_1efeb78);
            sub_f7d92c(&g_1efec00);
            sub_f7d92c(&g_1efed38);
            sub_f7d92c(&g_1f00238);
            sub_f7d92c(&g_1ef0c58);
            g_1fab562 = 1;
        }
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        v5 = sub_1129f50(ptr->field_20, g_1f00238);
        addr = ptr;
        addr->field_b0 = v5;
        v7 = &addr->field_b0;
        sub_f7d8d0(v7, v5);
        ptr6 = bl_MiniMapUtils__GetMiniMap(0);
        if (ptr6)
        {
            v9 = ptr6->field_178;
            ptr3 = ptr;
            ptr3->field_a8 = v9;
            v11 = &ptr3->field_a8;
            sub_f7d8d0(v11, v9);
            if (*((long long *)&v11->padding_0[8]))
            {
                v12 = sub_1249224(*((long long *)&v11->padding_0[8]), g_1efec00);
                p = ptr;
                p->field_a0 = v12;
                v14 = &p->field_a0;
                sub_f7d8d0(v14, v12);
                if (((char)Object__op_Inequality(*((long long *)&v14->padding_48[24]), 0, 0) & 1))
                {
                    if (*((long long *)&v14->padding_0[0]))
                    {
                        flag = 0;
                        Image__set_sprite(*((long long *)&v14->padding_0[0]), ptr->field_40, 0);
                        v16 = ptr->field_a0;
                        if (v16)
                        {
                            v17 = *(v16)->field_2b0;
                            *(v16)->field_2a8();
                        }
                    }
                }
                else
                {
                    if (*((long long *)&v7->padding_0[0]))
                    {
                        v18 = GameObject__get_transform(*((long long *)&v7->padding_0[0]), 0);
                        if (*((long long *)&v11->padding_0[0]))
                        {
                            v19 = v18;
                            v20 = Component__get_transform(*((long long *)&v11->padding_0[0]), 0);
                            if (v19)
                            {
                                Transform__SetParent(v19, v20, 0, 0);
                                if (*((long long *)&v14->padding_0[0]))
                                {
                                    v21 = sub_1231bc8(*((long long *)&v14->padding_0[0]), g_1efd060);
                                    if (!g_1fab1e0)
                                    {
                                        sub_f7d92c(&g_1ef22b8);
                                        g_1fab1e0 = 1;
                                    }
                                    if (v21)
                                    {
                                        RectTransform__set_anchoredPosition(v21, 0);
                                        if (*((long long *)&v7->padding_0[0]) && sub_1249224(*((long long *)&v7->padding_0[0]), g_1efeb78))
                                        {
                                            CanvasGroup__set_interactable();
                                            v22 = ptr;
                                            if (!g_1ef0c58->field_e0)
                                                sub_f7da5c(g_1ef0c58);
                                            if (((char)Object__op_Equality(v22->field_28, 0, 0) & 1))
                                            {
                                                v23 = sub_1231bc8(ptr, g_1efd0c8);
                                                ptr->field_28 = v23;
                                                sub_f7d8d0((struct bl_MiniMapItem_Recovered *)&v22->field_28, v23);
                                            }
                                            bl_MiniMapItem__StartEffect();
                                            if (ptr->field_b0)
                                            {
                                                ptr5 = sub_1249224(ptr->field_b0, g_1efed38);
                                                if (ptr5)
                                                {
                                                    v25 = ptr5;
                                                    ptr5->field_58 = ptr->field_94;
                                                    MonoBehaviour__StartCoroutine(v25, bl_IconItem__FadeIcon(ptr5), 0);
                                                    v27 = bl_IconItem__GetInfoItem(v25, *((long long *)&ptr->field_80));
                                                    return bl_IconItem__GetInfoItem(v25, *((long long *)&ptr->field_80));
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
    else
    {
        if (!g_1eef458->field_e0)
            sub_f7da5c(g_1eef458);
        v28 = Debug__Log();
        return Debug__Log();
    }
}
```

## `bl_MiniMapItem.CreateIcon` — RVA `0xcc8c60`

- Decompiled symbol: `bl_MiniMapItem_CreateIcon`
- Metadata signature: `private void CreateIcon() { }`
- Native interval: `712` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: CFGFast did not recover a function at the metadata RVA

```c
// 0x10c8c60: stp x30, x23, [sp, #-0x30]!
// 0x10c8c64: stp x22, x21, [sp, #0x10]
// 0x10c8c68: stp x20, x19, [sp, #0x20]
// 0x10c8c6c: adrp x20, #0x1fab000
// 0x10c8c70: adrp x23, #0x1e8c000
// 0x10c8c74: ldrb w8, [x20, #0x562]
// 0x10c8c78: ldr x23, [x23, #0xd8]
// 0x10c8c7c: mov x19, x0
// 0x10c8c80: tbnz w8, #0, #0x10c8ce0
// 0x10c8c84: adrp x0, #0x1e8c000
// 0x10c8c88: ldr x0, [x0, #0xbb0]
// 0x10c8c8c: bl #0xf7d92c
// 0x10c8c90: adrp x0, #0x1e8e000
// 0x10c8c94: ldr x0, [x0, #0xa18]
// 0x10c8c98: bl #0xf7d92c
// 0x10c8c9c: adrp x0, #0x1e8d000
// 0x10c8ca0: ldr x0, [x0, #0x160]
// 0x10c8ca4: bl #0xf7d92c
// 0x10c8ca8: adrp x0, #0x1e8d000
// 0x10c8cac: ldr x0, [x0, #0xbf8]
// 0x10c8cb0: bl #0xf7d92c
// 0x10c8cb4: adrp x0, #0x1e8e000
// 0x10c8cb8: ldr x0, [x0, #0xad8]
// 0x10c8cbc: bl #0xf7d92c
// 0x10c8cc0: adrp x0, #0x1e8d000
// 0x10c8cc4: ldr x0, [x0, #0x9e0]
// 0x10c8cc8: bl #0xf7d92c
// 0x10c8ccc: adrp x0, #0x1e8c000
// 0x10c8cd0: ldr x0, [x0, #0xd8]
// 0x10c8cd4: bl #0xf7d92c
// 0x10c8cd8: mov w8, #1
// 0x10c8cdc: strb w8, [x20, #0x562]
// 0x10c8ce0: ldr x0, [x23]
// 0x10c8ce4: adrp x21, #0x1e8d000
// 0x10c8ce8: ldr x20, [x19, #0x20]
// 0x10c8cec: ldr w8, [x0, #0xe0]
// 0x10c8cf0: ldr x21, [x21, #0x9e0]
// 0x10c8cf4: cbnz w8, #0x10c8cfc
// 0x10c8cf8: bl #0xf7da5c
// 0x10c8cfc: ldr x1, [x21]
// 0x10c8d00: mov x0, x20
// 0x10c8d04: bl #0x1129f50
// 0x10c8d08: mov x20, x19
// 0x10c8d0c: str x0, [x20, #0xb0]!
// 0x10c8d10: mov x1, x0
// 0x10c8d14: mov x0, x20
// 0x10c8d18: bl #0xf7d8d0
// 0x10c8d1c: mov w0, wzr
// 0x10c8d20: bl #0x10c6020
// 0x10c8d24: cbz x0, #0x10c8f24
// 0x10c8d28: ldr x1, [x0, #0x178]
// 0x10c8d2c: mov x22, x19
// 0x10c8d30: str x1, [x22, #0xa8]!
// 0x10c8d34: mov x0, x22
// 0x10c8d38: bl #0xf7d8d0
// 0x10c8d3c: ldr x0, [x22, #8]
// 0x10c8d40: cbz x0, #0x10c8f24
// 0x10c8d44: adrp x8, #0x1e8d000
// 0x10c8d48: ldr x8, [x8, #0xbf8]
// 0x10c8d4c: ldr x1, [x8]
// 0x10c8d50: bl #0x1249224
// 0x10c8d54: mov x21, x19
// 0x10c8d58: str x0, [x21, #0xa0]!
// 0x10c8d5c: mov x1, x0
// 0x10c8d60: mov x0, x21
// 0x10c8d64: bl #0xf7d8d0
// 0x10c8d68: ldur x0, [x21, #-0x60]
// 0x10c8d6c: mov x1, xzr
// 0x10c8d70: mov x2, xzr
// 0x10c8d74: bl #0x1b94ac8
// 0x10c8d78: tbz w0, #0, #0x10c8db0
// 0x10c8d7c: ldr x0, [x21]
// 0x10c8d80: cbz x0, #0x10c8f24
// 0x10c8d84: ldr x1, [x19, #0x40]
// 0x10c8d88: mov x2, xzr
// 0x10c8d8c: bl #0x1c13790
// 0x10c8d90: ldr x0, [x19, #0xa0]
// 0x10c8d94: cbz x0, #0x10c8f24
// 0x10c8d98: ldr x8, [x0]
// 0x10c8d9c: ldp s2, s3, [x19, #0x58]
// 0x10c8da0: ldp s0, s1, [x19, #0x50]
// 0x10c8da4: ldr x9, [x8, #0x2a8]
// 0x10c8da8: ldr x1, [x8, #0x2b0]
// 0x10c8dac: blr x9
// 0x10c8db0: ldr x0, [x20]
// 0x10c8db4: cbz x0, #0x10c8f24
// 0x10c8db8: mov x1, xzr
// 0x10c8dbc: bl #0x1b94c14
// 0x10c8dc0: ldr x8, [x22]
// 0x10c8dc4: cbz x8, #0x10c8f24
// 0x10c8dc8: mov x22, x0
// 0x10c8dcc: mov x0, x8
// 0x10c8dd0: mov x1, xzr
// 0x10c8dd4: bl #0x1b92154
// 0x10c8dd8: cbz x22, #0x10c8f24
// 0x10c8ddc: mov x1, x0
// 0x10c8de0: mov x0, x22
// 0x10c8de4: mov w2, wzr
// 0x10c8de8: mov x3, xzr
// 0x10c8dec: bl #0x1b9de4c
// 0x10c8df0: ldr x0, [x21]
// 0x10c8df4: cbz x0, #0x10c8f24
// 0x10c8df8: adrp x8, #0x1e8c000
// 0x10c8dfc: ldr x8, [x8, #0xbb0]
// 0x10c8e00: ldr x1, [x8]
// 0x10c8e04: bl #0x1231bc8
// 0x10c8e08: adrp x22, #0x1fab000
// 0x10c8e0c: ldrb w8, [x22, #0x1e0]
// 0x10c8e10: mov x21, x0
// 0x10c8e14: cbnz w8, #0x10c8e2c
// 0x10c8e18: adrp x0, #0x1e8c000
// 0x10c8e1c: ldr x0, [x0, #0x138]
// 0x10c8e20: bl #0xf7d92c
// 0x10c8e24: mov w8, #1
// 0x10c8e28: strb w8, [x22, #0x1e0]
// 0x10c8e2c: cbz x21, #0x10c8f24
// 0x10c8e30: adrp x8, #0x1e8c000
// 0x10c8e34: ldr x8, [x8, #0x138]
// 0x10c8e38: mov x0, x21
// 0x10c8e3c: mov x1, xzr
// 0x10c8e40: ldr x8, [x8]
// 0x10c8e44: ldr x8, [x8, #0xb8]
// 0x10c8e48: ldp s0, s1, [x8]
// 0x10c8e4c: bl #0x1b9c820
// 0x10c8e50: ldr x0, [x20]
// 0x10c8e54: cbz x0, #0x10c8f24
// 0x10c8e58: adrp x8, #0x1e8d000
// 0x10c8e5c: ldr x8, [x8, #0x160]
// 0x10c8e60: ldr x1, [x8]
// 0x10c8e64: bl #0x1249224
// 0x10c8e68: cbz x0, #0x10c8f24
// 0x10c8e6c: ldrb w1, [x19, #0x7c]
// 0x10c8e70: mov x2, xzr
// 0x10c8e74: bl #0x1d6de5c
// 0x10c8e78: mov x20, x19
// 0x10c8e7c: ldr x21, [x20, #0x28]!
// 0x10c8e80: ldr x0, [x23]
// 0x10c8e84: ldr w8, [x0, #0xe0]
// 0x10c8e88: cbnz w8, #0x10c8e90
// 0x10c8e8c: bl #0xf7da5c
// 0x10c8e90: mov x0, x21
// 0x10c8e94: mov x1, xzr
// 0x10c8e98: mov x2, xzr
// 0x10c8e9c: bl #0x1b9568c
// 0x10c8ea0: tbz w0, #0, #0x10c8ec8
// 0x10c8ea4: adrp x8, #0x1e8e000
// 0x10c8ea8: ldr x8, [x8, #0xa18]
// 0x10c8eac: mov x0, x19
// 0x10c8eb0: ldr x1, [x8]
// 0x10c8eb4: bl #0x1231bc8
// 0x10c8eb8: mov x1, x0
// 0x10c8ebc: str x0, [x19, #0x28]
// 0x10c8ec0: mov x0, x20
// 0x10c8ec4: bl #0xf7d8d0
// 0x10c8ec8: mov x0, x19
// 0x10c8ecc: bl #0x10c8f28
// 0x10c8ed0: ldr x0, [x19, #0xb0]
// 0x10c8ed4: cbz x0, #0x10c8f24
// 0x10c8ed8: adrp x8, #0x1e8e000
// 0x10c8edc: ldr x8, [x8, #0xad8]
// 0x10c8ee0: ldr x1, [x8]
// 0x10c8ee4: bl #0x1249224
// 0x10c8ee8: cbz x0, #0x10c8f24
// 0x10c8eec: ldr s0, [x19, #0x94]
// 0x10c8ef0: mov x20, x0
// 0x10c8ef4: str s0, [x0, #0x58]
// 0x10c8ef8: bl #0x10c6104
// 0x10c8efc: mov x1, x0
// 0x10c8f00: mov x0, x20
// 0x10c8f04: mov x2, xzr
// 0x10c8f08: bl #0x1b95d40
// 0x10c8f0c: ldr x1, [x19, #0x80]
// 0x10c8f10: mov x0, x20
// 0x10c8f14: ldp x20, x19, [sp, #0x20]
// 0x10c8f18: ldp x22, x21, [sp, #0x10]
// 0x10c8f1c: ldp x30, x23, [sp], #0x30
// 0x10c8f20: b #0x10c5d8c
// 0x10c8f24: bl #0xf7db74
```

## `bl_MiniMapItem.StartEffect` — RVA `0xcc8f28`

- Decompiled symbol: `bl_MiniMapItem_StartEffect`
- Metadata signature: `private void StartEffect() { }`
- Native interval: `160` bytes
- Result: `pseudocode`
- Heuristic layout hint: `bl_MiniMapItem_Recovered` matched 2 offsets against `bl_MiniMapItem` metadata (confidence 1.00).

```c
typedef struct bl_MiniMapItem_Recovered {
    char padding_0[152];
    unsigned int m_Effect;
    char padding_9c[4];
    long long Graphic;
} bl_MiniMapItem_Recovered;

extern long long g_1efcf08;
extern char g_1fab564;

void bl_MiniMapItem_StartEffect(struct_0 *ptr)
{
    long long v0;  // x0

    if (!(g_1fab564 & 1))
    {
        sub_f7d92c(&g_1efcf08);
        sub_f7d92c("e#");
        g_1fab564 = 1;
    }
    v0 = ptr->field_a0;
    if (v0)
    {
        v0 = sub_1231bc8(v0, g_1efcf08);
        if (ptr->field_98 != 1)
        {
            if (ptr->field_98)
            {
                return;
            }
            else if (v0)
            {
                Animator__SetInteger();
                return;
            }
        }
        else
        {
            if (v0)
            {
                Animator__SetInteger();
                return;
            }
        }
    }
    sub_f7db74(v0);
}
```

## `bl_MiniMapItem.Update` — RVA `0xcc8fc8`

- Decompiled symbol: `bl_MiniMapItem_Update`
- Metadata signature: `private void Update() { }`
- Native interval: `1848` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: Decompiler produced no C-like text

```c
// 0x10c8fc8: sub sp, sp, #0xb0
// 0x10c8fcc: stp d15, d14, [sp, #0x30]
// 0x10c8fd0: stp d13, d12, [sp, #0x40]
// 0x10c8fd4: stp d11, d10, [sp, #0x50]
// 0x10c8fd8: stp d9, d8, [sp, #0x60]
// 0x10c8fdc: stp x30, x25, [sp, #0x70]
// 0x10c8fe0: stp x24, x23, [sp, #0x80]
// 0x10c8fe4: stp x22, x21, [sp, #0x90]
// 0x10c8fe8: stp x20, x19, [sp, #0xa0]
// 0x10c8fec: adrp x20, #0x1fab000
// 0x10c8ff0: adrp x21, #0x1e8c000
// 0x10c8ff4: ldrb w8, [x20, #0x563]
// 0x10c8ff8: ldr x21, [x21, #0xd8]
// 0x10c8ffc: mov x19, x0
// 0x10c9000: tbnz w8, #0, #0x10c9030
// 0x10c9004: adrp x0, #0x1e8c000
// 0x10c9008: ldr x0, [x0, #0xbb0]
// 0x10c900c: bl #0xf7d92c
// 0x10c9010: adrp x0, #0x1e8c000
// 0x10c9014: ldr x0, [x0, #0xd8]
// 0x10c9018: bl #0xf7d92c
// 0x10c901c: adrp x0, #0x1e8e000
// 0x10c9020: ldr x0, [x0, #0xa08]
// 0x10c9024: bl #0xf7d92c
// 0x10c9028: mov w8, #1
// 0x10c902c: strb w8, [x20, #0x563]
// 0x10c9030: ldr x0, [x21]
// 0x10c9034: ldr x20, [x19, #0x28]
// 0x10c9038: ldr w8, [x0, #0xe0]
// 0x10c903c: cbnz w8, #0x10c9044
// 0x10c9040: bl #0xf7da5c
// 0x10c9044: mov x0, x20
// 0x10c9048: mov x1, xzr
// 0x10c904c: mov x2, xzr
// 0x10c9050: bl #0x1b9568c
// 0x10c9054: tbnz w0, #0, #0x10c9080
// 0x10c9058: ldr x0, [x21]
// 0x10c905c: ldr x20, [x19, #0xa0]
// 0x10c9060: ldr w8, [x0, #0xe0]
// 0x10c9064: cbnz w8, #0x10c906c
// 0x10c9068: bl #0xf7da5c
// 0x10c906c: mov x0, x20
// 0x10c9070: mov x1, xzr
// 0x10c9074: mov x2, xzr
// 0x10c9078: bl #0x1b9568c
// 0x10c907c: tbz w0, #0, #0x10c90a8
// 0x10c9080: ldp x20, x19, [sp, #0xa0]
// 0x10c9084: ldp x22, x21, [sp, #0x90]
// 0x10c9088: ldp x24, x23, [sp, #0x80]
// 0x10c908c: ldp x30, x25, [sp, #0x70]
// 0x10c9090: ldp d9, d8, [sp, #0x60]
// 0x10c9094: ldp d11, d10, [sp, #0x50]
// 0x10c9098: ldp d13, d12, [sp, #0x40]
// 0x10c909c: ldp d15, d14, [sp, #0x30]
// 0x10c90a0: add sp, sp, #0xb0
// 0x10c90a4: ret
// 0x10c90a8: ldr x0, [x19, #0xa0]
// 0x10c90ac: cbz x0, #0x10c96fc
// 0x10c90b0: adrp x8, #0x1e8c000
// 0x10c90b4: ldr x8, [x8, #0xbb0]
// 0x10c90b8: ldr x1, [x8]
// 0x10c90bc: bl #0x1231bc8
// 0x10c90c0: mov x20, x0
// 0x10c90c4: mov x0, x19
// 0x10c90c8: bl #0x10c9700
// 0x10c90cc: adrp x23, #0x1e8e000
// 0x10c90d0: ldr x23, [x23, #0xa08]
// 0x10c90d4: ldr x8, [x23]
// 0x10c90d8: ldr x8, [x8, #0xb8]
// 0x10c90dc: ldr x0, [x8, #8]
// 0x10c90e0: cbz x0, #0x10c96fc
// 0x10c90e4: ldp s4, s3, [x19, #0x34]
// 0x10c90e8: ldr s5, [x19, #0x30]
// 0x10c90ec: mov x1, xzr
// 0x10c90f0: fadd s2, s2, s3
// 0x10c90f4: fadd s1, s1, s4
// 0x10c90f8: fadd s0, s0, s5
// 0x10c90fc: bl #0x1b6f6c0
// 0x10c9100: ldr x0, [x19, #0xa8]
// 0x10c9104: cbz x0, #0x10c96fc
// 0x10c9108: mov x1, xzr
// 0x10c910c: mov v9.16b, v0.16b
// 0x10c9110: mov v8.16b, v1.16b
// 0x10c9114: bl #0x1b9c8ac
// 0x10c9118: ldr x0, [x19, #0xa8]
// 0x10c911c: cbz x0, #0x10c96fc
// 0x10c9120: mov x1, xzr
// 0x10c9124: mov v10.16b, v0.16b
// 0x10c9128: bl #0x1b9c8ac
// 0x10c912c: ldr x0, [x19, #0xa8]
// 0x10c9130: cbz x0, #0x10c96fc
// 0x10c9134: mov x1, xzr
// 0x10c9138: mov v11.16b, v0.16b
// 0x10c913c: bl #0x1b9c8ac
// 0x10c9140: ldr x0, [x19, #0xa8]
// 0x10c9144: cbz x0, #0x10c96fc
// 0x10c9148: mov x1, xzr
// 0x10c914c: mov v12.16b, v1.16b
// 0x10c9150: bl #0x1b9c8ac
// 0x10c9154: ldrb w8, [x19, #0x88]
// 0x10c9158: fmov s2, #0.50000000
// 0x10c915c: fmul s0, s9, s10
// 0x10c9160: fmul s3, s8, s12
// 0x10c9164: fmul s4, s11, s2
// 0x10c9168: fmul s1, s1, s2
// 0x10c916c: fsub s9, s0, s4
// 0x10c9170: fsub s8, s3, s1
// 0x10c9174: stp s9, s8, [x19, #0xc0]
// 0x10c9178: str wzr, [x19, #0xc8]
// 0x10c917c: cbz w8, #0x10c9234
// 0x10c9180: ldr x0, [x19, #0xa8]
// 0x10c9184: cbz x0, #0x10c96fc
// 0x10c9188: mov x1, xzr
// 0x10c918c: bl #0x1b9c8ac
// 0x10c9190: ldr x0, [x19, #0xa8]
// 0x10c9194: cbz x0, #0x10c96fc
// 0x10c9198: ldr s11, [x19, #0x8c]
// 0x10c919c: mov x1, xzr
// 0x10c91a0: mov v10.16b, v0.16b
// 0x10c91a4: bl #0x1b9c8ac
// 0x10c91a8: ldr s1, [x19, #0x8c]
// 0x10c91ac: fmov s2, #0.50000000
// 0x10c91b0: fmul s3, s10, s2
// 0x10c91b4: fmul s0, s0, s2
// 0x10c91b8: ldr x0, [x19, #0xa8]
// 0x10c91bc: fsub s2, s3, s11
// 0x10c91c0: fsub s0, s0, s1
// 0x10c91c4: fneg s2, s2
// 0x10c91c8: fcmp s9, s0
// 0x10c91cc: fcsel s0, s0, s9, gt
// 0x10c91d0: fcmp s9, s2
// 0x10c91d4: fcsel s0, s0, s2, pl
// 0x10c91d8: str s0, [x19, #0xc0]
// 0x10c91dc: cbz x0, #0x10c96fc
// 0x10c91e0: ldr s11, [x19, #0xc4]
// 0x10c91e4: mov x1, xzr
// 0x10c91e8: bl #0x1b9c8ac
// 0x10c91ec: ldr x0, [x19, #0xa8]
// 0x10c91f0: cbz x0, #0x10c96fc
// 0x10c91f4: ldr s12, [x19, #0x8c]
// 0x10c91f8: mov x1, xzr
// 0x10c91fc: mov v10.16b, v1.16b
// 0x10c9200: bl #0x1b9c8ac
// 0x10c9204: ldr s0, [x19, #0x8c]
// 0x10c9208: fmov s2, #0.50000000
// 0x10c920c: fmul s3, s10, s2
// 0x10c9210: fmul s1, s1, s2
// 0x10c9214: fsub s2, s3, s12
// 0x10c9218: fsub s0, s1, s0
// 0x10c921c: fneg s2, s2
// 0x10c9220: fcmp s11, s0
// 0x10c9224: fcsel s0, s0, s11, gt
// 0x10c9228: fcmp s11, s2
// 0x10c922c: fcsel s0, s0, s2, pl
// 0x10c9230: str s0, [x19, #0xc4]
// 0x10c9234: mov x0, x19
// 0x10c9238: bl #0x10c97dc
// 0x10c923c: cbz x0, #0x10c96fc
// 0x10c9240: ldrb w8, [x0, #0x6c]
// 0x10c9244: add x22, x19, #0x60
// 0x10c9248: cbz w8, #0x10c936c
// 0x10c924c: adrp x24, #0x1fab000
// 0x10c9250: ldrb w8, [x24, #0x2c9]
// 0x10c9254: cbnz w8, #0x10c926c
// 0x10c9258: adrp x0, #0x1e8c000
// 0x10c925c: ldr x0, [x0, #0x1e8]
// 0x10c9260: bl #0xf7d92c
// 0x10c9264: mov w8, #1
// 0x10c9268: strb w8, [x24, #0x2c9]
// 0x10c926c: ldr x0, [x19, #0x28]
// 0x10c9270: cbz x0, #0x10c96fc
// 0x10c9274: adrp x25, #0x1e8c000
// 0x10c9278: ldr x25, [x25, #0x1e8]
// 0x10c927c: mov x1, xzr
// 0x10c9280: ldr x8, [x25]
// 0x10c9284: ldr x8, [x8, #0xb8]
// 0x10c9288: ldr s0, [x8, #8]
// 0x10c928c: str s0, [sp, #0x2c]
// 0x10c9290: bl #0x1b9d508
// 0x10c9294: mov x0, x19
// 0x10c9298: mov v10.16b, v0.16b
// 0x10c929c: mov v11.16b, v1.16b
// 0x10c92a0: mov v12.16b, v2.16b
// 0x10c92a4: bl #0x10c97dc
// 0x10c92a8: cbz x0, #0x10c96fc
// 0x10c92ac: bl #0x10c7830
// 0x10c92b0: ldr x8, [x23]
// 0x10c92b4: ldr x8, [x8, #0xb8]
// 0x10c92b8: ldr x0, [x8, #8]
// 0x10c92bc: cbz x0, #0x10c96fc
// 0x10c92c0: mov x1, xzr
// 0x10c92c4: mov v13.16b, v0.16b
// 0x10c92c8: mov v14.16b, v1.16b
// 0x10c92cc: mov v15.16b, v2.16b
// 0x10c92d0: bl #0x1b92154
// 0x10c92d4: cbz x0, #0x10c96fc
// 0x10c92d8: fsub s0, s10, s13
// 0x10c92dc: fsub s1, s11, s14
// 0x10c92e0: fsub s2, s12, s15
// 0x10c92e4: mov x1, xzr
// 0x10c92e8: bl #0x1b9e7c8
// 0x10c92ec: adrp x23, #0x1fab000
// 0x10c92f0: ldrb w8, [x23, #0x2c8]
// 0x10c92f4: cbnz w8, #0x10c9314
// 0x10c92f8: adrp x0, #0x1e8c000
// 0x10c92fc: ldr x0, [x0, #0xa60]
// 0x10c9300: stp q1, q0, [sp]
// 0x10c9304: bl #0xf7d92c
// 0x10c9308: ldp q1, q0, [sp]
// 0x10c930c: mov w8, #1
// 0x10c9310: strb w8, [x23, #0x2c8]
// 0x10c9314: adrp x8, #0x1e8c000
// 0x10c9318: ldr x8, [x8, #0xa60]
// 0x10c931c: ldr x0, [x8]
// 0x10c9320: ldr w8, [x0, #0xe0]
// 0x10c9324: cbnz w8, #0x10c9334
// 0x10c9328: stp q1, q0, [sp]
// 0x10c932c: bl #0xf7da5c
// 0x10c9330: ldp q1, q0, [sp]
// 0x10c9334: adrp x8, #0x832000
// 0x10c9338: fmul s2, s0, s0
// 0x10c933c: fmul s3, s1, s1
// 0x10c9340: ldr s4, [x8, #0x41c]
// 0x10c9344: fadd s3, s2, s3
// 0x10c9348: fmov s2, wzr
// 0x10c934c: fadd s2, s3, s2
// 0x10c9350: fsqrt s2, s2
// 0x10c9354: fcmp s2, s4
// 0x10c9358: b.le #0x10c9424
// 0x10c935c: mov v0.s[1], v1.s[0]
// 0x10c9360: dup v1.2s, v2.s[0]
// 0x10c9364: fdiv v10.2s, v0.2s, v1.2s
// 0x10c9368: b #0x10c944c
// 0x10c936c: ldr x0, [x19, #0xa8]
// 0x10c9370: cbz x0, #0x10c96fc
// 0x10c9374: ldr s10, [x19, #0xc0]
// 0x10c9378: mov x1, xzr
// 0x10c937c: bl #0x1b9c8ac
// 0x10c9380: ldr s1, [x19, #0x8c]
// 0x10c9384: fmov s2, #0.50000000
// 0x10c9388: fmul s0, s0, s2
// 0x10c938c: fsub s0, s0, s1
// 0x10c9390: fcmp s10, s0
// 0x10c9394: b.eq #0x10c94d0
// 0x10c9398: ldr x0, [x19, #0xa8]
// 0x10c939c: cbz x0, #0x10c96fc
// 0x10c93a0: ldr s10, [x19, #0xc4]
// 0x10c93a4: mov x1, xzr
// 0x10c93a8: bl #0x1b9c8ac
// 0x10c93ac: ldr s0, [x19, #0x8c]
// 0x10c93b0: fmov s2, #0.50000000
// 0x10c93b4: fmul s1, s1, s2
// 0x10c93b8: fsub s0, s1, s0
// 0x10c93bc: fcmp s10, s0
// 0x10c93c0: b.eq #0x10c94d0
// 0x10c93c4: ldr x0, [x19, #0xa8]
// 0x10c93c8: cbz x0, #0x10c96fc
// 0x10c93cc: ldr s10, [x19, #0xc0]
// 0x10c93d0: mov x1, xzr
// 0x10c93d4: bl #0x1b9c8ac
// 0x10c93d8: ldr s1, [x19, #0x8c]
// 0x10c93dc: fmov s2, #-0.50000000
// 0x10c93e0: fmul s0, s0, s2
// 0x10c93e4: fsub s0, s0, s1
// 0x10c93e8: fcmp s10, s0
// 0x10c93ec: b.eq #0x10c94d0
// 0x10c93f0: ldr x0, [x19, #0xa8]
// 0x10c93f4: cbz x0, #0x10c96fc
// 0x10c93f8: ldr s10, [x19, #0xc4]
// 0x10c93fc: mov x1, xzr
// 0x10c9400: bl #0x1b9c8ac
// 0x10c9404: ldr s0, [x19, #0x8c]
// 0x10c9408: fmov s3, #0.50000000
// 0x10c940c: fmul s1, s1, s3
// 0x10c9410: fneg s2, s10
// 0x10c9414: fsub s0, s1, s0
// 0x10c9418: fcmp s0, s2
// 0x10c941c: b.eq #0x10c94d0
// 0x10c9420: b #0x10c94d4
// 0x10c9424: ldrb w8, [x24, #0x2c9]
// 0x10c9428: cbnz w8, #0x10c9440
// 0x10c942c: adrp x0, #0x1e8c000
// 0x10c9430: ldr x0, [x0, #0x1e8]
// 0x10c9434: bl #0xf7d92c
// 0x10c9438: mov w8, #1
// 0x10c943c: strb w8, [x24, #0x2c9]
// 0x10c9440: ldr x8, [x25]
// 0x10c9444: ldr x8, [x8, #0xb8]
// 0x10c9448: ldr d10, [x8]
// 0x10c944c: ldr s11, [x19, #0xc0]
// 0x10c9450: mov x0, x19
// 0x10c9454: bl #0x10c97dc
// 0x10c9458: cbz x0, #0x10c96fc
// 0x10c945c: ldr s0, [x0, #0x70]
// 0x10c9460: movi v1.2s, #0x3f, lsl #24
// 0x10c9464: fmul v3.2s, v10.2s, v1.2s
// 0x10c9468: fmov s1, #0.50000000
// 0x10c946c: fmul s0, s0, v3.s[0]
// 0x10c9470: fadd s0, s0, s1
// 0x10c9474: fabs s2, s11
// 0x10c9478: fabs s0, s0
// 0x10c947c: fcmp s2, s0
// 0x10c9480: b.lt #0x10c94d4
// 0x10c9484: mov x0, x19
// 0x10c9488: str q3, [sp, #0x10]
// 0x10c948c: bl #0x10c97dc
// 0x10c9490: cbz x0, #0x10c96fc
// 0x10c9494: ldr s0, [x0, #0x70]
// 0x10c9498: mov x0, x19
// 0x10c949c: str q0, [sp]
// 0x10c94a0: bl #0x10c97dc
// 0x10c94a4: cbz x0, #0x10c96fc
// 0x10c94a8: ldr q2, [sp]
// 0x10c94ac: ldr s1, [sp, #0x2c]
// 0x10c94b0: add x8, x0, #0x70
// 0x10c94b4: movi v0.2s, #0x3f, lsl #24
// 0x10c94b8: ld1 {v2.s}[1], [x8]
// 0x10c94bc: str s1, [x19, #0xc8]
// 0x10c94c0: ldr q1, [sp, #0x10]
// 0x10c94c4: fmul v1.2s, v1.2s, v2.2s
// 0x10c94c8: fadd v0.2s, v1.2s, v0.2s
// 0x10c94cc: str d0, [x19, #0xc0]
// 0x10c94d0: add x22, x19, #0x90
// 0x10c94d4: cbz x20, #0x10c96fc
// 0x10c94d8: ldp s0, s1, [x19, #0xc0]
// 0x10c94dc: ldr s10, [x22]
// 0x10c94e0: mov x0, x20
// 0x10c94e4: mov x1, xzr
// 0x10c94e8: bl #0x1b9c820
// 0x10c94ec: ldr x0, [x21]
// 0x10c94f0: ldr x21, [x19, #0xb8]
// 0x10c94f4: ldr w8, [x0, #0xe0]
// 0x10c94f8: cbnz w8, #0x10c9500
// 0x10c94fc: bl #0xf7da5c
// 0x10c9500: mov x0, x21
// 0x10c9504: mov x1, xzr
// 0x10c9508: mov x2, xzr
// 0x10c950c: bl #0x1b94ac8
// 0x10c9510: tbz w0, #0, #0x10c952c
// 0x10c9514: ldr x0, [x19, #0xb8]
// 0x10c9518: cbz x0, #0x10c96fc
// 0x10c951c: mov v0.16b, v9.16b
// 0x10c9520: mov v1.16b, v8.16b
// 0x10c9524: mov x1, xzr
// 0x10c9528: bl #0x1b9c820
// 0x10c952c: ldr x8, [x19, #0xd0]
// 0x10c9530: cbz x8, #0x10c96fc
// 0x10c9534: ldr s0, [x8, #0x4c]
// 0x10c9538: mov x0, x20
// 0x10c953c: mov x1, xzr
// 0x10c9540: fmul s10, s10, s0
// 0x10c9544: bl #0x1b9c8ac
// 0x10c9548: mov x0, xzr
// 0x10c954c: mov v8.16b, v0.16b
// 0x10c9550: mov v9.16b, v1.16b
// 0x10c9554: bl #0x1b89b60
// 0x10c9558: fmov s1, #8.00000000
// 0x10c955c: fmov s2, #1.00000000
// 0x10c9560: fmul s0, s0, s1
// 0x10c9564: fmov s3, wzr
// 0x10c9568: fmin s1, s0, s2
// 0x10c956c: fcmp s0, #0.0
// 0x10c9570: fsub s4, s10, s8
// 0x10c9574: fsub s5, s10, s9
// 0x10c9578: fcsel s0, s1, s3, pl
// 0x10c957c: fmul s1, s4, s0
// 0x10c9580: fmul s2, s5, s0
// 0x10c9584: fadd s0, s8, s1
// 0x10c9588: fadd s1, s9, s2
// 0x10c958c: mov x0, x20
// 0x10c9590: mov x1, xzr
// 0x10c9594: bl #0x1b9c93c
// 0x10c9598: ldr x0, [x19, #0xd0]
// 0x10c959c: cbz x0, #0x10c96fc
// 0x10c95a0: ldrb w8, [x0, #0x74]
// 0x10c95a4: cbz w8, #0x10c962c
// 0x10c95a8: adrp x21, #0x1fab000
// 0x10c95ac: ldrb w8, [x21, #0x2cb]
// 0x10c95b0: cbnz w8, #0x10c95c8
// 0x10c95b4: adrp x0, #0x1e8c000
// 0x10c95b8: ldr x0, [x0, #0xd88]
// 0x10c95bc: bl #0xf7d92c
// 0x10c95c0: mov w8, #1
// 0x10c95c4: strb w8, [x21, #0x2cb]
// 0x10c95c8: ldr x0, [x19, #0x28]
// 0x10c95cc: cbz x0, #0x10c96fc
// 0x10c95d0: adrp x8, #0x1e8c000
// 0x10c95d4: ldr x8, [x8, #0xd88]
// 0x10c95d8: mov x1, xzr
// 0x10c95dc: ldr x8, [x8]
// 0x10c95e0: ldr x8, [x8, #0xb8]
// 0x10c95e4: ldp s9, s8, [x8, #8]
// 0x10c95e8: ldr s10, [x8, #4]
// 0x10c95ec: bl #0x1b9d6f0
// 0x10c95f0: mov x0, x20
// 0x10c95f4: mov v1.16b, v10.16b
// 0x10c95f8: mov v2.16b, v9.16b
// 0x10c95fc: mov v3.16b, v8.16b
// 0x10c9600: ldp x20, x19, [sp, #0xa0]
// 0x10c9604: ldp x22, x21, [sp, #0x90]
// 0x10c9608: ldp x24, x23, [sp, #0x80]
// 0x10c960c: ldp x30, x25, [sp, #0x70]
// 0x10c9610: ldp d9, d8, [sp, #0x60]
// 0x10c9614: ldp d11, d10, [sp, #0x50]
// 0x10c9618: ldp d13, d12, [sp, #0x40]
// 0x10c961c: ldp d15, d14, [sp, #0x30]
// 0x10c9620: mov x1, xzr
// 0x10c9624: add sp, sp, #0xb0
// 0x10c9628: b #0x1b9d874
// 0x10c962c: mov x1, xzr
// 0x10c9630: bl #0x1b92154
// 0x10c9634: cbz x0, #0x10c96fc
// 0x10c9638: mov x1, xzr
// 0x10c963c: bl #0x1b9d6c8
// 0x10c9640: adrp x21, #0x1fab000
// 0x10c9644: ldrb w8, [x21, #0x2c9]
// 0x10c9648: mov v8.16b, v1.16b
// 0x10c964c: cbnz w8, #0x10c9664
// 0x10c9650: adrp x0, #0x1e8c000
// 0x10c9654: ldr x0, [x0, #0x1e8]
// 0x10c9658: bl #0xf7d92c
// 0x10c965c: mov w8, #1
// 0x10c9660: strb w8, [x21, #0x2c9]
// 0x10c9664: ldr x0, [x19, #0x28]
// 0x10c9668: cbz x0, #0x10c96fc
// 0x10c966c: adrp x8, #0x1e8c000
// 0x10c9670: ldr x8, [x8, #0x1e8]
// 0x10c9674: mov x1, xzr
// 0x10c9678: ldr x8, [x8]
// 0x10c967c: ldr x8, [x8, #0xb8]
// 0x10c9680: ldp s10, s9, [x8]
// 0x10c9684: bl #0x1b9d6f0
// 0x10c9688: mov x0, xzr
// 0x10c968c: bl #0x1b8b1c4
// 0x10c9690: adrp x8, #0x832000
// 0x10c9694: ldr s3, [x8, #0x554]
// 0x10c9698: mov x0, xzr
// 0x10c969c: fmul s0, s0, s3
// 0x10c96a0: fmul s1, s1, s3
// 0x10c96a4: fmul s2, s2, s3
// 0x10c96a8: bl #0x1b8b63c
// 0x10c96ac: adrp x8, #0x832000
// 0x10c96b0: ldr s2, [x8, #0x3e4]
// 0x10c96b4: fsub s3, s8, s1
// 0x10c96b8: mov x0, xzr
// 0x10c96bc: fmul s0, s10, s2
// 0x10c96c0: fmul s1, s9, s2
// 0x10c96c4: fmul s2, s3, s2
// 0x10c96c8: bl #0x1b8b12c
// 0x10c96cc: mov x0, x20
// 0x10c96d0: ldp x20, x19, [sp, #0xa0]
// 0x10c96d4: ldp x22, x21, [sp, #0x90]
// 0x10c96d8: ldp x24, x23, [sp, #0x80]
// 0x10c96dc: ldp x30, x25, [sp, #0x70]
// 0x10c96e0: ldp d9, d8, [sp, #0x60]
// 0x10c96e4: ldp d11, d10, [sp, #0x50]
// 0x10c96e8: ldp d13, d12, [sp, #0x40]
// 0x10c96ec: ldp d15, d14, [sp, #0x30]
// 0x10c96f0: mov x1, xzr
// 0x10c96f4: add sp, sp, #0xb0
// 0x10c96f8: b #0x1b9d774
// 0x10c96fc: bl #0xf7db74
```

## `bl_MiniMapItem.get_TargetPosition` — RVA `0xcc9700`

- Decompiled symbol: `bl_MiniMapItem_get_TargetPosition`
- Metadata signature: `public Vector3 get_TargetPosition() { }`
- Native interval: `220` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[40];
    unsigned long long field_28;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern long long g_1ef22e8;
extern char g_1fab2c9;
extern char g_1fab56b;

long long bl_MiniMapItem_get_TargetPosition(struct_1 *ptr)
{
    long long v0;  // x0
    unsigned long long v1;  // x0
    unsigned long long v2;  // x0

    if (!(g_1fab56b & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab56b = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v0 = Object__op_Equality(ptr->field_28, 0, 0);
    if (((char)v0 & 1))
    {
        if (!g_1fab2c9)
        {
            v0 = sub_f7d92c(&g_1ef22e8);
            g_1fab2c9 = 1;
        }
        return v0;
    }
    v1 = ptr->field_28;
    if (v1)
    {
        Transform__get_position(v1, 0);
        v1 = ptr->field_28;
        if (v1)
        {
            v2 = Transform__get_position(v1, 0);
            return Transform__get_position(v1, 0);
        }
    }
    sub_f7db74(v1);
}
```

## `bl_MiniMapItem.get_m_miniMap` — RVA `0xcc97dc`

- Decompiled symbol: `bl_MiniMapItem_get_m_miniMap`
- Metadata signature: `private bl_MiniMap get_m_miniMap() { }`
- Native interval: `200` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern long long g_1efd160;
extern char g_1fab56c;

long long bl_MiniMapItem_get_m_miniMap(long long *p)
{
    long long ptr[28];  // x19
    long long v1;  // x0
    long long v2;  // x0

    if (!(g_1fab56c & 1))
    {
        sub_f7d92c(&g_1efd160);
        sub_f7d92c(&g_1ef0c58);
        g_1fab56c = 1;
    }
    ptr = p + 27;
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (((char)Object__op_Equality(p[27], 0, 0) & 1))
    {
        v1 = p[22];
        if (!v1 || !((v1 = (long long)(unsigned long long)GameObject__get_transform(v1, 0), v1 && (v1 = (long long)(unsigned long long)Transform__get_root(), v1))))
            sub_f7db74(v1);
        v2 = sub_1231e2c();
        ptr[0] = v2;
        sub_f7d8d0(ptr, v2);
    }
    return ptr[0];
}
```

## `bl_MiniMapItem.DestroyItem` — RVA `0xcc98a4`

- Decompiled symbol: `bl_MiniMapItem_DestroyItem`
- Metadata signature: `public void DestroyItem(bool inmediate) { }`
- Native interval: `384` bytes
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
extern long long g_1efd0e0;
extern long long g_1f067d0;
extern long long g_1f0a7c0;
extern char g_1fab565;

void bl_MiniMapItem_DestroyItem(long long *a0, unsigned int a1)
{
    long long v0;  // x0
    unsigned int v1;  // w0
    unsigned long v2;  // x0

    if (!(g_1fab565 & 1))
    {
        sub_f7d92c(&g_1efd0e0);
        sub_f7d92c(&g_1eef458);
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c(&g_1f067d0);
        sub_f7d92c(&g_1f0a7c0);
        g_1fab565 = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (((char)Object__op_Equality(a0[20], 0, 0) & 1))
    {
        v0 = Object__get_name(a0, 0);
        String__Concat(g_1f0a7c0, v0, g_1f067d0, 0);
        if (g_1eef458->field_e0)
        {
            Debug__Log();
            return;
        }
        sub_f7da5c(g_1eef458);
        Debug__Log();
        return;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v1 = Object__op_Equality(a0[9], 0, 0);
    if (a0[20])
    {
        v2 = sub_1231bc8(a0[20], g_1efd0e0);
        if ((((char)v1 | (char)a1) & 1))
        {
            if (v2)
            {
                bl_IconItem__DestroyIcon(v2, a1 & 1, 0);
                return;
            }
        }
        else
        {
            if (v2)
            {
                bl_IconItem__DestroyIcon(v2, 0, a0[9]);
                return;
            }
        }
    }
    sub_f7db74();
}
```

## `bl_MiniMapItem.SetIcon` — RVA `0xcc9a24`

- Decompiled symbol: `bl_MiniMapItem_SetIcon`
- Metadata signature: `public void SetIcon(Sprite ico) { }`
- Native interval: `256` bytes
- Result: `pseudocode`

```c
typedef struct struct_3 {
    char padding_0[176];
    struct struct_2 *field_b0;
} struct_3;

typedef struct struct_2 {
    char padding_0[40];
    struct struct_2 *field_28;
} struct_2;

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
extern long long g_1efed38;
extern long long g_1f0fe30;
extern char g_1fab566;

void bl_MiniMapItem_SetIcon(struct_3 *ptr, unsigned long a1)
{
    unsigned long long v5;  // x30
    unsigned long long v6;  // x22
    unsigned long long v7;  // x21
    unsigned long long v8;  // x20
    unsigned long long v9;  // x19
    struct_2 *cur;  // x0
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
    if (!(g_1fab566 & 1))
    {
        sub_f7d92c(&g_1eef458);
        sub_f7d92c(&g_1efed38);
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c(&g_1f0fe30);
        g_1fab566 = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (((char)Object__op_Equality(ptr->field_b0, 0, 0) & 1))
    {
        if (!g_1eef458->field_e0)
            sub_f7da5c(g_1eef458);
        Debug__LogWarning();
        return;
    }
    cur = ptr->field_b0;
    if (cur)
    {
        cur = sub_1249224(cur, g_1efed38);
        if (cur)
        {
            cur = cur->field_28;
            if (cur)
            {
                Image__set_sprite();
                return;
            }
        }
    }
    sub_f7db74(cur);
}
```

## `bl_MiniMapItem.SetCircleArea` — RVA `0xcc9b24`

- Decompiled symbol: `bl_MiniMapItem_SetCircleArea`
- Metadata signature: `public void SetCircleArea(float radius, Color AreaColor) { }`
- Native interval: `168` bytes
- Result: `pseudocode`

```c
extern long long g_1efed38;
extern char g_1fab567;

void bl_MiniMapItem_SetCircleArea(void* ptr)
{
    unsigned long long v8;  // d12
    unsigned long long v9;  // d11
    unsigned long long v10;  // d10
    unsigned long long v11;  // d9
    unsigned long long v12;  // d8
    unsigned long long v13;  // x30
    unsigned long long v14;  // x20
    unsigned long long v15;  // x19
    unsigned long v16;  // x0
    unsigned long long v0;  // [bp-0x40]
    unsigned long long v1;  // [bp-0x38]
    unsigned long long v2;  // [bp-0x30]
    unsigned long long v3;  // [bp-0x28]
    unsigned long long v4;  // [bp-0x20]
    unsigned long long v5;  // [bp-0x18]
    unsigned long long v6;  // [bp-0x10]
    unsigned long long v7;  // [bp-0x8]

    v0 = v8;
    v1 = v9;
    v2 = v10;
    v3 = v11;
    v4 = v12;
    v5 = v13;
    v6 = v14;
    v7 = v15;
    if (!(g_1fab567 & 1))
    {
        sub_f7d92c(&g_1efed38);
        g_1fab567 = 1;
    }
    v16 = (long long)ptr[176];
    if (v16)
    {
        v16 = sub_1249224(v16, g_1efed38);
        if (v16)
        {
            *((unsigned long long *)&ptr[184]) = bl_IconItem__SetCircleArea(v16);
            sub_f7d8d0();
            return;
        }
    }
    sub_f7db74(v16);
}
```

## `bl_MiniMapItem.HideCircleArea` — RVA `0xcc9bcc`

- Decompiled symbol: `bl_MiniMapItem_HideCircleArea`
- Metadata signature: `public void HideCircleArea() { }`
- Native interval: `104` bytes
- Result: `pseudocode`

```c
extern long long g_1efed38;
extern char g_1fab568;

void bl_MiniMapItem_HideCircleArea(void* ptr)
{
    unsigned long long v3;  // x30
    unsigned long long v4;  // x20
    unsigned long long v5;  // x19
    unsigned long v6;  // x0
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x10]
    unsigned long long v2;  // [bp-0x8]

    v0 = v3;
    v1 = v4;
    v2 = v5;
    if (!(g_1fab568 & 1))
    {
        sub_f7d92c(&g_1efed38);
        g_1fab568 = 1;
    }
    v6 = (long long)ptr[176];
    if (v6)
    {
        v6 = sub_1249224(v6, g_1efed38);
        if (v6)
            bl_IconItem__HideCircleArea(v6); /* do not return */
    }
    sub_f7db74(v6);
}
```

## `bl_MiniMapItem.HideItem` — RVA `0xcc9c34`

- Decompiled symbol: `bl_MiniMapItem_HideItem`
- Metadata signature: `public void HideItem() { }`
- Native interval: `200` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    char padding_0[176];
    long long field_b0;
} struct_2;

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
extern char g_1fab569;

void bl_MiniMapItem_HideItem(struct_2 *a0)
{
    unsigned long long v4;  // x30
    unsigned long long v5;  // x21
    unsigned long long v6;  // x20
    unsigned long long v7;  // x19
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x18]
    unsigned long long v2;  // [bp-0x10]
    unsigned long long v3;  // [bp-0x8]

    v0 = v4;
    v1 = v5;
    v2 = v6;
    v3 = v7;
    if (!(g_1fab569 & 1))
    {
        sub_f7d92c(&g_1eef458);
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c("e\"");
        g_1fab569 = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (((char)Object__op_Inequality(a0->field_b0, 0, 0) & 1))
    {
        if (a0->field_b0)
        {
            GameObject__SetActive();
            return;
        }
        sub_f7db74(0);
    }
    else
    {
        if (!g_1eef458->field_e0)
            sub_f7da5c(g_1eef458);
        Debug__Log();
        return;
    }
}
```

## `bl_MiniMapItem.ShowItem` — RVA `0xcc9cfc`

- Decompiled symbol: `bl_MiniMapItem_ShowItem`
- Metadata signature: `public void ShowItem() { }`
- Native interval: `200` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    char padding_0[176];
    long long field_b0;
} struct_2;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

typedef struct struct_1 {
    char padding_0[224];
    unsigned int field_e0;
} struct_1;

extern struct_0 *g_1eef458;
extern struct_1 *g_1ef0c58;
extern char g_1fab56a;

void bl_MiniMapItem_ShowItem(struct_2 *a0)
{
    unsigned long long v4;  // x30
    unsigned long long v5;  // x21
    unsigned long long v6;  // x20
    unsigned long long v7;  // x19
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x18]
    unsigned long long v2;  // [bp-0x10]
    unsigned long long v3;  // [bp-0x8]

    v0 = v4;
    v1 = v5;
    v2 = v6;
    v3 = v7;
    if (!(g_1fab56a & 1))
    {
        sub_f7d92c(&g_1eef458);
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c("c\"");
        g_1fab56a = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (((char)Object__op_Inequality(a0->field_b0, 0, 0) & 1))
    {
        if (a0->field_b0)
        {
            GameObject__SetActive();
            return;
        }
        sub_f7db74(0);
    }
    else
    {
        if (!g_1eef458->field_e0)
            sub_f7da5c(g_1eef458);
        Debug__Log();
        return;
    }
}
```

## `bl_MiniMapItem.ctor` — RVA `0xcc9dc4`

- Decompiled symbol: `bl_MiniMapItem_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `236` bytes
- Result: `pseudocode`
- Heuristic layout hint: `bl_MiniMapItem_Recovered` matched 9 offsets against `bl_MiniMapItem` metadata (confidence 0.82).

```c
typedef struct bl_MiniMapItem_Recovered {
    char padding_0[48];
    unsigned long long OffSet;
    unsigned int field_38;
    char padding_3c[20];
    uint128_t IconColor;
    unsigned int Size;
    char padding_64[4];
    uint128_t CircleAreaRadius;
    unsigned int field_78;
    char isInteractable;
    char padding_7d[3];
    long long InfoItem;
    char OffScreen;
    char padding_89[3];
    unsigned long long BorderOffScreen;
    unsigned long long RenderDelay;
} bl_MiniMapItem_Recovered;

typedef struct struct_0 {
    unsigned long long field_0;
    unsigned int field_8;
} struct_0;

typedef struct struct_1 {
    char padding_0[184];
    struct struct_0 *field_b8;
} struct_1;

extern struct_1 *g_1ef22e8;
extern long long g_1f0afd8;
extern char g_1fab2c9;
extern char g_1fab56d;

void bl_MiniMapItem_ctor(struct_2 *ptr)
{
    unsigned long long v4;  // x30
    unsigned long long v5;  // x21
    unsigned long long v6;  // x20
    unsigned long long v7;  // x19
    unsigned long long v8;  // d2
    unsigned int v9;  // s3
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x18]
    unsigned long long v2;  // [bp-0x10]
    unsigned long long v3;  // [bp-0x8]

    v0 = v4;
    v1 = v5;
    v2 = v6;
    v3 = v7;
    if (!(g_1fab56d & 1))
    {
        sub_f7d92c(&g_1f0afd8);
        g_1fab56d = 1;
    }
    if (!g_1fab2c9)
    {
        sub_f7d92c(&g_1ef22e8);
        g_1fab2c9 = 1;
    }
    v8 = g_1ef22e8->field_b8->field_0;
    v9 = g_1ef22e8->field_b8->field_8;
    ptr->field_50 = 0x3f6666663f8000003f8000003f800000;
    *((uint128_t *)&(&ptr->padding_64)[1]) = 0x3f8000003f8000003f80000041200000;
    ptr->field_60 = 0x42200000;
    *((unsigned int *)((char *)&ptr->field_68 + 8)) = 1063675494;
    ptr->field_30 = v8;
    ptr->field_38 = v9;
    *((char *)&ptr->field_68 + 12) = 1;
    *((long long *)&ptr->field_78) = g_1f0afd8;
    sub_f7d8d0((struct bl_MiniMapItem_Recovered *)&ptr->field_78, g_1f0afd8);
    *((char *)&ptr->field_80) = 1;
    *((unsigned long long *)((char *)&ptr->field_80 + 4)) = 4692750812729038602;
    *((unsigned long long *)&(&ptr->padding_89)[1]) = 9640188314;
    MonoBehaviour__ctor();
    return;
}
```
