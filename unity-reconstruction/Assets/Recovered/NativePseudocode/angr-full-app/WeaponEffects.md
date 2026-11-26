# Native pseudocode: WeaponEffects

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `WeaponEffects.Start` — RVA `0xc8ed38`

- Decompiled symbol: `WeaponEffects_Start`
- Metadata signature: `public void Start() { }`
- Native interval: `324` bytes
- Result: `pseudocode`
- Heuristic layout hint: `WeaponEffects_Recovered` matched 5 offsets against `WeaponEffects` metadata (confidence 1.00).

```c
typedef struct WeaponEffects_Recovered {
    char padding_0[32];
    struct struct_0 *PlayerWeaponsComponent;
    long long WeaponBehaviorComponent;
    long long FPSWalkerComponent;
    long long weaponObj;
    char padding_40[344];
    unsigned long long activeParticles;
} WeaponEffects_Recovered;

typedef struct struct_2 {
    char padding_0[152];
    unsigned long long field_98;
} struct_2;

typedef struct struct_3 {
    char padding_0[40];
    long long field_28;
} struct_3;

typedef struct struct_0 {
    char padding_0[152];
    long long field_98;
} struct_0;

extern long long g_1eee540;
extern long long g_1efcf38;
extern long long g_1efebc0;
extern long long g_1efed60;
extern char g_1fab448;

void WeaponEffects_Start(struct_1 *ptr3, unsigned long a1, unsigned long a2, unsigned long a3)
{
    unsigned long long v3;  // x30
    unsigned long long v4;  // x20
    struct_1 *ptr;  // x0
    struct_3 *v14;  // x0
    long long v15;  // x0
    struct_1 *ptr4;  // x19
    unsigned long long v5;  // x19
    long long v6;  // x0
    struct_1 *p;  // x20
    struct_1 *v8;  // x20
    struct_2 *v9;  // x0
    struct_1 *addr;  // x20
    struct_1 *v11;  // x20
    unsigned long v12;  // x1
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x10]
    unsigned long long v2;  // [bp-0x8]

    v0 = v3;
    v1 = v4;
    v2 = v5;
    if (!(g_1fab448 & 1))
    {
        sub_f7d92c(&g_1efcf38);
        sub_f7d92c(&g_1efed60);
        sub_f7d92c(&g_1efebc0);
        sub_f7d92c(&g_1eee540);
        g_1fab448 = 1;
    }
    if (Component__get_transform(ptr3, 0))
    {
        v6 = Component__get_gameObject();
        p = ptr3;
        p->field_38 = v6;
        v8 = &p->field_38;
        sub_f7d8d0(v8, v6);
        if (*((long long *)&v8->padding_0[0]))
        {
            v9 = sub_1249488(*((long long *)&v8->padding_0[0]), g_1efed60);
            addr = ptr3;
            addr->field_20 = v9;
            v11 = &addr->field_20;
            sub_f7d8d0(v11, v9);
            if (*((long long *)&v11->padding_0[0]))
            {
                v12 = *((long long *)(*((long long *)&v11->padding_0[0]) + 152));
                ptr = ptr3;
                ptr->field_28 = v12;
                sub_f7d8d0((struct WeaponEffects_Recovered *)&ptr->field_28, v12);
                if (Camera__get_main(0) && Component__get_transform())
                {
                    v14 = sub_1231bc8();
                    if (v14 && v14->field_28)
                    {
                        v15 = sub_1249224(v14->field_28, g_1efebc0);
                        ptr3->field_30 = v15;
                        ptr4 = &ptr3->field_30;
                        sub_f7d8d0(ptr4, v15);
                        *((unsigned long long *)&ptr4->padding_40[296]) = sub_f7d9d4(g_1eee540, 0x100);
                        sub_f7d8d0();
                        return;
                    }
                }
            }
        }
    }
    sub_f7db74();
}
```

## `WeaponEffects.ImpactEffects` — RVA `0xc8ee7c`

- Decompiled symbol: `WeaponEffects_ImpactEffects`
- Metadata signature: `public bool ImpactEffects(Collider hitcol, Vector3 hitPoint, bool NpcAttack, bool meleeAttack, Vector3 rayNormal) { }`
- Native interval: `2716` bytes
- Result: `pseudocode`
- Heuristic layout hint: `WeaponEffects_Recovered` matched 2 offsets against `WeaponEffects` metadata (confidence 1.00).

```c
typedef struct struct_8 {
    struct struct_6 *field_0;
    char padding_8[16];
    unsigned int field_18;
    char padding_1c[4];
    struct struct_8 *field_20;
    struct struct_8 *field_28;
    char padding_30[16];
    struct struct_8 *field_40;
    struct struct_8 *field_48;
    struct struct_8 *field_50;
    struct struct_8 *field_58;
    struct struct_8 *field_60;
    struct struct_8 *field_68;
    struct struct_8 *field_70;
    char padding_78[8];
    struct struct_7 *field_80;
    struct struct_9 *field_88;
    char padding_90[8];
    struct struct_8 *field_98;
    char padding_a0[16];
    struct struct_8 *field_b0;
    char padding_b8[64];
    char field_f8;
    char padding_f9[31];
    struct struct_8 *field_118;
    struct struct_8 *field_120;
    struct struct_8 *field_128;
    struct struct_8 *field_130;
    struct struct_8 *field_138;
    struct struct_8 *field_140;
    struct struct_8 *field_148;
    struct struct_8 *field_150;
    struct struct_8 *field_158;
    struct struct_8 *field_160;
    struct struct_8 *field_168;
    struct struct_8 *field_170;
    struct struct_8 *field_178;
    unsigned int field_180;
} struct_8;

typedef struct struct_42 {
    char padding_0[24];
    unsigned int field_18;
    char padding_1c[4];
    struct struct_41 *field_20;
} struct_42;

typedef struct struct_30 {
    char padding_0[24];
    unsigned int field_18;
    char padding_1c[4];
    struct struct_29 *field_20;
} struct_30;

typedef struct struct_3 {
    struct struct_1 *field_0;
    char padding_8[16];
    unsigned int field_18;
    char padding_1c[4];
    struct struct_3 *field_20;
    struct struct_3 *field_28;
    char padding_30[16];
    struct struct_3 *field_40;
    struct struct_3 *field_48;
    struct struct_3 *field_50;
    struct struct_3 *field_58;
    struct struct_3 *field_60;
    struct struct_3 *field_68;
    struct struct_3 *field_70;
    char padding_78[8];
    struct struct_2 *field_80;
    struct struct_4 *field_88;
    char padding_90[8];
    struct struct_3 *field_98;
    char padding_a0[16];
    struct struct_3 *field_b0;
    char padding_b8[64];
    char field_f8;
    char padding_f9[31];
    struct struct_3 *field_118;
    struct struct_3 *field_120;
    struct struct_3 *field_128;
    struct struct_3 *field_130;
    struct struct_3 *field_138;
    struct struct_3 *field_140;
    struct struct_3 *field_148;
    struct struct_3 *field_150;
    struct struct_3 *field_158;
    struct struct_3 *field_160;
    struct struct_3 *field_168;
    struct struct_3 *field_170;
    struct struct_3 *field_178;
    unsigned int field_180;
} struct_3;

typedef struct struct_37 {
    char padding_0[176];
    struct struct_36 *field_b0;
    char padding_b8[118];
    unsigned short field_12e;
    char padding_130[36];
    unsigned int field_154;
    char padding_158[134];
    char field_1de;
    char padding_1df[74];
    char field_229;
} struct_37;

typedef struct struct_16 {
    char padding_0[312];
    struct struct_17 *field_138;
    unsigned long long field_140;
} struct_16;

typedef struct struct_13 {
    struct struct_11 *field_0;
    char padding_8[16];
    unsigned int field_18;
    char padding_1c[4];
    struct struct_13 *field_20;
    struct struct_13 *field_28;
    char padding_30[16];
    struct struct_13 *field_40;
    struct struct_13 *field_48;
    struct struct_13 *field_50;
    struct struct_13 *field_58;
    struct struct_13 *field_60;
    struct struct_13 *field_68;
    struct struct_13 *field_70;
    char padding_78[8];
    struct struct_12 *field_80;
    struct struct_14 *field_88;
    char padding_90[8];
    struct struct_13 *field_98;
    char padding_a0[16];
    struct struct_13 *field_b0;
    char padding_b8[64];
    char field_f8;
    char padding_f9[31];
    struct struct_13 *field_118;
    struct struct_13 *field_120;
    struct struct_13 *field_128;
    struct struct_13 *field_130;
    struct struct_13 *field_138;
    struct struct_13 *field_140;
    struct struct_13 *field_148;
    struct struct_13 *field_150;
    struct struct_13 *field_158;
    struct struct_13 *field_160;
    struct struct_13 *field_168;
    struct struct_13 *field_170;
    struct struct_13 *field_178;
    unsigned int field_180;
} struct_13;

typedef struct struct_21 {
    char padding_0[176];
    struct struct_20 *field_b0;
    char padding_b8[118];
    unsigned short field_12e;
} struct_21;

typedef struct struct_35 {
    char padding_0[340];
    unsigned int field_154;
    char padding_158[134];
    char field_1de;
    char padding_1df[74];
    char field_229;
} struct_35;

typedef struct struct_34 {
    char padding_0[176];
    struct struct_33 *field_b0;
    char padding_b8[118];
    unsigned short field_12e;
} struct_34;

typedef struct struct_18 {
    char padding_0[312];
    struct struct_19 *field_138;
    unsigned long long field_140;
} struct_18;

typedef struct struct_25 {
    char padding_0[176];
    struct struct_24 *field_b0;
    char padding_b8[118];
    unsigned short field_12e;
} struct_25;

typedef struct struct_32 {
    char padding_0[176];
    struct struct_31 *field_b0;
    char padding_b8[118];
    unsigned short field_12e;
} struct_32;

typedef struct WeaponEffects_Recovered {
    char padding_0[312];
    struct struct_23 *glassImpactSounds;
    unsigned long long fleshImpactSounds;
} WeaponEffects_Recovered;

typedef struct struct_6 {
    char padding_0[176];
    struct struct_5 *field_b0;
    char padding_b8[118];
    unsigned short field_12e;
    char padding_130[36];
    int field_154;
    char padding_158[134];
    char field_1de;
    char padding_1df[74];
    char field_229;
} struct_6;

typedef struct struct_7 {
    char padding_0[24];
    unsigned int field_18;
    char padding_1c[4];
    struct struct_8 *field_20;
} struct_7;

typedef struct struct_9 {
    char padding_0[24];
    unsigned int field_18;
    char padding_1c[4];
    struct struct_8 *field_20;
} struct_9;

typedef struct struct_41 {
    struct struct_39 *field_0;
    char padding_8[16];
    unsigned int field_18;
    char padding_1c[4];
    struct struct_41 *field_20;
    struct struct_41 *field_28;
    char padding_30[16];
    struct struct_41 *field_40;
    struct struct_41 *field_48;
    struct struct_41 *field_50;
    struct struct_41 *field_58;
    struct struct_41 *field_60;
    struct struct_41 *field_68;
    struct struct_41 *field_70;
    char padding_78[8];
    struct struct_40 *field_80;
    struct struct_42 *field_88;
    char padding_90[8];
    struct struct_41 *field_98;
    char padding_a0[16];
    struct struct_41 *field_b0;
    char padding_b8[64];
    char field_f8;
    char padding_f9[31];
    struct struct_41 *field_118;
    struct struct_41 *field_120;
    struct struct_41 *field_128;
    struct struct_41 *field_130;
    struct struct_41 *field_138;
    struct struct_41 *field_140;
    struct struct_41 *field_148;
    struct struct_41 *field_150;
    struct struct_41 *field_158;
    struct struct_41 *field_160;
    struct struct_41 *field_168;
    struct struct_41 *field_170;
    struct struct_41 *field_178;
    unsigned int field_180;
} struct_41;

typedef struct struct_29 {
    struct struct_27 *field_0;
    char padding_8[16];
    unsigned int field_18;
    char padding_1c[4];
    struct struct_29 *field_20;
    struct struct_29 *field_28;
    char padding_30[16];
    struct struct_29 *field_40;
    struct struct_29 *field_48;
    struct struct_29 *field_50;
    struct struct_29 *field_58;
    struct struct_29 *field_60;
    struct struct_29 *field_68;
    struct struct_29 *field_70;
    char padding_78[8];
    struct struct_30 *field_80;
    struct struct_28 *field_88;
    char padding_90[8];
    struct struct_29 *field_98;
    char padding_a0[16];
    struct struct_29 *field_b0;
    char padding_b8[64];
    char field_f8;
    char padding_f9[31];
    struct struct_29 *field_118;
    struct struct_29 *field_120;
    struct struct_29 *field_128;
    struct struct_29 *field_130;
    struct struct_29 *field_138;
    struct struct_29 *field_140;
    struct struct_29 *field_148;
    struct struct_29 *field_150;
    struct struct_29 *field_158;
    struct struct_29 *field_160;
    struct struct_29 *field_168;
    struct struct_29 *field_170;
    struct struct_29 *field_178;
    unsigned int field_180;
} struct_29;

typedef struct struct_1 {
    char padding_0[176];
    struct struct_0 *field_b0;
    char padding_b8[118];
    unsigned short field_12e;
    char padding_130[36];
    unsigned int field_154;
    char padding_158[134];
    char field_1de;
    char padding_1df[74];
    char field_229;
} struct_1;

typedef struct struct_2 {
    char padding_0[24];
    unsigned int field_18;
    char padding_1c[4];
    struct struct_3 *field_20;
} struct_2;

typedef struct struct_4 {
    char padding_0[24];
    unsigned int field_18;
    char padding_1c[4];
    struct struct_3 *field_20;
} struct_4;

typedef struct struct_36 {
    char padding_0[8];
    unsigned int field_8;
} struct_36;

typedef struct struct_17 {
    unsigned long long field_0;
} struct_17;

typedef struct struct_11 {
    char padding_0[176];
    struct struct_10 *field_b0;
    char padding_b8[118];
    unsigned short field_12e;
    char padding_130[36];
    unsigned int field_154;
    char padding_158[134];
    char field_1de;
    char padding_1df[74];
    char field_229;
} struct_11;

typedef struct struct_12 {
    char padding_0[24];
    unsigned int field_18;
    char padding_1c[4];
    struct struct_13 *field_20;
} struct_12;

typedef struct struct_14 {
    char padding_0[24];
    unsigned int field_18;
    char padding_1c[4];
    struct struct_13 *field_20;
} struct_14;

typedef struct struct_20 {
    char padding_0[8];
    unsigned int field_8;
} struct_20;

typedef struct struct_33 {
    char padding_0[8];
    unsigned int field_8;
} struct_33;

typedef struct struct_19 {
    unsigned long long field_0;
} struct_19;

typedef struct struct_24 {
    char padding_0[8];
    unsigned int field_8;
} struct_24;

typedef struct struct_31 {
    char padding_0[8];
    unsigned int field_8;
} struct_31;

typedef struct struct_23 {
    unsigned long long field_0;
} struct_23;

typedef struct struct_5 {
    char padding_0[8];
    unsigned int field_8;
} struct_5;

typedef struct struct_39 {
    char padding_0[176];
    struct struct_38 *field_b0;
    char padding_b8[118];
    unsigned short field_12e;
    char padding_130[36];
    unsigned int field_154;
    char padding_158[134];
    char field_1de;
    char padding_1df[74];
    char field_229;
} struct_39;

typedef struct struct_40 {
    char padding_0[24];
    unsigned int field_18;
    char padding_1c[4];
    struct struct_41 *field_20;
} struct_40;

typedef struct struct_27 {
    char padding_0[176];
    struct struct_26 *field_b0;
    char padding_b8[118];
    unsigned short field_12e;
    char padding_130[36];
    unsigned int field_154;
    char padding_158[134];
    char field_1de;
    char padding_1df[74];
    char field_229;
} struct_27;

typedef struct struct_28 {
    char padding_0[24];
    unsigned int field_18;
    char padding_1c[4];
    struct struct_29 *field_20;
} struct_28;

typedef struct struct_0 {
    char padding_0[8];
    unsigned int field_8;
} struct_0;

typedef struct struct_10 {
    char padding_0[8];
    unsigned int field_8;
} struct_10;

typedef struct struct_38 {
    char padding_0[8];
    unsigned int field_8;
} struct_38;

typedef struct struct_26 {
    char padding_0[8];
    unsigned int field_8;
} struct_26;

typedef struct struct_15 {
    char padding_0[224];
    unsigned int field_e0;
} struct_15;

extern struct_3 *g_1eefef8;
extern unsigned long long g_1eeff88;
extern struct_15 *g_1ef0c58;
extern long long g_1efd040;
extern long long g_1f09af8;
extern long long g_1f0a468;
extern long long g_1f0a770;
extern long long g_1f0c1a0;
extern long long g_1f0dcd0;
extern long long g_1f0fbf0;
extern struct_8 g_1fab000;
extern char g_1fab449;

unsigned int WeaponEffects_ImpactEffects(struct_8 *ptr, struct_8 *a1, unsigned long long a2, unsigned int a3)
{
    struct_8 *ptr18;  // x21
    struct_8 *p;  // x22
    unsigned long v9;  // x0
    struct_8 *addr;  // x23
    unsigned long long v3;  // x2
    unsigned long long v29;  // x2
    struct_3 **ptr19;  // x24
    struct_8 *v31;  // x0
    struct_8 *ptr16;  // x21
    long long v40;  // x0
    struct_13 **ptr20;  // x0
    struct_21 **ptr21;  // x0
    struct_35 *v43;  // x8
    struct_34 *ptr5;  // x8
    struct_21 **v45;  // x22
    unsigned long v46;  // x9
    unsigned long iter;  // x10
    unsigned long v48;  // x9
    unsigned long v49;  // x9
    struct_18 *ptr36;  // x0
    unsigned long long v51;  // x1
    struct_21 **v52;  // x0
    unsigned int v53;  // w8
    struct_25 **ptr22;  // x20
    struct_32 *ptr7;  // x8
    unsigned long v56;  // x9
    unsigned long node;  // x10
    unsigned long v58;  // x9
    unsigned long v59;  // x9
    struct_22 *ptr37;  // x0
    unsigned long long v61;  // x1
    struct_25 **v62;  // x0

    ptr18 = &g_1fab000.field_0;
    p = a3;
    addr = a1;
    if (!(g_1fab449 & 1))
    {
        sub_f7d92c(&g_1efd040);
        sub_f7d92c(&g_1eefef8);
        sub_f7d92c(&g_1eeff88);
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c("cY");
        sub_f7d92c("S&");
        sub_f7d92c(&g_1f0a468);
        sub_f7d92c(&g_1f0a770);
        sub_f7d92c(&g_1f0dcd0);
        sub_f7d92c(&g_1f09af8);
        sub_f7d92c(&g_1f0c1a0);
        sub_f7d92c(&g_1f0fbf0);
        g_1fab449 = 1;
    }
    v3 = a2;
    if (ptr->field_20)
    {
        while (true)
        {
LABEL_108f844:
            sub_f7db74(v31);
            do
            {
                v40 = sub_f1bd40(addr);
                if ((unsigned int)a1 != 1)
                {
                    ptr22 = sub_f7da60(p, *(ptr19));
                    if (!ptr22)
                    {
                        sub_1026098(v40);
                        sub_e29990(sub_f1bd40(0));
                    }
                    ptr7 = *(ptr22);
                    v56 = ptr7->field_12e;
                    if (v56)
                    {
                        node = &ptr7->field_b0->field_8;
                        do
                        {
                            v58 = v56;
                            if (*((long long *)(node - 8)) == *(ptr19))
                            {
                                ptr37 = &ptr7->padding_0[16 * *((int *)node) + 312];
                                goto LABEL_108f8f4;
                            }
                        } while ((v59 = (unsigned long)(v58 - 1), node = (unsigned long)(node + 16), v56 = (unsigned long)(v58 - 1), v58 != 1));
                    }
                    v29 = 0;
                    ptr37 = sub_f80110(ptr22);
LABEL_108f8f4:
                    v61 = *((long long *)&ptr37->padding_0[8]);
                    v62 = ptr22;
                    (*((long long *)&ptr37->padding_0[0]))();
                }
                ptr20 = __cxa_begin_catch();
                addr = *(ptr20);
                __cxa_end_catch(ptr20);
                a1 = *(ptr19);
                ptr21 = sub_f7da60(p, a1);
                if (ptr21)
                {
                    ptr5 = *(ptr21);
                    v45 = ptr21;
                    v46 = ptr5->field_12e;
                    if (v46)
                    {
                        iter = &ptr5->field_b0->field_8;
                        do
                        {
                            v48 = v46;
                            if (*((long long *)(iter - 8)) == *(ptr19))
                            {
                                ptr36 = &ptr5->padding_0[16 * *((int *)iter) + 312];
                                goto LABEL_108f650;
                            }
                        } while ((v49 = (unsigned long)(v48 - 1), iter = (unsigned long)(iter + 16), v46 = (unsigned long)(v48 - 1), v48 != 1));
                    }
                    v29 = 0;
                    ptr36 = sub_f80110(v45);
LABEL_108f650:
                    v51 = *((long long *)&ptr36->padding_0[8]);
                    v52 = v45;
                    (*((long long *)&ptr36->padding_0[0]))();
                }
            } while (addr);
            if (false)
                return 1;
            if (!((char)a2 & 1))
            {
                v43 = ptr18->field_0;
                v3 = v29;
                if (v43)
                {
                    if (v43->field_229)
                        goto LABEL_108f680;
                    if (2 > v43->field_154)
                    {
                        if (v43->field_1de)
                            goto LABEL_108f680;
                        v53 = 1061997773;
                    }
                    else
                    {
                        v53 = 1045220557;
                    }
LABEL_108f688:
                    ptr->field_180 = v53;
                    PlayAudioAtPos__PlayClipAt(ptr->field_178, a1);
                    return 1;
                }
            }
            else
            {
LABEL_108f680:
                v53 = 0x3f800000;
                goto LABEL_108f688;
            }
            v29 = v3;
            v9 = sub_f7db74(sub_f7df10(sub_f7db74()));
            v31 = sub_f7db7c(v9);
        }
    }
    a1 = ptr->field_20->field_98;
    ptr16 = ptr;
    ptr16->field_28 = a1;
    ptr18 = &ptr16->field_28;
    sub_f7d8d0(ptr18, a1);
    v3 = a2;
    if (!addr || !((a1 = NULL, v3 = a2, Component__get_gameObject(addr, 0))))
        goto LABEL_108f844;
    addr = GameObject__get_tag();
    if (2545987019 < (int)PrivateImplementationDetails___ComputeStringHash(addr, 0))
        goto LABEL_0x108f064;
    else
        goto LABEL_0x108efbc;
}
```

## `WeaponEffects.EmitRotatedParticle` — RVA `0xc8f918`

- Decompiled symbol: `WeaponEffects_EmitRotatedParticle`
- Metadata signature: `public void EmitRotatedParticle(ParticleSystem partSysToRotate, Vector3 direction) { }`
- Native interval: `828` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: Decompiler produced no C-like text

```c
// 0x108f918: sub sp, sp, #0xd0
// 0x108f91c: stp d15, d14, [sp, #0x60]
// 0x108f920: stp d13, d12, [sp, #0x70]
// 0x108f924: stp d11, d10, [sp, #0x80]
// 0x108f928: stp d9, d8, [sp, #0x90]
// 0x108f92c: stp x30, x23, [sp, #0xa0]
// 0x108f930: stp x22, x21, [sp, #0xb0]
// 0x108f934: stp x20, x19, [sp, #0xc0]
// 0x108f938: mov v10.16b, v0.16b
// 0x108f93c: movi v0.2d, #0000000000000000
// 0x108f940: stp q0, q0, [sp, #0x30]
// 0x108f944: str xzr, [sp, #0x28]
// 0x108f948: cbz x1, #0x108fc4c
// 0x108f94c: mov x19, x1
// 0x108f950: mov x20, x0
// 0x108f954: mov x0, x1
// 0x108f958: mov x1, xzr
// 0x108f95c: mov v8.16b, v2.16b
// 0x108f960: mov v9.16b, v1.16b
// 0x108f964: bl #0x1bc9cb4
// 0x108f968: str x0, [sp, #0x58]
// 0x108f96c: add x8, sp, #8
// 0x108f970: add x0, sp, #0x58
// 0x108f974: mov x1, xzr
// 0x108f978: bl #0x1bc9f50
// 0x108f97c: ldur q0, [sp, #8]
// 0x108f980: ldur q1, [sp, #0x18]
// 0x108f984: add x0, sp, #0x30
// 0x108f988: mov x1, xzr
// 0x108f98c: stp q0, q1, [sp, #0x30]
// 0x108f990: bl #0x1bca508
// 0x108f994: adrp x21, #0x1fab000
// 0x108f998: ldrb w8, [x21, #0x242]
// 0x108f99c: mov v11.16b, v0.16b
// 0x108f9a0: cbnz w8, #0x108f9b8
// 0x108f9a4: adrp x0, #0x1e8c000
// 0x108f9a8: ldr x0, [x0, #0xa60]
// 0x108f9ac: bl #0xf7d92c
// 0x108f9b0: mov w8, #1
// 0x108f9b4: strb w8, [x21, #0x242]
// 0x108f9b8: adrp x8, #0x1e8c000
// 0x108f9bc: ldr x8, [x8, #0xa60]
// 0x108f9c0: ldr x0, [x8]
// 0x108f9c4: ldr w8, [x0, #0xe0]
// 0x108f9c8: cbnz w8, #0x108f9d0
// 0x108f9cc: bl #0xf7da5c
// 0x108f9d0: fcvt d12, s11
// 0x108f9d4: add x0, sp, #8
// 0x108f9d8: mov v0.16b, v12.16b
// 0x108f9dc: bl #0x1db0c60
// 0x108f9e0: fcmp s11, #0.0
// 0x108f9e4: b.ge #0x108fa00
// 0x108f9e8: fmov d1, #-0.50000000
// 0x108f9ec: fcmp d0, d1
// 0x108f9f0: b.ne #0x108fa28
// 0x108f9f4: ldr d0, [sp, #8]
// 0x108f9f8: fmov d1, #-1.00000000
// 0x108f9fc: b #0x108fa14
// 0x108fa00: fmov d1, #0.50000000
// 0x108fa04: fcmp d0, d1
// 0x108fa08: b.ne #0x108fa34
// 0x108fa0c: ldr d0, [sp, #8]
// 0x108fa10: fmov d1, #1.00000000
// 0x108fa14: fcvtzs x8, d0
// 0x108fa18: fadd d1, d0, d1
// 0x108fa1c: tst x8, #1
// 0x108fa20: fcsel d0, d0, d1, eq
// 0x108fa24: b #0x108fa3c
// 0x108fa28: fadd d0, d12, d1
// 0x108fa2c: frintp d0, d0
// 0x108fa30: b #0x108fa3c
// 0x108fa34: fadd d0, d12, d1
// 0x108fa38: frintm d0, d0
// 0x108fa3c: mov x8, #0x7ff0000000000000
// 0x108fa40: fmov d1, x8
// 0x108fa44: fcvtzs w9, d0
// 0x108fa48: fcmp d0, d1
// 0x108fa4c: mov w8, #-0x80000000
// 0x108fa50: csel w1, w8, w9, eq
// 0x108fa54: mov x0, x19
// 0x108fa58: mov x2, xzr
// 0x108fa5c: bl #0x1bc9b7c
// 0x108fa60: ldrb w8, [x20, #0x1a8]
// 0x108fa64: cbz w8, #0x108fc28
// 0x108fa68: ldr x1, [x20, #0x198]
// 0x108fa6c: mov x0, x19
// 0x108fa70: mov x2, xzr
// 0x108fa74: bl #0x1bc99d8
// 0x108fa78: adrp x8, #0x832000
// 0x108fa7c: ldr s15, [x8, #0x3b8]
// 0x108fa80: mov w21, w0
// 0x108fa84: str w0, [x20, #0x1a4]
// 0x108fa88: sub w22, w0, #1
// 0x108fa8c: fmov s13, #0.50000000
// 0x108fa90: mov w23, #0x84
// 0x108fa94: fmov s14, #0.25000000
// 0x108fa98: mov x0, x19
// 0x108fa9c: mov x1, xzr
// 0x108faa0: bl #0x1bc9cb4
// 0x108faa4: str x0, [sp, #0x58]
// 0x108faa8: add x8, sp, #8
// 0x108faac: add x0, sp, #0x58
// 0x108fab0: mov x1, xzr
// 0x108fab4: bl #0x1bc9f50
// 0x108fab8: ldur q0, [sp, #8]
// 0x108fabc: ldur q1, [sp, #0x18]
// 0x108fac0: add x0, sp, #0x30
// 0x108fac4: mov x1, xzr
// 0x108fac8: stp q0, q1, [sp, #0x30]
// 0x108facc: bl #0x1bca508
// 0x108fad0: sub w8, w21, #1
// 0x108fad4: scvtf s2, w8
// 0x108fad8: scvtf s1, w22
// 0x108fadc: fsub s0, s2, s0
// 0x108fae0: fcmp s0, s1
// 0x108fae4: b.pl #0x108fc14
// 0x108fae8: mov x0, xzr
// 0x108faec: bl #0x1b901f4
// 0x108faf0: mov x0, x19
// 0x108faf4: mov x1, xzr
// 0x108faf8: mov v11.16b, v0.16b
// 0x108fafc: bl #0x1bc9580
// 0x108fb00: fcmp s11, s13
// 0x108fb04: str x0, [sp, #0x28]
// 0x108fb08: add x8, sp, #8
// 0x108fb0c: add x0, sp, #0x28
// 0x108fb10: mov x1, xzr
// 0x108fb14: b.le #0x108fb58
// 0x108fb18: bl #0x1bc9d80
// 0x108fb1c: ldur q0, [sp, #8]
// 0x108fb20: ldur q1, [sp, #0x18]
// 0x108fb24: add x0, sp, #0x30
// 0x108fb28: mov x1, xzr
// 0x108fb2c: stp q0, q1, [sp, #0x30]
// 0x108fb30: bl #0x1bca508
// 0x108fb34: mov x0, xzr
// 0x108fb38: mov v11.16b, v0.16b
// 0x108fb3c: bl #0x1b901f4
// 0x108fb40: fmov s1, #1.00000000
// 0x108fb44: fmin s1, s0, s1
// 0x108fb48: fcmp s0, s15
// 0x108fb4c: fcsel s0, s1, s15, pl
// 0x108fb50: fmul s0, s11, s0
// 0x108fb54: b #0x108fbd4
// 0x108fb58: bl #0x1bc9d80
// 0x108fb5c: ldur q0, [sp, #8]
// 0x108fb60: ldur q1, [sp, #0x18]
// 0x108fb64: add x0, sp, #0x30
// 0x108fb68: mov x1, xzr
// 0x108fb6c: stp q0, q1, [sp, #0x30]
// 0x108fb70: bl #0x1bca508
// 0x108fb74: mov x0, x19
// 0x108fb78: mov x1, xzr
// 0x108fb7c: mov v11.16b, v0.16b
// 0x108fb80: bl #0x1bc9580
// 0x108fb84: str x0, [sp, #0x28]
// 0x108fb88: add x8, sp, #8
// 0x108fb8c: add x0, sp, #0x28
// 0x108fb90: mov x1, xzr
// 0x108fb94: bl #0x1bc9d80
// 0x108fb98: ldur q0, [sp, #8]
// 0x108fb9c: ldur q1, [sp, #0x18]
// 0x108fba0: add x0, sp, #0x30
// 0x108fba4: mov x1, xzr
// 0x108fba8: stp q0, q1, [sp, #0x30]
// 0x108fbac: bl #0x1bca508
// 0x108fbb0: mov x0, xzr
// 0x108fbb4: mov v12.16b, v0.16b
// 0x108fbb8: bl #0x1b901f4
// 0x108fbbc: fmov s1, #0.75000000
// 0x108fbc0: fmin s1, s0, s1
// 0x108fbc4: fcmp s0, s14
// 0x108fbc8: fcsel s0, s1, s14, pl
// 0x108fbcc: fmul s0, s12, s0
// 0x108fbd0: fadd s0, s11, s0
// 0x108fbd4: ldr x8, [x20, #0x198]
// 0x108fbd8: str s0, [x20, #0x1ac]
// 0x108fbdc: cbz x8, #0x108fc4c
// 0x108fbe0: ldr w9, [x8, #0x18]
// 0x108fbe4: cmp w22, w9
// 0x108fbe8: b.hs #0x108fc50
// 0x108fbec: smaddl x8, w22, w23, x8
// 0x108fbf0: fmul s2, s8, s0
// 0x108fbf4: fmul s1, s9, s0
// 0x108fbf8: fmul s0, s10, s0
// 0x108fbfc: add x0, x8, #0x20
// 0x108fc00: mov x1, xzr
// 0x108fc04: bl #0x1bc9414
// 0x108fc08: ldr w21, [x20, #0x1a4]
// 0x108fc0c: sub w22, w22, #1
// 0x108fc10: b #0x108fa98
// 0x108fc14: ldr x1, [x20, #0x198]
// 0x108fc18: ldr w2, [x20, #0x1a4]
// 0x108fc1c: mov x0, x19
// 0x108fc20: mov x3, xzr
// 0x108fc24: bl #0x1bc98cc
// 0x108fc28: ldp x20, x19, [sp, #0xc0]
// 0x108fc2c: ldp x22, x21, [sp, #0xb0]
// 0x108fc30: ldp x30, x23, [sp, #0xa0]
// 0x108fc34: ldp d9, d8, [sp, #0x90]
// 0x108fc38: ldp d11, d10, [sp, #0x80]
// 0x108fc3c: ldp d13, d12, [sp, #0x70]
// 0x108fc40: ldp d15, d14, [sp, #0x60]
// 0x108fc44: add sp, sp, #0xd0
// 0x108fc48: ret
// 0x108fc4c: bl #0xf7db74
// 0x108fc50: bl #0xf7db7c
```

## `WeaponEffects.BulletMarks` — RVA `0xc8fc54`

- Decompiled symbol: `WeaponEffects_BulletMarks`
- Metadata signature: `public void BulletMarks(RaycastHit hit, bool meleeAttack) { }`
- Native interval: `2740` bytes
- Result: `pseudocode`
- Heuristic layout hint: `WeaponEffects_Recovered` matched 9 offsets against `WeaponEffects` metadata (confidence 1.00).

```c
typedef struct WeaponEffects_Recovered {
    char padding_0[208];
    struct struct_3 *dirtMarksID;
    struct struct_3 *metalMarksID;
    struct struct_3 *woodMarksID;
    struct struct_3 *glassMarksID;
    struct struct_3 *stoneMarksID;
    struct struct_3 *dirtMarksMeleeID;
    struct struct_3 *metalMarksMeleeID;
    struct struct_3 *woodMarksMeleeID;
    unsigned int markObjID;
} WeaponEffects_Recovered;

typedef struct struct_7 {
    char padding_0[24];
    unsigned int field_18;
} struct_7;

typedef struct struct_2 {
    char padding_0[48];
    struct struct_1 *field_30;
} struct_2;

typedef struct struct_3 {
    char padding_0[24];
    unsigned int field_18;
} struct_3;

typedef struct struct_1 {
    char padding_0[28];
    unsigned int field_1c;
    char padding_20[8];
    struct struct_0 *field_28;
} struct_1;

typedef struct struct_0 {
    char padding_0[24];
    unsigned int field_18;
} struct_0;

typedef struct struct_6 {
    char padding_0[12];
    unsigned int field_c;
    unsigned int field_10;
    unsigned int field_14;
    char padding_18[4];
    unsigned int field_1c;
    unsigned int field_20;
} struct_6;

typedef struct struct_5 {
    char padding_0[184];
    struct struct_6 *field_b8;
} struct_5;

extern struct_2 *g_1ef0c58;
extern struct_5 *g_1ef22e8;
extern long long g_1efcfa8;
extern long long g_1f09af8;
extern long long g_1f0a468;
extern long long g_1f0a770;
extern long long g_1f0c1a0;
extern long long g_1f0c700;
extern long long g_1f0cf30;
extern long long g_1f0dcd0;
extern long long g_1f0fbf0;
extern char g_1fab1e1;
extern char g_1fab2cb;
extern char g_1fab32c;
extern char g_1fab44a;

long long WeaponEffects_BulletMarks(struct_4 *ptr, long long a1, unsigned int a2)
{
    unsigned long v2;  // x20
    long long v3;  // x22
    long long v12;  // x0
    long long v13;  // x0
    long long v14;  // x0
    long long v15;  // x0
    long long v16;  // x0
    long long v17;  // x0
    long long v18;  // x0
    long long v19;  // x0
    long long v20;  // x0
    unsigned int v21;  // w21
    unsigned long long v4;  // x0
    struct_2 *v22;  // x22
    long long v23;  // x0
    long long ptr4[11];  // x0
    long long v25;  // x22
    long long v26;  // x21
    long long v27;  // x23
    unsigned int v28;  // s1
    unsigned int v29;  // s2
    long long v30;  // x0
    unsigned int ptr3[9];  // x8
    struct_7 *v5;  // x22
    unsigned int v32;  // s0
    unsigned int v33;  // s1
    unsigned int v34;  // s2
    unsigned int addr[9];  // x8
    unsigned int v36;  // s2
    unsigned int v37;  // s1
    unsigned int v38;  // s0
    unsigned long v39;  // 4253
    long long v40;  // x0
    long long v41;  // x0
    unsigned long v6;  // x0
    unsigned int p[9];  // x8
    unsigned int v43;  // s2
    unsigned int v44;  // s0
    unsigned int v45;  // s1
    unsigned int v46;  // s0
    unsigned long v47;  // 4249
    long long v48;  // x0
    long long v49;  // x0
    long long v50;  // x1
    long long v7;  // x0
    long long v8;  // x0
    long long v9;  // x0
    long long v10;  // x0
    long long v11;  // x0
    unsigned int v0;  // [bp-0x48]
    unsigned int v1;  // [bp-0x44]

    v2 = a2;
    if (!(g_1fab44a & 1))
    {
        sub_f7d92c("s.");
        sub_f7d92c(&g_1efcfa8);
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c("s%");
        sub_f7d92c(&g_1f0cf30);
        sub_f7d92c("S&");
        sub_f7d92c(&g_1f0a468);
        sub_f7d92c(&g_1f0a770);
        sub_f7d92c(&g_1f0dcd0);
        sub_f7d92c(&g_1f09af8);
        sub_f7d92c(&g_1f0c1a0);
        sub_f7d92c(&g_1f0c700);
        sub_f7d92c(&g_1f0fbf0);
        g_1fab44a = 1;
    }
    if (RaycastHit__get_collider(a1, 0) && Component__get_gameObject())
    {
        v3 = GameObject__get_tag();
        v4 = String__op_Equality(v3, g_1f09af8, 0);
        if (((char)v2 & 1))
        {
            if (((char)v4 & 1))
            {
LABEL_108fd78:
                v5 = ptr->field_f8;
                if (v5)
                    goto LABEL_108fe78;
            }
            else if (((char)String__op_Equality(v3, g_1f0c1a0, 0) & 1))
            {
                v5 = ptr->field_100;
                if (v5)
                    goto LABEL_108fe78;
            }
            else
            {
                if (!((char)String__op_Equality(v3, g_1f0fbf0, 0) & 1))
                {
                    if ((String__op_Equality(v3, g_1f0a770, 0) & 1))
                        goto LABEL_108fe70;
                    goto LABEL_108fd78;
                }
                v5 = ptr->field_108;
                if (v5)
                    goto LABEL_108fe78;
            }
        }
        else
        {
            if (((char)v4 & 1))
            {
LABEL_108fd88:
                v5 = ptr->field_d0;
                if (v5)
                    goto LABEL_108fe78;
            }
            else if (((char)String__op_Equality(v3, g_1f0c1a0, 0) & 1))
            {
                v5 = ptr->field_d8;
                if (v5)
                    goto LABEL_108fe78;
            }
            else if (((char)String__op_Equality(v3, g_1f0fbf0, 0) & 1))
            {
                v5 = ptr->field_e0;
                if (v5)
                    goto LABEL_108fe78;
            }
            else if (((char)String__op_Equality(v3, g_1f0a770, 0) & 1))
            {
LABEL_108fe70:
                v5 = ptr->field_e8;
                if (v5)
                    goto LABEL_108fe78;
            }
            else
            {
                if (!(String__op_Equality(v3, g_1f0dcd0, 0) & 1))
                    goto LABEL_108fd88;
                v5 = ptr->field_f0;
                if (v5)
                {
LABEL_108fe78:
                    v6 = Random__Range(0, v5->field_18, 0);
                    if (v5->field_18 <= (unsigned int)v6)
                        sub_f7db7c(v6);
                    ptr->field_110 = *((int *)&v5[1].padding_0[4 + 4 * (v6 & 4294967295)]);
                    v7 = RaycastHit__get_collider(a1, 0);
                    if (!g_1ef0c58->field_e0)
                        sub_f7da5c(g_1ef0c58);
                    v8 = Object__op_Implicit(v7, 0);
                    if (!((char)v8 & 1))
                        return v8;
                    if (RaycastHit__get_collider(a1, 0) && Component__get_gameObject())
                    {
                        v9 = GameObject__get_layer();
                        if ((int)v9 == 9)
                            return v9;
                        if (RaycastHit__get_collider(a1, 0) && Component__get_gameObject())
                        {
                            v10 = GameObject__get_layer();
                            if ((int)v10 == 13)
                                return v10;
                            if (RaycastHit__get_collider(a1, 0) && Component__get_gameObject())
                            {
                                v11 = GameObject__get_tag();
                                v12 = String__op_Inequality(v11, g_1f0c700, 0);
                                if (!((char)v12 & 1))
                                    return v12;
                                if (RaycastHit__get_collider(a1, 0) && Component__get_gameObject())
                                {
                                    v13 = GameObject__get_tag();
                                    v14 = String__op_Inequality(v13, g_1f0cf30, 0);
                                    if (!((char)v14 & 1))
                                        return v14;
                                    if (RaycastHit__get_collider(a1, 0) && Component__get_gameObject())
                                    {
                                        v15 = GameObject__get_tag();
                                        v16 = String__op_Inequality(v15, g_1f0a468, 0);
                                        if (!((char)v16 & 1))
                                            return v16;
                                        if (RaycastHit__get_collider(a1, 0) && Component__get_gameObject())
                                        {
                                            v17 = GameObject__get_tag();
                                            v18 = String__op_Inequality(v17, g_1f0f7c0, 0);
                                            if (!((char)v18 & 1))
                                                return v18;
                                            if (RaycastHit__get_collider(a1, 0) && Component__get_gameObject())
                                            {
                                                v19 = GameObject__get_tag();
                                                v20 = String__op_Inequality(v19, g_1f0fb38, 0);
                                                if (!((char)v20 & 1))
                                                    return v20;
                                                v21 = ptr->field_110;
                                                v22 = g_1eeea08->field_b8->field_0;
                                                RaycastHit__get_point(a1, 0);
                                                RaycastHit__get_normal(a1, 0);
                                                if (!g_1fab2cb)
                                                {
                                                    sub_f7d92c("-M");
                                                    g_1fab2cb = 1;
                                                }
                                                if (v22 && AzuObjectPool__SpawnPooledObj(v22, v21) && GameObject__get_transform() && Transform__GetChild() && (v23 = Component__get_gameObject(), v23 && (unsigned long long)GameObject__get_transform() && (ptr4 = (long long [11])sub_1231bc8(), ptr4 && (v25 = ptr4[9], v26 = ptr4[10], FadeOutDecals__InitializeDecal(ptr4), v26))))
                                                {
                                                    Transform__set_parent(v26, 0, 0);
                                                    v27 = GameObject__get_transform(v23, 0);
                                                    if (!g_1fab32c)
                                                    {
                                                        sub_f7d92c(&g_1ef22e8);
                                                        g_1fab32c = 1;
                                                    }
                                                    RaycastHit__get_normal(a1, 0);
                                                    v28 = g_1ef22e8->field_b8->field_1c;
                                                    v29 = g_1ef22e8->field_b8->field_20;
                                                    Quaternion__FromToRotation(0);
                                                    if (v27)
                                                    {
                                                        Transform__set_rotation(v27, 0);
                                                        Transform__get_localScale(v26, 0);
                                                        v30 = RaycastHit__get_transform(a1, 0);
                                                        if (v25)
                                                        {
                                                            Transform__set_parent(v25, v30, 0);
                                                            if (!g_1fab1e1)
                                                            {
                                                                sub_f7d92c(&g_1ef22e8);
                                                                g_1fab1e1 = 1;
                                                            }
                                                            ptr3 = g_1ef22e8->field_b8;
                                                            v32 = ptr3[3];
                                                            v33 = ptr3[4];
                                                            v34 = ptr3[5];
                                                            Transform__set_localScale(v25, 0);
                                                            if (RaycastHit__get_transform(a1, 0))
                                                            {
                                                                v0 = v29;
                                                                v1 = v28;
                                                                Transform__get_rotation();
                                                                Transform__set_rotation(v25, 0);
                                                                if (!g_1fab1e1)
                                                                {
                                                                    sub_f7d92c(&g_1ef22e8);
                                                                    g_1fab1e1 = 1;
                                                                }
                                                                if (Transform__get_parent(v25, 0) && Component__get_transform())
                                                                {
                                                                    Transform__get_localScale();
                                                                    if (!g_1fab1e1)
                                                                    {
                                                                        sub_f7d92c(&g_1ef22e8);
                                                                        g_1fab1e1 = 1;
                                                                    }
                                                                    addr = g_1ef22e8->field_b8;
                                                                    v36 = v34 - addr[5];
                                                                    v37 = v36 * v36;
                                                                    v38 = v37 + (v32 - addr[3]) * (v32 - addr[3]) + (v33 - addr[4]) * (v33 - addr[4]);
                                                                    v39 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v38, 786163454)) >> 5 & 3 | (unsigned long long)(CmpF(v38, 786163454) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v38, 786163454)) >> 5 & 3 | (unsigned long long)(CmpF(v38, 786163454) & 1)) & ((unsigned long long)(char)(CmpF(v38, 786163454)) >> 5 & 3 | (unsigned long long)(CmpF(v38, 786163454) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                                                                    if ((char)v39)
                                                                    {
LABEL_10903b4:
                                                                        if (Transform__get_parent(v25, 0) && Component__get_transform() && (Transform__get_localScale(), (unsigned long long)Transform__get_parent(v25, 0) && Component__get_transform()))
                                                                        {
                                                                            Transform__get_localScale();
                                                                            v48 = v25;
                                                                            goto LABEL_1090408;
                                                                        }
                                                                    }
                                                                    else if (Transform__get_parent(v25, 0) && (v40 = Component__get_transform(), (unsigned long long)RaycastHit__get_transform(a1, 0)))
                                                                    {
                                                                        v41 = Transform__get_root();
                                                                        if (!g_1ef0c58->field_e0)
                                                                            sub_f7da5c(g_1ef0c58);
                                                                        if ((Object__op_Equality(Component__get_transform(), v41, 0) & 1))
                                                                            goto LABEL_10903b4;
                                                                        if (Transform__get_parent(v25, 0) && Component__get_transform() && Transform__get_parent() && Component__get_transform())
                                                                        {
                                                                            Transform__get_localScale();
                                                                            if (!g_1fab1e1)
                                                                            {
                                                                                sub_f7d92c(&g_1ef22e8);
                                                                                g_1fab1e1 = 1;
                                                                            }
                                                                            p = g_1ef22e8->field_b8;
                                                                            v43 = v36 - p[5];
                                                                            v44 = (v38 - p[3]) * (v38 - p[3]);
                                                                            v45 = (v37 - p[4]) * (v37 - p[4]);
                                                                            v46 = v43 * v43 + (v38 - p[3]) * (v38 - p[3]) + (v37 - p[4]) * (v37 - p[4]);
                                                                            v47 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(v46, 786163454)) >> 5 & 3 | (unsigned long long)(CmpF(v46, 786163454) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v43 * v43 + v44 + v45, 786163454)) >> 5 & 3 | (unsigned long long)(CmpF(v43 * v43 + v44 + v45, 786163454) & 1)) & ((unsigned long long)(char)(CmpF(v46, 786163454)) >> 5 & 3 | (unsigned long long)(CmpF(v43 * v43 + v44 + v45, 786163454) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                                                                            if ((char)v47)
                                                                            {
LABEL_1090438:
                                                                                Transform__set_localScale(v25, 0);
                                                                                Transform__set_parent(v26, v25, 0);
                                                                                Transform__set_localScale(v26, 0);
                                                                                if (((char)v2 & 1))
                                                                                {
                                                                                    RaycastHit__get_point(a1, 0);
                                                                                    RaycastHit__get_normal(a1, 0);
                                                                                    v49 = 4294967226;
                                                                                    v50 = 70;
                                                                                }
                                                                                else
                                                                                {
                                                                                    Random__Range(0);
                                                                                    Transform__set_localScale(v26, 0);
                                                                                    RaycastHit__get_point(a1, 0);
                                                                                    RaycastHit__get_normal(a1, 0);
                                                                                    v49 = 4294967246;
                                                                                    v50 = 50;
                                                                                }
                                                                                Random__Range(v49, v50, 0);
                                                                            }
                                                                            if (Transform__get_parent(v25, 0) && Component__get_transform() && Transform__get_parent() && Component__get_transform() && (Transform__get_localScale(), (unsigned long long)Transform__get_parent(v25, 0) && Component__get_transform() && (unsigned long long)Transform__get_parent() && Component__get_transform() && (Transform__get_localScale(), (unsigned long long)Transform__get_parent(v25, 0) && (v48 = Component__get_transform(), v48))))
                                                                            {
LABEL_1090408:
                                                                                if (Transform__get_parent(v48, 0) && Component__get_transform())
                                                                                {
                                                                                    Transform__get_localScale();
                                                                                    goto LABEL_1090438;
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
    v6 = sub_f7db74();
    sub_f7db7c(v6);
}
```

## `WeaponEffects.BulletTracers` — RVA `0xc90708`

- Decompiled symbol: `WeaponEffects_BulletTracers`
- Metadata signature: `public void BulletTracers(Vector3 direction, Vector3 position, float tracerDist = 0.0, float tracerDistSwim = 0.0, bool isPlayer = true) { }`
- Native interval: `1224` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: Decompiler produced no C-like text

```c
// 0x1090708: sub sp, sp, #0xc0
// 0x109070c: stp d15, d14, [sp, #0x60]
// 0x1090710: stp d13, d12, [sp, #0x70]
// 0x1090714: stp d11, d10, [sp, #0x80]
// 0x1090718: stp d9, d8, [sp, #0x90]
// 0x109071c: stp x30, x21, [sp, #0xa0]
// 0x1090720: stp x20, x19, [sp, #0xb0]
// 0x1090724: adrp x21, #0x1fab000
// 0x1090728: ldrb w8, [x21, #0x44b]
// 0x109072c: mov w20, w1
// 0x1090730: mov v14.16b, v7.16b
// 0x1090734: mov v15.16b, v6.16b
// 0x1090738: mov v11.16b, v5.16b
// 0x109073c: mov v13.16b, v4.16b
// 0x1090740: mov v12.16b, v3.16b
// 0x1090744: mov v8.16b, v2.16b
// 0x1090748: mov v9.16b, v1.16b
// 0x109074c: mov v10.16b, v0.16b
// 0x1090750: mov x19, x0
// 0x1090754: tbnz w8, #0, #0x109076c
// 0x1090758: adrp x0, #0x1e8c000
// 0x109075c: ldr x0, [x0, #0xd8]
// 0x1090760: bl #0xf7d92c
// 0x1090764: mov w8, #1
// 0x1090768: strb w8, [x21, #0x44b]
// 0x109076c: movi v0.2d, #0000000000000000
// 0x1090770: stp q0, q0, [sp, #0x30]
// 0x1090774: str xzr, [sp, #0x28]
// 0x1090778: tbz w20, #0, #0x1090794
// 0x109077c: ldr x8, [x19, #0x28]
// 0x1090780: cbz x8, #0x1090bc8
// 0x1090784: ldr x8, [x8, #0xa8]
// 0x1090788: cbz x8, #0x1090bc8
// 0x109078c: ldrb w8, [x8, #0xaa]
// 0x1090790: cbz w8, #0x1090a34
// 0x1090794: ldr x1, [x19, #0xb8]
// 0x1090798: add x0, x19, #0x190
// 0x109079c: str x1, [x19, #0x190]
// 0x10907a0: bl #0xf7d8d0
// 0x10907a4: ldr x8, [x19, #0x30]
// 0x10907a8: cbz x8, #0x1090bc8
// 0x10907ac: ldrb w9, [x8, #0x256]
// 0x10907b0: adrp x8, #0x1e8c000
// 0x10907b4: ldr x8, [x8, #0xd8]
// 0x10907b8: cbz w9, #0x1090930
// 0x10907bc: ldr x0, [x8]
// 0x10907c0: ldr x20, [x19, #0xc8]
// 0x10907c4: ldr w8, [x0, #0xe0]
// 0x10907c8: cbnz w8, #0x10907d0
// 0x10907cc: bl #0xf7da5c
// 0x10907d0: mov x0, x20
// 0x10907d4: mov x1, xzr
// 0x10907d8: bl #0x1b98274
// 0x10907dc: tbz w0, #0, #0x1090ba8
// 0x10907e0: ldr x0, [x19, #0xc8]
// 0x10907e4: cbz x0, #0x1090bc8
// 0x10907e8: mov x1, xzr
// 0x10907ec: bl #0x1b92154
// 0x10907f0: cbz x0, #0x1090bc8
// 0x10907f4: fmul s0, s8, s14
// 0x10907f8: fmul s1, s9, s14
// 0x10907fc: fmul s3, s10, s14
// 0x1090800: fsub s2, s11, s0
// 0x1090804: fsub s1, s13, s1
// 0x1090808: fsub s0, s12, s3
// 0x109080c: mov x1, xzr
// 0x1090810: bl #0x1b9d5a8
// 0x1090814: ldr x0, [x19, #0xc8]
// 0x1090818: cbz x0, #0x1090bc8
// 0x109081c: mov x1, xzr
// 0x1090820: bl #0x1b92154
// 0x1090824: adrp x21, #0x1fab000
// 0x1090828: ldrb w8, [x21, #0x3e3]
// 0x109082c: mov x20, x0
// 0x1090830: cbnz w8, #0x1090848
// 0x1090834: adrp x0, #0x1e8c000
// 0x1090838: ldr x0, [x0, #0x1e8]
// 0x109083c: bl #0xf7d92c
// 0x1090840: mov w8, #1
// 0x1090844: strb w8, [x21, #0x3e3]
// 0x1090848: adrp x8, #0x1e8c000
// 0x109084c: ldr x8, [x8, #0x1e8]
// 0x1090850: mov v3.16b, v10.16b
// 0x1090854: mov v4.16b, v9.16b
// 0x1090858: mov v5.16b, v8.16b
// 0x109085c: ldr x8, [x8]
// 0x1090860: mov x0, xzr
// 0x1090864: ldr x8, [x8, #0xb8]
// 0x1090868: ldp s0, s1, [x8, #0x48]
// 0x109086c: ldr s2, [x8, #0x50]
// 0x1090870: bl #0x1b8ae38
// 0x1090874: cbz x20, #0x1090bc8
// 0x1090878: mov x0, x20
// 0x109087c: mov x1, xzr
// 0x1090880: bl #0x1b9d774
// 0x1090884: ldr x19, [x19, #0xc8]
// 0x1090888: cbz x19, #0x1090bc8
// 0x109088c: mov x0, x19
// 0x1090890: mov x1, xzr
// 0x1090894: bl #0x1bc9cb4
// 0x1090898: str x0, [sp, #0x58]
// 0x109089c: add x8, sp, #8
// 0x10908a0: add x0, sp, #0x58
// 0x10908a4: mov x1, xzr
// 0x10908a8: bl #0x1bc9f50
// 0x10908ac: ldur q0, [sp, #8]
// 0x10908b0: ldur q1, [sp, #0x18]
// 0x10908b4: add x0, sp, #0x30
// 0x10908b8: mov x1, xzr
// 0x10908bc: stp q0, q1, [sp, #0x30]
// 0x10908c0: bl #0x1bca508
// 0x10908c4: adrp x20, #0x1fab000
// 0x10908c8: ldrb w8, [x20, #0x242]
// 0x10908cc: mov v8.16b, v0.16b
// 0x10908d0: cbnz w8, #0x10908e8
// 0x10908d4: adrp x0, #0x1e8c000
// 0x10908d8: ldr x0, [x0, #0xa60]
// 0x10908dc: bl #0xf7d92c
// 0x10908e0: mov w8, #1
// 0x10908e4: strb w8, [x20, #0x242]
// 0x10908e8: adrp x8, #0x1e8c000
// 0x10908ec: ldr x8, [x8, #0xa60]
// 0x10908f0: ldr x0, [x8]
// 0x10908f4: ldr w8, [x0, #0xe0]
// 0x10908f8: cbnz w8, #0x1090900
// 0x10908fc: bl #0xf7da5c
// 0x1090900: fcvt d9, s8
// 0x1090904: add x0, sp, #8
// 0x1090908: mov v0.16b, v9.16b
// 0x109090c: bl #0x1db0c60
// 0x1090910: fcmp s8, #0.0
// 0x1090914: b.ge #0x1090a3c
// 0x1090918: fmov d1, #-0.50000000
// 0x109091c: fcmp d0, d1
// 0x1090920: b.ne #0x1090a8c
// 0x1090924: ldr d0, [sp, #8]
// 0x1090928: fmov d1, #-1.00000000
// 0x109092c: b #0x1090a50
// 0x1090930: ldr x0, [x8]
// 0x1090934: ldr x20, [x19, #0x190]
// 0x1090938: ldr w8, [x0, #0xe0]
// 0x109093c: cbnz w8, #0x1090944
// 0x1090940: bl #0xf7da5c
// 0x1090944: mov x0, x20
// 0x1090948: mov x1, xzr
// 0x109094c: bl #0x1b98274
// 0x1090950: tbz w0, #0, #0x1090ba8
// 0x1090954: ldr x0, [x19, #0x190]
// 0x1090958: cbz x0, #0x1090bc8
// 0x109095c: mov x1, xzr
// 0x1090960: bl #0x1b92154
// 0x1090964: cbz x0, #0x1090bc8
// 0x1090968: fmul s0, s8, s15
// 0x109096c: fmul s1, s9, s15
// 0x1090970: fmul s3, s10, s15
// 0x1090974: fadd s2, s11, s0
// 0x1090978: fadd s1, s13, s1
// 0x109097c: fadd s0, s12, s3
// 0x1090980: mov x1, xzr
// 0x1090984: bl #0x1b9d5a8
// 0x1090988: ldr x20, [x19, #0x190]
// 0x109098c: cbz x20, #0x1090bc8
// 0x1090990: mov x0, x20
// 0x1090994: mov x1, xzr
// 0x1090998: bl #0x1bc9cb4
// 0x109099c: str x0, [sp, #0x58]
// 0x10909a0: add x8, sp, #8
// 0x10909a4: add x0, sp, #0x58
// 0x10909a8: mov x1, xzr
// 0x10909ac: bl #0x1bc9f50
// 0x10909b0: ldur q0, [sp, #8]
// 0x10909b4: ldur q1, [sp, #0x18]
// 0x10909b8: add x0, sp, #0x30
// 0x10909bc: mov x1, xzr
// 0x10909c0: stp q0, q1, [sp, #0x30]
// 0x10909c4: bl #0x1bca508
// 0x10909c8: adrp x21, #0x1fab000
// 0x10909cc: ldrb w8, [x21, #0x242]
// 0x10909d0: mov v11.16b, v0.16b
// 0x10909d4: cbnz w8, #0x10909ec
// 0x10909d8: adrp x0, #0x1e8c000
// 0x10909dc: ldr x0, [x0, #0xa60]
// 0x10909e0: bl #0xf7d92c
// 0x10909e4: mov w8, #1
// 0x10909e8: strb w8, [x21, #0x242]
// 0x10909ec: adrp x8, #0x1e8c000
// 0x10909f0: ldr x8, [x8, #0xa60]
// 0x10909f4: ldr x0, [x8]
// 0x10909f8: ldr w8, [x0, #0xe0]
// 0x10909fc: cbnz w8, #0x1090a04
// 0x1090a00: bl #0xf7da5c
// 0x1090a04: fcvt d12, s11
// 0x1090a08: add x0, sp, #8
// 0x1090a0c: mov v0.16b, v12.16b
// 0x1090a10: bl #0x1db0c60
// 0x1090a14: fcmp s11, #0.0
// 0x1090a18: b.ge #0x1090a64
// 0x1090a1c: fmov d1, #-0.50000000
// 0x1090a20: fcmp d0, d1
// 0x1090a24: b.ne #0x1090ac8
// 0x1090a28: ldr d0, [sp, #8]
// 0x1090a2c: fmov d1, #-1.00000000
// 0x1090a30: b #0x1090a78
// 0x1090a34: ldr x1, [x19, #0xc0]
// 0x1090a38: b #0x1090798
// 0x1090a3c: fmov d1, #0.50000000
// 0x1090a40: fcmp d0, d1
// 0x1090a44: b.ne #0x1090a98
// 0x1090a48: ldr d0, [sp, #8]
// 0x1090a4c: fmov d1, #1.00000000
// 0x1090a50: fcvtzs x8, d0
// 0x1090a54: fadd d1, d0, d1
// 0x1090a58: tst x8, #1
// 0x1090a5c: fcsel d0, d0, d1, eq
// 0x1090a60: b #0x1090aa0
// 0x1090a64: fmov d1, #0.50000000
// 0x1090a68: fcmp d0, d1
// 0x1090a6c: b.ne #0x1090ad4
// 0x1090a70: ldr d0, [sp, #8]
// 0x1090a74: fmov d1, #1.00000000
// 0x1090a78: fcvtzs x8, d0
// 0x1090a7c: fadd d1, d0, d1
// 0x1090a80: tst x8, #1
// 0x1090a84: fcsel d0, d0, d1, eq
// 0x1090a88: b #0x1090adc
// 0x1090a8c: fadd d0, d9, d1
// 0x1090a90: frintp d0, d0
// 0x1090a94: b #0x1090aa0
// 0x1090a98: fadd d0, d9, d1
// 0x1090a9c: frintm d0, d0
// 0x1090aa0: mov x8, #0x7ff0000000000000
// 0x1090aa4: fmov d1, x8
// 0x1090aa8: fcvtzs w9, d0
// 0x1090aac: fcmp d0, d1
// 0x1090ab0: mov w8, #-0x80000000
// 0x1090ab4: csel w1, w8, w9, eq
// 0x1090ab8: mov x0, x19
// 0x1090abc: mov x2, xzr
// 0x1090ac0: bl #0x1bc9b7c
// 0x1090ac4: b #0x1090ba8
// 0x1090ac8: fadd d0, d12, d1
// 0x1090acc: frintp d0, d0
// 0x1090ad0: b #0x1090adc
// 0x1090ad4: fadd d0, d12, d1
// 0x1090ad8: frintm d0, d0
// 0x1090adc: mov x8, #0x7ff0000000000000
// 0x1090ae0: fmov d1, x8
// 0x1090ae4: fcvtzs w9, d0
// 0x1090ae8: fcmp d0, d1
// 0x1090aec: mov w8, #-0x80000000
// 0x1090af0: csel w1, w8, w9, eq
// 0x1090af4: mov x0, x20
// 0x1090af8: mov x2, xzr
// 0x1090afc: bl #0x1bc9b7c
// 0x1090b00: ldr x0, [x19, #0x190]
// 0x1090b04: cbz x0, #0x1090bc8
// 0x1090b08: ldr x1, [x19, #0x198]
// 0x1090b0c: mov x2, xzr
// 0x1090b10: bl #0x1bc99d8
// 0x1090b14: ldr x21, [x19, #0x198]
// 0x1090b18: str w0, [x19, #0x1a4]
// 0x1090b1c: cbz x21, #0x1090bc8
// 0x1090b20: mov w20, w0
// 0x1090b24: ldr x0, [x19, #0x190]
// 0x1090b28: cbz x0, #0x1090bc8
// 0x1090b2c: mov x1, xzr
// 0x1090b30: bl #0x1bc9580
// 0x1090b34: str x0, [sp, #0x28]
// 0x1090b38: add x8, sp, #8
// 0x1090b3c: add x0, sp, #0x28
// 0x1090b40: mov x1, xzr
// 0x1090b44: bl #0x1bc9d80
// 0x1090b48: ldur q0, [sp, #8]
// 0x1090b4c: ldur q1, [sp, #0x18]
// 0x1090b50: add x0, sp, #0x30
// 0x1090b54: mov x1, xzr
// 0x1090b58: stp q0, q1, [sp, #0x30]
// 0x1090b5c: bl #0x1bca508
// 0x1090b60: ldr w9, [x21, #0x18]
// 0x1090b64: sub w8, w20, #1
// 0x1090b68: cmp w8, w9
// 0x1090b6c: b.hs #0x1090bcc
// 0x1090b70: mov w9, #0x84
// 0x1090b74: smaddl x8, w8, w9, x21
// 0x1090b78: fmul s2, s8, s0
// 0x1090b7c: fmul s1, s9, s0
// 0x1090b80: fmul s0, s10, s0
// 0x1090b84: add x0, x8, #0x20
// 0x1090b88: mov x1, xzr
// 0x1090b8c: bl #0x1bc9414
// 0x1090b90: ldr x0, [x19, #0x190]
// 0x1090b94: cbz x0, #0x1090bc8
// 0x1090b98: ldr w2, [x19, #0x1a4]
// 0x1090b9c: ldr x1, [x19, #0x198]
// 0x1090ba0: mov x3, xzr
// 0x1090ba4: bl #0x1bc98cc
// 0x1090ba8: ldp x20, x19, [sp, #0xb0]
// 0x1090bac: ldp x30, x21, [sp, #0xa0]
// 0x1090bb0: ldp d9, d8, [sp, #0x90]
// 0x1090bb4: ldp d11, d10, [sp, #0x80]
// 0x1090bb8: ldp d13, d12, [sp, #0x70]
// 0x1090bbc: ldp d15, d14, [sp, #0x60]
// 0x1090bc0: add sp, sp, #0xc0
// 0x1090bc4: ret
// 0x1090bc8: bl #0xf7db74
// 0x1090bcc: bl #0xf7db7c
```

## `WeaponEffects.ExplosionEffect` — RVA `0xc90bd0`

- Decompiled symbol: `WeaponEffects_ExplosionEffect`
- Metadata signature: `public void ExplosionEffect(Vector3 position) { }`
- Native interval: `1312` bytes
- Result: `pseudocode`
- Heuristic layout hint: `WeaponEffects_Recovered` matched 2 offsets against `WeaponEffects` metadata (confidence 1.00).

```c
typedef struct WeaponEffects_Recovered {
    char padding_0[120];
    struct struct_3 *explosion;
    struct struct_5 *explosionObj;
} WeaponEffects_Recovered;

typedef struct struct_25 {
    char padding_0[176];
    struct struct_24 *field_b0;
    char padding_b8[118];
    unsigned short field_12e;
} struct_25;

typedef struct struct_5 {
    char padding_0[176];
    struct struct_4 *field_b0;
    char padding_b8[118];
    unsigned short field_12e;
} struct_5;

typedef struct struct_12 {
    char padding_0[312];
    struct struct_13 *field_138;
    unsigned long long field_140;
} struct_12;

typedef struct struct_11 {
    char padding_0[120];
    struct struct_8 *field_78;
    struct struct_10 *field_80;
} struct_11;

typedef struct struct_17 {
    char padding_0[176];
    struct struct_16 *field_b0;
    char padding_b8[118];
    unsigned short field_12e;
} struct_17;

typedef struct struct_23 {
    char padding_0[176];
    struct struct_22 *field_b0;
    char padding_b8[118];
    unsigned short field_12e;
} struct_23;

typedef struct struct_14 {
    char padding_0[312];
    struct struct_15 *field_138;
    unsigned long long field_140;
} struct_14;

typedef struct struct_21 {
    char padding_0[176];
    struct struct_20 *field_b0;
    char padding_b8[118];
    unsigned short field_12e;
} struct_21;

typedef struct struct_27 {
    char padding_0[176];
    struct struct_26 *field_b0;
    char padding_b8[118];
    unsigned short field_12e;
} struct_27;

typedef struct struct_18 {
    char padding_0[312];
    struct struct_19 *field_138;
    unsigned long long field_140;
} struct_18;

typedef struct struct_3 {
    char padding_0[176];
    struct struct_2 *field_b0;
    char padding_b8[118];
    unsigned short field_12e;
} struct_3;

typedef struct struct_24 {
    char padding_0[8];
    unsigned int field_8;
} struct_24;

typedef struct struct_4 {
    char padding_0[8];
    unsigned int field_8;
} struct_4;

typedef struct struct_13 {
    unsigned long long field_0;
} struct_13;

typedef struct struct_8 {
    char padding_0[176];
    struct struct_7 *field_b0;
    char padding_b8[118];
    unsigned short field_12e;
} struct_8;

typedef struct struct_10 {
    char padding_0[176];
    struct struct_9 *field_b0;
    char padding_b8[118];
    unsigned short field_12e;
} struct_10;

typedef struct struct_16 {
    char padding_0[8];
    unsigned int field_8;
} struct_16;

typedef struct struct_22 {
    char padding_0[8];
    unsigned int field_8;
} struct_22;

typedef struct struct_15 {
    unsigned long long field_0;
} struct_15;

typedef struct struct_20 {
    char padding_0[8];
    unsigned int field_8;
} struct_20;

typedef struct struct_26 {
    char padding_0[8];
    unsigned int field_8;
} struct_26;

typedef struct struct_19 {
    unsigned long long field_0;
} struct_19;

typedef struct struct_2 {
    char padding_0[8];
    unsigned int field_8;
} struct_2;

typedef struct struct_7 {
    char padding_0[8];
    unsigned int field_8;
} struct_7;

typedef struct struct_9 {
    char padding_0[8];
    unsigned int field_8;
} struct_9;

typedef struct struct_0 {
    char padding_0[8];
    unsigned int field_8;
} struct_0;

typedef struct struct_1 {
    char padding_0[176];
    struct struct_0 *field_b0;
    char padding_b8[118];
    unsigned short field_12e;
} struct_1;

extern struct_1 *g_1eefef8;
extern unsigned long long g_1eeff88;
extern long long g_1ef0c58;
extern long long g_1efd040;
extern char g_1fab44c;

unsigned long long WeaponEffects_ExplosionEffect(struct_6 *a0)
{
    struct_6 *ptr11;  // x20
    struct_25 *v6;  // x1
    struct_12 *ptr12;  // x0
    unsigned long long v17;  // x2
    unsigned long long v18;  // x1
    struct_6 *v19;  // x0
    long long v20;  // x21
    struct_11 **ptr8;  // x0
    struct_17 **ptr9;  // x0
    struct_23 *p;  // x8
    struct_17 **v24;  // x19
    struct_6 *ptr7;  // x19
    unsigned long v25;  // x9
    unsigned long cur;  // x10
    unsigned long v27;  // x9
    struct_14 *ptr13;  // x0
    unsigned long long v30;  // x2
    unsigned long long v31;  // x1
    struct_17 **v32;  // x0
    struct_21 **ptr10;  // x19
    struct_27 *addr;  // x8
    struct_6 *ptr;  // x19
    unsigned long v35;  // x9
    unsigned long iter;  // x10
    unsigned long v37;  // x9
    struct_18 *ptr14;  // x0
    unsigned long long v40;  // x2
    unsigned long long v41;  // x1
    struct_21 **v42;  // x0
    struct_5 *v9;  // x0
    struct_6 *v10;  // x0
    struct_5 *ptr5;  // x8
    unsigned long v12;  // x9
    unsigned long node;  // x10
    unsigned long v14;  // x9
    uint128_t choice;  // [bp-0xc0]
    uint128_t flag2;  // [bp-0xb0]
    unsigned long long flag;  // [bp-0x98]
    char *v3;  // [bp-0x60]
    char v4;  // [bp+0x0]

    v3 = &v4;
    ptr11 = a0;
    if (!(g_1fab44c & 1))
    {
        sub_f7d92c(&g_1efd040);
        sub_f7d92c(&g_1eefef8);
        sub_f7d92c(&g_1eeff88);
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c("cY");
        g_1fab44c = 1;
    }
    flag = 0;
    choice = 0;
    flag2 = 0;
    v6 = ptr11->field_78;
    ptr7 = ptr11;
    ptr7->field_80 = v6;
    ptr = &ptr7->field_80;
    sub_f7d8d0(ptr, v6);
    v9 = *((long long *)&ptr->padding_0[0]);
    if (v9 && !((v6 = NULL, v9 = (struct_5 *)(unsigned long long)GameObject__get_transform(v9, 0), !v9 || (v6 = NULL, Transform__set_position(), v9 = (struct_5 *)*((long long *)&ptr->padding_0[0]), !v9 || (v6 = NULL, v9 = (struct_5 *)(unsigned long long)GameObject__get_transform(v9, 0), !v9)))))
    {
        v6 = NULL;
        v10 = Transform__GetEnumerator();
        ptr = v10;
        if (v10)
        {
            ptr5 = *((long long *)&ptr->padding_0[0]);
            v12 = ptr5->field_12e;
            if (v12)
            {
                node = &ptr5->field_b0->field_8;
                do
                {
                    v14 = v12;
                    if (*((long long *)(node - 8)) == g_1eeff88)
                    {
                        ptr12 = &ptr5->padding_0[16 * *((int *)node) + 312];
                        v18 = *((long long *)&ptr12->padding_0[8]);
                        v19 = ptr;
                        (*((long long *)&ptr12->padding_0[0]))();
                    }
                } while ((node = (unsigned long)(node + 16), v12 = (unsigned long)(v14 - 1), v14 != 1));
            }
            v17 = 0;
            ptr12 = sub_f80110(ptr);
            v18 = *((long long *)&ptr12->padding_0[8]);
            v19 = ptr;
            (*((long long *)&ptr12->padding_0[0]))();
        }
    }
    else
    {
        v10 = sub_f7db74(v9);
    }
    sub_f7db74(v10);
    while (true)
    {
        v20 = sub_f1bd40(ptr11);
        if ((unsigned int)v6 != 1)
            break;
        ptr8 = __cxa_begin_catch(v20);
        ptr11 = *(ptr8);
        __cxa_end_catch(ptr8);
        v6 = g_1eefef8;
        ptr9 = sub_f7da60(ptr, g_1eefef8);
        if (ptr9)
        {
            p = *(ptr9);
            v24 = ptr9;
            v25 = p->field_12e;
            if (v25)
            {
                cur = &p->field_b0->field_8;
                do
                {
                    v27 = v25;
                    if (*((long long *)(cur - 8)) == g_1eefef8)
                    {
                        ptr13 = &p->padding_0[16 * *((int *)cur) + 312];
                        v31 = *((long long *)&ptr13->padding_0[8]);
                        v32 = v24;
                        (*((long long *)&ptr13->padding_0[0]))();
                    }
                } while ((cur = (unsigned long)(cur + 16), v25 = (unsigned long)(v27 - 1), v27 != 1));
            }
            v30 = 0;
            ptr13 = sub_f80110(v24);
            v31 = *((long long *)&ptr13->padding_0[8]);
            v32 = v24;
            (*((long long *)&ptr13->padding_0[0]))();
        }
        else if (!ptr11)
        {
            return 0;
        }
    }
    ptr10 = sub_f7da60(ptr, g_1eefef8);
    if (!ptr10)
    {
        sub_1026098(v20);
        sub_e29990(sub_f1bd40(0));
    }
    addr = *(ptr10);
    v35 = addr->field_12e;
    if (v35)
    {
        iter = &addr->field_b0->field_8;
        do
        {
            v37 = v35;
            if (*((long long *)(iter - 8)) == g_1eefef8)
            {
                ptr14 = &addr->padding_0[16 * *((int *)iter) + 312];
                v41 = *((long long *)&ptr14->padding_0[8]);
                v42 = ptr10;
                (*((long long *)&ptr14->padding_0[0]))();
            }
        } while ((iter = (unsigned long)(iter + 16), v35 = (unsigned long)(v37 - 1), v37 != 1));
    }
    v40 = 0;
    ptr14 = sub_f80110(ptr10);
    v41 = *((long long *)&ptr14->padding_0[8]);
    v42 = ptr10;
    (*((long long *)&ptr14->padding_0[0]))();
}
```

## `WeaponEffects.ctor` — RVA `0xc910f0`

- Decompiled symbol: `WeaponEffects_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `16` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[384];
    unsigned int field_180;
} struct_0;

long long WeaponEffects_ctor(struct_0 *ptr)
{
    long long v0;  // x0

    ptr->field_180 = 0x3f800000;
    v0 = MonoBehaviour__ctor();
    return MonoBehaviour__ctor();
}
```
