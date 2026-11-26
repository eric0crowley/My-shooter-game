# Native pseudocode: MarkerGroup

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `MarkerGroup.get_MarkerGroupRect` — RVA `0xc7b124`

- Decompiled symbol: `MarkerGroup_get_MarkerGroupRect`
- Metadata signature: `public RectTransform get_MarkerGroupRect() { }`
- Native interval: `164` bytes
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
extern long long g_1efd060;
extern char g_1fab3d9;

long long MarkerGroup_get_MarkerGroupRect(struct_1 *ptr)
{
    long long v0;  // x0

    if (!(g_1fab3d9 & 1))
    {
        sub_f7d92c(&g_1efd060);
        sub_f7d92c(&g_1ef0c58);
        g_1fab3d9 = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (!((char)Object__op_Implicit(ptr->field_20, 0) & 1))
    {
        v0 = sub_1231bc8(ptr, g_1efd060);
        ptr->field_20 = v0;
        sub_f7d8d0((struct struct_1 *)&ptr->field_20, v0);
    }
    return ptr->field_20;
}
```

## `MarkerGroup.ctor` — RVA `0xc7b368`

- Decompiled symbol: `MarkerGroup_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long MarkerGroup_ctor(void)
{
    long long v0;  // x0

    v0 = MonoBehaviour__ctor();
    return MonoBehaviour__ctor();
}
```
