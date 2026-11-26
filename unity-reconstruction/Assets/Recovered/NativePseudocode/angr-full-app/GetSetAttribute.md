# Native pseudocode: GetSetAttribute

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `GetSetAttribute.ctor` — RVA `0xccd834`

- Decompiled symbol: `GetSetAttribute_ctor`
- Metadata signature: `public void .ctor(string name) { }`
- Native interval: `48` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

void GetSetAttribute_ctor(struct_0 *ptr, unsigned long a1)
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
