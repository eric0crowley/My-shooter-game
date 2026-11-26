# Native pseudocode: AppleFall

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `AppleFall.Start` — RVA `0xc93310`

- Decompiled symbol: `AppleFall_Start`
- Metadata signature: `private void Start() { }`
- Native interval: `36` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[32];
    long long field_20;
} struct_0;

void AppleFall_Start(struct_0 *ptr)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    ptr->field_20 = Component__get_transform();
    sub_f7d8d0();
    return;
}
```

## `AppleFall.ApplyDamage` — RVA `0xc93334`

- Decompiled symbol: `AppleFall_ApplyDamage`
- Metadata signature: `public void ApplyDamage(float damage) { }`
- Native interval: `280` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[32];
    unsigned long long field_20;
} struct_0;

extern long long g_1efcf18;
extern long long g_1efd080;
extern char g_1fab460;

void AppleFall_ApplyDamage(struct_0 *ptr)
{
    unsigned long long v0;  // x0
    long long v1;  // x20

    if (!(g_1fab460 & 1))
    {
        sub_f7d92c(&g_1efcf18);
        sub_f7d92c(&g_1efd080);
        g_1fab460 = 1;
    }
    v0 = ptr->field_20;
    if (v0)
    {
        v0 = sub_1231bc8(v0, g_1efd080);
        if (v0)
        {
            if (((char)Rigidbody__get_useGravity() & 1))
                return;
            v1 = sub_1231bc8(ptr, g_1efcf18);
            Time__get_timeScale(0);
            Time__get_timeScale(0);
            v0 = Random__Range(0);
            if (v1)
            {
                AudioSource__set_pitch(v1, 0);
                v0 = sub_1231bc8(ptr, g_1efcf18);
                if (v0)
                {
                    AudioSource__Play();
                    v0 = ptr->field_20;
                    if (v0)
                    {
                        v0 = sub_1231bc8(v0, g_1efd080);
                        if (v0)
                        {
                            Rigidbody__set_useGravity();
                            return;
                        }
                    }
                }
            }
        }
    }
    sub_f7db74(v0);
}
```

## `AppleFall.OnCollisionEnter` — RVA `0xc9344c`

- Decompiled symbol: `AppleFall_OnCollisionEnter`
- Metadata signature: `public void OnCollisionEnter() { }`
- Native interval: `280` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[32];
    unsigned long long field_20;
} struct_0;

extern long long g_1efcf18;
extern long long g_1efd080;
extern char g_1fab461;

void AppleFall_OnCollisionEnter(struct_0 *ptr)
{
    unsigned long long v0;  // x0
    long long v1;  // x20

    if (!(g_1fab461 & 1))
    {
        sub_f7d92c(&g_1efcf18);
        sub_f7d92c(&g_1efd080);
        g_1fab461 = 1;
    }
    v0 = ptr->field_20;
    if (v0)
    {
        v0 = sub_1231bc8(v0, g_1efd080);
        if (v0)
        {
            if (((char)Rigidbody__get_useGravity() & 1))
                return;
            v1 = sub_1231bc8(ptr, g_1efcf18);
            Time__get_timeScale(0);
            Time__get_timeScale(0);
            v0 = Random__Range(0);
            if (v1)
            {
                AudioSource__set_pitch(v1, 0);
                v0 = sub_1231bc8(ptr, g_1efcf18);
                if (v0)
                {
                    AudioSource__Play();
                    v0 = ptr->field_20;
                    if (v0)
                    {
                        v0 = sub_1231bc8(v0, g_1efd080);
                        if (v0)
                        {
                            Rigidbody__set_useGravity();
                            return;
                        }
                    }
                }
            }
        }
    }
    sub_f7db74(v0);
}
```

## `AppleFall.ctor` — RVA `0xc93564`

- Decompiled symbol: `AppleFall_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long AppleFall_ctor(void)
{
    long long v0;  // x0

    v0 = MonoBehaviour__ctor();
    return MonoBehaviour__ctor();
}
```
