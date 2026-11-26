# Native pseudocode: PostEffectsHelper

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `PostEffectsHelper.OnRenderImage` — RVA `0xce6f38`

- Decompiled symbol: `PostEffectsHelper_OnRenderImage`
- Metadata signature: `private void OnRenderImage(RenderTexture source, RenderTexture destination) { }`
- Native interval: `104` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1eef458;
extern long long g_1f0cb48;
extern char g_1fab667;

void PostEffectsHelper_OnRenderImage(void)
{
    unsigned long long v3;  // x30
    unsigned long long v4;  // x20
    unsigned long long v5;  // x19
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x10]
    unsigned long long v2;  // [bp-0x8]

    v0 = v3;
    v1 = v4;
    v2 = v5;
    if (!(g_1fab667 & 1))
    {
        sub_f7d92c(&g_1eef458);
        sub_f7d92c(&g_1f0cb48);
        g_1fab667 = 1;
    }
    if (!g_1eef458->field_e0)
        sub_f7da5c(g_1eef458);
    Debug__Log();
    return;
}
```

## `PostEffectsHelper.DrawLowLevelPlaneAlignedWithCamera` — RVA `0xce6fa0`

- Decompiled symbol: `PostEffectsHelper_DrawLowLevelPlaneAlignedWithCamera`
- Metadata signature: `private static void DrawLowLevelPlaneAlignedWithCamera(float dist, RenderTexture source, RenderTexture dest, Material material, Camera cameraForProjectionMatrix) { }`
- Native interval: `576` bytes
- Result: `pseudocode`

```c
extern long long g_1f10630;
extern char g_1fab668;

int PostEffectsHelper_DrawLowLevelPlaneAlignedWithCamera(long long a0, long long a1, long long a2, long long a3)
{
    int i;  // w20
    char v0;  // [bp-0xe0]
    uint128_t v1;  // [bp-0xd0]
    uint128_t v2;  // [bp-0xc0]
    uint128_t v3;  // [bp-0xb0]
    char v4;  // [bp-0xa0]
    uint128_t v5;  // [bp-0x90]
    uint128_t v6;  // [bp-0x80]
    uint128_t v7;  // [bp-0x70]
    char v8;  // [bp-0x58]
    char v9;  // [bp-0x54]

    if (!(g_1fab668 & 1))
    {
        sub_f7d92c(&g_1f10630);
        g_1fab668 = 1;
    }
    RenderTexture__set_active(a1, 0);
    if (a2)
    {
        Material__SetTexture(a2, g_1f10630, a0, 0);
        GL__PushMatrix(0);
        GL__LoadIdentity(0);
        if (a3)
        {
            Camera__get_projectionMatrix(a3, 0);
            memcpy(&v0, &v4, 16);
            v1 = v5;
            v2 = v6;
            v3 = v7;
            GL__LoadProjectionMatrix(&v0, 0);
            Camera__get_fieldOfView(a3, 0);
            sincosf(&v9, &v8);
            Camera__get_aspect(a3, 0);
            if (Material__get_passCount(a2, 0) < 1)
                return GL__PopMatrix(0);
            i = 0;
            do
            {
                Material__SetPass(a2, i, 0);
                GL__Begin(7, 0);
                GL__TexCoord2(0);
                GL__Vertex3(0);
                GL__TexCoord2(0);
                GL__Vertex3(0);
                GL__TexCoord2(0);
                GL__Vertex3(0);
                GL__TexCoord2(0);
                GL__Vertex3(0);
                GL__End(0);
                i += 1;
            } while (i < Material__get_passCount(a2, 0));
            return GL__PopMatrix(0);
        }
    }
    sub_f7db74();
}
```

## `PostEffectsHelper.DrawBorder` — RVA `0xce71e0`

- Decompiled symbol: `PostEffectsHelper_DrawBorder`
- Metadata signature: `private static void DrawBorder(RenderTexture dest, Material material) { }`
- Native interval: `884` bytes
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

void PostEffectsHelper_DrawBorder(struct_0 **a0, long long a1, unsigned long a2)
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
    RenderTexture__set_active();
    GL__PushMatrix(0);
    GL__LoadOrtho(0);
    if (a1)
    {
        if (Material__get_passCount(a1, 0) >= 1)
        {
            flag = 0;
            Material__SetPass(a1, 0, 0);
            if (a0)
            {
                v19 = a0;
                v20 = *(a0)->field_180;
                *(a0)->field_178();
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

## `PostEffectsHelper.DrawLowLevelQuad` — RVA `0xce7554`

- Decompiled symbol: `PostEffectsHelper_DrawLowLevelQuad`
- Metadata signature: `private static void DrawLowLevelQuad(float x1, float x2, float y1, float y2, RenderTexture source, RenderTexture dest, Material material) { }`
- Native interval: `416` bytes
- Result: `pseudocode`

```c
extern long long g_1f10630;
extern char g_1fab669;

void PostEffectsHelper_DrawLowLevelQuad(long long a0, long long a1, long long a2)
{
    unsigned long long v10;  // d12
    unsigned long long v11;  // d11
    int i;  // w20
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
    if (!(g_1fab669 & 1))
    {
        sub_f7d92c(&g_1f10630);
        g_1fab669 = 1;
    }
    RenderTexture__set_active(a1, 0);
    if (a2)
    {
        Material__SetTexture(a2, g_1f10630, a0, 0);
        GL__PushMatrix(0);
        GL__LoadOrtho(0);
        if (Material__get_passCount(a2, 0) >= 1)
        {
            i = 0;
            do
            {
                Material__SetPass(a2, i, 0);
                GL__Begin(7, 0);
                GL__TexCoord2(0);
                GL__Vertex3(0);
                GL__TexCoord2(0);
                GL__Vertex3(0);
                GL__TexCoord2(0);
                GL__Vertex3(0);
                GL__TexCoord2(0);
                GL__Vertex3(0);
                GL__End(0);
                i += 1;
            } while (i < Material__get_passCount(a2, 0));
        }
        GL__PopMatrix();
        return;
    }
    sub_f7db74();
}
```

## `PostEffectsHelper.ctor` — RVA `0xce76f4`

- Decompiled symbol: `PostEffectsHelper_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long PostEffectsHelper_ctor(void)
{
    long long v0;  // x0

    v0 = MonoBehaviour__ctor();
    return MonoBehaviour__ctor();
}
```
