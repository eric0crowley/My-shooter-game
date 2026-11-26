# Native pseudocode: bl_TriggerLoad

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `bl_TriggerLoad.OnTriggerEnter` — RVA `0xceb828`

- Decompiled symbol: `bl_TriggerLoad_OnTriggerEnter`
- Metadata signature: `private void OnTriggerEnter(Collider other) { }`
- Native interval: `40` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[32];
    unsigned int field_20;
} struct_0;

long long bl_TriggerLoad_OnTriggerEnter(struct_0 *a0)
{
    unsigned long v0;  // x0
    long long v1;  // x0

    v0 = bl_SceneLoaderUtils__get_GetLoader();
    if (v0)
    {
        v1 = bl_SceneLoader__LoadLevel(v0, *((long long *)&a0->field_20));
        return bl_SceneLoader__LoadLevel(v0, *((long long *)&a0->field_20));
    }
    sub_f7db74();
}
```

## `bl_TriggerLoad.ctor` — RVA `0xceb850`

- Decompiled symbol: `bl_TriggerLoad_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long bl_TriggerLoad_ctor(void)
{
    long long v0;  // x0

    v0 = MonoBehaviour__ctor();
    return MonoBehaviour__ctor();
}
```
