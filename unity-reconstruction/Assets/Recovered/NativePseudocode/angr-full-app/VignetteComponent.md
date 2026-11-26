# Native pseudocode: VignetteComponent

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `VignetteComponent.get_active` — RVA `0xcda95c`

- Decompiled symbol: `VignetteComponent_get_active`
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

extern long long g_1efa128;
extern char g_1fab601;

unsigned long long VignetteComponent_get_active(struct_2 *a0, unsigned long a1)
{
    unsigned long long v0;  // x0

    if (!(g_1fab601 & 1))
    {
        sub_f7d92c(&g_1efa128);
        g_1fab601 = 1;
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

## `VignetteComponent.Prepare` — RVA `0xcda9c4`

- Decompiled symbol: `VignetteComponent_Prepare`
- Metadata signature: `public override void Prepare(Material uberMaterial) { }`
- Native interval: `656` bytes
- Result: `pseudocode`

```c
typedef struct struct_4 {
    char padding_0[24];
    struct struct_3 *field_18;
} struct_4;

typedef struct struct_3 {
    char padding_0[24];
    unsigned int field_18;
    char padding_1c[24];
    unsigned int field_34;
    unsigned int field_38;
    char padding_3c[4];
    long long field_40;
    unsigned int field_48;
    unsigned int field_4c;
} struct_3;

typedef struct struct_1 {
    char padding_0[184];
    struct struct_2 *field_b8;
    char padding_c0[32];
    unsigned int field_e0;
} struct_1;

typedef struct struct_2 {
    unsigned int field_0;
    unsigned int field_4;
    char padding_8[4];
    unsigned int field_c;
} struct_2;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern long long g_1efa128;
extern long long g_1f0f808;
extern long long g_1f0f810;
extern char g_1fab602;

long long VignetteComponent_Prepare(struct_4 *p, long long a1)
{
    struct_3 *ptr;  // x8
    unsigned int v3;  // s8
    unsigned long v4;  // x0
    struct_1 *v5;  // x0
    unsigned long v6;  // 4142
    unsigned long long v7;  // x0
    unsigned long v8;  // x0
    unsigned long v9;  // 4125
    struct_1 *v10;  // x0
    unsigned long long v11;  // x0
    unsigned int v0;  // [bp-0x78]
    unsigned int v1;  // [bp-0x74]

    if (!(g_1fab602 & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c(&g_1efa128);
        sub_f7d92c("3u");
        sub_f7d92c(&g_1f0f810);
        sub_f7d92c(&g_1f0f808);
        g_1fab602 = 1;
    }
    ptr = p->field_18;
    if (ptr)
    {
        v3 = ptr->field_48;
        v0 = ptr->field_34;
        v1 = ptr->field_38;
        if (!g_1ef3f48->field_e0)
            sub_f7da5c(g_1ef3f48);
        if (a1)
        {
            v4 = Material__SetColor(a1, g_1ef3f48->field_b8->field_0, 0);
            if (ptr->field_18 == 1)
            {
                if (!g_1ef0c58->field_e0)
                    sub_f7da5c(g_1ef0c58);
                v8 = Object__op_Inequality(ptr->field_40, 0, 0);
                v9 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v3, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v3, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v3, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v3, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v3, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v3, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                if ((char)v9)
                    return v8;
                if (((char)v8 & 1))
                {
                    Material__EnableKeyword(a1, g_1f0f810, 0);
                    v10 = g_1ef3f48;
                    if (!g_1ef3f48->field_e0)
                    {
                        sub_f7da5c(g_1ef3f48);
                        v10 = g_1ef3f48;
                    }
                    Material__SetTexture(a1, v10->field_b8->field_c, ptr->field_40, 0);
                    v11 = Material__SetFloat();
                    return Material__SetFloat();
                }
                else
                {
                    return v8;
                }
            }
            else if (!ptr->field_18)
            {
                v5 = g_1ef3f48;
                if (!g_1ef3f48->field_e0)
                {
                    sub_f7da5c(g_1ef3f48);
                    v5 = g_1ef3f48;
                }
                Material__SetVector(a1, v5->field_b8->field_4, 0);
                Material__EnableKeyword(a1, g_1f0f808, 0);
                v6 = arm64g_calculate_condition(9, (unsigned long long)(ptr->field_4c & 1), 0, 0);
                v7 = Material__SetVector();
                return Material__SetVector();
            }
            else
            {
                return v4;
            }
        }
    }
    sub_f7db74();
}
```

## `VignetteComponent.ctor` — RVA `0xcdac54`

- Decompiled symbol: `VignetteComponent_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `72` bytes
- Result: `pseudocode`

```c
extern long long g_1efa0b0;
extern char g_1fab603;

void VignetteComponent_ctor(unsigned long a0)
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
    if (!(g_1fab603 & 1))
    {
        sub_f7d92c(&g_1efa0b0);
        g_1fab603 = 1;
    }
}
```
