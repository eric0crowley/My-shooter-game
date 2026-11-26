# Native pseudocode: WaterZone

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `WaterZone.Start` — RVA `0xc99e2c`

- Decompiled symbol: `WaterZone_Start`
- Metadata signature: `private void Start() { }`
- Native interval: `1732` bytes
- Result: `pseudocode`
- Heuristic layout hint: `WaterZone_Recovered` matched 30 offsets against `WaterZone` metadata (confidence 0.77).

```c
typedef struct WaterZone_Recovered {
    char padding_0[32];
    struct struct_5 *FPSWalkerComponent;
    long long FootstepsComponent;
    long long PlayerWeaponsComponent;
    struct struct_8 *WeaponEffectsComponent;
    long long playerObj;
    long long weaponObj;
    char swimTimeState;
    char padding_51[7];
    long long audioSource;
    long long underwaterSound;
    char padding_68[8];
    long long waterPlane;
    unsigned int underwaterYpos;
    char padding_7c[4];
    long long waterPlaneTop;
    char padding_88[16];
    long long rippleEffect;
    char padding_a0[8];
    long long bubblesEffect;
    char padding_b0[8];
    long long waterSplash;
    char padding_c0[16];
    long long splashTrail;
    char padding_d8[24];
    long long SunlightObj;
    char padding_f8[16];
    unsigned int origSunightColor;
    unsigned int field_10c;
    unsigned int field_110;
    unsigned int field_114;
    char padding_118[20];
    char useCausticsLight;
    char padding_12d[3];
    long long causticsLight;
    char padding_138[8];
    struct struct_6 *frames;
    char padding_148[36];
    char fogEnabled;
    char padding_16d[3];
    unsigned int origFogMode;
    unsigned int origFogColor;
    unsigned int field_178;
    unsigned int field_17c;
    unsigned int field_180;
    unsigned int origLightColor;
    unsigned int field_188;
    unsigned int field_18c;
    unsigned int field_190;
    unsigned int origFogDensity;
    unsigned int origLinearFogStart;
    unsigned int origLinearFogEnd;
    long long myTransform;
    long long mainCamTransform;
} WaterZone_Recovered;

typedef struct struct_3 {
    char padding_0[40];
    long long field_28;
} struct_3;

typedef struct struct_4 {
    char padding_0[48];
    long long field_30;
} struct_4;

typedef struct struct_9 {
    char padding_0[360];
    unsigned long long field_168;
    char padding_170[229];
    unsigned int field_255;
    char field_259;
} struct_9;

typedef struct struct_13 {
    char padding_0[40];
    long long field_28;
} struct_13;

typedef struct struct_10 {
    char padding_0[136];
    struct struct_11 *field_88;
} struct_10;

typedef struct struct_12 {
    char padding_0[24];
    int field_18;
    char padding_1c[4];
    long long field_20;
} struct_12;

typedef struct struct_14 {
    char padding_0[24];
    unsigned long long field_18;
} struct_14;

typedef struct struct_5 {
    char padding_0[360];
    long long field_168;
    char padding_170[229];
    unsigned int field_255;
    char field_259;
} struct_5;

typedef struct struct_8 {
    char padding_0[136];
    long long field_88;
    long long field_90;
    long long field_98;
    long long field_a0;
} struct_8;

typedef struct struct_6 {
    char padding_0[24];
    unsigned long long field_18;
} struct_6;

typedef struct struct_11 {
    char padding_0[136];
    unsigned long long field_88;
    unsigned long long field_90;
    unsigned long long field_98;
    unsigned long long field_a0;
} struct_11;

typedef struct struct_2 {
    char padding_0[224];
    unsigned int field_e0;
} struct_2;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

typedef struct struct_1 {
    char padding_0[224];
    unsigned int field_e0;
} struct_1;

extern long long g_1eeb668;
extern long long g_1eee238;
extern struct_0 *g_1ef0c58;
extern struct_1 *g_1ef0e48;
extern struct_2 *g_1ef1f08;
extern long long g_1efcf38;
extern long long g_1efcf70;
extern long long g_1efcfb0;
extern long long g_1efea78;
extern long long g_1efebb8;
extern long long g_1efebc0;
extern long long g_1efec90;
extern long long g_1f0c5d8;
extern char g_1fab49e;

void WaterZone_Start(struct_7 *ptr)
{
    long long v0;  // x1
    long long v1;  // x1
    struct_9 *v10;  // x0
    struct_7 *ptr3;  // x20
    struct_7 *v12;  // x20
    long long v13;  // x0
    struct_7 *ptr4;  // x21
    struct_7 *v15;  // x21
    long long v16;  // x1
    struct_7 *ptr5;  // x0
    struct_13 *v18;  // x0
    struct_10 *ptr17;  // x0
    struct_3 *ptr18;  // x0
    unsigned long long v20[21];  // x1
    struct_7 *ptr6;  // x21
    struct_7 *v22;  // x21
    unsigned long v23;  // x1
    struct_7 *ptr7;  // x21
    struct_7 *v25;  // x21
    unsigned long v26;  // x1
    struct_7 *ptr8;  // x21
    struct_7 *v28;  // x21
    unsigned long v29;  // x1
    long long v3;  // x1
    struct_7 *ptr9;  // x21
    struct_7 *v31;  // x21
    unsigned long v32;  // x1
    struct_7 *ptr10;  // x21
    struct_7 *v34;  // x21
    unsigned long v35;  // x0
    long long v36;  // x0
    struct_7 *ptr11;  // x20
    struct_7 *v38;  // x20
    unsigned int v39;  // s1
    struct_7 *ptr12;  // x20
    unsigned int v40;  // s2
    unsigned int v41;  // s3
    struct_7 *ptr13;  // x20
    long long v43;  // x21
    struct_7 *p;  // x20
    long long v45;  // x0
    long long v46;  // x0
    struct_12 *ptr19;  // x0
    unsigned int v48;  // w8
    struct_12 *ptr14;  // x21
    struct_7 *v5;  // x20
    unsigned int v50;  // w23
    struct_12 *v51;  // x24
    struct_12 *ptr16;  // x24
    long long v53;  // x1
    struct_9 *addr;  // x8
    struct_4 *ptr20;  // x0
    long long v7;  // x1
    struct_7 *ptr15;  // x20
    struct_7 *v9;  // x20

    if (!(g_1fab49e & 1))
    {
        sub_f7d92c(&g_1efcf38);
        sub_f7d92c(&g_1efcf70);
        sub_f7d92c(&g_1efcfb0);
        sub_f7d92c(&g_1efea78);
        sub_f7d92c(&g_1efebb8);
        sub_f7d92c(&g_1efebc0);
        sub_f7d92c(&g_1efec90);
        sub_f7d92c(&g_1eee238);
        sub_f7d92c(&g_1eeb668);
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c(&g_1ef0e48);
        sub_f7d92c(&g_1ef1f08);
        sub_f7d92c(&g_1f0c5d8);
        g_1fab49e = 1;
    }
    v0 = Component__get_transform(ptr, 0);
    ptr->field_1a0 = v0;
    sub_f7d8d0((struct WaterZone_Recovered *)&ptr->field_1a0, v0);
    if (Camera__get_main(0))
    {
        v1 = Component__get_transform();
        ptr->field_1a8 = v1;
        sub_f7d8d0((struct WaterZone_Recovered *)&ptr->field_1a8, v1);
        if (ptr->field_1a8 && (ptr18 = (struct_3 *)sub_1231bc8(ptr->field_1a8, g_1efcf38), ptr18))
        {
            v3 = ptr18->field_28;
            ptr12 = ptr;
            ptr12->field_40 = v3;
            v5 = &ptr12->field_40;
            sub_f7d8d0(v5, v3);
            if (*((long long *)&v5->padding_148[32]) && (ptr20 = (struct_4 *)sub_1231bc8(*((long long *)&v5->padding_148[32]), g_1efcf38), ptr20))
            {
                v7 = ptr20->field_30;
                ptr15 = ptr;
                ptr15->field_48 = v7;
                v9 = &ptr15->field_48;
                sub_f7d8d0(v9, v7);
                if (*((long long *)&v9->padding_0[8]))
                {
                    v10 = sub_1249224(*((long long *)&v9->padding_0[8]), g_1efebc0);
                    ptr3 = ptr;
                    ptr3->field_20 = v10;
                    v12 = &ptr3->field_20;
                    sub_f7d8d0(v12, v10);
                    if (*((long long *)&v12->field_188) && Transform__get_parent(*((long long *)&v12->field_188), 0) && Component__get_transform())
                    {
                        v13 = sub_1231bc8();
                        ptr4 = ptr;
                        ptr4->field_28 = v13;
                        v15 = &ptr4->field_28;
                        sub_f7d8d0(v15, v13);
                        if (v15->field_20)
                        {
                            v16 = sub_1249224(v15->field_20, g_1efec90);
                            ptr5 = ptr;
                            ptr5->field_30 = v16;
                            sub_f7d8d0((struct WaterZone_Recovered *)&ptr5->field_30, v16);
                            if (Camera__get_main(0) && (v18 = (struct_13 *)sub_1231bc8(), v18 && v18->field_28 && (ptr17 = (struct_10 *)sub_1249224(v18->field_28, g_1efebb8), ptr17)))
                            {
                                v20 = ptr17->field_88;
                                ptr6 = ptr;
                                ptr6->field_38 = v20;
                                v22 = &ptr6->field_38;
                                sub_f7d8d0(v22, v20);
                                if (*((long long *)&v22->padding_0[0]))
                                {
                                    v23 = *((long long *)(*((long long *)&v22->padding_0[0]) + 136));
                                    ptr7 = ptr;
                                    ptr7->field_b8 = v23;
                                    v25 = &ptr7->field_b8;
                                    sub_f7d8d0(v25, v23);
                                    if (v25->field_80)
                                    {
                                        v26 = *((long long *)(v25->field_80 + 144));
                                        ptr8 = ptr;
                                        ptr8->field_98 = v26;
                                        v28 = &ptr8->field_98;
                                        sub_f7d8d0(v28, v26);
                                        if (v28->field_60)
                                        {
                                            v29 = *((long long *)(v28->field_60 + 152));
                                            ptr9 = ptr;
                                            ptr9->field_a8 = v29;
                                            v31 = &ptr9->field_a8;
                                            sub_f7d8d0(v31, v29);
                                            if (v31->field_70)
                                            {
                                                v32 = *((long long *)(v31->field_70 + 160));
                                                ptr10 = ptr;
                                                ptr10->field_d0 = v32;
                                                v34 = &ptr10->field_d0;
                                                sub_f7d8d0(v34, v32);
                                                if (v34->field_d0 && (v35 = (unsigned long)sub_1231bc8(v34->field_d0, g_1efcf70), *((long long *)&v12->padding_0[0])))
                                                {
                                                    if (!g_1ef0e48->field_e0)
                                                        sub_f7da5c(g_1ef0e48);
                                                    Physics__IgnoreCollision(v35, *((long long *)(*((long long *)&v12->padding_0[0]) + 360)), 1, 0);
                                                    if (Component__get_gameObject(ptr, 0))
                                                    {
                                                        v36 = sub_124913c();
                                                        ptr11 = ptr;
                                                        ptr11->field_58 = v36;
                                                        v38 = &ptr11->field_58;
                                                        sub_f7d8d0(v38, v36);
                                                        if (*((long long *)&v38->padding_0[0]) && (AudioSource__set_clip(*((long long *)&v38->padding_0[0]), ptr->field_60, 0), ptr->field_58 && (AudioSource__set_loop(ptr->field_58, 1, 0), *((long long *)&v38->padding_0[0]))))
                                                        {
                                                            AudioSource__set_volume(*((long long *)&v38->padding_0[0]), 0);
                                                            ptr->field_16c = (char)RenderSettings__get_fog(0) & 1;
                                                            RenderSettings__get_fogColor(0);
                                                            ptr->field_174 = 1061997773;
                                                            ptr->field_178 = v39;
                                                            ptr->field_17c = v40;
                                                            ptr->field_180 = v41;
                                                            RenderSettings__get_fogDensity(0);
                                                            ptr->field_194 = 1061997773;
                                                            ptr->field_170 = RenderSettings__get_fogMode(0);
                                                            RenderSettings__get_fogStartDistance(0);
                                                            ptr->field_198 = 1061997773;
                                                            RenderSettings__get_fogEndDistance(0);
                                                            ptr->field_19c = 1061997773;
                                                            RenderSettings__get_ambientLight(0);
                                                            ptr13 = ptr;
                                                            v43 = ptr13->field_f0;
                                                            p = &ptr13->field_f0;
                                                            *((unsigned int *)&p->padding_88[12]) = 1061997773;
                                                            *((unsigned int *)&p->field_98) = v39;
                                                            *((unsigned int *)((char *)&p->field_98 + 4)) = v40;
                                                            *((unsigned int *)&p->padding_a0[0]) = v41;
                                                            if (!g_1ef0c58->field_e0)
                                                                sub_f7da5c(g_1ef0c58);
                                                            if (!((char)Object__op_Implicit(v43, 0) & 1))
                                                            {
                                                                if (!g_1ef1f08->field_e0)
                                                                    sub_f7da5c(g_1ef1f08);
                                                                v45 = Type__GetTypeFromHandle(g_1eeb668, 0);
                                                                if (!g_1ef0c58->field_e0)
                                                                    sub_f7da5c(g_1ef0c58);
                                                                v46 = Object__FindObjectsOfType(v45, 0);
                                                                ptr19 = sub_f7da60(v46, g_1eee238);
                                                                if (ptr19)
                                                                {
                                                                    v48 = ptr19->field_18;
                                                                    ptr14 = ptr19;
                                                                    if (ptr19->field_18 < 1)
                                                                        goto LABEL_109a334;
                                                                    v50 = 0;
                                                                    while (true)
                                                                    {
                                                                        if (v48 <= v50)
                                                                            sub_f7db7c(ptr19);
                                                                        v51 = &ptr14->padding_0[8 * v50];
                                                                        ptr16 = &v51->field_20;
                                                                        if (!v51->field_20)
                                                                            break;
                                                                        ptr19 = Light__get_type(v51->field_20, 0);
                                                                        if ((unsigned int)ptr19 == 1)
                                                                        {
                                                                            if (ptr14->field_18 <= v50)
                                                                                sub_f7db7c(ptr19);
                                                                            if (!*((long long *)&ptr16->padding_0[0]) || !Component__get_gameObject(*((long long *)&ptr16->padding_0[0]), 0))
                                                                                break;
                                                                            ptr19 = GameObject__get_activeInHierarchy();
                                                                            if (!(ptr19 & 1))
                                                                                goto LABEL_109a304;
                                                                            if (ptr14->field_18 <= v50)
                                                                                sub_f7db7c(ptr19);
                                                                            v53 = *((long long *)&ptr16->padding_0[0]);
                                                                            *((long long *)&p->padding_0[0]) = v53;
                                                                            sub_f7d8d0(p, v53);
                                                                            goto LABEL_109a334;
                                                                        }
                                                                        else
                                                                        {
LABEL_109a304:
                                                                            v48 = ptr14->field_18;
                                                                            v50 += 1;
                                                                            if (v50 >= v48)
                                                                                goto LABEL_109a334;
                                                                        }
                                                                    }
                                                                }
                                                            }
                                                            else
                                                            {
LABEL_109a334:
                                                                if (!g_1ef0c58->field_e0)
                                                                    sub_f7da5c(g_1ef0c58);
                                                                if (!((char)Object__op_Implicit(*((long long *)&p->padding_0[0]), 0) & 1))
                                                                {
LABEL_109a378:
                                                                    if (!g_1ef0c58->field_e0)
                                                                        sub_f7da5c(g_1ef0c58);
                                                                    if (((char)Object__op_Implicit(ptr->field_70, 0) & 1))
                                                                    {
                                                                        if (ptr->field_70 && Component__get_gameObject(ptr->field_70, 0) && (GameObject__SetActive(), ptr->field_70 && Component__get_transform(ptr->field_70, 0)))
                                                                        {
                                                                            Transform__get_position();
                                                                            ptr->field_78 = v39;
                                                                            goto LABEL_109a3dc;
                                                                        }
                                                                    }
                                                                    else
                                                                    {
LABEL_109a3dc:
                                                                        if (ptr->field_12c)
                                                                        {
                                                                            if (!g_1ef0c58->field_e0)
                                                                                sub_f7da5c(g_1ef0c58);
                                                                            if (!(Object__op_Implicit(ptr->field_130, 0) & 1))
                                                                                goto LABEL_109a428;
                                                                            if (ptr->field_130 && Component__get_gameObject(ptr->field_130, 0))
                                                                            {
                                                                                GameObject__SetActive();
                                                                                goto LABEL_109a428;
                                                                            }
                                                                        }
                                                                        else
                                                                        {
LABEL_109a428:
                                                                            if (!g_1ef0c58->field_e0)
                                                                                sub_f7da5c(g_1ef0c58);
                                                                            if (((char)Object__op_Implicit(ptr->field_80, 0) & 1))
                                                                            {
                                                                                if (ptr->field_80 && Component__get_gameObject(ptr->field_80, 0))
                                                                                {
                                                                                    GameObject__SetActive();
                                                                                    goto LABEL_109a46c;
                                                                                }
                                                                            }
                                                                            else
                                                                            {
LABEL_109a46c:
                                                                                addr = ptr->field_20;
                                                                                ptr->field_50 = 0;
                                                                                if (addr)
                                                                                {
                                                                                    *((unsigned int *)&(&addr->padding_170)[1]) = 0;
                                                                                    *((char *)&addr->field_255 + 1) = 1;
                                                                                    if (ptr->field_140 && !ptr->field_140->field_18)
                                                                                        return;
                                                                                }
                                                                            }
                                                                        }
                                                                    }
                                                                }
                                                                else if (*((long long *)&p->padding_0[0]))
                                                                {
                                                                    Light__get_color(*((long long *)&p->padding_0[0]), 0);
                                                                    ptr->field_108 = 1061997773;
                                                                    ptr->field_10c = v39;
                                                                    ptr->field_110 = v40;
                                                                    ptr->field_114 = v41;
                                                                    goto LABEL_109a378;
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
    sub_f7db7c(sub_f7db74());
}
```

## `WaterZone.Update` — RVA `0xc9a4f0`

- Decompiled symbol: `WaterZone_Update`
- Metadata signature: `private void Update() { }`
- Native interval: `316` bytes
- Result: `pseudocode`
- Heuristic layout hint: `WaterZone_Recovered` matched 5 offsets against `WaterZone` metadata (confidence 1.00).

```c
typedef struct WaterZone_Recovered {
    char padding_0[32];
    struct struct_0 *FPSWalkerComponent;
    char padding_28[24];
    long long playerObj;
    char padding_48[8];
    char swimTimeState;
    char padding_51[335];
    long long myTransform;
    long long mainCamTransform;
} WaterZone_Recovered;

typedef struct struct_0 {
    char padding_0[597];
    unsigned int field_255;
    char field_259;
} struct_0;

extern long long g_1efcf70;
extern char g_1fab49f;

long long WaterZone_Update(struct_1 *ptr)
{
    long long v5;  // x0
    struct_0 *p;  // x8
    unsigned long long v7;  // x0
    unsigned long long v8;  // x0
    char v0;  // [bp-0x68]
    unsigned long long v1;  // [bp-0x58]
    char flag;  // [bp-0x50], Other Possible Types: unsigned long long
    unsigned long long choice;  // [bp-0x48]
    unsigned long long v4;  // [bp-0x40]

    if (!(g_1fab49f & 1))
    {
        sub_f7d92c(&g_1efcf70);
        g_1fab49f = 1;
    }
    flag = 0;
    choice = 0;
    v4 = 0;
    v5 = ptr->field_40;
    if (v5)
    {
        v5 = GameObject__get_activeInHierarchy(v5, 0);
        if (!((char)v5 & 1))
        {
            p = ptr->field_20;
            ptr->field_50 = 0;
            if (p)
            {
                *((unsigned int *)&(&p->padding_0)[1]) = 0;
                *((char *)&p->field_255 + 1) = 1;
                WaterZone__StopUnderwaterEffects();
                goto LABEL_109a568;
            }
        }
        else
        {
LABEL_109a568:
            v5 = ptr->field_1a0;
            if (v5)
            {
                v5 = sub_1231bc8(v5, g_1efcf70);
                if (v5)
                {
                    Collider__get_bounds();
                    memcpy(&flag, &v0, 16);
                    v4 = v1;
                    v5 = ptr->field_1a8;
                    if (v5)
                    {
                        Transform__get_position(v5, 0);
                        v5 = ptr->field_1a8;
                        if (v5)
                        {
                            Transform__get_up(v5, 0);
                            if (!((char)Bounds__Contains(&flag, 0) & 1))
                            {
                                v8 = WaterZone__StopUnderwaterEffects();
                                return WaterZone__StopUnderwaterEffects();
                            }
                            v7 = WaterZone__StartUnderwaterEffects(ptr);
                            return WaterZone__StartUnderwaterEffects(ptr);
                        }
                    }
                }
            }
        }
    }
    sub_f7db74(v5);
}
```

## `WaterZone.StopUnderwaterEffects` — RVA `0xc9a62c`

- Decompiled symbol: `WaterZone_StopUnderwaterEffects`
- Metadata signature: `private void StopUnderwaterEffects() { }`
- Native interval: `680` bytes
- Result: `pseudocode`
- Heuristic layout hint: `WaterZone_Recovered` matched 13 offsets against `WaterZone` metadata (confidence 1.00).

```c
typedef struct WaterZone_Recovered {
    char padding_0[32];
    struct struct_3 *FPSWalkerComponent;
    char padding_28[48];
    struct WaterZone_Recovered *audioSource;
    char padding_60[8];
    void* aboveWaterAudioSources;
    struct WaterZone_Recovered *waterPlane;
    char padding_78[8];
    struct WaterZone_Recovered *waterPlaneTop;
    char padding_88[32];
    struct WaterZone_Recovered *bubblesEffect;
    char padding_b0[56];
    char changeSunlightColor;
    char padding_e9[7];
    struct WaterZone_Recovered *SunlightObj;
    char padding_f8[52];
    char useCausticsLight;
    char padding_12d[3];
    struct WaterZone_Recovered *causticsLight;
    char padding_138[16];
    char effectsState;
    char padding_149[35];
    char fogEnabled;
    char padding_16d[3];
    unsigned int origFogMode;
} WaterZone_Recovered;

typedef struct struct_7 {
    char padding_0[40];
    struct struct_8 *field_28;
} struct_7;

typedef struct struct_6 {
    char padding_0[152];
    struct struct_5 *field_98;
} struct_6;

typedef struct struct_5 {
    char padding_0[560];
    char field_230;
} struct_5;

typedef struct struct_3 {
    char padding_0[40];
    struct struct_2 *field_28;
} struct_3;

typedef struct struct_8 {
    char padding_0[152];
    struct struct_9 *field_98;
} struct_8;

typedef struct struct_2 {
    char padding_0[152];
    struct struct_1 *field_98;
} struct_2;

typedef struct struct_9 {
    char padding_0[560];
    char field_230;
} struct_9;

typedef struct struct_1 {
    char padding_0[560];
    char field_230;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab4a5;

struct_4 * WaterZone_StopUnderwaterEffects(struct_4 *ptr)
{
    struct_4 *v0;  // x0
    struct_4 *v1;  // x0
    struct_4 *v3;  // x0
    void* p;  // x22
    unsigned long v5;  // x8
    unsigned long long pos;  // x23
    unsigned long v7;  // x20

    v0 = ptr;
    if (!(g_1fab4a5 & 1))
    {
        v1 = sub_f7d92c(&g_1ef0c58);
        g_1fab4a5 = 1;
        v0 = v1;
    }
    if (!ptr->field_148)
        return v0;
    v3 = ptr->field_58;
    if (v3 && (v3 = (struct_4 *)AudioSource__Pause(v3, 0), p = ptr->field_68, p))
    {
        v5 = (long long)p[24];
        if (v5 && (unsigned int)v5 >= 1)
        {
            pos = 0;
            do
            {
                if ((v5 & 4294967295) <= pos)
                    sub_f7db74(sub_f7db7c());
                v7 = *((long long *)(32 + (char *)p + 8 * pos));
                if (!g_1ef0c58->field_e0)
                    sub_f7da5c(g_1ef0c58);
                v3 = Object__op_Implicit(v7, 0);
                if (((char)v3 & 1))
                {
                    if (v7)
                        AudioSource__Play(v7, 0);
                    else
                        sub_f7db74(v3);
                }
                v5 = (int)p[24];
                pos += 1;
            } while (pos < (v5 & 4294967295));
        }
        v3 = ptr->field_a8;
        if (v3 && (v3 = (struct_4 *)Component__get_gameObject(v3, 0), v3))
        {
            GameObject__SetActive();
            RenderSettings__set_fog(ptr->field_16c, 0);
            RenderSettings__set_fogColor(0);
            RenderSettings__set_fogDensity(0);
            RenderSettings__set_fogMode(ptr->field_170, 0);
            RenderSettings__set_fogStartDistance(0);
            RenderSettings__set_fogEndDistance(0);
            RenderSettings__set_ambientLight(0);
            if (!g_1ef0c58->field_e0)
                sub_f7da5c(g_1ef0c58);
            if (((char)Object__op_Implicit(ptr->field_f0, 0) & 1) && ptr->field_e8)
            {
                v3 = ptr->field_f0;
                if (v3)
                {
                    Light__set_color(v3, 0);
                    goto LABEL_109a7c4;
                }
            }
            else
            {
LABEL_109a7c4:
                if (!g_1ef0c58->field_e0)
                    sub_f7da5c(g_1ef0c58);
                if (((char)Object__op_Implicit(ptr->field_70, 0) & 1))
                {
                    v3 = ptr->field_70;
                    if (v3 && (v3 = (struct_4 *)Component__get_gameObject(v3, 0), v3))
                    {
                        GameObject__SetActive();
                        goto LABEL_109a808;
                    }
                }
                else
                {
LABEL_109a808:
                    if (ptr->field_12c)
                    {
                        if (!g_1ef0c58->field_e0)
                            sub_f7da5c(g_1ef0c58);
                        if (!(Object__op_Implicit(ptr->field_130, 0) & 1))
                            goto LABEL_109a854;
                        v3 = ptr->field_130;
                        if (v3 && (v3 = (struct_4 *)Component__get_gameObject(v3, 0), v3))
                        {
                            GameObject__SetActive();
                            goto LABEL_109a854;
                        }
                    }
                    else
                    {
LABEL_109a854:
                        if (!g_1ef0c58->field_e0)
                            sub_f7da5c(g_1ef0c58);
                        v3 = Object__op_Implicit(ptr->field_80, 0);
                        if (((char)v3 & 1))
                        {
                            v3 = ptr->field_80;
                            if (v3 && (v3 = (struct_4 *)Component__get_gameObject(v3, 0), v3))
                            {
                                v3 = GameObject__SetActive();
                                goto LABEL_109a898;
                            }
                        }
                        else
                        {
LABEL_109a898:
                            if (ptr->field_20 && ptr->field_20->field_28 && ptr->field_20->field_28->field_98)
                            {
                                ptr->field_20->field_28->field_98->field_230 = 0;
                                ptr->field_148 = 0;
                                return v3;
                            }
                        }
                    }
                }
            }
        }
    }
    sub_f7db74(v3);
}
```

## `WaterZone.StartUnderwaterEffects` — RVA `0xc9a8d4`

- Decompiled symbol: `WaterZone_StartUnderwaterEffects`
- Metadata signature: `private void StartUnderwaterEffects() { }`
- Native interval: `1460` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: Decompiler produced no C-like text

```c
// 0x109a8d4: sub sp, sp, #0xa0
// 0x109a8d8: str d10, [sp, #0x50]
// 0x109a8dc: stp d9, d8, [sp, #0x58]
// 0x109a8e0: str x30, [sp, #0x68]
// 0x109a8e4: stp x24, x23, [sp, #0x70]
// 0x109a8e8: stp x22, x21, [sp, #0x80]
// 0x109a8ec: stp x20, x19, [sp, #0x90]
// 0x109a8f0: adrp x20, #0x1fab000
// 0x109a8f4: ldrb w8, [x20, #0x4a4]
// 0x109a8f8: mov x19, x0
// 0x109a8fc: tbnz w8, #0, #0x109a920
// 0x109a900: adrp x0, #0x1e8d000
// 0x109a904: ldr x0, [x0, #0xea8]
// 0x109a908: bl #0xf7d92c
// 0x109a90c: adrp x0, #0x1e8c000
// 0x109a910: ldr x0, [x0, #0xd8]
// 0x109a914: bl #0xf7d92c
// 0x109a918: mov w8, #1
// 0x109a91c: strb w8, [x20, #0x4a4]
// 0x109a920: movi v0.2d, #0000000000000000
// 0x109a924: str xzr, [sp, #0x48]
// 0x109a928: stp q0, q0, [sp, #0x20]
// 0x109a92c: adrp x21, #0x1e8c000
// 0x109a930: ldrb w8, [x19, #0x148]
// 0x109a934: ldr x21, [x21, #0xd8]
// 0x109a938: cbnz w8, #0x109abb0
// 0x109a93c: ldr x0, [x19, #0x58]
// 0x109a940: cbz x0, #0x109ae80
// 0x109a944: mov x1, xzr
// 0x109a948: bl #0x1b6a5cc
// 0x109a94c: ldr x22, [x19, #0x68]
// 0x109a950: cbz x22, #0x109ae80
// 0x109a954: ldr x8, [x22, #0x18]
// 0x109a958: cmp w8, #1
// 0x109a95c: b.lt #0x109a9bc
// 0x109a960: mov x23, xzr
// 0x109a964: and x8, x8, #0xffffffff
// 0x109a968: add x24, x22, #0x20
// 0x109a96c: cmp x23, w8, uxtw
// 0x109a970: b.hs #0x109ae84
// 0x109a974: ldr x0, [x21]
// 0x109a978: ldr x20, [x24, x23, lsl #3]
// 0x109a97c: ldr w8, [x0, #0xe0]
// 0x109a980: cbnz w8, #0x109a988
// 0x109a984: bl #0xf7da5c
// 0x109a988: mov x0, x20
// 0x109a98c: mov x1, xzr
// 0x109a990: mov x2, xzr
// 0x109a994: bl #0x1b94ac8
// 0x109a998: tbz w0, #0, #0x109a9ac
// 0x109a99c: cbz x20, #0x109ae80
// 0x109a9a0: mov x0, x20
// 0x109a9a4: mov x1, xzr
// 0x109a9a8: bl #0x1b6a7a8
// 0x109a9ac: ldr w8, [x22, #0x18]
// 0x109a9b0: add x23, x23, #1
// 0x109a9b4: cmp x23, w8, sxtw
// 0x109a9b8: b.lt #0x109a96c
// 0x109a9bc: ldr x0, [x19, #0xa8]
// 0x109a9c0: cbz x0, #0x109ae80
// 0x109a9c4: mov x1, xzr
// 0x109a9c8: bl #0x1b92190
// 0x109a9cc: cbz x0, #0x109ae80
// 0x109a9d0: mov w1, #1
// 0x109a9d4: mov x2, xzr
// 0x109a9d8: bl #0x1b94cd0
// 0x109a9dc: ldr x8, [x19, #0x30]
// 0x109a9e0: cbz x8, #0x109ae80
// 0x109a9e4: ldr d0, [x19, #0x150]
// 0x109a9e8: str d0, [x8, #0x110]
// 0x109a9ec: ldr s0, [x19, #0x158]
// 0x109a9f0: str s0, [x8, #0x118]
// 0x109a9f4: ldrb w8, [x19, #0x149]
// 0x109a9f8: cbz w8, #0x109aa50
// 0x109a9fc: mov w0, #1
// 0x109aa00: mov x1, xzr
// 0x109aa04: bl #0x1b79cb8
// 0x109aa08: ldr s0, [x19, #0x150]
// 0x109aa0c: ldr s1, [x19, #0x154]
// 0x109aa10: ldr s2, [x19, #0x158]
// 0x109aa14: ldr s3, [x19, #0x15c]
// 0x109aa18: mov x0, xzr
// 0x109aa1c: bl #0x1b79e9c
// 0x109aa20: ldr s0, [x19, #0x160]
// 0x109aa24: mov x0, xzr
// 0x109aa28: bl #0x1b79f44
// 0x109aa2c: ldr w0, [x19, #0x14c]
// 0x109aa30: mov x1, xzr
// 0x109aa34: bl #0x1b79ddc
// 0x109aa38: ldr s0, [x19, #0x164]
// 0x109aa3c: mov x0, xzr
// 0x109aa40: bl #0x1b79d1c
// 0x109aa44: ldr s0, [x19, #0x168]
// 0x109aa48: mov x0, xzr
// 0x109aa4c: bl #0x1b79d7c
// 0x109aa50: ldrb w8, [x19, #0x118]
// 0x109aa54: cbz w8, #0x109aa70
// 0x109aa58: ldr s0, [x19, #0x11c]
// 0x109aa5c: ldr s1, [x19, #0x120]
// 0x109aa60: ldr s2, [x19, #0x124]
// 0x109aa64: ldr s3, [x19, #0x128]
// 0x109aa68: mov x0, xzr
// 0x109aa6c: bl #0x1b7a000
// 0x109aa70: ldr x0, [x21]
// 0x109aa74: ldr x20, [x19, #0xf0]
// 0x109aa78: ldr w8, [x0, #0xe0]
// 0x109aa7c: cbnz w8, #0x109aa84
// 0x109aa80: bl #0xf7da5c
// 0x109aa84: mov x0, x20
// 0x109aa88: mov x1, xzr
// 0x109aa8c: bl #0x1b98274
// 0x109aa90: tbz w0, #0, #0x109aab8
// 0x109aa94: ldrb w8, [x19, #0xe8]
// 0x109aa98: cbz w8, #0x109aab8
// 0x109aa9c: ldr x0, [x19, #0xf0]
// 0x109aaa0: cbz x0, #0x109ae80
// 0x109aaa4: ldr s3, [x19, #0x104]
// 0x109aaa8: ldp s1, s2, [x19, #0xfc]
// 0x109aaac: ldr s0, [x19, #0xf8]
// 0x109aab0: mov x1, xzr
// 0x109aab4: bl #0x1b7bb80
// 0x109aab8: ldr x0, [x21]
// 0x109aabc: ldr x20, [x19, #0x70]
// 0x109aac0: ldr w8, [x0, #0xe0]
// 0x109aac4: cbnz w8, #0x109aacc
// 0x109aac8: bl #0xf7da5c
// 0x109aacc: mov x0, x20
// 0x109aad0: mov x1, xzr
// 0x109aad4: bl #0x1b98274
// 0x109aad8: tbz w0, #0, #0x109aafc
// 0x109aadc: ldr x0, [x19, #0x70]
// 0x109aae0: cbz x0, #0x109ae80
// 0x109aae4: mov x1, xzr
// 0x109aae8: bl #0x1b92190
// 0x109aaec: cbz x0, #0x109ae80
// 0x109aaf0: mov w1, #1
// 0x109aaf4: mov x2, xzr
// 0x109aaf8: bl #0x1b94cd0
// 0x109aafc: ldrb w8, [x19, #0x12c]
// 0x109ab00: cbz w8, #0x109ab48
// 0x109ab04: ldr x0, [x21]
// 0x109ab08: ldr x20, [x19, #0x130]
// 0x109ab0c: ldr w8, [x0, #0xe0]
// 0x109ab10: cbnz w8, #0x109ab18
// 0x109ab14: bl #0xf7da5c
// 0x109ab18: mov x0, x20
// 0x109ab1c: mov x1, xzr
// 0x109ab20: bl #0x1b98274
// 0x109ab24: tbz w0, #0, #0x109ab48
// 0x109ab28: ldr x0, [x19, #0x130]
// 0x109ab2c: cbz x0, #0x109ae80
// 0x109ab30: mov x1, xzr
// 0x109ab34: bl #0x1b92190
// 0x109ab38: cbz x0, #0x109ae80
// 0x109ab3c: mov w1, #1
// 0x109ab40: mov x2, xzr
// 0x109ab44: bl #0x1b94cd0
// 0x109ab48: ldr x0, [x21]
// 0x109ab4c: ldr x20, [x19, #0x80]
// 0x109ab50: ldr w8, [x0, #0xe0]
// 0x109ab54: cbnz w8, #0x109ab5c
// 0x109ab58: bl #0xf7da5c
// 0x109ab5c: mov x0, x20
// 0x109ab60: mov x1, xzr
// 0x109ab64: bl #0x1b98274
// 0x109ab68: tbz w0, #0, #0x109ab8c
// 0x109ab6c: ldr x0, [x19, #0x80]
// 0x109ab70: cbz x0, #0x109ae80
// 0x109ab74: mov x1, xzr
// 0x109ab78: bl #0x1b92190
// 0x109ab7c: cbz x0, #0x109ae80
// 0x109ab80: mov w1, wzr
// 0x109ab84: mov x2, xzr
// 0x109ab88: bl #0x1b94cd0
// 0x109ab8c: ldr x8, [x19, #0x20]
// 0x109ab90: cbz x8, #0x109ae80
// 0x109ab94: ldr x8, [x8, #0x28]
// 0x109ab98: cbz x8, #0x109ae80
// 0x109ab9c: ldr x8, [x8, #0x98]
// 0x109aba0: cbz x8, #0x109ae80
// 0x109aba4: mov w9, #1
// 0x109aba8: strb w9, [x8, #0x230]
// 0x109abac: strb w9, [x19, #0x148]
// 0x109abb0: ldr x0, [x21]
// 0x109abb4: ldr x20, [x19, #0x70]
// 0x109abb8: ldr w8, [x0, #0xe0]
// 0x109abbc: cbnz w8, #0x109abc4
// 0x109abc0: bl #0xf7da5c
// 0x109abc4: mov x0, x20
// 0x109abc8: mov x1, xzr
// 0x109abcc: bl #0x1b98274
// 0x109abd0: tbz w0, #0, #0x109ac30
// 0x109abd4: ldr x8, [x19, #0x20]
// 0x109abd8: cbz x8, #0x109ae80
// 0x109abdc: ldrb w9, [x8, #0x256]
// 0x109abe0: cbz w9, #0x109ac30
// 0x109abe4: ldr x0, [x8, #0x60]
// 0x109abe8: cbz x0, #0x109ae80
// 0x109abec: ldr x20, [x19, #0x70]
// 0x109abf0: mov x1, xzr
// 0x109abf4: bl #0x1b9d508
// 0x109abf8: ldr x8, [x19, #0x20]
// 0x109abfc: cbz x8, #0x109ae80
// 0x109ac00: ldr x0, [x8, #0x60]
// 0x109ac04: cbz x0, #0x109ae80
// 0x109ac08: ldr s9, [x19, #0x78]
// 0x109ac0c: mov x1, xzr
// 0x109ac10: mov v8.16b, v0.16b
// 0x109ac14: bl #0x1b9d508
// 0x109ac18: cbz x20, #0x109ae80
// 0x109ac1c: mov x0, x20
// 0x109ac20: mov v0.16b, v8.16b
// 0x109ac24: mov v1.16b, v9.16b
// 0x109ac28: mov x1, xzr
// 0x109ac2c: bl #0x1b9d5a8
// 0x109ac30: ldr x0, [x19, #0x1a0]
// 0x109ac34: cbz x0, #0x109ae80
// 0x109ac38: adrp x20, #0x1e8d000
// 0x109ac3c: ldr x20, [x20, #0xea8]
// 0x109ac40: ldr x1, [x20]
// 0x109ac44: bl #0x1231bc8
// 0x109ac48: cbz x0, #0x109ae80
// 0x109ac4c: mov x8, sp
// 0x109ac50: mov x1, xzr
// 0x109ac54: bl #0x1bcf9fc
// 0x109ac58: ldr x0, [x19, #0x1a8]
// 0x109ac5c: cbz x0, #0x109ae80
// 0x109ac60: ldr s0, [sp, #4]
// 0x109ac64: ldr s1, [sp, #0x10]
// 0x109ac68: mov x1, xzr
// 0x109ac6c: fadd s9, s0, s1
// 0x109ac70: bl #0x1b9d508
// 0x109ac74: adrp x8, #0x832000
// 0x109ac78: ldr s8, [x8, #0x524]
// 0x109ac7c: fadd s0, s9, s8
// 0x109ac80: fcmp s0, s1
// 0x109ac84: b.le #0x109aca0
// 0x109ac88: ldr x0, [x19, #0x1a8]
// 0x109ac8c: cbz x0, #0x109ae80
// 0x109ac90: mov x1, xzr
// 0x109ac94: bl #0x1b9d508
// 0x109ac98: fmov s0, #3.25000000
// 0x109ac9c: b #0x109acd4
// 0x109aca0: ldr x0, [x19, #0x1a0]
// 0x109aca4: cbz x0, #0x109ae80
// 0x109aca8: ldr x1, [x20]
// 0x109acac: bl #0x1231bc8
// 0x109acb0: cbz x0, #0x109ae80
// 0x109acb4: mov x8, sp
// 0x109acb8: mov x1, xzr
// 0x109acbc: bl #0x1bcf9fc
// 0x109acc0: ldr s0, [sp, #4]
// 0x109acc4: ldr s1, [sp, #0x10]
// 0x109acc8: fadd s0, s0, s1
// 0x109accc: fadd s1, s0, s8
// 0x109acd0: fmov s0, wzr
// 0x109acd4: ldr x20, [x19, #0xa8]
// 0x109acd8: stp s1, s0, [x19, #0xb0]
// 0x109acdc: cbz x20, #0x109ae80
// 0x109ace0: mov x0, x20
// 0x109ace4: mov x1, xzr
// 0x109ace8: bl #0x1bc9cb4
// 0x109acec: str x0, [sp, #0x48]
// 0x109acf0: mov x8, sp
// 0x109acf4: add x0, sp, #0x48
// 0x109acf8: mov x1, xzr
// 0x109acfc: bl #0x1bc9f50
// 0x109ad00: ldp q0, q1, [sp]
// 0x109ad04: add x0, sp, #0x20
// 0x109ad08: mov x1, xzr
// 0x109ad0c: stp q0, q1, [sp, #0x20]
// 0x109ad10: bl #0x1bca508
// 0x109ad14: adrp x21, #0x1fab000
// 0x109ad18: ldrb w8, [x21, #0x242]
// 0x109ad1c: mov v8.16b, v0.16b
// 0x109ad20: cbnz w8, #0x109ad38
// 0x109ad24: adrp x0, #0x1e8c000
// 0x109ad28: ldr x0, [x0, #0xa60]
// 0x109ad2c: bl #0xf7d92c
// 0x109ad30: mov w8, #1
// 0x109ad34: strb w8, [x21, #0x242]
// 0x109ad38: adrp x8, #0x1e8c000
// 0x109ad3c: ldr x8, [x8, #0xa60]
// 0x109ad40: ldr x0, [x8]
// 0x109ad44: ldr w8, [x0, #0xe0]
// 0x109ad48: cbnz w8, #0x109ad50
// 0x109ad4c: bl #0xf7da5c
// 0x109ad50: fcvt d9, s8
// 0x109ad54: mov x0, sp
// 0x109ad58: mov v0.16b, v9.16b
// 0x109ad5c: bl #0x1db0c60
// 0x109ad60: fcmp s8, #0.0
// 0x109ad64: b.ge #0x109ad80
// 0x109ad68: fmov d1, #-0.50000000
// 0x109ad6c: fcmp d0, d1
// 0x109ad70: b.ne #0x109ada8
// 0x109ad74: ldr d0, [sp]
// 0x109ad78: fmov d1, #-1.00000000
// 0x109ad7c: b #0x109ad94
// 0x109ad80: fmov d1, #0.50000000
// 0x109ad84: fcmp d0, d1
// 0x109ad88: b.ne #0x109adb4
// 0x109ad8c: ldr d0, [sp]
// 0x109ad90: fmov d1, #1.00000000
// 0x109ad94: fcvtzs x8, d0
// 0x109ad98: fadd d1, d0, d1
// 0x109ad9c: tst x8, #1
// 0x109ada0: fcsel d0, d0, d1, eq
// 0x109ada4: b #0x109adbc
// 0x109ada8: fadd d0, d9, d1
// 0x109adac: frintp d0, d0
// 0x109adb0: b #0x109adbc
// 0x109adb4: fadd d0, d9, d1
// 0x109adb8: frintm d0, d0
// 0x109adbc: mov x8, #0x7ff0000000000000
// 0x109adc0: fmov d1, x8
// 0x109adc4: fcvtzs w9, d0
// 0x109adc8: fcmp d0, d1
// 0x109adcc: mov w8, #-0x80000000
// 0x109add0: csel w1, w8, w9, eq
// 0x109add4: mov x0, x20
// 0x109add8: mov x2, xzr
// 0x109addc: bl #0x1bc9b7c
// 0x109ade0: ldr x0, [x19, #0xa8]
// 0x109ade4: cbz x0, #0x109ae80
// 0x109ade8: mov x1, xzr
// 0x109adec: bl #0x1b92154
// 0x109adf0: ldr x8, [x19, #0x1a8]
// 0x109adf4: cbz x8, #0x109ae80
// 0x109adf8: mov x20, x0
// 0x109adfc: mov x0, x8
// 0x109ae00: mov x1, xzr
// 0x109ae04: bl #0x1b9d508
// 0x109ae08: ldr x0, [x19, #0x1a8]
// 0x109ae0c: cbz x0, #0x109ae80
// 0x109ae10: ldr s10, [x19, #0xb0]
// 0x109ae14: mov x1, xzr
// 0x109ae18: mov v8.16b, v0.16b
// 0x109ae1c: bl #0x1b9d508
// 0x109ae20: ldr x0, [x19, #0x1a8]
// 0x109ae24: cbz x0, #0x109ae80
// 0x109ae28: mov x1, xzr
// 0x109ae2c: mov v9.16b, v2.16b
// 0x109ae30: bl #0x1b9d9b8
// 0x109ae34: cbz x20, #0x109ae80
// 0x109ae38: ldr s3, [x19, #0xb4]
// 0x109ae3c: mov x0, x20
// 0x109ae40: mov x1, xzr
// 0x109ae44: fmul s2, s2, s3
// 0x109ae48: fmul s1, s1, s3
// 0x109ae4c: fmul s0, s0, s3
// 0x109ae50: fadd s2, s9, s2
// 0x109ae54: fadd s1, s10, s1
// 0x109ae58: fadd s0, s8, s0
// 0x109ae5c: bl #0x1b9d5a8
// 0x109ae60: ldp x20, x19, [sp, #0x90]
// 0x109ae64: ldp x22, x21, [sp, #0x80]
// 0x109ae68: ldp x24, x23, [sp, #0x70]
// 0x109ae6c: ldr x30, [sp, #0x68]
// 0x109ae70: ldp d9, d8, [sp, #0x58]
// 0x109ae74: ldr d10, [sp, #0x50]
// 0x109ae78: add sp, sp, #0xa0
// 0x109ae7c: ret
// 0x109ae80: bl #0xf7db74
// 0x109ae84: bl #0xf7db7c
```

## `WaterZone.NextFrame` — RVA `0xc9ae88`

- Decompiled symbol: `WaterZone_NextFrame`
- Metadata signature: `private void NextFrame() { }`
- Native interval: `208` bytes
- Result: `pseudocode`
- Heuristic layout hint: `WaterZone_Recovered` matched 4 offsets against `WaterZone` metadata (confidence 1.00).

```c
typedef struct WaterZone_Recovered {
    char padding_0[300];
    char useCausticsLight;
    char padding_12d[3];
    struct WaterZone_Recovered *causticsLight;
    unsigned int index;
    char padding_13c[4];
    struct struct_1 *frames;
} WaterZone_Recovered;

typedef struct struct_3 {
    char padding_0[24];
    unsigned int field_18;
} struct_3;

typedef struct struct_1 {
    char padding_0[24];
    unsigned int field_18;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab4a0;

struct_2 * WaterZone_NextFrame(struct_2 *ptr)
{
    struct_2 *v0;  // x0
    struct_2 *v1;  // x0
    struct_2 *v3;  // x0
    struct_2 *v4;  // x0
    unsigned long v5;  // x10
    unsigned long v6;  // x9
    unsigned int v7;  // w9

    v0 = ptr;
    if (!(g_1fab4a0 & 1))
    {
        v1 = sub_f7d92c(&g_1ef0c58);
        g_1fab4a0 = 1;
        v0 = v1;
    }
    if (!ptr->field_12c)
        return v0;
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v3 = Object__op_Implicit(ptr->field_130, 0);
    if (!((char)v3 & 1))
        return v3;
    v4 = ptr->field_130;
    if (v4)
    {
        v4 = Behaviour__get_isActiveAndEnabled(v4, 0);
        if (!((char)v4 & 1))
        {
            return v4;
        }
        else if (ptr->field_140)
        {
            v5 = ptr->field_140->field_18;
            v6 = ptr->field_138 + 1;
            v7 = (unsigned int)v6 - (unsigned int)v5 * (unsigned int)(v6 / v5);
            ptr->field_138 = v7;
            if ((unsigned int)v5 <= v7)
                sub_f7db7c(v4);
            v4 = ptr->field_130;
        }
    }
    v4 = sub_f7db74(v4);
    sub_f7db7c(v4);
}
```

## `WaterZone.OnTriggerStay` — RVA `0xc9af58`

- Decompiled symbol: `WaterZone_OnTriggerStay`
- Metadata signature: `private void OnTriggerStay(Collider col) { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long WaterZone_OnTriggerStay(unsigned long a0, unsigned long a1)
{
    unsigned long long v0;  // x0

    v0 = WaterZone__EnterWater();
    return WaterZone__EnterWater();
}
```

## `WaterZone.EnterWater` — RVA `0xc9af5c`

- Decompiled symbol: `WaterZone_EnterWater`
- Metadata signature: `private void EnterWater(Collider col) { }`
- Native interval: `1588` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: Decompiler produced no C-like text

```c
// 0x109af5c: sub sp, sp, #0xa0
// 0x109af60: stp d11, d10, [sp, #0x40]
// 0x109af64: stp d9, d8, [sp, #0x50]
// 0x109af68: str x30, [sp, #0x60]
// 0x109af6c: stp x24, x23, [sp, #0x70]
// 0x109af70: stp x22, x21, [sp, #0x80]
// 0x109af74: stp x20, x19, [sp, #0x90]
// 0x109af78: adrp x21, #0x1fab000
// 0x109af7c: ldrb w8, [x21, #0x4a2]
// 0x109af80: mov x20, x1
// 0x109af84: mov x19, x0
// 0x109af88: tbnz w8, #0, #0x109afb8
// 0x109af8c: adrp x0, #0x1e8d000
// 0x109af90: ldr x0, [x0, #0xea8]
// 0x109af94: bl #0xf7d92c
// 0x109af98: adrp x0, #0x1e8d000
// 0x109af9c: ldr x0, [x0, #0xe08]
// 0x109afa0: bl #0xf7d92c
// 0x109afa4: adrp x0, #0x1e8d000
// 0x109afa8: ldr x0, [x0, #0xec0]
// 0x109afac: bl #0xf7d92c
// 0x109afb0: mov w8, #1
// 0x109afb4: strb w8, [x21, #0x4a2]
// 0x109afb8: movi v0.2d, #0000000000000000
// 0x109afbc: str xzr, [sp, #0x68]
// 0x109afc0: stp q0, q0, [sp, #0x20]
// 0x109afc4: cbz x20, #0x109b58c
// 0x109afc8: mov x0, x20
// 0x109afcc: mov x1, xzr
// 0x109afd0: bl #0x1b92190
// 0x109afd4: cbz x0, #0x109b58c
// 0x109afd8: adrp x21, #0x1e8d000
// 0x109afdc: ldr x21, [x21, #0xec0]
// 0x109afe0: mov x1, xzr
// 0x109afe4: bl #0x1b92774
// 0x109afe8: ldr x1, [x21]
// 0x109afec: mov x2, xzr
// 0x109aff0: bl #0x17f610c
// 0x109aff4: tbz w0, #0, #0x109b56c
// 0x109aff8: ldr x8, [x19, #0x20]
// 0x109affc: cbz x8, #0x109b58c
// 0x109b000: mov w9, #1
// 0x109b004: mov x0, x20
// 0x109b008: mov x1, xzr
// 0x109b00c: strb w9, [x8, #0x255]
// 0x109b010: bl #0x1b92190
// 0x109b014: cbz x0, #0x109b58c
// 0x109b018: adrp x22, #0x1e8d000
// 0x109b01c: ldr x22, [x22, #0xe08]
// 0x109b020: ldr x1, [x22]
// 0x109b024: bl #0x1249224
// 0x109b028: cbz x0, #0x109b58c
// 0x109b02c: mov x8, sp
// 0x109b030: mov x1, xzr
// 0x109b034: bl #0x1bcf9fc
// 0x109b038: ldr x0, [x19, #0x1a0]
// 0x109b03c: cbz x0, #0x109b58c
// 0x109b040: adrp x21, #0x1e8d000
// 0x109b044: ldr s8, [sp, #4]
// 0x109b048: ldr s9, [sp, #0x10]
// 0x109b04c: ldr x21, [x21, #0xea8]
// 0x109b050: ldr x1, [x21]
// 0x109b054: bl #0x1231bc8
// 0x109b058: cbz x0, #0x109b58c
// 0x109b05c: mov x8, sp
// 0x109b060: mov x1, xzr
// 0x109b064: bl #0x1bcf9fc
// 0x109b068: ldr x23, [x19, #0x20]
// 0x109b06c: cbz x23, #0x109b58c
// 0x109b070: adrp x8, #0x832000
// 0x109b074: ldr s0, [x8, #0x470]
// 0x109b078: ldr s1, [sp, #4]
// 0x109b07c: ldr s2, [sp, #0x10]
// 0x109b080: fadd s3, s8, s9
// 0x109b084: fadd s0, s3, s0
// 0x109b088: fadd s1, s1, s2
// 0x109b08c: fcmp s0, s1
// 0x109b090: b.ls #0x109b09c
// 0x109b094: strb wzr, [x23, #0x258]
// 0x109b098: b #0x109b148
// 0x109b09c: mov w24, #1
// 0x109b0a0: strb w24, [x23, #0x258]
// 0x109b0a4: ldrb w8, [x19, #0x50]
// 0x109b0a8: cbnz w8, #0x109b0bc
// 0x109b0ac: mov x0, xzr
// 0x109b0b0: bl #0x1b9ad30
// 0x109b0b4: str s0, [x23, #0x260]
// 0x109b0b8: strb w24, [x19, #0x50]
// 0x109b0bc: mov x0, x20
// 0x109b0c0: mov x1, xzr
// 0x109b0c4: bl #0x1b92190
// 0x109b0c8: cbz x0, #0x109b58c
// 0x109b0cc: ldr x1, [x22]
// 0x109b0d0: bl #0x1249224
// 0x109b0d4: cbz x0, #0x109b58c
// 0x109b0d8: mov x8, sp
// 0x109b0dc: mov x1, xzr
// 0x109b0e0: bl #0x1bcf9fc
// 0x109b0e4: ldr x0, [x19, #0x1a0]
// 0x109b0e8: cbz x0, #0x109b58c
// 0x109b0ec: ldr x1, [x21]
// 0x109b0f0: ldr s8, [sp, #4]
// 0x109b0f4: ldr s9, [sp, #0x10]
// 0x109b0f8: bl #0x1231bc8
// 0x109b0fc: cbz x0, #0x109b58c
// 0x109b100: mov x8, sp
// 0x109b104: mov x1, xzr
// 0x109b108: bl #0x1bcf9fc
// 0x109b10c: ldr x23, [x19, #0x20]
// 0x109b110: cbz x23, #0x109b58c
// 0x109b114: adrp x8, #0x832000
// 0x109b118: ldr s0, [x8, #0x324]
// 0x109b11c: ldr s1, [sp, #4]
// 0x109b120: ldr s2, [sp, #0x10]
// 0x109b124: fadd s3, s8, s9
// 0x109b128: fadd s0, s3, s0
// 0x109b12c: fadd s1, s1, s2
// 0x109b130: fcmp s0, s1
// 0x109b134: b.ls #0x109b140
// 0x109b138: strb wzr, [x23, #0x257]
// 0x109b13c: b #0x109b148
// 0x109b140: mov w8, #1
// 0x109b144: strb w8, [x23, #0x257]
// 0x109b148: ldr x0, [x19, #0x1a0]
// 0x109b14c: cbz x0, #0x109b58c
// 0x109b150: ldr x1, [x21]
// 0x109b154: ldr s8, [x23, #0x3b4]
// 0x109b158: bl #0x1231bc8
// 0x109b15c: cbz x0, #0x109b58c
// 0x109b160: mov x8, sp
// 0x109b164: mov x1, xzr
// 0x109b168: bl #0x1bcf9fc
// 0x109b16c: ldr x20, [x19, #0x20]
// 0x109b170: cbz x20, #0x109b58c
// 0x109b174: ldr s0, [sp, #4]
// 0x109b178: ldr s1, [sp, #0x10]
// 0x109b17c: fadd s0, s0, s1
// 0x109b180: fcmp s8, s0
// 0x109b184: b.ls #0x109b300
// 0x109b188: ldr s0, [x20, #0xc4]
// 0x109b18c: strb wzr, [x20, #0x256]
// 0x109b190: fcmp s0, #0.0
// 0x109b194: b.ne #0x109b328
// 0x109b198: ldr s0, [x20, #0xc0]
// 0x109b19c: fcmp s0, #0.0
// 0x109b1a0: b.ne #0x109b328
// 0x109b1a4: ldr x0, [x19, #0x40]
// 0x109b1a8: cbz x0, #0x109b58c
// 0x109b1ac: mov x1, xzr
// 0x109b1b0: bl #0x1b94c14
// 0x109b1b4: cbz x0, #0x109b58c
// 0x109b1b8: mov x1, xzr
// 0x109b1bc: bl #0x1b9d508
// 0x109b1c0: ldr x0, [x19, #0x1a0]
// 0x109b1c4: cbz x0, #0x109b58c
// 0x109b1c8: ldr x1, [x21]
// 0x109b1cc: mov v8.16b, v0.16b
// 0x109b1d0: bl #0x1231bc8
// 0x109b1d4: cbz x0, #0x109b58c
// 0x109b1d8: mov x8, sp
// 0x109b1dc: mov x1, xzr
// 0x109b1e0: bl #0x1bcf9fc
// 0x109b1e4: ldr x0, [x19, #0x40]
// 0x109b1e8: cbz x0, #0x109b58c
// 0x109b1ec: ldr s10, [sp, #4]
// 0x109b1f0: ldr s11, [sp, #0x10]
// 0x109b1f4: mov x1, xzr
// 0x109b1f8: bl #0x1b94c14
// 0x109b1fc: cbz x0, #0x109b58c
// 0x109b200: mov x1, xzr
// 0x109b204: bl #0x1b9d508
// 0x109b208: ldr x0, [x19, #0x98]
// 0x109b20c: cbz x0, #0x109b58c
// 0x109b210: mov x1, xzr
// 0x109b214: mov v9.16b, v2.16b
// 0x109b218: bl #0x1b92154
// 0x109b21c: cbz x0, #0x109b58c
// 0x109b220: adrp x8, #0x832000
// 0x109b224: ldr s0, [x8, #0x4e4]
// 0x109b228: fadd s1, s10, s11
// 0x109b22c: mov v2.16b, v9.16b
// 0x109b230: mov x1, xzr
// 0x109b234: fadd s1, s1, s0
// 0x109b238: mov v0.16b, v8.16b
// 0x109b23c: bl #0x1b9d5a8
// 0x109b240: ldp s8, s9, [x19, #0xa0]
// 0x109b244: mov x0, xzr
// 0x109b248: bl #0x1b9ad30
// 0x109b24c: fadd s1, s8, s9
// 0x109b250: fcmp s1, s0
// 0x109b254: b.pl #0x109b56c
// 0x109b258: ldr x20, [x19, #0x98]
// 0x109b25c: cbz x20, #0x109b58c
// 0x109b260: mov x0, x20
// 0x109b264: mov x1, xzr
// 0x109b268: bl #0x1bc9cb4
// 0x109b26c: str x0, [sp, #0x68]
// 0x109b270: mov x8, sp
// 0x109b274: add x0, sp, #0x68
// 0x109b278: mov x1, xzr
// 0x109b27c: bl #0x1bc9f50
// 0x109b280: ldp q0, q1, [sp]
// 0x109b284: add x0, sp, #0x20
// 0x109b288: mov x1, xzr
// 0x109b28c: stp q0, q1, [sp, #0x20]
// 0x109b290: bl #0x1bca508
// 0x109b294: adrp x21, #0x1fab000
// 0x109b298: ldrb w8, [x21, #0x242]
// 0x109b29c: mov v8.16b, v0.16b
// 0x109b2a0: cbnz w8, #0x109b2b8
// 0x109b2a4: adrp x0, #0x1e8c000
// 0x109b2a8: ldr x0, [x0, #0xa60]
// 0x109b2ac: bl #0xf7d92c
// 0x109b2b0: mov w8, #1
// 0x109b2b4: strb w8, [x21, #0x242]
// 0x109b2b8: adrp x8, #0x1e8c000
// 0x109b2bc: ldr x8, [x8, #0xa60]
// 0x109b2c0: ldr x0, [x8]
// 0x109b2c4: ldr w8, [x0, #0xe0]
// 0x109b2c8: cbnz w8, #0x109b2d0
// 0x109b2cc: bl #0xf7da5c
// 0x109b2d0: fcvt d9, s8
// 0x109b2d4: mov x0, sp
// 0x109b2d8: mov v0.16b, v9.16b
// 0x109b2dc: bl #0x1db0c60
// 0x109b2e0: fcmp s8, #0.0
// 0x109b2e4: b.ge #0x109b4b8
// 0x109b2e8: fmov d1, #-0.50000000
// 0x109b2ec: fcmp d0, d1
// 0x109b2f0: b.ne #0x109b528
// 0x109b2f4: ldr d0, [sp]
// 0x109b2f8: fmov d1, #-1.00000000
// 0x109b2fc: b #0x109b4cc
// 0x109b300: ldrb w8, [x20, #0x256]
// 0x109b304: cbnz w8, #0x109b56c
// 0x109b308: mov x0, xzr
// 0x109b30c: bl #0x1b9ad30
// 0x109b310: str s0, [x20, #0x264]
// 0x109b314: ldr x8, [x19, #0x20]
// 0x109b318: cbz x8, #0x109b58c
// 0x109b31c: mov w9, #1
// 0x109b320: strb w9, [x8, #0x256]
// 0x109b324: b #0x109b56c
// 0x109b328: ldr s8, [x19, #0xe4]
// 0x109b32c: mov x0, xzr
// 0x109b330: bl #0x1b9ad30
// 0x109b334: adrp x8, #0x832000
// 0x109b338: ldr s1, [x8, #0x520]
// 0x109b33c: fadd s1, s8, s1
// 0x109b340: fcmp s1, s0
// 0x109b344: b.pl #0x109b56c
// 0x109b348: ldr x0, [x19, #0x40]
// 0x109b34c: cbz x0, #0x109b58c
// 0x109b350: mov x1, xzr
// 0x109b354: bl #0x1b94c14
// 0x109b358: cbz x0, #0x109b58c
// 0x109b35c: mov x1, xzr
// 0x109b360: bl #0x1b9d508
// 0x109b364: ldr x0, [x19, #0x1a0]
// 0x109b368: cbz x0, #0x109b58c
// 0x109b36c: ldr x1, [x21]
// 0x109b370: mov v8.16b, v0.16b
// 0x109b374: bl #0x1231bc8
// 0x109b378: cbz x0, #0x109b58c
// 0x109b37c: mov x8, sp
// 0x109b380: mov x1, xzr
// 0x109b384: bl #0x1bcf9fc
// 0x109b388: ldr x0, [x19, #0x40]
// 0x109b38c: cbz x0, #0x109b58c
// 0x109b390: ldr s9, [sp, #4]
// 0x109b394: ldr s10, [sp, #0x10]
// 0x109b398: mov x1, xzr
// 0x109b39c: bl #0x1b94c14
// 0x109b3a0: cbz x0, #0x109b58c
// 0x109b3a4: mov x1, xzr
// 0x109b3a8: fadd s9, s9, s10
// 0x109b3ac: bl #0x1b9d508
// 0x109b3b0: adrp x8, #0x832000
// 0x109b3b4: ldr s0, [x8, #0x4e4]
// 0x109b3b8: ldr x0, [x19, #0xd0]
// 0x109b3bc: str s2, [x19, #0xe0]
// 0x109b3c0: fadd s0, s9, s0
// 0x109b3c4: stp s8, s0, [x19, #0xd8]
// 0x109b3c8: cbz x0, #0x109b58c
// 0x109b3cc: mov x1, xzr
// 0x109b3d0: bl #0x1b92154
// 0x109b3d4: cbz x0, #0x109b58c
// 0x109b3d8: ldp s1, s2, [x19, #0xdc]
// 0x109b3dc: ldr s0, [x19, #0xd8]
// 0x109b3e0: mov x1, xzr
// 0x109b3e4: bl #0x1b9d5a8
// 0x109b3e8: ldr x20, [x19, #0xd0]
// 0x109b3ec: cbz x20, #0x109b58c
// 0x109b3f0: mov x0, x20
// 0x109b3f4: mov x1, xzr
// 0x109b3f8: bl #0x1bc9cb4
// 0x109b3fc: str x0, [sp, #0x68]
// 0x109b400: mov x8, sp
// 0x109b404: add x0, sp, #0x68
// 0x109b408: mov x1, xzr
// 0x109b40c: bl #0x1bc9f50
// 0x109b410: ldp q0, q1, [sp]
// 0x109b414: add x0, sp, #0x20
// 0x109b418: mov x1, xzr
// 0x109b41c: stp q0, q1, [sp, #0x20]
// 0x109b420: bl #0x1bca508
// 0x109b424: adrp x21, #0x1fab000
// 0x109b428: ldrb w8, [x21, #0x242]
// 0x109b42c: mov v8.16b, v0.16b
// 0x109b430: cbnz w8, #0x109b448
// 0x109b434: adrp x0, #0x1e8c000
// 0x109b438: ldr x0, [x0, #0xa60]
// 0x109b43c: bl #0xf7d92c
// 0x109b440: mov w8, #1
// 0x109b444: strb w8, [x21, #0x242]
// 0x109b448: adrp x8, #0x1e8c000
// 0x109b44c: ldr x8, [x8, #0xa60]
// 0x109b450: ldr x0, [x8]
// 0x109b454: ldr w8, [x0, #0xe0]
// 0x109b458: cbnz w8, #0x109b460
// 0x109b45c: bl #0xf7da5c
// 0x109b460: fcvt d9, s8
// 0x109b464: mov x0, sp
// 0x109b468: mov v0.16b, v9.16b
// 0x109b46c: bl #0x1db0c60
// 0x109b470: fcmp s8, #0.0
// 0x109b474: b.ge #0x109b490
// 0x109b478: fmov d1, #-0.50000000
// 0x109b47c: fcmp d0, d1
// 0x109b480: b.ne #0x109b4e0
// 0x109b484: ldr d0, [sp]
// 0x109b488: fmov d1, #-1.00000000
// 0x109b48c: b #0x109b4a4
// 0x109b490: fmov d1, #0.50000000
// 0x109b494: fcmp d0, d1
// 0x109b498: b.ne #0x109b4ec
// 0x109b49c: ldr d0, [sp]
// 0x109b4a0: fmov d1, #1.00000000
// 0x109b4a4: fcvtzs x8, d0
// 0x109b4a8: fadd d1, d0, d1
// 0x109b4ac: tst x8, #1
// 0x109b4b0: fcsel d0, d0, d1, eq
// 0x109b4b4: b #0x109b4f4
// 0x109b4b8: fmov d1, #0.50000000
// 0x109b4bc: fcmp d0, d1
// 0x109b4c0: b.ne #0x109b534
// 0x109b4c4: ldr d0, [sp]
// 0x109b4c8: fmov d1, #1.00000000
// 0x109b4cc: fcvtzs x8, d0
// 0x109b4d0: fadd d1, d0, d1
// 0x109b4d4: tst x8, #1
// 0x109b4d8: fcsel d0, d0, d1, eq
// 0x109b4dc: b #0x109b53c
// 0x109b4e0: fadd d0, d9, d1
// 0x109b4e4: frintp d0, d0
// 0x109b4e8: b #0x109b4f4
// 0x109b4ec: fadd d0, d9, d1
// 0x109b4f0: frintm d0, d0
// 0x109b4f4: mov x8, #0x7ff0000000000000
// 0x109b4f8: fmov d1, x8
// 0x109b4fc: fcvtzs w9, d0
// 0x109b500: fcmp d0, d1
// 0x109b504: mov w8, #-0x80000000
// 0x109b508: csel w1, w8, w9, eq
// 0x109b50c: mov x0, x20
// 0x109b510: mov x2, xzr
// 0x109b514: bl #0x1bc9b7c
// 0x109b518: mov x0, xzr
// 0x109b51c: bl #0x1b9ad30
// 0x109b520: str s0, [x19, #0xe4]
// 0x109b524: b #0x109b56c
// 0x109b528: fadd d0, d9, d1
// 0x109b52c: frintp d0, d0
// 0x109b530: b #0x109b53c
// 0x109b534: fadd d0, d9, d1
// 0x109b538: frintm d0, d0
// 0x109b53c: mov x8, #0x7ff0000000000000
// 0x109b540: fmov d1, x8
// 0x109b544: fcvtzs w9, d0
// 0x109b548: fcmp d0, d1
// 0x109b54c: mov w8, #-0x80000000
// 0x109b550: csel w1, w8, w9, eq
// 0x109b554: mov x0, x20
// 0x109b558: mov x2, xzr
// 0x109b55c: bl #0x1bc9b7c
// 0x109b560: mov x0, xzr
// 0x109b564: bl #0x1b9ad30
// 0x109b568: str s0, [x19, #0xa0]
// 0x109b56c: ldp x20, x19, [sp, #0x90]
// 0x109b570: ldp x22, x21, [sp, #0x80]
// 0x109b574: ldp x24, x23, [sp, #0x70]
// 0x109b578: ldr x30, [sp, #0x60]
// 0x109b57c: ldp d9, d8, [sp, #0x50]
// 0x109b580: ldp d11, d10, [sp, #0x40]
// 0x109b584: add sp, sp, #0xa0
// 0x109b588: ret
// 0x109b58c: bl #0xf7db74
```

## `WaterZone.OnTriggerEnter` — RVA `0xc9b590`

- Decompiled symbol: `WaterZone_OnTriggerEnter`
- Metadata signature: `private void OnTriggerEnter(Collider col) { }`
- Native interval: `2112` bytes
- Result: `pseudocode`
- Heuristic layout hint: `WaterZone_Recovered` matched 2 offsets against `WaterZone` metadata (confidence 1.00).

```c
typedef struct struct_9 {
    char padding_0[176];
    struct struct_8 *field_b0;
    char padding_b8[118];
    unsigned short field_12e;
} struct_9;

typedef struct struct_3 {
    char padding_0[32];
    struct struct_4 *field_20;
    struct struct_2 *field_28;
    char padding_30[136];
    long long field_b8;
    unsigned int field_c0;
    unsigned int field_c4;
    unsigned int field_c8;
    unsigned int field_cc;
    char padding_d0[208];
    long long field_1a0;
} struct_3;

typedef struct struct_1 {
    char padding_0[176];
    struct struct_0 *field_b0;
    char padding_b8[118];
    unsigned short field_12e;
} struct_1;

typedef struct struct_2 {
    char padding_0[336];
    long long field_150;
} struct_2;

typedef struct struct_20 {
    char padding_0[176];
    struct struct_21 *field_b0;
} struct_20;

typedef struct WaterZone_Recovered {
    char padding_0[312];
    struct struct_7 *index;
    unsigned long long frames;
} WaterZone_Recovered;

typedef struct struct_19 {
    char padding_0[176];
    struct struct_18 *field_b0;
    char padding_b8[118];
    unsigned short field_12e;
} struct_19;

typedef struct struct_10 {
    char padding_0[312];
    struct struct_11 *field_138;
    unsigned long long field_140;
} struct_10;

typedef struct struct_15 {
    char padding_0[176];
    struct struct_14 *field_b0;
    char padding_b8[118];
    unsigned short field_12e;
} struct_15;

typedef struct struct_17 {
    char padding_0[176];
    struct struct_16 *field_b0;
    char padding_b8[118];
    unsigned short field_12e;
} struct_17;

typedef struct struct_12 {
    char padding_0[312];
    struct struct_13 *field_138;
    unsigned long long field_140;
} struct_12;

typedef struct struct_8 {
    unsigned long long field_0;
    unsigned int field_8;
    char padding_c[12];
    char field_18;
} struct_8;

typedef struct struct_4 {
    char padding_0[552];
    char field_228;
    char padding_229[119];
    char field_2a0;
} struct_4;

typedef struct struct_0 {
    char padding_0[8];
    unsigned int field_8;
} struct_0;

typedef struct struct_21 {
    unsigned long long field_0;
} struct_21;

typedef struct struct_7 {
    unsigned long long field_0;
} struct_7;

typedef struct struct_18 {
    char padding_0[8];
    unsigned int field_8;
} struct_18;

typedef struct struct_11 {
    unsigned long long field_0;
} struct_11;

typedef struct struct_14 {
    char padding_0[8];
    unsigned int field_8;
} struct_14;

typedef struct struct_16 {
    char padding_0[8];
    unsigned int field_8;
} struct_16;

typedef struct struct_13 {
    unsigned long long field_0;
} struct_13;

typedef struct struct_5 {
    char padding_0[224];
    unsigned int field_e0;
} struct_5;

extern long long g_1eefef8;
extern long long g_1eeff88;
extern struct_5 *g_1ef0c58;
extern long long g_1efcf70;
extern long long g_1efd040;
extern long long g_1f09310;
extern long long g_1f0a468;
extern long long g_1f0a770;
extern long long g_1f0c1a0;
extern long long g_1f0cf98;
extern long long g_1f0fbf0;
extern struct_9 *g_1fab000;
extern char g_1fab4a1;

int WaterZone_OnTriggerEnter(struct_3 *ptr, long long a1)
{
    struct_9 **ptr7;  // x20
    long long v8;  // x21
    unsigned int v15;  // s0
    unsigned int v16;  // s1
    unsigned long v17;  // 4163
    unsigned int v18;  // s1
    unsigned long v19;  // 4142
    long long v20;  // x0
    unsigned int v21;  // s0
    struct_9 **v22;  // x0
    struct_20 *p;  // x8
    unsigned long v24;  // x9
    unsigned long cur;  // x10
    unsigned long v26;  // x9
    struct_6 *ptr11;  // x0
    unsigned long long v29;  // x1
    struct_9 **v30;  // x0
    unsigned long long v31;  // x2
    long long v32;  // x22
    long long *ptr8;  // x0
    long long v9;  // x22
    struct_19 *addr;  // x8
    struct_1 **v35;  // x20
    unsigned long v36;  // x9
    unsigned long iter;  // x10
    unsigned long v38;  // x9
    struct_10 *ptr12;  // x0
    unsigned long long v41;  // x1
    struct_1 **v42;  // x0
    struct_15 **ptr9;  // x19
    struct_9 **v10;  // x0
    struct_17 *ptr5;  // x8
    unsigned long v45;  // x9
    unsigned long node;  // x10
    unsigned long v47;  // x9
    struct_12 *ptr13;  // x0
    unsigned long long v50;  // x1
    struct_15 **v51;  // x0
    char v11[673];  // x8
    long long v12;  // x0
    struct_1 **ptr10;  // x0
    unsigned int v14;  // s2
    unsigned int v0;  // [bp-0xdc]
    unsigned int v1;  // [bp-0xd0]
    uint128_t choice;  // [bp-0xc0]
    uint128_t flag2;  // [bp-0xb0]
    unsigned long long flag;  // [bp-0x98]
    char *v5;  // [bp-0x60]
    char v6;  // [bp+0x0]

    v5 = &v6;
    ptr7 = &g_1fab000;
    v8 = a1;
    if (!(g_1fab4a1 & 1))
    {
        sub_f7d92c(&g_1efcf70);
        sub_f7d92c(&g_1efd040);
        sub_f7d92c(&g_1eefef8);
        sub_f7d92c(&g_1eeff88);
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c("cY");
        sub_f7d92c("s%");
        sub_f7d92c(&g_1f0a468);
        sub_f7d92c(&g_1f0a770);
        sub_f7d92c(&g_1f0c1a0);
        sub_f7d92c(&g_1f0cf98);
        sub_f7d92c(&g_1f09310);
        sub_f7d92c(&g_1f0fbf0);
        g_1fab4a1 = 1;
    }
    v15 = 0;
    flag = 0;
    choice = 0;
    flag2 = 0;
    if (v8 && !((a1 = 0, !Component__get_gameObject(v8, 0) || (v9 = (long long)(unsigned long long)GameObject__get_tag(), a1 = 0, !Component__get_gameObject(v8, 0)))))
    {
        v10 = GameObject__get_transform();
        a1 = g_1f0cf98;
        ptr7 = v10;
        if (((char)String__op_Equality(v9, g_1f0cf98, 0) & 1))
        {
            v11 = ptr->field_20;
            if (v11)
            {
                if (v11[672] || !v11[552])
                    goto LABEL_109b824;
                goto LABEL_109b6f4;
            }
        }
        else
        {
LABEL_109b6f4:
            a1 = g_1f0f7c0;
            if (!((char)String__op_Equality(v9, g_1f0f7c0, 0) & 1) && (a1 = g_1f0c1a0, !((char)(unsigned long long)String__op_Equality(v9, g_1f0c1a0, 0) & 1) && (a1 = g_1f0fbf0, !((char)(unsigned long long)String__op_Equality(v9, g_1f0fbf0, 0) & 1) && (a1 = g_1f0a770, !((char)(unsigned long long)String__op_Equality(v9, g_1f0a770, 0) & 1) && (a1 = g_1f0a468, !((char)(unsigned long long)String__op_Equality(v9, g_1f0a468, 0) & 1))))))
            {
                a1 = 0;
                if (Component__get_gameObject(v8, 0))
                {
                    v12 = Object__get_name();
                    a1 = g_1f09310;
                    ptr10 = String__op_Equality(v12, g_1f09310, 0);
                    if (!((char)ptr10 & 1))
                        return *((unsigned int *)&ptr10);
                    goto LABEL_109b7b0;
                }
            }
            else
            {
LABEL_109b7b0:
                if (ptr7 && !((a1 = 0, Transform__get_position(ptr7, 0), !ptr->field_1a0 || (a1 = g_1efcf70, !sub_1231bc8(ptr->field_1a0, g_1efcf70)))))
                {
                    ptr10 = Collider__get_bounds();
                    v14 = 3201092813;
                    v15 = v0 + v1 + 3201092813;
                    v17 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v16, v15)) >> 5 & 3 | (unsigned long long)(CmpF(v16, v15) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v16, v15)) >> 5 & 3 | (unsigned long long)(CmpF(v16, v15) & 1)) & ((unsigned long long)(char)(CmpF(v16, v15)) >> 5 & 3 | (unsigned long long)(CmpF(v16, v15) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                    if ((char)v17)
                        return *((unsigned int *)&ptr10);
                    ptr10 = Time__get_time(0);
                    v18 = ptr->field_cc + 1058642330;
                    v19 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v18, v15)) >> 5 & 3 | (unsigned long long)(CmpF(v18, v15) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v18, v15)) >> 5 & 3 | (unsigned long long)(CmpF(v18, v15) & 1)) & ((unsigned long long)(char)(CmpF(v18, v15)) >> 5 & 3 | (unsigned long long)(CmpF(v18, v15) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                    if ((char)v19)
                        return *((unsigned int *)&ptr10);
LABEL_109b824:
                    a1 = g_1f0cf98;
                    if (((char)String__op_Equality(v9, g_1f0cf98, 0) & 1))
                    {
                        a1 = v8;
                        WaterZone__EnterWater(ptr, a1);
                        v15 = v15;
                        if (ptr->field_28)
                        {
                            if (!g_1ef0c58->field_e0)
                                sub_f7da5c(g_1ef0c58);
                            a1 = 0;
                            if (!(Object__op_Implicit(ptr->field_28->field_150, 0) & 1))
                                goto LABEL_109b940;
                            v15 = v15;
                            if (ptr->field_28 && !((a1 = 0, v15 = v15, !Component__get_gameObject(v8, 0) || (a1 = 0, v15 = v15, !(unsigned long long)GameObject__get_transform()))))
                            {
                                a1 = 0;
                                Transform__get_position();
                                PlayAudioAtPos__PlayClipAt(ptr->field_28->field_150, 0);
LABEL_109b940:
                                if (ptr7)
                                {
LABEL_109b944:
                                    a1 = 0;
                                    Transform__get_position(ptr7, 0);
                                    v15 = v15;
                                    if (ptr->field_1a0 && !((a1 = g_1efcf70, v15 = v15, !sub_1231bc8(ptr->field_1a0, g_1efcf70))))
                                    {
                                        Collider__get_bounds();
                                        a1 = 0;
                                        Transform__get_position(ptr7, 0);
                                        v20 = ptr->field_b8;
                                        ptr->field_c8 = v14;
                                        v21 = v0 + v1 + 1008981770;
                                        ptr->field_c0 = v15;
                                        ptr->field_c4 = v21;
                                        v15 = v21;
                                        if (v20 && !((a1 = 0, v15 = v21, !(unsigned long long)GameObject__get_transform(v20, 0) || (v15 = ptr->field_c0, a1 = 0, Transform__set_position(), !ptr->field_b8 || (a1 = 0, !(unsigned long long)GameObject__get_transform(ptr->field_b8, 0))))))
                                        {
                                            a1 = 0;
                                            v22 = Transform__GetEnumerator();
                                            ptr7 = v22;
                                            if (v22)
                                            {
                                                p = *(ptr7);
                                                v24 = *((short *)&p[1].padding_0[118]);
                                                if (v24)
                                                {
                                                    cur = p->field_b0 + 1;
                                                    do
                                                    {
                                                        v26 = v24;
                                                        if (*((long long *)(cur - 8)) == g_1eeff88)
                                                        {
                                                            ptr11 = &p->padding_0[16 * *((int *)cur) + 312];
                                                            v31 = 0;
                                                            v29 = *((long long *)&ptr11->padding_0[8]);
                                                            v30 = ptr7;
                                                            (*((long long *)&ptr11->padding_0[0]))();
                                                        }
                                                    } while ((cur = (unsigned long)(cur + 16), v24 = (unsigned long)(v26 - 1), v26 != 1));
                                                }
                                                v31 = 0;
                                                ptr11 = sub_f80110(ptr7);
                                                v29 = *((long long *)&ptr11->padding_0[8]);
                                                v30 = ptr7;
                                                (*((long long *)&ptr11->padding_0[0]))();
                                            }
                                            goto LABEL_109bcd4;
                                        }
                                    }
                                }
                            }
                        }
                    }
                    else
                    {
                        v15 = v15;
                        if (ptr->field_28)
                        {
                            v8 = ptr->field_28->field_150;
                            if (!g_1ef0c58->field_e0)
                                sub_f7da5c(g_1ef0c58);
                            a1 = 0;
                            if (!(Object__op_Implicit(v8, 0) & 1))
                                goto LABEL_109b940;
                            v15 = v15;
                            if (ptr->field_28 && !((v15 = v15, !ptr7)))
                            {
                                v8 = ptr->field_28->field_150;
                                Transform__get_position(ptr7, 0);
                                PlayAudioAtPos__PlayClipAt(v8, 0);
                                goto LABEL_109b944;
                            }
                        }
                    }
                }
            }
        }
    }
    v22 = sub_f7db74();
LABEL_109bcd4:
    sub_f7db74(v22);
    while (true)
    {
        v32 = sub_f1bd40(v8);
        if ((int)a1 != 1)
            break;
        ptr8 = __cxa_begin_catch(v32);
        v8 = *(ptr8);
        __cxa_end_catch(ptr8);
        a1 = g_1eefef8;
        ptr10 = sub_f7da60(ptr7, g_1eefef8);
        if (ptr10)
        {
            addr = *(ptr10);
            v35 = ptr10;
            v36 = addr->field_12e;
            if (v36)
            {
                iter = &addr->field_b0->field_8;
                do
                {
                    v38 = v36;
                    if (*((long long *)(iter - 8)) == g_1eefef8)
                    {
                        ptr12 = &addr->padding_0[16 * *((int *)iter) + 312];
                        v31 = 0;
                        v41 = *((long long *)&ptr12->padding_0[8]);
                        v42 = v35;
                        (*((long long *)&ptr12->padding_0[0]))();
                    }
                } while ((iter = (unsigned long)(iter + 16), v36 = (unsigned long)(v38 - 1), v38 != 1));
            }
            v31 = 0;
            ptr12 = sub_f80110(v35);
            v41 = *((long long *)&ptr12->padding_0[8]);
            v42 = v35;
            (*((long long *)&ptr12->padding_0[0]))();
        }
        else if (!v8)
        {
            if (false)
                return *((unsigned int *)&ptr10);
            ptr10 = Time__get_time(0);
            ptr->field_cc = v15;
            return *((unsigned int *)&ptr10);
        }
    }
    ptr9 = sub_f7da60(ptr7, g_1eefef8);
    if (!ptr9)
    {
        sub_1026098(v32);
        sub_e29990(sub_f1bd40(0));
    }
    ptr5 = *(ptr9);
    v45 = ptr5->field_12e;
    if (v45)
    {
        node = &ptr5->field_b0->field_8;
        do
        {
            v47 = v45;
            if (*((long long *)(node - 8)) == g_1eefef8)
            {
                ptr13 = &ptr5->padding_0[16 * *((int *)node) + 312];
                v31 = 0;
                v50 = *((long long *)&ptr13->padding_0[8]);
                v51 = ptr9;
                (*((long long *)&ptr13->padding_0[0]))();
            }
        } while ((node = (unsigned long)(node + 16), v45 = (unsigned long)(v47 - 1), v47 != 1));
    }
    v31 = 0;
    ptr13 = sub_f80110(ptr9);
    v50 = *((long long *)&ptr13->padding_0[8]);
    v51 = ptr9;
    (*((long long *)&ptr13->padding_0[0]))();
}
```

## `WaterZone.OnTriggerExit` — RVA `0xc9bdd0`

- Decompiled symbol: `WaterZone_OnTriggerExit`
- Metadata signature: `private void OnTriggerExit(Collider col) { }`
- Native interval: `144` bytes
- Result: `pseudocode`
- Heuristic layout hint: `WaterZone_Recovered` matched 2 offsets against `WaterZone` metadata (confidence 1.00).

```c
typedef struct WaterZone_Recovered {
    char padding_0[32];
    struct struct_0 *FPSWalkerComponent;
    char padding_28[40];
    char swimTimeState;
} WaterZone_Recovered;

typedef struct struct_0 {
    char padding_0[597];
    unsigned int field_255;
    char field_259;
} struct_0;

extern long long g_1f0cf98;
extern char g_1fab4a3;

void WaterZone_OnTriggerExit(struct_1 *ptr, long long a1)
{
    long long v0;  // x0
    struct_0 *p;  // x8

    if (!(g_1fab4a3 & 1))
    {
        sub_f7d92c(&g_1f0cf98);
        g_1fab4a3 = 1;
    }
    if (a1 && Component__get_gameObject(a1, 0))
    {
        v0 = GameObject__get_tag();
        if (!((char)String__op_Equality(v0, g_1f0cf98, 0) & 1))
            return;
        p = ptr->field_20;
        ptr->field_50 = 0;
        if (p)
        {
            *((unsigned int *)&(&p->padding_0)[1]) = 0;
            *((char *)&p->field_255 + 1) = 1;
            return;
        }
    }
    sub_f7db74();
}
```

## `WaterZone.ctor` — RVA `0xc9be60`

- Decompiled symbol: `WaterZone_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `112` bytes
- Result: `pseudocode`
- Heuristic layout hint: `WaterZone_Recovered` matched 14 offsets against `WaterZone` metadata (confidence 1.00).

```c
typedef struct WaterZone_Recovered {
    char padding_0[164];
    unsigned int rippleEmitDelay;
    char padding_a8[80];
    uint128_t underwaterSunightColor;
    uint128_t origSunightColor;
    char padding_118[4];
    uint128_t underwaterLightColor;
    char padding_12c[16];
    unsigned int fps;
    char padding_140[12];
    unsigned int underwaterFogMode;
    uint128_t underwaterFogColor;
    unsigned int underwaterFogDensity;
    char padding_164[4];
    unsigned int underwaterLinearFogEnd;
    char padding_16c[4];
    unsigned int origFogMode;
    uint128_t origFogColor;
    uint128_t origLightColor;
    unsigned long long origFogDensity;
    unsigned int origLinearFogEnd;
} WaterZone_Recovered;

long long WaterZone_ctor(struct_0 *ptr)
{
    struct_0 *p;  // x8
    long long v1;  // x0

    p = (char *)&ptr->field_f8 + 8;
    ptr->field_a4 = 0x3f000000;
    *((uint128_t *)&(&ptr->padding_a8)[1]) = 84405977751777816554375255149006920090;
    *((uint128_t *)&p->padding_0[0]) = 84405977751777816554375255149006920090;
    *((uint128_t *)&p->padding_0[20]) = 84405977751777816554375255149006920090;
    *((unsigned int *)((char *)&ptr->field_11c + 12)) = 30;
    ptr->field_14c = 1041865114;
    (&ptr->field_14c)[2] = 0x41700000;
    *((unsigned int *)&ptr->padding_12c[12]) = 1;
    *((uint128_t *)&ptr->field_13c) = 84405977751777816554375255149006920090;
    *((unsigned int *)&ptr->field_150) = 1;
    *((uint128_t *)&p->padding_0[108]) = 84405977751777816554375255149006920090;
    *((uint128_t *)&p->padding_0[124]) = 84405977751777816554375255149006920090;
    *((unsigned long long *)&p->padding_0[140]) = 4715268810898774426;
    (&ptr->field_170)[3] = 0x41f00000;
    v1 = MonoBehaviour__ctor();
    return MonoBehaviour__ctor();
}
```
