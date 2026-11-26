# Native pseudocode: BloomModel.Settings

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `BloomModel.Settings.get_defaultSettings` — RVA `0xcdb134`

- Decompiled symbol: `BloomModel_Settings_get_defaultSettings`
- Metadata signature: `public static BloomModel.Settings get_defaultSettings() { }`
- Native interval: `120` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    uint128_t field_10;
    unsigned long long field_20;
} struct_0;

long long BloomModel_Settings_get_defaultSettings(void)
{
    unsigned long v6;  // x0
    struct_0 *ptr;  // x8
    uint128_t v0;  // [bp-0x50]
    int v1;  // [bp-0x40], Other Possible Types: unsigned long long
    unsigned long long flag;  // [bp-0x38]
    unsigned long long v3;  // [bp-0x30]
    unsigned long choice;  // [bp-0x20]
    unsigned long long v5;  // [bp-0x18]

    v1 = 0;
    flag = 0;
    v3 = 0;
    v1 = (int)_INSERT(v1 CONCAT 0, 0, 0);
    *((char *)&(&v1)[3]) = 0;
    *((unsigned short *)&(&v1)[1]) = 0;
    v0 = 0x408000003f0000003f8ccccd3f000000;
    choice = 0;
    v5 = 0;
    sub_f7d8d0(&choice, 0);
    *((unsigned int *)&v5) = 0x40400000;
    *((unsigned long *)&(&v1)[8]) = choice;
    v3 = v5;
    v6 = sub_f7d8d0(&v1 - 8, 0);
    ptr->field_20 = v3;
    *((uint128_t *)&ptr->padding_0[0]) = v0;
    *((void*)&ptr->field_10) = v1;
    return v6;
}
```
