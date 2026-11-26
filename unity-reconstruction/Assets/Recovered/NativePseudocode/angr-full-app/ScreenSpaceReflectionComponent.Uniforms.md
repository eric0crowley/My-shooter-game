# Native pseudocode: ScreenSpaceReflectionComponent.Uniforms

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `ScreenSpaceReflectionComponent.Uniforms.cctor` — RVA `0xcd8ed0`

- Decompiled symbol: `ScreenSpaceReflectionComponent_Uniforms_cctor`
- Metadata signature: `private static void .cctor() { }`
- Native interval: `1632` bytes
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
    unsigned int field_68;
    unsigned int field_6c;
    unsigned int field_70;
    unsigned int field_74;
    unsigned int field_78;
    unsigned int field_7c;
    unsigned int field_80;
    unsigned int field_84;
    unsigned int field_88;
} struct_1;

typedef struct struct_0 {
    char padding_0[184];
    struct struct_1 *field_b8;
} struct_0;

extern struct_0 *g_1ef3920;
extern long long g_1f10240;
extern long long g_1f10248;
extern long long g_1f10268;
extern long long g_1f10468;
extern long long g_1f10470;
extern long long g_1f10480;
extern long long g_1f104a0;
extern long long g_1f104a8;
extern long long g_1f104b0;
extern long long g_1f10518;
extern long long g_1f10538;
extern long long g_1f105b0;
extern long long g_1f105d8;
extern long long g_1f105f0;
extern long long g_1f10660;
extern long long g_1f10668;
extern long long g_1f107f0;
extern long long g_1f10848;
extern long long g_1f10850;
extern long long g_1f10910;
extern long long g_1f10978;
extern long long g_1f10988;
extern char g_1fab5f5;

unsigned long long ScreenSpaceReflectionComponent_Uniforms_cctor(void)
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
    unsigned int v27;  // w0
    unsigned int v28;  // w0
    unsigned int v29;  // w0
    unsigned int v30;  // w0
    unsigned int v31;  // w0
    unsigned int v5;  // w0
    unsigned int v32;  // w0
    unsigned int v33;  // w0
    unsigned int v34;  // w0
    unsigned int v35;  // w0
    unsigned long long v36;  // x0
    unsigned int v6;  // w0
    unsigned int v7;  // w0
    unsigned int v8;  // w0
    unsigned int v9;  // w0
    unsigned int v10;  // w0
    unsigned int v11;  // w0
    char *v0;  // [bp-0x60]
    char v1;  // [bp+0x0]

    v0 = &v1;
    if (!(g_1fab5f5 & 1))
    {
        sub_f7d92c(&g_1ef3920);
        sub_f7d92c("+(");
        sub_f7d92c("W)");
        sub_f7d92c(&g_1f104b0);
        sub_f7d92c("i(");
        sub_f7d92c(&g_1f10850);
        sub_f7d92c("m)");
        sub_f7d92c(&g_1f10538);
        sub_f7d92c("A(");
        sub_f7d92c(&g_1f10268);
        sub_f7d92c(&g_1f10248);
        sub_f7d92c(&g_1f107f0);
        sub_f7d92c(&g_1f105b0);
        sub_f7d92c("o)");
        sub_f7d92c(&g_1f10978);
        sub_f7d92c("A*");
        sub_f7d92c(&g_1f10660);
        sub_f7d92c(&g_1f104a0);
        sub_f7d92c(&g_1f10480);
        sub_f7d92c("Y)");
        sub_f7d92c("e)");
        sub_f7d92c("))");
        sub_f7d92c("Q)");
        sub_f7d92c(&g_1f10668);
        sub_f7d92c("?(");
        sub_f7d92c(&g_1f10468);
        sub_f7d92c(&g_1f10910);
        sub_f7d92c(&g_1f10240);
        sub_f7d92c(&g_1f104a8);
        sub_f7d92c(&g_1f10848);
        sub_f7d92c(&g_1f10988);
        sub_f7d92c(&g_1f10470);
        sub_f7d92c(&g_1f105d8);
        sub_f7d92c("7(");
        sub_f7d92c(&g_1f105f0);
        sub_f7d92c(&g_1f10518);
        g_1fab5f5 = 1;
    }
    v2 = Shader__PropertyToID(g_1f10780, 0);
    g_1ef3920->field_b8->field_0 = v2;
    v3 = Shader__PropertyToID(g_1f10240, 0);
    g_1ef3920->field_b8->field_4 = v3;
    v4 = Shader__PropertyToID(g_1f10298, 0);
    g_1ef3920->field_b8->field_8 = v4;
    v5 = Shader__PropertyToID(g_1f10988, 0);
    g_1ef3920->field_b8->field_c = v5;
    v6 = Shader__PropertyToID(g_1f10248, 0);
    g_1ef3920->field_b8->field_10 = v6;
    v7 = Shader__PropertyToID(g_1f10978, 0);
    g_1ef3920->field_b8->field_14 = v7;
    v8 = Shader__PropertyToID(g_1f10668, 0);
    g_1ef3920->field_b8->field_18 = v8;
    v9 = Shader__PropertyToID(g_1f104b0, 0);
    g_1ef3920->field_b8->field_1c = v9;
    v10 = Shader__PropertyToID(g_1f10518, 0);
    g_1ef3920->field_b8->field_20 = v10;
    v11 = Shader__PropertyToID(g_1f10538, 0);
    g_1ef3920->field_b8->field_24 = v11;
    v12 = Shader__PropertyToID(g_1f10730, 0);
    g_1ef3920->field_b8->field_28 = v12;
    v13 = Shader__PropertyToID(g_1f10848, 0);
    g_1ef3920->field_b8->field_2c = v13;
    v14 = Shader__PropertyToID(g_1f107a0, 0);
    g_1ef3920->field_b8->field_30 = v14;
    v15 = Shader__PropertyToID(g_1f10660, 0);
    g_1ef3920->field_b8->field_34 = v15;
    v16 = Shader__PropertyToID(g_1f10468, 0);
    g_1ef3920->field_b8->field_38 = v16;
    v17 = Shader__PropertyToID(g_1f105f0, 0);
    g_1ef3920->field_b8->field_3c = v17;
    v18 = Shader__PropertyToID(g_1f107f0, 0);
    g_1ef3920->field_b8->field_40 = v18;
    v19 = Shader__PropertyToID(g_1f104a0, 0);
    g_1ef3920->field_b8->field_44 = v19;
    v20 = Shader__PropertyToID(g_1f104a8, 0);
    g_1ef3920->field_b8->field_48 = v20;
    v21 = Shader__PropertyToID(g_1f107a8, 0);
    g_1ef3920->field_b8->field_4c = v21;
    v22 = Shader__PropertyToID(g_1f10850, 0);
    g_1ef3920->field_b8->field_50 = v22;
    v23 = Shader__PropertyToID(g_1f105d8, 0);
    g_1ef3920->field_b8->field_54 = v23;
    v24 = Shader__PropertyToID(g_1f10748, 0);
    g_1ef3920->field_b8->field_58 = v24;
    v25 = Shader__PropertyToID(g_1f102e8, 0);
    g_1ef3920->field_b8->field_5c = v25;
    v26 = Shader__PropertyToID(g_1f10750, 0);
    g_1ef3920->field_b8->field_60 = v26;
    v27 = Shader__PropertyToID(g_1f10af0, 0);
    g_1ef3920->field_b8->field_64 = v27;
    v28 = Shader__PropertyToID(g_1f102f0, 0);
    g_1ef3920->field_b8->field_68 = v28;
    v29 = Shader__PropertyToID(g_1f10268, 0);
    g_1ef3920->field_b8->field_6c = v29;
    v30 = Shader__PropertyToID(g_1f10390, 0);
    g_1ef3920->field_b8->field_70 = v30;
    v31 = Shader__PropertyToID(g_1f10690, 0);
    g_1ef3920->field_b8->field_74 = v31;
    v32 = Shader__PropertyToID(g_1f105b0, 0);
    g_1ef3920->field_b8->field_78 = v32;
    v33 = Shader__PropertyToID(g_1f102c8, 0);
    g_1ef3920->field_b8->field_7c = v33;
    v34 = Shader__PropertyToID(g_1f10470, 0);
    g_1ef3920->field_b8->field_80 = v34;
    v35 = Shader__PropertyToID(g_1f10480, 0);
    g_1ef3920->field_b8->field_84 = v35;
    v36 = Shader__PropertyToID(g_1f10910, 0);
    g_1ef3920->field_b8->field_88 = v36;
    return v36;
}
```
