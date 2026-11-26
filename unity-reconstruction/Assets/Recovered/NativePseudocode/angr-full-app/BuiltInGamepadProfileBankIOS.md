# Native pseudocode: BuiltInGamepadProfileBankIOS

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `BuiltInGamepadProfileBankIOS.ctor` — RVA `0xc32a68`

- Decompiled symbol: `BuiltInGamepadProfileBankIOS_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `920` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
    unsigned int field_14;
    char field_18;
} struct_0;

extern long long g_1eee138;
extern long long g_1eefb08;
extern long long g_1f0bee0;
extern long long g_1f0dcb8;
extern char g_1fab139;

void BuiltInGamepadProfileBankIOS_ctor(long long a0)
{
    unsigned long long v18;  // x30
    unsigned long long v19;  // x28
    unsigned long long v28;  // x19
    void* v29;  // x0
    struct_0 *v30;  // x0
    struct_0 *v31;  // x0
    void* v32;  // x0
    void* v33;  // x0
    void* v34;  // x0
    void* v35;  // x0
    void* v36;  // x0
    void* v37;  // x0
    unsigned long long v20;  // x27
    void* v38;  // x0
    void* v39;  // x0
    unsigned long long v21;  // x26
    unsigned long long v22;  // x25
    unsigned long long v23;  // x24
    unsigned long long v24;  // x23
    unsigned long long v25;  // x22
    unsigned long long v26;  // x21
    unsigned long long v27;  // x20
    void* v0;  // [bp-0x90]
    void* v1;  // [bp-0x88]
    unsigned long v2;  // [bp-0x80]
    unsigned long v3;  // [bp-0x78]
    unsigned long v4;  // [bp-0x70]
    char *v5;  // [bp-0x60]
    unsigned long long v6;  // [bp-0x58]
    unsigned long long v7;  // [bp-0x50]
    unsigned long long v8;  // [bp-0x48]
    unsigned long long v9;  // [bp-0x40]
    unsigned long long v10;  // [bp-0x38]
    unsigned long long v11;  // [bp-0x30]
    unsigned long long v12;  // [bp-0x28]
    unsigned long long v13;  // [bp-0x20]
    unsigned long long v14;  // [bp-0x18]
    unsigned long long v15;  // [bp-0x10]
    unsigned long long v16;  // [bp-0x8]
    char v17;  // [bp+0x0]

    v5 = &v17;
    v6 = v18;
    v7 = v19;
    v8 = v20;
    v9 = v21;
    v10 = v22;
    v11 = v23;
    v12 = v24;
    v13 = v25;
    v14 = v26;
    v15 = v27;
    v16 = v28;
    if (!(g_1fab139 & 1))
    {
        sub_f7d92c(&g_1eee138);
        sub_f7d92c(&g_1eefb08);
        sub_f7d92c(&g_1f0bee0);
        sub_f7d92c(&g_1f0dcb8);
        g_1fab139 = 1;
    }
    Object__ctor(a0, 0);
    v4 = (unsigned long long)GamepadProfile_JoystickSource__Axes(0, 1, 1, 0);
    v3 = (unsigned long long)GamepadProfile_JoystickSource__Axes(2, 1, 3, 0);
    v2 = (unsigned long long)GamepadProfile_JoystickSource__Dpad(4, 5, 6, 7);
    v1 = GamepadProfile_KeySource__Key(14);
    v0 = GamepadProfile_KeySource__Key(13);
    v29 = GamepadProfile_KeySource__Key(15);
    v30 = GamepadProfile_KeySource__Key(12);
    v31 = GamepadProfile_KeySource__Empty();
    v32 = GamepadProfile_KeySource__Key(0);
    v33 = GamepadProfile_KeySource__KeyAndPlusAxis(8, 8);
    v34 = GamepadProfile_KeySource__KeyAndPlusAxis(9, 9);
    v35 = GamepadProfile_KeySource__KeyAndPlusAxis(10, 10);
    v36 = GamepadProfile_KeySource__KeyAndPlusAxis(11, 11);
    v37 = GamepadProfile_KeySource__Key(4294967295);
    v38 = GamepadProfile_KeySource__Key(4294967295);
    v39 = sub_f7db70(g_1eefb08);
    GamepadProfile__ctor(v39, g_1f0bee0, g_1f0bee0, 0, 0, 0, v4, v3, v2, v1, v0, v29, v30, v31, v32, v33, v34, v35, v36, v37, v38); /* do not return */
}
```
