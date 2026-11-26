# Native pseudocode: AI

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `AI.Start` — RVA `0xc7cad0`

- Decompiled symbol: `AI_Start`
- Metadata signature: `private void Start() { }`
- Native interval: `552` bytes
- Result: `pseudocode`
- Heuristic layout hint: `AI_Recovered` matched 6 offsets against `AI` metadata (confidence 1.00).

```c
typedef struct struct_1 {
    char padding_0[40];
    unsigned long long field_28;
} struct_1;

typedef struct AI_Recovered {
    char padding_0[40];
    long long playerObj;
    char padding_30[8];
    struct struct_6 *NPCMgrObj;
    char padding_40[64];
    struct struct_8 *NPCRegistryComponent;
    char padding_88[8];
    long long agent;
    char padding_98[48];
    unsigned int randomSpawnChance;
    char padding_cc[52];
    struct struct_9 *myTransform;
} AI_Recovered;

typedef struct struct_3 {
    char padding_0[40];
    struct struct_2 *field_28;
} struct_3;

typedef struct struct_11 {
    char padding_0[16];
    unsigned long long field_10;
    unsigned int field_18;
    unsigned int field_1c;
} struct_11;

typedef struct struct_5 {
    char padding_0[32];
    struct struct_4 *field_20;
} struct_5;

typedef struct struct_6 {
    char padding_0[40];
    long long field_28;
} struct_6;

typedef struct struct_8 {
    char padding_0[40];
    struct struct_7 *field_28;
} struct_8;

typedef struct struct_9 {
    char padding_0[40];
    unsigned long long field_28;
} struct_9;

typedef struct struct_2 {
    char padding_0[16];
    unsigned long long field_10;
    unsigned int field_18;
    unsigned int field_1c;
} struct_2;

typedef struct struct_4 {
    char padding_0[40];
    unsigned long long field_28;
} struct_4;

typedef struct struct_7 {
    char padding_0[16];
    unsigned long long field_10;
    unsigned int field_18;
    unsigned int field_1c;
} struct_7;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern long long g_1ef7618;
extern long long g_1efcf38;
extern long long g_1efd038;
extern long long g_1efeb10;
extern long long g_1efec78;
extern long long g_1f0c4b8;
extern char g_1fab3ef;

int AI_Start(struct_10 *p)
{
    struct_1 *v0;  // x0
    struct_10 *addr;  // x20
    struct_5 *ptr7;  // x0
    unsigned long v11;  // x1
    struct_10 *ptr3;  // x0
    long long v13;  // x0
    struct_10 *ptr4;  // x20
    struct_10 *ptr8;  // x20
    unsigned int v16;  // w0
    unsigned int v17;  // s1
    unsigned int v18;  // s0
    unsigned long v19;  // 4129
    struct_10 *ptr6;  // x20
    struct_1 *ptr9;  // x0
    struct_3 *v4;  // x0
    struct_10 *ptr5;  // x20
    struct_10 *v6;  // x20
    struct_11 *ptr;  // x20
    unsigned long v8;  // x8
    unsigned long v9;  // x10

    if (!(g_1fab3ef & 1))
    {
        sub_f7d92c(&g_1efcf38);
        sub_f7d92c(&g_1efd038);
        sub_f7d92c(&g_1efeb10);
        sub_f7d92c(&g_1efec78);
        sub_f7d92c(&g_1ef7618);
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c(&g_1f0c4b8);
        g_1fab3ef = 1;
    }
    v0 = GameObject__Find(g_1f0c4b8, 0);
    addr = p;
    addr->field_38 = v0;
    ptr6 = &addr->field_38;
    sub_f7d8d0(ptr6, v0);
    ptr9 = *((long long *)&ptr6->padding_0[0]);
    if (ptr9)
    {
        v4 = sub_1249224(ptr9, g_1efec78);
        ptr5 = p;
        ptr5->field_80 = v4;
        v6 = &ptr5->field_80;
        ptr9 = sub_f7d8d0(v6, v4);
        if (*((long long *)&v6->padding_0[0]))
        {
            ptr9 = p->field_100;
            if (ptr9)
            {
                ptr = *((long long *)(*((long long *)&v6->padding_0[0]) + 40));
                ptr9 = Component__get_gameObject(ptr9, 0);
                if (ptr9)
                {
                    ptr9 = sub_1249224();
                    if (ptr)
                    {
                        v8 = ptr->field_10;
                        ptr->field_1c = ptr->field_1c + 1;
                        if (v8)
                        {
                            v9 = ptr->field_18;
                            if (*((int *)(v8 + 24)) > (unsigned int)v9)
                            {
                                ptr7 = v8 + v9 * 8;
                                ptr->field_18 = (unsigned int)v9 + 1;
                                ptr7->field_20 = ptr9;
                                sub_f7d8d0(&ptr7->field_20);
                            }
                            else
                            {
                                sub_14a3390(ptr);
                            }
                            ptr9 = Camera__get_main(0);
                            if (ptr9)
                            {
                                ptr9 = Component__get_transform();
                                if (ptr9)
                                {
                                    ptr9 = sub_1231bc8();
                                    if (ptr9)
                                    {
                                        v11 = ptr9->field_28;
                                        ptr3 = p;
                                        ptr3->field_28 = v11;
                                        sub_f7d8d0(&ptr3->field_28, v11);
                                        v13 = sub_1231bc8(p, g_1efd038);
                                        ptr4 = p;
                                        ptr4->field_90 = v13;
                                        ptr8 = &ptr4->field_90;
                                        sub_f7d8d0(ptr8, v13);
                                        v16 = Random__get_value(0);
                                        v17 = (int)ptr8->field_38;
                                        v19 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v18, v17)) >> 5 & 3 | (unsigned long long)(CmpF(v18, v17) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v18, v17)) >> 5 & 3 | (unsigned long long)(CmpF(v18, v17) & 1)) & ((unsigned long long)(char)(CmpF(v18, v17)) >> 5 & 3 | (unsigned long long)(CmpF(v18, v17) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                                        if ((char)v19)
                                            return v16;
                                        ptr9 = p->field_100;
                                        if (ptr9)
                                        {
                                            Component__get_gameObject(ptr9, 0);
                                            if (g_1ef0c58->field_e0)
                                                return Object__Destroy();
                                            sub_f7da5c(g_1ef0c58);
                                            return Object__Destroy();
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
    sub_f7db74(ptr9);
}
```


## `AI.OnEnable` — RVA `0xc7ccf8`

- Decompiled symbol: `AI_OnEnable`
- Metadata signature: `private void OnEnable() { }`
- Native interval: `1448` bytes
- Result: `pseudocode`
- Heuristic layout hint: `AI_Recovered` matched 2 offsets against `AI` metadata (confidence 1.00).

```c
typedef struct struct_11 {
    char padding_0[32];
    char field_20;
    char padding_21[7];
    struct struct_4 *field_28;
    long long field_30;
    char padding_38[16];
    long long field_48;
    long long field_50;
    long long field_58;
    char padding_60[16];
    long long field_70;
    char padding_78[32];
    long long field_98;
    char field_a0;
    char padding_a1[15];
    struct struct_5 *field_b0;
    char padding_b8[8];
    struct struct_6 *field_c0;
    char padding_c8[48];
    unsigned int field_f8;
    char padding_fc[4];
    struct struct_7 *field_100;
    unsigned long long field_108;
    unsigned int field_110;
    char padding_114[48];
    unsigned int field_144;
    unsigned int field_148;
    unsigned int field_14c;
    char padding_150[56];
    struct struct_8 *field_188;
    char padding_190[12];
    unsigned int field_19c;
    char padding_1a0[56];
    struct AI_Recovered *field_1d8;
    struct struct_10 *field_1e0;
    char padding_1e8[32];
    unsigned int field_208;
    char padding_20c[12];
    unsigned int field_218;
    char padding_21c[116];
    unsigned int field_290;
    char padding_294[8];
    unsigned int field_29c;
} struct_11;

typedef struct struct_3 {
    char padding_0[40];
    struct struct_3 *field_28;
    struct struct_3 *field_30;
} struct_3;

typedef struct struct_4 {
    char padding_0[40];
    struct struct_4 *field_28;
    struct struct_4 *field_30;
} struct_4;

typedef struct struct_5 {
    char padding_0[40];
    struct struct_5 *field_28;
    struct struct_5 *field_30;
} struct_5;

typedef struct struct_6 {
    char padding_0[40];
    struct struct_6 *field_28;
    struct struct_6 *field_30;
} struct_6;

typedef struct struct_7 {
    char padding_0[40];
    struct struct_7 *field_28;
    struct struct_7 *field_30;
} struct_7;

typedef struct struct_8 {
    char padding_0[40];
    struct struct_8 *field_28;
    struct struct_8 *field_30;
} struct_8;

typedef struct AI_Recovered {
    char padding_0[40];
    struct AI_Recovered *playerObj;
    struct AI_Recovered *playerTransform;
} AI_Recovered;

typedef struct struct_10 {
    char padding_0[40];
    struct struct_10 *field_28;
    struct struct_10 *field_30;
} struct_10;

typedef struct struct_1 {
    char padding_0[24];
    unsigned long long field_18;
    unsigned int field_20;
} struct_1;

typedef struct struct_2 {
    char padding_0[184];
    struct struct_1 *field_b8;
} struct_2;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern struct_2 *g_1ef22e8;
extern long long g_1efcf08;
extern long long g_1efcf38;
extern long long g_1efcf68;
extern long long g_1efd028;
extern long long g_1efd1b8;
extern long long g_1efea78;
extern long long g_1efebc0;
extern long long g_1efed60;
extern long long g_1f08598;
extern char g_1fab32c;
extern char g_1fab3f0;

long long AI_OnEnable(struct_11 *ptr)
{
    struct_3 *v0;  // x0
    struct_11 *ptr15;  // x20
    unsigned int v10;  // w0
    struct_11 *ptr6;  // x20
    struct_3 *v12;  // x21
    struct_11 *ptr4;  // x20
    struct_3 *v14;  // x0
    struct_3 *v15;  // x1
    struct_11 *ptr7;  // x0
    struct_3 *v17;  // x1
    struct_11 *ptr8;  // x20
    struct_11 *ptr16;  // x20
    struct_3 *cur;  // x0
    long long v20;  // x1
    struct_11 *ptr9;  // x0
    long long v22;  // x0
    struct_11 *ptr10;  // x20
    struct_11 *ptr17;  // x20
    long long v25;  // x1
    struct_11 *ptr11;  // x0
    long long v27;  // x1
    struct_11 *ptr12;  // x0
    long long v29;  // x1
    unsigned long long v3;  // d0
    struct_11 *ptr13;  // x0
    long long v31;  // x0
    struct_11 *ptr14;  // x20
    struct_11 *ptr5;  // x20
    long long v34;  // x0
    long long v35;  // x0
    unsigned int v4;  // s1
    unsigned int v5;  // s2
    struct_3 *v6;  // x0
    struct_11 *p;  // x21
    struct_3 *v8;  // x0
    struct_11 *addr;  // x20

    if (!(g_1fab3f0 & 1))
    {
        sub_f7d92c(&g_1efcf08);
        sub_f7d92c(&g_1efcf38);
        sub_f7d92c(&g_1efcf68);
        sub_f7d92c(&g_1efd028);
        sub_f7d92c(&g_1efd1b8);
        sub_f7d92c(&g_1efea78);
        sub_f7d92c(&g_1efed60);
        sub_f7d92c(&g_1efebc0);
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c(&g_1f08598);
        g_1fab3f0 = 1;
    }
    v0 = Component__get_transform(ptr, 0);
    ptr15 = &ptr->field_100;
    ptr->field_100 = v0;
    sub_f7d8d0(ptr15, v0);
    if (!g_1fab32c)
    {
        sub_f7d92c(&g_1ef22e8);
        g_1fab32c = 1;
    }
    cur = ptr->field_100;
    v3 = g_1ef22e8->field_b8->field_18;
    v4 = g_1ef22e8->field_b8->field_20;
    ptr->field_108 = v3;
    ptr->field_110 = v4;
    if (cur)
    {
        Transform__get_position(cur, 0);
        ptr->field_144 = v3;
        ptr->field_148 = v4;
        ptr->field_14c = v5;
        ptr->field_290 = 0;
        ptr->field_f8 = 0xc1800000;
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        if (((char)Object__op_Implicit(ptr->field_188, 0) & 1))
        {
            cur = ptr->field_188;
            if (cur)
            {
                AudioClip__get_length(cur, 0);
                ptr->field_19c = (unsigned int)v3 * 0xc0000000;
                goto LABEL_107ce64;
            }
        }
        else
        {
LABEL_107ce64:
            cur = ptr->field_100;
            ptr->field_a0 = 0;
            if (cur)
            {
                cur = Component__get_gameObject(cur, 0);
                if (cur)
                {
                    v6 = sub_124913c();
                    p = &ptr->field_1e0;
                    ptr->field_1e0 = v6;
                    sub_f7d8d0(p, v6);
                    cur = ptr->field_1e0;
                    if (cur)
                    {
                        AudioSource__set_spatialBlend(cur, 0);
                        cur = *((long long *)&p->padding_0[0]);
                        if (cur)
                        {
                            AudioSource__set_volume(cur, 0);
                            cur = ptr->field_1e0;
                            if (cur)
                            {
                                AudioSource__set_pitch(cur, 0);
                                cur = *((long long *)&p->padding_0[0]);
                                if (cur)
                                {
                                    AudioSource__set_dopplerLevel(cur, 0);
                                    cur = *((long long *)&p->padding_0[0]);
                                    if (cur)
                                    {
                                        AudioSource__set_bypassEffects(cur, 1, 0);
                                        cur = *((long long *)&p->padding_0[0]);
                                        if (cur)
                                        {
                                            AudioSource__set_bypassListenerEffects(cur, 1, 0);
                                            cur = *((long long *)&p->padding_0[0]);
                                            if (cur)
                                            {
                                                AudioSource__set_bypassReverbZones(cur, 1, 0);
                                                cur = *((long long *)&p->padding_0[0]);
                                                if (cur)
                                                {
                                                    AudioSource__set_maxDistance(cur, 0);
                                                    cur = *((long long *)&p->padding_0[0]);
                                                    if (cur)
                                                    {
                                                        AudioSource__set_rolloffMode(cur, 1, 0);
                                                        cur = *((long long *)&p->padding_0[0]);
                                                        if (cur)
                                                        {
                                                            AudioSource__set_playOnAwake(cur, 0, 0);
                                                            cur = *((long long *)&ptr15->padding_0[0]);
                                                            if (cur)
                                                            {
                                                                cur = Component__get_gameObject(cur, 0);
                                                                if (cur)
                                                                {
                                                                    v8 = sub_124913c();
                                                                    addr = &ptr->field_1d8;
                                                                    ptr->field_1d8 = v8;
                                                                    sub_f7d8d0(addr, v8);
                                                                    cur = ptr->field_1d8;
                                                                    if (cur)
                                                                    {
                                                                        AudioSource__set_spatialBlend(cur, 0);
                                                                        cur = *((long long *)&addr->padding_0[0]);
                                                                        if (cur)
                                                                        {
                                                                            AudioSource__set_volume(cur, 0);
                                                                            cur = ptr->field_1d8;
                                                                            if (cur)
                                                                            {
                                                                                AudioSource__set_pitch(cur, 0);
                                                                                cur = *((long long *)&addr->padding_0[0]);
                                                                                if (cur)
                                                                                {
                                                                                    AudioSource__set_dopplerLevel(cur, 0);
                                                                                    cur = *((long long *)&addr->padding_0[0]);
                                                                                    if (cur)
                                                                                    {
                                                                                        AudioSource__set_bypassEffects(cur, 1, 0);
                                                                                        cur = *((long long *)&addr->padding_0[0]);
                                                                                        if (cur)
                                                                                        {
                                                                                            AudioSource__set_bypassListenerEffects(cur, 1, 0);
                                                                                            cur = *((long long *)&addr->padding_0[0]);
                                                                                            if (cur)
                                                                                            {
                                                                                                AudioSource__set_bypassReverbZones(cur, 1, 0);
                                                                                                cur = *((long long *)&addr->padding_0[0]);
                                                                                                if (cur)
                                                                                                {
                                                                                                    AudioSource__set_maxDistance(cur, 0);
                                                                                                    cur = *((long long *)&addr->padding_0[0]);
                                                                                                    if (cur)
                                                                                                    {
                                                                                                        AudioSource__set_rolloffMode(cur, 1, 0);
                                                                                                        cur = *((long long *)&addr->padding_0[0]);
                                                                                                        if (cur)
                                                                                                        {
                                                                                                            AudioSource__set_playOnAwake(cur, 0, 0);
                                                                                                            v10 = LayerMask__op_Implicit(1059841, 0);
                                                                                                            ptr6 = ptr;
                                                                                                            v12 = ptr6->field_c0;
                                                                                                            ptr4 = &ptr6->field_c0;
                                                                                                            *((unsigned int *)((char *)&ptr4->field_1d8 + 4)) = v10;
                                                                                                            if (!g_1ef0c58->field_e0)
                                                                                                                sub_f7da5c(g_1ef0c58);
                                                                                                            if (((char)Object__op_Equality(v12, 0, 0) & 1))
                                                                                                            {
                                                                                                                v14 = Component__get_transform(ptr, 0);
                                                                                                                ptr->field_c0 = v14;
                                                                                                                sub_f7d8d0(ptr4, v14);
                                                                                                            }
                                                                                                            cur = *((long long *)&ptr4->padding_0[0]);
                                                                                                            if (cur)
                                                                                                            {
                                                                                                                v15 = sub_1231bc8(cur, g_1efcf08);
                                                                                                                ptr7 = ptr;
                                                                                                                ptr7->field_b0 = v15;
                                                                                                                sub_f7d8d0(&ptr7->field_b0, v15);
                                                                                                                cur = Camera__get_main(0);
                                                                                                                if (cur)
                                                                                                                {
                                                                                                                    cur = Component__get_transform();
                                                                                                                    if (cur)
                                                                                                                    {
                                                                                                                        cur = sub_1231bc8();
                                                                                                                        if (cur)
                                                                                                                        {
                                                                                                                            v17 = cur->field_28;
                                                                                                                            ptr8 = ptr;
                                                                                                                            ptr8->field_28 = v17;
                                                                                                                            ptr16 = &ptr8->field_28;
                                                                                                                            sub_f7d8d0(ptr16, v17);
                                                                                                                            cur = *((long long *)&ptr16->padding_0[0]);
                                                                                                                            if (cur)
                                                                                                                            {
                                                                                                                                v20 = GameObject__get_transform(cur, 0);
                                                                                                                                ptr9 = ptr;
                                                                                                                                ptr9->field_30 = v20;
                                                                                                                                sub_f7d8d0(&ptr9->field_30, v20);
                                                                                                                                cur = Camera__get_main(0);
                                                                                                                                if (cur)
                                                                                                                                {
                                                                                                                                    cur = Component__get_transform();
                                                                                                                                    if (cur)
                                                                                                                                    {
                                                                                                                                        cur = sub_1231bc8();
                                                                                                                                        if (cur)
                                                                                                                                        {
                                                                                                                                            cur = cur->field_30;
                                                                                                                                            if (cur)
                                                                                                                                            {
                                                                                                                                                v22 = sub_1249488(cur, g_1efed60);
                                                                                                                                                ptr10 = ptr;
                                                                                                                                                ptr10->field_58 = v22;
                                                                                                                                                ptr17 = &ptr10->field_58;
                                                                                                                                                sub_f7d8d0(ptr17, v22);
                                                                                                                                                cur = ptr17->field_30;
                                                                                                                                                if (cur)
                                                                                                                                                {
                                                                                                                                                    v25 = sub_1249224(cur, g_1efebc0);
                                                                                                                                                    ptr11 = ptr;
                                                                                                                                                    ptr11->field_48 = v25;
                                                                                                                                                    sub_f7d8d0(&ptr11->field_48, v25);
                                                                                                                                                    v27 = sub_1231bc8(ptr, g_1efd028);
                                                                                                                                                    ptr12 = ptr;
                                                                                                                                                    ptr12->field_50 = v27;
                                                                                                                                                    sub_f7d8d0(&ptr12->field_50, v27);
                                                                                                                                                    v29 = sub_1231bc8(ptr, g_1efcf68);
                                                                                                                                                    ptr13 = ptr;
                                                                                                                                                    ptr13->field_70 = v29;
                                                                                                                                                    sub_f7d8d0(&ptr13->field_70, v29);
                                                                                                                                                    v31 = sub_1232400(ptr, g_1efd1b8);
                                                                                                                                                    ptr14 = ptr;
                                                                                                                                                    ptr14->field_98 = v31;
                                                                                                                                                    ptr5 = &ptr14->field_98;
                                                                                                                                                    sub_f7d8d0(ptr5, v31);
                                                                                                                                                    cur = *((long long *)&ptr5->padding_0[24]);
                                                                                                                                                    *((int *)&ptr5->padding_150[48]) = *((int *)&ptr5->padding_150[32]);
                                                                                                                                                    if (cur)
                                                                                                                                                    {
                                                                                                                                                        v34 = Animator__SetInteger(cur, g_1f08598, 0, 0);
                                                                                                                                                        if (!ptr->field_20)
                                                                                                                                                        {
                                                                                                                                                            MonoBehaviour__StopAllCoroutines(ptr, 0);
                                                                                                                                                            AI__SpawnNPC();
                                                                                                                                                            v35 = MonoBehaviour__StartCoroutine();
                                                                                                                                                            return MonoBehaviour__StartCoroutine();
                                                                                                                                                        }
                                                                                                                                                        return v34;
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
    sub_f7db74(cur);
}
```


## `AI.SpawnNPC` — RVA `0xc7d2a0`

- Decompiled symbol: `AI_SpawnNPC`
- Metadata signature: `public IEnumerator SpawnNPC() { }`
- Native interval: `108` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[12];
    long long field_20;
} struct_0;

extern long long g_1ef2b50;
extern char g_1fab3f1;

struct_0 * AI_SpawnNPC(long long a0)
{
    struct_0 *v0;  // x20
    struct_0 *ptr;  // x0

    if (!(g_1fab3f1 & 1))
    {
        sub_f7d92c(&g_1ef2b50);
        g_1fab3f1 = 1;
    }
    v0 = sub_f7db70(g_1ef2b50);
    Object__ctor(v0, 0);
    ptr = v0;
    ptr->field_10 = 0;
    ptr->field_20 = a0;
    sub_f7d8d0(&ptr->field_20, a0);
    return ptr;
}
```


## `AI.<SpawnNPC>d__127.ctor` — RVA `0xc7d30c`

- Decompiled symbol: `AI_SpawnNPC_d__127_ctor`
- Metadata signature: `public void .ctor(int <>1__state) { }`
- Native interval: `40` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

void AI_SpawnNPC_d__127_ctor(struct_0 *ptr, unsigned int a1)
{
    Object__ctor();
    ptr->field_10 = a1;
    return;
}
```


## `AI.OnDrawGizmos` — RVA `0xc7d334`

- Decompiled symbol: `AI_OnDrawGizmos`
- Metadata signature: `private void OnDrawGizmos() { }`
- Native interval: `1748` bytes
- Result: `pseudocode`
- Heuristic layout hint: `AI_Recovered` matched 5 offsets against `AI` metadata (confidence 0.71).

```c
typedef struct AI_Recovered {
    char padding_0[144];
    long long agent;
    char padding_98[404];
    unsigned int eyeHeight;
    char drawDebugGizmos;
    char padding_231[7];
    long long target;
    char padding_240[68];
    unsigned int lastVisibleTargetPosition;
    unsigned int field_288;
    unsigned int field_28c;
} AI_Recovered;

typedef struct struct_4 {
    unsigned int field_0;
    unsigned int field_4;
    unsigned int field_8;
} struct_4;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

typedef struct struct_1 {
    char padding_0[224];
    unsigned int field_e0;
} struct_1;

typedef struct struct_3 {
    char padding_0[184];
    struct struct_4 *field_b8;
} struct_3;

extern struct_0 *g_1ef0c58;
extern struct_1 *g_1ef0e48;
extern struct_3 *g_1ef22e8;
extern long long g_1efd038;
extern char g_1fab2c8;
extern char g_1fab2c9;
extern char g_1fab3e0;
extern char g_1fab3f2;

struct_5 * AI_OnDrawGizmos(struct_5 *ptr)
{
    struct_5 *v7;  // x0
    struct_5 *v8;  // x0
    unsigned long v17;  // 4205
    unsigned int v18;  // s4
    unsigned int v19;  // s5
    unsigned int v20;  // s6
    unsigned int p[3];  // x8
    unsigned int v22;  // w0
    unsigned long v23;  // cc_dep1
    struct_5 *v9;  // x0
    unsigned long v24;  // 4113
    unsigned long v25;  // 4106
    unsigned long v26;  // 4106
    long long v27;  // x1
    unsigned long long v28;  // x0
    unsigned int v10;  // s1
    unsigned int v11;  // s3
    unsigned int v12;  // s15
    unsigned int v13;  // s14
    unsigned int v14;  // s9
    unsigned int v15;  // s2
    unsigned int v16;  // s0
    unsigned int v0;  // [bp-0x7c]
    unsigned int v1;  // [bp-0x78]
    unsigned int v2;  // [bp-0x74]
    unsigned int v3;  // [bp-0x70]
    unsigned int v4;  // [bp-0x6c]
    unsigned int v5;  // [bp-0x68]
    unsigned int v6;  // [bp-0x64]

    v7 = ptr;
    if (!(g_1fab3f2 & 1))
    {
        sub_f7d92c(&g_1efd038);
        sub_f7d92c(&g_1ef0c58);
        v8 = sub_f7d92c(&g_1ef0e48);
        g_1fab3f2 = 1;
        v7 = v8;
    }
    v9 = v7;
    if (!ptr->field_230)
        return v9;
    Gizmos__set_color(0);
    if (Component__get_transform(ptr, 0))
    {
        Transform__get_position();
        Gizmos__DrawSphere(0);
        Gizmos__set_color(0);
        if (Component__get_transform(ptr, 0))
        {
            Transform__get_position();
            v10 = 0 + ptr->field_22c;
            Gizmos__DrawSphere(0);
            if (Component__get_transform(ptr, 0) && (v2 = 1015054465, v3 = 1064037356, v5 = 1045220557, Transform__get_position(), Component__get_transform(ptr, 0)))
            {
                Transform__get_up();
                v11 = ptr->field_22c;
                v12 = ptr->field_284;
                v13 = ptr->field_288;
                v14 = ptr->field_28c;
                v15 = 0 + 0 * v11;
                v6 = v15;
                if (!g_1fab2c8)
                {
                    sub_f7d92c("_F");
                    v15 = v6;
                    g_1fab2c8 = 1;
                }
                if (!g_1ef07e8->field_e0)
                    sub_f7da5c(g_1ef07e8);
                v16 = [D] unsupported_Iop_SqrtF32();
                v17 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v16, 925353388)) >> 5 & 3 | (unsigned long long)(CmpF(v16, 925353388) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v16, 925353388)) >> 5 & 3 | (unsigned long long)(CmpF(v16, 925353388) & 1)) & ((unsigned long long)(char)(CmpF(v16, 925353388)) >> 5 & 3 | (unsigned long long)(CmpF(v16, 925353388) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                if (!((char)v17))
                {
                    v18 = (v12 - (0x3f800000 + 0x3f800000 * v11)) / v16;
                    v19 = (v13 - (v10 + v10 * v11)) / v16;
                    v20 = (v14 - v15) / v16;
                }
                else
                {
                    if (!g_1fab2c9)
                    {
                        sub_f7d92c(&g_1ef22e8);
                        g_1fab2c9 = 1;
                    }
                    p = g_1ef22e8->field_b8;
                    v18 = p[0];
                    v19 = p[1];
                    v20 = p[2];
                }
                if (!g_1fab3e0)
                {
                    sub_f7d92c("_F");
                    g_1fab3e0 = 1;
                }
                if (!g_1ef07e8->field_e0)
                {
                    v4 = v18;
                    v0 = v20;
                    v1 = v19;
                    sub_f7da5c(g_1ef07e8);
                }
                v4 = v14;
                if (!g_1ef0e48->field_e0)
                    sub_f7da5c(g_1ef0e48);
                v22 = Physics__Linecast(0);
                v23 = v22 & 1;
                v24 = arm64g_calculate_condition(25, (unsigned long long)(v22 & 1), 0, 0);
                if ((char)v24)
                {
                    v25 = arm64g_calculate_condition(25, v23, 0, 0);
                    if (!((char)v25))
                        goto LABEL_107d67e;
LABEL_107d67d:
                }
                else
                {
                    v26 = arm64g_calculate_condition(25, v23, 0, 0);
                    if ((char)v26)
                        goto LABEL_107d67d;
LABEL_107d67e:
                }
                Gizmos__set_color();
                Gizmos__DrawLine(0);
                Gizmos__DrawSphere(0);
                if (!g_1ef0c58->field_e0)
                    sub_f7da5c(g_1ef0c58);
                if (((char)Object__op_Implicit(ptr->field_238, 0) & 1))
                {
                    Gizmos__set_color(0);
                    if (ptr->field_238 && (Transform__get_position(ptr->field_238, 0), Component__get_transform(ptr, 0)))
                    {
                        Transform__get_up();
                        Gizmos__DrawLine(0);
                        goto LABEL_107d774;
                    }
                }
                else
                {
LABEL_107d774:
                    Gizmos__set_color(0);
                    if (Component__get_transform(ptr, 0))
                    {
                        Transform__get_position();
                        if (Component__get_transform(ptr, 0))
                        {
                            Transform__get_forward();
                            if (Component__get_transform(ptr, 0))
                            {
                                Transform__get_up();
                                Gizmos__DrawSphere(0);
                                if (Component__get_transform(ptr, 0))
                                {
                                    Transform__get_forward();
                                    Quaternion__Internal_FromEulerRad(0);
                                    Quaternion__op_Multiply(0);
                                    v27 = sub_1231bc8(ptr, g_1efd038);
                                    ptr->field_90 = v27;
                                    sub_f7d8d0(&ptr->field_90, v27);
                                    Gizmos__set_color(0);
                                    if (Component__get_transform(ptr, 0))
                                    {
                                        Transform__get_position();
                                        if (Component__get_transform(ptr, 0))
                                        {
                                            Transform__get_up();
                                            if (ptr->field_90)
                                            {
                                                NavMeshAgent__get_radius(ptr->field_90, 0);
                                                Gizmos__DrawSphere(0);
                                                if (Component__get_transform(ptr, 0))
                                                {
                                                    Transform__get_position();
                                                    if (Component__get_transform(ptr, 0))
                                                    {
                                                        Transform__get_up();
                                                        if (ptr->field_90)
                                                        {
                                                            NavMeshAgent__get_radius(ptr->field_90, 0);
                                                            v28 = Gizmos__DrawSphere();
                                                            return Gizmos__DrawSphere();
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
    sub_f7db74();
}
```


## `AI.InitializeAnim` — RVA `0xc7da08`

- Decompiled symbol: `AI_InitializeAnim`
- Metadata signature: `private void InitializeAnim() { }`
- Native interval: `36` bytes
- Result: `pseudocode`

```c
void* AI_InitializeAnim(void* ptr)
{
    if (!(char)ptr[306] && !(char)ptr[307])
    {
        *((unsigned short *)&ptr[306]) = 257;
        return ptr;
    }
    *((char *)&ptr[306]) = 0;
    return ptr;
}
```


## `AI.StandWatch` — RVA `0xc7da2c`

- Decompiled symbol: `AI_StandWatch`
- Metadata signature: `private IEnumerator StandWatch() { }`
- Native interval: `108` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[12];
    long long field_20;
} struct_0;

extern long long g_1ef2b58;
extern char g_1fab3f3;

struct_0 * AI_StandWatch(long long a0)
{
    struct_0 *v0;  // x20
    struct_0 *ptr;  // x0

    if (!(g_1fab3f3 & 1))
    {
        sub_f7d92c(&g_1ef2b58);
        g_1fab3f3 = 1;
    }
    v0 = sub_f7db70(g_1ef2b58);
    Object__ctor(v0, 0);
    ptr = v0;
    ptr->field_10 = 0;
    ptr->field_20 = a0;
    sub_f7d8d0(&ptr->field_20, a0);
    return ptr;
}
```


## `AI.<StandWatch>d__130.ctor` — RVA `0xc7da98`

- Decompiled symbol: `AI_StandWatch_d__130_ctor`
- Metadata signature: `public void .ctor(int <>1__state) { }`
- Native interval: `40` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

void AI_StandWatch_d__130_ctor(struct_0 *ptr, unsigned int a1)
{
    Object__ctor();
    ptr->field_10 = a1;
    return;
}
```


## `AI.Patrol` — RVA `0xc7dac0`

- Decompiled symbol: `AI_Patrol`
- Metadata signature: `private IEnumerator Patrol() { }`
- Native interval: `108` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[12];
    long long field_20;
} struct_0;

extern long long g_1ef2b30;
extern char g_1fab3f4;

struct_0 * AI_Patrol(long long a0)
{
    struct_0 *v0;  // x20
    struct_0 *ptr;  // x0

    if (!(g_1fab3f4 & 1))
    {
        sub_f7d92c(&g_1ef2b30);
        g_1fab3f4 = 1;
    }
    v0 = sub_f7db70(g_1ef2b30);
    Object__ctor(v0, 0);
    ptr = v0;
    ptr->field_10 = 0;
    ptr->field_20 = a0;
    sub_f7d8d0(&ptr->field_20, a0);
    return ptr;
}
```


## `AI.<Patrol>d__131.ctor` — RVA `0xc7db2c`

- Decompiled symbol: `AI_Patrol_d__131_ctor`
- Metadata signature: `public void .ctor(int <>1__state) { }`
- Native interval: `40` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

void AI_Patrol_d__131_ctor(struct_0 *ptr, unsigned int a1)
{
    Object__ctor();
    ptr->field_10 = a1;
    return;
}
```


## `AI.CanSeeTarget` — RVA `0xc7db54`

- Decompiled symbol: `AI_CanSeeTarget`
- Metadata signature: `private void CanSeeTarget() { }`
- Native interval: `3940` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: Decompiler produced no C-like text

```c
// 0x107db54: sub sp, sp, #0xb0
// 0x107db58: stp d15, d14, [sp, #0x10]
// 0x107db5c: stp d13, d12, [sp, #0x20]
// 0x107db60: stp d11, d10, [sp, #0x30]
// 0x107db64: stp d9, d8, [sp, #0x40]
// 0x107db68: stp x29, x30, [sp, #0x50]
// 0x107db6c: stp x28, x27, [sp, #0x60]
// 0x107db70: stp x26, x25, [sp, #0x70]
// 0x107db74: stp x24, x23, [sp, #0x80]
// 0x107db78: stp x22, x21, [sp, #0x90]
// 0x107db7c: stp x20, x19, [sp, #0xa0]
// 0x107db80: adrp x20, #0x1fab000
// 0x107db84: ldrb w8, [x20, #0x3f5]
// 0x107db88: mov x19, x0
// 0x107db8c: tbnz w8, #0, #0x107dbb0
// 0x107db90: adrp x0, #0x1e8c000
// 0x107db94: ldr x0, [x0, #0xd8]
// 0x107db98: bl #0xf7d92c
// 0x107db9c: adrp x0, #0x1e8d000
// 0x107dba0: ldr x0, [x0, #0x4a8]
// 0x107dba4: bl #0xf7d92c
// 0x107dba8: mov w8, #1
// 0x107dbac: strb w8, [x20, #0x3f5]
// 0x107dbb0: ldr s8, [x19, #0x150]
// 0x107dbb4: mov x0, xzr
// 0x107dbb8: bl #0x1b9ad30
// 0x107dbbc: fmov s1, #1.00000000
// 0x107dbc0: fadd s1, s8, s1
// 0x107dbc4: fcmp s1, s0
// 0x107dbc8: b.gt #0x107e99c
// 0x107dbcc: adrp x25, #0x1e8c000
// 0x107dbd0: ldr x25, [x25, #0xd8]
// 0x107dbd4: mov x21, x19
// 0x107dbd8: ldr x20, [x21, #0x88]!
// 0x107dbdc: ldr x0, [x25]
// 0x107dbe0: ldr w8, [x0, #0xe0]
// 0x107dbe4: cbnz w8, #0x107dbec
// 0x107dbe8: bl #0xf7da5c
// 0x107dbec: mov x0, x20
// 0x107dbf0: mov x1, xzr
// 0x107dbf4: bl #0x1b98274
// 0x107dbf8: tbz w0, #0, #0x107dc10
// 0x107dbfc: ldr x0, [x21]
// 0x107dc00: cbz x0, #0x107eab0
// 0x107dc04: mov x1, xzr
// 0x107dc08: bl #0x1b91624
// 0x107dc0c: tbz w0, #0, #0x107e2a0
// 0x107dc10: ldr x0, [x25]
// 0x107dc14: ldr x22, [x19, #0x238]
// 0x107dc18: ldr w8, [x0, #0xe0]
// 0x107dc1c: cbnz w8, #0x107dc24
// 0x107dc20: bl #0xf7da5c
// 0x107dc24: mov x0, x22
// 0x107dc28: mov x1, xzr
// 0x107dc2c: add x20, x19, #0x238
// 0x107dc30: bl #0x1b98274
// 0x107dc34: tbz w0, #0, #0x107dc58
// 0x107dc38: ldr x0, [x20]
// 0x107dc3c: cbz x0, #0x107eab0
// 0x107dc40: mov x1, xzr
// 0x107dc44: bl #0x1b92190
// 0x107dc48: cbz x0, #0x107eab0
// 0x107dc4c: mov x1, xzr
// 0x107dc50: bl #0x1b94d50
// 0x107dc54: tbz w0, #0, #0x107e2a0
// 0x107dc58: ldr w8, [x19, #0xf0]
// 0x107dc5c: adrp x26, #0x1e8c000
// 0x107dc60: ldr x26, [x26, #0xa60]
// 0x107dc64: adrp x27, #0x1fab000
// 0x107dc68: cmp w8, #1
// 0x107dc6c: b.ne #0x107dc78
// 0x107dc70: ldrb w8, [x19, #0xf5]
// 0x107dc74: cbz w8, #0x107e0ac
// 0x107dc78: ldr x8, [x19, #0x48]
// 0x107dc7c: cbz x8, #0x107eab0
// 0x107dc80: ldr x0, [x25]
// 0x107dc84: ldr x22, [x8, #0x238]
// 0x107dc88: ldr w9, [x0, #0xe0]
// 0x107dc8c: cbnz w9, #0x107dc94
// 0x107dc90: bl #0xf7da5c
// 0x107dc94: mov x0, x22
// 0x107dc98: mov x1, xzr
// 0x107dc9c: bl #0x1b98274
// 0x107dca0: tbz w0, #0, #0x107e0ac
// 0x107dca4: ldr x0, [x19, #0x100]
// 0x107dca8: cbz x0, #0x107eab0
// 0x107dcac: mov x1, xzr
// 0x107dcb0: bl #0x1b9d508
// 0x107dcb4: ldr x0, [x19, #0x30]
// 0x107dcb8: cbz x0, #0x107eab0
// 0x107dcbc: ldr s14, [x19, #0x108]
// 0x107dcc0: ldr s15, [x19, #0x10c]
// 0x107dcc4: ldr s8, [x19, #0x110]
// 0x107dcc8: ldr s9, [x19, #0x22c]
// 0x107dccc: mov x1, xzr
// 0x107dcd0: mov v10.16b, v2.16b
// 0x107dcd4: mov v13.16b, v1.16b
// 0x107dcd8: mov v11.16b, v0.16b
// 0x107dcdc: bl #0x1b9d508
// 0x107dce0: ldr x8, [x19, #0x48]
// 0x107dce4: cbz x8, #0x107eab0
// 0x107dce8: ldr x0, [x8, #0x238]
// 0x107dcec: stp s1, s2, [sp, #8]
// 0x107dcf0: cbz x0, #0x107eab0
// 0x107dcf4: mov v12.16b, v0.16b
// 0x107dcf8: fmul s0, s14, s9
// 0x107dcfc: fmul s1, s15, s9
// 0x107dd00: fmul s2, s8, s9
// 0x107dd04: ldr s8, [x19, #0x108]
// 0x107dd08: ldr s9, [x19, #0x10c]
// 0x107dd0c: ldr s14, [x19, #0x110]
// 0x107dd10: mov x1, xzr
// 0x107dd14: fadd s15, s11, s0
// 0x107dd18: fadd s11, s13, s1
// 0x107dd1c: fadd s13, s10, s2
// 0x107dd20: bl #0x1bcfdf0
// 0x107dd24: fmul s1, s8, s0
// 0x107dd28: fmov s3, #0.25000000
// 0x107dd2c: fmul s1, s1, s3
// 0x107dd30: fadd s8, s12, s1
// 0x107dd34: ldr s1, [sp, #8]
// 0x107dd38: fmul s2, s9, s0
// 0x107dd3c: fmul s2, s2, s3
// 0x107dd40: ldrb w8, [x27, #0x3e0]
// 0x107dd44: fadd s9, s1, s2
// 0x107dd48: ldr s1, [sp, #0xc]
// 0x107dd4c: fmul s0, s14, s0
// 0x107dd50: fmul s0, s0, s3
// 0x107dd54: fadd s12, s1, s0
// 0x107dd58: cbnz w8, #0x107dd70
// 0x107dd5c: adrp x0, #0x1e8c000
// 0x107dd60: ldr x0, [x0, #0xa60]
// 0x107dd64: bl #0xf7d92c
// 0x107dd68: mov w8, #1
// 0x107dd6c: strb w8, [x27, #0x3e0]
// 0x107dd70: ldr x0, [x26]
// 0x107dd74: fsub s10, s15, s8
// 0x107dd78: fsub s9, s11, s9
// 0x107dd7c: fsub s8, s13, s12
// 0x107dd80: ldr w8, [x0, #0xe0]
// 0x107dd84: cbnz w8, #0x107dd8c
// 0x107dd88: bl #0xf7da5c
// 0x107dd8c: fmul s0, s10, s10
// 0x107dd90: fmul s1, s9, s9
// 0x107dd94: ldrb w8, [x19, #0x294]
// 0x107dd98: fadd s0, s0, s1
// 0x107dd9c: fmul s1, s8, s8
// 0x107dda0: fadd s0, s1, s0
// 0x107dda4: fsqrt s8, s0
// 0x107dda8: cbnz w8, #0x107df20
// 0x107ddac: ldrb w8, [x19, #0x114]
// 0x107ddb0: cbnz w8, #0x107df20
// 0x107ddb4: ldr x8, [x19, #0x48]
// 0x107ddb8: cbz x8, #0x107eab0
// 0x107ddbc: ldr s9, [x8, #0x19c]
// 0x107ddc0: mov x0, xzr
// 0x107ddc4: bl #0x1b9ad30
// 0x107ddc8: fmov s1, #2.50000000
// 0x107ddcc: fadd s1, s9, s1
// 0x107ddd0: fcmp s1, s0
// 0x107ddd4: b.pl #0x107df20
// 0x107ddd8: ldr s0, [x19, #0x20c]
// 0x107dddc: fcmp s8, s0
// 0x107dde0: b.pl #0x107df20
// 0x107dde4: ldr x0, [x25]
// 0x107dde8: ldr x22, [x19, #0x238]
// 0x107ddec: ldr x23, [x19, #0x30]
// 0x107ddf0: ldr w8, [x0, #0xe0]
// 0x107ddf4: cbnz w8, #0x107ddfc
// 0x107ddf8: bl #0xf7da5c
// 0x107ddfc: mov x0, x22
// 0x107de00: mov x1, x23
// 0x107de04: mov x2, xzr
// 0x107de08: bl #0x1b9568c
// 0x107de0c: tbnz w0, #0, #0x107de80
// 0x107de10: ldr x8, [x19, #0x48]
// 0x107de14: cbz x8, #0x107eab0
// 0x107de18: ldr x0, [x8, #0x160]
// 0x107de1c: cbz x0, #0x107eab0
// 0x107de20: ldr x22, [x19, #0x238]
// 0x107de24: mov x1, xzr
// 0x107de28: bl #0x1b94c14
// 0x107de2c: ldr x8, [x25]
// 0x107de30: mov x23, x0
// 0x107de34: ldr w9, [x8, #0xe0]
// 0x107de38: cbnz w9, #0x107de44
// 0x107de3c: mov x0, x8
// 0x107de40: bl #0xf7da5c
// 0x107de44: mov x0, x22
// 0x107de48: mov x1, x23
// 0x107de4c: mov x2, xzr
// 0x107de50: bl #0x1b9568c
// 0x107de54: tbnz w0, #0, #0x107de80
// 0x107de58: ldr x0, [x25]
// 0x107de5c: ldr x22, [x20]
// 0x107de60: ldr w8, [x0, #0xe0]
// 0x107de64: cbnz w8, #0x107de6c
// 0x107de68: bl #0xf7da5c
// 0x107de6c: mov x0, x22
// 0x107de70: mov x1, xzr
// 0x107de74: mov x2, xzr
// 0x107de78: bl #0x1b9568c
// 0x107de7c: tbz w0, #0, #0x107df20
// 0x107de80: ldr x0, [x25]
// 0x107de84: ldr x22, [x19, #0x58]
// 0x107de88: ldr w8, [x0, #0xe0]
// 0x107de8c: cbnz w8, #0x107de94
// 0x107de90: bl #0xf7da5c
// 0x107de94: mov x0, x22
// 0x107de98: mov x1, xzr
// 0x107de9c: bl #0x1b98274
// 0x107dea0: tbz w0, #0, #0x107df20
// 0x107dea4: ldr x8, [x19, #0x58]
// 0x107dea8: cbz x8, #0x107eab0
// 0x107deac: ldr x0, [x25]
// 0x107deb0: ldr x22, [x8, #0x98]
// 0x107deb4: ldr w9, [x0, #0xe0]
// 0x107deb8: cbnz w9, #0x107dec0
// 0x107debc: bl #0xf7da5c
// 0x107dec0: mov x0, x22
// 0x107dec4: mov x1, xzr
// 0x107dec8: bl #0x1b98274
// 0x107decc: tbz w0, #0, #0x107df20
// 0x107ded0: ldr x8, [x19, #0x58]
// 0x107ded4: cbz x8, #0x107eab0
// 0x107ded8: ldr x1, [x8, #0x98]
// 0x107dedc: mov x22, x19
// 0x107dee0: str x1, [x22, #0x60]!
// 0x107dee4: mov x0, x22
// 0x107dee8: bl #0xf7d8d0
// 0x107deec: ldr x8, [x22]
// 0x107def0: cbz x8, #0x107eab0
// 0x107def4: ldr s9, [x8, #0x1fc]
// 0x107def8: mov x0, xzr
// 0x107defc: bl #0x1b9ad30
// 0x107df00: fmov s1, #2.00000000
// 0x107df04: fadd s1, s9, s1
// 0x107df08: fcmp s1, s0
// 0x107df0c: b.le #0x107df20
// 0x107df10: ldr x8, [x22]
// 0x107df14: cbz x8, #0x107eab0
// 0x107df18: ldrb w8, [x8, #0x1f1]
// 0x107df1c: cbz w8, #0x107e9dc
// 0x107df20: ldrb w8, [x19, #0x114]
// 0x107df24: cbz w8, #0x107df5c
// 0x107df28: ldr x8, [x19, #0x48]
// 0x107df2c: cbz x8, #0x107eab0
// 0x107df30: ldr x0, [x8, #0x238]
// 0x107df34: cbz x0, #0x107eab0
// 0x107df38: mov x1, xzr
// 0x107df3c: bl #0x1bcfdf0
// 0x107df40: ldr x1, [x19, #0x30]
// 0x107df44: fmov s1, #0.25000000
// 0x107df48: fmul s0, s0, s1
// 0x107df4c: mov x0, x20
// 0x107df50: str s0, [x19, #0x27c]
// 0x107df54: str x1, [x19, #0x238]
// 0x107df58: bl #0xf7d8d0
// 0x107df5c: ldr s0, [x19, #0x218]
// 0x107df60: fcmp s8, s0
// 0x107df64: b.pl #0x107e0ac
// 0x107df68: ldr x8, [x19, #0x48]
// 0x107df6c: cbz x8, #0x107eab0
// 0x107df70: fmov s0, #2.00000000
// 0x107df74: fcmp s8, s0
// 0x107df78: adrp x24, #0x832000
// 0x107df7c: b.le #0x107e010
// 0x107df80: ldr s0, [x8, #0x170]
// 0x107df84: ldr s1, [x24, #0x3b8]
// 0x107df88: fabs s0, s0
// 0x107df8c: fcmp s0, s1
// 0x107df90: b.le #0x107e010
// 0x107df94: ldr x0, [x25]
// 0x107df98: ldr x22, [x19, #0x238]
// 0x107df9c: ldr x23, [x19, #0x30]
// 0x107dfa0: ldr w8, [x0, #0xe0]
// 0x107dfa4: cbnz w8, #0x107dfac
// 0x107dfa8: bl #0xf7da5c
// 0x107dfac: mov x0, x22
// 0x107dfb0: mov x1, x23
// 0x107dfb4: mov x2, xzr
// 0x107dfb8: bl #0x1b9568c
// 0x107dfbc: tbz w0, #0, #0x107e010
// 0x107dfc0: ldr s9, [x19, #0xf8]
// 0x107dfc4: mov x0, xzr
// 0x107dfc8: bl #0x1b9ad30
// 0x107dfcc: fmov s1, #6.00000000
// 0x107dfd0: fadd s1, s9, s1
// 0x107dfd4: fcmp s1, s0
// 0x107dfd8: b.gt #0x107dfe4
// 0x107dfdc: ldrb w8, [x19, #0x294]
// 0x107dfe0: cbz w8, #0x107e010
// 0x107dfe4: ldr x8, [x19, #0x48]
// 0x107dfe8: str wzr, [x19, #0x27c]
// 0x107dfec: cbz x8, #0x107eab0
// 0x107dff0: ldr x0, [x8, #0x160]
// 0x107dff4: cbz x0, #0x107eab0
// 0x107dff8: mov x1, xzr
// 0x107dffc: bl #0x1b94c14
// 0x107e000: mov x1, x0
// 0x107e004: str x0, [x20]
// 0x107e008: mov x0, x20
// 0x107e00c: bl #0xf7d8d0
// 0x107e010: ldr x8, [x19, #0x48]
// 0x107e014: cbz x8, #0x107eab0
// 0x107e018: fmov s0, #2.00000000
// 0x107e01c: fcmp s8, s0
// 0x107e020: b.mi #0x107e038
// 0x107e024: ldr s0, [x8, #0x170]
// 0x107e028: ldr s1, [x24, #0x3b8]
// 0x107e02c: fabs s0, s0
// 0x107e030: fcmp s0, s1
// 0x107e034: b.pl #0x107e0ac
// 0x107e038: ldr x0, [x8, #0x160]
// 0x107e03c: cbz x0, #0x107eab0
// 0x107e040: ldr x22, [x20]
// 0x107e044: mov x1, xzr
// 0x107e048: bl #0x1b94c14
// 0x107e04c: ldr x8, [x25]
// 0x107e050: mov x23, x0
// 0x107e054: ldr w9, [x8, #0xe0]
// 0x107e058: cbnz w9, #0x107e064
// 0x107e05c: mov x0, x8
// 0x107e060: bl #0xf7da5c
// 0x107e064: mov x0, x22
// 0x107e068: mov x1, x23
// 0x107e06c: mov x2, xzr
// 0x107e070: bl #0x1b9568c
// 0x107e074: tbz w0, #0, #0x107e0ac
// 0x107e078: ldr x8, [x19, #0x48]
// 0x107e07c: cbz x8, #0x107eab0
// 0x107e080: ldr x0, [x8, #0x238]
// 0x107e084: cbz x0, #0x107eab0
// 0x107e088: mov x1, xzr
// 0x107e08c: bl #0x1bcfdf0
// 0x107e090: ldr x1, [x19, #0x30]
// 0x107e094: fmov s1, #0.25000000
// 0x107e098: fmul s0, s0, s1
// 0x107e09c: mov x0, x20
// 0x107e0a0: str s0, [x19, #0x27c]
// 0x107e0a4: str x1, [x19, #0x238]
// 0x107e0a8: bl #0xf7d8d0
// 0x107e0ac: ldr x0, [x25]
// 0x107e0b0: ldr x22, [x19, #0x238]
// 0x107e0b4: ldr x23, [x19, #0x30]
// 0x107e0b8: ldr w8, [x0, #0xe0]
// 0x107e0bc: cbnz w8, #0x107e0c4
// 0x107e0c0: bl #0xf7da5c
// 0x107e0c4: mov x0, x22
// 0x107e0c8: mov x1, x23
// 0x107e0cc: mov x2, xzr
// 0x107e0d0: bl #0x1b9568c
// 0x107e0d4: tbnz w0, #0, #0x107e120
// 0x107e0d8: ldr x8, [x19, #0x48]
// 0x107e0dc: cbz x8, #0x107eab0
// 0x107e0e0: ldr x0, [x8, #0x160]
// 0x107e0e4: cbz x0, #0x107eab0
// 0x107e0e8: ldr x22, [x19, #0x238]
// 0x107e0ec: mov x1, xzr
// 0x107e0f0: bl #0x1b94c14
// 0x107e0f4: ldr x8, [x25]
// 0x107e0f8: mov x23, x0
// 0x107e0fc: ldr w9, [x8, #0xe0]
// 0x107e100: cbnz w9, #0x107e10c
// 0x107e104: mov x0, x8
// 0x107e108: bl #0xf7da5c
// 0x107e10c: mov x0, x22
// 0x107e110: mov x1, x23
// 0x107e114: mov x2, xzr
// 0x107e118: bl #0x1b9568c
// 0x107e11c: tbz w0, #0, #0x107e580
// 0x107e120: ldr x0, [x19, #0x100]
// 0x107e124: cbz x0, #0x107eab0
// 0x107e128: mov x1, xzr
// 0x107e12c: bl #0x1b9d508
// 0x107e130: ldr x0, [x19, #0x238]
// 0x107e134: stp s1, s0, [sp, #8]
// 0x107e138: cbz x0, #0x107eab0
// 0x107e13c: ldr s14, [x19, #0x108]
// 0x107e140: ldr s15, [x19, #0x10c]
// 0x107e144: ldr s8, [x19, #0x110]
// 0x107e148: ldr s9, [x19, #0x22c]
// 0x107e14c: mov x1, xzr
// 0x107e150: mov v10.16b, v2.16b
// 0x107e154: bl #0x1b9d508
// 0x107e158: ldr x0, [x20]
// 0x107e15c: cbz x0, #0x107eab0
// 0x107e160: ldr s3, [sp, #0xc]
// 0x107e164: mov v11.16b, v0.16b
// 0x107e168: fmul s0, s14, s9
// 0x107e16c: mov v12.16b, v1.16b
// 0x107e170: fadd s14, s3, s0
// 0x107e174: ldr s0, [sp, #8]
// 0x107e178: mov v13.16b, v2.16b
// 0x107e17c: fmul s1, s15, s9
// 0x107e180: fmul s2, s8, s9
// 0x107e184: mov x1, xzr
// 0x107e188: fadd s15, s0, s1
// 0x107e18c: fadd s10, s10, s2
// 0x107e190: bl #0x1b9d940
// 0x107e194: ldr s3, [x19, #0x27c]
// 0x107e198: fmul s0, s0, s3
// 0x107e19c: fmul s1, s1, s3
// 0x107e1a0: fmul s2, s2, s3
// 0x107e1a4: fadd s11, s11, s0
// 0x107e1a8: fadd s12, s12, s1
// 0x107e1ac: fadd s13, s13, s2
// 0x107e1b0: str s11, [x19, #0x248]
// 0x107e1b4: str s12, [x19, #0x24c]
// 0x107e1b8: str s13, [x19, #0x250]
// 0x107e1bc: ldrb w8, [x27, #0x3e0]
// 0x107e1c0: cbnz w8, #0x107e1d8
// 0x107e1c4: adrp x0, #0x1e8c000
// 0x107e1c8: ldr x0, [x0, #0xa60]
// 0x107e1cc: bl #0xf7d92c
// 0x107e1d0: mov w8, #1
// 0x107e1d4: strb w8, [x27, #0x3e0]
// 0x107e1d8: ldr x0, [x26]
// 0x107e1dc: fsub s11, s14, s11
// 0x107e1e0: fsub s9, s15, s12
// 0x107e1e4: fsub s8, s10, s13
// 0x107e1e8: ldr w8, [x0, #0xe0]
// 0x107e1ec: cbnz w8, #0x107e1f4
// 0x107e1f0: bl #0xf7da5c
// 0x107e1f4: fmul s0, s11, s11
// 0x107e1f8: fmul s1, s9, s9
// 0x107e1fc: fmul s2, s8, s8
// 0x107e200: fadd s0, s0, s1
// 0x107e204: fadd s0, s2, s0
// 0x107e208: fsqrt s0, s0
// 0x107e20c: str s0, [x19, #0x260]
// 0x107e210: adrp x29, #0x1fab000
// 0x107e214: ldr s11, [x19, #0x248]
// 0x107e218: ldr s12, [x19, #0x24c]
// 0x107e21c: ldrb w8, [x29, #0x2c8]
// 0x107e220: ldr s13, [x19, #0x250]
// 0x107e224: cbnz w8, #0x107e23c
// 0x107e228: adrp x0, #0x1e8c000
// 0x107e22c: ldr x0, [x0, #0xa60]
// 0x107e230: bl #0xf7d92c
// 0x107e234: mov w8, #1
// 0x107e238: strb w8, [x29, #0x2c8]
// 0x107e23c: ldr x0, [x26]
// 0x107e240: fsub s11, s11, s14
// 0x107e244: fsub s12, s12, s15
// 0x107e248: fsub s13, s13, s10
// 0x107e24c: ldr w8, [x0, #0xe0]
// 0x107e250: str s15, [sp, #8]
// 0x107e254: cbnz w8, #0x107e25c
// 0x107e258: bl #0xf7da5c
// 0x107e25c: adrp x8, #0x832000
// 0x107e260: fmul s0, s11, s11
// 0x107e264: fmul s1, s12, s12
// 0x107e268: ldr s15, [x8, #0x41c]
// 0x107e26c: adrp x28, #0x1e8c000
// 0x107e270: fmul s2, s13, s13
// 0x107e274: fadd s0, s0, s1
// 0x107e278: ldr x28, [x28, #0x1e8]
// 0x107e27c: fadd s0, s2, s0
// 0x107e280: fsqrt s0, s0
// 0x107e284: fcmp s0, s15
// 0x107e288: adrp x27, #0x1fab000
// 0x107e28c: b.le #0x107e2cc
// 0x107e290: fdiv s11, s11, s0
// 0x107e294: fdiv s12, s12, s0
// 0x107e298: fdiv s13, s13, s0
// 0x107e29c: b #0x107e2f8
// 0x107e2a0: add x0, x19, #0x238
// 0x107e2a4: mov x1, xzr
// 0x107e2a8: str xzr, [x19, #0x238]
// 0x107e2ac: bl #0xf7d8d0
// 0x107e2b0: mov x0, x21
// 0x107e2b4: mov x1, xzr
// 0x107e2b8: str xzr, [x19, #0x88]
// 0x107e2bc: bl #0xf7d8d0
// 0x107e2c0: strb wzr, [x19, #0x240]
// 0x107e2c4: strb wzr, [x19, #0x295]
// 0x107e2c8: b #0x107e99c
// 0x107e2cc: ldrb w8, [x27, #0x2c9]
// 0x107e2d0: cbnz w8, #0x107e2e8
// 0x107e2d4: adrp x0, #0x1e8c000
// 0x107e2d8: ldr x0, [x0, #0x1e8]
// 0x107e2dc: bl #0xf7d92c
// 0x107e2e0: mov w8, #1
// 0x107e2e4: strb w8, [x27, #0x2c9]
// 0x107e2e8: ldr x8, [x28]
// 0x107e2ec: ldr x8, [x8, #0xb8]
// 0x107e2f0: ldp s11, s12, [x8]
// 0x107e2f4: ldr s13, [x8, #8]
// 0x107e2f8: str s11, [x19, #0x264]
// 0x107e2fc: str s12, [x19, #0x268]
// 0x107e300: str s13, [x19, #0x26c]
// 0x107e304: adrp x22, #0x1fab000
// 0x107e308: ldrb w8, [x22, #0x3e3]
// 0x107e30c: str s14, [sp, #0xc]
// 0x107e310: cbnz w8, #0x107e328
// 0x107e314: adrp x0, #0x1e8c000
// 0x107e318: ldr x0, [x0, #0x1e8]
// 0x107e31c: bl #0xf7d92c
// 0x107e320: mov w8, #1
// 0x107e324: strb w8, [x22, #0x3e3]
// 0x107e328: ldr x8, [x28]
// 0x107e32c: ldr x8, [x8, #0xb8]
// 0x107e330: ldp s1, s0, [x8, #0x4c]
// 0x107e334: ldr s2, [x8, #0x48]
// 0x107e338: ldrb w8, [x29, #0x2c8]
// 0x107e33c: fmul s14, s12, s0
// 0x107e340: fmul s8, s13, s1
// 0x107e344: fmul s13, s13, s2
// 0x107e348: fmul s9, s11, s0
// 0x107e34c: fmul s11, s11, s1
// 0x107e350: fmul s12, s12, s2
// 0x107e354: cbnz w8, #0x107e36c
// 0x107e358: adrp x0, #0x1e8c000
// 0x107e35c: ldr x0, [x0, #0xa60]
// 0x107e360: bl #0xf7d92c
// 0x107e364: mov w8, #1
// 0x107e368: strb w8, [x29, #0x2c8]
// 0x107e36c: ldr x0, [x26]
// 0x107e370: fsub s14, s14, s8
// 0x107e374: fsub s9, s13, s9
// 0x107e378: fsub s8, s11, s12
// 0x107e37c: ldr w8, [x0, #0xe0]
// 0x107e380: cbnz w8, #0x107e388
// 0x107e384: bl #0xf7da5c
// 0x107e388: fmul s0, s14, s14
// 0x107e38c: fmul s1, s9, s9
// 0x107e390: fadd s0, s0, s1
// 0x107e394: fmul s1, s8, s8
// 0x107e398: fadd s0, s1, s0
// 0x107e39c: fsqrt s0, s0
// 0x107e3a0: fcmp s0, s15
// 0x107e3a4: b.gt #0x107e3c4
// 0x107e3a8: ldrb w8, [x27, #0x2c9]
// 0x107e3ac: cbnz w8, #0x107e3c4
// 0x107e3b0: adrp x0, #0x1e8c000
// 0x107e3b4: ldr x0, [x0, #0x1e8]
// 0x107e3b8: bl #0xf7d92c
// 0x107e3bc: mov w8, #1
// 0x107e3c0: strb w8, [x27, #0x2c9]
// 0x107e3c4: ldr s11, [x19, #0x260]
// 0x107e3c8: ldr s0, [x19, #0x218]
// 0x107e3cc: fcmp s11, s0
// 0x107e3d0: b.le #0x107e3e0
// 0x107e3d4: mov w8, #1
// 0x107e3d8: strb w8, [x19, #0x278]
// 0x107e3dc: b #0x107e998
// 0x107e3e0: ldr w0, [x19, #0x29c]
// 0x107e3e4: ldr s12, [x19, #0x264]
// 0x107e3e8: ldr s13, [x19, #0x268]
// 0x107e3ec: ldr s14, [x19, #0x26c]
// 0x107e3f0: mov x1, xzr
// 0x107e3f4: bl #0x1b9515c
// 0x107e3f8: adrp x8, #0x1e8d000
// 0x107e3fc: ldr x8, [x8, #0x4a8]
// 0x107e400: mov w22, w0
// 0x107e404: ldr x8, [x8]
// 0x107e408: ldr w9, [x8, #0xe0]
// 0x107e40c: cbnz w9, #0x107e418
// 0x107e410: mov x0, x8
// 0x107e414: bl #0xf7da5c
// 0x107e418: ldp s1, s0, [sp, #8]
// 0x107e41c: mov v2.16b, v10.16b
// 0x107e420: mov v3.16b, v12.16b
// 0x107e424: mov v4.16b, v13.16b
// 0x107e428: mov v5.16b, v14.16b
// 0x107e42c: mov v6.16b, v11.16b
// 0x107e430: mov w0, w22
// 0x107e434: mov x1, xzr
// 0x107e438: bl #0x1bccf88
// 0x107e43c: add x22, x19, #0x270
// 0x107e440: mov x1, x0
// 0x107e444: str x0, [x19, #0x270]
// 0x107e448: mov x0, x22
// 0x107e44c: bl #0xf7d8d0
// 0x107e450: ldrb w8, [x19, #0x114]
// 0x107e454: strb wzr, [x19, #0x278]
// 0x107e458: cbnz w8, #0x107e658
// 0x107e45c: ldr s8, [x19, #0x290]
// 0x107e460: mov x0, xzr
// 0x107e464: bl #0x1b9ad30
// 0x107e468: fcmp s8, s0
// 0x107e46c: b.pl #0x107e658
// 0x107e470: ldr s8, [x19, #0xf8]
// 0x107e474: mov x0, xzr
// 0x107e478: bl #0x1b9ad30
// 0x107e47c: fmov s1, #6.00000000
// 0x107e480: fadd s1, s8, s1
// 0x107e484: fcmp s1, s0
// 0x107e488: b.pl #0x107e658
// 0x107e48c: ldr x0, [x25]
// 0x107e490: ldr x23, [x19, #0x238]
// 0x107e494: ldr x24, [x19, #0x30]
// 0x107e498: ldr w8, [x0, #0xe0]
// 0x107e49c: cbnz w8, #0x107e4a4
// 0x107e4a0: bl #0xf7da5c
// 0x107e4a4: mov x0, x23
// 0x107e4a8: mov x1, x24
// 0x107e4ac: mov x2, xzr
// 0x107e4b0: bl #0x1b9568c
// 0x107e4b4: tbnz w0, #0, #0x107e4ec
// 0x107e4b8: ldr x8, [x19, #0x48]
// 0x107e4bc: cbz x8, #0x107eab0
// 0x107e4c0: ldr x0, [x25]
// 0x107e4c4: ldr x23, [x19, #0x238]
// 0x107e4c8: ldr x24, [x8, #0x168]
// 0x107e4cc: ldr w9, [x0, #0xe0]
// 0x107e4d0: cbnz w9, #0x107e4d8
// 0x107e4d4: bl #0xf7da5c
// 0x107e4d8: mov x0, x23
// 0x107e4dc: mov x1, x24
// 0x107e4e0: mov x2, xzr
// 0x107e4e4: bl #0x1b9568c
// 0x107e4e8: tbz w0, #0, #0x107e658
// 0x107e4ec: ldrb w8, [x19, #0x294]
// 0x107e4f0: cbnz w8, #0x107e658
// 0x107e4f4: ldr x8, [x19, #0x48]
// 0x107e4f8: cbz x8, #0x107eab0
// 0x107e4fc: ldrb w8, [x8, #0x2b1]
// 0x107e500: cbnz w8, #0x107e658
// 0x107e504: ldr s11, [x19, #0x248]
// 0x107e508: ldr s13, [x19, #0x24c]
// 0x107e50c: ldrb w8, [x29, #0x2c8]
// 0x107e510: ldr s14, [x19, #0x250]
// 0x107e514: cbnz w8, #0x107e52c
// 0x107e518: adrp x0, #0x1e8c000
// 0x107e51c: ldr x0, [x0, #0xa60]
// 0x107e520: bl #0xf7d92c
// 0x107e524: mov w8, #1
// 0x107e528: strb w8, [x29, #0x2c8]
// 0x107e52c: ldr s0, [sp, #0xc]
// 0x107e530: ldr x0, [x26]
// 0x107e534: fsub s8, s14, s10
// 0x107e538: fsub s12, s11, s0
// 0x107e53c: ldr s0, [sp, #8]
// 0x107e540: ldr w8, [x0, #0xe0]
// 0x107e544: fsub s11, s13, s0
// 0x107e548: cbnz w8, #0x107e550
// 0x107e54c: bl #0xf7da5c
// 0x107e550: fmul s0, s12, s12
// 0x107e554: fmul s1, s11, s11
// 0x107e558: fadd s0, s0, s1
// 0x107e55c: fmul s1, s8, s8
// 0x107e560: fadd s0, s1, s0
// 0x107e564: fsqrt s0, s0
// 0x107e568: fcmp s0, s15
// 0x107e56c: b.le #0x107e5e4
// 0x107e570: fdiv s9, s12, s0
// 0x107e574: fdiv s10, s11, s0
// 0x107e578: fdiv s8, s8, s0
// 0x107e57c: b #0x107e610
// 0x107e580: ldr x0, [x25]
// 0x107e584: ldr x22, [x21]
// 0x107e588: ldr w8, [x0, #0xe0]
// 0x107e58c: cbnz w8, #0x107e594
// 0x107e590: bl #0xf7da5c
// 0x107e594: mov x0, x22
// 0x107e598: mov x1, xzr
// 0x107e59c: bl #0x1b98274
// 0x107e5a0: tbz w0, #0, #0x107e998
// 0x107e5a4: ldr x0, [x21]
// 0x107e5a8: cbz x0, #0x107eab0
// 0x107e5ac: mov x1, xzr
// 0x107e5b0: bl #0x1b91624
// 0x107e5b4: tbz w0, #0, #0x107e998
// 0x107e5b8: ldr x0, [x25]
// 0x107e5bc: ldr x22, [x20]
// 0x107e5c0: ldr w8, [x0, #0xe0]
// 0x107e5c4: cbnz w8, #0x107e5cc
// 0x107e5c8: bl #0xf7da5c
// 0x107e5cc: mov x0, x22
// 0x107e5d0: mov x1, xzr
// 0x107e5d4: mov x2, xzr
// 0x107e5d8: bl #0x1b94ac8
// 0x107e5dc: tbnz w0, #0, #0x107e120
// 0x107e5e0: b #0x107e998
// 0x107e5e4: ldrb w8, [x27, #0x2c9]
// 0x107e5e8: cbnz w8, #0x107e600
// 0x107e5ec: adrp x0, #0x1e8c000
// 0x107e5f0: ldr x0, [x0, #0x1e8]
// 0x107e5f4: bl #0xf7d92c
// 0x107e5f8: mov w8, #1
// 0x107e5fc: strb w8, [x27, #0x2c9]
// 0x107e600: ldr x8, [x28]
// 0x107e604: ldr x8, [x8, #0xb8]
// 0x107e608: ldp s9, s10, [x8]
// 0x107e60c: ldr s8, [x8, #8]
// 0x107e610: mov x0, x19
// 0x107e614: mov x1, xzr
// 0x107e618: bl #0x1b92154
// 0x107e61c: cbz x0, #0x107eab0
// 0x107e620: mov x1, xzr
// 0x107e624: bl #0x1b9d9b8
// 0x107e628: adrp x8, #0x832000
// 0x107e62c: ldr s3, [x8, #0x478]
// 0x107e630: fmul s0, s9, s0
// 0x107e634: fmul s1, s10, s1
// 0x107e638: fadd s0, s0, s1
// 0x107e63c: fmul s1, s8, s2
// 0x107e640: fadd s0, s1, s0
// 0x107e644: fcmp s0, s3
// 0x107e648: b.pl #0x107e658
// 0x107e64c: mov w8, #0x101
// 0x107e650: strh w8, [x19, #0x278]
// 0x107e654: b #0x107e998
// 0x107e658: ldr x8, [x19, #0x270]
// 0x107e65c: strb wzr, [x19, #0x279]
// 0x107e660: cbz x8, #0x107eab0
// 0x107e664: mov x27, xzr
// 0x107e668: mov w28, #0x20
// 0x107e66c: ldr w9, [x8, #0x18]
// 0x107e670: cmp x27, w9, sxtw
// 0x107e674: b.ge #0x107e838
// 0x107e678: cmp x27, x9
// 0x107e67c: b.hs #0x107eab4
// 0x107e680: add x0, x8, x28
// 0x107e684: mov x1, xzr
// 0x107e688: bl #0x1bced24
// 0x107e68c: cbz x0, #0x107eab0
// 0x107e690: ldr x1, [x20]
// 0x107e694: mov x2, xzr
// 0x107e698: bl #0x1b9ec90
// 0x107e69c: tbnz w0, #0, #0x107e6d4
// 0x107e6a0: ldr x8, [x22]
// 0x107e6a4: cbz x8, #0x107eab0
// 0x107e6a8: ldr w9, [x8, #0x18]
// 0x107e6ac: cmp x27, x9
// 0x107e6b0: b.hs #0x107eab4
// 0x107e6b4: add x0, x8, x28
// 0x107e6b8: mov x1, xzr
// 0x107e6bc: bl #0x1bced24
// 0x107e6c0: cbz x0, #0x107eab0
// 0x107e6c4: ldr x1, [x19, #0x100]
// 0x107e6c8: mov x2, xzr
// 0x107e6cc: bl #0x1b9ec90
// 0x107e6d0: tbz w0, #0, #0x107e894
// 0x107e6d4: ldrb w8, [x19, #0xf5]
// 0x107e6d8: cbnz w8, #0x107e7bc
// 0x107e6dc: ldr w8, [x19, #0xf0]
// 0x107e6e0: cmp w8, #1
// 0x107e6e4: b.ne #0x107e7bc
// 0x107e6e8: ldr x0, [x25]
// 0x107e6ec: ldr x23, [x19, #0x238]
// 0x107e6f0: ldr x24, [x19, #0x28]
// 0x107e6f4: ldr w8, [x0, #0xe0]
// 0x107e6f8: cbnz w8, #0x107e700
// 0x107e6fc: bl #0xf7da5c
// 0x107e700: mov x0, x23
// 0x107e704: mov x1, x24
// 0x107e708: mov x2, xzr
// 0x107e70c: bl #0x1b94ac8
// 0x107e710: tbz w0, #0, #0x107e7bc
// 0x107e714: ldr x8, [x22]
// 0x107e718: cbz x8, #0x107eab0
// 0x107e71c: ldr w9, [x8, #0x18]
// 0x107e720: cmp x27, x9
// 0x107e724: b.hs #0x107eab4
// 0x107e728: add x0, x8, x28
// 0x107e72c: mov x1, xzr
// 0x107e730: bl #0x1bcec58
// 0x107e734: ldr x8, [x19, #0x48]
// 0x107e738: cbz x8, #0x107eab0
// 0x107e73c: mov x23, x0
// 0x107e740: ldr x0, [x25]
// 0x107e744: ldr x24, [x8, #0x238]
// 0x107e748: ldr w9, [x0, #0xe0]
// 0x107e74c: cbnz w9, #0x107e754
// 0x107e750: bl #0xf7da5c
// 0x107e754: mov x0, x23
// 0x107e758: mov x1, x24
// 0x107e75c: mov x2, xzr
// 0x107e760: bl #0x1b9568c
// 0x107e764: tbnz w0, #0, #0x107e894
// 0x107e768: ldr x8, [x22]
// 0x107e76c: cbz x8, #0x107eab0
// 0x107e770: ldr w9, [x8, #0x18]
// 0x107e774: cmp x27, x9
// 0x107e778: b.hs #0x107eab4
// 0x107e77c: add x0, x8, x28
// 0x107e780: mov x1, xzr
// 0x107e784: bl #0x1bcec58
// 0x107e788: ldr x8, [x19, #0x48]
// 0x107e78c: cbz x8, #0x107eab0
// 0x107e790: mov x23, x0
// 0x107e794: ldr x0, [x25]
// 0x107e798: ldr x24, [x8, #0x168]
// 0x107e79c: ldr w9, [x0, #0xe0]
// 0x107e7a0: cbnz w9, #0x107e7a8
// 0x107e7a4: bl #0xf7da5c
// 0x107e7a8: mov x0, x23
// 0x107e7ac: mov x1, x24
// 0x107e7b0: mov x2, xzr
// 0x107e7b4: bl #0x1b9568c
// 0x107e7b8: tbnz w0, #0, #0x107e894
// 0x107e7bc: ldr x8, [x22]
// 0x107e7c0: cbz x8, #0x107eab0
// 0x107e7c4: ldr w9, [x8, #0x18]
// 0x107e7c8: cmp x27, x9
// 0x107e7cc: b.hs #0x107eab4
// 0x107e7d0: add x0, x8, x28
// 0x107e7d4: mov x1, xzr
// 0x107e7d8: bl #0x1bced24
// 0x107e7dc: cbz x0, #0x107eab0
// 0x107e7e0: ldr x1, [x20]
// 0x107e7e4: mov x2, xzr
// 0x107e7e8: bl #0x1b9ec90
// 0x107e7ec: tbnz w0, #0, #0x107e804
// 0x107e7f0: ldr x8, [x22]
// 0x107e7f4: add x27, x27, #1
// 0x107e7f8: add x28, x28, #0x2c
// 0x107e7fc: cbnz x8, #0x107e66c
// 0x107e800: b #0x107eab0
// 0x107e804: ldr x8, [x22]
// 0x107e808: cbz x8, #0x107eab0
// 0x107e80c: ldr w9, [x8, #0x18]
// 0x107e810: cmp w27, w9
// 0x107e814: b.hs #0x107eab4
// 0x107e818: add x8, x8, x28
// 0x107e81c: ldr x9, [x8, #0x20]
// 0x107e820: ldr w10, [x8, #0x28]
// 0x107e824: ldp q0, q1, [x8]
// 0x107e828: add x8, x19, #0x2a0
// 0x107e82c: str x9, [x19, #0x2c0]
// 0x107e830: str w10, [x8, #0x28]
// 0x107e834: stp q0, q1, [x19, #0x2a0]
// 0x107e838: ldrb w8, [x19, #0x278]
// 0x107e83c: cbnz w8, #0x107e89c
// 0x107e840: ldr x8, [x19, #0x48]
// 0x107e844: cbz x8, #0x107eab0
// 0x107e848: ldr x0, [x8, #0x160]
// 0x107e84c: cbz x0, #0x107eab0
// 0x107e850: ldr x20, [x19, #0x238]
// 0x107e854: mov x1, xzr
// 0x107e858: bl #0x1b94c14
// 0x107e85c: ldr x8, [x25]
// 0x107e860: mov x21, x0
// 0x107e864: ldr w9, [x8, #0xe0]
// 0x107e868: cbnz w9, #0x107e874
// 0x107e86c: mov x0, x8
// 0x107e870: bl #0xf7da5c
// 0x107e874: mov x0, x20
// 0x107e878: mov x1, x21
// 0x107e87c: mov x2, xzr
// 0x107e880: bl #0x1b94ac8
// 0x107e884: tbz w0, #0, #0x107e9cc
// 0x107e888: strb wzr, [x19, #0x280]
// 0x107e88c: mov w8, #1
// 0x107e890: b #0x107e9d4
// 0x107e894: mov w8, #1
// 0x107e898: strb w8, [x19, #0x278]
// 0x107e89c: ldr x0, [x25]
// 0x107e8a0: ldr x22, [x21]
// 0x107e8a4: ldr w8, [x0, #0xe0]
// 0x107e8a8: cbnz w8, #0x107e8b0
// 0x107e8ac: bl #0xf7da5c
// 0x107e8b0: mov x0, x22
// 0x107e8b4: mov x1, xzr
// 0x107e8b8: bl #0x1b98274
// 0x107e8bc: adrp x22, #0x1fab000
// 0x107e8c0: tbz w0, #0, #0x107e998
// 0x107e8c4: ldrb w8, [x19, #0x114]
// 0x107e8c8: cbnz w8, #0x107e998
// 0x107e8cc: ldr x8, [x21]
// 0x107e8d0: cbz x8, #0x107eab0
// 0x107e8d4: ldr s8, [x8, #0x258]
// 0x107e8d8: mov x0, xzr
// 0x107e8dc: bl #0x1b9ad30
// 0x107e8e0: fcmp s8, s0
// 0x107e8e4: b.le #0x107e998
// 0x107e8e8: ldr x0, [x19, #0x100]
// 0x107e8ec: cbz x0, #0x107eab0
// 0x107e8f0: mov x1, xzr
// 0x107e8f4: bl #0x1b9d508
// 0x107e8f8: ldr x0, [x20]
// 0x107e8fc: cbz x0, #0x107eab0
// 0x107e900: mov x1, xzr
// 0x107e904: mov v8.16b, v0.16b
// 0x107e908: mov v9.16b, v1.16b
// 0x107e90c: mov v10.16b, v2.16b
// 0x107e910: bl #0x1b9d508
// 0x107e914: ldrb w8, [x22, #0x3e0]
// 0x107e918: mov v11.16b, v0.16b
// 0x107e91c: mov v12.16b, v1.16b
// 0x107e920: mov v13.16b, v2.16b
// 0x107e924: cbnz w8, #0x107e93c
// 0x107e928: adrp x0, #0x1e8c000
// 0x107e92c: ldr x0, [x0, #0xa60]
// 0x107e930: bl #0xf7d92c
// 0x107e934: mov w8, #1
// 0x107e938: strb w8, [x22, #0x3e0]
// 0x107e93c: ldr x0, [x26]
// 0x107e940: fsub s11, s8, s11
// 0x107e944: fsub s9, s9, s12
// 0x107e948: fsub s8, s10, s13
// 0x107e94c: ldr w8, [x0, #0xe0]
// 0x107e950: cbnz w8, #0x107e958
// 0x107e954: bl #0xf7da5c
// 0x107e958: fmul s0, s11, s11
// 0x107e95c: fmul s1, s9, s9
// 0x107e960: ldr s2, [x19, #0x20c]
// 0x107e964: fadd s0, s0, s1
// 0x107e968: fmul s1, s8, s8
// 0x107e96c: fadd s0, s1, s0
// 0x107e970: fsqrt s0, s0
// 0x107e974: fcmp s0, s2
// 0x107e978: b.pl #0x107e998
// 0x107e97c: mov x0, xzr
// 0x107e980: bl #0x1b9ad30
// 0x107e984: fmov s1, #6.00000000
// 0x107e988: mov w8, #1
// 0x107e98c: fadd s0, s0, s1
// 0x107e990: str s0, [x19, #0x290]
// 0x107e994: strb w8, [x19, #0x295]
// 0x107e998: strb wzr, [x19, #0x240]
// 0x107e99c: ldp x20, x19, [sp, #0xa0]
// 0x107e9a0: ldp x22, x21, [sp, #0x90]
// 0x107e9a4: ldp x24, x23, [sp, #0x80]
// 0x107e9a8: ldp x26, x25, [sp, #0x70]
// 0x107e9ac: ldp x28, x27, [sp, #0x60]
// 0x107e9b0: ldp x29, x30, [sp, #0x50]
// 0x107e9b4: ldp d9, d8, [sp, #0x40]
// 0x107e9b8: ldp d11, d10, [sp, #0x30]
// 0x107e9bc: ldp d13, d12, [sp, #0x20]
// 0x107e9c0: ldp d15, d14, [sp, #0x10]
// 0x107e9c4: add sp, sp, #0xb0
// 0x107e9c8: ret
// 0x107e9cc: mov w8, #1
// 0x107e9d0: strb w8, [x19, #0x280]
// 0x107e9d4: strb w8, [x19, #0x240]
// 0x107e9d8: b #0x107e99c
// 0x107e9dc: ldr x8, [x19, #0x48]
// 0x107e9e0: cbz x8, #0x107eab0
// 0x107e9e4: ldr x0, [x8, #0x160]
// 0x107e9e8: cbz x0, #0x107eab0
// 0x107e9ec: ldr x21, [x19, #0x238]
// 0x107e9f0: mov x1, xzr
// 0x107e9f4: bl #0x1b94c14
// 0x107e9f8: ldr x8, [x25]
// 0x107e9fc: mov x22, x0
// 0x107ea00: ldr w9, [x8, #0xe0]
// 0x107ea04: cbnz w9, #0x107ea10
// 0x107ea08: mov x0, x8
// 0x107ea0c: bl #0xf7da5c
// 0x107ea10: mov x0, x21
// 0x107ea14: mov x1, x22
// 0x107ea18: mov x2, xzr
// 0x107ea1c: bl #0x1b9568c
// 0x107ea20: tbz w0, #0, #0x107ea5c
// 0x107ea24: ldr x8, [x19, #0x48]
// 0x107ea28: str wzr, [x19, #0x27c]
// 0x107ea2c: cbz x8, #0x107eab0
// 0x107ea30: ldr x0, [x8, #0x160]
// 0x107ea34: cbz x0, #0x107eab0
// 0x107ea38: mov x1, xzr
// 0x107ea3c: bl #0x1b94c14
// 0x107ea40: mov x1, x0
// 0x107ea44: str x0, [x19, #0x238]
// 0x107ea48: mov x0, x20
// 0x107ea4c: bl #0xf7d8d0
// 0x107ea50: mov w8, #1
// 0x107ea54: strb w8, [x19, #0x280]
// 0x107ea58: b #0x107ea90
// 0x107ea5c: ldr x8, [x19, #0x48]
// 0x107ea60: cbz x8, #0x107eab0
// 0x107ea64: ldr x0, [x8, #0x238]
// 0x107ea68: cbz x0, #0x107eab0
// 0x107ea6c: mov x1, xzr
// 0x107ea70: bl #0x1bcfdf0
// 0x107ea74: ldr x1, [x19, #0x30]
// 0x107ea78: fmov s1, #0.25000000
// 0x107ea7c: fmul s0, s0, s1
// 0x107ea80: mov x0, x20
// 0x107ea84: str s0, [x19, #0x27c]
// 0x107ea88: str x1, [x19, #0x238]
// 0x107ea8c: bl #0xf7d8d0
// 0x107ea90: mov x0, xzr
// 0x107ea94: bl #0x1b9ad30
// 0x107ea98: fmov s1, #6.00000000
// 0x107ea9c: mov w8, #1
// 0x107eaa0: fadd s0, s0, s1
// 0x107eaa4: str s0, [x19, #0x290]
// 0x107eaa8: strb w8, [x19, #0x294]
// 0x107eaac: b #0x107e99c
// 0x107eab0: bl #0xf7db74
// 0x107eab4: bl #0xf7db7c
```


## `AI.Shoot` — RVA `0xc7eab8`

- Decompiled symbol: `AI_Shoot`
- Metadata signature: `private IEnumerator Shoot() { }`
- Native interval: `108` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[12];
    long long field_20;
} struct_0;

extern long long g_1ef2b48;
extern char g_1fab3f6;

struct_0 * AI_Shoot(long long a0)
{
    struct_0 *v0;  // x20
    struct_0 *ptr;  // x0

    if (!(g_1fab3f6 & 1))
    {
        sub_f7d92c(&g_1ef2b48);
        g_1fab3f6 = 1;
    }
    v0 = sub_f7db70(g_1ef2b48);
    Object__ctor(v0, 0);
    ptr = v0;
    ptr->field_10 = 0;
    ptr->field_20 = a0;
    sub_f7d8d0(&ptr->field_20, a0);
    return ptr;
}
```


## `AI.<Shoot>d__133.ctor` — RVA `0xc7eb24`

- Decompiled symbol: `AI_Shoot_d__133_ctor`
- Metadata signature: `public void .ctor(int <>1__state) { }`
- Native interval: `40` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

void AI_Shoot_d__133_ctor(struct_0 *ptr, unsigned int a1)
{
    Object__ctor();
    ptr->field_10 = a1;
    return;
}
```


## `AI.AttackTarget` — RVA `0xc7eb4c`

- Decompiled symbol: `AI_AttackTarget`
- Metadata signature: `private IEnumerator AttackTarget() { }`
- Native interval: `108` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[12];
    long long field_20;
} struct_0;

extern long long g_1ef2b28;
extern char g_1fab3f7;

struct_0 * AI_AttackTarget(long long a0)
{
    struct_0 *v0;  // x20
    struct_0 *ptr;  // x0

    if (!(g_1fab3f7 & 1))
    {
        sub_f7d92c(&g_1ef2b28);
        g_1fab3f7 = 1;
    }
    v0 = sub_f7db70(g_1ef2b28);
    Object__ctor(v0, 0);
    ptr = v0;
    ptr->field_10 = 0;
    ptr->field_20 = a0;
    sub_f7d8d0(&ptr->field_20, a0);
    return ptr;
}
```


## `AI.<AttackTarget>d__134.ctor` — RVA `0xc7ebb8`

- Decompiled symbol: `AI_AttackTarget_d__134_ctor`
- Metadata signature: `public void .ctor(int <>1__state) { }`
- Native interval: `40` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

void AI_AttackTarget_d__134_ctor(struct_0 *ptr, unsigned int a1)
{
    Object__ctor();
    ptr->field_10 = a1;
    return;
}
```


## `AI.SearchTarget` — RVA `0xc7ebe0`

- Decompiled symbol: `AI_SearchTarget`
- Metadata signature: `private void SearchTarget(Vector3 position) { }`
- Native interval: `316` bytes
- Result: `pseudocode`
- Heuristic layout hint: `AI_Recovered` matched 10 offsets against `AI` metadata (confidence 1.00).

```c
typedef struct AI_Recovered {
    char padding_0[48];
    long long playerTransform;
    char padding_38[16];
    struct struct_1 *FPSWalker;
    char padding_50[56];
    long long TargetAIComponent;
    char padding_90[60];
    unsigned int runSpeed;
    char padding_d0[12];
    unsigned int speedAmt;
    char padding_e0[52];
    char huntPlayer;
    char padding_115[291];
    long long target;
    char padding_240[28];
    char attackFinished;
    char padding_25d[51];
    unsigned int timeout;
    char padding_294[2];
    char damaged;
} AI_Recovered;

typedef struct struct_3 {
    char padding_0[352];
    unsigned long long field_160;
} struct_3;

typedef struct struct_1 {
    char padding_0[352];
    long long field_160;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab3f8;

struct_2 * AI_SearchTarget(struct_2 *ptr)
{
    struct_2 *v0;  // x0
    struct_2 *v1;  // x0
    struct_2 *v3;  // x0
    long long v4;  // x0
    unsigned long v5;  // x0
    unsigned long long v6;  // x0

    v0 = ptr;
    if (!(g_1fab3f8 & 1))
    {
        v1 = sub_f7d92c(&g_1ef0c58);
        g_1fab3f8 = 1;
        v0 = v1;
    }
    if (!ptr->field_25c)
        return v0;
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v3 = Object__op_Equality(ptr->field_238, ptr->field_30, 0);
    if (!((char)v3 & 1))
    {
        if (!ptr->field_48)
        {
            sub_f7db74();
        }
        else if (ptr->field_48->field_160)
        {
            v4 = GameObject__get_transform(ptr->field_48->field_160, 0);
            if (!g_1ef0c58->field_e0)
                sub_f7da5c(g_1ef0c58);
            v3 = Object__op_Equality(ptr->field_238, v4, 0);
            if (!((char)v3 & 1))
            {
                if (!g_1ef0c58->field_e0)
                    sub_f7da5c(g_1ef0c58);
                v3 = Object__op_Implicit(ptr->field_88, 0);
                if (!((char)v3 & 1))
                {
                    ptr->field_290 = 0;
                    ptr->field_296 = 0;
                    return v3;
                }
                else if (ptr->field_88)
                {
                    v3 = Behaviour__get_enabled(ptr->field_88, 0);
                    if (!((char)v3 & 1))
                    {
                        ptr->field_290 = 0;
                        ptr->field_296 = 0;
                        return v3;
                    }
                }
                else
                {
                    sub_f7db74();
                }
            }
        }
        else
        {
            sub_f7db74();
        }
    }
    if (ptr->field_114)
        return v3;
    v5 = ptr->field_238;
    ptr->field_dc = ptr->field_cc;
    if (v5)
    {
        Transform__get_position(v5, 0);
        v6 = AI__TravelToPoint(ptr);
        return AI__TravelToPoint(ptr);
    }
    sub_f7db74();
}
```


## `AI.TravelToPoint` — RVA `0xc7ed1c`

- Decompiled symbol: `AI_TravelToPoint`
- Metadata signature: `private void TravelToPoint(Vector3 position) { }`
- Native interval: `100` bytes
- Result: `pseudocode`
- Heuristic layout hint: `AI_Recovered` matched 2 offsets against `AI` metadata (confidence 1.00).

```c
typedef struct AI_Recovered {
    char padding_0[144];
    unsigned long long agent;
    char padding_98[452];
    char attackFinished;
} AI_Recovered;

struct_0 * AI_TravelToPoint(struct_0 *ptr, unsigned long a1)
{
    unsigned long v0;  // x0
    unsigned long long v1;  // x0

    if (!ptr->field_25c)
        return ptr;
    v0 = ptr->field_90;
    if (v0)
    {
        NavMeshAgent__SetDestination(v0, 0);
        v0 = ptr->field_90;
        if (v0)
        {
            NavMeshAgent__set_isStopped(v0, 0, 0);
            v0 = ptr->field_90;
            if (v0)
            {
                NavMeshAgent__set_speed(v0, 0);
                v1 = AI__SetSpeed(ptr);
                return AI__SetSpeed(ptr);
            }
        }
    }
    sub_f7db74(v0);
}
```


## `AI.RotateTowards` — RVA `0xc7ed80`

- Decompiled symbol: `AI_RotateTowards`
- Metadata signature: `public IEnumerator RotateTowards(Vector3 position, float rotationSpeed, float turnTimer, bool attacking = true) { }`
- Native interval: `184` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[12];
    long long field_20;
    unsigned int field_28;
    unsigned int field_2c;
    unsigned int field_30;
    char field_34;
    char padding_35[3];
    unsigned int field_38;
    unsigned int field_3c;
} struct_0;

extern long long g_1ef2b40;
extern char g_1fab3f9;

struct_0 * AI_RotateTowards(long long a0, char a1)
{
    struct_0 *v0;  // x20
    struct_0 *ptr;  // x0
    unsigned int v2;  // s0
    unsigned int v3;  // s1
    unsigned int v4;  // s2
    unsigned int v5;  // s3
    unsigned int v6;  // s4

    if (!(g_1fab3f9 & 1))
    {
        sub_f7d92c(&g_1ef2b40);
        g_1fab3f9 = 1;
    }
    v0 = sub_f7db70(g_1ef2b40);
    Object__ctor(v0, 0);
    ptr = v0;
    ptr->field_10 = 0;
    ptr->field_20 = a0;
    sub_f7d8d0(&ptr->field_20, a0);
    ptr->field_28 = v2;
    ptr->field_2c = v3;
    ptr->field_30 = v4;
    ptr->field_38 = v5;
    ptr->field_3c = v6;
    ptr->field_34 = a1 & 1;
    return ptr;
}
```


## `AI.<RotateTowards>d__136.ctor` — RVA `0xc7ee38`

- Decompiled symbol: `AI_RotateTowards_d__136_ctor`
- Metadata signature: `public void .ctor(int <>1__state) { }`
- Native interval: `40` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

void AI_RotateTowards_d__136_ctor(struct_0 *ptr, unsigned int a1)
{
    Object__ctor();
    ptr->field_10 = a1;
    return;
}
```


## `AI.UpdateModelYaw` — RVA `0xc7ee60`

- Decompiled symbol: `AI_UpdateModelYaw`
- Metadata signature: `private IEnumerator UpdateModelYaw() { }`
- Native interval: `108` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[12];
    long long field_20;
} struct_0;

extern long long g_1ef2b60;
extern char g_1fab3fa;

struct_0 * AI_UpdateModelYaw(long long a0)
{
    struct_0 *v0;  // x20
    struct_0 *ptr;  // x0

    if (!(g_1fab3fa & 1))
    {
        sub_f7d92c(&g_1ef2b60);
        g_1fab3fa = 1;
    }
    v0 = sub_f7db70(g_1ef2b60);
    Object__ctor(v0, 0);
    ptr = v0;
    ptr->field_10 = 0;
    ptr->field_20 = a0;
    sub_f7d8d0(&ptr->field_20, a0);
    return ptr;
}
```


## `AI.<UpdateModelYaw>d__137.ctor` — RVA `0xc7eecc`

- Decompiled symbol: `AI_UpdateModelYaw_d__137_ctor`
- Metadata signature: `public void .ctor(int <>1__state) { }`
- Native interval: `40` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

void AI_UpdateModelYaw_d__137_ctor(struct_0 *ptr, unsigned int a1)
{
    Object__ctor();
    ptr->field_10 = a1;
    return;
}
```


## `AI.SetSpeed` — RVA `0xc7eef4`

- Decompiled symbol: `AI_SetSpeed`
- Metadata signature: `private void SetSpeed(float speed) { }`
- Native interval: `280` bytes
- Result: `pseudocode`
- Heuristic layout hint: `AI_Recovered` matched 8 offsets against `AI` metadata (confidence 1.00).

```c
typedef struct AI_Recovered {
    char padding_0[144];
    unsigned long long agent;
    char padding_98[24];
    unsigned long long AnimatorComponent;
    char padding_b8[24];
    unsigned int walkSpeed;
    char padding_d4[288];
    unsigned int walkStepTime;
    unsigned int runStepTime;
    unsigned int stepInterval;
    char padding_200[88];
    unsigned int attackTime;
    char attackFinished;
} AI_Recovered;

extern long long g_1f08598;
extern char g_1fab3fc;

struct_0 * AI_SetSpeed(struct_0 *ptr, unsigned long a1, unsigned long a2)
{
    struct_0 *v0;  // x0
    struct_0 *v1;  // x0
    unsigned long v10;  // 4125
    struct_0 *v2;  // x0
    unsigned int v3;  // s0
    unsigned int v4;  // s0
    unsigned long v5;  // 4129
    unsigned long v6;  // x0
    unsigned long v8;  // 4125
    unsigned int v9;  // s9

    v0 = ptr;
    if (!(g_1fab3fc & 1))
    {
        v1 = sub_f7d92c(&g_1f08598);
        g_1fab3fc = 1;
        v0 = v1;
    }
    v3 = ptr->field_d0;
    v5 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v3, v4)) >> 5 & 3 | (unsigned long long)(CmpF(v3, v4) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v3, v4)) >> 5 & 3 | (unsigned long long)(CmpF(v3, v4) & 1)) & ((unsigned long long)(char)(CmpF(v3, v4)) >> 5 & 3 | (unsigned long long)(CmpF(v3, v4) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if (!((char)v5))
    {
        v6 = ptr->field_90;
        if (v6)
        {
            v2 = NavMeshAgent__get_hasPath(v6, 0);
            if (!(v2 & 1))
                goto LABEL_107ef70;
            v6 = ptr->field_b0;
            if (v6)
            {
                v2 = Animator__SetInteger(v6, g_1f08598, 2, 0);
                ptr->field_1fc = ptr->field_1f8;
                return v2;
            }
        }
    }
    else
    {
LABEL_107ef70:
        v8 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v4, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v4, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v4, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v4, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v4, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v4, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if (!((char)v8))
        {
            v6 = ptr->field_90;
            if (v6)
            {
                v2 = NavMeshAgent__get_hasPath(v6, 0);
                if (!(v2 & 1))
                    goto LABEL_107efb4;
                v6 = ptr->field_b0;
                if (v6)
                {
                    v2 = Animator__SetInteger(v6, g_1f08598, 1, 0);
                    ptr->field_1fc = ptr->field_1f4;
                    return v2;
                }
            }
        }
        else
        {
LABEL_107efb4:
            if (!ptr->field_25c)
            {
                ptr->field_1fc = 0xbf800000;
                return v2;
            }
            v9 = ptr->field_258;
            v2 = Time__get_time(0);
            v10 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v9, v3)) >> 5 & 3 | (unsigned long long)(CmpF(v9, v3) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v9, v3)) >> 5 & 3 | (unsigned long long)(CmpF(v9, v3) & 1)) & ((unsigned long long)(char)(CmpF(v9, v3)) >> 5 & 3 | (unsigned long long)(CmpF(v9, v3) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
            if ((char)v10)
            {
                ptr->field_1fc = 0xbf800000;
                return v2;
            }
            v6 = ptr->field_b0;
            if (v6)
            {
                v2 = Animator__SetInteger(v6, g_1f08598, 0, 0);
                ptr->field_1fc = 0xbf800000;
                return v2;
            }
        }
    }
    sub_f7db74(v6);
}
```


## `AI.PickNextWaypoint` — RVA `0xc7f00c`

- Decompiled symbol: `AI_PickNextWaypoint`
- Metadata signature: `private Transform PickNextWaypoint(Transform currentWaypoint, int curWaypointNumber) { }`
- Native interval: `232` bytes
- Result: `pseudocode`
- Heuristic layout hint: `AI_Recovered` matched 2 offsets against `AI` metadata (confidence 1.00).

```c
typedef struct AI_Recovered {
    char padding_0[288];
    struct struct_1 *waypointGroup;
    char padding_128[20];
    char countBackwards;
} AI_Recovered;

typedef struct struct_1 {
    char padding_0[40];
    struct struct_0 *field_28;
} struct_1;

typedef struct struct_0 {
    char padding_0[24];
    unsigned int field_18;
} struct_0;

extern long long g_1ef8a98;
extern long long g_1ef8aa0;
extern char g_1fab3fb;

void AI_PickNextWaypoint(struct_2 *ptr, unsigned long a1, unsigned int a2)
{
    if (!(g_1fab3fb & 1))
    {
        sub_f7d92c(&g_1ef8a98);
        sub_f7d92c(&g_1ef8aa0);
        g_1fab3fb = 1;
    }
    if (ptr->field_13c)
    {
        if (ptr->field_120 && ptr->field_120->field_28)
        {
            if (a2)
            {
                sub_14a30c0();
                return;
            }
            sub_14a30c0();
            ptr->field_13c = 0;
            return;
        }
    }
    else
    {
        if (ptr->field_120 && ptr->field_120->field_28)
        {
            if (ptr->field_120->field_28->field_18 - 1 > a2)
            {
                sub_14a30c0();
                return;
            }
            sub_14a30c0();
            ptr->field_13c = 1;
            return;
        }
    }
    sub_f7db74();
}
```


## `AI.PlayFootSteps` — RVA `0xc7f0f4`

- Decompiled symbol: `AI_PlayFootSteps`
- Metadata signature: `private IEnumerator PlayFootSteps() { }`
- Native interval: `108` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[12];
    long long field_20;
} struct_0;

extern long long g_1ef2b38;
extern char g_1fab3fd;

struct_0 * AI_PlayFootSteps(long long a0)
{
    struct_0 *v0;  // x20
    struct_0 *ptr;  // x0

    if (!(g_1fab3fd & 1))
    {
        sub_f7d92c(&g_1ef2b38);
        g_1fab3fd = 1;
    }
    v0 = sub_f7db70(g_1ef2b38);
    Object__ctor(v0, 0);
    ptr = v0;
    ptr->field_10 = 0;
    ptr->field_20 = a0;
    sub_f7d8d0(&ptr->field_20, a0);
    return ptr;
}
```


## `AI.<PlayFootSteps>d__141.ctor` — RVA `0xc7f160`

- Decompiled symbol: `AI_PlayFootSteps_d__141_ctor`
- Metadata signature: `public void .ctor(int <>1__state) { }`
- Native interval: `40` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

void AI_PlayFootSteps_d__141_ctor(struct_0 *ptr, unsigned int a1)
{
    Object__ctor();
    ptr->field_10 = a1;
    return;
}
```


## `AI.CommandNPC` — RVA `0xc7f188`

- Decompiled symbol: `AI_CommandNPC`
- Metadata signature: `public void CommandNPC() { }`
- Native interval: `1336` bytes
- Result: `pseudocode`
- Heuristic layout hint: `AI_Recovered` matched 22 offsets against `AI` metadata (confidence 0.92).

```c
typedef struct AI_Recovered {
    char padding_0[48];
    long long playerTransform;
    char padding_38[184];
    unsigned int factionNum;
    char padding_f4[12];
    long long myTransform;
    char padding_108[37];
    char followPlayer;
    char followOnUse;
    char padding_12f[1];
    char orderedMove;
    char padding_131[3];
    unsigned int commandedTime;
    unsigned int talkedTime;
    char padding_13c[8];
    unsigned int startPosition;
    unsigned int field_148;
    unsigned int field_14c;
    char padding_150[8];
    long long stayFx1;
    long long stayFx2;
    long long followFx1;
    long long followFx2;
    char padding_178[16];
    long long jokeFx;
    long long jokeFx2;
    int jokeActivate;
    unsigned int jokePlaying;
    int jokeCount;
    char padding_1a4[52];
    long long vocalFx;
    char padding_1e0[124];
    char attackFinished;
    char turning;
    char cancelRotate;
} AI_Recovered;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern long long g_1f0d6b8;
extern char g_1fab3fe;

unsigned long long AI_CommandNPC(struct_1 *ptr)
{
    unsigned int v0;  // s1
    unsigned int v1;  // s0
    unsigned int v11;  // s2
    unsigned int v12;  // s1
    unsigned long v13;  // 4138
    unsigned long v14;  // 4129
    unsigned long v15;  // x20
    unsigned long long v17;  // x0
    unsigned int v18;  // s8
    unsigned long long v19;  // x0
    unsigned long v2;  // 4138
    unsigned long v20;  // 4138
    unsigned long long v21;  // x0
    int v22;  // w8
    int v23;  // w9
    int v24;  // w8
    unsigned long v25;  // 4129
    unsigned long v26;  // x20
    unsigned int v3;  // w8
    long long v4;  // x0
    unsigned long v6;  // 4138
    unsigned long v7;  // 4129
    unsigned int v8;  // s0
    unsigned long v9;  // x20

    if (!(g_1fab3fe & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c(&g_1f0d6b8);
        g_1fab3fe = 1;
    }
    if (ptr->field_f0 == 1 && ptr->field_12e && (Time__get_time(0), v0 = ptr->field_134 + 0x3f000000, v2 = (unsigned long)arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v0, v1)) >> 5 & 3 | (unsigned long long)(CmpF(v0, v1) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v0, v1)) >> 5 & 3 | (unsigned long long)(CmpF(v0, v1) & 1)) & ((unsigned long long)(char)(CmpF(v0, v1)) >> 5 & 3 | (unsigned long long)(CmpF(v0, v1) & 1)) >> 1 & 1)) * 0x10000000, 0, 0), !((char)v2)))
    {
        ptr->field_130 = 0;
        ptr->field_25e = 0;
        Time__get_time(0);
        v3 = ptr->field_25c;
        ptr->field_134 = v1;
        if (v3 && !ptr->field_25d)
        {
            MonoBehaviour__StopCoroutine(ptr, g_1f0d6b8, 0);
            v4 = ptr->field_30;
            if (v4)
            {
                Transform__get_position(v4, 0);
                MonoBehaviour__StartCoroutine(ptr, AI__RotateTowards(ptr, 0), 0);
                goto LABEL_107f26c;
            }
        }
        else
        {
LABEL_107f26c:
            if (ptr->field_12d)
            {
                if (!g_1ef0c58->field_e0)
                    sub_f7da5c(g_1ef0c58);
                if (!((char)Object__op_Implicit(ptr->field_158, 0) & 1))
                {
                    if (!g_1ef0c58->field_e0)
                        sub_f7da5c(g_1ef0c58);
                    if ((Object__op_Implicit(ptr->field_160, 0) & 1))
                        goto LABEL_107f2bc;
                    goto LABEL_107f4a8;
                }
LABEL_107f2bc:
                if (!g_1ef0c58->field_e0)
                    sub_f7da5c(g_1ef0c58);
                if (((char)Object__op_Implicit(ptr->field_188, 0) & 1))
                {
                    v4 = ptr->field_188;
                    if (v4)
                    {
                        AudioClip__get_length(v4, 0);
                        Time__get_time(0);
                        v0 = ptr->field_19c + v1;
                        v6 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(v0, v1)) >> 5 & 3 | (unsigned long long)(CmpF(v0, v1) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v0, v1)) >> 5 & 3 | (unsigned long long)(CmpF(v0, v1) & 1)) & ((unsigned long long)(char)(CmpF(v0, v1)) >> 5 & 3 | (unsigned long long)(CmpF(v0, v1) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                        if ((char)v6)
                            goto LABEL_107f330;
                        goto LABEL_107f30c;
                    }
                }
                else
                {
LABEL_107f30c:
                    if (!g_1ef0c58->field_e0)
                        sub_f7da5c(g_1ef0c58);
                    if (!((char)Object__op_Implicit(ptr->field_188, 0) & 1))
                    {
LABEL_107f330:
                        Random__get_value(0);
                        v4 = ptr->field_1d8;
                        v7 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v1, 0x3f000000)) >> 5 & 3 | (unsigned long long)(CmpF(v1, 0x3f000000) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v1, 0x3f000000)) >> 5 & 3 | (unsigned long long)(CmpF(v1, 0x3f000000) & 1)) & ((unsigned long long)(char)(CmpF(v1, 0x3f000000)) >> 5 & 3 | (unsigned long long)(CmpF(v1, 0x3f000000) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                        if (!((char)v7))
                        {
                            if (v4)
                                goto LABEL_107f43c;
                        }
                        else
                        {
                            if (v4)
                            {
LABEL_107f43c:
                                AudioSource__set_clip();
                                v0 = 0x3f800000;
                                v4 = Random__Range(0);
                                if (ptr->field_1d8 && (AudioSource__set_pitch(ptr->field_1d8, 0), v4 = ptr->field_1d8, v4 && (v8 = 0x3f800000, v4 = (long long)(unsigned long long)AudioSource__set_spatialBlend(v4, 0), v9 = (unsigned long)ptr->field_1d8, v9)))
                                {
                                    AudioSource__PlayOneShot(v9, AudioSource__get_clip(v9, 0), 0);
                                    goto LABEL_107f4a8;
                                }
                            }
                        }
                    }
                    else
                    {
LABEL_107f4a8:
                        v4 = ptr->field_100;
                        if (v4)
                        {
                            Transform__get_position(v4, 0);
                            ptr->field_144 = v8;
                            ptr->field_148 = v0;
                            ptr->field_14c = v11;
                            ptr->field_12d = 0;
                            goto LABEL_107f548;
                        }
                    }
                }
            }
            else
            {
                if (!g_1ef0c58->field_e0)
                    sub_f7da5c(g_1ef0c58);
                if (!((char)Object__op_Implicit(ptr->field_168, 0) & 1))
                {
                    if (!g_1ef0c58->field_e0)
                        sub_f7da5c(g_1ef0c58);
                    if ((Object__op_Implicit(ptr->field_170, 0) & 1))
                        goto LABEL_107f39c;
                    goto LABEL_107f540;
                }
LABEL_107f39c:
                if (!g_1ef0c58->field_e0)
                    sub_f7da5c(g_1ef0c58);
                if (((char)Object__op_Implicit(ptr->field_188, 0) & 1))
                {
                    v4 = ptr->field_188;
                    if (v4)
                    {
                        AudioClip__get_length(v4, 0);
                        Time__get_time(0);
                        v12 = ptr->field_19c + v8;
                        v13 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(v12, v8)) >> 5 & 3 | (unsigned long long)(CmpF(v12, v8) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v12, v8)) >> 5 & 3 | (unsigned long long)(CmpF(v12, v8) & 1)) & ((unsigned long long)(char)(CmpF(v12, v8)) >> 5 & 3 | (unsigned long long)(CmpF(v12, v8) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                        if ((char)v13)
                            goto LABEL_107f410;
                        goto LABEL_107f3ec;
                    }
                }
                else
                {
LABEL_107f3ec:
                    if (!g_1ef0c58->field_e0)
                        sub_f7da5c(g_1ef0c58);
                    if (!((char)Object__op_Implicit(ptr->field_188, 0) & 1))
                    {
LABEL_107f410:
                        Random__get_value(0);
                        v4 = ptr->field_1d8;
                        v14 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v8, 0x3f000000)) >> 5 & 3 | (unsigned long long)(CmpF(v8, 0x3f000000) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v8, 0x3f000000)) >> 5 & 3 | (unsigned long long)(CmpF(v8, 0x3f000000) & 1)) & ((unsigned long long)(char)(CmpF(v8, 0x3f000000)) >> 5 & 3 | (unsigned long long)(CmpF(v8, 0x3f000000) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                        if (!((char)v14))
                        {
                            if (v4)
                                goto LABEL_107f4d4;
                        }
                        else
                        {
                            if (v4)
                            {
LABEL_107f4d4:
                                AudioSource__set_clip();
                                v4 = Random__Range(0);
                                if (ptr->field_1d8 && (AudioSource__set_pitch(ptr->field_1d8, 0), v4 = ptr->field_1d8, v4 && (v8 = 0x3f800000, v4 = (long long)(unsigned long long)AudioSource__set_spatialBlend(v4, 0), v15 = (unsigned long)ptr->field_1d8, v15)))
                                {
                                    AudioSource__PlayOneShot(v15, AudioSource__get_clip(v15, 0), 0);
                                    goto LABEL_107f540;
                                }
                            }
                        }
                    }
                    else
                    {
LABEL_107f540:
                        ptr->field_12d = 1;
                        goto LABEL_107f548;
                    }
                }
            }
        }
    }
    else
    {
LABEL_107f548:
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        v17 = Object__op_Implicit(ptr->field_188, 0);
        if (!((char)v17 & 1))
            return v17;
        if (ptr->field_f0 != 1)
            return v17;
        if (!ptr->field_12e)
            return v17;
        if (ptr->field_1a0)
        {
            v18 = ptr->field_138;
        }
        else
        {
            Time__get_time(0);
            v18 = v8;
            ptr->field_138 = v8;
        }
        v19 = Time__get_time(0);
        v20 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v18 + 0x3f000000, v8)) >> 5 & 3 | (unsigned long long)(CmpF(v18 + 0x3f000000, v8) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v18 + 0x3f000000, v8)) >> 5 & 3 | (unsigned long long)(CmpF(v18 + 0x3f000000, v8) & 1)) & ((unsigned long long)(char)(CmpF(v18 + 0x3f000000, v8)) >> 5 & 3 | (unsigned long long)(CmpF(v18 + 0x3f000000, v8) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if ((char)v20)
        {
            ptr->field_1a0 = 0;
            return v19;
        }
        v21 = Time__get_time(0);
        v22 = ptr->field_1a0;
        v23 = ptr->field_198;
        ptr->field_138 = v8;
        v24 = v22 + 1;
        ptr->field_1a0 = v24;
        if (v24 <= v23)
            return v21;
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        if (((char)Object__op_Implicit(ptr->field_190, 0) & 1))
        {
            Random__get_value(0);
            v4 = ptr->field_1d8;
            v25 = arm64g_calculate_condition(192, (((((unsigned long long)(char)(CmpF(v8, 0x3f000000)) >> 5 & 3 | (unsigned long long)(CmpF(v8, 0x3f000000) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v8, 0x3f000000)) >> 5 & 3 | (unsigned long long)(CmpF(v8, 0x3f000000) & 1)) & ((unsigned long long)(char)(CmpF(v8, 0x3f000000)) >> 5 & 3 | (unsigned long long)(CmpF(v8, 0x3f000000) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
            if ((char)v25)
                goto LABEL_107f62c;
            if (v4)
                goto LABEL_107f630;
        }
        else
        {
            v4 = ptr->field_1d8;
LABEL_107f62c:
            if (v4)
            {
LABEL_107f630:
                AudioSource__set_clip();
                v4 = Random__Range(0);
                if (ptr->field_1d8)
                {
                    AudioSource__set_pitch(ptr->field_1d8, 0);
                    v4 = ptr->field_1d8;
                    if (v4)
                    {
                        v4 = AudioSource__set_spatialBlend(v4, 0);
                        v26 = ptr->field_1d8;
                        if (v26)
                        {
                            AudioSource__PlayOneShot(v26, AudioSource__get_clip(v26, 0), 0);
                            v19 = Time__get_time(0);
                            ptr->field_19c = 0x3f800000;
                            ptr->field_1a0 = 0;
                            return v19;
                        }
                    }
                }
            }
        }
    }
    sub_f7db74(v4);
}
```


## `AI.GoToPosition` — RVA `0xc7f6c0`

- Decompiled symbol: `AI_GoToPosition`
- Metadata signature: `public void GoToPosition(Vector3 position, bool runToPos) { }`
- Native interval: `32` bytes
- Result: `pseudocode`
- Heuristic layout hint: `AI_Recovered` matched 3 offsets against `AI` metadata (confidence 0.60).

```c
typedef struct AI_Recovered {
    char padding_0[304];
    char orderedMove;
    char padding_131[19];
    unsigned int startPosition;
    unsigned int field_148;
    unsigned int field_14c;
    char padding_150[270];
    char cancelRotate;
} AI_Recovered;

struct_0 * AI_GoToPosition(struct_0 *ptr, char a1)
{
    unsigned int v0;  // s0
    unsigned int v1;  // s1
    unsigned int v2;  // s2

    ptr->field_144 = v0;
    ptr->field_148 = v1;
    ptr->field_130 = a1 & 1;
    ptr->field_25e = 1;
    ptr->field_14c = v2;
    return ptr;
}
```


## `AI.ChangeFaction` — RVA `0xc7f6e0`

- Decompiled symbol: `AI_ChangeFaction`
- Metadata signature: `public void ChangeFaction(int factionChange) { }`
- Native interval: `48` bytes
- Result: `pseudocode`
- Heuristic layout hint: `AI_Recovered` matched 2 offsets against `AI` metadata (confidence 1.00).

```c
typedef struct AI_Recovered {
    char padding_0[240];
    unsigned int factionNum;
    char padding_f4[324];
    unsigned long long target;
} AI_Recovered;

long long AI_ChangeFaction(struct_0 *ptr, unsigned int a1)
{
    unsigned long v0;  // x0

    ptr->field_238 = 0;
    v0 = sub_f7d8d0(&ptr->field_238, 0);
    ptr->field_f0 = a1;
    return v0;
}
```


## `AI.ctor` — RVA `0xc7f710`

- Decompiled symbol: `AI_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `216` bytes
- Result: `pseudocode`
- Heuristic layout hint: `AI_Recovered` matched 21 offsets against `AI` metadata (confidence 1.00).

```c
typedef struct AI_Recovered {
    char padding_0[200];
    uint128_t randomSpawnChance;
    unsigned long long runAnimSpeed;
    char padding_e0[16];
    unsigned int factionNum;
    char padding_f4[34];
    char walkOnPatrol;
    char padding_117[17];
    unsigned int firstWaypoint;
    char padding_12c[20];
    unsigned int pickNextDestDist;
    char padding_144[16];
    unsigned int vocalVol;
    char padding_158[64];
    unsigned int jokeActivate;
    char padding_19c[28];
    unsigned long long tauntDelay;
    unsigned int tauntVol;
    char padding_1c4[12];
    unsigned int alertVol;
    char padding_1d4[28];
    unsigned long long footStepVol;
    unsigned int runStepTime;
    char padding_1fc[8];
    unsigned long long shootRange;
    unsigned int listenRange;
    char padding_210[4];
    uint128_t shootAnimSpeed;
    unsigned long long delayShootTime;
    unsigned int eyeHeight;
    char padding_230[40];
    unsigned int attackTime;
    char attackFinished;
    char padding_25d[63];
    unsigned int searchMask;
} AI_Recovered;

void AI_ctor(struct_0 *ptr)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    struct_0 *p;  // x8
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    *((unsigned int *)&ptr->padding_12c[12]) = 0x40200000;
    *((unsigned int *)&ptr->padding_158[56]) = 33;
    *((unsigned long long *)((char *)&ptr->field_c8 + 8)) = 0x3f8000003f800000;
    *((uint128_t *)&(&ptr->padding_0)[1]) = 0x3f8000003f80000040c000003f800000;
    *((unsigned long long *)&ptr->padding_19c[20]) = 0x3f00000040000000;
    p = &ptr->padding_1fc;
    *((unsigned int *)&ptr->padding_144[8]) = 1060320051;
    *((unsigned int *)&ptr->field_1b8) = 1060320051;
    *((unsigned int *)&ptr->padding_1c4[4]) = 1060320051;
    *((unsigned long long *)&ptr->padding_1d4[20]) = 0x3f8000003f000000;
    *((unsigned int *)&ptr->field_1f0) = 0x3f800000;
    *((unsigned int *)&ptr->padding_e0[8]) = 1;
    ptr->padding_f4[26] = 1;
    *((unsigned int *)&ptr->padding_117[9]) = 1;
    *((unsigned long long *)&p->padding_0[0]) = 0x41f0000041700000;
    *((unsigned int *)&(&ptr->padding_1fc)[1]) = 0x41f00000;
    *((uint128_t *)&p->padding_0[16]) = 0x404000003ecccccd41f000003f800000;
    *((unsigned long long *)&p->padding_0[32]) = 4557642823950873395;
    *((unsigned int *)((char *)&ptr->field_214 + 12)) = 1053609165;
    *((unsigned int *)&ptr->padding_230[28]) = 0xc1800000;
    ptr->padding_230[32] = 1;
    *((unsigned int *)&ptr->padding_25d[51]) = LayerMask__op_Implicit(0, 0);
}
```


## `AI.<AttackTarget>d__134.Dispose` — RVA `0xc7f7e8`

- Decompiled symbol: `AI_AttackTarget_d__134_Dispose`
- Metadata signature: `private void System.IDisposable.Dispose() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long AI_AttackTarget_d__134_Dispose(void)
{
    unsigned long v0;  // x0

    return v0;
}
```


## `AI.<AttackTarget>d__134.MoveNext` — RVA `0xc7f7ec`

- Decompiled symbol: `AI_AttackTarget_d__134_MoveNext`
- Metadata signature: `private bool MoveNext() { }`
- Native interval: `2556` bytes
- Result: `pseudocode`

```c
extern long long g_1ef0c58;
extern long long g_1ef2440;
extern long long g_1f0d6b8;
extern char g_1fab3ff;
extern char g_85227c;

unsigned int AI_AttackTarget_d__134_MoveNext(unsigned long a0)
{
    if (!(g_1fab3ff & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c(&g_1ef2440);
        sub_f7d92c(&g_1f0d6b8);
        g_1fab3ff = 1;
    }
    if (4 < *((int *)(a0 + 16)))
        return 0;
    goto sub_107f874 + (&g_85227c)[*((int *)(a0 + 16))] * 4;
}
```


## `AI.<AttackTarget>d__134.get_Current` — RVA `0xc801e8`

- Decompiled symbol: `AI_AttackTarget_d__134_get_Current`
- Metadata signature: `private object System.Collections.Generic.IEnumerator<System.Object>.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long AI_AttackTarget_d__134_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```


## `AI.<AttackTarget>d__134.Reset` — RVA `0xc801f0`

- Decompiled symbol: `AI_AttackTarget_d__134_Reset`
- Metadata signature: `private void System.Collections.IEnumerator.Reset() { }`
- Native interval: `56` bytes
- Result: `pseudocode`

```c
extern long long g_1ef0bd8;
extern long long g_1f03f38;

void AI_AttackTarget_d__134_Reset(void)
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
    sub_f7da4c(v4, sub_f7d940(&g_1f03f38));
}
```


## `AI.<AttackTarget>d__134.get_Current` — RVA `0xc80228`

- Decompiled symbol: `AI_AttackTarget_d__134_get_Current`
- Metadata signature: `private object System.Collections.IEnumerator.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long AI_AttackTarget_d__134_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```


## `AI.<Patrol>d__131.Dispose` — RVA `0xc80230`

- Decompiled symbol: `AI_Patrol_d__131_Dispose`
- Metadata signature: `private void System.IDisposable.Dispose() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long AI_Patrol_d__131_Dispose(void)
{
    unsigned long v0;  // x0

    return v0;
}
```


## `AI.<Patrol>d__131.MoveNext` — RVA `0xc80234`

- Decompiled symbol: `AI_Patrol_d__131_MoveNext`
- Metadata signature: `private bool MoveNext() { }`
- Native interval: `2216` bytes
- Result: `pseudocode`

```c
typedef struct struct_6 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[4];
    long long field_18;
    struct struct_5 *field_20;
} struct_6;

typedef struct struct_5 {
    char padding_0[32];
    char field_20;
    char padding_21[7];
    long long field_28;
    char padding_30[24];
    struct struct_2 *field_48;
    char padding_50[48];
    long long field_80;
    char padding_88[8];
    long long field_90;
    void* field_98;
    char field_a0;
    char padding_a1[15];
    long long field_b0;
    char padding_b8[20];
    unsigned int field_cc;
    unsigned int field_d0;
    char padding_d4[8];
    unsigned int field_dc;
    unsigned int field_e0;
    char padding_e4[20];
    unsigned int field_f8;
    char padding_fc[4];
    long long field_100;
    char padding_108[12];
    char field_114;
    char field_115;
    char field_116;
    char padding_117[1];
    char field_118;
    char padding_119[7];
    struct struct_4 *field_120;
    char padding_128[5];
    char field_12d;
    char padding_12e[2];
    char field_130;
    char padding_131[15];
    unsigned int field_140;
    unsigned int field_144;
    unsigned int field_148;
    unsigned int field_14c;
    char padding_150[184];
    unsigned int field_208;
    char padding_20c[12];
    unsigned int field_218;
    char padding_21c[28];
    long long field_238;
    char field_240;
    char padding_241[23];
    unsigned int field_258;
    char field_25c;
    char padding_25d[55];
    char field_294;
    char field_295;
} struct_5;

typedef struct struct_4 {
    char padding_0[40];
    struct struct_3 *field_28;
} struct_4;

typedef struct struct_3 {
    char padding_0[24];
    unsigned int field_18;
} struct_3;

typedef struct struct_2 {
    char padding_0[568];
    long long field_238;
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
extern long long g_1ef2440;
extern long long g_1ef8a90;
extern long long g_1ef8a98;
extern long long g_1f08598;
extern char g_1fab3e0;
extern char g_1fab400;

unsigned int AI_Patrol_d__131_MoveNext(struct_6 *p, unsigned long a1, unsigned long a2, unsigned long a3)
{
    unsigned int flag;  // w8
    struct_5 *ptr;  // x20
    unsigned int v12;  // s1
    unsigned int v13;  // s2
    unsigned long v14;  // x0
    unsigned int v15;  // s2
    unsigned long v16;  // 4205
    long long v17;  // x0
    unsigned int v18;  // s3
    unsigned long v19;  // 4163
    unsigned int v20;  // s0
    long long v21;  // x0
    unsigned long v4;  // x0
    void* addr;  // x26
    unsigned long i;  // x27
    unsigned int v24;  // w8
    unsigned int v25;  // s11
    unsigned long v26;  // 4125
    unsigned int v27;  // w8
    unsigned int v28;  // s2
    unsigned int v29;  // s0
    unsigned long v30;  // 4205
    long long v31;  // x0
    unsigned long v5;  // x21
    unsigned int v32;  // s0
    unsigned int v33;  // s8
    unsigned long v34;  // 4125
    unsigned int v35;  // s2
    unsigned int v36;  // s0
    unsigned long v37;  // 4205
    unsigned int v38;  // s2
    unsigned int v39;  // s0
    unsigned long v40;  // 4218
    unsigned int v41;  // s0
    unsigned int v6;  // s11
    unsigned int v42;  // s8
    unsigned long v43;  // 4138
    struct_5 *ptr3;  // x0
    long long v45;  // x0
    unsigned int v46;  // s0
    unsigned int v47;  // s8
    unsigned long v48;  // 4125
    unsigned long long v49;  // x8
    long long v50;  // x20
    struct_6 *ptr4;  // x19
    unsigned int v7;  // w2
    long long v52;  // x0
    struct_6 *ptr5;  // x19
    unsigned int v8;  // s0
    unsigned long v9;  // 4129
    unsigned long v10;  // 4129
    unsigned int v11;  // s0
    char *v0;  // [bp-0x60]
    char v1;  // [bp+0x0]

    v0 = &v1;
    if (!(g_1fab400 & 1))
    {
        sub_f7d92c(&g_1ef8a90);
        sub_f7d92c(&g_1ef8a98);
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c(&g_1ef0e48);
        sub_f7d92c(&g_1ef2440);
        sub_f7d92c(&g_1f08598);
        g_1fab400 = 1;
    }
    flag = p->field_10;
    ptr = p->field_20;
    if (flag != 2)
    {
        if (flag == 1)
        {
            p->field_10 = 4294967295;
            goto LABEL_1080300;
        }
        else if (flag)
        {
            return 0;
        }
    }
    p->field_10 = 4294967295;
    if (ptr)
    {
        if (ptr->field_114)
        {
            MonoBehaviour__StartCoroutine(ptr, AI__SpawnNPC(ptr), 0);
            return 0;
        }
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        if (!((char)Object__op_Implicit(*((long long *)&ptr->field_118), 0) & 1))
        {
LABEL_10804c4:
            v4 = AI__StandWatch(ptr);
            MonoBehaviour__StartCoroutine(ptr, v4, 0);
            return 0;
        }
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        if (!((char)Object__op_Implicit(ptr->field_120, 0) & 1))
        {
            AI__StandWatch(ptr);
            MonoBehaviour__StartCoroutine(ptr, v4, 0);
            return 0;
        }
        v5 = &ptr->field_118;
        if (*((long long *)v5) && (Transform__get_position(*((long long *)v5), 0), ptr->field_100))
        {
            Transform__get_position(ptr->field_100, 0);
            if (!g_1fab3e0)
            {
                sub_f7d92c("_F");
                g_1fab3e0 = 1;
            }
            if (!g_1ef07e8->field_e0)
                sub_f7da5c(g_1ef07e8);
            if (ptr->field_120 && ptr->field_120->field_28)
            {
                v6 = [D] unsupported_Iop_SqrtF32();
                v7 = sub_14a3dc8(ptr->field_120->field_28, *((long long *)&ptr->field_118), g_1ef8a90);
                if (!ptr->field_115)
                {
LABEL_108048c:
                    v8 = ptr->field_140;
                    v10 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v6, v8)) >> 5 & 3 | (unsigned long long)(CmpF(v6, v8) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v6, v8)) >> 5 & 3 | (unsigned long long)(CmpF(v6, v8) & 1)) & ((unsigned long long)(char)(CmpF(v6, v8)) >> 5 & 3 | (unsigned long long)(CmpF(v6, v8) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                    if (!((char)v10))
                    {
                        if (ptr->field_120 && ptr->field_120->field_28)
                        {
                            if (ptr->field_120->field_28->field_18 == 1)
                            {
                                ptr->field_dc = 0;
                                ptr->field_144 = v11;
                                ptr->field_148 = v12;
                                ptr->field_14c = v13;
                                AI__StandWatch(ptr);
                                MonoBehaviour__StartCoroutine(ptr, v4, 0);
                                return 0;
                            }
                            v14 = (unsigned long long)AI__PickNextWaypoint(ptr, *((long long *)&ptr->field_118), v7);
                            *((unsigned long *)&ptr->field_118) = v14;
                            sub_f7d8d0(v5, v14);
                            if (!ptr->field_20)
                                goto LABEL_10805ac;
                            if (ptr->field_100)
                            {
                                Transform__get_position(ptr->field_100, 0);
                                if (!g_1fab3e0)
                                {
                                    sub_f7d92c("_F");
                                    g_1fab3e0 = 1;
                                }
                                if (!g_1ef07e8->field_e0)
                                    sub_f7da5c(g_1ef07e8);
                                v15 = ptr->field_140;
                                v8 = [D] unsupported_Iop_SqrtF32();
                                v16 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v8, v15)) >> 5 & 3 | (unsigned long long)(CmpF(v8, v15) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v8, v15)) >> 5 & 3 | (unsigned long long)(CmpF(v8, v15) & 1)) & ((unsigned long long)(char)(CmpF(v8, v15)) >> 5 & 3 | (unsigned long long)(CmpF(v8, v15) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                                if (!((char)v16))
                                {
                                    ptr->field_116 = 1;
                                    goto LABEL_10805ac;
                                }
                            }
                        }
                    }
                    else
                    {
LABEL_10805ac:
                        Time__get_time(0);
                        v17 = ptr->field_28;
                        v18 = ptr->field_f8 + 0x40c00000;
                        v19 = arm64g_calculate_condition(192, (((((unsigned long long)(char)(CmpF(v18, v8)) >> 5 & 3 | (unsigned long long)(CmpF(v18, v8) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v18, v8)) >> 5 & 3 | (unsigned long long)(CmpF(v18, v8) & 1)) & ((unsigned long long)(char)(CmpF(v18, v8)) >> 5 & 3 | (unsigned long long)(CmpF(v18, v8) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                        if ((char)v19)
                            v20 = ptr->field_208 * 0x40c00000;
                        else
                            v20 = ptr->field_208;
                        ptr->field_218 = v20;
                        if (v17)
                        {
                            if (((char)GameObject__get_activeInHierarchy(v17, 0) & 1) && !ptr->field_a0)
                            {
                                if (ptr->field_48)
                                {
                                    if (!g_1ef0c58->field_e0)
                                        sub_f7da5c(g_1ef0c58);
                                    v21 = Object__op_Implicit(ptr->field_48->field_238, 0);
                                    if (!(v21 & 1))
                                        goto LABEL_1080698;
                                    addr = ptr->field_98;
                                    if (addr)
                                    {
                                        if ((int)(long long)addr[24] >= 1)
                                        {
                                            i = 0;
                                            v24 = (long long)addr[24];
                                            do
                                            {
                                                if (v24 <= i)
                                                    sub_f7db7c(v21);
                                                if (!ptr->field_48)
                                                {
                                                    sub_f7db74();
                                                    sub_f7db7c(v21);
                                                }
                                                if (!g_1ef0e48->field_e0)
                                                    sub_f7da5c(g_1ef0e48);
                                                v21 = Physics__IgnoreCollision(*((long long *)(32 + (char *)addr + 8 * i)), ptr->field_48->field_238, 1, 0);
                                                v24 = (int)addr[24];
                                                i += 1;
                                            } while (i < v24);
                                        }
                                        ptr->field_a0 = 1;
                                        goto LABEL_1080698;
                                    }
                                }
                            }
                            else
                            {
LABEL_1080698:
                                AI__CanSeeTarget(ptr);
                                if (!g_1ef0c58->field_e0)
                                    sub_f7da5c(g_1ef0c58);
                                if (((char)Object__op_Implicit(ptr->field_238, 0) & 1) && ptr->field_240 || ptr->field_294 || ptr->field_295)
                                {
                                    v52 = MonoBehaviour__StartCoroutine(ptr, AI__AttackTarget(ptr), 0);
                                    p->field_18 = v52;
                                    ptr5 = &p->field_18;
                                    sub_f7d8d0(ptr5, v52);
                                    *((unsigned int *)&ptr5->padding_0[8]) = 1;
                                    return 1;
                                }
                                if (!g_1ef0c58->field_e0)
                                    sub_f7da5c(g_1ef0c58);
                                if (((char)Object__op_Implicit(ptr->field_80, 0) & 1))
                                {
                                    if (ptr->field_100 && (Component__get_gameObject(ptr->field_100, 0), ptr->field_100 && (Transform__get_position(ptr->field_100, 0), ptr->field_80)))
                                    {
                                        NPCRegistry__FindClosestTarget();
                                        goto LABEL_1080770;
                                    }
                                }
                                else
                                {
LABEL_1080770:
                                    v25 = ptr->field_258;
                                    Time__get_time(0);
                                    v26 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v25, v20)) >> 5 & 3 | (unsigned long long)(CmpF(v25, v20) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v25, v20)) >> 5 & 3 | (unsigned long long)(CmpF(v25, v20) & 1)) & ((unsigned long long)(char)(CmpF(v25, v20)) >> 5 & 3 | (unsigned long long)(CmpF(v25, v20) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                                    if ((char)v26)
                                    {
LABEL_1080300:
                                        v50 = sub_f7db70(g_1ef2440);
                                        WaitForSeconds__ctor(v50, 0);
                                        p->field_18 = v50;
                                        ptr4 = &p->field_18;
                                        sub_f7d8d0(ptr4, v50);
                                        *((unsigned int *)&ptr4->padding_0[8]) = 2;
                                        return 1;
                                    }
                                    v27 = ptr->field_12d;
                                    if (ptr->field_130)
                                    {
                                        if (v27)
                                            goto LABEL_1080990;
                                        if (ptr->field_100)
                                        {
                                            Transform__get_position(ptr->field_100, 0);
                                            if (!g_1fab3e0)
                                            {
                                                sub_f7d92c("_F");
                                                g_1fab3e0 = 1;
                                            }
                                            if (!g_1ef07e8->field_e0)
                                                sub_f7da5c(g_1ef07e8);
                                            v28 = ptr->field_140;
                                            v29 = [D] unsupported_Iop_SqrtF32();
                                            v30 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v29, v28)) >> 5 & 3 | (unsigned long long)(CmpF(v29, v28) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v29, v28)) >> 5 & 3 | (unsigned long long)(CmpF(v29, v28) & 1)) & ((unsigned long long)(char)(CmpF(v29, v28)) >> 5 & 3 | (unsigned long long)(CmpF(v29, v28) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                                            if (!((char)v30))
                                            {
                                                ptr->field_dc = ptr->field_cc;
                                                goto LABEL_1080ac8;
                                            }
                                            else
                                            {
                                                v31 = ptr->field_90;
                                                ptr->field_dc = 0;
                                                if (v31)
                                                {
                                                    NavMeshAgent__set_isStopped(v31, 1, 0);
                                                    v32 = ptr->field_dc;
                                                    AI__SetSpeed(ptr, 1, 0);
                                                    if (!ptr->field_25c || !((v33 = ptr->field_258, Time__get_time(0), v34 = (unsigned long)arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v33, v32)) >> 5 & 3 | (unsigned long long)(CmpF(v33, v32) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v33, v32)) >> 5 & 3 | (unsigned long long)(CmpF(v33, v32) & 1)) & ((unsigned long long)(char)(CmpF(v33, v32)) >> 5 & 3 | (unsigned long long)(CmpF(v33, v32) & 1)) >> 1 & 1)) * 0x10000000, 0, 0), !((char)v34))))
                                                        goto LABEL_10804c4;
                                                    if (ptr->field_b0)
                                                    {
                                                        Animator__SetInteger(ptr->field_b0, g_1f08598, 0, 0);
                                                        AI__StandWatch(ptr);
                                                        MonoBehaviour__StartCoroutine(ptr, v4, 0);
                                                        return 0;
                                                    }
                                                }
                                            }
                                        }
                                    }
                                    else
                                    {
                                        if (!v27)
                                        {
LABEL_1080990:
                                            ptr3 = ptr;
                                            v49 = 204;
                                            if (ptr->field_116)
                                                v49 = 208;
                                            ptr->field_dc = *((int *)&ptr->padding_0[v49]);
                                            goto LABEL_1080acc;
                                        }
                                        if (ptr->field_28 && GameObject__get_transform(ptr->field_28, 0) && (Transform__get_position(), ptr->field_100))
                                        {
                                            Transform__get_position(ptr->field_100, 0);
                                            if (!g_1fab3e0)
                                            {
                                                sub_f7d92c("_F");
                                                g_1fab3e0 = 1;
                                            }
                                            if (!g_1ef07e8->field_e0)
                                                sub_f7da5c(g_1ef07e8);
                                            v35 = ptr->field_140;
                                            v36 = [D] unsupported_Iop_SqrtF32();
                                            v37 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v36, v35)) >> 5 & 3 | (unsigned long long)(CmpF(v36, v35) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v36, v35)) >> 5 & 3 | (unsigned long long)(CmpF(v36, v35) & 1)) & ((unsigned long long)(char)(CmpF(v36, v35)) >> 5 & 3 | (unsigned long long)(CmpF(v36, v35) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                                            if (!((char)v37))
                                            {
                                                if (ptr->field_28 && GameObject__get_transform(ptr->field_28, 0) && (Transform__get_position(), ptr->field_100))
                                                {
                                                    Transform__get_position(ptr->field_100, 0);
                                                    if (!g_1fab3e0)
                                                    {
                                                        sub_f7d92c("_F");
                                                        g_1fab3e0 = 1;
                                                    }
                                                    if (!g_1ef07e8->field_e0)
                                                        sub_f7da5c(g_1ef07e8);
                                                    v38 = ptr->field_140;
                                                    v39 = [D] unsupported_Iop_SqrtF32();
                                                    v40 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v39, v38 * 2)) >> 5 & 3 | (unsigned long long)(CmpF(v39, v38 * 2) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v39, v38 * 2)) >> 5 & 3 | (unsigned long long)(CmpF(v39, v38 * 2) & 1)) & ((unsigned long long)(char)(CmpF(v39, v38 * 2)) >> 5 & 3 | (unsigned long long)(CmpF(v39, v38 * 2) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                                                    if (!((char)v40))
                                                    {
                                                        v41 = ptr->field_cc;
                                                        ptr->field_dc = v41;
                                                        Time__get_time(0);
                                                        ptr->field_e0 = v41;
                                                    }
                                                    else
                                                    {
                                                        v42 = ptr->field_e0;
                                                        Time__get_time(0);
                                                        v43 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v42 + 0x40000000, v39)) >> 5 & 3 | (unsigned long long)(CmpF(v42 + 0x40000000, v39) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v42 + 0x40000000, v39)) >> 5 & 3 | (unsigned long long)(CmpF(v42 + 0x40000000, v39) & 1)) & ((unsigned long long)(char)(CmpF(v42 + 0x40000000, v39)) >> 5 & 3 | (unsigned long long)(CmpF(v42 + 0x40000000, v39) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                                                        if (!((char)v43))
                                                            ptr->field_dc = ptr->field_d0;
                                                    }
                                                    if (ptr->field_28 && GameObject__get_transform(ptr->field_28, 0))
                                                    {
                                                        Transform__get_position();
LABEL_1080ac8:
                                                        ptr3 = ptr;
LABEL_1080acc:
                                                        AI__TravelToPoint(ptr3, 0);
                                                        goto LABEL_1080300;
                                                    }
                                                }
                                            }
                                            else
                                            {
                                                v45 = ptr->field_90;
                                                ptr->field_dc = 0;
                                                if (v45)
                                                {
                                                    NavMeshAgent__set_isStopped(v45, 1, 0);
                                                    v46 = ptr->field_dc;
                                                    AI__SetSpeed(ptr, 1, 0);
                                                    if (!ptr->field_25c || !((v47 = ptr->field_258, Time__get_time(0), v48 = (unsigned long)arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v47, v46)) >> 5 & 3 | (unsigned long long)(CmpF(v47, v46) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v47, v46)) >> 5 & 3 | (unsigned long long)(CmpF(v47, v46) & 1)) & ((unsigned long long)(char)(CmpF(v47, v46)) >> 5 & 3 | (unsigned long long)(CmpF(v47, v46) & 1)) >> 1 & 1)) * 0x10000000, 0, 0), !((char)v48))))
                                                        goto LABEL_1080300;
                                                    if (ptr->field_b0)
                                                    {
                                                        Animator__SetInteger(ptr->field_b0, g_1f08598, 0, 0);
                                                        goto LABEL_1080300;
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
                else if (ptr->field_120 && ptr->field_120->field_28)
                {
                    if (v7 != ptr->field_120->field_28->field_18 - 1)
                        goto LABEL_108048c;
                    v8 = ptr->field_140;
                    v9 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(v6, v8)) >> 5 & 3 | (unsigned long long)(CmpF(v6, v8) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v6, v8)) >> 5 & 3 | (unsigned long long)(CmpF(v6, v8) & 1)) & ((unsigned long long)(char)(CmpF(v6, v8)) >> 5 & 3 | (unsigned long long)(CmpF(v6, v8) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                    if ((char)v9)
                    {
                        ptr->field_dc = 0;
                        ptr->field_144 = v11;
                        ptr->field_148 = v12;
                        ptr->field_14c = v13;
                        AI__StandWatch(ptr);
                        MonoBehaviour__StartCoroutine(ptr, v4, 0);
                        return 0;
                    }
                    goto LABEL_10805ac;
                }
            }
        }
    }
    v21 = sub_f7db74();
    sub_f7db7c(v21);
}
```


## `AI.<Patrol>d__131.get_Current` — RVA `0xc80f60`

- Decompiled symbol: `AI_Patrol_d__131_get_Current`
- Metadata signature: `private object System.Collections.Generic.IEnumerator<System.Object>.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long AI_Patrol_d__131_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```


## `AI.<Patrol>d__131.Reset` — RVA `0xc80f68`

- Decompiled symbol: `AI_Patrol_d__131_Reset`
- Metadata signature: `private void System.Collections.IEnumerator.Reset() { }`
- Native interval: `56` bytes
- Result: `pseudocode`

```c
extern long long g_1ef0bd8;
extern long long g_1f03f40;

void AI_Patrol_d__131_Reset(void)
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
    sub_f7da4c(v4, sub_f7d940(&g_1f03f40));
}
```


## `AI.<Patrol>d__131.get_Current` — RVA `0xc80fa0`

- Decompiled symbol: `AI_Patrol_d__131_get_Current`
- Metadata signature: `private object System.Collections.IEnumerator.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long AI_Patrol_d__131_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```


## `AI.<PlayFootSteps>d__141.Dispose` — RVA `0xc80fa8`

- Decompiled symbol: `AI_PlayFootSteps_d__141_Dispose`
- Metadata signature: `private void System.IDisposable.Dispose() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long AI_PlayFootSteps_d__141_Dispose(void)
{
    unsigned long v0;  // x0

    return v0;
}
```


## `AI.<PlayFootSteps>d__141.MoveNext` — RVA `0xc80fac`

- Decompiled symbol: `AI_PlayFootSteps_d__141_MoveNext`
- Metadata signature: `private bool MoveNext() { }`
- Native interval: `344` bytes
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
    char padding_0[480];
    long long field_1e0;
    void* field_1e8;
    char padding_1f0[12];
    unsigned int field_1fc;
} struct_0;

extern long long g_1ef2440;
extern char g_1fab401;

unsigned long long AI_PlayFootSteps_d__141_MoveNext(struct_1 *ptr)
{
    unsigned long long v1;  // d8
    unsigned int v2;  // w21
    struct_1 *addr;  // x19
    struct_0 *p;  // x22
    unsigned int v4;  // s0
    unsigned long v5;  // 4129
    void* v6;  // x23
    long long v7;  // x0
    long long v8;  // x20
    long long v10;  // x20
    unsigned long long v0;  // [bp-0x40]

    v0 = v1;
    if (!(g_1fab401 & 1))
    {
        sub_f7d92c(&g_1ef2440);
        g_1fab401 = 1;
    }
    v2 = ptr->field_10;
    if (1 < v2)
    {
LABEL_10810e0:
        if (2 > v2)
            return 1;
        return 0;
    }
    p = ptr->field_20;
    ptr->field_10 = 4294967295;
    if (p && p->field_1e8)
    {
        if (!((long long)p->field_1e8[24] && !((v4 = p->field_1fc, v5 = (unsigned long)arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v4, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v4, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v4, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v4, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v4, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v4, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0), (char)v5))))
        {
LABEL_10810a4:
            v10 = sub_f7db70(g_1ef2440);
            WaitForSeconds__ctor(v10, 0);
            ptr->field_18 = v10;
            addr = &ptr->field_18;
            sub_f7d8d0(addr, v10);
            *((unsigned int *)&addr->padding_0[8]) = 1;
            goto LABEL_10810e0;
        }
        else if (p->field_1e0 && (AudioSource__set_pitch(p->field_1e0, 0), p->field_1e0 && (AudioSource__set_volume(p->field_1e0, 0), v6 = p->field_1e8, v6)))
        {
            v7 = Random__Range(0, (int)v6[24], 0);
            if ((int)v6[24] <= (int)v7)
                sub_f7db7c(v7);
            if (p->field_1e0 && (AudioSource__set_clip(p->field_1e0, *((long long *)(32 + (char *)v6 + 8 * (v7 & 4294967295))), 0), v8 = p->field_1e0, v8))
            {
                AudioSource__PlayOneShot(v8, AudioSource__get_clip(v8, 0), 0);
                goto LABEL_10810a4;
            }
        }
    }
    v7 = sub_f7db74();
    sub_f7db7c(v7);
}
```


## `AI.<PlayFootSteps>d__141.get_Current` — RVA `0xc81104`

- Decompiled symbol: `AI_PlayFootSteps_d__141_get_Current`
- Metadata signature: `private object System.Collections.Generic.IEnumerator<System.Object>.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long AI_PlayFootSteps_d__141_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```


## `AI.<PlayFootSteps>d__141.Reset` — RVA `0xc8110c`

- Decompiled symbol: `AI_PlayFootSteps_d__141_Reset`
- Metadata signature: `private void System.Collections.IEnumerator.Reset() { }`
- Native interval: `56` bytes
- Result: `pseudocode`

```c
extern long long g_1ef0bd8;
extern long long g_1f03f48;

void AI_PlayFootSteps_d__141_Reset(void)
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
    sub_f7da4c(v4, sub_f7d940(&g_1f03f48));
}
```


## `AI.<PlayFootSteps>d__141.get_Current` — RVA `0xc81144`

- Decompiled symbol: `AI_PlayFootSteps_d__141_get_Current`
- Metadata signature: `private object System.Collections.IEnumerator.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long AI_PlayFootSteps_d__141_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```


## `AI.<RotateTowards>d__136.Dispose` — RVA `0xc8114c`

- Decompiled symbol: `AI_RotateTowards_d__136_Dispose`
- Metadata signature: `private void System.IDisposable.Dispose() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long AI_RotateTowards_d__136_Dispose(void)
{
    unsigned long v0;  // x0

    return v0;
}
```


## `AI.<RotateTowards>d__136.MoveNext` — RVA `0xc81150`

- Decompiled symbol: `AI_RotateTowards_d__136_MoveNext`
- Metadata signature: `private bool MoveNext() { }`
- Native interval: `840` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[352];
    long long field_160;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab402;

unsigned int AI_RotateTowards_d__136_MoveNext(void* ptr, unsigned int a1, unsigned int a2)
{
    void* p;  // x20
    unsigned int v3;  // s0
    unsigned int v11;  // s2
    unsigned int v12;  // s2
    unsigned long v13;  // x9
    unsigned long addr;  // x10
    unsigned int v15;  // s8
    unsigned int v16;  // 4101
    unsigned long v17;  // 4124
    unsigned int v18;  // s9
    unsigned int v19;  // 4101
    unsigned int v4;  // s1
    unsigned long v20;  // 4124
    long long v21;  // x21
    long long v22;  // x20
    void* ptr3;  // x19
    unsigned long v5;  // 4138
    unsigned int v6;  // w8
    struct_1 *v7;  // x8
    unsigned int v8;  // w0
    unsigned int v9;  // s3
    unsigned int v10;  // s0
    unsigned int v0;  // [bp-0x80]
    unsigned int v1;  // [bp-0x74]

    if (!(g_1fab402 & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab402 = 1;
    }
    p = (long long)ptr[32];
    if ((int)ptr[16] != 1)
    {
        if ((int)ptr[16])
            return 0;
        *((unsigned int *)&ptr[16]) = 4294967295;
        Time__get_time(0);
        *((unsigned int *)&ptr[64]) = v3;
        if (p && (AI__SetSpeed(p, a1, a2), (long long)p[144]))
        {
            NavMeshAgent__set_isStopped((long long)p[144], 1, 0);
            goto LABEL_10811ec;
        }
    }
    else
    {
        *((unsigned int *)&ptr[16]) = 4294967295;
LABEL_10811ec:
        Time__get_time(0);
        v4 = (int)ptr[64] + (int)ptr[60];
        v5 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v4, v3)) >> 5 & 3 | (unsigned long long)(CmpF(v4, v3) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v4, v3)) >> 5 & 3 | (unsigned long long)(CmpF(v4, v3) & 1)) & ((unsigned long long)(char)(CmpF(v4, v3)) >> 5 & 3 | (unsigned long long)(CmpF(v4, v3) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if (!((char)v5))
        {
            if (p)
            {
                if ((char)p[606])
                {
                    *((unsigned short *)&p[605]) = 0;
                    return 0;
                }
                v6 = (char)p[640];
                *((char *)&p[605]) = 1;
                if (v6)
                {
                    v7 = (long long)p[72];
                    if (v7 && v7->field_160 && GameObject__get_transform(v7->field_160, 0))
                    {
                        Transform__get_position();
                        *((unsigned int *)&ptr[40]) = v3;
                        *((unsigned int *)&ptr[44]) = v4;
                        *((unsigned int *)&ptr[48]) = v11;
                        goto LABEL_1081390;
                    }
                }
                else
                {
                    if (!g_1ef0c58->field_e0)
                        sub_f7da5c(g_1ef0c58);
                    v8 = Object__op_Implicit((long long)p[568], 0);
                    if ((v8 & (char)ptr[52] & 1))
                    {
                        if (!g_1ef0c58->field_e0)
                            sub_f7da5c(g_1ef0c58);
                        if (((char)Object__op_Equality((long long)p[568], (long long)p[48], 0) & 1))
                        {
LABEL_10812ec:
                            if ((long long)p[568] && (Transform__get_position((long long)p[568], 0), (long long)p[568]))
                            {
                                Transform__get_up((long long)p[568], 0);
                                v9 = (int)p[636];
                                v10 = v3 + v3 * v9;
                                v12 = v11 + v11 * v9;
                                *((unsigned int *)&p[644]) = v10;
                                *((unsigned int *)&p[648]) = v4 + v4 * v9;
                                *((unsigned int *)&p[652]) = v12;
                                goto LABEL_1081390;
                            }
                        }
                        else
                        {
                            if (!g_1ef0c58->field_e0)
                                sub_f7da5c(g_1ef0c58);
                            if (!(Object__op_Implicit((long long)p[136], 0) & 1))
                                goto LABEL_108137c;
                            if ((long long)p[136])
                            {
                                if ((Behaviour__get_enabled((long long)p[136], 0) & 1))
                                    goto LABEL_10812ec;
                                goto LABEL_108137c;
                            }
                        }
                    }
                    else
                    {
LABEL_108137c:
                        v13 = (long long)ptr[40];
                        addr = p + 644;
                        *((int *)(addr + 8)) = (int)ptr[48];
                        *((unsigned long *)addr) = v13;
LABEL_1081390:
                        if ((long long)p[0x100])
                        {
                            Transform__get_position((long long)p[0x100], 0);
                            v15 = (int)p[644] - v10;
                            v16 = CmpF(v15, 0.0);
                            v17 = (((CmpF(v15, 0.0) >> 5 & 3 | CmpF(v15, 0.0) & 1) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1;
                            if ((char)((v17 - ((CmpF(v15, 0.0) >> 5 & 3 | CmpF(v15, 0.0) & 1) & (v16 >> 5 & 3 | CmpF(v15, 0.0) & 1) >> 1 & 1)) * 0x10000000 >> 30))
                            {
                                *((unsigned short *)&p[605]) = 0;
                                return 0;
                            }
                            v18 = (int)p[652] - v12;
                            v19 = CmpF(v18, 0.0);
                            v20 = (((CmpF(v18, 0.0) >> 5 & 3 | CmpF(v18, 0.0) & 1) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1;
                            if ((char)((v20 - ((CmpF(v18, 0.0) >> 5 & 3 | CmpF(v18, 0.0) & 1) & (v19 >> 5 & 3 | CmpF(v18, 0.0) & 1) >> 1 & 1)) * 0x10000000 >> 30))
                            {
                                *((unsigned short *)&p[605]) = 0;
                                return 0;
                            }
                            v21 = (long long)p[0x100];
                            if (v21)
                            {
                                Transform__get_rotation(v21, 0);
                                v1 = v10;
                                Quaternion__LookRotation(0);
                                Time__get_deltaTime(0);
                                v0 = (int)ptr[56] * v15;
                                Quaternion__Slerp(0);
                                Transform__set_rotation(v21, 0);
                                v22 = (long long)p[0x100];
                                if (v22)
                                {
                                    Transform__get_eulerAngles(v22, 0);
                                    Transform__set_eulerAngles(v22, 0);
                                    *((unsigned long long *)&ptr[24]) = 0;
                                    ptr3 = ptr + 24;
                                    sub_f7d8d0(ptr3, 0);
                                    *((unsigned int *)&ptr3[8]) = 1;
                                    return 1;
                                }
                            }
                        }
                    }
                }
            }
        }
        else
        {
            if (p)
            {
                *((unsigned short *)&p[605]) = 0;
                return 0;
            }
        }
    }
    sub_f7db74();
}
```


## `AI.<RotateTowards>d__136.get_Current` — RVA `0xc81498`

- Decompiled symbol: `AI_RotateTowards_d__136_get_Current`
- Metadata signature: `private object System.Collections.Generic.IEnumerator<System.Object>.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long AI_RotateTowards_d__136_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```


## `AI.<RotateTowards>d__136.Reset` — RVA `0xc814a0`

- Decompiled symbol: `AI_RotateTowards_d__136_Reset`
- Metadata signature: `private void System.Collections.IEnumerator.Reset() { }`
- Native interval: `56` bytes
- Result: `pseudocode`

```c
extern long long g_1ef0bd8;
extern long long g_1f03f50;

void AI_RotateTowards_d__136_Reset(void)
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
    sub_f7da4c(v4, sub_f7d940(&g_1f03f50));
}
```


## `AI.<RotateTowards>d__136.get_Current` — RVA `0xc814d8`

- Decompiled symbol: `AI_RotateTowards_d__136_get_Current`
- Metadata signature: `private object System.Collections.IEnumerator.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long AI_RotateTowards_d__136_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```


## `AI.<Shoot>d__133.Dispose` — RVA `0xc814e0`

- Decompiled symbol: `AI_Shoot_d__133_Dispose`
- Metadata signature: `private void System.IDisposable.Dispose() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long AI_Shoot_d__133_Dispose(void)
{
    unsigned long v0;  // x0

    return v0;
}
```


## `AI.<Shoot>d__133.MoveNext` — RVA `0xc814e4`

- Decompiled symbol: `AI_Shoot_d__133_MoveNext`
- Metadata signature: `private bool MoveNext() { }`
- Native interval: `516` bytes
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
    char padding_0[80];
    unsigned long long field_50;
    char padding_58[56];
    long long field_90;
    char padding_98[24];
    long long field_b0;
    char padding_b8[36];
    unsigned int field_dc;
    char padding_e0[208];
    char field_1b0;
    char padding_1b1[39];
    long long field_1d8;
    char padding_1e0[120];
    unsigned int field_258;
    char field_25c;
} struct_0;

extern long long g_1ef2440;
extern long long g_1f08598;
extern char g_1fab403;

unsigned int AI_Shoot_d__133_MoveNext(struct_1 *ptr, unsigned int a1, unsigned int a2)
{
    unsigned int flag;  // w8
    struct_0 *p;  // x20
    long long v2;  // x20
    struct_1 *addr;  // x19
    unsigned int v4;  // s0
    long long v5;  // x20
    struct_1 *ptr3;  // x19
    long long v7;  // x0

    if (!(g_1fab403 & 1))
    {
        sub_f7d92c(&g_1ef2440);
        sub_f7d92c("k\t");
        sub_f7d92c(&g_1f08598);
        g_1fab403 = 1;
    }
    flag = ptr->field_10;
    p = ptr->field_20;
    if (flag == 2)
    {
        ptr->field_10 = 4294967295;
        if (p)
        {
            v7 = p->field_b0;
            p->field_25c = 1;
            if (v7)
            {
                Animator__SetInteger(v7, g_1f08598, 0, 0);
                return 0;
            }
        }
    }
    else if (flag == 1)
    {
        ptr->field_10 = 4294967295;
        if (p && p->field_50)
        {
            NPCAttack__Fire();
            if (!p->field_1b0)
            {
LABEL_1081664:
                Time__get_time(0);
                p->field_258 = v4 + 0x40000000;
                Random__Range(0);
                v5 = sub_f7db70(g_1ef2440);
                WaitForSeconds__ctor(v5, 0);
                ptr->field_18 = v5;
                ptr3 = &ptr->field_18;
                sub_f7d8d0(ptr3, v5);
                *((unsigned int *)&ptr3->padding_0[8]) = 2;
                return 1;
            }
            if (p->field_1d8)
            {
                AudioSource__Stop(p->field_1d8, 0);
                goto LABEL_1081664;
            }
        }
    }
    else if (!flag)
    {
        ptr->field_10 = 4294967295;
        if (p)
        {
            p->field_25c = 0;
            p->field_dc = 0;
            AI__SetSpeed(p, a1, a2);
            if (p->field_90)
            {
                NavMeshAgent__set_isStopped(p->field_90, 1, 0);
                if (p->field_b0)
                {
                    Animator__SetInteger(p->field_b0, g_1f08598, 3, 0);
                    if (p->field_b0)
                    {
                        Animator__SetTrigger(p->field_b0, g_1f087c8, 0);
                        v2 = sub_f7db70(g_1ef2440);
                        WaitForSeconds__ctor(v2, 0);
                        ptr->field_18 = v2;
                        addr = &ptr->field_18;
                        sub_f7d8d0(addr, v2);
                        *((unsigned int *)&addr->padding_0[8]) = 1;
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


## `AI.<Shoot>d__133.get_Current` — RVA `0xc81764`

- Decompiled symbol: `AI_Shoot_d__133_get_Current`
- Metadata signature: `private object System.Collections.Generic.IEnumerator<System.Object>.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long AI_Shoot_d__133_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```


## `AI.<Shoot>d__133.Reset` — RVA `0xc8176c`

- Decompiled symbol: `AI_Shoot_d__133_Reset`
- Metadata signature: `private void System.Collections.IEnumerator.Reset() { }`
- Native interval: `56` bytes
- Result: `pseudocode`

```c
extern long long g_1ef0bd8;
extern long long g_1f03f58;

void AI_Shoot_d__133_Reset(void)
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
    sub_f7da4c(v4, sub_f7d940(&g_1f03f58));
}
```


## `AI.<Shoot>d__133.get_Current` — RVA `0xc817a4`

- Decompiled symbol: `AI_Shoot_d__133_get_Current`
- Metadata signature: `private object System.Collections.IEnumerator.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long AI_Shoot_d__133_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```


## `AI.<SpawnNPC>d__127.Dispose` — RVA `0xc817ac`

- Decompiled symbol: `AI_SpawnNPC_d__127_Dispose`
- Metadata signature: `private void System.IDisposable.Dispose() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long AI_SpawnNPC_d__127_Dispose(void)
{
    unsigned long v0;  // x0

    return v0;
}
```


## `AI.<SpawnNPC>d__127.MoveNext` — RVA `0xc817b0`

- Decompiled symbol: `AI_SpawnNPC_d__127_MoveNext`
- Metadata signature: `private bool MoveNext() { }`
- Native interval: `1156` bytes
- Result: `pseudocode`

```c
typedef struct struct_3 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[4];
    long long field_18;
    void* field_20;
} struct_3;

typedef struct struct_11 {
    char padding_0[40];
    struct struct_10 *field_28;
    struct struct_10 *field_30;
    char padding_38[16];
    struct struct_12 *field_48;
    char padding_50[64];
    struct struct_10 *field_90;
    char padding_98[40];
    unsigned long long field_c0;
    char padding_c8[4];
    unsigned int field_cc;
    char padding_d0[12];
    unsigned int field_dc;
    char padding_e0[16];
    unsigned int field_f0;
    char padding_f4[12];
    unsigned long long field_100;
    char padding_108[12];
    char field_114;
    char padding_115[3];
    struct struct_10 *field_118;
    struct struct_9 *field_120;
    unsigned int field_128;
    char field_12c;
    char padding_12d[23];
    unsigned int field_144;
    unsigned int field_148;
    unsigned int field_14c;
    unsigned int field_150;
    char padding_154[180];
    unsigned int field_208;
    char padding_20c[44];
    struct struct_10 *field_238;
    char padding_240[60];
    unsigned int field_27c;
    char padding_280[4];
    unsigned int field_284;
    unsigned int field_288;
    unsigned int field_28c;
} struct_11;

typedef struct struct_13 {
    char padding_0[568];
    struct struct_14 *field_238;
} struct_13;

typedef struct struct_9 {
    char padding_0[40];
    struct struct_10 *field_28;
} struct_9;

typedef struct struct_10 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[4];
    unsigned long long field_18;
    struct struct_11 *field_20;
} struct_10;

typedef struct struct_12 {
    char padding_0[568];
    struct struct_10 *field_238;
} struct_12;

typedef struct struct_14 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[4];
    unsigned long long field_18;
    struct struct_15 *field_20;
} struct_14;

typedef struct struct_15 {
    char padding_0[40];
    struct struct_14 *field_28;
    struct struct_14 *field_30;
    char padding_38[16];
    struct struct_13 *field_48;
    char padding_50[64];
    struct struct_14 *field_90;
    char padding_98[40];
    unsigned long long field_c0;
    char padding_c8[4];
    unsigned int field_cc;
    char padding_d0[12];
    unsigned int field_dc;
    char padding_e0[16];
    unsigned int field_f0;
    char padding_f4[12];
    unsigned long long field_100;
    char padding_108[12];
    char field_114;
    char padding_115[3];
    struct struct_14 *field_118;
    struct struct_16 *field_120;
    unsigned int field_128;
    char field_12c;
    char padding_12d[23];
    unsigned int field_144;
    unsigned int field_148;
    unsigned int field_14c;
    unsigned int field_150;
    char padding_154[180];
    unsigned int field_208;
    char padding_20c[44];
    struct struct_14 *field_238;
    char padding_240[60];
    unsigned int field_27c;
    char padding_280[4];
    unsigned int field_284;
    unsigned int field_288;
    unsigned int field_28c;
} struct_15;

typedef struct struct_16 {
    char padding_0[40];
    struct struct_14 *field_28;
} struct_16;

typedef struct struct_1 {
    char padding_0[224];
    unsigned int field_e0;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1eef458;
extern struct_1 *g_1ef0c58;
extern long long g_1ef2440;
extern long long g_1ef8aa0;
extern long long g_1efd038;
extern long long g_1f08040;
extern char g_1fab404;

unsigned int AI_SpawnNPC_d__127_MoveNext(struct_3 *p)
{
    struct_3 *v0;  // x0
    struct_3 *v1;  // x0
    struct_3 *ptr5;  // x20
    unsigned long v12;  // x1
    struct_3 *v13;  // x1
    unsigned long ptr4;  // x20
    unsigned int v15;  // s0
    unsigned int v16;  // s3
    unsigned int v17;  // s2
    long long v19;  // x0
    struct_3 *v2;  // x0
    struct_3 *v20;  // x1
    unsigned int v21;  // s0
    unsigned int v22;  // s1
    unsigned long v23;  // x0
    unsigned int flag;  // w8
    struct_11 *ptr;  // x19
    long long v5;  // x19
    struct_3 *v6;  // x0
    struct_11 *ptr3;  // x21
    unsigned long addr;  // x21
    unsigned int v9;  // s0

    v0 = p;
    if (!(g_1fab404 & 1))
    {
        sub_f7d92c(&g_1efd038);
        sub_f7d92c(&g_1eef458);
        sub_f7d92c(&g_1ef8aa0);
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c(&g_1ef2440);
        v1 = sub_f7d92c(&g_1f08040);
        g_1fab404 = 1;
        v0 = v1;
    }
    flag = p->field_10;
    ptr = p->field_20;
    if (flag != 2)
    {
        if (flag != 1)
        {
            if (!flag)
            {
                p->field_10 = 4294967295;
                v5 = sub_f7db70(g_1ef2440);
                WaitForSeconds__ctor(v5, 0);
                p->field_18 = v5;
                sub_f7d8d0(&p->field_18, v5);
                p->field_10 = 1;
                return 1;
            }
            return 0;
        }
        p->field_10 = 4294967295;
        if (ptr)
        {
            v6 = sub_1231bc8(ptr, g_1efd038);
            ptr3 = ptr;
            ptr3->field_90 = v6;
            addr = &ptr3->field_90;
            sub_f7d8d0(addr, v6);
            v2 = *((long long *)addr);
            if (v2 && (Behaviour__set_enabled(v2, 0, 0), v2 = (struct_3 *)*((long long *)addr), v2 && (Behaviour__set_enabled(v2, 1, 0), v2 = (struct_3 *)*((long long *)addr), v2 && (NavMeshAgent__set_speed(v2, 0), v2 = (struct_3 *)ptr->field_90, v2 && (v9 = 0x42700000, NavMeshAgent__set_acceleration(v2, 0), v2 = (struct_3 *)*((long long *)addr), v2)))))
            {
                if (!((char)NavMeshAgent__get_isOnNavMesh(v2, 0) & 1))
                {
                    p->field_18 = 0;
                    ptr5 = &p->field_18;
                    sub_f7d8d0(ptr5, 0);
                    *((unsigned int *)&ptr5->padding_0[8]) = 2;
                    return 1;
                }
LABEL_1081934:
                v2 = ptr->field_90;
                if (v2)
                {
                    if (!((char)NavMeshAgent__get_isOnNavMesh(v2, 0) & 1))
                    {
                        if (!g_1eef458->field_e0)
                            sub_f7da5c(g_1eef458);
                        Debug__Log(g_1f08040, 0);
                        return 0;
                    }
                    Time__get_time(0);
                    ptr->field_150 = v9;
                    MonoBehaviour__StartCoroutine(ptr, AI__PlayFootSteps(ptr), 0);
                    if (!g_1ef0c58->field_e0)
                        sub_f7da5c(g_1ef0c58);
                    v12 = ptr->field_100;
                    if (((char)Object__op_Inequality(ptr->field_c0, ptr->field_100, 0) & 1))
                    {
                        v12 = AI__UpdateModelYaw(ptr);
                        MonoBehaviour__StartCoroutine(ptr, v12, 0);
                    }
                    if (ptr->field_114)
                    {
                        v13 = ptr->field_30;
                        ptr4 = &ptr->field_238;
                        ptr->field_f0 = 2;
                        ptr->field_238 = v13;
                        v2 = sub_f7d8d0(ptr4, v13);
                        if (ptr->field_48)
                        {
                            v2 = ptr->field_48->field_238;
                            if (v2)
                            {
                                CapsuleCollider__get_height(v2, 0);
                                v2 = ptr->field_238;
                                v15 = v9 * 0x3e800000;
                                ptr->field_27c = v15;
                                if (v2)
                                {
                                    Transform__get_position(v2, 0);
                                    v2 = *((long long *)ptr4);
                                    if (v2)
                                    {
                                        Transform__get_up(v2, 0);
                                        v16 = ptr->field_27c;
                                        ptr->field_208 = 0x45000000;
                                        ptr->field_284 = v15 + v15 * v16;
                                        ptr->field_288 = 0x3e800000 + 0x3e800000 * v16;
                                        ptr->field_28c = v17 + v17 * v16;
                                        MonoBehaviour__StartCoroutine(ptr, AI__AttackTarget(ptr), 0);
                                        v2 = ptr->field_28;
                                        ptr->field_dc = ptr->field_cc;
                                        if (v2)
                                        {
                                            v2 = GameObject__get_transform(v2, 0);
                                            if (v2)
                                            {
                                                Transform__get_position();
                                                AI__TravelToPoint(ptr, 0);
                                                return 0;
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                    else if (!ptr->field_12c)
                    {
                        if (!g_1ef0c58->field_e0)
                            sub_f7da5c(g_1ef0c58);
                        v12 = 0;
                        v2 = Object__op_Implicit(ptr->field_120, 0);
                        if (!(v2 & 1))
                            goto LABEL_1081be8;
                        if (ptr->field_120 && (v2 = (struct_3 *)ptr->field_120->field_28, v2))
                        {
                            v19 = sub_14a30c0(v2, ptr->field_128 - 1, g_1ef8aa0);
                            if (!g_1ef0c58->field_e0)
                                sub_f7da5c(g_1ef0c58);
                            v12 = 0;
                            v2 = Object__op_Implicit(v19, 0);
                            if (!(v2 & 1))
                                goto LABEL_1081be8;
                            if (ptr->field_120)
                            {
                                v2 = ptr->field_120->field_28;
                                if (v2)
                                {
                                    v20 = sub_14a30c0(v2, ptr->field_128 - 1, g_1ef8aa0);
                                    ptr->field_118 = v20;
                                    sub_f7d8d0(&ptr->field_118, v20);
                                    v21 = ptr->field_cc;
                                    v2 = ptr->field_118;
                                    ptr->field_dc = v21;
                                    if (v2)
                                    {
                                        Transform__get_position(v2, 0);
                                        v2 = ptr->field_118;
                                        ptr->field_144 = v21;
                                        ptr->field_148 = v22;
                                        ptr->field_14c = v17;
                                        if (v2)
                                        {
                                            Transform__get_position(v2, 0);
                                            AI__TravelToPoint(ptr, 0);
                                            MonoBehaviour__StartCoroutine(ptr, AI__Patrol(ptr), 0);
                                            return 0;
                                        }
                                    }
                                }
                            }
                        }
                    }
                    else
                    {
LABEL_1081be8:
                        AI__TravelToPoint(ptr, v12);
                        v23 = AI__StandWatch(ptr);
                        MonoBehaviour__StartCoroutine(ptr, v23, 0);
                        return 0;
                    }
                }
            }
        }
    }
    else
    {
        p->field_10 = 4294967295;
        if (ptr)
            goto LABEL_1081934;
    }
    sub_f7db74(v2);
}
```


## `AI.<SpawnNPC>d__127.get_Current` — RVA `0xc81c34`

- Decompiled symbol: `AI_SpawnNPC_d__127_get_Current`
- Metadata signature: `private object System.Collections.Generic.IEnumerator<System.Object>.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long AI_SpawnNPC_d__127_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```


## `AI.<SpawnNPC>d__127.Reset` — RVA `0xc81c3c`

- Decompiled symbol: `AI_SpawnNPC_d__127_Reset`
- Metadata signature: `private void System.Collections.IEnumerator.Reset() { }`
- Native interval: `56` bytes
- Result: `pseudocode`

```c
extern long long g_1ef0bd8;
extern long long g_1f03f60;

void AI_SpawnNPC_d__127_Reset(void)
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
    sub_f7da4c(v4, sub_f7d940(&g_1f03f60));
}
```


## `AI.<SpawnNPC>d__127.get_Current` — RVA `0xc81c74`

- Decompiled symbol: `AI_SpawnNPC_d__127_get_Current`
- Metadata signature: `private object System.Collections.IEnumerator.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long AI_SpawnNPC_d__127_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```


## `AI.<StandWatch>d__130.Dispose` — RVA `0xc81c7c`

- Decompiled symbol: `AI_StandWatch_d__130_Dispose`
- Metadata signature: `private void System.IDisposable.Dispose() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long AI_StandWatch_d__130_Dispose(void)
{
    unsigned long v0;  // x0

    return v0;
}
```


## `AI.<StandWatch>d__130.MoveNext` — RVA `0xc81c80`

- Decompiled symbol: `AI_StandWatch_d__130_MoveNext`
- Metadata signature: `private bool MoveNext() { }`
- Native interval: `1656` bytes
- Result: `pseudocode`

```c
typedef struct struct_3 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[4];
    long long field_18;
    void* field_20;
} struct_3;

typedef struct struct_2 {
    char padding_0[568];
    long long field_238;
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
extern long long g_1ef2440;
extern long long g_1f08598;
extern char g_1fab3e0;
extern char g_1fab405;

unsigned int AI_StandWatch_d__130_MoveNext(struct_3 *p)
{
    unsigned int flag;  // w8
    void* ptr;  // x20
    unsigned long i;  // x24
    unsigned int v11;  // w8
    unsigned int v12;  // s8
    unsigned long v13;  // 4125
    unsigned int v14;  // s2
    unsigned int v15;  // s0
    unsigned long v16;  // 4205
    unsigned long long v17;  // x8
    unsigned int v18;  // w8
    unsigned int v19;  // s2
    unsigned int v20;  // s0
    unsigned long v21;  // 4205
    unsigned int v22;  // s1
    unsigned long v23;  // 4218
    unsigned int v24;  // s0
    unsigned int v25;  // s8
    unsigned long v26;  // 4138
    long long v27;  // x0
    unsigned int v28;  // s0
    unsigned int v29;  // s8
    long long v3;  // x0
    unsigned long v30;  // 4125
    struct_3 *ptr3;  // x19
    unsigned int v32;  // w8
    long long v33;  // x20
    long long v34;  // x0
    struct_3 *ptr4;  // x19
    unsigned int v4;  // s3
    unsigned int v5;  // s0
    unsigned long v6;  // 4163
    unsigned int v7;  // s0
    long long v8;  // x0
    void* addr;  // x23

    if (!(g_1fab405 & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c(&g_1ef0e48);
        sub_f7d92c(&g_1ef2440);
        sub_f7d92c(&g_1f08598);
        g_1fab405 = 1;
    }
    flag = p->field_10;
    ptr = p->field_20;
    if (flag - 2 >= 2)
    {
        if (flag != 1)
        {
            if (flag)
                return 0;
            goto LABEL_1081d08;
        }
        p->field_10 = 4294967295;
        if (ptr)
            goto LABEL_1081ebc;
    }
    else
    {
LABEL_1081d08:
        p->field_10 = 4294967295;
        if (ptr)
        {
            if ((char)ptr[276])
            {
                MonoBehaviour__StartCoroutine(ptr, AI__SpawnNPC(ptr), 0);
                return 0;
            }
            Time__get_time(0);
            v3 = (long long)ptr[40];
            v4 = (int)ptr[248] + 0x40c00000;
            v6 = arm64g_calculate_condition(192, (((((unsigned long long)(char)(CmpF(v4, v5)) >> 5 & 3 | (unsigned long long)(CmpF(v4, v5) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v4, v5)) >> 5 & 3 | (unsigned long long)(CmpF(v4, v5) & 1)) & ((unsigned long long)(char)(CmpF(v4, v5)) >> 5 & 3 | (unsigned long long)(CmpF(v4, v5) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
            if ((char)v6)
                v7 = (int)ptr[520] * 0x40c00000;
            else
                v7 = (int)ptr[520];
            *((unsigned int *)&ptr[536]) = v7;
            if (v3)
            {
                if (!(((char)GameObject__get_activeInHierarchy(v3, 0) & 1) && !(char)ptr[160]))
                {
LABEL_1081e30:
                    AI__CanSeeTarget(ptr);
                    if (!g_1ef0c58->field_e0)
                        sub_f7da5c(g_1ef0c58);
                    if (((char)Object__op_Implicit((long long)ptr[568], 0) & 1) && (char)ptr[576] || (char)ptr[660] || (char)ptr[661])
                    {
                        v34 = MonoBehaviour__StartCoroutine(ptr, AI__AttackTarget(ptr), 0);
                        p->field_18 = v34;
                        ptr4 = &p->field_18;
                        sub_f7d8d0(ptr4, v34);
                        *((unsigned int *)&ptr4->padding_0[8]) = 1;
                        return 1;
                    }
                    if (!g_1ef0c58->field_e0)
                        sub_f7da5c(g_1ef0c58);
                    if (!((char)Object__op_Implicit((long long)ptr[128], 0) & 1))
                    {
LABEL_1081ebc:
                        v12 = (int)ptr[600];
                        Time__get_time(0);
                        v13 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v12, v7)) >> 5 & 3 | (unsigned long long)(CmpF(v12, v7) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v12, v7)) >> 5 & 3 | (unsigned long long)(CmpF(v12, v7) & 1)) & ((unsigned long long)(char)(CmpF(v12, v7)) >> 5 & 3 | (unsigned long long)(CmpF(v12, v7) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                        if (!((char)v13))
                        {
                            if (!(char)ptr[301] || (char)ptr[304])
                            {
                                if ((long long)ptr[0x100])
                                {
                                    Transform__get_position((long long)ptr[0x100], 0);
                                    if (!g_1fab3e0)
                                    {
                                        sub_f7d92c("_F");
                                        g_1fab3e0 = 1;
                                    }
                                    if (!g_1ef07e8->field_e0)
                                        sub_f7da5c(g_1ef07e8);
                                    v14 = (int)ptr[320];
                                    v15 = [D] unsupported_Iop_SqrtF32();
                                    v16 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v15, v14)) >> 5 & 3 | (unsigned long long)(CmpF(v15, v14) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v15, v14)) >> 5 & 3 | (unsigned long long)(CmpF(v15, v14) & 1)) & ((unsigned long long)(char)(CmpF(v15, v14)) >> 5 & 3 | (unsigned long long)(CmpF(v15, v14) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                                    if (!((char)v16))
                                    {
                                        if (!(char)ptr[304])
                                            v17 = 208;
                                        else
                                            v17 = 204;
                                        v18 = (char)ptr[306];
                                        *((int *)&ptr[220]) = *((int *)((char *)ptr + v17));
                                        if (v18 || (char)ptr[307])
                                            *((char *)&ptr[306]) = 0;
                                        else
                                            *((unsigned short *)&ptr[306]) = 257;
                                        goto LABEL_1081fac;
                                    }
                                    if ((char)ptr[301])
                                        goto LABEL_1081fc0;
                                    goto LABEL_1082138;
                                }
                            }
                            else
                            {
LABEL_1081fc0:
                                if (!(char)ptr[304])
                                {
                                    if ((long long)ptr[40] && GameObject__get_transform((long long)ptr[40], 0) && (Transform__get_position(), (long long)ptr[0x100]))
                                    {
                                        Transform__get_position((long long)ptr[0x100], 0);
                                        if (!g_1fab3e0)
                                        {
                                            sub_f7d92c("_F");
                                            g_1fab3e0 = 1;
                                        }
                                        if (!g_1ef07e8->field_e0)
                                            sub_f7da5c(g_1ef07e8);
                                        v19 = (int)ptr[320];
                                        v20 = [D] unsupported_Iop_SqrtF32();
                                        v21 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v20, v19)) >> 5 & 3 | (unsigned long long)(CmpF(v20, v19) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v20, v19)) >> 5 & 3 | (unsigned long long)(CmpF(v20, v19) & 1)) & ((unsigned long long)(char)(CmpF(v20, v19)) >> 5 & 3 | (unsigned long long)(CmpF(v20, v19) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                                        if ((char)v21)
                                            goto LABEL_1082138;
                                        if ((char)ptr[301])
                                        {
                                            if ((long long)ptr[40] && GameObject__get_transform((long long)ptr[40], 0) && (Transform__get_position(), (long long)ptr[0x100]))
                                            {
                                                Transform__get_position((long long)ptr[0x100], 0);
                                                if (!g_1fab3e0)
                                                {
                                                    sub_f7d92c("_F");
                                                    g_1fab3e0 = 1;
                                                }
                                                if (!g_1ef07e8->field_e0)
                                                    sub_f7da5c(g_1ef07e8);
                                                v20 = [D] unsupported_Iop_SqrtF32();
                                                v22 = (int)ptr[320] * 2;
                                                v23 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v20, v22)) >> 5 & 3 | (unsigned long long)(CmpF(v20, v22) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v20, v22)) >> 5 & 3 | (unsigned long long)(CmpF(v20, v22) & 1)) & ((unsigned long long)(char)(CmpF(v20, v22)) >> 5 & 3 | (unsigned long long)(CmpF(v20, v22) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                                                if (!((char)v23))
                                                {
                                                    v24 = (int)ptr[204];
                                                    *((unsigned int *)&ptr[220]) = v24;
                                                    Time__get_time(0);
                                                    *((unsigned int *)&ptr[224]) = v24;
                                                    goto LABEL_10822a4;
                                                }
                                            }
                                        }
                                        else
                                        {
                                            v25 = (int)ptr[224];
                                            Time__get_time(0);
                                            v26 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v25 + 0x40000000, v20)) >> 5 & 3 | (unsigned long long)(CmpF(v25 + 0x40000000, v20) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v25 + 0x40000000, v20)) >> 5 & 3 | (unsigned long long)(CmpF(v25 + 0x40000000, v20) & 1)) & ((unsigned long long)(char)(CmpF(v25 + 0x40000000, v20)) >> 5 & 3 | (unsigned long long)(CmpF(v25 + 0x40000000, v20) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                                            if (!((char)v26))
                                                *((int *)&ptr[220]) = (int)ptr[208];
LABEL_10822a4:
                                            if ((char)ptr[306] || (char)ptr[307])
                                                *((char *)&ptr[306]) = 0;
                                            else
                                                *((unsigned short *)&ptr[306]) = 257;
                                            if ((long long)ptr[40] && GameObject__get_transform((long long)ptr[40], 0))
                                            {
                                                Transform__get_position();
LABEL_1081fac:
                                                AI__TravelToPoint(ptr, 0);
                                                goto LABEL_1082198;
                                            }
                                        }
                                    }
                                }
                                else
                                {
LABEL_1082138:
                                    v27 = (long long)ptr[144];
                                    *((unsigned int *)&ptr[220]) = 0;
                                    if (v27)
                                    {
                                        NavMeshAgent__set_isStopped(v27, 1, 0);
                                        v28 = (int)ptr[220];
                                        AI__SetSpeed(ptr, 1, 0);
                                        if (!(char)ptr[604] || !((v29 = (unsigned int)(int)ptr[600], Time__get_time(0), v30 = (unsigned long)arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v29, v28)) >> 5 & 3 | (unsigned long long)(CmpF(v29, v28) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v29, v28)) >> 5 & 3 | (unsigned long long)(CmpF(v29, v28) & 1)) & ((unsigned long long)(char)(CmpF(v29, v28)) >> 5 & 3 | (unsigned long long)(CmpF(v29, v28) & 1)) >> 1 & 1)) * 0x10000000, 0, 0), !((char)v30))))
                                            goto LABEL_1082198;
                                        if ((long long)ptr[176])
                                        {
                                            Animator__SetInteger((long long)ptr[176], g_1f08598, 0, 0);
                                            goto LABEL_1082198;
                                        }
                                    }
                                }
                            }
                        }
                        else
                        {
LABEL_1082198:
                            if ((char)ptr[306])
                            {
                                p->field_18 = 0;
                                ptr3 = &p->field_18;
                                sub_f7d8d0(ptr3, 0);
                                v32 = 2;
                            }
                            else
                            {
                                v33 = sub_f7db70(g_1ef2440);
                                WaitForSeconds__ctor(v33, 0);
                                p->field_18 = v33;
                                ptr3 = &p->field_18;
                                sub_f7d8d0(ptr3, v33);
                                v32 = 3;
                            }
                            *((unsigned int *)&ptr3->padding_0[8]) = v32;
                            return 1;
                        }
                    }
                    else
                    {
                        if ((long long)ptr[0x100] && (Component__get_gameObject((long long)ptr[0x100], 0), (long long)ptr[0x100] && (Transform__get_position((long long)ptr[0x100], 0), (long long)ptr[128])))
                        {
                            NPCRegistry__FindClosestTarget((long long)ptr[128], 0, ptr, (int)ptr[240]);
                            goto LABEL_1081ebc;
                        }
                    }
                }
                else if ((long long)ptr[72])
                {
                    if (!g_1ef0c58->field_e0)
                        sub_f7da5c(g_1ef0c58);
                    v8 = Object__op_Implicit(*((long long *)((long long)ptr[72] + 568)), 0);
                    if (!(v8 & 1))
                        goto LABEL_1081e30;
                    addr = (long long)ptr[152];
                    if (addr)
                    {
                        if ((int)(long long)addr[24] >= 1)
                        {
                            i = 0;
                            v11 = (long long)addr[24];
                            do
                            {
                                if (v11 <= i)
                                    sub_f7db7c(v8);
                                if (!(long long)ptr[72])
                                {
                                    sub_f7db74();
                                    sub_f7db7c(v8);
                                }
                                if (!g_1ef0e48->field_e0)
                                    sub_f7da5c(g_1ef0e48);
                                v8 = Physics__IgnoreCollision(*((long long *)(32 + (char *)addr + 8 * i)), *((long long *)((long long)ptr[72] + 568)), 1, 0);
                                v11 = (int)addr[24];
                                i += 1;
                            } while (i < v11);
                        }
                        *((char *)&ptr[160]) = 1;
                        goto LABEL_1081e30;
                    }
                }
            }
        }
    }
    v8 = sub_f7db74();
    sub_f7db7c(v8);
}
```


## `AI.<StandWatch>d__130.get_Current` — RVA `0xc822f8`

- Decompiled symbol: `AI_StandWatch_d__130_get_Current`
- Metadata signature: `private object System.Collections.Generic.IEnumerator<System.Object>.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long AI_StandWatch_d__130_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```


## `AI.<StandWatch>d__130.Reset` — RVA `0xc82300`

- Decompiled symbol: `AI_StandWatch_d__130_Reset`
- Metadata signature: `private void System.Collections.IEnumerator.Reset() { }`
- Native interval: `56` bytes
- Result: `pseudocode`

```c
extern long long g_1ef0bd8;
extern long long g_1f03f68;

void AI_StandWatch_d__130_Reset(void)
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
    sub_f7da4c(v4, sub_f7d940(&g_1f03f68));
}
```


## `AI.<StandWatch>d__130.get_Current` — RVA `0xc82338`

- Decompiled symbol: `AI_StandWatch_d__130_get_Current`
- Metadata signature: `private object System.Collections.IEnumerator.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long AI_StandWatch_d__130_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```


## `AI.<UpdateModelYaw>d__137.Dispose` — RVA `0xc82340`

- Decompiled symbol: `AI_UpdateModelYaw_d__137_Dispose`
- Metadata signature: `private void System.IDisposable.Dispose() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long AI_UpdateModelYaw_d__137_Dispose(void)
{
    unsigned long v0;  // x0

    return v0;
}
```


## `AI.<UpdateModelYaw>d__137.MoveNext` — RVA `0xc82344`

- Decompiled symbol: `AI_UpdateModelYaw_d__137_MoveNext`
- Metadata signature: `private bool MoveNext() { }`
- Native interval: `256` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: Decompiler produced no C-like text

```c
// 0x1082344: stp d9, d8, [sp, #-0x40]!
// 0x1082348: str x30, [sp, #0x10]
// 0x108234c: stp x22, x21, [sp, #0x20]
// 0x1082350: stp x20, x19, [sp, #0x30]
// 0x1082354: ldr w21, [x0, #0x10]
// 0x1082358: cmp w21, #1
// 0x108235c: b.hi #0x1082424
// 0x1082360: ldr x22, [x0, #0x20]
// 0x1082364: mov x19, x0
// 0x1082368: mov w8, #-1
// 0x108236c: str w8, [x0, #0x10]
// 0x1082370: cbz x22, #0x1082440
// 0x1082374: ldr s0, [x22, #0x1fc]
// 0x1082378: mov w8, #0xe4
// 0x108237c: mov w9, #0xe8
// 0x1082380: ldr s8, [x22, #0xec]
// 0x1082384: fcmp s0, #0.0
// 0x1082388: csel x8, x9, x8, gt
// 0x108238c: ldr s9, [x22, x8]
// 0x1082390: mov x0, xzr
// 0x1082394: bl #0x1b89b60
// 0x1082398: mov w8, #0x43340000
// 0x108239c: fsub s1, s9, s8
// 0x10823a0: fmov s3, w8
// 0x10823a4: ldr x0, [x22, #0xc0]
// 0x10823a8: fmul s4, s0, s3
// 0x10823ac: fnmul s0, s0, s3
// 0x10823b0: fcmp s1, #0.0
// 0x10823b4: fabd s2, s9, s8
// 0x10823b8: fcsel s0, s4, s0, ge
// 0x10823bc: fadd s0, s8, s0
// 0x10823c0: fcmp s2, s4
// 0x10823c4: fcsel s0, s0, s9, hi
// 0x10823c8: str s0, [x22, #0xec]
// 0x10823cc: cbz x0, #0x1082440
// 0x10823d0: mov x1, xzr
// 0x10823d4: bl #0x1b92154
// 0x10823d8: adrp x8, #0x832000
// 0x10823dc: ldr s0, [x22, #0xec]
// 0x10823e0: ldr s1, [x8, #0x3e4]
// 0x10823e4: mov x20, x0
// 0x10823e8: fmov s2, wzr
// 0x10823ec: mov x0, xzr
// 0x10823f0: fmul s1, s0, s1
// 0x10823f4: fmov s0, wzr
// 0x10823f8: bl #0x1b8b12c
// 0x10823fc: cbz x20, #0x1082440
// 0x1082400: mov x0, x20
// 0x1082404: mov x1, xzr
// 0x1082408: bl #0x1b9d874
// 0x108240c: str xzr, [x19, #0x18]!
// 0x1082410: mov x0, x19
// 0x1082414: mov x1, xzr
// 0x1082418: bl #0xf7d8d0
// 0x108241c: mov w8, #1
// 0x1082420: stur w8, [x19, #-8]
// 0x1082424: cmp w21, #2
// 0x1082428: ldp x20, x19, [sp, #0x30]
// 0x108242c: ldp x22, x21, [sp, #0x20]
// 0x1082430: ldr x30, [sp, #0x10]
// 0x1082434: cset w0, lo
// 0x1082438: ldp d9, d8, [sp], #0x40
// 0x108243c: ret
// 0x1082440: bl #0xf7db74
```


## `AI.<UpdateModelYaw>d__137.get_Current` — RVA `0xc82444`

- Decompiled symbol: `AI_UpdateModelYaw_d__137_get_Current`
- Metadata signature: `private object System.Collections.Generic.IEnumerator<System.Object>.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long AI_UpdateModelYaw_d__137_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```


## `AI.<UpdateModelYaw>d__137.Reset` — RVA `0xc8244c`

- Decompiled symbol: `AI_UpdateModelYaw_d__137_Reset`
- Metadata signature: `private void System.Collections.IEnumerator.Reset() { }`
- Native interval: `56` bytes
- Result: `pseudocode`

```c
extern long long g_1ef0bd8;
extern long long g_1f03f70;

void AI_UpdateModelYaw_d__137_Reset(void)
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
    sub_f7da4c(v4, sub_f7d940(&g_1f03f70));
}
```


## `AI.<UpdateModelYaw>d__137.get_Current` — RVA `0xc82484`

- Decompiled symbol: `AI_UpdateModelYaw_d__137_get_Current`
- Metadata signature: `private object System.Collections.IEnumerator.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long AI_UpdateModelYaw_d__137_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```
