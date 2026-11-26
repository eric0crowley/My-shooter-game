# Native pseudocode: bl_MiniMapUtils

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `bl_MiniMapUtils.GetMiniMap` — RVA `0xcc6020`

- Decompiled symbol: `bl_MiniMapUtils_GetMiniMap`
- Metadata signature: `public static bl_MiniMap GetMiniMap(int id = 0) { }`
- Native interval: `140` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[24];
    unsigned int field_18;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern long long g_1f00228;
extern char g_1fab57c;

long long bl_MiniMapUtils_GetMiniMap(unsigned int a0)
{
    struct_1 *v0;  // x0

    if (!(g_1fab57c & 1))
    {
        sub_f7d92c(&g_1f00228);
        sub_f7d92c(&g_1ef0c58);
        g_1fab57c = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v0 = sub_1129ea4(g_1f00228);
    if (!v0)
    {
        v0 = sub_f7db74();
    }
    else if (v0->field_18 > a0)
    {
        return *((long long *)&v0[1].padding_0[4 + 8 * a0]);
    }
    sub_f7db7c(v0);
}
```

## `bl_MiniMapUtils.CalculateMiniMapPosition` — RVA `0xcc791c`

- Decompiled symbol: `bl_MiniMapUtils_CalculateMiniMapPosition`
- Metadata signature: `public static Vector3 CalculateMiniMapPosition(Vector3 viewPoint, RectTransform maxAnchor) { }`
- Native interval: `144` bytes
- Result: `pseudocode`

```c
long long bl_MiniMapUtils_CalculateMiniMapPosition(long long a0)
{
    unsigned long long v0;  // x0

    if (a0)
    {
        RectTransform__get_sizeDelta();
        RectTransform__get_sizeDelta(a0, 0);
        RectTransform__get_sizeDelta(a0, 0);
        v0 = RectTransform__get_sizeDelta(a0, 0);
        return RectTransform__get_sizeDelta(a0, 0);
    }
    sub_f7db74();
}
```
