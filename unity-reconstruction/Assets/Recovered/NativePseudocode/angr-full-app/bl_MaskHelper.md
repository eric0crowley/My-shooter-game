# Native pseudocode: bl_MaskHelper

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `bl_MaskHelper.SetMaskedIcon` — RVA `0xcc5ffc`

- Decompiled symbol: `bl_MaskHelper_SetMaskedIcon`
- Metadata signature: `public void SetMaskedIcon(RectTransform trans) { }`
- Native interval: `36` bytes
- Result: `pseudocode`

```c
void bl_MaskHelper_SetMaskedIcon(unsigned long a0, unsigned long long a1)
{
    unsigned long long v1;  // x30
    unsigned long long v0;  // [bp-0x10]

    v0 = v1;
    if (a1)
    {
        Transform__SetParent();
        return;
    }
    sub_f7db74();
}
```

## `bl_MaskHelper.OnChange` — RVA `0xcc7f28`

- Decompiled symbol: `bl_MaskHelper_OnChange`
- Metadata signature: `public void OnChange(bool full = false) { }`
- Native interval: `248` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[48];
    long long field_30;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab573;

long long bl_MaskHelper_OnChange(struct_1 *a0, unsigned int a1)
{
    unsigned long long v0;  // x0
    long long v1;  // x0
    long long v2;  // x0
    unsigned long long v3;  // x0

    if (!(g_1fab573 & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab573 = 1;
    }
    v0 = bl_MaskHelper__get_m_image(a0);
    if (((char)a1 & 1))
    {
        if (v0)
        {
            Image__set_sprite();
            if (!g_1ef0c58->field_e0)
                sub_f7da5c(g_1ef0c58);
            v1 = Object__op_Inequality(a0->field_30, 0, 0);
            if (!((char)v1 & 1))
            {
                return v1;
            }
            else if (a0->field_30)
            {
                v3 = Image__set_sprite();
                return Image__set_sprite();
            }
        }
    }
    else
    {
        if (v0)
        {
            Image__set_sprite();
            if (!g_1ef0c58->field_e0)
                sub_f7da5c(g_1ef0c58);
            v2 = Object__op_Inequality(a0->field_30, 0, 0);
            if (!((char)v2 & 1))
            {
                return v2;
            }
            else if (a0->field_30)
            {
                v3 = Image__set_sprite();
                return Image__set_sprite();
            }
        }
    }
    sub_f7db74();
}
```

## `bl_MaskHelper.Start` — RVA `0xcca3cc`

- Decompiled symbol: `bl_MaskHelper_Start`
- Metadata signature: `private void Start() { }`
- Native interval: `36` bytes
- Result: `pseudocode`

```c
void bl_MaskHelper_Start(unsigned long a0)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    if (bl_MaskHelper__get_m_image())
    {
        Image__set_sprite();
        return;
    }
    sub_f7db74();
}
```

## `bl_MaskHelper.get_m_image` — RVA `0xcca3f0`

- Decompiled symbol: `bl_MaskHelper_get_m_image`
- Metadata signature: `private Image get_m_image() { }`
- Native interval: `168` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[80];
    long long field_50;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern long long g_1efcfd0;
extern char g_1fab572;

long long bl_MaskHelper_get_m_image(struct_1 *ptr)
{
    long long v0;  // x0

    if (!(g_1fab572 & 1))
    {
        sub_f7d92c(&g_1efcfd0);
        sub_f7d92c(&g_1ef0c58);
        g_1fab572 = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (((char)Object__op_Equality(ptr->field_50, 0, 0) & 1))
    {
        v0 = sub_1231bc8(ptr, g_1efcfd0);
        ptr->field_50 = v0;
        sub_f7d8d0((struct struct_1 *)&ptr->field_50, v0);
    }
    return ptr->field_50;
}
```

## `bl_MaskHelper.ctor` — RVA `0xcca498`

- Decompiled symbol: `bl_MaskHelper_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long bl_MaskHelper_ctor(void)
{
    long long v0;  // x0

    v0 = MonoBehaviour__ctor();
    return MonoBehaviour__ctor();
}
```
