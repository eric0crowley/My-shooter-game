# Native pseudocode: ColorGradingComponent.Uniforms

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `ColorGradingComponent.Uniforms.cctor` — RVA `0xcd21f8`

- Decompiled symbol: `ColorGradingComponent_Uniforms_cctor`
- Metadata signature: `private static void .cctor() { }`
- Native interval: `972` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    unsigned int field_0;
    unsigned int field_4;
    unsigned int field_8;
    unsigned int field_c;
    unsigned int field_10;
    unsigned int field_14;
    unsigned int field_18;
    unsigned int field_1c;
    unsigned int field_20;
    unsigned int field_24;
    unsigned int field_28;
    unsigned int field_2c;
    unsigned int field_30;
    unsigned int field_34;
    unsigned int field_38;
    unsigned int field_3c;
    unsigned int field_40;
    unsigned int field_44;
    unsigned int field_48;
    unsigned int field_4c;
} struct_1;

typedef struct struct_0 {
    char padding_0[184];
    struct struct_1 *field_b8;
} struct_0;

extern struct_0 *g_1ef2de0;
extern long long g_1f10440;
extern long long g_1f104b8;
extern long long g_1f105b8;
extern long long g_1f105d0;
extern long long g_1f10600;
extern long long g_1f10618;
extern long long g_1f10628;
extern long long g_1f10808;
extern long long g_1f10880;
extern char g_1fab5be;

unsigned long long ColorGradingComponent_Uniforms_cctor(void)
{
    unsigned int v2;  // w0
    unsigned int v3;  // w0
    unsigned int v12;  // w0
    unsigned int v13;  // w0
    unsigned int v14;  // w0
    unsigned int v15;  // w0
    unsigned int v16;  // w0
    unsigned int v17;  // w0
    unsigned int v18;  // w0
    unsigned int v19;  // w0
    unsigned int v20;  // w0
    unsigned long long v21;  // x0
    unsigned int v4;  // w0
    unsigned int v5;  // w0
    unsigned int v6;  // w0
    unsigned int v7;  // w0
    unsigned int v8;  // w0
    unsigned int v9;  // w0
    unsigned int v10;  // w0
    unsigned int v11;  // w0
    char *v0;  // [bp-0x60]
    char v1;  // [bp+0x0]

    v0 = &v1;
    if (!(g_1fab5be & 1))
    {
        sub_f7d92c(&g_1ef2de0);
        sub_f7d92c(&g_1f105b8);
        sub_f7d92c("!(");
        sub_f7d92c("G(");
        sub_f7d92c("E(");
        sub_f7d92c(&g_1f10600);
        sub_f7d92c(&g_1f10618);
        sub_f7d92c("\t)");
        sub_f7d92c(&g_1f10440);
        sub_f7d92c(&g_1f10880);
        sub_f7d92c("')");
        sub_f7d92c("I(");
        sub_f7d92c("m(");
        sub_f7d92c(&g_1f105d0);
        sub_f7d92c("S)");
        sub_f7d92c(&g_1f104b8);
        sub_f7d92c("%)");
        sub_f7d92c(&g_1f10628);
        sub_f7d92c("1)");
        sub_f7d92c("a(");
        sub_f7d92c(&g_1f10808);
        g_1fab5be = 1;
    }
    v2 = Shader__PropertyToID(g_1f10628, 0);
    g_1ef2de0->field_b8->field_0 = v2;
    v3 = Shader__PropertyToID(g_1f10680, 0);
    g_1ef2de0->field_b8->field_4 = v3;
    v4 = Shader__PropertyToID(g_1f10688, 0);
    g_1ef2de0->field_b8->field_8 = v4;
    v5 = Shader__PropertyToID(g_1f105b8, 0);
    g_1ef2de0->field_b8->field_c = v5;
    v6 = Shader__PropertyToID(g_1f10808, 0);
    g_1ef2de0->field_b8->field_10 = v6;
    v7 = Shader__PropertyToID(g_1f10370, 0);
    g_1ef2de0->field_b8->field_14 = v7;
    v8 = Shader__PropertyToID(g_1f10270, 0);
    g_1ef2de0->field_b8->field_18 = v8;
    v9 = Shader__PropertyToID(g_1f10600, 0);
    g_1ef2de0->field_b8->field_1c = v9;
    v10 = Shader__PropertyToID(g_1f105d0, 0);
    g_1ef2de0->field_b8->field_20 = v10;
    v11 = Shader__PropertyToID(g_1f104b8, 0);
    g_1ef2de0->field_b8->field_24 = v11;
    v12 = Shader__PropertyToID(g_1f10880, 0);
    g_1ef2de0->field_b8->field_28 = v12;
    v13 = Shader__PropertyToID(g_1f10738, 0);
    g_1ef2de0->field_b8->field_2c = v13;
    v14 = Shader__PropertyToID(g_1f106b0, 0);
    g_1ef2de0->field_b8->field_30 = v14;
    v15 = Shader__PropertyToID(g_1f10310, 0);
    g_1ef2de0->field_b8->field_34 = v15;
    v16 = Shader__PropertyToID(g_1f10308, 0);
    g_1ef2de0->field_b8->field_38 = v16;
    v17 = Shader__PropertyToID(g_1f10300, 0);
    g_1ef2de0->field_b8->field_3c = v17;
    v18 = Shader__PropertyToID(g_1f103a0, 0);
    g_1ef2de0->field_b8->field_40 = v18;
    v19 = Shader__PropertyToID(g_1f10610, 0);
    g_1ef2de0->field_b8->field_44 = v19;
    v20 = Shader__PropertyToID(g_1f10618, 0);
    g_1ef2de0->field_b8->field_48 = v20;
    v21 = Shader__PropertyToID(g_1f10440, 0);
    g_1ef2de0->field_b8->field_4c = v21;
    return v21;
}
```
