# Native pseudocode: ColorGradingModel.BasicSettings

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `ColorGradingModel.BasicSettings.get_defaultSettings` — RVA `0xcdb640`

- Decompiled symbol: `ColorGradingModel_BasicSettings_get_defaultSettings`
- Metadata signature: `public static ColorGradingModel.BasicSettings get_defaultSettings() { }`
- Native interval: `16` bytes
- Result: `pseudocode`

```c
long long ColorGradingModel_BasicSettings_get_defaultSettings(void)
{
    unsigned long long ptr[3];  // x8
    unsigned long v1;  // x0

    ptr[0] = 0;
    ptr[1] = 0;
    ptr[2] = 0x3f8000003f800000;
    return v1;
}
```
