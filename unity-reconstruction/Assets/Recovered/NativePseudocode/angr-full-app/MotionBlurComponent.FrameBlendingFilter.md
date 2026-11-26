# Native pseudocode: MotionBlurComponent.FrameBlendingFilter

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `MotionBlurComponent.FrameBlendingFilter.ctor` — RVA `0xcd5778`

- Decompiled symbol: `MotionBlurComponent_FrameBlendingFilter_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `120` bytes
- Result: `pseudocode`
- Heuristic layout hint: `MotionBlurComponent_FrameBlendingFilter_Recovered` matched 3 offsets against `MotionBlurComponent.FrameBlendingFilter` metadata (confidence 1.00).

```c
typedef struct MotionBlurComponent_FrameBlendingFilter_Recovered {
    char padding_0[16];
    char m_UseCompression;
    char padding_11[3];
    unsigned int m_RawTextureFormat;
    unsigned long long m_FrameList;
} MotionBlurComponent_FrameBlendingFilter_Recovered;

extern long long g_1eee618;
extern char g_1fab5e8;

void MotionBlurComponent_FrameBlendingFilter_ctor(struct_0 *ptr)
{
    unsigned long long v4;  // x30
    unsigned long long v5;  // x21
    unsigned long long v6;  // x20
    unsigned long long v7;  // x19
    long long v8;  // x0
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x18]
    unsigned long long v2;  // [bp-0x10]
    unsigned long long v3;  // [bp-0x8]

    v0 = v4;
    v1 = v5;
    v2 = v6;
    v3 = v7;
    if (!(g_1fab5e8 & 1))
    {
        sub_f7d92c(&g_1eee618);
        g_1fab5e8 = 1;
    }
    v8 = MotionBlurComponent_FrameBlendingFilter__CheckSupportCompression(Object__ctor(ptr, 0), 0);
    ptr->field_10 = (char)v8 & 1;
    ptr->field_14 = MotionBlurComponent_FrameBlendingFilter__GetPreferredRenderTextureFormat(v8);
    ptr->field_18 = sub_f7d9d4(g_1eee618, 4);
    sub_f7d8d0();
    return;
}
```

## `MotionBlurComponent.FrameBlendingFilter.Dispose` — RVA `0xcd591c`

- Decompiled symbol: `MotionBlurComponent_FrameBlendingFilter_Dispose`
- Metadata signature: `public void Dispose() { }`
- Native interval: `116` bytes
- Result: `pseudocode`
- Heuristic layout hint: `MotionBlurComponent_FrameBlendingFilter_Recovered` matched 2 offsets against `MotionBlurComponent.FrameBlendingFilter` metadata (confidence 0.67).

```c
typedef struct struct_1 {
    char padding_0[24];
    struct MotionBlurComponent_FrameBlendingFilter_Recovered *field_18;
} struct_1;

typedef struct MotionBlurComponent_FrameBlendingFilter_Recovered {
    char padding_0[24];
    unsigned long long m_FrameList;
    uint128_t m_LastFrameCount;
    uint128_t field_30;
} MotionBlurComponent_FrameBlendingFilter_Recovered;

struct_1 * MotionBlurComponent_FrameBlendingFilter_Dispose(struct_1 *p)
{
    struct_0 *v2;  // x19
    unsigned long ptr;  // x21
    int v0;  // [bp-0x40], Other Possible Types: uint128_t
    int v1;  // [bp-0x30], Other Possible Types: uint128_t

    v0 = 0;
    v1 = 0;
    v2 = p->field_18;
    if (v2)
    {
        if ((unsigned int)v2->field_18 >= 1)
        {
            ptr = &v2->field_20;
            if ((v2->field_18 & 4294967295) > 0)
            {
                v0 = (int)*((int128_t *)ptr);
                v1 = (int)*((int128_t *)(ptr + 16));
                MotionBlurComponent_FrameBlendingFilter_Frame__Release(&v0); /* do not return */
            }
            sub_f7db7c();
        }
        else
        {
            return p;
        }
    }
    sub_f7db74();
}
```

## `MotionBlurComponent.FrameBlendingFilter.BlendFrames` — RVA `0xcd6954`

- Decompiled symbol: `MotionBlurComponent_FrameBlendingFilter_BlendFrames`
- Metadata signature: `public void BlendFrames(CommandBuffer cb, float strength, RenderTargetIdentifier source, RenderTargetIdentifier destination, Material material) { }`
- Native interval: `1252` bytes
- Result: `pseudocode`
- Heuristic layout hint: `MotionBlurComponent_FrameBlendingFilter_Recovered` matched 2 offsets against `MotionBlurComponent.FrameBlendingFilter` metadata (confidence 0.67).

```c
typedef struct struct_2 {
    char padding_0[16];
    char field_10;
} struct_2;

typedef struct struct_0 {
    char padding_0[184];
    struct struct_1 *field_b8;
    char padding_c0[32];
    unsigned int field_e0;
} struct_0;

typedef struct struct_3 {
    uint128_t field_0;
    uint128_t field_10;
    unsigned long long field_20;
} struct_3;

typedef struct struct_4 {
    uint128_t field_0;
    uint128_t field_10;
    unsigned long long field_20;
} struct_4;

typedef struct struct_5 {
    char field_0[16];
    uint128_t field_10;
    unsigned long long field_20;
} struct_5;

typedef struct MotionBlurComponent_FrameBlendingFilter_Recovered {
    char field_0[16];
    uint128_t m_UseCompression;
    unsigned long long m_LastFrameCount;
} MotionBlurComponent_FrameBlendingFilter_Recovered;

typedef struct struct_1 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[36];
    unsigned int field_38;
    unsigned int field_3c;
    unsigned int field_40;
    unsigned int field_44;
    unsigned int field_48;
    unsigned int field_4c;
    unsigned int field_50;
    unsigned int field_54;
    unsigned int field_58;
    unsigned int field_5c;
    unsigned int field_60;
    unsigned int field_64;
} struct_1;

extern struct_0 *g_1ef3510;
extern char g_1fab5e9;

long long MotionBlurComponent_FrameBlendingFilter_BlendFrames(struct_2 *a0, long long a1, struct_3 *ptr, struct_4 *ptr3, long long a4, unsigned long a5)
{
    struct_0 *v62;  // x0
    struct_5 *p;  // x8
    struct_6 *addr;  // x9
    unsigned long long v65;  // x0
    int v0;  // [bp-0x4a0]
    int v1;  // [bp-0x490]
    unsigned long v2;  // [bp-0x480]
    int v3;  // [bp-0x470]
    int v4;  // [bp-0x460]
    unsigned long v5;  // [bp-0x450]
    int v6;  // [bp-0x440]
    int v7;  // [bp-0x430]
    unsigned long v8;  // [bp-0x420]
    int v9;  // [bp-0x410]
    int v10;  // [bp-0x400]
    unsigned long v11;  // [bp-0x3f0]
    char v12;  // [bp-0x3e0]
    uint128_t v13;  // [bp-0x3d0]
    unsigned long long v14;  // [bp-0x3c0]
    char v15;  // [bp-0x3b0]
    uint128_t v16;  // [bp-0x3a0]
    unsigned long long v17;  // [bp-0x390]
    char v18;  // [bp-0x380]
    uint128_t v19;  // [bp-0x370]
    unsigned long long v20;  // [bp-0x360]
    char v21;  // [bp-0x350]
    uint128_t v22;  // [bp-0x340]
    unsigned long long v23;  // [bp-0x330]
    char v24;  // [bp-0x320]
    uint128_t v25;  // [bp-0x310]
    unsigned long long v26;  // [bp-0x300]
    char v27;  // [bp-0x2f0]
    uint128_t v28;  // [bp-0x2e0]
    unsigned long long v29;  // [bp-0x2d0]
    char v30;  // [bp-0x2c0]
    uint128_t v31;  // [bp-0x2b0]
    unsigned long long v32;  // [bp-0x2a0]
    char v33;  // [bp-0x290]
    uint128_t v34;  // [bp-0x280]
    unsigned long long v35;  // [bp-0x270]
    int v36;  // [bp-0x260], Other Possible Types: char
    int v37;  // [bp-0x250], Other Possible Types: uint128_t
    unsigned long v38;  // [bp-0x240], Other Possible Types: unsigned long long
    char v39;  // [bp-0x230]
    uint128_t v40;  // [bp-0x220]
    unsigned long long v41;  // [bp-0x210]
    int v42;  // [bp-0x200], Other Possible Types: uint128_t
    int v43;  // [bp-0x1f0], Other Possible Types: uint128_t
    unsigned long v44;  // [bp-0x1e0], Other Possible Types: unsigned long long
    int v45;  // [bp-0x1d0], Other Possible Types: uint128_t
    int v46;  // [bp-0x1c0], Other Possible Types: uint128_t
    unsigned long v47;  // [bp-0x1b0], Other Possible Types: unsigned long long
    int v48;  // [bp-0x1a0]
    int v49;  // [bp-0x170]
    int v50;  // [bp-0x140]
    int v51;  // [bp-0x110]
    int flag7;  // [bp-0xe0]
    uint128_t flag5;  // [bp-0xd0]
    int flag6;  // [bp-0xc0]
    uint128_t flag3;  // [bp-0xb0]
    int flag4;  // [bp-0xa0]
    uint128_t flag2;  // [bp-0x90]
    int choice;  // [bp-0x80]
    uint128_t flag;  // [bp-0x70]
    char *v60;  // [bp-0x50]
    char v61;  // [bp+0x0]

    v60 = &v61;
    if (!(g_1fab5e9 & 1))
    {
        sub_f7d92c(&g_1ef3510);
        g_1fab5e9 = 1;
    }
    *((unsigned long long *)&(&v51)[32]) = 0;
    *((unsigned long long *)&(&v50)[32]) = 0;
    *((unsigned long long *)&(&v49)[32]) = 0;
    *((unsigned long long *)&(&v48)[32]) = 0;
    v47 = 0;
    v44 = 0;
    flag = 0;
    choice = 0;
    flag2 = 0;
    flag3 = 0;
    flag4 = 0;
    flag5 = 0;
    flag6 = 0;
    flag7 = 0;
    *((uint128_t *)&v51) = 0;
    *((uint128_t *)&(&v51)[16]) = 0;
    *((uint128_t *)&v50) = 0;
    *((uint128_t *)&(&v50)[16]) = 0;
    *((uint128_t *)&v49) = 0;
    *((uint128_t *)&(&v49)[16]) = 0;
    *((uint128_t *)&v48) = 0;
    *((uint128_t *)&(&v48)[16]) = 0;
    v45 = 0;
    v46 = 0;
    v42 = 0;
    v43 = 0;
    Time__get_time(0);
    MotionBlurComponent_FrameBlendingFilter__GetFrameRelative(a0, 4294967295);
    MotionBlurComponent_FrameBlendingFilter__GetFrameRelative(a0, 4294967294);
    MotionBlurComponent_FrameBlendingFilter__GetFrameRelative(a0, 4294967293);
    MotionBlurComponent_FrameBlendingFilter__GetFrameRelative(a0, 0xfffffffc);
    v62 = g_1ef3510;
    if (!g_1ef3510->field_e0)
    {
        sub_f7da5c(g_1ef3510);
        v62 = g_1ef3510;
    }
    RenderTargetIdentifier__op_Implicit(*((unsigned long long *)&choice), 0);
    memcpy(&v39, &v36, 16);
    v40 = v37;
    v41 = v38;
    if (a1)
    {
        memcpy(&v33, &v39, 16);
        v34 = v40;
        v35 = v41;
        CommandBuffer__SetGlobalTexture(a1, v62->field_b8->field_38, &v33, 0);
        RenderTargetIdentifier__op_Implicit(*((unsigned long long *)&flag4), 0);
        memcpy(&v30, &v36, 16);
        v31 = v37;
        v32 = v38;
        CommandBuffer__SetGlobalTexture(a1, g_1ef3510->field_b8->field_3c, &v30, 0);
        RenderTargetIdentifier__op_Implicit(*((unsigned long long *)&flag6), 0);
        memcpy(&v27, &v36, 16);
        v28 = v37;
        v29 = v38;
        CommandBuffer__SetGlobalTexture(a1, g_1ef3510->field_b8->field_40, &v27, 0);
        RenderTargetIdentifier__op_Implicit(*((unsigned long long *)&flag7), 0);
        memcpy(&v24, &v36, 16);
        v25 = v37;
        v26 = v38;
        CommandBuffer__SetGlobalTexture(a1, g_1ef3510->field_b8->field_44, &v24, 0);
        RenderTargetIdentifier__op_Implicit(*((unsigned long long *)(&choice + 8)), 0);
        memcpy(&v21, &v36, 16);
        v22 = v37;
        v23 = v38;
        CommandBuffer__SetGlobalTexture(a1, g_1ef3510->field_b8->field_48, &v21, 0);
        RenderTargetIdentifier__op_Implicit(*((unsigned long long *)(&flag4 + 8)), 0);
        memcpy(&v18, &v36, 16);
        v19 = v37;
        v20 = v38;
        CommandBuffer__SetGlobalTexture(a1, g_1ef3510->field_b8->field_4c, &v18, 0);
        RenderTargetIdentifier__op_Implicit(*((unsigned long long *)(&flag6 + 8)), 0);
        memcpy(&v15, &v36, 16);
        v16 = v37;
        v17 = v38;
        CommandBuffer__SetGlobalTexture(a1, g_1ef3510->field_b8->field_50, &v15, 0);
        RenderTargetIdentifier__op_Implicit(*((unsigned long long *)(&flag7 + 8)), 0);
        memcpy(&v12, &v36, 16);
        v13 = v37;
        v14 = v38;
        CommandBuffer__SetGlobalTexture(a1, g_1ef3510->field_b8->field_54, &v12, 0);
        MotionBlurComponent_FrameBlendingFilter_Frame__CalculateWeight(&choice);
        CommandBuffer__SetGlobalFloat(a1, g_1ef3510->field_b8->field_58, 0);
        MotionBlurComponent_FrameBlendingFilter_Frame__CalculateWeight(&flag4);
        CommandBuffer__SetGlobalFloat(a1, g_1ef3510->field_b8->field_5c, 0);
        MotionBlurComponent_FrameBlendingFilter_Frame__CalculateWeight(&flag6);
        CommandBuffer__SetGlobalFloat(a1, g_1ef3510->field_b8->field_60, 0);
        MotionBlurComponent_FrameBlendingFilter_Frame__CalculateWeight(&flag7);
        CommandBuffer__SetGlobalFloat(a1, g_1ef3510->field_b8->field_64, 0);
        v9 = (int)ptr->field_0;
        v10 = (int)ptr->field_10;
        v11 = ptr->field_20;
        CommandBuffer__SetGlobalTexture(a1, g_1ef3510->field_b8->field_10, &v9, 0);
        v38 = ptr->field_20;
        v36 = (int)ptr->field_0;
        v37 = (int)ptr->field_10;
        v8 = ptr3->field_20;
        v6 = (int)ptr3->field_0;
        v7 = (int)ptr3->field_10;
        if (a0->field_10)
        {
            p = &v50;
            addr = &v51;
            memcpy(&v51, &v6, 16);
            (&v51)[16] = v7;
            *((unsigned long *)&(&v51)[32]) = v8;
            v50 = v36;
            (&v50)[16] = v37;
            *((unsigned long *)&(&v50)[32]) = v38;
        }
        else
        {
            p = &v48;
            addr = &v49;
            memcpy(&v49, &v6, 16);
            (&v49)[16] = v7;
            *((unsigned long *)&(&v49)[32]) = v8;
            v48 = v36;
            (&v48)[16] = v37;
            *((unsigned long *)&(&v48)[32]) = v38;
        }
        v47 = addr->field_20;
        v45 = (int)addr->field_0;
        v46 = (int)addr->field_10;
        v44 = p->field_20;
        v42 = (int)p->field_0;
        v43 = (int)p->field_10;
        v3 = (int)p->field_0;
        v4 = (int)p->field_10;
        v5 = p->field_20;
        v0 = (int)addr->field_0;
        v1 = (int)addr->field_10;
        v2 = addr->field_20;
        v65 = CommandBuffer__Blit(a1, &v3, &v0, a4);
        return CommandBuffer__Blit(a1, &v3, &v0, a4);
    }
    sub_f7db74();
}
```

## `MotionBlurComponent.FrameBlendingFilter.PushFrame` — RVA `0xcd6e38`

- Decompiled symbol: `MotionBlurComponent_FrameBlendingFilter_PushFrame`
- Metadata signature: `public void PushFrame(CommandBuffer cb, RenderTargetIdentifier source, int width, int height, Material material) { }`
- Native interval: `288` bytes
- Result: `pseudocode`
- Heuristic layout hint: `MotionBlurComponent_FrameBlendingFilter_Recovered` matched 4 offsets against `MotionBlurComponent.FrameBlendingFilter` metadata (confidence 1.00).

```c
typedef struct MotionBlurComponent_FrameBlendingFilter_Recovered {
    char padding_0[16];
    char m_UseCompression;
    char padding_11[3];
    unsigned int m_RawTextureFormat;
    struct struct_0 *m_FrameList;
    unsigned int m_LastFrameCount;
} MotionBlurComponent_FrameBlendingFilter_Recovered;

typedef struct struct_0 {
    char padding_0[24];
    unsigned int field_18;
} struct_0;

typedef struct struct_2 {
    uint128_t field_0;
    uint128_t field_10;
    unsigned long long field_20;
} struct_2;

long long MotionBlurComponent_FrameBlendingFilter_PushFrame(struct_1 *p, long long a1, struct_2 *ptr, unsigned int a3, unsigned int a4, long long a5)
{
    unsigned long v9;  // x0
    struct_0 *addr;  // x8
    unsigned long v11;  // x10
    unsigned long v12;  // x9
    unsigned long v13;  // x0
    char v0;  // [bp-0xd0]
    int v1;  // [bp-0xc0]
    unsigned long v2;  // [bp-0xb0]
    char v3;  // [bp-0xa0]
    int v4;  // [bp-0x90]
    unsigned long v5;  // [bp-0x80]
    int v6;  // [bp-0x70]
    int v7;  // [bp-0x60]
    unsigned long v8;  // [bp-0x50]

    v9 = Time__get_frameCount(0);
    if ((unsigned int)v9 == p->field_20)
        return v9;
    addr = p->field_18;
    if (addr)
    {
        v11 = addr->field_18;
        v12 = (unsigned int)v9 - (unsigned int)v11 * (unsigned int)(v9 / v11);
        if (p->field_10)
        {
            v8 = ptr->field_20;
            v6 = (int)ptr->field_0;
            v7 = (int)ptr->field_10;
            if ((unsigned int)v11 > (unsigned int)v12)
            {
                memcpy(&v3, &v6, 16);
                v4 = v7;
                v5 = v8;
                v13 = MotionBlurComponent_FrameBlendingFilter_Frame__MakeRecord(32 + (char *)addr + 32 * (v12 * 0x100000000 >> 63 & 0xffffffff00000000 | v12 & 4294967295), a1, &v3, a3, a4, a5);
                p->field_20 = v9;
                return v13;
            }
        }
        else
        {
            v8 = ptr->field_20;
            v6 = (int)ptr->field_0;
            v7 = (int)ptr->field_10;
            if ((unsigned int)v11 > (unsigned int)v12)
            {
                memcpy(&v0, &v6, 16);
                v1 = v7;
                v2 = v8;
                v13 = MotionBlurComponent_FrameBlendingFilter_Frame__MakeRecordRaw(32 + (char *)addr + 32 * (v12 * 0x100000000 >> 63 & 0xffffffff00000000 | v12 & 4294967295), a1, &v0, a3, a4, p->field_14);
                p->field_20 = v9;
                return v13;
            }
        }
    }
    else
    {
        v9 = sub_f7db74();
    }
    sub_f7db7c(v9);
}
```

## `MotionBlurComponent.FrameBlendingFilter.CheckSupportCompression` — RVA `0xcd74b0`

- Decompiled symbol: `MotionBlurComponent_FrameBlendingFilter_CheckSupportCompression`
- Metadata signature: `private static bool CheckSupportCompression() { }`
- Native interval: `52` bytes
- Result: `pseudocode`

```c
unsigned long long MotionBlurComponent_FrameBlendingFilter_CheckSupportCompression(void)
{
    unsigned long long v0;  // x0

    if (!((char)SystemInfo__SupportsRenderTextureFormat(16, 0) & 1))
        return 0;
    if (SystemInfo__get_supportedRenderTargetCount(0) <= 1)
        v0 = 0;
    else
        v0 = 1;
    return v0;
}
```

## `MotionBlurComponent.FrameBlendingFilter.GetPreferredRenderTextureFormat` — RVA `0xcd74e4`

- Decompiled symbol: `MotionBlurComponent_FrameBlendingFilter_GetPreferredRenderTextureFormat`
- Metadata signature: `private static RenderTextureFormat GetPreferredRenderTextureFormat() { }`
- Native interval: `204` bytes
- Result: `pseudocode`

```c
extern long long g_1eee310;
extern long long g_1f05630;
extern char g_1fab5ea;

unsigned int MotionBlurComponent_FrameBlendingFilter_GetPreferredRenderTextureFormat(void)
{
    void* ptr;  // x19
    unsigned int v1;  // w8
    unsigned long i;  // x21

    if (!(g_1fab5ea & 1))
    {
        sub_f7d92c(&g_1eee310);
        sub_f7d92c(&g_1f05630);
        g_1fab5ea = 1;
    }
    ptr = sub_f7d9d4(g_1eee310, 3);
    RuntimeHelpers__InitializeArray(ptr, g_1f05630, 0);
    if (ptr)
    {
        v1 = (long long)ptr[24];
        if (v1 < 1)
            return 7;
        i = 0;
        do
        {
            if (v1 <= i)
            {
                sub_f7db7c();
                sub_f7db74();
            }
            if (((char)SystemInfo__SupportsRenderTextureFormat(*((int *)(32 + (char *)ptr + 4 * i)), 0) & 1))
                return *((int *)(32 + (char *)ptr + 4 * i));
            v1 = (int)ptr[24];
            i += 1;
        } while (i < v1);
        return 7;
    }
    sub_f7db74();
}
```

## `MotionBlurComponent.FrameBlendingFilter.GetFrameRelative` — RVA `0xcd7ae0`

- Decompiled symbol: `MotionBlurComponent_FrameBlendingFilter_GetFrameRelative`
- Metadata signature: `private MotionBlurComponent.FrameBlendingFilter.Frame GetFrameRelative(int offset) { }`
- Native interval: `100` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[24];
    struct struct_0 *field_18;
} struct_1;

typedef struct struct_0 {
    char padding_0[24];
    unsigned int field_18;
} struct_0;

int MotionBlurComponent_FrameBlendingFilter_GetFrameRelative(struct_1 *p, unsigned int a1)
{
    unsigned long v0;  // x0
    struct_0 *addr;  // x8
    unsigned long v2;  // x10
    unsigned long v3;  // x9
    uint128_t ptr3[4];  // x8
    uint128_t v5;  // q0
    uint128_t ptr[2];  // x8

    v0 = Time__get_frameCount(0);
    addr = p->field_18;
    if (addr)
    {
        v2 = addr->field_18;
        v3 = (unsigned int)v0 + a1 + (unsigned int)v2 - (unsigned int)v2 * (unsigned int)((v0 + a1 + v2) / v2);
        if ((unsigned int)v2 > (unsigned int)v3)
        {
            ptr3 = (char *)addr + 32 * (v3 * 0x100000000 >> 63 & 0xffffffff00000000 | v3 & 4294967295);
            v5 = ptr3[3];
            ptr[0] = ptr3[2];
            ptr[1] = v5;
            return v0;
        }
    }
    else
    {
        v0 = sub_f7db74();
    }
    sub_f7db7c(v0);
}
```
