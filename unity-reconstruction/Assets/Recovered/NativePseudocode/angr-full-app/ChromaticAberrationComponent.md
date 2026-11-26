# Native pseudocode: ChromaticAberrationComponent

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `ChromaticAberrationComponent.get_active` — RVA `0xcd0664`

- Decompiled symbol: `ChromaticAberrationComponent_get_active`
- Metadata signature: `public override bool get_active() { }`
- Native interval: `116` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    char padding_0[16];
    struct struct_0 *field_10;
    struct struct_1 *field_18;
} struct_2;

typedef struct struct_1 {
    char padding_0[16];
    char field_10;
    char padding_11[15];
    unsigned int field_20;
} struct_1;

typedef struct struct_0 {
    char padding_0[48];
    char field_30;
} struct_0;

extern long long g_1efa0d8;
extern char g_1fab5b2;

unsigned long long ChromaticAberrationComponent_get_active(struct_2 *ptr)
{
    struct_1 *p;  // x8
    unsigned int v1;  // s0
    unsigned long v2;  // 4129
    unsigned long long v3;  // x0

    if (!(g_1fab5b2 & 1))
    {
        sub_f7d92c(&g_1efa0d8);
        g_1fab5b2 = 1;
    }
    p = ptr->field_18;
    if (p)
    {
        if (!(p->field_10 && (v1 = p->field_20, v2 = (unsigned long)arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v1, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v1, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v1, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v1, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v1, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v1, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0), !((char)v2))))
        {
            return 0;
        }
        else if (ptr->field_10)
        {
            if (ptr->field_10->field_30)
                v3 = 0;
            else
                v3 = 1;
            return v3;
        }
    }
    sub_f7db74();
}
```

## `ChromaticAberrationComponent.OnDisable` — RVA `0xcd06d8`

- Decompiled symbol: `ChromaticAberrationComponent_OnDisable`
- Metadata signature: `public override void OnDisable() { }`
- Native interval: `40` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[32];
    long long field_20;
} struct_0;

void ChromaticAberrationComponent_OnDisable(struct_0 *ptr)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    GraphicsUtils__Destroy(ptr->field_20, 0);
    ptr->field_20 = 0;
    sub_f7d8d0();
    return;
}
```

## `ChromaticAberrationComponent.Prepare` — RVA `0xcd0700`

- Decompiled symbol: `ChromaticAberrationComponent_Prepare`
- Metadata signature: `public override void Prepare(Material uberMaterial) { }`
- Native interval: `636` bytes
- Result: `pseudocode`

```c
typedef struct struct_4 {
    char padding_0[24];
    struct struct_3 *field_18;
    long long field_20;
} struct_4;

typedef struct struct_3 {
    char padding_0[24];
    long long field_18;
} struct_3;

typedef struct struct_5 {
    char padding_0[24];
    unsigned int field_18;
    char padding_1c[4];
    uint128_t field_20;
    uint128_t field_30;
    uint128_t field_40;
} struct_5;

typedef struct struct_1 {
    char padding_0[184];
    struct struct_2 *field_b8;
    char padding_c0[32];
    unsigned int field_e0;
} struct_1;

typedef struct struct_2 {
    unsigned int field_0;
} struct_2;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern long long g_1eee028;
extern struct_0 *g_1ef0c58;
extern long long g_1ef1cc0;
extern struct_1 *g_1ef2db8;
extern long long g_1efa0d8;
extern long long g_1f08c40;
extern long long g_1f09328;
extern char g_1fab5b3;

void ChromaticAberrationComponent_Prepare(struct_4 *a0, long long a1)
{
    unsigned long long v6;  // x30
    unsigned long long v7;  // x23
    struct_5 *ptr;  // x1
    struct_1 *v17;  // x0
    unsigned long long v8;  // x22
    unsigned long long v9;  // x21
    unsigned long long v10;  // x20
    unsigned long long v11;  // x19
    struct_4 *p;  // x20
    long long v13;  // x21
    struct_5 *addr;  // x0
    unsigned int flag;  // w8
    unsigned long long v0;  // [bp-0x30]
    unsigned long long v1;  // [bp-0x28]
    unsigned long long v2;  // [bp-0x20]
    unsigned long long v3;  // [bp-0x18]
    unsigned long long v4;  // [bp-0x10]
    unsigned long long v5;  // [bp-0x8]

    v0 = v6;
    v1 = v7;
    v2 = v8;
    v3 = v9;
    v4 = v10;
    v5 = v11;
    if (!(g_1fab5b3 & 1))
    {
        sub_f7d92c(&g_1eee028);
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c(&g_1efa0d8);
        sub_f7d92c(&g_1ef1cc0);
        sub_f7d92c(&g_1ef2db8);
        sub_f7d92c(&g_1f08c40);
        sub_f7d92c(&g_1f09328);
        g_1fab5b3 = 1;
    }
    if (a0->field_18)
    {
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        if (((char)Object__op_Equality(a0->field_18->field_18, 0, 0) & 1))
        {
            p = &a0->field_20;
            if (!g_1ef0c58->field_e0)
                sub_f7da5c(g_1ef0c58);
            if (((char)Object__op_Equality(a0->field_20, 0, 0) & 1))
            {
                v13 = sub_f7db70(g_1ef1cc0);
                Texture2D__ctor(v13, 3, 1, 3, 0, 0);
                if (v13)
                {
                    Object__set_name(v13, g_1f09328, 0);
                    Texture__set_filterMode(v13, 1, 0);
                    Texture__set_wrapMode(v13, 1, 0);
                    Texture__set_anisoLevel(v13, 0, 0);
                    Object__set_hideFlags(v13, 52, 0);
                    *((long long *)&p->padding_0[0]) = v13;
                    sub_f7d8d0(p, v13);
                    addr = sub_f7d9d4(g_1eee028, 3);
                    if (addr)
                    {
                        flag = addr->field_18;
                        ptr = addr;
                        if (!flag || !((ptr->field_20 = 0x3f80000000000000000000003f800000, flag != 1 && (ptr->field_30 = 0x3f800000000000003f80000000000000, flag > 2))))
                            goto LABEL_10d0978;
                        ptr->field_40 = 0x3f8000003f8000000000000000000000;
                        if (*((long long *)&p->padding_0[0]) && !((Texture2D__SetPixels(*((long long *)&p->padding_0[0])), !*((long long *)&p->padding_0[0]))))
                        {
                            Texture2D__Apply(*((long long *)&p->padding_0[0]), 0);
                            goto LABEL_10d08ec;
                        }
                    }
                }
            }
            else
            {
LABEL_10d08ec:
                goto LABEL_10d08f0;
            }
        }
        else
        {
LABEL_10d08f0:
            if (a1)
            {
                Material__EnableKeyword(a1, g_1f08c40, 0);
                v17 = g_1ef2db8;
                if (!g_1ef2db8->field_e0)
                {
                    sub_f7da5c(g_1ef2db8);
                    v17 = g_1ef2db8;
                }
                Material__SetFloat(a1, v17->field_b8->field_0, 0);
                Material__SetTexture();
                return;
            }
        }
    }
    addr = sub_f7db74();
LABEL_10d0978:
    sub_f7db7c(addr);
}
```

## `ChromaticAberrationComponent.ctor` — RVA `0xcd097c`

- Decompiled symbol: `ChromaticAberrationComponent_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `72` bytes
- Result: `pseudocode`

```c
extern long long g_1efa078;
extern char g_1fab5b4;

void ChromaticAberrationComponent_ctor(unsigned long a0)
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
    if (!(g_1fab5b4 & 1))
    {
        sub_f7d92c(&g_1efa078);
        g_1fab5b4 = 1;
    }
}
```
