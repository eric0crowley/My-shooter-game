# Native pseudocode: jiggleBones

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `jiggleBones.Awake` — RVA `0xc6a6b4`

- Decompiled symbol: `jiggleBones_Awake`
- Metadata signature: `private void Awake() { }`
- Native interval: `120` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[40];
    unsigned long long field_28;
    unsigned int field_30;
    unsigned int field_34;
    unsigned int field_38;
    unsigned int field_3c;
    unsigned int field_40;
    unsigned int field_44;
    unsigned int field_48;
} struct_0;

unsigned long long jiggleBones_Awake(struct_0 *ptr)
{
    unsigned long long v0;  // x0
    unsigned int v1;  // s0
    unsigned int v2;  // s2
    unsigned int v3;  // s1
    unsigned long long v4;  // x0
    unsigned int v5;  // s0
    unsigned int v6;  // s1
    unsigned int v7;  // s2

    v0 = ptr->field_28;
    if (v0)
    {
        Transform__get_position(v0, 0);
        v0 = ptr->field_28;
        if (v0)
        {
            v1 = ptr->field_48;
            v2 = v1 * ptr->field_44;
            v3 = v1 * ptr->field_40;
            v4 = Transform__TransformDirection(v0, 0);
            ptr->field_30 = v5 + v1 * ptr->field_3c;
            ptr->field_34 = v6 + v3;
            ptr->field_38 = v7 + v2;
            return v4;
        }
    }
    sub_f7db74(v0);
}
```

## `jiggleBones.LateUpdate` — RVA `0xc6a72c`

- Decompiled symbol: `jiggleBones_LateUpdate`
- Metadata signature: `private void LateUpdate() { }`
- Native interval: `1140` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[32];
    char field_20;
    char padding_21[7];
    unsigned long long field_28;
    unsigned int field_30;
    unsigned int field_34;
    unsigned int field_38;
    unsigned int field_3c;
    unsigned int field_40;
    unsigned int field_44;
    unsigned int field_48;
    unsigned int field_4c;
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
    unsigned int field_78;
    unsigned int field_7c;
    char field_80;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1eef458;
extern long long g_1ef22e8;
extern char g_1fab32c;
extern char g_1fab32e;
extern char g_1fab3df;

unsigned long long jiggleBones_LateUpdate(struct_1 *ptr)
{
    unsigned long long v7;  // x0
    unsigned int v8;  // s0
    unsigned int v17;  // s19
    unsigned int v18;  // s0
    unsigned int v19;  // s7
    unsigned int v20;  // s5
    unsigned int v21;  // s6
    unsigned int v22;  // s1
    unsigned int v23;  // s16
    unsigned int v24;  // s1
    unsigned int v25;  // s2
    unsigned int v26;  // s1
    unsigned int v9;  // s0
    unsigned long long v27;  // x0
    unsigned int v28;  // s2
    unsigned long long v29;  // 4118
    unsigned int v30;  // s1
    unsigned long long v31;  // 4106
    unsigned int v32;  // s3
    unsigned long long v33;  // 4103
    unsigned long long v34;  // x0
    unsigned int v10;  // s3
    unsigned int v11;  // s4
    unsigned int v12;  // s0
    unsigned int v13;  // s1
    unsigned int v14;  // s18
    unsigned int v15;  // s17
    unsigned int v16;  // s2
    unsigned long long v0;  // [bp-0x90]
    unsigned long long v1;  // [bp-0x88]
    unsigned int v2;  // [bp-0x74]
    unsigned int v3;  // [bp-0x70]
    unsigned int v4;  // [bp-0x6c]
    unsigned int v5;  // [bp-0x68]
    unsigned int v6;  // [bp-0x64]

    if (!(g_1fab32e & 1))
    {
        sub_f7d92c(&g_1eef458);
        g_1fab32e = 1;
    }
    v7 = ptr->field_28;
    if (v7 && (Transform__set_rotation(v7, 0), v7 = ptr->field_28, v7 && (v8 = ptr->field_48, Transform__TransformDirection(v7, 0), v7 = ptr->field_28, v7)))
    {
        v2 = v8 * ptr->field_44;
        v3 = v8 * ptr->field_40;
        v4 = v8 * ptr->field_3c;
        Transform__TransformDirection(v7, 0);
        v7 = ptr->field_28;
        if (v7 && (Transform__get_position(v7, 0), v7 = ptr->field_28, v7))
        {
            v9 = ptr->field_48;
            Transform__TransformDirection(v7, 0);
            v10 = ptr->field_30;
            v11 = ptr->field_34;
            v12 = ptr->field_4c;
            v13 = ptr->field_50;
            v14 = ptr->field_38;
            v15 = ptr->field_78;
            v5 = 0x3f800000 + v9 * ptr->field_40;
            v6 = 0 + v9 * ptr->field_3c;
            v16 = 0x3f800000 - ptr->field_54;
            v17 = v12 * (v6 - v10);
            v18 = v12 * (0 + v9 * ptr->field_44 - v14);
            v19 = v17 / v13;
            v20 = v12 * (v5 - v11) + ptr->field_58 / 0xc1200000;
            v21 = v18 / v13;
            v22 = v20 / v13;
            v23 = ptr->field_74 + v19 * v16;
            ptr->field_6c = v22;
            ptr->field_70 = v21;
            v24 = ptr->field_7c;
            v7 = ptr->field_28;
            v25 = v15 + v16 * v22;
            ptr->field_5c = v17;
            ptr->field_60 = v20;
            v26 = v24 + v16 * v21;
            ptr->field_78 = v25;
            ptr->field_7c = v26;
            ptr->field_64 = v18;
            ptr->field_68 = v19;
            ptr->field_74 = v23;
            ptr->field_30 = v10 + v17 + v23;
            ptr->field_34 = v11 + v20 + v25;
            ptr->field_38 = v14 + v18 + v26;
            if (v7)
            {
                v27 = Transform__LookAt(v7, 0);
                if (ptr->field_80)
                {
                    if (!g_1fab3df)
                    {
                        sub_f7d92c("_F");
                        g_1fab3df = 1;
                    }
                    if (!g_1ef07e8->field_e0)
                        sub_f7da5c(g_1ef07e8);
                    v28 = ptr->field_3c;
                    v29 = (((CmpF(v28, 0.0) >> 5 & 3 | CmpF(v28, 0.0) & 1) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - ((CmpF(v28, 0.0) >> 5 & 3 | CmpF(v28, 0.0) & 1) & (CmpF(v28, 0.0) >> 5 & 3 | CmpF(v28, 0.0) & 1) >> 1 & 1);
                    v30 = ptr->field_40;
                    v31 = (((CmpF(v30, 0.0) >> 5 & 3 | CmpF(v30, 0.0) & 1) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - ((CmpF(v30, 0.0) >> 5 & 3 | CmpF(v30, 0.0) & 1) & (CmpF(v30, 0.0) >> 5 & 3 | CmpF(v30, 0.0) & 1) >> 1 & 1);
                    v32 = ptr->field_44;
                    v33 = (((CmpF(v32, 0.0) >> 5 & 3 | CmpF(v32, 0.0) & 1) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - ((CmpF(v32, 0.0) >> 5 & 3 | CmpF(v32, 0.0) & 1) & (CmpF(v32, 0.0) >> 5 & 3 | CmpF(v32, 0.0) & 1) >> 1 & 1);
                    v7 = ptr->field_28;
                    if (v7)
                    {
                        v27 = Transform__set_localScale(v7, 0);
                        goto LABEL_106aa14;
                    }
                }
                else
                {
LABEL_106aa14:
                    if (!ptr->field_20)
                        return v27;
                    v7 = ptr->field_28;
                    if (v7)
                    {
                        Transform__get_position(v7, 0);
                        if (!g_1eef458->field_e0)
                            sub_f7da5c(g_1eef458);
                        v0 = 0;
                        v1 = 0x3f8000003f800000;
                        Debug__DrawRay(0);
                        v7 = ptr->field_28;
                        if (v7)
                        {
                            Transform__get_position(v7, 0);
                            v0 = 0x3f80000000000000;
                            v1 = 0x3f80000000000000;
                            Debug__DrawRay(0);
                            if (!g_1fab32c)
                            {
                                sub_f7d92c(&g_1ef22e8);
                                g_1fab32c = 1;
                            }
                            v0 = 0x3f6bebec3f800000;
                            v1 = 4575657222423478401;
                            Debug__DrawRay(0);
                            if (!g_1fab32c)
                            {
                                sub_f7d92c(&g_1ef22e8);
                                g_1fab32c = 1;
                            }
                            v0 = 0x3f800000;
                            v1 = 0x3f80000000000000;
                            v34 = Debug__DrawRay(0);
                            return Debug__DrawRay(0);
                        }
                    }
                }
            }
        }
    }
    sub_f7db74(v7);
}
```

## `jiggleBones.ctor` — RVA `0xc6aba0`

- Decompiled symbol: `jiggleBones_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `52` bytes
- Result: `pseudocode`
- Heuristic layout hint: `jiggleBones_Recovered` matched 4 offsets against `jiggleBones` metadata (confidence 1.00).

```c
typedef struct jiggleBones_Recovered {
    char padding_0[32];
    char debugMode;
    char padding_21[27];
    uint128_t boneAxis;
    uint128_t bStiffness;
    char padding_5c[40];
    unsigned long long sideStretch;
} jiggleBones_Recovered;

long long jiggleBones_ctor(struct_0 *ptr)
{
    long long v0;  // x0

    ptr->field_20 = 1;
    *((uint128_t *)&(&ptr->padding_21)[1]) = 0x419000003f8000000000000000000000;
    *((uint128_t *)((char *)&ptr->field_3c + 12)) = 84073670752676845081235748548537210634;
    *((unsigned long long *)&ptr->padding_5c[36]) = 4489188110463768986;
    v0 = MonoBehaviour__ctor();
    return MonoBehaviour__ctor();
}
```
