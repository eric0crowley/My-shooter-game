# Native pseudocode: LB_LightingTrigger_Profile

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `LB_LightingTrigger_Profile.Start` — RVA `0xc7bc00`

- Decompiled symbol: `LB_LightingTrigger_Profile_Start`
- Metadata signature: `private void Start() { }`
- Native interval: `224` bytes
- Result: `pseudocode`
- Heuristic layout hint: `LB_LightingTrigger_Profile_Recovered` matched 3 offsets against `LB_LightingTrigger_Profile` metadata (confidence 1.00).

```c
typedef struct LB_LightingTrigger_Profile_Recovered {
    char padding_0[32];
    struct struct_0 *current;
    struct struct_1 *temp;
    char padding_30[8];
    long long cameraTag;
} LB_LightingTrigger_Profile_Recovered;

typedef struct struct_3 {
    char padding_0[56];
    uint128_t field_38;
    uint128_t field_48;
} struct_3;

typedef struct struct_0 {
    char padding_0[56];
    uint128_t field_38;
    uint128_t field_48;
} struct_0;

typedef struct struct_1 {
    char padding_0[56];
    unsigned int field_38[4];
    char field_44;
    char padding_45[3];
    uint128_t field_48;
} struct_1;

extern long long g_1efec60;
extern char g_1fab3e6;

long long LB_LightingTrigger_Profile_Start(struct_2 *ptr)
{
    struct_3 *v0;  // x0
    struct_2 *ptr3;  // x20
    void* p;  // x21
    struct_2 *ptr4;  // x19
    unsigned long v4;  // x0
    struct_0 *index;  // x8
    struct_1 *addr;  // x9

    if (!(g_1fab3e6 & 1))
    {
        sub_f7d92c(&g_1efec60);
        sub_f7d92c("oG");
        g_1fab3e6 = 1;
    }
    if (GameObject__FindGameObjectWithTag(ptr->field_38, 0))
    {
        v0 = sub_1249224();
        ptr->field_20 = v0;
        ptr3 = &ptr->field_20;
        sub_f7d8d0(ptr3, v0);
        p = sub_f7db70(g_1ef0968);
        *((unsigned long *)&p[56]) = 4580701253525936538;
        *((unsigned int *)&p[68]) = 1053609165;
        MonoBehaviour__ctor(p, 0);
        ptr->field_28 = p;
        ptr4 = &ptr->field_28;
        v4 = sub_f7d8d0(ptr4, p);
        index = *((long long *)&ptr3->padding_0[0]);
        if (index)
        {
            addr = *((long long *)&ptr4->padding_0[0]);
            if (addr)
            {
                *((int128_t *)&addr->field_38[0]) = *((int128_t *)&(&index->padding_0)[1]);
                *((int128_t *)&addr->field_44) = *((int128_t *)((char *)&index->field_38 + 8));
                return v4;
            }
        }
    }
    sub_f7db74();
}
```

## `LB_LightingTrigger_Profile.Update` — RVA `0xc7bd00`

- Decompiled symbol: `LB_LightingTrigger_Profile_Update`
- Metadata signature: `private void Update() { }`
- Native interval: `1204` bytes
- Result: `pseudocode`
- Heuristic layout hint: `LB_LightingTrigger_Profile_Recovered` matched 6 offsets against `LB_LightingTrigger_Profile` metadata (confidence 1.00).

```c
typedef struct LB_LightingTrigger_Profile_Recovered {
    char padding_0[32];
    struct struct_1 *current;
    struct struct_2 *temp;
    struct struct_3 *targetProfile;
    char padding_38[8];
    unsigned int blendSpeed;
    char padding_44[4];
    char isChanging;
    char isUpdating;
} LB_LightingTrigger_Profile_Recovered;

typedef struct struct_1 {
    char padding_0[56];
    unsigned int field_38;
    unsigned int field_3c;
    unsigned int field_40;
    unsigned int field_44;
    unsigned int field_48;
    unsigned int field_4c;
    unsigned int field_50;
    unsigned int field_54;
} struct_1;

typedef struct struct_2 {
    char padding_0[56];
    unsigned int field_38;
    unsigned int field_3c;
    unsigned int field_40;
    unsigned int field_44;
    unsigned int field_48;
    unsigned int field_4c;
    unsigned int field_50;
    unsigned int field_54;
} struct_2;

typedef struct struct_3 {
    char padding_0[56];
    unsigned int field_38;
    unsigned int field_3c;
    unsigned int field_40;
    unsigned int field_44;
    unsigned int field_48;
    unsigned int field_4c;
    unsigned int field_50;
    unsigned int field_54;
} struct_3;

int LB_LightingTrigger_Profile_Update(struct_0 *ptr, unsigned long a1)
{
    struct_0 *v0;  // x0
    unsigned int p[22];  // x20
    unsigned int addr[22];  // x20
    unsigned int v11;  // s0
    unsigned int v12;  // s1
    unsigned long v13;  // 4150
    unsigned int v14;  // s0
    unsigned int v15;  // s0
    unsigned int ptr3[22];  // x20
    unsigned int v17;  // s0
    unsigned int v18;  // s1
    unsigned long v19;  // 4150
    unsigned int v2;  // s8
    unsigned int v20;  // s0
    unsigned int v21;  // s0
    unsigned int ptr4[22];  // x20
    unsigned int v23;  // s0
    unsigned int v24;  // s1
    unsigned long v25;  // 4150
    unsigned int v26;  // s0
    unsigned int v27;  // s0
    unsigned int ptr5[22];  // x20
    unsigned int v29;  // s0
    unsigned int v30;  // s1
    unsigned long v31;  // 4150
    unsigned int v32;  // s0
    unsigned int v33;  // s0
    unsigned int ptr6[22];  // x20
    unsigned int v35;  // s0
    unsigned int v36;  // s1
    unsigned long v37;  // 4150
    unsigned int v38;  // s0
    unsigned int v39;  // s0
    unsigned int v4;  // s0
    unsigned int ptr7[22];  // x20
    unsigned int v41;  // s0
    unsigned int v42;  // s1
    unsigned long v43;  // 4150
    unsigned int v44;  // s0
    unsigned int v45;  // s0
    unsigned int ptr15[22];  // x20
    unsigned int v47;  // s8
    unsigned long ptr14;  // x20
    unsigned int idx14[22];  // x8
    unsigned int v5;  // s0
    unsigned int v51;  // s0
    unsigned int v52;  // s1
    unsigned long v53;  // 4150
    unsigned int v54;  // s0
    unsigned int v55;  // s0
    unsigned int ptr8[22];  // x20
    unsigned int v57;  // s0
    unsigned int v58;  // s1
    unsigned int v6;  // s1
    unsigned long v59;  // 4150
    unsigned int v60;  // s0
    unsigned int v61;  // s0
    unsigned int ptr9[22];  // x20
    unsigned int v63;  // s0
    unsigned int v64;  // s1
    unsigned long v65;  // 4150
    unsigned int v66;  // s0
    unsigned int v67;  // s0
    unsigned int ptr10[22];  // x20
    unsigned long v7;  // 4150
    unsigned int v69;  // s0
    unsigned int v70;  // s1
    unsigned long v71;  // 4150
    unsigned int v72;  // s0
    unsigned int v73;  // s0
    unsigned int ptr11[22];  // x20
    unsigned int v75;  // s0
    unsigned int v76;  // s1
    unsigned long v77;  // 4150
    unsigned int v78;  // s0
    unsigned int v8;  // s0
    unsigned int v79;  // s0
    unsigned int ptr12[22];  // x20
    unsigned int v81;  // s0
    unsigned int v82;  // s1
    unsigned long v83;  // 4150
    unsigned int v84;  // s0
    unsigned int v85;  // s0
    unsigned int ptr13[22];  // x20
    unsigned int v87;  // s0
    unsigned int v88;  // s1
    unsigned int v9;  // s0
    unsigned long v89;  // 4150
    unsigned int v90;  // s0
    unsigned int ptr16[22];  // x20
    struct_0 *v92;  // x0
    unsigned int v93;  // s0
    unsigned int v94;  // s1
    unsigned long v95;  // 4150
    unsigned int v96;  // s0

    v0 = ptr;
    if (!v0->field_49)
        return *((unsigned int *)&v0);
    p = ptr->field_20;
    if (p)
    {
        v2 = p[14];
        if (ptr->field_48)
        {
            if (ptr->field_30)
            {
                Time__get_deltaTime(0);
                v5 = v4 * ptr->field_40;
                v6 = [D] unsupported_Iop_ZeroHI96ofV128();
                v7 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v5, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v5, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v5, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v5, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v5, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v5, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                if ((char)v7)
                    v8 = v6;
                else
                    v8 = 0;
                v9 = v2 + (ptr->field_30->field_38 - v2) * v8;
                p[14] = v9;
                addr = ptr->field_20;
                if (addr && ptr->field_30)
                {
                    Time__get_deltaTime(0);
                    v11 = v9 * ptr->field_40;
                    v12 = [D] unsupported_Iop_ZeroHI96ofV128();
                    v13 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v11, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v11, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v11, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v11, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v11, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v11, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                    if ((char)v13)
                        v14 = v12;
                    else
                        v14 = 0;
                    v15 = addr[15] + (ptr->field_30->field_3c - addr[15]) * v14;
                    addr[15] = v15;
                    ptr3 = ptr->field_20;
                    if (ptr3 && ptr->field_30)
                    {
                        Time__get_deltaTime(0);
                        v17 = v15 * ptr->field_40;
                        v18 = [D] unsupported_Iop_ZeroHI96ofV128();
                        v19 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v17, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v17, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v17, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v17, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v17, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v17, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                        if ((char)v19)
                            v20 = v18;
                        else
                            v20 = 0;
                        v21 = ptr3[17] + (ptr->field_30->field_44 - ptr3[17]) * v20;
                        ptr3[17] = v21;
                        ptr4 = ptr->field_20;
                        if (ptr4 && ptr->field_30)
                        {
                            Time__get_deltaTime(0);
                            v23 = v21 * ptr->field_40;
                            v24 = [D] unsupported_Iop_ZeroHI96ofV128();
                            v25 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v23, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v23, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v23, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v23, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v23, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v23, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                            if ((char)v25)
                                v26 = v24;
                            else
                                v26 = 0;
                            v27 = ptr4[16] + (ptr->field_30->field_40 - ptr4[16]) * v26;
                            ptr4[16] = v27;
                            ptr5 = ptr->field_20;
                            if (ptr5 && ptr->field_30)
                            {
                                Time__get_deltaTime(0);
                                v29 = v27 * ptr->field_40;
                                v30 = [D] unsupported_Iop_ZeroHI96ofV128();
                                v31 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v29, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v29, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v29, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v29, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v29, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v29, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                                if ((char)v31)
                                    v32 = v30;
                                else
                                    v32 = 0;
                                v33 = ptr5[18] + (ptr->field_30->field_48 - ptr5[18]) * v32;
                                ptr5[18] = v33;
                                ptr6 = ptr->field_20;
                                if (ptr6 && ptr->field_30)
                                {
                                    Time__get_deltaTime(0);
                                    v35 = v33 * ptr->field_40;
                                    v36 = [D] unsupported_Iop_ZeroHI96ofV128();
                                    v37 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v35, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v35, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v35, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v35, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v35, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v35, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                                    if ((char)v37)
                                        v38 = v36;
                                    else
                                        v38 = 0;
                                    v39 = ptr6[19] + (ptr->field_30->field_4c - ptr6[19]) * v38;
                                    ptr6[19] = v39;
                                    ptr7 = ptr->field_20;
                                    if (ptr7 && ptr->field_30)
                                    {
                                        Time__get_deltaTime(0);
                                        v41 = v39 * ptr->field_40;
                                        v42 = [D] unsupported_Iop_ZeroHI96ofV128();
                                        v43 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v41, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v41, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v41, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v41, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v41, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v41, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                                        if ((char)v43)
                                            v44 = v42;
                                        else
                                            v44 = 0;
                                        v45 = ptr7[20] + (ptr->field_30->field_50 - ptr7[20]) * v44;
                                        ptr7[20] = v45;
                                        ptr15 = ptr->field_20;
                                        if (ptr15 && (v47 = ptr15[21], ptr14 = (unsigned long)(ptr15 + 84), idx14 = (unsigned int [22])ptr->field_30, idx14))
                                            goto LABEL_107c168;
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
            if (ptr->field_28)
            {
                Time__get_deltaTime(0);
                v51 = v4 * ptr->field_40;
                v52 = [D] unsupported_Iop_ZeroHI96ofV128();
                v53 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v51, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v51, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v51, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v51, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v51, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v51, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                if ((char)v53)
                    v54 = v52;
                else
                    v54 = 0;
                v55 = v2 + (ptr->field_28->field_38 - v2) * v54;
                p[14] = v55;
                ptr8 = ptr->field_20;
                if (ptr8 && ptr->field_28)
                {
                    Time__get_deltaTime(0);
                    v57 = v55 * ptr->field_40;
                    v58 = [D] unsupported_Iop_ZeroHI96ofV128();
                    v59 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v57, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v57, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v57, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v57, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v57, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v57, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                    if ((char)v59)
                        v60 = v58;
                    else
                        v60 = 0;
                    v61 = ptr8[15] + (ptr->field_28->field_3c - ptr8[15]) * v60;
                    ptr8[15] = v61;
                    ptr9 = ptr->field_20;
                    if (ptr9 && ptr->field_28)
                    {
                        Time__get_deltaTime(0);
                        v63 = v61 * ptr->field_40;
                        v64 = [D] unsupported_Iop_ZeroHI96ofV128();
                        v65 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v63, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v63, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v63, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v63, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v63, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v63, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                        if ((char)v65)
                            v66 = v64;
                        else
                            v66 = 0;
                        v67 = ptr9[17] + (ptr->field_28->field_44 - ptr9[17]) * v66;
                        ptr9[17] = v67;
                        ptr10 = ptr->field_20;
                        if (ptr10 && ptr->field_28)
                        {
                            Time__get_deltaTime(0);
                            v69 = v67 * ptr->field_40;
                            v70 = [D] unsupported_Iop_ZeroHI96ofV128();
                            v71 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v69, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v69, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v69, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v69, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v69, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v69, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                            if ((char)v71)
                                v72 = v70;
                            else
                                v72 = 0;
                            v73 = ptr10[16] + (ptr->field_28->field_40 - ptr10[16]) * v72;
                            ptr10[16] = v73;
                            ptr11 = ptr->field_20;
                            if (ptr11 && ptr->field_28)
                            {
                                Time__get_deltaTime(0);
                                v75 = v73 * ptr->field_40;
                                v76 = [D] unsupported_Iop_ZeroHI96ofV128();
                                v77 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v75, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v75, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v75, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v75, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v75, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v75, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                                if ((char)v77)
                                    v78 = v76;
                                else
                                    v78 = 0;
                                v79 = ptr11[18] + (ptr->field_28->field_48 - ptr11[18]) * v78;
                                ptr11[18] = v79;
                                ptr12 = ptr->field_20;
                                if (ptr12 && ptr->field_28)
                                {
                                    Time__get_deltaTime(0);
                                    v81 = v79 * ptr->field_40;
                                    v82 = [D] unsupported_Iop_ZeroHI96ofV128();
                                    v83 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v81, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v81, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v81, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v81, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v81, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v81, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                                    if ((char)v83)
                                        v84 = v82;
                                    else
                                        v84 = 0;
                                    v85 = ptr12[19] + (ptr->field_28->field_4c - ptr12[19]) * v84;
                                    ptr12[19] = v85;
                                    ptr13 = ptr->field_20;
                                    if (ptr13 && ptr->field_28)
                                    {
                                        Time__get_deltaTime(0);
                                        v87 = v85 * ptr->field_40;
                                        v88 = [D] unsupported_Iop_ZeroHI96ofV128();
                                        v89 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v87, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v87, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v87, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v87, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v87, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v87, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                                        if ((char)v89)
                                            v90 = v88;
                                        else
                                            v90 = 0;
                                        v45 = ptr13[20] + (ptr->field_28->field_50 - ptr13[20]) * v90;
                                        ptr13[20] = v45;
                                        ptr16 = ptr->field_20;
                                        if (ptr16 && (v47 = ptr16[21], ptr14 = (unsigned long)(ptr16 + 84), idx14 = (unsigned int [22])ptr->field_28, idx14))
                                        {
LABEL_107c168:
                                            v92 = Time__get_deltaTime(0);
                                            v93 = v45 * ptr->field_40;
                                            v94 = [D] unsupported_Iop_ZeroHI96ofV128();
                                            v95 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v93, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v93, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v93, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v93, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v93, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v93, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                                            if ((char)v95)
                                                v96 = v94;
                                            else
                                                v96 = 0;
                                            *((unsigned int *)ptr14) = v47 + (idx14[21] - v47) * v96;
                                            v0 = v92;
                                            return *((unsigned int *)&v0);
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

## `LB_LightingTrigger_Profile.OnTriggerEnter` — RVA `0xc7c1b4`

- Decompiled symbol: `LB_LightingTrigger_Profile_OnTriggerEnter`
- Metadata signature: `private void OnTriggerEnter(Collider col) { }`
- Native interval: `144` bytes
- Result: `pseudocode`
- Heuristic layout hint: `LB_LightingTrigger_Profile_Recovered` matched 2 offsets against `LB_LightingTrigger_Profile` metadata (confidence 1.00).

```c
typedef struct LB_LightingTrigger_Profile_Recovered {
    char padding_0[56];
    long long cameraTag;
    char padding_40[8];
    char isChanging;
} LB_LightingTrigger_Profile_Recovered;

extern long long g_1f0dcd8;
extern char g_1fab3e7;

long long LB_LightingTrigger_Profile_OnTriggerEnter(struct_0 *ptr, long long a1)
{
    long long v0;  // x0
    unsigned long v1;  // x0
    unsigned long v2;  // x0

    if (!(g_1fab3e7 & 1))
    {
        sub_f7d92c(&g_1f0dcd8);
        g_1fab3e7 = 1;
    }
    if (a1)
    {
        v0 = Component__get_tag(a1, 0);
        v1 = String__op_Equality(v0, ptr->field_38, 0);
        if (!((char)v1 & 1))
            return v1;
        MonoBehaviour__StopCoroutine(ptr, g_1f0dcd8, 0);
        v2 = MonoBehaviour__StartCoroutine(ptr, g_1f0dcd8, 0);
        ptr->field_48 = 1;
        return v2;
    }
    sub_f7db74();
}
```

## `LB_LightingTrigger_Profile.OnTriggerExit` — RVA `0xc7c244`

- Decompiled symbol: `LB_LightingTrigger_Profile_OnTriggerExit`
- Metadata signature: `private void OnTriggerExit(Collider col) { }`
- Native interval: `140` bytes
- Result: `pseudocode`
- Heuristic layout hint: `LB_LightingTrigger_Profile_Recovered` matched 2 offsets against `LB_LightingTrigger_Profile` metadata (confidence 1.00).

```c
typedef struct LB_LightingTrigger_Profile_Recovered {
    char padding_0[56];
    long long cameraTag;
    char padding_40[8];
    char isChanging;
} LB_LightingTrigger_Profile_Recovered;

extern long long g_1f0dcd8;
extern char g_1fab3e8;

long long LB_LightingTrigger_Profile_OnTriggerExit(struct_0 *ptr, long long a1)
{
    long long v0;  // x0
    unsigned long v1;  // x0
    unsigned long v2;  // x0

    if (!(g_1fab3e8 & 1))
    {
        sub_f7d92c(&g_1f0dcd8);
        g_1fab3e8 = 1;
    }
    if (a1)
    {
        v0 = Component__get_tag(a1, 0);
        v1 = String__op_Equality(v0, ptr->field_38, 0);
        if (!((char)v1 & 1))
            return v1;
        MonoBehaviour__StopCoroutine(ptr, g_1f0dcd8, 0);
        v2 = MonoBehaviour__StartCoroutine(ptr, g_1f0dcd8, 0);
        ptr->field_48 = 0;
        return v2;
    }
    sub_f7db74();
}
```

## `LB_LightingTrigger_Profile.StopUpdating` — RVA `0xc7c2d0`

- Decompiled symbol: `LB_LightingTrigger_Profile_StopUpdating`
- Metadata signature: `private IEnumerator StopUpdating() { }`
- Native interval: `108` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[12];
    long long field_20;
} struct_0;

extern char g_1fab3e9;

struct_0 * LB_LightingTrigger_Profile_StopUpdating(long long a0)
{
    struct_0 *v0;  // x20
    struct_0 *ptr;  // x0

    if (!(g_1fab3e9 & 1))
    {
        sub_f7d92c("-l");
        g_1fab3e9 = 1;
    }
    v0 = sub_f7db70(g_1ef33d0);
    Object__ctor(v0, 0);
    ptr = v0;
    ptr->field_10 = 0;
    ptr->field_20 = a0;
    sub_f7d8d0((struct struct_0 *)&ptr->field_20, a0);
    return ptr;
}
```

## `LB_LightingTrigger_Profile.<StopUpdating>d__12.ctor` — RVA `0xc7c33c`

- Decompiled symbol: `LB_LightingTrigger_Profile_StopUpdating_d__12_ctor`
- Metadata signature: `public void .ctor(int <>1__state) { }`
- Native interval: `40` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

void LB_LightingTrigger_Profile_StopUpdating_d__12_ctor(struct_0 *ptr, unsigned int a1)
{
    Object__ctor();
    ptr->field_10 = a1;
    return;
}
```

## `LB_LightingTrigger_Profile.ctor` — RVA `0xc7c364`

- Decompiled symbol: `LB_LightingTrigger_Profile_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `100` bytes
- Result: `pseudocode`
- Heuristic layout hint: `LB_LightingTrigger_Profile_Recovered` matched 2 offsets against `LB_LightingTrigger_Profile` metadata (confidence 1.00).

```c
typedef struct LB_LightingTrigger_Profile_Recovered {
    char padding_0[56];
    long long cameraTag;
    unsigned long long blendSpeed;
} LB_LightingTrigger_Profile_Recovered;

extern long long g_1f0bfa8;
extern char g_1fab3ea;

void LB_LightingTrigger_Profile_ctor(struct_0 *ptr)
{
    unsigned long long v4;  // x30
    unsigned long long v5;  // x21
    unsigned long long v6;  // x20
    unsigned long long v7;  // x19
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x18]
    unsigned long long v2;  // [bp-0x10]
    unsigned long long v3;  // [bp-0x8]

    v0 = v4;
    v1 = v5;
    v2 = v6;
    v3 = v7;
    if (!(g_1fab3ea & 1))
    {
        sub_f7d92c(&g_1f0bfa8);
        g_1fab3ea = 1;
    }
    ptr->field_38 = g_1f0bfa8;
    sub_f7d8d0((struct LB_LightingTrigger_Profile_Recovered *)&ptr->field_38, g_1f0bfa8);
    ptr->field_40 = 0x4040000041200000;
    MonoBehaviour__ctor();
    return;
}
```

## `LB_LightingTrigger_Profile.<StopUpdating>d__12.Dispose` — RVA `0xc7c3c8`

- Decompiled symbol: `LB_LightingTrigger_Profile_StopUpdating_d__12_Dispose`
- Metadata signature: `private void System.IDisposable.Dispose() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long LB_LightingTrigger_Profile_StopUpdating_d__12_Dispose(void)
{
    unsigned long v0;  // x0

    return v0;
}
```

## `LB_LightingTrigger_Profile.<StopUpdating>d__12.MoveNext` — RVA `0xc7c3cc`

- Decompiled symbol: `LB_LightingTrigger_Profile_StopUpdating_d__12_MoveNext`
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
    char padding_0[73];
    char field_49;
} struct_0;

extern long long g_1ef2440;
extern char g_1fab3eb;

unsigned int LB_LightingTrigger_Profile_StopUpdating_d__12_MoveNext(struct_1 *ptr)
{
    struct_0 *p;  // x8
    long long v1;  // x21
    struct_1 *addr;  // x19

    if (!(g_1fab3eb & 1))
    {
        sub_f7d92c(&g_1ef2440);
        g_1fab3eb = 1;
    }
    p = ptr->field_20;
    if (ptr->field_10 == 1)
    {
        ptr->field_10 = 4294967295;
        if (p)
        {
            p->field_49 = 0;
            return 0;
        }
    }
    else if (!ptr->field_10)
    {
        ptr->field_10 = 4294967295;
        if (p)
        {
            p->field_49 = 1;
            v1 = sub_f7db70(g_1ef2440);
            WaitForSeconds__ctor(v1, 0);
            ptr->field_18 = v1;
            addr = &ptr->field_18;
            sub_f7d8d0(addr, v1);
            *((unsigned int *)&addr->padding_0[8]) = 1;
            return 1;
        }
    }
    else
    {
        return 0;
    }
    sub_f7db74();
}
```

## `LB_LightingTrigger_Profile.<StopUpdating>d__12.get_Current` — RVA `0xc7c494`

- Decompiled symbol: `LB_LightingTrigger_Profile_StopUpdating_d__12_get_Current`
- Metadata signature: `private object System.Collections.Generic.IEnumerator<System.Object>.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long LB_LightingTrigger_Profile_StopUpdating_d__12_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```

## `LB_LightingTrigger_Profile.<StopUpdating>d__12.Reset` — RVA `0xc7c49c`

- Decompiled symbol: `LB_LightingTrigger_Profile_StopUpdating_d__12_Reset`
- Metadata signature: `private void System.Collections.IEnumerator.Reset() { }`
- Native interval: `56` bytes
- Result: `pseudocode`

```c
extern long long g_1ef0bd8;
extern long long g_1f047d8;

void LB_LightingTrigger_Profile_StopUpdating_d__12_Reset(void)
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
    sub_f7da4c(v4, sub_f7d940(&g_1f047d8));
}
```

## `LB_LightingTrigger_Profile.<StopUpdating>d__12.get_Current` — RVA `0xc7c4d4`

- Decompiled symbol: `LB_LightingTrigger_Profile_StopUpdating_d__12_get_Current`
- Metadata signature: `private object System.Collections.IEnumerator.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long LB_LightingTrigger_Profile_StopUpdating_d__12_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```
