# Native pseudocode: FxaaComponent

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `FxaaComponent.get_active` — RVA `0xcd4d84`

- Decompiled symbol: `FxaaComponent_get_active`
- Metadata signature: `public override bool get_active() { }`
- Native interval: `112` bytes
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
    char padding_11[3];
    unsigned int field_14;
} struct_1;

typedef struct struct_0 {
    char padding_0[48];
    char field_30;
} struct_0;

extern long long g_1efa0c0;
extern char g_1fab5d8;

unsigned long long FxaaComponent_get_active(struct_2 *ptr, unsigned long a1, unsigned long a2)
{
    struct_1 *v0;  // x8

    if (!(g_1fab5d8 & 1))
    {
        sub_f7d92c(&g_1efa0c0);
        g_1fab5d8 = 1;
    }
    v0 = ptr->field_18;
    if (v0)
    {
        if (!v0->field_10 || v0->field_14)
        {
            return 0;
        }
        else if (ptr->field_10)
        {
            if (ptr->field_10->field_30)
                return 0;
            return 1;
        }
    }
    sub_f7db74();
}
```

## `FxaaComponent.Render` — RVA `0xcd4df4`

- Decompiled symbol: `FxaaComponent_Render`
- Metadata signature: `public void Render(RenderTexture source, RenderTexture destination) { }`
- Native interval: `512` bytes
- Result: `pseudocode`

```c
typedef struct struct_11 {
    char padding_0[16];
    struct struct_10 *field_10;
    unsigned long long field_18;
} struct_11;

typedef struct struct_10 {
    char padding_0[32];
    long long field_20;
} struct_10;

typedef struct struct_2 {
    char padding_0[184];
    struct struct_3 *field_b8;
    char padding_c0[32];
    unsigned int field_e0;
} struct_2;

typedef struct struct_5 {
    char padding_0[184];
    struct struct_6 *field_b8;
    char padding_c0[32];
    unsigned int field_e0;
} struct_5;

typedef struct struct_4 {
    char padding_0[24];
    unsigned int field_18;
} struct_4;

typedef struct struct_3 {
    unsigned long long field_0;
} struct_3;

typedef struct struct_6 {
    struct struct_4 *field_0;
} struct_6;

typedef struct struct_1 {
    unsigned long long field_0;
} struct_1;

typedef struct struct_0 {
    char padding_0[184];
    struct struct_1 *field_b8;
    char padding_c0[32];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef2bd0;
extern struct_5 *g_1ef2bd8;
extern long long g_1efa0c0;
extern long long g_1f0aa78;
extern char g_1fab5d9;

void FxaaComponent_Render(struct_11 *a0, unsigned long a1, unsigned long a2)
{
    unsigned long long v13;  // d14
    unsigned long long v14;  // d13
    unsigned long long v23;  // x21
    unsigned long long v24;  // x20
    unsigned long long v25;  // x19
    struct_2 *v26;  // x0
    struct_5 *v27;  // x8
    struct_2 *v28;  // x21
    unsigned long long v15;  // d12
    unsigned long long v16;  // d11
    unsigned long long v17;  // d10
    unsigned long long v18;  // d9
    unsigned long long v19;  // d8
    unsigned long long v20;  // x30
    unsigned long long v21;  // x23
    unsigned long long v22;  // x22
    unsigned long long v0;  // [bp-0x70]
    unsigned long long v1;  // [bp-0x60]
    unsigned long long v2;  // [bp-0x58]
    unsigned long long v3;  // [bp-0x50]
    unsigned long long v4;  // [bp-0x48]
    unsigned long long v5;  // [bp-0x40]
    unsigned long long v6;  // [bp-0x38]
    unsigned long long v7;  // [bp-0x30]
    unsigned long long v8;  // [bp-0x28]
    unsigned long long v9;  // [bp-0x20]
    unsigned long long v10;  // [bp-0x18]
    unsigned long long v11;  // [bp-0x10]
    unsigned long long v12;  // [bp-0x8]

    v0 = v13;
    v1 = v14;
    v2 = v15;
    v3 = v16;
    v4 = v17;
    v5 = v18;
    v6 = v19;
    v7 = v20;
    v8 = v21;
    v9 = v22;
    v10 = v23;
    v11 = v24;
    v12 = v25;
    if (!(g_1fab5d9 & 1))
    {
        sub_f7d92c(&g_1ef2bd0);
        sub_f7d92c(&g_1ef2bd8);
        sub_f7d92c("g=");
        sub_f7d92c(&g_1efa0c0);
        sub_f7d92c(";j");
        sub_f7d92c(&g_1f0aa78);
        g_1fab5d9 = 1;
    }
    if (a0->field_18 && a0->field_10 && a0->field_10->field_20)
    {
        v26 = MaterialFactory__Get(a0->field_10->field_20, g_1f0aa78, 0);
        v27 = g_1ef2bd8;
        v28 = v26;
        if (!g_1ef2bd8->field_e0)
        {
            v26 = sub_f7da5c(g_1ef2bd8);
            v27 = g_1ef2bd8;
        }
        if (v27->field_b8->field_0)
        {
            if (v27->field_b8->field_0->field_18 <= *((int *)(a0->field_18 + 24)))
                goto LABEL_10d4ff0;
            v26 = g_1ef2bd0;
            if (!g_1ef2bd0->field_e0)
            {
                sub_f7da5c(g_1ef2bd0);
                v26 = g_1ef2bd0;
            }
            if (v26->field_b8->field_0)
            {
                if (*((int *)(v26->field_b8->field_0 + 24)) <= *((int *)(a0->field_18 + 24)))
                    goto LABEL_10d4ff0;
                if (!g_1ef31a8->field_e0)
                    sub_f7da5c(g_1ef31a8);
                if (v28)
                {
                    Material__SetVector(v28, g_1ef31a8->field_b8->field_0, 0);
                    Material__SetVector(v28, g_1ef31a8->field_b8->field_4, 0);
                    if (!g_1eefbb8->field_e0)
                        sub_f7da5c(g_1eefbb8);
                    Graphics__Blit();
                    return;
                }
            }
        }
    }
    v26 = sub_f7db74();
LABEL_10d4ff0:
    sub_f7db7c(v26);
}
```

## `FxaaComponent.ctor` — RVA `0xcd4ff4`

- Decompiled symbol: `FxaaComponent_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `72` bytes
- Result: `pseudocode`

```c
extern long long g_1efa068;
extern char g_1fab5da;

void FxaaComponent_ctor(unsigned long a0)
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
    if (!(g_1fab5da & 1))
    {
        sub_f7d92c(&g_1efa068);
        g_1fab5da = 1;
    }
}
```
