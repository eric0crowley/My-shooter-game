# Native pseudocode: ImageEffects

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `ImageEffects.RenderDistortion` — RVA `0xce5e5c`

- Decompiled symbol: `ImageEffects_RenderDistortion`
- Metadata signature: `public static void RenderDistortion(Material material, RenderTexture source, RenderTexture destination, float angle, Vector2 center, Vector2 radius) { }`
- Native interval: `608` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[12];
    unsigned long long field_c;
    unsigned int field_14;
} struct_1;

typedef struct struct_2 {
    char padding_0[184];
    struct struct_1 *field_b8;
} struct_2;

extern struct_2 *g_1ef22e8;
extern long long g_1f10258;
extern long long g_1f107e8;
extern char g_1fab1e1;
extern char g_1fab2c9;
extern char g_1fab65e;

long long ImageEffects_RenderDistortion(long long a0, long long a1, long long a2)
{
    unsigned int v20;  // s1
    unsigned int v21;  // s3
    unsigned int v22;  // s4
    unsigned int v23;  // s2
    unsigned int v24;  // s0
    unsigned long long v25;  // cc_dep1
    unsigned long v26;  // 4151
    unsigned long v27;  // 4106
    unsigned long v28;  // 4106
    unsigned long long v29;  // x0
    unsigned long v0;  // [bp-0x160]
    unsigned int v1;  // [bp-0x158]
    unsigned int v2;  // [bp-0x150]
    unsigned int v3;  // [bp-0x14c]
    unsigned int v4;  // [bp-0x148]
    unsigned int v5;  // [bp-0x144]
    char v6;  // [bp-0x140]
    uint128_t v7;  // [bp-0x130]
    uint128_t v8;  // [bp-0x120]
    uint128_t v9;  // [bp-0x110]
    int v10;  // [bp-0x100]
    uint128_t v11;  // [bp-0xf0]
    uint128_t v12;  // [bp-0xe0]
    uint128_t v13;  // [bp-0xd0]
    int v14;  // [bp-0xc0]
    uint128_t v15;  // [bp-0xb0]
    uint128_t v16;  // [bp-0xa0]
    uint128_t v17;  // [bp-0x90]
    char *v18;  // [bp-0x40]
    char v19;  // [bp+0x0]

    v18 = &v19;
    if (!(g_1fab65e & 1))
    {
        sub_f7d92c("g=");
        sub_f7d92c(&g_1f10258);
        sub_f7d92c(&g_1f107e8);
        sub_f7d92c("C(");
        g_1fab65e = 1;
    }
    if (a1)
    {
        v3 = v20;
        v4 = v21;
        v5 = v22;
        Texture__get_texelSize(a1, 0);
        v24 = 0x3f800000 - v23;
        v25 = ((((CmpF(v20, 0.0) >> 5 & 3 | CmpF(v20, 0.0) & 1) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - ((CmpF(v20, 0.0) >> 5 & 3 | CmpF(v20, 0.0) & 1) & (CmpF(v20, 0.0) >> 5 & 3 | CmpF(v20, 0.0) & 1) >> 1 & 1)) * 0x10000000;
        v26 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(v20, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v20, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v20, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v20, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v20, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v20, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if ((char)v26)
        {
            v27 = arm64g_calculate_condition(64, v25, 0, 0);
            if (!((char)v27))
                goto LABEL_10e5f1a;
LABEL_10e5f19:
        }
        else
        {
            v28 = arm64g_calculate_condition(64, v25, 0, 0);
            if ((char)v28)
                goto LABEL_10e5f19;
LABEL_10e5f1a:
            v24 = v23;
        }
        v2 = v24;
        if (!g_1fab2c9)
        {
            sub_f7d92c(&g_1ef22e8);
            g_1fab2c9 = 1;
        }
        Quaternion__Internal_FromEulerRad(0);
        if (!g_1fab1e1)
        {
            sub_f7d92c(&g_1ef22e8);
            g_1fab1e1 = 1;
        }
        v1 = *((int *)((char *)&g_1ef22e8->field_b8->field_c + 4));
        v0 = *((long long *)&(&g_1ef22e8->field_b8->padding_0)[1]);
        Matrix4x4__TRS(0);
        v16 = v12;
        v17 = v13;
        v14 = v10;
        v15 = v11;
        v10 = v14;
        v11 = v15;
        v12 = v16;
        v13 = v17;
        if (a0)
        {
            memcpy(&v6, &v10, 16);
            v7 = v11;
            v8 = v12;
            v9 = v13;
            Material__SetMatrix(a0, g_1f107e8, &v6, 0);
            Material__SetVector(a0, g_1f102f8, 0);
            Material__SetFloat(a0, g_1f10258, 0);
            if (!g_1eefbb8->field_e0)
                sub_f7da5c(g_1eefbb8);
            v29 = Graphics__Blit(a1, a2, a0, 0);
            return Graphics__Blit(a1, a2, a0, 0);
        }
    }
    sub_f7db74();
}
```

## `ImageEffects.Blit` — RVA `0xce60bc`

- Decompiled symbol: `ImageEffects_Blit`
- Metadata signature: `public static void Blit(RenderTexture source, RenderTexture dest) { }`
- Native interval: `104` bytes
- Result: `pseudocode`

```c
extern char g_1fab65f;

void ImageEffects_Blit(unsigned long a0, unsigned long a1)
{
    unsigned long long v5;  // x30
    unsigned long long v6;  // x22
    unsigned long long v7;  // x21
    unsigned long long v8;  // x20
    unsigned long long v9;  // x19
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
    if (!(g_1fab65f & 1))
    {
        sub_f7d92c("g=");
        g_1fab65f = 1;
    }
    if (!g_1eefbb8->field_e0)
        sub_f7da5c(g_1eefbb8);
    Graphics__Blit();
    return;
}
```

## `ImageEffects.BlitWithMaterial` — RVA `0xce6124`

- Decompiled symbol: `ImageEffects_BlitWithMaterial`
- Metadata signature: `public static void BlitWithMaterial(Material material, RenderTexture source, RenderTexture dest) { }`
- Native interval: `112` bytes
- Result: `pseudocode`

```c
extern char g_1fab660;

void ImageEffects_BlitWithMaterial(unsigned long a0, unsigned long a1, unsigned long a2)
{
    unsigned long long v6;  // x30
    unsigned long long v7;  // x23
    unsigned long long v8;  // x22
    unsigned long long v9;  // x21
    unsigned long long v10;  // x20
    unsigned long long v11;  // x19
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
    if (!(g_1fab660 & 1))
    {
        sub_f7d92c("g=");
        g_1fab660 = 1;
    }
    if (!g_1eefbb8->field_e0)
        sub_f7da5c(g_1eefbb8);
    Graphics__Blit();
    return;
}
```

## `ImageEffects.ctor` — RVA `0xce6194`

- Decompiled symbol: `ImageEffects_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long ImageEffects_ctor(void)
{
    long long v0;  // x0

    v0 = Object__ctor();
    return Object__ctor();
}
```
