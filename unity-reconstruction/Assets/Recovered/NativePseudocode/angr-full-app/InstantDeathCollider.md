# Native pseudocode: InstantDeathCollider

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `InstantDeathCollider.OnTriggerEnter` — RVA `0xc99b34`

- Decompiled symbol: `InstantDeathCollider_OnTriggerEnter`
- Metadata signature: `private void OnTriggerEnter(Collider col) { }`
- Native interval: `336` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[535];
    char field_217;
} struct_1;

typedef struct struct_2 {
    char padding_0[32];
    char field_20;
} struct_2;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern long long g_1efcf98;
extern long long g_1efd080;
extern long long g_1f0cf98;
extern char g_1fab49b;

long long InstantDeathCollider_OnTriggerEnter(struct_2 *a0, long long a1)
{
    long long v0;  // x0
    struct_1 *ptr;  // x0
    long long v2;  // x0
    long long v3;  // x0
    long long v4;  // x0
    long long v5;  // x0

    if (!(g_1fab49b & 1))
    {
        sub_f7d92c(&g_1efcf98);
        sub_f7d92c(&g_1efd080);
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c(&g_1f0cf98);
        g_1fab49b = 1;
    }
    if (a1 && Component__get_gameObject(a1, 0))
    {
        v0 = GameObject__get_tag();
        if (((char)String__op_Equality(v0, g_1f0cf98, 0) & 1))
        {
            ptr = sub_1231bc8(a1, g_1efcf98);
            if (a0->field_20)
            {
                if (ptr)
                {
                    ptr->field_217 = 0;
                    v2 = FPSPlayer__ApplyDamage();
                    return FPSPlayer__ApplyDamage();
                }
            }
            else
            {
                if (ptr)
                {
                    v2 = FPSPlayer__ApplyDamage();
                    return FPSPlayer__ApplyDamage();
                }
            }
        }
        else
        {
            v3 = sub_1231bc8(a1, g_1efd080);
            if (!g_1ef0c58->field_e0)
                sub_f7da5c(g_1ef0c58);
            v4 = Object__op_Implicit(v3, 0);
            if (!((char)v4 & 1))
            {
                return v4;
            }
            else if (Component__get_gameObject(a1, 0))
            {
                v5 = GameObject__SetActive();
                return GameObject__SetActive();
            }
        }
    }
    sub_f7db74();
}
```

## `InstantDeathCollider.Reset` — RVA `0xc99c84`

- Decompiled symbol: `InstantDeathCollider_Reset`
- Metadata signature: `private void Reset() { }`
- Native interval: `236` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern long long g_1efcf70;
extern long long g_1efea88;
extern char g_1fab49c;

long long InstantDeathCollider_Reset(long long a0)
{
    long long v0;  // x0
    long long v1;  // x0
    unsigned long long v2;  // x0

    if (!(g_1fab49c & 1))
    {
        sub_f7d92c(&g_1efcf70);
        sub_f7d92c(&g_1efea88);
        sub_f7d92c(&g_1ef0c58);
        g_1fab49c = 1;
    }
    v0 = sub_1231bc8(a0, g_1efcf70);
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v1 = Object__op_Equality(v0, 0, 0);
    if (!((char)v1 & 1))
        return v1;
    if (Component__get_gameObject(a0, 0))
    {
        sub_124913c();
        if (sub_1231bc8(a0, g_1efcf70))
        {
            v2 = Collider__set_isTrigger();
            return Collider__set_isTrigger();
        }
    }
    sub_f7db74();
}
```

## `InstantDeathCollider.ctor` — RVA `0xc99d70`

- Decompiled symbol: `InstantDeathCollider_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `16` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[32];
    char field_20;
} struct_0;

long long InstantDeathCollider_ctor(struct_0 *ptr)
{
    long long v0;  // x0

    ptr->field_20 = 1;
    v0 = MonoBehaviour__ctor();
    return MonoBehaviour__ctor();
}
```
