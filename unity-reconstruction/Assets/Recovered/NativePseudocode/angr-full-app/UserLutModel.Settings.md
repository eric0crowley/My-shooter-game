# Native pseudocode: UserLutModel.Settings

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `UserLutModel.Settings.get_defaultSettings` — RVA `0xcdc128`

- Decompiled symbol: `UserLutModel_Settings_get_defaultSettings`
- Metadata signature: `public static UserLutModel.Settings get_defaultSettings() { }`
- Native interval: `48` bytes
- Result: `pseudocode`

```c
long long UserLutModel_Settings_get_defaultSettings(void)
{
    unsigned long choice;  // [bp-0x20]
    unsigned long long flag;  // [bp-0x18]

    flag = 0;
    choice = 0;
    sub_f7d8d0(&choice, 0);
    return choice;
}
```
