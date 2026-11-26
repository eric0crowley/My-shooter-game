# Native pseudocode: GamepadProfile

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `GamepadProfile.GetKeySource` — RVA `0xc2dd88`

- Decompiled symbol: `GamepadProfile_GetKeySource`
- Metadata signature: `public GamepadProfile.KeySource GetKeySource(int id) { }`
- Native interval: `144` bytes
- Result: `pseudocode`

```c
extern char g_8322dc;

unsigned int GamepadProfile_GetKeySource(unsigned long a0, unsigned int a1)
{
    if (11 < a1)
        return 0;
    goto sub_102ddac + (&g_8322dc)[a1] * 4;
}
```

## `GamepadProfile.ctor` — RVA `0xc2fac0`

- Decompiled symbol: `GamepadProfile_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `572` bytes
- Result: `pseudocode`
- Heuristic layout hint: `GamepadProfile_Recovered` matched 5 offsets against `GamepadProfile` metadata (confidence 1.00).

```c
typedef struct GamepadProfile_Recovered {
    char padding_0[16];
    long long name;
    long long joystickIdentifier;
    unsigned int profileMode;
    char padding_24[4];
    long long unityVerFrom;
    long long unityVerTo;
} GamepadProfile_Recovered;

extern long long g_1ef3218;
extern long long g_1f07cd0;
extern long long g_1f07d20;
extern long long g_1f09a98;
extern long long g_1f0c5c0;
extern char g_1fab127;

long long GamepadProfile_ctor(struct_0 *ptr4)
{
    unsigned long long v8;  // x30
    unsigned long long v9;  // x25
    struct_0 *ptr;  // x0
    struct_0 *p;  // x0
    unsigned long long v10;  // x24
    unsigned long long v11;  // x23
    unsigned long long v12;  // x22
    unsigned long long v13;  // x21
    unsigned long long v14;  // x20
    unsigned long long v15;  // x19
    struct_0 *addr;  // x0
    struct_0 *ptr3;  // x0
    unsigned long long v0;  // [bp-0x40]
    unsigned long long v1;  // [bp-0x38]
    unsigned long long v2;  // [bp-0x30]
    unsigned long long v3;  // [bp-0x28]
    unsigned long long v4;  // [bp-0x20]
    unsigned long long v5;  // [bp-0x18]
    unsigned long long v6;  // [bp-0x10]
    unsigned long long v7;  // [bp-0x8]

    v0 = v8;
    v1 = v9;
    v2 = v10;
    v3 = v11;
    v4 = v12;
    v5 = v13;
    v6 = v14;
    v7 = v15;
    if (!(g_1fab127 & 1))
    {
        sub_f7d92c(&g_1ef3218);
        sub_f7d92c(&g_1f07d20);
        sub_f7d92c(&g_1f07cd0);
        sub_f7d92c(&g_1f09a98);
        sub_f7d92c(&g_1f0c5c0);
        g_1fab127 = 1;
    }
    Object__ctor(ptr4, 0);
    addr = ptr4;
    addr->field_10 = g_1f0c5c0;
    sub_f7d8d0((struct GamepadProfile_Recovered *)&addr->field_10, g_1f0c5c0);
    ptr3 = ptr4;
    ptr3->field_18 = g_1f09a98;
    sub_f7d8d0((struct GamepadProfile_Recovered *)&ptr3->field_18, g_1f09a98);
    ptr4->field_20 = 0;
    ptr = ptr4;
    ptr->field_28 = g_1f07cd0;
    sub_f7d8d0((struct GamepadProfile_Recovered *)&ptr->field_28, g_1f07cd0);
    p = ptr4;
    p->field_30 = g_1f07d20;
    sub_f7d8d0((struct GamepadProfile_Recovered *)&p->field_30, g_1f07d20);
    GamepadProfile_JoystickSource__ctor(sub_f7db70(g_1ef3218)); /* do not return */
}
```

## `GamepadProfile.IsCompatible` — RVA `0xc2fe74`

- Decompiled symbol: `GamepadProfile_IsCompatible`
- Metadata signature: `public bool IsCompatible(string deviceName) { }`
- Native interval: `172` bytes
- Result: `pseudocode`
- Heuristic layout hint: `GamepadProfile_Recovered` matched 2 offsets against `GamepadProfile` metadata (confidence 1.00).

```c
typedef struct GamepadProfile_Recovered {
    char padding_0[24];
    long long joystickIdentifier;
    unsigned int profileMode;
} GamepadProfile_Recovered;

extern char g_1fab128;

unsigned int GamepadProfile_IsCompatible(struct_1 *a0, long long a1)
{
    if (!(g_1fab128 & 1))
    {
        sub_f7d92c("+N");
        g_1fab128 = 1;
    }
    if (a0->field_20 == 1)
    {
        if (!g_1ef11c0->field_e0)
            sub_f7da5c(g_1ef11c0);
        if (!((char)Regex__IsMatch(a1, a0->field_18, 513, 0) & 1))
            return 0;
    }
    else if (!a0->field_20)
    {
        if (!a1)
        {
            sub_f7db74();
        }
        else if (((char)(String__IndexOf(a1, a0->field_18, 5, 0) >> 31) & 1))
        {
            return 0;
        }
    }
    return 1;
}
```

## `GamepadProfile.AddSupportedVersion` — RVA `0xc2ff20`

- Decompiled symbol: `GamepadProfile_AddSupportedVersion`
- Metadata signature: `public void AddSupportedVersion(string unityVer) { }`
- Native interval: `96` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[48];
    long long field_30;
} struct_0;

long long GamepadProfile_AddSupportedVersion(struct_0 *ptr, long long a1)
{
    unsigned long v0;  // x0
    unsigned long v1;  // x0
    long long v2;  // x0

    v0 = String__IsNullOrEmpty(a1, 0);
    if (((char)v0 & 1))
        return v0;
    if (ptr->field_30)
    {
        v1 = String__CompareTo(ptr->field_30, a1, 0);
        if (((char)(v1 >> 31) & 1))
        {
            ptr->field_30 = a1;
            v2 = sub_f7d8d0();
            return sub_f7d8d0();
        }
        return v1;
    }
    sub_f7db74(0);
}
```

## `GamepadProfile.GetJoystickSource` — RVA `0xc2ff80`

- Decompiled symbol: `GamepadProfile_GetJoystickSource`
- Metadata signature: `public GamepadProfile.JoystickSource GetJoystickSource(int id) { }`
- Native interval: `56` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[56];
    unsigned long long field_38;
} struct_0;

unsigned long long GamepadProfile_GetJoystickSource(struct_0 *a0, unsigned int flag)
{
    struct_0 *v0;  // x8

    if (flag == 2)
    {
        v0 = &a0[1].padding_0[8];
    }
    else if (flag == 1)
    {
        v0 = a0 + 1;
    }
    else if (!flag)
    {
        v0 = &a0->field_38;
    }
    else
    {
        return 0;
    }
    return *((long long *)&v0->padding_0[0]);
}
```

## `GamepadProfile.IsDuplicateOf` — RVA `0xc2ffb8`

- Decompiled symbol: `GamepadProfile_IsDuplicateOf`
- Metadata signature: `public bool IsDuplicateOf(GamepadProfile profile) { }`
- Native interval: `264` bytes
- Result: `pseudocode`

```c
unsigned int GamepadProfile_IsDuplicateOf(long long *a0, long long *a1)
{
    unsigned int i;  // w21
    unsigned int flag;  // w21
    long long v10[8];  // x8
    long long v11[8];  // x9
    unsigned long long v12;  // x0
    long long v2[8];  // x22
    long long v3[8];  // x23
    long long v4[8];  // x24
    long long v5[8];  // x25
    long long v6[8];  // x20
    long long v7[8];  // x19
    long long v8[8];  // x9
    long long v9[8];  // x8

    if (a1 && a0[3])
    {
        if (!((char)String__Equals(a0[3], a1[3], 5, 0) & 1))
        {
LABEL_10300a0:
            v12 = 0;
LABEL_10300a4:
            return (unsigned int)v12 & 1;
        }
        i = 0;
        do
        {
            if (!GamepadProfile__GetKeySource(a0, i))
                goto LABEL_10300bc;
            GamepadProfile__GetKeySource(a1, i);
            if (!(GamepadProfile_KeySource__IsDuplicateOf() & 1))
                goto LABEL_10300a0;
            i += 1;
        } while (i != 12);
        flag = 0;
        v2 = a0 + 9;
        v3 = a1 + 9;
        v4 = a0 + 8;
        v5 = a1 + 8;
        v6 = a0 + 7;
        v7 = a1 + 7;
        while (true)
        {
            v8 = v6;
            v9 = v7;
            if (flag)
            {
                if (flag != 2)
                {
                    v8 = v4;
                    v9 = v5;
                    if (flag != 1)
                        break;
                }
                else
                {
                    v8 = v2;
                    v9 = v3;
                }
            }
            v10 = v9;
            v11 = v8;
            if (!v11[0])
                break;
            v12 = GamepadProfile_JoystickSource__IsDuplicateOf(v11[0], v10[0]);
            if (flag == 2 || !((flag += 1, ((char)v12 & 1))))
                goto LABEL_10300a4;
        }
    }
LABEL_10300bc:
    sub_f7db74();
}
```

## `GamepadProfile.ctor` — RVA `0xc30188`

- Decompiled symbol: `GamepadProfile_ctor`
- Metadata signature: `public void .ctor(string name, string deviceIdentifier, GamepadProfile.ProfileMode profileMode, string unityVerFrom, string unityVerTo, GamepadProfile.JoystickSource leftStick, GamepadProfile.JoystickSource rightStick, GamepadProfile.JoystickSource dpad, GamepadProfile.KeySource keyFaceD, GamepadProfile.KeySource keyFaceR, GamepadProfile.KeySource keyFaceL, GamepadProfile.KeySource keyFaceU, GamepadProfile.KeySource keySelect, GamepadProfile.KeySource keyStart, GamepadProfile.KeySource keyL1, GamepadProfile.KeySource keyR1, GamepadProfile.KeySource keyL2, GamepadProfile.KeySource keyR2, GamepadProfile.KeySource keyL3, GamepadProfile.KeySource keyR3) { }`
- Native interval: `756` bytes
- Result: `pseudocode`
- Heuristic layout hint: `GamepadProfile_Recovered` matched 2 offsets against `GamepadProfile` metadata (confidence 1.00).

```c
typedef struct GamepadProfile_Recovered {
    char padding_0[16];
    unsigned long long name;
    char joystickIdentifier;
} GamepadProfile_Recovered;

extern unsigned long long g_1f07cc8;
extern unsigned long long g_1f07d20;
extern char g_1fab129;

void GamepadProfile_ctor(void* ptr, long long a1, long long a2, unsigned int a3, unsigned long long a4, unsigned long long a5, long long a6, long long a7, long long a8, struct_0 *a9, struct_0 *a10, struct_0 *a11, unsigned long a12, struct_0 *a13, struct_0 *a14, struct_0 *a15, struct_0 *a16, struct_0 *a17, struct_0 *a18, struct_0 *a19, struct_0 *a20)
{
    unsigned long long v23;  // x30
    unsigned long long v24;  // x28
    unsigned long long v33;  // x19
    long long v34;  // x23
    long long v35;  // x22
    long long v36;  // x24
    unsigned long v37;  // x21
    void* p;  // x0
    void* addr;  // x0
    unsigned long v40;  // 4124
    unsigned long long v41;  // x1
    unsigned long v42;  // 4124
    unsigned long long v25;  // x27
    unsigned long long v43;  // x1
    void* ptr3;  // x0
    void* ptr4;  // x0
    void* ptr5;  // x0
    void* ptr6;  // x0
    void* ptr7;  // x0
    void* ptr8;  // x0
    void* ptr9;  // x0
    void* ptr10;  // x0
    void* ptr11;  // x0
    unsigned long long v26;  // x26
    void* ptr12;  // x0
    void* ptr13;  // x0
    void* ptr14;  // x0
    void* ptr15;  // x0
    void* ptr16;  // x0
    unsigned long long v27;  // x25
    unsigned long long v28;  // x24
    unsigned long long v29;  // x23
    unsigned long long v30;  // x22
    unsigned long long v31;  // x21
    unsigned long long v32;  // x20
    struct_0 *v0;  // [bp-0xb8]
    struct_0 *v1;  // [bp-0xb0]
    struct_0 *v2;  // [bp-0xa8]
    struct_0 *v3;  // [bp-0xa0]
    struct_0 *v4;  // [bp-0x98]
    struct_0 *v5;  // [bp-0x90]
    struct_0 *v6;  // [bp-0x88]
    struct_0 *v7;  // [bp-0x80]
    struct_0 *v8;  // [bp-0x78]
    struct_0 *v9;  // [bp-0x70]
    struct_0 *v10;  // [bp-0x68]
    unsigned long v11;  // [bp-0x60]
    unsigned long long v12;  // [bp-0x58]
    unsigned long long v13;  // [bp-0x50]
    unsigned long long v14;  // [bp-0x48]
    unsigned long long v15;  // [bp-0x40]
    unsigned long long v16;  // [bp-0x38]
    unsigned long long v17;  // [bp-0x30]
    unsigned long long v18;  // [bp-0x28]
    unsigned long long v19;  // [bp-0x20]
    unsigned long long v20;  // [bp-0x18]
    unsigned long long v21;  // [bp-0x10]
    unsigned long long v22;  // [bp-0x8]

    v11 = &a8;
    v12 = v23;
    v13 = v24;
    v14 = v25;
    v15 = v26;
    v16 = v27;
    v17 = v28;
    v18 = v29;
    v19 = v30;
    v20 = v31;
    v21 = v32;
    v22 = v33;
    v34 = a8;
    v9 = a19;
    v10 = a20;
    v35 = a7;
    v36 = a6;
    v7 = a17;
    v8 = a18;
    v5 = a15;
    v6 = a16;
    v37 = a12;
    v3 = a14;
    v4 = a13;
    v0 = a10;
    v1 = a9;
    v2 = a11;
    if (!(g_1fab129 & 1))
    {
        sub_f7d92c(&g_1f07d20);
        sub_f7d92c(&g_1f07cc8);
        g_1fab129 = 1;
    }
    Object__ctor(ptr, 0);
    p = ptr;
    *((long long *)&p[16]) = a1;
    sub_f7d8d0(p + 16, a1);
    addr = ptr;
    *((long long *)&addr[24]) = a2;
    sub_f7d8d0(addr + 24, a2);
    *((unsigned int *)&ptr[32]) = a3;
    v40 = arm64g_calculate_condition(25, (unsigned long long)((unsigned int)(unsigned long long)String__IsNullOrEmpty(a4, 0) & 1), 0, 0);
    if ((char)v40)
        v41 = g_1f07cc8;
    else
        v41 = a4;
    *((unsigned long long *)&ptr[40]) = v41;
    sub_f7d8d0();
    v42 = arm64g_calculate_condition(25, (unsigned long long)((unsigned int)(unsigned long long)String__IsNullOrEmpty(a5, 0) & 1), 0, 0);
    if ((char)v42)
        v43 = g_1f07d20;
    else
        v43 = a5;
    *((unsigned long long *)&ptr[48]) = v43;
    sub_f7d8d0();
    if (!v36)
        v36 = GamepadProfile_JoystickSource__Empty();
    ptr3 = ptr;
    *((long long *)&ptr3[56]) = v36;
    sub_f7d8d0(ptr3 + 56, v36);
    if (!v35)
        v35 = GamepadProfile_JoystickSource__Empty();
    ptr4 = ptr;
    *((long long *)&ptr4[64]) = v35;
    sub_f7d8d0(ptr4 + 64, v35);
    if (!v34)
        v34 = GamepadProfile_JoystickSource__Empty();
    ptr5 = ptr;
    *((long long *)&ptr5[72]) = v34;
    sub_f7d8d0(ptr5 + 72, v34);
    if (!v37)
        v37 = GamepadProfile_KeySource__Empty();
    ptr6 = ptr;
    *((unsigned long *)&ptr6[80]) = v37;
    sub_f7d8d0(ptr6 + 80, v37);
    if (!v0)
        v0 = GamepadProfile_KeySource__Empty();
    ptr7 = ptr;
    *((struct_0 **)&ptr7[88]) = v0;
    sub_f7d8d0(ptr7 + 88);
    if (!v1)
        v1 = GamepadProfile_KeySource__Empty();
    ptr8 = ptr;
    *((struct_0 **)&ptr8[96]) = v1;
    sub_f7d8d0(ptr8 + 96);
    if (!v2)
        v2 = GamepadProfile_KeySource__Empty();
    ptr9 = ptr;
    *((struct_0 **)&ptr9[104]) = v2;
    sub_f7d8d0(ptr9 + 104);
    if (!v3)
        v3 = GamepadProfile_KeySource__Empty();
    ptr10 = ptr;
    *((struct_0 **)&ptr10[112]) = v3;
    sub_f7d8d0(ptr10 + 112);
    if (!v4)
        v4 = GamepadProfile_KeySource__Empty();
    ptr11 = ptr;
    *((struct_0 **)&ptr11[120]) = v4;
    sub_f7d8d0(ptr11 + 120);
    if (!v5)
        v5 = GamepadProfile_KeySource__Empty();
    ptr12 = ptr;
    *((struct_0 **)&ptr12[128]) = v5;
    sub_f7d8d0(ptr12 + 128);
    if (!v6)
        v6 = GamepadProfile_KeySource__Empty();
    ptr13 = ptr;
    *((struct_0 **)&ptr13[136]) = v6;
    sub_f7d8d0(ptr13 + 136);
    if (!v7)
        v7 = GamepadProfile_KeySource__Empty();
    ptr14 = ptr;
    *((struct_0 **)&ptr14[144]) = v7;
    sub_f7d8d0(ptr14 + 144);
    if (!v8)
        v8 = GamepadProfile_KeySource__Empty();
    ptr15 = ptr;
    *((struct_0 **)&ptr15[152]) = v8;
    sub_f7d8d0(ptr15 + 152);
    if (!v9)
        v9 = GamepadProfile_KeySource__Empty();
    ptr16 = ptr;
    *((struct_0 **)&ptr16[160]) = v9;
    sub_f7d8d0(ptr16 + 160);
    if (!v10)
        v10 = GamepadProfile_KeySource__Empty();
    *((struct_0 **)&ptr[168]) = v10;
    sub_f7d8d0();
    return;
}
```
