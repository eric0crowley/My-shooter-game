# Native pseudocode: SeparatorAttribute

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `SeparatorAttribute.ctor` — RVA `0xcca990`

- Decompiled symbol: `SeparatorAttribute_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `88` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

extern unsigned long long g_1f06220;
extern char g_1fab57b;

void SeparatorAttribute_ctor(struct_0 *ptr)
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
    if (!(g_1fab57b & 1))
    {
        sub_f7d92c(&g_1f06220);
        g_1fab57b = 1;
    }
    PropertyAttribute__ctor(ptr, 0);
    ptr->field_18 = g_1f06220;
    sub_f7d8d0();
    return;
}
```

## `SeparatorAttribute.ctor` — RVA `0xcca9e8`

- Decompiled symbol: `SeparatorAttribute_ctor`
- Metadata signature: `public void .ctor(string _title) { }`
- Native interval: `48` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

void SeparatorAttribute_ctor(struct_0 *ptr, unsigned long a1)
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
    PropertyAttribute__ctor();
    ptr->field_18 = a1;
    sub_f7d8d0();
    return;
}
```
