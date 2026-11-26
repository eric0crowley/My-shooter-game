# Native pseudocode: ColorGradingModel.CurvesSettings

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `ColorGradingModel.CurvesSettings.get_defaultSettings` — RVA `0xcdb6b0`

- Decompiled symbol: `ColorGradingModel_CurvesSettings_get_defaultSettings`
- Metadata signature: `public static ColorGradingModel.CurvesSettings get_defaultSettings() { }`
- Native interval: `1564` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned int field_18;
    char padding_1c[4];
    char field_20[28];
    char field_2c;
    char padding_2d[15];
    char field_3c[28];
    char field_48;
} struct_0;

typedef struct struct_1 {
    char padding_0[24];
    unsigned int field_18;
    char padding_1c[4];
    char field_20[28];
    char field_2c;
    char padding_2d[15];
    char field_3c[28];
    char field_48;
} struct_1;

typedef struct struct_2 {
    char padding_0[24];
    unsigned int field_18;
    char padding_1c[4];
    char field_20[28];
    char field_2c;
    char padding_2d[15];
    char field_3c[28];
    char field_48;
} struct_2;

typedef struct struct_3 {
    char padding_0[24];
    unsigned int field_18;
    char padding_1c[4];
    char field_20[28];
    char field_2c;
    char padding_2d[15];
    char field_3c[28];
    char field_48;
} struct_3;

extern long long g_1eee230;
extern long long g_1eeef00;
extern char g_1fab60f;

long long ColorGradingModel_CurvesSettings_get_defaultSettings(void)
{
    struct_0 *ptr;  // x20
    long long v44;  // x0
    long long v53;  // x0
    unsigned long v54;  // x0
    long long v55;  // x0
    unsigned long v56;  // x0
    long long v57;  // x0
    unsigned long v58;  // x0
    long long v59;  // x0
    unsigned long v60;  // x0
    long long v61;  // x0
    unsigned long v62;  // x0
    unsigned long v45;  // x0
    long long v63;  // x8
    unsigned long dst;  // x0
    struct_1 *p;  // x20
    long long v47;  // x0
    long long v48;  // x0
    struct_2 *addr;  // x20
    long long v50;  // x0
    unsigned long v51;  // x0
    struct_3 *ptr3;  // x20
    int v0;  // [bp-0x2a0]
    char v1;  // [bp-0x294]
    int v2;  // [bp-0x280]
    unsigned long long flag4;  // [bp-0x270]
    unsigned int flag;  // [bp-0x268]
    int v5;  // [bp-0x260]
    unsigned long flag11;  // [bp-0x240]
    int v7;  // [bp-0x238]
    int v8;  // [bp-0x220], Other Possible Types: char
    char v9;  // [bp-0x214]
    int v10;  // [bp-0x200]
    unsigned long long flag7;  // [bp-0x1f0]
    unsigned int flag3;  // [bp-0x1e8]
    int v13;  // [bp-0x1e0]
    unsigned long flag10;  // [bp-0x1c0]
    int v15;  // [bp-0x1b8]
    int v16;  // [bp-0x1a0]
    char v17;  // [bp-0x194]
    int v18;  // [bp-0x180]
    unsigned long long flag6;  // [bp-0x170]
    unsigned int flag2;  // [bp-0x168]
    int v21;  // [bp-0x160]
    unsigned long flag9;  // [bp-0x140]
    int v23;  // [bp-0x138]
    int v24;  // [bp-0x120]
    char v25;  // [bp-0x114]
    int v26;  // [bp-0x100]
    unsigned long long flag5;  // [bp-0xf0]
    unsigned int choice;  // [bp-0xe8]
    int v29;  // [bp-0xe0]
    unsigned long flag8;  // [bp-0xc0]
    int v31;  // [bp-0xb8]
    uint128_t v32;  // [bp-0xa0], Other Possible Types: unsigned long
    long long v33;  // [bp-0x98]
    uint128_t v34;  // [bp-0x90], Other Possible Types: unsigned long
    unsigned long v35;  // [bp-0x88]
    uint128_t v36;  // [bp-0x80], Other Possible Types: unsigned long
    unsigned long v37;  // [bp-0x78]
    uint128_t v38;  // [bp-0x70], Other Possible Types: unsigned long
    unsigned long v39;  // [bp-0x68]
    unsigned long long v40;  // [bp-0x60]
    char *v41;  // [bp-0x50]
    char v42;  // [bp+0x0]

    v41 = &v42;
    if (!(g_1fab60f & 1))
    {
        sub_f7d92c("W,");
        sub_f7d92c(&g_1eeef00);
        sub_f7d92c(&g_1eee230);
        g_1fab60f = 1;
    }
    v40 = 0;
    v36 = 0;
    v38 = 0;
    v32 = 0;
    v34 = 0;
    ptr = sub_f7d9d4(g_1eee230, 2);
    flag8 = 0;
    *((unsigned long long *)&v31) = 0;
    *((unsigned int *)&(&v31)[16]) = 0;
    *((unsigned long long *)&(&v31)[8]) = 0;
    Keyframe__ctor(&flag8, 0);
    if (!ptr)
        sub_f7db74();
    memcpy(&v29, &flag8, 16);
    *((uint128_t *)&(&v29)[12]) = *((uint128_t *)(&v31 + 4));
    if (ptr->field_18)
    {
        *((uint128_t *)&ptr->field_20[12]) = *((uint128_t *)(&v29 + 12));
        *((uint128_t *)&ptr->field_20[0]) = *((uint128_t *)&v29);
        *((unsigned long long *)&v26) = 0;
        *((unsigned long long *)&(&v26)[8]) = 0;
        choice = 0;
        flag5 = 0;
        Keyframe__ctor(&v26, 0);
        memcpy(&v25, &v26 - 12, 16);
        v24 = v26;
        if (ptr->field_18 > 1)
        {
            *((uint128_t *)&ptr->padding_2d[11]) = *((uint128_t *)(&v24 + 12));
            *((uint128_t *)&ptr->field_2c) = *((uint128_t *)&v24);
            v44 = sub_f7db70(g_1eee7c8);
            AnimationCurve__ctor(v44, ptr, 0);
            v45 = sub_f7db70(g_1eeef00);
            ColorGradingCurve__ctor(v45, v44, 0, 0);
            v32 = v45;
            sub_f7d8d0(&v32, v32);
            p = sub_f7d9d4(g_1eee230, 2);
            flag9 = 0;
            *((unsigned long long *)&v23) = 0;
            *((unsigned int *)&(&v23)[16]) = 0;
            *((unsigned long long *)&(&v23)[8]) = 0;
            Keyframe__ctor(&flag9, 0);
            if (!p)
                sub_f7db74();
            memcpy(&v21, &flag9, 16);
            *((uint128_t *)&(&v21)[12]) = *((uint128_t *)(&v23 + 4));
            if (p->field_18)
            {
                *((uint128_t *)&p->field_20[12]) = *((uint128_t *)(&v21 + 12));
                *((uint128_t *)&p->field_20[0]) = *((uint128_t *)&v21);
                *((unsigned long long *)&v18) = 0;
                *((unsigned long long *)&(&v18)[8]) = 0;
                flag2 = 0;
                flag6 = 0;
                Keyframe__ctor(&v18, 0);
                memcpy(&v17, &v18 - 12, 16);
                v16 = v18;
                if (p->field_18 > 1)
                {
                    *((uint128_t *)&p->padding_2d[11]) = *((uint128_t *)(&v16 + 12));
                    *((uint128_t *)&p->field_2c) = *((uint128_t *)&v16);
                    v47 = sub_f7db70(g_1eee7c8);
                    AnimationCurve__ctor(v47, p, 0);
                    v48 = sub_f7db70(g_1eeef00);
                    ColorGradingCurve__ctor(v48, v47, 0, 0);
                    v33 = v48;
                    sub_f7d8d0(&v32 | 8, v33);
                    addr = sub_f7d9d4(g_1eee230, 2);
                    flag10 = 0;
                    *((unsigned long long *)&v15) = 0;
                    *((unsigned int *)&(&v15)[16]) = 0;
                    *((unsigned long long *)&(&v15)[8]) = 0;
                    Keyframe__ctor(&flag10, 0);
                    if (!addr)
                        sub_f7db74();
                    memcpy(&v13, &flag10, 16);
                    *((uint128_t *)&(&v13)[12]) = *((uint128_t *)(&v15 + 4));
                    if (addr->field_18)
                    {
                        *((uint128_t *)&addr->field_20[12]) = *((uint128_t *)(&v13 + 12));
                        *((uint128_t *)&addr->field_20[0]) = *((uint128_t *)&v13);
                        *((unsigned long long *)&v10) = 0;
                        *((unsigned long long *)&(&v10)[8]) = 0;
                        flag3 = 0;
                        flag7 = 0;
                        Keyframe__ctor(&v10, 0);
                        memcpy(&v9, &v10 - 12, 16);
                        v8 = (int)_INSERT(v8 CONCAT 0, 0, v10);
                        if (addr->field_18 > 1)
                        {
                            *((uint128_t *)&addr->padding_2d[11]) = *((uint128_t *)(&v8 + 12));
                            *((uint128_t *)&addr->field_2c) = *((uint128_t *)&v8);
                            v50 = sub_f7db70(g_1eee7c8);
                            AnimationCurve__ctor(v50, addr, 0);
                            v51 = sub_f7db70(g_1eeef00);
                            ColorGradingCurve__ctor(v51, v50, 0, 0);
                            v34 = v51;
                            sub_f7d8d0(&v34, v34);
                            ptr3 = sub_f7d9d4(g_1eee230, 2);
                            flag11 = 0;
                            *((unsigned long long *)&v7) = 0;
                            *((unsigned int *)&(&v7)[16]) = 0;
                            *((unsigned long long *)&(&v7)[8]) = 0;
                            Keyframe__ctor(&flag11, 0);
                            if (!ptr3)
                                sub_f7db74();
                            memcpy(&v5, &flag11, 16);
                            *((uint128_t *)&(&v5)[12]) = *((uint128_t *)(&v7 + 4));
                            if (ptr3->field_18)
                            {
                                *((uint128_t *)&ptr3->field_20[12]) = *((uint128_t *)(&v5 + 12));
                                *((uint128_t *)&ptr3->field_20[0]) = *((uint128_t *)&v5);
                                *((unsigned long long *)&v2) = 0;
                                *((unsigned long long *)&(&v2)[8]) = 0;
                                flag = 0;
                                flag4 = 0;
                                Keyframe__ctor(&v2, 0);
                                memcpy(&v1, &v2 - 12, 16);
                                v0 = v2;
                                if (ptr3->field_18 > 1)
                                {
                                    *((uint128_t *)&ptr3->padding_2d[11]) = *((uint128_t *)(&v0 + 12));
                                    *((uint128_t *)&ptr3->field_2c) = *((uint128_t *)&v0);
                                    v53 = sub_f7db70(g_1eee7c8);
                                    AnimationCurve__ctor(v53, ptr3, 0);
                                    v54 = sub_f7db70(g_1eeef00);
                                    ColorGradingCurve__ctor(v54, v53, 0, 0);
                                    v35 = v54;
                                    sub_f7d8d0(&v35, v35);
                                    v55 = sub_f7db70(g_1eee7c8);
                                    AnimationCurve__ctor(v55, 0);
                                    v56 = sub_f7db70(g_1eeef00);
                                    ColorGradingCurve__ctor(v56, v55, 1, 0);
                                    v36 = v56;
                                    sub_f7d8d0(&v36, v36);
                                    v57 = sub_f7db70(g_1eee7c8);
                                    AnimationCurve__ctor(v57, 0);
                                    v58 = sub_f7db70(g_1eeef00);
                                    ColorGradingCurve__ctor(v58, v57, 1, 0);
                                    v37 = v58;
                                    sub_f7d8d0(&v37, v37);
                                    v59 = sub_f7db70(g_1eee7c8);
                                    AnimationCurve__ctor(v59, 0);
                                    v60 = sub_f7db70(g_1eeef00);
                                    ColorGradingCurve__ctor(v60, v59, 0, 0);
                                    v38 = v60;
                                    sub_f7d8d0(&v38, v38);
                                    v61 = sub_f7db70(g_1eee7c8);
                                    AnimationCurve__ctor(v61, 0);
                                    v62 = sub_f7db70(g_1eeef00);
                                    ColorGradingCurve__ctor(v62, v61, 0, 0);
                                    v39 = v62;
                                    sub_f7d8d0(&v39, v39);
                                    v40 = 0x100000000;
                                    dst = memcpy(v63, &v32, 72);
                                    return memcpy(v63, &v32, 72);
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    sub_f7db7c();
    sub_f7db74();
}
```
