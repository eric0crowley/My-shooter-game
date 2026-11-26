# Native pseudocode: MapArrow

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `MapArrow.get_ArrowRect` — RVA `0xc7a29c`

- Decompiled symbol: `MapArrow_get_ArrowRect`
- Metadata signature: `public RectTransform get_ArrowRect() { }`
- Native interval: `268` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    char padding_0[32];
    long long field_20;
} struct_2;

typedef struct struct_1 {
    char padding_0[224];
    unsigned int field_e0;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1eef458;
extern struct_1 *g_1ef0c58;
extern long long g_1efd060;
extern long long g_1f0d340;
extern char g_1fab3d1;

long long MapArrow_get_ArrowRect(struct_2 *ptr)
{
    long long v0;  // x0

    if (!(g_1fab3d1 & 1))
    {
        sub_f7d92c(&g_1efd060);
        sub_f7d92c(&g_1eef458);
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c(&g_1f0d340);
        g_1fab3d1 = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (!((char)Object__op_Implicit(ptr->field_20, 0) & 1))
    {
        v0 = sub_1231bc8(ptr, g_1efd060);
        ptr->field_20 = v0;
        sub_f7d8d0((struct struct_2 *)&ptr->field_20, v0);
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        if (!((char)Object__op_Implicit(ptr->field_20, 0) & 1))
        {
            if (!g_1eef458->field_e0)
                sub_f7da5c(g_1eef458);
            Debug__LogError(g_1f0d340, 0);
        }
    }
    return ptr->field_20;
}
```

## `MapArrow.rotate` — RVA `0xc7a3a8`

- Decompiled symbol: `MapArrow_rotate`
- Metadata signature: `public void rotate(Quaternion quat) { }`
- Native interval: `76` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    char padding_0[32];
    long long field_20;
} struct_2;

void MapArrow_rotate(void)
{
    unsigned long long v5;  // d11
    unsigned long long v6;  // d10
    unsigned long long v7;  // d9
    unsigned long long v8;  // d8
    unsigned long long v9;  // x30
    struct_2 *v10;  // x0
    unsigned long long v0;  // [bp-0x30]
    unsigned long long v1;  // [bp-0x28]
    unsigned long long v2;  // [bp-0x20]
    unsigned long long v3;  // [bp-0x18]
    unsigned long long v4;  // [bp-0x10]

    v0 = v5;
    v1 = v6;
    v2 = v7;
    v3 = v8;
    v4 = v9;
    if (MapArrow__get_ArrowRect(v10))
    {
        Transform__set_rotation();
        return;
    }
    sub_f7db74();
}
```

## `MapArrow.ctor` — RVA `0xc7a3f4`

- Decompiled symbol: `MapArrow_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long MapArrow_ctor(void)
{
    long long v0;  // x0

    v0 = MonoBehaviour__ctor();
    return MonoBehaviour__ctor();
}
```
