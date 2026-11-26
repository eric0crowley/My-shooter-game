# Native pseudocode: PostEffectsBase

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `PostEffectsBase.CheckShaderAndCreateMaterial` — RVA `0xce619c`

- Decompiled symbol: `PostEffectsBase_CheckShaderAndCreateMaterial`
- Metadata signature: `protected Material CheckShaderAndCreateMaterial(Shader s, Material m2Create) { }`
- Native interval: `852` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    char padding_0[360];
    struct struct_3 *field_168;
    unsigned long long field_170;
} struct_2;

typedef struct struct_6 {
    struct struct_4 *field_0;
    char padding_8[26];
    char field_22;
} struct_6;

typedef struct struct_1 {
    char padding_0[24];
    unsigned int field_18;
    char padding_1c[4];
    long long field_20;
} struct_1;

typedef struct struct_3 {
    unsigned long long field_0;
} struct_3;

typedef struct struct_4 {
    char padding_0[360];
    struct struct_5 *field_168;
    unsigned long long field_170;
} struct_4;

typedef struct struct_5 {
    unsigned long long field_0;
} struct_5;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern long long g_1eef458;
extern struct_0 *g_1ef0c58;
extern long long g_1f06790;
extern long long g_1f067f8;
extern long long g_1f0c2e8;
extern long long g_1f0e888;
extern char g_1fab661;

long long PostEffectsBase_CheckShaderAndCreateMaterial(struct_6 *ptr, struct_2 **a1, long long a2)
{
    long long v0;  // x0
    long long v1;  // x19
    unsigned long v10;  // x1
    unsigned long v2;  // 4111
    long long v3;  // x0
    unsigned long long flag;  // x2
    struct_1 *v5;  // x0
    struct_1 *p;  // x22
    struct_2 **v7;  // x0
    unsigned long v8;  // x1
    struct_6 *v9;  // x0

    if (!(g_1fab661 & 1))
    {
        sub_f7d92c(&g_1eef458);
        sub_f7d92c("7F");
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c("I)");
        sub_f7d92c(&g_1f067f8);
        sub_f7d92c(&g_1f0c2e8);
        sub_f7d92c(&g_1f06790);
        sub_f7d92c(&g_1f0e888);
        g_1fab661 = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (!((char)Object__op_Implicit(a1, 0) & 1))
    {
        v9 = ptr;
        v10 = ptr->field_0->field_170;
        ptr->field_0->field_168();
    }
    if (a1)
    {
        if (((char)Shader__get_isSupported(a1, 0) & 1))
        {
            if (!g_1ef0c58->field_e0)
                sub_f7da5c(g_1ef0c58);
            if (((char)Object__op_Implicit(a2, 0) & 1))
            {
                if (a2)
                {
                    v0 = Material__get_shader(a2, 0);
                    if (!g_1ef0c58->field_e0)
                        sub_f7da5c(g_1ef0c58);
                    if (((char)Object__op_Equality(v0, a1, 0) & 1))
                        return a2;
                }
                else
                {
                    sub_f7db74();
                    sub_f7db7c(v5);
                }
            }
        }
        if (((char)Shader__get_isSupported(a1, 0) & 1))
        {
            v1 = sub_f7db70(g_1ef07c0);
            Material__ctor(v1, a1, 0);
            if (v1)
            {
                Object__set_hideFlags(v1, 52, 0);
                if (!g_1ef0c58->field_e0)
                    sub_f7da5c(g_1ef0c58);
                v2 = arm64g_calculate_condition(25, (unsigned long long)((int)Object__op_Implicit(v1, 0) & 1), 0, 0);
                if ((char)v2)
                    v3 = v1;
                else
                    v3 = 0;
                return v3;
            }
        }
        else
        {
            flag = 0;
            Behaviour__set_enabled(ptr, 0, 0);
            ptr->field_22 = 0;
            v5 = sub_f7d9d4(g_1eee378, 5);
            if (v5)
            {
                if (v5->field_18)
                {
                    p = v5;
                    p->field_20 = g_1f0e888;
                    sub_f7d8d0((struct struct_1 *)&p->field_20, g_1f0e888);
                    v7 = a1;
                    v8 = *(a1)->field_170;
                    *(a1)->field_168();
                }
                sub_f7db7c(v5);
            }
        }
    }
    v5 = sub_f7db74();
    sub_f7db7c(v5);
}
```

## `PostEffectsBase.NotSupported` — RVA `0xce64f0`

- Decompiled symbol: `PostEffectsBase_NotSupported`
- Metadata signature: `protected void NotSupported() { }`
- Native interval: `32` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[34];
    char field_22;
} struct_0;

void PostEffectsBase_NotSupported(struct_0 *ptr)
{
    Behaviour__set_enabled();
    ptr->field_22 = 0;
    return;
}
```

## `PostEffectsBase.CreateMaterial` — RVA `0xce6510`

- Decompiled symbol: `PostEffectsBase_CreateMaterial`
- Metadata signature: `protected Material CreateMaterial(Shader s, Material m2Create) { }`
- Native interval: `484` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[360];
    struct struct_2 *field_168;
    unsigned long long field_170;
} struct_1;

typedef struct struct_2 {
    unsigned long long field_0;
} struct_2;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern long long g_1eef458;
extern struct_0 *g_1ef0c58;
extern long long g_1f0c2e8;
extern char g_1fab662;

long long PostEffectsBase_CreateMaterial(struct_1 **a0, long long a1, long long a2)
{
    long long v0;  // x20
    long long v1;  // x0
    long long v2;  // x20
    unsigned long v3;  // 4111
    long long v4;  // x0
    struct_1 **v5;  // x0
    unsigned long v6;  // x1

    v0 = a2;
    if (!(g_1fab662 & 1))
    {
        sub_f7d92c(&g_1eef458);
        sub_f7d92c("7F");
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c(&g_1f0c2e8);
        g_1fab662 = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (!((char)Object__op_Implicit(a1, 0) & 1))
    {
        v5 = a0;
        v6 = *(a0)->field_170;
        *(a0)->field_168();
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (!((char)Object__op_Implicit(v0, 0) & 1))
    {
LABEL_10e6668:
        if (a1)
            goto LABEL_10e666c;
    }
    else if (v0)
    {
        v1 = Material__get_shader(v0, 0);
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        if (!(Object__op_Equality(v1, a1, 0) & 1))
            goto LABEL_10e6668;
        if (a1)
        {
            if (((char)Shader__get_isSupported(a1, 0) & 1))
            {
                return v0;
            }
LABEL_10e666c:
            if (!((char)Shader__get_isSupported(a1, 0) & 1))
                return 0;
            v2 = sub_f7db70(g_1ef07c0);
            Material__ctor(v2, a1, 0);
            if (v2)
            {
                Object__set_hideFlags(v2, 52, 0);
                if (!g_1ef0c58->field_e0)
                    sub_f7da5c(g_1ef0c58);
                v3 = arm64g_calculate_condition(25, (unsigned long long)((int)Object__op_Implicit(v2, 0) & 1), 0, 0);
                if ((char)v3)
                    v4 = v2;
                else
                    v4 = 0;
                return v4;
            }
        }
    }
    sub_f7db74();
}
```

## `PostEffectsBase.OnEnable` — RVA `0xce66f4`

- Decompiled symbol: `PostEffectsBase_OnEnable`
- Metadata signature: `private void OnEnable() { }`
- Native interval: `12` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[34];
    char field_22;
} struct_0;

struct_0 * PostEffectsBase_OnEnable(struct_0 *ptr)
{
    ptr->field_22 = 1;
    return ptr;
}
```

## `PostEffectsBase.CheckSupport` — RVA `0xce6700`

- Decompiled symbol: `PostEffectsBase_CheckSupport`
- Metadata signature: `protected bool CheckSupport() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long PostEffectsBase_CheckSupport(unsigned long a0)
{
    unsigned long long v0;  // x0

    v0 = PostEffectsBase__CheckSupport();
    return PostEffectsBase__CheckSupport();
}
```

## `PostEffectsBase.CheckSupport` — RVA `0xce6708`

- Decompiled symbol: `PostEffectsBase_CheckSupport`
- Metadata signature: `protected bool CheckSupport(bool needDepth) { }`
- Native interval: `248` bytes
- Result: `pseudocode`
- Heuristic layout hint: `PostEffectsBase_Recovered` matched 3 offsets against `PostEffectsBase` metadata (confidence 1.00).

```c
typedef struct PostEffectsBase_Recovered {
    char padding_0[32];
    char supportHDRTextures;
    char supportDX11;
    char isSupported;
} PostEffectsBase_Recovered;

extern long long g_1efcf30;
extern char g_1fab664;

unsigned int PostEffectsBase_CheckSupport(struct_0 *ptr, unsigned int a1)
{
    char v0;  // x0
    long long v1;  // x0

    if (!(g_1fab664 & 1))
    {
        sub_f7d92c(&g_1efcf30);
        g_1fab664 = 1;
    }
    ptr->field_22 = 1;
    ptr->field_20 = (char)SystemInfo__SupportsRenderTextureFormat(2, 0) & 1;
    if (50 > SystemInfo__get_graphicsShaderLevel(0))
        v0 = 0;
    else
        v0 = SystemInfo__get_supportsComputeShaders(0);
    ptr->field_21 = v0 & 1;
    if (!((char)SystemInfo__get_supportsImageEffects(0) & 1))
    {
        Behaviour__set_enabled(ptr, 0, 0);
        ptr->field_22 = 0;
        return 0;
    }
    if (!((char)a1 & 1))
        return 1;
    if (((char)SystemInfo__SupportsRenderTextureFormat(1, 0) & 1))
    {
        v1 = sub_1231bc8(ptr, g_1efcf30);
        if (!v1)
            sub_f7db74();
        Camera__set_depthTextureMode(v1, Camera__get_depthTextureMode() | 1, 0);
    }
    else
    {
        Behaviour__set_enabled(ptr, 0, 0);
        ptr->field_22 = 0;
        return 0;
    }
    return 1;
}
```

## `PostEffectsBase.CheckResources` — RVA `0xce6800`

- Decompiled symbol: `PostEffectsBase_CheckResources`
- Metadata signature: `public virtual bool CheckResources() { }`
- Native interval: `192` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[360];
    struct struct_1 *field_168;
    unsigned long long field_170;
} struct_0;

typedef struct struct_1 {
    unsigned long long field_0;
} struct_1;

extern long long g_1eef458;
extern long long g_1f06808;
extern long long g_1f092f0;
extern char g_1fab663;

void PostEffectsBase_CheckResources(struct_0 **a0)
{
    unsigned long long v6;  // x30
    unsigned long long v7;  // x23
    unsigned long long v8;  // x22
    unsigned long long v9;  // x21
    unsigned long long v10;  // x20
    unsigned long long v11;  // x19
    struct_0 **v12;  // x0
    unsigned long v13;  // x1
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
    if (!(g_1fab663 & 1))
    {
        sub_f7d92c(&g_1eef458);
        sub_f7d92c(&g_1f06808);
        sub_f7d92c(&g_1f092f0);
        g_1fab663 = 1;
    }
    v12 = a0;
    v13 = *(a0)->field_170;
    *(a0)->field_168();
}
```

## `PostEffectsBase.Start` — RVA `0xce68c0`

- Decompiled symbol: `PostEffectsBase_Start`
- Metadata signature: `protected void Start() { }`
- Native interval: `12` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[376];
    unsigned long long field_178;
} struct_0;

long long PostEffectsBase_Start(struct_0 **a0)
{
    goto *(a0)->field_178;
}
```

## `PostEffectsBase.CheckSupport` — RVA `0xce68cc`

- Decompiled symbol: `PostEffectsBase_CheckSupport`
- Metadata signature: `protected bool CheckSupport(bool needDepth, bool needHdr) { }`
- Native interval: `88` bytes
- Result: `pseudocode`

```c
unsigned int PostEffectsBase_CheckSupport(char *ptr, unsigned int a1, unsigned int a2)
{
    unsigned long long v0;  // x0

    v0 = PostEffectsBase__CheckSupport(ptr, a1 & 1);
    if (((char)v0 & 1) && ((char)a2 & 1))
    {
        if (ptr[32])
        {
            v0 = 1;
        }
        else
        {
            Behaviour__set_enabled(ptr, 0, 0);
            v0 = 0;
            ptr[34] = 0;
        }
    }
    return (unsigned int)v0 & 1;
}
```

## `PostEffectsBase.Dx11Support` — RVA `0xce6924`

- Decompiled symbol: `PostEffectsBase_Dx11Support`
- Metadata signature: `public bool Dx11Support() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[33];
    char field_21;
} struct_0;

long long PostEffectsBase_Dx11Support(struct_0 *a0)
{
    return a0->field_21;
}
```

## `PostEffectsBase.ReportAutoDisable` — RVA `0xce692c`

- Decompiled symbol: `PostEffectsBase_ReportAutoDisable`
- Metadata signature: `protected void ReportAutoDisable() { }`
- Native interval: `184` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[360];
    struct struct_1 *field_168;
    unsigned long long field_170;
} struct_0;

typedef struct struct_1 {
    unsigned long long field_0;
} struct_1;

extern long long g_1eef458;
extern long long g_1f06700;
extern long long g_1f0e5f8;
extern char g_1fab665;

void PostEffectsBase_ReportAutoDisable(struct_0 **a0)
{
    unsigned long long v6;  // x30
    unsigned long long v7;  // x23
    unsigned long long v8;  // x22
    unsigned long long v9;  // x21
    unsigned long long v10;  // x20
    unsigned long long v11;  // x19
    struct_0 **v12;  // x0
    unsigned long v13;  // x1
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
    if (!(g_1fab665 & 1))
    {
        sub_f7d92c(&g_1eef458);
        sub_f7d92c(&g_1f06700);
        sub_f7d92c(&g_1f0e5f8);
        g_1fab665 = 1;
    }
    v12 = a0;
    v13 = *(a0)->field_170;
    *(a0)->field_168();
}
```

## `PostEffectsBase.CheckShader` — RVA `0xce69e4`

- Decompiled symbol: `PostEffectsBase_CheckShader`
- Metadata signature: `private bool CheckShader(Shader s) { }`
- Native interval: `456` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned int field_18;
    char padding_1c[4];
    long long field_20;
} struct_0;

typedef struct struct_1 {
    char padding_0[360];
    struct struct_2 *field_168;
    unsigned long long field_170;
} struct_1;

typedef struct struct_2 {
    unsigned long long field_0;
} struct_2;

extern long long g_1eef458;
extern long long g_1f06788;
extern long long g_1f067f8;
extern long long g_1f0e888;
extern char g_1fab666;

void PostEffectsBase_CheckShader(unsigned long a0, struct_1 **a1, unsigned long a2)
{
    unsigned long long v5;  // x30
    unsigned long long v6;  // x22
    unsigned long long v7;  // x21
    unsigned long long v8;  // x20
    unsigned long long v9;  // x19
    struct_0 *v10;  // x0
    struct_0 *ptr;  // x0
    struct_1 **v12;  // x0
    unsigned long v13;  // x1
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
    if (!(g_1fab666 & 1))
    {
        sub_f7d92c(&g_1eef458);
        sub_f7d92c("I)");
        sub_f7d92c(&g_1f067f8);
        sub_f7d92c(&g_1f0e888);
        sub_f7d92c(&g_1f06788);
        g_1fab666 = 1;
    }
    v10 = sub_f7d9d4(g_1eee378, 5);
    if (v10)
    {
        if (v10->field_18)
        {
            ptr = v10;
            ptr->field_20 = g_1f0e888;
            sub_f7d8d0((struct struct_0 *)&ptr->field_20, g_1f0e888);
            if (a1)
            {
                v12 = a1;
                v13 = *(a1)->field_170;
                *(a1)->field_168();
            }
        }
        else
        {
            sub_f7db7c();
        }
    }
    sub_f7db74();
}
```

## `PostEffectsBase.DrawBorder` — RVA `0xce6bac`

- Decompiled symbol: `PostEffectsBase_DrawBorder`
- Metadata signature: `protected void DrawBorder(RenderTexture dest, Material material) { }`
- Native interval: `888` bytes
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

void PostEffectsBase_DrawBorder(unsigned long a0, struct_0 **a1, long long a2)
{
    unsigned long long v9;  // d11
    unsigned long long v10;  // d10
    struct_0 **v19;  // x0
    unsigned long v20;  // x1
    unsigned long long v11;  // d9
    unsigned long long v12;  // d8
    unsigned long long v13;  // x30
    unsigned long long v14;  // x22
    unsigned long long v15;  // x21
    unsigned long long v16;  // x20
    unsigned long long v17;  // x19
    unsigned long long flag;  // x2
    unsigned long long v0;  // [bp-0x50]
    unsigned long long v1;  // [bp-0x48]
    unsigned long long v2;  // [bp-0x40]
    unsigned long long v3;  // [bp-0x38]
    unsigned long long v4;  // [bp-0x30]
    unsigned long long v5;  // [bp-0x20]
    unsigned long long v6;  // [bp-0x18]
    unsigned long long v7;  // [bp-0x10]
    unsigned long long v8;  // [bp-0x8]

    v0 = v9;
    v1 = v10;
    v2 = v11;
    v3 = v12;
    v4 = v13;
    v5 = v14;
    v6 = v15;
    v7 = v16;
    v8 = v17;
    RenderTexture__set_active(a1, 0);
    GL__PushMatrix(0);
    GL__LoadOrtho(0);
    if (a2)
    {
        if (Material__get_passCount(a2, 0) >= 1)
        {
            flag = 0;
            Material__SetPass(a2, 0, 0);
            if (a1)
            {
                v19 = a1;
                v20 = *(a1)->field_180;
                *(a1)->field_178();
            }
        }
        else
        {
            GL__PopMatrix();
            return;
        }
    }
    sub_f7db74();
}
```

## `PostEffectsBase.ctor` — RVA `0xce6f24`

- Decompiled symbol: `PostEffectsBase_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `20` bytes
- Result: `pseudocode`

```c
long long PostEffectsBase_ctor(char *ptr)
{
    long long v0;  // x0

    ptr[32] = 1;
    ptr[34] = 1;
    v0 = MonoBehaviour__ctor();
    return MonoBehaviour__ctor();
}
```
