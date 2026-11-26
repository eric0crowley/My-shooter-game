# Native pseudocode: MotionBlurComponent.Uniforms

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `MotionBlurComponent.Uniforms.cctor` — RVA `0xcd6fb8`

- Decompiled symbol: `MotionBlurComponent_Uniforms_cctor`
- Metadata signature: `private static void .cctor() { }`
- Native interval: `1236` bytes
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
    unsigned int field_50;
    unsigned int field_54;
    unsigned int field_58;
    unsigned int field_5c;
    unsigned int field_60;
    unsigned int field_64;
} struct_1;

typedef struct struct_0 {
    char padding_0[184];
    struct struct_1 *field_b8;
} struct_0;

extern struct_0 *g_1ef3510;
extern long long g_1f10548;
extern long long g_1f10550;
extern long long g_1f10558;
extern long long g_1f10560;
extern long long g_1f10568;
extern long long g_1f10570;
extern long long g_1f10578;
extern long long g_1f10580;
extern long long g_1f10588;
extern long long g_1f10590;
extern long long g_1f10598;
extern long long g_1f105a0;
extern long long g_1f10630;
extern long long g_1f10650;
extern long long g_1f10900;
extern long long g_1f10940;
extern long long g_1f10948;
extern long long g_1f10950;
extern long long g_1f10958;
extern long long g_1f10960;
extern long long g_1f10968;
extern long long g_1f10a60;
extern long long g_1f10a68;
extern char g_1fab5e6;

unsigned long long MotionBlurComponent_Uniforms_cctor(void)
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
    unsigned int v21;  // w0
    unsigned int v4;  // w0
    unsigned int v22;  // w0
    unsigned int v23;  // w0
    unsigned int v24;  // w0
    unsigned int v25;  // w0
    unsigned int v26;  // w0
    unsigned long long v27;  // x0
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
    if (!(g_1fab5e6 & 1))
    {
        sub_f7d92c(&g_1ef3510);
        sub_f7d92c(&g_1f105a0);
        sub_f7d92c(&g_1f10950);
        sub_f7d92c(&g_1f10598);
        sub_f7d92c("#)");
        sub_f7d92c(&g_1f10550);
        sub_f7d92c(&g_1f10650);
        sub_f7d92c(&g_1f10630);
        sub_f7d92c(&g_1f10570);
        sub_f7d92c(&g_1f10900);
        sub_f7d92c(&g_1f10968);
        sub_f7d92c(&g_1f10568);
        sub_f7d92c(&g_1f10558);
        sub_f7d92c(&g_1f10948);
        sub_f7d92c(&g_1f10578);
        sub_f7d92c(&g_1f10958);
        sub_f7d92c("\r)");
        sub_f7d92c(&g_1f10940);
        sub_f7d92c(&g_1f10590);
        sub_f7d92c(&g_1f10a60);
        sub_f7d92c("i)");
        sub_f7d92c(&g_1f10580);
        sub_f7d92c(&g_1f10548);
        sub_f7d92c(&g_1f10560);
        sub_f7d92c(&g_1f10588);
        sub_f7d92c(&g_1f10960);
        sub_f7d92c(&g_1f10a68);
        g_1fab5e6 = 1;
    }
    v2 = Shader__PropertyToID(g_1f10a60, 0);
    g_1ef3510->field_b8->field_0 = v2;
    v3 = Shader__PropertyToID(g_1f10650, 0);
    g_1ef3510->field_b8->field_4 = v3;
    v4 = Shader__PropertyToID(g_1f10790, 0);
    g_1ef3510->field_b8->field_8 = v4;
    v5 = Shader__PropertyToID(g_1f10a68, 0);
    g_1ef3510->field_b8->field_c = v5;
    v6 = Shader__PropertyToID(g_1f10630, 0);
    g_1ef3510->field_b8->field_10 = v6;
    v7 = Shader__PropertyToID(g_1f10940, 0);
    g_1ef3510->field_b8->field_14 = v7;
    v8 = Shader__PropertyToID(g_1f10948, 0);
    g_1ef3510->field_b8->field_18 = v8;
    v9 = Shader__PropertyToID(g_1f10950, 0);
    g_1ef3510->field_b8->field_1c = v9;
    v10 = Shader__PropertyToID(g_1f10960, 0);
    g_1ef3510->field_b8->field_20 = v10;
    v11 = Shader__PropertyToID(g_1f10958, 0);
    g_1ef3510->field_b8->field_24 = v11;
    v12 = Shader__PropertyToID(g_1f10968, 0);
    g_1ef3510->field_b8->field_28 = v12;
    v13 = Shader__PropertyToID(g_1f10678, 0);
    g_1ef3510->field_b8->field_2c = v13;
    v14 = Shader__PropertyToID(g_1f10620, 0);
    g_1ef3510->field_b8->field_30 = v14;
    v15 = Shader__PropertyToID(g_1f10900, 0);
    g_1ef3510->field_b8->field_34 = v15;
    v16 = Shader__PropertyToID(g_1f10550, 0);
    g_1ef3510->field_b8->field_38 = v16;
    v17 = Shader__PropertyToID(g_1f10568, 0);
    g_1ef3510->field_b8->field_3c = v17;
    v18 = Shader__PropertyToID(g_1f10580, 0);
    g_1ef3510->field_b8->field_40 = v18;
    v19 = Shader__PropertyToID(g_1f10598, 0);
    g_1ef3510->field_b8->field_44 = v19;
    v20 = Shader__PropertyToID(g_1f10548, 0);
    g_1ef3510->field_b8->field_48 = v20;
    v21 = Shader__PropertyToID(g_1f10560, 0);
    g_1ef3510->field_b8->field_4c = v21;
    v22 = Shader__PropertyToID(g_1f10578, 0);
    g_1ef3510->field_b8->field_50 = v22;
    v23 = Shader__PropertyToID(g_1f10590, 0);
    g_1ef3510->field_b8->field_54 = v23;
    v24 = Shader__PropertyToID(g_1f10558, 0);
    g_1ef3510->field_b8->field_58 = v24;
    v25 = Shader__PropertyToID(g_1f10570, 0);
    g_1ef3510->field_b8->field_5c = v25;
    v26 = Shader__PropertyToID(g_1f10588, 0);
    g_1ef3510->field_b8->field_60 = v26;
    v27 = Shader__PropertyToID(g_1f105a0, 0);
    g_1ef3510->field_b8->field_64 = v27;
    return v27;
}
```
