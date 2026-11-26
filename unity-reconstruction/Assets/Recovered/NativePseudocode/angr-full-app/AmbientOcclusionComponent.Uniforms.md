# Native pseudocode: AmbientOcclusionComponent.Uniforms

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `AmbientOcclusionComponent.Uniforms.cctor` — RVA `0xcce61c`

- Decompiled symbol: `AmbientOcclusionComponent_Uniforms_cctor`
- Metadata signature: `private static void .cctor() { }`
- Native interval: `532` bytes
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
} struct_1;

typedef struct struct_0 {
    char padding_0[184];
    struct struct_1 *field_b8;
} struct_0;

extern struct_0 *g_1ef2bc0;
extern long long g_1f103f0;
extern long long g_1f10498;
extern long long g_1f105c8;
extern long long g_1f10630;
extern long long g_1f107f8;
extern long long g_1f10900;
extern char g_1fab5a1;

unsigned long long AmbientOcclusionComponent_Uniforms_cctor(void)
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
    if (!(g_1fab5a1 & 1))
    {
        sub_f7d92c(&g_1ef2bc0);
        sub_f7d92c("+)");
        sub_f7d92c("-)");
        sub_f7d92c(&g_1f10630);
        sub_f7d92c(&g_1f105c8);
        sub_f7d92c(&g_1f103f0);
        sub_f7d92c(&g_1f10900);
        sub_f7d92c("/)");
        sub_f7d92c(&g_1f10498);
        sub_f7d92c(&g_1f107f8);
        sub_f7d92c("c)");
        g_1fab5a1 = 1;
    }
    v2 = Shader__PropertyToID(g_1f105c8, 0);
    g_1ef2bc0->field_b8->field_0 = v2;
    v3 = Shader__PropertyToID(g_1f10778, 0);
    g_1ef2bc0->field_b8->field_4 = v3;
    v4 = Shader__PropertyToID(g_1f10498, 0);
    g_1ef2bc0->field_b8->field_8 = v4;
    v5 = Shader__PropertyToID(g_1f103f0, 0);
    g_1ef2bc0->field_b8->field_c = v5;
    v6 = Shader__PropertyToID(g_1f107f8, 0);
    g_1ef2bc0->field_b8->field_10 = v6;
    v7 = Shader__PropertyToID(g_1f106a0, 0);
    g_1ef2bc0->field_b8->field_14 = v7;
    v8 = Shader__PropertyToID(g_1f106a8, 0);
    g_1ef2bc0->field_b8->field_18 = v8;
    v9 = Shader__PropertyToID(g_1f10698, 0);
    g_1ef2bc0->field_b8->field_1c = v9;
    v10 = Shader__PropertyToID(g_1f10630, 0);
    g_1ef2bc0->field_b8->field_20 = v10;
    v11 = Shader__PropertyToID(g_1f10900, 0);
    g_1ef2bc0->field_b8->field_24 = v11;
    return v11;
}
```
