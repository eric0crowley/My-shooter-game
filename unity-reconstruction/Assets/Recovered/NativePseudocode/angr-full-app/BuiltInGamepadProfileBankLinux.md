# Native pseudocode: BuiltInGamepadProfileBankLinux

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `BuiltInGamepadProfileBankLinux.ctor` — RVA `0xc32e00`

- Decompiled symbol: `BuiltInGamepadProfileBankLinux_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `100` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned long long field_10;
} struct_0;

extern long long g_1eee138;
extern char g_1fab13a;

void BuiltInGamepadProfileBankLinux_ctor(struct_0 *ptr)
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
    if (!(g_1fab13a & 1))
    {
        sub_f7d92c(&g_1eee138);
        g_1fab13a = 1;
    }
    Object__ctor(ptr, 0);
    ptr->field_10 = sub_f7d9d4(g_1eee138, 0);
    sub_f7d8d0();
    return;
}
```
