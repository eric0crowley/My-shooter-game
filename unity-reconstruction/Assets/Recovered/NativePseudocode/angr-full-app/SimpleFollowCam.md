# Native pseudocode: SimpleFollowCam

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `SimpleFollowCam.OnEnable` — RVA `0xc6642c`

- Decompiled symbol: `SimpleFollowCam_OnEnable`
- Metadata signature: `private void OnEnable() { }`
- Native interval: `324` bytes
- Result: `pseudocode`
- Heuristic layout hint: `SimpleFollowCam_Recovered` matched 3 offsets against `SimpleFollowCam` metadata (confidence 1.00).

```c
typedef struct SimpleFollowCam_Recovered {
    char padding_0[32];
    long long targetTransform;
    char padding_28[28];
    unsigned int camZoomFactor;
    char padding_48[24];
    long long cam;
} SimpleFollowCam_Recovered;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern long long g_1efcf30;
extern char g_1fab303;

long long SimpleFollowCam_OnEnable(struct_1 *ptr)
{
    long long v0;  // x0
    struct_1 *p;  // x20
    long long v2;  // x0
    long long v3;  // x0
    long long v4;  // x0
    unsigned int v5;  // s0
    unsigned int v6;  // s1
    unsigned int v7;  // s2

    if (!(g_1fab303 & 1))
    {
        sub_f7d92c(&g_1efcf30);
        sub_f7d92c(&g_1ef0c58);
        g_1fab303 = 1;
    }
    v0 = sub_1231bc8(ptr, g_1efcf30);
    ptr->field_60 = v0;
    p = &ptr->field_60;
    sub_f7d8d0(p, v0);
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (((char)Object__op_Inequality(*((long long *)&p->padding_0[0]), 0, 0) & 1))
    {
        v2 = *((long long *)&p->padding_0[0]);
        if (!v2)
        {
            sub_f7db74(v2);
        }
        else if (((char)Camera__get_orthographic(v2, 0) & 1))
        {
            ptr->field_44 = 0x3f000000;
        }
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v3 = Object__op_Inequality(ptr->field_20, 0, 0);
    if (!((char)v3 & 1))
        return v3;
    v2 = Component__get_transform(ptr, 0);
    if (!v2)
        sub_f7db74(v2);
    Transform__get_position();
    v2 = ptr->field_20;
    if (v2)
    {
        v4 = Transform__get_position(v2, 0);
        *((unsigned int *)&ptr->padding_28[4]) = v5 - v5;
        *((unsigned int *)&ptr->padding_28[8]) = v6 - v6;
        *((unsigned int *)&ptr->padding_28[12]) = v7 - v7;
        return v4;
    }
    sub_f7db74(v2);
}
```

## `SimpleFollowCam.Update` — RVA `0xc66570`

- Decompiled symbol: `SimpleFollowCam_Update`
- Metadata signature: `private void Update() { }`
- Native interval: `152` bytes
- Result: `pseudocode`
- Heuristic layout hint: `SimpleFollowCam_Recovered` matched 2 offsets against `SimpleFollowCam` metadata (confidence 1.00).

```c
typedef struct SimpleFollowCam_Recovered {
    char padding_0[68];
    unsigned int camZoomFactor;
    char padding_48[16];
    long long camZoomDeltaAxis;
} SimpleFollowCam_Recovered;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1eeed00;
extern char g_1fab304;

unsigned long long SimpleFollowCam_Update(struct_1 *ptr)
{
    unsigned long long v4;  // d8
    unsigned long long v5;  // x30
    unsigned long long v6;  // x20
    unsigned long long v7;  // x19
    unsigned long long v8;  // x0
    unsigned int v9;  // s8
    unsigned int v10;  // s0
    unsigned int v11;  // s0
    unsigned long v12;  // 4133
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x18]
    unsigned long long v2;  // [bp-0x10]
    unsigned long long v3;  // [bp-0x8]

    v0 = v4;
    v1 = v5;
    v2 = v6;
    v3 = v7;
    if (!(g_1fab304 & 1))
    {
        sub_f7d92c(&g_1eeed00);
        g_1fab304 = 1;
    }
    v8 = String__IsNullOrEmpty(ptr->field_58, 0);
    v9 = ptr->field_44;
    if (!((char)v8 & 1))
    {
        if (!g_1eeed00->field_e0)
            sub_f7da5c(g_1eeed00);
        v8 = CF2Input__GetAxis(ptr->field_58, 0);
        v9 = ptr->field_44 + v10;
    }
    v11 = [D] unsupported_Iop_ZeroHI96ofV128();
    v12 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v9, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v9, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v9, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v9, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v9, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v9, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if (!((char)v12))
        v11 = 0;
    ptr->field_44 = v11;
    return v8;
}
```

## `SimpleFollowCam.FixedUpdate` — RVA `0xc66608`

- Decompiled symbol: `SimpleFollowCam_FixedUpdate`
- Metadata signature: `private void FixedUpdate() { }`
- Native interval: `640` bytes
- Result: `pseudocode`
- Heuristic layout hint: `SimpleFollowCam_Recovered` matched 4 offsets against `SimpleFollowCam` metadata (confidence 1.00).

```c
typedef struct SimpleFollowCam_Recovered {
    char padding_0[32];
    long long targetTransform;
    unsigned int smoothingTime;
    char padding_2c[24];
    unsigned int camZoomFactor;
    char padding_48[24];
    long long cam;
} SimpleFollowCam_Recovered;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab305;

long long SimpleFollowCam_FixedUpdate(struct_1 *ptr)
{
    long long v1;  // x0
    long long v2;  // x0
    unsigned long v3;  // x20
    unsigned int v4;  // s2
    unsigned long v5;  // 4153
    unsigned int v6;  // s0
    unsigned long v7;  // 4133
    unsigned long long v8;  // x0
    unsigned int v0;  // [bp-0x70]

    if (!(g_1fab305 & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab305 = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v1 = Object__op_Equality(ptr->field_20, 0, 0);
    if (((char)v1 & 1))
        return v1;
    v2 = ptr->field_20;
    if (v2)
    {
        Transform__get_position(v2, 0);
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        if (((char)Object__op_Inequality(ptr->field_60, 0, 0) & 1))
        {
            v2 = ptr->field_60;
            if (v2)
            {
                v2 = Camera__get_orthographic(v2, 0);
                if (!(v2 & 1))
                    goto LABEL_1066784;
                v3 = ptr->field_60;
                if (v3)
                {
                    Camera__get_orthographicSize(v3, 0);
                    v4 = ptr->field_44;
                    v5 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v4, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v4, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v4, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v4, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v4, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v4, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                    CFUtils__get_realDeltaTimeClamped();
                    CFUtils__SmoothTowards(0);
                    Camera__set_orthographicSize(v3, 0);
LABEL_10667bc:
                    v6 = ptr->field_28;
                    v7 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v6, 981668463)) >> 5 & 3 | (unsigned long long)(CmpF(v6, 981668463) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v6, 981668463)) >> 5 & 3 | (unsigned long long)(CmpF(v6, 981668463) & 1)) & ((unsigned long long)(char)(CmpF(v6, 981668463)) >> 5 & 3 | (unsigned long long)(CmpF(v6, 981668463) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                    if (!((char)v7))
                    {
                        v2 = Component__get_transform(ptr, 0);
                        if (v2)
                        {
                            Transform__get_position();
                            Time__get_deltaTime(0);
                            v0 = v6;
                            Vector3__SmoothDamp(&ptr->padding_2c[12], 0);
                            goto LABEL_1066844;
                        }
                    }
                    else
                    {
LABEL_1066844:
                        v2 = Component__get_transform(ptr, 0);
                        if (v2)
                        {
                            v8 = Transform__set_position();
                            return Transform__set_position();
                        }
                    }
                }
            }
        }
        else
        {
LABEL_1066784:
            v2 = Component__get_transform(ptr, 0);
            if (v2)
            {
                Transform__get_forward();
                goto LABEL_10667bc;
            }
        }
    }
    sub_f7db74(v2);
}
```

## `SimpleFollowCam.ctor` — RVA `0xc66888`

- Decompiled symbol: `SimpleFollowCam_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `120` bytes
- Result: `pseudocode`
- Heuristic layout hint: `SimpleFollowCam_Recovered` matched 4 offsets against `SimpleFollowCam` metadata (confidence 1.00).

```c
typedef struct SimpleFollowCam_Recovered {
    char padding_0[40];
    unsigned int smoothingTime;
    char padding_2c[28];
    unsigned long long perspZoomOutOffset;
    unsigned int orthoZoomOutSize;
    char padding_54[4];
    long long camZoomDeltaAxis;
} SimpleFollowCam_Recovered;

extern long long g_1f08dc8;
extern char g_1fab306;

void SimpleFollowCam_ctor(struct_0 *ptr)
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
    if (!(g_1fab306 & 1))
    {
        sub_f7d92c(&g_1f08dc8);
        g_1fab306 = 1;
    }
    ptr->field_28 = 1036831949;
    ptr->field_48 = 0x4000000041200000;
    ptr->field_50 = 0x40a00000;
    ptr->field_58 = g_1f08dc8;
    sub_f7d8d0((struct SimpleFollowCam_Recovered *)&ptr->field_58, g_1f08dc8);
    MonoBehaviour__ctor();
    return;
}
```
