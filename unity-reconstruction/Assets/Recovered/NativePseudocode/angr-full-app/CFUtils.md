# Native pseudocode: CFUtils

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `CFUtils.get_realDeltaTime` — RVA `0xc4e208`

- Decompiled symbol: `CFUtils_get_realDeltaTime`
- Metadata signature: `public static float get_realDeltaTime() { }`
- Native interval: `60` bytes
- Result: `pseudocode`

```c
int CFUtils_get_realDeltaTime(void)
{
    if (Time__get_captureFramerate(0) < 1)
        return Time__get_unscaledDeltaTime();
    return Time__get_captureFramerate(0);
}
```

## `CFUtils.TransformRectAsBounds` — RVA `0xc51858`

- Decompiled symbol: `CFUtils_TransformRectAsBounds`
- Metadata signature: `public static Bounds TransformRectAsBounds(Rect r, Matrix4x4 tr, bool round) { }`
- Native interval: `836` bytes
- Result: `pseudocode`

```c
unsigned long long CFUtils_TransformRectAsBounds(long long a0, unsigned int a1)
{
    unsigned int v0;  // s2
    unsigned int v1;  // s14
    unsigned int v10;  // s0
    unsigned long v92;  // 4106
    unsigned int v93;  // s4
    unsigned int v94;  // s19
    unsigned long long v95;  // cc_dep1
    unsigned long v96;  // 4129
    unsigned int v97;  // s18
    unsigned long v98;  // 4106
    unsigned long v99;  // 4106
    unsigned int v100;  // s3
    unsigned int v11;  // s2
    unsigned long v101;  // 4129
    unsigned int v102;  // s17
    unsigned long v103;  // 4129
    unsigned int v104;  // s18
    unsigned long v105;  // 4129
    unsigned int v106;  // s19
    unsigned long v107;  // 4129
    unsigned int v108;  // s3
    unsigned int v109;  // s28
    unsigned long v110;  // 4132
    unsigned int v12;  // s7
    unsigned int v111;  // s4
    unsigned int v112;  // s27
    unsigned long v113;  // 4132
    unsigned int v114;  // s5
    unsigned long long v115;  // cc_dep1
    unsigned int v116;  // s24
    unsigned long v117;  // 4132
    unsigned int v118;  // s2
    unsigned long v119;  // 4106
    unsigned long v120;  // 4106
    unsigned long long v13;  // cc_dep1
    unsigned int v121;  // s7
    unsigned long long v122;  // cc_dep1
    unsigned long v123;  // 4129
    unsigned int v124;  // s16
    unsigned long v125;  // 4106
    unsigned long v126;  // 4106
    unsigned int v127;  // s20
    unsigned long long v128;  // cc_dep1
    unsigned int v14;  // s16
    unsigned long v129;  // 4129
    unsigned int v130;  // s0
    unsigned long v131;  // 4106
    unsigned long v132;  // 4106
    unsigned int v133;  // s6
    unsigned long v134;  // 4129
    unsigned int v135;  // s0
    unsigned long v136;  // 4129
    unsigned int v137;  // s1
    unsigned long v15;  // 4142
    unsigned long v138;  // 4129
    unsigned int v139;  // s2
    unsigned long v140;  // 4129
    unsigned int v141;  // s3
    unsigned long v142;  // 4129
    unsigned int v143;  // s4
    unsigned long v144;  // 4129
    unsigned int v145;  // s5
    unsigned int v146;  // s2
    unsigned int v147;  // s7
    unsigned int v16;  // s21
    unsigned int v148;  // s1
    unsigned int v149;  // s4
    unsigned int v150;  // s16
    unsigned int v151;  // s0
    unsigned int v152;  // s5
    unsigned long long v153;  // cc_dep1
    unsigned int v154;  // s3
    unsigned int v155;  // s6
    unsigned long v156;  // 4216
    unsigned int v157;  // s20
    unsigned long v17;  // 4106
    unsigned long v158;  // 4106
    unsigned long v159;  // 4106
    unsigned int v160;  // s4
    unsigned long long v161;  // cc_dep1
    unsigned int v162;  // s19
    unsigned long v163;  // 4132
    unsigned int v164;  // s2
    unsigned long v165;  // 4106
    unsigned long v166;  // 4106
    unsigned long v18;  // 4106
    unsigned int v167;  // s5
    unsigned long long v168;  // cc_dep1
    unsigned int v169;  // s18
    unsigned long v170;  // 4132
    unsigned int v171;  // s7
    unsigned long v172;  // 4106
    unsigned long v173;  // 4106
    unsigned int v174;  // s6
    unsigned int v19;  // s2
    unsigned long long v175;  // cc_dep1
    unsigned int v176;  // s17
    unsigned long v177;  // 4132
    unsigned int v178;  // s16
    unsigned long v179;  // 4106
    unsigned long v180;  // 4106
    unsigned int v181;  // s19
    unsigned long long v182;  // cc_dep1
    unsigned long v183;  // 4129
    unsigned int v2;  // s3
    unsigned int v184;  // s21
    unsigned long v185;  // 4106
    unsigned long v186;  // 4106
    unsigned int v187;  // s18
    unsigned long long v188;  // cc_dep1
    unsigned long v189;  // 4129
    unsigned int v190;  // s0
    unsigned long v191;  // 4106
    unsigned long v192;  // 4106
    unsigned int v20;  // s2
    unsigned int v193;  // s3
    unsigned long v194;  // 4129
    unsigned long v195;  // 4129
    unsigned long v196;  // 4129
    unsigned long v197;  // 4129
    unsigned long long v21;  // cc_dep1
    unsigned long v198;  // 4129
    unsigned long v199;  // 4129
    unsigned int ptr[6];  // x8
    unsigned int v201;  // s0
    unsigned long v22;  // 4129
    unsigned int v202;  // s1
    unsigned int v23;  // s22
    unsigned long v24;  // 4106
    unsigned long v25;  // 4106
    unsigned int v26;  // s7
    unsigned int v27;  // s7
    unsigned int v3;  // s15
    unsigned long long v28;  // cc_dep1
    unsigned long v29;  // 4129
    unsigned int v30;  // s23
    unsigned long v31;  // 4106
    unsigned long v32;  // 4106
    unsigned int v33;  // s16
    unsigned int v34;  // s16
    unsigned int v35;  // s26
    unsigned int v36;  // s0
    unsigned long long v4;  // x0
    unsigned int v37;  // s25
    unsigned int v38;  // s1
    unsigned int v39;  // s28
    unsigned int v40;  // s24
    unsigned int v41;  // s6
    unsigned int v42;  // s27
    unsigned int v43;  // s0
    unsigned int v44;  // s26
    unsigned int v45;  // s20
    unsigned int v46;  // s1
    unsigned int v5;  // s3
    unsigned int v47;  // s25
    unsigned long long v48;  // cc_dep1
    unsigned int v49;  // s6
    unsigned int v50;  // s24
    unsigned long v51;  // 4294
    unsigned int v52;  // s29
    unsigned long v53;  // 4106
    unsigned long v54;  // 4106
    unsigned int v55;  // s26
    unsigned int v6;  // s4
    unsigned long long v56;  // cc_dep1
    unsigned long v57;  // 4129
    unsigned int v58;  // s28
    unsigned long v59;  // 4106
    unsigned long v60;  // 4106
    unsigned int v61;  // s25
    unsigned long long v62;  // cc_dep1
    unsigned long v63;  // 4129
    unsigned int v64;  // s27
    unsigned int v7;  // s5
    unsigned long v65;  // 4106
    unsigned long v66;  // 4106
    unsigned int v67;  // s20
    unsigned long v68;  // 4129
    unsigned int v69;  // s21
    unsigned long v70;  // 4129
    unsigned int v71;  // s22
    unsigned long v72;  // 4129
    unsigned int v73;  // s23
    unsigned int v8;  // s6
    unsigned long v74;  // 4129
    unsigned int v75;  // s2
    unsigned int v76;  // s19
    unsigned long v77;  // 4132
    unsigned int v78;  // s7
    unsigned int v79;  // s18
    unsigned long v80;  // 4132
    unsigned int v81;  // s16
    unsigned long long v82;  // cc_dep1
    unsigned int v83;  // s17
    unsigned int v9;  // s1
    unsigned long v84;  // 4132
    unsigned int v85;  // s20
    unsigned long v86;  // 4106
    unsigned long v87;  // 4106
    unsigned int v88;  // s5
    unsigned long long v89;  // cc_dep1
    unsigned long v90;  // 4129
    unsigned long v91;  // 4106

    v1 = v0 * 0x3f000000;
    v3 = v2 * 0x3f000000;
    Matrix4x4__MultiplyPoint3x4();
    Matrix4x4__MultiplyVector(a0, 0);
    v4 = Matrix4x4__MultiplyVector(a0, 0);
    v5 = v1 * 0x3f800000;
    v6 = v1 * 0;
    v7 = v1 * 0;
    v8 = v3 * 0;
    v9 = v3 * 0x3f800000;
    v10 = v3 * 0;
    if (((char)a1 & 1))
    {
        v11 = -(v8);
        v12 = -(v9);
        v13 = ((((CmpF(v8, v11) >> 5 & 3 | CmpF(v8, v11) & 1) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - ((CmpF(v8, v11) >> 5 & 3 | CmpF(v8, v11) & 1) & (CmpF(v8, v11) >> 5 & 3 | CmpF(v8, v11) & 1) >> 1 & 1)) * 0x10000000;
        v14 = -(v10);
        v15 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(v8, v11)) >> 5 & 3 | (unsigned long long)(CmpF(v8, v11) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v8, v11)) >> 5 & 3 | (unsigned long long)(CmpF(v8, v11) & 1)) & ((unsigned long long)(char)(CmpF(v8, v11)) >> 5 & 3 | (unsigned long long)(CmpF(v8, v11) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if ((char)v15)
        {
            v16 = v8;
            v17 = arm64g_calculate_condition(192, v13, 0, 0);
            if (!((char)v17))
                goto LABEL_105191e;
LABEL_105191d:
            v19 = v8;
        }
        else
        {
            v16 = v11;
            v18 = arm64g_calculate_condition(192, v13, 0, 0);
            if ((char)v18)
                goto LABEL_105191d;
LABEL_105191e:
            v19 = v11;
        }
        v20 = v19;
        v21 = ((((CmpF(v9, v12) >> 5 & 3 | CmpF(v9, v12) & 1) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - ((CmpF(v9, v12) >> 5 & 3 | CmpF(v9, v12) & 1) & (CmpF(v9, v12) >> 5 & 3 | CmpF(v9, v12) & 1) >> 1 & 1)) * 0x10000000;
        v22 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(v9, v12)) >> 5 & 3 | (unsigned long long)(CmpF(v9, v12) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v9, v12)) >> 5 & 3 | (unsigned long long)(CmpF(v9, v12) & 1)) & ((unsigned long long)(char)(CmpF(v9, v12)) >> 5 & 3 | (unsigned long long)(CmpF(v9, v12) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if ((char)v22)
        {
            v23 = v9;
            v24 = arm64g_calculate_condition(192, v21, 0, 0);
            if (!((char)v24))
                goto LABEL_105192a;
LABEL_1051929:
            v26 = v9;
        }
        else
        {
            v23 = v12;
            v25 = arm64g_calculate_condition(192, v21, 0, 0);
            if ((char)v25)
                goto LABEL_1051929;
LABEL_105192a:
            v26 = v12;
        }
        v27 = v26;
        v28 = ((((CmpF(v10, v14) >> 5 & 3 | CmpF(v10, v14) & 1) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - ((CmpF(v10, v14) >> 5 & 3 | CmpF(v10, v14) & 1) & (CmpF(v10, v14) >> 5 & 3 | CmpF(v10, v14) & 1) >> 1 & 1)) * 0x10000000;
        v29 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(v10, v14)) >> 5 & 3 | (unsigned long long)(CmpF(v10, v14) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v10, v14)) >> 5 & 3 | (unsigned long long)(CmpF(v10, v14) & 1)) & ((unsigned long long)(char)(CmpF(v10, v14)) >> 5 & 3 | (unsigned long long)(CmpF(v10, v14) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if ((char)v29)
        {
            v30 = v10;
            v31 = arm64g_calculate_condition(192, v28, 0, 0);
            if (!((char)v31))
                goto LABEL_1051936;
LABEL_1051935:
            v33 = v10;
        }
        else
        {
            v30 = v14;
            v32 = arm64g_calculate_condition(192, v28, 0, 0);
            if ((char)v32)
                goto LABEL_1051935;
LABEL_1051936:
            v33 = v14;
        }
        v34 = v33;
        v35 = v7 * 1061494456;
        v36 = v10 * 1061494456;
        v37 = v6 * 1061494456;
        v38 = v9 * 1061494456;
        v39 = v35 + v36;
        v40 = v5 * 1061494456;
        v41 = v8 * 1061494456;
        v42 = v37 + v38;
        v43 = v36 - v35;
        v44 = -(v39);
        v45 = v40 + v41;
        v46 = v38 - v37;
        v47 = -(v42);
        v48 = ((((CmpF(v39, v44) >> 5 & 3 | CmpF(v39, v44) & 1) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - ((CmpF(v39, v44) >> 5 & 3 | CmpF(v39, v44) & 1) & (CmpF(v39, v44) >> 5 & 3 | CmpF(v39, v44) & 1) >> 1 & 1)) * 0x10000000;
        v49 = v41 - v40;
        v50 = -(v45);
        v51 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(v39, v44)) >> 5 & 3 | (unsigned long long)(CmpF(v39, v44) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v39, v44)) >> 5 & 3 | (unsigned long long)(CmpF(v39, v44) & 1)) & ((unsigned long long)(char)(CmpF(v39, v44)) >> 5 & 3 | (unsigned long long)(CmpF(v39, v44) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if ((char)v51)
        {
            v52 = v39;
            v53 = arm64g_calculate_condition(192, v48, 0, 0);
            if (!((char)v53))
                goto LABEL_105197e;
LABEL_105197d:
            v55 = v39;
        }
        else
        {
            v52 = v44;
            v54 = arm64g_calculate_condition(192, v48, 0, 0);
            if ((char)v54)
                goto LABEL_105197d;
LABEL_105197e:
            v55 = v44;
        }
        v56 = ((((CmpF(v42, v47) >> 5 & 3 | CmpF(v42, v47) & 1) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - ((CmpF(v42, v47) >> 5 & 3 | CmpF(v42, v47) & 1) & (CmpF(v42, v47) >> 5 & 3 | CmpF(v42, v47) & 1) >> 1 & 1)) * 0x10000000;
        v57 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(v42, v47)) >> 5 & 3 | (unsigned long long)(CmpF(v42, v47) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v42, v47)) >> 5 & 3 | (unsigned long long)(CmpF(v42, v47) & 1)) & ((unsigned long long)(char)(CmpF(v42, v47)) >> 5 & 3 | (unsigned long long)(CmpF(v42, v47) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if ((char)v57)
        {
            v58 = v42;
            v59 = arm64g_calculate_condition(192, v56, 0, 0);
            if (!((char)v59))
                goto LABEL_105198a;
LABEL_1051989:
            v61 = v42;
        }
        else
        {
            v58 = v47;
            v60 = arm64g_calculate_condition(192, v56, 0, 0);
            if ((char)v60)
                goto LABEL_1051989;
LABEL_105198a:
            v61 = v47;
        }
        v62 = ((((CmpF(v45, v50) >> 5 & 3 | CmpF(v45, v50) & 1) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - ((CmpF(v45, v50) >> 5 & 3 | CmpF(v45, v50) & 1) & (CmpF(v45, v50) >> 5 & 3 | CmpF(v45, v50) & 1) >> 1 & 1)) * 0x10000000;
        v63 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(v45, v50)) >> 5 & 3 | (unsigned long long)(CmpF(v45, v50) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v45, v50)) >> 5 & 3 | (unsigned long long)(CmpF(v45, v50) & 1)) & ((unsigned long long)(char)(CmpF(v45, v50)) >> 5 & 3 | (unsigned long long)(CmpF(v45, v50) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if ((char)v63)
        {
            v64 = v45;
            v65 = arm64g_calculate_condition(192, v62, 0, 0);
            if (!((char)v65))
                goto LABEL_1051996;
LABEL_1051995:
            v67 = v45;
        }
        else
        {
            v64 = v50;
            v66 = arm64g_calculate_condition(192, v62, 0, 0);
            if ((char)v66)
                goto LABEL_1051995;
LABEL_1051996:
            v67 = v50;
        }
        v68 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(v16, v64)) >> 5 & 3 | (unsigned long long)(CmpF(v16, v64) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v16, v64)) >> 5 & 3 | (unsigned long long)(CmpF(v16, v64) & 1)) & ((unsigned long long)(char)(CmpF(v16, v64)) >> 5 & 3 | (unsigned long long)(CmpF(v16, v64) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if ((char)v68)
            v69 = v16;
        else
            v69 = v64;
        v70 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(v23, v58)) >> 5 & 3 | (unsigned long long)(CmpF(v23, v58) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v23, v58)) >> 5 & 3 | (unsigned long long)(CmpF(v23, v58) & 1)) & ((unsigned long long)(char)(CmpF(v23, v58)) >> 5 & 3 | (unsigned long long)(CmpF(v23, v58) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if ((char)v70)
            v71 = v23;
        else
            v71 = v58;
        v72 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(v30, v52)) >> 5 & 3 | (unsigned long long)(CmpF(v30, v52) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v30, v52)) >> 5 & 3 | (unsigned long long)(CmpF(v30, v52) & 1)) & ((unsigned long long)(char)(CmpF(v30, v52)) >> 5 & 3 | (unsigned long long)(CmpF(v30, v52) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if ((char)v72)
            v73 = v30;
        else
            v73 = v52;
        v74 = arm64g_calculate_condition(192, (((((unsigned long long)(char)(CmpF(v20, v67)) >> 5 & 3 | (unsigned long long)(CmpF(v20, v67) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v20, v67)) >> 5 & 3 | (unsigned long long)(CmpF(v20, v67) & 1)) & ((unsigned long long)(char)(CmpF(v20, v67)) >> 5 & 3 | (unsigned long long)(CmpF(v20, v67) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if ((char)v74)
            v75 = v20;
        else
            v75 = v67;
        v76 = -(v7);
        v77 = arm64g_calculate_condition(192, (((((unsigned long long)(char)(CmpF(v27, v61)) >> 5 & 3 | (unsigned long long)(CmpF(v27, v61) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v27, v61)) >> 5 & 3 | (unsigned long long)(CmpF(v27, v61) & 1)) & ((unsigned long long)(char)(CmpF(v27, v61)) >> 5 & 3 | (unsigned long long)(CmpF(v27, v61) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if ((char)v77)
            v78 = v27;
        else
            v78 = v61;
        v79 = -(v6);
        v80 = arm64g_calculate_condition(192, (((((unsigned long long)(char)(CmpF(v34, v55)) >> 5 & 3 | (unsigned long long)(CmpF(v34, v55) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v34, v55)) >> 5 & 3 | (unsigned long long)(CmpF(v34, v55) & 1)) & ((unsigned long long)(char)(CmpF(v34, v55)) >> 5 & 3 | (unsigned long long)(CmpF(v34, v55) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if ((char)v80)
            v81 = v34;
        else
            v81 = v55;
        v82 = ((((CmpF(v7, v76) >> 5 & 3 | CmpF(v7, v76) & 1) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - ((CmpF(v7, v76) >> 5 & 3 | CmpF(v7, v76) & 1) & (CmpF(v7, v76) >> 5 & 3 | CmpF(v7, v76) & 1) >> 1 & 1)) * 0x10000000;
        v83 = -(v5);
        v84 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(v7, v76)) >> 5 & 3 | (unsigned long long)(CmpF(v7, v76) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v7, v76)) >> 5 & 3 | (unsigned long long)(CmpF(v7, v76) & 1)) & ((unsigned long long)(char)(CmpF(v7, v76)) >> 5 & 3 | (unsigned long long)(CmpF(v7, v76) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if ((char)v84)
        {
            v85 = v7;
            v86 = arm64g_calculate_condition(192, v82, 0, 0);
            if (!((char)v86))
                goto LABEL_10519de;
LABEL_10519dd:
            v88 = v7;
        }
        else
        {
            v85 = v76;
            v87 = arm64g_calculate_condition(192, v82, 0, 0);
            if ((char)v87)
                goto LABEL_10519dd;
LABEL_10519de:
            v88 = v76;
        }
        v89 = ((((CmpF(v6, v79) >> 5 & 3 | CmpF(v6, v79) & 1) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - ((CmpF(v6, v79) >> 5 & 3 | CmpF(v6, v79) & 1) & (CmpF(v6, v79) >> 5 & 3 | CmpF(v6, v79) & 1) >> 1 & 1)) * 0x10000000;
        v90 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(v6, v79)) >> 5 & 3 | (unsigned long long)(CmpF(v6, v79) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v6, v79)) >> 5 & 3 | (unsigned long long)(CmpF(v6, v79) & 1)) & ((unsigned long long)(char)(CmpF(v6, v79)) >> 5 & 3 | (unsigned long long)(CmpF(v6, v79) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if ((char)v90)
        {
            v94 = v6;
            v91 = arm64g_calculate_condition(192, v89, 0, 0);
            if (!((char)v91))
                goto LABEL_10519ea;
LABEL_10519e9:
            v93 = v6;
        }
        else
        {
            v94 = v79;
            v92 = arm64g_calculate_condition(192, v89, 0, 0);
            if ((char)v92)
                goto LABEL_10519e9;
LABEL_10519ea:
            v93 = v79;
        }
        v95 = ((((CmpF(v5, v83) >> 5 & 3 | CmpF(v5, v83) & 1) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - ((CmpF(v5, v83) >> 5 & 3 | CmpF(v5, v83) & 1) & (CmpF(v5, v83) >> 5 & 3 | CmpF(v5, v83) & 1) >> 1 & 1)) * 0x10000000;
        v96 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(v5, v83)) >> 5 & 3 | (unsigned long long)(CmpF(v5, v83) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v5, v83)) >> 5 & 3 | (unsigned long long)(CmpF(v5, v83) & 1)) & ((unsigned long long)(char)(CmpF(v5, v83)) >> 5 & 3 | (unsigned long long)(CmpF(v5, v83) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if ((char)v96)
        {
            v97 = v5;
            v98 = arm64g_calculate_condition(192, v95, 0, 0);
            if (!((char)v98))
                goto LABEL_10519f6;
LABEL_10519f5:
            v100 = v5;
        }
        else
        {
            v97 = v83;
            v99 = arm64g_calculate_condition(192, v95, 0, 0);
            if ((char)v99)
                goto LABEL_10519f5;
LABEL_10519f6:
            v100 = v83;
        }
        v101 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(v69, v97)) >> 5 & 3 | (unsigned long long)(CmpF(v69, v97) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v69, v97)) >> 5 & 3 | (unsigned long long)(CmpF(v69, v97) & 1)) & ((unsigned long long)(char)(CmpF(v69, v97)) >> 5 & 3 | (unsigned long long)(CmpF(v69, v97) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if ((char)v101)
            v102 = v69;
        else
            v102 = v97;
        v103 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(v71, v94)) >> 5 & 3 | (unsigned long long)(CmpF(v71, v94) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v71, v94)) >> 5 & 3 | (unsigned long long)(CmpF(v71, v94) & 1)) & ((unsigned long long)(char)(CmpF(v71, v94)) >> 5 & 3 | (unsigned long long)(CmpF(v71, v94) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if ((char)v103)
            v104 = v71;
        else
            v104 = v94;
        v105 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(v73, v85)) >> 5 & 3 | (unsigned long long)(CmpF(v73, v85) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v73, v85)) >> 5 & 3 | (unsigned long long)(CmpF(v73, v85) & 1)) & ((unsigned long long)(char)(CmpF(v73, v85)) >> 5 & 3 | (unsigned long long)(CmpF(v73, v85) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if ((char)v105)
            v106 = v73;
        else
            v106 = v85;
        v107 = arm64g_calculate_condition(192, (((((unsigned long long)(char)(CmpF(v75, v100)) >> 5 & 3 | (unsigned long long)(CmpF(v75, v100) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v75, v100)) >> 5 & 3 | (unsigned long long)(CmpF(v75, v100) & 1)) & ((unsigned long long)(char)(CmpF(v75, v100)) >> 5 & 3 | (unsigned long long)(CmpF(v75, v100) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if ((char)v107)
            v108 = v75;
        else
            v108 = v100;
        v109 = -(v43);
        v110 = arm64g_calculate_condition(192, (((((unsigned long long)(char)(CmpF(v78, v93)) >> 5 & 3 | (unsigned long long)(CmpF(v78, v93) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v78, v93)) >> 5 & 3 | (unsigned long long)(CmpF(v78, v93) & 1)) & ((unsigned long long)(char)(CmpF(v78, v93)) >> 5 & 3 | (unsigned long long)(CmpF(v78, v93) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if ((char)v110)
            v111 = v78;
        else
            v111 = v93;
        v112 = -(v46);
        v113 = arm64g_calculate_condition(192, (((((unsigned long long)(char)(CmpF(v81, v88)) >> 5 & 3 | (unsigned long long)(CmpF(v81, v88) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v81, v88)) >> 5 & 3 | (unsigned long long)(CmpF(v81, v88) & 1)) & ((unsigned long long)(char)(CmpF(v81, v88)) >> 5 & 3 | (unsigned long long)(CmpF(v81, v88) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if ((char)v113)
            v114 = v81;
        else
            v114 = v88;
        v115 = ((((CmpF(v43, v109) >> 5 & 3 | CmpF(v43, v109) & 1) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - ((CmpF(v43, v109) >> 5 & 3 | CmpF(v43, v109) & 1) & (CmpF(v43, v109) >> 5 & 3 | CmpF(v43, v109) & 1) >> 1 & 1)) * 0x10000000;
        v116 = -(v49);
        v117 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(v43, v109)) >> 5 & 3 | (unsigned long long)(CmpF(v43, v109) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v43, v109)) >> 5 & 3 | (unsigned long long)(CmpF(v43, v109) & 1)) & ((unsigned long long)(char)(CmpF(v43, v109)) >> 5 & 3 | (unsigned long long)(CmpF(v43, v109) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if ((char)v117)
        {
            v118 = v43;
            v119 = arm64g_calculate_condition(192, v115, 0, 0);
            if (!((char)v119))
                goto LABEL_1051a3e;
LABEL_1051a3d:
            v121 = v43;
        }
        else
        {
            v118 = v109;
            v120 = arm64g_calculate_condition(192, v115, 0, 0);
            if ((char)v120)
                goto LABEL_1051a3d;
LABEL_1051a3e:
            v121 = v109;
        }
        v122 = ((((CmpF(v46, v112) >> 5 & 3 | CmpF(v46, v112) & 1) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - ((CmpF(v46, v112) >> 5 & 3 | CmpF(v46, v112) & 1) & (CmpF(v46, v112) >> 5 & 3 | CmpF(v46, v112) & 1) >> 1 & 1)) * 0x10000000;
        v123 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(v46, v112)) >> 5 & 3 | (unsigned long long)(CmpF(v46, v112) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v46, v112)) >> 5 & 3 | (unsigned long long)(CmpF(v46, v112) & 1)) & ((unsigned long long)(char)(CmpF(v46, v112)) >> 5 & 3 | (unsigned long long)(CmpF(v46, v112) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if ((char)v123)
        {
            v124 = v46;
            v125 = arm64g_calculate_condition(192, v122, 0, 0);
            if (!((char)v125))
                goto LABEL_1051a4a;
LABEL_1051a49:
            v127 = v46;
        }
        else
        {
            v124 = v112;
            v126 = arm64g_calculate_condition(192, v122, 0, 0);
            if ((char)v126)
                goto LABEL_1051a49;
LABEL_1051a4a:
            v127 = v112;
        }
        v128 = ((((CmpF(v49, v116) >> 5 & 3 | CmpF(v49, v116) & 1) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - ((CmpF(v49, v116) >> 5 & 3 | CmpF(v49, v116) & 1) & (CmpF(v49, v116) >> 5 & 3 | CmpF(v49, v116) & 1) >> 1 & 1)) * 0x10000000;
        v129 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(v49, v116)) >> 5 & 3 | (unsigned long long)(CmpF(v49, v116) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v49, v116)) >> 5 & 3 | (unsigned long long)(CmpF(v49, v116) & 1)) & ((unsigned long long)(char)(CmpF(v49, v116)) >> 5 & 3 | (unsigned long long)(CmpF(v49, v116) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if ((char)v129)
        {
            v130 = v49;
            v131 = arm64g_calculate_condition(192, v128, 0, 0);
            if (!((char)v131))
                goto LABEL_1051a56;
LABEL_1051a55:
            v133 = v49;
        }
        else
        {
            v130 = v116;
            v132 = arm64g_calculate_condition(192, v128, 0, 0);
            if ((char)v132)
                goto LABEL_1051a55;
LABEL_1051a56:
            v133 = v116;
        }
        v134 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(v102, v130)) >> 5 & 3 | (unsigned long long)(CmpF(v102, v130) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v102, v130)) >> 5 & 3 | (unsigned long long)(CmpF(v102, v130) & 1)) & ((unsigned long long)(char)(CmpF(v102, v130)) >> 5 & 3 | (unsigned long long)(CmpF(v102, v130) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if ((char)v134)
            v135 = v102;
        else
            v135 = v130;
        v136 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(v104, v124)) >> 5 & 3 | (unsigned long long)(CmpF(v104, v124) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v104, v124)) >> 5 & 3 | (unsigned long long)(CmpF(v104, v124) & 1)) & ((unsigned long long)(char)(CmpF(v104, v124)) >> 5 & 3 | (unsigned long long)(CmpF(v104, v124) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if ((char)v136)
            v137 = v104;
        else
            v137 = v124;
        v138 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(v106, v118)) >> 5 & 3 | (unsigned long long)(CmpF(v106, v118) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v106, v118)) >> 5 & 3 | (unsigned long long)(CmpF(v106, v118) & 1)) & ((unsigned long long)(char)(CmpF(v106, v118)) >> 5 & 3 | (unsigned long long)(CmpF(v106, v118) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if ((char)v138)
            v139 = v106;
        else
            v139 = v118;
        v140 = arm64g_calculate_condition(192, (((((unsigned long long)(char)(CmpF(v108, v133)) >> 5 & 3 | (unsigned long long)(CmpF(v108, v133) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v108, v133)) >> 5 & 3 | (unsigned long long)(CmpF(v108, v133) & 1)) & ((unsigned long long)(char)(CmpF(v108, v133)) >> 5 & 3 | (unsigned long long)(CmpF(v108, v133) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if ((char)v140)
            v141 = v108;
        else
            v141 = v133;
        v142 = arm64g_calculate_condition(192, (((((unsigned long long)(char)(CmpF(v111, v127)) >> 5 & 3 | (unsigned long long)(CmpF(v111, v127) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v111, v127)) >> 5 & 3 | (unsigned long long)(CmpF(v111, v127) & 1)) & ((unsigned long long)(char)(CmpF(v111, v127)) >> 5 & 3 | (unsigned long long)(CmpF(v111, v127) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if ((char)v142)
            v143 = v111;
        else
            v143 = v127;
        v144 = arm64g_calculate_condition(192, (((((unsigned long long)(char)(CmpF(v114, v121)) >> 5 & 3 | (unsigned long long)(CmpF(v114, v121) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v114, v121)) >> 5 & 3 | (unsigned long long)(CmpF(v114, v121) & 1)) & ((unsigned long long)(char)(CmpF(v114, v121)) >> 5 & 3 | (unsigned long long)(CmpF(v114, v121) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if ((char)v144)
            v145 = v114;
        else
            v145 = v121;
    }
    else
    {
        v146 = v5 + v8;
        v147 = v6 + v9;
        v148 = v6 - v9;
        v149 = -(v146);
        v150 = v7 + v10;
        v151 = v7 - v10;
        v152 = -(v147);
        v153 = ((((CmpF(v146, v149) >> 5 & 3 | CmpF(v146, v149) & 1) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - ((CmpF(v146, v149) >> 5 & 3 | CmpF(v146, v149) & 1) & (CmpF(v146, v149) >> 5 & 3 | CmpF(v146, v149) & 1) >> 1 & 1)) * 0x10000000;
        v154 = v5 - v8;
        v155 = -(v150);
        v156 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(v146, v149)) >> 5 & 3 | (unsigned long long)(CmpF(v146, v149) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v146, v149)) >> 5 & 3 | (unsigned long long)(CmpF(v146, v149) & 1)) & ((unsigned long long)(char)(CmpF(v146, v149)) >> 5 & 3 | (unsigned long long)(CmpF(v146, v149) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if ((char)v156)
        {
            v157 = v146;
            v158 = arm64g_calculate_condition(192, v153, 0, 0);
            if (!((char)v158))
                goto LABEL_1051aba;
LABEL_1051ab9:
            v160 = v146;
        }
        else
        {
            v157 = v149;
            v159 = arm64g_calculate_condition(192, v153, 0, 0);
            if ((char)v159)
                goto LABEL_1051ab9;
LABEL_1051aba:
            v160 = v149;
        }
        v161 = ((((CmpF(v147, v152) >> 5 & 3 | CmpF(v147, v152) & 1) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - ((CmpF(v147, v152) >> 5 & 3 | CmpF(v147, v152) & 1) & (CmpF(v147, v152) >> 5 & 3 | CmpF(v147, v152) & 1) >> 1 & 1)) * 0x10000000;
        v162 = -(v151);
        v163 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(v147, v152)) >> 5 & 3 | (unsigned long long)(CmpF(v147, v152) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v147, v152)) >> 5 & 3 | (unsigned long long)(CmpF(v147, v152) & 1)) & ((unsigned long long)(char)(CmpF(v147, v152)) >> 5 & 3 | (unsigned long long)(CmpF(v147, v152) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if ((char)v163)
        {
            v164 = v147;
            v165 = arm64g_calculate_condition(192, v161, 0, 0);
            if (!((char)v165))
                goto LABEL_1051aca;
LABEL_1051ac9:
            v167 = v147;
        }
        else
        {
            v164 = v152;
            v166 = arm64g_calculate_condition(192, v161, 0, 0);
            if ((char)v166)
                goto LABEL_1051ac9;
LABEL_1051aca:
            v167 = v152;
        }
        v168 = ((((CmpF(v150, v155) >> 5 & 3 | CmpF(v150, v155) & 1) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - ((CmpF(v150, v155) >> 5 & 3 | CmpF(v150, v155) & 1) & (CmpF(v150, v155) >> 5 & 3 | CmpF(v150, v155) & 1) >> 1 & 1)) * 0x10000000;
        v169 = -(v148);
        v170 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(v150, v155)) >> 5 & 3 | (unsigned long long)(CmpF(v150, v155) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v150, v155)) >> 5 & 3 | (unsigned long long)(CmpF(v150, v155) & 1)) & ((unsigned long long)(char)(CmpF(v150, v155)) >> 5 & 3 | (unsigned long long)(CmpF(v150, v155) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if ((char)v170)
        {
            v171 = v150;
            v172 = arm64g_calculate_condition(192, v168, 0, 0);
            if (!((char)v172))
                goto LABEL_1051ada;
LABEL_1051ad9:
            v174 = v150;
        }
        else
        {
            v171 = v155;
            v173 = arm64g_calculate_condition(192, v168, 0, 0);
            if ((char)v173)
                goto LABEL_1051ad9;
LABEL_1051ada:
            v174 = v155;
        }
        v175 = ((((CmpF(v151, v162) >> 5 & 3 | CmpF(v151, v162) & 1) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - ((CmpF(v151, v162) >> 5 & 3 | CmpF(v151, v162) & 1) & (CmpF(v151, v162) >> 5 & 3 | CmpF(v151, v162) & 1) >> 1 & 1)) * 0x10000000;
        v176 = -(v154);
        v177 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(v151, v162)) >> 5 & 3 | (unsigned long long)(CmpF(v151, v162) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v151, v162)) >> 5 & 3 | (unsigned long long)(CmpF(v151, v162) & 1)) & ((unsigned long long)(char)(CmpF(v151, v162)) >> 5 & 3 | (unsigned long long)(CmpF(v151, v162) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if ((char)v177)
        {
            v178 = v151;
            v179 = arm64g_calculate_condition(192, v175, 0, 0);
            if (!((char)v179))
                goto LABEL_1051aea;
LABEL_1051ae9:
            v181 = v151;
        }
        else
        {
            v178 = v162;
            v180 = arm64g_calculate_condition(192, v175, 0, 0);
            if ((char)v180)
                goto LABEL_1051ae9;
LABEL_1051aea:
            v181 = v162;
        }
        v182 = ((((CmpF(v148, v169) >> 5 & 3 | CmpF(v148, v169) & 1) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - ((CmpF(v148, v169) >> 5 & 3 | CmpF(v148, v169) & 1) & (CmpF(v148, v169) >> 5 & 3 | CmpF(v148, v169) & 1) >> 1 & 1)) * 0x10000000;
        v183 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(v148, v169)) >> 5 & 3 | (unsigned long long)(CmpF(v148, v169) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v148, v169)) >> 5 & 3 | (unsigned long long)(CmpF(v148, v169) & 1)) & ((unsigned long long)(char)(CmpF(v148, v169)) >> 5 & 3 | (unsigned long long)(CmpF(v148, v169) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if ((char)v183)
        {
            v184 = v148;
            v185 = arm64g_calculate_condition(192, v182, 0, 0);
            if (!((char)v185))
                goto LABEL_1051af6;
LABEL_1051af5:
            v187 = v148;
        }
        else
        {
            v184 = v169;
            v186 = arm64g_calculate_condition(192, v182, 0, 0);
            if ((char)v186)
                goto LABEL_1051af5;
LABEL_1051af6:
            v187 = v169;
        }
        v188 = ((((CmpF(v154, v176) >> 5 & 3 | CmpF(v154, v176) & 1) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - ((CmpF(v154, v176) >> 5 & 3 | CmpF(v154, v176) & 1) & (CmpF(v154, v176) >> 5 & 3 | CmpF(v154, v176) & 1) >> 1 & 1)) * 0x10000000;
        v189 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(v154, v176)) >> 5 & 3 | (unsigned long long)(CmpF(v154, v176) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v154, v176)) >> 5 & 3 | (unsigned long long)(CmpF(v154, v176) & 1)) & ((unsigned long long)(char)(CmpF(v154, v176)) >> 5 & 3 | (unsigned long long)(CmpF(v154, v176) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if ((char)v189)
        {
            v190 = v154;
            v191 = arm64g_calculate_condition(192, v188, 0, 0);
            if (!((char)v191))
                goto LABEL_1051b02;
LABEL_1051b01:
            v193 = v154;
        }
        else
        {
            v190 = v176;
            v192 = arm64g_calculate_condition(192, v188, 0, 0);
            if ((char)v192)
                goto LABEL_1051b01;
LABEL_1051b02:
            v193 = v176;
        }
        v194 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(v157, v190)) >> 5 & 3 | (unsigned long long)(CmpF(v157, v190) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v157, v190)) >> 5 & 3 | (unsigned long long)(CmpF(v157, v190) & 1)) & ((unsigned long long)(char)(CmpF(v157, v190)) >> 5 & 3 | (unsigned long long)(CmpF(v157, v190) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if ((char)v194)
            v135 = v157;
        else
            v135 = v190;
        v195 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(v164, v184)) >> 5 & 3 | (unsigned long long)(CmpF(v164, v184) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v164, v184)) >> 5 & 3 | (unsigned long long)(CmpF(v164, v184) & 1)) & ((unsigned long long)(char)(CmpF(v164, v184)) >> 5 & 3 | (unsigned long long)(CmpF(v164, v184) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if ((char)v195)
            v137 = v164;
        else
            v137 = v184;
        v196 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(v171, v178)) >> 5 & 3 | (unsigned long long)(CmpF(v171, v178) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v171, v178)) >> 5 & 3 | (unsigned long long)(CmpF(v171, v178) & 1)) & ((unsigned long long)(char)(CmpF(v171, v178)) >> 5 & 3 | (unsigned long long)(CmpF(v171, v178) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if ((char)v196)
            v139 = v171;
        else
            v139 = v178;
        v197 = arm64g_calculate_condition(192, (((((unsigned long long)(char)(CmpF(v160, v193)) >> 5 & 3 | (unsigned long long)(CmpF(v160, v193) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v160, v193)) >> 5 & 3 | (unsigned long long)(CmpF(v160, v193) & 1)) & ((unsigned long long)(char)(CmpF(v160, v193)) >> 5 & 3 | (unsigned long long)(CmpF(v160, v193) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if ((char)v197)
            v141 = v160;
        else
            v141 = v193;
        v198 = arm64g_calculate_condition(192, (((((unsigned long long)(char)(CmpF(v167, v187)) >> 5 & 3 | (unsigned long long)(CmpF(v167, v187) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v167, v187)) >> 5 & 3 | (unsigned long long)(CmpF(v167, v187) & 1)) & ((unsigned long long)(char)(CmpF(v167, v187)) >> 5 & 3 | (unsigned long long)(CmpF(v167, v187) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if ((char)v198)
            v143 = v167;
        else
            v143 = v187;
        v199 = arm64g_calculate_condition(192, (((((unsigned long long)(char)(CmpF(v174, v181)) >> 5 & 3 | (unsigned long long)(CmpF(v174, v181) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v174, v181)) >> 5 & 3 | (unsigned long long)(CmpF(v174, v181) & 1)) & ((unsigned long long)(char)(CmpF(v174, v181)) >> 5 & 3 | (unsigned long long)(CmpF(v174, v181) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if ((char)v199)
            v145 = v174;
        else
            v145 = v181;
    }
    ptr[0] = v201 + v1 + (v141 + v135) * 0x3f000000;
    ptr[1] = v202 + v3 + (v143 + v137) * 0x3f000000;
    ptr[2] = 0 + (v145 + v139) * 0x3f000000;
    ptr[3] = (v141 - v135) * 0x3f000000;
    ptr[4] = (v143 - v137) * 0x3f000000;
    ptr[5] = (v145 - v139) * 0x3f000000;
    return v4;
}
```

## `CFUtils.ClampInsideUnitCircle` — RVA `0xc51fc4`

- Decompiled symbol: `CFUtils_ClampInsideUnitCircle`
- Metadata signature: `public static Vector2 ClampInsideUnitCircle(Vector2 np) { }`
- Native interval: `208` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[224];
    unsigned int field_e0;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern long long g_1ef22b8;
extern char g_1fab1e0;
extern char g_1fab243;

struct_1 * CFUtils_ClampInsideUnitCircle(void)
{
    unsigned int v0;  // s0
    unsigned int v1;  // s1
    unsigned long v3;  // 4191
    struct_0 *v4;  // x0
    unsigned int v5;  // s0
    unsigned long v6;  // 4140
    struct_1 *v7;  // x0

    v3 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(v0 * v0 + v1 * v1, 0x3f800000)) >> 5 & 3 | (unsigned long long)(CmpF(v0 * v0 + v1 * v1, 0x3f800000) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v0 * v0 + v1 * v1, 0x3f800000)) >> 5 & 3 | (unsigned long long)(CmpF(v0 * v0 + v1 * v1, 0x3f800000) & 1)) & ((unsigned long long)(char)(CmpF(v0 * v0 + v1 * v1, 0x3f800000)) >> 5 & 3 | (unsigned long long)(CmpF(v0 * v0 + v1 * v1, 0x3f800000) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if ((char)v3)
        return v7;
    if (!g_1fab243)
    {
        sub_f7d92c("_F");
        g_1fab243 = 1;
    }
    v4 = g_1ef07e8;
    if (!g_1ef07e8->field_e0)
        v4 = sub_f7da5c(g_1ef07e8);
    v5 = [D] unsupported_Iop_SqrtF32();
    v6 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v5, 925353388)) >> 5 & 3 | (unsigned long long)(CmpF(v5, 925353388) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v5, 925353388)) >> 5 & 3 | (unsigned long long)(CmpF(v5, 925353388) & 1)) & ((unsigned long long)(char)(CmpF(v5, 925353388)) >> 5 & 3 | (unsigned long long)(CmpF(v5, 925353388) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if (!((char)v6))
        return v4;
    if (!g_1fab1e0)
    {
        v4 = sub_f7d92c(&g_1ef22b8);
        g_1fab1e0 = 1;
    }
    return v4;
}
```

## `CFUtils.ClampInsideUnitSquare` — RVA `0xc52094`

- Decompiled symbol: `CFUtils_ClampInsideUnitSquare`
- Metadata signature: `public static Vector2 ClampInsideUnitSquare(Vector2 np) { }`
- Native interval: `104` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: Decompiler produced no C-like text

```c
// 0x1052094: fmov s2, #1.00000000
// 0x1052098: fcmp s0, s2
// 0x105209c: b.gt #0x10520ac
// 0x10520a0: fmov s3, #-1.00000000
// 0x10520a4: fcmp s0, s3
// 0x10520a8: b.pl #0x10520b8
// 0x10520ac: fmov s2, #1.00000000
// 0x10520b0: fdiv s2, s2, s0
// 0x10520b4: fabs s2, s2
// 0x10520b8: fmov s3, #1.00000000
// 0x10520bc: fcmp s1, s3
// 0x10520c0: b.gt #0x10520d0
// 0x10520c4: fmov s4, #-1.00000000
// 0x10520c8: fcmp s1, s4
// 0x10520cc: b.pl #0x10520e0
// 0x10520d0: fdiv s3, s3, s1
// 0x10520d4: fabs s3, s3
// 0x10520d8: fcmp s2, s3
// 0x10520dc: fcsel s2, s2, s3, mi
// 0x10520e0: fmov s5, #1.00000000
// 0x10520e4: fmul s3, s0, s2
// 0x10520e8: fmul s4, s1, s2
// 0x10520ec: fcmp s2, s5
// 0x10520f0: fcsel s0, s3, s0, mi
// 0x10520f4: fcsel s1, s4, s1, mi
// 0x10520f8: ret
```

## `CFUtils.ChangeMatrixTranl` — RVA `0xc52424`

- Decompiled symbol: `CFUtils_ChangeMatrixTranl`
- Metadata signature: `public static Matrix4x4 ChangeMatrixTranl(Matrix4x4 m, Vector3 newTransl) { }`
- Native interval: `60` bytes
- Result: `pseudocode`

```c
void CFUtils_ChangeMatrixTranl(uint128_t *p)
{
    uint128_t v0;  // q0
    uint128_t v1;  // q3
    uint128_t v2;  // q2
    uint128_t ptr[4];  // x8

    Matrix4x4__SetColumn();
    v0 = p[3];
    v1 = *(p);
    v2 = p[1];
    ptr[2] = p[2];
    ptr[3] = v0;
    ptr[0] = v1;
    ptr[1] = v2;
    return;
}
```

## `CFUtils.TransformRect` — RVA `0xc52460`

- Decompiled symbol: `CFUtils_TransformRect`
- Metadata signature: `public static Rect TransformRect(Rect r, Matrix4x4 tr, bool round) { }`
- Native interval: `76` bytes
- Result: `pseudocode`

```c
unsigned long long CFUtils_TransformRect(uint128_t *ptr, unsigned int a1)
{
    unsigned long long v4;  // x0
    int v0;  // [bp-0x70]
    int v1;  // [bp-0x60]
    int v2;  // [bp-0x50]
    int v3;  // [bp-0x40]

    v2 = (int)ptr[2];
    v3 = (int)ptr[3];
    v0 = (int)*(ptr);
    v1 = (int)ptr[1];
    v4 = CFUtils__TransformRectAsBounds(&v0, a1 & 1);
    return CFUtils__TransformRectAsBounds(&v0, a1 & 1);
}
```

## `CFUtils.ClampRectInside` — RVA `0xc524ac`

- Decompiled symbol: `CFUtils_ClampRectInside`
- Metadata signature: `public static Vector2 ClampRectInside(Rect rect, bool rectIsRound, Rect limiterRect, bool limiterIsRound) { }`
- Native interval: `12` bytes
- Result: `pseudocode`

```c
long long CFUtils_ClampRectInside(unsigned long a0, unsigned long a1)
{
    unsigned long long v0;  // x0
    unsigned long long v1;  // x0

    if (!((char)a1 & 1))
    {
        v1 = CFUtils__ClampRectInsideRect();
        return CFUtils__ClampRectInsideRect();
    }
    v0 = CFUtils__ClampEllipseInsideEllipse();
    return CFUtils__ClampEllipseInsideEllipse();
}
```

## `CFUtils.ClampInsideRect` — RVA `0xc52ca4`

- Decompiled symbol: `CFUtils_ClampInsideRect`
- Metadata signature: `public static Vector2 ClampInsideRect(Vector2 v, Rect r) { }`
- Native interval: `160` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: Decompiler produced no C-like text

```c
// 0x1052ca4: fadd s6, s3, s5
// 0x1052ca8: fcmp s1, s6
// 0x1052cac: b.pl #0x1052cd0
// 0x1052cb0: fcmp s1, s3
// 0x1052cb4: b.lt #0x1052cd0
// 0x1052cb8: fcmp s0, s2
// 0x1052cbc: b.lt #0x1052cd0
// 0x1052cc0: fadd s6, s2, s4
// 0x1052cc4: fcmp s0, s6
// 0x1052cc8: b.pl #0x1052cd0
// 0x1052ccc: ret
// 0x1052cd0: fmov s16, #0.50000000
// 0x1052cd4: fmul s7, s4, s16
// 0x1052cd8: fmul s6, s5, s16
// 0x1052cdc: fadd s5, s2, s7
// 0x1052ce0: fadd s2, s3, s6
// 0x1052ce4: fsub s0, s0, s5
// 0x1052ce8: fcmp s0, s7
// 0x1052cec: fsub s1, s1, s2
// 0x1052cf0: b.gt #0x1052d04
// 0x1052cf4: fnmul s3, s4, s16
// 0x1052cf8: fcmp s0, s3
// 0x1052cfc: fmov s3, #1.00000000
// 0x1052d00: b.pl #0x1052d0c
// 0x1052d04: fdiv s3, s7, s0
// 0x1052d08: fabs s3, s3
// 0x1052d0c: fcmp s1, s6
// 0x1052d10: b.gt #0x1052d20
// 0x1052d14: fneg s4, s6
// 0x1052d18: fcmp s1, s4
// 0x1052d1c: b.pl #0x1052d30
// 0x1052d20: fdiv s4, s6, s1
// 0x1052d24: fabs s4, s4
// 0x1052d28: fcmp s3, s4
// 0x1052d2c: fcsel s3, s3, s4, mi
// 0x1052d30: fmul s0, s0, s3
// 0x1052d34: fmul s1, s1, s3
// 0x1052d38: fadd s0, s5, s0
// 0x1052d3c: fadd s1, s2, s1
// 0x1052d40: ret
```

## `CFUtils.SmartDeltaAngle` — RVA `0xc57458`

- Decompiled symbol: `CFUtils_SmartDeltaAngle`
- Metadata signature: `public static float SmartDeltaAngle(float startAngle, float curAngle, float lastDelta) { }`
- Native interval: `84` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: Decompiler produced no C-like text

```c
// 0x1057458: mov w8, #0x43b40000
// 0x105745c: fadd s0, s0, s2
// 0x1057460: fmov s3, w8
// 0x1057464: fsub s0, s1, s0
// 0x1057468: mov w8, #-0x3c4c0000
// 0x105746c: fdiv s4, s0, s3
// 0x1057470: fmov s1, w8
// 0x1057474: frintm s4, s4
// 0x1057478: fmul s4, s4, s1
// 0x105747c: fadd s0, s0, s4
// 0x1057480: fmov s4, wzr
// 0x1057484: mov w8, #0x43340000
// 0x1057488: fmin s3, s0, s3
// 0x105748c: fcmp s0, #0.0
// 0x1057490: fmov s0, w8
// 0x1057494: fcsel s3, s3, s4, pl
// 0x1057498: fadd s1, s3, s1
// 0x105749c: fcmp s3, s0
// 0x10574a0: fcsel s0, s1, s3, gt
// 0x10574a4: fadd s0, s0, s2
// 0x10574a8: ret
```

## `CFUtils.MoveTowards` — RVA `0xc574ac`

- Decompiled symbol: `CFUtils_MoveTowards`
- Metadata signature: `public static float MoveTowards(float a, float b, float secondsPerUnit, float deltaTime, float epsilon) { }`
- Native interval: `76` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: Decompiler produced no C-like text

```c
// 0x10574ac: fcmp s2, s3
// 0x10574b0: b.ls #0x10574f0
// 0x10574b4: adrp x8, #0x832000
// 0x10574b8: ldr s5, [x8, #0x534]
// 0x10574bc: fcmp s2, s5
// 0x10574c0: b.mi #0x10574f0
// 0x10574c4: fabd s5, s1, s0
// 0x10574c8: fcmp s5, s4
// 0x10574cc: b.ls #0x10574f0
// 0x10574d0: fsub s4, s1, s0
// 0x10574d4: fdiv s2, s3, s2
// 0x10574d8: fneg s3, s2
// 0x10574dc: fcmp s4, #0.0
// 0x10574e0: fcsel s3, s2, s3, ge
// 0x10574e4: fadd s0, s3, s0
// 0x10574e8: fcmp s5, s2
// 0x10574ec: fcsel s1, s0, s1, hi
// 0x10574f0: mov v0.16b, v1.16b
// 0x10574f4: ret
```

## `CFUtils.get_realDeltaTimeClamped` — RVA `0xc5834c`

- Decompiled symbol: `CFUtils_get_realDeltaTimeClamped`
- Metadata signature: `public static float get_realDeltaTimeClamped() { }`
- Native interval: `24` bytes
- Result: `pseudocode`

```c
int CFUtils_get_realDeltaTimeClamped(void)
{
    return CFUtils__get_realDeltaTime();
}
```

## `CFUtils.get_editorStopped` — RVA `0xc58364`

- Decompiled symbol: `CFUtils_get_editorStopped`
- Metadata signature: `public static bool get_editorStopped() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
unsigned int CFUtils_get_editorStopped(void)
{
    return 0;
}
```

## `CFUtils.get_forcedMobileModeEnabled` — RVA `0xc5836c`

- Decompiled symbol: `CFUtils_get_forcedMobileModeEnabled`
- Metadata signature: `public static bool get_forcedMobileModeEnabled() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
unsigned int CFUtils_get_forcedMobileModeEnabled(void)
{
    return 1;
}
```

## `CFUtils.LogPrefixFull` — RVA `0xc58374`

- Decompiled symbol: `CFUtils_LogPrefixFull`
- Metadata signature: `public static string LogPrefixFull() { }`
- Native interval: `136` bytes
- Result: `pseudocode`

```c
extern long long g_1f100c8;
extern char g_1fab297;

long long CFUtils_LogPrefixFull(void)
{
    long long v1;  // x0
    unsigned long long v2;  // x0
    unsigned int v0;  // [bp-0x24]

    if (!(g_1fab297 & 1))
    {
        sub_f7d92c(&g_1f100c8);
        sub_f7d92c("3'");
        g_1fab297 = 1;
    }
    v0 = Time__get_frameCount(0);
    v1 = Int32__ToString(&v0, 0);
    v2 = String__Concat(g_1f0feb8, v1, g_1f100c8, 0);
    return String__Concat(g_1f0feb8, v1, g_1f100c8, 0);
}
```

## `CFUtils.LogPrefix` — RVA `0xc583fc`

- Decompiled symbol: `CFUtils_LogPrefix`
- Metadata signature: `public static string LogPrefix() { }`
- Native interval: `136` bytes
- Result: `pseudocode`

```c
extern long long g_1f100c8;
extern char g_1fab298;

long long CFUtils_LogPrefix(void)
{
    long long v1;  // x0
    unsigned long long v2;  // x0
    unsigned int v0;  // [bp-0x24]

    if (!(g_1fab298 & 1))
    {
        sub_f7d92c(&g_1f100c8);
        sub_f7d92c("3'");
        g_1fab298 = 1;
    }
    v0 = Time__get_frameCount(0);
    v1 = Int32__ToString(&v0, 0);
    v2 = String__Concat(g_1f0feb8, v1, g_1f100c8, 0);
    return String__Concat(g_1f0feb8, v1, g_1f100c8, 0);
}
```

## `CFUtils.ApplyDeltaInput` — RVA `0xc58484`

- Decompiled symbol: `CFUtils_ApplyDeltaInput`
- Metadata signature: `public static float ApplyDeltaInput(float accum, float delta) { }`
- Native interval: `64` bytes
- Result: `pseudocode`

```c
long long CFUtils_ApplyDeltaInput(void)
{
    unsigned int v0;  // s0
    unsigned long v1;  // 4125
    unsigned long v10;  // x0
    unsigned long v11;  // x0
    unsigned long v12;  // x0
    unsigned long v13;  // x0
    unsigned int v2;  // s1
    unsigned long v3;  // 4125
    unsigned long v4;  // 4129
    unsigned long v5;  // x0
    unsigned long v6;  // x0
    unsigned long v7;  // 4125
    unsigned long v8;  // 4125
    unsigned long v9;  // 4129

    v1 = arm64g_calculate_condition(176, (((((unsigned long long)(char)(CmpF(v0, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v0, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v0, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v0, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v0, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v0, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if (!((char)v1))
    {
        v3 = arm64g_calculate_condition(176, (((((unsigned long long)(char)(CmpF(v2, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v2, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v2, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v2, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v2, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v2, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if (!((char)v3))
        {
            v4 = arm64g_calculate_condition(192, (((((unsigned long long)(char)(CmpF(v0, v2)) >> 5 & 3 | (unsigned long long)(CmpF(v0, v2) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v0, v2)) >> 5 & 3 | (unsigned long long)(CmpF(v0, v2) & 1)) & ((unsigned long long)(char)(CmpF(v0, v2)) >> 5 & 3 | (unsigned long long)(CmpF(v0, v2) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
            if (!((char)v4))
                return v6;
            return v5;
        }
    }
    v7 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v0, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v0, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v0, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v0, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v0, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v0, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if ((char)v7)
        return v13;
    v8 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v2, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v2, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v2, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v2, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v2, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v2, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if ((char)v8)
        return v12;
    v9 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(v0, v2)) >> 5 & 3 | (unsigned long long)(CmpF(v0, v2) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v0, v2)) >> 5 & 3 | (unsigned long long)(CmpF(v0, v2) & 1)) & ((unsigned long long)(char)(CmpF(v0, v2)) >> 5 & 3 | (unsigned long long)(CmpF(v0, v2) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if (!((char)v9))
        return v11;
    return v10;
}
```

## `CFUtils.ApplyDeltaInputInt` — RVA `0xc584c4`

- Decompiled symbol: `CFUtils_ApplyDeltaInputInt`
- Metadata signature: `public static int ApplyDeltaInputInt(int accum, int delta) { }`
- Native interval: `48` bytes
- Result: `pseudocode`

```c
unsigned long long CFUtils_ApplyDeltaInputInt(unsigned long a0, unsigned long a1)
{
    unsigned long v0;  // 4113

    if (((char)(((unsigned int)a1 | (unsigned int)a0) >> 31) & 1))
    {
        v0 = arm64g_calculate_condition(185, (unsigned long long)((unsigned int)a1 & (unsigned int)a0), 0, 0);
        if (!((char)v0))
            return a1 + a0;
        if ((unsigned int)a0 < (unsigned int)a1)
            return a0 & 4294967295;
        return a1 & 4294967295;
    }
    else if ((unsigned int)a1 < (unsigned int)a0)
    {
        return a0 & 4294967295;
    }
    else
    {
        return a1 & 4294967295;
    }
}
```

## `CFUtils.ApplyPositveDeltaInput` — RVA `0xc584f4`

- Decompiled symbol: `CFUtils_ApplyPositveDeltaInput`
- Metadata signature: `public static float ApplyPositveDeltaInput(float positiveAccum, float delta) { }`
- Native interval: `20` bytes
- Result: `pseudocode`

```c
long long CFUtils_ApplyPositveDeltaInput(void)
{
    unsigned int v0;  // s1
    unsigned int v1;  // s0
    unsigned long v2;  // 4137
    unsigned long v3;  // 4106
    unsigned long v4;  // 4106
    unsigned long v5;  // x0
    unsigned long v6;  // x0

    v2 = arm64g_calculate_condition(192, (((((unsigned long long)(char)(CmpF(v0, v1)) >> 5 & 3 | (unsigned long long)(CmpF(v0, v1) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v0, v1)) >> 5 & 3 | (unsigned long long)(CmpF(v0, v1) & 1)) & ((unsigned long long)(char)(CmpF(v0, v1)) >> 5 & 3 | (unsigned long long)(CmpF(v0, v1) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if ((char)v2)
    {
        v3 = arm64g_calculate_condition(192, (((((unsigned long long)(char)(CmpF(v0, 0)) >> 5 & 3 | (unsigned long long)(CmpF(v0, 0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v0, 0)) >> 5 & 3 | (unsigned long long)(CmpF(v0, 0) & 1)) & ((unsigned long long)(char)(CmpF(v0, 0)) >> 5 & 3 | (unsigned long long)(CmpF(v0, 0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if (!((char)v3))
            return v6;
    }
    else
    {
        v4 = arm64g_calculate_condition(192, 0x40000000, 0, 0);
        if (!((char)v4))
            return v6;
    }
    return v5;
}
```

## `CFUtils.ApplyNegativeDeltaInput` — RVA `0xc58508`

- Decompiled symbol: `CFUtils_ApplyNegativeDeltaInput`
- Metadata signature: `public static float ApplyNegativeDeltaInput(float negativeAccum, float delta) { }`
- Native interval: `20` bytes
- Result: `pseudocode`

```c
long long CFUtils_ApplyNegativeDeltaInput(void)
{
    unsigned int v0;  // s1
    unsigned int v1;  // s0
    unsigned long v2;  // 4137
    unsigned long v3;  // 4106
    unsigned long v4;  // 4106
    unsigned long v5;  // x0
    unsigned long v6;  // x0

    v2 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(v0, v1)) >> 5 & 3 | (unsigned long long)(CmpF(v0, v1) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v0, v1)) >> 5 & 3 | (unsigned long long)(CmpF(v0, v1) & 1)) & ((unsigned long long)(char)(CmpF(v0, v1)) >> 5 & 3 | (unsigned long long)(CmpF(v0, v1) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if ((char)v2)
    {
        v3 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(v0, 0)) >> 5 & 3 | (unsigned long long)(CmpF(v0, 0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v0, 0)) >> 5 & 3 | (unsigned long long)(CmpF(v0, 0) & 1)) & ((unsigned long long)(char)(CmpF(v0, 0)) >> 5 & 3 | (unsigned long long)(CmpF(v0, 0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if (!((char)v3))
            return v6;
    }
    else
    {
        v4 = arm64g_calculate_condition(64, 0, 0, 0);
        if (!((char)v4))
            return v6;
    }
    return v5;
}
```

## `CFUtils.ApplySignedDeltaInput` — RVA `0xc5851c`

- Decompiled symbol: `CFUtils_ApplySignedDeltaInput`
- Metadata signature: `public static void ApplySignedDeltaInput(float v, ref float plusAccum, ref float minusAccum) { }`
- Native interval: `48` bytes
- Result: `pseudocode`

```c
unsigned int * CFUtils_ApplySignedDeltaInput(unsigned int *ptr, unsigned int *p)
{
    unsigned int v0;  // s0
    unsigned long v1;  // 4125
    unsigned int v2;  // s1
    unsigned long v3;  // 4129
    unsigned int v4;  // s1
    unsigned long v5;  // 4129

    v1 = arm64g_calculate_condition(160, (((((unsigned long long)(char)(CmpF(v0, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v0, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v0, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v0, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v0, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v0, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if (!((char)v1))
    {
        v2 = *(p);
        v3 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v2, v0)) >> 5 & 3 | (unsigned long long)(CmpF(v2, v0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v2, v0)) >> 5 & 3 | (unsigned long long)(CmpF(v2, v0) & 1)) & ((unsigned long long)(char)(CmpF(v2, v0)) >> 5 & 3 | (unsigned long long)(CmpF(v2, v0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if ((char)v3)
            return ptr;
        *(p) = v0;
        return ptr;
    }
    else
    {
        v4 = *(ptr);
        v5 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v4, v0)) >> 5 & 3 | (unsigned long long)(CmpF(v4, v0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v4, v0)) >> 5 & 3 | (unsigned long long)(CmpF(v4, v0) & 1)) & ((unsigned long long)(char)(CmpF(v4, v0)) >> 5 & 3 | (unsigned long long)(CmpF(v4, v0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if (!((char)v5))
        {
            *(ptr) = v0;
            return ptr;
        }
        return ptr;
    }
}
```

## `CFUtils.ApplySignedDeltaInputInt` — RVA `0xc5854c`

- Decompiled symbol: `CFUtils_ApplySignedDeltaInputInt`
- Metadata signature: `public static void ApplySignedDeltaInputInt(int v, ref int plusAccum, ref int minusAccum) { }`
- Native interval: `44` bytes
- Result: `pseudocode`

```c
unsigned long long CFUtils_ApplySignedDeltaInputInt(unsigned long long a0, unsigned int *ptr, unsigned int *p)
{
    if (((char)(a0 >> 31) & 1))
    {
        if (*(p) <= (unsigned int)a0)
            return a0;
        *(p) = a0;
        return a0;
    }
    else if ((unsigned int)a0 > *(ptr))
    {
        *(ptr) = a0;
        return a0;
    }
    else
    {
        return a0;
    }
}
```

## `CFUtils.GetScrollValue` — RVA `0xc58578`

- Decompiled symbol: `CFUtils_GetScrollValue`
- Metadata signature: `public static int GetScrollValue(float drag, int prevScroll, float thresh, float magnet) { }`
- Native interval: `136` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: Decompiler produced no C-like text

```c
// 0x1058578: stp d9, d8, [sp, #-0x20]!
// 0x105857c: stp x30, x19, [sp, #0x10]
// 0x1058580: adrp x19, #0x1fab000
// 0x1058584: ldrb w8, [x19, #0x2cc]
// 0x1058588: mov v8.16b, v1.16b
// 0x105858c: mov v9.16b, v0.16b
// 0x1058590: cbnz w8, #0x10585a8
// 0x1058594: adrp x0, #0x1e8c000
// 0x1058598: ldr x0, [x0, #0xa60]
// 0x105859c: bl #0xf7d92c
// 0x10585a0: mov w8, #1
// 0x10585a4: strb w8, [x19, #0x2cc]
// 0x10585a8: adrp x8, #0x1e8c000
// 0x10585ac: ldr x8, [x8, #0xa60]
// 0x10585b0: ldr x0, [x8]
// 0x10585b4: ldr w8, [x0, #0xe0]
// 0x10585b8: cbnz w8, #0x10585c0
// 0x10585bc: bl #0xf7da5c
// 0x10585c0: fneg s0, s9
// 0x10585c4: fcmp s9, #0.0
// 0x10585c8: fcsel s0, s0, s9, mi
// 0x10585cc: mov w8, #0x7f800000
// 0x10585d0: fdiv s0, s0, s8
// 0x10585d4: fmov s1, w8
// 0x10585d8: frintm s2, s0
// 0x10585dc: ldp x30, x19, [sp, #0x10]
// 0x10585e0: mov w9, #-0x80000000
// 0x10585e4: fcvtms w8, s0
// 0x10585e8: fcmp s2, s1
// 0x10585ec: csel w8, w9, w8, eq
// 0x10585f0: fcmp s9, #0.0
// 0x10585f4: cneg w0, w8, mi
// 0x10585f8: ldp d9, d8, [sp], #0x20
// 0x10585fc: ret
```

## `CFUtils.GetLerpFactor` — RVA `0xc58600`

- Decompiled symbol: `CFUtils_GetLerpFactor`
- Metadata signature: `private static float GetLerpFactor(float smoothingTime, float deltaTime, float maxLerpFactor) { }`
- Native interval: `28` bytes
- Result: `pseudocode`

```c
long long CFUtils_GetLerpFactor(void)
{
    unsigned int v0;  // s1
    unsigned int v1;  // s0
    unsigned int v2;  // s3
    unsigned int v3;  // s0
    unsigned long v4;  // 4142
    unsigned int v5;  // s0
    unsigned int v6;  // s2
    unsigned long v7;  // 4129
    unsigned long v8;  // x0
    unsigned long v9;  // x0

    v2 = v0 / v1;
    v3 = 0x3f800000;
    v4 = arm64g_calculate_condition(128, (((((unsigned long long)(char)(CmpF(v1, v0)) >> 5 & 3 | (unsigned long long)(CmpF(v1, v0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v1, v0)) >> 5 & 3 | (unsigned long long)(CmpF(v1, v0) & 1)) & ((unsigned long long)(char)(CmpF(v1, v0)) >> 5 & 3 | (unsigned long long)(CmpF(v1, v0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if ((char)v4)
        v5 = v2;
    else
        v5 = v3;
    v7 = arm64g_calculate_condition(192, (((((unsigned long long)(char)(CmpF(v5, v6)) >> 5 & 3 | (unsigned long long)(CmpF(v5, v6) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v5, v6)) >> 5 & 3 | (unsigned long long)(CmpF(v5, v6) & 1)) & ((unsigned long long)(char)(CmpF(v5, v6)) >> 5 & 3 | (unsigned long long)(CmpF(v5, v6) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if (!((char)v7))
        return v9;
    return v8;
}
```

## `CFUtils.SmoothTowards` — RVA `0xc5861c`

- Decompiled symbol: `CFUtils_SmoothTowards`
- Metadata signature: `public static float SmoothTowards(float a, float b, float smoothingTime, float deltaTime, float epsilon, float maxLeftFactor = 0.75) { }`
- Native interval: `88` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: Decompiler produced no C-like text

```c
// 0x105861c: adrp x8, #0x832000
// 0x1058620: ldr s6, [x8, #0x534]
// 0x1058624: fcmp s2, s6
// 0x1058628: b.mi #0x105866c
// 0x105862c: fabd s6, s1, s0
// 0x1058630: fcmp s6, s4
// 0x1058634: b.ls #0x105866c
// 0x1058638: fdiv s4, s3, s2
// 0x105863c: fcmp s2, s3
// 0x1058640: fmov s2, #1.00000000
// 0x1058644: fcsel s3, s4, s2, hi
// 0x1058648: fcmp s3, s5
// 0x105864c: fcsel s3, s5, s3, gt
// 0x1058650: fmin s2, s3, s2
// 0x1058654: fcmp s3, #0.0
// 0x1058658: fmov s3, wzr
// 0x105865c: fsub s1, s1, s0
// 0x1058660: fcsel s2, s2, s3, pl
// 0x1058664: fmul s1, s1, s2
// 0x1058668: fadd s1, s1, s0
// 0x105866c: mov v0.16b, v1.16b
// 0x1058670: ret
```

## `CFUtils.SmoothTowardsAngle` — RVA `0xc58674`

- Decompiled symbol: `CFUtils_SmoothTowardsAngle`
- Metadata signature: `public static float SmoothTowardsAngle(float a, float b, float smoothingTime, float deltaTime, float epsilon, float maxLeftFactor = 0.75) { }`
- Native interval: `264` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: Decompiler produced no C-like text

```c
// 0x1058674: mov w8, #0x43b40000
// 0x1058678: fsub s6, s0, s1
// 0x105867c: fmov s7, w8
// 0x1058680: mov w8, #-0x3c4c0000
// 0x1058684: fdiv s16, s6, s7
// 0x1058688: fmov s17, w8
// 0x105868c: frintm s16, s16
// 0x1058690: fmul s16, s16, s17
// 0x1058694: fadd s6, s6, s16
// 0x1058698: mov w8, #0x43340000
// 0x105869c: fmov s16, wzr
// 0x10586a0: fmin s7, s6, s7
// 0x10586a4: fcmp s6, #0.0
// 0x10586a8: fmov s6, w8
// 0x10586ac: adrp x8, #0x832000
// 0x10586b0: fcsel s7, s7, s16, pl
// 0x10586b4: ldr s16, [x8, #0x534]
// 0x10586b8: fadd s17, s7, s17
// 0x10586bc: fcmp s7, s6
// 0x10586c0: fcsel s6, s17, s7, gt
// 0x10586c4: fcmp s2, s16
// 0x10586c8: b.mi #0x1058774
// 0x10586cc: fabs s6, s6
// 0x10586d0: fcmp s6, s4
// 0x10586d4: b.ls #0x1058774
// 0x10586d8: fdiv s7, s3, s2
// 0x10586dc: fcmp s2, s3
// 0x10586e0: fmov s2, #1.00000000
// 0x10586e4: mov w8, #0x43b40000
// 0x10586e8: fcsel s2, s7, s2, hi
// 0x10586ec: fsub s4, s1, s0
// 0x10586f0: fmov s3, w8
// 0x10586f4: fcmp s2, s5
// 0x10586f8: mov w8, #-0x3c4c0000
// 0x10586fc: fcsel s2, s5, s2, gt
// 0x1058700: fdiv s5, s4, s3
// 0x1058704: fmov s7, w8
// 0x1058708: frintm s5, s5
// 0x105870c: fmul s5, s5, s7
// 0x1058710: fadd s4, s4, s5
// 0x1058714: fmov s16, wzr
// 0x1058718: mov w8, #0x43340000
// 0x105871c: fmin s3, s4, s3
// 0x1058720: fcmp s4, #0.0
// 0x1058724: fmov s5, w8
// 0x1058728: fcsel s3, s3, s16, pl
// 0x105872c: fabd s6, s1, s0
// 0x1058730: fadd s4, s3, s7
// 0x1058734: fcmp s3, s5
// 0x1058738: fcsel s4, s4, s3, gt
// 0x105873c: fnmul s3, s6, s2
// 0x1058740: fcmp s4, s3
// 0x1058744: fmul s2, s6, s2
// 0x1058748: b.le #0x1058754
// 0x105874c: fcmp s4, s2
// 0x1058750: b.mi #0x1058774
// 0x1058754: fadd s1, s4, s0
// 0x1058758: fsub s4, s1, s0
// 0x105875c: fcmp s4, #0.0
// 0x1058760: fabd s5, s1, s0
// 0x1058764: fcsel s3, s2, s3, ge
// 0x1058768: fadd s0, s3, s0
// 0x105876c: fcmp s5, s2
// 0x1058770: fcsel s1, s0, s1, hi
// 0x1058774: mov v0.16b, v1.16b
// 0x1058778: ret
```

## `CFUtils.SmoothTowardsVec2` — RVA `0xc5877c`

- Decompiled symbol: `CFUtils_SmoothTowardsVec2`
- Metadata signature: `public static Vector2 SmoothTowardsVec2(Vector2 a, Vector2 b, float smoothingTime, float deltaTime, float sqrEpsilon, float maxLeftFactor = 0.75) { }`
- Native interval: `144` bytes
- Result: `pseudocode`

```c
long long CFUtils_SmoothTowardsVec2(void)
{
    unsigned int v0;  // s6
    unsigned long long v1;  // 4102
    unsigned int v8;  // s3
    unsigned int v9;  // s1
    unsigned long v12;  // 4190
    unsigned int v13;  // s4
    unsigned int v14;  // s5
    unsigned int v15;  // s2
    unsigned long v16;  // 4142
    unsigned int v17;  // s7
    unsigned long v18;  // 4129
    unsigned int v19;  // s2
    unsigned long v20;  // 4133
    unsigned long v21;  // x0
    unsigned long v22;  // x0
    unsigned long v23;  // x0
    unsigned long v2;  // 4129
    unsigned long v3;  // x0
    unsigned long v4;  // 4129
    unsigned int v5;  // s2
    unsigned int v6;  // s0
    unsigned int v7;  // s16

    v1 = (((CmpF(v0, 0.0) >> 5 & 3 | CmpF(v0, 0.0) & 1) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - ((CmpF(v0, 0.0) >> 5 & 3 | CmpF(v0, 0.0) & 1) & (CmpF(v0, 0.0) >> 5 & 3 | CmpF(v0, 0.0) & 1) >> 1 & 1);
    if ((char)(v1 * 0x10000000 >> 30))
    {
        v2 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(v13, 981668463)) >> 5 & 3 | (unsigned long long)(CmpF(v13, 981668463) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v13, 981668463)) >> 5 & 3 | (unsigned long long)(CmpF(v13, 981668463) & 1)) & ((unsigned long long)(char)(CmpF(v13, 981668463)) >> 5 & 3 | (unsigned long long)(CmpF(v13, 981668463) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if ((char)v2)
            return v3;
    }
    else
    {
        v4 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(v13, 981668463)) >> 5 & 3 | (unsigned long long)(CmpF(v13, 981668463) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v13, 981668463)) >> 5 & 3 | (unsigned long long)(CmpF(v13, 981668463) & 1)) & ((unsigned long long)(char)(CmpF(v13, 981668463)) >> 5 & 3 | (unsigned long long)(CmpF(v13, 981668463) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if ((char)v4)
            return v23;
        v7 = v5 - v6;
        v12 = arm64g_calculate_condition(144, (((((unsigned long long)(char)(CmpF((v5 - v6) * (v5 - v6) + (v8 - v9) * (v8 - v9), v0)) >> 5 & 3 | (unsigned long long)(CmpF(v7 * v7 + (v8 - v9) * (v8 - v9), v0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF((v5 - v6) * (v5 - v6) + (v8 - v9) * (v8 - v9), v0)) >> 5 & 3 | (unsigned long long)(CmpF((v5 - v6) * (v5 - v6) + (v8 - v9) * (v8 - v9), v0) & 1)) & ((unsigned long long)(char)(CmpF((v5 - v6) * (v5 - v6) + (v8 - v9) * (v8 - v9), v0)) >> 5 & 3 | (unsigned long long)(CmpF((v5 - v6) * (v5 - v6) + (v8 - v9) * (v8 - v9), v0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if ((char)v12)
            return v22;
    }
    v15 = v14 / v13;
    v16 = arm64g_calculate_condition(128, (((((unsigned long long)(char)(CmpF(v13, v14)) >> 5 & 3 | (unsigned long long)(CmpF(v13, v14) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v13, v14)) >> 5 & 3 | (unsigned long long)(CmpF(v13, v14) & 1)) & ((unsigned long long)(char)(CmpF(v13, v14)) >> 5 & 3 | (unsigned long long)(CmpF(v13, v14) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if (!((char)v16))
        v15 = 0x3f800000;
    v18 = arm64g_calculate_condition(192, (((((unsigned long long)(char)(CmpF(v15, v17)) >> 5 & 3 | (unsigned long long)(CmpF(v15, v17) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v15, v17)) >> 5 & 3 | (unsigned long long)(CmpF(v15, v17) & 1)) & ((unsigned long long)(char)(CmpF(v15, v17)) >> 5 & 3 | (unsigned long long)(CmpF(v15, v17) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if ((char)v18)
        v19 = v17;
    else
        v19 = v15;
    v20 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v19, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v19, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v19, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v19, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v19, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v19, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    return v21;
}
```

## `CFUtils.SmoothTowardsVec3` — RVA `0xc5880c`

- Decompiled symbol: `CFUtils_SmoothTowardsVec3`
- Metadata signature: `public static Vector3 SmoothTowardsVec3(Vector3 a, Vector3 b, float smoothingTime, float deltaTime, float sqrEpsilon, float maxLeftFactor = 0.75) { }`
- Native interval: `176` bytes
- Result: `pseudocode`

```c
long long CFUtils_SmoothTowardsVec3(unsigned long a0, unsigned long a1, unsigned long a2, unsigned long a3, unsigned long a4, unsigned long a5, unsigned long a6, unsigned long a7, unsigned int a8, unsigned int a9)
{
    unsigned long long v0;  // 4104
    unsigned int v1;  // s6
    unsigned int v9;  // s21
    unsigned int v10;  // s5
    unsigned int v11;  // s2
    unsigned long v14;  // 4229
    unsigned int v15;  // s7
    unsigned int v16;  // s4
    unsigned long v17;  // 4146
    unsigned long v2;  // 4125
    unsigned long v18;  // 4129
    unsigned int v19;  // s3
    unsigned long v20;  // 4133
    unsigned long v3;  // 4125
    unsigned int v4;  // s3
    unsigned int v5;  // s0
    unsigned int v6;  // s20
    unsigned int v7;  // s4
    unsigned int v8;  // s1

    v0 = (((CmpF(a8, 0.0) >> 5 & 3 | CmpF(a8, 0.0) & 1) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - ((CmpF(a8, 0.0) >> 5 & 3 | CmpF(a8, 0.0) & 1) & (CmpF(a8, 0.0) >> 5 & 3 | CmpF(a8, 0.0) & 1) >> 1 & 1);
    if ((char)(v0 * 0x10000000 >> 30))
    {
        v2 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(v1, 981668463)) >> 5 & 3 | (unsigned long long)(CmpF(v1, 981668463) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v1, 981668463)) >> 5 & 3 | (unsigned long long)(CmpF(v1, 981668463) & 1)) & ((unsigned long long)(char)(CmpF(v1, 981668463)) >> 5 & 3 | (unsigned long long)(CmpF(v1, 981668463) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if ((char)v2)
            return a0;
    }
    else
    {
        v3 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(v1, 981668463)) >> 5 & 3 | (unsigned long long)(CmpF(v1, 981668463) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v1, 981668463)) >> 5 & 3 | (unsigned long long)(CmpF(v1, 981668463) & 1)) & ((unsigned long long)(char)(CmpF(v1, 981668463)) >> 5 & 3 | (unsigned long long)(CmpF(v1, 981668463) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if ((char)v3)
            return a0;
        v6 = (v4 - v5) * (v4 - v5);
        v9 = (v7 - v8) * (v7 - v8);
        v14 = arm64g_calculate_condition(144, (((((unsigned long long)(char)(CmpF((v10 - v11) * (v10 - v11) + (v4 - v5) * (v4 - v5) + (v7 - v8) * (v7 - v8), a8)) >> 5 & 3 | (unsigned long long)(CmpF((v10 - v11) * (v10 - v11) + v6 + v9, a8) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF((v10 - v11) * (v10 - v11) + (v4 - v5) * (v4 - v5) + (v7 - v8) * (v7 - v8), a8)) >> 5 & 3 | (unsigned long long)(CmpF((v10 - v11) * (v10 - v11) + (v4 - v5) * (v4 - v5) + (v7 - v8) * (v7 - v8), a8) & 1)) & ((unsigned long long)(char)(CmpF((v10 - v11) * (v10 - v11) + v6 + v9, a8)) >> 5 & 3 | (unsigned long long)(CmpF((v10 - v11) * (v10 - v11) + (v4 - v5) * (v4 - v5) + (v7 - v8) * (v7 - v8), a8) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if ((char)v14)
            return a0;
    }
    v16 = v15 / v1;
    v17 = arm64g_calculate_condition(128, (((((unsigned long long)(char)(CmpF(v1, v15)) >> 5 & 3 | (unsigned long long)(CmpF(v1, v15) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v1, v15)) >> 5 & 3 | (unsigned long long)(CmpF(v1, v15) & 1)) & ((unsigned long long)(char)(CmpF(v1, v15)) >> 5 & 3 | (unsigned long long)(CmpF(v1, v15) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if (!((char)v17))
        v16 = 0x3f800000;
    v18 = arm64g_calculate_condition(192, (((((unsigned long long)(char)(CmpF(v16, a9)) >> 5 & 3 | (unsigned long long)(CmpF(v16, a9) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v16, a9)) >> 5 & 3 | (unsigned long long)(CmpF(v16, a9) & 1)) & ((unsigned long long)(char)(CmpF(v16, a9)) >> 5 & 3 | (unsigned long long)(CmpF(v16, a9) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if ((char)v18)
        v19 = a9;
    else
        v19 = v16;
    v20 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v19, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v19, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v19, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v19, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v19, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v19, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    return a0;
}
```

## `CFUtils.SmoothTowardsColor` — RVA `0xc588bc`

- Decompiled symbol: `CFUtils_SmoothTowardsColor`
- Metadata signature: `public static Color SmoothTowardsColor(Color a, Color b, float smoothingTime, float deltaTime, float maxLeftFactor = 0.75) { }`
- Native interval: `136` bytes
- Result: `pseudocode`

```c
long long CFUtils_SmoothTowardsColor(unsigned long a0, unsigned long a1, unsigned long a2, unsigned long a3, unsigned long a4, unsigned long a5, unsigned long a6, unsigned long a7, unsigned int a8, unsigned int a9, unsigned int a10)
{
    unsigned long v0;  // 4133
    unsigned int v1;  // s16
    unsigned long v2;  // 4163
    unsigned long v3;  // 4129
    unsigned int v4;  // s16
    unsigned long v5;  // 4172

    v0 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(a8, 981668463)) >> 5 & 3 | (unsigned long long)(CmpF(a8, 981668463) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(a8, 981668463)) >> 5 & 3 | (unsigned long long)(CmpF(a8, 981668463) & 1)) & ((unsigned long long)(char)(CmpF(a8, 981668463)) >> 5 & 3 | (unsigned long long)(CmpF(a8, 981668463) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if ((char)v0)
        return a0;
    v1 = a9 / a8;
    v2 = arm64g_calculate_condition(128, (((((unsigned long long)(char)(CmpF(a8, a9)) >> 5 & 3 | (unsigned long long)(CmpF(a8, a9) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(a8, a9)) >> 5 & 3 | (unsigned long long)(CmpF(a8, a9) & 1)) & ((unsigned long long)(char)(CmpF(a8, a9)) >> 5 & 3 | (unsigned long long)(CmpF(a8, a9) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if (!((char)v2))
        v1 = 0x3f800000;
    v3 = arm64g_calculate_condition(192, (((((unsigned long long)(char)(CmpF(v1, a10)) >> 5 & 3 | (unsigned long long)(CmpF(v1, a10) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v1, a10)) >> 5 & 3 | (unsigned long long)(CmpF(v1, a10) & 1)) & ((unsigned long long)(char)(CmpF(v1, a10)) >> 5 & 3 | (unsigned long long)(CmpF(v1, a10) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if ((char)v3)
        v4 = a10;
    else
        v4 = v1;
    v5 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v4, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v4, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v4, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v4, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v4, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v4, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    return a0;
}
```

## `CFUtils.SmoothTowardsQuat` — RVA `0xc58944`

- Decompiled symbol: `CFUtils_SmoothTowardsQuat`
- Metadata signature: `public static Quaternion SmoothTowardsQuat(Quaternion a, Quaternion b, float smoothingTime, float deltaTime, float maxLeftFactor = 0.75) { }`
- Native interval: `116` bytes
- Result: `pseudocode`

```c
int CFUtils_SmoothTowardsQuat(unsigned int a0, unsigned long a1, unsigned long a2, unsigned long a3, unsigned long a4, unsigned long a5, unsigned long a6, unsigned long a7, unsigned int a8, unsigned int a9, unsigned int a10)
{
    unsigned long v1;  // 4140
    unsigned int v2;  // s18
    unsigned int v3;  // s19
    unsigned int v4;  // s16
    unsigned long v5;  // 4154
    unsigned int v6;  // s16
    unsigned long v7;  // 4129
    unsigned int v8;  // s16
    unsigned int v0;  // [bp-0x20]

    v1 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(a8, 981668463)) >> 5 & 3 | (unsigned long long)(CmpF(a8, 981668463) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(a8, 981668463)) >> 5 & 3 | (unsigned long long)(CmpF(a8, 981668463) & 1)) & ((unsigned long long)(char)(CmpF(a8, 981668463)) >> 5 & 3 | (unsigned long long)(CmpF(a8, 981668463) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if ((char)v1)
        return a0;
    v2 = a10;
    v3 = a9 / a8;
    v4 = 0x3f800000;
    v5 = arm64g_calculate_condition(128, (((((unsigned long long)(char)(CmpF(a8, a9)) >> 5 & 3 | (unsigned long long)(CmpF(a8, a9) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(a8, a9)) >> 5 & 3 | (unsigned long long)(CmpF(a8, a9) & 1)) & ((unsigned long long)(char)(CmpF(a8, a9)) >> 5 & 3 | (unsigned long long)(CmpF(a8, a9) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if ((char)v5)
        v6 = v3;
    else
        v6 = v4;
    v7 = arm64g_calculate_condition(192, (((((unsigned long long)(char)(CmpF(v6, v2)) >> 5 & 3 | (unsigned long long)(CmpF(v6, v2) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v6, v2)) >> 5 & 3 | (unsigned long long)(CmpF(v6, v2) & 1)) & ((unsigned long long)(char)(CmpF(v6, v2)) >> 5 & 3 | (unsigned long long)(CmpF(v6, v2) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if ((char)v7)
        v8 = v2;
    else
        v8 = v6;
    v0 = v8;
    return Quaternion__Slerp();
}
```

## `CFUtils.SmoothDamp` — RVA `0xc589b8`

- Decompiled symbol: `CFUtils_SmoothDamp`
- Metadata signature: `public static float SmoothDamp(float valFrom, float valTo, ref float vel, float smoothingTime, float deltaTime, float epsilon) { }`
- Native interval: `64` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: Decompiler produced no C-like text

```c
// 0x10589b8: adrp x8, #0x832000
// 0x10589bc: mov v5.16b, v3.16b
// 0x10589c0: ldr s3, [x8, #0x534]
// 0x10589c4: fcmp s2, s3
// 0x10589c8: b.mi #0x10589ec
// 0x10589cc: fabd s3, s1, s0
// 0x10589d0: fcmp s3, s4
// 0x10589d4: b.ls #0x10589ec
// 0x10589d8: adrp x8, #0x832000
// 0x10589dc: ldr s3, [x8, #0x3a4]
// 0x10589e0: mov v4.16b, v5.16b
// 0x10589e4: mov x1, xzr
// 0x10589e8: b #0x1b8c860
// 0x10589ec: mov v0.16b, v1.16b
// 0x10589f0: str wzr, [x0]
// 0x10589f4: ret
```

## `CFUtils.ScaleColorAlpha` — RVA `0xc589f8`

- Decompiled symbol: `CFUtils_ScaleColorAlpha`
- Metadata signature: `public static Color ScaleColorAlpha(Color color, float alphaScale) { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long CFUtils_ScaleColorAlpha(void)
{
    unsigned long v0;  // x0

    return v0;
}
```

## `CFUtils.GetComponentHereOrInParent` — RVA `0xc58a00`

- Decompiled symbol: `CFUtils_GetComponentHereOrInParent`
- Metadata signature: `public static Component GetComponentHereOrInParent(Component comp, Type compType) { }`
- Native interval: `216` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab299;

long long CFUtils_GetComponentHereOrInParent(long long a0, long long a1)
{
    long long v0;  // x21
    unsigned long long v1;  // x0

    if (!(g_1fab299 & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab299 = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (((char)Object__op_Equality(a0, 0, 0) & 1))
        return 0;
    if (a0)
    {
        v0 = Component__GetComponent(a0, a1, 0);
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        if (!((char)Object__op_Inequality(v0, 0, 0) & 1))
        {
            v1 = Component__GetComponentInParent();
            return Component__GetComponentInParent();
        }
        return v0;
    }
    sub_f7db74();
}
```

## `CFUtils.IsStretchyRectTransform` — RVA `0xc58ad8`

- Decompiled symbol: `CFUtils_IsStretchyRectTransform`
- Metadata signature: `public static bool IsStretchyRectTransform(Transform tr) { }`
- Native interval: `232` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern long long g_1ef1170;
extern char g_1fab29a;

unsigned int CFUtils_IsStretchyRectTransform(unsigned long long *a0)
{
    unsigned long long *v0;  // x19
    unsigned int v1;  // s0
    unsigned int v2;  // s0
    unsigned int v3;  // s1
    unsigned int v4;  // s1
    unsigned long v6;  // 4197
    unsigned int v7;  // w0

    v0 = a0;
    if (!(g_1fab29a & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c(&g_1ef1170);
        g_1fab29a = 1;
    }
    if (v0 && *(v0) != g_1ef1170)
        v0 = NULL;
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (!((char)Object__op_Inequality(v0, 0, 0) & 1))
        return 0;
    if (v0)
    {
        RectTransform__get_anchorMax(v0, 0);
        RectTransform__get_anchorMin(v0, 0);
        v2 = v1 - v1;
        v4 = v3 - v3;
        v6 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF((v1 - v1) * (v1 - v1) + (v3 - v3) * (v3 - v3), 786163454)) >> 5 & 3 | (unsigned long long)(CmpF(v2 * v2 + v4 * v4, 786163454) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF((v1 - v1) * (v1 - v1) + (v3 - v3) * (v3 - v3), 786163454)) >> 5 & 3 | (unsigned long long)(CmpF((v1 - v1) * (v1 - v1) + (v3 - v3) * (v3 - v3), 786163454) & 1)) & ((unsigned long long)(char)(CmpF((v1 - v1) * (v1 - v1) + (v3 - v3) * (v3 - v3), 786163454)) >> 5 & 3 | (unsigned long long)(CmpF((v1 - v1) * (v1 - v1) + (v3 - v3) * (v3 - v3), 786163454) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if ((char)v6)
            v7 = 0;
        else
            v7 = 1;
        return v7;
    }
    sub_f7db74();
}
```

## `CFUtils.GetWorldAABB` — RVA `0xc58bc0`

- Decompiled symbol: `CFUtils_GetWorldAABB`
- Metadata signature: `public static Bounds GetWorldAABB(Matrix4x4 tf, Vector3 center, Vector3 size) { }`
- Native interval: `712` bytes
- Result: `pseudocode`

```c
unsigned long long CFUtils_GetWorldAABB(long long a0)
{
    unsigned long long v16;  // d15
    unsigned long long v17;  // d14
    unsigned long long v26;  // x19
    unsigned long v115;  // 4129
    unsigned int v116;  // s14
    unsigned int v117;  // s1
    unsigned long v118;  // 4133
    unsigned int v119;  // s8
    unsigned int v120;  // s0
    unsigned int v121;  // s2
    unsigned long v122;  // 4129
    unsigned int v123;  // s9
    unsigned int v124;  // s9
    unsigned int v27;  // s3
    unsigned long v125;  // 4129
    unsigned int v126;  // s10
    unsigned int v127;  // s10
    unsigned long v128;  // 4129
    unsigned int v129;  // s11
    unsigned int v130;  // s11
    unsigned long v131;  // 4129
    unsigned int v132;  // s12
    unsigned long v133;  // 4129
    unsigned int v134;  // s13
    unsigned int v28;  // s3
    unsigned int v135;  // s14
    unsigned int v136;  // s1
    unsigned long v137;  // 4137
    unsigned int v138;  // s8
    unsigned int v139;  // s0
    unsigned int v140;  // s2
    unsigned long v141;  // 4129
    unsigned int v142;  // s9
    unsigned int v143;  // s9
    unsigned long v144;  // 4129
    unsigned int v29;  // s4
    unsigned int v145;  // s10
    unsigned int v146;  // s10
    unsigned long v147;  // 4129
    unsigned int v148;  // s11
    unsigned int v149;  // s11
    unsigned long v150;  // 4129
    unsigned int v151;  // s12
    unsigned long v152;  // 4129
    unsigned int v153;  // s13
    unsigned int v154;  // s1
    unsigned int v30;  // s4
    unsigned long v155;  // 4133
    unsigned int v156;  // s8
    unsigned int v157;  // s0
    unsigned int v158;  // s2
    unsigned long long v159;  // x0
    unsigned long v160;  // 4129
    unsigned int v161;  // s3
    unsigned int v162;  // s3
    unsigned long v163;  // 4129
    unsigned int v164;  // s4
    unsigned int v31;  // s5
    unsigned int v165;  // s4
    unsigned long v166;  // 4129
    unsigned int v167;  // s5
    unsigned int v168;  // s5
    unsigned long v169;  // 4129
    unsigned int v170;  // s0
    unsigned long v171;  // 4129
    unsigned int v172;  // s1
    unsigned long v173;  // 4129
    unsigned int v174;  // s2
    unsigned int v32;  // s5
    unsigned int ptr[6];  // x8
    unsigned int v33;  // s0
    unsigned int v34;  // s13
    unsigned int v35;  // s1
    unsigned long long v18;  // d13
    unsigned int v36;  // s10
    unsigned int v37;  // s2
    unsigned int v38;  // s12
    unsigned int v39;  // s14
    unsigned int v40;  // s15
    unsigned int v41;  // s8
    unsigned int v42;  // s0
    unsigned int v43;  // s1
    unsigned int v44;  // s2
    unsigned long long v45;  // cc_dep1
    unsigned long long v19;  // d12
    unsigned long v46;  // 4129
    unsigned int v47;  // s9
    unsigned long v48;  // 4106
    unsigned long v49;  // 4106
    unsigned int v50;  // s14
    unsigned long long v51;  // cc_dep1
    unsigned long v52;  // 4129
    unsigned int v53;  // s10
    unsigned long v54;  // 4106
    unsigned long v55;  // 4106
    unsigned long long v20;  // d11
    unsigned int v56;  // s15
    unsigned long long v57;  // cc_dep1
    unsigned long v58;  // 4129
    unsigned int v59;  // s11
    unsigned long v60;  // 4106
    unsigned long v61;  // 4106
    unsigned int v62;  // s8
    unsigned int v63;  // s2
    unsigned int v64;  // s0
    unsigned long long v21;  // d10
    unsigned int v65;  // s1
    unsigned long v66;  // 4129
    unsigned int v67;  // s9
    unsigned int v68;  // s9
    unsigned long v69;  // 4129
    unsigned int v70;  // s10
    unsigned int v71;  // s10
    unsigned long v72;  // 4129
    unsigned int v73;  // s11
    unsigned int v74;  // s11
    unsigned long long v22;  // d9
    unsigned long v75;  // 4129
    unsigned int v76;  // s14
    unsigned long v77;  // 4129
    unsigned int v78;  // s15
    unsigned long v79;  // 4129
    unsigned int v80;  // s8
    unsigned int v81;  // s2
    unsigned int v82;  // s0
    unsigned int v83;  // s1
    unsigned long v84;  // 4129
    unsigned long long v23;  // d8
    unsigned int v85;  // s9
    unsigned int v86;  // s9
    unsigned long v87;  // 4129
    unsigned int v88;  // s10
    unsigned int v89;  // s10
    unsigned long v90;  // 4129
    unsigned int v91;  // s11
    unsigned int v92;  // s11
    unsigned long v93;  // 4129
    unsigned int v94;  // s13
    unsigned long long v24;  // x30
    unsigned long v95;  // 4129
    unsigned int v96;  // s14
    unsigned int v97;  // s15
    unsigned int v98;  // s12
    unsigned int v99;  // s1
    unsigned long v100;  // 4141
    unsigned int v101;  // s8
    unsigned int v102;  // s0
    unsigned int v103;  // s2
    unsigned long v104;  // 4129
    unsigned long long v25;  // x20
    unsigned int v105;  // s9
    unsigned int v106;  // s9
    unsigned long v107;  // 4129
    unsigned int v108;  // s10
    unsigned int v109;  // s10
    unsigned long v110;  // 4129
    unsigned int v111;  // s11
    unsigned int v112;  // s11
    unsigned long v113;  // 4129
    unsigned int v114;  // s13
    unsigned int v0;  // [bp-0x6c]
    unsigned int v1;  // [bp-0x68]
    unsigned int v2;  // [bp-0x64]
    unsigned long long v3;  // [bp-0x60]
    unsigned long long v4;  // [bp-0x58]
    unsigned long long v5;  // [bp-0x50]
    unsigned long long v6;  // [bp-0x48]
    unsigned long long v7;  // [bp-0x40]
    unsigned long long v8;  // [bp-0x38]
    unsigned long long v9;  // [bp-0x30]
    unsigned long long v10;  // [bp-0x28]
    unsigned long long v11;  // [bp-0x20]
    unsigned int v12;  // [bp-0x18]
    unsigned int v13;  // [bp-0x14]
    unsigned long long v14;  // [bp-0x10]
    unsigned long long v15;  // [bp-0x8]

    v3 = v16;
    v4 = v17;
    v5 = v18;
    v6 = v19;
    v7 = v20;
    v8 = v21;
    v9 = v22;
    v10 = v23;
    v11 = v24;
    v14 = v25;
    v15 = v26;
    v28 = v27 * 0x3f000000;
    v30 = v29 * 0x3f000000;
    v32 = v31 * 0x3f000000;
    v34 = v33 - v28;
    v36 = v35 - v30;
    v0 = v33 + v28;
    v1 = v37 - v32;
    v38 = v35 + v30;
    v12 = v37 + v32;
    v13 = v36;
    Matrix4x4__MultiplyPoint3x4();
    v39 = v34;
    v40 = v36;
    v41 = v1;
    v42 = v34;
    v43 = v36;
    v44 = v12;
    Matrix4x4__MultiplyPoint3x4(a0, 0);
    v45 = ((((CmpF(v39, v42) >> 5 & 3 | CmpF(v39, v42) & 1) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - ((CmpF(v39, v42) >> 5 & 3 | CmpF(v39, v42) & 1) & (CmpF(v39, v42) >> 5 & 3 | CmpF(v39, v42) & 1) >> 1 & 1)) * 0x10000000;
    v46 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(v39, v42)) >> 5 & 3 | (unsigned long long)(CmpF(v39, v42) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v39, v42)) >> 5 & 3 | (unsigned long long)(CmpF(v39, v42) & 1)) & ((unsigned long long)(char)(CmpF(v39, v42)) >> 5 & 3 | (unsigned long long)(CmpF(v39, v42) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if ((char)v46)
    {
        v47 = v39;
        v48 = arm64g_calculate_condition(192, v45, 0, 0);
        if (!((char)v48))
            goto LABEL_1058c56;
LABEL_1058c55:
        v50 = v39;
    }
    else
    {
        v47 = v42;
        v49 = arm64g_calculate_condition(192, v45, 0, 0);
        if ((char)v49)
            goto LABEL_1058c55;
LABEL_1058c56:
        v50 = v42;
    }
    v51 = ((((CmpF(v40, v43) >> 5 & 3 | CmpF(v40, v43) & 1) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - ((CmpF(v40, v43) >> 5 & 3 | CmpF(v40, v43) & 1) & (CmpF(v40, v43) >> 5 & 3 | CmpF(v40, v43) & 1) >> 1 & 1)) * 0x10000000;
    v52 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(v40, v43)) >> 5 & 3 | (unsigned long long)(CmpF(v40, v43) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v40, v43)) >> 5 & 3 | (unsigned long long)(CmpF(v40, v43) & 1)) & ((unsigned long long)(char)(CmpF(v40, v43)) >> 5 & 3 | (unsigned long long)(CmpF(v40, v43) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if ((char)v52)
    {
        v53 = v40;
        v54 = arm64g_calculate_condition(192, v51, 0, 0);
        if (!((char)v54))
            goto LABEL_1058c62;
LABEL_1058c61:
        v56 = v40;
    }
    else
    {
        v53 = v43;
        v55 = arm64g_calculate_condition(192, v51, 0, 0);
        if ((char)v55)
            goto LABEL_1058c61;
LABEL_1058c62:
        v56 = v43;
    }
    v57 = ((((CmpF(v41, v44) >> 5 & 3 | CmpF(v41, v44) & 1) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - ((CmpF(v41, v44) >> 5 & 3 | CmpF(v41, v44) & 1) & (CmpF(v41, v44) >> 5 & 3 | CmpF(v41, v44) & 1) >> 1 & 1)) * 0x10000000;
    v58 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(v41, v44)) >> 5 & 3 | (unsigned long long)(CmpF(v41, v44) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v41, v44)) >> 5 & 3 | (unsigned long long)(CmpF(v41, v44) & 1)) & ((unsigned long long)(char)(CmpF(v41, v44)) >> 5 & 3 | (unsigned long long)(CmpF(v41, v44) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if ((char)v58)
    {
        v59 = v41;
        v60 = arm64g_calculate_condition(192, v57, 0, 0);
        if (!((char)v60))
            goto LABEL_1058c6e;
LABEL_1058c6d:
        v62 = v41;
    }
    else
    {
        v59 = v44;
        v61 = arm64g_calculate_condition(192, v57, 0, 0);
        if ((char)v61)
            goto LABEL_1058c6d;
LABEL_1058c6e:
        v62 = v44;
    }
    v63 = v1;
    v64 = v34;
    v65 = v38;
    v2 = v38;
    Matrix4x4__MultiplyPoint3x4();
    v66 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(v47, v64)) >> 5 & 3 | (unsigned long long)(CmpF(v47, v64) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v47, v64)) >> 5 & 3 | (unsigned long long)(CmpF(v47, v64) & 1)) & ((unsigned long long)(char)(CmpF(v47, v64)) >> 5 & 3 | (unsigned long long)(CmpF(v47, v64) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if ((char)v66)
        v67 = v47;
    else
        v67 = v64;
    v68 = v67;
    v69 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(v53, v65)) >> 5 & 3 | (unsigned long long)(CmpF(v53, v65) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v53, v65)) >> 5 & 3 | (unsigned long long)(CmpF(v53, v65) & 1)) & ((unsigned long long)(char)(CmpF(v53, v65)) >> 5 & 3 | (unsigned long long)(CmpF(v53, v65) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if ((char)v69)
        v70 = v53;
    else
        v70 = v65;
    v71 = v70;
    v72 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(v59, v63)) >> 5 & 3 | (unsigned long long)(CmpF(v59, v63) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v59, v63)) >> 5 & 3 | (unsigned long long)(CmpF(v59, v63) & 1)) & ((unsigned long long)(char)(CmpF(v59, v63)) >> 5 & 3 | (unsigned long long)(CmpF(v59, v63) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if ((char)v72)
        v73 = v59;
    else
        v73 = v63;
    v74 = v73;
    v75 = arm64g_calculate_condition(192, (((((unsigned long long)(char)(CmpF(v50, v64)) >> 5 & 3 | (unsigned long long)(CmpF(v50, v64) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v50, v64)) >> 5 & 3 | (unsigned long long)(CmpF(v50, v64) & 1)) & ((unsigned long long)(char)(CmpF(v50, v64)) >> 5 & 3 | (unsigned long long)(CmpF(v50, v64) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if ((char)v75)
        v76 = v50;
    else
        v76 = v64;
    v77 = arm64g_calculate_condition(192, (((((unsigned long long)(char)(CmpF(v56, v65)) >> 5 & 3 | (unsigned long long)(CmpF(v56, v65) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v56, v65)) >> 5 & 3 | (unsigned long long)(CmpF(v56, v65) & 1)) & ((unsigned long long)(char)(CmpF(v56, v65)) >> 5 & 3 | (unsigned long long)(CmpF(v56, v65) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if ((char)v77)
        v78 = v56;
    else
        v78 = v65;
    v79 = arm64g_calculate_condition(192, (((((unsigned long long)(char)(CmpF(v62, v63)) >> 5 & 3 | (unsigned long long)(CmpF(v62, v63) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v62, v63)) >> 5 & 3 | (unsigned long long)(CmpF(v62, v63) & 1)) & ((unsigned long long)(char)(CmpF(v62, v63)) >> 5 & 3 | (unsigned long long)(CmpF(v62, v63) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if ((char)v79)
        v80 = v62;
    else
        v80 = v63;
    v81 = v12;
    v82 = v34;
    v83 = v38;
    Matrix4x4__MultiplyPoint3x4();
    v84 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(v68, v82)) >> 5 & 3 | (unsigned long long)(CmpF(v68, v82) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v68, v82)) >> 5 & 3 | (unsigned long long)(CmpF(v68, v82) & 1)) & ((unsigned long long)(char)(CmpF(v68, v82)) >> 5 & 3 | (unsigned long long)(CmpF(v68, v82) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if ((char)v84)
        v85 = v68;
    else
        v85 = v82;
    v86 = v85;
    v87 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(v71, v83)) >> 5 & 3 | (unsigned long long)(CmpF(v71, v83) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v71, v83)) >> 5 & 3 | (unsigned long long)(CmpF(v71, v83) & 1)) & ((unsigned long long)(char)(CmpF(v71, v83)) >> 5 & 3 | (unsigned long long)(CmpF(v71, v83) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if ((char)v87)
        v88 = v71;
    else
        v88 = v83;
    v89 = v88;
    v90 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(v74, v81)) >> 5 & 3 | (unsigned long long)(CmpF(v74, v81) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v74, v81)) >> 5 & 3 | (unsigned long long)(CmpF(v74, v81) & 1)) & ((unsigned long long)(char)(CmpF(v74, v81)) >> 5 & 3 | (unsigned long long)(CmpF(v74, v81) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if ((char)v90)
        v91 = v74;
    else
        v91 = v81;
    v92 = v91;
    v93 = arm64g_calculate_condition(192, (((((unsigned long long)(char)(CmpF(v76, v82)) >> 5 & 3 | (unsigned long long)(CmpF(v76, v82) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v76, v82)) >> 5 & 3 | (unsigned long long)(CmpF(v76, v82) & 1)) & ((unsigned long long)(char)(CmpF(v76, v82)) >> 5 & 3 | (unsigned long long)(CmpF(v76, v82) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if ((char)v93)
        v94 = v76;
    else
        v94 = v82;
    v95 = arm64g_calculate_condition(192, (((((unsigned long long)(char)(CmpF(v78, v83)) >> 5 & 3 | (unsigned long long)(CmpF(v78, v83) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v78, v83)) >> 5 & 3 | (unsigned long long)(CmpF(v78, v83) & 1)) & ((unsigned long long)(char)(CmpF(v78, v83)) >> 5 & 3 | (unsigned long long)(CmpF(v78, v83) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if ((char)v95)
        v96 = v78;
    else
        v96 = v83;
    v97 = v0;
    v98 = v1;
    v99 = v13;
    v100 = arm64g_calculate_condition(192, (((((unsigned long long)(char)(CmpF(v80, v81)) >> 5 & 3 | (unsigned long long)(CmpF(v80, v81) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v80, v81)) >> 5 & 3 | (unsigned long long)(CmpF(v80, v81) & 1)) & ((unsigned long long)(char)(CmpF(v80, v81)) >> 5 & 3 | (unsigned long long)(CmpF(v80, v81) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if ((char)v100)
        v101 = v80;
    else
        v101 = v81;
    v102 = v97;
    v103 = v98;
    Matrix4x4__MultiplyPoint3x4();
    v104 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(v86, v102)) >> 5 & 3 | (unsigned long long)(CmpF(v86, v102) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v86, v102)) >> 5 & 3 | (unsigned long long)(CmpF(v86, v102) & 1)) & ((unsigned long long)(char)(CmpF(v86, v102)) >> 5 & 3 | (unsigned long long)(CmpF(v86, v102) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if ((char)v104)
        v105 = v86;
    else
        v105 = v102;
    v106 = v105;
    v107 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(v89, v99)) >> 5 & 3 | (unsigned long long)(CmpF(v89, v99) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v89, v99)) >> 5 & 3 | (unsigned long long)(CmpF(v89, v99) & 1)) & ((unsigned long long)(char)(CmpF(v89, v99)) >> 5 & 3 | (unsigned long long)(CmpF(v89, v99) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if ((char)v107)
        v108 = v89;
    else
        v108 = v99;
    v109 = v108;
    v110 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(v92, v103)) >> 5 & 3 | (unsigned long long)(CmpF(v92, v103) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v92, v103)) >> 5 & 3 | (unsigned long long)(CmpF(v92, v103) & 1)) & ((unsigned long long)(char)(CmpF(v92, v103)) >> 5 & 3 | (unsigned long long)(CmpF(v92, v103) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if ((char)v110)
        v111 = v92;
    else
        v111 = v103;
    v112 = v111;
    v113 = arm64g_calculate_condition(192, (((((unsigned long long)(char)(CmpF(v94, v102)) >> 5 & 3 | (unsigned long long)(CmpF(v94, v102) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v94, v102)) >> 5 & 3 | (unsigned long long)(CmpF(v94, v102) & 1)) & ((unsigned long long)(char)(CmpF(v94, v102)) >> 5 & 3 | (unsigned long long)(CmpF(v94, v102) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if ((char)v113)
        v114 = v94;
    else
        v114 = v102;
    v115 = arm64g_calculate_condition(192, (((((unsigned long long)(char)(CmpF(v96, v99)) >> 5 & 3 | (unsigned long long)(CmpF(v96, v99) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v96, v99)) >> 5 & 3 | (unsigned long long)(CmpF(v96, v99) & 1)) & ((unsigned long long)(char)(CmpF(v96, v99)) >> 5 & 3 | (unsigned long long)(CmpF(v96, v99) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if ((char)v115)
        v116 = v96;
    else
        v116 = v99;
    v117 = v2;
    v118 = arm64g_calculate_condition(192, (((((unsigned long long)(char)(CmpF(v101, v103)) >> 5 & 3 | (unsigned long long)(CmpF(v101, v103) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v101, v103)) >> 5 & 3 | (unsigned long long)(CmpF(v101, v103) & 1)) & ((unsigned long long)(char)(CmpF(v101, v103)) >> 5 & 3 | (unsigned long long)(CmpF(v101, v103) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if ((char)v118)
        v119 = v101;
    else
        v119 = v103;
    v120 = v97;
    v121 = v98;
    Matrix4x4__MultiplyPoint3x4();
    v122 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(v106, v120)) >> 5 & 3 | (unsigned long long)(CmpF(v106, v120) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v106, v120)) >> 5 & 3 | (unsigned long long)(CmpF(v106, v120) & 1)) & ((unsigned long long)(char)(CmpF(v106, v120)) >> 5 & 3 | (unsigned long long)(CmpF(v106, v120) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if ((char)v122)
        v123 = v106;
    else
        v123 = v120;
    v124 = v123;
    v125 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(v109, v117)) >> 5 & 3 | (unsigned long long)(CmpF(v109, v117) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v109, v117)) >> 5 & 3 | (unsigned long long)(CmpF(v109, v117) & 1)) & ((unsigned long long)(char)(CmpF(v109, v117)) >> 5 & 3 | (unsigned long long)(CmpF(v109, v117) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if ((char)v125)
        v126 = v109;
    else
        v126 = v117;
    v127 = v126;
    v128 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(v112, v121)) >> 5 & 3 | (unsigned long long)(CmpF(v112, v121) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v112, v121)) >> 5 & 3 | (unsigned long long)(CmpF(v112, v121) & 1)) & ((unsigned long long)(char)(CmpF(v112, v121)) >> 5 & 3 | (unsigned long long)(CmpF(v112, v121) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if ((char)v128)
        v129 = v112;
    else
        v129 = v121;
    v130 = v129;
    v131 = arm64g_calculate_condition(192, (((((unsigned long long)(char)(CmpF(v114, v120)) >> 5 & 3 | (unsigned long long)(CmpF(v114, v120) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v114, v120)) >> 5 & 3 | (unsigned long long)(CmpF(v114, v120) & 1)) & ((unsigned long long)(char)(CmpF(v114, v120)) >> 5 & 3 | (unsigned long long)(CmpF(v114, v120) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if ((char)v131)
        v132 = v114;
    else
        v132 = v120;
    v133 = arm64g_calculate_condition(192, (((((unsigned long long)(char)(CmpF(v116, v117)) >> 5 & 3 | (unsigned long long)(CmpF(v116, v117) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v116, v117)) >> 5 & 3 | (unsigned long long)(CmpF(v116, v117) & 1)) & ((unsigned long long)(char)(CmpF(v116, v117)) >> 5 & 3 | (unsigned long long)(CmpF(v116, v117) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if ((char)v133)
        v134 = v116;
    else
        v134 = v117;
    v135 = v12;
    v136 = v13;
    v137 = arm64g_calculate_condition(192, (((((unsigned long long)(char)(CmpF(v119, v121)) >> 5 & 3 | (unsigned long long)(CmpF(v119, v121) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v119, v121)) >> 5 & 3 | (unsigned long long)(CmpF(v119, v121) & 1)) & ((unsigned long long)(char)(CmpF(v119, v121)) >> 5 & 3 | (unsigned long long)(CmpF(v119, v121) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if ((char)v137)
        v138 = v119;
    else
        v138 = v121;
    v139 = v97;
    v140 = v135;
    Matrix4x4__MultiplyPoint3x4();
    v141 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(v124, v139)) >> 5 & 3 | (unsigned long long)(CmpF(v124, v139) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v124, v139)) >> 5 & 3 | (unsigned long long)(CmpF(v124, v139) & 1)) & ((unsigned long long)(char)(CmpF(v124, v139)) >> 5 & 3 | (unsigned long long)(CmpF(v124, v139) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if ((char)v141)
        v142 = v124;
    else
        v142 = v139;
    v143 = v142;
    v144 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(v127, v136)) >> 5 & 3 | (unsigned long long)(CmpF(v127, v136) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v127, v136)) >> 5 & 3 | (unsigned long long)(CmpF(v127, v136) & 1)) & ((unsigned long long)(char)(CmpF(v127, v136)) >> 5 & 3 | (unsigned long long)(CmpF(v127, v136) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if ((char)v144)
        v145 = v127;
    else
        v145 = v136;
    v146 = v145;
    v147 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(v130, v140)) >> 5 & 3 | (unsigned long long)(CmpF(v130, v140) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v130, v140)) >> 5 & 3 | (unsigned long long)(CmpF(v130, v140) & 1)) & ((unsigned long long)(char)(CmpF(v130, v140)) >> 5 & 3 | (unsigned long long)(CmpF(v130, v140) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if ((char)v147)
        v148 = v130;
    else
        v148 = v140;
    v149 = v148;
    v150 = arm64g_calculate_condition(192, (((((unsigned long long)(char)(CmpF(v132, v139)) >> 5 & 3 | (unsigned long long)(CmpF(v132, v139) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v132, v139)) >> 5 & 3 | (unsigned long long)(CmpF(v132, v139) & 1)) & ((unsigned long long)(char)(CmpF(v132, v139)) >> 5 & 3 | (unsigned long long)(CmpF(v132, v139) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if ((char)v150)
        v151 = v132;
    else
        v151 = v139;
    v152 = arm64g_calculate_condition(192, (((((unsigned long long)(char)(CmpF(v134, v136)) >> 5 & 3 | (unsigned long long)(CmpF(v134, v136) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v134, v136)) >> 5 & 3 | (unsigned long long)(CmpF(v134, v136) & 1)) & ((unsigned long long)(char)(CmpF(v134, v136)) >> 5 & 3 | (unsigned long long)(CmpF(v134, v136) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if ((char)v152)
        v153 = v134;
    else
        v153 = v136;
    v154 = v2;
    v155 = arm64g_calculate_condition(192, (((((unsigned long long)(char)(CmpF(v138, v140)) >> 5 & 3 | (unsigned long long)(CmpF(v138, v140) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v138, v140)) >> 5 & 3 | (unsigned long long)(CmpF(v138, v140) & 1)) & ((unsigned long long)(char)(CmpF(v138, v140)) >> 5 & 3 | (unsigned long long)(CmpF(v138, v140) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if ((char)v155)
        v156 = v138;
    else
        v156 = v140;
    v157 = v97;
    v158 = v135;
    v159 = Matrix4x4__MultiplyPoint3x4();
    v160 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(v143, v157)) >> 5 & 3 | (unsigned long long)(CmpF(v143, v157) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v143, v157)) >> 5 & 3 | (unsigned long long)(CmpF(v143, v157) & 1)) & ((unsigned long long)(char)(CmpF(v143, v157)) >> 5 & 3 | (unsigned long long)(CmpF(v143, v157) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if ((char)v160)
        v161 = v143;
    else
        v161 = v157;
    v162 = v161;
    v163 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(v146, v154)) >> 5 & 3 | (unsigned long long)(CmpF(v146, v154) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v146, v154)) >> 5 & 3 | (unsigned long long)(CmpF(v146, v154) & 1)) & ((unsigned long long)(char)(CmpF(v146, v154)) >> 5 & 3 | (unsigned long long)(CmpF(v146, v154) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if ((char)v163)
        v164 = v146;
    else
        v164 = v154;
    v165 = v164;
    v166 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(v149, v158)) >> 5 & 3 | (unsigned long long)(CmpF(v149, v158) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v149, v158)) >> 5 & 3 | (unsigned long long)(CmpF(v149, v158) & 1)) & ((unsigned long long)(char)(CmpF(v149, v158)) >> 5 & 3 | (unsigned long long)(CmpF(v149, v158) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if ((char)v166)
        v167 = v149;
    else
        v167 = v158;
    v168 = v167;
    v169 = arm64g_calculate_condition(192, (((((unsigned long long)(char)(CmpF(v151, v157)) >> 5 & 3 | (unsigned long long)(CmpF(v151, v157) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v151, v157)) >> 5 & 3 | (unsigned long long)(CmpF(v151, v157) & 1)) & ((unsigned long long)(char)(CmpF(v151, v157)) >> 5 & 3 | (unsigned long long)(CmpF(v151, v157) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if ((char)v169)
        v170 = v151;
    else
        v170 = v157;
    v171 = arm64g_calculate_condition(192, (((((unsigned long long)(char)(CmpF(v153, v154)) >> 5 & 3 | (unsigned long long)(CmpF(v153, v154) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v153, v154)) >> 5 & 3 | (unsigned long long)(CmpF(v153, v154) & 1)) & ((unsigned long long)(char)(CmpF(v153, v154)) >> 5 & 3 | (unsigned long long)(CmpF(v153, v154) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if ((char)v171)
        v172 = v153;
    else
        v172 = v154;
    v173 = arm64g_calculate_condition(192, (((((unsigned long long)(char)(CmpF(v156, v158)) >> 5 & 3 | (unsigned long long)(CmpF(v156, v158) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v156, v158)) >> 5 & 3 | (unsigned long long)(CmpF(v156, v158) & 1)) & ((unsigned long long)(char)(CmpF(v156, v158)) >> 5 & 3 | (unsigned long long)(CmpF(v156, v158) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if ((char)v173)
        v174 = v156;
    else
        v174 = v158;
    ptr[0] = (v162 + v170) * 0x3f000000;
    ptr[1] = (v165 + v172) * 0x3f000000;
    ptr[2] = (v168 + v174) * 0x3f000000;
    ptr[3] = (v170 - v162) * 0x3f000000;
    ptr[4] = (v172 - v165) * 0x3f000000;
    ptr[5] = (v174 - v168) * 0x3f000000;
    return v159;
}
```

## `CFUtils.GetWorldAABB` — RVA `0xc58e88`

- Decompiled symbol: `CFUtils_GetWorldAABB`
- Metadata signature: `public static Bounds GetWorldAABB(Matrix4x4 tf, Bounds localBounds) { }`
- Native interval: `92` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    uint128_t field_0;
    unsigned long long field_10;
} struct_0;

unsigned long long CFUtils_GetWorldAABB(uint128_t *ptr, unsigned long a1)
{
    unsigned long long v6;  // x0
    struct_0 *p;  // x8
    int v0;  // [bp-0x70]
    int v1;  // [bp-0x60]
    int v2;  // [bp-0x50]
    int v3;  // [bp-0x40]
    int v4;  // [bp-0x28]
    unsigned long v5;  // [bp-0x18]

    v2 = (int)ptr[2];
    v3 = (int)ptr[3];
    v0 = (int)*(ptr);
    v1 = (int)ptr[1];
    v6 = CFUtils__GetWorldAABB(&v0);
    p->field_10 = v5;
    *((void*)&p->field_0) = v4;
    return v6;
}
```

## `CFUtils.GetWorldRect` — RVA `0xc58ee4`

- Decompiled symbol: `CFUtils_GetWorldRect`
- Metadata signature: `public static Rect GetWorldRect(Matrix4x4 tf, Bounds localBounds) { }`
- Native interval: `108` bytes
- Result: `pseudocode`

```c
unsigned long long CFUtils_GetWorldRect(uint128_t *ptr, unsigned long a1)
{
    unsigned long long v8;  // x0
    int v0;  // [bp-0xb0]
    int v1;  // [bp-0xa0]
    int v2;  // [bp-0x90]
    int v3;  // [bp-0x80]
    int v4;  // [bp-0x70]
    int v5;  // [bp-0x60]
    int v6;  // [bp-0x50]
    int v7;  // [bp-0x40]

    v2 = (int)ptr[2];
    v3 = (int)ptr[3];
    v0 = (int)*(ptr);
    v1 = (int)ptr[1];
    v4 = (int)*(ptr);
    v5 = (int)ptr[1];
    v6 = (int)ptr[2];
    v7 = (int)ptr[3];
    v8 = CFUtils__GetWorldAABB(&v4);
    return CFUtils__GetWorldAABB(&v4);
}
```

## `CFUtils.ClampEllipseInsideEllipse` — RVA `0xc58f50`

- Decompiled symbol: `CFUtils_ClampEllipseInsideEllipse`
- Metadata signature: `public static Vector2 ClampEllipseInsideEllipse(Rect rect, Rect limiterRect) { }`
- Native interval: `496` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[224];
    unsigned int field_e0;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern long long g_1ef22b8;
extern char g_1fab1e0;
extern char g_1fab243;

struct_1 * CFUtils_ClampEllipseInsideEllipse(void)
{
    unsigned int v0;  // s2
    unsigned int v1;  // s16
    unsigned int v10;  // s1
    unsigned int v11;  // s1
    unsigned int v12;  // s4
    unsigned int v13;  // s7
    unsigned int v14;  // s5
    unsigned int v15;  // s4
    unsigned long v16;  // 4264
    unsigned long v17;  // 4125
    unsigned int v18;  // s12
    unsigned int v19;  // s13
    unsigned int v2;  // s3
    unsigned long v21;  // 4242
    struct_1 *v22;  // x0
    struct_0 *v23;  // x0, Other Possible Types: struct_1 *
    unsigned int v24;  // s1
    unsigned long v25;  // 4140
    unsigned long v26;  // 4125
    unsigned long v27;  // 4125
    unsigned long v28;  // 4125
    unsigned int v3;  // s2
    unsigned long v29;  // 4125
    struct_1 *v30;  // x0
    struct_1 *v31;  // x0
    struct_1 *v32;  // x0
    unsigned int v4;  // s6
    unsigned int v5;  // s6
    unsigned int v6;  // s7
    unsigned int v7;  // s3
    unsigned int v8;  // s0
    unsigned int v9;  // s0

    v1 = v0 * 0x3f000000;
    v3 = v2 * 0x3f000000;
    v5 = v4 * 0x3f000000;
    v7 = v6 * 0x3f000000;
    v9 = v8 + v1;
    v11 = v10 + v3;
    v13 = v12 + v5;
    v15 = v14 + v7;
    v16 = arm64g_calculate_condition(160, (((((unsigned long long)(char)(CmpF(v3, v7)) >> 5 & 3 | (unsigned long long)(CmpF(v3, v7) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v3, v7)) >> 5 & 3 | (unsigned long long)(CmpF(v3, v7) & 1)) & ((unsigned long long)(char)(CmpF(v3, v7)) >> 5 & 3 | (unsigned long long)(CmpF(v3, v7) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if (!((char)v16))
    {
        v17 = arm64g_calculate_condition(160, (((((unsigned long long)(char)(CmpF(v1, v5)) >> 5 & 3 | (unsigned long long)(CmpF(v1, v5) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v1, v5)) >> 5 & 3 | (unsigned long long)(CmpF(v1, v5) & 1)) & ((unsigned long long)(char)(CmpF(v1, v5)) >> 5 & 3 | (unsigned long long)(CmpF(v1, v5) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if (!((char)v17))
        {
            v18 = (v9 - v13) / (v5 - v1);
            v19 = (v11 - v15) / (v7 - v3);
            v21 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF((v9 - v13) / (v5 - v1) * (v9 - v13) / (v5 - v1) + (v11 - v15) / (v7 - v3) * (v11 - v15) / (v7 - v3), 0x3f800000)) >> 5 & 3 | (unsigned long long)(CmpF(v18 * v18 + v19 * v19, 0x3f800000) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF((v9 - v13) / (v5 - v1) * (v9 - v13) / (v5 - v1) + (v11 - v15) / (v7 - v3) * (v11 - v15) / (v7 - v3), 0x3f800000)) >> 5 & 3 | (unsigned long long)(CmpF((v9 - v13) / (v5 - v1) * (v9 - v13) / (v5 - v1) + (v11 - v15) / (v7 - v3) * (v11 - v15) / (v7 - v3), 0x3f800000) & 1)) & ((unsigned long long)(char)(CmpF(v18 * v18 + v19 * v19, 0x3f800000)) >> 5 & 3 | (unsigned long long)(CmpF((v9 - v13) / (v5 - v1) * (v9 - v13) / (v5 - v1) + (v11 - v15) / (v7 - v3) * (v11 - v15) / (v7 - v3), 0x3f800000) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
            if (!((char)v21))
            {
                if (!g_1fab1e0)
                {
                    v22 = sub_f7d92c(&g_1ef22b8);
                    g_1fab1e0 = 1;
                }
                return v22;
            }
            else
            {
                if (!g_1fab243)
                {
                    sub_f7d92c("_F");
                    g_1fab243 = 1;
                }
                v23 = g_1ef07e8;
                if (!g_1ef07e8->field_e0)
                    v23 = sub_f7da5c(g_1ef07e8);
                v24 = [D] unsupported_Iop_SqrtF32();
                v25 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v24, 925353388)) >> 5 & 3 | (unsigned long long)(CmpF(v24, 925353388) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v24, 925353388)) >> 5 & 3 | (unsigned long long)(CmpF(v24, 925353388) & 1)) & ((unsigned long long)(char)(CmpF(v24, 925353388)) >> 5 & 3 | (unsigned long long)(CmpF(v24, 925353388) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                if ((char)v25)
                {
                    if (!g_1fab1e0)
                    {
                        v23 = sub_f7d92c(&g_1ef22b8);
                        g_1fab1e0 = 1;
                    }
                }
                return v23;
            }
        }
    }
    v26 = arm64g_calculate_condition(176, (((((unsigned long long)(char)(CmpF(v1, v5)) >> 5 & 3 | (unsigned long long)(CmpF(v1, v5) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v1, v5)) >> 5 & 3 | (unsigned long long)(CmpF(v1, v5) & 1)) & ((unsigned long long)(char)(CmpF(v1, v5)) >> 5 & 3 | (unsigned long long)(CmpF(v1, v5) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if ((char)v26)
        v27 = arm64g_calculate_condition(160, (((((unsigned long long)(char)(CmpF(v9, v13)) >> 5 & 3 | (unsigned long long)(CmpF(v9, v13) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v9, v13)) >> 5 & 3 | (unsigned long long)(CmpF(v9, v13) & 1)) & ((unsigned long long)(char)(CmpF(v9, v13)) >> 5 & 3 | (unsigned long long)(CmpF(v9, v13) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    v28 = arm64g_calculate_condition(160, (((((unsigned long long)(char)(CmpF(v3, v7)) >> 5 & 3 | (unsigned long long)(CmpF(v3, v7) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v3, v7)) >> 5 & 3 | (unsigned long long)(CmpF(v3, v7) & 1)) & ((unsigned long long)(char)(CmpF(v3, v7)) >> 5 & 3 | (unsigned long long)(CmpF(v3, v7) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if ((char)v28)
        return v32;
    v29 = arm64g_calculate_condition(160, (((((unsigned long long)(char)(CmpF(v11, v15)) >> 5 & 3 | (unsigned long long)(CmpF(v11, v15) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v11, v15)) >> 5 & 3 | (unsigned long long)(CmpF(v11, v15) & 1)) & ((unsigned long long)(char)(CmpF(v11, v15)) >> 5 & 3 | (unsigned long long)(CmpF(v11, v15) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if ((char)v29)
        return v31;
    return v30;
}
```

## `CFUtils.ClampRectInsideEllipse` — RVA `0xc59140`

- Decompiled symbol: `CFUtils_ClampRectInsideEllipse`
- Metadata signature: `public static Vector2 ClampRectInsideEllipse(Rect rect, Rect limiterRect) { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[224];
    unsigned int field_e0;
} struct_1;

struct_1 * CFUtils_ClampRectInsideEllipse(void)
{
    struct_1 *v0;  // x0

    v0 = CFUtils__ClampEllipseInsideEllipse();
    return CFUtils__ClampEllipseInsideEllipse();
}
```

## `CFUtils.ClampRectInsideRect` — RVA `0xc59144`

- Decompiled symbol: `CFUtils_ClampRectInsideRect`
- Metadata signature: `public static Vector2 ClampRectInsideRect(Rect rect, Rect limiterRect) { }`
- Native interval: `296` bytes
- Result: `pseudocode`

```c
extern long long g_1ef22b8;
extern char g_1fab1e0;

void CFUtils_ClampRectInsideRect(void)
{
    unsigned int v0;  // s2
    unsigned int v1;  // s15
    unsigned int v8;  // s7
    unsigned int v9;  // s7
    unsigned int v10;  // s0
    unsigned int v11;  // s0
    unsigned int v12;  // s4
    unsigned int v13;  // s3
    unsigned long v14;  // 4189
    unsigned long v15;  // 4151
    unsigned long v16;  // 4151
    unsigned int v17;  // s3
    unsigned int v2;  // s6
    unsigned int v18;  // s4
    unsigned long v19;  // 4151
    unsigned long v20;  // 4151
    unsigned long v21;  // 4151
    unsigned int v3;  // s14
    unsigned int v4;  // s1
    unsigned int v5;  // s5
    unsigned int v6;  // s3
    unsigned int v7;  // s2

    v1 = v0 * 0x3f000000;
    v3 = v2 * 0x3f000000;
    if (!g_1fab1e0)
    {
        sub_f7d92c(&g_1ef22b8);
        g_1fab1e0 = 1;
    }
    v7 = v6 * 0x3f000000;
    v9 = v8 * 0x3f000000;
    v11 = v10 + v1;
    v13 = v12 + v3;
    v14 = arm64g_calculate_condition(160, (((((unsigned long long)(char)(CmpF(v1, v3)) >> 5 & 3 | (unsigned long long)(CmpF(v1, v3) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v1, v3)) >> 5 & 3 | (unsigned long long)(CmpF(v1, v3) & 1)) & ((unsigned long long)(char)(CmpF(v1, v3)) >> 5 & 3 | (unsigned long long)(CmpF(v1, v3) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if (!((char)v14))
    {
        v15 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v1 + v11, v3 + v13)) >> 5 & 3 | (unsigned long long)(CmpF(v1 + v11, v3 + v13) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v1 + v11, v3 + v13)) >> 5 & 3 | (unsigned long long)(CmpF(v1 + v11, v3 + v13) & 1)) & ((unsigned long long)(char)(CmpF(v1 + v11, v3 + v13)) >> 5 & 3 | (unsigned long long)(CmpF(v1 + v11, v3 + v13) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if ((char)v15)
        {
            v16 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v11 - v1, v13 - v3)) >> 5 & 3 | (unsigned long long)(CmpF(v11 - v1, v13 - v3) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v11 - v1, v13 - v3)) >> 5 & 3 | (unsigned long long)(CmpF(v11 - v1, v13 - v3) & 1)) & ((unsigned long long)(char)(CmpF(v11 - v1, v13 - v3)) >> 5 & 3 | (unsigned long long)(CmpF(v11 - v1, v13 - v3) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
            if (!((char)v16))
                goto LABEL_10591f8;
        }
    }
    else
    {
LABEL_10591f8:
    }
    v17 = v4 + v7;
    v18 = v5 + v9;
    v19 = arm64g_calculate_condition(160, (((((unsigned long long)(char)(CmpF(v7, v9)) >> 5 & 3 | (unsigned long long)(CmpF(v7, v9) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v7, v9)) >> 5 & 3 | (unsigned long long)(CmpF(v7, v9) & 1)) & ((unsigned long long)(char)(CmpF(v7, v9)) >> 5 & 3 | (unsigned long long)(CmpF(v7, v9) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if ((char)v19)
        return;
    v20 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v7 + v17, v9 + v18)) >> 5 & 3 | (unsigned long long)(CmpF(v7 + v17, v9 + v18) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v7 + v17, v9 + v18)) >> 5 & 3 | (unsigned long long)(CmpF(v7 + v17, v9 + v18) & 1)) & ((unsigned long long)(char)(CmpF(v7 + v17, v9 + v18)) >> 5 & 3 | (unsigned long long)(CmpF(v7 + v17, v9 + v18) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if (!((char)v20))
        return;
    v21 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v17 - v7, v18 - v9)) >> 5 & 3 | (unsigned long long)(CmpF(v17 - v7, v18 - v9) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v17 - v7, v18 - v9)) >> 5 & 3 | (unsigned long long)(CmpF(v17 - v7, v18 - v9) & 1)) & ((unsigned long long)(char)(CmpF(v17 - v7, v18 - v9)) >> 5 & 3 | (unsigned long long)(CmpF(v17 - v7, v18 - v9) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if ((char)v21)
        return;
    return;
}
```

## `CFUtils.ClampPerAxisInsideUnitSquare` — RVA `0xc5926c`

- Decompiled symbol: `CFUtils_ClampPerAxisInsideUnitSquare`
- Metadata signature: `public static Vector2 ClampPerAxisInsideUnitSquare(Vector2 np) { }`
- Native interval: `36` bytes
- Result: `pseudocode`

```c
long long CFUtils_ClampPerAxisInsideUnitSquare(void)
{
    unsigned int v0;  // s0
    unsigned long v1;  // 4137
    unsigned int v2;  // s1
    unsigned long v3;  // 4129
    unsigned long v4;  // x0
    unsigned long v5;  // x0

    v1 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v0, 0xbf800000)) >> 5 & 3 | (unsigned long long)(CmpF(v0, 0xbf800000) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v0, 0xbf800000)) >> 5 & 3 | (unsigned long long)(CmpF(v0, 0xbf800000) & 1)) & ((unsigned long long)(char)(CmpF(v0, 0xbf800000)) >> 5 & 3 | (unsigned long long)(CmpF(v0, 0xbf800000) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    v3 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v2, 0xbf800000)) >> 5 & 3 | (unsigned long long)(CmpF(v2, 0xbf800000) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v2, 0xbf800000)) >> 5 & 3 | (unsigned long long)(CmpF(v2, 0xbf800000) & 1)) & ((unsigned long long)(char)(CmpF(v2, 0xbf800000)) >> 5 & 3 | (unsigned long long)(CmpF(v2, 0xbf800000) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if (!((char)v3))
        return v5;
    return v4;
}
```

## `CFUtils.IsDirDiagonal` — RVA `0xc59290`

- Decompiled symbol: `CFUtils_IsDirDiagonal`
- Metadata signature: `public static bool IsDirDiagonal(Dir dir) { }`
- Native interval: `12` bytes
- Result: `pseudocode`

```c
unsigned int CFUtils_IsDirDiagonal(unsigned int a0)
{
    unsigned long v0;  // 4112

    v0 = arm64g_calculate_condition(25, (unsigned long long)(a0 & 1), 0, 0);
    if (!((char)v0))
        return 1;
    return 0;
}
```

## `CFUtils.VecToAngle` — RVA `0xc5929c`

- Decompiled symbol: `CFUtils_VecToAngle`
- Metadata signature: `public static float VecToAngle(Vector2 vec) { }`
- Native interval: `28` bytes
- Result: `pseudocode`

```c
void CFUtils_VecToAngle(void)
{
    CFUtils__NormalizeAnglePositive(atan2f());
    return;
}
```

## `CFUtils.NormalizeAnglePositive` — RVA `0xc592b8`

- Decompiled symbol: `CFUtils_NormalizeAnglePositive`
- Metadata signature: `public static float NormalizeAnglePositive(float a) { }`
- Native interval: `140` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: Decompiler produced no C-like text

```c
// 0x10592b8: mov w8, #0x43b40000
// 0x10592bc: fmov s1, w8
// 0x10592c0: fcmp s0, s1
// 0x10592c4: b.ge #0x1059318
// 0x10592c8: fcmp s0, #0.0
// 0x10592cc: b.ge #0x1059314
// 0x10592d0: mov w8, #-0x3c4c0000
// 0x10592d4: fmov s1, w8
// 0x10592d8: fcmp s0, s1
// 0x10592dc: b.hi #0x1059308
// 0x10592e0: mov w8, #0x43b40000
// 0x10592e4: fmov s1, w8
// 0x10592e8: fdiv s2, s0, s1
// 0x10592ec: frintm s2, s2
// 0x10592f0: fmul s2, s2, s1
// 0x10592f4: fsub s0, s0, s2
// 0x10592f8: fmin s1, s0, s1
// 0x10592fc: fcmp s0, #0.0
// 0x1059300: fmov s0, wzr
// 0x1059304: fcsel s0, s1, s0, pl
// 0x1059308: mov w8, #0x43b40000
// 0x105930c: fmov s1, w8
// 0x1059310: fadd s0, s0, s1
// 0x1059314: ret
// 0x1059318: mov w8, #0x43b40000
// 0x105931c: fmov s1, w8
// 0x1059320: fdiv s2, s0, s1
// 0x1059324: frintm s2, s2
// 0x1059328: fmul s2, s2, s1
// 0x105932c: fsub s0, s0, s2
// 0x1059330: fmin s1, s0, s1
// 0x1059334: fcmp s0, #0.0
// 0x1059338: fmov s0, wzr
// 0x105933c: fcsel s0, s1, s0, pl
// 0x1059340: ret
```

## `CFUtils.VecToAngle` — RVA `0xc59344`

- Decompiled symbol: `CFUtils_VecToAngle`
- Metadata signature: `public static float VecToAngle(Vector2 vec, float defaultAngle, float deadZoneSq) { }`
- Native interval: `268` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: Decompiler produced no C-like text

```c
// 0x1059344: str d10, [sp, #-0x30]!
// 0x1059348: stp d9, d8, [sp, #0x10]
// 0x105934c: stp x30, x19, [sp, #0x20]
// 0x1059350: mov v8.16b, v1.16b
// 0x1059354: mov v9.16b, v0.16b
// 0x1059358: fmul s0, s0, s0
// 0x105935c: fmul s1, s1, s1
// 0x1059360: fadd s10, s0, s1
// 0x1059364: fcmp s10, s3
// 0x1059368: b.mi #0x10593e0
// 0x105936c: adrp x8, #0x832000
// 0x1059370: ldr s0, [x8, #0x2e8]
// 0x1059374: fmov s1, #-1.00000000
// 0x1059378: fadd s1, s10, s1
// 0x105937c: fabs s1, s1
// 0x1059380: fcmp s1, s0
// 0x1059384: b.le #0x1059428
// 0x1059388: adrp x19, #0x1fab000
// 0x105938c: ldrb w8, [x19, #0x243]
// 0x1059390: cbnz w8, #0x10593a8
// 0x1059394: adrp x0, #0x1e8c000
// 0x1059398: ldr x0, [x0, #0xa60]
// 0x105939c: bl #0xf7d92c
// 0x10593a0: mov w8, #1
// 0x10593a4: strb w8, [x19, #0x243]
// 0x10593a8: adrp x8, #0x1e8c000
// 0x10593ac: ldr x8, [x8, #0xa60]
// 0x10593b0: ldr x0, [x8]
// 0x10593b4: ldr w8, [x0, #0xe0]
// 0x10593b8: cbnz w8, #0x10593c0
// 0x10593bc: bl #0xf7da5c
// 0x10593c0: adrp x8, #0x832000
// 0x10593c4: ldr s1, [x8, #0x41c]
// 0x10593c8: fsqrt s0, s10
// 0x10593cc: fcmp s0, s1
// 0x10593d0: b.le #0x10593f4
// 0x10593d4: fdiv s9, s9, s0
// 0x10593d8: fdiv s8, s8, s0
// 0x10593dc: b #0x1059428
// 0x10593e0: ldp x30, x19, [sp, #0x20]
// 0x10593e4: ldp d9, d8, [sp, #0x10]
// 0x10593e8: mov v0.16b, v2.16b
// 0x10593ec: ldr d10, [sp], #0x30
// 0x10593f0: ret
// 0x10593f4: adrp x19, #0x1fab000
// 0x10593f8: ldrb w8, [x19, #0x1e0]
// 0x10593fc: cbnz w8, #0x1059414
// 0x1059400: adrp x0, #0x1e8c000
// 0x1059404: ldr x0, [x0, #0x138]
// 0x1059408: bl #0xf7d92c
// 0x105940c: mov w8, #1
// 0x1059410: strb w8, [x19, #0x1e0]
// 0x1059414: adrp x8, #0x1e8c000
// 0x1059418: ldr x8, [x8, #0x138]
// 0x105941c: ldr x8, [x8]
// 0x1059420: ldr x8, [x8, #0xb8]
// 0x1059424: ldp s9, s8, [x8]
// 0x1059428: mov v0.16b, v9.16b
// 0x105942c: mov v1.16b, v8.16b
// 0x1059430: bl #0x1db0c90
// 0x1059434: adrp x8, #0x832000
// 0x1059438: ldr s1, [x8, #0x554]
// 0x105943c: ldp x30, x19, [sp, #0x20]
// 0x1059440: ldp d9, d8, [sp, #0x10]
// 0x1059444: fmul s0, s0, s1
// 0x1059448: ldr d10, [sp], #0x30
// 0x105944c: b #0x10592b8
```

## `CFUtils.DirToAngle` — RVA `0xc59450`

- Decompiled symbol: `CFUtils_DirToAngle`
- Metadata signature: `public static float DirToAngle(Dir d) { }`
- Native interval: `36` bytes
- Result: `pseudocode`

```c
long long CFUtils_DirToAngle(unsigned long a0)
{
    if ((unsigned int)a0 - 1 >= 8)
        return a0;
    return a0;
}
```

## `CFUtils.DirFromAngle` — RVA `0xc59474`

- Decompiled symbol: `CFUtils_DirFromAngle`
- Metadata signature: `public static Dir DirFromAngle(float ang, bool as8way) { }`
- Native interval: `280` bytes
- Result: `pseudocode`

```c
unsigned int CFUtils_DirFromAngle(unsigned int a0)
{
    unsigned long v10;  // 4128
    unsigned long v11;  // 4128
    unsigned long v12;  // 4137
    unsigned int v13;  // w0
    unsigned long v14;  // 4128
    unsigned long v15;  // 4128
    unsigned long v16;  // 4136
    unsigned int v17;  // w0
    unsigned long v2;  // 4127
    unsigned int v3;  // s1
    unsigned int v4;  // s0
    unsigned int v5;  // s0
    unsigned long v6;  // 4128
    unsigned long v7;  // 4128
    unsigned long v8;  // 4128
    unsigned long v9;  // 4128

    v2 = arm64g_calculate_condition(25, (unsigned long long)(a0 & 1), 0, 0);
    if ((char)v2)
        v3 = 0x41b40000;
    else
        v3 = 0x42340000;
    v5 = v3 + v4;
    CFUtils__NormalizeAnglePositive();
    if (((char)a0 & 1))
    {
        v6 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(v5, 0x42340000)) >> 5 & 3 | (unsigned long long)(CmpF(v5, 0x42340000) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v5, 0x42340000)) >> 5 & 3 | (unsigned long long)(CmpF(v5, 0x42340000) & 1)) & ((unsigned long long)(char)(CmpF(v5, 0x42340000)) >> 5 & 3 | (unsigned long long)(CmpF(v5, 0x42340000) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if ((char)v6)
            return 1;
        v7 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(v5, 0x42b40000)) >> 5 & 3 | (unsigned long long)(CmpF(v5, 0x42b40000) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v5, 0x42b40000)) >> 5 & 3 | (unsigned long long)(CmpF(v5, 0x42b40000) & 1)) & ((unsigned long long)(char)(CmpF(v5, 0x42b40000)) >> 5 & 3 | (unsigned long long)(CmpF(v5, 0x42b40000) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if ((char)v7)
            return 2;
        v8 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(v5, 0x43070000)) >> 5 & 3 | (unsigned long long)(CmpF(v5, 0x43070000) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v5, 0x43070000)) >> 5 & 3 | (unsigned long long)(CmpF(v5, 0x43070000) & 1)) & ((unsigned long long)(char)(CmpF(v5, 0x43070000)) >> 5 & 3 | (unsigned long long)(CmpF(v5, 0x43070000) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if (!((char)v8))
        {
            v9 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(v5, 0x43340000)) >> 5 & 3 | (unsigned long long)(CmpF(v5, 0x43340000) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v5, 0x43340000)) >> 5 & 3 | (unsigned long long)(CmpF(v5, 0x43340000) & 1)) & ((unsigned long long)(char)(CmpF(v5, 0x43340000)) >> 5 & 3 | (unsigned long long)(CmpF(v5, 0x43340000) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
            if ((char)v9)
                return 4;
            v10 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(v5, 0x43610000)) >> 5 & 3 | (unsigned long long)(CmpF(v5, 0x43610000) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v5, 0x43610000)) >> 5 & 3 | (unsigned long long)(CmpF(v5, 0x43610000) & 1)) & ((unsigned long long)(char)(CmpF(v5, 0x43610000)) >> 5 & 3 | (unsigned long long)(CmpF(v5, 0x43610000) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
            if ((char)v10)
                return 5;
            v11 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(v5, 0x43870000)) >> 5 & 3 | (unsigned long long)(CmpF(v5, 0x43870000) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v5, 0x43870000)) >> 5 & 3 | (unsigned long long)(CmpF(v5, 0x43870000) & 1)) & ((unsigned long long)(char)(CmpF(v5, 0x43870000)) >> 5 & 3 | (unsigned long long)(CmpF(v5, 0x43870000) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
            if ((char)v11)
                return 6;
            v12 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v5, 0x439d8000)) >> 5 & 3 | (unsigned long long)(CmpF(v5, 0x439d8000) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v5, 0x439d8000)) >> 5 & 3 | (unsigned long long)(CmpF(v5, 0x439d8000) & 1)) & ((unsigned long long)(char)(CmpF(v5, 0x439d8000)) >> 5 & 3 | (unsigned long long)(CmpF(v5, 0x439d8000) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
            if ((char)v12)
                v13 = 8;
            else
                v13 = 7;
            return v13;
        }
    }
    else
    {
        v14 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(v5, 0x42b40000)) >> 5 & 3 | (unsigned long long)(CmpF(v5, 0x42b40000) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v5, 0x42b40000)) >> 5 & 3 | (unsigned long long)(CmpF(v5, 0x42b40000) & 1)) & ((unsigned long long)(char)(CmpF(v5, 0x42b40000)) >> 5 & 3 | (unsigned long long)(CmpF(v5, 0x42b40000) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if ((char)v14)
            return 1;
        v15 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(v5, 0x43340000)) >> 5 & 3 | (unsigned long long)(CmpF(v5, 0x43340000) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v5, 0x43340000)) >> 5 & 3 | (unsigned long long)(CmpF(v5, 0x43340000) & 1)) & ((unsigned long long)(char)(CmpF(v5, 0x43340000)) >> 5 & 3 | (unsigned long long)(CmpF(v5, 0x43340000) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if (!((char)v15))
        {
            v16 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v5, 0x43870000)) >> 5 & 3 | (unsigned long long)(CmpF(v5, 0x43870000) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v5, 0x43870000)) >> 5 & 3 | (unsigned long long)(CmpF(v5, 0x43870000) & 1)) & ((unsigned long long)(char)(CmpF(v5, 0x43870000)) >> 5 & 3 | (unsigned long long)(CmpF(v5, 0x43870000) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
            if ((char)v16)
                v17 = 7;
            else
                v17 = 5;
            return v17;
        }
    }
    return 3;
}
```

## `CFUtils.DirFromAngleEx` — RVA `0xc5958c`

- Decompiled symbol: `CFUtils_DirFromAngleEx`
- Metadata signature: `public static Dir DirFromAngleEx(float ang, bool as8way, Dir lastDir, float magnetPow) { }`
- Native interval: `196` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: Decompiler produced no C-like text

```c
// 0x105958c: cbz w1, #0x1059648
// 0x1059590: adrp x8, #0x832000
// 0x1059594: ldr s2, [x8, #0x534]
// 0x1059598: fcmp s1, s2
// 0x105959c: b.le #0x1059648
// 0x10595a0: sub w8, w1, #1
// 0x10595a4: mov w9, #0x42340000
// 0x10595a8: fmov s3, w9
// 0x10595ac: scvtf s4, w8
// 0x10595b0: fmov s2, wzr
// 0x10595b4: cmp w8, #8
// 0x10595b8: fmul s4, s4, s3
// 0x10595bc: mov w9, #0x43b40000
// 0x10595c0: fmov s5, #1.00000000
// 0x10595c4: fcsel s4, s4, s2, lo
// 0x10595c8: fmov s6, #0.50000000
// 0x10595cc: fmov s7, w9
// 0x10595d0: fmin s17, s1, s5
// 0x10595d4: fsub s4, s4, s0
// 0x10595d8: mov w8, #-0x3c4c0000
// 0x10595dc: fmul s6, s17, s6
// 0x10595e0: fdiv s17, s4, s7
// 0x10595e4: fmov s16, w8
// 0x10595e8: frintm s17, s17
// 0x10595ec: fmul s17, s17, s16
// 0x10595f0: fadd s4, s4, s17
// 0x10595f4: fmin s7, s4, s7
// 0x10595f8: fcmp s4, #0.0
// 0x10595fc: mov w8, #0x43340000
// 0x1059600: fcsel s2, s7, s2, pl
// 0x1059604: fmov s4, w8
// 0x1059608: fadd s7, s2, s16
// 0x105960c: fcmp s2, s4
// 0x1059610: mov w9, #0x41b40000
// 0x1059614: fadd s6, s6, s5
// 0x1059618: fcsel s2, s7, s2, gt
// 0x105961c: fcmp s1, #0.0
// 0x1059620: fabs s1, s2
// 0x1059624: fcsel s2, s6, s5, pl
// 0x1059628: tst w0, #1
// 0x105962c: fmov s4, w9
// 0x1059630: fcsel s3, s4, s3, ne
// 0x1059634: fmul s2, s3, s2
// 0x1059638: fcmp s1, s2
// 0x105963c: b.pl #0x1059648
// 0x1059640: mov w0, w1
// 0x1059644: ret
// 0x1059648: and w0, w0, #1
// 0x105964c: b #0x1059474
```

## `CFUtils.DirDeltaAngle` — RVA `0xc59650`

- Decompiled symbol: `CFUtils_DirDeltaAngle`
- Metadata signature: `public static int DirDeltaAngle(Dir dirFrom, Dir dirTo) { }`
- Native interval: `352` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: Decompiler produced no C-like text

```c
// 0x1059650: mov w8, w0
// 0x1059654: mov w0, wzr
// 0x1059658: cbz w8, #0x10597ac
// 0x105965c: cbz w1, #0x10597ac
// 0x1059660: sub sp, sp, #0x30
// 0x1059664: stp d9, d8, [sp, #0x10]
// 0x1059668: stp x30, x19, [sp, #0x20]
// 0x105966c: sub w8, w8, #1
// 0x1059670: mov w9, #0x42340000
// 0x1059674: sub w10, w1, #1
// 0x1059678: fmov s1, w9
// 0x105967c: scvtf s2, w8
// 0x1059680: fmov s0, wzr
// 0x1059684: cmp w8, #8
// 0x1059688: scvtf s4, w10
// 0x105968c: fmul s2, s2, s1
// 0x1059690: fmul s1, s4, s1
// 0x1059694: fcsel s2, s2, s0, lo
// 0x1059698: cmp w10, #8
// 0x105969c: mov w9, #0x43b40000
// 0x10596a0: fcsel s1, s1, s0, lo
// 0x10596a4: fmov s3, w9
// 0x10596a8: fsub s1, s1, s2
// 0x10596ac: mov w8, #-0x3c4c0000
// 0x10596b0: fdiv s2, s1, s3
// 0x10596b4: fmov s4, w8
// 0x10596b8: frintm s2, s2
// 0x10596bc: fmul s2, s2, s4
// 0x10596c0: adrp x19, #0x1fab000
// 0x10596c4: fadd s1, s1, s2
// 0x10596c8: mov w9, #0x43340000
// 0x10596cc: ldrb w8, [x19, #0x242]
// 0x10596d0: fmin s3, s1, s3
// 0x10596d4: fcmp s1, #0.0
// 0x10596d8: fmov s2, w9
// 0x10596dc: fcsel s0, s3, s0, pl
// 0x10596e0: fadd s1, s0, s4
// 0x10596e4: fcmp s0, s2
// 0x10596e8: fcsel s9, s1, s0, gt
// 0x10596ec: cbnz w8, #0x1059704
// 0x10596f0: adrp x0, #0x1e8c000
// 0x10596f4: ldr x0, [x0, #0xa60]
// 0x10596f8: bl #0xf7d92c
// 0x10596fc: mov w8, #1
// 0x1059700: strb w8, [x19, #0x242]
// 0x1059704: adrp x8, #0x1e8c000
// 0x1059708: ldr x8, [x8, #0xa60]
// 0x105970c: ldr x0, [x8]
// 0x1059710: ldr w8, [x0, #0xe0]
// 0x1059714: cbnz w8, #0x105971c
// 0x1059718: bl #0xf7da5c
// 0x105971c: fcvt d8, s9
// 0x1059720: add x0, sp, #8
// 0x1059724: mov v0.16b, v8.16b
// 0x1059728: bl #0x1db0c60
// 0x105972c: fcmp s9, #0.0
// 0x1059730: b.ge #0x105974c
// 0x1059734: fmov d1, #-0.50000000
// 0x1059738: fcmp d0, d1
// 0x105973c: b.ne #0x1059774
// 0x1059740: ldr d0, [sp, #8]
// 0x1059744: fmov d1, #-1.00000000
// 0x1059748: b #0x1059760
// 0x105974c: fmov d1, #0.50000000
// 0x1059750: fcmp d0, d1
// 0x1059754: b.ne #0x1059780
// 0x1059758: ldr d0, [sp, #8]
// 0x105975c: fmov d1, #1.00000000
// 0x1059760: fcvtzs x8, d0
// 0x1059764: fadd d1, d0, d1
// 0x1059768: tst x8, #1
// 0x105976c: fcsel d0, d0, d1, eq
// 0x1059770: b #0x1059788
// 0x1059774: fadd d0, d8, d1
// 0x1059778: frintp d0, d0
// 0x105977c: b #0x1059788
// 0x1059780: fadd d0, d8, d1
// 0x1059784: frintm d0, d0
// 0x1059788: mov x8, #0x7ff0000000000000
// 0x105978c: ldp x30, x19, [sp, #0x20]
// 0x1059790: ldp d9, d8, [sp, #0x10]
// 0x1059794: fmov d1, x8
// 0x1059798: fcvtzs w9, d0
// 0x105979c: fcmp d0, d1
// 0x10597a0: mov w8, #-0x80000000
// 0x10597a4: csel w0, w8, w9, eq
// 0x10597a8: add sp, sp, #0x30
// 0x10597ac: ret
```

## `CFUtils.DirToNormal` — RVA `0xc597b0`

- Decompiled symbol: `CFUtils_DirToNormal`
- Metadata signature: `public static Vector2 DirToNormal(Dir dir) { }`
- Native interval: `112` bytes
- Result: `pseudocode`

```c
extern long long g_1ef22b8;
extern char g_1fab1e0;

unsigned long long CFUtils_DirToNormal(unsigned long long a0)
{
    if (8 > (unsigned int)a0 - 1)
        return a0;
    if (!g_1fab1e0)
    {
        a0 = sub_f7d92c(&g_1ef22b8);
        g_1fab1e0 = 1;
    }
    return a0;
}
```

## `CFUtils.DirToTangent` — RVA `0xc59820`

- Decompiled symbol: `CFUtils_DirToTangent`
- Metadata signature: `public static Vector2 DirToTangent(Dir dir) { }`
- Native interval: `112` bytes
- Result: `pseudocode`

```c
extern long long g_1ef22b8;
extern char g_1fab1e0;

unsigned long long CFUtils_DirToTangent(unsigned long long a0)
{
    if (8 > (unsigned int)a0 - 1)
        return a0;
    if (!g_1fab1e0)
    {
        a0 = sub_f7d92c(&g_1ef22b8);
        g_1fab1e0 = 1;
    }
    return a0;
}
```

## `CFUtils.GetOppositeDir` — RVA `0xc59890`

- Decompiled symbol: `CFUtils_GetOppositeDir`
- Metadata signature: `public static Dir GetOppositeDir(Dir dir) { }`
- Native interval: `36` bytes
- Result: `pseudocode`

```c
extern unsigned int g_852220[4];

unsigned int CFUtils_GetOppositeDir(unsigned int a0)
{
    if (7 < a0 - 1)
        return 0;
    return g_852220[1 + a0];
}
```

## `CFUtils.DirToVector` — RVA `0xc598b4`

- Decompiled symbol: `CFUtils_DirToVector`
- Metadata signature: `public static Vector2 DirToVector(Dir dir, bool circular) { }`
- Native interval: `464` bytes
- Result: `pseudocode`

```c
extern long long g_1ef22b8;
extern char g_1fab1e0;
extern char g_852120;

unsigned long long CFUtils_DirToVector(unsigned long long a0)
{
    unsigned long long v0;  // x0

    if (7 >= (unsigned int)a0 - 1)
    {
        goto sub_10598e8 + (&g_852120)[1 + a0] * 4;
    }
    else if (!g_1fab1e0)
    {
        v0 = sub_f7d92c(&g_1ef22b8);
        g_1fab1e0 = 1;
        return v0;
    }
    else
    {
        return a0;
    }
}
```

## `CFUtils.VecToDir` — RVA `0xc59a84`

- Decompiled symbol: `CFUtils_VecToDir`
- Metadata signature: `public static Dir VecToDir(Vector2 vec, bool as8way) { }`
- Native interval: `40` bytes
- Result: `pseudocode`

```c
unsigned int CFUtils_VecToDir(unsigned int a0)
{
    atan2f();
    CFUtils__NormalizeAnglePositive();
    return CFUtils__DirFromAngle(a0 & 1);
}
```

## `CFUtils.VecToDir` — RVA `0xc59aac`

- Decompiled symbol: `CFUtils_VecToDir`
- Metadata signature: `public static Dir VecToDir(Vector2 vec, Dir defaultDir, float deadZoneSq, bool as8way) { }`
- Native interval: `280` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: Decompiler produced no C-like text

```c
// 0x1059aac: stp d11, d10, [sp, #-0x40]!
// 0x1059ab0: stp d9, d8, [sp, #0x10]
// 0x1059ab4: str x30, [sp, #0x20]
// 0x1059ab8: stp x20, x19, [sp, #0x30]
// 0x1059abc: mov v8.16b, v1.16b
// 0x1059ac0: mov v9.16b, v0.16b
// 0x1059ac4: fmul s0, s0, s0
// 0x1059ac8: fmul s1, s1, s1
// 0x1059acc: fadd s10, s0, s1
// 0x1059ad0: fcmp s10, s2
// 0x1059ad4: b.ls #0x1059b48
// 0x1059ad8: adrp x8, #0x832000
// 0x1059adc: ldr s11, [x8, #0x41c]
// 0x1059ae0: fmov s0, #-1.00000000
// 0x1059ae4: fadd s0, s10, s0
// 0x1059ae8: fabs s0, s0
// 0x1059aec: mov w19, w1
// 0x1059af0: fcmp s0, s11
// 0x1059af4: b.le #0x1059b90
// 0x1059af8: adrp x20, #0x1fab000
// 0x1059afc: ldrb w8, [x20, #0x243]
// 0x1059b00: cbnz w8, #0x1059b18
// 0x1059b04: adrp x0, #0x1e8c000
// 0x1059b08: ldr x0, [x0, #0xa60]
// 0x1059b0c: bl #0xf7d92c
// 0x1059b10: mov w8, #1
// 0x1059b14: strb w8, [x20, #0x243]
// 0x1059b18: adrp x8, #0x1e8c000
// 0x1059b1c: ldr x8, [x8, #0xa60]
// 0x1059b20: ldr x0, [x8]
// 0x1059b24: ldr w8, [x0, #0xe0]
// 0x1059b28: cbnz w8, #0x1059b30
// 0x1059b2c: bl #0xf7da5c
// 0x1059b30: fsqrt s0, s10
// 0x1059b34: fcmp s0, s11
// 0x1059b38: b.le #0x1059b5c
// 0x1059b3c: fdiv s9, s9, s0
// 0x1059b40: fdiv s8, s8, s0
// 0x1059b44: b #0x1059b90
// 0x1059b48: ldp x20, x19, [sp, #0x30]
// 0x1059b4c: ldr x30, [sp, #0x20]
// 0x1059b50: ldp d9, d8, [sp, #0x10]
// 0x1059b54: ldp d11, d10, [sp], #0x40
// 0x1059b58: ret
// 0x1059b5c: adrp x20, #0x1fab000
// 0x1059b60: ldrb w8, [x20, #0x1e0]
// 0x1059b64: cbnz w8, #0x1059b7c
// 0x1059b68: adrp x0, #0x1e8c000
// 0x1059b6c: ldr x0, [x0, #0x138]
// 0x1059b70: bl #0xf7d92c
// 0x1059b74: mov w8, #1
// 0x1059b78: strb w8, [x20, #0x1e0]
// 0x1059b7c: adrp x8, #0x1e8c000
// 0x1059b80: ldr x8, [x8, #0x138]
// 0x1059b84: ldr x8, [x8]
// 0x1059b88: ldr x8, [x8, #0xb8]
// 0x1059b8c: ldp s9, s8, [x8]
// 0x1059b90: mov v0.16b, v9.16b
// 0x1059b94: mov v1.16b, v8.16b
// 0x1059b98: bl #0x1db0c90
// 0x1059b9c: adrp x8, #0x832000
// 0x1059ba0: ldr s1, [x8, #0x554]
// 0x1059ba4: fmul s0, s0, s1
// 0x1059ba8: bl #0x10592b8
// 0x1059bac: and w0, w19, #1
// 0x1059bb0: ldp x20, x19, [sp, #0x30]
// 0x1059bb4: ldr x30, [sp, #0x20]
// 0x1059bb8: ldp d9, d8, [sp, #0x10]
// 0x1059bbc: ldp d11, d10, [sp], #0x40
// 0x1059bc0: b #0x1059474
```

## `CFUtils.DigitalToDir` — RVA `0xc59bc4`

- Decompiled symbol: `CFUtils_DigitalToDir`
- Metadata signature: `public static Dir DigitalToDir(bool digiU, bool digiR, bool digiD, bool digiL) { }`
- Native interval: `116` bytes
- Result: `pseudocode`

```c
unsigned int CFUtils_DigitalToDir(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3)
{
    unsigned int v0;  // w9
    unsigned int v1;  // w11
    unsigned long v9;  // 4106
    unsigned long v10;  // 4106
    unsigned int v11;  // w11
    unsigned int v12;  // w10
    unsigned long v13;  // cc_dep1
    unsigned long v14;  // 4115
    unsigned int v15;  // w8
    unsigned long v16;  // 4108
    unsigned long v17;  // 4108
    unsigned long v18;  // 4115
    unsigned int v2;  // w10
    unsigned int v3;  // w8
    unsigned long v4;  // 4115
    unsigned int v5;  // w9
    unsigned long v6;  // 4116
    unsigned long v7;  // cc_dep1
    unsigned long v8;  // 4129

    v0 = a0 & a2;
    v1 = a1 & a3;
    v2 = v1 ^ a3;
    v3 = v1 ^ a1;
    if ((v0 & 1) != (a0 & 1))
    {
        v4 = arm64g_calculate_condition(25, (unsigned long long)(v2 & 1), 0, 0);
        if ((char)v4)
            v5 = 8;
        else
            v5 = 1;
        v6 = arm64g_calculate_condition(25, (unsigned long long)(v3 & 1), 0, 0);
        if (!((char)v6))
            return v5;
        return 2;
    }
    else
    {
        v7 = v2 & 1;
        v8 = arm64g_calculate_condition(9, (unsigned long long)(v2 & 1), 0, 0);
        if ((char)v8)
        {
            v12 = 5;
            v9 = arm64g_calculate_condition(25, v7, 0, 0);
            if (!((char)v9))
                goto LABEL_1059c1e;
LABEL_1059c1d:
            v11 = 7;
        }
        else
        {
            v12 = 6;
            v10 = arm64g_calculate_condition(25, v7, 0, 0);
            if ((char)v10)
                goto LABEL_1059c1d;
LABEL_1059c1e:
            v11 = 0;
        }
        v13 = v3 & 1;
        v14 = arm64g_calculate_condition(25, (unsigned long long)(v3 & 1), 0, 0);
        if ((char)v14)
        {
            v15 = 4;
            v16 = arm64g_calculate_condition(25, v13, 0, 0);
            if (!((char)v16))
                goto LABEL_1059c2a;
LABEL_1059c29:
            v11 = 3;
        }
        else
        {
            v15 = v12;
            v17 = arm64g_calculate_condition(25, v13, 0, 0);
            if ((char)v17)
                goto LABEL_1059c29;
LABEL_1059c2a:
        }
        v18 = arm64g_calculate_condition(25, (unsigned long long)((v0 ^ a2) & 1), 0, 0);
        if (!((char)v18))
            return v11;
        return v15;
    }
}
```

## `CFUtils.CircularToSquareJoystickVec` — RVA `0xc59c38`

- Decompiled symbol: `CFUtils_CircularToSquareJoystickVec`
- Metadata signature: `public static Vector2 CircularToSquareJoystickVec(Vector2 circularVec) { }`
- Native interval: `304` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: Decompiler produced no C-like text

```c
// 0x1059c38: stp d11, d10, [sp, #-0x30]!
// 0x1059c3c: stp d9, d8, [sp, #0x10]
// 0x1059c40: stp x30, x19, [sp, #0x20]
// 0x1059c44: adrp x8, #0x832000
// 0x1059c48: ldr s10, [x8, #0x41c]
// 0x1059c4c: mov v8.16b, v1.16b
// 0x1059c50: mov v9.16b, v0.16b
// 0x1059c54: fmul s0, s0, s0
// 0x1059c58: fmul s1, s1, s1
// 0x1059c5c: fadd s11, s0, s1
// 0x1059c60: fcmp s11, s10
// 0x1059c64: b.pl #0x1059ca0
// 0x1059c68: adrp x19, #0x1fab000
// 0x1059c6c: ldrb w8, [x19, #0x1e0]
// 0x1059c70: cbnz w8, #0x1059c88
// 0x1059c74: adrp x0, #0x1e8c000
// 0x1059c78: ldr x0, [x0, #0x138]
// 0x1059c7c: bl #0xf7d92c
// 0x1059c80: mov w8, #1
// 0x1059c84: strb w8, [x19, #0x1e0]
// 0x1059c88: adrp x8, #0x1e8c000
// 0x1059c8c: ldr x8, [x8, #0x138]
// 0x1059c90: ldr x8, [x8]
// 0x1059c94: ldr x8, [x8, #0xb8]
// 0x1059c98: ldp s0, s1, [x8]
// 0x1059c9c: b #0x1059d58
// 0x1059ca0: adrp x19, #0x1fab000
// 0x1059ca4: ldrb w8, [x19, #0x243]
// 0x1059ca8: cbnz w8, #0x1059cc0
// 0x1059cac: adrp x0, #0x1e8c000
// 0x1059cb0: ldr x0, [x0, #0xa60]
// 0x1059cb4: bl #0xf7d92c
// 0x1059cb8: mov w8, #1
// 0x1059cbc: strb w8, [x19, #0x243]
// 0x1059cc0: adrp x8, #0x1e8c000
// 0x1059cc4: ldr x8, [x8, #0xa60]
// 0x1059cc8: ldr x0, [x8]
// 0x1059ccc: ldr w8, [x0, #0xe0]
// 0x1059cd0: cbnz w8, #0x1059cd8
// 0x1059cd4: bl #0xf7da5c
// 0x1059cd8: fsqrt s1, s11
// 0x1059cdc: fcmp s1, s10
// 0x1059ce0: b.le #0x1059cf0
// 0x1059ce4: fdiv s0, s9, s1
// 0x1059ce8: fdiv s1, s8, s1
// 0x1059cec: b #0x1059d24
// 0x1059cf0: adrp x19, #0x1fab000
// 0x1059cf4: ldrb w8, [x19, #0x1e0]
// 0x1059cf8: cbnz w8, #0x1059d10
// 0x1059cfc: adrp x0, #0x1e8c000
// 0x1059d00: ldr x0, [x0, #0x138]
// 0x1059d04: bl #0xf7d92c
// 0x1059d08: mov w8, #1
// 0x1059d0c: strb w8, [x19, #0x1e0]
// 0x1059d10: adrp x8, #0x1e8c000
// 0x1059d14: ldr x8, [x8, #0x138]
// 0x1059d18: ldr x8, [x8]
// 0x1059d1c: ldr x8, [x8, #0xb8]
// 0x1059d20: ldp s0, s1, [x8]
// 0x1059d24: fabs s0, s0
// 0x1059d28: fabs s3, s1
// 0x1059d2c: fadd s0, s0, s3
// 0x1059d30: fmov s2, #1.00000000
// 0x1059d34: fmov s1, #-1.00000000
// 0x1059d38: fmul s4, s9, s0
// 0x1059d3c: fmul s3, s8, s0
// 0x1059d40: fmin s0, s4, s2
// 0x1059d44: fcmp s4, s1
// 0x1059d48: fcsel s0, s0, s1, pl
// 0x1059d4c: fcmp s3, s1
// 0x1059d50: b.mi #0x1059d58
// 0x1059d54: fmin s1, s3, s2
// 0x1059d58: ldp x30, x19, [sp, #0x20]
// 0x1059d5c: ldp d9, d8, [sp, #0x10]
// 0x1059d60: ldp d11, d10, [sp], #0x30
// 0x1059d64: ret
```

## `CFUtils.SquareToCircularJoystickVec` — RVA `0xc59d68`

- Decompiled symbol: `CFUtils_SquareToCircularJoystickVec`
- Metadata signature: `public static Vector2 SquareToCircularJoystickVec(Vector2 squareVec) { }`
- Native interval: `304` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: Decompiler produced no C-like text

```c
// 0x1059d68: stp d11, d10, [sp, #-0x30]!
// 0x1059d6c: stp d9, d8, [sp, #0x10]
// 0x1059d70: stp x30, x19, [sp, #0x20]
// 0x1059d74: adrp x8, #0x832000
// 0x1059d78: ldr s10, [x8, #0x41c]
// 0x1059d7c: mov v8.16b, v1.16b
// 0x1059d80: mov v9.16b, v0.16b
// 0x1059d84: fmul s0, s0, s0
// 0x1059d88: fmul s1, s1, s1
// 0x1059d8c: fadd s11, s0, s1
// 0x1059d90: fcmp s11, s10
// 0x1059d94: b.pl #0x1059dd0
// 0x1059d98: adrp x19, #0x1fab000
// 0x1059d9c: ldrb w8, [x19, #0x1e0]
// 0x1059da0: cbnz w8, #0x1059db8
// 0x1059da4: adrp x0, #0x1e8c000
// 0x1059da8: ldr x0, [x0, #0x138]
// 0x1059dac: bl #0xf7d92c
// 0x1059db0: mov w8, #1
// 0x1059db4: strb w8, [x19, #0x1e0]
// 0x1059db8: adrp x8, #0x1e8c000
// 0x1059dbc: ldr x8, [x8, #0x138]
// 0x1059dc0: ldr x8, [x8]
// 0x1059dc4: ldr x8, [x8, #0xb8]
// 0x1059dc8: ldp s0, s1, [x8]
// 0x1059dcc: b #0x1059e88
// 0x1059dd0: adrp x19, #0x1fab000
// 0x1059dd4: ldrb w8, [x19, #0x243]
// 0x1059dd8: cbnz w8, #0x1059df0
// 0x1059ddc: adrp x0, #0x1e8c000
// 0x1059de0: ldr x0, [x0, #0xa60]
// 0x1059de4: bl #0xf7d92c
// 0x1059de8: mov w8, #1
// 0x1059dec: strb w8, [x19, #0x243]
// 0x1059df0: adrp x8, #0x1e8c000
// 0x1059df4: ldr x8, [x8, #0xa60]
// 0x1059df8: ldr x0, [x8]
// 0x1059dfc: ldr w8, [x0, #0xe0]
// 0x1059e00: cbnz w8, #0x1059e08
// 0x1059e04: bl #0xf7da5c
// 0x1059e08: fsqrt s1, s11
// 0x1059e0c: fcmp s1, s10
// 0x1059e10: b.le #0x1059e20
// 0x1059e14: fdiv s0, s9, s1
// 0x1059e18: fdiv s1, s8, s1
// 0x1059e1c: b #0x1059e54
// 0x1059e20: adrp x19, #0x1fab000
// 0x1059e24: ldrb w8, [x19, #0x1e0]
// 0x1059e28: cbnz w8, #0x1059e40
// 0x1059e2c: adrp x0, #0x1e8c000
// 0x1059e30: ldr x0, [x0, #0x138]
// 0x1059e34: bl #0xf7d92c
// 0x1059e38: mov w8, #1
// 0x1059e3c: strb w8, [x19, #0x1e0]
// 0x1059e40: adrp x8, #0x1e8c000
// 0x1059e44: ldr x8, [x8, #0x138]
// 0x1059e48: ldr x8, [x8]
// 0x1059e4c: ldr x8, [x8, #0xb8]
// 0x1059e50: ldp s0, s1, [x8]
// 0x1059e54: fabs s0, s0
// 0x1059e58: fabs s3, s1
// 0x1059e5c: fadd s0, s0, s3
// 0x1059e60: fmov s2, #1.00000000
// 0x1059e64: fmov s1, #-1.00000000
// 0x1059e68: fdiv s4, s9, s0
// 0x1059e6c: fdiv s3, s8, s0
// 0x1059e70: fmin s0, s4, s2
// 0x1059e74: fcmp s4, s1
// 0x1059e78: fcsel s0, s0, s1, pl
// 0x1059e7c: fcmp s3, s1
// 0x1059e80: b.mi #0x1059e88
// 0x1059e84: fmin s1, s3, s2
// 0x1059e88: ldp x30, x19, [sp, #0x20]
// 0x1059e8c: ldp d9, d8, [sp, #0x10]
// 0x1059e90: ldp d11, d10, [sp], #0x30
// 0x1059e94: ret
```

## `CFUtils.GetLineNumber` — RVA `0xc59e98`

- Decompiled symbol: `CFUtils_GetLineNumber`
- Metadata signature: `public static int GetLineNumber(string str, int index) { }`
- Native interval: `112` bytes
- Result: `pseudocode`

```c
unsigned int CFUtils_GetLineNumber(long long a0, unsigned int a1)
{
    unsigned long long v0;  // x0
    unsigned int v1;  // w21
    unsigned int v2;  // w21
    unsigned int v3;  // w21

    if (!a0)
        sub_f7db74();
    v0 = String__IndexOf();
    if (((char)(v0 >> 31) & 1))
    {
        return 1;
    }
    else if (a1 > (unsigned int)v0)
    {
        v1 = 1;
        while (true)
        {
            v2 = v1;
            v3 = v2 + 1;
            v0 = String__IndexOf(a0, 10, (unsigned int)v0 + 1, 0);
            if (((char)(v0 >> 31) & 1))
                return v2 + 1;
            v1 = v3;
            if ((unsigned int)v0 >= a1)
                return v2 + 1;
        }
    }
    else
    {
        return 1;
    }
}
```

## `CFUtils.GetEnumMaxValue` — RVA `0xc59f08`

- Decompiled symbol: `CFUtils_GetEnumMaxValue`
- Metadata signature: `public static int GetEnumMaxValue(Type enumType) { }`
- Native interval: `756` bytes
- Result: `pseudocode`

```c
typedef struct struct_6 {
    char padding_0[176];
    struct struct_5 *field_b0;
    char padding_b8[118];
    unsigned short field_12e;
} struct_6;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

typedef struct struct_15 {
    char padding_0[176];
    struct struct_16 *field_b0;
} struct_15;

typedef struct struct_3 {
    char padding_0[312];
    struct struct_4 *field_138;
    unsigned long long field_140;
} struct_3;

typedef struct struct_2 {
    struct struct_1 *field_0;
} struct_2;

typedef struct struct_10 {
    char padding_0[176];
    struct struct_9 *field_b0;
    char padding_b8[118];
    unsigned short field_12e;
} struct_10;

typedef struct struct_18 {
    char padding_0[176];
    struct struct_17 *field_b0;
    char padding_b8[118];
    unsigned short field_12e;
} struct_18;

typedef struct struct_7 {
    char padding_0[312];
    struct struct_8 *field_138;
    unsigned long long field_140;
} struct_7;

typedef struct struct_14 {
    char padding_0[176];
    struct struct_13 *field_b0;
    char padding_b8[118];
    unsigned short field_12e;
} struct_14;

typedef struct struct_20 {
    char padding_0[176];
    struct struct_19 *field_b0;
    char padding_b8[118];
    unsigned short field_12e;
} struct_20;

typedef struct struct_11 {
    char padding_0[312];
    struct struct_12 *field_138;
    unsigned long long field_140;
} struct_11;

typedef struct struct_5 {
    unsigned long long field_0;
    unsigned int field_8;
    char padding_c[12];
    char field_18;
} struct_5;

typedef struct struct_16 {
    unsigned long long field_0;
} struct_16;

typedef struct struct_4 {
    unsigned long long field_0;
} struct_4;

typedef struct struct_1 {
    char padding_0[224];
    unsigned int field_e0;
} struct_1;

typedef struct struct_9 {
    char padding_0[8];
    unsigned int field_8;
} struct_9;

typedef struct struct_17 {
    char padding_0[8];
    unsigned int field_8;
} struct_17;

typedef struct struct_8 {
    unsigned long long field_0;
} struct_8;

typedef struct struct_13 {
    char padding_0[8];
    unsigned int field_8;
} struct_13;

typedef struct struct_19 {
    char padding_0[8];
    unsigned int field_8;
} struct_19;

typedef struct struct_12 {
    unsigned long long field_0;
} struct_12;

extern struct_0 *g_1eef760;
extern long long g_1eefef8;
extern long long g_1eeff88;
extern long long g_1ef0450;
extern struct_6 *g_1fab000;
extern char g_1fab29b;

unsigned int CFUtils_GetEnumMaxValue(long long a0)
{
    struct_6 **ptr6;  // x20
    struct_0 **v1;  // x21
    struct_3 *ptr11;  // x0
    unsigned long long v11;  // x2
    unsigned long long v12;  // x1
    struct_6 **v13;  // x0
    long long v14;  // x0
    struct_2 **ptr7;  // x0
    struct_10 **ptr8;  // x0
    struct_18 *ptr;  // x8
    struct_10 **v18;  // x20
    unsigned long v19;  // x9
    long long v2;  // x1
    unsigned long cur;  // x10
    unsigned long v21;  // x9
    struct_7 *ptr12;  // x0
    unsigned long long v24;  // x2
    unsigned long long v25;  // x1
    struct_10 **v26;  // x0
    struct_14 **ptr9;  // x20
    struct_20 *p;  // x8
    unsigned long v29;  // x9
    long long *ptr10;  // x22
    unsigned long iter;  // x10
    unsigned long v31;  // x9
    struct_11 *ptr13;  // x0
    unsigned long long v34;  // x2
    unsigned long long v35;  // x1
    struct_14 **v36;  // x0
    struct_6 **v4;  // x0
    struct_15 *addr;  // x8
    unsigned long v6;  // x9
    unsigned long node;  // x10
    unsigned long v8;  // x9

    ptr6 = &g_1fab000;
    v1 = &g_1eef760;
    if (!(g_1fab29b & 1))
    {
        sub_f7d92c(&g_1eef760);
        sub_f7d92c(&g_1eefef8);
        sub_f7d92c(&g_1eeff88);
        sub_f7d92c(&g_1ef0450);
        g_1fab29b = 1;
    }
    if (!g_1eef760->field_e0)
        sub_f7da5c(g_1eef760);
    v2 = 0;
    if (Enum__GetValues(a0, 0))
    {
        ptr10 = &g_1eefef8;
        v2 = 0;
        v4 = Array__GetEnumerator();
        ptr6 = v4;
        if (v4)
        {
            addr = *(ptr6);
            v6 = *((short *)&addr[1].padding_0[118]);
            if (v6)
            {
                node = addr->field_b0 + 1;
                do
                {
                    v8 = v6;
                    if (*((long long *)(node - 8)) == g_1eeff88)
                    {
                        ptr11 = &addr->padding_0[16 * *((int *)node) + 312];
                        v12 = *((long long *)&ptr11->padding_0[8]);
                        v13 = ptr6;
                        (*((long long *)&ptr11->padding_0[0]))();
                    }
                } while ((node = (unsigned long)(node + 16), v6 = (unsigned long)(v8 - 1), v8 != 1));
            }
            v11 = 0;
            ptr11 = sub_f80110(ptr6);
            v12 = *((long long *)&ptr11->padding_0[8]);
            v13 = ptr6;
            (*((long long *)&ptr11->padding_0[0]))();
        }
    }
    else
    {
        v4 = sub_f7db74();
    }
    sub_f7db74(v4);
    while (true)
    {
        v14 = sub_f1bd40(v1);
        if ((int)v2 != 1)
            break;
        ptr7 = __cxa_begin_catch();
        v1 = *(ptr7);
        __cxa_end_catch(ptr7);
        v2 = *(ptr10);
        ptr8 = sub_f7da60(ptr6, v2);
        if (ptr8)
        {
            ptr = *(ptr8);
            v18 = ptr8;
            v19 = ptr->field_12e;
            if (v19)
            {
                cur = &ptr->field_b0->field_8;
                do
                {
                    v21 = v19;
                    if (*((long long *)(cur - 8)) == *(ptr10))
                    {
                        ptr12 = &ptr->padding_0[16 * *((int *)cur) + 312];
                        v25 = *((long long *)&ptr12->padding_0[8]);
                        v26 = v18;
                        (*((long long *)&ptr12->padding_0[0]))();
                    }
                } while ((cur = (unsigned long)(cur + 16), v19 = (unsigned long)(v21 - 1), v21 != 1));
            }
            v24 = 0;
            ptr12 = sub_f80110(v18);
            v25 = *((long long *)&ptr12->padding_0[8]);
            v26 = v18;
            (*((long long *)&ptr12->padding_0[0]))();
        }
        else if (!v1)
        {
            return 0;
        }
    }
    ptr9 = sub_f7da60(ptr6, *(ptr10));
    if (!ptr9)
    {
        sub_1026098(v14);
        sub_e29990(sub_f1bd40(0));
    }
    p = *(ptr9);
    v29 = p->field_12e;
    if (v29)
    {
        iter = &p->field_b0->field_8;
        do
        {
            v31 = v29;
            if (*((long long *)(iter - 8)) == *(ptr10))
            {
                ptr13 = &p->padding_0[16 * *((int *)iter) + 312];
                v35 = *((long long *)&ptr13->padding_0[8]);
                v36 = ptr9;
                (*((long long *)&ptr13->padding_0[0]))();
            }
        } while ((iter = (unsigned long)(iter + 16), v29 = (unsigned long)(v31 - 1), v31 != 1));
    }
    v34 = 0;
    ptr13 = sub_f80110(ptr9);
    v35 = *((long long *)&ptr13->padding_0[8]);
    v36 = ptr9;
    (*((long long *)&ptr13->padding_0[0]))();
}
```

## `CFUtils.CycleInt` — RVA `0xc5a1fc`

- Decompiled symbol: `CFUtils_CycleInt`
- Metadata signature: `public static int CycleInt(int curId, int dir, int maxId) { }`
- Native interval: `28` bytes
- Result: `pseudocode`

```c
unsigned long long CFUtils_CycleInt(unsigned long a0, unsigned long a1, int a2)
{
    unsigned long v0;  // 4116

    v0 = arm64g_calculate_condition(65, a1 & 4294967295, a0 & 4294967295, 0);
    if ((char)v0)
    {
        return a2;
    }
    else if (a2 < (unsigned int)a1 + (unsigned int)a0)
    {
        return 0;
    }
    else
    {
        return a1 + a0;
    }
}
```

## `CFUtils.SetEventSystemSelectedObject` — RVA `0xc5a218`

- Decompiled symbol: `CFUtils_SetEventSystemSelectedObject`
- Metadata signature: `public static void SetEventSystemSelectedObject(GameObject o) { }`
- Native interval: `300` bytes
- Result: `pseudocode`

```c
typedef struct struct_4 {
    char padding_0[40];
    struct struct_5 *field_28;
    long long field_30;
} struct_4;

typedef struct struct_3 {
    char padding_0[200];
    unsigned long long field_c8;
    char padding_d0[96];
    char field_130;
} struct_3;

typedef struct struct_5 {
    struct struct_3 *field_0;
} struct_5;

typedef struct struct_2 {
    char padding_0[224];
    unsigned int field_e0;
} struct_2;

typedef struct struct_1 {
    char padding_0[304];
    char field_130;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1eef828;
extern struct_1 *g_1eefaf8;
extern struct_2 *g_1ef0c58;
extern char g_1fab29c;

long long CFUtils_SetEventSystemSelectedObject(long long a0)
{
    struct_4 *v0;  // x20
    unsigned long v1;  // x0
    struct_4 *ptr;  // x21
    struct_4 *v3;  // x21
    unsigned long v4;  // x0
    unsigned long v5;  // x10
    unsigned long long v6;  // x0

    if (!(g_1fab29c & 1))
    {
        sub_f7d92c(&g_1eef828);
        sub_f7d92c(&g_1eefaf8);
        sub_f7d92c(&g_1ef0c58);
        g_1fab29c = 1;
    }
    if (!g_1eef828->field_e0)
        sub_f7da5c(g_1eef828);
    v0 = EventSystem__get_current(0);
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v1 = Object__op_Inequality(v0, 0, 0);
    if (!((char)v1 & 1))
        return v1;
    if (v0)
    {
        ptr = v0;
        ptr->field_30 = a0;
        v3 = &ptr->field_30;
        v4 = sub_f7d8d0(v3, a0);
        if (!*((long long *)&v3->padding_0[8]))
            return v4;
        v5 = g_1eefaf8->field_130;
        if (*((char *)(*((long long *)*((long long *)&v3->padding_0[8])) + 304)) < (unsigned int)v5)
        {
            return v4;
        }
        else if (*((long long *)(*((long long *)(*((long long *)*((long long *)&v3->padding_0[8])) + 200)) + v5 * 8 - 8)) != g_1eefaf8)
        {
            return v4;
        }
        else
        {
            EventSystem__SetSelectedGameObject(v0, 0, 0, 0);
            v6 = EventSystem__SetSelectedGameObject();
            return EventSystem__SetSelectedGameObject();
        }
    }
    sub_f7db74();
}
```
