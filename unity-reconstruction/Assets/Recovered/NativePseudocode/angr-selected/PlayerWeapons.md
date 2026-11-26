# Native pseudocode: PlayerWeapons

> Metadata source-path string: `Assets/RFPSP/Scripts/Weapons/PlayerWeapons.cs`. This is a path string from the APK metadata, not recovered source text.

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `PlayerWeapons.Start` — RVA `0xcb1e14`

- Decompiled symbol: `PlayerWeapons_Start`
- Metadata signature: `private void Start() { }`
- Native interval: `2176` bytes
- Result: `pseudocode`

```c
typedef struct struct_20 {
    char padding_0[224];
    unsigned int field_e0;
} struct_20;

typedef struct struct_6 {
    char padding_0[32];
    long long field_20;
} struct_6;

typedef struct struct_7 {
    char padding_0[32];
    long long field_20;
} struct_7;

typedef struct struct_8 {
    char padding_0[32];
    long long field_20;
} struct_8;

typedef struct struct_4 {
    char padding_0[292];
    unsigned int field_124;
} struct_4;

typedef struct struct_21 {
    char padding_0[24];
    unsigned int field_18;
    char padding_1c[4];
    unsigned long long field_20;
} struct_21;

typedef struct struct_5 {
    char padding_0[292];
    unsigned int field_124;
} struct_5;

typedef struct struct_9 {
    char padding_0[288];
    char field_120;
} struct_9;

typedef struct struct_10 {
    char padding_0[288];
    char field_120;
} struct_10;

typedef struct struct_11 {
    char padding_0[32];
    long long field_20;
} struct_11;

typedef struct struct_12 {
    char padding_0[288];
    char field_120;
} struct_12;

typedef struct struct_13 {
    char padding_0[32];
    long long field_20;
} struct_13;

typedef struct struct_14 {
    char padding_0[288];
    char field_120;
} struct_14;

typedef struct struct_15 {
    char padding_0[32];
    long long field_20;
} struct_15;

typedef struct struct_16 {
    char padding_0[288];
    char field_120;
} struct_16;

typedef struct struct_17 {
    char padding_0[32];
    long long field_20;
} struct_17;

typedef struct struct_18 {
    char padding_0[288];
    char field_120;
} struct_18;

typedef struct struct_19 {
    char padding_0[288];
    char field_120;
} struct_19;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern long long g_1eeb668;
extern long long g_1eee238;
extern void g_1ef0c58;
extern struct_0 *g_1ef1f08;
extern long long g_1efcf38;
extern long long g_1efd178;
extern long long g_1efd1e8;
extern long long g_1efea78;
extern long long g_1efebb8;
extern long long g_1efebc0;
extern long long g_1efec08;
extern long long g_1efec18;
extern long long g_1efed18[5];
extern long long g_1f0bd20[5];
extern void g_1fab000;
extern char g_1fab4d4;

void* PlayerWeapons_Start(void* a0, unsigned long a1, unsigned long a2, unsigned long a3)
{
    void* p;  // x21
    long long v1[5];  // x22
    void* addr;  // x21
    long long v11;  // x0
    void* ptr4;  // x21
    long long v13;  // x0
    void* ptr5;  // x21
    long long v15;  // x0
    void* ptr6;  // x21
    long long v17;  // x0
    void* ptr7;  // x21
    long long v19;  // x0
    void* cur;  // x19
    void* ptr8;  // x21
    unsigned long v21;  // x8
    unsigned long v22;  // x9
    struct_6 *v23;  // x8
    long long v24;  // x0
    void* ptr9;  // x21
    unsigned long v26;  // x8
    unsigned long v27;  // x9
    struct_7 *v28;  // x8
    void* v29;  // x0
    long long v3;  // x0
    long long v30;  // x1
    void* ptr10;  // x0
    long long v32;  // x1
    long long v33;  // x0
    void* v34;  // x21
    void* v35;  // x21
    unsigned long long v36[18];  // x8
    unsigned long long v37;  // x23
    struct_8 *v38;  // x8
    struct_4 *ptr12;  // x0
    void* v4;  // x20
    struct_21 *i;  // x8
    struct_5 *v41;  // x1
    unsigned long v42;  // x8
    unsigned long v43;  // 4121
    unsigned long long v44[18];  // x8
    struct_9 *ptr13;  // x0
    unsigned long long v47[18];  // x8
    struct_10 *ptr14;  // x0
    unsigned long long v49[18];  // x8
    void* ptr;  // x20
    unsigned int v50;  // w9
    struct_11 *v51;  // x8
    struct_12 *v52;  // x0
    unsigned long long v53[18];  // x8
    unsigned long v54;  // x9
    struct_13 *v55;  // x8
    struct_14 *ptr15;  // x0
    unsigned int v57;  // w9
    struct_15 *v58;  // x8
    struct_16 *ptr16;  // x0
    long long v6;  // x1
    unsigned long long v60[18];  // x8
    unsigned int v61;  // w9
    struct_17 *v62;  // x8
    struct_18 *v63;  // x0
    unsigned long long v64[18];  // x8
    struct_19 *ptr17;  // x0
    void* v67;  // x0
    long long v68;  // x0
    void* ptr18;  // x0
    long long v7;  // x0
    unsigned int j;  // w8
    long long v71[5];  // x22
    void* v72;  // x0
    long long v73;  // x0
    void* ptr11;  // x21
    unsigned long v9;  // x1

    p = &g_1fab000;
    v1 = &g_1f0bd20[0];
    cur = a0;
    if (!(g_1fab4d4 & 1))
    {
        sub_f7d92c(&g_1efcf38);
        sub_f7d92c(&g_1efd1e8);
        sub_f7d92c(&g_1efd178);
        sub_f7d92c(&g_1efea78);
        sub_f7d92c(&g_1efebb8);
        sub_f7d92c(&g_1efebc0);
        sub_f7d92c(&g_1efec08);
        sub_f7d92c(&g_1efec18);
        sub_f7d92c(&g_1efed18[0]);
        sub_f7d92c(&g_1eee238);
        sub_f7d92c(&g_1eeb668);
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c(&g_1ef1f08);
        sub_f7d92c("_&");
        sub_f7d92c("\t:");
        sub_f7d92c(&g_1f0bd20[0]);
        g_1fab4d4 = 1;
    }
    *((unsigned int *)&cur[80]) = PlayerPrefs__GetInt(g_1f0bd20, 0);
    *((unsigned int *)&cur[84]) = PlayerPrefs__GetInt(g_1f0fb68, 0);
    v3 = Component__get_transform(cur, 0);
    v4 = cur + 0x100;
    *((long long *)&cur[0x100]) = v3;
    sub_f7d8d0(v4, v3);
    ptr = v4;
    if (Camera__get_main(0))
    {
        v6 = Component__get_transform();
        *((long long *)&cur[264]) = v6;
        sub_f7d8d0(cur + 264, v6);
        ptr = v4;
        if ((long long)cur[264])
        {
            v7 = sub_1231bc8((long long)cur[264], g_1efcf38);
            ptr11 = cur;
            *((long long *)&ptr11[168]) = v7;
            p = ptr11 + 168;
            sub_f7d8d0(p, v7);
            ptr = v4;
            if (*((long long *)p))
            {
                v9 = *((long long *)(*((long long *)p) + 40));
                addr = cur;
                *((unsigned long *)&addr[112]) = v9;
                p = addr + 112;
                sub_f7d8d0(p, v9);
                ptr = v4;
                if ((long long)p[56] && !((ptr = v4, !Component__get_transform((long long)p[56], 0) || (ptr = v4, !(unsigned long long)Transform__get_parent() || (ptr = v4, !Component__get_transform())))))
                {
                    v11 = Component__get_gameObject();
                    ptr4 = cur;
                    *((long long *)&ptr4[120]) = v11;
                    p = ptr4 + 120;
                    sub_f7d8d0(p, v11);
                    ptr = v4;
                    if ((long long)p[8])
                    {
                        v13 = sub_1249224((long long)p[8], g_1efec08);
                        ptr5 = cur;
                        *((long long *)&ptr5[128]) = v13;
                        p = ptr5 + 128;
                        sub_f7d8d0(p, v13);
                        ptr = v4;
                        if ((long long)p[16])
                        {
                            v15 = sub_1249224((long long)p[16], g_1efebc0);
                            ptr6 = cur;
                            *((long long *)&ptr6[136]) = v15;
                            p = ptr6 + 136;
                            sub_f7d8d0(p, v15);
                            ptr = v4;
                            if ((long long)p[24])
                            {
                                v17 = sub_1249224((long long)p[24], g_1efebb8);
                                ptr7 = cur;
                                *((long long *)&ptr7[144]) = v17;
                                p = ptr7 + 144;
                                sub_f7d8d0(p, v17);
                                ptr = v4;
                                if ((long long)p[32])
                                {
                                    v19 = sub_1249224((long long)p[32], g_1efec18);
                                    ptr8 = cur;
                                    *((long long *)&ptr8[160]) = v19;
                                    p = ptr8 + 160;
                                    sub_f7d8d0(p, v19);
                                    v21 = (long long)p[72];
                                    ptr = v4;
                                    if (v21)
                                    {
                                        v22 = (int)p[40];
                                        if (*((int *)(v21 + 24)) <= (unsigned int)v22)
                                            goto LABEL_10b2690;
                                        v23 = v21 + v22 * 8;
                                        ptr = v4;
                                        if (v23->field_20)
                                        {
                                            v1 = &g_1efed18[0];
                                            v24 = sub_1249224(v23->field_20, g_1efed18);
                                            ptr9 = cur;
                                            *((long long *)&ptr9[152]) = v24;
                                            p = ptr9 + 152;
                                            sub_f7d8d0(p, v24);
                                            v26 = (long long)p[80];
                                            ptr = v4;
                                            if (v26)
                                            {
                                                v27 = (int)p[56];
                                                if (*((int *)(v26 + 24)) <= (unsigned int)v27)
                                                    goto LABEL_10b2690;
                                                v28 = v26 + v27 * 8;
                                                ptr = v4;
                                                if (v28->field_20 && !((v29 = (void*)sub_1249224(v28->field_20, g_1efed18), ptr = v4, !*((long long *)ptr))))
                                                {
                                                    ptr = sub_1249224(v28->field_20, g_1efed18);
                                                    v30 = sub_123247c(*((long long *)v4), 1, g_1efd1e8);
                                                    ptr10 = cur;
                                                    *((long long *)&ptr10[240]) = v30;
                                                    sub_f7d8d0(ptr10 + 240, v30);
                                                    ptr = ptr;
                                                    if (Component__get_transform(cur, 0))
                                                    {
                                                        v32 = sub_123226c();
                                                        *((long long *)&cur[336]) = v32;
                                                        sub_f7d8d0(cur + 336, v32);
                                                        ptr = ptr;
                                                        if ((long long)cur[112])
                                                        {
                                                            v33 = sub_124913c((long long)cur[112], g_1efea78);
                                                            v34 = cur + 344;
                                                            *((long long *)&cur[344]) = v33;
                                                            sub_f7d8d0(v34, v33);
                                                            p = v34;
                                                            if ((long long)cur[344] && !((AudioSource__set_spatialBlend((long long)cur[344], 0), p = v34, ptr = ptr, !*((long long *)p))))
                                                            {
                                                                v35 = "\t:";
                                                                AudioSource__set_playOnAwake(*((long long *)v34), 0, 0);
                                                                if (!PlayerPrefs__GetInt(*((long long *)&g_1f14a10), 0))
                                                                {
                                                                    p = v35;
                                                                    if ((long long)cur[88])
                                                                    {
                                                                        Material__set_mainTexture((long long)cur[88], (long long)cur[96], 0);
                                                                        goto LABEL_10b2204;
                                                                    }
                                                                }
                                                                else
                                                                {
LABEL_10b2204:
                                                                    if (PlayerPrefs__GetInt(*((long long *)&g_1f14a10), 0) == 1)
                                                                    {
                                                                        p = v35;
                                                                        if ((long long)cur[88])
                                                                        {
                                                                            Material__set_mainTexture((long long)cur[88], (long long)cur[104], 0);
                                                                            goto LABEL_10b222c;
                                                                        }
                                                                    }
                                                                    else
                                                                    {
LABEL_10b222c:
                                                                        p = v35;
                                                                        if ((long long)cur[232])
                                                                        {
                                                                            p = &g_1ef0c58;
                                                                            v37 = 0;
                                                                            while ((int)v36[3] > (unsigned int)v37)
                                                                            {
                                                                                if ((int)v36[3] <= (unsigned int)v37)
                                                                                    goto LABEL_10b2690;
                                                                                v38 = &v36[v37];
                                                                                if (!v38->field_20 || (ptr12 = (struct_4 *)sub_1249224(v38->field_20, g_1efed18), ptr = ptr, !ptr12 || (ptr12->field_124 = (unsigned int)v37, v36 = (unsigned long long [18])(long long)cur[232], v37 += 1, ptr = ptr, !(long long)cur[232])) || (ptr12->field_124 = (unsigned int)v37, v36 = (unsigned long long [18])(long long)cur[232], v37 += 1, ptr = ptr, !(long long)cur[232]))
                                                                                    break;
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
    while (true)
    {
        do
        {
LABEL_10b227c:
            sub_f7db74();
            i = (long long)cur[248];
            *((unsigned int *)&cur[224]) = 0;
        } while (!i);
        if (!i->field_18)
            break;
        if (!i->field_20)
            continue;
        v41 = sub_1249224(i->field_20, v1[0]);
        *((struct_5 **)&cur[384]) = v41;
        sub_f7d8d0(cur + 384, v41);
        if (!(long long)cur[384])
            continue;
        v42 = (int)cur[80];
        *((int *)&cur[212]) = *((int *)((long long)cur[384] + 292));
        if (32 >= (unsigned int)v42)
        {
            v43 = arm64g_calculate_condition(10, 1 << ((char)v42 & 63) & 4296085796, 0, 0);
            if (!((char)v43))
            {
                v44 = (long long)cur[232];
                if (!v44)
                    continue;
                if ((int)v44[3] <= 12)
                    break;
                if (!v44[16] || !((ptr13 = (struct_9 *)sub_1249224(v44[16], v1[0]), ptr13)))
                    continue;
                ptr13->field_120 = 1;
                MonoBehaviour__StartCoroutine(cur, PlayerWeapons__SelectWeapon(), 0);
                if (!(long long)cur[32] || !((GameObject__SetActive((long long)cur[32], 0, 0), (long long)cur[56])))
                    continue;
                GameObject__SetActive((long long)cur[56], 0, 0);
                RenderSettings__set_fogStartDistance(0);
                if (!(long long)cur[72] || !((GameObject__SetActive((long long)cur[72], 0, 0), ptr)))
                    continue;
                goto LABEL_10b2500;
            }
            if (v42 == 31)
            {
                v47 = (long long)cur[232];
                if (!v47)
                    continue;
                if ((int)v47[3] <= 13)
                    break;
                if (!v47[17] || !((ptr14 = (struct_10 *)sub_1249224(v47[17], v1[0]), ptr14)))
                    continue;
                ptr14->field_120 = 1;
                goto LABEL_10b24dc;
            }
        }
        if (!(long long)cur[72] || !((GameObject__SetActive((long long)cur[72], 1, 0), v49 = (unsigned long long [18])(long long)cur[232], v49)))
            continue;
        v50 = (int)cur[84] + 1;
        if ((int)v49[3] <= v50)
            break;
        v51 = &v49[v50];
        if (!v51->field_20 || !((v52 = (struct_12 *)sub_1249224(v51->field_20, v1[0]), v52)))
            continue;
        v53 = (long long)cur[232];
        if (v52->field_120)
        {
            if (!v53)
                continue;
            v54 = (int)cur[200];
            if ((int)v53[3] <= (unsigned int)v54)
                break;
            v55 = &v53[v54];
            if (!v55->field_20 || !((ptr15 = (struct_14 *)sub_1249224(v55->field_20, v1[0]), ptr15)))
                continue;
            ptr15->field_120 = 1;
            goto LABEL_10b24d4;
        }
        else
        {
            if (!v53)
                continue;
            v57 = (int)cur[84] + 1;
            if ((int)v53[3] <= v57)
                break;
            v58 = &v53[v57];
            if (!v58->field_20 || !((ptr16 = (struct_16 *)sub_1249224(v58->field_20, v1[0]), ptr16 && (ptr16->field_120 = 1, v60 = (unsigned long long [18])(long long)cur[232], v60))))
                continue;
            v61 = (int)cur[84] + 1;
            if ((int)v60[3] <= v61)
                break;
            v62 = &v60[v61];
            if (!v62->field_20 || !((v63 = (struct_18 *)sub_1249224(v62->field_20, v1[0]), v63)))
                continue;
            if (v63->field_120)
            {
LABEL_10b24d4:
                goto LABEL_10b24dc;
            }
            else
            {
                v64 = (long long)cur[232];
                if (!v64)
                    continue;
                if ((int)v64[3] <= 1)
                    break;
                if (!v64[5] || !((ptr17 = (struct_19 *)sub_1249224(v64[5], v1[0]), ptr17)))
                    continue;
                ptr17->field_120 = 1;
LABEL_10b24dc:
                MonoBehaviour__StartCoroutine(cur, PlayerWeapons__SelectWeapon(), 0);
                if (!ptr)
                    continue;
LABEL_10b2500:
                *((unsigned short *)&ptr[290]) = 0;
                PlayerWeapons__UpdateTotalWeapons(cur);
                if (!*((int *)(*((long long *)p) + 224)))
                    sub_f7da5c(*((long long *)p));
                v67 = Object__op_Implicit((long long)cur[352], 0);
                if (((char)v67 & 1))
                    return v67;
                if (!g_1ef1f08->field_e0)
                    sub_f7da5c(g_1ef1f08);
                ptr = Type__GetTypeFromHandle(g_1eeb668, 0);
                if (!*((int *)(*((long long *)p) + 224)))
                    sub_f7da5c(*((long long *)p));
                v68 = Object__FindObjectsOfType(ptr, 0);
                ptr18 = sub_f7da60(v68, g_1eee238);
                if (!ptr18)
                    continue;
                j = (int)ptr18[24];
                ptr = ptr18;
                if ((int)ptr18[24] < 1)
                    return ptr18;
                p = NULL;
                cur += 352;
                while (j > (unsigned int)p)
                {
                    v71 = ptr + (p & 4294967295) * 8;
                    v1 = &v71[4];
                    if (!v71[4])
                        goto LABEL_10b227c;
                    v72 = Light__get_type(v71[4], 0);
                    if ((unsigned int)v72 == 1)
                    {
                        if ((int)ptr[24] <= (unsigned int)p)
                            break;
                        if (!v1[0] || !Component__get_gameObject(v1[0], 0))
                            goto LABEL_10b227c;
                        v72 = GameObject__get_activeInHierarchy();
                        if (((char)v72 & 1))
                        {
                            if ((int)ptr[24] <= (unsigned int)p)
                                break;
                            if (v1[0])
                            {
                                *((long long *)cur) = Component__get_transform(v1[0], 0);
                                v73 = sub_f7d8d0();
                                return sub_f7d8d0();
                            }
                            goto LABEL_10b227c;
                        }
                    }
                    if ((unsigned int)p + 1 >= (int)ptr[24])
                        return v72;
                }
            }
        }
    }
LABEL_10b2690:
    sub_f7db7c();
}
```


## `PlayerWeapons.SelectWeapon` — RVA `0xcb2694`

- Decompiled symbol: `PlayerWeapons_SelectWeapon`
- Metadata signature: `public IEnumerator SelectWeapon(int index, bool isOffhandThrow = false, bool endOffhandThrow = false) { }`
- Native interval: `156` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[12];
    long long field_20;
    unsigned int field_28;
    char field_2c;
    char field_2d;
} struct_0;

extern long long g_1ef36e8;
extern char g_1fab4d9;

struct_0 * PlayerWeapons_SelectWeapon(long long a0, unsigned int a1, char a2, char a3)
{
    struct_0 *v0;  // x21
    struct_0 *ptr;  // x0

    if (!(g_1fab4d9 & 1))
    {
        sub_f7d92c(&g_1ef36e8);
        g_1fab4d9 = 1;
    }
    v0 = sub_f7db70(g_1ef36e8);
    Object__ctor(v0, 0);
    ptr = v0;
    ptr->field_10 = 0;
    ptr->field_20 = a0;
    sub_f7d8d0(&ptr->field_20, a0);
    ptr->field_28 = a1;
    ptr->field_2c = a2 & 1;
    ptr->field_2d = a3 & 1;
    return ptr;
}
```


## `PlayerWeapons.UpdateTotalWeapons` — RVA `0xcb2730`

- Decompiled symbol: `PlayerWeapons_UpdateTotalWeapons`
- Metadata signature: `public void UpdateTotalWeapons() { }`
- Native interval: `220` bytes
- Result: `pseudocode`
- Heuristic layout hint: `PlayerWeapons_Recovered` matched 3 offsets against `PlayerWeapons` metadata (confidence 0.75).

```c
typedef struct PlayerWeapons_Recovered {
    char padding_0[216];
    unsigned int totalWeapons;
    char padding_dc[12];
    struct struct_0 *weaponOrder;
    char padding_f0[48];
    char switchTime;
    char padding_121[2];
    char field_123;
} PlayerWeapons_Recovered;

typedef struct struct_2 {
    char padding_0[24];
    unsigned int field_18;
} struct_2;

typedef struct struct_0 {
    char padding_0[24];
    int field_18;
} struct_0;

extern long long g_1efed18;
extern char g_1fab4d8;

struct_1 * PlayerWeapons_UpdateTotalWeapons(struct_1 *ptr)
{
    struct_1 *v0;  // x0
    struct_1 *v1;  // x0
    struct_1 *v2;  // x0
    struct_2 *v3;  // x8
    unsigned long long v4;  // x21
    unsigned int v5;  // w22
    struct_2 *v6;  // x8
    unsigned long v7;  // x0

    v0 = ptr;
    if (!(g_1fab4d8 & 1))
    {
        v1 = sub_f7d92c(&g_1efed18);
        g_1fab4d8 = 1;
        v0 = v1;
    }
    v3 = ptr->field_e8;
    ptr->field_d8 = 0;
    if (v3)
    {
        v4 = 5;
        do
        {
            v5 = v4 - 4;
            if (v3->field_18 <= v5)
                return v2;
            if (v3->field_18 <= v5)
                sub_f7db7c();
            if (!*((long long *)&v3->padding_0[8 * v4]) || !((v2 = (struct_1 *)sub_1249224(*((long long *)&v3->padding_0[8 * v4]), g_1efed18), v2)))
                break;
            if (!v2->field_120)
                continue;
            v6 = ptr->field_e8;
            if (!v6)
                break;
            if (v6->field_18 <= v5)
                sub_f7db7c();
            if (!*((long long *)&v6->padding_0[8 * v4]) || !((v2 = (struct_1 *)sub_1249224(*((long long *)&v6->padding_0[8 * v4]), g_1efed18), v2)))
                break;
            if (v2->field_123)
                ptr->field_d8 = ptr->field_d8 + 1;
        } while ((v3 = (struct_2 *)ptr->field_e8, v4 += 1, v3));
    }
    v7 = sub_f7db74();
    return sub_f7db74();
}
```


## `PlayerWeapons.Update` — RVA `0xcb280c`

- Decompiled symbol: `PlayerWeapons_Update`
- Metadata signature: `private void Update() { }`
- Native interval: `3456` bytes
- Result: `pseudocode`
- Heuristic layout hint: `PlayerWeapons_Recovered` matched 3 offsets against `PlayerWeapons` metadata (confidence 1.00).

```c
typedef struct struct_21 {
    char padding_0[288];
    char field_120;
    char field_121;
    char padding_122[6];
    int field_128;
} struct_21;

typedef struct struct_22 {
    char padding_0[272];
    unsigned long long field_110;
    unsigned long long field_118;
    char padding_120[2];
    char field_122;
    char padding_123[1];
    unsigned int field_124;
    char padding_128[12];
    unsigned int field_134;
    char padding_138[293];
    char field_25d;
    char padding_25e[302];
    unsigned long long field_38c;
    unsigned int field_394;
    char padding_398[13];
    char field_3a5;
    char padding_3a6[162];
    unsigned long long field_448;
} struct_22;

typedef struct struct_1 {
    char padding_0[32];
    long long field_20;
} struct_1;

typedef struct struct_27 {
    char padding_0[180];
    unsigned long long field_b4;
    unsigned int field_bc;
    char padding_c0[229];
    char field_1a5;
} struct_27;

typedef struct struct_24 {
    char padding_0[153];
    char field_99;
    char padding_9a[1];
    char field_9b;
    char padding_9c[3];
    char field_9f;
    char field_a0;
    char padding_a1[7];
    char field_a8;
    char field_a9;
    char field_aa;
    char field_ab;
    char field_ac;
    char field_ad;
    char field_ae;
    char field_af;
    char field_b0;
    char field_b1;
    char field_b2;
    char field_b3;
    char padding_b4[4];
    unsigned int field_b8;
    char padding_bc[52];
    char field_f0;
    char field_f1;
    char padding_f2[1];
    char field_f3;
} struct_24;

typedef struct struct_23 {
    char padding_0[524];
    unsigned int field_20c;
} struct_23;

typedef struct struct_25 {
    char padding_0[32];
    unsigned long long field_20;
} struct_25;

typedef struct struct_12 {
    char padding_0[32];
    long long field_20;
} struct_12;

typedef struct struct_13 {
    char padding_0[32];
    long long field_20;
} struct_13;

typedef struct struct_14 {
    char padding_0[32];
    long long field_20;
} struct_14;

typedef struct PlayerWeapons_Recovered {
    char padding_0[288];
    char switchTime;
    char padding_121[3];
    unsigned int sprintSwitchTime;
    unsigned int switching;
} PlayerWeapons_Recovered;

typedef struct struct_15 {
    char padding_0[32];
    long long field_20;
} struct_15;

typedef struct struct_16 {
    char padding_0[32];
    long long field_20;
} struct_16;

typedef struct struct_17 {
    char padding_0[32];
    long long field_20;
} struct_17;

typedef struct struct_18 {
    char padding_0[32];
    long long field_20;
} struct_18;

typedef struct struct_19 {
    char padding_0[32];
    long long field_20;
} struct_19;

typedef struct struct_20 {
    char padding_0[32];
    long long field_20;
} struct_20;

typedef struct struct_26 {
    char padding_0[24];
    unsigned int field_18;
    char padding_1c[12];
    unsigned long long field_28;
} struct_26;

typedef struct struct_2 {
    unsigned long long field_0;
    unsigned int field_8;
} struct_2;

typedef struct struct_3 {
    char padding_0[184];
    struct struct_2 *field_b8;
} struct_3;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern struct_3 *g_1ef22e8;
extern long long g_1efd070;
extern long long g_1efeb28;
extern long long g_1efed18;
extern long long g_1f08dd0;
extern long long g_1f0ae78;
extern long long g_1f0c5b0;
extern char g_1fab2c9;
extern char g_1fab4d5;

struct_21 * PlayerWeapons_Update(void* ptr)
{
    struct_21 *v0;  // x0
    void* v1;  // x8
    struct_27 *ptr3;  // x9
    unsigned int v11;  // s1
    struct_22 *v12;  // x8
    unsigned int v13;  // s0
    unsigned long v15;  // 4125
    unsigned long v16;  // 4125
    char v17[690];  // x8
    struct_24 *v18;  // x9
    unsigned long v19;  // 4129
    unsigned long v2;  // x9
    struct_25 *ptr6;  // x8
    unsigned int v21;  // w10
    unsigned int v22;  // w9
    struct_25 *v23;  // x8
    struct_12 *v24;  // x8
    struct_25 *v25;  // x8
    unsigned int v26;  // w9
    struct_13 *v27;  // x8
    struct_25 *v28;  // x8
    unsigned long v29;  // x9
    struct_1 *v3;  // x8
    struct_14 *v30;  // x8
    struct_4 *v31;  // x1
    struct_4 *idx7;  // x8
    unsigned int v33;  // w9
    unsigned int v34;  // w1
    unsigned long v35;  // x0
    void* v37;  // x22
    void* ptr5;  // x22
    unsigned int v39;  // w8
    long long v4;  // x0
    unsigned int v40;  // w1
    struct_24 *v42;  // x8
    struct_22 *v43;  // x8
    unsigned long v44;  // 4129
    struct_22 *ptr7;  // x8
    unsigned long long v46;  // x1
    unsigned long v47;  // 4125
    struct_24 *ptr8;  // x8
    unsigned long v49;  // 4129
    void* ptr4;  // x20
    unsigned long v50;  // 4125
    void* p;  // x8
    unsigned int v52;  // w9
    unsigned long long v53;  // x20
    struct_15 *v54;  // x8
    unsigned int v55;  // w9
    unsigned int v56;  // w21
    struct_16 *v57;  // x8
    void* v6;  // x20
    struct_17 *v58;  // x8
    unsigned long long v59;  // x20
    void* v60;  // x8
    struct_18 *v61;  // x8
    void* ptr9;  // x8
    unsigned int v63;  // w21
    unsigned long v64;  // 4119
    unsigned int v65;  // w21
    struct_19 *v66;  // x8
    struct_22 *v7;  // x20
    unsigned long v68;  // 4113
    void* ptr10;  // x8
    unsigned long v71;  // x20
    unsigned long v72;  // 4119
    struct_20 *v73;  // x8
    unsigned long v75;  // 4113
    unsigned int v8;  // s1
    struct_24 *v77;  // x8
    void* ptr11;  // x0
    unsigned int v79;  // w1
    unsigned int v81;  // s1
    unsigned int v82;  // s9
    unsigned long v83;  // 4153
    char v84;  // x8
    unsigned long v85;  // 4138
    unsigned int v86;  // s1
    unsigned long addr;  // x9
    unsigned long v87;  // 4149
    char v88;  // x8
    unsigned int v89;  // w8
    unsigned long v90;  // 4131
    struct_26 *v91;  // x8
    struct_21 *v92;  // x0
    struct_26 *v93;  // x8
    struct_26 *v94;  // x8
    struct_21 *v95;  // x0

    if (!(g_1fab4d5 & 1))
    {
        sub_f7d92c(&g_1efd070);
        sub_f7d92c(&g_1efeb28);
        sub_f7d92c(&g_1efed18);
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c(&g_1f08dd0);
        sub_f7d92c(&g_1f0ae78);
        sub_f7d92c(&g_1f0c5b0);
        g_1fab4d5 = 1;
    }
    if (!(char)ptr[306])
    {
LABEL_10b29fc:
        if ((char)ptr[381])
        {
            MonoBehaviour__StartCoroutine(ptr, PlayerWeapons__SelectWeapon(ptr, (int)ptr[376], 0, 1), 0);
            *((unsigned short *)&ptr[380]) = 0;
            *((char *)&ptr[382]) = 0;
        }
        Time__get_timeSinceLevelLoad(0);
        v15 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v13, 0x40000000)) >> 5 & 3 | (unsigned long long)(CmpF(v13, 0x40000000) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v13, 0x40000000)) >> 5 & 3 | (unsigned long long)(CmpF(v13, 0x40000000) & 1)) & ((unsigned long long)(char)(CmpF(v13, 0x40000000)) >> 5 & 3 | (unsigned long long)(CmpF(v13, 0x40000000) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if (!((char)v15) && !((v0 = (struct_21 *)(unsigned long long)Time__get_timeScale(0), v16 = (unsigned long)arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v13, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v13, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v13, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v13, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v13, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v13, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0), (char)v16)))
        {
            v17 = (long long)ptr[136];
            if (v17)
            {
                if (!v17[552] && v17[689] || (char)ptr[296])
                    goto LABEL_10b2d18;
                v18 = (long long)ptr[128];
                if (v18)
                {
                    if (v18->field_99)
                        goto LABEL_10b2d18;
                    if ((long long)ptr[152])
                    {
                        if (*((char *)((long long)ptr[152] + 933)))
                        {
                            if ((long long)ptr[144])
                            {
                                v13 = *((int *)((long long)ptr[144] + 524));
                                v19 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v13, 0x3f800000)) >> 5 & 3 | (unsigned long long)(CmpF(v13, 0x3f800000) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v13, 0x3f800000)) >> 5 & 3 | (unsigned long long)(CmpF(v13, 0x3f800000) & 1)) & ((unsigned long long)(char)(CmpF(v13, 0x3f800000)) >> 5 & 3 | (unsigned long long)(CmpF(v13, 0x3f800000) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                                if (!((char)v19))
                                    goto LABEL_10b2aa4;
                                goto LABEL_10b2d18;
                            }
                        }
                        else
                        {
LABEL_10b2aa4:
                            if (v17[408])
                                goto LABEL_10b2d18;
                            if (!v18->field_aa || (char)ptr[297])
                            {
LABEL_10b2abc:
                                v37 = ptr;
                                ptr5 = v37 + 220;
                                if ((int)v37[220] != (int)ptr5[8])
                                {
                                    if ((long long)ptr[384])
                                    {
                                        if (*((int *)((long long)ptr[384] + 296)) < 1 || (char)ptr[297])
                                            goto LABEL_10b2aec;
                                        if ((long long)ptr[128])
                                        {
                                            if (!*((char *)((long long)ptr[128] + 155)) || (char)ptr[380])
                                                goto LABEL_10b2aec;
                                            if ((long long)ptr[168])
                                            {
                                                if (*((char *)((long long)ptr[168] + 421)))
                                                    goto LABEL_10b2aec;
                                                if ((long long)ptr[152])
                                                {
                                                    WeaponBehavior__CancelWeaponPull((long long)ptr[152], 0);
                                                    v39 = (int)ptr[220];
                                                    v40 = (int)ptr[212];
                                                    *((char *)&ptr[382]) = 1;
                                                    *((unsigned int *)&ptr[376]) = v39;
                                                    MonoBehaviour__StartCoroutine(ptr, PlayerWeapons__SelectWeapon(ptr, v40, 1, 0), 0);
                                                    *((unsigned short *)&ptr[380]) = 1;
                                                    goto LABEL_10b2aec;
                                                }
                                            }
                                        }
                                    }
                                }
                                else
                                {
LABEL_10b2aec:
                                    if ((char)ptr[304])
                                        goto LABEL_10b2d18;
                                    v42 = (long long)ptr[128];
                                    if (v42)
                                    {
                                        if ((v42->field_a0 || v42->field_f3) && *((int *)ptr5) && !(char)ptr[380])
                                        {
                                            if ((long long)ptr[136])
                                            {
                                                if (*((char *)((long long)ptr[136] + 689)))
                                                    goto LABEL_10b2b2c;
                                                v43 = (long long)ptr[152];
                                                if (v43 && v43->field_122 && !v43->field_25d)
                                                {
                                                    PlayerWeapons__DropWeapon(ptr);
                                                    goto LABEL_10b2b2c;
                                                }
                                            }
                                        }
                                        else
                                        {
LABEL_10b2b2c:
                                            if ((long long)ptr[144])
                                            {
                                                v13 = *((int *)((long long)ptr[144] + 524));
                                                v44 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v13, 0x3f800000)) >> 5 & 3 | (unsigned long long)(CmpF(v13, 0x3f800000) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v13, 0x3f800000)) >> 5 & 3 | (unsigned long long)(CmpF(v13, 0x3f800000) & 1)) & ((unsigned long long)(char)(CmpF(v13, 0x3f800000)) >> 5 & 3 | (unsigned long long)(CmpF(v13, 0x3f800000) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                                                if (!((char)v44) && !(char)ptr[313])
                                                {
                                                    ptr7 = (long long)ptr[152];
                                                    if (ptr7)
                                                    {
                                                        ptr7->field_122 = 1;
                                                        if (!g_1ef0c58->field_e0)
                                                            sub_f7da5c(g_1ef0c58);
                                                        if (((char)Object__op_Implicit(*((long long *)&ptr7->padding_3a6[158]), 0) & 1))
                                                        {
                                                            if ((long long)ptr[152] && *((long long *)((long long)ptr[152] + 1096)) && sub_1231bc8(*((long long *)((long long)ptr[152] + 1096)), g_1efd070))
                                                            {
                                                                Renderer__set_enabled();
                                                                goto LABEL_10b2bb8;
                                                            }
                                                        }
                                                        else
                                                        {
LABEL_10b2bb8:
                                                            v46 = (int)ptr[220];
                                                            *((char *)&ptr[313]) = 1;
                                                            PlayerWeapons__DropWeapon(ptr, v46);
                                                            goto LABEL_10b2bcc;
                                                        }
                                                    }
                                                }
                                                else
                                                {
LABEL_10b2bcc:
                                                    v0 = Time__get_timeScale(0);
                                                    v47 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v13, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v13, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v13, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v13, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v13, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v13, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                                                    if (!((char)v47))
                                                    {
                                                        ptr8 = (long long)ptr[128];
                                                        if (ptr8)
                                                        {
                                                            v13 = ptr8->field_b8;
                                                            v49 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v13, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v13, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v13, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v13, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v13, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v13, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                                                            if (!((char)v49))
                                                            {
                                                                if ((long long)ptr[168])
                                                                {
                                                                    if (!*((char *)((long long)ptr[168] + 421)))
                                                                        goto LABEL_10b2c10;
                                                                    goto LABEL_10b2c00;
                                                                }
                                                            }
                                                            else
                                                            {
LABEL_10b2c00:
                                                                if (ptr8->field_a9 || ptr8->field_f0)
                                                                {
LABEL_10b2c10:
                                                                    v59 = *((int *)ptr5);
                                                                    if ((unsigned int)v59)
                                                                    {
                                                                        if ((v59 >> 31 & 1))
                                                                            goto LABEL_10b3358;
                                                                        while (true)
                                                                        {
                                                                            v53 = v59;
                                                                            v60 = (long long)ptr[232];
                                                                            if (!v60)
                                                                                break;
                                                                            if ((int)v60[24] <= (unsigned int)v53)
                                                                                sub_f7db7c(v0);
                                                                            v61 = v60 + (v53 & 4294967295) * 8;
                                                                            if (!v61->field_20 || !((v0 = (struct_21 *)sub_1249224(v61->field_20, g_1efed18), v0)))
                                                                                break;
                                                                            if (v0->field_120 && v0->field_121 && (unsigned int)v53 != *((int *)ptr5))
                                                                                goto LABEL_10b3334;
                                                                            if ((unsigned int)v53)
                                                                            {
LABEL_10b2c70:
                                                                                v59 = (unsigned int)v53 - 1;
                                                                                if (0 >= (unsigned int)v53)
                                                                                    goto LABEL_10b3358;
                                                                            }
                                                                            else
                                                                            {
                                                                                ptr9 = (long long)ptr[232];
                                                                                if (!ptr9)
                                                                                    break;
                                                                                v63 = (int)ptr9[24] - 1;
                                                                                v64 = arm64g_calculate_condition(67, (unsigned long long)(unsigned int)(int)ptr9[24], 1, 0);
                                                                                if ((char)v64)
                                                                                    goto LABEL_10b3358;
                                                                                while (true)
                                                                                {
                                                                                    v65 = v63;
                                                                                    if ((int)ptr9[24] <= v65)
                                                                                        sub_f7db7c(v0);
                                                                                    v66 = ptr9 + v65 * 8;
                                                                                    if (!v66->field_20 || !((v0 = (struct_21 *)sub_1249224(v66->field_20, g_1efed18), v0)))
                                                                                        break;
                                                                                    if (!v0->field_120 || !v0->field_121 || v65 == *((int *)ptr5))
                                                                                    {
                                                                                        v68 = arm64g_calculate_condition(67, (unsigned long long)v65, 1, 0);
                                                                                        if ((char)v68)
                                                                                            goto LABEL_10b2c70;
                                                                                        ptr9 = (long long)ptr[232];
                                                                                        v63 = v65 - 1;
                                                                                        if (!ptr9)
                                                                                            break;
                                                                                    }
                                                                                    else
                                                                                    {
                                                                                        v0 = MonoBehaviour__StartCoroutine(ptr, PlayerWeapons__SelectWeapon(ptr, v65, 0, 0), 0);
                                                                                        goto LABEL_10b2c70;
                                                                                    }
                                                                                }
                                                                            }
                                                                        }
                                                                    }
                                                                    else
                                                                    {
                                                                        ptr10 = (long long)ptr[232];
                                                                        if (ptr10)
                                                                        {
                                                                            v71 = (int)ptr10[24] - 1;
                                                                            v72 = arm64g_calculate_condition(67, (unsigned long long)(unsigned int)(int)ptr10[24], 1, 0);
                                                                            if ((char)v72)
                                                                                goto LABEL_10b3358;
                                                                            while (true)
                                                                            {
                                                                                v53 = v71;
                                                                                if ((int)ptr10[24] <= (unsigned int)v53)
                                                                                    sub_f7db7c(v0);
                                                                                v73 = ptr10 + (v53 & 4294967295) * 8;
                                                                                if (!v73->field_20 || !((v0 = (struct_21 *)sub_1249224(v73->field_20, g_1efed18), v0)))
                                                                                    break;
                                                                                if (v0->field_120 && v0->field_121 && (unsigned int)v53 != *((int *)ptr5))
                                                                                    goto LABEL_10b3334;
                                                                                v75 = arm64g_calculate_condition(67, v53 & 4294967295, 1, 0);
                                                                                if ((char)v75)
                                                                                    goto LABEL_10b3358;
                                                                                ptr10 = (long long)ptr[232];
                                                                                v71 = (unsigned int)v53 - 1;
                                                                                if (!ptr10)
                                                                                    break;
                                                                            }
                                                                            goto LABEL_10b3358;
                                                                        }
                                                                    }
                                                                }
                                                                else
                                                                {
                                                                    v50 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v13, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v13, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v13, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v13, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v13, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v13, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                                                                    if (!((char)v50))
                                                                    {
                                                                        if ((long long)ptr[168])
                                                                        {
                                                                            if (!*((char *)((long long)ptr[168] + 421)))
                                                                                goto LABEL_10b311c;
                                                                            goto LABEL_10b310c;
                                                                        }
                                                                    }
                                                                    else
                                                                    {
LABEL_10b310c:
                                                                        if (!ptr8->field_a8 && !ptr8->field_f1 && (!(char)ptr[312] || !(int)ptr[216]))
                                                                            goto LABEL_10b3358;
LABEL_10b311c:
                                                                        p = (long long)ptr[232];
                                                                        if (p)
                                                                        {
                                                                            v52 = (long long)p[24];
                                                                            v53 = (int)ptr[220];
                                                                            if (v52 - 1 > (unsigned int)v53)
                                                                            {
                                                                                if (v52 <= (unsigned int)v53)
                                                                                    goto LABEL_10b3358;
                                                                                while (true)
                                                                                {
                                                                                    if (v52 <= (unsigned int)v53)
                                                                                        sub_f7db7c(v0);
                                                                                    v54 = p + (v53 & 4294967295) * 8;
                                                                                    if (!v54->field_20 || !((v0 = (struct_21 *)sub_1249224(v54->field_20, g_1efed18), v0)))
                                                                                        break;
                                                                                    if (v0->field_120 && v0->field_121 && ((unsigned int)v53 != *((int *)ptr5) && !(char)ptr[312] || (unsigned int)v53 != *((int *)ptr5) && (unsigned int)v53 != (int)ptr[208] && (char)ptr[312]))
                                                                                        goto LABEL_10b3334;
                                                                                    p = (long long)ptr[232];
                                                                                    if (!p)
                                                                                        break;
                                                                                    v55 = (long long)p[24];
                                                                                    if ((unsigned int)v53 == v55 - 1 && v55 - 1 >= 1)
                                                                                    {
                                                                                        v56 = 0;
                                                                                        while (true)
                                                                                        {
                                                                                            if (v55 <= v56)
                                                                                                sub_f7db7c(v0);
                                                                                            v57 = p + v56 * 8;
                                                                                            if (!v57->field_20 || !((v0 = (struct_21 *)sub_1249224(v57->field_20, g_1efed18), v0)))
                                                                                                break;
                                                                                            if (!v0->field_120 || !v0->field_121 || (v56 == *((int *)ptr5) || (char)ptr[312]) && (v56 == *((int *)ptr5) || v56 == (int)ptr[208] || !(char)ptr[312]))
                                                                                            {
                                                                                                p = (long long)ptr[232];
                                                                                                if (!p)
                                                                                                    break;
                                                                                                v55 = (int)p[24];
                                                                                                v56 += 1;
                                                                                            }
                                                                                            else
                                                                                            {
                                                                                                v0 = MonoBehaviour__StartCoroutine(ptr, PlayerWeapons__SelectWeapon(ptr, v56, 0, 0), 0);
                                                                                                if (!(long long)ptr[232])
                                                                                                    break;
                                                                                                goto LABEL_10b3284;
                                                                                            }
                                                                                        }
                                                                                        break;
                                                                                    }
LABEL_10b3284:
                                                                                    v52 = (int)p[24];
                                                                                    v53 = (unsigned int)v53 + 1;
                                                                                    goto LABEL_10b3358;
                                                                                }
                                                                            }
                                                                            else
                                                                            {
                                                                                if (v52 - 1 < 1)
                                                                                    goto LABEL_10b3358;
                                                                                v53 = 0;
                                                                                while (true)
                                                                                {
                                                                                    if (v52 <= (unsigned int)v53)
                                                                                        sub_f7db7c(v0);
                                                                                    v58 = p + (v53 & 4294967295) * 8;
                                                                                    if (!v58->field_20 || !((v0 = (struct_21 *)sub_1249224(v58->field_20, g_1efed18), v0)))
                                                                                        break;
                                                                                    if (!v0->field_120 || !v0->field_121 || ((unsigned int)v53 == *((int *)ptr5) || (char)ptr[312]) && ((unsigned int)v53 == *((int *)ptr5) || (unsigned int)v53 == (int)ptr[208] || !(char)ptr[312]))
                                                                                    {
                                                                                        p = (long long)ptr[232];
                                                                                        if (!p)
                                                                                            break;
                                                                                        v52 = (int)p[24];
                                                                                        v53 = (unsigned int)v53 + 1;
                                                                                        goto LABEL_10b3358;
                                                                                    }
                                                                                    else
                                                                                    {
LABEL_10b3334:
                                                                                        MonoBehaviour__StartCoroutine(ptr, PlayerWeapons__SelectWeapon(ptr, v53, 0, 0), 0);
                                                                                        goto LABEL_10b3358;
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
LABEL_10b3358:
                                                        v77 = (long long)ptr[128];
                                                        if (v77)
                                                        {
                                                            if (v77->field_9f && *((int *)ptr5))
                                                            {
                                                                ptr11 = ptr;
                                                                v79 = 0;
                                                                goto LABEL_10b3550;
                                                            }
                                                            if (v77->field_ab)
                                                            {
                                                                if ((long long)ptr[232])
                                                                {
                                                                    if (*((int *)((long long)ptr[232] + 24)) - 1 < 1)
                                                                        goto LABEL_10b33b0;
                                                                    if (*((int *)ptr5) != 1)
                                                                    {
                                                                        v79 = 1;
                                                                        goto LABEL_10b354c;
                                                                    }
                                                                }
                                                            }
                                                            else
                                                            {
LABEL_10b33b0:
                                                                if (v77->field_ac)
                                                                {
                                                                    if ((long long)ptr[232])
                                                                    {
                                                                        if (2 > *((int *)((long long)ptr[232] + 24)) - 1)
                                                                            goto LABEL_10b33d0;
                                                                        if (*((int *)ptr5) != 2)
                                                                        {
                                                                            v79 = 2;
                                                                            goto LABEL_10b354c;
                                                                        }
                                                                    }
                                                                }
                                                                else
                                                                {
LABEL_10b33d0:
                                                                    if (v77->field_ad)
                                                                    {
                                                                        if ((long long)ptr[232])
                                                                        {
                                                                            if (3 > *((int *)((long long)ptr[232] + 24)) - 1)
                                                                                goto LABEL_10b33f0;
                                                                            if (*((int *)ptr5) != 3)
                                                                            {
                                                                                v79 = 3;
                                                                                goto LABEL_10b354c;
                                                                            }
                                                                        }
                                                                    }
                                                                    else
                                                                    {
LABEL_10b33f0:
                                                                        if (v77->field_ae)
                                                                        {
                                                                            if ((long long)ptr[232])
                                                                            {
                                                                                if (4 > *((int *)((long long)ptr[232] + 24)) - 1)
                                                                                    goto LABEL_10b3410;
                                                                                if (*((int *)ptr5) != 4)
                                                                                {
                                                                                    v79 = 4;
                                                                                    goto LABEL_10b354c;
                                                                                }
                                                                            }
                                                                        }
                                                                        else
                                                                        {
LABEL_10b3410:
                                                                            if (v77->field_af)
                                                                            {
                                                                                if ((long long)ptr[232])
                                                                                {
                                                                                    if (5 > *((int *)((long long)ptr[232] + 24)) - 1)
                                                                                        goto LABEL_10b3430;
                                                                                    if (*((int *)ptr5) != 5)
                                                                                    {
                                                                                        v79 = 5;
                                                                                        goto LABEL_10b354c;
                                                                                    }
                                                                                }
                                                                            }
                                                                            else
                                                                            {
LABEL_10b3430:
                                                                                if (v77->field_b0)
                                                                                {
                                                                                    if ((long long)ptr[232])
                                                                                    {
                                                                                        if (6 > *((int *)((long long)ptr[232] + 24)) - 1)
                                                                                            goto LABEL_10b3450;
                                                                                        if (*((int *)ptr5) != 6)
                                                                                        {
                                                                                            v79 = 6;
                                                                                            goto LABEL_10b354c;
                                                                                        }
                                                                                    }
                                                                                }
                                                                                else
                                                                                {
LABEL_10b3450:
                                                                                    if (v77->field_b1)
                                                                                    {
                                                                                        if ((long long)ptr[232])
                                                                                        {
                                                                                            if (7 > *((int *)((long long)ptr[232] + 24)) - 1)
                                                                                                goto LABEL_10b3470;
                                                                                            if (*((int *)ptr5) != 7)
                                                                                            {
                                                                                                v79 = 7;
                                                                                                goto LABEL_10b354c;
                                                                                            }
                                                                                        }
                                                                                    }
                                                                                    else
                                                                                    {
LABEL_10b3470:
                                                                                        if (v77->field_b2)
                                                                                        {
                                                                                            if ((long long)ptr[232])
                                                                                            {
                                                                                                if (8 > *((int *)((long long)ptr[232] + 24)) - 1)
                                                                                                    goto LABEL_10b3490;
                                                                                                if (*((int *)ptr5) != 8)
                                                                                                {
                                                                                                    v79 = 8;
LABEL_10b354c:
                                                                                                    ptr11 = ptr;
LABEL_10b3550:
                                                                                                    MonoBehaviour__StartCoroutine(ptr, PlayerWeapons__SelectWeapon(ptr11, v79, 0, 0), 0);
                                                                                                    goto LABEL_10b2d18;
                                                                                                }
                                                                                            }
                                                                                        }
                                                                                        else
                                                                                        {
LABEL_10b3490:
                                                                                            if (!v77->field_b3)
                                                                                                goto LABEL_10b2d18;
                                                                                            if ((long long)ptr[232] && *((int *)((long long)ptr[232] + 24)) - 1 >= 9 && *((int *)ptr5) != 9)
                                                                                            {
                                                                                                v79 = 9;
                                                                                                goto LABEL_10b354c;
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
                                ptr6 = (long long)ptr[248];
                                if (ptr6)
                                {
                                    v21 = *((int *)&ptr6->padding_0[24]);
                                    v22 = (int)ptr[224] + 1;
                                    if (v22 > v21 - 1)
                                    {
                                        if (!v21)
                                            sub_f7db7c(v0);
                                        if (ptr6->field_20 && (v0 = (struct_21 *)sub_1249224(ptr6->field_20, g_1efed18), v0))
                                        {
                                            if (!v0->field_120)
                                                goto LABEL_10b2f9c;
                                            v23 = (long long)ptr[248];
                                            if (v23)
                                            {
                                                if (!*((int *)&v23->padding_0[24]))
                                                    sub_f7db7c(v0);
                                                if (v23->field_20 && (v0 = (struct_21 *)sub_1249224(v23->field_20, g_1efed18), v0) && v0->field_128 >= 1)
                                                {
                                                    *((unsigned int *)&ptr[224]) = 0;
                                                    goto LABEL_10b2f9c;
                                                }
                                            }
                                        }
                                    }
                                    else
                                    {
                                        if (v21 <= v22)
                                            sub_f7db7c(v0);
                                        v24 = &ptr6->padding_0[8 * v22];
                                        if (v24->field_20 && (v0 = (struct_21 *)sub_1249224(v24->field_20, g_1efed18), v0))
                                        {
                                            if (v0->field_120)
                                            {
                                                v25 = (long long)ptr[248];
                                                if (v25)
                                                {
                                                    v26 = (int)ptr[224] + 1;
                                                    if (*((int *)&v25->padding_0[24]) <= v26)
                                                        sub_f7db7c(v0);
                                                    v27 = &v25->padding_0[8 * v26];
                                                    if (v27->field_20 && (v0 = (struct_21 *)sub_1249224(v27->field_20, g_1efed18), v0) && v0->field_128 >= 1)
                                                    {
                                                        *((unsigned int *)&ptr[224]) = (int)ptr[224] + 1;
                                                        goto LABEL_10b2f9c;
                                                    }
                                                }
                                            }
                                            else
                                            {
LABEL_10b2f9c:
                                                v28 = (long long)ptr[248];
                                                if (v28)
                                                {
                                                    v29 = (int)ptr[224];
                                                    if (*((int *)&v28->padding_0[24]) <= (unsigned int)v29)
                                                        sub_f7db7c(v0);
                                                    v30 = &v28->padding_0[8 * v29];
                                                    if (v30->field_20)
                                                    {
                                                        v31 = sub_1249224(v30->field_20, g_1efed18);
                                                        *((struct_4 **)&ptr[384]) = v31;
                                                        sub_f7d8d0(ptr + 384, v31);
                                                        idx7 = (long long)ptr[384];
                                                        if (idx7 && idx7->field_120 && idx7->field_128 >= 1)
                                                        {
                                                            v33 = (int)ptr[220];
                                                            *((unsigned int *)&ptr[212]) = idx7->field_124;
                                                            *((unsigned int *)&ptr[376]) = v33;
                                                            *((char *)&ptr[297]) = 1;
                                                            Time__get_time(0);
                                                            v34 = (int)ptr[212];
                                                            *((unsigned int *)&ptr[300]) = v13;
                                                            v35 = PlayerWeapons__SelectWeapon(ptr, v34, 1, 0);
                                                            MonoBehaviour__StartCoroutine(ptr, v35, 0);
                                                            MonoBehaviour__StartCoroutine(ptr, PlayerWeapons__DisplayGrenadeSwitch(), 0);
                                                            goto LABEL_10b2abc;
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
LABEL_10b2d18:
            Time__get_time(0);
            v81 = (int)ptr[288] + 1063172178;
            v82 = (int)ptr[300];
            v83 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v81, v13)) >> 5 & 3 | (unsigned long long)(CmpF(v81, v13) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v81, v13)) >> 5 & 3 | (unsigned long long)(CmpF(v81, v13) & 1)) & ((unsigned long long)(char)(CmpF(v81, v13)) >> 5 & 3 | (unsigned long long)(CmpF(v81, v13) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
            if ((char)v83)
                v84 = 0;
            else
                v84 = 1;
            *((char *)&ptr[296]) = v84;
            Time__get_time();
            v85 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v82 + 0x40000000, v13)) >> 5 & 3 | (unsigned long long)(CmpF(v82 + 0x40000000, v13) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v82 + 0x40000000, v13)) >> 5 & 3 | (unsigned long long)(CmpF(v82 + 0x40000000, v13) & 1)) & ((unsigned long long)(char)(CmpF(v82 + 0x40000000, v13)) >> 5 & 3 | (unsigned long long)(CmpF(v82 + 0x40000000, v13) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
            if (!((char)v85))
                *((char *)&ptr[297]) = 0;
            Time__get_time(0);
            v86 = (int)ptr[292] + 1054951342;
            v87 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v86, v13)) >> 5 & 3 | (unsigned long long)(CmpF(v86, v13) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v86, v13)) >> 5 & 3 | (unsigned long long)(CmpF(v86, v13) & 1)) & ((unsigned long long)(char)(CmpF(v86, v13)) >> 5 & 3 | (unsigned long long)(CmpF(v86, v13) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
            if ((char)v87)
                v88 = 0;
            else
                v88 = 1;
            *((char *)&ptr[304]) = v88;
            v0 = Time__get_timeScale();
            v89 = (char)ptr[328];
            v90 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v13, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v13, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v13, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v13, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v13, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v13, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
            if (!((char)v90))
            {
                if (v89)
                {
                    v91 = (long long)ptr[336];
                    if (v91)
                    {
                        if (v91->field_18 > 1)
                        {
                            if (v91->field_28)
                            {
                                v92 = AudioSource__Play(v91->field_28, 0);
                                *((char *)&ptr[328]) = 0;
                                return v92;
                            }
                        }
                        else
                        {
                            sub_f7db7c(v0);
                        }
                    }
                }
                else
                {
                    return v0;
                }
            }
            else
            {
                if (!v89)
                {
                    v93 = (long long)ptr[336];
                    if (v93)
                    {
                        if (v93->field_18 > 1)
                        {
                            if (v93->field_28)
                            {
                                v0 = AudioSource__get_isPlaying(v93->field_28, 0);
                                if (!((char)v0 & 1))
                                    return v0;
                                v94 = (long long)ptr[336];
                                if (v94)
                                {
                                    if (v94->field_18 > 1)
                                    {
                                        if (v94->field_28)
                                        {
                                            v95 = AudioSource__Pause(v94->field_28, 0);
                                            *((char *)&ptr[328]) = 1;
                                            return v95;
                                        }
                                    }
                                    else
                                    {
                                        sub_f7db7c(v0);
                                    }
                                }
                            }
                        }
                        else
                        {
                            sub_f7db7c(v0);
                        }
                    }
                }
                else
                {
                    return v0;
                }
            }
        }
    }
    else if ((long long)ptr[152] && (v0 = (struct_21 *)PlayerWeapons__SelectWeapon(ptr, *((int *)((long long)ptr[152] + 292)), 0, 0), (long long)ptr[152] && (v1 = (void*)(long long)ptr[232], v1)))
    {
        v2 = *((int *)((long long)ptr[152] + 292));
        if ((int)v1[24] <= (unsigned int)v2)
            sub_f7db7c(PlayerWeapons__SelectWeapon(ptr, *((int *)((long long)ptr[152] + 292)), 0, 0));
        v3 = v1 + v2 * 8;
        if (v3->field_20)
        {
            v4 = sub_1249224(v3->field_20, g_1efeb28);
            ptr4 = ptr;
            *((long long *)&ptr4[184]) = v4;
            v6 = ptr4 + 184;
            sub_f7d8d0(v6, v4);
            if (*((long long *)v6))
            {
                Animator__SetTrigger(*((long long *)v6), g_1f0ae78, 0);
                v7 = (long long)ptr[152];
                if (!g_1fab2c9)
                {
                    sub_f7d92c(&g_1ef22e8);
                    g_1fab2c9 = 1;
                }
                if (v7)
                {
                    v8 = g_1ef22e8->field_b8->field_8;
                    addr = &(&v7->padding_25e)[1];
                    *((unsigned long long *)addr) = g_1ef22e8->field_b8->field_0;
                    *((unsigned int *)(addr + 8)) = v8;
                    ptr3 = (long long)ptr[168];
                    if (ptr3 && (v11 = g_1ef22e8->field_b8->field_8, *((unsigned long long *)&(&ptr3->padding_0)[1]) = g_1ef22e8->field_b8->field_0, *((unsigned int *)((char *)&ptr3->field_b4 + 4)) = v11, v12 = (struct_22 *)(long long)ptr[152], v12 && (1 < v12->field_134 || !v12->field_124 || v12->field_110 && (Animator__SetTrigger(v12->field_110, g_1f0c5b0, 0), v12 = (struct_22 *)(long long)ptr[152], v12)) && v12->field_118 && (v13 = 0x3f800000, Animator__set_speed(v12->field_118, 0), (long long)ptr[152] && *((long long *)((long long)ptr[152] + 280)))))
                    {
                        Animator__SetTrigger(*((long long *)((long long)ptr[152] + 280)), g_1f08dd0, 0);
                        *((char *)&ptr[306]) = 0;
                        goto LABEL_10b29fc;
                    }
                }
            }
        }
    }
    sub_f7db7c(sub_f7db74());
}
```


## `PlayerWeapons.DisplayGrenadeSwitch` — RVA `0xcb358c`

- Decompiled symbol: `PlayerWeapons_DisplayGrenadeSwitch`
- Metadata signature: `private IEnumerator DisplayGrenadeSwitch() { }`
- Native interval: `108` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[12];
    long long field_20;
} struct_0;

extern long long g_1ef36e0;
extern char g_1fab4d6;

struct_0 * PlayerWeapons_DisplayGrenadeSwitch(long long a0)
{
    struct_0 *v0;  // x20
    struct_0 *ptr;  // x0

    if (!(g_1fab4d6 & 1))
    {
        sub_f7d92c(&g_1ef36e0);
        g_1fab4d6 = 1;
    }
    v0 = sub_f7db70(g_1ef36e0);
    Object__ctor(v0, 0);
    ptr = v0;
    ptr->field_10 = 0;
    ptr->field_20 = a0;
    sub_f7d8d0(&ptr->field_20, a0);
    return ptr;
}
```


## `PlayerWeapons.DropWeapon` — RVA `0xcb3684`

- Decompiled symbol: `PlayerWeapons_DropWeapon`
- Metadata signature: `public void DropWeapon(int weapon) { }`
- Native interval: `1416` bytes
- Result: `pseudocode`
- Heuristic layout hint: `PlayerWeapons_Recovered` matched 11 offsets against `PlayerWeapons` metadata (confidence 1.00).

```c
typedef struct PlayerWeapons_Recovered {
    char padding_0[112];
    long long playerObj;
    char padding_78[16];
    struct struct_7 *FPSWalkerComponent;
    struct struct_8 *FPSPlayerComponent;
    char padding_98[16];
    struct struct_9 *CameraControlComponent;
    char padding_b0[40];
    unsigned int totalWeapons;
    char padding_dc[12];
    unsigned long long weaponOrder;
    char padding_f0[24];
    long long mainCamTransform;
    char padding_110[16];
    char switchTime;
    char padding_121[23];
    char dropWeapon;
    char deadDropped;
    char padding_13a[22];
    struct struct_10 *aSources;
} PlayerWeapons_Recovered;

typedef struct struct_1 {
    char padding_0[32];
    long long field_20;
} struct_1;

typedef struct struct_2 {
    char padding_0[32];
    long long field_20;
} struct_2;

typedef struct struct_18 {
    char padding_0[24];
    unsigned int field_18;
    char padding_1c[12];
    unsigned long long field_28;
} struct_18;

typedef struct struct_16 {
    char padding_0[196];
    unsigned int field_c4;
} struct_16;

typedef struct struct_3 {
    char padding_0[32];
    long long field_20;
} struct_3;

typedef struct struct_4 {
    char padding_0[216];
    long long field_d8;
} struct_4;

typedef struct struct_19 {
    char padding_0[262];
    char field_106;
} struct_19;

typedef struct struct_5 {
    char padding_0[32];
    long long field_20;
} struct_5;

typedef struct struct_6 {
    char padding_0[216];
    long long field_d8;
} struct_6;

typedef struct struct_14 {
    char padding_0[32];
    long long field_20;
} struct_14;

typedef struct struct_15 {
    char padding_0[288];
    char field_120;
} struct_15;

typedef struct struct_17 {
    char padding_0[524];
    unsigned int field_20c;
} struct_17;

typedef struct struct_7 {
    char padding_0[196];
    unsigned int field_c4;
} struct_7;

typedef struct struct_8 {
    char padding_0[524];
    unsigned int field_20c;
} struct_8;

typedef struct struct_9 {
    char padding_0[262];
    char field_106;
} struct_9;

typedef struct struct_10 {
    char padding_0[24];
    unsigned int field_18;
    char padding_1c[12];
    long long field_28;
} struct_10;

typedef struct struct_12 {
    char padding_0[24];
    unsigned int field_18;
} struct_12;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

typedef struct struct_13 {
    char padding_0[184];
    struct struct_12 *field_b8;
} struct_13;

extern struct_0 *g_1ef0c58;
extern struct_13 *g_1ef22e8;
extern long long g_1efeca8;
extern long long g_1efed18;
extern long long g_1f00260;
extern char g_1fab32c;
extern char g_1fab3e1;
extern char g_1fab4d7;

struct_11 * PlayerWeapons_DropWeapon(struct_11 *ptr, unsigned int a1)
{
    unsigned long v4;  // x20
    struct_11 *v5;  // x0
    int v14;  // q0
    unsigned int v15;  // w8
    unsigned long long v16;  // cc_dep1
    unsigned int v17;  // s13
    unsigned long v18;  // 4102
    unsigned long v19;  // 4102
    unsigned long v20;  // 4102
    unsigned int v21;  // w8
    unsigned int v22;  // w9
    unsigned long v23;  // x8
    struct_11 *v6;  // x0
    struct_3 *v24;  // x8
    struct_4 *v25;  // x0
    unsigned long v26;  // x9
    struct_5 *v27;  // x9
    struct_6 *p;  // x0
    long long v29;  // x20
    long long v30;  // x0
    uint128_t v31;  // q1
    unsigned long v33;  // x0
    struct_11 *addr;  // x0
    unsigned long v34;  // x21
    unsigned int v35;  // s0
    unsigned long v36;  // 4137
    unsigned int v37;  // s8
    long long v38;  // x21
    unsigned int v39;  // s0
    unsigned long v40;  // 4137
    long long v41;  // x20
    unsigned long v42;  // x8
    unsigned long v43;  // x9
    unsigned long v8;  // x8
    struct_14 *v44;  // x8
    struct_15 *v45;  // x0
    unsigned int v46;  // s0
    unsigned long v47;  // 4129
    struct_11 *ptr3;  // x0
    unsigned int v49;  // w1
    long long v50;  // x0
    unsigned long long v9;  // x23
    struct_1 *v10;  // x8
    unsigned long v11;  // x8
    struct_2 *v12;  // x8
    struct_18 *v13;  // x8
    uint128_t v0;  // [bp-0xc0]
    int v1;  // [bp-0xb0]
    unsigned long v2;  // [bp-0xa0]
    uint128_t v3;  // [bp-0x90], Other Possible Types: unsigned long

    v4 = a1;
    v5 = ptr;
    if (!(g_1fab4d7 & 1))
    {
        sub_f7d92c(&g_1efeca8);
        sub_f7d92c(&g_1efed18);
        sub_f7d92c(&g_1f00260);
        v6 = sub_f7d92c(&g_1ef0c58);
        g_1fab4d7 = 1;
        v5 = v6;
    }
    v8 = ptr->field_e8;
    if (v8)
    {
        if (*((int *)(v8 + 24)) <= (unsigned int)v4)
            sub_f7db7c(v5);
        v9 = v4 * 0x100000000 >> 63 & 0xffffffff00000000 | v4 & 4294967295;
        v10 = v8 + v9 * 8;
        if (v10->field_20 && (addr = (struct_11 *)sub_1249224(v10->field_20, g_1efed18), addr))
        {
            if (!addr->field_120)
                return addr;
            v11 = ptr->field_e8;
            if (v11)
            {
                if (*((int *)(v11 + 24)) <= (unsigned int)v4)
                    sub_f7db7c(addr);
                v12 = v11 + v9 * 8;
                if (v12->field_20 && (addr = (struct_11 *)sub_1249224(v12->field_20, g_1efed18), addr && (addr->field_120 = 0, v13 = (struct_18 *)ptr->field_150, v13)))
                {
                    if (v13->field_18 <= 1)
                        sub_f7db7c(addr);
                    if (v13->field_28 && (AudioSource__Stop(v13->field_28, 0), ptr->field_88))
                    {
                        v14 = (int)ptr->field_88->field_c4;
                        v15 = ptr->field_139;
                        v16 = ((((CmpF(*((unsigned int *)&v14), 0.0) >> 5 & 3 | CmpF(*((unsigned int *)&v14), 0.0) & 1) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - ((CmpF(*((unsigned int *)&v14), 0.0) >> 5 & 3 | CmpF(*((unsigned int *)&v14), 0.0) & 1) & (CmpF(*((unsigned int *)&v14), 0.0) >> 5 & 3 | CmpF(*((unsigned int *)&v14), 0.0) & 1) >> 1 & 1)) * 0x10000000;
                        if (v15)
                        {
                            v17 = 0x40800000;
                            v18 = arm64g_calculate_condition(192, v16, 0, 0);
                            if (!((char)v18))
                                v17 = 0x40000000;
                        }
                        else
                        {
                            v17 = 0x41000000;
                            v19 = arm64g_calculate_condition(192, v16, 0, 0);
                            if (!((char)v19))
                            {
                                v17 = 0x40000000;
                                v20 = arm64g_calculate_condition(64, v16, 0, 0);
                                if (!((char)v20))
                                    v17 = 0x40800000;
                            }
                        }
                        if (v15)
                            v21 = 0;
                        else
                            v21 = 1;
                        if (*((int *)&ptr->padding_dc[0]) != *((int *)&ptr->padding_b0[32]))
                            v22 = 0;
                        else
                            v22 = 1;
                        if (*((int *)&ptr->padding_dc[0]) && !(v21 & v22 & 1))
                            ptr->field_138 = 1;
                        addr = PlayerWeapons__UpdateTotalWeapons(ptr);
                        v23 = ptr->field_e8;
                        if (v23)
                        {
                            if (*((int *)(v23 + 24)) <= (unsigned int)v4)
                                sub_f7db7c(addr);
                            v24 = v23 + v9 * 8;
                            if (v24->field_20 && (v25 = (struct_4 *)sub_1249224(v24->field_20, g_1efed18), v25))
                            {
                                if (!g_1ef0c58->field_e0)
                                    sub_f7da5c(g_1ef0c58);
                                addr = Object__op_Implicit(v25->field_d8, 0);
                                if (!((char)addr & 1))
                                {
LABEL_10b3b18:
                                    if (ptr->field_139)
                                    {
LABEL_10b3b20:
                                        ptr3 = ptr;
                                        v49 = 0;
                                        goto LABEL_10b3b28;
                                    }
                                    else
                                    {
                                        if (ptr->field_d8)
                                            return addr;
                                        if (!*((int *)&ptr->padding_dc[0]))
                                            return addr;
                                        v42 = *((int *)&ptr->padding_b0[32]);
                                        if (*((int *)&ptr->padding_dc[0]) == (unsigned int)v42)
                                            return addr;
                                        v43 = ptr->field_e8;
                                        if (v43)
                                        {
                                            if (*((int *)(v43 + 24)) <= (unsigned int)v42)
                                                sub_f7db7c(addr);
                                            v44 = v43 + v42 * 8;
                                            if (v44->field_20 && (v45 = (struct_15 *)sub_1249224(v44->field_20, g_1efed18), v45))
                                            {
                                                if (!v45->field_120)
                                                    goto LABEL_10b3b20;
                                                if (ptr->field_90)
                                                {
                                                    v46 = ptr->field_90->field_20c;
                                                    v47 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v46, 0x3f800000)) >> 5 & 3 | (unsigned long long)(CmpF(v46, 0x3f800000) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v46, 0x3f800000)) >> 5 & 3 | (unsigned long long)(CmpF(v46, 0x3f800000) & 1)) & ((unsigned long long)(char)(CmpF(v46, 0x3f800000)) >> 5 & 3 | (unsigned long long)(CmpF(v46, 0x3f800000) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                                                    if (!((char)v47))
                                                    {
                                                        v49 = *((int *)&ptr->padding_b0[32]);
                                                        ptr3 = ptr;
LABEL_10b3b28:
                                                        PlayerWeapons__SelectWeapon(ptr3, v49, 0, 0);
                                                        v50 = MonoBehaviour__StartCoroutine();
                                                        return MonoBehaviour__StartCoroutine();
                                                    }
                                                    goto LABEL_10b3b20;
                                                }
                                            }
                                        }
                                    }
                                }
                                else if (ptr->field_a8 && (v26 = (unsigned long)ptr->field_e8, v26))
                                {
                                    if (*((int *)(v26 + 24)) <= (unsigned int)v4)
                                        sub_f7db7c(addr);
                                    v27 = v26 + v9 * 8;
                                    if (v27->field_20 && (p = (struct_6 *)sub_1249224(v27->field_20, g_1efed18), p))
                                    {
                                        v29 = p->field_d8;
                                        if (!ptr->field_a8->field_106)
                                        {
                                            v30 = ptr->field_108;
                                            if (v30)
                                            {
LABEL_10b38c0:
                                                Transform__get_position(v30, 0);
                                                v3 = *((unsigned long long *)&v14);
                                                v2 = v31;
                                                if (ptr->field_70 && GameObject__get_transform(ptr->field_70, 0))
                                                {
                                                    Transform__get_forward();
                                                    if (!g_1fab32c)
                                                    {
                                                        v0 = v31;
                                                        v1 = v14;
                                                        sub_f7d92c(&g_1ef22e8);
                                                        g_1fab32c = 1;
                                                    }
                                                    if (ptr->field_108)
                                                    {
                                                        v3 = [D] unsupported_Iop_ZeroHI64ofV128();
                                                        Transform__get_rotation(ptr->field_108, 0);
                                                        if (!g_1ef0c58->field_e0)
                                                            sub_f7da5c(g_1ef0c58);
                                                        if (sub_112a1ac(v29, g_1f00260) && (v33 = (unsigned long)sub_1249224(), ptr->field_70 && (v34 = (unsigned long)sub_1249224(), GameObject__get_transform(ptr->field_70, 0) && (Transform__get_forward(), v34))))
                                                        {
                                                            v35 = v17 * (unsigned int)v3;
                                                            Rigidbody__AddForce(v34, 1, 0);
                                                            Random__get_value(0);
                                                            v36 = arm64g_calculate_condition(192, (((((unsigned long long)(char)(CmpF(v35, 0x3f000000)) >> 5 & 3 | (unsigned long long)(CmpF(v17 * (unsigned int)v3, 0x3f000000) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v17 * (unsigned int)v3, 0x3f000000)) >> 5 & 3 | (unsigned long long)(CmpF(v17 * (unsigned int)v3, 0x3f000000) & 1)) & ((unsigned long long)(char)(CmpF(v17 * (unsigned int)v3, 0x3f000000)) >> 5 & 3 | (unsigned long long)(CmpF(v17 * (unsigned int)v3, 0x3f000000) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                                                            if ((char)v36)
                                                                v37 = 0x40e00000;
                                                            else
                                                                v37 = 0xc0e00000;
                                                            v38 = sub_1249224();
                                                            if (!g_1fab32c)
                                                            {
                                                                sub_f7d92c(&g_1ef22e8);
                                                                g_1fab32c = 1;
                                                            }
                                                            if (v38)
                                                            {
                                                                v39 = v37 * g_1ef22e8->field_b8->field_18;
                                                                Rigidbody__AddRelativeTorque(v38, 1, 0);
                                                                Random__get_value(0);
                                                                v40 = arm64g_calculate_condition(192, (((((unsigned long long)(char)(CmpF(v39, 0x3f000000)) >> 5 & 3 | (unsigned long long)(CmpF(v39, 0x3f000000) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v39, 0x3f000000)) >> 5 & 3 | (unsigned long long)(CmpF(v39, 0x3f000000) & 1)) & ((unsigned long long)(char)(CmpF(v39, 0x3f000000)) >> 5 & 3 | (unsigned long long)(CmpF(v39, 0x3f000000) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                                                                v41 = sub_1249224();
                                                                if (!g_1fab3e1)
                                                                {
                                                                    sub_f7d92c(&g_1ef22e8);
                                                                    g_1fab3e1 = 1;
                                                                }
                                                                if (v41)
                                                                {
                                                                    addr = Rigidbody__AddRelativeTorque(v41, 1, 0);
                                                                    goto LABEL_10b3b18;
                                                                }
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                        else if (ptr->field_70 && (v30 = GameObject__get_transform(ptr->field_70, 0), v30))
                                        {
                                            goto LABEL_10b38c0;
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
    sub_f7db7c(sub_f7db74());
}
```


## `PlayerWeapons.LateUpdate` — RVA `0xcb3c0c`

- Decompiled symbol: `PlayerWeapons_LateUpdate`
- Metadata signature: `private void LateUpdate() { }`
- Native interval: `104` bytes
- Result: `pseudocode`

```c
void PlayerWeapons_LateUpdate(unsigned long long *ptr, unsigned long a1)
{
    unsigned long long v4;  // d9
    unsigned long long v5;  // d8
    unsigned long long v6;  // x30
    unsigned long long v7;  // x19
    unsigned long v8;  // x0
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x18]
    unsigned long long v2;  // [bp-0x10]
    unsigned long long v3;  // [bp-0x8]

    v0 = v4;
    v1 = v5;
    v2 = v6;
    v3 = v7;
    v8 = ptr[33];
    if (v8)
    {
        Transform__get_position(v8, 0);
        v8 = ptr[33];
        if (v8)
        {
            Transform__get_position(v8, 0);
            v8 = ptr[33];
            if (v8)
            {
                Transform__get_position(v8, 0);
                v8 = ptr[32];
                if (ptr[32])
                {
                    Transform__set_position();
                    return;
                }
            }
        }
    }
    sub_f7db74(v8);
}
```


## `PlayerWeapons.<DisplayGrenadeSwitch>d__63.ctor` — RVA `0xcb3c74`

- Decompiled symbol: `PlayerWeapons_DisplayGrenadeSwitch_d__63_ctor`
- Metadata signature: `public void .ctor(int <>1__state) { }`
- Native interval: `40` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

void PlayerWeapons_DisplayGrenadeSwitch_d__63_ctor(struct_0 *ptr, unsigned int a1)
{
    Object__ctor();
    ptr->field_10 = a1;
    return;
}
```


## `PlayerWeapons.<SelectWeapon>d__66.ctor` — RVA `0xcb3c9c`

- Decompiled symbol: `PlayerWeapons_SelectWeapon_d__66_ctor`
- Metadata signature: `public void .ctor(int <>1__state) { }`
- Native interval: `40` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

void PlayerWeapons_SelectWeapon_d__66_ctor(struct_0 *ptr, unsigned int a1)
{
    Object__ctor();
    ptr->field_10 = a1;
    return;
}
```


## `PlayerWeapons.SniperCallAnim` — RVA `0xcb3cc4`

- Decompiled symbol: `PlayerWeapons_SniperCallAnim`
- Metadata signature: `public void SniperCallAnim() { }`
- Native interval: `44` bytes
- Result: `pseudocode`

```c
void PlayerWeapons_SniperCallAnim(long long a0)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    PlayerWeapons__SelectWeapon(a0, 11, 0, 0);
    MonoBehaviour__StartCoroutine();
    return;
}
```


## `PlayerWeapons.GiveAllWeaponsAndAmmo` — RVA `0xcb3cf0`

- Decompiled symbol: `PlayerWeapons_GiveAllWeaponsAndAmmo`
- Metadata signature: `public void GiveAllWeaponsAndAmmo() { }`
- Native interval: `92` bytes
- Result: `pseudocode`
- Heuristic layout hint: `PlayerWeapons_Recovered` matched 3 offsets against `PlayerWeapons` metadata (confidence 1.00).

```c
typedef struct struct_1 {
    char padding_0[240];
    struct struct_0 *field_f0;
} struct_1;

typedef struct struct_0 {
    char padding_0[24];
    int field_18;
} struct_0;

typedef struct PlayerWeapons_Recovered {
    char padding_0[288];
    char switchTime;
    char padding_121[7];
    unsigned int switching;
    char padding_12c[12];
    unsigned int dropWeapon;
} PlayerWeapons_Recovered;

void PlayerWeapons_GiveAllWeaponsAndAmmo(struct_1 *p)
{
    struct_0 *addr;  // x8
    int v1;  // w9
    int v2;  // w10
    struct_2 *ptr;  // x12
    unsigned int v4;  // w13

    addr = p->field_f0;
    if (addr)
    {
        v1 = addr->field_18;
        if (v1 < 1)
            return;
        v2 = 0;
        while (true)
        {
            if (v1 != v2)
            {
                ptr = *((long long *)&addr[1].padding_0[4 + 8 * v2]);
                if (!ptr)
                    break;
                v4 = ptr->field_138;
                v2 += 1;
                ptr->field_120 = 1;
                ptr->field_128 = v4;
                if (v1 == v2)
                    return;
            }
            else
            {
                sub_f7db7c();
                break;
            }
        }
    }
    sub_f7db74();
}
```


## `PlayerWeapons.HaveWeaponfalse` — RVA `0xcb3d4c`

- Decompiled symbol: `PlayerWeapons_HaveWeaponfalse`
- Metadata signature: `public void HaveWeaponfalse() { }`
- Native interval: `32` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[64];
    unsigned long long field_40;
} struct_0;

void PlayerWeapons_HaveWeaponfalse(struct_0 *a0)
{
    unsigned long long v1;  // x30
    unsigned long long v0;  // [bp-0x10]

    v0 = v1;
    if (a0->field_40)
    {
        GameObject__SetActive();
        return;
    }
    sub_f7db74(0);
}
```


## `PlayerWeapons.ctor` — RVA `0xcb3d6c`

- Decompiled symbol: `PlayerWeapons_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `44` bytes
- Result: `pseudocode`
- Heuristic layout hint: `PlayerWeapons_Recovered` matched 3 offsets against `PlayerWeapons` metadata (confidence 1.00).

```c
typedef struct PlayerWeapons_Recovered {
    char padding_0[204];
    unsigned long long maxWeapons;
    char padding_d4[180];
    unsigned long long shellParentTime;
    unsigned int shellBtParentTime;
} PlayerWeapons_Recovered;

long long PlayerWeapons_ctor(struct_0 *ptr)
{
    *((unsigned long long *)&(&ptr->padding_0)[1]) = 4294967306;
    *((unsigned long long *)&ptr->padding_d4[176]) = 0x3dcccccd3f000000;
    *((unsigned int *)&ptr->field_188) = 1045220557;
}
```


## `PlayerWeapons.<DisplayGrenadeSwitch>d__63.Dispose` — RVA `0xcb3d98`

- Decompiled symbol: `PlayerWeapons_DisplayGrenadeSwitch_d__63_Dispose`
- Metadata signature: `private void System.IDisposable.Dispose() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long PlayerWeapons_DisplayGrenadeSwitch_d__63_Dispose(void)
{
    unsigned long v0;  // x0

    return v0;
}
```


## `PlayerWeapons.<DisplayGrenadeSwitch>d__63.MoveNext` — RVA `0xcb3d9c`

- Decompiled symbol: `PlayerWeapons_DisplayGrenadeSwitch_d__63_MoveNext`
- Metadata signature: `private bool MoveNext() { }`
- Native interval: `200` bytes
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
    char padding_0[376];
    unsigned int field_178;
} struct_0;

extern long long g_1ef2440;
extern char g_1fab4da;

unsigned int PlayerWeapons_DisplayGrenadeSwitch_d__63_MoveNext(struct_1 *ptr)
{
    long long v0;  // x20
    struct_0 *v1;  // x20

    if (!(g_1fab4da & 1))
    {
        sub_f7d92c(&g_1ef2440);
        g_1fab4da = 1;
    }
    if (ptr->field_10 == 1)
    {
        v1 = ptr->field_20;
        ptr->field_10 = 4294967295;
        if (!v1)
            sub_f7db74();
        MonoBehaviour__StartCoroutine(v1, PlayerWeapons__SelectWeapon(v1, v1->field_178, 0, 1), 0);
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


## `PlayerWeapons.<DisplayGrenadeSwitch>d__63.get_Current` — RVA `0xcb3e64`

- Decompiled symbol: `PlayerWeapons_DisplayGrenadeSwitch_d__63_get_Current`
- Metadata signature: `private object System.Collections.Generic.IEnumerator<System.Object>.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long PlayerWeapons_DisplayGrenadeSwitch_d__63_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```


## `PlayerWeapons.<DisplayGrenadeSwitch>d__63.Reset` — RVA `0xcb3e6c`

- Decompiled symbol: `PlayerWeapons_DisplayGrenadeSwitch_d__63_Reset`
- Metadata signature: `private void System.Collections.IEnumerator.Reset() { }`
- Native interval: `56` bytes
- Result: `pseudocode`

```c
extern long long g_1ef0bd8;
extern long long g_1f04ac8;

void PlayerWeapons_DisplayGrenadeSwitch_d__63_Reset(void)
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
    sub_f7da4c(v4, sub_f7d940(&g_1f04ac8));
}
```


## `PlayerWeapons.<DisplayGrenadeSwitch>d__63.get_Current` — RVA `0xcb3ea4`

- Decompiled symbol: `PlayerWeapons_DisplayGrenadeSwitch_d__63_get_Current`
- Metadata signature: `private object System.Collections.IEnumerator.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long PlayerWeapons_DisplayGrenadeSwitch_d__63_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```


## `PlayerWeapons.<SelectWeapon>d__66.Dispose` — RVA `0xcb3eac`

- Decompiled symbol: `PlayerWeapons_SelectWeapon_d__66_Dispose`
- Metadata signature: `private void System.IDisposable.Dispose() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long PlayerWeapons_SelectWeapon_d__66_Dispose(void)
{
    unsigned long v0;  // x0

    return v0;
}
```


## `PlayerWeapons.<SelectWeapon>d__66.MoveNext` — RVA `0xcb3eb0`

- Decompiled symbol: `PlayerWeapons_SelectWeapon_d__66_MoveNext`
- Metadata signature: `private bool MoveNext() { }`
- Native interval: `2476` bytes
- Result: `pseudocode`

```c
typedef struct struct_9 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[4];
    long long field_18;
    struct struct_7 *field_20;
    int field_28;
    char field_2c;
    char field_2d;
    char padding_2e[242];
    char field_120;
    char field_121;
    char padding_122[645];
    char field_3a7;
} struct_9;

typedef struct struct_20 {
    char padding_0[136];
    struct struct_21 *field_88;
    struct struct_14 *field_90;
    struct struct_16 *field_98;
    struct struct_17 *field_a0;
    struct struct_15 *field_a8;
    unsigned long long field_b0;
    unsigned long long field_b8;
    unsigned long long field_c0;
    char padding_c8[20];
    unsigned int field_dc;
    char padding_e0[8];
    struct struct_19 *field_e8;
    char padding_f0[16];
    unsigned long long field_100;
    char padding_108[24];
    unsigned int field_120;
    char padding_124[5];
    char field_129;
    char padding_12a[14];
    char field_138;
    char padding_139[7];
    unsigned long long field_140;
    char padding_148[16];
    unsigned long long field_158;
    char padding_160[28];
    char field_17c;
    char padding_17d[1];
    char field_17e;
} struct_20;

typedef struct struct_19 {
    char padding_0[32];
    unsigned long long field_20;
} struct_19;

typedef struct struct_10 {
    char padding_0[32];
    long long field_20;
} struct_10;

typedef struct struct_11 {
    char padding_0[32];
    long long field_20;
} struct_11;

typedef struct struct_12 {
    char padding_0[288];
    char field_120;
} struct_12;

typedef struct struct_14 {
    char padding_0[120];
    unsigned long long field_78;
    char padding_80[592];
    char field_2d0;
} struct_14;

typedef struct struct_16 {
    char padding_0[272];
    unsigned long long field_110;
    char padding_118[24];
    unsigned int field_130;
    char padding_134[529];
    char field_345;
    char padding_346[96];
    char field_3a6;
    char padding_3a7[17];
    unsigned int field_3b8;
    char padding_3bc[28];
    char field_3d8;
    char padding_3d9[852];
    char field_72d;
    char padding_72e[18];
    unsigned long long field_740;
    unsigned long long field_748;
    unsigned long long field_750;
} struct_16;

typedef struct struct_18 {
    char padding_0[88];
    unsigned long long field_58;
    char padding_60[56];
    unsigned long long field_98;
    unsigned long long field_a0;
    char padding_a8[129];
    char field_129;
    char padding_12a[270];
    unsigned int field_238;
} struct_18;

typedef struct struct_15 {
    char padding_0[32];
    unsigned long long field_20;
} struct_15;

typedef struct struct_1 {
    char padding_0[272];
    unsigned long long field_110;
    char padding_118[24];
    unsigned int field_130;
    char padding_134[529];
    char field_345;
    char padding_346[96];
    char field_3a6;
    char padding_3a7[17];
    unsigned int field_3b8;
    char padding_3bc[28];
    char field_3d8;
    char padding_3d9[852];
    char field_72d;
    char padding_72e[18];
    unsigned long long field_740;
    unsigned long long field_748;
    unsigned long long field_750;
} struct_1;

typedef struct struct_7 {
    char padding_0[136];
    struct struct_8 *field_88;
    struct struct_2 *field_90;
    struct struct_3 *field_98;
    struct struct_4 *field_a0;
    struct struct_5 *field_a8;
    long long field_b0;
    long long field_b8;
    char field_c0;
    char padding_c1[27];
    int field_dc;
    char padding_e0[8];
    struct struct_6 *field_e8;
    char padding_f0[16];
    long long field_100;
    char padding_108[24];
    unsigned int field_120;
    char padding_124[5];
    char field_129;
    char padding_12a[14];
    char field_138;
    char padding_139[7];
    long long field_140;
    char padding_148[16];
    long long field_158;
    char padding_160[28];
    char field_17c;
    char padding_17d[1];
    char field_17e;
} struct_7;

typedef struct struct_21 {
    char padding_0[416];
    char field_1a0;
    char padding_1a1[271];
    char field_2b0;
    char padding_2b1[46];
    char field_2df;
} struct_21;

typedef struct struct_17 {
    char padding_0[88];
    unsigned long long field_58;
    char padding_60[56];
    unsigned long long field_98;
    unsigned long long field_a0;
    char padding_a8[129];
    char field_129;
    char padding_12a[270];
    unsigned int field_238;
} struct_17;

typedef struct struct_8 {
    char padding_0[416];
    char field_1a0;
    char padding_1a1[271];
    char field_2b0;
    char padding_2b1[46];
    char field_2df;
} struct_8;

typedef struct struct_2 {
    char padding_0[120];
    char field_78;
    char padding_79[599];
    char field_2d0;
} struct_2;

typedef struct struct_3 {
    char padding_0[272];
    long long field_110;
    char padding_118[24];
    unsigned int field_130;
    char padding_134[529];
    char field_345;
    char padding_346[96];
    char field_3a6;
    char padding_3a7[17];
    unsigned int field_3b8;
    char padding_3bc[28];
    char field_3d8;
    char padding_3d9[852];
    char field_72d;
    char padding_72e[18];
    long long field_740;
    long long field_748;
    long long field_750;
} struct_3;

typedef struct struct_4 {
    char padding_0[88];
    char field_58;
    char padding_59[63];
    long long field_98;
    char field_a0;
    char padding_a1[136];
    char field_129;
    char padding_12a[270];
    unsigned int field_238;
} struct_4;

typedef struct struct_5 {
    char padding_0[32];
    long long field_20;
} struct_5;

typedef struct struct_6 {
    char padding_0[32];
    long long field_20;
} struct_6;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern long long g_1ef2440;
extern long long g_1efcf08;
extern long long g_1efeb28;
extern long long g_1efed18;
extern long long g_1f08e18;
extern long long g_1f0ae78;
extern long long g_1f0c5b0;
extern long long g_1f0d410;
extern long long g_1f0dc10;
extern long long g_1f0de68;
extern long long g_1f0de70;
extern char g_1fab4db;
extern unsigned int g_832168[4];

unsigned int PlayerWeapons_SelectWeapon_d__66_MoveNext(struct_9 *p)
{
    struct_9 *v2;  // x0
    struct_9 *v3;  // x0
    struct_10 *v11;  // x8
    long long v12;  // x0
    struct_20 *ptr4;  // x20
    unsigned long addr;  // x20
    struct_19 *v15;  // x8
    unsigned long v16;  // x9
    struct_11 *v17;  // x8
    struct_19 *v18;  // x8
    struct_12 *ptr9;  // x0
    struct_16 *v20;  // x8
    struct_9 *ptr5;  // x0
    struct_16 *v21;  // x0
    unsigned int v22;  // s0
    unsigned long v23;  // 4125
    unsigned int cur;  // s0
    char v25[736];  // x8
    unsigned long v26;  // 4125
    unsigned int v27;  // w9
    long long v28;  // x20
    struct_9 *ptr10;  // x19
    struct_19 *v30;  // x8
    struct_20 *ptr;  // x23
    unsigned long ptr8;  // x20
    unsigned long v32;  // x21
    unsigned long long off;  // x24
    unsigned int v34;  // w28
    long long v35;  // x0
    struct_19 *v36;  // x8
    struct_18 *ptr11;  // x22
    unsigned long v38;  // x0
    struct_19 *ptr12;  // x8
    unsigned long v6;  // x0
    struct_18 *ptr13;  // x0
    unsigned long v41;  // x1
    struct_19 *v42;  // x8
    struct_18 *ptr14;  // x22
    unsigned long v44;  // x0
    struct_19 *v45;  // x8
    struct_14 *ptr15;  // x22
    unsigned long v47;  // x0
    struct_19 *ptr16;  // x8
    struct_15 *ptr17;  // x0
    struct_20 *ptr6;  // x21
    unsigned long v50;  // x1
    struct_19 *v51;  // x8
    struct_1 *v52;  // x0
    struct_19 *v53;  // x8
    struct_19 *v54;  // x8
    struct_19 *v55;  // x8
    struct_9 *v56;  // x22
    struct_19 *v57;  // x8
    unsigned long v58;  // 4125
    char v59[736];  // x8
    unsigned long ptr3;  // x21
    struct_19 *v60;  // x8
    unsigned long v61;  // x0
    unsigned long v62;  // x22
    struct_19 *v63;  // x8
    struct_19 *v64;  // x8
    struct_19 *v9;  // x8
    unsigned long v10;  // x9
    char *v0;  // [bp-0x60]
    char v1;  // [bp+0x0]

    v0 = &v1;
    v2 = p;
    if (!(g_1fab4db & 1))
    {
        sub_f7d92c(&g_1efcf08);
        sub_f7d92c(&g_1efeb28);
        sub_f7d92c(&g_1efed18);
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c(&g_1ef2440);
        sub_f7d92c(&g_1f08e18);
        sub_f7d92c(&g_1f0dc10);
        sub_f7d92c(&g_1f0ae78);
        sub_f7d92c(&g_1f0c5b0);
        sub_f7d92c(&g_1f0d410);
        sub_f7d92c(&g_1f0de70);
        v3 = sub_f7d92c(&g_1f0de68);
        g_1fab4db = 1;
        v2 = v3;
    }
    ptr = p->field_20;
    if (p->field_10 != 1)
    {
        if (p->field_10)
            return 0;
        p->field_10 = 4294967295;
        if (Camera__get_main(0) && (v6 = (unsigned long)sub_1231bc8(), ptr))
        {
            ptr6 = ptr;
            ptr6->field_c0 = v6;
            ptr3 = &ptr6->field_c0;
            ptr5 = sub_f7d8d0(ptr3, v6);
            v9 = *((long long *)(ptr3 + 40));
            if (v9)
            {
                v10 = *((int *)(ptr3 + 28));
                if (*((int *)&v9->padding_0[24]) <= (unsigned int)v10)
                    sub_f7db7c(ptr5);
                v11 = &v9->padding_0[8 * v10];
                if (v11->field_20)
                {
                    v12 = sub_1249224(v11->field_20, g_1efeb28);
                    ptr4 = ptr;
                    ptr4->field_b0 = v12;
                    addr = &ptr4->field_b0;
                    ptr5 = sub_f7d8d0(addr, v12);
                    v15 = *((long long *)(addr + 56));
                    *((char *)(addr + 136)) = 0;
                    if (v15)
                    {
                        v16 = p->field_28;
                        if (*((int *)&v15->padding_0[24]) <= (unsigned int)v16)
                            sub_f7db7c(ptr5);
                        v17 = &v15->padding_0[8 * v16];
                        if (v17->field_20 && (ptr5 = (struct_9 *)sub_1249224(v17->field_20, g_1efed18), ptr5))
                        {
                            if (!ptr5->field_120 && p->field_28 || !ptr5->field_121 && !p->field_2c)
                                goto LABEL_10b4804;
                            if (ptr->field_88)
                            {
                                if (ptr->field_88->field_1a0)
                                    return 0;
                                if (ptr->field_17c)
                                    return 0;
                                if (p->field_28)
                                {
                                    v18 = ptr->field_e8;
                                    if (v18)
                                    {
                                        if (!*((int *)&v18->padding_0[24]))
                                            sub_f7db7c(ptr5);
                                        if (v18->field_20 && (ptr9 = (struct_12 *)sub_1249224(v18->field_20, g_1efed18), ptr9))
                                        {
                                            ptr9->field_120 = 0;
                                            goto LABEL_10b40b4;
                                        }
                                    }
                                }
                                else
                                {
LABEL_10b40b4:
                                    if (ptr->field_90 && (ptr->field_90->field_2d0 = 0, v20 = (struct_16 *)ptr->field_98, v20))
                                    {
                                        if (v20->field_72d)
                                        {
                                            if (!g_1ef0c58->field_e0)
                                                sub_f7da5c(g_1ef0c58);
                                            if (!((char)Object__op_Implicit(v20->field_740, 0) & 1))
                                            {
LABEL_10b4118:
                                                if (ptr->field_98)
                                                {
                                                    if (!g_1ef0c58->field_e0)
                                                        sub_f7da5c(g_1ef0c58);
                                                    if (((char)Object__op_Implicit(ptr->field_98->field_748, 0) & 1))
                                                    {
                                                        if (ptr->field_98 && ptr->field_98->field_748)
                                                        {
                                                            Behaviour__set_enabled(ptr->field_98->field_748, 0, 0);
                                                            goto LABEL_10b4160;
                                                        }
                                                    }
                                                    else
                                                    {
LABEL_10b4160:
                                                        if (ptr->field_98)
                                                        {
                                                            if (!g_1ef0c58->field_e0)
                                                                sub_f7da5c(g_1ef0c58);
                                                            if (!(Object__op_Implicit(ptr->field_98->field_750, 0) & 1))
                                                                goto LABEL_10b41a8;
                                                            if (ptr->field_98 && ptr->field_98->field_750)
                                                            {
                                                                Behaviour__set_enabled(ptr->field_98->field_750, 0, 0);
                                                                goto LABEL_10b41a8;
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                            else if (ptr->field_98 && ptr->field_98->field_740)
                                            {
                                                Renderer__set_enabled(ptr->field_98->field_740, 0, 0);
                                                goto LABEL_10b4118;
                                            }
                                        }
                                        else
                                        {
LABEL_10b41a8:
                                            v21 = ptr->field_98;
                                            if (v21)
                                            {
                                                if (*((int *)&v21->padding_134[0]) == v21->field_130)
                                                {
LABEL_10b41f8:
                                                    if (ptr->field_a0)
                                                    {
                                                        ptr->field_a0->field_129 = 0;
                                                        MonoBehaviour__StopCoroutine();
                                                        Time__get_time(0);
                                                        ptr->field_120 = v22;
                                                        Time__get_timeSinceLevelLoad(0);
                                                        v23 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v22, 0x3f800000)) >> 5 & 3 | (unsigned long long)(CmpF(v22, 0x3f800000) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v22, 0x3f800000)) >> 5 & 3 | (unsigned long long)(CmpF(v22, 0x3f800000) & 1)) & ((unsigned long long)(char)(CmpF(v22, 0x3f800000)) >> 5 & 3 | (unsigned long long)(CmpF(v22, 0x3f800000) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                                                        if (!((char)v23))
                                                        {
                                                            if (!ptr->field_17e && !ptr->field_129)
                                                            {
                                                                if (ptr->field_158 && (AudioSource__set_clip(ptr->field_158, ptr->field_140, 0), ptr->field_158 && (AudioSource__set_volume(ptr->field_158, 0), ptr->field_158)))
                                                                {
                                                                    AudioSource__Play(ptr->field_158, 0);
                                                                    goto LABEL_10b4280;
                                                                }
                                                            }
                                                            else
                                                            {
LABEL_10b4280:
                                                                if (*((long long *)ptr3) && (cur = 0x3f800000, Animator__set_speed(*((long long *)ptr3), 0), *((long long *)ptr3)))
                                                                {
                                                                    Animator__SetTrigger(*((long long *)ptr3), g_1f08e18, 0);
                                                                    goto LABEL_10b42b0;
                                                                }
                                                            }
                                                        }
                                                        else
                                                        {
LABEL_10b42b0:
                                                            if (*((long long *)addr) && Component__get_gameObject(*((long long *)addr), 0))
                                                            {
                                                                if (((char)GameObject__get_activeSelf() & 1))
                                                                {
                                                                    v25 = ptr->field_88;
                                                                    if (v25)
                                                                    {
                                                                        if (v25[688] || v25[735])
                                                                        {
                                                                            if (*((long long *)addr) && (Animator__SetTrigger(*((long long *)addr), g_1f0dc10, 0), ptr->field_98))
                                                                            {
                                                                                ptr->field_98->field_3a6 = 1;
                                                                                goto LABEL_10b4314;
                                                                            }
                                                                        }
                                                                        else
                                                                        {
                                                                            if (*((long long *)addr))
                                                                            {
                                                                                Animator__SetTrigger(*((long long *)addr), g_1f0de68, 0);
                                                                                goto LABEL_10b4314;
                                                                            }
                                                                        }
                                                                    }
                                                                }
                                                                else
                                                                {
LABEL_10b4314:
                                                                    ptr5 = Time__get_timeSinceLevelLoad(0);
                                                                    v26 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(cur, 0x40000000)) >> 5 & 3 | (unsigned long long)(CmpF(cur, 0x40000000) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(cur, 0x40000000)) >> 5 & 3 | (unsigned long long)(CmpF(cur, 0x40000000) & 1)) & ((unsigned long long)(char)(CmpF(cur, 0x40000000)) >> 5 & 3 | (unsigned long long)(CmpF(cur, 0x40000000) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                                                                    if ((char)v26)
                                                                        goto LABEL_10b43ac;
                                                                    if (ptr->field_98 && ptr->field_a0)
                                                                    {
                                                                        if (ptr->field_98->field_345 != 1 || p->field_2c)
                                                                            v27 = 0;
                                                                        else
                                                                            v27 = 1;
                                                                        ptr->field_a0->field_238 = g_832168[v27];
                                                                        v28 = sub_f7db70();
                                                                        WaitForSeconds__ctor(v28, 0);
                                                                        p->field_18 = v28;
                                                                        ptr10 = &p->field_18;
                                                                        sub_f7d8d0(ptr10, v28);
                                                                        *((unsigned int *)&ptr10->padding_0[8]) = 1;
                                                                        return 1;
                                                                    }
                                                                }
                                                            }
                                                        }
                                                    }
                                                }
                                                else if (ptr->field_a0)
                                                {
                                                    if (!ptr->field_a0->field_129)
                                                        goto LABEL_10b41f8;
                                                    if (v21->field_110 && (Animator__SetTrigger(v21->field_110, g_1f0c5b0, 0), ptr->field_98))
                                                    {
                                                        ptr->field_98->field_3b8 = 0;
                                                        goto LABEL_10b41f8;
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
LABEL_10b4854:
        sub_f7db7c(sub_f7db74());
    }
    else
    {
        p->field_10 = 4294967295;
        if (!ptr)
            sub_f7db7c(sub_f7db74());
LABEL_10b43ac:
        v30 = ptr->field_e8;
        if (!v30)
            sub_f7db7c(sub_f7db74());
        ptr8 = &ptr->field_b8;
        v32 = &ptr->field_98;
        off = 4;
        while (true)
        {
            v34 = off - 4;
            if (*((int *)&v30->padding_0[24]) <= v34)
                break;
            if (*((int *)&v30->padding_0[24]) <= v34)
                sub_f7db7c(ptr5);
            if (!*((long long *)&v30->padding_0[8 * off]))
                sub_f7db7c(sub_f7db74());
            v35 = sub_1249224(*((long long *)&v30->padding_0[8 * off]), g_1efeb28);
            *((long long *)ptr8) = v35;
            ptr5 = sub_f7d8d0(ptr8, v35);
            if (v34 == p->field_28)
            {
                v36 = ptr->field_e8;
                if (!v36)
                    sub_f7db7c(sub_f7db74());
                if (*((int *)&v36->padding_0[24]) <= v34)
                    sub_f7db7c(ptr5);
                if (!*((long long *)&v36->padding_0[8 * off]))
                    sub_f7db7c(sub_f7db74());
                ptr11 = ptr->field_a0;
                v38 = GameObject__get_transform(*((long long *)&v36->padding_0[8 * off]), 0);
                if (!ptr11)
                    sub_f7db7c(sub_f7db74());
                ptr11->field_a0 = v38;
                ptr5 = sub_f7d8d0(&ptr11->field_a0, v38);
                ptr12 = ptr->field_e8;
                if (!ptr12)
                    sub_f7db7c(sub_f7db74());
                if (*((int *)&ptr12->padding_0[24]) <= v34)
                    sub_f7db7c(ptr5);
                ptr13 = ptr->field_a0;
                if (!ptr13)
                    sub_f7db7c(sub_f7db74());
                v41 = *((long long *)&ptr12->padding_0[8 * off]);
                ptr13->field_98 = v41;
                ptr5 = sub_f7d8d0(&ptr13->field_98, v41);
                v42 = ptr->field_e8;
                if (!v42)
                    sub_f7db7c(sub_f7db74());
                if (*((int *)&v42->padding_0[24]) <= v34)
                    sub_f7db7c(ptr5);
                if (!*((long long *)&v42->padding_0[8 * off]))
                    sub_f7db7c(sub_f7db74());
                ptr14 = ptr->field_a0;
                v44 = sub_1249224(*((long long *)&v42->padding_0[8 * off]), g_1efed18);
                if (!ptr14)
                    sub_f7db7c(sub_f7db74());
                ptr14->field_58 = v44;
                ptr5 = sub_f7d8d0(&ptr14->field_58, v44);
                v45 = ptr->field_e8;
                if (!v45)
                    sub_f7db7c(sub_f7db74());
                if (*((int *)&v45->padding_0[24]) <= v34)
                    sub_f7db7c(ptr5);
                if (!*((long long *)&v45->padding_0[8 * off]))
                    sub_f7db7c(sub_f7db74());
                ptr15 = ptr->field_90;
                v47 = sub_1249224(*((long long *)&v45->padding_0[8 * off]), g_1efed18);
                if (!ptr15)
                    sub_f7db7c(sub_f7db74());
                ptr15->field_78 = v47;
                ptr5 = sub_f7d8d0(&ptr15->field_78, v47);
                ptr16 = ptr->field_e8;
                if (!ptr16)
                    sub_f7db7c(sub_f7db74());
                if (*((int *)&ptr16->padding_0[24]) <= v34)
                    sub_f7db7c(ptr5);
                ptr17 = ptr->field_a8;
                if (!ptr17)
                    sub_f7db7c(sub_f7db74());
                v50 = *((long long *)&ptr16->padding_0[8 * off]);
                ptr17->field_20 = v50;
                ptr5 = sub_f7d8d0(&ptr17->field_20, v50);
                v51 = ptr->field_e8;
                if (!v51)
                    sub_f7db7c(sub_f7db74());
                if (*((int *)&v51->padding_0[24]) <= v34)
                    sub_f7db7c(ptr5);
                if (!*((long long *)&v51->padding_0[8 * off]))
                    sub_f7db7c(sub_f7db74());
                v52 = sub_1249224(*((long long *)&v51->padding_0[8 * off]), g_1efed18);
                ptr->field_98 = v52;
                ptr5 = sub_f7d8d0(v32, v52);
                v53 = ptr->field_e8;
                if (!v53)
                    sub_f7db7c(sub_f7db74());
                if (*((int *)&v53->padding_0[24]) <= v34)
                    sub_f7db7c(ptr5);
                if (!*((long long *)&v53->padding_0[8 * off]))
                    sub_f7db7c(sub_f7db74());
                GameObject__SetActive(*((long long *)&v53->padding_0[8 * off]), 1, 0);
                if (p->field_2d)
                {
                    if (*((long long *)v32))
                    {
                        *((char *)(*((long long *)v32) + 984)) = 1;
                        Time__get_time(0);
                        cur += 0xbf000000;
                        ptr->field_120 = cur;
                    }
                    else
                    {
                        sub_f7db7c(sub_f7db74());
                    }
                }
                if (!*((long long *)v32))
                    sub_f7db7c(sub_f7db74());
                ptr5 = WeaponBehavior__InitializeWeapon();
                v54 = ptr->field_e8;
                ptr->field_dc = p->field_28;
                if (!v54)
                    sub_f7db7c(sub_f7db74());
                if (*((int *)&v54->padding_0[24]) <= v34)
                    sub_f7db7c(ptr5);
                if (!*((long long *)&v54->padding_0[8 * off]))
                    sub_f7db7c(sub_f7db74());
                ptr5 = GameObject__get_transform(*((long long *)&v54->padding_0[8 * off]), 0);
                v55 = ptr->field_e8;
                if (!v55)
                    sub_f7db7c(sub_f7db74());
                if (*((int *)&v55->padding_0[24]) <= v34)
                    sub_f7db7c(ptr5);
                v56 = ptr5;
                if (!*((long long *)&v55->padding_0[8 * off]))
                    sub_f7db7c(sub_f7db74());
                if (!GameObject__get_transform(*((long long *)&v55->padding_0[8 * off]), 0))
                    sub_f7db7c(sub_f7db74());
                ptr5 = Transform__get_localPosition();
                v57 = ptr->field_e8;
                if (!v57)
                    sub_f7db7c(sub_f7db74());
                if (*((int *)&v57->padding_0[24]) <= v34)
                    sub_f7db7c(ptr5);
                if (!*((long long *)&v57->padding_0[8 * off]))
                    sub_f7db7c(sub_f7db74());
                if (!GameObject__get_transform(*((long long *)&v57->padding_0[8 * off]), 0))
                    sub_f7db7c(sub_f7db74());
                Transform__get_localPosition();
                if (!v56)
                    sub_f7db7c(sub_f7db74());
                Transform__set_localPosition(v56, 0);
                Time__get_timeSinceLevelLoad(0);
                v58 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(cur, 0x40000000)) >> 5 & 3 | (unsigned long long)(CmpF(cur, 0x40000000) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(cur, 0x40000000)) >> 5 & 3 | (unsigned long long)(CmpF(cur, 0x40000000) & 1)) & ((unsigned long long)(char)(CmpF(cur, 0x40000000)) >> 5 & 3 | (unsigned long long)(CmpF(cur, 0x40000000) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                if (!((char)v58))
                {
                    if (!ptr->field_a0 || !((ptr->field_a0->field_238 = 0, v59 = (char [736])ptr->field_88, v59)))
                        sub_f7db7c(sub_f7db74());
                    if (v59[688] || v59[735])
                    {
                        if (*((long long *)ptr8))
                        {
                            ptr5 = Animator__SetTrigger(*((long long *)ptr8), g_1f0dc10, 0);
                            if (!*((long long *)v32))
                                sub_f7db7c(sub_f7db74());
                            *((char *)(*((long long *)v32) + 934)) = 1;
                            goto LABEL_10b47d8;
                        }
                        else
                        {
                            sub_f7db7c(sub_f7db74());
                        }
                    }
                    else
                    {
                        if (!*((long long *)ptr8))
                            sub_f7db7c(sub_f7db74());
                    }
                }
                else if (!*((long long *)ptr8))
                {
                    sub_f7db7c(sub_f7db74());
                }
                ptr5 = Animator__SetTrigger();
            }
            else
            {
                v60 = ptr->field_e8;
                if (!v60)
                    sub_f7db7c(sub_f7db74());
                if (*((int *)&v60->padding_0[24]) <= v34)
                    sub_f7db7c(ptr5);
                if (!*((long long *)&v60->padding_0[8 * off]))
                    sub_f7db7c(sub_f7db74());
                v61 = GameObject__get_transform(*((long long *)&v60->padding_0[8 * off]), 0);
                if (!ptr->field_100)
                    sub_f7db7c(sub_f7db74());
                v62 = v61;
                Transform__get_position(ptr->field_100, 0);
                if (!v62)
                    sub_f7db7c(sub_f7db74());
                Transform__set_position(v62, 0);
                if (!*((long long *)ptr8) || !Component__get_gameObject(*((long long *)ptr8), 0))
                    goto LABEL_10b4854;
                ptr5 = GameObject__get_activeSelf();
                if (((char)ptr5 & 1))
                {
                    if (*((long long *)ptr8))
                    {
                        ptr5 = Animator__SetTrigger(*((long long *)ptr8), g_1f0dc10, 0);
                        if (!*((long long *)v32))
                            sub_f7db7c(sub_f7db74());
                        *((char *)(*((long long *)v32) + 934)) = 1;
                    }
                    else
                    {
                        sub_f7db7c(sub_f7db74());
                    }
                }
                v63 = ptr->field_e8;
                if (!v63)
                {
                    sub_f7db7c(sub_f7db74());
                }
                else if (*((int *)&v63->padding_0[24]) <= v34)
                {
                    sub_f7db7c(ptr5);
                }
                else if (*((long long *)&v63->padding_0[8 * off]))
                {
                    ptr5 = sub_1249224(*((long long *)&v63->padding_0[8 * off]), g_1efed18);
                    if (!ptr5)
                        sub_f7db7c(sub_f7db74());
                    ptr5->field_3a7 = 1;
                    v64 = ptr->field_e8;
                    if (!v64)
                    {
                        sub_f7db7c(sub_f7db74());
                    }
                    else if (*((int *)&v64->padding_0[24]) <= v34)
                    {
                        sub_f7db7c(ptr5);
                    }
                    else if (*((long long *)&v64->padding_0[8 * off]))
                    {
                        ptr5 = GameObject__SetActive(*((long long *)&v64->padding_0[8 * off]), 0, 0);
                    }
                    else
                    {
                        sub_f7db7c(sub_f7db74());
                    }
                }
                else
                {
                    sub_f7db7c(sub_f7db74());
                }
            }
LABEL_10b47d8:
            v30 = ptr->field_e8;
            off += 1;
            if (!v30)
                sub_f7db7c(sub_f7db74());
        }
LABEL_10b4804:
        return 0;
    }
}
```


## `PlayerWeapons.<SelectWeapon>d__66.get_Current` — RVA `0xcb501c`

- Decompiled symbol: `PlayerWeapons_SelectWeapon_d__66_get_Current`
- Metadata signature: `private object System.Collections.Generic.IEnumerator<System.Object>.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long PlayerWeapons_SelectWeapon_d__66_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```


## `PlayerWeapons.<SelectWeapon>d__66.Reset` — RVA `0xcb5024`

- Decompiled symbol: `PlayerWeapons_SelectWeapon_d__66_Reset`
- Metadata signature: `private void System.Collections.IEnumerator.Reset() { }`
- Native interval: `56` bytes
- Result: `pseudocode`

```c
extern long long g_1ef0bd8;
extern long long g_1f04ad0;

void PlayerWeapons_SelectWeapon_d__66_Reset(void)
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
    sub_f7da4c(v4, sub_f7d940(&g_1f04ad0));
}
```


## `PlayerWeapons.<SelectWeapon>d__66.get_Current` — RVA `0xcb505c`

- Decompiled symbol: `PlayerWeapons_SelectWeapon_d__66_get_Current`
- Metadata signature: `private object System.Collections.IEnumerator.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long PlayerWeapons_SelectWeapon_d__66_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```
