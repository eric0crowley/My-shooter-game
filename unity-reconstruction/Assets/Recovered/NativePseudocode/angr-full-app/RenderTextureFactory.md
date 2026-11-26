# Native pseudocode: RenderTextureFactory

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `RenderTextureFactory.ctor` — RVA `0xcdf6b8`

- Decompiled symbol: `RenderTextureFactory_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `136` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    long long field_10;
} struct_0;

extern long long g_1ef6df8;
extern char g_1fab62c;

void RenderTextureFactory_ctor(struct_0 *ptr)
{
    unsigned long long v5;  // x30
    unsigned long long v6;  // x22
    unsigned long long v7;  // x21
    unsigned long long v8;  // x20
    unsigned long long v9;  // x19
    long long v10;  // x0
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
    if (!(g_1fab62c & 1))
    {
        sub_f7d92c(&g_1ef6df8);
        sub_f7d92c("]~");
        g_1fab62c = 1;
    }
    Object__ctor(ptr, 0);
    v10 = sub_f7db70(g_1eed180);
    sub_13d4e24(v10, g_1ef6df8);
    ptr->field_10 = v10;
    sub_f7d8d0();
    return;
}
```

## `RenderTextureFactory.Get` — RVA `0xcdf740`

- Decompiled symbol: `RenderTextureFactory_Get`
- Metadata signature: `public RenderTexture Get(RenderTexture baseRenderTexture) { }`
- Native interval: `280` bytes
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

extern long long g_1f0a290;
extern char g_1fab62d;

void RenderTextureFactory_Get(unsigned long a0, struct_0 **a1, unsigned long a2, unsigned long a3, unsigned long a4, unsigned long a5, unsigned long a6, unsigned long a7)
{
    unsigned long long v9;  // x30
    unsigned long long v10;  // x26
    unsigned long v19;  // x1
    unsigned long long v11;  // x25
    unsigned long long v12;  // x24
    unsigned long long v13;  // x23
    unsigned long long v14;  // x22
    unsigned long long v15;  // x21
    unsigned long long v16;  // x20
    unsigned long long v17;  // x19
    struct_0 **v18;  // x0
    unsigned long long v0;  // [bp-0x50]
    unsigned long long v1;  // [bp-0x40]
    unsigned long long v2;  // [bp-0x38]
    unsigned long long v3;  // [bp-0x30]
    unsigned long long v4;  // [bp-0x28]
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
    if (!(g_1fab62d & 1))
    {
        sub_f7d92c(&g_1f0a290);
        g_1fab62d = 1;
    }
    if (!a1)
        sub_f7db74();
    v18 = a1;
    v19 = *(a1)->field_180;
    *(a1)->field_178();
}
```

## `RenderTextureFactory.Get` — RVA `0xcdf858`

- Decompiled symbol: `RenderTextureFactory_Get`
- Metadata signature: `public RenderTexture Get(int width, int height, int depthBuffer = 0, RenderTextureFormat format = 2, RenderTextureReadWrite rw = 0, FilterMode filterMode = 1, TextureWrapMode wrapMode = 1, string name = "FactoryTempTexture") { }`
- Native interval: `228` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    long long field_10;
} struct_0;

extern long long g_1ef6e00;
extern char g_1fab62e;

long long RenderTextureFactory_Get(struct_0 *a0, unsigned int a1, unsigned int a2, unsigned int a3, unsigned int a4, unsigned int a5, unsigned long a6, unsigned int a7)
{
    long long v1;  // x0
    long long v2;  // x22
    long long v0;  // [bp+0x0]

    if (!(g_1fab62e & 1))
    {
        sub_f7d92c(&g_1ef6e00);
        g_1fab62e = 1;
    }
    v1 = RenderTexture__GetTemporary(a1, a2, a3, a4, a5, 0);
    if (v1)
    {
        v2 = v1;
        Texture__set_filterMode();
        Texture__set_wrapMode(v2, a7, 0);
        Object__set_name(v2, v0, 0);
        if (a0->field_10)
        {
            sub_13d6008(a0->field_10, v2, g_1ef6e00);
            return v2;
        }
    }
    sub_f7db74();
}
```

## `RenderTextureFactory.Release` — RVA `0xcdf93c`

- Decompiled symbol: `RenderTextureFactory_Release`
- Metadata signature: `public void Release(RenderTexture rt) { }`
- Native interval: `308` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[16];
    unsigned long long field_10;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern long long g_1eee8a8;
extern struct_0 *g_1ef0c58;
extern long long g_1ef6e10;
extern long long g_1ef6e20;
extern long long g_1f00b68;
extern long long g_1f088c0;
extern char g_1fab62f;

long long RenderTextureFactory_Release(struct_1 *ptr, long long a1)
{
    long long v0;  // x0
    unsigned long long v1;  // x0
    unsigned long long v2;  // x0
    long long v3;  // x0
    long long v4;  // x0

    if (!(g_1fab62f & 1))
    {
        sub_f7d92c(&g_1ef6e10);
        sub_f7d92c(&g_1ef6e20);
        sub_f7d92c(&g_1ef0c58);
        g_1fab62f = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v0 = Object__op_Equality(a1, 0, 0);
    if (((char)v0 & 1))
        return v0;
    v1 = ptr->field_10;
    if (v1)
    {
        if (!(sub_13d5518(v1, a1, g_1ef6e10) & 1))
            goto LABEL_10dfa1c;
        v1 = ptr->field_10;
        if (v1)
        {
            sub_13d56e4(v1, a1, g_1ef6e20);
            v2 = RenderTexture__ReleaseTemporary();
            return RenderTexture__ReleaseTemporary();
        }
    }
    sub_f7db74(v1);
LABEL_10dfa1c:
    v3 = String__Format(sub_f7d940(&g_1f088c0), a1, 0);
    v4 = sub_f7db70(sub_f7d940(&g_1eee8a8));
    ArgumentException__ctor(v4, v3, 0);
    sub_f7da4c(v4, sub_f7d940(&g_1f00b68));
}
```

## `RenderTextureFactory.ReleaseAll` — RVA `0xcdfa70`

- Decompiled symbol: `RenderTextureFactory_ReleaseAll`
- Metadata signature: `public void ReleaseAll() { }`
- Native interval: `204` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned long long field_10;
} struct_0;

extern long long g_1ef6338;
extern long long g_1ef6340;
extern long long g_1ef6e08;
extern long long g_1ef6e18;
extern char g_1fab630;

long long RenderTextureFactory_ReleaseAll(struct_0 *ptr)
{
    unsigned long long v3;  // x0
    unsigned long long v4;  // x0
    unsigned long flag;  // [bp-0x38]
    unsigned long long choice;  // [bp-0x30]
    long long flag2;  // [bp-0x28]

    if (!(g_1fab630 & 1))
    {
        sub_f7d92c(&g_1ef6338);
        sub_f7d92c(&g_1ef6340);
        sub_f7d92c(&g_1ef6e08);
        sub_f7d92c(&g_1ef6e18);
        g_1fab630 = 1;
    }
    flag = 0;
    choice = 0;
    flag2 = 0;
    v3 = ptr->field_10;
    if (v3)
    {
        sub_13d598c(v3, g_1ef6e18);
        while (((char)sub_130e518(&flag, g_1ef6338) & 1))
        {
            RenderTexture__ReleaseTemporary(flag2, 0);
        }
        v3 = ptr->field_10;
        if (v3)
        {
            v4 = sub_13d54b8(v3, g_1ef6e08);
            return sub_13d54b8(v3, g_1ef6e08);
        }
    }
    sub_f7db74(v3);
}
```

## `RenderTextureFactory.Dispose` — RVA `0xcdfb3c`

- Decompiled symbol: `RenderTextureFactory_Dispose`
- Metadata signature: `public void Dispose() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned long long field_10;
} struct_0;

long long RenderTextureFactory_Dispose(struct_0 *a0)
{
    long long v0;  // x0

    v0 = RenderTextureFactory__ReleaseAll(a0);
    return RenderTextureFactory__ReleaseAll(a0);
}
```
