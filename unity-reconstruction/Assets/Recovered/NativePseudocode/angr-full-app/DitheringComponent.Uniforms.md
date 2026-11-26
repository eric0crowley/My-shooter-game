# Native pseudocode: DitheringComponent.Uniforms

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `DitheringComponent.Uniforms.cctor` — RVA `0xcd35f4`

- Decompiled symbol: `DitheringComponent_Uniforms_cctor`
- Metadata signature: `private static void .cctor() { }`
- Native interval: `156` bytes
- Result: `pseudocode`

```c
extern long long g_1f103e8;
extern char g_1fab5cb;

unsigned long long DitheringComponent_Uniforms_cctor(void)
{
    unsigned int v0;  // w0
    unsigned long long v1;  // x0

    if (!(g_1fab5cb & 1))
    {
        sub_f7d92c("Oh");
        sub_f7d92c(&g_1f103e8);
        sub_f7d92c("}(");
        g_1fab5cb = 1;
    }
    v0 = Shader__PropertyToID(g_1f103e8, 0);
    g_1ef2f90->field_b8->field_0 = v0;
    v1 = Shader__PropertyToID(g_1f103e0, 0);
    g_1ef2f90->field_b8->field_4 = v1;
    return v1;
}
```
