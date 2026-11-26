# Native pseudocode: MultiDimensionalPool

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `MultiDimensionalPool.ctor` — RVA `0xc99004`

- Decompiled symbol: `MultiDimensionalPool_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `136` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[40];
    long long field_28;
} struct_0;

extern long long g_1eed618;
extern long long g_1ef7b40;
extern char g_1fab492;

void MultiDimensionalPool_ctor(struct_0 *ptr)
{
    unsigned long long v5;  // x30
    unsigned long long v6;  // x22
    unsigned long long v7;  // x21
    unsigned long long v8;  // x20
    unsigned long long v9;  // x19
    long long v10;  // x20
    unsigned long long v0;  // [bp-0x30]
    unsigned long long v1;  // [bp-0x20]
    unsigned long long v2;  // [bp-0x18]
    unsigned long long v3;  // [bp-0x10]
    unsigned long long v4;  // [bp-0x8]

    v0 = v5;
    v1 = v6;
    v2 = v7;
    v3 = v8;
    v4 = v9;
    if (!(g_1fab492 & 1))
    {
        sub_f7d92c(&g_1ef7b40);
        sub_f7d92c(&g_1eed618);
        g_1fab492 = 1;
    }
    v10 = sub_f7db70(g_1eed618);
    sub_14a2b64(v10, g_1ef7b40);
    ptr->field_28 = v10;
    sub_f7d8d0((struct struct_0 *)&ptr->field_28, v10);
    Object__ctor();
    return;
}
```
