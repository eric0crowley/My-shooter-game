# Native pseudocode: bl_CurveControlledBob

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `bl_CurveControlledBob.Setup` — RVA `0xcdfb40`

- Decompiled symbol: `bl_CurveControlledBob_Setup`
- Metadata signature: `public void Setup(Camera camera, float bobBaseInterval) { }`
- Native interval: `160` bytes
- Result: `pseudocode`
- Heuristic layout hint: `bl_CurveControlledBob_Recovered` matched 4 offsets against `bl_CurveControlledBob` metadata (confidence 0.67).

```c
typedef struct bl_CurveControlledBob_Recovered {
    char padding_0[24];
    long long Bobcurve;
    char padding_20[12];
    unsigned int m_BobBaseInterval;
    unsigned int m_OriginalCameraPosition;
    unsigned int field_34;
    unsigned int field_38;
    unsigned int m_Time;
} bl_CurveControlledBob_Recovered;

unsigned long long bl_CurveControlledBob_Setup(struct_0 *ptr, long long a1)
{
    unsigned int v6;  // s0
    long long v7;  // x20
    unsigned int v8;  // s1
    unsigned int v9;  // s2
    unsigned long long v11;  // x0
    int v0;  // [bp-0x60]
    int v1;  // [bp-0x40], Other Possible Types: unsigned long long
    unsigned long long choice;  // [bp-0x38]
    int v3;  // [bp-0x34]
    unsigned long long flag2;  // [bp-0x30]
    unsigned int flag;  // [bp-0x28]

    v1 = 0;
    choice = 0;
    flag = 0;
    flag2 = 0;
    ptr->field_2c = v6;
    if (a1 && Component__get_transform(a1, 0))
    {
        Transform__get_localPosition();
        v7 = ptr->field_18;
        ptr->field_30 = v6;
        ptr->field_34 = v8;
        ptr->field_38 = v9;
        if (v7)
        {
            AnimationCurve__get_Item(v7, AnimationCurve__get_length(v7, 0) - 1, 0);
            v1 = (int)*((uint128_t *)&v0);
            v3 = (int)*((uint128_t *)(&v0 + 12));
            v11 = Keyframe__get_time(&v1, 0);
            ptr->field_3c = *((unsigned int *)&v1);
            return v11;
        }
    }
    sub_f7db74();
}
```

## `bl_CurveControlledBob.DoHeadBob` — RVA `0xcdfbe0`

- Decompiled symbol: `bl_CurveControlledBob_DoHeadBob`
- Metadata signature: `public Vector3 DoHeadBob(float speed) { }`
- Native interval: `260` bytes
- Result: `pseudocode`
- Heuristic layout hint: `bl_CurveControlledBob_Recovered` matched 7 offsets against `bl_CurveControlledBob` metadata (confidence 1.00).

```c
typedef struct bl_CurveControlledBob_Recovered {
    char padding_0[24];
    unsigned long long Bobcurve;
    unsigned int VerticaltoHorizontalRatio;
    unsigned int m_CyclePositionX;
    unsigned int m_CyclePositionY;
    unsigned int m_BobBaseInterval;
    unsigned int m_OriginalCameraPosition;
    char padding_34[8];
    unsigned int m_Time;
} bl_CurveControlledBob_Recovered;

int bl_CurveControlledBob_DoHeadBob(struct_0 *ptr)
{
    unsigned long long v1;  // x0
    unsigned int v2;  // s11
    unsigned int v3;  // s0
    unsigned int v4;  // s0
    unsigned int v5;  // w0
    unsigned int v6;  // s2
    unsigned int v7;  // s0
    unsigned int v8;  // s1
    unsigned long v9;  // 4197
    unsigned long v10;  // 4125
    unsigned int v0;  // [bp-0x54]

    v1 = ptr->field_18;
    if (v1)
    {
        v0 = ptr->field_30;
        AnimationCurve__Evaluate(v1, 0);
        v1 = ptr->field_18;
        if (v1)
        {
            AnimationCurve__Evaluate(v1, 0);
            Time__get_deltaTime(0);
            v2 = ptr->field_28;
            v4 = ptr->field_24 + ptr->field_28 * v3 / ptr->field_2c;
            ptr->field_24 = v4;
            v5 = Time__get_deltaTime(0);
            v6 = ptr->field_24;
            v7 = ptr->field_3c;
            v8 = v2 + v4 * v3 / ptr->field_2c * ptr->field_20;
            ptr->field_28 = v8;
            v9 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v6, v7)) >> 5 & 3 | (unsigned long long)(CmpF(v6, v7) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v6, v7)) >> 5 & 3 | (unsigned long long)(CmpF(v6, v7) & 1)) & ((unsigned long long)(char)(CmpF(v6, v7)) >> 5 & 3 | (unsigned long long)(CmpF(v6, v7) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
            if (!((char)v9))
                ptr->field_24 = v6 - v7;
            v10 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v8, v7)) >> 5 & 3 | (unsigned long long)(CmpF(v8, v7) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v8, v7)) >> 5 & 3 | (unsigned long long)(CmpF(v8, v7) & 1)) & ((unsigned long long)(char)(CmpF(v8, v7)) >> 5 & 3 | (unsigned long long)(CmpF(v8, v7) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
            if ((char)v10)
                return v5;
            ptr->field_28 = v8 - v7;
            return v5;
        }
    }
    sub_f7db74(v1);
}
```

## `bl_CurveControlledBob.ctor` — RVA `0xcdfce4`

- Decompiled symbol: `bl_CurveControlledBob_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `584` bytes
- Result: `pseudocode`
- Heuristic layout hint: `bl_CurveControlledBob_Recovered` matched 3 offsets against `bl_CurveControlledBob` metadata (confidence 1.00).

```c
typedef struct bl_CurveControlledBob_Recovered {
    char padding_0[16];
    unsigned long long HorizontalBobRange;
    long long Bobcurve;
    unsigned int VerticaltoHorizontalRatio;
} bl_CurveControlledBob_Recovered;

typedef struct struct_1 {
    char padding_0[24];
    unsigned int field_18;
    char padding_1c[4];
    char field_20[28];
    char field_2c;
    char padding_2d[15];
    char field_3c[28];
    char field_48;
    char padding_49[15];
    char field_58[28];
    char field_64;
    char padding_65[15];
    char field_74[28];
    char field_80;
    char padding_81[15];
    char field_90[28];
    char field_9c;
} struct_1;

extern long long g_1eee230;
extern char g_1fab631;

long long bl_CurveControlledBob_ctor(struct_0 *p)
{
    struct_1 *ptr;  // x20
    long long v26;  // x21
    unsigned long v27;  // x0
    int v0;  // [bp-0x170]
    char v1;  // [bp-0x164]
    int v2;  // [bp-0x150]
    unsigned long long flag4;  // [bp-0x140]
    unsigned int flag;  // [bp-0x138]
    int v5;  // [bp-0x130]
    char v6;  // [bp-0x124]
    int v7;  // [bp-0x110]
    unsigned long long flag7;  // [bp-0x100]
    unsigned int flag3;  // [bp-0xf8]
    int v10;  // [bp-0xf0]
    char v11;  // [bp-0xe4]
    int v12;  // [bp-0xd0]
    unsigned long long flag6;  // [bp-0xc0]
    unsigned int flag2;  // [bp-0xb8]
    int v15;  // [bp-0xb0]
    char v16;  // [bp-0xa4]
    int v17;  // [bp-0x90]
    unsigned long long flag5;  // [bp-0x80]
    unsigned int choice;  // [bp-0x78]
    int v20;  // [bp-0x70]
    unsigned long flag8;  // [bp-0x50]
    int v22;  // [bp-0x48]
    char *v23;  // [bp-0x30]
    char v24;  // [bp+0x0]

    v23 = &v24;
    if (!(g_1fab631 & 1))
    {
        sub_f7d92c("W,");
        sub_f7d92c(&g_1eee230);
        g_1fab631 = 1;
    }
    p->field_10 = 4515128845357610435;
    ptr = sub_f7d9d4(g_1eee230, 5);
    flag8 = 0;
    *((unsigned long long *)&v22) = 0;
    *((unsigned int *)&(&v22)[16]) = 0;
    *((unsigned long long *)&(&v22)[8]) = 0;
    Keyframe__ctor(&flag8, 0);
    if (ptr)
    {
        memcpy(&v20, &flag8, 16);
        *((uint128_t *)&(&v20)[12]) = *((uint128_t *)(&v22 + 4));
        if (ptr->field_18)
        {
            *((uint128_t *)&ptr->field_20[12]) = *((uint128_t *)(&v20 + 12));
            *((uint128_t *)&ptr->field_20[0]) = *((uint128_t *)&v20);
            *((unsigned long long *)&v17) = 0;
            *((unsigned long long *)&(&v17)[8]) = 0;
            choice = 0;
            flag5 = 0;
            Keyframe__ctor(&v17, 0);
            memcpy(&v16, &v17 - 12, 16);
            v15 = v17;
            if (ptr->field_18 > 1)
            {
                *((uint128_t *)&ptr->padding_2d[11]) = *((uint128_t *)(&v15 + 12));
                *((uint128_t *)&ptr->field_2c) = *((uint128_t *)&v15);
                *((unsigned long long *)&v12) = 0;
                *((unsigned long long *)&(&v12)[8]) = 0;
                flag2 = 0;
                flag6 = 0;
                Keyframe__ctor(&v12, 0);
                memcpy(&v11, &v12 - 12, 16);
                v10 = v12;
                if (ptr->field_18 > 2)
                {
                    *((uint128_t *)&ptr->field_3c[24]) = *((uint128_t *)(&v10 + 12));
                    *((uint128_t *)&ptr->field_3c[12]) = *((uint128_t *)&v10);
                    *((unsigned long long *)&v7) = 0;
                    *((unsigned long long *)&(&v7)[8]) = 0;
                    flag3 = 0;
                    flag7 = 0;
                    Keyframe__ctor(&v7, 0);
                    memcpy(&v6, &v7 - 12, 16);
                    v5 = v7;
                    if (ptr->field_18 > 3)
                    {
                        *((uint128_t *)&ptr->field_58[8]) = *((uint128_t *)(&v5 + 12));
                        *((uint128_t *)&ptr->padding_49[11]) = *((uint128_t *)&v5);
                        *((unsigned long long *)&v2) = 0;
                        *((unsigned long long *)&(&v2)[8]) = 0;
                        flag = 0;
                        flag4 = 0;
                        Keyframe__ctor(&v2, 0);
                        memcpy(&v1, &v2 - 12, 16);
                        v0 = v2;
                        if (ptr->field_18 > 4)
                        {
                            *((uint128_t *)&ptr->padding_65[7]) = *((uint128_t *)(&v0 + 12));
                            *((uint128_t *)&ptr->field_58[24]) = *((uint128_t *)&v0);
                            v26 = sub_f7db70(g_1eee7c8);
                            AnimationCurve__ctor(v26, ptr, 0);
                            p->field_18 = v26;
                            sub_f7d8d0((struct bl_CurveControlledBob_Recovered *)&p->field_18, v26);
                            p->field_20 = 0x3f800000;
                            v27 = Object__ctor(p, 0);
                            return Object__ctor(p, 0);
                        }
                    }
                }
            }
        }
        sub_f7db7c();
    }
    sub_f7db74();
}
```
