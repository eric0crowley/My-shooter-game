# Native pseudocode: BloomComponent

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `BloomComponent.get_active` — RVA `0xcce830`

- Decompiled symbol: `BloomComponent_get_active`
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
    char padding_11[7];
    unsigned int field_18;
} struct_1;

typedef struct struct_0 {
    char padding_0[48];
    char field_30;
} struct_0;

extern long long g_1efa0c8;
extern char g_1fab5a2;

unsigned long long BloomComponent_get_active(struct_2 *ptr, unsigned long a1, unsigned long a2, unsigned long a3)
{
    struct_1 *p;  // x8
    unsigned int v1;  // s0
    unsigned long v2;  // 4129
    unsigned long long v3;  // x0

    if (!(g_1fab5a2 & 1))
    {
        sub_f7d92c(&g_1efa0c8);
        g_1fab5a2 = 1;
    }
    p = ptr->field_18;
    if (p)
    {
        if (!(p->field_10 && (v1 = p->field_18, v2 = (unsigned long)arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v1, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v1, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v1, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v1, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v1, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v1, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0), !((char)v2))))
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

## `BloomComponent.Prepare` — RVA `0xcce8a4`

- Decompiled symbol: `BloomComponent_Prepare`
- Metadata signature: `public void Prepare(RenderTexture source, Material uberMaterial, Texture autoExposure) { }`
- Native interval: `2416` bytes
- Result: `pseudocode`

```c
typedef struct struct_4 {
    char padding_0[16];
    struct struct_2 *field_10;
    struct struct_3 *field_18;
} struct_4;

typedef struct struct_3 {
    char padding_0[48];
    unsigned long long field_30;
} struct_3;

typedef struct struct_2 {
    char padding_0[32];
    long long field_20;
} struct_2;

typedef struct struct_0 {
    char padding_0[184];
    struct struct_1 *field_b8;
    char padding_c0[32];
    unsigned int field_e0;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

extern long long g_1eee870;
extern long long g_1ef0c58;
extern long long g_1efa0c8;
extern long long g_1f082c0;
extern long long g_1f08968;
extern long long g_1f08970;
extern long long g_1f0a290;
extern long long g_1f0aa58;
extern char g_1fab5a3;

long long BloomComponent_Prepare(struct_4 *idx, unsigned long a1, unsigned long long a2, long long a3)
{
    unsigned long long v21;  // d13
    unsigned long long v22;  // d12
    unsigned long long v31;  // x25
    unsigned long long v32;  // x24
    unsigned long long v33;  // x23
    unsigned long long v34;  // x22
    unsigned long long v35;  // x21
    unsigned long long v36;  // x20
    unsigned long long v37;  // x19
    long long v38;  // x0
    struct_0 *v39;  // x0
    unsigned long long v23;  // d11
    unsigned long long v24;  // d10
    unsigned long long v25;  // d9
    unsigned long long v26;  // d8
    unsigned long long v27;  // x30
    unsigned long long v28;  // x28
    unsigned long long v29;  // x27
    unsigned long long v30;  // x26
    unsigned long v0;  // [bp-0xb0]
    unsigned long long v1;  // [bp-0xa0]
    unsigned long long v2;  // [bp-0x90]
    unsigned long long v3;  // [bp-0x88]
    unsigned long long v4;  // [bp-0x80]
    unsigned long long v5;  // [bp-0x78]
    unsigned long long v6;  // [bp-0x70]
    unsigned long long v7;  // [bp-0x68]
    char *v8;  // [bp-0x60]
    unsigned long long v9;  // [bp-0x58]
    unsigned long long v10;  // [bp-0x50]
    unsigned long long v11;  // [bp-0x48]
    unsigned long long v12;  // [bp-0x40]
    unsigned long long v13;  // [bp-0x38]
    unsigned long long v14;  // [bp-0x30]
    unsigned long long v15;  // [bp-0x28]
    unsigned long long v16;  // [bp-0x20]
    unsigned long long v17;  // [bp-0x18]
    unsigned long long v18;  // [bp-0x10]
    unsigned long long v19;  // [bp-0x8]
    char v20;  // [bp+0x0]

    v2 = v21;
    v3 = v22;
    v4 = v23;
    v5 = v24;
    v6 = v25;
    v7 = v26;
    v8 = &v20;
    v9 = v27;
    v10 = v28;
    v11 = v29;
    v12 = v30;
    v13 = v31;
    v14 = v32;
    v15 = v33;
    v16 = v34;
    v17 = v35;
    v18 = v36;
    v19 = v37;
    v1 = a2;
    if (!(g_1fab5a3 & 1))
    {
        sub_f7d92c(&g_1eee870);
        sub_f7d92c("g=");
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c(&g_1efa0c8);
        sub_f7d92c("\tf");
        sub_f7d92c(&g_1f082c0);
        sub_f7d92c(&g_1f0aa58);
        sub_f7d92c(&g_1f0a290);
        sub_f7d92c(&g_1f08968);
        sub_f7d92c(&g_1f08970);
        g_1fab5a3 = 1;
    }
    if (idx->field_18 && idx->field_10 && idx->field_10->field_20)
    {
        v0 = idx->field_18->field_30;
        v38 = MaterialFactory__Get(idx->field_10->field_20, g_1f0aa58, 0);
        if (v38)
        {
            Material__set_shaderKeywords();
            v39 = g_1ef2cd0;
            if (!g_1ef2cd0->field_e0)
            {
                sub_f7da5c(g_1ef2cd0);
                v39 = g_1ef2cd0;
            }
            Material__SetTexture(v38, v39->field_b8->field_0, a3, 0);
            if (idx->field_10)
                PostProcessingContext__get_width(idx->field_10, 0); /* do not return */
        }
    }
    sub_f7da4c(sub_f7db98(sub_f7db7c(sub_f7db74())), 0);
}
```

## `BloomComponent.ctor` — RVA `0xccf220`

- Decompiled symbol: `BloomComponent_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `156` bytes
- Result: `pseudocode`

```c
extern long long g_1eee308;
extern long long g_1efa070;
extern char g_1fab5a4;

void BloomComponent_ctor(long long *a0)
{
    unsigned long long v5;  // x30
    unsigned long long v6;  // x22
    unsigned long long v7;  // x21
    unsigned long long v8;  // x20
    unsigned long long v9;  // x19
    long long v10;  // x1
    long long ptr[6];  // x0
    long long v12;  // x1
    long long p[6];  // x0
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
    if (!(g_1fab5a4 & 1))
    {
        sub_f7d92c(&g_1efa070);
        sub_f7d92c(&g_1eee308);
        g_1fab5a4 = 1;
    }
    v10 = sub_f7d9d4(g_1eee308, 16);
    ptr = a0;
    ptr[4] = v10;
    sub_f7d8d0((long long [6])&ptr[4], v10);
    v12 = sub_f7d9d4(g_1eee308, 16);
    p = a0;
    p[5] = v12;
    sub_f7d8d0((long long [6])&p[5], v12);
}
```
