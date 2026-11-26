# Native pseudocode: VignetteComponent.Uniforms

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `VignetteComponent.Uniforms.cctor` — RVA `0xcdac9c`

- Decompiled symbol: `VignetteComponent_Uniforms_cctor`
- Metadata signature: `private static void .cctor() { }`
- Native interval: `296` bytes
- Result: `pseudocode`

```c
extern char g_1fab604;

unsigned long long VignetteComponent_Uniforms_cctor(void)
{
    unsigned int v0;  // w0
    unsigned int v1;  // w0
    unsigned int v2;  // w0
    unsigned int v3;  // w0
    unsigned long long v4;  // x0

    if (!(g_1fab604 & 1))
    {
        sub_f7d92c("3u");
        sub_f7d92c("-*");
        sub_f7d92c("+*");
        sub_f7d92c("/*");
        sub_f7d92c("1*");
        sub_f7d92c("3*");
        g_1fab604 = 1;
    }
    v0 = Shader__PropertyToID(g_1f10aa0, 0);
    g_1ef3f48->field_b8->field_0 = v0;
    v1 = Shader__PropertyToID(g_1f10a98, 0);
    g_1ef3f48->field_b8->field_4 = v1;
    v2 = Shader__PropertyToID(g_1f10ab8, 0);
    g_1ef3f48->field_b8->field_8 = v2;
    v3 = Shader__PropertyToID(g_1f10aa8, 0);
    g_1ef3f48->field_b8->field_c = v3;
    v4 = Shader__PropertyToID(g_1f10ab0, 0);
    g_1ef3f48->field_b8->field_10 = v4;
    return v4;
}
```
