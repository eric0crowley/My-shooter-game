# Native pseudocode: SplashLoading

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `SplashLoading.Start` — RVA `0xcc462c`

- Decompiled symbol: `SplashLoading_Start`
- Metadata signature: `private void Start() { }`
- Native interval: `32` bytes
- Result: `pseudocode`

```c
void SplashLoading_Start(unsigned long a0)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    SplashLoading__LoadMenu();
    MonoBehaviour__StartCoroutine();
    return;
}
```

## `SplashLoading.LoadMenu` — RVA `0xcc464c`

- Decompiled symbol: `SplashLoading_LoadMenu`
- Metadata signature: `private IEnumerator LoadMenu() { }`
- Native interval: `88` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

extern long long g_1ef3a48;
extern char g_1fab533;

struct_0 * SplashLoading_LoadMenu(void)
{
    struct_0 *ptr;  // x0

    if (!(g_1fab533 & 1))
    {
        sub_f7d92c(&g_1ef3a48);
        g_1fab533 = 1;
    }
    ptr = sub_f7db70(g_1ef3a48);
    Object__ctor(ptr, 0);
    ptr->field_10 = 0;
    return ptr;
}
```

## `SplashLoading.<LoadMenu>d__1.ctor` — RVA `0xcc46a4`

- Decompiled symbol: `SplashLoading_LoadMenu_d__1_ctor`
- Metadata signature: `public void .ctor(int <>1__state) { }`
- Native interval: `40` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

void SplashLoading_LoadMenu_d__1_ctor(struct_0 *ptr, unsigned int a1)
{
    Object__ctor();
    ptr->field_10 = a1;
    return;
}
```

## `SplashLoading.ctor` — RVA `0xcc46cc`

- Decompiled symbol: `SplashLoading_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long SplashLoading_ctor(void)
{
    long long v0;  // x0

    v0 = MonoBehaviour__ctor();
    return MonoBehaviour__ctor();
}
```

## `SplashLoading.<LoadMenu>d__1.Dispose` — RVA `0xcc46d4`

- Decompiled symbol: `SplashLoading_LoadMenu_d__1_Dispose`
- Metadata signature: `private void System.IDisposable.Dispose() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long SplashLoading_LoadMenu_d__1_Dispose(void)
{
    unsigned long v0;  // x0

    return v0;
}
```

## `SplashLoading.<LoadMenu>d__1.MoveNext` — RVA `0xcc46d8`

- Decompiled symbol: `SplashLoading_LoadMenu_d__1_MoveNext`
- Metadata signature: `private bool MoveNext() { }`
- Native interval: `200` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[4];
    long long field_18;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1eee870;
extern long long g_1ef2440;
extern char g_1fab534;

unsigned int SplashLoading_LoadMenu_d__1_MoveNext(struct_1 *ptr)
{
    long long v0;  // x20

    if (!(g_1fab534 & 1))
    {
        sub_f7d92c(&g_1eee870);
        sub_f7d92c(&g_1ef2440);
        g_1fab534 = 1;
    }
    if (ptr->field_10 == 1)
    {
        ptr->field_10 = 4294967295;
        if (!g_1eee870->field_e0)
            sub_f7da5c(g_1eee870);
        Application__LoadLevel(1, 0);
    }
    else if (!ptr->field_10)
    {
        ptr->field_10 = 4294967295;
        v0 = sub_f7db70(g_1ef2440);
        WaitForSeconds__ctor(v0, 0);
        ptr->field_18 = v0;
        sub_f7d8d0((struct struct_1 *)&ptr->field_18, v0);
        ptr->field_10 = 1;
        return 1;
    }
    return 0;
}
```

## `SplashLoading.<LoadMenu>d__1.get_Current` — RVA `0xcc47a0`

- Decompiled symbol: `SplashLoading_LoadMenu_d__1_get_Current`
- Metadata signature: `private object System.Collections.Generic.IEnumerator<System.Object>.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long SplashLoading_LoadMenu_d__1_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```

## `SplashLoading.<LoadMenu>d__1.Reset` — RVA `0xcc47a8`

- Decompiled symbol: `SplashLoading_LoadMenu_d__1_Reset`
- Metadata signature: `private void System.Collections.IEnumerator.Reset() { }`
- Native interval: `56` bytes
- Result: `pseudocode`

```c
extern long long g_1ef0bd8;
extern long long g_1f04e88;

void SplashLoading_LoadMenu_d__1_Reset(void)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    long long v4;  // x0
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    v4 = sub_f7db70(sub_f7d940(&g_1ef0bd8));
    NotSupportedException__ctor(v4, 0);
    sub_f7da4c(v4, sub_f7d940(&g_1f04e88));
}
```

## `SplashLoading.<LoadMenu>d__1.get_Current` — RVA `0xcc47e0`

- Decompiled symbol: `SplashLoading_LoadMenu_d__1_get_Current`
- Metadata signature: `private object System.Collections.IEnumerator.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long SplashLoading_LoadMenu_d__1_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```
