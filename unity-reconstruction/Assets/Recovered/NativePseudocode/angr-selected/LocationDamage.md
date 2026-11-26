# Native pseudocode: LocationDamage

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `LocationDamage.OnEnable` — RVA `0xc8498c`

- Decompiled symbol: `LocationDamage_OnEnable`
- Metadata signature: `private void OnEnable() { }`
- Native interval: `160` bytes
- Result: `pseudocode`
- Heuristic layout hint: `LocationDamage_Recovered` matched 3 offsets against `LocationDamage` metadata (confidence 1.00).

```c
typedef struct LocationDamage_Recovered {
    char padding_0[56];
    char headShotState;
    char padding_39[15];
    long long myTransform;
    long long thisRigidBody;
} LocationDamage_Recovered;

extern long long g_1efd080;
extern char g_1fab411;

void LocationDamage_OnEnable(struct_0 *p, unsigned long a1, unsigned long a2, unsigned long a3)
{
    unsigned long long v3;  // x30
    unsigned long long v4;  // x20
    unsigned long long v5;  // x19
    long long v6;  // x0
    struct_0 *ptr;  // x20
    long long v8;  // x0
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x10]
    unsigned long long v2;  // [bp-0x8]

    v0 = v3;
    v1 = v4;
    v2 = v5;
    if (!(g_1fab411 & 1))
    {
        sub_f7d92c(&g_1efd080);
        g_1fab411 = 1;
    }
    if (Component__get_gameObject(p, 0))
    {
        GameObject__set_layer();
        v6 = Component__get_transform(p, 0);
        p->field_48 = v6;
        ptr = &p->field_48;
        sub_f7d8d0(ptr, v6);
        v8 = *((long long *)&ptr->padding_0[0]);
        ptr->padding_0[16] = 0;
        if (v8)
        {
            p->field_50 = sub_1231bc8(v8, g_1efd080);
            sub_f7d8d0();
            return;
        }
    }
    sub_f7db74();
}
```


## `LocationDamage.ApplyDamage` — RVA `0xc84a2c`

- Decompiled symbol: `LocationDamage_ApplyDamage`
- Metadata signature: `public void ApplyDamage(float damage, Vector3 attackDir, Vector3 attackerPos, Transform attacker, bool isPlayer, bool isExplosion) { }`
- Native interval: `1180` bytes
- Result: `pseudocode`

```c
typedef struct struct_12 {
    char padding_0[224];
    unsigned int field_e0;
} struct_12;

typedef struct struct_10 {
    char padding_0[88];
    struct struct_8 *field_58;
    char padding_60[16];
    struct struct_9 *field_70;
} struct_10;

typedef struct struct_9 {
    char padding_0[64];
    unsigned int field_40;
} struct_9;

typedef struct struct_11 {
    char padding_0[224];
    unsigned int field_e0;
} struct_11;

typedef struct struct_8 {
    char padding_0[144];
    long long field_90;
} struct_8;

typedef struct struct_3 {
    char padding_0[336];
    struct struct_4 *field_150;
    char padding_158[152];
    long long field_1f0;
} struct_3;

typedef struct struct_5 {
    char padding_0[8];
    struct struct_3 *field_8;
    char padding_10[16];
    unsigned int field_20;
} struct_5;

typedef struct struct_1 {
    char padding_0[1512];
    struct struct_2 *field_5e8;
    unsigned long long field_5f0;
} struct_1;

typedef struct struct_4 {
    struct struct_1 *field_0;
} struct_4;

typedef struct struct_2 {
    unsigned long long field_0;
} struct_2;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

typedef struct struct_7 {
    char padding_0[224];
    unsigned int field_e0;
} struct_7;

typedef struct struct_6 {
    char padding_0[184];
    struct struct_5 *field_b8;
} struct_6;

extern struct_0 *g_1eef458;
extern struct_6 *g_1eefae8;
extern struct_7 *g_1ef0c58;
extern long long g_1efcf18;
extern long long g_1f08038;
extern unsigned long long g_1f0a9c8;
extern char g_1fab3e0;
extern char g_1fab412;

struct_12 * LocationDamage_ApplyDamage(void* ptr, long long a1, unsigned int a2, unsigned int a3)
{
    unsigned long v0;  // x20
    struct_9 *v1;  // x0
    unsigned int v10;  // s8
    unsigned long v11;  // 4125
    long long v12;  // x20
    unsigned long v14;  // x0
    struct_5 *p;  // x9
    struct_3 *v16;  // x8
    struct_1 **v17;  // x0
    unsigned long long v18;  // x2
    unsigned long long v19;  // x1
    unsigned long v2;  // x4
    struct_9 *v20;  // x0
    unsigned long long v21;  // x0
    unsigned long v3;  // x3
    struct_12 *v4;  // x0
    unsigned int v5;  // s0
    unsigned long v6;  // 4129
    struct_11 *v7;  // x0
    unsigned int v8;  // s0
    unsigned long v9;  // 4201

    v0 = a3;
    if (!(g_1fab412 & 1))
    {
        sub_f7d92c(&g_1efcf18);
        sub_f7d92c(&g_1eef458);
        sub_f7d92c(&g_1eefae8);
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c(&g_1f0a9c8);
        sub_f7d92c(&g_1f08038);
        sub_f7d92c(")#");
        g_1fab412 = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (!((char)Object__op_Implicit((long long)ptr[32], 0) & 1))
    {
LABEL_1084bec:
        if (!g_1eef458->field_e0)
            sub_f7da5c(g_1eef458);
        v21 = Debug__Log();
        return Debug__Log();
    }
    if ((long long)ptr[32])
    {
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        if (!(Object__op_Implicit(*((long long *)((long long)ptr[32] + 112)), 0) & 1))
            goto LABEL_1084bec;
        if ((long long)ptr[32])
        {
            v1 = *((long long *)((long long)ptr[32] + 112));
            if (((char)a2 & 1))
            {
                if (v1)
                {
                    v2 = (long long)ptr[80];
                    v3 = (unsigned int)v0 & 1;
                    CharacterDamage__ApplyDamage(v1, a1, 1, (unsigned int)v0 & 1, (long long)ptr[80]);
                    if (!g_1ef0c58->field_e0)
                        sub_f7da5c(g_1ef0c58);
                    v4 = Object__op_Implicit((long long)ptr[48], 0);
                    if (!((char)v4 & 1))
                        return v4;
                    if ((char)ptr[56])
                        return v4;
                    if ((long long)ptr[32] && *((long long *)((long long)ptr[32] + 112)))
                    {
                        v5 = *((int *)(*((long long *)((long long)ptr[32] + 112)) + 64));
                        v6 = arm64g_calculate_condition(144, (((((unsigned long long)(char)(CmpF(v5, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v5, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v5, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v5, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v5, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v5, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                        if (!((char)v6))
                            return v4;
                        if ((long long)ptr[72])
                        {
                            Transform__get_position((long long)ptr[72], 0);
                            if (!g_1fab3e0)
                            {
                                sub_f7d92c("_F");
                                g_1fab3e0 = 1;
                            }
                            v7 = g_1ef07e8;
                            if (!g_1ef07e8->field_e0)
                                v7 = sub_f7da5c(g_1ef07e8);
                            v8 = [D] unsupported_Iop_SqrtF32();
                            v9 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v8, 0x41700000)) >> 5 & 3 | (unsigned long long)(CmpF(v8, 0x41700000) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v8, 0x41700000)) >> 5 & 3 | (unsigned long long)(CmpF(v8, 0x41700000) & 1)) & ((unsigned long long)(char)(CmpF(v8, 0x41700000)) >> 5 & 3 | (unsigned long long)(CmpF(v8, 0x41700000) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                            if ((char)v9)
                                return v7;
                            if (((char)v0 & 1))
                                return v7;
                            if ((long long)ptr[72])
                            {
                                Transform__get_position((long long)ptr[72], 0);
                                PlayAudioAtPos__PlayClipAt((long long)ptr[48], 0);
                                v10 = (int)ptr[60];
                                Random__get_value(0);
                                v11 = arm64g_calculate_condition(176, (((((unsigned long long)(char)(CmpF(v10, v8)) >> 5 & 3 | (unsigned long long)(CmpF(v10, v8) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v10, v8)) >> 5 & 3 | (unsigned long long)(CmpF(v10, v8) & 1)) & ((unsigned long long)(char)(CmpF(v10, v8)) >> 5 & 3 | (unsigned long long)(CmpF(v10, v8) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                                if ((char)v11)
                                {
LABEL_1084da0:
                                    *((char *)&ptr[56]) = 1;
                                    if (g_1eefae8->field_b8->field_8)
                                    {
                                        v14 = sub_1231bc8(g_1eefae8->field_b8->field_8, g_1efcf18);
                                        if (g_1eefae8->field_b8->field_8 && v14)
                                        {
                                            AudioSource__PlayOneShot();
                                            p = g_1eefae8->field_b8;
                                            v16 = p->field_8;
                                            p->field_20 = p->field_20 + 1;
                                            if (v16 && v16->field_1f0)
                                            {
                                                GameObject__SetActive(v16->field_1f0, 1, 0);
                                                if (g_1eefae8->field_b8->field_8)
                                                {
                                                    v17 = g_1eefae8->field_b8->field_8->field_150;
                                                    if (v17)
                                                    {
                                                        v18 = *(v17)->field_5f0;
                                                        v19 = g_1f0a9c8;
                                                        *(v17)->field_5e8();
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                                else if ((long long)ptr[32] && *((long long *)((long long)ptr[32] + 88)) && (v12 = *((long long *)(*((long long *)((long long)ptr[32] + 88)) + 144)), v12))
                                {
                                    MonoBehaviour__StartCoroutine(v12, FPSPlayer__ActivateBulletTime(v12, 0), 0);
                                    goto LABEL_1084da0;
                                }
                            }
                        }
                    }
                }
            }
            else
            {
                if (v1)
                {
                    v20 = CharacterDamage__ApplyDamage(v1, a1, 0, (unsigned int)v0 & 1, (long long)ptr[80]);
                    return CharacterDamage__ApplyDamage(v1, a1, 0, (unsigned int)v0 & 1, (long long)ptr[80]);
                }
            }
        }
    }
    sub_f7db74();
}
```


## `LocationDamage.headshotfunc` — RVA `0xc84ec8`

- Decompiled symbol: `LocationDamage_headshotfunc`
- Metadata signature: `private IEnumerator headshotfunc() { }`
- Native interval: `88` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

extern char g_1fab413;

struct_0 * LocationDamage_headshotfunc(void)
{
    struct_0 *ptr;  // x0

    if (!(g_1fab413 & 1))
    {
        sub_f7d92c("sl");
        g_1fab413 = 1;
    }
    ptr = sub_f7db70(g_1ef3450);
    Object__ctor(ptr, 0);
    ptr->field_10 = 0;
    return ptr;
}
```


## `LocationDamage.<headshotfunc>d__11.ctor` — RVA `0xc84f20`

- Decompiled symbol: `LocationDamage_headshotfunc_d__11_ctor`
- Metadata signature: `public void .ctor(int <>1__state) { }`
- Native interval: `40` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

void LocationDamage_headshotfunc_d__11_ctor(struct_0 *ptr, unsigned int a1)
{
    Object__ctor();
    ptr->field_10 = a1;
    return;
}
```


## `LocationDamage.OnCollisionEnter` — RVA `0xc84f48`

- Decompiled symbol: `LocationDamage_OnCollisionEnter`
- Metadata signature: `private void OnCollisionEnter(Collision hit) { }`
- Native interval: `332` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    char padding_0[32];
    long long field_20;
} struct_2;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

typedef struct struct_1 {
    char padding_0[224];
    unsigned int field_e0;
} struct_1;

extern struct_0 *g_1ef0c58;
extern struct_1 *g_1ef0e48;
extern long long g_1efcf70;
extern long long g_1efcff8;
extern char g_1fab414;

long long LocationDamage_OnCollisionEnter(long long *ptr, long long a1)
{
    long long v0;  // x0
    struct_2 *p;  // x21
    long long v2;  // x0
    unsigned long long v3;  // x0

    if (!(g_1fab414 & 1))
    {
        sub_f7d92c(&g_1efcf70);
        sub_f7d92c(&g_1efcff8);
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c(&g_1ef0e48);
        g_1fab414 = 1;
    }
    v0 = ptr[4];
    if (v0)
    {
        v0 = Behaviour__get_enabled(v0, 0);
        if (!((char)v0 & 1))
        {
            return v0;
        }
        else if (a1)
        {
            v0 = Collision__get_collider(a1, 0);
            if (v0)
            {
                p = sub_1231bc8();
                if (!g_1ef0c58->field_e0)
                    sub_f7da5c(g_1ef0c58);
                v0 = Object__op_Implicit(p, 0);
                if (!((char)v0 & 1))
                {
                    return v0;
                }
                else if (p)
                {
                    v0 = p->field_20;
                    if (v0)
                    {
                        v2 = Behaviour__get_enabled(v0, 0);
                        if (((char)v2 & 1))
                            return v2;
                        v0 = Collision__get_collider(a1, 0);
                        if (ptr[9])
                        {
                            sub_1231bc8(ptr[9], g_1efcf70);
                            if (!g_1ef0e48->field_e0)
                                sub_f7da5c(g_1ef0e48);
                            v3 = Physics__IgnoreCollision();
                            return Physics__IgnoreCollision();
                        }
                    }
                }
            }
        }
    }
    sub_f7db74(v0);
}
```


## `LocationDamage.ctor` — RVA `0xc85094`

- Decompiled symbol: `LocationDamage_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `32` bytes
- Result: `pseudocode`
- Heuristic layout hint: `LocationDamage_Recovered` matched 2 offsets against `LocationDamage` metadata (confidence 1.00).

```c
typedef struct LocationDamage_Recovered {
    char padding_0[40];
    unsigned long long damageMultiplier;
    char padding_30[16];
    unsigned int sloMoTime;
} LocationDamage_Recovered;

long long LocationDamage_ctor(struct_0 *ptr)
{
    ptr->field_28 = 0x403000003f800000;
    ptr->field_40 = 1063675494;
}
```


## `LocationDamage.<headshotfunc>d__11.Dispose` — RVA `0xc850b4`

- Decompiled symbol: `LocationDamage_headshotfunc_d__11_Dispose`
- Metadata signature: `private void System.IDisposable.Dispose() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long LocationDamage_headshotfunc_d__11_Dispose(void)
{
    unsigned long v0;  // x0

    return v0;
}
```


## `LocationDamage.<headshotfunc>d__11.MoveNext` — RVA `0xc850b8`

- Decompiled symbol: `LocationDamage_headshotfunc_d__11_MoveNext`
- Metadata signature: `private bool MoveNext() { }`
- Native interval: `212` bytes
- Result: `pseudocode`

```c
typedef struct struct_3 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[4];
    long long field_18;
} struct_3;

typedef struct struct_0 {
    char padding_0[496];
    long long field_1f0;
} struct_0;

typedef struct struct_1 {
    char padding_0[8];
    struct struct_0 *field_8;
} struct_1;

typedef struct struct_2 {
    char padding_0[184];
    struct struct_1 *field_b8;
} struct_2;

extern struct_2 *g_1eefae8;
extern long long g_1ef2440;
extern char g_1fab415;

unsigned int LocationDamage_headshotfunc_d__11_MoveNext(struct_3 *ptr)
{
    long long v0;  // x20
    struct_0 *v1;  // x8

    if (!(g_1fab415 & 1))
    {
        sub_f7d92c(&g_1eefae8);
        sub_f7d92c(&g_1ef2440);
        g_1fab415 = 1;
    }
    if (ptr->field_10 == 1)
    {
        ptr->field_10 = 4294967295;
        v1 = g_1eefae8->field_b8->field_8;
        if (!v1 || !v1->field_1f0)
            sub_f7db74();
        GameObject__SetActive(v1->field_1f0, 0, 0);
    }
    else if (!ptr->field_10)
    {
        ptr->field_10 = 4294967295;
        v0 = sub_f7db70(g_1ef2440);
        WaitForSeconds__ctor(v0, 0);
        ptr->field_18 = v0;
        sub_f7d8d0(&ptr->field_18, v0);
        ptr->field_10 = 1;
        return 1;
    }
    return 0;
}
```


## `LocationDamage.<headshotfunc>d__11.get_Current` — RVA `0xc8518c`

- Decompiled symbol: `LocationDamage_headshotfunc_d__11_get_Current`
- Metadata signature: `private object System.Collections.Generic.IEnumerator<System.Object>.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long LocationDamage_headshotfunc_d__11_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```


## `LocationDamage.<headshotfunc>d__11.Reset` — RVA `0xc85194`

- Decompiled symbol: `LocationDamage_headshotfunc_d__11_Reset`
- Metadata signature: `private void System.Collections.IEnumerator.Reset() { }`
- Native interval: `56` bytes
- Result: `pseudocode`

```c
extern long long g_1ef0bd8;
extern long long g_1f048a8;

void LocationDamage_headshotfunc_d__11_Reset(void)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    long long v4;  // x0
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    v4 = sub_f7db70(sub_f7d940(&g_1ef0bd8));
    NotSupportedException__ctor(v4, 0);
    sub_f7da4c(v4, sub_f7d940(&g_1f048a8));
}
```


## `LocationDamage.<headshotfunc>d__11.get_Current` — RVA `0xc851cc`

- Decompiled symbol: `LocationDamage_headshotfunc_d__11_get_Current`
- Metadata signature: `private object System.Collections.IEnumerator.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long LocationDamage_headshotfunc_d__11_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```
