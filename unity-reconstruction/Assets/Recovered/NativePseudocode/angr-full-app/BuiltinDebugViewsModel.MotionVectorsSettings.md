# Native pseudocode: BuiltinDebugViewsModel.MotionVectorsSettings

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `BuiltinDebugViewsModel.MotionVectorsSettings.get_defaultSettings` — RVA `0xcdb328`

- Decompiled symbol: `BuiltinDebugViewsModel_MotionVectorsSettings_get_defaultSettings`
- Metadata signature: `public static BuiltinDebugViewsModel.MotionVectorsSettings get_defaultSettings() { }`
- Native interval: `28` bytes
- Result: `pseudocode`
- Heuristic layout hint: `BuiltinDebugViewsModel_MotionVectorsSettings_Recovered` matched 2 offsets against `BuiltinDebugViewsModel.MotionVectorsSettings` metadata (confidence 1.00).

```c
typedef struct BuiltinDebugViewsModel_MotionVectorsSettings_Recovered {
    uint128_t sourceOpacity;
    unsigned long long motionVectorsResolution;
} BuiltinDebugViewsModel_MotionVectorsSettings_Recovered;

long long BuiltinDebugViewsModel_MotionVectorsSettings_get_defaultSettings(void)
{
    struct_0 *ptr;  // x8
    unsigned long v1;  // x0

    ptr->field_10 = 4791830003522207768;
    ptr->field_0 = 0x3f80000041800000000000003f800000;
    return v1;
}
```
