# Native pseudocode: ScreenSpaceReflectionComponent

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `ScreenSpaceReflectionComponent.GetCameraFlags` — RVA `0xcd7c2c`

- Decompiled symbol: `ScreenSpaceReflectionComponent_GetCameraFlags`
- Metadata signature: `public override DepthTextureMode GetCameraFlags() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
unsigned int ScreenSpaceReflectionComponent_GetCameraFlags(void)
{
    return 1;
}
```

## `ScreenSpaceReflectionComponent.get_active` — RVA `0xcd7c34`

- Decompiled symbol: `ScreenSpaceReflectionComponent_get_active`
- Metadata signature: `public override bool get_active() { }`
- Native interval: `124` bytes
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

extern long long g_1efa118;
extern char g_1fab5f0;

unsigned long long ScreenSpaceReflectionComponent_get_active(struct_2 *a0)
{
    unsigned long long v0;  // x0

    if (!(g_1fab5f0 & 1))
    {
        sub_f7d92c(&g_1efa118);
        g_1fab5f0 = 1;
    }
    if (a0->field_18)
    {
        if (!a0->field_18->field_10)
        {
            return 0;
        }
        else if (a0->field_10)
        {
            if (!((char)PostProcessingContext__get_isGBufferAvailable(a0->field_10, 0) & 1))
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
    }
    sub_f7db74();
}
```

## `ScreenSpaceReflectionComponent.OnEnable` — RVA `0xcd7cb0`

- Decompiled symbol: `ScreenSpaceReflectionComponent_OnEnable`
- Metadata signature: `public override void OnEnable() { }`
- Native interval: `328` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[40];
    struct struct_1 *field_28;
} struct_0;

typedef struct struct_1 {
    char padding_0[24];
    unsigned int field_18;
    char padding_1c[4];
    unsigned int field_20;
    unsigned int field_24;
    unsigned int field_28;
    unsigned int field_2c;
    unsigned int field_30;
} struct_1;

extern char g_1fab5f1;

long long ScreenSpaceReflectionComponent_OnEnable(struct_0 *ptr)
{
    unsigned int p[13];  // x21
    unsigned long v1;  // x0
    unsigned int addr[13];  // x20
    unsigned int ptr3[13];  // x20
    unsigned int ptr4[13];  // x20
    unsigned int ptr5[13];  // x19

    if (!(g_1fab5f1 & 1))
    {
        sub_f7d92c("s)");
        sub_f7d92c("y)");
        sub_f7d92c("{)");
        sub_f7d92c("u)");
        sub_f7d92c("w)");
        g_1fab5f1 = 1;
    }
    p = ptr->field_28;
    v1 = Shader__PropertyToID(g_1f107b8, 0);
    if (!p)
    {
LABEL_10d7df0:
        v1 = sub_f7db74();
    }
    else if (p[6])
    {
        p[8] = v1;
        addr = ptr->field_28;
        v1 = Shader__PropertyToID(g_1f107c0, 0);
        if (!addr)
            goto LABEL_10d7df0;
        if (addr[6] > 1)
        {
            addr[9] = v1;
            ptr3 = ptr->field_28;
            v1 = Shader__PropertyToID(g_1f107c8, 0);
            if (!ptr3)
                goto LABEL_10d7df0;
            if (ptr3[6] > 2)
            {
                ptr3[10] = v1;
                ptr4 = ptr->field_28;
                v1 = Shader__PropertyToID(g_1f107d0, 0);
                if (!ptr4)
                    goto LABEL_10d7df0;
                if (ptr4[6] > 3)
                {
                    ptr4[11] = v1;
                    ptr5 = ptr->field_28;
                    v1 = Shader__PropertyToID(g_1f107d8, 0);
                    if (!ptr5)
                        goto LABEL_10d7df0;
                    if (ptr5[6] > 4)
                    {
                        ptr5[12] = v1;
                        return v1;
                    }
                }
            }
        }
    }
    sub_f7db7c(v1);
}
```

## `ScreenSpaceReflectionComponent.GetName` — RVA `0xcd7df8`

- Decompiled symbol: `ScreenSpaceReflectionComponent_GetName`
- Metadata signature: `public override string GetName() { }`
- Native interval: `64` bytes
- Result: `pseudocode`

```c
extern unsigned long long g_1f0d810;
extern char g_1fab5f2;

long long ScreenSpaceReflectionComponent_GetName(void)
{
    if (!(g_1fab5f2 & 1))
    {
        sub_f7d92c(&g_1f0d810);
        g_1fab5f2 = 1;
    }
    return g_1f0d810;
}
```

## `ScreenSpaceReflectionComponent.GetCameraEvent` — RVA `0xcd7e38`

- Decompiled symbol: `ScreenSpaceReflectionComponent_GetCameraEvent`
- Metadata signature: `public override CameraEvent GetCameraEvent() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
unsigned int ScreenSpaceReflectionComponent_GetCameraEvent(void)
{
    return 9;
}
```

## `ScreenSpaceReflectionComponent.PopulateCommandBuffer` — RVA `0xcd7e40`

- Decompiled symbol: `ScreenSpaceReflectionComponent_PopulateCommandBuffer`
- Metadata signature: `public override void PopulateCommandBuffer(CommandBuffer cb) { }`
- Native interval: `4100` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[16];
    struct struct_0 *field_10;
    struct struct_2 *field_18;
} struct_1;

typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

typedef struct struct_2 {
    char padding_0[24];
    unsigned int field_18;
    char padding_1c[4];
    unsigned int field_20;
} struct_2;

extern long long g_1ef3920;
extern long long g_1efa118;
extern long long g_1f0aaa0;
extern char g_1fab5f3;

long long ScreenSpaceReflectionComponent_PopulateCommandBuffer(struct_1 *ptr, long long a1)
{
    unsigned int v51[9];  // x8
    long long v52;  // x22
    unsigned int v53;  // w0
    unsigned int v55;  // w26
    unsigned long long v56;  // x0
    unsigned int v0;  // [bp-0x744]
    long long v1;  // [bp-0x740], Other Possible Types: unsigned long
    unsigned int v2;  // [bp-0x734]
    char v3;  // [bp-0x730]
    uint128_t v4;  // [bp-0x720]
    unsigned long long v5;  // [bp-0x710]
    int v6;  // [bp-0x700]
    uint128_t v7;  // [bp-0x6f0]
    unsigned long long v8;  // [bp-0x6e0]
    char v9;  // [bp-0x6d0]
    uint128_t v10;  // [bp-0x6c0]
    unsigned long long v11;  // [bp-0x6b0]
    int v12;  // [bp-0x6a0]
    uint128_t v13;  // [bp-0x690]
    unsigned long long v14;  // [bp-0x680]
    char v15;  // [bp-0x670]
    uint128_t v16;  // [bp-0x660]
    unsigned long long v17;  // [bp-0x650]
    int v18;  // [bp-0x640]
    uint128_t v19;  // [bp-0x630]
    unsigned long long v20;  // [bp-0x620]
    int v21;  // [bp-0x470]
    uint128_t v22;  // [bp-0x460]
    unsigned long long v23;  // [bp-0x450]
    int v24;  // [bp-0x3e0]
    uint128_t v25;  // [bp-0x3d0]
    unsigned long long v26;  // [bp-0x3c0]
    int v27;  // [bp-0x350]
    uint128_t v28;  // [bp-0x340]
    unsigned long long v29;  // [bp-0x330]
    int v30;  // [bp-0x1e0]
    uint128_t v31;  // [bp-0x1d0]
    unsigned long long v32;  // [bp-0x1c0]
    uint128_t flag15;  // [bp-0x1a0]
    uint128_t flag14;  // [bp-0x190]
    uint128_t flag13;  // [bp-0x180]
    uint128_t flag12;  // [bp-0x170]
    uint128_t flag11;  // [bp-0x160]
    uint128_t flag10;  // [bp-0x150]
    uint128_t flag9;  // [bp-0x140]
    uint128_t flag8;  // [bp-0x130]
    uint128_t flag7;  // [bp-0x120]
    uint128_t flag6;  // [bp-0x110]
    uint128_t flag5;  // [bp-0x100]
    uint128_t flag4;  // [bp-0xf0]
    uint128_t flag3;  // [bp-0xe0]
    uint128_t flag2;  // [bp-0xd0]
    uint128_t choice;  // [bp-0xc0]
    uint128_t flag;  // [bp-0xb0]
    char *v49;  // [bp-0x60]
    char v50;  // [bp+0x0]

    v49 = &v50;
    if (!(g_1fab5f3 & 1))
    {
        sub_f7d92c(&g_1efa118);
        sub_f7d92c(&g_1ef3920);
        sub_f7d92c(&g_1f0aaa0);
        g_1fab5f3 = 1;
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
    v51 = ptr->field_18;
    if (v51 && ptr->field_10)
    {
        v1 = ptr->field_10->field_18;
        PostProcessingContext__get_width(); /* do not return */
    }
    sub_f7db74();
    if (v51[6])
    {
        RenderTargetIdentifier__op_Implicit(v51[8], 0);
        v32 = v29;
        v30 = v27;
        v31 = v28;
        RenderTargetIdentifier__op_Implicit(v2, 0);
        memcpy(&v15, &v27, 16);
        v16 = v28;
        v17 = v29;
        v18 = v30;
        v19 = v31;
        v20 = v32;
        CommandBuffer__Blit(a1, &v18, &v15, v52, 3, 0);
        v53 = Camera__get_pixelWidth(v1, 0);
        CommandBuffer__GetTemporaryRT(a1, v0, v53, Camera__get_pixelHeight(v1, 0) & 4294967295, 0, 1, v55, 0);
        RenderTargetIdentifier__op_Implicit(2, 0);
        v29 = v26;
        v27 = v24;
        v28 = v25;
        RenderTargetIdentifier__op_Implicit(v0, 0);
        memcpy(&v9, &v24, 16);
        v10 = v25;
        v11 = v26;
        v12 = v27;
        v13 = v28;
        v14 = v29;
        CommandBuffer__Blit(a1, &v12, &v9, v52, 1, 0);
        RenderTargetIdentifier__op_Implicit(v0, 0);
        v26 = v23;
        v24 = v21;
        v25 = v22;
        RenderTargetIdentifier__op_Implicit(2, 0);
        memcpy(&v3, &v21, 16);
        v4 = v22;
        v5 = v23;
        v6 = v24;
        v7 = v25;
        v8 = v26;
        CommandBuffer__Blit(a1, &v6, &v3, 0);
        v56 = CommandBuffer__ReleaseTemporaryRT(a1, v0, 0);
        return CommandBuffer__ReleaseTemporaryRT(a1, v0, 0);
    }
    sub_f7db7c();
}
```

## `ScreenSpaceReflectionComponent.ctor` — RVA `0xcd8e44`

- Decompiled symbol: `ScreenSpaceReflectionComponent_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `140` bytes
- Result: `pseudocode`
- Heuristic layout hint: `ScreenSpaceReflectionComponent_Recovered` matched 3 offsets against `ScreenSpaceReflectionComponent` metadata (confidence 1.00).

```c
typedef struct ScreenSpaceReflectionComponent_Recovered {
    char padding_0[33];
    char k_TraceBehindObjects;
    char padding_22[1];
    char k_BilateralUpsample;
    char padding_24[4];
    long long m_ReflectionTextures;
} ScreenSpaceReflectionComponent_Recovered;

extern long long g_1efa060;
extern char g_1fab5f4;

void ScreenSpaceReflectionComponent_ctor(struct_0 *ptr)
{
    unsigned long long v5;  // x30
    unsigned long long v6;  // x22
    unsigned long long v7;  // x21
    unsigned long long v8;  // x20
    unsigned long long v9;  // x19
    long long v10;  // x1
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
    if (!(g_1fab5f4 & 1))
    {
        sub_f7d92c("a(");
        sub_f7d92c(&g_1efa060);
        g_1fab5f4 = 1;
    }
    ptr->field_21 = 1;
    ptr->field_23 = 1;
    v10 = sub_f7d9d4(g_1eee1f8, 5);
    ptr->field_28 = v10;
    sub_f7d8d0((struct ScreenSpaceReflectionComponent_Recovered *)&ptr->field_28, v10);
    sub_15689ec();
    return;
}
```
