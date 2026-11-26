# Native pseudocode: DamageZone

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `DamageZone.Start` — RVA `0xc99530`

- Decompiled symbol: `DamageZone_Start`
- Metadata signature: `private void Start() { }`
- Native interval: `140` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[40];
    long long field_28;
} struct_0;

typedef struct struct_1 {
    char padding_0[48];
    long long field_30;
} struct_1;

extern long long g_1efcf38;
extern long long g_1efebb8;
extern char g_1fab498;

void DamageZone_Start(struct_1 *ptr, unsigned long a1)
{
    unsigned long long v3;  // x30
    unsigned long long v4;  // x20
    unsigned long long v5;  // x19
    struct_0 *v6;  // x0
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x10]
    unsigned long long v2;  // [bp-0x8]

    v0 = v3;
    v1 = v4;
    v2 = v5;
    if (!(g_1fab498 & 1))
    {
        sub_f7d92c(&g_1efcf38);
        sub_f7d92c(&g_1efebb8);
        g_1fab498 = 1;
    }
    if (Camera__get_main(0))
    {
        v6 = sub_1231bc8();
        if (v6 && v6->field_28)
        {
            ptr->field_30 = sub_1249224(v6->field_28, g_1efebb8);
            sub_f7d8d0();
            return;
        }
    }
    sub_f7db74();
}
```

## `DamageZone.OnTriggerStay` — RVA `0xc995bc`

- Decompiled symbol: `DamageZone_OnTriggerStay`
- Metadata signature: `private void OnTriggerStay(Collider col) { }`
- Native interval: `508` bytes
- Result: `pseudocode`
- Heuristic layout hint: `DamageZone_Recovered` matched 4 offsets against `DamageZone` metadata (confidence 1.00).

```c
typedef struct DamageZone_Recovered {
    char padding_0[32];
    unsigned int damage;
    char padding_24[4];
    unsigned int delay;
    unsigned int damageTime;
    long long FPSPlayerComponent;
} DamageZone_Recovered;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern long long g_1ef22e8;
extern long long g_1efcff8;
extern long long g_1f0cf98;
extern char g_1fab2c9;
extern char g_1fab499;

long long DamageZone_OnTriggerStay(struct_1 *ptr, long long a1)
{
    long long v0;  // x0
    unsigned int v1;  // s8
    unsigned int v2;  // s0
    unsigned long v3;  // 4125
    long long v4;  // x0
    long long v5;  // x0
    long long v6;  // x0
    long long v7;  // x0
    unsigned long long v8;  // x0

    if (!(g_1fab499 & 1))
    {
        sub_f7d92c(&g_1efcff8);
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c(&g_1f0cf98);
        g_1fab499 = 1;
    }
    if (a1 && Component__get_gameObject(a1, 0))
    {
        v0 = GameObject__get_tag();
        if (!(((char)String__op_Equality(v0, g_1f0cf98, 0) & 1) && !((v1 = ptr->field_2c, Time__get_time(0), v3 = (unsigned long)arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v1, v2)) >> 5 & 3 | (unsigned long long)(CmpF(v1, v2) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v1, v2)) >> 5 & 3 | (unsigned long long)(CmpF(v1, v2) & 1)) & ((unsigned long long)(char)(CmpF(v1, v2)) >> 5 & 3 | (unsigned long long)(CmpF(v1, v2) & 1)) >> 1 & 1)) * 0x10000000, 0, 0), (char)v3))))
        {
LABEL_1099688:
            if (Component__get_gameObject(a1, 0))
            {
                v4 = GameObject__get_layer();
                if ((int)v4 != 13)
                    return v4;
                v5 = sub_1231bc8(a1, g_1efcff8);
                if (!g_1ef0c58->field_e0)
                    sub_f7da5c(g_1ef0c58);
                v6 = Object__op_Implicit(v5, 0);
                if (!((char)v6 & 1))
                    return v6;
                v7 = sub_1231bc8(a1, g_1efcff8);
                if (!g_1fab2c9)
                {
                    sub_f7d92c(&g_1ef22e8);
                    g_1fab2c9 = 1;
                }
                if (Component__get_transform(ptr, 0))
                {
                    Transform__get_position();
                    if (v7)
                    {
                        v8 = LocationDamage__ApplyDamage();
                        return LocationDamage__ApplyDamage();
                    }
                }
            }
        }
        else if (ptr->field_30)
        {
            FPSPlayer__ApplyDamage(ptr->field_30, 0, 0, 0);
            Time__get_time(0);
            ptr->field_2c = ptr->field_20 + ptr->field_28;
            goto LABEL_1099688;
        }
    }
    sub_f7db74();
}
```

## `DamageZone.ctor` — RVA `0xc997b8`

- Decompiled symbol: `DamageZone_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `24` bytes
- Result: `pseudocode`

```c
long long DamageZone_ctor(unsigned int *ptr)
{
    long long v0;  // x0

    ptr[8] = 0x3f800000;
    ptr[10] = 0x3fe00000;
    v0 = MonoBehaviour__ctor();
    return MonoBehaviour__ctor();
}
```
