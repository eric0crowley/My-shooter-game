# Native pseudocode: ScreenSpaceReflectionModel.Settings

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `ScreenSpaceReflectionModel.Settings.get_defaultSettings` — RVA `0xcdc01c`

- Decompiled symbol: `ScreenSpaceReflectionModel_Settings_get_defaultSettings`
- Metadata signature: `public static ScreenSpaceReflectionModel.Settings get_defaultSettings() { }`
- Native interval: `84` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    unsigned long long field_0;
    unsigned int field_8;
    unsigned long long field_c;
    unsigned long long field_14;
    char field_1c;
    unsigned short field_1d;
    char field_1f;
    uint128_t field_20;
    unsigned int field_30;
} struct_0;

long long ScreenSpaceReflectionModel_Settings_get_defaultSettings(void)
{
    struct_0 *ptr;  // x8
    unsigned long v1;  // x0

    ptr->field_0 = 0x200000000;
    ptr->field_8 = 0x42c80000;
    *((unsigned long long *)&(&ptr->field_8)[1]) = 0x300000100;
    *((unsigned long long *)((char *)&ptr->field_c + 4)) = 0x3f8000003f000000;
    *((char *)&ptr->field_14 + 4) = 0;
    *((unsigned short *)((char *)&ptr->field_14 + 5)) = 0;
    *((char *)&ptr->field_14 + 7) = 0;
    *((uint128_t *)&ptr->field_1c) = 0x3f8000003f80000042c800003f800000;
    *((unsigned int *)&ptr->field_20) = 1022739087;
    return v1;
}
```
