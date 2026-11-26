# Native pseudocode: AutoContentFitter

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `AutoContentFitter.Update` — RVA `0xc5a344`

- Decompiled symbol: `AutoContentFitter_Update`
- Metadata signature: `private void Update() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long AutoContentFitter_Update(unsigned long a0)
{
    unsigned long long v0;  // x0

    v0 = AutoContentFitter__UpdatePreferredDimensions();
    return AutoContentFitter__UpdatePreferredDimensions();
}
```

## `AutoContentFitter.UpdatePreferredDimensions` — RVA `0xc5a348`

- Decompiled symbol: `AutoContentFitter_UpdatePreferredDimensions`
- Metadata signature: `public void UpdatePreferredDimensions() { }`
- Native interval: `300` bytes
- Result: `pseudocode`
- Heuristic layout hint: `AutoContentFitter_Recovered` matched 3 offsets against `AutoContentFitter` metadata (confidence 1.00).

```c
typedef struct AutoContentFitter_Recovered {
    char padding_0[32];
    unsigned long long source;
    char autoWidth;
    char autoHeight;
} AutoContentFitter_Recovered;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern unsigned long long g_1ef1170;
extern char g_1fab29d;

struct_1 * AutoContentFitter_UpdatePreferredDimensions(struct_1 *ptr)
{
    struct_1 *v0;  // x0
    struct_1 *v1;  // x0
    struct_1 *v2;  // x0
    struct_1 *v3;  // x0
    struct_1 *v4;  // x0
    struct_1 *v5;  // x20
    unsigned long v6;  // x0
    unsigned long long v7;  // x0

    v0 = ptr;
    if (!(g_1fab29d & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        v1 = sub_f7d92c(&g_1ef1170);
        g_1fab29d = 1;
        v0 = v1;
    }
    v2 = v0;
    if (!ptr->field_28 && !ptr->field_29)
        return v2;
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v3 = Object__op_Equality(ptr->field_20, 0, 0);
    if (((char)v3 & 1))
        return v3;
    v4 = Component__get_transform(ptr, 0);
    v5 = v4;
    if (!v4 || *((long long *)&v5->padding_0[0]) == g_1ef1170)
    {
        if (ptr->field_29)
        {
            v6 = ptr->field_20;
            if (!v6 || (v6 = (unsigned long)(unsigned long long)RectTransform__get_rect(v6, 0), !v5))
                goto LABEL_105a468;
            v4 = RectTransform__SetSizeWithCurrentAnchors(v5, 1, 0);
        }
        if (!ptr->field_28)
            return v4;
        v6 = ptr->field_20;
        if (v6)
        {
            v6 = RectTransform__get_rect(v6, 0);
            if (v5)
            {
                v7 = RectTransform__SetSizeWithCurrentAnchors();
                return RectTransform__SetSizeWithCurrentAnchors();
            }
        }
LABEL_105a468:
        sub_f7db74(v6);
    }
    sub_f7df10(v5);
}
```

## `AutoContentFitter.ctor` — RVA `0xc5a474`

- Decompiled symbol: `AutoContentFitter_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `16` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[44];
    unsigned long long field_2c;
} struct_0;

long long AutoContentFitter_ctor(struct_0 *ptr)
{
    long long v0;  // x0

    *((unsigned long long *)&(&ptr->padding_0)[1]) = 0x4120000041200000;
    v0 = MonoBehaviour__ctor();
    return MonoBehaviour__ctor();
}
```
