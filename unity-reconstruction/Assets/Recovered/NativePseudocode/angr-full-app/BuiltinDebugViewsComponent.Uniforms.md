# Native pseudocode: BuiltinDebugViewsComponent.Uniforms

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `BuiltinDebugViewsComponent.Uniforms.cctor` — RVA `0xcd04ac`

- Decompiled symbol: `BuiltinDebugViewsComponent_Uniforms_cctor`
- Metadata signature: `private static void .cctor() { }`
- Native interval: `392` bytes
- Result: `pseudocode`

```c
extern long long g_1f10250;
extern long long g_1f10630;
extern long long g_1f10810;
extern long long g_1f10900;
extern long long g_1f10908;
extern char g_1fab5b0;

unsigned long long BuiltinDebugViewsComponent_Uniforms_cctor(void)
{
    unsigned int v0;  // w0
    unsigned int v1;  // w0
    unsigned int v2;  // w0
    unsigned int v3;  // w0
    unsigned int v4;  // w0
    unsigned int v5;  // w0
    unsigned long long v6;  // x0

    if (!(g_1fab5b0 & 1))
    {
        sub_f7d92c("9f");
        sub_f7d92c("y(");
        sub_f7d92c(&g_1f10630);
        sub_f7d92c("3)");
        sub_f7d92c(&g_1f10900);
        sub_f7d92c(&g_1f10810);
        sub_f7d92c(&g_1f10908);
        sub_f7d92c(&g_1f10250);
        g_1fab5b0 = 1;
    }
    v0 = Shader__PropertyToID(g_1f103d0, 0);
    g_1ef2d28->field_b8->field_0 = v0;
    v1 = Shader__PropertyToID(g_1f10900, 0);
    g_1ef2d28->field_b8->field_4 = v1;
    v2 = Shader__PropertyToID(g_1f106b8, 0);
    g_1ef2d28->field_b8->field_8 = v2;
    v3 = Shader__PropertyToID(g_1f10630, 0);
    g_1ef2d28->field_b8->field_c = v3;
    v4 = Shader__PropertyToID(g_1f10908, 0);
    g_1ef2d28->field_b8->field_10 = v4;
    v5 = Shader__PropertyToID(g_1f10250, 0);
    g_1ef2d28->field_b8->field_14 = v5;
    v6 = Shader__PropertyToID(g_1f10810, 0);
    g_1ef2d28->field_b8->field_18 = v6;
    return v6;
}
```
