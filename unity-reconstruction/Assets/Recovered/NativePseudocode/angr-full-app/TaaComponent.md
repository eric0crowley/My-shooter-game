# Native pseudocode: TaaComponent

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `TaaComponent.get_active` — RVA `0xcd9530`

- Decompiled symbol: `TaaComponent_get_active`
- Metadata signature: `public override bool get_active() { }`
- Native interval: `144` bytes
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

extern long long g_1efa0c0;
extern char g_1fab5f6;

unsigned long long TaaComponent_get_active(struct_2 *ptr)
{
    struct_1 *v0;  // x8
    unsigned long long v1;  // x0

    if (!(g_1fab5f6 & 1))
    {
        sub_f7d92c(&g_1efa0c0);
        g_1fab5f6 = 1;
    }
    v0 = ptr->field_18;
    if (v0)
    {
        if (!v0->field_10 || v0->field_14 != 1 || !((char)SystemInfo__get_supportsMotionVectors(0) & 1) || 2 > SystemInfo__get_supportedRenderTargetCount(0))
        {
            return 0;
        }
        else if (ptr->field_10)
        {
            if (ptr->field_10->field_30)
                v1 = 0;
            else
                v1 = 1;
            return v1;
        }
    }
    sub_f7db74();
}
```

## `TaaComponent.GetCameraFlags` — RVA `0xcd95c0`

- Decompiled symbol: `TaaComponent_GetCameraFlags`
- Metadata signature: `public override DepthTextureMode GetCameraFlags() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
unsigned int TaaComponent_GetCameraFlags(void)
{
    return 5;
}
```

## `TaaComponent.get_jitterVector` — RVA `0xcd95c8`

- Decompiled symbol: `TaaComponent_get_jitterVector`
- Metadata signature: `public Vector2 get_jitterVector() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long TaaComponent_get_jitterVector(unsigned long a0)
{
    return a0;
}
```

## `TaaComponent.set_jitterVector` — RVA `0xcd95d0`

- Decompiled symbol: `TaaComponent_set_jitterVector`
- Metadata signature: `private void set_jitterVector(Vector2 value) { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
unsigned int [16] TaaComponent_set_jitterVector(unsigned int *ptr)
{
    unsigned int v0;  // s0
    unsigned int v1;  // s1

    ptr[14] = v0;
    ptr[15] = v1;
    return ptr;
}
```

## `TaaComponent.ResetHistory` — RVA `0xcd95d8`

- Decompiled symbol: `TaaComponent_ResetHistory`
- Metadata signature: `public void ResetHistory() { }`
- Native interval: `12` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[44];
    char field_2c;
} struct_0;

struct_0 * TaaComponent_ResetHistory(struct_0 *ptr)
{
    ptr->field_2c = 1;
    return ptr;
}
```

## `TaaComponent.SetProjectionMatrix` — RVA `0xcd95e4`

- Decompiled symbol: `TaaComponent_SetProjectionMatrix`
- Metadata signature: `public void SetProjectionMatrix(Func<Vector2, Matrix4x4> jitteredFunc) { }`
- Native interval: `624` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[16];
    struct struct_0 *field_10;
    unsigned long long field_18;
} struct_1;

typedef struct struct_0 {
    char padding_0[24];
    long long field_18;
} struct_0;

typedef struct struct_2 {
    char padding_0[24];
    struct struct_3 *field_18;
    char padding_20[8];
    unsigned long long field_28;
    char padding_30[16];
    unsigned long long field_40;
} struct_2;

typedef struct struct_3 {
    unsigned long long field_0;
} struct_3;

extern long long g_1ef3b10;
extern long long g_1efa0c0;
extern long long g_1f0aaa8;
extern char g_1fab5f7;

long long TaaComponent_SetProjectionMatrix(struct_1 *index, struct_2 *ptr)
{
    unsigned long long v28;  // d11
    unsigned long long v29;  // d10
    long long v38;  // x21
    unsigned long long flag;  // x2
    long long v40;  // x21
    unsigned long long v41;  // x0
    unsigned long long v42;  // x1
    unsigned long long v30;  // d9
    unsigned long long v31;  // d8
    unsigned long long v32;  // x30
    unsigned long long v33;  // x23
    unsigned long long v34;  // x22
    unsigned long long v35;  // x21
    unsigned long long v36;  // x20
    unsigned long long v37;  // x19
    char v0;  // [bp-0x1e0]
    uint128_t v1;  // [bp-0x1d0]
    uint128_t v2;  // [bp-0x1c0]
    uint128_t v3;  // [bp-0x1b0]
    char v4;  // [bp-0x120]
    uint128_t v5;  // [bp-0x110]
    uint128_t v6;  // [bp-0x100]
    uint128_t v7;  // [bp-0xf0]
    char v8;  // [bp-0xe0]
    uint128_t v9;  // [bp-0xd0]
    uint128_t v10;  // [bp-0xc0]
    uint128_t v11;  // [bp-0xb0]
    int flag3;  // [bp-0xa0]
    uint128_t flag4;  // [bp-0x90]
    uint128_t choice;  // [bp-0x80]
    uint128_t flag2;  // [bp-0x70]
    unsigned long long v16;  // [bp-0x60]
    unsigned long long v17;  // [bp-0x58]
    unsigned long long v18;  // [bp-0x50]
    unsigned long long v19;  // [bp-0x48]
    char *v20;  // [bp-0x40]
    unsigned long long v21;  // [bp-0x30]
    unsigned long long v22;  // [bp-0x28]
    unsigned long long v23;  // [bp-0x20]
    unsigned long long v24;  // [bp-0x18]
    unsigned long long v25;  // [bp-0x10]
    unsigned long long v26;  // [bp-0x8]
    char v27;  // [bp+0x0]

    v16 = v28;
    v17 = v29;
    v18 = v30;
    v19 = v31;
    v20 = &v27;
    v21 = v32;
    v22 = v33;
    v23 = v34;
    v24 = v35;
    v25 = v36;
    v26 = v37;
    if (!(g_1fab5f7 & 1))
    {
        sub_f7d92c(&g_1efa0c0);
        sub_f7d92c(&g_1ef3b10);
        sub_f7d92c(&g_1f0aaa8);
        g_1fab5f7 = 1;
    }
    choice = 0;
    flag2 = 0;
    flag3 = 0;
    flag4 = 0;
    if (index->field_18)
    {
        TaaComponent__GenerateRandomOffset();
        if (index->field_10)
        {
            v38 = index->field_10->field_18;
            if (v38)
            {
                Camera__get_projectionMatrix(v38, 0);
                flag = 0;
                memcpy(&v4, &v8, 16);
                v5 = v9;
                v6 = v10;
                v7 = v11;
                Camera__set_nonJitteredProjectionMatrix(v38, &v4, 0);
                if (index->field_10)
                {
                    v40 = index->field_10->field_18;
                    if (ptr)
                    {
                        v41 = ptr->field_40;
                        v42 = ptr->field_28;
                        ptr->field_18();
                    }
                    else if (v40)
                    {
                        if (((char)Camera__get_orthographic(v40, 0) & 1))
                            TaaComponent__GetOrthographicProjectionMatrix(index);
                        else
                            TaaComponent__GetPerspectiveProjectionMatrix(index);
                        memcpy(&v0, &flag3, 16);
                        v1 = flag4;
                        v2 = choice;
                        v3 = flag2;
                        Camera__set_projectionMatrix(v40);
                        if (index->field_10 && index->field_10->field_18)
                        {
                            Camera__set_useJitteredProjectionMatrixForTransparentRendering(index->field_10->field_18, 0, 0);
                            if (index->field_10)
                                PostProcessingContext__get_width(index->field_10, 0); /* do not return */
                        }
                    }
                }
            }
        }
    }
    sub_f7db74();
}
```

## `TaaComponent.GenerateRandomOffset` — RVA `0xcd9854`

- Decompiled symbol: `TaaComponent_GenerateRandomOffset`
- Metadata signature: `private Vector2 GenerateRandomOffset() { }`
- Native interval: `148` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[40];
    int field_28;
} struct_0;

struct_0 * TaaComponent_GenerateRandomOffset(struct_0 *ptr)
{
    int v0;  // w8
    unsigned int j;  // w9
    unsigned long v2;  // 4116
    unsigned int i;  // w10
    unsigned int v6;  // w8

    v0 = ptr->field_28;
    j = v0 & 1023;
    v2 = arm64g_calculate_condition(9, (unsigned long long)(v0 & 1023), 0, 0);
    if (!((char)v2))
    {
        i = j;
        do
        {
            i = (i * 0x80000000 | i >> 1) & 2147483647;
        } while (i);
        do
        {
            j = __ROL__(j * 2863311531, 31) & 2147483647;
        } while (2 < j);
    }
    if (8 <= v0 + 1)
        v6 = 0;
    else
        v6 = v0 + 1;
    ptr->field_28 = v6;
    return ptr;
}
```

## `TaaComponent.GetPerspectiveProjectionMatrix` — RVA `0xcd98e8`

- Decompiled symbol: `TaaComponent_GetPerspectiveProjectionMatrix`
- Metadata signature: `private Matrix4x4 GetPerspectiveProjectionMatrix(Vector2 offset) { }`
- Native interval: `1064` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[16];
    struct struct_0 *field_10;
} struct_1;

typedef struct struct_0 {
    char padding_0[24];
    long long field_18;
} struct_0;

long long TaaComponent_GetPerspectiveProjectionMatrix(struct_1 *a0)
{
    unsigned long long v17;  // d15
    unsigned long long v18;  // d14
    unsigned long long v27;  // x21
    unsigned long long v28;  // x20
    unsigned long long v29;  // x19
    unsigned long long v19;  // d13
    unsigned long long v20;  // d12
    unsigned long long v21;  // d11
    unsigned long long v22;  // d10
    unsigned long long v23;  // d9
    unsigned long long v24;  // d8
    unsigned long long v25;  // x30
    unsigned long long v26;  // x22
    uint128_t flag2;  // [bp-0xb0]
    uint128_t flag3;  // [bp-0xa0]
    uint128_t flag;  // [bp-0x90]
    uint128_t choice;  // [bp-0x80]
    unsigned long long v4;  // [bp-0x70]
    unsigned long long v5;  // [bp-0x68]
    unsigned long long v6;  // [bp-0x60]
    unsigned long long v7;  // [bp-0x58]
    unsigned long long v8;  // [bp-0x50]
    unsigned long long v9;  // [bp-0x48]
    unsigned long long v10;  // [bp-0x40]
    unsigned long long v11;  // [bp-0x38]
    unsigned long long v12;  // [bp-0x30]
    unsigned long long v13;  // [bp-0x20]
    unsigned long long v14;  // [bp-0x18]
    unsigned long long v15;  // [bp-0x10]
    unsigned long long v16;  // [bp-0x8]

    v4 = v17;
    v5 = v18;
    v6 = v19;
    v7 = v20;
    v8 = v21;
    v9 = v22;
    v10 = v23;
    v11 = v24;
    v12 = v25;
    v13 = v26;
    v14 = v27;
    v15 = v28;
    v16 = v29;
    flag = 0;
    choice = 0;
    flag2 = 0;
    flag3 = 0;
    if (a0->field_10 && a0->field_10->field_18)
    {
        tanf(Camera__get_fieldOfView(a0->field_10->field_18, 0), 0);
        if (a0->field_10 && a0->field_10->field_18)
        {
            Camera__get_aspect(a0->field_10->field_18, 0);
            if (a0->field_10)
                PostProcessingContext__get_width(a0->field_10, 0); /* do not return */
        }
    }
    sub_f7db74();
}
```

## `TaaComponent.GetOrthographicProjectionMatrix` — RVA `0xcd9d10`

- Decompiled symbol: `TaaComponent_GetOrthographicProjectionMatrix`
- Metadata signature: `private Matrix4x4 GetOrthographicProjectionMatrix(Vector2 offset) { }`
- Native interval: `336` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[16];
    struct struct_0 *field_10;
} struct_1;

typedef struct struct_0 {
    char padding_0[24];
    long long field_18;
} struct_0;

long long TaaComponent_GetOrthographicProjectionMatrix(struct_1 *a0, unsigned long a1, unsigned long a2)
{
    unsigned long long v11;  // d13
    unsigned long long v12;  // d12
    unsigned long long v21;  // x19
    unsigned long long v13;  // d11
    unsigned long long v14;  // d10
    unsigned long long v15;  // d9
    unsigned long long v16;  // d8
    unsigned long long v17;  // x30
    unsigned long long v18;  // x22
    unsigned long long v19;  // x21
    unsigned long long v20;  // x20
    unsigned long long v0;  // [bp-0x60]
    unsigned long long v1;  // [bp-0x58]
    unsigned long long v2;  // [bp-0x50]
    unsigned long long v3;  // [bp-0x48]
    unsigned long long v4;  // [bp-0x40]
    unsigned long long v5;  // [bp-0x38]
    unsigned long long v6;  // [bp-0x30]
    unsigned long long v7;  // [bp-0x20]
    unsigned long long v8;  // [bp-0x18]
    unsigned long long v9;  // [bp-0x10]
    unsigned long long v10;  // [bp-0x8]

    v0 = v11;
    v1 = v12;
    v2 = v13;
    v3 = v14;
    v4 = v15;
    v5 = v16;
    v6 = v17;
    v7 = v18;
    v8 = v19;
    v9 = v20;
    v10 = v21;
    if (a0->field_10 && a0->field_10->field_18)
    {
        Camera__get_orthographicSize(a0->field_10->field_18, 0);
        if (a0->field_10 && a0->field_10->field_18)
        {
            Camera__get_aspect(a0->field_10->field_18, 0);
            if (a0->field_10)
                PostProcessingContext__get_width(a0->field_10, 0); /* do not return */
        }
    }
    sub_f7db74();
}
```

## `TaaComponent.Render` — RVA `0xcd9e60`

- Decompiled symbol: `TaaComponent_Render`
- Metadata signature: `public void Render(RenderTexture source, RenderTexture destination) { }`
- Native interval: `1096` bytes
- Result: `pseudocode`

```c
typedef struct struct_4 {
    char padding_0[16];
    struct struct_1 *field_10;
    unsigned long long field_18;
    char padding_20[12];
    char field_2c;
    char padding_2d[3];
    struct struct_5 *field_30;
} struct_4;

typedef struct struct_1 {
    char padding_0[32];
    long long field_20;
} struct_1;

typedef struct struct_2 {
    char padding_0[376];
    struct struct_3 *field_178;
    unsigned long long field_180;
} struct_2;

typedef struct struct_6 {
    char padding_0[376];
    struct struct_7 *field_178;
    unsigned long long field_180;
} struct_6;

typedef struct struct_5 {
    struct struct_2 *field_0;
} struct_5;

typedef struct struct_3 {
    unsigned long long field_0;
} struct_3;

typedef struct struct_7 {
    unsigned long long field_0;
} struct_7;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern long long g_1ef3b10;
extern long long g_1efa0c0;
extern long long g_1f0aaa8;
extern long long g_1f0e028;
extern char g_1fab5f8;

void TaaComponent_Render(struct_4 *ptr, struct_6 **a1, unsigned long a2)
{
    unsigned long long v13;  // d10
    unsigned long long v14;  // d9
    unsigned long long v23;  // x21
    unsigned long long v24;  // x20
    unsigned long long v25;  // x19
    unsigned long long v26;  // x2
    struct_2 **v27;  // x0
    unsigned long long v28;  // x1
    struct_6 **v29;  // x0
    unsigned long v30;  // x1
    unsigned long long v15;  // d8
    unsigned long long v16;  // x30
    unsigned long long v17;  // x27
    unsigned long long v18;  // x26
    unsigned long long v19;  // x25
    unsigned long long v20;  // x24
    unsigned long long v21;  // x23
    unsigned long long v22;  // x22
    unsigned long long v0;  // [bp-0x70]
    unsigned long long v1;  // [bp-0x60]
    unsigned long long v2;  // [bp-0x58]
    unsigned long long v3;  // [bp-0x50]
    unsigned long long v4;  // [bp-0x48]
    unsigned long long v5;  // [bp-0x40]
    unsigned long long v6;  // [bp-0x38]
    unsigned long long v7;  // [bp-0x30]
    unsigned long long v8;  // [bp-0x28]
    unsigned long long v9;  // [bp-0x20]
    unsigned long long v10;  // [bp-0x18]
    unsigned long long v11;  // [bp-0x10]
    unsigned long long v12;  // [bp-0x8]

    v0 = v13;
    v1 = v14;
    v2 = v15;
    v3 = v16;
    v4 = v17;
    v5 = v18;
    v6 = v19;
    v7 = v20;
    v8 = v21;
    v9 = v22;
    v10 = v23;
    v11 = v24;
    v12 = v25;
    if (!(g_1fab5f8 & 1))
    {
        sub_f7d92c("g=");
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c(&g_1efa0c0);
        sub_f7d92c(&g_1ef3b10);
        sub_f7d92c(&g_1f0e028);
        sub_f7d92c(&g_1f0aaa8);
        g_1fab5f8 = 1;
    }
    if (ptr->field_10 && ptr->field_10->field_20 && MaterialFactory__Get(ptr->field_10->field_20, g_1f0aaa8, 0) && (v26 = 0, Material__set_shaderKeywords(), ptr->field_18))
    {
        if (!ptr->field_2c)
        {
            if (!g_1ef0c58->field_e0)
                sub_f7da5c(g_1ef0c58);
            v26 = 0;
            if ((Object__op_Equality(ptr->field_30, 0, 0) & 1))
                goto LABEL_10d9fd8;
            v27 = ptr->field_30;
            if (v27)
            {
                v28 = *(v27)->field_180;
                *(v27)->field_178();
            }
        }
        else
        {
LABEL_10d9fd8:
            if (!g_1ef0c58->field_e0)
                sub_f7da5c(g_1ef0c58);
            if (((char)Object__op_Implicit(ptr->field_30, 0) & 1))
                RenderTexture__ReleaseTemporary(ptr->field_30, 0);
            if (a1)
            {
                v29 = a1;
                v30 = *(a1)->field_180;
                *(a1)->field_178();
            }
        }
    }
    sub_f7db7c(sub_f7db74());
}
```

## `TaaComponent.GetHaltonValue` — RVA `0xcda2a8`

- Decompiled symbol: `TaaComponent_GetHaltonValue`
- Metadata signature: `private float GetHaltonValue(int index, int radix) { }`
- Native interval: `68` bytes
- Result: `pseudocode`

```c
long long TaaComponent_GetHaltonValue(unsigned long a0, unsigned long long a1, unsigned long long a2)
{
    int i;  // w8

    if ((unsigned int)a1 < 1)
        return a0;
    do
    {
        a1 = a1 / a2 & 4294967295;
    } while (0 < i);
    return a0;
}
```

## `TaaComponent.OnDisable` — RVA `0xcda2ec`

- Decompiled symbol: `TaaComponent_OnDisable`
- Metadata signature: `public override void OnDisable() { }`
- Native interval: `156` bytes
- Result: `pseudocode`
- Heuristic layout hint: `TaaComponent_Recovered` matched 3 offsets against `TaaComponent` metadata (confidence 1.00).

```c
typedef struct TaaComponent_Recovered {
    char padding_0[40];
    unsigned int m_SampleIndex;
    char m_ResetHistory;
    char padding_2d[3];
    long long m_HistoryTexture;
} TaaComponent_Recovered;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab5f9;

long long TaaComponent_OnDisable(struct_1 *ptr)
{
    struct_1 *v0;  // x20
    unsigned long v1;  // x0

    if (!(g_1fab5f9 & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab5f9 = 1;
    }
    v0 = &ptr->field_30;
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (((char)Object__op_Inequality(ptr->field_30, 0, 0) & 1))
        RenderTexture__ReleaseTemporary(*((long long *)&v0->padding_0[0]), 0);
    ptr->field_30 = 0;
    v1 = sub_f7d8d0(v0, 0);
    ptr->field_28 = 0;
    ptr->field_2c = 1;
    return v1;
}
```

## `TaaComponent.ctor` — RVA `0xcda388`

- Decompiled symbol: `TaaComponent_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `136` bytes
- Result: `pseudocode`
- Heuristic layout hint: `TaaComponent_Recovered` matched 2 offsets against `TaaComponent` metadata (confidence 1.00).

```c
typedef struct TaaComponent_Recovered {
    char padding_0[32];
    long long m_MRT;
    char padding_28[4];
    char m_ResetHistory;
} TaaComponent_Recovered;

extern long long g_1eee2f8;
extern long long g_1efa068;
extern char g_1fab5fa;

void TaaComponent_ctor(struct_0 *ptr)
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
    if (!(g_1fab5fa & 1))
    {
        sub_f7d92c(&g_1efa068);
        sub_f7d92c(&g_1eee2f8);
        g_1fab5fa = 1;
    }
    v10 = sub_f7d9d4(g_1eee2f8, 2);
    ptr->field_20 = v10;
    sub_f7d8d0((struct TaaComponent_Recovered *)&ptr->field_20, v10);
    ptr->field_2c = 1;
}
```
