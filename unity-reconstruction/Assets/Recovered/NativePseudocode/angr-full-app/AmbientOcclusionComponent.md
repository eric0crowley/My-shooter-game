# Native pseudocode: AmbientOcclusionComponent

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `AmbientOcclusionComponent.get_occlusionSource` — RVA `0xccd8c4`

- Decompiled symbol: `AmbientOcclusionComponent_get_occlusionSource`
- Metadata signature: `private AmbientOcclusionComponent.OcclusionSource get_occlusionSource() { }`
- Native interval: `164` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned long long field_10;
    struct struct_1 *field_18;
} struct_0;

typedef struct struct_1 {
    char padding_0[33];
    char field_21;
    char padding_22[1];
    char field_23;
} struct_1;

extern long long g_1efa0b8;
extern char g_1fab59b;

unsigned int AmbientOcclusionComponent_get_occlusionSource(struct_0 *ptr)
{
    unsigned long long v0;  // x0
    char v1[36];  // x8

    if (!(g_1fab59b & 1))
    {
        sub_f7d92c(&g_1efa0b8);
        g_1fab59b = 1;
    }
    v0 = ptr->field_10;
    if (v0)
    {
        v0 = PostProcessingContext__get_isGBufferAvailable(v0, 0);
        v1 = ptr->field_18;
        if (((char)v0 & 1))
        {
            if (v1)
            {
                if (!(v1[33] & 1))
                    return 2;
LABEL_10cd920:
                if (!(v1[35] & 1))
                    return 1;
                v0 = ptr->field_10;
                if (v0)
                {
                    v0 = PostProcessingContext__get_isGBufferAvailable(v0, 0);
                    if (!((char)v0 & 1))
                    {
                        return 0;
                    }
                    else if (ptr->field_18)
                    {
                        if (!(ptr->field_18->field_21 & 1))
                            return 1;
                        return 0;
                    }
                }
            }
        }
        else
        {
            if (v1)
                goto LABEL_10cd920;
        }
    }
    sub_f7db74(v0);
}
```

## `AmbientOcclusionComponent.get_ambientOnlySupported` — RVA `0xccd968`

- Decompiled symbol: `AmbientOcclusionComponent_get_ambientOnlySupported`
- Metadata signature: `private bool get_ambientOnlySupported() { }`
- Native interval: `144` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    long long field_10;
} struct_0;

extern long long g_1efa0b8;
extern char g_1fab59c;

long long AmbientOcclusionComponent_get_ambientOnlySupported(struct_0 *a0)
{
    unsigned long long v3;  // x30
    unsigned long long v4;  // x20
    unsigned long long v5;  // x19
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x10]
    unsigned long long v2;  // [bp-0x8]

    v0 = v3;
    v1 = v4;
    v2 = v5;
    if (!(g_1fab59c & 1))
    {
        sub_f7d92c(&g_1efa0b8);
        g_1fab59c = 1;
    }
    if (a0->field_10)
        PostProcessingContext__get_isHdr(a0->field_10, 0); /* do not return */
    sub_f7db74(0);
}
```

## `AmbientOcclusionComponent.get_active` — RVA `0xccd9f8`

- Decompiled symbol: `AmbientOcclusionComponent_get_active`
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
    char padding_11[3];
    unsigned int field_14;
} struct_1;

typedef struct struct_0 {
    char padding_0[48];
    char field_30;
} struct_0;

extern long long g_1efa0b8;
extern char g_1fab59d;

unsigned long long AmbientOcclusionComponent_get_active(struct_2 *ptr)
{
    struct_1 *p;  // x8
    unsigned int v1;  // s0
    unsigned long v2;  // 4129
    unsigned long long v3;  // x0

    if (!(g_1fab59d & 1))
    {
        sub_f7d92c(&g_1efa0b8);
        g_1fab59d = 1;
    }
    p = ptr->field_18;
    if (p)
    {
        if (!(p->field_10 && (v1 = p->field_14, v2 = (unsigned long)arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v1, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v1, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v1, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v1, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v1, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v1, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0), !((char)v2))))
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

## `AmbientOcclusionComponent.GetCameraFlags` — RVA `0xccda6c`

- Decompiled symbol: `AmbientOcclusionComponent_GetCameraFlags`
- Metadata signature: `public override DepthTextureMode GetCameraFlags() { }`
- Native interval: `56` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned long long field_10;
    struct struct_1 *field_18;
} struct_0;

typedef struct struct_1 {
    char padding_0[33];
    char field_21;
    char padding_22[1];
    char field_23;
} struct_1;

long long AmbientOcclusionComponent_GetCameraFlags(struct_0 *a0)
{
    unsigned long long v3;  // x30
    unsigned long long v4;  // x20
    unsigned long long v5;  // x19
    unsigned int v6;  // w20
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x10]
    unsigned long long v2;  // [bp-0x8]

    v0 = v3;
    v1 = v4;
    v2 = v5;
    if (AmbientOcclusionComponent__get_occlusionSource(a0))
        v6 = 0;
    else
        v6 = 1;
    if (AmbientOcclusionComponent__get_occlusionSource(a0) != 2)
        return v6 | 2;
    return v6;
}
```

## `AmbientOcclusionComponent.GetName` — RVA `0xccdaa4`

- Decompiled symbol: `AmbientOcclusionComponent_GetName`
- Metadata signature: `public override string GetName() { }`
- Native interval: `64` bytes
- Result: `pseudocode`

```c
extern unsigned long long g_1f08448;
extern char g_1fab59e;

long long AmbientOcclusionComponent_GetName(void)
{
    if (!(g_1fab59e & 1))
    {
        sub_f7d92c(&g_1f08448);
        g_1fab59e = 1;
    }
    return g_1f08448;
}
```

## `AmbientOcclusionComponent.GetCameraEvent` — RVA `0xccdae4`

- Decompiled symbol: `AmbientOcclusionComponent_GetCameraEvent`
- Metadata signature: `public override CameraEvent GetCameraEvent() { }`
- Native interval: `80` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    long long field_10;
} struct_0;

typedef struct struct_2 {
    char padding_0[16];
    struct struct_3 *field_10;
} struct_2;

typedef struct struct_1 {
    char padding_0[24];
    struct struct_0 *field_18;
} struct_1;

typedef struct struct_3 {
    char padding_0[24];
    struct struct_4 *field_18;
} struct_3;

typedef struct struct_0 {
    char padding_0[20];
    unsigned int field_14;
} struct_0;

typedef struct struct_4 {
    char padding_0[20];
    unsigned int field_14;
} struct_4;

unsigned long long AmbientOcclusionComponent_GetCameraEvent(struct_0 *a0, unsigned long a1)
{
    unsigned long long v0;  // x0

    if (!((char)AmbientOcclusionComponent__get_ambientOnlySupported(a0) & 1))
        return 12;
    if (a0->field_10 && *((long long *)(a0->field_10 + 16)) && *((long long *)(*((long long *)(a0->field_10 + 16)) + 24)))
    {
        if (*((int *)(*((long long *)(*((long long *)(a0->field_10 + 16)) + 24)) + 20)) == 4)
            v0 = 12;
        else
            v0 = 21;
        return v0;
    }
    sub_f7db74();
}
```

## `AmbientOcclusionComponent.PopulateCommandBuffer` — RVA `0xccdb44`

- Decompiled symbol: `AmbientOcclusionComponent_PopulateCommandBuffer`
- Metadata signature: `public override void PopulateCommandBuffer(CommandBuffer cb) { }`
- Native interval: `2484` bytes
- Result: `pseudocode`

```c
typedef struct struct_4 {
    char padding_0[16];
    struct struct_2 *field_10;
    struct struct_3 *field_18;
} struct_4;

typedef struct struct_3 {
    char padding_0[28];
    unsigned long long field_1c;
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
    unsigned int field_4;
    unsigned int field_8;
    char padding_c[4];
    unsigned int field_10;
} struct_1;

typedef struct struct_6 {
    long long field_0;
} struct_6;

typedef struct struct_5 {
    struct struct_6 *field_0;
    unsigned long long field_8;
    unsigned long long field_10;
    unsigned long long field_18;
} struct_5;

extern struct_5 g_1db6f18;
extern struct_0 *g_1ef2bc0;
extern long long g_1efa0b8;
extern long long g_1f0a250;
extern long long g_1f0a258;
extern long long g_1f0a260;
extern long long g_1f0a268;
extern long long g_1f0aa48;
extern long long g_1f0aa50;
extern char g_1fab59f;

long long AmbientOcclusionComponent_PopulateCommandBuffer(struct_4 *a0, unsigned long a1)
{
    unsigned long long v33;  // d9
    unsigned long long v34;  // d8
    unsigned long long v43;  // x21
    unsigned long long v44;  // x20
    unsigned long long v45;  // x19
    long long v46;  // x0
    long long v47;  // x20
    struct_0 *v48;  // x0
    unsigned long v49;  // 4118
    struct_0 *v50;  // x0
    struct_0 *v51;  // x0
    unsigned int v52;  // w8
    unsigned long long v35;  // x30
    long long v53;  // x8
    unsigned long long v36;  // x28
    unsigned long long v37;  // x27
    unsigned long long v38;  // x26
    unsigned long long v39;  // x25
    unsigned long long v40;  // x24
    unsigned long long v41;  // x23
    unsigned long long v42;  // x22
    uint128_t flag17;  // [bp-0x190]
    uint128_t flag16;  // [bp-0x180]
    unsigned long long flag5;  // [bp-0x170]
    uint128_t flag15;  // [bp-0x160]
    uint128_t flag14;  // [bp-0x150]
    unsigned long long flag4;  // [bp-0x140]
    uint128_t flag13;  // [bp-0x130]
    uint128_t flag12;  // [bp-0x120]
    unsigned long long flag3;  // [bp-0x110]
    uint128_t flag11;  // [bp-0x100]
    uint128_t flag10;  // [bp-0xf0]
    unsigned long long flag2;  // [bp-0xe0]
    uint128_t flag9;  // [bp-0xd0]
    uint128_t flag8;  // [bp-0xc0]
    unsigned long long choice;  // [bp-0xb0]
    uint128_t flag7;  // [bp-0xa0]
    uint128_t flag6;  // [bp-0x90]
    unsigned long long flag;  // [bp-0x80]
    unsigned long long v18;  // [bp-0x70]
    unsigned long long v19;  // [bp-0x68]
    char *v20;  // [bp-0x60]
    unsigned long long v21;  // [bp-0x58]
    unsigned long long v22;  // [bp-0x50]
    unsigned long long v23;  // [bp-0x48]
    unsigned long long v24;  // [bp-0x40]
    unsigned long long v25;  // [bp-0x38]
    unsigned long long v26;  // [bp-0x30]
    unsigned long long v27;  // [bp-0x28]
    unsigned long long v28;  // [bp-0x20]
    unsigned long long v29;  // [bp-0x18]
    unsigned long long v30;  // [bp-0x10]
    unsigned long long v31;  // [bp-0x8]
    char v32;  // [bp+0x0]

    v18 = v33;
    v19 = v34;
    v20 = &v32;
    v21 = v35;
    v22 = v36;
    v23 = v37;
    v24 = v38;
    v25 = v39;
    v26 = v40;
    v27 = v41;
    v28 = v42;
    v29 = v43;
    v30 = v44;
    v31 = v45;
    if (!(g_1fab59f & 1))
    {
        sub_f7d92c(&g_1efa0b8);
        sub_f7d92c(&g_1ef2bc0);
        sub_f7d92c(&g_1f0a258);
        sub_f7d92c(&g_1f0a268);
        sub_f7d92c(&g_1f0aa48);
        sub_f7d92c(&g_1f0a250);
        sub_f7d92c(&g_1f0a260);
        sub_f7d92c(&g_1f0aa50);
        g_1fab59f = 1;
    }
    flag = 0;
    choice = 0;
    flag2 = 0;
    flag3 = 0;
    flag4 = 0;
    flag5 = 0;
    flag6 = 0;
    flag7 = 0;
    flag8 = 0;
    flag9 = 0;
    flag10 = 0;
    flag11 = 0;
    flag12 = 0;
    flag13 = 0;
    flag14 = 0;
    flag15 = 0;
    flag16 = 0;
    flag17 = 0;
    if (a0->field_18 && a0->field_10 && a0->field_10->field_20)
    {
        MaterialFactory__Get(a0->field_10->field_20, g_1f0aa50, 0);
        if (a0->field_10 && a0->field_10->field_20)
        {
            v46 = MaterialFactory__Get(a0->field_10->field_20, g_1f0aa48, 0);
            if (v46)
            {
                v47 = v46;
                Material__set_shaderKeywords();
                v48 = g_1ef2bc0;
                if (!g_1ef2bc0->field_e0)
                {
                    sub_f7da5c(g_1ef2bc0);
                    v48 = g_1ef2bc0;
                }
                Material__SetFloat(v47, v48->field_b8->field_0, 0);
                Material__SetFloat(v47, g_1ef2bc0->field_b8->field_4, 0);
                v49 = arm64g_calculate_condition(10, *((long long *)&(&a0->field_18->padding_0)[1]) & 0x100000000, 0, 0);
                Material__SetFloat();
                v50 = g_1ef2bc0;
                if (!g_1ef2bc0->field_e0)
                {
                    sub_f7da5c(g_1ef2bc0);
                    v50 = g_1ef2bc0;
                }
                Material__SetInt(v47, v50->field_b8->field_10, *((long long *)&(&a0->field_18->padding_0)[1]) & 4294967295, 0);
                if (a0->field_10)
                {
                    if (!((char)PostProcessingContext__get_isGBufferAvailable(a0->field_10, 0) & 1) && ((char)RenderSettings__get_fog(0) & 1))
                    {
                        v51 = g_1ef2bc0;
                        if (!g_1ef2bc0->field_e0)
                        {
                            sub_f7da5c(g_1ef2bc0);
                            v51 = g_1ef2bc0;
                        }
                        RenderSettings__get_fogDensity(0);
                        RenderSettings__get_fogStartDistance(0);
                        RenderSettings__get_fogEndDistance(0);
                        Material__SetVector(v47, v51->field_b8->field_8, 0);
                        v52 = RenderSettings__get_fogMode(0) - 1;
                        if (2 < v52)
                            goto LABEL_10cddf8;
                        v53 = (&g_1db6f18.field_0)[v52];
                    }
                    else
                    {
                        v53 = &g_1f0a268;
                    }
                    Material__EnableKeyword(v47, *((long long *)v53), 0);
LABEL_10cddf8:
                    if (a0->field_10)
                        PostProcessingContext__get_width(a0->field_10, 0); /* do not return */
                }
            }
        }
    }
    sub_f7db74();
}
```

## `AmbientOcclusionComponent.ctor` — RVA `0xcce4f8`

- Decompiled symbol: `AmbientOcclusionComponent_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `292` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned int field_18;
    char padding_1c[4];
    uint128_t field_20;
    uint128_t field_30;
    unsigned long long field_40;
    uint128_t field_48;
    uint128_t field_58;
    unsigned long long field_68;
} struct_0;

typedef struct struct_2 {
    char padding_0[32];
    struct struct_1 *field_20;
} struct_2;

typedef struct struct_1 {
    char padding_0[24];
    unsigned int field_18;
    char padding_1c[4];
    uint128_t field_20;
    uint128_t field_30;
    unsigned long long field_40;
    uint128_t field_48;
    uint128_t field_58;
    unsigned long long field_68;
} struct_1;

extern long long g_1eee300;
extern long long g_1efa040;
extern char g_1fab5a0;

long long AmbientOcclusionComponent_ctor(struct_2 *p)
{
    struct_0 *ptr;  // x20
    unsigned long long v13;  // x0
    int v0;  // [bp-0xd0]
    uint128_t v1;  // [bp-0xc0]
    unsigned long long v2;  // [bp-0xb0]
    int v3;  // [bp-0xa0]
    uint128_t v4;  // [bp-0x90]
    unsigned long long v5;  // [bp-0x80]
    char v6;  // [bp-0x78]
    uint128_t v7;  // [bp-0x68]
    unsigned long long v8;  // [bp-0x58]
    char v9;  // [bp-0x50]
    uint128_t v10;  // [bp-0x40]
    unsigned long long v11;  // [bp-0x30]

    if (!(g_1fab5a0 & 1))
    {
        sub_f7d92c(&g_1efa040);
        sub_f7d92c(&g_1eee300);
        g_1fab5a0 = 1;
    }
    ptr = sub_f7d9d4(g_1eee300, 2);
    RenderTargetIdentifier__op_Implicit(10, 0);
    memcpy(&v9, &v6, 16);
    v10 = v7;
    v11 = v8;
    if (ptr)
    {
        memcpy(&v3, &v9, 16);
        v4 = v10;
        v5 = v11;
        if (ptr->field_18)
        {
            ptr->field_40 = v5;
            *((void*)&ptr->field_20) = v3;
            ptr->field_30 = v4;
            RenderTargetIdentifier__op_Implicit(2, 0);
            memcpy(&v0, &v6, 16);
            v1 = v7;
            v2 = v8;
            if (ptr->field_18 > 1)
            {
                *((unsigned long long *)((char *)&ptr->field_58 + 8)) = v2;
                *((uint128_t *)((char *)&ptr->field_48 + 8)) = v1;
                *((void*)&(&ptr->field_40)[1]) = v0;
                p->field_20 = ptr;
                sub_f7d8d0((struct struct_2 *)&p->field_20, ptr);
                v13 = sub_15689ec(p, g_1efa040);
                return sub_15689ec(p, g_1efa040);
            }
        }
        sub_f7db7c();
    }
    sub_f7db74();
}
```
