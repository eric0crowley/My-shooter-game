# Native pseudocode: WorldRecenter

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `WorldRecenter.LateUpdate` — RVA `0xc9bed0`

- Decompiled symbol: `WorldRecenter_LateUpdate`
- Metadata signature: `private void LateUpdate() { }`
- Native interval: `1188` bytes
- Result: `pseudocode`
- Heuristic layout hint: `WorldRecenter_Recovered` matched 6 offsets against `WorldRecenter` metadata (confidence 0.86).

```c
typedef struct struct_4 {
    char padding_0[224];
    unsigned int field_e0;
} struct_4;

typedef struct WorldRecenter_Recovered {
    struct struct_0 *field_0;
    char padding_8[24];
    long long objects;
    unsigned int threshold;
    char refreshTerrain;
    char padding_2d[3];
    unsigned int worldRecenterTime;
    char padding_34[4];
    struct struct_1 *emitterParticles;
    unsigned int numParticlesAlive;
} WorldRecenter_Recovered;

typedef struct struct_3 {
    char padding_0[224];
    unsigned int field_e0;
} struct_3;

typedef struct struct_10 {
    char padding_0[24];
    unsigned int field_18;
} struct_10;

typedef struct struct_9 {
    char padding_0[200];
    unsigned long long field_c8;
    char padding_d0[96];
    char field_130;
} struct_9;

typedef struct struct_5 {
    char padding_0[24];
    unsigned int field_18;
} struct_5;

typedef struct struct_11 {
    char padding_0[24];
    unsigned int field_18;
} struct_11;

typedef struct struct_0 {
    char padding_0[24];
    unsigned int field_18;
} struct_0;

typedef struct struct_1 {
    char padding_0[24];
    unsigned int field_18;
} struct_1;

typedef struct struct_8 {
    char padding_0[224];
    unsigned int field_e0;
} struct_8;

typedef struct struct_6 {
    char padding_0[224];
    unsigned int field_e0;
} struct_6;

extern struct_6 *g_1ef0c58;
extern struct_8 *g_1ef1f08;
extern char g_1fab3df;
extern char g_1fab4a6;

struct_4 * WorldRecenter_LateUpdate(struct_2 *ptr)
{
    struct_2 *p;  // x20
    struct_3 *v1;  // x0
    struct_10 *addr;  // x25
    unsigned int v11;  // w8
    unsigned int v12;  // w26
    struct_9 **v13;  // x21
    unsigned long v14;  // x9
    long long v15;  // x0
    struct_5 *v16;  // x0
    struct_10 *ptr3;  // x22
    unsigned int v18;  // w8
    unsigned int v2;  // s2
    unsigned int v19;  // w24
    struct_11 *v20;  // x1
    unsigned long i;  // x26
    unsigned long long v22;  // x27
    long long v23;  // x0
    struct_4 *v24;  // x0
    unsigned int v3;  // s0
    unsigned long v4;  // 4192
    struct_4 *v5;  // x0
    unsigned long v6;  // 4155
    long long v7;  // x0
    long long v8;  // x0
    struct_4 *v9;  // x0

    if (!(g_1fab4a6 & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c("GK");
        sub_f7d92c("GK");
        sub_f7d92c("cY");
        sub_f7d92c("cY");
        sub_f7d92c(&g_1ef1f08);
        g_1fab4a6 = 1;
    }
    if (Component__get_gameObject(ptr, 0) && GameObject__get_transform())
    {
        Transform__get_position();
        if (!g_1fab3df)
        {
            sub_f7d92c("_F");
            g_1fab3df = 1;
        }
        v1 = g_1ef07e8;
        if (!g_1ef07e8->field_e0)
            v1 = sub_f7da5c(g_1ef07e8);
        v2 = ptr->field_28;
        v3 = [D] unsupported_Iop_SqrtF32();
        v4 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v3, v2)) >> 5 & 3 | (unsigned long long)(CmpF(v3, v2) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v3, v2)) >> 5 & 3 | (unsigned long long)(CmpF(v3, v2) & 1)) & ((unsigned long long)(char)(CmpF(v3, v2)) >> 5 & 3 | (unsigned long long)(CmpF(v3, v2) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if ((char)v4)
            return v1;
        Time__get_time(0);
        ptr->field_30 = v3;
        Time__get_timeScale(0);
        v5 = Time__get_time(0);
        v6 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v3 * 1045220558, v3)) >> 5 & 3 | (unsigned long long)(CmpF(v3 * 1045220558, v3) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v3 * 1045220558, v3)) >> 5 & 3 | (unsigned long long)(CmpF(v3 * 1045220558, v3) & 1)) & ((unsigned long long)(char)(CmpF(v3 * 1045220558, v3)) >> 5 & 3 | (unsigned long long)(CmpF(v3 * 1045220558, v3) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if ((char)v6)
            return v5;
        if (!g_1ef1f08->field_e0)
            sub_f7da5c(g_1ef1f08);
        v7 = Type__GetTypeFromHandle(g_1eebae8, 0);
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        v8 = Object__FindObjectsOfType(v7, 0);
        ptr->field_20 = v8;
        p = &ptr->field_20;
        v9 = sub_f7d8d0(p, v8);
        addr = p->field_0;
        if (addr)
        {
            v11 = addr->field_18;
            if (addr->field_18 >= 1)
            {
                v12 = 0;
                while (true)
                {
                    if (v11 <= v12)
                        goto LABEL_109c360;
                    v13 = *((long long *)&addr[1].padding_0[4 + 8 * v12]);
                    if (!v13)
                        break;
                    v14 = g_1ef1e78->field_130;
                    if (*(v13)->field_130 < (unsigned int)v14)
                    {
                        sub_f7df10(v13);
                        sub_f7df10(p);
                    }
                    if (*((long long *)(*(v13)->field_c8 + v14 * 8 - 8)) != g_1ef1e78)
                    {
                        sub_f7df10(v13);
                        sub_f7df10(p);
                    }
                    v15 = Transform__get_parent(v13, 0);
                    if (!g_1ef0c58->field_e0)
                        sub_f7da5c(g_1ef0c58);
                    v9 = Object__op_Equality(v15, 0, 0);
                    if (((char)v9 & 1))
                    {
                        if (!Component__get_gameObject(v13, 0))
                            break;
                        v9 = GameObject__get_layer();
                        if ((unsigned int)v9 != 14)
                        {
                            Transform__get_position(v13, 0);
                            v9 = Transform__set_position(v13, 0);
                        }
                    }
                    v11 = addr->field_18;
                    v12 += 1;
                    if (v12 >= v11)
                        goto LABEL_109c168;
                }
            }
            else
            {
LABEL_109c168:
                if (!g_1ef1f08->field_e0)
                    sub_f7da5c(g_1ef1f08);
                v13 = Type__GetTypeFromHandle(g_1eeb808, 0);
                if (!g_1ef0c58->field_e0)
                    sub_f7da5c(g_1ef0c58);
                v16 = Object__FindObjectsOfType(v13, 0);
                p->field_0 = v16;
                v9 = sub_f7d8d0(p, v16);
                ptr3 = p->field_0;
                if (ptr3)
                {
                    v18 = ptr3->field_18;
                    if (v18 >= 1)
                    {
                        v19 = 0;
                        while (true)
                        {
                            if (v18 <= v19)
                                goto LABEL_109c360;
                            p = *((long long *)&ptr3[1].padding_0[4 + 8 * v19]);
                            if (!p)
                                break;
                            if (p->field_0 != g_1ef0e10)
                                sub_f7df10(p);
                            v9 = ParticleSystem__GetParticles(p, ptr->field_38, 0);
                            v20 = ptr->field_38;
                            ptr->field_40 = (unsigned int)v9;
                            if ((unsigned int)v9 >= 1)
                            {
                                i = 0;
                                v22 = 32;
                                do
                                {
                                    if (!v20)
                                        goto LABEL_109c35c;
                                    if (v20->field_18 <= i)
                                        goto LABEL_109c360;
                                    v13 = &v20->padding_0[v22];
                                    ParticleSystem_Particle__get_position(v13, 0);
                                    v9 = ParticleSystem_Particle__set_position(v13, 0);
                                    v20 = ptr->field_38;
                                    i += 1;
                                    v22 += 132;
                                } while (i < ptr->field_40);
                                goto LABEL_109c360;
                            }
                            v9 = ParticleSystem__SetParticles(p);
                            v18 = ptr3->field_18;
                            v19 += 1;
                            if (v19 >= v18)
                                goto LABEL_109c29c;
                        }
                    }
                    else
                    {
LABEL_109c29c:
                        if (!ptr->field_2c)
                            return v9;
                        v23 = Terrain__get_activeTerrain(0);
                        if (!g_1ef0c58->field_e0)
                            sub_f7da5c(g_1ef0c58);
                        v24 = Object__op_Implicit(v23, 0);
                        if (!((char)v24 & 1))
                        {
                            return v24;
                        }
                        else if (Terrain__get_activeTerrain(0) && Terrain__get_terrainData())
                        {
                            TerrainData__GetHeights();
                        }
                    }
                }
            }
        }
    }
LABEL_109c35c:
    v9 = sub_f7db74();
LABEL_109c360:
    sub_f7db7c(v9);
    sub_f7df10(v13);
    sub_f7df10(p);
}
```

## `WorldRecenter.ctor` — RVA `0xc9c374`

- Decompiled symbol: `WorldRecenter_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `116` bytes
- Result: `pseudocode`
- Heuristic layout hint: `WorldRecenter_Recovered` matched 3 offsets against `WorldRecenter` metadata (confidence 1.00).

```c
typedef struct WorldRecenter_Recovered {
    char padding_0[40];
    unsigned int threshold;
    char refreshTerrain;
    char padding_2d[11];
    long long emitterParticles;
} WorldRecenter_Recovered;

extern long long g_1eee540;
extern char g_1fab4a7;

void WorldRecenter_ctor(struct_0 *ptr)
{
    unsigned long long v4;  // x30
    unsigned long long v5;  // x21
    unsigned long long v6;  // x20
    unsigned long long v7;  // x19
    long long v8;  // x1
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x18]
    unsigned long long v2;  // [bp-0x10]
    unsigned long long v3;  // [bp-0x8]

    v0 = v4;
    v1 = v5;
    v2 = v6;
    v3 = v7;
    if (!(g_1fab4a7 & 1))
    {
        sub_f7d92c(&g_1eee540);
        g_1fab4a7 = 1;
    }
    ptr->field_28 = 0x442f0000;
    ptr->field_2c = 1;
    v8 = sub_f7d9d4(g_1eee540, 1);
    ptr->field_38 = v8;
    sub_f7d8d0((struct WorldRecenter_Recovered *)&ptr->field_38, v8);
    MonoBehaviour__ctor();
    return;
}
```
