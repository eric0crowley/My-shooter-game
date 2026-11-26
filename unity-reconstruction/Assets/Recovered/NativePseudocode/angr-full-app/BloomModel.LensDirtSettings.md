# Native pseudocode: BloomModel.LensDirtSettings

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `BloomModel.LensDirtSettings.get_defaultSettings` — RVA `0xcdb230`

- Decompiled symbol: `BloomModel_LensDirtSettings_get_defaultSettings`
- Metadata signature: `public static BloomModel.LensDirtSettings get_defaultSettings() { }`
- Native interval: `48` bytes
- Result: `pseudocode`

```c
long long BloomModel_LensDirtSettings_get_defaultSettings(void)
{
    unsigned long choice;  // [bp-0x20]
    unsigned long long flag;  // [bp-0x18]

    flag = 0;
    choice = 0;
    sub_f7d8d0(&choice, 0);
    return choice;
}
```
