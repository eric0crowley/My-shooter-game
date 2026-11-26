# Native pseudocode: EdgeClimbTriggerActivate

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `EdgeClimbTriggerActivate.OnTriggerEnter` — RVA `0xc95404`

- Decompiled symbol: `EdgeClimbTriggerActivate_OnTriggerEnter`
- Metadata signature: `private void OnTriggerEnter(Collider other) { }`
- Native interval: `32` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[32];
    unsigned long long field_20;
} struct_0;

void EdgeClimbTriggerActivate_OnTriggerEnter(struct_0 *a0)
{
    unsigned long long v1;  // x30
    unsigned long long v0;  // [bp-0x10]

    v0 = v1;
    if (a0->field_20)
    {
        Collider__set_enabled();
        return;
    }
    sub_f7db74(0);
}
```

## `EdgeClimbTriggerActivate.ctor` — RVA `0xc95424`

- Decompiled symbol: `EdgeClimbTriggerActivate_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long EdgeClimbTriggerActivate_ctor(void)
{
    long long v0;  // x0

    v0 = MonoBehaviour__ctor();
    return MonoBehaviour__ctor();
}
```
