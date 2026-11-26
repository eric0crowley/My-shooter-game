# Native pseudocode: Displace

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `Displace.Awake` — RVA `0xce1d28`

- Decompiled symbol: `Displace_Awake`
- Metadata signature: `public void Awake() { }`
- Native interval: `32` bytes
- Result: `pseudocode`

```c
void Displace_Awake(void)
{
    if (!((char)Behaviour__get_enabled() & 1))
        Displace__OnDisable(); /* do not return */
    Displace__OnEnable(); /* do not return */
}
```

## `Displace.OnEnable` — RVA `0xce1d48`

- Decompiled symbol: `Displace_OnEnable`
- Metadata signature: `public void OnEnable() { }`
- Native interval: `100` bytes
- Result: `pseudocode`

```c
extern char g_1fab640;

void Displace_OnEnable(void)
{
    unsigned long long v4;  // x30
    unsigned long long v5;  // x21
    unsigned long long v6;  // x20
    unsigned long long v7;  // x19
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x18]
    unsigned long long v2;  // [bp-0x10]
    unsigned long long v3;  // [bp-0x8]

    v0 = v4;
    v1 = v5;
    v2 = v6;
    v3 = v7;
    if (!(g_1fab640 & 1))
    {
        sub_f7d92c("A&");
        sub_f7d92c("C&");
        g_1fab640 = 1;
    }
    Shader__EnableKeyword(g_1f0faf8, 0);
    Shader__DisableKeyword();
    return;
}
```

## `Displace.OnDisable` — RVA `0xce1dac`

- Decompiled symbol: `Displace_OnDisable`
- Metadata signature: `public void OnDisable() { }`
- Native interval: `100` bytes
- Result: `pseudocode`

```c
extern char g_1fab641;

void Displace_OnDisable(void)
{
    unsigned long long v4;  // x30
    unsigned long long v5;  // x21
    unsigned long long v6;  // x20
    unsigned long long v7;  // x19
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x18]
    unsigned long long v2;  // [bp-0x10]
    unsigned long long v3;  // [bp-0x8]

    v0 = v4;
    v1 = v5;
    v2 = v6;
    v3 = v7;
    if (!(g_1fab641 & 1))
    {
        sub_f7d92c("A&");
        sub_f7d92c("C&");
        g_1fab641 = 1;
    }
    Shader__EnableKeyword(g_1f0faf0, 0);
    Shader__DisableKeyword();
    return;
}
```

## `Displace.ctor` — RVA `0xce1e10`

- Decompiled symbol: `Displace_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long Displace_ctor(void)
{
    long long v0;  // x0

    v0 = MonoBehaviour__ctor();
    return MonoBehaviour__ctor();
}
```
