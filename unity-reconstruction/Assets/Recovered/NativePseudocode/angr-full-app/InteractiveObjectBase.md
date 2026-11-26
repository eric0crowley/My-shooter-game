# Native pseudocode: InteractiveObjectBase

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `InteractiveObjectBase.IsNear` — RVA `0xc66138`

- Decompiled symbol: `InteractiveObjectBase_IsNear`
- Metadata signature: `public virtual bool IsNear(CharacterAction chara) { }`
- Native interval: `148` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[32];
    unsigned int field_20;
} struct_0;

unsigned int InteractiveObjectBase_IsNear(struct_0 *ptr, long long a1)
{
    unsigned long long v1;  // d10
    unsigned int v2;  // s2
    unsigned int v3;  // s2
    unsigned int v4;  // s0
    unsigned int v5;  // s0
    unsigned int v6;  // s1
    unsigned int v7;  // s1
    unsigned int v8;  // s0
    unsigned int v9;  // s1
    unsigned long v10;  // 4265
    unsigned long long v0;  // [bp-0x30]

    v0 = v1;
    if (a1 && Component__get_transform(a1, 0))
    {
        Transform__get_position();
        if (Component__get_transform(ptr, 0))
        {
            Transform__get_position();
            v3 = v2 - v2;
            v5 = (v4 - v4) * (v4 - v4);
            v7 = (v6 - v6) * (v6 - v6);
            v8 = (v2 - v2) * (v2 - v2) + (v4 - v4) * (v4 - v4) + (v6 - v6) * (v6 - v6);
            v9 = ptr->field_20 * ptr->field_20;
            v10 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v8, v9)) >> 5 & 3 | (unsigned long long)(CmpF(v3 * v3 + v5 + v7, v9) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF((v2 - v2) * (v2 - v2) + (v4 - v4) * (v4 - v4) + (v6 - v6) * (v6 - v6), v9)) >> 5 & 3 | (unsigned long long)(CmpF((v2 - v2) * (v2 - v2) + (v4 - v4) * (v4 - v4) + (v6 - v6) * (v6 - v6), v9) & 1)) & ((unsigned long long)(char)(CmpF((v2 - v2) * (v2 - v2) + v5 + v7, v9)) >> 5 & 3 | (unsigned long long)(CmpF((v2 - v2) * (v2 - v2) + (v4 - v4) * (v4 - v4) + (v6 - v6) * (v6 - v6), v9) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
            if (!((char)v10))
                return 1;
            return 0;
        }
    }
    sub_f7db74();
}
```

## `InteractiveObjectBase.OnDrawGizmos` — RVA `0xc661cc`

- Decompiled symbol: `InteractiveObjectBase_OnDrawGizmos`
- Metadata signature: `private void OnDrawGizmos() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long InteractiveObjectBase_OnDrawGizmos(unsigned long a0)
{
    unsigned long long v0;  // x0

    v0 = InteractiveObjectBase__DrawDefaultGizmo();
    return InteractiveObjectBase__DrawDefaultGizmo();
}
```

## `InteractiveObjectBase.DrawDefaultGizmo` — RVA `0xc661d0`

- Decompiled symbol: `InteractiveObjectBase_DrawDefaultGizmo`
- Metadata signature: `protected void DrawDefaultGizmo() { }`
- Native interval: `148` bytes
- Result: `pseudocode`

```c
extern char g_1fab32b;

int InteractiveObjectBase_DrawDefaultGizmo(long long a0)
{
    uint128_t ptr[8];  // x8
    int v0;  // [bp-0x60]
    int v1;  // [bp-0x50]
    int v2;  // [bp-0x40]
    int v3;  // [bp-0x30]

    if (!g_1fab32b)
    {
        sub_f7d92c("eF");
        g_1fab32b = 1;
    }
    ptr = g_1ef0800->field_b8;
    v2 = (int)ptr[6];
    v3 = (int)ptr[7];
    v0 = (int)ptr[4];
    v1 = (int)ptr[5];
    Gizmos__set_matrix(&v0, 0);
    if (Component__get_transform(a0, 0))
    {
        Transform__get_position();
        return Gizmos__DrawWireSphere(0);
    }
    sub_f7db74();
}
```

## `InteractiveObjectBase.ctor` — RVA `0xc66264`

- Decompiled symbol: `InteractiveObjectBase_ctor`
- Metadata signature: `protected void .ctor() { }`
- Native interval: `16` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[32];
    unsigned int field_20;
} struct_0;

long long InteractiveObjectBase_ctor(struct_0 *ptr)
{
    unsigned long long v0;  // x0

    ptr->field_20 = 0x40000000;
    v0 = MonoBehaviour__ctor();
    return MonoBehaviour__ctor();
}
```
