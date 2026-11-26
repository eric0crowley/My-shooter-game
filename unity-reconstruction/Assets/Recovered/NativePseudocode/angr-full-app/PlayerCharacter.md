# Native pseudocode: PlayerCharacter

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `PlayerCharacter.Start` — RVA `0xca7780`

- Decompiled symbol: `PlayerCharacter_Start`
- Metadata signature: `private void Start() { }`
- Native interval: `3720` bytes
- Result: `pseudocode`
- Heuristic layout hint: `PlayerCharacter_Recovered` matched 27 offsets against `PlayerCharacter` metadata (confidence 1.00).

```c
typedef struct struct_26 {
    char padding_0[32];
    long long field_20;
    long long field_28;
    long long field_30;
    long long field_38;
    char padding_40[8];
    long long field_48;
    long long field_50;
    long long field_58;
    long long field_60;
    struct struct_25 *field_68;
    struct struct_27 *field_70;
    long long field_78;
    struct struct_29 *field_80;
    struct struct_30 *field_88;
    char padding_90[8];
    struct struct_31 *field_98;
    long long field_a0;
    long long field_a8;
    long long field_b0;
    long long field_b8;
    long long field_c0;
    long long field_c8;
    long long field_d0;
    char padding_d8[8];
    long long field_e0;
    long long field_e8;
    unsigned int field_f0;
    char padding_f4[4];
    struct struct_32 *field_f8;
    char padding_100[510];
    char field_2fe;
    char padding_2ff[9];
    long long field_308;
} struct_26;

typedef struct struct_3 {
    char padding_0[32];
    struct struct_2 *field_20;
} struct_3;

typedef struct struct_8 {
    char padding_0[40];
    unsigned long long field_28;
    unsigned long long field_30;
    char padding_38[104];
    unsigned long long field_a0;
    struct PlayerCharacter_Recovered *field_a8;
    char padding_b0[86];
    char field_106;
} struct_8;

typedef struct struct_14 {
    char padding_0[104];
    struct struct_13 *field_68;
} struct_14;

typedef struct struct_19 {
    char padding_0[168];
    unsigned long long field_a8;
    struct struct_18 *field_b0;
} struct_19;

typedef struct struct_24 {
    char padding_0[80];
    unsigned long long field_50;
} struct_24;

typedef struct struct_54 {
    char padding_0[232];
    unsigned long long field_e8;
} struct_54;

typedef struct struct_35 {
    struct struct_34 *field_0;
    char padding_8[24];
    long long field_20;
} struct_35;

typedef struct struct_55 {
    char padding_0[24];
    unsigned int field_18;
} struct_55;

typedef struct struct_31 {
    char padding_0[232];
    unsigned long long field_e8;
} struct_31;

typedef struct struct_40 {
    char padding_0[32];
    long long field_20;
} struct_40;

typedef struct struct_39 {
    char padding_0[32];
    long long field_20;
    long long field_28;
    long long field_30;
    long long field_38;
    char padding_40[808];
    unsigned int field_368;
    char field_36c;
    char padding_36d[275];
    unsigned long long field_480;
    char padding_488[24];
    unsigned long long field_4a0;
    char padding_4a8[408];
    unsigned long long field_640;
} struct_39;

typedef struct struct_41 {
    char padding_0[16];
    long long field_10;
} struct_41;

typedef struct struct_36 {
    char padding_0[48];
    unsigned long long field_30;
} struct_36;

typedef struct struct_37 {
    char padding_0[40];
    unsigned long long field_28;
} struct_37;

typedef struct struct_38 {
    char padding_0[56];
    unsigned long long field_38;
} struct_38;

typedef struct struct_42 {
    char padding_0[16];
    long long field_10;
} struct_42;

typedef struct struct_43 {
    char padding_0[16];
    long long field_10;
} struct_43;

typedef struct struct_44 {
    char padding_0[16];
    long long field_10;
} struct_44;

typedef struct struct_45 {
    char padding_0[16];
    long long field_10;
} struct_45;

typedef struct struct_46 {
    char padding_0[24];
    long long field_18;
} struct_46;

typedef struct struct_47 {
    char padding_0[24];
    long long field_18;
} struct_47;

typedef struct struct_48 {
    char padding_0[24];
    long long field_18;
} struct_48;

typedef struct struct_49 {
    char padding_0[24];
    long long field_18;
} struct_49;

typedef struct struct_50 {
    char padding_0[24];
    long long field_18;
} struct_50;

typedef struct struct_51 {
    char padding_0[32];
    long long field_20;
} struct_51;

typedef struct struct_52 {
    char padding_0[32];
    long long field_20;
} struct_52;

typedef struct struct_53 {
    char padding_0[32];
    long long field_20;
} struct_53;

typedef struct struct_25 {
    char padding_0[168];
    char field_a8;
    char padding_a9[7];
    struct struct_26 *field_b0;
} struct_25;

typedef struct struct_27 {
    char padding_0[104];
    struct struct_28 *field_68;
} struct_27;

typedef struct struct_29 {
    char padding_0[40];
    long long field_28;
    long long field_30;
    char padding_38[104];
    char field_a0;
    char padding_a1[7];
    struct struct_26 *field_a8;
    char padding_b0[86];
    char field_106;
} struct_29;

typedef struct struct_30 {
    char padding_0[80];
    long long field_50;
} struct_30;

typedef struct struct_32 {
    char padding_0[32];
    struct struct_33 *field_20;
} struct_32;

typedef struct struct_2 {
    char padding_0[24];
    unsigned int field_18;
} struct_2;

typedef struct PlayerCharacter_Recovered {
    char padding_0[32];
    unsigned long long anim;
    unsigned long long headBone;
    unsigned long long chestBone;
    unsigned long long spineBone;
    char padding_40[8];
    unsigned long long playerObj;
    unsigned long long playerTransform;
    unsigned long long weaponObj;
    unsigned long long InputComponent;
    struct struct_4 *walkerComponent;
    struct struct_6 *FPSPlayerComponent;
    unsigned long long SmoothMouseLookComponent;
    struct struct_8 *CameraControlComponent;
    struct struct_9 *GunSwayComponent;
    char padding_90[8];
    struct struct_10 *PlayerWeaponsComponent;
    unsigned long long myTransform;
    unsigned long long AllSkinnedMeshes;
    unsigned long long AllMeshRenderers;
    unsigned long long fpBodyObj;
    unsigned long long fpBodyTransform;
    unsigned long long fpBodyAnim;
    unsigned long long fpBodySkinnedMesh;
    char padding_d8[8];
    unsigned long long fpBodyController;
    unsigned long long alternateBodyMaterial;
    unsigned int materialToReplace;
    char padding_f4[4];
    struct struct_11 *weaponModels;
    char padding_100[510];
    char tpModeState;
    char padding_2ff[9];
    unsigned long long mainCamTransform;
} PlayerCharacter_Recovered;

typedef struct struct_13 {
    char padding_0[232];
    unsigned long long field_e8;
} struct_13;

typedef struct struct_18 {
    char padding_0[32];
    unsigned long long field_20;
    unsigned long long field_28;
    unsigned long long field_30;
    unsigned long long field_38;
    char padding_40[8];
    unsigned long long field_48;
    unsigned long long field_50;
    unsigned long long field_58;
    unsigned long long field_60;
    struct struct_19 *field_68;
    struct struct_16 *field_70;
    unsigned long long field_78;
    struct struct_17 *field_80;
    struct struct_20 *field_88;
    char padding_90[8];
    struct struct_21 *field_98;
    unsigned long long field_a0;
    unsigned long long field_a8;
    unsigned long long field_b0;
    unsigned long long field_b8;
    unsigned long long field_c0;
    unsigned long long field_c8;
    unsigned long long field_d0;
    char padding_d8[8];
    unsigned long long field_e0;
    unsigned long long field_e8;
    unsigned int field_f0;
    char padding_f4[4];
    struct struct_22 *field_f8;
    char padding_100[510];
    char field_2fe;
    char padding_2ff[9];
    unsigned long long field_308;
} struct_18;

typedef struct struct_34 {
    char padding_0[64];
    long long field_40;
} struct_34;

typedef struct struct_28 {
    char padding_0[232];
    unsigned long long field_e8;
} struct_28;

typedef struct struct_33 {
    char padding_0[24];
    int field_18;
} struct_33;

typedef struct struct_4 {
    char padding_0[168];
    unsigned long long field_a8;
    struct PlayerCharacter_Recovered *field_b0;
} struct_4;

typedef struct struct_6 {
    char padding_0[104];
    struct struct_7 *field_68;
} struct_6;

typedef struct struct_9 {
    char padding_0[80];
    unsigned long long field_50;
} struct_9;

typedef struct struct_10 {
    char padding_0[232];
    unsigned long long field_e8;
} struct_10;

typedef struct struct_11 {
    char padding_0[32];
    struct struct_12 *field_20;
} struct_11;

typedef struct struct_16 {
    char padding_0[104];
    struct struct_15 *field_68;
} struct_16;

typedef struct struct_17 {
    char padding_0[40];
    unsigned long long field_28;
    unsigned long long field_30;
    char padding_38[104];
    unsigned long long field_a0;
    struct struct_18 *field_a8;
    char padding_b0[86];
    char field_106;
} struct_17;

typedef struct struct_20 {
    char padding_0[80];
    unsigned long long field_50;
} struct_20;

typedef struct struct_21 {
    char padding_0[232];
    unsigned long long field_e8;
} struct_21;

typedef struct struct_22 {
    char padding_0[32];
    struct struct_23 *field_20;
} struct_22;

typedef struct struct_7 {
    char padding_0[232];
    unsigned long long field_e8;
} struct_7;

typedef struct struct_12 {
    char padding_0[24];
    unsigned int field_18;
} struct_12;

typedef struct struct_15 {
    char padding_0[232];
    unsigned long long field_e8;
} struct_15;

typedef struct struct_23 {
    char padding_0[24];
    unsigned int field_18;
} struct_23;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

typedef struct struct_1 {
    char padding_0[224];
    unsigned int field_e0;
} struct_1;

extern struct_0 *g_1eef458;
extern struct_1 *g_1ef0c58;
extern long long g_1ef22e8;
extern long long g_1ef8178;
extern long long g_1ef8180;
extern long long g_1efcf38;
extern long long g_1efd118;
extern long long g_1efd148;
extern long long g_1efd1d8;
extern long long g_1efd1e0;
extern long long g_1efeb28;
extern long long g_1efebb8;
extern long long g_1efebc0;
extern long long g_1efebd8;
extern long long g_1efec08;
extern long long g_1efec88;
extern long long g_1efeca0;
extern long long g_1efecd8;
extern long long g_1efed18;
extern long long g_1efed58;
extern long long g_1efed68;
extern long long g_1efed70;
extern long long g_1f00260;
extern long long g_1f08048;
extern char g_1fab1e1;
extern char g_1fab2c9;
extern char g_1fab4c0;

long long PlayerCharacter_Start(struct_26 *p)
{
    long long v2;  // x0
    struct_26 *v3;  // x21
    struct_26 *ptr3;  // x23
    unsigned long v102;  // x1
    struct_3 *v103;  // x8
    struct_37 *ptr30;  // x0
    unsigned long v105;  // x1
    struct_3 *v106;  // x8
    struct_38 *ptr31;  // x0
    unsigned long v108;  // x1
    struct_3 *v109;  // x8
    struct_42 *v110;  // x0
    struct_3 *v111;  // x8
    struct_26 *v13;  // x23
    struct_43 *v112;  // x0
    long long v113;  // x1
    struct_39 *ptr4;  // x0
    struct_3 *v115;  // x8
    struct_44 *v116;  // x0
    long long v117;  // x1
    struct_39 *ptr5;  // x0
    struct_3 *v119;  // x8
    struct_45 *v120;  // x0
    struct_3 *v121;  // x8
    long long v14;  // x0
    struct_46 *v122;  // x0
    struct_3 *v123;  // x8
    struct_47 *v124;  // x0
    struct_3 *v125;  // x8
    struct_48 *v126;  // x0
    long long v127;  // x0
    struct_3 *v128;  // x8
    struct_49 *v129;  // x0
    struct_3 *v130;  // x8
    struct_50 *v131;  // x0
    struct_26 *ptr6;  // x23
    unsigned long v132;  // x0
    unsigned long v133;  // x23
    long long v134;  // x0
    struct_3 *v135;  // x8
    struct_51 *v136;  // x0
    struct_3 *v137;  // x8
    struct_52 *v138;  // x0
    struct_3 *v139;  // x8
    struct_53 *v140;  // x0
    unsigned long v141;  // x0
    struct_26 *v16;  // x23
    unsigned long v142;  // x23
    long long v143;  // x0
    unsigned long v145;  // x0
    long long v17;  // x1
    struct_26 *ptr7;  // x0
    struct_8 *v19;  // x0
    struct_26 *ptr8;  // x21
    struct_26 *v21;  // x21
    struct_3 *v4;  // x0
    unsigned long v22;  // x1
    struct_26 *ptr9;  // x21
    struct_26 *idx29;  // x21
    unsigned long v25;  // x1
    struct_26 *ptr10;  // x21
    struct_26 *v27;  // x21
    long long v28;  // x0
    struct_26 *ptr11;  // x21
    struct_26 *v30;  // x21
    long long v31;  // x0
    struct_26 *ptr12;  // x19
    struct_26 *ptr13;  // x21
    struct_26 *v33;  // x21
    struct_14 *v34;  // x0
    struct_26 *ptr14;  // x21
    struct_26 *v36;  // x21
    struct_19 *v37;  // x0
    struct_26 *ptr15;  // x23
    struct_26 *ptr27;  // x23
    struct_24 *v40;  // x0
    struct_26 *ptr16;  // x21
    struct_26 *ptr;  // x19
    struct_26 *ptr28;  // x21
    struct_24 *v43;  // x8
    long long v44;  // x0
    struct_26 *ptr17;  // x21
    struct_26 *v46;  // x21
    struct_54 *v47;  // x1
    struct_26 *ptr18;  // x21
    struct_26 *v49;  // x21
    long long v50;  // x0
    struct_26 *ptr19;  // x24
    long long v7;  // x0
    struct_26 *v52;  // x24
    long long v53;  // x1
    struct_26 *ptr20;  // x0
    long long v55;  // x0
    struct_26 *ptr21;  // x25
    struct_26 *ptr32;  // x25
    struct_8 *ptr33;  // x0
    struct_8 *ptr34;  // x25
    unsigned long v60;  // x0
    struct_19 *ptr35;  // x0
    struct_26 *ptr22;  // x20
    struct_19 *ptr36;  // x23
    unsigned long v63;  // x0
    unsigned long v64;  // x0
    long long v65;  // x0
    struct_26 *ptr23;  // x23
    struct_26 *v67;  // x23
    long long v69;  // x0
    struct_26 *ptr24;  // x24
    struct_26 *v71;  // x24
    struct_26 *ptr29;  // x20
    long long v73;  // x0
    struct_26 *ptr25;  // x23
    struct_26 *v75;  // x23
    long long v76;  // x0
    struct_26 *ptr26;  // x23
    struct_26 *v78;  // x23
    struct_35 *v79;  // x0
    unsigned long v80;  // x25
    unsigned long v81;  // x29
    long long v10;  // x0
    struct_35 *v82;  // x24
    long long v83;  // x0
    struct_35 *ptr37;  // x0
    unsigned long v85;  // x0
    unsigned long v86;  // x23
    long long v87;  // x0
    long long v88;  // x23
    long long v89;  // x23
    unsigned long v90;  // x0
    struct_3 *i;  // x8
    long long v11;  // x0
    unsigned int v92;  // w22
    unsigned long long v93;  // x8
    struct_40 *v94;  // x8
    struct_39 *ptr38;  // x0
    long long v96;  // x1
    struct_39 *addr;  // x23
    struct_3 *v98;  // x8
    struct_41 *v99;  // x0
    struct_3 *v100;  // x8
    struct_36 *ptr39;  // x0
    char *v0;  // [bp-0x60]
    char v1;  // [bp+0x0]

    v0 = &v1;
    if (!(g_1fab4c0 & 1))
    {
        sub_f7d92c(&g_1efd118);
        sub_f7d92c(&g_1efd148);
        sub_f7d92c(&g_1efcf38);
        sub_f7d92c(&g_1efd1d8);
        sub_f7d92c(&g_1efd1e0);
        sub_f7d92c(&g_1eef458);
        sub_f7d92c(&g_1efed58);
        sub_f7d92c(&g_1efed68);
        sub_f7d92c(&g_1efed70);
        sub_f7d92c(&g_1efeb28);
        sub_f7d92c(&g_1efebb8);
        sub_f7d92c(&g_1efebc0);
        sub_f7d92c(&g_1efebd8);
        sub_f7d92c(&g_1efec08);
        sub_f7d92c(&g_1efec88);
        sub_f7d92c(&g_1efeca0);
        sub_f7d92c(&g_1efecd8);
        sub_f7d92c(&g_1efed18);
        sub_f7d92c(&g_1ef8178);
        sub_f7d92c(&g_1ef8180);
        sub_f7d92c(&g_1f00260);
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c(&g_1f08048);
        g_1fab4c0 = 1;
    }
    if (Camera__get_main(0))
    {
        v2 = Component__get_transform();
        v3 = &p->field_308;
        p->field_308 = v2;
        sub_f7d8d0(v3, v2);
        v4 = sub_1231e2c(p, g_1efd148);
        ptr12 = p;
        ptr12->field_f8 = v4;
        ptr = &ptr12->field_f8;
        sub_f7d8d0(ptr, v4);
        if (!*((long long *)&ptr->padding_0[0]) || !Component__get_gameObject(*((long long *)&ptr->padding_0[0]), 0))
            goto LABEL_10a85c8;
        GameObject__SetActive();
        v7 = sub_1231e2c(p, g_1efd118);
        ptr22 = p;
        ptr22->field_20 = v7;
        ptr29 = &ptr22->field_20;
        sub_f7d8d0(ptr29, v7);
        if (!*((long long *)&ptr29->padding_0[0]))
        {
            v145 = sub_f7db74();
            return sub_f7db74();
        }
        v10 = Animator__GetBoneTransform(*((long long *)&ptr29->padding_0[0]), 10, 0);
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        if (!((char)Object__op_Implicit(v10, 0) & 1))
        {
            if (!g_1eef458->field_e0)
                sub_f7da5c(g_1eef458);
            Debug__Log(g_1f08048, 0);
LABEL_10a7a54:
            if (!*((long long *)&ptr29->padding_0[0]))
            {
                v145 = sub_f7db74();
                return sub_f7db74();
            }
            Animator__set_applyRootMotion(*((long long *)&ptr29->padding_0[0]), 0, 0);
            if (!*((long long *)&v3->padding_0[0]))
            {
                v145 = sub_f7db74();
                return sub_f7db74();
            }
            v19 = sub_1231bc8(*((long long *)&v3->padding_0[0]), g_1efcf38);
            ptr8 = p;
            ptr8->field_80 = v19;
            v21 = &ptr8->field_80;
            sub_f7d8d0(v21, v19);
            if (!*((long long *)&v21->padding_0[0]))
            {
                v145 = sub_f7db74();
                return sub_f7db74();
            }
            v22 = *((long long *)(*((long long *)&v21->padding_0[0]) + 40));
            ptr9 = p;
            ptr9->field_48 = v22;
            idx29 = &ptr9->field_48;
            sub_f7d8d0(idx29, v22);
            if (!idx29->field_38)
            {
                v145 = sub_f7db74();
                return sub_f7db74();
            }
            v25 = *((long long *)(idx29->field_38 + 48));
            ptr10 = p;
            ptr10->field_58 = v25;
            v27 = &ptr10->field_58;
            sub_f7d8d0(v27, v25);
            if (!*((long long *)&v27->padding_0[16]))
            {
                v145 = sub_f7db74();
                return sub_f7db74();
            }
            v28 = GameObject__get_transform(*((long long *)&v27->padding_0[16]), 0);
            ptr11 = p;
            ptr11->field_50 = v28;
            v30 = &ptr11->field_50;
            sub_f7d8d0(v30, v28);
            if (!*((long long *)&v30->padding_0[8]))
            {
                v145 = sub_f7db74();
                return sub_f7db74();
            }
            v31 = sub_1249224(*((long long *)&v30->padding_0[8]), g_1efec08);
            ptr13 = p;
            ptr13->field_60 = v31;
            v33 = &ptr13->field_60;
            sub_f7d8d0(v33, v31);
            if (!*((long long *)&v33->padding_0[24]))
            {
                v145 = sub_f7db74();
                return sub_f7db74();
            }
            v34 = sub_1249224(*((long long *)&v33->padding_0[24]), g_1efebb8);
            ptr14 = p;
            ptr14->field_70 = v34;
            v36 = &ptr14->field_70;
            sub_f7d8d0(v36, v34);
            if (!v36->field_28)
            {
                v145 = sub_f7db74();
                return sub_f7db74();
            }
            v37 = sub_1249224(v36->field_28, g_1efebc0);
            ptr15 = p;
            ptr15->field_68 = v37;
            ptr27 = &ptr15->field_68;
            sub_f7d8d0(ptr27, v37);
            if (!*((long long *)&ptr27->padding_0[16]))
            {
                v145 = sub_f7db74();
                return sub_f7db74();
            }
            v40 = sub_1249224(*((long long *)&ptr27->padding_0[16]), g_1efebd8);
            ptr16 = p;
            ptr16->field_88 = v40;
            ptr28 = &ptr16->field_88;
            sub_f7d8d0(ptr28, v40);
            v43 = *((long long *)&ptr28->padding_0[0]);
            if (!v43 || !v43->field_50)
                goto LABEL_10a85c8;
            v44 = sub_1249224(v43->field_50, g_1efecd8);
            ptr17 = p;
            ptr17->field_78 = v44;
            v46 = &ptr17->field_78;
            sub_f7d8d0(v46, v44);
            if (!*((long long *)&v46->padding_0[8]))
            {
                v145 = sub_f7db74();
                return sub_f7db74();
            }
            v47 = *((long long *)(*((long long *)&v46->padding_0[8]) + 104));
            ptr18 = p;
            ptr18->field_98 = v47;
            v49 = &ptr18->field_98;
            sub_f7d8d0(v49, v47);
            v50 = Component__get_transform(p, 0);
            ptr19 = p;
            ptr19->field_a0 = v50;
            v52 = &ptr19->field_a0;
            sub_f7d8d0(v52, v50);
            v53 = sub_123247c(p, 1, g_1efd1e0);
            ptr20 = p;
            ptr20->field_a8 = v53;
            sub_f7d8d0(&ptr20->field_a8, v53);
            v55 = sub_123247c(p, 1, g_1efd1d8);
            ptr21 = p;
            ptr21->field_b0 = v55;
            ptr32 = &ptr21->field_b0;
            sub_f7d8d0(ptr32, v55);
            ptr33 = ptr32->field_30;
            if (!ptr33)
            {
                v145 = sub_f7db74();
                return sub_f7db74();
            }
            p->field_2fe = ptr33->field_106;
            ptr33->field_a8 = p;
            sub_f7d8d0(&ptr33->field_a8, p);
            ptr34 = p->field_80;
            v60 = Component__get_gameObject(p, 0);
            if (!ptr34 || !((ptr34->field_a0 = (unsigned long long)v60, sub_f7d8d0(ptr34 + 160, v60), ptr35 = (struct_19 *)*((long long *)&ptr27->padding_0[0]), ptr35)))
                goto LABEL_10a85c8;
            ptr35->field_b0 = p;
            sub_f7d8d0(&ptr35->field_b0, p);
            ptr36 = p->field_68;
            v63 = Component__get_gameObject(p, 0);
            if (!ptr36 || !((ptr36->field_a8 = (unsigned long long)v63, sub_f7d8d0(ptr36 + 168, v63), *((long long *)&v52->padding_0[0]) && (v64 = (unsigned long)Component__get_gameObject(*((long long *)&v52->padding_0[0]), 0), *((long long *)&v52->padding_0[0]) && (Transform__get_position(*((long long *)&v52->padding_0[0]), 0), *((long long *)&v52->padding_0[0]))))))
                goto LABEL_10a85c8;
            Transform__get_rotation(*((long long *)&v52->padding_0[0]), 0);
            if (!g_1ef0c58->field_e0)
                sub_f7da5c(g_1ef0c58);
            v65 = sub_112a1ac(v64, g_1f00260);
            ptr23 = p;
            ptr23->field_b8 = v65;
            v67 = &ptr23->field_b8;
            sub_f7d8d0(v67, v65);
            if (!*((long long *)&v67->padding_0[0]))
            {
                v145 = sub_f7db74();
                return sub_f7db74();
            }
            Object__Destroy(sub_1249224(*((long long *)&v67->padding_0[0]), g_1efec88), 0);
            if (!*((long long *)&v67->padding_0[0]))
            {
                v145 = sub_f7db74();
                return sub_f7db74();
            }
            v69 = sub_1249224(*((long long *)&v67->padding_0[0]), g_1efeb28);
            ptr24 = p;
            ptr24->field_c8 = v69;
            v71 = &ptr24->field_c8;
            sub_f7d8d0(v71, v69);
            if (!*((long long *)&v71->padding_0[16]) || !sub_1249488(*((long long *)&v71->padding_0[16]), g_1efed70))
                goto LABEL_10a85c8;
            Object__Destroy(Component__get_gameObject(), 0);
            if (!*((long long *)&v67->padding_0[0]))
            {
                v145 = sub_f7db74();
                return sub_f7db74();
            }
            v73 = GameObject__get_transform(*((long long *)&v67->padding_0[0]), 0);
            ptr25 = p;
            ptr25->field_c0 = v73;
            v75 = &ptr25->field_c0;
            sub_f7d8d0(v75, v73);
            if (!*((long long *)&v75->padding_0[8]) || !((Animator__set_runtimeAnimatorController(*((long long *)&v75->padding_0[8]), p->field_e0, 0), p->field_b8)))
                goto LABEL_10a85c8;
            v76 = sub_1249488(p->field_b8, g_1efed68);
            ptr26 = p;
            ptr26->field_d0 = v76;
            v78 = &ptr26->field_d0;
            sub_f7d8d0(v78, v76);
            if (!*((long long *)&v78->padding_0[0]) || !((Renderer__set_shadowCastingMode(*((long long *)&v78->padding_0[0]), 0, 0), *((long long *)&v71->padding_0[0]))))
                goto LABEL_10a85c8;
            if (((char)Object__op_Implicit(Animator__GetBoneTransform(*((long long *)&v71->padding_0[0]), 10, 0), 0, 0) & 1))
            {
                if (*((long long *)&v71->padding_0[0]) && Animator__GetBoneTransform(*((long long *)&v71->padding_0[0]), 10, 0) && (Transform__set_localScale(), *((long long *)&v71->padding_0[0]) && (unsigned long long)Animator__GetBoneTransform(*((long long *)&v71->padding_0[0]), 14, 0) && (Transform__set_localScale(), *((long long *)&v71->padding_0[0]) && (unsigned long long)Animator__GetBoneTransform(*((long long *)&v71->padding_0[0]), 13, 0))))
                {
                    Transform__set_localScale();
                    goto LABEL_10a7f50;
                }
            }
            else
            {
                if (!g_1eef458->field_e0)
                    sub_f7da5c(g_1eef458);
                Debug__Log(g_1f08048, 0);
LABEL_10a7f50:
                if (!g_1ef0c58->field_e0)
                    sub_f7da5c(g_1ef0c58);
                if (((char)Object__op_Implicit(p->field_e8, 0) & 1))
                {
                    if (*((long long *)&v78->padding_0[0]) && Component__get_gameObject(*((long long *)&v78->padding_0[0]), 0) && sub_1249224() && (v79 = (struct_35 *)(unsigned long long)Renderer__get_materials(), v79))
                    {
                        v80 = p->field_e8;
                        v81 = p->field_f0;
                        v82 = v79;
                        if (v80 && (v83 = sub_f7da60(v80, v82->field_0->field_40), !v83))
                            goto LABEL_10a85fc;
                        if (*((int *)&v82->padding_8[16]) <= (unsigned int)v81)
                            goto LABEL_10a85f8;
                        ptr37 = &(&v82->field_0)[v81];
                        ptr37->field_20 = v80;
                        sub_f7d8d0(&ptr37->field_20, v80);
                        if (*((long long *)&v78->padding_0[0]) && Component__get_gameObject(*((long long *)&v78->padding_0[0]), 0) && sub_1249224())
                        {
                            Renderer__set_materials();
                            goto LABEL_10a8014;
                        }
                    }
                }
                else
                {
LABEL_10a8014:
                    if (!*((long long *)&ptr->padding_0[0]))
                    {
                        v145 = sub_f7db74();
                        return sub_f7db74();
                    }
                    v85 = Component__get_transform(*((long long *)&ptr->padding_0[0]), 0);
                    if (!*((long long *)&ptr29->padding_0[0]))
                    {
                        v145 = sub_f7db74();
                        return sub_f7db74();
                    }
                    v86 = v85;
                    v87 = Animator__GetBoneTransform(*((long long *)&ptr29->padding_0[0]), 18, 0);
                    if (!v86)
                    {
                        v145 = sub_f7db74();
                        return sub_f7db74();
                    }
                    Transform__set_parent(v86, v87, 0);
                    if (!*((long long *)&ptr->padding_0[0]))
                    {
                        v145 = sub_f7db74();
                        return sub_f7db74();
                    }
                    v88 = Component__get_transform(*((long long *)&ptr->padding_0[0]), 0);
                    if (!g_1fab2c9)
                    {
                        sub_f7d92c(&g_1ef22e8);
                        g_1fab2c9 = 1;
                    }
                    if (!v88)
                    {
                        v145 = sub_f7db74();
                        return sub_f7db74();
                    }
                    Transform__set_localPosition(v88, 0);
                    if (!*((long long *)&ptr->padding_0[0]))
                    {
                        v145 = sub_f7db74();
                        return sub_f7db74();
                    }
                    v89 = Component__get_transform(*((long long *)&ptr->padding_0[0]), 0);
                    if (!g_1fab1e1)
                    {
                        sub_f7d92c(&g_1ef22e8);
                        g_1fab1e1 = 1;
                    }
                    if (!v89)
                    {
                        v145 = sub_f7db74();
                        return sub_f7db74();
                    }
                    Transform__set_localScale(v89, 0);
                    if (!*((long long *)&ptr->padding_0[0]))
                    {
                        v145 = sub_f7db74();
                        return sub_f7db74();
                    }
                    if (!Component__get_transform(*((long long *)&ptr->padding_0[0]), 0))
                    {
                        v145 = sub_f7db74();
                        return sub_f7db74();
                    }
                    v90 = Transform__set_localEulerAngles();
                    i = p->field_f8;
                    if (!i)
                    {
                        v145 = sub_f7db74();
                        return sub_f7db74();
                    }
                    v92 = 0;
                    do
                    {
                        if (!i->field_20)
                        {
                            v145 = sub_f7db74();
                            return sub_f7db74();
                        }
                        if (i->field_20->field_18 <= v92)
                            return v90;
                        if (!*((long long *)&v49->padding_0[0]))
                        {
                            v145 = sub_f7db74();
                            return sub_f7db74();
                        }
                        v93 = *((long long *)(*((long long *)&v49->padding_0[0]) + 232));
                        if (!v93)
                        {
                            v145 = sub_f7db74();
                            return sub_f7db74();
                        }
                        if (*((int *)(v93 + 24)) <= v92)
                            goto LABEL_10a85f8;
                        else
                            goto LABEL_10a8180;
LABEL_10a8180:
                        v94 = v93 + v92 * 8;
                        if (!v94->field_20)
                        {
                            v145 = sub_f7db74();
                            return sub_f7db74();
                        }
                        ptr38 = sub_1249224(v94->field_20, g_1efed18);
                        if (!ptr38)
                        {
                            v145 = sub_f7db74();
                            return sub_f7db74();
                        }
                        v96 = *((long long *)&ptr29->padding_0[0]);
                        addr = ptr38;
                        ptr38->field_20 = v96;
                        sub_f7d8d0(&ptr38->field_20, v96);
                        v98 = *((long long *)&ptr->padding_0[0]);
                        if (!v98)
                        {
                            v145 = sub_f7db74();
                            return sub_f7db74();
                        }
                        if (!v98->field_20)
                        {
                            v145 = sub_f7db74();
                            return sub_f7db74();
                        }
                        v99 = sub_14a30c0(v98->field_20, v92, g_1ef8180);
                        if (!v99)
                        {
                            v145 = sub_f7db74();
                            return sub_f7db74();
                        }
                        if (!g_1ef0c58->field_e0)
                            sub_f7da5c(g_1ef0c58);
                        if (((char)Object__op_Implicit(v99->field_10, 0) & 1))
                        {
                            v100 = *((long long *)&ptr->padding_0[0]);
                            if (!v100)
                            {
                                v145 = sub_f7db74();
                                return sub_f7db74();
                            }
                            if (!v100->field_20)
                            {
                                v145 = sub_f7db74();
                                return sub_f7db74();
                            }
                            ptr39 = sub_14a30c0(v100->field_20, v92, g_1ef8180);
                            if (!ptr39)
                            {
                                v145 = sub_f7db74();
                                return sub_f7db74();
                            }
                            v102 = ptr39->field_30;
                            addr->field_4a0 = v102;
                            sub_f7d8d0(&addr->field_4a0, v102);
                            v103 = *((long long *)&ptr->padding_0[0]);
                            if (!v103 || !v103->field_20 || !((ptr30 = (struct_37 *)(unsigned long long)sub_14a30c0(v103->field_20, (unsigned long long)v92, g_1ef8180), ptr30 && (v105 = (unsigned long)ptr30->field_28, addr->field_480 = (unsigned long long)v105, sub_f7d8d0(addr + 1152, v105), v106 = (struct_3 *)*((long long *)&ptr->padding_0[0]), v106 && v106->field_20 && (ptr31 = (struct_38 *)(unsigned long long)sub_14a30c0(v106->field_20, (unsigned long long)v92, g_1ef8180), ptr31 && (v108 = (unsigned long)ptr31->field_38, addr->field_640 = (unsigned long long)v108, sub_f7d8d0(addr + 1600, v108), v109 = (struct_3 *)*((long long *)&ptr->padding_0[0]), v109 && v109->field_20 && (v110 = (struct_42 *)(unsigned long long)sub_14a30c0(v109->field_20, (unsigned long long)v92, g_1ef8180), v110 && v110->field_10)))))))
                                break;
                            GameObject__SetActive(v110->field_10, 1, 0);
                            if (addr->field_36c)
                            {
                                v111 = *((long long *)&ptr->padding_0[0]);
                                if (!v111)
                                {
                                    v145 = sub_f7db74();
                                    return sub_f7db74();
                                }
                                if (!v111->field_20)
                                {
                                    v145 = sub_f7db74();
                                    return sub_f7db74();
                                }
                                v112 = sub_14a30c0(v111->field_20, v92, g_1ef8180);
                                if (!v112)
                                {
                                    v145 = sub_f7db74();
                                    return sub_f7db74();
                                }
                                if (!v112->field_10)
                                    break;
                                v113 = sub_1249224(v112->field_10, g_1efeb28);
                                ptr4 = addr;
                                ptr4->field_30 = v113;
                                sub_f7d8d0(&ptr4->field_30, v113);
                            }
                            if (addr->field_368 == 3)
                            {
                                v115 = *((long long *)&ptr->padding_0[0]);
                                if (!v115)
                                {
                                    v145 = sub_f7db74();
                                    return sub_f7db74();
                                }
                                if (!v115->field_20)
                                {
                                    v145 = sub_f7db74();
                                    return sub_f7db74();
                                }
                                v116 = sub_14a30c0(v115->field_20, v92, g_1ef8180);
                                if (!v116)
                                {
                                    v145 = sub_f7db74();
                                    return sub_f7db74();
                                }
                                if (!v116->field_10)
                                    break;
                                v117 = sub_1249224(v116->field_10, g_1efeb28);
                                ptr5 = addr;
                                ptr5->field_28 = v117;
                                sub_f7d8d0(&ptr5->field_28, v117);
                            }
                            v119 = *((long long *)&ptr->padding_0[0]);
                            if (!v119)
                            {
                                v145 = sub_f7db74();
                                return sub_f7db74();
                            }
                            if (!v119->field_20)
                            {
                                v145 = sub_f7db74();
                                return sub_f7db74();
                            }
                            v120 = sub_14a30c0(v119->field_20, v92, g_1ef8180);
                            if (!v120)
                            {
                                v145 = sub_f7db74();
                                return sub_f7db74();
                            }
                            if (!v120->field_10)
                                break;
                            GameObject__SetActive(v120->field_10, 0, 0);
                        }
                        v121 = *((long long *)&ptr->padding_0[0]);
                        if (!v121)
                        {
                            v145 = sub_f7db74();
                            return sub_f7db74();
                        }
                        if (!v121->field_20)
                        {
                            v145 = sub_f7db74();
                            return sub_f7db74();
                        }
                        v122 = sub_14a30c0(v121->field_20, v92, g_1ef8180);
                        if (!v122)
                        {
                            v145 = sub_f7db74();
                            return sub_f7db74();
                        }
                        if (!g_1ef0c58->field_e0)
                            sub_f7da5c(g_1ef0c58);
                        if (((char)Object__op_Inequality(v122->field_18, 0, 0) & 1))
                        {
                            v123 = *((long long *)&ptr->padding_0[0]);
                            if (!v123)
                            {
                                v145 = sub_f7db74();
                                return sub_f7db74();
                            }
                            if (!v123->field_20)
                            {
                                v145 = sub_f7db74();
                                return sub_f7db74();
                            }
                            v124 = sub_14a30c0(v123->field_20, v92, g_1ef8180);
                            if (!v124)
                            {
                                v145 = sub_f7db74();
                                return sub_f7db74();
                            }
                            if (!v124->field_18)
                                break;
                            GameObject__SetActive(v124->field_18, 1, 0);
                            if (addr->field_368 == 6)
                            {
                                v125 = *((long long *)&ptr->padding_0[0]);
                                if (!v125)
                                {
                                    v145 = sub_f7db74();
                                    return sub_f7db74();
                                }
                                if (!v125->field_20)
                                {
                                    v145 = sub_f7db74();
                                    return sub_f7db74();
                                }
                                v126 = sub_14a30c0(v125->field_20, v92, g_1ef8180);
                                if (!v126)
                                {
                                    v145 = sub_f7db74();
                                    return sub_f7db74();
                                }
                                if (!v126->field_18)
                                    break;
                                v127 = sub_1249488(v126->field_18, g_1efed58);
                                addr->field_38 = v127;
                                sub_f7d8d0(&addr->field_38, v127);
                            }
                            v128 = *((long long *)&ptr->padding_0[0]);
                            if (!v128)
                            {
                                v145 = sub_f7db74();
                                return sub_f7db74();
                            }
                            if (!v128->field_20)
                            {
                                v145 = sub_f7db74();
                                return sub_f7db74();
                            }
                            v129 = sub_14a30c0(v128->field_20, v92, g_1ef8180);
                            if (!v129)
                            {
                                v145 = sub_f7db74();
                                return sub_f7db74();
                            }
                            if (!v129->field_18 || !((GameObject__SetActive(v129->field_18, 0, 0), v130 = (struct_3 *)*((long long *)&ptr->padding_0[0]), v130 && v130->field_20 && (v131 = (struct_50 *)(unsigned long long)sub_14a30c0(v130->field_20, (unsigned long long)v92, g_1ef8180), v131 && v131->field_18 && (v132 = (unsigned long)GameObject__get_transform(v131->field_18, 0), *((long long *)&ptr29->padding_0[0]) && (v133 = (unsigned long)GameObject__get_transform(v131->field_18, 0), v134 = (long long)(unsigned long long)Animator__GetBoneTransform(*((long long *)&ptr29->padding_0[0]), 17, 0), v133))))))
                                break;
                            Transform__set_parent(v133, Animator__GetBoneTransform(*((long long *)&ptr29->padding_0[0]), 17, 0), 0);
                        }
                        v135 = *((long long *)&ptr->padding_0[0]);
                        if (!v135)
                        {
                            v145 = sub_f7db74();
                            return sub_f7db74();
                        }
                        if (!v135->field_20)
                        {
                            v145 = sub_f7db74();
                            return sub_f7db74();
                        }
                        v136 = sub_14a30c0(v135->field_20, v92, g_1ef8180);
                        if (!v136)
                        {
                            v145 = sub_f7db74();
                            return sub_f7db74();
                        }
                        if (!g_1ef0c58->field_e0)
                            sub_f7da5c(g_1ef0c58);
                        v90 = Object__op_Inequality(v136->field_20, 0, 0);
                        if (((char)v90 & 1))
                        {
                            v137 = *((long long *)&ptr->padding_0[0]);
                            if (!v137)
                            {
                                v145 = sub_f7db74();
                                return sub_f7db74();
                            }
                            if (!v137->field_20)
                            {
                                v145 = sub_f7db74();
                                return sub_f7db74();
                            }
                            v138 = sub_14a30c0(v137->field_20, v92, g_1ef8180);
                            if (!v138)
                            {
                                v145 = sub_f7db74();
                                return sub_f7db74();
                            }
                            if (!v138->field_20 || !((GameObject__SetActive(v138->field_20, 0, 0), v139 = (struct_3 *)*((long long *)&ptr->padding_0[0]), v139 && v139->field_20 && (v140 = (struct_53 *)(unsigned long long)sub_14a30c0(v139->field_20, (unsigned long long)v92, g_1ef8180), v140 && v140->field_20 && (v141 = (unsigned long)GameObject__get_transform(v140->field_20, 0), *((long long *)&ptr29->padding_0[0]) && (v142 = (unsigned long)GameObject__get_transform(v140->field_20, 0), v143 = (long long)(unsigned long long)Animator__GetBoneTransform(*((long long *)&ptr29->padding_0[0]), 8, 0), v142))))))
                                break;
                            v90 = Transform__set_parent(v142, Animator__GetBoneTransform(*((long long *)&ptr29->padding_0[0]), 8, 0), 0);
                        }
                        i = *((long long *)&ptr->padding_0[0]);
                        v92 += 1;
                    } while (i);
LABEL_10a85f8:
                    v83 = sub_f7db7c();
LABEL_10a85fc:
                    sub_f7da4c(sub_f7db98(v83), 0);
                }
            }
        }
        else if (*((long long *)&ptr29->padding_0[0]))
        {
            v11 = Animator__GetBoneTransform(*((long long *)&ptr29->padding_0[0]), 10, 0);
            ptr3 = p;
            ptr3->field_28 = v11;
            v13 = &ptr3->field_28;
            sub_f7d8d0(v13, v11);
            if (*((long long *)&v13->padding_0[8]))
            {
                v14 = Animator__GetBoneTransform(*((long long *)&v13->padding_0[8]), 8, 0);
                ptr6 = p;
                ptr6->field_30 = v14;
                v16 = &ptr6->field_30;
                sub_f7d8d0(v16, v14);
                if (*((long long *)&v16->padding_0[16]))
                {
                    v17 = Animator__GetBoneTransform(*((long long *)&v16->padding_0[16]), 7, 0);
                    ptr7 = p;
                    ptr7->field_38 = v17;
                    sub_f7d8d0(&ptr7->field_38, v17);
                    goto LABEL_10a7a54;
                }
            }
        }
    }
LABEL_10a85c8:
    v145 = sub_f7db74();
    return sub_f7db74();
}
```

## `PlayerCharacter.Update` — RVA `0xca8608`

- Decompiled symbol: `PlayerCharacter_Update`
- Metadata signature: `private void Update() { }`
- Native interval: `15340` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: Decompiler produced no C-like text

```c
// 0x10a8608: sub sp, sp, #0xa0
// 0x10a860c: stp d15, d14, [sp, #0x10]
// 0x10a8610: stp d13, d12, [sp, #0x20]
// 0x10a8614: stp d11, d10, [sp, #0x30]
// 0x10a8618: stp d9, d8, [sp, #0x40]
// 0x10a861c: str x30, [sp, #0x50]
// 0x10a8620: stp x26, x25, [sp, #0x60]
// 0x10a8624: stp x24, x23, [sp, #0x70]
// 0x10a8628: stp x22, x21, [sp, #0x80]
// 0x10a862c: stp x20, x19, [sp, #0x90]
// 0x10a8630: adrp x20, #0x1fab000
// 0x10a8634: ldrb w8, [x20, #0x4c1]
// 0x10a8638: mov x19, x0
// 0x10a863c: tbnz w8, #0, #0x10a8720
// 0x10a8640: adrp x0, #0x1e8e000
// 0x10a8644: ldr x0, [x0, #0x550]
// 0x10a8648: bl #0xf7d92c
// 0x10a864c: adrp x0, #0x1e8e000
// 0x10a8650: ldr x0, [x0, #0x558]
// 0x10a8654: bl #0xf7d92c
// 0x10a8658: adrp x0, #0x1e8c000
// 0x10a865c: ldr x0, [x0, #0xd8]
// 0x10a8660: bl #0xf7d92c
// 0x10a8664: adrp x0, #0x1e8e000
// 0x10a8668: ldr x0, [x0, #0x568]
// 0x10a866c: bl #0xf7d92c
// 0x10a8670: adrp x0, #0x1e8e000
// 0x10a8674: ldr x0, [x0, #0x570]
// 0x10a8678: bl #0xf7d92c
// 0x10a867c: adrp x0, #0x1e8e000
// 0x10a8680: ldr x0, [x0, #0x578]
// 0x10a8684: bl #0xf7d92c
// 0x10a8688: adrp x0, #0x1e8e000
// 0x10a868c: ldr x0, [x0, #0x580]
// 0x10a8690: bl #0xf7d92c
// 0x10a8694: adrp x0, #0x1e8e000
// 0x10a8698: ldr x0, [x0, #0x588]
// 0x10a869c: bl #0xf7d92c
// 0x10a86a0: adrp x0, #0x1e8e000
// 0x10a86a4: ldr x0, [x0, #0x590]
// 0x10a86a8: bl #0xf7d92c
// 0x10a86ac: adrp x0, #0x1e8e000
// 0x10a86b0: ldr x0, [x0, #0x598]
// 0x10a86b4: bl #0xf7d92c
// 0x10a86b8: adrp x0, #0x1e8e000
// 0x10a86bc: ldr x0, [x0, #0x498]
// 0x10a86c0: bl #0xf7d92c
// 0x10a86c4: adrp x0, #0x1e8e000
// 0x10a86c8: ldr x0, [x0, #0x5a0]
// 0x10a86cc: bl #0xf7d92c
// 0x10a86d0: adrp x0, #0x1e8e000
// 0x10a86d4: ldr x0, [x0, #0x5a8]
// 0x10a86d8: bl #0xf7d92c
// 0x10a86dc: adrp x0, #0x1e8e000
// 0x10a86e0: ldr x0, [x0, #0x5b0]
// 0x10a86e4: bl #0xf7d92c
// 0x10a86e8: adrp x0, #0x1e8e000
// 0x10a86ec: ldr x0, [x0, #0x5b8]
// 0x10a86f0: bl #0xf7d92c
// 0x10a86f4: adrp x0, #0x1e8e000
// 0x10a86f8: ldr x0, [x0, #0x4b8]
// 0x10a86fc: bl #0xf7d92c
// 0x10a8700: adrp x0, #0x1e8e000
// 0x10a8704: ldr x0, [x0, #0x5c0]
// 0x10a8708: bl #0xf7d92c
// 0x10a870c: adrp x0, #0x1e8e000
// 0x10a8710: ldr x0, [x0, #0x5c8]
// 0x10a8714: bl #0xf7d92c
// 0x10a8718: mov w8, #1
// 0x10a871c: strb w8, [x20, #0x4c1]
// 0x10a8720: ldr x8, [x19, #0x70]
// 0x10a8724: cbz x8, #0x10ac1ec
// 0x10a8728: ldr x0, [x19, #0x20]
// 0x10a872c: cbz x0, #0x10ac1ec
// 0x10a8730: mov x1, xzr
// 0x10a8734: bl #0x1b673a0
// 0x10a8738: tbz w0, #0, #0x10ab9d0
// 0x10a873c: ldr x0, [x19, #0xc8]
// 0x10a8740: cbz x0, #0x10ac1ec
// 0x10a8744: mov x1, xzr
// 0x10a8748: bl #0x1b673a0
// 0x10a874c: tbz w0, #0, #0x10ab9d0
// 0x10a8750: mov x0, xzr
// 0x10a8754: bl #0x1b9ae58
// 0x10a8758: fcmp s0, #0.0
// 0x10a875c: b.le #0x10ab9d0
// 0x10a8760: ldr x8, [x19, #0x70]
// 0x10a8764: cbz x8, #0x10ac1ec
// 0x10a8768: ldr x1, [x8, #0x78]
// 0x10a876c: mov x20, x19
// 0x10a8770: str x1, [x20, #0x90]!
// 0x10a8774: mov x0, x20
// 0x10a8778: bl #0xf7d8d0
// 0x10a877c: ldur x8, [x20, #-0x10]
// 0x10a8780: cbz x8, #0x10ac1ec
// 0x10a8784: ldrb w8, [x8, #0x106]
// 0x10a8788: cbz w8, #0x10a8a70
// 0x10a878c: ldr x0, [x19, #0xa0]
// 0x10a8790: cbz x0, #0x10ac1ec
// 0x10a8794: ldr s0, [x19, #0x18c]
// 0x10a8798: mov x1, xzr
// 0x10a879c: mov v1.16b, v0.16b
// 0x10a87a0: mov v2.16b, v0.16b
// 0x10a87a4: bl #0x1b9dbe0
// 0x10a87a8: ldr x0, [x19, #0x50]
// 0x10a87ac: cbz x0, #0x10ac1ec
// 0x10a87b0: mov x1, xzr
// 0x10a87b4: bl #0x1b9d508
// 0x10a87b8: ldr x0, [x19, #0x50]
// 0x10a87bc: cbz x0, #0x10ac1ec
// 0x10a87c0: mov x1, xzr
// 0x10a87c4: mov v8.16b, v0.16b
// 0x10a87c8: bl #0x1b9d508
// 0x10a87cc: ldr x0, [x19, #0x50]
// 0x10a87d0: cbz x0, #0x10ac1ec
// 0x10a87d4: ldr s11, [x19, #0x1d4]
// 0x10a87d8: mov x1, xzr
// 0x10a87dc: mov v10.16b, v1.16b
// 0x10a87e0: bl #0x1b9d508
// 0x10a87e4: ldr x8, [x19, #0x80]
// 0x10a87e8: fsub s10, s10, s11
// 0x10a87ec: str s8, [x19, #0x174]
// 0x10a87f0: str s10, [x19, #0x178]
// 0x10a87f4: str s2, [x19, #0x17c]
// 0x10a87f8: cbz x8, #0x10ac1ec
// 0x10a87fc: ldr s11, [x19, #0x170]
// 0x10a8800: ldr s12, [x19, #0x16c]
// 0x10a8804: ldr s13, [x19, #0x168]
// 0x10a8808: ldr s14, [x8, #0x118]
// 0x10a880c: mov x0, xzr
// 0x10a8810: mov v9.16b, v2.16b
// 0x10a8814: add x21, x19, #0x15c
// 0x10a8818: bl #0x1b9ae30
// 0x10a881c: mov w8, #0x7f800000
// 0x10a8820: str s0, [sp]
// 0x10a8824: fmov s7, w8
// 0x10a8828: mov v0.16b, v13.16b
// 0x10a882c: mov v1.16b, v12.16b
// 0x10a8830: mov v2.16b, v11.16b
// 0x10a8834: mov v3.16b, v8.16b
// 0x10a8838: mov v4.16b, v10.16b
// 0x10a883c: mov v5.16b, v9.16b
// 0x10a8840: mov x0, x21
// 0x10a8844: mov v6.16b, v14.16b
// 0x10a8848: mov x1, xzr
// 0x10a884c: bl #0x1b89b88
// 0x10a8850: ldr x0, [x19, #0xa0]
// 0x10a8854: str s0, [x19, #0x168]
// 0x10a8858: str s1, [x19, #0x16c]
// 0x10a885c: str s2, [x19, #0x170]
// 0x10a8860: cbz x0, #0x10ac1ec
// 0x10a8864: mov x1, xzr
// 0x10a8868: bl #0x1b9d5a8
// 0x10a886c: ldr x0, [x19, #0x50]
// 0x10a8870: cbz x0, #0x10ac1ec
// 0x10a8874: ldr s8, [x19, #0x158]
// 0x10a8878: ldr s9, [x19, #0x110]
// 0x10a887c: mov x1, xzr
// 0x10a8880: bl #0x1b9d6c8
// 0x10a8884: ldr x21, [x19, #0xa0]
// 0x10a8888: fadd s0, s8, s9
// 0x10a888c: fadd s0, s0, s1
// 0x10a8890: str wzr, [x19, #0x118]
// 0x10a8894: str s0, [x19, #0x11c]
// 0x10a8898: str wzr, [x19, #0x120]
// 0x10a889c: cbz x21, #0x10ac1ec
// 0x10a88a0: mov x0, x21
// 0x10a88a4: mov x1, xzr
// 0x10a88a8: bl #0x1b9d6f0
// 0x10a88ac: adrp x8, #0x832000
// 0x10a88b0: mov v8.16b, v0.16b
// 0x10a88b4: mov v9.16b, v1.16b
// 0x10a88b8: mov v10.16b, v2.16b
// 0x10a88bc: mov v11.16b, v3.16b
// 0x10a88c0: ldr s0, [x19, #0x118]
// 0x10a88c4: ldr s2, [x8, #0x3e4]
// 0x10a88c8: ldr s1, [x19, #0x11c]
// 0x10a88cc: ldr s3, [x19, #0x120]
// 0x10a88d0: mov x0, xzr
// 0x10a88d4: fmul s0, s0, s2
// 0x10a88d8: fmul s1, s1, s2
// 0x10a88dc: fmul s2, s3, s2
// 0x10a88e0: bl #0x1b8b12c
// 0x10a88e4: mov x0, xzr
// 0x10a88e8: mov v12.16b, v0.16b
// 0x10a88ec: mov v13.16b, v1.16b
// 0x10a88f0: mov v14.16b, v2.16b
// 0x10a88f4: mov v15.16b, v3.16b
// 0x10a88f8: bl #0x1b9ae30
// 0x10a88fc: ldr s1, [x19, #0x138]
// 0x10a8900: mov v2.16b, v10.16b
// 0x10a8904: mov v3.16b, v11.16b
// 0x10a8908: mov v4.16b, v12.16b
// 0x10a890c: fmul s0, s0, s1
// 0x10a8910: str s0, [sp]
// 0x10a8914: mov v0.16b, v8.16b
// 0x10a8918: mov v1.16b, v9.16b
// 0x10a891c: mov v5.16b, v13.16b
// 0x10a8920: mov v6.16b, v14.16b
// 0x10a8924: mov v7.16b, v15.16b
// 0x10a8928: mov x0, xzr
// 0x10a892c: bl #0x1b8af84
// 0x10a8930: mov x0, x21
// 0x10a8934: mov x1, xzr
// 0x10a8938: bl #0x1b9d874
// 0x10a893c: ldr x0, [x19, #0xd0]
// 0x10a8940: cbz x0, #0x10ac1ec
// 0x10a8944: mov w1, wzr
// 0x10a8948: mov x2, xzr
// 0x10a894c: bl #0x1b799d0
// 0x10a8950: ldr x0, [x19, #0xa0]
// 0x10a8954: cbz x0, #0x10ac1ec
// 0x10a8958: ldr x21, [x19, #0xc0]
// 0x10a895c: mov x1, xzr
// 0x10a8960: bl #0x1b9d508
// 0x10a8964: cbz x21, #0x10ac1ec
// 0x10a8968: mov x0, x21
// 0x10a896c: mov x1, xzr
// 0x10a8970: bl #0x1b9d5a8
// 0x10a8974: ldr x0, [x19, #0xa0]
// 0x10a8978: cbz x0, #0x10ac1ec
// 0x10a897c: ldr x21, [x19, #0xc0]
// 0x10a8980: mov x1, xzr
// 0x10a8984: bl #0x1b9d6f0
// 0x10a8988: cbz x21, #0x10ac1ec
// 0x10a898c: mov x0, x21
// 0x10a8990: mov x1, xzr
// 0x10a8994: bl #0x1b9d774
// 0x10a8998: ldr x0, [x19, #0xa0]
// 0x10a899c: cbz x0, #0x10ac1ec
// 0x10a89a0: ldr x21, [x19, #0xc0]
// 0x10a89a4: mov x1, xzr
// 0x10a89a8: bl #0x1b9db40
// 0x10a89ac: cbz x21, #0x10ac1ec
// 0x10a89b0: mov x0, x21
// 0x10a89b4: mov x1, xzr
// 0x10a89b8: bl #0x1b9dbe0
// 0x10a89bc: ldr x8, [x19, #0x80]
// 0x10a89c0: cbz x8, #0x10ac1ec
// 0x10a89c4: ldrb w10, [x8, #0x106]
// 0x10a89c8: ldrb w9, [x19, #0xd8]
// 0x10a89cc: ldrb w8, [x19, #0x2fe]
// 0x10a89d0: cbz w10, #0x10a8c00
// 0x10a89d4: cbz w9, #0x10a8c9c
// 0x10a89d8: cbz w8, #0x10a8e24
// 0x10a89dc: ldr x21, [x19, #0xa8]
// 0x10a89e0: cbz x21, #0x10ac1ec
// 0x10a89e4: ldr w8, [x21, #0x18]
// 0x10a89e8: cmp w8, #1
// 0x10a89ec: b.lt #0x10a8a24
// 0x10a89f0: mov w22, wzr
// 0x10a89f4: cmp w22, w8
// 0x10a89f8: b.hs #0x10ac1f0
// 0x10a89fc: add x8, x21, w22, sxtw #3
// 0x10a8a00: ldr x0, [x8, #0x20]
// 0x10a8a04: cbz x0, #0x10ac1ec
// 0x10a8a08: mov w1, #1
// 0x10a8a0c: mov x2, xzr
// 0x10a8a10: bl #0x1b79a14
// 0x10a8a14: ldr w8, [x21, #0x18]
// 0x10a8a18: add w22, w22, #1
// 0x10a8a1c: cmp w22, w8
// 0x10a8a20: b.lt #0x10a89f4
// 0x10a8a24: ldr x21, [x19, #0xb0]
// 0x10a8a28: cbz x21, #0x10ac1ec
// 0x10a8a2c: ldr w8, [x21, #0x18]
// 0x10a8a30: cmp w8, #1
// 0x10a8a34: b.lt #0x10a8d58
// 0x10a8a38: mov w22, wzr
// 0x10a8a3c: cmp w22, w8
// 0x10a8a40: b.hs #0x10ac1f0
// 0x10a8a44: add x8, x21, w22, sxtw #3
// 0x10a8a48: ldr x0, [x8, #0x20]
// 0x10a8a4c: cbz x0, #0x10ac1ec
// 0x10a8a50: mov w1, #1
// 0x10a8a54: mov x2, xzr
// 0x10a8a58: bl #0x1b79a14
// 0x10a8a5c: ldr w8, [x21, #0x18]
// 0x10a8a60: add w22, w22, #1
// 0x10a8a64: cmp w22, w8
// 0x10a8a68: b.lt #0x10a8a3c
// 0x10a8a6c: b #0x10a8d58
// 0x10a8a70: ldrb w8, [x19, #0xd8]
// 0x10a8a74: cbz w8, #0x10a878c
// 0x10a8a78: ldr x8, [x19, #0x68]
// 0x10a8a7c: cbz x8, #0x10ac1ec
// 0x10a8a80: ldrb w9, [x8, #0x2d0]
// 0x10a8a84: cbz w9, #0x10a925c
// 0x10a8a88: ldr x9, [x20]
// 0x10a8a8c: cbz x9, #0x10ac1ec
// 0x10a8a90: ldr w9, [x9, #0x368]
// 0x10a8a94: cbz w9, #0x10a9610
// 0x10a8a98: ldr s8, [x19, #0x1ec]
// 0x10a8a9c: mov x0, xzr
// 0x10a8aa0: bl #0x1b9ae30
// 0x10a8aa4: fmov s9, wzr
// 0x10a8aa8: fsub s1, s9, s8
// 0x10a8aac: mov w8, #0x42c80000
// 0x10a8ab0: fabs s2, s1
// 0x10a8ab4: fcmp s1, #0.0
// 0x10a8ab8: fmov s1, w8
// 0x10a8abc: fmul s3, s0, s1
// 0x10a8ac0: fnmul s0, s0, s1
// 0x10a8ac4: ldr s10, [x19, #0x1c8]
// 0x10a8ac8: ldr s11, [x19, #0x1bc]
// 0x10a8acc: fcsel s0, s3, s0, ge
// 0x10a8ad0: fadd s0, s8, s0
// 0x10a8ad4: fcmp s2, s3
// 0x10a8ad8: fcsel s0, s0, s9, hi
// 0x10a8adc: mov x0, xzr
// 0x10a8ae0: str s0, [x19, #0x1ec]
// 0x10a8ae4: bl #0x1b9ae30
// 0x10a8ae8: fmov s8, #1.00000000
// 0x10a8aec: fcmp s0, #0.0
// 0x10a8af0: fmov s9, wzr
// 0x10a8af4: fmin s0, s0, s8
// 0x10a8af8: fsub s1, s11, s10
// 0x10a8afc: ldr s11, [x19, #0x1b0]
// 0x10a8b00: fcsel s0, s0, s9, pl
// 0x10a8b04: ldr s12, [x19, #0x1a8]
// 0x10a8b08: fmul s0, s1, s0
// 0x10a8b0c: fadd s0, s10, s0
// 0x10a8b10: mov x0, xzr
// 0x10a8b14: str s0, [x19, #0x1c8]
// 0x10a8b18: bl #0x1b9ae30
// 0x10a8b1c: mov w9, #0x42000000
// 0x10a8b20: fsub s1, s12, s11
// 0x10a8b24: fmov s3, w9
// 0x10a8b28: ldr x8, [x19, #0x90]
// 0x10a8b2c: fmul s4, s0, s3
// 0x10a8b30: fnmul s0, s0, s3
// 0x10a8b34: fcmp s1, #0.0
// 0x10a8b38: fabd s2, s12, s11
// 0x10a8b3c: fcsel s0, s4, s0, ge
// 0x10a8b40: fadd s0, s11, s0
// 0x10a8b44: fcmp s2, s4
// 0x10a8b48: fcsel s0, s0, s12, hi
// 0x10a8b4c: str s0, [x19, #0x1b0]
// 0x10a8b50: cbz x8, #0x10ac1ec
// 0x10a8b54: ldr w8, [x8, #0x368]
// 0x10a8b58: mov w9, #0x1d8
// 0x10a8b5c: ldr s10, [x19, #0x1e4]
// 0x10a8b60: mov x0, xzr
// 0x10a8b64: cmp w8, #0
// 0x10a8b68: mov w8, #0x1dc
// 0x10a8b6c: csel x8, x8, x9, eq
// 0x10a8b70: ldr s11, [x19, x8]
// 0x10a8b74: bl #0x1b9ae30
// 0x10a8b78: fmov s1, #8.00000000
// 0x10a8b7c: fsub s2, s11, s10
// 0x10a8b80: fmul s4, s0, s1
// 0x10a8b84: fnmul s0, s0, s1
// 0x10a8b88: fcmp s2, #0.0
// 0x10a8b8c: fabd s3, s11, s10
// 0x10a8b90: ldr s12, [x19, #0x188]
// 0x10a8b94: ldr s13, [x19, #0x184]
// 0x10a8b98: fcsel s0, s4, s0, ge
// 0x10a8b9c: fadd s0, s10, s0
// 0x10a8ba0: fcmp s3, s4
// 0x10a8ba4: fcsel s0, s0, s11, hi
// 0x10a8ba8: mov x0, xzr
// 0x10a8bac: str s0, [x19, #0x1e4]
// 0x10a8bb0: bl #0x1b9ae30
// 0x10a8bb4: fsub s1, s13, s12
// 0x10a8bb8: fneg s3, s0
// 0x10a8bbc: ldr s10, [x19, #0x1cc]
// 0x10a8bc0: fcmp s1, #0.0
// 0x10a8bc4: fabd s2, s13, s12
// 0x10a8bc8: fcsel s1, s0, s3, ge
// 0x10a8bcc: fadd s1, s12, s1
// 0x10a8bd0: fcmp s2, s0
// 0x10a8bd4: fcsel s0, s1, s13, hi
// 0x10a8bd8: mov x0, xzr
// 0x10a8bdc: str s0, [x19, #0x188]
// 0x10a8be0: bl #0x1b9ae30
// 0x10a8be4: fmov s1, #7.00000000
// 0x10a8be8: fmul s0, s0, s1
// 0x10a8bec: fmin s1, s0, s8
// 0x10a8bf0: fcmp s0, #0.0
// 0x10a8bf4: fcsel s0, s1, s9, pl
// 0x10a8bf8: fsub s1, s9, s10
// 0x10a8bfc: b #0x10a93c0
// 0x10a8c00: cbz w9, #0x10a8d60
// 0x10a8c04: cbnz w8, #0x10a8e24
// 0x10a8c08: ldr x21, [x19, #0xa8]
// 0x10a8c0c: cbz x21, #0x10ac1ec
// 0x10a8c10: ldr w8, [x21, #0x18]
// 0x10a8c14: cmp w8, #1
// 0x10a8c18: b.lt #0x10a8c50
// 0x10a8c1c: mov w22, wzr
// 0x10a8c20: cmp w22, w8
// 0x10a8c24: b.hs #0x10ac1f0
// 0x10a8c28: add x8, x21, w22, sxtw #3
// 0x10a8c2c: ldr x0, [x8, #0x20]
// 0x10a8c30: cbz x0, #0x10ac1ec
// 0x10a8c34: mov w1, #3
// 0x10a8c38: mov x2, xzr
// 0x10a8c3c: bl #0x1b79a14
// 0x10a8c40: ldr w8, [x21, #0x18]
// 0x10a8c44: add w22, w22, #1
// 0x10a8c48: cmp w22, w8
// 0x10a8c4c: b.lt #0x10a8c20
// 0x10a8c50: ldr x21, [x19, #0xb0]
// 0x10a8c54: cbz x21, #0x10ac1ec
// 0x10a8c58: ldr w8, [x21, #0x18]
// 0x10a8c5c: cmp w8, #1
// 0x10a8c60: b.lt #0x10a8e1c
// 0x10a8c64: mov w22, wzr
// 0x10a8c68: cmp w22, w8
// 0x10a8c6c: b.hs #0x10ac1f0
// 0x10a8c70: add x8, x21, w22, sxtw #3
// 0x10a8c74: ldr x0, [x8, #0x20]
// 0x10a8c78: cbz x0, #0x10ac1ec
// 0x10a8c7c: mov w1, #3
// 0x10a8c80: mov x2, xzr
// 0x10a8c84: bl #0x1b79a14
// 0x10a8c88: ldr w8, [x21, #0x18]
// 0x10a8c8c: add w22, w22, #1
// 0x10a8c90: cmp w22, w8
// 0x10a8c94: b.lt #0x10a8c68
// 0x10a8c98: b #0x10a8e1c
// 0x10a8c9c: cbz w8, #0x10a8e24
// 0x10a8ca0: ldr x22, [x19, #0xa8]
// 0x10a8ca4: cbz x22, #0x10ac1ec
// 0x10a8ca8: ldr w8, [x22, #0x18]
// 0x10a8cac: cmp w8, #1
// 0x10a8cb0: b.lt #0x10a8cfc
// 0x10a8cb4: mov w23, wzr
// 0x10a8cb8: cmp w23, w8
// 0x10a8cbc: b.hs #0x10ac1f0
// 0x10a8cc0: add x8, x22, w23, sxtw #3
// 0x10a8cc4: ldr x21, [x8, #0x20]
// 0x10a8cc8: cbz x21, #0x10ac1ec
// 0x10a8ccc: mov w1, #1
// 0x10a8cd0: mov x0, x21
// 0x10a8cd4: mov x2, xzr
// 0x10a8cd8: bl #0x1b799d0
// 0x10a8cdc: mov w1, #1
// 0x10a8ce0: mov x0, x21
// 0x10a8ce4: mov x2, xzr
// 0x10a8ce8: bl #0x1b79a14
// 0x10a8cec: ldr w8, [x22, #0x18]
// 0x10a8cf0: add w23, w23, #1
// 0x10a8cf4: cmp w23, w8
// 0x10a8cf8: b.lt #0x10a8cb8
// 0x10a8cfc: ldr x22, [x19, #0xb0]
// 0x10a8d00: cbz x22, #0x10ac1ec
// 0x10a8d04: ldr w8, [x22, #0x18]
// 0x10a8d08: cmp w8, #1
// 0x10a8d0c: b.lt #0x10a8d58
// 0x10a8d10: mov w23, wzr
// 0x10a8d14: cmp w23, w8
// 0x10a8d18: b.hs #0x10ac1f0
// 0x10a8d1c: add x8, x22, w23, sxtw #3
// 0x10a8d20: ldr x21, [x8, #0x20]
// 0x10a8d24: cbz x21, #0x10ac1ec
// 0x10a8d28: mov w1, #1
// 0x10a8d2c: mov x0, x21
// 0x10a8d30: mov x2, xzr
// 0x10a8d34: bl #0x1b799d0
// 0x10a8d38: mov w1, #1
// 0x10a8d3c: mov x0, x21
// 0x10a8d40: mov x2, xzr
// 0x10a8d44: bl #0x1b79a14
// 0x10a8d48: ldr w8, [x22, #0x18]
// 0x10a8d4c: add w23, w23, #1
// 0x10a8d50: cmp w23, w8
// 0x10a8d54: b.lt #0x10a8d14
// 0x10a8d58: strb wzr, [x19, #0x2fe]
// 0x10a8d5c: b #0x10a8e24
// 0x10a8d60: cbnz w8, #0x10a8e24
// 0x10a8d64: ldr x22, [x19, #0xa8]
// 0x10a8d68: cbz x22, #0x10ac1ec
// 0x10a8d6c: ldr w8, [x22, #0x18]
// 0x10a8d70: cmp w8, #1
// 0x10a8d74: b.lt #0x10a8dc0
// 0x10a8d78: mov w23, wzr
// 0x10a8d7c: cmp w23, w8
// 0x10a8d80: b.hs #0x10ac1f0
// 0x10a8d84: add x8, x22, w23, sxtw #3
// 0x10a8d88: ldr x21, [x8, #0x20]
// 0x10a8d8c: cbz x21, #0x10ac1ec
// 0x10a8d90: mov x0, x21
// 0x10a8d94: mov w1, wzr
// 0x10a8d98: mov x2, xzr
// 0x10a8d9c: bl #0x1b799d0
// 0x10a8da0: mov w1, #3
// 0x10a8da4: mov x0, x21
// 0x10a8da8: mov x2, xzr
// 0x10a8dac: bl #0x1b79a14
// 0x10a8db0: ldr w8, [x22, #0x18]
// 0x10a8db4: add w23, w23, #1
// 0x10a8db8: cmp w23, w8
// 0x10a8dbc: b.lt #0x10a8d7c
// 0x10a8dc0: ldr x22, [x19, #0xb0]
// 0x10a8dc4: cbz x22, #0x10ac1ec
// 0x10a8dc8: ldr w8, [x22, #0x18]
// 0x10a8dcc: cmp w8, #1
// 0x10a8dd0: b.lt #0x10a8e1c
// 0x10a8dd4: mov w23, wzr
// 0x10a8dd8: cmp w23, w8
// 0x10a8ddc: b.hs #0x10ac1f0
// 0x10a8de0: add x8, x22, w23, sxtw #3
// 0x10a8de4: ldr x21, [x8, #0x20]
// 0x10a8de8: cbz x21, #0x10ac1ec
// 0x10a8dec: mov x0, x21
// 0x10a8df0: mov w1, wzr
// 0x10a8df4: mov x2, xzr
// 0x10a8df8: bl #0x1b799d0
// 0x10a8dfc: mov w1, #3
// 0x10a8e00: mov x0, x21
// 0x10a8e04: mov x2, xzr
// 0x10a8e08: bl #0x1b79a14
// 0x10a8e0c: ldr w8, [x22, #0x18]
// 0x10a8e10: add w23, w23, #1
// 0x10a8e14: cmp w23, w8
// 0x10a8e18: b.lt #0x10a8dd8
// 0x10a8e1c: mov w8, #1
// 0x10a8e20: strb w8, [x19, #0x2fe]
// 0x10a8e24: mov x22, x19
// 0x10a8e28: ldr x8, [x22, #0x68]!
// 0x10a8e2c: cbz x8, #0x10ac1ec
// 0x10a8e30: add x23, x19, #0x144
// 0x10a8e34: ldr d8, [x8, #0xc0]
// 0x10a8e38: ldr d9, [x23, #0xb0]
// 0x10a8e3c: mov x0, xzr
// 0x10a8e40: str d8, [x23]
// 0x10a8e44: bl #0x1b9ae30
// 0x10a8e48: ldr s1, [x19, #0x1fc]
// 0x10a8e4c: fmov s2, #1.00000000
// 0x10a8e50: fmov s3, wzr
// 0x10a8e54: fmul s0, s0, s1
// 0x10a8e58: fmin s1, s0, s2
// 0x10a8e5c: fcmp s0, #0.0
// 0x10a8e60: fcsel s0, s1, s3, pl
// 0x10a8e64: fsub v1.2s, v8.2s, v9.2s
// 0x10a8e68: fmul v0.2s, v1.2s, v0.s[0]
// 0x10a8e6c: fadd v0.2s, v9.2s, v0.2s
// 0x10a8e70: str d0, [x23, #0xb0]
// 0x10a8e74: ldr x8, [x19, #0x68]
// 0x10a8e78: cbz x8, #0x10ac1ec
// 0x10a8e7c: ldr s0, [x8, #0xc4]
// 0x10a8e80: ldr x21, [x19, #0x20]
// 0x10a8e84: fmov s1, #0.50000000
// 0x10a8e88: adrp x24, #0x832000
// 0x10a8e8c: fabs s0, s0
// 0x10a8e90: fcmp s0, s1
// 0x10a8e94: b.le #0x10a8eec
// 0x10a8e98: mov x0, xzr
// 0x10a8e9c: bl #0x1b89b60
// 0x10a8ea0: cbz x21, #0x10ac1ec
// 0x10a8ea4: adrp x25, #0x1e8e000
// 0x10a8ea8: ldr x25, [x25, #0x598]
// 0x10a8eac: ldr s8, [x24, #0x4d4]
// 0x10a8eb0: mov v2.16b, v0.16b
// 0x10a8eb4: fmov s0, wzr
// 0x10a8eb8: ldr x1, [x25]
// 0x10a8ebc: mov x0, x21
// 0x10a8ec0: mov v1.16b, v8.16b
// 0x10a8ec4: mov x2, xzr
// 0x10a8ec8: bl #0x1b67484
// 0x10a8ecc: ldr x21, [x19, #0xc8]
// 0x10a8ed0: mov x0, xzr
// 0x10a8ed4: bl #0x1b89b60
// 0x10a8ed8: cbz x21, #0x10ac1ec
// 0x10a8edc: ldr x1, [x25]
// 0x10a8ee0: mov v2.16b, v0.16b
// 0x10a8ee4: fmov s0, wzr
// 0x10a8ee8: b #0x10a8f4c
// 0x10a8eec: ldr s8, [x8, #0xc0]
// 0x10a8ef0: mov x0, xzr
// 0x10a8ef4: bl #0x1b89b60
// 0x10a8ef8: cbz x21, #0x10ac1ec
// 0x10a8efc: adrp x25, #0x1e8e000
// 0x10a8f00: ldr x25, [x25, #0x598]
// 0x10a8f04: mov v2.16b, v0.16b
// 0x10a8f08: fabs s0, s8
// 0x10a8f0c: ldr s8, [x24, #0x4d4]
// 0x10a8f10: ldr x1, [x25]
// 0x10a8f14: mov x0, x21
// 0x10a8f18: mov x2, xzr
// 0x10a8f1c: mov v1.16b, v8.16b
// 0x10a8f20: bl #0x1b67484
// 0x10a8f24: ldr x8, [x19, #0x68]
// 0x10a8f28: cbz x8, #0x10ac1ec
// 0x10a8f2c: ldr x21, [x19, #0xc8]
// 0x10a8f30: ldr s9, [x8, #0xc0]
// 0x10a8f34: mov x0, xzr
// 0x10a8f38: bl #0x1b89b60
// 0x10a8f3c: cbz x21, #0x10ac1ec
// 0x10a8f40: ldr x1, [x25]
// 0x10a8f44: mov v2.16b, v0.16b
// 0x10a8f48: fabs s0, s9
// 0x10a8f4c: mov x0, x21
// 0x10a8f50: mov v1.16b, v8.16b
// 0x10a8f54: mov x2, xzr
// 0x10a8f58: bl #0x1b67484
// 0x10a8f5c: ldr x8, [x19, #0x68]
// 0x10a8f60: cbz x8, #0x10ac1ec
// 0x10a8f64: ldr x21, [x19, #0x20]
// 0x10a8f68: ldr s9, [x8, #0xc0]
// 0x10a8f6c: mov x0, xzr
// 0x10a8f70: bl #0x1b89b60
// 0x10a8f74: cbz x21, #0x10ac1ec
// 0x10a8f78: adrp x25, #0x1e8e000
// 0x10a8f7c: ldr x25, [x25, #0x570]
// 0x10a8f80: adrp x8, #0x832000
// 0x10a8f84: ldr s12, [x8, #0x550]
// 0x10a8f88: mov v2.16b, v0.16b
// 0x10a8f8c: ldr x1, [x25]
// 0x10a8f90: mov x0, x21
// 0x10a8f94: mov v0.16b, v9.16b
// 0x10a8f98: mov v1.16b, v12.16b
// 0x10a8f9c: mov x2, xzr
// 0x10a8fa0: bl #0x1b67484
// 0x10a8fa4: ldr x8, [x19, #0x68]
// 0x10a8fa8: cbz x8, #0x10ac1ec
// 0x10a8fac: ldr x21, [x19, #0x20]
// 0x10a8fb0: ldr s10, [x8, #0xc4]
// 0x10a8fb4: mov x0, xzr
// 0x10a8fb8: bl #0x1b89b60
// 0x10a8fbc: cbz x21, #0x10ac1ec
// 0x10a8fc0: adrp x26, #0x1e8e000
// 0x10a8fc4: ldr x26, [x26, #0x590]
// 0x10a8fc8: ldr s9, [x24, #0x4d4]
// 0x10a8fcc: mov v2.16b, v0.16b
// 0x10a8fd0: mov x0, x21
// 0x10a8fd4: ldr x1, [x26]
// 0x10a8fd8: mov v0.16b, v10.16b
// 0x10a8fdc: mov v1.16b, v9.16b
// 0x10a8fe0: mov x2, xzr
// 0x10a8fe4: bl #0x1b67484
// 0x10a8fe8: ldr x8, [x19, #0x68]
// 0x10a8fec: cbz x8, #0x10ac1ec
// 0x10a8ff0: ldr x21, [x19, #0xc8]
// 0x10a8ff4: ldr s10, [x8, #0xc0]
// 0x10a8ff8: mov x0, xzr
// 0x10a8ffc: bl #0x1b89b60
// 0x10a9000: cbz x21, #0x10ac1ec
// 0x10a9004: ldr x1, [x25]
// 0x10a9008: mov v2.16b, v0.16b
// 0x10a900c: mov x0, x21
// 0x10a9010: mov v0.16b, v10.16b
// 0x10a9014: mov v1.16b, v12.16b
// 0x10a9018: mov x2, xzr
// 0x10a901c: bl #0x1b67484
// 0x10a9020: ldr x8, [x19, #0x68]
// 0x10a9024: cbz x8, #0x10ac1ec
// 0x10a9028: ldr x21, [x19, #0xc8]
// 0x10a902c: ldr s10, [x8, #0xc4]
// 0x10a9030: mov x0, xzr
// 0x10a9034: bl #0x1b89b60
// 0x10a9038: cbz x21, #0x10ac1ec
// 0x10a903c: ldr x1, [x26]
// 0x10a9040: mov v2.16b, v0.16b
// 0x10a9044: mov x0, x21
// 0x10a9048: mov v0.16b, v10.16b
// 0x10a904c: mov v1.16b, v9.16b
// 0x10a9050: mov x2, xzr
// 0x10a9054: bl #0x1b67484
// 0x10a9058: ldr x8, [x22]
// 0x10a905c: cbz x8, #0x10ac1ec
// 0x10a9060: ldrb w21, [x8, #0x2e8]
// 0x10a9064: mov x0, xzr
// 0x10a9068: bl #0x1b9ad30
// 0x10a906c: cbz w21, #0x10a9078
// 0x10a9070: str s0, [x19, #0x140]
// 0x10a9074: b #0x10a907c
// 0x10a9078: str s0, [x19, #0x13c]
// 0x10a907c: ldr x8, [x22]
// 0x10a9080: cbz x8, #0x10ac1ec
// 0x10a9084: ldrb w8, [x8, #0x258]
// 0x10a9088: cbnz w8, #0x10a9124
// 0x10a908c: ldr x8, [x19, #0x80]
// 0x10a9090: cbz x8, #0x10ac1ec
// 0x10a9094: ldr s8, [x8, #0x1a0]
// 0x10a9098: mov x0, xzr
// 0x10a909c: bl #0x1b9ad30
// 0x10a90a0: adrp x8, #0x832000
// 0x10a90a4: ldr s1, [x8, #0x2f8]
// 0x10a90a8: fadd s1, s8, s1
// 0x10a90ac: fcmp s1, s0
// 0x10a90b0: b.pl #0x10a9124
// 0x10a90b4: ldr x8, [x19, #0x80]
// 0x10a90b8: cbz x8, #0x10ac1ec
// 0x10a90bc: ldrb w8, [x8, #0x106]
// 0x10a90c0: cbz w8, #0x10a95c8
// 0x10a90c4: ldr x0, [x19, #0xa0]
// 0x10a90c8: cbz x0, #0x10ac1ec
// 0x10a90cc: mov x1, xzr
// 0x10a90d0: bl #0x1b9d6c8
// 0x10a90d4: ldr s0, [x19, #0x11c]
// 0x10a90d8: mov w8, #0x43b40000
// 0x10a90dc: fmov s2, w8
// 0x10a90e0: mov w9, #-0x3c4c0000
// 0x10a90e4: fsub s0, s0, s1
// 0x10a90e8: fdiv s1, s0, s2
// 0x10a90ec: fmov s3, w9
// 0x10a90f0: frintm s1, s1
// 0x10a90f4: fmul s1, s1, s3
// 0x10a90f8: fadd s0, s0, s1
// 0x10a90fc: fmov s1, wzr
// 0x10a9100: mov w8, #0x43340000
// 0x10a9104: fmin s2, s0, s2
// 0x10a9108: fcmp s0, #0.0
// 0x10a910c: fmov s0, w8
// 0x10a9110: fcsel s1, s2, s1, pl
// 0x10a9114: fadd s2, s1, s3
// 0x10a9118: fcmp s1, s0
// 0x10a911c: fcsel s0, s2, s1, gt
// 0x10a9120: b #0x10a9608
// 0x10a9124: str wzr, [x19, #0x1f0]
// 0x10a9128: ldr x8, [x19, #0x78]
// 0x10a912c: cbz x8, #0x10ac1ec
// 0x10a9130: ldr s0, [x8, #0x7c]
// 0x10a9134: fmov s1, #0.50000000
// 0x10a9138: adrp x24, #0x832000
// 0x10a913c: fabs s0, s0
// 0x10a9140: fcmp s0, s1
// 0x10a9144: b.le #0x10a91a4
// 0x10a9148: ldr x8, [x19, #0x70]
// 0x10a914c: cbz x8, #0x10ac1ec
// 0x10a9150: ldrb w8, [x8, #0x2d0]
// 0x10a9154: cbnz w8, #0x10a9178
// 0x10a9158: ldr s8, [x19, #0x200]
// 0x10a915c: ldr s10, [x19, #0x204]
// 0x10a9160: mov x0, xzr
// 0x10a9164: bl #0x1b9ad30
// 0x10a9168: fmul s1, s10, s9
// 0x10a916c: fadd s1, s8, s1
// 0x10a9170: fcmp s1, s0
// 0x10a9174: b.le #0x10a91a4
// 0x10a9178: ldr s8, [x19, #0x300]
// 0x10a917c: mov x0, xzr
// 0x10a9180: bl #0x1b89b60
// 0x10a9184: ldr s1, [x24, #0x3a0]
// 0x10a9188: fadd s0, s8, s0
// 0x10a918c: str s0, [x19, #0x300]
// 0x10a9190: fcmp s0, s1
// 0x10a9194: b.le #0x10a91a8
// 0x10a9198: mov w8, #0x41840000
// 0x10a919c: str w8, [x19, #0x1f0]
// 0x10a91a0: b #0x10a91a8
// 0x10a91a4: str wzr, [x19, #0x300]
// 0x10a91a8: ldr x8, [x22]
// 0x10a91ac: cbz x8, #0x10ac1ec
// 0x10a91b0: ldr s0, [x19, #0x1f8]
// 0x10a91b4: ldr s1, [x19, #0x1f4]
// 0x10a91b8: ldrb w8, [x8, #0x2dc]
// 0x10a91bc: ldr x9, [x19, #0x60]
// 0x10a91c0: fabs s2, s0
// 0x10a91c4: fabs s1, s1
// 0x10a91c8: fcmp s2, s1
// 0x10a91cc: fcsel s1, s2, s1, gt
// 0x10a91d0: fcmp s0, #0.0
// 0x10a91d4: ccmp w8, #0, #4, lt
// 0x10a91d8: fneg s0, s1
// 0x10a91dc: fcsel s0, s1, s0, eq
// 0x10a91e0: str s0, [x19, #0x20c]
// 0x10a91e4: cbz x9, #0x10ac1ec
// 0x10a91e8: ldr s1, [x19, #0x148]
// 0x10a91ec: ldr s2, [x9, #0xc8]
// 0x10a91f0: fcmp s1, s2
// 0x10a91f4: b.le #0x10a9200
// 0x10a91f8: mov w8, #1
// 0x10a91fc: b #0x10a96dc
// 0x10a9200: fneg s0, s2
// 0x10a9204: fcmp s1, s0
// 0x10a9208: b.pl #0x10a9214
// 0x10a920c: mov w8, #4
// 0x10a9210: b #0x10a96dc
// 0x10a9214: ldr s1, [x19, #0x144]
// 0x10a9218: ldrb w9, [x19, #0x2ec]
// 0x10a921c: fcmp s1, s2
// 0x10a9220: b.le #0x10a922c
// 0x10a9224: cbnz w9, #0x10a924c
// 0x10a9228: b #0x10a9254
// 0x10a922c: cbz w9, #0x10a963c
// 0x10a9230: ldr x9, [x20]
// 0x10a9234: cbz x9, #0x10ac1ec
// 0x10a9238: ldrb w9, [x9, #0x1f8]
// 0x10a923c: cmp w8, #0
// 0x10a9240: cset w8, ne
// 0x10a9244: cbz w9, #0x10a9658
// 0x10a9248: tbnz w8, #0, #0x10a9658
// 0x10a924c: mov w8, #0x3f000000
// 0x10a9250: str w8, [x19, #0x20c]
// 0x10a9254: mov w8, #3
// 0x10a9258: b #0x10a96dc
// 0x10a925c: ldrb w9, [x8, #0x2dc]
// 0x10a9260: cbnz w9, #0x10a926c
// 0x10a9264: ldrb w9, [x8, #0x258]
// 0x10a9268: cbz w9, #0x10a99d8
// 0x10a926c: ldr s9, [x19, #0x1ec]
// 0x10a9270: mov x0, xzr
// 0x10a9274: bl #0x1b9ae30
// 0x10a9278: mov w8, #0x42c80000
// 0x10a927c: fmov s8, wzr
// 0x10a9280: fmov s1, w8
// 0x10a9284: fmul s2, s0, s1
// 0x10a9288: fnmul s0, s0, s1
// 0x10a928c: fsub s1, s8, s9
// 0x10a9290: fcmp s1, #0.0
// 0x10a9294: ldr s10, [x19, #0x1c8]
// 0x10a9298: ldr s11, [x19, #0x1c0]
// 0x10a929c: fabd s1, s8, s9
// 0x10a92a0: fcsel s0, s2, s0, ge
// 0x10a92a4: fadd s0, s9, s0
// 0x10a92a8: fcmp s1, s2
// 0x10a92ac: fcsel s0, s0, s8, hi
// 0x10a92b0: mov x0, xzr
// 0x10a92b4: str s0, [x19, #0x1ec]
// 0x10a92b8: bl #0x1b9ae30
// 0x10a92bc: fmov s1, #10.00000000
// 0x10a92c0: fsub s2, s11, s10
// 0x10a92c4: fmul s4, s0, s1
// 0x10a92c8: fnmul s0, s0, s1
// 0x10a92cc: fcmp s2, #0.0
// 0x10a92d0: fabd s3, s11, s10
// 0x10a92d4: ldr s9, [x19, #0x1b0]
// 0x10a92d8: ldr s12, [x19, #0x1a4]
// 0x10a92dc: fcsel s0, s4, s0, ge
// 0x10a92e0: fadd s0, s10, s0
// 0x10a92e4: fcmp s3, s4
// 0x10a92e8: fcsel s0, s0, s11, hi
// 0x10a92ec: mov x0, xzr
// 0x10a92f0: str s0, [x19, #0x1c8]
// 0x10a92f4: bl #0x1b9ae30
// 0x10a92f8: mov w8, #0x42000000
// 0x10a92fc: fsub s1, s12, s9
// 0x10a9300: fmov s3, w8
// 0x10a9304: fmul s4, s0, s3
// 0x10a9308: fnmul s0, s0, s3
// 0x10a930c: fcmp s1, #0.0
// 0x10a9310: fabd s2, s12, s9
// 0x10a9314: ldr s10, [x19, #0x1e4]
// 0x10a9318: ldr s11, [x19, #0x1d0]
// 0x10a931c: fcsel s0, s4, s0, ge
// 0x10a9320: fadd s0, s9, s0
// 0x10a9324: fcmp s2, s4
// 0x10a9328: fcsel s0, s0, s12, hi
// 0x10a932c: mov x0, xzr
// 0x10a9330: str s0, [x19, #0x1b0]
// 0x10a9334: bl #0x1b9ae30
// 0x10a9338: fmov s1, #8.00000000
// 0x10a933c: fsub s2, s11, s10
// 0x10a9340: fmul s4, s0, s1
// 0x10a9344: fnmul s0, s0, s1
// 0x10a9348: fcmp s2, #0.0
// 0x10a934c: fabd s3, s11, s10
// 0x10a9350: ldr s9, [x19, #0x188]
// 0x10a9354: ldr s12, [x19, #0x180]
// 0x10a9358: fcsel s0, s4, s0, ge
// 0x10a935c: fadd s0, s10, s0
// 0x10a9360: fcmp s3, s4
// 0x10a9364: fcsel s0, s0, s11, hi
// 0x10a9368: mov x0, xzr
// 0x10a936c: str s0, [x19, #0x1e4]
// 0x10a9370: bl #0x1b9ae30
// 0x10a9374: fsub s1, s12, s9
// 0x10a9378: fneg s3, s0
// 0x10a937c: fcmp s1, #0.0
// 0x10a9380: fabd s2, s12, s9
// 0x10a9384: ldr s10, [x19, #0x1cc]
// 0x10a9388: fcsel s1, s0, s3, ge
// 0x10a938c: fadd s1, s9, s1
// 0x10a9390: fcmp s2, s0
// 0x10a9394: fcsel s0, s1, s12, hi
// 0x10a9398: mov x0, xzr
// 0x10a939c: str s0, [x19, #0x188]
// 0x10a93a0: bl #0x1b9ae30
// 0x10a93a4: fmov s1, #7.00000000
// 0x10a93a8: fmov s2, #1.00000000
// 0x10a93ac: fmul s0, s0, s1
// 0x10a93b0: fmin s1, s0, s2
// 0x10a93b4: fcmp s0, #0.0
// 0x10a93b8: fcsel s0, s1, s8, pl
// 0x10a93bc: fsub s1, s8, s10
// 0x10a93c0: fmul s0, s1, s0
// 0x10a93c4: fadd s0, s10, s0
// 0x10a93c8: str s0, [x19, #0x1cc]
// 0x10a93cc: ldr x0, [x19, #0xa0]
// 0x10a93d0: cbz x0, #0x10ac1ec
// 0x10a93d4: ldr s0, [x19, #0x188]
// 0x10a93d8: mov x1, xzr
// 0x10a93dc: mov v1.16b, v0.16b
// 0x10a93e0: mov v2.16b, v0.16b
// 0x10a93e4: bl #0x1b9dbe0
// 0x10a93e8: ldr x0, [x19, #0x50]
// 0x10a93ec: cbz x0, #0x10ac1ec
// 0x10a93f0: mov x1, xzr
// 0x10a93f4: bl #0x1b9d508
// 0x10a93f8: ldr x0, [x19, #0x50]
// 0x10a93fc: cbz x0, #0x10ac1ec
// 0x10a9400: mov x1, xzr
// 0x10a9404: mov v8.16b, v0.16b
// 0x10a9408: bl #0x1b9d508
// 0x10a940c: ldr x0, [x19, #0x50]
// 0x10a9410: cbz x0, #0x10ac1ec
// 0x10a9414: ldr s11, [x19, #0x1e4]
// 0x10a9418: mov x1, xzr
// 0x10a941c: mov v9.16b, v1.16b
// 0x10a9420: bl #0x1b9d508
// 0x10a9424: fsub s9, s9, s11
// 0x10a9428: ldr s11, [x19, #0x168]
// 0x10a942c: ldr s12, [x19, #0x16c]
// 0x10a9430: ldr s13, [x19, #0x170]
// 0x10a9434: ldr s14, [x19, #0x314]
// 0x10a9438: mov x0, xzr
// 0x10a943c: mov v10.16b, v2.16b
// 0x10a9440: str s8, [x19, #0x174]
// 0x10a9444: str s9, [x19, #0x178]
// 0x10a9448: str s2, [x19, #0x17c]
// 0x10a944c: add x21, x19, #0x15c
// 0x10a9450: bl #0x1b9ae30
// 0x10a9454: mov w8, #0x7f800000
// 0x10a9458: str s0, [sp]
// 0x10a945c: fmov s7, w8
// 0x10a9460: mov v0.16b, v11.16b
// 0x10a9464: mov v1.16b, v12.16b
// 0x10a9468: mov v2.16b, v13.16b
// 0x10a946c: mov v3.16b, v8.16b
// 0x10a9470: mov v4.16b, v9.16b
// 0x10a9474: mov v5.16b, v10.16b
// 0x10a9478: mov x0, x21
// 0x10a947c: mov v6.16b, v14.16b
// 0x10a9480: mov x1, xzr
// 0x10a9484: bl #0x1b89b88
// 0x10a9488: ldr x0, [x19, #0x50]
// 0x10a948c: str s0, [x19, #0x168]
// 0x10a9490: str s1, [x19, #0x16c]
// 0x10a9494: str s2, [x19, #0x170]
// 0x10a9498: cbz x0, #0x10ac1ec
// 0x10a949c: ldr x21, [x19, #0xa0]
// 0x10a94a0: mov x1, xzr
// 0x10a94a4: mov v8.16b, v0.16b
// 0x10a94a8: mov v9.16b, v1.16b
// 0x10a94ac: mov v10.16b, v2.16b
// 0x10a94b0: bl #0x1b9d9b8
// 0x10a94b4: ldr x0, [x19, #0x50]
// 0x10a94b8: cbz x0, #0x10ac1ec
// 0x10a94bc: ldr s14, [x19, #0x1c8]
// 0x10a94c0: mov x1, xzr
// 0x10a94c4: mov v11.16b, v0.16b
// 0x10a94c8: mov v12.16b, v1.16b
// 0x10a94cc: mov v13.16b, v2.16b
// 0x10a94d0: bl #0x1b9d8c8
// 0x10a94d4: cbz x21, #0x10ac1ec
// 0x10a94d8: ldr s3, [x19, #0x1cc]
// 0x10a94dc: fmul s4, s13, s14
// 0x10a94e0: fmul s5, s12, s14
// 0x10a94e4: fmul s6, s11, s14
// 0x10a94e8: fadd s4, s10, s4
// 0x10a94ec: fadd s5, s9, s5
// 0x10a94f0: fadd s6, s8, s6
// 0x10a94f4: fmul s2, s2, s3
// 0x10a94f8: fmul s1, s1, s3
// 0x10a94fc: fmul s0, s0, s3
// 0x10a9500: fadd s2, s4, s2
// 0x10a9504: fadd s1, s5, s1
// 0x10a9508: fadd s0, s6, s0
// 0x10a950c: mov x0, x21
// 0x10a9510: mov x1, xzr
// 0x10a9514: bl #0x1b9d5a8
// 0x10a9518: ldr x0, [x19, #0x50]
// 0x10a951c: cbz x0, #0x10ac1ec
// 0x10a9520: ldr s8, [x19, #0x1b0]
// 0x10a9524: ldr s9, [x19, #0x158]
// 0x10a9528: ldr s10, [x19, #0x110]
// 0x10a952c: mov x1, xzr
// 0x10a9530: bl #0x1b9d6c8
// 0x10a9534: ldr s0, [x19, #0x1ec]
// 0x10a9538: ldr x0, [x19, #0xa0]
// 0x10a953c: fadd s2, s9, s10
// 0x10a9540: fadd s1, s2, s1
// 0x10a9544: fadd s1, s0, s1
// 0x10a9548: str s8, [x19, #0x118]
// 0x10a954c: str s1, [x19, #0x11c]
// 0x10a9550: str wzr, [x19, #0x120]
// 0x10a9554: cbz x0, #0x10ac1ec
// 0x10a9558: fmov s2, wzr
// 0x10a955c: mov v0.16b, v8.16b
// 0x10a9560: mov x1, xzr
// 0x10a9564: bl #0x1b9d748
// 0x10a9568: ldr s8, [x19, #0x310]
// 0x10a956c: mov x0, xzr
// 0x10a9570: bl #0x1b9ad30
// 0x10a9574: adrp x8, #0x831000
// 0x10a9578: ldr d1, [x8, #0xfb8]
// 0x10a957c: fcvt d2, s8
// 0x10a9580: fcvt d0, s0
// 0x10a9584: fadd d1, d2, d1
// 0x10a9588: fcmp d1, d0
// 0x10a958c: b.mi #0x10a95a0
// 0x10a9590: ldr x8, [x19, #0x68]
// 0x10a9594: cbz x8, #0x10ac1ec
// 0x10a9598: ldrb w8, [x8, #0x2b1]
// 0x10a959c: cbz w8, #0x10a9648
// 0x10a95a0: ldr x0, [x19, #0xd0]
// 0x10a95a4: cbz x0, #0x10ac1ec
// 0x10a95a8: mov w1, #1
// 0x10a95ac: mov x2, xzr
// 0x10a95b0: bl #0x1b799d0
// 0x10a95b4: ldr x8, [x19, #0x80]
// 0x10a95b8: cbz x8, #0x10ac1ec
// 0x10a95bc: ldr s0, [x8, #0x118]
// 0x10a95c0: str s0, [x19, #0x314]
// 0x10a95c4: b #0x10a8950
// 0x10a95c8: ldr x8, [x19, #0x78]
// 0x10a95cc: cbz x8, #0x10ac1ec
// 0x10a95d0: ldr s8, [x19, #0x1f0]
// 0x10a95d4: ldr s10, [x8, #0x7c]
// 0x10a95d8: mov x0, xzr
// 0x10a95dc: bl #0x1b9ae30
// 0x10a95e0: fmov s1, #10.00000000
// 0x10a95e4: fmov s2, #1.00000000
// 0x10a95e8: fmul s0, s0, s1
// 0x10a95ec: fmov s3, wzr
// 0x10a95f0: fmin s1, s0, s2
// 0x10a95f4: fcmp s0, #0.0
// 0x10a95f8: fcsel s0, s1, s3, pl
// 0x10a95fc: fsub s1, s10, s8
// 0x10a9600: fmul s0, s1, s0
// 0x10a9604: fadd s0, s8, s0
// 0x10a9608: str s0, [x19, #0x1f0]
// 0x10a960c: b #0x10a9128
// 0x10a9610: ldrb w8, [x8, #0x2e8]
// 0x10a9614: cbz w8, #0x10a8a98
// 0x10a9618: ldr w8, [x19, #0x22c]
// 0x10a961c: and w8, w8, #0xfffffffe
// 0x10a9620: cmp w8, #2
// 0x10a9624: b.ne #0x10a8a98
// 0x10a9628: ldr s8, [x19, #0x1ec]
// 0x10a962c: ldr s9, [x19, #0x19c]
// 0x10a9630: mov x0, xzr
// 0x10a9634: bl #0x1b9ae30
// 0x10a9638: b #0x10a8aa8
// 0x10a963c: fcmp s1, s0
// 0x10a9640: b.pl #0x10a9670
// 0x10a9644: b #0x10a96d8
// 0x10a9648: mov w8, #0xb717
// 0x10a964c: movk w8, #0x38d1, lsl #16
// 0x10a9650: str w8, [x19, #0x314]
// 0x10a9654: b #0x10a8950
// 0x10a9658: cmp w9, #0
// 0x10a965c: cset w9, ne
// 0x10a9660: fcmp s1, s0
// 0x10a9664: b.mi #0x10a96cc
// 0x10a9668: orr w8, w9, w8
// 0x10a966c: tbz w8, #0, #0x10a96cc
// 0x10a9670: ldr s8, [x19, #0x140]
// 0x10a9674: mov x0, xzr
// 0x10a9678: bl #0x1b9ad30
// 0x10a967c: adrp x8, #0x832000
// 0x10a9680: ldr s1, [x8, #0x330]
// 0x10a9684: fadd s1, s8, s1
// 0x10a9688: fcmp s1, s0
// 0x10a968c: b.pl #0x10ac144
// 0x10a9690: ldr x8, [x22]
// 0x10a9694: cbz x8, #0x10ac1ec
// 0x10a9698: ldrb w8, [x8, #0x258]
// 0x10a969c: cbz w8, #0x10a9a6c
// 0x10a96a0: ldr x8, [x19, #0x60]
// 0x10a96a4: cbz x8, #0x10ac1ec
// 0x10a96a8: ldrb w9, [x8, #0x8d]
// 0x10a96ac: cbnz w9, #0x10a96b8
// 0x10a96b0: ldrb w8, [x8, #0x8f]
// 0x10a96b4: cbz w8, #0x10a9a6c
// 0x10a96b8: mov w8, #1
// 0x10a96bc: mov w9, #0x3f800000
// 0x10a96c0: str w8, [x19, #0x22c]
// 0x10a96c4: str w9, [x19, #0x20c]
// 0x10a96c8: b #0x10a96e0
// 0x10a96cc: mov w8, #0xcccd
// 0x10a96d0: movk w8, #0xbecc, lsl #16
// 0x10a96d4: str w8, [x19, #0x20c]
// 0x10a96d8: mov w8, #2
// 0x10a96dc: str w8, [x19, #0x22c]
// 0x10a96e0: ldr x0, [x19, #0x20]
// 0x10a96e4: cbz x0, #0x10ac1ec
// 0x10a96e8: adrp x21, #0x1e8e000
// 0x10a96ec: ldr w2, [x19, #0x22c]
// 0x10a96f0: ldr x21, [x21, #0x5a0]
// 0x10a96f4: mov x3, xzr
// 0x10a96f8: ldr x1, [x21]
// 0x10a96fc: bl #0x1b67734
// 0x10a9700: ldr x0, [x19, #0xc8]
// 0x10a9704: cbz x0, #0x10ac1ec
// 0x10a9708: ldr w2, [x19, #0x22c]
// 0x10a970c: ldr x1, [x21]
// 0x10a9710: mov x3, xzr
// 0x10a9714: bl #0x1b67734
// 0x10a9718: ldr x8, [x19, #0x68]
// 0x10a971c: cbz x8, #0x10ac1ec
// 0x10a9720: ldrb w9, [x8, #0x228]
// 0x10a9724: cbz w9, #0x10a9798
// 0x10a9728: ldrb w9, [x8, #0x2dc]
// 0x10a972c: ldrb w8, [x19, #0x218]
// 0x10a9730: cbz w9, #0x10a9740
// 0x10a9734: cbz w8, #0x10a975c
// 0x10a9738: ldr s10, [x19, #0x21c]
// 0x10a973c: b #0x10a9774
// 0x10a9740: cbz w8, #0x10a98d4
// 0x10a9744: mov x0, xzr
// 0x10a9748: bl #0x1b9ad30
// 0x10a974c: mov v10.16b, v0.16b
// 0x10a9750: str s0, [x19, #0x21c]
// 0x10a9754: strb wzr, [x19, #0x218]
// 0x10a9758: b #0x10a98d8
// 0x10a975c: mov x0, xzr
// 0x10a9760: bl #0x1b9ad30
// 0x10a9764: mov v10.16b, v0.16b
// 0x10a9768: mov w8, #1
// 0x10a976c: str s0, [x19, #0x21c]
// 0x10a9770: strb w8, [x19, #0x218]
// 0x10a9774: ldr s8, [x19, #0x224]
// 0x10a9778: mov x0, xzr
// 0x10a977c: bl #0x1b9ad30
// 0x10a9780: fadd s1, s10, s8
// 0x10a9784: fcmp s1, s0
// 0x10a9788: b.le #0x10a9798
// 0x10a978c: mov w8, #1
// 0x10a9790: str w8, [x19, #0x220]
// 0x10a9794: b #0x10a979c
// 0x10a9798: str wzr, [x19, #0x220]
// 0x10a979c: ldr x8, [x19, #0x90]
// 0x10a97a0: cbz x8, #0x10ac1ec
// 0x10a97a4: ldr w2, [x19, #0x220]
// 0x10a97a8: cmp w2, #0
// 0x10a97ac: cset w9, ne
// 0x10a97b0: strb w9, [x8, #0x4aa]
// 0x10a97b4: ldr x0, [x19, #0x20]
// 0x10a97b8: cbz x0, #0x10ac1ec
// 0x10a97bc: adrp x21, #0x1e8e000
// 0x10a97c0: ldr x21, [x21, #0x5c0]
// 0x10a97c4: mov x3, xzr
// 0x10a97c8: ldr x1, [x21]
// 0x10a97cc: bl #0x1b67734
// 0x10a97d0: ldr x0, [x19, #0xc8]
// 0x10a97d4: cbz x0, #0x10ac1ec
// 0x10a97d8: ldr w2, [x19, #0x220]
// 0x10a97dc: ldr x1, [x21]
// 0x10a97e0: mov x3, xzr
// 0x10a97e4: bl #0x1b67734
// 0x10a97e8: ldr x8, [x19, #0x70]
// 0x10a97ec: cbz x8, #0x10ac1ec
// 0x10a97f0: ldr s0, [x8, #0x20c]
// 0x10a97f4: fcmp s0, #0.0
// 0x10a97f8: b.ge #0x10a9808
// 0x10a97fc: mov w8, #7
// 0x10a9800: str w8, [x19, #0x230]
// 0x10a9804: b #0x10a9ad8
// 0x10a9808: ldr w9, [x19, #0x220]
// 0x10a980c: cbnz w9, #0x10a9ad8
// 0x10a9810: ldr x9, [x22]
// 0x10a9814: cbz x9, #0x10ac1ec
// 0x10a9818: ldrb w10, [x9, #0x228]
// 0x10a981c: cbz w10, #0x10a9920
// 0x10a9820: ldrb w10, [x9, #0x2b1]
// 0x10a9824: cbz w10, #0x10a9910
// 0x10a9828: ldr x10, [x19, #0x60]
// 0x10a982c: cbz x10, #0x10ac1ec
// 0x10a9830: ldr s1, [x19, #0x20c]
// 0x10a9834: ldr s0, [x10, #0xc8]
// 0x10a9838: fcmp s1, s0
// 0x10a983c: b.le #0x10a9910
// 0x10a9840: ldr s2, [x19, #0x148]
// 0x10a9844: fabs s1, s1
// 0x10a9848: fmov s3, #-0.50000000
// 0x10a984c: fneg s4, s1
// 0x10a9850: fcmp s2, s3
// 0x10a9854: fabs s2, s2
// 0x10a9858: fcsel s1, s1, s4, gt
// 0x10a985c: fcmp s2, s0
// 0x10a9860: str s1, [x19, #0x20c]
// 0x10a9864: b.ge #0x10a9878
// 0x10a9868: ldr s1, [x23]
// 0x10a986c: fabs s1, s1
// 0x10a9870: fcmp s1, s0
// 0x10a9874: b.lt #0x10a98c8
// 0x10a9878: mov w8, #1
// 0x10a987c: mov x0, xzr
// 0x10a9880: str w8, [x19, #0x230]
// 0x10a9884: bl #0x1b9ad30
// 0x10a9888: ldr s8, [x19, #0x1c8]
// 0x10a988c: ldr s9, [x19, #0x1b8]
// 0x10a9890: mov x0, xzr
// 0x10a9894: str s0, [x19, #0x210]
// 0x10a9898: bl #0x1b9ae30
// 0x10a989c: fmov s1, #7.00000000
// 0x10a98a0: fmov s2, #1.00000000
// 0x10a98a4: fmul s0, s0, s1
// 0x10a98a8: fmov s3, wzr
// 0x10a98ac: fmin s1, s0, s2
// 0x10a98b0: fcmp s0, #0.0
// 0x10a98b4: fcsel s0, s1, s3, pl
// 0x10a98b8: fsub s1, s9, s8
// 0x10a98bc: fmul s0, s1, s0
// 0x10a98c0: fadd s0, s8, s0
// 0x10a98c4: str s0, [x19, #0x1c8]
// 0x10a98c8: mov w8, #-0x3e800000
// 0x10a98cc: str w8, [x19, #0x200]
// 0x10a98d0: b #0x10a9ad8
// 0x10a98d4: ldr s10, [x19, #0x21c]
// 0x10a98d8: ldr s8, [x19, #0x224]
// 0x10a98dc: mov x0, xzr
// 0x10a98e0: bl #0x1b9ad30
// 0x10a98e4: fadd s1, s10, s8
// 0x10a98e8: fcmp s1, s0
// 0x10a98ec: b.le #0x10a9908
// 0x10a98f0: ldr x8, [x22]
// 0x10a98f4: cbz x8, #0x10ac1ec
// 0x10a98f8: ldrb w8, [x8, #0x2d0]
// 0x10a98fc: cbz w8, #0x10a9928
// 0x10a9900: mov w8, #3
// 0x10a9904: b #0x10a992c
// 0x10a9908: str wzr, [x19, #0x220]
// 0x10a990c: b #0x10a9930
// 0x10a9910: ldrb w10, [x9, #0x2d0]
// 0x10a9914: cbz w10, #0x10a9970
// 0x10a9918: mov w8, #2
// 0x10a991c: b #0x10a9a98
// 0x10a9920: mov w8, #3
// 0x10a9924: b #0x10a9800
// 0x10a9928: mov w8, #2
// 0x10a992c: str w8, [x19, #0x220]
// 0x10a9930: ldr s8, [x19, #0x21c]
// 0x10a9934: ldr s10, [x19, #0x224]
// 0x10a9938: mov x0, xzr
// 0x10a993c: bl #0x1b9ad30
// 0x10a9940: adrp x8, #0x832000
// 0x10a9944: ldr s1, [x8, #0x390]
// 0x10a9948: fmul s1, s10, s1
// 0x10a994c: fadd s1, s8, s1
// 0x10a9950: fcmp s1, s0
// 0x10a9954: b.pl #0x10a979c
// 0x10a9958: ldr x8, [x22]
// 0x10a995c: cbz x8, #0x10ac1ec
// 0x10a9960: ldrb w8, [x8, #0x2d0]
// 0x10a9964: cbnz w8, #0x10a979c
// 0x10a9968: str wzr, [x19, #0x230]
// 0x10a996c: b #0x10a979c
// 0x10a9970: ldrb w10, [x9, #0x258]
// 0x10a9974: cbz w10, #0x10a9a5c
// 0x10a9978: ldrb w8, [x8, #0x2d0]
// 0x10a997c: cbnz w8, #0x10a99b4
// 0x10a9980: ldr s8, [x19, #0x200]
// 0x10a9984: ldr s10, [x19, #0x204]
// 0x10a9988: mov x0, xzr
// 0x10a998c: bl #0x1b9ad30
// 0x10a9990: fmul s1, s10, s9
// 0x10a9994: fadd s1, s8, s1
// 0x10a9998: fcmp s1, s0
// 0x10a999c: b.pl #0x10a99b4
// 0x10a99a0: ldr x8, [x20]
// 0x10a99a4: cbz x8, #0x10ac1ec
// 0x10a99a8: ldr w8, [x8, #0x368]
// 0x10a99ac: cmp w8, #6
// 0x10a99b0: b.ne #0x10a9a94
// 0x10a99b4: ldr x8, [x20]
// 0x10a99b8: cbz x8, #0x10ac1ec
// 0x10a99bc: ldr w9, [x8, #0x368]
// 0x10a99c0: cmp w9, #6
// 0x10a99c4: b.ne #0x10a99d0
// 0x10a99c8: ldrb w8, [x8, #0x1d4]
// 0x10a99cc: cbz w8, #0x10a9a94
// 0x10a99d0: mov w8, #5
// 0x10a99d4: b #0x10a9a98
// 0x10a99d8: ldrb w9, [x8, #0x2b1]
// 0x10a99dc: cbz w9, #0x10a9de8
// 0x10a99e0: ldr s8, [x19, #0x1ec]
// 0x10a99e4: mov x0, xzr
// 0x10a99e8: bl #0x1b9ae30
// 0x10a99ec: mov w8, #0x42c80000
// 0x10a99f0: fmov s9, wzr
// 0x10a99f4: fmov s1, w8
// 0x10a99f8: ldr w8, [x19, #0x22c]
// 0x10a99fc: fsub s3, s9, s8
// 0x10a9a00: fmul s2, s0, s1
// 0x10a9a04: fnmul s0, s0, s1
// 0x10a9a08: fcmp s3, #0.0
// 0x10a9a0c: fabd s4, s9, s8
// 0x10a9a10: fcsel s0, s2, s0, ge
// 0x10a9a14: fcmp s4, s2
// 0x10a9a18: fadd s0, s8, s0
// 0x10a9a1c: fcsel s0, s0, s9, hi
// 0x10a9a20: cmp w8, #2
// 0x10a9a24: str s0, [x19, #0x1ec]
// 0x10a9a28: b.ne #0x10a9f20
// 0x10a9a2c: ldr s8, [x19, #0x1cc]
// 0x10a9a30: ldr s10, [x19, #0x1c4]
// 0x10a9a34: mov x0, xzr
// 0x10a9a38: bl #0x1b9ae30
// 0x10a9a3c: fmov s1, #7.00000000
// 0x10a9a40: fmov s2, #1.00000000
// 0x10a9a44: fmul s0, s0, s1
// 0x10a9a48: fmin s1, s0, s2
// 0x10a9a4c: fcmp s0, #0.0
// 0x10a9a50: fcsel s0, s1, s9, pl
// 0x10a9a54: fsub s1, s10, s8
// 0x10a9a58: b #0x10abfac
// 0x10a9a5c: ldrb w8, [x9, #0x2dc]
// 0x10a9a60: cbz w8, #0x10a9f18
// 0x10a9a64: mov w8, #6
// 0x10a9a68: b #0x10a9a98
// 0x10a9a6c: ldr x8, [x19, #0x80]
// 0x10a9a70: cbz x8, #0x10ac1ec
// 0x10a9a74: ldrb w8, [x8, #0x106]
// 0x10a9a78: ldr s0, [x19, #0x1f0]
// 0x10a9a7c: cbz w8, #0x10a9f60
// 0x10a9a80: fmov s1, #16.00000000
// 0x10a9a84: fcmp s0, s1
// 0x10a9a88: b.gt #0x10a9f68
// 0x10a9a8c: fmov s1, #-16.00000000
// 0x10a9a90: b #0x10ac0a8
// 0x10a9a94: mov w8, #4
// 0x10a9a98: str w8, [x19, #0x230]
// 0x10a9a9c: ldr s8, [x19, #0x1c8]
// 0x10a9aa0: ldr s9, [x19, #0x1b4]
// 0x10a9aa4: mov x0, xzr
// 0x10a9aa8: bl #0x1b9ae30
// 0x10a9aac: fmov s1, #7.00000000
// 0x10a9ab0: fmov s2, #1.00000000
// 0x10a9ab4: fmul s0, s0, s1
// 0x10a9ab8: fmov s3, wzr
// 0x10a9abc: fmin s1, s0, s2
// 0x10a9ac0: fcmp s0, #0.0
// 0x10a9ac4: fcsel s0, s1, s3, pl
// 0x10a9ac8: fsub s1, s9, s8
// 0x10a9acc: fmul s0, s1, s0
// 0x10a9ad0: fadd s0, s8, s0
// 0x10a9ad4: str s0, [x19, #0x1c8]
// 0x10a9ad8: ldr w8, [x19, #0x22c]
// 0x10a9adc: ldr s9, [x19, #0x2dc]
// 0x10a9ae0: fmov s8, #1.00000000
// 0x10a9ae4: fmov s10, wzr
// 0x10a9ae8: cmp w8, #0
// 0x10a9aec: fcsel s11, s10, s8, eq
// 0x10a9af0: mov x0, xzr
// 0x10a9af4: str s11, [x19, #0x2d8]
// 0x10a9af8: bl #0x1b89b60
// 0x10a9afc: fadd s0, s0, s0
// 0x10a9b00: ldr x0, [x19, #0x20]
// 0x10a9b04: fmin s1, s0, s8
// 0x10a9b08: fcmp s0, #0.0
// 0x10a9b0c: fcsel s0, s1, s10, pl
// 0x10a9b10: fsub s1, s11, s9
// 0x10a9b14: fmul s0, s1, s0
// 0x10a9b18: fadd s0, s9, s0
// 0x10a9b1c: str s0, [x19, #0x2dc]
// 0x10a9b20: cbz x0, #0x10ac1ec
// 0x10a9b24: adrp x21, #0x1e8e000
// 0x10a9b28: ldr x21, [x21, #0x5b8]
// 0x10a9b2c: mov x2, xzr
// 0x10a9b30: ldr x1, [x21]
// 0x10a9b34: bl #0x1b673dc
// 0x10a9b38: ldr x0, [x19, #0xc8]
// 0x10a9b3c: cbz x0, #0x10ac1ec
// 0x10a9b40: ldr s0, [x19, #0x2dc]
// 0x10a9b44: ldr x1, [x21]
// 0x10a9b48: mov x2, xzr
// 0x10a9b4c: bl #0x1b673dc
// 0x10a9b50: ldr x0, [x19, #0x20]
// 0x10a9b54: cbz x0, #0x10ac1ec
// 0x10a9b58: adrp x21, #0x1e8e000
// 0x10a9b5c: ldr w2, [x19, #0x230]
// 0x10a9b60: ldr x21, [x21, #0x588]
// 0x10a9b64: mov x3, xzr
// 0x10a9b68: ldr x1, [x21]
// 0x10a9b6c: bl #0x1b67734
// 0x10a9b70: ldr x0, [x19, #0xc8]
// 0x10a9b74: cbz x0, #0x10ac1ec
// 0x10a9b78: ldr w2, [x19, #0x230]
// 0x10a9b7c: ldr x1, [x21]
// 0x10a9b80: mov x3, xzr
// 0x10a9b84: bl #0x1b67734
// 0x10a9b88: ldr x8, [x19, #0x90]
// 0x10a9b8c: cbz x8, #0x10ac1ec
// 0x10a9b90: ldr w8, [x8, #0x368]
// 0x10a9b94: cbnz w8, #0x10a9bb8
// 0x10a9b98: ldr s0, [x19, #0x20c]
// 0x10a9b9c: ldr s1, [x19, #0x148]
// 0x10a9ba0: fmov s2, #-0.50000000
// 0x10a9ba4: fabs s0, s0
// 0x10a9ba8: fneg s3, s0
// 0x10a9bac: fcmp s1, s2
// 0x10a9bb0: fcsel s0, s0, s3, gt
// 0x10a9bb4: str s0, [x19, #0x20c]
// 0x10a9bb8: ldr x8, [x19, #0x70]
// 0x10a9bbc: cbz x8, #0x10ac1ec
// 0x10a9bc0: ldr x0, [x19, #0x20]
// 0x10a9bc4: cbz x0, #0x10ac1ec
// 0x10a9bc8: adrp x21, #0x1e8e000
// 0x10a9bcc: ldr s0, [x19, #0x20c]
// 0x10a9bd0: ldrb w8, [x8, #0x2d0]
// 0x10a9bd4: ldr x21, [x21, #0x568]
// 0x10a9bd8: ldr x1, [x21]
// 0x10a9bdc: cbz w8, #0x10a9c0c
// 0x10a9be0: adrp x8, #0x832000
// 0x10a9be4: ldr s9, [x8, #0x4a0]
// 0x10a9be8: mov x2, xzr
// 0x10a9bec: fmul s0, s0, s9
// 0x10a9bf0: bl #0x1b673dc
// 0x10a9bf4: ldr x0, [x19, #0xc8]
// 0x10a9bf8: cbz x0, #0x10ac1ec
// 0x10a9bfc: ldr s0, [x19, #0x20c]
// 0x10a9c00: ldr x1, [x21]
// 0x10a9c04: fmul s0, s0, s9
// 0x10a9c08: b #0x10a9c24
// 0x10a9c0c: mov x2, xzr
// 0x10a9c10: bl #0x1b673dc
// 0x10a9c14: ldr x0, [x19, #0xc8]
// 0x10a9c18: cbz x0, #0x10ac1ec
// 0x10a9c1c: ldr s0, [x19, #0x20c]
// 0x10a9c20: ldr x1, [x21]
// 0x10a9c24: mov x2, xzr
// 0x10a9c28: bl #0x1b673dc
// 0x10a9c2c: ldr x8, [x20]
// 0x10a9c30: cbz x8, #0x10ac1ec
// 0x10a9c34: ldr x0, [x19, #0x20]
// 0x10a9c38: cbz x0, #0x10ac1ec
// 0x10a9c3c: ldrb w2, [x8, #0x36c]
// 0x10a9c40: adrp x8, #0x1e8e000
// 0x10a9c44: ldr x8, [x8, #0x578]
// 0x10a9c48: mov x3, xzr
// 0x10a9c4c: ldr x1, [x8]
// 0x10a9c50: bl #0x1b675e4
// 0x10a9c54: ldr x8, [x20]
// 0x10a9c58: cbz x8, #0x10ac1ec
// 0x10a9c5c: ldr x0, [x19, #0x20]
// 0x10a9c60: cbz x0, #0x10ac1ec
// 0x10a9c64: ldrb w2, [x8, #0x36d]
// 0x10a9c68: adrp x8, #0x1e8e000
// 0x10a9c6c: ldr x8, [x8, #0x580]
// 0x10a9c70: mov x3, xzr
// 0x10a9c74: ldr x1, [x8]
// 0x10a9c78: bl #0x1b675e4
// 0x10a9c7c: ldr x8, [x19, #0x70]
// 0x10a9c80: cbz x8, #0x10ac1ec
// 0x10a9c84: ldrb w8, [x8, #0x2d0]
// 0x10a9c88: cbnz w8, #0x10a9cc0
// 0x10a9c8c: ldr s8, [x19, #0x200]
// 0x10a9c90: ldr s9, [x19, #0x204]
// 0x10a9c94: ldr s10, [x19, #0x2f0]
// 0x10a9c98: mov x0, xzr
// 0x10a9c9c: bl #0x1b9ad30
// 0x10a9ca0: fmul s1, s9, s10
// 0x10a9ca4: fadd s1, s8, s1
// 0x10a9ca8: fcmp s1, s0
// 0x10a9cac: b.pl #0x10a9cc0
// 0x10a9cb0: ldr x8, [x20]
// 0x10a9cb4: cbz x8, #0x10ac1ec
// 0x10a9cb8: ldrb w8, [x8, #0x229]
// 0x10a9cbc: cbz w8, #0x10a9d34
// 0x10a9cc0: ldr x8, [x22]
// 0x10a9cc4: cbz x8, #0x10ac1ec
// 0x10a9cc8: ldrb w9, [x8, #0x2b1]
// 0x10a9ccc: cbz w9, #0x10a9cfc
// 0x10a9cd0: ldr s8, [x19, #0x200]
// 0x10a9cd4: ldr s9, [x19, #0x204]
// 0x10a9cd8: ldr s10, [x19, #0x2f0]
// 0x10a9cdc: mov x0, xzr
// 0x10a9ce0: bl #0x1b9ad30
// 0x10a9ce4: fmul s1, s9, s10
// 0x10a9ce8: fadd s1, s8, s1
// 0x10a9cec: fcmp s1, s0
// 0x10a9cf0: b.mi #0x10a9d34
// 0x10a9cf4: ldr x8, [x22]
// 0x10a9cf8: cbz x8, #0x10ac1ec
// 0x10a9cfc: ldrb w9, [x8, #0x258]
// 0x10a9d00: cbz w9, #0x10a9d10
// 0x10a9d04: ldr w9, [x19, #0x230]
// 0x10a9d08: cmp w9, #5
// 0x10a9d0c: b.ne #0x10a9d34
// 0x10a9d10: ldr x9, [x20]
// 0x10a9d14: cbz x9, #0x10ac1ec
// 0x10a9d18: ldr w9, [x9, #0x368]
// 0x10a9d1c: fmov s9, wzr
// 0x10a9d20: cbnz w9, #0x10a9ff4
// 0x10a9d24: ldrb w9, [x8, #0x2d0]
// 0x10a9d28: cbnz w9, #0x10a9d34
// 0x10a9d2c: ldrb w8, [x8, #0x2e8]
// 0x10a9d30: cbz w8, #0x10a9ff4
// 0x10a9d34: ldr x8, [x19, #0x98]
// 0x10a9d38: cbz x8, #0x10ac1ec
// 0x10a9d3c: ldrb w8, [x8, #0x17e]
// 0x10a9d40: fmov s9, wzr
// 0x10a9d44: cbnz w8, #0x10a9ff4
// 0x10a9d48: ldr x8, [x20]
// 0x10a9d4c: cbz x8, #0x10ac1ec
// 0x10a9d50: ldrb w9, [x8, #0x1d4]
// 0x10a9d54: cbnz w9, #0x10a9ff4
// 0x10a9d58: ldr x9, [x19, #0x60]
// 0x10a9d5c: cbz x9, #0x10ac1ec
// 0x10a9d60: ldr s1, [x19, #0x148]
// 0x10a9d64: ldr s0, [x9, #0xc8]
// 0x10a9d68: fcmp s1, s0
// 0x10a9d6c: b.ge #0x10a9d8c
// 0x10a9d70: fmov s0, #-0.50000000
// 0x10a9d74: fcmp s1, s0
// 0x10a9d78: b.pl #0x10a9dbc
// 0x10a9d7c: ldr s0, [x23]
// 0x10a9d80: fneg s1, s1
// 0x10a9d84: fneg s0, s0
// 0x10a9d88: b #0x10a9fe4
// 0x10a9d8c: ldr x9, [x22]
// 0x10a9d90: cbz x9, #0x10ac1ec
// 0x10a9d94: ldrb w10, [x9, #0x2b1]
// 0x10a9d98: cbnz w10, #0x10a9fe0
// 0x10a9d9c: ldrb w10, [x9, #0x258]
// 0x10a9da0: cbnz w10, #0x10a9fe0
// 0x10a9da4: ldr w8, [x8, #0x368]
// 0x10a9da8: cbz w8, #0x10a9fd8
// 0x10a9dac: fmov s0, #0.50000000
// 0x10a9db0: fcmp s1, s0
// 0x10a9db4: b.gt #0x10a9fe0
// 0x10a9db8: b #0x10a9ff4
// 0x10a9dbc: ldr x9, [x22]
// 0x10a9dc0: cbz x9, #0x10ac1ec
// 0x10a9dc4: ldrb w10, [x9, #0x2b1]
// 0x10a9dc8: cbnz w10, #0x10a9fe0
// 0x10a9dcc: ldrb w10, [x9, #0x258]
// 0x10a9dd0: cbnz w10, #0x10a9fe0
// 0x10a9dd4: ldr w8, [x8, #0x368]
// 0x10a9dd8: cbnz w8, #0x10a9ff4
// 0x10a9ddc: ldrb w8, [x9, #0x2e8]
// 0x10a9de0: cbnz w8, #0x10a9fe0
// 0x10a9de4: b #0x10a9ff4
// 0x10a9de8: ldrb w8, [x8, #0x2e8]
// 0x10a9dec: cbz w8, #0x10ac14c
// 0x10a9df0: ldr s9, [x19, #0x1ec]
// 0x10a9df4: ldr s8, [x19, #0x190]
// 0x10a9df8: mov x0, xzr
// 0x10a9dfc: bl #0x1b9ae30
// 0x10a9e00: mov w8, #0x42c80000
// 0x10a9e04: fmov s1, w8
// 0x10a9e08: fmul s0, s0, s1
// 0x10a9e0c: fsub s1, s8, s9
// 0x10a9e10: fneg s3, s0
// 0x10a9e14: fcmp s1, #0.0
// 0x10a9e18: fabs s2, s1
// 0x10a9e1c: ldr s10, [x19, #0x1c8]
// 0x10a9e20: ldr s11, [x19, #0x1b4]
// 0x10a9e24: fcsel s1, s0, s3, ge
// 0x10a9e28: fadd s1, s9, s1
// 0x10a9e2c: fcmp s2, s0
// 0x10a9e30: fcsel s0, s1, s8, hi
// 0x10a9e34: mov x0, xzr
// 0x10a9e38: str s0, [x19, #0x1ec]
// 0x10a9e3c: bl #0x1b9ae30
// 0x10a9e40: fmov s8, #1.00000000
// 0x10a9e44: fcmp s0, #0.0
// 0x10a9e48: fmov s9, wzr
// 0x10a9e4c: fmin s0, s0, s8
// 0x10a9e50: fsub s1, s11, s10
// 0x10a9e54: ldr s11, [x19, #0x1b0]
// 0x10a9e58: fcsel s0, s0, s9, pl
// 0x10a9e5c: ldr s12, [x19, #0x1a4]
// 0x10a9e60: fmul s0, s1, s0
// 0x10a9e64: fadd s0, s10, s0
// 0x10a9e68: mov x0, xzr
// 0x10a9e6c: str s0, [x19, #0x1c8]
// 0x10a9e70: bl #0x1b9ae30
// 0x10a9e74: mov w8, #0x42000000
// 0x10a9e78: fsub s1, s12, s11
// 0x10a9e7c: fmov s3, w8
// 0x10a9e80: fmul s4, s0, s3
// 0x10a9e84: fnmul s0, s0, s3
// 0x10a9e88: fcmp s1, #0.0
// 0x10a9e8c: fabd s2, s12, s11
// 0x10a9e90: ldr s10, [x19, #0x1e4]
// 0x10a9e94: ldr s13, [x19, #0x1d0]
// 0x10a9e98: fcsel s0, s4, s0, ge
// 0x10a9e9c: fadd s0, s11, s0
// 0x10a9ea0: fcmp s2, s4
// 0x10a9ea4: fcsel s0, s0, s12, hi
// 0x10a9ea8: mov x0, xzr
// 0x10a9eac: str s0, [x19, #0x1b0]
// 0x10a9eb0: bl #0x1b9ae30
// 0x10a9eb4: fmov s1, #8.00000000
// 0x10a9eb8: fsub s2, s13, s10
// 0x10a9ebc: fmul s4, s0, s1
// 0x10a9ec0: fnmul s0, s0, s1
// 0x10a9ec4: fcmp s2, #0.0
// 0x10a9ec8: fabd s3, s13, s10
// 0x10a9ecc: ldr s11, [x19, #0x188]
// 0x10a9ed0: ldr s12, [x19, #0x180]
// 0x10a9ed4: fcsel s0, s4, s0, ge
// 0x10a9ed8: fadd s0, s10, s0
// 0x10a9edc: fcmp s3, s4
// 0x10a9ee0: fcsel s0, s0, s13, hi
// 0x10a9ee4: mov x0, xzr
// 0x10a9ee8: str s0, [x19, #0x1e4]
// 0x10a9eec: bl #0x1b9ae30
// 0x10a9ef0: fsub s1, s12, s11
// 0x10a9ef4: fneg s3, s0
// 0x10a9ef8: ldr s10, [x19, #0x1cc]
// 0x10a9efc: fcmp s1, #0.0
// 0x10a9f00: fabd s2, s12, s11
// 0x10a9f04: fcsel s1, s0, s3, ge
// 0x10a9f08: fadd s1, s11, s1
// 0x10a9f0c: fcmp s2, s0
// 0x10a9f10: fcsel s0, s1, s12, hi
// 0x10a9f14: b #0x10a8bd8
// 0x10a9f18: str wzr, [x19, #0x230]
// 0x10a9f1c: b #0x10a9a9c
// 0x10a9f20: ldr s8, [x19, #0x1cc]
// 0x10a9f24: cmp w8, #3
// 0x10a9f28: b.ne #0x10abf84
// 0x10a9f2c: ldr s9, [x19, #0x1c4]
// 0x10a9f30: mov x0, xzr
// 0x10a9f34: bl #0x1b9ae30
// 0x10a9f38: fmov s2, #7.00000000
// 0x10a9f3c: fmov s3, #1.00000000
// 0x10a9f40: fmul s0, s0, s2
// 0x10a9f44: fneg s1, s9
// 0x10a9f48: fmov s4, wzr
// 0x10a9f4c: fmin s2, s0, s3
// 0x10a9f50: fcmp s0, #0.0
// 0x10a9f54: fcsel s0, s2, s4, pl
// 0x10a9f58: fsub s1, s1, s8
// 0x10a9f5c: b #0x10abfac
// 0x10a9f60: fcmp s0, s9
// 0x10a9f64: b.le #0x10ac0a0
// 0x10a9f68: ldr x21, [x19, #0x20]
// 0x10a9f6c: mov x0, xzr
// 0x10a9f70: bl #0x1b89b60
// 0x10a9f74: cbz x21, #0x10ac1ec
// 0x10a9f78: adrp x25, #0x1e8e000
// 0x10a9f7c: ldr x25, [x25, #0x598]
// 0x10a9f80: ldr s10, [x24, #0x3a0]
// 0x10a9f84: mov v2.16b, v0.16b
// 0x10a9f88: fmov s0, #1.00000000
// 0x10a9f8c: ldr x1, [x25]
// 0x10a9f90: mov x0, x21
// 0x10a9f94: mov v1.16b, v10.16b
// 0x10a9f98: mov x2, xzr
// 0x10a9f9c: bl #0x1b67484
// 0x10a9fa0: ldr x21, [x19, #0xc8]
// 0x10a9fa4: mov x0, xzr
// 0x10a9fa8: bl #0x1b89b60
// 0x10a9fac: cbz x21, #0x10ac1ec
// 0x10a9fb0: ldr x1, [x25]
// 0x10a9fb4: mov v2.16b, v0.16b
// 0x10a9fb8: fmov s0, #1.00000000
// 0x10a9fbc: mov x0, x21
// 0x10a9fc0: mov v1.16b, v10.16b
// 0x10a9fc4: mov x2, xzr
// 0x10a9fc8: bl #0x1b67484
// 0x10a9fcc: ldr x8, [x19, #0x68]
// 0x10a9fd0: mov w9, #3
// 0x10a9fd4: b #0x10ac11c
// 0x10a9fd8: ldrb w8, [x9, #0x2e8]
// 0x10a9fdc: cbz w8, #0x10a9dac
// 0x10a9fe0: ldr s0, [x23]
// 0x10a9fe4: bl #0x1db0c90
// 0x10a9fe8: adrp x8, #0x832000
// 0x10a9fec: ldr s1, [x8, #0x554]
// 0x10a9ff0: fmul s9, s0, s1
// 0x10a9ff4: ldr s8, [x19, #0x110]
// 0x10a9ff8: mov x0, xzr
// 0x10a9ffc: str s9, [x19, #0x10c]
// 0x10aa000: bl #0x1b89b60
// 0x10aa004: mov w8, #0x43b40000
// 0x10aa008: fmov s1, #5.00000000
// 0x10aa00c: fsub s2, s9, s8
// 0x10aa010: fmov s3, w8
// 0x10aa014: mov w8, #-0x3c4c0000
// 0x10aa018: fmul s0, s0, s1
// 0x10aa01c: fdiv s1, s2, s3
// 0x10aa020: fmov s4, w8
// 0x10aa024: frintm s1, s1
// 0x10aa028: fmul s1, s1, s4
// 0x10aa02c: fadd s1, s2, s1
// 0x10aa030: fmov s2, wzr
// 0x10aa034: mov w8, #0x43340000
// 0x10aa038: fmin s3, s1, s3
// 0x10aa03c: fcmp s1, #0.0
// 0x10aa040: fmov s1, w8
// 0x10aa044: fcsel s3, s3, s2, pl
// 0x10aa048: fcmp s3, s1
// 0x10aa04c: fmov s1, #1.00000000
// 0x10aa050: fadd s4, s3, s4
// 0x10aa054: fmin s1, s0, s1
// 0x10aa058: fcsel s3, s4, s3, gt
// 0x10aa05c: fcmp s0, #0.0
// 0x10aa060: ldr x8, [x19, #0x68]
// 0x10aa064: fcsel s0, s1, s2, pl
// 0x10aa068: fmul s0, s0, s3
// 0x10aa06c: fadd s0, s8, s0
// 0x10aa070: str s0, [x19, #0x110]
// 0x10aa074: cbz x8, #0x10ac1ec
// 0x10aa078: ldrb w8, [x8, #0x258]
// 0x10aa07c: cbz w8, #0x10aa0d0
// 0x10aa080: ldr w9, [x19, #0x230]
// 0x10aa084: ldr x8, [x19, #0x90]
// 0x10aa088: cmp w9, #5
// 0x10aa08c: b.ne #0x10aa0b0
// 0x10aa090: cbz x8, #0x10ac1ec
// 0x10aa094: ldr w9, [x8, #0x368]
// 0x10aa098: cmp w9, #6
// 0x10aa09c: b.eq #0x10aa0b4
// 0x10aa0a0: sub w9, w9, #1
// 0x10aa0a4: cmp w9, #2
// 0x10aa0a8: b.hs #0x10aa0c8
// 0x10aa0ac: b #0x10aa0d0
// 0x10aa0b0: cbz x8, #0x10ac1ec
// 0x10aa0b4: ldrb w9, [x8, #0x1d4]
// 0x10aa0b8: cbz w9, #0x10aa0d0
// 0x10aa0bc: ldr w9, [x8, #0x368]
// 0x10aa0c0: cmp w9, #6
// 0x10aa0c4: b.ne #0x10aa0d0
// 0x10aa0c8: ldrb w8, [x8, #0x229]
// 0x10aa0cc: cbz w8, #0x10aaf10
// 0x10aa0d0: ldr s9, [x19, #0x158]
// 0x10aa0d4: mov x0, xzr
// 0x10aa0d8: bl #0x1b89b60
// 0x10aa0dc: mov w8, #0x42800000
// 0x10aa0e0: fmov s10, wzr
// 0x10aa0e4: fmov s1, w8
// 0x10aa0e8: fmul s0, s0, s1
// 0x10aa0ec: fsub s1, s10, s9
// 0x10aa0f0: fneg s3, s0
// 0x10aa0f4: fcmp s1, #0.0
// 0x10aa0f8: ldr x0, [x19, #0xa0]
// 0x10aa0fc: fabs s2, s1
// 0x10aa100: fcsel s1, s0, s3, ge
// 0x10aa104: fadd s1, s9, s1
// 0x10aa108: fcmp s2, s0
// 0x10aa10c: fcsel s0, s1, s10, hi
// 0x10aa110: str s0, [x19, #0x158]
// 0x10aa114: cbz x0, #0x10ac1ec
// 0x10aa118: mov x1, xzr
// 0x10aa11c: bl #0x1b9d6c8
// 0x10aa120: ldr s0, [x19, #0x11c]
// 0x10aa124: mov w8, #0x43b40000
// 0x10aa128: fmov s2, w8
// 0x10aa12c: mov w9, #-0x3c4c0000
// 0x10aa130: fsub s0, s0, s1
// 0x10aa134: fdiv s1, s0, s2
// 0x10aa138: fmov s3, w9
// 0x10aa13c: frintm s1, s1
// 0x10aa140: fmul s1, s1, s3
// 0x10aa144: fadd s0, s0, s1
// 0x10aa148: fmov s1, wzr
// 0x10aa14c: mov w8, #0x43340000
// 0x10aa150: fmin s2, s0, s2
// 0x10aa154: fcmp s0, #0.0
// 0x10aa158: fmov s0, w8
// 0x10aa15c: fcsel s1, s2, s1, pl
// 0x10aa160: fadd s2, s1, s3
// 0x10aa164: fcmp s1, s0
// 0x10aa168: fcsel s0, s2, s1, gt
// 0x10aa16c: mov w8, #0x42b40000
// 0x10aa170: fabs s0, s0
// 0x10aa174: fmov s1, w8
// 0x10aa178: fcmp s0, s1
// 0x10aa17c: b.gt #0x10aa1ac
// 0x10aa180: ldr x8, [x19, #0x70]
// 0x10aa184: cbz x8, #0x10ac1ec
// 0x10aa188: ldrb w8, [x8, #0x2d0]
// 0x10aa18c: cbnz w8, #0x10aa1ac
// 0x10aa190: ldr s8, [x19, #0x200]
// 0x10aa194: ldr s9, [x19, #0x204]
// 0x10aa198: mov x0, xzr
// 0x10aa19c: bl #0x1b9ad30
// 0x10aa1a0: fadd s1, s8, s9
// 0x10aa1a4: fcmp s1, s0
// 0x10aa1a8: b.le #0x10aa1ec
// 0x10aa1ac: ldr s8, [x19, #0x13c]
// 0x10aa1b0: mov x0, xzr
// 0x10aa1b4: bl #0x1b9ad30
// 0x10aa1b8: ldr s1, [x24, #0x3a0]
// 0x10aa1bc: fadd s1, s8, s1
// 0x10aa1c0: fcmp s1, s0
// 0x10aa1c4: b.pl #0x10aa1ec
// 0x10aa1c8: ldr s9, [x19, #0x138]
// 0x10aa1cc: mov x0, xzr
// 0x10aa1d0: bl #0x1b89b60
// 0x10aa1d4: mov w8, #0x43000000
// 0x10aa1d8: mov w9, #0x42100000
// 0x10aa1dc: fmov s1, w8
// 0x10aa1e0: fmul s0, s0, s1
// 0x10aa1e4: fmov s10, w9
// 0x10aa1e8: b #0x10aa208
// 0x10aa1ec: ldr s9, [x19, #0x138]
// 0x10aa1f0: ldr s10, [x19, #0x134]
// 0x10aa1f4: mov x0, xzr
// 0x10aa1f8: bl #0x1b89b60
// 0x10aa1fc: mov w8, #0x42800000
// 0x10aa200: fmov s1, w8
// 0x10aa204: fmul s0, s0, s1
// 0x10aa208: fsub s1, s10, s9
// 0x10aa20c: fneg s3, s0
// 0x10aa210: fcmp s1, #0.0
// 0x10aa214: ldr x0, [x19, #0x50]
// 0x10aa218: fabs s2, s1
// 0x10aa21c: fcsel s1, s0, s3, ge
// 0x10aa220: fadd s1, s9, s1
// 0x10aa224: fcmp s2, s0
// 0x10aa228: fcsel s0, s1, s10, hi
// 0x10aa22c: str s0, [x19, #0x138]
// 0x10aa230: cbz x0, #0x10ac1ec
// 0x10aa234: mov x1, xzr
// 0x10aa238: str s12, [sp, #0x5c]
// 0x10aa23c: bl #0x1b9d9b8
// 0x10aa240: ldr x0, [x19, #0xa0]
// 0x10aa244: cbz x0, #0x10ac1ec
// 0x10aa248: mov x1, xzr
// 0x10aa24c: mov v9.16b, v0.16b
// 0x10aa250: mov v10.16b, v1.16b
// 0x10aa254: mov v11.16b, v2.16b
// 0x10aa258: bl #0x1b9d9b8
// 0x10aa25c: adrp x21, #0x1fab000
// 0x10aa260: ldrb w8, [x21, #0x3e2]
// 0x10aa264: mov v12.16b, v0.16b
// 0x10aa268: mov v13.16b, v1.16b
// 0x10aa26c: mov v14.16b, v2.16b
// 0x10aa270: cbnz w8, #0x10aa288
// 0x10aa274: adrp x0, #0x1e8c000
// 0x10aa278: ldr x0, [x0, #0xa60]
// 0x10aa27c: bl #0xf7d92c
// 0x10aa280: mov w8, #1
// 0x10aa284: strb w8, [x21, #0x3e2]
// 0x10aa288: adrp x21, #0x1e8c000
// 0x10aa28c: ldr x21, [x21, #0xa60]
// 0x10aa290: fmul s0, s9, s9
// 0x10aa294: fmul s1, s10, s10
// 0x10aa298: fadd s0, s0, s1
// 0x10aa29c: ldr x0, [x21]
// 0x10aa2a0: fmul s1, s11, s11
// 0x10aa2a4: fadd s15, s1, s0
// 0x10aa2a8: fmul s0, s12, s12
// 0x10aa2ac: ldr w8, [x0, #0xe0]
// 0x10aa2b0: fmul s1, s13, s13
// 0x10aa2b4: fadd s0, s0, s1
// 0x10aa2b8: fmul s1, s14, s14
// 0x10aa2bc: fadd s8, s1, s0
// 0x10aa2c0: cbnz w8, #0x10aa2c8
// 0x10aa2c4: bl #0xf7da5c
// 0x10aa2c8: adrp x8, #0x832000
// 0x10aa2cc: ldr s1, [x8, #0x344]
// 0x10aa2d0: fmul s0, s15, s8
// 0x10aa2d4: fsqrt s0, s0
// 0x10aa2d8: fcmp s0, s1
// 0x10aa2dc: fmov s1, wzr
// 0x10aa2e0: b.mi #0x10aa338
// 0x10aa2e4: ldr x0, [x21]
// 0x10aa2e8: fmul s1, s9, s12
// 0x10aa2ec: fmul s2, s10, s13
// 0x10aa2f0: fmul s3, s11, s14
// 0x10aa2f4: fadd s1, s1, s2
// 0x10aa2f8: fadd s1, s3, s1
// 0x10aa2fc: ldr w8, [x0, #0xe0]
// 0x10aa300: fdiv s0, s1, s0
// 0x10aa304: fmov s1, #1.00000000
// 0x10aa308: fmov s2, #-1.00000000
// 0x10aa30c: fmin s1, s0, s1
// 0x10aa310: fcmp s0, s2
// 0x10aa314: fcsel s8, s1, s2, pl
// 0x10aa318: cbnz w8, #0x10aa320
// 0x10aa31c: bl #0xf7da5c
// 0x10aa320: fcvt d0, s8
// 0x10aa324: bl #0x1db0ca0
// 0x10aa328: adrp x8, #0x832000
// 0x10aa32c: ldr s1, [x8, #0x554]
// 0x10aa330: fcvt s0, d0
// 0x10aa334: fmul s1, s0, s1
// 0x10aa338: ldr x0, [x19, #0x50]
// 0x10aa33c: str s1, [x19, #0x12c]
// 0x10aa340: cbz x0, #0x10ac1ec
// 0x10aa344: mov x1, xzr
// 0x10aa348: bl #0x1b9d9b8
// 0x10aa34c: ldr x0, [x19, #0xa0]
// 0x10aa350: ldr s11, [sp, #0x5c]
// 0x10aa354: cbz x0, #0x10ac1ec
// 0x10aa358: mov x1, xzr
// 0x10aa35c: mov v9.16b, v0.16b
// 0x10aa360: mov v10.16b, v2.16b
// 0x10aa364: bl #0x1b9d9b8
// 0x10aa368: fmul s0, s10, s0
// 0x10aa36c: fmul s1, s9, s2
// 0x10aa370: fsub s0, s0, s1
// 0x10aa374: fcmp s0, #0.0
// 0x10aa378: b.pl #0x10aa388
// 0x10aa37c: ldr s0, [x19, #0x12c]
// 0x10aa380: fneg s0, s0
// 0x10aa384: str s0, [x19, #0x12c]
// 0x10aa388: ldr x8, [x22]
// 0x10aa38c: cbz x8, #0x10ac1ec
// 0x10aa390: ldrb w9, [x8, #0x2dc]
// 0x10aa394: cbz w9, #0x10aa3ac
// 0x10aa398: ldrb w8, [x8, #0x2e8]
// 0x10aa39c: cbz w8, #0x10aa3ac
// 0x10aa3a0: mov x0, xzr
// 0x10aa3a4: bl #0x1b9ad30
// 0x10aa3a8: str s0, [x19, #0x214]
// 0x10aa3ac: ldr s8, [x19, #0x228]
// 0x10aa3b0: mov x0, xzr
// 0x10aa3b4: bl #0x1b9ad30
// 0x10aa3b8: adrp x8, #0x832000
// 0x10aa3bc: ldr s1, [x8, #0x4e8]
// 0x10aa3c0: fadd s1, s8, s1
// 0x10aa3c4: fcmp s1, s0
// 0x10aa3c8: b.gt #0x10aa490
// 0x10aa3cc: ldr x0, [x19, #0x308]
// 0x10aa3d0: cbz x0, #0x10ac1ec
// 0x10aa3d4: mov x1, xzr
// 0x10aa3d8: bl #0x1b9d6c8
// 0x10aa3dc: ldr x0, [x19, #0xa0]
// 0x10aa3e0: cbz x0, #0x10ac1ec
// 0x10aa3e4: mov x1, xzr
// 0x10aa3e8: mov v9.16b, v1.16b
// 0x10aa3ec: bl #0x1b9d6c8
// 0x10aa3f0: ldr s0, [x19, #0x158]
// 0x10aa3f4: mov w8, #0x43b40000
// 0x10aa3f8: fmov s2, w8
// 0x10aa3fc: mov w8, #-0x3c4c0000
// 0x10aa400: fsub s0, s1, s0
// 0x10aa404: fsub s0, s0, s9
// 0x10aa408: fdiv s3, s0, s2
// 0x10aa40c: fmov s1, w8
// 0x10aa410: frintm s3, s3
// 0x10aa414: fmul s3, s3, s1
// 0x10aa418: fadd s0, s0, s3
// 0x10aa41c: fmov s3, wzr
// 0x10aa420: mov w8, #0x43340000
// 0x10aa424: fmin s2, s0, s2
// 0x10aa428: fcmp s0, #0.0
// 0x10aa42c: fmov s0, w8
// 0x10aa430: fcsel s2, s2, s3, pl
// 0x10aa434: fadd s1, s2, s1
// 0x10aa438: fcmp s2, s0
// 0x10aa43c: fcsel s0, s1, s2, gt
// 0x10aa440: fabs s0, s0
// 0x10aa444: fmov s1, #15.00000000
// 0x10aa448: fcmp s0, s1
// 0x10aa44c: b.gt #0x10aa490
// 0x10aa450: ldr s8, [x19, #0x210]
// 0x10aa454: mov x0, xzr
// 0x10aa458: bl #0x1b9ad30
// 0x10aa45c: adrp x8, #0x832000
// 0x10aa460: ldr s1, [x8, #0x4b0]
// 0x10aa464: fadd s1, s8, s1
// 0x10aa468: fcmp s1, s0
// 0x10aa46c: b.gt #0x10aa490
// 0x10aa470: ldr s8, [x19, #0x214]
// 0x10aa474: mov x0, xzr
// 0x10aa478: bl #0x1b9ad30
// 0x10aa47c: adrp x8, #0x832000
// 0x10aa480: ldr s1, [x8, #0x3ec]
// 0x10aa484: fadd s1, s8, s1
// 0x10aa488: fcmp s1, s0
// 0x10aa48c: b.le #0x10aaf28
// 0x10aa490: ldr x8, [x20]
// 0x10aa494: cbz x8, #0x10ac1ec
// 0x10aa498: mov w9, wzr
// 0x10aa49c: strb w9, [x8, #0x4a9]
// 0x10aa4a0: ldr s8, [x19, #0x13c]
// 0x10aa4a4: mov x0, xzr
// 0x10aa4a8: bl #0x1b9ad30
// 0x10aa4ac: ldr s1, [x24, #0x3a0]
// 0x10aa4b0: fadd s1, s8, s1
// 0x10aa4b4: fcmp s1, s0
// 0x10aa4b8: b.pl #0x10aa504
// 0x10aa4bc: ldr x8, [x19, #0x70]
// 0x10aa4c0: cbz x8, #0x10ac1ec
// 0x10aa4c4: ldrb w8, [x8, #0x2d0]
// 0x10aa4c8: cbnz w8, #0x10aa4dc
// 0x10aa4cc: ldr x8, [x20]
// 0x10aa4d0: cbz x8, #0x10ac1ec
// 0x10aa4d4: ldrb w8, [x8, #0x3a5]
// 0x10aa4d8: cbz w8, #0x10aa504
// 0x10aa4dc: ldr s9, [x19, #0x128]
// 0x10aa4e0: mov x0, xzr
// 0x10aa4e4: add x21, x19, #0x128
// 0x10aa4e8: bl #0x1b89b60
// 0x10aa4ec: mov w8, #0x42f00000
// 0x10aa4f0: mov w9, #0x42800000
// 0x10aa4f4: fmov s1, w8
// 0x10aa4f8: fmul s0, s0, s1
// 0x10aa4fc: fmov s10, w9
// 0x10aa500: b #0x10aa5c0
// 0x10aa504: ldr x0, [x19, #0x308]
// 0x10aa508: cbz x0, #0x10ac1ec
// 0x10aa50c: mov x1, xzr
// 0x10aa510: bl #0x1b9d6c8
// 0x10aa514: ldr x0, [x19, #0x48]
// 0x10aa518: cbz x0, #0x10ac1ec
// 0x10aa51c: mov x1, xzr
// 0x10aa520: mov v9.16b, v1.16b
// 0x10aa524: bl #0x1b94c14
// 0x10aa528: cbz x0, #0x10ac1ec
// 0x10aa52c: mov x1, xzr
// 0x10aa530: bl #0x1b9d6c8
// 0x10aa534: mov w8, #0x43b40000
// 0x10aa538: fsub s0, s1, s9
// 0x10aa53c: fmov s1, w8
// 0x10aa540: mov w8, #-0x3c4c0000
// 0x10aa544: fdiv s2, s0, s1
// 0x10aa548: fmov s3, w8
// 0x10aa54c: frintm s2, s2
// 0x10aa550: fmul s2, s2, s3
// 0x10aa554: fadd s0, s0, s2
// 0x10aa558: fmov s2, wzr
// 0x10aa55c: mov w8, #0x43340000
// 0x10aa560: fmin s1, s0, s1
// 0x10aa564: fcmp s0, #0.0
// 0x10aa568: fcsel s0, s1, s2, pl
// 0x10aa56c: fmov s1, w8
// 0x10aa570: ldr s9, [x19, #0x128]
// 0x10aa574: fadd s2, s0, s3
// 0x10aa578: fcmp s0, s1
// 0x10aa57c: fcsel s0, s2, s0, gt
// 0x10aa580: fabs s0, s0
// 0x10aa584: fmov s1, #30.00000000
// 0x10aa588: fcmp s0, s1
// 0x10aa58c: add x21, x19, #0x128
// 0x10aa590: b.le #0x10aa5a8
// 0x10aa594: ldr s10, [x19, #0x124]
// 0x10aa598: mov x0, xzr
// 0x10aa59c: bl #0x1b89b60
// 0x10aa5a0: mov w8, #0x43800000
// 0x10aa5a4: b #0x10aa5b8
// 0x10aa5a8: mov x0, xzr
// 0x10aa5ac: bl #0x1b89b60
// 0x10aa5b0: mov w8, #0x42f00000
// 0x10aa5b4: fmov s10, #16.00000000
// 0x10aa5b8: fmov s1, w8
// 0x10aa5bc: fmul s0, s0, s1
// 0x10aa5c0: fsub s1, s10, s9
// 0x10aa5c4: fneg s3, s0
// 0x10aa5c8: fcmp s1, #0.0
// 0x10aa5cc: fabs s2, s1
// 0x10aa5d0: fcsel s1, s0, s3, ge
// 0x10aa5d4: fadd s1, s9, s1
// 0x10aa5d8: fcmp s2, s0
// 0x10aa5dc: fcsel s0, s1, s10, hi
// 0x10aa5e0: str s0, [x21]
// 0x10aa5e4: ldr x8, [x22]
// 0x10aa5e8: cbz x8, #0x10ac1ec
// 0x10aa5ec: ldrb w8, [x8, #0x258]
// 0x10aa5f0: cbz w8, #0x10aa62c
// 0x10aa5f4: ldr x8, [x19, #0x70]
// 0x10aa5f8: cbz x8, #0x10ac1ec
// 0x10aa5fc: ldrb w8, [x8, #0x2d0]
// 0x10aa600: cbnz w8, #0x10aa620
// 0x10aa604: ldr s8, [x19, #0x200]
// 0x10aa608: ldr s9, [x19, #0x204]
// 0x10aa60c: mov x0, xzr
// 0x10aa610: bl #0x1b9ad30
// 0x10aa614: fadd s1, s8, s9
// 0x10aa618: fcmp s1, s0
// 0x10aa61c: b.le #0x10aa62c
// 0x10aa620: mov w8, #-0x3df40000
// 0x10aa624: fmov s9, w8
// 0x10aa628: b #0x10aa630
// 0x10aa62c: fmov s9, wzr
// 0x10aa630: ldr x8, [x19, #0x70]
// 0x10aa634: cbz x8, #0x10ac1ec
// 0x10aa638: ldrb w8, [x8, #0x2d0]
// 0x10aa63c: cbnz w8, #0x10aa65c
// 0x10aa640: ldr s8, [x19, #0x200]
// 0x10aa644: ldr s10, [x19, #0x204]
// 0x10aa648: mov x0, xzr
// 0x10aa64c: bl #0x1b9ad30
// 0x10aa650: fadd s1, s8, s10
// 0x10aa654: fcmp s1, s0
// 0x10aa658: b.le #0x10aa790
// 0x10aa65c: ldr x8, [x20]
// 0x10aa660: cbz x8, #0x10ac1ec
// 0x10aa664: ldr w9, [x8, #0x368]
// 0x10aa668: fmov s0, wzr
// 0x10aa66c: cmp w9, #3
// 0x10aa670: b.eq #0x10aa678
// 0x10aa674: ldr s0, [x19, #0x14c]
// 0x10aa678: str s0, [x19, #0x150]
// 0x10aa67c: ldr w9, [x8, #0x368]
// 0x10aa680: cmp w9, #6
// 0x10aa684: b.ne #0x10aa7e0
// 0x10aa688: ldr x9, [x19, #0xf8]
// 0x10aa68c: cbz x9, #0x10ac1ec
// 0x10aa690: ldr x0, [x9, #0x20]
// 0x10aa694: cbz x0, #0x10ac1ec
// 0x10aa698: adrp x24, #0x1e8e000
// 0x10aa69c: ldrb w25, [x8, #0x1d4]
// 0x10aa6a0: ldr w1, [x8, #0x124]
// 0x10aa6a4: ldr x24, [x24, #0x558]
// 0x10aa6a8: ldr x2, [x24]
// 0x10aa6ac: bl #0x14a30c0
// 0x10aa6b0: cbz x0, #0x10ac1ec
// 0x10aa6b4: adrp x8, #0x1e8c000
// 0x10aa6b8: ldr x8, [x8, #0xd8]
// 0x10aa6bc: ldr x21, [x0, #0x10]
// 0x10aa6c0: ldr x8, [x8]
// 0x10aa6c4: ldr w9, [x8, #0xe0]
// 0x10aa6c8: cbnz w9, #0x10aa6d4
// 0x10aa6cc: mov x0, x8
// 0x10aa6d0: bl #0xf7da5c
// 0x10aa6d4: mov x0, x21
// 0x10aa6d8: mov x1, xzr
// 0x10aa6dc: mov x2, xzr
// 0x10aa6e0: bl #0x1b94ac8
// 0x10aa6e4: cbz w25, #0x10aa7a0
// 0x10aa6e8: tbz w0, #0, #0x10aa7e0
// 0x10aa6ec: ldr x8, [x20]
// 0x10aa6f0: cbz x8, #0x10ac1ec
// 0x10aa6f4: ldr s8, [x8, #0x1b8]
// 0x10aa6f8: ldr s10, [x19, #0x2f8]
// 0x10aa6fc: mov x0, xzr
// 0x10aa700: bl #0x1b9ad30
// 0x10aa704: fadd s1, s8, s10
// 0x10aa708: fcmp s1, s0
// 0x10aa70c: b.pl #0x10aa720
// 0x10aa710: ldr x8, [x22]
// 0x10aa714: cbz x8, #0x10ac1ec
// 0x10aa718: ldrb w8, [x8, #0x2dc]
// 0x10aa71c: cbz w8, #0x10aa758
// 0x10aa720: ldr x8, [x20]
// 0x10aa724: cbz x8, #0x10ac1ec
// 0x10aa728: ldr s8, [x8, #0x1b8]
// 0x10aa72c: ldr s10, [x19, #0x2f8]
// 0x10aa730: mov x0, xzr
// 0x10aa734: bl #0x1b9ad30
// 0x10aa738: fmul s1, s10, s11
// 0x10aa73c: fadd s1, s8, s1
// 0x10aa740: fcmp s1, s0
// 0x10aa744: b.pl #0x10aa7e0
// 0x10aa748: ldr x8, [x22]
// 0x10aa74c: cbz x8, #0x10ac1ec
// 0x10aa750: ldrb w8, [x8, #0x2dc]
// 0x10aa754: cbz w8, #0x10aa7e0
// 0x10aa758: ldr x9, [x19, #0xf8]
// 0x10aa75c: cbz x9, #0x10ac1ec
// 0x10aa760: ldr x8, [x20]
// 0x10aa764: cbz x8, #0x10ac1ec
// 0x10aa768: ldr x0, [x9, #0x20]
// 0x10aa76c: cbz x0, #0x10ac1ec
// 0x10aa770: ldr w1, [x8, #0x124]
// 0x10aa774: ldr x2, [x24]
// 0x10aa778: bl #0x14a30c0
// 0x10aa77c: cbz x0, #0x10ac1ec
// 0x10aa780: ldr x0, [x0, #0x10]
// 0x10aa784: cbz x0, #0x10ac1ec
// 0x10aa788: mov w1, #1
// 0x10aa78c: b #0x10aa7d8
// 0x10aa790: ldr x8, [x19, #0x90]
// 0x10aa794: str wzr, [x19, #0x150]
// 0x10aa798: cbnz x8, #0x10aa67c
// 0x10aa79c: b #0x10ac1ec
// 0x10aa7a0: tbz w0, #0, #0x10aa7e0
// 0x10aa7a4: ldr x9, [x19, #0xf8]
// 0x10aa7a8: cbz x9, #0x10ac1ec
// 0x10aa7ac: ldr x8, [x20]
// 0x10aa7b0: cbz x8, #0x10ac1ec
// 0x10aa7b4: ldr x0, [x9, #0x20]
// 0x10aa7b8: cbz x0, #0x10ac1ec
// 0x10aa7bc: ldr w1, [x8, #0x124]
// 0x10aa7c0: ldr x2, [x24]
// 0x10aa7c4: bl #0x14a30c0
// 0x10aa7c8: cbz x0, #0x10ac1ec
// 0x10aa7cc: ldr x0, [x0, #0x10]
// 0x10aa7d0: cbz x0, #0x10ac1ec
// 0x10aa7d4: mov w1, wzr
// 0x10aa7d8: mov x2, xzr
// 0x10aa7dc: bl #0x1b94cd0
// 0x10aa7e0: ldr s8, [x19, #0x130]
// 0x10aa7e4: ldr s10, [x19, #0x12c]
// 0x10aa7e8: ldr s11, [x19, #0x150]
// 0x10aa7ec: mov x0, xzr
// 0x10aa7f0: bl #0x1b89b60
// 0x10aa7f4: ldr s1, [x19, #0x128]
// 0x10aa7f8: fadd s2, s9, s10
// 0x10aa7fc: mov w8, #0x43b40000
// 0x10aa800: fadd s2, s2, s11
// 0x10aa804: fmov s3, w8
// 0x10aa808: fsub s2, s2, s8
// 0x10aa80c: mov w8, #-0x3c4c0000
// 0x10aa810: fmul s0, s0, s1
// 0x10aa814: fdiv s1, s2, s3
// 0x10aa818: fmov s4, w8
// 0x10aa81c: frintm s1, s1
// 0x10aa820: fmul s1, s1, s4
// 0x10aa824: fadd s1, s2, s1
// 0x10aa828: fmov s2, wzr
// 0x10aa82c: mov w8, #0x43340000
// 0x10aa830: fmin s3, s1, s3
// 0x10aa834: fcmp s1, #0.0
// 0x10aa838: fmov s1, w8
// 0x10aa83c: fcsel s3, s3, s2, pl
// 0x10aa840: fcmp s3, s1
// 0x10aa844: fmov s1, #1.00000000
// 0x10aa848: fadd s4, s3, s4
// 0x10aa84c: mov w8, #0x42b40000
// 0x10aa850: fcsel s3, s4, s3, gt
// 0x10aa854: fmin s1, s0, s1
// 0x10aa858: fcmp s0, #0.0
// 0x10aa85c: fmov s4, w8
// 0x10aa860: mov w8, #-0x3d4c0000
// 0x10aa864: fcsel s1, s1, s2, pl
// 0x10aa868: fmov s0, w8
// 0x10aa86c: ldr x8, [x19, #0x90]
// 0x10aa870: fmul s1, s1, s3
// 0x10aa874: fadd s1, s8, s1
// 0x10aa878: fmin s2, s1, s4
// 0x10aa87c: fcmp s1, s0
// 0x10aa880: fcsel s0, s2, s0, pl
// 0x10aa884: str s0, [x19, #0x130]
// 0x10aa888: cbz x8, #0x10ac1ec
// 0x10aa88c: ldrb w9, [x8, #0x3a5]
// 0x10aa890: ldr w8, [x19, #0x220]
// 0x10aa894: cbz w9, #0x10aa8ac
// 0x10aa898: cbnz w8, #0x10aa8b8
// 0x10aa89c: mov x0, xzr
// 0x10aa8a0: bl #0x1b9ad30
// 0x10aa8a4: str s0, [x19, #0x200]
// 0x10aa8a8: b #0x10aa8b8
// 0x10aa8ac: cbz w8, #0x10aae84
// 0x10aa8b0: mov w8, #-0x3e800000
// 0x10aa8b4: str w8, [x19, #0x200]
// 0x10aa8b8: ldr x8, [x19, #0x70]
// 0x10aa8bc: cbz x8, #0x10ac1ec
// 0x10aa8c0: ldr x8, [x8, #0x50]
// 0x10aa8c4: cbz x8, #0x10ac1ec
// 0x10aa8c8: ldrb w9, [x8, #0x129]
// 0x10aa8cc: ldrb w8, [x19, #0x2c0]
// 0x10aa8d0: cbz w9, #0x10aa964
// 0x10aa8d4: cbnz w8, #0x10aa9e0
// 0x10aa8d8: ldr x8, [x20]
// 0x10aa8dc: cbz x8, #0x10ac1ec
// 0x10aa8e0: adrp x9, #0x1e8c000
// 0x10aa8e4: ldr x9, [x9, #0xd8]
// 0x10aa8e8: ldr x21, [x8, #0x28]
// 0x10aa8ec: ldr x0, [x9]
// 0x10aa8f0: ldr w9, [x0, #0xe0]
// 0x10aa8f4: cbnz w9, #0x10aa8fc
// 0x10aa8f8: bl #0xf7da5c
// 0x10aa8fc: mov x0, x21
// 0x10aa900: mov x1, xzr
// 0x10aa904: bl #0x1b98274
// 0x10aa908: tbz w0, #0, #0x10aa94c
// 0x10aa90c: ldr x8, [x20]
// 0x10aa910: cbz x8, #0x10ac1ec
// 0x10aa914: ldr x0, [x8, #0x28]
// 0x10aa918: cbz x0, #0x10ac1ec
// 0x10aa91c: mov x1, xzr
// 0x10aa920: bl #0x1b673a0
// 0x10aa924: tbz w0, #0, #0x10aa94c
// 0x10aa928: ldr x8, [x20]
// 0x10aa92c: cbz x8, #0x10ac1ec
// 0x10aa930: ldr x0, [x8, #0x28]
// 0x10aa934: cbz x0, #0x10ac1ec
// 0x10aa938: adrp x8, #0x1e8e000
// 0x10aa93c: ldr x8, [x8, #0x498]
// 0x10aa940: mov x2, xzr
// 0x10aa944: ldr x1, [x8]
// 0x10aa948: bl #0x1b67884
// 0x10aa94c: mov x0, xzr
// 0x10aa950: bl #0x1b9ad30
// 0x10aa954: mov w8, #1
// 0x10aa958: str s0, [x19, #0x2c4]
// 0x10aa95c: strb w8, [x19, #0x2c0]
// 0x10aa960: b #0x10aa9e0
// 0x10aa964: cbz w8, #0x10aa9e0
// 0x10aa968: ldr x8, [x20]
// 0x10aa96c: cbz x8, #0x10ac1ec
// 0x10aa970: adrp x9, #0x1e8c000
// 0x10aa974: ldr x9, [x9, #0xd8]
// 0x10aa978: ldr x21, [x8, #0x28]
// 0x10aa97c: ldr x0, [x9]
// 0x10aa980: ldr w9, [x0, #0xe0]
// 0x10aa984: cbnz w9, #0x10aa98c
// 0x10aa988: bl #0xf7da5c
// 0x10aa98c: mov x0, x21
// 0x10aa990: mov x1, xzr
// 0x10aa994: bl #0x1b98274
// 0x10aa998: tbz w0, #0, #0x10aa9dc
// 0x10aa99c: ldr x8, [x20]
// 0x10aa9a0: cbz x8, #0x10ac1ec
// 0x10aa9a4: ldr x0, [x8, #0x28]
// 0x10aa9a8: cbz x0, #0x10ac1ec
// 0x10aa9ac: mov x1, xzr
// 0x10aa9b0: bl #0x1b673a0
// 0x10aa9b4: tbz w0, #0, #0x10aa9dc
// 0x10aa9b8: ldr x8, [x20]
// 0x10aa9bc: cbz x8, #0x10ac1ec
// 0x10aa9c0: ldr x0, [x8, #0x28]
// 0x10aa9c4: cbz x0, #0x10ac1ec
// 0x10aa9c8: adrp x8, #0x1e8e000
// 0x10aa9cc: ldr x8, [x8, #0x5a8]
// 0x10aa9d0: mov x2, xzr
// 0x10aa9d4: ldr x1, [x8]
// 0x10aa9d8: bl #0x1b67884
// 0x10aa9dc: strb wzr, [x19, #0x2c0]
// 0x10aa9e0: ldr x8, [x20]
// 0x10aa9e4: cbz x8, #0x10ac1ec
// 0x10aa9e8: ldr w9, [x8, #0x368]
// 0x10aa9ec: cmp w9, #3
// 0x10aa9f0: b.eq #0x10aaa30
// 0x10aa9f4: cmp w9, #5
// 0x10aa9f8: b.ne #0x10aaa4c
// 0x10aa9fc: adrp x9, #0x1e8c000
// 0x10aaa00: ldr x9, [x9, #0xd8]
// 0x10aaa04: ldr x21, [x8, #0x30]
// 0x10aaa08: ldr x0, [x9]
// 0x10aaa0c: ldr w9, [x0, #0xe0]
// 0x10aaa10: cbnz w9, #0x10aaa18
// 0x10aaa14: bl #0xf7da5c
// 0x10aaa18: mov x0, x21
// 0x10aaa1c: mov x1, xzr
// 0x10aaa20: bl #0x1b98274
// 0x10aaa24: tbz w0, #0, #0x10aaa38
// 0x10aaa28: add x8, x19, #0x2d4
// 0x10aaa2c: b #0x10aaa3c
// 0x10aaa30: add x8, x19, #0x2d0
// 0x10aaa34: b #0x10aaa3c
// 0x10aaa38: add x8, x19, #0x2cc
// 0x10aaa3c: ldr s0, [x8]
// 0x10aaa40: ldr x8, [x19, #0x90]
// 0x10aaa44: str s0, [x19, #0x2c8]
// 0x10aaa48: cbz x8, #0x10ac1ec
// 0x10aaa4c: ldrb w9, [x8, #0x229]
// 0x10aaa50: cbz w9, #0x10aaa7c
// 0x10aaa54: ldr s0, [x19, #0x2f4]
// 0x10aaa58: ldrb w8, [x8, #0x36d]
// 0x10aaa5c: fmov s1, #0.25000000
// 0x10aaa60: mov w9, #-0x3e800000
// 0x10aaa64: fmul s1, s0, s1
// 0x10aaa68: cmp w8, #0
// 0x10aaa6c: fcsel s0, s0, s1, eq
// 0x10aaa70: str s0, [x19, #0x2f0]
// 0x10aaa74: str w9, [x19, #0x2c4]
// 0x10aaa78: b #0x10aaab8
// 0x10aaa7c: ldr w9, [x8, #0x368]
// 0x10aaa80: sub w9, w9, #1
// 0x10aaa84: cmp w9, #1
// 0x10aaa88: b.hi #0x10aaab0
// 0x10aaa8c: ldrb w9, [x8, #0x1f8]
// 0x10aaa90: cbnz w9, #0x10aaaa4
// 0x10aaa94: ldr x9, [x22]
// 0x10aaa98: cbz x9, #0x10ac1ec
// 0x10aaa9c: ldrb w9, [x9, #0x2dc]
// 0x10aaaa0: cbz w9, #0x10ab0b4
// 0x10aaaa4: ldr s0, [x8, #0x370]
// 0x10aaaa8: str s0, [x19, #0x2f0]
// 0x10aaaac: b #0x10aaab8
// 0x10aaab0: mov w8, #0x3f800000
// 0x10aaab4: str w8, [x19, #0x2f0]
// 0x10aaab8: ldr x8, [x19, #0x70]
// 0x10aaabc: cbz x8, #0x10ac1ec
// 0x10aaac0: ldr s0, [x8, #0x20c]
// 0x10aaac4: fcmp s0, #0.0
// 0x10aaac8: b.ge #0x10aade0
// 0x10aaacc: strb wzr, [x19, #0x2fd]
// 0x10aaad0: adrp x20, #0x1fab000
// 0x10aaad4: ldr d10, [x19, #0x2a0]
// 0x10aaad8: ldrb w8, [x20, #0x2c9]
// 0x10aaadc: ldr s12, [x19, #0x2a8]
// 0x10aaae0: cbnz w8, #0x10aaaf8
// 0x10aaae4: adrp x0, #0x1e8c000
// 0x10aaae8: ldr x0, [x0, #0x1e8]
// 0x10aaaec: bl #0xf7d92c
// 0x10aaaf0: mov w8, #1
// 0x10aaaf4: strb w8, [x20, #0x2c9]
// 0x10aaaf8: adrp x21, #0x1e8c000
// 0x10aaafc: ldr x21, [x21, #0x1e8]
// 0x10aab00: mov x0, xzr
// 0x10aab04: ldr x8, [x21]
// 0x10aab08: ldr x8, [x8, #0xb8]
// 0x10aab0c: ldr d13, [x8]
// 0x10aab10: ldr s14, [x8, #8]
// 0x10aab14: bl #0x1b9ae30
// 0x10aab18: fmov s11, #24.00000000
// 0x10aab1c: fmov s9, #1.00000000
// 0x10aab20: fmul s0, s0, s11
// 0x10aab24: fmov s8, wzr
// 0x10aab28: fcmp s0, #0.0
// 0x10aab2c: fmin s0, s0, s9
// 0x10aab30: fsub v1.2s, v13.2s, v10.2s
// 0x10aab34: fsub s2, s14, s12
// 0x10aab38: fcsel s0, s0, s8, pl
// 0x10aab3c: fmul v1.2s, v1.2s, v0.s[0]
// 0x10aab40: fmul s0, s2, s0
// 0x10aab44: fadd v1.2s, v10.2s, v1.2s
// 0x10aab48: fadd s0, s12, s0
// 0x10aab4c: str d1, [x19, #0x2a0]
// 0x10aab50: str s0, [x19, #0x2a8]
// 0x10aab54: ldr d12, [x23, #0x168]
// 0x10aab58: ldrb w8, [x20, #0x2c9]
// 0x10aab5c: ldr s10, [x19, #0x2b4]
// 0x10aab60: cbnz w8, #0x10aab78
// 0x10aab64: adrp x0, #0x1e8c000
// 0x10aab68: ldr x0, [x0, #0x1e8]
// 0x10aab6c: bl #0xf7d92c
// 0x10aab70: mov w8, #1
// 0x10aab74: strb w8, [x20, #0x2c9]
// 0x10aab78: ldr x8, [x21]
// 0x10aab7c: mov x0, xzr
// 0x10aab80: ldr x8, [x8, #0xb8]
// 0x10aab84: ldr d13, [x8]
// 0x10aab88: ldr s14, [x8, #8]
// 0x10aab8c: bl #0x1b9ae30
// 0x10aab90: fmul s0, s0, s11
// 0x10aab94: fmin s2, s0, s9
// 0x10aab98: fcmp s0, #0.0
// 0x10aab9c: fsub v1.2s, v13.2s, v12.2s
// 0x10aaba0: fcsel s0, s2, s8, pl
// 0x10aaba4: fmul v1.2s, v1.2s, v0.s[0]
// 0x10aaba8: fadd v1.2s, v12.2s, v1.2s
// 0x10aabac: str d1, [x23, #0x168]
// 0x10aabb0: fsub s2, s14, s10
// 0x10aabb4: ldr s9, [x19, #0x284]
// 0x10aabb8: fmul s0, s2, s0
// 0x10aabbc: fadd s0, s10, s0
// 0x10aabc0: mov x0, xzr
// 0x10aabc4: str s0, [x19, #0x2b4]
// 0x10aabc8: bl #0x1b89b60
// 0x10aabcc: fmov s10, #8.00000000
// 0x10aabd0: fsub s1, s8, s9
// 0x10aabd4: fmul s3, s0, s10
// 0x10aabd8: fnmul s0, s0, s10
// 0x10aabdc: fcmp s1, #0.0
// 0x10aabe0: fabd s2, s8, s9
// 0x10aabe4: ldr s11, [x19, #0x280]
// 0x10aabe8: fcsel s0, s3, s0, ge
// 0x10aabec: fadd s0, s9, s0
// 0x10aabf0: fcmp s2, s3
// 0x10aabf4: fcsel s0, s0, s8, hi
// 0x10aabf8: mov x0, xzr
// 0x10aabfc: str s0, [x19, #0x284]
// 0x10aac00: bl #0x1b89b60
// 0x10aac04: fsub s2, s8, s11
// 0x10aac08: fmul s1, s0, s10
// 0x10aac0c: fnmul s0, s0, s10
// 0x10aac10: ldrb w8, [x19, #0x2ff]
// 0x10aac14: fcmp s2, #0.0
// 0x10aac18: fabd s3, s8, s11
// 0x10aac1c: fcsel s0, s1, s0, ge
// 0x10aac20: fadd s0, s11, s0
// 0x10aac24: fcmp s3, s1
// 0x10aac28: fcsel s0, s0, s8, hi
// 0x10aac2c: str s0, [x19, #0x280]
// 0x10aac30: cbnz w8, #0x10ab738
// 0x10aac34: ldr x8, [x19, #0xf8]
// 0x10aac38: cbz x8, #0x10ac1ec
// 0x10aac3c: adrp x22, #0x1e8e000
// 0x10aac40: adrp x23, #0x1e8c000
// 0x10aac44: ldr x22, [x22, #0x558]
// 0x10aac48: ldr x23, [x23, #0xd8]
// 0x10aac4c: mov w20, wzr
// 0x10aac50: ldr x0, [x8, #0x20]
// 0x10aac54: cbz x0, #0x10ac1ec
// 0x10aac58: ldr w8, [x0, #0x18]
// 0x10aac5c: cmp w20, w8
// 0x10aac60: b.ge #0x10aae78
// 0x10aac64: ldr x2, [x22]
// 0x10aac68: mov w1, w20
// 0x10aac6c: bl #0x14a30c0
// 0x10aac70: cbz x0, #0x10ac1ec
// 0x10aac74: ldr x8, [x23]
// 0x10aac78: ldr x21, [x0, #0x10]
// 0x10aac7c: ldr w9, [x8, #0xe0]
// 0x10aac80: cbnz w9, #0x10aac8c
// 0x10aac84: mov x0, x8
// 0x10aac88: bl #0xf7da5c
// 0x10aac8c: mov x0, x21
// 0x10aac90: mov x1, xzr
// 0x10aac94: bl #0x1b98274
// 0x10aac98: tbz w0, #0, #0x10aacd0
// 0x10aac9c: ldr x8, [x19, #0xf8]
// 0x10aaca0: cbz x8, #0x10ac1ec
// 0x10aaca4: ldr x0, [x8, #0x20]
// 0x10aaca8: cbz x0, #0x10ac1ec
// 0x10aacac: ldr x2, [x22]
// 0x10aacb0: mov w1, w20
// 0x10aacb4: bl #0x14a30c0
// 0x10aacb8: cbz x0, #0x10ac1ec
// 0x10aacbc: ldr x0, [x0, #0x10]
// 0x10aacc0: cbz x0, #0x10ac1ec
// 0x10aacc4: mov w1, wzr
// 0x10aacc8: mov x2, xzr
// 0x10aaccc: bl #0x1b94cd0
// 0x10aacd0: ldr x8, [x19, #0xf8]
// 0x10aacd4: cbz x8, #0x10ac1ec
// 0x10aacd8: ldr x0, [x8, #0x20]
// 0x10aacdc: cbz x0, #0x10ac1ec
// 0x10aace0: ldr x2, [x22]
// 0x10aace4: mov w1, w20
// 0x10aace8: bl #0x14a30c0
// 0x10aacec: cbz x0, #0x10ac1ec
// 0x10aacf0: ldr x8, [x23]
// 0x10aacf4: ldr x21, [x0, #0x18]
// 0x10aacf8: ldr w9, [x8, #0xe0]
// 0x10aacfc: cbnz w9, #0x10aad08
// 0x10aad00: mov x0, x8
// 0x10aad04: bl #0xf7da5c
// 0x10aad08: mov x0, x21
// 0x10aad0c: mov x1, xzr
// 0x10aad10: mov x2, xzr
// 0x10aad14: bl #0x1b94ac8
// 0x10aad18: tbz w0, #0, #0x10aad50
// 0x10aad1c: ldr x8, [x19, #0xf8]
// 0x10aad20: cbz x8, #0x10ac1ec
// 0x10aad24: ldr x0, [x8, #0x20]
// 0x10aad28: cbz x0, #0x10ac1ec
// 0x10aad2c: ldr x2, [x22]
// 0x10aad30: mov w1, w20
// 0x10aad34: bl #0x14a30c0
// 0x10aad38: cbz x0, #0x10ac1ec
// 0x10aad3c: ldr x0, [x0, #0x18]
// 0x10aad40: cbz x0, #0x10ac1ec
// 0x10aad44: mov w1, wzr
// 0x10aad48: mov x2, xzr
// 0x10aad4c: bl #0x1b94cd0
// 0x10aad50: ldr x8, [x19, #0xf8]
// 0x10aad54: cbz x8, #0x10ac1ec
// 0x10aad58: ldr x0, [x8, #0x20]
// 0x10aad5c: cbz x0, #0x10ac1ec
// 0x10aad60: ldr x2, [x22]
// 0x10aad64: mov w1, w20
// 0x10aad68: bl #0x14a30c0
// 0x10aad6c: cbz x0, #0x10ac1ec
// 0x10aad70: ldr x8, [x23]
// 0x10aad74: ldr x21, [x0, #0x20]
// 0x10aad78: ldr w9, [x8, #0xe0]
// 0x10aad7c: cbnz w9, #0x10aad88
// 0x10aad80: mov x0, x8
// 0x10aad84: bl #0xf7da5c
// 0x10aad88: mov x0, x21
// 0x10aad8c: mov x1, xzr
// 0x10aad90: mov x2, xzr
// 0x10aad94: bl #0x1b94ac8
// 0x10aad98: tbz w0, #0, #0x10aadd0
// 0x10aad9c: ldr x8, [x19, #0xf8]
// 0x10aada0: cbz x8, #0x10ac1ec
// 0x10aada4: ldr x0, [x8, #0x20]
// 0x10aada8: cbz x0, #0x10ac1ec
// 0x10aadac: ldr x2, [x22]
// 0x10aadb0: mov w1, w20
// 0x10aadb4: bl #0x14a30c0
// 0x10aadb8: cbz x0, #0x10ac1ec
// 0x10aadbc: ldr x0, [x0, #0x20]
// 0x10aadc0: cbz x0, #0x10ac1ec
// 0x10aadc4: mov w1, wzr
// 0x10aadc8: mov x2, xzr
// 0x10aadcc: bl #0x1b94cd0
// 0x10aadd0: ldr x8, [x19, #0xf8]
// 0x10aadd4: add w20, w20, #1
// 0x10aadd8: cbnz x8, #0x10aac50
// 0x10aaddc: b #0x10ac1ec
// 0x10aade0: ldr s8, [x19, #0x2c4]
// 0x10aade4: ldr s9, [x19, #0x2c8]
// 0x10aade8: mov x0, xzr
// 0x10aadec: bl #0x1b9ad30
// 0x10aadf0: fadd s1, s8, s9
// 0x10aadf4: fcmp s1, s0
// 0x10aadf8: b.le #0x10aae30
// 0x10aadfc: ldr x8, [x19, #0x98]
// 0x10aae00: cbz x8, #0x10ac1ec
// 0x10aae04: ldr s8, [x8, #0x120]
// 0x10aae08: ldr s9, [x19, #0x2e0]
// 0x10aae0c: mov x0, xzr
// 0x10aae10: bl #0x1b9ad30
// 0x10aae14: fadd s1, s8, s9
// 0x10aae18: fcmp s1, s0
// 0x10aae1c: b.pl #0x10aae30
// 0x10aae20: ldr x8, [x20]
// 0x10aae24: cbz x8, #0x10ac1ec
// 0x10aae28: ldrb w8, [x8, #0x229]
// 0x10aae2c: cbz w8, #0x10aaf38
// 0x10aae30: ldr x8, [x19, #0x70]
// 0x10aae34: cbz x8, #0x10ac1ec
// 0x10aae38: ldrb w8, [x8, #0x2d0]
// 0x10aae3c: cbnz w8, #0x10ab0fc
// 0x10aae40: ldr s8, [x19, #0x200]
// 0x10aae44: ldr s9, [x19, #0x204]
// 0x10aae48: ldr s10, [x19, #0x2f0]
// 0x10aae4c: mov x0, xzr
// 0x10aae50: bl #0x1b9ad30
// 0x10aae54: ldr x8, [x19, #0x68]
// 0x10aae58: fmul s1, s9, s10
// 0x10aae5c: fadd s1, s8, s1
// 0x10aae60: fcmp s1, s0
// 0x10aae64: b.le #0x10aaea0
// 0x10aae68: cbz x8, #0x10ac1ec
// 0x10aae6c: ldrb w9, [x8, #0x258]
// 0x10aae70: cbnz w9, #0x10aaea4
// 0x10aae74: b #0x10ab0fc
// 0x10aae78: mov w8, #1
// 0x10aae7c: strb w8, [x19, #0x2ff]
// 0x10aae80: b #0x10ab738
// 0x10aae84: ldr x8, [x22]
// 0x10aae88: cbz x8, #0x10ac1ec
// 0x10aae8c: ldrb w9, [x8, #0x2dc]
// 0x10aae90: cbz w9, #0x10aa8b8
// 0x10aae94: ldrb w8, [x8, #0x2e8]
// 0x10aae98: cbnz w8, #0x10aa8b0
// 0x10aae9c: b #0x10aa8b8
// 0x10aaea0: cbz x8, #0x10ac1ec
// 0x10aaea4: ldrb w8, [x8, #0x258]
// 0x10aaea8: cbz w8, #0x10aaee4
// 0x10aaeac: ldr s8, [x19, #0x200]
// 0x10aaeb0: ldr s9, [x19, #0x204]
// 0x10aaeb4: mov x0, xzr
// 0x10aaeb8: bl #0x1b9ad30
// 0x10aaebc: fmov s1, #0.50000000
// 0x10aaec0: fmul s1, s9, s1
// 0x10aaec4: fadd s1, s8, s1
// 0x10aaec8: fcmp s1, s0
// 0x10aaecc: b.le #0x10aaee4
// 0x10aaed0: ldr x8, [x20]
// 0x10aaed4: cbz x8, #0x10ac1ec
// 0x10aaed8: ldr w8, [x8, #0x368]
// 0x10aaedc: cmp w8, #6
// 0x10aaee0: b.ne #0x10ab0fc
// 0x10aaee4: ldr x8, [x20]
// 0x10aaee8: cbz x8, #0x10ac1ec
// 0x10aaeec: ldrb w8, [x8, #0x1d4]
// 0x10aaef0: cbnz w8, #0x10ab0fc
// 0x10aaef4: ldr x8, [x19, #0x80]
// 0x10aaef8: cbz x8, #0x10ac1ec
// 0x10aaefc: ldrb w8, [x8, #0x106]
// 0x10aaf00: cbz w8, #0x10ab0bc
// 0x10aaf04: ldr x8, [x19, #0x98]
// 0x10aaf08: cbnz x8, #0x10ab0f4
// 0x10aaf0c: b #0x10ac1ec
// 0x10aaf10: ldr s9, [x19, #0x158]
// 0x10aaf14: ldr s10, [x19, #0x154]
// 0x10aaf18: mov x0, xzr
// 0x10aaf1c: bl #0x1b89b60
// 0x10aaf20: mov w8, #0x43e00000
// 0x10aaf24: b #0x10aa0e4
// 0x10aaf28: ldr x8, [x20]
// 0x10aaf2c: cbz x8, #0x10ac1ec
// 0x10aaf30: mov w9, #1
// 0x10aaf34: b #0x10aa49c
// 0x10aaf38: ldr s8, [x19, #0x280]
// 0x10aaf3c: mov x0, xzr
// 0x10aaf40: bl #0x1b89b60
// 0x10aaf44: fmov s2, #1.00000000
// 0x10aaf48: fmov s1, #9.00000000
// 0x10aaf4c: fsub s4, s2, s8
// 0x10aaf50: ldr x8, [x19, #0x80]
// 0x10aaf54: fmul s3, s0, s1
// 0x10aaf58: fnmul s0, s0, s1
// 0x10aaf5c: fcmp s4, #0.0
// 0x10aaf60: fabd s5, s2, s8
// 0x10aaf64: fcsel s0, s3, s0, ge
// 0x10aaf68: fadd s0, s8, s0
// 0x10aaf6c: fcmp s5, s3
// 0x10aaf70: fcsel s0, s0, s2, hi
// 0x10aaf74: str s0, [x19, #0x280]
// 0x10aaf78: cbz x8, #0x10ac1ec
// 0x10aaf7c: ldrb w8, [x8, #0x106]
// 0x10aaf80: cbz w8, #0x10ab080
// 0x10aaf84: adrp x20, #0x1fab000
// 0x10aaf88: ldr d10, [x19, #0x2a0]
// 0x10aaf8c: ldrb w8, [x20, #0x2c9]
// 0x10aaf90: ldr s11, [x19, #0x2a8]
// 0x10aaf94: cbnz w8, #0x10aafac
// 0x10aaf98: adrp x0, #0x1e8c000
// 0x10aaf9c: ldr x0, [x0, #0x1e8]
// 0x10aafa0: bl #0xf7d92c
// 0x10aafa4: mov w8, #1
// 0x10aafa8: strb w8, [x20, #0x2c9]
// 0x10aafac: adrp x21, #0x1e8c000
// 0x10aafb0: ldr x21, [x21, #0x1e8]
// 0x10aafb4: mov x0, xzr
// 0x10aafb8: ldr x8, [x21]
// 0x10aafbc: ldr x8, [x8, #0xb8]
// 0x10aafc0: ldr d12, [x8]
// 0x10aafc4: ldr s13, [x8, #8]
// 0x10aafc8: bl #0x1b9ae30
// 0x10aafcc: mov w8, #0x42000000
// 0x10aafd0: fmov s1, w8
// 0x10aafd4: fmov s8, #1.00000000
// 0x10aafd8: fmul s0, s0, s1
// 0x10aafdc: fmov s9, wzr
// 0x10aafe0: fcmp s0, #0.0
// 0x10aafe4: fmin s0, s0, s8
// 0x10aafe8: fsub v1.2s, v12.2s, v10.2s
// 0x10aafec: fsub s2, s13, s11
// 0x10aaff0: fcsel s0, s0, s9, pl
// 0x10aaff4: fmul v1.2s, v1.2s, v0.s[0]
// 0x10aaff8: fmul s0, s2, s0
// 0x10aaffc: fadd v1.2s, v10.2s, v1.2s
// 0x10ab000: fadd s0, s11, s0
// 0x10ab004: str d1, [x19, #0x2a0]
// 0x10ab008: str s0, [x19, #0x2a8]
// 0x10ab00c: ldr d10, [x23, #0x168]
// 0x10ab010: ldrb w8, [x20, #0x2c9]
// 0x10ab014: ldr s11, [x19, #0x2b4]
// 0x10ab018: cbnz w8, #0x10ab030
// 0x10ab01c: adrp x0, #0x1e8c000
// 0x10ab020: ldr x0, [x0, #0x1e8]
// 0x10ab024: bl #0xf7d92c
// 0x10ab028: mov w8, #1
// 0x10ab02c: strb w8, [x20, #0x2c9]
// 0x10ab030: ldr x8, [x21]
// 0x10ab034: mov x0, xzr
// 0x10ab038: ldr x8, [x8, #0xb8]
// 0x10ab03c: ldr d12, [x8]
// 0x10ab040: ldr s13, [x8, #8]
// 0x10ab044: bl #0x1b9ae30
// 0x10ab048: mov w8, #0x42000000
// 0x10ab04c: fmov s3, w8
// 0x10ab050: fmul s0, s0, s3
// 0x10ab054: fmin s3, s0, s8
// 0x10ab058: fcmp s0, #0.0
// 0x10ab05c: fsub v1.2s, v12.2s, v10.2s
// 0x10ab060: fsub s2, s13, s11
// 0x10ab064: fcsel s0, s3, s9, pl
// 0x10ab068: fmul v1.2s, v1.2s, v0.s[0]
// 0x10ab06c: fmul s0, s2, s0
// 0x10ab070: fadd v1.2s, v10.2s, v1.2s
// 0x10ab074: fadd s0, s11, s0
// 0x10ab078: str d1, [x23, #0x168]
// 0x10ab07c: str s0, [x19, #0x2b4]
// 0x10ab080: ldr x0, [x19, #0x20]
// 0x10ab084: mov w8, #-0x3e800000
// 0x10ab088: str w8, [x19, #0x200]
// 0x10ab08c: cbz x0, #0x10ac1ec
// 0x10ab090: adrp x8, #0x1e8e000
// 0x10ab094: ldr x8, [x8, #0x5b0]
// 0x10ab098: mov w2, #3
// 0x10ab09c: mov x3, xzr
// 0x10ab0a0: ldr x1, [x8]
// 0x10ab0a4: bl #0x1b67734
// 0x10ab0a8: mov w8, #1
// 0x10ab0ac: strb w8, [x19, #0x2fd]
// 0x10ab0b0: b #0x10ab738
// 0x10ab0b4: ldr s0, [x8, #0x374]
// 0x10ab0b8: b #0x10aaaa8
// 0x10ab0bc: ldr x8, [x19, #0x98]
// 0x10ab0c0: cbz x8, #0x10ac1ec
// 0x10ab0c4: ldr x9, [x8, #0x98]
// 0x10ab0c8: cbz x9, #0x10ac1ec
// 0x10ab0cc: ldr w10, [x19, #0x2e4]
// 0x10ab0d0: ldr w9, [x9, #0x124]
// 0x10ab0d4: cmp w10, w9
// 0x10ab0d8: b.ne #0x10ab0f4
// 0x10ab0dc: ldrb w9, [x8, #0x17e]
// 0x10ab0e0: cbnz w9, #0x10ab0f4
// 0x10ab0e4: ldr x9, [x22]
// 0x10ab0e8: cbz x9, #0x10ac1ec
// 0x10ab0ec: ldrb w9, [x9, #0x258]
// 0x10ab0f0: cbz w9, #0x10ac1bc
// 0x10ab0f4: ldrb w8, [x8, #0x17e]
// 0x10ab0f8: cbz w8, #0x10ab188
// 0x10ab0fc: ldr w8, [x19, #0x220]
// 0x10ab100: cbnz w8, #0x10ab188
// 0x10ab104: ldr x8, [x19, #0x98]
// 0x10ab108: cbz x8, #0x10ac1ec
// 0x10ab10c: ldr s8, [x8, #0x120]
// 0x10ab110: ldr s9, [x19, #0x2e0]
// 0x10ab114: mov x0, xzr
// 0x10ab118: bl #0x1b9ad30
// 0x10ab11c: adrp x8, #0x832000
// 0x10ab120: ldr s1, [x8, #0x340]
// 0x10ab124: fmul s1, s9, s1
// 0x10ab128: fadd s1, s8, s1
// 0x10ab12c: fcmp s1, s0
// 0x10ab130: b.pl #0x10ab188
// 0x10ab134: ldr x8, [x22]
// 0x10ab138: cbz x8, #0x10ac1ec
// 0x10ab13c: ldrb w9, [x8, #0x2dc]
// 0x10ab140: cbz w9, #0x10ab9fc
// 0x10ab144: ldr x9, [x19, #0x78]
// 0x10ab148: cbz x9, #0x10ac1ec
// 0x10ab14c: ldr s0, [x9, #0x78]
// 0x10ab150: ldr d1, [x23, #0x108]
// 0x10ab154: ldr s2, [x19, #0x254]
// 0x10ab158: fmul v1.2s, v1.2s, v0.s[0]
// 0x10ab15c: fmul s0, s0, s2
// 0x10ab160: str d1, [x23, #0x168]
// 0x10ab164: str s0, [x19, #0x2b4]
// 0x10ab168: ldr s2, [x9, #0x78]
// 0x10ab16c: ldr s0, [x19, #0x258]
// 0x10ab170: ldr s1, [x19, #0x25c]
// 0x10ab174: ldr s3, [x19, #0x260]
// 0x10ab178: fmul s0, s2, s0
// 0x10ab17c: fmul s1, s2, s1
// 0x10ab180: fmul s2, s2, s3
// 0x10ab184: b #0x10abb1c
// 0x10ab188: adrp x21, #0x1fab000
// 0x10ab18c: ldr d8, [x19, #0x2a0]
// 0x10ab190: ldrb w8, [x21, #0x2c9]
// 0x10ab194: ldr s12, [x19, #0x2a8]
// 0x10ab198: cbnz w8, #0x10ab1b0
// 0x10ab19c: adrp x0, #0x1e8c000
// 0x10ab1a0: ldr x0, [x0, #0x1e8]
// 0x10ab1a4: bl #0xf7d92c
// 0x10ab1a8: mov w8, #1
// 0x10ab1ac: strb w8, [x21, #0x2c9]
// 0x10ab1b0: adrp x24, #0x1e8c000
// 0x10ab1b4: ldr x24, [x24, #0x1e8]
// 0x10ab1b8: mov x0, xzr
// 0x10ab1bc: ldr x8, [x24]
// 0x10ab1c0: ldr x8, [x8, #0xb8]
// 0x10ab1c4: ldr d13, [x8]
// 0x10ab1c8: ldr s14, [x8, #8]
// 0x10ab1cc: bl #0x1b9ae30
// 0x10ab1d0: fmov s9, #24.00000000
// 0x10ab1d4: fmov s10, #1.00000000
// 0x10ab1d8: fmul s0, s0, s9
// 0x10ab1dc: fmov s11, wzr
// 0x10ab1e0: fcmp s0, #0.0
// 0x10ab1e4: fmin s0, s0, s10
// 0x10ab1e8: fsub v1.2s, v13.2s, v8.2s
// 0x10ab1ec: fsub s2, s14, s12
// 0x10ab1f0: fcsel s0, s0, s11, pl
// 0x10ab1f4: fmul v1.2s, v1.2s, v0.s[0]
// 0x10ab1f8: fmul s0, s2, s0
// 0x10ab1fc: fadd v1.2s, v8.2s, v1.2s
// 0x10ab200: fadd s0, s12, s0
// 0x10ab204: str d1, [x19, #0x2a0]
// 0x10ab208: str s0, [x19, #0x2a8]
// 0x10ab20c: ldr d12, [x23, #0x168]
// 0x10ab210: ldrb w8, [x21, #0x2c9]
// 0x10ab214: ldr s8, [x19, #0x2b4]
// 0x10ab218: cbnz w8, #0x10ab230
// 0x10ab21c: adrp x0, #0x1e8c000
// 0x10ab220: ldr x0, [x0, #0x1e8]
// 0x10ab224: bl #0xf7d92c
// 0x10ab228: mov w8, #1
// 0x10ab22c: strb w8, [x21, #0x2c9]
// 0x10ab230: ldr x8, [x24]
// 0x10ab234: mov x0, xzr
// 0x10ab238: ldr x8, [x8, #0xb8]
// 0x10ab23c: ldr d13, [x8]
// 0x10ab240: ldr s14, [x8, #8]
// 0x10ab244: bl #0x1b9ae30
// 0x10ab248: fmul s0, s0, s9
// 0x10ab24c: fmin s1, s0, s10
// 0x10ab250: fcmp s0, #0.0
// 0x10ab254: fcsel s0, s1, s11, pl
// 0x10ab258: fsub v1.2s, v13.2s, v12.2s
// 0x10ab25c: fmul v1.2s, v1.2s, v0.s[0]
// 0x10ab260: fadd v1.2s, v12.2s, v1.2s
// 0x10ab264: str d1, [x23, #0x168]
// 0x10ab268: ldr x8, [x19, #0x98]
// 0x10ab26c: fsub s1, s14, s8
// 0x10ab270: fmul s0, s1, s0
// 0x10ab274: fadd s0, s8, s0
// 0x10ab278: str s0, [x19, #0x2b4]
// 0x10ab27c: cbz x8, #0x10ac1ec
// 0x10ab280: ldr s8, [x8, #0x120]
// 0x10ab284: ldr s9, [x19, #0x2e0]
// 0x10ab288: mov x0, xzr
// 0x10ab28c: bl #0x1b9ad30
// 0x10ab290: fadd s1, s8, s9
// 0x10ab294: fcmp s1, s0
// 0x10ab298: b.le #0x10ab344
// 0x10ab29c: ldr x0, [x19, #0x20]
// 0x10ab2a0: cbz x0, #0x10ac1ec
// 0x10ab2a4: adrp x8, #0x1e8e000
// 0x10ab2a8: ldr x8, [x8, #0x5b0]
// 0x10ab2ac: mov w2, #4
// 0x10ab2b0: mov x3, xzr
// 0x10ab2b4: ldr x1, [x8]
// 0x10ab2b8: bl #0x1b67734
// 0x10ab2bc: ldr s8, [x19, #0x280]
// 0x10ab2c0: mov w8, #-0x3e800000
// 0x10ab2c4: mov x0, xzr
// 0x10ab2c8: str w8, [x19, #0x2c4]
// 0x10ab2cc: str w8, [x19, #0x200]
// 0x10ab2d0: bl #0x1b89b60
// 0x10ab2d4: fmov s2, #1.00000000
// 0x10ab2d8: fmov s1, #3.00000000
// 0x10ab2dc: fsub s4, s2, s8
// 0x10ab2e0: fmul s3, s0, s1
// 0x10ab2e4: fnmul s0, s0, s1
// 0x10ab2e8: fcmp s4, #0.0
// 0x10ab2ec: ldr s9, [x19, #0x284]
// 0x10ab2f0: fabd s5, s2, s8
// 0x10ab2f4: fcsel s0, s3, s0, ge
// 0x10ab2f8: fadd s0, s8, s0
// 0x10ab2fc: fcmp s5, s3
// 0x10ab300: fcsel s0, s0, s2, hi
// 0x10ab304: mov x0, xzr
// 0x10ab308: str s0, [x19, #0x280]
// 0x10ab30c: bl #0x1b89b60
// 0x10ab310: fmov s2, wzr
// 0x10ab314: fmov s1, #4.00000000
// 0x10ab318: fsub s4, s2, s9
// 0x10ab31c: fmul s3, s0, s1
// 0x10ab320: fnmul s0, s0, s1
// 0x10ab324: fcmp s4, #0.0
// 0x10ab328: fabd s5, s2, s9
// 0x10ab32c: fcsel s0, s3, s0, ge
// 0x10ab330: fadd s0, s9, s0
// 0x10ab334: fcmp s5, s3
// 0x10ab338: fcsel s0, s0, s2, hi
// 0x10ab33c: str s0, [x19, #0x284]
// 0x10ab340: b #0x10ab448
// 0x10ab344: ldr x8, [x22]
// 0x10ab348: cbz x8, #0x10ac1ec
// 0x10ab34c: ldrb w9, [x8, #0x228]
// 0x10ab350: cbz w9, #0x10ab378
// 0x10ab354: ldr x9, [x20]
// 0x10ab358: cbz x9, #0x10ac1ec
// 0x10ab35c: ldr w21, [x9, #0x368]
// 0x10ab360: ldrb w9, [x8, #0x2d0]
// 0x10ab364: cmp w21, #5
// 0x10ab368: b.ne #0x10ab38c
// 0x10ab36c: cbz w9, #0x10ab3e4
// 0x10ab370: ldr w8, [x19, #0x220]
// 0x10ab374: cbnz w8, #0x10ab3e4
// 0x10ab378: ldr s8, [x19, #0x280]
// 0x10ab37c: mov x0, xzr
// 0x10ab380: bl #0x1b89b60
// 0x10ab384: fmov s1, #1.00000000
// 0x10ab388: b #0x10ab3f4
// 0x10ab38c: cbz w9, #0x10ab398
// 0x10ab390: ldr w9, [x19, #0x220]
// 0x10ab394: cbz w9, #0x10aba98
// 0x10ab398: ldrb w22, [x8, #0x2dc]
// 0x10ab39c: cbz w22, #0x10ab3a8
// 0x10ab3a0: ldr w9, [x19, #0x22c]
// 0x10ab3a4: cbnz w9, #0x10ab3e4
// 0x10ab3a8: ldr w9, [x19, #0x220]
// 0x10ab3ac: cmp w9, #1
// 0x10ab3b0: b.eq #0x10ab3e4
// 0x10ab3b4: ldrb w8, [x8, #0x258]
// 0x10ab3b8: cbz w8, #0x10ab3c8
// 0x10ab3bc: ldr w8, [x19, #0x230]
// 0x10ab3c0: cmp w8, #5
// 0x10ab3c4: b.ne #0x10ab3e4
// 0x10ab3c8: ldr s8, [x19, #0x280]
// 0x10ab3cc: mov x0, xzr
// 0x10ab3d0: bl #0x1b89b60
// 0x10ab3d4: cbnz w21, #0x10ab3dc
// 0x10ab3d8: cbnz w22, #0x10ab384
// 0x10ab3dc: cbnz w21, #0x10ab384
// 0x10ab3e0: b #0x10ab3f0
// 0x10ab3e4: ldr s8, [x19, #0x280]
// 0x10ab3e8: mov x0, xzr
// 0x10ab3ec: bl #0x1b89b60
// 0x10ab3f0: fmov s1, wzr
// 0x10ab3f4: fsub s2, s1, s8
// 0x10ab3f8: fmov s3, #3.00000000
// 0x10ab3fc: fabs s4, s2
// 0x10ab400: fcmp s2, #0.0
// 0x10ab404: ldr x0, [x19, #0x20]
// 0x10ab408: fmul s2, s0, s3
// 0x10ab40c: fnmul s0, s0, s3
// 0x10ab410: fcsel s0, s2, s0, ge
// 0x10ab414: fadd s0, s8, s0
// 0x10ab418: fcmp s4, s2
// 0x10ab41c: fcsel s0, s0, s1, hi
// 0x10ab420: str s0, [x19, #0x280]
// 0x10ab424: cbz x0, #0x10ac1ec
// 0x10ab428: adrp x8, #0x1e8e000
// 0x10ab42c: ldr x8, [x8, #0x5b0]
// 0x10ab430: mov w2, wzr
// 0x10ab434: mov x3, xzr
// 0x10ab438: ldr x1, [x8]
// 0x10ab43c: bl #0x1b67734
// 0x10ab440: mov x0, x19
// 0x10ab444: bl #0x10ac1f4
// 0x10ab448: ldr x8, [x19, #0x98]
// 0x10ab44c: cbz x8, #0x10ac1ec
// 0x10ab450: ldrb w9, [x8, #0x17e]
// 0x10ab454: cbz w9, #0x10ab6b8
// 0x10ab458: ldrb w9, [x19, #0x2fc]
// 0x10ab45c: cbnz w9, #0x10ab66c
// 0x10ab460: ldr x8, [x8, #0x98]
// 0x10ab464: cbz x8, #0x10ac1ec
// 0x10ab468: ldr w9, [x19, #0x2e4]
// 0x10ab46c: ldr w8, [x8, #0x124]
// 0x10ab470: cmp w9, w8
// 0x10ab474: b.eq #0x10ab66c
// 0x10ab478: ldr x0, [x19, #0x20]
// 0x10ab47c: cbz x0, #0x10ac1ec
// 0x10ab480: adrp x8, #0x1e8e000
// 0x10ab484: ldr x8, [x8, #0x5c8]
// 0x10ab488: mov x2, xzr
// 0x10ab48c: ldr x1, [x8]
// 0x10ab490: bl #0x1b67884
// 0x10ab494: ldr x9, [x19, #0xf8]
// 0x10ab498: cbz x9, #0x10ac1ec
// 0x10ab49c: ldr x8, [x20]
// 0x10ab4a0: cbz x8, #0x10ac1ec
// 0x10ab4a4: ldr x0, [x9, #0x20]
// 0x10ab4a8: cbz x0, #0x10ac1ec
// 0x10ab4ac: adrp x22, #0x1e8e000
// 0x10ab4b0: ldr w1, [x8, #0x124]
// 0x10ab4b4: ldr x22, [x22, #0x558]
// 0x10ab4b8: ldr x2, [x22]
// 0x10ab4bc: bl #0x14a30c0
// 0x10ab4c0: cbz x0, #0x10ac1ec
// 0x10ab4c4: adrp x23, #0x1e8c000
// 0x10ab4c8: ldr x23, [x23, #0xd8]
// 0x10ab4cc: ldr x21, [x0, #0x10]
// 0x10ab4d0: ldr x8, [x23]
// 0x10ab4d4: ldr w9, [x8, #0xe0]
// 0x10ab4d8: cbnz w9, #0x10ab4e4
// 0x10ab4dc: mov x0, x8
// 0x10ab4e0: bl #0xf7da5c
// 0x10ab4e4: mov x0, x21
// 0x10ab4e8: mov x1, xzr
// 0x10ab4ec: mov x2, xzr
// 0x10ab4f0: bl #0x1b94ac8
// 0x10ab4f4: tbz w0, #0, #0x10ab534
// 0x10ab4f8: ldr x9, [x19, #0xf8]
// 0x10ab4fc: cbz x9, #0x10ac1ec
// 0x10ab500: ldr x8, [x20]
// 0x10ab504: cbz x8, #0x10ac1ec
// 0x10ab508: ldr x0, [x9, #0x20]
// 0x10ab50c: cbz x0, #0x10ac1ec
// 0x10ab510: ldr w1, [x8, #0x124]
// 0x10ab514: ldr x2, [x22]
// 0x10ab518: bl #0x14a30c0
// 0x10ab51c: cbz x0, #0x10ac1ec
// 0x10ab520: ldr x0, [x0, #0x10]
// 0x10ab524: cbz x0, #0x10ac1ec
// 0x10ab528: mov w1, wzr
// 0x10ab52c: mov x2, xzr
// 0x10ab530: bl #0x1b94cd0
// 0x10ab534: ldr x8, [x19, #0x98]
// 0x10ab538: cbz x8, #0x10ac1ec
// 0x10ab53c: ldrb w8, [x8, #0x17e]
// 0x10ab540: cbnz w8, #0x10ab664
// 0x10ab544: ldr x9, [x19, #0xf8]
// 0x10ab548: cbz x9, #0x10ac1ec
// 0x10ab54c: ldr x8, [x20]
// 0x10ab550: cbz x8, #0x10ac1ec
// 0x10ab554: ldr x0, [x9, #0x20]
// 0x10ab558: cbz x0, #0x10ac1ec
// 0x10ab55c: ldr w1, [x8, #0x124]
// 0x10ab560: ldr x2, [x22]
// 0x10ab564: bl #0x14a30c0
// 0x10ab568: cbz x0, #0x10ac1ec
// 0x10ab56c: ldr x8, [x23]
// 0x10ab570: ldr x21, [x0, #0x18]
// 0x10ab574: ldr w9, [x8, #0xe0]
// 0x10ab578: cbnz w9, #0x10ab584
// 0x10ab57c: mov x0, x8
// 0x10ab580: bl #0xf7da5c
// 0x10ab584: mov x0, x21
// 0x10ab588: mov x1, xzr
// 0x10ab58c: mov x2, xzr
// 0x10ab590: bl #0x1b94ac8
// 0x10ab594: tbz w0, #0, #0x10ab5d4
// 0x10ab598: ldr x9, [x19, #0xf8]
// 0x10ab59c: cbz x9, #0x10ac1ec
// 0x10ab5a0: ldr x8, [x20]
// 0x10ab5a4: cbz x8, #0x10ac1ec
// 0x10ab5a8: ldr x0, [x9, #0x20]
// 0x10ab5ac: cbz x0, #0x10ac1ec
// 0x10ab5b0: ldr w1, [x8, #0x124]
// 0x10ab5b4: ldr x2, [x22]
// 0x10ab5b8: bl #0x14a30c0
// 0x10ab5bc: cbz x0, #0x10ac1ec
// 0x10ab5c0: ldr x0, [x0, #0x18]
// 0x10ab5c4: cbz x0, #0x10ac1ec
// 0x10ab5c8: mov w1, wzr
// 0x10ab5cc: mov x2, xzr
// 0x10ab5d0: bl #0x1b94cd0
// 0x10ab5d4: ldr x9, [x19, #0xf8]
// 0x10ab5d8: cbz x9, #0x10ac1ec
// 0x10ab5dc: ldr x8, [x20]
// 0x10ab5e0: cbz x8, #0x10ac1ec
// 0x10ab5e4: ldr x0, [x9, #0x20]
// 0x10ab5e8: cbz x0, #0x10ac1ec
// 0x10ab5ec: ldr w1, [x8, #0x124]
// 0x10ab5f0: ldr x2, [x22]
// 0x10ab5f4: bl #0x14a30c0
// 0x10ab5f8: cbz x0, #0x10ac1ec
// 0x10ab5fc: ldr x8, [x23]
// 0x10ab600: ldr x21, [x0, #0x20]
// 0x10ab604: ldr w9, [x8, #0xe0]
// 0x10ab608: cbnz w9, #0x10ab614
// 0x10ab60c: mov x0, x8
// 0x10ab610: bl #0xf7da5c
// 0x10ab614: mov x0, x21
// 0x10ab618: mov x1, xzr
// 0x10ab61c: mov x2, xzr
// 0x10ab620: bl #0x1b94ac8
// 0x10ab624: tbz w0, #0, #0x10ab664
// 0x10ab628: ldr x9, [x19, #0xf8]
// 0x10ab62c: cbz x9, #0x10ac1ec
// 0x10ab630: ldr x8, [x20]
// 0x10ab634: cbz x8, #0x10ac1ec
// 0x10ab638: ldr x0, [x9, #0x20]
// 0x10ab63c: cbz x0, #0x10ac1ec
// 0x10ab640: ldr w1, [x8, #0x124]
// 0x10ab644: ldr x2, [x22]
// 0x10ab648: bl #0x14a30c0
// 0x10ab64c: cbz x0, #0x10ac1ec
// 0x10ab650: ldr x0, [x0, #0x20]
// 0x10ab654: cbz x0, #0x10ac1ec
// 0x10ab658: mov w1, wzr
// 0x10ab65c: mov x2, xzr
// 0x10ab660: bl #0x1b94cd0
// 0x10ab664: mov w8, #1
// 0x10ab668: strb w8, [x19, #0x2fc]
// 0x10ab66c: ldr s8, [x19, #0x284]
// 0x10ab670: mov x0, xzr
// 0x10ab674: bl #0x1b89b60
// 0x10ab678: fmov s2, #1.00000000
// 0x10ab67c: fmov s1, #4.00000000
// 0x10ab680: ldr w8, [x19, #0x2e4]
// 0x10ab684: fsub s4, s2, s8
// 0x10ab688: fmul s3, s0, s1
// 0x10ab68c: fnmul s0, s0, s1
// 0x10ab690: fcmp s4, #0.0
// 0x10ab694: fabd s5, s2, s8
// 0x10ab698: fcsel s0, s3, s0, ge
// 0x10ab69c: fcmp s5, s3
// 0x10ab6a0: fadd s0, s8, s0
// 0x10ab6a4: neg w8, w8
// 0x10ab6a8: fcsel s0, s0, s2, hi
// 0x10ab6ac: str s0, [x19, #0x284]
// 0x10ab6b0: str w8, [x19, #0x2e4]
// 0x10ab6b4: b #0x10ab6f8
// 0x10ab6b8: ldr s8, [x19, #0x284]
// 0x10ab6bc: mov x0, xzr
// 0x10ab6c0: bl #0x1b89b60
// 0x10ab6c4: fmov s2, wzr
// 0x10ab6c8: fmov s1, #4.00000000
// 0x10ab6cc: fsub s4, s2, s8
// 0x10ab6d0: fmul s3, s0, s1
// 0x10ab6d4: fnmul s0, s0, s1
// 0x10ab6d8: fcmp s4, #0.0
// 0x10ab6dc: fabd s5, s2, s8
// 0x10ab6e0: fcsel s0, s3, s0, ge
// 0x10ab6e4: fcmp s5, s3
// 0x10ab6e8: fadd s0, s8, s0
// 0x10ab6ec: fcsel s0, s0, s2, hi
// 0x10ab6f0: str s0, [x19, #0x284]
// 0x10ab6f4: strb wzr, [x19, #0x2fc]
// 0x10ab6f8: ldr x0, [x19, #0x20]
// 0x10ab6fc: cbz x0, #0x10ac1ec
// 0x10ab700: adrp x8, #0x1e8e000
// 0x10ab704: ldr x8, [x8, #0x4b8]
// 0x10ab708: mov x2, xzr
// 0x10ab70c: ldr x1, [x8]
// 0x10ab710: bl #0x1b67994
// 0x10ab714: mov x0, xzr
// 0x10ab718: bl #0x1b9ad30
// 0x10ab71c: mov w8, #-0x3e800000
// 0x10ab720: mov w9, #1
// 0x10ab724: str s0, [x19, #0x228]
// 0x10ab728: strb wzr, [x19, #0x2ec]
// 0x10ab72c: str wzr, [x19, #0x2e8]
// 0x10ab730: str w8, [x19, #0x200]
// 0x10ab734: strb w9, [x19, #0x2fd]
// 0x10ab738: ldr x8, [x19, #0x80]
// 0x10ab73c: cbz x8, #0x10ac1ec
// 0x10ab740: ldrb w9, [x8, #0x106]
// 0x10ab744: eor w9, w9, #1
// 0x10ab748: strb w9, [x8, #0xb0]
// 0x10ab74c: ldr x0, [x19, #0x20]
// 0x10ab750: cbz x0, #0x10ac1ec
// 0x10ab754: ldr s0, [x19, #0x280]
// 0x10ab758: mov w1, #1
// 0x10ab75c: mov x2, xzr
// 0x10ab760: bl #0x1b67d48
// 0x10ab764: ldr x0, [x19, #0x20]
// 0x10ab768: cbz x0, #0x10ac1ec
// 0x10ab76c: ldr s0, [x19, #0x284]
// 0x10ab770: mov w1, #2
// 0x10ab774: mov x2, xzr
// 0x10ab778: bl #0x1b67d48
// 0x10ab77c: ldr s14, [x19, #0x294]
// 0x10ab780: ldr s8, [x19, #0x2ac]
// 0x10ab784: mov x0, xzr
// 0x10ab788: bl #0x1b89b60
// 0x10ab78c: mov w8, #0x43b40000
// 0x10ab790: fmov s2, #12.00000000
// 0x10ab794: fsub s1, s8, s14
// 0x10ab798: fmov s8, w8
// 0x10ab79c: mov w8, #-0x3c4c0000
// 0x10ab7a0: fmul s0, s0, s2
// 0x10ab7a4: fdiv s2, s1, s8
// 0x10ab7a8: fmov s11, w8
// 0x10ab7ac: frintm s2, s2
// 0x10ab7b0: fmul s2, s2, s11
// 0x10ab7b4: fadd s1, s1, s2
// 0x10ab7b8: fmov s10, wzr
// 0x10ab7bc: mov w8, #0x43340000
// 0x10ab7c0: fmin s2, s1, s8
// 0x10ab7c4: fcmp s1, #0.0
// 0x10ab7c8: fmov s13, w8
// 0x10ab7cc: fcsel s1, s2, s10, pl
// 0x10ab7d0: fmov s3, #1.00000000
// 0x10ab7d4: fadd s2, s1, s11
// 0x10ab7d8: fcmp s1, s13
// 0x10ab7dc: fcsel s1, s2, s1, gt
// 0x10ab7e0: fmin s2, s0, s3
// 0x10ab7e4: fcmp s0, #0.0
// 0x10ab7e8: ldr s15, [x19, #0x298]
// 0x10ab7ec: fcsel s0, s2, s10, pl
// 0x10ab7f0: ldr s9, [x19, #0x2b0]
// 0x10ab7f4: fmul s0, s0, s1
// 0x10ab7f8: fadd s0, s14, s0
// 0x10ab7fc: mov x0, xzr
// 0x10ab800: fmov s12, #1.00000000
// 0x10ab804: str s0, [x19, #0x294]
// 0x10ab808: bl #0x1b89b60
// 0x10ab80c: fmov s2, #24.00000000
// 0x10ab810: fsub s1, s9, s15
// 0x10ab814: fmul s0, s0, s2
// 0x10ab818: fdiv s2, s1, s8
// 0x10ab81c: frintm s2, s2
// 0x10ab820: fmul s2, s2, s11
// 0x10ab824: fadd s1, s1, s2
// 0x10ab828: fmin s2, s1, s8
// 0x10ab82c: fcmp s1, #0.0
// 0x10ab830: fcsel s1, s2, s10, pl
// 0x10ab834: fadd s2, s1, s11
// 0x10ab838: fcmp s1, s13
// 0x10ab83c: fcsel s1, s2, s1, gt
// 0x10ab840: fmin s2, s0, s12
// 0x10ab844: fcmp s0, #0.0
// 0x10ab848: ldr s9, [x19, #0x29c]
// 0x10ab84c: fcsel s0, s2, s10, pl
// 0x10ab850: ldr s14, [x19, #0x2b4]
// 0x10ab854: fmul s0, s0, s1
// 0x10ab858: fadd s0, s15, s0
// 0x10ab85c: mov x0, xzr
// 0x10ab860: str s0, [x19, #0x298]
// 0x10ab864: bl #0x1b89b60
// 0x10ab868: fsub s1, s14, s9
// 0x10ab86c: fdiv s2, s1, s8
// 0x10ab870: frintm s2, s2
// 0x10ab874: fmul s2, s2, s11
// 0x10ab878: fadd s1, s1, s2
// 0x10ab87c: fmin s2, s1, s8
// 0x10ab880: fcmp s1, #0.0
// 0x10ab884: fcsel s1, s2, s10, pl
// 0x10ab888: fmov s12, #12.00000000
// 0x10ab88c: fadd s2, s1, s11
// 0x10ab890: fcmp s1, s13
// 0x10ab894: fmul s0, s0, s12
// 0x10ab898: fcsel s1, s2, s1, gt
// 0x10ab89c: fmov s2, #1.00000000
// 0x10ab8a0: fmin s2, s0, s2
// 0x10ab8a4: fcmp s0, #0.0
// 0x10ab8a8: ldr s14, [x19, #0x288]
// 0x10ab8ac: fcsel s0, s2, s10, pl
// 0x10ab8b0: ldr s15, [x19, #0x2a0]
// 0x10ab8b4: fmul s0, s0, s1
// 0x10ab8b8: fadd s0, s9, s0
// 0x10ab8bc: mov x0, xzr
// 0x10ab8c0: str s0, [x19, #0x29c]
// 0x10ab8c4: bl #0x1b89b60
// 0x10ab8c8: fsub s1, s15, s14
// 0x10ab8cc: fdiv s2, s1, s8
// 0x10ab8d0: frintm s2, s2
// 0x10ab8d4: fmul s2, s2, s11
// 0x10ab8d8: fadd s1, s1, s2
// 0x10ab8dc: fmin s2, s1, s8
// 0x10ab8e0: fcmp s1, #0.0
// 0x10ab8e4: fcsel s1, s2, s10, pl
// 0x10ab8e8: fadd s2, s1, s11
// 0x10ab8ec: fcmp s1, s13
// 0x10ab8f0: fmul s0, s0, s12
// 0x10ab8f4: fcsel s1, s2, s1, gt
// 0x10ab8f8: fmov s2, #1.00000000
// 0x10ab8fc: fmin s2, s0, s2
// 0x10ab900: fcmp s0, #0.0
// 0x10ab904: ldr s9, [x19, #0x28c]
// 0x10ab908: fcsel s0, s2, s10, pl
// 0x10ab90c: ldr s15, [x19, #0x2a4]
// 0x10ab910: fmul s0, s0, s1
// 0x10ab914: fadd s0, s14, s0
// 0x10ab918: mov x0, xzr
// 0x10ab91c: fmov s12, #1.00000000
// 0x10ab920: str s0, [x19, #0x288]
// 0x10ab924: bl #0x1b89b60
// 0x10ab928: fmov s1, #24.00000000
// 0x10ab92c: fmul s0, s0, s1
// 0x10ab930: fsub s1, s15, s9
// 0x10ab934: fdiv s2, s1, s8
// 0x10ab938: frintm s2, s2
// 0x10ab93c: fmul s2, s2, s11
// 0x10ab940: fadd s1, s1, s2
// 0x10ab944: fmin s2, s1, s8
// 0x10ab948: fcmp s1, #0.0
// 0x10ab94c: fcsel s1, s2, s10, pl
// 0x10ab950: fadd s2, s1, s11
// 0x10ab954: fcmp s1, s13
// 0x10ab958: fcsel s1, s2, s1, gt
// 0x10ab95c: fmin s2, s0, s12
// 0x10ab960: fcmp s0, #0.0
// 0x10ab964: ldr s14, [x19, #0x290]
// 0x10ab968: fcsel s0, s2, s10, pl
// 0x10ab96c: ldr s15, [x19, #0x2a8]
// 0x10ab970: fmul s0, s0, s1
// 0x10ab974: fadd s0, s9, s0
// 0x10ab978: mov x0, xzr
// 0x10ab97c: str s0, [x19, #0x28c]
// 0x10ab980: bl #0x1b89b60
// 0x10ab984: fmov s1, #12.00000000
// 0x10ab988: fmul s0, s0, s1
// 0x10ab98c: fsub s1, s15, s14
// 0x10ab990: fdiv s2, s1, s8
// 0x10ab994: frintm s2, s2
// 0x10ab998: fmul s2, s2, s11
// 0x10ab99c: fadd s1, s1, s2
// 0x10ab9a0: fmin s2, s1, s8
// 0x10ab9a4: fcmp s1, #0.0
// 0x10ab9a8: fcsel s1, s2, s10, pl
// 0x10ab9ac: fadd s2, s1, s11
// 0x10ab9b0: fcmp s1, s13
// 0x10ab9b4: fmin s3, s0, s12
// 0x10ab9b8: fcsel s1, s2, s1, gt
// 0x10ab9bc: fcmp s0, #0.0
// 0x10ab9c0: fcsel s0, s3, s10, pl
// 0x10ab9c4: fmul s0, s0, s1
// 0x10ab9c8: fadd s0, s14, s0
// 0x10ab9cc: str s0, [x19, #0x290]
// 0x10ab9d0: ldp x20, x19, [sp, #0x90]
// 0x10ab9d4: ldp x22, x21, [sp, #0x80]
// 0x10ab9d8: ldp x24, x23, [sp, #0x70]
// 0x10ab9dc: ldp x26, x25, [sp, #0x60]
// 0x10ab9e0: ldr x30, [sp, #0x50]
// 0x10ab9e4: ldp d9, d8, [sp, #0x40]
// 0x10ab9e8: ldp d11, d10, [sp, #0x30]
// 0x10ab9ec: ldp d13, d12, [sp, #0x20]
// 0x10ab9f0: ldp d15, d14, [sp, #0x10]
// 0x10ab9f4: add sp, sp, #0xa0
// 0x10ab9f8: ret
// 0x10ab9fc: ldr x9, [x20]
// 0x10aba00: cbz x9, #0x10ac1ec
// 0x10aba04: ldr w10, [x9, #0x368]
// 0x10aba08: cmp w10, #6
// 0x10aba0c: b.ne #0x10aba28
// 0x10aba10: ldrb w9, [x9, #0x1d4]
// 0x10aba14: cbz w9, #0x10aba28
// 0x10aba18: ldr x9, [x19, #0x80]
// 0x10aba1c: cbz x9, #0x10ac1ec
// 0x10aba20: ldrb w9, [x9, #0x1a5]
// 0x10aba24: cbz w9, #0x10abaac
// 0x10aba28: ldr x9, [x19, #0x80]
// 0x10aba2c: cbz x9, #0x10ac1ec
// 0x10aba30: ldrb w9, [x9, #0x1a5]
// 0x10aba34: cbnz w9, #0x10abb28
// 0x10aba38: ldr x9, [x19, #0x78]
// 0x10aba3c: cbz x9, #0x10ac1ec
// 0x10aba40: ldr s0, [x9, #0x78]
// 0x10aba44: ldr s1, [x19, #0x234]
// 0x10aba48: ldr s2, [x19, #0x238]
// 0x10aba4c: ldr s4, [x19, #0x23c]
// 0x10aba50: adrp x10, #0x832000
// 0x10aba54: ldr s3, [x19, #0x2e8]
// 0x10aba58: fmul s1, s0, s1
// 0x10aba5c: fmul s2, s0, s2
// 0x10aba60: fmul s0, s0, s4
// 0x10aba64: ldr s4, [x10, #0x4c4]
// 0x10aba68: str s0, [x19, #0x2b4]
// 0x10aba6c: adrp x10, #0x832000
// 0x10aba70: str s1, [x19, #0x2ac]
// 0x10aba74: fmul s4, s3, s4
// 0x10aba78: fadd s0, s2, s4
// 0x10aba7c: str s0, [x19, #0x2b0]
// 0x10aba80: ldr s5, [x19, #0x240]
// 0x10aba84: ldr s1, [x10, #0x444]
// 0x10aba88: ldr s2, [x9, #0x78]
// 0x10aba8c: ldr s4, [x19, #0x244]
// 0x10aba90: ldr s6, [x19, #0x248]
// 0x10aba94: b #0x10abb08
// 0x10aba98: ldr s8, [x19, #0x280]
// 0x10aba9c: mov x0, xzr
// 0x10abaa0: bl #0x1b89b60
// 0x10abaa4: cbnz w21, #0x10ab384
// 0x10abaa8: b #0x10ab3f0
// 0x10abaac: ldr x9, [x19, #0x78]
// 0x10abab0: cbz x9, #0x10ac1ec
// 0x10abab4: ldr s0, [x9, #0x78]
// 0x10abab8: ldr s1, [x19, #0x264]
// 0x10ababc: ldr s2, [x19, #0x268]
// 0x10abac0: ldr s4, [x19, #0x26c]
// 0x10abac4: adrp x10, #0x832000
// 0x10abac8: ldr s3, [x19, #0x2e8]
// 0x10abacc: fmul s1, s0, s1
// 0x10abad0: fmul s2, s0, s2
// 0x10abad4: fmul s0, s0, s4
// 0x10abad8: ldr s4, [x10, #0x4c4]
// 0x10abadc: str s0, [x19, #0x2b4]
// 0x10abae0: adrp x10, #0x832000
// 0x10abae4: str s1, [x19, #0x2ac]
// 0x10abae8: fmul s4, s3, s4
// 0x10abaec: fadd s0, s2, s4
// 0x10abaf0: str s0, [x19, #0x2b0]
// 0x10abaf4: ldr s5, [x19, #0x270]
// 0x10abaf8: ldr s1, [x10, #0x444]
// 0x10abafc: ldr s2, [x9, #0x78]
// 0x10abb00: ldr s4, [x19, #0x274]
// 0x10abb04: ldr s6, [x19, #0x278]
// 0x10abb08: fmul s1, s3, s1
// 0x10abb0c: fmul s3, s2, s4
// 0x10abb10: fmul s0, s2, s5
// 0x10abb14: fadd s1, s3, s1
// 0x10abb18: fmul s2, s2, s6
// 0x10abb1c: str s0, [x19, #0x2a0]
// 0x10abb20: str s1, [x19, #0x2a4]
// 0x10abb24: str s2, [x19, #0x2a8]
// 0x10abb28: ldrb w8, [x8, #0x2dc]
// 0x10abb2c: cbz w8, #0x10abb88
// 0x10abb30: ldr x8, [x20]
// 0x10abb34: cbz x8, #0x10ac1ec
// 0x10abb38: ldr w8, [x8, #0x368]
// 0x10abb3c: cmp w8, #5
// 0x10abb40: b.ne #0x10abb88
// 0x10abb44: ldr s8, [x19, #0x200]
// 0x10abb48: ldr s9, [x19, #0x204]
// 0x10abb4c: mov x0, xzr
// 0x10abb50: bl #0x1b9ad30
// 0x10abb54: fadd s1, s8, s9
// 0x10abb58: fcmp s1, s0
// 0x10abb5c: b.le #0x10abb70
// 0x10abb60: ldr x8, [x20]
// 0x10abb64: cbz x8, #0x10ac1ec
// 0x10abb68: ldrb w8, [x8, #0x229]
// 0x10abb6c: cbz w8, #0x10abb88
// 0x10abb70: ldr s8, [x19, #0x280]
// 0x10abb74: mov x0, xzr
// 0x10abb78: add x21, x19, #0x280
// 0x10abb7c: bl #0x1b89b60
// 0x10abb80: fmov s1, wzr
// 0x10abb84: b #0x10abb9c
// 0x10abb88: ldr s8, [x19, #0x280]
// 0x10abb8c: mov x0, xzr
// 0x10abb90: add x21, x19, #0x280
// 0x10abb94: bl #0x1b89b60
// 0x10abb98: fmov s1, #1.00000000
// 0x10abb9c: fsub s2, s1, s8
// 0x10abba0: fmov s3, #9.00000000
// 0x10abba4: fabs s4, s2
// 0x10abba8: fcmp s2, #0.0
// 0x10abbac: fmul s2, s0, s3
// 0x10abbb0: fnmul s0, s0, s3
// 0x10abbb4: fcsel s0, s2, s0, ge
// 0x10abbb8: fadd s0, s8, s0
// 0x10abbbc: fcmp s4, s2
// 0x10abbc0: fcsel s0, s0, s1, hi
// 0x10abbc4: str s0, [x21]
// 0x10abbc8: ldr x8, [x20]
// 0x10abbcc: cbz x8, #0x10ac1ec
// 0x10abbd0: ldr w9, [x8, #0x368]
// 0x10abbd4: sub w9, w9, #1
// 0x10abbd8: cmp w9, #2
// 0x10abbdc: b.lo #0x10abbe8
// 0x10abbe0: ldrb w9, [x8, #0x229]
// 0x10abbe4: cbz w9, #0x10abc14
// 0x10abbe8: ldr s8, [x19, #0x200]
// 0x10abbec: ldr s9, [x19, #0x204]
// 0x10abbf0: ldr s10, [x19, #0x2f0]
// 0x10abbf4: mov x0, xzr
// 0x10abbf8: bl #0x1b9ad30
// 0x10abbfc: fmul s1, s9, s10
// 0x10abc00: fadd s1, s8, s1
// 0x10abc04: fcmp s1, s0
// 0x10abc08: b.gt #0x10abc2c
// 0x10abc0c: ldr x8, [x20]
// 0x10abc10: cbz x8, #0x10ac1ec
// 0x10abc14: ldrb w8, [x8, #0x1d4]
// 0x10abc18: cbnz w8, #0x10abc2c
// 0x10abc1c: ldr x8, [x19, #0x98]
// 0x10abc20: cbz x8, #0x10ac1ec
// 0x10abc24: ldrb w8, [x8, #0x17e]
// 0x10abc28: cbz w8, #0x10abe8c
// 0x10abc2c: ldr x8, [x22]
// 0x10abc30: cbz x8, #0x10ac1ec
// 0x10abc34: ldrb w9, [x8, #0x2e8]
// 0x10abc38: cbz w9, #0x10abc44
// 0x10abc3c: ldrb w9, [x8, #0x258]
// 0x10abc40: cbz w9, #0x10abd04
// 0x10abc44: ldr x9, [x20]
// 0x10abc48: cbz x9, #0x10ac1ec
// 0x10abc4c: ldrb w10, [x9, #0x1d4]
// 0x10abc50: cbz w10, #0x10abc60
// 0x10abc54: ldr w10, [x9, #0x368]
// 0x10abc58: cmp w10, #6
// 0x10abc5c: b.eq #0x10abd0c
// 0x10abc60: ldr s8, [x19, #0x2e8]
// 0x10abc64: mov x0, xzr
// 0x10abc68: bl #0x1b89b60
// 0x10abc6c: mov w8, #0x43b40000
// 0x10abc70: fmov s1, #7.00000000
// 0x10abc74: fmov s3, wzr
// 0x10abc78: fmov s2, w8
// 0x10abc7c: fmul s0, s0, s1
// 0x10abc80: fsub s1, s3, s8
// 0x10abc84: mov w8, #-0x3c4c0000
// 0x10abc88: fdiv s5, s1, s2
// 0x10abc8c: fmov s4, w8
// 0x10abc90: frintm s5, s5
// 0x10abc94: fmul s5, s5, s4
// 0x10abc98: fadd s1, s1, s5
// 0x10abc9c: mov w8, #0x43340000
// 0x10abca0: fmin s2, s1, s2
// 0x10abca4: fcmp s1, #0.0
// 0x10abca8: fmov s1, w8
// 0x10abcac: fcsel s2, s2, s3, pl
// 0x10abcb0: fmov s5, #1.00000000
// 0x10abcb4: fadd s4, s2, s4
// 0x10abcb8: fcmp s2, s1
// 0x10abcbc: fmin s5, s0, s5
// 0x10abcc0: fcsel s1, s4, s2, gt
// 0x10abcc4: fcmp s0, #0.0
// 0x10abcc8: fcsel s0, s5, s3, pl
// 0x10abccc: ldr s9, [x19, #0x200]
// 0x10abcd0: fmul s0, s0, s1
// 0x10abcd4: fadd s0, s8, s0
// 0x10abcd8: mov x0, xzr
// 0x10abcdc: str s0, [x19, #0x2e8]
// 0x10abce0: bl #0x1b9ad30
// 0x10abce4: adrp x8, #0x832000
// 0x10abce8: ldr s1, [x8, #0x334]
// 0x10abcec: fadd s1, s9, s1
// 0x10abcf0: fcmp s1, s0
// 0x10abcf4: b.le #0x10abdb8
// 0x10abcf8: mov w8, #1
// 0x10abcfc: strb w8, [x19, #0x2ec]
// 0x10abd00: b #0x10abdbc
// 0x10abd04: ldr x9, [x20]
// 0x10abd08: cbz x9, #0x10ac1ec
// 0x10abd0c: ldrb w10, [x9, #0x1d4]
// 0x10abd10: cbz w10, #0x10abd3c
// 0x10abd14: ldr w9, [x9, #0x368]
// 0x10abd18: cmp w9, #6
// 0x10abd1c: b.ne #0x10abd3c
// 0x10abd20: ldrb w9, [x8, #0x258]
// 0x10abd24: cbz w9, #0x10abf5c
// 0x10abd28: ldr s8, [x19, #0x2e8]
// 0x10abd2c: mov x0, xzr
// 0x10abd30: bl #0x1b89b60
// 0x10abd34: fmov s1, #10.00000000
// 0x10abd38: b #0x10abd4c
// 0x10abd3c: ldr s8, [x19, #0x2e8]
// 0x10abd40: mov x0, xzr
// 0x10abd44: bl #0x1b89b60
// 0x10abd48: fmov s1, wzr
// 0x10abd4c: mov w8, #0x43b40000
// 0x10abd50: fsub s1, s1, s8
// 0x10abd54: fmov s2, #7.00000000
// 0x10abd58: fmov s3, w8
// 0x10abd5c: mov w8, #-0x3c4c0000
// 0x10abd60: fmul s0, s0, s2
// 0x10abd64: fdiv s2, s1, s3
// 0x10abd68: fmov s4, w8
// 0x10abd6c: frintm s2, s2
// 0x10abd70: fmul s2, s2, s4
// 0x10abd74: fadd s1, s1, s2
// 0x10abd78: fmov s2, wzr
// 0x10abd7c: mov w8, #0x43340000
// 0x10abd80: fmin s3, s1, s3
// 0x10abd84: fcmp s1, #0.0
// 0x10abd88: fmov s1, w8
// 0x10abd8c: fcsel s3, s3, s2, pl
// 0x10abd90: fcmp s3, s1
// 0x10abd94: fmov s1, #1.00000000
// 0x10abd98: fadd s4, s3, s4
// 0x10abd9c: fmin s1, s0, s1
// 0x10abda0: fcsel s3, s4, s3, gt
// 0x10abda4: fcmp s0, #0.0
// 0x10abda8: fcsel s0, s1, s2, pl
// 0x10abdac: fmul s0, s0, s3
// 0x10abdb0: fadd s0, s8, s0
// 0x10abdb4: str s0, [x19, #0x2e8]
// 0x10abdb8: strb wzr, [x19, #0x2ec]
// 0x10abdbc: ldr s8, [x19, #0x284]
// 0x10abdc0: mov x0, xzr
// 0x10abdc4: bl #0x1b89b60
// 0x10abdc8: fmov s2, #1.00000000
// 0x10abdcc: fmov s1, #7.00000000
// 0x10abdd0: fsub s4, s2, s8
// 0x10abdd4: fmul s3, s0, s1
// 0x10abdd8: fnmul s0, s0, s1
// 0x10abddc: fcmp s4, #0.0
// 0x10abde0: fabd s5, s2, s8
// 0x10abde4: fcsel s0, s3, s0, ge
// 0x10abde8: fadd s0, s8, s0
// 0x10abdec: fcmp s5, s3
// 0x10abdf0: fcsel s0, s0, s2, hi
// 0x10abdf4: str s0, [x19, #0x284]
// 0x10abdf8: ldr s8, [x19, #0x200]
// 0x10abdfc: ldr s9, [x19, #0x208]
// 0x10abe00: mov x0, xzr
// 0x10abe04: bl #0x1b9ad30
// 0x10abe08: fadd s1, s8, s9
// 0x10abe0c: fcmp s1, s0
// 0x10abe10: b.le #0x10abe2c
// 0x10abe14: ldr x0, [x19, #0x20]
// 0x10abe18: cbz x0, #0x10ac1ec
// 0x10abe1c: adrp x8, #0x1e8e000
// 0x10abe20: ldr x8, [x8, #0x5b0]
// 0x10abe24: mov w2, #2
// 0x10abe28: b #0x10abe78
// 0x10abe2c: ldr x8, [x20]
// 0x10abe30: cbz x8, #0x10ac1ec
// 0x10abe34: ldrb w8, [x8, #0x239]
// 0x10abe38: cbz w8, #0x10abe64
// 0x10abe3c: ldr x8, [x19, #0x70]
// 0x10abe40: cbz x8, #0x10ac1ec
// 0x10abe44: ldrb w8, [x8, #0x2d0]
// 0x10abe48: cbz w8, #0x10abe64
// 0x10abe4c: ldr x0, [x19, #0x20]
// 0x10abe50: cbz x0, #0x10ac1ec
// 0x10abe54: adrp x8, #0x1e8e000
// 0x10abe58: ldr x8, [x8, #0x5b0]
// 0x10abe5c: mov w2, #5
// 0x10abe60: b #0x10abe78
// 0x10abe64: ldr x0, [x19, #0x20]
// 0x10abe68: cbz x0, #0x10ac1ec
// 0x10abe6c: adrp x8, #0x1e8e000
// 0x10abe70: ldr x8, [x8, #0x5b0]
// 0x10abe74: mov w2, #1
// 0x10abe78: ldr x1, [x8]
// 0x10abe7c: mov x3, xzr
// 0x10abe80: bl #0x1b67734
// 0x10abe84: strb wzr, [x19, #0x2fd]
// 0x10abe88: b #0x10ab738
// 0x10abe8c: ldr s8, [x19, #0x284]
// 0x10abe90: mov x0, xzr
// 0x10abe94: bl #0x1b89b60
// 0x10abe98: fmov s9, wzr
// 0x10abe9c: fmov s1, #7.00000000
// 0x10abea0: fsub s3, s9, s8
// 0x10abea4: fmul s2, s0, s1
// 0x10abea8: fnmul s0, s0, s1
// 0x10abeac: fcmp s3, #0.0
// 0x10abeb0: ldr s10, [x19, #0x2e8]
// 0x10abeb4: fabd s4, s9, s8
// 0x10abeb8: fcsel s0, s2, s0, ge
// 0x10abebc: fadd s0, s8, s0
// 0x10abec0: fcmp s4, s2
// 0x10abec4: fcsel s0, s0, s9, hi
// 0x10abec8: mov x0, xzr
// 0x10abecc: str s0, [x19, #0x284]
// 0x10abed0: bl #0x1b89b60
// 0x10abed4: mov w8, #0x43b40000
// 0x10abed8: fmov s1, #9.00000000
// 0x10abedc: fmov s2, w8
// 0x10abee0: fsub s3, s9, s10
// 0x10abee4: mov w8, #-0x3c4c0000
// 0x10abee8: fmul s0, s0, s1
// 0x10abeec: fdiv s1, s3, s2
// 0x10abef0: fmov s4, w8
// 0x10abef4: frintm s1, s1
// 0x10abef8: fmul s1, s1, s4
// 0x10abefc: fadd s1, s3, s1
// 0x10abf00: mov w8, #0x43340000
// 0x10abf04: fmin s2, s1, s2
// 0x10abf08: fcmp s1, #0.0
// 0x10abf0c: fmov s1, w8
// 0x10abf10: fcsel s2, s2, s9, pl
// 0x10abf14: fmov s3, #1.00000000
// 0x10abf18: fadd s4, s2, s4
// 0x10abf1c: fcmp s2, s1
// 0x10abf20: ldr x8, [x19, #0x90]
// 0x10abf24: fmin s3, s0, s3
// 0x10abf28: fcsel s1, s4, s2, gt
// 0x10abf2c: fcmp s0, #0.0
// 0x10abf30: fcsel s0, s3, s9, pl
// 0x10abf34: fmul s0, s0, s1
// 0x10abf38: fadd s0, s10, s0
// 0x10abf3c: str s0, [x19, #0x2e8]
// 0x10abf40: strb wzr, [x19, #0x2ec]
// 0x10abf44: cbz x8, #0x10ac1ec
// 0x10abf48: ldrb w8, [x8, #0x229]
// 0x10abf4c: cbz w8, #0x10abdf8
// 0x10abf50: mov w8, #-0x3e800000
// 0x10abf54: str w8, [x19, #0x200]
// 0x10abf58: b #0x10abdf8
// 0x10abf5c: ldr w9, [x19, #0x22c]
// 0x10abf60: cmp w9, #4
// 0x10abf64: b.eq #0x10abf70
// 0x10abf68: cmp w9, #1
// 0x10abf6c: b.ne #0x10ac1a0
// 0x10abf70: ldr s8, [x19, #0x2e8]
// 0x10abf74: mov x0, xzr
// 0x10abf78: bl #0x1b89b60
// 0x10abf7c: fmov s1, #-30.00000000
// 0x10abf80: b #0x10abd4c
// 0x10abf84: mov x0, xzr
// 0x10abf88: bl #0x1b9ae30
// 0x10abf8c: fmov s1, #7.00000000
// 0x10abf90: fmov s2, #1.00000000
// 0x10abf94: fmul s0, s0, s1
// 0x10abf98: fmov s3, wzr
// 0x10abf9c: fmin s1, s0, s2
// 0x10abfa0: fcmp s0, #0.0
// 0x10abfa4: fcsel s0, s1, s3, pl
// 0x10abfa8: fsub s1, s3, s8
// 0x10abfac: ldr s9, [x19, #0x1c8]
// 0x10abfb0: ldr s10, [x19, #0x1b8]
// 0x10abfb4: fmul s0, s1, s0
// 0x10abfb8: fadd s0, s8, s0
// 0x10abfbc: mov x0, xzr
// 0x10abfc0: str s0, [x19, #0x1cc]
// 0x10abfc4: bl #0x1b9ae30
// 0x10abfc8: fmov s1, #1.00000000
// 0x10abfcc: fcmp s0, #0.0
// 0x10abfd0: fmov s2, wzr
// 0x10abfd4: fmin s0, s0, s1
// 0x10abfd8: fsub s3, s10, s9
// 0x10abfdc: ldr s8, [x19, #0x1b0]
// 0x10abfe0: fcsel s0, s0, s2, pl
// 0x10abfe4: ldr s10, [x19, #0x1ac]
// 0x10abfe8: fmul s0, s3, s0
// 0x10abfec: fadd s0, s9, s0
// 0x10abff0: mov x0, xzr
// 0x10abff4: str s0, [x19, #0x1c8]
// 0x10abff8: bl #0x1b9ae30
// 0x10abffc: mov w8, #0x42000000
// 0x10ac000: fsub s1, s10, s8
// 0x10ac004: fmov s3, w8
// 0x10ac008: fmul s4, s0, s3
// 0x10ac00c: fnmul s0, s0, s3
// 0x10ac010: fcmp s1, #0.0
// 0x10ac014: fabd s2, s10, s8
// 0x10ac018: ldr s9, [x19, #0x1e4]
// 0x10ac01c: ldr s11, [x19, #0x1e0]
// 0x10ac020: fcsel s0, s4, s0, ge
// 0x10ac024: fadd s0, s8, s0
// 0x10ac028: fcmp s2, s4
// 0x10ac02c: fcsel s0, s0, s10, hi
// 0x10ac030: mov x0, xzr
// 0x10ac034: str s0, [x19, #0x1b0]
// 0x10ac038: bl #0x1b9ae30
// 0x10ac03c: fmov s1, #8.00000000
// 0x10ac040: fsub s2, s11, s9
// 0x10ac044: fmul s4, s0, s1
// 0x10ac048: fnmul s0, s0, s1
// 0x10ac04c: fcmp s2, #0.0
// 0x10ac050: fabd s3, s11, s9
// 0x10ac054: ldr s8, [x19, #0x188]
// 0x10ac058: ldr s10, [x19, #0x180]
// 0x10ac05c: fcsel s0, s4, s0, ge
// 0x10ac060: fadd s0, s9, s0
// 0x10ac064: fcmp s3, s4
// 0x10ac068: fcsel s0, s0, s11, hi
// 0x10ac06c: mov x0, xzr
// 0x10ac070: str s0, [x19, #0x1e4]
// 0x10ac074: bl #0x1b9ae30
// 0x10ac078: fsub s1, s10, s8
// 0x10ac07c: fneg s3, s0
// 0x10ac080: fcmp s1, #0.0
// 0x10ac084: fabd s2, s10, s8
// 0x10ac088: fcsel s1, s0, s3, ge
// 0x10ac08c: fadd s1, s8, s1
// 0x10ac090: fcmp s2, s0
// 0x10ac094: fcsel s0, s1, s10, hi
// 0x10ac098: str s0, [x19, #0x188]
// 0x10ac09c: b #0x10a93cc
// 0x10ac0a0: adrp x8, #0x832000
// 0x10ac0a4: ldr s1, [x8, #0x444]
// 0x10ac0a8: fcmp s0, s1
// 0x10ac0ac: b.pl #0x10ac144
// 0x10ac0b0: ldr x21, [x19, #0x20]
// 0x10ac0b4: mov x0, xzr
// 0x10ac0b8: bl #0x1b89b60
// 0x10ac0bc: cbz x21, #0x10ac1ec
// 0x10ac0c0: adrp x25, #0x1e8e000
// 0x10ac0c4: ldr x25, [x25, #0x598]
// 0x10ac0c8: ldr s10, [x24, #0x3a0]
// 0x10ac0cc: mov v2.16b, v0.16b
// 0x10ac0d0: fmov s0, #1.00000000
// 0x10ac0d4: ldr x1, [x25]
// 0x10ac0d8: mov x0, x21
// 0x10ac0dc: mov v1.16b, v10.16b
// 0x10ac0e0: mov x2, xzr
// 0x10ac0e4: bl #0x1b67484
// 0x10ac0e8: ldr x21, [x19, #0xc8]
// 0x10ac0ec: mov x0, xzr
// 0x10ac0f0: bl #0x1b89b60
// 0x10ac0f4: cbz x21, #0x10ac1ec
// 0x10ac0f8: ldr x1, [x25]
// 0x10ac0fc: mov v2.16b, v0.16b
// 0x10ac100: fmov s0, #1.00000000
// 0x10ac104: mov x0, x21
// 0x10ac108: mov v1.16b, v10.16b
// 0x10ac10c: mov x2, xzr
// 0x10ac110: bl #0x1b67484
// 0x10ac114: ldr x8, [x19, #0x68]
// 0x10ac118: mov w9, #2
// 0x10ac11c: str w9, [x19, #0x22c]
// 0x10ac120: mov w9, #0x3f800000
// 0x10ac124: str w9, [x19, #0x20c]
// 0x10ac128: cbz x8, #0x10ac1ec
// 0x10ac12c: ldrb w8, [x8, #0x2dc]
// 0x10ac130: cbz w8, #0x10a96e0
// 0x10ac134: mov x0, xzr
// 0x10ac138: bl #0x1b9ad30
// 0x10ac13c: str s0, [x19, #0x214]
// 0x10ac140: b #0x10a96e0
// 0x10ac144: str wzr, [x19, #0x22c]
// 0x10ac148: b #0x10a96e0
// 0x10ac14c: ldr x8, [x20]
// 0x10ac150: cbz x8, #0x10ac1ec
// 0x10ac154: ldr w8, [x8, #0x368]
// 0x10ac158: mov w9, #0x194
// 0x10ac15c: mov w10, #0x198
// 0x10ac160: ldr w21, [x19, #0x22c]
// 0x10ac164: cmp w8, #0
// 0x10ac168: csel x8, x10, x9, eq
// 0x10ac16c: ldr s8, [x19, x8]
// 0x10ac170: cmp w21, #2
// 0x10ac174: str s8, [x19, #0x1a0]
// 0x10ac178: b.ne #0x10ac1c8
// 0x10ac17c: ldr s9, [x19, #0x1ec]
// 0x10ac180: mov x0, xzr
// 0x10ac184: bl #0x1b9ae30
// 0x10ac188: mov w8, #0x42200000
// 0x10ac18c: mov w9, #0x43480000
// 0x10ac190: fmov s1, w8
// 0x10ac194: fadd s8, s8, s1
// 0x10ac198: fmov s1, w9
// 0x10ac19c: b #0x10a9e08
// 0x10ac1a0: ldrb w21, [x8, #0x2d0]
// 0x10ac1a4: ldr s8, [x19, #0x2e8]
// 0x10ac1a8: mov x0, xzr
// 0x10ac1ac: bl #0x1b89b60
// 0x10ac1b0: cbz w21, #0x10abd48
// 0x10ac1b4: fmov s1, #-20.00000000
// 0x10ac1b8: b #0x10abd4c
// 0x10ac1bc: ldrb w9, [x19, #0x27c]
// 0x10ac1c0: cbnz w9, #0x10ab0fc
// 0x10ac1c4: b #0x10ab0f4
// 0x10ac1c8: ldr s9, [x19, #0x1ec]
// 0x10ac1cc: mov x0, xzr
// 0x10ac1d0: bl #0x1b9ae30
// 0x10ac1d4: cmp w21, #3
// 0x10ac1d8: b.ne #0x10a9e00
// 0x10ac1dc: fmov s1, #-20.00000000
// 0x10ac1e0: mov w8, #0x43480000
// 0x10ac1e4: fadd s8, s8, s1
// 0x10ac1e8: b #0x10a9e04
// 0x10ac1ec: bl #0xf7db74
// 0x10ac1f0: bl #0xf7db7c
```

## `PlayerCharacter.SelectCurrentWeapon` — RVA `0xcac1f4`

- Decompiled symbol: `PlayerCharacter_SelectCurrentWeapon`
- Metadata signature: `public void SelectCurrentWeapon() { }`
- Native interval: `1028` bytes
- Result: `pseudocode`
- Heuristic layout hint: `PlayerCharacter_Recovered` matched 6 offsets against `PlayerCharacter` metadata (confidence 1.00).

```c
typedef struct PlayerCharacter_Recovered {
    char padding_0[32];
    long long anim;
    char padding_28[104];
    struct struct_1 *WeaponBehaviorComponent;
    struct struct_2 *PlayerWeaponsComponent;
    char padding_a0[40];
    long long fpBodyAnim;
    char padding_d0[40];
    struct struct_3 *weaponModels;
    char padding_100[484];
    unsigned int lastWeapon;
} PlayerCharacter_Recovered;

typedef struct struct_20 {
    char padding_0[152];
    unsigned long long field_98;
    char padding_a0[222];
    char field_17e;
} struct_20;

typedef struct struct_19 {
    char padding_0[32];
    struct struct_17 *field_20;
} struct_19;

typedef struct struct_5 {
    char padding_0[16];
    long long field_10;
} struct_5;

typedef struct struct_6 {
    char padding_0[16];
    unsigned long long field_10;
} struct_6;

typedef struct struct_7 {
    char padding_0[24];
    long long field_18;
} struct_7;

typedef struct struct_8 {
    char padding_0[24];
    long long field_18;
} struct_8;

typedef struct struct_9 {
    char padding_0[32];
    long long field_20;
} struct_9;

typedef struct struct_10 {
    char padding_0[32];
    long long field_20;
} struct_10;

typedef struct struct_11 {
    char padding_0[16];
    long long field_10;
} struct_11;

typedef struct struct_12 {
    char padding_0[24];
    long long field_18;
} struct_12;

typedef struct struct_13 {
    char padding_0[24];
    long long field_18;
} struct_13;

typedef struct struct_14 {
    char padding_0[32];
    long long field_20;
} struct_14;

typedef struct struct_15 {
    char padding_0[32];
    long long field_20;
} struct_15;

typedef struct struct_1 {
    char padding_0[292];
    int field_124;
    char padding_128[576];
    unsigned int field_368;
} struct_1;

typedef struct struct_2 {
    char padding_0[152];
    unsigned long long field_98;
    char padding_a0[222];
    char field_17e;
} struct_2;

typedef struct struct_3 {
    char padding_0[32];
    struct PlayerCharacter_Recovered *field_20;
} struct_3;

typedef struct struct_17 {
    char padding_0[32];
    unsigned long long field_20;
    char padding_28[104];
    struct struct_18 *field_90;
    struct struct_16 *field_98;
    char padding_a0[40];
    unsigned long long field_c8;
    char padding_d0[40];
    struct struct_19 *field_f8;
    char padding_100[484];
    unsigned int field_2e4;
} struct_17;

typedef struct struct_18 {
    char padding_0[292];
    unsigned int field_124;
    char padding_128[576];
    unsigned int field_368;
} struct_18;

typedef struct struct_16 {
    char padding_0[152];
    unsigned long long field_98;
    char padding_a0[222];
    char field_17e;
} struct_16;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern long long g_1ef8178;
extern long long g_1ef8180;
extern char g_1fab4c3;

struct_4 * PlayerCharacter_SelectCurrentWeapon(struct_4 *ptr)
{
    struct_4 *v0;  // x0
    struct_4 *v1;  // x0
    struct_8 *v10;  // x0
    struct_9 *v11;  // x0
    struct_10 *v12;  // x0
    struct_11 *v13;  // x0
    struct_12 *v14;  // x0
    struct_13 *v15;  // x0
    struct_14 *v16;  // x0
    struct_15 *v17;  // x0
    struct_4 *v2;  // x0
    struct_19 *p;  // x8
    unsigned int v4;  // w20
    struct_4 *v5;  // x0
    struct_5 *v6;  // x0
    unsigned long v7;  // x0
    struct_6 *v8;  // x0
    struct_7 *v9;  // x0

    v0 = ptr;
    if (!(g_1fab4c3 & 1))
    {
        sub_f7d92c(&g_1ef8178);
        sub_f7d92c(&g_1ef8180);
        sub_f7d92c(&g_1ef0c58);
        v1 = sub_f7d92c("g&");
        g_1fab4c3 = 1;
        v0 = v1;
    }
    v2 = v0;
    if (ptr->field_98 && ptr->field_98->field_98)
    {
        if (ptr->field_2e4 == *((int *)(ptr->field_98->field_98 + 292)))
            return v2;
        p = ptr->field_f8;
        if (p)
        {
            v4 = 0;
            do
            {
                v5 = p->field_20;
                if (!v5)
                    break;
                if (*((int *)&v5->padding_0[24]) <= v4)
                    return v5;
                if (!ptr->field_90 || !((v6 = (struct_5 *)(unsigned long long)sub_14a30c0(), v6)))
                    break;
                if (!g_1ef0c58->field_e0)
                    sub_f7da5c(g_1ef0c58);
                v7 = Object__op_Inequality(v6->field_10, 0, 0);
                if (v4 == ptr->field_90->field_124)
                {
                    if (((char)v7 & 1))
                    {
                        if (!ptr->field_90 || !ptr->field_f8 || !ptr->field_f8->field_20 || !((v8 = (struct_6 *)(unsigned long long)sub_14a30c0(ptr->field_f8->field_20, (unsigned long long)v4, g_1ef8180), v8 && v8->field_10)))
                            break;
                        GameObject__SetActive();
                    }
                    if (!ptr->field_f8 || !ptr->field_f8->field_20 || !((v9 = (struct_7 *)(unsigned long long)sub_14a30c0(ptr->field_f8->field_20, (unsigned long long)v4, g_1ef8180), v9)))
                        break;
                    if (!g_1ef0c58->field_e0)
                        sub_f7da5c(g_1ef0c58);
                    if (((char)Object__op_Inequality(v9->field_18, 0, 0) & 1))
                    {
                        if (!ptr->field_f8 || !ptr->field_f8->field_20 || !((v10 = (struct_8 *)(unsigned long long)sub_14a30c0(ptr->field_f8->field_20, (unsigned long long)v4, g_1ef8180), v10 && v10->field_18)))
                            break;
                        GameObject__SetActive(v10->field_18, 1, 0);
                    }
                    if (!ptr->field_f8 || !ptr->field_f8->field_20 || !((v11 = (struct_9 *)(unsigned long long)sub_14a30c0(ptr->field_f8->field_20, (unsigned long long)v4, g_1ef8180), v11)))
                        break;
                    if (!g_1ef0c58->field_e0)
                        sub_f7da5c(g_1ef0c58);
                    if (((char)Object__op_Inequality(v11->field_20, 0, 0) & 1))
                    {
                        if (!ptr->field_f8 || !ptr->field_f8->field_20 || !((v12 = (struct_10 *)(unsigned long long)sub_14a30c0(ptr->field_f8->field_20, (unsigned long long)v4, g_1ef8180), v12 && v12->field_20)))
                            break;
                        GameObject__SetActive(v12->field_20, 1, 0);
                    }
                    if (!ptr->field_90 || !ptr->field_20 || !((Animator__SetInteger(ptr->field_20, g_1f0fb88, (unsigned long long)ptr->field_90->field_368, 0), ptr->field_90 && ptr->field_c8 && (Animator__SetInteger(ptr->field_c8, g_1f0fb88, (unsigned long long)ptr->field_90->field_368, 0), ptr->field_90))))
                        break;
                    ptr->field_2e4 = ptr->field_90->field_124;
                }
                else
                {
                    if (((char)v7 & 1))
                    {
                        if (!ptr->field_f8 || !ptr->field_f8->field_20 || !((v13 = (struct_11 *)(unsigned long long)sub_14a30c0(ptr->field_f8->field_20, (unsigned long long)v4, g_1ef8180), v13 && v13->field_10)))
                            break;
                        GameObject__SetActive(v13->field_10, 0, 0);
                    }
                    if (!ptr->field_98)
                        break;
                    if (ptr->field_98->field_17e)
                        continue;
                    if (!ptr->field_f8 || !ptr->field_f8->field_20 || !((v14 = (struct_12 *)(unsigned long long)sub_14a30c0(ptr->field_f8->field_20, (unsigned long long)v4, g_1ef8180), v14)))
                        break;
                    if (!g_1ef0c58->field_e0)
                        sub_f7da5c(g_1ef0c58);
                    if (((char)Object__op_Inequality(v14->field_18, 0, 0) & 1))
                    {
                        if (!ptr->field_f8 || !ptr->field_f8->field_20 || !((v15 = (struct_13 *)(unsigned long long)sub_14a30c0(ptr->field_f8->field_20, (unsigned long long)v4, g_1ef8180), v15 && v15->field_18)))
                            break;
                        GameObject__SetActive(v15->field_18, 0, 0);
                    }
                    if (!ptr->field_f8 || !ptr->field_f8->field_20 || !((v16 = (struct_14 *)(unsigned long long)sub_14a30c0(ptr->field_f8->field_20, (unsigned long long)v4, g_1ef8180), v16)))
                        break;
                    if (!g_1ef0c58->field_e0)
                        sub_f7da5c(g_1ef0c58);
                    if (!(Object__op_Inequality(v16->field_20, 0, 0) & 1))
                        continue;
                    if (!ptr->field_f8 || !ptr->field_f8->field_20 || !((v17 = (struct_15 *)(unsigned long long)sub_14a30c0(ptr->field_f8->field_20, (unsigned long long)v4, g_1ef8180), v17 && v17->field_20)))
                        break;
                    GameObject__SetActive(v17->field_20, 0, 0);
                }
            } while ((p = (struct_19 *)ptr->field_f8, v4 += 1, p));
        }
    }
    sub_f7db74();
}
```

## `PlayerCharacter.LateUpdate` — RVA `0xcac5f8`

- Decompiled symbol: `PlayerCharacter_LateUpdate`
- Metadata signature: `private void LateUpdate() { }`
- Native interval: `416` bytes
- Result: `pseudocode`
- Heuristic layout hint: `PlayerCharacter_Recovered` matched 6 offsets against `PlayerCharacter` metadata (confidence 1.00).

```c
typedef struct PlayerCharacter_Recovered {
    char padding_0[40];
    long long headBone;
    long long chestBone;
    long long spineBone;
    char padding_40[40];
    struct struct_1 *walkerComponent;
    char padding_70[584];
    unsigned int headRotation;
    char padding_2bc[65];
    char rotateHead;
} PlayerCharacter_Recovered;

typedef struct struct_1 {
    char padding_0[720];
    char field_2d0;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab4c2;

long long PlayerCharacter_LateUpdate(struct_2 *ptr)
{
    unsigned int v0;  // s0
    unsigned long v1;  // 4129
    long long v2;  // x20
    long long v3;  // x20
    long long v4;  // x0
    unsigned long long v5;  // x0

    if (!(g_1fab4c2 & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab4c2 = 1;
    }
    if (ptr->field_2fd)
    {
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        if (((char)Object__op_Implicit(ptr->field_28, 0) & 1))
        {
            v0 = ptr->field_2b8;
            v1 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v0, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v0, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v0, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v0, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v0, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v0, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
            if (!((char)v1))
            {
                if (ptr->field_68)
                {
                    v2 = ptr->field_28;
                    if (!v2)
                        sub_f7db74();
                    Transform__get_eulerAngles(v2, 0);
                    Transform__set_eulerAngles(v2, 0);
                }
                else
                {
                    sub_f7db74();
                }
            }
        }
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (((char)Object__op_Implicit(ptr->field_38, 0) & 1))
    {
        v3 = ptr->field_38;
        if (!v3)
            sub_f7db74();
        Transform__get_eulerAngles(v3, 0);
        Transform__set_eulerAngles(v3, 0);
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v4 = Object__op_Implicit(ptr->field_30, 0);
    if (!((char)v4 & 1))
        return v4;
    if (ptr->field_30)
    {
        Transform__get_eulerAngles(ptr->field_30, 0);
        v5 = Transform__set_eulerAngles();
        return Transform__set_eulerAngles();
    }
    sub_f7db74();
}
```

## `PlayerCharacter.ctor` — RVA `0xcac798`

- Decompiled symbol: `PlayerCharacter_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `228` bytes
- Result: `pseudocode`
- Heuristic layout hint: `PlayerCharacter_Recovered` matched 20 offsets against `PlayerCharacter` metadata (confidence 0.95).

```c
typedef struct PlayerCharacter_Recovered {
    char padding_0[216];
    char displayVisibleBody;
    char padding_d9[39];
    unsigned long long weaponModelParentAngles;
    unsigned int field_108;
    char padding_10c[24];
    unsigned int boneSpeed;
    char padding_128[12];
    unsigned int slerpSpeed;
    char padding_138[4];
    unsigned long long idleTime;
    char padding_144[60];
    uint128_t modelStandScale;
    char padding_190[12];
    unsigned int yawAngUnarmedCrouchStrafe;
    char padding_1a0[4];
    unsigned long long modelPitch;
    unsigned int modelPitchRun;
    char padding_1b0[4];
    uint128_t modelForward;
    char padding_1c4[12];
    uint128_t modelUpFP;
    unsigned int modelUpRun;
    char padding_1e4[24];
    uint128_t inputSmoothingSpeed;
    char padding_20c[24];
    unsigned int proneTransitionLength;
    char padding_228[144];
    unsigned long long headRotation;
    char padding_2c0[4];
    unsigned int reloadStartTime;
    char padding_2c8[4];
    unsigned long long reloadDurationRifle;
    unsigned int reloadDurationShotgun;
    char padding_2d8[8];
    unsigned int switchDuration;
    char padding_2e4[16];
    unsigned long long offhandMeleeTime;
} PlayerCharacter_Recovered;

long long PlayerCharacter_ctor(struct_0 *ptr)
{
    struct_0 *p;  // x8

    ptr->field_d8 = 1;
    ptr->field_108 = 1132901827;
    ptr->field_124 = 0x40800000;
    ptr->field_134 = 0x41600000;
    ptr->field_100 = 4866795235720659927;
    p = &(&ptr->padding_138)[1];
    *((unsigned long long *)&p->padding_0[0]) = 0xc2000000c2000000;
    *((uint128_t *)&ptr->padding_144[56]) = 84339516336375052015308778491318842163;
    *((unsigned int *)((char *)&ptr->field_180 + 12)) = 0xc1c80000;
    *((unsigned long long *)&p->padding_0[104]) = 0xc0e00000c0e00000;
    ptr->field_19c = 0xc1a00000;
    *((uint128_t *)&p->padding_0[120]) = 255959465997320705669107797959034221363;
    ptr->field_1b4 = 81481676177128747894296548506590615962;
    *((unsigned int *)&ptr->padding_1c4[0]) = 1066192077;
    *((uint128_t *)&p->padding_0[192]) = 0x3ecccccd40000000c200000040800000;
    *((unsigned long long *)&ptr->padding_228[108]) = 4525216907501187891;
    *((unsigned int *)((char *)&ptr->field_1fc + 4)) = 1060320051;
    *((unsigned int *)&ptr->padding_228[120]) = 0xc2000000;
    *((unsigned long long *)&p->field_180) = 0x3f80000040100000;
    *((unsigned int *)&ptr->padding_228[136]) = 0x3f800000;
    *((unsigned int *)&ptr->field_2b8) = 1050253722;
    p->field_1a4 = 4525216907482061865;
}
```
