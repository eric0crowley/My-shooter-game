# Native pseudocode: GamepadProfile.GenericProfile

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `GamepadProfile.GenericProfile.ctor` — RVA `0xc30928`

- Decompiled symbol: `GamepadProfile_GenericProfile_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `324` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned long long field_10;
    char field_18;
} struct_0;

extern long long g_1f06220;
extern long long g_1f0a6e0;
extern char g_1fab134;

void GamepadProfile_GenericProfile_ctor(void* a0)
{
    unsigned long long v16;  // x30
    unsigned long long v17;  // x28
    unsigned long long v26;  // x19
    void* v27;  // x0
    void* v28;  // x0
    struct_0 *v29;  // x0
    struct_0 *v30;  // x0
    struct_0 *v31;  // x0
    struct_0 *v32;  // x0
    struct_0 *v33;  // x0
    struct_0 *v34;  // x0
    struct_0 *v35;  // x0
    unsigned long long v18;  // x27
    struct_0 *v36;  // x0
    struct_0 *v37;  // x0
    struct_0 *v38;  // x0
    unsigned long long v19;  // x26
    unsigned long long v20;  // x25
    unsigned long long v21;  // x24
    unsigned long long v22;  // x23
    unsigned long long v23;  // x22
    unsigned long long v24;  // x21
    unsigned long long v25;  // x20
    unsigned long v0;  // [bp-0x80]
    unsigned long v1;  // [bp-0x78]
    unsigned long v2;  // [bp-0x70]
    char *v3;  // [bp-0x60]
    unsigned long long v4;  // [bp-0x58]
    unsigned long long v5;  // [bp-0x50]
    unsigned long long v6;  // [bp-0x48]
    unsigned long long v7;  // [bp-0x40]
    unsigned long long v8;  // [bp-0x38]
    unsigned long long v9;  // [bp-0x30]
    unsigned long long v10;  // [bp-0x28]
    unsigned long long v11;  // [bp-0x20]
    unsigned long long v12;  // [bp-0x18]
    unsigned long long v13;  // [bp-0x10]
    unsigned long long v14;  // [bp-0x8]
    char v15;  // [bp+0x0]

    v3 = &v15;
    v4 = v16;
    v5 = v17;
    v6 = v18;
    v7 = v19;
    v8 = v20;
    v9 = v21;
    v10 = v22;
    v11 = v23;
    v12 = v24;
    v13 = v25;
    v14 = v26;
    if (!(g_1fab134 & 1))
    {
        sub_f7d92c(&g_1f06220);
        sub_f7d92c(&g_1f0a6e0);
        g_1fab134 = 1;
    }
    v2 = (unsigned long long)GamepadProfile_JoystickSource__Axes(0, 1, 1, 0);
    v1 = (unsigned long long)GamepadProfile_JoystickSource__Empty();
    v0 = (unsigned long long)GamepadProfile_JoystickSource__Empty();
    v27 = GamepadProfile_KeySource__Key(0);
    v28 = GamepadProfile_KeySource__Key(1);
    v29 = GamepadProfile_KeySource__Empty();
    v30 = GamepadProfile_KeySource__Empty();
    v31 = GamepadProfile_KeySource__Empty();
    v32 = GamepadProfile_KeySource__Empty();
    v33 = GamepadProfile_KeySource__Empty();
    v34 = GamepadProfile_KeySource__Empty();
    v35 = GamepadProfile_KeySource__Empty();
    v36 = GamepadProfile_KeySource__Empty();
    v37 = GamepadProfile_KeySource__Empty();
    v38 = GamepadProfile_KeySource__Empty();
    GamepadProfile__ctor(a0, g_1f0a6e0, g_1f06220, 0, 0, 0, v2, v1, v0, v27, v28, v29, v30, v31, v32, v33, v34, v35, v36, v37, v38); /* do not return */
}
```

## `GamepadProfile.GenericProfile.ctor` — RVA `0xc30a6c`

- Decompiled symbol: `GamepadProfile_GenericProfile_ctor`
- Metadata signature: `public void .ctor(GamepadProfile.JoystickSource leftStick, GamepadProfile.JoystickSource rightStick, GamepadProfile.JoystickSource dpad, GamepadProfile.KeySource keyFaceD, GamepadProfile.KeySource keyFaceR, GamepadProfile.KeySource keyFaceL, GamepadProfile.KeySource keyFaceU, GamepadProfile.KeySource keySelect, GamepadProfile.KeySource keyStart, GamepadProfile.KeySource keyL1, GamepadProfile.KeySource keyR1, GamepadProfile.KeySource keyL2, GamepadProfile.KeySource keyR2, GamepadProfile.KeySource keyL3, GamepadProfile.KeySource keyR3) { }`
- Native interval: `260` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned long long field_10;
    char field_18;
} struct_0;

extern long long g_1f06220;
extern long long g_1f0a6e0;
extern char g_1fab135;

void GamepadProfile_GenericProfile_ctor(void* a0, long long a1, long long a2, long long a3, struct_0 *a4, struct_0 *a5, struct_0 *a6, unsigned int a7, struct_0 *a8, struct_0 *a9, struct_0 *a10, struct_0 *a11, struct_0 *a12, struct_0 *a13, struct_0 *a14, struct_0 *a15)
{
    unsigned long long v14;  // x30
    unsigned long long v15;  // x28
    unsigned long long v24;  // x19
    long long v25;  // x10
    long long v26;  // x9
    unsigned long long v16;  // x27
    unsigned long long v17;  // x26
    unsigned long long v18;  // x25
    unsigned long long v19;  // x24
    unsigned long long v20;  // x23
    unsigned long long v21;  // x22
    unsigned long long v22;  // x21
    unsigned long long v23;  // x20
    long long v0;  // [bp-0x78]
    long long v1;  // [bp-0x70]
    unsigned long v2;  // [bp-0x60]
    unsigned long long v3;  // [bp-0x58]
    unsigned long long v4;  // [bp-0x50]
    unsigned long long v5;  // [bp-0x48]
    unsigned long long v6;  // [bp-0x40]
    unsigned long long v7;  // [bp-0x38]
    unsigned long long v8;  // [bp-0x30]
    unsigned long long v9;  // [bp-0x28]
    unsigned long long v10;  // [bp-0x20]
    unsigned long long v11;  // [bp-0x18]
    unsigned long long v12;  // [bp-0x10]
    unsigned long long v13;  // [bp-0x8]

    v2 = &vvar_8;
    v3 = v14;
    v4 = v15;
    v5 = v16;
    v6 = v17;
    v7 = v18;
    v8 = v19;
    v9 = v20;
    v10 = v21;
    v11 = v22;
    v12 = v23;
    v13 = v24;
    v25 = a2;
    v26 = a1;
    if (!(g_1fab135 & 1))
    {
        v0 = v26;
        v1 = v25;
        sub_f7d92c(&g_1f06220);
        sub_f7d92c(&g_1f0a6e0);
        v25 = v1;
        v26 = v0;
        g_1fab135 = 1;
    }
    GamepadProfile__ctor(a0, g_1f0a6e0, g_1f06220, 0, 0, 0, v26, v25, a3, a4, a5, a6, a7, vvar_8, a9, a10, a11, a12, a13, a14, a15); /* do not return */
}
```
