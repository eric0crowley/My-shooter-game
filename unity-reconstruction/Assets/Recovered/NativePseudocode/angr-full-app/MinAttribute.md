# Native pseudocode: MinAttribute

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `MinAttribute.ctor` — RVA `0xccd864`

- Decompiled symbol: `MinAttribute_ctor`
- Metadata signature: `public void .ctor(float min) { }`
- Native interval: `40` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[20];
    unsigned int field_14;
} struct_0;

void MinAttribute_ctor(struct_0 *ptr)
{
    unsigned int v0;  // s0

    PropertyAttribute__ctor();
    ptr->field_14 = v0;
    return;
}
```
