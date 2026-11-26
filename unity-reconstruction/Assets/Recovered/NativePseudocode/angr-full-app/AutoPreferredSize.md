# Native pseudocode: AutoPreferredSize

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `AutoPreferredSize.OnEnable` — RVA `0xc5a484`

- Decompiled symbol: `AutoPreferredSize_OnEnable`
- Metadata signature: `private void OnEnable() { }`
- Native interval: `176` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[32];
    long long field_20;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern long long g_1efcff0;
extern char g_1fab29e;

long long AutoPreferredSize_OnEnable(struct_1 *ptr)
{
    long long v0;  // x0
    long long v1;  // x0

    if (!(g_1fab29e & 1))
    {
        sub_f7d92c(&g_1efcff0);
        sub_f7d92c(&g_1ef0c58);
        g_1fab29e = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v0 = Object__op_Equality(ptr->field_20, 0, 0);
    if (!((char)v0 & 1))
        return v0;
    ptr->field_20 = sub_1231bc8(ptr, g_1efcff0);
    v1 = sub_f7d8d0();
    return sub_f7d8d0();
}
```

## `AutoPreferredSize.Update` — RVA `0xc5a534`

- Decompiled symbol: `AutoPreferredSize_Update`
- Metadata signature: `private void Update() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long AutoPreferredSize_Update(unsigned long a0)
{
    unsigned long long v0;  // x0

    v0 = AutoPreferredSize__UpdatePreferredDimensions();
    return AutoPreferredSize__UpdatePreferredDimensions();
}
```

## `AutoPreferredSize.UpdatePreferredDimensions` — RVA `0xc5a538`

- Decompiled symbol: `AutoPreferredSize_UpdatePreferredDimensions`
- Metadata signature: `public void UpdatePreferredDimensions() { }`
- Native interval: `252` bytes
- Result: `pseudocode`
- Heuristic layout hint: `AutoPreferredSize_Recovered` matched 4 offsets against `AutoPreferredSize` metadata (confidence 1.00).

```c
typedef struct AutoPreferredSize_Recovered {
    char padding_0[32];
    struct struct_4 *target;
    char autoWidth;
    char autoHeight;
    char padding_2a[14];
    unsigned long long source;
} AutoPreferredSize_Recovered;

typedef struct struct_5 {
    char padding_0[824];
    unsigned long long field_338;
    char padding_340[24];
    struct struct_6 *field_358;
    unsigned long long field_360;
} struct_5;

typedef struct struct_4 {
    struct struct_1 *field_0;
} struct_4;

typedef struct struct_6 {
    unsigned long long field_0;
} struct_6;

typedef struct struct_1 {
    char padding_0[824];
    unsigned long long field_338;
    char padding_340[24];
    struct struct_2 *field_358;
    unsigned long long field_360;
} struct_1;

typedef struct struct_2 {
    unsigned long long field_0;
} struct_2;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab29f;

struct_3 * AutoPreferredSize_UpdatePreferredDimensions(struct_3 *ptr)
{
    struct_3 *v0;  // x0
    struct_3 *v1;  // x0
    struct_3 *v2;  // x0
    unsigned long long flag;  // x2
    struct_3 *v4;  // x0
    unsigned long v5;  // x0
    struct_5 **v6;  // x20
    struct_5 **v7;  // x0
    unsigned long v8;  // x1

    v0 = ptr;
    if (!(g_1fab29f & 1))
    {
        v1 = sub_f7d92c(&g_1ef0c58);
        g_1fab29f = 1;
        v0 = v1;
    }
    v2 = v0;
    if (!ptr->field_28 && !ptr->field_29)
        return v2;
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    flag = 0;
    v4 = Object__op_Equality(ptr->field_38, 0, 0);
    if (((char)v4 & 1))
        return v4;
    if (ptr->field_29)
    {
        v5 = ptr->field_38;
        if (v5)
        {
            v6 = ptr->field_20;
            v5 = RectTransform__get_rect(v5, 0);
            if (v6)
            {
                v7 = v6;
                v8 = *(v6)->field_360;
                *(v6)->field_358();
            }
        }
    }
    else if (ptr->field_28)
    {
        v5 = ptr->field_38;
        if (v5)
        {
            v5 = RectTransform__get_rect(v5, 0);
            if (ptr->field_20)
                goto ptr->field_20->field_0->field_338;
        }
    }
    else
    {
        return v4;
    }
    sub_f7db74(v5);
}
```

## `AutoPreferredSize.ctor` — RVA `0xc5a634`

- Decompiled symbol: `AutoPreferredSize_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `16` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[44];
    unsigned long long field_2c;
} struct_0;

long long AutoPreferredSize_ctor(struct_0 *ptr)
{
    long long v0;  // x0

    *((unsigned long long *)&(&ptr->padding_0)[1]) = 0x4120000041200000;
    v0 = MonoBehaviour__ctor();
    return MonoBehaviour__ctor();
}
```
