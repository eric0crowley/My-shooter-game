# Native pseudocode: <PrivateImplementationDetails>

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `<PrivateImplementationDetails>.ComputeStringHash` — RVA `0xceb858`

- Decompiled symbol: `PrivateImplementationDetails_ComputeStringHash`
- Metadata signature: `internal static uint ComputeStringHash(string s) { }`
- Native interval: `124` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    int field_10;
} struct_0;

extern char g_1000193;

unsigned int PrivateImplementationDetails_ComputeStringHash(struct_0 *a0)
{
    unsigned int v0;  // w20
    int i;  // w21
    int v2;  // w21
    int v3;  // w21

    if (!a0)
        return 0;
    v0 = 2166136261;
    if (a0->field_10 < 1)
        return 2166136261;
    i = 0;
    do
    {
        v2 = i;
        v3 = v2 + 1;
        v0 = &g_1000193 * (v0 ^ (int)String__get_Chars(a0, v2, 0) & 65535);
        i = v3;
    } while (i < a0->field_10);
    return v0;
}
```
