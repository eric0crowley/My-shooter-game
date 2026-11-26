# Native pseudocode: MobileColorGrading

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `MobileColorGrading.ctor` — RVA `0xc7bce0`

- Decompiled symbol: `MobileColorGrading_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `32` bytes
- Result: `pseudocode`
- Heuristic layout hint: `MobileColorGrading_Recovered` matched 2 offsets against `MobileColorGrading` metadata (confidence 1.00).

```c
typedef struct MobileColorGrading_Recovered {
    char padding_0[56];
    unsigned long long Exposure;
    char padding_40[4];
    unsigned int Gamma;
} MobileColorGrading_Recovered;

long long MobileColorGrading_ctor(struct_0 *ptr)
{
    long long v0;  // x0

    ptr->field_38 = 4580701253525936538;
    ptr->field_44 = 1053609165;
    v0 = MonoBehaviour__ctor();
    return MonoBehaviour__ctor();
}
```

## `MobileColorGrading.OnEnable` — RVA `0xc7c4dc`

- Decompiled symbol: `MobileColorGrading_OnEnable`
- Metadata signature: `private void OnEnable() { }`
- Native interval: `376` bytes
- Result: `pseudocode`
- Heuristic layout hint: `MobileColorGrading_Recovered` matched 2 offsets against `MobileColorGrading` metadata (confidence 1.00).

```c
typedef struct MobileColorGrading_Recovered {
    char padding_0[40];
    struct struct_4 *colorMaterial;
    long long shader;
} MobileColorGrading_Recovered;

typedef struct struct_5 {
    char padding_0[200];
    unsigned long long field_c8;
    char padding_d0[96];
    char field_130;
} struct_5;

typedef struct struct_2 {
    char padding_0[200];
    unsigned long long field_c8;
    char padding_d0[96];
    char field_130;
} struct_2;

typedef struct struct_4 {
    struct struct_2 *field_0;
} struct_4;

typedef struct struct_1 {
    char padding_0[224];
    unsigned int field_e0;
} struct_1;

extern struct_1 *g_1ef0c58;
extern long long g_1f093d0;
extern long long g_1f0aa10;
extern char g_1fab3ec;

long long MobileColorGrading_OnEnable(struct_3 *p)
{
    struct_3 *ptr;  // x20
    long long v1;  // x0
    long long v2;  // x0
    struct_5 **v3;  // x0
    unsigned long v4;  // x9
    struct_5 **v5;  // x10

    if (!(g_1fab3ec & 1))
    {
        sub_f7d92c("7F");
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c(&g_1f0aa10);
        sub_f7d92c(&g_1f093d0);
        g_1fab3ec = 1;
    }
    ptr = &p->field_28;
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v1 = Object__op_Equality(p->field_28, 0, 0);
    if (!((char)v1 & 1))
        return v1;
    v2 = Shader__Find(g_1f0aa10, 0);
    p->field_30 = v2;
    sub_f7d8d0((struct MobileColorGrading_Recovered *)&p->field_30, v2);
    v3 = Resources__Load(g_1f093d0, 0);
    if (v3)
    {
        v4 = g_1ef07c0->field_130;
        if ((unsigned int)v4 > *(v3)->field_130)
        {
            v5 = NULL;
        }
        else if (*((long long *)(*(v3)->field_c8 + v4 * 8 - 8)) == g_1ef07c0)
        {
            v5 = v3;
        }
        else
        {
            v5 = NULL;
        }
        *((struct_5 ***)&ptr->padding_0[0]) = v5;
    }
    else
    {
        *((struct_2 ***)&ptr->padding_0[0]) = NULL;
    }
    sub_f7d8d0(ptr);
    if (!*((long long *)&ptr->padding_0[0]))
        sub_f7db74(0);
}
```

## `MobileColorGrading.Start` — RVA `0xc7c654`

- Decompiled symbol: `MobileColorGrading_Start`
- Metadata signature: `private void Start() { }`
- Native interval: `300` bytes
- Result: `pseudocode`
- Heuristic layout hint: `MobileColorGrading_Recovered` matched 2 offsets against `MobileColorGrading` metadata (confidence 1.00).

```c
typedef struct MobileColorGrading_Recovered {
    char padding_0[40];
    struct struct_3 *colorMaterial;
    long long shader;
} MobileColorGrading_Recovered;

typedef struct struct_4 {
    char padding_0[200];
    unsigned long long field_c8;
    char padding_d0[96];
    char field_130;
} struct_4;

typedef struct struct_1 {
    char padding_0[200];
    unsigned long long field_c8;
    char padding_d0[96];
    char field_130;
} struct_1;

typedef struct struct_3 {
    struct struct_1 *field_0;
} struct_3;

extern long long g_1f093d0;
extern long long g_1f0aa10;
extern char g_1fab3ed;

void MobileColorGrading_Start(struct_2 *ptr, unsigned long a1, unsigned long a2)
{
    unsigned long long v5;  // x30
    unsigned long long v6;  // x22
    unsigned long long v7;  // x21
    unsigned long long v8;  // x20
    unsigned long long v9;  // x19
    long long v10;  // x0
    struct_4 **v11;  // x0
    unsigned long v12;  // x9
    struct_4 **v13;  // x10
    struct_2 *v14;  // x19
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
    if (!(g_1fab3ed & 1))
    {
        sub_f7d92c("7F");
        sub_f7d92c(&g_1f0aa10);
        sub_f7d92c(&g_1f093d0);
        g_1fab3ed = 1;
    }
    v10 = Shader__Find(g_1f0aa10, 0);
    ptr->field_30 = v10;
    sub_f7d8d0((struct MobileColorGrading_Recovered *)&ptr->field_30, v10);
    v11 = Resources__Load(g_1f093d0, 0);
    if (v11)
    {
        v12 = g_1ef07c0->field_130;
        if ((unsigned int)v12 > *(v11)->field_130)
        {
            v13 = NULL;
        }
        else if (*((long long *)(*(v11)->field_c8 + v12 * 8 - 8)) == g_1ef07c0)
        {
            v13 = v11;
        }
        else
        {
            v13 = NULL;
        }
        ptr->field_28 = v13;
        v14 = &ptr->field_28;
    }
    else
    {
        ptr->field_28 = NULL;
        v14 = &ptr->field_28;
    }
    sub_f7d8d0(v14);
    if (!*((long long *)&v14->padding_0[0]))
        sub_f7db74(0);
}
```

## `MobileColorGrading.OnRenderImage` — RVA `0xc7c780`

- Decompiled symbol: `MobileColorGrading_OnRenderImage`
- Metadata signature: `private void OnRenderImage(RenderTexture source, RenderTexture destination) { }`
- Native interval: `832` bytes
- Result: `pseudocode`
- Heuristic layout hint: `MobileColorGrading_Recovered` matched 4 offsets against `MobileColorGrading` metadata (confidence 1.00).

```c
typedef struct MobileColorGrading_Recovered {
    char padding_0[32];
    unsigned int toneMapping;
    char padding_24[4];
    unsigned long long colorMaterial;
    char padding_30[16];
    unsigned int Saturation;
    char padding_44[4];
    unsigned int vignetteIntensity;
} MobileColorGrading_Recovered;

extern long long g_1f08288;
extern long long g_1f08290;
extern long long g_1f0d7d8;
extern long long g_1f0d7e0;
extern long long g_1f0fa08;
extern long long g_1f10430;
extern long long g_1f104c0;
extern long long g_1f10808;
extern char g_1fab3ee;

void MobileColorGrading_OnRenderImage(struct_1 *ptr, unsigned long a1, unsigned long a2)
{
    unsigned long long v5;  // x30
    unsigned long long v6;  // x22
    unsigned int flag;  // w8
    unsigned long long v7;  // x21
    unsigned long long v8;  // x20
    unsigned long long v9;  // x19
    unsigned long long v10;  // x0
    unsigned int v11;  // s0
    unsigned long v12;  // 4129
    unsigned int v13;  // s0
    unsigned long long v14;  // 4103
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
    if (!(g_1fab3ee & 1))
    {
        sub_f7d92c("g=");
        sub_f7d92c(&g_1f0fa08);
        sub_f7d92c(&g_1f08288);
        sub_f7d92c("W(");
        sub_f7d92c(&g_1f08290);
        sub_f7d92c(&g_1f0d7d8);
        sub_f7d92c(&g_1f0d7e0);
        sub_f7d92c(")*");
        sub_f7d92c("\t&");
        sub_f7d92c("a(");
        sub_f7d92c(&g_1f10808);
        sub_f7d92c(&g_1f104c0);
        sub_f7d92c(&g_1f10430);
        g_1fab3ee = 1;
    }
    v10 = ptr->field_28;
    if (v10 && (Material__SetVector(v10, g_1f10348, 0), v10 = ptr->field_28, v10 && (Material__SetFloat(v10, g_1f10370, 0), v10 = ptr->field_28, v10 && (Material__SetFloat(v10, g_1f104c0, 0), v10 = ptr->field_28, v10 && (Material__SetFloat(v10, g_1f10430, 0), v10 = ptr->field_28, v10 && (Material__SetFloat(v10, g_1f10a90, 0), v10 = ptr->field_28, v10 && (Material__SetFloat(v10, g_1f10808, 0), v10 = ptr->field_28, v10)))))))
    {
        v11 = ptr->field_40;
        v12 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v11, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v11, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v11, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v11, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v11, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v11, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if (!((char)v12))
        {
            Material__DisableKeyword();
            v10 = ptr->field_28;
        }
        else
        {
            Material__DisableKeyword();
            v10 = ptr->field_28;
            if (v10 && (Material__EnableKeyword(), v10 = ptr->field_28, v10))
            {
                v13 = ptr->field_48;
                v14 = (((CmpF(v13, 0.0) >> 5 & 3 | CmpF(v13, 0.0) & 1) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - ((CmpF(v13, 0.0) >> 5 & 3 | CmpF(v13, 0.0) & 1) & (CmpF(v13, 0.0) >> 5 & 3 | CmpF(v13, 0.0) & 1) >> 1 & 1);
                if ((char)(v14 * 0x10000000 >> 30))
                {
                    Material__DisableKeyword();
                    v10 = ptr->field_28;
                    if (v10)
                        goto LABEL_107c9f0;
                }
                else
                {
                    Material__DisableKeyword();
                    v10 = ptr->field_28;
                    if (v10)
                    {
LABEL_107c9f0:
                        Material__EnableKeyword();
                        flag = ptr->field_20;
                        if (!ptr->field_20)
                        {
                            v10 = ptr->field_28;
                            if (v10 && (Material__DisableKeyword(v10, g_1f08288, 0), v10 = ptr->field_28, v10))
                            {
                                Material__EnableKeyword(v10, g_1f08290, 0);
                                flag = ptr->field_20;
                                goto LABEL_107ca40;
                            }
                        }
                        else
                        {
LABEL_107ca40:
                            if (flag == 1)
                            {
                                v10 = ptr->field_28;
                                if (v10 && (Material__DisableKeyword(v10, g_1f08290, 0), v10 = ptr->field_28, v10))
                                {
                                    Material__EnableKeyword(v10, g_1f08288, 0);
                                    goto LABEL_107ca80;
                                }
                            }
                            else
                            {
LABEL_107ca80:
                                if (!g_1eefbb8->field_e0)
                                    sub_f7da5c(g_1eefbb8);
                                Graphics__Blit();
                                return;
                            }
                        }
                    }
                }
            }
        }
    }
    sub_f7db74(v10);
}
```
