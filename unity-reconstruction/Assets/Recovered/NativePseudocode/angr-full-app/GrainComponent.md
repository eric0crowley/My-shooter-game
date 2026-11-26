# Native pseudocode: GrainComponent

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `GrainComponent.get_active` — RVA `0xcd50d8`

- Decompiled symbol: `GrainComponent_get_active`
- Metadata signature: `public override bool get_active() { }`
- Native interval: `132` bytes
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

extern long long g_1efa108;
extern char g_1fab5dc;

unsigned long long GrainComponent_get_active(struct_2 *ptr)
{
    struct_1 *p;  // x8
    unsigned int v1;  // s0
    unsigned long v2;  // 4129
    unsigned long long v3;  // x0

    if (!(g_1fab5dc & 1))
    {
        sub_f7d92c(&g_1efa108);
        g_1fab5dc = 1;
    }
    p = ptr->field_18;
    if (p)
    {
        if (!(p->field_10 && (v1 = p->field_18, v2 = (unsigned long)arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v1, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v1, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v1, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v1, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v1, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v1, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0), !((char)v2) && ((char)(unsigned long long)SystemInfo__SupportsRenderTextureFormat(2, 0) & 1))))
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

## `GrainComponent.OnDisable` — RVA `0xcd515c`

- Decompiled symbol: `GrainComponent_OnDisable`
- Metadata signature: `public override void OnDisable() { }`
- Native interval: `40` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[32];
    long long field_20;
} struct_0;

void GrainComponent_OnDisable(struct_0 *ptr)
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

## `GrainComponent.Prepare` — RVA `0xcd5184`

- Decompiled symbol: `GrainComponent_Prepare`
- Metadata signature: `public override void Prepare(Material uberMaterial) { }`
- Native interval: `928` bytes
- Result: `pseudocode`

```c
typedef struct struct_6 {
    char padding_0[16];
    struct struct_4 *field_10;
    struct struct_5 *field_18;
    long long field_20;
} struct_6;

typedef struct struct_5 {
    char padding_0[20];
    unsigned long long field_14;
} struct_5;

typedef struct struct_4 {
    char padding_0[32];
    long long field_20;
} struct_4;

typedef struct struct_2 {
    char padding_0[184];
    struct struct_3 *field_b8;
    char padding_c0[32];
    unsigned int field_e0;
} struct_2;

typedef struct struct_3 {
    unsigned int field_0;
    char padding_4[4];
    unsigned int field_8;
    unsigned int field_c;
} struct_3;

typedef struct struct_1 {
    char padding_0[224];
    unsigned int field_e0;
} struct_1;

extern struct_1 *g_1ef0c58;
extern long long g_1ef1298;
extern struct_2 *g_1ef3248;
extern long long g_1efa108;
extern long long g_1f0a628;
extern long long g_1f0a7b8;
extern long long g_1f0aa88;
extern char g_1fab5dd;

long long GrainComponent_Prepare(struct_6 *a0, long long a1)
{
    unsigned long long v14;  // d12
    unsigned long long v15;  // d11
    unsigned long long v24;  // x22
    unsigned long long v25;  // x21
    unsigned long long v26;  // x20
    unsigned long long v27;  // x19
    unsigned int v28;  // w23
    struct_6 *ptr;  // x21
    long long v30;  // x22
    long long v31;  // x22
    struct_2 *v32;  // x0
    unsigned long long v16;  // d10
    unsigned long long v17;  // d9
    unsigned long long v18;  // d8
    unsigned long long v19;  // x30
    unsigned long long v20;  // x26
    unsigned long long v21;  // x25
    unsigned long long v22;  // x24
    unsigned long long v23;  // x23
    unsigned long long v0;  // [bp-0x70]
    unsigned long long v1;  // [bp-0x68]
    unsigned long long v2;  // [bp-0x60]
    unsigned long long v3;  // [bp-0x58]
    unsigned long long v4;  // [bp-0x50]
    unsigned long long v5;  // [bp-0x48]
    unsigned long long v6;  // [bp-0x40]
    unsigned long long v7;  // [bp-0x38]
    unsigned long long v8;  // [bp-0x30]
    unsigned long long v9;  // [bp-0x28]
    unsigned long long v10;  // [bp-0x20]
    unsigned long long v11;  // [bp-0x18]
    unsigned long long v12;  // [bp-0x10]
    unsigned long long v13;  // [bp-0x8]

    v0 = v14;
    v1 = v15;
    v2 = v16;
    v3 = v17;
    v4 = v18;
    v5 = v19;
    v6 = v20;
    v7 = v21;
    v8 = v22;
    v9 = v23;
    v10 = v24;
    v11 = v25;
    v12 = v26;
    v13 = v27;
    if (!(g_1fab5dd & 1))
    {
        sub_f7d92c("g=");
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c(&g_1efa108);
        sub_f7d92c(&g_1ef1298);
        sub_f7d92c(&g_1ef3248);
        sub_f7d92c(&g_1f0a7b8);
        sub_f7d92c(&g_1f0aa88);
        sub_f7d92c(&g_1f0a628);
        g_1fab5dd = 1;
    }
    if (a0->field_18 && a1)
    {
        v28 = *((long long *)&(&a0->field_18->padding_0)[1]);
        Material__EnableKeyword(a1, g_1f0a628, 0);
        Time__get_realtimeSinceStartup(0);
        Random__get_value(0);
        Random__get_value(0);
        ptr = &a0->field_20;
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        if (((char)Object__op_Equality(a0->field_20, 0, 0) & 1))
        {
LABEL_10d52b8:
            GraphicsUtils__Destroy(*((long long *)&ptr->padding_0[0]), 0);
            v30 = sub_f7db70(g_1ef1298);
            RenderTexture__ctor(v30, 192, 192, 0, 2, 0);
            if (v30)
            {
                Texture__set_filterMode(v30, 1, 0);
                Texture__set_wrapMode(v30, 0, 0);
                Texture__set_anisoLevel(v30, 0, 0);
                Object__set_name(v30, g_1f0a7b8, 0);
                *((long long *)&ptr->padding_0[0]) = v30;
                sub_f7d8d0(ptr, v30);
                if (*((long long *)&ptr->padding_0[0]))
                {
                    RenderTexture__Create(*((long long *)&ptr->padding_0[0]), 0);
LABEL_10d535c:
                    if (a0->field_10 && a0->field_10->field_20)
                    {
                        v31 = MaterialFactory__Get(a0->field_10->field_20, g_1f0aa88, 0);
                        if (!g_1ef3248->field_e0)
                            sub_f7da5c(g_1ef3248);
                        if (v31)
                        {
                            Material__SetFloat(v31, g_1ef3248->field_b8->field_c, 0);
                            if (!g_1eefbb8->field_e0)
                                sub_f7da5c(g_1eefbb8);
                            Graphics__Blit(0, *((long long *)&ptr->padding_0[0]), v31, v28 & 1, 0);
                            v32 = g_1ef3248;
                            if (!g_1ef3248->field_e0)
                            {
                                sub_f7da5c(g_1ef3248);
                                v32 = g_1ef3248;
                            }
                            Material__SetTexture(a1, v32->field_b8->field_8, a0->field_20, 0);
                            Material__SetVector(a1, g_1ef3248->field_b8->field_0, 0);
                            if (a0->field_10)
                                PostProcessingContext__get_width(a0->field_10, 0); /* do not return */
                        }
                    }
                }
            }
        }
        else if (*((long long *)&ptr->padding_0[0]))
        {
            if ((RenderTexture__IsCreated(*((long long *)&ptr->padding_0[0]), 0) & 1))
                goto LABEL_10d535c;
            goto LABEL_10d52b8;
        }
    }
    sub_f7db74();
}
```

## `GrainComponent.ctor` — RVA `0xcd5524`

- Decompiled symbol: `GrainComponent_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `72` bytes
- Result: `pseudocode`

```c
extern long long g_1efa0a0;
extern char g_1fab5de;

void GrainComponent_ctor(unsigned long a0)
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
    if (!(g_1fab5de & 1))
    {
        sub_f7d92c(&g_1efa0a0);
        g_1fab5de = 1;
    }
}
```
