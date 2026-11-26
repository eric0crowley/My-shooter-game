# Native pseudocode: EnemyHealth

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `EnemyHealth.Start` — RVA `0xc6d558`

- Decompiled symbol: `EnemyHealth_Start`
- Metadata signature: `private void Start() { }`
- Native interval: `232` bytes
- Result: `pseudocode`
- Heuristic layout hint: `EnemyHealth_Recovered` matched 3 offsets against `EnemyHealth` metadata (confidence 1.00).

```c
typedef struct EnemyHealth_Recovered {
    char padding_0[32];
    unsigned int healthPoints;
    unsigned int tempHealthPoints;
    long long ai;
} EnemyHealth_Recovered;

typedef struct struct_1 {
    long long field_0;
} struct_1;

typedef struct struct_0 {
    char padding_0[184];
    struct struct_1 *field_b8;
} struct_0;

extern struct_0 *g_1eef748;
extern long long g_1efcf80;
extern long long g_1efd108;
extern char g_1fab349;

long long EnemyHealth_Start(struct_2 *ptr)
{
    long long v0;  // x1
    long long v1;  // x0
    unsigned long v2;  // x0
    unsigned int v3;  // s0
    unsigned long v4;  // 4133
    unsigned long long v5;  // x0

    if (!(g_1fab349 & 1))
    {
        sub_f7d92c(&g_1efcf80);
        sub_f7d92c(&g_1efd108);
        sub_f7d92c(&g_1eef748);
        g_1fab349 = 1;
    }
    v0 = sub_1231bc8(ptr, g_1efd108);
    ptr->field_28 = v0;
    sub_f7d8d0(&ptr->field_28, v0);
    v1 = sub_1231bc8(ptr, g_1efcf80);
    g_1eef748->field_b8->field_0 = v1;
    v2 = sub_f7d8d0(g_1eef748->field_b8, v1);
    v3 = ptr->field_20;
    ptr->field_24 = v3;
    v4 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v3, 0x3f800000)) >> 5 & 3 | (unsigned long long)(CmpF(v3, 0x3f800000) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v3, 0x3f800000)) >> 5 & 3 | (unsigned long long)(CmpF(v3, 0x3f800000) & 1)) & ((unsigned long long)(char)(CmpF(v3, 0x3f800000)) >> 5 & 3 | (unsigned long long)(CmpF(v3, 0x3f800000) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if ((char)v4)
        return v2;
    v5 = EnemyHealth__Damage(ptr, 0);
    return EnemyHealth__Damage(ptr, 0);
}
```

## `EnemyHealth.Damage` — RVA `0xc6d640`

- Decompiled symbol: `EnemyHealth_Damage`
- Metadata signature: `public void Damage(float damage, bool isPlayer) { }`
- Native interval: `648` bytes
- Result: `pseudocode`
- Heuristic layout hint: `EnemyHealth_Recovered` matched 4 offsets against `EnemyHealth` metadata (confidence 1.00).

```c
typedef struct EnemyHealth_Recovered {
    char padding_0[32];
    unsigned int healthPoints;
    char padding_24[12];
    char checkDead;
    char padding_31[39];
    long long UI_HealthBar;
    char padding_60[16];
    char ActiveShield;
} EnemyHealth_Recovered;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern long long g_1ef0750;
extern struct_0 *g_1ef0c58;
extern long long g_1ef2ad8;
extern long long g_1f09a80;
extern char g_1fab34a;

struct_1 * EnemyHealth_Damage(struct_1 *ptr, unsigned long a1)
{
    struct_1 *v0;  // x0
    struct_1 *v1;  // x0
    struct_1 *v2;  // x0
    unsigned int v3;  // s0
    struct_1 *v4;  // x0
    unsigned int v5;  // s0
    unsigned long v6;  // 4129

    v0 = ptr;
    if (!(g_1fab34a & 1))
    {
        sub_f7d92c(&g_1ef0750);
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c(&g_1ef2ad8);
        v1 = sub_f7d92c(&g_1f09a80);
        g_1fab34a = 1;
        v0 = v1;
    }
    v2 = v0;
    if (ptr->field_30)
    {
        return v2;
    }
    else if (!ptr->field_70)
    {
        ptr->field_20 = ptr->field_20 - v3;
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        v4 = Object__op_Inequality(ptr->field_58, 0, 0);
        if (((char)v4 & 1))
        {
            if (ptr->field_58)
                v4 = Image__set_fillAmount(ptr->field_58, 0);
            else
                sub_f7db74(0);
        }
        v5 = ptr->field_20;
        v6 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v5, 0x3f800000)) >> 5 & 3 | (unsigned long long)(CmpF(v5, 0x3f800000) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v5, 0x3f800000)) >> 5 & 3 | (unsigned long long)(CmpF(v5, 0x3f800000) & 1)) & ((unsigned long long)(char)(CmpF(v5, 0x3f800000)) >> 5 & 3 | (unsigned long long)(CmpF(v5, 0x3f800000) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if ((char)v6)
            return v4;
        EnemyHealth__PlayDieSound(ptr); /* do not return */
    }
    else
    {
        return v2;
    }
}
```

## `EnemyHealth.PlayDieSound` — RVA `0xc6d8c8`

- Decompiled symbol: `EnemyHealth_PlayDieSound`
- Metadata signature: `private void PlayDieSound() { }`
- Native interval: `188` bytes
- Result: `pseudocode`
- Heuristic layout hint: `EnemyHealth_Recovered` matched 2 offsets against `EnemyHealth` metadata (confidence 1.00).

```c
typedef struct EnemyHealth_Recovered {
    char padding_0[72];
    long long myAudioSource;
    struct struct_0 *DieSound;
} EnemyHealth_Recovered;

typedef struct struct_0 {
    char padding_0[24];
    unsigned int field_18;
} struct_0;

void EnemyHealth_PlayDieSound(struct_1 *ptr)
{
    unsigned long long v4;  // x30
    unsigned long long v5;  // x21
    unsigned long long v6;  // x20
    unsigned long long v7;  // x19
    struct_0 *v8;  // x21
    long long v9;  // x0
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x18]
    unsigned long long v2;  // [bp-0x10]
    unsigned long long v3;  // [bp-0x8]

    v0 = v4;
    v1 = v5;
    v2 = v6;
    v3 = v7;
    Random__Range(0);
    if (ptr->field_48 && !((AudioSource__set_pitch(ptr->field_48, 0), !ptr->field_48 || (AudioSource__set_volume(ptr->field_48, 0), v8 = (struct_0 *)ptr->field_50, !v8))))
    {
        v9 = Random__Range(0, v8->field_18, 0);
        if (v8->field_18 <= (int)v9)
            goto LABEL_106d980;
        if (ptr->field_48)
        {
            AudioSource__set_clip(ptr->field_48, *((long long *)&v8[1].padding_0[4 + 8 * (v9 & 4294967295)]), 0);
            if (ptr->field_48)
            {
                AudioSource__set_loop(ptr->field_48, 0, 0);
                if (ptr->field_48)
                {
                    AudioSource__Play();
                    return;
                }
            }
        }
    }
    v9 = sub_f7db74();
LABEL_106d980:
    sub_f7db7c(v9);
}
```

## `EnemyHealth.CallRespawn` — RVA `0xc6d984`

- Decompiled symbol: `EnemyHealth_CallRespawn`
- Metadata signature: `private IEnumerator CallRespawn() { }`
- Native interval: `108` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[12];
    long long field_20;
} struct_0;

extern long long g_1ef3038;
extern char g_1fab34b;

struct_0 * EnemyHealth_CallRespawn(long long a0)
{
    struct_0 *v0;  // x20
    struct_0 *ptr;  // x0

    if (!(g_1fab34b & 1))
    {
        sub_f7d92c(&g_1ef3038);
        g_1fab34b = 1;
    }
    v0 = sub_f7db70(g_1ef3038);
    Object__ctor(v0, 0);
    ptr = v0;
    ptr->field_10 = 0;
    ptr->field_20 = a0;
    sub_f7d8d0(&ptr->field_20, a0);
    return ptr;
}
```

## `EnemyHealth.<CallRespawn>d__16.ctor` — RVA `0xc6d9f0`

- Decompiled symbol: `EnemyHealth_CallRespawn_d__16_ctor`
- Metadata signature: `public void .ctor(int <>1__state) { }`
- Native interval: `40` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

void EnemyHealth_CallRespawn_d__16_ctor(struct_0 *ptr, unsigned int a1)
{
    Object__ctor();
    ptr->field_10 = a1;
    return;
}
```

## `EnemyHealth.Set_Shield_Acticated` — RVA `0xc6da18`

- Decompiled symbol: `EnemyHealth_Set_Shield_Acticated`
- Metadata signature: `private IEnumerator Set_Shield_Acticated() { }`
- Native interval: `108` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[12];
    long long field_20;
} struct_0;

extern long long g_1ef3040;
extern char g_1fab34c;

struct_0 * EnemyHealth_Set_Shield_Acticated(long long a0)
{
    struct_0 *v0;  // x20
    struct_0 *ptr;  // x0

    if (!(g_1fab34c & 1))
    {
        sub_f7d92c(&g_1ef3040);
        g_1fab34c = 1;
    }
    v0 = sub_f7db70(g_1ef3040);
    Object__ctor(v0, 0);
    ptr = v0;
    ptr->field_10 = 0;
    ptr->field_20 = a0;
    sub_f7d8d0(&ptr->field_20, a0);
    return ptr;
}
```

## `EnemyHealth.<Set_Shield_Acticated>d__17.ctor` — RVA `0xc6da84`

- Decompiled symbol: `EnemyHealth_Set_Shield_Acticated_d__17_ctor`
- Metadata signature: `public void .ctor(int <>1__state) { }`
- Native interval: `40` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

void EnemyHealth_Set_Shield_Acticated_d__17_ctor(struct_0 *ptr, unsigned int a1)
{
    Object__ctor();
    ptr->field_10 = a1;
    return;
}
```

## `EnemyHealth.ctor` — RVA `0xc6daac`

- Decompiled symbol: `EnemyHealth_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `16` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[32];
    unsigned int field_20;
} struct_0;

long long EnemyHealth_ctor(struct_0 *ptr)
{
    ptr->field_20 = 0x42c80000;
}
```

## `EnemyHealth.<CallRespawn>d__16.Dispose` — RVA `0xc6dabc`

- Decompiled symbol: `EnemyHealth_CallRespawn_d__16_Dispose`
- Metadata signature: `private void System.IDisposable.Dispose() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long EnemyHealth_CallRespawn_d__16_Dispose(void)
{
    unsigned long v0;  // x0

    return v0;
}
```

## `EnemyHealth.<CallRespawn>d__16.MoveNext` — RVA `0xc6dac0`

- Decompiled symbol: `EnemyHealth_CallRespawn_d__16_MoveNext`
- Metadata signature: `private bool MoveNext() { }`
- Native interval: `660` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[4];
    long long field_18;
    struct struct_1 *field_20;
    long long field_28;
} struct_2;

typedef struct struct_1 {
    char padding_0[32];
    unsigned int field_20;
    unsigned int field_24;
    struct struct_0 *field_28;
    char field_30;
} struct_1;

typedef struct struct_0 {
    char padding_0[192];
    long long field_c0;
    long long field_c8;
    char padding_d0[48];
    char field_100;
} struct_0;

extern long long g_1ef2440;
extern long long g_1efd078;
extern long long g_1efd088;
extern long long g_1f09968;
extern long long g_1f0d618;
extern long long g_1f131d8;
extern char g_1fab34d;

unsigned int EnemyHealth_CallRespawn_d__16_MoveNext(struct_2 *ptr)
{
    unsigned int flag;  // w8
    struct_1 *p;  // x20
    struct_0 *v10;  // x8
    struct_0 *addr;  // x8
    long long v12;  // x0
    long long v2;  // x0
    struct_2 *v3;  // x21
    struct_0 *ptr3;  // x8
    long long v5;  // x20
    struct_2 *ptr4;  // x19
    long long v7;  // x8
    long long v8;  // x20
    struct_2 *ptr5;  // x19

    if (!(g_1fab34d & 1))
    {
        sub_f7d92c(&g_1efd078);
        sub_f7d92c(&g_1efd088);
        sub_f7d92c(&g_1ef2440);
        sub_f7d92c(&g_1f09968);
        sub_f7d92c(&g_1f131d8);
        sub_f7d92c(&g_1f0d618);
        g_1fab34d = 1;
    }
    flag = ptr->field_10;
    p = ptr->field_20;
    if (flag == 2)
    {
        ptr->field_10 = 4294967295;
        if (p)
        {
            v10 = p->field_28;
            p->field_20 = p->field_24;
            if (v10 && v10->field_c0)
            {
                Animator__SetInteger(v10->field_c0, g_1f09968, 0, 0);
                if (p->field_28 && p->field_28->field_c0)
                {
                    Animator__SetBool(p->field_28->field_c0, g_1f131d8, 0, 0);
                    if (p->field_28 && p->field_28->field_c0)
                    {
                        Animator__Play(p->field_28->field_c0, g_1f0d618, 0);
                        addr = p->field_28;
                        p->field_30 = 0;
                        if (addr)
                        {
                            v12 = addr->field_c8;
                            addr->field_100 = 0;
                            if (v12)
                            {
                                NavMeshAgent__set_speed(v12, 0);
                                MonoBehaviour__StartCoroutine(p, EnemyHealth__Set_Shield_Acticated(p), 0);
                                if (Component__get_transform(p, 0) && sub_1231bc8())
                                {
                                    RespawnCharacter__RespawnNow();
                                    return 0;
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    else if (flag == 1)
    {
        v7 = ptr->field_28;
        ptr->field_10 = 4294967295;
        if (v7)
        {
            v8 = sub_f7db70(g_1ef2440);
            WaitForSeconds__ctor(v8, 0);
            ptr->field_18 = v8;
            ptr5 = &ptr->field_18;
            sub_f7d8d0(ptr5, v8);
            *((unsigned int *)&ptr5->padding_0[8]) = 2;
            return 1;
        }
    }
    else if (!flag)
    {
        ptr->field_10 = 4294967295;
        if (p && Component__get_transform(p, 0))
        {
            v2 = sub_1231bc8();
            ptr->field_28 = v2;
            v3 = &ptr->field_28;
            sub_f7d8d0(v3, v2);
            ptr3 = p->field_28;
            if (ptr3)
            {
                if (!ptr3->field_100)
                    ptr3->field_100 = 1;
                if (ptr3->field_c0)
                {
                    Animator__SetInteger(ptr3->field_c0, g_1f09968, 2, 0);
                    if (*((long long *)&v3->padding_0[0]))
                    {
                        SetTeamId__CountKill();
                        v5 = sub_f7db70(g_1ef2440);
                        WaitForSeconds__ctor(v5, 0);
                        ptr->field_18 = v5;
                        ptr4 = &ptr->field_18;
                        sub_f7d8d0(ptr4, v5);
                        *((unsigned int *)&ptr4->padding_0[8]) = 1;
                        return 1;
                    }
                }
            }
        }
    }
    else
    {
        return 0;
    }
    sub_f7db74();
}
```

## `EnemyHealth.<CallRespawn>d__16.get_Current` — RVA `0xc6df04`

- Decompiled symbol: `EnemyHealth_CallRespawn_d__16_get_Current`
- Metadata signature: `private object System.Collections.Generic.IEnumerator<System.Object>.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long EnemyHealth_CallRespawn_d__16_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```

## `EnemyHealth.<CallRespawn>d__16.Reset` — RVA `0xc6df0c`

- Decompiled symbol: `EnemyHealth_CallRespawn_d__16_Reset`
- Metadata signature: `private void System.Collections.IEnumerator.Reset() { }`
- Native interval: `56` bytes
- Result: `pseudocode`

```c
extern long long g_1ef0bd8;
extern long long g_1f04528;

void EnemyHealth_CallRespawn_d__16_Reset(void)
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
    sub_f7da4c(v4, sub_f7d940(&g_1f04528));
}
```

## `EnemyHealth.<CallRespawn>d__16.get_Current` — RVA `0xc6df44`

- Decompiled symbol: `EnemyHealth_CallRespawn_d__16_get_Current`
- Metadata signature: `private object System.Collections.IEnumerator.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long EnemyHealth_CallRespawn_d__16_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```

## `EnemyHealth.<Set_Shield_Acticated>d__17.Dispose` — RVA `0xc6df4c`

- Decompiled symbol: `EnemyHealth_Set_Shield_Acticated_d__17_Dispose`
- Metadata signature: `private void System.IDisposable.Dispose() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long EnemyHealth_Set_Shield_Acticated_d__17_Dispose(void)
{
    unsigned long v0;  // x0

    return v0;
}
```

## `EnemyHealth.<Set_Shield_Acticated>d__17.MoveNext` — RVA `0xc6df50`

- Decompiled symbol: `EnemyHealth_Set_Shield_Acticated_d__17_MoveNext`
- Metadata signature: `private bool MoveNext() { }`
- Native interval: `188` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[4];
    long long field_18;
    struct struct_0 *field_20;
} struct_1;

typedef struct struct_0 {
    char padding_0[112];
    char field_70;
} struct_0;

extern long long g_1ef2440;
extern char g_1fab34e;

unsigned int EnemyHealth_Set_Shield_Acticated_d__17_MoveNext(struct_1 *ptr)
{
    struct_0 *p;  // x8
    long long v1;  // x21
    struct_1 *addr;  // x19

    if (!(g_1fab34e & 1))
    {
        sub_f7d92c(&g_1ef2440);
        g_1fab34e = 1;
    }
    p = ptr->field_20;
    if (ptr->field_10 == 1)
    {
        ptr->field_10 = 4294967295;
        if (p)
        {
            p->field_70 = 0;
            return 0;
        }
    }
    else if (!ptr->field_10)
    {
        ptr->field_10 = 4294967295;
        if (p)
        {
            p->field_70 = 1;
            v1 = sub_f7db70(g_1ef2440);
            WaitForSeconds__ctor(v1, 0);
            ptr->field_18 = v1;
            addr = &ptr->field_18;
            sub_f7d8d0(addr, v1);
            *((unsigned int *)&addr->padding_0[8]) = 1;
            return 1;
        }
    }
    else
    {
        return 0;
    }
    sub_f7db74();
}
```

## `EnemyHealth.<Set_Shield_Acticated>d__17.get_Current` — RVA `0xc6e00c`

- Decompiled symbol: `EnemyHealth_Set_Shield_Acticated_d__17_get_Current`
- Metadata signature: `private object System.Collections.Generic.IEnumerator<System.Object>.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long EnemyHealth_Set_Shield_Acticated_d__17_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```

## `EnemyHealth.<Set_Shield_Acticated>d__17.Reset` — RVA `0xc6e014`

- Decompiled symbol: `EnemyHealth_Set_Shield_Acticated_d__17_Reset`
- Metadata signature: `private void System.Collections.IEnumerator.Reset() { }`
- Native interval: `56` bytes
- Result: `pseudocode`

```c
extern long long g_1ef0bd8;
extern long long g_1f04530;

void EnemyHealth_Set_Shield_Acticated_d__17_Reset(void)
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
    sub_f7da4c(v4, sub_f7d940(&g_1f04530));
}
```

## `EnemyHealth.<Set_Shield_Acticated>d__17.get_Current` — RVA `0xc6e04c`

- Decompiled symbol: `EnemyHealth_Set_Shield_Acticated_d__17_get_Current`
- Metadata signature: `private object System.Collections.IEnumerator.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long EnemyHealth_Set_Shield_Acticated_d__17_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```
