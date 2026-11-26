# Native pseudocode: GamepadManager

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `GamepadManager.get_activeManager` — RVA `0xc2a250`

- Decompiled symbol: `GamepadManager_get_activeManager`
- Metadata signature: `public static GamepadManager get_activeManager() { }`
- Native interval: `72` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    unsigned long long field_0;
} struct_1;

typedef struct struct_0 {
    char padding_0[184];
    struct struct_1 *field_b8;
} struct_0;

extern struct_0 *g_1eefb00;
extern char g_1fab0f2;

long long GamepadManager_get_activeManager(void)
{
    if (!(g_1fab0f2 & 1))
    {
        sub_f7d92c(&g_1eefb00);
        g_1fab0f2 = 1;
    }
    return g_1eefb00->field_b8->field_0;
}
```

## `GamepadManager.set_activeManager` — RVA `0xc2a298`

- Decompiled symbol: `GamepadManager_set_activeManager`
- Metadata signature: `private static void set_activeManager(GamepadManager value) { }`
- Native interval: `88` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    unsigned long long field_0;
} struct_1;

typedef struct struct_0 {
    char padding_0[184];
    struct struct_1 *field_b8;
} struct_0;

extern struct_0 *g_1eefb00;
extern char g_1fab0f3;

void GamepadManager_set_activeManager(unsigned long a0)
{
    unsigned long long v4;  // x30
    unsigned long long v5;  // x21
    unsigned long long v6;  // x20
    unsigned long long v7;  // x19
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x18]
    unsigned long long v2;  // [bp-0x10]
    unsigned long long v3;  // [bp-0x8]

    v0 = v4;
    v1 = v5;
    v2 = v6;
    v3 = v7;
    if (!(g_1fab0f3 & 1))
    {
        sub_f7d92c(&g_1eefb00);
        g_1fab0f3 = 1;
    }
    g_1eefb00->field_b8->field_0 = a0;
    sub_f7d8d0();
    return;
}
```

## `GamepadManager.add_onGamepadDisconnected` — RVA `0xc2a2f0`

- Decompiled symbol: `GamepadManager_add_onGamepadDisconnected`
- Metadata signature: `public static void add_onGamepadDisconnected(GamepadManager.OnDisconnectionCallback value) { }`
- Native interval: `188` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[8];
    long long field_8;
} struct_0;

typedef struct struct_1 {
    char padding_0[184];
    struct struct_0 *field_b8;
} struct_1;

extern struct_1 *g_1eefb00;
extern char g_1fab0f4;

long long GamepadManager_add_onGamepadDisconnected(long long a0)
{
    long long v0;  // x20
    long long v1;  // x20
    long long v2;  // x8
    long long v3;  // x20

    if (!(g_1fab0f4 & 1))
    {
        sub_f7d92c(&g_1eefb00);
        sub_f7d92c("uj");
        g_1fab0f4 = 1;
    }
    v0 = g_1eefb00->field_b8->field_8;
    while (true)
    {
        v1 = v0;
        v2 = Delegate__Combine(v1, a0, 0);
        if (v2 && *((long long *)v2) != g_1ef3208)
            sub_f7df10(v2);
        v3 = sub_f60ebc(&g_1eefb00->field_b8->field_8, v2, v1);
        v0 = v3;
        if (v1 == v0)
            return v3;
    }
}
```

## `GamepadManager.remove_onGamepadDisconnected` — RVA `0xc2a3ac`

- Decompiled symbol: `GamepadManager_remove_onGamepadDisconnected`
- Metadata signature: `public static void remove_onGamepadDisconnected(GamepadManager.OnDisconnectionCallback value) { }`
- Native interval: `188` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[8];
    long long field_8;
} struct_0;

typedef struct struct_1 {
    char padding_0[184];
    struct struct_0 *field_b8;
} struct_1;

extern struct_1 *g_1eefb00;
extern char g_1fab0f5;

long long GamepadManager_remove_onGamepadDisconnected(long long a0)
{
    long long v0;  // x20
    long long v1;  // x20
    unsigned long long *v2;  // x8
    long long v3;  // x20

    if (!(g_1fab0f5 & 1))
    {
        sub_f7d92c(&g_1eefb00);
        sub_f7d92c("uj");
        g_1fab0f5 = 1;
    }
    v0 = g_1eefb00->field_b8->field_8;
    while (true)
    {
        v1 = v0;
        v2 = Delegate__Remove(v1, a0, 0);
        if (v2 && *(v2) != g_1ef3208)
            sub_f7df10(v2);
        v3 = sub_f60ebc(&g_1eefb00->field_b8->field_8, v2, v1);
        v0 = v3;
        if (v1 == v0)
            return v3;
    }
}
```

## `GamepadManager.add_onGamepadDisactivated` — RVA `0xc2a468`

- Decompiled symbol: `GamepadManager_add_onGamepadDisactivated`
- Metadata signature: `public static void add_onGamepadDisactivated(GamepadManager.OnDisconnectionCallback value) { }`
- Native interval: `188` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    long long field_10;
} struct_0;

typedef struct struct_1 {
    char padding_0[184];
    struct struct_0 *field_b8;
} struct_1;

extern struct_1 *g_1eefb00;
extern char g_1fab0f6;

long long GamepadManager_add_onGamepadDisactivated(long long a0)
{
    long long v0;  // x20
    long long v1;  // x20
    long long v2;  // x8
    long long v3;  // x20

    if (!(g_1fab0f6 & 1))
    {
        sub_f7d92c(&g_1eefb00);
        sub_f7d92c("uj");
        g_1fab0f6 = 1;
    }
    v0 = g_1eefb00->field_b8->field_10;
    while (true)
    {
        v1 = v0;
        v2 = Delegate__Combine(v1, a0, 0);
        if (v2 && *((long long *)v2) != g_1ef3208)
            sub_f7df10(v2);
        v3 = sub_f60ebc(&g_1eefb00->field_b8->field_10, v2, v1);
        v0 = v3;
        if (v1 == v0)
            return v3;
    }
}
```

## `GamepadManager.remove_onGamepadDisactivated` — RVA `0xc2a524`

- Decompiled symbol: `GamepadManager_remove_onGamepadDisactivated`
- Metadata signature: `public static void remove_onGamepadDisactivated(GamepadManager.OnDisconnectionCallback value) { }`
- Native interval: `188` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    long long field_10;
} struct_0;

typedef struct struct_1 {
    char padding_0[184];
    struct struct_0 *field_b8;
} struct_1;

extern struct_1 *g_1eefb00;
extern char g_1fab0f7;

long long GamepadManager_remove_onGamepadDisactivated(long long a0)
{
    long long v0;  // x20
    long long v1;  // x20
    long long v2;  // x8
    long long v3;  // x20

    if (!(g_1fab0f7 & 1))
    {
        sub_f7d92c(&g_1eefb00);
        sub_f7d92c("uj");
        g_1fab0f7 = 1;
    }
    v0 = g_1eefb00->field_b8->field_10;
    while (true)
    {
        v1 = v0;
        v2 = Delegate__Remove(v1, a0, 0);
        if (v2 && *((long long *)v2) != g_1ef3208)
            sub_f7df10(v2);
        v3 = sub_f60ebc(&g_1eefb00->field_b8->field_10, v2, v1);
        v0 = v3;
        if (v1 == v0)
            return v3;
    }
}
```

## `GamepadManager.add_onGamepadConnected` — RVA `0xc2a5e0`

- Decompiled symbol: `GamepadManager_add_onGamepadConnected`
- Metadata signature: `public static void add_onGamepadConnected(GamepadManager.OnConnectionChnageCallback value) { }`
- Native interval: `188` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    long long field_18;
} struct_0;

typedef struct struct_1 {
    char padding_0[184];
    struct struct_0 *field_b8;
} struct_1;

extern struct_1 *g_1eefb00;
extern char g_1fab0f8;

long long GamepadManager_add_onGamepadConnected(long long a0)
{
    long long v0;  // x20
    long long v1;  // x20
    long long v2;  // x8
    long long v3;  // x20

    if (!(g_1fab0f8 & 1))
    {
        sub_f7d92c(&g_1eefb00);
        sub_f7d92c("qj");
        g_1fab0f8 = 1;
    }
    v0 = g_1eefb00->field_b8->field_18;
    while (true)
    {
        v1 = v0;
        v2 = Delegate__Combine(v1, a0, 0);
        if (v2 && *((long long *)v2) != g_1ef3200)
            sub_f7df10(v2);
        v3 = sub_f60ebc(&g_1eefb00->field_b8->field_18, v2, v1);
        v0 = v3;
        if (v1 == v0)
            return v3;
    }
}
```

## `GamepadManager.remove_onGamepadConnected` — RVA `0xc2a69c`

- Decompiled symbol: `GamepadManager_remove_onGamepadConnected`
- Metadata signature: `public static void remove_onGamepadConnected(GamepadManager.OnConnectionChnageCallback value) { }`
- Native interval: `188` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    long long field_18;
} struct_0;

typedef struct struct_1 {
    char padding_0[184];
    struct struct_0 *field_b8;
} struct_1;

extern struct_1 *g_1eefb00;
extern char g_1fab0f9;

long long GamepadManager_remove_onGamepadConnected(long long a0)
{
    long long v0;  // x20
    long long v1;  // x20
    long long v2;  // x8
    long long v3;  // x20

    if (!(g_1fab0f9 & 1))
    {
        sub_f7d92c(&g_1eefb00);
        sub_f7d92c("qj");
        g_1fab0f9 = 1;
    }
    v0 = g_1eefb00->field_b8->field_18;
    while (true)
    {
        v1 = v0;
        v2 = Delegate__Remove(v1, a0, 0);
        if (v2 && *((long long *)v2) != g_1ef3200)
            sub_f7df10(v2);
        v3 = sub_f60ebc(&g_1eefb00->field_b8->field_18, v2, v1);
        v0 = v3;
        if (v1 == v0)
            return v3;
    }
}
```

## `GamepadManager.add_onGamepadActivated` — RVA `0xc2a758`

- Decompiled symbol: `GamepadManager_add_onGamepadActivated`
- Metadata signature: `public static void add_onGamepadActivated(GamepadManager.OnConnectionChnageCallback value) { }`
- Native interval: `188` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[32];
    long long field_20;
} struct_0;

typedef struct struct_1 {
    char padding_0[184];
    struct struct_0 *field_b8;
} struct_1;

extern struct_1 *g_1eefb00;
extern char g_1fab0fa;

long long GamepadManager_add_onGamepadActivated(long long a0)
{
    long long v0;  // x20
    long long v1;  // x20
    long long v2;  // x8
    long long v3;  // x20

    if (!(g_1fab0fa & 1))
    {
        sub_f7d92c(&g_1eefb00);
        sub_f7d92c("qj");
        g_1fab0fa = 1;
    }
    v0 = g_1eefb00->field_b8->field_20;
    while (true)
    {
        v1 = v0;
        v2 = Delegate__Combine(v1, a0, 0);
        if (v2 && *((long long *)v2) != g_1ef3200)
            sub_f7df10(v2);
        v3 = sub_f60ebc(&g_1eefb00->field_b8->field_20, v2, v1);
        v0 = v3;
        if (v1 == v0)
            return v3;
    }
}
```

## `GamepadManager.remove_onGamepadActivated` — RVA `0xc2a814`

- Decompiled symbol: `GamepadManager_remove_onGamepadActivated`
- Metadata signature: `public static void remove_onGamepadActivated(GamepadManager.OnConnectionChnageCallback value) { }`
- Native interval: `188` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[32];
    long long field_20;
} struct_0;

typedef struct struct_1 {
    char padding_0[184];
    struct struct_0 *field_b8;
} struct_1;

extern struct_1 *g_1eefb00;
extern char g_1fab0fb;

long long GamepadManager_remove_onGamepadActivated(long long a0)
{
    long long v0;  // x20
    long long v1;  // x20
    long long v2;  // x8
    long long v3;  // x20

    if (!(g_1fab0fb & 1))
    {
        sub_f7d92c(&g_1eefb00);
        sub_f7d92c("qj");
        g_1fab0fb = 1;
    }
    v0 = g_1eefb00->field_b8->field_20;
    while (true)
    {
        v1 = v0;
        v2 = Delegate__Remove(v1, a0, 0);
        if (v2 && *((long long *)v2) != g_1ef3200)
            sub_f7df10(v2);
        v3 = sub_f60ebc(&g_1eefb00->field_b8->field_20, v2, v1);
        v0 = v3;
        if (v1 == v0)
            return v3;
    }
}
```

## `GamepadManager.add_onChange` — RVA `0xc2a8d0`

- Decompiled symbol: `GamepadManager_add_onChange`
- Metadata signature: `public static void add_onChange(Action value) { }`
- Native interval: `188` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[40];
    long long field_28;
} struct_0;

typedef struct struct_1 {
    char padding_0[184];
    struct struct_0 *field_b8;
} struct_1;

extern struct_1 *g_1eefb00;
extern char g_1fab0fc;

long long GamepadManager_add_onChange(long long a0)
{
    long long v0;  // x20
    long long v1;  // x20
    long long v2;  // x8
    long long v3;  // x20

    if (!(g_1fab0fc & 1))
    {
        sub_f7d92c("++");
        sub_f7d92c(&g_1eefb00);
        g_1fab0fc = 1;
    }
    v0 = g_1eefb00->field_b8->field_28;
    while (true)
    {
        v1 = v0;
        v2 = Delegate__Combine(v1, a0, 0);
        if (v2 && *((long long *)v2) != g_1eee648)
            sub_f7df10(v2);
        v3 = sub_f60ebc(&g_1eefb00->field_b8->field_28, v2, v1);
        v0 = v3;
        if (v1 == v0)
            return v3;
    }
}
```

## `GamepadManager.remove_onChange` — RVA `0xc2a98c`

- Decompiled symbol: `GamepadManager_remove_onChange`
- Metadata signature: `public static void remove_onChange(Action value) { }`
- Native interval: `188` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[40];
    long long field_28;
} struct_0;

typedef struct struct_1 {
    char padding_0[184];
    struct struct_0 *field_b8;
} struct_1;

extern struct_1 *g_1eefb00;
extern char g_1fab0fd;

long long GamepadManager_remove_onChange(long long a0)
{
    long long v0;  // x20
    long long v1;  // x20
    long long v2;  // x8
    long long v3;  // x20

    if (!(g_1fab0fd & 1))
    {
        sub_f7d92c("++");
        sub_f7d92c(&g_1eefb00);
        g_1fab0fd = 1;
    }
    v0 = g_1eefb00->field_b8->field_28;
    while (true)
    {
        v1 = v0;
        v2 = Delegate__Remove(v1, a0, 0);
        if (v2 && *((long long *)v2) != g_1eee648)
            sub_f7df10(v2);
        v3 = sub_f60ebc(&g_1eefb00->field_b8->field_28, v2, v1);
        v0 = v3;
        if (v1 == v0)
            return v3;
    }
}
```

## `GamepadManager.GetJoyAxisName` — RVA `0xc2aa48`

- Decompiled symbol: `GamepadManager_GetJoyAxisName`
- Metadata signature: `public static string GetJoyAxisName(int joyId, int axisId) { }`
- Native interval: `184` bytes
- Result: `pseudocode`

```c
extern long long g_1f11650;
extern char g_1fab0fe;

long long GamepadManager_GetJoyAxisName(unsigned int a0, unsigned int a1)
{
    long long v2;  // x0
    long long v3;  // x0
    unsigned long long v4;  // x0
    unsigned int v0;  // [bp-0x28]
    unsigned int v1;  // [bp-0x24]

    v0 = a1;
    v1 = a0;
    if (!(g_1fab0fe & 1))
    {
        sub_f7d92c("MT");
        sub_f7d92c(&g_1f11650);
        g_1fab0fe = 1;
    }
    if (3 >= a0 && 10 > a1)
    {
        v2 = Int32__ToString(&v1, 0);
        v3 = Int32__ToString(&v0, 0);
        v4 = String__Concat(g_1f11650, v2, v3, 0);
        return String__Concat(g_1f11650, v2, v3, 0);
    }
    return g_1ef18f0->field_b8->field_0;
}
```

## `GamepadManager.GetJoyKeyCode` — RVA `0xc2ab00`

- Decompiled symbol: `GamepadManager_GetJoyKeyCode`
- Metadata signature: `public static KeyCode GetJoyKeyCode(int joyId, int keyId) { }`
- Native interval: `44` bytes
- Result: `pseudocode`

```c
unsigned long long GamepadManager_GetJoyKeyCode(unsigned int a0, unsigned long long a1)
{
    if (3 < a0)
    {
        return 0;
    }
    else if (((char)(a1 >> 31) & 1))
    {
        return 0;
    }
    else if ((unsigned int)a1 < 20)
    {
        return (unsigned int)a1 + 20 * a0 + 350;
    }
    else
    {
        return 0;
    }
}
```

## `GamepadManager.ctor` — RVA `0xc2ab2c`

- Decompiled symbol: `GamepadManager_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `860` bytes
- Result: `pseudocode`

```c
extern long long g_1eed9f0;
extern long long g_1eee758;
extern long long g_1eef1b0;
extern long long g_1ef0548;
extern long long g_1ef9050;
extern long long g_1ef9058;
extern char g_1fab0ff;

long long GamepadManager_ctor(long long a0)
{
    unsigned long long v8;  // x30
    unsigned long long v9;  // x25
    unsigned long long v10;  // x24
    unsigned long long v11;  // x23
    unsigned long long v12;  // x22
    unsigned long long v13;  // x21
    unsigned long long v14;  // x20
    unsigned long long v15;  // x19
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
    if (!(g_1fab0ff & 1))
    {
        sub_f7d92c(&g_1eee758);
        sub_f7d92c(&g_1eef1b0);
        sub_f7d92c("cj");
        sub_f7d92c(&g_1ef0548);
        sub_f7d92c(&g_1ef9058);
        sub_f7d92c(&g_1ef9050);
        sub_f7d92c(&g_1eed9f0);
        g_1fab0ff = 1;
    }
    ComponentBase__ctor(a0, 0); /* do not return */
}
```

## `GamepadManager.OnInitComponent` — RVA `0xc2b2d4`

- Decompiled symbol: `GamepadManager_OnInitComponent`
- Metadata signature: `protected override void OnInitComponent() { }`
- Native interval: `24` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[40];
    long long field_28;
} struct_0;

long long GamepadManager_OnInitComponent(struct_0 *a0)
{
    unsigned long long v0;  // x0

    if (a0->field_28)
    {
        v0 = CustomGamepadProfileBank__LoadFromPlayerPrefs(a0->field_28);
        return CustomGamepadProfileBank__LoadFromPlayerPrefs(a0->field_28);
    }
    sub_f7db74(0);
}
```

## `GamepadManager.OnDestroyComponent` — RVA `0xc2b2f0`

- Decompiled symbol: `GamepadManager_OnDestroyComponent`
- Metadata signature: `protected override void OnDestroyComponent() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long GamepadManager_OnDestroyComponent(void)
{
    unsigned long v0;  // x0

    return v0;
}
```

## `GamepadManager.OnEnableComponent` — RVA `0xc2b2f4`

- Decompiled symbol: `GamepadManager_OnEnableComponent`
- Metadata signature: `protected override void OnEnableComponent() { }`
- Native interval: `344` bytes
- Result: `pseudocode`

```c
typedef struct struct_3 {
    char padding_0[48];
    char field_30;
} struct_3;

typedef struct struct_2 {
    long long field_0;
} struct_2;

typedef struct struct_1 {
    char padding_0[184];
    struct struct_2 *field_b8;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_1 *g_1eefb00;
extern struct_0 *g_1ef0c58;
extern char g_1fab100;
extern char g_1fab1dd;

unsigned long long GamepadManager_OnEnableComponent(struct_3 *a0)
{
    unsigned long long v0;  // x0
    unsigned long long v1;  // x0
    unsigned long long v2;  // x0
    unsigned long long v3;  // x0
    unsigned long long v4;  // x0
    unsigned long long v5;  // x0

    if (!(g_1fab100 & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab100 = 1;
    }
    if (!g_1fab1dd)
    {
        sub_f7d92c(&g_1eefb00);
        g_1fab1dd = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (((char)Object__op_Equality(g_1eefb00->field_b8->field_0, 0, 0) & 1))
    {
        v0 = GamepadManager__SetAsMain(a0);
        if (!a0->field_30)
            return v0;
        v1 = CFUtils__get_editorStopped(0);
        if (((char)v1 & 1))
            return v1;
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        v2 = Object__DontDestroyOnLoad();
        return Object__DontDestroyOnLoad();
    }
    else
    {
        if (!g_1fab1dd)
        {
            sub_f7d92c(&g_1eefb00);
            g_1fab1dd = 1;
        }
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        v3 = Object__op_Inequality(g_1eefb00->field_b8->field_0, a0, 0);
        if (!((char)v3 & 1))
            return v3;
        v4 = CFUtils__get_editorStopped(0);
        if (!((char)v4 & 1))
        {
            v5 = Behaviour__set_enabled();
            return Behaviour__set_enabled();
        }
        return v4;
    }
}
```

## `GamepadManager.SetAsMain` — RVA `0xc2b44c`

- Decompiled symbol: `GamepadManager_SetAsMain`
- Metadata signature: `public void SetAsMain() { }`
- Native interval: `432` bytes
- Result: `pseudocode`

```c
extern long long g_1eeed00;
extern long long g_1ef0c58;
extern long long g_1efede8;
extern char g_1fab102;

long long GamepadManager_SetAsMain(long long a0)
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
    if (!(g_1fab102 & 1))
    {
        sub_f7d92c("++");
        sub_f7d92c(&g_1eeed00);
        sub_f7d92c(&g_1efede8);
        sub_f7d92c(&g_1ef0c58);
        g_1fab102 = 1;
    }
    Behaviour__set_enabled(a0, 1, 0);
    GamepadManager__IsMain(a0); /* do not return */
}
```

## `GamepadManager.IsMain` — RVA `0xc2b5fc`

- Decompiled symbol: `GamepadManager_IsMain`
- Metadata signature: `public bool IsMain() { }`
- Native interval: `144` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern long long g_1eefb00;
extern struct_0 *g_1ef0c58;
extern char g_1fab101;
extern char g_1fab1dd;

void GamepadManager_IsMain(unsigned long a0)
{
    unsigned long long v4;  // x30
    unsigned long long v5;  // x21
    unsigned long long v6;  // x20
    unsigned long long v7;  // x19
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x18]
    unsigned long long v2;  // [bp-0x10]
    unsigned long long v3;  // [bp-0x8]

    v0 = v4;
    v1 = v5;
    v2 = v6;
    v3 = v7;
    if (!(g_1fab101 & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab101 = 1;
    }
    if (!g_1fab1dd)
    {
        sub_f7d92c(&g_1eefb00);
        g_1fab1dd = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    Object__op_Equality();
    return;
}
```

## `GamepadManager.RemoveAsMain` — RVA `0xc2b68c`

- Decompiled symbol: `GamepadManager_RemoveAsMain`
- Metadata signature: `public void RemoveAsMain() { }`
- Native interval: `336` bytes
- Result: `pseudocode`

```c
typedef struct struct_3 {
    long long field_0;
} struct_3;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

typedef struct struct_1 {
    char padding_0[224];
    unsigned int field_e0;
} struct_1;

typedef struct struct_2 {
    char padding_0[184];
    struct struct_3 *field_b8;
} struct_2;

extern struct_0 *g_1eeed00;
extern struct_2 *g_1eefb00;
extern struct_1 *g_1ef0c58;
extern long long g_1efede8;
extern char g_1fab103;
extern char g_1fab1dd;
extern char g_1fab1de;

long long GamepadManager_RemoveAsMain(long long a0)
{
    long long v0;  // x0
    unsigned long long v1;  // x0

    if (!(g_1fab103 & 1))
    {
        sub_f7d92c("++");
        sub_f7d92c(&g_1eeed00);
        sub_f7d92c(&g_1efede8);
        sub_f7d92c(&g_1ef0c58);
        g_1fab103 = 1;
    }
    if (!g_1fab1dd)
    {
        sub_f7d92c(&g_1eefb00);
        g_1fab1dd = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (((char)Object__op_Equality(g_1eefb00->field_b8->field_0, a0, 0) & 1))
    {
        if (!g_1fab1de)
        {
            sub_f7d92c(&g_1eefb00);
            g_1fab1de = 1;
        }
        g_1eefb00->field_b8->field_0 = 0;
        sub_f7d8d0(g_1eefb00->field_b8, 0);
    }
    v0 = sub_f7db70(g_1eee648);
    Action__ctor(v0, a0, g_1efede8, 0);
    if (!g_1eeed00->field_e0)
        sub_f7da5c(g_1eeed00);
    v1 = CF2Input__remove_onActiveRigChange(v0);
    return CF2Input__remove_onActiveRigChange(v0);
}
```

## `GamepadManager.OnActiveRigChange` — RVA `0xc2b8b8`

- Decompiled symbol: `GamepadManager_OnActiveRigChange`
- Metadata signature: `private void OnActiveRigChange() { }`
- Native interval: `484` bytes
- Result: `pseudocode`
- Heuristic layout hint: `GamepadManager_Recovered` matched 3 offsets against `GamepadManager` metadata (confidence 1.00).

```c
typedef struct struct_5 {
    char padding_0[24];
    unsigned int field_18;
} struct_5;

typedef struct GamepadManager_Recovered {
    char padding_0[112];
    struct struct_2 *freeGamepads;
    struct struct_3 *connectedGamepads;
    long long gamepadsCombined;
} GamepadManager_Recovered;

typedef struct struct_1 {
    char padding_0[184];
    struct struct_0 *field_b8;
    char padding_c0[32];
    unsigned int field_e0;
} struct_1;

typedef struct struct_2 {
    char padding_0[24];
    int field_18;
} struct_2;

typedef struct struct_3 {
    char padding_0[24];
    int field_18;
} struct_3;

typedef struct struct_0 {
    char padding_0[24];
    long long field_18;
} struct_0;

extern struct_1 *g_1eeed00;
extern long long g_1ef9070;
extern long long g_1ef9078;
extern char g_1fab105;
extern char g_1fab1df;

struct_5 * GamepadManager_OnActiveRigChange(struct_4 *ptr)
{
    long long v0;  // x21
    struct_1 *v1;  // x0
    unsigned long long v10;  // x0
    struct_2 *v2;  // x0
    int v3;  // w21
    long long v4;  // x22
    struct_1 *v5;  // x0
    struct_3 *v6;  // x0
    int v7;  // w21
    long long v8;  // x22
    struct_1 *v9;  // x0

    if (!(g_1fab105 & 1))
    {
        sub_f7d92c(&g_1eeed00);
        sub_f7d92c(&g_1ef9070);
        sub_f7d92c(&g_1ef9078);
        g_1fab105 = 1;
    }
    v0 = ptr->field_80;
    if (!g_1eeed00->field_e0)
        sub_f7da5c(g_1eeed00);
    if (!g_1fab1df)
    {
        sub_f7d92c(&g_1eeed00);
        g_1fab1df = 1;
    }
    v1 = g_1eeed00;
    if (!g_1eeed00->field_e0)
    {
        sub_f7da5c(g_1eeed00);
        v1 = g_1eeed00;
    }
    if (v0)
    {
        GamepadManager_Gamepad__SetRig(v0, v1->field_b8->field_18);
        v2 = ptr->field_70;
        if (v2)
        {
            v3 = 0;
            do
            {
                if (v2->field_18 <= v3)
                {
                    v6 = ptr->field_78;
                    if (v6)
                    {
                        v7 = 0;
                        do
                        {
                            if (v6->field_18 <= v7)
                                return v6;
                            v8 = sub_14a30c0();
                            if (!g_1eeed00->field_e0)
                                sub_f7da5c(g_1eeed00);
                            if (!g_1fab1df)
                            {
                                sub_f7d92c(&g_1eeed00);
                                g_1fab1df = 1;
                            }
                            v9 = g_1eeed00;
                            if (!g_1eeed00->field_e0)
                            {
                                sub_f7da5c(g_1eeed00);
                                v9 = g_1eeed00;
                            }
                        } while (v8 && (GamepadManager_Gamepad__SetRig(v8, v9->field_b8->field_18), v6 = (struct_3 *)ptr->field_78, v7 = (int)(v7 + 1), v6));
                    }
                }
                v4 = sub_14a30c0();
                if (!g_1eeed00->field_e0)
                    sub_f7da5c(g_1eeed00);
                if (!g_1fab1df)
                {
                    sub_f7d92c(&g_1eeed00);
                    g_1fab1df = 1;
                }
                v5 = g_1eeed00;
                if (!g_1eeed00->field_e0)
                {
                    sub_f7da5c(g_1eeed00);
                    v5 = g_1eeed00;
                }
            } while (v4 && (GamepadManager_Gamepad__SetRig(v4, v5->field_b8->field_18), v2 = (struct_2 *)ptr->field_70, v3 = (int)(v3 + 1), v2));
        }
    }
    v10 = sub_f7db74();
    return sub_f7db74();
}
```

## `GamepadManager.GetCustomProfileBank` — RVA `0xc2bb78`

- Decompiled symbol: `GamepadManager_GetCustomProfileBank`
- Metadata signature: `public CustomGamepadProfileBank GetCustomProfileBank() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[40];
    unsigned long long field_28;
} struct_0;

long long GamepadManager_GetCustomProfileBank(struct_0 *a0)
{
    return a0->field_28;
}
```

## `GamepadManager.OnDisableComponent` — RVA `0xc2bb80`

- Decompiled symbol: `GamepadManager_OnDisableComponent`
- Metadata signature: `protected override void OnDisableComponent() { }`
- Native interval: `228` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[104];
    struct struct_0 *field_68;
} struct_1;

typedef struct struct_0 {
    char padding_0[24];
    int field_18;
} struct_0;

extern long long g_1eefb00;
extern long long g_1ef9070;
extern long long g_1ef9078;
extern char g_1fab104;

void GamepadManager_OnDisableComponent(struct_1 *ptr)
{
    unsigned long long v4;  // x30
    unsigned long long v5;  // x21
    unsigned long long v6;  // x20
    unsigned long long v7;  // x19
    struct_0 *i;  // x0
    int v9;  // w20
    long long v10;  // x0
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x18]
    unsigned long long v2;  // [bp-0x10]
    unsigned long long v3;  // [bp-0x8]

    v0 = v4;
    v1 = v5;
    v2 = v6;
    v3 = v7;
    if (!(g_1fab104 & 1))
    {
        sub_f7d92c(&g_1eefb00);
        sub_f7d92c(&g_1ef9070);
        sub_f7d92c(&g_1ef9078);
        g_1fab104 = 1;
    }
    i = ptr->field_68;
    if (i)
    {
        v9 = 0;
        do
        {
            if (i->field_18 <= v9)
                GamepadManager__IsMain(ptr); /* do not return */
            v10 = sub_14a30c0();
            if (v10)
                GamepadManager__DisconnectGamepad(ptr, v10, 3);
            i = ptr->field_68;
            v9 += 1;
        } while (i);
    }
    sub_f7db74(i);
    GamepadManager__IsMain(ptr); /* do not return */
}
```

## `GamepadManager.DisconnectGamepad` — RVA `0xc2bc64`

- Decompiled symbol: `GamepadManager_DisconnectGamepad`
- Metadata signature: `private void DisconnectGamepad(GamepadManager.Gamepad g, GamepadManager.DisconnectionReason reason) { }`
- Native interval: `168` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[32];
    char field_20;
} struct_0;

extern long long g_1eefb00;
extern char g_1fab10e;

void GamepadManager_DisconnectGamepad(long long a0, struct_0 *a1, unsigned int a2)
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
    if (!(g_1fab10e & 1))
    {
        sub_f7d92c(&g_1eefb00);
        g_1fab10e = 1;
    }
    if (a1)
    {
        if (a1->field_20)
            GamepadManager__DisactivateGamepad(a0, a1, a2);
        GamepadManager__IsMain(a0); /* do not return */
    }
    sub_f7db74();
}
```

## `GamepadManager.Update` — RVA `0xc2c004`

- Decompiled symbol: `GamepadManager_Update`
- Metadata signature: `private void Update() { }`
- Native interval: `428` bytes
- Result: `pseudocode`

```c
typedef struct struct_3 {
    char padding_0[34];
    char field_22;
} struct_3;

typedef struct struct_1 {
    char padding_0[184];
    struct struct_0 *field_b8;
    char padding_c0[32];
    unsigned int field_e0;
} struct_1;

typedef struct struct_0 {
    char padding_0[24];
    long long field_18;
} struct_0;

typedef struct struct_2 {
    char padding_0[224];
    unsigned int field_e0;
} struct_2;

extern struct_1 *g_1eeed00;
extern struct_2 *g_1ef0c58;
extern long long g_1ef9070;
extern long long g_1ef9078;
extern char g_1fab106;
extern char g_1fab1df;

long long GamepadManager_Update(unsigned long long *ptr)
{
    unsigned long long v0;  // x0
    int v1;  // w20
    int v2;  // w20
    struct_3 *v3;  // x0
    struct_1 *v4;  // x0
    long long v5;  // x0
    unsigned long long v6;  // x0

    if (!(g_1fab106 & 1))
    {
        sub_f7d92c(&g_1eeed00);
        sub_f7d92c(&g_1ef9070);
        sub_f7d92c(&g_1ef9078);
        sub_f7d92c(&g_1ef0c58);
        g_1fab106 = 1;
    }
    GamepadManager__CheckJoystickConnections(ptr);
    v0 = ptr[15];
    if (v0)
    {
        v1 = 0;
        do
        {
            if (*((int *)(v0 + 24)) <= v1)
            {
                v0 = ptr[13];
                if (v0)
                {
                    v2 = 0;
                    do
                    {
                        if (*((int *)(v0 + 24)) > v2)
                        {
                            v3 = sub_14a30c0();
                            if (!v3 || v3->field_22)
                                continue;
                            v0 = ptr[16];
                            if (!v0)
                                break;
                            GamepadManager_Gamepad__ApplyGamepadState(v0);
                        }
                        else
                        {
                            v0 = ptr[16];
                            if (v0)
                            {
                                GamepadManager_Gamepad__Update(v0);
                                if (!g_1eeed00->field_e0)
                                    sub_f7da5c(g_1eeed00);
                                if (!g_1fab1df)
                                {
                                    sub_f7d92c(&g_1eeed00);
                                    g_1fab1df = 1;
                                }
                                v4 = g_1eeed00;
                                if (!g_1eeed00->field_e0)
                                {
                                    sub_f7da5c(g_1eeed00);
                                    v4 = g_1eeed00;
                                }
                                if (!g_1ef0c58->field_e0)
                                    sub_f7da5c(g_1ef0c58);
                                v5 = Object__op_Inequality(v4->field_b8->field_18, 0, 0);
                                if (!((char)v5 & 1))
                                    return v5;
                                v6 = GamepadManager__ApplyToRig(ptr, v4->field_b8->field_18);
                                return GamepadManager__ApplyToRig(ptr, v4->field_b8->field_18);
                            }
                            break;
                        }
                    } while ((v0 = ptr[13], v2 = (int)(v2 + 1), v0));
                }
            }
        } while ((v0 = (unsigned long long)sub_14a30c0(), v0 && (GamepadManager_Gamepad__Update(), v0 = ptr[15], v1 = (int)(v1 + 1), v0)));
    }
    sub_f7db74(v0);
}
```

## `GamepadManager.CheckJoystickConnections` — RVA `0xc2c1b0`

- Decompiled symbol: `GamepadManager_CheckJoystickConnections`
- Metadata signature: `private void CheckJoystickConnections() { }`
- Native interval: `76` bytes
- Result: `pseudocode`

```c
unsigned long long GamepadManager_CheckJoystickConnections(unsigned int *ptr)
{
    unsigned long long v0;  // x0
    unsigned int v1;  // s1
    unsigned int v2;  // s0
    unsigned int v3;  // s0
    unsigned long v4;  // 4146
    unsigned long long v5;  // x0

    GamepadManager__CheckUnactivatedGamepads();
    v0 = Time__get_unscaledDeltaTime(0);
    v1 = ptr[13];
    v3 = ptr[14] + v2;
    ptr[14] = v3;
    v4 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(v3, v1)) >> 5 & 3 | (unsigned long long)(CmpF(v3, v1) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v3, v1)) >> 5 & 3 | (unsigned long long)(CmpF(v3, v1) & 1)) & ((unsigned long long)(char)(CmpF(v3, v1)) >> 5 & 3 | (unsigned long long)(CmpF(v3, v1) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if ((char)v4)
        return v0;
    v5 = GamepadManager__ConnectJoysticks(ptr);
    return GamepadManager__ConnectJoysticks(ptr);
}
```

## `GamepadManager.ApplyToRig` — RVA `0xc2c42c`

- Decompiled symbol: `GamepadManager_ApplyToRig`
- Metadata signature: `private void ApplyToRig(InputRig rig) { }`
- Native interval: `312` bytes
- Result: `pseudocode`
- Heuristic layout hint: `GamepadManager_Recovered` matched 2 offsets against `GamepadManager` metadata (confidence 1.00).

```c
typedef struct struct_2 {
    char padding_0[232];
    struct struct_1 *field_e8;
    long long field_f0;
} struct_2;

typedef struct GamepadManager_Recovered {
    char padding_0[104];
    struct struct_3 *activeGamepads;
    char padding_70[16];
    long long gamepadsCombined;
} GamepadManager_Recovered;

typedef struct struct_3 {
    char padding_0[24];
    unsigned int field_18;
} struct_3;

typedef struct struct_5 {
    char padding_0[34];
    char field_22;
} struct_5;

typedef struct struct_1 {
    char padding_0[24];
    unsigned int field_18;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern long long g_1ef9070;
extern long long g_1ef9078;
extern char g_1fab107;

unsigned long long GamepadManager_ApplyToRig(struct_4 *ptr, struct_2 *p)
{
    unsigned long long v0;  // x0
    struct_3 *v1;  // x0
    unsigned long long v2;  // x21
    struct_5 *v3;  // x0
    struct_1 *addr;  // x8
    unsigned long v5;  // x9
    long long v6;  // x0
    unsigned long long v7;  // x0

    if (!(g_1fab107 & 1))
    {
        sub_f7d92c(&g_1ef9070);
        sub_f7d92c(&g_1ef9078);
        sub_f7d92c(&g_1ef0c58);
        g_1fab107 = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v0 = Object__op_Equality(p, 0, 0);
    if (((char)v0 & 1))
        return v0;
    v1 = ptr->field_68;
    if (ptr->field_68)
    {
        v2 = 0;
        do
        {
            if (v1->field_18 <= v2)
                goto LABEL_0x102c538;
            v3 = sub_14a30c0();
            if (!v3 || v3->field_22)
                continue;
            if (!p || !((addr = (struct_1 *)p->field_e8, addr)))
                break;
            v5 = addr->field_18;
            if ((v5 & 4294967295) <= v2)
                continue;
            if (v5 <= v2)
                sub_f7db7c();
            if (!*((long long *)&addr[1].padding_0[4 + 8 * v2]))
                break;
            InputRig_GamepadConfig__SyncGamepad();
        } while ((v1 = (struct_3 *)ptr->field_68, v2 += 1, v1));
    }
    do
    {
        do
        {
            sub_f7db74(v6);
        } while (!p);
    } while (!p->field_f0);
    v7 = InputRig_GamepadConfig__SyncGamepad(p->field_f0, ptr->field_80, p, 0);
    return InputRig_GamepadConfig__SyncGamepad(p->field_f0, ptr->field_80, p, 0);
}
```

## `GamepadManager.CheckUnactivatedGamepads` — RVA `0xc2c564`

- Decompiled symbol: `GamepadManager_CheckUnactivatedGamepads`
- Metadata signature: `private void CheckUnactivatedGamepads() { }`
- Native interval: `300` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[120];
    void* field_78;
} struct_0;

extern long long g_1eefb00;
extern long long g_1ef9070;
extern long long g_1ef9078;
extern char g_1fab110;

void GamepadManager_CheckUnactivatedGamepads(struct_0 *ptr)
{
    unsigned long long v6;  // x30
    unsigned long long v7;  // x23
    unsigned long long v8;  // x22
    unsigned long long v9;  // x21
    unsigned long long v10;  // x20
    unsigned long long v11;  // x19
    void* i;  // x0
    unsigned int v13;  // w20
    void* v14;  // x21
    unsigned long long v0;  // [bp-0x30]
    unsigned long long v1;  // [bp-0x28]
    unsigned long long v2;  // [bp-0x20]
    unsigned long long v3;  // [bp-0x18]
    unsigned long long v4;  // [bp-0x10]
    unsigned long long v5;  // [bp-0x8]

    v0 = v6;
    v1 = v7;
    v2 = v8;
    v3 = v9;
    v4 = v10;
    v5 = v11;
    if (!(g_1fab110 & 1))
    {
        sub_f7d92c(&g_1eefb00);
        sub_f7d92c(&g_1ef9070);
        sub_f7d92c(&g_1ef9078);
        g_1fab110 = 1;
    }
    i = ptr->field_78;
    if (i)
    {
        v13 = 0;
        do
        {
            if ((int)i[24] <= v13)
                GamepadManager__IsMain(ptr); /* do not return */
            i = sub_14a30c0();
            if (!i)
                break;
            v14 = i;
            if ((char)i[33] && (long long)v14[24] && !(char)v14[34] && !(char)v14[32] && (((char)GamepadManager_Gamepad__AnyInternalKeyPressed(v14) & 1) || ((char)GamepadManager_Gamepad__AnyInternalAxisPressed(v14) & 1)))
                GamepadManager__ActivateGamepad(ptr, v14);
            i = ptr->field_78;
            v13 += 1;
        } while (i);
    }
    sub_f7db74(i);
    GamepadManager__IsMain(ptr); /* do not return */
}
```

## `GamepadManager.ConnectJoysticks` — RVA `0xc2c690`

- Decompiled symbol: `GamepadManager_ConnectJoysticks`
- Metadata signature: `private void ConnectJoysticks() { }`
- Native interval: `552` bytes
- Result: `pseudocode`
- Heuristic layout hint: `GamepadManager_Recovered` matched 3 offsets against `GamepadManager` metadata (confidence 1.00).

```c
typedef struct GamepadManager_Recovered {
    char padding_0[56];
    unsigned int elapsedSinceLastConnectionCheck;
    char padding_3c[60];
    struct struct_0 *connectedGamepads;
    char padding_80[16];
    long long deviceConnections;
} GamepadManager_Recovered;

typedef struct struct_0 {
    char padding_0[33];
    char field_21;
    char padding_22[6];
    long long field_28;
    unsigned int field_30;
} struct_0;

typedef struct struct_2 {
    char padding_0[33];
    char field_21;
    char padding_22[6];
    unsigned long long field_28;
    unsigned int field_30;
} struct_2;

extern long long g_1eefb00;
extern long long g_1ef9070;
extern long long g_1ef9078;
extern char g_1fab10f;

void GamepadManager_ConnectJoysticks(struct_1 *ptr)
{
    long long v0;  // x0
    struct_1 *p;  // x20
    long long v9;  // x22
    long long v10;  // x0
    long long v11;  // x0
    struct_0 *v2;  // x0, Other Possible Types: struct_2 *
    unsigned long long v3;  // x25
    unsigned int v4;  // w24
    int i;  // w20
    struct_0 *addr;  // x21
    long long v7;  // x0
    unsigned int v8;  // w20

    if (!(g_1fab10f & 1))
    {
        sub_f7d92c(&g_1eefb00);
        sub_f7d92c(&g_1ef9070);
        sub_f7d92c(&g_1ef9078);
        g_1fab10f = 1;
    }
    ptr->field_38 = 0;
    v0 = Input__GetJoystickNames(0);
    ptr->field_90 = v0;
    p = &ptr->field_90;
    sub_f7d8d0(p, v0);
    v2 = *((long long *)&p->padding_0[24]);
    if (v2)
    {
        v3 = 0;
        v4 = 0;
        i = 0;
    }
    else
    {
LABEL_102c79c:
        sub_f7db74(v2);
        goto LABEL_102c7a0;
    }
    while (*((int *)&v2->padding_0[24]) > i)
    {
        v2 = sub_14a30c0();
        if (!v2)
            goto LABEL_102c79c;
        addr = v2;
        if (v2->field_21)
        {
            v7 = GamepadManager__GetConnectedDeviceName(ptr, addr->field_30);
            if (((char)String__op_Equality(v7, addr->field_28, 0) & 1))
            {
                v4 |= 1 << ((char)addr->field_30 & 31);
            }
            else
            {
                GamepadManager__DisconnectGamepad(ptr, addr, 2);
                v3 = 1;
            }
        }
        v2 = ptr->field_78;
        i += 1;
        goto LABEL_102c79c;
    }
LABEL_102c7a0:
    v8 = 0;
    while (true)
    {
        v9 = GamepadManager__GetConnectedDeviceName(ptr, v8);
        if (!((char)String__IsNullOrEmpty(v9, 0) & 1) && !((char)(v4 >> ((char)v8 & 31)) & 1) && !((v10 = GamepadManager__FindDisconnectedGamepad(ptr, (unsigned long long)v8, v9), !v10 && !((v10 = GamepadManager__AddConnectedGamepad(ptr), v10)))))
        {
            GamepadManager_Gamepad__ConnectToJoy(v10, v8, v9);
            v11 = GamepadManager__GetProfileForDevice(ptr, v9);
            if (v11)
            {
                GamepadManager_Gamepad__SetProfile(v10, v11);
                break;
            }
        }
        else
        {
            v8 += 1;
            if (v8 == 4)
            {
                if (((char)v3 & 1))
                    GamepadManager__IsMain(ptr); /* do not return */
                return;
            }
        }
    }
    GamepadManager__IsMain(ptr); /* do not return */
}
```

## `GamepadManager.GetConnectedDeviceName` — RVA `0xc2c8b8`

- Decompiled symbol: `GamepadManager_GetConnectedDeviceName`
- Metadata signature: `private string GetConnectedDeviceName(int internalJoyId) { }`
- Native interval: `132` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

typedef struct struct_4 {
    char padding_0[144];
    unsigned long long field_90;
} struct_4;

extern char g_1fab108;

struct_0 * GamepadManager_GetConnectedDeviceName(struct_4 *ptr, unsigned int a1)
{
    unsigned long v0;  // x19
    unsigned long long v1;  // x8
    unsigned long v2;  // 4102
    struct_0 *v3;  // x0

    v0 = a1;
    if (!(g_1fab108 & 1))
    {
        sub_f7d92c("MT");
        g_1fab108 = 1;
    }
    if (!((char)(v0 >> 31) & 1))
    {
        v1 = ptr->field_90;
        if (v1 && *((int *)(v1 + 24)) > (unsigned int)v0)
        {
            v2 = arm64g_calculate_condition(147, (unsigned long long)(unsigned int)*((int *)(v1 + 24)), v0 & 4294967295, 0);
            if ((char)v2)
                sub_f7db7c();
            v3 = *((long long *)(v1 + (v0 & 4294967295) * 8 + 32));
            if (v3 && v3->field_10)
                return v3;
        }
    }
    return g_1ef18f0->field_b8->field_0;
}
```

## `GamepadManager.AddConnectedGamepad` — RVA `0xc2c93c`

- Decompiled symbol: `GamepadManager_AddConnectedGamepad`
- Metadata signature: `private GamepadManager.Gamepad AddConnectedGamepad() { }`
- Native interval: `292` bytes
- Result: `pseudocode`

```c
typedef struct struct_3 {
    char padding_0[16];
    unsigned long long field_10;
    unsigned int field_18;
    unsigned int field_1c;
} struct_3;

typedef struct struct_0 {
    char padding_0[16];
    unsigned long long field_10;
    int field_18;
    unsigned int field_1c;
} struct_0;

typedef struct struct_2 {
    char padding_0[32];
    struct struct_1 *field_20;
} struct_2;

typedef struct struct_1 {
    char padding_0[16];
    unsigned long long field_10;
    unsigned int field_18;
    unsigned int field_1c;
} struct_1;

extern long long g_1ef9058;
extern long long g_1ef9068;
extern long long g_1ef9070;
extern long long g_1ef9078;
extern char g_1fab109;

struct_3 * GamepadManager_AddConnectedGamepad(struct_0 **p, unsigned long a1, unsigned long a2)
{
    struct_0 *ptr;  // x0
    struct_0 *v1;  // x8
    struct_0 *v2;  // x19
    unsigned long long v3;  // x8
    unsigned long v4;  // x10
    struct_2 *addr;  // x8

    if (!(g_1fab109 & 1))
    {
        sub_f7d92c(&g_1ef9058);
        sub_f7d92c(&g_1ef9068);
        sub_f7d92c(&g_1ef9070);
        sub_f7d92c(&g_1ef9078);
        g_1fab109 = 1;
    }
    ptr = p[14];
    if (ptr)
    {
        if (ptr->field_18 >= 1)
        {
            ptr = sub_14a30c0();
            v1 = p[14];
            if (v1)
            {
                v2 = ptr;
                sub_14a48fc(v1, v1->field_18 - 1, g_1ef9068);
                ptr = p[15];
                if (ptr)
                {
                    v3 = ptr->field_10;
                    ptr->field_1c = ptr->field_1c + 1;
                    if (v3)
                    {
                        v4 = ptr->field_18;
                        if (*((int *)(v3 + 24)) <= (unsigned int)v4)
                        {
                            sub_14a3390();
                            return v2;
                        }
                        addr = v3 + v4 * 8;
                        ptr->field_18 = (unsigned int)v4 + 1;
                        addr->field_20 = v2;
                        sub_f7d8d0((struct struct_2 *)&addr->field_20, v2);
                        return v2;
                    }
                }
            }
        }
        else
        {
            return NULL;
        }
    }
    sub_f7db74(ptr);
}
```

## `GamepadManager.FindDisconnectedGamepad` — RVA `0xc2ca60`

- Decompiled symbol: `GamepadManager_FindDisconnectedGamepad`
- Metadata signature: `private GamepadManager.Gamepad FindDisconnectedGamepad(int internalJoyId, string deviceName) { }`
- Native interval: `248` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    char padding_0[33];
    char field_21;
    char padding_22[14];
    unsigned int field_30;
} struct_2;

typedef struct struct_1 {
    char padding_0[120];
    struct struct_0 *field_78;
} struct_1;

typedef struct struct_0 {
    char padding_0[33];
    char field_21;
    char padding_22[14];
    unsigned int field_30;
} struct_0;

extern long long g_1ef9070;
extern long long g_1ef9078;
extern char g_1fab10a;

struct_2 * GamepadManager_FindDisconnectedGamepad(struct_1 *ptr, unsigned int a1, unsigned long a2)
{
    struct_0 *v0;  // x0, Other Possible Types: struct_2 *
    struct_2 *v1;  // x24
    struct_2 *v2;  // x25
    int i;  // w22
    struct_0 *v4;  // x23

    if (!(g_1fab10a & 1))
    {
        sub_f7d92c(&g_1ef9070);
        sub_f7d92c(&g_1ef9078);
        g_1fab10a = 1;
    }
    v0 = ptr->field_78;
    if (v0)
    {
        v1 = NULL;
        v2 = NULL;
        i = 0;
    }
    else
    {
LABEL_102cb2c:
        sub_f7db74(v0);
        goto LABEL_102cb30;
    }
    while (*((int *)&v0->padding_0[24]) > i)
    {
        v0 = sub_14a30c0();
        if (!v0)
            goto LABEL_102cb2c;
        v4 = v0;
        if (!v0->field_21)
        {
            if (!v1)
                v1 = v4;
            if (((char)String__op_Equality() & 1))
            {
                if (v4->field_30 == a1)
                {
                    return v4;
                }
                else if (!v2)
                {
                    v2 = v4;
                }
            }
        }
        v0 = ptr->field_78;
        i += 1;
        goto LABEL_102cb2c;
    }
LABEL_102cb30:
    if (v2)
        return v2;
    return v1;
}
```

## `GamepadManager.ActivateGamepad` — RVA `0xc2cb58`

- Decompiled symbol: `GamepadManager_ActivateGamepad`
- Metadata signature: `private void ActivateGamepad(GamepadManager.Gamepad g) { }`
- Native interval: `508` bytes
- Result: `pseudocode`

```c
typedef struct struct_4 {
    char padding_0[104];
    struct struct_3 *field_68;
} struct_4;

typedef struct struct_0 {
    char padding_0[32];
    char field_20;
    char padding_21[19];
    int field_34;
} struct_0;

typedef struct struct_5 {
    char padding_0[16];
    unsigned long long field_10;
    unsigned int field_18;
    unsigned int field_1c;
} struct_5;

typedef struct struct_2 {
    char padding_0[32];
    struct struct_1 *field_20;
} struct_2;

typedef struct struct_3 {
    char padding_0[16];
    unsigned long long field_10;
    int field_18;
    unsigned int field_1c;
} struct_3;

typedef struct struct_1 {
    char padding_0[32];
    char field_20;
    char padding_21[19];
    unsigned int field_34;
} struct_1;

extern long long g_1eefb00;
extern long long g_1ef9058;
extern long long g_1ef9070;
extern long long g_1ef9078;
extern long long g_1ef9080;
extern char g_1fab10b;

struct_4 * GamepadManager_ActivateGamepad(struct_4 *ptr, struct_0 *addr)
{
    struct_4 *v0;  // x0
    struct_4 *v1;  // x0
    struct_4 *v2;  // x0
    unsigned long v3;  // x21
    struct_5 *p;  // x0
    unsigned long v5;  // x8
    struct_2 *ptr3;  // x0
    struct_4 *v7;  // x0
    struct_4 *v8;  // x0

    v0 = ptr;
    if (!(g_1fab10b & 1))
    {
        sub_f7d92c(&g_1eefb00);
        sub_f7d92c(&g_1ef9058);
        sub_f7d92c(&g_1ef9070);
        sub_f7d92c(&g_1ef9078);
        v1 = sub_f7d92c(&g_1ef9080);
        g_1fab10b = 1;
        v0 = v1;
    }
    v2 = v0;
    if (!addr)
        return v2;
    v3 = addr->field_34;
    if (!((char)(v3 >> 31) & 1))
    {
        p = ptr->field_68;
        if (!p)
            goto LABEL_102cc28;
        if (p->field_18 <= (unsigned int)v3 || sub_14a30c0())
            goto LABEL_102cbf4;
        p = ptr->field_68;
        if (!p)
            goto LABEL_102cc28;
        sub_14a3114(p, v3 & 4294967295, addr, g_1ef9080);
    }
    else
    {
LABEL_102cbf4:
        p = ptr->field_68;
        if (p)
        {
            v3 = 0;
            do
            {
            } while (p->field_18 > (unsigned int)v3 && sub_14a30c0() && (p = (struct_5 *)ptr->field_68, v3 = (unsigned long)(unsigned long long)((unsigned int)v3 + 1), p));
        }
        do
        {
            do
            {
                do
                {
LABEL_102cc28:
                    sub_f7db74(p);
                } while ((p = (struct_5 *)ptr->field_68, !p));
                sub_14a3114(p, v3 & 4294967295, addr, g_1ef9080);
                if (!((char)(v3 >> 31) & 1))
                    goto LABEL_102cce4;
            } while ((p = (struct_5 *)ptr->field_68, !p));
        } while ((v3 = (unsigned long)(unsigned long long)p->field_18, v5 = (unsigned long)p->field_10, p->field_1c = p->field_1c + 1, !v5));
        if (*((int *)(v5 + 24)) > (unsigned int)v3)
        {
            p->field_18 = (unsigned int)v3 + 1;
            ptr3 = v5 + (v3 * 0x100000000 >> 63 & 0xffffffff00000000 | v3 & 4294967295) * 8;
            ptr3->field_20 = addr;
            v7 = sub_f7d8d0((struct struct_2 *)&ptr3->field_20, addr);
            if (((char)(v3 >> 31) & 1))
                return v7;
        }
        else
        {
            v8 = sub_14a3390();
            if (((char)(v3 >> 31) & 1))
                return v8;
        }
    }
LABEL_102cce4:
    addr->field_34 = v3;
    addr->field_20 = 1;
    GamepadManager_Gamepad__Reset(addr);
    GamepadManager__CountActiveGamepads(ptr);
    GamepadManager__IsMain(ptr); /* do not return */
}
```

## `GamepadManager.CountActiveGamepads` — RVA `0xc2cd64`

- Decompiled symbol: `GamepadManager_CountActiveGamepads`
- Metadata signature: `private void CountActiveGamepads() { }`
- Native interval: `148` bytes
- Result: `pseudocode`
- Heuristic layout hint: `GamepadManager_Recovered` matched 2 offsets against `GamepadManager` metadata (confidence 1.00).

```c
typedef struct struct_2 {
    char padding_0[24];
    unsigned int field_18;
} struct_2;

typedef struct GamepadManager_Recovered {
    char padding_0[104];
    struct struct_0 *activeGamepads;
    char padding_70[24];
    unsigned int activeGamepadNum;
} GamepadManager_Recovered;

typedef struct struct_0 {
    char padding_0[24];
    int field_18;
} struct_0;

extern long long g_1ef9070;
extern long long g_1ef9078;
extern char g_1fab10d;

struct_2 * GamepadManager_CountActiveGamepads(struct_1 *ptr)
{
    struct_0 *i;  // x0
    int v1;  // w20
    unsigned long v2;  // x0

    if (!(g_1fab10d & 1))
    {
        sub_f7d92c(&g_1ef9070);
        sub_f7d92c(&g_1ef9078);
        g_1fab10d = 1;
    }
    i = ptr->field_68;
    ptr->field_88 = 0;
    if (i)
    {
        v1 = 0;
        do
        {
            if (i->field_18 <= v1)
                return i;
            if (sub_14a30c0())
                ptr->field_88 = ptr->field_88 + 1;
            i = ptr->field_68;
            v1 += 1;
        } while (i);
    }
    v2 = sub_f7db74(i);
    return sub_f7db74(i);
}
```

## `GamepadManager.DisactivateGamepad` — RVA `0xc2cdf8`

- Decompiled symbol: `GamepadManager_DisactivateGamepad`
- Metadata signature: `private void DisactivateGamepad(GamepadManager.Gamepad g, GamepadManager.DisconnectionReason reason) { }`
- Native interval: `268` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[32];
    char field_20;
} struct_0;

extern long long g_1eefb00;
extern long long g_1ef9060;
extern long long g_1ef9080;
extern char g_1fab10c;

unsigned long long GamepadManager_DisactivateGamepad(unsigned long long a0, struct_0 *a1, unsigned long a2)
{
    unsigned long long v0;  // x0
    unsigned long long v1;  // x0
    unsigned long long v2;  // x0

    v0 = a0;
    if (!(g_1fab10c & 1))
    {
        sub_f7d92c(&g_1eefb00);
        sub_f7d92c(&g_1ef9060);
        v1 = sub_f7d92c(&g_1ef9080);
        g_1fab10c = 1;
        v0 = v1;
    }
    v2 = v0;
    if (!a1)
    {
        return v2;
    }
    else if (a1->field_20)
    {
        GamepadManager__IsMain(a0); /* do not return */
    }
    else
    {
        return v2;
    }
}
```

## `GamepadManager.GetProfileForDevice` — RVA `0xc2d0a4`

- Decompiled symbol: `GamepadManager_GetProfileForDevice`
- Metadata signature: `private GamepadProfile GetProfileForDevice(string joyDevice) { }`
- Native interval: `88` bytes
- Result: `pseudocode`

```c
typedef struct struct_3 {
    char padding_0[376];
    unsigned long long field_178;
} struct_3;

typedef struct struct_1 {
    char padding_0[40];
    struct struct_2 *field_28;
} struct_1;

typedef struct struct_0 {
    char padding_0[376];
    unsigned long long field_178;
} struct_0;

typedef struct struct_4 {
    char padding_0[392];
    struct struct_5 *field_188;
    unsigned long long field_190;
} struct_4;

typedef struct struct_2 {
    struct struct_0 *field_0;
} struct_2;

typedef struct struct_5 {
    unsigned long long field_0;
} struct_5;

struct_3 ** GamepadManager_GetProfileForDevice(struct_1 *ptr, long long a1)
{
    struct_0 **v0;  // x0
    struct_4 **v1;  // x0
    long long v2;  // x1
    unsigned long long v3;  // x2
    struct_3 **v4;  // x0

    v0 = ptr->field_28;
    if (v0)
    {
        v0 = CustomGamepadProfileBank__GetProfile(v0, a1);
        if (v0)
            return v0;
    }
    v1 = BuiltInGamepadProfileBank__Inst(v0);
    if (v1)
    {
        v2 = a1;
        v3 = *(v1)->field_190;
        *(v1)->field_188();
    }
    v4 = BuiltInGamepadProfileBank__Inst();
    if (!v4)
        return v4;
    goto *(v4)->field_178;
}
```

## `GamepadManager.GetGamepadSlotCount` — RVA `0xc2d264`

- Decompiled symbol: `GamepadManager_GetGamepadSlotCount`
- Metadata signature: `public int GetGamepadSlotCount() { }`
- Native interval: `72` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[104];
    struct struct_0 *field_68;
} struct_1;

typedef struct struct_0 {
    char padding_0[24];
    unsigned int field_18;
} struct_0;

extern long long g_1ef9070;
extern char g_1fab111;

int GamepadManager_GetGamepadSlotCount(struct_1 *a0)
{
    if (!(g_1fab111 & 1))
    {
        sub_f7d92c(&g_1ef9070);
        g_1fab111 = 1;
    }
    if (a0->field_68)
        return a0->field_68->field_18;
    sub_f7db74();
}
```

## `GamepadManager.GetActiveGamepadCount` — RVA `0xc2d2ac`

- Decompiled symbol: `GamepadManager_GetActiveGamepadCount`
- Metadata signature: `public int GetActiveGamepadCount() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[136];
    unsigned int field_88;
} struct_0;

int GamepadManager_GetActiveGamepadCount(struct_0 *a0)
{
    return a0->field_88;
}
```

## `GamepadManager.GetGamepadAtSlot` — RVA `0xc2d2b4`

- Decompiled symbol: `GamepadManager_GetGamepadAtSlot`
- Metadata signature: `public GamepadManager.Gamepad GetGamepadAtSlot(int slot) { }`
- Native interval: `132` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[104];
    unsigned long long field_68;
} struct_0;

extern long long g_1ef9070;
extern long long g_1ef9078;
extern char g_1fab112;

unsigned int GamepadManager_GetGamepadAtSlot(struct_0 *a0, unsigned int a1)
{
    unsigned long v0;  // x19

    v0 = a1;
    if (!(g_1fab112 & 1))
    {
        sub_f7d92c(&g_1ef9070);
        sub_f7d92c(&g_1ef9078);
        g_1fab112 = 1;
    }
    if (((char)(v0 >> 31) & 1))
        return 0;
    if (a0->field_68)
    {
        if (*((int *)(a0->field_68 + 24)) > (unsigned int)v0)
            return sub_14a30c0();
        return 0;
    }
    sub_f7db74(0);
}
```

## `GamepadManager.GetCombinedGamepad` — RVA `0xc2d338`

- Decompiled symbol: `GamepadManager_GetCombinedGamepad`
- Metadata signature: `public GamepadManager.Gamepad GetCombinedGamepad() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[128];
    unsigned long long field_80;
} struct_0;

long long GamepadManager_GetCombinedGamepad(struct_0 *a0)
{
    return a0->field_80;
}
```

## `GamepadManager.GetConnectedGamepadCount` — RVA `0xc2d340`

- Decompiled symbol: `GamepadManager_GetConnectedGamepadCount`
- Metadata signature: `public int GetConnectedGamepadCount() { }`
- Native interval: `72` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[120];
    struct struct_0 *field_78;
} struct_1;

typedef struct struct_0 {
    char padding_0[24];
    unsigned int field_18;
} struct_0;

extern long long g_1ef9070;
extern char g_1fab113;

int GamepadManager_GetConnectedGamepadCount(struct_1 *a0, unsigned long a1)
{
    if (!(g_1fab113 & 1))
    {
        sub_f7d92c(&g_1ef9070);
        g_1fab113 = 1;
    }
    if (a0->field_78)
        return a0->field_78->field_18;
    sub_f7db74();
}
```

## `GamepadManager.GetConnectedGamepad` — RVA `0xc2d388`

- Decompiled symbol: `GamepadManager_GetConnectedGamepad`
- Metadata signature: `public GamepadManager.Gamepad GetConnectedGamepad(int index) { }`
- Native interval: `132` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[120];
    unsigned long long field_78;
} struct_0;

extern long long g_1ef9070;
extern long long g_1ef9078;
extern char g_1fab114;

unsigned int GamepadManager_GetConnectedGamepad(struct_0 *a0, unsigned int a1)
{
    unsigned long v0;  // x19

    v0 = a1;
    if (!(g_1fab114 & 1))
    {
        sub_f7d92c(&g_1ef9070);
        sub_f7d92c(&g_1ef9078);
        g_1fab114 = 1;
    }
    if (((char)(v0 >> 31) & 1))
        return 0;
    if (a0->field_78)
    {
        if (*((int *)(a0->field_78 + 24)) > (unsigned int)v0)
            return sub_14a30c0();
        return 0;
    }
    sub_f7db74(0);
}
```

## `GamepadManager.DisactivateGamepads` — RVA `0xc2d40c`

- Decompiled symbol: `GamepadManager_DisactivateGamepads`
- Metadata signature: `public void DisactivateGamepads() { }`
- Native interval: `220` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[104];
    struct struct_0 *field_68;
} struct_1;

typedef struct struct_0 {
    char padding_0[24];
    int field_18;
} struct_0;

extern long long g_1eefb00;
extern long long g_1ef9070;
extern long long g_1ef9078;
extern char g_1fab115;

void GamepadManager_DisactivateGamepads(struct_1 *ptr)
{
    unsigned long long v4;  // x30
    unsigned long long v5;  // x21
    unsigned long long v6;  // x20
    unsigned long long v7;  // x19
    struct_0 *i;  // x0
    int v9;  // w20
    struct_0 *v10;  // x0
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x18]
    unsigned long long v2;  // [bp-0x10]
    unsigned long long v3;  // [bp-0x8]

    v0 = v4;
    v1 = v5;
    v2 = v6;
    v3 = v7;
    if (!(g_1fab115 & 1))
    {
        sub_f7d92c(&g_1eefb00);
        sub_f7d92c(&g_1ef9070);
        sub_f7d92c(&g_1ef9078);
        g_1fab115 = 1;
    }
    i = ptr->field_68;
    if (i)
    {
        v9 = 0;
        do
        {
            if (i->field_18 <= v9)
                GamepadManager__IsMain(ptr); /* do not return */
            v10 = sub_14a30c0();
            if (v10)
                GamepadManager__DisactivateGamepad(ptr, v10, 0);
            i = ptr->field_68;
            v9 += 1;
        } while (i);
    }
    sub_f7db74(i);
    GamepadManager__IsMain(ptr); /* do not return */
}
```
