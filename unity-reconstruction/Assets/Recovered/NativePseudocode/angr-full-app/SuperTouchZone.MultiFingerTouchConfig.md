# Native pseudocode: SuperTouchZone.MultiFingerTouchConfig

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `SuperTouchZone.MultiFingerTouchConfig.ctor` — RVA `0xc49670`

- Decompiled symbol: `SuperTouchZone_MultiFingerTouchConfig_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `236` bytes
- Result: `pseudocode`

```c
extern long long g_1ef0548;
extern long long g_1ef1e10;
extern long long g_1ef1e20;
extern char g_1fab23e;

long long SuperTouchZone_MultiFingerTouchConfig_ctor(long long a0)
{
    unsigned long long v6;  // x30
    unsigned long long v7;  // x23
    unsigned long long v8;  // x22
    unsigned long long v9;  // x21
    unsigned long long v10;  // x20
    unsigned long long v11;  // x19
    unsigned long long v0;  // [bp-0x30]
    unsigned long long v1;  // [bp-0x28]
    unsigned long long v2;  // [bp-0x20]
    unsigned long long v3;  // [bp-0x18]
    unsigned long long v4;  // [bp-0x10]
    unsigned long long v5;  // [bp-0x8]

    v0 = v6;
    v1 = v7;
    v2 = v8;
    v3 = v9;
    v4 = v10;
    v5 = v11;
    if (!(g_1fab23e & 1))
    {
        sub_f7d92c(&g_1ef0548);
        sub_f7d92c(&g_1ef1e10);
        sub_f7d92c(&g_1ef1e20);
        g_1fab23e = 1;
    }
    Object__ctor(a0, 0);
    TouchGestureStateBinding__ctor(sub_f7db70(g_1ef1e20), 0, 0); /* do not return */
}
```
