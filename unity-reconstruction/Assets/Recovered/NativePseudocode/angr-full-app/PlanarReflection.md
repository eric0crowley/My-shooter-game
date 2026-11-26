# Native pseudocode: PlanarReflection

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `PlanarReflection.Start` — RVA `0xce1ec8`

- Decompiled symbol: `PlanarReflection_Start`
- Metadata signature: `public void Start() { }`
- Native interval: `252` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    char padding_0[88];
    unsigned long long field_58;
} struct_2;

typedef struct struct_4 {
    struct struct_3 *field_0;
    char padding_8[24];
    unsigned long long field_20;
} struct_4;

typedef struct struct_3 {
    char padding_0[200];
    unsigned long long field_c8;
    char padding_d0[96];
    char field_130;
} struct_3;

typedef struct struct_1 {
    char padding_0[304];
    char field_130;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern long long g_1eebbf8;
extern struct_0 *g_1ef1f08;
extern struct_1 *g_1ef2470;
extern char g_1fab642;

void PlanarReflection_Start(struct_2 *ptr)
{
    unsigned long long v5;  // x30
    unsigned long long v6;  // x22
    unsigned long long v7;  // x21
    unsigned long long v8;  // x20
    unsigned long long v9;  // x19
    long long v10;  // x20
    long long v11;  // x0
    struct_4 *index;  // x0
    unsigned long v13;  // x9
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
    if (!(g_1fab642 & 1))
    {
        sub_f7d92c(&g_1ef1f08);
        sub_f7d92c(&g_1eebbf8);
        sub_f7d92c(&g_1ef2470);
        g_1fab642 = 1;
    }
    v10 = Component__get_gameObject(ptr, 0);
    if (!g_1ef1f08->field_e0)
        sub_f7da5c(g_1ef1f08);
    v11 = Type__GetTypeFromHandle(g_1eebbf8, 0);
    if (v10 && !((index = (struct_4 *)(unsigned long long)GameObject__GetComponent(v10, v11, 0), !index)))
    {
        v13 = g_1ef2470->field_130;
        if (index->field_0->field_130 >= (unsigned int)v13 && *((long long *)(index->field_0->field_c8 + v13 * 8 - 8)) == g_1ef2470)
        {
            ptr->field_58 = index->field_20;
            sub_f7d8d0();
            return;
        }
    }
    else
    {
        index = sub_f7db74();
    }
    sub_f7df10(index);
}
```

## `PlanarReflection.CreateReflectionCameraFor` — RVA `0xce1fc4`

- Decompiled symbol: `PlanarReflection_CreateReflectionCameraFor`
- Metadata signature: `private Camera CreateReflectionCameraFor(Camera cam) { }`
- Native interval: `780` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    char padding_0[36];
    char field_24;
} struct_2;

typedef struct struct_4 {
    struct struct_3 *field_0;
    char padding_8[16];
    unsigned int field_18;
    char padding_1c[4];
    char field_20;
} struct_4;

typedef struct struct_3 {
    char padding_0[64];
    long long field_40;
} struct_3;

typedef struct struct_1 {
    char padding_0[224];
    unsigned int field_e0;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern long long g_1eee3d8;
extern long long g_1eefaf0;
extern struct_0 *g_1ef0c58;
extern struct_1 *g_1ef1f08;
extern long long g_1efeb60;
extern long long g_1f0d398;
extern char g_1fab643;

long long PlanarReflection_CreateReflectionCameraFor(struct_2 *a0, long long a1, unsigned long a2)
{
    unsigned long v0;  // x0
    long long v1;  // x2
    long long v10;  // x0
    long long v12;  // x0
    long long v13;  // x21
    long long v14;  // x0
    long long v2;  // x0
    long long v3;  // x21
    struct_4 *v4;  // x23
    unsigned long v5;  // x0
    unsigned long v6;  // x21
    struct_4 *ptr;  // x0
    long long v8;  // x0
    long long v9;  // x0

    if (!(g_1fab643 & 1))
    {
        sub_f7d92c("O1");
        sub_f7d92c(&g_1efeb60);
        sub_f7d92c(&g_1eefaf0);
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c(&g_1eee3d8);
        sub_f7d92c(&g_1ef1f08);
        sub_f7d92c(&g_1f0d398);
        g_1fab643 = 1;
    }
    if (Component__get_gameObject(a0, 0) && !((v0 = (unsigned long)Object__get_name(), !a1)))
    {
        v1 = Object__get_name(a1, 0);
        v2 = String__Concat(Object__get_name(), g_1f0d398, v1, 0);
        v3 = GameObject__Find(v2, 0, v1, 0);
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        if (!((char)Object__op_Implicit(v3, 0) & 1))
        {
            v4 = sub_f7d9d4(g_1eee3d8, 1);
            if (!g_1ef1f08->field_e0)
                sub_f7da5c(g_1ef1f08);
            v5 = Type__GetTypeFromHandle(g_1eeb1f0, 0);
            if (v4)
            {
                v6 = v5;
                if (v5 && (v5 = (unsigned long)sub_f7da60(v6, v4->field_0->field_40), !v5))
                    goto LABEL_10e22c4;
                if (!v4->field_18)
                    goto LABEL_10e22c0;
                ptr = v4;
                *((unsigned long *)&ptr->field_20) = v6;
                sub_f7d8d0((struct struct_4 *)&ptr->field_20, v6);
                v8 = sub_f7db70(g_1eefaf0);
                v3 = v8;
                GameObject__ctor(v8, v2, v4, 0);
                goto LABEL_10e2174;
            }
        }
        else
        {
LABEL_10e2174:
            if (!g_1ef1f08->field_e0)
                sub_f7da5c(g_1ef1f08);
            v9 = Type__GetTypeFromHandle(g_1eeb1f0, 0);
            if (v3)
            {
                v10 = GameObject__GetComponent(v3, v9, 0);
                if (!g_1ef0c58->field_e0)
                    sub_f7da5c(g_1ef0c58);
                if (!((char)Object__op_Implicit(v10, 0) & 1))
                {
                    if (!g_1ef1f08->field_e0)
                        sub_f7da5c(g_1ef1f08);
                    GameObject__AddComponent(v3, Type__GetTypeFromHandle(g_1eeb1f0, 0), 0);
                }
                v12 = sub_1249224(v3, g_1efeb60);
                if (v12)
                {
                    v13 = v12;
                    Camera__set_backgroundColor();
                    Camera__set_clearFlags();
                    PlanarReflection__SetStandardCameraParameter();
                    v14 = Camera__get_targetTexture(v13, 0);
                    if (!g_1ef0c58->field_e0)
                        sub_f7da5c(g_1ef0c58);
                    if (((char)Object__op_Implicit(v14, 0) & 1))
                        return v13;
                    Camera__set_targetTexture(v13, PlanarReflection__CreateTextureFor(), 0);
                    return v13;
                }
            }
        }
    }
    v5 = sub_f7db74();
LABEL_10e22c0:
    v5 = sub_f7db7c(v5);
LABEL_10e22c4:
    sub_f7da4c(sub_f7db98(v5), 0);
}
```

## `PlanarReflection.SetStandardCameraParameter` — RVA `0xce22d0`

- Decompiled symbol: `PlanarReflection_SetStandardCameraParameter`
- Metadata signature: `private void SetStandardCameraParameter(Camera cam, LayerMask mask) { }`
- Native interval: `180` bytes
- Result: `pseudocode`

```c
extern char g_1fab644;

void PlanarReflection_SetStandardCameraParameter(unsigned long a0, long long a1, unsigned int a2)
{
    unsigned long long v5;  // x30
    unsigned long long v6;  // x22
    unsigned long long v7;  // x21
    unsigned long long v8;  // x20
    unsigned long long v9;  // x19
    unsigned int v10;  // w0
    char v11;  // x0
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
    if (!(g_1fab644 & 1))
    {
        sub_f7d92c("S&");
        g_1fab644 = 1;
    }
    v10 = LayerMask__op_Implicit(a2, 0);
    v11 = LayerMask__NameToLayer(g_1f0fb38, 0);
    if (a1)
    {
        Camera__set_cullingMask(a1, v10 & ~(1 << (v11 & 31)), 0);
        Camera__set_backgroundColor(a1, 0);
        Behaviour__set_enabled();
        return;
    }
    sub_f7db74();
}
```

## `PlanarReflection.CreateTextureFor` — RVA `0xce2384`

- Decompiled symbol: `PlanarReflection_CreateTextureFor`
- Metadata signature: `private RenderTexture CreateTextureFor(Camera cam) { }`
- Native interval: `348` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: Decompiler produced no C-like text

```c
// 0x10e2384: stp d9, d8, [sp, #-0x40]!
// 0x10e2388: str x30, [sp, #0x10]
// 0x10e238c: stp x22, x21, [sp, #0x20]
// 0x10e2390: stp x20, x19, [sp, #0x30]
// 0x10e2394: adrp x20, #0x1fab000
// 0x10e2398: ldrb w8, [x20, #0x645]
// 0x10e239c: mov x19, x1
// 0x10e23a0: tbnz w8, #0, #0x10e23b8
// 0x10e23a4: adrp x0, #0x1e8e000
// 0x10e23a8: ldr x0, [x0, #0xeb0]
// 0x10e23ac: bl #0xf7d92c
// 0x10e23b0: mov w8, #1
// 0x10e23b4: strb w8, [x20, #0x645]
// 0x10e23b8: cbz x19, #0x10e24dc
// 0x10e23bc: mov x0, x19
// 0x10e23c0: mov x1, xzr
// 0x10e23c4: bl #0x1b6eedc
// 0x10e23c8: adrp x21, #0x1fab000
// 0x10e23cc: ldrb w8, [x21, #0x2cc]
// 0x10e23d0: scvtf s8, w0
// 0x10e23d4: fmov s9, #0.50000000
// 0x10e23d8: cbnz w8, #0x10e23f0
// 0x10e23dc: adrp x0, #0x1e8c000
// 0x10e23e0: ldr x0, [x0, #0xa60]
// 0x10e23e4: bl #0xf7d92c
// 0x10e23e8: mov w8, #1
// 0x10e23ec: strb w8, [x21, #0x2cc]
// 0x10e23f0: adrp x22, #0x1e8c000
// 0x10e23f4: ldr x22, [x22, #0xa60]
// 0x10e23f8: fmul s8, s8, s9
// 0x10e23fc: ldr x0, [x22]
// 0x10e2400: ldr w8, [x0, #0xe0]
// 0x10e2404: cbnz w8, #0x10e240c
// 0x10e2408: bl #0xf7da5c
// 0x10e240c: mov w8, #0x7f800000
// 0x10e2410: frintm s0, s8
// 0x10e2414: fmov s1, w8
// 0x10e2418: fcvtms w9, s8
// 0x10e241c: fcmp s0, s1
// 0x10e2420: mov w8, #-0x80000000
// 0x10e2424: mov x0, x19
// 0x10e2428: mov x1, xzr
// 0x10e242c: csel w20, w8, w9, eq
// 0x10e2430: bl #0x1b6ef18
// 0x10e2434: ldrb w8, [x21, #0x2cc]
// 0x10e2438: scvtf s8, w0
// 0x10e243c: fmov s9, #0.50000000
// 0x10e2440: cbnz w8, #0x10e2458
// 0x10e2444: adrp x0, #0x1e8c000
// 0x10e2448: ldr x0, [x0, #0xa60]
// 0x10e244c: bl #0xf7d92c
// 0x10e2450: mov w8, #1
// 0x10e2454: strb w8, [x21, #0x2cc]
// 0x10e2458: ldr x0, [x22]
// 0x10e245c: adrp x19, #0x1e8e000
// 0x10e2460: fmul s8, s8, s9
// 0x10e2464: ldr w8, [x0, #0xe0]
// 0x10e2468: ldr x19, [x19, #0xeb0]
// 0x10e246c: cbnz w8, #0x10e2474
// 0x10e2470: bl #0xf7da5c
// 0x10e2474: ldr x0, [x19]
// 0x10e2478: mov w9, #0x7f800000
// 0x10e247c: frintm s0, s8
// 0x10e2480: fmov s1, w9
// 0x10e2484: fcvtms w8, s8
// 0x10e2488: fcmp s0, s1
// 0x10e248c: mov w9, #-0x80000000
// 0x10e2490: csel w21, w9, w8, eq
// 0x10e2494: bl #0xf7db70
// 0x10e2498: mov w3, #0x18
// 0x10e249c: mov w1, w20
// 0x10e24a0: mov w2, w21
// 0x10e24a4: mov x4, xzr
// 0x10e24a8: mov x19, x0
// 0x10e24ac: bl #0x1b83954
// 0x10e24b0: cbz x19, #0x10e24dc
// 0x10e24b4: mov w1, #0x34
// 0x10e24b8: mov x0, x19
// 0x10e24bc: mov x2, xzr
// 0x10e24c0: bl #0x1b98c88
// 0x10e24c4: mov x0, x19
// 0x10e24c8: ldp x20, x19, [sp, #0x30]
// 0x10e24cc: ldp x22, x21, [sp, #0x20]
// 0x10e24d0: ldr x30, [sp, #0x10]
// 0x10e24d4: ldp d9, d8, [sp], #0x40
// 0x10e24d8: ret
// 0x10e24dc: bl #0xf7db74
```

## `PlanarReflection.RenderHelpCameras` — RVA `0xce24e0`

- Decompiled symbol: `PlanarReflection_RenderHelpCameras`
- Metadata signature: `public void RenderHelpCameras(Camera currentCam) { }`
- Native interval: `440` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern long long g_1eec4b0;
extern struct_0 *g_1ef0c58;
extern long long g_1ef5210;
extern long long g_1ef5218;
extern long long g_1ef5228;
extern void g_1ef5230;
extern long long g_1ef5238;
extern char g_1fab646;

unsigned long long PlanarReflection_RenderHelpCameras(long long *p, long long a1)
{
    long long addr[13];  // x21
    long long v1;  // x0
    long long ptr[13];  // x21
    long long v3;  // x22
    unsigned long long v4;  // x0
    long long v5[13];  // x21
    long long v6;  // x0
    unsigned long long v7;  // x0

    if (!(g_1fab646 & 1))
    {
        sub_f7d92c(&g_1ef5218);
        sub_f7d92c(&g_1ef5228);
        sub_f7d92c(&g_1ef5210);
        sub_f7d92c(&g_1ef5230);
        sub_f7d92c(&g_1ef5238);
        sub_f7d92c(&g_1eec4b0);
        sub_f7d92c(&g_1ef0c58);
        g_1fab646 = 1;
    }
    addr = p;
    v1 = addr[12];
    ptr = &addr[12];
    if (!v1)
    {
        v3 = sub_f7db70(g_1eec4b0);
        sub_12a78f8(v3, g_1ef5210);
        ptr[0] = v3;
        sub_f7d8d0(ptr, v3);
        v1 = ptr[0];
        if (v1)
            goto LABEL_10e25a4;
    }
    else
    {
LABEL_10e25a4:
        if (!((char)sub_12a7df4(v1, a1, g_1ef5228) & 1))
        {
            v1 = ptr[0];
            if (v1)
            {
                sub_12a7bec(v1, a1, 0, g_1ef5218);
                goto LABEL_10e25dc;
            }
        }
        else
        {
LABEL_10e25dc:
            v1 = ptr[0];
            if (v1)
            {
                v4 = sub_12a7b60(v1, a1, *((long long *)&g_1ef5230));
                if (((char)v4 & 1))
                    return v4;
                v5 = p;
                if (!g_1ef0c58->field_e0)
                    sub_f7da5c(g_1ef0c58);
                if (!((char)Object__op_Implicit(v5[10], 0) & 1))
                {
                    v6 = PlanarReflection__CreateReflectionCameraFor(p, a1, *((long long *)&g_1ef5230));
                    p[10] = v6;
                    sub_f7d8d0((long long [13])&v5[10], v6);
                }
                PlanarReflection__RenderReflectionFor();
                v1 = p[12];
                if (v1)
                {
                    v7 = sub_12a7bd4();
                    return sub_12a7bd4();
                }
            }
        }
    }
    sub_f7db74(v1);
}
```

## `PlanarReflection.RenderReflectionFor` — RVA `0xce2698`

- Decompiled symbol: `PlanarReflection_RenderReflectionFor`
- Metadata signature: `private void RenderReflectionFor(Camera cam, Camera reflectCamera) { }`
- Native interval: `1692` bytes
- Result: `pseudocode`
- Heuristic layout hint: `PlanarReflection_Recovered` matched 6 offsets against `PlanarReflection` metadata (confidence 0.60).

```c
typedef struct PlanarReflection_Recovered {
    char padding_0[32];
    unsigned int reflectionMask;
    char reflectSkybox;
    char padding_25[3];
    unsigned int clearColor;
    unsigned int field_2c;
    unsigned int field_30;
    char padding_34[4];
    long long reflectionSampler;
    char padding_40[4];
    unsigned int m_Oldpos;
    unsigned int field_48;
    unsigned int field_4c;
    char padding_50[8];
    unsigned long long m_SharedMaterial;
} PlanarReflection_Recovered;

typedef struct struct_1 {
    char padding_0[224];
    unsigned int field_e0;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern long long g_1eeb9a0;
extern struct_0 *g_1ef0c58;
extern unsigned long long g_1ef1748;
extern struct_1 *g_1ef1f08;
extern char g_1fab64b;

long long PlanarReflection_RenderReflectionFor(struct_2 *ptr, long long a1, long long a2)
{
    long long v39;  // x0
    unsigned long long v40;  // x22
    unsigned long long v41;  // x0
    long long v42;  // x0
    unsigned int v44;  // s1
    long long v45;  // x23
    unsigned int v46;  // s2
    unsigned long long v47;  // x0
    char v0;  // [bp-0x2e0]
    uint128_t v1;  // [bp-0x2d0]
    uint128_t v2;  // [bp-0x2c0]
    uint128_t v3;  // [bp-0x2b0]
    int v4;  // [bp-0x2a0]
    uint128_t v5;  // [bp-0x290]
    uint128_t v6;  // [bp-0x280]
    uint128_t v7;  // [bp-0x270]
    char v8;  // [bp-0x260]
    uint128_t v9;  // [bp-0x250]
    uint128_t v10;  // [bp-0x240]
    uint128_t v11;  // [bp-0x230]
    int v12;  // [bp-0x220]
    uint128_t v13;  // [bp-0x210]
    uint128_t v14;  // [bp-0x200]
    uint128_t v15;  // [bp-0x1f0]
    char v16;  // [bp-0x1e0]
    uint128_t v17;  // [bp-0x1d0]
    uint128_t v18;  // [bp-0x1c0]
    uint128_t v19;  // [bp-0x1b0]
    int v20;  // [bp-0x1a0]
    uint128_t v21;  // [bp-0x190]
    uint128_t v22;  // [bp-0x180]
    uint128_t v23;  // [bp-0x170]
    int v24;  // [bp-0x160]
    uint128_t v25;  // [bp-0x150]
    uint128_t v26;  // [bp-0x140]
    uint128_t v27;  // [bp-0x130]
    int v28;  // [bp-0x120], Other Possible Types: uint128_t
    uint128_t v29;  // [bp-0x110]
    uint128_t v30;  // [bp-0x100]
    uint128_t v31;  // [bp-0xf0]
    int v32;  // [bp-0xe0], Other Possible Types: uint128_t
    uint128_t v33;  // [bp-0xd0]
    uint128_t v34;  // [bp-0xc0]
    uint128_t v35;  // [bp-0xb0]
    char *v36;  // [bp-0x60]
    unsigned int v37;  // [bp-0x54]
    char v38;  // [bp+0x0]

    v36 = &v38;
    if (!(g_1fab64b & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c(&g_1eeb9a0);
        sub_f7d92c(&g_1ef1748);
        sub_f7d92c(&g_1ef1f08);
        sub_f7d92c("S&");
        g_1fab64b = 1;
    }
    v34 = 0;
    v35 = 0;
    v32 = 0;
    v33 = 0;
    v30 = 0;
    v31 = 0;
    v28 = 0;
    v29 = 0;
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v39 = Object__op_Implicit(a2, 0);
    if (!((char)v39 & 1))
        return v39;
    v40 = ptr->field_58;
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (((char)Object__op_Implicit(v40, 0) & 1))
    {
        v41 = ptr->field_58;
        if (v41)
        {
            v42 = Material__HasProperty(v41, ptr->field_38, 0);
            if (!((char)v42 & 1))
                return v42;
            goto LABEL_10e2798;
        }
    }
    else
    {
LABEL_10e2798:
        v40 = LayerMask__op_Implicit(ptr->field_20, 0) & 4294967295;
        v41 = LayerMask__NameToLayer(g_1f0fb38, 0);
        if (a2)
        {
            PlanarReflection__SaneCameraSettings(Camera__set_cullingMask(a2, (unsigned int)v40 & ~(1 << ((char)v41 & 31)), 0), a2, 0);
            v44 = ptr->field_2c;
            Camera__set_backgroundColor(a2, 0);
            v41 = Camera__set_clearFlags();
            if (!ptr->field_24)
            {
LABEL_10e29e4:
                GL__set_invertCulling(1, 0);
                v41 = Component__get_transform(ptr, 0);
                if (a1)
                {
                    v40 = v41;
                    v41 = Component__get_transform(a1, 0);
                    if (v41)
                    {
                        Transform__get_eulerAngles();
                        v41 = Component__get_transform(a2, 0);
                        if (v41)
                        {
                            Transform__set_eulerAngles();
                            v45 = Component__get_transform(a2, 0);
                            v41 = Component__get_transform(a1, 0);
                            if (v41)
                            {
                                v41 = Transform__get_position();
                                if (v45)
                                {
                                    v41 = Transform__set_position(v45, 0);
                                    if (v40)
                                    {
                                        v41 = Component__get_transform(v40, 0);
                                        if (v41)
                                        {
                                            Transform__get_position();
                                            Transform__get_position(v40, 0);
                                            v41 = Component__get_transform(v40, 0);
                                            if (v41)
                                            {
                                                Transform__get_up();
                                                Matrix4x4__get_zero(0);
                                                v34 = v26;
                                                v35 = v27;
                                                v32 = v24;
                                                v33 = v25;
                                                v20 = v32;
                                                v21 = v33;
                                                v22 = v34;
                                                v23 = v35;
                                                v46 = ptr->field_30;
                                                PlanarReflection__CalculateReflectionMatrix(&v20);
                                                v41 = Component__get_transform(a1, 0);
                                                if (v41)
                                                {
                                                    Transform__get_position();
                                                    ptr->field_44 = -(ptr->field_28);
                                                    ptr->field_48 = v44;
                                                    ptr->field_4c = v46;
                                                    Matrix4x4__MultiplyPoint(&v32, 0);
                                                    v37 = v46;
                                                    Camera__get_worldToCameraMatrix(a1, 0);
                                                    memcpy(&v16, &v24, 16);
                                                    v17 = v25;
                                                    v18 = v26;
                                                    v19 = v27;
                                                    v12 = v32;
                                                    v13 = v33;
                                                    v14 = v34;
                                                    v15 = v35;
                                                    Matrix4x4__op_Multiply(&v16, &v12, 0);
                                                    memcpy(&v8, &v24, 16);
                                                    v9 = v25;
                                                    v10 = v26;
                                                    v11 = v27;
                                                    Camera__set_worldToCameraMatrix(a2, &v8, 0);
                                                    PlanarReflection__CameraSpacePlane(ptr, a2);
                                                    Camera__get_projectionMatrix(a1, 0);
                                                    v30 = v26;
                                                    v31 = v27;
                                                    v28 = v24;
                                                    v29 = v25;
                                                    v4 = v28;
                                                    v5 = v29;
                                                    v6 = v30;
                                                    v7 = v31;
                                                    PlanarReflection__CalculateObliqueMatrix(&v4);
                                                    memcpy(&v0, &v28, 16);
                                                    v1 = v29;
                                                    v2 = v30;
                                                    v3 = v31;
                                                    Camera__set_projectionMatrix(a2, &v0, 0);
                                                    v41 = Component__get_transform(a2, 0);
                                                    if (v41)
                                                    {
                                                        Transform__set_position();
                                                        v41 = Component__get_transform(a1, 0);
                                                        if (v41)
                                                        {
                                                            Transform__get_eulerAngles();
                                                            v41 = Component__get_transform(a2, 0);
                                                            if (v41)
                                                            {
                                                                Transform__set_eulerAngles();
                                                                Camera__Render(a2, 0);
                                                                v47 = GL__set_invertCulling(0, 0);
                                                                return GL__set_invertCulling(0, 0);
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
            else if (a1)
            {
                v40 = Component__get_gameObject(a1, 0);
                if (!g_1ef1f08->field_e0)
                    sub_f7da5c(g_1ef1f08);
                v41 = Type__GetTypeFromHandle(g_1eeb9a0, 0);
                if (v40)
                {
                    v40 = GameObject__GetComponent(v40, v41, 0);
                    if (!g_1ef0c58->field_e0)
                        sub_f7da5c(g_1ef0c58);
                    if (!(Object__op_Implicit(v40, 0) & 1))
                        goto LABEL_10e29e4;
                    v40 = Component__get_gameObject(a2, 0);
                    if (!g_1ef1f08->field_e0)
                        sub_f7da5c(g_1ef1f08);
                    v41 = Type__GetTypeFromHandle(g_1eeb9a0, 0);
                    if (v40)
                    {
                        v40 = GameObject__GetComponent(v40, v41, 0);
                        if (v40 && *((long long *)v40) != g_1ef1748)
                            goto LABEL_10e2d2c;
                        if (!g_1ef0c58->field_e0)
                            sub_f7da5c(g_1ef0c58);
                        if (!((char)Object__op_Implicit(v40, 0) & 1))
                        {
                            v40 = Component__get_gameObject(a2, 0);
                            if (!g_1ef1f08->field_e0)
                                sub_f7da5c(g_1ef1f08);
                            v41 = Type__GetTypeFromHandle(g_1eeb9a0, 0);
                            if (v40)
                            {
                                v40 = GameObject__AddComponent(v40, v41, 0);
                                if (!v40 || *((long long *)v40) == g_1ef1748)
                                    goto LABEL_10e2984;
                                goto LABEL_10e2d2c;
                            }
                        }
                        else
                        {
LABEL_10e2984:
                            if (!g_1ef1f08->field_e0)
                                sub_f7da5c(g_1ef1f08);
                            v41 = Component__GetComponent(a1, Type__GetTypeFromHandle(g_1eeb9a0, 0), 0);
                            if (v41)
                            {
                                if (*((long long *)v41) != g_1ef1748)
                                    sub_f7df10(v41);
                                v41 = Skybox__get_material();
                                if (v40)
                                {
                                    Skybox__set_material(v40, v41, 0);
                                    goto LABEL_10e29e4;
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    sub_f7db74(v41);
LABEL_10e2d2c:
    sub_f7df10(v41);
}
```

## `PlanarReflection.LateUpdate` — RVA `0xce2d34`

- Decompiled symbol: `PlanarReflection_LateUpdate`
- Metadata signature: `public void LateUpdate() { }`
- Native interval: `88` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[96];
    unsigned long long field_60;
} struct_0;

extern long long g_1ef5220;
extern char g_1fab647;

unsigned long long PlanarReflection_LateUpdate(struct_0 *a0)
{
    if (!(g_1fab647 & 1))
    {
        sub_f7d92c(&g_1ef5220);
        g_1fab647 = 1;
    }
    if (!a0->field_60)
        return 0;
}
```

## `PlanarReflection.WaterTileBeingRendered` — RVA `0xce2d8c`

- Decompiled symbol: `PlanarReflection_WaterTileBeingRendered`
- Metadata signature: `public void WaterTileBeingRendered(Transform tr, Camera currentCam) { }`
- Native interval: `224` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab648;

long long PlanarReflection_WaterTileBeingRendered(long long *ptr, unsigned long a1, long long a2)
{
    long long v0;  // x0
    long long v1;  // x0
    long long v2;  // x0
    unsigned long long v3;  // x0

    if (!(g_1fab648 & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab648 = 1;
    }
    PlanarReflection__RenderHelpCameras(ptr, a2);
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v0 = Object__op_Implicit(ptr[10], 0);
    if (!((char)v0 & 1))
        return v0;
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v1 = Object__op_Implicit(ptr[11], 0);
    if (!((char)v1 & 1))
        return v1;
    v2 = ptr[10];
    if (v2)
    {
        v2 = Camera__get_targetTexture(v2, 0);
        if (ptr[11])
        {
            v3 = Material__SetTexture();
            return Material__SetTexture();
        }
    }
    sub_f7db74(v2);
}
```

## `PlanarReflection.OnEnable` — RVA `0xce2e6c`

- Decompiled symbol: `PlanarReflection_OnEnable`
- Metadata signature: `public void OnEnable() { }`
- Native interval: `100` bytes
- Result: `pseudocode`

```c
extern char g_1fab649;

void PlanarReflection_OnEnable(void)
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
    if (!(g_1fab649 & 1))
    {
        sub_f7d92c(";&");
        sub_f7d92c("?&");
        g_1fab649 = 1;
    }
    Shader__EnableKeyword(g_1f0fad8, 0);
    Shader__DisableKeyword();
    return;
}
```

## `PlanarReflection.OnDisable` — RVA `0xce2ed0`

- Decompiled symbol: `PlanarReflection_OnDisable`
- Metadata signature: `public void OnDisable() { }`
- Native interval: `100` bytes
- Result: `pseudocode`

```c
extern char g_1fab64a;

void PlanarReflection_OnDisable(void)
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
    if (!(g_1fab64a & 1))
    {
        sub_f7d92c(";&");
        sub_f7d92c("?&");
        g_1fab64a = 1;
    }
    Shader__EnableKeyword(g_1f0fae8, 0);
    Shader__DisableKeyword();
    return;
}
```

## `PlanarReflection.SaneCameraSettings` — RVA `0xce2f34`

- Decompiled symbol: `PlanarReflection_SaneCameraSettings`
- Metadata signature: `private void SaneCameraSettings(Camera helperCam) { }`
- Native interval: `96` bytes
- Result: `pseudocode`

```c
void PlanarReflection_SaneCameraSettings(unsigned long a0, long long a1)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    if (!a1)
        sub_f7db74();
    Camera__set_depthTextureMode(a1, 0, 0);
    Camera__set_backgroundColor(a1, 0);
    Camera__set_clearFlags(a1, 2, 0);
}
```

## `PlanarReflection.CalculateReflectionMatrix` — RVA `0xce2f94`

- Decompiled symbol: `PlanarReflection_CalculateReflectionMatrix`
- Metadata signature: `private static Matrix4x4 CalculateReflectionMatrix(Matrix4x4 reflectionMat, Vector4 plane) { }`
- Native interval: `168` bytes
- Result: `pseudocode`

```c
void* PlanarReflection_CalculateReflectionMatrix(void* ptr)
{
    unsigned int v0;  // s0
    unsigned int v1;  // s17
    int v10;  // q3
    uint128_t p[4];  // x8
    unsigned int v2;  // s3
    unsigned int v3;  // s3
    unsigned int v4;  // s1
    unsigned int v5;  // s18
    unsigned int v6;  // s2
    unsigned int v7;  // s6
    int v8;  // q1
    int v9;  // q2

    v1 = v0 * 0xc0000000;
    v3 = v2 * 0xc0000000;
    v5 = v4 * 0xc0000000;
    v7 = v6 * 0xc0000000;
    *((unsigned int *)ptr) = 0x3f800000 - v0 * v0 * 2;
    *((unsigned int *)&ptr[4]) = v0 * v5;
    *((unsigned int *)&ptr[16]) = v4 * v1;
    *((unsigned int *)&ptr[20]) = 0x3f800000 - v4 * v4 * 2;
    *((unsigned int *)&ptr[12]) = 0;
    *((unsigned int *)&ptr[28]) = 0;
    *((unsigned int *)&ptr[44]) = 0;
    *((unsigned int *)&ptr[60]) = 0x3f800000;
    *((unsigned int *)&ptr[32]) = v6 * v1;
    *((unsigned int *)&ptr[36]) = v6 * v5;
    *((unsigned int *)&ptr[48]) = v0 * v3;
    *((unsigned int *)&ptr[52]) = v4 * v3;
    *((unsigned int *)&ptr[8]) = v0 * v7;
    *((unsigned int *)&ptr[40]) = 0x3f800000 - v6 * v6 * 2;
    *((unsigned int *)&ptr[56]) = v6 * v3;
    *((unsigned int *)&ptr[24]) = v4 * v7;
    v8 = (int)(int128_t)ptr[48];
    v9 = (int)*((int128_t *)ptr);
    v10 = (int)(int128_t)ptr[16];
    p[2] = (int128_t)ptr[32];
    *((void*)&p[3]) = v8;
    *((void*)&p[0]) = v9;
    *((void*)&p[1]) = v10;
    return ptr;
}
```

## `PlanarReflection.CameraSpacePlane` — RVA `0xce303c`

- Decompiled symbol: `PlanarReflection_CameraSpacePlane`
- Metadata signature: `private Vector4 CameraSpacePlane(Camera cam, Vector3 pos, Vector3 normal, float sideSign) { }`
- Native interval: `424` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[224];
    unsigned int field_e0;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern long long g_1ef22e8;
extern char g_1fab2c8;
extern char g_1fab2c9;

struct_1 * PlanarReflection_CameraSpacePlane(unsigned long a0, long long a1)
{
    struct_0 *v8;  // x0
    unsigned int v9;  // s2
    unsigned long v10;  // 4205
    char v0;  // [bp-0xd0]
    uint128_t v1;  // [bp-0xc0]
    uint128_t v2;  // [bp-0xb0]
    uint128_t v3;  // [bp-0xa0]
    char flag;  // [bp-0x90], Other Possible Types: uint128_t
    uint128_t v5;  // [bp-0x80]
    uint128_t v6;  // [bp-0x70]
    uint128_t v7;  // [bp-0x60]

    v6 = 0;
    v7 = 0;
    flag = 0;
    v5 = 0;
    if (a1)
    {
        Camera__get_worldToCameraMatrix(a1, 0);
        memcpy(&flag, &v0, 16);
        v5 = v1;
        v6 = v2;
        v7 = v3;
        Matrix4x4__MultiplyPoint(&flag, 0);
        Matrix4x4__MultiplyVector(&flag, 0);
        if (!g_1fab2c8)
        {
            sub_f7d92c("_F");
            g_1fab2c8 = 1;
        }
        v8 = g_1ef07e8;
        if (!g_1ef07e8->field_e0)
            v8 = sub_f7da5c(g_1ef07e8);
        v9 = [D] unsupported_Iop_SqrtF32();
        v10 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v9, 925353388)) >> 5 & 3 | (unsigned long long)(CmpF(v9, 925353388) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v9, 925353388)) >> 5 & 3 | (unsigned long long)(CmpF(v9, 925353388) & 1)) & ((unsigned long long)(char)(CmpF(v9, 925353388)) >> 5 & 3 | (unsigned long long)(CmpF(v9, 925353388) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if (!((char)v10))
            return v8;
        if (!g_1fab2c9)
        {
            v8 = sub_f7d92c(&g_1ef22e8);
            g_1fab2c9 = 1;
        }
        return v8;
    }
    sub_f7db74();
}
```

## `PlanarReflection.CalculateObliqueMatrix` — RVA `0xce31e4`

- Decompiled symbol: `PlanarReflection_CalculateObliqueMatrix`
- Metadata signature: `private static Matrix4x4 CalculateObliqueMatrix(Matrix4x4 projection, Vector4 clipPlane) { }`
- Native interval: `392` bytes
- Result: `pseudocode`

```c
unsigned long long PlanarReflection_CalculateObliqueMatrix(uint128_t *p)
{
    unsigned int v12;  // s0
    unsigned long v13;  // 4157
    uint128_t ptr[4];  // x8
    unsigned long v14;  // 4102
    unsigned int v15;  // s1
    unsigned long v16;  // 4125
    unsigned long v17;  // 4102
    unsigned long long v18;  // x0
    uint128_t v19;  // q0
    uint128_t v20;  // q3
    uint128_t v21;  // q2
    char v0;  // [bp-0x100]
    uint128_t v1;  // [bp-0xf0]
    uint128_t v2;  // [bp-0xe0]
    uint128_t v3;  // [bp-0xd0]
    char v4;  // [bp-0xc0]
    uint128_t v5;  // [bp-0xb0]
    uint128_t v6;  // [bp-0xa0]
    uint128_t v7;  // [bp-0x90]
    char v8;  // [bp-0x80]
    uint128_t v9;  // [bp-0x70]
    uint128_t v10;  // [bp-0x60]
    uint128_t v11;  // [bp-0x50]

    Matrix4x4__get_inverse();
    memcpy(&v8, &v4, 16);
    v9 = v5;
    v10 = v6;
    v11 = v7;
    v13 = arm64g_calculate_condition(192, (((((unsigned long long)(char)(CmpF(v12, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v12, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v12, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v12, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v12, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v12, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if (!((char)v13))
        v14 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(v12, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v12, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v12, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v12, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v12, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v12, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    v16 = arm64g_calculate_condition(192, (((((unsigned long long)(char)(CmpF(v15, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v15, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v15, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v15, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v15, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v15, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if (!((char)v16))
        v17 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(v15, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v15, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v15, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v15, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v15, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v15, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    memcpy(&v0, &v8, 16);
    v1 = v9;
    v2 = v10;
    v3 = v11;
    Matrix4x4__op_Multiply(&v0, 0);
    Matrix4x4__get_Item(p, 3, 0);
    Matrix4x4__set_Item(p, 2, 0);
    Matrix4x4__get_Item(p, 7, 0);
    Matrix4x4__set_Item(p, 6, 0);
    Matrix4x4__get_Item(p, 11, 0);
    Matrix4x4__set_Item(p, 10, 0);
    Matrix4x4__get_Item(p, 15, 0);
    v18 = Matrix4x4__set_Item(p, 14, 0);
    v19 = p[3];
    v20 = *(p);
    v21 = p[1];
    ptr[2] = p[2];
    ptr[3] = v19;
    ptr[0] = v20;
    ptr[1] = v21;
    return v18;
}
```

## `PlanarReflection.Sgn` — RVA `0xce336c`

- Decompiled symbol: `PlanarReflection_Sgn`
- Metadata signature: `private static float Sgn(float a) { }`
- Native interval: `28` bytes
- Result: `pseudocode`

```c
long long PlanarReflection_Sgn(void)
{
    unsigned int v0;  // s0
    unsigned long v1;  // 4125
    unsigned long v2;  // 4102
    unsigned long v3;  // x0

    v1 = arm64g_calculate_condition(192, (((((unsigned long long)(char)(CmpF(v0, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v0, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v0, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v0, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v0, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v0, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if (!((char)v1))
        v2 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(v0, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v0, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v0, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v0, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v0, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v0, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    return v3;
}
```

## `PlanarReflection.ctor` — RVA `0xce3388`

- Decompiled symbol: `PlanarReflection_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `112` bytes
- Result: `pseudocode`
- Heuristic layout hint: `PlanarReflection_Recovered` matched 3 offsets against `PlanarReflection` metadata (confidence 1.00).

```c
typedef struct PlanarReflection_Recovered {
    char padding_0[40];
    uint128_t clearColor;
    long long reflectionSampler;
    unsigned int clipPlaneOffset;
} PlanarReflection_Recovered;

extern char g_1fab64c;

void PlanarReflection_ctor(struct_0 *ptr)
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
    if (!(g_1fab64c & 1))
    {
        sub_f7d92c("q)");
        g_1fab64c = 1;
    }
    *((uint128_t *)&(&ptr->padding_0)[1]) = 0x3f8000003f0000003f0000003f000000;
    *((long long *)((char *)&ptr->field_28 + 8)) = g_1f107b0;
    sub_f7d8d0((struct PlanarReflection_Recovered *)((char *)&ptr->field_28 + 8), g_1f107b0);
    *((unsigned int *)&ptr->field_38) = 1032805417;
    MonoBehaviour__ctor();
    return;
}
```
