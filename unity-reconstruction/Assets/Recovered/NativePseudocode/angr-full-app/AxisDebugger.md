# Native pseudocode: AxisDebugger

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `AxisDebugger.Update` — RVA `0xc68c04`

- Decompiled symbol: `AxisDebugger_Update`
- Metadata signature: `private void Update() { }`
- Native interval: `540` bytes
- Result: `pseudocode`
- Heuristic layout hint: `AxisDebugger_Recovered` matched 5 offsets against `AxisDebugger` metadata (confidence 0.62).

```c
typedef struct AxisDebugger_Recovered {
    char padding_0[36];
    unsigned int deltaResetKey;
    unsigned long long cfScroll;
    unsigned int unScroll[2];
    unsigned int field_34;
    unsigned int cfMouseDelta[2];
    char field_3c;
    char padding_3d[3];
    unsigned int unMouseDelta[2];
    char field_44;
} AxisDebugger_Recovered;

typedef struct struct_1 {
    char padding_0[184];
    struct struct_0 *field_b8;
    char padding_c0[32];
    unsigned int field_e0;
} struct_1;

typedef struct struct_0 {
    char padding_0[24];
    long long field_18;
} struct_0;

typedef struct struct_5 {
    unsigned long long field_0;
} struct_5;

typedef struct struct_4 {
    char padding_0[184];
    struct struct_5 *field_b8;
} struct_4;

typedef struct struct_2 {
    char padding_0[224];
    unsigned int field_e0;
} struct_2;

extern struct_1 *g_1eeed00;
extern struct_2 *g_1ef0c58;
extern struct_4 *g_1ef22b8;
extern long long g_1f0c3a8;
extern long long g_1f0c3b0;
extern char g_1fab1df;
extern char g_1fab1e0;
extern char g_1fab321;

void AxisDebugger_Update(struct_3 *ptr)
{
    unsigned int v0;  // s9
    unsigned long v1;  // d0
    unsigned int v2;  // s8
    unsigned int v3;  // s1
    unsigned int v4;  // s0
    struct_1 *v5;  // x0
    unsigned int v6;  // s0
    long long v7;  // x0

    if (!(g_1fab321 & 1))
    {
        sub_f7d92c(&g_1eeed00);
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c(&g_1f0c3b0);
        sub_f7d92c(&g_1f0c3a8);
        g_1fab321 = 1;
    }
    if (((char)Input__GetKeyDown(ptr->field_24, 0) & 1))
    {
        if (!g_1fab1e0)
        {
            sub_f7d92c(&g_1ef22b8);
            g_1fab1e0 = 1;
        }
        *((unsigned long long *)&ptr->field_30[0]) = g_1ef22b8->field_b8->field_0;
        ptr->field_28 = g_1ef22b8->field_b8->field_0;
        *((unsigned long long *)&ptr->field_34) = g_1ef22b8->field_b8->field_0;
        *((unsigned long long *)&ptr->field_38[1]) = g_1ef22b8->field_b8->field_0;
    }
    if (!g_1eeed00->field_e0)
        sub_f7da5c(g_1eeed00);
    CF2Input__get_mouseScrollDelta(0);
    v0 = ptr->field_30[0];
    v1 = [D] unsupported_Iop_ZeroHI64ofV128();
    ptr->field_28 = v1;
    Input__get_mouseScrollDelta(0);
    v2 = ptr->field_30[1];
    ptr->field_30[0] = v0 + (unsigned int)v1;
    Input__get_mouseScrollDelta(0);
    v4 = v2 + v3;
    ptr->field_30[1] = v4;
    if (!g_1fab1df)
    {
        sub_f7d92c(&g_1eeed00);
        g_1fab1df = 1;
    }
    v5 = g_1eeed00;
    if (!g_1eeed00->field_e0)
    {
        sub_f7da5c(g_1eeed00);
        v5 = g_1eeed00;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (((char)Object__op_Inequality(v5->field_b8->field_18, 0, 0) & 1))
    {
        if (!g_1eeed00->field_e0)
            sub_f7da5c(g_1eeed00);
        CF2Input__GetAxis(g_1f0c3a8, 0);
        v6 = ptr->field_34 + v4;
        ptr->field_34 = v6;
        CF2Input__GetAxis(g_1f0c3b0, 0);
        ptr->field_38[0] = ptr->field_38[0] + v6;
    }
    v7 = AxisDebugger__GetUnityAxis();
    ptr->field_38[1] = ptr->field_38[1];
    AxisDebugger__GetUnityAxis(v7, g_1f0c3b0);
    *((int *)&ptr->field_3c) = *((int *)&ptr->field_3c);
    return;
}
```

## `AxisDebugger.GetUnityAxis` — RVA `0xc68e20`

- Decompiled symbol: `AxisDebugger_GetUnityAxis`
- Metadata signature: `private float GetUnityAxis(string name, float defaultVal = 0.0) { }`
- Native interval: `156` bytes
- Result: `pseudocode`

```c
long long AxisDebugger_GetUnityAxis(unsigned long a0, long long a1)
{
    unsigned long long v0;  // x0

    v0 = Input__GetAxis(a1, 0);
    return Input__GetAxis(a1, 0);
}
```

## `AxisDebugger.OnGUI` — RVA `0xc68ebc`

- Decompiled symbol: `AxisDebugger_OnGUI`
- Metadata signature: `private void OnGUI() { }`
- Native interval: `2796` bytes
- Result: `pseudocode`
- Heuristic layout hint: `AxisDebugger_Recovered` matched 7 offsets against `AxisDebugger` metadata (confidence 1.00).

```c
typedef struct struct_17 {
    char padding_0[184];
    struct struct_16 *field_b8;
    char padding_c0[32];
    unsigned int field_e0;
} struct_17;

typedef struct AxisDebugger_Recovered {
    char padding_0[33];
    char drawMouseStats;
    char drawUnityAxes;
    char padding_23[5];
    unsigned long long cfScroll;
    unsigned long long unScroll;
    unsigned long long cfMouseDelta;
    unsigned long long unMouseDelta;
    long long skin;
} AxisDebugger_Recovered;

typedef struct struct_2 {
    char padding_0[16];
    struct struct_0 *field_10;
} struct_2;

typedef struct struct_0 {
    char padding_0[184];
    struct struct_1 *field_b8;
    char padding_c0[32];
    unsigned int field_e0;
    char padding_e4[81];
    char field_135;
} struct_0;

typedef struct struct_15 {
    char padding_0[128];
    struct struct_14 *field_80;
} struct_15;

typedef struct struct_8 {
    char padding_0[24];
    unsigned int field_18;
    char padding_1c[4];
    long long field_20;
    struct struct_8 *field_28;
    long long field_30;
    struct struct_8 *field_38;
    long long field_40;
    struct struct_8 *field_48;
    long long field_50;
    struct struct_8 *field_58;
} struct_8;

typedef struct struct_7 {
    long long field_0;
    char padding_8[48];
    struct struct_6 *field_38;
} struct_7;

typedef struct struct_14 {
    char padding_0[16];
    struct struct_13 *field_10;
} struct_14;

typedef struct struct_13 {
    char padding_0[24];
    int field_18;
} struct_13;

typedef struct struct_22 {
    char padding_0[16];
    long long field_10;
} struct_22;

typedef struct struct_10 {
    char padding_0[24];
    unsigned int field_18;
    char padding_1c[4];
    struct struct_9 *field_20;
} struct_10;

typedef struct struct_12 {
    char padding_0[24];
    unsigned int field_18;
    char padding_1c[4];
    struct struct_11 *field_20;
} struct_12;

typedef struct struct_16 {
    char padding_0[24];
    struct struct_15 *field_18;
} struct_16;

typedef struct struct_1 {
    long long field_0;
} struct_1;

typedef struct struct_6 {
    char padding_0[16];
    struct struct_4 *field_10;
} struct_6;

typedef struct struct_9 {
    char padding_0[24];
    unsigned int field_18;
    char padding_1c[4];
    unsigned long long field_20;
    struct struct_9 *field_28;
    unsigned long long field_30;
    struct struct_9 *field_38;
    unsigned long long field_40;
    struct struct_9 *field_48;
    unsigned long long field_50;
    struct struct_9 *field_58;
} struct_9;

typedef struct struct_11 {
    char padding_0[24];
    unsigned int field_18;
    char padding_1c[4];
    unsigned long long field_20;
    struct struct_11 *field_28;
    unsigned long long field_30;
    struct struct_11 *field_38;
    unsigned long long field_40;
    struct struct_11 *field_48;
    unsigned long long field_50;
    struct struct_11 *field_58;
} struct_11;

typedef struct struct_4 {
    char padding_0[184];
    struct struct_5 *field_b8;
    char padding_c0[32];
    unsigned int field_e0;
    char padding_e4[81];
    char field_135;
} struct_4;

typedef struct struct_5 {
    unsigned long long field_0;
} struct_5;

typedef struct struct_20 {
    char padding_0[224];
    unsigned int field_e0;
} struct_20;

typedef struct struct_3 {
    unsigned long long field_0;
    char padding_8[48];
    struct struct_2 *field_38;
} struct_3;

extern long long g_1db6f08;
extern long long g_1eee120;
extern struct_17 *g_1eeed00;
extern struct_20 *g_1ef0c58;
extern long long g_1ef90d0;
extern long long g_1ef90d8;
extern struct_3 *g_1efbd88;
extern long long g_1f06220;
extern struct_7 g_1f06820;
extern long long g_1f07690;
extern long long g_1f083a0;
extern long long g_1f08c28;
extern long long g_1f0d820;
extern long long g_1f0f260;
extern long long g_1f0f268;
extern char g_1fab1df;
extern char g_1fab322;

long long AxisDebugger_OnGUI(struct_21 *ptr)
{
    struct_17 *v5;  // x0
    long long v6;  // x0
    struct_2 *addr;  // x8
    struct_0 *v16;  // x0
    struct_0 *v17;  // x0
    struct_8 *v18;  // x0
    struct_8 *v19;  // x20
    struct_8 *ptr3;  // x21
    struct_8 *v21;  // x21
    struct_8 *ptr4;  // x21
    struct_8 *v23;  // x21
    struct_7 *v24;  // x24
    long long v7;  // x0
    struct_8 *ptr5;  // x21
    struct_8 *v26;  // x21
    struct_8 *ptr6;  // x21
    struct_8 *v28;  // x21
    struct_8 *ptr7;  // x21
    struct_8 *v30;  // x21
    struct_8 *ptr8;  // x21
    struct_8 *v32;  // x21
    struct_8 *ptr9;  // x21
    struct_8 *v34;  // x21
    long long v8;  // x0
    struct_8 *v35;  // x1
    struct_8 *ptr10;  // x0
    long long v37;  // x0
    struct_2 *ptr11;  // x8
    struct_0 *v39;  // x0
    struct_0 *v40;  // x0
    struct_17 *idx18;  // x0
    struct_13 *v42;  // x20
    int v43;  // w21
    struct_2 *ptr12;  // x8
    unsigned int v44;  // s0
    struct_22 *v45;  // x0
    struct_22 *v46;  // x23
    unsigned long long v47;  // 4103
    unsigned int v48;  // 4099
    unsigned long v49;  // 4115
    struct_2 *ptr13;  // x8
    struct_0 *v51;  // x0
    struct_0 *v52;  // x0
    struct_2 *ptr14;  // x8
    struct_0 *v10;  // x0
    struct_0 *v54;  // x0
    struct_0 *v55;  // x0
    unsigned int v56;  // s0
    unsigned long long v57;  // 4105
    unsigned int v58;  // w9
    unsigned long long v59;  // 4102
    unsigned int v60;  // w10
    unsigned long long v61;  // 4102
    unsigned int v62;  // w10
    unsigned int v63;  // w9
    struct_0 *v11;  // x0
    unsigned long v64;  // cc_dep1
    unsigned long v65;  // 4106
    unsigned long v66;  // 4106
    long long v67;  // x0
    long long v68;  // x0
    struct_2 *ptr15;  // x8
    struct_0 *v70;  // x0
    struct_0 *v71;  // x0
    struct_10 *v72;  // x23
    struct_8 *v73;  // x1
    struct_17 *v12;  // x0
    struct_10 *ptr16;  // x0
    unsigned int v75;  // s0
    unsigned long long v76;  // 4105
    unsigned int v77;  // w9
    unsigned long long v78;  // 4102
    unsigned int v79;  // w10
    unsigned long long v80;  // 4102
    unsigned int v81;  // w10
    unsigned int v82;  // w9
    unsigned long v83;  // cc_dep1
    long long v13;  // x0
    unsigned long v84;  // 4106
    unsigned long v85;  // 4106
    long long v86;  // x0
    struct_2 *ptr17;  // x8
    struct_0 *v88;  // x0
    struct_0 *v89;  // x0
    struct_12 *v90;  // x23
    struct_8 *v91;  // x1
    struct_12 *ptr18;  // x0
    unsigned long long v93;  // x0
    long long v14;  // x0
    long long *ptr;  // x0
    long long v95;  // x0
    long long v96;  // x0
    unsigned int v0;  // [bp-0xa0], Other Possible Types: unsigned long long
    unsigned int v1;  // [bp-0x9c]
    unsigned long long v2;  // [bp-0x98], Other Possible Types: unsigned long
    char *v3;  // [bp-0x60]
    char v4;  // [bp+0x0]

    v3 = &v4;
    if (!(g_1fab322 & 1))
    {
        sub_f7d92c(&g_1efbd88);
        sub_f7d92c(&g_1eeed00);
        sub_f7d92c(&g_1eee120);
        sub_f7d92c("y<");
        sub_f7d92c("O<");
        sub_f7d92c(&g_1ef90d0);
        sub_f7d92c(&g_1ef90d8);
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c("I)");
        sub_f7d92c(&g_1f083a0);
        sub_f7d92c(&g_1f0f260);
        sub_f7d92c(&g_1f0f268);
        sub_f7d92c("Y");
        sub_f7d92c(&g_1f0d820);
        sub_f7d92c(&g_1f06220);
        sub_f7d92c(&g_1f07690);
        sub_f7d92c(&g_1f08c28);
        sub_f7d92c(&g_1f06820.field_0);
        g_1fab322 = 1;
    }
    v0 = 0;
    v2 = 0;
    if (!g_1eeed00->field_e0)
        sub_f7da5c(g_1eeed00);
    if (!g_1fab1df)
    {
        sub_f7d92c(&g_1eeed00);
        g_1fab1df = 1;
    }
    v5 = g_1eeed00;
    if (!g_1eeed00->field_e0)
    {
        sub_f7da5c(g_1eeed00);
        v5 = g_1eeed00;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v6 = Object__op_Equality(v5->field_b8->field_18, 0, 0);
    if (((char)v6 & 1))
        return v6;
    if (!g_1eefa78->field_e0)
        sub_f7da5c(g_1eefa78);
    GUI__set_skin(ptr->field_48, 0);
    v7 = GUI__get_skin(0);
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (!((char)Object__op_Inequality(v7, 0, 0) & 1))
    {
        if (!g_1eefab8->field_e0)
            sub_f7da5c(g_1eefab8);
        v8 = GUIStyle__get_none(0);
        goto LABEL_1069108;
    }
    if (!g_1eefa78->field_e0)
        sub_f7da5c(g_1eefa78);
    if (GUI__get_skin(0))
    {
        v8 = GUISkin__get_box();
LABEL_1069108:
        ptr12 = g_1efbd88->field_38;
        if (!g_1efbd88->field_38)
        {
            sub_f80068(g_1efbd88);
            ptr12 = g_1efbd88->field_38;
        }
        v10 = ptr12->field_10;
        if (!(v10->field_135 & 1))
            v10 = sub_f8000c(v10);
        if (!v10->field_e0)
            sub_f7da5c();
        v11 = g_1efbd88->field_38->field_10;
        if (!(v11->field_135 & 1))
            v11 = sub_f8000c(v11);
        GUILayout__BeginVertical(v8, v11->field_b8->field_0, 0);
        if (!g_1eeed00->field_e0)
            sub_f7da5c(g_1eeed00);
        if (!g_1fab1df)
        {
            sub_f7d92c(&g_1eeed00);
            g_1fab1df = 1;
        }
        v12 = g_1eeed00;
        if (!g_1eeed00->field_e0)
        {
            sub_f7da5c(g_1eeed00);
            v12 = g_1eeed00;
        }
        if (v12->field_b8->field_18)
        {
            v13 = Object__get_name(v12->field_b8->field_18, 0);
            v14 = String__Concat(g_1f083a0, v13, 0);
            addr = g_1efbd88->field_38;
            if (!g_1efbd88->field_38)
            {
                sub_f80068(g_1efbd88);
                addr = g_1efbd88->field_38;
            }
            v16 = addr->field_10;
            if (!(v16->field_135 & 1))
                v16 = sub_f8000c(v16);
            if (!v16->field_e0)
                sub_f7da5c();
            v17 = g_1efbd88->field_38->field_10;
            if (!(v17->field_135 & 1))
                v17 = sub_f8000c(v17);
            GUILayout__Box(v14, v17->field_b8->field_0, 0);
            if (ptr->field_21)
            {
                v18 = sub_f7d9d4(g_1eee378, 8);
                if (v18)
                {
                    v19 = v18;
                    if (v18->field_18)
                    {
                        ptr3 = v19;
                        ptr3->field_20 = g_1f0d820;
                        v21 = &ptr3->field_20;
                        sub_f7d8d0(v21, g_1f0d820);
                        v2 = ptr->field_28;
                        v18 = sub_106a514(&v2, 0, 0, 0);
                        if (*((int *)&v21->padding_0[8]) > 1 && (ptr4 = v19, ptr4->field_28 = (struct struct_8 *)v18, v23 = ptr4 + 40, v18 = (struct_8 *)sub_f7d8d0(v23, v18), *((int *)&v23->padding_0[16]) > 2))
                        {
                            v24 = &g_1f06820.field_0;
                            ptr5 = v19;
                            ptr5->field_30 = g_1f06820.field_0;
                            v26 = &ptr5->field_30;
                            sub_f7d8d0(v26, g_1f06820.field_0);
                            v2 = ptr->field_30;
                            v18 = sub_106a514(&v2, 0, 0, 0);
                            if (v26->field_18 > 3 && (ptr6 = v19, ptr6->field_38 = (struct struct_8 *)v18, v28 = ptr6 + 56, v18 = (struct_8 *)sub_f7d8d0(v28, v18), (int)v28->field_20 > 4))
                            {
                                ptr7 = v19;
                                ptr7->field_40 = g_1f06380;
                                v30 = &ptr7->field_40;
                                sub_f7d8d0(v30, g_1f06380);
                                v2 = ptr->field_38;
                                v18 = sub_106a514(&v2, 0, 0, 0);
                                if ((int)v30->field_28 > 5 && (ptr8 = v19, ptr8->field_48 = (struct struct_8 *)v18, v32 = ptr8 + 72, v18 = (struct_8 *)sub_f7d8d0(v32, v18), (int)v32->field_30 > 6))
                                {
                                    ptr9 = v19;
                                    ptr9->field_50 = g_1f06820.field_0;
                                    v34 = &ptr9->field_50;
                                    sub_f7d8d0(v34, g_1f06820.field_0);
                                    v2 = ptr->field_40;
                                    v18 = sub_106a514(&v2, 0, 0, 0);
                                    if ((int)v34->field_38 > 7)
                                    {
                                        v35 = v18;
                                        ptr10 = v19;
                                        ptr10->field_58 = v35;
                                        sub_f7d8d0((struct struct_8 *)&ptr10->field_58, v35);
                                        v37 = String__Concat(v19, 0);
                                        ptr11 = g_1efbd88->field_38;
                                        if (!g_1efbd88->field_38)
                                        {
                                            sub_f80068(g_1efbd88);
                                            ptr11 = g_1efbd88->field_38;
                                        }
                                        v39 = ptr11->field_10;
                                        if (!(v39->field_135 & 1))
                                            v39 = sub_f8000c(v39);
                                        if (!v39->field_e0)
                                            sub_f7da5c();
                                        v40 = g_1efbd88->field_38->field_10;
                                        if (!(v40->field_135 & 1))
                                            v40 = sub_f8000c(v40);
                                        GUILayout__Box(v37, v40->field_b8->field_0, 0);
                                        goto LABEL_1069450;
                                    }
                                }
                            }
                        }
                    }
                }
            }
            else
            {
LABEL_1069450:
                if (!g_1eeed00->field_e0)
                    sub_f7da5c(g_1eeed00);
                if (!g_1fab1df)
                {
                    sub_f7d92c(&g_1eeed00);
                    g_1fab1df = 1;
                }
                idx18 = g_1eeed00;
                if (!g_1eeed00->field_e0)
                {
                    sub_f7da5c(g_1eeed00);
                    idx18 = g_1eeed00;
                }
                if (idx18->field_b8->field_18 && idx18->field_b8->field_18->field_80 && !((v42 = (struct_13 *)idx18->field_b8->field_18->field_80->field_10, !v42)))
                {
                    if (v42->field_18 >= 1)
                    {
                        v43 = 0;
                        do
                        {
                            v45 = sub_14a30c0(v42, v43, g_1ef90d8);
                            v0 = 0;
                            if (!v45)
                                goto LABEL_1069968;
                            v46 = v45;
                            InputRig_AxisConfig__GetAnalog();
                            v1 = v44;
                            Input__GetAxis(v46->field_10, 0);
                            v0 = v44;
                            v44 = v1;
                            v47 = (((CmpF(v44, 0.0) >> 5 & 3 | CmpF(v44, 0.0) & 1) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - ((CmpF(v44, 0.0) >> 5 & 3 | CmpF(v44, 0.0) & 1) & (CmpF(v44, 0.0) >> 5 & 3 | CmpF(v44, 0.0) & 1) >> 1 & 1);
                            if ((char)(v47 * 0x10000000 >> 30) && (!ptr->field_22 || !((v44 = v0, v48 = (unsigned int)(CmpF(v44, 0.0)), v49 = (unsigned long)(((((unsigned long long)(char)(CmpF(v44, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v44, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1), !((char)((v49 - (((unsigned long long)(char)(CmpF(v44, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v44, 0.0) & 1)) & ((unsigned long long)v48 >> 5 & 3 | (unsigned long long)(CmpF(v44, 0.0) & 1)) >> 1 & 1)) * 0x10000000 >> 30))))))
                                continue;
                            ptr13 = g_1efbd88->field_38;
                            if (!g_1efbd88->field_38)
                            {
                                sub_f80068(g_1efbd88);
                                ptr13 = g_1efbd88->field_38;
                            }
                            v51 = ptr13->field_10;
                            if (!(v51->field_135 & 1))
                                v51 = sub_f8000c(v51);
                            if (!v51->field_e0)
                                sub_f7da5c();
                            v52 = g_1efbd88->field_38->field_10;
                            if (!(v52->field_135 & 1))
                                v52 = sub_f8000c(v52);
                            GUILayout__BeginVertical(v52->field_b8->field_0, 0);
                            ptr14 = g_1efbd88->field_38;
                            if (!g_1efbd88->field_38)
                            {
                                sub_f80068(g_1efbd88);
                                ptr14 = g_1efbd88->field_38;
                            }
                            v54 = ptr14->field_10;
                            if (!(v54->field_135 & 1))
                                v54 = sub_f8000c(v54);
                            if (!v54->field_e0)
                                sub_f7da5c();
                            v55 = g_1efbd88->field_38->field_10;
                            if (!(v55->field_135 & 1))
                                v55 = sub_f8000c(v55);
                            GUILayout__Label(v46->field_10, v55->field_b8->field_0, 0);
                            v56 = v1;
                            v57 = (((CmpF(v56, 0.0) >> 5 & 3 | CmpF(v56, 0.0) & 1) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - ((CmpF(v56, 0.0) >> 5 & 3 | CmpF(v56, 0.0) & 1) & (CmpF(v56, 0.0) >> 5 & 3 | CmpF(v56, 0.0) & 1) >> 1 & 1);
                            if (!((char)(v57 * 0x10000000 >> 30)))
                                v58 = 0;
                            else
                                v58 = 1;
                            v59 = (((CmpF(v56, 0x3f800000) >> 5 & 3 | CmpF(v56, 0x3f800000) & 1) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - ((CmpF(v56, 0x3f800000) >> 5 & 3 | CmpF(v56, 0x3f800000) & 1) & (CmpF(v56, 0x3f800000) >> 5 & 3 | CmpF(v56, 0x3f800000) & 1) >> 1 & 1);
                            if (!((char)(v59 * 0x10000000 >> 30)))
                                v60 = 0;
                            else
                                v60 = 1;
                            v61 = (((CmpF(v56, 0xbf800000) >> 5 & 3 | CmpF(v56, 0xbf800000) & 1) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - ((CmpF(v56, 0xbf800000) >> 5 & 3 | CmpF(v56, 0xbf800000) & 1) & (CmpF(v56, 0xbf800000) >> 5 & 3 | CmpF(v56, 0xbf800000) & 1) >> 1 & 1);
                            if (!((char)(v61 * 0x10000000 >> 30)))
                                v62 = 0;
                            else
                                v62 = 1;
                            v63 = v62 | v58 | v60;
                            v64 = v63;
                            if (v63)
                            {
                                v65 = arm64g_calculate_condition(19, v64, 0, 0);
                                if (!((char)v65))
                                    goto LABEL_106963a;
                                goto LABEL_1069639;
                            }
                            else
                            {
                                v66 = arm64g_calculate_condition(19, v64, 0, 0);
                                if ((char)v66)
                                {
LABEL_1069639:
                                    goto LABEL_106963a;
                                }
                                else
                                {
LABEL_106963a:
                                    if (!g_1eefa78->field_e0)
                                        sub_f7da5c(g_1eefa78);
                                    GUI__set_color(0);
                                    v67 = Single__ToString(&v1, g_1f07690, 0);
                                    v68 = String__Concat(g_1f08c28, v67, 0);
                                    v24 = g_1efbd88;
                                    ptr15 = g_1efbd88->field_38;
                                    if (!g_1efbd88->field_38)
                                    {
                                        sub_f80068(g_1efbd88);
                                        ptr15 = g_1efbd88->field_38;
                                    }
                                    v70 = ptr15->field_10;
                                    if (!(v70->field_135 & 1))
                                        v70 = sub_f8000c(v70);
                                    if (!v70->field_e0)
                                        sub_f7da5c();
                                    v71 = g_1efbd88->field_38->field_10;
                                    if (!(v71->field_135 & 1))
                                        v71 = sub_f8000c(v71);
                                    GUILayout__Label(v68, v71->field_b8->field_0, 0);
                                    v72 = sub_f7d9d4(g_1eee120, 1);
                                    v18 = GUILayout__Width(0);
                                    if (!v72)
                                        goto LABEL_1069968;
                                    if (!v72->field_18)
                                        goto LABEL_106996c;
                                    v73 = v18;
                                    ptr16 = v72;
                                    ptr16->field_20 = v73;
                                    sub_f7d8d0((struct struct_10 *)&ptr16->field_20, v73);
                                    GUILayout__Box(g_1f06220, v72, 0);
                                    if (ptr->field_22)
                                    {
                                        v75 = v0;
                                        v76 = (((CmpF(v75, 0.0) >> 5 & 3 | CmpF(v75, 0.0) & 1) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - ((CmpF(v75, 0.0) >> 5 & 3 | CmpF(v75, 0.0) & 1) & (CmpF(v75, 0.0) >> 5 & 3 | CmpF(v75, 0.0) & 1) >> 1 & 1);
                                        if (!((char)(v76 * 0x10000000 >> 30)))
                                            v77 = 0;
                                        else
                                            v77 = 1;
                                        v78 = (((CmpF(v75, 0x3f800000) >> 5 & 3 | CmpF(v75, 0x3f800000) & 1) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - ((CmpF(v75, 0x3f800000) >> 5 & 3 | CmpF(v75, 0x3f800000) & 1) & (CmpF(v75, 0x3f800000) >> 5 & 3 | CmpF(v75, 0x3f800000) & 1) >> 1 & 1);
                                        if (!((char)(v78 * 0x10000000 >> 30)))
                                            v79 = 0;
                                        else
                                            v79 = 1;
                                        v80 = (((CmpF(v75, 0xbf800000) >> 5 & 3 | CmpF(v75, 0xbf800000) & 1) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - ((CmpF(v75, 0xbf800000) >> 5 & 3 | CmpF(v75, 0xbf800000) & 1) & (CmpF(v75, 0xbf800000) >> 5 & 3 | CmpF(v75, 0xbf800000) & 1) >> 1 & 1);
                                        if (!((char)(v80 * 0x10000000 >> 30)))
                                            v81 = 0;
                                        else
                                            v81 = 1;
                                        v82 = v81 | v77 | v79;
                                        v83 = v82;
                                        if (v82)
                                        {
                                            v84 = arm64g_calculate_condition(19, v83, 0, 0);
                                            if (!((char)v84))
                                                goto LABEL_106978a;
                                        }
                                        else
                                        {
                                            v85 = arm64g_calculate_condition(19, v83, 0, 0);
                                            if (!((char)v85))
                                            {
LABEL_106978a:
                                                if (!g_1eefa78->field_e0)
                                                    sub_f7da5c(g_1eefa78);
                                                GUI__set_color(0);
                                                if (true)
                                                    Single__ToString(&v0, g_1f07690, 0);
                                                v86 = String__Concat(g_1f0f260);
                                                v24 = g_1efbd88;
                                                ptr17 = g_1efbd88->field_38;
                                                if (!g_1efbd88->field_38)
                                                {
                                                    sub_f80068(g_1efbd88);
                                                    ptr17 = g_1efbd88->field_38;
                                                }
                                                v88 = ptr17->field_10;
                                                if (!(v88->field_135 & 1))
                                                    v88 = sub_f8000c(v88);
                                                if (!v88->field_e0)
                                                    sub_f7da5c();
                                                v89 = g_1efbd88->field_38->field_10;
                                                if (!(v89->field_135 & 1))
                                                    v89 = sub_f8000c(v89);
                                                GUILayout__Label(v86, v89->field_b8->field_0, 0);
                                                v90 = sub_f7d9d4(g_1eee120, 1);
                                                v18 = GUILayout__Width(0);
                                                if (!v90)
                                                    goto LABEL_1069968;
                                                if (!v90->field_18)
                                                    goto LABEL_106996c;
                                                v91 = v18;
                                                ptr18 = v90;
                                                ptr18->field_20 = v91;
                                                sub_f7d8d0((struct struct_12 *)&ptr18->field_20, v91);
                                                GUILayout__Box(g_1f06220, v90, 0);
                                                goto LABEL_10698a8;
                                            }
                                        }
                                        goto LABEL_106978a;
                                    }
                                    else
                                    {
LABEL_10698a8:
                                        GUILayout__EndVertical(0);
                                        if (!g_1eefa78->field_e0)
                                            sub_f7da5c(g_1eefa78);
                                        v44 = 0x3f800000;
                                        GUI__set_color(0);
                                    }
                                }
                            }
                        } while ((v43 = (int)(v43 + 1), v43 < v42->field_18));
                    }
                    else
                    {
                        v93 = GUILayout__EndVertical(0);
                        return GUILayout__EndVertical(0);
                    }
                }
            }
        }
    }
LABEL_1069968:
    v18 = sub_f7db74();
LABEL_106996c:
    sub_f7db7c(v18);
    ptr = __cxa_allocate_exception(8);
    *(ptr) = v24->field_0;
    v95 = __cxa_throw(ptr, &g_1db6f08, 0);
    __cxa_end_catch();
    v96 = sub_1026098(v95);
    sub_e29990(v96);
}
```

## `AxisDebugger.ctor` — RVA `0xc699a8`

- Decompiled symbol: `AxisDebugger_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `24` bytes
- Result: `pseudocode`
- Heuristic layout hint: `AxisDebugger_Recovered` matched 2 offsets against `AxisDebugger` metadata (confidence 1.00).

```c
typedef struct AxisDebugger_Recovered {
    char padding_0[32];
    char drawGUI;
    char padding_21[3];
    unsigned int deltaResetKey;
} AxisDebugger_Recovered;

long long AxisDebugger_ctor(struct_0 *ptr)
{
    long long v0;  // x0

    ptr->field_20 = 1;
    ptr->field_24 = 286;
    v0 = MonoBehaviour__ctor();
    return MonoBehaviour__ctor();
}
```
