# Native pseudocode: bl_LoadingScreenExample

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `bl_LoadingScreenExample.Update` — RVA `0xc799f0`

- Decompiled symbol: `bl_LoadingScreenExample_Update`
- Metadata signature: `private void Update() { }`
- Native interval: `68` bytes
- Result: `pseudocode`
- Heuristic layout hint: `bl_LoadingScreenExample_Recovered` matched 2 offsets against `bl_LoadingScreenExample` metadata (confidence 1.00).

```c
typedef struct bl_LoadingScreenExample_Recovered {
    char padding_0[32];
    unsigned int SceneName;
    char padding_24[4];
    char loaded;
} bl_LoadingScreenExample_Recovered;

struct_0 * bl_LoadingScreenExample_Update(struct_0 *ptr)
{
    struct_0 *v0;  // x0
    unsigned long v1;  // x0
    struct_0 *v2;  // x0

    if (ptr->field_28)
        return ptr;
    v0 = Input__GetKeyDown(32, 0);
    if (!((char)v0 & 1))
        return v0;
    v1 = bl_SceneLoader__GetActiveLoader();
    if (v1)
    {
        v2 = bl_SceneLoader__LoadLevel(v1, *((long long *)&ptr->field_20));
        ptr->field_28 = 1;
        return v2;
    }
    sub_f7db74();
}
```

## `bl_LoadingScreenExample.ctor` — RVA `0xc79a34`

- Decompiled symbol: `bl_LoadingScreenExample_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `88` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[32];
    long long field_20;
} struct_0;

extern long long g_1f0bdc0;
extern char g_1fab3cb;

void bl_LoadingScreenExample_ctor(struct_0 *ptr)
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
    if (!(g_1fab3cb & 1))
    {
        sub_f7d92c(&g_1f0bdc0);
        g_1fab3cb = 1;
    }
    ptr->field_20 = g_1f0bdc0;
    sub_f7d8d0((struct struct_0 *)&ptr->field_20, g_1f0bdc0);
    MonoBehaviour__ctor();
    return;
}
```
