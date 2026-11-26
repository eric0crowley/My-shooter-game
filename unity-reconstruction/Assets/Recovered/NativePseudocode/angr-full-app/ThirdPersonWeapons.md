# Native pseudocode: ThirdPersonWeapons

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `ThirdPersonWeapons.ctor` — RVA `0xcb57b4`

- Decompiled symbol: `ThirdPersonWeapons_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `136` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[32];
    long long field_20;
} struct_0;

extern long long g_1eed750;
extern long long g_1ef8170;
extern char g_1fab4df;

void ThirdPersonWeapons_ctor(struct_0 *ptr)
{
    unsigned long long v5;  // x30
    unsigned long long v6;  // x22
    unsigned long long v7;  // x21
    unsigned long long v8;  // x20
    unsigned long long v9;  // x19
    long long v10;  // x20
    unsigned long long v0;  // [bp-0x30]
    unsigned long long v1;  // [bp-0x20]
    unsigned long long v2;  // [bp-0x18]
    unsigned long long v3;  // [bp-0x10]
    unsigned long long v4;  // [bp-0x8]

    v0 = v5;
    v1 = v6;
    v2 = v7;
    v3 = v8;
    v4 = v9;
    if (!(g_1fab4df & 1))
    {
        sub_f7d92c(&g_1ef8170);
        sub_f7d92c(&g_1eed750);
        g_1fab4df = 1;
    }
    v10 = sub_f7db70(g_1eed750);
    sub_14a2b64(v10, g_1ef8170);
    ptr->field_20 = v10;
    sub_f7d8d0((struct struct_0 *)&ptr->field_20, v10);
    MonoBehaviour__ctor();
    return;
}
```
