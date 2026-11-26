# Native pseudocode: CharacterDamage

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `CharacterDamage.OnEnable` — RVA `0xc8248c`

- Decompiled symbol: `CharacterDamage_OnEnable`
- Metadata signature: `private void OnEnable() { }`
- Native interval: `368` bytes
- Result: `pseudocode`
- Heuristic layout hint: `CharacterDamage_Recovered` matched 7 offsets against `CharacterDamage` metadata (confidence 1.00).

```c
typedef struct CharacterDamage_Recovered {
    char padding_0[48];
    long long AIComponent;
    long long RemoveBodyComponent;
    unsigned int hitPoints;
    unsigned int initialHitPoints;
    char padding_48[48];
    long long bodies;
    char padding_80[33];
    char removeBody;
    char padding_a2[54];
    long long myTransform;
} CharacterDamage_Recovered;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern long long g_1efcef8;
extern long long g_1efd068;
extern long long g_1efd1c8;
extern char g_1fab406;

void CharacterDamage_OnEnable(struct_1 *ptr)
{
    unsigned long long v6;  // x30
    unsigned long long v7;  // x23
    struct_1 *p;  // x21
    struct_1 *ptr3;  // x21
    long long v18;  // x0
    struct_1 *v19;  // x21
    struct_1 *ptr4;  // x21
    long long v21;  // x0
    unsigned long long v8;  // x22
    unsigned long long v9;  // x21
    unsigned long long v10;  // x20
    unsigned long long v11;  // x19
    long long v12;  // x0
    struct_1 *addr;  // x20
    struct_1 *ptr5;  // x20
    long long v15;  // x0
    unsigned long long v0;  // [bp-0x30]
    unsigned long long v1;  // [bp-0x28]
    unsigned long long v2;  // [bp-0x20]
    unsigned long long v3;  // [bp-0x18]
    unsigned long long v4;  // [bp-0x10]
    unsigned long long v5;  // [bp-0x8]

    v0 = v6;
    v1 = v7;
    v2 = v8;
    v3 = v9;
    v4 = v10;
    v5 = v11;
    if (!(g_1fab406 & 1))
    {
        sub_f7d92c(&g_1efcef8);
        sub_f7d92c(&g_1efd068);
        sub_f7d92c(&g_1efd1c8);
        sub_f7d92c(&g_1ef0c58);
        g_1fab406 = 1;
    }
    v12 = Component__get_transform(ptr, 0);
    addr = ptr;
    addr->field_d8 = v12;
    ptr5 = &addr->field_d8;
    sub_f7d8d0(ptr5, v12);
    v15 = sub_1231bc8(ptr, g_1efd068);
    p = ptr;
    p->field_38 = v15;
    ptr3 = &p->field_38;
    sub_f7d8d0(ptr3, v15);
    if (ptr3->padding_48[33])
    {
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        if (((char)Object__op_Implicit(*((long long *)&ptr3->padding_0[0]), 0) & 1))
        {
            v18 = *((long long *)&ptr3->padding_0[0]);
            if (!v18)
                goto LABEL_10825f8;
            Behaviour__set_enabled(v18, 0, 0);
        }
    }
    v19 = ptr;
    ptr4 = &v19->field_30;
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (!((char)Object__op_Implicit(v19->field_30, 0) & 1))
    {
        v18 = *((long long *)&ptr5->padding_0[0]);
        if (!v18)
        {
LABEL_10825f8:
            sub_f7db74(v18);
        }
        v21 = sub_1231bc8(v18, g_1efcef8);
        *((long long *)&ptr4->padding_0[0]) = v21;
        sub_f7d8d0(ptr4, v21);
    }
    ptr->field_44 = ptr->field_40;
    ptr->field_78 = sub_1232400(ptr, g_1efd1c8);
    sub_f7d8d0();
    return;
}
```


## `CharacterDamage.Start` — RVA `0xc825fc`

- Decompiled symbol: `CharacterDamage_Start`
- Metadata signature: `private void Start() { }`
- Native interval: `144` bytes
- Result: `pseudocode`

```c
typedef struct struct_3 {
    char padding_0[32];
    long long field_20;
} struct_3;

extern long long g_1efd0f8;
extern char g_1fab407;

void CharacterDamage_Start(struct_3 *ptr)
{
    unsigned long long v5;  // x30
    unsigned long long v6;  // x22
    unsigned long long v7;  // x21
    unsigned long long v8;  // x20
    unsigned long long v9;  // x19
    unsigned long long v0;  // [bp-0x30]
    unsigned long long v1;  // [bp-0x20]
    unsigned long long v2;  // [bp-0x18]
    unsigned long long v3;  // [bp-0x10]
    unsigned long long v4;  // [bp-0x8]

    v0 = v5;
    v1 = v6;
    v2 = v7;
    v3 = v8;
    v4 = v9;
    if (!(g_1fab407 & 1))
    {
        sub_f7d92c("72");
        sub_f7d92c(&g_1efd0f8);
        g_1fab407 = 1;
    }
    g_1eeee18->field_b8->field_0 = ptr;
    sub_f7d8d0(g_1eeee18->field_b8, ptr);
    ptr->field_20 = sub_1231bc8(ptr, g_1efd0f8);
    sub_f7d8d0();
    return;
}
```


## `CharacterDamage.Update` — RVA `0xc8268c`

- Decompiled symbol: `CharacterDamage_Update`
- Metadata signature: `private void Update() { }`
- Native interval: `1420` bytes
- Result: `pseudocode`
- Heuristic layout hint: `CharacterDamage_Recovered` matched 8 offsets against `CharacterDamage` metadata (confidence 1.00).

```c
typedef struct CharacterDamage_Recovered {
    char padding_0[48];
    struct struct_4 *AIComponent;
    char padding_38[24];
    long long gunItem;
    long long gunObj;
    long long gunInst;
    char padding_68[16];
    struct struct_5 *bodies;
    char ragdollActive;
    char ragdollState;
    char padding_82[38];
    unsigned int gunStayTime;
} CharacterDamage_Recovered;

typedef struct struct_7 {
    char padding_0[24];
    unsigned int field_18;
} struct_7;

typedef struct struct_9 {
    char padding_0[72];
    struct struct_10 *field_48;
    char padding_50[72];
    void* field_98;
    char padding_a0[16];
    unsigned long long field_b0;
} struct_9;

typedef struct struct_8 {
    char padding_0[568];
    unsigned long long field_238;
} struct_8;

typedef struct struct_2 {
    char padding_0[32];
    long long field_20;
} struct_2;

typedef struct struct_4 {
    char padding_0[72];
    struct struct_3 *field_48;
    char padding_50[72];
    void* field_98;
    char padding_a0[16];
    long long field_b0;
} struct_4;

typedef struct struct_5 {
    char padding_0[24];
    int field_18;
} struct_5;

typedef struct struct_10 {
    char padding_0[568];
    unsigned long long field_238;
} struct_10;

typedef struct struct_3 {
    char padding_0[568];
    long long field_238;
} struct_3;

typedef struct struct_1 {
    char padding_0[224];
    unsigned int field_e0;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern struct_1 *g_1ef0e48;
extern long long g_1efeb98;
extern long long g_1efed28;
extern long long g_1f00260;
extern char g_1fab408;

struct_6 * CharacterDamage_Update(struct_6 *ptr, unsigned long a1, unsigned long a2, unsigned long a3, unsigned long a4)
{
    struct_6 *v0;  // x0
    struct_6 *v1;  // x0
    unsigned int v10;  // w8
    unsigned int j;  // w21
    struct_2 *v12;  // x8
    struct_6 *v13;  // x0
    long long v14;  // x0
    struct_6 *v15;  // x20
    void* p;  // x24
    unsigned long k;  // x25
    unsigned int v18;  // w8
    long long v19;  // x0
    struct_6 *v2;  // x0
    unsigned int v20;  // s0
    unsigned long v21;  // 4129
    long long v22;  // x0
    unsigned long v23;  // x0
    unsigned long v24;  // x20
    long long v25;  // x0
    unsigned long long v26;  // x21
    unsigned long v27;  // x22
    struct_6 *v28;  // x0
    struct_7 *addr;  // x20
    unsigned int v4;  // w8
    unsigned int v5;  // w9
    void* ptr3;  // x22
    unsigned long i;  // x23
    unsigned int v8;  // w8
    struct_7 *ptr4;  // x20

    v0 = ptr;
    if (!(g_1fab408 & 1))
    {
        sub_f7d92c(&g_1efeb98);
        sub_f7d92c(&g_1efed28);
        sub_f7d92c(&g_1f00260);
        sub_f7d92c(&g_1ef0c58);
        v1 = sub_f7d92c(&g_1ef0e48);
        g_1fab408 = 1;
        v0 = v1;
    }
    addr = ptr->field_78;
    if (addr)
    {
        v4 = addr->field_18;
        if (addr->field_18 < 2)
            return v0;
        v5 = ptr->field_81;
        if (ptr->field_80)
        {
            if (!v5)
            {
                return v0;
            }
            else if (ptr->field_30 && ptr->field_30->field_b0)
            {
                v2 = Behaviour__set_enabled(ptr->field_30->field_b0, 0, 0);
                if (ptr->field_30)
                {
                    ptr3 = ptr->field_30->field_98;
                    if (ptr3)
                    {
                        if ((int)(long long)ptr3[24] >= 1)
                        {
                            i = 0;
                            v8 = (long long)ptr3[24];
                            do
                            {
                                if (v8 <= i)
                                    sub_f7db7c(v2);
                                if (!ptr->field_30)
                                    sub_f7db7c(sub_f7db74());
                                if (!ptr->field_30->field_48)
                                    sub_f7db7c(sub_f7db74());
                                if (!Component__get_gameObject(ptr->field_30->field_48, 0))
                                    sub_f7db7c(sub_f7db74());
                                v2 = GameObject__get_activeInHierarchy();
                                if (((char)v2 & 1))
                                {
                                    if (!ptr->field_30)
                                    {
                                        sub_f7db7c(sub_f7db74());
                                    }
                                    else if (ptr->field_30->field_48)
                                    {
                                        if (!g_1ef0e48->field_e0)
                                            sub_f7da5c(g_1ef0e48);
                                        v2 = Physics__IgnoreCollision(*((long long *)(32 + (char *)ptr3 + 8 * i)), ptr->field_30->field_48->field_238, 1, 0);
                                    }
                                    else
                                    {
                                        sub_f7db7c(sub_f7db74());
                                    }
                                }
                                v8 = (int)ptr3[24];
                                i += 1;
                            } while (i < v8);
                        }
                        ptr4 = ptr->field_78;
                        if (ptr4)
                        {
                            v10 = ptr4->field_18;
                            if (ptr4->field_18 >= 1)
                            {
                                j = 0;
                                do
                                {
                                    if (v10 <= j)
                                        sub_f7db7c(v2);
                                    v12 = &ptr4->padding_0[8 * j];
                                    if (!v12->field_20)
                                        sub_f7db7c(sub_f7db74());
                                    v2 = Rigidbody__set_isKinematic(v12->field_20, 0, 0);
                                    v10 = ptr4->field_18;
                                    j += 1;
                                } while (j < v10);
                            }
                            if (!g_1ef0c58->field_e0)
                                sub_f7da5c(g_1ef0c58);
                            v13 = Object__op_Implicit(ptr->field_58, 0);
                            if (!((char)v13 & 1))
                            {
                                ptr->field_81 = 0;
                                return v13;
                            }
                            else if (ptr->field_58 && Component__get_gameObject(ptr->field_58, 0))
                            {
                                GameObject__SetActive();
                                if (ptr->field_58)
                                {
                                    Transform__get_position(ptr->field_58, 0);
                                    if (ptr->field_58)
                                    {
                                        Transform__get_rotation(ptr->field_58, 0);
                                        if (!g_1ef0c58->field_e0)
                                            sub_f7da5c(g_1ef0c58);
                                        v14 = sub_112a1ac(ptr->field_50, g_1f00260);
                                        ptr->field_60 = v14;
                                        v15 = &ptr->field_60;
                                        v2 = sub_f7d8d0(v15, v14);
                                        if (v15->field_30)
                                        {
                                            p = v15->field_30->field_98;
                                            if (p)
                                            {
                                                if ((int)(long long)p[24] >= 1)
                                                {
                                                    k = 0;
                                                    v18 = (long long)p[24];
                                                    do
                                                    {
                                                        if (v18 <= k)
                                                            sub_f7db7c(v2);
                                                        if (!*((long long *)&v15->padding_0[0]))
                                                            sub_f7db7c(sub_f7db74());
                                                        v19 = sub_1249224(*((long long *)&v15->padding_0[0]), g_1efeb98);
                                                        if (!g_1ef0e48->field_e0)
                                                            sub_f7da5c(g_1ef0e48);
                                                        v2 = Physics__IgnoreCollision(*((long long *)(32 + (char *)p + 8 * k)), v19, 1, 0);
                                                        v18 = (int)p[24];
                                                        k += 1;
                                                    } while (k < v18);
                                                }
                                                if (*((long long *)&v15->padding_0[0]) && GameObject__get_transform(*((long long *)&v15->padding_0[0]), 0))
                                                {
                                                    Transform__Rotate();
                                                    if (ptr->field_60 && GameObject__get_transform(ptr->field_60, 0))
                                                    {
                                                        Transform__get_position();
                                                        if (Component__get_transform(ptr, 0))
                                                        {
                                                            Transform__get_forward();
                                                            if (*((long long *)&v15->padding_0[0]) && GameObject__get_transform(*((long long *)&v15->padding_0[0]), 0))
                                                            {
                                                                v13 = Transform__set_position();
                                                                v20 = ptr->field_a8;
                                                                v21 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v20, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v20, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v20, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v20, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v20, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v20, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                                                                if ((char)v21)
                                                                {
                                                                    ptr->field_81 = 0;
                                                                    return v13;
                                                                }
                                                                else if (*((long long *)&v15->padding_0[0]))
                                                                {
                                                                    v22 = sub_1249224(*((long long *)&v15->padding_0[0]), g_1efed28);
                                                                    if (!g_1ef0c58->field_e0)
                                                                        sub_f7da5c(g_1ef0c58);
                                                                    v13 = Object__op_Implicit(v22, 0);
                                                                    if (!((char)v13 & 1))
                                                                    {
                                                                        ptr->field_81 = 0;
                                                                        return v13;
                                                                    }
                                                                    else if (*((long long *)&v15->padding_0[0]))
                                                                    {
                                                                        v23 = sub_1249224(*((long long *)&v15->padding_0[0]), g_1efed28);
                                                                        if (*((long long *)&v15->padding_0[0]))
                                                                        {
                                                                            v24 = v23;
                                                                            if (sub_1249224(*((long long *)&v15->padding_0[0]), g_1efed28))
                                                                            {
                                                                                v25 = WeaponPickup__DestroyWeapon();
                                                                                if (v24)
                                                                                {
                                                                                    v13 = MonoBehaviour__StartCoroutine(v24, v25, 0);
                                                                                    ptr->field_81 = 0;
                                                                                    return v13;
                                                                                }
                                                                            }
                                                                        }
                                                                    }
                                                                }
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
        else
        {
            if (!v5)
            {
                v26 = 0;
                v27 = &addr[1].padding_0[4];
                while (true)
                {
                    if (v4 <= (unsigned int)v26)
                        sub_f7db7c(v2);
                    if (!*((long long *)(v27 + v26 * 8)))
                        break;
                    v2 = Rigidbody__set_isKinematic(*((long long *)(v27 + v26 * 8)), 1, 0);
                    v4 = addr->field_18;
                    v26 += 1;
                    if ((unsigned int)v26 >= v4)
                    {
                        if (!ptr->field_30 || !ptr->field_30->field_b0)
                            break;
                        Behaviour__set_enabled(ptr->field_30->field_b0, 1, 0);
                        if (!g_1ef0c58->field_e0)
                            sub_f7da5c(g_1ef0c58);
                        v28 = Object__op_Implicit(ptr->field_58, 0);
                        if (((char)v28 & 1))
                        {
                            if (!ptr->field_58 || !Component__get_gameObject(ptr->field_58, 0))
                                break;
                            GameObject__SetActive();
                            if (!g_1ef0c58->field_e0)
                                sub_f7da5c(g_1ef0c58);
                            v28 = Object__op_Implicit(ptr->field_60, 0);
                            if (((char)v28 & 1))
                            {
                                if (!g_1ef0c58->field_e0)
                                    sub_f7da5c(g_1ef0c58);
                                v28 = Object__Destroy(ptr->field_60, 0);
                            }
                        }
                        ptr->field_81 = 1;
                        return v28;
                        break;
                    }
                }
            }
            else
            {
                return v0;
            }
        }
    }
    sub_f7db7c(sub_f7db74());
}
```


## `CharacterDamage.ApplyDamage` — RVA `0xc82c18`

- Decompiled symbol: `CharacterDamage_ApplyDamage`
- Metadata signature: `public void ApplyDamage(float damage, Vector3 attackDir, Vector3 attackerPos, Transform attacker, bool isPlayer, bool isExplosion, Rigidbody hitBody, float bodyForce = 0.0) { }`
- Native interval: `1672` bytes
- Result: `pseudocode`
- Heuristic layout hint: `CharacterDamage_Recovered` matched 2 offsets against `CharacterDamage` metadata (confidence 1.00).

```c
typedef struct struct_9 {
    char padding_0[48];
    struct struct_8 *field_30;
    char padding_38[8];
    unsigned int field_40;
    unsigned int field_44;
    char padding_48[104];
    char field_b0;
    char padding_b1[7];
    unsigned int field_b8;
    unsigned int field_bc;
    unsigned int field_c0;
    unsigned int field_c4;
    unsigned int field_c8;
    unsigned int field_cc;
    unsigned int field_d0;
    char padding_d4[12];
    char field_e0;
    char padding_e1[7];
    long long field_e8;
} struct_9;

typedef struct struct_15 {
    char padding_0[40];
    unsigned long long field_28;
    char padding_30[24];
    struct struct_13 *field_48;
    char padding_50[8];
    struct struct_11 *field_58;
    char padding_60[40];
    struct struct_14 *field_88;
    char padding_90[96];
    unsigned int field_f0;
    char field_f4;
    char field_f5;
    char padding_f6[2];
    unsigned int field_f8;
    char padding_fc[24];
    char field_114;
    char padding_115[291];
    unsigned long long field_238;
    char padding_240[57];
    char field_279;
    char padding_27a[2];
    unsigned int field_27c;
    char padding_280[22];
    char field_296;
} struct_15;

typedef struct struct_13 {
    char padding_0[568];
    unsigned long long field_238;
} struct_13;

typedef struct struct_14 {
    char padding_0[556];
    unsigned int field_22c;
} struct_14;

typedef struct struct_3 {
    char padding_0[556];
    unsigned int field_22c;
} struct_3;

typedef struct struct_11 {
    char padding_0[144];
    unsigned long long field_90;
    struct struct_12 *field_98;
} struct_11;

typedef struct struct_10 {
    char padding_0[516];
    unsigned int field_204;
    char padding_208[33];
    char field_229;
} struct_10;

typedef struct struct_8 {
    char padding_0[40];
    long long field_28;
    char padding_30[24];
    struct struct_4 *field_48;
    char padding_50[8];
    struct CharacterDamage_Recovered *field_58;
    char padding_60[40];
    struct struct_7 *field_88;
    char padding_90[96];
    unsigned int field_f0;
    char field_f4;
    char field_f5;
    char padding_f6[2];
    unsigned int field_f8;
    char padding_fc[24];
    char field_114;
    char padding_115[291];
    long long field_238;
    char padding_240[57];
    char field_279;
    char padding_27a[2];
    unsigned int field_27c;
    char padding_280[22];
    char field_296;
} struct_8;

typedef struct struct_12 {
    char padding_0[516];
    unsigned int field_204;
    char padding_208[33];
    char field_229;
} struct_12;

typedef struct struct_4 {
    char padding_0[568];
    long long field_238;
} struct_4;

typedef struct CharacterDamage_Recovered {
    char padding_0[144];
    long long dead;
    struct struct_5 *dieSound;
} CharacterDamage_Recovered;

typedef struct struct_7 {
    char padding_0[556];
    unsigned int field_22c;
} struct_7;

typedef struct struct_5 {
    char padding_0[516];
    unsigned int field_204;
    char padding_208[33];
    char field_229;
} struct_5;

typedef struct struct_0 {
    unsigned int field_0;
    char padding_4[4];
    long long field_8;
} struct_0;

typedef struct struct_1 {
    char padding_0[184];
    struct struct_0 *field_b8;
} struct_1;

typedef struct struct_2 {
    char padding_0[224];
    unsigned int field_e0;
} struct_2;

extern struct_1 *g_1eefae8;
extern struct_2 *g_1ef0c58;
extern long long g_1efcef8;
extern long long g_1f0bd20;
extern long long g_1f14d40;
extern char g_1fab409;

struct_9 * CharacterDamage_ApplyDamage(struct_9 *ptr, long long a1, unsigned int a2, unsigned int a3, unsigned long a4)
{
    unsigned long v0;  // x22
    struct_9 *v1;  // x0
    long long v10;  // x1
    struct_15 *ptr3;  // x23
    struct_15 *ptr4;  // x0
    unsigned long ptr5;  // x0
    long long v14;  // x0
    struct_15 *ptr6;  // x8
    struct_15 *ptr7;  // x24
    struct_3 *v17;  // x0
    struct_15 *p;  // x8
    unsigned int v19;  // s0
    struct_9 *v2;  // x0
    unsigned int v20;  // s0
    unsigned int v21;  // s0
    unsigned int v22;  // s1
    unsigned long v23;  // 4142
    struct_15 *ptr8;  // x8
    struct_11 *addr;  // x8
    struct_10 *ptr9;  // x9
    unsigned int v27;  // s2
    unsigned long v28;  // 4129
    unsigned int v29;  // w10
    struct_9 *v3;  // x0
    unsigned long v30;  // x23
    struct_15 *ptr10;  // x22
    unsigned int v33;  // s2
    unsigned int v34;  // s3
    unsigned int v35;  // s4
    unsigned int v36;  // s5
    unsigned int v37;  // s6
    unsigned int v38;  // s1
    struct_9 *v39;  // x0
    unsigned int v4;  // s0
    unsigned int v40;  // s0
    unsigned long v41;  // 4129
    unsigned long v42;  // 4125
    unsigned long v5;  // 4129
    struct_15 *v6;  // x8
    unsigned int v7;  // s0
    unsigned long v8;  // 4146
    struct_15 *ptr11;  // x23

    v0 = a3;
    v1 = ptr;
    if (!(g_1fab409 & 1))
    {
        sub_f7d92c(&g_1efcef8);
        sub_f7d92c(&g_1eefae8);
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c(&g_1f14d40);
        v2 = sub_f7d92c(&g_1f0bd20);
        g_1fab409 = 1;
        v1 = v2;
    }
    v3 = v1;
    v4 = ptr->field_40;
    v5 = arm64g_calculate_condition(144, (((((unsigned long long)(char)(CmpF(v4, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v4, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v4, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v4, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v4, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v4, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if ((char)v5)
        return v3;
    v6 = ptr->field_30;
    if (v6)
    {
        if (!v6->field_296 && !v6->field_114 && (v7 = v4 / ptr->field_44, v8 = (unsigned long)arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v7, 1059481190)) >> 5 & 3 | (unsigned long long)(CmpF(v7, 1059481190) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v7, 1059481190)) >> 5 & 3 | (unsigned long long)(CmpF(v7, 1059481190) & 1)) & ((unsigned long long)(char)(CmpF(v7, 1059481190)) >> 5 & 3 | (unsigned long long)(CmpF(v7, 1059481190) & 1)) >> 1 & 1)) * 0x10000000, 0, 0), !((char)v8)))
        {
            if (!g_1ef0c58->field_e0)
                sub_f7da5c(g_1ef0c58);
            if (!((char)Object__op_Implicit(a1, 0) & 1) || ((char)v0 & 1))
                goto LABEL_1082e38;
            if (((char)a2 & 1))
            {
                ptr11 = ptr->field_30;
                if (ptr11)
                {
                    if (ptr11->field_f4)
                        goto LABEL_1082e38;
                    if (ptr11->field_28)
                    {
                        v10 = GameObject__get_transform(ptr11->field_28, 0);
                        ptr11->field_238 = v10;
                        sub_f7d8d0(&ptr11->field_238, v10);
                        ptr3 = ptr->field_30;
                        if (ptr3 && ptr3->field_48 && ptr3->field_48->field_238 && (CapsuleCollider__get_height(ptr3->field_48->field_238, 0), ptr3->field_27c = v7 * 0x3e800000, ptr4 = (struct_15 *)ptr->field_30, ptr4 && (ptr4->field_88 = (struct struct_14 *)NULL, ptr5 = (unsigned long)(ptr4 + 136), *((char *)(ptr5 + 109)) = 1, sub_f7d8d0(ptr5, 0), ptr->field_30)))
                        {
                            ptr->field_30->field_296 = 1;
                            goto LABEL_1082e38;
                        }
                    }
                }
            }
            else if (a1 && (v14 = sub_1231bc8(a1, g_1efcef8), v14 && (ptr6 = (struct_15 *)ptr->field_30, ptr6)))
            {
                if (*((int *)(v14 + 240)) == ptr6->field_f0)
                    goto LABEL_1082e38;
                ptr6->field_238 = a1;
                sub_f7d8d0(&ptr6->field_238, a1);
                ptr7 = ptr->field_30;
                v17 = sub_1231bc8(a1, g_1efcef8);
                if (ptr7 && (ptr7->field_88 = (struct struct_14 *)v17, sub_f7d8d0(ptr7 + 136, v17), p = (struct_15 *)ptr->field_30, p && p->field_88))
                {
                    v19 = p->field_88->field_22c;
                    p->field_296 = 1;
                    p->field_27c = v19;
                    goto LABEL_1082e38;
                }
            }
        }
        else
        {
LABEL_1082e38:
            v20 = ptr->field_40;
            v22 = v20 - v21;
            v23 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v22, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v22, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v22, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v22, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v22, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v22, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
            if (!((char)v23))
            {
                ptr8 = ptr->field_30;
                if (ptr8)
                {
                    if (ptr8->field_279)
                    {
                        addr = ptr8->field_58;
                        if (addr && (ptr9 = (struct_10 *)addr->field_98, ptr9))
                        {
                            v27 = ptr9->field_204;
                            v28 = arm64g_calculate_condition(192, (((((unsigned long long)(char)(CmpF(v27, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v27, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v27, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v27, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v27, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v27, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                            if (!((char)v28) && !ptr9->field_229)
                                goto LABEL_1082ecc;
                            v29 = ptr->field_b0;
                            v20 += v21 * 0xc2000000;
                            ptr->field_40 = v20;
                            if (!v29)
                                goto LABEL_1082ed0;
                            v30 = addr->field_90;
                            if (v30)
                            {
                                v20 = ptr->field_b8;
                                MonoBehaviour__StartCoroutine(v30, FPSPlayer__ActivateBulletTime(v30, 0), 0);
                                goto LABEL_1082ed0;
                            }
                        }
                    }
                    else
                    {
LABEL_1082ecc:
                        ptr->field_40 = v22;
LABEL_1082ed0:
                        ptr10 = ptr->field_30;
                        ptr->field_cc = v33;
                        ptr->field_d0 = v34;
                        ptr->field_bc = v35;
                        ptr->field_c0 = v36;
                        ptr->field_c4 = v37;
                        ptr->field_c8 = v38;
                        ptr->field_e0 = (char)v0 & 1;
                        Time__get_time(0);
                        if (ptr10)
                        {
                            ptr10->field_f8 = v20;
                            if (!g_1ef0c58->field_e0)
                                sub_f7da5c(g_1ef0c58);
                            v39 = Object__op_Inequality(ptr->field_e8, 0, 0);
                            if (!((char)v39 & 1))
                            {
                                v40 = ptr->field_40;
LABEL_1082f78:
                                v42 = arm64g_calculate_condition(128, (((((unsigned long long)(char)(CmpF(v40, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v40, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v40, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v40, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v40, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v40, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                                if ((char)v42)
                                    return v39;
                                if (PlayerPrefs__GetInt(g_1f0bd20, 0) == 32)
                                {
                                    if (g_1eefae8->field_b8->field_8)
                                        GameController__SniperEnemySpawnFun(g_1eefae8->field_b8->field_8, 0); /* do not return */
                                }
                                else
                                {
                                    if (PlayerPrefs__GetInt(g_1f0bd20, 0) == 31)
                                    {
                                        PlayerPrefs__GetInt(g_1f14d40, 0);
                                        if (g_1eefae8->field_b8->field_8)
                                            GameController__EnemyKill(g_1eefae8->field_b8->field_8, 0); /* do not return */
                                    }
                                    else
                                    {
                                        if (g_1eefae8->field_b8->field_8)
                                        {
                                            GameController__Enemydown(g_1eefae8->field_b8->field_8, 0);
                                            if (g_1eefae8->field_b8->field_8)
                                                GameController__EnemyKill(g_1eefae8->field_b8->field_8, 0); /* do not return */
                                        }
                                    }
                                }
                            }
                            else if (ptr->field_e8)
                            {
                                v39 = Image__set_fillAmount(ptr->field_e8, 0);
                                v40 = ptr->field_40;
                                v41 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v40, 0x3f800000)) >> 5 & 3 | (unsigned long long)(CmpF(v40, 0x3f800000) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v40, 0x3f800000)) >> 5 & 3 | (unsigned long long)(CmpF(v40, 0x3f800000) & 1)) & ((unsigned long long)(char)(CmpF(v40, 0x3f800000)) >> 5 & 3 | (unsigned long long)(CmpF(v40, 0x3f800000) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                                if (!((char)v41))
                                {
                                    g_1eefae8->field_b8->field_0 = 2;
                                    goto LABEL_1082f78;
                                }
                            }
                        }
                    }
                }
            }
            else
            {
                ptr->field_40 = 0;
                goto LABEL_1082ed0;
            }
        }
    }
    sub_f7db74();
}
```


## `CharacterDamage.Die` — RVA `0xc832a0`

- Decompiled symbol: `CharacterDamage_Die`
- Metadata signature: `private void Die() { }`
- Native interval: `2276` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: Decompiler produced no C-like text

```c
// 0x10832a0: sub sp, sp, #0x110
// 0x10832a4: stp d15, d14, [sp, #0x70]
// 0x10832a8: stp d13, d12, [sp, #0x80]
// 0x10832ac: stp d11, d10, [sp, #0x90]
// 0x10832b0: stp d9, d8, [sp, #0xa0]
// 0x10832b4: stp x29, x30, [sp, #0xb0]
// 0x10832b8: stp x28, x27, [sp, #0xc0]
// 0x10832bc: stp x26, x25, [sp, #0xd0]
// 0x10832c0: stp x24, x23, [sp, #0xe0]
// 0x10832c4: stp x22, x21, [sp, #0xf0]
// 0x10832c8: stp x20, x19, [sp, #0x100]
// 0x10832cc: adrp x20, #0x1fab000
// 0x10832d0: adrp x27, #0x1e8c000
// 0x10832d4: ldrb w8, [x20, #0x40c]
// 0x10832d8: ldr x27, [x27, #0xd8]
// 0x10832dc: mov x19, x0
// 0x10832e0: tbnz w8, #0, #0x1083364
// 0x10832e4: adrp x0, #0x1e8d000
// 0x10832e8: ldr x0, [x0, #0xde0]
// 0x10832ec: bl #0xf7d92c
// 0x10832f0: adrp x0, #0x1e8d000
// 0x10832f4: ldr x0, [x0, #0xd00]
// 0x10832f8: bl #0xf7d92c
// 0x10832fc: adrp x0, #0x1e8d000
// 0x1083300: ldr x0, [x0, #0xdf0]
// 0x1083304: bl #0xf7d92c
// 0x1083308: adrp x0, #0x1e8d000
// 0x108330c: ldr x0, [x0, #0xe30]
// 0x1083310: bl #0xf7d92c
// 0x1083314: adrp x0, #0x1e8d000
// 0x1083318: ldr x0, [x0, #0xe38]
// 0x108331c: bl #0xf7d92c
// 0x1083320: adrp x0, #0x1e8c000
// 0x1083324: ldr x0, [x0, #0xd8]
// 0x1083328: bl #0xf7d92c
// 0x108332c: adrp x0, #0x1e8d000
// 0x1083330: ldr x0, [x0, #0x4a8]
// 0x1083334: bl #0xf7d92c
// 0x1083338: adrp x0, #0x1e8d000
// 0x108333c: ldr x0, [x0, #0xe40]
// 0x1083340: bl #0xf7d92c
// 0x1083344: adrp x0, #0x1e8d000
// 0x1083348: ldr x0, [x0, #0xe48]
// 0x108334c: bl #0xf7d92c
// 0x1083350: adrp x0, #0x1e8d000
// 0x1083354: ldr x0, [x0, #0xe50]
// 0x1083358: bl #0xf7d92c
// 0x108335c: mov w8, #1
// 0x1083360: strb w8, [x20, #0x40c]
// 0x1083364: ldr x0, [x27]
// 0x1083368: movi v0.2d, #0000000000000000
// 0x108336c: stur q0, [sp, #0x5c]
// 0x1083370: stp q0, q0, [sp, #0x40]
// 0x1083374: ldr w8, [x0, #0xe0]
// 0x1083378: ldr x20, [x19, #0x98]
// 0x108337c: cbnz w8, #0x1083384
// 0x1083380: bl #0xf7da5c
// 0x1083384: mov x0, x20
// 0x1083388: mov x1, xzr
// 0x108338c: bl #0x1b98274
// 0x1083390: tbz w0, #0, #0x10833d4
// 0x1083394: ldr x20, [x19, #0x98]
// 0x1083398: mov x0, x19
// 0x108339c: mov x1, xzr
// 0x10833a0: bl #0x1b92154
// 0x10833a4: cbz x0, #0x1083b74
// 0x10833a8: mov x1, xzr
// 0x10833ac: bl #0x1b9d508
// 0x10833b0: mov w8, #0x43fa0000
// 0x10833b4: fmov s3, #1.00000000
// 0x10833b8: fmov s4, #1.00000000
// 0x10833bc: fmov s5, #1.00000000
// 0x10833c0: fmov s6, #1.00000000
// 0x10833c4: fmov s7, w8
// 0x10833c8: mov x0, x20
// 0x10833cc: mov x1, xzr
// 0x10833d0: bl #0x108d260
// 0x10833d4: ldr x1, [x19, #0x30]
// 0x10833d8: cbz x1, #0x1083b74
// 0x10833dc: ldr x0, [x1, #0x80]
// 0x10833e0: cbz x0, #0x1083b74
// 0x10833e4: bl #0x1083e2c
// 0x10833e8: ldr x8, [x19, #0x30]
// 0x10833ec: cbz x8, #0x1083b74
// 0x10833f0: ldrb w9, [x8, #0x20]
// 0x10833f4: cbz w9, #0x1083430
// 0x10833f8: ldr x0, [x27]
// 0x10833fc: ldr x20, [x8, #0x78]
// 0x1083400: ldr w9, [x0, #0xe0]
// 0x1083404: cbnz w9, #0x108340c
// 0x1083408: bl #0xf7da5c
// 0x108340c: mov x0, x20
// 0x1083410: mov x1, xzr
// 0x1083414: bl #0x1b98274
// 0x1083418: tbz w0, #0, #0x1083430
// 0x108341c: ldr x1, [x19, #0x30]
// 0x1083420: cbz x1, #0x1083b74
// 0x1083424: ldr x0, [x1, #0x78]
// 0x1083428: cbz x0, #0x1083b74
// 0x108342c: bl #0x1083f28
// 0x1083430: ldr x8, [x19, #0x30]
// 0x1083434: cbz x8, #0x1083b74
// 0x1083438: ldr x0, [x8, #0x90]
// 0x108343c: cbz x0, #0x1083b74
// 0x1083440: mov w1, #1
// 0x1083444: mov x2, xzr
// 0x1083448: bl #0x1b53ec0
// 0x108344c: ldr x0, [x19, #0x30]
// 0x1083450: cbz x0, #0x1083b74
// 0x1083454: mov x1, xzr
// 0x1083458: bl #0x1b96124
// 0x108345c: ldr x0, [x27]
// 0x1083460: ldr x20, [x19, #0x88]
// 0x1083464: ldr w8, [x0, #0xe0]
// 0x1083468: cbnz w8, #0x1083470
// 0x108346c: bl #0xf7da5c
// 0x1083470: mov x0, x20
// 0x1083474: mov x1, xzr
// 0x1083478: bl #0x1b98274
// 0x108347c: tbz w0, #0, #0x1083b44
// 0x1083480: mov x0, x19
// 0x1083484: mov x1, xzr
// 0x1083488: bl #0x1b92190
// 0x108348c: cbz x0, #0x1083b74
// 0x1083490: adrp x8, #0x1e8d000
// 0x1083494: ldr x8, [x8, #0xe30]
// 0x1083498: mov w1, #1
// 0x108349c: ldr x2, [x8]
// 0x10834a0: bl #0x1249ec4
// 0x10834a4: cbz x0, #0x1083b74
// 0x10834a8: ldr w8, [x0, #0x18]
// 0x10834ac: mov x20, x0
// 0x10834b0: cmp w8, #1
// 0x10834b4: b.lt #0x1083550
// 0x10834b8: adrp x23, #0x1e8d000
// 0x10834bc: ldr x23, [x23, #0xe48]
// 0x10834c0: mov w22, wzr
// 0x10834c4: mov w24, #1
// 0x10834c8: cmp w22, w8
// 0x10834cc: b.hs #0x1083b78
// 0x10834d0: add x8, x20, w22, sxtw #3
// 0x10834d4: ldr x21, [x8, #0x20]
// 0x10834d8: cbz x21, #0x1083b74
// 0x10834dc: mov x0, x21
// 0x10834e0: mov x1, xzr
// 0x10834e4: bl #0x1b92154
// 0x10834e8: cbz x0, #0x1083b74
// 0x10834ec: mov x1, xzr
// 0x10834f0: mov x2, xzr
// 0x10834f4: bl #0x1b9dcb4
// 0x10834f8: ldr x0, [x21, #0x20]
// 0x10834fc: cbz x0, #0x1083b74
// 0x1083500: mov w1, wzr
// 0x1083504: mov x2, xzr
// 0x1083508: bl #0x1bcf2d0
// 0x108350c: ldr x0, [x21, #0x78]
// 0x1083510: cbz x0, #0x1083b74
// 0x1083514: mov w1, wzr
// 0x1083518: mov x2, xzr
// 0x108351c: bl #0x1bcf9b8
// 0x1083520: mov x0, x21
// 0x1083524: mov x1, xzr
// 0x1083528: bl #0x1b92190
// 0x108352c: cbz x0, #0x1083b74
// 0x1083530: ldr x1, [x23]
// 0x1083534: mov x2, xzr
// 0x1083538: bl #0x1b94d8c
// 0x108353c: strb w24, [x21, #0x31]
// 0x1083540: ldr w8, [x20, #0x18]
// 0x1083544: add w22, w22, #1
// 0x1083548: cmp w22, w8
// 0x108354c: b.lt #0x10834c8
// 0x1083550: ldr x20, [x19, #0x88]
// 0x1083554: mov x0, x19
// 0x1083558: mov x1, xzr
// 0x108355c: bl #0x1b92154
// 0x1083560: cbz x0, #0x1083b74
// 0x1083564: mov x1, xzr
// 0x1083568: bl #0x1b9d508
// 0x108356c: mov x0, x19
// 0x1083570: mov x1, xzr
// 0x1083574: mov v8.16b, v0.16b
// 0x1083578: mov v9.16b, v1.16b
// 0x108357c: mov v10.16b, v2.16b
// 0x1083580: bl #0x1b92154
// 0x1083584: cbz x0, #0x1083b74
// 0x1083588: mov x1, xzr
// 0x108358c: bl #0x1b9d6f0
// 0x1083590: ldr x0, [x27]
// 0x1083594: mov v11.16b, v0.16b
// 0x1083598: mov v12.16b, v1.16b
// 0x108359c: mov v13.16b, v2.16b
// 0x10835a0: ldr w8, [x0, #0xe0]
// 0x10835a4: mov v14.16b, v3.16b
// 0x10835a8: cbnz w8, #0x10835b0
// 0x10835ac: bl #0xf7da5c
// 0x10835b0: adrp x8, #0x1e8d000
// 0x10835b4: ldr x8, [x8, #0xe38]
// 0x10835b8: mov x0, x20
// 0x10835bc: mov v0.16b, v8.16b
// 0x10835c0: mov v1.16b, v9.16b
// 0x10835c4: ldr x1, [x8]
// 0x10835c8: mov v2.16b, v10.16b
// 0x10835cc: mov v3.16b, v11.16b
// 0x10835d0: mov v4.16b, v12.16b
// 0x10835d4: mov v5.16b, v13.16b
// 0x10835d8: mov v6.16b, v14.16b
// 0x10835dc: bl #0x112a1ac
// 0x10835e0: mov x21, x19
// 0x10835e4: str x0, [x21, #0x90]!
// 0x10835e8: mov x1, x0
// 0x10835ec: mov x0, x21
// 0x10835f0: bl #0xf7d8d0
// 0x10835f4: ldr x0, [x21]
// 0x10835f8: cbz x0, #0x1083b74
// 0x10835fc: adrp x8, #0x1e8d000
// 0x1083600: ldr x8, [x8, #0xde0]
// 0x1083604: ldr x1, [x8]
// 0x1083608: bl #0x1231bc8
// 0x108360c: mov x28, x19
// 0x1083610: str x0, [x28, #0x38]!
// 0x1083614: mov x1, x0
// 0x1083618: mov x0, x28
// 0x108361c: bl #0xf7d8d0
// 0x1083620: mov x0, x19
// 0x1083624: mov x1, xzr
// 0x1083628: bl #0x1b92154
// 0x108362c: ldr x1, [x19, #0x90]
// 0x1083630: bl #0x108414c
// 0x1083634: ldr x0, [x19, #0x90]
// 0x1083638: cbz x0, #0x1083b74
// 0x108363c: adrp x8, #0x1e8d000
// 0x1083640: ldr x8, [x8, #0xd00]
// 0x1083644: ldr x1, [x8]
// 0x1083648: bl #0x1232400
// 0x108364c: cbz x0, #0x1083b74
// 0x1083650: ldr x8, [x0, #0x18]
// 0x1083654: mov x22, x0
// 0x1083658: cmp w8, #1
// 0x108365c: b.lt #0x10836c8
// 0x1083660: adrp x26, #0x1e8d000
// 0x1083664: ldr x26, [x26, #0x4a8]
// 0x1083668: mov x20, xzr
// 0x108366c: and x8, x8, #0xffffffff
// 0x1083670: add x25, x22, #0x20
// 0x1083674: cmp x20, w8, uxtw
// 0x1083678: b.hs #0x1083b78
// 0x108367c: ldr x8, [x19, #0x30]
// 0x1083680: cbz x8, #0x1083b74
// 0x1083684: ldr x8, [x8, #0x48]
// 0x1083688: cbz x8, #0x1083b74
// 0x108368c: ldr x0, [x26]
// 0x1083690: ldr x23, [x25, x20, lsl #3]
// 0x1083694: ldr x24, [x8, #0x238]
// 0x1083698: ldr w9, [x0, #0xe0]
// 0x108369c: cbnz w9, #0x10836a4
// 0x10836a0: bl #0xf7da5c
// 0x10836a4: mov w2, #1
// 0x10836a8: mov x0, x23
// 0x10836ac: mov x1, x24
// 0x10836b0: mov x3, xzr
// 0x10836b4: bl #0x1bcb368
// 0x10836b8: ldr w8, [x22, #0x18]
// 0x10836bc: add x20, x20, #1
// 0x10836c0: cmp x20, w8, sxtw
// 0x10836c4: b.lt #0x1083674
// 0x10836c8: ldr w0, [x19, #0xe4]
// 0x10836cc: ldp s8, s9, [x19, #0xbc]
// 0x10836d0: ldp s10, s11, [x19, #0xc4]
// 0x10836d4: ldp s12, s13, [x19, #0xcc]
// 0x10836d8: mov x1, xzr
// 0x10836dc: bl #0x1b9515c
// 0x10836e0: adrp x8, #0x1e8d000
// 0x10836e4: ldr x8, [x8, #0x4a8]
// 0x10836e8: mov w22, w0
// 0x10836ec: ldr x8, [x8]
// 0x10836f0: ldr w9, [x8, #0xe0]
// 0x10836f4: cbnz w9, #0x1083700
// 0x10836f8: mov x0, x8
// 0x10836fc: bl #0xf7da5c
// 0x1083700: adrp x8, #0x832000
// 0x1083704: adrp x9, #0x832000
// 0x1083708: ldr s3, [x8, #0x4f4]
// 0x108370c: ldr s7, [x9, #0x2fc]
// 0x1083710: add x0, sp, #0x40
// 0x1083714: mov v0.16b, v8.16b
// 0x1083718: mov v1.16b, v9.16b
// 0x108371c: mov v2.16b, v10.16b
// 0x1083720: mov v4.16b, v11.16b
// 0x1083724: mov v5.16b, v12.16b
// 0x1083728: mov v6.16b, v13.16b
// 0x108372c: mov w1, w22
// 0x1083730: mov x2, xzr
// 0x1083734: bl #0x1bccacc
// 0x1083738: str x28, [sp, #0x10]
// 0x108373c: tbz w0, #0, #0x1083780
// 0x1083740: add x0, sp, #0x40
// 0x1083744: mov x1, xzr
// 0x1083748: bl #0x1bcee00
// 0x108374c: ldr x8, [x27]
// 0x1083750: mov x22, x0
// 0x1083754: ldr w9, [x8, #0xe0]
// 0x1083758: cbnz w9, #0x1083764
// 0x108375c: mov x0, x8
// 0x1083760: bl #0xf7da5c
// 0x1083764: mov x0, x22
// 0x1083768: mov x1, xzr
// 0x108376c: bl #0x1b98274
// 0x1083770: tbz w0, #0, #0x1083780
// 0x1083774: ldr s0, [x19, #0xc8]
// 0x1083778: fcmp s0, #0.0
// 0x108377c: b.ne #0x1083a54
// 0x1083780: ldr x0, [x21]
// 0x1083784: cbz x0, #0x1083b74
// 0x1083788: adrp x8, #0x1e8d000
// 0x108378c: ldr x8, [x8, #0xdf0]
// 0x1083790: ldr x1, [x8]
// 0x1083794: bl #0x1232400
// 0x1083798: cbz x0, #0x1083b74
// 0x108379c: ldr x8, [x0, #0x18]
// 0x10837a0: mov x21, x0
// 0x10837a4: cmp w8, #1
// 0x10837a8: b.lt #0x1083a88
// 0x10837ac: adrp x22, #0x1e8c000
// 0x10837b0: adrp x23, #0x1e8c000
// 0x10837b4: adrp x9, #0x832000
// 0x10837b8: ldr x22, [x22, #0x1e8]
// 0x10837bc: ldr x23, [x23, #0xa60]
// 0x10837c0: ldr s11, [x9, #0x41c]
// 0x10837c4: mov x26, xzr
// 0x10837c8: and x8, x8, #0xffffffff
// 0x10837cc: add x27, x21, #0x20
// 0x10837d0: adrp x29, #0x1fab000
// 0x10837d4: mov w25, #1
// 0x10837d8: fmov v9.2s, #-2.50000000
// 0x10837dc: fmov s10, #-2.50000000
// 0x10837e0: adrp x20, #0x1fab000
// 0x10837e4: adrp x28, #0x1fab000
// 0x10837e8: fmov v0.2s, #10.00000000
// 0x10837ec: str d0, [sp, #0x18]
// 0x10837f0: cmp x26, w8, uxtw
// 0x10837f4: b.hs #0x1083b78
// 0x10837f8: ldr x24, [x27, x26, lsl #3]
// 0x10837fc: cbz x24, #0x10838f4
// 0x1083800: adrp x9, #0x1e8d000
// 0x1083804: ldr x8, [x24]
// 0x1083808: ldr x9, [x9, #0xe40]
// 0x108380c: ldrb w10, [x8, #0x130]
// 0x1083810: ldr x1, [x9]
// 0x1083814: ldrb w9, [x1, #0x130]
// 0x1083818: cmp w10, w9
// 0x108381c: b.lo #0x1083b7c
// 0x1083820: ldr x8, [x8, #0xc8]
// 0x1083824: add x8, x8, x9, lsl #3
// 0x1083828: ldur x8, [x8, #-8]
// 0x108382c: cmp x8, x1
// 0x1083830: b.ne #0x1083b7c
// 0x1083834: ldrb w8, [x19, #0xe0]
// 0x1083838: cbnz w8, #0x10838fc
// 0x108383c: mov x0, x24
// 0x1083840: mov x1, xzr
// 0x1083844: bl #0x1b92154
// 0x1083848: cbz x0, #0x1083b74
// 0x108384c: mov x1, xzr
// 0x1083850: bl #0x1b98300
// 0x1083854: adrp x8, #0x1e8d000
// 0x1083858: ldr x8, [x8, #0xe50]
// 0x108385c: mov x2, xzr
// 0x1083860: ldr x1, [x8]
// 0x1083864: bl #0x17f610c
// 0x1083868: tbz w0, #0, #0x1083a08
// 0x108386c: ldr x0, [x19, #0xd8]
// 0x1083870: cbz x0, #0x1083b74
// 0x1083874: mov x1, xzr
// 0x1083878: bl #0x1b9d508
// 0x108387c: ldur d14, [x19, #0xbc]
// 0x1083880: ldrb w8, [x20, #0x2c8]
// 0x1083884: ldr s15, [x19, #0xc4]
// 0x1083888: mov v8.16b, v2.16b
// 0x108388c: cbnz w8, #0x10838a4
// 0x1083890: mov x0, x23
// 0x1083894: stp q1, q0, [sp, #0x20]
// 0x1083898: bl #0xf7d92c
// 0x108389c: ldp q1, q0, [sp, #0x20]
// 0x10838a0: strb w25, [x20, #0x2c8]
// 0x10838a4: ldr x0, [x23]
// 0x10838a8: ldr w8, [x0, #0xe0]
// 0x10838ac: cbnz w8, #0x10838bc
// 0x10838b0: stp q1, q0, [sp, #0x20]
// 0x10838b4: bl #0xf7da5c
// 0x10838b8: ldp q1, q0, [sp, #0x20]
// 0x10838bc: mov v0.s[1], v1.s[0]
// 0x10838c0: fsub v1.2s, v0.2s, v14.2s
// 0x10838c4: fsub s4, s8, s15
// 0x10838c8: fmul v2.2s, v1.2s, v1.2s
// 0x10838cc: faddp s2, v2.2s
// 0x10838d0: fmul s3, s4, s4
// 0x10838d4: fadd s2, s3, s2
// 0x10838d8: fsqrt s2, s2
// 0x10838dc: fcmp s2, s11
// 0x10838e0: b.le #0x1083a1c
// 0x10838e4: dup v3.2s, v2.s[0]
// 0x10838e8: fdiv v1.2s, v1.2s, v3.2s
// 0x10838ec: fdiv s2, s4, s2
// 0x10838f0: b #0x1083a40
// 0x10838f4: ldrb w8, [x19, #0xe0]
// 0x10838f8: cbz w8, #0x1083b74
// 0x10838fc: ldr x0, [x19, #0xd8]
// 0x1083900: cbz x0, #0x1083b74
// 0x1083904: mov x1, xzr
// 0x1083908: bl #0x1b9d508
// 0x108390c: ldur d14, [x19, #0xbc]
// 0x1083910: ldrb w8, [x29, #0x32c]
// 0x1083914: ldr s15, [x19, #0xc4]
// 0x1083918: mov v8.16b, v2.16b
// 0x108391c: str d0, [sp, #0x30]
// 0x1083920: str d1, [sp, #0x20]
// 0x1083924: cbnz w8, #0x1083934
// 0x1083928: mov x0, x22
// 0x108392c: bl #0xf7d92c
// 0x1083930: strb w25, [x29, #0x32c]
// 0x1083934: ldr x8, [x22]
// 0x1083938: ldrb w9, [x20, #0x2c8]
// 0x108393c: ldr x8, [x8, #0xb8]
// 0x1083940: ldr d12, [x8, #0x18]
// 0x1083944: ldr s13, [x8, #0x20]
// 0x1083948: cbnz w9, #0x1083958
// 0x108394c: mov x0, x23
// 0x1083950: bl #0xf7d92c
// 0x1083954: strb w25, [x20, #0x2c8]
// 0x1083958: ldr x0, [x23]
// 0x108395c: ldr w8, [x0, #0xe0]
// 0x1083960: cbnz w8, #0x1083968
// 0x1083964: bl #0xf7da5c
// 0x1083968: ldp q3, q2, [sp, #0x20]
// 0x108396c: fmul v0.2s, v12.2s, v9.2s
// 0x1083970: fmul s1, s13, s10
// 0x1083974: fadd v0.2s, v14.2s, v0.2s
// 0x1083978: mov v2.s[1], v3.s[0]
// 0x108397c: fadd s1, s15, s1
// 0x1083980: fsub v0.2s, v2.2s, v0.2s
// 0x1083984: fsub s1, s8, s1
// 0x1083988: fmul v2.2s, v0.2s, v0.2s
// 0x108398c: faddp s2, v2.2s
// 0x1083990: fmul s3, s1, s1
// 0x1083994: fadd s2, s3, s2
// 0x1083998: fsqrt s2, s2
// 0x108399c: fcmp s2, s11
// 0x10839a0: b.le #0x10839b4
// 0x10839a4: dup v3.2s, v2.s[0]
// 0x10839a8: fdiv v8.2s, v0.2s, v3.2s
// 0x10839ac: fdiv s13, s1, s2
// 0x10839b0: b #0x10839d8
// 0x10839b4: ldrb w8, [x28, #0x2c9]
// 0x10839b8: cbnz w8, #0x10839c8
// 0x10839bc: mov x0, x22
// 0x10839c0: bl #0xf7d92c
// 0x10839c4: strb w25, [x28, #0x2c9]
// 0x10839c8: ldr x8, [x22]
// 0x10839cc: ldr x8, [x8, #0xb8]
// 0x10839d0: ldr d8, [x8]
// 0x10839d4: ldr s13, [x8, #8]
// 0x10839d8: fmov s0, #4.50000000
// 0x10839dc: fmov s1, #7.50000000
// 0x10839e0: mov x0, xzr
// 0x10839e4: bl #0x1b9012c
// 0x10839e8: cbz x24, #0x1083b74
// 0x10839ec: fmul s2, s13, s0
// 0x10839f0: fmul v0.2s, v8.2s, v0.s[0]
// 0x10839f4: mov s1, v0.s[1]
// 0x10839f8: mov w1, #1
// 0x10839fc: mov x0, x24
// 0x1083a00: mov x2, xzr
// 0x1083a04: bl #0x1bcf5b8
// 0x1083a08: ldr w8, [x21, #0x18]
// 0x1083a0c: add x26, x26, #1
// 0x1083a10: cmp x26, w8, sxtw
// 0x1083a14: b.lt #0x10837f0
// 0x1083a18: b #0x1083a88
// 0x1083a1c: ldrb w8, [x28, #0x2c9]
// 0x1083a20: cbnz w8, #0x1083a30
// 0x1083a24: mov x0, x22
// 0x1083a28: bl #0xf7d92c
// 0x1083a2c: strb w25, [x28, #0x2c9]
// 0x1083a30: ldr x8, [x22]
// 0x1083a34: ldr x8, [x8, #0xb8]
// 0x1083a38: ldr d1, [x8]
// 0x1083a3c: ldr s2, [x8, #8]
// 0x1083a40: ldr d0, [sp, #0x18]
// 0x1083a44: fmul v0.2s, v1.2s, v0.2s
// 0x1083a48: fmov s1, #10.00000000
// 0x1083a4c: fmul s2, s2, s1
// 0x1083a50: b #0x10839f4
// 0x1083a54: add x0, sp, #0x40
// 0x1083a58: mov x1, xzr
// 0x1083a5c: bl #0x1bcee00
// 0x1083a60: cbz x0, #0x1083b74
// 0x1083a64: ldp s1, s0, [x19, #0xcc]
// 0x1083a68: ldr s3, [x19, #0xc8]
// 0x1083a6c: fmov s4, #10.00000000
// 0x1083a70: mov w1, #1
// 0x1083a74: fmul s2, s0, s4
// 0x1083a78: fmul s1, s1, s4
// 0x1083a7c: fmul s0, s3, s4
// 0x1083a80: mov x2, xzr
// 0x1083a84: bl #0x1bcf5b8
// 0x1083a88: adrp x22, #0x1e8c000
// 0x1083a8c: ldr x22, [x22, #0xd8]
// 0x1083a90: ldr x20, [sp, #0x10]
// 0x1083a94: ldr x0, [x22]
// 0x1083a98: ldr x21, [x20]
// 0x1083a9c: ldr w8, [x0, #0xe0]
// 0x1083aa0: cbnz w8, #0x1083aa8
// 0x1083aa4: bl #0xf7da5c
// 0x1083aa8: mov x0, x21
// 0x1083aac: mov x1, xzr
// 0x1083ab0: bl #0x1b98274
// 0x1083ab4: tbz w0, #0, #0x1083af4
// 0x1083ab8: ldr x0, [x20]
// 0x1083abc: cbz x0, #0x1083b74
// 0x1083ac0: ldrb w8, [x19, #0xa1]
// 0x1083ac4: cbz w8, #0x1083ae8
// 0x1083ac8: mov w1, #1
// 0x1083acc: mov x2, xzr
// 0x1083ad0: bl #0x1b91660
// 0x1083ad4: ldr x8, [x20]
// 0x1083ad8: cbz x8, #0x1083b74
// 0x1083adc: ldr s0, [x19, #0xa4]
// 0x1083ae0: str s0, [x8, #0x24]
// 0x1083ae4: b #0x1083af4
// 0x1083ae8: mov w1, wzr
// 0x1083aec: mov x2, xzr
// 0x1083af0: bl #0x1b91660
// 0x1083af4: ldrb w20, [x19, #0xa0]
// 0x1083af8: mov x0, x19
// 0x1083afc: mov x1, xzr
// 0x1083b00: bl #0x1b92154
// 0x1083b04: cbz x0, #0x1083b74
// 0x1083b08: mov x1, xzr
// 0x1083b0c: cbz w20, #0x1083b1c
// 0x1083b10: bl #0x1b9d400
// 0x1083b14: cbz x0, #0x1083b74
// 0x1083b18: mov x1, xzr
// 0x1083b1c: bl #0x1b92190
// 0x1083b20: ldr x8, [x22]
// 0x1083b24: mov x19, x0
// 0x1083b28: ldr w9, [x8, #0xe0]
// 0x1083b2c: cbnz w9, #0x1083b38
// 0x1083b30: mov x0, x8
// 0x1083b34: bl #0xf7da5c
// 0x1083b38: mov x0, x19
// 0x1083b3c: mov x1, xzr
// 0x1083b40: bl #0x1b98a20
// 0x1083b44: ldp x20, x19, [sp, #0x100]
// 0x1083b48: ldp x22, x21, [sp, #0xf0]
// 0x1083b4c: ldp x24, x23, [sp, #0xe0]
// 0x1083b50: ldp x26, x25, [sp, #0xd0]
// 0x1083b54: ldp x28, x27, [sp, #0xc0]
// 0x1083b58: ldp x29, x30, [sp, #0xb0]
// 0x1083b5c: ldp d9, d8, [sp, #0xa0]
// 0x1083b60: ldp d11, d10, [sp, #0x90]
// 0x1083b64: ldp d13, d12, [sp, #0x80]
// 0x1083b68: ldp d15, d14, [sp, #0x70]
// 0x1083b6c: add sp, sp, #0x110
// 0x1083b70: ret
// 0x1083b74: bl #0xf7db74
// 0x1083b78: bl #0xf7db7c
// 0x1083b7c: mov x0, x24
// 0x1083b80: bl #0xf7df10
```


## `CharacterDamage.RagDollDie` — RVA `0xc83b84`

- Decompiled symbol: `CharacterDamage_RagDollDie`
- Metadata signature: `private void RagDollDie(Rigidbody hitBody, float bodyForce) { }`
- Native interval: `680` bytes
- Result: `pseudocode`
- Heuristic layout hint: `CharacterDamage_Recovered` matched 7 offsets against `CharacterDamage` metadata (confidence 1.00).

```c
typedef struct struct_3 {
    char padding_0[32];
    char field_20;
    char padding_21[3];
    unsigned int field_24;
    char padding_28[40];
    struct struct_3 *field_50;
    char padding_58[32];
    struct struct_3 *field_78;
    struct struct_3 *field_80;
    char padding_88[8];
    struct struct_3 *field_90;
    char padding_98[24];
    struct struct_3 *field_b0;
    struct struct_3 *field_b8;
} struct_3;

typedef struct CharacterDamage_Recovered {
    char padding_0[48];
    struct struct_1 *AIComponent;
    struct struct_1 *RemoveBodyComponent;
    char padding_40[64];
    char ragdollActive;
    char padding_81[23];
    long long dieSound;
    char padding_a0[1];
    char removeBody;
    char padding_a2[2];
    unsigned int bodyStayTime;
    char padding_a8[72];
    struct struct_1 *ShowMe;
} CharacterDamage_Recovered;

typedef struct struct_1 {
    char padding_0[32];
    char field_20;
    char padding_21[3];
    unsigned int field_24;
    char padding_28[40];
    struct struct_1 *field_50;
    char padding_58[32];
    struct struct_1 *field_78;
    struct struct_1 *field_80;
    char padding_88[8];
    struct struct_1 *field_90;
    char padding_98[24];
    struct struct_1 *field_b0;
    struct struct_1 *field_b8;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab40a;

struct_3 * CharacterDamage_RagDollDie(struct_2 *ptr, long long a1)
{
    struct_3 *v0;  // x0
    struct_1 *v1;  // x8
    struct_1 *v2;  // x8
    struct_3 *v4;  // x0
    unsigned long long v5;  // x0

    if (!(g_1fab40a & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab40a = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (((char)Object__op_Inequality(ptr->field_f0, 0, 0) & 1))
    {
        v0 = ptr->field_f0;
        if (v0)
        {
            GameObject__SetActive(v0, 1, 0);
            goto LABEL_1083bfc;
        }
    }
    else
    {
LABEL_1083bfc:
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        v0 = Object__op_Implicit(ptr->field_98, 0);
        if (((char)v0 & 1))
        {
            v0 = Component__get_transform(ptr, 0);
            if (v0)
            {
                Transform__get_position();
                v0 = PlayAudioAtPos__PlayClipAt(ptr->field_98, 0);
                goto LABEL_1083c60;
            }
        }
        else
        {
LABEL_1083c60:
            if (ptr->field_30 && (v0 = (struct_3 *)ptr->field_30->field_80, v0 && (v0 = (struct_3 *)(unsigned long long)NPCRegistry__UnregisterNPC(), v1 = (struct_1 *)ptr->field_30, v1)))
            {
                if (v1->field_20)
                {
                    if (!g_1ef0c58->field_e0)
                        sub_f7da5c(g_1ef0c58);
                    v0 = Object__op_Implicit(v1->field_78, 0);
                    if (!(v0 & 1))
                        goto LABEL_1083cbc;
                    if (ptr->field_30 && (v0 = (struct_3 *)ptr->field_30->field_78, v0))
                    {
                        v0 = NPCSpawner__UnregisterSpawnedNPC(v0);
                        goto LABEL_1083cbc;
                    }
                }
                else
                {
LABEL_1083cbc:
                    if (ptr->field_30 && (v0 = (struct_3 *)ptr->field_30->field_b0, v0 && (v0 = (struct_3 *)(unsigned long long)Behaviour__set_enabled(v0, 0, 0), v2 = (struct_1 *)ptr->field_30, ptr->field_80 = 1, v2 && v2->field_50)))
                    {
                        if (!g_1ef0c58->field_e0)
                            sub_f7da5c(g_1ef0c58);
                        v0 = Object__op_Implicit(v2->field_50->field_b8, 0);
                        if (!((char)v0 & 1))
                        {
LABEL_1083d38:
                            if (ptr->field_30)
                            {
                                v0 = ptr->field_30->field_50;
                                if (v0)
                                {
                                    Behaviour__set_enabled(v0, 0, 0);
                                    v0 = ptr->field_30;
                                    if (v0)
                                    {
                                        v0 = MonoBehaviour__StopAllCoroutines(v0, 0);
                                        if (ptr->field_30)
                                        {
                                            v0 = ptr->field_30->field_90;
                                            if (v0)
                                            {
                                                Behaviour__set_enabled(v0, 0, 0);
                                                v0 = ptr->field_30;
                                                if (v0)
                                                {
                                                    Behaviour__set_enabled(v0, 0, 0);
                                                    MonoBehaviour__StartCoroutine(ptr, CharacterDamage__ApplyForce(ptr, a1), 0);
                                                    if (!g_1ef0c58->field_e0)
                                                        sub_f7da5c(g_1ef0c58);
                                                    v4 = Object__op_Implicit(ptr->field_38, 0);
                                                    if (!((char)v4 & 1))
                                                        return v4;
                                                    v0 = ptr->field_38;
                                                    if (v0)
                                                    {
                                                        if (ptr->field_a1)
                                                        {
                                                            v0 = Behaviour__set_enabled();
                                                            if (ptr->field_38)
                                                            {
                                                                ptr->field_38->field_24 = ptr->field_a4;
                                                                return v0;
                                                            }
                                                        }
                                                        else
                                                        {
                                                            v5 = Behaviour__set_enabled();
                                                            return Behaviour__set_enabled();
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                        else if (ptr->field_30 && ptr->field_30->field_50 && (v0 = (struct_3 *)ptr->field_30->field_50->field_b8, v0))
                        {
                            v0 = Renderer__set_enabled(v0, 0, 0);
                            goto LABEL_1083d38;
                        }
                    }
                }
            }
        }
    }
    sub_f7db74(v0);
}
```


## `CharacterDamage.ApplyForce` — RVA `0xc8409c`

- Decompiled symbol: `CharacterDamage_ApplyForce`
- Metadata signature: `public IEnumerator ApplyForce(Rigidbody body, float force) { }`
- Native interval: `136` bytes
- Result: `pseudocode`
- Heuristic layout hint: `CharacterDamage_Recovered` matched 2 offsets against `CharacterDamage` metadata (confidence 0.67).

```c
typedef struct CharacterDamage_Recovered {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[12];
    long long minimapitem;
    long long onDie;
} CharacterDamage_Recovered;

extern long long g_1ef2da8;
extern char g_1fab40b;

struct_0 * CharacterDamage_ApplyForce(long long a0, long long a1)
{
    struct_0 *v0;  // x21
    struct_0 *ptr;  // x0
    struct_0 *p;  // x0

    if (!(g_1fab40b & 1))
    {
        sub_f7d92c(&g_1ef2da8);
        g_1fab40b = 1;
    }
    v0 = sub_f7db70(g_1ef2da8);
    Object__ctor(v0, 0);
    ptr = v0;
    ptr->field_10 = 0;
    ptr->field_20 = a0;
    sub_f7d8d0(&ptr->field_20, a0);
    p = ptr;
    p->field_28 = a1;
    sub_f7d8d0(&p->field_28, a1);
    return p;
}
```


## `CharacterDamage.<ApplyForce>d__38.ctor` — RVA `0xc84124`

- Decompiled symbol: `CharacterDamage_ApplyForce_d__38_ctor`
- Metadata signature: `public void .ctor(int <>1__state) { }`
- Native interval: `40` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

void CharacterDamage_ApplyForce_d__38_ctor(struct_0 *ptr, unsigned int a1)
{
    Object__ctor();
    ptr->field_10 = a1;
    return;
}
```


## `CharacterDamage.CopyTransformsRecurse` — RVA `0xc8414c`

- Decompiled symbol: `CharacterDamage_CopyTransformsRecurse`
- Metadata signature: `private static void CopyTransformsRecurse(Transform src, Transform dst) { }`
- Native interval: `896` bytes
- Result: `pseudocode`

```c
typedef struct struct_4 {
    char padding_0[176];
    struct struct_3 *field_b0;
    char padding_b8[118];
    unsigned short field_12e;
} struct_4;

typedef struct struct_2 {
    struct struct_1 *field_0;
} struct_2;

typedef struct struct_20 {
    char padding_0[176];
    struct struct_19 *field_b0;
    char padding_b8[118];
    unsigned short field_12e;
} struct_20;

typedef struct struct_5 {
    char padding_0[312];
    struct struct_6 *field_138;
    unsigned long long field_140;
} struct_5;

typedef struct struct_10 {
    char padding_0[176];
    struct struct_9 *field_b0;
    char padding_b8[118];
    unsigned short field_12e;
} struct_10;

typedef struct struct_16 {
    char padding_0[176];
    struct struct_15 *field_b0;
    char padding_b8[118];
    unsigned short field_12e;
} struct_16;

typedef struct struct_7 {
    char padding_0[312];
    struct struct_8 *field_138;
    unsigned long long field_140;
} struct_7;

typedef struct struct_14 {
    char padding_0[176];
    struct struct_13 *field_b0;
    char padding_b8[118];
    unsigned short field_12e;
} struct_14;

typedef struct struct_18 {
    char padding_0[176];
    struct struct_17 *field_b0;
    char padding_b8[118];
    unsigned short field_12e;
} struct_18;

typedef struct struct_11 {
    char padding_0[312];
    struct struct_12 *field_138;
    unsigned long long field_140;
} struct_11;

typedef struct struct_3 {
    unsigned long long field_0;
    unsigned int field_8;
    char padding_c[12];
    char field_18;
} struct_3;

typedef struct struct_1 {
    char padding_0[176];
    struct struct_0 *field_b0;
    char padding_b8[118];
    unsigned short field_12e;
} struct_1;

typedef struct struct_19 {
    unsigned long long field_0;
    unsigned int field_8;
    char padding_c[12];
    char field_18;
} struct_19;

typedef struct struct_6 {
    unsigned long long field_0;
} struct_6;

typedef struct struct_9 {
    char padding_0[8];
    unsigned int field_8;
} struct_9;

typedef struct struct_15 {
    char padding_0[8];
    unsigned int field_8;
} struct_15;

typedef struct struct_8 {
    unsigned long long field_0;
} struct_8;

typedef struct struct_13 {
    char padding_0[8];
    unsigned int field_8;
} struct_13;

typedef struct struct_17 {
    char padding_0[8];
    unsigned int field_8;
} struct_17;

typedef struct struct_12 {
    unsigned long long field_0;
} struct_12;

typedef struct struct_0 {
    unsigned long long field_0;
    unsigned int field_8;
    char padding_c[12];
    char field_18;
} struct_0;

extern struct_2 *g_1eefef8;
extern long long g_1eeff88;
extern long long g_1ef0c58;
extern char g_1fab40e;

unsigned long long CharacterDamage_CopyTransformsRecurse(long long a0, struct_4 **a1)
{
    struct_4 **ptr6;  // x19
    long long v2;  // x20
    unsigned long long v11;  // x2
    unsigned long long v12;  // x1
    struct_4 **v13;  // x0
    long long v14;  // x0
    long long *ptr7;  // x0
    struct_10 **ptr8;  // x0
    struct_16 *ptr;  // x8
    struct_10 **v18;  // x19
    unsigned long v19;  // x9
    unsigned long cur;  // x10
    struct_2 **ptr9;  // x23
    unsigned long v21;  // x9
    struct_7 *ptr11;  // x0
    unsigned long long v24;  // x2
    unsigned long long v25;  // x1
    struct_10 **v26;  // x0
    struct_14 **ptr10;  // x19
    struct_18 *p;  // x8
    unsigned long v29;  // x9
    unsigned long iter;  // x10
    struct_4 **v4;  // x0
    unsigned long v31;  // x9
    struct_11 *ptr12;  // x0
    unsigned long long v34;  // x2
    unsigned long long v35;  // x1
    struct_14 **v36;  // x0
    struct_20 *addr;  // x8
    unsigned long v6;  // x9
    unsigned long node;  // x10
    unsigned long v8;  // x9
    struct_5 *ptr13;  // x0
    long long v0;  // [bp-0x48]

    ptr6 = a1;
    v2 = a0;
    if (!(g_1fab40e & 1))
    {
        sub_f7d92c(&g_1eefef8);
        sub_f7d92c(&g_1eeff88);
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c("cY");
        g_1fab40e = 1;
    }
    if (v2 && !((a1 = NULL, Transform__get_position(v2, 0), !ptr6)))
    {
        ptr9 = &g_1eefef8;
        Transform__set_position(ptr6, 0);
        Transform__get_rotation(v2, 0);
        Transform__set_rotation(ptr6, 0);
        a1 = NULL;
        v4 = Transform__GetEnumerator(ptr6, 0);
        ptr6 = v4;
        if (v4)
        {
            addr = *(ptr6);
            v6 = addr->field_12e;
            if (v6)
            {
                node = &addr->field_b0->field_8;
                do
                {
                    v8 = v6;
                    if (*((long long *)(node - 8)) == g_1eeff88)
                    {
                        ptr13 = &addr->padding_0[16 * *((int *)node) + 312];
                        v12 = *((long long *)&ptr13->padding_0[8]);
                        v13 = ptr6;
                        (*((long long *)&ptr13->padding_0[0]))();
                    }
                } while ((node = (unsigned long)(node + 16), v6 = (unsigned long)(v8 - 1), v8 != 1));
            }
            v11 = 0;
            ptr13 = sub_f80110(ptr6);
            v12 = *((long long *)&ptr13->padding_0[8]);
            v13 = ptr6;
            (*((long long *)&ptr13->padding_0[0]))();
        }
    }
    else
    {
        v4 = sub_f7db74();
    }
    sub_f7db74(v4);
    while (true)
    {
        v14 = sub_f1bd40(v2);
        if ((unsigned int)a1 != 1)
            break;
        ptr7 = __cxa_begin_catch();
        v2 = *(ptr7);
        __cxa_end_catch(ptr7);
        a1 = *(ptr9);
        ptr8 = sub_f7da60(ptr6, a1);
        if (ptr8)
        {
            ptr = *(ptr8);
            v18 = ptr8;
            v19 = ptr->field_12e;
            if (v19)
            {
                cur = &ptr->field_b0->field_8;
                do
                {
                    v21 = v19;
                    if (*((long long *)(cur - 8)) == *(ptr9))
                    {
                        ptr11 = &ptr->padding_0[16 * *((int *)cur) + 312];
                        v25 = *((long long *)&ptr11->padding_0[8]);
                        v26 = v18;
                        (*((long long *)&ptr11->padding_0[0]))();
                    }
                } while ((cur = (unsigned long)(cur + 16), v19 = (unsigned long)(v21 - 1), v21 != 1));
            }
            v24 = 0;
            ptr11 = sub_f80110(v18);
            v25 = *((long long *)&ptr11->padding_0[8]);
            v26 = v18;
            (*((long long *)&ptr11->padding_0[0]))();
        }
        else if (!v2)
        {
            return 0;
        }
    }
    v0 = v14;
    ptr10 = sub_f7da60(ptr6, *(ptr9));
    if (!ptr10)
    {
        sub_1026098(v0);
        sub_e29990(sub_f1bd40(0));
    }
    p = *(ptr10);
    v29 = p->field_12e;
    if (v29)
    {
        iter = &p->field_b0->field_8;
        do
        {
            v31 = v29;
            if (*((long long *)(iter - 8)) == *(ptr9))
            {
                ptr12 = &p->padding_0[16 * *((int *)iter) + 312];
                v35 = *((long long *)&ptr12->padding_0[8]);
                v36 = ptr10;
                (*((long long *)&ptr12->padding_0[0]))();
            }
        } while ((iter = (unsigned long)(iter + 16), v29 = (unsigned long)(v31 - 1), v31 != 1));
    }
    v34 = 0;
    ptr12 = sub_f80110(ptr10);
    v35 = *((long long *)&ptr12->padding_0[8]);
    v36 = ptr10;
    (*((long long *)&ptr12->padding_0[0]))();
}
```


## `CharacterDamage.GunPopupfunc` — RVA `0xc844cc`

- Decompiled symbol: `CharacterDamage_GunPopupfunc`
- Metadata signature: `private IEnumerator GunPopupfunc() { }`
- Native interval: `88` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

extern long long g_1ef2db0;
extern char g_1fab40d;

struct_0 * CharacterDamage_GunPopupfunc(void)
{
    struct_0 *ptr;  // x0

    if (!(g_1fab40d & 1))
    {
        sub_f7d92c(&g_1ef2db0);
        g_1fab40d = 1;
    }
    ptr = sub_f7db70(g_1ef2db0);
    Object__ctor(ptr, 0);
    ptr->field_10 = 0;
    return ptr;
}
```


## `CharacterDamage.<GunPopupfunc>d__40.ctor` — RVA `0xc84524`

- Decompiled symbol: `CharacterDamage_GunPopupfunc_d__40_ctor`
- Metadata signature: `public void .ctor(int <>1__state) { }`
- Native interval: `40` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

void CharacterDamage_GunPopupfunc_d__40_ctor(struct_0 *ptr, unsigned int a1)
{
    Object__ctor();
    ptr->field_10 = a1;
    return;
}
```


## `CharacterDamage.ctor` — RVA `0xc8454c`

- Decompiled symbol: `CharacterDamage_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `112` bytes
- Result: `pseudocode`
- Heuristic layout hint: `CharacterDamage_Recovered` matched 7 offsets against `CharacterDamage` metadata (confidence 0.88).

```c
typedef struct CharacterDamage_Recovered {
    char padding_0[64];
    unsigned int hitPoints;
    char padding_44[4];
    unsigned int attackForce;
    char padding_4c[28];
    unsigned long long gunItemRotation;
    unsigned int field_70;
    char padding_74[48];
    unsigned long long bodyStayTime;
    char padding_ac[4];
    char sloMoBackstab;
    char padding_b1[3];
    unsigned long long sloMoDeathTime;
    char padding_bc[40];
    unsigned int raymask;
} CharacterDamage_Recovered;

void CharacterDamage_ctor(struct_0 *ptr)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    ptr->field_40 = 0x42c80000;
    ptr->field_48 = 0x40300000;
    ptr->field_70 = 0x43340000;
    ptr->field_68 = 0x4334000000000000;
    ptr->padding_ac[0] = 1;
    *((unsigned long long *)&(&ptr->padding_74)[1]) = 0xbf80000041700000;
    *((unsigned long long *)&ptr->field_b0) = 4568451461350319718;
    *((unsigned int *)&ptr->padding_bc[36]) = LayerMask__op_Implicit(0x2000, 0);
}
```


## `CharacterDamage.<ApplyForce>d__38.Dispose` — RVA `0xc845bc`

- Decompiled symbol: `CharacterDamage_ApplyForce_d__38_Dispose`
- Metadata signature: `private void System.IDisposable.Dispose() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long CharacterDamage_ApplyForce_d__38_Dispose(void)
{
    unsigned long v0;  // x0

    return v0;
}
```


## `CharacterDamage.<ApplyForce>d__38.MoveNext` — RVA `0xc845c0`

- Decompiled symbol: `CharacterDamage_ApplyForce_d__38_MoveNext`
- Metadata signature: `private bool MoveNext() { }`
- Native interval: `672` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: Decompiler produced no C-like text

```c
// 0x10845c0: sub sp, sp, #0xc0
// 0x10845c4: stp d15, d14, [sp, #0x20]
// 0x10845c8: stp d13, d12, [sp, #0x30]
// 0x10845cc: stp d11, d10, [sp, #0x40]
// 0x10845d0: stp d9, d8, [sp, #0x50]
// 0x10845d4: str x30, [sp, #0x60]
// 0x10845d8: stp x28, x27, [sp, #0x70]
// 0x10845dc: stp x26, x25, [sp, #0x80]
// 0x10845e0: stp x24, x23, [sp, #0x90]
// 0x10845e4: stp x22, x21, [sp, #0xa0]
// 0x10845e8: stp x20, x19, [sp, #0xb0]
// 0x10845ec: adrp x20, #0x1fab000
// 0x10845f0: ldrb w8, [x20, #0x40f]
// 0x10845f4: mov x19, x0
// 0x10845f8: tbnz w8, #0, #0x1084610
// 0x10845fc: adrp x0, #0x1e8d000
// 0x1084600: ldr x0, [x0, #0x3e8]
// 0x1084604: bl #0xf7d92c
// 0x1084608: mov w8, #1
// 0x108460c: strb w8, [x20, #0x40f]
// 0x1084610: ldr w8, [x19, #0x10]
// 0x1084614: cmp w8, #1
// 0x1084618: b.eq #0x1084668
// 0x108461c: cbnz w8, #0x1084824
// 0x1084620: mov w8, #-1
// 0x1084624: str w8, [x19, #0x10]
// 0x1084628: adrp x8, #0x1e8d000
// 0x108462c: ldr x8, [x8, #0x3e8]
// 0x1084630: ldr x0, [x8]
// 0x1084634: bl #0xf7db70
// 0x1084638: adrp x8, #0x832000
// 0x108463c: ldr s0, [x8, #0x45c]
// 0x1084640: mov x1, xzr
// 0x1084644: mov x20, x0
// 0x1084648: bl #0x1b99b00
// 0x108464c: mov x0, x19
// 0x1084650: str x20, [x0, #0x18]!
// 0x1084654: mov x1, x20
// 0x1084658: bl #0xf7d8d0
// 0x108465c: mov w0, #1
// 0x1084660: str w0, [x19, #0x10]
// 0x1084664: b #0x1084828
// 0x1084668: ldr x22, [x19, #0x20]
// 0x108466c: mov w8, #-1
// 0x1084670: str w8, [x19, #0x10]
// 0x1084674: cbz x22, #0x1084858
// 0x1084678: ldrb w8, [x22, #0xe0]
// 0x108467c: cbz w8, #0x10847f8
// 0x1084680: ldr x23, [x22, #0x78]
// 0x1084684: cbz x23, #0x1084858
// 0x1084688: ldr w8, [x23, #0x18]
// 0x108468c: cmp w8, #1
// 0x1084690: b.lt #0x1084824
// 0x1084694: adrp x19, #0x1e8c000
// 0x1084698: adrp x9, #0x832000
// 0x108469c: adrp x20, #0x1e8c000
// 0x10846a0: ldr x19, [x19, #0x1e8]
// 0x10846a4: ldr s11, [x9, #0x41c]
// 0x10846a8: ldr x20, [x20, #0xa60]
// 0x10846ac: mov w24, wzr
// 0x10846b0: adrp x25, #0x1fab000
// 0x10846b4: mov w26, #1
// 0x10846b8: fmov v9.2s, #-2.50000000
// 0x10846bc: fmov s10, #-2.50000000
// 0x10846c0: adrp x27, #0x1fab000
// 0x10846c4: adrp x28, #0x1fab000
// 0x10846c8: cmp w24, w8
// 0x10846cc: b.hs #0x108485c
// 0x10846d0: ldr x0, [x22, #0xd8]
// 0x10846d4: cbz x0, #0x1084858
// 0x10846d8: add x8, x23, w24, sxtw #3
// 0x10846dc: ldr x21, [x8, #0x20]
// 0x10846e0: mov x1, xzr
// 0x10846e4: bl #0x1b9d508
// 0x10846e8: ldur d12, [x22, #0xbc]
// 0x10846ec: ldrb w8, [x25, #0x32c]
// 0x10846f0: ldr s13, [x22, #0xc4]
// 0x10846f4: mov v8.16b, v2.16b
// 0x10846f8: str d0, [sp, #0x10]
// 0x10846fc: str d1, [sp]
// 0x1084700: cbnz w8, #0x1084710
// 0x1084704: mov x0, x19
// 0x1084708: bl #0xf7d92c
// 0x108470c: strb w26, [x25, #0x32c]
// 0x1084710: ldr x8, [x19]
// 0x1084714: ldrb w9, [x27, #0x2c8]
// 0x1084718: ldr x8, [x8, #0xb8]
// 0x108471c: ldr d15, [x8, #0x18]
// 0x1084720: ldr s14, [x8, #0x20]
// 0x1084724: cbnz w9, #0x1084734
// 0x1084728: mov x0, x20
// 0x108472c: bl #0xf7d92c
// 0x1084730: strb w26, [x27, #0x2c8]
// 0x1084734: ldr x0, [x20]
// 0x1084738: ldr w8, [x0, #0xe0]
// 0x108473c: cbnz w8, #0x1084744
// 0x1084740: bl #0xf7da5c
// 0x1084744: ldp q3, q2, [sp]
// 0x1084748: fmul v0.2s, v15.2s, v9.2s
// 0x108474c: fmul s1, s14, s10
// 0x1084750: fadd v0.2s, v12.2s, v0.2s
// 0x1084754: mov v2.s[1], v3.s[0]
// 0x1084758: fadd s1, s13, s1
// 0x108475c: fsub v0.2s, v2.2s, v0.2s
// 0x1084760: fsub s1, s8, s1
// 0x1084764: fmul v2.2s, v0.2s, v0.2s
// 0x1084768: faddp s2, v2.2s
// 0x108476c: fmul s3, s1, s1
// 0x1084770: fadd s2, s3, s2
// 0x1084774: fsqrt s2, s2
// 0x1084778: fcmp s2, s11
// 0x108477c: b.le #0x1084790
// 0x1084780: dup v3.2s, v2.s[0]
// 0x1084784: fdiv v8.2s, v0.2s, v3.2s
// 0x1084788: fdiv s12, s1, s2
// 0x108478c: b #0x10847b4
// 0x1084790: ldrb w8, [x28, #0x2c9]
// 0x1084794: cbnz w8, #0x10847a4
// 0x1084798: mov x0, x19
// 0x108479c: bl #0xf7d92c
// 0x10847a0: strb w26, [x28, #0x2c9]
// 0x10847a4: ldr x8, [x19]
// 0x10847a8: ldr x8, [x8, #0xb8]
// 0x10847ac: ldr d8, [x8]
// 0x10847b0: ldr s12, [x8, #8]
// 0x10847b4: fmov s0, #2.50000000
// 0x10847b8: fmov s1, #4.50000000
// 0x10847bc: mov x0, xzr
// 0x10847c0: bl #0x1b9012c
// 0x10847c4: cbz x21, #0x1084858
// 0x10847c8: fmul s2, s12, s0
// 0x10847cc: fmul v0.2s, v8.2s, v0.s[0]
// 0x10847d0: mov s1, v0.s[1]
// 0x10847d4: mov w1, #1
// 0x10847d8: mov x0, x21
// 0x10847dc: mov x2, xzr
// 0x10847e0: bl #0x1bcf5b8
// 0x10847e4: ldr w8, [x23, #0x18]
// 0x10847e8: add w24, w24, #1
// 0x10847ec: cmp w24, w8
// 0x10847f0: b.lt #0x10846c8
// 0x10847f4: b #0x1084824
// 0x10847f8: ldr x0, [x19, #0x28]
// 0x10847fc: cbz x0, #0x1084858
// 0x1084800: ldr s0, [x22, #0x48]
// 0x1084804: ldp s3, s1, [x22, #0xcc]
// 0x1084808: ldr s4, [x22, #0xc8]
// 0x108480c: mov w1, #1
// 0x1084810: mov x2, xzr
// 0x1084814: fmul s2, s0, s1
// 0x1084818: fmul s1, s0, s3
// 0x108481c: fmul s0, s0, s4
// 0x1084820: bl #0x1bcf5b8
// 0x1084824: mov w0, wzr
// 0x1084828: ldp x20, x19, [sp, #0xb0]
// 0x108482c: ldp x22, x21, [sp, #0xa0]
// 0x1084830: ldp x24, x23, [sp, #0x90]
// 0x1084834: ldp x26, x25, [sp, #0x80]
// 0x1084838: ldp x28, x27, [sp, #0x70]
// 0x108483c: ldr x30, [sp, #0x60]
// 0x1084840: ldp d9, d8, [sp, #0x50]
// 0x1084844: ldp d11, d10, [sp, #0x40]
// 0x1084848: ldp d13, d12, [sp, #0x30]
// 0x108484c: ldp d15, d14, [sp, #0x20]
// 0x1084850: add sp, sp, #0xc0
// 0x1084854: ret
// 0x1084858: bl #0xf7db74
// 0x108485c: bl #0xf7db7c
```


## `CharacterDamage.<ApplyForce>d__38.get_Current` — RVA `0xc84860`

- Decompiled symbol: `CharacterDamage_ApplyForce_d__38_get_Current`
- Metadata signature: `private object System.Collections.Generic.IEnumerator<System.Object>.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long CharacterDamage_ApplyForce_d__38_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```


## `CharacterDamage.<ApplyForce>d__38.Reset` — RVA `0xc84868`

- Decompiled symbol: `CharacterDamage_ApplyForce_d__38_Reset`
- Metadata signature: `private void System.Collections.IEnumerator.Reset() { }`
- Native interval: `56` bytes
- Result: `pseudocode`

```c
extern long long g_1ef0bd8;
extern long long g_1f04268;

void CharacterDamage_ApplyForce_d__38_Reset(void)
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
    sub_f7da4c(v4, sub_f7d940(&g_1f04268));
}
```


## `CharacterDamage.<ApplyForce>d__38.get_Current` — RVA `0xc848a0`

- Decompiled symbol: `CharacterDamage_ApplyForce_d__38_get_Current`
- Metadata signature: `private object System.Collections.IEnumerator.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long CharacterDamage_ApplyForce_d__38_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```


## `CharacterDamage.<GunPopupfunc>d__40.Dispose` — RVA `0xc848a8`

- Decompiled symbol: `CharacterDamage_GunPopupfunc_d__40_Dispose`
- Metadata signature: `private void System.IDisposable.Dispose() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long CharacterDamage_GunPopupfunc_d__40_Dispose(void)
{
    unsigned long v0;  // x0

    return v0;
}
```


## `CharacterDamage.<GunPopupfunc>d__40.MoveNext` — RVA `0xc848ac`

- Decompiled symbol: `CharacterDamage_GunPopupfunc_d__40_MoveNext`
- Metadata signature: `private bool MoveNext() { }`
- Native interval: `152` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[4];
    long long field_18;
} struct_0;

extern long long g_1ef2440;
extern char g_1fab410;

unsigned int CharacterDamage_GunPopupfunc_d__40_MoveNext(struct_0 *ptr)
{
    unsigned int v0;  // w0
    long long v1;  // x20
    unsigned int v2;  // w8

    if (!(g_1fab410 & 1))
    {
        sub_f7d92c(&g_1ef2440);
        g_1fab410 = 1;
    }
    v0 = 0;
    if (ptr->field_10 == 1)
    {
        v2 = 4294967295;
    }
    else if (!ptr->field_10)
    {
        ptr->field_10 = 4294967295;
        v1 = sub_f7db70(g_1ef2440);
        WaitForSeconds__ctor(v1, 0);
        ptr->field_18 = v1;
        sub_f7d8d0(&ptr->field_18, v1);
        v2 = 1;
        v0 = 1;
    }
    else
    {
        return 0;
    }
    ptr->field_10 = v2;
    return v0;
}
```


## `CharacterDamage.<GunPopupfunc>d__40.get_Current` — RVA `0xc84944`

- Decompiled symbol: `CharacterDamage_GunPopupfunc_d__40_get_Current`
- Metadata signature: `private object System.Collections.Generic.IEnumerator<System.Object>.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long CharacterDamage_GunPopupfunc_d__40_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```


## `CharacterDamage.<GunPopupfunc>d__40.Reset` — RVA `0xc8494c`

- Decompiled symbol: `CharacterDamage_GunPopupfunc_d__40_Reset`
- Metadata signature: `private void System.Collections.IEnumerator.Reset() { }`
- Native interval: `56` bytes
- Result: `pseudocode`

```c
extern long long g_1ef0bd8;
extern long long g_1f04270;

void CharacterDamage_GunPopupfunc_d__40_Reset(void)
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
    sub_f7da4c(v4, sub_f7d940(&g_1f04270));
}
```


## `CharacterDamage.<GunPopupfunc>d__40.get_Current` — RVA `0xc84984`

- Decompiled symbol: `CharacterDamage_GunPopupfunc_d__40_get_Current`
- Metadata signature: `private object System.Collections.IEnumerator.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long CharacterDamage_GunPopupfunc_d__40_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```
