# Native pseudocode: InputRig.AutomaticInputConfig.RelatedAxis

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `InputRig.AutomaticInputConfig.RelatedAxis.IsEnabling` — RVA `0xc424a8`

- Decompiled symbol: `InputRig_AutomaticInputConfig_RelatedAxis_IsEnabling`
- Metadata signature: `public bool IsEnabling(InputRig rig) { }`
- Native interval: `80` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[128];
    unsigned long long field_80;
} struct_0;

unsigned long long InputRig_AutomaticInputConfig_RelatedAxis_IsEnabling(struct_0 *a0, struct_0 *a1)
{
    unsigned long v0;  // x0
    unsigned int v1;  // w0
    unsigned long long v2;  // x0

    if (a1)
    {
        v0 = (unsigned long long)InputRig__GetAxisConfig(a1, *((long long *)&a0->padding_0[16]), &a0->padding_0[28]);
        if (!v0)
            return 1;
        v1 = InputRig_AxisConfig__IsControlledByInput(v0);
        if (a0->padding_0[24] != (v1 & 1))
            v2 = 0;
        else
            v2 = 1;
        return v2;
    }
    sub_f7db74();
}
```

## `InputRig.AutomaticInputConfig.RelatedAxis.ctor` — RVA `0xc424f8`

- Decompiled symbol: `InputRig_AutomaticInputConfig_RelatedAxis_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `96` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    char padding_0[16];
    unsigned long long field_10;
} struct_2;

extern char g_1fab205;

void InputRig_AutomaticInputConfig_RelatedAxis_ctor(struct_2 *ptr)
{
    unsigned long long v4;  // x30
    unsigned long long v5;  // x21
    unsigned long long v6;  // x20
    unsigned long long v7;  // x19
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x18]
    unsigned long long v2;  // [bp-0x10]
    unsigned long long v3;  // [bp-0x8]

    v0 = v4;
    v1 = v5;
    v2 = v6;
    v3 = v7;
    if (!(g_1fab205 & 1))
    {
        sub_f7d92c("MT");
        g_1fab205 = 1;
    }
    Object__ctor(ptr, 0);
    ptr->field_10 = g_1ef18f0->field_b8->field_0;
    sub_f7d8d0();
    return;
}
```
