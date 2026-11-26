# Native pseudocode: bl_SceneLoader.OnLoaded

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `bl_SceneLoader.OnLoaded.ctor` — RVA `0xc77d78`

- Decompiled symbol: `bl_SceneLoader_OnLoaded_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long bl_SceneLoader_OnLoaded_ctor(void)
{
    unsigned long long v0;  // x0

    v0 = UnityEvent__ctor();
    return UnityEvent__ctor();
}
```
