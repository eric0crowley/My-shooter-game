# Native pseudocode: MoveTrigger

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `MoveTrigger.Start` — RVA `0xc855a0`

- Decompiled symbol: `MoveTrigger_Start`
- Metadata signature: `private void Start() { }`
- Native interval: `156` bytes
- Result: `pseudocode`
- Heuristic layout hint: `MoveTrigger_Recovered` matched 2 offsets against `MoveTrigger` metadata (confidence 1.00).

```c
typedef struct MoveTrigger_Recovered {
    char padding_0[32];
    struct struct_1 *npcToMove;
    char padding_28[24];
    char isStartingTrigger;
} MoveTrigger_Recovered;

typedef struct struct_1 {
    char padding_0[302];
    unsigned short field_12e;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab41a;

long long MoveTrigger_Start(struct_2 *idx)
{
    long long v0;  // x0

    if (!(g_1fab41a & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab41a = 1;
    }
    if (!idx->field_40)
    {
        if (Component__get_gameObject(idx, 0))
            GameObject__SetActive();
        else
            sub_f7db74();
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v0 = Object__op_Implicit(idx->field_20, 0);
    if (!((char)v0 & 1))
        return v0;
    if (idx->field_20)
    {
        idx->field_20->field_12e = 0x100;
        return v0;
    }
    sub_f7db74();
}
```

## `MoveTrigger.OnTriggerStay` — RVA `0xc8563c`

- Decompiled symbol: `MoveTrigger_OnTriggerStay`
- Metadata signature: `private void OnTriggerStay(Collider col) { }`
- Native interval: `608` bytes
- Result: `pseudocode`
- Heuristic layout hint: `MoveTrigger_Recovered` matched 6 offsets against `MoveTrigger` metadata (confidence 1.00).

```c
typedef struct struct_4 {
    char padding_0[49];
    unsigned short field_31;
    char padding_33[253];
    char field_130;
    char padding_131[19];
    unsigned int field_144;
    unsigned int field_148;
    unsigned int field_14c;
    char padding_150[136];
    struct struct_4 *field_1d8;
    char padding_1e0[126];
    char field_25e;
    char field_25f;
} struct_4;

typedef struct MoveTrigger_Recovered {
    char padding_0[32];
    struct struct_1 *npcToMove;
    struct struct_1 *movePosition;
    char runToGoal;
    char moved;
    char padding_32[6];
    struct struct_1 *nextMoveTrigger;
    char padding_40[8];
    struct struct_2 *followSnds;
} MoveTrigger_Recovered;

typedef struct struct_1 {
    char padding_0[49];
    unsigned short field_31;
    char padding_33[253];
    char field_130;
    char padding_131[19];
    unsigned int field_144;
    unsigned int field_148;
    unsigned int field_14c;
    char padding_150[136];
    struct struct_1 *field_1d8;
    char padding_1e0[126];
    char field_25e;
    char field_25f;
} struct_1;

typedef struct struct_2 {
    char padding_0[24];
    unsigned long long field_18;
} struct_2;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern long long g_1f0cf98;
extern char g_1fab41b;

struct_4 * MoveTrigger_OnTriggerStay(struct_3 *ptr, long long a1)
{
    struct_4 *v0;  // x0
    struct_1 *v1;  // x0, Other Possible Types: struct_4 *
    long long v2;  // x0
    struct_1 *p;  // x20
    unsigned int v4;  // s0
    unsigned int v5;  // s1
    unsigned int v6;  // s2
    struct_2 *v7;  // x21
    struct_4 *v8;  // x20

    if (!(g_1fab41b & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c(&g_1f0cf98);
        g_1fab41b = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v0 = Object__op_Implicit(ptr->field_20, 0);
    if (!((char)v0 & 1))
        return v0;
    v1 = ptr->field_20;
    if (v1)
    {
        v1 = Behaviour__get_enabled(v1, 0);
        if (!((char)v1 & 1))
            return v1;
        if (a1 && (v1 = (struct_1 *)Component__get_gameObject(a1, 0), v1))
        {
            v2 = GameObject__get_tag();
            v1 = String__op_Equality(v2, g_1f0cf98, 0);
            if (!((char)v1 & 1))
                return v1;
            if (ptr->field_31)
                return v1;
            p = ptr->field_20;
            if (p)
            {
                if (p->padding_1e0[119])
                    return v1;
                v1 = ptr->field_28;
                if (v1)
                {
                    v1 = Transform__get_position(v1, 0);
                    p->padding_33[252] = ptr->field_30;
                    *((unsigned int *)&p->padding_131[18]) = v4;
                    p->field_144 = v5;
                    p->padding_1e0[118] = 1;
                    p->field_148 = v6;
                    if (ptr->field_48)
                    {
                        if (!ptr->field_48->field_18)
                        {
LABEL_1085820:
                            if (!g_1ef0c58->field_e0)
                                sub_f7da5c(g_1ef0c58);
                            v1 = Object__op_Implicit(ptr->field_38, 0);
                            if (((char)v1 & 1))
                            {
                                v1 = ptr->field_38;
                                if (v1 && (v1 = (struct_1 *)Component__get_gameObject(v1, 0), v1 && (v1 = (struct_1 *)GameObject__SetActive(), ptr->field_38)))
                                {
                                    *((unsigned short *)&(&ptr->field_38->padding_0)[1]) = 0;
                                    goto LABEL_1085870;
                                }
                            }
                            else
                            {
LABEL_1085870:
                                if (ptr->field_20)
                                {
                                    ptr->field_20->padding_1e0[119] = 1;
                                    ptr->field_31 = 1;
                                    return v1;
                                }
                            }
                        }
                        else if (ptr->field_20 && (v1 = (struct_1 *)*((long long *)&ptr->field_20->padding_150[132]), v1 && (v1 = (struct_1 *)AudioSource__set_volume(v1, 0), ptr->field_20 && (v1 = (struct_1 *)(unsigned long long)Random__Range(0), *((long long *)&ptr->field_20->padding_150[132]) && (v1 = (struct_1 *)(unsigned long long)AudioSource__set_pitch(*((long long *)&ptr->field_20->padding_150[132]), 0), ptr->field_20 && (v1 = (struct_1 *)*((long long *)&ptr->field_20->padding_150[132]), v1 && (v1 = (struct_1 *)AudioSource__set_spatialBlend(v1, 0), ptr->field_20 && (v7 = (struct_2 *)ptr->field_48, v7))))))))
                        {
                            v1 = Random__Range(0, (unsigned int)v7->field_18, 0);
                            if ((int)v7->field_18 <= (unsigned int)v1)
                                sub_f7db7c(v1);
                            if (*((long long *)&ptr->field_20->padding_150[132]) && (v1 = (struct_1 *)(unsigned long long)AudioSource__set_clip(*((long long *)&ptr->field_20->padding_150[132]), *((long long *)&v7[1].padding_0[8 * (v1 & 4294967295)]), 0), ptr->field_20 && (v8 = (struct_4 *)*((long long *)&ptr->field_20->padding_150[132]), v8)))
                            {
                                AudioSource__PlayOneShot(v8, AudioSource__get_clip(v8, 0), 0);
                                goto LABEL_1085820;
                            }
                        }
                    }
                }
            }
        }
    }
    v1 = sub_f7db74(v1);
    sub_f7db7c(v1);
}
```

## `MoveTrigger.Update` — RVA `0xc8589c`

- Decompiled symbol: `MoveTrigger_Update`
- Metadata signature: `private void Update() { }`
- Native interval: `348` bytes
- Result: `pseudocode`
- Heuristic layout hint: `MoveTrigger_Recovered` matched 4 offsets against `MoveTrigger` metadata (confidence 0.80).

```c
typedef struct struct_3 {
    char padding_0[32];
    struct struct_2 *field_20;
    struct struct_3 *field_28;
    char padding_30[1];
    char field_31;
    char field_32;
    char padding_33[173];
    unsigned int field_e0;
} struct_3;

typedef struct struct_5 {
    char padding_0[48];
    struct MoveTrigger_Recovered *field_30;
    char padding_38[200];
    struct MoveTrigger_Recovered *field_100;
    char padding_108[56];
    unsigned int field_140;
    char padding_144[282];
    char field_25e;
    char field_25f;
} struct_5;

typedef struct struct_2 {
    char padding_0[48];
    struct struct_3 *field_30;
    char padding_38[200];
    struct struct_3 *field_100;
    char padding_108[56];
    unsigned int field_140;
    char padding_144[282];
    char field_25e;
    char field_25f;
} struct_2;

typedef struct MoveTrigger_Recovered {
    char padding_0[32];
    struct struct_5 *npcToMove;
    struct MoveTrigger_Recovered *movePosition;
    char padding_30[1];
    char moved;
    char rotated;
    char padding_33[173];
    unsigned int field_e0;
} MoveTrigger_Recovered;

extern char g_1fab3e0;

struct_3 * MoveTrigger_Update(struct_3 *ptr)
{
    struct_3 *v0;  // x0
    struct_5 *p;  // x20
    unsigned int v2;  // s3
    unsigned int v3;  // s0
    unsigned long v4;  // 4244
    struct_3 *v5;  // x0

    if (!ptr->field_31)
    {
        return ptr;
    }
    else if (!ptr->field_32)
    {
        v0 = ptr->field_28;
        if (v0)
        {
            v0 = Transform__get_position(v0, 0);
            if (ptr->field_20)
            {
                v0 = ptr->field_20->field_100;
                if (v0)
                {
                    Transform__get_position(v0, 0);
                    if (!g_1fab3e0)
                    {
                        sub_f7d92c("_F");
                        g_1fab3e0 = 1;
                    }
                    v0 = g_1ef07e8;
                    if (!g_1ef07e8->field_e0)
                        v0 = sub_f7da5c(g_1ef07e8);
                    p = ptr->field_20;
                    if (p)
                    {
                        v2 = p->field_140;
                        v3 = [D] unsupported_Iop_SqrtF32();
                        v4 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v3, v2)) >> 5 & 3 | (unsigned long long)(CmpF(v3, v2) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v3, v2)) >> 5 & 3 | (unsigned long long)(CmpF(v3, v2) & 1)) & ((unsigned long long)(char)(CmpF(v3, v2)) >> 5 & 3 | (unsigned long long)(CmpF(v3, v2) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                        if ((char)v4)
                            return v0;
                        v0 = p->field_30;
                        p->field_25e = 0;
                        if (v0)
                        {
                            Transform__get_position(v0, 0);
                            v0 = MonoBehaviour__StartCoroutine(p, AI__RotateTowards(p, 0), 0);
                            if (ptr->field_20)
                            {
                                ptr->field_20->field_25f = 0;
                                v0 = Component__get_gameObject(ptr, 0);
                                if (v0)
                                {
                                    v5 = GameObject__SetActive();
                                    ptr->field_32 = 1;
                                    return v5;
                                }
                            }
                        }
                    }
                }
            }
        }
        sub_f7db74(v0);
    }
    else
    {
        return ptr;
    }
}
```

## `MoveTrigger.ctor` — RVA `0xc859f8`

- Decompiled symbol: `MoveTrigger_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `20` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[80];
    unsigned int field_50;
} struct_0;

long long MoveTrigger_ctor(struct_0 *ptr)
{
    ptr->field_50 = 1060320051;
}
```
