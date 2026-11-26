# Native pseudocode: EyeAdaptationComponent.Uniforms

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `EyeAdaptationComponent.Uniforms.cctor` — RVA `0xcd456c`

- Decompiled symbol: `EyeAdaptationComponent_Uniforms_cctor`
- Metadata signature: `private static void .cctor() { }`
- Native interval: `348` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    unsigned int field_0;
    unsigned int field_4;
    unsigned int field_8;
    unsigned int field_c;
    unsigned int field_10;
    unsigned int field_14;
} struct_1;

typedef struct struct_0 {
    char padding_0[184];
    struct struct_1 *field_b8;
} struct_0;

extern struct_0 *g_1ef30d8;
extern long long g_1f10260;
extern long long g_1f10438;
extern long long g_1f10818;
extern long long g_1f108a0;
extern char g_1fab5d2;

unsigned long long EyeAdaptationComponent_Uniforms_cctor(void)
{
    unsigned int v0;  // w0
    unsigned int v1;  // w0
    unsigned int v2;  // w0
    unsigned int v3;  // w0
    unsigned int v4;  // w0
    unsigned long long v5;  // x0

    if (!(g_1fab5d2 & 1))
    {
        sub_f7d92c(&g_1ef30d8);
        sub_f7d92c(&g_1f108a0);
        sub_f7d92c(&g_1f10438);
        sub_f7d92c(&g_1f10818);
        sub_f7d92c(&g_1f10260);
        sub_f7d92c("o(");
        sub_f7d92c("K)");
        g_1fab5d2 = 1;
    }
    v0 = Shader__PropertyToID(g_1f10718, 0);
    g_1ef30d8->field_b8->field_0 = v0;
    v1 = Shader__PropertyToID(g_1f108a0, 0);
    g_1ef30d8->field_b8->field_4 = v1;
    v2 = Shader__PropertyToID(g_1f10818, 0);
    g_1ef30d8->field_b8->field_8 = v2;
    v3 = Shader__PropertyToID(g_1f10438, 0);
    g_1ef30d8->field_b8->field_c = v3;
    v4 = Shader__PropertyToID(g_1f10260, 0);
    g_1ef30d8->field_b8->field_10 = v4;
    v5 = Shader__PropertyToID(g_1f103a8, 0);
    g_1ef30d8->field_b8->field_14 = v5;
    return v5;
}
```
