# Native pseudocode: NPCAttack

> Metadata source-path string: `Assets/RFPSP/Scripts/AI/NPCAttack.cs`. This is a path string from the APK metadata, not recovered source text.

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `NPCAttack.Fire` — RVA `0xc816e8`

- Decompiled symbol: `NPCAttack_Fire`
- Metadata signature: `public void Fire() { }`
- Native interval: `124` bytes
- Result: `pseudocode`
- Heuristic layout hint: `NPCAttack_Recovered` matched 4 offsets against `NPCAttack` metadata (confidence 1.00).

```c
typedef struct NPCAttack_Recovered {
    char padding_0[92];
    unsigned int fireRate;
    char padding_60[40];
    char shooting;
    char reloading;
    char padding_8a[86];
    unsigned int shootStartTime;
} NPCAttack_Recovered;

int NPCAttack_Fire(struct_0 *ptr)
{
    struct_0 *p;  // x20
    struct_0 *addr;  // x0
    unsigned int v2;  // s1
    unsigned int v3;  // s0
    unsigned long v4;  // 4138
    struct_0 *v5;  // x0

    p = &ptr->field_88;
    addr = ptr;
    if (!addr->field_89)
    {
        if (p->padding_0[0])
        {
            addr = Time__get_time(0);
            v2 = ptr->field_e0 + ptr->field_5c;
            v4 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(v2, v3)) >> 5 & 3 | (unsigned long long)(CmpF(v2, v3) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v2, v3)) >> 5 & 3 | (unsigned long long)(CmpF(v2, v3) & 1)) & ((unsigned long long)(char)(CmpF(v2, v3)) >> 5 & 3 | (unsigned long long)(CmpF(v2, v3) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
            if (!((char)v4))
                return *((unsigned int *)&addr);
        }
        else
        {
            NPCAttack__FireOneShot(ptr);
            v5 = Time__get_time(0);
            ptr->field_e0 = v3;
            ptr->field_88 = 1;
            p = &ptr->padding_60[24];
            addr = v5;
        }
    }
    p->padding_0[0] = 0;
    return *((unsigned int *)&addr);
}
```

## `NPCAttack.OnEnable` — RVA `0xc85a0c`

- Decompiled symbol: `NPCAttack_OnEnable`
- Metadata signature: `private void OnEnable() { }`
- Native interval: `516` bytes
- Result: `pseudocode`
- Heuristic layout hint: `NPCAttack_Recovered` matched 10 offsets against `NPCAttack` metadata (confidence 1.00).

```c
typedef struct NPCAttack_Recovered {
    char padding_0[32];
    struct struct_3 *AIComponent;
    long long WeaponEffectsComponent;
    long long FPSWalker;
    struct struct_4 *playerObj;
    struct struct_5 *myTransform;
    char padding_48[20];
    unsigned int fireRate;
    char padding_60[88];
    struct struct_6 *muzzleFlash;
    long long muzzleFlashTransform;
    char padding_c8[16];
    long long aSource;
    unsigned int shootStartTime;
} NPCAttack_Recovered;

typedef struct struct_1 {
    char padding_0[40];
    struct struct_1 *field_28;
    char padding_30[152];
    struct struct_1 *field_c8;
} struct_1;

typedef struct struct_9 {
    char padding_0[40];
    struct struct_8 *field_28;
} struct_9;

typedef struct struct_3 {
    char padding_0[40];
    struct struct_2 *field_28;
} struct_3;

typedef struct struct_4 {
    char padding_0[40];
    struct struct_4 *field_28;
    char padding_30[152];
    struct struct_4 *field_c8;
} struct_4;

typedef struct struct_5 {
    char padding_0[40];
    struct struct_5 *field_28;
    char padding_30[152];
    struct struct_5 *field_c8;
} struct_5;

typedef struct struct_6 {
    char padding_0[40];
    struct struct_6 *field_28;
    char padding_30[152];
    struct struct_6 *field_c8;
} struct_6;

typedef struct struct_8 {
    char padding_0[40];
    struct struct_8 *field_28;
    char padding_30[152];
    struct struct_8 *field_c8;
} struct_8;

typedef struct struct_2 {
    char padding_0[40];
    struct struct_2 *field_28;
    char padding_30[152];
    struct struct_2 *field_c8;
} struct_2;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern long long g_1efcef8;
extern long long g_1efcf18;
extern long long g_1efcf38;
extern long long g_1efebb8;
extern long long g_1efebc0;
extern long long g_1efed20;
extern char g_1fab41c;

long long NPCAttack_OnEnable(struct_7 *ptr)
{
    struct_1 *v0;  // x0
    struct_7 *p;  // x20
    struct_7 *addr;  // x0
    struct_1 *v11;  // x1
    struct_7 *ptr4;  // x20
    struct_7 *ptr8;  // x20
    long long v14;  // x1
    struct_7 *ptr5;  // x0
    long long v16;  // x0
    struct_7 *ptr10;  // x19
    unsigned long v18;  // x0
    struct_7 *ptr9;  // x20
    struct_1 *cur;  // x0
    long long v4;  // x1
    struct_7 *ptr6;  // x0
    struct_9 *v6;  // x0
    struct_7 *ptr7;  // x20
    struct_7 *v8;  // x20
    long long v9;  // x1

    if (!(g_1fab41c & 1))
    {
        sub_f7d92c(&g_1efcef8);
        sub_f7d92c(&g_1efcf18);
        sub_f7d92c(&g_1efcf38);
        sub_f7d92c(&g_1efebb8);
        sub_f7d92c(&g_1efebc0);
        sub_f7d92c(&g_1efed20);
        sub_f7d92c(&g_1ef0c58);
        g_1fab41c = 1;
    }
    v0 = Component__get_transform(ptr, 0);
    p = ptr;
    p->field_40 = v0;
    ptr9 = &p->field_40;
    sub_f7d8d0(ptr9, v0);
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (((char)Object__op_Implicit(*((long long *)&ptr9->padding_60[24]), 0) & 1))
    {
        cur = ptr->field_b8;
        if (!cur)
            sub_f7db74(cur);
        v4 = Component__get_transform(cur, 0);
        ptr6 = ptr;
        ptr6->field_c0 = v4;
        sub_f7d8d0(&ptr6->field_c0, v4);
    }
    cur = *((long long *)&ptr9->padding_0[0]);
    if (cur)
    {
        v6 = sub_1231bc8(cur, g_1efcef8);
        ptr7 = ptr;
        ptr7->field_20 = v6;
        v8 = &ptr7->field_20;
        cur = sub_f7d8d0(v8, v6);
        if (*((long long *)&v8->padding_0[0]))
        {
            cur = *((long long *)(*((long long *)&v8->padding_0[0]) + 40));
            if (cur)
            {
                cur = sub_1249224(cur, g_1efebb8);
                if (cur)
                {
                    cur = cur->field_c8;
                    if (cur)
                    {
                        v9 = sub_1249224(cur, g_1efed20);
                        addr = ptr;
                        addr->field_28 = v9;
                        sub_f7d8d0(&addr->field_28, v9);
                        cur = Camera__get_main(0);
                        if (cur)
                        {
                            cur = Component__get_transform();
                            if (cur)
                            {
                                cur = sub_1231bc8();
                                if (cur)
                                {
                                    v11 = cur->field_28;
                                    ptr4 = ptr;
                                    ptr4->field_38 = v11;
                                    ptr8 = &ptr4->field_38;
                                    sub_f7d8d0(ptr8, v11);
                                    cur = *((long long *)&ptr8->padding_0[0]);
                                    if (cur)
                                    {
                                        v14 = sub_1249224(cur, g_1efebc0);
                                        ptr5 = ptr;
                                        ptr5->field_30 = v14;
                                        sub_f7d8d0(&ptr5->field_30, v14);
                                        v16 = sub_1231bc8(ptr, g_1efcf18);
                                        ptr->field_d8 = v16;
                                        ptr10 = &ptr->field_d8;
                                        v18 = sub_f7d8d0(ptr10, v16);
                                        *((unsigned int *)&ptr10->padding_0[8]) = *((int *)&ptr10->padding_60[28]) * 0xc0000000;
                                        return v18;
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    sub_f7db74(cur);
}
```

## `NPCAttack.Update` — RVA `0xc85c10`

- Decompiled symbol: `NPCAttack_Update`
- Metadata signature: `private void Update() { }`
- Native interval: `416` bytes
- Result: `pseudocode`
- Heuristic layout hint: `NPCAttack_Recovered` matched 4 offsets against `NPCAttack` metadata (confidence 1.00).

```c
typedef struct NPCAttack_Recovered {
    char padding_0[92];
    unsigned int fireRate;
    char padding_60[40];
    char shooting;
    char reloading;
    char padding_8a[86];
    unsigned int shootStartTime;
} NPCAttack_Recovered;

typedef struct struct_2 {
    char padding_0[48];
    unsigned long long field_30;
    char padding_38[16];
    struct struct_3 *field_48;
    char padding_50[56];
    unsigned long long field_88;
    char padding_90[424];
    unsigned long long field_238;
} struct_2;

typedef struct struct_1 {
    char padding_0[352];
    unsigned long long field_160;
} struct_1;

typedef struct struct_3 {
    char padding_0[352];
    unsigned long long field_160;
} struct_3;

extern struct_0 *g_1ef0c58;
extern char g_1fab41d;

long long NPCAttack_Update(struct_0 *ptr)
{
    long long v0;  // x0
    unsigned int v1;  // s1
    unsigned int v2;  // s0
    unsigned long v3;  // 4138
    struct_2 *v4;  // x8
    struct_2 *v5;  // x8
    long long v6;  // x0
    long long v7;  // x0
    long long v8;  // x0

    if (!(g_1fab41d & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab41d = 1;
    }
    v0 = Time__get_time(0);
    v1 = ptr->field_e0 + ptr->field_5c;
    v3 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v1, v2)) >> 5 & 3 | (unsigned long long)(CmpF(v1, v2) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v1, v2)) >> 5 & 3 | (unsigned long long)(CmpF(v1, v2) & 1)) & ((unsigned long long)(char)(CmpF(v1, v2)) >> 5 & 3 | (unsigned long long)(CmpF(v1, v2) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if (!((char)v3))
        ptr->field_88 = 0;
    if (ptr->padding_60[24])
    {
        *((unsigned int *)&ptr->padding_60[28]) = 0;
        ptr->padding_60[24] = 1;
        ptr->padding_60[32] = 0;
        return v0;
    }
    else if (*((int *)&ptr->padding_60[36]) + *((int *)&ptr->padding_60[0]) > *((int *)&ptr->padding_60[28]))
    {
        v4 = *((long long *)&ptr->padding_0[32]);
        if (v4)
        {
            if (!g_1ef0c58->field_e0)
                sub_f7da5c(g_1ef0c58);
            if (!((char)Object__op_Equality(v4->field_238, v4->field_30, 0) & 1))
            {
                v5 = *((long long *)&ptr->padding_0[32]);
                if (v5 && v5->field_48 && v5->field_48->field_160)
                {
                    v6 = GameObject__get_transform(v5->field_48->field_160, 0);
                    if (!g_1ef0c58->field_e0)
                        sub_f7da5c(g_1ef0c58);
                    if ((Object__op_Equality(v5->field_238, v6, 0) & 1))
                        goto LABEL_1085d10;
                    if (*((long long *)&ptr->padding_0[32]))
                    {
                        if (!g_1ef0c58->field_e0)
                            sub_f7da5c(g_1ef0c58);
                        v0 = Object__op_Implicit(*((long long *)(*((long long *)&ptr->padding_0[32]) + 136)), 0);
                        if (!((char)v0 & 1))
                        {
                            *((unsigned int *)&ptr->padding_60[28]) = 0;
                            ptr->padding_60[24] = 1;
                            ptr->padding_60[32] = 0;
                            return v0;
                        }
                        if (*((long long *)&ptr->padding_0[32]) && *((long long *)(*((long long *)&ptr->padding_0[32]) + 136)))
                        {
                            v0 = Behaviour__get_enabled(*((long long *)(*((long long *)&ptr->padding_0[32]) + 136)), 0);
                            if (!((char)v0 & 1))
                            {
                                *((unsigned int *)&ptr->padding_60[28]) = 0;
                                ptr->padding_60[24] = 1;
                                ptr->padding_60[32] = 0;
                                return v0;
                            }
                            goto LABEL_1085d10;
                        }
                    }
                }
            }
            else
            {
LABEL_1085d10:
                v7 = NPCAttack__Fire(ptr);
                if (ptr->padding_60[32])
                    return v7;
                v8 = Random__Range(0, *((int *)&ptr->padding_60[4]), 0);
                *((int *)&ptr->padding_60[36]) = v8;
                ptr->padding_60[32] = 1;
                return v8;
            }
        }
        sub_f7db74();
    }
    else
    {
        *((unsigned int *)&ptr->padding_60[28]) = 0;
        ptr->padding_60[24] = 1;
        ptr->padding_60[32] = 0;
        return v0;
    }
}
```

## `NPCAttack.LateUpdate` — RVA `0xc85db0`

- Decompiled symbol: `NPCAttack_LateUpdate`
- Metadata signature: `private void LateUpdate() { }`
- Native interval: `220` bytes
- Result: `pseudocode`
- Heuristic layout hint: `NPCAttack_Recovered` matched 4 offsets against `NPCAttack` metadata (confidence 1.00).

```c
typedef struct NPCAttack_Recovered {
    char padding_0[92];
    unsigned int fireRate;
    char padding_60[42];
    char mFlashState;
    char padding_8b[45];
    unsigned long long muzzleFlash;
    char padding_c0[32];
    unsigned int shootStartTime;
} NPCAttack_Recovered;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab41e;

long long NPCAttack_LateUpdate(struct_1 *ptr)
{
    unsigned long v0;  // x0
    unsigned long v1;  // x0
    unsigned long v10;  // x0
    long long v11;  // x0
    unsigned int v2;  // s1
    unsigned int v3;  // s2
    unsigned int v4;  // w8
    unsigned int v5;  // s0
    unsigned long v6;  // d0
    unsigned long long v7;  // d1
    unsigned long v8;  // 4175
    unsigned long long v9;  // x0

    if (!(g_1fab41e & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab41e = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v0 = Object__op_Implicit(ptr->field_b8, 0);
    if (!((char)v0 & 1))
        return v0;
    v1 = Time__get_time(0);
    v2 = ptr->field_e0;
    v3 = ptr->field_5c;
    v4 = ptr->field_8a;
    v6 = v5 - ptr->field_e0;
    v7 = ptr->field_5c * 4599616371426034975;
    v8 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v7, v6)) >> 5 & 3 | (unsigned long long)(CmpF((unsigned long long)v3 * 4599616371426034975, (unsigned long long)(v5 - v2)) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF((unsigned long long)v3 * 4599616371426034975, (unsigned long long)(v5 - v2))) >> 5 & 3 | (unsigned long long)(CmpF((unsigned long long)v3 * 4599616371426034975, (unsigned long long)(v5 - v2)) & 1)) & ((unsigned long long)(char)(CmpF((unsigned long long)v3 * 4599616371426034975, (unsigned long long)(v5 - v2))) >> 5 & 3 | (unsigned long long)(CmpF((unsigned long long)v3 * 4599616371426034975, (unsigned long long)(v5 - v2)) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if (!((char)v8))
    {
        if (v4)
        {
            v9 = ptr->field_b8;
            if (v9)
            {
                v10 = Renderer__set_enabled(v9, 1, 0);
                ptr->field_8a = 0;
                return v10;
            }
        }
        else
        {
            return v1;
        }
    }
    else
    {
        if (v4)
            return v1;
        v9 = ptr->field_b8;
        if (v9)
        {
            v11 = Renderer__set_enabled();
            return Renderer__set_enabled();
        }
    }
    sub_f7db74(v9);
}
```

## `NPCAttack.FireOneShot` — RVA `0xc85e8c`

- Decompiled symbol: `NPCAttack_FireOneShot`
- Metadata signature: `private void FireOneShot() { }`
- Native interval: `4144` bytes
- Result: `pseudocode`
- Heuristic layout hint: `NPCAttack_Recovered` matched 20 offsets against `NPCAttack` metadata (confidence 0.77).

```c
typedef struct NPCAttack_Recovered {
    char padding_0[32];
    struct struct_2 *AIComponent;
    unsigned long long WeaponEffectsComponent;
    struct struct_5 *FPSWalker;
    char padding_38[8];
    long long myTransform;
    unsigned int targetPos;
    unsigned int field_4c;
    unsigned int field_50;
    char padding_54[4];
    unsigned int inaccuracy;
    char padding_5c[12];
    unsigned int force;
    unsigned int damage;
    char isMeleeAttack;
    char padding_71[3];
    unsigned int damageAmt;
    char padding_78[4];
    unsigned int shotsFired;
    char padding_80[10];
    char mFlashState;
    char padding_8b[1];
    unsigned int rayOrigin;
    unsigned int field_90;
    unsigned int field_94;
    unsigned int targetDir;
    unsigned int field_9c;
    unsigned int field_a0;
    char padding_a4[4];
    struct struct_3 *hits;
    char hitObject;
    char padding_b1[15];
    long long muzzleFlashTransform;
    long long firesnd;
    unsigned int fireFxRandPitch;
    char padding_d4[4];
    unsigned long long aSource;
} NPCAttack_Recovered;

typedef struct struct_2 {
    char padding_0[40];
    long long field_28;
    char padding_30[88];
    long long field_88;
    char padding_90[412];
    unsigned int field_22c;
    char padding_230[76];
    unsigned int field_27c;
    char padding_280[4];
    unsigned int field_284;
    unsigned int field_288;
    unsigned int field_28c;
    char padding_290[12];
    unsigned int field_29c;
} struct_2;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

typedef struct struct_8 {
    char padding_0[24];
    unsigned int field_18;
} struct_8;

typedef struct struct_3 {
    char padding_0[24];
    unsigned int field_18;
} struct_3;

typedef struct struct_9 {
    uint128_t field_0;
    uint128_t field_10;
    unsigned long long field_20;
    unsigned int field_28;
} struct_9;

typedef struct struct_5 {
    char padding_0[720];
    char field_2d0;
    char padding_2d1[11];
    char field_2dc;
} struct_5;

typedef struct struct_7 {
    unsigned int field_0;
    unsigned int field_4;
    unsigned int field_8;
} struct_7;

typedef struct struct_6 {
    char padding_0[184];
    struct struct_7 *field_b8;
} struct_6;

extern struct_6 *g_1ef22e8;
extern char g_1fab2c9;

long long NPCAttack_FireOneShot(struct_4 *ptr)
{
    uint128_t v6;  // q0
    struct_0 **v7;  // x22
    int v19;  // q2
    long long v65;  // x0
    long long v66;  // x0
    unsigned int v67;  // w0
    long long v68;  // x0
    unsigned int v69;  // w0
    long long v70;  // x0
    long long v71;  // x0
    unsigned long v72;  // x0
    int v73;  // q8
    unsigned long v74;  // x20
    long long v75;  // x0
    unsigned long v76;  // x0
    int v77;  // q8
    unsigned long v78;  // x20
    uint128_t v1;  // [bp-0xa0]

    if (!RaycastHit__get_collider(&v1, 0))
        goto LABEL_0x108639c;
    if (!Component__get_gameObject())
        goto LABEL_0x108639c;
    v65 = sub_1249224();
    if (!*(v7)->field_e0)
        sub_f7da5c(*(v7));
    if (((char)Object__op_Implicit(v65, 0) & 1))
    {
        if (!RaycastHit__get_collider(&v1, 0))
            goto LABEL_0x108639c;
        if (!Component__get_gameObject())
            goto LABEL_0x108639c;
        if (!sub_1249224())
            goto LABEL_0x108639c;
        v6 = ptr->field_74;
        AppleFall__ApplyDamage();
    }
    if (!RaycastHit__get_collider(&v1, 0))
        goto LABEL_0x108639c;
    if (!Component__get_gameObject())
        goto LABEL_0x108639c;
    v66 = sub_1249224();
    if (!*(v7)->field_e0)
        sub_f7da5c(*(v7));
    v67 = Object__op_Implicit(v66, 0);
    if (!RaycastHit__get_collider(&v1, 0))
        goto LABEL_0x108639c;
    if (!Component__get_gameObject())
        goto LABEL_0x108639c;
    if (((char)v67 & 1))
    {
        if (!sub_1249224())
            goto LABEL_0x108639c;
        v6 = ptr->field_74;
        BreakableObject__ApplyDamage();
    }
    else
    {
        v68 = sub_1249224();
        if (!*(v7)->field_e0)
            sub_f7da5c(*(v7));
        v69 = Object__op_Implicit(v68, 0);
        if (!RaycastHit__get_collider(&v1, 0))
            goto LABEL_0x108639c;
        if (!Component__get_gameObject())
            goto LABEL_0x108639c;
        if (((char)v69 & 1))
        {
            if (!sub_1249224())
                goto LABEL_0x108639c;
            v6 = ptr->field_74;
            ExplosiveObject__ApplyDamage();
        }
        else
        {
            v70 = sub_1249224();
            if (!*(v7)->field_e0)
                sub_f7da5c(*(v7));
            if (((char)Object__op_Implicit(v70, 0) & 1))
            {
                if (!RaycastHit__get_collider(&v1, 0))
                    goto LABEL_0x108639c;
                if (!Component__get_gameObject())
                    goto LABEL_0x108639c;
                if (!sub_1249224())
                    goto LABEL_0x108639c;
                v6 = ptr->field_74;
                MineExplosion__ApplyDamage();
            }
        }
    }
    if (!RaycastHit__get_collider(&v1, 0))
        goto LABEL_0x108639c;
    if (!Component__get_gameObject())
        goto LABEL_0x108639c;
    v71 = sub_1249224();
    if (!*(v7)->field_e0)
        sub_f7da5c(*(v7));
    if (((char)Object__op_Implicit(v71, 0) & 1))
    {
        if (!RaycastHit__get_collider(&v1, 0))
            goto LABEL_0x108639c;
        if (!Component__get_gameObject())
            goto LABEL_0x108639c;
        v72 = sub_1249224();
        v73 = (int)ptr->field_74;
        v74 = v72;
        if (!g_1fab2c9)
        {
            sub_f7d92c(&g_1ef22e8);
            g_1fab2c9 = 1;
        }
        if (!ptr->field_40)
            goto LABEL_0x108639c;
        Transform__get_position(ptr->field_40, 0);
        if (!v74)
            goto LABEL_0x108639c;
        v6 = (uint128_t)v73;
        v19 = (int)g_1ef22e8->field_b8->field_4;
        CharacterDamage__ApplyDamage(v74, ptr->field_40, 0, 0, 0);
    }
    if (!RaycastHit__get_collider(&v1, 0))
        goto LABEL_0x108639c;
    if (!Component__get_gameObject())
        goto LABEL_0x108639c;
    v75 = sub_1249224();
    if (!*(v7)->field_e0)
        sub_f7da5c(*(v7));
    if (!(Object__op_Implicit(v75, 0) & 1))
        goto LABEL_0x1086dd8;
    if (!RaycastHit__get_collider(&v1, 0))
        goto LABEL_0x108639c;
    if (!Component__get_gameObject())
        goto LABEL_0x108639c;
    v76 = sub_1249224();
    v77 = (int)ptr->field_74;
    v78 = v76;
    if (!g_1fab2c9)
    {
        sub_f7d92c(&g_1ef22e8);
        g_1fab2c9 = 1;
    }
    if (!ptr->field_40)
        goto LABEL_0x108639c;
    Transform__get_position(ptr->field_40, 0);
    if (!v78)
        goto LABEL_0x108639c;
    v6 = (uint128_t)v77;
    v19 = (int)g_1ef22e8->field_b8->field_4;
    LocationDamage__ApplyDamage(v78, ptr->field_40, 0, 0);
}
```

## `NPCAttack.ctor` — RVA `0xc86ebc`

- Decompiled symbol: `NPCAttack_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `64` bytes
- Result: `pseudocode`
- Heuristic layout hint: `NPCAttack_Recovered` matched 5 offsets against `NPCAttack` metadata (confidence 1.00).

```c
typedef struct NPCAttack_Recovered {
    char padding_0[84];
    unsigned long long range;
    unsigned int fireRate;
    char padding_60[8];
    unsigned long long force;
    char padding_70[8];
    char doneShooting;
    char padding_79[87];
    unsigned int fireFxRandPitch;
} NPCAttack_Recovered;

long long NPCAttack_ctor(struct_0 *ptr)
{
    *((unsigned int *)((char *)&ptr->field_54 + 4)) = 1036429296;
    ptr->padding_70[0] = 1;
    *((unsigned long long *)&(&ptr->padding_0)[1]) = 0x3f00000042c80000;
    *((unsigned long long *)&ptr->padding_60[4]) = 0x4120000041a00000;
    *((unsigned int *)&ptr->padding_79[79]) = 1063004406;
}
```
