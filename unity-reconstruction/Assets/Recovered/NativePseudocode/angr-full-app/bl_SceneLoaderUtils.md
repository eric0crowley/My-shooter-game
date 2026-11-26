# Native pseudocode: bl_SceneLoaderUtils

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `bl_SceneLoaderUtils.get_GetLoader` — RVA `0xc7653c`

- Decompiled symbol: `bl_SceneLoaderUtils_get_GetLoader`
- Metadata signature: `public static bl_SceneLoader get_GetLoader() { }`
- Native interval: `196` bytes
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

extern struct_0 *g_1eef458;
extern struct_1 *g_1ef0c58;
extern long long g_1f00218;
extern long long g_1f09b70;
extern char g_1fab3a8;

long long bl_SceneLoaderUtils_get_GetLoader(void)
{
    long long v0;  // x0

    if (!(g_1fab3a8 & 1))
    {
        sub_f7d92c(&g_1eef458);
        sub_f7d92c(&g_1f00218);
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c(&g_1f09b70);
        g_1fab3a8 = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v0 = sub_1129dbc(g_1f00218);
    if (!((char)Object__op_Equality(v0, 0, 0) & 1))
        return v0;
    if (!g_1eef458->field_e0)
        sub_f7da5c(g_1eef458);
    Debug__LogWarning(g_1f09b70, 0);
    return v0;
}
```

## `bl_SceneLoaderUtils.GetSceneLoaderManager` — RVA `0xc76600`

- Decompiled symbol: `bl_SceneLoaderUtils_GetSceneLoaderManager`
- Metadata signature: `public static bl_SceneLoaderManager GetSceneLoaderManager() { }`
- Native interval: `356` bytes
- Result: `pseudocode`

```c
typedef struct struct_4 {
    char padding_0[200];
    unsigned long long field_c8;
    char padding_d0[96];
    char field_130;
} struct_4;

typedef struct struct_1 {
    char padding_0[224];
    unsigned int field_e0;
} struct_1;

typedef struct struct_3 {
    char padding_0[304];
    char field_130;
} struct_3;

typedef struct struct_2 {
    char padding_0[224];
    unsigned int field_e0;
} struct_2;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern long long g_1eebcd8;
extern struct_0 *g_1eef458;
extern struct_1 *g_1ef0c58;
extern struct_2 *g_1ef1f08;
extern struct_3 *g_1ef2b08;
extern long long g_1f0c820;
extern long long g_1f0d800;
extern char g_1fab3a9;

struct_4 ** bl_SceneLoaderUtils_GetSceneLoaderManager(void)
{
    long long v0;  // x0
    struct_4 **v1;  // x0
    unsigned long v2;  // x10
    struct_4 **v3;  // x19

    if (!(g_1fab3a9 & 1))
    {
        sub_f7d92c(&g_1eef458);
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c(&g_1ef1f08);
        sub_f7d92c(&g_1f0d800);
        sub_f7d92c(&g_1f0c820);
        sub_f7d92c(&g_1eebcd8);
        sub_f7d92c(&g_1ef2b08);
        g_1fab3a9 = 1;
    }
    if (!g_1ef1f08->field_e0)
        sub_f7da5c(g_1ef1f08);
    v0 = Type__GetTypeFromHandle(g_1eebcd8, 0);
    v1 = Resources__Load(g_1f0d800, v0, 0);
    if (!v1 || (v2 = (unsigned long)(unsigned long long)g_1ef2b08->field_130, (unsigned int)v2 > (unsigned int)*(v1)->field_130))
    {
        v3 = NULL;
    }
    else if (*((long long *)(*(v1)->field_c8 + v2 * 8 - 8)) == g_1ef2b08)
    {
        v3 = v1;
    }
    else
    {
        v3 = NULL;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (!((char)Object__op_Equality(v3, 0, 0) & 1))
        return v3;
    if (!g_1eef458->field_e0)
        sub_f7da5c(g_1eef458);
    Debug__LogWarning(g_1f0c820, 0);
    return v3;
}
```

## `bl_SceneLoaderUtils.LoadLevelAsync` — RVA `0xc76764`

- Decompiled symbol: `bl_SceneLoaderUtils_LoadLevelAsync`
- Metadata signature: `public static AsyncOperation LoadLevelAsync(int scene) { }`
- Native interval: `88` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef14f0;
extern char g_1fab3aa;

void bl_SceneLoaderUtils_LoadLevelAsync(unsigned long a0)
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
    if (!(g_1fab3aa & 1))
    {
        sub_f7d92c(&g_1ef14f0);
        g_1fab3aa = 1;
    }
    if (!g_1ef14f0->field_e0)
        sub_f7da5c(g_1ef14f0);
}
```

## `bl_SceneLoaderUtils.LoadLevelAsync` — RVA `0xc767bc`

- Decompiled symbol: `bl_SceneLoaderUtils_LoadLevelAsync`
- Metadata signature: `public static AsyncOperation LoadLevelAsync(string scene) { }`
- Native interval: `88` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef14f0;
extern char g_1fab3ab;

void bl_SceneLoaderUtils_LoadLevelAsync(unsigned long a0)
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
    if (!(g_1fab3ab & 1))
    {
        sub_f7d92c(&g_1ef14f0);
        g_1fab3ab = 1;
    }
    if (!g_1ef14f0->field_e0)
        sub_f7da5c(g_1ef14f0);
}
```
