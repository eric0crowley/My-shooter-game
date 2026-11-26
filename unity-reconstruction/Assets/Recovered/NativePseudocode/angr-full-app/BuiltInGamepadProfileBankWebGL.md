# Native pseudocode: BuiltInGamepadProfileBankWebGL

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `BuiltInGamepadProfileBankWebGL.ctor` — RVA `0xc32e64`

- Decompiled symbol: `BuiltInGamepadProfileBankWebGL_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `1396` bytes
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
extern long long g_1f0bf38;
extern long long g_1f0cd28;
extern long long g_1f0fca8;
extern long long g_1f15c68;
extern char g_1fab13c;

void BuiltInGamepadProfileBankWebGL_ctor(long long a0)
{
    unsigned long long v20;  // x30
    unsigned long long v21;  // x28
    unsigned long long v30;  // x19
    struct_0 *v31;  // x0
    void* v32;  // x0
    void* v33;  // x0
    void* v34;  // x0
    void* v35;  // x0
    void* v36;  // x0
    void* v37;  // x0
    void* v38;  // x0
    void* v39;  // x0
    unsigned long long v22;  // x27
    void* v40;  // x0
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
    void* v3;  // [bp-0x80]
    unsigned long v4;  // [bp-0x78]
    unsigned long v5;  // [bp-0x70]
    unsigned long v6;  // [bp-0x68]
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
    if (!(g_1fab13c & 1))
    {
        sub_f7d92c(&g_1eee138);
        sub_f7d92c(&g_1eefb08);
        sub_f7d92c(&g_1f0fca8);
        sub_f7d92c(&g_1f0bf38);
        sub_f7d92c(&g_1f0cd28);
        sub_f7d92c(&g_1f08570);
        sub_f7d92c("Y#");
        sub_f7d92c(&g_1f15c68);
        g_1fab13c = 1;
    }
    v0 = a0;
    Object__ctor(a0, 0);
    sub_f7d9d4(g_1eee138, 3);
    v6 = (unsigned long long)GamepadProfile_JoystickSource__Axes(0, 1, 1, 0);
    v5 = (unsigned long long)GamepadProfile_JoystickSource__Axes(3, 1, 4, 0);
    v4 = (unsigned long long)GamepadProfile_JoystickSource__Axes(5, 1, 6, 1);
    v3 = GamepadProfile_KeySource__Key(0);
    v2 = GamepadProfile_KeySource__Key(1);
    v1 = GamepadProfile_KeySource__Key(2);
    v31 = GamepadProfile_KeySource__Key(3);
    v32 = GamepadProfile_KeySource__Key(6);
    v33 = GamepadProfile_KeySource__Key(7);
    v34 = GamepadProfile_KeySource__Key(4);
    v35 = GamepadProfile_KeySource__Key(5);
    v36 = GamepadProfile_KeySource__PlusAxis(8);
    v37 = GamepadProfile_KeySource__PlusAxis(9);
    v38 = GamepadProfile_KeySource__Key(8);
    v39 = GamepadProfile_KeySource__Key(9);
    v40 = sub_f7db70(g_1eefb08);
    GamepadProfile__ctor(v40, g_1f0fca8, g_1f15c68, 0, 0, 0, v6, v5, v4, v3, v2, v1, v31, v32, v33, v34, v35, v36, v37, v38, v39); /* do not return */
}
```
