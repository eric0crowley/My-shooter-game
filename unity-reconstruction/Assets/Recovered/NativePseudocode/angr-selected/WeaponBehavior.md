# Native pseudocode: WeaponBehavior

> Metadata source-path string: `Assets/RFPSP/Scripts/Weapons/WeaponBehavior.cs`. This is a path string from the APK metadata, not recovered source text.

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `WeaponBehavior.CancelWeaponPull` — RVA `0xcb35f8`

- Decompiled symbol: `WeaponBehavior_CancelWeaponPull`
- Metadata signature: `public void CancelWeaponPull(bool neutralAnim = false) { }`
- Native interval: `140` bytes
- Result: `pseudocode`
- Heuristic layout hint: `WeaponBehavior_Recovered` matched 6 offsets against `WeaponBehavior` metadata (confidence 1.00).

```c
typedef struct WeaponBehavior_Recovered {
    char padding_0[272];
    unsigned long long WeaponAnimatorComponent;
    char padding_118[12];
    unsigned int weaponNumber;
    char padding_128[105];
    char fireOnReleaseState;
    char padding_192[54];
    unsigned long long fireHoldTimer;
    char padding_1d0[4];
    unsigned short pullAnimState;
    char padding_1d6[1210];
    unsigned long long otherfx;
} WeaponBehavior_Recovered;

extern long long g_1f0c5b0;
extern char g_1fab4ed;

unsigned long long WeaponBehavior_CancelWeaponPull(struct_0 *ptr, unsigned int a1)
{
    unsigned long v0;  // x0
    unsigned long long v1;  // x0
    unsigned long long v2;  // x0

    if (!(g_1fab4ed & 1))
    {
        sub_f7d92c(&g_1f0c5b0);
        g_1fab4ed = 1;
    }
    v0 = ptr->field_690;
    ptr->field_191 = 0;
    ptr->field_1d4 = 0;
    ptr->field_1c8 = 0;
    if (v0)
    {
        v1 = AudioSource__Stop(v0, 0);
        if (!((char)a1 & 1))
        {
            return v1;
        }
        else if (ptr->field_124)
        {
            v0 = ptr->field_110;
            if (v0)
            {
                v2 = Animator__SetTrigger();
                return Animator__SetTrigger();
            }
        }
        else
        {
            return v1;
        }
    }
    sub_f7db74(v0);
}
```


## `WeaponBehavior.InitializeWeapon` — RVA `0xcb485c`

- Decompiled symbol: `WeaponBehavior_InitializeWeapon`
- Metadata signature: `public void InitializeWeapon() { }`
- Native interval: `1984` bytes
- Result: `pseudocode`
- Heuristic layout hint: `WeaponBehavior_Recovered` matched 40 offsets against `WeaponBehavior` metadata (confidence 0.95).

```c
typedef struct WeaponBehavior_Recovered {
    char padding_0[64];
    long long playerObj;
    long long weaponObj;
    char padding_50[16];
    struct struct_5 *AmmoText1;
    struct struct_6 *AmmoText2;
    long long myTransform;
    long long mainCamTransform;
    struct struct_7 *FPSWalkerComponent;
    struct struct_13 *PlayerWeaponsComponent;
    struct struct_8 *IronsightsComponent;
    struct struct_10 *FPSPlayerComponent;
    char padding_a0[64];
    long long weaponMesh;
    char padding_e8[40];
    long long WeaponAnimatorComponent;
    char padding_118[16];
    int ammo;
    char padding_12c[36];
    unsigned int fireRate;
    char padding_154[161];
    char unarmed;
    char doReload;
    char nonReloadWeapon;
    char padding_1f8[12];
    unsigned int meleeSwingDelay;
    char padding_208[388];
    unsigned long long gunAnglesTarget;
    unsigned int field_394;
    unsigned long long gunAngles;
    unsigned int field_3a0;
    char padding_3a4[40];
    unsigned int readyTime;
    unsigned int offhandThrowReadyMod;
    unsigned int readyTimeAmt;
    char isOffhandThrow;
    char padding_3d9[7];
    unsigned int startTime;
    char padding_3e4[197];
    char muzzActive;
    char padding_4aa[134];
    long long capsule;
    char padding_538[328];
    struct struct_11 *aSources;
    long long firefx;
    long long otherfx;
    long long fireSnd;
    char padding_6a0[40];
    long long readySnd;
    char padding_6d0[40];
    unsigned long long firingPauseMinimumTime;
    long long autoFireAsource1;
    long long autoFireAsource2;
    char padding_710[29];
    char useLight;
    char padding_72e[13];
    char lightOn;
    char padding_73c[4];
    long long lightConeMesh;
    long long spot;
    long long point;
} WeaponBehavior_Recovered;

typedef struct struct_1 {
    char padding_0[40];
    long long field_28;
} struct_1;

typedef struct struct_2 {
    char padding_0[48];
    long long field_30;
} struct_2;

typedef struct struct_4 {
    char padding_0[80];
    struct struct_3 *field_50;
    char padding_58[120];
    unsigned long long field_d0;
    char padding_d8[56];
    unsigned long long field_110;
    unsigned long long field_118;
    char padding_120[245];
    char field_215;
} struct_4;

typedef struct struct_18 {
    char padding_0[297];
    char field_129;
} struct_18;

typedef struct struct_14 {
    char padding_0[416];
    char field_1a0;
} struct_14;

typedef struct struct_15 {
    char padding_0[24];
    unsigned int field_18;
    char padding_1c[4];
    unsigned long long field_20;
    unsigned long long field_28;
    unsigned long long field_30;
} struct_15;

typedef struct struct_16 {
    char padding_0[72];
    unsigned long long field_48;
} struct_16;

typedef struct struct_17 {
    char padding_0[72];
    unsigned long long field_48;
} struct_17;

typedef struct struct_5 {
    char padding_0[72];
    long long field_48;
} struct_5;

typedef struct struct_6 {
    char padding_0[72];
    unsigned long long field_48;
} struct_6;

typedef struct struct_7 {
    char padding_0[416];
    char field_1a0;
} struct_7;

typedef struct struct_13 {
    char padding_0[296];
    char field_128;
    char padding_129[85];
    char field_17e;
} struct_13;

typedef struct struct_8 {
    char padding_0[297];
    char field_129;
} struct_8;

typedef struct struct_10 {
    char padding_0[80];
    struct struct_9 *field_50;
    char padding_58[120];
    long long field_d0;
    char padding_d8[56];
    long long field_110;
    long long field_118;
    char padding_120[245];
    char field_215;
} struct_10;

typedef struct struct_11 {
    char padding_0[24];
    unsigned int field_18;
    char padding_1c[4];
    long long field_20;
    long long field_28;
    long long field_30;
} struct_11;

typedef struct struct_3 {
    char padding_0[297];
    char field_129;
} struct_3;

typedef struct struct_9 {
    char padding_0[297];
    char field_129;
} struct_9;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern long long g_1efcf38;
extern long long g_1efeb20;
extern long long g_1efeb28;
extern long long g_1efeb88;
extern long long g_1efebb8;
extern long long g_1efebc0;
extern long long g_1efec90;
extern long long g_1efed90;
extern long long g_1f0d320;
extern long long g_1f0d410;
extern char g_1fab4e1;

long long WeaponBehavior_InitializeWeapon(struct_12 *ptr)
{
    long long v0;  // x0
    struct_12 *p;  // x20
    struct_2 *ptr12;  // x0
    long long v11;  // x1
    struct_12 *addr;  // x21
    struct_12 *v13;  // x21
    struct_4 *v14;  // x0
    struct_12 *ptr3;  // x25
    struct_12 *v16;  // x25
    struct_18 *v17;  // x1
    struct_12 *ptr4;  // x21
    struct_12 *v19;  // x21
    struct_12 *v2;  // x20
    char v20[383];  // x0
    struct_12 *ptr5;  // x21
    struct_12 *v22;  // x21
    long long v23;  // x0
    struct_12 *v24;  // x22
    struct_14 *v25;  // x0
    struct_12 *ptr6;  // x24
    struct_12 *v27;  // x24
    struct_15 *v28;  // x0
    struct_12 *ptr11;  // x26
    long long v3;  // x0
    unsigned long v30;  // x0
    struct_15 *ptr13;  // x8
    unsigned long v32;  // x1
    struct_12 *v33;  // x23
    struct_15 *ptr14;  // x8
    unsigned long v35;  // x1
    struct_12 *v36;  // x27
    struct_15 *ptr15;  // x8
    unsigned long v38;  // x1
    struct_15 *ptr16;  // x8
    struct_12 *ptr7;  // x21
    unsigned long v40;  // x1
    unsigned long v41;  // d0
    long long v42;  // x1
    struct_4 *v43;  // x8
    struct_16 *v44;  // x0
    struct_12 *ptr8;  // x27
    struct_12 *v46;  // x27
    struct_17 *v47;  // x0
    struct_12 *ptr9;  // x26
    struct_12 *v49;  // x26
    struct_12 *v5;  // x21
    unsigned long long v50;  // 4103
    long long v51;  // x0
    unsigned long v52;  // x0
    unsigned long v53;  // 4129
    long long v54;  // x0
    unsigned long v55;  // 4125
    long long v56;  // x0
    struct_12 *idx17;  // x8
    long long v58;  // x0
    long long v59;  // x0
    struct_1 *ptr17;  // x0
    unsigned int v60;  // s0
    unsigned int v61;  // s1
    unsigned long v62;  // x0
    unsigned long v63;  // x19
    unsigned long v64;  // x0
    long long v65;  // x0
    unsigned long long v66;  // x0
    long long v7;  // x1
    struct_12 *ptr10;  // x21
    struct_12 *v9;  // x21

    if (!(g_1fab4e1 & 1))
    {
        sub_f7d92c(&g_1efcf38);
        sub_f7d92c(&g_1efeb20);
        sub_f7d92c(&g_1efeb28);
        sub_f7d92c(&g_1efeb88);
        sub_f7d92c(&g_1efebb8);
        sub_f7d92c(&g_1efebc0);
        sub_f7d92c(&g_1efec90);
        sub_f7d92c(&g_1efed90);
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c(&g_1f0d410);
        sub_f7d92c(&g_1f0d320);
        g_1fab4e1 = 1;
    }
    v0 = Component__get_transform(ptr, 0);
    p = ptr;
    p->field_70 = v0;
    v2 = &p->field_70;
    sub_f7d8d0(v2, v0);
    if (Camera__get_main(0))
    {
        v3 = Component__get_transform();
        ptr7 = ptr;
        ptr7->field_78 = v3;
        v5 = &ptr7->field_78;
        sub_f7d8d0(v5, v3);
        if (*((long long *)&v5->padding_0[0]) && (ptr17 = (struct_1 *)sub_1231bc8(*((long long *)&v5->padding_0[0]), g_1efcf38), ptr17))
        {
            v7 = ptr17->field_28;
            ptr10 = ptr;
            ptr10->field_40 = v7;
            v9 = &ptr10->field_40;
            sub_f7d8d0(v9, v7);
            if (*((long long *)&v9->padding_0[56]) && (ptr12 = (struct_2 *)sub_1231bc8(*((long long *)&v9->padding_0[56]), g_1efcf38), ptr12))
            {
                v11 = ptr12->field_30;
                addr = ptr;
                addr->field_48 = v11;
                v13 = &addr->field_48;
                sub_f7d8d0(v13, v11);
                if (*((long long *)&v13->padding_0[8]))
                {
                    v14 = sub_1249224(*((long long *)&v13->padding_0[8]), g_1efebb8);
                    ptr3 = ptr;
                    ptr3->field_98 = v14;
                    v16 = &ptr3->field_98;
                    sub_f7d8d0(v16, v14);
                    if (*((long long *)&v16->padding_0[0]))
                    {
                        v17 = *((long long *)(*((long long *)&v16->padding_0[0]) + 80));
                        ptr4 = ptr;
                        ptr4->field_90 = v17;
                        v19 = &ptr4->field_90;
                        sub_f7d8d0(v19, v17);
                        if (v19->field_48)
                        {
                            v20 = sub_1249224(v19->field_48, g_1efec90);
                            ptr5 = ptr;
                            ptr5->field_88 = v20;
                            v22 = &ptr5->field_88;
                            sub_f7d8d0(v22, v20);
                            if (*((long long *)&v22->padding_50[8]))
                            {
                                v23 = sub_1249224(*((long long *)&v22->padding_50[8]), g_1efeb28);
                                v24 = &ptr->field_110;
                                ptr->field_110 = v23;
                                sub_f7d8d0(v24, v23);
                                if (ptr->field_40)
                                {
                                    v25 = sub_1249224(ptr->field_40, g_1efebc0);
                                    ptr6 = ptr;
                                    ptr6->field_80 = v25;
                                    v27 = &ptr6->field_80;
                                    sub_f7d8d0(v27, v25);
                                    if (*((long long *)&v27->padding_0[56]))
                                    {
                                        v28 = sub_1249b80(*((long long *)&v27->padding_0[56]), g_1efed90);
                                        ptr11 = &ptr->padding_538[320];
                                        *((struct_15 **)&ptr->padding_538[320]) = v28;
                                        v30 = sub_f7d8d0(ptr11, v28);
                                        ptr13 = *((long long *)&ptr->padding_538[320]);
                                        if (ptr13)
                                        {
                                            if (ptr13->field_18 <= 1)
                                                sub_f7db7c(v30);
                                            v32 = ptr13->field_28;
                                            v33 = &ptr->field_688;
                                            ptr->field_688 = v32;
                                            v30 = sub_f7d8d0(v33, v32);
                                            ptr14 = *((long long *)&ptr->padding_538[320]);
                                            if (ptr14)
                                            {
                                                if (!ptr14->field_18)
                                                    sub_f7db7c(v30);
                                                v35 = ptr14->field_20;
                                                v36 = &ptr->field_680;
                                                ptr->field_680 = v35;
                                                sub_f7d8d0(v36, v35);
                                                if (ptr->field_680 && (AudioSource__set_clip(ptr->field_680, ptr->field_690, 0), ptr->field_680 && (AudioSource__set_spatialBlend(ptr->field_680, 0), *((long long *)&v36->padding_0[0]) && (AudioSource__set_panStereo(*((long long *)&v36->padding_0[0]), 0), *((long long *)&v36->padding_0[0]) && (v30 = (unsigned long)(unsigned long long)AudioSource__set_velocityUpdateMode(*((long long *)&v36->padding_0[0]), 0, 0), ptr15 = (struct_15 *)*((long long *)&ptr11->padding_0[0]), ptr15)))))
                                                {
                                                    if (!ptr15->field_18)
                                                        sub_f7db7c(v30);
                                                    v38 = ptr15->field_20;
                                                    ptr->field_6f8 = v38;
                                                    v30 = sub_f7d8d0(&ptr->field_6f8, v38);
                                                    ptr16 = *((long long *)&ptr->padding_538[320]);
                                                    if (ptr16)
                                                    {
                                                        if (ptr16->field_18 <= 2)
                                                            sub_f7db7c(v30);
                                                        v40 = ptr16->field_30;
                                                        ptr->field_700 = v40;
                                                        sub_f7d8d0(&ptr->field_700, v40);
                                                        if (ptr->field_700)
                                                        {
                                                            AudioSource__set_clip(ptr->field_700, ptr->field_690, 0);
                                                            v41 = ptr->field_150;
                                                            *((unsigned long *)&ptr->padding_6d0[32]) = v41;
                                                            WeaponBehavior__CancelWeaponPull(ptr, 0);
                                                            if (ptr->field_40)
                                                            {
                                                                v42 = sub_1249224(ptr->field_40, g_1efeb88);
                                                                *((long long *)&ptr->padding_4aa[126]) = v42;
                                                                sub_f7d8d0(&ptr->padding_4aa[126], v42);
                                                                v43 = ptr->field_98;
                                                                ptr->padding_3e4[189] = 1;
                                                                if (v43 && v43->field_110)
                                                                {
                                                                    v44 = sub_1249224(v43->field_110, g_1efeb20);
                                                                    ptr8 = ptr;
                                                                    ptr8->field_60 = v44;
                                                                    v46 = &ptr8->field_60;
                                                                    sub_f7d8d0(v46, v44);
                                                                    if (*((long long *)&v46->padding_0[56]) && *((long long *)(*((long long *)&v46->padding_0[56]) + 280)))
                                                                    {
                                                                        v47 = sub_1249224(*((long long *)(*((long long *)&v46->padding_0[56]) + 280)), g_1efeb20);
                                                                        ptr9 = ptr;
                                                                        ptr9->field_68 = v47;
                                                                        v49 = &ptr9->field_68;
                                                                        sub_f7d8d0(v49, v47);
                                                                        if (*((long long *)&v49->padding_0[48]) && *((long long *)(*((long long *)&v49->padding_0[48]) + 208)) && (GameObject__SetActive(*((long long *)(*((long long *)&v49->padding_0[48]) + 208)), 1, 0), *((long long *)&v16->padding_0[0])))
                                                                        {
                                                                            if (!*((char *)(*((long long *)&v16->padding_0[0]) + 533)) || ptr->field_1f5 || !((v41 = (unsigned long)(unsigned long long)ptr->field_204, v50 = ((((unsigned long long)(char)(CmpF((unsigned int)v41, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF((unsigned int)v41, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF((unsigned int)v41, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF((unsigned int)v41, 0.0) & 1)) & ((unsigned long long)(char)(CmpF((unsigned int)v41, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF((unsigned int)v41, 0.0) & 1)) >> 1 & 1), (char)(v50 * 0x10000000 >> 30))))
                                                                            {
                                                                                if (*((long long *)&v46->padding_0[0]) && *((long long *)(*((long long *)&v46->padding_0[0]) + 72)) && (Behaviour__set_enabled(*((long long *)(*((long long *)&v46->padding_0[0]) + 72)), 0, 0), *((long long *)&v49->padding_0[0]) && *((long long *)(*((long long *)&v49->padding_0[0]) + 72))))
                                                                                    goto LABEL_10b4ca4;
                                                                            }
                                                                            else if (*((long long *)&v46->padding_0[0]) && *((long long *)(*((long long *)&v46->padding_0[0]) + 72)) && (Behaviour__set_enabled(*((long long *)(*((long long *)&v46->padding_0[0]) + 72)), 1, 0), *((long long *)&v49->padding_0[0]) && *((long long *)(*((long long *)&v49->padding_0[0]) + 72))))
                                                                            {
LABEL_10b4ca4:
                                                                                v51 = Behaviour__set_enabled();
                                                                                if (!(!ptr->field_1f5 && !ptr->field_1f6 && !ptr->field_1f7 && 0 >= ptr->field_128))
                                                                                {
LABEL_10b4ce0:
                                                                                    if (ptr->padding_710[21])
                                                                                    {
                                                                                        if (!g_1ef0c58->field_e0)
                                                                                            sub_f7da5c(g_1ef0c58);
                                                                                        v52 = Object__op_Implicit(*((long long *)&ptr->padding_72e[10]), 0);
                                                                                        if (ptr->padding_72e[5])
                                                                                        {
                                                                                            if (((char)v52 & 1))
                                                                                            {
                                                                                                if (*((long long *)&ptr->padding_72e[10]))
                                                                                                {
                                                                                                    Renderer__set_enabled(*((long long *)&ptr->padding_72e[10]), 1, 0);
                                                                                                    goto LABEL_10b4d30;
                                                                                                }
                                                                                            }
                                                                                            else
                                                                                            {
LABEL_10b4d30:
                                                                                                if (!g_1ef0c58->field_e0)
                                                                                                    sub_f7da5c(g_1ef0c58);
                                                                                                if (((char)Object__op_Implicit(ptr->field_740, 0) & 1))
                                                                                                {
                                                                                                    if (ptr->field_740)
                                                                                                    {
                                                                                                        Behaviour__set_enabled(ptr->field_740, 1, 0);
                                                                                                        goto LABEL_10b4d68;
                                                                                                    }
                                                                                                }
                                                                                                else
                                                                                                {
LABEL_10b4d68:
                                                                                                    if (!g_1ef0c58->field_e0)
                                                                                                        sub_f7da5c(g_1ef0c58);
                                                                                                    v51 = Object__op_Implicit(ptr->field_748, 0);
                                                                                                    if (!(v51 & 1))
                                                                                                        goto LABEL_10b4e64;
                                                                                                    if (ptr->field_748)
                                                                                                        goto LABEL_10b4e58;
                                                                                                }
                                                                                            }
                                                                                        }
                                                                                        else
                                                                                        {
                                                                                            if (((char)v52 & 1))
                                                                                            {
                                                                                                if (*((long long *)&ptr->padding_72e[10]))
                                                                                                {
                                                                                                    Renderer__set_enabled(*((long long *)&ptr->padding_72e[10]), 0, 0);
                                                                                                    goto LABEL_10b4df4;
                                                                                                }
                                                                                            }
                                                                                            else
                                                                                            {
LABEL_10b4df4:
                                                                                                if (!g_1ef0c58->field_e0)
                                                                                                    sub_f7da5c(g_1ef0c58);
                                                                                                if (((char)Object__op_Implicit(ptr->field_740, 0) & 1))
                                                                                                {
                                                                                                    if (ptr->field_740)
                                                                                                    {
                                                                                                        Behaviour__set_enabled(ptr->field_740, 0, 0);
                                                                                                        goto LABEL_10b4e2c;
                                                                                                    }
                                                                                                }
                                                                                                else
                                                                                                {
LABEL_10b4e2c:
                                                                                                    if (!g_1ef0c58->field_e0)
                                                                                                        sub_f7da5c(g_1ef0c58);
                                                                                                    v51 = Object__op_Implicit(ptr->field_748, 0);
                                                                                                    if (!(v51 & 1))
                                                                                                        goto LABEL_10b4e64;
                                                                                                    if (ptr->field_748)
                                                                                                    {
LABEL_10b4e58:
                                                                                                        v51 = Behaviour__set_enabled();
                                                                                                        goto LABEL_10b4e64;
                                                                                                    }
                                                                                                }
                                                                                            }
                                                                                        }
                                                                                    }
                                                                                    else
                                                                                    {
LABEL_10b4e64:
                                                                                        if (ptr->field_1f5)
                                                                                            return v51;
                                                                                        if (0 >= ptr->field_128 && !ptr->field_1f6)
                                                                                        {
                                                                                            v41 = ptr->field_204;
                                                                                            v53 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF((unsigned int)v41, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF((unsigned int)v41, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF((unsigned int)v41, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF((unsigned int)v41, 0.0) & 1)) & ((unsigned long long)(char)(CmpF((unsigned int)v41, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF((unsigned int)v41, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                                                                                            if ((char)v53)
                                                                                                return v51;
                                                                                        }
                                                                                        v54 = Time__get_timeSinceLevelLoad(0);
                                                                                        v55 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF((unsigned int)v41, 0x40000000)) >> 5 & 3 | (unsigned long long)(CmpF((unsigned int)v41, 0x40000000) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF((unsigned int)v41, 0x40000000)) >> 5 & 3 | (unsigned long long)(CmpF((unsigned int)v41, 0x40000000) & 1)) & ((unsigned long long)(char)(CmpF((unsigned int)v41, 0x40000000)) >> 5 & 3 | (unsigned long long)(CmpF((unsigned int)v41, 0x40000000) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                                                                                        if ((char)v55)
                                                                                            return v54;
                                                                                        if (*((long long *)&v22->padding_0[0]))
                                                                                        {
                                                                                            if (*((char *)(*((long long *)&v22->padding_0[0]) + 296)))
                                                                                            {
                                                                                                MonoBehaviour__StopCoroutine(ptr, g_1f0d410, 0);
                                                                                                if (ptr->field_90)
                                                                                                {
                                                                                                    ptr->field_90->field_129 = 0;
                                                                                                    Time__get_time(0);
                                                                                                    *((unsigned int *)&ptr->field_3d8) = v41;
                                                                                                    v56 = Component__get_transform(ptr, 0);
                                                                                                    ptr->field_70 = v56;
                                                                                                    sub_f7d8d0(v2, v56);
                                                                                                    idx17 = &(&ptr->padding_208)[1];
                                                                                                    v58 = ptr->field_70;
                                                                                                    *((long long *)&ptr->field_394) = *((long long *)&idx17->padding_0[0]);
                                                                                                    *((int *)&ptr->field_398) = *((int *)&idx17->padding_0[8]);
                                                                                                    if (v58)
                                                                                                    {
                                                                                                        v59 = Transform__set_localEulerAngles(v58, 0);
                                                                                                        v60 = *((int *)&ptr->padding_3a4[32]);
                                                                                                        if ((char)ptr->field_3d0)
                                                                                                        {
                                                                                                            v61 = *((int *)&ptr->padding_3a4[36]);
                                                                                                            *((char *)&ptr->field_3d0) = 0;
                                                                                                            ptr->field_3cc = v60 * v61;
                                                                                                            return v59;
                                                                                                        }
                                                                                                        v62 = ptr->field_688;
                                                                                                        ptr->field_3cc = v60;
                                                                                                        if (v62)
                                                                                                        {
                                                                                                            AudioSource__set_volume(v62, 0);
                                                                                                            if (*((long long *)&v33->padding_0[0]))
                                                                                                            {
                                                                                                                AudioSource__set_clip(*((long long *)&v33->padding_0[0]), *((long long *)&ptr->padding_6a0[32]), 0);
                                                                                                                v63 = ptr->field_688;
                                                                                                                if (v63)
                                                                                                                {
                                                                                                                    v64 = AudioSource__get_clip(v63, 0);
                                                                                                                    if (*((long long *)&v33->padding_0[0]))
                                                                                                                    {
                                                                                                                        AudioSource__get_volume(*((long long *)&v33->padding_0[0]), 0);
                                                                                                                        v65 = AudioSource__PlayOneShot(v63, v64, 0);
                                                                                                                        if (*((long long *)&v22->padding_0[0]))
                                                                                                                        {
                                                                                                                            if (*((char *)(*((long long *)&v22->padding_0[0]) + 382)))
                                                                                                                                return v65;
                                                                                                                            if (*((long long *)&v24->padding_0[0]))
                                                                                                                            {
                                                                                                                                v66 = Animator__SetTrigger();
                                                                                                                                return Animator__SetTrigger();
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
                                                                                                return v54;
                                                                                            }
                                                                                        }
                                                                                    }
                                                                                }
                                                                                else if (*((long long *)&v27->padding_0[0]))
                                                                                {
                                                                                    *((char *)(*((long long *)&v27->padding_0[0]) + 416)) = 1;
                                                                                    goto LABEL_10b4ce0;
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
    sub_f7db7c(sub_f7db74());
}
```


## `WeaponBehavior.Start` — RVA `0xcb583c`

- Decompiled symbol: `WeaponBehavior_Start`
- Metadata signature: `private void Start() { }`
- Native interval: `2696` bytes
- Result: `pseudocode`
- Heuristic layout hint: `WeaponBehavior_Recovered` matched 9 offsets against `WeaponBehavior` metadata (confidence 1.00).

```c
typedef struct struct_17 {
    char padding_0[64];
    long long field_40;
    long long field_48;
    char padding_50[16];
    long long field_60;
    long long field_68;
    long long field_70;
    long long field_78;
    long long field_80;
    struct struct_7 *field_88;
    struct struct_8 *field_90;
    struct struct_11 *field_98;
    long long field_a0;
    long long field_a8;
    long long field_b0;
    struct struct_12 *field_b8;
    long long field_c0;
    long long field_c8;
    long long field_d0;
    char padding_d8[8];
    long long field_e0;
    unsigned int field_e8;
    unsigned int field_ec;
    unsigned int field_f0;
    char padding_f4[4];
    unsigned int field_f8;
    unsigned int field_fc;
    unsigned int field_100;
    char padding_104[4];
    long long field_108;
    long long field_110;
    long long field_118;
    char padding_120[8];
    int field_128;
    int field_12c;
    char padding_130[4];
    int field_134;
    char padding_138[28];
    int field_154;
    char padding_158[134];
    char field_1de;
    char padding_1df[18];
    char field_1f1;
    char field_1f2;
    char padding_1f3[2];
    char field_1f5;
    char padding_1f6[6];
    unsigned int field_1fc;
    char padding_200[4];
    unsigned int field_204;
    char padding_208[316];
    char field_344;
    char padding_345[11];
    unsigned int field_350;
    char padding_354[40];
    unsigned int field_37c;
    char padding_380[12];
    unsigned long long field_38c;
    unsigned int field_394;
    unsigned long long field_398;
    unsigned int field_3a0;
    char padding_3a4[56];
    unsigned int field_3dc;
    char padding_3e0[16];
    long long field_3f0;
    unsigned int field_3f8;
    unsigned int field_3fc;
    unsigned int field_400;
    char padding_404[12];
    unsigned int field_410;
    char padding_414[52];
    long long field_448;
    unsigned int field_450;
    unsigned int field_454;
    unsigned int field_458;
    unsigned int field_45c;
    unsigned int field_460;
    char padding_464[4];
    long long field_468;
    char padding_470[8];
    long long field_478;
    long long field_480;
    char padding_488[8];
    long long field_490;
    long long field_498;
    char padding_4a0[64];
    long long field_4e0;
    char padding_4e8[72];
    long long field_530;
    char padding_538[8];
    long long field_540;
    char padding_548[16];
    long long field_558;
    struct struct_13 *field_560;
    struct struct_14 *field_568;
    struct struct_15 *field_570;
    char padding_578[8];
    uint128_t field_580;
    char padding_590[24];
    unsigned int field_5a8;
    unsigned int field_5ac;
    char padding_5b0[208];
    struct struct_16 *field_680;
    long long field_688;
    long long field_690;
    long long field_698;
    char padding_6a0[96];
    long long field_700;
    long long field_708;
} struct_17;

typedef struct struct_1 {
    char padding_0[40];
    long long field_28;
} struct_1;

typedef struct struct_2 {
    char padding_0[48];
    long long field_30;
} struct_2;

typedef struct WeaponBehavior_Recovered {
    char padding_0[80];
    struct struct_3 *ammoUiObj;
    unsigned long long ammoUiObjShadow;
    unsigned long long AmmoText1;
    struct struct_4 *AmmoText2;
    char padding_70[16];
    unsigned long long FPSWalkerComponent;
    unsigned long long PlayerWeaponsComponent;
    unsigned long long IronsightsComponent;
    char padding_98[120];
    unsigned long long WeaponAnimatorComponent;
    unsigned long long CameraAnimatorComponent;
} WeaponBehavior_Recovered;

typedef struct struct_26 {
    char padding_0[40];
    unsigned long long field_28;
} struct_26;

typedef struct struct_25 {
    char padding_0[352];
    unsigned long long field_160;
    uint128_t field_168;
} struct_25;

typedef struct struct_6 {
    char padding_0[168];
    unsigned long long field_a8;
} struct_6;

typedef struct struct_12 {
    char padding_0[168];
    long long field_a8;
} struct_12;

typedef struct struct_18 {
    char padding_0[24];
    unsigned int field_18;
    char padding_1c[4];
    unsigned long long field_20;
    unsigned long long field_28;
    unsigned long long field_30;
} struct_18;

typedef struct struct_19 {
    char padding_0[24];
    unsigned int field_18;
} struct_19;

typedef struct struct_23 {
    char padding_0[32];
    long long field_20;
} struct_23;

typedef struct struct_20 {
    char padding_0[24];
    unsigned int field_18;
} struct_20;

typedef struct struct_27 {
    char padding_0[16];
    unsigned long long field_10;
    unsigned int field_18;
    unsigned int field_1c;
} struct_27;

typedef struct struct_24 {
    char padding_0[32];
    unsigned long long field_20;
} struct_24;

typedef struct struct_7 {
    char padding_0[352];
    long long field_160;
    uint128_t field_168;
} struct_7;

typedef struct struct_8 {
    char padding_0[40];
    long long field_28;
} struct_8;

typedef struct struct_11 {
    char padding_0[80];
    struct struct_9 *field_50;
    long long field_58;
    long long field_60;
    struct struct_10 *field_68;
    char padding_70[16];
    long long field_80;
    long long field_88;
    long long field_90;
    char padding_98[120];
    long long field_110;
    long long field_118;
} struct_11;

typedef struct struct_13 {
    char padding_0[24];
    unsigned int field_18;
} struct_13;

typedef struct struct_14 {
    char padding_0[24];
    unsigned int field_18;
} struct_14;

typedef struct struct_15 {
    char padding_0[16];
    unsigned long long field_10;
    unsigned int field_18;
    unsigned int field_1c;
} struct_15;

typedef struct struct_16 {
    char padding_0[24];
    unsigned int field_18;
    char padding_1c[4];
    long long field_20;
    long long field_28;
    long long field_30;
} struct_16;

typedef struct struct_3 {
    char padding_0[40];
    unsigned long long field_28;
} struct_3;

typedef struct struct_4 {
    char padding_0[352];
    unsigned long long field_160;
    uint128_t field_168;
} struct_4;

typedef struct struct_9 {
    char padding_0[40];
    unsigned long long field_28;
} struct_9;

typedef struct struct_10 {
    char padding_0[352];
    unsigned long long field_160;
    uint128_t field_168;
} struct_10;

typedef struct struct_22 {
    char padding_0[4];
    unsigned int field_4;
    unsigned int field_8;
} struct_22;

typedef struct struct_21 {
    char padding_0[184];
    struct struct_22 *field_b8;
} struct_21;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern struct_21 *g_1ef22e8;
extern long long g_1ef8070;
extern long long g_1efcf08;
extern long long g_1efcf38;
extern long long g_1efd070;
extern long long g_1efeb20;
extern long long g_1efeb28;
extern long long g_1efeb88;
extern long long g_1efebb8;
extern long long g_1efec30;
extern long long g_1efed90;
extern long long g_1efeda8;
extern long long g_1f10970;
extern char g_1fab2c9;
extern char g_1fab4e0;
extern unsigned int g_832198[4];

long long WeaponBehavior_Start(struct_17 *ptr)
{
    long long v0;  // x1
    struct_17 *ptr5;  // x0
    long long v10;  // x1
    int v101;  // w9
    int v102;  // w9
    int v104;  // w8
    unsigned int v105;  // s0
    unsigned int v106;  // w0
    unsigned int v107;  // s0
    struct_17 *idx29;  // x9
    unsigned long v109;  // x0
    struct_17 *ptr6;  // x0
    long long v110;  // x0
    unsigned long v111;  // x0
    int v113;  // w11
    int v114;  // w12
    unsigned int v115;  // w9
    unsigned int v116;  // w9
    unsigned int v117;  // w9
    int v118;  // w11
    unsigned int v119;  // w8
    long long v12;  // x1
    unsigned int v120;  // s0
    long long v13;  // x1
    long long v14;  // x1
    struct_5 *v15;  // x0
    struct_17 *ptr7;  // x21
    struct_17 *v17;  // x21
    unsigned long v18;  // x1
    struct_17 *ptr8;  // x21
    long long v2;  // x0
    struct_17 *idx11;  // x21
    struct_26 *v21;  // x1
    struct_17 *ptr9;  // x21
    struct_17 *idx13;  // x21
    struct_25 *v24;  // x1
    struct_17 *ptr10;  // x21
    struct_17 *idx15;  // x21
    unsigned long v27;  // x1
    struct_17 *ptr11;  // x21
    struct_17 *v29;  // x21
    struct_17 *ptr12;  // x20
    unsigned long v30;  // x1
    struct_17 *ptr13;  // x21
    struct_17 *v32;  // x21
    unsigned long v33;  // x1
    struct_17 *ptr14;  // x0
    struct_6 *v35;  // x0
    struct_17 *ptr15;  // x21
    struct_17 *v37;  // x21
    unsigned long v38;  // x1
    struct_17 *ptr16;  // x21
    struct_17 *v4;  // x20
    struct_17 *v40;  // x21
    unsigned long v41;  // x1
    struct_17 *ptr17;  // x21
    struct_17 *v43;  // x21
    long long v44;  // x1
    struct_17 *ptr18;  // x21
    struct_17 *v46;  // x21
    unsigned long v47;  // x0
    unsigned int v48;  // s0
    unsigned int v49;  // s1
    struct_1 *ptr22;  // x0
    unsigned int v50;  // s2
    struct_5 *v51;  // x8
    long long v52;  // x0
    struct_17 *ptr19;  // x21
    struct_17 *v54;  // x21
    long long v55;  // x0
    struct_17 *ptr20;  // x21
    struct_17 *v57;  // x21
    struct_18 *v58;  // x1
    unsigned long v59;  // x0
    long long v6;  // x1
    struct_18 *ptr23;  // x8
    unsigned long v61;  // x1
    struct_18 *ptr24;  // x8
    unsigned long v63;  // x1
    struct_18 *ptr25;  // x8
    unsigned long v65;  // x1
    struct_18 *ptr26;  // x8
    unsigned long v67;  // x1
    struct_25 *ptr4;  // x8
    int v69;  // q0
    struct_17 *ptr21;  // x20
    unsigned long v70;  // x1
    struct_19 *v71;  // x0
    struct_17 *ptr3;  // x21
    struct_19 *ptr27;  // x8
    unsigned long long v74;  // x27
    struct_17 *addr;  // x22
    unsigned long v76;  // x9
    struct_19 *v77;  // x8
    struct_23 *v78;  // x8
    struct_20 *v79;  // x0
    struct_17 *v8;  // x20
    struct_20 *ptr28;  // x8
    unsigned long long v81;  // x23
    unsigned long v82;  // x9
    struct_27 *p;  // x0
    unsigned long v84;  // x1
    unsigned long v85;  // x8
    unsigned long v86;  // x10
    struct_24 *ptr29;  // x8
    long long v88;  // x1
    unsigned long v89;  // x0
    struct_2 *ptr30;  // x0
    unsigned int v90;  // s3
    unsigned long v91;  // x20
    unsigned int v92;  // s1
    unsigned int v93;  // s2
    long long v94;  // x1
    long long v95;  // x1
    unsigned long v96;  // x0
    long long v97;  // x1
    unsigned int v98;  // s0
    unsigned long long v99;  // 4103

    if (!(g_1fab4e0 & 1))
    {
        sub_f7d92c(&g_1efcf08);
        sub_f7d92c(&g_1efcf38);
        sub_f7d92c(&g_1efd070);
        sub_f7d92c(&g_1efeb20);
        sub_f7d92c(&g_1efeb28);
        sub_f7d92c(&g_1efeb88);
        sub_f7d92c(&g_1efebb8);
        sub_f7d92c(&g_1efec30);
        sub_f7d92c(&g_1efeda8);
        sub_f7d92c(&g_1efed90);
        sub_f7d92c(&g_1ef8070);
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c(&g_1f10970);
        g_1fab4e0 = 1;
    }
    v0 = Component__get_transform(ptr, 0);
    ptr5 = ptr;
    ptr5->field_70 = v0;
    sub_f7d8d0(&ptr5->field_70, v0);
    if (Camera__get_main(0))
    {
        v2 = Component__get_transform();
        ptr12 = ptr;
        ptr12->field_78 = v2;
        v4 = &ptr12->field_78;
        sub_f7d8d0(v4, v2);
        if (*((long long *)&v4->padding_0[0]))
        {
            ptr22 = sub_1231bc8(*((long long *)&v4->padding_0[0]), g_1efcf38);
            if (ptr22)
            {
                v6 = ptr22->field_28;
                ptr21 = ptr;
                ptr21->field_40 = v6;
                v8 = &ptr21->field_40;
                sub_f7d8d0(v8, v6);
                if (*((long long *)&v8->padding_0[56]))
                {
                    ptr30 = sub_1231bc8(*((long long *)&v8->padding_0[56]), g_1efcf38);
                    if (ptr30)
                    {
                        v10 = ptr30->field_30;
                        ptr6 = ptr;
                        ptr6->field_48 = v10;
                        sub_f7d8d0(&ptr6->field_48, v10);
                        v12 = sub_1231bc8(ptr, g_1efcf08);
                        ptr->field_108 = v12;
                        sub_f7d8d0(&ptr->field_108, v12);
                        if (Camera__get_main(0))
                        {
                            v13 = sub_1231bc8();
                            ptr->field_118 = v13;
                            sub_f7d8d0(&ptr->field_118, v13);
                            if (ptr->field_e0)
                            {
                                v14 = sub_1249224(ptr->field_e0, g_1efeb28);
                                ptr->field_110 = v14;
                                sub_f7d8d0(&ptr->field_110, v14);
                                if (ptr->field_40)
                                {
                                    v15 = sub_1249224(ptr->field_40, g_1efebb8);
                                    ptr7 = ptr;
                                    ptr7->field_98 = v15;
                                    v17 = &ptr7->field_98;
                                    sub_f7d8d0(v17, v15);
                                    if (*((long long *)&v17->padding_0[0]))
                                    {
                                        v18 = *((long long *)(*((long long *)&v17->padding_0[0]) + 96));
                                        ptr8 = ptr;
                                        ptr8->field_80 = v18;
                                        idx11 = &ptr8->field_80;
                                        sub_f7d8d0(idx11, v18);
                                        if (*((long long *)&idx11->padding_0[24]))
                                        {
                                            v21 = *((long long *)(*((long long *)&idx11->padding_0[24]) + 80));
                                            ptr9 = ptr;
                                            ptr9->field_90 = v21;
                                            idx13 = &ptr9->field_90;
                                            sub_f7d8d0(idx13, v21);
                                            if (*((long long *)&idx13->padding_0[8]))
                                            {
                                                v24 = *((long long *)(*((long long *)&idx13->padding_0[8]) + 104));
                                                ptr10 = ptr;
                                                ptr10->field_88 = v24;
                                                idx15 = &ptr10->field_88;
                                                sub_f7d8d0(idx15, v24);
                                                if (*((long long *)&idx15->padding_0[16]))
                                                {
                                                    v27 = *((long long *)(*((long long *)&idx15->padding_0[16]) + 88));
                                                    ptr11 = ptr;
                                                    ptr11->field_a0 = v27;
                                                    v29 = &ptr11->field_a0;
                                                    sub_f7d8d0(v29, v27);
                                                    if (*((long long *)&v29->padding_0[8]))
                                                    {
                                                        v30 = *((long long *)(*((long long *)&v29->padding_0[8]) + 128));
                                                        ptr13 = ptr;
                                                        ptr13->field_a8 = v30;
                                                        v32 = &ptr13->field_a8;
                                                        sub_f7d8d0(v32, v30);
                                                        if (*((long long *)&v32->padding_0[16]))
                                                        {
                                                            v33 = *((long long *)(*((long long *)&v32->padding_0[16]) + 136));
                                                            ptr14 = ptr;
                                                            ptr14->field_b0 = v33;
                                                            sub_f7d8d0(&ptr14->field_b0, v33);
                                                            if (Camera__get_main(0))
                                                            {
                                                                v35 = sub_1231bc8();
                                                                ptr15 = ptr;
                                                                ptr15->field_b8 = v35;
                                                                v37 = &ptr15->field_b8;
                                                                sub_f7d8d0(v37, v35);
                                                                if (*((long long *)&v37->padding_0[32]))
                                                                {
                                                                    v38 = *((long long *)(*((long long *)&v37->padding_0[32]) + 144));
                                                                    ptr16 = ptr;
                                                                    ptr16->field_c0 = v38;
                                                                    v40 = &ptr16->field_c0;
                                                                    sub_f7d8d0(v40, v38);
                                                                    if (*((long long *)&v40->padding_0[48]))
                                                                    {
                                                                        v41 = *((long long *)(*((long long *)&v40->padding_0[48]) + 40));
                                                                        ptr17 = ptr;
                                                                        ptr17->field_c8 = v41;
                                                                        v43 = &ptr17->field_c8;
                                                                        sub_f7d8d0(v43, v41);
                                                                        if (*((long long *)&v43->padding_0[16]))
                                                                        {
                                                                            v44 = *((long long *)(*((long long *)&v43->padding_0[16]) + 168));
                                                                            ptr18 = ptr;
                                                                            ptr18->field_d0 = v44;
                                                                            v46 = &ptr18->field_d0;
                                                                            sub_f7d8d0(v46, v44);
                                                                            if (*((long long *)&v46->padding_0[16]) && GameObject__get_transform(*((long long *)&v46->padding_0[16]), 0))
                                                                            {
                                                                                Transform__get_localPosition();
                                                                                v47 = ptr->field_e0;
                                                                                ptr->field_f8 = v48;
                                                                                ptr->field_fc = v49;
                                                                                ptr->field_100 = v50;
                                                                                if (v47 && GameObject__get_transform(v47, 0))
                                                                                {
                                                                                    Transform__get_localScale();
                                                                                    v51 = ptr->field_98;
                                                                                    ptr->field_e8 = v48;
                                                                                    ptr->field_ec = v49;
                                                                                    ptr->field_f0 = v50;
                                                                                    if (v51 && v51->field_110)
                                                                                    {
                                                                                        v52 = sub_1249224(v51->field_110, g_1efeb20);
                                                                                        ptr19 = ptr;
                                                                                        ptr19->field_60 = v52;
                                                                                        v54 = &ptr19->field_60;
                                                                                        sub_f7d8d0(v54, v52);
                                                                                        if (*((long long *)&v54->padding_0[56]) && *((long long *)(*((long long *)&v54->padding_0[56]) + 280)))
                                                                                        {
                                                                                            v55 = sub_1249224(*((long long *)(*((long long *)&v54->padding_0[56]) + 280)), g_1efeb20);
                                                                                            ptr20 = ptr;
                                                                                            ptr20->field_68 = v55;
                                                                                            v57 = &ptr20->field_68;
                                                                                            sub_f7d8d0(v57, v55);
                                                                                            if (*((long long *)&v57->padding_0[32]))
                                                                                            {
                                                                                                v58 = sub_1249b80(*((long long *)&v57->padding_0[32]), g_1efed90);
                                                                                                *((struct_18 **)&ptr->padding_5b0[192]) = v58;
                                                                                                v59 = sub_f7d8d0(&ptr->padding_5b0[192], v58);
                                                                                                ptr23 = *((long long *)&ptr->padding_5b0[192]);
                                                                                                if (ptr23)
                                                                                                {
                                                                                                    if (ptr23->field_18 > 1)
                                                                                                    {
                                                                                                        v61 = ptr23->field_28;
                                                                                                        ptr->field_680 = v61;
                                                                                                        v59 = sub_f7d8d0(&ptr->field_680, v61);
                                                                                                        ptr24 = *((long long *)&ptr->padding_5b0[192]);
                                                                                                        if (ptr24)
                                                                                                        {
                                                                                                            if (ptr24->field_18)
                                                                                                            {
                                                                                                                v63 = ptr24->field_20;
                                                                                                                *((unsigned long *)&ptr->padding_5b0[200]) = v63;
                                                                                                                sub_f7d8d0(&ptr->padding_5b0[200], v63);
                                                                                                                if (*((long long *)&ptr->padding_5b0[200]))
                                                                                                                {
                                                                                                                    v59 = AudioSource__set_clip(*((long long *)&ptr->padding_5b0[200]), ptr->field_688, 0);
                                                                                                                    ptr25 = *((long long *)&ptr->padding_5b0[192]);
                                                                                                                    if (ptr25)
                                                                                                                    {
                                                                                                                        if (ptr25->field_18)
                                                                                                                        {
                                                                                                                            v65 = ptr25->field_20;
                                                                                                                            *((unsigned long *)&ptr->padding_6a0[80]) = v65;
                                                                                                                            v59 = sub_f7d8d0(&ptr->padding_6a0[80], v65);
                                                                                                                            ptr26 = *((long long *)&ptr->padding_5b0[192]);
                                                                                                                            if (ptr26)
                                                                                                                            {
                                                                                                                                if (ptr26->field_18 > 2)
                                                                                                                                {
                                                                                                                                    v67 = ptr26->field_30;
                                                                                                                                    *((unsigned long *)&ptr->padding_6a0[88]) = v67;
                                                                                                                                    sub_f7d8d0(&ptr->padding_6a0[88], v67);
                                                                                                                                    ptr4 = ptr->field_88;
                                                                                                                                    if (ptr4)
                                                                                                                                    {
                                                                                                                                        v69 = (int)*((int128_t *)&(&ptr4->field_160)[1]);
                                                                                                                                        *((void*)&ptr->padding_578[0]) = v69;
                                                                                                                                        v70 = ptr4->field_160;
                                                                                                                                        *((unsigned long *)&ptr->padding_538[0]) = v70;
                                                                                                                                        sub_f7d8d0(&ptr->padding_538, v70);
                                                                                                                                        if (ptr->field_e0)
                                                                                                                                        {
                                                                                                                                            v71 = sub_1249e48(ptr->field_e0, g_1efeda8);
                                                                                                                                            ptr3 = &ptr->field_558;
                                                                                                                                            ptr->field_558 = v71;
                                                                                                                                            v59 = sub_f7d8d0(ptr3, v71);
                                                                                                                                            ptr27 = ptr->field_558;
                                                                                                                                            if (ptr27)
                                                                                                                                            {
                                                                                                                                                v74 = 0;
                                                                                                                                                addr = &ptr->field_560;
                                                                                                                                                while (true)
                                                                                                                                                {
                                                                                                                                                    v76 = ptr27->field_18;
                                                                                                                                                    if ((v76 & 4294967295) > v74)
                                                                                                                                                    {
                                                                                                                                                        if (v76 <= v74)
                                                                                                                                                            sub_f7db7c(v59);
                                                                                                                                                        if (!g_1ef0c58->field_e0)
                                                                                                                                                            sub_f7da5c(g_1ef0c58);
                                                                                                                                                        v59 = Object__op_Inequality(*((long long *)&ptr27[1].padding_0[4 + 8 * v74]), *((long long *)&ptr->padding_548[8]), 0);
                                                                                                                                                        if (((char)v59 & 1))
                                                                                                                                                        {
                                                                                                                                                            v77 = *((long long *)&ptr3->padding_0[0]);
                                                                                                                                                            if (!v77)
                                                                                                                                                                sub_f7db7c(sub_f7db74());
                                                                                                                                                            if (v77->field_18 <= v74)
                                                                                                                                                                sub_f7db7c(v59);
                                                                                                                                                            v78 = &v77->padding_0[8 * v74];
                                                                                                                                                            if (!v78->field_20)
                                                                                                                                                                sub_f7db7c(sub_f7db74());
                                                                                                                                                            v79 = Renderer__get_materials(v78->field_20, 0);
                                                                                                                                                            *((struct_20 **)&addr->padding_0[0]) = v79;
                                                                                                                                                            v59 = sub_f7d8d0(addr, v79);
                                                                                                                                                            ptr28 = *((long long *)&addr->padding_0[0]);
                                                                                                                                                            if (!ptr28)
                                                                                                                                                                sub_f7db7c(sub_f7db74());
                                                                                                                                                            v81 = 0;
                                                                                                                                                            do
                                                                                                                                                            {
                                                                                                                                                                v82 = ptr28->field_18;
                                                                                                                                                                if ((v82 & 4294967295) <= v81)
                                                                                                                                                                    goto LABEL_10b5e58;
                                                                                                                                                                if (v82 <= v81)
                                                                                                                                                                    sub_f7db7c(v59);
                                                                                                                                                                p = ptr->field_568;
                                                                                                                                                                if (!p)
                                                                                                                                                                    sub_f7db7c(sub_f7db74());
                                                                                                                                                                v84 = *((long long *)&ptr28[1].padding_0[4 + 8 * v81]);
                                                                                                                                                                v85 = p->field_10;
                                                                                                                                                                p->field_1c = p->field_1c + 1;
                                                                                                                                                                if (!v85)
                                                                                                                                                                    sub_f7db7c(sub_f7db74());
                                                                                                                                                                v86 = p->field_18;
                                                                                                                                                                if (*((int *)(v85 + 24)) > (unsigned int)v86)
                                                                                                                                                                {
                                                                                                                                                                    ptr29 = v85 + v86 * 8;
                                                                                                                                                                    p->field_18 = (unsigned int)v86 + 1;
                                                                                                                                                                    ptr29->field_20 = v84;
                                                                                                                                                                    v59 = sub_f7d8d0(&ptr29->field_20);
                                                                                                                                                                }
                                                                                                                                                                else
                                                                                                                                                                {
                                                                                                                                                                    v59 = sub_14a3390();
                                                                                                                                                                }
                                                                                                                                                                ptr28 = *((long long *)&addr->padding_0[0]);
                                                                                                                                                                v81 += 1;
                                                                                                                                                            } while (ptr28);
                                                                                                                                                        }
LABEL_10b5e58:
                                                                                                                                                        ptr27 = *((long long *)&ptr3->padding_0[0]);
                                                                                                                                                        v74 += 1;
                                                                                                                                                        if (!ptr27)
                                                                                                                                                            sub_f7db7c(sub_f7db74());
                                                                                                                                                    }
                                                                                                                                                    else if (*((long long *)&v8->padding_0[0]))
                                                                                                                                                    {
                                                                                                                                                        v88 = sub_1249224(*((long long *)&v8->padding_0[0]), g_1efeb88);
                                                                                                                                                        *((long long *)&ptr->padding_4e8[64]) = v88;
                                                                                                                                                        sub_f7d8d0(&ptr->padding_4e8[64], v88);
                                                                                                                                                        if (!g_1ef0c58->field_e0)
                                                                                                                                                            sub_f7da5c(g_1ef0c58);
                                                                                                                                                        if (!((char)Object__op_Implicit(*((long long *)&ptr->padding_3e0[8]), 0) & 1))
                                                                                                                                                        {
                                                                                                                                                            if (!g_1ef0c58->field_e0)
                                                                                                                                                                sub_f7da5c(g_1ef0c58);
                                                                                                                                                            if (((char)Object__op_Implicit(*((long long *)&ptr->padding_414[44]), 0) & 1))
                                                                                                                                                            {
                                                                                                                                                                if (*((long long *)&ptr->padding_414[44]))
                                                                                                                                                                {
                                                                                                                                                                    Transform__get_position(*((long long *)&ptr->padding_414[44]), 0);
                                                                                                                                                                    v89 = *((long long *)&ptr->padding_414[44]);
                                                                                                                                                                    *((unsigned int *)&ptr->field_3f0) = *((unsigned int *)&v69);
                                                                                                                                                                    *((unsigned int *)((char *)&ptr->field_3f0 + 4)) = v49;
                                                                                                                                                                    ptr->field_3f8 = v50;
                                                                                                                                                                    if (!v89)
                                                                                                                                                                        sub_f7db7c(sub_f7db74());
                                                                                                                                                                    Transform__get_forward(v89, 0);
                                                                                                                                                                    v90 = *((int *)&ptr->padding_404[4]);
                                                                                                                                                                    v91 = *((long long *)&ptr->padding_414[44]);
                                                                                                                                                                    *((unsigned int *)&ptr->field_3f0) = *((unsigned int *)&v69) + *((unsigned int *)&v69) * v90;
                                                                                                                                                                    *((unsigned int *)((char *)&ptr->field_3f0 + 4)) = v49 + v49 * v90;
                                                                                                                                                                    ptr->field_3f8 = v50 + v50 * v90;
                                                                                                                                                                    if (!g_1fab2c9)
                                                                                                                                                                    {
                                                                                                                                                                        sub_f7d92c(&g_1ef22e8);
                                                                                                                                                                        g_1fab2c9 = 1;
                                                                                                                                                                    }
                                                                                                                                                                    if (!v91)
                                                                                                                                                                        sub_f7db7c(sub_f7db74());
                                                                                                                                                                    v92 = g_1ef22e8->field_b8->field_4;
                                                                                                                                                                    v93 = g_1ef22e8->field_b8->field_8;
                                                                                                                                                                    Transform__set_localEulerAngles(v91, 0);
                                                                                                                                                                }
                                                                                                                                                                else
                                                                                                                                                                {
                                                                                                                                                                    sub_f7db7c(sub_f7db74());
                                                                                                                                                                }
                                                                                                                                                            }
                                                                                                                                                        }
                                                                                                                                                        else if (*((long long *)&ptr->padding_3e0[8]))
                                                                                                                                                        {
                                                                                                                                                            Transform__get_position(*((long long *)&ptr->padding_3e0[8]), 0);
                                                                                                                                                            *((unsigned int *)&ptr->field_3f0) = *((unsigned int *)&v69);
                                                                                                                                                            *((unsigned int *)((char *)&ptr->field_3f0 + 4)) = v49;
                                                                                                                                                            ptr->field_3f8 = v50;
                                                                                                                                                        }
                                                                                                                                                        else
                                                                                                                                                        {
                                                                                                                                                            sub_f7db7c(sub_f7db74());
                                                                                                                                                        }
                                                                                                                                                        if (!g_1ef0c58->field_e0)
                                                                                                                                                            sub_f7da5c(g_1ef0c58);
                                                                                                                                                        if (((char)Object__op_Implicit(*((long long *)&ptr->padding_414[44]), 0) & 1))
                                                                                                                                                        {
                                                                                                                                                            if (*((long long *)&ptr->padding_414[44]))
                                                                                                                                                            {
                                                                                                                                                                v94 = sub_1231bc8(*((long long *)&ptr->padding_414[44]), g_1efd070);
                                                                                                                                                                *((long long *)&ptr->padding_470[0]) = v94;
                                                                                                                                                                sub_f7d8d0(&ptr->padding_470, v94);
                                                                                                                                                                if (!g_1ef0c58->field_e0)
                                                                                                                                                                    sub_f7da5c(g_1ef0c58);
                                                                                                                                                                if (((char)Object__op_Implicit(*((long long *)&ptr->field_460), 0) & 1))
                                                                                                                                                                {
                                                                                                                                                                    if (*((long long *)&ptr->field_460))
                                                                                                                                                                    {
                                                                                                                                                                        v95 = sub_1249224(*((long long *)&ptr->field_460), g_1efec30);
                                                                                                                                                                        *((long long *)&ptr->padding_488[0]) = v95;
                                                                                                                                                                        sub_f7d8d0(&ptr->padding_488, v95);
                                                                                                                                                                    }
                                                                                                                                                                    else
                                                                                                                                                                    {
                                                                                                                                                                        sub_f7db7c(sub_f7db74());
                                                                                                                                                                    }
                                                                                                                                                                }
                                                                                                                                                            }
                                                                                                                                                            else
                                                                                                                                                            {
                                                                                                                                                                sub_f7db7c(sub_f7db74());
                                                                                                                                                            }
                                                                                                                                                        }
                                                                                                                                                        if (!g_1ef0c58->field_e0)
                                                                                                                                                            sub_f7da5c(g_1ef0c58);
                                                                                                                                                        v96 = Object__op_Implicit(*((long long *)&ptr->padding_4a0[56]), 0);
                                                                                                                                                        if (((char)v96 & 1))
                                                                                                                                                        {
                                                                                                                                                            if (*((long long *)&ptr->padding_4a0[56]))
                                                                                                                                                            {
                                                                                                                                                                v97 = sub_1231bc8(*((long long *)&ptr->padding_4a0[56]), g_1efd070);
                                                                                                                                                                ptr->field_490 = v97;
                                                                                                                                                                v96 = sub_f7d8d0(&ptr->field_490, v97);
                                                                                                                                                            }
                                                                                                                                                            else
                                                                                                                                                            {
                                                                                                                                                                sub_f7db7c(sub_f7db74());
                                                                                                                                                            }
                                                                                                                                                        }
                                                                                                                                                        if (ptr->field_1f5)
                                                                                                                                                            return v96;
                                                                                                                                                        v98 = ptr->field_204;
                                                                                                                                                        v99 = (((CmpF(v98, 0.0) >> 5 & 3 | CmpF(v98, 0.0) & 1) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - ((CmpF(v98, 0.0) >> 5 & 3 | CmpF(v98, 0.0) & 1) & (CmpF(v98, 0.0) >> 5 & 3 | CmpF(v98, 0.0) & 1) >> 1 & 1);
                                                                                                                                                        if ((char)(v99 * 0x10000000 >> 30))
                                                                                                                                                        {
                                                                                                                                                            if (!g_1ef0c58->field_e0)
                                                                                                                                                                sub_f7da5c(g_1ef0c58);
                                                                                                                                                            if (((char)Object__op_Implicit(*((long long *)&ptr->padding_414[44]), 0) & 1))
                                                                                                                                                            {
                                                                                                                                                                if (ptr->padding_470)
                                                                                                                                                                {
                                                                                                                                                                    Renderer__set_enabled(ptr->padding_470, 0, 0);
                                                                                                                                                                    if (!ptr->padding_470)
                                                                                                                                                                    {
                                                                                                                                                                        sub_f7db7c(sub_f7db74());
                                                                                                                                                                    }
                                                                                                                                                                    else if (Renderer__get_material(ptr->padding_470, 0))
                                                                                                                                                                    {
                                                                                                                                                                        Material__GetColor();
                                                                                                                                                                        *((unsigned int *)((char *)&ptr->field_448 + 4)) = v98;
                                                                                                                                                                        ptr->field_450 = v92;
                                                                                                                                                                        ptr->field_454 = v93;
                                                                                                                                                                        ptr->field_458 = v90;
                                                                                                                                                                        if (!g_1ef0c58->field_e0)
                                                                                                                                                                            sub_f7da5c(g_1ef0c58);
                                                                                                                                                                        if (((char)Object__op_Implicit(ptr->field_478, 0) & 1))
                                                                                                                                                                        {
                                                                                                                                                                            if (ptr->field_478)
                                                                                                                                                                                Renderer__set_enabled(ptr->field_478, 0, 0);
                                                                                                                                                                            else
                                                                                                                                                                                sub_f7db7c(sub_f7db74());
                                                                                                                                                                        }
                                                                                                                                                                        if (!g_1ef0c58->field_e0)
                                                                                                                                                                            sub_f7da5c(g_1ef0c58);
                                                                                                                                                                        if (((char)Object__op_Implicit(*((long long *)&ptr->field_460), 0) & 1))
                                                                                                                                                                        {
                                                                                                                                                                            if (ptr->padding_488)
                                                                                                                                                                                Behaviour__set_enabled(ptr->padding_488, 0, 0);
                                                                                                                                                                            else
                                                                                                                                                                                sub_f7db7c(sub_f7db74());
                                                                                                                                                                        }
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
                                                                                                                                                            if (ptr->padding_130 < ptr->field_12c)
                                                                                                                                                            {
                                                                                                                                                                v101 = (int)ptr->padding_130;
                                                                                                                                                            }
                                                                                                                                                            else
                                                                                                                                                            {
                                                                                                                                                                v102 = ptr->field_12c;
                                                                                                                                                                v101 = v102;
                                                                                                                                                            }
                                                                                                                                                            if (v102 < 0)
                                                                                                                                                                v104 = 0;
                                                                                                                                                            else
                                                                                                                                                                v104 = v101;
                                                                                                                                                        }
                                                                                                                                                        else
                                                                                                                                                        {
                                                                                                                                                            v104 = (int)ptr->padding_130;
                                                                                                                                                        }
                                                                                                                                                        ptr->field_12c = v104;
                                                                                                                                                        v105 = 0x40600000;
                                                                                                                                                        if (!ptr->field_1de)
                                                                                                                                                            v105 = 0x40d00000;
                                                                                                                                                        if (1 < ptr->field_154)
                                                                                                                                                            v105 = 0x40000000;
                                                                                                                                                        *((unsigned int *)&ptr->field_448) = v105;
                                                                                                                                                        v106 = LayerMask__op_Implicit(LayerMask__op_Implicit() & 4294705151, 0);
                                                                                                                                                        v107 = *((int *)&ptr->padding_590[8]);
                                                                                                                                                        ptr->field_37c = v106;
                                                                                                                                                        idx29 = &(&ptr->padding_380)[1];
                                                                                                                                                        ptr->field_1fc = 0xbf800000;
                                                                                                                                                        *((unsigned int *)&ptr->padding_590[12]) = v107;
                                                                                                                                                        v109 = ptr->field_e0;
                                                                                                                                                        *((long long *)&ptr->field_394) = *((long long *)&idx29->padding_0[0]);
                                                                                                                                                        *((int *)&ptr->field_398) = *((int *)&idx29->padding_0[8]);
                                                                                                                                                        if (v109 && GameObject__get_transform(v109, 0) && (Transform__get_localEulerAngles(), v110 = ptr->field_70, ptr->field_350 = v93, v110))
                                                                                                                                                        {
                                                                                                                                                            v111 = Transform__set_localEulerAngles(v110, 0);
                                                                                                                                                            v113 = ptr->field_134;
                                                                                                                                                            v114 = (int)ptr->padding_130;
                                                                                                                                                            if (*((int *)&ptr->padding_138[0]) < ptr->field_128)
                                                                                                                                                            {
                                                                                                                                                                v115 = *((int *)&ptr->padding_138[0]);
                                                                                                                                                            }
                                                                                                                                                            else
                                                                                                                                                            {
                                                                                                                                                                v116 = ptr->field_128;
                                                                                                                                                                v115 = v116;
                                                                                                                                                            }
                                                                                                                                                            if (v116 < 0)
                                                                                                                                                                v117 = 0;
                                                                                                                                                            if (ptr->padding_130 >= v113)
                                                                                                                                                                v114 = v113;
                                                                                                                                                            if (v113 < 0)
                                                                                                                                                                v118 = 0;
                                                                                                                                                            else
                                                                                                                                                                v118 = v114;
                                                                                                                                                            if (ptr->field_344)
                                                                                                                                                                v119 = 0;
                                                                                                                                                            else
                                                                                                                                                                v119 = 1;
                                                                                                                                                            v120 = g_832198[v119];
                                                                                                                                                            ptr->field_1f2 = ptr->field_1f1;
                                                                                                                                                            ptr->field_128 = v117;
                                                                                                                                                            ptr->field_134 = v118;
                                                                                                                                                            *((unsigned int *)&ptr->padding_3a4[48]) = v120;
                                                                                                                                                            return v111;
                                                                                                                                                        }
                                                                                                                                                        break;
                                                                                                                                                    }
                                                                                                                                                }
                                                                                                                                            }
                                                                                                                                        }
                                                                                                                                    }
                                                                                                                                }
                                                                                                                                else
                                                                                                                                {
                                                                                                                                    sub_f7db7c(v59);
                                                                                                                                }
                                                                                                                            }
                                                                                                                        }
                                                                                                                        else
                                                                                                                        {
                                                                                                                            sub_f7db7c(v59);
                                                                                                                        }
                                                                                                                    }
                                                                                                                }
                                                                                                            }
                                                                                                            else
                                                                                                            {
                                                                                                                sub_f7db7c(v59);
                                                                                                            }
                                                                                                        }
                                                                                                    }
                                                                                                    else
                                                                                                    {
                                                                                                        sub_f7db7c(v59);
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
    sub_f7db7c(sub_f7db74());
}
```


## `WeaponBehavior.LateUpdate` — RVA `0xcb62c4`

- Decompiled symbol: `WeaponBehavior_LateUpdate`
- Metadata signature: `private void LateUpdate() { }`
- Native interval: `1456` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: Decompiler produced no C-like text

```c
// 0x10b62c4: sub sp, sp, #0x70
// 0x10b62c8: stp d15, d14, [sp, #0x10]
// 0x10b62cc: stp d13, d12, [sp, #0x20]
// 0x10b62d0: stp d11, d10, [sp, #0x30]
// 0x10b62d4: stp d9, d8, [sp, #0x40]
// 0x10b62d8: stp x30, x21, [sp, #0x50]
// 0x10b62dc: stp x20, x19, [sp, #0x60]
// 0x10b62e0: adrp x20, #0x1fab000
// 0x10b62e4: ldrb w8, [x20, #0x4e2]
// 0x10b62e8: mov x19, x0
// 0x10b62ec: tbnz w8, #0, #0x10b6304
// 0x10b62f0: adrp x0, #0x1e8c000
// 0x10b62f4: ldr x0, [x0, #0xd8]
// 0x10b62f8: bl #0xf7d92c
// 0x10b62fc: mov w8, #1
// 0x10b6300: strb w8, [x20, #0x4e2]
// 0x10b6304: mov x0, xzr
// 0x10b6308: bl #0x1b9ae58
// 0x10b630c: fcmp s0, #0.0
// 0x10b6310: b.le #0x10b6850
// 0x10b6314: mov x0, xzr
// 0x10b6318: bl #0x1b89b60
// 0x10b631c: fcmp s0, #0.0
// 0x10b6320: b.le #0x10b6850
// 0x10b6324: mov x0, xzr
// 0x10b6328: bl #0x1b9ae30
// 0x10b632c: fcmp s0, #0.0
// 0x10b6330: b.le #0x10b6850
// 0x10b6334: ldr s8, [x19, #0x1fc]
// 0x10b6338: ldr s9, [x19, #0x150]
// 0x10b633c: mov x0, xzr
// 0x10b6340: bl #0x1b9ad30
// 0x10b6344: fadd s1, s8, s9
// 0x10b6348: fmov s9, wzr
// 0x10b634c: fcmp s1, s0
// 0x10b6350: fmov s10, wzr
// 0x10b6354: b.pl #0x10b6394
// 0x10b6358: ldrb w9, [x19, #0x239]
// 0x10b635c: ldr x8, [x19, #0x98]
// 0x10b6360: cbz w9, #0x10b6380
// 0x10b6364: cbz x8, #0x10b6870
// 0x10b6368: ldrb w9, [x8, #0x2d0]
// 0x10b636c: cbz w9, #0x10b6384
// 0x10b6370: ldrb w8, [x8, #0x460]
// 0x10b6374: cbnz w8, #0x10b6390
// 0x10b6378: ldr s10, [x19, #0x278]
// 0x10b637c: b #0x10b6394
// 0x10b6380: cbz x8, #0x10b6870
// 0x10b6384: ldrb w8, [x8, #0x460]
// 0x10b6388: fmov s10, wzr
// 0x10b638c: cbz w8, #0x10b6394
// 0x10b6390: ldr s10, [x19, #0x288]
// 0x10b6394: ldr s8, [x19, #0x294]
// 0x10b6398: mov x0, xzr
// 0x10b639c: str s10, [x19, #0x28c]
// 0x10b63a0: add x20, x19, #0x290
// 0x10b63a4: bl #0x1b9ae30
// 0x10b63a8: mov w8, #0x43b40000
// 0x10b63ac: mov v4.16b, v0.16b
// 0x10b63b0: fmov s0, w8
// 0x10b63b4: fsub s1, s10, s8
// 0x10b63b8: mov w8, #-0x3c4c0000
// 0x10b63bc: fdiv s3, s1, s0
// 0x10b63c0: fmov s2, w8
// 0x10b63c4: frintm s3, s3
// 0x10b63c8: fmul s3, s3, s2
// 0x10b63cc: fadd s1, s1, s3
// 0x10b63d0: mov w8, #0x43340000
// 0x10b63d4: fmin s0, s1, s0
// 0x10b63d8: fcmp s1, #0.0
// 0x10b63dc: fmov s3, w8
// 0x10b63e0: fcsel s0, s0, s9, pl
// 0x10b63e4: adrp x8, #0x832000
// 0x10b63e8: fadd s1, s0, s2
// 0x10b63ec: ldr s2, [x8, #0x3b8]
// 0x10b63f0: fcmp s0, s3
// 0x10b63f4: fcsel s0, s1, s0, gt
// 0x10b63f8: mov w8, #0x7f800000
// 0x10b63fc: fadd s1, s8, s0
// 0x10b6400: fmov s3, w8
// 0x10b6404: mov v0.16b, v8.16b
// 0x10b6408: mov x0, x20
// 0x10b640c: mov x1, xzr
// 0x10b6410: bl #0x1b8c860
// 0x10b6414: ldr x8, [x19, #0x80]
// 0x10b6418: str s0, [x19, #0x294]
// 0x10b641c: cbz x8, #0x10b6870
// 0x10b6420: ldr s8, [x19, #0x298]
// 0x10b6424: ldr s9, [x8, #0xc0]
// 0x10b6428: mov x0, xzr
// 0x10b642c: bl #0x1b9ae30
// 0x10b6430: fmov s1, #7.00000000
// 0x10b6434: fmov s2, #1.00000000
// 0x10b6438: fmul s0, s0, s1
// 0x10b643c: fmov s3, wzr
// 0x10b6440: ldr x8, [x19, #0x90]
// 0x10b6444: fmin s1, s0, s2
// 0x10b6448: fcmp s0, #0.0
// 0x10b644c: fcsel s0, s1, s3, pl
// 0x10b6450: fsub s1, s9, s8
// 0x10b6454: fmul s0, s1, s0
// 0x10b6458: fadd s0, s8, s0
// 0x10b645c: str s0, [x19, #0x298]
// 0x10b6460: cbz x8, #0x10b6870
// 0x10b6464: ldr x9, [x19, #0xc0]
// 0x10b6468: cbz x9, #0x10b6870
// 0x10b646c: ldr x10, [x19, #0xc8]
// 0x10b6470: cbz x10, #0x10b6870
// 0x10b6474: ldr s1, [x19, #0x350]
// 0x10b6478: ldr s2, [x19, #0x294]
// 0x10b647c: ldr s3, [x8, #0x250]
// 0x10b6480: ldr s4, [x19, #0x354]
// 0x10b6484: ldr s5, [x19, #0x358]
// 0x10b6488: ldr s6, [x9, #0xbc]
// 0x10b648c: ldr s7, [x10, #0x4c]
// 0x10b6490: ldr s16, [x8, #0x1e0]
// 0x10b6494: fadd s1, s1, s2
// 0x10b6498: fmul s2, s3, s4
// 0x10b649c: ldr x0, [x19, #0xe0]
// 0x10b64a0: fadd s1, s1, s2
// 0x10b64a4: fmul s0, s0, s5
// 0x10b64a8: fadd s1, s1, s6
// 0x10b64ac: fsub s0, s1, s0
// 0x10b64b0: fmul s1, s7, s16
// 0x10b64b4: fsub s0, s0, s1
// 0x10b64b8: str s0, [x19, #0x348]
// 0x10b64bc: cbz x0, #0x10b6870
// 0x10b64c0: mov x1, xzr
// 0x10b64c4: bl #0x1b94c14
// 0x10b64c8: cbz x0, #0x10b6870
// 0x10b64cc: mov x1, xzr
// 0x10b64d0: bl #0x1b9d7c8
// 0x10b64d4: ldr s0, [x19, #0x348]
// 0x10b64d8: mov w8, #0x43b40000
// 0x10b64dc: fmov s1, w8
// 0x10b64e0: mov w9, #-0x3c4c0000
// 0x10b64e4: fsub s0, s0, s2
// 0x10b64e8: fdiv s2, s0, s1
// 0x10b64ec: fmov s3, w9
// 0x10b64f0: frintm s2, s2
// 0x10b64f4: fmul s2, s2, s3
// 0x10b64f8: fadd s0, s0, s2
// 0x10b64fc: mov w8, #0x43340000
// 0x10b6500: fmov s2, wzr
// 0x10b6504: fmin s1, s0, s1
// 0x10b6508: fcmp s0, #0.0
// 0x10b650c: fmov s0, w8
// 0x10b6510: ldr x8, [x19, #0x98]
// 0x10b6514: fcsel s1, s1, s2, pl
// 0x10b6518: fadd s2, s1, s3
// 0x10b651c: fcmp s1, s0
// 0x10b6520: fcsel s0, s2, s1, gt
// 0x10b6524: str s0, [x19, #0x34c]
// 0x10b6528: cbz x8, #0x10b6870
// 0x10b652c: ldrb w8, [x8, #0x2d0]
// 0x10b6530: cbz w8, #0x10b653c
// 0x10b6534: ldrb w8, [x19, #0x239]
// 0x10b6538: cbz w8, #0x10b65a4
// 0x10b653c: ldr x8, [x19, #0xa0]
// 0x10b6540: cbz x8, #0x10b6870
// 0x10b6544: ldr x0, [x8, #0x38]
// 0x10b6548: cbz x0, #0x10b6870
// 0x10b654c: mov w1, #1
// 0x10b6550: mov x2, xzr
// 0x10b6554: bl #0x1b94cd0
// 0x10b6558: ldr x8, [x19, #0xa0]
// 0x10b655c: cbz x8, #0x10b6870
// 0x10b6560: ldr x0, [x8, #0x40]
// 0x10b6564: cbz x0, #0x10b6870
// 0x10b6568: mov w1, #1
// 0x10b656c: mov x2, xzr
// 0x10b6570: bl #0x1b94cd0
// 0x10b6574: ldr x8, [x19, #0xa0]
// 0x10b6578: cbz x8, #0x10b6870
// 0x10b657c: ldr x0, [x8, #0x48]
// 0x10b6580: cbz x0, #0x10b6870
// 0x10b6584: mov w1, wzr
// 0x10b6588: mov x2, xzr
// 0x10b658c: bl #0x1b94cd0
// 0x10b6590: ldr x8, [x19, #0xa0]
// 0x10b6594: cbz x8, #0x10b6870
// 0x10b6598: ldr x0, [x8, #0x50]
// 0x10b659c: cbnz x0, #0x10b6740
// 0x10b65a0: b #0x10b6870
// 0x10b65a4: ldr x0, [x19, #0xe0]
// 0x10b65a8: cbz x0, #0x10b6870
// 0x10b65ac: mov x1, xzr
// 0x10b65b0: bl #0x1b94c14
// 0x10b65b4: ldr x8, [x19, #0xe0]
// 0x10b65b8: cbz x8, #0x10b6870
// 0x10b65bc: mov x20, x0
// 0x10b65c0: mov x0, x8
// 0x10b65c4: mov x1, xzr
// 0x10b65c8: bl #0x1b94c14
// 0x10b65cc: cbz x0, #0x10b6870
// 0x10b65d0: mov x1, xzr
// 0x10b65d4: bl #0x1b9cb18
// 0x10b65d8: ldp s10, s12, [x19, #0xf8]
// 0x10b65dc: ldr s13, [x19, #0x100]
// 0x10b65e0: mov x0, xzr
// 0x10b65e4: mov v8.16b, v0.16b
// 0x10b65e8: mov v11.16b, v1.16b
// 0x10b65ec: mov v15.16b, v2.16b
// 0x10b65f0: bl #0x1b9ae30
// 0x10b65f4: adrp x21, #0x1fab000
// 0x10b65f8: ldrb w8, [x21, #0x4d2]
// 0x10b65fc: mov v14.16b, v0.16b
// 0x10b6600: cbnz w8, #0x10b6618
// 0x10b6604: adrp x0, #0x1e8c000
// 0x10b6608: ldr x0, [x0, #0xa60]
// 0x10b660c: bl #0xf7d92c
// 0x10b6610: mov w8, #1
// 0x10b6614: strb w8, [x21, #0x4d2]
// 0x10b6618: fsub s9, s10, s8
// 0x10b661c: mov v2.16b, v8.16b
// 0x10b6620: fsub s8, s12, s11
// 0x10b6624: mov v4.16b, v15.16b
// 0x10b6628: fsub s15, s13, s15
// 0x10b662c: fmul s0, s9, s9
// 0x10b6630: fmul s1, s8, s8
// 0x10b6634: fadd s0, s0, s1
// 0x10b6638: fmul s1, s15, s15
// 0x10b663c: mov v3.16b, v11.16b
// 0x10b6640: fadd s11, s1, s0
// 0x10b6644: fcmp s11, #0.0
// 0x10b6648: b.eq #0x10b66c0
// 0x10b664c: adrp x8, #0x832000
// 0x10b6650: ldr s0, [x8, #0x458]
// 0x10b6654: stp s4, s3, [sp, #4]
// 0x10b6658: str s2, [sp, #0xc]
// 0x10b665c: fmul s14, s14, s0
// 0x10b6660: fcmp s14, #0.0
// 0x10b6664: b.lt #0x10b6674
// 0x10b6668: fmul s0, s14, s14
// 0x10b666c: fcmp s11, s0
// 0x10b6670: b.ls #0x10b66c0
// 0x10b6674: adrp x8, #0x1e8c000
// 0x10b6678: ldr x8, [x8, #0xa60]
// 0x10b667c: ldr x0, [x8]
// 0x10b6680: ldr w8, [x0, #0xe0]
// 0x10b6684: cbnz w8, #0x10b668c
// 0x10b6688: bl #0xf7da5c
// 0x10b668c: ldr s3, [sp, #0xc]
// 0x10b6690: fsqrt s0, s11
// 0x10b6694: fdiv s1, s9, s0
// 0x10b6698: fmul s1, s14, s1
// 0x10b669c: fadd s10, s3, s1
// 0x10b66a0: ldr s1, [sp, #8]
// 0x10b66a4: fdiv s2, s8, s0
// 0x10b66a8: fmul s2, s14, s2
// 0x10b66ac: fdiv s0, s15, s0
// 0x10b66b0: fadd s12, s1, s2
// 0x10b66b4: ldr s1, [sp, #4]
// 0x10b66b8: fmul s0, s14, s0
// 0x10b66bc: fadd s13, s1, s0
// 0x10b66c0: cbz x20, #0x10b6870
// 0x10b66c4: mov x0, x20
// 0x10b66c8: mov v0.16b, v10.16b
// 0x10b66cc: mov v1.16b, v12.16b
// 0x10b66d0: mov v2.16b, v13.16b
// 0x10b66d4: mov x1, xzr
// 0x10b66d8: bl #0x1b9cba4
// 0x10b66dc: ldr x8, [x19, #0xa0]
// 0x10b66e0: cbz x8, #0x10b6870
// 0x10b66e4: ldr x0, [x8, #0x48]
// 0x10b66e8: cbz x0, #0x10b6870
// 0x10b66ec: mov w1, #1
// 0x10b66f0: mov x2, xzr
// 0x10b66f4: bl #0x1b94cd0
// 0x10b66f8: ldr x8, [x19, #0xa0]
// 0x10b66fc: cbz x8, #0x10b6870
// 0x10b6700: ldr x0, [x8, #0x50]
// 0x10b6704: cbz x0, #0x10b6870
// 0x10b6708: mov w1, #1
// 0x10b670c: mov x2, xzr
// 0x10b6710: bl #0x1b94cd0
// 0x10b6714: ldr x8, [x19, #0xa0]
// 0x10b6718: cbz x8, #0x10b6870
// 0x10b671c: ldr x0, [x8, #0x38]
// 0x10b6720: cbz x0, #0x10b6870
// 0x10b6724: mov w1, wzr
// 0x10b6728: mov x2, xzr
// 0x10b672c: bl #0x1b94cd0
// 0x10b6730: ldr x8, [x19, #0xa0]
// 0x10b6734: cbz x8, #0x10b6870
// 0x10b6738: ldr x0, [x8, #0x40]
// 0x10b673c: cbz x0, #0x10b6870
// 0x10b6740: mov w1, wzr
// 0x10b6744: mov x2, xzr
// 0x10b6748: bl #0x1b94cd0
// 0x10b674c: adrp x21, #0x1e8c000
// 0x10b6750: ldr x21, [x21, #0xd8]
// 0x10b6754: ldr x20, [x19, #0x448]
// 0x10b6758: ldr x0, [x21]
// 0x10b675c: ldr w8, [x0, #0xe0]
// 0x10b6760: cbnz w8, #0x10b6768
// 0x10b6764: bl #0xf7da5c
// 0x10b6768: mov x0, x20
// 0x10b676c: mov x1, xzr
// 0x10b6770: bl #0x1b98274
// 0x10b6774: tbz w0, #0, #0x10b6794
// 0x10b6778: ldr x0, [x19, #0xe0]
// 0x10b677c: cbz x0, #0x10b6870
// 0x10b6780: mov x1, xzr
// 0x10b6784: bl #0x1b94c14
// 0x10b6788: ldr x8, [x19, #0x448]
// 0x10b678c: cbnz x8, #0x10b67d0
// 0x10b6790: b #0x10b6870
// 0x10b6794: ldr x0, [x21]
// 0x10b6798: ldr x20, [x19, #0x3f0]
// 0x10b679c: ldr w8, [x0, #0xe0]
// 0x10b67a0: cbnz w8, #0x10b67a8
// 0x10b67a4: bl #0xf7da5c
// 0x10b67a8: mov x0, x20
// 0x10b67ac: mov x1, xzr
// 0x10b67b0: bl #0x1b98274
// 0x10b67b4: tbz w0, #0, #0x10b6850
// 0x10b67b8: ldr x0, [x19, #0xe0]
// 0x10b67bc: cbz x0, #0x10b6870
// 0x10b67c0: mov x1, xzr
// 0x10b67c4: bl #0x1b94c14
// 0x10b67c8: ldr x8, [x19, #0x3f0]
// 0x10b67cc: cbz x8, #0x10b6870
// 0x10b67d0: mov x20, x0
// 0x10b67d4: mov x0, x8
// 0x10b67d8: mov x1, xzr
// 0x10b67dc: bl #0x1b9d508
// 0x10b67e0: ldr x0, [x19, #0xe0]
// 0x10b67e4: cbz x0, #0x10b6870
// 0x10b67e8: mov x1, xzr
// 0x10b67ec: mov v8.16b, v0.16b
// 0x10b67f0: mov v9.16b, v1.16b
// 0x10b67f4: mov v10.16b, v2.16b
// 0x10b67f8: bl #0x1b94c14
// 0x10b67fc: cbz x0, #0x10b6870
// 0x10b6800: mov x1, xzr
// 0x10b6804: bl #0x1b9d9b8
// 0x10b6808: cbz x20, #0x10b6870
// 0x10b680c: mov v3.16b, v0.16b
// 0x10b6810: mov v4.16b, v1.16b
// 0x10b6814: mov v5.16b, v2.16b
// 0x10b6818: ldr s6, [x19, #0x34c]
// 0x10b681c: mov x0, x20
// 0x10b6820: mov v0.16b, v8.16b
// 0x10b6824: mov v1.16b, v9.16b
// 0x10b6828: mov v2.16b, v10.16b
// 0x10b682c: ldp x20, x19, [sp, #0x60]
// 0x10b6830: ldp x30, x21, [sp, #0x50]
// 0x10b6834: ldp d9, d8, [sp, #0x40]
// 0x10b6838: ldp d11, d10, [sp, #0x30]
// 0x10b683c: ldp d13, d12, [sp, #0x20]
// 0x10b6840: ldp d15, d14, [sp, #0x10]
// 0x10b6844: mov x1, xzr
// 0x10b6848: add sp, sp, #0x70
// 0x10b684c: b #0x1b9e490
// 0x10b6850: ldp x20, x19, [sp, #0x60]
// 0x10b6854: ldp x30, x21, [sp, #0x50]
// 0x10b6858: ldp d9, d8, [sp, #0x40]
// 0x10b685c: ldp d11, d10, [sp, #0x30]
// 0x10b6860: ldp d13, d12, [sp, #0x20]
// 0x10b6864: ldp d15, d14, [sp, #0x10]
// 0x10b6868: add sp, sp, #0x70
// 0x10b686c: ret
// 0x10b6870: bl #0xf7db74
```


## `WeaponBehavior.Update` — RVA `0xcb6874`

- Decompiled symbol: `WeaponBehavior_Update`
- Metadata signature: `private void Update() { }`
- Native interval: `9500` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: Decompiler produced no C-like text

```c
// 0x10b6874: sub sp, sp, #0xf0
// 0x10b6878: stp d15, d14, [sp, #0x80]
// 0x10b687c: stp d13, d12, [sp, #0x90]
// 0x10b6880: stp d11, d10, [sp, #0xa0]
// 0x10b6884: stp d9, d8, [sp, #0xb0]
// 0x10b6888: stp x30, x23, [sp, #0xc0]
// 0x10b688c: stp x22, x21, [sp, #0xd0]
// 0x10b6890: stp x20, x19, [sp, #0xe0]
// 0x10b6894: adrp x20, #0x1fab000
// 0x10b6898: ldrb w8, [x20, #0x4e3]
// 0x10b689c: mov x19, x0
// 0x10b68a0: tbnz w8, #0, #0x10b6990
// 0x10b68a4: adrp x0, #0x1e8e000
// 0x10b68a8: ldr x0, [x0, #0x6e0]
// 0x10b68ac: bl #0xf7d92c
// 0x10b68b0: adrp x0, #0x1e8e000
// 0x10b68b4: ldr x0, [x0, #0x6e8]
// 0x10b68b8: bl #0xf7d92c
// 0x10b68bc: adrp x0, #0x1e8e000
// 0x10b68c0: ldr x0, [x0, #0x6f0]
// 0x10b68c4: bl #0xf7d92c
// 0x10b68c8: adrp x0, #0x1e8c000
// 0x10b68cc: ldr x0, [x0, #0xd8]
// 0x10b68d0: bl #0xf7d92c
// 0x10b68d4: adrp x0, #0x1e8d000
// 0x10b68d8: ldr x0, [x0, #0x4a8]
// 0x10b68dc: bl #0xf7d92c
// 0x10b68e0: adrp x0, #0x1e8e000
// 0x10b68e4: ldr x0, [x0, #0x6d8]
// 0x10b68e8: bl #0xf7d92c
// 0x10b68ec: adrp x0, #0x1e8e000
// 0x10b68f0: ldr x0, [x0, #0x660]
// 0x10b68f4: bl #0xf7d92c
// 0x10b68f8: adrp x0, #0x1e8e000
// 0x10b68fc: ldr x0, [x0, #0x6f8]
// 0x10b6900: bl #0xf7d92c
// 0x10b6904: adrp x0, #0x1e8e000
// 0x10b6908: ldr x0, [x0, #0x700]
// 0x10b690c: bl #0xf7d92c
// 0x10b6910: adrp x0, #0x1e8e000
// 0x10b6914: ldr x0, [x0, #0x708]
// 0x10b6918: bl #0xf7d92c
// 0x10b691c: adrp x0, #0x1e8e000
// 0x10b6920: ldr x0, [x0, #0x640]
// 0x10b6924: bl #0xf7d92c
// 0x10b6928: adrp x0, #0x1e8d000
// 0x10b692c: ldr x0, [x0, #0xc80]
// 0x10b6930: bl #0xf7d92c
// 0x10b6934: adrp x0, #0x1e8e000
// 0x10b6938: ldr x0, [x0, #0x710]
// 0x10b693c: bl #0xf7d92c
// 0x10b6940: adrp x0, #0x1e8e000
// 0x10b6944: ldr x0, [x0, #0x718]
// 0x10b6948: bl #0xf7d92c
// 0x10b694c: adrp x0, #0x1e8e000
// 0x10b6950: ldr x0, [x0, #0x498]
// 0x10b6954: bl #0xf7d92c
// 0x10b6958: adrp x0, #0x1e8e000
// 0x10b695c: ldr x0, [x0, #0x4b8]
// 0x10b6960: bl #0xf7d92c
// 0x10b6964: adrp x0, #0x1e8e000
// 0x10b6968: ldr x0, [x0, #0x618]
// 0x10b696c: bl #0xf7d92c
// 0x10b6970: adrp x0, #0x1e8e000
// 0x10b6974: ldr x0, [x0, #0x5c8]
// 0x10b6978: bl #0xf7d92c
// 0x10b697c: adrp x0, #0x1e8e000
// 0x10b6980: ldr x0, [x0, #0x720]
// 0x10b6984: bl #0xf7d92c
// 0x10b6988: mov w8, #1
// 0x10b698c: strb w8, [x20, #0x4e3]
// 0x10b6990: movi v0.2d, #0000000000000000
// 0x10b6994: mov x0, xzr
// 0x10b6998: str wzr, [sp, #0x70]
// 0x10b699c: stp q0, q0, [sp, #0x50]
// 0x10b69a0: bl #0x1b9ae58
// 0x10b69a4: fcmp s0, #0.0
// 0x10b69a8: b.le #0x10b7970
// 0x10b69ac: mov x0, xzr
// 0x10b69b0: bl #0x1b89b60
// 0x10b69b4: fcmp s0, #0.0
// 0x10b69b8: b.le #0x10b7970
// 0x10b69bc: ldr x8, [x19, #0x80]
// 0x10b69c0: cbz x8, #0x10b8d8c
// 0x10b69c4: ldr d0, [x8, #0xc0]
// 0x10b69c8: add x21, x19, #0x3ac
// 0x10b69cc: str d0, [x21]
// 0x10b69d0: ldr x0, [x19, #0x78]
// 0x10b69d4: cbz x0, #0x10b8d8c
// 0x10b69d8: mov x1, xzr
// 0x10b69dc: bl #0x1b9d508
// 0x10b69e0: ldr x0, [x19, #0x70]
// 0x10b69e4: cbz x0, #0x10b8d8c
// 0x10b69e8: mov x1, xzr
// 0x10b69ec: mov v8.16b, v0.16b
// 0x10b69f0: mov v9.16b, v1.16b
// 0x10b69f4: mov v10.16b, v2.16b
// 0x10b69f8: bl #0x1b9d400
// 0x10b69fc: cbz x0, #0x10b8d8c
// 0x10b6a00: mov x1, xzr
// 0x10b6a04: bl #0x1b92154
// 0x10b6a08: cbz x0, #0x10b8d8c
// 0x10b6a0c: mov x1, xzr
// 0x10b6a10: bl #0x1b9d9b8
// 0x10b6a14: adrp x20, #0x1fab000
// 0x10b6a18: ldrb w8, [x20, #0x2c8]
// 0x10b6a1c: mov v11.16b, v0.16b
// 0x10b6a20: mov v12.16b, v1.16b
// 0x10b6a24: mov v13.16b, v2.16b
// 0x10b6a28: cbnz w8, #0x10b6a40
// 0x10b6a2c: adrp x0, #0x1e8c000
// 0x10b6a30: ldr x0, [x0, #0xa60]
// 0x10b6a34: bl #0xf7d92c
// 0x10b6a38: mov w8, #1
// 0x10b6a3c: strb w8, [x20, #0x2c8]
// 0x10b6a40: adrp x22, #0x1e8c000
// 0x10b6a44: ldr x22, [x22, #0xa60]
// 0x10b6a48: ldr x0, [x22]
// 0x10b6a4c: ldr w8, [x0, #0xe0]
// 0x10b6a50: cbnz w8, #0x10b6a58
// 0x10b6a54: bl #0xf7da5c
// 0x10b6a58: adrp x8, #0x832000
// 0x10b6a5c: fmul s0, s11, s11
// 0x10b6a60: fmul s1, s12, s12
// 0x10b6a64: ldr s14, [x8, #0x41c]
// 0x10b6a68: fadd s0, s0, s1
// 0x10b6a6c: fmul s1, s13, s13
// 0x10b6a70: fadd s0, s1, s0
// 0x10b6a74: fsqrt s2, s0
// 0x10b6a78: fcmp s2, s14
// 0x10b6a7c: b.le #0x10b6a90
// 0x10b6a80: fdiv s0, s11, s2
// 0x10b6a84: fdiv s1, s12, s2
// 0x10b6a88: fdiv s2, s13, s2
// 0x10b6a8c: b #0x10b6ac8
// 0x10b6a90: adrp x23, #0x1fab000
// 0x10b6a94: ldrb w8, [x23, #0x2c9]
// 0x10b6a98: cbnz w8, #0x10b6ab0
// 0x10b6a9c: adrp x0, #0x1e8c000
// 0x10b6aa0: ldr x0, [x0, #0x1e8]
// 0x10b6aa4: bl #0xf7d92c
// 0x10b6aa8: mov w8, #1
// 0x10b6aac: strb w8, [x23, #0x2c9]
// 0x10b6ab0: adrp x8, #0x1e8c000
// 0x10b6ab4: ldr x8, [x8, #0x1e8]
// 0x10b6ab8: ldr x8, [x8]
// 0x10b6abc: ldr x8, [x8, #0xb8]
// 0x10b6ac0: ldp s0, s1, [x8]
// 0x10b6ac4: ldr s2, [x8, #8]
// 0x10b6ac8: add x0, x19, #0x414
// 0x10b6acc: str s0, [x19, #0x420]
// 0x10b6ad0: fmov s0, #20.00000000
// 0x10b6ad4: mov x1, xzr
// 0x10b6ad8: str s8, [x19, #0x414]
// 0x10b6adc: str s9, [x19, #0x418]
// 0x10b6ae0: str s10, [x19, #0x41c]
// 0x10b6ae4: str s1, [x19, #0x424]
// 0x10b6ae8: str s2, [x19, #0x428]
// 0x10b6aec: bl #0x1b754fc
// 0x10b6af0: ldr x0, [x19, #0x78]
// 0x10b6af4: cbz x0, #0x10b8d8c
// 0x10b6af8: mov x1, xzr
// 0x10b6afc: mov v8.16b, v0.16b
// 0x10b6b00: mov v9.16b, v1.16b
// 0x10b6b04: mov v10.16b, v2.16b
// 0x10b6b08: bl #0x1b9d508
// 0x10b6b0c: ldrb w8, [x20, #0x2c8]
// 0x10b6b10: mov v11.16b, v0.16b
// 0x10b6b14: mov v12.16b, v1.16b
// 0x10b6b18: mov v13.16b, v2.16b
// 0x10b6b1c: cbnz w8, #0x10b6b34
// 0x10b6b20: adrp x0, #0x1e8c000
// 0x10b6b24: ldr x0, [x0, #0xa60]
// 0x10b6b28: bl #0xf7d92c
// 0x10b6b2c: mov w8, #1
// 0x10b6b30: strb w8, [x20, #0x2c8]
// 0x10b6b34: ldr x0, [x22]
// 0x10b6b38: fsub s11, s8, s11
// 0x10b6b3c: fsub s9, s9, s12
// 0x10b6b40: fsub s8, s10, s13
// 0x10b6b44: ldr w8, [x0, #0xe0]
// 0x10b6b48: cbnz w8, #0x10b6b50
// 0x10b6b4c: bl #0xf7da5c
// 0x10b6b50: fmul s0, s11, s11
// 0x10b6b54: fmul s1, s9, s9
// 0x10b6b58: fadd s0, s0, s1
// 0x10b6b5c: fmul s1, s8, s8
// 0x10b6b60: fadd s0, s1, s0
// 0x10b6b64: fsqrt s2, s0
// 0x10b6b68: fcmp s2, s14
// 0x10b6b6c: b.le #0x10b6b80
// 0x10b6b70: fdiv s0, s11, s2
// 0x10b6b74: fdiv s1, s9, s2
// 0x10b6b78: fdiv s2, s8, s2
// 0x10b6b7c: b #0x10b6bb8
// 0x10b6b80: adrp x20, #0x1fab000
// 0x10b6b84: ldrb w8, [x20, #0x2c9]
// 0x10b6b88: cbnz w8, #0x10b6ba0
// 0x10b6b8c: adrp x0, #0x1e8c000
// 0x10b6b90: ldr x0, [x0, #0x1e8]
// 0x10b6b94: bl #0xf7d92c
// 0x10b6b98: mov w8, #1
// 0x10b6b9c: strb w8, [x20, #0x2c9]
// 0x10b6ba0: adrp x8, #0x1e8c000
// 0x10b6ba4: ldr x8, [x8, #0x1e8]
// 0x10b6ba8: ldr x8, [x8]
// 0x10b6bac: ldr x8, [x8, #0xb8]
// 0x10b6bb0: ldp s0, s1, [x8]
// 0x10b6bb4: ldr s2, [x8, #8]
// 0x10b6bb8: ldr x8, [x19, #0xb8]
// 0x10b6bbc: str s0, [x19, #0x42c]
// 0x10b6bc0: str s1, [x19, #0x430]
// 0x10b6bc4: str s2, [x19, #0x434]
// 0x10b6bc8: cbz x8, #0x10b8d8c
// 0x10b6bcc: ldrb w9, [x8, #0x106]
// 0x10b6bd0: ldrb w8, [x19, #0xf4]
// 0x10b6bd4: cbz w9, #0x10b6c28
// 0x10b6bd8: cbnz w8, #0x10b6c10
// 0x10b6bdc: ldr x0, [x19, #0xe0]
// 0x10b6be0: cbz x0, #0x10b8d8c
// 0x10b6be4: mov x1, xzr
// 0x10b6be8: bl #0x1b94c14
// 0x10b6bec: cbz x0, #0x10b8d8c
// 0x10b6bf0: adrp x8, #0x832000
// 0x10b6bf4: ldr s0, [x8, #0x534]
// 0x10b6bf8: mov x1, xzr
// 0x10b6bfc: mov v1.16b, v0.16b
// 0x10b6c00: mov v2.16b, v0.16b
// 0x10b6c04: bl #0x1b9dbe0
// 0x10b6c08: mov w8, #1
// 0x10b6c0c: strb w8, [x19, #0xf4]
// 0x10b6c10: adrp x8, #0x832000
// 0x10b6c14: ldr s0, [x19, #0x3cc]
// 0x10b6c18: ldr s1, [x8, #0x4f4]
// 0x10b6c1c: fmul s0, s0, s1
// 0x10b6c20: str s0, [x19, #0x3d4]
// 0x10b6c24: b #0x10b6c54
// 0x10b6c28: cbz w8, #0x10b6c54
// 0x10b6c2c: ldr x0, [x19, #0xe0]
// 0x10b6c30: cbz x0, #0x10b8d8c
// 0x10b6c34: mov x1, xzr
// 0x10b6c38: bl #0x1b94c14
// 0x10b6c3c: cbz x0, #0x10b8d8c
// 0x10b6c40: ldp s1, s2, [x19, #0xec]
// 0x10b6c44: ldr s0, [x19, #0xe8]
// 0x10b6c48: mov x1, xzr
// 0x10b6c4c: bl #0x1b9dbe0
// 0x10b6c50: strb wzr, [x19, #0xf4]
// 0x10b6c54: ldrb w8, [x19, #0x1f6]
// 0x10b6c58: cbnz w8, #0x10b6c80
// 0x10b6c5c: ldrb w8, [x19, #0x1f7]
// 0x10b6c60: cbnz w8, #0x10b6c80
// 0x10b6c64: ldr w8, [x19, #0x128]
// 0x10b6c68: cmp w8, #0
// 0x10b6c6c: b.gt #0x10b6c80
// 0x10b6c70: ldr x8, [x19, #0x80]
// 0x10b6c74: cbz x8, #0x10b8d8c
// 0x10b6c78: mov w9, #1
// 0x10b6c7c: strb w9, [x8, #0x1a0]
// 0x10b6c80: ldrb w8, [x19, #0x538]
// 0x10b6c84: cbz w8, #0x10b6e90
// 0x10b6c88: adrp x8, #0x1e8c000
// 0x10b6c8c: ldr x8, [x8, #0xd8]
// 0x10b6c90: ldr x20, [x19, #0x540]
// 0x10b6c94: ldr x0, [x8]
// 0x10b6c98: ldr w8, [x0, #0xe0]
// 0x10b6c9c: cbnz w8, #0x10b6ca4
// 0x10b6ca0: bl #0xf7da5c
// 0x10b6ca4: mov x0, x20
// 0x10b6ca8: mov x1, xzr
// 0x10b6cac: bl #0x1b98274
// 0x10b6cb0: tbz w0, #0, #0x10b6dac
// 0x10b6cb4: mov x0, xzr
// 0x10b6cb8: bl #0x1b9ad30
// 0x10b6cbc: ldr s1, [x19, #0x57c]
// 0x10b6cc0: ldr s2, [x19, #0x578]
// 0x10b6cc4: fadd s1, s1, s2
// 0x10b6cc8: fcmp s0, s1
// 0x10b6ccc: b.le #0x10b6dac
// 0x10b6cd0: ldr x0, [x19, #0x78]
// 0x10b6cd4: cbz x0, #0x10b8d8c
// 0x10b6cd8: mov x1, xzr
// 0x10b6cdc: bl #0x1b9d508
// 0x10b6ce0: ldr x0, [x19, #0x78]
// 0x10b6ce4: cbz x0, #0x10b8d8c
// 0x10b6ce8: mov x1, xzr
// 0x10b6cec: mov v8.16b, v0.16b
// 0x10b6cf0: mov v9.16b, v1.16b
// 0x10b6cf4: mov v11.16b, v2.16b
// 0x10b6cf8: bl #0x1b9d940
// 0x10b6cfc: ldrb w8, [x19, #0x539]
// 0x10b6d00: fmov s3, #0.25000000
// 0x10b6d04: fmul s0, s0, s3
// 0x10b6d08: fmul s1, s1, s3
// 0x10b6d0c: fmul s2, s2, s3
// 0x10b6d10: fsub s10, s8, s0
// 0x10b6d14: fsub s9, s9, s1
// 0x10b6d18: fsub s8, s11, s2
// 0x10b6d1c: str s10, [x19, #0x548]
// 0x10b6d20: str s9, [x19, #0x54c]
// 0x10b6d24: str s8, [x19, #0x550]
// 0x10b6d28: cbnz w8, #0x10b6da0
// 0x10b6d2c: ldr x0, [x19, #0x540]
// 0x10b6d30: cbz x0, #0x10b8d8c
// 0x10b6d34: mov x1, xzr
// 0x10b6d38: bl #0x1b9d508
// 0x10b6d3c: ldr w0, [x19, #0x378]
// 0x10b6d40: mov x1, xzr
// 0x10b6d44: mov v11.16b, v0.16b
// 0x10b6d48: mov v12.16b, v1.16b
// 0x10b6d4c: mov v13.16b, v2.16b
// 0x10b6d50: bl #0x1b9515c
// 0x10b6d54: adrp x8, #0x1e8d000
// 0x10b6d58: ldr x8, [x8, #0x4a8]
// 0x10b6d5c: mov w20, w0
// 0x10b6d60: ldr x8, [x8]
// 0x10b6d64: ldr w9, [x8, #0xe0]
// 0x10b6d68: cbnz w9, #0x10b6d74
// 0x10b6d6c: mov x0, x8
// 0x10b6d70: bl #0xf7da5c
// 0x10b6d74: mov v0.16b, v10.16b
// 0x10b6d78: mov v1.16b, v9.16b
// 0x10b6d7c: mov v2.16b, v8.16b
// 0x10b6d80: mov v3.16b, v11.16b
// 0x10b6d84: mov v4.16b, v12.16b
// 0x10b6d88: mov v5.16b, v13.16b
// 0x10b6d8c: mov w0, w20
// 0x10b6d90: mov x1, xzr
// 0x10b6d94: bl #0x1bcc4ac
// 0x10b6d98: and w8, w0, #1
// 0x10b6d9c: strb w8, [x19, #0x53a]
// 0x10b6da0: mov x0, xzr
// 0x10b6da4: bl #0x1b9ad30
// 0x10b6da8: str s0, [x19, #0x57c]
// 0x10b6dac: ldrb w8, [x19, #0x53a]
// 0x10b6db0: ldr s2, [x19, #0x590]
// 0x10b6db4: cbz w8, #0x10b6f60
// 0x10b6db8: ldr s3, [x19, #0x580]
// 0x10b6dbc: fcmp s2, s3
// 0x10b6dc0: b.le #0x10b7030
// 0x10b6dc4: ldr d0, [x21, #0x1e8]
// 0x10b6dc8: ldr d1, [x21, #0x1d8]
// 0x10b6dcc: add x8, x19, #0x590
// 0x10b6dd0: add x9, x19, #0x58c
// 0x10b6dd4: mov v2.s[1], v0.s[0]
// 0x10b6dd8: mov v3.s[1], v1.s[0]
// 0x10b6ddc: add x8, x8, #0xc
// 0x10b6de0: mov v3.s[2], v1.s[1]
// 0x10b6de4: mov v2.s[2], v0.s[1]
// 0x10b6de8: ld1 {v3.s}[3], [x9]
// 0x10b6dec: ld1 {v2.s}[3], [x8]
// 0x10b6df0: mov x0, xzr
// 0x10b6df4: stp q3, q2, [sp]
// 0x10b6df8: bl #0x1b9ae30
// 0x10b6dfc: fmov s1, #5.00000000
// 0x10b6e00: fmov s2, #1.00000000
// 0x10b6e04: fmul s0, s0, s1
// 0x10b6e08: fmov s3, wzr
// 0x10b6e0c: fmin s1, s0, s2
// 0x10b6e10: fcmp s0, #0.0
// 0x10b6e14: fcsel s0, s1, s3, pl
// 0x10b6e18: ldp q1, q2, [sp]
// 0x10b6e1c: ldr x0, [x19, #0x570]
// 0x10b6e20: fsub v1.4s, v1.4s, v2.4s
// 0x10b6e24: fmul v0.4s, v1.4s, v0.s[0]
// 0x10b6e28: fadd v0.4s, v2.4s, v0.4s
// 0x10b6e2c: str q0, [x19, #0x590]
// 0x10b6e30: cbz x0, #0x10b8d8c
// 0x10b6e34: adrp x22, #0x1e8e000
// 0x10b6e38: adrp x23, #0x1e8d000
// 0x10b6e3c: ldr x22, [x22, #0x6f0]
// 0x10b6e40: ldr x23, [x23, #0xc80]
// 0x10b6e44: mov w20, wzr
// 0x10b6e48: ldr w8, [x0, #0x18]
// 0x10b6e4c: cmp w20, w8
// 0x10b6e50: b.ge #0x10b7030
// 0x10b6e54: ldr x2, [x22]
// 0x10b6e58: mov w1, w20
// 0x10b6e5c: bl #0x14a30c0
// 0x10b6e60: cbz x0, #0x10b8d8c
// 0x10b6e64: ldr s3, [x19, #0x59c]
// 0x10b6e68: ldr s2, [x19, #0x598]
// 0x10b6e6c: ldr s1, [x19, #0x594]
// 0x10b6e70: ldr s0, [x19, #0x590]
// 0x10b6e74: ldr x1, [x23]
// 0x10b6e78: mov x2, xzr
// 0x10b6e7c: bl #0x1b7a790
// 0x10b6e80: ldr x0, [x19, #0x570]
// 0x10b6e84: add w20, w20, #1
// 0x10b6e88: cbnz x0, #0x10b6e48
// 0x10b6e8c: b #0x10b8d8c
// 0x10b6e90: ldr s1, [x19, #0x590]
// 0x10b6e94: mov w8, #0x437f0000
// 0x10b6e98: fmov s0, w8
// 0x10b6e9c: fcmp s1, s0
// 0x10b6ea0: b.pl #0x10b7030
// 0x10b6ea4: ldr d0, [x21, #0x1e8]
// 0x10b6ea8: add x8, x19, #0x590
// 0x10b6eac: add x8, x8, #0xc
// 0x10b6eb0: mov x0, xzr
// 0x10b6eb4: mov v1.s[1], v0.s[0]
// 0x10b6eb8: mov v1.s[2], v0.s[1]
// 0x10b6ebc: ld1 {v1.s}[3], [x8]
// 0x10b6ec0: str q1, [sp, #0x10]
// 0x10b6ec4: bl #0x1b9ae30
// 0x10b6ec8: fmov s1, #5.00000000
// 0x10b6ecc: fmov s2, #1.00000000
// 0x10b6ed0: fmul s0, s0, s1
// 0x10b6ed4: fmin s1, s0, s2
// 0x10b6ed8: ldr q2, [sp, #0x10]
// 0x10b6edc: fmov s3, wzr
// 0x10b6ee0: fmov v4.4s, #1.00000000
// 0x10b6ee4: ldr x0, [x19, #0x570]
// 0x10b6ee8: fcmp s0, #0.0
// 0x10b6eec: fcsel s0, s1, s3, pl
// 0x10b6ef0: fsub v1.4s, v4.4s, v2.4s
// 0x10b6ef4: fmul v0.4s, v1.4s, v0.s[0]
// 0x10b6ef8: fadd v0.4s, v2.4s, v0.4s
// 0x10b6efc: str q0, [x19, #0x590]
// 0x10b6f00: cbz x0, #0x10b8d8c
// 0x10b6f04: adrp x22, #0x1e8e000
// 0x10b6f08: adrp x23, #0x1e8d000
// 0x10b6f0c: ldr x22, [x22, #0x6f0]
// 0x10b6f10: ldr x23, [x23, #0xc80]
// 0x10b6f14: mov w20, wzr
// 0x10b6f18: ldr w8, [x0, #0x18]
// 0x10b6f1c: cmp w20, w8
// 0x10b6f20: b.ge #0x10b702c
// 0x10b6f24: ldr x2, [x22]
// 0x10b6f28: mov w1, w20
// 0x10b6f2c: bl #0x14a30c0
// 0x10b6f30: cbz x0, #0x10b8d8c
// 0x10b6f34: ldr s3, [x19, #0x59c]
// 0x10b6f38: ldr s2, [x19, #0x598]
// 0x10b6f3c: ldr s1, [x19, #0x594]
// 0x10b6f40: ldr s0, [x19, #0x590]
// 0x10b6f44: ldr x1, [x23]
// 0x10b6f48: mov x2, xzr
// 0x10b6f4c: bl #0x1b7a790
// 0x10b6f50: ldr x0, [x19, #0x570]
// 0x10b6f54: add w20, w20, #1
// 0x10b6f58: cbnz x0, #0x10b6f18
// 0x10b6f5c: b #0x10b8d8c
// 0x10b6f60: mov w8, #0x437f0000
// 0x10b6f64: fmov s0, w8
// 0x10b6f68: fcmp s2, s0
// 0x10b6f6c: b.pl #0x10b7030
// 0x10b6f70: ldr d0, [x21, #0x1e8]
// 0x10b6f74: add x8, x19, #0x590
// 0x10b6f78: add x8, x8, #0xc
// 0x10b6f7c: mov x0, xzr
// 0x10b6f80: mov v2.s[1], v0.s[0]
// 0x10b6f84: mov v2.s[2], v0.s[1]
// 0x10b6f88: ld1 {v2.s}[3], [x8]
// 0x10b6f8c: str q2, [sp, #0x10]
// 0x10b6f90: bl #0x1b9ae30
// 0x10b6f94: fmov s1, #5.00000000
// 0x10b6f98: fmov s2, #1.00000000
// 0x10b6f9c: fmul s0, s0, s1
// 0x10b6fa0: fmin s1, s0, s2
// 0x10b6fa4: ldr q2, [sp, #0x10]
// 0x10b6fa8: fmov s3, wzr
// 0x10b6fac: fmov v4.4s, #1.00000000
// 0x10b6fb0: ldr x0, [x19, #0x570]
// 0x10b6fb4: fcmp s0, #0.0
// 0x10b6fb8: fcsel s0, s1, s3, pl
// 0x10b6fbc: fsub v1.4s, v4.4s, v2.4s
// 0x10b6fc0: fmul v0.4s, v1.4s, v0.s[0]
// 0x10b6fc4: fadd v0.4s, v2.4s, v0.4s
// 0x10b6fc8: str q0, [x19, #0x590]
// 0x10b6fcc: cbz x0, #0x10b8d8c
// 0x10b6fd0: adrp x22, #0x1e8e000
// 0x10b6fd4: adrp x23, #0x1e8d000
// 0x10b6fd8: ldr x22, [x22, #0x6f0]
// 0x10b6fdc: ldr x23, [x23, #0xc80]
// 0x10b6fe0: mov w20, wzr
// 0x10b6fe4: ldr w8, [x0, #0x18]
// 0x10b6fe8: cmp w20, w8
// 0x10b6fec: b.ge #0x10b7030
// 0x10b6ff0: ldr x2, [x22]
// 0x10b6ff4: mov w1, w20
// 0x10b6ff8: bl #0x14a30c0
// 0x10b6ffc: cbz x0, #0x10b8d8c
// 0x10b7000: ldr s3, [x19, #0x59c]
// 0x10b7004: ldr s2, [x19, #0x598]
// 0x10b7008: ldr s1, [x19, #0x594]
// 0x10b700c: ldr s0, [x19, #0x590]
// 0x10b7010: ldr x1, [x23]
// 0x10b7014: mov x2, xzr
// 0x10b7018: bl #0x1b7a790
// 0x10b701c: ldr x0, [x19, #0x570]
// 0x10b7020: add w20, w20, #1
// 0x10b7024: cbnz x0, #0x10b6fe4
// 0x10b7028: b #0x10b8d8c
// 0x10b702c: strb wzr, [x19, #0x53a]
// 0x10b7030: adrp x22, #0x1e8c000
// 0x10b7034: ldr x22, [x22, #0xd8]
// 0x10b7038: ldr x20, [x19, #0x3f0]
// 0x10b703c: ldr x0, [x22]
// 0x10b7040: ldr w8, [x0, #0xe0]
// 0x10b7044: cbnz w8, #0x10b704c
// 0x10b7048: bl #0xf7da5c
// 0x10b704c: mov x0, x20
// 0x10b7050: mov x1, xzr
// 0x10b7054: bl #0x1b98274
// 0x10b7058: tbz w0, #0, #0x10b7070
// 0x10b705c: ldr x0, [x19, #0x3f0]
// 0x10b7060: cbz x0, #0x10b8d8c
// 0x10b7064: mov x1, xzr
// 0x10b7068: bl #0x1b9d508
// 0x10b706c: b #0x10b70e8
// 0x10b7070: ldr x0, [x22]
// 0x10b7074: ldr x20, [x19, #0x448]
// 0x10b7078: ldr w8, [x0, #0xe0]
// 0x10b707c: cbnz w8, #0x10b7084
// 0x10b7080: bl #0xf7da5c
// 0x10b7084: mov x0, x20
// 0x10b7088: mov x1, xzr
// 0x10b708c: bl #0x1b98274
// 0x10b7090: tbz w0, #0, #0x10b70f4
// 0x10b7094: ldr x0, [x19, #0x448]
// 0x10b7098: cbz x0, #0x10b8d8c
// 0x10b709c: mov x1, xzr
// 0x10b70a0: bl #0x1b9d508
// 0x10b70a4: ldr x0, [x19, #0x448]
// 0x10b70a8: str s0, [x19, #0x3f8]
// 0x10b70ac: str s1, [x19, #0x3fc]
// 0x10b70b0: str s2, [x19, #0x400]
// 0x10b70b4: cbz x0, #0x10b8d8c
// 0x10b70b8: mov x1, xzr
// 0x10b70bc: mov v8.16b, v0.16b
// 0x10b70c0: mov v9.16b, v1.16b
// 0x10b70c4: mov v10.16b, v2.16b
// 0x10b70c8: bl #0x1b9d9b8
// 0x10b70cc: ldr s3, [x19, #0x410]
// 0x10b70d0: fmul s0, s3, s0
// 0x10b70d4: fmul s1, s3, s1
// 0x10b70d8: fmul s2, s3, s2
// 0x10b70dc: fsub s0, s8, s0
// 0x10b70e0: fsub s1, s9, s1
// 0x10b70e4: fsub s2, s10, s2
// 0x10b70e8: str s0, [x19, #0x3f8]
// 0x10b70ec: str s1, [x19, #0x3fc]
// 0x10b70f0: str s2, [x19, #0x400]
// 0x10b70f4: ldr s0, [x19, #0x204]
// 0x10b70f8: fcmp s0, #0.0
// 0x10b70fc: b.ne #0x10b7108
// 0x10b7100: ldrb w8, [x19, #0x1f5]
// 0x10b7104: cbz w8, #0x10b7138
// 0x10b7108: ldr x10, [x19, #0x60]
// 0x10b710c: cbz x10, #0x10b8d8c
// 0x10b7110: ldr w8, [x19, #0x12c]
// 0x10b7114: str w8, [x10, #0x20]
// 0x10b7118: ldr w9, [x19, #0x128]
// 0x10b711c: str w9, [x10, #0x24]
// 0x10b7120: ldr x10, [x19, #0x68]
// 0x10b7124: cbz x10, #0x10b8d8c
// 0x10b7128: stp w8, w9, [x10, #0x20]
// 0x10b712c: ldrb w8, [x19, #0x1f5]
// 0x10b7130: cbnz w8, #0x10b7970
// 0x10b7134: b #0x10b7168
// 0x10b7138: ldr x8, [x19, #0x60]
// 0x10b713c: cbz x8, #0x10b8d8c
// 0x10b7140: ldr w9, [x19, #0x12c]
// 0x10b7144: str w9, [x8, #0x20]
// 0x10b7148: ldr w11, [x19, #0x128]
// 0x10b714c: str w11, [x8, #0x24]
// 0x10b7150: ldr x10, [x19, #0x68]
// 0x10b7154: cbz x10, #0x10b8d8c
// 0x10b7158: stp w9, w11, [x10, #0x20]
// 0x10b715c: ldrb w9, [x19, #0x1f6]
// 0x10b7160: strb w9, [x8, #0x28]
// 0x10b7164: strb w9, [x10, #0x28]
// 0x10b7168: ldr x8, [x19, #0x98]
// 0x10b716c: cbz x8, #0x10b8d8c
// 0x10b7170: ldr s0, [x8, #0x20c]
// 0x10b7174: fcmp s0, #0.0
// 0x10b7178: b.lt #0x10b78e4
// 0x10b717c: ldr s8, [x19, #0x3e8]
// 0x10b7180: ldr s9, [x19, #0x3e4]
// 0x10b7184: mov x0, xzr
// 0x10b7188: bl #0x1b9ad30
// 0x10b718c: ldrb w8, [x19, #0x1f6]
// 0x10b7190: fadd s1, s8, s9
// 0x10b7194: fcmp s1, s0
// 0x10b7198: cset w9, gt
// 0x10b719c: strb w9, [x19, #0x3ec]
// 0x10b71a0: cbz w8, #0x10b71ac
// 0x10b71a4: ldrb w8, [x19, #0x229]
// 0x10b71a8: cbz w8, #0x10b729c
// 0x10b71ac: ldr x8, [x19, #0x80]
// 0x10b71b0: cbz x8, #0x10b8d8c
// 0x10b71b4: ldrb w9, [x8, #0x1a0]
// 0x10b71b8: cbz w9, #0x10b722c
// 0x10b71bc: mov x0, x19
// 0x10b71c0: mov w1, wzr
// 0x10b71c4: bl #0x10b35f8
// 0x10b71c8: ldr x8, [x19, #0x98]
// 0x10b71cc: mov w9, #1
// 0x10b71d0: strb w9, [x19, #0x346]
// 0x10b71d4: cbz x8, #0x10b8d8c
// 0x10b71d8: ldr x8, [x8, #0x68]
// 0x10b71dc: cbz x8, #0x10b8d8c
// 0x10b71e0: strh wzr, [x8, #0x17c]
// 0x10b71e4: strb wzr, [x8, #0x17e]
// 0x10b71e8: ldr x8, [x19, #0x80]
// 0x10b71ec: cbz x8, #0x10b8d8c
// 0x10b71f0: ldrb w8, [x8, #0x195]
// 0x10b71f4: cbz w8, #0x10b75f8
// 0x10b71f8: ldr x8, [x19, #0x90]
// 0x10b71fc: cbz x8, #0x10b8d8c
// 0x10b7200: ldr s0, [x19, #0x204]
// 0x10b7204: adrp x9, #0x831000
// 0x10b7208: add x9, x9, #0xe58
// 0x10b720c: fcmp s0, #0.0
// 0x10b7210: cset w10, eq
// 0x10b7214: ldr s0, [x9, w10, uxtw #2]
// 0x10b7218: str s0, [x8, #0x23c]
// 0x10b721c: strb wzr, [x19, #0x3a4]
// 0x10b7220: strb wzr, [x19, #0x3a7]
// 0x10b7224: mov w8, #1
// 0x10b7228: b #0x10b7620
// 0x10b722c: ldrb w9, [x19, #0x346]
// 0x10b7230: cbz w9, #0x10b7238
// 0x10b7234: strb wzr, [x19, #0x346]
// 0x10b7238: ldr x9, [x19, #0x90]
// 0x10b723c: cbz x9, #0x10b8d8c
// 0x10b7240: str wzr, [x9, #0x23c]
// 0x10b7244: ldrb w10, [x8, #0x2b1]
// 0x10b7248: cbnz w10, #0x10b7254
// 0x10b724c: ldrb w10, [x8, #0x2dc]
// 0x10b7250: cbz w10, #0x10b726c
// 0x10b7254: ldrb w9, [x9, #0x129]
// 0x10b7258: cbz w9, #0x10b7264
// 0x10b725c: ldrb w10, [x8, #0x147]
// 0x10b7260: cbz w10, #0x10b726c
// 0x10b7264: ldrb w10, [x8, #0x2d0]
// 0x10b7268: cbz w10, #0x10b7428
// 0x10b726c: ldrb w8, [x19, #0x3a7]
// 0x10b7270: cbnz w8, #0x10b7288
// 0x10b7274: mov x0, xzr
// 0x10b7278: bl #0x1b9ad30
// 0x10b727c: mov w8, #1
// 0x10b7280: str s0, [x19, #0x3a8]
// 0x10b7284: strb w8, [x19, #0x3a7]
// 0x10b7288: mov w9, #1
// 0x10b728c: mov w8, wzr
// 0x10b7290: strb w9, [x19, #0x3a4]
// 0x10b7294: strb wzr, [x19, #0x3c5]
// 0x10b7298: b #0x10b7620
// 0x10b729c: ldr x8, [x19, #0x80]
// 0x10b72a0: cbz x8, #0x10b8d8c
// 0x10b72a4: ldrb w9, [x8, #0x2b1]
// 0x10b72a8: cbz w9, #0x10b72cc
// 0x10b72ac: ldrb w9, [x8, #0x147]
// 0x10b72b0: cbnz w9, #0x10b72cc
// 0x10b72b4: ldr x9, [x19, #0xa0]
// 0x10b72b8: cbz x9, #0x10b8d8c
// 0x10b72bc: ldrb w9, [x9, #0x89]
// 0x10b72c0: cbnz w9, #0x10b72cc
// 0x10b72c4: ldrb w9, [x8, #0x2c2]
// 0x10b72c8: cbz w9, #0x10b758c
// 0x10b72cc: ldr x9, [x19, #0xa0]
// 0x10b72d0: cbz x9, #0x10b8d8c
// 0x10b72d4: ldrb w9, [x9, #0x89]
// 0x10b72d8: cbz w9, #0x10b7328
// 0x10b72dc: ldr w9, [x19, #0x134]
// 0x10b72e0: ldr w10, [x19, #0x130]
// 0x10b72e4: cmp w9, w10
// 0x10b72e8: b.eq #0x10b7328
// 0x10b72ec: ldr s0, [x19, #0x3b8]
// 0x10b72f0: scvtf s1, w9
// 0x10b72f4: fadd s1, s1, s1
// 0x10b72f8: scvtf s0, s0
// 0x10b72fc: fcmp s1, s0
// 0x10b7300: b.hi #0x10b7328
// 0x10b7304: ldr s8, [x19, #0x3c8]
// 0x10b7308: ldr s9, [x19, #0x3bc]
// 0x10b730c: mov x0, xzr
// 0x10b7310: bl #0x1b9ad30
// 0x10b7314: fadd s1, s8, s9
// 0x10b7318: fcmp s1, s0
// 0x10b731c: b.mi #0x10b7330
// 0x10b7320: ldr x8, [x19, #0x80]
// 0x10b7324: cbz x8, #0x10b8d8c
// 0x10b7328: ldrb w8, [x8, #0x1a0]
// 0x10b732c: cbz w8, #0x10b7498
// 0x10b7330: ldr x8, [x19, #0x90]
// 0x10b7334: cbz x8, #0x10b8d8c
// 0x10b7338: ldrb w9, [x8, #0x129]
// 0x10b733c: cbz w9, #0x10b71ac
// 0x10b7340: strb wzr, [x8, #0x129]
// 0x10b7344: adrp x20, #0x1e8e000
// 0x10b7348: ldr x20, [x20, #0x498]
// 0x10b734c: mov x0, x19
// 0x10b7350: mov x2, xzr
// 0x10b7354: ldr x1, [x20]
// 0x10b7358: bl #0x1b960e0
// 0x10b735c: ldr w8, [x19, #0x134]
// 0x10b7360: ldr w9, [x19, #0x130]
// 0x10b7364: cmp w8, w9
// 0x10b7368: b.eq #0x10b7380
// 0x10b736c: mov w8, #-0x3e800000
// 0x10b7370: str wzr, [x19, #0x3b8]
// 0x10b7374: str w8, [x19, #0x3c0]
// 0x10b7378: str w8, [x19, #0x3c8]
// 0x10b737c: str w8, [x19, #0x3e8]
// 0x10b7380: ldr x0, [x19, #0x118]
// 0x10b7384: cbz x0, #0x10b8d8c
// 0x10b7388: fmov s0, #1.00000000
// 0x10b738c: mov x1, xzr
// 0x10b7390: bl #0x1b67eb4
// 0x10b7394: ldr x0, [x19, #0x118]
// 0x10b7398: cbz x0, #0x10b8d8c
// 0x10b739c: adrp x8, #0x1e8e000
// 0x10b73a0: ldr x8, [x8, #0x640]
// 0x10b73a4: mov x2, xzr
// 0x10b73a8: ldr x1, [x8]
// 0x10b73ac: bl #0x1b67884
// 0x10b73b0: ldr w8, [x19, #0x134]
// 0x10b73b4: ldr w9, [x19, #0x130]
// 0x10b73b8: cmp w8, w9
// 0x10b73bc: b.ne #0x10b73ec
// 0x10b73c0: ldr s8, [x19, #0x3c0]
// 0x10b73c4: ldr s9, [x19, #0x3bc]
// 0x10b73c8: mov x0, xzr
// 0x10b73cc: bl #0x1b9ad30
// 0x10b73d0: fmov s1, #0.50000000
// 0x10b73d4: fmul s1, s9, s1
// 0x10b73d8: fadd s1, s8, s1
// 0x10b73dc: fcmp s1, s0
// 0x10b73e0: b.pl #0x10b73ec
// 0x10b73e4: ldrb w8, [x19, #0x3c5]
// 0x10b73e8: cbz w8, #0x10b7554
// 0x10b73ec: ldr x0, [x19, #0x690]
// 0x10b73f0: cbz x0, #0x10b8d8c
// 0x10b73f4: mov x1, xzr
// 0x10b73f8: mov x2, xzr
// 0x10b73fc: bl #0x1b6a588
// 0x10b7400: ldr w8, [x19, #0x134]
// 0x10b7404: ldr w9, [x19, #0x130]
// 0x10b7408: cmp w8, w9
// 0x10b740c: b.ne #0x10b71ac
// 0x10b7410: ldr x0, [x19, #0x110]
// 0x10b7414: cbz x0, #0x10b8d8c
// 0x10b7418: ldr x1, [x20]
// 0x10b741c: mov x2, xzr
// 0x10b7420: bl #0x1b67884
// 0x10b7424: b #0x10b71ac
// 0x10b7428: ldr x10, [x19, #0x98]
// 0x10b742c: cbz x10, #0x10b8d8c
// 0x10b7430: ldrb w10, [x10, #0x2d0]
// 0x10b7434: cbz w10, #0x10b7444
// 0x10b7438: ldr s0, [x19, #0x204]
// 0x10b743c: fcmp s0, #0.0
// 0x10b7440: b.eq #0x10b726c
// 0x10b7444: ldrb w11, [x8, #0x2c2]
// 0x10b7448: cbnz w11, #0x10b726c
// 0x10b744c: ldrb w11, [x8, #0x228]
// 0x10b7450: cbz w11, #0x10b7580
// 0x10b7454: ldr s0, [x8, #0x290]
// 0x10b7458: fmov s1, #0.75000000
// 0x10b745c: fcmp s0, s1
// 0x10b7460: b.gt #0x10b726c
// 0x10b7464: ldr x11, [x19, #0xa0]
// 0x10b7468: cbz x11, #0x10b8d8c
// 0x10b746c: ldrb w11, [x11, #0x89]
// 0x10b7470: cbz w11, #0x10b747c
// 0x10b7474: ldrb w11, [x8, #0x2dc]
// 0x10b7478: cbz w11, #0x10b726c
// 0x10b747c: ldr s0, [x19, #0x3b0]
// 0x10b7480: ldrb w11, [x8, #0x146]
// 0x10b7484: fcmp s0, #0.0
// 0x10b7488: b.eq #0x10b75ac
// 0x10b748c: b.vs #0x10b75ac
// 0x10b7490: cbnz w11, #0x10b75d0
// 0x10b7494: b #0x10b75b0
// 0x10b7498: ldr w8, [x19, #0x12c]
// 0x10b749c: cmp w8, #0
// 0x10b74a0: b.gt #0x10b71ac
// 0x10b74a4: mov x0, xzr
// 0x10b74a8: bl #0x1b9ad30
// 0x10b74ac: ldr s1, [x19, #0x1fc]
// 0x10b74b0: ldr s2, [x19, #0x150]
// 0x10b74b4: fsub s0, s0, s1
// 0x10b74b8: fcmp s0, s2
// 0x10b74bc: b.le #0x10b71ac
// 0x10b74c0: ldrb w8, [x19, #0x3a4]
// 0x10b74c4: cbnz w8, #0x10b74d8
// 0x10b74c8: ldr x8, [x19, #0x80]
// 0x10b74cc: cbz x8, #0x10b8d8c
// 0x10b74d0: ldrb w8, [x8, #0x147]
// 0x10b74d4: cbz w8, #0x10b71ac
// 0x10b74d8: ldrb w8, [x19, #0x1f6]
// 0x10b74dc: cbz w8, #0x10b71ac
// 0x10b74e0: ldr w8, [x19, #0x128]
// 0x10b74e4: cmp w8, #1
// 0x10b74e8: b.lt #0x10b71ac
// 0x10b74ec: ldr x8, [x19, #0x90]
// 0x10b74f0: cbz x8, #0x10b8d8c
// 0x10b74f4: ldrb w8, [x8, #0x129]
// 0x10b74f8: cbnz w8, #0x10b71ac
// 0x10b74fc: ldr x8, [x19, #0x88]
// 0x10b7500: cbz x8, #0x10b8d8c
// 0x10b7504: ldrb w8, [x8, #0x128]
// 0x10b7508: cbnz w8, #0x10b71ac
// 0x10b750c: ldr x8, [x19, #0x80]
// 0x10b7510: cbz x8, #0x10b8d8c
// 0x10b7514: ldrb w8, [x8, #0x1a0]
// 0x10b7518: cbnz w8, #0x10b71ac
// 0x10b751c: ldr s8, [x19, #0x3e0]
// 0x10b7520: ldr s9, [x19, #0x3d4]
// 0x10b7524: mov x0, xzr
// 0x10b7528: bl #0x1b9ad30
// 0x10b752c: fadd s1, s8, s9
// 0x10b7530: fcmp s1, s0
// 0x10b7534: b.pl #0x10b71ac
// 0x10b7538: adrp x8, #0x1e8e000
// 0x10b753c: ldr x8, [x8, #0x498]
// 0x10b7540: mov x0, x19
// 0x10b7544: mov x2, xzr
// 0x10b7548: ldr x1, [x8]
// 0x10b754c: bl #0x1b95b9c
// 0x10b7550: b #0x10b71ac
// 0x10b7554: ldr w8, [x19, #0x130]
// 0x10b7558: ldr w9, [x19, #0x12c]
// 0x10b755c: ldr w10, [x19, #0x128]
// 0x10b7560: sub w12, w8, w9
// 0x10b7564: subs w11, w10, w12
// 0x10b7568: str w12, [x19, #0x3b4]
// 0x10b756c: b.ge #0x10b7598
// 0x10b7570: add w8, w10, w9
// 0x10b7574: str w8, [x19, #0x12c]
// 0x10b7578: str wzr, [x19, #0x128]
// 0x10b757c: b #0x10b75a0
// 0x10b7580: ldrb w11, [x8, #0x2a0]
// 0x10b7584: cbnz w11, #0x10b726c
// 0x10b7588: b #0x10b7454
// 0x10b758c: ldrb w9, [x8, #0x2e8]
// 0x10b7590: cbnz w9, #0x10b7330
// 0x10b7594: b #0x10b72cc
// 0x10b7598: str w11, [x19, #0x128]
// 0x10b759c: str w8, [x19, #0x12c]
// 0x10b75a0: mov w8, #1
// 0x10b75a4: strb w8, [x19, #0x3c5]
// 0x10b75a8: b #0x10b71ac
// 0x10b75ac: cbnz w11, #0x10b75b8
// 0x10b75b0: ldrb w11, [x8, #0x2e8]
// 0x10b75b4: cbnz w11, #0x10b75d0
// 0x10b75b8: ldr s0, [x21]
// 0x10b75bc: fcmp s0, #0.0
// 0x10b75c0: b.eq #0x10b75f8
// 0x10b75c4: b.vs #0x10b75f8
// 0x10b75c8: ldrb w11, [x8, #0x2dc]
// 0x10b75cc: cbz w11, #0x10b75f8
// 0x10b75d0: strb wzr, [x19, #0x3a7]
// 0x10b75d4: cbz w9, #0x10b75e0
// 0x10b75d8: ldrb w8, [x8, #0x147]
// 0x10b75dc: cbz w8, #0x10b75f0
// 0x10b75e0: cbz w10, #0x10b75f0
// 0x10b75e4: ldr s0, [x19, #0x204]
// 0x10b75e8: fcmp s0, #0.0
// 0x10b75ec: b.eq #0x10b7614
// 0x10b75f0: strb wzr, [x19, #0x3a4]
// 0x10b75f4: b #0x10b7224
// 0x10b75f8: ldrb w8, [x19, #0x3a7]
// 0x10b75fc: cbnz w8, #0x10b7614
// 0x10b7600: mov x0, xzr
// 0x10b7604: bl #0x1b9ad30
// 0x10b7608: mov w8, #1
// 0x10b760c: str s0, [x19, #0x3a8]
// 0x10b7610: strb w8, [x19, #0x3a7]
// 0x10b7614: mov w9, #1
// 0x10b7618: mov w8, wzr
// 0x10b761c: strb w9, [x19, #0x3a4]
// 0x10b7620: ldr x9, [x19, #0xa0]
// 0x10b7624: cbz x9, #0x10b8d8c
// 0x10b7628: ldrb w9, [x9, #0x89]
// 0x10b762c: cbz w9, #0x10b772c
// 0x10b7630: ldrb w9, [x19, #0x3ed]
// 0x10b7634: cmp w9, #0
// 0x10b7638: cset w9, eq
// 0x10b763c: orr w8, w9, w8
// 0x10b7640: tbnz w8, #0, #0x10b776c
// 0x10b7644: ldr w8, [x19, #0x12c]
// 0x10b7648: cmp w8, #0
// 0x10b764c: b.gt #0x10b776c
// 0x10b7650: ldrb w8, [x19, #0x1f6]
// 0x10b7654: cbz w8, #0x10b776c
// 0x10b7658: ldr w8, [x19, #0x128]
// 0x10b765c: cmp w8, #0
// 0x10b7660: b.gt #0x10b776c
// 0x10b7664: ldrb w8, [x19, #0x221]
// 0x10b7668: cbnz w8, #0x10b776c
// 0x10b766c: ldr x0, [x19, #0x108]
// 0x10b7670: cbz x0, #0x10b8d8c
// 0x10b7674: add x8, sp, #0x28
// 0x10b7678: mov w1, wzr
// 0x10b767c: mov x2, xzr
// 0x10b7680: bl #0x1b67df8
// 0x10b7684: ldur q0, [sp, #0x28]
// 0x10b7688: ldur q1, [sp, #0x38]
// 0x10b768c: ldr w8, [sp, #0x48]
// 0x10b7690: add x0, sp, #0x50
// 0x10b7694: mov x1, xzr
// 0x10b7698: stp q0, q1, [sp, #0x50]
// 0x10b769c: str w8, [sp, #0x70]
// 0x10b76a0: bl #0x1b67398
// 0x10b76a4: adrp x8, #0x832000
// 0x10b76a8: ldr s1, [x8, #0x440]
// 0x10b76ac: fcmp s0, s1
// 0x10b76b0: b.le #0x10b776c
// 0x10b76b4: ldr x0, [x19, #0x690]
// 0x10b76b8: cbz x0, #0x10b8d8c
// 0x10b76bc: fmov s0, #1.00000000
// 0x10b76c0: mov x1, xzr
// 0x10b76c4: bl #0x1b6a478
// 0x10b76c8: ldr x0, [x19, #0x690]
// 0x10b76cc: cbz x0, #0x10b8d8c
// 0x10b76d0: ldr x1, [x19, #0x6c0]
// 0x10b76d4: mov x2, xzr
// 0x10b76d8: bl #0x1b6a588
// 0x10b76dc: ldr x20, [x19, #0x690]
// 0x10b76e0: cbz x20, #0x10b8d8c
// 0x10b76e4: mov x0, x20
// 0x10b76e8: mov x1, xzr
// 0x10b76ec: bl #0x1b6a54c
// 0x10b76f0: ldr x8, [x19, #0x690]
// 0x10b76f4: cbz x8, #0x10b8d8c
// 0x10b76f8: mov x21, x0
// 0x10b76fc: mov x0, x8
// 0x10b7700: mov x1, xzr
// 0x10b7704: bl #0x1b6a43c
// 0x10b7708: fmov s1, #1.00000000
// 0x10b770c: fdiv s0, s1, s0
// 0x10b7710: mov x0, x20
// 0x10b7714: mov x1, x21
// 0x10b7718: mov x2, xzr
// 0x10b771c: bl #0x1b6a66c
// 0x10b7720: strb wzr, [x19, #0x3a5]
// 0x10b7724: strb wzr, [x19, #0x3ed]
// 0x10b7728: b #0x10b776c
// 0x10b772c: mov w8, #1
// 0x10b7730: mov x0, xzr
// 0x10b7734: strb w8, [x19, #0x3ed]
// 0x10b7738: strb wzr, [x19, #0x1f4]
// 0x10b773c: bl #0x1b9ad30
// 0x10b7740: ldr s1, [x19, #0x728]
// 0x10b7744: fsub s0, s0, s1
// 0x10b7748: fmov s1, #2.00000000
// 0x10b774c: fcmp s0, s1
// 0x10b7750: b.le #0x10b776c
// 0x10b7754: mov x0, xzr
// 0x10b7758: bl #0x1b69ac4
// 0x10b775c: mov x0, xzr
// 0x10b7760: str d0, [x19, #0x720]
// 0x10b7764: bl #0x1b9ad30
// 0x10b7768: str s0, [x19, #0x728]
// 0x10b776c: ldr x8, [x19, #0xa0]
// 0x10b7770: cbz x8, #0x10b8d8c
// 0x10b7774: ldrb w9, [x8, #0x8c]
// 0x10b7778: cbnz w9, #0x10b7784
// 0x10b777c: ldrb w8, [x8, #0xf2]
// 0x10b7780: cbz w8, #0x10b78b0
// 0x10b7784: ldrb w8, [x19, #0x1dd]
// 0x10b7788: cbz w8, #0x10b78b8
// 0x10b778c: ldrb w8, [x19, #0x3a4]
// 0x10b7790: cbz w8, #0x10b78b8
// 0x10b7794: ldr x8, [x19, #0x90]
// 0x10b7798: cbz x8, #0x10b8d8c
// 0x10b779c: ldrb w8, [x8, #0x129]
// 0x10b77a0: cbnz w8, #0x10b78b8
// 0x10b77a4: ldr x0, [x19, #0x108]
// 0x10b77a8: cbz x0, #0x10b8d8c
// 0x10b77ac: add x8, sp, #0x28
// 0x10b77b0: mov w1, wzr
// 0x10b77b4: mov x2, xzr
// 0x10b77b8: bl #0x1b67df8
// 0x10b77bc: ldur q0, [sp, #0x28]
// 0x10b77c0: ldur q1, [sp, #0x38]
// 0x10b77c4: ldr w8, [sp, #0x48]
// 0x10b77c8: add x0, sp, #0x50
// 0x10b77cc: mov x1, xzr
// 0x10b77d0: stp q0, q1, [sp, #0x50]
// 0x10b77d4: str w8, [sp, #0x70]
// 0x10b77d8: bl #0x1b67398
// 0x10b77dc: adrp x8, #0x832000
// 0x10b77e0: ldr s1, [x8, #0x440]
// 0x10b77e4: fcmp s0, s1
// 0x10b77e8: b.le #0x10b78b8
// 0x10b77ec: ldrb w8, [x19, #0x1dc]
// 0x10b77f0: strb wzr, [x19, #0x1e8]
// 0x10b77f4: str wzr, [x19, #0x1ec]
// 0x10b77f8: strb wzr, [x19, #0x192]
// 0x10b77fc: cbz w8, #0x10b78b8
// 0x10b7800: ldrb w8, [x19, #0x1de]
// 0x10b7804: cbz w8, #0x10b86fc
// 0x10b7808: add x8, x19, #0x1dd
// 0x10b780c: strh wzr, [x8]
// 0x10b7810: ldr w8, [x19, #0x154]
// 0x10b7814: ldr x0, [x19, #0x690]
// 0x10b7818: fmov s0, #6.50000000
// 0x10b781c: fmov s1, #2.00000000
// 0x10b7820: cmp w8, #1
// 0x10b7824: fcsel s0, s1, s0, gt
// 0x10b7828: str s0, [x19, #0x450]
// 0x10b782c: cbz x0, #0x10b8d8c
// 0x10b7830: fmov s0, #1.00000000
// 0x10b7834: mov x1, xzr
// 0x10b7838: bl #0x1b6a478
// 0x10b783c: ldr x0, [x19, #0x690]
// 0x10b7840: cbz x0, #0x10b8d8c
// 0x10b7844: ldr x1, [x19, #0x6c0]
// 0x10b7848: mov x2, xzr
// 0x10b784c: bl #0x1b6a588
// 0x10b7850: ldr x20, [x19, #0x690]
// 0x10b7854: cbz x20, #0x10b8d8c
// 0x10b7858: mov x0, x20
// 0x10b785c: mov x1, xzr
// 0x10b7860: bl #0x1b6a54c
// 0x10b7864: ldr x8, [x19, #0x690]
// 0x10b7868: cbz x8, #0x10b8d8c
// 0x10b786c: mov x21, x0
// 0x10b7870: mov x0, x8
// 0x10b7874: mov x1, xzr
// 0x10b7878: bl #0x1b6a43c
// 0x10b787c: fmov s1, #1.00000000
// 0x10b7880: fdiv s0, s1, s0
// 0x10b7884: mov x0, x20
// 0x10b7888: mov x1, x21
// 0x10b788c: mov x2, xzr
// 0x10b7890: bl #0x1b6a66c
// 0x10b7894: ldrb w8, [x19, #0x1e1]
// 0x10b7898: cbz w8, #0x10b78b8
// 0x10b789c: ldrb w8, [x19, #0x1e0]
// 0x10b78a0: cbnz w8, #0x10b78b8
// 0x10b78a4: mov w8, #1
// 0x10b78a8: strb w8, [x19, #0x1e0]
// 0x10b78ac: b #0x10b78b8
// 0x10b78b0: mov w8, #1
// 0x10b78b4: strb w8, [x19, #0x1dd]
// 0x10b78b8: mov x0, xzr
// 0x10b78bc: bl #0x1b9ad30
// 0x10b78c0: adrp x8, #0x832000
// 0x10b78c4: ldr s1, [x19, #0x1fc]
// 0x10b78c8: ldr s2, [x19, #0x150]
// 0x10b78cc: ldr s3, [x8, #0x4f4]
// 0x10b78d0: fsub s0, s0, s1
// 0x10b78d4: fadd s1, s2, s3
// 0x10b78d8: fcmp s0, s1
// 0x10b78dc: b.le #0x10b78e4
// 0x10b78e0: str wzr, [x19, #0x4cc]
// 0x10b78e4: ldrb w8, [x19, #0x3a4]
// 0x10b78e8: cbnz w8, #0x10b7934
// 0x10b78ec: ldr x8, [x19, #0x80]
// 0x10b78f0: cbz x8, #0x10b8d8c
// 0x10b78f4: ldrb w9, [x8, #0x1a0]
// 0x10b78f8: cbnz w9, #0x10b7934
// 0x10b78fc: ldrb w9, [x8, #0x2d0]
// 0x10b7900: cbnz w9, #0x10b7934
// 0x10b7904: ldr s0, [x8, #0x2cc]
// 0x10b7908: ldr s1, [x8, #0x3bc]
// 0x10b790c: fcmp s0, s1
// 0x10b7910: b.pl #0x10b791c
// 0x10b7914: ldrb w9, [x8, #0x2dd]
// 0x10b7918: cbnz w9, #0x10b7934
// 0x10b791c: ldr x9, [x19, #0x90]
// 0x10b7920: cbz x9, #0x10b8d8c
// 0x10b7924: ldrb w9, [x9, #0x129]
// 0x10b7928: cbnz w9, #0x10b7934
// 0x10b792c: ldrb w9, [x8, #0x2c2]
// 0x10b7930: cbz w9, #0x10b8714
// 0x10b7934: ldrb w8, [x19, #0x3a6]
// 0x10b7938: cbz w8, #0x10b7970
// 0x10b793c: ldr x20, [x19, #0x88]
// 0x10b7940: mov x0, xzr
// 0x10b7944: bl #0x1b9ad30
// 0x10b7948: cbz x20, #0x10b8d8c
// 0x10b794c: str s0, [x20, #0x124]
// 0x10b7950: ldr x0, [x19, #0x108]
// 0x10b7954: cbz x0, #0x10b8d8c
// 0x10b7958: adrp x8, #0x1e8e000
// 0x10b795c: ldr x8, [x8, #0x710]
// 0x10b7960: mov x2, xzr
// 0x10b7964: ldr x1, [x8]
// 0x10b7968: bl #0x1b67884
// 0x10b796c: strb wzr, [x19, #0x3a6]
// 0x10b7970: ldr x20, [x19, #0x690]
// 0x10b7974: mov x0, xzr
// 0x10b7978: bl #0x1b9ae58
// 0x10b797c: cbz x20, #0x10b8d8c
// 0x10b7980: mov x0, x20
// 0x10b7984: mov x1, xzr
// 0x10b7988: bl #0x1b6a500
// 0x10b798c: ldr x20, [x19, #0x688]
// 0x10b7990: ldr s8, [x19, #0x714]
// 0x10b7994: mov x0, xzr
// 0x10b7998: bl #0x1b9ae58
// 0x10b799c: cbz x20, #0x10b8d8c
// 0x10b79a0: fmul s0, s8, s0
// 0x10b79a4: mov x0, x20
// 0x10b79a8: mov x1, xzr
// 0x10b79ac: bl #0x1b6a500
// 0x10b79b0: ldr x0, [x19, #0x688]
// 0x10b79b4: cbz x0, #0x10b8d8c
// 0x10b79b8: ldr x20, [x19, #0x700]
// 0x10b79bc: mov x1, xzr
// 0x10b79c0: bl #0x1b6a4c4
// 0x10b79c4: cbz x20, #0x10b8d8c
// 0x10b79c8: mov x0, x20
// 0x10b79cc: mov x1, xzr
// 0x10b79d0: bl #0x1b6a500
// 0x10b79d4: ldr x0, [x19, #0x688]
// 0x10b79d8: cbz x0, #0x10b8d8c
// 0x10b79dc: ldr x20, [x19, #0x708]
// 0x10b79e0: mov x1, xzr
// 0x10b79e4: bl #0x1b6a4c4
// 0x10b79e8: cbz x20, #0x10b8d8c
// 0x10b79ec: mov x0, x20
// 0x10b79f0: mov x1, xzr
// 0x10b79f4: bl #0x1b6a500
// 0x10b79f8: mov x0, xzr
// 0x10b79fc: bl #0x1b9ae58
// 0x10b7a00: fcmp s0, #0.0
// 0x10b7a04: b.le #0x10b807c
// 0x10b7a08: ldr x8, [x19, #0xb8]
// 0x10b7a0c: cbz x8, #0x10b8d8c
// 0x10b7a10: ldrb w8, [x8, #0x106]
// 0x10b7a14: cbz w8, #0x10b7a6c
// 0x10b7a18: ldr x1, [x19, #0x480]
// 0x10b7a1c: add x0, x19, #0x488
// 0x10b7a20: str x1, [x19, #0x488]
// 0x10b7a24: bl #0xf7d8d0
// 0x10b7a28: adrp x8, #0x1e8c000
// 0x10b7a2c: ldr x8, [x8, #0xd8]
// 0x10b7a30: ldr x20, [x19, #0x478]
// 0x10b7a34: ldr x0, [x8]
// 0x10b7a38: ldr w8, [x0, #0xe0]
// 0x10b7a3c: cbnz w8, #0x10b7a44
// 0x10b7a40: bl #0xf7da5c
// 0x10b7a44: mov x0, x20
// 0x10b7a48: mov x1, xzr
// 0x10b7a4c: bl #0x1b98274
// 0x10b7a50: tbz w0, #0, #0x10b7a7c
// 0x10b7a54: ldr x0, [x19, #0x478]
// 0x10b7a58: cbz x0, #0x10b8d8c
// 0x10b7a5c: mov w1, wzr
// 0x10b7a60: mov x2, xzr
// 0x10b7a64: bl #0x1b799d0
// 0x10b7a68: b #0x10b7a7c
// 0x10b7a6c: ldr x1, [x19, #0x478]
// 0x10b7a70: add x0, x19, #0x488
// 0x10b7a74: str x1, [x19, #0x488]
// 0x10b7a78: bl #0xf7d8d0
// 0x10b7a7c: ldrb w8, [x19, #0x1f5]
// 0x10b7a80: cbz w8, #0x10b7edc
// 0x10b7a84: mov x0, xzr
// 0x10b7a88: bl #0x1b9ae30
// 0x10b7a8c: fcmp s0, #0.0
// 0x10b7a90: b.le #0x10b7c3c
// 0x10b7a94: ldrb w8, [x19, #0x1f5]
// 0x10b7a98: cbnz w8, #0x10b7c3c
// 0x10b7a9c: ldr s9, [x19, #0x398]
// 0x10b7aa0: ldr s8, [x19, #0x38c]
// 0x10b7aa4: mov x0, xzr
// 0x10b7aa8: add x20, x19, #0x380
// 0x10b7aac: bl #0x1b9ae30
// 0x10b7ab0: mov w8, #0x43b40000
// 0x10b7ab4: mov v4.16b, v0.16b
// 0x10b7ab8: fsub s0, s8, s9
// 0x10b7abc: fmov s1, w8
// 0x10b7ac0: mov w8, #-0x3c4c0000
// 0x10b7ac4: fdiv s2, s0, s1
// 0x10b7ac8: fmov s3, w8
// 0x10b7acc: frintm s2, s2
// 0x10b7ad0: fmul s2, s2, s3
// 0x10b7ad4: fadd s0, s0, s2
// 0x10b7ad8: mov w8, #0x43340000
// 0x10b7adc: fmin s1, s0, s1
// 0x10b7ae0: fcmp s0, #0.0
// 0x10b7ae4: fmov s0, w8
// 0x10b7ae8: adrp x8, #0x832000
// 0x10b7aec: fmov s11, wzr
// 0x10b7af0: ldr s8, [x8, #0x4e8]
// 0x10b7af4: fcsel s1, s1, s11, pl
// 0x10b7af8: fadd s2, s1, s3
// 0x10b7afc: fcmp s1, s0
// 0x10b7b00: fcsel s0, s2, s1, gt
// 0x10b7b04: mov w8, #0x7f800000
// 0x10b7b08: fadd s1, s9, s0
// 0x10b7b0c: fmov s3, w8
// 0x10b7b10: mov v0.16b, v9.16b
// 0x10b7b14: mov x0, x20
// 0x10b7b18: mov v2.16b, v8.16b
// 0x10b7b1c: mov x1, xzr
// 0x10b7b20: bl #0x1b8c860
// 0x10b7b24: ldr x8, [x19, #0xc0]
// 0x10b7b28: str s0, [x19, #0x398]
// 0x10b7b2c: cbz x8, #0x10b8d8c
// 0x10b7b30: ldr s9, [x19, #0x39c]
// 0x10b7b34: ldr s10, [x19, #0x390]
// 0x10b7b38: ldr s12, [x8, #0xb8]
// 0x10b7b3c: mov x0, xzr
// 0x10b7b40: add x20, x19, #0x384
// 0x10b7b44: bl #0x1b9ae30
// 0x10b7b48: mov v4.16b, v0.16b
// 0x10b7b4c: mov w8, #0x43b40000
// 0x10b7b50: fadd s0, s10, s12
// 0x10b7b54: fmov s13, w8
// 0x10b7b58: fsub s0, s0, s9
// 0x10b7b5c: mov w8, #-0x3c4c0000
// 0x10b7b60: fdiv s1, s0, s13
// 0x10b7b64: fmov s12, w8
// 0x10b7b68: frintm s1, s1
// 0x10b7b6c: fmul s1, s1, s12
// 0x10b7b70: fadd s0, s0, s1
// 0x10b7b74: mov w8, #0x43340000
// 0x10b7b78: fmin s1, s0, s13
// 0x10b7b7c: fcmp s0, #0.0
// 0x10b7b80: fmov s14, w8
// 0x10b7b84: fcsel s0, s1, s11, pl
// 0x10b7b88: fadd s1, s0, s12
// 0x10b7b8c: fcmp s0, s14
// 0x10b7b90: mov w8, #0x7f800000
// 0x10b7b94: fcsel s0, s1, s0, gt
// 0x10b7b98: fmov s10, w8
// 0x10b7b9c: fadd s1, s9, s0
// 0x10b7ba0: mov v0.16b, v9.16b
// 0x10b7ba4: mov x0, x20
// 0x10b7ba8: mov v2.16b, v8.16b
// 0x10b7bac: mov v3.16b, v10.16b
// 0x10b7bb0: mov x1, xzr
// 0x10b7bb4: bl #0x1b8c860
// 0x10b7bb8: ldr s9, [x19, #0x3a0]
// 0x10b7bbc: ldr s15, [x19, #0x394]
// 0x10b7bc0: mov x0, xzr
// 0x10b7bc4: str s0, [x19, #0x39c]
// 0x10b7bc8: add x20, x19, #0x388
// 0x10b7bcc: bl #0x1b9ae30
// 0x10b7bd0: mov v4.16b, v0.16b
// 0x10b7bd4: fsub s0, s15, s9
// 0x10b7bd8: fdiv s1, s0, s13
// 0x10b7bdc: frintm s1, s1
// 0x10b7be0: fmul s1, s1, s12
// 0x10b7be4: fadd s0, s0, s1
// 0x10b7be8: fmin s1, s0, s13
// 0x10b7bec: fcmp s0, #0.0
// 0x10b7bf0: fcsel s0, s1, s11, pl
// 0x10b7bf4: fadd s1, s0, s12
// 0x10b7bf8: fcmp s0, s14
// 0x10b7bfc: fcsel s0, s1, s0, gt
// 0x10b7c00: fadd s1, s9, s0
// 0x10b7c04: mov v0.16b, v9.16b
// 0x10b7c08: mov x0, x20
// 0x10b7c0c: mov v2.16b, v8.16b
// 0x10b7c10: mov v3.16b, v10.16b
// 0x10b7c14: mov x1, xzr
// 0x10b7c18: bl #0x1b8c860
// 0x10b7c1c: ldr x0, [x19, #0x70]
// 0x10b7c20: str s0, [x19, #0x3a0]
// 0x10b7c24: cbz x0, #0x10b8d8c
// 0x10b7c28: mov v2.16b, v0.16b
// 0x10b7c2c: ldr s1, [x19, #0x39c]
// 0x10b7c30: ldr s0, [x19, #0x398]
// 0x10b7c34: mov x1, xzr
// 0x10b7c38: bl #0x1b9d848
// 0x10b7c3c: ldrb w8, [x19, #0x72d]
// 0x10b7c40: cbz w8, #0x10b807c
// 0x10b7c44: ldr x8, [x19, #0xb8]
// 0x10b7c48: cbz x8, #0x10b8d8c
// 0x10b7c4c: ldrb w8, [x8, #0x106]
// 0x10b7c50: cbz w8, #0x10b7c64
// 0x10b7c54: ldr x8, [x19, #0x98]
// 0x10b7c58: cbz x8, #0x10b8d8c
// 0x10b7c5c: ldrb w8, [x8, #0x2d0]
// 0x10b7c60: cbz w8, #0x10b80a0
// 0x10b7c64: ldr x0, [x19, #0x748]
// 0x10b7c68: cbz x0, #0x10b8d8c
// 0x10b7c6c: mov x1, xzr
// 0x10b7c70: bl #0x1b92154
// 0x10b7c74: ldr x8, [x19, #0x78]
// 0x10b7c78: cbz x8, #0x10b8d8c
// 0x10b7c7c: mov x20, x0
// 0x10b7c80: mov x0, x8
// 0x10b7c84: mov x1, xzr
// 0x10b7c88: bl #0x1b9d508
// 0x10b7c8c: cbz x20, #0x10b8d8c
// 0x10b7c90: mov x0, x20
// 0x10b7c94: mov x1, xzr
// 0x10b7c98: bl #0x1b9d5a8
// 0x10b7c9c: ldr x0, [x19, #0x748]
// 0x10b7ca0: cbz x0, #0x10b8d8c
// 0x10b7ca4: mov x1, xzr
// 0x10b7ca8: bl #0x1b92154
// 0x10b7cac: ldr x8, [x19, #0x730]
// 0x10b7cb0: cbz x8, #0x10b8d8c
// 0x10b7cb4: mov x20, x0
// 0x10b7cb8: mov x0, x8
// 0x10b7cbc: mov x1, xzr
// 0x10b7cc0: bl #0x1b9d6f0
// 0x10b7cc4: cbz x20, #0x10b8d8c
// 0x10b7cc8: mov x0, x20
// 0x10b7ccc: mov x1, xzr
// 0x10b7cd0: bl #0x1b9d774
// 0x10b7cd4: ldrb w8, [x19, #0x738]
// 0x10b7cd8: cbz w8, #0x10b7da0
// 0x10b7cdc: ldr x0, [x19, #0x748]
// 0x10b7ce0: cbz x0, #0x10b8d8c
// 0x10b7ce4: mov x1, xzr
// 0x10b7ce8: bl #0x1b92154
// 0x10b7cec: cbz x0, #0x10b8d8c
// 0x10b7cf0: mov x1, xzr
// 0x10b7cf4: mov x20, x0
// 0x10b7cf8: bl #0x1b9d6f0
// 0x10b7cfc: adrp x8, #0x832000
// 0x10b7d00: mov v9.16b, v1.16b
// 0x10b7d04: ldr s1, [x8, #0x300]
// 0x10b7d08: mov v8.16b, v0.16b
// 0x10b7d0c: mov v10.16b, v2.16b
// 0x10b7d10: fmov s0, wzr
// 0x10b7d14: fmov s2, wzr
// 0x10b7d18: mov x0, xzr
// 0x10b7d1c: mov v11.16b, v3.16b
// 0x10b7d20: bl #0x1b8b12c
// 0x10b7d24: fmul s4, s11, s0
// 0x10b7d28: fmul s5, s8, s3
// 0x10b7d2c: fmul s7, s10, s1
// 0x10b7d30: fmul s16, s11, s1
// 0x10b7d34: fmul s17, s9, s3
// 0x10b7d38: fmul s18, s10, s0
// 0x10b7d3c: fmul s20, s8, s1
// 0x10b7d40: fmul s21, s8, s0
// 0x10b7d44: fmul s22, s9, s0
// 0x10b7d48: fmul s0, s9, s1
// 0x10b7d4c: fmul s1, s11, s2
// 0x10b7d50: fmul s23, s11, s3
// 0x10b7d54: fmul s3, s10, s3
// 0x10b7d58: fmul s6, s9, s2
// 0x10b7d5c: fmul s19, s8, s2
// 0x10b7d60: fmul s24, s10, s2
// 0x10b7d64: fadd s2, s4, s5
// 0x10b7d68: fadd s4, s16, s17
// 0x10b7d6c: fadd s1, s1, s3
// 0x10b7d70: fsub s3, s23, s21
// 0x10b7d74: fadd s2, s6, s2
// 0x10b7d78: fadd s4, s18, s4
// 0x10b7d7c: fadd s5, s20, s1
// 0x10b7d80: fsub s3, s3, s0
// 0x10b7d84: fsub s0, s2, s7
// 0x10b7d88: fsub s1, s4, s19
// 0x10b7d8c: fsub s2, s5, s22
// 0x10b7d90: fsub s3, s3, s24
// 0x10b7d94: mov x0, x20
// 0x10b7d98: mov x1, xzr
// 0x10b7d9c: bl #0x1b9d774
// 0x10b7da0: ldr x8, [x19, #0xa0]
// 0x10b7da4: cbz x8, #0x10b8d8c
// 0x10b7da8: ldrb w9, [x8, #0x9e]
// 0x10b7dac: cbz w9, #0x10b7fbc
// 0x10b7db0: ldr x0, [x19, #0x690]
// 0x10b7db4: cbz x0, #0x10b8d8c
// 0x10b7db8: fmov s0, #1.00000000
// 0x10b7dbc: mov x1, xzr
// 0x10b7dc0: bl #0x1b6a478
// 0x10b7dc4: ldr x0, [x19, #0x690]
// 0x10b7dc8: cbz x0, #0x10b8d8c
// 0x10b7dcc: ldr x1, [x19, #0x6c0]
// 0x10b7dd0: mov x2, xzr
// 0x10b7dd4: bl #0x1b6a588
// 0x10b7dd8: ldr x20, [x19, #0x690]
// 0x10b7ddc: cbz x20, #0x10b8d8c
// 0x10b7de0: mov x0, x20
// 0x10b7de4: mov x1, xzr
// 0x10b7de8: bl #0x1b6a54c
// 0x10b7dec: ldr x8, [x19, #0x690]
// 0x10b7df0: cbz x8, #0x10b8d8c
// 0x10b7df4: mov x21, x0
// 0x10b7df8: mov x0, x8
// 0x10b7dfc: mov x1, xzr
// 0x10b7e00: bl #0x1b6a43c
// 0x10b7e04: fmov s1, #1.00000000
// 0x10b7e08: fdiv s0, s1, s0
// 0x10b7e0c: mov x0, x20
// 0x10b7e10: mov x1, x21
// 0x10b7e14: mov x2, xzr
// 0x10b7e18: bl #0x1b6a66c
// 0x10b7e1c: adrp x21, #0x1e8c000
// 0x10b7e20: ldr x21, [x21, #0xd8]
// 0x10b7e24: ldrb w22, [x19, #0x73b]
// 0x10b7e28: ldr x20, [x19, #0x740]
// 0x10b7e2c: ldr x0, [x21]
// 0x10b7e30: ldr w8, [x0, #0xe0]
// 0x10b7e34: cbnz w8, #0x10b7e3c
// 0x10b7e38: bl #0xf7da5c
// 0x10b7e3c: mov x0, x20
// 0x10b7e40: mov x1, xzr
// 0x10b7e44: bl #0x1b98274
// 0x10b7e48: cbz w22, #0x10b7fec
// 0x10b7e4c: tbz w0, #0, #0x10b7e64
// 0x10b7e50: ldr x0, [x19, #0x740]
// 0x10b7e54: cbz x0, #0x10b8d8c
// 0x10b7e58: mov w1, wzr
// 0x10b7e5c: mov x2, xzr
// 0x10b7e60: bl #0x1b799d0
// 0x10b7e64: ldr x0, [x21]
// 0x10b7e68: ldr x20, [x19, #0x748]
// 0x10b7e6c: ldr w8, [x0, #0xe0]
// 0x10b7e70: cbnz w8, #0x10b7e78
// 0x10b7e74: bl #0xf7da5c
// 0x10b7e78: mov x0, x20
// 0x10b7e7c: mov x1, xzr
// 0x10b7e80: bl #0x1b98274
// 0x10b7e84: tbz w0, #0, #0x10b7e9c
// 0x10b7e88: ldr x0, [x19, #0x748]
// 0x10b7e8c: cbz x0, #0x10b8d8c
// 0x10b7e90: mov w1, wzr
// 0x10b7e94: mov x2, xzr
// 0x10b7e98: bl #0x1b91660
// 0x10b7e9c: ldr x0, [x21]
// 0x10b7ea0: ldr x20, [x19, #0x750]
// 0x10b7ea4: ldr w8, [x0, #0xe0]
// 0x10b7ea8: cbnz w8, #0x10b7eb0
// 0x10b7eac: bl #0xf7da5c
// 0x10b7eb0: mov x0, x20
// 0x10b7eb4: mov x1, xzr
// 0x10b7eb8: bl #0x1b98274
// 0x10b7ebc: tbz w0, #0, #0x10b7ed4
// 0x10b7ec0: ldr x0, [x19, #0x750]
// 0x10b7ec4: cbz x0, #0x10b8d8c
// 0x10b7ec8: mov w1, wzr
// 0x10b7ecc: mov x2, xzr
// 0x10b7ed0: bl #0x1b91660
// 0x10b7ed4: strb wzr, [x19, #0x73b]
// 0x10b7ed8: b #0x10b807c
// 0x10b7edc: ldr x8, [x19, #0x98]
// 0x10b7ee0: cbz x8, #0x10b8d8c
// 0x10b7ee4: ldr s0, [x8, #0x20c]
// 0x10b7ee8: fcmp s0, #0.0
// 0x10b7eec: b.le #0x10b7fd0
// 0x10b7ef0: adrp x21, #0x1e8c000
// 0x10b7ef4: ldr x21, [x21, #0xd8]
// 0x10b7ef8: ldr x20, [x19, #0x448]
// 0x10b7efc: ldr x0, [x21]
// 0x10b7f00: ldr w8, [x0, #0xe0]
// 0x10b7f04: cbnz w8, #0x10b7f0c
// 0x10b7f08: bl #0xf7da5c
// 0x10b7f0c: mov x0, x20
// 0x10b7f10: mov x1, xzr
// 0x10b7f14: bl #0x1b98274
// 0x10b7f18: tbz w0, #0, #0x10b822c
// 0x10b7f1c: ldr x0, [x21]
// 0x10b7f20: ldr x20, [x19, #0x488]
// 0x10b7f24: ldr w8, [x0, #0xe0]
// 0x10b7f28: cbnz w8, #0x10b7f30
// 0x10b7f2c: bl #0xf7da5c
// 0x10b7f30: mov x0, x20
// 0x10b7f34: mov x1, xzr
// 0x10b7f38: bl #0x1b98274
// 0x10b7f3c: tbz w0, #0, #0x10b8264
// 0x10b7f40: ldr x0, [x19, #0x488]
// 0x10b7f44: cbz x0, #0x10b8d8c
// 0x10b7f48: mov x1, xzr
// 0x10b7f4c: bl #0x1b79994
// 0x10b7f50: tbz w0, #0, #0x10b8264
// 0x10b7f54: ldr s8, [x19, #0x460]
// 0x10b7f58: fcmp s8, #0.0
// 0x10b7f5c: b.le #0x10b8250
// 0x10b7f60: ldr s9, [x19, #0x450]
// 0x10b7f64: mov x0, xzr
// 0x10b7f68: bl #0x1b89b60
// 0x10b7f6c: ldr x0, [x19, #0x488]
// 0x10b7f70: fmul s0, s9, s0
// 0x10b7f74: fsub s0, s8, s0
// 0x10b7f78: fmov s1, wzr
// 0x10b7f7c: fmax s0, s0, s1
// 0x10b7f80: str s0, [x19, #0x460]
// 0x10b7f84: cbz x0, #0x10b8d8c
// 0x10b7f88: mov x1, xzr
// 0x10b7f8c: bl #0x1b79b88
// 0x10b7f90: cbz x0, #0x10b8d8c
// 0x10b7f94: adrp x8, #0x1e8e000
// 0x10b7f98: ldr s3, [x19, #0x460]
// 0x10b7f9c: ldr s2, [x19, #0x45c]
// 0x10b7fa0: ldr s1, [x19, #0x458]
// 0x10b7fa4: ldr s0, [x19, #0x454]
// 0x10b7fa8: ldr x8, [x8, #0x6d8]
// 0x10b7fac: mov x2, xzr
// 0x10b7fb0: ldr x1, [x8]
// 0x10b7fb4: bl #0x1b7a790
// 0x10b7fb8: b #0x10b8264
// 0x10b7fbc: ldrb w9, [x19, #0x73a]
// 0x10b7fc0: cbz w9, #0x10b807c
// 0x10b7fc4: ldrb w8, [x8, #0x93]
// 0x10b7fc8: cbnz w8, #0x10b7db0
// 0x10b7fcc: b #0x10b807c
// 0x10b7fd0: b.hi #0x10b7a84
// 0x10b7fd4: ldrb w8, [x19, #0x192]
// 0x10b7fd8: cbz w8, #0x10b7a84
// 0x10b7fdc: ldr x8, [x19, #0x88]
// 0x10b7fe0: cbz x8, #0x10b8d8c
// 0x10b7fe4: strb wzr, [x8, #0x17e]
// 0x10b7fe8: b #0x10b7a84
// 0x10b7fec: tbz w0, #0, #0x10b8004
// 0x10b7ff0: ldr x0, [x19, #0x740]
// 0x10b7ff4: cbz x0, #0x10b8d8c
// 0x10b7ff8: mov w1, #1
// 0x10b7ffc: mov x2, xzr
// 0x10b8000: bl #0x1b799d0
// 0x10b8004: ldr x0, [x21]
// 0x10b8008: ldr x20, [x19, #0x748]
// 0x10b800c: ldr w8, [x0, #0xe0]
// 0x10b8010: cbnz w8, #0x10b8018
// 0x10b8014: bl #0xf7da5c
// 0x10b8018: mov x0, x20
// 0x10b801c: mov x1, xzr
// 0x10b8020: bl #0x1b98274
// 0x10b8024: tbz w0, #0, #0x10b803c
// 0x10b8028: ldr x0, [x19, #0x748]
// 0x10b802c: cbz x0, #0x10b8d8c
// 0x10b8030: mov w1, #1
// 0x10b8034: mov x2, xzr
// 0x10b8038: bl #0x1b91660
// 0x10b803c: ldr x0, [x21]
// 0x10b8040: ldr x20, [x19, #0x750]
// 0x10b8044: ldr w8, [x0, #0xe0]
// 0x10b8048: cbnz w8, #0x10b8050
// 0x10b804c: bl #0xf7da5c
// 0x10b8050: mov x0, x20
// 0x10b8054: mov x1, xzr
// 0x10b8058: bl #0x1b98274
// 0x10b805c: tbz w0, #0, #0x10b8074
// 0x10b8060: ldr x0, [x19, #0x750]
// 0x10b8064: cbz x0, #0x10b8d8c
// 0x10b8068: mov w1, #1
// 0x10b806c: mov x2, xzr
// 0x10b8070: bl #0x1b91660
// 0x10b8074: mov w8, #1
// 0x10b8078: strb w8, [x19, #0x73b]
// 0x10b807c: ldp x20, x19, [sp, #0xe0]
// 0x10b8080: ldp x22, x21, [sp, #0xd0]
// 0x10b8084: ldp x30, x23, [sp, #0xc0]
// 0x10b8088: ldp d9, d8, [sp, #0xb0]
// 0x10b808c: ldp d11, d10, [sp, #0xa0]
// 0x10b8090: ldp d13, d12, [sp, #0x90]
// 0x10b8094: ldp d15, d14, [sp, #0x80]
// 0x10b8098: add sp, sp, #0xf0
// 0x10b809c: ret
// 0x10b80a0: adrp x8, #0x1e8c000
// 0x10b80a4: ldr x8, [x8, #0xd8]
// 0x10b80a8: ldr x20, [x19, #0xd0]
// 0x10b80ac: ldr x0, [x8]
// 0x10b80b0: ldr w8, [x0, #0xe0]
// 0x10b80b4: cbnz w8, #0x10b80bc
// 0x10b80b8: bl #0xf7da5c
// 0x10b80bc: mov x0, x20
// 0x10b80c0: mov x1, xzr
// 0x10b80c4: bl #0x1b98274
// 0x10b80c8: tbz w0, #0, #0x10b7da0
// 0x10b80cc: ldr x0, [x19, #0x748]
// 0x10b80d0: cbz x0, #0x10b8d8c
// 0x10b80d4: mov x1, xzr
// 0x10b80d8: bl #0x1b92154
// 0x10b80dc: ldr x8, [x19, #0xd0]
// 0x10b80e0: cbz x8, #0x10b8d8c
// 0x10b80e4: mov x20, x0
// 0x10b80e8: mov x0, x8
// 0x10b80ec: mov x1, xzr
// 0x10b80f0: bl #0x1b92154
// 0x10b80f4: cbz x0, #0x10b8d8c
// 0x10b80f8: mov x1, xzr
// 0x10b80fc: bl #0x1b9d508
// 0x10b8100: ldr x0, [x19, #0xd0]
// 0x10b8104: cbz x0, #0x10b8d8c
// 0x10b8108: mov x1, xzr
// 0x10b810c: mov v8.16b, v0.16b
// 0x10b8110: mov v9.16b, v1.16b
// 0x10b8114: mov v10.16b, v2.16b
// 0x10b8118: bl #0x1b92154
// 0x10b811c: cbz x0, #0x10b8d8c
// 0x10b8120: mov x1, xzr
// 0x10b8124: bl #0x1b9d9b8
// 0x10b8128: ldr x0, [x19, #0xd0]
// 0x10b812c: cbz x0, #0x10b8d8c
// 0x10b8130: mov x1, xzr
// 0x10b8134: mov v11.16b, v2.16b
// 0x10b8138: mov v13.16b, v1.16b
// 0x10b813c: mov v12.16b, v0.16b
// 0x10b8140: str s10, [sp, #0x10]
// 0x10b8144: mov v10.16b, v9.16b
// 0x10b8148: mov v9.16b, v8.16b
// 0x10b814c: bl #0x1b92154
// 0x10b8150: cbz x0, #0x10b8d8c
// 0x10b8154: mov x1, xzr
// 0x10b8158: bl #0x1b9d940
// 0x10b815c: ldr x0, [x19, #0xd0]
// 0x10b8160: cbz x0, #0x10b8d8c
// 0x10b8164: mov x1, xzr
// 0x10b8168: mov v14.16b, v0.16b
// 0x10b816c: mov v15.16b, v1.16b
// 0x10b8170: mov v8.16b, v2.16b
// 0x10b8174: bl #0x1b92154
// 0x10b8178: cbz x0, #0x10b8d8c
// 0x10b817c: mov x1, xzr
// 0x10b8180: bl #0x1b9d8c8
// 0x10b8184: cbz x20, #0x10b8d8c
// 0x10b8188: adrp x8, #0x832000
// 0x10b818c: ldr s7, [x8, #0x3e0]
// 0x10b8190: ldr s17, [sp, #0x10]
// 0x10b8194: fmov s4, #0.50000000
// 0x10b8198: fmov s3, #0.50000000
// 0x10b819c: fmul s2, s2, s4
// 0x10b81a0: fmul s1, s1, s4
// 0x10b81a4: fmul s0, s0, s4
// 0x10b81a8: fmul s4, s12, s7
// 0x10b81ac: fmul s16, s13, s7
// 0x10b81b0: fmul s7, s11, s7
// 0x10b81b4: fmul s5, s14, s3
// 0x10b81b8: fmul s6, s15, s3
// 0x10b81bc: fmul s3, s8, s3
// 0x10b81c0: fsub s4, s9, s4
// 0x10b81c4: fsub s16, s10, s16
// 0x10b81c8: fsub s7, s17, s7
// 0x10b81cc: fadd s4, s4, s5
// 0x10b81d0: fadd s5, s16, s6
// 0x10b81d4: fadd s3, s7, s3
// 0x10b81d8: fadd s2, s3, s2
// 0x10b81dc: fadd s1, s5, s1
// 0x10b81e0: fadd s0, s4, s0
// 0x10b81e4: mov x0, x20
// 0x10b81e8: mov x1, xzr
// 0x10b81ec: bl #0x1b9d5a8
// 0x10b81f0: ldr x0, [x19, #0x748]
// 0x10b81f4: cbz x0, #0x10b8d8c
// 0x10b81f8: mov x1, xzr
// 0x10b81fc: bl #0x1b92154
// 0x10b8200: ldr x8, [x19, #0xd0]
// 0x10b8204: cbz x8, #0x10b8d8c
// 0x10b8208: mov x20, x0
// 0x10b820c: mov x0, x8
// 0x10b8210: mov x1, xzr
// 0x10b8214: bl #0x1b92154
// 0x10b8218: cbz x0, #0x10b8d8c
// 0x10b821c: mov x1, xzr
// 0x10b8220: bl #0x1b9d6f0
// 0x10b8224: cbnz x20, #0x10b7d94
// 0x10b8228: b #0x10b8d8c
// 0x10b822c: ldr x0, [x21]
// 0x10b8230: ldr x20, [x19, #0x448]
// 0x10b8234: ldr w8, [x0, #0xe0]
// 0x10b8238: cbnz w8, #0x10b8240
// 0x10b823c: bl #0xf7da5c
// 0x10b8240: mov x0, x20
// 0x10b8244: mov x1, xzr
// 0x10b8248: bl #0x1b98274
// 0x10b824c: tbz w0, #0, #0x10b8264
// 0x10b8250: ldr x0, [x19, #0x488]
// 0x10b8254: cbz x0, #0x10b8d8c
// 0x10b8258: mov w1, wzr
// 0x10b825c: mov x2, xzr
// 0x10b8260: bl #0x1b799d0
// 0x10b8264: ldr x0, [x21]
// 0x10b8268: ldr x20, [x19, #0x468]
// 0x10b826c: ldr w8, [x0, #0xe0]
// 0x10b8270: cbnz w8, #0x10b8278
// 0x10b8274: bl #0xf7da5c
// 0x10b8278: mov x0, x20
// 0x10b827c: mov x1, xzr
// 0x10b8280: bl #0x1b98274
// 0x10b8284: tbz w0, #0, #0x10b834c
// 0x10b8288: ldr x8, [x19, #0xb8]
// 0x10b828c: cbz x8, #0x10b8d8c
// 0x10b8290: ldr x0, [x19, #0x490]
// 0x10b8294: cbz x0, #0x10b8d8c
// 0x10b8298: ldrb w8, [x8, #0x106]
// 0x10b829c: cbz w8, #0x10b82c4
// 0x10b82a0: mov w1, wzr
// 0x10b82a4: mov x2, xzr
// 0x10b82a8: bl #0x1b91660
// 0x10b82ac: ldr x0, [x19, #0x490]
// 0x10b82b0: cbz x0, #0x10b8d8c
// 0x10b82b4: fmov s0, wzr
// 0x10b82b8: mov x1, xzr
// 0x10b82bc: bl #0x1b7bccc
// 0x10b82c0: b #0x10b834c
// 0x10b82c4: mov x1, xzr
// 0x10b82c8: bl #0x1b91624
// 0x10b82cc: tbz w0, #0, #0x10b834c
// 0x10b82d0: ldr x0, [x19, #0x490]
// 0x10b82d4: cbz x0, #0x10b8d8c
// 0x10b82d8: mov x1, xzr
// 0x10b82dc: bl #0x1b7bc90
// 0x10b82e0: fcmp s0, #0.0
// 0x10b82e4: b.le #0x10b8338
// 0x10b82e8: mov x0, xzr
// 0x10b82ec: bl #0x1b9ad30
// 0x10b82f0: ldr s1, [x19, #0x1fc]
// 0x10b82f4: ldr s2, [x19, #0x470]
// 0x10b82f8: fsub s0, s0, s1
// 0x10b82fc: fcmp s0, s2
// 0x10b8300: b.le #0x10b834c
// 0x10b8304: ldr x20, [x19, #0x490]
// 0x10b8308: cbz x20, #0x10b8d8c
// 0x10b830c: mov x0, x20
// 0x10b8310: mov x1, xzr
// 0x10b8314: bl #0x1b7bc90
// 0x10b8318: ldr s9, [x19, #0x474]
// 0x10b831c: mov x0, xzr
// 0x10b8320: mov v8.16b, v0.16b
// 0x10b8324: bl #0x1b89b60
// 0x10b8328: fmul s0, s9, s0
// 0x10b832c: fsub s0, s8, s0
// 0x10b8330: mov x0, x20
// 0x10b8334: b #0x10b82b8
// 0x10b8338: ldr x0, [x19, #0x490]
// 0x10b833c: cbz x0, #0x10b8d8c
// 0x10b8340: mov w1, wzr
// 0x10b8344: mov x2, xzr
// 0x10b8348: bl #0x1b91660
// 0x10b834c: ldr x8, [x19, #0xa0]
// 0x10b8350: cbz x8, #0x10b8d8c
// 0x10b8354: ldrb w8, [x8, #0x8b]
// 0x10b8358: cbz w8, #0x10b836c
// 0x10b835c: ldr x8, [x19, #0x90]
// 0x10b8360: cbz x8, #0x10b8d8c
// 0x10b8364: ldrb w8, [x8, #0x129]
// 0x10b8368: cbz w8, #0x10b8688
// 0x10b836c: ldrb w8, [x19, #0x190]
// 0x10b8370: cbz w8, #0x10b8a64
// 0x10b8374: ldr w8, [x19, #0x128]
// 0x10b8378: cmp w8, #1
// 0x10b837c: b.lt #0x10b8a64
// 0x10b8380: ldrb w8, [x19, #0x229]
// 0x10b8384: cbnz w8, #0x10b8a64
// 0x10b8388: ldr x8, [x19, #0xb8]
// 0x10b838c: cbz x8, #0x10b8d8c
// 0x10b8390: ldrb w8, [x8, #0x1a5]
// 0x10b8394: cbnz w8, #0x10b8a64
// 0x10b8398: ldr x8, [x19, #0x88]
// 0x10b839c: cbz x8, #0x10b8d8c
// 0x10b83a0: ldrb w9, [x8, #0x129]
// 0x10b83a4: cbnz w9, #0x10b8a64
// 0x10b83a8: ldr x9, [x19, #0x80]
// 0x10b83ac: cbz x9, #0x10b8d8c
// 0x10b83b0: ldrb w10, [x9, #0x198]
// 0x10b83b4: cbnz w10, #0x10b8a64
// 0x10b83b8: ldrb w9, [x9, #0x1a0]
// 0x10b83bc: cbnz w9, #0x10b8a64
// 0x10b83c0: ldrb w9, [x19, #0x346]
// 0x10b83c4: cbnz w9, #0x10b8a64
// 0x10b83c8: ldr x9, [x19, #0xa0]
// 0x10b83cc: cbz x9, #0x10b8d8c
// 0x10b83d0: ldrb w9, [x9, #0x89]
// 0x10b83d4: cbz w9, #0x10b83e0
// 0x10b83d8: ldrb w9, [x8, #0x17e]
// 0x10b83dc: cbz w9, #0x10b83f8
// 0x10b83e0: ldr w9, [x19, #0x124]
// 0x10b83e4: ldr w10, [x8, #0xd4]
// 0x10b83e8: cmp w9, w10
// 0x10b83ec: b.ne #0x10b87f4
// 0x10b83f0: ldrb w8, [x8, #0x17c]
// 0x10b83f4: cbz w8, #0x10b87f4
// 0x10b83f8: mov x0, xzr
// 0x10b83fc: bl #0x1b9ad30
// 0x10b8400: ldr s1, [x19, #0x1fc]
// 0x10b8404: ldr s2, [x19, #0x150]
// 0x10b8408: fsub s0, s0, s1
// 0x10b840c: fcmp s0, s2
// 0x10b8410: b.le #0x10b87f4
// 0x10b8414: ldr s8, [x19, #0x1c0]
// 0x10b8418: ldr s9, [x19, #0x1bc]
// 0x10b841c: mov x0, xzr
// 0x10b8420: bl #0x1b9ad30
// 0x10b8424: fadd s1, s8, s9
// 0x10b8428: fcmp s1, s0
// 0x10b842c: b.pl #0x10b87f4
// 0x10b8430: ldr s8, [x19, #0x1c8]
// 0x10b8434: ldr s0, [x19, #0x1c4]
// 0x10b8438: fcmp s8, s0
// 0x10b843c: b.pl #0x10b845c
// 0x10b8440: mov x0, xzr
// 0x10b8444: bl #0x1b89b60
// 0x10b8448: ldr s1, [x19, #0x1c4]
// 0x10b844c: fadd s0, s8, s0
// 0x10b8450: str s0, [x19, #0x1c8]
// 0x10b8454: fdiv s0, s0, s1
// 0x10b8458: str s0, [x19, #0x1cc]
// 0x10b845c: ldrb w8, [x19, #0x1d4]
// 0x10b8460: cbnz w8, #0x10b8650
// 0x10b8464: ldrb w8, [x19, #0x1d5]
// 0x10b8468: cbnz w8, #0x10b8650
// 0x10b846c: ldr x0, [x19, #0x110]
// 0x10b8470: cbz x0, #0x10b8d8c
// 0x10b8474: adrp x8, #0x1e8e000
// 0x10b8478: ldr x8, [x8, #0x5c8]
// 0x10b847c: mov x2, xzr
// 0x10b8480: ldr x1, [x8]
// 0x10b8484: bl #0x1b67884
// 0x10b8488: ldr w8, [x19, #0x368]
// 0x10b848c: cmp w8, #6
// 0x10b8490: b.ne #0x10b8530
// 0x10b8494: ldr x0, [x21]
// 0x10b8498: ldr x20, [x19, #0x20]
// 0x10b849c: ldr w8, [x0, #0xe0]
// 0x10b84a0: cbnz w8, #0x10b84a8
// 0x10b84a4: bl #0xf7da5c
// 0x10b84a8: mov x0, x20
// 0x10b84ac: mov x1, xzr
// 0x10b84b0: bl #0x1b98274
// 0x10b84b4: tbz w0, #0, #0x10b8530
// 0x10b84b8: ldr x0, [x19, #0x20]
// 0x10b84bc: cbz x0, #0x10b8d8c
// 0x10b84c0: adrp x22, #0x1e8e000
// 0x10b84c4: ldr x22, [x22, #0x6f8]
// 0x10b84c8: mov x2, xzr
// 0x10b84cc: ldr x1, [x22]
// 0x10b84d0: bl #0x1b67884
// 0x10b84d4: ldr x0, [x21]
// 0x10b84d8: ldr x20, [x19, #0x38]
// 0x10b84dc: ldr w8, [x0, #0xe0]
// 0x10b84e0: cbnz w8, #0x10b84e8
// 0x10b84e4: bl #0xf7da5c
// 0x10b84e8: mov x0, x20
// 0x10b84ec: mov x1, xzr
// 0x10b84f0: bl #0x1b98274
// 0x10b84f4: tbz w0, #0, #0x10b8530
// 0x10b84f8: ldr x8, [x19, #0x80]
// 0x10b84fc: cbz x8, #0x10b8d8c
// 0x10b8500: ldrb w8, [x8, #0x2dc]
// 0x10b8504: cbnz w8, #0x10b8530
// 0x10b8508: ldr x0, [x19, #0x38]
// 0x10b850c: cbz x0, #0x10b8d8c
// 0x10b8510: mov x1, xzr
// 0x10b8514: bl #0x1b673a0
// 0x10b8518: tbz w0, #0, #0x10b8530
// 0x10b851c: ldr x0, [x19, #0x38]
// 0x10b8520: cbz x0, #0x10b8d8c
// 0x10b8524: ldr x1, [x22]
// 0x10b8528: mov x2, xzr
// 0x10b852c: bl #0x1b67884
// 0x10b8530: ldrb w8, [x19, #0x1a0]
// 0x10b8534: cbz w8, #0x10b8568
// 0x10b8538: ldr x0, [x19, #0x118]
// 0x10b853c: cbz x0, #0x10b8d8c
// 0x10b8540: ldr s0, [x19, #0x1a4]
// 0x10b8544: mov x1, xzr
// 0x10b8548: bl #0x1b67eb4
// 0x10b854c: ldr x0, [x19, #0x118]
// 0x10b8550: cbz x0, #0x10b8d8c
// 0x10b8554: adrp x8, #0x1e8e000
// 0x10b8558: ldr x8, [x8, #0x720]
// 0x10b855c: mov x2, xzr
// 0x10b8560: ldr x1, [x8]
// 0x10b8564: bl #0x1b67884
// 0x10b8568: ldrb w8, [x19, #0x1a8]
// 0x10b856c: cbz w8, #0x10b85a0
// 0x10b8570: ldr x0, [x19, #0x118]
// 0x10b8574: cbz x0, #0x10b8d8c
// 0x10b8578: ldr s0, [x19, #0x1ac]
// 0x10b857c: mov x1, xzr
// 0x10b8580: bl #0x1b67eb4
// 0x10b8584: ldr x0, [x19, #0x118]
// 0x10b8588: cbz x0, #0x10b8d8c
// 0x10b858c: adrp x8, #0x1e8e000
// 0x10b8590: ldr x8, [x8, #0x660]
// 0x10b8594: mov x2, xzr
// 0x10b8598: ldr x1, [x8]
// 0x10b859c: bl #0x1b67884
// 0x10b85a0: ldr x0, [x21]
// 0x10b85a4: ldr x20, [x19, #0x6d0]
// 0x10b85a8: ldr w8, [x0, #0xe0]
// 0x10b85ac: cbnz w8, #0x10b85b4
// 0x10b85b0: bl #0xf7da5c
// 0x10b85b4: mov x0, x20
// 0x10b85b8: mov x1, xzr
// 0x10b85bc: bl #0x1b98274
// 0x10b85c0: tbz w0, #0, #0x10b8630
// 0x10b85c4: ldr x0, [x19, #0x690]
// 0x10b85c8: cbz x0, #0x10b8d8c
// 0x10b85cc: fmov s0, #1.00000000
// 0x10b85d0: mov x1, xzr
// 0x10b85d4: bl #0x1b6a478
// 0x10b85d8: ldr x0, [x19, #0x690]
// 0x10b85dc: cbz x0, #0x10b8d8c
// 0x10b85e0: ldr x1, [x19, #0x6d0]
// 0x10b85e4: mov x2, xzr
// 0x10b85e8: bl #0x1b6a588
// 0x10b85ec: ldr x20, [x19, #0x690]
// 0x10b85f0: cbz x20, #0x10b8d8c
// 0x10b85f4: mov x0, x20
// 0x10b85f8: mov x1, xzr
// 0x10b85fc: bl #0x1b6a54c
// 0x10b8600: ldr x8, [x19, #0x690]
// 0x10b8604: cbz x8, #0x10b8d8c
// 0x10b8608: mov x21, x0
// 0x10b860c: mov x0, x8
// 0x10b8610: mov x1, xzr
// 0x10b8614: bl #0x1b6a43c
// 0x10b8618: fmov s1, #1.00000000
// 0x10b861c: fdiv s0, s1, s0
// 0x10b8620: mov x0, x20
// 0x10b8624: mov x1, x21
// 0x10b8628: mov x2, xzr
// 0x10b862c: bl #0x1b6a66c
// 0x10b8630: mov x0, xzr
// 0x10b8634: bl #0x1b9ad30
// 0x10b8638: mov w8, #0x101
// 0x10b863c: add x9, x19, #0x191
// 0x10b8640: mov w10, #1
// 0x10b8644: str s0, [x19, #0x1b8]
// 0x10b8648: strh w8, [x19, #0x1d4]
// 0x10b864c: strh w10, [x9]
// 0x10b8650: ldr x8, [x19, #0x88]
// 0x10b8654: cbz x8, #0x10b8d8c
// 0x10b8658: ldrb w9, [x8, #0x17c]
// 0x10b865c: cbz w9, #0x10b89dc
// 0x10b8660: ldr w9, [x19, #0x124]
// 0x10b8664: ldr w10, [x8, #0xd4]
// 0x10b8668: cmp w9, w10
// 0x10b866c: b.ne #0x10b89dc
// 0x10b8670: ldr x9, [x19, #0xa0]
// 0x10b8674: cbz x9, #0x10b8d8c
// 0x10b8678: ldrb w9, [x9, #0x9b]
// 0x10b867c: cbnz w9, #0x10b89dc
// 0x10b8680: strb wzr, [x8, #0x17c]
// 0x10b8684: b #0x10b89dc
// 0x10b8688: ldr w8, [x19, #0x128]
// 0x10b868c: cmp w8, #1
// 0x10b8690: b.lt #0x10b836c
// 0x10b8694: ldrb w8, [x19, #0x1f6]
// 0x10b8698: cbz w8, #0x10b836c
// 0x10b869c: ldr w8, [x19, #0x12c]
// 0x10b86a0: ldr w9, [x19, #0x130]
// 0x10b86a4: cmp w8, w9
// 0x10b86a8: b.ge #0x10b836c
// 0x10b86ac: mov x0, xzr
// 0x10b86b0: bl #0x1b9ad30
// 0x10b86b4: ldr s1, [x19, #0x1fc]
// 0x10b86b8: ldr s2, [x19, #0x150]
// 0x10b86bc: fsub s0, s0, s1
// 0x10b86c0: fcmp s0, s2
// 0x10b86c4: b.le #0x10b836c
// 0x10b86c8: ldr x8, [x19, #0xa0]
// 0x10b86cc: cbz x8, #0x10b8d8c
// 0x10b86d0: ldrb w8, [x8, #0x89]
// 0x10b86d4: cbnz w8, #0x10b836c
// 0x10b86d8: mov w8, #1
// 0x10b86dc: strb w8, [x19, #0x3c5]
// 0x10b86e0: adrp x8, #0x1e8e000
// 0x10b86e4: ldr x8, [x8, #0x498]
// 0x10b86e8: mov x0, x19
// 0x10b86ec: mov x2, xzr
// 0x10b86f0: ldr x1, [x8]
// 0x10b86f4: bl #0x1b95b9c
// 0x10b86f8: b #0x10b836c
// 0x10b86fc: ldrb w8, [x19, #0x1e1]
// 0x10b8700: cbz w8, #0x10b8760
// 0x10b8704: ldrb w8, [x19, #0x1e0]
// 0x10b8708: cbz w8, #0x10b8760
// 0x10b870c: strb wzr, [x19, #0x1e0]
// 0x10b8710: b #0x10b8768
// 0x10b8714: ldrb w8, [x8, #0x2e8]
// 0x10b8718: cbz w8, #0x10b7934
// 0x10b871c: ldrb w8, [x19, #0x3a6]
// 0x10b8720: cbnz w8, #0x10b7970
// 0x10b8724: ldr x20, [x19, #0x88]
// 0x10b8728: mov x0, xzr
// 0x10b872c: bl #0x1b9ad30
// 0x10b8730: cbz x20, #0x10b8d8c
// 0x10b8734: str s0, [x20, #0x124]
// 0x10b8738: ldr x0, [x19, #0x108]
// 0x10b873c: cbz x0, #0x10b8d8c
// 0x10b8740: adrp x8, #0x1e8e000
// 0x10b8744: ldr x8, [x8, #0x618]
// 0x10b8748: mov x2, xzr
// 0x10b874c: ldr x1, [x8]
// 0x10b8750: bl #0x1b67884
// 0x10b8754: mov w8, #1
// 0x10b8758: strb w8, [x19, #0x3a6]
// 0x10b875c: b #0x10b7970
// 0x10b8760: mov w8, #1
// 0x10b8764: strb w8, [x19, #0x1de]
// 0x10b8768: ldr w8, [x19, #0x154]
// 0x10b876c: ldr x0, [x19, #0x690]
// 0x10b8770: fmov s0, #3.50000000
// 0x10b8774: fmov s1, #2.00000000
// 0x10b8778: cmp w8, #1
// 0x10b877c: fcsel s0, s1, s0, gt
// 0x10b8780: strb wzr, [x19, #0x1dd]
// 0x10b8784: str s0, [x19, #0x450]
// 0x10b8788: cbz x0, #0x10b8d8c
// 0x10b878c: fmov s0, #1.00000000
// 0x10b8790: mov x1, xzr
// 0x10b8794: bl #0x1b6a478
// 0x10b8798: ldr x0, [x19, #0x690]
// 0x10b879c: cbz x0, #0x10b8d8c
// 0x10b87a0: ldr x1, [x19, #0x6c0]
// 0x10b87a4: mov x2, xzr
// 0x10b87a8: bl #0x1b6a588
// 0x10b87ac: ldr x20, [x19, #0x690]
// 0x10b87b0: cbz x20, #0x10b8d8c
// 0x10b87b4: mov x0, x20
// 0x10b87b8: mov x1, xzr
// 0x10b87bc: bl #0x1b6a54c
// 0x10b87c0: ldr x8, [x19, #0x690]
// 0x10b87c4: cbz x8, #0x10b8d8c
// 0x10b87c8: mov x21, x0
// 0x10b87cc: mov x0, x8
// 0x10b87d0: mov x1, xzr
// 0x10b87d4: bl #0x1b6a43c
// 0x10b87d8: fmov s1, #1.00000000
// 0x10b87dc: fdiv s0, s1, s0
// 0x10b87e0: mov x0, x20
// 0x10b87e4: mov x1, x21
// 0x10b87e8: mov x2, xzr
// 0x10b87ec: bl #0x1b6a66c
// 0x10b87f0: b #0x10b78b8
// 0x10b87f4: ldrb w8, [x19, #0x191]
// 0x10b87f8: cbz w8, #0x10b89dc
// 0x10b87fc: ldr s8, [x19, #0x1b8]
// 0x10b8800: ldr s9, [x19, #0x1b4]
// 0x10b8804: mov x0, xzr
// 0x10b8808: bl #0x1b9ad30
// 0x10b880c: fadd s1, s8, s9
// 0x10b8810: fcmp s1, s0
// 0x10b8814: b.pl #0x10b89dc
// 0x10b8818: ldr s8, [x19, #0x3e0]
// 0x10b881c: ldr s9, [x19, #0x3d4]
// 0x10b8820: mov x0, xzr
// 0x10b8824: bl #0x1b9ad30
// 0x10b8828: fadd s1, s8, s9
// 0x10b882c: fcmp s1, s0
// 0x10b8830: b.pl #0x10b89dc
// 0x10b8834: mov x0, xzr
// 0x10b8838: strb wzr, [x19, #0x1d4]
// 0x10b883c: bl #0x1b9ad30
// 0x10b8840: ldrb w8, [x19, #0x1f6]
// 0x10b8844: str s0, [x19, #0x1c0]
// 0x10b8848: cbz w8, #0x10b885c
// 0x10b884c: ldr x8, [x19, #0x90]
// 0x10b8850: cbz x8, #0x10b8d8c
// 0x10b8854: ldrb w8, [x8, #0x129]
// 0x10b8858: cbnz w8, #0x10b89d8
// 0x10b885c: ldr x0, [x19, #0x110]
// 0x10b8860: cbz x0, #0x10b8d8c
// 0x10b8864: adrp x8, #0x1e8e000
// 0x10b8868: ldr x8, [x8, #0x4b8]
// 0x10b886c: mov x2, xzr
// 0x10b8870: ldr x1, [x8]
// 0x10b8874: bl #0x1b67884
// 0x10b8878: ldr w8, [x19, #0x368]
// 0x10b887c: cmp w8, #7
// 0x10b8880: b.ne #0x10b8914
// 0x10b8884: ldr x0, [x21]
// 0x10b8888: ldr x20, [x19, #0x20]
// 0x10b888c: ldr w8, [x0, #0xe0]
// 0x10b8890: cbnz w8, #0x10b8898
// 0x10b8894: bl #0xf7da5c
// 0x10b8898: mov x0, x20
// 0x10b889c: mov x1, xzr
// 0x10b88a0: bl #0x1b98274
// 0x10b88a4: tbz w0, #0, #0x10b8914
// 0x10b88a8: adrp x20, #0x1e8e000
// 0x10b88ac: ldr x20, [x20, #0x700]
// 0x10b88b0: mov x1, xzr
// 0x10b88b4: ldr x0, [x20]
// 0x10b88b8: bl #0x1b8fab8
// 0x10b88bc: ldr x8, [x19, #0x20]
// 0x10b88c0: str w0, [x19, #0x128]
// 0x10b88c4: cbz x8, #0x10b8d8c
// 0x10b88c8: adrp x9, #0x1e8e000
// 0x10b88cc: ldr x9, [x9, #0x708]
// 0x10b88d0: mov x0, x8
// 0x10b88d4: mov x2, xzr
// 0x10b88d8: ldr x1, [x9]
// 0x10b88dc: bl #0x1b67884
// 0x10b88e0: adrp x8, #0x1e8e000
// 0x10b88e4: ldr x8, [x8, #0x6e0]
// 0x10b88e8: ldr x8, [x8]
// 0x10b88ec: ldr x8, [x8, #0xb8]
// 0x10b88f0: ldr x0, [x8]
// 0x10b88f4: cbz x0, #0x10b8d8c
// 0x10b88f8: mov x1, xzr
// 0x10b88fc: bl #0x10c24b4
// 0x10b8900: ldr w8, [x19, #0x128]
// 0x10b8904: ldr x0, [x20]
// 0x10b8908: mov x2, xzr
// 0x10b890c: sub w1, w8, #1
// 0x10b8910: bl #0x1b8f9e4
// 0x10b8914: ldr x0, [x21]
// 0x10b8918: ldr x20, [x19, #0x38]
// 0x10b891c: ldr w8, [x0, #0xe0]
// 0x10b8920: cbnz w8, #0x10b8928
// 0x10b8924: bl #0xf7da5c
// 0x10b8928: mov x0, x20
// 0x10b892c: mov x1, xzr
// 0x10b8930: bl #0x1b98274
// 0x10b8934: tbz w0, #0, #0x10b8968
// 0x10b8938: ldr x0, [x19, #0x38]
// 0x10b893c: cbz x0, #0x10b8d8c
// 0x10b8940: mov x1, xzr
// 0x10b8944: bl #0x1b673a0
// 0x10b8948: tbz w0, #0, #0x10b8968
// 0x10b894c: ldr x0, [x19, #0x38]
// 0x10b8950: cbz x0, #0x10b8d8c
// 0x10b8954: adrp x8, #0x1e8e000
// 0x10b8958: ldr x8, [x8, #0x718]
// 0x10b895c: mov x2, xzr
// 0x10b8960: ldr x1, [x8]
// 0x10b8964: bl #0x1b67884
// 0x10b8968: ldrb w8, [x19, #0x193]
// 0x10b896c: cbz w8, #0x10b89a0
// 0x10b8970: ldr x0, [x19, #0x118]
// 0x10b8974: cbz x0, #0x10b8d8c
// 0x10b8978: ldr s0, [x19, #0x194]
// 0x10b897c: mov x1, xzr
// 0x10b8980: bl #0x1b67eb4
// 0x10b8984: ldr x0, [x19, #0x118]
// 0x10b8988: cbz x0, #0x10b8d8c
// 0x10b898c: adrp x8, #0x1e8e000
// 0x10b8990: ldr x8, [x8, #0x720]
// 0x10b8994: mov x2, xzr
// 0x10b8998: ldr x1, [x8]
// 0x10b899c: bl #0x1b67884
// 0x10b89a0: ldrb w8, [x19, #0x198]
// 0x10b89a4: cbz w8, #0x10b89d8
// 0x10b89a8: ldr x0, [x19, #0x118]
// 0x10b89ac: cbz x0, #0x10b8d8c
// 0x10b89b0: ldr s0, [x19, #0x19c]
// 0x10b89b4: mov x1, xzr
// 0x10b89b8: bl #0x1b67eb4
// 0x10b89bc: ldr x0, [x19, #0x118]
// 0x10b89c0: cbz x0, #0x10b8d8c
// 0x10b89c4: adrp x8, #0x1e8e000
// 0x10b89c8: ldr x8, [x8, #0x660]
// 0x10b89cc: mov x2, xzr
// 0x10b89d0: ldr x1, [x8]
// 0x10b89d4: bl #0x1b67884
// 0x10b89d8: strb wzr, [x19, #0x191]
// 0x10b89dc: ldrb w8, [x19, #0x191]
// 0x10b89e0: cbnz w8, #0x10b8a64
// 0x10b89e4: ldr s8, [x19, #0x1c0]
// 0x10b89e8: ldr s9, [x19, #0x1bc]
// 0x10b89ec: mov x0, xzr
// 0x10b89f0: bl #0x1b9ad30
// 0x10b89f4: fadd s1, s8, s9
// 0x10b89f8: fcmp s1, s0
// 0x10b89fc: b.pl #0x10b8a64
// 0x10b8a00: ldrb w8, [x19, #0x1d5]
// 0x10b8a04: cbz w8, #0x10b8a3c
// 0x10b8a08: ldrb w8, [x19, #0x1f6]
// 0x10b8a0c: cbz w8, #0x10b8a20
// 0x10b8a10: ldr x8, [x19, #0x90]
// 0x10b8a14: cbz x8, #0x10b8d8c
// 0x10b8a18: ldrb w8, [x8, #0x129]
// 0x10b8a1c: cbnz w8, #0x10b8a38
// 0x10b8a20: ldr x0, [x19, #0x690]
// 0x10b8a24: mov w8, #1
// 0x10b8a28: strb w8, [x19, #0x192]
// 0x10b8a2c: cbz x0, #0x10b8d8c
// 0x10b8a30: mov x1, xzr
// 0x10b8a34: bl #0x1b6a768
// 0x10b8a38: strb wzr, [x19, #0x1d5]
// 0x10b8a3c: ldr x8, [x19, #0x88]
// 0x10b8a40: cbz x8, #0x10b8d8c
// 0x10b8a44: ldrb w9, [x8, #0x17e]
// 0x10b8a48: cbz w9, #0x10b8a64
// 0x10b8a4c: ldr w9, [x19, #0x124]
// 0x10b8a50: ldr w10, [x8, #0xd4]
// 0x10b8a54: cmp w9, w10
// 0x10b8a58: b.ne #0x10b8a64
// 0x10b8a5c: mov w9, #1
// 0x10b8a60: strb w9, [x8, #0x17d]
// 0x10b8a64: ldrb w8, [x19, #0x20c]
// 0x10b8a68: cbz w8, #0x10b8a94
// 0x10b8a6c: ldr x8, [x19, #0x80]
// 0x10b8a70: cbz x8, #0x10b8d8c
// 0x10b8a74: ldrb w9, [x8, #0x198]
// 0x10b8a78: cbnz w9, #0x10b8a94
// 0x10b8a7c: ldrb w8, [x8, #0x1a0]
// 0x10b8a80: cbnz w8, #0x10b8a94
// 0x10b8a84: ldr x8, [x19, #0xb8]
// 0x10b8a88: cbz x8, #0x10b8d8c
// 0x10b8a8c: ldrb w8, [x8, #0x1a5]
// 0x10b8a90: cbz w8, #0x10b8bd8
// 0x10b8a94: ldr x8, [x19, #0xa0]
// 0x10b8a98: cbz x8, #0x10b8d8c
// 0x10b8a9c: ldrb w9, [x8, #0x89]
// 0x10b8aa0: ldrb w8, [x19, #0x190]
// 0x10b8aa4: cbz w9, #0x10b8ab8
// 0x10b8aa8: cbnz w8, #0x10b8abc
// 0x10b8aac: ldrb w8, [x19, #0x229]
// 0x10b8ab0: cbnz w8, #0x10b8acc
// 0x10b8ab4: b #0x10b8b4c
// 0x10b8ab8: cbz w8, #0x10b8acc
// 0x10b8abc: ldrb w8, [x19, #0x192]
// 0x10b8ac0: cbz w8, #0x10b8acc
// 0x10b8ac4: ldrb w8, [x19, #0x1f4]
// 0x10b8ac8: cbz w8, #0x10b8b4c
// 0x10b8acc: strb wzr, [x19, #0x1df]
// 0x10b8ad0: strb wzr, [x19, #0x1f0]
// 0x10b8ad4: ldrb w8, [x19, #0x1e8]
// 0x10b8ad8: cbz w8, #0x10b8b78
// 0x10b8adc: ldrb w8, [x19, #0x1e0]
// 0x10b8ae0: cbz w8, #0x10b8b78
// 0x10b8ae4: ldrb w8, [x19, #0x3a4]
// 0x10b8ae8: cbz w8, #0x10b8b28
// 0x10b8aec: ldr x8, [x19, #0x90]
// 0x10b8af0: cbz x8, #0x10b8d8c
// 0x10b8af4: ldrb w8, [x8, #0x129]
// 0x10b8af8: cbnz w8, #0x10b8b28
// 0x10b8afc: ldr x8, [x19, #0x88]
// 0x10b8b00: cbz x8, #0x10b8d8c
// 0x10b8b04: ldrb w8, [x8, #0x128]
// 0x10b8b08: cbnz w8, #0x10b8b28
// 0x10b8b0c: ldr s8, [x19, #0x3e0]
// 0x10b8b10: ldr s9, [x19, #0x3d4]
// 0x10b8b14: mov x0, xzr
// 0x10b8b18: bl #0x1b9ad30
// 0x10b8b1c: fadd s1, s8, s9
// 0x10b8b20: fcmp s1, s0
// 0x10b8b24: b.le #0x10b8d14
// 0x10b8b28: mov w8, wzr
// 0x10b8b2c: strb wzr, [x19, #0x1e8]
// 0x10b8b30: str wzr, [x19, #0x1ec]
// 0x10b8b34: ldr w9, [x19, #0x1e4]
// 0x10b8b38: cmp w8, w9
// 0x10b8b3c: b.ge #0x10b8b70
// 0x10b8b40: mov x0, x19
// 0x10b8b44: bl #0x10b8d90
// 0x10b8b48: b #0x10b8b78
// 0x10b8b4c: ldrb w8, [x19, #0x1de]
// 0x10b8b50: cbz w8, #0x10b8ba0
// 0x10b8b54: ldrb w8, [x19, #0x1df]
// 0x10b8b58: cbnz w8, #0x10b8ad4
// 0x10b8b5c: mov x0, x19
// 0x10b8b60: bl #0x10b8d90
// 0x10b8b64: mov w8, #1
// 0x10b8b68: strb w8, [x19, #0x1df]
// 0x10b8b6c: b #0x10b8ad4
// 0x10b8b70: strb wzr, [x19, #0x1e8]
// 0x10b8b74: str wzr, [x19, #0x1ec]
// 0x10b8b78: mov x0, xzr
// 0x10b8b7c: bl #0x1b9ad30
// 0x10b8b80: ldr s1, [x19, #0x1fc]
// 0x10b8b84: adrp x8, #0x832000
// 0x10b8b88: ldr s2, [x8, #0x4f4]
// 0x10b8b8c: fsub s0, s0, s1
// 0x10b8b90: fcmp s0, s2
// 0x10b8b94: b.le #0x10b7a84
// 0x10b8b98: strb wzr, [x19, #0x3a5]
// 0x10b8b9c: b #0x10b7a84
// 0x10b8ba0: ldrb w8, [x19, #0x1e0]
// 0x10b8ba4: cbz w8, #0x10b8d08
// 0x10b8ba8: ldrb w8, [x19, #0x1e8]
// 0x10b8bac: cbnz w8, #0x10b8ad4
// 0x10b8bb0: ldrb w8, [x19, #0x1f0]
// 0x10b8bb4: cbnz w8, #0x10b8ad4
// 0x10b8bb8: ldr w9, [x19, #0x1ec]
// 0x10b8bbc: ldr w10, [x19, #0x1e4]
// 0x10b8bc0: mov w8, #1
// 0x10b8bc4: strb w8, [x19, #0x1e8]
// 0x10b8bc8: cmp w9, w10
// 0x10b8bcc: b.ge #0x10b8ad4
// 0x10b8bd0: strb w8, [x19, #0x1f0]
// 0x10b8bd4: b #0x10b8ad4
// 0x10b8bd8: ldr x8, [x19, #0xa8]
// 0x10b8bdc: cbz x8, #0x10b8d8c
// 0x10b8be0: ldr s0, [x8, #0x78]
// 0x10b8be4: mov w8, #-0x3d740000
// 0x10b8be8: fmov s1, w8
// 0x10b8bec: fcmp s0, s1
// 0x10b8bf0: b.gt #0x10b8bfc
// 0x10b8bf4: ldrb w8, [x19, #0x220]
// 0x10b8bf8: cbz w8, #0x10b8a94
// 0x10b8bfc: ldr x8, [x19, #0xa0]
// 0x10b8c00: cbz x8, #0x10b8d8c
// 0x10b8c04: ldrb w9, [x8, #0x9d]
// 0x10b8c08: cbz w9, #0x10b8d1c
// 0x10b8c0c: ldrb w8, [x19, #0x229]
// 0x10b8c10: cbnz w8, #0x10b8d40
// 0x10b8c14: mov x0, xzr
// 0x10b8c18: bl #0x1b9ad30
// 0x10b8c1c: ldr s1, [x19, #0x1fc]
// 0x10b8c20: ldr s2, [x19, #0x150]
// 0x10b8c24: fsub s0, s0, s1
// 0x10b8c28: fcmp s0, s2
// 0x10b8c2c: b.le #0x10b8d40
// 0x10b8c30: ldr s8, [x19, #0x224]
// 0x10b8c34: ldr s9, [x19, #0x210]
// 0x10b8c38: mov x0, xzr
// 0x10b8c3c: bl #0x1b9ad30
// 0x10b8c40: fadd s1, s8, s9
// 0x10b8c44: fcmp s1, s0
// 0x10b8c48: b.pl #0x10b8d40
// 0x10b8c4c: ldr x8, [x19, #0x88]
// 0x10b8c50: cbz x8, #0x10b8d8c
// 0x10b8c54: ldrb w8, [x8, #0x17e]
// 0x10b8c58: cbnz w8, #0x10b8d40
// 0x10b8c5c: ldr s0, [x19, #0x1cc]
// 0x10b8c60: fcmp s0, #0.0
// 0x10b8c64: b.ne #0x10b8d40
// 0x10b8c68: ldr s8, [x19, #0x3e0]
// 0x10b8c6c: ldr s9, [x19, #0x3d4]
// 0x10b8c70: mov x0, xzr
// 0x10b8c74: bl #0x1b9ad30
// 0x10b8c78: fadd s1, s8, s9
// 0x10b8c7c: fcmp s1, s0
// 0x10b8c80: b.pl #0x10b8d40
// 0x10b8c84: ldr x8, [x19, #0x80]
// 0x10b8c88: cbz x8, #0x10b8d8c
// 0x10b8c8c: ldrb w9, [x8, #0x2dc]
// 0x10b8c90: cbz w9, #0x10b8c9c
// 0x10b8c94: ldrb w8, [x8, #0x2e8]
// 0x10b8c98: cbnz w8, #0x10b8d40
// 0x10b8c9c: ldrb w8, [x19, #0x1e8]
// 0x10b8ca0: cbnz w8, #0x10b8d40
// 0x10b8ca4: mov w20, #1
// 0x10b8ca8: mov x0, xzr
// 0x10b8cac: strb w20, [x19, #0x229]
// 0x10b8cb0: bl #0x1b9ad30
// 0x10b8cb4: str s0, [x19, #0x224]
// 0x10b8cb8: strb w20, [x19, #0x228]
// 0x10b8cbc: str xzr, [x19, #0x6f0]
// 0x10b8cc0: str xzr, [x19, #0x6e0]
// 0x10b8cc4: adrp x8, #0x1e8e000
// 0x10b8cc8: ldr x8, [x8, #0x498]
// 0x10b8ccc: mov x0, x19
// 0x10b8cd0: mov x2, xzr
// 0x10b8cd4: ldr x1, [x8]
// 0x10b8cd8: bl #0x1b960e0
// 0x10b8cdc: ldr x8, [x19, #0x90]
// 0x10b8ce0: cbz x8, #0x10b8d8c
// 0x10b8ce4: strb wzr, [x8, #0x129]
// 0x10b8ce8: ldr x0, [x19, #0x690]
// 0x10b8cec: cbz x0, #0x10b8d8c
// 0x10b8cf0: mov x1, xzr
// 0x10b8cf4: mov x2, xzr
// 0x10b8cf8: bl #0x1b6a588
// 0x10b8cfc: mov x0, x19
// 0x10b8d00: bl #0x10b8d90
// 0x10b8d04: b #0x10b8d40
// 0x10b8d08: mov x0, x19
// 0x10b8d0c: bl #0x10b8d90
// 0x10b8d10: b #0x10b8ad4
// 0x10b8d14: ldr w8, [x19, #0x1ec]
// 0x10b8d18: b #0x10b8b34
// 0x10b8d1c: ldrb w9, [x19, #0x221]
// 0x10b8d20: cbz w9, #0x10b8d40
// 0x10b8d24: ldr s0, [x19, #0x204]
// 0x10b8d28: fcmp s0, #0.0
// 0x10b8d2c: b.ne #0x10b8d40
// 0x10b8d30: ldr w9, [x19, #0x128]
// 0x10b8d34: cbnz w9, #0x10b8d40
// 0x10b8d38: ldr w9, [x19, #0x12c]
// 0x10b8d3c: cbz w9, #0x10b8d80
// 0x10b8d40: ldr s8, [x19, #0x224]
// 0x10b8d44: ldr s9, [x19, #0x210]
// 0x10b8d48: mov x0, xzr
// 0x10b8d4c: bl #0x1b9ad30
// 0x10b8d50: fadd s1, s8, s9
// 0x10b8d54: fcmp s1, s0
// 0x10b8d58: b.pl #0x10b8a94
// 0x10b8d5c: ldrb w8, [x19, #0x228]
// 0x10b8d60: strb wzr, [x19, #0x229]
// 0x10b8d64: cbz w8, #0x10b8a94
// 0x10b8d68: ldr w8, [x19, #0x134]
// 0x10b8d6c: ldr w9, [x19, #0x130]
// 0x10b8d70: cmp w8, w9
// 0x10b8d74: b.eq #0x10b8a94
// 0x10b8d78: strb wzr, [x19, #0x228]
// 0x10b8d7c: b #0x10b8a94
// 0x10b8d80: ldrb w8, [x8, #0x8a]
// 0x10b8d84: cbnz w8, #0x10b8c0c
// 0x10b8d88: b #0x10b8d40
// 0x10b8d8c: bl #0xf7db74
```


## `WeaponBehavior.Fire` — RVA `0xcb8d90`

- Decompiled symbol: `WeaponBehavior_Fire`
- Metadata signature: `private void Fire() { }`
- Native interval: `1404` bytes
- Result: `pseudocode`
- Heuristic layout hint: `WeaponBehavior_Recovered` matched 47 offsets against `WeaponBehavior` metadata (confidence 1.00).

```c
typedef struct WeaponBehavior_Recovered {
    char padding_0[128];
    struct struct_3 *FPSWalkerComponent;
    struct struct_0 *PlayerWeaponsComponent;
    struct struct_1 *IronsightsComponent;
    char padding_98[32];
    struct struct_4 *CameraControlComponent;
    char padding_c0[104];
    int ammo;
    int bulletsLeft;
    unsigned int bulletsPerClip;
    char padding_134[28];
    unsigned int fireRate;
    char padding_154[62];
    char doReleaseFire;
    char padding_193[75];
    char semiAuto;
    char semiState;
    char padding_1e0[17];
    char silentShots;
    char initialSilentShots;
    char fireableUnderwater;
    char waterFireState;
    char padding_1f5[1];
    char doReload;
    char padding_1f7[5];
    unsigned int shootStartTime;
    char padding_200[4];
    unsigned int meleeSwingDelay;
    char padding_208[33];
    char meleeActive;
    char padding_22a[378];
    char canShoot;
    char shooting;
    char padding_3a6[2];
    unsigned int recoveryTime;
    char padding_3ac[12];
    unsigned int bulletsReloaded;
    unsigned int reloadTime;
    unsigned int reloadStartTime;
    char padding_3c4[4];
    unsigned int reloadEndTime;
    char padding_3cc[8];
    unsigned int readyTimeAmt;
    char padding_3d8[4];
    unsigned int recoveryTimeAmt;
    unsigned int startTime;
    char padding_3e4[4];
    unsigned int reloadLastStartTime;
    char padding_3ec[1];
    char cantFireState;
    char padding_3ee[188];
    char disableFiring;
    char padding_4ab[33];
    unsigned int bulletsJustFired;
    char padding_4d0[312];
    char spawnShell;
    char padding_609[127];
    long long firefx;
    long long otherfx;
    long long fireSnd;
    long long meleeSnd;
    char padding_6a8[24];
    long long noammoSnd;
    char padding_6c8[24];
    unsigned long long nextFireTime;
    unsigned long long schedulingTime;
    unsigned long long lastFireTime;
    unsigned long long firingPauseMinimumTime;
    char padding_700[20];
    unsigned int firePitch;
    unsigned long long time;
    unsigned long long oldTime;
    char padding_728[4];
    char audioDisabled;
} WeaponBehavior_Recovered;

typedef struct struct_6 {
    char padding_0[297];
    char field_129;
} struct_6;

typedef struct struct_5 {
    char padding_0[296];
    char field_128;
} struct_5;

typedef struct struct_3 {
    char padding_0[406];
    char field_196;
    char padding_197[1];
    char field_198;
    char padding_199[189];
    char field_256;
} struct_3;

typedef struct struct_0 {
    char padding_0[296];
    char field_128;
} struct_0;

typedef struct struct_1 {
    char padding_0[297];
    char field_129;
} struct_1;

typedef struct struct_4 {
    char padding_0[262];
    char field_106;
    char padding_107[158];
    char field_1a5;
} struct_4;

extern long long g_1f0a458;
extern long long g_1f0c470;
extern long long g_1f0d410;
extern long long g_1f0db38;
extern char g_1fab4e4;

struct_2 * WeaponBehavior_Fire(struct_2 *ptr)
{
    struct_2 *v0;  // x0
    struct_2 *v1;  // x0
    struct_2 *v10;  // x0
    unsigned int v11;  // w9
    unsigned int v12;  // w10
    unsigned int v13;  // w8
    unsigned long v15;  // d0
    unsigned long v16;  // 4165
    unsigned int v17;  // s1
    unsigned long v18;  // 4138
    struct_2 *v19;  // x0
    struct_2 *v2;  // x0
    unsigned int v20;  // s1
    unsigned long v21;  // 4138
    struct_2 *v22;  // x0
    unsigned int v23;  // s1
    unsigned long v24;  // 4138
    unsigned long v25;  // d1
    unsigned int v26;  // 4099
    unsigned long v27;  // 4115
    unsigned long v28;  // d0
    unsigned long v29;  // 4133
    unsigned int v3;  // w8
    struct_2 *v30;  // x0
    unsigned int v31;  // w8
    unsigned long v32;  // d2
    unsigned long v33;  // 4166
    unsigned long long v34;  // d1
    unsigned long v35;  // 4142
    struct_2 *v36;  // x0
    unsigned long v37;  // 4125
    unsigned int v38;  // s1
    unsigned long v39;  // 4146
    unsigned int v4;  // w9
    unsigned long v40;  // d2
    unsigned long long v41;  // d0
    unsigned long v42;  // 4150
    unsigned int v43;  // w8
    unsigned long v44;  // x20
    char v46;  // x8
    unsigned long long v47;  // 4102
    unsigned long v48;  // x20
    char v5[422];  // x9
    unsigned int v50;  // s1
    unsigned long v51;  // d0
    unsigned int v52;  // w8
    unsigned int v53;  // w9
    struct_2 *v54;  // x0
    unsigned int v55;  // s0
    unsigned long long v56;  // 4103
    struct_2 *v57;  // x0
    char v6[599];  // x9
    unsigned long long v7;  // x11
    unsigned long v8;  // x20
    unsigned long v9;  // x0

    v0 = ptr;
    if (!(g_1fab4e4 & 1))
    {
        sub_f7d92c(&g_1f0c470);
        sub_f7d92c(&g_1f0a458);
        sub_f7d92c(&g_1f0db38);
        v1 = sub_f7d92c(&g_1f0d410);
        g_1fab4e4 = 1;
        v0 = v1;
    }
    v2 = v0;
    v3 = ptr->field_229;
    if (!v3)
    {
        v4 = ptr->field_1f6;
        if (ptr->field_12c > 0)
        {
            if (v4)
                goto LABEL_10b8ef4;
        }
        else
        {
            if (v4)
                return v2;
        }
        if (ptr->field_128 < 1)
            return v2;
LABEL_10b8ef4:
        if (ptr->field_1de && ptr->field_1df)
            return v2;
    }
    v5 = ptr->field_b8;
    if (v5)
    {
        if (v5[421])
            return v2;
        if (ptr->field_4aa && v5[262])
            return v2;
        v6 = ptr->field_80;
        if (v6)
        {
            if (!v3)
                v7 = 0;
            else
                v7 = 1;
            if (!(v6[598] && !((char)v7 & 1) && (!ptr->field_1f3 || v6[406])))
            {
                v11 = *((int *)&ptr->padding_134[0]);
                v12 = ptr->field_130;
                if (v11 == v12)
                {
                    if (ptr->field_90)
                    {
                        if (ptr->field_90->field_129)
                            v13 = 0;
                        else
                            v13 = 1;
                        goto LABEL_10b8fb8;
                    }
                }
                else
                {
                    if (v3 || !ptr->field_1f6 && 0 < ptr->field_128)
                        goto LABEL_10b8fb8;
                    if (ptr->field_90)
                    {
                        if (ptr->field_90->field_129)
                        {
                            if (v11 == v12)
                                return v2;
                            v15 = _INSERT(_INSERT(ptr->field_12c CONCAT 0, 0, ptr->field_12c), 4, 0);
                            v16 = arm64g_calculate_condition(128, (((((unsigned long long)(char)(CmpF(v11 * 2, (unsigned int)v15)) >> 5 & 3 | (unsigned long long)(CmpF(v11 * 2, (unsigned int)v15) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v11 * 2, (unsigned int)v15)) >> 5 & 3 | (unsigned long long)(CmpF(v11 * 2, (unsigned int)v15) & 1)) & ((unsigned long long)(char)(CmpF(v11 * 2, (unsigned int)v15)) >> 5 & 3 | (unsigned long long)(CmpF(v11 * 2, (unsigned int)v15) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                            if ((char)v16)
                                return v2;
                            v2 = Time__get_time(0);
                            v17 = ptr->field_3c8 + ptr->field_3bc;
                            v18 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v17, (unsigned int)v15)) >> 5 & 3 | (unsigned long long)(CmpF(v17, (unsigned int)v15) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v17, (unsigned int)v15)) >> 5 & 3 | (unsigned long long)(CmpF(v17, (unsigned int)v15) & 1)) & ((unsigned long long)(char)(CmpF(v17, (unsigned int)v15)) >> 5 & 3 | (unsigned long long)(CmpF(v17, (unsigned int)v15) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                            if ((char)v18)
                                return v2;
                        }
                        else
                        {
                            if (v11 == v12)
                                return v2;
                            if (ptr->field_12c <= 0)
                                return v2;
                        }
LABEL_10b8fb8:
                        if (ptr->field_3a4)
                        {
                            if (ptr->field_88)
                            {
                                if (!ptr->field_88->field_128)
                                    goto LABEL_10b8fe0;
                                goto LABEL_10b8fd0;
                            }
                        }
                        else
                        {
LABEL_10b8fd0:
                            if (!ptr->field_192 && !ptr->field_229)
                                return v2;
LABEL_10b8fe0:
                            v19 = Time__get_time(0);
                            v20 = ptr->field_3a8 + ptr->field_3dc;
                            v21 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(v20, (unsigned int)v15)) >> 5 & 3 | (unsigned long long)(CmpF(v20, (unsigned int)v15) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v20, (unsigned int)v15)) >> 5 & 3 | (unsigned long long)(CmpF(v20, (unsigned int)v15) & 1)) & ((unsigned long long)(char)(CmpF(v20, (unsigned int)v15)) >> 5 & 3 | (unsigned long long)(CmpF(v20, (unsigned int)v15) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                            if (!((char)v21))
                            {
                                if (ptr->field_b8)
                                {
                                    if (!ptr->field_b8->field_106 && !ptr->field_192 && !ptr->field_229)
                                        return v19;
                                    goto LABEL_10b901c;
                                }
                            }
                            else
                            {
LABEL_10b901c:
                                v22 = Time__get_time(0);
                                v23 = ptr->field_3e0 + ptr->field_3d4;
                                v24 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v23, (unsigned int)v15)) >> 5 & 3 | (unsigned long long)(CmpF(v23, (unsigned int)v15) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v23, (unsigned int)v15)) >> 5 & 3 | (unsigned long long)(CmpF(v23, (unsigned int)v15) & 1)) & ((unsigned long long)(char)(CmpF(v23, (unsigned int)v15)) >> 5 & 3 | (unsigned long long)(CmpF(v23, (unsigned int)v15) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                                if ((char)v24)
                                    return v22;
                                AudioSettings__get_dspTime(0);
                                v25 = ptr->field_720;
                                v26 = CmpF(v15, v25);
                                v27 = (((CmpF(v15, v25) >> 5 & 3 | CmpF(v15, v25) & 1) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1;
                                if (!((char)((v27 - ((CmpF(v15, v25) >> 5 & 3 | CmpF(v15, v25) & 1) & (v26 >> 5 & 3 | CmpF(v15, v25) & 1) >> 1 & 1)) * 0x10000000 >> 30)) && !((v28 = (unsigned long)(unsigned long long)ptr->field_150, v29 = (unsigned long)arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF((unsigned int)v28, 1050253722)) >> 5 & 3 | (unsigned long long)(CmpF((unsigned int)v28, 1050253722) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF((unsigned int)v28, 1050253722)) >> 5 & 3 | (unsigned long long)(CmpF((unsigned int)v28, 1050253722) & 1)) & ((unsigned long long)(char)(CmpF((unsigned int)v28, 1050253722)) >> 5 & 3 | (unsigned long long)(CmpF((unsigned int)v28, 1050253722) & 1)) >> 1 & 1)) * 0x10000000, 0, 0), (char)v29)))
                                {
                                    v30 = AudioSettings__get_dspTime(0);
                                    ptr->field_718 = v28;
                                    ptr->field_72c = 0;
                                }
                                else
                                {
                                    v30 = Time__get_time(0);
                                    v31 = ptr->field_72c;
                                    v28 &= 4294967295;
                                    ptr->field_718 = v28;
                                    if (!v31)
                                    {
                                        ptr->field_6f0 = 0;
                                        ptr->field_6e0 = 0;
                                        ptr->field_72c = 1;
                                    }
                                }
                                v32 = ptr->field_6f0 + ptr->field_150 * 1061997773;
                                v33 = arm64g_calculate_condition(192, (((((unsigned long long)(char)(CmpF(v32, v28)) >> 5 & 3 | (unsigned long long)(CmpF(v32, v28) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v32, v28)) >> 5 & 3 | (unsigned long long)(CmpF(v32, v28) & 1)) & ((unsigned long long)(char)(CmpF(v32, v28)) >> 5 & 3 | (unsigned long long)(CmpF(v32, v28) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                                if ((char)v33)
                                    return v30;
                                v34 = ptr->field_6f0 + ptr->field_6f8;
                                v35 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v28, v34)) >> 5 & 3 | (unsigned long long)(CmpF(v28, v34) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v28, v34)) >> 5 & 3 | (unsigned long long)(CmpF(v28, v34) & 1)) & ((unsigned long long)(char)(CmpF(v28, v34)) >> 5 & 3 | (unsigned long long)(CmpF(v28, v34) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                                if (!((char)v35))
                                    ptr->field_6e0 = v28;
                                v36 = Time__get_timeScale(0);
                                v37 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF((unsigned int)v28, 0x3f800000)) >> 5 & 3 | (unsigned long long)(CmpF((unsigned int)v28, 0x3f800000) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF((unsigned int)v28, 0x3f800000)) >> 5 & 3 | (unsigned long long)(CmpF((unsigned int)v28, 0x3f800000) & 1)) & ((unsigned long long)(char)(CmpF((unsigned int)v28, 0x3f800000)) >> 5 & 3 | (unsigned long long)(CmpF((unsigned int)v28, 0x3f800000) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                                if (!((char)v37))
                                {
                                    v36 = Time__get_time(0);
                                    v38 = ptr->field_1fc + ptr->field_150;
                                    v39 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF((unsigned int)v28, v38)) >> 5 & 3 | (unsigned long long)(CmpF((unsigned int)v28, v38) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF((unsigned int)v28, v38)) >> 5 & 3 | (unsigned long long)(CmpF((unsigned int)v28, v38) & 1)) & ((unsigned long long)(char)(CmpF((unsigned int)v28, v38)) >> 5 & 3 | (unsigned long long)(CmpF((unsigned int)v28, v38) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                                    if ((char)v39)
                                        return v36;
                                }
                                v40 = ptr->field_718;
                                v41 = ptr->field_6e0 - ptr->field_6e8;
                                v42 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v40, v41)) >> 5 & 3 | (unsigned long long)(CmpF(v40, v41) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v40, v41)) >> 5 & 3 | (unsigned long long)(CmpF(v40, v41) & 1)) & ((unsigned long long)(char)(CmpF(v40, v41)) >> 5 & 3 | (unsigned long long)(CmpF(v40, v41) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                                if ((char)v42)
                                    return v36;
                                Random__Range(0);
                                v43 = ptr->field_229;
                                ptr->field_714 = 1064682127;
                                if (v43)
                                {
                                    if (ptr->field_688 && (AudioSource__set_clip(ptr->field_688, ptr->field_6a0, 0), v44 = (unsigned long)ptr->field_688, v44))
                                    {
                                        AudioSource__PlayOneShot(v44, AudioSource__get_clip(v44, 0), 0);
                                        v46 = 1;
                                        goto LABEL_10b91e4;
                                    }
                                }
                                else
                                {
                                    Time__get_timeScale(0);
                                    v47 = (((CmpF(1064682127, 0x3f800000) >> 5 & 3 | CmpF(1064682127, 0x3f800000) & 1) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - ((CmpF(1064682127, 0x3f800000) >> 5 & 3 | CmpF(1064682127, 0x3f800000) & 1) & (CmpF(1064682127, 0x3f800000) >> 5 & 3 | CmpF(1064682127, 0x3f800000) & 1) >> 1 & 1);
                                    if ((char)(v47 * 0x10000000 >> 30))
                                    {
                                        WeaponBehavior__PlayerAltAutoFireSources();
                                        goto LABEL_10b91e0;
                                    }
                                    else
                                    {
                                        if (ptr->field_688 && (AudioSource__set_clip(ptr->field_688, ptr->field_698, 0), v48 = (unsigned long)ptr->field_688, v48))
                                        {
                                            AudioSource__PlayOneShot(v48, AudioSource__get_clip(v48, 0), 0);
LABEL_10b91e0:
                                            v46 = ptr->field_1f2;
LABEL_10b91e4:
                                            v50 = ptr->field_150;
                                            ptr->field_1f1 = v46;
                                            v51 = ptr->field_6e0;
                                            v52 = *((int *)&ptr->padding_134[0]);
                                            v53 = ptr->field_130;
                                            ptr->field_6f0 = v51;
                                            ptr->field_6e0 = v51 + v50;
                                            if (v52 != v53)
                                            {
                                                ptr->field_3b8 = 0;
                                                ptr->field_3c0 = 0xc1800000;
                                                ptr->field_3c8 = 0xc1800000;
                                                ptr->field_3e8 = 0xc1800000;
                                            }
                                            MonoBehaviour__StopCoroutine(ptr, g_1f0a458, 0);
                                            MonoBehaviour__StartCoroutine(ptr, g_1f0a458, 0);
                                            MonoBehaviour__StopCoroutine(ptr, g_1f0d410, 0);
                                            if (ptr->field_90)
                                            {
                                                ptr->field_90->field_129 = 0;
                                                if (ptr->field_690)
                                                {
                                                    v54 = AudioSource__set_clip(ptr->field_690, 0, 0);
                                                    v55 = ptr->field_204;
                                                    v56 = (((CmpF(v55, 0.0) >> 5 & 3 | CmpF(v55, 0.0) & 1) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - ((CmpF(v55, 0.0) >> 5 & 3 | CmpF(v55, 0.0) & 1) & (CmpF(v55, 0.0) >> 5 & 3 | CmpF(v55, 0.0) & 1) >> 1 & 1);
                                                    if ((char)(v56 * 0x10000000 >> 30) && !ptr->field_229)
                                                    {
                                                        ptr->field_4cc = ptr->field_4cc + 1;
                                                        v54 = MonoBehaviour__StartCoroutine(ptr, g_1f0c470, 0);
                                                        if (ptr->field_608)
                                                            v54 = MonoBehaviour__StartCoroutine(ptr, g_1f0db38, 0);
                                                    }
                                                    if (ptr->field_80)
                                                    {
                                                        if (ptr->field_80->field_198)
                                                            return v54;
                                                        v57 = Time__get_time(0);
                                                        ptr->field_1fc = v55;
                                                        ptr->field_3a5 = 1;
                                                        ptr->field_192 = 0;
                                                        return v57;
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
            else if (!ptr->field_3ed)
            {
                return v2;
            }
            else if (ptr->field_690)
            {
                AudioSource__set_volume(ptr->field_690, 0);
                if (ptr->field_690)
                {
                    AudioSource__set_clip(ptr->field_690, ptr->field_6c0, 0);
                    v8 = ptr->field_690;
                    if (v8)
                    {
                        v9 = AudioSource__get_clip(v8, 0);
                        if (ptr->field_690)
                        {
                            AudioSource__get_volume(ptr->field_690, 0);
                            v10 = AudioSource__PlayOneShot(v8, v9, 0);
                            ptr->field_3ed = 0;
                            ptr->field_1f4 = 1;
                            return v10;
                        }
                    }
                }
            }
        }
    }
    sub_f7db74();
}
```


## `WeaponBehavior.PlayerAltAutoFireSources` — RVA `0xcb930c`

- Decompiled symbol: `WeaponBehavior_PlayerAltAutoFireSources`
- Metadata signature: `public void PlayerAltAutoFireSources(double playTime) { }`
- Native interval: `172` bytes
- Result: `pseudocode`
- Heuristic layout hint: `WeaponBehavior_Recovered` matched 5 offsets against `WeaponBehavior` metadata (confidence 1.00).

```c
typedef struct WeaponBehavior_Recovered {
    char padding_0[1672];
    long long firefx;
    char padding_690[8];
    long long fireSnd;
    char padding_6a0[96];
    long long autoFireAsource1;
    long long autoFireAsource2;
    char curAutofireAsource;
} WeaponBehavior_Recovered;

unsigned long long WeaponBehavior_PlayerAltAutoFireSources(struct_0 *ptr)
{
    long long v0;  // x0
    unsigned long long v2;  // x0

    v0 = ptr->field_688;
    if (v0)
    {
        AudioSource__set_clip(v0, ptr->field_698, 0);
        v0 = ptr->field_708;
        if (v0)
        {
            AudioSource__set_clip(v0, ptr->field_698, 0);
            if (ptr->field_710)
            {
                v0 = ptr->field_700;
                if (v0)
                {
                    AudioSource__set_volume(v0, 0);
                    v0 = ptr->field_700;
                    if (ptr->field_700)
                    {
                        v2 = AudioSource__PlayScheduled();
                        ptr->field_710 = 0;
                        return v2;
                    }
                }
            }
            else
            {
                v0 = ptr->field_708;
                if (v0)
                {
                    AudioSource__set_volume(v0, 0);
                    v0 = ptr->field_708;
                    if (ptr->field_708)
                    {
                        v2 = AudioSource__PlayScheduled();
                        ptr->field_710 = 1;
                        return v2;
                    }
                }
            }
        }
    }
    sub_f7db74(v0);
}
```


## `WeaponBehavior.FireOneShot` — RVA `0xcb93b8`

- Decompiled symbol: `WeaponBehavior_FireOneShot`
- Metadata signature: `private IEnumerator FireOneShot() { }`
- Native interval: `108` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[12];
    long long field_20;
} struct_0;

extern long long g_1ef4008;
extern char g_1fab4e5;

struct_0 * WeaponBehavior_FireOneShot(long long a0)
{
    struct_0 *v0;  // x20
    struct_0 *ptr;  // x0

    if (!(g_1fab4e5 & 1))
    {
        sub_f7d92c(&g_1ef4008);
        g_1fab4e5 = 1;
    }
    v0 = sub_f7db70(g_1ef4008);
    Object__ctor(v0, 0);
    ptr = v0;
    ptr->field_10 = 0;
    ptr->field_20 = a0;
    sub_f7d8d0(&ptr->field_20, a0);
    return ptr;
}
```


## `WeaponBehavior.<FireOneShot>d__354.ctor` — RVA `0xcb9424`

- Decompiled symbol: `WeaponBehavior_FireOneShot_d__354_ctor`
- Metadata signature: `public void .ctor(int <>1__state) { }`
- Native interval: `40` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

void WeaponBehavior_FireOneShot_d__354_ctor(struct_0 *ptr, unsigned int a1)
{
    Object__ctor();
    ptr->field_10 = a1;
    return;
}
```


## `WeaponBehavior.HitObject` — RVA `0xcb944c`

- Decompiled symbol: `WeaponBehavior_HitObject`
- Metadata signature: `private void HitObject(RaycastHit hit, Vector3 directionArg, bool isSecondCast = false) { }`
- Native interval: `3376` bytes
- Result: `pseudocode`
- Heuristic layout hint: `WeaponBehavior_Recovered` matched 9 offsets against `WeaponBehavior` metadata (confidence 1.00).

```c
typedef struct struct_8 {
    char padding_0[32];
    unsigned int field_20;
} struct_8;

typedef struct struct_1 {
    uint128_t field_0;
    char field_10[28];
    char field_1c;
} struct_1;

typedef struct WeaponBehavior_Recovered {
    char padding_0[112];
    long long myTransform;
    long long mainCamTransform;
    char padding_80[24];
    struct struct_0 *FPSPlayerComponent;
    char padding_a0[16];
    long long WeaponEffectsComponent;
    char padding_b8[136];
    unsigned int damageAmt;
    char padding_144[20];
    int hitCount;
    char padding_15c[168];
    unsigned int meleeSwingDelay;
    char padding_208[20];
    unsigned int offhandMeleeDamage;
    char padding_220[9];
    char meleeActive;
} WeaponBehavior_Recovered;

typedef struct struct_0 {
    char padding_0[500];
    unsigned int field_1f4;
    char field_1f8;
} struct_0;

typedef struct struct_3 {
    char padding_0[32];
    long long field_20;
} struct_3;

typedef struct struct_4 {
    char padding_0[32];
    unsigned int field_20;
} struct_4;

typedef struct struct_5 {
    char padding_0[32];
    long long field_20;
} struct_5;

typedef struct struct_6 {
    char padding_0[32];
    long long field_20;
} struct_6;

typedef struct struct_7 {
    char padding_0[32];
    long long field_20;
} struct_7;

extern struct_0 *g_1ef0c58;
extern long long g_1efeb10;
extern long long g_1efeb30;
extern long long g_1efeb48;
extern long long g_1efeb90;
extern long long g_1efebb0;
extern long long g_1efec38;
extern long long g_1efec58;
extern long long g_1efecc0;
extern long long g_1efed48;
extern long long g_1f0a468;
extern char g_1fab4e6;

struct_8 * WeaponBehavior_HitObject(struct_2 *ptr, struct_1 *p, unsigned int a2)
{
    long long v11;  // x0
    long long v12;  // x22
    unsigned int v21;  // w0
    long long v22;  // x0
    struct_3 *v23;  // x0
    struct_4 *v24;  // x0
    long long v25;  // x0
    long long v26;  // x0
    unsigned long v27;  // x0
    unsigned long v28;  // x22
    long long v29;  // x0
    struct_5 *v30;  // x0
    unsigned long v31;  // x0
    unsigned long v32;  // x22
    long long v33;  // x0
    struct_6 *v34;  // x0
    unsigned long v35;  // x0
    unsigned long v36;  // x22
    struct_8 *v37;  // x0
    long long v38;  // x0
    struct_7 *v39;  // x0
    long long v40;  // x0
    struct_8 *v41;  // x0
    unsigned int v42;  // w8
    unsigned int v43;  // s0
    unsigned long long v44;  // 4103
    unsigned long long v45;  // x0
    unsigned int v46;  // s0
    unsigned long long v47;  // 4103
    long long v48;  // x0
    struct_8 *v49;  // x0
    long long v50;  // x0
    long long v15;  // x0
    struct_8 *v51;  // x0
    unsigned long long v52;  // x0
    long long v16;  // x0
    unsigned int v17;  // w0
    long long v18;  // x0
    unsigned int v19;  // w0
    long long v20;  // x0
    char v0;  // [bp-0x110]
    int v1;  // [bp-0x100]
    int v2;  // [bp-0xf4]
    char v3;  // [bp-0xe0]
    int v4;  // [bp-0xd0]
    int v5;  // [bp-0xc4]
    int v6;  // [bp-0xb0]
    int v7;  // [bp-0xa0]
    int v8;  // [bp-0x94]
    char *v9;  // [bp-0x50]
    char v10;  // [bp+0x0]

    v9 = &v10;
    if (!(g_1fab4e6 & 1))
    {
        sub_f7d92c(&g_1efeb10);
        sub_f7d92c(&g_1efeb30);
        sub_f7d92c(&g_1efeb48);
        sub_f7d92c(&g_1efeb90);
        sub_f7d92c(&g_1efebb0);
        sub_f7d92c(&g_1efec38);
        sub_f7d92c(&g_1efec58);
        sub_f7d92c(&g_1efecc0);
        sub_f7d92c(&g_1efed48);
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c("_2");
        sub_f7d92c(&g_1f0a468);
        g_1fab4e6 = 1;
    }
    v11 = RaycastHit__get_rigidbody(p, 0);
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (!((char)Object__op_Implicit(v11, 0) & 1))
    {
LABEL_10b95f4:
        ptr->field_140 = ptr->field_21c;
        if (RaycastHit__get_collider(p, 0) && Component__get_gameObject())
        {
            switch ((unsigned int)GameObject__get_layer())
            {
            case 13:
                if (RaycastHit__get_collider(p, 0) && Component__get_gameObject())
                {
                    v26 = sub_1249224();
                    if (!g_1ef0c58->field_e0)
                        sub_f7da5c(g_1ef0c58);
                    if (((char)Object__op_Implicit(v26, 0) & 1))
                    {
                        if (RaycastHit__get_collider(p, 0) && Component__get_gameObject() && sub_1249224())
                        {
                            if (!(Behaviour__get_enabled() & 1))
                                goto LABEL_10b98f8;
                            if (RaycastHit__get_collider(p, 0) && Component__get_gameObject() && (v27 = (unsigned long)sub_1249224(), ptr->field_78 && (v28 = (unsigned long)sub_1249224(), Transform__get_position(ptr->field_78, 0), v28 && (CharacterDamage__ApplyDamage(v28, ptr->field_70, 1, 0, 0), ptr->field_98))))
                            {
                                FPSPlayer__UpdateHitTime(ptr->field_98);
                                goto LABEL_10b98f8;
                            }
                        }
                    }
                    else
                    {
LABEL_10b98f8:
                        if (RaycastHit__get_collider(p, 0) && Component__get_gameObject())
                        {
                            v29 = sub_1249224();
                            if (!g_1ef0c58->field_e0)
                                sub_f7da5c(g_1ef0c58);
                            if (!(Object__op_Implicit(v29, 0) & 1))
                                goto LABEL_10b9a94;
                            if (RaycastHit__get_collider(p, 0) && Component__get_gameObject() && (v30 = (struct_5 *)sub_1249224(), v30 && v30->field_20))
                            {
                                if (!(Behaviour__get_enabled(v30->field_20, 0) & 1))
                                    goto LABEL_10b9a94;
                                if (RaycastHit__get_collider(p, 0) && Component__get_gameObject() && (v31 = (unsigned long)sub_1249224(), ptr->field_78 && (v32 = (unsigned long)sub_1249224(), Transform__get_position(ptr->field_78, 0), v32)))
                                {
                                    LocationDamage__ApplyDamage(v32, ptr->field_70, 1, 0);
                                    break;
                                }
                            }
                        }
                    }
                }
                break;
            case 1:
                if (RaycastHit__get_collider(p, 0) && Component__get_gameObject())
                {
                    v25 = sub_1249224();
                    if (!g_1ef0c58->field_e0)
                        sub_f7da5c(g_1ef0c58);
                    if (!(Object__op_Implicit(v25, 0) & 1))
                        goto LABEL_10b9a94;
                    if (RaycastHit__get_collider(p, 0) && Component__get_gameObject() && sub_1249224())
                    {
                        BreakableObject__ApplyDamage();
                        break;
                    }
                }
                break;
            case 0:
                if (RaycastHit__get_collider(p, 0) && Component__get_gameObject())
                {
                    v15 = sub_1249224();
                    if (!g_1ef0c58->field_e0)
                        sub_f7da5c(g_1ef0c58);
                    if (((char)Object__op_Implicit(v15, 0) & 1))
                    {
                        if (RaycastHit__get_collider(p, 0) && Component__get_gameObject() && sub_1249224() && (AppleFall__ApplyDamage(), ptr->field_98))
                        {
                            FPSPlayer__UpdateHitTime(ptr->field_98);
                            goto LABEL_10b96f0;
                        }
                    }
                    else
                    {
LABEL_10b96f0:
                        if (RaycastHit__get_collider(p, 0) && Component__get_gameObject())
                        {
                            v16 = sub_1249224();
                            if (!g_1ef0c58->field_e0)
                                sub_f7da5c(g_1ef0c58);
                            v17 = Object__op_Implicit(v16, 0);
                            if (RaycastHit__get_collider(p, 0) && Component__get_gameObject())
                            {
                                v18 = sub_1249224();
                                if (!g_1ef0c58->field_e0)
                                    sub_f7da5c(g_1ef0c58);
                                v19 = Object__op_Implicit(v18, 0);
                                if (RaycastHit__get_collider(p, 0) && Component__get_gameObject())
                                {
                                    if (((char)v19 & 1))
                                    {
                                        if (sub_1249224())
                                        {
                                            ExplosiveObject__ApplyDamage();
                                            break;
                                        }
                                    }
                                    else
                                    {
                                        v20 = sub_1249224();
                                        if (!g_1ef0c58->field_e0)
                                            sub_f7da5c(g_1ef0c58);
                                        v21 = Object__op_Implicit(v20, 0);
                                        if (RaycastHit__get_collider(p, 0) && Component__get_gameObject())
                                        {
                                            if (((char)v21 & 1))
                                            {
                                                if (sub_1249224() && (MineExplosion__ApplyDamage(), ptr->field_98))
                                                {
                                                    FPSPlayer__UpdateHitTime(ptr->field_98);
                                                    goto LABEL_10b9a94;
                                                }
                                            }
                                            else
                                            {
                                                v22 = sub_1249224();
                                                if (!g_1ef0c58->field_e0)
                                                    sub_f7da5c(g_1ef0c58);
                                                if (!(Object__op_Implicit(v22, 0) & 1))
                                                    goto LABEL_10b9a94;
                                                if (RaycastHit__get_collider(p, 0) && Component__get_gameObject() && (v23 = (struct_3 *)sub_1249224(), v23 && v23->field_20 && (v24 = (struct_4 *)sub_1249224(v23->field_20, g_1efecc0), v24)))
                                                {
                                                    if (v24->field_20 != 1)
                                                        goto LABEL_10b9a94;
                                                    if (RaycastHit__get_collider(p, 0) && Component__get_gameObject())
                                                    {
                                                        getHit__applyDamage(v23, 0, 1);
                                                        goto LABEL_10b9a94;
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
                break;
            default:
LABEL_10b9a94:
                if (RaycastHit__get_collider(p, 0) && Component__get_gameObject())
                {
                    v33 = sub_1249224();
                    if (!g_1ef0c58->field_e0)
                        sub_f7da5c(g_1ef0c58);
                    if (((char)Object__op_Implicit(v33, 0) & 1))
                    {
                        if (RaycastHit__get_collider(p, 0) && Component__get_gameObject() && (v34 = (struct_6 *)sub_1249224(), v34 && v34->field_20))
                        {
                            if (!(Behaviour__get_enabled(v34->field_20, 0) & 1))
                                goto LABEL_10b9ba8;
                            if (RaycastHit__get_collider(p, 0) && Component__get_gameObject() && (v35 = (unsigned long)sub_1249224(), ptr->field_78 && (v36 = (unsigned long)sub_1249224(), Transform__get_position(ptr->field_78, 0), v36 && (LocationDamage__ApplyDamage(v36, ptr->field_70, 1, 0), ptr->field_98))))
                            {
                                v37 = FPSPlayer__UpdateHitTime(ptr->field_98);
                                goto LABEL_10b9ca4;
                            }
                        }
                    }
                    else
                    {
LABEL_10b9ba8:
                        if (RaycastHit__get_collider(p, 0) && Component__get_gameObject())
                        {
                            v38 = sub_1249224();
                            if (!g_1ef0c58->field_e0)
                                sub_f7da5c(g_1ef0c58);
                            v37 = Object__op_Implicit(v38, 0);
                            if (((char)v37 & 1))
                            {
                                if (RaycastHit__get_collider(p, 0) && Component__get_gameObject() && (v39 = (struct_7 *)sub_1249224(), v39 && v39->field_20 && (v37 = (struct_8 *)sub_1249224(v39->field_20, g_1efecc0), v37)))
                                {
                                    if (v37->field_20 != 1)
                                        goto LABEL_10b9ca4;
                                    if (RaycastHit__get_collider(p, 0) && Component__get_gameObject())
                                    {
                                        v37 = getHit__applyDamage(v39, 0, 1);
                                        goto LABEL_10b9ca4;
                                    }
                                }
                            }
                            else
                            {
LABEL_10b9ca4:
                                if (((char)a2 & 1))
                                    return v37;
                                if (RaycastHit__get_collider(p, 0) && Component__get_gameObject())
                                {
                                    v40 = GameObject__get_tag();
                                    v41 = String__op_Equality(v40, g_1f0a468, 0);
                                    if (((char)v41 & 1))
                                    {
                                        v42 = ptr->field_158 + 1;
                                        ptr->field_158 = v42;
                                        if (3 < v42)
                                            return v41;
                                        v43 = ptr->field_204;
                                        v44 = (((CmpF(v43, 0.0) >> 5 & 3 | CmpF(v43, 0.0) & 1) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - ((CmpF(v43, 0.0) >> 5 & 3 | CmpF(v43, 0.0) & 1) & (CmpF(v43, 0.0) >> 5 & 3 | CmpF(v43, 0.0) & 1) >> 1 & 1);
                                        if (!((char)(v44 * 0x10000000 >> 30)) || ptr->field_229)
                                        {
                                            RaycastHit__get_collider(p, 0);
                                            RaycastHit__get_point(p, 0);
                                            if (ptr->field_78)
                                            {
                                                Transform__get_forward(ptr->field_78, 0);
                                                RaycastHit__get_normal(p, 0);
                                                if (ptr->field_b0)
                                                {
                                                    v45 = WeaponEffects__ImpactEffects();
                                                    return WeaponEffects__ImpactEffects();
                                                }
                                            }
                                        }
                                        else
                                        {
                                            RaycastHit__get_collider(p, 0);
                                            RaycastHit__get_point(p, 0);
                                            if (ptr->field_78)
                                            {
                                                Transform__get_forward(ptr->field_78, 0);
                                                RaycastHit__get_normal(p, 0);
                                                if (ptr->field_b0)
                                                {
                                                    v45 = WeaponEffects__ImpactEffects();
                                                    return WeaponEffects__ImpactEffects();
                                                }
                                            }
                                        }
                                    }
                                    else
                                    {
                                        v46 = ptr->field_204;
                                        v47 = (((CmpF(v46, 0.0) >> 5 & 3 | CmpF(v46, 0.0) & 1) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - ((CmpF(v46, 0.0) >> 5 & 3 | CmpF(v46, 0.0) & 1) & (CmpF(v46, 0.0) >> 5 & 3 | CmpF(v46, 0.0) & 1) >> 1 & 1);
                                        if (!((char)(v47 * 0x10000000 >> 30)) || ptr->field_229)
                                        {
                                            v50 = RaycastHit__get_collider(p, 0);
                                            RaycastHit__get_point(p, 0);
                                            RaycastHit__get_normal(p, 0);
                                            if (ptr->field_b0)
                                            {
                                                WeaponEffects__ImpactEffects(ptr->field_b0, v50, 0, 1, 0);
                                                if (RaycastHit__get_collider(p, 0))
                                                {
                                                    v51 = Collider__get_isTrigger();
                                                    if (((char)v51 & 1))
                                                        return v51;
                                                    v8 = (int)*((int128_t *)&p->field_10[12]);
                                                    v6 = (int)p->field_0;
                                                    *((int128_t *)&v7) = *((int128_t *)&p->field_10[0]);
                                                    if (ptr->field_b0)
                                                    {
                                                        memcpy(&v0, &v6, 16);
                                                        v1 = (int)*((uint128_t *)&v7);
                                                        v2 = (int)*((uint128_t *)(&v7 + 12));
                                                        v52 = WeaponEffects__BulletMarks();
                                                        return WeaponEffects__BulletMarks();
                                                    }
                                                }
                                            }
                                        }
                                        else
                                        {
                                            v48 = RaycastHit__get_collider(p, 0);
                                            RaycastHit__get_point(p, 0);
                                            RaycastHit__get_normal(p, 0);
                                            if (ptr->field_b0)
                                            {
                                                WeaponEffects__ImpactEffects(ptr->field_b0, v48, 0, 0, 0);
                                                if (RaycastHit__get_collider(p, 0))
                                                {
                                                    v49 = Collider__get_isTrigger();
                                                    if (((char)v49 & 1))
                                                        return v49;
                                                    v8 = (int)*((int128_t *)&p->field_10[12]);
                                                    v6 = (int)p->field_0;
                                                    *((int128_t *)&v7) = *((int128_t *)&p->field_10[0]);
                                                    if (ptr->field_b0)
                                                    {
                                                        memcpy(&v3, &v6, 16);
                                                        v4 = (int)*((uint128_t *)&v7);
                                                        v5 = (int)*((uint128_t *)(&v7 + 12));
                                                        v52 = WeaponEffects__BulletMarks();
                                                        return WeaponEffects__BulletMarks();
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
    else if (RaycastHit__get_rigidbody(p, 0))
    {
        if (!(Rigidbody__get_useGravity() & 1))
            goto LABEL_10b95f4;
        v12 = RaycastHit__get_rigidbody(p, 0);
        Time__get_fixedDeltaTime(0);
        RaycastHit__get_point(p, 0);
        if (v12)
        {
            Rigidbody__AddForceAtPosition(v12, 0);
            goto LABEL_10b95f4;
        }
    }
    sub_f7db74();
}
```


## `WeaponBehavior.EmitTracers` — RVA `0xcba17c`

- Decompiled symbol: `WeaponBehavior_EmitTracers`
- Metadata signature: `private IEnumerator EmitTracers(Vector3 tracerDirection) { }`
- Native interval: `144` bytes
- Result: `pseudocode`
- Heuristic layout hint: `WeaponBehavior_Recovered` matched 3 offsets against `WeaponBehavior` metadata (confidence 0.60).

```c
typedef struct WeaponBehavior_Recovered {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[12];
    long long PlayerModelAnim;
    unsigned int tpPistolAnim;
    unsigned int field_2c;
    unsigned int tpShotgunAnim;
} WeaponBehavior_Recovered;

extern long long g_1ef4000;
extern char g_1fab4e7;

struct_0 * WeaponBehavior_EmitTracers(long long a0)
{
    struct_0 *v0;  // x20
    struct_0 *ptr;  // x0
    unsigned int v2;  // s0
    unsigned int v3;  // s1
    unsigned int v4;  // s2

    if (!(g_1fab4e7 & 1))
    {
        sub_f7d92c(&g_1ef4000);
        g_1fab4e7 = 1;
    }
    v0 = sub_f7db70(g_1ef4000);
    Object__ctor(v0, 0);
    ptr = v0;
    ptr->field_10 = 0;
    ptr->field_20 = a0;
    sub_f7d8d0(&ptr->field_20, a0);
    ptr->field_28 = v2;
    ptr->field_2c = v3;
    ptr->field_30 = v4;
    return ptr;
}
```


## `WeaponBehavior.<EmitTracers>d__356.ctor` — RVA `0xcba20c`

- Decompiled symbol: `WeaponBehavior_EmitTracers_d__356_ctor`
- Metadata signature: `public void .ctor(int <>1__state) { }`
- Native interval: `40` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

void WeaponBehavior_EmitTracers_d__356_ctor(struct_0 *ptr, unsigned int a1)
{
    Object__ctor();
    ptr->field_10 = a1;
    return;
}
```


## `WeaponBehavior.MuzzFlash` — RVA `0xcba234`

- Decompiled symbol: `WeaponBehavior_MuzzFlash`
- Metadata signature: `private IEnumerator MuzzFlash() { }`
- Native interval: `116` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[32];
    long long field_20;
} struct_0;

extern long long g_1ef4010;
extern char g_1fab4e8;

struct_0 * WeaponBehavior_MuzzFlash(long long a0)
{
    struct_0 *v0;  // x20
    struct_0 *ptr;  // x0

    if (!(g_1fab4e8 & 1))
    {
        sub_f7d92c(&g_1ef4010);
        g_1fab4e8 = 1;
    }
    v0 = sub_f7db70(g_1ef4010);
    WeaponBehavior_MuzzFlash_d__357__ctor(v0, 0, 0);
    if (v0)
    {
        ptr = v0;
        ptr->field_20 = a0;
        sub_f7d8d0(&ptr->field_20, a0);
        return v0;
    }
    sub_f7db74();
}
```


## `WeaponBehavior.BarrelSmoke` — RVA `0xcba2a8`

- Decompiled symbol: `WeaponBehavior_BarrelSmoke`
- Metadata signature: `private IEnumerator BarrelSmoke() { }`
- Native interval: `108` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[12];
    long long field_20;
} struct_0;

extern long long g_1ef3ff8;
extern char g_1fab4e9;

struct_0 * WeaponBehavior_BarrelSmoke(long long a0)
{
    struct_0 *v0;  // x20
    struct_0 *ptr;  // x0

    if (!(g_1fab4e9 & 1))
    {
        sub_f7d92c(&g_1ef3ff8);
        g_1fab4e9 = 1;
    }
    v0 = sub_f7db70(g_1ef3ff8);
    Object__ctor(v0, 0);
    ptr = v0;
    ptr->field_10 = 0;
    ptr->field_20 = a0;
    sub_f7d8d0(&ptr->field_20, a0);
    return ptr;
}
```


## `WeaponBehavior.<BarrelSmoke>d__358.ctor` — RVA `0xcba314`

- Decompiled symbol: `WeaponBehavior_BarrelSmoke_d__358_ctor`
- Metadata signature: `public void .ctor(int <>1__state) { }`
- Native interval: `40` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

void WeaponBehavior_BarrelSmoke_d__358_ctor(struct_0 *ptr, unsigned int a1)
{
    Object__ctor();
    ptr->field_10 = a1;
    return;
}
```


## `WeaponBehavior.SpawnShell` — RVA `0xcba33c`

- Decompiled symbol: `WeaponBehavior_SpawnShell`
- Metadata signature: `private IEnumerator SpawnShell() { }`
- Native interval: `116` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[32];
    long long field_20;
} struct_0;

extern long long g_1ef4020;
extern char g_1fab4ea;

struct_0 * WeaponBehavior_SpawnShell(long long a0)
{
    struct_0 *v0;  // x20
    struct_0 *ptr;  // x0

    if (!(g_1fab4ea & 1))
    {
        sub_f7d92c(&g_1ef4020);
        g_1fab4ea = 1;
    }
    v0 = sub_f7db70(g_1ef4020);
    WeaponBehavior_SpawnShell_d__359__ctor(v0, 0, 0);
    if (v0)
    {
        ptr = v0;
        ptr->field_20 = a0;
        sub_f7d8d0(&ptr->field_20, a0);
        return v0;
    }
    sub_f7db74();
}
```


## `WeaponBehavior.CheckForReload` — RVA `0xcba3b0`

- Decompiled symbol: `WeaponBehavior_CheckForReload`
- Metadata signature: `public bool CheckForReload() { }`
- Native interval: `200` bytes
- Result: `pseudocode`
- Heuristic layout hint: `WeaponBehavior_Recovered` matched 8 offsets against `WeaponBehavior` metadata (confidence 1.00).

```c
typedef struct WeaponBehavior_Recovered {
    char padding_0[144];
    struct struct_0 *IronsightsComponent;
    char padding_98[8];
    struct struct_1 *InputComponent;
    char padding_a8[128];
    int ammo;
    int bulletsLeft;
    char padding_130[32];
    unsigned int fireRate;
    char padding_154[162];
    char doReload;
    char padding_1f7[5];
    unsigned int shootStartTime;
    char padding_200[453];
    char sprintReloadState;
} WeaponBehavior_Recovered;

typedef struct struct_0 {
    char padding_0[297];
    char field_129;
} struct_0;

typedef struct struct_1 {
    char padding_0[137];
    char field_89;
} struct_1;

extern long long g_1f0d410;
extern char g_1fab4eb;

unsigned int WeaponBehavior_CheckForReload(struct_2 *ptr)
{
    unsigned int v0;  // s1
    unsigned int v1;  // s2
    unsigned int v2;  // s0
    unsigned long v3;  // 4146

    if (!(g_1fab4eb & 1))
    {
        sub_f7d92c(&g_1f0d410);
        g_1fab4eb = 1;
    }
    if (ptr->field_90)
    {
        if (ptr->field_90->field_129 || ptr->field_128 < 1 || !ptr->field_1f6 || *((int *)&ptr->padding_130[0]) <= ptr->field_12c)
            return 0;
        Time__get_time(0);
        v0 = ptr->field_1fc;
        v1 = ptr->field_150;
        v3 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v2 - v0, v1)) >> 5 & 3 | (unsigned long long)(CmpF(v2 - v0, v1) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v2 - v0, v1)) >> 5 & 3 | (unsigned long long)(CmpF(v2 - v0, v1) & 1)) & ((unsigned long long)(char)(CmpF(v2 - v0, v1)) >> 5 & 3 | (unsigned long long)(CmpF(v2 - v0, v1) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if (!((char)v3))
        {
            if (!ptr->field_a0)
            {
                sub_f7db74();
            }
            else if (!ptr->field_a0->field_89)
            {
                ptr->field_3c5 = 1;
                MonoBehaviour__StartCoroutine(ptr, g_1f0d410, 0);
                return 1;
            }
        }
        return 0;
    }
    sub_f7db74();
}
```


## `WeaponBehavior.Reload` — RVA `0xcba478`

- Decompiled symbol: `WeaponBehavior_Reload`
- Metadata signature: `private IEnumerator Reload() { }`
- Native interval: `116` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[32];
    long long field_20;
} struct_0;

extern long long g_1ef4018;
extern char g_1fab4ec;

struct_0 * WeaponBehavior_Reload(long long a0)
{
    struct_0 *v0;  // x20
    struct_0 *ptr;  // x0

    if (!(g_1fab4ec & 1))
    {
        sub_f7d92c(&g_1ef4018);
        g_1fab4ec = 1;
    }
    v0 = sub_f7db70(g_1ef4018);
    WeaponBehavior_Reload_d__361__ctor(v0, 0, 0);
    if (v0)
    {
        ptr = v0;
        ptr->field_20 = a0;
        sub_f7d8d0(&ptr->field_20, a0);
        return v0;
    }
    sub_f7db74();
}
```


## `WeaponBehavior.SprayDirection` — RVA `0xcba4ec`

- Decompiled symbol: `WeaponBehavior_SprayDirection`
- Metadata signature: `private Vector3 SprayDirection() { }`
- Native interval: `384` bytes
- Result: `pseudocode`
- Heuristic layout hint: `WeaponBehavior_Recovered` matched 11 offsets against `WeaponBehavior` metadata (confidence 1.00).

```c
typedef struct WeaponBehavior_Recovered {
    char padding_0[112];
    unsigned long long myTransform;
    char padding_78[8];
    struct struct_0 *FPSWalkerComponent;
    char padding_88[16];
    struct struct_1 *FPSPlayerComponent;
    char padding_a0[24];
    struct struct_2 *CameraControlComponent;
    char padding_c0[284];
    char fireModeSelectable;
    char padding_1dd[1];
    char semiAuto;
    char padding_1df[37];
    unsigned int meleeSwingDelay;
    char padding_208[708];
    int bulletsJustFired;
    char padding_4d0[216];
    unsigned int shotSpread;
    unsigned int shotSpreadAmt;
    char padding_5b0[68];
    char useRecoilIncrease;
} WeaponBehavior_Recovered;

typedef struct struct_0 {
    char padding_0[720];
    char field_2d0;
} struct_0;

typedef struct struct_1 {
    char padding_0[720];
    char field_2d0;
} struct_1;

typedef struct struct_2 {
    char padding_0[262];
    char field_106;
} struct_2;

void WeaponBehavior_SprayDirection(struct_3 *ptr)
{
    unsigned long long v7;  // d12
    unsigned long long v8;  // d11
    unsigned int v17;  // s1
    unsigned int v18;  // s2
    unsigned int v19;  // s1
    unsigned int v20;  // w8
    unsigned long long v9;  // d10
    unsigned long long v10;  // d9
    unsigned long long v11;  // d8
    unsigned long long v12;  // x30
    unsigned long long v13;  // x19
    unsigned int v14;  // s0
    unsigned int v15;  // s1
    unsigned long long v16;  // 4103
    unsigned long long v0;  // [bp-0x40]
    unsigned long long v1;  // [bp-0x30]
    unsigned long long v2;  // [bp-0x28]
    unsigned long long v3;  // [bp-0x20]
    unsigned long long v4;  // [bp-0x18]
    unsigned long long v5;  // [bp-0x10]
    unsigned long long v6;  // [bp-0x8]

    v0 = v7;
    v1 = v8;
    v2 = v9;
    v3 = v10;
    v4 = v11;
    v5 = v12;
    v6 = v13;
    if (ptr->field_80)
    {
        v14 = 0x3f400000;
        if (!ptr->field_80->field_2d0)
            v14 = 0x3f800000;
        if (ptr->field_98)
        {
            if (ptr->field_98->field_2d0 && !((v15 = ptr->field_204, v16 = ((((unsigned long long)(char)(CmpF(v15, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v15, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v15, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v15, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v15, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v15, 0.0) & 1)) >> 1 & 1), !((char)(v16 * 0x10000000 >> 30)))))
            {
                if (ptr->field_1dc && ptr->field_1de)
                {
                    v17 = ptr->field_5a8;
                    v18 = 0x40a00000;
                }
                else
                {
                    v17 = ptr->field_5a8;
                    v18 = 0x40400000;
                }
                v19 = v17 / v18;
            }
            else if (ptr->field_1dc && ptr->field_1de)
            {
                v19 = ptr->field_5a8 * 0x3f000000;
            }
            else
            {
                v19 = ptr->field_5a8;
            }
            v20 = ptr->field_5f4;
            ptr->field_5ac = v14 * v19;
            if (v20 && ptr->field_4cc > *((int *)&ptr[1].padding_0[3]))
                powf();
            Random__get_value(0);
            Random__get_value(0);
            if (ptr->field_b8)
            {
                if (ptr->field_b8->field_106)
                {
                    if (Camera__get_main(0) && Component__get_transform())
                        goto LABEL_10ba620;
                }
                else
                {
                    if (ptr->field_70)
                    {
LABEL_10ba620:
                        Transform__TransformDirection();
                        return;
                    }
                }
            }
        }
    }
    sub_f7db74();
}
```


## `WeaponBehavior.WeaponKick` — RVA `0xcba66c`

- Decompiled symbol: `WeaponBehavior_WeaponKick`
- Metadata signature: `private void WeaponKick() { }`
- Native interval: `900` bytes
- Result: `pseudocode`
- Heuristic layout hint: `WeaponBehavior_Recovered` matched 2 offsets against `WeaponBehavior` metadata (confidence 0.67).

```c
typedef struct struct_3 {
    char padding_0[262];
    char field_106;
} struct_3;

typedef struct struct_4 {
    char padding_0[720];
    char field_2d0;
} struct_4;

typedef struct WeaponBehavior_Recovered {
    char padding_0[160];
    unsigned int InputComponent;
    unsigned int field_a4;
    char MouseLookComponent;
} WeaponBehavior_Recovered;

void* WeaponBehavior_WeaponKick(void* ptr)
{
    char v1[733];  // x8
    unsigned int v2;  // s0
    unsigned int v11;  // s8
    unsigned int v12;  // s0
    unsigned int v13;  // s1
    unsigned int v14;  // s9
    unsigned int v15;  // s1
    unsigned long long v16;  // cc_dep1
    unsigned int v17;  // s0
    unsigned int v18;  // s2
    unsigned long v19;  // 4162
    unsigned long v20;  // 4106
    unsigned long long v3;  // 4103
    unsigned long v21;  // 4106
    unsigned long v22;  // x20
    void* v23;  // x0
    char v24[733];  // x8
    unsigned int v25;  // s0
    struct_5 *p;  // x8
    unsigned int v27;  // s1
    unsigned long v28;  // 4129
    unsigned int v29;  // s1
    unsigned int v30;  // s2
    void* addr;  // x8
    unsigned long v31;  // 4133
    unsigned long v32;  // 4125
    unsigned int v33;  // s0
    unsigned int v34;  // s0
    unsigned long v35;  // 4129
    unsigned int v36;  // s0
    unsigned int v37;  // s1
    unsigned long v38;  // 4133
    unsigned long v39;  // 4125
    unsigned long v5;  // d1
    unsigned long v10;  // d0
    unsigned int v0;  // [bp-0x40]

    if ((long long)ptr[184])
    {
        if (*((char *)((long long)ptr[184] + 262)))
            return ptr;
        if ((long long)ptr[152])
        {
            if (!*((char *)((long long)ptr[152] + 720)))
            {
                v1 = (long long)ptr[128];
                if (v1)
                {
                    if (v1[732])
                        goto LABEL_10ba6cc;
                    *((unsigned int *)&ptr[1496]) = (int)ptr[1480] * 0x3f000000;
LABEL_10ba71c:
                    v10 = [D] unsupported_Iop_ZeroHI64ofV128();
                    v5 = v10 & 4294967295;
                    *((unsigned long *)&ptr[1488]) = v10;
                    goto LABEL_10ba75c;
                }
            }
            else
            {
LABEL_10ba6cc:
                v2 = (int)ptr[516];
                v3 = (((CmpF(v2, 0.0) >> 5 & 3 | CmpF(v2, 0.0) & 1) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - ((CmpF(v2, 0.0) >> 5 & 3 | CmpF(v2, 0.0) & 1) & (CmpF(v2, 0.0) >> 5 & 3 | CmpF(v2, 0.0) & 1) >> 1 & 1);
                if ((char)(v3 * 0x10000000 >> 30))
                {
                    addr = ptr + 1476;
                    *((int *)&ptr[1488]) = (int)ptr[1472];
                    v5 = *((long long *)addr);
                    *((unsigned long *)&addr[16]) = v5;
LABEL_10ba75c:
                    Random__Range(0);
                    v11 = (unsigned int)v5 * 0xc0000000;
                    v12 = (int)ptr[1488] * 0x3fc00000;
                    v13 = (int)ptr[1488] * 2;
                    Random__Range(0);
                    if ((long long)ptr[168])
                    {
                        v14 = v12;
                        if (!*((char *)((long long)ptr[168] + 168)))
                        {
                            Random__get_value(0);
                            v15 = (int)ptr[1496];
                            v16 = ((((CmpF(v12, 0x3f000000) >> 5 & 3 | CmpF(v12, 0x3f000000) & 1) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - ((CmpF(v12, 0x3f000000) >> 5 & 3 | CmpF(v12, 0x3f000000) & 1) & (CmpF(v12, 0x3f000000) >> 5 & 3 | CmpF(v12, 0x3f000000) & 1) >> 1 & 1)) * 0x10000000;
                            v17 = -(v15);
                            v18 = v15 * 0xbf000000;
                            v19 = arm64g_calculate_condition(128, (((((unsigned long long)(char)(CmpF(v12, 0x3f000000)) >> 5 & 3 | (unsigned long long)(CmpF(v12, 0x3f000000) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v12, 0x3f000000)) >> 5 & 3 | (unsigned long long)(CmpF(v12, 0x3f000000) & 1)) & ((unsigned long long)(char)(CmpF(v12, 0x3f000000)) >> 5 & 3 | (unsigned long long)(CmpF(v12, 0x3f000000) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                            if ((char)v19)
                            {
                                v20 = arm64g_calculate_condition(128, v16, 0, 0);
                                if (!((char)v20))
                                    goto LABEL_10ba7ca;
LABEL_10ba7c9:
                                v17 = v15 * 0x3f000000;
                            }
                            else
                            {
                                v21 = arm64g_calculate_condition(128, v16, 0, 0);
                                if ((char)v21)
                                    goto LABEL_10ba7c9;
LABEL_10ba7ca:
                            }
                            Random__Range();
                            v13 = v17 * 0x3f000000;
                            v12 = v17 + v13;
                            *((unsigned int *)&ptr[1540]) = v12;
                        }
                        if ((long long)ptr[120])
                        {
                            Transform__get_localRotation((long long)ptr[120], 0);
                            Quaternion__Internal_ToEulerRad(0);
                            Quaternion__Internal_MakePositive(0);
                            Quaternion__Internal_FromEulerRad(0);
                            v22 = (long long)ptr[120];
                            *((unsigned int *)&ptr[1456]) = (v12 * 1113927393 - v14) * 1016003125;
                            *((unsigned int *)&ptr[1460]) = (v13 * 1113927393 - v11) * 1016003125;
                            *((unsigned int *)&ptr[1464]) = v18 * 1131753712311103125;
                            *((unsigned int *)&ptr[1468]) = 1016003125;
                            if (v22)
                            {
                                Transform__get_localRotation(v22, 0);
                                v0 = 1036831949;
                                Quaternion__Slerp(0);
                                v23 = Transform__set_localRotation(v22, 0);
                                if ((char)ptr[1524])
                                {
                                    v24 = (long long)ptr[128];
                                    if ((int)ptr[1228] > (int)ptr[1528])
                                    {
                                        if (v24 && !v24[732])
                                        {
                                            v25 = (int)ptr[1228] - (int)ptr[1528] + 1;
                                            v23 = powf();
                                            goto LABEL_10ba960;
                                        }
                                    }
                                    else
                                    {
                                        if (v24)
                                        {
                                            v25 = 1067030938;
                                            if (v24[732])
                                                v25 = 0x3f000000;
LABEL_10ba960:
                                            if (!(char)ptr[1508])
                                                return v23;
                                            p = (long long)ptr[168];
                                            if (p)
                                            {
                                                if (p->field_a8)
                                                    return v23;
                                                v27 = (int)ptr[1512];
                                                v28 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v27, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v27, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v27, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v27, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v27, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v27, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                                                if (!((char)v28))
                                                    p->field_a4 = v25 / 0x40c00000 * v14 * 0x3e000000 * v27 + p->field_a4;
                                                v29 = (int)ptr[1516];
                                                v30 = (int)ptr[1520];
                                                v31 = arm64g_calculate_condition(192, (((((unsigned long long)(char)(CmpF(v29, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v29, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v29, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v29, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v29, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v29, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                                                if (!((char)v31))
                                                {
                                                    v32 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v30, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v30, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v30, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v30, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v30, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v30, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                                                    if ((char)v32)
                                                        return v23;
                                                }
                                                v33 = p->field_a0 + v25 * 0x3f000000 * (v11 * 0x3e800000 * v29 + v30);
                                                p->field_a0 = v33;
                                                return v23;
                                            }
                                        }
                                    }
                                }
                                else if (!(char)ptr[1508])
                                {
                                    return v23;
                                }
                                else
                                {
                                    p = (long long)ptr[168];
                                    if (p)
                                    {
                                        if (p->field_a8)
                                            return v23;
                                        v34 = (int)ptr[1512];
                                        v35 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v34, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v34, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v34, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v34, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v34, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v34, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                                        if (!((char)v35))
                                            p->field_a4 = v14 * 0x3e000000 * v34 + p->field_a4;
                                        v36 = (int)ptr[1516];
                                        v37 = (int)ptr[1520];
                                        v38 = arm64g_calculate_condition(192, (((((unsigned long long)(char)(CmpF(v36, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v36, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v36, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v36, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v36, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v36, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                                        if (!((char)v38))
                                        {
                                            v39 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v37, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v37, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v37, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v37, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v37, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v37, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                                            if ((char)v39)
                                                return v23;
                                        }
                                        p->field_a0 = p->field_a0 + v11 * 0x3e800000 * v36 + v37;
                                        return v23;
                                    }
                                }
                            }
                        }
                    }
                }
                else
                {
                    v1 = (long long)ptr[128];
                    *((unsigned int *)&ptr[1496]) = (int)ptr[1480] * 0x3f000000;
                    if (v1)
                        goto LABEL_10ba71c;
                }
            }
        }
    }
    sub_f7db74();
}
```


## `WeaponBehavior.ctor` — RVA `0xcba9f0`

- Decompiled symbol: `WeaponBehavior_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `1180` bytes
- Result: `pseudocode`
- Heuristic layout hint: `WeaponBehavior_Recovered` matched 89 offsets against `WeaponBehavior` metadata (confidence 0.86).

```c
typedef struct WeaponBehavior_Recovered {
    char padding_0[289];
    unsigned short cycleSelect;
    char addsToTotalWeaps;
    char padding_124[24];
    unsigned int damage;
    char padding_140[4];
    unsigned long long force;
    char padding_14c[4];
    unsigned long long fireRate;
    char padding_158[8];
    unsigned int projSpawnForward;
    char padding_164[28];
    unsigned int minimumProjForce;
    char padding_184[16];
    unsigned int CamReleaseAnim1speed;
    char padding_198[4];
    unsigned int CamReleaseAnim2speed;
    char padding_1a0[4];
    unsigned int CamPullAnim1speed;
    char padding_1a8[4];
    unsigned int CamPullAnim2speed;
    char useWeaponKick;
    char padding_1b1[3];
    uint128_t pullTime;
    unsigned int maxHoldTime;
    char padding_1c8[16];
    unsigned int fuseTime;
    char padding_1dc[8];
    unsigned int burstShots;
    char padding_1e8[11];
    char fireableUnderwater;
    char padding_1f4[2];
    char doReload;
    char padding_1f7[5];
    unsigned int shootStartTime;
    char showAimingCrosshair;
    char padding_201[7];
    unsigned int tpMeleeSwingDelay;
    char padding_20c[4];
    uint128_t meleeAttackTime;
    char allowDownwardMelee;
    char padding_221[11];
    unsigned long long verticalDZUpper;
    unsigned int horizontalDZ;
    char canZoom;
    char padding_239[2];
    unsigned short hitCancelsBlock;
    char padding_23d[3];
    unsigned long long blockDefenseAmt;
    char padding_248[4];
    unsigned int zoomFOV;
    char padding_250[4];
    unsigned long long zoomFOVDz;
    char padding_25c[4];
    unsigned long long unzoomXPosition;
    char padding_268[4];
    unsigned long long zoomXPosition;
    char padding_274[4];
    unsigned long long blockRoll;
    unsigned int backstabYPosition;
    char padding_284[4];
    unsigned long long backstabRoll;
    char padding_290[12];
    uint128_t crouchWalkYPosition;
    unsigned long long sprintXPosition;
    char padding_2b4[4];
    unsigned long long walkBobAngles;
    unsigned int field_2c0;
    unsigned long long walkBobPosition;
    unsigned int field_2cc;
    unsigned long long sprintBobAngles;
    unsigned int field_2d8;
    unsigned long long sprintBobPosition;
    unsigned int field_2e4;
    unsigned long long zoomBobAngles;
    unsigned int field_2f0;
    unsigned long long zoomBobPosition;
    unsigned int field_2fc;
    unsigned long long crouchBobAngles;
    unsigned int field_308;
    unsigned long long crouchBobPosition;
    unsigned int field_314;
    unsigned long long proneBobAngles;
    unsigned int field_320;
    unsigned long long proneBobPosition;
    unsigned int field_32c;
    uint128_t swayAmountUnzoomed;
    unsigned int zoomIdleSwayAmt;
    char padding_344[16];
    uint128_t rollSwayAmt;
    unsigned int strafeSideSprint;
    char padding_368[8];
    unsigned long long tpSwingTimeL;
    char padding_378[8];
    unsigned long long gunAngleVel;
    unsigned int field_388;
    unsigned long long gunAnglesTarget;
    unsigned int field_394;
    unsigned long long gunAngles;
    unsigned int field_3a0;
    char canShoot;
    char padding_3a5[23];
    unsigned int reloadTime;
    char padding_3c0[12];
    unsigned long long readyTime;
    char padding_3d4[16];
    unsigned int reloadLastTime;
    char padding_3e8[40];
    unsigned int shotOriginDist;
    char padding_414[60];
    uint128_t muzzleFlashReduction;
    unsigned int field_460;
    char padding_464[12];
    unsigned long long muzzleLightDelay;
    char padding_478[49];
    char muzzActive;
    char padding_4aa[1];
    char useBarrelSmoke;
    char padding_4ac[4];
    unsigned int smokeForward;
    char padding_4b4[36];
    unsigned int barrelSmokeDuration;
    char padding_4dc[1];
    char useMuzzleSmoke;
    char padding_4de[22];
    uint128_t muzzleSmokeColor;
    unsigned int muzzleSmokeAlpha;
    char useTracers;
    char padding_509[103];
    long long materialList;
    unsigned int updateInterval;
    char padding_57c[20];
    uint128_t smoothedColor;
    char padding_5a0[32];
    unsigned long long kickUp;
    unsigned int kickRoll;
    char padding_5cc[12];
    unsigned long long kickRollAmt;
    unsigned int kickBackAmtZoom;
    char padding_5e4[4];
    unsigned long long viewClimbUp;
    unsigned int viewClimbRight;
    char padding_5f4[4];
    unsigned int shotsBeforeRecoil;
    unsigned long long viewKickIncrease;
    char padding_604[76];
    unsigned long long shellScale;
    unsigned int field_658;
    char padding_65c[4];
    uint128_t shellForce;
    unsigned long long shellRotateUp;
    unsigned int shellDuration;
    char padding_67c[44];
    unsigned int fireVol;
    char padding_6ac[60];
    unsigned long long schedulingTime;
    char padding_6f0[8];
    unsigned long long firingPauseMinimumTime;
    char padding_700[88];
    unsigned long long pointRange2Cam;
} WeaponBehavior_Recovered;

typedef struct struct_2 {
    char padding_0[184];
    struct struct_1 *field_b8;
} struct_2;

typedef struct struct_1 {
    unsigned long long field_0;
    unsigned int field_8;
    unsigned long long field_c;
    unsigned int field_14;
} struct_1;

extern long long g_1eed710;
extern struct_2 *g_1ef22e8;
extern long long g_1ef8060;
extern char g_1fab1e1;
extern char g_1fab2c9;
extern char g_1fab4ee;

void WeaponBehavior_ctor(struct_0 *ptr)
{
    unsigned long long v8;  // x30
    unsigned long long v9;  // x24
    unsigned int v18;  // s1
    unsigned int v19;  // s1
    unsigned int v20;  // s1
    unsigned int v21;  // s1
    unsigned int v22;  // s1
    unsigned int v23;  // s1
    unsigned int v24;  // s1
    unsigned int v25;  // s1
    unsigned int v26;  // s1
    unsigned int v27;  // s1
    unsigned long long v10;  // x23
    unsigned int v28;  // s1
    unsigned int v29;  // s1
    unsigned long long v30;  // d0
    unsigned int v31;  // s1
    long long v32;  // x20
    unsigned long long v11;  // x22
    unsigned long long v12;  // x21
    unsigned long long v13;  // x20
    unsigned long long v14;  // x19
    struct_0 *p;  // x21
    uint128_t v16;  // q2
    struct_2 *pos;  // x8
    uint128_t v0;  // [bp-0x50]
    unsigned long long v1;  // [bp-0x40]
    unsigned long long v2;  // [bp-0x30]
    unsigned long long v3;  // [bp-0x28]
    unsigned long long v4;  // [bp-0x20]
    unsigned long long v5;  // [bp-0x18]
    unsigned long long v6;  // [bp-0x10]
    unsigned long long v7;  // [bp-0x8]

    v1 = v8;
    v2 = v9;
    v3 = v10;
    v4 = v11;
    v5 = v12;
    v6 = v13;
    v7 = v14;
    p = &ptr->field_1ac;
    if (!(g_1fab4ee & 1))
    {
        sub_f7d92c(&g_1ef8060);
        sub_f7d92c(&g_1eed710);
        g_1fab4ee = 1;
    }
    *((unsigned short *)&(&ptr->padding_0)[1]) = 257;
    *((unsigned int *)&ptr->padding_124[23]) = 10;
    *((char *)&ptr->field_121 + 1) = 1;
    *((unsigned long long *)&ptr->padding_140) = 4812096201845375176;
    *((unsigned long long *)&ptr->padding_14c) = 5331396592;
    *((unsigned int *)&ptr->padding_164[20]) = 0x3fc00000;
    *((unsigned int *)&ptr->padding_158[0]) = 0x3f000000;
    *((unsigned int *)&ptr->padding_184[8]) = 0x3f800000;
    ptr->field_194 = 0x3f800000;
    ptr->field_19c = 0x3f800000;
    ptr->field_1a4 = 0x3f800000;
    ptr->padding_1a8[0] = 1;
    *((unsigned long long *)&p->padding_0[0]) = 0x3f0000003f000000 CONCAT 0x3f0000003f000000;
    *((unsigned int *)((char *)&ptr->field_1b4 + 4)) = 0x40400000;
    *((unsigned int *)&ptr->padding_1c8[4]) = 0x40000000;
    ptr->field_1d8 = 3;
    *((unsigned int *)&ptr->padding_1e8[8]) = 0xc1800000;
    *((char *)&ptr->field_1e4 + 3) = 1;
    ptr->padding_1e8[2] = 1;
    ptr->padding_1f4[0] = 1;
    ptr->field_1fc = 0x3f800000;
    *((char *)&ptr->field_210) = 1;
    *((uint128_t *)&ptr->padding_201[3]) = 88767507113241082517942889968075119002;
    *((unsigned long long *)&p->padding_0[120]) = 0x4140000041f80000;
    *((unsigned int *)&ptr->padding_221[3]) = 0x42400000;
    ptr->padding_221[7] = 1;
    *((unsigned short *)&ptr->padding_221[10]) = 257;
    ptr->field_22c = 0x3ee666663f000000;
    *((unsigned int *)&ptr->field_238) = 0x425c0000;
    *((unsigned long long *)&p->padding_0[160]) = 0x3e99999a42540000;
    *((unsigned long long *)&ptr->padding_248) = 4345995260147783434;
    *((unsigned long long *)&p->padding_0[184]) = 4396377932374694953;
    *((unsigned long long *)&ptr->padding_25c) = 0xbd8f5c2941f00000;
    *((unsigned long long *)&ptr->padding_268) = 0x3f80000041f00000;
    *((unsigned int *)&ptr->field_260) = 1023611503;
    *((uint128_t *)&p->padding_0[232]) = 249910814033910460654181279820824172298;
    *((unsigned long long *)&p->padding_0[248]) = 4320573338001447322;
    if (!g_1fab1e1)
    {
        sub_f7d92c(&g_1ef22e8);
        g_1fab1e1 = 1;
    }
    v16 = 0x3f8000003f800000 CONCAT 0x3f8000003f800000;
    pos = g_1ef22e8;
    v18 = *((int *)((char *)&g_1ef22e8->field_b8->field_c + 4));
    *((long long *)&ptr->padding_290[0]) = *((long long *)&(&g_1ef22e8->field_b8->field_8)[1]);
    *((unsigned int *)&ptr->padding_290[8]) = v18;
    v19 = *((int *)((char *)&g_1ef22e8->field_b8->field_c + 4));
    *((long long *)&p->padding_0[272]) = *((long long *)&(&g_1ef22e8->field_b8->field_8)[1]);
    *((unsigned int *)&(&ptr->padding_290)[1 + 8]) = v19;
    v20 = *((int *)((char *)&g_1ef22e8->field_b8->field_c + 4));
    *((long long *)&ptr->field_29c) = *((long long *)&(&g_1ef22e8->field_b8->field_8)[1]);
    *((unsigned int *)((char *)&ptr->field_29c + 8)) = v20;
    v21 = *((int *)((char *)&g_1ef22e8->field_b8->field_c + 4));
    *((long long *)&p->padding_124[3]) = *((long long *)&(&g_1ef22e8->field_b8->field_8)[1]);
    *((unsigned int *)((char *)&ptr->field_2ac + 4)) = v21;
    v22 = *((int *)((char *)&g_1ef22e8->field_b8->field_c + 4));
    *((long long *)&ptr->padding_2b4) = *((long long *)&(&g_1ef22e8->field_b8->field_8)[1]);
    *((unsigned int *)&ptr->field_2b8) = v22;
    v23 = *((int *)((char *)&g_1ef22e8->field_b8->field_c + 4));
    *((long long *)&p->field_13c) = *((long long *)&(&g_1ef22e8->field_b8->field_8)[1]);
    (&ptr->field_2c0)[1] = v23;
    v24 = *((int *)((char *)&g_1ef22e8->field_b8->field_c + 4));
    ptr->field_2c4 = *((long long *)&(&g_1ef22e8->field_b8->field_8)[1]);
    ptr->field_2cc = v24;
    v25 = *((int *)((char *)&g_1ef22e8->field_b8->field_c + 4));
    p->field_150 = *((long long *)&(&g_1ef22e8->field_b8->field_8)[1]);
    *((unsigned int *)((char *)&ptr->field_2d0 + 4)) = v25;
    v26 = *((int *)((char *)&g_1ef22e8->field_b8->field_c + 4));
    *((long long *)&ptr->field_2d8) = *((long long *)&(&g_1ef22e8->field_b8->field_8)[1]);
    *((unsigned int *)&ptr->field_2dc) = v26;
    v27 = *((int *)((char *)&g_1ef22e8->field_b8->field_c + 4));
    *((long long *)&p->padding_164[4]) = *((long long *)&(&g_1ef22e8->field_b8->field_8)[1]);
    (&ptr->field_2e4)[1] = v27;
    *((uint128_t *)&ptr->field_2e8) = v16;
    *((unsigned int *)&ptr->field_2f4) = 0x3f800000;
    *((uint128_t *)&p->padding_198) = 0x3e4ccccd3f0000003f00000041f00000;
    *((unsigned int *)((char *)&ptr->field_30c + 4)) = 1045220557;
    ptr->field_318 = 4503599628411690025;
    v0 = v16;
    if (!g_1fab2c9)
    {
        sub_f7d92c(&g_1ef22e8);
        v16 = v0;
        pos = g_1ef22e8;
        g_1fab2c9 = 1;
    }
    v28 = pos->field_b8->field_8;
    ptr->field_324 = pos->field_b8->field_0;
    ptr->field_32c = v28;
    v29 = pos->field_b8->field_8;
    *((unsigned long long *)&p->padding_1c8[4]) = pos->field_b8->field_0;
    *((unsigned int *)((char *)&ptr->field_330 + 4)) = v29;
    v30 = pos->field_b8->field_0;
    v31 = pos->field_b8->field_8;
    ptr->padding_344[0] = 1;
    *((unsigned long long *)((char *)&ptr->field_330 + 8)) = v30;
    ptr->field_340 = v31;
    *((unsigned int *)&(&ptr->padding_344)[1 + 8]) = 0x3fe00000;
    *((unsigned long long *)&p->padding_20c) = 4525216907499510170;
    *((unsigned int *)((char *)&ptr->field_370 + 4)) = 1067030938;
    *((unsigned int *)&ptr->field_398) = 0x3f000000;
    *((unsigned int *)&ptr->padding_414[32]) = 1041865114;
    *((unsigned int *)((char *)&ptr->field_450 + 8)) = 1051931443;
    *((uint128_t *)&ptr->padding_3d4[0]) = 0x3f8000003f8000003f80000040d00000;
    ptr->field_3e4 = 0;
    *((unsigned long long *)&ptr->padding_3e8[12]) = 4812096202882206925;
    ptr->padding_414[25] = 1;
    ptr->padding_414[27] = 1;
    *((char *)&ptr->field_450 + 13) = 1;
    *((uint128_t *)&p->field_2f4) = v16;
    *((unsigned int *)&ptr->padding_478[12]) = 0x3e800000;
    ptr->padding_478[16] = 1;
    v32 = sub_f7db70(g_1eed710);
    sub_14a2b64(v32, g_1ef8060);
    *((long long *)&ptr->padding_4de[18]) = v32;
    sub_f7d8d0(&ptr->padding_4de[18], v32);
    *((unsigned int *)&(&ptr->padding_4de)[1 + 4]) = 0x3e800000;
    *((uint128_t *)&ptr->field_504) = v0;
    *((unsigned int *)&ptr->padding_509[51]) = 0x41700000;
    *((unsigned int *)&ptr->padding_509[75]) = 3163511849;
    *((unsigned int *)&ptr->padding_509[91]) = 0x3f400000;
    *((unsigned long long *)&ptr->padding_509[67]) = 0xbccccccd41a00000;
    *((unsigned long long *)&ptr->padding_509[43]) = 0x4000000040e00000;
    *((unsigned int *)&ptr->padding_509[99]) = 4;
    *((unsigned long long *)&ptr->padding_509[83]) = 0x3f8000003f800000;
    p->field_3cc = 0x400000003fe00000;
    ptr->field_5c8 = 0x3f800000;
    *((uint128_t *)&ptr->padding_5cc[4]) = 82146290175005731576521198532001844429;
    *((unsigned int *)&ptr->field_5e8) = 5;
    *((unsigned int *)&ptr->padding_604[16]) = 1063675494;
    ptr->field_5c0 = 0x3f8000003f800000;
    *((unsigned long long *)&ptr->field_5e0) = 0x3e8000003e800000;
    ptr->field_650 = 4591870180066957722;
    *((unsigned long long *)&(&ptr->padding_65c)[1]) = 4587366580439587226;
    *((unsigned long long *)&ptr->padding_6ac[12]) = 0x3e4ccccd41000000;
}
```


## `WeaponBehavior.<BarrelSmoke>d__358.Dispose` — RVA `0xcbae8c`

- Decompiled symbol: `WeaponBehavior_BarrelSmoke_d__358_Dispose`
- Metadata signature: `private void System.IDisposable.Dispose() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long WeaponBehavior_BarrelSmoke_d__358_Dispose(void)
{
    unsigned long v0;  // x0

    return v0;
}
```


## `WeaponBehavior.<BarrelSmoke>d__358.MoveNext` — RVA `0xcbae90`

- Decompiled symbol: `WeaponBehavior_BarrelSmoke_d__358_MoveNext`
- Metadata signature: `private bool MoveNext() { }`
- Native interval: `1308` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: Decompiler produced no C-like text

```c
// 0x10bae90: sub sp, sp, #0xc0
// 0x10bae94: stp d15, d14, [sp, #0x60]
// 0x10bae98: stp d13, d12, [sp, #0x70]
// 0x10bae9c: stp d11, d10, [sp, #0x80]
// 0x10baea0: stp d9, d8, [sp, #0x90]
// 0x10baea4: stp x30, x21, [sp, #0xa0]
// 0x10baea8: stp x20, x19, [sp, #0xb0]
// 0x10baeac: adrp x20, #0x1fab000
// 0x10baeb0: ldrb w8, [x20, #0x4ef]
// 0x10baeb4: mov x19, x0
// 0x10baeb8: tbnz w8, #0, #0x10baed0
// 0x10baebc: adrp x0, #0x1e8d000
// 0x10baec0: ldr x0, [x0, #0x3e8]
// 0x10baec4: bl #0xf7d92c
// 0x10baec8: mov w8, #1
// 0x10baecc: strb w8, [x20, #0x4ef]
// 0x10baed0: movi v0.2d, #0000000000000000
// 0x10baed4: str xzr, [sp, #0x58]
// 0x10baed8: stp q0, q0, [sp, #0x30]
// 0x10baedc: ldr w8, [x19, #0x10]
// 0x10baee0: ldr x21, [x19, #0x20]
// 0x10baee4: subs w8, w8, #2
// 0x10baee8: b.lo #0x10baf68
// 0x10baeec: cmp w8, #2
// 0x10baef0: b.hs #0x10bafcc
// 0x10baef4: mov w8, #-1
// 0x10baef8: str w8, [x19, #0x10]
// 0x10baefc: cbz x21, #0x10bb3a8
// 0x10baf00: ldr s8, [x19, #0x28]
// 0x10baf04: ldr s9, [x21, #0x4d8]
// 0x10baf08: mov x0, xzr
// 0x10baf0c: bl #0x1b9ad30
// 0x10baf10: fadd s1, s8, s9
// 0x10baf14: fcmp s1, s0
// 0x10baf18: b.le #0x10baf5c
// 0x10baf1c: ldr s8, [x21, #0x224]
// 0x10baf20: ldr s9, [x21, #0x210]
// 0x10baf24: mov x0, xzr
// 0x10baf28: bl #0x1b9ad30
// 0x10baf2c: fadd s1, s8, s9
// 0x10baf30: fcmp s1, s0
// 0x10baf34: b.pl #0x10baf58
// 0x10baf38: ldr x8, [x21, #0x80]
// 0x10baf3c: cbz x8, #0x10bb3a8
// 0x10baf40: ldrb w8, [x8, #0x2b1]
// 0x10baf44: cbnz w8, #0x10baf58
// 0x10baf48: ldr x8, [x21, #0x88]
// 0x10baf4c: cbz x8, #0x10bb3a8
// 0x10baf50: ldrb w8, [x8, #0x17e]
// 0x10baf54: cbz w8, #0x10bb01c
// 0x10baf58: strb wzr, [x21, #0x4dc]
// 0x10baf5c: mov w0, wzr
// 0x10baf60: strb wzr, [x21, #0x4dc]
// 0x10baf64: b #0x10baffc
// 0x10baf68: mov w8, #-1
// 0x10baf6c: str w8, [x19, #0x10]
// 0x10baf70: cbz x21, #0x10bb3a8
// 0x10baf74: ldrb w8, [x21, #0x4a9]
// 0x10baf78: cbz w8, #0x10bafd4
// 0x10baf7c: mov x0, xzr
// 0x10baf80: bl #0x1b9ad30
// 0x10baf84: str s0, [x19, #0x28]
// 0x10baf88: adrp x8, #0x1e8d000
// 0x10baf8c: ldr x8, [x8, #0x3e8]
// 0x10baf90: ldr x0, [x8]
// 0x10baf94: bl #0xf7db70
// 0x10baf98: adrp x8, #0x832000
// 0x10baf9c: ldr s0, [x8, #0x3c8]
// 0x10bafa0: mov x1, xzr
// 0x10bafa4: mov x20, x0
// 0x10bafa8: bl #0x1b99b00
// 0x10bafac: str x20, [x19, #0x18]!
// 0x10bafb0: mov x0, x19
// 0x10bafb4: mov x1, x20
// 0x10bafb8: bl #0xf7d8d0
// 0x10bafbc: mov w8, #2
// 0x10bafc0: stur w8, [x19, #-8]
// 0x10bafc4: mov w0, #1
// 0x10bafc8: b #0x10baffc
// 0x10bafcc: mov w0, wzr
// 0x10bafd0: b #0x10baffc
// 0x10bafd4: ldr x8, [x21, #0xb8]
// 0x10bafd8: cbz x8, #0x10bb3a8
// 0x10bafdc: ldrb w8, [x8, #0x106]
// 0x10bafe0: cbz w8, #0x10baf7c
// 0x10bafe4: str xzr, [x19, #0x18]!
// 0x10bafe8: mov x0, x19
// 0x10bafec: mov x1, xzr
// 0x10baff0: bl #0xf7d8d0
// 0x10baff4: mov w0, #1
// 0x10baff8: stur w0, [x19, #-8]
// 0x10baffc: ldp x20, x19, [sp, #0xb0]
// 0x10bb000: ldp x30, x21, [sp, #0xa0]
// 0x10bb004: ldp d9, d8, [sp, #0x90]
// 0x10bb008: ldp d11, d10, [sp, #0x80]
// 0x10bb00c: ldp d13, d12, [sp, #0x70]
// 0x10bb010: ldp d15, d14, [sp, #0x60]
// 0x10bb014: add sp, sp, #0xc0
// 0x10bb018: ret
// 0x10bb01c: ldr x8, [x21, #0xa0]
// 0x10bb020: cbz x8, #0x10bb3a8
// 0x10bb024: ldrb w8, [x8, #0x89]
// 0x10bb028: cbz w8, #0x10bb03c
// 0x10bb02c: ldr x8, [x21, #0x90]
// 0x10bb030: cbz x8, #0x10bb3a8
// 0x10bb034: ldrb w8, [x8, #0x129]
// 0x10bb038: cbz w8, #0x10bb1ac
// 0x10bb03c: ldr x8, [x21, #0xb8]
// 0x10bb040: cbz x8, #0x10bb3a8
// 0x10bb044: ldrb w8, [x8, #0x106]
// 0x10bb048: cbz w8, #0x10bb07c
// 0x10bb04c: ldr x0, [x21, #0x4b8]
// 0x10bb050: cbz x0, #0x10bb3a8
// 0x10bb054: mov x1, xzr
// 0x10bb058: bl #0x1b92154
// 0x10bb05c: ldr x8, [x21, #0x4a0]
// 0x10bb060: cbz x8, #0x10bb3a8
// 0x10bb064: mov x20, x0
// 0x10bb068: mov x0, x8
// 0x10bb06c: mov x1, xzr
// 0x10bb070: bl #0x1b9d508
// 0x10bb074: cbnz x20, #0x10bb26c
// 0x10bb078: b #0x10bb3a8
// 0x10bb07c: ldr x8, [x21, #0x98]
// 0x10bb080: cbz x8, #0x10bb3a8
// 0x10bb084: ldrb w8, [x8, #0x2d0]
// 0x10bb088: cbz w8, #0x10bb09c
// 0x10bb08c: ldr x8, [x21, #0xc0]
// 0x10bb090: cbz x8, #0x10bb3a8
// 0x10bb094: ldrb w8, [x8, #0x6a]
// 0x10bb098: cbz w8, #0x10bb1e0
// 0x10bb09c: ldr x0, [x21, #0x4b8]
// 0x10bb0a0: cbz x0, #0x10bb3a8
// 0x10bb0a4: mov x1, xzr
// 0x10bb0a8: bl #0x1b92154
// 0x10bb0ac: ldr x8, [x21, #0x78]
// 0x10bb0b0: cbz x8, #0x10bb3a8
// 0x10bb0b4: mov x20, x0
// 0x10bb0b8: mov x0, x8
// 0x10bb0bc: mov x1, xzr
// 0x10bb0c0: bl #0x1b9d508
// 0x10bb0c4: ldr x0, [x21, #0x78]
// 0x10bb0c8: cbz x0, #0x10bb3a8
// 0x10bb0cc: mov x1, xzr
// 0x10bb0d0: mov v8.16b, v0.16b
// 0x10bb0d4: mov v9.16b, v1.16b
// 0x10bb0d8: mov v11.16b, v2.16b
// 0x10bb0dc: bl #0x1b9d8c8
// 0x10bb0e0: ldr x0, [x21, #0x78]
// 0x10bb0e4: str s0, [sp, #0xc]
// 0x10bb0e8: cbz x0, #0x10bb3a8
// 0x10bb0ec: stp s9, s8, [sp, #4]
// 0x10bb0f0: ldr s9, [x21, #0x4c0]
// 0x10bb0f4: mov x1, xzr
// 0x10bb0f8: mov v12.16b, v1.16b
// 0x10bb0fc: mov v15.16b, v2.16b
// 0x10bb100: bl #0x1b9d940
// 0x10bb104: ldr x0, [x21, #0x78]
// 0x10bb108: cbz x0, #0x10bb3a8
// 0x10bb10c: ldr s10, [x21, #0x4c4]
// 0x10bb110: mov x1, xzr
// 0x10bb114: mov v13.16b, v0.16b
// 0x10bb118: mov v14.16b, v1.16b
// 0x10bb11c: mov v8.16b, v2.16b
// 0x10bb120: bl #0x1b9d9b8
// 0x10bb124: cbz x20, #0x10bb3a8
// 0x10bb128: ldr s22, [sp, #4]
// 0x10bb12c: fmul s7, s12, s9
// 0x10bb130: ldr s16, [sp, #0xc]
// 0x10bb134: ldr s3, [x21, #0x4b0]
// 0x10bb138: fadd s7, s22, s7
// 0x10bb13c: ldr s22, [sp, #8]
// 0x10bb140: ldr s4, [x21, #0x4c8]
// 0x10bb144: ldr s17, [x21, #0x434]
// 0x10bb148: ldr s20, [x21, #0x430]
// 0x10bb14c: ldr s21, [x21, #0x42c]
// 0x10bb150: fmul s5, s15, s9
// 0x10bb154: fmul s16, s16, s9
// 0x10bb158: fmul s6, s8, s10
// 0x10bb15c: fmul s18, s14, s10
// 0x10bb160: fmul s19, s13, s10
// 0x10bb164: fadd s5, s11, s5
// 0x10bb168: fadd s16, s22, s16
// 0x10bb16c: fadd s5, s5, s6
// 0x10bb170: fadd s6, s7, s18
// 0x10bb174: fadd s7, s16, s19
// 0x10bb178: fmul s2, s2, s3
// 0x10bb17c: fmul s1, s1, s3
// 0x10bb180: fmul s0, s0, s3
// 0x10bb184: fmul s16, s4, s17
// 0x10bb188: fmul s17, s4, s20
// 0x10bb18c: fmul s3, s4, s21
// 0x10bb190: fadd s2, s5, s2
// 0x10bb194: fadd s1, s6, s1
// 0x10bb198: fadd s0, s7, s0
// 0x10bb19c: fadd s2, s2, s16
// 0x10bb1a0: fadd s1, s1, s17
// 0x10bb1a4: fadd s0, s0, s3
// 0x10bb1a8: b #0x10bb26c
// 0x10bb1ac: ldr s8, [x21, #0x1fc]
// 0x10bb1b0: mov x0, xzr
// 0x10bb1b4: bl #0x1b9ad30
// 0x10bb1b8: adrp x8, #0x832000
// 0x10bb1bc: ldr s1, [x8, #0x3b8]
// 0x10bb1c0: fadd s1, s8, s1
// 0x10bb1c4: fcmp s1, s0
// 0x10bb1c8: b.pl #0x10bb390
// 0x10bb1cc: ldr x8, [x21, #0xa0]
// 0x10bb1d0: cbz x8, #0x10bb3a8
// 0x10bb1d4: ldrb w8, [x8, #0x89]
// 0x10bb1d8: cbnz w8, #0x10bb03c
// 0x10bb1dc: b #0x10bb390
// 0x10bb1e0: ldr x0, [x21, #0x4b8]
// 0x10bb1e4: cbz x0, #0x10bb3a8
// 0x10bb1e8: mov x1, xzr
// 0x10bb1ec: bl #0x1b92154
// 0x10bb1f0: ldr x8, [x21, #0x78]
// 0x10bb1f4: cbz x8, #0x10bb3a8
// 0x10bb1f8: mov x20, x0
// 0x10bb1fc: mov x0, x8
// 0x10bb200: mov x1, xzr
// 0x10bb204: bl #0x1b9d508
// 0x10bb208: ldr x0, [x21, #0x78]
// 0x10bb20c: cbz x0, #0x10bb3a8
// 0x10bb210: mov x1, xzr
// 0x10bb214: mov v8.16b, v0.16b
// 0x10bb218: mov v9.16b, v1.16b
// 0x10bb21c: mov v10.16b, v2.16b
// 0x10bb220: bl #0x1b9d9b8
// 0x10bb224: cbz x20, #0x10bb3a8
// 0x10bb228: ldr s3, [x21, #0x4b0]
// 0x10bb22c: ldr s4, [x21, #0x4c8]
// 0x10bb230: ldr s5, [x21, #0x434]
// 0x10bb234: ldr s6, [x21, #0x430]
// 0x10bb238: ldr s7, [x21, #0x42c]
// 0x10bb23c: fmul s2, s2, s3
// 0x10bb240: fmul s1, s1, s3
// 0x10bb244: fmul s0, s0, s3
// 0x10bb248: fmul s3, s4, s5
// 0x10bb24c: fmul s5, s4, s6
// 0x10bb250: fmul s4, s4, s7
// 0x10bb254: fadd s2, s10, s2
// 0x10bb258: fadd s1, s9, s1
// 0x10bb25c: fadd s0, s8, s0
// 0x10bb260: fadd s2, s2, s3
// 0x10bb264: fadd s1, s1, s5
// 0x10bb268: fadd s0, s0, s4
// 0x10bb26c: mov x0, x20
// 0x10bb270: mov x1, xzr
// 0x10bb274: bl #0x1b9d5a8
// 0x10bb278: mov x0, xzr
// 0x10bb27c: bl #0x1b9ae58
// 0x10bb280: fcmp s0, #0.0
// 0x10bb284: b.le #0x10bb390
// 0x10bb288: ldr x20, [x21, #0x4b8]
// 0x10bb28c: cbz x20, #0x10bb3a8
// 0x10bb290: mov x0, x20
// 0x10bb294: mov x1, xzr
// 0x10bb298: bl #0x1bc9cb4
// 0x10bb29c: str x0, [sp, #0x58]
// 0x10bb2a0: add x8, sp, #0x10
// 0x10bb2a4: add x0, sp, #0x58
// 0x10bb2a8: mov x1, xzr
// 0x10bb2ac: bl #0x1bc9f50
// 0x10bb2b0: ldp q0, q1, [sp, #0x10]
// 0x10bb2b4: add x0, sp, #0x30
// 0x10bb2b8: mov x1, xzr
// 0x10bb2bc: stp q0, q1, [sp, #0x30]
// 0x10bb2c0: bl #0x1bca508
// 0x10bb2c4: adrp x21, #0x1fab000
// 0x10bb2c8: ldrb w8, [x21, #0x242]
// 0x10bb2cc: mov v8.16b, v0.16b
// 0x10bb2d0: cbnz w8, #0x10bb2e8
// 0x10bb2d4: adrp x0, #0x1e8c000
// 0x10bb2d8: ldr x0, [x0, #0xa60]
// 0x10bb2dc: bl #0xf7d92c
// 0x10bb2e0: mov w8, #1
// 0x10bb2e4: strb w8, [x21, #0x242]
// 0x10bb2e8: adrp x8, #0x1e8c000
// 0x10bb2ec: ldr x8, [x8, #0xa60]
// 0x10bb2f0: ldr x0, [x8]
// 0x10bb2f4: ldr w8, [x0, #0xe0]
// 0x10bb2f8: cbnz w8, #0x10bb300
// 0x10bb2fc: bl #0xf7da5c
// 0x10bb300: fcvt d9, s8
// 0x10bb304: add x0, sp, #0x10
// 0x10bb308: mov v0.16b, v9.16b
// 0x10bb30c: bl #0x1db0c60
// 0x10bb310: fcmp s8, #0.0
// 0x10bb314: b.ge #0x10bb330
// 0x10bb318: fmov d1, #-0.50000000
// 0x10bb31c: fcmp d0, d1
// 0x10bb320: b.ne #0x10bb358
// 0x10bb324: ldr d0, [sp, #0x10]
// 0x10bb328: fmov d1, #-1.00000000
// 0x10bb32c: b #0x10bb344
// 0x10bb330: fmov d1, #0.50000000
// 0x10bb334: fcmp d0, d1
// 0x10bb338: b.ne #0x10bb364
// 0x10bb33c: ldr d0, [sp, #0x10]
// 0x10bb340: fmov d1, #1.00000000
// 0x10bb344: fcvtzs x8, d0
// 0x10bb348: fadd d1, d0, d1
// 0x10bb34c: tst x8, #1
// 0x10bb350: fcsel d0, d0, d1, eq
// 0x10bb354: b #0x10bb36c
// 0x10bb358: fadd d0, d9, d1
// 0x10bb35c: frintp d0, d0
// 0x10bb360: b #0x10bb36c
// 0x10bb364: fadd d0, d9, d1
// 0x10bb368: frintm d0, d0
// 0x10bb36c: mov x8, #0x7ff0000000000000
// 0x10bb370: fmov d1, x8
// 0x10bb374: fcvtzs w9, d0
// 0x10bb378: fcmp d0, d1
// 0x10bb37c: mov w8, #-0x80000000
// 0x10bb380: csel w1, w8, w9, eq
// 0x10bb384: mov x0, x20
// 0x10bb388: mov x2, xzr
// 0x10bb38c: bl #0x1bc9b7c
// 0x10bb390: str xzr, [x19, #0x18]!
// 0x10bb394: mov x0, x19
// 0x10bb398: mov x1, xzr
// 0x10bb39c: bl #0xf7d8d0
// 0x10bb3a0: mov w8, #3
// 0x10bb3a4: b #0x10bafc0
// 0x10bb3a8: bl #0xf7db74
```


## `WeaponBehavior.<BarrelSmoke>d__358.get_Current` — RVA `0xcbb3ac`

- Decompiled symbol: `WeaponBehavior_BarrelSmoke_d__358_get_Current`
- Metadata signature: `private object System.Collections.Generic.IEnumerator<System.Object>.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long WeaponBehavior_BarrelSmoke_d__358_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```


## `WeaponBehavior.<BarrelSmoke>d__358.Reset` — RVA `0xcbb3b4`

- Decompiled symbol: `WeaponBehavior_BarrelSmoke_d__358_Reset`
- Metadata signature: `private void System.Collections.IEnumerator.Reset() { }`
- Native interval: `56` bytes
- Result: `pseudocode`

```c
extern long long g_1ef0bd8;
extern long long g_1f05360;

void WeaponBehavior_BarrelSmoke_d__358_Reset(void)
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
    sub_f7da4c(v4, sub_f7d940(&g_1f05360));
}
```


## `WeaponBehavior.<BarrelSmoke>d__358.get_Current` — RVA `0xcbb3ec`

- Decompiled symbol: `WeaponBehavior_BarrelSmoke_d__358_get_Current`
- Metadata signature: `private object System.Collections.IEnumerator.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long WeaponBehavior_BarrelSmoke_d__358_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```


## `WeaponBehavior.<EmitTracers>d__356.Dispose` — RVA `0xcbb3f4`

- Decompiled symbol: `WeaponBehavior_EmitTracers_d__356_Dispose`
- Metadata signature: `private void System.IDisposable.Dispose() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long WeaponBehavior_EmitTracers_d__356_Dispose(void)
{
    unsigned long v0;  // x0

    return v0;
}
```


## `WeaponBehavior.<EmitTracers>d__356.MoveNext` — RVA `0xcbb3f8`

- Decompiled symbol: `WeaponBehavior_EmitTracers_d__356_MoveNext`
- Metadata signature: `private bool MoveNext() { }`
- Native interval: `644` bytes
- Result: `pseudocode`

```c
typedef struct struct_4 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[4];
    unsigned long long field_18;
    struct struct_3 *field_20;
} struct_4;

typedef struct struct_3 {
    char padding_0[120];
    long long field_78;
    char padding_80[16];
    struct struct_0 *field_90;
    struct struct_1 *field_98;
    char padding_a0[16];
    unsigned long long field_b0;
    struct struct_2 *field_b8;
    char padding_c0[876];
    unsigned int field_42c;
    unsigned int field_430;
    unsigned int field_434;
    char padding_438[104];
    long long field_4a0;
    char padding_4a8[1];
    char field_4a9;
    char padding_4aa[6];
    unsigned int field_4b0;
    char padding_4b4[88];
    unsigned int field_50c;
    unsigned int field_510;
    unsigned int field_514;
    char padding_518[12];
    unsigned int field_524;
    unsigned int field_528;
    unsigned int field_52c;
} struct_3;

typedef struct struct_2 {
    char padding_0[262];
    char field_106;
} struct_2;

typedef struct struct_0 {
    char padding_0[297];
    char field_129;
} struct_0;

typedef struct struct_1 {
    char padding_0[720];
    char field_2d0;
} struct_1;

unsigned int WeaponBehavior_EmitTracers_d__356_MoveNext(struct_4 *p)
{
    struct_3 *ptr;  // x21
    struct_2 *v1;  // x8
    unsigned int v9;  // s1
    unsigned int v10;  // s4
    unsigned int v11;  // s5
    unsigned int v12;  // s2
    unsigned int v13;  // s1
    unsigned int v14;  // s14
    unsigned int v15;  // s3
    unsigned int v16;  // s3
    unsigned int v17;  // s0
    unsigned long long v2;  // x0
    struct_4 *addr;  // x19
    unsigned int v3;  // s3
    unsigned int v4;  // s3
    unsigned int v5;  // s7
    unsigned int v6;  // s17
    unsigned int v7;  // s3
    unsigned int v8;  // s0

    if (2 <= p->field_10)
        return 0;
    ptr = p->field_20;
    p->field_10 = 4294967295;
    if (ptr)
    {
        v1 = ptr->field_b8;
        if (ptr->field_4a9)
        {
            if (v1)
                goto LABEL_10bb440;
        }
        else
        {
            if (v1)
            {
                if (!v1->field_106)
                {
LABEL_10bb440:
                    if (v1->field_106)
                    {
                        if (ptr->field_4a0)
                        {
                            Transform__get_position(ptr->field_4a0, 0);
                            if (ptr->field_b0)
                            {
                                WeaponEffects__BulletTracers(ptr->field_b0, 1, 0);
                                return 0;
                            }
                        }
                    }
                    else
                    {
                        if (ptr->field_98 && ptr->field_78 && (Transform__get_position(ptr->field_78, 0), ptr->field_78))
                        {
                            if (ptr->field_98->field_2d0)
                            {
                                Transform__get_up();
                                if (ptr->field_78)
                                {
                                    v3 = ptr->field_510;
                                    Transform__get_forward(ptr->field_78, 0);
                                    v4 = ptr->field_4b0;
                                    v5 = ptr->field_514;
                                    v6 = ptr->field_430;
                                    v7 = v17 + v17 * v3 + v17 * v3 * v4;
                                    v8 = ptr->field_434;
                                    v10 = v9 + v9 * v3 + v9 * v3 * v4;
                                    v11 = ptr->field_42c * v5;
                                    v13 = v12 + v12 * v3 + v12 * v3 * v4;
                                    goto LABEL_10bb608;
                                }
                            }
                            else
                            {
                                Transform__get_right();
                                if (ptr->field_78 && (v14 = ptr->field_50c, Transform__get_up(ptr->field_78, 0), ptr->field_78))
                                {
                                    v15 = ptr->field_510;
                                    Transform__get_forward(ptr->field_78, 0);
                                    v16 = ptr->field_4b0;
                                    v5 = ptr->field_514;
                                    v6 = ptr->field_430;
                                    v7 = v17 + v17 * v14 + v17 * v15 + v17 * v15 * v16;
                                    v8 = ptr->field_434;
                                    v10 = v9 + v9 * v14 + v9 * v15 + v9 * v15 * v16;
                                    v11 = ptr->field_42c * v5;
                                    v13 = v12 + v12 * v14 + v12 * v15 + v12 * v15 * v16;
LABEL_10bb608:
                                    v2 = ptr->field_b0;
                                    ptr->field_524 = v7 + v11;
                                    ptr->field_528 = v10 + v6 * v5;
                                    ptr->field_52c = v13 + v8 * v5;
                                    if (v2)
                                    {
                                        WeaponEffects__BulletTracers(v2, 1, 0);
                                        return 0;
                                    }
                                }
                            }
                        }
                    }
                }
                else if (ptr->field_90)
                {
                    if (!ptr->field_90->field_129)
                    {
                        p->field_18 = 0;
                        addr = &p->field_18;
                        sub_f7d8d0(addr, 0);
                        *((unsigned int *)&addr->padding_0[8]) = 1;
                        return 1;
                    }
                    goto LABEL_10bb440;
                }
            }
        }
    }
    sub_f7db74();
}
```


## `WeaponBehavior.<EmitTracers>d__356.get_Current` — RVA `0xcbb67c`

- Decompiled symbol: `WeaponBehavior_EmitTracers_d__356_get_Current`
- Metadata signature: `private object System.Collections.Generic.IEnumerator<System.Object>.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long WeaponBehavior_EmitTracers_d__356_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```


## `WeaponBehavior.<EmitTracers>d__356.Reset` — RVA `0xcbb684`

- Decompiled symbol: `WeaponBehavior_EmitTracers_d__356_Reset`
- Metadata signature: `private void System.Collections.IEnumerator.Reset() { }`
- Native interval: `56` bytes
- Result: `pseudocode`

```c
extern long long g_1ef0bd8;
extern long long g_1f05368;

void WeaponBehavior_EmitTracers_d__356_Reset(void)
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
    sub_f7da4c(v4, sub_f7d940(&g_1f05368));
}
```


## `WeaponBehavior.<EmitTracers>d__356.get_Current` — RVA `0xcbb6bc`

- Decompiled symbol: `WeaponBehavior_EmitTracers_d__356_get_Current`
- Metadata signature: `private object System.Collections.IEnumerator.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long WeaponBehavior_EmitTracers_d__356_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```


## `WeaponBehavior.<FireOneShot>d__354.Dispose` — RVA `0xcbb6c4`

- Decompiled symbol: `WeaponBehavior_FireOneShot_d__354_Dispose`
- Metadata signature: `private void System.IDisposable.Dispose() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long WeaponBehavior_FireOneShot_d__354_Dispose(void)
{
    unsigned long v0;  // x0

    return v0;
}
```


## `WeaponBehavior.<FireOneShot>d__354.MoveNext` — RVA `0xcbb6c8`

- Decompiled symbol: `WeaponBehavior_FireOneShot_d__354_MoveNext`
- Metadata signature: `private bool MoveNext() { }`
- Native interval: `6608` bytes
- Result: `pseudocode`

```c
typedef struct struct_9 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[4];
    long long field_18;
    struct struct_8 *field_20;
} struct_9;

typedef struct struct_8 {
    char padding_0[32];
    long long field_20;
    long long field_28;
    long long field_30;
    char padding_38[8];
    unsigned long long field_40;
    char padding_48[48];
    long long field_78;
    struct struct_4 *field_80;
    char padding_88[16];
    struct struct_5 *field_98;
    char padding_a0[8];
    struct struct_6 *field_a8;
    char padding_b0[8];
    struct struct_7 *field_b8;
    char padding_c0[80];
    long long field_110;
    long long field_118;
    char padding_120[8];
    unsigned int field_128;
    unsigned int field_12c;
    char padding_130[24];
    unsigned int field_148;
    unsigned int field_14c;
    char padding_150[4];
    int field_154;
    unsigned int field_158;
    unsigned int field_15c;
    char padding_160[8];
    long long field_168;
    long long field_170;
    unsigned int field_178;
    char field_17c;
    char padding_17d[3];
    unsigned int field_180;
    unsigned int field_184;
    unsigned int field_188;
    unsigned int field_18c;
    char padding_190[32];
    char field_1b0;
    char padding_1b1[23];
    unsigned long long field_1c8;
    char field_1cc;
    char padding_1cd[11];
    unsigned int field_1d8;
    char padding_1dc[4];
    char field_1e0;
    char padding_1e1[11];
    unsigned int field_1ec;
    char padding_1f0[6];
    char field_1f6;
    char padding_1f7[1];
    char field_1f8;
    char padding_1f9[11];
    unsigned int field_204;
    char padding_208[16];
    unsigned int field_218;
    char padding_21c[13];
    char field_229;
    char padding_22a[322];
    char field_36c;
    char padding_36d[11];
    unsigned int field_378;
    unsigned int field_37c;
    char padding_380[132];
    unsigned int field_404;
    unsigned int field_408;
    unsigned int field_40c;
    char padding_410[28];
    unsigned long long field_42c;
    unsigned int field_434;
    unsigned int field_438;
    unsigned int field_43c;
    unsigned int field_440;
    char padding_444[196];
    char field_508;
    char padding_509[39];
    long long field_530;
} struct_8;

typedef struct struct_4 {
    char padding_0[568];
    long long field_238;
    char padding_240[113];
    char field_2b1;
    char padding_2b2[298];
    unsigned int field_3dc;
} struct_4;

typedef struct struct_1 {
    uint128_t field_0;
    char field_10[28];
    char field_1c;
} struct_1;

typedef struct struct_6 {
    char padding_0[168];
    char field_a8;
} struct_6;

typedef struct struct_7 {
    char padding_0[262];
    char field_106;
    char padding_107[161];
    unsigned int field_1a8;
} struct_7;

typedef struct struct_12 {
    char padding_0[32];
    unsigned int field_20;
} struct_12;

typedef struct struct_5 {
    char padding_0[1120];
    char field_460;
} struct_5;

typedef struct struct_11 {
    unsigned int field_0;
    unsigned int field_4;
    unsigned int field_8;
} struct_11;

typedef struct struct_3 {
    char padding_0[224];
    unsigned int field_e0;
} struct_3;

typedef struct struct_2 {
    char padding_0[224];
    unsigned int field_e0;
} struct_2;

typedef struct struct_10 {
    char padding_0[184];
    struct struct_11 *field_b8;
} struct_10;

extern struct_2 *g_1ef0c58;
extern struct_3 *g_1ef0e48;
extern struct_10 *g_1ef22e8;
extern long long g_1ef2440;
extern long long g_1efcf10;
extern long long g_1efeb98;
extern long long g_1efebd0;
extern long long g_1efeca8;
extern long long g_1f08de8;
extern long long g_1f08df0;
extern long long g_1f0a430;
extern long long g_1f0c0b0;
extern long long g_1f0c0c0;
extern long long g_1f0c0c8;
extern long long g_1f0cac0;
extern long long g_1f0d140;
extern long long g_1f0de28;
extern long long g_1f0de30;
extern char g_1fab2c8;
extern char g_1fab2c9;
extern char g_1fab32c;
extern char g_1fab3e0;
extern char g_1fab3e1;
extern char g_1fab4f0;

unsigned int WeaponBehavior_FireOneShot_d__354_MoveNext(struct_9 *p)
{
    unsigned int flag5;  // w8
    struct_8 *ptr;  // x19
    unsigned int v77;  // s1
    unsigned int v78;  // s2
    unsigned long long v79;  // x0
    unsigned int v80;  // w0
    unsigned int v81;  // s2
    unsigned int v82;  // s14
    unsigned int v83;  // s0
    unsigned int v84;  // s0
    unsigned int v85;  // s1
    long long v69;  // x19
    unsigned int v86;  // s2
    unsigned int v87;  // s8
    unsigned int v88;  // s9
    unsigned int v89;  // s10
    unsigned int v90;  // s11
    unsigned int v91;  // s14
    unsigned int v92;  // s3
    unsigned long v93;  // 4252
    unsigned int v94;  // s8
    unsigned int v95;  // s12
    struct_9 *ptr6;  // x20
    unsigned int v96;  // s13
    unsigned int ptr4[3];  // x8
    unsigned int v98;  // w24
    unsigned long long v99;  // x25
    long long v100;  // x0
    unsigned long v101;  // x0
    long long v102;  // x0
    unsigned int v103[56];  // x0
    unsigned int ptr3[56];  // x24
    unsigned int v105;  // s1
    unsigned int v71;  // s0
    unsigned int v106;  // s0
    unsigned long v107;  // 4129
    unsigned int v108;  // s0
    long long v109;  // x0
    long long v110;  // x24
    long long v111;  // x24
    unsigned int v112;  // s0
    struct_7 *v113;  // x8
    long long v114;  // x24
    unsigned int v115;  // s0
    unsigned long long v72;  // 4104
    unsigned long v116;  // 4129
    unsigned int v117;  // s0
    unsigned long v118;  // 4129
    long long v119;  // x24
    long long v120;  // x24
    long long v121;  // x0
    struct_12 *ptr7;  // x0
    unsigned int v123;  // s0
    unsigned int v124;  // w8
    unsigned long long v125;  // 4105
    unsigned long v73;  // x29
    unsigned long v126;  // x9
    unsigned int v127;  // w0
    unsigned int v128;  // s0
    unsigned long v129;  // 4125
    long long v130;  // x0
    unsigned int v131;  // w0
    struct_1 *v132;  // x1
    unsigned int v133;  // w0
    long long v134;  // x0
    unsigned int v135;  // w0
    unsigned int v74;  // s0
    struct_8 *ptr8;  // x0
    struct_6 *v137;  // x8
    unsigned int v138;  // w0
    unsigned int v139;  // w0
    long long v140;  // x0
    unsigned int v141;  // w0
    struct_7 *v143;  // x8
    unsigned int v144;  // w0
    struct_1 *v145;  // x1
    unsigned long ptr5;  // x20
    unsigned int v146;  // w0
    unsigned int v147;  // w0
    unsigned int v148;  // w0
    int v150;  // q0
    unsigned long v151;  // 4157
    long long v152;  // x19
    struct_9 *ptr9;  // x20
    long long v155;  // x19
    unsigned long addr;  // x21
    long long v156;  // x19
    unsigned long v0;  // [bp-0x390]
    unsigned long ptr10;  // [bp-0x388]
    unsigned long v2;  // [bp-0x380]
    unsigned int v3;  // [bp-0x374]
    char v4[4];  // [bp-0x370]
    unsigned int v5;  // [bp-0x36c]
    unsigned int v6;  // [bp-0x368]
    unsigned int v7;  // [bp-0x364]
    unsigned int v8;  // [bp-0x360]
    unsigned int v9;  // [bp-0x35c]
    unsigned int v10;  // [bp-0x358]
    unsigned int v11;  // [bp-0x354]
    unsigned int v12;  // [bp-0x350]
    unsigned int v13;  // [bp-0x34c]
    unsigned int v14;  // [bp-0x348]
    unsigned int v15;  // [bp-0x344]
    unsigned int v16;  // [bp-0x340]
    unsigned int v17;  // [bp-0x33c]
    unsigned int v18;  // [bp-0x338]
    unsigned int v19;  // [bp-0x334]
    unsigned int v20;  // [bp-0x330]
    unsigned int v21;  // [bp-0x32c]
    unsigned int v22;  // [bp-0x328]
    unsigned int v23;  // [bp-0x324]
    unsigned int v24;  // [bp-0x320]
    unsigned int v25;  // [bp-0x31c]
    unsigned long v26;  // [bp-0x318], Other Possible Types: unsigned int
    char v27;  // [bp-0x310]
    int v28;  // [bp-0x300]
    int v29;  // [bp-0x2f4]
    char v30;  // [bp-0x2e0]
    int v31;  // [bp-0x2d0]
    int v32;  // [bp-0x2c4]
    char v33;  // [bp-0x2b0]
    int v34;  // [bp-0x2a0]
    int v35;  // [bp-0x294]
    char v36;  // [bp-0x280]
    int v37;  // [bp-0x270]
    int v38;  // [bp-0x264]
    struct_1 v39;  // [bp-0x250]
    int v40;  // [bp-0x240]
    char v41;  // [bp-0x234]
    struct_1 v42;  // [bp-0x220]
    int v43;  // [bp-0x210]
    char v44;  // [bp-0x204]
    struct_1 v45;  // [bp-0x1f0]
    int v46;  // [bp-0x1e0]
    char v47;  // [bp-0x1c0]
    int v48;  // [bp-0x1b0]
    int v49;  // [bp-0x1a4]
    struct_1 v50;  // [bp-0x190]
    int v51;  // [bp-0x180]
    int v52;  // [bp-0x174]
    char v53;  // [bp-0x160]
    int v54;  // [bp-0x150]
    int v55;  // [bp-0x144]
    struct_1 v56;  // [bp-0x130]
    int v57;  // [bp-0x120]
    int v58;  // [bp-0x114]
    int flag3;  // [bp-0x100]
    uint128_t flag4;  // [bp-0xf0]
    uint128_t flag2;  // [bp-0xe4]
    int choice;  // [bp-0xd0]
    int v63;  // [bp-0xc0]
    uint128_t flag;  // [bp-0xb4]
    char *v65;  // [bp-0x60]
    char v66;  // [bp+0x0]

    v65 = &v66;
    if (!(g_1fab4f0 & 1))
    {
        sub_f7d92c("s.");
        sub_f7d92c(&g_1efcf10);
        sub_f7d92c(&g_1efeb98);
        sub_f7d92c(&g_1efebd0);
        sub_f7d92c(&g_1efeca8);
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c(&g_1ef0e48);
        sub_f7d92c(&g_1ef2440);
        sub_f7d92c(&g_1f08de8);
        sub_f7d92c(&g_1f0cac0);
        sub_f7d92c("S&");
        sub_f7d92c(&g_1f0de30);
        sub_f7d92c(&g_1f0de28);
        sub_f7d92c(&g_1f0c0c0);
        sub_f7d92c(&g_1f0a430);
        sub_f7d92c(&g_1f0c0b0);
        sub_f7d92c(&g_1f0c0c8);
        sub_f7d92c(&g_1f08df0);
        sub_f7d92c(&g_1f0d140);
        g_1fab4f0 = 1;
    }
    flag = 0;
    choice = 0;
    *((uint128_t *)&v63) = 0;
    flag2 = 0;
    flag3 = 0;
    flag4 = 0;
    flag5 = p->field_10;
    ptr = p->field_20;
    if (3 > flag5 - 2)
    {
        p->field_10 = 4294967295;
        if (ptr)
            goto LABEL_10bb828;
    }
    else if (flag5 != 1)
    {
        if (flag5)
        {
LABEL_10bcc1c:
            return 0;
        }
        p->field_10 = 4294967295;
        if (ptr)
        {
            if (!ptr->padding_21c[9])
                goto LABEL_10bcc30;
            if (ptr->field_80)
            {
                if (ptr->field_80->field_2b1)
                {
                    v69 = sub_f7db70(g_1ef2440);
                    WaitForSeconds__ctor(v69, 0);
                    p->field_18 = v69;
                    ptr6 = &p->field_18;
                    sub_f7d8d0(ptr6, v69);
                    *((unsigned int *)&ptr6->padding_0[8]) = 1;
                    return 1;
                }
                goto LABEL_10bcc30;
            }
        }
    }
    else
    {
        p->field_10 = 4294967295;
        if (ptr)
        {
LABEL_10bcc30:
            v71 = *((int *)&ptr->padding_1f9[7]);
            ptr->field_158 = 0;
            v72 = (((CmpF(v71, 0.0) >> 5 & 3 | CmpF(v71, 0.0) & 1) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - ((CmpF(v71, 0.0) >> 5 & 3 | CmpF(v71, 0.0) & 1) & (CmpF(v71, 0.0) >> 5 & 3 | CmpF(v71, 0.0) & 1) >> 1 & 1);
            if (!((char)(v72 * 0x10000000 >> 30)) || ptr->padding_21c[9])
            {
                if (ptr->padding_1f0[4])
                {
LABEL_10bcc60:
                    if (ptr->padding_21c[9])
                    {
LABEL_10bcc68:
                        if (ptr->field_118 && (Animator__set_speed(ptr->field_118, 0), ptr->field_118 && (Animator__SetTrigger(ptr->field_118, g_1f08de8, 0), ptr->field_110)))
                        {
                            if (ptr->padding_21c[9])
                            {
                                Animator__SetTrigger();
                                if (!g_1ef0c58->field_e0)
                                    sub_f7da5c(g_1ef0c58);
                                if (!(Object__op_Implicit(ptr->field_20, 0) & 1))
                                    goto LABEL_10bce54;
                                if (ptr->field_20)
                                {
                                    Animator__SetTrigger(ptr->field_20, g_1f0cac0, 0);
                                    goto LABEL_10bce54;
                                }
                            }
                            else
                            {
                                Animator__SetTrigger();
                                if (!g_1ef0c58->field_e0)
                                    sub_f7da5c(g_1ef0c58);
                                if (((char)Object__op_Implicit(ptr->field_20, 0) & 1))
                                {
                                    if (ptr->field_20)
                                    {
                                        Animator__SetTrigger(ptr->field_20, g_1f0de28, 0);
                                        goto LABEL_10bce4c;
                                    }
                                }
                                else
                                {
LABEL_10bce4c:
                                    ptr->padding_1f0[4] = 1;
LABEL_10bce54:
                                    if (ptr->padding_21c[9])
                                    {
                                        v152 = sub_f7db70(g_1ef2440);
                                        WaitForSeconds__ctor(v152, 0);
                                        p->field_18 = v152;
                                        ptr9 = &p->field_18;
                                        sub_f7d8d0(ptr9, v152);
                                        *((unsigned int *)&ptr9->padding_0[8]) = 4;
                                        return 1;
                                    }
                                    if (ptr->field_b8)
                                    {
                                        if (ptr->field_b8->field_106)
                                        {
                                            v155 = sub_f7db70(g_1ef2440);
                                            WaitForSeconds__ctor(v155, 0);
                                            p->field_18 = v155;
                                            ptr9 = &p->field_18;
                                            sub_f7d8d0(ptr9, v155);
                                            *((unsigned int *)&ptr9->padding_0[8]) = 3;
                                            return 1;
                                        }
                                        v156 = sub_f7db70(g_1ef2440);
                                        WaitForSeconds__ctor(v156, 0);
                                        p->field_18 = v156;
                                        ptr9 = &p->field_18;
                                        sub_f7d8d0(ptr9, v156);
                                        *((unsigned int *)&ptr9->padding_0[8]) = 2;
                                        return 1;
                                    }
                                }
                            }
                        }
                    }
                    else
                    {
                        if (ptr->field_118 && (Animator__set_speed(ptr->field_118, 0), ptr->field_118 && (Animator__SetTrigger(ptr->field_118, g_1f08df0, 0), ptr->field_110)))
                        {
                            Animator__SetTrigger(ptr->field_110, g_1f0c0c8, 0);
                            if (!g_1ef0c58->field_e0)
                                sub_f7da5c(g_1ef0c58);
                            if (((char)Object__op_Implicit(ptr->field_20, 0) & 1))
                            {
                                if (ptr->field_20)
                                {
                                    Animator__SetTrigger(ptr->field_20, g_1f0de30, 0);
                                    goto LABEL_10bcda4;
                                }
                            }
                            else
                            {
LABEL_10bcda4:
                                ptr->padding_1f0[4] = 0;
                                goto LABEL_10bce54;
                            }
                        }
                    }
                }
                else if (ptr->field_98)
                {
                    if (!ptr->field_98->field_460)
                        goto LABEL_10bcc68;
                    goto LABEL_10bcc60;
                }
            }
            else
            {
                if (ptr->field_1b0)
                {
                    WeaponBehavior__WeaponKick(ptr);
                    if (ptr->field_110)
                    {
                        Animator__SetTrigger(ptr->field_110, g_1f0a430, 0);
                        goto LABEL_10bcdd8;
                    }
                }
                else
                {
LABEL_10bcdd8:
                    if (ptr->padding_1f0[2])
                        ptr->field_12c = ptr->field_12c - 1;
                    else
                        ptr->field_128 = ptr->field_128 - 1;
                    if (ptr->padding_1dc[0])
                        *((unsigned int *)&ptr->padding_1e1[7]) = *((int *)&ptr->padding_1e1[7]) + 1;
                    if (!g_1ef0c58->field_e0)
                        sub_f7da5c(g_1ef0c58);
                    if (!((char)Object__op_Implicit(ptr->field_20, 0) & 1))
                    {
LABEL_10bcfbc:
                        if (ptr->padding_22a[318])
                        {
                            if (!g_1ef0c58->field_e0)
                                sub_f7da5c(g_1ef0c58);
                            if (!(Object__op_Implicit(ptr->field_30, 0) & 1))
                                goto LABEL_10bd018;
                            if (ptr->field_30)
                            {
                                if (!(Animator__get_isInitialized(ptr->field_30, 0) & 1))
                                    goto LABEL_10bd018;
                                if (ptr->field_30)
                                {
                                    Animator__SetTrigger(ptr->field_30, g_1f0d140, 0);
                                    goto LABEL_10bd018;
                                }
                            }
                        }
                        else
                        {
LABEL_10bd018:
                            if (!g_1ef0c58->field_e0)
                                sub_f7da5c(g_1ef0c58);
                            if (!((char)Object__op_Implicit(ptr->field_28, 0) & 1))
                            {
LABEL_10bb828:
                                if (ptr->field_154 < 1)
                                    return 0;
                                v0 = &ptr->field_148;
                                ptr10 = &ptr->padding_380[128];
                                v2 = &ptr->padding_208[12];
                                v5 = 1061997773;
                                v73 = &ptr->field_78;
                                strncpy(&v4, "fff?", 4);
                                v74 = 925353388;
                                ptr5 = &ptr->field_168;
                                addr = &ptr->field_170;
                                v77 = 0;
                                v3 = 925353388;
                                do
                                {
                                    v6 = v77;
                                    WeaponBehavior__SprayDirection(ptr);
                                    v79 = ptr->field_40;
                                    *((unsigned int *)&ptr->padding_380[128]) = v74;
                                    ptr->field_404 = v77;
                                    ptr->field_408 = v78;
                                    if (!v79)
                                        sub_f7db74();
                                    if (!GameObject__get_transform(v79, 0))
                                        sub_f7db74();
                                    Transform__get_position();
                                    if (!ptr->field_40)
                                        sub_f7db74();
                                    if (!GameObject__get_transform(ptr->field_40, 0))
                                        sub_f7db74();
                                    Transform__get_up();
                                    v26 = v78;
                                    if (!*((long long *)v73))
                                        goto LABEL_10bd094;
                                    Transform__get_position(*((long long *)v73), 0);
                                    if (!g_1fab3e0)
                                    {
                                        sub_f7d92c("_F");
                                        g_1fab3e0 = 1;
                                    }
                                    if (!g_1ef07e8->field_e0)
                                        sub_f7da5c(g_1ef07e8);
                                    if (!ptr->field_40)
                                        sub_f7db74();
                                    if (!GameObject__get_transform(ptr->field_40, 0))
                                        sub_f7db74();
                                    v20 = v77;
                                    v21 = v74;
                                    v22 = v78;
                                    v23 = v77;
                                    v24 = v74;
                                    v25 = v78;
                                    Transform__get_position();
                                    if (!*((long long *)v73))
                                        sub_f7db74();
                                    Transform__get_position(*((long long *)v73), 0);
                                    if (!g_1fab3e0)
                                    {
                                        sub_f7d92c("_F");
                                        g_1fab3e0 = 1;
                                    }
                                    if (!g_1ef07e8->field_e0)
                                        sub_f7da5c(g_1ef07e8);
                                    if (!*((long long *)v73))
                                        sub_f7db74();
                                    v18 = v77;
                                    v19 = v77;
                                    v14 = v78;
                                    v15 = v77;
                                    v16 = v74;
                                    v17 = v78;
                                    Transform__get_position(*((long long *)v73), 0);
                                    if (!*((long long *)v73))
                                        sub_f7db74();
                                    v13 = v74;
                                    Transform__get_forward(*((long long *)v73), 0);
                                    if (!*((long long *)v73))
                                        sub_f7db74();
                                    Transform__get_forward(*((long long *)v73), 0);
                                    v8 = v77;
                                    v9 = v74;
                                    v7 = ptr->field_404;
                                    v10 = v78;
                                    v11 = ptr->field_408;
                                    v12 = ptr->field_148;
                                    v80 = LayerMask__op_Implicit(*((int *)&ptr->padding_36d[7]), 0);
                                    if (!g_1ef0e48->field_e0)
                                        sub_f7da5c(g_1ef0e48);
                                    v81 = v5;
                                    v82 = v19 + v20 * v81;
                                    v25 += v26 * v81;
                                    v26 = v74 + v21 * v81;
                                    v83 = [D] unsupported_Iop_SqrtF32();
                                    v84 = v74 + v83 * v74;
                                    v85 = v77 + v83 * v77;
                                    v86 = v78 + v83 * v78;
                                    if (((char)Physics__Raycast(&flag3, v80, 0) & 1))
                                    {
                                        RaycastHit__get_point(&flag3, 0);
                                        v87 = v84;
                                        v88 = v85;
                                        v89 = v86;
                                        v90 = v82;
                                    }
                                    else
                                    {
                                        if (*((long long *)v73))
                                        {
                                            Transform__get_position(*((long long *)v73), 0);
                                            if (!*((long long *)v73))
                                                sub_f7db74();
                                            v90 = v82;
                                            Transform__get_forward(*((long long *)v73), 0);
                                            v87 = v84 + (v84 + *((int *)&ptr->padding_380[128])) * 0x41a00000;
                                            v88 = v85 + (v85 + ptr->field_404) * 0x41a00000;
                                            v89 = v86 + (v86 + ptr->field_408) * 0x41a00000;
                                        }
                                        else
                                        {
                                            sub_f7db74();
                                        }
                                    }
                                    v91 = v26;
                                    if (!g_1fab2c8)
                                    {
                                        sub_f7d92c("_F");
                                        g_1fab2c8 = 1;
                                    }
                                    if (!g_1ef07e8->field_e0)
                                        sub_f7da5c(g_1ef07e8);
                                    v92 = [D] unsupported_Iop_SqrtF32();
                                    v93 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v92, v3)) >> 5 & 3 | (unsigned long long)(CmpF(v92, v3) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v92, v3)) >> 5 & 3 | (unsigned long long)(CmpF(v92, v3) & 1)) & ((unsigned long long)(char)(CmpF(v92, v3)) >> 5 & 3 | (unsigned long long)(CmpF(v92, v3) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                                    if (!((char)v93))
                                    {
                                        v94 = (v87 - v91) / v92;
                                        v95 = (v88 - v90) / v92;
                                        v96 = (v89 - v25) / v92;
                                    }
                                    else
                                    {
                                        if (!g_1fab2c9)
                                        {
                                            sub_f7d92c(&g_1ef22e8);
                                            g_1fab2c9 = 1;
                                        }
                                        ptr4 = g_1ef22e8->field_b8;
                                        v94 = ptr4[0];
                                        v95 = ptr4[1];
                                        v96 = ptr4[2];
                                    }
                                    v98 = ptr->field_15c;
                                    ptr->field_434 = v94;
                                    ptr->field_438 = v95;
                                    ptr->field_43c = v96;
                                    if (v98 && !ptr->padding_21c[9])
                                    {
                                        if (!ptr->field_a8)
                                            sub_f7db74();
                                        if (!ptr->field_b8)
                                            sub_f7db74();
                                        if (!*((long long *)v73))
                                            sub_f7db74();
                                        v99 = g_1eeea08->field_b8->field_0;
                                        Transform__get_position(*((long long *)v73), 0);
                                        if (!*((long long *)v73))
                                            sub_f7db74();
                                        Transform__get_forward(*((long long *)v73), 0);
                                        if (ptr->field_b8->field_106)
                                        {
                                            if (*((long long *)v73))
                                            {
                                                Transform__get_rotation();
                                                if (!v99)
                                                    sub_f7db74();
                                            }
                                            else
                                            {
                                                sub_f7db74();
                                            }
                                        }
                                        else
                                        {
                                            if (*((long long *)v73))
                                            {
                                                Transform__get_rotation();
                                                if (!v99)
                                                    sub_f7db74();
                                            }
                                            else
                                            {
                                                sub_f7db74();
                                            }
                                        }
                                        v100 = AzuObjectPool__SpawnPooledObj(v99, v98, 0);
                                        *((long long *)ptr5) = v100;
                                        sub_f7d8d0(ptr5, v100);
                                        if (!*((long long *)ptr5) || !((v101 = (unsigned long)sub_1249224(*((long long *)ptr5), g_1efeb98), ptr->field_80)))
                                            goto LABEL_10bd094;
                                        if (!g_1ef0e48->field_e0)
                                            sub_f7da5c(g_1ef0e48);
                                        Physics__IgnoreCollision(v101, ptr->field_80->field_238, 1, 0);
                                        if (!*((long long *)ptr5))
                                            sub_f7db74();
                                        if (!GameObject__get_transform(*((long long *)ptr5), 0))
                                            sub_f7db74();
                                        v102 = sub_1231bc8();
                                        if (!g_1ef0c58->field_e0)
                                            sub_f7da5c(g_1ef0c58);
                                        if (!((char)Object__op_Implicit(v102, 0) & 1))
                                        {
LABEL_10bc670:
                                            if (!*((long long *)ptr5))
                                                sub_f7db74();
                                            v109 = sub_1249224(*((long long *)ptr5), g_1efeca8);
                                            *((long long *)addr) = v109;
                                            sub_f7d8d0(addr, v109);
                                            v110 = *((long long *)addr);
                                            if (!g_1fab2c9)
                                            {
                                                sub_f7d92c(&g_1ef22e8);
                                                g_1fab2c9 = 1;
                                            }
                                            if (!v110)
                                                sub_f7db74();
                                            Rigidbody__set_velocity(v110, 0);
                                            v111 = *((long long *)addr);
                                            if (!g_1fab2c9)
                                            {
                                                sub_f7d92c(&g_1ef22e8);
                                                g_1fab2c9 = 1;
                                            }
                                            if (!v111)
                                                sub_f7db74();
                                            Rigidbody__set_angularVelocity(v111, 0);
                                            v112 = ptr->field_178;
                                            if (ptr->field_17c)
                                                v112 = ptr->field_178 * *((int *)((char *)&ptr->field_1c8 + 4)) + ptr->field_180;
                                            v113 = ptr->field_b8;
                                            ptr->field_184 = v112;
                                            if (!v113)
                                                sub_f7db74();
                                            v114 = *((long long *)addr);
                                            if (v113->field_106)
                                            {
                                                if (*((long long *)v73))
                                                {
                                                    Transform__get_forward(*((long long *)v73), 0);
                                                    if (!v114)
                                                        sub_f7db74();
                                                }
                                                else
                                                {
                                                    sub_f7db74();
                                                }
                                            }
                                            else
                                            {
                                                if (!v114)
                                                    sub_f7db74();
                                            }
                                            Rigidbody__AddForce(v114, 1, 0);
                                            v115 = ptr->field_188;
                                            v116 = arm64g_calculate_condition(192, (((((unsigned long long)(char)(CmpF(v115, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v115, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v115, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v115, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v115, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v115, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                                            if ((char)v116 || (v117 = ptr->field_18c, v118 = (unsigned long)arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v117, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v117, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v117, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v117, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v117, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v117, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0), !((char)v118)))
                                            {
                                                if (*((long long *)addr))
                                                {
                                                    Rigidbody__set_maxAngularVelocity(*((long long *)addr), 0);
                                                    v119 = *((long long *)addr);
                                                    if (!g_1fab32c)
                                                    {
                                                        sub_f7d92c(&g_1ef22e8);
                                                        g_1fab32c = 1;
                                                    }
                                                    Random__Range(0);
                                                    if (!v119)
                                                        sub_f7db74();
                                                    Rigidbody__AddRelativeTorque(v119, 0);
                                                    v120 = *((long long *)addr);
                                                    if (!g_1fab3e1)
                                                    {
                                                        sub_f7d92c(&g_1ef22e8);
                                                        g_1fab3e1 = 1;
                                                    }
                                                    Random__Range(0);
                                                    if (!v120)
                                                        sub_f7db74();
                                                    Rigidbody__AddRelativeTorque(v120, 0);
                                                }
                                                else
                                                {
                                                    sub_f7db74();
                                                }
                                            }
                                            if (!*((long long *)ptr5))
                                                sub_f7db74();
                                            v121 = sub_1249224(*((long long *)ptr5), g_1efebd0);
                                            if (!g_1ef0c58->field_e0)
                                                sub_f7da5c(g_1ef0c58);
                                            if (((char)Object__op_Implicit(v121, 0) & 1))
                                            {
                                                if (*((long long *)ptr5))
                                                {
                                                    ptr7 = sub_1249224(*((long long *)ptr5), g_1efebd0);
                                                    if (!ptr7)
                                                        sub_f7db74();
                                                    ptr7->field_20 = *((int *)&ptr->padding_1cd[7]) * (0x3f800000 - *((int *)((char *)&ptr->field_1c8 + 4))) + 1045220557;
                                                }
                                                else
                                                {
                                                    sub_f7db74();
                                                }
                                            }
                                            ptr->field_1c8 = 0;
                                            goto LABEL_10bcb8c;
                                        }
                                        if (!*((long long *)ptr5))
                                            sub_f7db74();
                                        if (!GameObject__get_transform(*((long long *)ptr5), 0))
                                            sub_f7db74();
                                        v103 = sub_1231bc8();
                                        if (!v103)
                                            sub_f7db74();
                                        ptr3 = v103;
                                        ArrowObject__InitializeProjectile();
                                        v105 = *((int *)((char *)&ptr->field_1c8 + 4));
                                        ptr3[16] = ptr3[14] * v105;
                                        v106 = v105 * ptr->field_178 / ptr->field_178;
                                        ptr3[54] = v106;
                                        ptr3[26] = ptr->field_15c;
                                        if (!Camera__get_main(0))
                                            sub_f7db74();
                                        Camera__get_nearClipPlane();
                                        v107 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(v106, 1036831949)) >> 5 & 3 | (unsigned long long)(CmpF(v106, 1036831949) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v106, 1036831949)) >> 5 & 3 | (unsigned long long)(CmpF(v106, 1036831949) & 1)) & ((unsigned long long)(char)(CmpF(v106, 1036831949)) >> 5 & 3 | (unsigned long long)(CmpF(v106, 1036831949) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                                        if (!((char)v107))
                                        {
                                            if (!ptr->field_b8)
                                                sub_f7db74();
                                            if (!ptr->field_b8->field_106)
                                                goto LABEL_10bc408;
                                        }
                                        if (!ptr->field_a8)
                                            sub_f7db74();
                                        if (!ptr->field_a8->field_a8)
                                        {
                                            v108 = 1045220557;
LABEL_10bc66c:
                                            ptr3[55] = v108;
                                            goto LABEL_10bc670;
                                        }
LABEL_10bc408:
                                        v108 = 0;
                                        goto LABEL_10bc66c;
                                    }
                                    v123 = *((int *)&ptr->padding_1f9[7]);
                                    v124 = ptr->padding_21c[9];
                                    v125 = (((CmpF(v123, 0.0) >> 5 & 3 | CmpF(v123, 0.0) & 1) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - ((CmpF(v123, 0.0) >> 5 & 3 | CmpF(v123, 0.0) & 1) & (CmpF(v123, 0.0) >> 5 & 3 | CmpF(v123, 0.0) & 1) >> 1 & 1);
                                    if (!((char)(v125 * 0x10000000 >> 30)))
                                    {
                                        v126 = v2;
                                        if (!v124)
                                            v126 = v0;
LABEL_10bbe34:
                                        v143 = ptr->field_b8;
                                        ptr->field_14c = *((int *)v126);
                                        if (!v143)
                                            sub_f7db74();
                                        if (!*((long long *)v73))
                                            sub_f7db74();
                                        Transform__get_position(*((long long *)v73), 0);
                                        if (!*((long long *)&ptr->padding_509[35]))
                                            sub_f7db74();
                                        CapsuleCollider__get_radius(*((long long *)&ptr->padding_509[35]), 0);
                                        if (v143->field_106)
                                        {
                                            if (!*((long long *)v73))
                                                sub_f7db74();
                                            Transform__get_forward(*((long long *)v73), 0);
                                            if (!ptr->field_b8)
                                                sub_f7db74();
                                            if (!ptr->field_80)
                                                sub_f7db74();
                                            v25 = ptr->field_80->field_3dc;
                                            v26 = ptr->field_b8->field_1a8;
                                            v144 = LayerMask__op_Implicit(*((int *)&ptr->padding_36d[7]), 0);
                                            if (!g_1ef0e48->field_e0)
                                                sub_f7da5c(g_1ef0e48);
                                            if (((char)Physics__SphereCast(&choice, v144, 0) & 1))
                                            {
                                                memcpy(&v45, &choice, 16);
                                                *((uint128_t *)&v46) = *((uint128_t *)&v63);
                                                *((uint128_t *)&(&v46)[12]) = *((uint128_t *)(&v63 + 12));
                                                if (!*((long long *)v73))
                                                    sub_f7db74();
                                                Transform__get_forward(*((long long *)v73), 0);
                                                v145 = &v30;
                                                memcpy(&v30, &v45, 16);
                                                v31 = (int)*((uint128_t *)&v46);
                                                v32 = (int)*((uint128_t *)(&v46 + 12));
                                            }
                                            else
                                            {
                                                if (!*((long long *)v73))
                                                    sub_f7db74();
                                                Transform__get_position(*((long long *)v73), 0);
                                                if (!*((long long *)v73))
                                                    sub_f7db74();
                                                Transform__get_forward(*((long long *)v73), 0);
                                                if (!ptr->field_b8)
                                                    sub_f7db74();
                                                v146 = LayerMask__op_Implicit(*((int *)&ptr->padding_36d[7]), 0);
                                                if (!g_1ef0e48->field_e0)
                                                    sub_f7da5c(g_1ef0e48);
                                                if (!(Physics__Raycast(&choice, v146, 0) & 1))
                                                    goto LABEL_10bc24c;
                                                memcpy(&v45, &choice, 16);
                                                *((uint128_t *)&v46) = *((uint128_t *)&v63);
                                                *((uint128_t *)&(&v46)[12]) = *((uint128_t *)(&v63 + 12));
                                                if (!*((long long *)v73))
                                                    sub_f7db74();
                                                Transform__get_forward(*((long long *)v73), 0);
                                                v145 = &v27;
                                                memcpy(&v27, &v45, 16);
                                                v28 = (int)*((uint128_t *)&v46);
                                                v29 = (int)*((uint128_t *)(&v46 + 12));
                                            }
                                        }
                                        else
                                        {
                                            if (!ptr->field_80)
                                                sub_f7db74();
                                            v26 = *((long long *)(ptr10 + 40));
                                            v25 = *((int *)((char *)&ptr->field_42c + 4));
                                            v147 = LayerMask__op_Implicit(*((int *)&ptr->padding_36d[7]), 0);
                                            if (!g_1ef0e48->field_e0)
                                                sub_f7da5c(g_1ef0e48);
                                            if (((char)Physics__SphereCast(&choice, v147, 0) & 1))
                                            {
                                                v145 = &v36;
                                                memcpy(&v36, &choice, 16);
                                                v37 = (int)*((uint128_t *)&v63);
                                                v38 = (int)*((uint128_t *)(&v63 + 12));
                                            }
                                            else
                                            {
                                                if (!*((long long *)v73))
                                                    sub_f7db74();
                                                Transform__get_position(*((long long *)v73), 0);
                                                v148 = LayerMask__op_Implicit(*((int *)&ptr->padding_36d[7]), 0);
                                                if (!g_1ef0e48->field_e0)
                                                    sub_f7da5c(g_1ef0e48);
                                                if (!(Physics__Raycast(&choice, v148, 0) & 1))
                                                    goto LABEL_10bc24c;
                                                v145 = &v33;
                                                memcpy(&v33, &choice, 16);
                                                v34 = (int)*((uint128_t *)&v63);
                                                v35 = (int)*((uint128_t *)(&v63 + 12));
                                            }
                                        }
                                        WeaponBehavior__HitObject(ptr, v145, 0);
LABEL_10bc24c:
                                        if (ptr->padding_21c[9])
                                            break;
                                        goto LABEL_10bcb8c;
                                    }
                                    v126 = v2;
                                    if (v124)
                                        goto LABEL_10bbe34;
                                    if (!ptr->field_b8)
                                        sub_f7db74();
                                    if (ptr->field_b8->field_106)
                                    {
                                        v127 = LayerMask__op_Implicit(*((int *)&ptr->padding_36d[7]), 0);
                                        if (!g_1ef0e48->field_e0)
                                            sub_f7da5c(g_1ef0e48);
                                        v128 = v91;
                                        if (!(Physics__Raycast(&choice, v127, 0) & 1))
                                            continue;
                                        RaycastHit__get_distance(&choice, 0);
                                        v129 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v128, 0x3fc00000)) >> 5 & 3 | (unsigned long long)(CmpF(v128, 0x3fc00000) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v128, 0x3fc00000)) >> 5 & 3 | (unsigned long long)(CmpF(v128, 0x3fc00000) & 1)) & ((unsigned long long)(char)(CmpF(v128, 0x3fc00000)) >> 5 & 3 | (unsigned long long)(CmpF(v128, 0x3fc00000) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                                        if (!((char)v129))
                                        {
                                            memcpy(&v50, &choice, 16);
                                            v51 = (int)*((uint128_t *)&v63);
                                            v52 = (int)*((uint128_t *)(&v63 + 12));
                                            WeaponBehavior__HitObject(ptr, &v50, 0);
                                            if (!RaycastHit__get_transform(&choice, 0))
                                                sub_f7db74();
                                            v130 = Component__get_tag();
                                            if (!(String__op_Equality(v130, g_1f0fb38, 0) & 1))
                                                continue;
                                            RaycastHit__get_point(&choice, 0);
                                            v131 = LayerMask__op_Implicit(ptr->field_378, 0);
                                            if (!g_1ef0e48->field_e0)
                                                sub_f7da5c(g_1ef0e48);
                                            if (!(Physics__Raycast(&choice, v131, 0) & 1))
                                                continue;
                                            v132 = &v47;
                                            memcpy(&v47, &choice, 16);
                                            v48 = (int)*((uint128_t *)&v63);
                                            v49 = (int)*((uint128_t *)(&v63 + 12));
                                        }
                                        else
                                        {
                                            if (!*((long long *)v73))
                                                sub_f7db74();
                                            Transform__get_position(*((long long *)v73), 0);
                                            if (!*((long long *)v73))
                                                sub_f7db74();
                                            Transform__get_forward(*((long long *)v73), 0);
                                            if (!*((long long *)v73))
                                                sub_f7db74();
                                            Transform__get_forward(*((long long *)v73), 0);
                                            v24 = 0x3fc00000;
                                            v25 = v128;
                                            v21 = ptr->field_404;
                                            v22 = *((int *)&ptr->padding_380[128]);
                                            v23 = ptr->field_408;
                                            v26 = ptr->field_148;
                                            v133 = LayerMask__op_Implicit(*((int *)&ptr->padding_36d[7]), 0);
                                            if (!g_1ef0e48->field_e0)
                                                sub_f7da5c(g_1ef0e48);
                                            if (!(Physics__Raycast(&choice, v133, 0) & 1))
                                                continue;
                                            memcpy(&v45, &choice, 16);
                                            *((uint128_t *)&v46) = *((uint128_t *)&v63);
                                            *((uint128_t *)&(&v46)[12]) = *((uint128_t *)(&v63 + 12));
                                            if (!*((long long *)v73))
                                                sub_f7db74();
                                            Transform__get_forward(*((long long *)v73), 0);
                                            memcpy(&v44, &v46 - 12, 16);
                                            v42 = v45;
                                            v43 = (int)*((uint128_t *)&v46);
                                            WeaponBehavior__HitObject(ptr, &v42, 0);
                                            if (!RaycastHit__get_transform(&choice, 0))
                                                sub_f7db74();
                                            v134 = Component__get_tag();
                                            if (!(String__op_Equality(v134, g_1f0fb38, 0) & 1))
                                                continue;
                                            RaycastHit__get_point(&choice, 0);
                                            v135 = LayerMask__op_Implicit(ptr->field_378, 0);
                                            if (!g_1ef0e48->field_e0)
                                                sub_f7da5c(g_1ef0e48);
                                            if (!(Physics__Raycast(&choice, v135, 0) & 1))
                                                continue;
                                            memcpy(&v45, &choice, 16);
                                            *((uint128_t *)&v46) = *((uint128_t *)&v63);
                                            *((uint128_t *)&(&v46)[12]) = *((uint128_t *)(&v63 + 12));
                                            if (!*((long long *)v73))
                                                sub_f7db74();
                                            Transform__get_forward(*((long long *)v73), 0);
                                            v132 = &v39;
                                            memcpy(&v41, &v46 - 12, 16);
                                            v39 = v45;
                                            v40 = (int)*((uint128_t *)&v46);
                                        }
                                        ptr8 = ptr;
                                        goto LABEL_10bcb5c;
                                    }
                                    v137 = ptr->field_a8;
                                    if (!v137)
                                        sub_f7db74();
                                    if (v137->field_a8)
                                    {
                                        if (!*((long long *)v73))
                                            sub_f7db74();
                                        Transform__get_position(*((long long *)v73), 0);
                                        v138 = LayerMask__op_Implicit(*((int *)&ptr->padding_36d[7]), 0);
                                        if (!g_1ef0e48->field_e0)
                                            sub_f7da5c(g_1ef0e48);
                                        if ((Physics__Raycast(&choice, v138, 0) & 1))
                                            goto LABEL_10bc538;
                                        v137 = ptr->field_a8;
                                        if (!v137)
                                            sub_f7db74();
                                    }
                                    if (v137->field_a8)
                                        continue;
                                    if (!*((long long *)v73))
                                        sub_f7db74();
                                    Transform__get_position(*((long long *)v73), 0);
                                    v139 = LayerMask__op_Implicit(*((int *)&ptr->padding_36d[7]), 0);
                                    if (!g_1ef0e48->field_e0)
                                        sub_f7da5c(g_1ef0e48);
                                    if (!(Physics__Raycast(&choice, v139, 0) & 1))
                                        continue;
LABEL_10bc538:
                                    memcpy(&v56, &choice, 16);
                                    v57 = (int)*((uint128_t *)&v63);
                                    v58 = (int)*((uint128_t *)(&v63 + 12));
                                    WeaponBehavior__HitObject(ptr, &v56, 0);
                                    if (!RaycastHit__get_transform(&choice, 0))
                                        sub_f7db74();
                                    v140 = Component__get_tag();
                                    if (!(String__op_Equality(v140, g_1f0fb38, 0) & 1))
                                        continue;
                                    RaycastHit__get_point(&choice, 0);
                                    v141 = LayerMask__op_Implicit(ptr->field_378, 0);
                                    if (!g_1ef0e48->field_e0)
                                        sub_f7da5c(g_1ef0e48);
                                    if (!(Physics__Raycast(&choice, v141, 0) & 1))
                                        continue;
                                    v132 = &v53;
                                    memcpy(&v53, &choice, 16);
                                    v54 = (int)*((uint128_t *)&v63);
                                    v55 = (int)*((uint128_t *)(&v63 + 12));
                                    ptr8 = ptr;
LABEL_10bcb5c:
                                    WeaponBehavior__HitObject(ptr8, v132, 1);
                                    if (ptr->padding_444[192])
                                        MonoBehaviour__StartCoroutine(ptr, WeaponBehavior__EmitTracers(ptr), 0);
LABEL_10bcb8c:
                                    v78 = 0x3f800000;
                                    v150 = (int)_INSERT(_INSERT(ptr->field_154 CONCAT 0, 0, ptr->field_154), 4, 0);
                                    v74 = _INSERT(v150, 8, 0);
                                    v77 = v6 + 0x3f800000;
                                    v151 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(v77, v74)) >> 5 & 3 | (unsigned long long)(CmpF(v77, v74) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v77, v74)) >> 5 & 3 | (unsigned long long)(CmpF(v77, v74) & 1)) & ((unsigned long long)(char)(CmpF(v77, v74)) >> 5 & 3 | (unsigned long long)(CmpF(v77, v74) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                                } while ((char)v151);
                                goto LABEL_10bcc1c;
                            }
                            else
                            {
                                if (!g_1ef0c58->field_e0)
                                    sub_f7da5c(g_1ef0c58);
                                if (!(Object__op_Implicit(ptr->field_28, 0) & 1))
                                    goto LABEL_10bb828;
                                if (ptr->field_28)
                                {
                                    if (!(Animator__get_isInitialized(ptr->field_28, 0) & 1))
                                        goto LABEL_10bb828;
                                    if (ptr->field_28)
                                    {
                                        Animator__SetTrigger(ptr->field_28, g_1f0a430, 0);
                                        goto LABEL_10bb828;
                                    }
                                }
                            }
                        }
                    }
                    else if (ptr->field_20)
                    {
                        Animator__SetTrigger(ptr->field_20, g_1f0a430, 0);
                        goto LABEL_10bcfbc;
                    }
                }
            }
        }
    }
LABEL_10bd094:
    sub_f7db74();
}
```


## `WeaponBehavior.<FireOneShot>d__354.get_Current` — RVA `0xcbd098`

- Decompiled symbol: `WeaponBehavior_FireOneShot_d__354_get_Current`
- Metadata signature: `private object System.Collections.Generic.IEnumerator<System.Object>.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long WeaponBehavior_FireOneShot_d__354_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```


## `WeaponBehavior.<FireOneShot>d__354.Reset` — RVA `0xcbd0a0`

- Decompiled symbol: `WeaponBehavior_FireOneShot_d__354_Reset`
- Metadata signature: `private void System.Collections.IEnumerator.Reset() { }`
- Native interval: `56` bytes
- Result: `pseudocode`

```c
extern long long g_1ef0bd8;
extern long long g_1f05370;

void WeaponBehavior_FireOneShot_d__354_Reset(void)
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
    sub_f7da4c(v4, sub_f7d940(&g_1f05370));
}
```


## `WeaponBehavior.<FireOneShot>d__354.get_Current` — RVA `0xcbd0d8`

- Decompiled symbol: `WeaponBehavior_FireOneShot_d__354_get_Current`
- Metadata signature: `private object System.Collections.IEnumerator.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long WeaponBehavior_FireOneShot_d__354_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```


## `WeaponBehavior.<MuzzFlash>d__357.ctor` — RVA `0xcbd0e0`

- Decompiled symbol: `WeaponBehavior_MuzzFlash_d__357_ctor`
- Metadata signature: `public void .ctor(int <>1__state) { }`
- Native interval: `40` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

void WeaponBehavior_MuzzFlash_d__357_ctor(struct_0 *ptr, unsigned int a1)
{
    Object__ctor();
    ptr->field_10 = a1;
    return;
}
```


## `WeaponBehavior.<MuzzFlash>d__357.Dispose` — RVA `0xcbd108`

- Decompiled symbol: `WeaponBehavior_MuzzFlash_d__357_Dispose`
- Metadata signature: `private void System.IDisposable.Dispose() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long WeaponBehavior_MuzzFlash_d__357_Dispose(void)
{
    unsigned long v0;  // x0

    return v0;
}
```


## `WeaponBehavior.<MuzzFlash>d__357.MoveNext` — RVA `0xcbd10c`

- Decompiled symbol: `WeaponBehavior_MuzzFlash_d__357_MoveNext`
- Metadata signature: `private bool MoveNext() { }`
- Native interval: `1812` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: Decompiler produced no C-like text

```c
// 0x10bd10c: sub sp, sp, #0xc0
// 0x10bd110: stp d15, d14, [sp, #0x60]
// 0x10bd114: stp d13, d12, [sp, #0x70]
// 0x10bd118: stp d11, d10, [sp, #0x80]
// 0x10bd11c: stp d9, d8, [sp, #0x90]
// 0x10bd120: stp x30, x21, [sp, #0xa0]
// 0x10bd124: stp x20, x19, [sp, #0xb0]
// 0x10bd128: adrp x19, #0x1fab000
// 0x10bd12c: ldrb w8, [x19, #0x4f1]
// 0x10bd130: mov x20, x0
// 0x10bd134: tbnz w8, #0, #0x10bd158
// 0x10bd138: adrp x0, #0x1e8c000
// 0x10bd13c: ldr x0, [x0, #0xd8]
// 0x10bd140: bl #0xf7d92c
// 0x10bd144: adrp x0, #0x1e8e000
// 0x10bd148: ldr x0, [x0, #0x6d8]
// 0x10bd14c: bl #0xf7d92c
// 0x10bd150: mov w8, #1
// 0x10bd154: strb w8, [x19, #0x4f1]
// 0x10bd158: movi v0.2d, #0000000000000000
// 0x10bd15c: str xzr, [sp, #0x58]
// 0x10bd160: stp q0, q0, [sp, #0x30]
// 0x10bd164: ldr w8, [x20, #0x10]
// 0x10bd168: ldr x19, [x20, #0x20]
// 0x10bd16c: cmp w8, #1
// 0x10bd170: b.eq #0x10bd1b4
// 0x10bd174: cbnz w8, #0x10bd580
// 0x10bd178: mov w8, #-1
// 0x10bd17c: str w8, [x20, #0x10]
// 0x10bd180: cbz x19, #0x10bd81c
// 0x10bd184: adrp x8, #0x1e8c000
// 0x10bd188: ldr x8, [x8, #0xd8]
// 0x10bd18c: ldr x21, [x19, #0x448]
// 0x10bd190: ldr x0, [x8]
// 0x10bd194: ldr w8, [x0, #0xe0]
// 0x10bd198: cbnz w8, #0x10bd1a0
// 0x10bd19c: bl #0xf7da5c
// 0x10bd1a0: mov x0, x21
// 0x10bd1a4: mov x1, xzr
// 0x10bd1a8: bl #0x1b98274
// 0x10bd1ac: tbnz w0, #0, #0x10bd1c0
// 0x10bd1b0: b #0x10bd580
// 0x10bd1b4: mov w8, #-1
// 0x10bd1b8: str w8, [x20, #0x10]
// 0x10bd1bc: cbz x19, #0x10bd81c
// 0x10bd1c0: ldrb w8, [x19, #0x4a9]
// 0x10bd1c4: cbz w8, #0x10bd26c
// 0x10bd1c8: ldr x8, [x19, #0x80]
// 0x10bd1cc: cbz x8, #0x10bd81c
// 0x10bd1d0: ldrb w8, [x8, #0x256]
// 0x10bd1d4: cbz w8, #0x10bd2a8
// 0x10bd1d8: adrp x8, #0x1e8c000
// 0x10bd1dc: ldr x8, [x8, #0xd8]
// 0x10bd1e0: ldr x20, [x19, #0x4b8]
// 0x10bd1e4: ldr x0, [x8]
// 0x10bd1e8: ldr w8, [x0, #0xe0]
// 0x10bd1ec: cbnz w8, #0x10bd1f4
// 0x10bd1f0: bl #0xf7da5c
// 0x10bd1f4: mov x0, x20
// 0x10bd1f8: mov x1, xzr
// 0x10bd1fc: bl #0x1b98274
// 0x10bd200: tbz w0, #0, #0x10bd240
// 0x10bd204: ldr w8, [x19, #0x4cc]
// 0x10bd208: ldr w9, [x19, #0x4ac]
// 0x10bd20c: cmp w8, w9
// 0x10bd210: b.lt #0x10bd240
// 0x10bd214: ldrb w8, [x19, #0x4dc]
// 0x10bd218: cbnz w8, #0x10bd240
// 0x10bd21c: mov x0, x19
// 0x10bd220: mov x1, xzr
// 0x10bd224: bl #0x10ba2a8
// 0x10bd228: mov x1, x0
// 0x10bd22c: mov x0, x19
// 0x10bd230: mov x2, xzr
// 0x10bd234: bl #0x1b95d40
// 0x10bd238: mov w8, #1
// 0x10bd23c: strb w8, [x19, #0x4dc]
// 0x10bd240: ldr x8, [x19, #0x80]
// 0x10bd244: cbz x8, #0x10bd81c
// 0x10bd248: ldrb w8, [x8, #0x256]
// 0x10bd24c: cbz w8, #0x10bd3b8
// 0x10bd250: ldr x8, [x19, #0x88]
// 0x10bd254: cbz x8, #0x10bd81c
// 0x10bd258: ldr d0, [x8, #0x110]
// 0x10bd25c: add x9, x19, #0x454
// 0x10bd260: str d0, [x9]
// 0x10bd264: ldr s0, [x8, #0x118]
// 0x10bd268: b #0x10bd3c8
// 0x10bd26c: ldr x8, [x19, #0xb8]
// 0x10bd270: cbz x8, #0x10bd81c
// 0x10bd274: ldrb w8, [x8, #0x106]
// 0x10bd278: cbz w8, #0x10bd1c8
// 0x10bd27c: ldr x8, [x19, #0x90]
// 0x10bd280: cbz x8, #0x10bd81c
// 0x10bd284: ldrb w8, [x8, #0x129]
// 0x10bd288: cbnz w8, #0x10bd1c8
// 0x10bd28c: str xzr, [x20, #0x18]!
// 0x10bd290: mov x0, x20
// 0x10bd294: mov x1, xzr
// 0x10bd298: bl #0xf7d8d0
// 0x10bd29c: mov w0, #1
// 0x10bd2a0: stur w0, [x20, #-8]
// 0x10bd2a4: b #0x10bd584
// 0x10bd2a8: adrp x21, #0x1e8c000
// 0x10bd2ac: ldr x21, [x21, #0xd8]
// 0x10bd2b0: ldr x20, [x19, #0x468]
// 0x10bd2b4: ldr x0, [x21]
// 0x10bd2b8: ldr w8, [x0, #0xe0]
// 0x10bd2bc: cbnz w8, #0x10bd2c4
// 0x10bd2c0: bl #0xf7da5c
// 0x10bd2c4: mov x0, x20
// 0x10bd2c8: mov x1, xzr
// 0x10bd2cc: bl #0x1b98274
// 0x10bd2d0: tbz w0, #0, #0x10bd30c
// 0x10bd2d4: ldr x8, [x19, #0xb8]
// 0x10bd2d8: cbz x8, #0x10bd81c
// 0x10bd2dc: ldrb w8, [x8, #0x106]
// 0x10bd2e0: cbnz w8, #0x10bd30c
// 0x10bd2e4: ldr x0, [x19, #0x490]
// 0x10bd2e8: cbz x0, #0x10bd81c
// 0x10bd2ec: mov w1, #1
// 0x10bd2f0: mov x2, xzr
// 0x10bd2f4: bl #0x1b91660
// 0x10bd2f8: ldr x0, [x19, #0x490]
// 0x10bd2fc: cbz x0, #0x10bd81c
// 0x10bd300: fmov s0, #8.00000000
// 0x10bd304: mov x1, xzr
// 0x10bd308: bl #0x1b7bccc
// 0x10bd30c: ldrb w8, [x19, #0x4dd]
// 0x10bd310: cbz w8, #0x10bd1d8
// 0x10bd314: ldr x0, [x21]
// 0x10bd318: ldr x20, [x19, #0x4e0]
// 0x10bd31c: ldr w8, [x0, #0xe0]
// 0x10bd320: cbnz w8, #0x10bd328
// 0x10bd324: bl #0xf7da5c
// 0x10bd328: mov x0, x20
// 0x10bd32c: mov x1, xzr
// 0x10bd330: bl #0x1b98274
// 0x10bd334: tbz w0, #0, #0x10bd1d8
// 0x10bd338: ldr s0, [x19, #0x504]
// 0x10bd33c: ldr x0, [x19, #0x498]
// 0x10bd340: str s0, [x19, #0x500]
// 0x10bd344: cbz x0, #0x10bd81c
// 0x10bd348: mov x1, xzr
// 0x10bd34c: bl #0x1b79b88
// 0x10bd350: cbz x0, #0x10bd81c
// 0x10bd354: adrp x8, #0x1e8e000
// 0x10bd358: ldr s3, [x19, #0x500]
// 0x10bd35c: ldr s2, [x19, #0x4fc]
// 0x10bd360: ldr s1, [x19, #0x4f8]
// 0x10bd364: ldr s0, [x19, #0x4f4]
// 0x10bd368: ldr x8, [x8, #0x6d8]
// 0x10bd36c: mov x2, xzr
// 0x10bd370: ldr x1, [x8]
// 0x10bd374: bl #0x1b7a790
// 0x10bd378: ldr x8, [x19, #0xb8]
// 0x10bd37c: cbz x8, #0x10bd81c
// 0x10bd380: ldrb w8, [x8, #0x106]
// 0x10bd384: cbz w8, #0x10bd5a4
// 0x10bd388: ldr x0, [x19, #0x4e0]
// 0x10bd38c: cbz x0, #0x10bd81c
// 0x10bd390: mov x1, xzr
// 0x10bd394: bl #0x1b92154
// 0x10bd398: ldr x8, [x19, #0x4a0]
// 0x10bd39c: cbz x8, #0x10bd81c
// 0x10bd3a0: mov x20, x0
// 0x10bd3a4: mov x0, x8
// 0x10bd3a8: mov x1, xzr
// 0x10bd3ac: bl #0x1b9d508
// 0x10bd3b0: cbnz x20, #0x10bd704
// 0x10bd3b4: b #0x10bd81c
// 0x10bd3b8: add x8, x19, #0x454
// 0x10bd3bc: fmov v0.2s, #1.00000000
// 0x10bd3c0: str d0, [x8]
// 0x10bd3c4: fmov s0, #1.00000000
// 0x10bd3c8: adrp x8, #0x832000
// 0x10bd3cc: str s0, [x19, #0x45c]
// 0x10bd3d0: ldr s0, [x8, #0x4d4]
// 0x10bd3d4: fmov s1, #0.50000000
// 0x10bd3d8: mov x0, xzr
// 0x10bd3dc: bl #0x1b9012c
// 0x10bd3e0: ldr x0, [x19, #0x488]
// 0x10bd3e4: str s0, [x19, #0x460]
// 0x10bd3e8: cbz x0, #0x10bd81c
// 0x10bd3ec: mov x1, xzr
// 0x10bd3f0: bl #0x1b79b88
// 0x10bd3f4: cbz x0, #0x10bd81c
// 0x10bd3f8: adrp x8, #0x1e8e000
// 0x10bd3fc: ldr s3, [x19, #0x460]
// 0x10bd400: ldr s2, [x19, #0x45c]
// 0x10bd404: ldr s1, [x19, #0x458]
// 0x10bd408: ldr s0, [x19, #0x454]
// 0x10bd40c: ldr x8, [x8, #0x6d8]
// 0x10bd410: mov x2, xzr
// 0x10bd414: ldr x1, [x8]
// 0x10bd418: bl #0x1b7a790
// 0x10bd41c: ldr x0, [x19, #0x488]
// 0x10bd420: cbz x0, #0x10bd81c
// 0x10bd424: mov w1, #1
// 0x10bd428: mov x2, xzr
// 0x10bd42c: bl #0x1b799d0
// 0x10bd430: ldr x8, [x19, #0xb8]
// 0x10bd434: cbz x8, #0x10bd81c
// 0x10bd438: ldrb w8, [x8, #0x106]
// 0x10bd43c: cbz w8, #0x10bd514
// 0x10bd440: ldr x0, [x19, #0x488]
// 0x10bd444: cbz x0, #0x10bd81c
// 0x10bd448: mov x1, xzr
// 0x10bd44c: bl #0x1b92154
// 0x10bd450: cbz x0, #0x10bd81c
// 0x10bd454: mov x1, xzr
// 0x10bd458: mov x19, x0
// 0x10bd45c: bl #0x1b9d7f0
// 0x10bd460: mov x0, xzr
// 0x10bd464: mov v8.16b, v0.16b
// 0x10bd468: mov v9.16b, v1.16b
// 0x10bd46c: mov v10.16b, v2.16b
// 0x10bd470: mov v11.16b, v3.16b
// 0x10bd474: bl #0x1b901f4
// 0x10bd478: adrp x8, #0x832000
// 0x10bd47c: ldr s1, [x8, #0x3e4]
// 0x10bd480: mov w8, #0x43b40000
// 0x10bd484: fmov s2, w8
// 0x10bd488: fmul s0, s0, s2
// 0x10bd48c: fmul s2, s0, s1
// 0x10bd490: fmov s0, wzr
// 0x10bd494: fmov s1, wzr
// 0x10bd498: mov x0, xzr
// 0x10bd49c: bl #0x1b8b12c
// 0x10bd4a0: fmul s4, s11, s0
// 0x10bd4a4: fmul s5, s8, s3
// 0x10bd4a8: fmul s7, s10, s1
// 0x10bd4ac: fmul s16, s11, s1
// 0x10bd4b0: fmul s17, s9, s3
// 0x10bd4b4: fmul s18, s10, s0
// 0x10bd4b8: fmul s20, s8, s1
// 0x10bd4bc: fmul s21, s8, s0
// 0x10bd4c0: fmul s22, s9, s0
// 0x10bd4c4: fmul s0, s9, s1
// 0x10bd4c8: fmul s1, s11, s2
// 0x10bd4cc: fmul s23, s11, s3
// 0x10bd4d0: fmul s3, s10, s3
// 0x10bd4d4: fmul s6, s9, s2
// 0x10bd4d8: fmul s19, s8, s2
// 0x10bd4dc: fmul s24, s10, s2
// 0x10bd4e0: fadd s2, s4, s5
// 0x10bd4e4: fadd s4, s16, s17
// 0x10bd4e8: fadd s1, s1, s3
// 0x10bd4ec: fsub s3, s23, s21
// 0x10bd4f0: fadd s2, s6, s2
// 0x10bd4f4: fadd s4, s18, s4
// 0x10bd4f8: fadd s5, s20, s1
// 0x10bd4fc: fsub s3, s3, s0
// 0x10bd500: fsub s0, s2, s7
// 0x10bd504: fsub s1, s4, s19
// 0x10bd508: fsub s2, s5, s22
// 0x10bd50c: fsub s3, s3, s24
// 0x10bd510: b #0x10bd574
// 0x10bd514: ldr x19, [x19, #0x448]
// 0x10bd518: mov x0, xzr
// 0x10bd51c: bl #0x1b901f4
// 0x10bd520: adrp x20, #0x1fab000
// 0x10bd524: ldrb w8, [x20, #0x3e3]
// 0x10bd528: mov v8.16b, v0.16b
// 0x10bd52c: cbnz w8, #0x10bd544
// 0x10bd530: adrp x0, #0x1e8c000
// 0x10bd534: ldr x0, [x0, #0x1e8]
// 0x10bd538: bl #0xf7d92c
// 0x10bd53c: mov w8, #1
// 0x10bd540: strb w8, [x20, #0x3e3]
// 0x10bd544: adrp x8, #0x1e8c000
// 0x10bd548: ldr x8, [x8, #0x1e8]
// 0x10bd54c: mov x0, xzr
// 0x10bd550: ldr x8, [x8]
// 0x10bd554: ldr x8, [x8, #0xb8]
// 0x10bd558: ldp s1, s2, [x8, #0x48]
// 0x10bd55c: ldr s3, [x8, #0x50]
// 0x10bd560: mov w8, #0x43b40000
// 0x10bd564: fmov s0, w8
// 0x10bd568: fmul s0, s8, s0
// 0x10bd56c: bl #0x1b8b260
// 0x10bd570: cbz x19, #0x10bd81c
// 0x10bd574: mov x0, x19
// 0x10bd578: mov x1, xzr
// 0x10bd57c: bl #0x1b9d874
// 0x10bd580: mov w0, wzr
// 0x10bd584: ldp x20, x19, [sp, #0xb0]
// 0x10bd588: ldp x30, x21, [sp, #0xa0]
// 0x10bd58c: ldp d9, d8, [sp, #0x90]
// 0x10bd590: ldp d11, d10, [sp, #0x80]
// 0x10bd594: ldp d13, d12, [sp, #0x70]
// 0x10bd598: ldp d15, d14, [sp, #0x60]
// 0x10bd59c: add sp, sp, #0xc0
// 0x10bd5a0: ret
// 0x10bd5a4: ldr x8, [x19, #0x98]
// 0x10bd5a8: cbz x8, #0x10bd81c
// 0x10bd5ac: ldr x0, [x19, #0x4e0]
// 0x10bd5b0: cbz x0, #0x10bd81c
// 0x10bd5b4: ldrb w21, [x8, #0x2d0]
// 0x10bd5b8: mov x1, xzr
// 0x10bd5bc: bl #0x1b92154
// 0x10bd5c0: ldr x8, [x19, #0x78]
// 0x10bd5c4: cbz x8, #0x10bd81c
// 0x10bd5c8: mov x20, x0
// 0x10bd5cc: mov x0, x8
// 0x10bd5d0: mov x1, xzr
// 0x10bd5d4: bl #0x1b9d508
// 0x10bd5d8: ldr x0, [x19, #0x78]
// 0x10bd5dc: cbz x0, #0x10bd81c
// 0x10bd5e0: mov v8.16b, v0.16b
// 0x10bd5e4: mov v9.16b, v1.16b
// 0x10bd5e8: mov v10.16b, v2.16b
// 0x10bd5ec: mov x1, xzr
// 0x10bd5f0: cbz w21, #0x10bd644
// 0x10bd5f4: bl #0x1b9d9b8
// 0x10bd5f8: cbz x20, #0x10bd81c
// 0x10bd5fc: ldr s3, [x19, #0x4b0]
// 0x10bd600: ldr s4, [x19, #0x4f0]
// 0x10bd604: ldr s5, [x19, #0x434]
// 0x10bd608: ldr s6, [x19, #0x430]
// 0x10bd60c: ldr s7, [x19, #0x42c]
// 0x10bd610: fmul s2, s2, s3
// 0x10bd614: fmul s1, s1, s3
// 0x10bd618: fmul s0, s0, s3
// 0x10bd61c: fmul s3, s4, s5
// 0x10bd620: fmul s5, s4, s6
// 0x10bd624: fmul s4, s4, s7
// 0x10bd628: fadd s2, s10, s2
// 0x10bd62c: fadd s1, s9, s1
// 0x10bd630: fadd s0, s8, s0
// 0x10bd634: fadd s2, s2, s3
// 0x10bd638: fadd s1, s1, s5
// 0x10bd63c: fadd s0, s0, s4
// 0x10bd640: b #0x10bd704
// 0x10bd644: bl #0x1b9d8c8
// 0x10bd648: ldr x0, [x19, #0x78]
// 0x10bd64c: cbz x0, #0x10bd81c
// 0x10bd650: ldr s12, [x19, #0x4e8]
// 0x10bd654: mov x1, xzr
// 0x10bd658: mov v15.16b, v2.16b
// 0x10bd65c: stp s1, s0, [sp, #8]
// 0x10bd660: bl #0x1b9d940
// 0x10bd664: ldr x0, [x19, #0x78]
// 0x10bd668: str s0, [sp, #4]
// 0x10bd66c: cbz x0, #0x10bd81c
// 0x10bd670: ldr s13, [x19, #0x4ec]
// 0x10bd674: mov x1, xzr
// 0x10bd678: mov v14.16b, v1.16b
// 0x10bd67c: mov v11.16b, v2.16b
// 0x10bd680: bl #0x1b9d9b8
// 0x10bd684: cbz x20, #0x10bd81c
// 0x10bd688: ldp s7, s16, [sp, #8]
// 0x10bd68c: ldr s19, [sp, #4]
// 0x10bd690: ldr s3, [x19, #0x4b0]
// 0x10bd694: ldr s4, [x19, #0x4f0]
// 0x10bd698: ldr s17, [x19, #0x434]
// 0x10bd69c: ldr s20, [x19, #0x430]
// 0x10bd6a0: ldr s21, [x19, #0x42c]
// 0x10bd6a4: fmul s5, s15, s12
// 0x10bd6a8: fmul s7, s7, s12
// 0x10bd6ac: fmul s16, s16, s12
// 0x10bd6b0: fmul s6, s11, s13
// 0x10bd6b4: fmul s18, s14, s13
// 0x10bd6b8: fmul s19, s19, s13
// 0x10bd6bc: fadd s5, s10, s5
// 0x10bd6c0: fadd s7, s9, s7
// 0x10bd6c4: fadd s16, s8, s16
// 0x10bd6c8: fadd s5, s5, s6
// 0x10bd6cc: fadd s6, s7, s18
// 0x10bd6d0: fadd s7, s16, s19
// 0x10bd6d4: fmul s2, s2, s3
// 0x10bd6d8: fmul s1, s1, s3
// 0x10bd6dc: fmul s0, s0, s3
// 0x10bd6e0: fmul s16, s4, s17
// 0x10bd6e4: fmul s17, s4, s20
// 0x10bd6e8: fmul s3, s4, s21
// 0x10bd6ec: fadd s2, s5, s2
// 0x10bd6f0: fadd s1, s6, s1
// 0x10bd6f4: fadd s0, s7, s0
// 0x10bd6f8: fadd s2, s2, s16
// 0x10bd6fc: fadd s1, s1, s17
// 0x10bd700: fadd s0, s0, s3
// 0x10bd704: mov x0, x20
// 0x10bd708: mov x1, xzr
// 0x10bd70c: bl #0x1b9d5a8
// 0x10bd710: ldr x20, [x19, #0x4e0]
// 0x10bd714: cbz x20, #0x10bd81c
// 0x10bd718: mov x0, x20
// 0x10bd71c: mov x1, xzr
// 0x10bd720: bl #0x1bc9cb4
// 0x10bd724: str x0, [sp, #0x58]
// 0x10bd728: add x8, sp, #0x10
// 0x10bd72c: add x0, sp, #0x58
// 0x10bd730: mov x1, xzr
// 0x10bd734: bl #0x1bc9f50
// 0x10bd738: ldp q0, q1, [sp, #0x10]
// 0x10bd73c: add x0, sp, #0x30
// 0x10bd740: mov x1, xzr
// 0x10bd744: stp q0, q1, [sp, #0x30]
// 0x10bd748: bl #0x1bca508
// 0x10bd74c: adrp x21, #0x1fab000
// 0x10bd750: ldrb w8, [x21, #0x242]
// 0x10bd754: mov v8.16b, v0.16b
// 0x10bd758: cbnz w8, #0x10bd770
// 0x10bd75c: adrp x0, #0x1e8c000
// 0x10bd760: ldr x0, [x0, #0xa60]
// 0x10bd764: bl #0xf7d92c
// 0x10bd768: mov w8, #1
// 0x10bd76c: strb w8, [x21, #0x242]
// 0x10bd770: adrp x8, #0x1e8c000
// 0x10bd774: ldr x8, [x8, #0xa60]
// 0x10bd778: ldr x0, [x8]
// 0x10bd77c: ldr w8, [x0, #0xe0]
// 0x10bd780: cbnz w8, #0x10bd788
// 0x10bd784: bl #0xf7da5c
// 0x10bd788: fcvt d9, s8
// 0x10bd78c: add x0, sp, #0x10
// 0x10bd790: mov v0.16b, v9.16b
// 0x10bd794: bl #0x1db0c60
// 0x10bd798: fcmp s8, #0.0
// 0x10bd79c: b.ge #0x10bd7b8
// 0x10bd7a0: fmov d1, #-0.50000000
// 0x10bd7a4: fcmp d0, d1
// 0x10bd7a8: b.ne #0x10bd7e0
// 0x10bd7ac: ldr d0, [sp, #0x10]
// 0x10bd7b0: fmov d1, #-1.00000000
// 0x10bd7b4: b #0x10bd7cc
// 0x10bd7b8: fmov d1, #0.50000000
// 0x10bd7bc: fcmp d0, d1
// 0x10bd7c0: b.ne #0x10bd7ec
// 0x10bd7c4: ldr d0, [sp, #0x10]
// 0x10bd7c8: fmov d1, #1.00000000
// 0x10bd7cc: fcvtzs x8, d0
// 0x10bd7d0: fadd d1, d0, d1
// 0x10bd7d4: tst x8, #1
// 0x10bd7d8: fcsel d0, d0, d1, eq
// 0x10bd7dc: b #0x10bd7f4
// 0x10bd7e0: fadd d0, d9, d1
// 0x10bd7e4: frintp d0, d0
// 0x10bd7e8: b #0x10bd7f4
// 0x10bd7ec: fadd d0, d9, d1
// 0x10bd7f0: frintm d0, d0
// 0x10bd7f4: mov x8, #0x7ff0000000000000
// 0x10bd7f8: fmov d1, x8
// 0x10bd7fc: fcvtzs w9, d0
// 0x10bd800: fcmp d0, d1
// 0x10bd804: mov w8, #-0x80000000
// 0x10bd808: csel w1, w8, w9, eq
// 0x10bd80c: mov x0, x20
// 0x10bd810: mov x2, xzr
// 0x10bd814: bl #0x1bc9b7c
// 0x10bd818: b #0x10bd1d8
// 0x10bd81c: bl #0xf7db74
```


## `WeaponBehavior.<MuzzFlash>d__357.get_Current` — RVA `0xcbd820`

- Decompiled symbol: `WeaponBehavior_MuzzFlash_d__357_get_Current`
- Metadata signature: `private object System.Collections.Generic.IEnumerator<System.Object>.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long WeaponBehavior_MuzzFlash_d__357_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```


## `WeaponBehavior.<MuzzFlash>d__357.Reset` — RVA `0xcbd828`

- Decompiled symbol: `WeaponBehavior_MuzzFlash_d__357_Reset`
- Metadata signature: `private void System.Collections.IEnumerator.Reset() { }`
- Native interval: `56` bytes
- Result: `pseudocode`

```c
extern long long g_1ef0bd8;
extern long long g_1f05378;

void WeaponBehavior_MuzzFlash_d__357_Reset(void)
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
    sub_f7da4c(v4, sub_f7d940(&g_1f05378));
}
```


## `WeaponBehavior.<MuzzFlash>d__357.get_Current` — RVA `0xcbd860`

- Decompiled symbol: `WeaponBehavior_MuzzFlash_d__357_get_Current`
- Metadata signature: `private object System.Collections.IEnumerator.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long WeaponBehavior_MuzzFlash_d__357_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```


## `WeaponBehavior.<Reload>d__361.ctor` — RVA `0xcbd868`

- Decompiled symbol: `WeaponBehavior_Reload_d__361_ctor`
- Metadata signature: `public void .ctor(int <>1__state) { }`
- Native interval: `40` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

void WeaponBehavior_Reload_d__361_ctor(struct_0 *ptr, unsigned int a1)
{
    Object__ctor();
    ptr->field_10 = a1;
    return;
}
```


## `WeaponBehavior.<Reload>d__361.Dispose` — RVA `0xcbd890`

- Decompiled symbol: `WeaponBehavior_Reload_d__361_Dispose`
- Metadata signature: `private void System.IDisposable.Dispose() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long WeaponBehavior_Reload_d__361_Dispose(void)
{
    unsigned long v0;  // x0

    return v0;
}
```


## `WeaponBehavior.<Reload>d__361.MoveNext` — RVA `0xcbd894`

- Decompiled symbol: `WeaponBehavior_Reload_d__361_MoveNext`
- Metadata signature: `private bool MoveNext() { }`
- Native interval: `1492` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: Decompiler produced no C-like text

```c
// 0x10bd894: str d8, [sp, #-0x30]!
// 0x10bd898: stp x30, x21, [sp, #0x10]
// 0x10bd89c: stp x20, x19, [sp, #0x20]
// 0x10bd8a0: adrp x19, #0x1fab000
// 0x10bd8a4: ldrb w8, [x19, #0x4f2]
// 0x10bd8a8: mov x20, x0
// 0x10bd8ac: tbnz w8, #0, #0x10bd93c
// 0x10bd8b0: adrp x0, #0x1e8c000
// 0x10bd8b4: ldr x0, [x0, #0xd8]
// 0x10bd8b8: bl #0xf7d92c
// 0x10bd8bc: adrp x0, #0x1e8d000
// 0x10bd8c0: ldr x0, [x0, #0x3e8]
// 0x10bd8c4: bl #0xf7d92c
// 0x10bd8c8: adrp x0, #0x1e8e000
// 0x10bd8cc: ldr x0, [x0, #0x808]
// 0x10bd8d0: bl #0xf7d92c
// 0x10bd8d4: adrp x0, #0x1e8e000
// 0x10bd8d8: ldr x0, [x0, #0x810]
// 0x10bd8dc: bl #0xf7d92c
// 0x10bd8e0: adrp x0, #0x1e8e000
// 0x10bd8e4: ldr x0, [x0, #0x818]
// 0x10bd8e8: bl #0xf7d92c
// 0x10bd8ec: adrp x0, #0x1e8d000
// 0x10bd8f0: ldr x0, [x0]
// 0x10bd8f4: bl #0xf7d92c
// 0x10bd8f8: adrp x0, #0x1e8e000
// 0x10bd8fc: ldr x0, [x0, #0x820]
// 0x10bd900: bl #0xf7d92c
// 0x10bd904: adrp x0, #0x1e8e000
// 0x10bd908: ldr x0, [x0, #0x498]
// 0x10bd90c: bl #0xf7d92c
// 0x10bd910: adrp x0, #0x1e8e000
// 0x10bd914: ldr x0, [x0, #0x828]
// 0x10bd918: bl #0xf7d92c
// 0x10bd91c: adrp x0, #0x1e8e000
// 0x10bd920: ldr x0, [x0, #0x830]
// 0x10bd924: bl #0xf7d92c
// 0x10bd928: adrp x0, #0x1e8e000
// 0x10bd92c: ldr x0, [x0, #0x7f0]
// 0x10bd930: bl #0xf7d92c
// 0x10bd934: mov w8, #1
// 0x10bd938: strb w8, [x19, #0x4f2]
// 0x10bd93c: ldr w8, [x20, #0x10]
// 0x10bd940: ldr x19, [x20, #0x20]
// 0x10bd944: cmp w8, #1
// 0x10bd948: b.eq #0x10bda74
// 0x10bd94c: cbnz w8, #0x10bda5c
// 0x10bd950: mov w8, #-1
// 0x10bd954: str w8, [x20, #0x10]
// 0x10bd958: cbz x19, #0x10bde64
// 0x10bd95c: ldrb w8, [x19, #0x229]
// 0x10bd960: cbnz w8, #0x10bda5c
// 0x10bd964: ldr x8, [x19, #0x80]
// 0x10bd968: cbz x8, #0x10bde64
// 0x10bd96c: ldrb w8, [x8, #0x1a0]
// 0x10bd970: cbnz w8, #0x10bda5c
// 0x10bd974: mov x0, xzr
// 0x10bd978: bl #0x1b9ad58
// 0x10bd97c: fmov s1, #2.00000000
// 0x10bd980: fcmp s0, s1
// 0x10bd984: b.le #0x10bda5c
// 0x10bd988: ldr x8, [x19, #0x80]
// 0x10bd98c: cbz x8, #0x10bde64
// 0x10bd990: ldrb w9, [x8, #0x2b1]
// 0x10bd994: cbz w9, #0x10bd9cc
// 0x10bd998: ldr s0, [x19, #0x3ac]
// 0x10bd99c: fabs s1, s0
// 0x10bd9a0: fmov s0, #0.75000000
// 0x10bd9a4: fcmp s1, s0
// 0x10bd9a8: b.gt #0x10bd9bc
// 0x10bd9ac: ldr s1, [x19, #0x3b0]
// 0x10bd9b0: fabs s1, s1
// 0x10bd9b4: fcmp s1, s0
// 0x10bd9b8: b.le #0x10bd9cc
// 0x10bd9bc: ldrb w9, [x8, #0x2c2]
// 0x10bd9c0: cbnz w9, #0x10bd9cc
// 0x10bd9c4: ldrb w8, [x8, #0x147]
// 0x10bd9c8: cbz w8, #0x10bda5c
// 0x10bd9cc: ldr w8, [x19, #0x128]
// 0x10bd9d0: cmp w8, #1
// 0x10bd9d4: b.lt #0x10bda5c
// 0x10bd9d8: ldr x8, [x19, #0x98]
// 0x10bd9dc: cbz x8, #0x10bde64
// 0x10bd9e0: strb wzr, [x8, #0x2d0]
// 0x10bd9e4: ldr w8, [x19, #0x134]
// 0x10bd9e8: ldr w9, [x19, #0x130]
// 0x10bd9ec: cmp w8, w9
// 0x10bd9f0: b.ne #0x10bdde8
// 0x10bd9f4: ldr x0, [x19, #0x690]
// 0x10bd9f8: cbz x0, #0x10bde64
// 0x10bd9fc: fmov s0, #1.00000000
// 0x10bda00: mov x1, xzr
// 0x10bda04: bl #0x1b6a478
// 0x10bda08: ldr x0, [x19, #0x690]
// 0x10bda0c: cbz x0, #0x10bde64
// 0x10bda10: ldr x1, [x19, #0x6b0]
// 0x10bda14: mov x2, xzr
// 0x10bda18: bl #0x1b6a588
// 0x10bda1c: ldr x0, [x19, #0x690]
// 0x10bda20: cbz x0, #0x10bde64
// 0x10bda24: mov x1, xzr
// 0x10bda28: bl #0x1b6a5cc
// 0x10bda2c: ldr x0, [x19, #0x118]
// 0x10bda30: cbz x0, #0x10bde64
// 0x10bda34: fmov s0, #1.00000000
// 0x10bda38: mov x1, xzr
// 0x10bda3c: bl #0x1b67eb4
// 0x10bda40: ldrb w8, [x19, #0x344]
// 0x10bda44: cbz w8, #0x10bdd90
// 0x10bda48: ldr x0, [x19, #0x118]
// 0x10bda4c: cbz x0, #0x10bde64
// 0x10bda50: adrp x8, #0x1e8e000
// 0x10bda54: ldr x8, [x8, #0x810]
// 0x10bda58: b #0x10bddc0
// 0x10bda5c: mov w21, wzr
// 0x10bda60: mov w0, w21
// 0x10bda64: ldp x20, x19, [sp, #0x20]
// 0x10bda68: ldp x30, x21, [sp, #0x10]
// 0x10bda6c: ldr d8, [sp], #0x30
// 0x10bda70: ret
// 0x10bda74: mov w8, #-1
// 0x10bda78: str w8, [x20, #0x10]
// 0x10bda7c: cbz x19, #0x10bde64
// 0x10bda80: ldr w10, [x19, #0x130]
// 0x10bda84: ldr w9, [x19, #0x12c]
// 0x10bda88: ldr w11, [x19, #0x134]
// 0x10bda8c: sub w8, w10, w9
// 0x10bda90: cmp w11, w10
// 0x10bda94: str w8, [x19, #0x3b4]
// 0x10bda98: b.ne #0x10bdac8
// 0x10bda9c: ldr x11, [x19, #0x90]
// 0x10bdaa0: cbz x11, #0x10bde64
// 0x10bdaa4: strb wzr, [x11, #0x129]
// 0x10bdaa8: ldr w11, [x19, #0x128]
// 0x10bdaac: mov w21, wzr
// 0x10bdab0: subs w8, w11, w8
// 0x10bdab4: b.ge #0x10bdaf0
// 0x10bdab8: add w8, w11, w9
// 0x10bdabc: str w8, [x19, #0x12c]
// 0x10bdac0: str wzr, [x19, #0x128]
// 0x10bdac4: b #0x10bda60
// 0x10bdac8: ldr w12, [x19, #0x128]
// 0x10bdacc: cmp w8, w11
// 0x10bdad0: b.ge #0x10bdafc
// 0x10bdad4: subs w13, w12, w8
// 0x10bdad8: b.lt #0x10bdb04
// 0x10bdadc: ldr w9, [x19, #0x3b8]
// 0x10bdae0: str w10, [x19, #0x12c]
// 0x10bdae4: str w13, [x19, #0x128]
// 0x10bdae8: add w9, w9, w11
// 0x10bdaec: b #0x10bdb28
// 0x10bdaf0: str w8, [x19, #0x128]
// 0x10bdaf4: str w10, [x19, #0x12c]
// 0x10bdaf8: b #0x10bda60
// 0x10bdafc: subs w10, w12, w11
// 0x10bdb00: b.ge #0x10bdb14
// 0x10bdb04: add w9, w12, w9
// 0x10bdb08: str w9, [x19, #0x12c]
// 0x10bdb0c: str wzr, [x19, #0x128]
// 0x10bdb10: b #0x10bdb2c
// 0x10bdb14: ldr w12, [x19, #0x3b8]
// 0x10bdb18: add w9, w11, w9
// 0x10bdb1c: str w9, [x19, #0x12c]
// 0x10bdb20: str w10, [x19, #0x128]
// 0x10bdb24: add w9, w12, w11
// 0x10bdb28: str w9, [x19, #0x3b8]
// 0x10bdb2c: cmp w8, #1
// 0x10bdb30: b.lt #0x10bdd78
// 0x10bdb34: adrp x20, #0x1e8e000
// 0x10bdb38: ldr x20, [x20, #0x498]
// 0x10bdb3c: mov x0, x19
// 0x10bdb40: mov x2, xzr
// 0x10bdb44: ldr x1, [x20]
// 0x10bdb48: bl #0x1b95b9c
// 0x10bdb4c: ldr x0, [x19, #0x110]
// 0x10bdb50: cbz x0, #0x10bde64
// 0x10bdb54: ldr x1, [x20]
// 0x10bdb58: mov x2, xzr
// 0x10bdb5c: bl #0x1b67884
// 0x10bdb60: ldr x0, [x19, #0x118]
// 0x10bdb64: cbz x0, #0x10bde64
// 0x10bdb68: adrp x8, #0x1e8e000
// 0x10bdb6c: ldr x8, [x8, #0x818]
// 0x10bdb70: mov x2, xzr
// 0x10bdb74: ldr x1, [x8]
// 0x10bdb78: bl #0x1b67884
// 0x10bdb7c: ldr w8, [x19, #0x3b4]
// 0x10bdb80: ldr w9, [x19, #0x134]
// 0x10bdb84: cmp w8, w9
// 0x10bdb88: b.le #0x10bdc08
// 0x10bdb8c: ldr w8, [x19, #0x128]
// 0x10bdb90: cmp w8, #0
// 0x10bdb94: b.le #0x10bdc08
// 0x10bdb98: ldr x0, [x19, #0x690]
// 0x10bdb9c: cbz x0, #0x10bde64
// 0x10bdba0: ldr x1, [x19, #0x6b0]
// 0x10bdba4: mov x2, xzr
// 0x10bdba8: bl #0x1b6a588
// 0x10bdbac: ldr x8, [x19, #0x80]
// 0x10bdbb0: cbz x8, #0x10bde64
// 0x10bdbb4: ldrb w8, [x8, #0x2dc]
// 0x10bdbb8: cbnz w8, #0x10bdccc
// 0x10bdbbc: adrp x8, #0x1e8c000
// 0x10bdbc0: ldr x8, [x8, #0xd8]
// 0x10bdbc4: ldr x20, [x19, #0x20]
// 0x10bdbc8: ldr x0, [x8]
// 0x10bdbcc: ldr w8, [x0, #0xe0]
// 0x10bdbd0: cbnz w8, #0x10bdbd8
// 0x10bdbd4: bl #0xf7da5c
// 0x10bdbd8: mov x0, x20
// 0x10bdbdc: mov x1, xzr
// 0x10bdbe0: bl #0x1b98274
// 0x10bdbe4: tbz w0, #0, #0x10bdccc
// 0x10bdbe8: ldr x0, [x19, #0x20]
// 0x10bdbec: cbz x0, #0x10bde64
// 0x10bdbf0: adrp x8, #0x1e8e000
// 0x10bdbf4: ldr x8, [x8, #0x830]
// 0x10bdbf8: mov x2, xzr
// 0x10bdbfc: ldr x1, [x8]
// 0x10bdc00: bl #0x1b67884
// 0x10bdc04: b #0x10bdccc
// 0x10bdc08: ldr x0, [x19, #0x690]
// 0x10bdc0c: cbz x0, #0x10bde64
// 0x10bdc10: ldr x1, [x19, #0x6b8]
// 0x10bdc14: mov x2, xzr
// 0x10bdc18: bl #0x1b6a588
// 0x10bdc1c: ldr x0, [x19, #0x110]
// 0x10bdc20: cbz x0, #0x10bde64
// 0x10bdc24: adrp x8, #0x1e8d000
// 0x10bdc28: ldr x8, [x8]
// 0x10bdc2c: mov x2, xzr
// 0x10bdc30: ldr x1, [x8]
// 0x10bdc34: bl #0x1b67884
// 0x10bdc38: ldr x8, [x19, #0x80]
// 0x10bdc3c: cbz x8, #0x10bde64
// 0x10bdc40: ldrb w8, [x8, #0x2dc]
// 0x10bdc44: cbnz w8, #0x10bdcb4
// 0x10bdc48: adrp x8, #0x1e8c000
// 0x10bdc4c: ldr x8, [x8, #0xd8]
// 0x10bdc50: ldr x20, [x19, #0x20]
// 0x10bdc54: ldr x0, [x8]
// 0x10bdc58: ldr w8, [x0, #0xe0]
// 0x10bdc5c: cbnz w8, #0x10bdc64
// 0x10bdc60: bl #0xf7da5c
// 0x10bdc64: mov x0, x20
// 0x10bdc68: mov x1, xzr
// 0x10bdc6c: bl #0x1b98274
// 0x10bdc70: tbz w0, #0, #0x10bdcb4
// 0x10bdc74: ldr x0, [x19, #0x20]
// 0x10bdc78: cbz x0, #0x10bde64
// 0x10bdc7c: adrp x8, #0x1e8e000
// 0x10bdc80: ldr x8, [x8, #0x808]
// 0x10bdc84: mov x2, xzr
// 0x10bdc88: ldr x1, [x8]
// 0x10bdc8c: bl #0x1b67884
// 0x10bdc90: ldrb w8, [x19, #0x36c]
// 0x10bdc94: cbz w8, #0x10bdcb4
// 0x10bdc98: ldr x0, [x19, #0x30]
// 0x10bdc9c: cbz x0, #0x10bde64
// 0x10bdca0: adrp x8, #0x1e8e000
// 0x10bdca4: ldr x8, [x8, #0x7f0]
// 0x10bdca8: mov x2, xzr
// 0x10bdcac: ldr x1, [x8]
// 0x10bdcb0: bl #0x1b67884
// 0x10bdcb4: mov x0, xzr
// 0x10bdcb8: bl #0x1b9ad30
// 0x10bdcbc: ldr x8, [x19, #0x90]
// 0x10bdcc0: str s0, [x19, #0x3e8]
// 0x10bdcc4: cbz x8, #0x10bde64
// 0x10bdcc8: strb wzr, [x8, #0x129]
// 0x10bdccc: ldr x0, [x19, #0x690]
// 0x10bdcd0: cbz x0, #0x10bde64
// 0x10bdcd4: fmov s0, #1.00000000
// 0x10bdcd8: mov x1, xzr
// 0x10bdcdc: bl #0x1b6a478
// 0x10bdce0: ldr x20, [x19, #0x690]
// 0x10bdce4: mov x0, xzr
// 0x10bdce8: bl #0x1b9ae58
// 0x10bdcec: mov x0, xzr
// 0x10bdcf0: mov v8.16b, v0.16b
// 0x10bdcf4: bl #0x1b9ae58
// 0x10bdcf8: adrp x8, #0x832000
// 0x10bdcfc: mov v1.16b, v0.16b
// 0x10bdd00: ldr s0, [x8, #0x400]
// 0x10bdd04: mov x0, xzr
// 0x10bdd08: fmul s0, s8, s0
// 0x10bdd0c: bl #0x1b9012c
// 0x10bdd10: cbz x20, #0x10bde64
// 0x10bdd14: mov x0, x20
// 0x10bdd18: mov x1, xzr
// 0x10bdd1c: bl #0x1b6a500
// 0x10bdd20: ldr x20, [x19, #0x690]
// 0x10bdd24: cbz x20, #0x10bde64
// 0x10bdd28: mov x0, x20
// 0x10bdd2c: mov x1, xzr
// 0x10bdd30: bl #0x1b6a54c
// 0x10bdd34: ldr x8, [x19, #0x690]
// 0x10bdd38: cbz x8, #0x10bde64
// 0x10bdd3c: mov x21, x0
// 0x10bdd40: mov x0, x8
// 0x10bdd44: mov x1, xzr
// 0x10bdd48: bl #0x1b6a43c
// 0x10bdd4c: fmov s1, #1.00000000
// 0x10bdd50: fdiv s0, s1, s0
// 0x10bdd54: mov x0, x20
// 0x10bdd58: mov x1, x21
// 0x10bdd5c: mov x2, xzr
// 0x10bdd60: bl #0x1b6a66c
// 0x10bdd64: mov x0, xzr
// 0x10bdd68: bl #0x1b9ad30
// 0x10bdd6c: mov w21, wzr
// 0x10bdd70: str s0, [x19, #0x3c8]
// 0x10bdd74: b #0x10bda60
// 0x10bdd78: ldr x8, [x19, #0x90]
// 0x10bdd7c: cbz x8, #0x10bde64
// 0x10bdd80: mov w21, wzr
// 0x10bdd84: strb wzr, [x8, #0x129]
// 0x10bdd88: str wzr, [x19, #0x3b8]
// 0x10bdd8c: b #0x10bda60
// 0x10bdd90: ldr w8, [x19, #0x124]
// 0x10bdd94: ldr x0, [x19, #0x118]
// 0x10bdd98: sub w8, w8, #5
// 0x10bdd9c: cmp w8, #2
// 0x10bdda0: b.hi #0x10bddb4
// 0x10bdda4: cbz x0, #0x10bde64
// 0x10bdda8: adrp x8, #0x1e8e000
// 0x10bddac: ldr x8, [x8, #0x828]
// 0x10bddb0: b #0x10bddc0
// 0x10bddb4: cbz x0, #0x10bde64
// 0x10bddb8: adrp x8, #0x1e8e000
// 0x10bddbc: ldr x8, [x8, #0x820]
// 0x10bddc0: ldr x1, [x8]
// 0x10bddc4: mov x2, xzr
// 0x10bddc8: bl #0x1b67884
// 0x10bddcc: ldr x0, [x19, #0x110]
// 0x10bddd0: cbz x0, #0x10bde64
// 0x10bddd4: adrp x8, #0x1e8e000
// 0x10bddd8: ldr x8, [x8, #0x498]
// 0x10bdddc: mov x2, xzr
// 0x10bdde0: ldr x1, [x8]
// 0x10bdde4: bl #0x1b67884
// 0x10bdde8: ldr x8, [x19, #0x90]
// 0x10bddec: cbz x8, #0x10bde64
// 0x10bddf0: mov w21, #1
// 0x10bddf4: mov x0, xzr
// 0x10bddf8: strb w21, [x8, #0x129]
// 0x10bddfc: bl #0x1b9ad30
// 0x10bde00: ldr w8, [x19, #0x134]
// 0x10bde04: ldr w9, [x19, #0x130]
// 0x10bde08: str s0, [x19, #0x3c0]
// 0x10bde0c: strb wzr, [x19, #0x1e8]
// 0x10bde10: str wzr, [x19, #0x1ec]
// 0x10bde14: cmp w8, w9
// 0x10bde18: b.eq #0x10bde28
// 0x10bde1c: ldr w8, [x19, #0x3b8]
// 0x10bde20: cmp w8, #1
// 0x10bde24: b.lt #0x10bda80
// 0x10bde28: adrp x8, #0x1e8d000
// 0x10bde2c: ldr s8, [x19, #0x3bc]
// 0x10bde30: ldr x8, [x8, #0x3e8]
// 0x10bde34: ldr x0, [x8]
// 0x10bde38: bl #0xf7db70
// 0x10bde3c: mov v0.16b, v8.16b
// 0x10bde40: mov x1, xzr
// 0x10bde44: mov x19, x0
// 0x10bde48: bl #0x1b99b00
// 0x10bde4c: str x19, [x20, #0x18]!
// 0x10bde50: mov x0, x20
// 0x10bde54: mov x1, x19
// 0x10bde58: bl #0xf7d8d0
// 0x10bde5c: stur w21, [x20, #-8]
// 0x10bde60: b #0x10bda60
// 0x10bde64: bl #0xf7db74
```


## `WeaponBehavior.<Reload>d__361.get_Current` — RVA `0xcbde68`

- Decompiled symbol: `WeaponBehavior_Reload_d__361_get_Current`
- Metadata signature: `private object System.Collections.Generic.IEnumerator<System.Object>.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long WeaponBehavior_Reload_d__361_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```


## `WeaponBehavior.<Reload>d__361.Reset` — RVA `0xcbde70`

- Decompiled symbol: `WeaponBehavior_Reload_d__361_Reset`
- Metadata signature: `private void System.Collections.IEnumerator.Reset() { }`
- Native interval: `56` bytes
- Result: `pseudocode`

```c
extern long long g_1ef0bd8;
extern long long g_1f05380;

void WeaponBehavior_Reload_d__361_Reset(void)
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
    sub_f7da4c(v4, sub_f7d940(&g_1f05380));
}
```


## `WeaponBehavior.<Reload>d__361.get_Current` — RVA `0xcbdea8`

- Decompiled symbol: `WeaponBehavior_Reload_d__361_get_Current`
- Metadata signature: `private object System.Collections.IEnumerator.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long WeaponBehavior_Reload_d__361_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```


## `WeaponBehavior.<SpawnShell>d__359.ctor` — RVA `0xcbdeb0`

- Decompiled symbol: `WeaponBehavior_SpawnShell_d__359_ctor`
- Metadata signature: `public void .ctor(int <>1__state) { }`
- Native interval: `40` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

void WeaponBehavior_SpawnShell_d__359_ctor(struct_0 *ptr, unsigned int a1)
{
    Object__ctor();
    ptr->field_10 = a1;
    return;
}
```


## `WeaponBehavior.<SpawnShell>d__359.Dispose` — RVA `0xcbded8`

- Decompiled symbol: `WeaponBehavior_SpawnShell_d__359_Dispose`
- Metadata signature: `private void System.IDisposable.Dispose() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long WeaponBehavior_SpawnShell_d__359_Dispose(void)
{
    unsigned long v0;  // x0

    return v0;
}
```


## `WeaponBehavior.<SpawnShell>d__359.MoveNext` — RVA `0xcbdedc`

- Decompiled symbol: `WeaponBehavior_SpawnShell_d__359_MoveNext`
- Metadata signature: `private bool MoveNext() { }`
- Native interval: `1640` bytes
- Result: `pseudocode`

```c
typedef struct struct_9 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[4];
    long long field_18;
    struct struct_8 *field_20;
} struct_9;

typedef struct struct_8 {
    char padding_0[64];
    long long field_40;
    char padding_48[72];
    struct struct_3 *field_90;
    struct struct_4 *field_98;
    char padding_a0[8];
    struct struct_5 *field_a8;
    char padding_b0[8];
    struct struct_6 *field_b8;
    struct struct_7 *field_c0;
    char padding_c8[993];
    char field_4a9;
    char padding_4aa[354];
    unsigned int field_60c;
    long long field_610;
    char padding_618[8];
    unsigned int field_620;
    unsigned int field_624;
    unsigned int field_628;
    char padding_62c[4];
    unsigned long long field_630;
    unsigned long long field_638;
    unsigned long long field_640;
    unsigned long long field_648;
    unsigned int field_650;
    char padding_654[8];
    unsigned int field_65c;
    char padding_660[4];
    unsigned int field_664;
    unsigned int field_668;
    unsigned int field_66c;
} struct_8;

typedef struct struct_6 {
    char padding_0[262];
    char field_106;
} struct_6;

typedef struct struct_3 {
    char padding_0[297];
    char field_129;
} struct_3;

typedef struct struct_4 {
    char padding_0[720];
    char field_2d0;
} struct_4;

typedef struct struct_7 {
    char padding_0[106];
    char field_6a;
} struct_7;

typedef struct struct_17 {
    char padding_0[32];
    struct struct_10 *field_20;
    char padding_28[16];
    struct struct_16 *field_38;
    long long field_40;
    long long field_48;
    long long field_50;
    long long field_58;
    char padding_60[100];
    unsigned int field_c4;
    char field_c8;
} struct_17;

typedef struct struct_5 {
    char padding_0[168];
    char field_a8;
} struct_5;

typedef struct struct_10 {
    char padding_0[720];
    char field_2d0;
} struct_10;

typedef struct struct_16 {
    char padding_0[64];
    unsigned long long field_40;
    char padding_48[72];
    struct struct_11 *field_90;
    struct struct_12 *field_98;
    char padding_a0[8];
    struct struct_13 *field_a8;
    char padding_b0[8];
    struct struct_14 *field_b8;
    struct struct_15 *field_c0;
    char padding_c8[993];
    char field_4a9;
    char padding_4aa[354];
    unsigned int field_60c;
    unsigned long long field_610;
    char padding_618[8];
    unsigned int field_620;
    unsigned int field_624;
    unsigned int field_628;
    char padding_62c[4];
    unsigned long long field_630;
    unsigned long long field_638;
    unsigned long long field_640;
    unsigned long long field_648;
    unsigned int field_650;
    char padding_654[8];
    unsigned int field_65c;
    char padding_660[4];
    unsigned int field_664;
    unsigned int field_668;
    unsigned int field_66c;
} struct_16;

typedef struct struct_11 {
    char padding_0[297];
    char field_129;
} struct_11;

typedef struct struct_12 {
    char padding_0[720];
    char field_2d0;
} struct_12;

typedef struct struct_13 {
    char padding_0[168];
    char field_a8;
} struct_13;

typedef struct struct_14 {
    char padding_0[262];
    char field_106;
} struct_14;

typedef struct struct_15 {
    char padding_0[106];
    char field_6a;
} struct_15;

typedef struct struct_2 {
    char padding_0[224];
    unsigned int field_e0;
} struct_2;

extern struct_2 *g_1ef0c58;
extern long long g_1ef22e8;
extern long long g_1ef2440;
extern long long g_1efeca8;
extern long long g_1efecc8;
extern char g_1fab2c9;
extern char g_1fab4f3;

unsigned int WeaponBehavior_SpawnShell_d__359_MoveNext(struct_9 *p)
{
    struct_8 *ptr;  // x19
    unsigned int v1;  // s8
    unsigned int v10;  // s8
    unsigned long v11;  // x0
    unsigned long v12;  // 4133
    struct_17 *v13;  // x0
    struct_17 *ptr9;  // x20
    long long v15;  // x1
    struct_17 *ptr3;  // x0
    long long v17;  // x1
    struct_17 *ptr4;  // x0
    struct_17 *ptr5;  // x0
    unsigned long v2;  // 4129
    long long v20;  // x0
    struct_17 *ptr6;  // x22
    struct_17 *addr;  // x22
    struct_4 *v23;  // x1
    struct_17 *ptr7;  // x0
    long long v25;  // x0
    struct_17 *ptr8;  // x23
    struct_17 *ptr10;  // x23
    unsigned long v28;  // x0
    unsigned long v29;  // x23
    long long v3;  // x19
    long long v30;  // x0
    long long v31;  // x21
    long long v32;  // x21
    unsigned int v33;  // s10
    struct_6 *v34;  // x8
    unsigned int v35;  // s1
    unsigned int v36;  // s5
    unsigned int v37;  // s4
    unsigned int v38;  // s4
    long long v39;  // x21
    struct_9 *ptr11;  // x20
    unsigned long v40;  // 4176
    struct_9 *ptr12;  // x20
    unsigned long v6;  // 4102
    unsigned long v7;  // x1
    unsigned long v8;  // x21
    long long v9;  // x1

    if (!(g_1fab4f3 & 1))
    {
        sub_f7d92c("s.");
        sub_f7d92c(&g_1efeca8);
        sub_f7d92c(&g_1efecc8);
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c(&g_1ef2440);
        g_1fab4f3 = 1;
    }
    ptr = p->field_20;
    if (2 > p->field_10)
    {
        p->field_10 = 4294967295;
        if (ptr)
        {
            if (ptr->field_4a9)
            {
LABEL_10bdf70:
                v1 = ptr->field_65c;
                v2 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v1, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v1, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v1, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v1, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v1, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v1, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                if (!((char)v2))
                {
                    v3 = sub_f7db70(g_1ef2440);
                    WaitForSeconds__ctor(v3, 0);
                    p->field_18 = v3;
                    ptr11 = &p->field_18;
                    sub_f7d8d0(ptr11, v3);
                    *((unsigned int *)&ptr11->padding_0[8]) = 2;
                    return 1;
                }
            }
            else if (ptr->field_b8)
            {
                if (!ptr->field_b8->field_106)
                    goto LABEL_10bdf70;
                if (ptr->field_90)
                {
                    if (!ptr->field_90->field_129)
                    {
                        p->field_18 = 0;
                        ptr12 = &p->field_18;
                        sub_f7d8d0(ptr12, 0);
                        *((unsigned int *)&ptr12->padding_0[8]) = 1;
                        return 1;
                    }
                    goto LABEL_10bdf70;
                }
            }
        }
    }
    else
    {
        v6 = arm64g_calculate_condition(19, (unsigned long long)p->field_10, 2, 0);
        if ((char)v6)
            return 0;
        p->field_10 = 4294967295;
        if (ptr && ptr->field_b8)
        {
            if (ptr->field_b8->field_106)
            {
                v7 = ptr->field_640;
                goto LABEL_10be070;
            }
            if (!g_1ef0c58->field_e0)
                sub_f7da5c(g_1ef0c58);
            if (!((char)Object__op_Implicit(ptr->field_638, 0) & 1))
            {
LABEL_10be06c:
                v7 = ptr->field_630;
                goto LABEL_10be070;
            }
            else if (ptr->field_98)
            {
                if (!ptr->field_98->field_2d0)
                    goto LABEL_10be06c;
                if (ptr->field_c0)
                {
                    if (ptr->field_c0->field_6a)
                        goto LABEL_10be06c;
                    v7 = ptr->field_638;
LABEL_10be070:
                    ptr->field_648 = v7;
                    sub_f7d8d0(&ptr->field_648);
                    if (ptr->field_648 && (Transform__get_position(ptr->field_648, 0), ptr->field_648 && Component__get_transform(ptr->field_648, 0) && (Transform__get_rotation(), g_1eeea08->field_b8->field_0)))
                    {
                        v8 = &ptr->field_610;
                        v9 = AzuObjectPool__SpawnPooledObj(g_1eeea08->field_b8->field_0, ptr->field_60c, 0);
                        ptr->field_610 = v9;
                        sub_f7d8d0(v8, v9);
                        if (ptr->field_b8)
                        {
                            if (ptr->field_b8->field_106)
                            {
                                if (ptr->field_610)
                                {
                                    v10 = ptr->field_650;
                                    v11 = GameObject__get_transform(ptr->field_610, 0);
                                    v12 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v10, 0x40400000)) >> 5 & 3 | (unsigned long long)(CmpF(v10, 0x40400000) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v10, 0x40400000)) >> 5 & 3 | (unsigned long long)(CmpF(v10, 0x40400000) & 1)) & ((unsigned long long)(char)(CmpF(v10, 0x40400000)) >> 5 & 3 | (unsigned long long)(CmpF(v10, 0x40400000) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                                    if (!((char)v12))
                                    {
                                        if (v11)
                                            goto LABEL_10be198;
                                    }
                                    else
                                    {
                                        if (v11)
                                        {
LABEL_10be198:
                                            Transform__set_localScale();
                                            if (*((long long *)v8))
                                            {
                                                v13 = sub_1249224(*((long long *)v8), g_1efecc8);
                                                if (v13)
                                                {
                                                    ptr9 = v13;
                                                    MonoBehaviour__StopAllCoroutines();
                                                    v15 = ptr->field_40;
                                                    ptr3 = ptr9;
                                                    ptr3->field_50 = v15;
                                                    sub_f7d8d0(&ptr3->field_50, v15);
                                                    if (ptr->field_a8)
                                                    {
                                                        ptr9->field_c8 = ptr->field_a8->field_a8;
                                                        if (ptr->field_40)
                                                        {
                                                            v17 = sub_1249224(ptr->field_40, g_1efeca8);
                                                            ptr4 = ptr9;
                                                            ptr4->field_48 = v17;
                                                            sub_f7d8d0(&ptr4->field_48, v17);
                                                            ptr5 = ptr9;
                                                            ptr5->field_38 = ptr;
                                                            sub_f7d8d0(&ptr5->field_38, ptr);
                                                            if (Component__get_gameObject(ptr9, 0))
                                                            {
                                                                v20 = sub_1249224();
                                                                ptr6 = ptr9;
                                                                ptr6->field_40 = v20;
                                                                addr = &ptr6->field_40;
                                                                sub_f7d8d0(addr, v20);
                                                                v23 = ptr->field_98;
                                                                ptr7 = ptr9;
                                                                ptr7->field_20 = v23;
                                                                sub_f7d8d0(&ptr7->field_20, v23);
                                                                if (Component__get_transform(ptr, 0))
                                                                {
                                                                    v25 = Component__get_gameObject();
                                                                    ptr8 = ptr9;
                                                                    ptr8->field_58 = v25;
                                                                    ptr10 = &ptr8->field_58;
                                                                    sub_f7d8d0(ptr10, v25);
                                                                    *((unsigned int *)&ptr10->padding_60[12]) = ptr->field_60c;
                                                                    if (ptr->field_610)
                                                                    {
                                                                        GameObject__SetActive(ptr->field_610, 0, 0);
                                                                        if (*((long long *)v8) && GameObject__get_transform(*((long long *)v8), 0))
                                                                        {
                                                                            Transform__set_parent();
                                                                            if (*((long long *)v8))
                                                                            {
                                                                                v28 = GameObject__get_transform(*((long long *)v8), 0);
                                                                                if (ptr->field_630)
                                                                                {
                                                                                    v29 = v28;
                                                                                    if (Component__get_transform(ptr->field_630, 0))
                                                                                    {
                                                                                        v30 = Transform__get_parent();
                                                                                        if (v29)
                                                                                        {
                                                                                            Transform__set_parent(v29, v30, 0);
                                                                                            if (*((long long *)v8))
                                                                                            {
                                                                                                GameObject__SetActive(*((long long *)v8), 1, 0);
                                                                                                v31 = *((long long *)&addr->padding_0[0]);
                                                                                                if (!g_1fab2c9)
                                                                                                {
                                                                                                    sub_f7d92c(&g_1ef22e8);
                                                                                                    g_1fab2c9 = 1;
                                                                                                }
                                                                                                if (v31)
                                                                                                {
                                                                                                    Rigidbody__set_velocity(v31, 0);
                                                                                                    v32 = *((long long *)&addr->padding_0[0]);
                                                                                                    if (!g_1fab2c9)
                                                                                                    {
                                                                                                        sub_f7d92c(&g_1ef22e8);
                                                                                                        g_1fab2c9 = 1;
                                                                                                    }
                                                                                                    if (v32)
                                                                                                    {
                                                                                                        Rigidbody__set_angularVelocity(v32, 0);
                                                                                                        if (*((long long *)&addr->padding_0[0]))
                                                                                                        {
                                                                                                            Rigidbody__set_maxAngularVelocity(*((long long *)&addr->padding_0[0]), 0);
                                                                                                            v33 = ptr->field_668;
                                                                                                            Random__get_value(0);
                                                                                                            Random__get_value(0);
                                                                                                            Random__get_value(0);
                                                                                                            v34 = ptr->field_b8;
                                                                                                            v35 = ptr->field_668 * 1053609165;
                                                                                                            v36 = ptr->field_66c * 1045220557;
                                                                                                            v37 = ptr->field_66c * 1053609165;
                                                                                                            ptr->field_624 = ptr->field_664 * 1214289647658178970;
                                                                                                            ptr->field_620 = v33 * 1060320051 + v35 * 0x447a0000;
                                                                                                            ptr->field_628 = v37 + v36 * 0x447a0000;
                                                                                                            if (v34)
                                                                                                            {
                                                                                                                if (!v34->field_106)
                                                                                                                {
                                                                                                                    v39 = *((long long *)&addr->padding_0[0]);
                                                                                                                    if (Component__get_transform(ptr, 0))
                                                                                                                    {
                                                                                                                        Transform__TransformDirection();
                                                                                                                        if (*((long long *)&addr->padding_0[0]))
                                                                                                                        {
                                                                                                                            Rigidbody__AddForce(v39, 1, 0);
                                                                                                                            ShellEjection__InitializeShell(ptr9); /* do not return */
                                                                                                                        }
                                                                                                                    }
                                                                                                                }
                                                                                                                else if (ptr->field_648)
                                                                                                                {
                                                                                                                    Transform__TransformDirection(ptr->field_648, 0);
                                                                                                                    v38 = ptr->field_650;
                                                                                                                    v39 = *((long long *)&addr->padding_0[0]);
                                                                                                                    v40 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v38, 0x40400000)) >> 5 & 3 | (unsigned long long)(CmpF(v38, 0x40400000) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v38, 0x40400000)) >> 5 & 3 | (unsigned long long)(CmpF(v38, 0x40400000) & 1)) & ((unsigned long long)(char)(CmpF(v38, 0x40400000)) >> 5 & 3 | (unsigned long long)(CmpF(v38, 0x40400000) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                                                                                                                    if (!((char)v40))
                                                                                                                    {
                                                                                                                        if (v39)
                                                                                                                        {
                                                                                                                            Rigidbody__AddForce(v39, 1, 0);
                                                                                                                            ShellEjection__InitializeShell(ptr9); /* do not return */
                                                                                                                        }
                                                                                                                    }
                                                                                                                    else
                                                                                                                    {
                                                                                                                        if (v39)
                                                                                                                        {
                                                                                                                            Rigidbody__AddForce(v39, 1, 0);
                                                                                                                            ShellEjection__InitializeShell(ptr9); /* do not return */
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
                            else
                            {
                                if (*((long long *)v8) && GameObject__get_transform(*((long long *)v8), 0))
                                    goto LABEL_10be198;
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


## `WeaponBehavior.<SpawnShell>d__359.get_Current` — RVA `0xcbe544`

- Decompiled symbol: `WeaponBehavior_SpawnShell_d__359_get_Current`
- Metadata signature: `private object System.Collections.Generic.IEnumerator<System.Object>.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long WeaponBehavior_SpawnShell_d__359_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```


## `WeaponBehavior.<SpawnShell>d__359.Reset` — RVA `0xcbe54c`

- Decompiled symbol: `WeaponBehavior_SpawnShell_d__359_Reset`
- Metadata signature: `private void System.Collections.IEnumerator.Reset() { }`
- Native interval: `56` bytes
- Result: `pseudocode`

```c
extern long long g_1ef0bd8;
extern long long g_1f05388;

void WeaponBehavior_SpawnShell_d__359_Reset(void)
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
    sub_f7da4c(v4, sub_f7d940(&g_1f05388));
}
```


## `WeaponBehavior.<SpawnShell>d__359.get_Current` — RVA `0xcbe584`

- Decompiled symbol: `WeaponBehavior_SpawnShell_d__359_get_Current`
- Metadata signature: `private object System.Collections.IEnumerator.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long WeaponBehavior_SpawnShell_d__359_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```
