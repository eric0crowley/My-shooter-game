# Native pseudocode: VignetteModel.Settings

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `VignetteModel.Settings.get_defaultSettings` — RVA `0xcdc294`

- Decompiled symbol: `VignetteModel_Settings_get_defaultSettings`
- Metadata signature: `public static VignetteModel.Settings get_defaultSettings() { }`
- Native interval: `128` bytes
- Result: `pseudocode`
- Heuristic layout hint: `VignetteModel_Settings_Recovered` matched 2 offsets against `VignetteModel.Settings` metadata (confidence 0.67).

```c
typedef struct VignetteModel_Settings_Recovered {
    char padding_0[16];
    uint128_t field_10;
    uint128_t smoothness;
    unsigned long long opacity;
} VignetteModel_Settings_Recovered;

long long VignetteModel_Settings_get_defaultSettings(void)
{
    unsigned long v4;  // x0
    struct_0 *ptr;  // x8
    uint128_t choice;  // [bp-0x60]
    int v1;  // [bp-0x50], Other Possible Types: uint128_t
    uint128_t flag;  // [bp-0x40]
    unsigned long long v3;  // [bp-0x30], Other Possible Types: unsigned long

    v1 = 0;
    flag = 0;
    choice = 0;
    v1 = (int)_INSERT(v1 CONCAT 0, 4, 0x3f0000003f000000);
    *((unsigned int *)&v1) = 0x3f800000;
    *((unsigned int *)&(&v1)[20]) = 0x3f800000;
    *((unsigned long long *)&(&v1)[12]) = 4489188110477190758;
    *((unsigned long long *)&(&v1)[24]) = 0;
    v3 = 0;
    v4 = sub_f7d8d0(&v1 - 24, 0);
    *((unsigned int *)&v3) = 0x3f800000;
    *((char *)&v3 + 4) = 0;
    ptr->field_10 = *((uint128_t *)&v1);
    ptr->field_20 = *((uint128_t *)(&v1 + 16));
    ptr->field_30 = v3;
    *((uint128_t *)&ptr->padding_0[0]) = choice;
    return v4;
}
```
