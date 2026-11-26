# Native pseudocode: DoorOpen

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `DoorOpen.OnTriggerEnter` — RVA `0xcbfc88`

- Decompiled symbol: `DoorOpen_OnTriggerEnter`
- Metadata signature: `private void OnTriggerEnter(Collider col) { }`
- Native interval: `172` bytes
- Result: `pseudocode`

```c
extern long long g_1efcf08;
extern long long g_1f0cf98;
extern char g_1fab4fb;

void DoorOpen_OnTriggerEnter(long long a0, long long a1)
{
    long long v0;  // x0

    if (!(g_1fab4fb & 1))
    {
        sub_f7d92c(&g_1efcf08);
        sub_f7d92c(&g_1f0cf98);
        g_1fab4fb = 1;
    }
    if (a1 && Component__get_gameObject(a1, 0))
    {
        v0 = GameObject__get_tag();
        if (!((char)String__op_Equality(v0, g_1f0cf98, 0) & 1))
        {
            return;
        }
        else if (sub_1231bc8(a0, g_1efcf08))
        {
            Behaviour__set_enabled();
            return;
        }
    }
    sub_f7db74();
}
```

## `DoorOpen.ctor` — RVA `0xcbfd34`

- Decompiled symbol: `DoorOpen_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long DoorOpen_ctor(void)
{
    long long v0;  // x0

    v0 = MonoBehaviour__ctor();
    return MonoBehaviour__ctor();
}
```
