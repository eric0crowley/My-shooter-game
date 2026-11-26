# Native pseudocode: SpriteRotator

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `SpriteRotator.Start` — RVA `0xcc47e8`

- Decompiled symbol: `SpriteRotator_Start`
- Metadata signature: `private void Start() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long SpriteRotator_Start(void)
{
    unsigned long v0;  // x0

    return v0;
}
```

## `SpriteRotator.Update` — RVA `0xcc47ec`

- Decompiled symbol: `SpriteRotator_Update`
- Metadata signature: `private void Update() { }`
- Native interval: `124` bytes
- Result: `pseudocode`

```c
extern long long g_1ef22e8;
extern char g_1fab591;

void SpriteRotator_Update(unsigned long a0)
{
    unsigned long long v4;  // x30
    unsigned long long v5;  // x21
    unsigned long long v6;  // x20
    unsigned long long v7;  // x19
    long long v8;  // x0
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x18]
    unsigned long long v2;  // [bp-0x10]
    unsigned long long v3;  // [bp-0x8]

    v0 = v4;
    v1 = v5;
    v2 = v6;
    v3 = v7;
    v8 = Component__get_transform();
    if (!g_1fab591)
    {
        sub_f7d92c(&g_1ef22e8);
        g_1fab591 = 1;
    }
    if (!v8)
        sub_f7db74();
}
```

## `SpriteRotator.ctor` — RVA `0xcc4868`

- Decompiled symbol: `SpriteRotator_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long SpriteRotator_ctor(void)
{
    long long v0;  // x0

    v0 = MonoBehaviour__ctor();
    return MonoBehaviour__ctor();
}
```
