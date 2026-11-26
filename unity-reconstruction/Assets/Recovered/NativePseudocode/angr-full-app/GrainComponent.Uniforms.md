# Native pseudocode: GrainComponent.Uniforms

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `GrainComponent.Uniforms.cctor` — RVA `0xcd556c`

- Decompiled symbol: `GrainComponent_Uniforms_cctor`
- Metadata signature: `private static void .cctor() { }`
- Native interval: `252` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    unsigned int field_0;
    unsigned int field_4;
    unsigned int field_8;
    unsigned int field_c;
} struct_1;

typedef struct struct_0 {
    char padding_0[184];
    struct struct_1 *field_b8;
} struct_0;

extern struct_0 *g_1ef3248;
extern long long g_1f10500;
extern long long g_1f10508;
extern long long g_1f10510;
extern char g_1fab5df;

unsigned long long GrainComponent_Uniforms_cctor(void)
{
    unsigned int v0;  // w0
    unsigned int v1;  // w0
    unsigned int v2;  // w0
    unsigned long long v3;  // x0

    if (!(g_1fab5df & 1))
    {
        sub_f7d92c(&g_1ef3248);
        sub_f7d92c("O)");
        sub_f7d92c(&g_1f10500);
        sub_f7d92c(&g_1f10508);
        sub_f7d92c(&g_1f10510);
        g_1fab5df = 1;
    }
    v0 = Shader__PropertyToID(g_1f10508, 0);
    g_1ef3248->field_b8->field_0 = v0;
    v1 = Shader__PropertyToID(g_1f10510, 0);
    g_1ef3248->field_b8->field_4 = v1;
    v2 = Shader__PropertyToID(g_1f10500, 0);
    g_1ef3248->field_b8->field_8 = v2;
    v3 = Shader__PropertyToID(g_1f10728, 0);
    g_1ef3248->field_b8->field_c = v3;
    return v3;
}
```
