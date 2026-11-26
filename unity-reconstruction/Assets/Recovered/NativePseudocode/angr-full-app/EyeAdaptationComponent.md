# Native pseudocode: EyeAdaptationComponent

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `EyeAdaptationComponent.get_active` — RVA `0xcd3690`

- Decompiled symbol: `EyeAdaptationComponent_get_active`
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
} struct_1;

typedef struct struct_0 {
    char padding_0[48];
    char field_30;
} struct_0;

extern long long g_1efa0f8;
extern char g_1fab5cc;

unsigned long long EyeAdaptationComponent_get_active(struct_2 *a0)
{
    unsigned long long v0;  // x0

    if (!(g_1fab5cc & 1))
    {
        sub_f7d92c(&g_1efa0f8);
        g_1fab5cc = 1;
    }
    if (a0->field_18)
    {
        if (!(a0->field_18->field_10 && ((char)SystemInfo__get_supportsComputeShaders(0) & 1)))
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

## `EyeAdaptationComponent.ResetHistory` — RVA `0xcd3704`

- Decompiled symbol: `EyeAdaptationComponent_ResetHistory`
- Metadata signature: `public void ResetHistory() { }`
- Native interval: `12` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[80];
    char field_50;
} struct_0;

struct_0 * EyeAdaptationComponent_ResetHistory(struct_0 *ptr)
{
    ptr->field_50 = 1;
    return ptr;
}
```

## `EyeAdaptationComponent.OnEnable` — RVA `0xcd3710`

- Decompiled symbol: `EyeAdaptationComponent_OnEnable`
- Metadata signature: `public override void OnEnable() { }`
- Native interval: `12` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[80];
    char field_50;
} struct_0;

struct_0 * EyeAdaptationComponent_OnEnable(struct_0 *ptr)
{
    ptr->field_50 = 1;
    return ptr;
}
```

## `EyeAdaptationComponent.OnDisable` — RVA `0xcd371c`

- Decompiled symbol: `EyeAdaptationComponent_OnDisable`
- Metadata signature: `public override void OnDisable() { }`
- Native interval: `252` bytes
- Result: `pseudocode`
- Heuristic layout hint: `EyeAdaptationComponent_Recovered` matched 3 offsets against `EyeAdaptationComponent` metadata (confidence 1.00).

```c
typedef struct EyeAdaptationComponent_Recovered {
    char padding_0[40];
    long long m_HistogramBuffer;
    void* m_AutoExposurePool;
    char padding_38[16];
    long long m_DebugHistogram;
} EyeAdaptationComponent_Recovered;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab5cd;

void EyeAdaptationComponent_OnDisable(struct_1 *ptr)
{
    unsigned long long v5;  // x30
    unsigned long long v6;  // x22
    unsigned long long v7;  // x21
    unsigned long long v8;  // x20
    unsigned long long v9;  // x19
    void* p;  // x20
    unsigned long v11;  // x21
    unsigned int v12;  // w8
    struct_1 *addr;  // x19
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
    if (!(g_1fab5cd & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab5cd = 1;
    }
    p = ptr->field_30;
    if (p)
    {
        if ((int)(long long)p[24] >= 1)
        {
            v11 = 0;
            v12 = (long long)p[24];
            do
            {
                if (v12 <= v11)
                {
                    sub_f7db7c();
                    goto LABEL_10d3814;
                }
            } while ((GraphicsUtils__Destroy(*((long long *)(32 + (char *)p + 8 * v11)), 0), v12 = (unsigned int)(int)p[24], v11 = (unsigned long)(v11 + 1), v11 < (unsigned long long)v12));
        }
        if (ptr->field_28)
            ComputeBuffer__Release(ptr->field_28, 0);
        ptr->field_28 = 0;
        sub_f7d8d0((struct EyeAdaptationComponent_Recovered *)&ptr->field_28, 0);
        addr = &ptr->field_48;
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        if (((char)Object__op_Inequality(ptr->field_48, 0, 0) & 1))
        {
            if (!*((long long *)&addr->padding_0[0]))
                goto LABEL_10d3814;
            RenderTexture__Release(*((long long *)&addr->padding_0[0]), 0);
        }
        *((long long *)&addr->padding_0[0]) = 0;
        sub_f7d8d0();
        return;
    }
LABEL_10d3814:
    sub_f7db74();
}
```

## `EyeAdaptationComponent.GetHistogramScaleOffsetRes` — RVA `0xcd3818`

- Decompiled symbol: `EyeAdaptationComponent_GetHistogramScaleOffsetRes`
- Metadata signature: `private Vector4 GetHistogramScaleOffsetRes() { }`
- Native interval: `192` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    long long field_10;
    unsigned long long field_18;
} struct_0;

extern long long g_1efa0f8;
extern char g_1fab5ce;

long long EyeAdaptationComponent_GetHistogramScaleOffsetRes(struct_0 *a0, unsigned long a1)
{
    unsigned long long v8;  // d11
    unsigned long long v9;  // d10
    unsigned long long v10;  // d9
    unsigned long long v11;  // d8
    unsigned long long v12;  // x30
    unsigned long long v13;  // x21
    unsigned long long v14;  // x20
    unsigned long long v15;  // x19
    unsigned long long v0;  // [bp-0x40]
    unsigned long long v1;  // [bp-0x38]
    unsigned long long v2;  // [bp-0x30]
    unsigned long long v3;  // [bp-0x28]
    unsigned long long v4;  // [bp-0x20]
    unsigned long long v5;  // [bp-0x18]
    unsigned long long v6;  // [bp-0x10]
    unsigned long long v7;  // [bp-0x8]

    v0 = v8;
    v1 = v9;
    v2 = v10;
    v3 = v11;
    v4 = v12;
    v5 = v13;
    v6 = v14;
    v7 = v15;
    if (!(g_1fab5ce & 1))
    {
        sub_f7d92c(&g_1efa0f8);
        g_1fab5ce = 1;
    }
    if (a0->field_18 && a0->field_10)
        PostProcessingContext__get_width(a0->field_10, 0); /* do not return */
    sub_f7db74();
}
```

## `EyeAdaptationComponent.Prepare` — RVA `0xcd38d8`

- Decompiled symbol: `EyeAdaptationComponent_Prepare`
- Metadata signature: `public Texture Prepare(RenderTexture source, Material uberMaterial) { }`
- Native interval: `2744` bytes
- Result: `pseudocode`
- Heuristic layout hint: `EyeAdaptationComponent_Recovered` matched 2 offsets against `EyeAdaptationComponent` metadata (confidence 1.00).

```c
typedef struct struct_5 {
    char padding_0[16];
    struct EyeAdaptationComponent_Recovered *field_10;
    struct struct_6 *field_18;
    long long field_20;
    long long field_28;
    struct struct_4 *field_30;
} struct_5;

typedef struct struct_9 {
    char padding_0[376];
    struct struct_10 *field_178;
    unsigned long long field_180;
} struct_9;

typedef struct struct_12 {
    struct struct_11 *field_0;
    char padding_8[16];
    unsigned int field_18;
    char padding_1c[4];
    unsigned long long field_20;
    unsigned long long field_28;
} struct_12;

typedef struct EyeAdaptationComponent_Recovered {
    char padding_0[32];
    long long m_EyeCompute;
    unsigned long long m_HistogramBuffer;
} EyeAdaptationComponent_Recovered;

typedef struct struct_6 {
    char padding_0[36];
    unsigned int field_24;
    char padding_28[4];
    unsigned int field_2c;
} struct_6;

typedef struct struct_4 {
    struct struct_3 *field_0;
    char padding_8[16];
    unsigned int field_18;
    char padding_1c[4];
    long long field_20;
    long long field_28;
} struct_4;

typedef struct struct_10 {
    unsigned long long field_0;
} struct_10;

typedef struct struct_11 {
    char padding_0[64];
    unsigned long long field_40;
} struct_11;

typedef struct struct_3 {
    char padding_0[64];
    long long field_40;
} struct_3;

typedef struct struct_8 {
    char padding_0[224];
    unsigned int field_e0;
} struct_8;

extern long long g_1eee3f8;
extern long long g_1eee870;
extern long long g_1eeefc0;
extern struct_8 *g_1ef0c58;
extern long long g_1ef1298;
extern long long g_1ef30d8;
extern long long g_1efa0f8;
extern long long g_1f00c30;
extern long long g_1f08300;
extern unsigned long long g_1f0a290;
extern long long g_1f0aa70;
extern long long g_1f0bad8;
extern long long g_1f0d9f8;
extern long long g_1f10540;
extern long long g_1f10818;
extern long long g_1f10890;
extern char g_1fab5cf;

void EyeAdaptationComponent_Prepare(struct_5 *ptr, long long a1)
{
    unsigned long long v27;  // d15
    unsigned long long v28;  // d14
    unsigned long long v37;  // x27
    unsigned long long v38;  // x26
    unsigned long long v39;  // x25
    unsigned long long v40;  // x24
    unsigned long long v41;  // x23
    unsigned long long v42;  // x22
    unsigned long long v43;  // x21
    unsigned long long v44;  // x20
    unsigned long long v45;  // x19
    unsigned int p[12];  // x8
    unsigned long long v29;  // d13
    struct_5 *v47;  // x23
    unsigned int v48;  // s9
    unsigned int v49;  // w26
    struct_5 *addr;  // x23
    long long v51;  // x0
    long long v52;  // x1
    struct_5 *v53;  // x22
    struct_5 *ptr3;  // x22
    long long v55;  // x24
    unsigned int v56;  // s1
    unsigned long long v30;  // d12
    unsigned int v57;  // s2
    unsigned int v58;  // 4107
    unsigned long v59;  // 4134
    unsigned int v60;  // s3
    unsigned int v61;  // 4104
    unsigned long v62;  // 4121
    unsigned long long flag2;  // x6
    unsigned long long flag3;  // x7
    unsigned long long v65;  // x5
    struct_9 **v66;  // x24
    unsigned long long v31;  // d11
    unsigned long v67;  // x0
    struct_12 *v68;  // x8
    struct_12 *v69;  // x8
    struct_12 *ptr4;  // x25
    long long v71;  // x26
    struct_12 *v72;  // x8
    struct_12 *v73;  // x8
    struct_12 *ptr5;  // x25
    long long v75;  // x26
    unsigned int v76;  // w0
    unsigned long long v32;  // d10
    unsigned int v77;  // w25
    struct_9 **v78;  // x3
    unsigned long long flag;  // x4
    unsigned long long choice;  // x2
    unsigned int v81;  // s0
    struct_9 **v82;  // x0
    unsigned long v83;  // x1
    unsigned long long v33;  // d9
    unsigned long long v34;  // d8
    unsigned long long v35;  // x30
    unsigned long long v36;  // x28
    unsigned long v0;  // [bp-0xd0]
    unsigned long long flag4;  // [bp-0xc8]
    unsigned int v2;  // [bp-0xb8]
    unsigned int v3;  // [bp-0xb4]
    unsigned int v4;  // [bp-0xb0]
    unsigned int v5;  // [bp-0xac]
    unsigned long long v6;  // [bp-0xa0]
    unsigned long long v7;  // [bp-0x98]
    unsigned long long v8;  // [bp-0x90]
    unsigned long long v9;  // [bp-0x88]
    unsigned long long v10;  // [bp-0x80]
    unsigned long long v11;  // [bp-0x78]
    unsigned long long v12;  // [bp-0x70]
    unsigned long long v13;  // [bp-0x68]
    char *v14;  // [bp-0x60]
    unsigned long long v15;  // [bp-0x58]
    unsigned long long v16;  // [bp-0x50]
    unsigned long long v17;  // [bp-0x48]
    unsigned long long v18;  // [bp-0x40]
    unsigned long long v19;  // [bp-0x38]
    unsigned long long v20;  // [bp-0x30]
    unsigned long long v21;  // [bp-0x28]
    unsigned long long v22;  // [bp-0x20]
    unsigned long long v23;  // [bp-0x18]
    unsigned long long v24;  // [bp-0x10]
    unsigned long long v25;  // [bp-0x8]
    char v26;  // [bp+0x0]

    v6 = v27;
    v7 = v28;
    v8 = v29;
    v9 = v30;
    v10 = v31;
    v11 = v32;
    v12 = v33;
    v13 = v34;
    v14 = &v26;
    v15 = v35;
    v16 = v36;
    v17 = v37;
    v18 = v38;
    v19 = v39;
    v20 = v40;
    v21 = v41;
    v22 = v42;
    v23 = v43;
    v24 = v44;
    v25 = v45;
    if (!(g_1fab5cf & 1))
    {
        sub_f7d92c(&g_1eee870);
        sub_f7d92c(&g_1eeefc0);
        sub_f7d92c("e:");
        sub_f7d92c("g=");
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c(&g_1efa0f8);
        sub_f7d92c(&g_1ef1298);
        sub_f7d92c(&g_1f00c30);
        sub_f7d92c(&g_1eee3f8);
        sub_f7d92c(&g_1ef30d8);
        sub_f7d92c(&g_1f0aa70);
        sub_f7d92c(&g_1f08300);
        sub_f7d92c(&g_1f0d9f8);
        sub_f7d92c(&g_1f10818);
        sub_f7d92c(&g_1f0a290);
        sub_f7d92c(&g_1f0bad8);
        sub_f7d92c(&g_1f10890);
        sub_f7d92c(&g_1f10540);
        g_1fab5cf = 1;
    }
    p = ptr->field_18;
    if (p)
    {
        v47 = ptr;
        v48 = p[9];
        v49 = p[11];
        addr = &v47->field_20;
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        if (((char)Object__op_Equality(v47->field_20, 0, 0) & 1))
        {
            v51 = sub_11328ac(g_1f0d9f8, g_1f00c30);
            *((long long *)&addr->padding_0[0]) = v51;
            sub_f7d8d0(addr, v51);
        }
        if (ptr->field_10 && ptr->field_10->field_20 && MaterialFactory__Get(ptr->field_10->field_20, g_1f0aa70, 0))
        {
            v52 = 0;
            Material__set_shaderKeywords();
            v53 = ptr;
            ptr3 = &v53->field_28;
            if (!v53->field_28)
            {
                v55 = sub_f7db70(g_1eeefc0);
                ComputeBuffer__ctor(v55, 64, 4, 0);
                v52 = v55;
                *((long long *)&ptr3->padding_0[0]) = v52;
                sub_f7d8d0(ptr3, v52);
            }
            if (!g_1eef898->field_b8->field_0)
            {
                v52 = sub_f7d9d4(g_1eee3f8, 64);
                g_1eef898->field_b8->field_0 = v52;
                sub_f7d8d0(g_1eef898->field_b8, v52);
            }
            EyeAdaptationComponent__GetHistogramScaleOffsetRes(ptr, v52);
            v5 = v56;
            if (ptr->field_10 && a1 && !((v2 = v49, RenderTexture__get_format(a1, 0), !ptr->field_10->field_28)))
            {
                v58 = CmpF(v57, 0x7f800000);
                v59 = (((CmpF(v57, 0x7f800000) >> 5 & 3 | CmpF(v57, 0x7f800000) & 1) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1;
                v61 = CmpF(v60, 0x7f800000);
                v62 = (((CmpF(v60, 0x7f800000) >> 5 & 3 | CmpF(v60, 0x7f800000) & 1) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1;
                flag2 = 1;
                flag3 = 1;
                v65 = 0;
                v0 = g_1f0a290;
                flag4 = 0;
                v66 = RenderTextureFactory__Get();
                if (!g_1eefbb8->field_e0)
                    sub_f7da5c(g_1eefbb8);
                v67 = Graphics__Blit(a1, v66, 0);
                v68 = ptr->field_30;
                if (v68)
                {
                    if (!v68->field_18)
                        goto LABEL_10d4380;
                    if (!g_1ef0c58->field_e0)
                        sub_f7da5c(g_1ef0c58);
                    v67 = Object__op_Equality(v68->field_20, 0, 0);
                    if (!((char)v67 & 1))
                    {
                        v69 = ptr->field_30;
                        if (v69)
                        {
                            if (!v69->field_18)
                                goto LABEL_10d4380;
                            if (v69->field_20)
                            {
                                v67 = RenderTexture__IsCreated(v69->field_20, 0);
                                if ((v67 & 1))
                                    goto LABEL_10d3cb8;
                                goto LABEL_10d3c5c;
                            }
                        }
                    }
                    else
                    {
LABEL_10d3c5c:
                        ptr4 = ptr->field_30;
                        v65 = 0;
                        v71 = sub_f7db70(g_1ef1298);
                        v67 = RenderTexture__ctor(v71, 1, 1, 0, 14, 0);
                        if (ptr4)
                        {
                            if (v71 && (v67 = (unsigned long)sub_f7da60(v71, ptr4->field_0->field_40), !v67))
                                goto LABEL_10d4384;
                            if (!ptr4->field_18)
                                goto LABEL_10d4380;
                            ptr4->field_20 = v71;
                            v67 = sub_f7d8d0((struct struct_12 *)&ptr4->field_20, v71);
LABEL_10d3cb8:
                            v72 = ptr->field_30;
                            if (v72)
                            {
                                if (v72->field_18 <= 1)
                                    goto LABEL_10d4380;
                                if (!g_1ef0c58->field_e0)
                                    sub_f7da5c(g_1ef0c58);
                                v67 = Object__op_Equality(v72->field_28, 0, 0);
                                if (!((char)v67 & 1))
                                {
                                    v73 = ptr->field_30;
                                    if (v73)
                                    {
                                        if (v73->field_18 <= 1)
                                            goto LABEL_10d4380;
                                        if (v73->field_28)
                                        {
                                            if ((RenderTexture__IsCreated(v73->field_28, 0) & 1))
                                                goto LABEL_10d3d7c;
                                            goto LABEL_10d3d1c;
                                        }
                                    }
                                }
                                else
                                {
LABEL_10d3d1c:
                                    ptr5 = ptr->field_30;
                                    v65 = 0;
                                    v75 = sub_f7db70(g_1ef1298);
                                    v67 = RenderTexture__ctor(v75, 1, 1, 0, 14, 0);
                                    if (ptr5)
                                    {
                                        if (v75 && (v67 = (unsigned long)sub_f7da60(v75, ptr5->field_0->field_40), !v67))
                                            goto LABEL_10d4384;
                                        if (ptr5->field_18 <= 1)
                                            goto LABEL_10d4380;
                                        ptr5->field_28 = v75;
                                        sub_f7d8d0((struct struct_12 *)&ptr5->field_28, v75);
LABEL_10d3d7c:
                                        if (*((long long *)&ptr3->padding_0[0]))
                                        {
                                            ComputeBuffer__SetData(*((long long *)&ptr3->padding_0[0]), g_1eef898->field_b8->field_0, 0);
                                            if (*((long long *)&addr->padding_0[0]))
                                            {
                                                v76 = ComputeShader__FindKernel(*((long long *)&addr->padding_0[0]), g_1f0bad8, 0);
                                                if (*((long long *)&addr->padding_0[0]))
                                                {
                                                    v77 = v76;
                                                    ComputeShader__SetBuffer(*((long long *)&addr->padding_0[0]), v77, g_1f10540, *((long long *)&ptr3->padding_0[0]), 0);
                                                    if (*((long long *)&addr->padding_0[0]))
                                                    {
                                                        v78 = v66;
                                                        flag = 0;
                                                        ComputeShader__SetTexture(*((long long *)&addr->padding_0[0]), v77, g_1f10890, v66, 0);
                                                        if (*((long long *)&addr->padding_0[0]))
                                                        {
                                                            v4 = v48;
                                                            choice = 0;
                                                            v3 = v81;
                                                            ComputeShader__SetVector(*((long long *)&addr->padding_0[0]), g_1f10818, 0);
                                                            if (v66)
                                                            {
                                                                v82 = v66;
                                                                v83 = *(v66)->field_180;
                                                                *(v66)->field_178();
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    v67 = sub_f7db74();
LABEL_10d4380:
    v67 = sub_f7db7c(v67);
LABEL_10d4384:
    sub_f7da4c(sub_f7db98(v67), 0);
}
```

## `EyeAdaptationComponent.OnGUI` — RVA `0xcd4390`

- Decompiled symbol: `EyeAdaptationComponent_OnGUI`
- Metadata signature: `public void OnGUI() { }`
- Native interval: `340` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab5d0;

long long EyeAdaptationComponent_OnGUI(unsigned long long *ptr)
{
    long long v0;  // x0
    unsigned long v1;  // x0
    long long v2;  // x0

    if (!(g_1fab5d0 & 1))
    {
        sub_f7d92c("O<");
        sub_f7d92c(&g_1ef0c58);
        g_1fab5d0 = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v0 = Object__op_Equality(ptr[9], 0, 0);
    if (((char)v0 & 1))
        return v0;
    v1 = ptr[9];
    if (v1)
    {
        v2 = RenderTexture__IsCreated(v1, 0);
        if (!((char)v2 & 1))
            return v2;
        v1 = ptr[2];
        if (v1)
            PostProcessingContext__get_viewport(v1, 0); /* do not return */
    }
    sub_f7db74(v1);
}
```

## `EyeAdaptationComponent.ctor` — RVA `0xcd44e4`

- Decompiled symbol: `EyeAdaptationComponent_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `136` bytes
- Result: `pseudocode`
- Heuristic layout hint: `EyeAdaptationComponent_Recovered` matched 2 offsets against `EyeAdaptationComponent` metadata (confidence 1.00).

```c
typedef struct EyeAdaptationComponent_Recovered {
    char padding_0[48];
    long long m_AutoExposurePool;
    char padding_38[24];
    char m_FirstFrame;
} EyeAdaptationComponent_Recovered;

extern long long g_1eee308;
extern long long g_1efa098;
extern char g_1fab5d1;

void EyeAdaptationComponent_ctor(struct_0 *ptr)
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
    if (!(g_1fab5d1 & 1))
    {
        sub_f7d92c(&g_1efa098);
        sub_f7d92c(&g_1eee308);
        g_1fab5d1 = 1;
    }
    v10 = sub_f7d9d4(g_1eee308, 2);
    ptr->field_30 = v10;
    sub_f7d8d0((struct EyeAdaptationComponent_Recovered *)&ptr->field_30, v10);
    ptr->field_50 = 1;
}
```
