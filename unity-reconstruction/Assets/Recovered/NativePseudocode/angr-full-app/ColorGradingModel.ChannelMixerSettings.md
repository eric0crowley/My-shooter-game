# Native pseudocode: ColorGradingModel.ChannelMixerSettings

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `ColorGradingModel.ChannelMixerSettings.get_defaultSettings` — RVA `0xcdb650`

- Decompiled symbol: `ColorGradingModel_ChannelMixerSettings_get_defaultSettings`
- Metadata signature: `public static ColorGradingModel.ChannelMixerSettings get_defaultSettings() { }`
- Native interval: `24` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    uint128_t field_0;
    uint128_t field_10;
    unsigned long long field_20;
} struct_0;

long long ColorGradingModel_ChannelMixerSettings_get_defaultSettings(void)
{
    struct_0 *ptr;  // x8
    unsigned long v1;  // x0

    ptr->field_20 = 0x3f800000;
    ptr->field_0 = 0x3f800000;
    ptr->field_10 = 0x3f800000;
    return v1;
}
```
