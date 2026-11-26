# Native pseudocode: FxaaComponent.Uniforms

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `FxaaComponent.Uniforms.cctor` — RVA `0xcd503c`

- Decompiled symbol: `FxaaComponent_Uniforms_cctor`
- Metadata signature: `private static void .cctor() { }`
- Native interval: `156` bytes
- Result: `pseudocode`

```c
extern char g_1fab5db;

unsigned long long FxaaComponent_Uniforms_cctor(void)
{
    unsigned int v0;  // w0
    unsigned long long v1;  // x0

    if (!(g_1fab5db & 1))
    {
        sub_f7d92c(";j");
        sub_f7d92c("_(");
        sub_f7d92c("a)");
        g_1fab5db = 1;
    }
    v0 = Shader__PropertyToID(g_1f10770, 0);
    g_1ef31a8->field_b8->field_0 = v0;
    v1 = Shader__PropertyToID(g_1f10368, 0);
    g_1ef31a8->field_b8->field_4 = v1;
    return v1;
}
```
