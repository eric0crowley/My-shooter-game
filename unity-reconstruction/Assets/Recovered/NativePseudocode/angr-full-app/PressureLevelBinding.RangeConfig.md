# Native pseudocode: PressureLevelBinding.RangeConfig

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `PressureLevelBinding.RangeConfig.ctor` — RVA `0xc68804`

- Decompiled symbol: `PressureLevelBinding_RangeConfig_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `108` bytes
- Result: `pseudocode`
- Heuristic layout hint: `PressureLevelBinding_RangeConfig_Recovered` matched 3 offsets against `PressureLevelBinding.RangeConfig` metadata (confidence 1.00).

```c
typedef struct PressureLevelBinding_RangeConfig_Recovered {
    char padding_0[16];
    unsigned long long min;
    char padding_18[8];
    long long axisTarget;
    char positiveAxisSide;
} PressureLevelBinding_RangeConfig_Recovered;

extern long long g_1f06220;
extern char g_1fab320;

void PressureLevelBinding_RangeConfig_ctor(struct_0 *ptr)
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
    if (!(g_1fab320 & 1))
    {
        sub_f7d92c(&g_1f06220);
        g_1fab320 = 1;
    }
    ptr->field_10 = 0x3f8000003f000000;
    ptr->field_20 = g_1f06220;
    sub_f7d8d0((struct PressureLevelBinding_RangeConfig_Recovered *)&ptr->field_20, g_1f06220);
    ptr->field_28 = 1;
    Object__ctor();
    return;
}
```

## `PressureLevelBinding.RangeConfig.Update` — RVA `0xc68b78`

- Decompiled symbol: `PressureLevelBinding_RangeConfig_Update`
- Metadata signature: `public void Update(InputRig rig, float val) { }`
- Native interval: `140` bytes
- Result: `pseudocode`
- Heuristic layout hint: `PressureLevelBinding_RangeConfig_Recovered` matched 5 offsets against `PressureLevelBinding.RangeConfig` metadata (confidence 1.00).

```c
typedef struct PressureLevelBinding_RangeConfig_Recovered {
    char padding_0[16];
    unsigned int min;
    unsigned int max;
    unsigned int keyTarget;
    char padding_1c[4];
    long long axisTarget;
    char positiveAxisSide;
} PressureLevelBinding_RangeConfig_Recovered;

struct_0 * PressureLevelBinding_RangeConfig_Update(struct_0 *ptr, long long a1)
{
    unsigned int v0;  // s1
    unsigned int v1;  // s0
    unsigned long v2;  // 4142
    unsigned int v3;  // s1
    unsigned long v4;  // 4133
    struct_0 *v5;  // x0

    v0 = ptr->field_10;
    v2 = arm64g_calculate_condition(192, (((((unsigned long long)(char)(CmpF(v0, v1)) >> 5 & 3 | (unsigned long long)(CmpF(v0, v1) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v0, v1)) >> 5 & 3 | (unsigned long long)(CmpF(v0, v1) & 1)) & ((unsigned long long)(char)(CmpF(v0, v1)) >> 5 & 3 | (unsigned long long)(CmpF(v0, v1) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if ((char)v2)
        return ptr;
    v3 = ptr->field_14;
    v4 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(v3, v1)) >> 5 & 3 | (unsigned long long)(CmpF(v3, v1) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v3, v1)) >> 5 & 3 | (unsigned long long)(CmpF(v3, v1) & 1)) & ((unsigned long long)(char)(CmpF(v3, v1)) >> 5 & 3 | (unsigned long long)(CmpF(v3, v1) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if ((char)v4)
        return ptr;
    if (ptr->field_18)
    {
        if (a1)
            InputRig__SetKeyCode(a1);
        else
            sub_f7db74();
    }
    v5 = String__IsNullOrEmpty(ptr->field_20, 0);
    if (((char)v5 & 1))
    {
        return v5;
    }
    else if (!a1)
    {
        sub_f7db74();
    }
}
```
