# Native pseudocode: BuiltinDebugViewsModel.Settings

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `BuiltinDebugViewsModel.Settings.get_defaultSettings` — RVA `0xcdb2cc`

- Decompiled symbol: `BuiltinDebugViewsModel_Settings_get_defaultSettings`
- Metadata signature: `public static BuiltinDebugViewsModel.Settings get_defaultSettings() { }`
- Native interval: `40` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    unsigned int field_0;
    uint128_t field_4;
    unsigned long long field_14;
    unsigned int field_1c;
} struct_0;

long long BuiltinDebugViewsModel_Settings_get_defaultSettings(void)
{
    struct_0 *ptr;  // x8
    unsigned long v1;  // x0

    ptr->field_0 = 0;
    *((unsigned long long *)((char *)&ptr->field_4 + 4)) = 0x183f800000;
    *((uint128_t *)&(&ptr->field_0)[1]) = 0x41800000000000003f8000003f800000;
    *((unsigned int *)((char *)&ptr->field_4 + 12)) = 0x42800000;
    return v1;
}
```
