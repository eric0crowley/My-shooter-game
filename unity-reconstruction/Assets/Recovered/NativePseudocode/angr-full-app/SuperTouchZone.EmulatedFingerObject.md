# Native pseudocode: SuperTouchZone.EmulatedFingerObject

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `SuperTouchZone.EmulatedFingerObject.ctor` — RVA `0xc4d010`

- Decompiled symbol: `SuperTouchZone_EmulatedFingerObject_ctor`
- Metadata signature: `public void .ctor(SuperTouchZone parentZone) { }`
- Native interval: `44` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[80];
    unsigned long long field_50;
} struct_0;

void SuperTouchZone_EmulatedFingerObject_ctor(struct_0 *ptr, unsigned long a1)
{
    unsigned long long v3;  // x30
    unsigned long long v4;  // x20
    unsigned long long v5;  // x19
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x10]
    unsigned long long v2;  // [bp-0x8]

    v0 = v3;
    v1 = v4;
    v2 = v5;
    TouchObject__ctor();
    ptr->field_50 = a1;
    sub_f7d8d0();
    return;
}
```
