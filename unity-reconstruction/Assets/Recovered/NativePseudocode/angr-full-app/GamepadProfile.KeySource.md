# Native pseudocode: GamepadProfile.KeySource

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `GamepadProfile.KeySource.Empty` — RVA `0xc2fe10`

- Decompiled symbol: `GamepadProfile_KeySource_Empty`
- Metadata signature: `public static GamepadProfile.KeySource Empty() { }`
- Native interval: `100` bytes
- Result: `pseudocode`
- Heuristic layout hint: `GamepadProfile_KeySource_Recovered` matched 2 offsets against `GamepadProfile.KeySource` metadata (confidence 1.00).

```c
typedef struct GamepadProfile_KeySource_Recovered {
    char padding_0[16];
    unsigned long long keyId;
    char axisSign;
} GamepadProfile_KeySource_Recovered;

extern long long g_1ef3220;
extern char g_1fab133;

struct_0 * GamepadProfile_KeySource_Empty(void)
{
    struct_0 *ptr;  // x19

    if (!(g_1fab133 & 1))
    {
        sub_f7d92c(&g_1ef3220);
        g_1fab133 = 1;
    }
    ptr = sub_f7db70(g_1ef3220);
    Object__ctor(ptr, 0);
    ptr->field_10 = 18446744073709551615 CONCAT 18446744073709551615;
    ptr->field_18 = 1;
    return ptr;
}
```

## `GamepadProfile.KeySource.IsDuplicateOf` — RVA `0xc300c0`

- Decompiled symbol: `GamepadProfile_KeySource_IsDuplicateOf`
- Metadata signature: `public bool IsDuplicateOf(GamepadProfile.KeySource a) { }`
- Native interval: `76` bytes
- Result: `pseudocode`
- Heuristic layout hint: `GamepadProfile_KeySource_Recovered` matched 3 offsets against `GamepadProfile.KeySource` metadata (confidence 1.00).

```c
typedef struct GamepadProfile_KeySource_Recovered {
    char padding_0[16];
    unsigned int keyId;
    unsigned int axisId;
    char axisSign;
} GamepadProfile_KeySource_Recovered;

typedef struct struct_1 {
    char padding_0[24];
    char field_18;
} struct_1;

unsigned long long GamepadProfile_KeySource_IsDuplicateOf(struct_1 *a0, struct_0 *a1)
{
    unsigned long long v0;  // x0

    if (a1)
    {
        if (*((int *)&a0->padding_0[16]) != a1->field_10 || *((int *)&a0->padding_0[20]) != a1->field_14)
            return 0;
        if (a0->field_18 != a1->field_18)
            v0 = 0;
        else
            v0 = 1;
        return v0;
        return 0;
    }
    sub_f7db74();
}
```

## `GamepadProfile.KeySource.ctor` — RVA `0xc304cc`

- Decompiled symbol: `GamepadProfile_KeySource_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `40` bytes
- Result: `pseudocode`
- Heuristic layout hint: `GamepadProfile_KeySource_Recovered` matched 2 offsets against `GamepadProfile.KeySource` metadata (confidence 1.00).

```c
typedef struct GamepadProfile_KeySource_Recovered {
    char padding_0[16];
    unsigned long long keyId;
    char axisSign;
} GamepadProfile_KeySource_Recovered;

void GamepadProfile_KeySource_ctor(struct_0 *ptr)
{
    Object__ctor();
    ptr->field_10 = 18446744073709551615 CONCAT 18446744073709551615;
    ptr->field_18 = 1;
    return;
}
```

## `GamepadProfile.KeySource.SetKey` — RVA `0xc305bc`

- Decompiled symbol: `GamepadProfile_KeySource_SetKey`
- Metadata signature: `public void SetKey(int keyId) { }`
- Native interval: `20` bytes
- Result: `pseudocode`
- Heuristic layout hint: `GamepadProfile_KeySource_Recovered` matched 3 offsets against `GamepadProfile.KeySource` metadata (confidence 1.00).

```c
typedef struct GamepadProfile_KeySource_Recovered {
    char padding_0[16];
    unsigned int keyId;
    unsigned int axisId;
    char axisSign;
} GamepadProfile_KeySource_Recovered;

struct_0 * GamepadProfile_KeySource_SetKey(struct_0 *ptr, unsigned int a1)
{
    ptr->field_10 = a1;
    ptr->field_14 = 4294967295;
    ptr->field_18 = 1;
    return ptr;
}
```

## `GamepadProfile.KeySource.SetAxis` — RVA `0xc30698`

- Decompiled symbol: `GamepadProfile_KeySource_SetAxis`
- Metadata signature: `public void SetAxis(int axisId, bool axisSign) { }`
- Native interval: `20` bytes
- Result: `pseudocode`
- Heuristic layout hint: `GamepadProfile_KeySource_Recovered` matched 3 offsets against `GamepadProfile.KeySource` metadata (confidence 1.00).

```c
typedef struct GamepadProfile_KeySource_Recovered {
    char padding_0[16];
    unsigned int keyId;
    unsigned int axisId;
    char axisSign;
} GamepadProfile_KeySource_Recovered;

struct_0 * GamepadProfile_KeySource_SetAxis(struct_0 *ptr, unsigned int a1, char a2)
{
    ptr->field_10 = 4294967295;
    ptr->field_14 = a1;
    ptr->field_18 = a2 & 1;
    return ptr;
}
```

## `GamepadProfile.KeySource.IsEmpty` — RVA `0xc306ac`

- Decompiled symbol: `GamepadProfile_KeySource_IsEmpty`
- Metadata signature: `public bool IsEmpty() { }`
- Native interval: `28` bytes
- Result: `pseudocode`

```c
unsigned int GamepadProfile_KeySource_IsEmpty(unsigned int *a0)
{
    if (((char)(a0[4] >> 31) & 1))
        return (a0[5] * 2 | a0[5] >> 31) & 1;
    return 0;
}
```

## `GamepadProfile.KeySource.Clear` — RVA `0xc306c8`

- Decompiled symbol: `GamepadProfile_KeySource_Clear`
- Metadata signature: `public void Clear() { }`
- Native interval: `20` bytes
- Result: `pseudocode`
- Heuristic layout hint: `GamepadProfile_KeySource_Recovered` matched 2 offsets against `GamepadProfile.KeySource` metadata (confidence 1.00).

```c
typedef struct GamepadProfile_KeySource_Recovered {
    char padding_0[16];
    unsigned long long keyId;
    char axisSign;
} GamepadProfile_KeySource_Recovered;

struct_0 * GamepadProfile_KeySource_Clear(struct_0 *ptr)
{
    ptr->field_10 = 18446744073709551615 CONCAT 18446744073709551615;
    ptr->field_18 = 1;
    return ptr;
}
```

## `GamepadProfile.KeySource.ctor` — RVA `0xc306dc`

- Decompiled symbol: `GamepadProfile_KeySource_ctor`
- Metadata signature: `private void .ctor(int keyId, int axisId, bool axisSign) { }`
- Native interval: `60` bytes
- Result: `pseudocode`
- Heuristic layout hint: `GamepadProfile_KeySource_Recovered` matched 3 offsets against `GamepadProfile.KeySource` metadata (confidence 1.00).

```c
typedef struct GamepadProfile_KeySource_Recovered {
    char padding_0[16];
    unsigned int keyId;
    unsigned int axisId;
    char axisSign;
} GamepadProfile_KeySource_Recovered;

void GamepadProfile_KeySource_ctor(struct_0 *ptr, unsigned int a1, unsigned int a2, char a3)
{
    Object__ctor();
    ptr->field_10 = a1;
    ptr->field_14 = a2;
    ptr->field_18 = a3 & 1;
    return;
}
```

## `GamepadProfile.KeySource.Key` — RVA `0xc30718`

- Decompiled symbol: `GamepadProfile_KeySource_Key`
- Metadata signature: `public static GamepadProfile.KeySource Key(int keyId) { }`
- Native interval: `104` bytes
- Result: `pseudocode`
- Heuristic layout hint: `GamepadProfile_KeySource_Recovered` matched 3 offsets against `GamepadProfile.KeySource` metadata (confidence 1.00).

```c
typedef struct GamepadProfile_KeySource_Recovered {
    char padding_0[16];
    unsigned int keyId;
    unsigned int axisId;
    char axisSign;
} GamepadProfile_KeySource_Recovered;

extern long long g_1ef3220;
extern char g_1fab12e;

struct_0 * GamepadProfile_KeySource_Key(unsigned int a0)
{
    struct_0 *ptr;  // x20

    if (!(g_1fab12e & 1))
    {
        sub_f7d92c(&g_1ef3220);
        g_1fab12e = 1;
    }
    ptr = sub_f7db70(g_1ef3220);
    Object__ctor(ptr, 0);
    ptr->field_10 = a0;
    ptr->field_14 = 4294967295;
    ptr->field_18 = 1;
    return ptr;
}
```

## `GamepadProfile.KeySource.PlusAxis` — RVA `0xc30780`

- Decompiled symbol: `GamepadProfile_KeySource_PlusAxis`
- Metadata signature: `public static GamepadProfile.KeySource PlusAxis(int axisId) { }`
- Native interval: `104` bytes
- Result: `pseudocode`
- Heuristic layout hint: `GamepadProfile_KeySource_Recovered` matched 3 offsets against `GamepadProfile.KeySource` metadata (confidence 1.00).

```c
typedef struct GamepadProfile_KeySource_Recovered {
    char padding_0[16];
    unsigned int keyId;
    unsigned int axisId;
    char axisSign;
} GamepadProfile_KeySource_Recovered;

extern long long g_1ef3220;
extern char g_1fab12f;

struct_0 * GamepadProfile_KeySource_PlusAxis(unsigned int a0)
{
    struct_0 *ptr;  // x20

    if (!(g_1fab12f & 1))
    {
        sub_f7d92c(&g_1ef3220);
        g_1fab12f = 1;
    }
    ptr = sub_f7db70(g_1ef3220);
    Object__ctor(ptr, 0);
    ptr->field_10 = 4294967295;
    ptr->field_14 = a0;
    ptr->field_18 = 1;
    return ptr;
}
```

## `GamepadProfile.KeySource.MinusAxis` — RVA `0xc307e8`

- Decompiled symbol: `GamepadProfile_KeySource_MinusAxis`
- Metadata signature: `public static GamepadProfile.KeySource MinusAxis(int axisId) { }`
- Native interval: `100` bytes
- Result: `pseudocode`
- Heuristic layout hint: `GamepadProfile_KeySource_Recovered` matched 3 offsets against `GamepadProfile.KeySource` metadata (confidence 1.00).

```c
typedef struct GamepadProfile_KeySource_Recovered {
    char padding_0[16];
    unsigned int keyId;
    unsigned int axisId;
    char axisSign;
} GamepadProfile_KeySource_Recovered;

extern long long g_1ef3220;
extern char g_1fab130;

struct_0 * GamepadProfile_KeySource_MinusAxis(unsigned int a0)
{
    struct_0 *ptr;  // x20

    if (!(g_1fab130 & 1))
    {
        sub_f7d92c(&g_1ef3220);
        g_1fab130 = 1;
    }
    ptr = sub_f7db70(g_1ef3220);
    Object__ctor(ptr, 0);
    ptr->field_10 = 4294967295;
    ptr->field_14 = a0;
    ptr->field_18 = 0;
    return ptr;
}
```

## `GamepadProfile.KeySource.KeyAndPlusAxis` — RVA `0xc3084c`

- Decompiled symbol: `GamepadProfile_KeySource_KeyAndPlusAxis`
- Metadata signature: `public static GamepadProfile.KeySource KeyAndPlusAxis(int keyId, int axisId) { }`
- Native interval: `112` bytes
- Result: `pseudocode`
- Heuristic layout hint: `GamepadProfile_KeySource_Recovered` matched 3 offsets against `GamepadProfile.KeySource` metadata (confidence 1.00).

```c
typedef struct GamepadProfile_KeySource_Recovered {
    char padding_0[16];
    unsigned int keyId;
    unsigned int axisId;
    char axisSign;
} GamepadProfile_KeySource_Recovered;

extern long long g_1ef3220;
extern char g_1fab131;

struct_0 * GamepadProfile_KeySource_KeyAndPlusAxis(unsigned int a0, unsigned int a1)
{
    struct_0 *ptr;  // x21

    if (!(g_1fab131 & 1))
    {
        sub_f7d92c(&g_1ef3220);
        g_1fab131 = 1;
    }
    ptr = sub_f7db70(g_1ef3220);
    Object__ctor(ptr, 0);
    ptr->field_10 = a0;
    ptr->field_14 = a1;
    ptr->field_18 = 1;
    return ptr;
}
```

## `GamepadProfile.KeySource.KeyAndMinusAxis` — RVA `0xc308bc`

- Decompiled symbol: `GamepadProfile_KeySource_KeyAndMinusAxis`
- Metadata signature: `public static GamepadProfile.KeySource KeyAndMinusAxis(int keyId, int axisId) { }`
- Native interval: `108` bytes
- Result: `pseudocode`
- Heuristic layout hint: `GamepadProfile_KeySource_Recovered` matched 3 offsets against `GamepadProfile.KeySource` metadata (confidence 1.00).

```c
typedef struct GamepadProfile_KeySource_Recovered {
    char padding_0[16];
    unsigned int keyId;
    unsigned int axisId;
    char axisSign;
} GamepadProfile_KeySource_Recovered;

extern long long g_1ef3220;
extern char g_1fab132;

struct_0 * GamepadProfile_KeySource_KeyAndMinusAxis(unsigned int a0, unsigned int a1)
{
    struct_0 *ptr;  // x21

    if (!(g_1fab132 & 1))
    {
        sub_f7d92c(&g_1ef3220);
        g_1fab132 = 1;
    }
    ptr = sub_f7db70(g_1ef3220);
    Object__ctor(ptr, 0);
    ptr->field_10 = a0;
    ptr->field_14 = a1;
    ptr->field_18 = 0;
    return ptr;
}
```
