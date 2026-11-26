# Native pseudocode: ColorGradingModel.TonemappingSettings

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `ColorGradingModel.TonemappingSettings.get_defaultSettings` — RVA `0xcdb61c`

- Decompiled symbol: `ColorGradingModel_TonemappingSettings_get_defaultSettings`
- Metadata signature: `public static ColorGradingModel.TonemappingSettings get_defaultSettings() { }`
- Native interval: `36` bytes
- Result: `pseudocode`
- Heuristic layout hint: `ColorGradingModel_TonemappingSettings_Recovered` matched 3 offsets against `ColorGradingModel.TonemappingSettings` metadata (confidence 1.00).

```c
typedef struct ColorGradingModel_TonemappingSettings_Recovered {
    unsigned int tonemapper;
    uint128_t neutralBlackIn;
    unsigned long long neutralWhiteLevel;
} ColorGradingModel_TonemappingSettings_Recovered;

long long ColorGradingModel_TonemappingSettings_get_defaultSettings(void)
{
    struct_0 *ptr;  // x8
    unsigned long v1;  // x0

    ptr->field_0 = 2;
    *((uint128_t *)&(&ptr->field_0)[1]) = 86565973225492646227553185613494867722;
    *((unsigned long long *)((char *)&ptr->field_4 + 4)) = 4692750812804913562;
    return v1;
}
```
