# Native pseudocode: LB_LightingTrigger_Direct

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `LB_LightingTrigger_Direct.Start` — RVA `0xc7b370`

- Decompiled symbol: `LB_LightingTrigger_Direct_Start`
- Metadata signature: `private void Start() { }`
- Native interval: `200` bytes
- Result: `pseudocode`

```c
extern long long g_1efec60;
extern char g_1fab3da;

long long LB_LightingTrigger_Direct_Start(long long *ptr)
{
    unsigned long long v4;  // x30
    unsigned long long v5;  // x21
    unsigned long long v6;  // x20
    unsigned long long v7;  // x19
    long long v8;  // x0
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x18]
    unsigned long long v2;  // [bp-0x10]
    unsigned long long v3;  // [bp-0x8]

    v0 = v4;
    v1 = v5;
    v2 = v6;
    v3 = v7;
    if (!(g_1fab3da & 1))
    {
        sub_f7d92c(&g_1efec60);
        sub_f7d92c("oG");
        g_1fab3da = 1;
    }
    if (GameObject__FindGameObjectWithTag(ptr[6], 0))
    {
        v8 = sub_1249224();
        ptr[4] = v8;
        sub_f7d8d0(ptr + 4, v8);
        MobileColorGrading__ctor(sub_f7db70(g_1ef0968), 0); /* do not return */
    }
    sub_f7db74();
}
```

## `LB_LightingTrigger_Direct.Update` — RVA `0xc7b438`

- Decompiled symbol: `LB_LightingTrigger_Direct_Update`
- Metadata signature: `private void Update() { }`
- Native interval: `1160` bytes
- Result: `pseudocode`
- Heuristic layout hint: `LB_LightingTrigger_Direct_Recovered` matched 13 offsets against `LB_LightingTrigger_Direct` metadata (confidence 1.00).

```c
typedef struct LB_LightingTrigger_Direct_Recovered {
    char padding_0[32];
    struct struct_1 *current;
    struct struct_2 *temp;
    char padding_30[8];
    unsigned int blendSpeed;
    char padding_3c[4];
    unsigned int Exposure;
    unsigned int Contrast;
    unsigned int Gamma;
    unsigned int Saturation;
    unsigned int vignetteIntensity;
    unsigned int R;
    unsigned int G;
    unsigned int B;
    char isChanging;
    char isUpdating;
} LB_LightingTrigger_Direct_Recovered;

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

int LB_LightingTrigger_Direct_Update(struct_0 *ptr, unsigned long a1)
{
    unsigned int p[22];  // x20
    unsigned int v1;  // s8
    unsigned int v9;  // s0
    unsigned int v98;  // s0
    unsigned int v10;  // s1
    unsigned long v11;  // 4150
    unsigned int v12;  // s0
    unsigned int v13;  // s0
    unsigned int addr[22];  // x20
    unsigned int v15;  // s0
    unsigned int v16;  // s1
    unsigned long v17;  // 4150
    unsigned int v18;  // s0
    unsigned int v19;  // s0
    unsigned int ptr3[22];  // x20
    unsigned int v21;  // s0
    unsigned int v22;  // s1
    unsigned long v23;  // 4150
    unsigned int v24;  // s0
    unsigned int v25;  // s0
    unsigned int ptr4[22];  // x20
    unsigned int v27;  // s0
    unsigned int v28;  // s1
    unsigned long v29;  // 4150
    unsigned int v30;  // s0
    unsigned int v31;  // s0
    unsigned int ptr5[22];  // x20
    unsigned int v33;  // s0
    unsigned int v34;  // s1
    unsigned long v35;  // 4150
    unsigned int v36;  // s0
    unsigned int v37;  // s0
    unsigned int ptr6[22];  // x20
    unsigned int v3;  // s0
    unsigned int v39;  // s0
    unsigned int v40;  // s1
    unsigned long v41;  // 4150
    unsigned int v42;  // s0
    unsigned int v43;  // s0
    unsigned int ptr15[22];  // x20
    unsigned int v45;  // s8
    unsigned long ptr14;  // x20
    unsigned int v47;  // s0
    unsigned int v48;  // s1
    unsigned int v4;  // s1
    unsigned long v49;  // 4150
    unsigned int v50;  // s0
    unsigned int v51;  // s1
    unsigned int v53;  // s0
    unsigned int v54;  // s1
    unsigned long v55;  // 4150
    unsigned int v56;  // s0
    unsigned int v57;  // s0
    unsigned long v5;  // 4150
    unsigned int ptr7[22];  // x20
    unsigned int v59;  // s0
    unsigned int v60;  // s1
    unsigned long v61;  // 4150
    unsigned int v62;  // s0
    unsigned int v63;  // s0
    unsigned int ptr8[22];  // x20
    unsigned int v65;  // s0
    unsigned int v66;  // s1
    unsigned long v67;  // 4150
    unsigned int v6;  // s0
    unsigned int v68;  // s0
    unsigned int v69;  // s0
    unsigned int ptr9[22];  // x20
    unsigned int v71;  // s0
    unsigned int v72;  // s1
    unsigned long v73;  // 4150
    unsigned int v74;  // s0
    unsigned int v75;  // s0
    unsigned int ptr10[22];  // x20
    unsigned int v77;  // s0
    unsigned int v7;  // s0
    unsigned int v78;  // s1
    unsigned long v79;  // 4150
    unsigned int v80;  // s0
    unsigned int v81;  // s0
    unsigned int ptr11[22];  // x20
    unsigned int v83;  // s0
    unsigned int v84;  // s1
    unsigned long v85;  // 4150
    unsigned int v86;  // s0
    unsigned int v87;  // s0
    unsigned int ptr12[22];  // x20
    unsigned int ptr13[22];  // x20
    unsigned int v89;  // s0
    unsigned int v90;  // s1
    unsigned long v91;  // 4150
    unsigned int v92;  // s0
    unsigned int v93;  // s0
    unsigned int ptr16[22];  // x20
    unsigned int v95;  // s0
    unsigned int v96;  // s1
    unsigned long v97;  // 4150

    if (!ptr->field_61)
        return *((unsigned int *)&ptr);
    p = ptr->field_20;
    if (p)
    {
        v1 = p[14];
        if (ptr->field_60)
        {
            Time__get_deltaTime(0);
            v3 = v98 * ptr->field_38;
            v4 = [D] unsupported_Iop_ZeroHI96ofV128();
            v5 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v3, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v3, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v3, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v3, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v3, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v3, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
            if ((char)v5)
                v6 = v4;
            else
                v6 = 0;
            v7 = v1 + (ptr->field_40 - v1) * v6;
            p[14] = v7;
            ptr12 = ptr->field_20;
            if (ptr12)
            {
                Time__get_deltaTime(0);
                v9 = v7 * ptr->field_38;
                v10 = [D] unsupported_Iop_ZeroHI96ofV128();
                v11 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v9, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v9, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v9, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v9, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v9, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v9, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                if ((char)v11)
                    v12 = v10;
                else
                    v12 = 0;
                v13 = ptr12[15] + (ptr->field_44 - ptr12[15]) * v12;
                ptr12[15] = v13;
                addr = ptr->field_20;
                if (addr)
                {
                    Time__get_deltaTime(0);
                    v15 = v13 * ptr->field_38;
                    v16 = [D] unsupported_Iop_ZeroHI96ofV128();
                    v17 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v15, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v15, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v15, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v15, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v15, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v15, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                    if ((char)v17)
                        v18 = v16;
                    else
                        v18 = 0;
                    v19 = addr[17] + (ptr->field_48 - addr[17]) * v18;
                    addr[17] = v19;
                    ptr3 = ptr->field_20;
                    if (ptr3)
                    {
                        Time__get_deltaTime(0);
                        v21 = v19 * ptr->field_38;
                        v22 = [D] unsupported_Iop_ZeroHI96ofV128();
                        v23 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v21, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v21, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v21, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v21, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v21, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v21, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                        if ((char)v23)
                            v24 = v22;
                        else
                            v24 = 0;
                        v25 = ptr3[16] + (ptr->field_4c - ptr3[16]) * v24;
                        ptr3[16] = v25;
                        ptr4 = ptr->field_20;
                        if (ptr4)
                        {
                            Time__get_deltaTime(0);
                            v27 = v25 * ptr->field_38;
                            v28 = [D] unsupported_Iop_ZeroHI96ofV128();
                            v29 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v27, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v27, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v27, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v27, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v27, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v27, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                            if ((char)v29)
                                v30 = v28;
                            else
                                v30 = 0;
                            v31 = ptr4[18] + (ptr->field_50 - ptr4[18]) * v30;
                            ptr4[18] = v31;
                            ptr5 = ptr->field_20;
                            if (ptr5)
                            {
                                Time__get_deltaTime(0);
                                v33 = v31 * ptr->field_38;
                                v34 = [D] unsupported_Iop_ZeroHI96ofV128();
                                v35 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v33, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v33, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v33, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v33, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v33, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v33, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                                if ((char)v35)
                                    v36 = v34;
                                else
                                    v36 = 0;
                                v37 = ptr5[19] + (ptr->field_54 - ptr5[19]) * v36;
                                ptr5[19] = v37;
                                ptr6 = ptr->field_20;
                                if (ptr6)
                                {
                                    Time__get_deltaTime(0);
                                    v39 = v37 * ptr->field_38;
                                    v40 = [D] unsupported_Iop_ZeroHI96ofV128();
                                    v41 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v39, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v39, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v39, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v39, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v39, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v39, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                                    if ((char)v41)
                                        v42 = v40;
                                    else
                                        v42 = 0;
                                    v43 = ptr6[20] + (ptr->field_58 - ptr6[20]) * v42;
                                    ptr6[20] = v43;
                                    ptr15 = ptr->field_20;
                                    if (ptr15)
                                    {
                                        ptr = Time__get_deltaTime(0);
                                        v47 = v43 * ptr->field_38;
                                        v48 = [D] unsupported_Iop_ZeroHI96ofV128();
                                        v49 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v47, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v47, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v47, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v47, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v47, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v47, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                                        if ((char)v49)
                                            v50 = v48;
                                        else
                                            v50 = 0;
                                        ptr15[21] = ptr15[21] + (ptr->field_5c - ptr15[21]) * v50;
                                        return *((unsigned int *)&ptr);
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
        else if (ptr->field_28)
        {
            Time__get_deltaTime(0);
            v53 = v98 * ptr->field_38;
            v54 = [D] unsupported_Iop_ZeroHI96ofV128();
            v55 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v53, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v53, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v53, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v53, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v53, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v53, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
            if ((char)v55)
                v56 = v54;
            else
                v56 = 0;
            v57 = v1 + (ptr->field_28->field_38 - v1) * v56;
            p[14] = v57;
            ptr7 = ptr->field_20;
            if (ptr7 && ptr->field_28)
            {
                Time__get_deltaTime(0);
                v59 = v57 * ptr->field_38;
                v60 = [D] unsupported_Iop_ZeroHI96ofV128();
                v61 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v59, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v59, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v59, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v59, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v59, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v59, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                if ((char)v61)
                    v62 = v60;
                else
                    v62 = 0;
                v63 = ptr7[15] + (ptr->field_28->field_3c - ptr7[15]) * v62;
                ptr7[15] = v63;
                ptr8 = ptr->field_20;
                if (ptr8 && ptr->field_28)
                {
                    Time__get_deltaTime(0);
                    v65 = v63 * ptr->field_38;
                    v66 = [D] unsupported_Iop_ZeroHI96ofV128();
                    v67 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v65, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v65, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v65, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v65, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v65, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v65, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                    if ((char)v67)
                        v68 = v66;
                    else
                        v68 = 0;
                    v69 = ptr8[17] + (ptr->field_28->field_44 - ptr8[17]) * v68;
                    ptr8[17] = v69;
                    ptr9 = ptr->field_20;
                    if (ptr9 && ptr->field_28)
                    {
                        Time__get_deltaTime(0);
                        v71 = v69 * ptr->field_38;
                        v72 = [D] unsupported_Iop_ZeroHI96ofV128();
                        v73 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v71, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v71, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v71, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v71, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v71, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v71, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                        if ((char)v73)
                            v74 = v72;
                        else
                            v74 = 0;
                        v75 = ptr9[16] + (ptr->field_28->field_40 - ptr9[16]) * v74;
                        ptr9[16] = v75;
                        ptr10 = ptr->field_20;
                        if (ptr10 && ptr->field_28)
                        {
                            Time__get_deltaTime(0);
                            v77 = v75 * ptr->field_38;
                            v78 = [D] unsupported_Iop_ZeroHI96ofV128();
                            v79 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v77, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v77, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v77, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v77, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v77, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v77, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                            if ((char)v79)
                                v80 = v78;
                            else
                                v80 = 0;
                            v81 = ptr10[18] + (ptr->field_28->field_48 - ptr10[18]) * v80;
                            ptr10[18] = v81;
                            ptr11 = ptr->field_20;
                            if (ptr11 && ptr->field_28)
                            {
                                Time__get_deltaTime(0);
                                v83 = v81 * ptr->field_38;
                                v84 = [D] unsupported_Iop_ZeroHI96ofV128();
                                v85 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v83, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v83, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v83, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v83, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v83, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v83, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                                if ((char)v85)
                                    v86 = v84;
                                else
                                    v86 = 0;
                                v87 = ptr11[19] + (ptr->field_28->field_4c - ptr11[19]) * v86;
                                ptr11[19] = v87;
                                ptr13 = ptr->field_20;
                                if (ptr13 && ptr->field_28)
                                {
                                    Time__get_deltaTime(0);
                                    v89 = v87 * ptr->field_38;
                                    v90 = [D] unsupported_Iop_ZeroHI96ofV128();
                                    v91 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v89, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v89, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v89, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v89, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v89, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v89, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                                    if ((char)v91)
                                        v92 = v90;
                                    else
                                        v92 = 0;
                                    v93 = ptr13[20] + (ptr->field_28->field_50 - ptr13[20]) * v92;
                                    ptr13[20] = v93;
                                    ptr16 = ptr->field_20;
                                    if (ptr16)
                                    {
                                        v45 = ptr16[21];
                                        ptr14 = &ptr16[21];
                                        if (ptr->field_28)
                                        {
                                            ptr = Time__get_deltaTime(0);
                                            v95 = v93 * ptr->field_38;
                                            v96 = [D] unsupported_Iop_ZeroHI96ofV128();
                                            v97 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v95, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v95, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v95, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v95, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v95, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v95, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                                            if ((char)v97)
                                                v50 = v96;
                                            else
                                                v50 = 0;
                                            v51 = ptr->field_28->field_54 - ptr16[21];
                                            *((unsigned int *)ptr14) = v45 + v51 * v50;
                                            return *((unsigned int *)&ptr);
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

## `LB_LightingTrigger_Direct.OnTriggerEnter` — RVA `0xc7b8c0`

- Decompiled symbol: `LB_LightingTrigger_Direct_OnTriggerEnter`
- Metadata signature: `private void OnTriggerEnter(Collider col) { }`
- Native interval: `144` bytes
- Result: `pseudocode`
- Heuristic layout hint: `LB_LightingTrigger_Direct_Recovered` matched 2 offsets against `LB_LightingTrigger_Direct` metadata (confidence 1.00).

```c
typedef struct LB_LightingTrigger_Direct_Recovered {
    char padding_0[48];
    long long cameraTag;
    char padding_38[40];
    char isChanging;
} LB_LightingTrigger_Direct_Recovered;

extern long long g_1f0dcd8;
extern char g_1fab3db;

unsigned long long LB_LightingTrigger_Direct_OnTriggerEnter(struct_0 *ptr, long long a1)
{
    long long v0;  // x0
    unsigned long long v1;  // x0
    unsigned long long v2;  // x0

    if (!(g_1fab3db & 1))
    {
        sub_f7d92c(&g_1f0dcd8);
        g_1fab3db = 1;
    }
    if (a1)
    {
        v0 = Component__get_tag(a1, 0);
        v1 = String__op_Equality(v0, ptr->field_30, 0);
        if (!((char)v1 & 1))
            return v1;
        MonoBehaviour__StopCoroutine(ptr, g_1f0dcd8, 0);
        v2 = MonoBehaviour__StartCoroutine(ptr, g_1f0dcd8, 0);
        ptr->field_60 = 1;
        return v2;
    }
    sub_f7db74();
}
```

## `LB_LightingTrigger_Direct.OnTriggerExit` — RVA `0xc7b950`

- Decompiled symbol: `LB_LightingTrigger_Direct_OnTriggerExit`
- Metadata signature: `private void OnTriggerExit(Collider col) { }`
- Native interval: `140` bytes
- Result: `pseudocode`
- Heuristic layout hint: `LB_LightingTrigger_Direct_Recovered` matched 2 offsets against `LB_LightingTrigger_Direct` metadata (confidence 1.00).

```c
typedef struct LB_LightingTrigger_Direct_Recovered {
    char padding_0[48];
    long long cameraTag;
    char padding_38[40];
    char isChanging;
} LB_LightingTrigger_Direct_Recovered;

extern long long g_1f0dcd8;
extern char g_1fab3dc;

long long LB_LightingTrigger_Direct_OnTriggerExit(struct_0 *ptr, long long a1)
{
    long long v0;  // x0
    unsigned long v1;  // x0
    unsigned long v2;  // x0

    if (!(g_1fab3dc & 1))
    {
        sub_f7d92c(&g_1f0dcd8);
        g_1fab3dc = 1;
    }
    if (a1)
    {
        v0 = Component__get_tag(a1, 0);
        v1 = String__op_Equality(v0, ptr->field_30, 0);
        if (!((char)v1 & 1))
            return v1;
        MonoBehaviour__StopCoroutine(ptr, g_1f0dcd8, 0);
        v2 = MonoBehaviour__StartCoroutine(ptr, g_1f0dcd8, 0);
        ptr->field_60 = 0;
        return v2;
    }
    sub_f7db74();
}
```

## `LB_LightingTrigger_Direct.StopUpdating` — RVA `0xc7b9dc`

- Decompiled symbol: `LB_LightingTrigger_Direct_StopUpdating`
- Metadata signature: `private IEnumerator StopUpdating() { }`
- Native interval: `116` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[32];
    long long field_20;
} struct_0;

extern char g_1fab3dd;

struct_0 * LB_LightingTrigger_Direct_StopUpdating(long long a0)
{
    struct_0 *v0;  // x20
    struct_0 *ptr;  // x0

    if (!(g_1fab3dd & 1))
    {
        sub_f7d92c("+l");
        g_1fab3dd = 1;
    }
    v0 = sub_f7db70(g_1ef33c8);
    LB_LightingTrigger_Direct_StopUpdating_d__19__ctor(v0, 0, 0);
    if (v0)
    {
        ptr = v0;
        ptr->field_20 = a0;
        sub_f7d8d0((struct struct_0 *)&ptr->field_20, a0);
        return v0;
    }
    sub_f7db74();
}
```

## `LB_LightingTrigger_Direct.ctor` — RVA `0xc7ba50`

- Decompiled symbol: `LB_LightingTrigger_Direct_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `116` bytes
- Result: `pseudocode`
- Heuristic layout hint: `LB_LightingTrigger_Direct_Recovered` matched 4 offsets against `LB_LightingTrigger_Direct` metadata (confidence 1.00).

```c
typedef struct LB_LightingTrigger_Direct_Recovered {
    char padding_0[48];
    long long cameraTag;
    unsigned long long blendSpeed;
    char padding_40[4];
    unsigned long long Contrast;
    unsigned int Saturation;
} LB_LightingTrigger_Direct_Recovered;

extern long long g_1f0bfa8;
extern char g_1fab3de;

void LB_LightingTrigger_Direct_ctor(struct_0 *ptr)
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
    if (!(g_1fab3de & 1))
    {
        sub_f7d92c(&g_1f0bfa8);
        g_1fab3de = 1;
    }
    ptr->field_30 = g_1f0bfa8;
    sub_f7d8d0((struct LB_LightingTrigger_Direct_Recovered *)&ptr->field_30, g_1f0bfa8);
    *((unsigned long long *)&(&ptr->padding_40)[1]) = 0x3f8000003f800000;
    ptr->field_38 = 0x4040000041200000;
    *((unsigned int *)((char *)&ptr->field_44 + 4)) = 0x3f800000;
    MonoBehaviour__ctor();
    return;
}
```

## `LB_LightingTrigger_Direct.<StopUpdating>d__19.ctor` — RVA `0xc7bac4`

- Decompiled symbol: `LB_LightingTrigger_Direct_StopUpdating_d__19_ctor`
- Metadata signature: `public void .ctor(int <>1__state) { }`
- Native interval: `40` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

void LB_LightingTrigger_Direct_StopUpdating_d__19_ctor(struct_0 *ptr, unsigned int a1)
{
    Object__ctor();
    ptr->field_10 = a1;
    return;
}
```

## `LB_LightingTrigger_Direct.<StopUpdating>d__19.Dispose` — RVA `0xc7baec`

- Decompiled symbol: `LB_LightingTrigger_Direct_StopUpdating_d__19_Dispose`
- Metadata signature: `private void System.IDisposable.Dispose() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long LB_LightingTrigger_Direct_StopUpdating_d__19_Dispose(void)
{
    unsigned long v0;  // x0

    return v0;
}
```

## `LB_LightingTrigger_Direct.<StopUpdating>d__19.MoveNext` — RVA `0xc7baf0`

- Decompiled symbol: `LB_LightingTrigger_Direct_StopUpdating_d__19_MoveNext`
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
    char padding_0[97];
    char field_61;
} struct_0;

extern long long g_1ef2440;
extern char g_1fab3e5;

unsigned int LB_LightingTrigger_Direct_StopUpdating_d__19_MoveNext(struct_1 *ptr)
{
    struct_0 *p;  // x8
    long long v1;  // x21
    struct_1 *addr;  // x19

    if (!(g_1fab3e5 & 1))
    {
        sub_f7d92c(&g_1ef2440);
        g_1fab3e5 = 1;
    }
    p = ptr->field_20;
    if (ptr->field_10 == 1)
    {
        ptr->field_10 = 4294967295;
        if (p)
        {
            p->field_61 = 0;
            return 0;
        }
    }
    else if (!ptr->field_10)
    {
        ptr->field_10 = 4294967295;
        if (p)
        {
            p->field_61 = 1;
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

## `LB_LightingTrigger_Direct.<StopUpdating>d__19.get_Current` — RVA `0xc7bbb8`

- Decompiled symbol: `LB_LightingTrigger_Direct_StopUpdating_d__19_get_Current`
- Metadata signature: `private object System.Collections.Generic.IEnumerator<System.Object>.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long LB_LightingTrigger_Direct_StopUpdating_d__19_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```

## `LB_LightingTrigger_Direct.<StopUpdating>d__19.Reset` — RVA `0xc7bbc0`

- Decompiled symbol: `LB_LightingTrigger_Direct_StopUpdating_d__19_Reset`
- Metadata signature: `private void System.Collections.IEnumerator.Reset() { }`
- Native interval: `56` bytes
- Result: `pseudocode`

```c
extern long long g_1ef0bd8;
extern long long g_1f047d0;

void LB_LightingTrigger_Direct_StopUpdating_d__19_Reset(void)
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
    sub_f7da4c(v4, sub_f7d940(&g_1f047d0));
}
```

## `LB_LightingTrigger_Direct.<StopUpdating>d__19.get_Current` — RVA `0xc7bbf8`

- Decompiled symbol: `LB_LightingTrigger_Direct_StopUpdating_d__19_get_Current`
- Metadata signature: `private object System.Collections.IEnumerator.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long LB_LightingTrigger_Direct_StopUpdating_d__19_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```
