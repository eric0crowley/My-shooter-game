# Native pseudocode: ShowBigBanner

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `ShowBigBanner.OnEnable` — RVA `0xc75db0`

- Decompiled symbol: `ShowBigBanner_OnEnable`
- Metadata signature: `private void OnEnable() { }`
- Native interval: `96` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    char padding_0[32];
    unsigned int field_20;
} struct_2;

typedef struct struct_1 {
    long long *field_0;
} struct_1;

typedef struct struct_0 {
    char padding_0[184];
    struct struct_1 *field_b8;
} struct_0;

extern struct_0 *g_1eee700;
extern char g_1fab3a2;

void ShowBigBanner_OnEnable(struct_2 *ptr)
{
    if (!(g_1fab3a2 & 1))
    {
        sub_f7d92c(&g_1eee700);
        g_1fab3a2 = 1;
    }
    ptr->field_20 = ptr->field_20 + 1;
    if (g_1eee700->field_b8->field_0)
        AdsManager__Request_Big_Banner(g_1eee700->field_b8->field_0); /* do not return */
    sub_f7db74(0);
}
```

## `ShowBigBanner.OnDisable` — RVA `0xc75e10`

- Decompiled symbol: `ShowBigBanner_OnDisable`
- Metadata signature: `private void OnDisable() { }`
- Native interval: `100` bytes
- Result: `pseudocode`

```c
typedef struct struct_3 {
    char padding_0[32];
    unsigned int field_20;
} struct_3;

typedef struct struct_0 {
    char padding_0[88];
    unsigned long long field_58;
} struct_0;

typedef struct struct_2 {
    struct struct_0 *field_0;
} struct_2;

typedef struct struct_1 {
    char padding_0[184];
    struct struct_2 *field_b8;
} struct_1;

extern struct_1 *g_1eee700;
extern char g_1fab3a3;

void ShowBigBanner_OnDisable(struct_3 *ptr)
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
    if (!(g_1fab3a3 & 1))
    {
        sub_f7d92c(&g_1eee700);
        g_1fab3a3 = 1;
    }
    ptr->field_20 = 0;
    sub_f7db74();
}
```

## `ShowBigBanner.ctor` — RVA `0xc75e74`

- Decompiled symbol: `ShowBigBanner_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long ShowBigBanner_ctor(void)
{
    long long v0;  // x0

    v0 = MonoBehaviour__ctor();
    return MonoBehaviour__ctor();
}
```
