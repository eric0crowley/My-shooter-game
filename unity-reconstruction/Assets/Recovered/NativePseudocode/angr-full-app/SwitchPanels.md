# Native pseudocode: SwitchPanels

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `SwitchPanels.Awake` — RVA `0xccb698`

- Decompiled symbol: `SwitchPanels_Awake`
- Metadata signature: `private void Awake() { }`
- Native interval: `192` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[280];
    unsigned long long field_118;
} struct_0;

extern long long g_1eedda0;
extern long long g_1efb280;
extern long long g_1efd0b8;
extern long long g_1f01dc8;
extern char g_1fab58a;

void SwitchPanels_Awake(long long a0)
{
    unsigned long long v4;  // x30
    unsigned long long v5;  // x21
    unsigned long long v6;  // x20
    unsigned long long v7;  // x19
    long long v9;  // x0
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x18]
    unsigned long long v2;  // [bp-0x10]
    unsigned long long v3;  // [bp-0x8]

    v0 = v4;
    v1 = v5;
    v2 = v6;
    v3 = v7;
    if (!(g_1fab58a & 1))
    {
        sub_f7d92c(&g_1efd0b8);
        sub_f7d92c(&g_1f01dc8);
        sub_f7d92c(&g_1eedda0);
        sub_f7d92c(&g_1efb280);
        g_1fab58a = 1;
    }
    if (sub_1231bc8(a0, g_1efd0b8))
    {
        v9 = sub_f7db70(g_1eedda0);
        sub_1637f10(v9, a0, g_1f01dc8, 0);
    }
    sub_f7db74();
}
```

## `SwitchPanels.OnToggleClick` — RVA `0xccb758`

- Decompiled symbol: `SwitchPanels_OnToggleClick`
- Metadata signature: `public void OnToggleClick(bool isActive) { }`
- Native interval: `72` bytes
- Result: `pseudocode`

```c
void SwitchPanels_OnToggleClick(long long *ptr, unsigned int a1)
{
    unsigned long long v3;  // x30
    unsigned long long v4;  // x20
    unsigned long long v5;  // x19
    long long v6;  // x0
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x10]
    unsigned long long v2;  // [bp-0x8]

    v0 = v3;
    v1 = v4;
    v2 = v5;
    v6 = ptr[4];
    if (v6)
    {
        GameObject__SetActive(v6, a1 & 1, 0);
        v6 = ptr[5];
        if (ptr[5])
        {
            GameObject__SetActive();
            return;
        }
    }
    sub_f7db74(v6);
}
```

## `SwitchPanels.ctor` — RVA `0xccb7a0`

- Decompiled symbol: `SwitchPanels_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long SwitchPanels_ctor(void)
{
    long long v0;  // x0

    v0 = MonoBehaviour__ctor();
    return MonoBehaviour__ctor();
}
```
