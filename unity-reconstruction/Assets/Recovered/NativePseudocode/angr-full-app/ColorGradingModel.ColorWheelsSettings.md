# Native pseudocode: ColorGradingModel.ColorWheelsSettings

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `ColorGradingModel.ColorWheelsSettings.get_defaultSettings` — RVA `0xcdb688`

- Decompiled symbol: `ColorGradingModel_ColorWheelsSettings_get_defaultSettings`
- Metadata signature: `public static ColorGradingModel.ColorWheelsSettings get_defaultSettings() { }`
- Native interval: `40` bytes
- Result: `pseudocode`

```c
long long ColorGradingModel_ColorWheelsSettings_get_defaultSettings(void)
{
    unsigned int *ptr;  // x8
    unsigned long v1;  // x0

    *(ptr) = 1;
    memset(ptr + 1, 0, 96);
    return v1;
}
```
