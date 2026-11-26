# Native pseudocode: InspectorButtonAttribute

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `InspectorButtonAttribute.get_ButtonWidth` — RVA `0xcca8a8`

- Decompiled symbol: `InspectorButtonAttribute_get_ButtonWidth`
- Metadata signature: `public float get_ButtonWidth() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long InspectorButtonAttribute_get_ButtonWidth(unsigned long a0)
{
    return a0;
}
```

## `InspectorButtonAttribute.set_ButtonWidth` — RVA `0xcca8b0`

- Decompiled symbol: `InspectorButtonAttribute_set_ButtonWidth`
- Metadata signature: `public void set_ButtonWidth(float value) { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[32];
    unsigned int field_20;
} struct_0;

struct_0 * InspectorButtonAttribute_set_ButtonWidth(struct_0 *ptr)
{
    unsigned int v0;  // s0

    ptr->field_20 = v0;
    return ptr;
}
```

## `InspectorButtonAttribute.ctor` — RVA `0xcca8b8`

- Decompiled symbol: `InspectorButtonAttribute_ctor`
- Metadata signature: `public void .ctor(string MethodName) { }`
- Native interval: `132` bytes
- Result: `pseudocode`
- Heuristic layout hint: `InspectorButtonAttribute_Recovered` matched 2 offsets against `InspectorButtonAttribute` metadata (confidence 1.00).

```c
typedef struct struct_0 {
    char padding_0[184];
    struct struct_1 *field_b8;
    char padding_c0[32];
    unsigned int field_e0;
} struct_0;

typedef struct InspectorButtonAttribute_Recovered {
    char padding_0[24];
    unsigned long long MethodName;
    unsigned int _buttonWidth;
} InspectorButtonAttribute_Recovered;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

extern char g_1fab579;

void InspectorButtonAttribute_ctor(struct_2 *ptr, unsigned long a1)
{
    unsigned long long v5;  // x30
    unsigned long long v6;  // x22
    unsigned long long v7;  // x21
    unsigned long long v8;  // x20
    unsigned long long v9;  // x19
    struct_0 *index;  // x0
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
    if (!(g_1fab579 & 1))
    {
        sub_f7d92c("eB");
        g_1fab579 = 1;
    }
    index = g_1ef0430;
    if (!g_1ef0430->field_e0)
    {
        sub_f7da5c(g_1ef0430);
        index = g_1ef0430;
    }
    ptr->field_20 = index->field_b8->field_0;
    PropertyAttribute__ctor(ptr, 0);
    ptr->field_18 = a1;
    sub_f7d8d0();
    return;
}
```

## `InspectorButtonAttribute.cctor` — RVA `0xcca93c`

- Decompiled symbol: `InspectorButtonAttribute_cctor`
- Metadata signature: `private static void .cctor() { }`
- Native interval: `76` bytes
- Result: `pseudocode`

```c
extern char g_1fab57a;

unsigned long long InspectorButtonAttribute_cctor(void)
{
    unsigned long long v0;  // x0

    if (!(g_1fab57a & 1))
    {
        v0 = sub_f7d92c("eB");
        g_1fab57a = 1;
    }
    g_1ef0430->field_b8->field_0 = 0x43160000;
    return v0;
}
```
