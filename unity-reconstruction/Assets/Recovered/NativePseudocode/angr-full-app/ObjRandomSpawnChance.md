# Native pseudocode: ObjRandomSpawnChance

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `ObjRandomSpawnChance.Start` — RVA `0xc99d80`

- Decompiled symbol: `ObjRandomSpawnChance_Start`
- Metadata signature: `private void Start() { }`
- Native interval: `156` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[32];
    unsigned int field_20;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab49d;

int ObjRandomSpawnChance_Start(struct_1 *ptr)
{
    unsigned int v0;  // w0
    unsigned int v1;  // s1
    unsigned int v2;  // s0
    unsigned long v3;  // 4129

    if (!(g_1fab49d & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab49d = 1;
    }
    v0 = Random__get_value(0);
    v1 = ptr->field_20;
    v3 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v2, v1)) >> 5 & 3 | (unsigned long long)(CmpF(v2, v1) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v2, v1)) >> 5 & 3 | (unsigned long long)(CmpF(v2, v1) & 1)) & ((unsigned long long)(char)(CmpF(v2, v1)) >> 5 & 3 | (unsigned long long)(CmpF(v2, v1) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if ((char)v3)
        return v0;
    if (Component__get_transform(ptr, 0))
    {
        Component__get_gameObject();
        if (g_1ef0c58->field_e0)
            return Object__Destroy();
        sub_f7da5c(g_1ef0c58);
        return Object__Destroy();
    }
    sub_f7db74();
}
```

## `ObjRandomSpawnChance.ctor` — RVA `0xc99e1c`

- Decompiled symbol: `ObjRandomSpawnChance_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `16` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[32];
    unsigned int field_20;
} struct_0;

long long ObjRandomSpawnChance_ctor(struct_0 *ptr)
{
    long long v0;  // x0

    ptr->field_20 = 0x3f800000;
    v0 = MonoBehaviour__ctor();
    return MonoBehaviour__ctor();
}
```
