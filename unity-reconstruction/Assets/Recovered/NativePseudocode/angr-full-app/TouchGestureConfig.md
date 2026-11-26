# Native pseudocode: TouchGestureConfig

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `TouchGestureConfig.ctor` — RVA `0xc61ab8`

- Decompiled symbol: `TouchGestureConfig_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `40` bytes
- Result: `pseudocode`
- Heuristic layout hint: `TouchGestureConfig_Recovered` matched 3 offsets against `TouchGestureConfig` metadata (confidence 1.00).

```c
typedef struct TouchGestureConfig_Recovered {
    char padding_0[16];
    unsigned int maxTapCount;
    char cleanTapsOnly;
    char padding_15[11];
    unsigned int swipeOriginalDirResetMode;
} TouchGestureConfig_Recovered;

void TouchGestureConfig_ctor(struct_0 *ptr)
{
    Object__ctor();
    ptr->field_10 = 1;
    ptr->field_14 = 1;
    ptr->field_20 = 1;
    return;
}
```
