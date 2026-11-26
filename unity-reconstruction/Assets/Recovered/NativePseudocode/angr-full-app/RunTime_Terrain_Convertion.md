# Native pseudocode: RunTime_Terrain_Convertion

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `RunTime_Terrain_Convertion.Start` — RVA `0xccb7a8`

- Decompiled symbol: `RunTime_Terrain_Convertion_Start`
- Metadata signature: `private void Start() { }`
- Native interval: `1100` bytes
- Result: `pseudocode`
- Heuristic layout hint: `RunTime_Terrain_Convertion_Recovered` matched 4 offsets against `RunTime_Terrain_Convertion` metadata (confidence 1.00).

```c
typedef struct struct_3 {
    char padding_0[24];
    int field_18;
    char padding_1c[4];
    long long field_20;
} struct_3;

typedef struct RunTime_Terrain_Convertion_Recovered {
    char padding_0[32];
    long long sourceTerrain;
    long long convertInfo;
    char generateBasemap;
    char attachMeshCollider;
} RunTime_Terrain_Convertion_Recovered;

typedef struct struct_1 {
    char padding_0[224];
    unsigned int field_e0;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern long long g_1eefaf0;
extern struct_0 *g_1ef0c58;
extern struct_1 *g_1ef1bb0;
extern long long g_1ef22e8;
extern long long g_1efeac8;
extern long long g_1efead0;
extern long long g_1efead8;
extern long long g_1efec48;
extern long long g_1efec50;
extern char g_1fab2c9;
extern char g_1fab58b;

struct_3 * RunTime_Terrain_Convertion_Start(struct_2 *a0)
{
    struct_3 *v2;  // x0
    struct_3 *v3;  // x0
    unsigned long v12;  // 4102
    unsigned long long v13;  // x25
    struct_3 *v14;  // x26
    long long v15;  // x0
    long long v16;  // x0
    long long v17;  // x23
    long long v18;  // x24
    long long v19;  // x0
    long long v20;  // x24
    unsigned long v21;  // x0
    struct_3 *ptr;  // x21
    unsigned long v22;  // x24
    struct_3 *v23;  // x0
    long long v24;  // x23
    struct_3 *v5;  // x0
    unsigned int flag;  // w8
    long long v7;  // x22
    long long v8;  // x21
    struct_3 *v9;  // x0
    long long v10;  // x0
    unsigned long long v11;  // x0
    char *v0;  // [bp-0x60]
    char v1;  // [bp+0x0]

    v0 = &v1;
    if (!(g_1fab58b & 1))
    {
        sub_f7d92c(&g_1efeac8);
        sub_f7d92c(&g_1efead0);
        sub_f7d92c(&g_1efead8);
        sub_f7d92c(&g_1efec48);
        sub_f7d92c(&g_1efec50);
        sub_f7d92c(&g_1eefaf0);
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c(&g_1ef1bb0);
        g_1fab58b = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v2 = Object__op_Inequality(a0->field_20, 0, 0);
    if (!((char)v2 & 1))
        return v2;
    if (!g_1ef1bb0->field_e0)
        sub_f7da5c(g_1ef1bb0);
    v3 = TerrainToMeshConverter__Convert(a0->field_20, a0->field_28, 0, 0, 0);
    if (!v3)
        return v3;
    ptr = v3;
    if (a0->field_30)
        v5 = RunTime_Terrain_Convertion__GenerateMaterial_Basemap(a0);
    else
        v5 = RunTime_Terrain_Convertion__GenerateMaterial_Splatmap(a0);
    flag = ptr->field_18;
    if (flag != 1)
    {
        v12 = arm64g_calculate_condition(179, (unsigned long long)flag, 1, 0);
        if ((char)v12)
            return v5;
        v13 = 0;
        v14 = &ptr->field_20;
        while (flag > (unsigned int)v13)
        {
            if (!*((long long *)&v14->padding_0[8 * v13]))
                goto LABEL_10cbbec;
            v15 = Object__get_name(*((long long *)&v14->padding_0[8 * v13]), 0);
            v16 = sub_f7db70(g_1eefaf0);
            v17 = v16;
            GameObject__ctor(v16, v15, 0);
            if (!v17 || (v18 = (long long)(unsigned long long)GameObject__get_transform(v17, 0), !Component__get_gameObject(a0, 0) || (v19 = (long long)(unsigned long long)GameObject__get_transform(), !v18)))
                goto LABEL_10cbbec;
            Transform__set_parent(v18, v19, 0);
            v20 = GameObject__get_transform(v17, 0);
            if (!g_1fab2c9)
            {
                sub_f7d92c(&g_1ef22e8);
                g_1fab2c9 = 1;
            }
            if (!v20)
                goto LABEL_10cbbec;
            Transform__set_localPosition(v20, 0);
            v21 = sub_124913c(v17, g_1efead0);
            if (ptr->field_18 <= (unsigned int)v13)
                break;
            v22 = v21;
            if (!v21 || !((MeshFilter__set_sharedMesh(v22, *((long long *)&v14->padding_0[8 * v13]), 0), sub_124913c(v17, g_1efead8))))
                goto LABEL_10cbbec;
            v23 = Renderer__set_sharedMaterial();
            if (a0->field_31)
            {
                v24 = sub_124913c(v17, g_1efeac8);
                if (!v24)
                    goto LABEL_10cbbec;
                v23 = MeshCollider__set_sharedMesh(v24, MeshFilter__get_sharedMesh(v22, 0), 0);
            }
            if ((unsigned int)v13 + 1 >= ptr->field_18)
                return v23;
        }
        goto LABEL_10cbbf0;
    }
    else if (Component__get_gameObject(a0, 0))
    {
        v7 = sub_1249224();
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        if (!((char)Object__op_Equality(v7, 0, 0) & 1))
        {
LABEL_10cb940:
            if (!ptr->field_18)
                sub_f7db7c();
            if (v7 && !((MeshFilter__set_sharedMesh(v7, ptr->field_20, 0), !Component__get_gameObject(a0, 0))))
            {
                v8 = sub_1249224();
                if (!g_1ef0c58->field_e0)
                    sub_f7da5c(g_1ef0c58);
                if (((char)Object__op_Equality(v8, 0, 0) & 1))
                {
                    if (Component__get_gameObject(a0, 0))
                    {
                        v8 = sub_124913c();
                        goto LABEL_10cb9cc;
                    }
                }
                else
                {
LABEL_10cb9cc:
                    if (v8)
                    {
                        v9 = Renderer__set_sharedMaterial(v8, v5, 0);
                        if (!a0->field_31)
                            return v9;
                        if (Component__get_gameObject(a0, 0))
                        {
                            v10 = sub_124913c();
                            MeshFilter__get_sharedMesh(v7, 0);
                            if (v10)
                            {
                                v11 = MeshCollider__set_sharedMesh();
                                return MeshCollider__set_sharedMesh();
                            }
                        }
                    }
                }
            }
        }
        else if (Component__get_gameObject(a0, 0))
        {
            v7 = sub_124913c();
            goto LABEL_10cb940;
        }
    }
LABEL_10cbbec:
    sub_f7db74();
LABEL_10cbbf0:
    sub_f7db7c();
}
```

## `RunTime_Terrain_Convertion.GenerateMaterial_Basemap` — RVA `0xccbbf4`

- Decompiled symbol: `RunTime_Terrain_Convertion_GenerateMaterial_Basemap`
- Metadata signature: `private Material GenerateMaterial_Basemap() { }`
- Native interval: `444` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

typedef struct struct_1 {
    char padding_0[224];
    unsigned int field_e0;
} struct_1;

extern struct_0 *g_1ef0c58;
extern struct_1 *g_1ef1bb0;
extern long long g_1f0bcc0;
extern long long g_1f0bcc8;
extern char g_1fab58c;

long long RunTime_Terrain_Convertion_GenerateMaterial_Basemap(unsigned long a0)
{
    unsigned int flag2;  // w0
    unsigned long v3;  // 4112
    long long v4;  // x0
    long long v5;  // x0
    long long v6;  // x19
    long long choice;  // [bp-0x48]
    long long flag;  // [bp-0x38]

    if (!(g_1fab58c & 1))
    {
        sub_f7d92c("7F");
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c(&g_1ef1bb0);
        sub_f7d92c("9(");
        sub_f7d92c(&g_1f0bcc8);
        sub_f7d92c(&g_1f0bcc0);
        g_1fab58c = 1;
    }
    flag = 0;
    choice = 0;
    flag2 = QualitySettings__get_activeColorSpace(0);
    if (!g_1ef1bb0->field_e0)
        sub_f7da5c(g_1ef1bb0);
    TerrainToMeshConverter__ExtractBasemap();
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v3 = arm64g_calculate_condition(25, (unsigned long long)((int)Object__op_Inequality(choice, 0, 0) & 1), 0, 0);
    v4 = Shader__Find();
    v5 = sub_f7db70(g_1ef07c0);
    v6 = v5;
    Material__ctor(v5, v4, 0);
    if (v6)
    {
        Material__set_mainTexture(v6, flag, 0);
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        if (!((char)Object__op_Inequality(choice, 0, 0) & 1))
            return v6;
        Material__SetTexture(v6, g_1f102d0, choice, 0);
        return v6;
    }
    sub_f7db74();
}
```

## `RunTime_Terrain_Convertion.GenerateMaterial_Splatmap` — RVA `0xccbdb0`

- Decompiled symbol: `RunTime_Terrain_Convertion_GenerateMaterial_Splatmap`
- Metadata signature: `private Material GenerateMaterial_Splatmap() { }`
- Native interval: `1796` bytes
- Result: `pseudocode`

```c
typedef struct struct_3 {
    char padding_0[24];
    unsigned int field_18;
} struct_3;

typedef struct struct_4 {
    char padding_0[24];
    unsigned int field_18;
    char padding_1c[4];
    long long field_20;
} struct_4;

typedef struct struct_5 {
    char padding_0[24];
    unsigned int field_18;
} struct_5;

typedef struct struct_6 {
    char padding_0[24];
    unsigned int field_18;
} struct_6;

typedef struct struct_7 {
    char padding_0[24];
    unsigned int field_18;
} struct_7;

typedef struct struct_8 {
    char padding_0[24];
    unsigned int field_18;
} struct_8;

typedef struct struct_9 {
    char padding_0[32];
    long long field_20;
} struct_9;

typedef struct struct_2 {
    char padding_0[224];
    unsigned int field_e0;
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
extern long long g_1ef0450;
extern struct_1 *g_1ef0c58;
extern struct_2 *g_1ef1bb0;
extern long long g_1f07668;
extern long long g_1f09ab8;
extern long long g_1f0bcc8;
extern long long g_1f0d9f0;
extern long long g_1f0e178;
extern long long g_1f0f818;
extern long long g_1f10a08;
extern long long g_1f10a38;
extern long long g_1f10a40;
extern long long g_1f10a48;
extern long long g_1f10a50;
extern long long g_1f10a58;
extern char g_1fab58d;

long long RunTime_Terrain_Convertion_GenerateMaterial_Splatmap(struct_9 *a0)
{
    void* v13;  // x0
    void* ptr;  // x20
    unsigned int v23;  // w9
    unsigned long v24;  // 4117
    long long *v25;  // x27
    long long v26;  // x0
    long long v27;  // x21
    long long v28;  // x0
    long long v29;  // x0
    long long v30;  // x0
    long long v31;  // x19
    unsigned int flag7;  // w8
    unsigned int flag6;  // w0
    long long *v33;  // x9
    void* v34;  // x8
    long long v35;  // x0
    long long v36;  // x0
    unsigned long v37;  // x29
    unsigned long v38;  // x28
    long long v39;  // x0
    struct_4 *v40;  // x8
    long long v41;  // x0
    long long v42;  // x0
    long long v16;  // x20
    long long v43;  // x0
    long long v44;  // x0
    long long v17;  // x19
    unsigned long v18;  // x0
    struct_4 *v19;  // x8
    unsigned int v20;  // w8
    unsigned int v21;  // w24
    unsigned int v22;  // w8
    unsigned int v0;  // [bp-0xa4]
    unsigned int v1;  // [bp-0xa0]
    unsigned int v2;  // [bp-0x9c]
    unsigned int v3;  // [bp-0x98]
    unsigned int v4;  // [bp-0x94]
    struct_7 *flag4;  // [bp-0x90]
    struct_8 *flag5;  // [bp-0x88]
    struct_5 *flag2;  // [bp-0x80]
    struct_6 *flag3;  // [bp-0x78]
    struct_3 *flag;  // [bp-0x70]
    struct_4 *choice;  // [bp-0x68]
    char *v11;  // [bp-0x60]
    char v12;  // [bp+0x0]

    v11 = &v12;
    if (!(g_1fab58d & 1))
    {
        sub_f7d92c(&g_1eef458);
        sub_f7d92c(&g_1ef0450);
        sub_f7d92c("7F");
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c(&g_1ef1bb0);
        sub_f7d92c(&g_1f10a58);
        sub_f7d92c(&g_1f10a38);
        sub_f7d92c(&g_1f0e178);
        sub_f7d92c(&g_1f09ab8);
        sub_f7d92c(&g_1f07668);
        sub_f7d92c("I\n");
        sub_f7d92c(&g_1f10a48);
        sub_f7d92c("?=");
        sub_f7d92c(&g_1f0d9f0);
        sub_f7d92c(&g_1f10a08);
        sub_f7d92c(&g_1f10a40);
        sub_f7d92c("\t*");
        sub_f7d92c(&g_1f0f818);
        sub_f7d92c(&g_1f0bcc8);
        sub_f7d92c(&g_1f10a50);
        g_1fab58d = 1;
    }
    flag = NULL;
    choice = NULL;
    flag2 = NULL;
    flag3 = NULL;
    flag4 = NULL;
    flag5 = NULL;
    v4 = 0;
    if (!g_1ef1bb0->field_e0)
        sub_f7da5c(g_1ef1bb0);
    v13 = TerrainToMeshConverter__ExtractSplatmaps(a0->field_20, 0);
    if (!v13)
        return 0;
    ptr = v13;
    if (!(long long)v13[24])
        return 0;
    if (!g_1ef1bb0->field_e0)
        sub_f7da5c(g_1ef1bb0);
    flag6 = TerrainToMeshConverter__ExtractTexturesInfo(a0->field_20, &choice, &flag, &flag3, &flag2, &flag5, &flag4, 0);
    if (flag6 && choice)
    {
        if (flag6 == 1)
        {
            v16 = Shader__Find(g_1f0bcc8, 0);
            if (!g_1ef0c58->field_e0)
                sub_f7da5c(g_1ef0c58);
            if (!((char)Object__op_Inequality(v16, 0, 0) & 1))
                return 0;
            v17 = sub_f7db70(g_1ef07c0);
            v18 = Material__ctor(v17, v16, 0);
            v19 = choice;
            if (v19)
            {
                if (!v19->field_18)
                {
                    sub_f7db7c(v18);
                }
                else if (v17)
                {
                    v18 = Material__set_mainTexture(v17, v19->field_20, 0);
                    if (flag3)
                    {
                        if (flag3->field_18)
                        {
                            v18 = Material__set_mainTextureScale(v17, 0);
                            if (flag2)
                            {
                                if (flag2->field_18)
                                {
                                    Material__set_mainTextureOffset(v17, 0);
                                    return v17;
                                }
                                sub_f7db7c(v18);
                            }
                        }
                        else
                        {
                            sub_f7db7c(v18);
                        }
                    }
                }
            }
        }
        else
        {
            if (flag6 < 8)
                v20 = flag6;
            else
                v20 = 8;
            if (2 < v20)
                v21 = v20;
            else
                v21 = 2;
            if (!flag)
                v22 = 0;
            else
                v22 = 1;
            if (5 <= v21)
                v23 = 0;
            else
                v23 = 1;
            v24 = arm64g_calculate_condition(25, (unsigned long long)(v23 & v22), 0, 0);
            if ((char)v24)
                v25 = "I\n";
            else
                v25 = &g_1f09ab8;
            v26 = String__Concat();
            v3 = v21;
            v27 = Shader__Find(String__Format(v26, sub_f7da64(g_1ef0450, &v3), 0), 0, 0);
            if (!g_1ef0c58->field_e0)
                sub_f7da5c(g_1ef0c58);
            if (((char)Object__op_Equality(v27, 0, 0) & 1))
            {
                v28 = String__Concat(g_1f0f818, *(v25), g_1f07668, 0);
                v3 = v21;
                v29 = String__Format(v28, sub_f7da64(g_1ef0450, &v3), 0);
                v30 = String__Concat(g_1f0d9f0, v29, 0);
                if (!g_1eef458->field_e0)
                    sub_f7da5c(g_1eef458);
                Debug__LogWarning(v30, 0);
                return 0;
            }
            v31 = sub_f7db70(g_1ef07c0);
            v18 = Material__ctor(v31, v27, 0);
            flag7 = (long long)ptr[24];
            if (flag7 != 1)
            {
                if (flag7 >= 3)
                {
                    v4 = flag7;
                    v35 = Int32__ToString(&v4, 0);
                    v36 = String__Concat(g_1f0e178, v35, 0);
                    if (!g_1eef458->field_e0)
                        sub_f7da5c(g_1eef458);
                    v18 = Debug__Log(v36, 0);
                    flag7 = (long long)ptr[24];
                }
                if (!flag7)
                    sub_f7db7c(v18);
                if (v31)
                {
                    v18 = Material__SetTexture(v31, g_1f10a08, (long long)ptr[32], 0);
                    if ((int)ptr[24] <= 1)
                        sub_f7db7c(v18);
                    v33 = "\t*";
                    v34 = ptr + 40;
LABEL_10cc2bc:
                    Material__SetTexture(v31, *(v33), *((long long *)v34), 0);
                    v37 = 0;
                    while (true)
                    {
                        v38 = v37 + 1;
                        v3 = v38;
                        v39 = sub_f7da64(g_1ef0450, &v3);
                        v18 = String__Format(g_1f10a38, v39, 0);
                        v40 = choice;
                        if (!v40)
                            break;
                        if (v40->field_18 <= v37)
                            sub_f7db7c(v18);
                        Material__SetTexture(v31, v18, (&v40->field_20)[v37], 0);
                        v2 = v38;
                        v41 = sub_f7da64(g_1ef0450, &v2);
                        v18 = String__Format(g_1f10a58, v41, 0);
                        if (!flag3)
                            break;
                        if (flag3->field_18 <= v37)
                            sub_f7db7c(v18);
                        Material__SetFloat(v31, v18, 0);
                        v1 = v38;
                        v42 = sub_f7da64(g_1ef0450, &v1);
                        v18 = String__Format(g_1f10a48, v42, 0);
                        if (!flag5)
                            break;
                        if (flag5->field_18 <= v37)
                            sub_f7db7c(v18);
                        Material__SetFloat(v31, v18, 0);
                        v0 = v38;
                        v43 = sub_f7da64(g_1ef0450, &v0);
                        v18 = String__Format(g_1f10a40, v43, 0);
                        if (!flag4)
                            break;
                        if (flag4->field_18 <= v37)
                            sub_f7db7c(v18);
                        Material__SetFloat(v31, v18, 0);
                        if ((v23 & v22 & 1))
                        {
                            v3 = v38;
                            v44 = sub_f7da64(g_1ef0450, &v3);
                            v18 = String__Format(g_1f10a50, v44, 0);
                            if (!flag)
                                break;
                            if (flag->field_18 <= v37)
                                sub_f7db7c(v18);
                            Material__SetTexture(v31, v18, *((long long *)&flag[1].padding_0[4 + 8 * v37]), 0);
                        }
                        v37 = v38;
                        if (v21 == v38)
                            return v31;
                    }
                }
            }
            else if (v31)
            {
                v33 = &g_1f10a08;
                v34 = ptr + 32;
                goto LABEL_10cc2bc;
            }
        }
        sub_f7db7c(sub_f7db74());
    }
    if (!g_1eef458->field_e0)
        sub_f7da5c(g_1eef458);
    Debug__LogWarning(g_1f156e8, 0);
    return 0;
}
```

## `RunTime_Terrain_Convertion.ctor` — RVA `0xccc4b4`

- Decompiled symbol: `RunTime_Terrain_Convertion_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long RunTime_Terrain_Convertion_ctor(void)
{
    long long v0;  // x0

    v0 = MonoBehaviour__ctor();
    return MonoBehaviour__ctor();
}
```
