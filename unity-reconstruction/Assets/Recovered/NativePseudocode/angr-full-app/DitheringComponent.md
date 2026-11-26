# Native pseudocode: DitheringComponent

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `DitheringComponent.get_active` — RVA `0xcd3294`

- Decompiled symbol: `DitheringComponent_get_active`
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

extern long long g_1efa0f0;
extern char g_1fab5c7;

unsigned long long DitheringComponent_get_active(struct_2 *a0)
{
    unsigned long long v0;  // x0

    if (!(g_1fab5c7 & 1))
    {
        sub_f7d92c(&g_1efa0f0);
        g_1fab5c7 = 1;
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

## `DitheringComponent.OnDisable` — RVA `0xcd32fc`

- Decompiled symbol: `DitheringComponent_OnDisable`
- Metadata signature: `public override void OnDisable() { }`
- Native interval: `12` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[32];
    unsigned long long field_20;
} struct_0;

long long DitheringComponent_OnDisable(struct_0 *ptr)
{
    long long v0;  // x0

    ptr->field_20 = 0;
    v0 = sub_f7d8d0();
    return sub_f7d8d0();
}
```

## `DitheringComponent.LoadNoiseTextures` — RVA `0xcd3308`

- Decompiled symbol: `DitheringComponent_LoadNoiseTextures`
- Metadata signature: `private void LoadNoiseTextures() { }`
- Native interval: `260` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned int field_18;
} struct_0;

typedef struct struct_2 {
    char padding_0[32];
    struct struct_1 *field_20;
} struct_2;

typedef struct struct_1 {
    char padding_0[24];
    int field_18;
} struct_1;

typedef struct struct_3 {
    char padding_0[32];
    char field_20;
} struct_3;

extern long long g_1eee3b8;
extern long long g_1f00c60;
extern char g_1fab5c8;

long long DitheringComponent_LoadNoiseTextures(struct_2 *p)
{
    struct_0 *v1;  // x0
    struct_2 *ptr;  // x19
    int v3;  // w22
    struct_1 *v4;  // x23
    long long v5;  // x0
    long long v6;  // x0
    unsigned long v7;  // x0
    unsigned long v8;  // x1
    struct_3 *addr;  // x0
    unsigned long v10;  // x0
    int v0;  // [bp-0x34]

    if (!(g_1fab5c8 & 1))
    {
        sub_f7d92c(&g_1f00c60);
        sub_f7d92c(&g_1eee3b8);
        sub_f7d92c("%\n");
        g_1fab5c8 = 1;
    }
    v1 = sub_f7d9d4(g_1eee3b8, 64);
    p->field_20 = v1;
    ptr = &p->field_20;
    sub_f7d8d0(ptr, v1);
    v3 = 0;
    v0 = 0;
    while (true)
    {
        v4 = *((long long *)&ptr->padding_0[0]);
        v5 = Int32__ToString(&v0, 0);
        v6 = String__Concat(g_1f08ab0, v5, 0);
        v7 = sub_11328ac(v6, g_1f00c60, 0);
        if (v4)
        {
            if (v4->field_18 <= v3)
                break;
            v8 = v7;
            addr = &v4->padding_0[8 * v3];
            *((unsigned long *)&addr->field_20) = v8;
            v10 = sub_f7d8d0((struct struct_3 *)&addr->field_20, v8);
            v3 = v0 + 1;
            v0 = v3;
            if (v3 >= 64)
                return v10;
        }
        else
        {
            v7 = sub_f7db74();
            break;
        }
    }
    sub_f7db7c(v7);
}
```

## `DitheringComponent.Prepare` — RVA `0xcd340c`

- Decompiled symbol: `DitheringComponent_Prepare`
- Metadata signature: `public override void Prepare(Material uberMaterial) { }`
- Native interval: `416` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    char padding_0[32];
    struct struct_1 *field_20;
} struct_2;

typedef struct struct_0 {
    char padding_0[184];
    struct struct_1 *field_b8;
    char padding_c0[32];
    unsigned int field_e0;
} struct_0;

typedef struct struct_1 {
    char padding_0[24];
    int field_18;
} struct_1;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

extern long long g_1f09878;
extern char g_1fab5c9;

long long DitheringComponent_Prepare(struct_2 *ptr, long long a1)
{
    unsigned long long v9;  // d9
    unsigned long long v10;  // d8
    unsigned long v19;  // x8
    unsigned long v20;  // x9
    struct_0 *v21;  // x0
    unsigned long long v11;  // x30
    unsigned long long v12;  // x24
    unsigned long long v13;  // x23
    unsigned long long v14;  // x22
    unsigned long long v15;  // x21
    unsigned long long v16;  // x20
    unsigned long long v17;  // x19
    int v18;  // w8
    unsigned long long v0;  // [bp-0x50]
    unsigned long long v1;  // [bp-0x48]
    unsigned long long v2;  // [bp-0x40]
    unsigned long long v3;  // [bp-0x30]
    unsigned long long v4;  // [bp-0x28]
    unsigned long long v5;  // [bp-0x20]
    unsigned long long v6;  // [bp-0x18]
    unsigned long long v7;  // [bp-0x10]
    unsigned long long v8;  // [bp-0x8]

    v0 = v9;
    v1 = v10;
    v2 = v11;
    v3 = v12;
    v4 = v13;
    v5 = v14;
    v6 = v15;
    v7 = v16;
    v8 = v17;
    if (!(g_1fab5c9 & 1))
    {
        sub_f7d92c("Oh");
        sub_f7d92c(&g_1f09878);
        g_1fab5c9 = 1;
    }
    if (64 <= *((int *)&ptr[1].padding_0[0]) + 1)
        v18 = 0;
    else
        v18 = *((int *)&ptr[1].padding_0[0]) + 1;
    *((int *)&ptr[1].padding_0[0]) = v18;
    Random__get_value();
    Random__get_value(0);
    v19 = ptr->field_20;
    if (ptr->field_20 || (DitheringComponent__LoadNoiseTextures(ptr), v19 = (unsigned long)ptr->field_20, v19))
    {
        v20 = *((int *)&ptr[1].padding_0[0]);
        if (*((int *)(v19 + 24)) <= (unsigned int)v20)
        {
            sub_f7db7c();
        }
        else if (a1)
        {
            Material__EnableKeyword(a1, g_1f09878, 0);
            v21 = g_1ef2f90;
            if (!g_1ef2f90->field_e0)
            {
                sub_f7da5c(g_1ef2f90);
                v21 = g_1ef2f90;
            }
            Material__SetTexture(a1, v21->field_b8->field_0, *((long long *)(v19 + v20 * 8 + 32)), 0);
            if (*((long long *)&ptr->padding_0[16]))
                PostProcessingContext__get_width(*((long long *)&ptr->padding_0[16]), 0); /* do not return */
        }
    }
    sub_f7db74();
    sub_f7db7c();
}
```

## `DitheringComponent.ctor` — RVA `0xcd35ac`

- Decompiled symbol: `DitheringComponent_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `72` bytes
- Result: `pseudocode`

```c
extern long long g_1efa090;
extern char g_1fab5ca;

void DitheringComponent_ctor(unsigned long a0)
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
    if (!(g_1fab5ca & 1))
    {
        sub_f7d92c(&g_1efa090);
        g_1fab5ca = 1;
    }
}
```
