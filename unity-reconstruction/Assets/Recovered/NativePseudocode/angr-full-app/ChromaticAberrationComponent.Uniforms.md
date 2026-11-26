# Native pseudocode: ChromaticAberrationComponent.Uniforms

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `ChromaticAberrationComponent.Uniforms.cctor` — RVA `0xcd09c4`

- Decompiled symbol: `ChromaticAberrationComponent_Uniforms_cctor`
- Metadata signature: `private static void .cctor() { }`
- Native interval: `156` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    unsigned int field_0;
    unsigned int field_4;
} struct_1;

typedef struct struct_0 {
    char padding_0[184];
    struct struct_1 *field_b8;
} struct_0;

extern struct_0 *g_1ef2db8;
extern char g_1fab5b5;

unsigned long long ChromaticAberrationComponent_Uniforms_cctor(void)
{
    unsigned int v0;  // w0
    unsigned long long v1;  // x0

    if (!(g_1fab5b5 & 1))
    {
        sub_f7d92c(&g_1ef2db8);
        sub_f7d92c("K(");
        sub_f7d92c("M(");
        g_1fab5b5 = 1;
    }
    v0 = Shader__PropertyToID(g_1f10318, 0);
    g_1ef2db8->field_b8->field_0 = v0;
    v1 = Shader__PropertyToID(g_1f10320, 0);
    g_1ef2db8->field_b8->field_4 = v1;
    return v1;
}
```
