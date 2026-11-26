# Native pseudocode: Footsteps

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `Footsteps.Start` — RVA `0xc9c3e8`

- Decompiled symbol: `Footsteps_Start`
- Metadata signature: `private void Start() { }`
- Native interval: `552` bytes
- Result: `pseudocode`
- Heuristic layout hint: `Footsteps_Recovered` matched 8 offsets against `Footsteps` metadata (confidence 0.80).

```c
typedef struct struct_1 {
    char padding_0[40];
    long long field_28;
} struct_1;

typedef struct Footsteps_Recovered {
    char padding_0[32];
    long long FPSWalkerComponent;
    long long FPSPlayerComponent;
    long long InputComponent;
    long long playerObj;
    char padding_40[304];
    long long aSource;
    long long terrain;
    long long terrainData;
    unsigned int terrainPos;
    unsigned int field_18c;
    unsigned int field_190;
} Footsteps_Recovered;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern long long g_1efcf38;
extern long long g_1efea78;
extern long long g_1efebb8;
extern long long g_1efebc0;
extern long long g_1efec08;
extern char g_1fab4a8;

long long Footsteps_Start(struct_2 *ptr)
{
    struct_1 *ptr5;  // x0
    long long v1;  // x1
    long long v10;  // x0
    struct_2 *p;  // x20
    struct_2 *v12;  // x20
    long long v13;  // x0
    struct_2 *v14;  // x20
    long long v15;  // x0
    unsigned long v16;  // x0
    long long v17;  // x1
    long long v18;  // x1
    unsigned long v19;  // x0
    struct_2 *addr;  // x20
    unsigned int v20;  // s1
    unsigned int v21;  // s2
    struct_2 *v3;  // x20
    long long v4;  // x0
    struct_2 *ptr3;  // x20
    struct_2 *v6;  // x20
    long long v7;  // x0
    struct_2 *ptr4;  // x20
    struct_2 *v9;  // x20

    if (!(g_1fab4a8 & 1))
    {
        sub_f7d92c(&g_1efcf38);
        sub_f7d92c(&g_1efea78);
        sub_f7d92c(&g_1efebb8);
        sub_f7d92c(&g_1efebc0);
        sub_f7d92c(&g_1efec08);
        sub_f7d92c(&g_1ef0c58);
        g_1fab4a8 = 1;
    }
    if (Camera__get_main(0) && Component__get_transform())
    {
        ptr5 = sub_1231bc8();
        if (ptr5)
        {
            v1 = ptr5->field_28;
            addr = ptr;
            addr->field_38 = v1;
            v3 = &addr->field_38;
            sub_f7d8d0(v3, v1);
            if (*((long long *)&v3->padding_0[0]))
            {
                v4 = sub_1249224(*((long long *)&v3->padding_0[0]), g_1efebc0);
                ptr3 = ptr;
                ptr3->field_20 = v4;
                v6 = &ptr3->field_20;
                sub_f7d8d0(v6, v4);
                if (*((long long *)&v6->padding_0[24]))
                {
                    v7 = sub_1249224(*((long long *)&v6->padding_0[24]), g_1efebb8);
                    ptr4 = ptr;
                    ptr4->field_28 = v7;
                    v9 = &ptr4->field_28;
                    sub_f7d8d0(v9, v7);
                    if (*((long long *)&v9->padding_0[16]))
                    {
                        v10 = sub_1249224(*((long long *)&v9->padding_0[16]), g_1efec08);
                        p = ptr;
                        p->field_30 = v10;
                        v12 = &p->field_30;
                        sub_f7d8d0(v12, v10);
                        if (*((long long *)&v12->padding_0[8]))
                        {
                            v13 = sub_124913c(*((long long *)&v12->padding_0[8]), g_1efea78);
                            v14 = &ptr->field_170;
                            ptr->field_170 = v13;
                            sub_f7d8d0(v14, v13);
                            if (ptr->field_170)
                            {
                                AudioSource__set_spatialBlend(ptr->field_170, 0);
                                if (*((long long *)&v14->padding_0[0]))
                                {
                                    AudioSource__set_playOnAwake(*((long long *)&v14->padding_0[0]), 0, 0);
                                    v15 = Terrain__get_activeTerrain(0);
                                    if (!g_1ef0c58->field_e0)
                                        sub_f7da5c(g_1ef0c58);
                                    v16 = Object__op_Implicit(v15, 0);
                                    if (!((char)v16 & 1))
                                        return v16;
                                    v17 = Terrain__get_activeTerrain(0);
                                    ptr->field_178 = v17;
                                    sub_f7d8d0(&ptr->field_178, v17);
                                    if (ptr->field_178)
                                    {
                                        v18 = Terrain__get_terrainData(ptr->field_178, 0);
                                        ptr->field_180 = v18;
                                        sub_f7d8d0(&ptr->field_180, v18);
                                        if (ptr->field_178 && Component__get_transform(ptr->field_178, 0))
                                        {
                                            v19 = Transform__get_position();
                                            ptr->field_188 = 0;
                                            ptr->field_18c = v20;
                                            ptr->field_190 = v21;
                                            return v19;
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

## `Footsteps.FootstepSfx` — RVA `0xc9c610`

- Decompiled symbol: `Footsteps_FootstepSfx`
- Metadata signature: `public void FootstepSfx() { }`
- Native interval: `1872` bytes
- Result: `pseudocode`
- Heuristic layout hint: `Footsteps_Recovered` matched 32 offsets against `Footsteps` metadata (confidence 1.00).

```c
typedef struct Footsteps_Recovered {
    char padding_0[32];
    struct struct_1 *FPSWalkerComponent;
    struct struct_2 *FPSPlayerComponent;
    struct struct_4 *InputComponent;
    char padding_38[8];
    long long materialType;
    unsigned int volumeAmt;
    char padding_4c[4];
    long long footStepClip;
    unsigned int terrainIndex;
    char onTerrain;
    char padding_5d[7];
    unsigned int dirtTerrainIndex2;
    char padding_68[4];
    unsigned int dirtStepVol;
    void* dirtSteps;
    char padding_78[12];
    unsigned int stoneStepVol;
    void* stoneSteps;
    char padding_90[12];
    unsigned int grassStepVol;
    void* grassSteps;
    char padding_a8[12];
    unsigned int gravelStepVol;
    void* gravelSteps;
    char padding_c0[12];
    unsigned int sandStepVol;
    void* sandSteps;
    unsigned int defaultStepVol;
    char padding_dc[4];
    void* defaultSteps;
    unsigned int woodStepVol;
    char padding_ec[4];
    void* woodSteps;
    unsigned int metalStepVol;
    char padding_fc[4];
    void* metalSteps;
    unsigned int waterSoundVol;
    char padding_10c[4];
    void* waterSounds;
    unsigned int climbSoundVol;
    char padding_11c[4];
    void* climbSounds;
    unsigned int proneStepVol;
    char padding_12c[4];
    void* proneSteps;
    char padding_138[56];
    long long aSource;
} Footsteps_Recovered;

typedef struct struct_5 {
    char padding_0[524];
    unsigned int field_20c;
} struct_5;

typedef struct struct_6 {
    char padding_0[552];
    char field_228;
    char padding_229[44];
    char field_255;
    char field_256;
    char padding_257[62];
    char field_295;
    char field_296;
    char padding_297[21];
    unsigned int field_2ac;
    char padding_2b0[44];
    char field_2dc;
} struct_6;

typedef struct struct_1 {
    char padding_0[552];
    char field_228;
    char padding_229[44];
    char field_255;
    char field_256;
    char padding_257[62];
    char field_295;
    char field_296;
    char padding_297[21];
    unsigned int field_2ac;
    char padding_2b0[44];
    char field_2dc;
} struct_1;

typedef struct struct_2 {
    char padding_0[524];
    unsigned int field_20c;
} struct_2;

typedef struct struct_4 {
    char padding_0[220];
    unsigned int field_dc;
    unsigned int field_e0;
} struct_4;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern long long g_1f09af8;
extern long long g_1f0a7c8;
extern long long g_1f0a7d0;
extern long long g_1f0c1a0;
extern long long g_1f0d7c8;
extern long long g_1f0dcd0;
extern long long g_1f0fbf0;
extern char g_1fab4a9;

struct_3 * Footsteps_FootstepSfx(struct_3 *ptr)
{
    struct_3 *v0;  // x0
    struct_3 *v1;  // x0
    struct_6 *ptr15;  // x8
    void* v11;  // x20
    unsigned int v12;  // w0
    unsigned long v13;  // x1
    struct_3 *ptr4;  // x20
    struct_3 *addr;  // x20
    unsigned int v16;  // s0
    void* v17;  // x20
    unsigned int v18;  // w0
    unsigned long v19;  // x1
    struct_3 *v2;  // x0
    struct_3 *ptr5;  // x20
    unsigned long v21;  // x0
    void* v22;  // x20
    unsigned int v23;  // w0
    unsigned long v24;  // x1
    struct_3 *ptr6;  // x20
    struct_3 *v26;  // x20
    unsigned int v27;  // s0
    struct_3 *v28;  // x0
    unsigned int v29;  // s1
    unsigned int v3;  // s0
    unsigned long v30;  // 4142
    long long v31;  // x0
    unsigned int v32;  // w0
    unsigned int v33;  // w8
    unsigned long v34;  // x20
    unsigned int v35;  // w0
    void* v36;  // x20
    unsigned int v37;  // w0
    unsigned long v38;  // x1
    struct_3 *ptr7;  // x20
    unsigned long v4;  // 4129
    struct_3 *p;  // x20
    unsigned int v41;  // s0
    void* v42;  // x20
    unsigned int v43;  // w0
    unsigned long v44;  // x1
    struct_3 *ptr8;  // x20
    void* v46;  // x20
    unsigned int v47;  // w0
    unsigned long v48;  // x1
    struct_3 *ptr9;  // x20
    unsigned int ptr3[57];  // x8
    unsigned long v50;  // 4102
    void* v51;  // x20
    unsigned int v52;  // w0
    unsigned long v53;  // x1
    struct_3 *ptr10;  // x20
    void* v55;  // x20
    unsigned int v56;  // w0
    unsigned long v57;  // x1
    struct_3 *ptr11;  // x20
    void* v59;  // x20
    unsigned int v6;  // s0
    unsigned int v60;  // w0
    unsigned long v61;  // x1
    struct_3 *ptr12;  // x20
    void* v63;  // x20
    unsigned int v64;  // w0
    unsigned long v65;  // x1
    struct_3 *ptr13;  // x20
    void* v67;  // x20
    unsigned int v68;  // w0
    unsigned long v69;  // x1
    unsigned long long v7;  // 4103
    struct_3 *ptr14;  // x20
    struct_3 *v71;  // x0
    unsigned long long v72;  // x0
    unsigned long v73;  // x0
    unsigned int v8;  // 4099
    unsigned long v9;  // 4115

    v0 = ptr;
    if (!(g_1fab4a9 & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c(&g_1f0dcd0);
        sub_f7d92c(&g_1f09af8);
        sub_f7d92c(&g_1f0a7d0);
        sub_f7d92c(&g_1f0c1a0);
        sub_f7d92c(&g_1f0d7c8);
        sub_f7d92c(&g_1f0a7c8);
        v1 = sub_f7d92c(&g_1f0fbf0);
        g_1fab4a9 = 1;
        v0 = v1;
    }
    v2 = v0;
    if (ptr->field_28)
    {
        v3 = ptr->field_28->field_20c;
        v4 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v3, 0x3f800000)) >> 5 & 3 | (unsigned long long)(CmpF(v3, 0x3f800000) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v3, 0x3f800000)) >> 5 & 3 | (unsigned long long)(CmpF(v3, 0x3f800000) & 1)) & ((unsigned long long)(char)(CmpF(v3, 0x3f800000)) >> 5 & 3 | (unsigned long long)(CmpF(v3, 0x3f800000) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if ((char)v4)
            return v2;
        ptr3 = ptr->field_30;
        if (ptr3)
        {
            v6 = ptr3[55];
            v7 = (((CmpF(v6, 0.0) >> 5 & 3 | CmpF(v6, 0.0) & 1) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - ((CmpF(v6, 0.0) >> 5 & 3 | CmpF(v6, 0.0) & 1) & (CmpF(v6, 0.0) >> 5 & 3 | CmpF(v6, 0.0) & 1) >> 1 & 1);
            if ((char)(v7 * 0x10000000 >> 30))
            {
                v6 = ptr3[56];
                v8 = CmpF(v6, 0.0);
                v9 = (((CmpF(v6, 0.0) >> 5 & 3 | CmpF(v6, 0.0) & 1) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1;
                if ((char)((v9 - ((CmpF(v6, 0.0) >> 5 & 3 | CmpF(v6, 0.0) & 1) & (v8 >> 5 & 3 | CmpF(v6, 0.0) & 1) >> 1 & 1)) * 0x10000000 >> 30))
                    return v2;
            }
            ptr15 = ptr->field_20;
            if (ptr15)
            {
                if (ptr15->field_2dc)
                {
                    v11 = ptr->field_130;
                    if (v11)
                    {
                        if (!(long long)v11[24])
                            return v2;
                        v12 = Random__Range(0);
                        if ((int)v11[24] > v12)
                        {
                            v13 = *((long long *)(32 + (char *)v11 + 8 * v12));
                            ptr4 = ptr;
                            ptr4->field_50 = v13;
                            addr = &ptr4->field_50;
                            sub_f7d8d0(addr, v13);
                            v16 = addr->field_d8;
                            goto LABEL_109c720;
                        }
                    }
                }
                else if (ptr15->field_295)
                {
                    v17 = ptr->field_120;
                    if (v17)
                    {
                        if (!(long long)v17[24])
                            return v2;
                        if (!ptr15->field_296)
                        {
                            v18 = Random__Range(0);
                            if ((int)v17[24] <= v18)
                                sub_f7db7c();
                            v19 = *((long long *)(32 + (char *)v17 + 8 * v18));
                            ptr5 = ptr;
                            ptr5->field_50 = v19;
                            addr = &ptr5->field_50;
                            sub_f7d8d0(addr, v19);
                            v16 = *((int *)&addr->padding_c0[8]);
                        }
                        else
                        {
                            return v2;
                        }
LABEL_109c720:
                        v21 = addr->field_120;
                        *((unsigned int *)&addr->padding_0[8]) = v16;
                        if (v21)
                            goto LABEL_109c72c;
                    }
                }
                else if (ptr15->field_255)
                {
                    v22 = ptr->field_110;
                    if (v22)
                    {
                        if (!(long long)v22[24])
                            return v2;
                        v23 = Random__Range(0);
                        if ((int)v22[24] <= v23)
                            sub_f7db7c();
                        v24 = *((long long *)(32 + (char *)v22 + 8 * v23));
                        ptr6 = ptr;
                        ptr6->field_50 = v24;
                        v26 = &ptr6->field_50;
                        sub_f7d8d0(v26, v24);
                        if (v26->field_30)
                        {
                            v27 = ptr->field_108;
                            v21 = ptr->field_170;
                            if (v26->field_30[2].padding_0[142])
                                v27 = ptr->field_108 * 0x3f000000;
                            ptr->field_48 = v27;
                            if (v21)
                                goto LABEL_109c72c;
                        }
                    }
                }
                else
                {
                    if (!ptr15->field_228)
                        return v2;
                    v28 = Time__get_time(0);
                    v29 = ptr15->field_2ac + 1050253722;
                    v30 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v29, v6)) >> 5 & 3 | (unsigned long long)(CmpF(v29, v6) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v29, v6)) >> 5 & 3 | (unsigned long long)(CmpF(v29, v6) & 1)) & ((unsigned long long)(char)(CmpF(v29, v6)) >> 5 & 3 | (unsigned long long)(CmpF(v29, v6) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                    if ((char)v30)
                        return v28;
                    if (ptr->field_5c)
                    {
                        v31 = Terrain__get_activeTerrain(0);
                        if (!g_1ef0c58->field_e0)
                            sub_f7da5c(g_1ef0c58);
                        if (!(Object__op_Implicit(v31, 0) & 1))
                            goto LABEL_109cd14;
                        if (Component__get_transform(ptr, 0))
                        {
                            Transform__get_position();
                            v32 = Footsteps__GetTerrainTextureIndex();
                            v33 = *((int *)&ptr->padding_5d[3]);
                            ptr->field_58 = v32;
                            if (v32 == v33 || v32 == ptr->field_64 || v32 == ptr->padding_68)
                                goto LABEL_109cc84;
                            if (v32 == *((int *)&ptr->padding_78[0]) || v32 == *((int *)&ptr->padding_78[4]) || v32 == *((int *)&ptr->padding_78[8]))
                                goto LABEL_109ca70;
                            if (v32 != *((int *)&ptr->padding_90[0]) && v32 != *((int *)&ptr->padding_90[4]) && v32 != *((int *)&ptr->padding_90[8]))
                            {
                                if (v32 == *((int *)&ptr->padding_a8[0]) || v32 == *((int *)&ptr->padding_a8[4]) || v32 == *((int *)&ptr->padding_a8[8]))
                                    goto LABEL_109caf4;
                                if (v32 == *((int *)&ptr->padding_c0[8]))
                                    goto LABEL_109cbbc;
                                goto LABEL_109cccc;
                            }
                        }
                    }
                    else
                    {
                        v34 = ptr->field_40;
                        v35 = PrivateImplementationDetails___ComputeStringHash(v34, 0);
                        if (1479220765 >= v35)
                        {
                            switch (v35)
                            {
                            case 81868168:
                                if (!(String__op_Equality(v34, g_1f0fbf0, 0) & 1))
                                    goto LABEL_109cccc;
                                v46 = ptr->field_f0;
                                if (v46 && (long long)v46[24])
                                {
                                    v47 = Random__Range(0);
                                    if ((int)v46[24] > v47)
                                    {
                                        v48 = *((long long *)(32 + (char *)v46 + 8 * v47));
                                        ptr9 = ptr;
                                        ptr9->field_50 = v48;
                                        p = &ptr9->field_50;
                                        sub_f7d8d0(p, v48);
                                        v41 = *((int *)&p->padding_90[8]);
                                        break;
                                    }
                                }
                                break;
                            case 1044434307:
                                if (!(String__op_Equality(v34, g_1f0d7c8, 0) & 1))
                                    goto LABEL_109cccc;
LABEL_109cbbc:
                                v42 = ptr->field_d0;
                                if (v42 && (long long)v42[24])
                                {
                                    v43 = Random__Range(0);
                                    if ((int)v42[24] > v43)
                                    {
                                        v44 = *((long long *)(32 + (char *)v42 + 8 * v43));
                                        ptr8 = ptr;
                                        ptr8->field_50 = v44;
                                        p = &ptr8->field_50;
                                        sub_f7d8d0(p, v44);
                                        v41 = *((int *)&p->padding_78[4]);
                                        break;
                                    }
                                }
                                break;
                            case 1479220765:
                                if (!(String__op_Equality(v34, g_1f0a7c8, 0) & 1))
                                    goto LABEL_109cccc;
                                v36 = ptr->field_a0;
                                if (v36 && (long long)v36[24])
                                {
                                    v37 = Random__Range(0);
                                    if ((int)v36[24] > v37)
                                    {
                                        v38 = *((long long *)(32 + (char *)v36 + 8 * v37));
                                        ptr7 = ptr;
                                        ptr7->field_50 = v38;
                                        p = &ptr7->field_50;
                                        sub_f7d8d0(p, v38);
                                        v41 = (unsigned int)p->padding_4c;
                                        break;
                                    }
                                }
                                break;
                            default:
LABEL_109cccc:
                                v67 = ptr->field_e0;
                                if (!v67)
                                {
                                    v73 = sub_f7db74();
                                    return sub_f7db74();
                                }
LABEL_109ccd4:
                                if ((long long)v67[24])
                                {
                                    v68 = Random__Range(0);
                                    if ((int)v67[24] <= v68)
                                        sub_f7db7c();
                                    v69 = *((long long *)(32 + (char *)v67 + 8 * v68));
                                    ptr14 = ptr;
                                    ptr14->field_50 = v69;
                                    p = &ptr14->field_50;
                                    sub_f7d8d0(p, v69);
                                    v41 = (int)p->field_88;
LABEL_109cd10:
                                    *((unsigned int *)&p->padding_0[8]) = v41;
                                }
LABEL_109cd14:
                                if (!g_1ef0c58->field_e0)
                                    sub_f7da5c(g_1ef0c58);
                                v71 = Object__op_Implicit(ptr->field_50, 0);
                                if (!((char)v71 & 1))
                                    return v71;
                                v21 = ptr->field_170;
                                if (v21)
                                {
LABEL_109c72c:
                                    AudioSource__set_clip(v21, ptr->field_50, 0);
                                    if (ptr->field_170)
                                    {
                                        AudioSource__set_volume(ptr->field_170, 0);
                                        if (ptr->field_170)
                                        {
                                            v72 = AudioSource__Play();
                                            return AudioSource__Play();
                                        }
                                    }
                                }
                            }
                        }
                        else if (2840670588 >= v35)
                        {
                            v50 = arm64g_calculate_condition(3, (unsigned long long)v35, 2840670588, 0);
                            if (!((char)v50))
                            {
                                if (v35 != 1842662042)
                                    goto LABEL_109cccc;
                                if (!(String__op_Equality(v34, g_1f0dcd0, 0) & 1))
                                    goto LABEL_109cccc;
LABEL_109ca70:
                                v51 = ptr->field_88;
                                if (v51 && (long long)v51[24])
                                {
                                    v52 = Random__Range(0);
                                    if ((int)v51[24] > v52)
                                    {
                                        v53 = *((long long *)(32 + (char *)v51 + 8 * v52));
                                        ptr10 = ptr;
                                        ptr10->field_50 = v53;
                                        p = &ptr10->field_50;
                                        sub_f7d8d0(p, v53);
                                        v41 = *((int *)((char *)&p->field_30 + 4));
                                        goto LABEL_109cd10;
                                    }
                                }
                            }
                            else
                            {
                                if (!(String__op_Equality(v34, g_1f0c1a0, 0) & 1))
                                    goto LABEL_109cccc;
                                v55 = ptr->field_100;
                                if (v55 && (long long)v55[24])
                                {
                                    v56 = Random__Range(0);
                                    if ((int)v55[24] > v56)
                                    {
                                        v57 = *((long long *)(32 + (char *)v55 + 8 * v56));
                                        ptr11 = ptr;
                                        ptr11->field_50 = v57;
                                        p = &ptr11->field_50;
                                        sub_f7d8d0(p, v57);
                                        v41 = *((int *)&p->padding_a8[0]);
                                        goto LABEL_109cd10;
                                    }
                                }
                            }
                        }
                        else
                        {
                            switch (v35)
                            {
                            case 2948072384:
                                if (!(String__op_Equality(v34, g_1f09af8, 0) & 1))
                                    goto LABEL_109cccc;
LABEL_109cc84:
                                v63 = ptr->field_70;
                                if (v63 && (long long)v63[24])
                                {
                                    v64 = Random__Range(0);
                                    if ((int)v63[24] > v64)
                                    {
                                        v65 = *((long long *)(32 + (char *)v63 + 8 * v64));
                                        ptr13 = ptr;
                                        ptr13->field_50 = v65;
                                        p = &ptr13->field_50;
                                        sub_f7d8d0(p, v65);
                                        v41 = *((int *)&p->padding_0[28]);
                                        break;
                                    }
                                }
                                break;
                            case 4176637722:
                                if (!(String__op_Equality(v34, g_1f0a7d0, 0) & 1))
                                    goto LABEL_109cccc;
LABEL_109caf4:
                                v59 = ptr->field_b8;
                                if (v59 && (long long)v59[24])
                                {
                                    v60 = Random__Range(0);
                                    if ((int)v59[24] > v60)
                                    {
                                        v61 = *((long long *)(32 + (char *)v59 + 8 * v60));
                                        ptr12 = ptr;
                                        ptr12->field_50 = v61;
                                        p = &ptr12->field_50;
                                        sub_f7d8d0(p, v61);
                                        v41 = p->field_64;
                                        break;
                                    }
                                }
                                break;
                            default:
LABEL_109cccc:
                                v67 = ptr->field_e0;
                                if (!v67)
                                {
                                    v73 = sub_f7db74();
                                    return sub_f7db74();
                                }
                                goto LABEL_109ccd4;
                            }
                        }
                    }
                }
            }
        }
    }
    v73 = sub_f7db74();
    return sub_f7db74();
}
```

## `Footsteps.GetTerrainTextureIndex` — RVA `0xc9cd60`

- Decompiled symbol: `Footsteps_GetTerrainTextureIndex`
- Metadata signature: `private int GetTerrainTextureIndex(Vector3 WorldPos) { }`
- Native interval: `112` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned int field_18;
} struct_0;

unsigned long long Footsteps_GetTerrainTextureIndex(void)
{
    struct_0 *ptr;  // x0
    unsigned long i;  // x9
    unsigned long long v2;  // x0
    unsigned long long idx;  // x10
    unsigned int v4;  // s0
    unsigned int v5;  // s1
    unsigned long v6;  // 4137
    unsigned long v7;  // 4109

    ptr = Footsteps__GetTexturesAtPoint();
    if (ptr)
    {
        i = ptr->field_18;
        if ((__ROL__(i, 32) & 0xffffffff00000000) < 1)
            return 0;
        v2 = 0;
        idx = 0;
        v4 = 0;
        while (i != idx)
        {
            v5 = *((int *)&ptr[1].padding_0[4 + 4 * idx]);
            v6 = arm64g_calculate_condition(192, (((((unsigned long long)(char)(CmpF(v5, v4)) >> 5 & 3 | (unsigned long long)(CmpF(v5, v4) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v5, v4)) >> 5 & 3 | (unsigned long long)(CmpF(v5, v4) & 1)) & ((unsigned long long)(char)(CmpF(v5, v4)) >> 5 & 3 | (unsigned long long)(CmpF(v5, v4) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
            if ((char)v6)
                v2 = idx & 4294967295;
            else
                v2 &= 4294967295;
            idx += 1;
            v7 = arm64g_calculate_condition(192, (((((unsigned long long)(char)(CmpF(v5, v4)) >> 5 & 3 | (unsigned long long)(CmpF(v5, v4) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v5, v4)) >> 5 & 3 | (unsigned long long)(CmpF(v5, v4) & 1)) & ((unsigned long long)(char)(CmpF(v5, v4)) >> 5 & 3 | (unsigned long long)(CmpF(v5, v4) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
            if ((char)v7)
                v4 = v5;
            else
                v4 = v4;
            if ((i * 0x100000000 >> 63 & 0xffffffff00000000 | i & 4294967295) == idx)
                return v2;
        }
        sub_f7db7c();
    }
    sub_f7db74();
}
```

## `Footsteps.GetTexturesAtPoint` — RVA `0xc9cdd0`

- Decompiled symbol: `Footsteps_GetTexturesAtPoint`
- Metadata signature: `private float[] GetTexturesAtPoint(Vector3 WorldPos) { }`
- Native interval: `420` bytes
- Result: `pseudocode`
- Heuristic layout hint: `Footsteps_Recovered` matched 2 offsets against `Footsteps` metadata (confidence 0.67).

```c
typedef struct struct_3 {
    char padding_0[16];
    struct struct_4 *field_10;
    unsigned int field_18;
} struct_3;

typedef struct Footsteps_Recovered {
    char padding_0[384];
    struct struct_0 *terrainData;
    unsigned int terrainPos;
    char padding_18c[4];
    unsigned int field_190;
} Footsteps_Recovered;

typedef struct struct_0 {
    char padding_0[16];
    struct struct_1 *field_10;
    unsigned int field_18;
} struct_0;

typedef struct struct_4 {
    unsigned int field_0;
    char padding_4[12];
    unsigned int field_10;
    char padding_14[12];
    unsigned int field_20;
} struct_4;

typedef struct struct_1 {
    unsigned int field_0;
    char padding_4[12];
    unsigned int field_10;
    char padding_14[12];
    unsigned int field_20;
} struct_1;

extern char g_1fab4aa;

struct_3 * Footsteps_GetTexturesAtPoint(struct_2 *ptr)
{
    struct_0 *ptr3;  // x0
    unsigned int v1;  // w0
    struct_0 *p;  // x19
    unsigned int v11;  // w0
    unsigned long v12;  // x8
    unsigned int addr[9];  // x10
    unsigned long long index;  // x9
    unsigned int v15;  // w11
    unsigned int v2;  // s0
    unsigned int v3;  // s0
    unsigned int v4;  // 4113
    unsigned long v5;  // 4172
    unsigned int v6;  // s2
    unsigned int v7;  // s0
    unsigned int v8;  // 4111
    unsigned long v9;  // 4168

    if (!(g_1fab4aa & 1))
    {
        sub_f7d92c("1)");
        g_1fab4aa = 1;
    }
    ptr3 = ptr->field_180;
    if (ptr3)
    {
        TerrainData__get_size(ptr3, 0);
        ptr3 = ptr->field_180;
        if (ptr3)
        {
            v1 = TerrainData__get_alphamapWidth(ptr3, 0);
            ptr3 = ptr->field_180;
            v3 = (v2 - ptr->field_188) / v2 * v1;
            v4 = CmpF(v3, 0x7f800000);
            v5 = (((CmpF(v3, 0x7f800000) >> 5 & 3 | CmpF(v3, 0x7f800000) & 1) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1;
            if (ptr3)
            {
                TerrainData__get_size(ptr3, 0);
                ptr3 = ptr->field_180;
                if (ptr3)
                {
                    ptr3 = TerrainData__get_alphamapHeight(ptr3, 0);
                    if (ptr->field_180)
                    {
                        v7 = (v6 - ptr->field_190) / 0x7f800000 * (unsigned int)ptr3;
                        v8 = CmpF(v7, 0x7f800000);
                        v9 = (((CmpF(v7, 0x7f800000) >> 5 & 3 | CmpF(v7, 0x7f800000) & 1) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1;
                        ptr3 = TerrainData__GetAlphamaps();
                        if (ptr3)
                        {
                            p = ptr3;
                            v11 = Array__GetUpperBound();
                            ptr3 = sub_f7d9d4(g_1eee368, v11 + 1);
                            if (ptr3)
                            {
                                v12 = ptr3->field_18;
                                if ((__ROL__(v12, 32) & 0xffffffff00000000) < 1)
                                    return ptr3;
                                addr = p->field_10;
                                index = 0;
                                v15 = addr[0];
                                while (v15 && addr[4] && addr[8] > index && v12 > index)
                                {
                                    *((int *)&ptr3[1].padding_0[4 + 4 * index]) = *((int *)&p[1].padding_0[4 + 4 * index]);
                                    if ((v12 * 0x100000000 >> 63 & 0xffffffff00000000 | v12 & 4294967295) == index + 1)
                                        return ptr3;
                                }
                                ptr3 = sub_f7db7c();
                            }
                        }
                    }
                }
            }
        }
    }
    sub_f7db74(ptr3);
}
```

## `Footsteps.ctor` — RVA `0xc9cf74`

- Decompiled symbol: `Footsteps_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `88` bytes
- Result: `pseudocode`
- Heuristic layout hint: `Footsteps_Recovered` matched 18 offsets against `Footsteps` metadata (confidence 1.00).

```c
typedef struct Footsteps_Recovered {
    char padding_0[72];
    unsigned int volumeAmt;
    char padding_4c[24];
    unsigned long long dirtTerrainIndex2;
    unsigned int dirtStepVol;
    char padding_70[12];
    unsigned long long stoneTerrainIndex2;
    unsigned int stoneStepVol;
    char padding_88[12];
    unsigned long long grassTerrainIndex2;
    unsigned int grassStepVol;
    char padding_a0[12];
    unsigned long long gravelTerrainIndex2;
    unsigned int gravelStepVol;
    char padding_b8[12];
    unsigned long long sandTerrainIndex2;
    unsigned int sandStepVol;
    char padding_d0[8];
    unsigned int defaultStepVol;
    char padding_dc[12];
    unsigned int woodStepVol;
    char padding_ec[12];
    unsigned int metalStepVol;
    char padding_fc[12];
    unsigned int waterSoundVol;
    char padding_10c[12];
    unsigned int climbSoundVol;
    char padding_11c[12];
    unsigned int proneStepVol;
    char padding_12c[52];
    unsigned int foliageRustleVol;
} Footsteps_Recovered;

long long Footsteps_ctor(struct_0 *ptr)
{
    ptr->field_48 = 0x3f800000;
    *((unsigned long long *)&(&ptr->padding_4c)[1]) = 18446744073709551615;
    *((unsigned int *)((char *)&ptr->field_64 + 4)) = 0x3f800000;
    *((unsigned long long *)&ptr->padding_70[8]) = 18446744073709551615;
    *((unsigned int *)((char *)&ptr->field_7c + 4)) = 0x3f800000;
    *((unsigned long long *)&ptr->padding_88[8]) = 18446744073709551615;
    *((unsigned int *)((char *)&ptr->field_94 + 4)) = 0x3f800000;
    *((unsigned long long *)&ptr->padding_a0[8]) = 18446744073709551615;
    *((unsigned int *)((char *)&ptr->field_ac + 4)) = 0x3f800000;
    *((unsigned long long *)&ptr->padding_b8[8]) = 18446744073709551615;
    *((unsigned int *)((char *)&ptr->field_c4 + 4)) = 0x3f800000;
    *((unsigned int *)&ptr->padding_d0[4]) = 0x3f800000;
    *((unsigned int *)&ptr->padding_dc[8]) = 0x3f800000;
    *((unsigned int *)&ptr->padding_ec[8]) = 0x3f800000;
    *((unsigned int *)&ptr->padding_fc[8]) = 0x3f800000;
    *((unsigned int *)&ptr->padding_10c[8]) = 0x3f800000;
    *((unsigned int *)&ptr->padding_11c[8]) = 0x3f800000;
    *((unsigned int *)&ptr->padding_12c[48]) = 0x3f800000;
}
```
