# Native pseudocode: MovePlayerAndCamera

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `MovePlayerAndCamera.Start` — RVA `0xc8beb0`

- Decompiled symbol: `MovePlayerAndCamera_Start`
- Metadata signature: `private void Start() { }`
- Native interval: `720` bytes
- Result: `pseudocode`
- Heuristic layout hint: `MovePlayerAndCamera_Recovered` matched 14 offsets against `MovePlayerAndCamera` metadata (confidence 1.00).

```c
typedef struct struct_1 {
    char padding_0[40];
    struct struct_1 *field_28;
    struct struct_1 *field_30;
    char padding_38[104];
    unsigned long long field_a0;
    unsigned long long field_a8;
} struct_1;

typedef struct MovePlayerAndCamera_Recovered {
    char padding_0[32];
    struct struct_2 *CinemaCameraObj;
    char padding_28[18];
    char noCrosshair;
    char padding_3b[5];
    struct struct_3 *FPSWeaponsObj;
    struct struct_4 *FPSPlayerObj;
    struct struct_5 *FPSCameraObj;
    struct struct_6 *MainCameraObj;
    long long PlayerCharacterObj;
    long long PlayerCharacterComponent;
    struct struct_7 *CameraControlComponent;
    long long MouseLookComponent;
    struct struct_8 *FPSPlayerComponent;
    long long FPSWalkerComponent;
    long long PlayerWeaponsComponent;
    long long IronsightsComponent;
} MovePlayerAndCamera_Recovered;

typedef struct struct_10 {
    char padding_0[745];
    char field_2e9;
} struct_10;

typedef struct struct_2 {
    char padding_0[40];
    struct struct_2 *field_28;
    struct struct_2 *field_30;
    char padding_38[104];
    unsigned long long field_a0;
    unsigned long long field_a8;
} struct_2;

typedef struct struct_3 {
    char padding_0[40];
    struct struct_3 *field_28;
    struct struct_3 *field_30;
    char padding_38[104];
    unsigned long long field_a0;
    unsigned long long field_a8;
} struct_3;

typedef struct struct_4 {
    char padding_0[40];
    struct struct_4 *field_28;
    struct struct_4 *field_30;
    char padding_38[104];
    unsigned long long field_a0;
    unsigned long long field_a8;
} struct_4;

typedef struct struct_5 {
    char padding_0[40];
    struct struct_5 *field_28;
    struct struct_5 *field_30;
    char padding_38[104];
    unsigned long long field_a0;
    unsigned long long field_a8;
} struct_5;

typedef struct struct_6 {
    char padding_0[40];
    struct struct_6 *field_28;
    struct struct_6 *field_30;
    char padding_38[104];
    unsigned long long field_a0;
    unsigned long long field_a8;
} struct_6;

typedef struct struct_7 {
    char padding_0[40];
    struct struct_7 *field_28;
    struct struct_7 *field_30;
    char padding_38[104];
    long long field_a0;
    long long field_a8;
} struct_7;

typedef struct struct_8 {
    char padding_0[745];
    char field_2e9;
} struct_8;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern long long g_1efeb68;
extern long long g_1efebb8;
extern long long g_1efebc0;
extern long long g_1efec18;
extern long long g_1efec90;
extern long long g_1efecd8;
extern char g_1fab43a;

struct_1 * MovePlayerAndCamera_Start(struct_9 *ptr)
{
    struct_1 *v0;  // x0
    struct_9 *p;  // x20
    struct_9 *addr;  // x21
    struct_9 *ptr15;  // x21
    struct_1 *v12;  // x0
    struct_9 *ptr3;  // x21
    struct_9 *ptr13;  // x21
    struct_1 *v15;  // x0
    long long v16;  // x0
    struct_9 *ptr4;  // x20
    struct_9 *ptr16;  // x20
    struct_10 *v19;  // x0
    struct_9 *ptr14;  // x20
    struct_9 *ptr5;  // x20
    struct_9 *ptr17;  // x20
    long long v22;  // x0
    struct_9 *ptr6;  // x20
    struct_9 *ptr18;  // x20
    long long v25;  // x0
    struct_9 *ptr7;  // x20
    struct_9 *ptr19;  // x20
    long long v28;  // x0
    struct_9 *ptr8;  // x20
    struct_1 *v3;  // x0
    struct_9 *v30;  // x20
    unsigned long v31;  // x1
    struct_9 *ptr9;  // x20
    struct_9 *idx14;  // x20
    unsigned long v34;  // x1
    struct_9 *ptr10;  // x20
    struct_9 *v36;  // x20
    struct_9 *ptr11;  // x21
    struct_9 *v5;  // x21
    struct_1 *v6;  // x1
    struct_9 *ptr12;  // x21
    struct_9 *idx4;  // x21
    struct_1 *v9;  // x1

    if (!(g_1fab43a & 1))
    {
        sub_f7d92c(&g_1efeb68);
        sub_f7d92c(&g_1efebb8);
        sub_f7d92c(&g_1efebc0);
        sub_f7d92c(&g_1efec18);
        sub_f7d92c(&g_1efec90);
        sub_f7d92c(&g_1efecd8);
        sub_f7d92c(&g_1ef0c58);
        g_1fab43a = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (((char)Object__op_Implicit(ptr->field_20, 0) & 1))
    {
        v0 = ptr->field_20;
        if (!v0)
            sub_f7db74(v0);
        GameObject__SetActive(v0, 0, 0);
    }
    p = ptr;
    v0 = p->field_58;
    ptr14 = &p->field_58;
    if (v0)
    {
        v3 = sub_1249224(v0, g_1efeb68);
        ptr11 = ptr;
        ptr11->field_70 = v3;
        v5 = &ptr11->field_70;
        v0 = sub_f7d8d0(v5, v3);
        if (*((long long *)&v5->padding_0[0]))
        {
            v6 = *((long long *)(*((long long *)&v5->padding_0[0]) + 40));
            ptr12 = ptr;
            ptr12->field_48 = v6;
            idx4 = &ptr12->field_48;
            v0 = sub_f7d8d0(idx4, v6);
            if (*((long long *)&idx4->padding_28[0]))
            {
                v9 = *((long long *)(*((long long *)&idx4->padding_28[0]) + 48));
                addr = ptr;
                addr->field_40 = v9;
                ptr15 = &addr->field_40;
                sub_f7d8d0(ptr15, v9);
                v0 = *((long long *)&ptr15->padding_28[8]);
                if (v0)
                {
                    v0 = Component__get_transform(v0, 0);
                    if (v0)
                    {
                        v0 = Transform__get_parent();
                        if (v0)
                        {
                            v0 = Component__get_transform();
                            if (v0)
                            {
                                v12 = Component__get_gameObject();
                                ptr3 = ptr;
                                ptr3->field_50 = v12;
                                ptr13 = &ptr3->field_50;
                                sub_f7d8d0(ptr13, v12);
                                v0 = Camera__get_main(0);
                                if (v0)
                                {
                                    v0 = Component__get_transform();
                                    if (v0)
                                    {
                                        v15 = Component__get_gameObject();
                                        *((struct_1 **)&ptr14->padding_0[0]) = v15;
                                        sub_f7d8d0(ptr14, v15);
                                        v0 = *((long long *)&ptr13->padding_0[0]);
                                        if (v0)
                                        {
                                            v16 = sub_1249224(v0, g_1efecd8);
                                            ptr4 = ptr;
                                            ptr4->field_78 = v16;
                                            ptr16 = &ptr4->field_78;
                                            sub_f7d8d0(ptr16, v16);
                                            v0 = *((long long *)&ptr16->padding_28[8]);
                                            if (v0)
                                            {
                                                v19 = sub_1249224(v0, g_1efebb8);
                                                ptr5 = ptr;
                                                ptr5->field_80 = v19;
                                                ptr17 = &ptr5->field_80;
                                                sub_f7d8d0(ptr17, v19);
                                                v0 = *((long long *)&ptr17->padding_28[16]);
                                                if (v0)
                                                {
                                                    v22 = sub_1249224(v0, g_1efebc0);
                                                    ptr6 = ptr;
                                                    ptr6->field_88 = v22;
                                                    ptr18 = &ptr6->field_88;
                                                    sub_f7d8d0(ptr18, v22);
                                                    v0 = ptr18->field_48;
                                                    if (v0)
                                                    {
                                                        v25 = sub_1249224(v0, g_1efec90);
                                                        ptr7 = ptr;
                                                        ptr7->field_90 = v25;
                                                        ptr19 = &ptr7->field_90;
                                                        sub_f7d8d0(ptr19, v25);
                                                        v0 = ptr19->field_48;
                                                        if (v0)
                                                        {
                                                            v28 = sub_1249224(v0, g_1efec18);
                                                            ptr8 = ptr;
                                                            ptr8->field_98 = v28;
                                                            v30 = &ptr8->field_98;
                                                            v0 = sub_f7d8d0(v30, v28);
                                                            if (*((long long *)&v30->padding_28[0]))
                                                            {
                                                                v31 = *((long long *)(*((long long *)&v30->padding_28[0]) + 168));
                                                                ptr9 = ptr;
                                                                ptr9->field_68 = v31;
                                                                idx14 = &ptr9->field_68;
                                                                v0 = sub_f7d8d0(idx14, v31);
                                                                if (*((long long *)&idx14->padding_0[8]))
                                                                {
                                                                    v34 = *((long long *)(*((long long *)&idx14->padding_0[8]) + 160));
                                                                    ptr10 = ptr;
                                                                    ptr10->field_60 = v34;
                                                                    v36 = &ptr10->field_60;
                                                                    v0 = sub_f7d8d0(v36, v34);
                                                                    if (v36->field_20)
                                                                    {
                                                                        if (*((char *)&v36->field_20[4].field_28 + 1))
                                                                            return v0;
                                                                        ptr->field_3a = 1;
                                                                        return v0;
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
    sub_f7db74(v0);
}
```

## `MovePlayerAndCamera.Update` — RVA `0xc8c180`

- Decompiled symbol: `MovePlayerAndCamera_Update`
- Metadata signature: `private void Update() { }`
- Native interval: `592` bytes
- Result: `pseudocode`
- Heuristic layout hint: `MovePlayerAndCamera_Recovered` matched 3 offsets against `MovePlayerAndCamera` metadata (confidence 1.00).

```c
typedef struct MovePlayerAndCamera_Recovered {
    char padding_0[32];
    long long CinemaCameraObj;
    long long movePos;
    char padding_30[88];
    struct struct_2 *FPSWalkerComponent;
} MovePlayerAndCamera_Recovered;

typedef struct struct_2 {
    char padding_0[568];
    long long field_238;
} struct_2;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

typedef struct struct_1 {
    char padding_0[224];
    unsigned int field_e0;
} struct_1;

extern struct_0 *g_1eeed00;
extern struct_1 *g_1ef0c58;
extern long long g_1ef22e8;
extern char g_1fab32c;
extern char g_1fab43b;

long long MovePlayerAndCamera_Update(struct_3 *ptr)
{
    long long v0;  // x0
    unsigned int v1;  // s0
    unsigned long v2;  // 4129
    long long v3;  // x0
    long long v4;  // x0
    long long v5;  // x0
    long long v6;  // x0
    unsigned long long v7;  // x0

    if (!(g_1fab43b & 1))
    {
        sub_f7d92c(&g_1eeed00);
        sub_f7d92c(&g_1ef0c58);
        g_1fab43b = 1;
    }
    v0 = Time__get_timeSinceLevelLoad(0);
    v2 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v1, 1045220557)) >> 5 & 3 | (unsigned long long)(CmpF(v1, 1045220557) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v1, 1045220557)) >> 5 & 3 | (unsigned long long)(CmpF(v1, 1045220557) & 1)) & ((unsigned long long)(char)(CmpF(v1, 1045220557)) >> 5 & 3 | (unsigned long long)(CmpF(v1, 1045220557) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if ((char)v2)
        return v0;
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (((char)Object__op_Implicit(ptr->field_28, 0) & 1))
    {
        if (!g_1eeed00->field_e0)
            sub_f7da5c(g_1eeed00);
        if (((char)CF2Input__GetKeyDown(277, 0) & 1))
        {
            v3 = ptr->field_28;
            if (!v3)
                sub_f7db74(v3);
            v3 = Transform__get_position(v3, 0);
            if (!g_1fab32c)
            {
                v3 = sub_f7d92c(&g_1ef22e8);
                g_1fab32c = 1;
            }
            if (!ptr->field_88)
                sub_f7db74(v3);
            v3 = ptr->field_88->field_238;
            if (!v3)
                sub_f7db74(v3);
            CapsuleCollider__get_height(v3, 0);
            MovePlayerAndCamera__MovePlayer();
        }
    }
    if (!g_1eeed00->field_e0)
        sub_f7da5c(g_1eeed00);
    if (((char)CF2Input__GetKeyDown(127, 0) & 1))
    {
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        if (((char)Object__op_Implicit(ptr->field_20, 0) & 1))
            MovePlayerAndCamera__ReleaseMainCamera(ptr);
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v4 = Object__op_Implicit(ptr->field_28, 0);
    if (!((char)v4 & 1))
        return v4;
    if (!g_1eeed00->field_e0)
        sub_f7da5c(g_1eeed00);
    v5 = CF2Input__GetKeyDown(279, 0);
    if (!((char)v5 & 1))
        return v5;
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v6 = Object__op_Implicit(ptr->field_20, 0);
    if (!((char)v6 & 1))
        return v6;
    v7 = MovePlayerAndCamera__ReleaseMainCameraAndMovePlayer(ptr);
    return MovePlayerAndCamera__ReleaseMainCameraAndMovePlayer(ptr);
}
```

## `MovePlayerAndCamera.MovePlayer` — RVA `0xc8c3d0`

- Decompiled symbol: `MovePlayerAndCamera_MovePlayer`
- Metadata signature: `public void MovePlayer(Vector3 position, float camYaw = 0.0, float camPitch = 0.0) { }`
- Native interval: `1088` bytes
- Result: `pseudocode`
- Heuristic layout hint: `MovePlayerAndCamera_Recovered` matched 8 offsets against `MovePlayerAndCamera` metadata (confidence 1.00).

```c
typedef struct struct_5 {
    char padding_0[360];
    unsigned long long field_168;
    unsigned int field_170;
    char padding_174[116];
    unsigned int field_1e8;
} struct_5;

typedef struct MovePlayerAndCamera_Recovered {
    char padding_0[64];
    struct struct_0 *FPSWeaponsObj;
    struct struct_0 *FPSPlayerObj;
    struct struct_0 *FPSCameraObj;
    char padding_58[8];
    struct struct_0 *PlayerCharacterObj;
    struct struct_0 *PlayerCharacterComponent;
    struct struct_4 *CameraControlComponent;
    struct struct_1 *MouseLookComponent;
    char padding_80[8];
    struct struct_2 *FPSWalkerComponent;
} MovePlayerAndCamera_Recovered;

typedef struct struct_1 {
    char padding_0[80];
    unsigned int field_50;
    unsigned int field_54;
    unsigned int field_58;
    unsigned int field_5c;
    unsigned int field_60;
    unsigned int field_64;
    unsigned int field_68;
    unsigned int field_6c;
    unsigned int field_70;
    unsigned int field_74;
    char padding_78[4];
    unsigned int field_7c;
    char padding_80[4];
    unsigned int field_84;
    unsigned int field_88;
    unsigned int field_8c;
    unsigned int field_90;
    unsigned int field_94;
    char padding_98[8];
    unsigned long long field_a0;
} struct_1;

typedef struct struct_2 {
    char padding_0[568];
    struct struct_0 *field_238;
    char padding_240[380];
    unsigned int field_3bc;
} struct_2;

typedef struct struct_0 {
    char padding_0[360];
    unsigned long long field_168;
    unsigned int field_170;
    char padding_174[116];
    unsigned int field_1e8;
} struct_0;

typedef struct struct_4 {
    char padding_0[304];
    unsigned int field_130;
    unsigned int field_134;
    unsigned int field_138;
    unsigned int field_13c;
    char padding_140[12];
    unsigned int field_14c;
    unsigned int field_150;
    unsigned int field_154;
    unsigned int field_158;
    unsigned int field_15c;
    unsigned int field_160;
} struct_4;

typedef struct struct_7 {
    char padding_0[24];
    unsigned int field_18;
    unsigned int field_1c;
    unsigned int field_20;
} struct_7;

typedef struct struct_6 {
    char padding_0[184];
    struct struct_7 *field_b8;
} struct_6;

extern struct_6 *g_1ef22e8;
extern char g_1fab32c;

struct_5 * MovePlayerAndCamera_MovePlayer(struct_3 *ptr)
{
    struct_5 *v2;  // x0
    unsigned long v3;  // d1
    unsigned int v12;  // s13
    unsigned int v13;  // s11
    unsigned int v14;  // s12
    unsigned int ptr4[89];  // x8
    unsigned int ptr5[89];  // x8
    struct_5 *v17;  // x20
    struct_5 *v18;  // x20
    unsigned int v19;  // s0
    struct_5 *ptr8;  // x20
    unsigned int v21;  // s12
    unsigned long v4;  // d0
    struct_5 *v23;  // x20
    unsigned int v24;  // s3
    unsigned int v25;  // 4099
    unsigned long v26;  // 4116
    long long v27;  // x20
    struct_5 *v28;  // x20
    struct_1 *p;  // x20
    unsigned int v30;  // s4
    struct_1 *addr;  // x20
    struct_5 *v5;  // x0
    struct_1 *ptr3;  // x19
    unsigned int ptr6[89];  // x8
    unsigned int v7;  // s0
    unsigned int ptr7[9];  // x10
    unsigned int v9;  // s1
    unsigned int v10;  // s2
    unsigned int v11;  // s2
    int v0;  // [bp-0x80]
    int v1;  // [bp-0x70]

    v2 = ptr->field_48;
    *((unsigned long *)&v1) = v3;
    *((unsigned long *)&v0) = v4;
    if (v2)
    {
        v5 = GameObject__get_activeInHierarchy(v2, 0);
        if (!((char)v5 & 1))
            return v5;
        MovePlayerAndCamera__CancelPlayerActions(ptr);
        v2 = Time__get_time(0);
        if (ptr->field_70)
        {
            ptr->field_70->field_130 = v4;
            v2 = Time__get_time(0);
            if (ptr->field_78)
            {
                ptr->field_78->field_84 = v4;
                if (!g_1fab32c)
                {
                    v2 = sub_f7d92c(&g_1ef22e8);
                    g_1fab32c = 1;
                }
                if (ptr->field_88)
                {
                    ptr6 = ptr->field_70;
                    if (ptr6)
                    {
                        v7 = ptr->field_88->field_3bc;
                        ptr7 = g_1ef22e8->field_b8;
                        v9 = ptr7[6];
                        v10 = ptr7[7];
                        v12 = v11 + ptr7[8] * v7;
                        ptr6[88] = v12;
                        v13 = (unsigned int)v0 + v9 * v7;
                        ptr6[86] = v13;
                        v14 = (unsigned int)v1 + v10 * v7;
                        ptr6[87] = v14;
                        ptr4 = ptr->field_70;
                        if (ptr4)
                        {
                            ptr4[83] = v13;
                            ptr4[84] = v14;
                            ptr4[85] = v12;
                            ptr5 = ptr->field_70;
                            if (ptr5)
                            {
                                ptr5[77] = v13;
                                ptr5[78] = v14;
                                ptr5[79] = v12;
                                v2 = ptr->field_48;
                                if (v2)
                                {
                                    v2 = GameObject__get_transform(v2, 0);
                                    if (v2)
                                    {
                                        Transform__set_position();
                                        v2 = ptr->field_50;
                                        if (v2)
                                        {
                                            v2 = GameObject__get_transform(v2, 0);
                                            if (v2)
                                            {
                                                Transform__set_position();
                                                v2 = ptr->field_40;
                                                if (v2)
                                                {
                                                    v2 = GameObject__get_transform(v2, 0);
                                                    if (ptr->field_50)
                                                    {
                                                        v17 = v2;
                                                        v2 = GameObject__get_transform(ptr->field_50, 0);
                                                        if (v2)
                                                        {
                                                            v2 = Transform__get_position();
                                                            if (v17)
                                                            {
                                                                Transform__set_position(v17, 0);
                                                                v2 = ptr->field_60;
                                                                if (v2)
                                                                {
                                                                    v2 = GameObject__get_transform(v2, 0);
                                                                    v18 = v2;
                                                                    if (!g_1fab32c)
                                                                    {
                                                                        v2 = sub_f7d92c(&g_1ef22e8);
                                                                        g_1fab32c = 1;
                                                                    }
                                                                    if (ptr->field_88)
                                                                    {
                                                                        v2 = ptr->field_88->field_238;
                                                                        if (v2)
                                                                        {
                                                                            v2 = CapsuleCollider__get_height(v2, 0);
                                                                            if (v18)
                                                                            {
                                                                                v19 = *((unsigned int *)&v0) - g_1ef22e8->field_b8->field_18 * v13 * 0x3f000000;
                                                                                v2 = Transform__set_position(v18, 0);
                                                                                ptr8 = ptr->field_68;
                                                                                if (!g_1fab32c)
                                                                                {
                                                                                    v2 = sub_f7d92c(&g_1ef22e8);
                                                                                    g_1fab32c = 1;
                                                                                }
                                                                                if (ptr->field_88)
                                                                                {
                                                                                    v2 = ptr->field_88->field_238;
                                                                                    if (v2)
                                                                                    {
                                                                                        v21 = g_1ef22e8->field_b8->field_20;
                                                                                        v2 = CapsuleCollider__get_height(v2, 0);
                                                                                        if (ptr8)
                                                                                        {
                                                                                            ptr8->field_168 = [D] unsupported_Iop_ZeroHI64ofV128();
                                                                                            ptr8->field_170 = v11 + v21 * v19 * 0xbf000000;
                                                                                            v2 = ptr->field_68;
                                                                                            if (v2)
                                                                                            {
                                                                                                v2 = Component__get_transform(v2, 0);
                                                                                                if (ptr->field_48)
                                                                                                {
                                                                                                    v23 = v2;
                                                                                                    v2 = GameObject__get_transform(ptr->field_48, 0);
                                                                                                    if (v2)
                                                                                                    {
                                                                                                        v2 = Transform__get_rotation();
                                                                                                        if (v23)
                                                                                                        {
                                                                                                            v2 = Transform__set_rotation(v23, 0);
                                                                                                            if (ptr->field_68)
                                                                                                            {
                                                                                                                v25 = CmpF(v24, 0.0);
                                                                                                                v26 = (((CmpF(v24, 0.0) >> 5 & 3 | CmpF(v24, 0.0) & 1) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1;
                                                                                                                ptr->field_68->field_1e8 = *((unsigned int *)&v1);
                                                                                                                if ((char)((v26 - ((CmpF(v24, 0.0) >> 5 & 3 | CmpF(v24, 0.0) & 1) & (v25 >> 5 & 3 | CmpF(v24, 0.0) & 1) >> 1 & 1)) * 0x10000000 >> 30))
                                                                                                                    return v2;
                                                                                                                v2 = ptr->field_50;
                                                                                                                if (v2)
                                                                                                                {
                                                                                                                    v27 = GameObject__get_transform(v2, 0);
                                                                                                                    v2 = Quaternion__Internal_FromEulerRad(0);
                                                                                                                    if (v27)
                                                                                                                    {
                                                                                                                        Transform__set_rotation(v27, 0);
                                                                                                                        v2 = ptr->field_40;
                                                                                                                        if (v2)
                                                                                                                        {
                                                                                                                            v2 = GameObject__get_transform(v2, 0);
                                                                                                                            if (ptr->field_50)
                                                                                                                            {
                                                                                                                                v28 = v2;
                                                                                                                                v2 = GameObject__get_transform(ptr->field_50, 0);
                                                                                                                                if (v2)
                                                                                                                                {
                                                                                                                                    v2 = Transform__get_rotation();
                                                                                                                                    if (v28)
                                                                                                                                    {
                                                                                                                                        v2 = Transform__set_rotation(v28, 0);
                                                                                                                                        p = ptr->field_78;
                                                                                                                                        if (p)
                                                                                                                                        {
                                                                                                                                            p->field_50 = v24;
                                                                                                                                            p->field_54 = v30;
                                                                                                                                            p->field_7c = 0;
                                                                                                                                            p->field_a0 = 0;
                                                                                                                                            Quaternion__Internal_FromEulerRad(0);
                                                                                                                                            p->field_58 = 0;
                                                                                                                                            p->field_5c = 0;
                                                                                                                                            p->field_60 = 0;
                                                                                                                                            p->field_64 = 0xbf000000;
                                                                                                                                            addr = ptr->field_78;
                                                                                                                                            v2 = Quaternion__Internal_FromEulerRad(0);
                                                                                                                                            if (addr)
                                                                                                                                            {
                                                                                                                                                addr->field_68 = 0;
                                                                                                                                                addr->field_6c = 0;
                                                                                                                                                addr->field_70 = 0;
                                                                                                                                                addr->field_74 = 0xbf000000;
                                                                                                                                                ptr3 = ptr->field_78;
                                                                                                                                                v2 = Quaternion__Internal_FromEulerRad(0);
                                                                                                                                                if (ptr3)
                                                                                                                                                {
                                                                                                                                                    ptr3->field_88 = 0;
                                                                                                                                                    ptr3->field_8c = 0;
                                                                                                                                                    ptr3->field_90 = 0;
                                                                                                                                                    ptr3->field_94 = 0xbf000000;
                                                                                                                                                    return v2;
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
    sub_f7db74(v2);
}
```

## `MovePlayerAndCamera.ReleaseMainCamera` — RVA `0xc8c810`

- Decompiled symbol: `MovePlayerAndCamera_ReleaseMainCamera`
- Metadata signature: `public void ReleaseMainCamera() { }`
- Native interval: `612` bytes
- Result: `pseudocode`
- Heuristic layout hint: `MovePlayerAndCamera_Recovered` matched 10 offsets against `MovePlayerAndCamera` metadata (confidence 1.00).

```c
typedef struct MovePlayerAndCamera_Recovered {
    char padding_0[32];
    long long CinemaCameraObj;
    char padding_28[16];
    char toggleState;
    char padding_39[7];
    unsigned long long FPSWeaponsObj;
    unsigned long long FPSPlayerObj;
    long long FPSCameraObj;
    unsigned long long MainCameraObj;
    char padding_60[8];
    struct struct_0 *PlayerCharacterComponent;
    unsigned long long CameraControlComponent;
    unsigned long long MouseLookComponent;
    char padding_80[24];
    unsigned long long IronsightsComponent;
} MovePlayerAndCamera_Recovered;

typedef struct struct_0 {
    char padding_0[184];
    unsigned long long field_b8;
} struct_0;

unsigned long long MovePlayerAndCamera_ReleaseMainCamera(struct_1 *ptr)
{
    unsigned long v0;  // x0
    unsigned long v1;  // x20
    unsigned long v2;  // x20
    unsigned long long v3;  // x0
    unsigned long v5;  // x20
    unsigned long v6;  // x20

    if (ptr->field_38)
    {
        v0 = ptr->field_58;
        if (v0)
        {
            v0 = GameObject__get_transform(v0, 0);
            if (ptr->field_50)
            {
                v1 = v0;
                v0 = GameObject__get_transform(ptr->field_50, 0);
                if (v0)
                {
                    v0 = Transform__get_rotation();
                    if (v1)
                    {
                        Transform__set_rotation(v1, 0);
                        v0 = ptr->field_58;
                        if (v0)
                        {
                            v0 = GameObject__get_transform(v0, 0);
                            if (ptr->field_50)
                            {
                                v2 = v0;
                                v0 = GameObject__get_transform(ptr->field_50, 0);
                                if (v0)
                                {
                                    v0 = Transform__get_position();
                                    if (v2)
                                    {
                                        Transform__set_position(v2, 0);
                                        v0 = ptr->field_70;
                                        if (v0)
                                        {
                                            Behaviour__set_enabled(v0, 1, 0);
                                            v0 = ptr->field_78;
                                            if (v0)
                                            {
                                                Behaviour__set_enabled(v0, 1, 0);
                                                v0 = ptr->field_40;
                                                if (v0)
                                                {
                                                    GameObject__SetActive(v0, 1, 0);
                                                    v0 = ptr->field_48;
                                                    if (v0)
                                                    {
                                                        GameObject__SetActive(v0, 1, 0);
                                                        v0 = MovePlayerAndCamera__TogglePlayerCharacterVisibility(ptr);
                                                        if (ptr->field_68)
                                                        {
                                                            v0 = ptr->field_68->field_b8;
                                                            if (v0)
                                                            {
                                                                GameObject__SetActive(v0, 1, 0);
                                                                MovePlayerAndCamera__CancelPlayerActions(ptr);
                                                                v3 = MovePlayerAndCamera__ToggleGuiDisplay(ptr);
                                                                ptr->field_38 = 0;
                                                                return v3;
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
        MovePlayerAndCamera__ToggleGuiDisplay(ptr);
        v0 = ptr->field_40;
        if (v0)
        {
            GameObject__SetActive(v0, 0, 0);
            v0 = ptr->field_48;
            if (v0)
            {
                GameObject__SetActive(v0, 0, 0);
                v0 = MovePlayerAndCamera__TogglePlayerCharacterVisibility(ptr);
                if (ptr->field_68)
                {
                    v0 = ptr->field_68->field_b8;
                    if (v0)
                    {
                        GameObject__SetActive(v0, 0, 0);
                        v0 = ptr->field_70;
                        if (v0)
                        {
                            Behaviour__set_enabled(v0, 0, 0);
                            v0 = ptr->field_78;
                            if (v0)
                            {
                                Behaviour__set_enabled(v0, 0, 0);
                                v0 = ptr->field_58;
                                if (v0)
                                {
                                    v0 = GameObject__get_transform(v0, 0);
                                    if (ptr->field_20)
                                    {
                                        v5 = v0;
                                        v0 = GameObject__get_transform(ptr->field_20, 0);
                                        if (v0)
                                        {
                                            v0 = Transform__get_position();
                                            if (v5)
                                            {
                                                Transform__set_position(v5, 0);
                                                v0 = ptr->field_58;
                                                if (v0)
                                                {
                                                    v0 = GameObject__get_transform(v0, 0);
                                                    if (ptr->field_20)
                                                    {
                                                        v6 = v0;
                                                        v0 = GameObject__get_transform(ptr->field_20, 0);
                                                        if (v0)
                                                        {
                                                            v0 = Transform__get_rotation();
                                                            if (v6)
                                                            {
                                                                Transform__set_rotation(v6, 0);
                                                                v0 = Camera__get_main(0);
                                                                if (ptr->field_98 && v0)
                                                                {
                                                                    v3 = Camera__set_fieldOfView();
                                                                    ptr->field_38 = 1;
                                                                    return v3;
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
    sub_f7db74(v0);
}
```

## `MovePlayerAndCamera.ReleaseMainCameraAndMovePlayer` — RVA `0xc8ca74`

- Decompiled symbol: `MovePlayerAndCamera_ReleaseMainCameraAndMovePlayer`
- Metadata signature: `public void ReleaseMainCameraAndMovePlayer() { }`
- Native interval: `796` bytes
- Result: `pseudocode`
- Heuristic layout hint: `MovePlayerAndCamera_Recovered` matched 12 offsets against `MovePlayerAndCamera` metadata (confidence 1.00).

```c
typedef struct struct_5 {
    char padding_0[360];
    unsigned long long field_168;
    unsigned int field_170;
    char padding_174[116];
    unsigned int field_1e8;
} struct_5;

typedef struct MovePlayerAndCamera_Recovered {
    char padding_0[32];
    long long CinemaCameraObj;
    unsigned long long movePos;
    char padding_30[8];
    char toggleState;
    char padding_39[7];
    unsigned long long FPSWeaponsObj;
    unsigned long long FPSPlayerObj;
    long long FPSCameraObj;
    unsigned long long MainCameraObj;
    char padding_60[8];
    struct struct_0 *PlayerCharacterComponent;
    unsigned long long CameraControlComponent;
    unsigned long long MouseLookComponent;
    char padding_80[8];
    struct struct_1 *FPSWalkerComponent;
    char padding_90[8];
    unsigned long long IronsightsComponent;
} MovePlayerAndCamera_Recovered;

typedef struct struct_0 {
    char padding_0[184];
    unsigned long long field_b8;
} struct_0;

typedef struct struct_1 {
    char padding_0[568];
    unsigned long long field_238;
} struct_1;

extern long long g_1ef22e8;
extern char g_1fab32c;

struct_5 * MovePlayerAndCamera_ReleaseMainCameraAndMovePlayer(struct_2 *ptr)
{
    unsigned long v0;  // x0
    unsigned long v1;  // x20
    unsigned long v2;  // x20
    struct_5 *v3;  // x0
    unsigned long v5;  // x20
    unsigned long v6;  // x20

    if (ptr->field_38)
    {
        v0 = ptr->field_58;
        if (v0)
        {
            v0 = GameObject__get_transform(v0, 0);
            if (ptr->field_50)
            {
                v1 = v0;
                v0 = GameObject__get_transform(ptr->field_50, 0);
                if (v0)
                {
                    v0 = Transform__get_rotation();
                    if (v1)
                    {
                        Transform__set_rotation(v1, 0);
                        v0 = ptr->field_58;
                        if (v0)
                        {
                            v0 = GameObject__get_transform(v0, 0);
                            if (ptr->field_50)
                            {
                                v2 = v0;
                                v0 = GameObject__get_transform(ptr->field_50, 0);
                                if (v0)
                                {
                                    v0 = Transform__get_position();
                                    if (v2)
                                    {
                                        Transform__set_position(v2, 0);
                                        v0 = ptr->field_70;
                                        if (v0)
                                        {
                                            Behaviour__set_enabled(v0, 1, 0);
                                            v0 = ptr->field_78;
                                            if (v0)
                                            {
                                                Behaviour__set_enabled(v0, 1, 0);
                                                v0 = ptr->field_40;
                                                if (v0)
                                                {
                                                    GameObject__SetActive(v0, 1, 0);
                                                    v0 = ptr->field_48;
                                                    if (v0)
                                                    {
                                                        GameObject__SetActive(v0, 1, 0);
                                                        v0 = MovePlayerAndCamera__TogglePlayerCharacterVisibility(ptr);
                                                        if (ptr->field_68)
                                                        {
                                                            v0 = ptr->field_68->field_b8;
                                                            if (v0)
                                                            {
                                                                GameObject__SetActive(v0, 1, 0);
                                                                MovePlayerAndCamera__CancelPlayerActions();
                                                                MovePlayerAndCamera__ToggleGuiDisplay(ptr);
                                                                v0 = ptr->field_28;
                                                                if (v0)
                                                                {
                                                                    v0 = Transform__get_position(v0, 0);
                                                                    if (!g_1fab32c)
                                                                    {
                                                                        v0 = sub_f7d92c(&g_1ef22e8);
                                                                        g_1fab32c = 1;
                                                                    }
                                                                    if (ptr->field_88)
                                                                    {
                                                                        v0 = ptr->field_88->field_238;
                                                                        if (v0)
                                                                        {
                                                                            CapsuleCollider__get_height(v0, 0);
                                                                            v3 = MovePlayerAndCamera__MovePlayer(ptr);
                                                                            ptr->field_38 = 0;
                                                                            return v3;
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
        MovePlayerAndCamera__ToggleGuiDisplay(ptr);
        v0 = ptr->field_40;
        if (v0)
        {
            GameObject__SetActive(v0, 0, 0);
            v0 = ptr->field_48;
            if (v0)
            {
                GameObject__SetActive(v0, 0, 0);
                v0 = MovePlayerAndCamera__TogglePlayerCharacterVisibility(ptr);
                if (ptr->field_68)
                {
                    v0 = ptr->field_68->field_b8;
                    if (v0)
                    {
                        GameObject__SetActive(v0, 0, 0);
                        v0 = ptr->field_70;
                        if (v0)
                        {
                            Behaviour__set_enabled(v0, 0, 0);
                            v0 = ptr->field_78;
                            if (v0)
                            {
                                Behaviour__set_enabled(v0, 0, 0);
                                v0 = ptr->field_58;
                                if (v0)
                                {
                                    v0 = GameObject__get_transform(v0, 0);
                                    if (ptr->field_20)
                                    {
                                        v5 = v0;
                                        v0 = GameObject__get_transform(ptr->field_20, 0);
                                        if (v0)
                                        {
                                            v0 = Transform__get_position();
                                            if (v5)
                                            {
                                                Transform__set_position(v5, 0);
                                                v0 = ptr->field_58;
                                                if (v0)
                                                {
                                                    v0 = GameObject__get_transform(v0, 0);
                                                    if (ptr->field_20)
                                                    {
                                                        v6 = v0;
                                                        v0 = GameObject__get_transform(ptr->field_20, 0);
                                                        if (v0)
                                                        {
                                                            v0 = Transform__get_rotation();
                                                            if (v6)
                                                            {
                                                                Transform__set_rotation(v6, 0);
                                                                v0 = Camera__get_main(0);
                                                                if (ptr->field_98 && v0)
                                                                {
                                                                    v3 = Camera__set_fieldOfView();
                                                                    ptr->field_38 = 1;
                                                                    return v3;
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
    sub_f7db74(v0);
}
```

## `MovePlayerAndCamera.CancelPlayerActions` — RVA `0xc8cd90`

- Decompiled symbol: `MovePlayerAndCamera_CancelPlayerActions`
- Metadata signature: `private void CancelPlayerActions() { }`
- Native interval: `408` bytes
- Result: `pseudocode`
- Heuristic layout hint: `MovePlayerAndCamera_Recovered` matched 5 offsets against `MovePlayerAndCamera` metadata (confidence 1.00).

```c
typedef struct MovePlayerAndCamera_Recovered {
    char padding_0[104];
    struct struct_1 *PlayerCharacterComponent;
    char padding_70[16];
    struct struct_2 *FPSPlayerComponent;
    struct struct_3 *FPSWalkerComponent;
    struct struct_1 *PlayerWeaponsComponent;
    struct struct_4 *IronsightsComponent;
} MovePlayerAndCamera_Recovered;

typedef struct struct_10 {
    char padding_0[152];
    struct struct_9 *field_98;
    char padding_a0[52];
    unsigned int field_d4;
    char padding_d8[90];
    char field_132;
    char padding_133[1];
    unsigned int field_134;
    char padding_138[68];
    char field_17c;
    char field_17d;
    char field_17e;
    char padding_17f[129];
    unsigned int field_200;
    char padding_204[192];
    unsigned int field_2c4;
    char padding_2c8[28];
    unsigned int field_2e4;
} struct_10;

typedef struct struct_8 {
    char padding_0[289];
    char field_121;
    char padding_122[111];
    unsigned short field_191;
    char padding_193[53];
    unsigned int field_1c8;
    unsigned int field_1cc;
    char padding_1d0[4];
    unsigned short field_1d4;
    char padding_1d6[438];
    unsigned long long field_38c;
    unsigned int field_394;
} struct_8;

typedef struct struct_3 {
    char padding_0[672];
    char field_2a0;
    char padding_2a1[7];
    char field_2a8;
    char padding_2a9[8];
    char field_2b1;
    char padding_2b2[16];
    char field_2c2;
    char padding_2c3[13];
    unsigned short field_2d0;
    char field_2d2;
    char padding_2d3[9];
    unsigned short field_2dc;
    char field_2de;
    char padding_2df[33];
    char field_300;
} struct_3;

typedef struct struct_4 {
    char padding_0[168];
    unsigned long long field_a8;
    char padding_b0[64];
    unsigned int field_f0;
    char padding_f4[8];
    unsigned int field_fc;
    unsigned int field_100;
    char padding_104[37];
    char field_129;
    char padding_12a[270];
    unsigned int field_238;
} struct_4;

typedef struct struct_2 {
    char padding_0[720];
    char field_2d0;
} struct_2;

typedef struct struct_1 {
    char padding_0[152];
    struct struct_0 *field_98;
    char padding_a0[52];
    unsigned int field_d4;
    char padding_d8[90];
    char field_132;
    char padding_133[1];
    unsigned int field_134;
    char padding_138[68];
    char field_17c;
    char field_17d;
    char field_17e;
    char padding_17f[129];
    unsigned int field_200;
    char padding_204[192];
    unsigned int field_2c4;
    char padding_2c8[28];
    unsigned int field_2e4;
} struct_1;

typedef struct struct_9 {
    char padding_0[289];
    char field_121;
    char padding_122[111];
    unsigned short field_191;
    char padding_193[53];
    unsigned int field_1c8;
    unsigned int field_1cc;
    char padding_1d0[4];
    unsigned short field_1d4;
    char padding_1d6[438];
    unsigned long long field_38c;
    unsigned int field_394;
} struct_9;

typedef struct struct_0 {
    char padding_0[289];
    char field_121;
    char padding_122[111];
    unsigned short field_191;
    char padding_193[53];
    unsigned int field_1c8;
    unsigned int field_1cc;
    char padding_1d0[4];
    unsigned short field_1d4;
    char padding_1d6[438];
    unsigned long long field_38c;
    unsigned int field_394;
} struct_0;

typedef struct struct_6 {
    unsigned long long field_0;
    unsigned int field_8;
} struct_6;

typedef struct struct_7 {
    char padding_0[184];
    struct struct_6 *field_b8;
} struct_7;

extern struct_7 *g_1ef22e8;
extern char g_1fab2c9;

void MovePlayerAndCamera_CancelPlayerActions(struct_5 *ptr)
{
    unsigned long long v5;  // x30
    unsigned long long v6;  // x22
    struct_10 *addr;  // x21
    char v16;  // x8
    struct_4 *ptr3;  // x8
    unsigned int v18;  // s0
    struct_3 *ptr4;  // x8
    struct_1 *ptr6;  // x8
    unsigned long long v7;  // x21
    unsigned long long v8;  // x20
    unsigned long long v9;  // x19
    struct_10 *ptr8;  // x0
    struct_8 *ptr5;  // x20
    struct_3 *p;  // x8
    unsigned int v13;  // s1
    unsigned long ptr7;  // x8
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
    ptr8 = ptr->field_90;
    if (ptr8)
    {
        ptr5 = ptr8->field_98;
        ptr8 = MonoBehaviour__StopAllCoroutines(ptr8, 0);
        if (ptr5)
        {
            ptr8 = MonoBehaviour__StopAllCoroutines(ptr5, 0);
            p = ptr->field_88;
            if (p)
            {
                p->field_2a0 = 0;
                p->field_300 = 0;
                p->field_2d2 = 0;
                p->field_2de = 0;
                p->field_2a8 = 1;
                p->field_2d0 = 0x100;
                p->field_2dc = 0x100;
                if (!g_1fab2c9)
                {
                    ptr8 = sub_f7d92c(&g_1ef22e8);
                    g_1fab2c9 = 1;
                }
                v13 = g_1ef22e8->field_b8->field_8;
                ptr7 = &ptr5->padding_1d6[434];
                *((unsigned long long *)ptr7) = g_1ef22e8->field_b8->field_0;
                *((unsigned int *)(ptr7 + 8)) = v13;
                addr = ptr->field_90;
                if (addr)
                {
                    if (*((int *)&addr->padding_d8[4]) != addr->field_d4 || ptr5->field_121)
                        v16 = 0;
                    else
                        v16 = 1;
                    addr->field_17d = v16;
                    addr->field_17e = 0;
                    addr->field_17c = 0;
                    *((unsigned short *)&ptr5->padding_1d0[0]) = 0;
                    *((unsigned short *)&(&ptr5->padding_122)[1]) = 0;
                    *((unsigned int *)&ptr5->padding_193[52]) = 0;
                    ptr3 = ptr->field_98;
                    if (ptr3)
                    {
                        ptr3->field_238 = 0;
                        ptr3->field_129 = 0;
                        if (ptr->field_80)
                        {
                            ptr->field_80->field_2d0 = 0;
                            v18 = ptr3->field_f0;
                            ptr3->field_fc = v18;
                            ptr3->field_100 = v18;
                            ptr4 = ptr->field_88;
                            if (ptr4)
                            {
                                ptr4->field_2b1 = 0;
                                ptr4->field_2a0 = 0;
                                ptr4->field_300 = 0;
                                ptr4->field_2c2 = 1;
                                ptr4->field_2a8 = 1;
                                addr->field_132 = 1;
                                ptr8 = Time__get_time(0);
                                addr->field_134 = v18;
                                ptr6 = ptr->field_68;
                                if (ptr6)
                                {
                                    ptr6->field_2e4 = 4294967295;
                                    ptr6->field_200 = 0xc1800000;
                                    ptr6->field_2c4 = 0xc1800000;
                                    ptr8 = WeaponBehavior__CancelWeaponPull(ptr5, 0, 0);
                                    if (ptr->field_98)
                                    {
                                        ptr->field_98->field_a8 = 0;
                                        ptr5->field_1c8 = 0;
                                        ptr8 = ptr->field_68;
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    sub_f7db74(ptr8);
}
```

## `MovePlayerAndCamera.ToggleGuiDisplay` — RVA `0xc8cf28`

- Decompiled symbol: `MovePlayerAndCamera_ToggleGuiDisplay`
- Metadata signature: `public void ToggleGuiDisplay() { }`
- Native interval: `80` bytes
- Result: `pseudocode`
- Heuristic layout hint: `MovePlayerAndCamera_Recovered` matched 3 offsets against `MovePlayerAndCamera` metadata (confidence 1.00).

```c
typedef struct MovePlayerAndCamera_Recovered {
    char padding_0[57];
    char toggleGuiState;
    char noCrosshair;
    char padding_3b[69];
    struct struct_0 *FPSPlayerComponent;
} MovePlayerAndCamera_Recovered;

typedef struct struct_2 {
    char padding_0[376];
    unsigned long long field_178;
} struct_2;

typedef struct struct_0 {
    char padding_0[376];
    long long field_178;
} struct_0;

struct_1 * MovePlayerAndCamera_ToggleGuiDisplay(struct_1 *ptr)
{
    struct_1 *v0;  // x0
    char v3;  // x8
    struct_1 *v4;  // x0

    if (ptr->field_39)
    {
        v0 = ptr;
        if (!v0->field_3a)
        {
            if (ptr->field_80 && ptr->field_80->field_178)
                v0 = Behaviour__set_enabled(ptr->field_80->field_178, 1, 0);
            else
                sub_f7db74();
        }
        v3 = 0;
        v4 = v0;
    }
    else
    {
        v3 = 1;
        v4 = ptr;
    }
    ptr->field_39 = v3;
    return v4;
}
```

## `MovePlayerAndCamera.ToggleCinemaCamera` — RVA `0xc8cf78`

- Decompiled symbol: `MovePlayerAndCamera_ToggleCinemaCamera`
- Metadata signature: `public void ToggleCinemaCamera() { }`
- Native interval: `348` bytes
- Result: `pseudocode`
- Heuristic layout hint: `MovePlayerAndCamera_Recovered` matched 8 offsets against `MovePlayerAndCamera` metadata (confidence 1.00).

```c
typedef struct MovePlayerAndCamera_Recovered {
    char padding_0[32];
    unsigned long long CinemaCameraObj;
    char padding_28[16];
    char toggleState;
    char padding_39[7];
    unsigned long long FPSWeaponsObj;
    unsigned long long FPSPlayerObj;
    unsigned long long FPSCameraObj;
    char padding_58[16];
    struct struct_0 *PlayerCharacterComponent;
    struct struct_1 *CameraControlComponent;
    struct struct_2 *MouseLookComponent;
} MovePlayerAndCamera_Recovered;

typedef struct struct_1 {
    char padding_0[304];
    unsigned int field_130;
} struct_1;

typedef struct struct_2 {
    char padding_0[132];
    unsigned int field_84;
} struct_2;

typedef struct struct_0 {
    char padding_0[184];
    unsigned long long field_b8;
} struct_0;

long long MovePlayerAndCamera_ToggleCinemaCamera(struct_3 *ptr)
{
    unsigned long long v0;  // x0
    unsigned int v1;  // s0
    unsigned long v2;  // x0

    if (ptr->field_38)
    {
        v0 = ptr->field_20;
        if (v0)
        {
            GameObject__SetActive(v0, 0, 0);
            v0 = Time__get_time(0);
            if (ptr->field_70)
            {
                ptr->field_70->field_130 = v1;
                v0 = Time__get_time(0);
                if (ptr->field_78)
                {
                    ptr->field_78->field_84 = v1;
                    v0 = ptr->field_50;
                    if (v0)
                    {
                        GameObject__SetActive(v0, 1, 0);
                        v0 = ptr->field_40;
                        if (v0)
                        {
                            GameObject__SetActive(v0, 1, 0);
                            v0 = ptr->field_48;
                            if (v0)
                            {
                                GameObject__SetActive(v0, 1, 0);
                                v0 = MovePlayerAndCamera__TogglePlayerCharacterVisibility();
                                if (ptr->field_68)
                                {
                                    v0 = ptr->field_68->field_b8;
                                    if (v0)
                                    {
                                        GameObject__SetActive(v0, 1, 0);
                                        MovePlayerAndCamera__CancelPlayerActions(ptr);
                                        v2 = MovePlayerAndCamera__ToggleGuiDisplay(ptr);
                                        ptr->field_38 = 0;
                                        return v2;
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
        MovePlayerAndCamera__ToggleGuiDisplay(ptr);
        v0 = ptr->field_40;
        if (v0)
        {
            GameObject__SetActive(v0, 0, 0);
            v0 = ptr->field_48;
            if (v0)
            {
                GameObject__SetActive(v0, 0, 0);
                v0 = ptr->field_50;
                if (v0)
                {
                    GameObject__SetActive(v0, 0, 0);
                    v0 = MovePlayerAndCamera__TogglePlayerCharacterVisibility();
                    if (ptr->field_68)
                    {
                        v0 = ptr->field_68->field_b8;
                        if (v0)
                        {
                            GameObject__SetActive(v0, 0, 0);
                            v0 = ptr->field_20;
                            if (v0)
                            {
                                v2 = GameObject__SetActive(v0, 1, 0);
                                ptr->field_38 = 1;
                                return v2;
                            }
                        }
                    }
                }
            }
        }
    }
    sub_f7db74(v0);
}
```

## `MovePlayerAndCamera.TogglePlayerCharacterVisibility` — RVA `0xc8d0d4`

- Decompiled symbol: `MovePlayerAndCamera_TogglePlayerCharacterVisibility`
- Metadata signature: `private void TogglePlayerCharacterVisibility() { }`
- Native interval: `388` bytes
- Result: `pseudocode`
- Heuristic layout hint: `MovePlayerAndCamera_Recovered` matched 2 offsets against `MovePlayerAndCamera` metadata (confidence 1.00).

```c
typedef struct MovePlayerAndCamera_Recovered {
    char padding_0[104];
    struct struct_2 *PlayerCharacterComponent;
    char padding_70[48];
    char playerModelToggleState;
} MovePlayerAndCamera_Recovered;

typedef struct struct_10 {
    char padding_0[168];
    struct struct_11 *field_a8;
    struct struct_12 *field_b0;
} struct_10;

typedef struct struct_9 {
    char padding_0[24];
    unsigned int field_18;
} struct_9;

typedef struct struct_4 {
    char padding_0[32];
    long long field_20;
} struct_4;

typedef struct struct_8 {
    char padding_0[24];
    unsigned int field_18;
} struct_8;

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

typedef struct struct_2 {
    char padding_0[168];
    struct struct_0 *field_a8;
    struct struct_1 *field_b0;
} struct_2;

typedef struct struct_11 {
    char padding_0[24];
    unsigned int field_18;
} struct_11;

typedef struct struct_12 {
    char padding_0[24];
    unsigned int field_18;
} struct_12;

typedef struct struct_0 {
    char padding_0[24];
    int field_18;
} struct_0;

typedef struct struct_1 {
    char padding_0[24];
    int field_18;
} struct_1;

void MovePlayerAndCamera_TogglePlayerCharacterVisibility(struct_3 *ptr3)
{
    struct_9 *ptr;  // x20
    unsigned int v1;  // w8
    unsigned int j;  // w21
    struct_5 *v11;  // x8
    unsigned int v13;  // w8
    struct_3 *v14;  // x0
    unsigned int k;  // w21
    struct_3 *v16;  // x0
    struct_6 *v17;  // x8
    struct_3 *v18;  // x0
    struct_8 *p;  // x20
    struct_3 *v2;  // x0
    unsigned int v20;  // w8
    unsigned int l;  // w21
    struct_7 *v22;  // x8
    unsigned int i;  // w21
    struct_3 *v4;  // x0
    struct_3 *ptr4;  // x0
    struct_4 *v6;  // x8
    struct_3 *v7;  // x0
    struct_8 *addr;  // x20
    unsigned int v9;  // w8

    if (ptr3->field_68)
    {
        ptr = ptr3->field_68->field_b0;
        if (ptr3->field_a0)
        {
            if (ptr)
            {
                v1 = ptr->field_18;
                v2 = ptr3;
                if (ptr->field_18 >= 1)
                {
                    i = 0;
                    v4 = ptr3;
                    do
                    {
                        if (v1 <= i)
                            sub_f7db7c(v4);
                        v6 = &ptr->padding_0[8 * i];
                        if (!v6->field_20)
                            sub_f7db7c(sub_f7db74());
                        if (!Component__get_gameObject(v6->field_20, 0))
                            sub_f7db7c(sub_f7db74());
                        v7 = GameObject__SetActive();
                        v1 = ptr->field_18;
                        i += 1;
                        v4 = v7;
                        v2 = v7;
                    } while (i < ptr->field_18);
                }
                if (ptr3->field_68)
                {
                    addr = ptr3->field_68->field_a8;
                    if (addr)
                    {
                        v9 = addr->field_18;
                        if (addr->field_18 >= 1)
                        {
                            j = 0;
                            do
                            {
                                if (v9 <= j)
                                    sub_f7db7c(ptr4);
                                v11 = &addr->padding_0[8 * j];
                                if (!v11->field_20)
                                    sub_f7db7c(sub_f7db74());
                                ptr4 = Renderer__set_enabled(v11->field_20, 1, 0);
                                v9 = addr->field_18;
                                j += 1;
                            } while (j < addr->field_18);
                        }
                        ptr3->field_a0 = 0;
                        return;
                    }
                }
            }
        }
        else
        {
            if (ptr)
            {
                v13 = ptr->field_18;
                v14 = ptr3;
                if (ptr->field_18 >= 1)
                {
                    k = 0;
                    v16 = ptr3;
                    do
                    {
                        if (v13 <= k)
                            sub_f7db7c(v16);
                        v17 = &ptr->padding_0[8 * k];
                        if (!v17->field_20)
                            sub_f7db7c(sub_f7db74());
                        if (!Component__get_gameObject(v17->field_20, 0))
                            sub_f7db7c(sub_f7db74());
                        v18 = GameObject__SetActive();
                        v13 = ptr->field_18;
                        k += 1;
                        v16 = v18;
                        v14 = v18;
                    } while (k < ptr->field_18);
                }
                if (ptr3->field_68)
                {
                    p = ptr3->field_68->field_a8;
                    if (p)
                    {
                        v20 = p->field_18;
                        if (p->field_18 >= 1)
                        {
                            l = 0;
                            do
                            {
                                if (v20 <= l)
                                    sub_f7db7c(ptr4);
                                v22 = &p->padding_0[8 * l];
                                if (!v22->field_20)
                                    sub_f7db7c(sub_f7db74());
                                ptr4 = Renderer__set_enabled(v22->field_20, 0, 0);
                                v20 = p->field_18;
                                l += 1;
                            } while (l < p->field_18);
                        }
                        ptr3->field_a0 = 1;
                        return;
                    }
                }
            }
        }
    }
    sub_f7db7c(sub_f7db74());
}
```

## `MovePlayerAndCamera.ctor` — RVA `0xc8d258`

- Decompiled symbol: `MovePlayerAndCamera_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long MovePlayerAndCamera_ctor(void)
{
    long long v0;  // x0

    v0 = MonoBehaviour__ctor();
    return MonoBehaviour__ctor();
}
```
