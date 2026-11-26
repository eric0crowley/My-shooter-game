# Native pseudocode: UserLutComponent

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `UserLutComponent.get_active` — RVA `0xcda538`

- Decompiled symbol: `UserLutComponent_get_active`
- Metadata signature: `public override bool get_active() { }`
- Native interval: `272` bytes
- Result: `pseudocode`

```c
typedef struct struct_5 {
    char padding_0[24];
    struct struct_3 *field_18;
} struct_5;

typedef struct struct_3 {
    char padding_0[16];
    char field_10;
    char padding_11[7];
    struct struct_4 *field_18;
    unsigned int field_20;
} struct_3;

typedef struct struct_1 {
    char padding_0[408];
    struct struct_2 *field_198;
    unsigned long long field_1a0;
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
extern long long g_1efa120;
extern char g_1fab5fc;

unsigned int UserLutComponent_get_active(struct_5 *p, unsigned long a1)
{
    struct_3 *ptr;  // x8
    struct_1 **v1;  // x20
    unsigned int v2;  // s8
    unsigned long long flag;  // x2
    unsigned int v4;  // w0
    unsigned long v5;  // 4137
    struct_1 **v6;  // x0
    unsigned long long v7;  // x1

    if (!(g_1fab5fc & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c(&g_1efa120);
        g_1fab5fc = 1;
    }
    ptr = p->field_18;
    if (ptr)
    {
        if (ptr->field_10)
        {
            v1 = ptr->field_18;
            v2 = ptr->field_20;
            if (!g_1ef0c58->field_e0)
                sub_f7da5c(g_1ef0c58);
            flag = 0;
            v4 = Object__op_Inequality(v1, 0, 0);
            v5 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v2, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v2, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v2, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v2, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v2, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v2, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
            if ((char)v5)
            {
                return 0;
            }
            else if (!((char)v4 & 1))
            {
                return 0;
            }
            else if (v1)
            {
                v6 = v1;
                v7 = *(v1)->field_1a0;
                *(v1)->field_198();
            }
        }
        else
        {
            return 0;
        }
    }
    sub_f7db74();
}
```

## `UserLutComponent.Prepare` — RVA `0xcda648`

- Decompiled symbol: `UserLutComponent_Prepare`
- Metadata signature: `public override void Prepare(Material uberMaterial) { }`
- Native interval: `320` bytes
- Result: `pseudocode`

```c
typedef struct struct_6 {
    char padding_0[24];
    struct struct_4 *field_18;
} struct_6;

typedef struct struct_4 {
    char padding_0[24];
    struct struct_5 *field_18;
} struct_4;

typedef struct struct_2 {
    char padding_0[376];
    struct struct_3 *field_178;
    unsigned long long field_180;
} struct_2;

typedef struct struct_0 {
    char padding_0[184];
    struct struct_1 *field_b8;
    char padding_c0[32];
    unsigned int field_e0;
} struct_0;

typedef struct struct_5 {
    struct struct_2 *field_0;
} struct_5;

typedef struct struct_3 {
    unsigned long long field_0;
} struct_3;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

extern struct_0 *g_1ef3e18;
extern long long g_1efa120;
extern char g_1fab5fd;

void UserLutComponent_Prepare(struct_6 *idx, long long a1)
{
    unsigned long long v7;  // d8
    unsigned long long v8;  // x30
    unsigned long long flag;  // x3
    struct_2 **v18;  // x0
    unsigned long long v19;  // x1
    unsigned long long v9;  // x23
    unsigned long long v10;  // x22
    unsigned long long v11;  // x21
    unsigned long long v12;  // x20
    unsigned long long v13;  // x19
    struct_2 **v14;  // x20
    struct_0 *v15;  // x0
    struct_2 **v16;  // x2
    unsigned long long v0;  // [bp-0x40]
    unsigned long long v1;  // [bp-0x30]
    unsigned long long v2;  // [bp-0x28]
    unsigned long long v3;  // [bp-0x20]
    unsigned long long v4;  // [bp-0x18]
    unsigned long long v5;  // [bp-0x10]
    unsigned long long v6;  // [bp-0x8]

    v0 = v7;
    v1 = v8;
    v2 = v9;
    v3 = v10;
    v4 = v11;
    v5 = v12;
    v6 = v13;
    if (!(g_1fab5fd & 1))
    {
        sub_f7d92c(&g_1efa120);
        sub_f7d92c(&g_1ef3e18);
        sub_f7d92c("3$");
        g_1fab5fd = 1;
    }
    if (idx->field_18 && a1)
    {
        v14 = idx->field_18->field_18;
        Material__EnableKeyword(a1, g_1f0f2c0, 0);
        v15 = g_1ef3e18;
        if (!g_1ef3e18->field_e0)
        {
            sub_f7da5c(g_1ef3e18);
            v15 = g_1ef3e18;
        }
        v16 = v14;
        flag = 0;
        Material__SetTexture(a1, v15->field_b8->field_0, v14, 0);
        if (v14)
        {
            v18 = v14;
            v19 = *(v14)->field_180;
            *(v14)->field_178();
        }
    }
    sub_f7db74();
}
```

## `UserLutComponent.OnGUI` — RVA `0xcda788`

- Decompiled symbol: `UserLutComponent_OnGUI`
- Metadata signature: `public void OnGUI() { }`
- Native interval: `240` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    long long field_10;
    unsigned long long field_18;
} struct_0;

extern long long g_1efa120;
extern char g_1fab5fe;

long long UserLutComponent_OnGUI(struct_0 *a0)
{
    unsigned long long v6;  // d8
    unsigned long long v7;  // x30
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
    if (!(g_1fab5fe & 1))
    {
        sub_f7d92c("O<");
        sub_f7d92c(&g_1efa120);
        g_1fab5fe = 1;
    }
    if (a0->field_18 && a0->field_10)
        PostProcessingContext__get_viewport(a0->field_10, 0); /* do not return */
    sub_f7db74();
}
```

## `UserLutComponent.ctor` — RVA `0xcda878`

- Decompiled symbol: `UserLutComponent_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `72` bytes
- Result: `pseudocode`

```c
extern long long g_1efa0a8;
extern char g_1fab5ff;

void UserLutComponent_ctor(unsigned long a0)
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
    if (!(g_1fab5ff & 1))
    {
        sub_f7d92c(&g_1efa0a8);
        g_1fab5ff = 1;
    }
}
```
