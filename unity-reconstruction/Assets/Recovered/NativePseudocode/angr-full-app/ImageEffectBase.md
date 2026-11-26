# Native pseudocode: ImageEffectBase

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `ImageEffectBase.Start` — RVA `0xce5c58`

- Decompiled symbol: `ImageEffectBase_Start`
- Metadata signature: `protected virtual void Start() { }`
- Native interval: `160` bytes
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
extern char g_1fab65b;

long long ImageEffectBase_Start(struct_1 *a0)
{
    long long v0;  // x0
    long long v1;  // x0

    if (!(g_1fab65b & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab65b = 1;
    }
    if (((char)SystemInfo__get_supportsImageEffects(0) & 1))
    {
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        if (((char)Object__op_Implicit(a0->field_20, 0) & 1))
        {
            if (a0->field_20)
            {
                v0 = Shader__get_isSupported(a0->field_20, 0);
                if (((char)v0 & 1))
                    return v0;
            }
            else
            {
                sub_f7db74(0);
            }
        }
    }
    v1 = Behaviour__set_enabled();
    return Behaviour__set_enabled();
}
```

## `ImageEffectBase.get_material` — RVA `0xce5cf8`

- Decompiled symbol: `ImageEffectBase_get_material`
- Metadata signature: `protected Material get_material() { }`
- Native interval: `208` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab65c;

long long ImageEffectBase_get_material(long long *ptr)
{
    long long v0;  // x22

    if (!(g_1fab65c & 1))
    {
        sub_f7d92c("7F");
        sub_f7d92c(&g_1ef0c58);
        g_1fab65c = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (((char)Object__op_Equality(ptr[5], 0, 0) & 1))
    {
        v0 = sub_f7db70(g_1ef07c0);
        Material__ctor(v0, ptr[4], 0);
        ptr[5] = v0;
        sub_f7d8d0(ptr + 5, v0);
        if (!ptr[5])
            sub_f7db74(0);
        Object__set_hideFlags(ptr[5], 61, 0);
    }
    return ptr[5];
}
```

## `ImageEffectBase.OnDisable` — RVA `0xce5dc8`

- Decompiled symbol: `ImageEffectBase_OnDisable`
- Metadata signature: `protected virtual void OnDisable() { }`
- Native interval: `140` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[40];
    long long field_28;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab65d;

long long ImageEffectBase_OnDisable(struct_1 *a0)
{
    long long v0;  // x0
    long long v1;  // x0

    if (!(g_1fab65d & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab65d = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v0 = Object__op_Implicit(a0->field_28, 0);
    if (!((char)v0 & 1))
        return v0;
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v1 = Object__DestroyImmediate();
    return Object__DestroyImmediate();
}
```

## `ImageEffectBase.ctor` — RVA `0xce5e54`

- Decompiled symbol: `ImageEffectBase_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long ImageEffectBase_ctor(void)
{
    long long v0;  // x0

    v0 = MonoBehaviour__ctor();
    return MonoBehaviour__ctor();
}
```
