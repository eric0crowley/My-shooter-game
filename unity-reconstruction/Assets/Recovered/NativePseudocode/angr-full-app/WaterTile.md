# Native pseudocode: WaterTile

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `WaterTile.Start` — RVA `0xce59a8`

- Decompiled symbol: `WaterTile_Start`
- Metadata signature: `public void Start() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long WaterTile_Start(unsigned long a0)
{
    unsigned long long v0;  // x0

    v0 = WaterTile__AcquireComponents();
    return WaterTile__AcquireComponents();
}
```

## `WaterTile.AcquireComponents` — RVA `0xce59ac`

- Decompiled symbol: `WaterTile_AcquireComponents`
- Metadata signature: `private void AcquireComponents() { }`
- Native interval: `448` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern long long g_1efd050;
extern long long g_1efd0d0;
extern char g_1fab659;

long long WaterTile_AcquireComponents(long long *a0)
{
    long long v0[6];  // x20
    long long ptr[6];  // x20
    long long v2;  // x0
    unsigned int v3;  // w0
    long long v4;  // x0
    long long p[6];  // x20
    long long v6;  // x0
    long long v7;  // x0
    unsigned int v8;  // w0
    long long v9;  // x0

    if (!(g_1fab659 & 1))
    {
        sub_f7d92c(&g_1efd050);
        sub_f7d92c(&g_1efd0d0);
        sub_f7d92c(&g_1ef0c58);
        g_1fab659 = 1;
    }
    v0 = a0;
    ptr = &v0[4];
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (((char)Object__op_Implicit(v0[4], 0) & 1))
    {
LABEL_10e5aa4:
        p = a0;
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        v6 = Object__op_Implicit(p[5], 0);
        if (((char)v6 & 1))
            return v6;
        if (Component__get_transform(a0, 0))
        {
            v7 = Transform__get_parent();
            if (!g_1ef0c58->field_e0)
                sub_f7da5c(g_1ef0c58);
            v8 = Object__op_Implicit(v7, 0);
            if (Component__get_transform(a0, 0) && (!((char)v8 & 1) || Transform__get_parent()))
            {
                p[5] = sub_1231bc8();
                v9 = sub_f7d8d0();
                return sub_f7d8d0();
            }
        }
    }
    else if (Component__get_transform(a0, 0))
    {
        v2 = Transform__get_parent();
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        v3 = Object__op_Implicit(v2, 0);
        if (Component__get_transform(a0, 0) && (!((char)v3 & 1) || Transform__get_parent()))
        {
            v4 = sub_1231bc8();
            ptr[0] = v4;
            sub_f7d8d0(ptr, v4);
            goto LABEL_10e5aa4;
        }
    }
    sub_f7db74();
}
```

## `WaterTile.OnWillRenderObject` — RVA `0xce5b6c`

- Decompiled symbol: `WaterTile_OnWillRenderObject`
- Metadata signature: `public void OnWillRenderObject() { }`
- Native interval: `228` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab65a;

long long WaterTile_OnWillRenderObject(void* a0)
{
    long long v0;  // x0
    long long v1;  // x0
    long long v2;  // x0
    long long v3;  // x0

    if (!(g_1fab65a & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab65a = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (((char)Object__op_Implicit((long long)a0[32], 0) & 1))
    {
        Component__get_transform(a0, 0);
        v0 = Camera__get_current(0);
        if (!(long long)a0[32])
            sub_f7db74();
        PlanarReflection__WaterTileBeingRendered((long long)a0[32], 0, v0);
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v1 = Object__op_Implicit((long long)a0[40], 0);
    if (!((char)v1 & 1))
        return v1;
    Component__get_transform(a0, 0);
    v2 = Camera__get_current(0);
    if ((long long)a0[40])
    {
        v3 = WaterBase__WaterTileBeingRendered((long long)a0[40], 0, v2);
        return WaterBase__WaterTileBeingRendered((long long)a0[40], 0, v2);
    }
    sub_f7db74();
}
```

## `WaterTile.ctor` — RVA `0xce5c50`

- Decompiled symbol: `WaterTile_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long WaterTile_ctor(void)
{
    long long v0;  // x0

    v0 = MonoBehaviour__ctor();
    return MonoBehaviour__ctor();
}
```
