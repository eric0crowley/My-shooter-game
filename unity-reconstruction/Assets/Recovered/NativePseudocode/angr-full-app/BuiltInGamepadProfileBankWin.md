# Native pseudocode: BuiltInGamepadProfileBankWin

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `BuiltInGamepadProfileBankWin.ctor` — RVA `0xc32088`

- Decompiled symbol: `BuiltInGamepadProfileBankWin_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `2528` bytes
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
extern long long g_1f08570;
extern long long g_1f08578;
extern long long g_1f09528;
extern long long g_1f0bf38;
extern long long g_1f0cd28;
extern long long g_1f0fca8;
extern long long g_1f13cc8;
extern long long g_1f13cd0;
extern char g_1fab13d;

void BuiltInGamepadProfileBankWin_ctor(long long a0)
{
    unsigned long long v20;  // x30
    unsigned long long v21;  // x28
    unsigned long long v30;  // x19
    void* v31;  // x0
    struct_0 *v32;  // x0
    void* v33;  // x0
    void* v34;  // x0
    void* v35;  // x0
    void* v36;  // x0
    void* v37;  // x0
    void* v38;  // x0
    void* v39;  // x0
    unsigned long long v22;  // x27
    void* v40;  // x0
    void* v41;  // x0
    unsigned long long v23;  // x26
    unsigned long long v24;  // x25
    unsigned long long v25;  // x24
    unsigned long long v26;  // x23
    unsigned long long v27;  // x22
    unsigned long long v28;  // x21
    unsigned long long v29;  // x20
    long long v0;  // [bp-0x98]
    void* v1;  // [bp-0x90]
    void* v2;  // [bp-0x88]
    unsigned long v3;  // [bp-0x80]
    unsigned long v4;  // [bp-0x78]
    unsigned long v5;  // [bp-0x70]
    unsigned long long v6;  // [bp-0x68]
    char *v7;  // [bp-0x60]
    unsigned long long v8;  // [bp-0x58]
    unsigned long long v9;  // [bp-0x50]
    unsigned long long v10;  // [bp-0x48]
    unsigned long long v11;  // [bp-0x40]
    unsigned long long v12;  // [bp-0x38]
    unsigned long long v13;  // [bp-0x30]
    unsigned long long v14;  // [bp-0x28]
    unsigned long long v15;  // [bp-0x20]
    unsigned long long v16;  // [bp-0x18]
    unsigned long long v17;  // [bp-0x10]
    unsigned long long v18;  // [bp-0x8]
    char v19;  // [bp+0x0]

    v7 = &v19;
    v8 = v20;
    v9 = v21;
    v10 = v22;
    v11 = v23;
    v12 = v24;
    v13 = v25;
    v14 = v26;
    v15 = v27;
    v16 = v28;
    v17 = v29;
    v18 = v30;
    if (!(g_1fab13d & 1))
    {
        sub_f7d92c(&g_1eee138);
        sub_f7d92c(&g_1eefb08);
        sub_f7d92c(&g_1f0fca8);
        sub_f7d92c(&g_1f0bf38);
        sub_f7d92c(&g_1f13cc8);
        sub_f7d92c(&g_1f0cd28);
        sub_f7d92c(&g_1f13cd0);
        sub_f7d92c(&g_1f09528);
        sub_f7d92c(&g_1f08570);
        sub_f7d92c(&g_1f08578);
        sub_f7d92c("Y#");
        g_1fab13d = 1;
    }
    v0 = a0;
    Object__ctor(a0, 0);
    v6 = sub_f7d9d4(g_1eee138, 6);
    v5 = (unsigned long long)GamepadProfile_JoystickSource__Axes(0, 1, 1, 0);
    v4 = (unsigned long long)GamepadProfile_JoystickSource__Axes(2, 1, 3, 0);
    v3 = (unsigned long long)GamepadProfile_JoystickSource__Axes(4, 1, 5, 1);
    v2 = GamepadProfile_KeySource__Key(9);
    v1 = GamepadProfile_KeySource__Key(8);
    v31 = GamepadProfile_KeySource__Key(7);
    v32 = GamepadProfile_KeySource__Key(6);
    v33 = GamepadProfile_KeySource__Key(11);
    v34 = GamepadProfile_KeySource__Key(0);
    v35 = GamepadProfile_KeySource__Key(5);
    v36 = GamepadProfile_KeySource__Key(4);
    v37 = GamepadProfile_KeySource__PlusAxis(4294967295);
    v38 = GamepadProfile_KeySource__MinusAxis(4294967295);
    v39 = GamepadProfile_KeySource__Key(3);
    v40 = GamepadProfile_KeySource__Key(2);
    v41 = sub_f7db70(g_1eefb08);
    GamepadProfile__ctor(v41, g_1f13cd0, g_1f13cc8, 0, 0, 0, v5, v4, v3, v2, v1, v31, v32, v33, v34, v35, v36, v37, v38, v39, v40); /* do not return */
}
```
