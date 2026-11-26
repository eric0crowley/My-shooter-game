# Native pseudocode: ColorGradingModel.Settings

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `ColorGradingModel.Settings.get_defaultSettings` — RVA `0xcdb4f8`

- Decompiled symbol: `ColorGradingModel_Settings_get_defaultSettings`
- Metadata signature: `public static ColorGradingModel.Settings get_defaultSettings() { }`
- Native interval: `204` bytes
- Result: `pseudocode`

```c
long long ColorGradingModel_Settings_get_defaultSettings(void)
{
    long long v25;  // x8
    unsigned long dst;  // x0
    char v0;  // [bp-0x170]
    unsigned int v1;  // [bp-0x128]
    uint128_t v2;  // [bp-0x124]
    unsigned long long v3;  // [bp-0x114]
    unsigned long long flag9;  // [bp-0x10c]
    unsigned long long flag8;  // [bp-0x104]
    uint128_t v6;  // [bp-0xfc]
    uint128_t v7;  // [bp-0xec]
    unsigned int flag;  // [bp-0xdc]
    unsigned int choice;  // [bp-0xd8]
    unsigned long long v10;  // [bp-0xd4]
    unsigned int flag2;  // [bp-0xcc]
    uint128_t flag10;  // [bp-0xc8]
    uint128_t flag11;  // [bp-0xb8]
    uint128_t flag12;  // [bp-0xa8]
    uint128_t flag13;  // [bp-0x98]
    uint128_t flag14;  // [bp-0x88]
    uint128_t flag15;  // [bp-0x78]
    int flag5;  // [bp-0x68]
    uint128_t flag6;  // [bp-0x58]
    uint128_t flag3;  // [bp-0x48]
    uint128_t flag4;  // [bp-0x38]
    unsigned long long flag7;  // [bp-0x28]
    char *v23;  // [bp-0x20]
    char v24;  // [bp+0x0]

    v23 = &v24;
    flag3 = 0;
    flag4 = 0;
    flag5 = 0;
    flag6 = 0;
    v2 = 86565973225492646227553185613494867722;
    v1 = 2;
    v3 = 4692750812804913562;
    flag7 = 0;
    v6 = 0x3f8000003f8000003f800000;
    flag8 = 0;
    flag9 = 0;
    v7 = 0x3f8000000000000000000000;
    flag = 0;
    choice = 0;
    v10 = 0x3f800000;
    flag10 = 0;
    flag11 = 0;
    flag12 = 0;
    flag13 = 0;
    flag14 = 0;
    flag15 = 0;
    flag2 = 1;
    ColorGradingModel_CurvesSettings__get_defaultSettings();
    memcpy(&flag5, &v0, 72);
    sub_f7d8d0(&flag5, 0);
    dst = memcpy(v25, &v1, 264);
    return memcpy(v25, &v1, 264);
}
```
