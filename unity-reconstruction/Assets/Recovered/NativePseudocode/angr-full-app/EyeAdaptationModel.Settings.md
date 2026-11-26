# Native pseudocode: EyeAdaptationModel.Settings

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `EyeAdaptationModel.Settings.get_defaultSettings` — RVA `0xcdbe20`

- Decompiled symbol: `EyeAdaptationModel_Settings_get_defaultSettings`
- Metadata signature: `public static EyeAdaptationModel.Settings get_defaultSettings() { }`
- Native interval: `68` bytes
- Result: `pseudocode`
- Heuristic layout hint: `EyeAdaptationModel_Settings_Recovered` matched 6 offsets against `EyeAdaptationModel.Settings` metadata (confidence 0.75).

```c
typedef struct EyeAdaptationModel_Settings_Recovered {
    uint128_t lowPercent;
    unsigned int keyValue;
    char dynamicKeyValue;
    unsigned short field_15;
    char field_17;
    unsigned int adaptationType;
    unsigned long long speedUp;
    unsigned long long logMin;
} EyeAdaptationModel_Settings_Recovered;

long long EyeAdaptationModel_Settings_get_defaultSettings(void)
{
    struct_0 *ptr;  // x8
    unsigned long v1;  // x0

    *((unsigned short *)&(&ptr->field_14)[1]) = 0;
    *((char *)&ptr->field_15 + 1) = 0;
    ptr->field_0 = 0x3f800000c0a0000042be000042340000;
    ptr->field_10 = 0x3e800000;
    *((unsigned long long *)&ptr->field_18) = 0x3f80000040000000;
    *((unsigned int *)&ptr->field_17) = 0;
    ptr->field_14 = 1;
    *((unsigned long long *)((char *)&ptr->field_1c + 4)) = 21474836472;
    return v1;
}
```
