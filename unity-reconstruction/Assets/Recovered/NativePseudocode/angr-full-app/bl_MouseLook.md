# Native pseudocode: bl_MouseLook

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `bl_MouseLook.Init` — RVA `0xce0880`

- Decompiled symbol: `bl_MouseLook_Init`
- Metadata signature: `public void Init(Transform character, Transform camera) { }`
- Native interval: `80` bytes
- Result: `pseudocode`

```c
long long bl_MouseLook_Init(unsigned int *ptr, long long a1, long long a2)
{
    unsigned int v0;  // s0
    unsigned int v1;  // s1
    unsigned int v2;  // s2
    unsigned int v3;  // s3
    unsigned long v4;  // x0

    if (a1)
    {
        Transform__get_localRotation(a1, 0);
        ptr[11] = v0;
        ptr[12] = v1;
        ptr[13] = v2;
        ptr[14] = v3;
        if (a2)
        {
            v4 = Transform__get_localRotation(a2, 0);
            ptr[15] = v0;
            ptr[16] = v1;
            ptr[17] = v2;
            ptr[18] = v3;
            return v4;
        }
    }
    sub_f7db74();
}
```

## `bl_MouseLook.LookRotation` — RVA `0xce1518`

- Decompiled symbol: `bl_MouseLook_LookRotation`
- Metadata signature: `public void LookRotation(Transform character, Transform camera) { }`
- Native interval: `804` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
    unsigned int field_14;
    char field_18;
    char padding_19[11];
    char field_24;
    char padding_25[3];
    unsigned int field_28;
    unsigned int field_2c;
    unsigned int field_30;
    unsigned int field_34;
    unsigned int field_38;
    unsigned int field_3c;
    unsigned int field_40;
    unsigned int field_44;
    unsigned int field_48;
} struct_0;

extern long long g_1f0c3a8;
extern long long g_1f0c3b0;
extern char g_1fab63e;

void bl_MouseLook_LookRotation(struct_0 *ptr, long long a1, long long a2)
{
    unsigned long long v17;  // d15
    unsigned long long v18;  // d14
    unsigned long long v27;  // x23
    unsigned long long v28;  // x22
    unsigned long long v29;  // x21
    unsigned long long v30;  // x20
    unsigned long long v31;  // x19
    unsigned int v32;  // s10
    unsigned int v33;  // s11
    unsigned int v34;  // s12
    unsigned int v35;  // s14
    unsigned int v36;  // s15
    unsigned long long v19;  // d13
    unsigned int v37;  // s0
    unsigned int v38;  // s1
    unsigned int v39;  // s8
    unsigned int v40;  // s9
    unsigned int v41;  // s3
    unsigned int v42;  // s3
    unsigned int v43;  // s10
    unsigned int v44;  // s11
    unsigned int v45;  // s0
    unsigned int v46;  // w8
    unsigned long long v20;  // d12
    unsigned int v47;  // s0
    unsigned int v48;  // s1
    unsigned int v49;  // s2
    unsigned int v50;  // s0
    unsigned long long v21;  // d11
    unsigned long long v22;  // d10
    unsigned long long v23;  // d9
    unsigned long long v24;  // d8
    unsigned long long v25;  // x30
    unsigned long long v26;  // x24
    unsigned int v0;  // [bp-0x90]
    unsigned long long v1;  // [bp-0x80]
    unsigned long long v2;  // [bp-0x78]
    unsigned long long v3;  // [bp-0x70]
    unsigned long long v4;  // [bp-0x68]
    unsigned long long v5;  // [bp-0x60]
    unsigned long long v6;  // [bp-0x58]
    unsigned long long v7;  // [bp-0x50]
    unsigned long long v8;  // [bp-0x48]
    unsigned long long v9;  // [bp-0x40]
    unsigned int v10;  // [bp-0x34]
    unsigned long long v11;  // [bp-0x30]
    unsigned long long v12;  // [bp-0x28]
    unsigned long long v13;  // [bp-0x20]
    unsigned long long v14;  // [bp-0x18]
    unsigned long long v15;  // [bp-0x10]
    unsigned long long v16;  // [bp-0x8]

    v1 = v17;
    v2 = v18;
    v3 = v19;
    v4 = v20;
    v5 = v21;
    v6 = v22;
    v7 = v23;
    v8 = v24;
    v9 = v25;
    v11 = v26;
    v12 = v27;
    v13 = v28;
    v14 = v29;
    v15 = v30;
    v16 = v31;
    if (!(g_1fab63e & 1))
    {
        sub_f7d92c(&g_1f0c3b0);
        sub_f7d92c(&g_1f0c3a8);
        g_1fab63e = 1;
    }
    Input__GetAxis(g_1f0c3a8, 0);
    Input__GetAxis(g_1f0c3b0, 0);
    v32 = ptr->field_14;
    v33 = ptr->field_2c;
    v34 = ptr->field_30;
    v35 = ptr->field_34;
    v36 = ptr->field_38;
    v38 = v37 * ptr->field_10 * 1016003125;
    Quaternion__Internal_FromEulerRad(0);
    v39 = ptr->field_3c;
    v40 = ptr->field_40;
    v42 = v33 * v38 + v36 * 0 + v35 * v41;
    v43 = ptr->field_44;
    v44 = ptr->field_48;
    ptr->field_34 = v42 - v34 * 0;
    ptr->field_38 = v36 * v41 - v33 * 0 - v34 * v38 - v35 * 0;
    v45 = v32 * -(v37) * 1016003125;
    ptr->field_2c = v34 * 0 + v36 * 0 + v33 * v41 - v35 * v38;
    ptr->field_30 = v35 * 0 + v36 * v38 + v34 * v41 - v33 * 0;
    Quaternion__Internal_FromEulerRad(0);
    v46 = ptr->field_18;
    v47 = v40 * 0 + v44 * v45 + v39 * v42 - v43 * 0;
    v48 = v43 * v45 + v44 * 0 + v40 * v42 - v39 * 0;
    v49 = v39 * 0 + v44 * 0 + v43 * v42 - v40 * v45;
    ptr->field_3c = v47;
    ptr->field_40 = v48;
    ptr->field_44 = v49;
    ptr->field_48 = v44 * v42 - v39 * v45 - v40 * 0 - v43 * 0;
    if (v46)
    {
        bl_MouseLook__ClampRotationAroundXAxis(ptr);
        ptr->field_3c = v47;
        ptr->field_40 = v48;
        ptr->field_44 = v49;
        ptr->field_48 = 0x3f800000;
    }
    if (ptr->field_24)
    {
        if (a1)
        {
            Transform__get_localRotation(a1, 0);
            v10 = v47;
            Time__get_deltaTime(0);
            v0 = ptr->field_28 * v47;
            v50 = v10;
            Quaternion__Slerp(0);
            Transform__set_localRotation(a1, 0);
            if (a2)
            {
                Transform__get_localRotation(a2, 0);
                v10 = v50;
                Time__get_deltaTime(0);
                v0 = ptr->field_28 * v50;
                Quaternion__Slerp(0);
                goto LABEL_10e1808;
            }
        }
    }
    else
    {
        if (a1 && (Transform__set_localRotation(a1, 0), a2))
        {
LABEL_10e1808:
            Transform__set_localRotation();
            return;
        }
    }
    sub_f7db74();
}
```

## `bl_MouseLook.ClampRotationAroundXAxis` — RVA `0xce1a94`

- Decompiled symbol: `bl_MouseLook_ClampRotationAroundXAxis`
- Metadata signature: `private Quaternion ClampRotationAroundXAxis(Quaternion q) { }`
- Native interval: `100` bytes
- Result: `pseudocode`

```c
void bl_MouseLook_ClampRotationAroundXAxis(unsigned int *ptr)
{
    unsigned int v0;  // s2
    unsigned int v1;  // s3
    unsigned int v2;  // s0
    unsigned int v3;  // s3
    unsigned int v4;  // s0
    unsigned long v5;  // 4158
    unsigned long v6;  // 4129

    atanf();
    v0 = ptr[7];
    v1 = ptr[8];
    v4 = v2 / v3 * 1122316001;
    v5 = arm64g_calculate_condition(192, (((((unsigned long long)(char)(CmpF(v4, v1)) >> 5 & 3 | (unsigned long long)(CmpF(v4, v1) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v4, v1)) >> 5 & 3 | (unsigned long long)(CmpF(v4, v1) & 1)) & ((unsigned long long)(char)(CmpF(v4, v1)) >> 5 & 3 | (unsigned long long)(CmpF(v4, v1) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    v6 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v4, v0)) >> 5 & 3 | (unsigned long long)(CmpF(v4, v0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v4, v0)) >> 5 & 3 | (unsigned long long)(CmpF(v4, v0) & 1)) & ((unsigned long long)(char)(CmpF(v4, v0)) >> 5 & 3 | (unsigned long long)(CmpF(v4, v0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if (!((char)v6))
    {
        tanf();
        return;
    }
    tanf();
    return;
}
```

## `bl_MouseLook.ctor` — RVA `0xce1af8`

- Decompiled symbol: `bl_MouseLook_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `44` bytes
- Result: `pseudocode`
- Heuristic layout hint: `bl_MouseLook_Recovered` matched 4 offsets against `bl_MouseLook` metadata (confidence 1.00).

```c
typedef struct bl_MouseLook_Recovered {
    char padding_0[16];
    unsigned long long XSensitivity;
    char clampVerticalRotation;
    char padding_19[3];
    unsigned long long MinimumX;
    char padding_24[4];
    unsigned int smoothTime;
} bl_MouseLook_Recovered;

long long bl_MouseLook_ctor(struct_0 *ptr)
{
    long long v0;  // x0

    ptr->field_10 = 0x4000000040000000;
    ptr->field_18 = 1;
    *((unsigned long long *)&(&ptr->padding_19)[1]) = 0x42b40000c2b40000;
    *((unsigned int *)&ptr->padding_24[0]) = 0x40a00000;
    v0 = Object__ctor();
    return Object__ctor();
}
```
