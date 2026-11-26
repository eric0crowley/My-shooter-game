# Native pseudocode: NPCSpawner

> Metadata source-path string: `Assets/RFPSP/Scripts/AI/NPCSpawner.cs`. This is a path string from the APK metadata, not recovered source text.

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `NPCSpawner.UnregisterSpawnedNPC` — RVA `0xc83f28`

- Decompiled symbol: `NPCSpawner_UnregisterSpawnedNPC`
- Metadata signature: `public void UnregisterSpawnedNPC(AI NpcAI) { }`
- Native interval: `372` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[68];
    unsigned int field_44;
    unsigned int field_48;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern long long g_1ef7620;
extern long long g_1ef7628;
extern long long g_1ef7630;
extern int g_1fab000;
extern char g_1fab427;

unsigned int [19] NPCSpawner_UnregisterSpawnedNPC(struct_1 **ptr, long long a1)
{
    int v0;  // w21
    unsigned int p[19];  // x0
    struct_0 **v2;  // x23
    long long v3;  // x0
    unsigned int v4[19];  // x0
    unsigned int v5[19];  // x0
    unsigned int v6;  // w9
    unsigned int v7;  // w8
    long long v8;  // x0

    v0 = (int)&g_1fab000;
    if (!(g_1fab427 & 1))
    {
        sub_f7d92c(&g_1ef7620);
        sub_f7d92c(&g_1ef7628);
        sub_f7d92c(&g_1ef7630);
        sub_f7d92c(&g_1ef0c58);
        g_1fab427 = 1;
    }
    p = ptr[8];
    if (p)
    {
        v2 = &g_1ef0c58;
        v0 = 0;
        do
        {
            if (p[6] <= v0)
                return p;
            v3 = sub_14a30c0();
            if (!g_1ef0c58->field_e0)
                sub_f7da5c(g_1ef0c58);
        } while (!((char)Object__op_Equality(v3, a1, 0) & 1) && (p = (unsigned int [19])ptr[8], v0 = (int)(v0 + 1), p));
    }
    do
    {
        do
        {
            do
            {
                sub_f7db74(p);
            } while ((p = (unsigned int [19])ptr[8], !p));
            sub_14a48fc(p, v0, g_1ef7620);
            if (!*(v2)->field_e0)
                sub_f7da5c(*(v2));
            v4 = Object__op_Implicit(ptr[4], 0);
            if (!((char)v4 & 1))
                return v4;
            p = ptr[4];
        } while (!p);
        v5 = Behaviour__get_enabled(p, 0);
        if (!((char)v5 & 1))
            return v5;
        p = ptr[4];
    } while (!p);
    v6 = p[17];
    v7 = p[18] + 1;
    p[18] = v7;
    if (v6 <= v7)
    {
        WaveManager__StartWave();
        v8 = MonoBehaviour__StartCoroutine();
        return MonoBehaviour__StartCoroutine();
    }
    return p;
}
```

## `NPCSpawner.Start` — RVA `0xc873b0`

- Decompiled symbol: `NPCSpawner_Start`
- Metadata signature: `private void Start() { }`
- Native interval: `12` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[52];
    unsigned int field_34;
} struct_0;

struct_0 * NPCSpawner_Start(struct_0 *ptr)
{
    ptr->field_34 = 0xc4800000;
    return ptr;
}
```

## `NPCSpawner.Update` — RVA `0xc873bc`

- Decompiled symbol: `NPCSpawner_Update`
- Metadata signature: `private void Update() { }`
- Native interval: `168` bytes
- Result: `pseudocode`
- Heuristic layout hint: `NPCSpawner_Recovered` matched 13 offsets against `NPCSpawner` metadata (confidence 1.00).

```c
typedef struct NPCSpawner_Recovered {
    char padding_0[40];
    long long NPCPrefab;
    unsigned int spawnDelay;
    unsigned int spawnTime;
    long long NPCInstance;
    struct struct_0 *Npcs;
    char padding_48[8];
    struct struct_1 *waypointGroup;
    unsigned int firstWaypoint;
    char padding_5c[12];
    char unlimitedSpawning;
    char huntPlayer;
    char padding_6a[2];
    int maxActiveNpcs;
    int NpcsToSpawn;
    unsigned int spawnedNpcAmt;
    char pauseSpawning;
} NPCSpawner_Recovered;

typedef struct struct_13 {
    char padding_0[16];
    unsigned long long field_10;
    unsigned int field_18;
    unsigned int field_1c;
} struct_13;

typedef struct struct_7 {
    char padding_0[32];
    char field_20;
    char padding_21[7];
    long long field_28;
    char padding_30[72];
    char field_78;
    char padding_79[155];
    char field_114;
    char padding_115[1];
    char field_116;
    char padding_117[9];
    struct struct_6 *field_120;
    unsigned int field_128;
    char field_12c;
    char padding_12d[3];
    char field_130;
    char padding_131[19];
    unsigned int field_144;
    unsigned int field_148;
    unsigned int field_14c;
    char padding_150[270];
    char field_25e;
} struct_7;

typedef struct struct_5 {
    char padding_0[32];
    struct struct_4 *field_20;
} struct_5;

typedef struct struct_12 {
    char padding_0[40];
    unsigned long long field_28;
} struct_12;

typedef struct struct_0 {
    char padding_0[16];
    unsigned long long field_10;
    unsigned int field_18;
    unsigned int field_1c;
} struct_0;

typedef struct struct_1 {
    char padding_0[40];
    unsigned long long field_28;
} struct_1;

typedef struct struct_6 {
    char padding_0[40];
    long long field_28;
} struct_6;

typedef struct struct_4 {
    char padding_0[32];
    char field_20;
    char padding_21[7];
    unsigned long long field_28;
    char padding_30[72];
    unsigned long long field_78;
    char padding_80[148];
    char field_114;
    char padding_115[1];
    char field_116;
    char padding_117[9];
    struct struct_3 *field_120;
    unsigned int field_128;
    char field_12c;
    char padding_12d[3];
    char field_130;
    char padding_131[19];
    unsigned int field_144;
    unsigned int field_148;
    unsigned int field_14c;
    char padding_150[270];
    char field_25e;
} struct_4;

typedef struct struct_3 {
    char padding_0[40];
    unsigned long long field_28;
} struct_3;

typedef struct struct_8 {
    char padding_0[112];
    long long field_70;
} struct_8;

typedef struct struct_9 {
    char padding_0[192];
    struct struct_8 *field_c0;
} struct_9;

typedef struct struct_11 {
    char padding_0[224];
    unsigned int field_e0;
} struct_11;

typedef struct struct_10 {
    char padding_0[32];
    struct struct_9 *field_20;
} struct_10;

extern char g_1087464;
extern struct_11 *g_1ef0c58;
extern struct_10 *g_1ef7618;
extern long long g_1ef7628;
extern long long g_1ef8aa0;
extern long long g_1efd030;
extern long long g_1efeb10;
extern long long g_1f00260;
extern unsigned long long g_1fab000;
extern char g_1fab425;
extern char g_1fab426;

struct_2 * NPCSpawner_Update(struct_2 *a0, unsigned long a1)
{
    unsigned long long v12;  // d9
    unsigned long long v13;  // d8
    unsigned long long v22;  // d9
    unsigned long long v23;  // d8
    unsigned long long v24;  // d14
    unsigned long long v25;  // d13
    unsigned long long v26;  // d12
    unsigned long long v27;  // d11
    unsigned long long v28;  // d10
    unsigned long long v29;  // x22
    unsigned long long v30;  // x21
    struct_2 *p;  // x19
    unsigned long long v14;  // x30
    struct_2 *v32;  // x0
    long long v33;  // x0
    struct_2 *ptr4;  // x20
    struct_2 *v35;  // x20
    struct_7 *v36;  // x0
    struct_13 *addr;  // x8
    unsigned long v38;  // x9
    unsigned long v39;  // x11
    struct_7 *ptr;  // x20
    struct_5 *ptr6;  // x0
    unsigned long long v15;  // x20
    unsigned long v42;  // x0
    unsigned long v43;  // x1
    struct_7 *ptr5;  // x0
    struct_12 *v45;  // x1
    struct_7 *v46;  // x21
    unsigned int v47;  // w8
    unsigned int v49;  // w8
    struct_2 *v50;  // x0
    unsigned int v51;  // s2
    struct_2 *ptr3;  // x19
    struct_2 *v17;  // x0
    unsigned int v18;  // s1
    unsigned int v19;  // s0
    unsigned long v20;  // 4138
    struct_2 *v21;  // x0
    unsigned long long v0;  // [bp-0x60]
    unsigned long long v1;  // [bp-0x58]
    unsigned long long v2;  // [bp-0x50]
    unsigned long long v3;  // [bp-0x48]
    unsigned long long v4;  // [bp-0x40]
    unsigned long long v5;  // [bp-0x38]
    unsigned long long v6;  // [bp-0x30]
    unsigned long v7;  // [bp-0x28], Other Possible Types: unsigned long long
    unsigned long long v8;  // [bp-0x20]
    unsigned long long v9;  // [bp-0x18]
    unsigned long long v10;  // [bp-0x10]
    struct_2 *v11;  // [bp-0x8]

    v6 = v12;
    v7 = v13;
    v8 = v14;
    v15 = &g_1fab000;
    ptr3 = a0;
    if (!(g_1fab425 & 1))
    {
        a0 = sub_f7d92c(&g_1ef7628);
        g_1fab425 = 1;
    }
    if (ptr3->field_78)
        return a0;
    if (!ptr3->field_40)
    {
        vvar_206{r256|8b} = (int)&g_1087464;
        v21 = sub_f7db74();
    }
    else if (ptr3->field_6c > ptr3->field_40->field_18)
    {
        if (!ptr3->field_68 && ptr3->field_70 <= ptr3->field_74)
            return a0;
        v17 = Time__get_time(0);
        v18 = ptr3->field_34 + ptr3->field_30;
        v20 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v18, v19)) >> 5 & 3 | (unsigned long long)(CmpF(v18, v19) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v18, v19)) >> 5 & 3 | (unsigned long long)(CmpF(v18, v19) & 1)) & ((unsigned long long)(char)(CmpF(v18, v19)) >> 5 & 3 | (unsigned long long)(CmpF(v18, v19) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if ((char)v20)
            return v17;
        a1 = ptr3->field_28;
        v21 = ptr3;
        v15 = v10;
        ptr3 = v11;
        vvar_96{r256|8b} = v8;
        v22 = v6;
        v23 = v7;
    }
    else
    {
        return a0;
    }
    v0 = v24;
    v1 = v25;
    v2 = v26;
    v3 = v27;
    v4 = v28;
    v5 = v22;
    v6 = v23;
    v7 = vvar_96{r256|8b};
    v8 = v29;
    v9 = v30;
    v10 = v15;
    v11 = ptr3;
    p = v21;
    if (!(g_1fab426 & 1))
    {
        sub_f7d92c(&g_1efd030);
        sub_f7d92c(&g_1efeb10);
        sub_f7d92c(&g_1ef7618);
        sub_f7d92c(&g_1ef8aa0);
        sub_f7d92c(&g_1f00260);
        sub_f7d92c(&g_1ef0c58);
        g_1fab426 = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v32 = Object__op_Implicit(p->field_28, 0);
    if (!((char)v32 & 1))
        return v32;
    if (Component__get_transform(p, 0) && (Transform__get_position(), Component__get_transform(p, 0)))
    {
        Transform__get_rotation();
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        v33 = sub_112a1ac(a1, g_1f00260);
        ptr4 = p;
        ptr4->field_38 = v33;
        v35 = &ptr4->field_38;
        sub_f7d8d0(v35, v33);
        if (*((long long *)&v35->padding_0[0]) && (v36 = (struct_7 *)sub_1249224(*((long long *)&v35->padding_0[0]), g_1efeb10), addr = (struct_13 *)p->field_40, addr && (v38 = (unsigned long)addr->field_10, addr->field_1c = addr->field_1c + 1, v38)))
        {
            v39 = addr->field_18;
            ptr = v36;
            if (*((int *)(v38 + 24)) > (unsigned int)v39)
            {
                ptr6 = v38 + v39 * 8;
                addr->field_18 = (unsigned int)v39 + 1;
                ptr6->field_20 = ptr;
                sub_f7d8d0(&ptr6->field_20, ptr);
            }
            else
            {
                sub_14a3390(addr, ptr, g_1ef7618->field_20->field_c0->field_70);
            }
            if (Component__get_transform(p, 0) && (v42 = (unsigned long)sub_1231bc8(), ptr))
            {
                v43 = sub_1231bc8();
                ptr5 = ptr;
                *((unsigned long *)&ptr5->field_78) = v43;
                sub_f7d8d0(&ptr5->field_78, v43);
                if (p->field_69)
                    ptr->field_114 = 1;
                ptr->field_20 = 1;
                v45 = p->field_50;
                v46 = &ptr->field_120;
                ptr->field_120 = v45;
                sub_f7d8d0(v46, v45);
                v47 = p->field_58;
                ptr->field_116 = 0;
                ptr->field_12c = 0;
                ptr->field_128 = v47;
                MonoBehaviour__StartCoroutine(ptr, AI__SpawnNPC(ptr), 0);
                Time__get_time(0);
                v49 = p->field_69;
                p->field_34 = v19;
                if (v49)
                {
                    if (ptr->field_28 && GameObject__get_transform(ptr->field_28, 0))
                        goto LABEL_1087720;
                }
                else
                {
                    if (*((long long *)&v46->padding_0[0]) && *((long long *)(*((long long *)&v46->padding_0[0]) + 40)) && sub_14a30c0(*((long long *)(*((long long *)&v46->padding_0[0]) + 40)), p->field_58, g_1ef8aa0) && Component__get_transform())
                    {
LABEL_1087720:
                        v50 = Transform__get_position();
                        ptr->field_144 = v19;
                        ptr->field_148 = v18;
                        ptr->field_130 = 1;
                        ptr->field_25e = 1;
                        ptr->field_14c = v51;
                        p->field_74 = p->field_74 + 1;
                        return v50;
                    }
                }
            }
        }
    }
    sub_f7db74();
}
```

## `NPCSpawner.Spawn` — RVA `0xc87464`

- Decompiled symbol: `NPCSpawner_Spawn`
- Metadata signature: `private void Spawn(GameObject NpcPrefab) { }`
- Native interval: `780` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: CFGFast did not recover a function at the metadata RVA

```c
// 0x1087464: str d14, [sp, #-0x60]!
// 0x1087468: stp d13, d12, [sp, #8]
// 0x108746c: stp d11, d10, [sp, #0x18]
// 0x1087470: stp d9, d8, [sp, #0x28]
// 0x1087474: str x30, [sp, #0x38]
// 0x1087478: stp x22, x21, [sp, #0x40]
// 0x108747c: stp x20, x19, [sp, #0x50]
// 0x1087480: adrp x21, #0x1fab000
// 0x1087484: adrp x22, #0x1e8c000
// 0x1087488: ldrb w8, [x21, #0x426]
// 0x108748c: ldr x22, [x22, #0xd8]
// 0x1087490: mov x20, x1
// 0x1087494: mov x19, x0
// 0x1087498: tbnz w8, #0, #0x10874ec
// 0x108749c: adrp x0, #0x1e8d000
// 0x10874a0: ldr x0, [x0, #0xf18]
// 0x10874a4: bl #0xf7d92c
// 0x10874a8: adrp x0, #0x1e8d000
// 0x10874ac: ldr x0, [x0, #0xce0]
// 0x10874b0: bl #0xf7d92c
// 0x10874b4: adrp x0, #0x1e8d000
// 0x10874b8: ldr x0, [x0, #0xcf0]
// 0x10874bc: bl #0xf7d92c
// 0x10874c0: adrp x0, #0x1e8d000
// 0x10874c4: ldr x0, [x0, #0xd60]
// 0x10874c8: bl #0xf7d92c
// 0x10874cc: adrp x0, #0x1e8d000
// 0x10874d0: ldr x0, [x0, #0x9c8]
// 0x10874d4: bl #0xf7d92c
// 0x10874d8: adrp x0, #0x1e8c000
// 0x10874dc: ldr x0, [x0, #0xd8]
// 0x10874e0: bl #0xf7d92c
// 0x10874e4: mov w8, #1
// 0x10874e8: strb w8, [x21, #0x426]
// 0x10874ec: ldr x0, [x22]
// 0x10874f0: ldr x21, [x19, #0x28]
// 0x10874f4: ldr w8, [x0, #0xe0]
// 0x10874f8: cbnz w8, #0x1087500
// 0x10874fc: bl #0xf7da5c
// 0x1087500: mov x0, x21
// 0x1087504: mov x1, xzr
// 0x1087508: bl #0x1b98274
// 0x108750c: tbz w0, #0, #0x108774c
// 0x1087510: mov x0, x19
// 0x1087514: mov x1, xzr
// 0x1087518: bl #0x1b92154
// 0x108751c: cbz x0, #0x108776c
// 0x1087520: mov x1, xzr
// 0x1087524: bl #0x1b9d508
// 0x1087528: mov x0, x19
// 0x108752c: mov x1, xzr
// 0x1087530: mov v8.16b, v0.16b
// 0x1087534: mov v9.16b, v1.16b
// 0x1087538: mov v10.16b, v2.16b
// 0x108753c: bl #0x1b92154
// 0x1087540: cbz x0, #0x108776c
// 0x1087544: mov x1, xzr
// 0x1087548: bl #0x1b9d6f0
// 0x108754c: ldr x0, [x22]
// 0x1087550: mov v11.16b, v0.16b
// 0x1087554: mov v12.16b, v1.16b
// 0x1087558: mov v13.16b, v2.16b
// 0x108755c: ldr w8, [x0, #0xe0]
// 0x1087560: mov v14.16b, v3.16b
// 0x1087564: cbnz w8, #0x108756c
// 0x1087568: bl #0xf7da5c
// 0x108756c: adrp x8, #0x1e8d000
// 0x1087570: ldr x8, [x8, #0x9c8]
// 0x1087574: mov x0, x20
// 0x1087578: mov v0.16b, v8.16b
// 0x108757c: mov v1.16b, v9.16b
// 0x1087580: ldr x1, [x8]
// 0x1087584: mov v2.16b, v10.16b
// 0x1087588: mov v3.16b, v11.16b
// 0x108758c: mov v4.16b, v12.16b
// 0x1087590: mov v5.16b, v13.16b
// 0x1087594: mov v6.16b, v14.16b
// 0x1087598: bl #0x112a1ac
// 0x108759c: mov x20, x19
// 0x10875a0: str x0, [x20, #0x38]!
// 0x10875a4: mov x1, x0
// 0x10875a8: mov x0, x20
// 0x10875ac: bl #0xf7d8d0
// 0x10875b0: ldr x0, [x20]
// 0x10875b4: cbz x0, #0x108776c
// 0x10875b8: adrp x8, #0x1e8d000
// 0x10875bc: ldr x8, [x8, #0xce0]
// 0x10875c0: ldr x1, [x8]
// 0x10875c4: bl #0x1249224
// 0x10875c8: ldr x8, [x19, #0x40]
// 0x10875cc: cbz x8, #0x108776c
// 0x10875d0: adrp x10, #0x1e8d000
// 0x10875d4: ldr x10, [x10, #0xcf0]
// 0x10875d8: ldr w11, [x8, #0x1c]
// 0x10875dc: ldr x9, [x8, #0x10]
// 0x10875e0: ldr x10, [x10]
// 0x10875e4: add w11, w11, #1
// 0x10875e8: str w11, [x8, #0x1c]
// 0x10875ec: cbz x9, #0x108776c
// 0x10875f0: ldrsw x11, [x8, #0x18]
// 0x10875f4: ldr w12, [x9, #0x18]
// 0x10875f8: mov x20, x0
// 0x10875fc: cmp w11, w12
// 0x1087600: b.hs #0x1087620
// 0x1087604: add w10, w11, #1
// 0x1087608: add x0, x9, x11, lsl #3
// 0x108760c: str w10, [x8, #0x18]
// 0x1087610: str x20, [x0, #0x20]!
// 0x1087614: mov x1, x20
// 0x1087618: bl #0xf7d8d0
// 0x108761c: b #0x1087638
// 0x1087620: ldr x9, [x10, #0x20]
// 0x1087624: mov x0, x8
// 0x1087628: mov x1, x20
// 0x108762c: ldr x9, [x9, #0xc0]
// 0x1087630: ldr x2, [x9, #0x70]
// 0x1087634: bl #0x14a3390
// 0x1087638: mov x0, x19
// 0x108763c: mov x1, xzr
// 0x1087640: bl #0x1b92154
// 0x1087644: cbz x0, #0x108776c
// 0x1087648: adrp x8, #0x1e8d000
// 0x108764c: ldr x8, [x8, #0xf18]
// 0x1087650: ldr x1, [x8]
// 0x1087654: bl #0x1231bc8
// 0x1087658: cbz x20, #0x108776c
// 0x108765c: mov x1, x0
// 0x1087660: mov x0, x20
// 0x1087664: str x1, [x0, #0x78]!
// 0x1087668: bl #0xf7d8d0
// 0x108766c: ldrb w8, [x19, #0x69]
// 0x1087670: cbz w8, #0x108767c
// 0x1087674: mov w8, #1
// 0x1087678: strb w8, [x20, #0x114]
// 0x108767c: mov w8, #1
// 0x1087680: strb w8, [x20, #0x20]
// 0x1087684: ldr x1, [x19, #0x50]
// 0x1087688: add x21, x20, #0x120
// 0x108768c: mov x0, x21
// 0x1087690: str x1, [x20, #0x120]
// 0x1087694: bl #0xf7d8d0
// 0x1087698: ldr w8, [x19, #0x58]
// 0x108769c: mov x0, x20
// 0x10876a0: strb wzr, [x20, #0x116]
// 0x10876a4: strb wzr, [x20, #0x12c]
// 0x10876a8: str w8, [x20, #0x128]
// 0x10876ac: bl #0x107d2a0
// 0x10876b0: mov x1, x0
// 0x10876b4: mov x0, x20
// 0x10876b8: mov x2, xzr
// 0x10876bc: bl #0x1b95d40
// 0x10876c0: mov x0, xzr
// 0x10876c4: bl #0x1b9ad30
// 0x10876c8: ldrb w8, [x19, #0x69]
// 0x10876cc: str s0, [x19, #0x34]
// 0x10876d0: cbz w8, #0x10876ec
// 0x10876d4: ldr x0, [x20, #0x28]
// 0x10876d8: cbz x0, #0x108776c
// 0x10876dc: mov x1, xzr
// 0x10876e0: bl #0x1b94c14
// 0x10876e4: cbnz x0, #0x1087720
// 0x10876e8: b #0x108776c
// 0x10876ec: ldr x8, [x21]
// 0x10876f0: cbz x8, #0x108776c
// 0x10876f4: ldr x0, [x8, #0x28]
// 0x10876f8: cbz x0, #0x108776c
// 0x10876fc: adrp x8, #0x1e8d000
// 0x1087700: ldr w1, [x19, #0x58]
// 0x1087704: ldr x8, [x8, #0xd60]
// 0x1087708: ldr x2, [x8]
// 0x108770c: bl #0x14a30c0
// 0x1087710: cbz x0, #0x108776c
// 0x1087714: mov x1, xzr
// 0x1087718: bl #0x1b92154
// 0x108771c: cbz x0, #0x108776c
// 0x1087720: mov x1, xzr
// 0x1087724: bl #0x1b9d508
// 0x1087728: mov w8, #1
// 0x108772c: str s0, [x20, #0x144]
// 0x1087730: str s1, [x20, #0x148]
// 0x1087734: strb w8, [x20, #0x130]
// 0x1087738: strb w8, [x20, #0x25e]
// 0x108773c: str s2, [x20, #0x14c]
// 0x1087740: ldr w8, [x19, #0x74]
// 0x1087744: add w8, w8, #1
// 0x1087748: str w8, [x19, #0x74]
// 0x108774c: ldp x20, x19, [sp, #0x50]
// 0x1087750: ldp x22, x21, [sp, #0x40]
// 0x1087754: ldr x30, [sp, #0x38]
// 0x1087758: ldp d9, d8, [sp, #0x28]
// 0x108775c: ldp d11, d10, [sp, #0x18]
// 0x1087760: ldp d13, d12, [sp, #8]
// 0x1087764: ldr d14, [sp], #0x60
// 0x1087768: ret
// 0x108776c: bl #0xf7db74
```

## `NPCSpawner.ctor` — RVA `0xc877dc`

- Decompiled symbol: `NPCSpawner_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `168` bytes
- Result: `pseudocode`
- Heuristic layout hint: `NPCSpawner_Recovered` matched 5 offsets against `NPCSpawner` metadata (confidence 1.00).

```c
typedef struct NPCSpawner_Recovered {
    char padding_0[48];
    unsigned int spawnDelay;
    char padding_34[12];
    long long Npcs;
    char padding_48[16];
    unsigned int firstWaypoint;
    char padding_5c[12];
    char unlimitedSpawning;
    char padding_69[3];
    unsigned long long maxActiveNpcs;
} NPCSpawner_Recovered;

extern long long g_1eed520;
extern long long g_1ef7610;
extern char g_1fab428;

void NPCSpawner_ctor(struct_0 *ptr)
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
    if (!(g_1fab428 & 1))
    {
        sub_f7d92c(&g_1ef7610);
        sub_f7d92c(&g_1eed520);
        g_1fab428 = 1;
    }
    ptr->field_30 = 0x41f00000;
    v10 = sub_f7db70(g_1eed520);
    sub_14a2b64(v10, g_1ef7610);
    ptr->field_40 = v10;
    sub_f7d8d0(&ptr->field_40, v10);
    ptr->field_58 = 1;
    ptr->field_68 = 1;
    *((unsigned long long *)&(&ptr->padding_69)[1]) = 21474836483;
}
```
