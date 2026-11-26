# Native pseudocode: Check_AI_Behaviour

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `Check_AI_Behaviour.Update` — RVA `0xc6d1fc`

- Decompiled symbol: `Check_AI_Behaviour_Update`
- Metadata signature: `private void Update() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long Check_AI_Behaviour_Update(unsigned long a0)
{
    unsigned long long v0;  // x0

    v0 = Check_AI_Behaviour__castRay();
    return Check_AI_Behaviour__castRay();
}
```

## `Check_AI_Behaviour.castRay` — RVA `0xc6d200`

- Decompiled symbol: `Check_AI_Behaviour_castRay`
- Metadata signature: `private void castRay() { }`
- Native interval: `508` bytes
- Result: `pseudocode`
- Heuristic layout hint: `Check_AI_Behaviour_Recovered` matched 4 offsets against `Check_AI_Behaviour` metadata (confidence 1.00).

```c
typedef struct Check_AI_Behaviour_Recovered {
    char padding_0[40];
    unsigned long long ai;
    unsigned long long ShootPoint;
    char padding_38[4];
    char showSpeed;
    char padding_3d[3];
    unsigned int RateOfMove_Time;
} Check_AI_Behaviour_Recovered;

typedef struct struct_1 {
    char padding_0[224];
    unsigned int field_e0;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1eef458;
extern struct_1 *g_1ef0e48;
extern long long g_1f08030;
extern char g_1fab347;

unsigned long long Check_AI_Behaviour_castRay(struct_2 *ptr)
{
    unsigned long v5;  // x0
    unsigned long long v6;  // x0
    unsigned int v7;  // s8
    unsigned long long v8;  // x0
    unsigned long v9;  // 4125
    unsigned long long v0;  // [bp-0x90]
    unsigned long long v1;  // [bp-0x88]
    int choice;  // [bp-0x80]
    uint128_t flag2;  // [bp-0x70]
    uint128_t flag;  // [bp-0x64]

    if (!(g_1fab347 & 1))
    {
        sub_f7d92c(&g_1eef458);
        sub_f7d92c(&g_1ef0e48);
        sub_f7d92c(&g_1f08030);
        g_1fab347 = 1;
    }
    flag = 0;
    choice = 0;
    flag2 = 0;
    v5 = ptr->field_30;
    if (v5)
    {
        v5 = Component__get_transform(v5, 0);
        if (v5)
        {
            Transform__get_position();
            v5 = Component__get_transform(ptr, 0);
            if (v5)
            {
                Transform__get_forward();
                if (!g_1eef458->field_e0)
                    sub_f7da5c(g_1eef458);
                v0 = 0x3f8000003f800000;
                v1 = 0x3f8000003f800000;
                Debug__DrawRay(0);
                if (ptr->field_3c)
                    MonoBehaviour__print(g_1f08030, 0);
                v5 = ptr->field_30;
                if (v5)
                {
                    v5 = Component__get_transform(v5, 0);
                    if (v5)
                    {
                        Transform__get_position();
                        v5 = Component__get_transform(ptr, 0);
                        if (v5)
                        {
                            Transform__get_forward();
                            if (!g_1ef0e48->field_e0)
                                sub_f7da5c(g_1ef0e48);
                            v6 = Physics__Raycast(&choice, 0);
                            if (!((char)v6 & 1))
                                return v6;
                            v7 = ptr->field_40;
                            v8 = Time__get_time(0);
                            v9 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v7, 0)) >> 5 & 3 | (unsigned long long)(CmpF(v7, 0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v7, 0)) >> 5 & 3 | (unsigned long long)(CmpF(v7, 0) & 1)) & ((unsigned long long)(char)(CmpF(v7, 0)) >> 5 & 3 | (unsigned long long)(CmpF(v7, 0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                            if ((char)v9)
                                return v8;
                            v5 = ptr->field_28;
                            if (v5)
                                my_AI__ChangePosition(); /* do not return */
                        }
                    }
                }
            }
        }
    }
    sub_f7db74(v5);
}
```

## `Check_AI_Behaviour.ctor` — RVA `0xc6d440`

- Decompiled symbol: `Check_AI_Behaviour_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long Check_AI_Behaviour_ctor(void)
{
}
```
