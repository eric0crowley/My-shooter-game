# Native pseudocode: BloomModel.BloomSettings

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `BloomModel.BloomSettings.get_thresholdLinear` — RVA `0xccf214`

- Decompiled symbol: `BloomModel_BloomSettings_get_thresholdLinear`
- Metadata signature: `public float get_thresholdLinear() { }`
- Native interval: `12` bytes
- Result: `pseudocode`

```c
void BloomModel_BloomSettings_get_thresholdLinear(unsigned long a0)
{
    Mathf__GammaToLinearSpace();
    return;
}
```

## `BloomModel.BloomSettings.set_thresholdLinear` — RVA `0xcdb1f8`

- Decompiled symbol: `BloomModel_BloomSettings_set_thresholdLinear`
- Metadata signature: `public void set_thresholdLinear(float value) { }`
- Native interval: `28` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

int BloomModel_BloomSettings_set_thresholdLinear(struct_0 *ptr)
{
    unsigned int v0;  // w0
    unsigned int v1;  // s0

    v0 = Mathf__LinearToGammaSpace(0);
    ptr->field_4 = v1;
    return v0;
}
```

## `BloomModel.BloomSettings.get_defaultSettings` — RVA `0xcdb214`

- Decompiled symbol: `BloomModel_BloomSettings_get_defaultSettings`
- Metadata signature: `public static BloomModel.BloomSettings get_defaultSettings() { }`
- Native interval: `28` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    uint128_t field_0;
    char field_10;
    unsigned short field_11;
    char field_13;
} struct_0;

long long BloomModel_BloomSettings_get_defaultSettings(void)
{
    struct_0 *ptr;  // x8
    unsigned long v1;  // x0

    ptr->field_10 = 0;
    *((unsigned short *)&(&ptr->field_10)[1]) = 0;
    *((char *)&ptr->field_11 + 1) = 0;
    ptr->field_0 = 0x408000003f0000003f8ccccd3f000000;
    return v1;
}
```
