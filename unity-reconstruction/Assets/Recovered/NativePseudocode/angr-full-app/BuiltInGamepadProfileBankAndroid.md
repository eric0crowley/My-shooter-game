# Native pseudocode: BuiltInGamepadProfileBankAndroid

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `BuiltInGamepadProfileBankAndroid.ctor` — RVA `0xc30e4c`

- Decompiled symbol: `BuiltInGamepadProfileBankAndroid_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `2884` bytes
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
extern long long g_1f07010;
extern long long g_1f07d08;
extern long long g_1f07d10;
extern long long g_1f09bf8;
extern long long g_1f0bf38;
extern long long g_1f0c228;
extern long long g_1f0cd28;
extern long long g_1f0db08;
extern long long g_1f0fca8;
extern char g_1fab138;

void BuiltInGamepadProfileBankAndroid_ctor(void* ptr)
{
    unsigned long long v19;  // x30
    unsigned long long v20;  // x28
    unsigned long long v29;  // x19
    void* v30;  // x0
    unsigned int v31;  // w0
    void* v32;  // x0
    void* v33;  // x0
    void* v34;  // x0
    void* v35;  // x0
    void* v36;  // x0
    void* v37;  // x0
    void* v38;  // x0
    unsigned long long v21;  // x27
    void* v39;  // x0
    unsigned long v40;  // x0
    unsigned long v41;  // x24
    void* v42;  // x0
    struct_0 *v43;  // x0
    void* v44;  // x0
    void* v45;  // x0
    void* v46;  // x0
    void* v47;  // x0
    void* v48;  // x0
    unsigned long long v22;  // x26
    void* v49;  // x0
    void* v50;  // x0
    void* v51;  // x0
    void* v52;  // x0
    unsigned long long v23;  // x25
    unsigned long long v24;  // x24
    unsigned long long v25;  // x23
    unsigned long long v26;  // x22
    unsigned long long v27;  // x21
    unsigned long long v28;  // x20
    void* v0;  // [bp-0x98]
    void* v1;  // [bp-0x90]
    void* v2;  // [bp-0x88], Other Possible Types: unsigned long
    unsigned long v3;  // [bp-0x80]
    unsigned long v4;  // [bp-0x78]
    unsigned long v5;  // [bp-0x68], Other Possible Types: unsigned long long
    char *v6;  // [bp-0x60]
    unsigned long long v7;  // [bp-0x58]
    unsigned long long v8;  // [bp-0x50]
    unsigned long long v9;  // [bp-0x48]
    unsigned long long v10;  // [bp-0x40]
    unsigned long long v11;  // [bp-0x38]
    unsigned long long v12;  // [bp-0x30]
    unsigned long long v13;  // [bp-0x28]
    unsigned long long v14;  // [bp-0x20]
    unsigned long long v15;  // [bp-0x18]
    unsigned long long v16;  // [bp-0x10]
    unsigned long long v17;  // [bp-0x8]
    char v18;  // [bp+0x0]

    v6 = &v18;
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
    v17 = v29;
    if (!(g_1fab138 & 1))
    {
        sub_f7d92c(&g_1eee138);
        sub_f7d92c(&g_1eefb08);
        sub_f7d92c("}j");
        sub_f7d92c(&g_1f0db08);
        sub_f7d92c(&g_1f0fca8);
        sub_f7d92c(&g_1f0bf38);
        sub_f7d92c(&g_1f0cd28);
        sub_f7d92c(&g_1f0c228);
        sub_f7d92c(&g_1f09bf8);
        sub_f7d92c(&g_1f07010);
        sub_f7d92c("Y#");
        sub_f7d92c(&g_1f07d10);
        sub_f7d92c("1\n");
        sub_f7d92c(&g_1f07d08);
        g_1fab138 = 1;
    }
    Object__ctor(ptr, 0);
    v5 = (unsigned long long)GamepadProfile_JoystickSource__Axes(0, 1, 1, 0);
    v4 = (unsigned long long)GamepadProfile_JoystickSource__Axes(2, 1, 3, 0);
    v3 = (unsigned long long)GamepadProfile_JoystickSource__Axes(4, 1, 5, 0);
    v2 = GamepadProfile_KeySource__Key(0);
    v1 = GamepadProfile_KeySource__Key(1);
    v30 = GamepadProfile_KeySource__Key(2);
    v31 = (unsigned int)GamepadProfile_KeySource__Key(3);
    v32 = GamepadProfile_KeySource__Key(11);
    v33 = GamepadProfile_KeySource__Key(10);
    v34 = GamepadProfile_KeySource__Key(4);
    v35 = GamepadProfile_KeySource__Key(5);
    v36 = GamepadProfile_KeySource__KeyAndPlusAxis(6, 6);
    v37 = GamepadProfile_KeySource__KeyAndPlusAxis(7, 7);
    v38 = GamepadProfile_KeySource__Key(8);
    v39 = GamepadProfile_KeySource__Key(9);
    v40 = sub_f7db70(g_1ef3210);
    v41 = v40;
    GamepadProfile_GenericProfile__ctor(v40, v5, v4, v3, v2, v1, v30, v31, v32, v33, v34, v35, v36, v37, v38, v39);
    *((unsigned long *)&ptr[24]) = v41;
    sub_f7d8d0(ptr + 24, v41);
    v5 = sub_f7d9d4(g_1eee138, 6);
    v4 = (unsigned long long)GamepadProfile_JoystickSource__Axes(0, 1, 1, 0);
    v3 = (unsigned long long)GamepadProfile_JoystickSource__Axes(2, 1, 3, 0);
    v2 = (unsigned long long)GamepadProfile_JoystickSource__Axes(4, 1, 5, 0);
    v1 = GamepadProfile_KeySource__Key(0);
    v0 = GamepadProfile_KeySource__Key(1);
    v42 = GamepadProfile_KeySource__Key(2);
    v43 = GamepadProfile_KeySource__Key(3);
    v44 = GamepadProfile_KeySource__Key(11);
    v45 = GamepadProfile_KeySource__Key(10);
    v46 = GamepadProfile_KeySource__Key(4);
    v47 = GamepadProfile_KeySource__Key(5);
    v48 = GamepadProfile_KeySource__Key(6);
    v49 = GamepadProfile_KeySource__Key(7);
    v50 = GamepadProfile_KeySource__Key(8);
    v51 = GamepadProfile_KeySource__Key(9);
    v52 = sub_f7db70(g_1eefb08);
    GamepadProfile__ctor(v52, g_1f07d10, g_1f07d08, 0, 0, 0, v4, v3, v2, v1, v0, v42, v43, v44, v45, v46, v47, v48, v49, v50, v51); /* do not return */
}
```
