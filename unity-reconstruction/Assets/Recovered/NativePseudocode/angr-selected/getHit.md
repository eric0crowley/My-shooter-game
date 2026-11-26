# Native pseudocode: getHit

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `getHit.Start` — RVA `0xc6e054`

- Decompiled symbol: `getHit_Start`
- Metadata signature: `private void Start() { }`
- Native interval: `252` bytes
- Result: `pseudocode`
- Heuristic layout hint: `getHit_Recovered` matched 2 offsets against `getHit` metadata (confidence 1.00).

```c
typedef struct getHit_Recovered {
    char padding_0[32];
    unsigned long long myHealthOBJ;
    long long EH;
} getHit_Recovered;

typedef struct struct_2 {
    unsigned long long field_0;
} struct_2;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

typedef struct struct_1 {
    char padding_0[184];
    struct struct_2 *field_b8;
} struct_1;

extern struct_0 *g_1ef0c58;
extern struct_1 *g_1ef2b18;
extern long long g_1efd100;
extern long long g_1efeba8;
extern char g_1fab34f;

void getHit_Start(struct_3 *ptr, unsigned long a1, unsigned long a2)
{
    unsigned long long v4;  // x30
    unsigned long long v5;  // x21
    unsigned long long v6;  // x20
    unsigned long long v7;  // x19
    unsigned long long v8;  // x0
    long long v9;  // x0
    long long v10;  // x1
    unsigned long long v11;  // x0
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x18]
    unsigned long long v2;  // [bp-0x10]
    unsigned long long v3;  // [bp-0x8]

    v0 = v4;
    v1 = v5;
    v2 = v6;
    v3 = v7;
    if (!(g_1fab34f & 1))
    {
        sub_f7d92c(&g_1efd100);
        sub_f7d92c(&g_1efeba8);
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c(&g_1ef2b18);
        g_1fab34f = 1;
    }
    v8 = ptr->field_20;
    if (v8)
    {
        v9 = sub_1249224(v8, g_1efeba8);
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        if (((char)Object__op_Implicit(v9, 0) & 1))
        {
            v8 = ptr->field_20;
            if (!v8)
                goto LABEL_106e14c;
            v10 = sub_1249224(v8, g_1efeba8);
            ptr->field_28 = v10;
            sub_f7d8d0(&ptr->field_28, v10);
        }
        v11 = sub_1231bc8(ptr, g_1efd100);
        g_1ef2b18->field_b8->field_0 = v11;
        sub_f7d8d0();
        return;
    }
LABEL_106e14c:
    sub_f7db74(v8);
}
```


## `getHit.applyDamage` — RVA `0xc6e150`

- Decompiled symbol: `getHit_applyDamage`
- Metadata signature: `public void applyDamage(float damage, bool is_HeadShot, bool isPlayer) { }`
- Native interval: `176` bytes
- Result: `pseudocode`

```c
typedef struct struct_3 {
    char padding_0[32];
    unsigned int field_20;
} struct_3;

typedef struct struct_2 {
    char padding_0[40];
    struct struct_1 *field_28;
} struct_2;

typedef struct struct_1 {
    char padding_0[32];
    unsigned int field_20;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab350;

struct_3 * getHit_applyDamage(struct_2 *ptr, unsigned long a1, unsigned int a2)
{
    struct_3 *v0;  // x0
    struct_1 *p;  // x0
    unsigned int v2;  // s0
    unsigned long v3;  // 4129
    struct_1 *v4;  // x0

    if (!(g_1fab350 & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab350 = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v0 = Object__op_Implicit(ptr->field_28, 0);
    if (!((char)v0 & 1))
        return v0;
    p = ptr->field_28;
    if (p)
    {
        v2 = p->field_20;
        v3 = arm64g_calculate_condition(160, (((((unsigned long long)(char)(CmpF(v2, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v2, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v2, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v2, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v2, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v2, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if ((char)v3)
        {
            v4 = EnemyHealth__Damage(p, a2 & 1);
            return EnemyHealth__Damage(p, a2 & 1);
        }
        return p;
    }
    sub_f7db74(0);
}
```


## `getHit.ctor` — RVA `0xc6e200`

- Decompiled symbol: `getHit_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long getHit_ctor(void)
{
}
```
