# Native pseudocode: FogComponent.Uniforms

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `FogComponent.Uniforms.cctor` — RVA `0xcd4c5c`

- Decompiled symbol: `FogComponent_Uniforms_cctor`
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

extern struct_0 *g_1ef3150;
extern long long g_1f10418;
extern long long g_1f10490;
extern long long g_1f108a8;
extern long long g_1f10900;
extern char g_1fab5d7;

unsigned long long FogComponent_Uniforms_cctor(void)
{
    unsigned int v0;  // w0
    unsigned int v1;  // w0
    unsigned int v2;  // w0
    unsigned int v3;  // w0
    unsigned long long v4;  // x0

    if (!(g_1fab5d7 & 1))
    {
        sub_f7d92c(&g_1ef3150);
        sub_f7d92c("q(");
        sub_f7d92c(&g_1f10490);
        sub_f7d92c(&g_1f10418);
        sub_f7d92c(&g_1f10900);
        sub_f7d92c(&g_1f108a8);
        g_1fab5d7 = 1;
    }
    v0 = Shader__PropertyToID(g_1f10490, 0);
    g_1ef3150->field_b8->field_0 = v0;
    v1 = Shader__PropertyToID(g_1f103b0, 0);
    g_1ef3150->field_b8->field_4 = v1;
    v2 = Shader__PropertyToID(g_1f108a8, 0);
    g_1ef3150->field_b8->field_8 = v2;
    v3 = Shader__PropertyToID(g_1f10418, 0);
    g_1ef3150->field_b8->field_c = v3;
    v4 = Shader__PropertyToID(g_1f10900, 0);
    g_1ef3150->field_b8->field_10 = v4;
    return v4;
}
```
