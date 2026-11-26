# Native pseudocode: DepthOfFieldComponent

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `DepthOfFieldComponent.get_active` — RVA `0xcd25c4`

- Decompiled symbol: `DepthOfFieldComponent_get_active`
- Metadata signature: `public override bool get_active() { }`
- Native interval: `104` bytes
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
} struct_1;

typedef struct struct_0 {
    char padding_0[48];
    char field_30;
} struct_0;

extern long long g_1efa0e8;
extern char g_1fab5bf;

unsigned long long DepthOfFieldComponent_get_active(struct_2 *a0)
{
    unsigned long long v0;  // x0

    if (!(g_1fab5bf & 1))
    {
        sub_f7d92c(&g_1efa0e8);
        g_1fab5bf = 1;
    }
    if (a0->field_18)
    {
        if (!a0->field_18->field_10)
        {
            return 0;
        }
        else if (a0->field_10)
        {
            if (a0->field_10->field_30)
                v0 = 0;
            else
                v0 = 1;
            return v0;
        }
    }
    sub_f7db74();
}
```

## `DepthOfFieldComponent.GetCameraFlags` — RVA `0xcd262c`

- Decompiled symbol: `DepthOfFieldComponent_GetCameraFlags`
- Metadata signature: `public override DepthTextureMode GetCameraFlags() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
unsigned int DepthOfFieldComponent_GetCameraFlags(void)
{
    return 1;
}
```

## `DepthOfFieldComponent.CalculateFocalLength` — RVA `0xcd2634`

- Decompiled symbol: `DepthOfFieldComponent_CalculateFocalLength`
- Metadata signature: `private float CalculateFocalLength() { }`
- Native interval: `156` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    char padding_0[16];
    struct struct_0 *field_10;
    struct struct_1 *field_18;
} struct_2;

typedef struct struct_1 {
    char padding_0[32];
    char field_20;
} struct_1;

typedef struct struct_0 {
    char padding_0[24];
    long long field_18;
} struct_0;

extern long long g_1efa0e8;
extern char g_1fab5c0;

void DepthOfFieldComponent_CalculateFocalLength(struct_2 *a0, unsigned long a1)
{
    if (!(g_1fab5c0 & 1))
    {
        sub_f7d92c(&g_1efa0e8);
        g_1fab5c0 = 1;
    }
    if (a0->field_18)
    {
        if (!(a0->field_18->field_20 & 1))
        {
            return;
        }
        else if (a0->field_10 && a0->field_10->field_18)
        {
            tanf(Camera__get_fieldOfView(a0->field_10->field_18, 0), 0);
            return;
        }
    }
    sub_f7db74();
}
```

## `DepthOfFieldComponent.CalculateMaxCoCRadius` — RVA `0xcd26d0`

- Decompiled symbol: `DepthOfFieldComponent_CalculateMaxCoCRadius`
- Metadata signature: `private float CalculateMaxCoCRadius(int screenHeight) { }`
- Native interval: `116` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

extern long long g_1efa0e8;
extern char g_1fab5c1;

struct_0 * DepthOfFieldComponent_CalculateMaxCoCRadius(struct_0 *a0, unsigned long a1, unsigned long a2)
{
    struct_0 *v0;  // x0
    struct_0 *v1;  // x0
    struct_0 *v2;  // x0

    v0 = a0;
    if (!(g_1fab5c1 & 1))
    {
        v1 = sub_f7d92c(&g_1efa0e8);
        g_1fab5c1 = 1;
        v0 = v1;
    }
    v2 = v0;
    if (a0->field_18)
        return v2;
    sub_f7db74();
}
```

## `DepthOfFieldComponent.CheckHistory` — RVA `0xcd2744`

- Decompiled symbol: `DepthOfFieldComponent_CheckHistory`
- Metadata signature: `private bool CheckHistory(int width, int height) { }`
- Native interval: `208` bytes
- Result: `pseudocode`

```c
typedef struct struct_3 {
    char padding_0[32];
    struct struct_4 *field_20;
} struct_3;

typedef struct struct_1 {
    char padding_0[376];
    struct struct_2 *field_178;
    unsigned long long field_180;
} struct_1;

typedef struct struct_4 {
    struct struct_1 *field_0;
} struct_4;

typedef struct struct_2 {
    unsigned long long field_0;
} struct_2;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab5c2;

unsigned int DepthOfFieldComponent_CheckHistory(struct_3 *ptr, unsigned long a1, unsigned long a2)
{
    unsigned long long flag;  // x2
    struct_1 **v1;  // x0
    unsigned long long v2;  // x1

    if (!(g_1fab5c2 & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab5c2 = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    flag = 0;
    if (!((char)Object__op_Inequality(ptr->field_20, 0, 0) & 1))
        return 0;
    v1 = ptr->field_20;
    if (v1)
    {
        if (((char)RenderTexture__IsCreated(v1, 0) & 1))
        {
            v1 = ptr->field_20;
            if (v1)
            {
                v2 = *(v1)->field_180;
                *(v1)->field_178();
            }
        }
        else
        {
            return 0;
        }
    }
    sub_f7db74(v1);
}
```

## `DepthOfFieldComponent.SelectFormat` — RVA `0xcd2814`

- Decompiled symbol: `DepthOfFieldComponent_SelectFormat`
- Metadata signature: `private RenderTextureFormat SelectFormat(RenderTextureFormat primary, RenderTextureFormat secondary) { }`
- Native interval: `76` bytes
- Result: `pseudocode`

```c
unsigned int DepthOfFieldComponent_SelectFormat(unsigned long a0, unsigned int a1, unsigned int a2)
{
    unsigned long v0;  // 4116

    if (((char)SystemInfo__SupportsRenderTextureFormat(a1, 0) & 1))
        return a1;
    v0 = arm64g_calculate_condition(25, (unsigned long long)((unsigned int)(unsigned long long)SystemInfo__SupportsRenderTextureFormat((unsigned long long)a2, 0) & 1), 0, 0);
    if (!((char)v0))
        return 7;
    return a2;
}
```

## `DepthOfFieldComponent.Prepare` — RVA `0xcd2860`

- Decompiled symbol: `DepthOfFieldComponent_Prepare`
- Metadata signature: `public void Prepare(RenderTexture source, Material uberMaterial, bool antialiasCoC, Vector2 taaJitter, float taaBlending) { }`
- Native interval: `1836` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    char padding_0[16];
    struct struct_0 *field_10;
    struct struct_1 *field_18;
} struct_2;

typedef struct struct_0 {
    char padding_0[376];
    struct struct_1 *field_178;
    unsigned long long field_180;
} struct_0;

typedef struct struct_0 {
    char padding_0[24];
    long long field_18;
} struct_0;

typedef struct struct_1 {
    char padding_0[32];
    char field_20;
} struct_1;

typedef struct struct_1 {
    unsigned long long field_0;
} struct_1;

extern long long g_1ef0c58;
extern long long g_1ef2f60;
extern long long g_1efa0e8;
extern long long g_1f09850;
extern long long g_1f09858;
extern long long g_1f0a290;
extern long long g_1f0aa68;
extern char g_1fab5c3;

void DepthOfFieldComponent_Prepare(struct_2 *idx, struct_0 **a1, unsigned long a2, unsigned long a3)
{
    unsigned long long v21;  // d15
    unsigned long long v22;  // d14
    unsigned long long v31;  // x27
    unsigned long long v32;  // x26
    unsigned long long v33;  // x25
    unsigned long long v34;  // x24
    unsigned long long v35;  // x23
    unsigned long long v36;  // x22
    unsigned long long v37;  // x21
    unsigned long long v38;  // x20
    unsigned long long v39;  // x19
    unsigned int v40;  // s8
    unsigned long long v23;  // d13
    unsigned long v41;  // 4116
    unsigned int v42;  // s0
    unsigned long v43;  // 4129
    struct_0 **v44;  // x0
    unsigned long v45;  // x1
    unsigned long long v24;  // d12
    unsigned long long v25;  // d11
    unsigned long long v26;  // d10
    unsigned long long v27;  // d9
    unsigned long long v28;  // d8
    unsigned long long v29;  // x30
    unsigned long long v30;  // x28
    unsigned long long v0;  // [bp-0xa0]
    unsigned long long v1;  // [bp-0x98]
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

    v0 = v21;
    v1 = v22;
    v2 = v23;
    v3 = v24;
    v4 = v25;
    v5 = v26;
    v6 = v27;
    v7 = v28;
    v8 = &v20;
    v9 = v29;
    v10 = v30;
    v11 = v31;
    v12 = v32;
    v13 = v33;
    v14 = v34;
    v15 = v35;
    v16 = v36;
    v17 = v37;
    v18 = v38;
    v19 = v39;
    if (!(g_1fab5c3 & 1))
    {
        sub_f7d92c("g=");
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c(&g_1efa0e8);
        sub_f7d92c(&g_1ef2f60);
        sub_f7d92c(&g_1f09850);
        sub_f7d92c(&g_1f0aa68);
        sub_f7d92c(&g_1f0a290);
        sub_f7d92c(&g_1f09858);
        g_1fab5c3 = 1;
    }
    if (idx->field_18)
    {
        v40 = *((int *)&idx->field_18->padding_0[20]);
        if (!((char)SystemInfo__SupportsRenderTextureFormat(16, 0) & 1))
            v41 = arm64g_calculate_condition(25, (unsigned long long)((unsigned int)(unsigned long long)SystemInfo__SupportsRenderTextureFormat(15, 0) & 1), 0, 0);
        DepthOfFieldComponent__CalculateFocalLength(idx, 0);
        v43 = arm64g_calculate_condition(192, (((((unsigned long long)(char)(CmpF(v40, v42)) >> 5 & 3 | (unsigned long long)(CmpF(v40, v42) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v40, v42)) >> 5 & 3 | (unsigned long long)(CmpF(v40, v42) & 1)) & ((unsigned long long)(char)(CmpF(v40, v42)) >> 5 & 3 | (unsigned long long)(CmpF(v40, v42) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if (a1)
        {
            v44 = a1;
            v45 = *(a1)->field_180;
            *(a1)->field_178();
        }
    }
    sub_f7db74();
}
```

## `DepthOfFieldComponent.OnDisable` — RVA `0xcd2f8c`

- Decompiled symbol: `DepthOfFieldComponent_OnDisable`
- Metadata signature: `public override void OnDisable() { }`
- Native interval: `128` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[32];
    long long field_20;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab5c4;

void DepthOfFieldComponent_OnDisable(struct_1 *a0)
{
    unsigned long long v4;  // x30
    unsigned long long v5;  // x21
    unsigned long long v6;  // x20
    unsigned long long v7;  // x19
    struct_1 *ptr;  // x19
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x18]
    unsigned long long v2;  // [bp-0x10]
    unsigned long long v3;  // [bp-0x8]

    v0 = v4;
    v1 = v5;
    v2 = v6;
    v3 = v7;
    if (!(g_1fab5c4 & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab5c4 = 1;
    }
    ptr = &a0->field_20;
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (((char)Object__op_Inequality(a0->field_20, 0, 0) & 1))
        RenderTexture__ReleaseTemporary(*((long long *)&ptr->padding_0[0]), 0);
    *((long long *)&ptr->padding_0[0]) = 0;
    sub_f7d8d0();
    return;
}
```

## `DepthOfFieldComponent.ctor` — RVA `0xcd300c`

- Decompiled symbol: `DepthOfFieldComponent_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `72` bytes
- Result: `pseudocode`

```c
extern long long g_1efa088;
extern char g_1fab5c5;

void DepthOfFieldComponent_ctor(unsigned long a0)
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
    if (!(g_1fab5c5 & 1))
    {
        sub_f7d92c(&g_1efa088);
        g_1fab5c5 = 1;
    }
}
```
