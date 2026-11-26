# Native pseudocode: Water

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `Water.OnWillRenderObject` — RVA `0xce3740`

- Decompiled symbol: `Water_OnWillRenderObject`
- Metadata signature: `public void OnWillRenderObject() { }`
- Native interval: `2472` bytes
- Result: `pseudocode`
- Heuristic layout hint: `Water_Recovered` matched 5 offsets against `Water` metadata (confidence 1.00).

```c
typedef struct Water_Recovered {
    char padding_0[32];
    int waterMode;
    char disablePixelLights;
    char padding_25[35];
    long long m_ReflectionTexture;
    long long m_RefractionTexture;
    int m_HardwareWaterSupport;
} Water_Recovered;

typedef struct struct_2 {
    char field_0;
} struct_2;

typedef struct struct_1 {
    char padding_0[184];
    struct struct_2 *field_b8;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern struct_1 *g_1ef2468;
extern long long g_1efd070;
extern char g_1fab64f;

long long Water_OnWillRenderObject(struct_3 *ptr)
{
    long long v83;  // x0
    long long v84;  // x0
    int flag5;  // w25
    unsigned int v94;  // w0
    long long v95;  // x0
    unsigned int v96;  // s2
    unsigned int v97;  // s2
    long long v98;  // x22
    unsigned int v99;  // s1
    long long v100;  // x22
    long long v101;  // x22
    long long v102;  // x22
    long long v85;  // x0
    unsigned int v103;  // w0
    long long v104;  // x0
    unsigned int v105;  // w0
    long long v106;  // x22
    long long v107;  // x22
    long long v108;  // x22
    unsigned int v109;  // w0
    long long v110;  // x22
    long long v111;  // x22
    long long v86;  // x0
    long long v87;  // x0
    long long v88;  // x0
    long long v89;  // x20
    long long v90;  // x0
    int v91;  // w0
    int v92;  // w8
    unsigned int flag;  // [bp-0x53c]
    unsigned int v1;  // [bp-0x538]
    unsigned int v2;  // [bp-0x534]
    unsigned int v3;  // [bp-0x530]
    unsigned int v4;  // [bp-0x52c]
    unsigned int v5;  // [bp-0x528]
    unsigned int choice;  // [bp-0x524]
    char v7;  // [bp-0x520]
    uint128_t v8;  // [bp-0x510]
    uint128_t v9;  // [bp-0x500]
    uint128_t v10;  // [bp-0x4f0]
    char v11;  // [bp-0x4e0]
    uint128_t v12;  // [bp-0x4d0]
    uint128_t v13;  // [bp-0x4c0]
    uint128_t v14;  // [bp-0x4b0]
    int v15;  // [bp-0x4a0]
    uint128_t v16;  // [bp-0x490]
    uint128_t v17;  // [bp-0x480]
    uint128_t v18;  // [bp-0x470]
    char v19;  // [bp-0x460]
    uint128_t v20;  // [bp-0x450]
    uint128_t v21;  // [bp-0x440]
    uint128_t v22;  // [bp-0x430]
    char v23;  // [bp-0x420]
    uint128_t v24;  // [bp-0x410]
    uint128_t v25;  // [bp-0x400]
    uint128_t v26;  // [bp-0x3f0]
    int v27;  // [bp-0x3e0]
    uint128_t v28;  // [bp-0x3d0]
    uint128_t v29;  // [bp-0x3c0]
    uint128_t v30;  // [bp-0x3b0]
    char v31;  // [bp-0x3a0]
    uint128_t v32;  // [bp-0x390]
    uint128_t v33;  // [bp-0x380]
    uint128_t v34;  // [bp-0x370]
    int v35;  // [bp-0x360]
    uint128_t v36;  // [bp-0x350]
    uint128_t v37;  // [bp-0x340]
    uint128_t v38;  // [bp-0x330]
    char v39;  // [bp-0x320]
    uint128_t v40;  // [bp-0x310]
    uint128_t v41;  // [bp-0x300]
    uint128_t v42;  // [bp-0x2f0]
    char v43;  // [bp-0x2e0]
    uint128_t v44;  // [bp-0x2d0]
    uint128_t v45;  // [bp-0x2c0]
    uint128_t v46;  // [bp-0x2b0]
    char v47;  // [bp-0x2a0]
    uint128_t v48;  // [bp-0x290]
    uint128_t v49;  // [bp-0x280]
    uint128_t v50;  // [bp-0x270]
    char v51;  // [bp-0x260]
    uint128_t v52;  // [bp-0x250]
    uint128_t v53;  // [bp-0x240]
    uint128_t v54;  // [bp-0x230]
    char v55;  // [bp-0x220]
    uint128_t v56;  // [bp-0x210]
    uint128_t v57;  // [bp-0x200]
    uint128_t v58;  // [bp-0x1f0]
    int v59;  // [bp-0x1e0]
    uint128_t v60;  // [bp-0x1d0]
    uint128_t v61;  // [bp-0x1c0]
    uint128_t v62;  // [bp-0x1b0]
    char v63;  // [bp-0x1a0]
    uint128_t v64;  // [bp-0x190]
    uint128_t v65;  // [bp-0x180]
    uint128_t v66;  // [bp-0x170]
    char v67;  // [bp-0x160]
    uint128_t v68;  // [bp-0x150]
    uint128_t v69;  // [bp-0x140]
    uint128_t v70;  // [bp-0x130]
    char v71;  // [bp-0x120]
    uint128_t v72;  // [bp-0x110]
    uint128_t v73;  // [bp-0x100]
    uint128_t v74;  // [bp-0xf0]
    int flag4;  // [bp-0xe0]
    uint128_t v76;  // [bp-0xd0]
    uint128_t v77;  // [bp-0xc0]
    uint128_t v78;  // [bp-0xb0]
    long long flag3;  // [bp-0x98]
    char *v80;  // [bp-0x50]
    long long flag2;  // [bp-0x48]
    char v82;  // [bp+0x0]

    v80 = &v82;
    if (!(g_1fab64f & 1))
    {
        sub_f7d92c(&g_1efd070);
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c(&g_1ef2468);
        sub_f7d92c(";&");
        sub_f7d92c("})");
        sub_f7d92c("=&");
        sub_f7d92c("q)");
        sub_f7d92c("?&");
        g_1fab64f = 1;
    }
    flag2 = 0;
    flag3 = 0;
    v78 = 0;
    v77 = 0;
    v76 = 0;
    flag4 = 0;
    v83 = Behaviour__get_enabled(ptr, 0);
    if (!((char)v83 & 1))
        return v83;
    v84 = sub_1231bc8(ptr, g_1efd070);
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v85 = Object__op_Implicit(v84, 0);
    if (!((char)v85 & 1))
        return v85;
    if (sub_1231bc8(ptr, g_1efd070))
    {
        v86 = Renderer__get_sharedMaterial();
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        v87 = Object__op_Implicit(v86, 0);
        if (!((char)v87 & 1))
            return v87;
        if (sub_1231bc8(ptr, g_1efd070))
        {
            v88 = Renderer__get_enabled();
            if (!((char)v88 & 1))
                return v88;
            v89 = Camera__get_current(0);
            if (!g_1ef0c58->field_e0)
                sub_f7da5c(g_1ef0c58);
            v90 = Object__op_Implicit(v89, 0);
            if (!((char)v90 & 1))
                return v90;
            if (g_1ef2468->field_b8->field_0)
                return v90;
            g_1ef2468->field_b8->field_0 = 1;
            v91 = Water__FindHardwareWaterSupport();
            v92 = ptr->field_20;
            ptr->field_58 = v91;
            if (v91 < v92)
                flag5 = v91;
            else
                flag5 = v92;
            Water__CreateWaterObjects();
            if (Component__get_transform(ptr, 0) && (Transform__get_position(), Component__get_transform(ptr, 0)))
            {
                Transform__get_up();
                v94 = QualitySettings__get_pixelLightCount(0);
                if (ptr->field_24)
                    QualitySettings__set_pixelLightCount(0, 0);
                v95 = Water__UpdateCameraModes(Water__UpdateCameraModes(), v89, flag3);
                if (flag5 >= 1)
                {
                    Matrix4x4__get_zero(0);
                    memcpy(&flag4, &v71, 16);
                    v76 = v72;
                    v77 = v73;
                    v78 = v74;
                    v97 = v96;
                    Water__CalculateReflectionMatrix(&flag4);
                    if (v89 && Component__get_transform(v89, 0))
                    {
                        Transform__get_position();
                        v3 = v97;
                        Matrix4x4__MultiplyPoint(&flag4, 0);
                        v98 = flag2;
                        v5 = v99;
                        choice = 0;
                        v4 = v97;
                        Camera__get_worldToCameraMatrix(v89, 0);
                        memcpy(&v63, &v71, 16);
                        v64 = v72;
                        v65 = v73;
                        v66 = v74;
                        v59 = flag4;
                        v60 = v76;
                        v61 = v77;
                        v62 = v78;
                        Matrix4x4__op_Multiply(&v63, &v59, 0);
                        memcpy(&v71, &v67, 16);
                        v72 = v68;
                        v73 = v69;
                        v74 = v70;
                        if (v98)
                        {
                            memcpy(&v55, &v71, 16);
                            v56 = v72;
                            v57 = v73;
                            v58 = v74;
                            Camera__set_worldToCameraMatrix(v98, &v55, 0);
                            Water__CameraSpacePlane(ptr, flag2);
                            v100 = flag2;
                            Camera__CalculateObliqueMatrix(v89, 0);
                            memcpy(&v67, &v51, 16);
                            v68 = v52;
                            v69 = v53;
                            v70 = v54;
                            if (v100)
                            {
                                memcpy(&v47, &v67, 16);
                                v48 = v68;
                                v49 = v69;
                                v50 = v70;
                                Camera__set_projectionMatrix(v100, &v47, 0);
                                v101 = flag2;
                                Camera__get_projectionMatrix(v89, 0);
                                memcpy(&v51, &v43, 16);
                                v52 = v44;
                                v53 = v45;
                                v54 = v46;
                                Camera__get_worldToCameraMatrix(v89, 0);
                                memcpy(&v31, &v43, 16);
                                v32 = v44;
                                v33 = v45;
                                v34 = v46;
                                v35 = (int)*((int128_t *)&v51);
                                v36 = v52;
                                v37 = v53;
                                v38 = v54;
                                Matrix4x4__op_Multiply(&v35, &v31, 0);
                                memcpy(&v43, &v39, 16);
                                v44 = v40;
                                v45 = v41;
                                v46 = v42;
                                if (v101)
                                {
                                    v2 = v96;
                                    v27 = (int)*((int128_t *)&v43);
                                    v28 = v44;
                                    v29 = v45;
                                    v30 = v46;
                                    Camera__set_cullingMatrix(v101, &v27, 0);
                                    v102 = flag2;
                                    v103 = LayerMask__get_value(&ptr->padding_25[11], 0);
                                    if (v102 && (v1 = v99, Camera__set_cullingMask(v102, (unsigned long long)(v103 & 4294967279), 0), v104 = flag2, v104))
                                    {
                                        flag = 0;
                                        Camera__set_targetTexture(v104, ptr->field_48, 0);
                                        v105 = GL__get_invertCulling(0);
                                        GL__set_invertCulling(~(v105) & 1, 0);
                                        if (flag2 && Component__get_transform(flag2, 0) && (Transform__set_position(), Component__get_transform(v89, 0) && (Transform__get_eulerAngles(), flag2 && Component__get_transform(flag2, 0) && (Transform__set_eulerAngles(), flag2 && (Camera__Render(flag2, 0), flag2 && Component__get_transform(flag2, 0))))))
                                        {
                                            Transform__set_position();
                                            GL__set_invertCulling(v105 & 1, 0);
                                            if (sub_1231bc8(ptr, g_1efd070) && Renderer__get_sharedMaterial())
                                            {
                                                v95 = Material__SetTexture();
                                                if (flag5 < 2)
                                                    goto LABEL_10e3fdc;
                                                v106 = flag3;
                                                Camera__get_worldToCameraMatrix(v89, 0);
                                                memcpy(&v71, &v67, 16);
                                                v72 = v68;
                                                v73 = v69;
                                                v74 = v70;
                                                if (v106)
                                                {
                                                    memcpy(&v23, &v71, 16);
                                                    v24 = v72;
                                                    v25 = v73;
                                                    v26 = v74;
                                                    Camera__set_worldToCameraMatrix(v106, &v23, 0);
                                                    Water__CameraSpacePlane(ptr, flag3);
                                                    v107 = flag3;
                                                    Camera__CalculateObliqueMatrix(v89, 0);
                                                    memcpy(&v67, &v51, 16);
                                                    v68 = v52;
                                                    v69 = v53;
                                                    v70 = v54;
                                                    if (v107)
                                                    {
                                                        memcpy(&v19, &v67, 16);
                                                        v20 = v68;
                                                        v21 = v69;
                                                        v22 = v70;
                                                        Camera__set_projectionMatrix(v107, &v19, 0);
                                                        v108 = flag3;
                                                        Camera__get_projectionMatrix(v89, 0);
                                                        memcpy(&v51, &v43, 16);
                                                        v52 = v44;
                                                        v53 = v45;
                                                        v54 = v46;
                                                        Camera__get_worldToCameraMatrix(v89, 0);
                                                        memcpy(&v11, &v43, 16);
                                                        v12 = v44;
                                                        v13 = v45;
                                                        v14 = v46;
                                                        v15 = (int)*((int128_t *)&v51);
                                                        v16 = v52;
                                                        v17 = v53;
                                                        v18 = v54;
                                                        Matrix4x4__op_Multiply(&v15, &v11, 0);
                                                        memcpy(&v43, &v39, 16);
                                                        v44 = v40;
                                                        v45 = v41;
                                                        v46 = v42;
                                                        if (v108)
                                                        {
                                                            memcpy(&v7, &v43, 16);
                                                            v8 = v44;
                                                            v9 = v45;
                                                            v10 = v46;
                                                            Camera__set_cullingMatrix(v108, &v7, 0);
                                                            v109 = LayerMask__get_value(&ptr->padding_25[15], 0);
                                                            if (...)
                                                            {
                                                                v95 = Material__SetTexture();
                                                                goto LABEL_10e3fdc;
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
                else
                {
LABEL_10e3fdc:
                    if (ptr->field_24)
                        v95 = QualitySettings__set_pixelLightCount(v94, 0);
                    if (flag5 == 2)
                    {
                        Shader__DisableKeyword(g_1f0fae8, 0);
                        Shader__DisableKeyword(g_1f0fad8, 0);
                        v95 = Shader__EnableKeyword(g_1f0fae0, 0);
                        g_1ef2468->field_b8->field_0 = 0;
                        return v95;
                    }
                    if (flag5 == 1)
                    {
                        Shader__DisableKeyword(g_1f0fae8, 0);
                        Shader__EnableKeyword(g_1f0fad8, 0);
                    }
                    else if (!flag5)
                    {
                        Shader__EnableKeyword(g_1f0fae8, 0);
                        Shader__DisableKeyword(g_1f0fad8, 0);
                    }
                    else
                    {
                        g_1ef2468->field_b8->field_0 = 0;
                        return v95;
                    }
                    v95 = Shader__DisableKeyword(g_1f0fae0, 0);
                    g_1ef2468->field_b8->field_0 = 0;
                    return v95;
                }
            }
        }
    }
    sub_f7db74();
}
```

## `Water.FindHardwareWaterSupport` — RVA `0xce40e8`

- Decompiled symbol: `Water_FindHardwareWaterSupport`
- Metadata signature: `private Water.WaterMode FindHardwareWaterSupport() { }`
- Native interval: `352` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern long long g_1efd070;
extern long long g_1f0d3a0;
extern long long g_1f0d3a8;
extern char g_1fab654;

unsigned int Water_FindHardwareWaterSupport(long long a0)
{
    long long v0;  // x0
    long long v1;  // x19
    long long v2;  // x0

    if (!(g_1fab654 & 1))
    {
        sub_f7d92c(&g_1efd070);
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c("5&");
        sub_f7d92c(&g_1f0d3a0);
        sub_f7d92c(&g_1f0d3a8);
        g_1fab654 = 1;
    }
    v0 = sub_1231bc8(a0, g_1efd070);
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (!((char)Object__op_Implicit(v0, 0) & 1))
        return 0;
    if (sub_1231bc8(a0, g_1efd070))
    {
        v1 = Renderer__get_sharedMaterial();
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        if (!((char)Object__op_Implicit(v1, 0) & 1))
        {
            return 0;
        }
        else if (v1)
        {
            v2 = Material__GetTag(v1, g_1f0fac0, 0, 0);
            if (!((char)String__op_Equality(v2, g_1f0d3a8, 0, 0) & 1))
                return String__op_Equality(v2, g_1f0d3a0, 0) & 1;
            return 2;
        }
    }
    sub_f7db74();
}
```

## `Water.GetWaterMode` — RVA `0xce4248`

- Decompiled symbol: `Water_GetWaterMode`
- Metadata signature: `private Water.WaterMode GetWaterMode() { }`
- Native interval: `20` bytes
- Result: `pseudocode`
- Heuristic layout hint: `Water_Recovered` matched 2 offsets against `Water` metadata (confidence 1.00).

```c
typedef struct Water_Recovered {
    char padding_0[32];
    int waterMode;
    char padding_24[52];
    unsigned int m_HardwareWaterSupport;
} Water_Recovered;

long long Water_GetWaterMode(struct_0 *a0)
{
    if (a0->field_58 >= a0->field_20)
        return a0->field_20;
    return a0->field_58;
}
```

## `Water.CreateWaterObjects` — RVA `0xce425c`

- Decompiled symbol: `Water_CreateWaterObjects`
- Metadata signature: `private void CreateWaterObjects(Camera currentCamera, out Camera reflectionCamera, out Camera refractionCamera) { }`
- Native interval: `2376` bytes
- Result: `pseudocode`
- Heuristic layout hint: `Water_Recovered` matched 8 offsets against `Water` metadata (confidence 1.00).

```c
typedef struct Water_Recovered {
    char padding_0[32];
    int waterMode;
    char padding_24[4];
    unsigned int textureSize;
    char padding_2c[12];
    char m_ReflectionCameras;
    char padding_39[7];
    char m_RefractionCameras;
    char padding_41[7];
    char m_ReflectionTexture;
    char padding_49[7];
    char m_RefractionTexture;
    char padding_51[11];
    unsigned int m_OldReflectionTextureSize;
    unsigned int m_OldRefractionTextureSize;
} Water_Recovered;

typedef struct struct_3 {
    struct struct_2 *field_0;
    char padding_8[16];
    unsigned int field_18;
    char padding_1c[4];
    char field_20;
    char padding_21[7];
    char field_28;
} struct_3;

typedef struct struct_6 {
    struct struct_5 *field_0;
    char padding_8[16];
    unsigned int field_18;
    char padding_1c[4];
    char field_20;
    char padding_21[7];
    char field_28;
} struct_6;

typedef struct struct_2 {
    char padding_0[64];
    long long field_40;
} struct_2;

typedef struct struct_5 {
    char padding_0[64];
    long long field_40;
} struct_5;

typedef struct struct_1 {
    char padding_0[224];
    unsigned int field_e0;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern long long g_1eeb9a0;
extern long long g_1eee3d8;
extern long long g_1eefaf0;
extern struct_0 *g_1ef0c58;
extern long long g_1ef1298;
extern struct_1 *g_1ef1f08;
extern long long g_1ef5258;
extern long long g_1ef5260;
extern long long g_1efeab0;
extern long long g_1efeb60;
extern long long g_1f066f0;
extern char g_1fab653;

long long Water_CreateWaterObjects(struct_4 *ptr, long long a1, void* p, void* addr)
{
    unsigned int v1;  // w8
    unsigned int v2;  // w9
    long long v10;  // x0
    long long v11;  // x0
    struct_3 *v12;  // x25
    unsigned long v13;  // x0
    unsigned long v14;  // x23
    struct_3 *ptr5;  // x0
    unsigned long v16;  // x23
    struct_3 *ptr6;  // x0
    long long v18;  // x0
    long long v19;  // x23
    unsigned int v3;  // w27
    unsigned long v20;  // x0
    long long v21;  // x24
    long long v22;  // x24
    struct_4 *v23;  // x22
    struct_4 *ptr3;  // x22
    unsigned long v25;  // x24
    long long v26;  // x0
    unsigned long v27;  // x0
    long long v28;  // x0
    long long v29;  // x0
    unsigned long v4;  // x0
    struct_6 *v30;  // x24
    unsigned long v31;  // x22
    struct_6 *ptr7;  // x0
    unsigned long v33;  // x22
    struct_6 *ptr8;  // x0
    long long v35;  // x0
    long long v36;  // x22
    unsigned long v37;  // x0
    long long v38;  // x23
    long long v39;  // x23
    struct_4 *v5;  // x23
    unsigned long long v40;  // x0
    struct_4 *ptr4;  // x23
    unsigned long v7;  // x25
    long long v8;  // x0
    unsigned long v9;  // x0
    unsigned int v0;  // [bp-0x54]

    if (!(g_1fab653 & 1))
    {
        sub_f7d92c("O1");
        sub_f7d92c(&g_1ef5258);
        sub_f7d92c(&g_1ef5260);
        sub_f7d92c(&g_1efeab0);
        sub_f7d92c(&g_1efeb60);
        sub_f7d92c(&g_1eefaf0);
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c(&g_1ef1298);
        sub_f7d92c(&g_1eeb9a0);
        sub_f7d92c(&g_1eee3d8);
        sub_f7d92c(&g_1ef1f08);
        sub_f7d92c("U&");
        sub_f7d92c("s*");
        sub_f7d92c("q*");
        sub_f7d92c("W&");
        sub_f7d92c(&g_1f066f0);
        g_1fab653 = 1;
    }
    v0 = 0;
    v1 = *((int *)&ptr->padding_51[7]);
    v2 = ptr->field_20;
    *((unsigned long *)p) = 0;
    if (v1 < v2)
        v3 = v1;
    else
        v3 = v2;
    sub_f7d8d0();
    *((unsigned long *)addr) = 0;
    v4 = sub_f7d8d0(addr, 0);
    if (v3 < 1)
        return v4;
    v5 = ptr;
    ptr4 = &v5->field_48;
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (!((char)Object__op_Implicit(*((long long *)&v5->field_48), 0) & 1) || ptr->field_5c != ptr->field_28)
    {
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        if (((char)Object__op_Implicit(*((long long *)&ptr4->padding_0[0]), 0) & 1))
        {
            if (!g_1ef0c58->field_e0)
                sub_f7da5c(g_1ef0c58);
            Object__DestroyImmediate(*((long long *)&ptr4->padding_0[0]), 0);
        }
        v7 = sub_f7db70(g_1ef1298);
        RenderTexture__ctor(v7, ptr->field_28, ptr->field_28, 16, 0);
        *((unsigned long *)&ptr->field_48) = v7;
        sub_f7d8d0(ptr4, v7);
        v0 = Object__GetInstanceID(ptr, 0);
        v8 = Int32__ToString(&v0, 0);
        v13 = String__Concat(g_1f10bb0, v8, 0);
        if (*((long long *)&ptr->field_48) && !((Object__set_name(*((long long *)&ptr->field_48), v13, 0), v13 = (unsigned long)*((long long *)&ptr4->padding_0[0]), !v13 || (RenderTexture__set_isPowerOfTwo(v13, 1, 0), v13 = (unsigned long)*((long long *)&ptr4->padding_0[0]), !v13))))
        {
            Object__set_hideFlags(v13, 52, 0);
            ptr->field_5c = ptr->field_28;
            goto LABEL_10e44d4;
        }
    }
    else
    {
LABEL_10e44d4:
        v13 = *((long long *)&ptr->field_38);
        if (v13)
        {
            sub_12b29e0(v13, a1, p, g_1ef5258);
            if (!g_1ef0c58->field_e0)
                sub_f7da5c(g_1ef0c58);
            v9 = Object__op_Implicit(*((long long *)p), 0);
            if (!((char)v9 & 1))
            {
                v0 = Object__GetInstanceID(ptr, 0);
                v13 = Int32__ToString(&v0, 0);
                if (a1)
                {
                    v0 = Object__GetInstanceID(a1, 0);
                    v10 = Int32__ToString(&v0, 0);
                    v11 = String__Concat(g_1f0fb40, v13, g_1f066f0, v10, 0);
                    v12 = sub_f7d9d4(g_1eee3d8, 2);
                    if (!g_1ef1f08->field_e0)
                        sub_f7da5c(g_1ef1f08);
                    v13 = Type__GetTypeFromHandle(g_1eeb1f0, 0);
                    if (v12)
                    {
                        v14 = v13;
                        if (v13 && (v13 = (unsigned long)sub_f7da60(v14, v12->field_0->field_40), !v13))
                            goto LABEL_10e4b98;
                        if (!v12->field_18)
                            goto LABEL_10e4b94;
                        ptr5 = v12;
                        *((unsigned long *)&ptr5->field_20) = v14;
                        sub_f7d8d0((struct struct_3 *)&ptr5->field_20, v14);
                        v13 = Type__GetTypeFromHandle(g_1eeb9a0, 0);
                        v16 = v13;
                        if (v13 && (v13 = (unsigned long)sub_f7da60(v16, v12->field_0->field_40), !v13))
                            goto LABEL_10e4b98;
                        if (v12->field_18 <= 1)
                            goto LABEL_10e4b94;
                        ptr6 = v12;
                        *((unsigned long *)&ptr6->field_28) = v16;
                        sub_f7d8d0((struct struct_3 *)&ptr6->field_28, v16);
                        v18 = sub_f7db70(g_1eefaf0);
                        v19 = v18;
                        v13 = GameObject__ctor(v18, v11, v12, 0);
                        if (v19)
                        {
                            v20 = sub_1249224(v19, g_1efeb60);
                            *((unsigned long *)p) = v20;
                            sub_f7d8d0(p, v20);
                            v13 = *((long long *)p);
                            if (v13 && !((Behaviour__set_enabled(v13, 0, 0), v13 = (unsigned long)*((long long *)p), !v13)))
                            {
                                v21 = Component__get_transform(v13, 0);
                                v13 = Component__get_transform(ptr, 0);
                                if (v13 && !((v13 = (unsigned long)(unsigned long long)Transform__get_position(), !v21 || (Transform__set_position(v21, 0), v13 = (unsigned long)*((long long *)p), !v13))))
                                {
                                    v22 = Component__get_transform(v13, 0);
                                    v13 = Component__get_transform(ptr, 0);
                                    if (v13 && !((v13 = (unsigned long)(unsigned long long)Transform__get_rotation(), !v22 || (Transform__set_rotation(v22, 0), v13 = (unsigned long)*((long long *)p), !v13 || (v13 = (unsigned long)Component__get_gameObject(v13, 0), !v13)))))
                                    {
                                        sub_124913c();
                                        Object__set_hideFlags(v19, 61, 0);
                                        v13 = *((long long *)&ptr->field_38);
                                        if (v13)
                                        {
                                            v9 = sub_12b11c0(v13, a1, *((long long *)p), g_1ef5260);
                                            goto LABEL_10e4788;
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
            else
            {
LABEL_10e4788:
                if (v3 < 2)
                    return v9;
                v23 = ptr;
                ptr3 = &v23->field_50;
                if (!g_1ef0c58->field_e0)
                    sub_f7da5c(g_1ef0c58);
                if (!((char)Object__op_Implicit(*((long long *)&v23->field_50), 0) & 1) || ptr->field_60 != ptr->field_28)
                {
                    if (!g_1ef0c58->field_e0)
                        sub_f7da5c(g_1ef0c58);
                    if (((char)Object__op_Implicit(*((long long *)&ptr3->padding_0[0]), 0) & 1))
                    {
                        if (!g_1ef0c58->field_e0)
                            sub_f7da5c(g_1ef0c58);
                        Object__DestroyImmediate(*((long long *)&ptr3->padding_0[0]), 0);
                    }
                    v25 = sub_f7db70(g_1ef1298);
                    RenderTexture__ctor(v25, ptr->field_28, ptr->field_28, 16, 0);
                    *((unsigned long *)&ptr->field_50) = v25;
                    sub_f7d8d0(ptr3, v25);
                    v0 = Object__GetInstanceID(ptr, 0);
                    v26 = Int32__ToString(&v0, 0);
                    v13 = String__Concat(g_1f10bb8, v26, 0);
                    if (*((long long *)&ptr->field_50) && !((Object__set_name(*((long long *)&ptr->field_50), v13, 0), v13 = (unsigned long)*((long long *)&ptr3->padding_0[0]), !v13 || (RenderTexture__set_isPowerOfTwo(v13, 1, 0), v13 = (unsigned long)*((long long *)&ptr3->padding_0[0]), !v13))))
                    {
                        Object__set_hideFlags(v13, 52, 0);
                        ptr->field_60 = ptr->field_28;
                        goto LABEL_10e48c8;
                    }
                }
                else
                {
LABEL_10e48c8:
                    v13 = *((long long *)&ptr->field_40);
                    if (v13)
                    {
                        sub_12b29e0(v13, a1, addr, g_1ef5258);
                        if (!g_1ef0c58->field_e0)
                            sub_f7da5c(g_1ef0c58);
                        v27 = Object__op_Implicit(*((long long *)addr), 0);
                        if (((char)v27 & 1))
                            return v27;
                        v0 = Object__GetInstanceID(ptr, 0);
                        v13 = Int32__ToString(&v0, 0);
                        if (a1)
                        {
                            v0 = Object__GetInstanceID(a1, 0);
                            v28 = Int32__ToString(&v0, 0);
                            v29 = String__Concat(g_1f0fb48, v13, g_1f066f0, v28, 0);
                            v30 = sub_f7d9d4(g_1eee3d8, 2);
                            if (!g_1ef1f08->field_e0)
                                sub_f7da5c(g_1ef1f08);
                            v13 = Type__GetTypeFromHandle(g_1eeb1f0, 0);
                            if (v30)
                            {
                                v31 = v13;
                                if (v13 && (v13 = (unsigned long)sub_f7da60(v31, v30->field_0->field_40), !v13))
                                    goto LABEL_10e4b98;
                                if (!v30->field_18)
                                    goto LABEL_10e4b94;
                                ptr7 = v30;
                                *((unsigned long *)&ptr7->field_20) = v31;
                                sub_f7d8d0((struct struct_6 *)&ptr7->field_20, v31);
                                v13 = Type__GetTypeFromHandle(g_1eeb9a0, 0);
                                v33 = v13;
                                if (v13 && (v13 = (unsigned long)sub_f7da60(v33, v30->field_0->field_40), !v13))
                                    goto LABEL_10e4b98;
                                if (v30->field_18 <= 1)
                                    goto LABEL_10e4b94;
                                ptr8 = v30;
                                *((unsigned long *)&ptr8->field_28) = v33;
                                sub_f7d8d0((struct struct_6 *)&ptr8->field_28, v33);
                                v35 = sub_f7db70(g_1eefaf0);
                                v36 = v35;
                                v13 = GameObject__ctor(v35, v29, v30, 0);
                                if (v36)
                                {
                                    v37 = sub_1249224(v36, g_1efeb60);
                                    *((unsigned long *)addr) = v37;
                                    sub_f7d8d0(addr, v37);
                                    v13 = *((long long *)addr);
                                    if (v13)
                                    {
                                        Behaviour__set_enabled(v13, 0, 0);
                                        v13 = *((long long *)addr);
                                        if (v13)
                                        {
                                            v38 = Component__get_transform(v13, 0);
                                            v13 = Component__get_transform(ptr, 0);
                                            if (v13)
                                            {
                                                v13 = Transform__get_position();
                                                if (v38)
                                                {
                                                    Transform__set_position(v38, 0);
                                                    v13 = *((long long *)addr);
                                                    if (v13)
                                                    {
                                                        v39 = Component__get_transform(v13, 0);
                                                        v13 = Component__get_transform(ptr, 0);
                                                        if (v13)
                                                        {
                                                            v13 = Transform__get_rotation();
                                                            if (v39)
                                                            {
                                                                Transform__set_rotation(v39, 0);
                                                                v13 = *((long long *)addr);
                                                                if (v13)
                                                                {
                                                                    v13 = Component__get_gameObject(v13, 0);
                                                                    if (v13)
                                                                    {
                                                                        sub_124913c();
                                                                        Object__set_hideFlags(v36, 61, 0);
                                                                        v13 = *((long long *)&ptr->field_40);
                                                                        if (v13)
                                                                        {
                                                                            v40 = sub_12b11c0(v13, a1, *((long long *)addr), g_1ef5260);
                                                                            return sub_12b11c0(v13, a1, *((long long *)addr), g_1ef5260);
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
            }
        }
    }
    v13 = sub_f7db74(v13);
LABEL_10e4b94:
    v13 = sub_f7db7c(v13);
LABEL_10e4b98:
    sub_f7da4c(sub_f7db98(v13), 0);
}
```

## `Water.UpdateCameraModes` — RVA `0xce4ba4`

- Decompiled symbol: `Water_UpdateCameraModes`
- Metadata signature: `private void UpdateCameraModes(Camera src, Camera dest) { }`
- Native interval: `572` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern long long g_1efd090;
extern char g_1fab652;

long long Water_UpdateCameraModes(unsigned long a0, long long a1, long long a2)
{
    long long v0;  // x0
    unsigned int v1;  // w0
    long long v2;  // x22
    long long v3;  // x21
    long long v4;  // x0
    unsigned long long v7;  // x0

    if (!(g_1fab652 & 1))
    {
        sub_f7d92c(&g_1efd090);
        sub_f7d92c(&g_1ef0c58);
        g_1fab652 = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v0 = Object__op_Equality(a2, 0, 0);
    if (((char)v0 & 1))
        return v0;
    if (a1 && (v1 = (unsigned int)(unsigned long long)Camera__get_clearFlags(a1, 0), a2))
    {
        Camera__set_clearFlags(a2, Camera__get_clearFlags(a1, 0) & 4294967295, 0);
        Camera__get_backgroundColor(a1, 0);
        Camera__set_backgroundColor(a2, 0);
        if (Camera__get_clearFlags(a1, 0) != 1)
        {
LABEL_10e4d3c:
            Camera__get_farClipPlane(a1, 0);
            Camera__set_farClipPlane(a2, 0);
            Camera__get_nearClipPlane(a1, 0);
            Camera__set_nearClipPlane(a2, 0);
            Camera__set_orthographic(a2, Camera__get_orthographic(a1, 0) & 1, 0);
            Camera__get_fieldOfView(a1, 0);
            Camera__set_fieldOfView(a2, 0);
            Camera__get_aspect(a1, 0);
            Camera__set_aspect(a2, 0);
            Camera__get_orthographicSize(a1, 0);
            v7 = Camera__set_orthographicSize();
            return Camera__set_orthographicSize();
        }
        v2 = sub_1231bc8(a1, g_1efd090);
        v3 = sub_1231bc8(a2, g_1efd090);
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        if (!((char)Object__op_Implicit(v2, 0) & 1))
        {
LABEL_10e4d28:
            if (v3)
            {
                Behaviour__set_enabled(v3, 0, 0);
                goto LABEL_10e4d3c;
            }
        }
        else if (v2)
        {
            v4 = Skybox__get_material(v2, 0);
            if (!g_1ef0c58->field_e0)
                sub_f7da5c(g_1ef0c58);
            if (!(Object__op_Implicit(v4, 0) & 1))
                goto LABEL_10e4d28;
            if (v3)
            {
                Behaviour__set_enabled(v3, 1, 0);
                Skybox__set_material(v3, Skybox__get_material(v2, 0), 0);
                goto LABEL_10e4d3c;
            }
        }
    }
    sub_f7db74();
}
```

## `Water.CalculateReflectionMatrix` — RVA `0xce4de0`

- Decompiled symbol: `Water_CalculateReflectionMatrix`
- Metadata signature: `private static void CalculateReflectionMatrix(ref Matrix4x4 reflectionMat, Vector4 plane) { }`
- Native interval: `152` bytes
- Result: `pseudocode`

```c
unsigned int [16] Water_CalculateReflectionMatrix(unsigned int *ptr)
{
    unsigned int v0;  // s0
    unsigned int v1;  // s17
    unsigned int v2;  // s3
    unsigned int v3;  // s3
    unsigned int v4;  // s1
    unsigned int v5;  // s18
    unsigned int v6;  // s2
    unsigned int v7;  // s6

    v1 = v0 * 0xc0000000;
    v3 = v2 * 0xc0000000;
    v5 = v4 * 0xc0000000;
    v7 = v6 * 0xc0000000;
    *(ptr) = 0x3f800000 - v0 * v0 * 2;
    ptr[1] = v0 * v5;
    ptr[4] = v4 * v1;
    ptr[5] = 0x3f800000 - v4 * v4 * 2;
    ptr[3] = 0;
    ptr[7] = 0;
    ptr[11] = 0;
    ptr[8] = v6 * v1;
    ptr[9] = v6 * v5;
    ptr[12] = v0 * v3;
    ptr[13] = v4 * v3;
    ptr[2] = v0 * v7;
    ptr[6] = v4 * v7;
    ptr[10] = 0x3f800000 - v6 * v6 * 2;
    ptr[14] = v6 * v3;
    ptr[15] = 0x3f800000;
    return ptr;
}
```

## `Water.CameraSpacePlane` — RVA `0xce4e78`

- Decompiled symbol: `Water_CameraSpacePlane`
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

struct_1 * Water_CameraSpacePlane(unsigned long a0, long long a1)
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

## `Water.OnDisable` — RVA `0xce5020`

- Decompiled symbol: `Water_OnDisable`
- Metadata signature: `private void OnDisable() { }`
- Native interval: `856` bytes
- Result: `pseudocode`
- Heuristic layout hint: `Water_Recovered` matched 4 offsets against `Water` metadata (confidence 1.00).

```c
typedef struct Water_Recovered {
    char padding_0[56];
    unsigned long long m_ReflectionCameras;
    unsigned long long m_RefractionCameras;
    long long m_ReflectionTexture;
    struct struct_1 *m_RefractionTexture;
} Water_Recovered;

typedef struct struct_1 {
    long long field_0;
} struct_1;

typedef struct struct_2 {
    char padding_0[224];
    unsigned int field_e0;
} struct_2;

extern struct_2 *g_1ef0c58;
extern long long g_1ef5248;
extern long long g_1ef5250;
extern long long g_1ef6708;
extern long long g_1ef6710;
extern long long g_1ef6718;
extern long long g_1ef7038;
extern char g_1fab650;

long long Water_OnDisable(struct_0 *a0)
{
    struct_0 *ptr;  // x19
    struct_0 *v7;  // x20
    long long *ptr4;  // x23
    long long v17;  // x0
    unsigned long v18;  // x0
    struct_0 *v19;  // x0
    unsigned long long *ptr5;  // x0
    unsigned long long v21;  // x20
    struct_0 *v22;  // x0
    long long v24;  // x0
    unsigned long long v25;  // x0
    struct_0 *ptr7;  // x20
    struct_0 *ptr3;  // x20
    long long *p;  // x21
    struct_0 *addr;  // x20
    long long v12;  // x1
    unsigned long v13;  // x0
    long long *v14;  // x25
    long long *ptr8;  // x24
    char v0;  // [bp-0x98]
    uint128_t v1;  // [bp-0x88]
    unsigned long long v2;  // [bp-0x78]
    int flag;  // [bp-0x70], Other Possible Types: char
    uint128_t v4;  // [bp-0x60]
    unsigned long long v5;  // [bp-0x50]

    ptr = a0;
    if (!(g_1fab650 & 1))
    {
        sub_f7d92c(&g_1ef5248);
        sub_f7d92c(&g_1ef5250);
        sub_f7d92c(&g_1ef6708);
        sub_f7d92c(&g_1ef6710);
        sub_f7d92c(&g_1ef6718);
        sub_f7d92c(&g_1ef7038);
        sub_f7d92c(&g_1ef0c58);
        g_1fab650 = 1;
    }
    v5 = 0;
    v7 = ptr;
    flag = 0;
    v4 = 0;
    ptr7 = &v7->field_48;
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (((char)Object__op_Implicit(v7->field_48, 0) & 1))
    {
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        Object__DestroyImmediate(*((long long *)&ptr7->padding_0[0]), 0);
        *((long long *)&ptr7->padding_0[0]) = 0;
        sub_f7d8d0(ptr7, 0);
    }
    ptr3 = ptr;
    p = &ptr3->field_50->field_0;
    addr = &ptr3->field_50;
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v12 = 0;
    if (((char)Object__op_Implicit(p, 0) & 1))
    {
        p = *((long long *)&addr->padding_0[0]);
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        Object__DestroyImmediate(p, 0);
        v12 = 0;
        *((long long **)&addr->padding_0[0]) = NULL;
        sub_f7d8d0(addr, 0);
    }
    v13 = ptr->field_38;
    if (v13)
    {
        v14 = &g_1ef5250;
        ptr8 = &g_1ef6710;
        ptr4 = &g_1ef5248;
        p = &g_1ef6708;
        sub_12b1604(v13, g_1ef5250);
        memcpy(&flag, &v0, 16);
        v4 = v1;
        v5 = v2;
        while (true)
        {
            v12 = g_1ef6710;
            if (!((char)sub_1329144(&flag, g_1ef6710) & 1))
            {
                v12 = g_1ef6708;
                sub_1329264(&flag, g_1ef6708);
                v13 = ptr->field_38;
                if (!v13 || !((v12 = *(ptr4), sub_12b135c(v13, *(ptr4)), v13 = (unsigned long)ptr->field_40, v13)))
                    break;
                sub_12b1604(v13, *(v14));
                memcpy(&flag, &v0, 16);
                v4 = v1;
                v5 = v2;
                while (true)
                {
                    v12 = *(ptr8);
                    if (!((char)sub_1329144(&flag, v12) & 1))
                    {
                        sub_1329264(&flag, *(p));
                        goto LABEL_10e5284;
                    }
                    v18 = *((unsigned long long *)((void*)&v4 + 8));
                    if (!v18)
                        break;
                    v24 = Component__get_gameObject(v18, 0);
                    if (!g_1ef0c58->field_e0)
                        sub_f7da5c(g_1ef0c58);
                    Object__DestroyImmediate(v24, 0);
                }
                break;
            }
            else if (*((unsigned long long *)((void*)&v4 + 8)))
            {
                v17 = Component__get_gameObject(*((unsigned long long *)((void*)&v4 + 8)), 0);
                if (!g_1ef0c58->field_e0)
                    sub_f7da5c(g_1ef0c58);
                Object__DestroyImmediate(v17, 0);
            }
            else
            {
                v18 = sub_f7db74(0);
                v13 = sub_f7db74(v18);
                break;
            }
        }
    }
    while (true)
    {
        v19 = sub_f7db74(v13);
        if ((int)v12 != 1)
        {
            ptr = v19;
            sub_1329264(&flag, *(p));
            goto LABEL_10e5364;
        }
        ptr5 = __cxa_begin_catch();
        v21 = *(ptr5);
        __cxa_end_catch(ptr5);
        v12 = *(p);
        sub_1329264(&flag, v12);
        if (*(ptr5))
            break;
LABEL_10e5284:
        v13 = ptr->field_40;
        if (v13)
        {
            v25 = sub_12b135c(v13, *(ptr4));
            return sub_12b135c(v13, *(ptr4));
        }
    }
    v22 = sub_f1bd40(v21);
    ptr = v22;
    sub_1329264(&flag, *(p));
    if (true)
    {
LABEL_10e5364:
        sub_1026098(ptr);
        sub_e29990(sub_f1bd40(0));
    }
    sub_e29990(sub_f1bd40(0));
}
```

## `Water.Update` — RVA `0xce5378`

- Decompiled symbol: `Water_Update`
- Metadata signature: `private void Update() { }`
- Native interval: `664` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[224];
    unsigned int field_e0;
} struct_1;

extern struct_1 *g_1ef0c58;
extern long long g_1efd070;
extern char g_1fab651;

long long Water_Update(long long a0)
{
    long long v0;  // x0
    long long v1;  // x0
    long long v2;  // x19
    long long v3;  // x0
    unsigned long long v4;  // x0

    if (!(g_1fab651 & 1))
    {
        sub_f7d92c(&g_1efd070);
        sub_f7d92c("_F");
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c("[&");
        sub_f7d92c("7*");
        sub_f7d92c("9*");
        sub_f7d92c("5*");
        g_1fab651 = 1;
    }
    v0 = sub_1231bc8(a0, g_1efd070);
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v1 = Object__op_Implicit(v0, 0);
    if (!((char)v1 & 1))
        return v1;
    if (sub_1231bc8(a0, g_1efd070))
    {
        v2 = Renderer__get_sharedMaterial();
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        v3 = Object__op_Implicit(v2, 0);
        if (!((char)v3 & 1))
        {
            return v3;
        }
        else if (v2)
        {
            Material__GetVector(v2, g_1f0fb58, 0);
            Material__GetFloat(v2, g_1f10ac8, 0);
            Time__get_timeSinceLevelLoad(0);
            if (!g_1ef07e8->field_e0)
                sub_f7da5c(g_1ef07e8);
            Math__IEEERemainder(0);
            Math__IEEERemainder(0);
            Math__IEEERemainder(0);
            Math__IEEERemainder(0);
            Material__SetVector(v2, g_1f10ac0, 0);
            v4 = Material__SetVector();
            return Material__SetVector();
        }
    }
    sub_f7db74();
}
```

## `Water.ctor` — RVA `0xce5610`

- Decompiled symbol: `Water_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `240` bytes
- Result: `pseudocode`
- Heuristic layout hint: `Water_Recovered` matched 8 offsets against `Water` metadata (confidence 1.00).

```c
typedef struct Water_Recovered {
    char padding_0[32];
    unsigned int waterMode;
    char disablePixelLights;
    char padding_25[3];
    unsigned long long textureSize;
    unsigned int reflectLayers;
    unsigned int refractLayers;
    long long m_ReflectionCameras;
    long long m_RefractionCameras;
    char padding_48[16];
    unsigned int m_HardwareWaterSupport;
} Water_Recovered;

extern long long g_1eec4b8;
extern long long g_1ef5240;
extern char g_1fab655;

void Water_ctor(struct_0 *ptr)
{
    unsigned long long v6;  // x30
    unsigned long long v7;  // x23
    unsigned long long v8;  // x22
    unsigned long long v9;  // x21
    unsigned long long v10;  // x20
    unsigned long long v11;  // x19
    long long v12;  // x20
    struct_0 *p;  // x0
    long long v14;  // x20
    struct_0 *addr;  // x0
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
    if (!(g_1fab655 & 1))
    {
        sub_f7d92c(&g_1ef5240);
        sub_f7d92c(&g_1eec4b8);
        g_1fab655 = 1;
    }
    ptr->field_20 = 2;
    ptr->field_24 = 1;
    ptr->field_28 = 0x3d8f5c2900000100;
    ptr->field_30 = LayerMask__op_Implicit(4294967295, 0);
    ptr->field_34 = LayerMask__op_Implicit(4294967295, 0);
    v12 = sub_f7db70(g_1eec4b8);
    sub_12b0eec(v12, g_1ef5240);
    p = ptr;
    p->field_38 = v12;
    sub_f7d8d0((struct Water_Recovered *)&p->field_38, v12);
    v14 = sub_f7db70(g_1eec4b8);
    sub_12b0eec(v14, g_1ef5240);
    addr = ptr;
    addr->field_40 = v14;
    sub_f7d8d0((struct Water_Recovered *)&addr->field_40, v14);
    ptr->field_58 = 2;
    MonoBehaviour__ctor();
    return;
}
```
