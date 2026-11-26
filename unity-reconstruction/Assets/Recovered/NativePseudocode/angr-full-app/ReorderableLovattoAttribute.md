# Native pseudocode: ReorderableLovattoAttribute

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `ReorderableLovattoAttribute.ctor` — RVA `0xce80b8`

- Decompiled symbol: `ReorderableLovattoAttribute_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `28` bytes
- Result: `pseudocode`

```c
void ReorderableLovattoAttribute_ctor(unsigned long a0)
{
    ReorderableLovattoAttribute__ctor(); /* do not return */
}
```

## `ReorderableLovattoAttribute.ctor` — RVA `0xce80d4`

- Decompiled symbol: `ReorderableLovattoAttribute_ctor`
- Metadata signature: `public void .ctor(string elementNameProperty) { }`
- Native interval: `28` bytes
- Result: `pseudocode`

```c
void ReorderableLovattoAttribute_ctor(unsigned long a0, unsigned long a1)
{
    ReorderableLovattoAttribute__ctor(); /* do not return */
}
```

## `ReorderableLovattoAttribute.ctor` — RVA `0xce80f0`

- Decompiled symbol: `ReorderableLovattoAttribute_ctor`
- Metadata signature: `public void .ctor(bool add, bool remove, bool draggable, string elementNameProperty, string elementNameOverride, string elementIconPath) { }`
- Native interval: `128` bytes
- Result: `pseudocode`
- Heuristic layout hint: `ReorderableLovattoAttribute_Recovered` matched 6 offsets against `ReorderableLovattoAttribute` metadata (confidence 1.00).

```c
typedef struct ReorderableLovattoAttribute_Recovered {
    char padding_0[20];
    char add;
    char remove;
    char draggable;
    char padding_17[9];
    long long elementNameProperty;
    long long elementNameOverride;
    unsigned long long elementIconPath;
} ReorderableLovattoAttribute_Recovered;

void ReorderableLovattoAttribute_ctor(struct_0 *ptr, char a1, char a2, char a3, long long a4, long long a5, unsigned long a6)
{
    unsigned long long v8;  // x30
    unsigned long long v9;  // x25
    unsigned long long v10;  // x24
    unsigned long long v11;  // x23
    unsigned long long v12;  // x22
    unsigned long long v13;  // x21
    unsigned long long v14;  // x20
    unsigned long long v15;  // x19
    struct_0 *p;  // x0
    struct_0 *addr;  // x0
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
    PropertyAttribute__ctor();
    p = ptr;
    ptr->field_14 = a1 & 1;
    ptr->field_15 = a2 & 1;
    ptr->field_16 = a3 & 1;
    p->field_20 = a4;
    sub_f7d8d0((struct ReorderableLovattoAttribute_Recovered *)&p->field_20, a4);
    addr = ptr;
    addr->field_28 = a5;
    sub_f7d8d0((struct ReorderableLovattoAttribute_Recovered *)&addr->field_28, a5);
    ptr->field_30 = a6;
    sub_f7d8d0();
    return;
}
```

## `ReorderableLovattoAttribute.ctor` — RVA `0xce8170`

- Decompiled symbol: `ReorderableLovattoAttribute_ctor`
- Metadata signature: `public void .ctor(string elementNameProperty, string elementIconPath) { }`
- Native interval: `28` bytes
- Result: `pseudocode`
- Heuristic layout hint: `ReorderableLovattoAttribute_Recovered` matched 6 offsets against `ReorderableLovattoAttribute` metadata (confidence 1.00).

```c
typedef struct ReorderableLovattoAttribute_Recovered {
    char padding_0[20];
    char add;
    char remove;
    char draggable;
    char padding_17[9];
    long long elementNameProperty;
    long long elementNameOverride;
    unsigned long long elementIconPath;
} ReorderableLovattoAttribute_Recovered;

void ReorderableLovattoAttribute_ctor(struct_0 *a0, long long a1, unsigned int a2)
{
    ReorderableLovattoAttribute__ctor(a0, 1, 1, 1, a1, 0, a2); /* do not return */
}
```

## `ReorderableLovattoAttribute.ctor` — RVA `0xce818c`

- Decompiled symbol: `ReorderableLovattoAttribute_ctor`
- Metadata signature: `public void .ctor(string elementNameProperty, string elementNameOverride, string elementIconPath) { }`
- Native interval: `28` bytes
- Result: `pseudocode`
- Heuristic layout hint: `ReorderableLovattoAttribute_Recovered` matched 6 offsets against `ReorderableLovattoAttribute` metadata (confidence 1.00).

```c
typedef struct ReorderableLovattoAttribute_Recovered {
    char padding_0[20];
    char add;
    char remove;
    char draggable;
    char padding_17[9];
    long long elementNameProperty;
    long long elementNameOverride;
    unsigned long long elementIconPath;
} ReorderableLovattoAttribute_Recovered;

void ReorderableLovattoAttribute_ctor(struct_0 *a0, long long a1, long long a2, unsigned int a3)
{
    ReorderableLovattoAttribute__ctor(a0, 1, 1, 1, a1, a2, a3); /* do not return */
}
```

## `ReorderableLovattoAttribute.ctor` — RVA `0xce81a8`

- Decompiled symbol: `ReorderableLovattoAttribute_ctor`
- Metadata signature: `public void .ctor(bool add, bool remove, bool draggable, string elementNameProperty, string elementIconPath) { }`
- Native interval: `24` bytes
- Result: `pseudocode`
- Heuristic layout hint: `ReorderableLovattoAttribute_Recovered` matched 6 offsets against `ReorderableLovattoAttribute` metadata (confidence 1.00).

```c
typedef struct ReorderableLovattoAttribute_Recovered {
    char padding_0[20];
    char add;
    char remove;
    char draggable;
    char padding_17[9];
    long long elementNameProperty;
    long long elementNameOverride;
    unsigned long long elementIconPath;
} ReorderableLovattoAttribute_Recovered;

void ReorderableLovattoAttribute_ctor(struct_0 *a0, char a1, char a2, char a3, long long a4, unsigned int a5)
{
    ReorderableLovattoAttribute__ctor(a0, a1 & 1, a2 & 1, a3 & 1, a4, 0, a5); /* do not return */
}
```
