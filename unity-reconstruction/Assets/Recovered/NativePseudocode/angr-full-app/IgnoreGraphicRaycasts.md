# Native pseudocode: IgnoreGraphicRaycasts

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `IgnoreGraphicRaycasts.IsRaycastLocationValid` — RVA `0xc5a644`

- Decompiled symbol: `IgnoreGraphicRaycasts_IsRaycastLocationValid`
- Metadata signature: `private bool UnityEngine.ICanvasRaycastFilter.IsRaycastLocationValid(Vector2 sp, Camera eventCamera) { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
unsigned int IgnoreGraphicRaycasts_IsRaycastLocationValid(void)
{
    return 0;
}
```

## `IgnoreGraphicRaycasts.ctor` — RVA `0xc5a64c`

- Decompiled symbol: `IgnoreGraphicRaycasts_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long IgnoreGraphicRaycasts_ctor(void)
{
    long long v0;  // x0

    v0 = MonoBehaviour__ctor();
    return MonoBehaviour__ctor();
}
```
