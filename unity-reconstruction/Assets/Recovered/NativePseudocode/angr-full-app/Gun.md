# Native pseudocode: Gun

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `Gun.OnEnable` — RVA `0xc67bd0`

- Decompiled symbol: `Gun_OnEnable`
- Metadata signature: `private void OnEnable() { }`
- Native interval: `96` bytes
- Result: `pseudocode`
- Heuristic layout hint: `Gun_Recovered` matched 2 offsets against `Gun` metadata (confidence 1.00).

```c
typedef struct Gun_Recovered {
    char padding_0[64];
    char isFiring;
    char padding_41[39];
    long long audioSource;
} Gun_Recovered;

extern long long g_1efcf18;
extern char g_1fab311;

long long Gun_OnEnable(struct_0 *ptr)
{
    long long v0;  // x0
    struct_0 *p;  // x19
    unsigned long v2;  // x0

    if (!(g_1fab311 & 1))
    {
        sub_f7d92c(&g_1efcf18);
        g_1fab311 = 1;
    }
    v0 = sub_1231bc8(ptr, g_1efcf18);
    ptr->field_68 = v0;
    p = &ptr->field_68;
    v2 = sub_f7d8d0(p, v0);
    p->padding_0[40] = 0;
    return v2;
}
```

## `Gun.SetTriggerState` — RVA `0xc67c30`

- Decompiled symbol: `Gun_SetTriggerState`
- Metadata signature: `public void SetTriggerState(bool fire) { }`
- Native interval: `32` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[64];
    char field_40;
} struct_0;

struct_0 * Gun_SetTriggerState(struct_0 *ptr, unsigned long a1)
{
    unsigned int v0;  // w8
    unsigned long long v1;  // x0

    v0 = (unsigned int)a1 & 1;
    if (ptr->field_40 == v0)
        return ptr;
    ptr->field_40 = v0;
    if (!((char)a1 & 1))
        return ptr;
    v1 = Gun__FireBullet();
    return Gun__FireBullet();
}
```

## `Gun.FireBullet` — RVA `0xc67c50`

- Decompiled symbol: `Gun_FireBullet`
- Metadata signature: `private void FireBullet() { }`
- Native interval: `764` bytes
- Result: `pseudocode`
- Heuristic layout hint: `Gun_Recovered` matched 10 offsets against `Gun` metadata (confidence 1.00).

```c
typedef struct struct_1 {
    char padding_0[32];
    unsigned long long field_20;
    long long field_28;
    long long field_30;
    char padding_38[12];
    unsigned int field_44;
    unsigned int field_48;
    char field_4c;
    char padding_4d[7];
    int field_54;
    unsigned long long field_58;
    long long field_60;
    unsigned long long field_68;
} struct_1;

typedef struct struct_3 {
    char padding_0[32];
    struct Gun_Recovered *field_20;
    char padding_28[12];
    unsigned int field_34;
    char padding_38[12];
    unsigned int field_44;
} struct_3;

typedef struct Gun_Recovered {
    char padding_0[32];
    unsigned long long shotParticles;
    unsigned long long shotSound;
    unsigned long long emptySound;
    char padding_38[12];
    unsigned int shotInterval;
    unsigned int lastShotTime;
    char unlimitedAmmo;
    char padding_4d[7];
    unsigned int bulletCount;
    unsigned long long projectileOrigin;
    unsigned long long bulletPrefab;
    unsigned long long audioSource;
} Gun_Recovered;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern long long g_1f00258;
extern char g_1fab313;

long long Gun_FireBullet(struct_1 *ptr)
{
    long long v0;  // x0
    unsigned int v1;  // s2
    struct_3 *p;  // x20
    long long v12;  // x0
    long long v13;  // x0
    unsigned long long v14;  // x0
    unsigned int v2;  // s0
    unsigned int v3;  // s0
    unsigned long v4;  // 4146
    unsigned int v5;  // w8
    long long v6;  // x0
    long long v7;  // x0
    unsigned long v8;  // x0
    struct_3 *addr;  // x20

    if (!(g_1fab313 & 1))
    {
        sub_f7d92c(&g_1f00258);
        sub_f7d92c(&g_1ef0c58);
        g_1fab313 = 1;
    }
    v0 = Time__get_time(0);
    v1 = ptr->field_44;
    v3 = v2 - ptr->field_48;
    v4 = arm64g_calculate_condition(176, (((((unsigned long long)(char)(CmpF(v3, v1)) >> 5 & 3 | (unsigned long long)(CmpF(v3, v1) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v3, v1)) >> 5 & 3 | (unsigned long long)(CmpF(v3, v1) & 1)) & ((unsigned long long)(char)(CmpF(v3, v1)) >> 5 & 3 | (unsigned long long)(CmpF(v3, v1) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if ((char)v4)
        return v0;
    Time__get_time(0);
    v5 = ptr->field_4c;
    ptr->field_48 = v3;
    if (v5)
    {
LABEL_1067cd4:
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        if (((char)Object__op_Inequality(ptr->field_20, 0, 0) & 1))
        {
            v8 = ptr->field_20;
            if (v8)
            {
                ParticleSystem__Play(v8, 0);
                goto LABEL_1067d14;
            }
        }
        else
        {
LABEL_1067d14:
            if (!g_1ef0c58->field_e0)
                sub_f7da5c(g_1ef0c58);
            if (((char)Object__op_Inequality(ptr->field_58, 0, 0) & 1))
            {
                if (!g_1ef0c58->field_e0)
                    sub_f7da5c(g_1ef0c58);
                if (!(Object__op_Inequality(ptr->field_60, 0, 0) & 1))
                    goto LABEL_1067e20;
                v8 = ptr->field_58;
                if (v8 && (Transform__get_position(v8, 0), v8 = (unsigned long)ptr->field_58, v8))
                {
                    Transform__get_rotation(v8, 0);
                    if (!g_1ef0c58->field_e0)
                        sub_f7da5c(g_1ef0c58);
                    addr = sub_112a1ac(ptr->field_60, g_1f00258);
                    v8 = Object__op_Inequality(addr, 0, 0);
                    if (!(v8 & 1))
                        goto LABEL_1067e20;
                    if (addr)
                    {
                        addr->field_20 = ptr;
                        p = &addr->field_20;
                        sub_f7d8d0(p, ptr);
                        *((unsigned int *)&p->padding_0[20]) = 0;
                        *((int *)((char *)&p->field_20 + 4)) = [D] unsupported_Iop_ZeroHI96ofV128();
                        goto LABEL_1067e20;
                    }
                }
            }
            else
            {
LABEL_1067e20:
                if (!g_1ef0c58->field_e0)
                    sub_f7da5c(g_1ef0c58);
                v12 = Object__op_Inequality(ptr->field_68, 0, 0);
                if (!((char)v12 & 1))
                    return v12;
                if (!g_1ef0c58->field_e0)
                    sub_f7da5c(g_1ef0c58);
                v13 = Object__op_Inequality(ptr->field_28, 0, 0);
                if (!((char)v13 & 1))
                    return v13;
                v8 = ptr->field_68;
                if (v8)
                {
                    AudioSource__set_loop(v8, 0, 0);
                    v8 = ptr->field_68;
                    if (v8)
                    {
                        v14 = AudioSource__PlayOneShot();
                        return AudioSource__PlayOneShot();
                    }
                }
            }
        }
    }
    else if (ptr->field_54 >= 1)
    {
        ptr->field_54 = ptr->field_54 - 1;
        goto LABEL_1067cd4;
    }
    else
    {
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        v6 = Object__op_Inequality(ptr->field_68, 0, 0);
        if (!((char)v6 & 1))
            return v6;
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        v7 = Object__op_Inequality(ptr->field_30, 0, 0);
        if (!((char)v7 & 1))
            return v7;
        v8 = ptr->field_68;
        if (v8)
        {
            AudioSource__set_loop(v8, 0, 0);
            v8 = ptr->field_68;
            if (v8)
            {
                v14 = AudioSource__PlayOneShot();
                return AudioSource__PlayOneShot();
            }
        }
    }
    sub_f7db74(v8);
}
```

## `Gun.FixedUpdate` — RVA `0xc67f4c`

- Decompiled symbol: `Gun_FixedUpdate`
- Metadata signature: `private void FixedUpdate() { }`
- Native interval: `16` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[64];
    char field_40;
} struct_0;

struct_0 * Gun_FixedUpdate(struct_0 *a0)
{
    long long v0;  // x0

    if (!a0->field_40)
        return a0;
    v0 = Gun__FireBullet(a0);
    return Gun__FireBullet(a0);
}
```

## `Gun.Reload` — RVA `0xc67f5c`

- Decompiled symbol: `Gun_Reload`
- Metadata signature: `public void Reload() { }`
- Native interval: `204` bytes
- Result: `pseudocode`
- Heuristic layout hint: `Gun_Recovered` matched 4 offsets against `Gun` metadata (confidence 1.00).

```c
typedef struct Gun_Recovered {
    char padding_0[56];
    long long reloadSound;
    char padding_40[16];
    unsigned int bulletCapacity;
    unsigned int bulletCount;
    char padding_58[16];
    unsigned long long audioSource;
} Gun_Recovered;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab312;

long long Gun_Reload(struct_1 *ptr)
{
    unsigned long long v0;  // x20
    long long v1;  // x0
    long long v2;  // x0
    unsigned long long v3;  // x0
    unsigned long long v4;  // x0

    if (!(g_1fab312 & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab312 = 1;
    }
    v0 = ptr->field_68;
    ptr->field_54 = ptr->field_50;
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v1 = Object__op_Inequality(v0, 0, 0);
    if (!((char)v1 & 1))
        return v1;
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v2 = Object__op_Inequality(ptr->field_38, 0, 0);
    if (!((char)v2 & 1))
        return v2;
    v3 = ptr->field_68;
    if (v3)
    {
        AudioSource__set_loop(v3, 0, 0);
        v3 = ptr->field_68;
        if (v3)
        {
            v4 = AudioSource__PlayOneShot();
            return AudioSource__PlayOneShot();
        }
    }
    sub_f7db74(v3);
}
```

## `Gun.ctor` — RVA `0xc68028`

- Decompiled symbol: `Gun_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `28` bytes
- Result: `pseudocode`
- Heuristic layout hint: `Gun_Recovered` matched 2 offsets against `Gun` metadata (confidence 1.00).

```c
typedef struct Gun_Recovered {
    char padding_0[68];
    unsigned int shotInterval;
    char padding_48[8];
    unsigned long long bulletCapacity;
} Gun_Recovered;

long long Gun_ctor(struct_0 *ptr)
{
    long long v0;  // x0

    ptr->field_44 = 1043542835;
    ptr->field_50 = 171798691880;
    v0 = MonoBehaviour__ctor();
    return MonoBehaviour__ctor();
}
```
