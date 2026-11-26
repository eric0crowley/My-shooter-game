# Native pseudocode: SunShafts

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `SunShafts.CheckResources` — RVA `0xce76fc`

- Decompiled symbol: `SunShafts_CheckResources`
- Metadata signature: `public override bool CheckResources() { }`
- Native interval: `140` bytes
- Result: `pseudocode`
- Heuristic layout hint: `SunShafts_Recovered` matched 5 offsets against `SunShafts` metadata (confidence 0.83).

```c
typedef struct SunShafts_Recovered {
    char padding_0[34];
    char field_22;
    char padding_23[69];
    char useDepthTexture;
    char padding_69[7];
    struct struct_2 **sunShaftsShader;
    long long sunShaftsMaterial;
    struct struct_2 **simpleClearShader;
    long long simpleClearMaterial;
} SunShafts_Recovered;

unsigned int SunShafts_CheckResources(struct_0 *a0)
{
    struct_0 *v0;  // x20
    struct_0 *ptr;  // x20
    long long v2;  // x0
    struct_0 *v3;  // x20
    struct_0 *p;  // x20
    long long v5;  // x0

    PostEffectsBase__CheckSupport(a0, a0->field_68);
    v0 = a0;
    ptr = &v0->field_78;
    v2 = PostEffectsBase__CheckShaderAndCreateMaterial(a0, a0->field_70, v0->field_78);
    *((long long *)&ptr->padding_0[0]) = v2;
    sub_f7d8d0(ptr, v2);
    v3 = a0;
    p = &v3->field_88;
    v5 = PostEffectsBase__CheckShaderAndCreateMaterial(a0, a0->field_80, v3->field_88);
    *((long long *)&p->padding_0[0]) = v5;
    sub_f7d8d0(p, v5);
    if (!a0->field_22)
        PostEffectsBase__ReportAutoDisable(a0); /* do not return */
    return 1;
}
```

## `SunShafts.Start` — RVA `0xce7788`

- Decompiled symbol: `SunShafts_Start`
- Metadata signature: `private void Start() { }`
- Native interval: `512` bytes
- Result: `pseudocode`

```c
typedef struct struct_3 {
    char padding_0[24];
    int field_18;
    char padding_1c[4];
    long long field_20;
} struct_3;

typedef struct struct_2 {
    char padding_0[48];
    long long field_30;
} struct_2;

typedef struct struct_1 {
    char padding_0[224];
    unsigned int field_e0;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern long long g_1eeb668;
extern long long g_1eee238;
extern struct_0 *g_1ef0c58;
extern struct_1 *g_1ef1f08;
extern char g_1fab66a;

struct_3 * SunShafts_Start(struct_2 *p, unsigned long a1, unsigned long a2)
{
    struct_3 *v0;  // x0
    long long v1;  // x0
    long long v10;  // x0
    long long v2;  // x0
    struct_3 *addr;  // x0
    unsigned int i;  // w8
    struct_3 *ptr;  // x20
    unsigned int v6;  // w23
    struct_3 *v7;  // x24
    struct_3 *v8;  // x24
    long long v9;  // x0

    if (!(g_1fab66a & 1))
    {
        sub_f7d92c(&g_1eee238);
        sub_f7d92c(&g_1eeb668);
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c(&g_1ef1f08);
        g_1fab66a = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v0 = Object__op_Implicit(p->field_30, 0);
    if (((char)v0 & 1))
        return v0;
    if (!g_1ef1f08->field_e0)
        sub_f7da5c(g_1ef1f08);
    v1 = Type__GetTypeFromHandle(g_1eeb668, 0);
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v2 = Object__FindObjectsOfType(v1, 0);
    addr = sub_f7da60(v2, g_1eee238);
    if (addr)
    {
        i = addr->field_18;
        ptr = addr;
        if (addr->field_18 < 1)
            return addr;
        v6 = 0;
        while (i > v6)
        {
            v7 = &ptr->padding_0[8 * v6];
            v8 = &v7->field_20;
            if (!v7->field_20)
                goto LABEL_10e7980;
            addr = Light__get_type(v7->field_20, 0);
            if ((unsigned int)addr == 1)
            {
                if (ptr->field_18 <= v6)
                    break;
                if (!*((long long *)&v8->padding_0[0]) || !Component__get_gameObject(*((long long *)&v8->padding_0[0]), 0))
                    goto LABEL_10e7980;
                addr = GameObject__get_activeInHierarchy();
                if (((char)addr & 1))
                {
                    if (ptr->field_18 <= v6)
                        break;
                    if (!*((long long *)&v8->padding_0[0]))
                        goto LABEL_10e7980;
                    v9 = Light__get_cookie(*((long long *)&v8->padding_0[0]), 0);
                    if (!g_1ef0c58->field_e0)
                        sub_f7da5c(g_1ef0c58);
                    addr = Object__op_Equality(v9, 0, 0);
                    if (((char)addr & 1))
                    {
                        if (ptr->field_18 <= v6)
                            break;
                        if (*((long long *)&v8->padding_0[0]))
                        {
                            p->field_30 = Component__get_transform(*((long long *)&v8->padding_0[0]), 0);
                            v10 = sub_f7d8d0();
                            return sub_f7d8d0();
                        }
                        goto LABEL_10e7980;
                    }
                }
            }
            if (v6 + 1 >= ptr->field_18)
                return addr;
        }
        goto LABEL_10e7984;
    }
LABEL_10e7980:
    addr = sub_f7db74();
LABEL_10e7984:
    sub_f7db7c(addr);
}
```

## `SunShafts.OnRenderImage` — RVA `0xce7988`

- Decompiled symbol: `SunShafts_OnRenderImage`
- Metadata signature: `private void OnRenderImage(RenderTexture source, RenderTexture destination) { }`
- Native interval: `1764` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[376];
    struct struct_1 *field_178;
    unsigned long long field_180;
} struct_0;

typedef struct struct_1 {
    unsigned long long field_0;
} struct_1;

extern long long g_1ef0c58;
extern long long g_1efcf30;
extern long long g_1f10878;
extern long long g_1f108e0;
extern long long g_1f108e8;
extern long long g_1f108f0;
extern char g_1fab66b;

void SunShafts_OnRenderImage(struct_0 **a0, unsigned long a1, unsigned long a2)
{
    unsigned long long v18;  // d12
    unsigned long long v19;  // d11
    unsigned long long v28;  // x24
    unsigned long long v29;  // x23
    unsigned long long v30;  // x22
    unsigned long long v31;  // x21
    unsigned long long v32;  // x20
    unsigned long long v33;  // x19
    struct_0 **v34;  // x0
    unsigned long v35;  // x1
    unsigned long long v20;  // d10
    unsigned long long v21;  // d9
    unsigned long long v22;  // d8
    unsigned long long v23;  // x30
    unsigned long long v24;  // x28
    unsigned long long v25;  // x27
    unsigned long long v26;  // x26
    unsigned long long v27;  // x25
    unsigned long long v0;  // [bp-0x90]
    unsigned long long v1;  // [bp-0x80]
    unsigned long long v2;  // [bp-0x78]
    unsigned long long v3;  // [bp-0x70]
    unsigned long long v4;  // [bp-0x68]
    char *v5;  // [bp-0x60]
    unsigned long long v6;  // [bp-0x58]
    unsigned long long v7;  // [bp-0x50]
    unsigned long long v8;  // [bp-0x48]
    unsigned long long v9;  // [bp-0x40]
    unsigned long long v10;  // [bp-0x38]
    unsigned long long v11;  // [bp-0x30]
    unsigned long long v12;  // [bp-0x28]
    unsigned long long v13;  // [bp-0x20]
    unsigned long long v14;  // [bp-0x18]
    unsigned long long v15;  // [bp-0x10]
    unsigned long long v16;  // [bp-0x8]
    char v17;  // [bp+0x0]

    v0 = v18;
    v1 = v19;
    v2 = v20;
    v3 = v21;
    v4 = v22;
    v5 = &v17;
    v6 = v23;
    v7 = v24;
    v8 = v25;
    v9 = v26;
    v10 = v27;
    v11 = v28;
    v12 = v29;
    v13 = v30;
    v14 = v31;
    v15 = v32;
    v16 = v33;
    if (!(g_1fab66b & 1))
    {
        sub_f7d92c(&g_1efcf30);
        sub_f7d92c("g=");
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c(&g_1f10878);
        sub_f7d92c("Y(");
        sub_f7d92c(&g_1f108e0);
        sub_f7d92c(&g_1f108f0);
        sub_f7d92c(&g_1f108e8);
        sub_f7d92c("5(");
        g_1fab66b = 1;
    }
    v34 = a0;
    v35 = *(a0)->field_180;
    *(a0)->field_178();
}
```

## `SunShafts.ctor` — RVA `0xce806c`

- Decompiled symbol: `SunShafts_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `76` bytes
- Result: `pseudocode`
- Heuristic layout hint: `SunShafts_Recovered` matched 7 offsets against `SunShafts` metadata (confidence 0.78).

```c
typedef struct SunShafts_Recovered {
    char padding_0[32];
    char field_20;
    char padding_21[1];
    char field_22;
    char padding_23[1];
    unsigned int resolution;
    char padding_28[16];
    unsigned int radialBlurIterations;
    uint128_t sunColor;
    uint128_t sunThreshold;
    unsigned long long sunShaftBlurRadius;
    unsigned int maxRadius;
    char useDepthTexture;
} SunShafts_Recovered;

long long SunShafts_ctor(struct_0 *ptr)
{
    long long v0;  // x0

    *((unsigned long long *)&(&ptr->field_38)[1]) = 0x3f8000003f800000 CONCAT 0x3f8000003f800000;
    ptr->field_38 = 2;
    *((uint128_t *)((char *)&ptr->field_3c + 12)) = 84405977751886136296787914036996913234;
    ptr->field_24 = 1;
    *((unsigned int *)((char *)&ptr->field_5c + 4)) = 0x3f400000;
    *((char *)&ptr->field_64) = 1;
    ptr->field_20 = 1;
    *((unsigned long long *)((char *)&ptr->field_4c + 12)) = 0x3f93333340200000;
    ptr->field_22 = 1;
    v0 = MonoBehaviour__ctor();
    return MonoBehaviour__ctor();
}
```
