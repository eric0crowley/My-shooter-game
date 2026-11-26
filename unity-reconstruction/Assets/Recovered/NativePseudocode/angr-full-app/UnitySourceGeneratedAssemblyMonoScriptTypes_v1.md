# Native pseudocode: UnitySourceGeneratedAssemblyMonoScriptTypes_v1

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `UnitySourceGeneratedAssemblyMonoScriptTypes_v1.Get` — RVA `0xc2a150`

- Decompiled symbol: `UnitySourceGeneratedAssemblyMonoScriptTypes_v1_Get`
- Metadata signature: `private static UnitySourceGeneratedAssemblyMonoScriptTypes_v1.MonoScriptData Get() { }`
- Native interval: `248` bytes
- Result: `pseudocode`

```c
extern long long g_1f05658;
extern char g_1fab0f0;

unsigned long long __start_il2cpp(void)
{
    long long v4;  // x21
    long long v5;  // x21
    unsigned long long v6;  // x0
    uint128_t ptr[2];  // x8
    int v0;  // [bp-0x50]
    unsigned long long flag;  // [bp-0x48]
    int v2;  // [bp-0x40], Other Possible Types: unsigned long long
    unsigned long long choice;  // [bp-0x38]

    if (!(g_1fab0f0 & 1))
    {
        sub_f7d92c("e'");
        sub_f7d92c("\t");
        sub_f7d92c(&g_1f05658);
        g_1fab0f0 = 1;
    }
    flag = 0;
    v2 = 0;
    choice = 0;
    v4 = sub_f7d9d4(g_1eedff8, 7986);
    RuntimeHelpers__InitializeArray(v4, g_1f05650, 0);
    *((long long *)&v0) = v4;
    sub_f7d8d0(&v0, v4);
    v5 = sub_f7d9d4(g_1eedff8, 6041);
    RuntimeHelpers__InitializeArray(v5, g_1f05658, 0);
    *((long long *)&(&v0)[8]) = v5;
    v6 = sub_f7d8d0(&v0 - 8, v5);
    v2 = (int)_INSERT(v2 CONCAT 0, 8, 0);
    *((unsigned long long *)&v2) = 399431958665;
    *((void*)&ptr[0]) = v0;
    *((void*)&ptr[1]) = v2;
    return v6;
}
```

## `UnitySourceGeneratedAssemblyMonoScriptTypes_v1.ctor` — RVA `0xc2a248`

- Decompiled symbol: `UnitySourceGeneratedAssemblyMonoScriptTypes_v1_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long UnitySourceGeneratedAssemblyMonoScriptTypes_v1_ctor(void)
{
    unsigned long long v0;  // x0

    v0 = Object__ctor();
    return Object__ctor();
}
```

## `UnitySourceGeneratedAssemblyMonoScriptTypes_v1.Get` — RVA `0xccc4bc`

- Decompiled symbol: `UnitySourceGeneratedAssemblyMonoScriptTypes_v1_Get`
- Metadata signature: `private static UnitySourceGeneratedAssemblyMonoScriptTypes_v1.MonoScriptData Get() { }`
- Native interval: `248` bytes
- Result: `pseudocode`

```c
extern long long g_1f05638;
extern long long g_1f05640;
extern char g_1fab58e;

long long UnitySourceGeneratedAssemblyMonoScriptTypes_v1_Get(void)
{
    long long v4;  // x21
    long long v5;  // x21
    unsigned long v6;  // x0
    uint128_t ptr[2];  // x8
    int v0;  // [bp-0x50]
    unsigned long long flag;  // [bp-0x48]
    int v2;  // [bp-0x40], Other Possible Types: unsigned long long
    unsigned long long choice;  // [bp-0x38]

    if (!(g_1fab58e & 1))
    {
        sub_f7d92c("e'");
        sub_f7d92c(&g_1f05638);
        sub_f7d92c(&g_1f05640);
        g_1fab58e = 1;
    }
    flag = 0;
    v2 = 0;
    choice = 0;
    v4 = sub_f7d9d4(g_1eedff8, 14482);
    RuntimeHelpers__InitializeArray(v4, g_1f05638, 0);
    *((long long *)&v0) = v4;
    sub_f7d8d0(&v0, v4);
    v5 = sub_f7d9d4(g_1eedff8, 10063);
    RuntimeHelpers__InitializeArray(v5, g_1f05640, 0);
    *((long long *)&(&v0)[8]) = v5;
    v6 = sub_f7d8d0(&v0 - 8, v5);
    v2 = (int)_INSERT(v2 CONCAT 0, 8, 0);
    *((unsigned long long *)&v2) = 962072674588;
    *((void*)&ptr[0]) = v0;
    *((void*)&ptr[1]) = v2;
    return v6;
}
```

## `UnitySourceGeneratedAssemblyMonoScriptTypes_v1.ctor` — RVA `0xccc5b4`

- Decompiled symbol: `UnitySourceGeneratedAssemblyMonoScriptTypes_v1_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long UnitySourceGeneratedAssemblyMonoScriptTypes_v1_ctor(void)
{
    long long v0;  // x0

    v0 = Object__ctor();
    return Object__ctor();
}
```
