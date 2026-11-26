# Native pseudocode: bl_LoadingScreenUI

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `bl_LoadingScreenUI.Init` — RVA `0xc76910`

- Decompiled symbol: `bl_LoadingScreenUI_Init`
- Metadata signature: `public void Init(bl_SceneLoader loader) { }`
- Native interval: `844` bytes
- Result: `pseudocode`
- Heuristic layout hint: `bl_LoadingScreenUI_Recovered` matched 14 offsets against `bl_LoadingScreenUI` metadata (confidence 1.00).

```c
typedef struct bl_LoadingScreenUI_Recovered {
    char padding_0[64];
    struct struct_2 *BackgroundImage;
    struct struct_3 *FilledImage;
    struct struct_4 *LoadBarSlider;
    struct struct_5 *ContinueUI;
    struct struct_6 *RootUI;
    struct struct_7 *FlashImage;
    struct struct_8 *SkipKeyText;
    char padding_78[16];
    struct struct_9 *FadeImageCanvas;
    long long k__BackingField;
    long long BackgroundAlpha;
    long long LoadingBarAlpha;
    struct struct_10 *Manager;
    long long m_SceneLoader;
    long long cacheTips;
} bl_LoadingScreenUI_Recovered;

typedef struct struct_1 {
    char padding_0[32];
    unsigned long long field_20;
} struct_1;

typedef struct struct_2 {
    char padding_0[32];
    unsigned long long field_20;
} struct_2;

typedef struct struct_3 {
    char padding_0[32];
    unsigned long long field_20;
} struct_3;

typedef struct struct_4 {
    char padding_0[32];
    unsigned long long field_20;
} struct_4;

typedef struct struct_5 {
    char padding_0[32];
    unsigned long long field_20;
} struct_5;

typedef struct struct_6 {
    char padding_0[32];
    unsigned long long field_20;
} struct_6;

typedef struct struct_7 {
    char padding_0[32];
    unsigned long long field_20;
} struct_7;

typedef struct struct_8 {
    char padding_0[32];
    unsigned long long field_20;
} struct_8;

typedef struct struct_9 {
    char padding_0[32];
    unsigned long long field_20;
} struct_9;

typedef struct struct_10 {
    char padding_0[32];
    long long field_20;
} struct_10;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern long long g_1efcf48;
extern long long g_1efeb78;
extern char g_1fab3b5;

void bl_LoadingScreenUI_Init(struct_11 *ptr, long long a1)
{
    unsigned long long v5;  // x30
    unsigned long long v6;  // x22
    long long v15;  // x0
    struct_11 *addr;  // x21
    struct_11 *v17;  // x21
    long long v18;  // x1
    struct_11 *ptr3;  // x0
    long long v20;  // x1
    struct_11 *ptr4;  // x0
    unsigned long v23;  // x1
    struct_11 *ptr5;  // x0
    unsigned long long v7;  // x21
    unsigned long long v8;  // x20
    unsigned long long v9;  // x19
    struct_11 *ptr6;  // x0
    struct_1 *v11;  // x1
    struct_11 *ptr7;  // x20
    struct_11 *p;  // x20
    struct_1 *v14;  // x0
    unsigned long long v0;  // [bp-0x30]
    unsigned long long v1;  // [bp-0x20]
    unsigned long long v2;  // [bp-0x18]
    unsigned long long v3;  // [bp-0x10]
    unsigned long long v4;  // [bp-0x8]

    v0 = v5;
    v1 = v6;
    v2 = v7;
    v3 = v8;
    v4 = v9;
    if (!(g_1fab3b5 & 1))
    {
        sub_f7d92c(&g_1efcf48);
        sub_f7d92c(&g_1efeb78);
        sub_f7d92c(&g_1ef0c58);
        g_1fab3b5 = 1;
    }
    ptr6 = ptr;
    ptr6->field_b0 = a1;
    sub_f7d8d0((struct bl_LoadingScreenUI_Recovered *)&ptr6->field_b0, a1);
    v11 = bl_SceneLoaderManager__get_Instance(0);
    ptr7 = ptr;
    ptr7->field_a8 = v11;
    p = &ptr7->field_a8;
    sub_f7d8d0(p, v11);
    v14 = p->field_48;
    if (v14)
    {
        v15 = sub_1249224(v14, g_1efeb78);
        addr = ptr;
        addr->field_90 = v15;
        v17 = &addr->field_90;
        sub_f7d8d0(v17, v15);
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        if (((char)Object__op_Inequality(v17->field_40, 0, 0) & 1))
        {
            v14 = ptr->field_50;
            if (v14)
            {
                v18 = sub_1231bc8(v14, g_1efcf48);
                ptr3 = ptr;
                ptr3->field_a0 = v18;
                sub_f7d8d0((struct bl_LoadingScreenUI_Recovered *)&ptr3->field_a0, v18);
                goto LABEL_1076a0c;
            }
        }
        else
        {
LABEL_1076a0c:
            if (!g_1ef0c58->field_e0)
                sub_f7da5c(g_1ef0c58);
            if (((char)Object__op_Inequality(ptr->field_40, 0, 0) & 1))
            {
                v14 = ptr->field_40;
                if (v14)
                {
                    v20 = sub_1231bc8(v14, g_1efcf48);
                    ptr4 = ptr;
                    ptr4->field_98 = v20;
                    sub_f7d8d0((struct bl_LoadingScreenUI_Recovered *)&ptr4->field_98, v20);
                    goto LABEL_1076a5c;
                }
            }
            else
            {
LABEL_1076a5c:
                v14 = ptr->field_60;
                if (v14)
                {
                    GameObject__SetActive(v14, 0, 0);
                    if (!g_1ef0c58->field_e0)
                        sub_f7da5c(g_1ef0c58);
                    if (((char)Object__op_Inequality(ptr->field_58, 0, 0) & 1))
                    {
                        v14 = ptr->field_58;
                        if (v14)
                        {
                            GameObject__SetActive(v14, 0, 0);
                            goto LABEL_1076aac;
                        }
                    }
                    else
                    {
LABEL_1076aac:
                        if (!g_1ef0c58->field_e0)
                            sub_f7da5c(g_1ef0c58);
                        if (((char)Object__op_Inequality(ptr->field_68, 0, 0) & 1))
                        {
                            v14 = ptr->field_68;
                            if (v14)
                            {
                                GameObject__SetActive(v14, 0, 0);
                                goto LABEL_1076ae8;
                            }
                        }
                        else
                        {
LABEL_1076ae8:
                            if (!g_1ef0c58->field_e0)
                                sub_f7da5c(g_1ef0c58);
                            if (((char)Object__op_Inequality(ptr->field_88, 0, 0) & 1))
                            {
                                v14 = ptr->field_88;
                                if (v14)
                                {
                                    CanvasGroup__set_alpha(v14, 0);
                                    MonoBehaviour__StartCoroutine(ptr, bl_LoadingScreenUI__FadeOutCanvas(ptr, ptr->field_88), 0);
                                    goto LABEL_1076b44;
                                }
                            }
                            else
                            {
LABEL_1076b44:
                                if (!g_1ef0c58->field_e0)
                                    sub_f7da5c(g_1ef0c58);
                                if (((char)Object__op_Inequality(ptr->field_70, 0, 0) & 1))
                                {
                                    v14 = ptr->field_70;
                                    if (v14)
                                    {
                                        GameObject__SetActive(v14, 0, 0);
                                        goto LABEL_1076b80;
                                    }
                                }
                                else
                                {
LABEL_1076b80:
                                    v14 = *((long long *)&p->padding_0[0]);
                                    if (v14)
                                    {
                                        v14 = bl_SceneLoaderManager__get_HasTips(v14, 0);
                                        if (!((char)v14 & 1))
                                        {
LABEL_1076bac:
                                            if (!g_1ef0c58->field_e0)
                                                sub_f7da5c(g_1ef0c58);
                                            if (!((char)Object__op_Inequality(ptr->field_48, 0, 0) & 1))
                                            {
LABEL_1076bfc:
                                                bl_LoadingScreenUI__get_Source(ptr);
                                            }
                                            v14 = ptr->field_48;
                                            if (v14 && (Image__set_type(v14, 3, 0), v14 = (struct_1 *)ptr->field_48, v14))
                                            {
                                                Image__set_fillAmount(v14, 0);
                                                goto LABEL_1076bfc;
                                            }
                                        }
                                        else if (*((long long *)&p->padding_0[0]))
                                        {
                                            v23 = *((long long *)(*((long long *)&p->padding_0[0]) + 32));
                                            ptr5 = ptr;
                                            ptr5->field_b8 = v23;
                                            sub_f7d8d0((struct bl_LoadingScreenUI_Recovered *)&ptr5->field_b8, v23);
                                            goto LABEL_1076bac;
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
    sub_f7db74(v14);
}
```

## `bl_LoadingScreenUI.OnUpdate` — RVA `0xc76e50`

- Decompiled symbol: `bl_LoadingScreenUI_OnUpdate`
- Metadata signature: `public void OnUpdate() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long bl_LoadingScreenUI_OnUpdate(unsigned long a0)
{
    unsigned long long v0;  // x0

    v0 = bl_LoadingScreenUI__LoadingRotator();
    return bl_LoadingScreenUI__LoadingRotator();
}
```

## `bl_LoadingScreenUI.UpdateLoadProgress` — RVA `0xc76fcc`

- Decompiled symbol: `bl_LoadingScreenUI_UpdateLoadProgress`
- Metadata signature: `public void UpdateLoadProgress(float value, float delayedValue) { }`
- Native interval: `372` bytes
- Result: `pseudocode`
- Heuristic layout hint: `bl_LoadingScreenUI_Recovered` matched 4 offsets against `bl_LoadingScreenUI` metadata (confidence 1.00).

```c
typedef struct bl_LoadingScreenUI_Recovered {
    char padding_0[48];
    struct struct_7 *ProgressText;
    char padding_38[16];
    struct struct_8 *FilledImage;
    struct struct_8 *LoadBarSlider;
    char padding_58[88];
    struct struct_5 *m_SceneLoader;
} bl_LoadingScreenUI_Recovered;

typedef struct struct_3 {
    char padding_0[1064];
    struct struct_4 *field_428;
    unsigned long long field_430;
} struct_3;

typedef struct struct_5 {
    char padding_0[104];
    long long field_68;
} struct_5;

typedef struct struct_1 {
    char padding_0[1512];
    struct struct_2 *field_5e8;
    unsigned long long field_5f0;
} struct_1;

typedef struct struct_7 {
    struct struct_1 *field_0;
} struct_7;

typedef struct struct_8 {
    struct struct_3 *field_0;
} struct_8;

typedef struct struct_4 {
    unsigned long long field_0;
} struct_4;

typedef struct struct_2 {
    unsigned long long field_0;
} struct_2;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern long long g_1f0a1e8;
extern char g_1fab3b8;

long long bl_LoadingScreenUI_UpdateLoadProgress(struct_6 *ptr)
{
    struct_3 **v1;  // x0
    unsigned long long flag;  // x2
    unsigned long long v3;  // x1
    long long v4;  // x0
    unsigned int v5;  // s1
    struct_1 **v6;  // x19
    struct_3 **v7;  // x1
    struct_1 **v8;  // x0
    unsigned long long v9;  // x2
    unsigned int v0;  // [bp-0x34]

    if (!(g_1fab3b8 & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c(&g_1f0a1e8);
        g_1fab3b8 = 1;
    }
    v0 = 0;
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (((char)Object__op_Inequality(ptr->field_48, 0, 0) & 1))
    {
        v1 = ptr->field_48;
        if (!v1)
            sub_f7db74(v1);
        Image__set_fillAmount(v1, 0);
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    flag = 0;
    if (((char)Object__op_Inequality(ptr->field_50, 0, 0) & 1))
    {
        v1 = ptr->field_50;
        if (v1)
        {
            v3 = *(v1)->field_430;
            *(v1)->field_428();
        }
    }
    else
    {
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        v4 = Object__op_Inequality(ptr->field_30, 0, 0);
        if (!((char)v4 & 1))
            return v4;
        v0 = v5 * 0x42c80000;
        v1 = Single__ToString(&v0, g_1f0a1e8, 0);
        if (ptr->field_b0)
        {
            v6 = ptr->field_30;
            v1 = String__Format(ptr->field_b0->field_68, v1, 0);
            if (v6)
            {
                v7 = v1;
                v8 = v6;
                v9 = *(v6)->field_5f0;
                *(v6)->field_5e8();
            }
        }
    }
    sub_f7db74(v1);
}
```

## `bl_LoadingScreenUI.OnFinish` — RVA `0xc77224`

- Decompiled symbol: `bl_LoadingScreenUI_OnFinish`
- Metadata signature: `public void OnFinish() { }`
- Native interval: `404` bytes
- Result: `pseudocode`
- Heuristic layout hint: `bl_LoadingScreenUI_Recovered` matched 8 offsets against `bl_LoadingScreenUI` metadata (confidence 1.00).

```c
typedef struct bl_LoadingScreenUI_Recovered {
    char padding_0[72];
    long long FilledImage;
    long long LoadBarSlider;
    long long ContinueUI;
    char padding_60[8];
    unsigned long long FlashImage;
    long long SkipKeyText;
    char padding_78[8];
    long long LoadingCircleCanvas;
    char padding_88[24];
    long long LoadingBarAlpha;
    char padding_a8[8];
    struct struct_2 *m_SceneLoader;
} bl_LoadingScreenUI_Recovered;

typedef struct struct_2 {
    char padding_0[32];
    unsigned int field_20;
    char padding_24[48];
    char field_54;
    char padding_55[107];
    struct struct_1 *field_c0;
} struct_2;

typedef struct struct_1 {
    char padding_0[40];
    unsigned int field_28;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab3ba;

unsigned long long bl_LoadingScreenUI_OnFinish(struct_3 *ptr)
{
    struct_2 *p;  // x8
    unsigned int flag;  // w9
    long long v2;  // x0
    unsigned long long v5;  // x0

    if (!(g_1fab3ba & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab3ba = 1;
    }
    p = ptr->field_b0;
    if (p)
    {
        if ((!p->field_c0 || (flag = p->field_c0->field_28, !flag)) && (flag = p->field_20, !flag))
            goto LABEL_1077294;
        switch (flag)
        {
        case 4:
LABEL_1077294:
            v2 = ptr->field_70;
            if (v2)
            {
LABEL_107729c:
                GameObject__SetActive(v2, 1, 0);
            }
            break;
        case 1:
            v2 = ptr->field_58;
            if (v2)
                goto LABEL_107729c;
            break;
        default:
            goto LABEL_10772a8;
        }
LABEL_10772a8:
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        if (((char)Object__op_Inequality(ptr->field_80, 0, 0) & 1))
            MonoBehaviour__StartCoroutine(ptr, bl_LoadingScreenUI__FadeOutCanvas(ptr, ptr->field_80), 0);
        if (ptr->field_b0)
        {
            if (ptr->field_b0->field_54)
            {
                if (!g_1ef0c58->field_e0)
                    sub_f7da5c(g_1ef0c58);
                if (((char)Object__op_Inequality(ptr->field_a0, 0, 0) & 1))
                {
                    MonoBehaviour__StartCoroutine(ptr, bl_LoadingScreenUI__FadeOutCanvas(ptr, ptr->field_a0), 0);
                }
                else
                {
                    if (ptr->field_50 && Component__get_gameObject(ptr->field_50, 0))
                        GameObject__SetActive();
                    if (ptr->field_48 && Component__get_gameObject(ptr->field_48, 0))
                        GameObject__SetActive();
                }
            }
            if (!ptr->field_68)
                return 0;
            v5 = GameObject__SetActive();
            return GameObject__SetActive();
        }
    }
    sub_f7db74();
}
```

## `bl_LoadingScreenUI.SetupUIForScene` — RVA `0xc77464`

- Decompiled symbol: `bl_LoadingScreenUI_SetupUIForScene`
- Metadata signature: `public void SetupUIForScene(bl_SceneLoaderInfo info) { }`
- Native interval: `1052` bytes
- Result: `pseudocode`
- Heuristic layout hint: `bl_LoadingScreenUI_Recovered` matched 13 offsets against `bl_LoadingScreenUI` metadata (confidence 1.00).

```c
typedef struct bl_LoadingScreenUI_Recovered {
    char padding_0[32];
    struct struct_18 *SceneNameText;
    struct struct_19 *DescriptionText;
    struct struct_20 *ProgressText;
    struct struct_21 *TipText;
    struct struct_22 *BackgroundImage;
    char padding_48[8];
    struct struct_23 *LoadBarSlider;
    char padding_58[8];
    long long RootUI;
    char padding_68[40];
    long long k__BackingField;
    char padding_98[16];
    long long Manager;
    struct struct_15 *m_SceneLoader;
    struct struct_16 *cacheTips;
    long long cacheBackgrounds;
    char padding_c8[4];
    unsigned int CurrentTip;
} bl_LoadingScreenUI_Recovered;

typedef struct struct_15 {
    char padding_0[49];
    char field_31;
    char field_32;
    char padding_33[21];
    char field_48;
    char padding_49[31];
    long long field_68;
} struct_15;

typedef struct struct_25 {
    char padding_0[24];
    unsigned long long field_18;
    unsigned long long field_20;
    char padding_28[16];
    struct struct_24 *field_38;
} struct_25;

typedef struct struct_24 {
    char padding_0[24];
    unsigned long long field_18;
    long long field_20;
} struct_24;

typedef struct struct_11 {
    char padding_0[680];
    struct struct_12 *field_2a8;
    unsigned long long field_2b0;
} struct_11;

typedef struct struct_3 {
    char padding_0[1512];
    struct struct_4 *field_5e8;
    unsigned long long field_5f0;
} struct_3;

typedef struct struct_5 {
    char padding_0[1512];
    struct struct_6 *field_5e8;
    unsigned long long field_5f0;
} struct_5;

typedef struct struct_13 {
    char padding_0[1064];
    struct struct_14 *field_428;
    unsigned long long field_430;
} struct_13;

typedef struct struct_7 {
    char padding_0[1512];
    struct struct_8 *field_5e8;
    unsigned long long field_5f0;
} struct_7;

typedef struct struct_16 {
    char padding_0[24];
    unsigned int field_18;
} struct_16;

typedef struct struct_9 {
    char padding_0[1512];
    struct struct_10 *field_5e8;
    unsigned long long field_5f0;
} struct_9;

typedef struct struct_18 {
    struct struct_3 *field_0;
} struct_18;

typedef struct struct_19 {
    struct struct_5 *field_0;
} struct_19;

typedef struct struct_20 {
    struct struct_7 *field_0;
} struct_20;

typedef struct struct_21 {
    struct struct_9 *field_0;
} struct_21;

typedef struct struct_22 {
    struct struct_11 *field_0;
} struct_22;

typedef struct struct_23 {
    struct struct_13 *field_0;
} struct_23;

typedef struct struct_12 {
    unsigned long long field_0;
} struct_12;

typedef struct struct_4 {
    unsigned long long field_0;
} struct_4;

typedef struct struct_6 {
    unsigned long long field_0;
} struct_6;

typedef struct struct_14 {
    unsigned long long field_0;
} struct_14;

typedef struct struct_8 {
    unsigned long long field_0;
} struct_8;

typedef struct struct_10 {
    unsigned long long field_0;
} struct_10;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern long long g_1ef0450;
extern struct_0 *g_1ef0c58;
extern long long g_1ef85c0;
extern long long g_1ef8688;
extern long long g_1ef8690;
extern char g_1fab3bb;

void bl_LoadingScreenUI_SetupUIForScene(struct_17 *ptr, struct_25 *p)
{
    unsigned long long v6;  // x30
    unsigned long long v7;  // x22
    struct_11 **v16;  // x0
    unsigned long long v17;  // x1
    struct_3 **v18;  // x0
    unsigned long long v19;  // x1
    unsigned long long v20;  // x2
    struct_5 **v21;  // x0
    unsigned long long v22;  // x1
    unsigned long long v23;  // x2
    unsigned long long v24;  // x2
    unsigned long long v25;  // x1
    unsigned long long v8;  // x21
    unsigned long long choice;  // x2
    struct_13 **v27;  // x0
    unsigned long long v28;  // x1
    struct_7 **v29;  // x20
    long long v30;  // x0
    unsigned long v31;  // x0
    unsigned long v32;  // x1
    struct_7 **v33;  // x0
    unsigned long long v34;  // x2
    unsigned int v35;  // w0
    unsigned long long v9;  // x20
    struct_16 *v36;  // x8
    struct_9 **v37;  // x20
    unsigned long v38;  // x0
    unsigned long v39;  // x1
    struct_9 **v40;  // x0
    unsigned long long v41;  // x2
    unsigned long long v10;  // x19
    unsigned long v11;  // x0
    struct_24 *addr;  // x1
    unsigned long long v13;  // x8
    unsigned long long v14;  // x2
    unsigned long long v0;  // [bp-0x30]
    unsigned int flag;  // [bp-0x24]
    unsigned long long v2;  // [bp-0x20]
    unsigned long long v3;  // [bp-0x18]
    unsigned long long v4;  // [bp-0x10]
    unsigned long long v5;  // [bp-0x8]

    v0 = v6;
    v2 = v7;
    v3 = v8;
    v4 = v9;
    v5 = v10;
    if (!(g_1fab3bb & 1))
    {
        sub_f7d92c(&g_1ef0450);
        sub_f7d92c(&g_1ef85c0);
        sub_f7d92c(&g_1ef8688);
        sub_f7d92c(&g_1ef8690);
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c("MT");
        g_1fab3bb = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v11 = Object__op_Inequality(ptr->field_40, 0, 0);
    if (!((char)v11 & 1))
    {
LABEL_10775a4:
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        if (((char)Object__op_Inequality(ptr->field_20, 0, 0) & 1))
        {
            if (p)
            {
                v18 = ptr->field_20;
                if (v18)
                {
                    v19 = p->field_18;
                    v20 = *(v18)->field_5f0;
                    *(v18)->field_5e8();
                }
            }
        }
        else
        {
            if (!g_1ef0c58->field_e0)
                sub_f7da5c(g_1ef0c58);
            if (((char)Object__op_Inequality(ptr->field_28, 0, 0) & 1))
            {
                if (ptr->field_b0)
                {
                    v21 = ptr->field_28;
                    if (ptr->field_b0->field_32)
                    {
                        if (p && v21)
                        {
                            v22 = p->field_20;
                            v23 = *(v21)->field_5f0;
                            *(v21)->field_5e8();
                        }
                    }
                    else
                    {
                        if (v21)
                        {
                            v24 = *(v21)->field_5f0;
                            v25 = g_1ef18f0->field_b8->field_0;
                            *(v21)->field_5e8();
                        }
                    }
                }
            }
            else
            {
                if (!g_1ef0c58->field_e0)
                    sub_f7da5c(g_1ef0c58);
                choice = 0;
                if (((char)Object__op_Inequality(ptr->field_50, 0, 0) & 1))
                {
                    v27 = ptr->field_50;
                    if (v27)
                    {
                        v28 = *(v27)->field_430;
                        *(v27)->field_428();
                    }
                }
                else
                {
                    if (!g_1ef0c58->field_e0)
                        sub_f7da5c(g_1ef0c58);
                    if (((char)Object__op_Inequality(ptr->field_30, 0, 0) & 1))
                    {
                        if (ptr->field_b0)
                        {
                            v29 = ptr->field_30;
                            flag = 0;
                            v30 = sub_f7da64(g_1ef0450, &flag);
                            v31 = String__Format(ptr->field_b0->field_68, v30, 0);
                            if (v29)
                            {
                                v32 = v31;
                                v33 = v29;
                                v34 = *(v29)->field_5f0;
                                *(v29)->field_5e8();
                            }
                        }
                    }
                    else
                    {
                        if (ptr->field_a8)
                        {
                            if (((char)bl_SceneLoaderManager__get_HasTips(ptr->field_a8, 0) & 1))
                            {
                                if (!g_1ef0c58->field_e0)
                                    sub_f7da5c(g_1ef0c58);
                                if (!(Object__op_Inequality(ptr->field_38, 0, 0) & 1))
                                    goto LABEL_1077810;
                                if (ptr->field_b0)
                                {
                                    if (ptr->field_b0->field_48)
                                    {
                                        if (ptr->field_b8 && !((v35 = (unsigned int)(unsigned long long)Random__Range(0, (unsigned long long)ptr->field_b8->field_18, 0), v36 = (struct_16 *)ptr->field_b8, ptr->field_cc = (unsigned int)(unsigned long long)Random__Range(0, (unsigned long long)ptr->field_b8->field_18, 0), !ptr->field_b8)))
                                        {
                                            v37 = ptr->field_38;
                                            goto LABEL_10777d8;
                                        }
                                    }
                                    else
                                    {
                                        if (ptr->field_b8)
                                        {
                                            v37 = ptr->field_38;
LABEL_10777d8:
                                            v38 = sub_14a30c0();
                                            if (v37)
                                            {
                                                v39 = v38;
                                                v40 = v37;
                                                v41 = *(v37)->field_5f0;
                                                *(v37)->field_5e8();
                                            }
                                        }
                                    }
                                }
                            }
                            else
                            {
LABEL_1077810:
                                if (ptr->field_90)
                                {
                                    CanvasGroup__set_alpha(ptr->field_90, 0);
                                    if (ptr->field_60)
                                    {
                                        GameObject__SetActive(ptr->field_60, 1, 0);
                                        bl_LoadingScreenUI__get_Source(ptr);
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    else if (ptr->field_b0)
    {
        if (!ptr->field_b0->field_31)
            goto LABEL_10775a4;
        if (p && !((addr = (struct_24 *)p->field_38, !addr)))
        {
            v13 = addr->field_18;
            if (2 > (unsigned int)v13)
            {
                if (!v13)
                    goto LABEL_10775a4;
                if (!(unsigned int)v13)
                    goto LABEL_107787c;
                if (ptr->field_40)
                {
                    v14 = 0;
                    Image__set_sprite(ptr->field_40, addr->field_20, 0);
LABEL_107757c:
                    v16 = ptr->field_40;
                    if (v16)
                    {
                        v17 = *(v16)->field_2b0;
                        *(v16)->field_2a8();
                    }
                }
            }
            else if (ptr->field_c0)
            {
                sub_14a359c(ptr->field_c0);
                v14 = 0;
                MonoBehaviour__StartCoroutine(ptr, bl_LoadingScreenUI__BackgroundTransition(ptr), 0);
                goto LABEL_107757c;
            }
        }
    }
    v11 = sub_f7db74();
LABEL_107787c:
    sub_f7db7c(v11);
}
```

## `bl_LoadingScreenUI.ResetUI` — RVA `0xc779c4`

- Decompiled symbol: `bl_LoadingScreenUI_ResetUI`
- Metadata signature: `public void ResetUI() { }`
- Native interval: `72` bytes
- Result: `pseudocode`
- Heuristic layout hint: `bl_LoadingScreenUI_Recovered` matched 4 offsets against `bl_LoadingScreenUI` metadata (confidence 1.00).

```c
typedef struct bl_LoadingScreenUI_Recovered {
    char padding_0[48];
    struct struct_7 *ProgressText;
    char padding_38[16];
    struct struct_8 *FilledImage;
    struct struct_8 *LoadBarSlider;
    char padding_58[88];
    struct struct_5 *m_SceneLoader;
} bl_LoadingScreenUI_Recovered;

typedef struct struct_7 {
    struct struct_1 *field_0;
} struct_7;

typedef struct struct_8 {
    struct struct_3 *field_0;
} struct_8;

typedef struct struct_5 {
    char padding_0[104];
    long long field_68;
} struct_5;

typedef struct struct_1 {
    char padding_0[1512];
    struct struct_2 *field_5e8;
    unsigned long long field_5f0;
} struct_1;

typedef struct struct_3 {
    char padding_0[1064];
    struct struct_4 *field_428;
    unsigned long long field_430;
} struct_3;

typedef struct struct_2 {
    unsigned long long field_0;
} struct_2;

typedef struct struct_4 {
    unsigned long long field_0;
} struct_4;

void bl_LoadingScreenUI_ResetUI(struct_6 *ptr)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    unsigned long v4;  // x0
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    v4 = *((long long *)&ptr->padding_58[48]);
    if (v4)
    {
        CanvasGroup__set_alpha(v4, 0);
        bl_LoadingScreenUI__UpdateLoadProgress(ptr);
        v4 = *((long long *)&ptr->padding_58[8]);
        if (*((long long *)&ptr->padding_58[8]))
        {
            GameObject__SetActive();
            return;
        }
    }
    sub_f7db74(v4);
}
```

## `bl_LoadingScreenUI.TransitionToScene` — RVA `0xc77a0c`

- Decompiled symbol: `bl_LoadingScreenUI_TransitionToScene`
- Metadata signature: `public void TransitionToScene() { }`
- Native interval: `60` bytes
- Result: `pseudocode`

```c
void bl_LoadingScreenUI_TransitionToScene(long long a0)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    MonoBehaviour__StartCoroutine(a0, bl_LoadingScreenUI__FadeAudio(), 0);
    bl_LoadingScreenUI__LoadNextSceneIE(a0);
    MonoBehaviour__StartCoroutine();
    return;
}
```

## `bl_LoadingScreenUI.get_RootAlpha` — RVA `0xc782ec`

- Decompiled symbol: `bl_LoadingScreenUI_get_RootAlpha`
- Metadata signature: `public CanvasGroup get_RootAlpha() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[144];
    unsigned long long field_90;
} struct_0;

long long bl_LoadingScreenUI_get_RootAlpha(struct_0 *a0)
{
    return a0->field_90;
}
```

## `bl_LoadingScreenUI.set_RootAlpha` — RVA `0xc782f4`

- Decompiled symbol: `bl_LoadingScreenUI_set_RootAlpha`
- Metadata signature: `public void set_RootAlpha(CanvasGroup value) { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[144];
    unsigned long long field_90;
} struct_0;

long long bl_LoadingScreenUI_set_RootAlpha(struct_0 *ptr, unsigned long a1)
{
    long long v0;  // x0

    ptr->field_90 = a1;
    v0 = sub_f7d8d0();
    return sub_f7d8d0();
}
```

## `bl_LoadingScreenUI.FadeOutCanvas` — RVA `0xc782fc`

- Decompiled symbol: `bl_LoadingScreenUI_FadeOutCanvas`
- Metadata signature: `private IEnumerator FadeOutCanvas(CanvasGroup alpha, float delay = 0.0) { }`
- Native interval: `152` bytes
- Result: `pseudocode`
- Heuristic layout hint: `bl_LoadingScreenUI_Recovered` matched 3 offsets against `bl_LoadingScreenUI` metadata (confidence 0.75).

```c
typedef struct bl_LoadingScreenUI_Recovered {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[12];
    unsigned int SceneNameText;
    char padding_24[4];
    long long DescriptionText;
    long long ProgressText;
} bl_LoadingScreenUI_Recovered;

extern long long g_1ef4170;
extern char g_1fab3c1;

struct_0 * bl_LoadingScreenUI_FadeOutCanvas(long long a0, long long a1)
{
    struct_0 *v0;  // x21
    struct_0 *p;  // x0
    struct_0 *ptr;  // x0
    unsigned int v3;  // s0

    if (!(g_1fab3c1 & 1))
    {
        sub_f7d92c(&g_1ef4170);
        g_1fab3c1 = 1;
    }
    v0 = sub_f7db70(g_1ef4170);
    Object__ctor(v0, 0);
    p = v0;
    p->field_10 = 0;
    p->field_30 = a0;
    sub_f7d8d0((struct bl_LoadingScreenUI_Recovered *)&p->field_30, a0);
    ptr = p;
    ptr->field_28 = a1;
    sub_f7d8d0((struct bl_LoadingScreenUI_Recovered *)&ptr->field_28, a1);
    ptr->field_20 = v3;
    return ptr;
}
```

## `bl_LoadingScreenUI.get_Source` — RVA `0xc78394`

- Decompiled symbol: `bl_LoadingScreenUI_get_Source`
- Metadata signature: `private AudioSource get_Source() { }`
- Native interval: `292` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[216];
    long long field_d8;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern long long g_1efcf18;
extern long long g_1efea78;
extern char g_1fab3c3;

long long bl_LoadingScreenUI_get_Source(struct_1 *p)
{
    struct_1 *ptr;  // x19
    long long v1;  // x0
    long long v2;  // x0

    if (!(g_1fab3c3 & 1))
    {
        sub_f7d92c(&g_1efcf18);
        sub_f7d92c(&g_1efea78);
        sub_f7d92c(&g_1ef0c58);
        g_1fab3c3 = 1;
    }
    ptr = &p->field_d8;
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (!((char)Object__op_Equality(p->field_d8, 0, 0) & 1))
        return *((long long *)&ptr->padding_0[0]);
    v1 = sub_1231bc8(p, g_1efcf18);
    p->field_d8 = v1;
    sub_f7d8d0(ptr, v1);
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (((char)Object__op_Equality(p->field_d8, 0, 0) & 1))
    {
        if (Component__get_gameObject(p, 0))
        {
            v2 = sub_124913c();
            *((long long *)&ptr->padding_0[0]) = v2;
            sub_f7d8d0(ptr, v2);
            if (!*((long long *)&ptr->padding_0[0]))
                sub_f7db74();
            AudioSource__set_playOnAwake(*((long long *)&ptr->padding_0[0]), 0, 0);
        }
        else
        {
            sub_f7db74();
        }
    }
    return *((long long *)&ptr->padding_0[0]);
}
```

## `bl_LoadingScreenUI.Start` — RVA `0xc784b8`

- Decompiled symbol: `bl_LoadingScreenUI_Start`
- Metadata signature: `private void Start() { }`
- Native interval: `164` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern long long g_1eeddc8;
extern struct_0 *g_1ef14f0;
extern long long g_1f03f30;
extern char g_1fab3b6;

void bl_LoadingScreenUI_Start(long long a0)
{
    unsigned long long v6;  // x30
    unsigned long long v7;  // x23
    unsigned long long v8;  // x22
    unsigned long long v9;  // x21
    unsigned long long v10;  // x20
    unsigned long long v11;  // x19
    long long v12;  // x0
    unsigned long long v0;  // [bp-0x30]
    unsigned long long v1;  // [bp-0x28]
    unsigned long long v2;  // [bp-0x20]
    unsigned long long v3;  // [bp-0x18]
    unsigned long long v4;  // [bp-0x10]
    unsigned long long v5;  // [bp-0x8]

    v0 = v6;
    v1 = v7;
    v2 = v8;
    v3 = v9;
    v4 = v10;
    v5 = v11;
    if (!(g_1fab3b6 & 1))
    {
        sub_f7d92c(&g_1ef14f0);
        sub_f7d92c(&g_1eeddc8);
        sub_f7d92c(&g_1f03f30);
        g_1fab3b6 = 1;
    }
    v12 = sub_f7db70(g_1eeddc8);
    sub_1638640(v12, a0, g_1f03f30, 0);
    if (!g_1ef14f0->field_e0)
        sub_f7da5c(g_1ef14f0);
}
```

## `bl_LoadingScreenUI.OnDestroy` — RVA `0xc7855c`

- Decompiled symbol: `bl_LoadingScreenUI_OnDestroy`
- Metadata signature: `private void OnDestroy() { }`
- Native interval: `164` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern long long g_1eeddc8;
extern struct_0 *g_1ef14f0;
extern long long g_1f03f30;
extern char g_1fab3b7;

void bl_LoadingScreenUI_OnDestroy(long long a0)
{
    unsigned long long v6;  // x30
    unsigned long long v7;  // x23
    unsigned long long v8;  // x22
    unsigned long long v9;  // x21
    unsigned long long v10;  // x20
    unsigned long long v11;  // x19
    long long v12;  // x0
    unsigned long long v0;  // [bp-0x30]
    unsigned long long v1;  // [bp-0x28]
    unsigned long long v2;  // [bp-0x20]
    unsigned long long v3;  // [bp-0x18]
    unsigned long long v4;  // [bp-0x10]
    unsigned long long v5;  // [bp-0x8]

    v0 = v6;
    v1 = v7;
    v2 = v8;
    v3 = v9;
    v4 = v10;
    v5 = v11;
    if (!(g_1fab3b7 & 1))
    {
        sub_f7d92c(&g_1ef14f0);
        sub_f7d92c(&g_1eeddc8);
        sub_f7d92c(&g_1f03f30);
        g_1fab3b7 = 1;
    }
    v12 = sub_f7db70(g_1eeddc8);
    sub_1638640(v12, a0, g_1f03f30, 0);
    if (!g_1ef14f0->field_e0)
        sub_f7da5c(g_1ef14f0);
}
```

## `bl_LoadingScreenUI.OnSceneChange` — RVA `0xc78600`

- Decompiled symbol: `bl_LoadingScreenUI_OnSceneChange`
- Metadata signature: `private void OnSceneChange(Scene from, Scene to) { }`
- Native interval: `32` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[96];
    unsigned long long field_60;
} struct_0;

void bl_LoadingScreenUI_OnSceneChange(struct_0 *a0)
{
    unsigned long long v1;  // x30
    unsigned long long v0;  // [bp-0x10]

    v0 = v1;
    if (a0->field_60)
    {
        GameObject__SetActive();
        return;
    }
    sub_f7db74(0);
}
```

## `bl_LoadingScreenUI.LoadingRotator` — RVA `0xc78620`

- Decompiled symbol: `bl_LoadingScreenUI_LoadingRotator`
- Metadata signature: `private void LoadingRotator() { }`
- Native interval: `276` bytes
- Result: `pseudocode`
- Heuristic layout hint: `bl_LoadingScreenUI_Recovered` matched 2 offsets against `bl_LoadingScreenUI` metadata (confidence 1.00).

```c
typedef struct bl_LoadingScreenUI_Recovered {
    char padding_0[120];
    long long LoadingCircle;
    char padding_80[48];
    struct struct_1 *m_SceneLoader;
} bl_LoadingScreenUI_Recovered;

typedef struct struct_1 {
    char padding_0[48];
    char field_30;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern long long g_1ef22e8;
extern char g_1fab3b9;
extern char g_1fab3e3;

long long bl_LoadingScreenUI_LoadingRotator(struct_2 *ptr)
{
    long long v0;  // x0
    long long v1;  // x20

    if (!(g_1fab3b9 & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab3b9 = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v0 = Object__op_Equality(ptr->field_78, 0, 0);
    if (((char)v0 & 1))
        return v0;
    v1 = ptr->field_78;
    if (!g_1fab3e3)
    {
        sub_f7d92c(&g_1ef22e8);
        g_1fab3e3 = 1;
    }
    if (ptr->field_b0)
    {
        if (ptr->field_b0->field_30)
            Time__get_deltaTime(0);
        else
            Time__get_unscaledDeltaTime(0);
    }
    sub_f7db74();
}
```

## `bl_LoadingScreenUI.FadeAudio` — RVA `0xc78734`

- Decompiled symbol: `bl_LoadingScreenUI_FadeAudio`
- Metadata signature: `private IEnumerator FadeAudio(bool FadeIn) { }`
- Native interval: `128` bytes
- Result: `pseudocode`
- Heuristic layout hint: `bl_LoadingScreenUI_Recovered` matched 2 offsets against `bl_LoadingScreenUI` metadata (confidence 0.67).

```c
typedef struct bl_LoadingScreenUI_Recovered {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[12];
    long long SceneNameText;
    char DescriptionText;
} bl_LoadingScreenUI_Recovered;

extern long long g_1ef4160;
extern char g_1fab3be;

struct_0 * bl_LoadingScreenUI_FadeAudio(long long a0, char a1)
{
    struct_0 *v0;  // x20
    struct_0 *ptr;  // x0

    if (!(g_1fab3be & 1))
    {
        sub_f7d92c(&g_1ef4160);
        g_1fab3be = 1;
    }
    v0 = sub_f7db70(g_1ef4160);
    Object__ctor(v0, 0);
    ptr = v0;
    ptr->field_10 = 0;
    ptr->field_20 = a0;
    sub_f7d8d0((struct bl_LoadingScreenUI_Recovered *)&ptr->field_20, a0);
    ptr->field_28 = a1 & 1;
    return ptr;
}
```

## `bl_LoadingScreenUI.LoadNextSceneIE` — RVA `0xc787b4`

- Decompiled symbol: `bl_LoadingScreenUI_LoadNextSceneIE`
- Metadata signature: `private IEnumerator LoadNextSceneIE() { }`
- Native interval: `108` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[12];
    long long field_20;
} struct_0;

extern long long g_1ef4178;
extern char g_1fab3c0;

struct_0 * bl_LoadingScreenUI_LoadNextSceneIE(long long a0)
{
    struct_0 *v0;  // x20
    struct_0 *ptr;  // x0

    if (!(g_1fab3c0 & 1))
    {
        sub_f7d92c(&g_1ef4178);
        g_1fab3c0 = 1;
    }
    v0 = sub_f7db70(g_1ef4178);
    Object__ctor(v0, 0);
    ptr = v0;
    ptr->field_10 = 0;
    ptr->field_20 = a0;
    sub_f7d8d0((struct struct_0 *)&ptr->field_20, a0);
    return ptr;
}
```

## `bl_LoadingScreenUI.BackgroundTransition` — RVA `0xc78820`

- Decompiled symbol: `bl_LoadingScreenUI_BackgroundTransition`
- Metadata signature: `private IEnumerator BackgroundTransition() { }`
- Native interval: `108` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[12];
    long long field_20;
} struct_0;

extern long long g_1ef4158;
extern char g_1fab3bc;

struct_0 * bl_LoadingScreenUI_BackgroundTransition(long long a0)
{
    struct_0 *v0;  // x20
    struct_0 *ptr;  // x0

    if (!(g_1fab3bc & 1))
    {
        sub_f7d92c(&g_1ef4158);
        g_1fab3bc = 1;
    }
    v0 = sub_f7db70(g_1ef4158);
    Object__ctor(v0, 0);
    ptr = v0;
    ptr->field_10 = 0;
    ptr->field_20 = a0;
    sub_f7d8d0((struct struct_0 *)&ptr->field_20, a0);
    return ptr;
}
```

## `bl_LoadingScreenUI.TipsLoop` — RVA `0xc7888c`

- Decompiled symbol: `bl_LoadingScreenUI_TipsLoop`
- Metadata signature: `private IEnumerator TipsLoop() { }`
- Native interval: `108` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[12];
    long long field_20;
} struct_0;

extern long long g_1ef4180;
extern char g_1fab3bd;

struct_0 * bl_LoadingScreenUI_TipsLoop(long long a0)
{
    struct_0 *v0;  // x20
    struct_0 *ptr;  // x0

    if (!(g_1fab3bd & 1))
    {
        sub_f7d92c(&g_1ef4180);
        g_1fab3bd = 1;
    }
    v0 = sub_f7db70(g_1ef4180);
    Object__ctor(v0, 0);
    ptr = v0;
    ptr->field_10 = 0;
    ptr->field_20 = a0;
    sub_f7d8d0((struct struct_0 *)&ptr->field_20, a0);
    return ptr;
}
```

## `bl_LoadingScreenUI.<BackgroundTransition>d__38.ctor` — RVA `0xc788f8`

- Decompiled symbol: `bl_LoadingScreenUI_BackgroundTransition_d__38_ctor`
- Metadata signature: `public void .ctor(int <>1__state) { }`
- Native interval: `40` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

void bl_LoadingScreenUI_BackgroundTransition_d__38_ctor(struct_0 *ptr, unsigned int a1)
{
    Object__ctor();
    ptr->field_10 = a1;
    return;
}
```

## `bl_LoadingScreenUI.<TipsLoop>d__39.ctor` — RVA `0xc78920`

- Decompiled symbol: `bl_LoadingScreenUI_TipsLoop_d__39_ctor`
- Metadata signature: `public void .ctor(int <>1__state) { }`
- Native interval: `40` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

void bl_LoadingScreenUI_TipsLoop_d__39_ctor(struct_0 *ptr, unsigned int a1)
{
    Object__ctor();
    ptr->field_10 = a1;
    return;
}
```

## `bl_LoadingScreenUI.<FadeAudio>d__40.ctor` — RVA `0xc78948`

- Decompiled symbol: `bl_LoadingScreenUI_FadeAudio_d__40_ctor`
- Metadata signature: `public void .ctor(int <>1__state) { }`
- Native interval: `40` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

void bl_LoadingScreenUI_FadeAudio_d__40_ctor(struct_0 *ptr, unsigned int a1)
{
    Object__ctor();
    ptr->field_10 = a1;
    return;
}
```

## `bl_LoadingScreenUI.WaitNextTip` — RVA `0xc78970`

- Decompiled symbol: `bl_LoadingScreenUI_WaitNextTip`
- Metadata signature: `private IEnumerator WaitNextTip(float t) { }`
- Native interval: `124` bytes
- Result: `pseudocode`
- Heuristic layout hint: `bl_LoadingScreenUI_Recovered` matched 2 offsets against `bl_LoadingScreenUI` metadata (confidence 0.67).

```c
typedef struct bl_LoadingScreenUI_Recovered {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[12];
    long long SceneNameText;
    unsigned int DescriptionText;
} bl_LoadingScreenUI_Recovered;

extern long long g_1ef4188;
extern char g_1fab3bf;

struct_0 * bl_LoadingScreenUI_WaitNextTip(long long a0)
{
    struct_0 *v0;  // x20
    struct_0 *ptr;  // x0
    unsigned int v2;  // s0

    if (!(g_1fab3bf & 1))
    {
        sub_f7d92c(&g_1ef4188);
        g_1fab3bf = 1;
    }
    v0 = sub_f7db70(g_1ef4188);
    Object__ctor(v0, 0);
    ptr = v0;
    ptr->field_10 = 0;
    ptr->field_20 = a0;
    sub_f7d8d0((struct bl_LoadingScreenUI_Recovered *)&ptr->field_20, a0);
    ptr->field_28 = v2;
    return ptr;
}
```

## `bl_LoadingScreenUI.<WaitNextTip>d__41.ctor` — RVA `0xc789ec`

- Decompiled symbol: `bl_LoadingScreenUI_WaitNextTip_d__41_ctor`
- Metadata signature: `public void .ctor(int <>1__state) { }`
- Native interval: `40` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

void bl_LoadingScreenUI_WaitNextTip_d__41_ctor(struct_0 *ptr, unsigned int a1)
{
    Object__ctor();
    ptr->field_10 = a1;
    return;
}
```

## `bl_LoadingScreenUI.<LoadNextSceneIE>d__42.ctor` — RVA `0xc78a14`

- Decompiled symbol: `bl_LoadingScreenUI_LoadNextSceneIE_d__42_ctor`
- Metadata signature: `public void .ctor(int <>1__state) { }`
- Native interval: `40` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

void bl_LoadingScreenUI_LoadNextSceneIE_d__42_ctor(struct_0 *ptr, unsigned int a1)
{
    Object__ctor();
    ptr->field_10 = a1;
    return;
}
```

## `bl_LoadingScreenUI.<FadeOutCanvas>d__43.ctor` — RVA `0xc78a3c`

- Decompiled symbol: `bl_LoadingScreenUI_FadeOutCanvas_d__43_ctor`
- Metadata signature: `public void .ctor(int <>1__state) { }`
- Native interval: `40` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

void bl_LoadingScreenUI_FadeOutCanvas_d__43_ctor(struct_0 *ptr, unsigned int a1)
{
    Object__ctor();
    ptr->field_10 = a1;
    return;
}
```

## `bl_LoadingScreenUI.FadeInCanvas` — RVA `0xc78a64`

- Decompiled symbol: `bl_LoadingScreenUI_FadeInCanvas`
- Metadata signature: `private IEnumerator FadeInCanvas(CanvasGroup alpha, float delay = 0.0) { }`
- Native interval: `152` bytes
- Result: `pseudocode`
- Heuristic layout hint: `bl_LoadingScreenUI_Recovered` matched 3 offsets against `bl_LoadingScreenUI` metadata (confidence 0.75).

```c
typedef struct bl_LoadingScreenUI_Recovered {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[12];
    unsigned int SceneNameText;
    char padding_24[4];
    long long DescriptionText;
    long long ProgressText;
} bl_LoadingScreenUI_Recovered;

extern long long g_1ef4168;
extern char g_1fab3c2;

struct_0 * bl_LoadingScreenUI_FadeInCanvas(long long a0, long long a1)
{
    struct_0 *v0;  // x21
    struct_0 *p;  // x0
    struct_0 *ptr;  // x0
    unsigned int v3;  // s0

    if (!(g_1fab3c2 & 1))
    {
        sub_f7d92c(&g_1ef4168);
        g_1fab3c2 = 1;
    }
    v0 = sub_f7db70(g_1ef4168);
    Object__ctor(v0, 0);
    p = v0;
    p->field_10 = 0;
    p->field_30 = a0;
    sub_f7d8d0((struct bl_LoadingScreenUI_Recovered *)&p->field_30, a0);
    ptr = p;
    ptr->field_28 = a1;
    sub_f7d8d0((struct bl_LoadingScreenUI_Recovered *)&ptr->field_28, a1);
    ptr->field_20 = v3;
    return ptr;
}
```

## `bl_LoadingScreenUI.<FadeInCanvas>d__44.ctor` — RVA `0xc78afc`

- Decompiled symbol: `bl_LoadingScreenUI_FadeInCanvas_d__44_ctor`
- Metadata signature: `public void .ctor(int <>1__state) { }`
- Native interval: `40` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

void bl_LoadingScreenUI_FadeInCanvas_d__44_ctor(struct_0 *ptr, unsigned int a1)
{
    Object__ctor();
    ptr->field_10 = a1;
    return;
}
```

## `bl_LoadingScreenUI.get_DeltaTime` — RVA `0xc78b24`

- Decompiled symbol: `bl_LoadingScreenUI_get_DeltaTime`
- Metadata signature: `public float get_DeltaTime() { }`
- Native interval: `48` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[176];
    struct struct_0 *field_b0;
} struct_1;

typedef struct struct_0 {
    char padding_0[48];
    char field_30;
} struct_0;

void bl_LoadingScreenUI_get_DeltaTime(struct_1 *a0)
{
    unsigned long long v1;  // x30
    unsigned long long v0;  // [bp-0x10]

    v0 = v1;
    if (a0->field_b0)
    {
        if (a0->field_b0->field_30)
        {
            Time__get_deltaTime();
            return;
        }
        Time__get_unscaledDeltaTime();
        return;
    }
    sub_f7db74();
}
```

## `bl_LoadingScreenUI.ctor` — RVA `0xc78b54`

- Decompiled symbol: `bl_LoadingScreenUI_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `136` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[192];
    long long field_c0;
} struct_0;

extern long long g_1eed828;
extern long long g_1ef85b8;
extern char g_1fab3c4;

void bl_LoadingScreenUI_ctor(struct_0 *ptr)
{
    unsigned long long v5;  // x30
    unsigned long long v6;  // x22
    unsigned long long v7;  // x21
    unsigned long long v8;  // x20
    unsigned long long v9;  // x19
    long long v10;  // x20
    unsigned long long v0;  // [bp-0x30]
    unsigned long long v1;  // [bp-0x20]
    unsigned long long v2;  // [bp-0x18]
    unsigned long long v3;  // [bp-0x10]
    unsigned long long v4;  // [bp-0x8]

    v0 = v5;
    v1 = v6;
    v2 = v7;
    v3 = v8;
    v4 = v9;
    if (!(g_1fab3c4 & 1))
    {
        sub_f7d92c(&g_1ef85b8);
        sub_f7d92c(&g_1eed828);
        g_1fab3c4 = 1;
    }
    v10 = sub_f7db70(g_1eed828);
    sub_14a2b64(v10, g_1ef85b8);
    ptr->field_c0 = v10;
    sub_f7d8d0((struct struct_0 *)&ptr->field_c0, v10);
    MonoBehaviour__ctor();
    return;
}
```

## `bl_LoadingScreenUI.<BackgroundTransition>d__38.Dispose` — RVA `0xc78bdc`

- Decompiled symbol: `bl_LoadingScreenUI_BackgroundTransition_d__38_Dispose`
- Metadata signature: `private void System.IDisposable.Dispose() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long bl_LoadingScreenUI_BackgroundTransition_d__38_Dispose(void)
{
    unsigned long v0;  // x0

    return v0;
}
```

## `bl_LoadingScreenUI.<BackgroundTransition>d__38.MoveNext` — RVA `0xc78be0`

- Decompiled symbol: `bl_LoadingScreenUI_BackgroundTransition_d__38_MoveNext`
- Metadata signature: `private bool MoveNext() { }`
- Native interval: `688` bytes
- Result: `pseudocode`

```c
extern long long g_1ef2430;
extern long long g_1ef2440;
extern long long g_1ef85c8;
extern long long g_1ef85d0;
extern char g_1fab3c5;
extern char g_852273;

unsigned int bl_LoadingScreenUI_BackgroundTransition_d__38_MoveNext(unsigned long a0)
{
    if (!(g_1fab3c5 & 1))
    {
        sub_f7d92c(&g_1ef85c8);
        sub_f7d92c(&g_1ef85d0);
        sub_f7d92c(&g_1ef2430);
        sub_f7d92c(&g_1ef2440);
        g_1fab3c5 = 1;
    }
    if (4 < *((int *)(a0 + 16)))
        return 0;
    goto sub_1078c5c + (&g_852273)[*((int *)(a0 + 16))] * 4;
}
```

## `bl_LoadingScreenUI.<BackgroundTransition>d__38.get_Current` — RVA `0xc78e90`

- Decompiled symbol: `bl_LoadingScreenUI_BackgroundTransition_d__38_get_Current`
- Metadata signature: `private object System.Collections.Generic.IEnumerator<System.Object>.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long bl_LoadingScreenUI_BackgroundTransition_d__38_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```

## `bl_LoadingScreenUI.<BackgroundTransition>d__38.Reset` — RVA `0xc78e98`

- Decompiled symbol: `bl_LoadingScreenUI_BackgroundTransition_d__38_Reset`
- Metadata signature: `private void System.Collections.IEnumerator.Reset() { }`
- Native interval: `56` bytes
- Result: `pseudocode`

```c
extern long long g_1ef0bd8;
extern long long g_1f054d8;

void bl_LoadingScreenUI_BackgroundTransition_d__38_Reset(void)
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
    sub_f7da4c(v4, sub_f7d940(&g_1f054d8));
}
```

## `bl_LoadingScreenUI.<BackgroundTransition>d__38.get_Current` — RVA `0xc78ed0`

- Decompiled symbol: `bl_LoadingScreenUI_BackgroundTransition_d__38_get_Current`
- Metadata signature: `private object System.Collections.IEnumerator.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long bl_LoadingScreenUI_BackgroundTransition_d__38_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```

## `bl_LoadingScreenUI.<FadeAudio>d__40.Dispose` — RVA `0xc78ed8`

- Decompiled symbol: `bl_LoadingScreenUI_FadeAudio_d__40_Dispose`
- Metadata signature: `private void System.IDisposable.Dispose() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long bl_LoadingScreenUI_FadeAudio_d__40_Dispose(void)
{
    unsigned long v0;  // x0

    return v0;
}
```

## `bl_LoadingScreenUI.<FadeAudio>d__40.MoveNext` — RVA `0xc78edc`

- Decompiled symbol: `bl_LoadingScreenUI_FadeAudio_d__40_MoveNext`
- Metadata signature: `private bool MoveNext() { }`
- Native interval: `544` bytes
- Result: `pseudocode`

```c
typedef struct struct_3 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[12];
    struct struct_2 *field_20;
    char field_28;
} struct_3;

typedef struct struct_2 {
    char padding_0[176];
    struct struct_1 *field_b0;
} struct_2;

typedef struct struct_1 {
    char padding_0[136];
    long long field_88;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern long long g_1ef2430;
extern char g_1fab3c6;

unsigned int bl_LoadingScreenUI_FadeAudio_d__40_MoveNext(struct_3 *ptr)
{
    unsigned int flag;  // w8
    struct_2 *v1;  // x20

    if (!(g_1fab3c6 & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c(&g_1ef2430);
        g_1fab3c6 = 1;
    }
    flag = ptr->field_10;
    v1 = ptr->field_20;
    if (flag == 2)
    {
        ptr->field_10 = 4294967295;
        if (v1)
            bl_LoadingScreenUI__get_Source(v1);
    }
    else if (flag == 1)
    {
        ptr->field_10 = 4294967295;
        if (v1)
            bl_LoadingScreenUI__get_Source(v1);
    }
    else if (!flag)
    {
        ptr->field_10 = 4294967295;
        if (v1 && v1->field_b0)
        {
            if (!g_1ef0c58->field_e0)
                sub_f7da5c(g_1ef0c58);
            if (((char)Object__op_Equality(v1->field_b0->field_88, 0, 0) & 1))
            {
                return 0;
            }
            else if (!ptr->field_28)
            {
                bl_LoadingScreenUI__get_Source(v1);
            }
            else
            {
                bl_LoadingScreenUI__get_Source(v1);
            }
        }
    }
    else
    {
        return 0;
    }
    sub_f7db74();
}
```

## `bl_LoadingScreenUI.<FadeAudio>d__40.get_Current` — RVA `0xc790fc`

- Decompiled symbol: `bl_LoadingScreenUI_FadeAudio_d__40_get_Current`
- Metadata signature: `private object System.Collections.Generic.IEnumerator<System.Object>.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long bl_LoadingScreenUI_FadeAudio_d__40_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```

## `bl_LoadingScreenUI.<FadeAudio>d__40.Reset` — RVA `0xc79104`

- Decompiled symbol: `bl_LoadingScreenUI_FadeAudio_d__40_Reset`
- Metadata signature: `private void System.Collections.IEnumerator.Reset() { }`
- Native interval: `56` bytes
- Result: `pseudocode`

```c
extern long long g_1ef0bd8;
extern long long g_1f054e0;

void bl_LoadingScreenUI_FadeAudio_d__40_Reset(void)
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
    sub_f7da4c(v4, sub_f7d940(&g_1f054e0));
}
```

## `bl_LoadingScreenUI.<FadeAudio>d__40.get_Current` — RVA `0xc7913c`

- Decompiled symbol: `bl_LoadingScreenUI_FadeAudio_d__40_get_Current`
- Metadata signature: `private object System.Collections.IEnumerator.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long bl_LoadingScreenUI_FadeAudio_d__40_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```

## `bl_LoadingScreenUI.<FadeInCanvas>d__44.Dispose` — RVA `0xc79144`

- Decompiled symbol: `bl_LoadingScreenUI_FadeInCanvas_d__44_Dispose`
- Metadata signature: `private void System.IDisposable.Dispose() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long bl_LoadingScreenUI_FadeInCanvas_d__44_Dispose(void)
{
    unsigned long v0;  // x0

    return v0;
}
```

## `bl_LoadingScreenUI.<FadeInCanvas>d__44.MoveNext` — RVA `0xc79148`

- Decompiled symbol: `bl_LoadingScreenUI_FadeInCanvas_d__44_MoveNext`
- Metadata signature: `private bool MoveNext() { }`
- Native interval: `300` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[4];
    long long field_18;
    char padding_20[8];
    long long field_28;
    struct struct_1 *field_30;
} struct_0;

typedef struct struct_1 {
    char padding_0[176];
    struct struct_0 *field_b0;
} struct_1;

typedef struct struct_0 {
    char padding_0[48];
    char field_30;
} struct_0;

extern long long g_1ef2440;
extern char g_1fab3c7;

unsigned int bl_LoadingScreenUI_FadeInCanvas_d__44_MoveNext(struct_0 *ptr)
{
    long long v0;  // x0
    struct_1 *v1;  // x20
    unsigned int v2;  // s0
    unsigned long v3;  // 4125
    long long v4;  // x20

    if (!(g_1fab3c7 & 1))
    {
        sub_f7d92c(&g_1ef2440);
        g_1fab3c7 = 1;
    }
    if (2 > ptr->field_10 - 1)
    {
        v0 = ptr->field_28;
        v1 = ptr->field_30;
        ptr->field_10 = 4294967295;
        if (v0)
        {
            v0 = CanvasGroup__get_alpha(v0, 0);
            v3 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v2, 0x3f800000)) >> 5 & 3 | (unsigned long long)(CmpF(v2, 0x3f800000) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v2, 0x3f800000)) >> 5 & 3 | (unsigned long long)(CmpF(v2, 0x3f800000) & 1)) & ((unsigned long long)(char)(CmpF(v2, 0x3f800000)) >> 5 & 3 | (unsigned long long)(CmpF(v2, 0x3f800000) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
            if ((char)v3)
                return 0;
            if (ptr->field_28)
            {
                v0 = CanvasGroup__get_alpha(ptr->field_28, 0);
                if (v1)
                    bl_LoadingScreenUI__get_DeltaTime(v1); /* do not return */
            }
        }
        sub_f7db74(v0);
    }
    else if (!ptr->field_10)
    {
        ptr->field_10 = 4294967295;
        v4 = sub_f7db70(g_1ef2440);
        WaitForSeconds__ctor(v4, 0);
        ptr->field_18 = v4;
        sub_f7d8d0((struct struct_0 *)&ptr->field_18, v4);
        ptr->field_10 = 1;
        return 1;
    }
    else
    {
        return 0;
    }
}
```

## `bl_LoadingScreenUI.<FadeInCanvas>d__44.get_Current` — RVA `0xc79274`

- Decompiled symbol: `bl_LoadingScreenUI_FadeInCanvas_d__44_get_Current`
- Metadata signature: `private object System.Collections.Generic.IEnumerator<System.Object>.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long bl_LoadingScreenUI_FadeInCanvas_d__44_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```

## `bl_LoadingScreenUI.<FadeInCanvas>d__44.Reset` — RVA `0xc7927c`

- Decompiled symbol: `bl_LoadingScreenUI_FadeInCanvas_d__44_Reset`
- Metadata signature: `private void System.Collections.IEnumerator.Reset() { }`
- Native interval: `56` bytes
- Result: `pseudocode`

```c
extern long long g_1ef0bd8;
extern long long g_1f054e8;

void bl_LoadingScreenUI_FadeInCanvas_d__44_Reset(void)
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
    sub_f7da4c(v4, sub_f7d940(&g_1f054e8));
}
```

## `bl_LoadingScreenUI.<FadeInCanvas>d__44.get_Current` — RVA `0xc792b4`

- Decompiled symbol: `bl_LoadingScreenUI_FadeInCanvas_d__44_get_Current`
- Metadata signature: `private object System.Collections.IEnumerator.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long bl_LoadingScreenUI_FadeInCanvas_d__44_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```

## `bl_LoadingScreenUI.<FadeOutCanvas>d__43.Dispose` — RVA `0xc792bc`

- Decompiled symbol: `bl_LoadingScreenUI_FadeOutCanvas_d__43_Dispose`
- Metadata signature: `private void System.IDisposable.Dispose() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long bl_LoadingScreenUI_FadeOutCanvas_d__43_Dispose(void)
{
    unsigned long v0;  // x0

    return v0;
}
```

## `bl_LoadingScreenUI.<FadeOutCanvas>d__43.MoveNext` — RVA `0xc792c0`

- Decompiled symbol: `bl_LoadingScreenUI_FadeOutCanvas_d__43_MoveNext`
- Metadata signature: `private bool MoveNext() { }`
- Native interval: `296` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[4];
    long long field_18;
    char padding_20[8];
    long long field_28;
    struct struct_1 *field_30;
} struct_0;

typedef struct struct_1 {
    char padding_0[176];
    struct struct_0 *field_b0;
} struct_1;

typedef struct struct_0 {
    char padding_0[48];
    char field_30;
} struct_0;

extern long long g_1ef2440;
extern char g_1fab3c8;

unsigned int bl_LoadingScreenUI_FadeOutCanvas_d__43_MoveNext(struct_0 *ptr)
{
    long long v0;  // x0
    struct_1 *v1;  // x20
    unsigned int v2;  // s0
    unsigned long v3;  // 4125
    long long v4;  // x20

    if (!(g_1fab3c8 & 1))
    {
        sub_f7d92c(&g_1ef2440);
        g_1fab3c8 = 1;
    }
    if (2 > ptr->field_10 - 1)
    {
        v0 = ptr->field_28;
        v1 = ptr->field_30;
        ptr->field_10 = 4294967295;
        if (v0)
        {
            v0 = CanvasGroup__get_alpha(v0, 0);
            v3 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v2, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v2, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v2, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v2, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v2, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v2, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
            if ((char)v3)
                return 0;
            if (ptr->field_28)
            {
                v0 = CanvasGroup__get_alpha(ptr->field_28, 0);
                if (v1)
                    bl_LoadingScreenUI__get_DeltaTime(v1); /* do not return */
            }
        }
        sub_f7db74(v0);
    }
    else if (!ptr->field_10)
    {
        ptr->field_10 = 4294967295;
        v4 = sub_f7db70(g_1ef2440);
        WaitForSeconds__ctor(v4, 0);
        ptr->field_18 = v4;
        sub_f7d8d0((struct struct_0 *)&ptr->field_18, v4);
        ptr->field_10 = 1;
        return 1;
    }
    else
    {
        return 0;
    }
}
```

## `bl_LoadingScreenUI.<FadeOutCanvas>d__43.get_Current` — RVA `0xc793e8`

- Decompiled symbol: `bl_LoadingScreenUI_FadeOutCanvas_d__43_get_Current`
- Metadata signature: `private object System.Collections.Generic.IEnumerator<System.Object>.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long bl_LoadingScreenUI_FadeOutCanvas_d__43_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```

## `bl_LoadingScreenUI.<FadeOutCanvas>d__43.Reset` — RVA `0xc793f0`

- Decompiled symbol: `bl_LoadingScreenUI_FadeOutCanvas_d__43_Reset`
- Metadata signature: `private void System.Collections.IEnumerator.Reset() { }`
- Native interval: `56` bytes
- Result: `pseudocode`

```c
extern long long g_1ef0bd8;
extern long long g_1f054f0;

void bl_LoadingScreenUI_FadeOutCanvas_d__43_Reset(void)
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
    sub_f7da4c(v4, sub_f7d940(&g_1f054f0));
}
```

## `bl_LoadingScreenUI.<FadeOutCanvas>d__43.get_Current` — RVA `0xc79428`

- Decompiled symbol: `bl_LoadingScreenUI_FadeOutCanvas_d__43_get_Current`
- Metadata signature: `private object System.Collections.IEnumerator.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long bl_LoadingScreenUI_FadeOutCanvas_d__43_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```

## `bl_LoadingScreenUI.<LoadNextSceneIE>d__42.Dispose` — RVA `0xc79430`

- Decompiled symbol: `bl_LoadingScreenUI_LoadNextSceneIE_d__42_Dispose`
- Metadata signature: `private void System.IDisposable.Dispose() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long bl_LoadingScreenUI_LoadNextSceneIE_d__42_Dispose(void)
{
    unsigned long v0;  // x0

    return v0;
}
```

## `bl_LoadingScreenUI.<LoadNextSceneIE>d__42.MoveNext` — RVA `0xc79434`

- Decompiled symbol: `bl_LoadingScreenUI_LoadNextSceneIE_d__42_MoveNext`
- Metadata signature: `private bool MoveNext() { }`
- Native interval: `256` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[12];
    struct struct_1 *field_20;
} struct_2;

typedef struct struct_1 {
    char padding_0[136];
    long long field_88;
    char padding_90[32];
    struct struct_0 *field_b0;
} struct_1;

typedef struct struct_0 {
    char padding_0[160];
    long long field_a0;
} struct_0;

unsigned int bl_LoadingScreenUI_LoadNextSceneIE_d__42_MoveNext(struct_2 *ptr)
{
    struct_1 *p;  // x20
    unsigned int v1;  // s0
    unsigned long v2;  // 4125
    struct_0 *v3;  // x8

    p = ptr->field_20;
    if (ptr->field_10 != 1)
    {
        if (ptr->field_10)
            return 0;
        ptr->field_10 = 4294967295;
        if (p && p->field_88)
        {
            v1 = 0;
            CanvasGroup__set_alpha(p->field_88, 0);
LABEL_1079488:
            if (p->field_88)
            {
                CanvasGroup__get_alpha(p->field_88, 0);
                v2 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v1, 0x3f800000)) >> 5 & 3 | (unsigned long long)(CmpF(v1, 0x3f800000) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v1, 0x3f800000)) >> 5 & 3 | (unsigned long long)(CmpF(v1, 0x3f800000) & 1)) & ((unsigned long long)(char)(CmpF(v1, 0x3f800000)) >> 5 & 3 | (unsigned long long)(CmpF(v1, 0x3f800000) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                if ((char)v2)
                {
                    v3 = p->field_b0;
                    if (v3 && v3->field_a0)
                    {
                        AsyncOperation__set_allowSceneActivation(v3->field_a0, 1, 0);
                        return 0;
                    }
                }
                else if (p->field_88)
                {
                    CanvasGroup__get_alpha(p->field_88, 0);
                    bl_LoadingScreenUI__get_DeltaTime(p); /* do not return */
                }
            }
        }
    }
    else
    {
        ptr->field_10 = 4294967295;
        if (p)
            goto LABEL_1079488;
    }
    sub_f7db74();
}
```

## `bl_LoadingScreenUI.<LoadNextSceneIE>d__42.get_Current` — RVA `0xc79534`

- Decompiled symbol: `bl_LoadingScreenUI_LoadNextSceneIE_d__42_get_Current`
- Metadata signature: `private object System.Collections.Generic.IEnumerator<System.Object>.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long bl_LoadingScreenUI_LoadNextSceneIE_d__42_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```

## `bl_LoadingScreenUI.<LoadNextSceneIE>d__42.Reset` — RVA `0xc7953c`

- Decompiled symbol: `bl_LoadingScreenUI_LoadNextSceneIE_d__42_Reset`
- Metadata signature: `private void System.Collections.IEnumerator.Reset() { }`
- Native interval: `56` bytes
- Result: `pseudocode`

```c
extern long long g_1ef0bd8;
extern long long g_1f054f8;

void bl_LoadingScreenUI_LoadNextSceneIE_d__42_Reset(void)
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
    sub_f7da4c(v4, sub_f7d940(&g_1f054f8));
}
```

## `bl_LoadingScreenUI.<LoadNextSceneIE>d__42.get_Current` — RVA `0xc79574`

- Decompiled symbol: `bl_LoadingScreenUI_LoadNextSceneIE_d__42_get_Current`
- Metadata signature: `private object System.Collections.IEnumerator.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long bl_LoadingScreenUI_LoadNextSceneIE_d__42_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```

## `bl_LoadingScreenUI.<TipsLoop>d__39.Dispose` — RVA `0xc7957c`

- Decompiled symbol: `bl_LoadingScreenUI_TipsLoop_d__39_Dispose`
- Metadata signature: `private void System.IDisposable.Dispose() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long bl_LoadingScreenUI_TipsLoop_d__39_Dispose(void)
{
    unsigned long v0;  // x0

    return v0;
}
```

## `bl_LoadingScreenUI.<TipsLoop>d__39.MoveNext` — RVA `0xc79580`

- Decompiled symbol: `bl_LoadingScreenUI_TipsLoop_d__39_MoveNext`
- Metadata signature: `private bool MoveNext() { }`
- Native interval: `772` bytes
- Result: `pseudocode`

```c
extern long long g_1ef0c58;
extern long long g_1ef8688;
extern long long g_1ef8690;
extern char g_1fab3c9;
extern char g_852278;

unsigned int bl_LoadingScreenUI_TipsLoop_d__39_MoveNext(unsigned long a0)
{
    if (!(g_1fab3c9 & 1))
    {
        sub_f7d92c(&g_1ef8688);
        sub_f7d92c(&g_1ef8690);
        sub_f7d92c(&g_1ef0c58);
        g_1fab3c9 = 1;
    }
    if (3 < *((int *)(a0 + 16)))
        return 0;
    goto sub_10795f0 + (&g_852278)[*((int *)(a0 + 16))] * 4;
}
```

## `bl_LoadingScreenUI.<TipsLoop>d__39.get_Current` — RVA `0xc79884`

- Decompiled symbol: `bl_LoadingScreenUI_TipsLoop_d__39_get_Current`
- Metadata signature: `private object System.Collections.Generic.IEnumerator<System.Object>.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long bl_LoadingScreenUI_TipsLoop_d__39_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```

## `bl_LoadingScreenUI.<TipsLoop>d__39.Reset` — RVA `0xc7988c`

- Decompiled symbol: `bl_LoadingScreenUI_TipsLoop_d__39_Reset`
- Metadata signature: `private void System.Collections.IEnumerator.Reset() { }`
- Native interval: `56` bytes
- Result: `pseudocode`

```c
extern long long g_1ef0bd8;
extern long long g_1f05500;

void bl_LoadingScreenUI_TipsLoop_d__39_Reset(void)
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
    sub_f7da4c(v4, sub_f7d940(&g_1f05500));
}
```

## `bl_LoadingScreenUI.<TipsLoop>d__39.get_Current` — RVA `0xc798c4`

- Decompiled symbol: `bl_LoadingScreenUI_TipsLoop_d__39_get_Current`
- Metadata signature: `private object System.Collections.IEnumerator.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long bl_LoadingScreenUI_TipsLoop_d__39_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```

## `bl_LoadingScreenUI.<WaitNextTip>d__41.Dispose` — RVA `0xc798cc`

- Decompiled symbol: `bl_LoadingScreenUI_WaitNextTip_d__41_Dispose`
- Metadata signature: `private void System.IDisposable.Dispose() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long bl_LoadingScreenUI_WaitNextTip_d__41_Dispose(void)
{
    unsigned long v0;  // x0

    return v0;
}
```

## `bl_LoadingScreenUI.<WaitNextTip>d__41.MoveNext` — RVA `0xc798d0`

- Decompiled symbol: `bl_LoadingScreenUI_WaitNextTip_d__41_MoveNext`
- Metadata signature: `private bool MoveNext() { }`
- Native interval: `216` bytes
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
    char padding_0[200];
    char field_c8;
} struct_0;

extern long long g_1ef2440;
extern char g_1fab3ca;

unsigned int bl_LoadingScreenUI_WaitNextTip_d__41_MoveNext(struct_1 *ptr)
{
    struct_0 *p;  // x20
    long long v1;  // x20
    struct_1 *addr;  // x19

    if (!(g_1fab3ca & 1))
    {
        sub_f7d92c(&g_1ef2440);
        g_1fab3ca = 1;
    }
    p = ptr->field_20;
    if (ptr->field_10 == 1)
    {
        ptr->field_10 = 4294967295;
        if (!p)
            sub_f7db74();
        MonoBehaviour__StartCoroutine(p, bl_LoadingScreenUI__TipsLoop(p), 0);
    }
    else if (!ptr->field_10)
    {
        ptr->field_10 = 4294967295;
        if (p)
        {
            p->field_c8 = p->field_c8 ^ 1;
            v1 = sub_f7db70(g_1ef2440);
            WaitForSeconds__ctor(v1, 0);
            ptr->field_18 = v1;
            addr = &ptr->field_18;
            sub_f7d8d0(addr, v1);
            *((unsigned int *)&addr->padding_0[8]) = 1;
            return 1;
        }
        sub_f7db74();
    }
    return 0;
}
```

## `bl_LoadingScreenUI.<WaitNextTip>d__41.get_Current` — RVA `0xc799a8`

- Decompiled symbol: `bl_LoadingScreenUI_WaitNextTip_d__41_get_Current`
- Metadata signature: `private object System.Collections.Generic.IEnumerator<System.Object>.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long bl_LoadingScreenUI_WaitNextTip_d__41_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```

## `bl_LoadingScreenUI.<WaitNextTip>d__41.Reset` — RVA `0xc799b0`

- Decompiled symbol: `bl_LoadingScreenUI_WaitNextTip_d__41_Reset`
- Metadata signature: `private void System.Collections.IEnumerator.Reset() { }`
- Native interval: `56` bytes
- Result: `pseudocode`

```c
extern long long g_1ef0bd8;
extern long long g_1f05508;

void bl_LoadingScreenUI_WaitNextTip_d__41_Reset(void)
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
    sub_f7da4c(v4, sub_f7d940(&g_1f05508));
}
```

## `bl_LoadingScreenUI.<WaitNextTip>d__41.get_Current` — RVA `0xc799e8`

- Decompiled symbol: `bl_LoadingScreenUI_WaitNextTip_d__41_get_Current`
- Metadata signature: `private object System.Collections.IEnumerator.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long bl_LoadingScreenUI_WaitNextTip_d__41_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```
