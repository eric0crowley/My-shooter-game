# Native pseudocode: AntialiasingModel.Settings

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `AntialiasingModel.Settings.get_defaultSettings` — RVA `0xcdae60`

- Decompiled symbol: `AntialiasingModel_Settings_get_defaultSettings`
- Metadata signature: `public static AntialiasingModel.Settings get_defaultSettings() { }`
- Native interval: `28` bytes
- Result: `pseudocode`
- Heuristic layout hint: `AntialiasingModel_Settings_Recovered` matched 2 offsets against `AntialiasingModel.Settings` metadata (confidence 1.00).

```c
typedef struct AntialiasingModel_Settings_Recovered {
    unsigned long long method;
    uint128_t taaSettings;
} AntialiasingModel_Settings_Recovered;

long long AntialiasingModel_Settings_get_defaultSettings(void)
{
    struct_0 *ptr;  // x8
    unsigned long v1;  // x0

    ptr->field_0 = 0x200000000;
    *((uint128_t *)&(&ptr->field_0)[1]) = 0x3f59999a3f7333333e99999a3f400000;
    return v1;
}
```
