# Native pseudocode: NPCRegistry

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `NPCRegistry.FindClosestTarget` — RVA `0xc80adc`

- Decompiled symbol: `NPCRegistry_FindClosestTarget`
- Metadata signature: `public void FindClosestTarget(GameObject NPC, AI NpcAIcomponent, Vector3 myPos, float distance, int myFaction) { }`
- Native interval: `1156` bytes
- Result: `pseudocode`
- Heuristic layout hint: `NPCRegistry_Recovered` matched 7 offsets against `NPCRegistry` metadata (confidence 1.00).

```c
typedef struct NPCRegistry_Recovered {
    char padding_0[32];
    struct struct_2 *FPSWalker;
    struct struct_1 *Npcs;
    char padding_30[8];
    struct struct_1 *playerTransform;
    unsigned int nearestNpcDist;
    unsigned int NpcDist;
    unsigned int playerDist;
    unsigned int playerDistMod;
} NPCRegistry_Recovered;

typedef struct struct_11 {
    char padding_0[224];
    unsigned int field_e0;
    char padding_e4[12];
    unsigned int field_f0;
    char padding_f4[12];
    struct struct_11 *field_100;
} struct_11;

typedef struct struct_8 {
    char padding_0[136];
    struct struct_6 *field_88;
    char padding_90[132];
    char field_114;
    char padding_115[263];
    unsigned int field_21c;
    char padding_220[24];
    struct struct_7 *field_238;
    char padding_240[60];
    unsigned int field_27c;
    char padding_280[4];
    unsigned int field_284;
    unsigned int field_288;
    unsigned int field_28c;
    char padding_290[4];
    char field_294;
} struct_8;

typedef struct struct_2 {
    char padding_0[568];
    struct struct_1 *field_238;
    char padding_240[144];
    char field_2d0;
    char padding_2d1[11];
    char field_2dc;
} struct_2;

typedef struct struct_10 {
    char padding_0[256];
    struct struct_9 *field_100;
    char padding_108[292];
    unsigned int field_22c;
} struct_10;

typedef struct struct_6 {
    char padding_0[256];
    struct struct_5 *field_100;
    char padding_108[292];
    unsigned int field_22c;
} struct_6;

typedef struct struct_1 {
    char padding_0[224];
    unsigned int field_e0;
    char padding_e4[12];
    unsigned int field_f0;
    char padding_f4[12];
    struct struct_1 *field_100;
} struct_1;

typedef struct struct_7 {
    char padding_0[224];
    unsigned int field_e0;
    char padding_e4[12];
    unsigned int field_f0;
    char padding_f4[12];
    struct struct_7 *field_100;
} struct_7;

typedef struct struct_9 {
    char padding_0[224];
    unsigned int field_e0;
    char padding_e4[12];
    unsigned int field_f0;
    char padding_f4[12];
    struct struct_9 *field_100;
} struct_9;

typedef struct struct_5 {
    char padding_0[224];
    unsigned int field_e0;
    char padding_e4[12];
    unsigned int field_f0;
    char padding_f4[12];
    struct struct_5 *field_100;
} struct_5;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern long long g_1ef7628;
extern long long g_1ef7630;
extern char g_1fab3e0;
extern char g_1fab423;

long long NPCRegistry_FindClosestTarget(struct_3 *ptr, unsigned long a1, struct_8 *p, unsigned int flag)
{
    uint128_t v2;  // q3
    uint128_t v3;  // q8
    uint128_t v11;  // q0
    struct_10 *addr;  // x22
    int v13;  // w24
    unsigned int v14;  // s2
    unsigned int v30;  // s1
    struct_11 *cur;  // x0
    unsigned int v16;  // s2
    unsigned int v17;  // s2
    unsigned long v18;  // 4244
    unsigned long v19;  // 4129
    long long v20;  // x0
    unsigned long v21;  // 4133
    unsigned long v22;  // 4129
    struct_11 *v23;  // x1
    long long v24;  // x0
    long long v25;  // x0
    unsigned int v4;  // s2
    unsigned int v26;  // s0
    unsigned long v27;  // x1
    long long v28;  // x0
    unsigned int v29;  // s3
    uint128_t v6;  // q0
    struct_2 *v7;  // x8
    unsigned int v8;  // s0
    char *v0;  // [bp-0x60]
    char v1;  // [bp+0x0]

    v0 = &v1;
    v3 = v2;
    if (!(g_1fab423 & 1))
    {
        sub_f7d92c(&g_1ef7628);
        sub_f7d92c(&g_1ef7630);
        sub_f7d92c(&g_1ef0c58);
        g_1fab423 = 1;
    }
    cur = ptr->field_38;
    ptr->field_40 = v3;
    if (cur)
    {
        Transform__get_position(cur, 0);
        if (!g_1fab3e0)
        {
            sub_f7d92c("_F");
            g_1fab3e0 = 1;
        }
        cur = g_1ef07e8;
        if (!g_1ef07e8->field_e0)
            cur = sub_f7da5c(g_1ef07e8);
        v30 = (v4 - v4) * (v4 - v4);
        ptr->field_48 = [D] unsupported_Iop_SqrtF32();
        if (p)
        {
            v6 = v3;
            if (!p->field_294)
            {
                v7 = ptr->field_20;
                if (!v7)
                    sub_f7db74(cur);
                if (v7->field_2d0)
                {
                    v8 = p->field_21c;
                }
                else
                {
                    v6 = v3;
                    if (!v7->field_2dc)
                        goto LABEL_1080c1c;
                    v30 = 0x3f400000;
                    v8 = p->field_21c * 0x3f400000;
                }
                v6 = v8 * (unsigned int)v3;
            }
LABEL_1080c1c:
            v11 = v6;
            cur = ptr->field_28;
            ptr->field_4c = v11;
            if (cur)
            {
                addr = NULL;
                v13 = 0;
                v14 = v4;
                do
                {
                    v16 = v14;
                    if (*((int *)&cur->padding_0[24]) <= v13)
                    {
                        if (flag != 1 && !((v11 = (uint128_t)ptr->field_48, v30 = ptr->field_4c, v21 = (unsigned long)arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF((unsigned int)v11, v30)) >> 5 & 3 | (unsigned long long)(CmpF((unsigned int)v11, v30) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF((unsigned int)v11, v30)) >> 5 & 3 | (unsigned long long)(CmpF((unsigned int)v11, v30) & 1)) & ((unsigned long long)(char)(CmpF((unsigned int)v11, v30)) >> 5 & 3 | (unsigned long long)(CmpF((unsigned int)v11, v30) & 1)) >> 1 & 1)) * 0x10000000, 0, 0), (char)v21 || (v30 = ptr->field_40, v22 = (unsigned long)arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF((unsigned int)v11, v30)) >> 5 & 3 | (unsigned long long)(CmpF((unsigned int)v11, v30) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF((unsigned int)v11, v30)) >> 5 & 3 | (unsigned long long)(CmpF((unsigned int)v11, v30) & 1)) & ((unsigned long long)(char)(CmpF((unsigned int)v11, v30)) >> 5 & 3 | (unsigned long long)(CmpF((unsigned int)v11, v30) & 1)) >> 1 & 1)) * 0x10000000, 0, 0), !((char)v22)))) || p->field_114)
                        {
                            v23 = ptr->field_38;
                            p->field_238 = v23;
                            cur = sub_f7d8d0(&p->field_238, v23);
                            if (ptr->field_20)
                            {
                                cur = ptr->field_20->field_238;
                                if (cur)
                                {
                                    CapsuleCollider__get_height(cur, 0);
                                    p->field_88 = NULL;
                                    p->field_27c = (unsigned int)v11 * 0x3e800000;
                                    v24 = sub_f7d8d0();
                                    return sub_f7d8d0();
                                }
                                break;
                            }
                        }
                        else
                        {
                            if (!g_1ef0c58->field_e0)
                                sub_f7da5c(g_1ef0c58);
                            v25 = Object__op_Implicit(addr, 0);
                            if (!((char)v25 & 1))
                                return v25;
                            p->field_88 = addr;
                            cur = sub_f7d8d0(&p->field_88, addr);
                            if (addr)
                            {
                                v26 = addr->field_22c;
                                p->field_27c = v26;
                                v27 = addr->field_100;
                                p->field_238 = v27;
                                sub_f7d8d0(&p->field_238, v27);
                                cur = addr->field_100;
                                if (cur)
                                {
                                    Transform__get_position(cur, 0);
                                    cur = addr->field_100;
                                    if (cur)
                                    {
                                        v28 = Transform__get_up(cur, 0);
                                        v29 = addr->field_22c;
                                        p->field_284 = v26 + v26 * v29;
                                        p->field_288 = v30 + v30 * v29;
                                        p->field_28c = v16 + v16 * v29;
                                        return v28;
                                    }
                                    break;
                                }
                            }
                        }
                    }
                    cur = sub_14a30c0();
                    if (!cur || !((cur = (struct_11 *)cur->field_100, cur)))
                        break;
                    Transform__get_position(cur, 0);
                    if (!g_1fab3e0)
                    {
                        sub_f7d92c("_F");
                        g_1fab3e0 = 1;
                    }
                    if (!g_1ef07e8->field_e0)
                        sub_f7da5c(g_1ef07e8);
                    v17 = v4 - v16;
                    v30 = v17 * v17;
                    v11 = [D] unsupported_Iop_SqrtF32();
                    ptr->field_44 = v11;
                    v18 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF((unsigned int)v11, (unsigned int)v3)) >> 5 & 3 | (unsigned long long)(CmpF((unsigned int)v11, (unsigned int)v3) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF((unsigned int)v11, (unsigned int)v3)) >> 5 & 3 | (unsigned long long)(CmpF((unsigned int)v11, (unsigned int)v3) & 1)) & ((unsigned long long)(char)(CmpF((unsigned int)v11, (unsigned int)v3)) >> 5 & 3 | (unsigned long long)(CmpF((unsigned int)v11, (unsigned int)v3) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                    if ((char)v18 || !((v30 = ptr->field_40, v19 = (unsigned long)arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF((unsigned int)v11, v30)) >> 5 & 3 | (unsigned long long)(CmpF((unsigned int)v11, v30) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF((unsigned int)v11, v30)) >> 5 & 3 | (unsigned long long)(CmpF((unsigned int)v11, v30) & 1)) & ((unsigned long long)(char)(CmpF((unsigned int)v11, v30)) >> 5 & 3 | (unsigned long long)(CmpF((unsigned int)v11, v30) & 1)) >> 1 & 1)) * 0x10000000, 0, 0), !((char)v19))))
                        continue;
                    cur = ptr->field_28;
                    if (!cur)
                        break;
                    v20 = sub_14a30c0(cur, v13, g_1ef7630);
                    if (!g_1ef0c58->field_e0)
                        sub_f7da5c(g_1ef0c58);
                    if (!(Object__op_Inequality(p, v20, 0) & 1))
                        continue;
                    if (flag != 3)
                    {
                        if (flag != 2)
                        {
                            if (flag != 1)
                                continue;
                            cur = ptr->field_28;
                            if (!cur || !((cur = (struct_11 *)(unsigned long long)sub_14a30c0(cur, (unsigned long long)(unsigned int)v13, g_1ef7630), cur)))
                                break;
                            if (cur->field_f0 == 2)
                                goto LABEL_1080dcc;
                        }
                        else
                        {
                            cur = ptr->field_28;
                            if (!cur || !((cur = (struct_11 *)(unsigned long long)sub_14a30c0(cur, (unsigned long long)(unsigned int)v13, g_1ef7630), cur)))
                                break;
                            if (cur->field_f0 == 1)
                                goto LABEL_1080dcc;
                        }
                        cur = ptr->field_28;
                        if (!cur || !((cur = (struct_11 *)(unsigned long long)sub_14a30c0(cur, (unsigned long long)(unsigned int)v13, g_1ef7630), cur)))
                            break;
                        if (cur->field_f0 != 3)
                            continue;
                    }
                    else
                    {
                        cur = ptr->field_28;
                        if (!cur || !((cur = (struct_11 *)(unsigned long long)sub_14a30c0(cur, (unsigned long long)(unsigned int)v13, g_1ef7630), cur)))
                            break;
                        if (cur->field_f0 == 3)
                            continue;
                    }
LABEL_1080dcc:
                    v11 = ptr->field_44;
                    cur = ptr->field_28;
                    ptr->field_40 = v11;
                    if (!cur)
                        break;
                    addr = sub_14a30c0(cur, v13, g_1ef7630);
                    cur = ptr->field_28;
                    v13 += 1;
                    v14 = v17;
                } while (cur);
            }
        }
    }
    sub_f7db74(cur);
}
```


## `NPCRegistry.UnregisterNPC` — RVA `0xc83e2c`

- Decompiled symbol: `NPCRegistry_UnregisterNPC`
- Metadata signature: `public void UnregisterNPC(AI NpcAI) { }`
- Native interval: `252` bytes
- Result: `pseudocode`

```c
typedef struct struct_3 {
    char padding_0[24];
    unsigned int field_18;
} struct_3;

typedef struct struct_2 {
    char padding_0[40];
    struct struct_1 *field_28;
} struct_2;

typedef struct struct_1 {
    char padding_0[24];
    int field_18;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern long long g_1ef7620;
extern long long g_1ef7628;
extern long long g_1ef7630;
extern char g_1fab421;

struct_3 * NPCRegistry_UnregisterNPC(struct_2 *ptr, long long a1)
{
    struct_1 *v0;  // x0
    int v1;  // w21
    long long v2;  // x0
    unsigned long v3;  // x0

    if (!(g_1fab421 & 1))
    {
        sub_f7d92c(&g_1ef7620);
        sub_f7d92c(&g_1ef7628);
        sub_f7d92c(&g_1ef7630);
        sub_f7d92c(&g_1ef0c58);
        g_1fab421 = 1;
    }
    v0 = ptr->field_28;
    if (v0)
    {
        v1 = 0;
        do
        {
            if (v0->field_18 <= v1)
                return v0;
            v2 = sub_14a30c0();
            if (!g_1ef0c58->field_e0)
                sub_f7da5c(g_1ef0c58);
            if (!(Object__op_Equality(v2, a1, 0) & 1))
                continue;
            v0 = ptr->field_28;
            if (!v0)
                break;
            sub_14a48fc(v0, v1, g_1ef7620);
        } while ((v0 = (struct_1 *)ptr->field_28, v1 = (int)(v1 + 1), v0));
    }
    v3 = sub_f7db74(v0);
    return sub_f7db74(v0);
}
```


## `NPCRegistry.Start` — RVA `0xc86efc`

- Decompiled symbol: `NPCRegistry_Start`
- Metadata signature: `private void Start() { }`
- Native interval: `208` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[40];
    long long field_28;
} struct_0;

extern long long g_1efcf38;
extern long long g_1efebc0;
extern char g_1fab420;

void NPCRegistry_Start(long long *addr)
{
    unsigned long long v3;  // x30
    unsigned long long v4;  // x20
    unsigned long long v5;  // x19
    struct_0 *ptr3;  // x0
    long long v7;  // x1
    long long ptr[8];  // x20
    long long v9[8];  // x20
    long long v10;  // x0
    long long p[8];  // x20
    long long v12[8];  // x20
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x10]
    unsigned long long v2;  // [bp-0x8]

    v0 = v3;
    v1 = v4;
    v2 = v5;
    if (!(g_1fab420 & 1))
    {
        sub_f7d92c(&g_1efcf38);
        sub_f7d92c(&g_1efebc0);
        g_1fab420 = 1;
    }
    if (Camera__get_main(0) && Component__get_transform())
    {
        ptr3 = sub_1231bc8();
        if (ptr3)
        {
            v7 = ptr3->field_28;
            ptr = addr;
            ptr[6] = v7;
            v9 = &ptr[6];
            sub_f7d8d0(v9, v7);
            if (v9[0])
            {
                v10 = sub_1249224(v9[0], g_1efebc0);
                p = addr;
                p[4] = v10;
                v12 = &p[4];
                sub_f7d8d0(v12, v10);
                if (v12[2])
                {
                    addr[7] = GameObject__get_transform(v12[2], 0);
                    sub_f7d8d0();
                    return;
                }
            }
        }
    }
    sub_f7db74();
}
```


## `NPCRegistry.MoveFolowingNpcs` — RVA `0xc86fcc`

- Decompiled symbol: `NPCRegistry_MoveFolowingNpcs`
- Metadata signature: `public void MoveFolowingNpcs(Vector3 position) { }`
- Native interval: `860` bytes
- Result: `pseudocode`

```c
typedef struct struct_3 {
    char padding_0[240];
    unsigned int field_f0;
    char padding_f4[57];
    char field_12d;
    char padding_12e[1];
    char field_12f;
    char field_130;
    char padding_131[19];
    unsigned int field_144;
    unsigned int field_148;
    unsigned int field_14c;
    char padding_150[40];
    unsigned long long field_178;
    unsigned long long field_180;
    char padding_188[80];
    struct struct_3 *field_1d8;
    char padding_1e0[126];
    char field_25e;
} struct_3;

typedef struct struct_2 {
    char padding_0[40];
    struct struct_1 *field_28;
} struct_2;

typedef struct struct_1 {
    char padding_0[240];
    unsigned int field_f0;
    char padding_f4[57];
    char field_12d;
    char padding_12e[1];
    char field_12f;
    char field_130;
    char padding_131[19];
    unsigned int field_144;
    unsigned int field_148;
    unsigned int field_14c;
    char padding_150[40];
    long long field_178;
    long long field_180;
    char padding_188[80];
    struct struct_1 *field_1d8;
    char padding_1e0[126];
    char field_25e;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern long long g_1ef7628;
extern long long g_1ef7630;
extern char g_1fab422;

struct_3 * NPCRegistry_MoveFolowingNpcs(struct_2 *ptr)
{
    struct_1 *cur;  // x0, Other Possible Types: struct_3 *
    unsigned long long v1;  // x21
    unsigned long v8;  // 4125
    unsigned long v9;  // x8
    struct_3 *v10;  // x0
    struct_3 *v11;  // x0
    struct_3 *v12;  // x0
    struct_3 *p;  // x0
    struct_3 *v14;  // x0
    struct_3 *v15;  // x0
    unsigned int v16;  // s0
    int v2;  // w20
    unsigned int v3;  // s0
    unsigned int v4;  // s0
    unsigned int v5;  // s1
    unsigned int v6;  // s2
    struct_3 *v7;  // x21

    if (!(g_1fab422 & 1))
    {
        sub_f7d92c(&g_1ef7628);
        sub_f7d92c(&g_1ef7630);
        sub_f7d92c(&g_1ef0c58);
        g_1fab422 = 1;
    }
    cur = ptr->field_28;
    if (cur)
    {
        v1 = 0;
        v2 = 0;
        v4 = v3;
        do
        {
            v16 = v4;
            if (*((int *)&cur->padding_0[24]) <= v2)
                return cur;
            cur = sub_14a30c0();
            if (!cur)
                break;
            if (cur->field_12f)
                continue;
            cur = ptr->field_28;
            if (!cur || !((cur = (struct_1 *)(unsigned long long)sub_14a30c0(cur, (unsigned long long)(unsigned int)v2, g_1ef7630), cur)))
                break;
            if (cur->field_f0 != 1)
                continue;
            cur = ptr->field_28;
            if (!cur || !((cur = (struct_1 *)(unsigned long long)sub_14a30c0(cur, (unsigned long long)(unsigned int)v2, g_1ef7630), cur)))
                break;
            if (!cur->field_12d)
            {
                cur = ptr->field_28;
                if (!cur || !((cur = (struct_1 *)(unsigned long long)sub_14a30c0(cur, (unsigned long long)(unsigned int)v2, g_1ef7630), cur)))
                    break;
                if (!cur->field_130)
                    continue;
            }
            cur = ptr->field_28;
            if (!cur || !((cur = (struct_1 *)(unsigned long long)sub_14a30c0(cur, (unsigned long long)(unsigned int)v2, g_1ef7630), cur)))
                break;
            cur->field_130 = 1;
            cur->field_25e = 1;
            cur->field_144 = v3;
            cur->field_148 = v5;
            cur->field_14c = v6;
            cur = ptr->field_28;
            if (!cur || !((cur = (struct_1 *)(unsigned long long)sub_14a30c0(cur, (unsigned long long)(unsigned int)v2, g_1ef7630), cur)))
                break;
            cur->field_12d = 0;
            if (!((char)v1 & 1))
            {
                cur = ptr->field_28;
                if (!cur || !((cur = (struct_1 *)(unsigned long long)sub_14a30c0(cur, (unsigned long long)(unsigned int)v2, g_1ef7630), cur)))
                    break;
                if (!g_1ef0c58->field_e0)
                    sub_f7da5c(g_1ef0c58);
                if (!((char)Object__op_Implicit(cur->field_178, 0) & 1))
                {
                    cur = ptr->field_28;
                    if (!cur || !((cur = (struct_1 *)(unsigned long long)sub_14a30c0(cur, (unsigned long long)(unsigned int)v2, g_1ef7630), cur)))
                        break;
                    if (!g_1ef0c58->field_e0)
                        sub_f7da5c(g_1ef0c58);
                    if (!((char)Object__op_Implicit(cur->field_180, 0) & 1))
                    {
                        v1 = 0;
                        continue;
                    }
                }
                Random__get_value(0);
                cur = ptr->field_28;
                if (!cur || !((cur = (struct_1 *)(unsigned long long)sub_14a30c0(cur, (unsigned long long)(unsigned int)v2, g_1ef7630), cur && ptr->field_28 && (v7 = (struct_3 *)cur->field_1d8, cur = (struct_1 *)(unsigned long long)sub_14a30c0(ptr->field_28, (unsigned long long)(unsigned int)v2, g_1ef7630), cur))))
                    break;
                v8 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v16, 0x3f000000)) >> 5 & 3 | (unsigned long long)(CmpF(v16, 0x3f000000) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v16, 0x3f000000)) >> 5 & 3 | (unsigned long long)(CmpF(v16, 0x3f000000) & 1)) & ((unsigned long long)(char)(CmpF(v16, 0x3f000000)) >> 5 & 3 | (unsigned long long)(CmpF(v16, 0x3f000000) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                if (!((char)v8))
                {
                    if (!v7)
                        break;
                    v9 = &cur->field_178;
                }
                else
                {
                    if (!v7)
                        break;
                    v9 = &cur->field_180;
                }
                AudioSource__set_clip(v7, *((long long *)v9), 0);
                cur = ptr->field_28;
                if (...)
                    break;
                AudioSource__PlayOneShot(v12->field_1d8, v15, 0);
            }
            v1 = 1;
        } while ((cur = (struct_1 *)ptr->field_28, v2 = (int)(v2 + 1), v4 = v16, cur));
    }
    sub_f7db74(cur);
}
```


## `NPCRegistry.ctor` — RVA `0xc87328`

- Decompiled symbol: `NPCRegistry_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `136` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[40];
    long long field_28;
} struct_0;

extern long long g_1eed520;
extern long long g_1ef7610;
extern char g_1fab424;

void NPCRegistry_ctor(struct_0 *ptr)
{
    unsigned long long v5;  // x30
    unsigned long long v6;  // x22
    unsigned long long v7;  // x21
    unsigned long long v8;  // x20
    unsigned long long v9;  // x19
    long long v10;  // x20
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
    if (!(g_1fab424 & 1))
    {
        sub_f7d92c(&g_1ef7610);
        sub_f7d92c(&g_1eed520);
        g_1fab424 = 1;
    }
    v10 = sub_f7db70(g_1eed520);
    sub_14a2b64(v10, g_1ef7610);
    ptr->field_28 = v10;
    sub_f7d8d0(&ptr->field_28, v10);
}
```
