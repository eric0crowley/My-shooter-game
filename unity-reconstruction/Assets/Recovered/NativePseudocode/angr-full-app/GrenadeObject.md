# Native pseudocode: GrenadeObject

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `GrenadeObject.Start` — RVA `0xcae314`

- Decompiled symbol: `GrenadeObject_Start`
- Metadata signature: `private void Start() { }`
- Native interval: `88` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[40];
    long long field_28;
} struct_0;

extern long long g_1efcf90;
extern char g_1fab4cb;

void GrenadeObject_Start(struct_0 *ptr)
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
    if (!(g_1fab4cb & 1))
    {
        sub_f7d92c(&g_1efcf90);
        g_1fab4cb = 1;
    }
    ptr->field_28 = sub_1231bc8(ptr, g_1efcf90);
    sub_f7d8d0();
    return;
}
```

## `GrenadeObject.OnEnable` — RVA `0xcae36c`

- Decompiled symbol: `GrenadeObject_OnEnable`
- Metadata signature: `private void OnEnable() { }`
- Native interval: `28` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[36];
    unsigned int field_24;
} struct_0;

int GrenadeObject_OnEnable(struct_0 *ptr)
{
    unsigned int v0;  // w0
    unsigned int v1;  // s0

    v0 = Time__get_time(0);
    ptr->field_24 = v1;
    return v0;
}
```

## `GrenadeObject.Update` — RVA `0xcae388`

- Decompiled symbol: `GrenadeObject_Update`
- Metadata signature: `private void Update() { }`
- Native interval: `88` bytes
- Result: `pseudocode`
- Heuristic layout hint: `GrenadeObject_Recovered` matched 3 offsets against `GrenadeObject` metadata (confidence 1.00).

```c
typedef struct GrenadeObject_Recovered {
    char padding_0[32];
    unsigned int fuseTimeAmt;
    unsigned int startTime;
    unsigned long long ExplosiveObjectComponent;
} GrenadeObject_Recovered;

int GrenadeObject_Update(struct_0 *ptr)
{
    unsigned int v0;  // w0
    unsigned int v1;  // s1
    unsigned int v2;  // s0
    unsigned long v3;  // 4138

    v0 = Time__get_time(0);
    v1 = ptr->field_24 + ptr->field_20;
    v3 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v1, v2)) >> 5 & 3 | (unsigned long long)(CmpF(v1, v2) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v1, v2)) >> 5 & 3 | (unsigned long long)(CmpF(v1, v2) & 1)) & ((unsigned long long)(char)(CmpF(v1, v2)) >> 5 & 3 | (unsigned long long)(CmpF(v1, v2) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if ((char)v3)
        return v0;
    if (ptr->field_28)
        return ExplosiveObject__ApplyDamage();
    sub_f7db74(0);
}
```

## `GrenadeObject.ctor` — RVA `0xcae3e0`

- Decompiled symbol: `GrenadeObject_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long GrenadeObject_ctor(void)
{
}
```
