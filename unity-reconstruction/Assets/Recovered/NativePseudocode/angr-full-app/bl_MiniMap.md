# Native pseudocode: bl_MiniMap

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `bl_MiniMap.Awake` — RVA `0xcc641c`

- Decompiled symbol: `bl_MiniMap_Awake`
- Metadata signature: `private void Awake() { }`
- Native interval: `300` bytes
- Result: `pseudocode`
- Heuristic layout hint: `bl_MiniMap_Recovered` matched 12 offsets against `bl_MiniMap` metadata (confidence 0.86).

```c
typedef struct bl_MiniMap_Recovered {
    char padding_0[56];
    long long MMCamera;
    unsigned int m_Type;
    unsigned int m_Mode;
    unsigned int m_MapType;
    char padding_4c[8];
    unsigned int DefaultHeight;
    char padding_58[20];
    char useCompassRotation;
    char padding_6d[8];
    char DynamicRotation;
    char padding_76[258];
    long long MMUIRoot;
    long long PlayerIcon;
    char padding_188[36];
    char DefaultRotationMode;
    char padding_1ad[3];
    unsigned int DeafultMapRot;
    unsigned int field_1b4;
    unsigned int field_1b8;
    char DefaultRotationCircle;
} bl_MiniMap_Recovered;

typedef struct struct_1 {
    char padding_0[8];
    long long field_8;
    long long field_10;
} struct_1;

typedef struct struct_0 {
    char padding_0[184];
    struct struct_1 *field_b8;
} struct_0;

extern struct_0 *g_1ef2b00;
extern long long g_1f0c248;
extern char g_1fab54a;

long long bl_MiniMap_Awake(struct_2 *ptr)
{
    long long v0;  // x1
    long long p[3];  // x0
    long long v10;  // x0
    long long v2;  // x1
    long long addr[3];  // x0
    unsigned int flag;  // w8
    char v5;  // x9
    unsigned int v6;  // s0
    unsigned int v7;  // s1
    unsigned int v8;  // s2
    long long v9;  // x0

    if (!(g_1fab54a & 1))
    {
        sub_f7d92c(&g_1f0c248);
        sub_f7d92c(&g_1ef2b00);
        g_1fab54a = 1;
    }
    bl_MiniMap__GetMiniMapSize(ptr);
    v0 = ptr->field_38;
    p = g_1ef2b00->field_b8;
    p[1] = v0;
    sub_f7d8d0((long long [3])&p[1], v0);
    v2 = ptr->field_178;
    addr = g_1ef2b00->field_b8;
    addr[2] = v2;
    sub_f7d8d0((long long [3])&addr[2], v2);
    ptr->field_1ac = ptr->field_75;
    if (bl_MiniMap__get_m_Transform(ptr))
    {
        Transform__get_eulerAngles();
        flag = ptr->field_40;
        v5 = ptr->field_6c;
        ptr->field_1b0 = v6;
        ptr->field_1b4 = v7;
        ptr->field_1b8 = v8;
        ptr->field_1bc = v5;
        if (flag == 1)
            bl_MiniMap__CreateMapPlane(ptr);
        if (ptr->field_44 == 1)
            bl_MiniMap__ConfigureCamera3D(ptr);
        if (!ptr->field_48)
        {
            v10 = PlayerPrefs__GetFloat(g_1f0c248, 0);
            ptr->field_54 = ptr->field_54;
            return v10;
        }
        bl_MiniMap__ConfigureWorlTarget(ptr);
        if (ptr->field_180 && Component__get_gameObject(ptr->field_180, 0))
        {
            v9 = GameObject__SetActive();
            return GameObject__SetActive();
        }
    }
    sub_f7db74();
}
```

## `bl_MiniMap.GetMiniMapSize` — RVA `0xcc6548`

- Decompiled symbol: `bl_MiniMap_GetMiniMapSize`
- Metadata signature: `private void GetMiniMapSize() { }`
- Native interval: `88` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[192];
    unsigned int field_c0;
    unsigned int field_c4;
    unsigned int field_c8;
    unsigned int field_cc;
    unsigned int field_d0;
    unsigned int field_d4;
    unsigned int field_d8;
    unsigned int field_dc;
    char padding_e0[152];
    unsigned long long field_178;
} struct_0;

unsigned long long bl_MiniMap_GetMiniMapSize(struct_0 *ptr)
{
    unsigned long long v0;  // x0
    unsigned int v1;  // s0
    unsigned int v2;  // s1
    unsigned long long v3;  // x0
    unsigned int v4;  // s2

    v0 = ptr->field_178;
    if (v0)
    {
        RectTransform__get_sizeDelta(v0, 0);
        v0 = ptr->field_178;
        ptr->field_d8 = v1;
        ptr->field_dc = v2;
        if (v0)
        {
            RectTransform__get_anchoredPosition(v0, 0);
            v0 = ptr->field_178;
            ptr->field_c0 = v1;
            ptr->field_c4 = v2;
            ptr->field_c8 = 0;
            if (v0)
            {
                v3 = Transform__get_eulerAngles(v0, 0);
                ptr->field_cc = v1;
                ptr->field_d0 = v2;
                ptr->field_d4 = v4;
                return v3;
            }
        }
    }
    sub_f7db74(v0);
}
```

## `bl_MiniMap.get_m_Transform` — RVA `0xcc65a0`

- Decompiled symbol: `bl_MiniMap_get_m_Transform`
- Metadata signature: `private Transform get_m_Transform() { }`
- Native interval: `160` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[464];
    long long field_1d0;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern long long g_1efd0c8;
extern char g_1fab55e;

long long bl_MiniMap_get_m_Transform(struct_1 *ptr)
{
    long long v0;  // x0

    if (!(g_1fab55e & 1))
    {
        sub_f7d92c(&g_1efd0c8);
        sub_f7d92c(&g_1ef0c58);
        g_1fab55e = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (((char)Object__op_Equality(ptr->field_1d0, 0, 0) & 1))
    {
        v0 = sub_1231bc8(ptr, g_1efd0c8);
        ptr->field_1d0 = v0;
        sub_f7d8d0((struct struct_1 *)&ptr->field_1d0, v0);
    }
    return ptr->field_1d0;
}
```

## `bl_MiniMap.CreateMapPlane` — RVA `0xcc6640`

- Decompiled symbol: `bl_MiniMap_CreateMapPlane`
- Metadata signature: `private void CreateMapPlane() { }`
- Native interval: `752` bytes
- Result: `pseudocode`
- Heuristic layout hint: `bl_MiniMap_Recovered` matched 7 offsets against `bl_MiniMap` metadata (confidence 1.00).

```c
typedef struct bl_MiniMap_Recovered {
    char padding_0[48];
    unsigned int MiniMapLayer;
    char padding_34[4];
    long long MMCamera;
    char padding_40[216];
    long long MapTexture;
    char padding_120[64];
    long long MapPlane;
    long long WorldSpace;
    char padding_170[8];
    long long MMUIRoot;
    char padding_180[64];
    long long plane;
} bl_MiniMap_Recovered;

typedef struct struct_1 {
    char padding_0[224];
    unsigned int field_e0;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1eef458;
extern struct_1 *g_1ef0c58;
extern long long g_1efeca0;
extern long long g_1f00238;
extern long long g_1f09a00;
extern long long g_1f0bfe0;
extern long long g_1f0c240;
extern char g_1fab54b;

void bl_MiniMap_CreateMapPlane(struct_2 *ptr)
{
    unsigned long long v10;  // d12
    unsigned long long v11;  // d11
    long long v20;  // x0
    long long v21;  // x0
    struct_2 *p;  // x20
    long long v23;  // x21
    unsigned long long v12;  // d10
    unsigned long long v13;  // d9
    unsigned long long v14;  // d8
    unsigned long long v15;  // x30
    unsigned long long v16;  // x22
    unsigned long long v17;  // x21
    unsigned long long v18;  // x20
    unsigned long long v19;  // x19
    unsigned long long v0;  // [bp-0x50]
    unsigned long long v1;  // [bp-0x48]
    unsigned long long v2;  // [bp-0x40]
    unsigned long long v3;  // [bp-0x38]
    unsigned long long v4;  // [bp-0x30]
    unsigned long long v5;  // [bp-0x28]
    unsigned long long v6;  // [bp-0x20]
    unsigned long long v7;  // [bp-0x18]
    unsigned long long v8;  // [bp-0x10]
    unsigned long long v9;  // [bp-0x8]

    v0 = v10;
    v1 = v11;
    v2 = v12;
    v3 = v13;
    v4 = v14;
    v5 = v15;
    v6 = v16;
    v7 = v17;
    v8 = v18;
    v9 = v19;
    if (!(g_1fab54b & 1))
    {
        sub_f7d92c(&g_1eef458);
        sub_f7d92c(&g_1efeca0);
        sub_f7d92c(&g_1f00238);
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c(&g_1f0c240);
        sub_f7d92c(&g_1f0bfe0);
        sub_f7d92c(&g_1f09a00);
        g_1fab54b = 1;
    }
    if (((char)String__IsNullOrEmpty(LayerMask__LayerToName(ptr->field_30, 0), 0) & 1))
    {
        if (!g_1eef458->field_e0)
            sub_f7da5c(g_1eef458);
        Debug__LogError(g_1f0c240, 0);
        v20 = ptr->field_178;
        if (!v20 || !((v20 = Component__get_gameObject(v20, 0), v20)))
            goto LABEL_10c692c;
        GameObject__SetActive();
        Behaviour__set_enabled(ptr, 0, 0);
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (((char)Object__op_Equality(ptr->field_118, 0, 0) & 1))
    {
        if (!g_1eef458->field_e0)
            sub_f7da5c(g_1eef458);
        Debug__LogError();
        return;
    }
    else
    {
        v20 = ptr->field_168;
        if (v20)
        {
            Transform__get_localPosition(v20, 0);
            v20 = ptr->field_168;
            if (v20)
            {
                RectTransform__get_sizeDelta(v20, 0);
                v20 = ptr->field_38;
                if (v20)
                {
                    Camera__set_cullingMask(v20, 1 << ((char)ptr->field_30 & 31), 0);
                    if (!g_1ef0c58->field_e0)
                        sub_f7da5c(g_1ef0c58);
                    v21 = sub_1129f50(ptr->field_160, g_1f00238);
                    p = &ptr->field_1c0;
                    ptr->field_1c0 = v21;
                    sub_f7d8d0(p, v21);
                    v20 = ptr->field_1c0;
                    if (v20)
                    {
                        v20 = GameObject__get_transform(v20, 0);
                        if (v20)
                        {
                            Transform__set_localPosition();
                            v20 = *((long long *)&p->padding_0[0]);
                            if (v20)
                            {
                                v20 = GameObject__get_transform(v20, 0);
                                if (v20)
                                {
                                    Transform__set_localScale();
                                    v20 = *((long long *)&p->padding_0[0]);
                                    if (v20)
                                    {
                                        v23 = sub_1249224(v20, g_1efeca0);
                                        v20 = bl_MiniMap__CreateMaterial(ptr);
                                        if (v23)
                                        {
                                            Renderer__set_material(v23, v20, 0);
                                            v20 = *((long long *)&p->padding_0[0]);
                                            if (v20)
                                            {
                                                GameObject__set_layer(v20, ptr->field_30, 0);
                                                v20 = ptr->field_1c0;
                                                if (v20)
                                                {
                                                    GameObject__SetActive(v20, 0, 0);
                                                    v20 = *((long long *)&p->padding_0[0]);
                                                    if (v20)
                                                        GameObject__SetActive(v20, 1, 0);
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
LABEL_10c692c:
    sub_f7db74(v20);
}
```

## `bl_MiniMap.ConfigureCamera3D` — RVA `0xcc6930`

- Decompiled symbol: `bl_MiniMap_ConfigureCamera3D`
- Metadata signature: `public void ConfigureCamera3D() { }`
- Native interval: `320` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    char padding_0[368];
    unsigned long long field_170;
} struct_2;

typedef struct struct_1 {
    char padding_0[224];
    unsigned int field_e0;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1eef458;
extern struct_1 *g_1ef0c58;
extern long long g_1f0c840;
extern char g_1fab54c;

void bl_MiniMap_ConfigureCamera3D(struct_2 *ptr)
{
    unsigned long long v4;  // x30
    unsigned long long v5;  // x21
    unsigned long long v6;  // x20
    unsigned long long v7;  // x19
    long long v8;  // x0
    long long v9;  // x0
    long long v10;  // x20
    unsigned long long v11;  // x0
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x18]
    unsigned long long v2;  // [bp-0x10]
    unsigned long long v3;  // [bp-0x8]

    v0 = v4;
    v1 = v5;
    v2 = v6;
    v3 = v7;
    if (!(g_1fab54c & 1))
    {
        sub_f7d92c(&g_1eef458);
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c(&g_1f0c840);
        g_1fab54c = 1;
    }
    v8 = Camera__get_main(0);
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (((char)Object__op_Inequality(v8, 0, 0) & 1))
        v9 = Camera__get_main(0);
    else
        v9 = Camera__get_current(0);
    v10 = v9;
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (((char)Object__op_Equality(v10, 0, 0) & 1))
    {
        if (!g_1eef458->field_e0)
            sub_f7da5c(g_1eef458);
        Debug__LogWarning();
        return;
    }
    v11 = ptr->field_170;
    if (v11)
    {
        v11 = Canvas__set_worldCamera(v11, v10, 0);
        if (v10)
        {
            Camera__set_nearClipPlane(v10, 0);
            v11 = ptr->field_170;
        }
    }
    sub_f7db74(v11);
}
```

## `bl_MiniMap.ConfigureWorlTarget` — RVA `0xcc6a70`

- Decompiled symbol: `bl_MiniMap_ConfigureWorlTarget`
- Metadata signature: `public void ConfigureWorlTarget() { }`
- Native interval: `260` bytes
- Result: `pseudocode`
- Heuristic layout hint: `bl_MiniMap_Recovered` matched 3 offsets against `bl_MiniMap` metadata (confidence 1.00).

```c
typedef struct bl_MiniMap_Recovered {
    char padding_0[32];
    struct struct_3 *m_Target;
    char padding_28[344];
    struct struct_3 *PlayerIcon;
    char padding_188[8];
    long long ItemPrefab;
} bl_MiniMap_Recovered;

typedef struct struct_3 {
    struct struct_1 *field_0;
    char padding_8[24];
    unsigned long long field_20;
    char padding_28[24];
    unsigned long long field_40;
    char padding_48[144];
    unsigned long long field_d8;
} struct_3;

typedef struct struct_7 {
    struct struct_5 *field_0;
    char padding_8[24];
    long long field_20;
    char padding_28[24];
    long long field_40;
    char padding_48[144];
    unsigned long long field_d8;
} struct_7;

typedef struct struct_1 {
    char padding_0[664];
    struct struct_2 *field_298;
    unsigned long long field_2a0;
} struct_1;

typedef struct struct_5 {
    char padding_0[664];
    struct struct_6 *field_298;
    unsigned long long field_2a0;
} struct_5;

typedef struct struct_2 {
    unsigned long long field_0;
} struct_2;

typedef struct struct_6 {
    unsigned long long field_0;
} struct_6;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern long long g_1efeb00;
extern char g_1fab54d;

long long bl_MiniMap_ConfigureWorlTarget(struct_4 *ptr)
{
    unsigned long long flag;  // x2
    long long v1;  // x0
    struct_3 *v2;  // x0
    struct_7 *addr;  // x0
    long long v4;  // x1
    unsigned long v6;  // x1
    struct_7 *p;  // x0
    unsigned long long v8;  // x1

    if (!(g_1fab54d & 1))
    {
        sub_f7d92c(&g_1efeb00);
        sub_f7d92c(&g_1ef0c58);
        g_1fab54d = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    flag = 0;
    v1 = Object__op_Equality(ptr->field_20, 0, 0);
    if (((char)v1 & 1))
        return v1;
    v2 = ptr->field_20;
    if (v2)
    {
        addr = sub_124913c(v2, g_1efeb00);
        v2 = addr;
        if (v2)
        {
            v4 = ptr->field_190;
            addr->field_20 = v4;
            v2 = sub_f7d8d0((struct struct_7 *)&addr->field_20, v4);
            if (ptr->field_180)
            {
                v6 = ptr->field_180->field_d8;
                p = addr;
                p->field_40 = v6;
                sub_f7d8d0((struct struct_7 *)&p->field_40, v6);
                v2 = ptr->field_180;
                if (v2)
                {
                    v8 = v2->field_0->field_2a0;
                    v2->field_0->field_298();
                }
            }
        }
    }
    sub_f7db74(v2);
}
```

## `bl_MiniMap.CreateMaterial` — RVA `0xcc6b74`

- Decompiled symbol: `bl_MiniMap_CreateMaterial`
- Metadata signature: `public Material CreateMaterial() { }`
- Native interval: `356` bytes
- Result: `pseudocode`

```c
extern long long g_1f103f8;
extern long long g_1f10400;
extern long long g_1f10408;
extern long long g_1f10410;
extern long long g_1f10898;
extern char g_1fab557;

long long bl_MiniMap_CreateMaterial(long long *a0)
{
    long long v0;  // x20

    if (!(g_1fab557 & 1))
    {
        sub_f7d92c("7F");
        sub_f7d92c(&g_1f10898);
        sub_f7d92c(&g_1f10410);
        sub_f7d92c(&g_1f103f8);
        sub_f7d92c(&g_1f10408);
        sub_f7d92c(&g_1f10400);
        g_1fab557 = 1;
    }
    v0 = sub_f7db70(g_1ef07c0);
    Material__ctor(v0, a0[43], 0);
    if (v0)
    {
        Material__set_mainTexture(v0, a0[35], 0);
        Material__SetTexture(v0, g_1f10408, a0[35], 0);
        Material__SetFloat(v0, g_1f10410, 0);
        Material__SetColor(v0, g_1f10400, 0);
        Material__SetColor(v0, g_1f10898, 0);
        Material__EnableKeyword(v0, g_1f103f8, 0);
        return v0;
    }
    sub_f7db74();
}
```

## `bl_MiniMap.DelayPositionInvoke` — RVA `0xcc6cd8`

- Decompiled symbol: `bl_MiniMap_DelayPositionInvoke`
- Metadata signature: `private void DelayPositionInvoke() { }`
- Native interval: `60` bytes
- Result: `pseudocode`
- Heuristic layout hint: `bl_MiniMap_Recovered` matched 3 offsets against `bl_MiniMap` metadata (confidence 1.00).

```c
typedef struct bl_MiniMap_Recovered {
    char padding_0[56];
    long long MMCamera;
    char padding_40[392];
    unsigned int defaultYCameraPosition;
    char getDelayPositionCamera;
} bl_MiniMap_Recovered;

void bl_MiniMap_DelayPositionInvoke(struct_0 *ptr)
{
    long long v0;  // x0
    unsigned int v1;  // s1

    v0 = ptr->field_38;
    if (v0)
    {
        v0 = Component__get_transform(v0, 0);
        if (v0)
        {
            Transform__get_position();
            ptr->field_1c8 = v1;
            ptr->field_1cc = 1;
            return;
        }
    }
    sub_f7db74(v0);
}
```

## `bl_MiniMap.Update` — RVA `0xcc6d14`

- Decompiled symbol: `bl_MiniMap_Update`
- Metadata signature: `private void Update() { }`
- Native interval: `184` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab54e;

long long bl_MiniMap_Update(long long *a0)
{
    long long v0;  // x0
    long long v1;  // x0
    unsigned long long v2;  // x0

    if (!(g_1fab54e & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab54e = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v0 = Object__op_Equality(a0[4], 0, 0);
    if (((char)v0 & 1))
        return v0;
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v1 = Object__op_Equality(a0[7], 0, 0);
    if (!((char)v1 & 1))
    {
        bl_MiniMap__Inputs(a0);
        bl_MiniMap__PositionControll(a0);
        bl_MiniMap__RotationControll(a0);
        v2 = bl_MiniMap__MapSize(a0);
        return bl_MiniMap__MapSize(a0);
    }
    return v1;
}
```

## `bl_MiniMap.Inputs` — RVA `0xcc6dcc`

- Decompiled symbol: `bl_MiniMap_Inputs`
- Metadata signature: `private void Inputs() { }`
- Native interval: `128` bytes
- Result: `pseudocode`

```c
unsigned long long bl_MiniMap_Inputs(unsigned int *ptr)
{
    unsigned int v0;  // s0
    unsigned int v1;  // s1
    unsigned long v2;  // 4133
    unsigned long long v3;  // x0
    unsigned int v4;  // s0
    unsigned int v5;  // s1
    unsigned long v6;  // 4133
    unsigned long long v7;  // x0

    if (((char)Input__GetKeyDown(ptr[13], 0) & 1))
        bl_MiniMap__ToggleSize(ptr);
    if (((char)Input__GetKeyDown(ptr[25], 0) & 1))
    {
        v0 = ptr[21];
        v1 = ptr[22];
        v2 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v0, v1)) >> 5 & 3 | (unsigned long long)(CmpF(v0, v1) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v0, v1)) >> 5 & 3 | (unsigned long long)(CmpF(v0, v1) & 1)) & ((unsigned long long)(char)(CmpF(v0, v1)) >> 5 & 3 | (unsigned long long)(CmpF(v0, v1) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if (!((char)v2))
            bl_MiniMap__ChangeHeight(ptr, 1);
    }
    v3 = Input__GetKeyDown(ptr[24], 0);
    if (!((char)v3 & 1))
        return v3;
    v4 = ptr[21];
    v5 = ptr[23];
    v6 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v4, v5)) >> 5 & 3 | (unsigned long long)(CmpF(v4, v5) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v4, v5)) >> 5 & 3 | (unsigned long long)(CmpF(v4, v5) & 1)) & ((unsigned long long)(char)(CmpF(v4, v5)) >> 5 & 3 | (unsigned long long)(CmpF(v4, v5) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if ((char)v6)
        return v3;
    v7 = bl_MiniMap__ChangeHeight();
    return bl_MiniMap__ChangeHeight();
}
```

## `bl_MiniMap.PositionControll` — RVA `0xcc6e4c`

- Decompiled symbol: `bl_MiniMap_PositionControll`
- Metadata signature: `private void PositionControll() { }`
- Native interval: `784` bytes
- Result: `pseudocode`
- Heuristic layout hint: `bl_MiniMap_Recovered` matched 7 offsets against `bl_MiniMap` metadata (confidence 0.88).

```c
typedef struct bl_MiniMap_Recovered {
    char padding_0[56];
    long long MMCamera;
    char padding_40[8];
    unsigned int m_MapType;
    char padding_4c[12];
    unsigned int maxHeight;
    char padding_5c[268];
    long long WorldSpace;
    char padding_170[16];
    long long PlayerIcon;
    char padding_188[32];
    unsigned int field_1a8;
    char padding_1ac[20];
    long long plane;
    char padding_1c8[4];
    char getDelayPositionCamera;
} bl_MiniMap_Recovered;

typedef struct struct_1 {
    char padding_0[16];
    long long field_10;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

typedef struct struct_2 {
    char padding_0[184];
    struct struct_1 *field_b8;
} struct_2;

extern struct_0 *g_1ef0c58;
extern struct_2 *g_1ef2b00;
extern char g_1fab54f;

long long bl_MiniMap_PositionControll(struct_3 *ptr)
{
    long long v2;  // x0
    long long v3;  // x20
    unsigned int v4;  // s0
    long long v5;  // x20
    unsigned long v6;  // 4146
    long long v7;  // x0
    long long v8;  // x0
    unsigned int v0;  // [bp-0x68]
    unsigned int v1;  // [bp-0x64]

    if (!(g_1fab54f & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c(&g_1ef2b00);
        g_1fab54f = 1;
    }
    if (ptr->field_48)
    {
LABEL_10c7064:
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        v7 = Object__op_Inequality(ptr->field_1c0, 0, 0);
        if (!((char)v7 & 1))
            return v7;
        if (ptr->field_1cc)
        {
            if (ptr->field_1c0 && GameObject__get_transform(ptr->field_1c0, 0))
            {
                Transform__get_position();
                if (ptr->field_168)
                {
                    Transform__get_position(ptr->field_168, 0);
                    if (ptr->field_38 && Component__get_transform(ptr->field_38, 0))
                    {
                        Transform__get_position();
                        if (ptr->field_1c0 && GameObject__get_transform(ptr->field_1c0, 0))
                        {
                            v8 = Transform__set_position();
                            return Transform__set_position();
                        }
                    }
                }
            }
        }
        else
        {
            return v7;
        }
    }
    else if (bl_MiniMap__get_m_Transform(ptr) && (Transform__get_position(), (unsigned long long)bl_MiniMap__get_Target(ptr) && (Transform__get_position(), (unsigned long long)bl_MiniMap__get_Target(ptr))))
    {
        Transform__get_position();
        v2 = bl_MiniMap__get_Target(ptr);
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        if (((char)Object__op_Inequality(v2, 0, 0) & 1))
        {
            bl_MiniMap__get_TargetPosition(ptr);
            if (ptr->field_38 && (Camera__WorldToViewportPoint(ptr->field_38, 0), ptr->field_180))
            {
                v3 = Graphic__get_rectTransform(ptr->field_180, 0);
                bl_MiniMapUtils__CalculateMiniMapPosition(g_1ef2b00->field_b8->field_10);
                if (v3)
                {
                    RectTransform__set_anchoredPosition(v3, 0);
                    goto LABEL_10c6f9c;
                }
            }
        }
        else
        {
LABEL_10c6f9c:
            v1 = ptr->field_1a8;
            if (bl_MiniMap__get_Target(ptr))
            {
                v0 = ptr->field_58;
                Transform__get_position();
                v5 = bl_MiniMap__get_m_Transform(ptr);
                if (bl_MiniMap__get_m_Transform(ptr))
                {
                    Transform__get_position();
                    Time__get_deltaTime(0);
                    v6 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v4 * 0x41200000, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v4 * 0x41200000, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v4 * 0x41200000, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v4 * 0x41200000, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v4 * 0x41200000, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v4 * 0x41200000, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                    if (v5)
                    {
                        Transform__set_position(v5, 0);
                        goto LABEL_10c7064;
                    }
                }
            }
        }
    }
    sub_f7db74();
}
```

## `bl_MiniMap.RotationControll` — RVA `0xcc715c`

- Decompiled symbol: `bl_MiniMap_RotationControll`
- Metadata signature: `private void RotationControll() { }`
- Native interval: `820` bytes
- Result: `pseudocode`
- Heuristic layout hint: `bl_MiniMap_Recovered` matched 6 offsets against `bl_MiniMap` metadata (confidence 1.00).

```c
typedef struct bl_MiniMap_Recovered {
    char padding_0[68];
    unsigned int m_Mode;
    unsigned int m_MapType;
    char padding_4c[41];
    char DynamicRotation;
    char SmoothRotation;
    char padding_77[1];
    unsigned int LerpRotation;
    char padding_7c[260];
    long long PlayerIcon;
} bl_MiniMap_Recovered;

extern long long g_1ef22e8;
extern long long g_1efd060;
extern char g_1fab2c9;
extern char g_1fab2cb;
extern char g_1fab550;

void bl_MiniMap_RotationControll(struct_0 *ptr)
{
    unsigned long long v11;  // d13
    unsigned long long v12;  // d12
    unsigned long long v21;  // x19
    long long v22;  // x0
    long long v23;  // x20
    unsigned int v24;  // w21
    long long v25;  // x0
    unsigned int v26;  // s0
    unsigned int v27;  // s1
    unsigned int v28;  // s1
    unsigned int v29;  // 4098
    unsigned long v30;  // 4111
    unsigned long long v13;  // d11
    unsigned int v31;  // s0
    unsigned int v32;  // s0
    unsigned long v33;  // 4141
    unsigned long v34;  // 4128
    unsigned int v35;  // s0
    long long v36;  // x0
    unsigned int v37;  // s0
    unsigned long v38;  // 4150
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
    if (!(g_1fab550 & 1))
    {
        sub_f7d92c(&g_1efd060);
        g_1fab550 = 1;
    }
    v22 = ptr->field_180;
    if (v22)
    {
        v23 = sub_1231bc8(v22, g_1efd060);
        if (!ptr->field_75 || ptr->field_48 == 1)
        {
            v22 = bl_MiniMap__get_m_Transform(ptr);
            if (v22)
            {
                Transform__set_eulerAngles();
                if (ptr->field_44)
                {
                    v22 = bl_MiniMap__get_Target(ptr);
                    if (v22)
                    {
                        v22 = Transform__get_localEulerAngles();
                        if (!g_1fab2c9)
                        {
                            v22 = sub_f7d92c(&g_1ef22e8);
                            g_1fab2c9 = 1;
                        }
                        if (v23)
                        {
                            Transform__set_localEulerAngles();
                            return;
                        }
                    }
                }
                else
                {
                    if (!g_1fab2c9)
                    {
                        sub_f7d92c(&g_1ef22e8);
                        g_1fab2c9 = 1;
                    }
                    v22 = bl_MiniMap__get_Target(ptr);
                    if (v22 && (v22 = (long long)(unsigned long long)Transform__get_eulerAngles(), v23))
                        goto LABEL_10c746c;
                }
            }
        }
        else
        {
            v22 = bl_MiniMap__get_m_Transform(ptr);
            if (v22)
            {
                Transform__get_eulerAngles();
                v22 = bl_MiniMap__get_Target(ptr);
                if (v22)
                {
                    v22 = Transform__get_eulerAngles();
                    if (ptr->field_76)
                    {
                        v24 = ptr->field_44;
                        if (!g_1fab2cb)
                        {
                            v22 = sub_f7d92c("-M");
                            g_1fab2cb = 1;
                        }
                        if (v23)
                        {
                            v25 = v23;
                            v26 = g_1ef1058->field_b8->field_0;
                            v27 = g_1ef1058->field_b8->field_4;
                            if (v24)
                                Transform__set_localRotation(v25, 0);
                            else
                                Transform__set_rotation(v25, 0);
                            v22 = bl_MiniMap__get_m_Transform(ptr);
                            if (v22)
                            {
                                Transform__get_eulerAngles();
                                v29 = CmpF(v27, v28);
                                v30 = (((CmpF(v27, v28) >> 5 & 3 | CmpF(v27, v28) & 1) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1;
                                v31 = v26;
                                if (!((char)((v30 - ((CmpF(v27, v28) >> 5 & 3 | CmpF(v27, v28) & 1) & (v29 >> 5 & 3 | CmpF(v27, v28) & 1) >> 1 & 1)) * 0x10000000 >> 30)))
                                {
                                    v22 = bl_MiniMap__get_m_Transform(ptr);
                                    if (v22)
                                    {
                                        Transform__get_eulerAngles();
                                        v32 = v28 - v27;
                                        v33 = arm64g_calculate_condition(192, (((((unsigned long long)(char)(CmpF(v32, 0x43340000)) >> 5 & 3 | (unsigned long long)(CmpF(v32, 0x43340000) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v32, 0x43340000)) >> 5 & 3 | (unsigned long long)(CmpF(v32, 0x43340000) & 1)) & ((unsigned long long)(char)(CmpF(v32, 0x43340000)) >> 5 & 3 | (unsigned long long)(CmpF(v32, 0x43340000) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                                        if (!((char)v33) && (v34 = (unsigned long)arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v32, 0xc3340000)) >> 5 & 3 | (unsigned long long)(CmpF(v32, 0xc3340000) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v32, 0xc3340000)) >> 5 & 3 | (unsigned long long)(CmpF(v32, 0xc3340000) & 1)) & ((unsigned long long)(char)(CmpF(v32, 0xc3340000)) >> 5 & 3 | (unsigned long long)(CmpF(v32, 0xc3340000) & 1)) >> 1 & 1)) * 0x10000000, 0, 0), v31 = v32, (char)v34))
                                            goto LABEL_10c73ec;
                                        v22 = bl_MiniMap__get_m_Transform(ptr);
                                        if (v22)
                                        {
                                            Transform__set_eulerAngles();
                                            v31 = v35;
                                            goto LABEL_10c73ec;
                                        }
                                    }
                                }
                                else
                                {
LABEL_10c73ec:
                                    v36 = bl_MiniMap__get_m_Transform(ptr);
                                    v22 = Component__get_transform(ptr, 0);
                                    if (v22)
                                    {
                                        Transform__get_eulerAngles();
                                        v22 = Time__get_deltaTime(0);
                                        v37 = v31 * ptr->field_78;
                                        v38 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v37, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v37, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v37, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v37, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v37, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v37, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                                        if (v36)
                                        {
LABEL_10c746c:
                                            Transform__set_eulerAngles();
                                            return;
                                        }
                                    }
                                }
                            }
                        }
                    }
                    else
                    {
                        v22 = bl_MiniMap__get_m_Transform(ptr);
                        if (v22)
                            goto LABEL_10c746c;
                    }
                }
            }
        }
    }
    sub_f7db74(v22);
}
```

## `bl_MiniMap.MapSize` — RVA `0xcc7490`

- Decompiled symbol: `bl_MiniMap_MapSize`
- Metadata signature: `private void MapSize() { }`
- Native interval: `748` bytes
- Result: `pseudocode`
- Heuristic layout hint: `bl_MiniMap_Recovered` matched 10 offsets against `bl_MiniMap` metadata (confidence 0.71).

```c
typedef struct bl_MiniMap_Recovered {
    char padding_0[56];
    long long MMCamera;
    char padding_40[40];
    unsigned int LerpHeight;
    char padding_6c[9];
    char DynamicRotation;
    char padding_76[42];
    unsigned int FullMapPosition;
    unsigned int field_a4;
    char padding_a8[16];
    unsigned int FullMapSize;
    unsigned int field_bc;
    unsigned int MiniMapPosition;
    unsigned int field_c4;
    char padding_c8[16];
    unsigned int MiniMapSize;
    unsigned int field_dc;
    unsigned int LerpTransition;
    char padding_e4[148];
    long long MMUIRoot;
    char padding_180[44];
    char DefaultRotationMode;
} bl_MiniMap_Recovered;

typedef struct struct_1 {
    char field_0;
} struct_1;

typedef struct struct_0 {
    char padding_0[184];
    struct struct_1 *field_b8;
} struct_0;

extern struct_0 *g_1ef2b00;
extern char g_1fab551;

void bl_MiniMap_MapSize(struct_2 *ptr)
{
    unsigned long long v12;  // d13
    unsigned long long v13;  // d12
    long long v22;  // x20
    unsigned int v23;  // w8
    unsigned int v24;  // s0
    unsigned int v25;  // s0
    unsigned int v26;  // s1
    unsigned long v27;  // 4176
    unsigned int v28;  // s0
    unsigned int v29;  // s0
    unsigned int v30;  // s1
    unsigned int v31;  // s9
    unsigned long long v14;  // d11
    unsigned int v32;  // s0
    unsigned int v33;  // s1
    unsigned long v34;  // 4180
    unsigned int v35;  // s0
    unsigned long v36;  // d0
    unsigned long v37;  // d1
    unsigned int v38;  // w9
    unsigned int v39;  // s0
    unsigned int v40;  // s1
    unsigned long long v15;  // d10
    unsigned long v41;  // 4176
    unsigned int v42;  // s0
    unsigned int v43;  // s0
    unsigned int v44;  // s9
    unsigned int v45;  // s0
    unsigned int v46;  // s1
    unsigned long v47;  // 4180
    unsigned int v48;  // s0
    unsigned long long v16;  // d9
    unsigned int v49;  // s0
    unsigned long v50;  // 4182
    unsigned int v51;  // s0
    unsigned int v52;  // s0
    unsigned long v53;  // 4154
    unsigned long long v17;  // d8
    unsigned long long v18;  // x30
    unsigned long long v19;  // x21
    unsigned long long v20;  // x20
    unsigned long long v21;  // x19
    unsigned long v0;  // [bp-0x70]
    unsigned long v1;  // [bp-0x60]
    unsigned long long v2;  // [bp-0x50]
    unsigned long long v3;  // [bp-0x48]
    unsigned long long v4;  // [bp-0x40]
    unsigned long long v5;  // [bp-0x38]
    unsigned long long v6;  // [bp-0x30]
    unsigned long long v7;  // [bp-0x28]
    unsigned long long v8;  // [bp-0x20]
    unsigned long long v9;  // [bp-0x18]
    unsigned long long v10;  // [bp-0x10]
    unsigned long long v11;  // [bp-0x8]

    v2 = v12;
    v3 = v13;
    v4 = v14;
    v5 = v15;
    v6 = v16;
    v7 = v17;
    v8 = v18;
    v9 = v19;
    v10 = v20;
    v11 = v21;
    if (!(g_1fab551 & 1))
    {
        sub_f7d92c(&g_1ef2b00);
        g_1fab551 = 1;
    }
    v22 = ptr->field_178;
    v23 = ptr->field_75;
    if (g_1ef2b00->field_b8->field_0)
    {
        if (v23)
        {
            ptr->field_75 = 0;
            bl_MiniMap__ResetMapRotation(ptr);
        }
        if (v22)
        {
            RectTransform__get_sizeDelta(v22, 0);
            Time__get_deltaTime(0);
            v25 = v24 * ptr->field_e0;
            v26 = [D] unsupported_Iop_ZeroHI96ofV128();
            v27 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v25, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v25, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v25, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v25, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v25, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v25, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
            if ((char)v27)
                v28 = v26;
            else
                v28 = 0;
            v29 = v24 + (ptr->field_b8 - v24) * v28;
            RectTransform__set_sizeDelta();
            RectTransform__get_anchoredPosition(v22, 0);
            v31 = v30 + (ptr->field_bc - v30) * v28;
            Time__get_deltaTime(0);
            v32 = v29 * ptr->field_e0;
            v33 = [D] unsupported_Iop_ZeroHI96ofV128();
            v34 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v32, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v32, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v32, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v32, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v32, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v32, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
            if ((char)v34)
                v35 = v33;
            else
                v35 = 0;
            v36 = v29 + (ptr->field_a0 - v29) * v35;
            v37 = v31 + (ptr->field_a4 - v31) * v35;
            RectTransform__set_anchoredPosition();
            Transform__get_localEulerAngles(v22, 0);
            goto LABEL_10c76b0;
        }
    }
    else
    {
        v38 = ptr->field_1ac;
        if (v23 != v38)
            ptr->field_75 = v38;
        if (v22)
        {
            RectTransform__get_sizeDelta(v22, 0);
            Time__get_deltaTime(0);
            v39 = v24 * ptr->field_e0;
            v40 = [D] unsupported_Iop_ZeroHI96ofV128();
            v41 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v39, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v39, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v39, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v39, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v39, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v39, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
            if ((char)v41)
                v42 = v40;
            else
                v42 = 0;
            v43 = v24 + (ptr->field_d8 - v24) * v42;
            RectTransform__set_sizeDelta();
            RectTransform__get_anchoredPosition(v22, 0);
            v44 = v30 + (ptr->field_dc - v30) * v42;
            Time__get_deltaTime(0);
            v45 = v43 * ptr->field_e0;
            v46 = [D] unsupported_Iop_ZeroHI96ofV128();
            v47 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v45, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v45, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v45, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v45, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v45, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v45, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
            if ((char)v47)
                v48 = v46;
            else
                v48 = 0;
            v36 = v43 + (ptr->field_c0 - v43) * v48;
            v37 = v44 + (ptr->field_c4 - v44) * v48;
            RectTransform__set_anchoredPosition();
            Transform__get_localEulerAngles(v22, 0);
LABEL_10c76b0:
            v1 = v36;
            v0 = v37;
            Time__get_deltaTime(0);
            v49 = (unsigned int)v36 * ptr->field_e0;
            v50 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v49, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v49, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v49, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v49, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v49, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v49, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
            v51 = [D] unsupported_Iop_ZeroHI64ofV128();
            Transform__set_localEulerAngles();
            if (ptr->field_38)
            {
                Camera__get_orthographicSize(ptr->field_38, 0);
                Time__get_deltaTime(0);
                v52 = v51 * ptr->field_68;
                v53 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v52, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v52, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v52, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v52, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v52, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v52, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                Camera__set_orthographicSize();
                return;
            }
        }
    }
    sub_f7db74();
}
```

## `bl_MiniMap.get_Target` — RVA `0xcc777c`

- Decompiled symbol: `bl_MiniMap_get_Target`
- Metadata signature: `public Transform get_Target() { }`
- Native interval: `180` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[32];
    long long field_20;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern long long g_1efd0c8;
extern long long g_1efed00;
extern char g_1fab55c;

void bl_MiniMap_get_Target(struct_1 *a0)
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
    if (!(g_1fab55c & 1))
    {
        sub_f7d92c(&g_1efd0c8);
        sub_f7d92c(&g_1efed00);
        sub_f7d92c(&g_1ef0c58);
        g_1fab55c = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (!((char)Object__op_Inequality(a0->field_20, 0, 0) & 1))
    {
        sub_1231bc8();
        return;
    }
    if (a0->field_20)
    {
        sub_1249224();
        return;
    }
    sub_f7db74(0);
}
```

## `bl_MiniMap.get_TargetPosition` — RVA `0xcc7830`

- Decompiled symbol: `bl_MiniMap_get_TargetPosition`
- Metadata signature: `public Vector3 get_TargetPosition() { }`
- Native interval: `236` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[32];
    long long field_20;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern long long g_1ef22e8;
extern char g_1fab2c9;
extern char g_1fab55d;

long long bl_MiniMap_get_TargetPosition(struct_1 *ptr)
{
    long long v0;  // x0
    long long v1;  // x0
    unsigned long long v2;  // x0

    if (!(g_1fab55d & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab55d = 1;
    }
    if (!g_1fab2c9)
    {
        sub_f7d92c(&g_1ef22e8);
        g_1fab2c9 = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v0 = Object__op_Inequality(ptr->field_20, 0, 0);
    if (!((char)v0 & 1))
        return v0;
    v1 = ptr->field_20;
    if (v1)
    {
        v1 = GameObject__get_transform(v1, 0);
        if (v1)
        {
            v2 = Transform__get_position();
            return Transform__get_position();
        }
    }
    sub_f7db74(v1);
}
```

## `bl_MiniMap.ToggleSize` — RVA `0xcc79ac`

- Decompiled symbol: `bl_MiniMap_ToggleSize`
- Metadata signature: `private void ToggleSize() { }`
- Native interval: `1012` bytes
- Result: `pseudocode`
- Heuristic layout hint: `bl_MiniMap_Recovered` matched 11 offsets against `bl_MiniMap` metadata (confidence 1.00).

```c
typedef struct bl_MiniMap_Recovered {
    char padding_0[40];
    unsigned long long LevelName;
    char padding_30[24];
    unsigned int m_MapType;
    char padding_4c[8];
    unsigned int DefaultHeight;
    unsigned int maxHeight;
    char padding_5c[16];
    char useCompassRotation;
    char padding_6d[15];
    char ShowLevelName;
    char ShowPanelInfo;
    char padding_7e[10];
    long long BottonAnimator;
    long long PanelInfoAnimator;
    char padding_98[90];
    char ResetOffSetOnChange;
    char padding_f3[201];
    char DefaultRotationCircle;
} bl_MiniMap_Recovered;

typedef struct struct_4 {
    char padding_0[1512];
    struct struct_5 *field_5e8;
    unsigned long long field_5f0;
} struct_4;

typedef struct struct_5 {
    unsigned long long field_0;
} struct_5;

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
extern struct_1 *g_1ef2b00;
extern long long g_1efd140;
extern long long g_1f0c248;
extern long long g_1f14958;
extern long long g_1f14c08;
extern char g_1fab552;

long long bl_MiniMap_ToggleSize(struct_3 *ptr)
{
    unsigned int v0;  // w9
    unsigned long v1;  // cc_dep1
    unsigned long long v10;  // x1
    unsigned long long v11;  // x2
    unsigned long long v12;  // x0
    long long v13;  // x0
    long long v14;  // x0
    unsigned long v2;  // 4102
    long long v3;  // x0
    unsigned long v4;  // 4102
    unsigned int v5;  // w8
    long long v6;  // x0
    unsigned int v7;  // w20
    long long v8;  // x0
    struct_4 **v9;  // x0

    if (!(g_1fab552 & 1))
    {
        sub_f7d92c(&g_1efd140);
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c(&g_1f14958);
        sub_f7d92c(&g_1f0c248);
        sub_f7d92c(&g_1f14c08);
        sub_f7d92c(&g_1ef2b00);
        g_1fab552 = 1;
    }
    v0 = g_1ef2b00->field_b8->field_0;
    g_1ef2b00->field_b8->field_0 = (char)v0 ^ 1;
    v1 = ptr->field_48;
    if (!v0)
    {
        v2 = arm64g_calculate_condition(3, v1, 1, 0);
        if (!((char)v2))
            ptr->field_54 = ptr->field_58;
        ptr->field_6c = 0;
        v3 = bl_MiniMap__get_m_maskHelper(ptr);
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        if (!(Object__op_Implicit(v3, 0) & 1))
            goto LABEL_10c7b14;
        if (bl_MiniMap__get_m_maskHelper(ptr))
            goto LABEL_10c7b0c;
    }
    else
    {
        v4 = arm64g_calculate_condition(3, v1, 1, 0);
        if (!((char)v4))
        {
            PlayerPrefs__GetFloat(g_1f0c248, 0);
            ptr->field_54 = ptr->field_54;
        }
        v5 = ptr->field_1bc;
        if (ptr->field_6c != v5)
            ptr->field_6c = v5;
        v6 = bl_MiniMap__get_m_maskHelper(ptr);
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        if (((char)Object__op_Implicit(v6, 0) & 1))
        {
            if (!bl_MiniMap__get_m_maskHelper(ptr))
                sub_f7db74();
LABEL_10c7b0c:
            bl_MaskHelper__OnChange();
        }
LABEL_10c7b14:
        if (ptr->field_f2)
            bl_MiniMap__GoToTarget(ptr); /* do not return */
        if (g_1ef2b00->field_b8->field_0)
            v7 = 1;
        else
            v7 = 2;
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        if (!(((char)Object__op_Inequality(ptr->field_88, 0, 0) & 1) && ptr->field_7c))
        {
            if (!g_1ef0c58->field_e0)
                sub_f7da5c(g_1ef0c58);
            if (((char)Object__op_Inequality(ptr->field_88, 0, 0) & 1))
            {
                if (ptr->field_88 && Component__get_gameObject(ptr->field_88, 0))
                {
                    GameObject__SetActive();
                    goto LABEL_10c7c9c;
                }
            }
            else
            {
LABEL_10c7c9c:
                if (!g_1ef0c58->field_e0)
                    sub_f7da5c(g_1ef0c58);
                if (((char)Object__op_Inequality(ptr->field_90, 0, 0) & 1) && ptr->field_7d)
                {
                    if (ptr->field_90 && Component__get_gameObject(ptr->field_90, 0))
                    {
                        if (!((char)GameObject__get_activeSelf() & 1))
                        {
                            if (ptr->field_90 && Component__get_gameObject(ptr->field_90, 0))
                            {
                                GameObject__SetActive();
                                goto LABEL_10c7d0c;
                            }
                        }
                        else
                        {
LABEL_10c7d0c:
                            if (ptr->field_90)
                            {
                                v12 = Animator__SetInteger();
                                return Animator__SetInteger();
                            }
                        }
                    }
                }
                else
                {
                    if (!g_1ef0c58->field_e0)
                        sub_f7da5c(g_1ef0c58);
                    v13 = Object__op_Inequality(ptr->field_90, 0, 0);
                    if (!((char)v13 & 1))
                        return v13;
                    if (ptr->field_90 && Component__get_gameObject(ptr->field_90, 0))
                    {
                        v14 = GameObject__SetActive();
                        return GameObject__SetActive();
                    }
                }
            }
        }
        else if (ptr->field_88 && Component__get_gameObject(ptr->field_88, 0))
        {
            if (((char)GameObject__get_activeSelf() & 1))
            {
LABEL_10c7bac:
                if (ptr->field_88 && Component__get_transform(ptr->field_88, 0))
                {
                    v8 = sub_1231e2c();
                    if (!g_1ef0c58->field_e0)
                        sub_f7da5c(g_1ef0c58);
                    if (((char)Object__op_Inequality(v8, 0, 0) & 1))
                    {
                        if (ptr->field_88 && Component__get_transform(ptr->field_88, 0))
                        {
                            v9 = sub_1231e2c();
                            if (v9)
                            {
                                v10 = ptr->field_28;
                                v11 = *(v9)->field_5f0;
                                *(v9)->field_5e8();
                            }
                        }
                    }
                    else
                    {
                        if (ptr->field_88)
                        {
                            Animator__SetInteger(ptr->field_88, g_1f14c08, v7, 0);
                            goto LABEL_10c7c9c;
                        }
                    }
                }
            }
            else if (ptr->field_88 && Component__get_gameObject(ptr->field_88, 0))
            {
                GameObject__SetActive();
                goto LABEL_10c7bac;
            }
        }
    }
    sub_f7db74();
}
```

## `bl_MiniMap.ChangeHeight` — RVA `0xcc7da0`

- Decompiled symbol: `bl_MiniMap_ChangeHeight`
- Metadata signature: `public void ChangeHeight(bool b) { }`
- Native interval: `160` bytes
- Result: `pseudocode`

```c
extern long long g_1f0c248;
extern char g_1fab555;

unsigned int [24] bl_MiniMap_ChangeHeight(unsigned int *ptr, unsigned int a1)
{
    unsigned int v0[24];  // x0
    unsigned int v1[24];  // x0
    unsigned int v2[24];  // x0
    unsigned int v3;  // s1
    unsigned int v4;  // s0
    unsigned long v5;  // 4158
    unsigned int v6;  // s1
    unsigned long v7;  // 4158

    v0 = ptr;
    if (!(g_1fab555 & 1))
    {
        v1 = sub_f7d92c(&g_1f0c248);
        g_1fab555 = 1;
        v0 = v1;
    }
    v2 = v0;
    if (ptr[18] == 1)
        return v2;
    if (((char)a1 & 1))
    {
        v3 = ptr[22];
        v4 = ptr[21] + ptr[20];
        v5 = arm64g_calculate_condition(144, (((((unsigned long long)(char)(CmpF(v4, v3)) >> 5 & 3 | (unsigned long long)(CmpF(v4, v3) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v4, v3)) >> 5 & 3 | (unsigned long long)(CmpF(v4, v3) & 1)) & ((unsigned long long)(char)(CmpF(v4, v3)) >> 5 & 3 | (unsigned long long)(CmpF(v4, v3) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if (!((char)v5))
            v4 = v3;
    }
    else
    {
        v6 = ptr[23];
        v4 = ptr[21] - ptr[20];
        v7 = arm64g_calculate_condition(160, (((((unsigned long long)(char)(CmpF(v4, v6)) >> 5 & 3 | (unsigned long long)(CmpF(v4, v6) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v4, v6)) >> 5 & 3 | (unsigned long long)(CmpF(v4, v6) & 1)) & ((unsigned long long)(char)(CmpF(v4, v6)) >> 5 & 3 | (unsigned long long)(CmpF(v4, v6) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if (!((char)v7))
            v4 = v6;
    }
LABEL_10c7e28:
    ptr[21] = v4;
    goto LABEL_10c7e28;
}
```

## `bl_MiniMap.ResetMapRotation` — RVA `0xcc7e40`

- Decompiled symbol: `bl_MiniMap_ResetMapRotation`
- Metadata signature: `private void ResetMapRotation() { }`
- Native interval: `44` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[464];
    long long field_1d0;
} struct_1;

void bl_MiniMap_ResetMapRotation(void)
{
    unsigned long long v1;  // x30
    struct_1 *v2;  // x0
    unsigned long long v0;  // [bp-0x10]

    v0 = v1;
    if (bl_MiniMap__get_m_Transform(v2))
    {
        Transform__set_eulerAngles();
        return;
    }
    sub_f7db74();
}
```

## `bl_MiniMap.get_m_maskHelper` — RVA `0xcc7e6c`

- Decompiled symbol: `bl_MiniMap_get_m_maskHelper`
- Metadata signature: `private bl_MaskHelper get_m_maskHelper() { }`
- Native interval: `188` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[472];
    long long field_1d8;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern long long g_1efd158;
extern char g_1fab55f;

long long bl_MiniMap_get_m_maskHelper(struct_1 *a0)
{
    struct_1 *ptr;  // x19
    long long v1;  // x0

    if (!(g_1fab55f & 1))
    {
        sub_f7d92c(&g_1efd158);
        sub_f7d92c(&g_1ef0c58);
        g_1fab55f = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    ptr = &a0->field_1d8;
    if (((char)Object__op_Equality(a0->field_1d8, 0, 0) & 1))
    {
        if (Component__get_transform(a0, 0) && Transform__get_root())
        {
            v1 = sub_1231e2c();
            *((long long *)&ptr->padding_0[0]) = v1;
            sub_f7d8d0(ptr, v1);
        }
        else
        {
            sub_f7db74();
        }
    }
    return *((long long *)&ptr->padding_0[0]);
}
```

## `bl_MiniMap.GoToTarget` — RVA `0xcc8020`

- Decompiled symbol: `bl_MiniMap_GoToTarget`
- Metadata signature: `public void GoToTarget() { }`
- Native interval: `44` bytes
- Result: `pseudocode`

```c
void bl_MiniMap_GoToTarget(long long a0)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    MonoBehaviour__StopAllCoroutines();
    bl_MiniMap__ResetOffset(a0);
    MonoBehaviour__StartCoroutine();
    return;
}
```

## `bl_MiniMap.SetDragPosition` — RVA `0xcc804c`

- Decompiled symbol: `bl_MiniMap_SetDragPosition`
- Metadata signature: `public void SetDragPosition(Vector3 pos) { }`
- Native interval: `184` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    char padding_0[241];
    char field_f1;
    char padding_f2[2];
    unsigned int field_f4;
    unsigned int field_f8;
    unsigned int field_fc;
    unsigned int field_100;
    char padding_104[156];
    unsigned int field_1a0;
    char padding_1a4[4];
    unsigned int field_1a8;
} struct_2;

typedef struct struct_1 {
    char field_0;
} struct_1;

typedef struct struct_0 {
    char padding_0[184];
    struct struct_1 *field_b8;
} struct_0;

extern struct_0 *g_1ef2b00;
extern char g_1fab553;

void bl_MiniMap_SetDragPosition(struct_2 *ptr)
{
    unsigned int v0;  // s0
    unsigned int v1;  // s0
    unsigned int v10;  // s3
    unsigned long v11;  // 4136
    unsigned int v12;  // s0
    unsigned long v13;  // 4129
    unsigned int v2;  // s4
    unsigned int v3;  // s2
    unsigned int v4;  // s1
    unsigned int v5;  // s1
    unsigned int v6;  // s3
    unsigned long v7;  // 4208
    unsigned long v8;  // 4129
    unsigned int v9;  // s0

    if (!(g_1fab553 & 1))
    {
        sub_f7d92c(&g_1ef2b00);
        g_1fab553 = 1;
    }
    if (ptr->field_f1 && !g_1ef2b00->field_b8->field_0)
        return;
    v1 = ptr->field_1a0 - v0 * ptr->field_f4;
    v2 = ptr->field_fc;
    v3 = ptr->field_100;
    v5 = ptr->field_1a8 - v4 * ptr->field_f8;
    v6 = -(v2);
    v7 = arm64g_calculate_condition(192, (((((unsigned long long)(char)(CmpF(v1, v2)) >> 5 & 3 | (unsigned long long)(CmpF(v1, v2) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v1, v2)) >> 5 & 3 | (unsigned long long)(CmpF(v1, v2) & 1)) & ((unsigned long long)(char)(CmpF(v1, v2)) >> 5 & 3 | (unsigned long long)(CmpF(v1, v2) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if (!((char)v7))
        v2 = v1;
    v8 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v1, v6)) >> 5 & 3 | (unsigned long long)(CmpF(v1, v6) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v1, v6)) >> 5 & 3 | (unsigned long long)(CmpF(v1, v6) & 1)) & ((unsigned long long)(char)(CmpF(v1, v6)) >> 5 & 3 | (unsigned long long)(CmpF(v1, v6) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if ((char)v8)
        v9 = v2;
    else
        v9 = v6;
    v10 = -(v3);
    ptr->field_1a0 = v9;
    v11 = arm64g_calculate_condition(192, (((((unsigned long long)(char)(CmpF(v5, v3)) >> 5 & 3 | (unsigned long long)(CmpF(v5, v3) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v5, v3)) >> 5 & 3 | (unsigned long long)(CmpF(v5, v3) & 1)) & ((unsigned long long)(char)(CmpF(v5, v3)) >> 5 & 3 | (unsigned long long)(CmpF(v5, v3) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if ((char)v11)
        v12 = v3;
    else
        v12 = v5;
    v13 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v5, v10)) >> 5 & 3 | (unsigned long long)(CmpF(v5, v10) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v5, v10)) >> 5 & 3 | (unsigned long long)(CmpF(v5, v10) & 1)) & ((unsigned long long)(char)(CmpF(v5, v10)) >> 5 & 3 | (unsigned long long)(CmpF(v5, v10) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if (!((char)v13))
        v12 = v10;
    ptr->field_1a8 = v12;
    return;
}
```

## `bl_MiniMap.ResetOffset` — RVA `0xcc8104`

- Decompiled symbol: `bl_MiniMap_ResetOffset`
- Metadata signature: `private IEnumerator ResetOffset() { }`
- Native interval: `108` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[12];
    long long field_20;
} struct_0;

extern long long g_1ef4190;
extern char g_1fab554;

struct_0 * bl_MiniMap_ResetOffset(long long a0)
{
    struct_0 *v0;  // x20
    struct_0 *ptr;  // x0

    if (!(g_1fab554 & 1))
    {
        sub_f7d92c(&g_1ef4190);
        g_1fab554 = 1;
    }
    v0 = sub_f7db70(g_1ef4190);
    Object__ctor(v0, 0);
    ptr = v0;
    ptr->field_10 = 0;
    ptr->field_20 = a0;
    sub_f7d8d0((struct struct_0 *)&ptr->field_20, a0);
    return ptr;
}
```

## `bl_MiniMap.<ResetOffset>d__81.ctor` — RVA `0xcc8170`

- Decompiled symbol: `bl_MiniMap_ResetOffset_d__81_ctor`
- Metadata signature: `public void .ctor(int <>1__state) { }`
- Native interval: `40` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

void bl_MiniMap_ResetOffset_d__81_ctor(struct_0 *ptr, unsigned int a1)
{
    Object__ctor();
    ptr->field_10 = a1;
    return;
}
```

## `bl_MiniMap.DoHitEffect` — RVA `0xcc8198`

- Decompiled symbol: `bl_MiniMap_DoHitEffect`
- Metadata signature: `public void DoHitEffect() { }`
- Native interval: `248` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    char padding_0[152];
    unsigned long long field_98;
} struct_2;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

typedef struct struct_1 {
    char padding_0[224];
    unsigned int field_e0;
} struct_1;

extern struct_0 *g_1eef458;
extern struct_1 *g_1ef0c58;
extern long long g_1f0ab08;
extern long long g_1f0cfa0;
extern char g_1fab556;

void bl_MiniMap_DoHitEffect(struct_2 *ptr)
{
    unsigned long long v4;  // x30
    unsigned long long v5;  // x21
    unsigned long long v6;  // x20
    unsigned long long v7;  // x19
    unsigned long long v8;  // x0
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x18]
    unsigned long long v2;  // [bp-0x10]
    unsigned long long v3;  // [bp-0x8]

    v0 = v4;
    v1 = v5;
    v2 = v6;
    v3 = v7;
    if (!(g_1fab556 & 1))
    {
        sub_f7d92c(&g_1eef458);
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c(&g_1f0ab08);
        sub_f7d92c(&g_1f0cfa0);
        g_1fab556 = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (((char)Object__op_Equality(ptr->field_98, 0, 0) & 1))
    {
        if (!g_1eef458->field_e0)
            sub_f7da5c(g_1eef458);
        Debug__LogWarning();
        return;
    }
    v8 = ptr->field_98;
    if (v8)
    {
        Animator__set_speed(v8, 0);
        v8 = ptr->field_98;
    }
    sub_f7db74(v8);
}
```

## `bl_MiniMap.CreateNewItem` — RVA `0xcc8290`

- Decompiled symbol: `bl_MiniMap_CreateNewItem`
- Metadata signature: `public void CreateNewItem(bl_MMItemInfo item) { }`
- Native interval: `464` bytes
- Result: `pseudocode`
- Heuristic layout hint: `bl_MiniMap_Recovered` matched 6 offsets against `bl_MiniMap` metadata (confidence 1.00).

```c
typedef struct struct_1 {
    char padding_0[32];
    long long field_20;
    unsigned int field_28;
    uint128_t field_2c;
    char field_3c;
    char padding_3d[3];
    long long field_40;
    unsigned int field_48;
} struct_1;

typedef struct struct_3 {
    char padding_0[392];
    long long field_188;
} struct_3;

typedef struct bl_MiniMap_Recovered {
    char padding_0[40];
    long long LevelName;
    char padding_30[16];
    long long m_Type;
    char padding_48[8];
    uint128_t scrollSensitivity;
    unsigned int IncreaseHeightKey;
    char padding_64[24];
    char ShowLevelName;
    char padding_7d[27];
    unsigned int HitEffectAnimator;
} bl_MiniMap_Recovered;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern long long g_1efed40;
extern long long g_1f00260;
extern char g_1fab2cb;
extern char g_1fab558;

long long bl_MiniMap_CreateNewItem(struct_3 *addr, struct_1 *ptr3)
{
    long long v0;  // x20
    struct_2 *ptr;  // x20
    long long v2;  // x1
    struct_2 *p;  // x0
    long long v4;  // x0
    long long v5;  // x0

    if (!(g_1fab558 & 1))
    {
        sub_f7d92c(&g_1efed40);
        sub_f7d92c(&g_1f00260);
        sub_f7d92c(&g_1ef0c58);
        g_1fab558 = 1;
    }
    if (ptr3)
    {
        v0 = addr->field_188;
        if (!g_1fab2cb)
        {
            sub_f7d92c("-M");
            g_1fab2cb = 1;
        }
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        if (sub_112a1ac(v0, g_1f00260))
        {
            ptr = sub_1249224();
            if (((char)Object__op_Inequality(ptr3->field_20, 0, 0) & 1))
            {
                if (ptr)
                {
                    v2 = ptr3->field_20;
                    p = ptr;
                    p->field_28 = v2;
                    sub_f7d8d0((struct bl_MiniMap_Recovered *)&p->field_28, v2);
LABEL_10c83c8:
                    ptr->field_60 = ptr3->field_28;
                    ptr->field_50 = *((int128_t *)&(&ptr3->field_28)[1]);
                    ptr->field_7c = *((char *)&ptr3->field_2c + 12);
                    ptr->field_98 = ptr3->field_40;
                    if (!g_1ef0c58->field_e0)
                        sub_f7da5c(g_1ef0c58);
                    v4 = Object__op_Inequality(*((long long *)&ptr3->field_3c), 0, 0);
                    if (!((char)v4 & 1))
                        return v4;
                    ptr->field_40 = *((long long *)&ptr3->field_3c);
                    v5 = sub_f7d8d0();
                    return sub_f7d8d0();
                }
            }
            else
            {
                if (ptr)
                    goto LABEL_10c83c8;
            }
        }
    }
    sub_f7db74();
}
```

## `bl_MiniMap.RotationMap` — RVA `0xcc8460`

- Decompiled symbol: `bl_MiniMap_RotationMap`
- Metadata signature: `public void RotationMap(bool mode) { }`
- Native interval: `104` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char field_0;
} struct_1;

typedef struct struct_0 {
    char padding_0[184];
    struct struct_1 *field_b8;
} struct_0;

extern struct_0 *g_1ef2b00;
extern char g_1fab559;

char [429] bl_MiniMap_RotationMap(char *ptr, char a1)
{
    char v0[429];  // x0
    char v1[429];  // x0
    char v2[429];  // x0
    char v3;  // x8

    v0 = ptr;
    if (!(g_1fab559 & 1))
    {
        v1 = sub_f7d92c(&g_1ef2b00);
        g_1fab559 = 1;
        v0 = v1;
    }
    v2 = v0;
    if (!g_1ef2b00->field_b8->field_0)
    {
        v3 = a1 & 1;
        ptr[117] = v3;
        ptr[428] = v3;
    }
    return v2;
}
```

## `bl_MiniMap.ChangeMapSize` — RVA `0xcc84c8`

- Decompiled symbol: `bl_MiniMap_ChangeMapSize`
- Metadata signature: `public void ChangeMapSize(bool fullscreen) { }`
- Native interval: `80` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char field_0;
} struct_1;

typedef struct struct_0 {
    char padding_0[184];
    struct struct_1 *field_b8;
} struct_0;

extern struct_0 *g_1ef2b00;
extern char g_1fab55a;

unsigned long long bl_MiniMap_ChangeMapSize(unsigned long long a0, char a1)
{
    if (!(g_1fab55a & 1))
    {
        a0 = sub_f7d92c(&g_1ef2b00);
        g_1fab55a = 1;
    }
    g_1ef2b00->field_b8->field_0 = a1 & 1;
    return a0;
}
```

## `bl_MiniMap.SetTarget` — RVA `0xcc8518`

- Decompiled symbol: `bl_MiniMap_SetTarget`
- Metadata signature: `public void SetTarget(GameObject t) { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[32];
    unsigned long long field_20;
} struct_0;

long long bl_MiniMap_SetTarget(struct_0 *ptr, unsigned long a1)
{
    long long v0;  // x0

    ptr->field_20 = a1;
    v0 = sub_f7d8d0();
    return sub_f7d8d0();
}
```

## `bl_MiniMap.SetMapTexture` — RVA `0xcc8520`

- Decompiled symbol: `bl_MiniMap_SetMapTexture`
- Metadata signature: `public void SetMapTexture(Texture t) { }`
- Native interval: `200` bytes
- Result: `pseudocode`
- Heuristic layout hint: `bl_MiniMap_Recovered` matched 2 offsets against `bl_MiniMap` metadata (confidence 1.00).

```c
typedef struct bl_MiniMap_Recovered {
    char padding_0[64];
    unsigned int m_Type;
    char padding_44[380];
    long long plane;
} bl_MiniMap_Recovered;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1eef458;
extern long long g_1efec50;
extern char g_1fab55b;

void bl_MiniMap_SetMapTexture(struct_1 *ptr, unsigned long a1)
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
    if (!(g_1fab55b & 1))
    {
        sub_f7d92c(&g_1eef458);
        sub_f7d92c(&g_1efec50);
        sub_f7d92c("#'");
        g_1fab55b = 1;
    }
    if (ptr->field_40 == 1)
    {
        v8 = ptr->field_1c0;
        if (v8)
        {
            v8 = sub_1249224(v8, g_1efec50);
            if (v8)
            {
                v8 = Renderer__get_material();
                if (v8)
                {
                    Material__set_mainTexture();
                    return;
                }
            }
        }
        sub_f7db74(v8);
    }
    else
    {
        if (!g_1eef458->field_e0)
            sub_f7da5c(g_1eef458);
        Debug__LogWarning();
        return;
    }
}
```

## `bl_MiniMap.GetFullMapSize` — RVA `0xcc85e8`

- Decompiled symbol: `bl_MiniMap_GetFullMapSize`
- Metadata signature: `private void GetFullMapSize() { }`
- Native interval: `88` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[160];
    unsigned int field_a0;
    unsigned int field_a4;
    unsigned int field_a8;
    unsigned int field_ac;
    unsigned int field_b0;
    unsigned int field_b4;
    unsigned int field_b8;
    unsigned int field_bc;
    char padding_c0[184];
    unsigned long long field_178;
} struct_0;

unsigned long long bl_MiniMap_GetFullMapSize(struct_0 *ptr)
{
    unsigned long long v0;  // x0
    unsigned int v1;  // s0
    unsigned int v2;  // s1
    unsigned long long v3;  // x0
    unsigned int v4;  // s2

    v0 = ptr->field_178;
    if (v0)
    {
        RectTransform__get_sizeDelta(v0, 0);
        v0 = ptr->field_178;
        ptr->field_b8 = v1;
        ptr->field_bc = v2;
        if (v0)
        {
            RectTransform__get_anchoredPosition(v0, 0);
            v0 = ptr->field_178;
            ptr->field_a0 = v1;
            ptr->field_a4 = v2;
            ptr->field_a8 = 0;
            if (v0)
            {
                v3 = Transform__get_eulerAngles(v0, 0);
                ptr->field_ac = v1;
                ptr->field_b0 = v2;
                ptr->field_b4 = v4;
                return v3;
            }
        }
    }
    sub_f7db74(v0);
}
```

## `bl_MiniMap.ctor` — RVA `0xcc8640`

- Decompiled symbol: `bl_MiniMap_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `780` bytes
- Result: `pseudocode`
- Heuristic layout hint: `bl_MiniMap_Recovered` matched 32 offsets against `bl_MiniMap` metadata (confidence 0.84).

```c
typedef struct bl_MiniMap_Recovered {
    char padding_0[48];
    unsigned long long MiniMapLayer;
    char padding_38[8];
    unsigned int m_Type;
    char padding_44[8];
    unsigned long long IconMultiplier;
    unsigned long long DefaultHeight;
    unsigned int minHeight;
    unsigned long long IncreaseHeightKey;
    unsigned int LerpHeight;
    char padding_6c[4];
    unsigned int CompassSize;
    unsigned short RotationAlwaysFront;
    char SmoothRotation;
    char padding_77[1];
    unsigned int LerpRotation;
    unsigned short ShowLevelName;
    char padding_7e[2];
    unsigned int HitEffectSpeed;
    char padding_84[28];
    unsigned long long FullMapPosition;
    unsigned int field_a8;
    unsigned long long FullMapRotation;
    unsigned int field_b4;
    unsigned long long FullMapSize;
    unsigned long long MiniMapPosition;
    unsigned int field_c8;
    unsigned long long MiniMapRotation;
    unsigned int field_d4;
    unsigned long long MiniMapSize;
    unsigned int LerpTransition;
    char padding_e4[4];
    long long GetWorldRect;
    unsigned short CanDragMiniMap;
    char ResetOffSetOnChange;
    char padding_f3[1];
    uint128_t DragMovementSpeed;
    char padding_104[12];
    unsigned long long HotSpot;
    char padding_118[8];
    uint128_t TintColor;
    uint128_t SpecularColor;
    uint128_t EmessiveColor;
    unsigned int EmissionAmount;
    char padding_154[68];
    long long ItemsList;
    unsigned long long DragOffset;
    unsigned int field_1a8;
    char padding_1ac[4];
    unsigned long long DeafultMapRot;
    unsigned int field_1b8;
} bl_MiniMap_Recovered;

typedef struct struct_2 {
    unsigned long long field_0;
} struct_2;

typedef struct struct_3 {
    unsigned long long field_0;
    unsigned int field_8;
} struct_3;

typedef struct struct_1 {
    char padding_0[184];
    struct struct_2 *field_b8;
} struct_1;

typedef struct struct_4 {
    char padding_0[184];
    struct struct_3 *field_b8;
} struct_4;

extern long long g_1eec6b8;
extern struct_1 *g_1ef22b8;
extern struct_4 *g_1ef22e8;
extern long long g_1ef5a38;
extern long long g_1f06220;
extern char g_1fab1e0;
extern char g_1fab2c9;
extern char g_1fab560;

void bl_MiniMap_ctor(struct_0 *ptr)
{
    unsigned long long v10;  // x30
    unsigned long long v11;  // x27
    unsigned long long v20;  // d0
    unsigned int v21;  // w8
    unsigned int v22;  // s1
    unsigned long long v23;  // d0
    unsigned int v24;  // w8
    unsigned int v25;  // s1
    unsigned long long v26;  // d0
    struct_0 *p;  // x20
    unsigned long long v28;  // d2
    long long v29;  // x20
    unsigned long long v12;  // x26
    unsigned int v30;  // s1
    unsigned int v31;  // s1
    unsigned long long v13;  // x25
    unsigned long long v14;  // x24
    unsigned long long v15;  // x23
    unsigned long long v16;  // x22
    unsigned long long v17;  // x21
    unsigned long long v18;  // x20
    unsigned long long v19;  // x19
    unsigned long long v0;  // [bp-0x50]
    unsigned long long v1;  // [bp-0x48]
    unsigned long long v2;  // [bp-0x40]
    unsigned long long v3;  // [bp-0x38]
    unsigned long long v4;  // [bp-0x30]
    unsigned long long v5;  // [bp-0x28]
    unsigned long long v6;  // [bp-0x20]
    unsigned long long v7;  // [bp-0x18]
    unsigned long long v8;  // [bp-0x10]
    unsigned long long v9;  // [bp-0x8]

    v0 = v10;
    v1 = v11;
    v2 = v12;
    v3 = v13;
    v4 = v14;
    v5 = v15;
    v6 = v16;
    v7 = v17;
    v8 = v18;
    v9 = v19;
    if (!(g_1fab560 & 1))
    {
        sub_f7d92c(&g_1ef5a38);
        sub_f7d92c(&g_1eec6b8);
        sub_f7d92c(&g_1f06220);
        g_1fab560 = 1;
    }
    ptr->field_30 = 433791696906;
    *((unsigned long long *)&(&ptr->padding_44)[1]) = 0x33f800000;
    *((unsigned long long *)((char *)&ptr->field_4c + 4)) = 0x42a0000041f00000;
    *((unsigned int *)((char *)&ptr->field_54 + 4)) = 0x40a00000;
    ptr->field_68 = 0x432f0000;
    *((unsigned int *)&ptr->field_60) = 0x41000000;
    ptr->field_70 = 0x41000000;
    ptr->field_40 = 1;
    *((unsigned short *)&ptr->padding_6c[0]) = 257;
    ptr->padding_6c[2] = 1;
    ptr->field_74 = 257;
    ptr->field_78 = 0x3fc00000;
    *((unsigned long long *)&ptr->field_5c) = 1155346202894;
    if (!g_1fab1e0)
    {
        sub_f7d92c(&g_1ef22b8);
        g_1fab1e0 = 1;
    }
    v20 = g_1ef22b8->field_b8->field_0;
    *((unsigned int *)&ptr->field_a0) = 0;
    v21 = 0;
    *((unsigned long long *)&ptr->padding_84[20]) = v20;
    if (!g_1fab2c9)
    {
        sub_f7d92c(&g_1ef22e8);
        g_1fab2c9 = 1;
        if (g_1fab1e0)
            v21 = 0;
        else
            v21 = 1;
    }
    v22 = g_1ef22e8->field_b8->field_8;
    *((unsigned long long *)((char *)&ptr->field_a0 + 4)) = g_1ef22e8->field_b8->field_0;
    (&ptr->field_a8)[1] = v22;
    if (v21)
    {
        sub_f7d92c(&g_1ef22b8);
        g_1fab1e0 = 1;
    }
    ptr->field_ac = g_1ef22b8->field_b8->field_0;
    v23 = g_1ef22b8->field_b8->field_0;
    *((unsigned int *)&ptr->field_b8) = 0;
    v24 = 0;
    *((unsigned long long *)&ptr->field_b4) = v23;
    if (!g_1fab2c9)
    {
        sub_f7d92c(&g_1ef22e8);
        g_1fab2c9 = 1;
        if (g_1fab1e0)
            v24 = 0;
        else
            v24 = 1;
    }
    v25 = g_1ef22e8->field_b8->field_8;
    *((unsigned long long *)((char *)&ptr->field_b8 + 4)) = g_1ef22e8->field_b8->field_0;
    *((unsigned int *)((char *)&ptr->field_c0 + 4)) = v25;
    if (v24)
    {
        sub_f7d92c(&g_1ef22b8);
        g_1fab1e0 = 1;
    }
    v26 = g_1ef22b8->field_b8->field_0;
    *((unsigned int *)&ptr->field_cc) = 0x40e00000;
    *((unsigned long long *)&ptr->field_c8) = v26;
    *((long long *)&ptr->field_d4) = g_1f06220;
    p = &ptr->field_d4;
    sub_f7d8d0(p, g_1f06220);
    *((unsigned short *)&p->padding_0[8]) = 257;
    p->padding_0[10] = 1;
    *((uint128_t *)&p->padding_0[12]) = 0x447a0000447a00003eb333333f000000;
    if (!g_1fab1e0)
    {
        sub_f7d92c(&g_1ef22b8);
        g_1fab1e0 = 1;
    }
    v28 = g_1ef22b8->field_b8->field_0;
    *((uint128_t *)&ptr->padding_104) = 0x3f6666663f8000003f8000003f800000;
    *((uint128_t *)&ptr->field_110) = 0x3f6666663f8000003f8000003f800000;
    ptr->field_120 = 0x3f666666000000000000000000000000;
    *((unsigned int *)&ptr->field_130) = 0x3f800000;
    *((unsigned long long *)&ptr->field_f4) = v28;
    v29 = sub_f7db70(g_1eec6b8);
    sub_12b0eec(v29, g_1ef5a38);
    *((long long *)&ptr->padding_154[36]) = v29;
    sub_f7d8d0((struct bl_MiniMap_Recovered *)&ptr->padding_154[36], v29);
    if (!g_1fab2c9)
    {
        sub_f7d92c(&g_1ef22e8);
        g_1fab2c9 = 1;
    }
    v30 = g_1ef22e8->field_b8->field_8;
    *((unsigned long long *)&ptr->padding_154[44]) = g_1ef22e8->field_b8->field_0;
    *((unsigned int *)&ptr->padding_154[52]) = v30;
    v31 = g_1ef22e8->field_b8->field_8;
    *((unsigned long long *)&ptr->padding_154[60]) = g_1ef22e8->field_b8->field_0;
    *((unsigned int *)&ptr->field_198) = v31;
    MonoBehaviour__ctor();
    return;
}
```

## `bl_MiniMap.<ResetOffset>d__81.Dispose` — RVA `0xcc894c`

- Decompiled symbol: `bl_MiniMap_ResetOffset_d__81_Dispose`
- Metadata signature: `private void System.IDisposable.Dispose() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long bl_MiniMap_ResetOffset_d__81_Dispose(void)
{
    unsigned long v0;  // x0

    return v0;
}
```

## `bl_MiniMap.<ResetOffset>d__81.MoveNext` — RVA `0xcc8950`

- Decompiled symbol: `bl_MiniMap_ResetOffset_d__81_MoveNext`
- Metadata signature: `private bool MoveNext() { }`
- Native interval: `464` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
    char padding_e4[188];
    unsigned long long field_1a0;
    unsigned int field_1a8;
} struct_0;

typedef struct struct_1 {
    unsigned long long field_0;
    unsigned int field_8;
} struct_1;

typedef struct struct_2 {
    char padding_0[184];
    struct struct_1 *field_b8;
} struct_2;

extern struct_2 *g_1ef22e8;
extern char g_1fab2c9;
extern char g_1fab3e0;

unsigned int bl_MiniMap_ResetOffset_d__81_MoveNext(void* p)
{
    struct_0 *ptr;  // x20
    unsigned int v1;  // s0
    unsigned int v10;  // s1
    unsigned long v2;  // 4197
    unsigned int v3;  // s9
    unsigned int v4;  // s3
    unsigned int v5;  // s0
    unsigned int v6;  // s1
    unsigned int v7;  // s0
    unsigned long v8;  // 4182

    if (2 <= (int)p[16])
        return 0;
    ptr = (long long)p[32];
    *((unsigned int *)&p[16]) = 4294967295;
    if (ptr)
    {
        if (!g_1fab2c9)
        {
            sub_f7d92c(&g_1ef22e8);
            g_1fab2c9 = 1;
        }
        if (!g_1fab3e0)
        {
            sub_f7d92c("_F");
            g_1fab3e0 = 1;
        }
        if (!g_1ef07e8->field_e0)
            sub_f7da5c(g_1ef07e8);
        v1 = [D] unsupported_Iop_SqrtF32();
        v2 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v1, 1045220557)) >> 5 & 3 | (unsigned long long)(CmpF(v1, 1045220557) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v1, 1045220557)) >> 5 & 3 | (unsigned long long)(CmpF(v1, 1045220557) & 1)) & ((unsigned long long)(char)(CmpF(v1, 1045220557)) >> 5 & 3 | (unsigned long long)(CmpF(v1, 1045220557) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if (!((char)v2))
        {
            v3 = ptr->field_1a8;
            if (!g_1fab2c9)
            {
                sub_f7d92c(&g_1ef22e8);
                g_1fab2c9 = 1;
            }
            Time__get_deltaTime(0);
            v4 = g_1ef22e8->field_b8->field_8 - v3;
            v5 = v1 * ptr->field_e0;
            v6 = [D] unsupported_Iop_ZeroHI96ofV128();
            v7 = 0;
            v8 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v5, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v5, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v5, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v5, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v5, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v5, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
            if ((char)v8)
                v7 = v6;
            ptr->field_1a0 = [D] unsupported_Iop_ZeroHI64ofV128();
            ptr->field_1a8 = v3 + v4 * v7;
            *((unsigned long long *)&p[24]) = 0;
            sub_f7d8d0();
            *((unsigned int *)&p[16]) = 1;
            return 1;
        }
        else
        {
            if (!g_1fab2c9)
            {
                sub_f7d92c(&g_1ef22e8);
                g_1fab2c9 = 1;
            }
            v10 = g_1ef22e8->field_b8->field_8;
            ptr->field_1a0 = g_1ef22e8->field_b8->field_0;
            ptr->field_1a8 = v10;
            return 0;
        }
    }
    sub_f7db74();
}
```

## `bl_MiniMap.<ResetOffset>d__81.get_Current` — RVA `0xcc8b20`

- Decompiled symbol: `bl_MiniMap_ResetOffset_d__81_get_Current`
- Metadata signature: `private object System.Collections.Generic.IEnumerator<System.Object>.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long bl_MiniMap_ResetOffset_d__81_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```

## `bl_MiniMap.<ResetOffset>d__81.Reset` — RVA `0xcc8b28`

- Decompiled symbol: `bl_MiniMap_ResetOffset_d__81_Reset`
- Metadata signature: `private void System.Collections.IEnumerator.Reset() { }`
- Native interval: `56` bytes
- Result: `pseudocode`

```c
extern long long g_1ef0bd8;
extern long long g_1f05510;

void bl_MiniMap_ResetOffset_d__81_Reset(void)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    long long v4;  // x0
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    v4 = sub_f7db70(sub_f7d940(&g_1ef0bd8));
    NotSupportedException__ctor(v4, 0);
    sub_f7da4c(v4, sub_f7d940(&g_1f05510));
}
```

## `bl_MiniMap.<ResetOffset>d__81.get_Current` — RVA `0xcc8b60`

- Decompiled symbol: `bl_MiniMap_ResetOffset_d__81_get_Current`
- Metadata signature: `private object System.Collections.IEnumerator.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long bl_MiniMap_ResetOffset_d__81_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```
