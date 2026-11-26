# Native pseudocode: InputRig.AutomaticInputConfig.RelatedKey

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `InputRig.AutomaticInputConfig.RelatedKey.IsEnabling` — RVA `0xc42460`

- Decompiled symbol: `InputRig_AutomaticInputConfig_RelatedKey_IsEnabling`
- Metadata signature: `public bool IsEnabling(InputRig rig) { }`
- Native interval: `72` bytes
- Result: `pseudocode`
- Heuristic layout hint: `InputRig_AutomaticInputConfig_RelatedKey_Recovered` matched 2 offsets against `InputRig.AutomaticInputConfig.RelatedKey` metadata (confidence 1.00).

```c
typedef struct InputRig_AutomaticInputConfig_RelatedKey_Recovered {
    char padding_0[16];
    unsigned int key;
    char mustBeControlledByInput;
} InputRig_AutomaticInputConfig_RelatedKey_Recovered;

unsigned long long InputRig_AutomaticInputConfig_RelatedKey_IsEnabling(struct_0 *a0, long long *a1)
{
    unsigned int v0;  // w0
    unsigned long long v1;  // x0

    if (!a0->field_10)
        return 1;
    if (a1)
    {
        v0 = InputRig__GetKey(a1, a0->field_10);
        if (a0->field_14 != (v0 & 1))
            v1 = 0;
        else
            v1 = 1;
        return v1;
    }
    sub_f7db74();
}
```

## `InputRig.AutomaticInputConfig.RelatedKey.ctor` — RVA `0xc42558`

- Decompiled symbol: `InputRig_AutomaticInputConfig_RelatedKey_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long InputRig_AutomaticInputConfig_RelatedKey_ctor(void)
{
    long long v0;  // x0

    v0 = Object__ctor();
    return Object__ctor();
}
```
