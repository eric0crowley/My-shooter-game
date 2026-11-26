# Native pseudocode: GunRotation

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `GunRotation.Update` — RVA `0xcc2624`

- Decompiled symbol: `GunRotation_Update`
- Metadata signature: `private void Update() { }`
- Native interval: `256` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1eeed00;
extern long long g_1ef22e8;
extern long long g_1f0c3a8;
extern char g_1fab51d;
extern char g_1fab590;

void GunRotation_Update(long long a0)
{
    unsigned long long v5;  // d8
    unsigned long long v6;  // x30
    unsigned long long v7;  // x21
    unsigned long long v8;  // x20
    unsigned long long v9;  // x19
    long long v10;  // x0
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
    if (!(g_1fab51d & 1))
    {
        sub_f7d92c(&g_1eeed00);
        sub_f7d92c(&g_1f0c3a8);
        g_1fab51d = 1;
    }
    if (Component__get_transform(a0, 0))
    {
        Transform__Rotate();
        if (!g_1eeed00->field_e0)
            sub_f7da5c(g_1eeed00);
        CF2Input__GetAxis(g_1f0c3a8, 0);
        v10 = Component__get_transform(a0, 0);
        if (!g_1fab590)
        {
            sub_f7d92c(&g_1ef22e8);
            g_1fab590 = 1;
        }
    }
    sub_f7db74();
}
```

## `GunRotation.ctor` — RVA `0xcc2724`

- Decompiled symbol: `GunRotation_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long GunRotation_ctor(void)
{
    long long v0;  // x0

    v0 = MonoBehaviour__ctor();
    return MonoBehaviour__ctor();
}
```
