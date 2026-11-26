# Native pseudocode: DepthOfFieldModel.Settings

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `DepthOfFieldModel.Settings.get_defaultSettings` — RVA `0xcdbd20`

- Decompiled symbol: `DepthOfFieldModel_Settings_get_defaultSettings`
- Metadata signature: `public static DepthOfFieldModel.Settings get_defaultSettings() { }`
- Native interval: `44` bytes
- Result: `pseudocode`
- Heuristic layout hint: `DepthOfFieldModel_Settings_Recovered` matched 4 offsets against `DepthOfFieldModel.Settings` metadata (confidence 0.67).

```c
typedef struct DepthOfFieldModel_Settings_Recovered {
    unsigned long long focusDistance;
    unsigned int focalLength;
    char useCameraFov;
    unsigned short field_d;
    char field_f;
    unsigned int kernelSize;
} DepthOfFieldModel_Settings_Recovered;

long long DepthOfFieldModel_Settings_get_defaultSettings(void)
{
    struct_0 *ptr;  // x8
    unsigned long v1;  // x0

    ptr->field_c = 0;
    *((unsigned short *)&(&ptr->field_c)[1]) = 0;
    *((char *)&ptr->field_d + 1) = 0;
    ptr->field_8 = 0x42480000;
    ptr->field_0 = 0x40b3333341200000;
    *((unsigned int *)&ptr->field_f) = 1;
    return v1;
}
```
