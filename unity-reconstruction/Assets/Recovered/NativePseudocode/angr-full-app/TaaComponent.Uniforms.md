# Native pseudocode: TaaComponent.Uniforms

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `TaaComponent.Uniforms.cctor` — RVA `0xcda410`

- Decompiled symbol: `TaaComponent_Uniforms_cctor`
- Metadata signature: `private static void .cctor() { }`
- Native interval: `296` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    unsigned int field_0;
    unsigned int field_4;
    unsigned int field_8;
    unsigned int field_c;
    unsigned int field_10;
} struct_1;

typedef struct struct_0 {
    char padding_0[184];
    struct struct_1 *field_b8;
} struct_0;

extern struct_0 *g_1ef3b10;
extern long long g_1f10478;
extern long long g_1f105a8;
extern long long g_1f105e8;
extern long long g_1f10630;
extern long long g_1f10868;
extern char g_1fab5fb;

unsigned long long TaaComponent_Uniforms_cctor(void)
{
    unsigned int v0;  // w0
    unsigned int v1;  // w0
    unsigned int v2;  // w0
    unsigned int v3;  // w0
    unsigned long long v4;  // x0

    if (!(g_1fab5fb & 1))
    {
        sub_f7d92c(&g_1ef3b10);
        sub_f7d92c(&g_1f105e8);
        sub_f7d92c(&g_1f10630);
        sub_f7d92c(&g_1f10868);
        sub_f7d92c(&g_1f10478);
        sub_f7d92c(&g_1f105a8);
        g_1fab5fb = 1;
    }
    v0 = Shader__PropertyToID(g_1f105e8, 0);
    g_1ef3b10->field_b8->field_0 = v0;
    v1 = Shader__PropertyToID(g_1f10868, 0);
    g_1ef3b10->field_b8->field_4 = v1;
    v2 = Shader__PropertyToID(g_1f10478, 0);
    g_1ef3b10->field_b8->field_8 = v2;
    v3 = Shader__PropertyToID(g_1f105a8, 0);
    g_1ef3b10->field_b8->field_c = v3;
    v4 = Shader__PropertyToID(g_1f10630, 0);
    g_1ef3b10->field_b8->field_10 = v4;
    return v4;
}
```
