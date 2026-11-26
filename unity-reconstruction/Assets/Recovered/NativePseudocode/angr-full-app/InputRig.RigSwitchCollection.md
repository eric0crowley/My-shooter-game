# Native pseudocode: InputRig.RigSwitchCollection

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `InputRig.RigSwitchCollection.get_changed` — RVA `0xc3efa8`

- Decompiled symbol: `InputRig_RigSwitchCollection_get_changed`
- Metadata signature: `public bool get_changed() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[32];
    char field_20;
} struct_0;

long long InputRig_RigSwitchCollection_get_changed(struct_0 *a0)
{
    return a0->field_20;
}
```

## `InputRig.RigSwitchCollection.set_changed` — RVA `0xc3efb0`

- Decompiled symbol: `InputRig_RigSwitchCollection_set_changed`
- Metadata signature: `public void set_changed(bool value) { }`
- Native interval: `12` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[32];
    char field_20;
} struct_0;

struct_0 * InputRig_RigSwitchCollection_set_changed(struct_0 *ptr, char a1)
{
    ptr->field_20 = a1 & 1;
    return ptr;
}
```

## `InputRig.RigSwitchCollection.ctor` — RVA `0xc3efbc`

- Decompiled symbol: `InputRig_RigSwitchCollection_ctor`
- Metadata signature: `public void .ctor(InputRig rig) { }`
- Native interval: `92` bytes
- Result: `pseudocode`

```c
extern long long g_1ef9870;
extern char g_1fab1e9;

void InputRig_RigSwitchCollection_ctor(unsigned long a0, unsigned long a1)
{
    unsigned long long v5;  // x30
    unsigned long long v6;  // x22
    unsigned long long v7;  // x21
    unsigned long long v8;  // x20
    unsigned long long v9;  // x19
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
    if (!(g_1fab1e9 & 1))
    {
        sub_f7d92c(&g_1ef9870);
        g_1fab1e9 = 1;
    }
}
```

## `InputRig.RigSwitchCollection.Add` — RVA `0xc3f018`

- Decompiled symbol: `InputRig_RigSwitchCollection_Add`
- Metadata signature: `public InputRig.RigSwitch Add(string name, bool undoable) { }`
- Native interval: `288` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    char padding_0[16];
    long long field_10;
} struct_2;

typedef struct struct_1 {
    char padding_0[16];
    struct struct_0 *field_10;
} struct_1;

typedef struct struct_0 {
    char padding_0[16];
    unsigned long long field_10;
    unsigned int field_18;
    unsigned int field_1c;
} struct_0;

typedef struct struct_4 {
    char padding_0[32];
    struct struct_3 *field_20;
} struct_4;

typedef struct struct_3 {
    char padding_0[16];
    unsigned long long field_10;
} struct_3;

extern long long g_1ef3348;
extern long long g_1ef9108;
extern long long g_1ef9878;
extern char g_1fab1ea;

struct_2 * InputRig_RigSwitchCollection_Add(struct_1 *p, long long a1)
{
    struct_2 *v0;  // x19
    struct_2 *v1;  // x19
    struct_2 *addr;  // x0
    struct_0 *ptr;  // x0
    unsigned long long v4;  // x8
    unsigned long v5;  // x10
    struct_4 *ptr3;  // x8

    if (!(g_1fab1ea & 1))
    {
        sub_f7d92c(&g_1ef9108);
        sub_f7d92c(&g_1ef9878);
        sub_f7d92c(&g_1ef3348);
        g_1fab1ea = 1;
    }
    v0 = sub_1526618(p, a1, g_1ef9878);
    if (v0)
        return v0;
    v1 = sub_f7db70(g_1ef3348);
    Object__ctor(v1, 0);
    if (v1)
    {
        addr = v1;
        addr->field_10 = a1;
        sub_f7d8d0((struct struct_2 *)&addr->field_10, a1);
        ptr = p->field_10;
        if (ptr)
        {
            v4 = ptr->field_10;
            ptr->field_1c = ptr->field_1c + 1;
            if (v4)
            {
                v5 = ptr->field_18;
                if (*((int *)(v4 + 24)) <= (unsigned int)v5)
                {
                    sub_14a3390();
                    return v1;
                }
                ptr3 = v4 + v5 * 8;
                ptr->field_18 = (unsigned int)v5 + 1;
                ptr3->field_20 = v1;
                sub_f7d8d0((struct struct_4 *)&ptr3->field_20, v1);
                return v1;
            }
        }
    }
    sub_f7db74();
}
```

## `InputRig.RigSwitchCollection.SetSwitchState` — RVA `0xc3f140`

- Decompiled symbol: `InputRig_RigSwitchCollection_SetSwitchState`
- Metadata signature: `public void SetSwitchState(string name, ref int cachedId, bool state) { }`
- Native interval: `152` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[25];
    char field_19;
} struct_1;

typedef struct struct_0 {
    char padding_0[32];
    char field_20;
} struct_0;

extern long long g_1ef9880;
extern char g_1fab1eb;

struct_1 * InputRig_RigSwitchCollection_SetSwitchState(struct_0 *ptr, long long a1, long long a2, unsigned int a3)
{
    struct_1 *p;  // x0
    unsigned int v1;  // w9
    unsigned int v2;  // w8

    if (!(g_1fab1eb & 1))
    {
        sub_f7d92c(&g_1ef9880);
        g_1fab1eb = 1;
    }
    p = sub_15264f8(ptr, a1, a2, g_1ef9880);
    if (!p)
        return p;
    if (!p->field_19)
        v1 = 0;
    else
        v1 = 1;
    v2 = a3 & 1;
    if (v1 != v2)
        ptr->field_20 = 1;
    p->field_19 = v2;
    return p;
}
```

## `InputRig.RigSwitchCollection.SetSwitchState` — RVA `0xc3f1d8`

- Decompiled symbol: `InputRig_RigSwitchCollection_SetSwitchState`
- Metadata signature: `public void SetSwitchState(string name, bool state) { }`
- Native interval: `28` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[25];
    char field_19;
} struct_1;

typedef struct struct_0 {
    char padding_0[32];
    char field_20;
} struct_0;

struct_1 * InputRig_RigSwitchCollection_SetSwitchState(struct_0 *a0, long long a1, unsigned int a2)
{
    struct_1 *v1;  // x0
    unsigned int flag;  // [bp-0x4]

    flag = 0;
    v1 = InputRig_RigSwitchCollection__SetSwitchState(a0, a1, &flag, a2 & 1);
    return InputRig_RigSwitchCollection__SetSwitchState(a0, a1, &flag, a2 & 1);
}
```

## `InputRig.RigSwitchCollection.GetSwitchState` — RVA `0xc3f1f4`

- Decompiled symbol: `InputRig_RigSwitchCollection_GetSwitchState`
- Metadata signature: `public bool GetSwitchState(string name, ref int cachedId, bool fallbackValue) { }`
- Native interval: `132` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[25];
    char field_19;
} struct_0;

extern long long g_1ef9880;
extern char g_1fab1ec;

unsigned int InputRig_RigSwitchCollection_GetSwitchState(long long a0, long long a1, long long a2, unsigned int a3)
{
    unsigned int v0;  // w19
    struct_0 *v1;  // x0

    v0 = a3;
    if (!(g_1fab1ec & 1))
    {
        sub_f7d92c(&g_1ef9880);
        g_1fab1ec = 1;
    }
    v1 = sub_15264f8(a0, a1, a2, g_1ef9880);
    if (v1)
    {
        if (!v1->field_19)
            v0 = 0;
        else
            v0 = 1;
    }
    return v0 & 1;
}
```

## `InputRig.RigSwitchCollection.GetSwitchState` — RVA `0xc3f278`

- Decompiled symbol: `InputRig_RigSwitchCollection_GetSwitchState`
- Metadata signature: `public bool GetSwitchState(string name, bool fallbackValue) { }`
- Native interval: `116` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[25];
    char field_19;
} struct_0;

extern long long g_1ef9878;
extern char g_1fab1ed;

unsigned int InputRig_RigSwitchCollection_GetSwitchState(long long a0, long long a1, unsigned int a2)
{
    unsigned int v0;  // w19
    struct_0 *v1;  // x0

    v0 = a2;
    if (!(g_1fab1ed & 1))
    {
        sub_f7d92c(&g_1ef9878);
        g_1fab1ed = 1;
    }
    v1 = sub_1526618(a0, a1, g_1ef9878);
    if (v1)
    {
        if (!v1->field_19)
            v0 = 0;
        else
            v0 = 1;
    }
    return v0 & 1;
}
```

## `InputRig.RigSwitchCollection.ToggleSwitchState` — RVA `0xc3f2ec`

- Decompiled symbol: `InputRig_RigSwitchCollection_ToggleSwitchState`
- Metadata signature: `public bool ToggleSwitchState(string name, ref int cachedId, bool fallbackValue) { }`
- Native interval: `148` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[32];
    char field_20;
} struct_0;

typedef struct struct_1 {
    char padding_0[25];
    char field_19;
} struct_1;

extern long long g_1ef9880;
extern char g_1fab1ee;

unsigned int InputRig_RigSwitchCollection_ToggleSwitchState(struct_0 *p, long long a1, long long a2, unsigned int a3)
{
    unsigned int v0;  // w19
    struct_1 *ptr;  // x0
    unsigned int v2;  // w8

    v0 = a3;
    if (!(g_1fab1ee & 1))
    {
        sub_f7d92c(&g_1ef9880);
        g_1fab1ee = 1;
    }
    ptr = sub_15264f8(p, a1, a2, g_1ef9880);
    if (ptr)
    {
        p->field_20 = 1;
        v2 = ptr->field_19;
        if (v2)
            v0 = 0;
        else
            v0 = 1;
        ptr->field_19 = (char)v2 ^ 1;
    }
    return v0 & 1;
}
```

## `InputRig.RigSwitchCollection.ToggleSwitchState` — RVA `0xc3f39c`

- Decompiled symbol: `InputRig_RigSwitchCollection_ToggleSwitchState`
- Metadata signature: `public bool ToggleSwitchState(string name, bool fallbackValue) { }`
- Native interval: `32` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[32];
    char field_20;
} struct_0;

unsigned int InputRig_RigSwitchCollection_ToggleSwitchState(struct_0 *a0, long long a1, unsigned int a2)
{
    unsigned int flag;  // [bp-0x4]

    flag = 0;
    return InputRig_RigSwitchCollection__ToggleSwitchState(a0, a1, &flag, a2 & 1) & 1;
}
```

## `InputRig.RigSwitchCollection.SetAll` — RVA `0xc3f3bc`

- Decompiled symbol: `InputRig_RigSwitchCollection_SetAll`
- Metadata signature: `public void SetAll(bool state) { }`
- Native interval: `192` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    char padding_0[25];
    char field_19;
} struct_2;

typedef struct struct_1 {
    char padding_0[16];
    struct struct_0 *field_10;
    char padding_18[8];
    char field_20;
} struct_1;

typedef struct struct_0 {
    char padding_0[25];
    char field_19;
} struct_0;

extern long long g_1ef9110;
extern long long g_1ef9118;
extern char g_1fab1ef;

struct_2 * InputRig_RigSwitchCollection_SetAll(struct_1 *ptr, unsigned int a1)
{
    struct_0 *p;  // x0, Other Possible Types: struct_2 *
    int v1;  // w21
    unsigned int v2;  // w8
    unsigned long v3;  // x0

    if (!(g_1fab1ef & 1))
    {
        sub_f7d92c(&g_1ef9110);
        sub_f7d92c(&g_1ef9118);
        g_1fab1ef = 1;
    }
    p = ptr->field_10;
    if (p)
    {
        v1 = 0;
        do
        {
            if (*((int *)&p->padding_0[24]) <= v1)
                return p;
            p = sub_14a30c0();
            if (!p)
                break;
            if (!p->field_19)
                v2 = 0;
            else
                v2 = 1;
            if (v2 != (a1 & 1))
            {
                ptr->field_20 = 1;
                p->field_19 = (char)a1 & 1;
            }
            p = ptr->field_10;
            v1 += 1;
        } while (p);
    }
    v3 = sub_f7db74(p);
    return sub_f7db74(p);
}
```

## `InputRig.RigSwitchCollection.ResetSwitch` — RVA `0xc3f47c`

- Decompiled symbol: `InputRig_RigSwitchCollection_ResetSwitch`
- Metadata signature: `public void ResetSwitch(string name, ref int cachedId) { }`
- Native interval: `132` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[32];
    char field_20;
} struct_0;

extern long long g_1ef9880;
extern char g_1fab1f0;

char [26] InputRig_RigSwitchCollection_ResetSwitch(struct_0 *p, long long a1, long long a2)
{
    char ptr[26];  // x0
    unsigned int v1;  // w8

    if (!(g_1fab1f0 & 1))
    {
        sub_f7d92c(&g_1ef9880);
        g_1fab1f0 = 1;
    }
    ptr = sub_15264f8(p, a1, a2, g_1ef9880);
    if (!ptr)
        return ptr;
    v1 = ptr[24];
    if (v1 == ptr[25])
        return ptr;
    p->field_20 = 1;
    ptr[25] = v1;
    return ptr;
}
```

## `InputRig.RigSwitchCollection.ResetSwitch` — RVA `0xc3f500`

- Decompiled symbol: `InputRig_RigSwitchCollection_ResetSwitch`
- Metadata signature: `public void ResetSwitch(string name) { }`
- Native interval: `24` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[32];
    char field_20;
} struct_0;

char [26] InputRig_RigSwitchCollection_ResetSwitch(struct_0 *a0, long long a1)
{
    char v1[26];  // x0
    unsigned int flag;  // [bp-0x4]

    flag = 0;
    v1 = InputRig_RigSwitchCollection__ResetSwitch(a0, a1, &flag);
    return InputRig_RigSwitchCollection__ResetSwitch(a0, a1, &flag);
}
```

## `InputRig.RigSwitchCollection.Reset` — RVA `0xc3f518`

- Decompiled symbol: `InputRig_RigSwitchCollection_Reset`
- Metadata signature: `public void Reset() { }`
- Native interval: `168` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    void* field_10;
    char padding_18[8];
    char field_20;
} struct_0;

extern long long g_1ef9110;
extern long long g_1ef9118;
extern char g_1fab1f1;

void* InputRig_RigSwitchCollection_Reset(struct_0 *ptr)
{
    void* p;  // x0
    unsigned int v1;  // w20
    unsigned int v2;  // w8
    unsigned long v3;  // x0

    if (!(g_1fab1f1 & 1))
    {
        sub_f7d92c(&g_1ef9110);
        sub_f7d92c(&g_1ef9118);
        g_1fab1f1 = 1;
    }
    p = ptr->field_10;
    if (p)
    {
        v1 = 0;
        do
        {
            if ((int)p[24] <= v1)
                return p;
            p = sub_14a30c0();
            if (!p)
                break;
            v2 = (char)p[24];
            if (v2 != (char)p[25])
            {
                ptr->field_20 = 1;
                *((char *)&p[25]) = v2;
            }
            p = ptr->field_10;
            v1 += 1;
        } while (p);
    }
    v3 = sub_f7db74(p);
    return sub_f7db74(p);
}
```

## `InputRig.RigSwitchCollection.GetSwitchId` — RVA `0xc3f5c0`

- Decompiled symbol: `InputRig_RigSwitchCollection_GetSwitchId`
- Metadata signature: `public int GetSwitchId(string name) { }`
- Native interval: `116` bytes
- Result: `pseudocode`

```c
extern long long g_1ef9880;
extern char g_1fab1f2;

unsigned long long InputRig_RigSwitchCollection_GetSwitchId(long long a0, long long a1)
{
    unsigned long long v2;  // x30
    unsigned long long v0;  // [bp-0x30]
    unsigned int v1;  // [bp-0x24]

    v0 = v2;
    if (!(g_1fab1f2 & 1))
    {
        sub_f7d92c(&g_1ef9880);
        g_1fab1f2 = 1;
    }
    v1 = 4294967295;
    if (!sub_15264f8(a0, a1, &v1, g_1ef9880))
        return 4294967295;
    return v1;
}
```
