# Native pseudocode: SplitScreenCamAddOn

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `SplitScreenCamAddOn.OnEnable` — RVA `0xc64c18`

- Decompiled symbol: `SplitScreenCamAddOn_OnEnable`
- Metadata signature: `private void OnEnable() { }`
- Native interval: `88` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[40];
    unsigned long long field_28;
} struct_0;

extern long long g_1efcf30;
extern char g_1fab2f1;

void SplitScreenCamAddOn_OnEnable(struct_0 *ptr)
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
    if (!(g_1fab2f1 & 1))
    {
        sub_f7d92c(&g_1efcf30);
        g_1fab2f1 = 1;
    }
    ptr->field_28 = sub_1231bc8(ptr, g_1efcf30);
    sub_f7d8d0();
    return;
}
```

## `SplitScreenCamAddOn.OnDisable` — RVA `0xc64c70`

- Decompiled symbol: `SplitScreenCamAddOn_OnDisable`
- Metadata signature: `private void OnDisable() { }`
- Native interval: `132` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[40];
    long long field_28;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab2f2;

unsigned long long SplitScreenCamAddOn_OnDisable(struct_1 *a0)
{
    unsigned long long v0;  // x0

    if (!(g_1fab2f2 & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab2f2 = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v0 = Object__op_Inequality(a0->field_28, 0, 0);
    if (!((char)v0 & 1))
    {
        return v0;
    }
    else if (!a0->field_28)
    {
        sub_f7db74(0);
    }
}
```

## `SplitScreenCamAddOn.LateUpdate` — RVA `0xc64cf4`

- Decompiled symbol: `SplitScreenCamAddOn_LateUpdate`
- Metadata signature: `private void LateUpdate() { }`
- Native interval: `1192` bytes
- Result: `pseudocode`
- Heuristic layout hint: `SplitScreenCamAddOn_Recovered` matched 2 offsets against `SplitScreenCamAddOn` metadata (confidence 1.00).

```c
typedef struct SplitScreenCamAddOn_Recovered {
    char padding_0[40];
    unsigned long long cam;
    char preMult;
} SplitScreenCamAddOn_Recovered;

typedef struct struct_2 {
    char padding_0[12];
    unsigned long long field_c;
    unsigned int field_14;
} struct_2;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

typedef struct struct_3 {
    char padding_0[184];
    struct struct_2 *field_b8;
} struct_3;

extern struct_0 *g_1ef0c58;
extern struct_3 *g_1ef22e8;
extern char g_1fab1e1;
extern char g_1fab2c9;
extern char g_1fab2f3;

unsigned long long SplitScreenCamAddOn_LateUpdate(struct_1 *ptr)
{
    unsigned long long v38;  // x0
    unsigned long long v39;  // x0
    unsigned long long v40;  // x8
    int v41;  // q0
    uint128_t v42;  // q1
    uint128_t v43;  // q2
    uint128_t v44;  // q3
    unsigned long long v45;  // x0
    unsigned long v0;  // [bp-0x290]
    unsigned int v1;  // [bp-0x288]
    char v2;  // [bp-0x278]
    char v3;  // [bp-0x274]
    char v4;  // [bp-0x270]
    uint128_t v5;  // [bp-0x260]
    uint128_t v6;  // [bp-0x250]
    uint128_t v7;  // [bp-0x240]
    char v8;  // [bp-0x230]
    uint128_t v9;  // [bp-0x220]
    uint128_t v10;  // [bp-0x210]
    uint128_t v11;  // [bp-0x200]
    int v12;  // [bp-0x1f0]
    uint128_t v13;  // [bp-0x1e0]
    uint128_t v14;  // [bp-0x1d0]
    uint128_t v15;  // [bp-0x1c0]
    char v16;  // [bp-0x1b0]
    uint128_t v17;  // [bp-0x1a0]
    uint128_t v18;  // [bp-0x190]
    uint128_t v19;  // [bp-0x180]
    int v20;  // [bp-0x170]
    uint128_t v21;  // [bp-0x160]
    uint128_t v22;  // [bp-0x150]
    uint128_t v23;  // [bp-0x140]
    char v24;  // [bp-0x130]
    uint128_t v25;  // [bp-0x120]
    uint128_t v26;  // [bp-0x110]
    uint128_t v27;  // [bp-0x100]
    int v28;  // [bp-0xf0], Other Possible Types: char
    uint128_t v29;  // [bp-0xe0]
    uint128_t v30;  // [bp-0xd0]
    uint128_t v31;  // [bp-0xc0]
    int v32;  // [bp-0xb0]
    uint128_t v33;  // [bp-0xa0]
    uint128_t v34;  // [bp-0x90]
    uint128_t v35;  // [bp-0x80]
    char *v36;  // [bp-0x30]
    char v37;  // [bp+0x0]

    v36 = &v37;
    if (!(g_1fab2f3 & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab2f3 = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v38 = Object__op_Equality(ptr->field_28, 0, 0);
    if (((char)v38 & 1))
        return v38;
    v39 = ptr->field_28;
    if (v39)
    {
        Camera__get_rect(v39, 0);
        v39 = Screen__get_width(0);
        if (ptr->field_28)
        {
            Camera__get_rect(ptr->field_28, 0);
            Screen__get_height(0);
            sincosf(&v3, &v2);
            v39 = ptr->field_28;
            if (v39)
            {
                v39 = Camera__get_orthographic(v39, 0);
                v40 = ptr->field_28;
                if (((char)v39 & 1))
                {
                    if (v40 && (Camera__get_orthographicSize(v40, 0), v39 = ptr->field_28, v39 && (Camera__get_orthographicSize(v39, 0), v39 = ptr->field_28, v39 && (Camera__get_orthographicSize(v39, 0), v39 = ptr->field_28, v39 && (Camera__get_orthographicSize(v39, 0), v39 = ptr->field_28, v39 && (Camera__get_nearClipPlane(v39, 0), v39 = ptr->field_28, v39))))))
                    {
                        Camera__get_farClipPlane(v39, 0);
                        Matrix4x4__Ortho(0);
                        goto LABEL_1064f14;
                    }
                }
                else
                {
                    if (v40 && (Camera__get_fieldOfView(v40, 0), v39 = ptr->field_28, v39 && (Camera__get_nearClipPlane(v39, 0), v39 = ptr->field_28, v39)))
                    {
                        Camera__get_farClipPlane(v39, 0);
                        Matrix4x4__Perspective(0);
LABEL_1064f14:
                        memcpy(&v32, &v28, 16);
                        v33 = v29;
                        v34 = v30;
                        v35 = v31;
                        if (ptr->field_30)
                        {
                            if (!g_1fab2c9)
                            {
                                sub_f7d92c(&g_1ef22e8);
                                g_1fab2c9 = 1;
                            }
                            Quaternion__Internal_FromEulerRad(0);
                            if (!g_1fab1e1)
                            {
                                sub_f7d92c(&g_1ef22e8);
                                g_1fab1e1 = 1;
                            }
                            v1 = *((int *)((char *)&g_1ef22e8->field_b8->field_c + 4));
                            v0 = *((long long *)&(&g_1ef22e8->field_b8->padding_0)[1]);
                            Matrix4x4__TRS(0);
                            memcpy(&v24, &v28, 16);
                            v25 = v29;
                            v26 = v30;
                            v27 = v31;
                            v20 = v32;
                            v21 = v33;
                            v22 = v34;
                            v23 = v35;
                            Matrix4x4__op_Multiply(&v24, &v20, 0);
                            v41 = (int)v28;
                            v42 = v29;
                            v43 = v30;
                            v44 = v31;
                        }
                        else
                        {
                            memcpy(&v28, &v32, 16);
                            v29 = v33;
                            v30 = v34;
                            v31 = v35;
                            if (!g_1fab2c9)
                            {
                                sub_f7d92c(&g_1ef22e8);
                                g_1fab2c9 = 1;
                            }
                            Quaternion__Internal_FromEulerRad(0);
                            if (!g_1fab1e1)
                            {
                                sub_f7d92c(&g_1ef22e8);
                                g_1fab1e1 = 1;
                            }
                            v1 = *((int *)((char *)&g_1ef22e8->field_b8->field_c + 4));
                            v0 = *((long long *)&(&g_1ef22e8->field_b8->padding_0)[1]);
                            Matrix4x4__TRS(0);
                            memcpy(&v8, &v16, 16);
                            v9 = v17;
                            v10 = v18;
                            v11 = v19;
                            v12 = v28;
                            v13 = v29;
                            v14 = v30;
                            v15 = v31;
                            Matrix4x4__op_Multiply(&v12, &v8, 0);
                            v41 = (int)v16;
                            v42 = v17;
                            v43 = v18;
                            v44 = v19;
                        }
                        v32 = v41;
                        v33 = v42;
                        v34 = v43;
                        v35 = v44;
                        v39 = ptr->field_28;
                        memcpy(&v28, &v32, 16);
                        v29 = v33;
                        v30 = v34;
                        v31 = v35;
                        if (v39)
                        {
                            memcpy(&v4, &v28, 16);
                            v5 = v29;
                            v6 = v30;
                            v7 = v31;
                            v45 = Camera__set_projectionMatrix(v39, &v4, 0);
                            return Camera__set_projectionMatrix(v39, &v4, 0);
                        }
                    }
                }
            }
        }
    }
    sub_f7db74(v39);
}
```

## `SplitScreenCamAddOn.ctor` — RVA `0xc6519c`

- Decompiled symbol: `SplitScreenCamAddOn_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `16` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[48];
    char field_30;
} struct_0;

long long SplitScreenCamAddOn_ctor(struct_0 *ptr)
{
    unsigned long long v0;  // x0

    ptr->field_30 = 1;
    v0 = MonoBehaviour__ctor();
    return MonoBehaviour__ctor();
}
```
