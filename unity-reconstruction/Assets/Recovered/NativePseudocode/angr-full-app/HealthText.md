# Native pseudocode: HealthText

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `HealthText.Start` — RVA `0xc91288`

- Decompiled symbol: `HealthText_Start`
- Metadata signature: `private void Start() { }`
- Native interval: `140` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    char padding_0[64];
    struct struct_3 *field_40;
} struct_2;

typedef struct struct_4 {
    char padding_0[680];
    struct struct_5 *field_2a8;
    unsigned long long field_2b0;
} struct_4;

typedef struct struct_0 {
    char padding_0[680];
    struct struct_1 *field_2a8;
    unsigned long long field_2b0;
} struct_0;

typedef struct struct_3 {
    struct struct_0 *field_0;
} struct_3;

typedef struct struct_5 {
    unsigned long long field_0;
} struct_5;

typedef struct struct_1 {
    unsigned long long field_0;
} struct_1;

extern long long g_1efd0b0;
extern char g_1fab44f;

void HealthText_Start(struct_2 *p)
{
    unsigned long long v4;  // x30
    unsigned long long v5;  // x21
    unsigned long long v6;  // x20
    unsigned long long v7;  // x19
    struct_4 **v8;  // x0
    struct_2 *ptr;  // x20
    struct_0 **v10;  // x0
    unsigned long long v11;  // x1
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x18]
    unsigned long long v2;  // [bp-0x10]
    unsigned long long v3;  // [bp-0x8]

    v0 = v4;
    v1 = v5;
    v2 = v6;
    v3 = v7;
    if (!(g_1fab44f & 1))
    {
        sub_f7d92c(&g_1efd0b0);
        g_1fab44f = 1;
    }
    v8 = sub_1231bc8(p, g_1efd0b0);
    p->field_40 = v8;
    ptr = &p->field_40;
    sub_f7d8d0(ptr, v8);
    v10 = *((long long *)&ptr->padding_0[0]);
    if (!*((long long *)&ptr->padding_0[0]))
        sub_f7db74(0);
    v11 = *((long long *)(*((long long *)*((long long *)&ptr->padding_0[0])) + 688));
    (*((long long *)(*((long long *)*((long long *)&ptr->padding_0[0])) + 680)))();
}
```

## `HealthText.Update` — RVA `0xc91314`

- Decompiled symbol: `HealthText_Update`
- Metadata signature: `private void Update() { }`
- Native interval: `212` bytes
- Result: `pseudocode`
- Heuristic layout hint: `HealthText_Recovered` matched 4 offsets against `HealthText` metadata (confidence 1.00).

```c
typedef struct HealthText_Recovered {
    char padding_0[32];
    unsigned int healthGui;
    unsigned int oldHealthGui;
    char padding_28[16];
    char showNegativeHP;
    char padding_39[7];
    struct struct_3 *guiTextComponent;
} HealthText_Recovered;

typedef struct struct_0 {
    char padding_0[1512];
    struct struct_1 *field_5e8;
} struct_0;

typedef struct struct_3 {
    struct struct_0 *field_0;
} struct_3;

typedef struct struct_1 {
    unsigned long long field_0;
} struct_1;

extern long long g_1f06ae0;
extern long long g_1f07670;
extern char g_1fab450;

struct_2 * HealthText_Update(struct_2 *ptr)
{
    unsigned int v0;  // s0
    unsigned int v1;  // s1
    unsigned int v2;  // 4105
    unsigned long v3;  // 4122
    unsigned long v4;  // 4125
    struct_0 **v5;  // x0
    unsigned long long *v6;  // x9
    long long v7;  // x0

    if (!(g_1fab450 & 1))
    {
        sub_f7d92c(&g_1f06ae0);
        sub_f7d92c(&g_1f07670);
        g_1fab450 = 1;
    }
    v0 = ptr->field_20;
    v1 = ptr->field_24;
    v2 = CmpF(v0, v1);
    v3 = (((CmpF(v0, v1) >> 5 & 3 | CmpF(v0, v1) & 1) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1;
    if ((char)((v3 - ((CmpF(v0, v1) >> 5 & 3 | CmpF(v0, v1) & 1) & (v2 >> 5 & 3 | CmpF(v0, v1) & 1) >> 1 & 1)) * 0x10000000 >> 30))
        return &ptr->field_20;
    v4 = arm64g_calculate_condition(128, (((((unsigned long long)(char)(CmpF(v0, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v0, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v0, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v0, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v0, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v0, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if ((char)v4 || ptr->field_38)
    {
        v7 = Single__ToString();
        v5 = String__Concat(v7, g_1f06ae0, 0);
        if (!ptr->field_40)
            sub_f7db74(v5);
        v6 = &ptr->field_40->field_0->field_5e8->field_0;
    }
    else
    {
        v5 = ptr->field_40;
        if (!v5)
            sub_f7db74(v5);
        v6 = &*(v5)->field_5e8->field_0;
    }
    v6();
}
```

## `HealthText.ctor` — RVA `0xc913e8`

- Decompiled symbol: `HealthText_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `24` bytes
- Result: `pseudocode`
- Heuristic layout hint: `HealthText_Recovered` matched 2 offsets against `HealthText` metadata (confidence 1.00).

```c
typedef struct HealthText_Recovered {
    char padding_0[36];
    unsigned int oldHealthGui;
    char padding_28[16];
    char showNegativeHP;
} HealthText_Recovered;

long long HealthText_ctor(struct_0 *ptr)
{
    long long v0;  // x0

    ptr->field_24 = 0xc4000000;
    ptr->field_38 = 1;
    v0 = MonoBehaviour__ctor();
    return MonoBehaviour__ctor();
}
```
