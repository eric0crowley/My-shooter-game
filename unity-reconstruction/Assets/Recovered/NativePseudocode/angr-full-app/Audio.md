# Native pseudocode: Audio

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `Audio.Start` — RVA `0xcbfa18`

- Decompiled symbol: `Audio_Start`
- Metadata signature: `private void Start() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long Audio_Start(void)
{
    unsigned long v0;  // x0

    return v0;
}
```

## `Audio.Update` — RVA `0xcbfa1c`

- Decompiled symbol: `Audio_Update`
- Metadata signature: `private void Update() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long Audio_Update(void)
{
    unsigned long v0;  // x0

    return v0;
}
```

## `Audio.AudioClipFunc` — RVA `0xcbfa20`

- Decompiled symbol: `Audio_AudioClipFunc`
- Metadata signature: `public void AudioClipFunc() { }`
- Native interval: `92` bytes
- Result: `pseudocode`

```c
extern long long g_1efcf18;
extern char g_1fab4f8;

void Audio_AudioClipFunc(long long a0)
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
    if (!(g_1fab4f8 & 1))
    {
        sub_f7d92c(&g_1efcf18);
        g_1fab4f8 = 1;
    }
    if (sub_1231bc8(a0, g_1efcf18))
    {
        AudioSource__PlayOneShot();
        return;
    }
    sub_f7db74();
}
```

## `Audio.ctor` — RVA `0xcbfa7c`

- Decompiled symbol: `Audio_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long Audio_ctor(void)
{
    long long v0;  // x0

    v0 = MonoBehaviour__ctor();
    return MonoBehaviour__ctor();
}
```
