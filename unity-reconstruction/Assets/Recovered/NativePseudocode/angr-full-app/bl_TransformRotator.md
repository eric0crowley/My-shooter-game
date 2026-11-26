# Native pseudocode: bl_TransformRotator

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `bl_TransformRotator.Update` — RVA `0xce8b9c`

- Decompiled symbol: `bl_TransformRotator_Update`
- Metadata signature: `private void Update() { }`
- Native interval: `152` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[40];
    unsigned long long field_28;
} struct_0;

extern long long g_1ef22e8;
extern char g_1fab3e3;

void bl_TransformRotator_Update(struct_0 *ptr)
{
    unsigned long long v7;  // d10
    unsigned long long v8;  // d9
    unsigned long long v9;  // d8
    unsigned long long v10;  // x30
    unsigned long long v11;  // x21
    unsigned long long v12;  // x20
    unsigned long long v13;  // x19
    unsigned long long v14;  // x19
    unsigned long long v0;  // [bp-0x40]
    unsigned long long v1;  // [bp-0x30]
    unsigned long long v2;  // [bp-0x28]
    unsigned long long v3;  // [bp-0x20]
    unsigned long long v4;  // [bp-0x18]
    unsigned long long v5;  // [bp-0x10]
    unsigned long long v6;  // [bp-0x8]

    v0 = v7;
    v1 = v8;
    v2 = v9;
    v3 = v10;
    v4 = v11;
    v5 = v12;
    v6 = v13;
    v14 = ptr->field_28;
    if (!g_1fab3e3)
    {
        sub_f7d92c(&g_1ef22e8);
        g_1fab3e3 = 1;
    }
    Time__get_deltaTime(0);
    if (!v14)
        sub_f7db74();
}
```

## `bl_TransformRotator.ctor` — RVA `0xce8c34`

- Decompiled symbol: `bl_TransformRotator_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `16` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[32];
    unsigned int field_20;
} struct_0;

long long bl_TransformRotator_ctor(struct_0 *ptr)
{
    long long v0;  // x0

    ptr->field_20 = 0x41200000;
    v0 = MonoBehaviour__ctor();
    return MonoBehaviour__ctor();
}
```
