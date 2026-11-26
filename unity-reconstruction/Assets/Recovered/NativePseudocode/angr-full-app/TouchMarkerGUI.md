# Native pseudocode: TouchMarkerGUI

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `TouchMarkerGUI.ctor` — RVA `0xc55de4`

- Decompiled symbol: `TouchMarkerGUI_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long TouchMarkerGUI_ctor(void)
{
    long long v0;  // x0

    v0 = MonoBehaviour__ctor();
    return MonoBehaviour__ctor();
}
```

## `TouchMarkerGUI.OnEnable` — RVA `0xc55dec`

- Decompiled symbol: `TouchMarkerGUI_OnEnable`
- Metadata signature: `private void OnEnable() { }`
- Native interval: `88` bytes
- Result: `pseudocode`

```c
extern char g_1fab27e;

void TouchMarkerGUI_OnEnable(unsigned long a0)
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
    if (!(g_1fab27e & 1))
    {
        sub_f7d92c("!Y");
        g_1fab27e = 1;
    }
    g_1ef1e30->field_b8->field_0 = a0;
    sub_f7d8d0();
    return;
}
```

## `TouchMarkerGUI.OnDisable` — RVA `0xc55e44`

- Decompiled symbol: `TouchMarkerGUI_OnDisable`
- Metadata signature: `private void OnDisable() { }`
- Native interval: `180` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab27f;

long long TouchMarkerGUI_OnDisable(long long a0)
{
    long long v0;  // x0
    long long v1;  // x0

    if (!(g_1fab27f & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c("!Y");
        g_1fab27f = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v0 = Object__op_Equality(g_1ef1e30->field_b8->field_0, a0, 0);
    if (!((char)v0 & 1))
        return v0;
    g_1ef1e30->field_b8->field_0 = 0;
    v1 = sub_f7d8d0();
    return sub_f7d8d0();
}
```

## `TouchMarkerGUI.OnGUI` — RVA `0xc55ef8`

- Decompiled symbol: `TouchMarkerGUI_OnGUI`
- Metadata signature: `private void OnGUI() { }`
- Native interval: `508` bytes
- Result: `pseudocode`

```c
typedef struct struct_7 {
    char padding_0[184];
    struct struct_6 *field_b8;
    char padding_c0[32];
    unsigned int field_e0;
} struct_7;

typedef struct struct_3 {
    char padding_0[184];
    struct struct_2 *field_b8;
    char padding_c0[32];
    unsigned int field_e0;
} struct_3;

typedef struct struct_1 {
    char padding_0[264];
    struct struct_0 *field_108;
} struct_1;

typedef struct struct_0 {
    char padding_0[24];
    int field_18;
} struct_0;

typedef struct struct_10 {
    char padding_0[200];
    unsigned long long field_c8;
    char padding_d0[96];
    char field_130;
} struct_10;

typedef struct struct_6 {
    char padding_0[24];
    struct struct_5 *field_18;
} struct_6;

typedef struct struct_2 {
    char padding_0[24];
    struct struct_1 *field_18;
} struct_2;

typedef struct struct_5 {
    char padding_0[264];
    struct struct_4 *field_108;
} struct_5;

typedef struct struct_4 {
    char padding_0[24];
    unsigned int field_18;
} struct_4;

typedef struct struct_8 {
    char padding_0[224];
    unsigned int field_e0;
} struct_8;

extern struct_3 *g_1eeed00;
extern struct_8 *g_1ef0c58;
extern long long g_1ef8a30;
extern long long g_1ef8a38;
extern char g_1fab1df;
extern char g_1fab280;

struct_7 * TouchMarkerGUI_OnGUI(void)
{
    struct_3 *v0;  // x0
    struct_7 *v1;  // x0
    struct_3 *idx;  // x0
    struct_0 *v3;  // x19
    int v4;  // w20
    struct_10 **v5;  // x0
    unsigned long v6;  // x10
    struct_10 **v7;  // x21
    struct_7 *v8;  // x0

    if (!(g_1fab280 & 1))
    {
        sub_f7d92c(&g_1eeed00);
        sub_f7d92c(&g_1ef8a30);
        sub_f7d92c(&g_1ef8a38);
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c("{U");
        g_1fab280 = 1;
    }
    if (!g_1eeed00->field_e0)
        sub_f7da5c(g_1eeed00);
    if (!g_1fab1df)
    {
        sub_f7d92c(&g_1eeed00);
        g_1fab1df = 1;
    }
    v0 = g_1eeed00;
    if (!g_1eeed00->field_e0)
    {
        sub_f7da5c(g_1eeed00);
        v0 = g_1eeed00;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v1 = Object__op_Equality(v0->field_b8->field_18, 0, 0);
    if (((char)v1 & 1))
        return v1;
    if (!g_1eeed00->field_e0)
        sub_f7da5c(g_1eeed00);
    if (!g_1fab1df)
    {
        sub_f7d92c(&g_1eeed00);
        g_1fab1df = 1;
    }
    idx = g_1eeed00;
    if (!g_1eeed00->field_e0)
    {
        sub_f7da5c(g_1eeed00);
        idx = g_1eeed00;
    }
    if (idx->field_b8->field_18)
    {
        v3 = idx->field_b8->field_18->field_108;
        if (v3)
        {
            if (v3->field_18 >= 1)
            {
                v4 = 0;
                while (true)
                {
                    v5 = sub_14a30c0(v3, v4, g_1ef8a38);
                    if (!v5 || (v6 = (unsigned long)(unsigned long long)g_1ef1a70->field_130, (unsigned int)v6 > (unsigned int)*(v5)->field_130))
                    {
                        v7 = NULL;
                    }
                    else if (*((long long *)(*(v5)->field_c8 + v6 * 8 - 8)) == g_1ef1a70)
                    {
                        v7 = v5;
                    }
                    else
                    {
                        v7 = NULL;
                    }
                    if (!g_1ef0c58->field_e0)
                        sub_f7da5c(g_1ef0c58);
                    v8 = Object__op_Inequality(v7, 0, 0);
                    if (((char)v8 & 1))
                    {
                        if (!v7)
                            break;
                        v8 = SuperTouchZone__DrawMarkerGUI(v7);
                    }
                    v4 += 1;
                    if (v4 >= v3->field_18)
                        return v8;
                }
            }
            else
            {
                return idx;
            }
        }
    }
    sub_f7db74();
}
```
