# Native pseudocode: GraphicsUtils

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `GraphicsUtils.get_isLinearColorSpace` — RVA `0xcdec1c`

- Decompiled symbol: `GraphicsUtils_get_isLinearColorSpace`
- Metadata signature: `public static bool get_isLinearColorSpace() { }`
- Native interval: `28` bytes
- Result: `pseudocode`

```c
unsigned long long GraphicsUtils_get_isLinearColorSpace(void)
{
    unsigned long long v1;  // x30
    unsigned long long v0;  // [bp-0x10]

    v0 = v1;
    if (QualitySettings__get_activeColorSpace(0) == 1)
        return 1;
    return 0;
}
```

## `GraphicsUtils.get_supportsDX11` — RVA `0xcdec38`

- Decompiled symbol: `GraphicsUtils_get_supportsDX11`
- Metadata signature: `public static bool get_supportsDX11() { }`
- Native interval: `44` bytes
- Result: `pseudocode`

```c
unsigned int GraphicsUtils_get_supportsDX11(void)
{
    if (50 <= SystemInfo__get_graphicsShaderLevel(0))
        return SystemInfo__get_supportsComputeShaders();
    return 0;
}
```

## `GraphicsUtils.get_whiteTexture` — RVA `0xcdec64`

- Decompiled symbol: `GraphicsUtils_get_whiteTexture`
- Metadata signature: `public static Texture2D get_whiteTexture() { }`
- Native interval: `300` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    char padding_0[224];
    unsigned int field_e0;
} struct_2;

extern struct_2 *g_1ef0c58;
extern long long g_1ef1cc0;
extern char g_1fab624;

long long GraphicsUtils_get_whiteTexture(void)
{
    long long v0;  // x19
    long long v1;  // x0

    if (!(g_1fab624 & 1))
    {
        sub_f7d92c("w=");
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c(&g_1ef1cc0);
        g_1fab624 = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (!((char)Object__op_Inequality(g_1eefbd0->field_b8->field_0, 0, 0) & 1))
    {
        v0 = sub_f7db70(g_1ef1cc0);
        Texture2D__ctor(v0, 1, 1, 5, 0, 0);
        g_1eefbd0->field_b8->field_0 = v0;
        sub_f7d8d0(g_1eefbd0->field_b8, v0);
        v1 = g_1eefbd0->field_b8->field_0;
        if (!v1 || !((Texture2D__SetPixel(v1, 0, 0, 0), v1 = g_1eefbd0->field_b8->field_0, v1)))
            sub_f7db74(v1);
        Texture2D__Apply(v1, 0);
    }
    return g_1eefbd0->field_b8->field_0;
}
```

## `GraphicsUtils.get_quad` — RVA `0xcded90`

- Decompiled symbol: `GraphicsUtils_get_quad`
- Metadata signature: `public static Mesh get_quad() { }`
- Native interval: `624` bytes
- Result: `pseudocode`

```c
typedef struct struct_3 {
    char padding_0[24];
    unsigned int field_18;
    char padding_1c[4];
    unsigned long long field_20;
    unsigned int field_28;
    unsigned long long field_2c;
    unsigned int field_34;
    unsigned long long field_38;
    unsigned int field_40;
    unsigned long long field_44;
    unsigned int field_4c;
} struct_3;

typedef struct struct_4 {
    char padding_0[24];
    unsigned int field_18;
    char padding_1c[4];
    unsigned long long field_20;
    unsigned long long field_28;
    unsigned long long field_30;
    unsigned long long field_38;
} struct_4;

typedef struct struct_0 {
    char padding_0[8];
    long long field_8;
} struct_0;

typedef struct struct_2 {
    char padding_0[224];
    unsigned int field_e0;
} struct_2;

extern long long g_1eee408;
extern long long g_1eee410;
extern long long g_1ef0868;
extern struct_2 *g_1ef0c58;
extern long long g_1f05648;
extern char g_1fab625;

long long GraphicsUtils_get_quad(void)
{
    struct_3 *addr;  // x0
    unsigned int flag;  // w8
    struct_3 *ptr;  // x19
    struct_4 *ptr3;  // x0
    unsigned int choice;  // w8
    struct_4 *p;  // x20
    long long v6;  // x0
    long long v7;  // x22
    struct_0 *ptr4;  // x0

    if (!(g_1fab625 & 1))
    {
        sub_f7d92c("w=");
        sub_f7d92c("a(");
        sub_f7d92c(&g_1ef0868);
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c(&g_1f05648);
        sub_f7d92c(&g_1eee408);
        sub_f7d92c(&g_1eee410);
        g_1fab625 = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (((char)Object__op_Inequality(g_1eefbd0->field_b8->field_8, 0, 0) & 1))
        return g_1eefbd0->field_b8->field_8;
    addr = sub_f7d9d4(g_1eee410, 4);
    if (addr)
    {
        flag = addr->field_18;
        ptr = addr;
        if (flag && !((ptr->field_20 = 0xbf800000bf800000, ptr->field_28 = 0, flag == 1 || (*((unsigned long long *)&(&ptr->field_28)[1]) = 0x3f8000003f800000, *((unsigned int *)((char *)&ptr->field_2c + 4)) = 0, flag <= 2 || (*((unsigned int *)&ptr->field_38) = 0, *((unsigned long long *)&ptr->field_34) = 0xbf8000003f800000, flag == 3)))))
        {
            (&ptr->field_40)[1] = 0;
            *((unsigned long long *)((char *)&ptr->field_38 + 4)) = 0x3f800000bf800000;
            ptr3 = sub_f7d9d4(g_1eee408, 4);
            if (ptr3)
            {
                choice = ptr3->field_18;
                p = ptr3;
                if (!choice || (p->field_20 = 0, choice == 1 || (p->field_28 = 0x3f8000003f800000, choice <= 2 || (p->field_30 = 0x3f800000, choice == 3))))
                    goto LABEL_10deff8;
                p->field_38 = 0x3f80000000000000;
                v6 = sub_f7d9d4(g_1eee1f8, 6);
                RuntimeHelpers__InitializeArray(v6, g_1f05648, 0);
                v7 = sub_f7db70(g_1ef0868);
                Mesh__ctor(v7, 0);
                if (v7)
                {
                    Mesh__set_vertices(v7, ptr, 0);
                    Mesh__set_uv(v7, p, 0);
                    Mesh__set_triangles(v7, v6, 0);
                    ptr4 = g_1eefbd0->field_b8;
                    ptr4->field_8 = v7;
                    sub_f7d8d0((struct struct_0 *)&ptr4->field_8, v7);
                    if (g_1eefbd0->field_b8->field_8)
                    {
                        Mesh__RecalculateNormals(g_1eefbd0->field_b8->field_8, 0);
                        if (g_1eefbd0->field_b8->field_8)
                        {
                            Mesh__RecalculateBounds(g_1eefbd0->field_b8->field_8, 0);
                            return g_1eefbd0->field_b8->field_8;
                        }
                    }
                }
            }
        }
        else
        {
LABEL_10deff8:
            sub_f7db7c();
        }
    }
    sub_f7db74();
}
```

## `GraphicsUtils.Blit` — RVA `0xcdf000`

- Decompiled symbol: `GraphicsUtils_Blit`
- Metadata signature: `public static void Blit(Material material, int pass) { }`
- Native interval: `252` bytes
- Result: `pseudocode`

```c
void GraphicsUtils_Blit(long long a0, unsigned int a1, unsigned long a2, unsigned long a3, unsigned long a4)
{
    unsigned long long v4;  // d8
    unsigned long long v5;  // x30
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
    GL__PushMatrix(0);
    GL__LoadOrtho(0);
    if (a0)
    {
        Material__SetPass(a0, a1, 0);
        GL__Begin(5, 0);
        GL__TexCoord2(0);
        GL__Vertex3(0);
        GL__TexCoord2(0);
        GL__Vertex3(0);
        GL__TexCoord2(0);
        GL__Vertex3(0);
        GL__TexCoord2(0);
        GL__Vertex3(0);
        GL__End(0);
        GL__PopMatrix();
        return;
    }
    sub_f7db74();
}
```

## `GraphicsUtils.ClearAndBlit` — RVA `0xcdf0fc`

- Decompiled symbol: `GraphicsUtils_ClearAndBlit`
- Metadata signature: `public static void ClearAndBlit(Texture source, RenderTexture destination, Material material, int pass, bool clearColor = true, bool clearDepth = false) { }`
- Native interval: `408` bytes
- Result: `pseudocode`

```c
extern long long g_1f10630;
extern char g_1fab626;

void GraphicsUtils_ClearAndBlit(long long a0, long long a1, long long a2, unsigned int a3, unsigned int a4)
{
    unsigned long long v8;  // d8
    unsigned long long v9;  // x30
    unsigned long long v10;  // x24
    unsigned long long v11;  // x23
    unsigned long long v12;  // x22
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
    if (!(g_1fab626 & 1))
    {
        sub_f7d92c(&g_1f10630);
        g_1fab626 = 1;
    }
    RenderTexture__get_active(0);
    RenderTexture__set_active(a1, 0);
    GL__Clear(0, a4 & 1, 0);
    GL__PushMatrix(0);
    GL__LoadOrtho(0);
    if (a2)
    {
        Material__SetTexture(a2, g_1f10630, a0, 0);
        Material__SetPass(a2, a3, 0);
        GL__Begin(5, 0);
        GL__TexCoord2(0);
        GL__Vertex3(0);
        GL__TexCoord2(0);
        GL__Vertex3(0);
        GL__TexCoord2(0);
        GL__Vertex3(0);
        GL__TexCoord2(0);
        GL__Vertex3(0);
        GL__End(0);
        GL__PopMatrix(0);
        RenderTexture__set_active();
        return;
    }
    sub_f7db74();
}
```

## `GraphicsUtils.Destroy` — RVA `0xcdf294`

- Decompiled symbol: `GraphicsUtils_Destroy`
- Metadata signature: `public static void Destroy(Object obj) { }`
- Native interval: `136` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab627;

long long GraphicsUtils_Destroy(long long a0)
{
    long long v0;  // x0
    unsigned long long v1;  // x0

    if (!(g_1fab627 & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab627 = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v0 = Object__op_Inequality(a0, 0, 0);
    if (!((char)v0 & 1))
        return v0;
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v1 = Object__Destroy();
    return Object__Destroy();
}
```

## `GraphicsUtils.Dispose` — RVA `0xcdf31c`

- Decompiled symbol: `GraphicsUtils_Dispose`
- Metadata signature: `public static void Dispose() { }`
- Native interval: `72` bytes
- Result: `pseudocode`

```c
extern char g_1fab628;

long long GraphicsUtils_Dispose(void)
{
    long long v0;  // x0

    if (!(g_1fab628 & 1))
    {
        sub_f7d92c("w=");
        g_1fab628 = 1;
    }
    v0 = GraphicsUtils__Destroy(g_1eefbd0->field_b8->field_8);
    return GraphicsUtils__Destroy(g_1eefbd0->field_b8->field_8);
}
```
