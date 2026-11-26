# Native pseudocode: BloomComponent.Uniforms

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `BloomComponent.Uniforms.cctor` — RVA `0xccf2bc`

- Decompiled symbol: `BloomComponent_Uniforms_cctor`
- Metadata signature: `private static void .cctor() { }`
- Native interval: `532` bytes
- Result: `pseudocode`

```c
extern long long g_1f10260;
extern long long g_1f10800;
extern long long g_1f10938;
extern char g_1fab5a5;

unsigned long long BloomComponent_Uniforms_cctor(void)
{
    unsigned int v2;  // w0
    unsigned int v3;  // w0
    unsigned int v4;  // w0
    unsigned int v5;  // w0
    unsigned int v6;  // w0
    unsigned int v7;  // w0
    unsigned int v8;  // w0
    unsigned int v9;  // w0
    unsigned int v10;  // w0
    unsigned long long v11;  // x0
    char *v0;  // [bp-0x60]
    char v1;  // [bp+0x0]

    v0 = &v1;
    if (!(g_1fab5a5 & 1))
    {
        sub_f7d92c("\tf");
        sub_f7d92c(&g_1f10938);
        sub_f7d92c("3(");
        sub_f7d92c(&g_1f10800);
        sub_f7d92c("1(");
        sub_f7d92c("/(");
        sub_f7d92c("k(");
        sub_f7d92c(&g_1f10260);
        sub_f7d92c("-(");
        sub_f7d92c("#(");
        sub_f7d92c("U)");
        g_1fab5a5 = 1;
    }
    v2 = Shader__PropertyToID(g_1f10260, 0);
    g_1ef2cd0->field_b8->field_0 = v2;
    v3 = Shader__PropertyToID(g_1f10938, 0);
    g_1ef2cd0->field_b8->field_4 = v3;
    v4 = Shader__PropertyToID(g_1f10398, 0);
    g_1ef2cd0->field_b8->field_8 = v4;
    v5 = Shader__PropertyToID(g_1f10740, 0);
    g_1ef2cd0->field_b8->field_c = v5;
    v6 = Shader__PropertyToID(g_1f10800, 0);
    g_1ef2cd0->field_b8->field_10 = v6;
    v7 = Shader__PropertyToID(g_1f10278, 0);
    g_1ef2cd0->field_b8->field_14 = v7;
    v8 = Shader__PropertyToID(g_1f102a0, 0);
    g_1ef2cd0->field_b8->field_18 = v8;
    v9 = Shader__PropertyToID(g_1f102b8, 0);
    g_1ef2cd0->field_b8->field_1c = v9;
    v10 = Shader__PropertyToID(g_1f102b0, 0);
    g_1ef2cd0->field_b8->field_20 = v10;
    v11 = Shader__PropertyToID(g_1f102a8, 0);
    g_1ef2cd0->field_b8->field_24 = v11;
    return v11;
}
```
