# Native pseudocode: ColorGradingCurve

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `ColorGradingCurve.ctor` — RVA `0xcde908`

- Decompiled symbol: `ColorGradingCurve_ctor`
- Metadata signature: `public void .ctor(AnimationCurve curve, float zeroValue, bool loop, Vector2 bounds) { }`
- Native interval: `180` bytes
- Result: `pseudocode`
- Heuristic layout hint: `ColorGradingCurve_Recovered` matched 4 offsets against `ColorGradingCurve` metadata (confidence 1.00).

```c
typedef struct struct_2 {
    char padding_0[224];
    unsigned int field_e0;
} struct_2;

typedef struct ColorGradingCurve_Recovered {
    char padding_0[16];
    long long curve;
    char m_Loop;
    char padding_19[3];
    unsigned int m_ZeroValue;
    unsigned int m_Range;
} ColorGradingCurve_Recovered;

typedef struct struct_1 {
    char padding_0[224];
    unsigned int field_e0;
} struct_1;

extern char g_1fab243;

struct_2 * ColorGradingCurve_ctor(struct_0 *ptr, long long a1, char a2)
{
    struct_0 *p;  // x21
    unsigned int v1;  // s0
    struct_1 *v2;  // x0

    Object__ctor();
    ptr->field_10 = a1;
    p = &ptr->field_10;
    sub_f7d8d0(p, a1);
    *((unsigned int *)&p->padding_0[12]) = v1;
    p->padding_0[8] = a2 & 1;
    if (!g_1fab243)
    {
        sub_f7d92c("_F");
        g_1fab243 = 1;
    }
    v2 = g_1ef07e8;
    if (!g_1ef07e8->field_e0)
        v2 = sub_f7da5c(g_1ef07e8);
    ptr->field_20 = [D] unsupported_Iop_SqrtF32();
    return v2;
}
```

## `ColorGradingCurve.Cache` — RVA `0xcde9bc`

- Decompiled symbol: `ColorGradingCurve_Cache`
- Metadata signature: `public void Cache() { }`
- Native interval: `484` bytes
- Result: `pseudocode`
- Heuristic layout hint: `ColorGradingCurve_Recovered` matched 3 offsets against `ColorGradingCurve` metadata (confidence 1.00).

```c
typedef struct ColorGradingCurve_Recovered {
    char padding_0[16];
    unsigned long long curve;
    char m_Loop;
    char padding_19[15];
    long long m_InternalLoopingCurve;
} ColorGradingCurve_Recovered;

extern char g_1fab623;

struct_0 * ColorGradingCurve_Cache(struct_0 *ptr)
{
    struct_0 *v18;  // x0
    struct_0 *v19;  // x0
    struct_0 *v20;  // x0
    long long v21;  // x0
    struct_0 *v22;  // x0
    struct_0 *p;  // x20
    long long v24;  // x22
    unsigned long long v25;  // x0
    char v0;  // [bp-0xf0]
    uint128_t v1;  // [bp-0xe4]
    char v2;  // [bp-0xd0]
    uint128_t v3;  // [bp-0xc4]
    char v4;  // [bp-0xb0]
    uint128_t v5;  // [bp-0xa4]
    char v6;  // [bp-0x90]
    uint128_t v7;  // [bp-0x84]
    char choice;  // [bp-0x70], Other Possible Types: unsigned long long
    unsigned long long flag6;  // [bp-0x68]
    uint128_t v10;  // [bp-0x64]
    unsigned long long flag7;  // [bp-0x60]
    unsigned int flag2;  // [bp-0x58]
    char flag3;  // [bp-0x50], Other Possible Types: unsigned long long
    unsigned long long flag4;  // [bp-0x48]
    uint128_t v15;  // [bp-0x44]
    unsigned long long flag5;  // [bp-0x40]
    unsigned int flag;  // [bp-0x38]

    v18 = ptr;
    if (!(g_1fab623 & 1))
    {
        v19 = sub_f7d92c("W,");
        g_1fab623 = 1;
        v18 = v19;
    }
    v20 = v18;
    flag3 = 0;
    flag4 = 0;
    flag = 0;
    flag5 = 0;
    choice = 0;
    flag6 = 0;
    flag2 = 0;
    flag7 = 0;
    if (!ptr->field_18)
        return v20;
    v21 = ptr->field_10;
    if (v21)
    {
        v22 = AnimationCurve__get_length(v21, 0);
        if ((unsigned int)v22 < 2)
            return v22;
        p = &ptr->field_28;
        if (!ptr->field_28)
        {
            v24 = sub_f7db70(g_1eee7c8);
            AnimationCurve__ctor(v24, 0);
            *((long long *)&p->padding_0[0]) = v24;
            sub_f7d8d0(p, v24);
        }
        v21 = ptr->field_10;
        if (v21)
        {
            AnimationCurve__get_Item(v21, (unsigned int)v22 - 1, 0);
            memcpy(&flag3, &v6, 16);
            v15 = v7;
            Keyframe__get_time(&flag3, 0);
            Keyframe__set_time(&flag3, 0);
            v21 = ptr->field_10;
            if (v21)
            {
                AnimationCurve__get_Item(v21, 0, 0);
                memcpy(&choice, &v6, 16);
                v10 = v7;
                Keyframe__get_time(&choice, 0);
                Keyframe__set_time(&choice, 0);
                v21 = ptr->field_10;
                if (v21)
                {
                    v21 = AnimationCurve__get_keys(v21, 0);
                    if (ptr->field_28)
                    {
                        AnimationCurve__set_keys(ptr->field_28, v21, 0);
                        v21 = *((long long *)&p->padding_0[0]);
                        memcpy(&v6, &flag3, 16);
                        v7 = v15;
                        if (v21)
                        {
                            memcpy(&v4, &v6, 16);
                            v5 = v7;
                            AnimationCurve__AddKey(v21, &v4, 0);
                            v21 = *((long long *)&p->padding_0[0]);
                            memcpy(&v2, &choice, 16);
                            v3 = v10;
                            if (v21)
                            {
                                memcpy(&v0, &v2, 16);
                                v1 = v3;
                                v25 = AnimationCurve__AddKey(v21, &v0, 0);
                                return AnimationCurve__AddKey(v21, &v0, 0);
                            }
                        }
                    }
                }
            }
        }
    }
    sub_f7db74(v21);
}
```

## `ColorGradingCurve.Evaluate` — RVA `0xcdeba0`

- Decompiled symbol: `ColorGradingCurve_Evaluate`
- Metadata signature: `public float Evaluate(float t) { }`
- Native interval: `124` bytes
- Result: `pseudocode`
- Heuristic layout hint: `ColorGradingCurve_Recovered` matched 3 offsets against `ColorGradingCurve` metadata (confidence 1.00).

```c
typedef struct ColorGradingCurve_Recovered {
    char padding_0[16];
    unsigned long long curve;
    char m_Loop;
    char padding_19[15];
    unsigned long long m_InternalLoopingCurve;
} ColorGradingCurve_Recovered;

unsigned long long ColorGradingCurve_Evaluate(struct_0 *ptr)
{
    unsigned long long v0;  // x0
    unsigned long long v1;  // x0
    unsigned long long v2;  // x0

    v0 = ptr->field_10;
    if (v0)
    {
        v1 = AnimationCurve__get_length(v0, 0);
        if (!(unsigned int)v1)
            return v1;
        if (ptr->field_18)
        {
            v0 = ptr->field_10;
            if (v0)
            {
                if (AnimationCurve__get_length(v0, 0) == 1)
                    goto LABEL_10debe4;
                v0 = ptr->field_28;
                if (ptr->field_28)
                {
                    v2 = AnimationCurve__Evaluate();
                    return AnimationCurve__Evaluate();
                }
            }
        }
        else
        {
LABEL_10debe4:
            v0 = ptr->field_10;
            if (ptr->field_10)
            {
                v2 = AnimationCurve__Evaluate();
                return AnimationCurve__Evaluate();
            }
        }
    }
    sub_f7db74(v0);
}
```
