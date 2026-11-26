# Native pseudocode: LeanColliderDamage

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `LeanColliderDamage.Start` — RVA `0xca76c8`

- Decompiled symbol: `LeanColliderDamage_Start`
- Metadata signature: `private void Start() { }`
- Native interval: `140` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[40];
    long long field_28;
} struct_0;

typedef struct struct_1 {
    char padding_0[32];
    long long field_20;
} struct_1;

extern long long g_1efcf38;
extern long long g_1efebb8;
extern char g_1fab4bf;

void LeanColliderDamage_Start(struct_1 *ptr)
{
    unsigned long long v3;  // x30
    unsigned long long v4;  // x20
    unsigned long long v5;  // x19
    struct_0 *v6;  // x0
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x10]
    unsigned long long v2;  // [bp-0x8]

    v0 = v3;
    v1 = v4;
    v2 = v5;
    if (!(g_1fab4bf & 1))
    {
        sub_f7d92c(&g_1efcf38);
        sub_f7d92c(&g_1efebb8);
        g_1fab4bf = 1;
    }
    if (Camera__get_main(0))
    {
        v6 = sub_1231bc8();
        if (v6 && v6->field_28)
        {
            ptr->field_20 = sub_1249224(v6->field_28, g_1efebb8);
            sub_f7d8d0();
            return;
        }
    }
    sub_f7db74();
}
```

## `LeanColliderDamage.ApplyDamage` — RVA `0xca7754`

- Decompiled symbol: `LeanColliderDamage_ApplyDamage`
- Metadata signature: `public void ApplyDamage(float damage) { }`
- Native interval: `36` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[32];
    unsigned long long field_20;
} struct_0;

void LeanColliderDamage_ApplyDamage(struct_0 *a0)
{
    unsigned long long v1;  // x30
    unsigned long long v0;  // [bp-0x10]

    v0 = v1;
    if (a0->field_20)
    {
        FPSPlayer__ApplyDamage();
        return;
    }
    sub_f7db74(0);
}
```

## `LeanColliderDamage.ctor` — RVA `0xca7778`

- Decompiled symbol: `LeanColliderDamage_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long LeanColliderDamage_ctor(void)
{
    long long v0;  // x0

    v0 = MonoBehaviour__ctor();
    return MonoBehaviour__ctor();
}
```
