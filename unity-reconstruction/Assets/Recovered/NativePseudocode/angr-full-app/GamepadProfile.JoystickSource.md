# Native pseudocode: GamepadProfile.JoystickSource

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `GamepadProfile.JoystickSource.ctor` — RVA `0xc2fcfc`

- Decompiled symbol: `GamepadProfile_JoystickSource_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `276` bytes
- Result: `pseudocode`
- Heuristic layout hint: `GamepadProfile_JoystickSource_Recovered` matched 4 offsets against `GamepadProfile.JoystickSource` metadata (confidence 1.00).

```c
typedef struct GamepadProfile_JoystickSource_Recovered {
    char padding_0[16];
    struct struct_1 *keyU;
    struct struct_2 *keyD;
    struct struct_3 *keyR;
    struct struct_4 *keyL;
} GamepadProfile_JoystickSource_Recovered;

typedef struct struct_0 {
    char padding_0[16];
    unsigned long long field_10;
    char field_18;
} struct_0;

typedef struct struct_6 {
    char padding_0[16];
    unsigned long long field_10;
    char field_18;
} struct_6;

typedef struct struct_7 {
    char padding_0[16];
    unsigned long long field_10;
    char field_18;
} struct_7;

typedef struct struct_8 {
    char padding_0[16];
    unsigned long long field_10;
    char field_18;
} struct_8;

typedef struct struct_1 {
    char padding_0[16];
    unsigned long long field_10;
    char field_18;
} struct_1;

typedef struct struct_2 {
    char padding_0[16];
    unsigned long long field_10;
    char field_18;
} struct_2;

typedef struct struct_3 {
    char padding_0[16];
    unsigned long long field_10;
    char field_18;
} struct_3;

typedef struct struct_4 {
    char padding_0[16];
    unsigned long long field_10;
    char field_18;
} struct_4;

extern long long g_1ef3220;
extern char g_1fab12a;

void GamepadProfile_JoystickSource_ctor(struct_5 *ptr7)
{
    unsigned long long v5;  // x30
    unsigned long long v6;  // x22
    struct_5 *ptr4;  // x0
    struct_8 *ptr;  // x20
    unsigned long long v7;  // x21
    unsigned long long v8;  // x20
    unsigned long long v9;  // x19
    struct_0 *p;  // x20
    struct_5 *ptr5;  // x0
    struct_6 *addr;  // x20
    struct_5 *ptr6;  // x0
    struct_7 *ptr3;  // x20
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
    if (!(g_1fab12a & 1))
    {
        sub_f7d92c(&g_1ef3220);
        g_1fab12a = 1;
    }
    Object__ctor(ptr7, 0);
    p = sub_f7db70(g_1ef3220);
    Object__ctor(p, 0);
    ptr5 = ptr7;
    p->field_10 = 18446744073709551615 CONCAT 18446744073709551615;
    p->field_18 = 1;
    ptr5->field_18 = p;
    sub_f7d8d0((struct GamepadProfile_JoystickSource_Recovered *)&ptr5->field_18, p);
    addr = sub_f7db70(g_1ef3220);
    Object__ctor(addr, 0);
    ptr6 = ptr7;
    addr->field_10 = 18446744073709551615 CONCAT 18446744073709551615;
    addr->field_18 = 1;
    ptr6->field_10 = addr;
    sub_f7d8d0((struct GamepadProfile_JoystickSource_Recovered *)&ptr6->field_10, addr);
    ptr3 = sub_f7db70(g_1ef3220);
    Object__ctor(ptr3, 0);
    ptr4 = ptr7;
    ptr3->field_10 = 18446744073709551615 CONCAT 18446744073709551615;
    ptr3->field_18 = 1;
    ptr4->field_28 = ptr3;
    sub_f7d8d0((struct GamepadProfile_JoystickSource_Recovered *)&ptr4->field_28, ptr3);
    ptr = sub_f7db70(g_1ef3220);
    Object__ctor(ptr, 0);
    ptr->field_10 = 18446744073709551615 CONCAT 18446744073709551615;
    ptr->field_18 = 1;
    ptr7->field_20 = ptr;
    sub_f7d8d0();
    return;
}
```

## `GamepadProfile.JoystickSource.IsDuplicateOf` — RVA `0xc3010c`

- Decompiled symbol: `GamepadProfile_JoystickSource_IsDuplicateOf`
- Metadata signature: `public bool IsDuplicateOf(GamepadProfile.JoystickSource a) { }`
- Native interval: `124` bytes
- Result: `pseudocode`
- Heuristic layout hint: `GamepadProfile_JoystickSource_Recovered` matched 2 offsets against `GamepadProfile.JoystickSource` metadata (confidence 0.67).

```c
typedef struct GamepadProfile_JoystickSource_Recovered {
    char padding_0[16];
    unsigned int keyU;
    unsigned int field_14;
    char keyD;
} GamepadProfile_JoystickSource_Recovered;

typedef struct struct_1 {
    char padding_0[24];
    char field_18;
} struct_1;

unsigned long long GamepadProfile_JoystickSource_IsDuplicateOf(struct_1 **a0, struct_0 **a1, unsigned long a2, unsigned long a3, unsigned long a4, unsigned long a5, unsigned long a6, unsigned long a7)
{
    unsigned long long v0;  // x0

    if (a1 && a0[3])
    {
        if (!((char)GamepadProfile_KeySource__IsDuplicateOf(a0[3], a1[3]) & 1))
        {
            return 0;
        }
        else if (a0[2])
        {
            if (!((char)GamepadProfile_KeySource__IsDuplicateOf(a0[2], a1[2]) & 1))
            {
                return 0;
            }
            else if (a0[5])
            {
                if (!((char)GamepadProfile_KeySource__IsDuplicateOf(a0[5], a1[5]) & 1))
                {
                    return 0;
                }
                else if (a0[4])
                {
                    v0 = GamepadProfile_KeySource__IsDuplicateOf(a0[4], a1[4]);
                    return GamepadProfile_KeySource__IsDuplicateOf(a0[4], a1[4]);
                }
            }
        }
    }
    sub_f7db74();
}
```

## `GamepadProfile.JoystickSource.Empty` — RVA `0xc3047c`

- Decompiled symbol: `GamepadProfile_JoystickSource_Empty`
- Metadata signature: `public static GamepadProfile.JoystickSource Empty() { }`
- Native interval: `80` bytes
- Result: `pseudocode`
- Heuristic layout hint: `GamepadProfile_JoystickSource_Recovered` matched 4 offsets against `GamepadProfile.JoystickSource` metadata (confidence 1.00).

```c
typedef struct GamepadProfile_JoystickSource_Recovered {
    char padding_0[16];
    struct struct_1 *keyU;
    struct struct_2 *keyD;
    struct struct_3 *keyR;
    struct struct_4 *keyL;
} GamepadProfile_JoystickSource_Recovered;

typedef struct struct_1 {
    char padding_0[16];
    unsigned long long field_10;
    char field_18;
} struct_1;

typedef struct struct_2 {
    char padding_0[16];
    unsigned long long field_10;
    char field_18;
} struct_2;

typedef struct struct_3 {
    char padding_0[16];
    unsigned long long field_10;
    char field_18;
} struct_3;

typedef struct struct_4 {
    char padding_0[16];
    unsigned long long field_10;
    char field_18;
} struct_4;

extern long long g_1ef3218;
extern char g_1fab12d;

void GamepadProfile_JoystickSource_Empty(void)
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
    if (!(g_1fab12d & 1))
    {
        sub_f7d92c(&g_1ef3218);
        g_1fab12d = 1;
    }
    GamepadProfile_JoystickSource__ctor(sub_f7db70(g_1ef3218)); /* do not return */
}
```

## `GamepadProfile.JoystickSource.Dpad` — RVA `0xc304f4`

- Decompiled symbol: `GamepadProfile_JoystickSource_Dpad`
- Metadata signature: `public static GamepadProfile.JoystickSource Dpad(int keyU, int keyR, int keyD, int keyL) { }`
- Native interval: `200` bytes
- Result: `pseudocode`
- Heuristic layout hint: `GamepadProfile_JoystickSource_Recovered` matched 4 offsets against `GamepadProfile.JoystickSource` metadata (confidence 1.00).

```c
typedef struct GamepadProfile_JoystickSource_Recovered {
    char padding_0[16];
    struct struct_1 *keyU;
    struct struct_2 *keyD;
    struct struct_3 *keyR;
    struct struct_4 *keyL;
} GamepadProfile_JoystickSource_Recovered;

typedef struct struct_1 {
    char padding_0[16];
    unsigned long long field_10;
    char field_18;
} struct_1;

typedef struct struct_2 {
    char padding_0[16];
    unsigned long long field_10;
    char field_18;
} struct_2;

typedef struct struct_3 {
    char padding_0[16];
    unsigned long long field_10;
    char field_18;
} struct_3;

typedef struct struct_4 {
    char padding_0[16];
    unsigned long long field_10;
    char field_18;
} struct_4;

extern long long g_1ef3218;
extern char g_1fab12b;

void GamepadProfile_JoystickSource_Dpad(unsigned long a0, unsigned long a1, unsigned long a2, unsigned long a3)
{
    unsigned long long v7;  // x30
    unsigned long long v8;  // x24
    unsigned long long v9;  // x23
    unsigned long long v10;  // x22
    unsigned long long v11;  // x21
    unsigned long long v12;  // x20
    unsigned long long v13;  // x19
    unsigned long long v0;  // [bp-0x40]
    unsigned long long v1;  // [bp-0x30]
    unsigned long long v2;  // [bp-0x28]
    unsigned long long v3;  // [bp-0x20]
    unsigned long long v4;  // [bp-0x18]
    unsigned long long v5;  // [bp-0x10]
    unsigned long long v6;  // [bp-0x8]

    v0 = v7;
    v1 = v8;
    v2 = v9;
    v3 = v10;
    v4 = v11;
    v5 = v12;
    v6 = v13;
    if (!(g_1fab12b & 1))
    {
        sub_f7d92c(&g_1ef3218);
        g_1fab12b = 1;
    }
    GamepadProfile_JoystickSource__ctor(sub_f7db70(g_1ef3218)); /* do not return */
}
```

## `GamepadProfile.JoystickSource.Axes` — RVA `0xc305d0`

- Decompiled symbol: `GamepadProfile_JoystickSource_Axes`
- Metadata signature: `public static GamepadProfile.JoystickSource Axes(int horzAxisId, bool horzPositiveRight, int vertAxisId, bool vertPositiveUp) { }`
- Native interval: `200` bytes
- Result: `pseudocode`
- Heuristic layout hint: `GamepadProfile_JoystickSource_Recovered` matched 4 offsets against `GamepadProfile.JoystickSource` metadata (confidence 1.00).

```c
typedef struct GamepadProfile_JoystickSource_Recovered {
    char padding_0[16];
    struct struct_1 *keyU;
    struct struct_2 *keyD;
    struct struct_3 *keyR;
    struct struct_4 *keyL;
} GamepadProfile_JoystickSource_Recovered;

typedef struct struct_1 {
    char padding_0[16];
    unsigned long long field_10;
    char field_18;
} struct_1;

typedef struct struct_2 {
    char padding_0[16];
    unsigned long long field_10;
    char field_18;
} struct_2;

typedef struct struct_3 {
    char padding_0[16];
    unsigned long long field_10;
    char field_18;
} struct_3;

typedef struct struct_4 {
    char padding_0[16];
    unsigned long long field_10;
    char field_18;
} struct_4;

extern long long g_1ef3218;
extern char g_1fab12c;

void GamepadProfile_JoystickSource_Axes(unsigned long a0, unsigned long a1, unsigned long a2, unsigned long a3)
{
    unsigned long long v7;  // x30
    unsigned long long v8;  // x24
    unsigned long long v9;  // x23
    unsigned long long v10;  // x22
    unsigned long long v11;  // x21
    unsigned long long v12;  // x20
    unsigned long long v13;  // x19
    unsigned long long v0;  // [bp-0x40]
    unsigned long long v1;  // [bp-0x30]
    unsigned long long v2;  // [bp-0x28]
    unsigned long long v3;  // [bp-0x20]
    unsigned long long v4;  // [bp-0x18]
    unsigned long long v5;  // [bp-0x10]
    unsigned long long v6;  // [bp-0x8]

    v0 = v7;
    v1 = v8;
    v2 = v9;
    v3 = v10;
    v4 = v11;
    v5 = v12;
    v6 = v13;
    if (!(g_1fab12c & 1))
    {
        sub_f7d92c(&g_1ef3218);
        g_1fab12c = 1;
    }
    GamepadProfile_JoystickSource__ctor(sub_f7db70(g_1ef3218)); /* do not return */
}
```
