# Native pseudocode: BuiltInGamepadProfileBank

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `BuiltInGamepadProfileBank.GetProfile` — RVA `0xc2d590`

- Decompiled symbol: `BuiltInGamepadProfileBank_GetProfile`
- Metadata signature: `public static GamepadProfile GetProfile(string deviceName) { }`
- Native interval: `44` bytes
- Result: `pseudocode`

```c
void BuiltInGamepadProfileBank_GetProfile(unsigned long a0)
{
    BuiltInGamepadProfileBank__Inst();
    if (!BuiltInGamepadProfileBank__Inst())
        return;
    goto *((long long *)(*((long long *)BuiltInGamepadProfileBank__Inst()) + 392));
}
```

## `BuiltInGamepadProfileBank.GetGenericProfile` — RVA `0xc2d5bc`

- Decompiled symbol: `BuiltInGamepadProfileBank_GetGenericProfile`
- Metadata signature: `public static GamepadProfile GetGenericProfile() { }`
- Native interval: `36` bytes
- Result: `pseudocode`

```c
void BuiltInGamepadProfileBank_GetGenericProfile(void)
{
    BuiltInGamepadProfileBank__Inst();
    if (!BuiltInGamepadProfileBank__Inst())
        return;
    goto *((long long *)(*((long long *)BuiltInGamepadProfileBank__Inst()) + 376));
}
```

## `BuiltInGamepadProfileBank.ctor` — RVA `0xc30b80`

- Decompiled symbol: `BuiltInGamepadProfileBank_ctor`
- Metadata signature: `protected void .ctor() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long BuiltInGamepadProfileBank_ctor(void)
{
    long long v0;  // x0

    v0 = Object__ctor();
    return Object__ctor();
}
```

## `BuiltInGamepadProfileBank.Inst` — RVA `0xc30b88`

- Decompiled symbol: `BuiltInGamepadProfileBank_Inst`
- Metadata signature: `private static BuiltInGamepadProfileBank Inst() { }`
- Native interval: `440` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    unsigned long long field_0;
} struct_1;

typedef struct struct_0 {
    char padding_0[184];
    struct struct_1 *field_b8;
} struct_0;

typedef struct struct_2 {
    char padding_0[224];
    unsigned int field_e0;
} struct_2;

extern struct_2 *g_1eee870;
extern struct_0 *g_1eeec58;
extern long long g_1eeec60;
extern long long g_1eeec68;
extern long long g_1eeec70;
extern long long g_1eeec78;
extern long long g_1eeec80;
extern long long g_1eeec88;
extern char g_1fab137;
extern char g_832558;

unsigned long long BuiltInGamepadProfileBank_Inst(void)
{
    unsigned int v0;  // w0

    if (!(g_1fab137 & 1))
    {
        sub_f7d92c(&g_1eee870);
        sub_f7d92c(&g_1eeec60);
        sub_f7d92c(&g_1eeec68);
        sub_f7d92c(&g_1eeec70);
        sub_f7d92c(&g_1eeec78);
        sub_f7d92c(&g_1eeec80);
        sub_f7d92c(&g_1eeec88);
        sub_f7d92c(&g_1eeec58);
        g_1fab137 = 1;
    }
    if (g_1eeec58->field_b8->field_0)
        return g_1eeec58->field_b8->field_0;
    if (!g_1eee870->field_e0)
        sub_f7da5c(g_1eee870);
    v0 = Application__get_platform(0);
    if (20 >= v0)
    {
        goto sub_1030c60 + (&g_832558)[v0] * 4;
    }
    else if (v0 == 31)
    {
        BuiltInGamepadProfileBankIOS__ctor(sub_f7db70(g_1eeec68)); /* do not return */
    }
    else
    {
        return g_1eeec58->field_b8->field_0;
    }
}
```

## `BuiltInGamepadProfileBank.GetInternalGenericProfile` — RVA `0xc30d40`

- Decompiled symbol: `BuiltInGamepadProfileBank_GetInternalGenericProfile`
- Metadata signature: `protected virtual GamepadProfile GetInternalGenericProfile() { }`
- Native interval: `108` bytes
- Result: `pseudocode`

```c
extern char g_1fab136;

long long BuiltInGamepadProfileBank_GetInternalGenericProfile(void* a0)
{
    void* ptr;  // x19
    unsigned long v1;  // x20

    if (!(g_1fab136 & 1))
    {
        sub_f7d92c("}j");
        g_1fab136 = 1;
    }
    ptr = a0 + 24;
    if ((long long)a0[24])
        return (long long)a0[24];
    v1 = sub_f7db70(g_1ef3210);
    GamepadProfile_GenericProfile__ctor(v1);
    *((unsigned long *)ptr) = v1;
    sub_f7d8d0(ptr, v1);
    return *((long long *)ptr);
}
```

## `BuiltInGamepadProfileBank.FindProfile` — RVA `0xc30dac`

- Decompiled symbol: `BuiltInGamepadProfileBank_FindProfile`
- Metadata signature: `protected virtual GamepadProfile FindProfile(string deviceName) { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long BuiltInGamepadProfileBank_FindProfile(unsigned long a0)
{
    unsigned long long v0;  // x0

    v0 = BuiltInGamepadProfileBank__FindInternalProfile();
    return BuiltInGamepadProfileBank__FindInternalProfile();
}
```

## `BuiltInGamepadProfileBank.FindInternalProfile` — RVA `0xc30db0`

- Decompiled symbol: `BuiltInGamepadProfileBank_FindInternalProfile`
- Metadata signature: `protected GamepadProfile FindInternalProfile(string deviceName) { }`
- Native interval: `156` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    void* field_10;
} struct_0;

typedef struct struct_1 {
    char padding_0[32];
    struct struct_1 *field_20;
} struct_1;

typedef struct struct_1 {
    char padding_0[24];
    long long field_18;
    unsigned int field_20;
} struct_1;

unsigned long long BuiltInGamepadProfileBank_FindInternalProfile(struct_0 *ptr, long long a1)
{
    void* p;  // x8
    unsigned long v1;  // x9
    unsigned long long v2;  // x21
    struct_1 *v3;  // x9
    unsigned long v4;  // x0

    p = ptr->field_10;
    if (!p)
        return 0;
    v1 = (long long)p[24];
    if (!v1)
    {
        return 0;
    }
    else if ((unsigned int)v1 >= 1)
    {
        v2 = 0;
        do
        {
            if ((v1 & 4294967295) <= v2)
            {
LABEL_1030e44:
                sub_f7db74(sub_f7db7c());
            }
            v3 = p + v2 * 8;
            if (!v3->field_20)
                continue;
            v4 = GamepadProfile__IsCompatible(v3->field_20, a1);
            p = ptr->field_10;
            if (((char)v4 & 1))
            {
                if (!p)
                    sub_f7db74(v4);
                if ((int)p[24] > (unsigned int)v2)
                    return *((long long *)(32 + (char *)p + 8 * v2));
                goto LABEL_1030e44;
            }
            else if (!p)
            {
                sub_f7db74(v4);
            }
        } while ((v1 = (unsigned long)(unsigned long long)(unsigned int)(int)p[24], v2 += 1, v2 < (v1 & 4294967295)));
    }
    else
    {
        return 0;
    }
    return 0;
}
```
